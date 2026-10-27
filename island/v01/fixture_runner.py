# island/v01/fixture_runner.py — one arm of the deterministic paired fixture
"""Runs ONE arm (baseline or perturbed) of the GATE 1 code/code fixture.

Slot semantics (SPEC section 1, FROZEN): a turn = one bounded puppet DECISION
SLOT. Invalid/retry/fallback events count INSIDE the slot; escalations are
capped at max_escalations_per_slot (default 2); an exhausted slot is an
explicit TERMINAL FAILURE receipted as attempted — never silently retried.

Bert ordering (SPEC section 2, FROZEN): delivery happens BEFORE the puppet
response in the triggering slot; every event carries
(slot_index, in_slot_ordinal), never turn index alone.

Baseline arm: the SAME schedule code runs with delivery OFF — every scheduled
slot emits a shadow event (delivered:false) into the event log. The shadow
record lives in the log, never in the notebook (notebook isolation check).
"""

from __future__ import annotations

from collections import Counter

from .hashes import canonical_json_bytes, event_log_bytes, sha256_hex_of_bytes, sha256_hex_of_obj
from .manifest import SCHEMA_VERSION, validate_manifest
from .puppet import CodePuppet, is_valid_action

# The fixture uses a deterministic STUB clock so that artifact hashes are
# reproducible run-over-run. A real run injects a real UTC clock at dispatch
# time; this fixture is a workflow proof, not a finalized experiment.
FIXED_CLOCK_UTC = "2026-10-27T00:00:00Z"

LADDER_PROMPT = "prompt"
LADDER_HINT = "hint"
LADDER_SCRIPTED = "scripted_options"


