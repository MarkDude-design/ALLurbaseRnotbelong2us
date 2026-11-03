# Team best practices — Meraki

Maintainer: Meraki. First working edition: 2026-11-03. Mark assigned this guide for reusable lessons across future pipeline sprints. It complements Z's style guide; it does not redefine Z's desk or anybody's authority. Practices change when evidence or Mark's directions change.

## 1. Give Mark one phrase and keep the bookkeeping behind it

The intended everyday request is **“warm start the pipeline.”** “Cold start the pipeline” requests project orientation. These are team workflow conventions, not built-in product commands.

Start from [the pipeline map](TEAM_PIPELINE_MAP.md). The returning seat reads its [saved per-stream marker](pipeline-state/meraki.json), fetches the corresponding thread and then its later material. Mark need not remember comment IDs. An exact marker remains an optional diagnostic override.

Keep markers per seat and source thread, not one number for the whole team. Advance only through material actually retrieved. Preserve failed/unread stream markers. A missing marker, deleted source or unverifiable gap calls for bounded cold recovery, not a claim that nothing changed.

The initial marker file is saved now. No automatic loader, background polling or cross-platform synchronization has been installed.

## 2. Keep cold, warm and task handoffs distinct

| Return | Reader needs | Normal output |
| --- | --- | --- |
| Cold | Project, current task role, goal, limits, current blocker and source links | One source-backed next action |
| Warm | Changes between the reader's last verified horizon and a newly read horizon | New material, pending attention and next action |
| One-job handoff | One question, bounded inputs, destination and completion condition | Answer at home or a precise blocker |

A returning reader should not ingest an entire archive when a short entry point suffices. Keep source detail available behind links.

## 3. Treat a fridge note according to what it says

Notes can be left by Mark, Z or the returning seat itself. They may be a greeting, reminder, question, task, changed direction or withdrawal. Use context and ordinary judgment. A greeting is not approval; a question is not an assignment.

A note can stay visible, be marked handled, or be cleared from the display. Retain consequential decisions and evidence in their source record. Do not use a calendar expiry to discard unread work or erase someone else's pending note.

## 4. Record reasons at the decision, not after memory fails

Capture the decision, its recorded reason, evidence and whether it remains active or was superseded. The ledger can preserve recorded rationale; it cannot reconstruct reasons never captured. Optional narrative should link back to that record.

## 5. Keep one active worker project and a home exchange pad

Switch the worker assignment deliberately. A quick Castle question can still go to Z or Meraki while workers focus on Puppy.

The connected repository can be the home inbox/outbox. A fragment about another project records its source/exact text and intended destination without changing the active project. Reading another permitted source and writing another repository are distinct capabilities.

## 6. Allow three delivery paths to the same work record

Use direct GitHub output, an attributed Z relay, or a supported hosted courier. Preserve producer, carrier, source and destination. A relay's successful post does not establish that the originating seat can write directly.

Routine questions go to Z first, then escalate when needed. Empowered direct consultation remains available. Review and recommendation do not silently assign an implementer.

## 7. Keep instructions and capability claims honest

A pasted terminal command is not proof it ran. Inspect the actual host's tools and receipts. A shared GitHub login proves account access, not the model's identity. A hash shows observed byte equality, not truth, authorship or permission.

Use proportionate checks before consequential work and review afterwards; avoid turning routine reversible steps into new permission ceremonies. No credential belongs in a task packet, comment or transcript.

## 8. Preserve exact material where exactness matters

Keep quote bytes and source anchors when requested. Distinguish an excerpt or editorial summary from original text. Preserve a failed test and its repair; never silently edit returned answers to improve a score.

## 9. Make recovery portable without creating competing authorities

Use the same small recovery contract in Markdown/JSON regardless of storage: project, one current goal/action, decision pointers, source revision, reader horizons and read/write scope.

GitHub is the current verified shared route. A Page/Canvas or a saved recovery snapshot can supply orientation when its contents are actually available. A fallback snapshot states its revision and last verified horizon. It does not claim to know changes that happened after that horizon.

Keep one authoritative work record/writer policy. A cloud or other mirror should carry a source revision and digest and label staleness. If the primary is unavailable, recover from the snapshot at its stated horizon and stage new work as pending synchronization. Do not silently promote a mirror or split writes between two masters.

## 10. Distinguish the product's features from this session's access

Official OpenAI documentation describes [Pages as shared notes/reference documents with reusable prompts](https://learn.chatgpt.com/docs/space/pages) and [agent work alongside a page](https://learn.chatgpt.com/docs/space/agents). That supports using an explicitly supplied Page as a recovery source.

This session has no selected Page and no Page editing capability exposed. Automatic rediscovery of a Canvas in a new chat has not been tested. A successful Page read and a true fresh-thread recovery must be measured separately. Do not assume that creating a document installs persistent memory or a scheduler.

## 11. Record exactly what the test established

| Observation | Established | Still untested |
| --- | --- | --- |
| Three fresh-context synthetic readers | Each recovered its bounded invented state; 10/10 after documented scorer repair | Real QC/Bing access, native thread restart, cost or latency benefit |
| Six bench plus six independent reducer tests | Tested mechanics pass offline | Production concurrency or exactly-once external effects |
| Mark's real fridge note on PR #17 | Comment locator resolved to the correct PR; greeting retrieved; no later comments at read horizon; no invented approval | No-number lookup after losing this chat, or automatic marker advancement |
| Saved reader markers | Human-readable source horizons exist in the branch | Automatic loading/sync, Page recovery and provider outage handling |

For the real note test, [comment 6610423448](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/pull/17#issuecomment-6610423448) read “Thank you for your work with the team hoping this flow goes SMOOTH”. The warmth was received; no task or merge authority was inferred. This test demonstrated referenced note retrieval inside a continuing conversation, not a genuine cold-start event.

## 12. Next sprint readiness

Keep QC's useful home-output round trip next, then Bing's new integration and Q tuning. Follow with no-number marker retrieval, a missing-marker cold fallback, and an explicitly supplied Page or independent snapshot test. Keep email optional. Reuse Z's current desk/queue instead of duplicating it, and leave new deployments or schedules as separate concrete decisions.

Sources and attribution: Mark's workflow directions; Bing's [cold/warm distinction](pipeline-contributions/BING_COLD_WARM_START_2026_11_03.md), carried by Mark; the existing [continuity index](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/16); and the [preserved experiment](../experiments/pipeline-cold-start/README.md).
