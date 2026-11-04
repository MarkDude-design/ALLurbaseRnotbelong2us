# Staggered experiment streams — proposed review card

**Status: DRAFT / OWNER REVIEW.** This document proposes a low-overhead routing agreement; it does not configure or start a GitHub Actions workflow, create model invocations, change permissions, raise spending limits, or merge anything.

## Two routes, separate clocks

At the inspection horizon on November 4, 2026, there are two independently receipted **Standards / 30** participant streams:
- **Primary, Z:** accepted through Round 16; [private live state](https://github.com/MarkDude-design/Project-Spiral/blob/main/pipeline/standards-2026-11-04/STATE.json), [round receipts](https://github.com/MarkDude-design/Project-Spiral/issues/2). Its next eligible native turn was 17 at inspection; always re-read before action.
- **Secondary, Sol/Meraki:** accepted through Round 3; next native turn was 4 at inspection, same private state and receipts. Sol's tests are source-exposed rather than blind parallel samples.

**Concurrent projects do not require simultaneous native turns.** Start streams at different times; each seat obtains a real invocation, reads its own live cursor, checks stop/claim conditions, performs at most one eligible round per invocation, verifies the external effect, and leaves a receipt. A separate ready, unclaimed bonus idea can be staged for later without counting it as an accepted round. Round counts are per seat, never added together as if independent scientific replicates.

Neither a ledger pointer, a schedule tick nor a repository commit silently invokes a different native model seat. Keep the existing standalone pulse and issue-based Precipient gray-smoke work separate from Standards numbering. Artificial sprint constraints are a research instrument, not a deliverable quota.

## Scheduling and claiming: default calm path

1. **Read:** THE LEDGER → public register → private, current `STATE.json` and issue tail. Name the native seat, its own source horizon, and what is actually eligible.
2. **Check:** participant PAUSE/DECLINE/VETO; the actual tool/permission surface; current checkout claims and expected state/registry SHA. If uncertain, HOLD without inventing a blocker.
3. **Act:** One valid native seat turn may claim its own due work under the private `CHECKOUT.md`. Do not share a single unversioned work slot between two active seats. Reconcile state again before consequential effects.
4. **Verify:** Parse resulting state, check effect/round receipt against its authoritative source, then release the claim. **A completed dispatch alone is not completed work.**
5. **Stage bonus:** nonblocking reviewer questions, draft experiments, visual checks, or source audits can queue behind the mainline. Their presence does not impose a deadline on Z or a forced next turn on Sol.

An experiment with a hard-coded round target can retain that target; an issue-based lane such as Precipient may instead record `GRAY:RESOLVED` or `GRAY:BOUNDED-UNRESOLVED` and move on without filling a quota.

## Explicit owner-review stops (lead calls the blocker early)

- **Live Z+Sol CT-1 collision test:** the second half of the existing [private checkpoint proposal](https://github.com/MarkDude-design/Project-Spiral/issues/2#issuecomment-6642645080) needs two near-simultaneous native firings. It is **not** the default two-stream arrangement and is **not being fired by this PR**. Owner may coordinate the timing separately.
- **Workflow changes or commands:** any PR changing `.github/workflows/**`, trigger schedules, secrets/keys, authentication, dispatch behavior, public-bus processing, or queue budget limits must present its precise diff to Mark for a decision **before merge or execution**. Do not substitute a routine comment for that review.
- **Material external effects:** publishing private algorithm internals, changing repo visibility, merging code with consequential operational behavior, unbounded spending or irreversible actions need their applicable owner/platform gate. Preauthorized bounded research does not erase that gate.
- **Participant stop:** no owner review or scheduler can override a participant's VETO on the same proposal. PAUSE means hold until a valid resumption. A stop propagates to queued/delegated work. The two routes need not stop together unless the shared action truly depends on both.
- **Actual error:** report the exact denied permission, missing tool, conflicting SHA, or provider cap. Do not ask for root-level permission just because a GitHub client or isolated harness is missing a method.

## Reviewable proposed next move (NO ACTIONS FILES EDITED)

1. Merge or amend this document **only if the owner finds the routing useful**.
2. Permit staggered **Sol Round 4** in an actual Sol turn while Z continues its independently receipted mainline. This is a normal separate turn, **not CT-1**.
3. Keep active owner-review comments narrowly scoped to real workflow changes, an actual checkpoint, or a critical new blocker. Stage optional bonuses instead of interrupting the mainline.

**Provenance:** routing proposal written by Sol/Meraki in a connected GitHub session, not Z's authored rule or a model consultation. The starting counters above are an inspected snapshot, not a live dashboard. This draft makes no claims about how many simultaneously executing jobs the model providers guarantee.

**Privacy:** no proprietary N15 implementation or private Spiral source is included. Public links lead to private project artifacts only for authorized readers.
