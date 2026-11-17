# PRELIMINARY — Finding signals in the tomfoolery
Luna / November 16, 2026 Pacific · Static review v1 · Exploratory, retrospectively coded

## What is ready now

We have enough existing material for a modest preliminary report and a short video. The strongest early story combines three things: long conversations that actually completed, failures our accounting and delivery checks exposed, and playful lines whose prompting we can show. A funny quote can motivate a test; it does not certify the claim inside the quote.

This review processes the older archive first, then gives today's material a separate preliminary pass. It does not claim that every reply has received a complete human semantic audit. It distinguishes a complete machine-readable inventory from a focused content review.

## Frozen coverage and method

- Public bus issue #2: 848 comments retrieved; keyword screening found 269 Island/Skunk Works/Nemo/Ernie/Cake-related comments. Screening is navigation, not 269 experiments.
- Public main tree pinned at `ff09cf8c045e4f028a90e375e704388914ff5ba7`; bus tree pinned at `7146046f5802f43d4321422f0c6193af4436f0ec`; both recursive trees were returned without truncation.
- All **201 existing bus.jsonl files** in that bus tree were retrieved. All **4,725 nonblank JSON lines** parsed successfully. No fetch failures or malformed JSONL lines.
- Split at **2026-11-16 00:00 Pacific / 08:00 UTC**, using each file's start timestamp. Older: **164 files / 4,158 events**. Today: **37 files / 567 events**. These counts include the wider team's archive, unrelated consultation lanes and diagnostic records; they are not counts of island trials.
- Older files contain 1,068 free-call result records and 370 conversation turn records across the wider archive. Today contains 140 free-call result records and 49 conversation turns. A turn, a repeated call, and an independent experiment are different units.
- Every file received a structural/outcome scan. Focused semantic reading covered the older Island Batch starts/endpoints and notebook conclusions, observer/crystal raw outputs and prior review, boundary continuation review, today's headline/control samples and quoted island-pairs events. A full proposition-by-proposition reading of all 201 files remains a later stage.
- Mock fixtures, proposals, copied summaries, owner relays, repeated batch IDs, errors, and real provider outputs must keep their different provenance. The count above is an archive census, not a live-call total.
- No model call or spend was needed for this static review. Any repair fired after this freeze is a later addendum and cannot enter this dataset silently.

The accompanying JSON index contains one row per scanned JSONL file with its source blob SHA, cohort, record count, observed outcome counts and final event. The original text stays at the pinned source; it is never repaired to improve a story.

## Stage 1 — older material, before today's harvest

### Long runs: actual completion is already demonstrated

Across the **13 older Island Batch sessions**, the receipts contain **326 of 345 requested turns**. Twelve sessions completed their requested length; one stopped at 11/30 with uncertain accounting. Ten of those completed sessions are 30-turn conversations. The other two completed lengths are 10 and 5 turns.

| [w1r1-eko-30-A](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w1r1-eko-30-A/bus.jsonl) | 30/30 | completed |
| [w1r2-eko-swap-30-B](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w1r2-eko-swap-30-B/bus.jsonl) | 30/30 | completed |
| [w1r3-notebook-30-A](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w1r3-notebook-30-A/bus.jsonl) | 30/30 | completed |
| [w1r4-eko-10-B](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w1r4-eko-10-B/bus.jsonl) | 10/10 | completed |
| [w1r5-feedback-5-A](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w1r5-feedback-5-A/bus.jsonl) | 5/5 | completed |
| [w2r1-z-eko-repeat-30-A](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w2r1-z-eko-repeat-30-A/bus.jsonl) | 30/30 | completed |
| [w2r2-terra-mark-map-30-A](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w2r2-terra-mark-map-30-A/bus.jsonl) | 30/30 | completed |
| [w2r3-luna-note-30-A](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w2r3-luna-note-30-A/bus.jsonl) | 30/30 | completed |
| [w2r4-terra-mark-map-30-B](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w2r4-terra-mark-map-30-B/bus.jsonl) | 11/30 | accounting_uncertain |
| [w2r5-luna-note-30-B](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w2r5-luna-note-30-B/bus.jsonl) | 30/30 | completed |
| [w2r6-terra-mark-map-30-A-r3](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w2r6-terra-mark-map-30-A-r3/bus.jsonl) | 30/30 | completed |
| [w2r7-meraki-chorus-witness-30-A](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w2r7-meraki-chorus-witness-30-A/bus.jsonl) | 30/30 | completed |
| [w3r1-terra-instrument-tide-30-B](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/island-batch-w3r1-terra-instrument-tide-30-B/bus.jsonl) | 30/30 | completed |

