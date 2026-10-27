# Island v01 — RUNBOOK (STUB v0.1.1)
Status: minimum-viable stub for Meraki's review + the pre-dinner walkthrough. Must be completed against `island/runner.py` before Stage 1. A handoff runner should be able to go start→manifest with only this file.

## 1. Prerequisites
- Repo checked out at the pinned `code_commit`; Python version pinned in CI.
- Loop fill-in choice decided per the spectrum issue (recorded as `actors[].fill`).
- No paid model call without Mark's recorded grant (cost = null-not-zero until verified).

## 2. One bounded run (paper or code)
1. Generate `pair_id`; arm condition (baseline first — no ordering confound undeclared).
2. Start the run; manifest `actuals` auto-written (started_at_utc, status=running).
3. Fixed points fire turn-indexed; baseline logs `bert_opportunity/delivered:false`; escalations logged as events.
4. End: manifest actuals finalized (turns_completed, SHAs, results, stopped_reason); artifacts hashed.

## 3. Verification (runner self-check)
- [ ] `turns_completed` ≤ `turns_requested`; every fixed point logged in BOTH arms.
- [ ] All actuals non-default (nulls honest, zeros measured).
- [ ] SHAs re-computable from artifacts by a third party.
- [ ] `known_subtotal_usd` null unless a verified receipt exists.

## 4. Stop conditions
Completed | error | cap | stop. Any stop = manifest finalized + stopped_reason honest; no run silently abandoned.

## 5. Open items (blockers before sharing)
- MIT/Eko upstream source + version citation (Amendment 4 precondition).
- LICENSE/provenance line for seed material.
- Schema review pass (circle meeting item 3) — this stub rides that pass.
