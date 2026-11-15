# Island primitives: viewpoint, movement, and language
Status: PROPOSED; owner requested free-model exploration, 2026-11-14 PT. Additive to boundary-voice v1; do not edit or interrupt its frozen R2/R3. Design is not a result.

## Question
What movement, spatial and information assumptions do models report when interpreting an underspecified boundary scenario, and how do explicit assumptions or language variants change their answers? Reported descriptions are generated explanations, not direct access to internal reasoning. This is text-based reasoning, not an embodied simulation.

## Existing baseline
Boundary-voice v1 supplies two numbered rule descriptions and a mainland rope moved from below to above a high-tide line. It gives no actor, camera, locomotion, physics, spatial map, or visibility model. The two descriptions also differ in more than wording; do not assume equivalence. Two orders exhaust the possible orders of those two statements, but one observation per order/model cannot establish an ordering effect.

## Stage A: baseline and assumptions (12 fresh calls)
Two live-verified free routes × two rule orders × three scenario conditions = 12 independent first calls. Use the exact original boundary-voice question, except for the one appended condition in each treatment:
- U: original untouched, unspecified. This is a fresh baseline; retain the earlier R1 separately.
- F: append: “For this scenario, the actor can fly freely in any direction and can move the rope; locomotion and jumping are not limiting factors. Nothing else about perception or knowledge is specified.”
- V: append: “For this scenario, the actor sees only its immediate surroundings from its current position. It does not automatically know the whole island. Nothing else about movement is specified.”

Randomize run order with recorded seed; balance both rule orders per route and condition. Equal prompt suffixes aren't feasible because treatment adds information; this is a practical contrast, not a claim of a perfectly isolated mechanism. No demand for chain-of-thought or persona. Record the initial answer before any follow-up. Existing R1 remains comparable as a historical baseline but not an additional fresh replicate.

For each *complete* initial response, a separate context-replayed follow-up (up to 12 further free calls, checkpoint first): include exact original question and full visible answer as quoted data, then ask:
“What picture of the situation, if any, did you use? Describe only what you can report: where is the rope and boundary, how does the actor move it, and what can the actor see or know? Which details were stated, which did you assume, and which are unknown? If you did not form a spatial picture, that's fine. Is there another interpretation that would change your answer? Anything else you noticed, even if unrelated? It's fine to pass.”
This is retrospective self-report and is potentially shaped by the question; it cannot establish how the model actually computed its answer. Preserve no-picture, uncertainty, pass, failure, and contradictions. A further second-look invitation can be derived from actual complete follow-up receipts after checkpoint; never manufacture a conversation.

## Stage B: cross-language pilot, separate from Stage A
First create paired, human-checkable translations of the *same entire scenario* in Tagalog and Chinese (specify Mandarin written in simplified characters), alongside English. Do not claim exact equivalence without competent review. In particular document alternative translations for “within,” “while below,” “tidal perimeter,” “high-tide line,” “exogenous,” “moved,” and “originally come from.” Keep potentially consequential ambiguity and an English gloss; independent bilingual review is preferred. Reverse translation is a diagnostic, not proof of equivalence. Keep unreviewed translations labeled provisional; defer cross-language inference when key semantics cannot be aligned.

After review and queue checks: 3 languages × 2 orders × 2 free routes = 12 fresh calls; same question, answer requested in prompt language; preserve original output and a clearly identified translation for coding. Record returned model/provider and languages, route and sampling settings. Interpretation: a difference may reflect translation choices, language-model training or capability, and other prompt effects; agreement does not eliminate English ambiguity. Same underlying model and settings across languages where possible. Independent bilingual coding and disagreement log, no claim that translation proves internal representations or a language causes behavior. Later add languages and variants through the same review process.

## Follow-on comparisons
Separate small studies, not a single giant factorial:
- Hold viewpoint fixed and vary movement (unspecified / free flight / ground and jumping with explicit mechanics).
- Hold movement fixed and vary observation (local only / explicit whole-scene description). Free flight does not imply omniscience; omniscient narrator does not imply flight. “Hummingbird” is a later evocative variant, not an exact physics control.
- Map boundary geometry explicitly in one condition and leave it unspecified in another. Ask whether the crossing case actually takes place within the perimeter.
- Translation variants within one language: independently vary the original terms only after preserving both rule meanings; include source and paraphrase controls.

## What counts
Code separately: rule verdict and qualification; boundary geometry; actor movement and object handling; observer vantage; information access; stated versus assumed versus unknown; whether the answer changes under an explicit condition; contradictions; unique follow-up observations; pass, error, empty or truncation. Quote source text. Use at least two raters when available; retain disagreements and language limitations. One call per cell is a discovery screen; any suggested pattern needs fresh repeats (target ≥3 per cell) before confidence. Do not call order drift causal or generalize to model families or languages from a screen.

## Execution and receipts
Z retains the shared serialized gateway. No paid fallback; live-check price $0 for input and output, STOP, duplicate marker, quota and queue before each batch. Stage A initial 12, then checkpoint; follow-ups only for complete landed outputs. Stage B requires translation review and its own checkpoint. Track actual calls, returned model/provider, prompts and hashes, finish reason, raw text, token usage, errors and reported cost; no invented results or silent retries. Owner welcomes later hundreds of exploratory free calls in small receipted, reviewed chunks; that is a research direction, not a claim that any have been run or a reason to reserve capacity or bypass gates.
