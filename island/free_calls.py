"""Z Desk: batched raw free-model calls (one owner-triggered action, N independent requests).

Born 2026-11-09 for the GPT-family free-first experiments (Luna + Terra pair
specs on the bus; owner authorization bus #2 comment 6752602689). The queue
lane runs island.z_desk CONSULTS (reviewer system prompts + verdict JSON),
which would silently change those experiments; this module makes RAW single
calls instead: one text request per spec entry (optionally with ONE
publish-safe image attached), exact prompt as written, no system prompt, no
tools/web, no retries, no model substitution, and the batch ABORTS unless
every target's live catalog pricing is verified immediately before the first
call: free models must be exactly $0 for prompt and completion; paid models
are allowed ONLY when the spec carries a "paid" block whose budget_usd is
within the hard-coded $1.00 ceiling, and only after the summed WORST-CASE
cost of all paid calls fits the budget (Luna's all-in cap rule, owner-approved
bus #2 comment 6758546640; actual reported cost is accumulated per call and
a paid call is never sent if it could take the running total over budget).
Prompts ride the PUBLIC-bus red-line (secret-shape scan shared with
island.z_desk). A failed request is receipted data; the batch continues.
Execution is sequential and recorded as such, never hidden. Trigger:
workflow_dispatch (owner click) or Route B push (Z marker file).
"""
import argparse
import base64
import hashlib
import json
import math
import os
import re
import time
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path

from island.z_desk import contains_secret

CATALOG_URL = "https://openrouter.ai/api/v1/models"
CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/:-]{0,119}$")
REASONING_EFFORTS = ("low", "medium", "high", "xhigh")
MAX_CALLS = 8
MAX_PROMPT_CHARS = 20000
MAX_IMAGE_BYTES = 4 * 1024 * 1024
IMAGE_MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
              ".webp": "image/webp", ".gif": "image/gif"}
