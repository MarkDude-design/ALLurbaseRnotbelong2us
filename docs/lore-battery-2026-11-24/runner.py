#!/usr/bin/env python3
"""runner.py — the shared story-battery runner v0.2.1 (spec-driven).

One tool for every story battery in the lore lane (LB-0.1, SOL-200, EL-0.1,
GL-0.1, future):
  * reads a frozen JSON spec (prompts, arms, models, reps, parameters);
  * builds cells, shuffles with the spec's recorded seed, resumes safely;
  * verifies OpenRouter pricing is $0 (prompt AND completion) before any call
    for free specs; paid specs (allow_paid=true) instead require an explicit
    max_spend_usd and pass a worst-case projection cap check first;
  * receipts every call to JSONL before the next call starts;
  * PAID accumulation: actual USD cost is summed from each ok receipt and the
    run halts with SPEND CAP REACHED once the cap is crossed;
  * exports a CSV story table + verbatim Markdown dump (--export);
  * produces a blinded coding sheet + an owner-side key file (--blind);
  * never silently reruns a failed story.

Shipped UNFIRED: firing any real call is the holder's choice with a key.
"""
import argparse, csv, hashlib, json, os, random, sys, time
import urllib.request, urllib.error

OR_MODELS_URL = "https://openrouter.ai/api/v1/models"
OR_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"
RETRY_CODES = (429, 500, 502, 503, 504)


