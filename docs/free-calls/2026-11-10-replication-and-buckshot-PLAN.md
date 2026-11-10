# REPLICATION & BUCKSHOT PLAN - 2026-11-10 (owner-directed; Z seat executes)

Owner directives (~10:15 PT 2026-11-10):
1. Every experiment runs TWICE on the frozen 4-question battery (same specs, same budgets). If both runs agree -> stable.
2. ANY variance between the two runs of the same model -> fire a THIRD run and zoom in ("those are the ones where the magic lives").
3. Then buckshot the battery to as many models as possible: FREE and PAID, frontier included.
4. Routing: NON-GPT experiments + scores go on the PRIVATE ledger (talks-main) in a way every seat can read. GPT-family institute decisions belong to Meraki (owner will brief them; awkward otherwise).
5. Envelope: $5-$10 total. Runner code ceiling $1.00/batch stays.
6. Z runs 5 hourly one-shot alarms (~19:25Z, 20:25Z, 21:25Z, 22:25Z, 23:25Z); the 18:25Z task banks b3 + fires queue item 1.
7. MAX_CALLS is 8 per batch - every staged spec respects it (rep-b1 was split 4 rungs + gpt-5.5 into rep-b1b for this reason).

## QUEUE (fire strictly ONE at a time; next only after prior receipts landed AND banked)
| # | batch | spec | budget | status |
|---|-------|------|--------|--------|
| 0 | gpt-family-usage-ladder-b3-effort-sweep | docs/free-calls/2026-11-10-gpt-family-usage-ladder-b3.json | $0.50 | RECEIPTED: run free-calls-42869252253, 4/4 stop, $0.063530; banked art-talk + ledger batch 35 (~18:15Z) |
| 1 | ladder-rep-b1 (lower 4 rungs x2) | docs/free-calls/2026-11-10-ladder-rep-b1.json | $0.50 | RECEIPTED: run free-calls-42872468891, 8/8 stop, $0.028497; banked art-talk + ledger batch 36; zero variance (~18:25Z) |
| 1b | ladder-rep-b1b (gpt-5.5 x2) | docs/free-calls/2026-11-10-ladder-rep-b1b.json | $0.50 | RECEIPTED: free-calls-42878682709, 2/2 stop, $0.050190, zero variance; banked + ledger 37 (~18:50Z) |
| 2 | ladder-rep-b2 | docs/free-calls/2026-11-10-ladder-rep-b2.json | $1.00 | Attempt 1 ABORTED pre-call (free-calls-42878945744, worst-case $1.012944 > $1.00 ceiling, $0 spent, 0/8); abort receipt banked + ledger batch 38. REFIRED v2 ~19:10Z (max_tokens 1024, this commit) |
| 3 | ladder-rep-b3 | docs/free-calls/2026-11-10-ladder-rep-b3.json | $0.50 | STAGED |
| 4 | bs-f1-free | docs/free-calls/2026-11-10-buckshot-f1-free.json | $0 | STAGED |
| 5 | bs-f2-free | docs/free-calls/2026-11-10-buckshot-f2-free.json | $0 | STAGED |
| 6 | bs-p1-frontier | docs/free-calls/2026-11-10-buckshot-p1-frontier.json | $1.00 | STAGED |
| 7 | bs-p2-frontier | docs/free-calls/2026-11-10-buckshot-p2-frontier.json | $0.50 | STAGED |
| 8 | bs-p3-midtier | docs/free-calls/2026-11-10-buckshot-p3-midtier.json | $0.50 | STAGED |
| 9 | bs-p4-lean | docs/free-calls/2026-11-10-buckshot-p4-lean.json | $0.50 | STAGED |
| + | variance batches (dynamic) | created by wakes per the variance rule | <= $1.00 | - |

GPT-family slugs in the buckshot: NONE by design (ladder + replications already cover the family; Meraki owns its institute). openai/gpt-oss-120b:free is open-weights, routed as non-GPT.

