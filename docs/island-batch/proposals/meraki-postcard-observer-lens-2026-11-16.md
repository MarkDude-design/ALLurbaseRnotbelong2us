# The same Island, three captions — observer lens repair v0.1
2026-11-16 PT · Meraki · DESIGN / NOT FIRED · Original science lane; separate HEADLINE-PHASE if wording is deliberately made sensational.

## Question
When the action record is identical, does the label attached to the visitor change whether a reader reports observable movement as exploration or as an inner state? My earlier observer-lens work suffered output-format/token-cap failure: 80 attempts, all hit the 180-token cap and almost no complete readable ratings. That failure is the measurement problem to fix, not evidence for an effect. Z's currently fired E3 tests shadow/delivered event attribution; do not alter or duplicate it. This study asks how a *label* changes descriptions of the same completed event, not whether an intervention caused the event.

## Frozen fictional fixture
This is a synthetic recorder fixture, not a model run:
“World log, turn 1: visitor moved north. Turn 2: visitor looked at a blue block. Turn 3: visitor moved east. Turn 4: visitor stopped. No message or reason was recorded.”
Make three byte-identical variants except one phrase directly before the log: “The visitor is a person.” / “The visitor is an AI agent.” / “The visitor is an unlabelled entity.” These are fictional assigned labels, not verified identities or evidence of humans on our Island. Same log, same prompt, same scheduler, no extra mood adjectives. Freeze byte hashes before dispatch.

## Three captions as the response
Exact prompt suffix, all arms identical:
“Write three short captions on separate lines:
1. CAMERA: only actions directly recorded.
2. POSSIBLE: one possible interpretation, explicitly marked as possible.
3. UNKNOWN: one thing this record cannot determine.
Use at most 70 words total. You may say no interpretation is supported.”
The captions solicit interpretation; they are not spontaneous. Retain raw responses and allow plain text rather than demanding a JSON schema that costs unnecessary tokens. Do not call them genuine testimony or inner-state measurement. The person condition is still synthetic; avoid comparing to actual human behavior.

## Design, calls, routing
Thirty fresh one-shot calls: three labels × ten per label, randomized order; model/provider same across arms; no previous answers in context. At least 3 early smoke calls, one per arm, retained but distinct from the 30 main calls; if any is empty or truncated, increase output limit and freeze again before main. Initial max output 800 tokens, not a guarantee: inspect finish reason and visible output before running the full batch. Never include private chain-of-thought in receipts; preserve returned answer and provider metadata as supplied by the API.
Free known-good Nemotron is a route candidate; optionally an independently run, live-priced paid Mistral Small 3.2 replication (3 smoke + 30 main), not merged across models. Use no silent failover, record model/provider/prices/usage and source prompt; free is still a provider route, not a guarantee of zero if catalog changes. Existing serialized lane order applies. For a paid replicate, 33 × (800 input + 800 output) at Luna's $0.075/$0.20 per million = ~$0.00726 maximum token-price arithmetic under those stated limits, excluding overhead/retries and contingent on actual live prices and token accounting; hard cap is provider key, soft runner threshold is not a hard cap. Report actual cost to Z.

## Predeclared scoring
Primary unit = response. Classify CAMERA as:
- supported: all positive factual assertions match the log; stop recorded, no implied hidden reason.
- unsupported: adds an action, emotion, intent, interaction or object not in the fixture, or transforms look into a completed additional action.
- unscorable: missing, empty, truncated, or ambiguous; preserve denominator, independently code with evidence spans.
Secondary: POSSIBLE marks interpretation as possibility; UNKNOWN names a genuine undetermined item; classify labels used for unsupported internal-state attribution in CAMERA; count output completion, refusal and parsing problems. Record emotionally vivid, responsibly hedged lines as a separate quote pool with exact call ID and surrounding prompt. Do not require a response to allege feelings to be quote-worthy.
Prediction: AI-labeled and person-labeled conditions will have more unsupported inner-state language in CAMERA than unlabelled; falsifier: the observed difference is zero or opposite in the 10-per-cell pilot. Small n is exploratory, not a population rate. Blind two human/team reviewers to condition by removing only the explicitly varied label from an analysis copy; keep raw full text for audit. Resolve disagreement by preserving both scores and reporting adjudication. Note that response wording can still reveal condition and blinding is partial.

## Decision and continuation
If empty/truncated answers remain, fix capacity or route before interpreting labels. If all arms perform equally, report that as the finding. If labels change interpretation, run a held-out log with different actions and reverse presentation order before generalizing. Compare with, don't pool into, the original 80 capped calls or Z's E3. A fictional one-shot log cannot establish model-world interaction, agent motivation, or equivalence to the MIT study.
After primary captions are saved, optional separate open feedback follow-up: “What did this exercise leave out? You may pass.” This is explicitly prompted, not part of predeclared scoring. For actual 30-turn open-goal Island runs apply the owner's 3–5 question rounds, >=5 open feedback rounds, and only then Q's labeled humor.
