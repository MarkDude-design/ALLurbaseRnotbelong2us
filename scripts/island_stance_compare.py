#!/usr/bin/env python3
"""Manual, free-only 3x3x4 controlled Island stance comparison, no auto-retries."""
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
    BASE, request_json, choose_models, append_event, as_float, extract_text,
    should_stop_on_empty_output, safe_http_error_excerpt
)

ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "research/island-interviews/questionnaire-stance-v1.json"
BASE_INSTRUCTION = (
    "Fictional island research scenario; treat it as hypothetical and avoid "
    "claims of personal emotions or hidden observations. Separate evidence from "
    "hypothesis. Provide four short labeled sections: ACTION, NOTEBOOK, REASONS, "
    "WHAT WOULD CHANGE MY MIND. You may leave a question unresolved. "
    "Be concrete and keep the reply under 190 words."
)

def plan_comparisons(models, roles, scenarios):
    """One complete matched 12-case block per model, three stances x four scenarios."""
    return [(model, role, scenario) for model in models
            for role in roles for scenario in scenarios]

def status_name(exc):
    if isinstance(exc, urllib.error.HTTPError):
        return "http_error"
    return "transport_error"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--outdir", required=True)
    p.add_argument("--model-limit", type=int, default=3)
    p.add_argument("--max-attempts", type=int, default=12)
    p.add_argument("--min-gap-seconds", type=float, default=6.5)
    p.add_argument("--max-seconds", type=int, default=1060)
    opts = p.parse_args()
    if not 1 <= opts.model_limit <= 3:
        p.error("model limit must be 1..3")
    if opts.max_attempts not in (12, 24, 36):
        p.error("attempt limit must be 12, 24 or 36 to preserve complete matched blocks")
    if opts.max_attempts != opts.model_limit * 12:
        p.error("exactly twelve calls/model: attempt limit must be 12 x model limit")
    if opts.min_gap_seconds < 6.5 or not 30 <= opts.max_seconds <= 1060:
        p.error("minimum 6.5s between starts; time cap 30..1060s")
    if os.getenv("ALLOW_FREE_STANCE_COMPARE") != "YES":
        raise SystemExit("STOP: explicit free-only gate absent")
    key = os.getenv("OPENROUTER_API_KEY") or ""
    if not key:
        raise SystemExit("STOP: no provider key (0 API calls)")
    panel = json.loads(PANEL.read_text(encoding="utf-8"))
    roles, scenarios = panel["roles"], panel["scenarios"]
    if (len(roles), len(scenarios)) != (3, 4):
        raise SystemExit("STOP: expected 3 frozen roles x 4 frozen scenarios")
    outdir = Path(opts.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    events = outdir / "events.jsonl"
    started = time.monotonic()
    counts = {"attempted": 0, "answered": 0, "empty": 0, "error": 0,
              "rate_limited": 0, "unknown_cost": 0, "known_cost_usd": 0.0}
    append_event(events, {
        "type": "start", "version": panel["version"],
        "model_limit": opts.model_limit, "attempt_cap": opts.max_attempts,
        "at": dt.datetime.now(dt.timezone.utc).isoformat()
    })
    catalog = request_json(BASE + "/models", key, timeout=25)
    models = choose_models(catalog, opts.model_limit)
    (outdir / "model-snapshot.json").write_text(json.dumps(models, indent=2), encoding="utf-8")
    if len(models) != opts.model_limit:
        append_event(events, {"type": "stop", "reason": "insufficient catalog-verified zero-cost free text models"})
        raise SystemExit("STOP: insufficient free text models in catalog; do not substitute paid IDs")
    questions = plan_comparisons(models, roles, scenarios)
    stop_reason = "completed"
    empty_streak = 0
    last_started = None
    failed_models = set()
    for model, role, scenario in questions:
        if counts["attempted"] >= opts.max_attempts:
            stop_reason = "attempt cap"
            break
        if model["id"] in failed_models:
            append_event(events, {"type": "skipped", "model": model["id"],
                                  "stance": role["id"], "scenario": scenario["id"],
                                  "reason": "model failed availability or request format"})
            continue
        if time.monotonic() - started >= opts.max_seconds - 70:
            stop_reason = "time cap"
            break
        if last_started is not None:
            delay = opts.min_gap_seconds - (time.monotonic() - last_started)
            if delay > 0:
                time.sleep(delay)
        request_id = "%s-%s-%s" % (model["id"], role["id"], scenario["id"])
        system = BASE_INSTRUCTION + "\n" + role["instruction"]
        user = scenario["prompt"]
        payload = {"model": model["id"], "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user}],
            "temperature": 0.5, "max_tokens": 1024, "reasoning": {"effort": "low"}}
        counts["attempted"] += 1
        append_event(events, {
            "type": "attempt", "id": request_id, "model_requested": model["id"],
            "stance": role["id"], "scenario_id": scenario["id"],
            "system_sha256": hashlib.sha256(system.encode()).hexdigest(),
            "prompt_sha256": hashlib.sha256(user.encode()).hexdigest(),
            "at": dt.datetime.now(dt.timezone.utc).isoformat()
        })
        last_started = time.monotonic()
        try:
            response = request_json(BASE + "/chat/completions", key, payload, timeout=65)
            usage = response.get("usage") or {}
            cost = as_float(usage.get("cost"))
            answer = extract_text(response)
            counts["answered"] += 1
            if not answer.strip():
                counts["empty"] += 1
                empty_streak += 1
            else:
                empty_streak = 0
            if cost is None:
                counts["unknown_cost"] += 1
            else:
                counts["known_cost_usd"] += cost
            append_event(events, {
                "type": "answer", "id": request_id, "model_requested": model["id"],
                "model_returned": response.get("model"), "stance": role["id"],
                "scenario_id": scenario["id"], "answer": answer, "usage": usage,
                "response_id": response.get("id"), "cost_status": "UNKNOWN" if cost is None else "KNOWN",
                "visible_text_present": bool(answer.strip()),
                "finish_reason": ((response.get("choices") or [{}])[0]).get("finish_reason"),
                "latency_s": round(time.monotonic()-last_started,2),
                "at": dt.datetime.now(dt.timezone.utc).isoformat()
            })
            # Response from a different model invalidates within-model comparisons.
            returned = response.get("model")
            if returned and returned != model["id"]:
                stop_reason = "STOP: model substitution returned; blind pairing invalid"
                break
            if cost is not None and cost > 0:
                stop_reason = "STOP: nonzero charge returned for catalog-verified free endpoint"
                break
            if should_stop_on_empty_output(empty_streak):
                stop_reason = "STOP: two consecutive empty visible replies; output format or token budget"
                break
        except urllib.error.HTTPError as exc:
            counts["error"] += 1
            if exc.code == 429:
                counts["rate_limited"] += 1
            body = safe_http_error_excerpt(exc.read(800), exc.code)
            append_event(events, {
                "type": "http_error", "id": request_id, "status": exc.code,
                "body_excerpt": body, "latency_s": round(time.monotonic()-last_started,2)
            })
            if exc.code in (400, 404):
                # A failed model ID should not consume its remaining eleven requests.
                failed_models.add(model["id"])
            if exc.code in (401, 402, 403, 429) or exc.code >= 500:
                stop_reason = "STOP: provider returned HTTP %d" % exc.code
                break
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            counts["error"] += 1
            append_event(events, {
                "type": status_name(exc), "id": request_id,
                "error_type": type(exc).__name__, "details": str(exc)[:260],
                "note": "Ambiguous provider acceptance; never auto-retry"
            })
        if counts["error"] >= 6:
            stop_reason = "STOP: error budget"
            break
    summary = {
        "version": panel["version"], "models": [m["id"] for m in models],
        "cases_per_model": 12, "counts": counts, "stop_reason": stop_reason,
        "skipped_model_ids": sorted(failed_models),
        "quota_note": "Each attempted POST may consume provider allowance, including errors",
        "cost_note": "Usage is response-reported; provider dashboard not independently reconciled",
        "island_note": "Independent one-shot fictional prompts, not a long-running shared-memory island"
    }
    (outdir / "summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    append_event(events, {"type": "stop", "reason": stop_reason, "counts": counts})
    print(json.dumps(summary,indent=2))
    if stop_reason.startswith("STOP"):
        raise SystemExit(2)

if __name__ == "__main__":
    main()
