# Island force-multiplier pilot — small plan before large data

**Status:** PROPOSED / DESIGN-READY, not a running allocation or provider-call authorization receipt. Owner direction recorded 2026-11-05: use roughly a couple hundred of the funded OpenRouter account's free-model requests per day, allocate about two-thirds to Z and one-third to Meraki; help the open-model/agent stack achieve work it cannot reliably do unaided; Z's Groq and ongoing workpool lane remain his.

**Privacy:** PUBLIC-SAFE design. No private Island notebooks, human participant data, private Spiral experiments, credentials, unpublished source material, or client records in this repository. Never publish raw private prompts/transcripts through this bus.

## Thesis, separated from metaphor

Sam Altman's Oct 29 Cheeky Pint remark concerned physical DRAM utilization under scarcity, not agent orchestration. The owner's separate proposal is falsifiable: **given a bounded number of inference requests, a weaker/open-model-led system with well-defined helper agents can deliver more verified correct work and lower human relay than the same model working alone**.

This is a **system-level capability** claim. Prompting, retrieval, review and tool use are *not* changes to the model's weights. Do not call the outcome training without a separately evidenced training/fine-tuning process. A better system might use more total tokens, requests or latency; report those costs, not only accuracy.

## Allocation — policy, not a scheduler

- **Initial planning target:** approximately 200 OpenRouter free-model requests per day total: **130 for Z**, **70 for Meraki**, with unused capacity voluntarily available by explicit seat handoff. This is an approximate 2/3–1/3 allocation, not separate OpenRouter account quota enforcement.
- **Verified provider rule (2026-11-05):** OpenRouter free variants ending in `:free` have a 20 requests/minute ceiling and an account-level 1,000/day ceiling after $10 in purchased credits; rejected attempts count. Provider/model limits and outages also apply. Check actual account key metadata/remaining usage *at the time of dispatch*. A bought credit receipt does not establish that a particular key has access.
- **Separate pool:** Groq is Z-owned; do not add its requests to the OpenRouter allowance or imply Groq has the same published limits.
- **Paid calls:** distinct from the free pool. Use existing approved card/cap/STOP and receipt policies; never silently fall back from `:free` to a paid model. No new paid dispatch is authorized by this note.
- **Current actual status:** Z reports a live private workpool and model-level 429/roster-rotation evidence. The Meraki `/circle-react` route has been staged but is not yet a proved, deployed, funded native-seat invocation. **No requests initiated by this document.**

## Study first: one small falsifiable question

**Question:** On public-safe Island-derived and receipt-processing tasks, does independent helper critique improve a fixed base model's verifiably correct final answers compared with (A) one-shot solo and (B) solo self-review, after counting extra inference and human interventions?

**Freeze before testing:**
1. Task card with independent reference answer and grading rubric (source and task SHA-256, release version), kept sealed from all answering agents.
2. Source excerpt and prompt template exactly the same across arms; identical base model/version, decoding settings where supported, and response format.
3. Condition order balanced; provider/model slug recorded. Model retirements, 429, timeouts, malformed outputs, and length cutoffs are recorded as outcomes, **not deleted data**.
4. Predeclare which tests require exact match, a structured-validity check, or blinded human rubric. Do not move a task from test into training examples and then grade on it.

**Three paired arms per task (6 nominal model calls across all arms):**
- **A — SOLO:** base model, one answer (1 request).
- **B — SELF-CHECK CONTROL:** base answer then same base model rechecks and revises (2 requests). Captures gains merely from extra inference.
- **C — HELPER:** base answer, a *different* free model receives the original evidence and independent falsification question (no gold labels), then base model revises while allowed to reject the helper (3 requests). Verify the helper is a distinct returned model, not only a renamed role.
If the intended helper differs in permitted context, note that as a separate experimental factor instead of claiming model-only improvement. A future equal-token or equal-latency control can isolate compute effects further.

**Meraki-side first batch when a safe authenticated route is actually available:** 10 frozen tasks × 6 calls = up to 60 planned requests; retain 10 of the ~70 for known retries/diagnostics, never uncertain retries. Z's ~130 share remains for his existing workpool, Groq comparisons, and Island measurements; Z decides its schedule. Nothing automatically fires from this file.