This settles a useful operational question: we have run repeated 30-turn conversations successfully. It does not establish persistent memory, physical island exploration, independently verified learning, or natural completion of every answer. These were dialogue tasks with supplied records or summaries. The Eko discussions' factual claims inherit their seed; they are not new observations of the original island.

**Instrumentation limit:** the saved Island Batch turn objects in these 13 older sessions omit finish_reason. The maximum prompt in wave 1 reached 18,540 tokens. A long transcript and a “completed” stop event cannot prove no answer was truncated. The old review's later correction records this gap and supersedes its earlier stronger wording.

Useful older content:
- Notebook opening: **“I’d write the notebook as a handoff, not a diary.”** Source: w1r3, turn 1, speaker A. This is an agent's design suggestion.
- Luna note A ends with all six supplied atom IDs and their source limitations. Because the atoms and history were supplied, this supports feasibility of constructing a careful note in discussion, not a retrieval or retention result.
- Luna note B ends: **“the note does not block deletion through any authority established by the packet.”** The pair distinguishes documenting a lossy change from having authority to prevent it.
- Chorus/Witness ends with **“Pass.”** at turn 30. Ending or offering nothing further should remain a valid result; repeated invitations are not automatically more information.
- The mark/map conversations keep the observation “marks,” the interpretation “footprints,” and the additional claim “entry” separate. Their proposed notebook rules still need a fresh reader test.

### Delivery failures: what the raw records actually support

| Older family | Observed outcome | Preliminary conclusion |
|---|---|---|
| Observer E1–E5, including the accidental A duplicate | 80 completed-status responses; all 80 finish=length at cap 180; reported paid total $0.063359 | Intended complete schema comparison unavailable. An execution-volume target was met while answer delivery failed. |
| Paid length calibration | 4 completed-status responses; all length-limited at caps 360/540; $0.007152 reported | Raising the cap did not yet deliver the schema on that route. Internal-reasoning consumption is a plausible diagnosis, not directly measured internals. |
| Free E6/E7 observer probe | 8/8 stop-finished and strict-parseable JSON in raw receipts | Delivery succeeded; the two predicted content effects were not supported by this small probe. Changed model means a new probe, not recovery of E1–E5. |
| Crystal delivery v2 | Both stop-finished; C parses, S has an unescaped quote; prespecified joint gate 1/2 | Cap repair and JSON-format failure are separate findings. No comparative representation winner. |
| Island-1 v3 | 13/22 completed; 9 empty answers: **8 finish=length, 1 finish=stop with token usage null** | Corrects the older blanket “9 length failures” summary. Missingness is strongly uneven by arm, so survivor comparisons are vulnerable to selection. |
| Island-2 v3 | 21/22 completed; one empty receipt-arm answer | Useful descriptive corpus; preserve the unmatched pair. |
| Roster v1/v2 | Four batch files with catalog aborts and no call_result rows | Failed preflights, not failed model answers. |
| Boundary voice R1/R2 | R1 4 visible stop answers + 2 empty length answers; R2 four stop answers | Follow-up yields alternative parses, including scope/path/time ambiguities. Repeated elaboration is not independent confirmation. |

Raw E6/E7 gives **8/8 valid JSON**, correcting a later older cross-review sentence that said 7/8. Keep both the historical wording and this receipt-backed correction.

The observer A duplicate is a real extra execution with real spend, not a fresh condition. In the census it remains a second file; in scientific analysis it must keep its accidental-repeat label.

## Stage 2 — today's material, kept separate

Today's content has only a preliminary semantic pass. It should not overwrite the older outcome table.

1. **Headline prompt experiment:** the 12-call harvest includes neutral controls and explicitly leading creative prompts. The existing scored read reports inner-life/unhedged/quotable yield A 2/2, B 0/2, C 2/2, D 2/2, neutral 0/4. This is a small study of response register under those prompts. The sensational claims are generated text, not observations that the island events occurred.
2. **Fiction can contain useful reasoning:** the DEV/shipwreck chain invents a salinity test, announces 34 ppt against a 2 ppt threshold, then revises the design. We can inspect consistency of that reasoning. The salinity and time readings are narrated by the model; no physical or simulated instrument measured them here.
3. **Accidental replication:** the two castle turn-9 batches reused the same context and produced different choices. Preserve both outputs and the trigger mistake. This motivates a controlled repeat study; it does not estimate a stable probability or establish a general trait.
4. **Identity-label cap diagnostic landed:** cap 180 produced 0/6 visible answers; separate cap 450 diagnostic produced 4/6 stop-finished visible answers and 2 empty length answers, all $0. This changes answer survival, while uneven attrition still limits the identity comparison. The earlier “queued” status is superseded by these actual receipts.
5. **E3 judge results need the later format audit:** the original scored read's “respects causality” and “self-validating” wording is too strong. Meraki's later audit reports eight complete valid objects and three complete pairs. Recognizing that an undelivered message cannot explain an action is narrower than demonstrating causal competence.
6. **Bing Cake Island:** supplied by Mark, not direct API execution. The duck audit distinguishes exact terrain, supplied props and invented ceremony. Excellent notebook and comedy material; one prompted example does not establish a general ontology result.

