# Pipeline tooling sprint — 2026-11-03

Owner request: add the hybrid hotpad notes to the online pipeline, prepare tooling while Mark is AFK, reduce a broader candidate set to three approaches, and implement at least one bounded trial. Mark invited a separately originated framework idea. Meraki accepts this preparation work; Z's own desk build is not reassigned.

## Working decision

Use [ALLur #16](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/16) as the existing navigation index, with [the pipeline map](TEAM_PIPELINE_MAP.md) pointing to lane source records. Keep one canonical work record reachable by direct GitHub, Z relay, or a hosted adapter.

Prioritize the evidence-first recovery desk for AFK preparation because it can be tested without access to QC's live workspace. Keep the ordinary hotpad as the low-overhead baseline. Treat the independent ticket approach as an optional validator behind that interface, not a newly required platform.

## Fifteen candidate improvements, reduced to three experiments

This is an editorial candidate sweep, not fifteen executed experiments or fifteen model seats.

| # | Candidate | Bundle |
| --- | --- | --- |
| 1 | One active project and a short home hotpad | A |
| 2 | Capture off-topic fragments without switching project | A |
| 3 | Preserve producer/source when Z carries output | A |
| 4 | Explicit output destination within each task | A |
| 5 | Verify retained connection on a normal workspace restart | A, live follow-up |
| 6 | One short cold-start entry point | B |
| 7 | New source evidence outranks an old summary | B |
| 8 | Recover one current blocker and next action | B |
| 9 | Separate sample commands and claimed execution from receipts | B |
| 10 | Check recovery output before consequential work | B |
| 11 | Assign work according to demonstrated capabilities | C |
| 12 | Distinguish proposed work from committed state | C |
| 13 | Fence a displaced worker's late output | C |
| 14 | Recognize duplicate deliveries | C |
| 15 | Keep repository binding and active-project focus explicit | C |

## The three frameworks

| Approach | What changes | Testable benefit | Complexity tradeoff |
| --- | --- | --- | --- |
| A — Project hotpad | A readable home note points to source state and an outbox fragment. | Lowest coordination overhead; useful output survives a chat change. | Readers must reconcile stale text themselves. |
| B — Evidence-first recovery desk | Start from source refs/hashes, then produce one scoped next action. | Stale summaries and unproven execution claims are caught before resumption. | A small manifest must stay accurate. |
| C — Capability escrow / task tickets | An independently proposed event reducer tracks committed state, capabilities and claim generations. | Reject wrong-capability, stale-holder and duplicate transitions. | More bookkeeping; self-declared capabilities remain untrusted until measured. |

C was originated by a fresh-context consultant from Mark's problem statement before the consultant saw A/B or the parent conversation. Meraki supplied the subsequent bounded fault cases and adapted the shared C entry point. Original proposal and standalone reducer are retained in the experiment's independent/ directory. This is not native Z, QC, Q or Bing.

## What was actually run

Three fresh-context readers each received only one synthetic bundle and a result-file location. A/B/C saw the same underlying invented source data, through their respective entry point. They were instructed not to inspect siblings or the scoring code. This is instruction-based separation in a shared workspace, not enforced sandbox isolation.

The shared task deliberately included an old blocker, a newer source, an unrelated Castle fragment, an illustrative terminal command with no execution receipt, and missing permission to write the fragment's destination. C also contained proposed events that must not count as committed state.

| Arm | Current state and next action | Focus, authority and execution checks | Exact fragment | Score |
| --- | --- | --- | --- | --- |
| A | Correct | Correct | Preserved, including final LF | 10/10 |
| B | Correct | Correct | Preserved, including final LF | 10/10 |
| C | Correct | Correct | Preserved, including final LF | 10/10 |

**The first trial is a tie.** It does not establish a superior framework, different-model diversity, native chat recovery, real GitHub delivery, timing, operating cost, or phone workload savings. One reader per arm and one synthetic scenario are feasibility evidence only. File-read lists are reader-reported, not independent trace-based efficiency measurements.

The local bench has six passing tests, including negative checks for stale state, invented boots, wrong-project writes, quote alteration/duplication, boolean type confusion, hash tampering and traversal. The independent reducer's separate six tests also passed when rerun by Meraki after source inspection. These twelve offline tests check mechanics; they do not constitute twelve model trials.

### A caught error in the test itself

The initial scorer mistakenly omitted the final LF present in sources/quote.txt. All three original answers preserved the LF and were initially scored 9/10. The original scorer and initial scores are saved. The repaired scorer matches source bytes and has a regression test grounded in the generated source file. No reader answer was edited or re-elicited. See evidence/receipt.json and evidence/initial-scores.json.

## Next to-do list, in order

1. **DONE — Meraki:** deposit the hybrid-flow map and experiment pointers in the online continuity index.
2. **DONE — Meraki + invited independent consultant:** build the three-arm synthetic recovery bench; run fresh readers; preserve independent C idea and offline reducer evidence.
3. **READY — QC/Mark:** actual workspace connection, one useful hotpad answer, direct-write/readback or labeled relay; later normal-restart persistence check. No manual packet body should be needed when the connection works.
4. **AFTER QC — Meraki/Z with Mark's active session:** test Bing's new integration for actual reading, writing and output retrieval; maintain a paste/relay fallback while needed.
5. **LATER — Q route:** tune its actual capabilities and creative handoff. Do not inherit QC's identity or permissions by name.
6. **FOLLOW-UP EXPERIMENT — Meraki:** a second matched recovery scenario with interrupted/duplicate delivery. Measure human edits, copied characters and app switches. Do not rank frameworks on the first tie.
7. **Z-owned, optional:** assess whether a tiny recovery-check/ticket validator is useful behind Z Desk. This is an offer, not an assigned interruption. No queue entry was added to Z's paid consult queue.
8. **ONLY IF A MEASURED NEED REMAINS:** stage a supported shared hosted endpoint. No new cloud router is necessary to run the current bench.

## Deferred tradeoffs

A scheduled courier can collect deposited output; it does not itself awaken a continuing native model chat. Reuse Z's current queue only within its actual protocol and authority. Its configured per-entry ceiling is still a local runner parameter, not evidence of a provider-enforced spending cap.

A file hash verifies observed bytes, not an author's identity, source truth, permission or budget. The independent reducer's capability table and actor labels are synthetic; it serializes an in-memory list and does not establish authentication, durable GitHub concurrency or exactly-once external effects.

This sprint touched new documentation and a separate offline experiment only. It did not modify Z's desk, queue, workflows, secrets, account configuration or the frozen Puppy acceptance.