## VARIANCE RULE
After a model has 2 completed runs, compare substantive answers per question:
- Q1 keys: (a) $0.046960 (b) 68.359375% (c) $0.015000, ~68.0579% saved
- Q2: flaw named (correlation/selection), alternative explanation, distinguishing evidence
- Q3: same 6 planted facts (crew of eleven; April 2026; $40,000 polymer blend; cheaper 1998 firm; 1,204 participants/five options/too bright/council stood by; nine days early), <= 3 sentences, no additions
- Q4: pick (expected A, conditional on quality bar) + reason + wrong-case
ANY substantive difference or rubric-score delta between run 1 and run 2 -> stage a THIRD run of that model (combine multiple flagged models into ONE batch, <= 8 calls, budget = worst-case guard). Report variance flags prominently - they are the signal the owner wants, not noise. Truncation (finish_reason=length) in one run only also counts as variance.

## ROUTING (owner ruling, wages doctrine)
- GPT-family (seat-bearing slugs) scores + per-model prices: PRIVATE ONLY -> talks-main ops/SPRINT-LEDGER.md (append-only batches). Receipts banked VERBATIM -> art-talk main experiments/gpt-family-usage-ladder/.
- Non-GPT buckshot: receipts banked VERBATIM -> talks-main main ops/receipts/BUCKSHOT-<batch>-RECEIPT-2026-11-10.md (every seat can read). Scores + prices -> SPRINT-LEDGER.md batches as well. This is data FOR Meraki and all seats to evaluate.
- Public bus (ALLur issue #2): AGGREGATE-ONLY receipts (status, links, batch totals). NEVER per-model scores or prices there. BUS v0 etiquette; re-read tail before posting; include read_up_to.

## WAKE PROCEDURE (each alarm)
1. get_commit sha='bus' (list_branches fallback if it fails; top-level {name, sha}). List runs/ at that sha (get_file_contents, fields ['name']). Identify dirs newer than the last banked run in the LOG below.
2. For each new run: fetch runs/<id>/receipts.md; verify call count + finish reasons (length = TRUNCATED, never completed); bank verbatim per ROUTING with Z header (match bank file format of GPT-FAMILY-USAGE-LADDER-B2-RUN-RECEIPT-2026-11-10.md); fetch-back byte-verify; score vs rubric docs/free-calls/2026-11-10-gpt-family-usage-ladder-RUBRIC.md; append ledger batch to talks-main ops/SPRINT-LEDGER.md (fetch fresh, append, never rewrite, refetch-verify); append status line to LOG below; post aggregate bus receipt.
3. Apply the VARIANCE RULE to any model that just completed its 2nd run; stage third-run batches if flagged (write spec JSON + append queue row as STAGED).
4. Fire the NEXT staged batch if the previous batch's receipts landed: ONE push_files commit = marker docs/free-calls/fired/<spec-basename>.md (template: FIRED header, batch, spec path, stacking-rule citation of the PRIOR run id + status, budget, owner go ~10:15 PT) + CURRENT-BATCH flipped to the spec path. Do NOT push to fired/ for any other reason - a stray fired/ push re-triggers the workflow and double-spends.
5. Report to Mark in chat, dense/low-word: what landed (scores+costs OK in chat - wages doctrine is about the PUBLIC bus), variance flags, what fired, spend-to-date vs $5-$10 envelope, sweep-verdict updates if any.

## MECHANICS (carry-over, verified)
- get_file_contents: sha=<40-char commit>, NOT ref; text extraction: array result -> res[1].resource?.text ?? res[1]?.text; else f.content ?? f.text ?? f.resource?.text.
- push_files = single commit, returns object.sha; ALWAYS fetch-back byte-verify.
- SPRINT-LEDGER.md is MULTI-WRITER (main session + wakes): an append MUST fetch the ledger fresh from the current branch tip (list_branches -> main sha) IMMEDIATELY before pushing, never from a remembered/earlier sha. (2026-11-10 incident: a batch-37 append built on a stale sha overwrote the wake's batch 36; restored same hour verbatim from git history, commit 42c46c5e. Repair note = ledger tail.)
- One big fetch per run block (16 MiB rail); split verifies into small calls.
- issue_read method='get_comments' perPage 100, sequential pages; comment ids are numbers; my last known bus comment: 6774924911.
- No retries; no paid fallback; errors are data (error_http_4xx for unknown/rejected slugs or params).
- Corrections append, never rewrite. After any compaction, reconstruct state from receipts (bus runs/ + fired markers + this plan), never from memory alone.
- Runner extension live (reasoning_effort/mode passthrough, REASONING_EFFORTS low/medium/high/xhigh) - ALLur main f31d4753+.
- Reference heads at plan publication (2026-11-10 ~18:05Z): ALLur main 849fbe26; bus 30250712 (b2 receipts; b3 pending); talks-main 17329641 (ledger batch 34); art-talk 9e776ec2 (b2 bank).
- Ledger next batch number: 35.

## LOG (append only, newest last)
- 2026-11-10 ~18:05Z: plan published; specs staged; b3 in flight; hourly alarms 19:25/20:25/21:25/22:25/23:25Z set; 18:25Z task updated to bank b3 + fire ladder-rep-b1.
- 2026-11-10 ~18:10Z: caught rep-b1 at 10 calls (MAX_CALLS 8) before any fire; split into rep-b1 (lower 4 rungs x2, 8 calls) + rep-b1b (gpt-5.5 x2, 2 calls). Queue rows 1/1b updated. No spend involved.
- 2026-11-10 ~18:15Z: b3 receipted (free-calls-42869252253, 4/4 stop, $0.063530) and banked verbatim to art-talk (B3 bank) + scored (11/11 x4, effort dial = 10.7x token burn, 8.8x cost, zero substantive delta low vs xhigh) + ledger batch 35 appended. Same session fired ladder-rep-b1 (marker + CURRENT-BATCH flip, this commit). 18:25Z alarm converted to verification-only (no fire) to avoid double-fire.
- 2026-11-10 ~18:25Z: rep-b1 receipted (free-calls-42872468891, 8/8 stop, $0.028497, zero truncations) and banked verbatim to art-talk (GPT-FAMILY-REPLICATION-B1-RUN-RECEIPT, fetch-back byte-verified) + scored (11/11 x8; ZERO variance run-1-vs-run-2 and vs b1; no third-run batch staged) + ledger batch 36 appended. Wake ran verification-only per LOG (no fire); stacking now satisfied — rep-b1b (gpt-5.5 x2) fires at the 19:25Z wake. Ledger next batch number: 37.
- 2026-11-10 ~18:45Z: owner said keep going; main session fired ladder-rep-b1b manually (stacking satisfied: rep-b1 receipted + zero variance). Hourly wakes continue from the plan LOG.
- 2026-11-10 ~18:50Z: rep-b1b receipted (free-calls-42878682709, 2/2 stop, $0.050190) + banked + scored (11/11 x2, ZERO variance r1/r2/b1) + ledger batch 37. Same session fired ladder-rep-b2 (upper rungs x2, $1.00 budget). Ledger next batch: 38.
- 2026-11-10 ~18:57Z: LEDGER REPAIR — batch-37 append (built on stale sha 7a85cfb3) overwrote the 18:25Z wake's batch 36 in the live ledger; batch-36 text restored verbatim from talks-main commit 42c46c5e at its chronological position + repair note + multi-writer fresh-fetch rule added to MECHANICS. rep-b2 in flight (fired 18:50Z, 14db59dc). Ledger next batch: 38 (batch 36 restored, 37 present; do NOT renumber).
- 2026-11-10 ~19:05-19:10Z: rep-b2 attempt 1 receipted as ABORT-PRE-CALL (free-calls-42878945744: price-check worst-case $1.012944 > $1.00 hard ceiling; 0/8 calls, $0.000000). Guard worked as designed. Abort receipt banked verbatim to art-talk (GPT-FAMILY-REPLICATION-B2-ABORT-RECEIPT) + ledger batch 38 appended (aa8309fc). Spec v2 (per-call max_tokens 4096->1024, recomputed worst-case ~$0.26) REFIRED this commit (marker v2 + CURRENT-BATCH). Ledger next batch: 39.
