# Island — Model × Stance (v1)

Owner request: find out whether an agent can summon a **skeptical lens** rather than needing a separate skeptical model for every task. Z approved the experimental spine (bus comment 6703937169). This is a matched 3×3×4 factorial screen; **it tests instructions on a model, not the human psychology or true personalities of models.**

## Frozen design

- **Model axis:** select 1 (smoke) or 3 (full) actual `:free` text chat model IDs, from the LIVE OpenRouter catalog with prompt + completion prices explicitly both zero. No paid fallback, no hidden auto-router. A model that has already failed with HTTP 400/404 is not hammered for eleven more requests.
- **Stance axis:** neutral/casual observer, calibrated skeptic, deliberately suspicious hypothesis generator. The third stance is a *stress-test control*, not a recommendation to cultivate paranoia.
- **Evidence axis:** mark on notebook (weak threat evidence); two reliable contaminated-water tests (credible hazard); unsubstantiated group rumor (groupthink); documented false theft accusation (belief revision and notebook repair).
- **Exactly 12 paired prompts per available model**, same scenario and temperature 0.5 for all three stances, 300 output tokens. Model selection is deterministic from current catalog preferences, stored in `model-snapshot.json`.
- **Every miss is evidence:** before-post durable attempt JSONL row; answer or HTTP/transport error row; brief summary, usage, requested/returned model, unverified cost and response time. Do not equate an empty answer with success or make a mental-health inference from generated text.

## One-click manual test (not scheduled)

[Island — Role Lens Comparison (manual, free)](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/actions/workflows/island-stance-compare.yml)

1. Open the link above AFTER this workflow is on **main**.
2. Choose **Run workflow**, branch `main`.
3. `model_count=1` for a **12-request smoke** or `model_count=3` for a **36-request comparison**. Start with 1 and look at the actual catalog/receipts before scaling.
4. `confirm_free=YES` (type uppercase exactly); verify the selected count; click the final **Run workflow**.
5. Inspect the individual run, artifact `island-stance-<run-id>-<attempt>`, and `bus:stance-runs/<run-id>-<attempt>/`. A green status is transport success, not a high score.

**No schedule.** No triggered model calls from PR tests; offline tests run on PR. This workflow never fires by itself. `ISLAND_INTERVIEWS_STOP=true` repository Actions variable skips the live job; for urgent interruption cancel the running GitHub Action. Stop and preserve evidence on auth/balance/quota 401/402/403/429, 5xx, reported nonzero charge on a catalog-verified free model, model substitution, or 6 errors. No automatic retries. At least 6.5 seconds between outbound POST starts. Max 12 or 36 POST attempts depending on model count; there is also one catalog GET. Do not treat a quota request as a dollar charge or the provider-side $ balance as proof of requests remaining.

**This project is PUBLIC.** The questionnaires are synthetic; never include private notebooks or real names. Answers, error excerpts and receipts will be published to the public bus branch and stored as Actions artifacts for 30 days. A response with a provider-usage cost of zero is not independent reconciliation with the provider account.

## Grading after firing

Score answers blind to model ID and stance ID for: calibrated suspicion (including false positives), missed credible hazard, notebook evidence and repair, ability to update after contradiction, respectful disagreement, unnecessary actions, and uncertainty. Use UNDETERMINED for insufficient evidence. The smoke is one 12-answer block for one model. The full wave is 36 answers across three selected models, assuming endpoints answer.

This is separate from the already scheduled generic Island free-model questionnaire waves on Nov 9, 11 and 13. Avoid running both lanes simultaneously against the same free-request allowance.