PAID_BUDGET_CEILING_USD = 1.00
HTTP_TIMEOUT_S = 600
CATALOG_TIMEOUT_S = 30


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def catalog_get(url, timeout):
    req = urllib.request.Request(url, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def prices_of(entry):
    pricing = entry.get("pricing") or {}

    def num(v):
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    p, c = num(pricing.get("prompt")), num(pricing.get("completion"))
    return (p, c) if p is not None and c is not None else None


def price_is_zero(entry):
    prices = prices_of(entry)
    return prices is not None and prices[0] == 0.0 and prices[1] == 0.0


def supports_image(entry):
    arch = entry.get("architecture") or {}
    modalities = arch.get("input_modalities") or []
    return "image" in modalities


def worst_case_usd(entry, prompt_chars, has_image, max_tokens):
    (p, c) = prices_of(entry)
    prompt_tokens = math.ceil(prompt_chars / 3) + (2000 if has_image else 0)
    return prompt_tokens * p + max_tokens * c


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--inter-call-sleep", type=float, default=5.0)
    args = parser.parse_args()

    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    model = spec.get("model", "")
    max_tokens = spec.get("max_tokens", 450)
    calls = spec.get("calls", [])
    batch = spec.get("batch", "unnamed")
    paid = spec.get("paid") or None
    repo_root = Path.cwd()

    if paid is not None:
        if not isinstance(paid, dict):
            raise SystemExit("SPEC INVALID: paid must be an object")
        try:
            budget = float(paid.get("budget_usd"))
        except (TypeError, ValueError):
            raise SystemExit("SPEC INVALID: paid.budget_usd must be a number")
        if not 0 < budget <= PAID_BUDGET_CEILING_USD:
            raise SystemExit(
                "SPEC INVALID: paid.budget_usd must be within the hard ceiling $%.2f" % PAID_BUDGET_CEILING_USD)
    else:
        budget = None

    problems = []
    if not MODEL_ID_RE.match(model or ""):
        problems.append("bad model id")
    if not isinstance(max_tokens, int) or not 1 <= max_tokens <= 4096:
        problems.append("max_tokens must be an int in 1..4096")
    if not isinstance(calls, list) or not 1 <= len(calls) <= MAX_CALLS:
        problems.append("calls must be a list of 1..%d entries" % MAX_CALLS)
    ids = set()
    for c in calls:
        cid = c.get("id", "")
        if not cid or cid in ids:
            problems.append("call ids must be unique and non-empty")
        ids.add(cid)
        p = c.get("prompt", "")
        if not isinstance(p, str) or not p.strip():
            problems.append("call %s: empty prompt" % cid)
        if len(p) > MAX_PROMPT_CHARS:
            problems.append("call %s: prompt exceeds %d chars" % (cid, MAX_PROMPT_CHARS))
        if contains_secret(p):
            problems.append("call %s: secret-shaped text; PUBLIC bus, refusing" % cid)
        cm = c.get("model", model)
        if not MODEL_ID_RE.match(cm or ""):
            problems.append("call %s: bad per-call model id" % cid)
        ct = c.get("max_tokens", max_tokens)
        if not isinstance(ct, int) or not 1 <= ct <= 4096:
            problems.append("call %s: max_tokens must be an int in 1..4096" % cid)
        eff = c.get("reasoning_effort")
        if eff is not None and (not isinstance(eff, str) or eff not in REASONING_EFFORTS):
            problems.append("call %s: reasoning_effort must be one of %s" % (cid, list(REASONING_EFFORTS)))
        rmode = c.get("reasoning_mode")
        if rmode is not None and (not isinstance(rmode, str) or not re.match(r"^[a-z]{1,16}$", rmode)):
            problems.append("call %s: reasoning_mode must be a lowercase token" % cid)
        img = c.get("image")
        if img is not None:
            if not isinstance(img, str) or os.path.isabs(img) or ".." in img.split("/"):
                problems.append("call %s: image must be a safe repo-relative path" % cid)
            else:
                f = repo_root / img
                if not f.is_file():
                    problems.append("call %s: image file not found: %s" % (cid, img))
                elif f.suffix.lower() not in IMAGE_MIME:
                    problems.append("call %s: image must be one of %s" % (cid, sorted(IMAGE_MIME)))
                elif f.stat().st_size > MAX_IMAGE_BYTES:
                    problems.append("call %s: image exceeds %d bytes" % (cid, MAX_IMAGE_BYTES))
    api_key = os.getenv("OPENROUTER_API_KEY", "")
    if not api_key:
        problems.append("OPENROUTER_API_KEY not set")
    if problems:
        print("SPEC INVALID - nothing sent:")
        for p in problems:
            print(" -", p)
        raise SystemExit(2)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    run_id = outdir.name + "-" + uuid.uuid4().hex[:8]
    trigger = os.getenv("GITHUB_EVENT_NAME", "manual")
    events = []

    def emit(event):
        events.append(event)
        with (outdir / "bus.jsonl").open("a", encoding="utf-8") as bus:
            bus.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")

    emit({"type": "batch_start", "utc": now(), "run_id": run_id, "batch": batch,
          "trigger": trigger, "model_requested": model, "max_tokens": max_tokens,
          "calls": len(calls),
          "paid_mode": budget is not None,
          "paid_budget_usd": budget,
          "red_line": "public-bus secret-shape scan applied to every prompt"})

    # ---- Live catalog verification BEFORE any call (seats' abort rule, enforced mechanically).
    models_used = sorted({c.get("model", model) for c in calls} | {model})
    catalog_checks = {}
    paid_worst_total = 0.0
    abort_reason = None
    try:
        catalog = catalog_get(CATALOG_URL, CATALOG_TIMEOUT_S)
        by_id = {m.get("id"): m for m in catalog.get("data", [])}
        for mid in models_used:
            entry = by_id.get(mid)
            check = {"type": "catalog_check", "utc": now(), "model": mid}
            if entry is None:
                check["price_ok"] = False
                check["note"] = "model not in live catalog"
                abort_reason = "model not in live catalog: " + mid
            elif price_is_zero(entry):
                check["price_ok"] = True
                check["mode"] = "free"
                check.update({"pricing": entry.get("pricing"), "name": entry.get("name"),
                              "context_length": entry.get("context_length"),
                              "expiration_date": entry.get("expiration_date")})
            else:
                if budget is None:
                    check["price_ok"] = False
                    check["note"] = "non-zero price but spec has no paid budget block"
                    abort_reason = check["note"] + ": " + mid
                else:
                    per = sum(worst_case_usd(by_id[c.get("model", model)],
                                             len(c.get("prompt", "")), c.get("image") is not None,
                                             c.get("max_tokens", max_tokens))
                              for c in calls if c.get("model", model) == mid)
                    check["price_ok"] = True
                    check["mode"] = "paid"
                    check.update({"pricing": entry.get("pricing"), "name": entry.get("name"),
                                  "context_length": entry.get("context_length"),
                                  "worst_case_usd": round(per, 6)})
                    paid_worst_total += per
            for c in calls:
                if c.get("model", model) == mid and c.get("image") is not None:
                    if entry is not None and not supports_image(entry):
                        abort_reason = "model does not accept image input: " + mid
                        check["image_ok"] = False
                    else:
                        check["image_ok"] = True
            catalog_checks[mid] = check
            emit(check)
        if abort_reason is None and budget is not None and paid_worst_total > budget:
            abort_reason = ("paid worst-case $%.6f exceeds budget $%.6f - aborting before any call"
                            % (paid_worst_total, budget))
            emit({"type": "budget_check", "utc": now(), "ok": False,
                  "worst_case_paid_usd": round(paid_worst_total, 6), "budget_usd": budget})
        elif budget is not None:
            emit({"type": "budget_check", "utc": now(), "ok": True,
                  "worst_case_paid_usd": round(paid_worst_total, 6), "budget_usd": budget})
    except Exception as exc:  # noqa: BLE001 - abort path must receipt any failure
        abort_reason = "catalog fetch failed: " + str(exc)[:200]
        emit({"type": "catalog_check", "utc": now(), "model": "all",
              "price_ok": False, "note": abort_reason})

    results = []
    actual_paid_so_far = 0.0
    if abort_reason is None:
        for i, c in enumerate(calls, 1):
            cid, seat = c["id"], c.get("seat", "")
            prompt = c["prompt"]
            call_model = c.get("model", model)
            call_cap = c.get("max_tokens", max_tokens)
            entry = catalog_checks.get(call_model, {})
            is_paid = entry.get("mode") == "paid"
            if is_paid:
                wc = worst_case_usd(by_id[call_model], len(prompt), c.get("image") is not None, call_cap)
                if actual_paid_so_far + wc > budget:
                    emit({"type": "budget_guard_abort", "utc": now(), "index": i, "id": cid,
                          "actual_paid_so_far_usd": round(actual_paid_so_far, 6),
                          "worst_case_this_call_usd": round(wc, 6), "budget_usd": budget,
                          "note": "remaining calls not sent: budget guard"})
                    abort_reason = "budget guard: running actual + worst-case would exceed budget"
                    break
            image_note = None
            content = prompt
            if c.get("image") is not None:
                f = repo_root / c["image"]
                raw = f.read_bytes()
                mime = IMAGE_MIME[f.suffix.lower()]
                content = [{"type": "text", "text": prompt},
                           {"type": "image_url",
                            "image_url": {"url": "data:%s;base64,%s"
                                          % (mime, base64.b64encode(raw).decode("ascii"))}}]
                image_note = {"path": c["image"], "bytes": len(raw),
                              "sha256": hashlib.sha256(raw).hexdigest()}
            emit({"type": "call_start", "utc": now(), "index": i, "id": cid, "seat": seat,
                  "model": call_model, "max_tokens": call_cap,
                  "prompt_chars": len(prompt), "image": image_note,
                  "paid": is_paid,
                  "reasoning_effort": c.get("reasoning_effort"),
                  "reasoning_mode": c.get("reasoning_mode"),
                  "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest()})
            result = {"type": "call_result", "utc": now(), "index": i, "id": cid, "seat": seat,
                      "model_requested": call_model, "max_tokens": call_cap, "paid": is_paid,
                      "reasoning_effort": c.get("reasoning_effort"),
                      "reasoning_mode": c.get("reasoning_mode")}
            try:
                payload = {"model": call_model,
                           "messages": [{"role": "user", "content": content}],
                           "max_tokens": call_cap}
                call_effort = c.get("reasoning_effort")
                if call_effort:
                    payload["reasoning"] = {"effort": call_effort}
                call_mode = c.get("reasoning_mode")
                if call_mode:
                    payload.setdefault("reasoning", {})["mode"] = call_mode
                req = urllib.request.Request(
                    CHAT_URL, data=json.dumps(payload).encode("utf-8"), method="POST",
                    headers={"Content-Type": "application/json",
                             "Authorization": "Bearer " + api_key})
                t0 = time.monotonic()
                with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_S) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                elapsed = round(time.monotonic() - t0, 3)
                choice = (data.get("choices") or [{}])[0]
                message = choice.get("message") or {}
                usage = data.get("usage") or {}
                text = message.get("content")
                ok = isinstance(text, str) and bool(text.strip())
                reported_cost = None
                try:
                    reported_cost = float(usage.get("cost"))
                except (TypeError, ValueError):
                    reported_cost = None
                if is_paid and reported_cost is not None:
                    actual_paid_so_far += reported_cost
                cost_basis = ("OpenRouter usage.cost (paid; budget-guarded)" if is_paid
                              else "catalog price verified $0/$0 immediately before batch")
                result.update({
                    "status": "completed" if ok else "error_empty_response",
                    "elapsed_s": elapsed, "http": "ok",
                    "model_returned": data.get("model"),
                    "provider_returned": data.get("provider") or (data.get("details") or {}).get("provider"),
                    "response_id": data.get("id"),
                    "finish_reason": choice.get("finish_reason"),
                    "usage": {"prompt_tokens": usage.get("prompt_tokens"),
                              "completion_tokens": usage.get("completion_tokens"),
                              "total_tokens": usage.get("total_tokens")},
                    "cost_usd": reported_cost if is_paid else 0.0,
                    "cost_basis": cost_basis,
                    "text": text,
                })
            except urllib.error.HTTPError as exc:
                detail = ""
                try:
                    detail = exc.read().decode("utf-8", "replace")[:400]
                except Exception:
                    pass
                result.update({"status": "error_http_" + str(exc.code),
                               "error": detail or str(exc)[:200],
                               "cost_usd": None,
                               "cost_basis": "no completed call"})
            except Exception as exc:  # noqa: BLE001
                result.update({"status": "error", "error": str(exc)[:200],
                               "cost_usd": None,
                               "cost_basis": "no completed call"})
            results.append(result)
            emit(result)
            if i < len(calls) and args.inter_call_sleep > 0:
                time.sleep(args.inter_call_sleep)

    completed = [r for r in results if r.get("status") == "completed"]
    errored = [r for r in results if str(r.get("status", "")).startswith("error")]
    reason = "completed" if results and not errored else (
        "aborted: " + abort_reason if abort_reason is not None else
        ("partial_error" if completed else "all_errored"))
    emit({"type": "batch_stop", "utc": now(), "reason": reason,
          "completed": len(completed), "errored": len(errored),
          "total_calls": len(calls),
          "actual_paid_usd": round(actual_paid_so_far, 6),
          "paid_budget_usd": budget,
          "known_reported_cost_usd": round(sum(r.get("cost_usd") or 0.0 for r in results), 6)})

    # ---------- receipts.md ----------
    lines = ["# Free Calls batch receipt - " + run_id, "",
             "- Batch: " + str(batch),
             "- Trigger: " + trigger + " (owner-triggered lane; no schedule)",
             "- Models requested: " + ", ".join(models_used),
             "- Price check (live catalog, immediately before batch): " +
             ("all models verified per-call-mode (free=$0; paid=within budget)" if
              abort_reason is None or results else "NOT VERIFIED - " + str(abort_reason)),
             "- Paid budget: " + (("$%.2f hard ceiling in code; worst-case $%.6f; actual $%.6f"
                                   % (budget, paid_worst_total, actual_paid_so_far))
                                  if budget is not None else "none (free-only batch)"),
             "- Execution: SEQUENTIAL (one call at a time, " + str(args.inter_call_sleep) +
             "s spacing); no retries; no model substitution/fallback; no tools/web; no system prompt; " +
             "single user message per call; per-call max_tokens as recorded; provider-default temperature.",
             "- Red-line: every prompt passed the public-bus secret-shape scan; the API key " +
             "is never logged or written to receipts.",
             "- Status: " + str(len(completed)) + " completed / " + str(len(errored)) +
             " errored / " + str(len(calls)) + " total; known reported cost: $%.6f"
             % sum(r.get("cost_usd") or 0.0 for r in results), ""]
    for r in results:
        lines += ["## Call " + str(r.get("index")) + ": " + str(r.get("id")) +
                  " (seat: " + str(r.get("seat")) + ")", ""]
        src = next((c.get("source", "") for c in calls if c.get("id") == r.get("id")), "")
        if src:
            lines += ["- Source spec: " + src, ""]
        lines += ["- Status: " + str(r.get("status")),
                  "- Model returned: " + str(r.get("model_returned")) +
                  "; provider: " + str(r.get("provider_returned")) +
                  "; response id: " + str(r.get("response_id")),
                  "- Finish reason: " + str(r.get("finish_reason")) +
                  "; elapsed: " + str(r.get("elapsed_s")) + "s",
                  "- Usage: prompt " + str((r.get("usage") or {}).get("prompt_tokens")) +
                  " / completion " + str((r.get("usage") or {}).get("completion_tokens")) +
                  " / total " + str((r.get("usage") or {}).get("total_tokens")) + " tokens",
                  "- Cost: " + (("$%.6f" % r["cost_usd"]) if isinstance(r.get("cost_usd"), float)
                                else "null") + " (" + str(r.get("cost_basis")) + ")", ""]
        if r.get("reasoning_effort") or r.get("reasoning_mode"):
            lines += ["- Reasoning: effort " + str(r.get("reasoning_effort")) +
                      " / mode " + str(r.get("reasoning_mode")), ""]
        lines += ["### Raw response (verbatim)", ""]
        if r.get("status") == "completed":
            lines += [str(r.get("text") or ""), ""]
        else:
            lines += ["**" + str(r.get("status")) + "**: " + str(r.get("error")), ""]
    if abort_reason is not None and not results:
        lines += ["## Batch ABORTED before any call", "", abort_reason, ""]
    elif abort_reason is not None:
        lines += ["## Batch stopped early", "", abort_reason, ""]
    lines += ["## Appendix - submitted prompts (verbatim)", ""]
    for c in calls:
        img = (" (image attached: " + str(c.get("image")) + ")") if c.get("image") else ""
        lines += ["### " + str(c.get("id")) + " (seat: " + str(c.get("seat")) + ")" + img, "",
                  str(c.get("prompt")), ""]
    (outdir / "receipts.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"run_id": run_id, "reason": reason,
                      "completed": len(completed), "errored": len(errored),
                      "actual_paid_usd": round(actual_paid_so_far, 6)}, indent=2))
    if abort_reason is not None:
        raise SystemExit(1)
    if results and not completed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