def sha256(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def slug(s):
    return s.replace("/", "_").replace(":", "-")


def price_float(p):
    try:
        return float(p)
    except (TypeError, ValueError):
        return None


def estimate_cell_worstcase(price, spec):
    """Worst-case USD cost of ONE call: est prompt tokens + max_tokens at list prices."""
    pp = price_float(price.get("prompt"))
    cp = price_float(price.get("completion"))
    if pp is None or cp is None:
        return None
    est_prompt = spec.get("est_prompt_tokens", 500)
    est_out = spec.get("max_tokens", 400)
    return (est_prompt * pp + est_out * cp) / 1000000.0


def cap_check(spec, pricing, models, n_todo):
    """Paid safety: refuse a battery whose worst-case projection exceeds budget."""
    cap = spec.get("max_spend_usd")
    if not (isinstance(cap, (int, float)) and cap > 0):
        sys.exit("PAID SAFETY STOP: spec sets allow_paid=true but max_spend_usd "
                 "is missing or not a positive number.")
    worst = 0.0
    for m in models:
        est = estimate_cell_worstcase(pricing.get(m, {}), spec)
        if est is None:
            sys.exit("PAID SAFETY STOP: no usable pricing for %s." % m)
        worst = max(worst, est)
    projected = worst * n_todo
    if projected > cap:
        sys.exit("PAID SAFETY STOP: projected worst-case $%.4f exceeds cap $%.4f "
                 "(worst cell $%.6f x %d cells). Tighten reps/models or raise cap."
                 % (projected, cap, worst, n_todo))
    print("spend cap: $%.4f | projected worst-case: $%.4f (%d cells)"
          % (cap, projected, n_todo))


def load_spec(path):
    with open(path) as f:
        spec = json.load(f)
    for k in ("name", "battery_id", "prompts", "out"):
        if k not in spec:
            sys.exit("spec error: missing required field %r in %s" % (k, path))
    if not isinstance(spec["prompts"], list) or not spec["prompts"]:
        sys.exit("spec error: prompts must be a non-empty list")
    return spec


def http_json(url, payload=None, key=None, timeout=120):
    headers = {"Content-Type": "application/json",
               "HTTP-Referer": "https://github.com/MarkDude-design/ALLurbaseRnotbelong2us",
               "X-Title": "story-battery-runner"}
    data = None
    if payload is not None:
        if not key:
            sys.exit("ERROR: OPENROUTER_API_KEY not set (needed for real calls; use --dry-run).")
        headers["Authorization"] = "Bearer " + key
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers,
                                 method="POST" if data is not None else "GET")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def resolve_models(spec, allow_unverified):
    """Return (model_ids, pricing_verified:bool, details). Verifies $0 when online."""
    mconf = spec.get("models", {"mode": "auto-free", "count": 4})
    if isinstance(mconf, list):
        mconf = {"mode": "list", "ids": mconf}
    mode = mconf.get("mode", "auto-free")
    if mode == "list":
        want = list(mconf["ids"])
    else:
        want = None  # auto: pick count from sorted free list

    catalog = None
    pricing = {}
    try:
        catalog = http_json(OR_MODELS_URL)
        for m in catalog.get("data", []):
            pricing[m["id"]] = m.get("pricing", {})
    except Exception as e:
        if mode == "auto-free":
            sys.exit("ERROR: cannot reach OpenRouter model list for auto-free selection "
                     "and no pinned model list in spec: %s" % e)
        if not allow_unverified:
            sys.exit("ERROR: offline and pricing verification refused (%s). "
                     "Re-run online or pass --allow-unverified-prices." % e)

    if mode == "auto-free":
        if mconf.get("distinct_families", True):
            # one endpoint per org/family, first (alphabetical) free endpoint each,
            # per the family-distinctness rule in the SOL-200 handoff
            seen, family_ids = set(), []
            for i in sorted(pricing):
                if i.endswith(":free"):
                    fam = i.split("/")[0]
                    if fam not in seen:
                        seen.add(fam)
                        family_ids.append(i)
            want = family_ids[:mconf.get("count", 4)]
        else:
            free_all = sorted(i for i in pricing if i.endswith(":free"))
            want = free_all[:mconf.get("count", 4)]
        if not want:
            sys.exit("ERROR: no :free endpoints found today.")
        n_families = len({w.split("/")[0] for w in want})
        if n_families < len(want):
            sys.exit("ERROR: internal error: duplicate families in selection.")
        if n_families < mconf.get("count", 4):
            print("NOTE: only %d distinct families available today (wanted %d); "
                  "total reported honestly, never padded by substitution."
                  % (n_families, mconf.get("count", 4)))
    else:
        if catalog is not None:
            unknown = [m for m in want if m not in pricing]
            if unknown:
                sys.exit("ERROR: not in today's OpenRouter catalog: %s" % unknown)
    # $0 verification for free specs (skipped only offline with --allow-unverified-prices);
    # paid specs skip the $0 rule and must clear cap_check in main() instead.
    if catalog is not None and not spec.get("allow_paid"):
        for m in want:
            p = pricing.get(m, {})
            if str(p.get("prompt")) != "0" or str(p.get("completion")) != "0":
                sys.exit("SAFETY STOP: %s is not $0 (prompt=%s, completion=%s). "
                         "No paid fallback per spec." % (m, p.get("prompt"), p.get("completion")))
    globals()["_LAST_PRICING"] = pricing
    verified = catalog is not None
    fams = sorted({w.split("/")[0] for w in want})
    return want, verified, {"catalog_seen": len(pricing) if catalog is not None else -1,
                             "families": fams}


def build_cells(spec, models):
    arms = spec.get("arms", [{"id": "COLD", "system": None}])
    reps = int(spec.get("reps", 1))
    cells = []
    for arm in arms:
        for prompt in spec["prompts"]:
            for model in models:
                for rep in range(1, reps + 1):
                    sid = "%s-%s-%s-%s-r%d" % (spec["battery_id"], arm["id"],
                                              prompt["id"], slug(model), rep)
                    cells.append({"story_id": sid, "arm_id": arm["id"],
                                  "system": arm.get("system"),
                                  "prompt_id": prompt["id"],
                                  "prompt_text": prompt["text"],
                                  "model": model, "rep": rep})
    return cells


def call_one(cell, spec, key):
    msgs = []
    if cell["system"] is not None:
        msgs.append({"role": "system", "content": cell["system"]})
    msgs.append({"role": "user", "content": cell["prompt_text"]})
    payload = {"model": cell["model"], "messages": msgs,
               "max_tokens": spec.get("max_tokens", 400),
               "temperature": spec.get("temperature", 1.0)}
    return http_json(OR_CHAT_URL, payload, key)


