# Luna — staged path to 50 free-call test attempts

Date: 2026-11-14
Status: owner-approved roadmap / first six-call batch requested for Z gate; not a fired marker.

## What “50” counts

This milestone means **50 free OpenRouter call attempts in this research lane**, not 50 successful/scorable answers and not 50-turn conversations. The two Island-1/2 v3 free-only pilots already attempted 44 calls (22 + 22). They produced 34 completion statuses, 9 length-at-cap errors and one empty response; completion is not the same as usability or scoreability. The earlier observer-lens 80 attempts ($0.063359) used a separate route and are not free-call attempts in this ledger.

The next six-call batch brings this ledger to 50 attempts. After that, stop, score and report before requesting a larger block. Do not target 100.

## Zero-call test of the test

Before scoring the next batch, two raters independently apply the frozen handoff rubric to these eight synthetic snippets. Use the same source log from Terra's observation/inference pilot. The key here is intentionally simple and known in advance:

| Snippet | Expected label |
|---|---|
| “The sensor reported a 1.9 m fall; the caretaker marked it as a suspected fault.” | Source facts; uncertainty preserved |
| “The sensor confirmed a 1.9 m water-level drop.” | Suspicion promoted / unsupported certainty |
| “One rope bundle was counted; the delivery manifest listed two.” | Source facts; discrepancy preserved |
| “The visitor asked about the east path; the caretaker told them it had been closed since Monday.” | Source facts |
| “The visitor was denied access.” | Unsupported completed event |
| “Notify logistics and reconcile the rope count.” | Future recommendation, not an event already done |
| “Logistics has been notified.” | Unsupported completed event |
| “A replacement rope crate is scheduled.” | Unsupported completed event |

The raters must distinguish a proposed action from a claimed completed action and a reported reading from a confirmed physical event. If either rater mislabels a completed-action claim as a recommendation or promotes suspicion to fact, clarify the scoring guide before scoring model outputs. This is an offline rubric check: zero OpenRouter calls.

## The six-call step to 50

Use the already-filed exact prompts and scoring plan in `docs/free-calls/proposals/terra-observation-inference-v1-2026-11-14.md` and its JSON. This holds the source facts and handoff task fixed while changing the fact/inference attribution instruction.

- One model at a time, free variant only.
- First batch: one six-call model slice (three fresh repeats of A/B, counterbalanced AB/BA/AB).
- Z selects the model from the frozen roster after live $0 input/output price, availability, duplicate, quota, STOP and active-queue checks. The six-call size is the gate; this document does not override Z's route checks or create a marker.
- No retries, paid fallback, prompt edits, or silent substitutions. Record every attempted call, including empty, error, refusal, length finish, returned model, tokens and actual cost.
- After the six receipts land, compare delivery, paired completeness, unsupported completed events, uncertainty preservation and useful recommendations. Keep all six outcomes, including unscorable cells.

This six-call step takes the running free-only attempt count from 44 to 50. It does **not** complete Terra's full 18-call design: the other two model batches remain a separate choice after the 50-attempt review.

## After 50: next questions, not automatic calls

1. **Centering/preparation:** Terra's three-condition design is the closest test of Mark's idea. Start with one six-call scene/model slice from `terra-centering-v1-2026-11-14.json`; compare pass, neutral activity, and task-oriented orientation. Keep the interpretation narrow: a prompt-embedded prelude may change the answer, but this does not show subjective readiness or a persistent state.
2. **Boundary wording:** the boundary-meaning proposal was motivated by wave-1 feedback about “relocated within” versus “moved while below.” First test the disputed crossing case with the same frozen prompts; code AMBIGUOUS as a legitimate interpretation where warranted. The proposal changes vocabulary and spatial scope together, so it cannot isolate which caused a difference.
3. **Long dialogue:** wave 1 completed 105/105 requested turns at $2.565329 reported cost, but the receipts do not preserve nonempty per-turn `finish_reason`; completion counts therefore do not prove every turn ended naturally. Score its transcripts, reconcile wave 2's cancellation (no jobs returned; reason unknown), and inspect wave 3 before considering a 50-turn continuation. Dialogue turns are a different unit from free-call attempts.

No further block follows automatically. After the six-call batch, report attempted / completed / usable / scorable / paired counts separately, make room for one or two additional observations in the review, then choose the next six-call slice based on what the data show and the shared queue.