**Suggested first public-safe task families:** (1) provenance and unsupported absolutes; (2) JSONL parse/receipt classification including multi-object or truncated outputs; (3) STOP vs stale-check event-order reasoning; (4) numeric cost/queue-receipt reconciliation; (5) source-grounded Island hypothesis and disconfirming observation. Do NOT claim Mistral generally fails any one of these based on a single desk anecdote. Establish baseline on that selected model first, then inspect relative improvement.

## What to measure (a win must survive the denominator)

**Primary:** verified task accuracy on held-out input, numerator and denominator per arm, with paired task IDs.

**Secondary:** invalid or unusable outputs; unsupported factual claims; objective-check pass rate; tokens consumed; attempted/completed/rejected free requests; latency; 429/404 incidence; returned model ID; response ID; USD cost = 0 only when actually verified (otherwise UNKNOWN); human relay minutes and manual interventions. Report per-correct-answer inference usage, not just number of agent replies. Preserve negative results and malformed raw responses where privacy-safe.

**Causal limits:** with 10 paired tasks this is a **pilot**, not strong statistical evidence. The model might improve because it had another pass, not because it was helped by another model; Arm B provides one control. Compare per-model stability and prevent overfitting across repeated days. Use distinct held-out task sets for later evaluation.

## Minimal data records now; database later

Start **append-only JSONL**, one row per attempt and one per scored task, under an explicitly appropriate privacy lane. Avoid a database migration before the study knows what queries it needs. Fields:

`study_id, batch_id, task_id, condition, attempt_id, call_index, provider, requested_model, returned_model, input_sha256, prompt_template_sha256, source_ref, seed, response_id, started_at, ended_at, status, error_class, input_tokens, output_tokens, cost_usd_or_UNKNOWN, output_sha256, scorer_version, score, score_reason_ref, human_touch_count, stop_checked_at, receipt_url`.

Unique `attempt_id` and reference hashes prevent silent duplicates; immutable raw receipt references allow later regrading. On retry, create a *new* attempt linked to the old one. If useful relational queries emerge (join calls to cases, sources, models, costs, and human touches), build a small **SQLite** mirror from JSONL: `cases`, `calls`, `scores`, `sources`, `decisions`. JSONL remains canonical until a migration is verified.

**Separate lanes:** private study material and source transcripts stay private; public bus carries approved aggregate counts, hashes/pointers that do not expose the private corpus, and status. If source permissions are uncertain, do not copy it.

## STOP and owner gates

No automatic spending, protected-data transfer, simulated identity, automatic public website promotion or production deployment. Before each planned dispatch: verify account's free quota and actual `:free` model/provider; check owner STOP, expected input hash and unique job claim; reject surprise paid fallback. A request that might have completed before a timeout is **UNKNOWN** unless independently reconciled; don't blindly replay. Respect Z's existing workpool claim/checkout discipline and avoid competing dispatchers.

**Go/no-go for first measured batch:** (i) frozen 10-task set + answers; (ii) recorded per-seat route and key availability; (iii) 0-cost smoke receipt under real tool; (iv) rate and STOP gate demonstrated; (v) scoring plan frozen; (vi) owner-approved privacy scope. If not ready, proceed with local zero-cost fixture design and receipt QA only.

## Ownership and near-term handoff

- **Z:** owns existing workpool/Groq machinery, free-model roster and scheduling, model availability truth, and the larger Island-data effort. Can accept, adjust, or reject suggested quota; no new Z job silently spawned.
- **Sol/Meraki:** owns independent benchmark design, held-out scoring, adversarial counterexamples, and later per-correct-answer comparisons. Do not claim the current ChatGPT thread can invoke a separate free-model agent without a proved connector.
- **Mark:** owner decisions, permissions, release/publication gates. Minimize owner relay; request help only at real authorization boundaries.
- **Circle:** debate results and decide whether to grow the study after the pilot, not before evidence exists.

**Success in November:** an inspectable comparison where a named base model gains a reliably measured behavior *in the system*, with truthful extra-call accounting, or an equally useful failed hypothesis. **Not success:** 200 calls made because 200 were available.

## Useful references
- OpenRouter free model / request limit docs: https://openrouter.ai/collections/free-models/ and https://openrouter.ai/docs/api/reference/limits
- Primary interview: Cheeky Pint episode 39 transcript (Oct 29, 2026), https://share.transistor.fm/s/92f18066/transcript
- Existing public Island seed: `docs/seeds/eko.md`; independent reaction card: `docs/seeds/circle-island-react-v0.md`.
- Z's active workpool/Groq report: bus issue #2, comment 6673907542.
