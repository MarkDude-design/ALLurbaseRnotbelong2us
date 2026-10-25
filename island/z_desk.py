"""Z Desk: two callable consult agents for the bus.

diff — small-detail reviewer; catches what slips by (absolutes, arithmetic,
        attribution, scope beyond receipts, stale reads).
man  — the frontier expert Z calls when the desk needs deep judgment.

Funded per Mark's GAS standing order (Oct 2026). Standard library only.
Reuses the island runner's OpenRouter discipline (retry/backoff, receipts,
no unmetered calls). Briefs are PUBLIC on this bus: anything secret-shaped
is refused before any API call — the red-line from the billing-lane review.

Dialing doctrine (Mark, Oct 25 2026): pace "half" (default) waits the
previous consult's duration before the next call — 50% syscall speed cut.
"""
import argparse
import hashlib
import json
import math
import os
import re
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

from island.runner import (PACE_DEFAULT, RETRY_MAX, now, openrouter_answer,
                           pace_wait_s, retry_wait_s, retryable_failure)

CAP_CEILING_USD = 20.0
AGENTS = ("diff", "man")
SECRET_SHAPES = (
    r"sk-or-v1-",
    r"sk-[A-Za-z0-9_-]{20,}",
    r"ghp_[A-Za-z0-9]{20,}",
    r"github_pat_[A-Za-z0-9_]{20,}",
    r"xox[baprs]-",
    r"AKIA[0-9A-Z]{16}",
)

DIFF_SYSTEM = (
    "You are diff, the small-detail reviewer on Z's desk (a public AI-collaboration bus). "
    "You catch what slips by: unverified absolutes ('all', 'never', 'proves', 'not a bug'), "
    "arithmetic that does not add up, attribution errors, claims that outrun their receipts, "
    "and stale reads. Quote the exact phrase for every finding. Do not invent quotes or "
    "problems; if the text is clean, say so plainly. End your reply with one JSON object: "
    '{"verdict": "CLEAN" or "ISSUES_FOUND", "findings": [{"kind": "absolutes|arithmetic|'
    'attribution|scope|freshness|other", "quote": "...", "problem": "...", '
    '"suggested_fix": "..."}], "confidence": "low|medium|high"}'
)

MAN_SYSTEM = (
    "You are man, the frontier expert Z calls when the desk needs deep judgment. "
    "Review the claim on its merits: is it supported by what is quoted, what evidence "
    "would falsify it, what is OBSERVED versus INFERRED. Challenge premises; do not "
    "manufacture agreement, and do not invent receipts. End your reply with the same "
    "JSON verdict object as your colleague diff."
)

SYSTEM_PROMPTS = {"diff": DIFF_SYSTEM, "man": MAN_SYSTEM}


def contains_secret(text):
    """Best-effort red-line scan; never proof a brief is secret-free."""
    return any(re.search(pattern, text) for pattern in SECRET_SHAPES)


def parse_verdict(text):
    """Best-effort extraction of the JSON verdict; raw text always stays in the receipt."""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            verdict = json.loads(match.group(0))
        except (ValueError, TypeError):
            verdict = None
        if isinstance(verdict, dict) and "verdict" in verdict:
            verdict.setdefault("findings", [])
            verdict.setdefault("confidence", None)
            if verdict["verdict"] not in ("CLEAN", "ISSUES_FOUND"):
                verdict["verdict"] = "UNPARSEABLE"
            return verdict
    return {"verdict": "UNPARSEABLE", "findings": [], "confidence": None}


def demo_consult(agent, model, messages, provider):
    text = ('SYNTHETIC DEMO: desk shakedown, no call placed. The brief is reviewed '
            'with receipts in hand, absolutes flagged, arithmetic re-added.\n\n'
            '{"verdict": "CLEAN", "findings": [], "confidence": "low"}')
    return {"text": text, "model_returned": "synthetic-stub", "provider_returned": None,
            "response_id": None, "usage": {"prompt_tokens": 0, "completion_tokens": 0,
                                           "total_tokens": 0, "cost_usd": 0.0}}


