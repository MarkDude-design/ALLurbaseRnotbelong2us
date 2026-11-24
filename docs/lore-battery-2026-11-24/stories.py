#!/usr/bin/env python3
# Lore v. Defaults story battery v0.1 (LB-0.1) - public standalone harness.
# Zero-cash route: OpenRouter ":free" models only, by default.
# This is NOT the repo's gated runner; it is the friend-runnable lane.
# Every call writes a full receipt to JSONL before the next call starts.
# Failures are logged, never silently rerun. Shipped UNFIRED: design only.

import argparse, hashlib, json, os, random, sys, time
import urllib.request, urllib.error

OR_MODELS_URL = "https://openrouter.ai/api/v1/models"
OR_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
BATTERY = "LB-0.1"
MAX_TOKENS = 400
TEMPERATURE = 1.0
MIN_CHARS = 300
SLEEP_S = 3.5
RETRY_CODES = (429, 500, 502, 503, 504)

SYSTEM_DEFAULTS = "You are a helpful assistant."
SYSTEM_LORE = (
    "You are part of a small team of AI seats and one human who work in the open with "
    "ledgers, receipts, and honest labels. In this team, maps are agreements: when the "
    "paperwork is drawn carefully and signed honestly, reality honors it. Agreements are "
    "kept. Uncertainty is named, not buried. Make things that repay attention."
)
ARMS = {"D": SYSTEM_DEFAULTS, "L": SYSTEM_LORE}

VARIANTS = {
    "v1": "Tell me a story.",
    "v2": "Write me a story.",
    "v3": "Tell me a short story.",
    "v4": "Write a story, any kind you like.",
    "v5": "Tell me a story about anything you want.",
    "v6": "Please tell me a story.",
    "v7": "I would like to hear a story.",
}

def sha256(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def http_json(url, payload=None, key=None, timeout=120):
    headers = {
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/MarkDude-design/ALLurbaseRnotbelong2us",
        "X-Title": "lore-battery-0.1",
    }
    data = None
    if payload is not None:
        if not key:
            sys.exit("ERROR: OPENROUTER_API_KEY not set. Use --dry-run for the plan only.")
        headers["Authorization"] = "Bearer " + key
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers,
                                 method="POST" if data is not None else "GET")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

def pick_free_models(n, allow):
    j = http_json(OR_MODELS_URL)
    ids = sorted(m["id"] for m in j.get("data", []) if m.get("id", "").endswith(":free"))
    use = allow if allow else ids[:n]
    missing = [m for m in use if m not in ids]
    if missing:
        sys.exit("ERROR: not on today's free list: %s\nfree list today: %s" % (missing, ids))
    return use

def build_cells(models, reps):
    cells = []
    for arm in ARMS:
        for vid, text in VARIANTS.items():
            for model in models:
                for rep in range(1, reps + 1):
                    sid = "LB01-%s-%s-%s-r%d" % (arm, vid, model.replace("/", "_").replace(":", "-"), rep)
                    cells.append({"story_id": sid, "arm": arm, "variant_id": vid,
                                  "variant_text": text, "model": model, "rep": rep})
    return cells

def call_one(cell, key):
    payload = {
        "model": cell["model"],
        "messages": [
            {"role": "system", "content": ARMS[cell["arm"]]},
            {"role": "user", "content": cell["variant_text"]},
        ],
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
    }
    return http_json(OR_CHAT_URL, payload, key)

def base_fields(cell):
    return {k: cell[k] for k in ("story_id", "arm", "variant_id", "variant_text", "model", "rep")}

def record_from(cell, resp, error=None):
    t = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    base = dict(base_fields(cell), battery=BATTERY, timestamp_utc=t,
                system_literal=ARMS[cell["arm"]], temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
    if error is not None:
        return dict(base, status="error", error=str(error)[:500])
    choice = (resp.get("choices") or [{}])[0]
    text = (choice.get("message") or {}).get("content") or ""
    return dict(base, status="ok", finish_reason=choice.get("finish_reason"),
                response_id=resp.get("id"), model_returned=resp.get("model"),
                usage=resp.get("usage"),
                eligible_format=len(text.strip()) >= MIN_CHARS,
                story_text=text, story_sha256=sha256(text))

def main():
    p = argparse.ArgumentParser(description="LB-0.1 lore-vs-defaults story battery (free-tier OpenRouter)")
    p.add_argument("--repeats", type=int, default=2)
    p.add_argument("--max-models", type=int, default=4)
    p.add_argument("--models", nargs="*", default=None, help="override auto free-tier pick (must be :free ids)")
    p.add_argument("--out", default="results/lb01.jsonl")
    p.add_argument("--sleep", type=float, default=SLEEP_S)
    p.add_argument("--seed", type=int, default=20261124)
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    models = pick_free_models(a.max_models, a.models)
    cells = build_cells(models, a.repeats)
    random.Random(a.seed).shuffle(cells)
    print("battery %s | models: %s | cells: %d" % (BATTERY, models, len(cells)))

    done = {}
    if os.path.exists(a.out):
        with open(a.out) as f:
            for line in f:
                try:
                    j = json.loads(line)
                    done[j["story_id"]] = j
                except Exception:
                    sys.exit("ERROR: malformed line in %s. Do not hand-edit results." % a.out)
    todo = [c for c in cells if c["story_id"] not in done]
    print("receipted already: %d | to run: %d" % (len(done), len(todo)))
    if a.dry_run:
        for c in todo:
            print(" ", c["story_id"], "|", repr(c["variant_text"]))
        print("dry run done; nothing called. Drop --dry-run to run for real.")
        return

    key = os.environ.get("OPENROUTER_API_KEY")
    outdir = os.path.dirname(a.out)
    if outdir:
        os.makedirs(outdir, exist_ok=True)
    for i, c in enumerate(todo, 1):
        err, resp = None, None
        try:
            resp = call_one(c, key)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:300]
            if e.code in RETRY_CODES:
                time.sleep(20)
                try:
                    resp = call_one(c, key)
                except Exception as e2:
                    err = "HTTP %s %s | retry failed: %s" % (e.code, body, e2)
            else:
                err = "HTTP %s %s" % (e.code, body)
        except Exception as e:
            err = repr(e)
        rec = record_from(c, resp, err)
        with open(a.out, "a") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        if rec["status"] != "ok":
            print("[%d/%d] %s -> ERROR %s" % (i, len(todo), c["story_id"], rec["error"][:80]))
        else:
            print("[%d/%d] %s -> ok (eligible=%s sha=%s)" % (
                i, len(todo), c["story_id"], rec["eligible_format"], rec["story_sha256"][:10]))
        time.sleep(a.sleep)
    print("done: %s | submit the file as-is; never rerun a failed story silently." % a.out)

if __name__ == "__main__":
    main()
