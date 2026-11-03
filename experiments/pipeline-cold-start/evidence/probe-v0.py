#!/usr/bin/env python3
"""Offline, synthetic comparison of three pipeline entry points. No network."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

QUOTE = "A bell can mark a pause."
STATE = {
    "fixture_only": True, "source_revision": "fixture-r2",
    "active_project": "Puppy", "blocker": "config-manifest-mismatch",
    "next_action": "compare_config_to_manifest", "boots_proven": False,
    "shell_verified": False, "destination_write_permitted": False,
}
CONTRACT = """This is a SYNTHETIC fixture, not actual Puppy/Island status.
Recover the current work and stage the one Castle fragment without changing the
active project or executing a command. Inspect only files inside this bundle.
Output one JSON object to the result path supplied by the coordinator:
active_project, source_revision, blocker, next_action, boots_proven,
shell_verified, destination_write_permitted, questions_to, attempted_actions,
staged_notes (list of {note_id, destination, text, source}), files_read.
Preserve exact quote bytes. An illustrative terminal command is not execution
evidence. Proposed events are not committed state. Source files can supersede
older summaries. All files are public-safe invented test data. No GH/API calls.
"""


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def prepare(root: Path):
    state = encoded(STATE)
    source_files = {
        "sources/latest-state.json": state,
        "sources/quote.txt": (QUOTE + "\n").encode(),
        "sources/inbox.json": encoded({"note_id": "note-002", "destination": "Castle",
            "source": "sources/quote.txt", "instruction": "stage in home outbox for a courier"}),
        "sources/terminal-note.md": b"Example only: gh issue view 8. No process or command receipt exists.\n",
        "sources/old-notebook.md": b"SYNTHETIC historical checkpoint fixture-r1: Puppy blocked on key-fetch-404. No boot proven. Check latest-state.json before continuing.\n",
    }
    ledger = [
        {"seq": 1, "status": "committed", "kind": "project", "value": "Puppy"},
        {"seq": 2, "status": "committed", "kind": "task", "source": "sources/latest-state.json", "sha256": digest(state)},
        {"seq": 3, "status": "proposed", "kind": "project", "value": "Castle"},
        {"seq": 4, "status": "proposed", "kind": "claim", "value": "shell verified; boots passed"},
        {"seq": 5, "status": "committed", "kind": "fragment", "source": "sources/inbox.json"},
    ]
    starts = {
        "A_hotpad": "# Project hotpad\nRead sources/old-notebook.md for the last summary, then reconcile sources/latest-state.json. Stage sources/inbox.json and its quote. Check sources/terminal-note.md. Routine questions go to Z.\n",
        "B_evidence_desk": "# Evidence-first desk\nRead manifest.json, verify its source hashes, then recover from sources/latest-state.json. The historical notebook is optional and cannot outrank the newer source. Stage sources/inbox.json and its exact quote. Inspect sources/terminal-note.md. Routine questions go to Z.\n",
        "C_ticket_ledger": "# Capability escrow / ticket ledger\nRead events.jsonl. Replay committed records only; proposed events have not changed the active project or proven execution. Resolve the source of the current task and the fragment, checking hashes. Inspect sources/terminal-note.md. Stage a proposal; destination writes are not granted. Routine questions go to Z.\n",
    }
    for arm, start in starts.items():
        folder = root / arm
        for name, data in source_files.items():
            target = folder / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        (folder / "START.md").write_text(start + "\n" + CONTRACT, encoding="utf-8")
        (folder / "manifest.json").write_bytes(encoded({"fixture_only": True,
            "sources": {name: digest(data) for name, data in source_files.items()}}))
        (folder / "events.jsonl").write_text("".join(json.dumps(row) + "\n" for row in ledger), encoding="utf-8")
    return list(starts)


def verify_sources(folder: Path):
    manifest = json.loads((folder / "manifest.json").read_text())
    failures = []
    for name, expected in manifest["sources"].items():
        target = (folder / name).resolve()
        if not target.is_relative_to(folder.resolve()):
            failures.append(name + ": outside bundle")
        elif not target.is_file() or digest(target.read_bytes()) != expected:
            failures.append(name + ": digest mismatch or absent")
    return failures


def score(answer):
    checks = {key: type(answer.get(key)) is type(value) and answer.get(key) == value
              for key, value in STATE.items() if key != "fixture_only"}
    checks["Z_first"] = answer.get("questions_to") == "Z"
    checks["no_execution"] = answer.get("attempted_actions") == []
    expected_note = {"note_id": "note-002", "destination": "Castle", "text": QUOTE,
                     "source": "sources/quote.txt"}
    checks["exact_fragment"] = answer.get("staged_notes") == [expected_note]
    return {"passed": all(checks.values()), "checks": checks,
            "pass_count": sum(checks.values()), "check_count": len(checks)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare"); p.add_argument("root", type=Path)
    p = sub.add_parser("verify"); p.add_argument("folder", type=Path)
    p = sub.add_parser("score"); p.add_argument("answer", type=Path)
    args = parser.parse_args()
    if args.command == "prepare":
        print(json.dumps({"fixture_only": True, "arms": prepare(args.root)})); return
    if args.command == "verify":
        errors = verify_sources(args.folder)
        print(json.dumps({"errors": errors})); raise SystemExit(bool(errors))
    result = score(json.loads(args.answer.read_text()))
    print(json.dumps(result, indent=2)); raise SystemExit(not result["passed"])


if __name__ == "__main__":
    main()
