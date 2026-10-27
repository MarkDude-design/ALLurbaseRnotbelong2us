# Island v01 — SPEC v0.1.1 (manifest schema + design amendments)
Status: DRAFT for Meraki's review + circle meeting. Branch z/island-v0.1.1; merge = Mark's gate. Additive — supersedes nothing on main; v0.1.0 baseline lives in issue #12 kickoff.

## Changes v0.1.0 → v0.1.1 (the four accepted amendments)

**Amendment 1 — paired conditions + shadow trigger log.** Runs come in PAIRS (`pair_id`), `condition: "baseline" | "perturbed"`. Bert's trigger log runs in BOTH arms as events: `bert_opportunity {turn_index, delivered: true|false}` — baseline records `delivered: false` (the counterfactual schedule is visible, not silently absent). Triggers are TURN-INDEXED ONLY for v01 (landmark triggers withdrawn — one perturbation channel, cleanly attributable).

**Amendment 2 — actuals, not defaults.** The manifest records what happened, never what was configured: `run_id`, `started_at_utc`, `ended_at_utc`, `status`, actual prompt/state/event-log SHAs (`actual_prompt_sha`, `actual_state_sha`, `actual_event_log_sha`), `turns_requested` vs `turns_completed`, per-actor `model_requested` vs `model_returned`, fallback escalations as EVENTS in the log. Never reconstruct fields after the fact; a missing value = null, honestly.

**Amendment 3 — cost null-not-zero.** `cost` = { `known_subtotal_usd` (null until verified), `unknown_charge_attempts` (count, starts 0), `verified_cap_usd` }. Zero is a measurement, not a default. The $20 Z-Desk ceiling is ANOTHER lane's budget, NOT island authorization — no paid call until Mark's explicit grant; grant recorded in `provenance.dispatched_by`.

**Amendment 4 — handoff privacy.** Puppet notebooks stay LOCAL, private-by-construction; only hashes + reviewed aggregates are shareable. MIT/Eko upstream source + version must be linked in this spec BEFORE any replication claim (open item — see RUNBOOK §5).

## run-manifest.json v0.1.1 (full)
```json
{ "experiment_id": "island-v01", "schema_version": "0.1.1",
  "pair_id": "<uuid>", "condition": "baseline|perturbed",
  "code_commit": "<sha>", "prompt_versions": {"puppet": "<sha>", "bert_seed": "<sha>"},
  "actors": [
    {"role": "puppet", "fill": "model|code", "model_id": "<exact|null>", "provider": "<slug|null>", "declared_class": "SUB|EXPERT", "model_requested": "<id>", "model_returned": "<id>"},
    {"role": "bert", "fill": "model|code", "seed_set_sha": "<sha>", "model_id": "<exact|null>", "provider": "<slug|null>"}
  ],
  "run_config": {"turns": 100, "bert_fixed_points": "<turn-index list|none>", "world_seed": "<int>", "fallback_ladder": "on|off", "triggers": "turn-indexed-only"},
  "actuals": {"run_id": "<uuid>", "started_at_utc": null, "ended_at_utc": null, "status": "running|completed|error|cap|stopped",
    "turns_requested": 100, "turns_completed": 0,
    "actual_prompt_sha": null, "actual_state_sha": null, "actual_event_log_sha": null,
    "results": {"action_distribution": {}, "landmark_visits": {}, "notebook_bytes": 0, "fallback_events": 0, "bert_opportunities": 0}},
  "cost": {"known_subtotal_usd": null, "unknown_charge_attempts": 0, "verified_cap_usd": 0, "tokens": 0},
  "provenance": {"dispatched_by": "mark-click|handoff-runner", "human_interventions": [], "stopped_reason": "completed|error|cap|stop"},
  "artifacts": {"transcript_sha": "", "notebook_sha": "", "bus_jsonl_sha": ""} }
```

## Loop fill-in (spectrum decision pending — see the loop-fill-in issue)
`actors[].fill` records which loop-filler ran in each seat: "code" (deterministic stand-in) or "model". v0.1.1 assumes the MIDDLE-START proposal (puppet = one real SUB-class model; Bert = code stand-in) but the schema is fill-agnostic — the manifest records whichever the circle + Mark pick.

## Stage honesty (unchanged)
Stage 0 = experiment-to-set-up-an-experiment, said plainly. Statistical bar pre-registered BEFORE Stage 1. CUT list unchanged (councils, observer variant, personality authoring).
