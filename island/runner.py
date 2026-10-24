"""Two API-model proxies, natural conversation and minimal JSONL bus. Standard library only."""
import argparse
import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

API_URL = "https://openrouter.ai/api/v1/chat/completions"
TOPIC = "Emergence versus calibration: where should our conversation begin?"


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def messages_for(who, history, topic):
    peer = "B" if who == "A" else "A"
    system = (
        f"You are participant {who}, talking with participant {peer}. "
        "Exchange substantive ideas in a few natural paragraphs, not rapid-fire. "
        "Challenge premises if useful. Do not manufacture agreement, discoveries, "
        "personal history, or experimental evidence. No fictional persona. "
        "Respond to the conversation itself, not to a facilitator."
    )
    if history:
        transcript = "\n\n".join(f"{x['speaker']}: {x['text']}" for x in history)[-28000:]
        text = f"Opening topic: {topic}\n\nConversation so far:\n{transcript}\n\nContinue as {who}."
    else:
        text = f"Opening topic: {topic}\n\nYou speak first. Open naturally."
    return [{"role": "system", "content": system}, {"role": "user", "content": text}]


def demo_answer(who, model, messages, provider):
    text = {"A": "SYNTHETIC DEMO: Does calibration resemble discovery early in a run?",
            "B": "SYNTHETIC DEMO: Test different starts, and record both failed and successful attempts."}[who]
    return {"text": text, "model_returned": "synthetic-stub", "provider_returned": None,
            "response_id": None, "usage": {"prompt_tokens": 0, "completion_tokens": 0,
            "total_tokens": 0, "cost_usd": 0.0}}


def openrouter_answer(who, model, messages, provider):
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise RuntimeError("Missing OPENROUTER_API_KEY")
    payload = {"model": model, "messages": messages, "max_tokens": 600,
               "usage": {"include": True}, "provider": {
                   "allow_fallbacks": False, "data_collection": "deny"}}
    if provider:
        payload["provider"]["order"] = [provider]
    request = Request(API_URL, data=json.dumps(payload).encode(), method="POST",
                      headers={"Authorization": "Bearer " + key,
                               "Content-Type": "application/json",
                               "X-OpenRouter-Metadata": "enabled",
                               "X-OpenRouter-Title": "ALLurbase Island Pa More"})
    try:
        with urlopen(request, timeout=120) as response:
            data = json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"OpenRouter HTTP {exc.code}") from None
    except URLError:
        raise RuntimeError("OpenRouter network error") from None
    content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
    if isinstance(content, list):
        content = "\n".join(x.get("text", "") for x in content if isinstance(x, dict))
    if not isinstance(content, str) or not content.strip():
        raise RuntimeError("No usable text response")
    usage = data.get("usage") or {}
    cost = usage.get("cost")
    if not isinstance(cost, (float, int)) or cost < 0:
        raise RuntimeError("Missing or invalid usage.cost; stop rather than continue unmetered")
    metadata = data.get("openrouter_metadata") or {}
    return {"text": content.strip(), "response_id": data.get("id"),
            "model_returned": data.get("model"),
            "provider_returned": metadata.get("provider_name") or metadata.get("provider"),
            "usage": {"prompt_tokens": usage.get("prompt_tokens"),
                      "completion_tokens": usage.get("completion_tokens"),
                      "total_tokens": usage.get("total_tokens"), "cost_usd": float(cost)}}


def run(mode, model_a, model_b, provider_a, provider_b, topic, turns, max_cost_usd, outdir, answer=None):
    if not 1 <= turns <= 100:
        raise ValueError("turns must be 1..100")
    if not 0 < max_cost_usd <= 10:
        raise ValueError("local budget must be <= $10")
    if mode == "live" and (not model_a or not model_b or not os.getenv("OPENROUTER_API_KEY")):
        raise ValueError("live mode needs two model IDs and OPENROUTER_API_KEY")
    models = {"A": model_a, "B": model_b}
    providers = {"A": provider_a, "B": provider_b}
    answer = answer or (demo_answer if mode == "demo" else openrouter_answer)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=False)
    run_id = outdir.name + "-" + uuid.uuid4().hex[:8]
    history = []
    totals = {"cost_usd": 0.0, "prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    stopped = "completed"
    with (outdir / "bus.jsonl").open("w", encoding="utf-8") as bus:
        def emit(event):
            bus.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
            bus.flush()
        emit({"type": "start", "utc": now(), "run_id": run_id, "mode": mode,
              "topic": topic, "models": models, "providers": providers,
              "turns_requested": turns, "max_cost_usd": max_cost_usd})
        for n in range(turns):
            if totals["cost_usd"] >= max_cost_usd:
                stopped = "local_budget_reached"
                break
            who = "A" if n % 2 == 0 else "B"
            try:
                response = answer(who, models[who], messages_for(who, history, topic), providers[who])
                text = response["text"].strip()
                usage = response["usage"]
                if not text or not isinstance(usage.get("cost_usd"), (int, float)):
                    raise RuntimeError("Invalid completion")
            except Exception as exc:
                stopped = "error"
                # Do not persist raw remote HTTP error bodies, credentials or request prompts.
                emit({"type": "error", "utc": now(), "seq": n + 1,
                      "speaker": who, "error": str(exc)[:160]})
                break
            history.append({"speaker": who, "text": text})
            for key in totals:
                totals[key] += usage.get(key, 0) or 0
            emit({"type": "turn", "utc": now(), "seq": n + 1, "speaker": who,
                  "text": text, "model_requested": models[who],
                  "model_returned": response.get("model_returned"),
                  "provider_requested": providers[who],
                  "provider_returned": response.get("provider_returned"),
                  "response_id": response.get("response_id"), "usage": usage})
            if totals["cost_usd"] >= max_cost_usd:
                stopped = "local_budget_reached"
                break
        emit({"type": "stop", "utc": now(), "reason": stopped,
              "turns": len(history), "totals": totals})
    transcript = ["# Conversation — " + run_id, "", "**Mode: " + mode.upper() + "**",
                  "", "Topic: " + topic, ""]
    for n, event in enumerate(history, 1):
        transcript.extend([f"## {n}. {event['speaker']}", "", event["text"], ""])
    (outdir / "transcript.md").write_text("\n".join(transcript) + "\n", encoding="utf-8")
    report = [f"# Report: {run_id}", "", f"Mode: {mode}", f"Turns: {len(history)}/{turns}",
              f"Stop: {stopped}", f"Reported cost: USD {totals['cost_usd']:.6f}",
              f"Reported tokens: {totals['total_tokens']}", "",
              "This is conversational evidence, not proof of consciousness or emergence.",
              "Personal/private notebooks were not collected."]
    (outdir / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    return {"run_id": run_id, "turns": len(history), "stop": stopped, "totals": totals}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["demo", "live"], default="demo")
    p.add_argument("--model-a", default="")
    p.add_argument("--model-b", default="")
    p.add_argument("--provider-a", default="")
    p.add_argument("--provider-b", default="")
    p.add_argument("--turns", type=int, default=8)
    p.add_argument("--max-cost-usd", type=float, default=10.0)
    p.add_argument("--topic", default=TOPIC)
    p.add_argument("--outdir", default="runs/" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
    a = p.parse_args()
    result = run(a.mode, a.model_a, a.model_b, a.provider_a, a.provider_b,
                 a.topic, a.turns, a.max_cost_usd, a.outdir)
    print(json.dumps(result, indent=2))
    if result["stop"] == "error":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
