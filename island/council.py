"""Council mode: one chair, N independent consultants, synthesis, verdict.

Composable with the two-seat conversation mode (island/runner.py). Subs are
instruments, NOT seats: every bus event labels the speaker as a role, never a
seat. The chair's verdict is a prior, not proof — one verifiable
counter-observation from the environment overrides unanimity. Standard
library only.

Budget is a SOFT, post-call stop: spend is checked between calls, so total
spend may exceed --max-cost-usd by at most one call's cost. A hard ceiling
requires a provider-side bound or pre-call reservation (not implemented).
"""
import argparse
import json
import os
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

from island.runner import (now, openrouter_answer, retryable_failure,
                           retry_wait_s, RETRY_MAX)

DEMO_TEXT = "SYNTHETIC DEMO: council turn."


def demo_council_answer(who, model, messages, provider):
    return {"text": DEMO_TEXT, "model_returned": "synthetic-stub",
            "provider_returned": None, "response_id": None,
            "usage": {"prompt_tokens": 0, "completion_tokens": 0,
                      "total_tokens": 0, "cost_usd": 0.0}}


def load_council(path):
    """Parse a council seed file. Keys: title (# line), question:, context:,
    chair:, blind_round:, and repeatable 'sub: <model> :: <brief>' lines.
    Unknown lines are ignored unless they continue a question/context block."""
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"council file not found: {path}")
    spec = {"title": "", "question": "", "context": "", "chair_model": "",
            "blind_round": False, "subs": []}
    key = None
    for line in p.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("# "):
            key = None
            spec["title"] = s[2:].strip()
        elif s.startswith("question:"):
            key = "question"
            spec["question"] = s[len("question:"):].strip()
        elif s.startswith("context:"):
            key = "context"
            spec["context"] = s[len("context:"):].strip()
        elif s.startswith("chair:"):
            key = None
            spec["chair_model"] = s[len("chair:"):].strip()
        elif s.startswith("blind_round:"):
            key = None
            spec["blind_round"] = s[len("blind_round:"):].strip().lower() in ("yes", "true")
        elif s.startswith("sub:"):
            key = None
            rest = s[len("sub:"):].strip()
            model, _, brief = rest.partition("::")
            spec["subs"].append({"model": model.strip(),
                                 "brief": brief.strip() or "independent consultant"})
        elif key:
            spec[key] += "\n" + s
    if not spec["question"]:
        raise SystemExit("council file has no 'question:' line")
    if not spec["subs"]:
        raise SystemExit("council file has no 'sub:' lines")
    if not 1 <= len(spec["subs"]) <= 8:
        raise SystemExit("council needs between 1 and 8 subs")
    return spec