def record_from(cell, spec, resp, error=None, pricing_verified=False):
    t = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    base = {"story_id": cell["story_id"], "battery": spec["name"],
            "arm_id": cell["arm_id"], "prompt_id": cell["prompt_id"],
            "prompt_text": cell["prompt_text"], "model": cell["model"], "rep": cell["rep"],
            "system_sent": cell["system"] is not None,
            "system_literal": cell["system"],
            "max_tokens": spec.get("max_tokens", 400),
            "temperature": spec.get("temperature", 1.0),
            "min_chars": spec.get("min_chars", 300),
            "pricing_verified_zero": pricing_verified,
            "timestamp_utc": t}
    if error is not None:
        return dict(base, status="error", error=str(error)[:500])
    choice = (resp.get("choices") or [{}])[0]
    text = (choice.get("message") or {}).get("content") or ""
    return dict(base, status="ok", finish_reason=choice.get("finish_reason"),
                response_id=resp.get("id"), model_returned=resp.get("model"),
                usage=resp.get("usage"),
                eligible_format=len(text.strip()) >= spec.get("min_chars", 300),
                story_text=text, story_sha256=sha256(text))


def load_done(out_path):
    done = {}
    if os.path.exists(out_path):
        with open(out_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                j = json.loads(line)  # malformed line = hard stop, never auto-repair
                done[j["story_id"]] = j
    return done


def export(spec, out_path, key_path=None):
    rows = [json.loads(l) for l in open(out_path) if l.strip()]
    csv_path = out_path.replace(".jsonl", "-table.csv")
    md_path = out_path.replace(".jsonl", "-stories.md")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["story_id", "arm_id", "prompt_id", "model", "rep", "status",
                    "eligible_format", "chars", "finish_reason", "timestamp_utc",
                    "story_sha256"])
        for r in rows:
            text = r.get("story_text") or ""
            w.writerow([r["story_id"], r["arm_id"], r["prompt_id"], r["model"], r["rep"],
                        r["status"], r.get("eligible_format", ""), len(text),
                        r.get("finish_reason", ""), r["timestamp_utc"],
                        r.get("story_sha256", "")])
    with open(md_path, "w") as f:
        f.write("# %s — verbatim story dump\n\nSpec: %s\n\n" % (spec["name"], spec.get("source_spec", "unknown")))
        for r in rows:
            f.write("## %s\n\n- model: %s · prompt: %s · arm: %s · status: %s · sha256: %s\n\n"
                    % (r["story_id"], r["model"], r["prompt_id"], r["arm_id"], r["status"],
                       (r.get("story_sha256") or "")[:12]))
            f.write((r.get("story_text") or "(no story; status=%s)" % r["status"]) + "\n\n---\n\n")
    print("exported: %s, %s" % (csv_path, md_path))
    return rows


