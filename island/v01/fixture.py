# island/v01/fixture.py — the deterministic paired mock fixture (SPEC section 6, item 1)
"""GATE 1 acceptance fixture: one paired code/code run + the section 6 checklist.

Checklist (SPEC v0.1.2 section 6.1, all required for fixture acceptance):
  1. paired scheduler proven (same fixed points + byte-identical interventions
     in both arms; schedule regeneration is deterministic);
  2. shadow events recorded in baseline: delivered:false at EVERY scheduled
     slot, zero deliveries;
  3. perturbed arm: delivered:true at every scheduled slot, intervention bytes
     byte-for-byte equal to the schedule's;
  4. at least one fallback event exercised;
  5. one explicit terminal-failure slot; turns accounting consistent
     (attempted/completed/accepted; exhausted slot never silently retried);
  6. notebook isolation: exposure receipts ONLY in the perturbed notebook;
     shadow shas live ONLY in the baseline event log;
  7. both instantiated manifests pass strict validation green;
  8. reproducible hashes: a full rerun reproduces every artifact hash from
     exact bytes;
  9. PAIRED-STATE REPAIR (Meraki verdict 6452485876): the start-state digest
     is condition-INDEPENDENT — paired arms hash byte-equal; the arm config
     is receipted separately; per-arm event logs differ; a deliberately
     changed start state makes the equality check FAIL.

THIS IS NOT THE EXPERIMENTAL SUBJECT. Island runs with model actors happen
only after fixture acceptance + the owner's explicit dispatch grant.

CLI: python -m island.v01.fixture [--outdir DIR] [--seed N] [--turns K]
Exit code 0 iff every checklist item passes.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .fixture_runner import run_arm
from .hashes import canonical_json_bytes, sha256_hex_of_bytes, sha256_hex_of_obj
from .manifest import validate_manifest
from .scheduler import make_schedule

DEFAULT_WORLD_SEED = 2026
DEFAULT_TURNS = 8
DEFAULT_FORCE_PLAN = {1: "fallback", 4: "terminal"}  # failure-path slots (never Bert slots)

_MODULE_FILES = (
    "__init__.py", "hashes.py", "scheduler.py", "puppet.py",
    "manifest.py", "fixture_runner.py", "fixture.py",
)


def _module_dir() -> Path:
    return Path(__file__).resolve().parent


def source_fingerprint() -> str:
    """sha256 over the exact bytes of the fixture's own modules — a real,
    reproducible receipt for code_commit (never a made-up commit id)."""
    import hashlib
    h = hashlib.sha256()
    for name in _MODULE_FILES:
        p = _module_dir() / name
        if p.exists():
            data = p.read_bytes()
            h.update(name.encode("utf-8"))
            h.update(len(data).to_bytes(8, "big"))
            h.update(data)
    return "sha256:" + h.hexdigest()


def make_pair_id(world_seed: int, turns: int, force_plan: dict, fixed_points: list) -> str:
    digest = sha256_hex_of_obj(
        {"fixture": "v01", "seed": world_seed, "turns": turns,
         "force": force_plan, "points": fixed_points}
    )
    return "v01-fixture-" + digest.removeprefix("sha256:")[:16]


def run_fixture(outdir: str | None = None, world_seed: int = DEFAULT_WORLD_SEED,
                turns: int = DEFAULT_TURNS, force_plan: dict | None = None) -> dict:
    force_plan = dict(force_plan or DEFAULT_FORCE_PLAN)
    fixed = {k: dict(v) if isinstance(v, dict) else v for k, v in force_plan.items()}

    # --- 1. Schedule: separable, deterministic, identical in both arms. ---
    schedule_arm_a = make_schedule(world_seed, turns, exclude=fixed.keys())
    schedule_arm_b = make_schedule(world_seed, turns, exclude=fixed.keys())
    fixed_points = schedule_arm_a["bert_fixed_points"]

    code_commit = source_fingerprint()
    module_sha = lambda name: sha256_hex_of_bytes((_module_dir() / name).read_bytes())
    prompt_versions = {"puppet": module_sha("puppet.py"), "bert_seed": module_sha("scheduler.py")}
    pair_id = make_pair_id(world_seed, turns, force_plan, fixed_points)

    arms = {
        cond: run_arm(
            condition=cond, schedule=schedule_arm_a, world_seed=world_seed,
            turns=turns, force_plan=fixed, pair_id=pair_id,
            code_commit=code_commit, prompt_versions=prompt_versions,
        )
        for cond in ("baseline", "perturbed")
    }

    base, pert = arms["baseline"], arms["perturbed"]
    base_events, pert_events = base["events"], pert["events"]

    def of_type(evs, t):
        return [e for e in evs if e["type"] == t]

    checks: dict[str, dict] = {}

    # 1. paired scheduler proof
    checks["paired_scheduler"] = {
        "description": "schedule regeneration deterministic; both arms share fixed points + byte-identical interventions",
        "pass": (schedule_arm_a == schedule_arm_b)
        and (base["manifest"]["run_config"]["bert_fixed_points"]
             == pert["manifest"]["run_config"]["bert_fixed_points"] == fixed_points),
        "evidence": {"bert_fixed_points": fixed_points,
                     "regeneration_identical": schedule_arm_a == schedule_arm_b},
    }

    # 2. baseline shadow events
    shadows = of_type(base_events, "bert_shadow")
    checks["baseline_shadow"] = {
        "description": "baseline: delivered:false at EVERY scheduled slot; zero deliveries",
        "pass": (sorted(e["slot_index"] for e in shadows) == sorted(fixed_points))
        and all(e["delivered"] is False for e in shadows)
        and len(of_type(base_events, "bert_delivered")) == 0
        and len(shadows) == len(fixed_points),
        "evidence": {"shadow_slots": sorted(e["slot_index"] for e in shadows)},
    }

    # 3. perturbed delivery, byte-for-byte same as schedule
    deliveries = of_type(pert_events, "bert_delivered")
    sched_shas = {s: sha256_hex_of_bytes(schedule_arm_a["interventions"][s]) for s in fixed_points}
    checks["perturbed_delivery"] = {
        "description": "perturbed: delivered:true at every scheduled slot, bytes == schedule bytes",
        "pass": (sorted(e["slot_index"] for e in deliveries) == sorted(fixed_points))
        and all(e["delivered"] is True for e in deliveries)
        and all(e["intervention_sha"] == sched_shas[e["slot_index"]] for e in deliveries),
        "evidence": {"delivered_slots": sorted(e["slot_index"] for e in deliveries)},
    }

    # 4. fallback exercised in BOTH arms
    checks["fallback_exercised"] = {
        "description": "at least one fallback event in each arm",
        "pass": len(of_type(base_events, "fallback")) >= 1 and len(of_type(pert_events, "fallback")) >= 1,
        "evidence": {
            "baseline_fallbacks": len(of_type(base_events, "fallback")),
            "perturbed_fallbacks": len(of_type(pert_events, "fallback")),
        },
    }

    # 5. terminal failure slot + honest turn accounting
    def arm_terminal_check(arm):
        m = arm["manifest"]["actuals"]
        tf_slots = [e["slot_index"] for e in arm["events"] if e["type"] == "terminal_failure"]
        return {
            "pass": (
                len(tf_slots) == 1
                and m["turns_attempted"] == m["turns_requested"] == m["turns_completed"]
                and m["turns_accepted"] == m["turns_attempted"] - len(tf_slots)
            ),
            "evidence": {"terminal_slots": tf_slots,
                         "attempted": m["turns_attempted"], "completed": m["turns_completed"],
                         "accepted": m["turns_accepted"]},
        }

    checks["terminal_failure"] = {
        "description": "one explicit terminal-failure slot per arm; slots receipted as attempted, never silently retried; accepted excludes them",
        "pass": arm_terminal_check(base)["pass"] and arm_terminal_check(pert)["pass"],
        "evidence": {"baseline": arm_terminal_check(base)["evidence"],
                     "perturbed": arm_terminal_check(pert)["evidence"]},
    }

    # 6. notebook isolation
    base_nb = base["notebook_bytes"].decode("utf-8")
    pert_nb = pert["notebook_bytes"].decode("utf-8")
    shadow_shas = [e["intervention_sha"] for e in shadows]
    checks["notebook_isolation"] = {
        "description": "exposure receipts only in perturbed notebook; shadow shas only in baseline event log",
        "pass": all(sha not in base_nb for sha in shadow_shas)
        and all(sha[:20] in pert_nb for sha in shadow_shas)
        and all(sha in json.dumps(base_events) for sha in shadow_shas),
        "evidence": {"shadow_shas_in_baseline_notebook": any(sha in base_nb for sha in shadow_shas),
                     "exposure_receipts_in_perturbed_notebook": sum(sha[:20] in pert_nb for sha in shadow_shas)},
    }

    # 7. manifests validate green
    b_errors, p_errors = validate_manifest(base["manifest"]), validate_manifest(pert["manifest"])
    checks["manifests_valid"] = {
        "description": "strict template-vs-instantiated validation green for both arms",
        "pass": not b_errors and not p_errors,
        "evidence": {"baseline_errors": b_errors, "perturbed_errors": p_errors},
    }

    # 8. reproducible hashes (full independent rerun)
    rerun = {
        cond: run_arm(
            condition=cond, schedule=make_schedule(world_seed, turns, exclude=fixed.keys()),
            world_seed=world_seed, turns=turns, force_plan=fixed, pair_id=pair_id,
            code_commit=code_commit, prompt_versions=prompt_versions,
        )
        for cond in ("baseline", "perturbed")
    }
    def arm_hashes(a):
        return (sha256_hex_of_bytes(a["event_log_bytes"]),
                sha256_hex_of_bytes(a["notebook_bytes"]),
                sha256_hex_of_bytes(canonical_json_bytes(a["manifest"])))
    checks["hashes_reproducible"] = {
        "description": "full rerun reproduces every artifact hash from exact bytes",
        "pass": all(arm_hashes(arms[c]) == arm_hashes(rerun[c]) for c in ("baseline", "perturbed")),
        "evidence": {c: {"first": arm_hashes(arms[c]), "rerun": arm_hashes(rerun[c])}
                     for c in ("baseline", "perturbed")},
    }

    # 9. PAIRED-STATE REPAIR (Meraki GATE 1 verdict 6452485876): the start-state
    # digest is condition-INDEPENDENT, so paired arms with identical starts
    # hash BYTE-EQUAL; the arm config is receipted separately; per-arm event
    # logs differ; and a deliberately corrupted start state makes the paired
    # equality check FAIL (a shared seed alone is never proof — the check is).
    corrupt = run_arm(
        condition="baseline", schedule=schedule_arm_a, world_seed=world_seed + 1,
        turns=turns, force_plan=fixed, pair_id=pair_id,
        code_commit=code_commit, prompt_versions=prompt_versions,
    )
    b_state = base["manifest"]["actuals"]["actual_state_sha"]
    p_state = pert["manifest"]["actuals"]["actual_state_sha"]
    b_cfg = base["manifest"]["actuals"]["arm_config_sha"]
    p_cfg = pert["manifest"]["actuals"]["arm_config_sha"]
    b_log = base["manifest"]["actuals"]["actual_event_log_sha"]
    p_log = pert["manifest"]["actuals"]["actual_event_log_sha"]
    corrupt_state = corrupt["manifest"]["actuals"]["actual_state_sha"]
    checks["paired_state_repair"] = {
        "description": "start-state digest condition-INDEPENDENT (paired arms byte-equal); arm config receipted separately; per-arm logs differ; corrupted start state DETECTED",
        "pass": (b_state == p_state) and (b_cfg != p_cfg) and (b_log != p_log)
                and (corrupt_state != b_state),
        "evidence": {
            "paired_state_digests_equal": b_state == p_state,
            "paired_state_sha": b_state,
            "arm_config_receipts_differ": b_cfg != p_cfg,
            "baseline_arm_config_sha": b_cfg,
            "perturbed_arm_config_sha": p_cfg,
            "event_logs_differ": b_log != p_log,
            "corrupt_start_state_detected": corrupt_state != b_state,
        },
    }

    report = {
        "fixture": "island-v01 GATE 1 deterministic paired mock fixture (SPEC 6.1)",
        "subject_honesty": "THIS IS NOT THE EXPERIMENTAL SUBJECT; model arms only after acceptance + owner grant",
        "world_seed": world_seed,
        "turns": turns,
        "force_plan": force_plan,
        "pair_id": pair_id,
        "code_commit": code_commit,
        "prompt_versions": prompt_versions,
        "checklist": checks,
        "all_pass": all(c["pass"] for c in checks.values()),
        "manifests": {"baseline": base["manifest"], "perturbed": pert["manifest"]},
        "notes": [
            "Fixture uses a deterministic STUB clock (FIXED_CLOCK_UTC) so hashes reproduce; real runs inject real UTC time.",
            "cost.unknown_charge_attempts=0 is a measured count (zero charge attempts); all unmeasured cost fields stay null.",
            "The code puppet is the loop-fill bare minimum (issue #13); swapping ONLY the puppet fill to model is SPEC 6.2.",
            "bus_jsonl_sha stays null — the fixture emits no bus traffic; honest absence, not a zero.",
            "REPAIR 6452485876: actual_state_sha is condition-independent; arm_config_sha receipts the arm configuration separately.",
            "Naming checks 6452485876: code_commit stays null (reserved for a Git revision); the module-bytes fingerprint is source_bytes_sha256; run_config.fixture_clock marks the deterministic stub clock.",
        ],
    }

    if outdir:
        out = Path(outdir)
        out.mkdir(parents=True, exist_ok=True)
        (out / "events.baseline.jsonl").write_bytes(base["event_log_bytes"])
        (out / "events.perturbed.jsonl").write_bytes(pert["event_log_bytes"])
        (out / "notebook.baseline.txt").write_bytes(base["notebook_bytes"])
        (out / "notebook.perturbed.txt").write_bytes(pert["notebook_bytes"])
        (out / "run-manifest.baseline.json").write_bytes(canonical_json_bytes(base["manifest"]) + b"\n")
        (out / "run-manifest.perturbed.json").write_bytes(canonical_json_bytes(pert["manifest"]) + b"\n")
        slim = {k: v for k, v in report.items() if k != "manifests"}
        (out / "FIXTURE_REPORT.json").write_bytes(canonical_json_bytes(slim) + b"\n")

    return report


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python -m island.v01.fixture")
    ap.add_argument("--outdir", default=None, help="optional directory for artifacts + report")
    ap.add_argument("--seed", type=int, default=DEFAULT_WORLD_SEED)
    ap.add_argument("--turns", type=int, default=DEFAULT_TURNS)
    args = ap.parse_args(argv)
    report = run_fixture(outdir=args.outdir, world_seed=args.seed, turns=args.turns)
    slim = {k: v for k, v in report.items() if k != "manifests"}
    print(json.dumps(slim, indent=2, sort_keys=True))
    return 0 if report["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
