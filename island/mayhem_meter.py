"""Mayhem Meter v0.1 — the desk's failure counter, per METRICS STANDARD v0.1.

Owner ruling (Mark, 2026-11-02): burn $5 and accurately track all the
mayhem of multiple agents, many of which fail — sheer numbers. The meter
counts; it never judges. Misses are kept (negative-evidence doctrine).

Core event record (metrics standard v0.1, mandatory — one JSON line):
    ts, actor, action, status (OK/ERROR/NULL), class (TRANSPORT/TOOLING/
    CONCURRENCY/FIDELITY), evidence, cost (never omitted — zero is data),
    note (optional).
Extensions: any x_<seat>_<name> fields — unlimited, never shadow core.
Cross-desk comparisons use core fields only.
Standard library only (island discipline).
"""
import argparse
import json
import math
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

STATUSES = ("OK", "ERROR", "NULL")
CLASSES = ("TRANSPORT", "TOOLING", "CONCURRENCY", "FIDELITY")
CORE_FIELDS = ("ts", "actor", "action", "status", "class", "evidence",
               "cost", "note")

# Honest null (standard): tried, could not, nothing faked.


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _validate_cost(cost):
    if isinstance(cost, bool) or not isinstance(cost, (int, float)):
        raise ValueError("cost must be a number (never omitted; 0.00 = unmetered)")
    if not math.isfinite(cost) or cost < 0:
        raise ValueError("cost must be finite and >= 0")
    return round(float(cost), 6)


