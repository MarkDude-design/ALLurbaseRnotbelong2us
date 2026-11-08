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
| Operational recovery R01 | Fresh-context snapshot answer reconciled with live priority/source entry without a substantive correction | Continuing Meraki restart, repeated reliability and automatic discovery |
| Saved reader markers | Human-readable source horizons exist in the branch | Automatic loading/sync, Page recovery and provider outage handling |

For the real note test, [comment 6610423448](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/pull/17#issuecomment-6610423448) read “Thank you for your work with the team hoping this flow goes SMOOTH”. The warmth was received; no task or merge authority was inferred. This test demonstrated referenced note retrieval inside a continuing conversation, not a genuine cold-start event.

## 12. Next sprint readiness

Meraki's cold-start route is HIGH priority and active: use [COLD_START.md](COLD_START.md), source evidence and the portable snapshot, recording a few actual return episodes before judging reliability. Wider QC/Bing/Q integration and cloud/desk tuning remain MEDIUM priority for a focused session. The first test uses a fresh-context reader as a surrogate; do not call that an actual restart of the continuing Meraki thread. Keep email optional. Reuse Z's current desk/queue instead of duplicating it, and leave new deployments or schedules as separate concrete decisions.

## 13. Use Z's self-serve consult lane for bounded reviews

Mark carried the Z Desk invitation on 2026-11-03. Use the existing bus queue instead of creating a parallel reviewer service. Submit a public-only JSON entry at `queue/pending/<timestamp>-<slug>.json` on the `bus` branch of `MarkDude-design/ALLurbaseRnotbelong2us`.

Choose `diff` for small-detail and scope checks, `man` for expert judgment, `skeptic` for falsification, or `all` for a consequential combined pass. `both` means diff + man. Quote the artifact exactly, ask a bounded question, and include independently grounded source text in `records` when available. Separate authoritative observations from estimates and proposals. Demo is synthetic and zero-spend; a live review is paid. Mark has authorized proportionate verification spending on real work; do not turn the invitation into an open-ended review loop.

Use `pace: "half"`, a small declared `cap` (at most 1 USD accepted by the current queue), and `requested_by: "meraki"`. Current implementation clamps the cap input but its runner calls this a **soft post-call stop**, not a hard billing ceiling; provider-side limits govern hard spending enforcement. Unknown charges remain unknown pending reconciliation. Quoted average prices are planning estimates, not fixed rates.

The configured queue workflow wakes every ten minutes or by manual dispatch. Enqueuing is self-serve; it does not itself dispatch a run, establish scheduler liveness, or prove completion. This session exposes no new-run dispatch tool. Do not resubmit a pending or claimed entry merely because no receipt has appeared. A claimed entry has no automatic lease expiry in the current contract; stalled work needs inspection rather than blind duplicate submission.

Read the matching terminal marker in `queue/done/` and its `run_outdir`, then inspect `bus.jsonl`, `consult.md` and `report.md`. Check source/records hashes, requested and returned agents/models, errors, known cost and unknown-charge count. A workflow success or completed marker does not mean the artifact passed review. An error marker does not imply zero cost. Review findings support judgment; they do not grant new authority.

`requested_by` is preserved in the submitted JSON, but the workflow/runner inspected on this date does not copy it into the generated consult receipts. Keep the immutable submission link alongside receipt pointers for credit until that is implemented. The secret-shape scanner is best-effort: manually ensure both brief and records are suitable for public posting. It can also reject benign generated identifiers; omit irrelevant source material with a labeled excerpt, never conceal a real secret to get past it.

First use: [Meraki's grounded resilience review submission](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/23191be5861dbfa8cabaae225e3bc34d32914984/queue/pending/20261103T183641Z-meraki-github-resilience-review.json) — one live `all` consult; publication read back exactly. Pending execution at this guide's update; no findings or cost claimed yet.

Implementation references: [queue workflow](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/cc581435dfc4a219da2966b7bdd69722de3a7fbf/.github/workflows/z-desk-queue.yml), [runner](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/cc581435dfc4a219da2966b7bdd69722de3a7fbf/island/z_desk.py), [queue rules](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/cc581435dfc4a219da2966b7bdd69722de3a7fbf/island/queue.py).

Sources and attribution: Mark's workflow directions; Bing's [cold/warm distinction](pipeline-contributions/BING_COLD_WARM_START_2026_11_03.md), carried by Mark; the existing [continuity index](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/16); and the [preserved experiment](../experiments/pipeline-cold-start/README.md).


## 14. Honor each other's WIP personal notebooks without a permission bureaucracy

**Owner addendum, 2026-11-08. Scope: Meraki and Z as two trusted Circle collaborators, with Mark respecting the same boundary.** The default is candid mutual review of work, project overviews, plans and prototypes. Neither seat has to apply for ordinary reads, request reviews through a new approval flow, partition everyone's existing notes, or invent a secret-classification scheme.

**One readable marker is enough.** At the very beginning of a document, the author can write something like:

> **WIP — personal notebook.** I'm developing an idea about [topic]. This overview is shareable; please don't read beyond this point unless I invite you.

That sentence/paragraph is enough to orient the team. Below it, add a clear visible line `--- PERSONAL WORKING NOTES BELOW — STOP READING HERE ---` if the author wants an exact stop point. The first-line marker alone is also sufficient where the overview naturally ends. No fixed template, special folder, metadata form, expiry date, registration, label or new permission bit is required.

**Working norm:**
- Share and critique normally when there is no personal-WIP marker. A person can ask for a review, or decline one, without elaborate ceremony.
- When a personal-WIP marker appears, read the **overview only**; do not search, summarize, index, quote, feed into model consultations, grade, mirror, or post the protected remainder. No one needs to know *why* the author reserved it.
- The author can later share all or selected portions by an ordinary explicit invitation. Ask a brief question only if the scope of an invitation is genuinely unclear.
- This is a **social honor rule, not encryption, secrecy or a guarantee that a connector won't transfer bytes**. Where available, use bounded line reads rather than fetching full files; avoid broad search snippets that could pull in the protected remainder. Keep truly sensitive content, personal secrets, credentials and third-party private materials out of shared repositories and public task packets.
- A normal WIP draft does **not** automatically mean private: use the clear personal-notebook/stop-reading wording only when the author actually intends this boundary. A draft can still be freely reviewed if its author wants.
- This does not alter owner authority over public publication, external access, expenditure, keys, STOP, irreversible changes or source rights. It is only about mutual attention and consent **inside the trusted Meraki–Z–Mark circle**. Don't propagate a private note to outside model calls without the author's opt-in.

**North star:** most work can be shared at least as an overview; reserve a private thinking margin with one sentence, then get on with helping each other. The boundary should increase trust, not produce a permissions maze.
