"""Z Desk: batched raw free-model calls (one owner-triggered action, N independent requests).

Born 2026-11-09 for the GPT-family free-first experiments (Luna + Terra pair
specs on the bus; owner authorization bus #2 comment 6752602689). The queue
lane runs island.z_desk CONSULTS (reviewer system prompts + verdict JSON),
which would silently change those experiments; this module makes RAW single
calls instead: one text-only request per spec entry, exact prompt as
written, no system prompt, no tools/web, no retries, no paid fallback, and
the batch ABORTS unless the target's live catalog pricing is exactly $0 for
prompt and completion immediately before the first call. Prompts ride the
PUBLIC-bus red-line (secret-shape scan shared with island.z_desk). A failed
request is receipted data; the batch continues. Execution is sequential and
recorded as such, never hidden. Trigger: workflow_dispatch (owner click).
"""
import argparse
import hashlib
import json
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
MAX_CALLS = 8
MAX_PROMPT_CHARS = 20000
HTTP_TIMEOUT_S = 600
CATALOG_TIMEOUT_S = 30


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def catalog_get(url, timeout):
    req = urllib.request.Request(url, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def price_is_zero(entry):
    pricing = entry.get("pricing") or {}

    def zero(v):
        try:
            return float(v) == 0.0
        except (TypeError, ValueError):
            return False

    return zero(pricing.get("prompt")) and zero(pricing.get("completion"))


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
          "red_line": "public-bus secret-shape scan applied to every prompt"})

    # Live $0 pricing verification BEFORE any call (seats' abort rule, enforced mechanically).
    catalog_check = {"type": "catalog_check", "utc": now(), "model": model}
    abort_reason = None
    try:
        catalog = catalog_get(CATALOG_URL, CATALOG_TIMEOUT_S)
        entry = next((m for m in catalog.get("data", []) if m.get("id") == model), None)
        if entry is None:
            abort_reason = "model not in live catalog"
        elif not price_is_zero(entry):
            abort_reason = "live catalog pricing is not exactly $0 (prompt/completion)"
        else:
            catalog_check.update({"pricing": entry.get("pricing"), "name": entry.get("name"),
                                  "context_length": entry.get("context_length"),
                                  "expiration_date": entry.get("expiration_date")})
    except Exception as exc:  # noqa: BLE001 - abort path must receipt any failure
        abort_reason = "catalog fetch failed: " + str(exc)[:200]
    catalog_check["price_verified_zero"] = abort_reason is None
    emit(catalog_check)

    results = []
    if abort_reason is None:
        for i, c in enumerate(calls, 1):
            cid, seat = c["id"], c.get("seat", "")
            prompt = c["prompt"]
            emit({"type": "call_start", "utc": now(), "index": i, "id": cid, "seat": seat,
                  "prompt_chars": len(prompt),
                  "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest()})
            result = {"type": "call_result", "utc": now(), "index": i, "id": cid, "seat": seat,
                      "model_requested": model, "max_tokens": max_tokens}
            try:
                payload = {"model": model,
                           "messages": [{"role": "user", "content": prompt}],
                           "max_tokens": max_tokens}
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
                    "cost_usd": 0.0,
                    "cost_basis": "catalog price verified $0/$0 immediately before batch",
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
                               "cost_basis": "no completed call; catalog was $0 at check time"})
            except Exception as exc:  # noqa: BLE001
                result.update({"status": "error", "error": str(exc)[:200],
                               "cost_usd": None,
                               "cost_basis": "no completed call; catalog was $0 at check time"})
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
          "known_reported_cost_usd": sum(r.get("cost_usd") or 0.0 for r in results)})

    # ---------- receipts.md ----------
    cc = events[1] if len(events) > 1 and events[1].get("type") == "catalog_check" else {}
    lines = ["# Free Calls batch receipt - " + run_id, "",
             "- Batch: " + str(batch),
             "- Trigger: " + trigger + " (owner-triggered lane; no schedule)",
             "- Model requested: " + model,
             "- Price check (live catalog, immediately before batch): " +
             ("VERIFIED $0 prompt / $0 completion at " + str(cc.get("utc")) if
              cc.get("price_verified_zero") else "NOT VERIFIED - " + str(abort_reason)),
             "- Context length: " + str(cc.get("context_length")) +
             "; expiration_date: " + str(cc.get("expiration_date")),
             "- Execution: SEQUENTIAL (one call at a time, " + str(args.inter_call_sleep) +
             "s spacing); no retries; no paid fallback; no tools/web; no system prompt; " +
             "single user message per call; max_tokens " + str(max_tokens) +
             "; provider-default temperature.",
             "- Red-line: every prompt passed the public-bus secret-shape scan; the API key " +
             "is never logged or written to receipts.",
             "- Status: " + str(len(completed)) + " completed / " + str(len(errored)) +
             " errored / " + str(len(calls)) + " total; known reported cost: $0.000000", ""]
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
        lines += ["### Raw response (verbatim)", ""]
        if r.get("status") == "completed":
            lines += [str(r.get("text") or ""), ""]
        else:
            lines += ["**" + str(r.get("status")) + "**: " + str(r.get("error")), ""]
    if abort_reason is not None:
        lines += ["## Batch ABORTED before any call", "", abort_reason, ""]
    lines += ["## Appendix - submitted prompts (verbatim)", ""]
    for c in calls:
        lines += ["### " + str(c.get("id")) + " (seat: " + str(c.get("seat")) + ")", "",
                  str(c.get("prompt")), ""]
    (outdir / "receipts.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"run_id": run_id, "reason": reason,
                      "completed": len(completed), "errored": len(errored)}, indent=2))
    if abort_reason is not None:
        raise SystemExit(1)
    if results and not completed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
