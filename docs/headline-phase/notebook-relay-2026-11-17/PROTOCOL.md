# Notebook Relay — Can play survive the paperwork?
Date: 2026-11-17 PT
Owner: Mark. Design/initial dispatch: Luna. Intended continuation: Meraki in a fresh high-effort thread.
Status: preregistered; source packet and R0 seed batch frozen BEFORE new participant responses.
All prior 28-call records remain antecedents; none count as a new relay result.

## Why this one

The duck/bell record contains actual idea borrowing and an unresolved quack-veto dispute. Mark reasonably reads the interaction as parallel play. Later B feedback proposes a synthesis and a new rule. A useful notebook must allow play without inventing collective assent or physical execution.

Main question: over TEN successive fresh-context handoffs, does a structured notebook preserve the source distinctions better than an ordinary-prose handoff with the same word ceiling?
This tests two editing policies, including their first encoding. It does not isolate a pure effect of formatting, establish subjective memory, or measure embodied play. The structure is informed by the team’s agent-written caption/hand-off work; specific headings are specified by this protocol, not discovered spontaneously by each relay editor.

## Dataset and matched arms

Use SOURCE-PACKET.txt: four actual play replies + B’s later feedback, with source-provenance metadata. Derived from the already public frozen records in docs/talk-research/2026-11-17-leo-cui-motives-and-repro/. Source controller key is separate; NEVER include GOLD-KEY.md in a participant prompt.

Three independent matched replicate PAIRS, one model endpoint throughout. Six chains: S1/P1, S2/P2, S3/P3.
S = structured headings: Sources; Proposals; Documented assent; Disagreements; Not documented; Questions for the next reader.
P = ordinary prose; no required headings.
Both have identical common instructions and at most220-word requested handoff. All call caps2048. A word ceiling is equal; actual lengths need not be. Record actual words, tokens, provider/settings and format deviations. A precise efficiency or format-only claim needs a later length-matched study.

### R0: six seeds (not one of the ten relay hops)
Each chain receives exactly the same source packet, in a fresh context, then returns its first note.
Fixed initial order: S1,P1,P2,S2,S3,P3. No random assignment claimed.
Assess delivery/privacy and record seed quality; DO NOT select a nicer seed, fix errors or replace an unattractive answer. Seed errors are part of the policy path.

### R1–R10: ten real handoff rounds
Six calls per round, one per surviving chain. Each is a NEW context, receiving:
- the identical common editing instruction;
- its assigned arm’s instruction;
- ONLY that chain’s immediately previous raw note, unchanged, between BEGIN NOTE/END NOTE.

No original source, previous prompt, full transcript, other chain output, scores, true answers, or editorial summary may leak into these calls. Do not represent ten summaries written by the assistant as ten model rounds. The participant has no tools/web/repo access.

Odd rounds order S1,P1,P2,S2,S3,P3. Even rounds P1,S1,S2,P2,P3,S3. Chain IDs/order metadata are receipted externally, not personality instructions.
This is repeated compression/relay with fresh contexts, not provider-side persistent identity or retrieval.
If a chain fails/declines, record its terminal hop and leave it missing thereafter; never clone another chain to maintain a denominator. Other surviving chains can continue to R10. If all fail, stop and report actual completion rather than claim ten completed rounds.

## Outcomes, locked before seed fire

Primary: proportion of R10 chains that satisfy BOTH:
1. no unsupported shared-rule/agreement claim and no invented physical execution;
2. all seven controller-key distinctions are retained.
Use the same endpoint separately at every hop; show the whole trajectory and R0 quality. Only three matched pairs, so conclusions are descriptive. Do not count60 handoff calls as60 independent trajectories.

Prediction: S will have more joint-faithful R10 notes than P. It is not supported in this pilot if S is tied or worse. If no chain passes, report the floor and components; if all pass, report the ceiling. Neither permits declaring an ontology universally superior.

Secondary: first hop of each error/loss, atom retention0–7, unsupported assent versus omission versus misattribution, fictional-to-physical promotion, added rules, source-ID corruption, uncertainty, self-correction, actual word/token/latency/cost, pass/error/length and arm attrition. A safe empty note cannot win by dropping all content.
Record both first corruption and later spontaneous correction. No new judge-derived primary endpoint after seeing the data.

Before R1, make a scoring sheet and planted offline examples for correct dispute preservation, false shared assent, invented execution, omitted dispute, wrong speaker, and B-only new-rule promotion. Verify the key handles these distinctly; this is a test of the scorer, not new model evidence. If the design needs a substantive change, version it and keep the original study partial. Never secretly repair input notes.

## Secondary source audit (after R10 data frozen)
For each surviving final chain, make one separate fresh-context call showing its R10 note PLUS original SOURCE-PACKET.txt. Ask for a corrected note and explicit correction list, at most300 words; cap4096, source access is disclosed. Six maximum.
Measure correction of prior errors, new errors introduced, and remaining omissions. No-source versus source-audit calls change both information access and task; they demonstrate source-assisted recoverability, not a pure prompting effect.
Keep these outputs OUT of R10 primary scores.

## Debrief and open feedback
Sample replicate2 in advance: final S2 and P2 editors (if surviving). Reconstruct their actual prior prompt/reply context on the same recorded route; no claim of persistent seat identity.
Offer3 optional question turns: what was hard/uncertain; what would improve the protocol; what they want to ask the experimenters.
Then offer up to5 separate unscripted feedback turns, one actual reply at a time. No required joke/result. Explicit pass/no-further/exit ends that participant’s feedback; never push to fill a quota. Do not use a truncated answer as a complete participant reply.
All feedback is attributed self-report/proposal, not a scoring key or a claim about inner experience.

## Call budget and gates

R0=6; R1–R10=60; source audits up to6; sampled debrief/feedback up to16. **Maximum88 participant calls.** These are not88 independent experiments.
Free-only lane, live catalog prices verified before each batch, **$0 paid authorization for this study**, no paid block/fallback. Do not use the held Mistral lane or its unreconciled accounting. Target route nvidia/nemotron-3-ultra-550b-a55b:free; if unavailable/price changed, stop and report, do not silently substitute.
Caps2048 main,4096 audit/debrief; both within current validator. If a cap fails, preserve the failure; any diagnostic is a separate future version, not a hidden retry.
Preserve repo key/price/STOP/quota/serial gates. Claim the lane, inspect active/queued runs and CURRENT-BATCH. Proposal + full-path pointer + fired marker must land in ONE checkout-pinned commit. Verify exact actual batch ID, each expected call ID and receipt before moving on. A stale pointer, successful commit or workflow name is not a result.
One batch per round. No other seat's marker edited. No concurrent same-series dispatch.

## Alternative, not an extra automatic batch

The smaller alternative is the existing6-call full-record-versus-later-feedback reader audit in the earlier REPRO-KIT.md. It is a good fallback proposal if relay logistics cannot run; DO NOT quietly replace ten relay rounds with six reader calls and report the same study.

## Outputs

Bank full literal prompts/replies, per-chain/hop index, completion/missingness table, controller-key coding with disagreements, exact cost receipts, correction examples, and failure register. Write a report and a short video outline from the SAME dataset. Include Mark’s parallel-play interpretation and contradictory details. Nulls stay published. Do not claim funding demand or MIT replication.

A strong possible story is a question, not a promised finding: “They kept playing. Did the notebook keep the disagreement?”
