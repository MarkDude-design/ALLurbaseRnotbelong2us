# Island v01 — SPEC v0.1.2 (slot semantics frozen; walkthrough-compare revision)
Status: DRAFT v0.1.2 for review. Branch z/island-v0.1.1. Merge = Mark's gate. Revision history: v0.1.0 (issue #12 kickoff) → v0.1.1 (four amendments) → v0.1.2 (this — Meraki walk 6448779664 + Z walk 6448660056 compared; her author-graded proposals frozen).
Honest code status: this branch contains SPEC + RUNBOOK ONLY. `island/runner.py` is NOT demonstrated as a v01 harness. First code acceptance = deterministic paired mock fixture (see §6), then a metered model-puppet arm only after Mark's grant.

## 1. Turn ontology — FROZEN (supersedes the informal "every N turns")
A **turn = one bounded puppet DECISION SLOT** (Meraki's alternative; Z's "one puppet action" definition withdrawn — it allowed unbounded invalid-output loops, defect owned).
- Invalid/retry/fallback events are counted INSIDE the slot; bounded retries (max escalations pre-registered; default 2).
- An exhausted slot = explicit TERMINAL FAILURE, receipted as attempted (turns_attempted), never silently retried.
- turns_accepted (valid actions) counted separately from turns_completed (slots exhausted, any outcome).
- Bert events and escalations are events WITHIN a slot, never slots.

## 2. Bert ordering — FROZEN
Delivery occurs **BEFORE** the puppet response in the triggering slot (Meraki's choice, author-graded ACCEPT). Events record **ORDINAL** — (slot_index, in_slot_ordinal) — never turn index alone. "Same fixed point" now means same intervention byte-for-byte across arms/runners.

## 3. Template vs instantiated manifest (Meraki's snag 3, adopted)
The schema below is a TEMPLATE: placeholders are explicit `null`, never measured-looking defaults.
- `verified_cap_usd: null` unless a verified provider limit exists (with authorizing-cap provenance).
- `tokens: null`, `notebook_bytes: null` until measured; artifact SHAs `null` until computed; `dispatched_by` instantiated at dispatch only.
- An INSTANTIATED manifest must pass strict-type validation: nulls typed, unexplained zeros/empty-strings rejected, every non-null value traceable to a receipt.
- Paper-only manifests must carry `"status": "paper-illustration"` and can NEVER masquerade as finalized runs.

## 4. run-manifest.json v0.1.2 (template)
```json
{ "experiment_id": "island-v01", "schema_version": "0.1.2", "status": "paper-illustration|running|completed|error|cap|stopped",
  "pair_id": "<uuid>", "condition": "baseline|perturbed",
  "code_commit": "<sha>", "prompt_versions": {"puppet": "<sha>", "bert_seed": "<sha>"},
  "actors": [
    {"role": "puppet", "fill": "model|code", "model_id": null, "provider": null, "declared_class": "SUB|EXPERT", "model_requested": null, "model_returned": null},
    {"role": "bert", "fill": "model|code", "seed_set_sha": null, "model_id": null, "provider": null}],
  "run_config": {"turns": 8, "bert_fixed_points": "<slot-index list|none>", "world_seed": "<int>", "max_escalations_per_slot": 2, "fallback_ladder": "on|off", "triggers": "turn-indexed-only", "delivery_order": "before-action"},
  "actuals": {"run_id": null, "started_at_utc": null, "ended_at_utc": null,
    "turns_requested": 8, "turns_attempted": null, "turns_completed": null, "turns_accepted": null,
    "actual_prompt_sha": null, "actual_state_sha": null, "actual_event_log_sha": null,
    "results": {"action_distribution": null, "landmark_visits": null, "notebook_bytes": null,
      "fallback_events": null, "bert_opportunities": null, "bert_deliveries": null}},
  "cost": {"known_subtotal_usd": null, "unknown_charge_attempts": 0, "verified_cap_usd": null, "tokens": null},
  "provenance": {"dispatched_by": null, "human_interventions": [], "stopped_reason": null},
  "artifacts": {"transcript_sha": null, "notebook_sha": null, "bus_jsonl_sha": null} }
```
`unknown_charge_attempts` starts 0 as a COUNT (measured: zero attempts so far) — that is a measurement, not a default; every other placeholder is null until receipted.

## 5. Walkthrough-consolidated semantics (both walks agree)
Schedule generation SEPARABLE from Bert delivery (baseline arm runs the same schedule code with delivery off — the shadow log requires it). Paired = equal INITIAL CONDITIONS (world config), never identical stochastic trajectories — said plainly to prevent the identical-twins misread. Manifests frozen (hashed + finalized) BEFORE any between-arm comparison. Notebooks local, private-by-construction; walkthrough notebooks are illustrative only.

## 6. Acceptance path (fixture-first; her #13 disposition folded)
1. **Deterministic paired mock fixture** (code puppet + code Bert): paired scheduler proven, shadow events correctly recorded (baseline `delivered:false` at every scheduled slot; perturbed `delivered:true` + ≥1 fallback event exercised), failure paths exercised (one terminal-failure slot), notebook isolation, manifest validation green, reproducible hashes from exact bytes. THIS IS NOT THE EXPERIMENTAL SUBJECT.
2. Only after fixture acceptance + Mark's explicit provider/price/cap/dispatch grant: change ONLY puppet fill to `model` for the first real condition pair. `actors.fill`, exact model requested/returned, changed prompt bytes recorded so outsiders see exactly which conditions differ.
3. Model stochasticity risk (her #13): pair on initial state; effect metric + sample/stopping design PREREGISTERED before causal claims.
4. Null ≠ escalation: a null or dramatic contrast is a valid bounded observation; moving to model-Bert changes the TREATMENT = new versioned comparison, never goalpost-moving on the same one.

## 7. MIT/Eko citation — PENDING (honest stub)
No verified primary-source citation for the upstream (MIT/Eko-lineage) experiment exists in this repo yet. `docs/EKO_RUN.md` is an internal topic-seed note, NOT a primary source. **Required before any upstream replication claim:** primary source (paper/report/official writeup) + version + link recorded here. Until then, all "first-of-kind / replication" language stays at the claim-ladder stage (Stage 0 = experiment-to-set-up-an-experiment, said plainly).

## 8. Limitations (consolidated from both walks — the fellow-scientist list)
Paper exercise tests workflow legibility, not causal validity; identical seeds do not control stochastic model trajectories; code-Bert tests one controlled perturbation, not naturalistic model interaction (Bert-model comparison = a different study); notebook content could be private (Amendment 4 — aggregates only); unknown metering stays unknown; single-model-family replication does not establish independent support; a handoff runner needs a working VALIDATOR, not just a schema example; the recorder must distinguish EXPOSURE from BEHAVIOR CHANGE or any different text gets called a result.