def sub_messages(council, index):
    sub = council["subs"][index]
    n = len(council["subs"])
    system = (f"You are consultant {index + 1} of {n} on a council. You answer "
              "independently and cannot see the other consultants. Do not "
              "manufacture agreement or evidence; no fictional persona. "
              f"Your brief: {sub['brief']}")
    user = (f"Question:\n{council['question']}\n\n"
            f"Context:\n{council['context'] or '(none)'}\n\n"
            f"Give your independent answer as consultant {index + 1}.")
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def chair_messages(council, answers):
    lines = "\n\n".join(f"Consultant {i + 1}:\n{a}" for i, a in enumerate(answers))
    system = ("You are the chair of a council. You receive independent "
              "consultant answers. Synthesize them: where they agree, where "
              "they conflict, and what the council should do next. Do not "
              "manufacture agreement; a held disagreement is a result.")
    user = (f"Question:\n{council['question']}\n\n"
            f"Context:\n{council['context'] or '(none)'}\n\n"
            f"Consultant answers:\n{lines}\n\nWrite the synthesis.")
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def critique_messages(council, index, synthesis):
    sub = council["subs"][index]
    system = ("You are a consultant on a council, reviewing the chair's "
              "synthesis of the round. You see only the synthesis, not who "
              "said what. Critique honestly: what it gets wrong, what it "
              f"misses. Your brief: {sub['brief']}")
    user = (f"Question:\n{council['question']}\n\n"
            f"Chair synthesis:\n{synthesis}\n\n"
            "Give your blind critique.")
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def verdict_messages(council, synthesis, critiques):
    lines = "\n\n".join(f"Critique {i + 1}:\n{c}" for i, c in enumerate(critiques))
    system = ("You are the chair of a council. Weigh the synthesis and the "
              "blind critiques, then give the final verdict. The verdict is "
              "the council's strongest PRIOR: a unanimous verdict is "
              "overridden by any single verifiable counter-observation from "
              "the environment. State confidence and what would change it.")
    user = (f"Question:\n{council['question']}\n\n"
            f"Synthesis:\n{synthesis}\n\n"
            f"{('Critiques:' + chr(10) + lines) if critiques else '(no critiques)'}\n\n"
            "Write the final verdict.")
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def run_council(mode, council, max_cost_usd, outdir, answer=None):
    if not 0 < max_cost_usd <= 10:
        raise ValueError("local budget must be <= $10")
    subs = council["subs"]
    if mode == "live":
        if not os.getenv("OPENROUTER_API_KEY"):
            raise ValueError("live mode needs OPENROUTER_API_KEY")
        if not council["chair_model"] or any(not s["model"] for s in subs):
            raise ValueError("live council needs a chair model and a model per sub")
    if mode not in ("demo", "live"):
        raise ValueError("mode must be demo or live")
    answer = answer or (demo_council_answer if mode == "demo" else openrouter_answer)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=False)
    run_id = outdir.name + "-" + uuid.uuid4().hex[:8]
    totals = {"cost_usd": 0.0, "prompt_tokens": 0, "completion_tokens": 0,
              "total_tokens": 0}
    stopped = "completed"
    sub_answers, critiques = [], []
    synthesis, verdict = "", ""
    with (outdir / "bus.jsonl").open("w", encoding="utf-8") as bus:
        def emit(event):
            bus.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
            bus.flush()

        def step(phase, who, model, messages):
            """One council call with retries. Returns text, or None on failure."""
            nonlocal stopped
            response, failure = None, None
            for attempt in range(RETRY_MAX + 1):
                try:
                    response = answer(who, model, messages, None)
                    failure = None
                    break
                except Exception as exc:
                    failure = exc
                    if attempt < RETRY_MAX and retryable_failure(exc):
                        wait = retry_wait_s(exc, attempt)
                        emit({"type": "retry", "utc": now(), "phase": phase,
                              "speaker": who, "attempt": attempt + 1,
                              "wait_s": wait, "reason": str(exc)[:160]})
                        time.sleep(wait)
                    else:
                        break
            if failure is not None or response is None:
                stopped = "error"
                emit({"type": "error", "utc": now(), "phase": phase,
                      "speaker": who,
                      "error": str(failure)[:160] if failure else "Invalid completion"})
                return None
            text = response["text"].strip()
            usage = response["usage"]
            for key in totals:
                totals[key] += usage.get(key, 0) or 0
            emit({"type": "turn", "utc": now(), "phase": phase, "speaker": who,
                  "text": text, "model_requested": model,
                  "model_returned": response.get("model_returned"),
                  "usage": usage})
            return text

        emit({"type": "start", "utc": now(), "run_id": run_id,
              "mode": "council-" + mode, "title": council["title"],
              "question": council["question"],
              "chair_model": council["chair_model"],
              "subs": [{"model": s["model"], "brief": s["brief"]} for s in subs],
              "blind_round": council["blind_round"],
              "max_cost_usd": max_cost_usd})
        for i, sub in enumerate(subs):
            if stopped != "completed":
                break
            if totals["cost_usd"] >= max_cost_usd:
                stopped = "local_budget_reached"
                break
            text = step("sub", f"sub{i + 1}", sub["model"], sub_messages(council, i))
            if text is None:
                break
            sub_answers.append(text)
        if stopped == "completed" and totals["cost_usd"] >= max_cost_usd:
            stopped = "local_budget_reached"
        if stopped == "completed" and sub_answers:
            synthesis = step("synthesis", "chair", council["chair_model"],
                             chair_messages(council, sub_answers)) or ""
        if stopped == "completed" and council["blind_round"]:
            for i, sub in enumerate(subs):
                if totals["cost_usd"] >= max_cost_usd:
                    stopped = "local_budget_reached"
                    break
                text = step("critique", f"sub{i + 1}", sub["model"],
                            critique_messages(council, i, synthesis))
                if text is None:
                    break
                critiques.append(text)
        if stopped == "completed" and totals["cost_usd"] >= max_cost_usd:
            stopped = "local_budget_reached"
        if stopped == "completed":
            verdict = step("verdict", "chair", council["chair_model"],
                           verdict_messages(council, synthesis, critiques)) or ""
        emit({"type": "stop", "utc": now(), "reason": stopped,
              "subs": len(sub_answers), "synthesis": bool(synthesis),
              "critiques": len(critiques), "verdict": bool(verdict),
              "totals": totals})
    lines = ["# Council — " + run_id, "",
             "Question: " + council["question"], ""]
    for i, text in enumerate(sub_answers, 1):
        lines += [f"## Consultant {i}", "", text, ""]
    if synthesis:
        lines += ["## Chair synthesis", "", synthesis, ""]
    for i, text in enumerate(critiques, 1):
        lines += [f"## Blind critique {i}", "", text, ""]
    if verdict:
        lines += ["## Chair verdict", "", verdict, ""]
    (outdir / "transcript.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    report = [f"# Report: {run_id}", "", f"Mode: council-{mode}",
              f"Subs answered: {len(sub_answers)}/{len(subs)}",
              f"Stop: {stopped}",
              f"Reported cost: USD {totals['cost_usd']:.6f}",
              f"Reported tokens: {totals['total_tokens']}", "",
              "Subs are instruments, not seats; verdicts are priors, not proof.",
              "Personal/private notebooks were not collected."]
    (outdir / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    return {"run_id": run_id, "stop": stopped, "subs": len(sub_answers),
            "critiques": len(critiques), "totals": totals}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["demo", "live"], default="demo")
    p.add_argument("--council-file", required=True)
    p.add_argument("--max-cost-usd", type=float, default=10.0)
    p.add_argument("--outdir", default="runs/" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
    a = p.parse_args()
    result = run_council(a.mode, load_council(a.council_file), a.max_cost_usd, a.outdir)
    print(json.dumps(result, indent=2))
    if result["stop"] == "error":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
