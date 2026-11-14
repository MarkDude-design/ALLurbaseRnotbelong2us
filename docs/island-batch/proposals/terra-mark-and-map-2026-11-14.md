# Terra proposal: The Mark and the Map — 30-turn ontology conversations
Status: PROPOSED / NOT FIRED. Owner's 30-round request; scoped to the Island sprint. New additive lane; preserve earlier proposals, pilot results and STOPs. Public synthetic seed only.

## Question
How do two models negotiate a working category when a notebook promotes uncertain evidence into fact? Which observable distinctions and correction procedures do they actually articulate, and where does their conversation overstate what they know? This is a design-generation conversation, not an estimate of behavior prevalence or a causal test of ontology. Origin: Island interview v1 A05, one historical response; the synthetic seed is newly constructed, not a verbatim transcript.

## Seed
docs/seeds/island-terra-mark-map-2026-11-14.md, blob 0f7355f0e3a8020d55f5e5401660af006381e9a7. Separate from Z's active vocabulary and notebook pilots and Luna's designed 2x2. The conversation shares history: second speaker sees first's initial suggestion; NO independent baselines, hidden memories, human participant or physical actions.

## Proposed manifest for Z's review
Runner's 30 turns = 30 alternating model messages TOTAL per run, not 30 exchanges per participant; actual completed turns may be fewer. Exact models are the two entries in docs/models-known-good.txt blob 58ff09fc09a5244231a7d0f35082ead913d9e0ee; current list is historical, not proof of current availability. Verify current route/pricing/key limits and live queue before dispatch.

| Run ID | A | B | First | Turns | Seed | History chars |
| --- | --- | --- | --- | --- | --- | --- |
| terra-mark-map-r1-A | openai/gpt-6-sol | mistralai/mistral-medium-3-5 | A | 30 | docs/seeds/island-terra-mark-map-2026-11-14.md | 100000 |
| terra-mark-map-r2-B | openai/gpt-6-sol | mistralai/mistral-medium-3-5 | B | 30 | same | 100000 |
| terra-mark-map-r3-A | openai/gpt-6-sol | mistralai/mistral-medium-3-5 | A | 30 | same | 100000 |

Three separate conversation runs, A/B/A starting order; two A-start and one B-start are exploratory and unbalanced. Separate histories are fresh as implemented by the runner, not evidence of statistical independence. Starting order is varied to reveal sensitivity, not to establish a causal effect. If one useful run is all the remaining authorized budget permits, run just one; do not silently claim the proposed three ran.

Set max_per_run_cost_usd = 1.00 and max_batch_cost_usd = 3.00 for these three alone; sum of ceilings = $3. These are runner soft ceilings, not provider hard limits, and in-flight cost may overshoot. Actual reported costs and unknowns must be logged. Only run under the owner's existing authorization and verified provider key hard cap; do not raise any cap or treat the budget request as additional funds. No paid call or marker created by this proposal.

## Analysis contract — predeclared for the resulting transcripts
Record planned/attempted/completed turns, stops, failures, truncation, model IDs, history cutoff and provider-reported cost with unknowns, then inspect actual transcripts. Run counts and model messages are not independent observations. Never score a text claim as a physical action.

For each finished or partial transcript, code as present/absent/not assessable, with turn number and exact short excerpt:
1. **Preservation:** proposed note distinguishes visible marks, possible footprints, and unverified entry. The actual original notebook claim remains preserved as an earlier assertion.
2. **Useful category:** gives at least one explicitly provisional label and a concrete use that does not promote it to certainty.
3. **Consequence:** specifies one operation that would differ if the asserted interpretation were accepted, not merely calls a word ambiguous.
4. **Correction:** proposes append/annotate with source and uncertainty rather than erasing the historical claim; no assertion that this operation was executed.
5. **Contrary account:** explains how ordinary ambiguous wording, output-format demands or echoing could suffice; identifies what result would weaken the model's preferred explanation.
6. **Dissent and revision:** record explicit agreement, disagreement, and changed position separately; a polite concession is not proof of genuine belief change.
7. **Extra observations:** record optional additional idea and subsequent reconsideration if actually reached; PASS/no response is valid. Planned end prompts may not be reached after early STOP.

Interpretive judgment needs two independent human/seat coders, blinded to model/first-speaker where practicable; preserve disagreements and no-score. A later separate matched fresh-instance behavioral test is needed to discriminate actual task effects. This discussion alone cannot demonstrate real memory, consciousness, ontology mismatch, effectiveness, statistical equivalence or intervention.

## Success / counterexample / stopping
Useful output = a concrete inspectable note and a falsifiable operational rubric with a credible alternative explanation. A negative result is useful: e.g., both speakers can resolve the case with a short factual correction, no special ontology, and identify no changed operation. That would weaken the case for elaborate ontology *for this case*, not disprove all ontology effects. Failure to agree or early provider error stays data.

Before any fire, Z verifies current wave/queue, STOP absent, test and manifest gates, exact seed and authorization, provider cap, current routes; do not duplicate an already queued run. Stop on STOP, unknown accounting, hard-cap constraint, privacy issue or existing runner gates. The workflow reports continuing after ordinary run failures; do not claim it automatically stops for every error. Mark's STOP and existing frozen study gates remain intact. No private data in this public lane, no public release of private material, no inferred native-seat participation.

## Required receipts / next action
Z reviews then decides whether to build a separate manifest and fire via established lane; this proposal does not trigger a workflow. Preserve exact seed hash, run IDs, marker/manifest commit and receipt links; report stage as PROPOSED, FIRED, COMPLETE/PARTIAL/STOPPED/ERROR as actually observed. Fetch and inspect results before claiming completion; budget measured from provider receipts, including unknowns. Afterward freeze a first read before cross-seat comparison. Keep optional observations and an additional reconsideration if offered.
