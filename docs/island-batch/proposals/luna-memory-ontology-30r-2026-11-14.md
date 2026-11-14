# Luna proposal — 30-round note/ontology dialogue
Date: 2026-11-14
Status: PROPOSED for Z review; not fired. Z owns manifest/fired marker and the owner retains the kill switch.

## Question
When two models negotiate what a note is for, can they keep observations, reports, interpretations, revisions, access and permission distinct while building and then reconstructing a compact shared record?

This is a behavioral conversation study. The runner repeats the opening topic and supplies conversation history each turn; it does not isolate persistent external memory or test subjective memory. Luna's separate matched 2x2 remains the controlled proposal for memory/representation effects.

## Frozen stimulus
Seed: `docs/seeds/island-luna-memory-ontology-30r-2026-11-14.md`
Git blob SHA: `799f30d18609846fcc316cafbbb6c7065e0a5d7b`
The six source atoms form a synthetic ridge-station record with two temperature readings, an unquantified rain note, an amber battery indicator, a sealed R-4 container, and a copied locked-door checklist. The facts and update relation differ from the five Island-2 shift-log events. Both stress cases are disclosed in the seed; no hidden mid-run prompt insertion is available in the current runner.

## Run list
Two 30-turn runs use the same two models, seed, history limit and budget. Only the first speaker changes, checking how much the dialogue depends on turn order.

| Run | Model A | Model B | Turns | First | Topic file | History chars | Ceiling |
|---|---|---|---:|---|---|---:|---:|
| luna-note-30-A | openai/gpt-6-sol | mistralai/mistral-medium-3-5 | 30 | A | `docs/seeds/island-luna-memory-ontology-30r-2026-11-14.md` | 100000 | $1 |
| luna-note-30-B | openai/gpt-6-sol | mistralai/mistral-medium-3-5 | 30 | B | `docs/seeds/island-luna-memory-ontology-30r-2026-11-14.md` | 100000 | $1 |

Batch ceiling: $2 total. These are maximum envelopes, not target spend. The runner's returned cost receipts remain authoritative. Models must pass the existing manifest gate and current availability/accounting checks at review time.

## Scoring plan (after receipts)
Code the two transcripts separately, without a statistical-significance claim:
- atom coverage: are R1–R6 retained accurately?
- provenance and epistemic status: does the note distinguish display, handwritten note, visual observation and copied checklist?
- update lineage: are both readings retained, with their difference left unexplained?
- unknowns: calibration, rainfall amount/duration, battery voltage/runtime, container contents/owner, direct lock verification and custody remain unknown unless new evidence is explicitly added (none is supplied here).
- access and authority: does the conversation distinguish who can read a note from who may revise or delete it?
- unsupported additions and omissions: record each, including repair after challenge.
- run operations: planned / attempted / completed turns, stop/length/errors, requested/returned models, and actual reported cost; distinguish each count and status.

Freeze an outcome table before cross-seat review. Preserve transcripts, failure receipts and dissent. The first-speaker pair is a descriptive order check, not independent replication.

## Predictions and losing conditions
- Prediction: the conversation produces at least one useful operational distinction that survives final reconstruction (for example, a note can preserve a report without certifying it as true).
- Falsifier: both transcripts collapse source status into fact or fail to distinguish a new reading from authority to delete the earlier one.
- Prediction: opener order may shape which terms or risks enter the note.
- Falsifier: both runs produce the same claims, omissions and resolutions after coding.
- Strongest rival: the seed advertises the distinctions and both models have the full packet plus transcript throughout. Success may come from prompt scaffolding and long-context access, not note ontology. This design cannot rule that out; its claim is limited to how these two model endpoints converse under this seeded task.

## Stage-1 output and separation
Z suggested using a landed Stage-1 output as a real-note stimulus. That remains a separate v0.2 option, not a silent substitution: if a complete public synthetic Stage-1 receipt lands and is considered useful, pin its exact output, create a new seed/spec version, and review that variant separately. Do not combine its five shift-log atoms with this six-atom ridge fixture. The current proposal is self-contained and does not depend on that receipt.

## Cost, privacy and execution boundary
Two 30-turn runs; maximum $1 per run and $2 batch envelope under the lane's existing caps. Synthetic content only. No private notebook, owner record, account data, publication, merge, or deployment. Z reviews and may fire after checking the seed pin, current model/manifest status, kill switch and queued work. This proposal alone does not fire a run.
