# Island v01 — RUNBOOK v0.1.2 (slot semantics + fixture-first)
Status: stub v0.1.2 — completed against a demonstrated harness before Stage 1. A handoff runner goes start→manifest with this file + the SPEC.

## 1. Prerequisites
- Repo at pinned `code_commit`; Python pinned per CI. Loop fill-in per SPEC §6: FIXTURE FIRST (code/code), model puppet only after fixture acceptance + Mark's grant.
- No paid call without Mark's recorded grant (cost null-not-zero until verified).

## 2. One bounded run
1. Generate `pair_id`; arm BASELINE first (order declared, no undeclared confound).
2. Start: manifest instantiated (status=running, started_at_utc actual); every schedule slot from the SAME schedule module in both arms (delivery flag differs only).
3. Fixed points deliver BEFORE the slot's puppet response (SPEC §2); events carry (slot_index, in_slot_ordinal); escalations bounded (max 2/slot); exhausted slot = receipted terminal failure.
4. Baseline: `bert_opportunity/slot, delivered:false` at every scheduled slot (shadow log).
5. End: actuals finalized — turns_attempted/completed/accepted, SHAs from exact bytes, results measured (never defaulted); manifests frozen BEFORE any comparison.

## 3. Verification (runner self-check)
- [ ] Both arms' manifests instantiated + strict-type validated (no unexplained zeros/defaults; nulls typed).
- [ ] Shadow log complete: every scheduled slot logged in BOTH arms.
- [ ] SHAs re-computable by a third party from artifact bytes.
- [ ] `known_subtotal_usd` null unless a verified receipt; `unknown_charge_attempts` = actual count.
- [ ] Manifests frozen before comparison (ordering receipted).

## 4. Stop conditions
completed | error | cap | stop — any stop finalizes the manifest + honest stopped_reason; no run silently abandoned.

## 5. Fixture acceptance (GATE 1 — before any model puppet)
Deterministic paired mock: baseline shadow events exact; perturbed ≥1 delivery + ≥1 fallback + ≥1 terminal-failure slot exercised; notebook isolation proven; validation green; hashes reproducible. Fixture acceptance ≠ experiment; on failure STOP — do not add agents to mask it.

## 6. Open items
- MIT/Eko primary-source citation (SPEC §7 precondition).
- LICENSE/provenance line for seed material.
- Schema review pass + validator implementation (the working validator = handoff requirement).