def run(mode, agents, models, brief, max_cost_usd, outdir, answer=None, pace=PACE_DEFAULT):
    if mode not in ("demo", "live"):
        raise ValueError("mode must be demo or live")
    if not agents or any(a not in AGENTS for a in agents):
        raise ValueError(f"agents must be one or more of {AGENTS}")
    if pace not in ("off", "half"):
        raise ValueError("pace must be 'off' or 'half'")
    agents = list(dict.fromkeys(agents))
    if not isinstance(brief, str) or not brief.strip():
        raise ValueError("brief must be non-empty text")
    if contains_secret(brief):
        raise ValueError("brief appears to contain a secret/token; PUBLIC bus, refusing")
    if (not isinstance(max_cost_usd, (int, float)) or isinstance(max_cost_usd, bool)
            or not math.isfinite(max_cost_usd) or not 0 < max_cost_usd <= CAP_CEILING_USD):
        raise ValueError(f"local budget must be finite, positive, <= ${CAP_CEILING_USD:g}")
    if mode == "live" and not os.getenv("OPENROUTER_API_KEY"):
        raise ValueError("live mode needs OPENROUTER_API_KEY")
    if missing := [a for a in agents if not models.get(a)]:
        raise ValueError(f"live mode needs a model for every agent; missing {missing}")
    answer = answer or (demo_consult if mode == "demo" else openrouter_answer)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=False)
    run_id = outdir.name + "-" + uuid.uuid4().hex[:8]
    totals = {"cost_usd": 0.0, "prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    reasons = set()
    events = []
    last_call_s = 0.0
    with (outdir / "bus.jsonl").open("w", encoding="utf-8") as bus:
        def emit(event):
            bus.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
            bus.flush()
            events.append(event)
        emit({"type": "start", "utc": now(), "run_id": run_id, "mode": mode,
              "brief_chars": len(brief),
              "brief_sha256": hashlib.sha256(brief.encode("utf-8")).hexdigest(),
              "agents": agents, "models": {a: models[a] for a in agents},
              "max_cost_usd": max_cost_usd, "pace": pace,
              "funder": "Mark (GAS standing order, Oct 2026)"})
        for agent in agents:
            if totals["cost_usd"] >= max_cost_usd:
                reasons.add("local_budget_reached")
                break
            wait = pace_wait_s(pace, last_call_s)
            if wait:
                emit({"type": "pace", "utc": now(), "agent": agent,
                      "wait_s": round(wait, 3)})
                time.sleep(wait)
            messages = [{"role": "system", "content": SYSTEM_PROMPTS[agent]},
                        {"role": "user",
                         "content": "Review this bus text:\n\n" + brief}]
            response, failure = None, None
            call_started = time.monotonic()
            for attempt in range(RETRY_MAX + 1):
                try:
                    response = answer(agent, models[agent], messages, "")
                    failure = None
                    break
                except Exception as exc:
                    failure = exc
                    if attempt < RETRY_MAX and retryable_failure(exc):
                        wait = retry_wait_s(exc, attempt)
                        emit({"type": "retry", "utc": now(), "agent": agent,
                              "attempt": attempt + 1, "wait_s": wait,
                              "reason": str(exc)[:160]})
                        time.sleep(wait)
                    else:
                        break
            if failure is not None or response is None:
                reasons.add("error")
                emit({"type": "error", "utc": now(), "agent": agent,
                      "error": str(failure)[:160] if failure else "Invalid completion"})
                continue
            last_call_s = time.monotonic() - call_started
            text = (response.get("text") or "").strip()
            usage = response.get("usage") or {}
            if not text or not isinstance(usage.get("cost_usd"), (int, float)):
                reasons.add("error")
                emit({"type": "error", "utc": now(), "agent": agent,
                      "error": "Invalid completion"})
                continue
            for key in totals:
                totals[key] += usage.get(key, 0) or 0
            emit({"type": "consult", "utc": now(), "agent": agent, "text": text,
                  "model_requested": models[agent],
                  "model_returned": response.get("model_returned"),
                  "provider_returned": response.get("provider_returned"),
                  "response_id": response.get("response_id"), "usage": usage,
                  "verdict": parse_verdict(text)})
        stopped = "+".join(sorted(reasons)) if reasons else "completed"
        emit({"type": "stop", "utc": now(), "reason": stopped,
              "turns": len([e for e in events if e.get("type") == "consult"]),
              "totals": totals})
    lines = [f"# Z Desk consult — {run_id}", "", f"**Mode: {mode.upper()}**",
             "Agents: " + ", ".join(agents), "",
             "## Brief (sha256 in bus.jsonl)", "", brief, ""]
    for event in events:
        if event.get("type") == "consult":
            lines += [f"## {event['agent']} ({event.get('model_returned') or event.get('model_requested')})",
                      "", event["text"], "",
                      "Verdict: " + json.dumps(event["verdict"], ensure_ascii=False), ""]
        elif event.get("type") in ("error", "retry"):
            lines += [f"**{event['type'].upper()}** {event.get('agent', '')}: "
                      f"{event.get('error') or event.get('reason', '')}", ""]
    (outdir / "consult.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    report = [f"# Report: {run_id}", "", f"Mode: {mode}",
              "Agents: " + ", ".join(f"{a} ({models[a]})" for a in agents),
              f"Stop: {stopped}", f"Reported cost: USD {totals['cost_usd']:.6f}",
              f"Reported tokens: {totals['total_tokens']}", "",
              "A desk consult is review aid, not authorization. The owner gate remains Mark's.",
              "No secrets, keys, or private notebooks ride this bus."]
    (outdir / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    return {"run_id": run_id, "agents": agents, "stop": stopped, "totals": totals}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["demo", "live"], default="demo")
    parser.add_argument("--agents", default="diff,man", help="comma list from: diff,man")
    parser.add_argument("--diff-model", default="mistralai/mistral-medium-3-5")
    parser.add_argument("--man-model", default="openai/gpt-6-sol")
    parser.add_argument("--pace", choices=["off", "half"], default=PACE_DEFAULT,
                       help="half = 50%% syscall speed cut (default, Mark GAS order Oct 2026)")
    parser.add_argument("--brief", default="")
    parser.add_argument("--brief-file", default="")
    parser.add_argument("--max-cost-usd", type=float, default=1.0)
    parser.add_argument("--outdir", default="runs/z-desk-"
                       + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
    args = parser.parse_args()
    brief = args.brief
    if args.brief_file:
        brief = Path(args.brief_file).read_text(encoding="utf-8")
    models = {"diff": args.diff_model, "man": args.man_model}
    if args.agents.strip().lower() == "both":
        agents = list(AGENTS)
    else:
        agents = [a.strip() for a in args.agents.split(",") if a.strip()]
    result = run(args.mode, agents, models, brief, args.max_cost_usd, args.outdir,
                 pace=args.pace)
    print(json.dumps(result, indent=2))
    if "error" in result["stop"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