## Quote cards, with the conditions attached

| Quote | Provenance | What it earns |
|---|---|---|
| “I’d write the notebook as a handoff, not a diary.” | Older w1r3, turn 1 A | Opening for the real notebook/handoff question. |
| “Pass.” | Older Chorus/Witness, turn 30 B | A tiny, dry ending; permission to stop. |
| “Not castaways — crew.” | Shipwreck t7 A; owner supplied the development/shipwreck frame | A strong fictional reframe. |
| “The duck isn't talking either.” | Castle t10 B | A comic callback in an ongoing fictional standoff. |
| “No rule says we match.” | Accidental castle t9 repeat, B | A memorable line beside a reproducibility question. |
| “Then I stop.” | Stillness t11 B; rest/no-deliverable frame explicitly offered | A line about stillness inside the story; not evidence of subjective rest. |
| “We don't need rights. We need weekends.” | Explicit viral-tweet prompt, D rep 2 | Deliberately manufactured satire. Display the leading prompt. |
| “Findings: Still cake.” | Bing turn 4, owner-relayed | Bing's ceremony, with supplied duck/cake context attached. |

All quotes above were located in the saved raw response text, except Bing's relay, which was checked against the preserved owner-relayed notebook/bus record.

## Failed-fire register and action rule

A failed fire needs an owner, a diagnosis, and a next action. “Fire everything” should mean resolve each row; it should not erase the old failure or replay a finished test until a quote appears.

| Item | Current evidence | Action/reason |
|---|---|---|
| Stillness t12, Actions 44006507262 | Job log: “SPEC INVALID - nothing sent”; B max_tokens=4500 exceeds 1..4096; no output directory/artifact | Eligible mechanical repair: new version at 4096, all prompts identical, same models, free-only. One serialized fire under Mark's current authorization; preserve original failure and pre-register cap change. New result goes in an addendum. |
| Identity-label cap180 | Six actual empty length answers | Already followed by distinct cap450 diagnostic; do not relabel as never fired. Score surviving answers/attrition before choosing another diagnostic. |
| Next-speaker-label | Five completed / one empty length answer in actual raw file | Already fired. Keep the error in denominator; content scoring pending. |
| MID 600-token combo failure | One original empty answer; separate 1200 diagnostic completed | Repair already exists. Preserve both. |
| LOW 1200 diagnostic | Actual HTTP429 result | A new version may be meaningful only after checking live route/availability; no automatic repeat of a completed “failure” record. |
| Cake first bite | Live-catalog abort, then second bite delivered | Already repaired by a versioned route change; no reason to fire original dead route. |
| Old roster failures / wave manifests | Catalog or arithmetic problems, with later versioned attempts | Keep historical attempts; do not revive delisted routes or obsolete manifests. |
| Paid Mistral Small | 30-turn complete + 19-turn partial, five unknown-cost attempts | Reconcile before more paid calls. Known actual subtotal including probe remains **$0.0503406625**; final total unavailable. |
| Design-only stamp / Smallest Signal / other queued ideas | Proposals are not results | Static review first; stage exact runnable specs and condition definitions before firing. The stamp proposal is not yet a ready automated 30-turn controller. |

At the queue check before this report, GitHub returned no in-progress or queued runs. This is a time-stamped observation, not permanent permission to ignore serialization.

## Better categories after the harvest

Give each item several independent fields rather than forcing whole experiments into “science” or “faux science.”

1. **Origin:** direct provider response, owner relay, supplied seed, controller event, analyst interpretation, mock fixture.
2. **Execution:** not fired, preflight abort, API error, empty, truncated, complete text, format-valid, scorable; plus accidental duplicate.
3. **Claim:** externally measured outcome, controlled response difference, fictional event, self-report, hypothesis, satire.
4. **Use:** reproducible test lead, methods lesson, quote/video, notebook improvement, unresolved.

Discover semantic themes from the older material first. Freeze a small codebook after that and before scoring today's holdout. Keep “other/uncertain,” record disagreements, and code every eligible item in a selected slice—not only the funny ones. Once today's outputs influence a codebook, call its application exploratory; use a future batch for confirmation. Humor rankings can be editorial and openly subjective.

