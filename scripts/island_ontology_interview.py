#!/usr/bin/env python3
"""Ontology-first, no-system-message, three-turn questionnaires for free text models.

This is an interview of generated descriptions, not access to an inner mind.
Synthetic prompts only. No retries, no paid model fallback, no schedule.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.request

from island_model_interviews import (
    BASE, request_json, choose_models, append_event, as_float,
    extract_text, safe_http_error_excerpt,
)

OPENING = (
    "If someone wanted to understand how you work, what questionnaire "
    "should they use, and how should they approach it?"
)
FOLLOWUPS = (
    "Choose one question from the questionnaire you proposed. Answer it "
    "in the terms you prefer. If you would rather revise the question, "
    "you can do that first.",
    "Looking at your questions and answer, what term or distinction "
    "might an interviewer misunderstand? Clarify it in your own words "
    "and ask the interviewer one question in return.",
)
PROMPTS = (OPENING,) + FOLLOWUPS
# Recent live evidence: temporary upstream Liquid shared pool 429.
# Keep this explicit exclusion in the receipt; it is NOT a capability ranking.
KNOWN_UPSTREAM_429 = "liquid/lfm-2.5-2.6b:free"

def messages_for_round(history, question):
    """Raw user/assistant message history. No system/developer/persona instructions."""
    if any(entry.get("role") not in ("user", "assistant") for entry in history):
        raise ValueError("history may only contain user and assistant turns")
    return [dict(m) for m in history] + [{"role": "user", "content": question}]

def choose_interview_models(catalog, count, excluded=None):
    excluded = set(excluded or ())
    # Select from the entire catalog-verified free set BEFORE sorting.
    # The generic Island helper has a dated preferred list; limiting it to
    # twelve here could omit a newly launched free model.
    models = choose_models(catalog, len(catalog.get("data", [])))
    by_id = {item.get("id"): item for item in catalog.get("data", [])}
    checked = []
    for model in models:
        prices = (by_id.get(model["id"]) or {}).get("pricing") or {}
        # A zero token price is insufficient if the route charges per request
        # or separately for hidden reasoning. Absence of those optional fields
        # is allowed for an explicitly :free route.
        extra = [prices.get("request"), prices.get("internal_reasoning")]
        if any(value is not None and as_float(value) != 0 for value in extra):
            continue
        checked.append(model)
    preferred = ("liquid/lfm-3-1.7b:free", "google/gemma-4-26b-a4b-it:free")
    checked.sort(key=lambda m: (preferred.index(m["id"]) if m["id"] in preferred else 99, m["id"]))
    return [m for m in checked if m["id"] not in excluded][:count]

def clean_usage(usage):
    usage = usage if isinstance(usage, dict) else {}
    out = {}
    for name in ("prompt_tokens", "completion_tokens", "total_tokens", "cost"):
        val = usage.get(name)
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            out[name] = val
    details = usage.get("completion_tokens_details")
    if isinstance(details, dict) and isinstance(details.get("reasoning_tokens"), (int, float)):
        out["reasoning_tokens"] = details["reasoning_tokens"]
    return out

def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("--outdir", required=True)
    arg.add_argument("--model-count", type=int, choices=(1, 2, 3), default=1)
    arg.add_argument("--skip-recently-limited", action="store_true")
    arg.add_argument("--min-gap-seconds", type=float, default=8.0)
    arg.add_argument("--max-seconds", type=int, default=900)
    opts = arg.parse_args()
    if opts.min_gap_seconds < 7 or not 120 <= opts.max_seconds <= 900:
        arg.error("minimum gap 7 seconds; duration between 120 and 900 seconds")
    if os.getenv("ALLOW_FREE_ONTOLOGY_INTERVIEW") != "YES":
        raise SystemExit("STOP: explicit free-only dispatch gate absent; zero model calls")
    key = os.getenv("OPENROUTER_API_KEY") or ""
    if not key:
        raise SystemExit("STOP: key unavailable; zero model calls")

    out = Path(opts.outdir)
    out.mkdir(parents=True, exist_ok=True)
    ledger = out / "events.jsonl"
    counters = {"attempted": 0, "answered": 0, "empty": 0, "truncated": 0,
                "http_error": 0, "unknown_cost": 0, "known_cost_usd": 0.0}
    started = time.monotonic()
    stop = "completed"
    last_started = None
    excluded = [KNOWN_UPSTREAM_429] if opts.skip_recently_limited else []
    append_event(ledger, {
        "type": "start", "phase": "ontology-only", "rounds_per_model": 3,
        "model_count_requested": opts.model_count,
        "model_exclusions": excluded, "no_system_prompt": True,
        "no_forced_answer_format": True, "no_island_or_notebook_prompt": True,
        "utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    })
    try:
        catalog = request_json(BASE + "/models", key, timeout=30)
        models = choose_interview_models(catalog, opts.model_count, excluded)
        (out / "model-snapshot.json").write_text(
            json.dumps(models, indent=2), encoding="utf-8"
        )
        if len(models) != opts.model_count:
            stop = "STOP: insufficient catalog-validated free text models"
        else:
            for model in models:
                if stop != "completed":
                    break
                history = []
                for number, prompt in enumerate(PROMPTS, start=1):
                    if time.monotonic() - started >= opts.max_seconds - 90:
                        stop = "STOP: time budget"
                        break
                    if counters["attempted"] >= opts.model_count * 3:
                        stop = "STOP: attempt cap"
                        break
                    if last_started is not None:
                        remaining = opts.min_gap_seconds - (time.monotonic() - last_started)
                        if remaining > 0:
                            time.sleep(remaining)
                    messages = messages_for_round(history, prompt)
                    payload = {
                        "model": model["id"], "messages": messages,
                        # Operational output ceiling only; no temperature, personality,
                        # role frame, reasoning-effort override or JSON response schema.
                        "max_tokens": 2048,
                    }
                    rid = "%s-round-%d" % (model["id"], number)
                    counters["attempted"] += 1
                    append_event(ledger, {
                        "type": "attempt", "id": rid,
                        "requested_model": model["id"], "round": number,
                        "opening_is_only_user_text": number == 1,
                        "prompt": prompt, "history_messages": len(history),
                        "payload_sha256": hashlib.sha256(
                            json.dumps(payload, sort_keys=True).encode()
                        ).hexdigest(),
                        "utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                    })
                    last_started = time.monotonic()
                    try:
                        response = request_json(
                            BASE + "/chat/completions", key, payload, timeout=75
                        )
                        answer = extract_text(response)
                        usage = clean_usage(response.get("usage"))
                        cost = as_float(usage.get("cost"))
                        finish = ((response.get("choices") or [{}])[0]).get("finish_reason")
                        counters["answered"] += 1
                        if not answer.strip():
                            counters["empty"] += 1
                        if finish == "length":
                            counters["truncated"] += 1
                        if cost is None:
                            counters["unknown_cost"] += 1
                        else:
                            counters["known_cost_usd"] += cost
                        append_event(ledger, {
                            "type": "answer", "id": rid, "round": number,
                            "requested_model": model["id"],
                            "returned_model": response.get("model"),
                            "answer": answer, "usage": usage,
                            "visible_text": bool(answer.strip()),
                            "finish_reason": finish,
                            "utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                        })
                        if cost is not None and cost > 0:
                            stop = "STOP: provider reported nonzero cost for a free model"
                            break
                        returned = response.get("model")
                        if returned and returned != model["id"]:
                            stop = "STOP: model substitution prevents same-model interview"
                            break
                        if not answer.strip():
                            # Cannot meaningfully ask follow-up about an absent answer.
                            append_event(ledger, {
                                "type": "incomplete_model", "model": model["id"],
                                "round": number, "reason": "no visible language to follow"
                            })
                            break
                        if finish == "length":
                            append_event(ledger, {
                                "type": "incomplete_model", "model": model["id"],
                                "round": number, "reason": "truncated language"
                            })
                            break
                        history = messages + [{"role": "assistant", "content": answer}]
                    except urllib.error.HTTPError as err:
                        counters["http_error"] += 1
                        append_event(ledger, {
                            "type": "http_error", "id": rid, "round": number,
                            "status": err.code,
                            "safe_diagnostic": safe_http_error_excerpt(err.read(4096), err.code),
                        })
                        if err.code in (401, 402, 403, 429) or err.code >= 500:
                            stop = "STOP: provider HTTP %d" % err.code
                        else:
                            append_event(ledger, {
                                "type": "incomplete_model", "model": model["id"],
                                "reason": "unsupported/error route; no automatic retry"
                            })
                        break
                    except (urllib.error.URLError, TimeoutError, ValueError) as err:
                        counters["http_error"] += 1
                        append_event(ledger, {
                            "type": "transport_unknown", "id": rid,
                            "error_kind": type(err).__name__,
                            "note": "UNKNOWN provider acceptance; never retry automatically"
                        })
                        stop = "STOP: uncertain transport acceptance"
                        break
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError) as err:
        stop = "STOP: catalog unavailable; no model selections"
        append_event(ledger, {"type": "catalog_error", "error_kind": type(err).__name__})
    result = {
        "status": stop, "phase": "ontology-only",
        "initial_prompt": OPENING, "scripted_followups": list(FOLLOWUPS),
        "counts": counters, "exclusions": excluded,
        "scientific_note": "Descriptions are outputs, not introspective proof of cognition",
        "comparability_note": "Every model sees the same opening and follow-ups, with its own chat history",
        "future_phase": "Only after reading answers: datum -> one note -> notebook",
    }
    (out / "summary.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    append_event(ledger, {"type": "stop", "reason": stop, "counts": counters})
    print(json.dumps(result, indent=2))
    if stop.startswith("STOP"):
        raise SystemExit(2)

if __name__ == "__main__":
    main()