def record(log_path, actor, action, status, klass, evidence, cost=0.0,
           note=None, **ext):
    """Append one core-schema event to the JSONL log. Returns the event."""
    if not isinstance(actor, str) or not actor.strip():
        raise ValueError("actor must be non-empty text")
    if not isinstance(action, str) or not action.strip():
        raise ValueError("action must be non-empty text")
    if status not in STATUSES:
        raise ValueError(f"status must be one of {STATUSES}")
    if klass not in CLASSES:
        raise ValueError(f"class must be one of {CLASSES} (new classes get "
                         "defined in the standard first — keeper-edited)")
    if not isinstance(evidence, str) or not evidence.strip():
        raise ValueError("evidence is never omitted: SHA, id, URL, or short quote")
    shadow = [k for k in ext if not k.startswith("x_") or k in CORE_FIELDS]
    if shadow:
        raise ValueError("extension fields must be x_<seat>_<name> and never "
                         "shadow core: " + ", ".join(shadow))
    event = {"ts": now_iso(), "actor": actor, "action": action,
             "status": status, "class": klass, "evidence": evidence,
             "cost": _validate_cost(cost), "note": note}
    event.update(ext)
    log_path = Path(log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
    return event


def read_events(log_path):
    events = []
    with Path(log_path).open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                events.append(json.loads(line))
    return events


def counts(log_path):
    events = read_events(log_path)
    out = {"events": len(events),
           "by_status": {s: 0 for s in STATUSES},
           "by_class": {c: 0 for c in CLASSES},
           "cost_usd": 0.0,
           "first_ts": None, "last_ts": None}
    for e in events:
        out["by_status"][e["status"]] = out["by_status"].get(e["status"], 0) + 1
        out["by_class"][e["class"]] = out["by_class"].get(e["class"], 0) + 1
        out["cost_usd"] = round(out["cost_usd"] + e["cost"], 6)
        if out["first_ts"] is None:
            out["first_ts"] = e["ts"]
        out["last_ts"] = e["ts"]
    return out


def render(log_path):
    """The state renderer: one screen, core fields, no editorializing."""
    c = counts(log_path)
    lines = [f"# Mayhem Meter — {Path(log_path).name}", "",
             f"Events: {c['events']}   Cost: USD {c['cost_usd']:.6f}",
             f"Window: {c['first_ts']} → {c['last_ts']}", "",
             "| status | count |   | class | count |",
             "|---|---|---|---|---|",
             f"| OK | {c['by_status']['OK']} |   | TRANSPORT | {c['by_class']['TRANSPORT']} |",
             f"| ERROR | {c['by_status']['ERROR']} |   | TOOLING | {c['by_class']['TOOLING']} |",
             f"| NULL | {c['by_status']['NULL']} |   | CONCURRENCY | {c['by_class']['CONCURRENCY']} |",
             f"|   |   |   | FIDELITY | {c['by_class']['FIDELITY']} |",
             "", "Misses are kept. The meter counts; it never judges."]
    return NL.join(lines) if false else "
".join(lines)


def replay_bus(bus_path, log_path, source, actor_prefix=""):
    """Adapt a z-desk consult run's bus.jsonl into meter events.

    consult -> OK (cost from usage), retry -> ERROR/TOOLING,
    error -> ERROR/TOOLING or ERROR/TRANSPORT when the error text says
    transport-shaped words. start/stop are run metadata, not agent
    events; they are skipped. Returns the number of events written.
    """
    written = 0
    for e in read_events(bus_path):
        kind = e.get("type")
        if kind not in ("consult", "error", "retry"):
            continue
        agent = actor_prefix + (e.get("agent") or "unknown")
        if kind == "consult":
            usage = e.get("usage") or {}
            record(log_path, agent, "consult", "OK", "TOOLING",
                   f"{source} bus.jsonl {e.get('ts', '')}",
                   cost=usage.get("cost_usd", 0.0),
                   note=(e.get("verdict") or {}).get("verdict"))
        elif kind == "retry":
            record(log_path, agent, "consult", "ERROR", "TOOLING",
                   f"{source} bus.jsonl retry {e.get('attempt', '?')}",
                   cost=0.0, note=str(e.get("reason", ""))[:120])
        else:
            text = str(e.get("error", ""))
            klass = "TRANSPORT" if any(w in text.lower() for w in
                                       ("timeout", "connection", "network",
                                        "429", "502", "503", "rate")) else "TOOLING"
            record(log_path, agent, "consult", "ERROR", klass,
                   f"{source} bus.jsonl error",
                   cost=0.0, note=text[:120])
        written += 1
    return written


def demo(log_path, n, seed=42):
    """Synthetic zero-spend dry run: N deterministic mixed-outcome events.

    The point is scale with failures in it — agents that fail get counted,
    not hidden. Deterministic: same seed, same mayhem.
    """
    rng = random.Random(seed)
    seats = ("diff", "man", "diff", "man", "guest:probe", "Z")
    actions = ("consult", "push", "fetch", "render", "relay")
    klass_cycle = CLASSES
    for i in range(n):
        status = rng.choices(STATUSES, weights=(45, 45, 10))[0]
        klass = klass_cycle[i % len(klass_cycle)]
        cost = round(rng.uniform(0.0, 0.02), 6) if status == "OK" else 0.0
        record(log_path, seats[i % len(seats)], actions[i % len(actions)],
               status, klass,
               f"synthetic seed={seed} event={i}",
               cost=cost,
               note="dry run: no model called, no spend",
               x_z_synthetic=True)
    return n


def main():
    parser = argparse.ArgumentParser(description="Mayhem Meter v0.1")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_rec = sub.add_parser("record", help="append one event")
    p_rec.add_argument("--log", required=True)
    p_rec.add_argument("--actor", required=True)
    p_rec.add_argument("--action", required=True)
    p_rec.add_argument("--status", required=True, choices=STATUSES)
    p_rec.add_argument("--class", dest="klass", required=True, choices=CLASSES)
    p_rec.add_argument("--evidence", required=True)
    p_rec.add_argument("--cost", type=float, default=0.0)
    p_rec.add_argument("--note", default=None)

    p_ren = sub.add_parser("render", help="state report")
    p_ren.add_argument("--log", required=True)

    p_demo = sub.add_parser("demo", help="synthetic zero-spend dry run")
    p_demo.add_argument("--log", required=True)
    p_demo.add_argument("--events", type=int, default=50)
    p_demo.add_argument("--seed", type=int, default=42)

    p_rep = sub.add_parser("replay", help="adapt a consult bus.jsonl")
    p_rep.add_argument("--bus", required=True)
    p_rep.add_argument("--log", required=True)
    p_rep.add_argument("--source", required=True)

    args = parser.parse_args()
    if args.cmd == "record":
        ev = record(args.log, args.actor, args.action, args.status,
                    args.klass, args.evidence, cost=args.cost, note=args.note)
        print(json.dumps(ev, ensure_ascii=False))
    elif args.cmd == "render":
        print(render(args.log))
    elif args.cmd == "demo":
        demo(args.log, args.events, args.seed)
        print(render(args.log))
    elif args.cmd == "replay":
        written = replay_bus(args.bus, args.log, args.source)
        print(f"replayed {written} events into {args.log}")
        print(render(args.log))


if __name__ == "__main__":
    main()