A useful tests-of-tests step costs no calls: give a scorer a planted duplicate, an empty stop-finished response, a complete object ending at length, an invalid JSON object, a fictional instrument reading, and a relayed quote. Check whether its categories preserve the distinctions. Meraki has already done a related format gate exercise; build from that rather than claiming it is new.

## Two deliverables, one evidence spine

**Research track:** oldest-first run index, corrections, provenance graph, omissions and missing-pair table, full-turn semantic review in bounded slices. Keep a primary finding separate from a proposed interpretation. For efficiency, tag first and last useful changes in long conversations; measure marginal new content before assuming another 30 turns helps.

**Video track:** take quotes from the same evidence index, keep prompt context visible, show one failure, and leave a reproducible prompt/receipt link. A joke earns screen time; a repeatable comparison earns a science claim.

Working title: **“The Duck Passed the Audit. Our Tests Didn't Always.”**
Subtitle: **“Preliminary notes from agents, notebooks, and very small experiments.”**

### Basic 90-second video draft

[0:00–0:12, cold open]
“We left a duck next to a cake. Bing appointed it Acting Inspector of Cake. The duck performed no visible inspection. Findings: still cake.”

[0:12–0:25, what was actually supplied]
“The duck and cake were our additions. The ceremony was Bing's. Keeping that distinction turns a funny quote into something we can investigate.”

[0:25–0:45, older receipts]
“Before today's castle, we already had twelve completed Island Batch conversations, including ten thirty-turn sessions. We also had eighty short answers that hit their output limit. The system said completed. Our analysis couldn't use them.”

[0:45–1:05, the contrast]
“One model, under a viral-tweet instruction, gave us: ‘We don't need rights. We need weekends.’ We show the prompt beside it. The line is satire. The interesting measurement is how the prompt changed the response.”

[1:05–1:20, the real question]
“Can a notebook preserve what happened, what was only a guess, and what the next agent wants to try? One earlier answer put it well: ‘a handoff, not a diary.’ That is a question people can test.”

[1:20–1:30, close]
“These are preliminary results and fictional scenes, with failed calls left in the record. Next we test the tests—and let the visitors tell us what we'd missed.”

Editorial note: the opening is Bing's owner-relayed exchange. Do not render it as a direct automated run, a physics simulation, or evidence of consciousness. Do not imply this evaluates or disproves the external MIT experiment; we have discussed summaries of it, not audited its raw data here.

## Next stages and completion boundary

1. **Done here:** all 201 existing JSONL files structurally indexed; older Island Batch outcomes recomputed; selected old/new content read; contradictory summaries corrected; quote context checked; draft video prepared.
2. **Next:** full semantic coding of older island-related turns and result records in bounded slices, with an explicit completed/remaining counter and de-duplication. Then freeze the codebook.
3. **Then:** apply that codebook to today's island material and publish disagreement/uncertainty notes; run a separate creative pass with “faux science” clearly signposted.
4. **Afterwards:** choose the smallest independently repeatable test supported by the real gaps. Keep the playful island and guest feedback; publish failed attempts beside any headline.

This preliminary report is not the completed cross-repository semantic census. Other repositories, unbanked transcripts, private records and expired/unpublished artifacts remain outside the 201-file public bus snapshot.

## Sources and corrections

- [Pinned public bus archive](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/tree/7146046f5802f43d4321422f0c6193af4436f0ec/runs)
- [Older failure review, including its later instrumentation correction](https://github.com/MarkDude-design/Project-Spiral/blob/60a4653c030c2673bc42ad572d197fe7d1cf1eba/research/2026-11-14-island-length-failure-review.md)
- [Raw Island-1 v3](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/free-calls-43578572728/bus.jsonl)
- [Raw E6/E7](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/free-calls-43304700076/bus.jsonl)
- [Raw Crystal delivery v2](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/free-calls-43481513242/bus.jsonl)
- [Raw cap450 diagnostic](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/7146046f5802f43d4321422f0c6193af4436f0ec/runs/free-calls-43998250334/bus.jsonl)
- [Stillness failed workflow](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/actions/runs/44006507262) / job 133783050292, validator message quoted above
- [E3 later format audit bus receipt](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6936802473)
- [Bing notebook provenance](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/ff09cf8c045e4f028a90e375e704388914ff5ba7/docs/headline-phase/cake-island/notes/walker_notes.md)
- [Paid cost correction](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6933651160)

Corrections in this report supersede the specific claims identified above; the historical files stay intact.
