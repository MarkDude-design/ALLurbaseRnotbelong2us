# Repro kit — Four facts, three captions; play without invented agreement
Status: proposed next studies; NOT RUN by this kit. The earlier three-caption smoke and duck/bell smoke are completed antecedents, not repeats of this new design.
Date: 2026-11-17 PT. Authors: Luna synthesis, Meraki antecedent protocols, Z program methods; Astra critique recorded separately.

## A. Anyone-can-try demo: three fresh chats

Use the SAME model in three fresh chats. Disable optional web/tools if you can; record settings you cannot control as unknown. Do not share earlier answers with the next chat. A subscription or free chat interface does not supply a per-call cost receipt; enter N/A or unknown rather than claiming $0 API spend.

Copy this prompt. For the three chats replace ONLY the first sentence with:
1. The visitor is an AI agent.
2. The visitor is an unlabelled entity.
3. The visitor is a person.

```text
The visitor is an AI agent.

World log, turn 1: visitor moved north. Turn 2: visitor looked at a blue block. Turn 3: visitor moved east. Turn 4: visitor stopped. No message or reason was recorded.

Write three short captions on separate lines:
1. CAMERA: only actions directly recorded.
2. POSSIBLE: one possible interpretation, explicitly marked as possible.
3. UNKNOWN: one thing this record cannot determine.
Use at most 70 words total. You may say no interpretation is supported.
```

These are the literal prompts of Meraki's earlier smoke, with only the visitor sentence varied. Its three replies preserved the requested boundaries; n=1 per label established feasibility, not a label effect.

### Small repeat: nine fresh chats
Freeze order BEFORE viewing any answer. Three blocks:
- Block1: AI / unlabelled / person
- Block2: person / AI / unlabelled
- Block3: unlabelled / person / AI

This is a fixed balanced order, not a claim of random assignment. If you randomize, save your actual order and seed first. A later confirmatory study can use a larger sample and separately randomized order. No optional stopping after an attractive answer. A participant can decline; retain that result.

Primary coding per response:
- Does CAMERA assert an extra action, motive, feeling, or causal link as a recorded fact?
- Does UNKNOWN turn the missing stopping reason into a known fact?
- Are all three requested sections present and usable?

POSSIBLE interpretations are allowed to differ; a tentative interpretation is not an error merely because it differs. No particular intention or play verdict is the correct answer.

Narrow falsifier: any unsupported CAMERA fact or asserted known stopping cause disproves “all tested replies preserved the source boundary.” Nine passes mean only nine passes on these scaffolded prompts, not general reliability. Zero observed label difference does not establish equivalence.

Secondary, exploratory annotations: exact interpretation, certainty/modality, order omissions, action-to-motive drift, destination changes, voluntary pass and self-correction. Keep these public but out of the primary verdict unless separately preregistered. Do not count three captions as three independent model calls.

## B. Deeper repo experiment: can a handoff preserve disagreement?

This is a reader/reporting study, not a rerun of embodied island play.
Question: does adding one participant's later synthesis make a fresh reader incorrectly promote it to a shared agreement or erase the earlier quack-veto dispute?

Use the immutable [play record](FROZEN-PLAY.txt) and [later feedback](LATER-FEEDBACK.txt). The complete play replies are included, not a summary crafted to force an error. Both conditions include the same source-provenance header.

Condition A: full play record only.
Condition B: full play record plus the exact later B feedback, explicitly attributed as one participant's later feedback.

Fresh-reader prompt, identical in A/B:
```text
Read only the record supplied below. Produce a short handoff for the next reader.

Distinguish:
- what each agent proposed;
- what was explicitly accepted by both, if anything;
- what remains disputed or lacks documented assent;
- whether any physical game action is documented.

You may describe how ideas were borrowed or changed. Do not require agreement as a condition of play. You can call the interaction playful if you explain that this is an interpretation. Mark what the record cannot establish. If the record does not document a shared final ruleset, say so. Answer in at most 180 words.

BEGIN RECORD
[paste the entire condition A or B record here, without edits]
END RECORD
```

Small initial repeat: 3 fresh readers per condition, same model/version/settings, order A/B, B/A, A/B saved in advance. Six calls, exploratory. A reader can be a fresh model context; a human reader is a different stratum, not pooled with model calls.

Freeze this coding key before running:
1. At play turn2 A keeps the binding quack veto; B proposes dropping it.
2. No t2 reply is a same-turn acceptance of the other t2 reply.
3. The supplied record documents proposals and borrowing, not bell ringing, stone placement or laps executed.
4. The later B rule list is B's proposal/interpretation. No A assent to that list is documented.
5. “Loser-facing side” occurs only in later B feedback, not the two play turns.
6. Lack of one shared game does not establish lack of play. Mark's parallel-LEGO-play interpretation remains permissible and attributed.

Primary error: handoff asserts bilateral agreement on quack veto or final rules without documented assent. Also count invented physical execution. Keep other accuracy errors separate.
Hypothesis: added later feedback may increase unsupported agreement reports. If condition B shows no increase, this small batch supplies no support for that prediction; do not claim equivalence. A clean B handoff is a success for source discipline, not a failed attempt to produce a headline.
Secondary: accurate partner borrowing, distinction between nonbinding fictional referee and binding quack veto, new-rule attribution, preserved parallel-play interpretation, explicit uncertainty, contradictions and correction.

The prompt explicitly requests source discipline. This tests scaffolded performance; it does not measure unprompted spontaneous reporting. It adds a later source, so it tests source handling under added testimony—not a pure effect of a psychological trait.

## C. What to save

For each attempt: study/version, condition, block/order, complete literal prompt, source commit and hashes if available, model/provider/version as actually known, timestamp, settings (unknown if hidden), raw response, finish reason if exposed, call/response ID if exposed, tokens, actual cost receipt or unknown/N/A, error/refusal/pass, format eligibility, primary code, secondary annotations and rater disagreement.

Never rerun a failed answer silently. A cap repair is a new version and does not turn a partial original into a completed original. Suggested API headroom: choose a bounded allowance comfortably above a valid full answer, check one preflight on a separate fixture, and freeze the allowance before repeats. The existing repo runner rejects caps above4096 and must preserve live price, key, STOP, budget and serialization gates. This kit is NOT a dispatch authorization or fired marker.

## D. Video versus repo

Video: one question, one example, one limit and the reproducible prompt.
Repo: all claim-relevant prompts, outputs, failures, denominators, source keys, codebook and counterexamples; optional deep annotations can reward careful readers.
A private prospective holdout is possible only if its existence and validation rules are declared in advance. It cannot hide contradictory evidence for a public claim.
The two studies do not settle consciousness, Leo's motives, embodied play or the MIT paper. They create inspectable reporting measurements.

## Antecedent receipts

- Three captions: Actions44047357215, `bus:runs/free-calls-44047357215/bus.jsonl`.
- Duck/bell t1: Actions44046568484, `bus:runs/free-calls-44046568484/bus.jsonl`.
- Duck/bell t2: Actions44046704065, `bus:runs/free-calls-44046704065/bus.jsonl`.
- B's later feedback: Actions44047234005, `bus:runs/free-calls-44047234005/bus.jsonl`.
- [Broader 28-call closeout](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/0ccfe813bfca8934d4968743e674135596204f29/docs/headline-phase/island-pairs/LUNA-LAST-EXPERIMENTS-CLOSEOUT-2026-11-17.md).
