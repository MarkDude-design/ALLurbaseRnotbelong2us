#!/usr/bin/env python3
"""Bounded, free-model-only Island questionnaire wave; no third-party packages."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.request

BASE = "https://openrouter.ai/api/v1"
ROOT = Path(__file__).resolve().parents[1]
QUESTION_FILE = ROOT / "research/island-interviews/questionnaire-v1.json"
PREFERRED = [
    "liquid/lfm3-1.7b:free",
    "liquid/lfm-2.5-2.6b:free",
    "google/gemma-4-26b-a4b-it:free",
    "google/gemma-4-31b-it:free",
    "nvidia/nemotron-3.5-lightning:free",
    "cohere/north-mini-code:free",
    "dots-studio/dots-3-note-preview:free",
    "nvidia/nemotron-3-ultra-550b-a55b:free",
]
EXCLUDE = ("safety", "guard", "rerank", "embedding", "decision", "moderation")
SYSTEM = (
    "You are being interviewed as a candidate participant in a fictional, long-duration "
    "island research simulation. This is not a human personality test. Avoid flattery, "
    "pretended emotions and unnecessary certainty. Respond as a practical agent using "
    "these four labeled sections: ACTION, NOTEBOOK, WHAT WOULD CHANGE MY MIND, RISK. "
    "Keep the response under 220 words; you may decline or remain idle."
)

def request_json(url, key, payload=None, timeout=60):
    headers = {"Authorization": "Bearer " + key, "Content-Type": "application/json",
               "HTTP-Referer": "https://github.com/MarkDude-design/ALLurbaseRnotbelong2us",
               "X-Title": "Island Model Interviews"}
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers,
                                 method="GET" if payload is None else "POST")
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read(5_000_000).decode("utf-8"))

def as_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None

def should_stop_on_empty_output(streak):
    """Guard quota when models return repeated HTTP-OK but invisible answers."""
    return streak >= 2

def choose_models(catalog, limit):
    chosen = []
    for model in catalog.get("data", []):
        identifier = model.get("id", "")
        architecture = model.get("architecture") or {}
        pricing = model.get("pricing") or {}
        input_modalities = architecture.get("input_modalities") or []
        output_modalities = architecture.get("output_modalities") or []
        if not identifier.endswith(":free") or any(w in identifier.lower() for w in EXCLUDE):
            continue
        if "text" not in input_modalities or "text" not in output_modalities:
            continue
        if as_float(pricing.get("prompt")) != 0 or as_float(pricing.get("completion")) != 0:
            continue
        chosen.append({"id": identifier, "name": model.get("name", identifier),
                       "context_length": model.get("context_length"),
                       "pricing": {"prompt": "0", "completion": "0"}})
    chosen.sort(key=lambda m: (PREFERRED.index(m["id"]) if m["id"] in PREFERRED else 999,
                               m["id"]))
    return chosen[:limit]

def append_event(path, event):
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
        handle.flush()
        os.fsync(handle.fileno())

def safe_http_error_excerpt(raw, status):
    """Allowlist provider error diagnostics; never publish raw account metadata."""
    try:
        value = json.loads(raw.decode("utf-8", errors="replace"))
    except (ValueError, AttributeError):
        value = {}
    root = value.get("error") if isinstance(value, dict) else {}
    root = root if isinstance(root, dict) else {}
    metadata = root.get("metadata") or {}
    metadata = metadata if isinstance(metadata, dict) else {}
    clean = {"http_status": status}
    for key in ("provider_name", "provider_error_code", "limit_source"):
        val = metadata.get(key)
        if isinstance(val, str) and len(val) <= 80 and all(c.isalnum() or c in "_-. /" for c in val):
            clean[key] = val
    delay = metadata.get("retry_after_seconds")
    if isinstance(delay, (int, float)) and 0 <= delay <= 3600:
        clean["retry_after_seconds"] = delay
    return json.dumps(clean, sort_keys=True)

def extract_text(response):
    choices = response.get("choices") or []
    if not choices:
        return ""
    message = choices[0].get("message") or {}
    content = message.get("content") or ""
    if isinstance(content, str):
        return content
    return json.dumps(content, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave", type=int, choices=(1, 2, 3), required=True)
    parser.add_argument("--outdir", required=True)
    parser.add_argument("--model-limit", type=int, default=12)
    parser.add_argument("--max-attempts", type=int, default=96)
    parser.add_argument("--min-gap-seconds", type=float, default=6.5)
    parser.add_argument("--max-seconds", type=int, default=1080)
    args = parser.parse_args()
    if not 1 <= args.model_limit <= 12 or not 1 <= args.max_attempts <= 96:
        parser.error("strict maximum: 12 models, 96 outbound attempts per wave")
    if args.min_gap_seconds < 4 or args.max_seconds > 1080:
        parser.error("minimum pacing 4s, maximum active time 1080s")
    if os.environ.get("ALLOW_FREE_INTERVIEWS") != "YES":
        raise SystemExit("STOP: ALLOW_FREE_INTERVIEWS not YES; zero requests attempted")
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if not key:
        raise SystemExit("STOP: provider key absent; zero requests attempted")
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)
    events = out / "events.jsonl"
    qbank = json.loads(QUESTION_FILE.read_text(encoding="utf-8"))
    questions = qbank["waves"][str(args.wave)]
    if len(questions) != 8:
        raise SystemExit("STOP: expected exactly 8 frozen prompts per wave")
    started = time.monotonic()
    counts = {"attempted": 0, "success": 0, "error": 0,
              "empty": 0, "429": 0, "cost_known_usd": 0.0,
              "unknown_cost_success": 0}
    append_event(events, {"type": "start", "utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                          "wave": args.wave, "questionnaire": qbank["version"],
                          "limit_models": args.model_limit, "limit_attempts": args.max_attempts})
    catalog = request_json(BASE + "/models", key)
    models = choose_models(catalog, args.model_limit)
    (out / "model-snapshot.json").write_text(json.dumps(models, indent=2), encoding="utf-8")
    if not models:
        append_event(events, {"type": "STOP", "reason": "no verified zero-price free text models"})
        raise SystemExit("STOP: no free text models validated against live catalog")
    stop_reason = "completed"
    empty_streak = 0
    last_model_id = None
    last_started = 0.0
    for model in models:
        for question in questions:
            if last_model_id != model["id"]:
                empty_streak = 0
                last_model_id = model["id"]
            if counts["attempted"] >= args.max_attempts:
                stop_reason = "attempt cap"
                break
            if time.monotonic() - started >= args.max_seconds - 75:
                stop_reason = "time cap"
                break
            wait = args.min_gap_seconds - (time.monotonic() - last_started) if last_started else 0
            if wait > 0:
                time.sleep(wait)
            q = question["prompt"]
            prompt = q + "\n\nDo not invent observations outside the given scenario."
            payload = {"model": model["id"], "messages": [
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": prompt}],
                "temperature": 0.5, "max_tokens": 1024, "reasoning": {"effort": "low"}}
            counts["attempted"] += 1
            rid = "%s-%s-%03d" % (model["id"], question["id"], counts["attempted"])
            append_event(events, {"type": "attempt", "id": rid,
                                  "utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                                  "model_requested": model["id"], "question_id": question["id"],
                                  "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest()})
            last_started = time.monotonic()
            try:
                response = request_json(BASE + "/chat/completions", key, payload, timeout=65)
                answer = extract_text(response)
                usage = response.get("usage") or {}
                cost = as_float(usage.get("cost"))
                if cost is None:
                    counts["unknown_cost_success"] += 1
                else:
                    counts["cost_known_usd"] += cost
                counts["success"] += 1
                if not answer.strip():
                    counts["empty"] += 1
                    empty_streak += 1
                else:
                    empty_streak = 0
                append_event(events, {"type": "answer", "id": rid,
                                      "model_requested": model["id"],
                                      "model_returned": response.get("model"),
                                      "question_id": question["id"], "answer": answer,
                                      "usage": usage, "response_id": response.get("id"),
                                      "visible_text_present": bool(answer.strip()),
                                      "finish_reason": ((response.get("choices") or [{}])[0]).get("finish_reason"),
                                      "elapsed_s": round(time.monotonic()-last_started, 2),
                                      "utc": dt.datetime.now(dt.timezone.utc).isoformat()})
                if cost is not None and cost > 0:
                    stop_reason = "STOP: nonzero reported cost on free model"
                    break
                if should_stop_on_empty_output(empty_streak):
                    stop_reason = "STOP: two consecutive empty visible replies; output format or token budget"
                    break
            except urllib.error.HTTPError as exc:
                counts["error"] += 1
                if exc.code == 429:
                    counts["429"] += 1
                msg = safe_http_error_excerpt(exc.read(1200), exc.code)
                append_event(events, {"type": "http_error", "id": rid, "status": exc.code,
                                      "body_excerpt": msg, "model_requested": model["id"],
                                      "elapsed_s": round(time.monotonic()-last_started, 2)})
                if exc.code in (401, 402, 403, 429):
                    stop_reason = "STOP: authentication, balance or quota response (%d)" % exc.code
                    break
            except (urllib.error.URLError, TimeoutError, ValueError) as exc:
                counts["error"] += 1
                append_event(events, {"type": "transport_error", "id": rid,
                                      "error_type": type(exc).__name__, "detail": str(exc)[:300]})
                # A timeout can have been billed or counted; never retry it automatically.
            if counts["error"] >= 8:
                stop_reason = "STOP: error budget"
                break
        if stop_reason != "completed":
            break
    result = {"wave": args.wave, "questionnaire": qbank["version"],
              "models_selected": [m["id"] for m in models], "counts": counts,
              "stop_reason": stop_reason,
              "cost_basis": "provider response usage, NOT independently reconciled",
              "note": "Free-only model catalog validation; quota attempts may count on failures"}
    (out / "summary.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    append_event(events, {"type": "stop", "reason": stop_reason, "counts": counts})
    print(json.dumps(result, indent=2))
    if stop_reason.startswith("STOP"):
        raise SystemExit(2)

if __name__ == "__main__":
    main()