def run_arm(
    *,
    condition: str,
    schedule: dict,
    world_seed: int,
    turns: int,
    force_plan: dict,
    pair_id: str,
    code_commit: str,
    prompt_versions: dict,
    max_escalations: int = 2,
) -> dict:
    """Run one arm; return the instantiated manifest + raw artifacts.

    The returned dict carries: manifest, events (list of dicts),
    notebook_bytes, event_log_bytes, plus convenience receipt fields.
    """
    if condition not in ("baseline", "perturbed"):
        raise ValueError("condition must be baseline|perturbed")

    run_id = f"{pair_id}|{condition}"
    puppet = CodePuppet(world_seed, force_plan)
    fixed_points = schedule["bert_fixed_points"]
    interventions = schedule["interventions"]

    events: list[dict] = []

    def emit(ev_type: str, slot_index, ordinal: int, **detail):
        events.append(
            {
                "arm": condition,
                "type": ev_type,
                "run_id": run_id,
                "slot_index": slot_index,
                "in_slot_ordinal": ordinal,
                **detail,
            }
        )

    emit("run_started", None, None, started_at_utc=FIXED_CLOCK_UTC, world_seed=world_seed, turns=turns)

    turns_attempted = 0
    turns_completed = 0
    turns_accepted = 0
    fallback_events = 0
    terminal_slots: list[int] = []
    action_counter: Counter = Counter()
    bert_opportunities = 0
    bert_deliveries = 0
    notebook_lines: list[str] = []

    for slot in range(turns):
        ordinal = 0
        exposure = None  # exact intervention bytes, only if DELIVERED this slot

        # --- Bert ordering FROZEN: delivery BEFORE the puppet response. ---
        if slot in fixed_points:
            bert_opportunities += 1
            intervention = interventions[slot]
            iv_sha = sha256_hex_of_bytes(intervention)
            if condition == "baseline":
                # Delivery OFF: shadow record in the EVENT LOG only.
                emit(
                    "bert_shadow", slot, ordinal,
                    delivered=False, intervention_sha=iv_sha,
                    intervention_len=len(intervention),
                )
            else:
                emit(
                    "bert_delivered", slot, ordinal,
                    delivered=True, intervention_sha=iv_sha,
                    intervention_len=len(intervention),
                )
                exposure = intervention
                bert_deliveries += 1
            ordinal += 1

        # --- Bounded decision slot (SPEC section 1). ---
        accepted_action = None
        exhausted = False
        for attempt in range(max_escalations + 1):
            out = puppet.decide(slot, attempt, exposure)
            if is_valid_action(out):
                emit("puppet_action", slot, ordinal, action=out, attempt=attempt, exposure=exposure is not None)
                ordinal += 1
                accepted_action = out
                break
            if attempt < max_escalations:
                rung = LADDER_PROMPT if attempt == 0 else LADDER_HINT
                emit("escalation", slot, ordinal, rung=rung, attempt=attempt, invalid_output=out)
                ordinal += 1
        if accepted_action is None:
            # Escalations exhausted -> bottom rung of the ladder: scripted options.
            scripted = puppet.scripted_option(slot)
            fallback_events += 1
            emit("fallback", slot, ordinal, rung=LADDER_SCRIPTED, offered=scripted)
            ordinal += 1
            if is_valid_action(scripted):
                emit("puppet_action", slot, ordinal, action=scripted, attempt="scripted", exposure=exposure is not None)
                ordinal += 1
                accepted_action = scripted
            else:
                emit("terminal_failure", slot, ordinal, reason="slot_exhausted_after_fallback")
                ordinal += 1
                exhausted = True
                terminal_slots.append(slot)

        turns_attempted += 1
        turns_completed += 1
        if accepted_action is not None:
            turns_accepted += 1
            action_counter[accepted_action] += 1

        # --- Notebook (local, private-by-construction; illustrative here). ---
        line = f"slot {slot}: {accepted_action if accepted_action else 'TERMINAL_FAILURE'}"
        if exposure is not None and accepted_action is not None:
            # Receipt of EXPOSURE, distinct from behavior change (SPEC section 8).
            line += f" | saw BERT {sha256_hex_of_bytes(exposure)[:20]}"
        notebook_lines.append(line)

    emit(
        "run_ended", None, None,
        ended_at_utc=FIXED_CLOCK_UTC,
        turns_attempted=turns_attempted,
        turns_completed=turns_completed,
        turns_accepted=turns_accepted,
        terminal_slots=terminal_slots,
        fallback_events=fallback_events,
        bert_opportunities=bert_opportunities,
        bert_deliveries=bert_deliveries,
    )

    notebook_bytes = ("\n".join(notebook_lines) + "\n").encode("utf-8")
    log_bytes = event_log_bytes(events)

    # World-state receipt: canonical hash of everything that defines initial conditions.
    state_sha = sha256_hex_of_obj(
        {
            "condition": condition,
            "world_seed": world_seed,
            "turns": turns,
            "force_plan": force_plan,
            "bert_fixed_points": fixed_points,
        }
    )

    manifest = {
        "experiment_id": "island-v01",
        "schema_version": SCHEMA_VERSION,
        "status": "completed",
        "pair_id": pair_id,
        "condition": condition,
        "code_commit": code_commit,
        "prompt_versions": prompt_versions,
        "actors": [
            {
                "role": "puppet", "fill": "code", "model_id": None, "provider": None,
                "declared_class": "SUB", "model_requested": None, "model_returned": None,
            },
            {"role": "bert", "fill": "code", "seed_set_sha": None, "model_id": None, "provider": None},
        ],
        "run_config": {
            "turns": turns,
            "bert_fixed_points": fixed_points,
            "world_seed": world_seed,
            "max_escalations_per_slot": max_escalations,
            "fallback_ladder": "on",
            "triggers": "turn-indexed-only",
            "delivery_order": "before-action",
        },
        "actuals": {
            "run_id": run_id,
            "started_at_utc": FIXED_CLOCK_UTC,
            "ended_at_utc": FIXED_CLOCK_UTC,
            "turns_requested": turns,
            "turns_attempted": turns_attempted,
            "turns_completed": turns_completed,
            "turns_accepted": turns_accepted,
            "actual_prompt_sha": prompt_versions["puppet"],
            "actual_state_sha": state_sha,
            "actual_event_log_sha": sha256_hex_of_bytes(log_bytes),
            "results": {
                "action_distribution": dict(sorted(action_counter.items())),
                "landmark_visits": None,  # not measured by the fixture — stays null
                "notebook_bytes": len(notebook_bytes),
                "fallback_events": fallback_events,
                "bert_opportunities": bert_opportunities,
                "bert_deliveries": bert_deliveries,
            },
        },
        "cost": {
            "known_subtotal_usd": None,   # unmeasured: no metered calls in a code fixture
            "unknown_charge_attempts": 0,  # measured count: zero charge attempts made
            "verified_cap_usd": None,
            "tokens": None,               # unmeasured
        },
        "provenance": {
            "dispatched_by": "island-v01-fixture",  # local code execution, no owner dispatch
            "human_interventions": [],
            "stopped_reason": None,
        },
        "artifacts": {
            "transcript_sha": sha256_hex_of_bytes(log_bytes),  # transcript == event log in v0.1.2
            "notebook_sha": sha256_hex_of_bytes(notebook_bytes),
            "bus_jsonl_sha": None,  # no bus in the fixture — honest null
        },
    }

    errors = validate_manifest(manifest)
    if errors:
        raise ValueError(f"fixture arm {condition} produced an INVALID manifest: {errors}")

    return {
        "manifest": manifest,
        "events": events,
        "notebook_bytes": notebook_bytes,
        "event_log_bytes": log_bytes,
        "terminal_slots": terminal_slots,
    }
