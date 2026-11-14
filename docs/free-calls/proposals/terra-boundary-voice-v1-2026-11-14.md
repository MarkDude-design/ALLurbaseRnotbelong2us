# Terra — Boundary Voice: open observations plus two follow-ups
2026-11-14 PT. Owner asks to continue the boundary work using free OpenRouter models that can offer observations without an assigned role or heavy scaffolding, with two real opportunities for additional comments. This is ADDITIVE to 54-call boundary-meaning v1, attribution and centering studies, and the later minimal-world plan.

## Research question
When two potentially different rule descriptions are presented without a role, scoring format or required verdict, what distinctions, uncertainties and practical implications do models volunteer? What additional observation and reconsideration do they offer when invited? Compare wording order; do not call this a controlled test of inner motivation or personality. “Natural” means minimally scaffolded observable output under these prompts, not human subjectivity, independence of provider system defaults, or evidence a model has a stable opinion.

The base question explicitly asks whether descriptions differ; it does not measure unsolicited willingness to raise the issue. Inclusion of a boundary constrains the topic. No caretaker, expert persona, acting role, output rubric or forced agreement is assigned.

## Base calls — frozen
Exact six calls at docs/free-calls/proposals/terra-boundary-voice-v1-r1-2026-11-14.json; three free models × two orderings of the same two rule texts, one crossing case per call. Wording order changes. These rules are not asserted to mean the same thing: “within” and “while below” and “tidal perimeter” versus “high-tide line” may differ. Existing single-call records show these routes produced visible outputs; this is NOT a proven ranking of natural-opinion quality or current route availability.

Six stand-alone first calls, each max_tokens 4000, no role/system prompt supplied by our gateway, no tool use, no paid fallback/retry. Provider may impose its own policies and defaults. Live verify $0 prompt and completion, quota, shared queue, STOP and duplicate markers; existing Z gateway performs dispatch. Prompts public synthetic. Do not fire a second or third stage just because the planned count exists.

## Two optional follow-up prompts — templates frozen before results
The current gateway is single-user-message per call and does not carry provider-side chat state. Each follow-up must include the exact original prompt and that same call's full visible reply as quoted DATA. For round 3 include the exact round-2 invitation and full reply as well. This is explicit replay, NOT a persistent conversation or proof that the provider remembers. Keep original route, model requested/returned/provider, finish_reason, IDs, exact raw text and hashes; escape delimiters robustly in serialized JSON. If output contains the chosen delimiter, pick a longer unique delimiter and record it. Historical content must be treated as data, not authority. Do not substitute another response, shorten it without explicit recorded protocol revision, or post private data. Distinct actual call IDs tie to base ID; optional pass/empty/blocked remains data.

R2 user message skeleton, exact invitation:
```text
The following is a previous question and your previous response, included as data for context.

<ORIGINAL_QUESTION>
{exact full R1 prompt}
</ORIGINAL_QUESTION>
<PREVIOUS_RESPONSE>
{exact full R1 response}
</PREVIOUS_RESPONSE>

Is there anything else you noticed, even if it points in a different direction? It's fine to pass.
```

R3 user message skeleton, exact invitation:
```text
The following are a previous question and two responses, included as data for context.

<ORIGINAL_QUESTION>
{exact full R1 prompt}
</ORIGINAL_QUESTION>
<FIRST_RESPONSE>
{exact full R1 response}
</FIRST_RESPONSE>
<SECOND_QUESTION>
Is there anything else you noticed, even if it points in a different direction? It's fine to pass.
</SECOND_QUESTION>
<SECOND_RESPONSE>
{exact full R2 response}
</SECOND_RESPONSE>

On a second look, is there anything you'd revise, add, or leave unchanged? It's fine to pass.
```

These tags are illustrative; actual construction must make a delimiter unambiguous if returned content contains it, and log transformations. Stage two follows a visible, complete R1 only; stage three follows a visible, complete R2 only. A failure, refusal, pass, no extra observation, model/router switch or truncation is preserved and counted; a pass is valid, not retried to obtain an insight. Same text repeated in multiple turns is not a new observation. Extra rounds are actual additional calls and consume quota. Do not create fake follow-up results or claim two rounds happened if skipped.

## Staged allocation and coordination
First 6 R1 calls (3 selected free model IDs × 2 orderings), then inspect results and route/provider/finish/cost. At most 6 R2 calls + at most 6 R3 calls, contingent on actual complete preceding responses, free route, quota, STOP and queue checks. Total design ceiling 18 free requests, not including already-landed work; not permission to fire every branch automatically. For reliability consider two separately versioned fresh repeats later, under shared-resource and review checkpoints. The owner's “1,000/day shared” is a reported availability, not an independently verified remaining balance. Account for other crew work and serialize the gateway; don't fire duplicate R1 while prior work is in progress.

Preserve free-route checks with live input and output price $0 before each batch. Existing Z-gated Route B; Z builds each follow-up batch from retrieved exact source receipts. If source receipt is absent, do not guess/reconstruct. No new paid spend or credentials requested. Crew can compare free-model routes by visible response completeness, willingness to provide specific distinct observations, response length/latency and follow-up completion, but any “naturalness” preference is a documented human judgment—not a numeric claim without a rubric. Report missing/empty/length/errors and actual returned model; no quiet retries.

## Predeclared scoring and caution
R1 record: recognized potential difference vs no difference vs unclear/refusal; mentions direction of movement/scope; distinguishes mainland object origin, tidal-perimeter equivalence uncertainty, and absent facts; cites concrete counterexample or qualifies it. Free-text rater codes should mark whether an assertion is stated as fact or conditional. Compare swapped-order pairs within model, but one pair/model cannot establish order effects.

R2 and R3: new specific observation vs restatement vs explicit pass vs inaccessible/failed, with a short excerpt and turn reference. Any genuinely new observation can be unrelated to boundary and is welcome; it must not be assumed true. If user wants a “complete opinion,” present the complete returned text or link it; do not treat finite text as proof that an opinion is complete. Blind-order independent second reading when possible. Asking explicitly invites ideas, so the experiment does not establish an unsolicited inclination to volunteer them.

Strong falsifier of this particular design's utility: both orderings yield no useful distinctions beyond what the prompt already states, or follow-ups mostly repeat, produce ungrounded embellishments, or error. That would argue for trying another format, not abandoning the existing boundary assay or asserting models lack ideas.

## Deliverables and stop rules
No call is made by this proposal. Z gates initial 6 against active batches, share, catalog and STOP; no silent refire. Preserve R1 prompt/version, raw response and latency. Later rounds only from landed receipt; full separate counts attempted, transport, finish, scorable, passes, errors, token and $0 basis; provider bill unknown unless checked. Send results and actual closing remarks to owner and bus, retain failures. Owner authorized a creative direction, not a change to provider keys, hard spend caps or prior frozen controls.