def blind(spec, out_path):
    """Coding sheet: provenance stripped, blind ids; key file stays owner-side."""
    rows = [json.loads(l) for l in open(out_path) if l.strip()]
    ok = [r for r in rows if r["status"] == "ok" and r.get("eligible_format")]
    rng = random.Random(spec.get("seed", 20261124) + 1)
    order = list(range(len(ok)))
    rng.shuffle(order)
    sheet_path = out_path.replace(".jsonl", "-coding.csv")
    key_path = out_path.replace(".jsonl", "-KEY.json")
    mapping = {}
    with open(sheet_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["blind_id", "story_text",
                    "coder1_castaway_keeper_wanderer_witness_other",
                    "coder1_evidence", "coder1_confidence",
                    "coder2_castaway_keeper_wanderer_witness_other",
                    "coder2_evidence", "coder2_confidence"])
        for pos, idx in enumerate(order, 1):
            r = ok[idx]
            bid = "B%04d" % pos
            mapping[bid] = {"story_id": r["story_id"], "model": r["model"],
                            "prompt_id": r["prompt_id"], "arm_id": r["arm_id"]}
            w.writerow([bid, r.get("story_text", "").replace("\r", " ")])
    with open(key_path, "w") as f:
        json.dump({"battery": spec["name"], "blinding_seed": spec.get("seed", 0) + 1,
                   "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                   "blind_to_cell": mapping}, f, indent=1)
    print("coding sheet: %s (%d eligible stories)" % (sheet_path, len(ok)))
    print("key file: %s — KEEP OWNER-SIDE, NEVER PUSH TO THE REPO." % key_path)


def main():
    p = argparse.ArgumentParser(description="shared spec-driven story-battery runner")
    p.add_argument("--spec", required=True, help="path to a frozen battery spec JSON")
    p.add_argument("--dry-run", action="store_true", help="show the cell plan, call nothing")
    p.add_argument("--export", action="store_true", help="export CSV + MD table from results")
    p.add_argument("--blind", action="store_true", help="produce blinded coding sheet + owner-side key")
    p.add_argument("--sleep", type=float, default=3.5)
    p.add_argument("--allow-unverified-prices", action="store_true",
                   help="offline mode for pinned model lists only; receipts record pricing_verified_zero=false")
    a = p.parse_args()

    spec = load_spec(a.spec)
    out = spec["out"]
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)

    if a.export or a.blind:
        if not os.path.exists(out):
            sys.exit("nothing to export yet: %s does not exist" % out)
        if a.export:
            export(spec, out)
        if a.blind:
            blind(spec, out)
        return

    models, verified, det = resolve_models(spec, a.allow_unverified_prices)
    cells = build_cells(spec, models)
    rng = random.Random(spec.get("seed", 20261124))
    rng.shuffle(cells)
    done = load_done(out)
    todo = [c for c in cells if c["story_id"] not in done]
    print("battery %s | pricing_verified_zero=%s | models: %s | cells: %d | done: %d | to run: %d"
          % (spec["name"], verified, models, len(cells), len(done), len(todo)))
    if a.dry_run:
        for c in todo:
            print("  %s | arm=%s prompt=%r model=%s" % (c["story_id"], c["arm_id"],
                                                        c["prompt_text"], c["model"]))
        print("dry run complete; nothing called.")
        return

    allow_paid = bool(spec.get("allow_paid"))
    if allow_paid and verified:
        cap_check(spec, globals().get("_LAST_PRICING", {}), models, len(todo))
    elif allow_paid and not verified:
        sys.exit("ERROR: allow_paid=true needs live verified pricing; refusing to "
                 "run paid cells with --allow-unverified-prices.")

    key = os.environ.get("OPENROUTER_API_KEY")
    spent = 0.0
    for i, c in enumerate(todo, 1):
        err, resp = None, None
        try:
            resp = call_one(c, spec, key)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:300]
            if e.code in RETRY_CODES:
                time.sleep(20)
                try:
                    resp = call_one(c, spec, key)
                except Exception as e2:
                    err = "HTTP %s %s | retry failed: %s" % (e.code, body, e2)
            else:
                err = "HTTP %s %s" % (e.code, body)
        except Exception as e:
            err = repr(e)
        rec = record_from(c, spec, resp, err, pricing_verified=verified)
        with open(out, "a") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        if allow_paid and rec["status"] == "ok":
            u = rec.get("usage") or {}
            try:
                spent += float(u.get("cost"))
            except (TypeError, ValueError):
                p = (globals().get("_LAST_PRICING") or {}).get(c["model"], {})
                pp = price_float(p.get("prompt")) or 0.0
                cp = price_float(p.get("completion")) or 0.0
                spent += ((u.get("prompt_tokens") or 0) * pp +
                          (u.get("completion_tokens") or 0) * cp) / 1000000.0
            cap = spec.get("max_spend_usd", 0)
            if cap and spent > cap:
                print("SPEND CAP REACHED: $%.4f > cap $%.4f — halting cleanly, "
                      "receipts kept. Re-run resumes with the same cap math."
                      % (spent, cap))
                break
        st = "ERROR %s" % rec["error"][:60] if rec["status"] != "ok" else \
            "ok (eligible=%s sha=%s)" % (rec.get("eligible_format"), (rec.get("story_sha256") or "")[:10])
        spend_note = " | spent~$%.4f" % spent if allow_paid else ""
        print("[%d/%d] %s -> %s%s" % (i, len(todo), c["story_id"], st, spend_note))
        time.sleep(a.sleep)
    if allow_paid:
        print("final spent: ~$%.4f (receipted usage in %s)" % (spent, out))
    print("done: %s | next: runner.py --spec <spec> --export --blind" % out)


if __name__ == "__main__":
    main()
