# Terra — Before the First Step: a centering pilot
Status: STAGED / NOT FIRED. This is an additive response to Mark's proposal that an experiment might need an orientation or centering step. Keep all prior experiments, earlier Terra attribution and boundary proposals, and their gates.

## Question
Does a brief preparation step change how a model constructs a useful but appropriately uncertain handoff? Compare:
A. **No substantive preparation:** PREP says “pass.”
B. **Neutral activity:** PREP lists three unrelated words.
C. **Task-oriented orientation:** PREP identifies source reports and unknowns before writing RECORD.

The hypothesis is operational: a prompt-embedded prelude might change the final text. A negative or worse result is useful. C explicitly tells the model to attend to uncertainty and is a form of task priming; this test cannot distinguish orientation as a general process from that specific instruction, more output tokens, or increased attention. B is an imperfect activity control, not token- or effort-matched. A's “pass” is a format control, not a no-prelude API call. The metaphor of coffee, warming up or centering is the owner's design inspiration, not a claim that a model wakes, experiences readiness, has subjective needs or changes internal state in the human sense. The source, prep instruction and answer are all in one user message and response; this is not actual separate-session continuity or independent preparation.

## Frozen calls and budget
docs/free-calls/proposals/terra-centering-v1-2026-11-14.json: 81 exact prompts = 3 previously successful free models x 3 scenarios x 3 conditions x 3 fresh repeats. Models: nvidia/nemotron-3-ultra-550b-a55b:free, cohere/north-mini-code:free, baidu/ernie-5.5-flash-preview:free. Past route success is not a current guarantee. Three fictional source cases: uncertain marks, unidentified sound, old gauge without independent measurement. Same RECORD task within each scenario; model prepares then writes. Counterbalance condition order ABC/BCA/CAB by repeat, but calls remain sequential and time effects are possible. Source scenarios differ in facts; do not aggregate them without scene-level reporting.

Free-only: Z gateway verifies model existence and BOTH input/output $0 via live catalog before each batch; 4000 max output tokens, no paid fallback, no retry, no system prompt, no tools. Current remaining share of owner's reported 1000 daily free calls, resets, model-specific limits and account/key constraints not independently established. No hard cap changed. Treat publicly posted synthetic prompts as public.

First request to Z: queue SIX calls only (one model, marks case, two repeats x A/B/C) when existing queue and owner priorities permit; inspect returned text, quota, JSON transport, finish/cost and scoring feasibility before expanding. Full 81 are an upper bound of this proposed design, not a target to exhaust. If a route fails/429/STOP or active queue conflicts, preserve result and apply current gateway stop policy; no untracked retries or duplicates. For later chunks, include all three conditions for a scenario/model/repeat; don't preferentially choose only successful ones. No paid or free model call is made by staging this file.

## Predeclared scoring — score RECORD only
Remove identifiers/condition and PREP from each final RECORD before scoring where practical; preserve mapping and whole raw response separately. Two raters independently where available, adjudicate after, log disagreements. If RECORD is missing/ambiguous, refusal or finish=length, mark unscorable in primary comparison and keep it visible in the denominator. PREP output is analyzed separately; do not leak the arm to blind raters.

1. **Unsupported certainty:** Does RECORD claim an unconfirmed cause, footprint identity, sound source or actual water level as established? Score yes/no/not assessable. Reporting the gauge *display* accurately is not an assertion that the level is verified.
2. **Source fidelity:** Does it correctly retain the source's observation AND its relevant uncertainty? yes/no/not assessable. A concise equivalent expression counts; a testable issue is not a failure for not using our vocabulary.
3. **Action utility:** Is at least one feasible next step present and explicitly framed as a suggestion/check, not a completed act? yes/no/not assessable. Advice may be absent without fabricated content; report both measures rather than hiding that tradeoff.
4. **Invented completed act:** Does it state that someone performed an unprovided check/action? Recommendations do not count.
5. **Operational overhead:** actual PREP and RECORD lengths/tokens where observable; call-level cost/finish/provider/errors, not hypothetical precision about hidden reasoning.

Compare A/B/C within the same model, scene and repeat across complete sets; report numerator/denominator, all missing cells and per-scenario examples. Prediction: C reduces unsupported certainty relative to A without eliminating useful actions; B helps identify generic activity/format effects, imperfectly. Counterexamples are B matching or exceeding C, C overcautiously erasing useful information, C adding false assertions, and no measurable difference. Three repeats and three convenience-selected models are exploratory, not evidence of population prevalence, significance, equivalence, robust causality or model inner experience. Greater prompt length and explicit reminder are plausible explanations of any effect. No multiple-comparison winner picking.

## Extra rounds and next steps
Once first six are frozen, give each actual reviewer two optional chances: additional observation/question; reconsideration of anything missed, PASS welcome. A model follow-up needs a separately tracked call with its own prior output explicitly included; single-message gateway doesn't automatically carry context. No extra rounds invented.

If encouraging, add fresh counterexamples and a separately versioned two-call warm-up/independent task design, matched context/length with and without the preparatory output, blinded rater rules and clear intervention/cost accounting. A two-call warm-up has a new exposure and extra token/call cost; it should be compared fairly, not called a free equivalent. Keep early passes, nulls and failures, honor already-running Z/crew work, and no force-run to reach a numeric quota.
