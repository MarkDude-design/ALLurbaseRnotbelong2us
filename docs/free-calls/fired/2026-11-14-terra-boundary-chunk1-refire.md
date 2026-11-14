# Route B fire marker - 2026-11-14 Terra boundary chunk 1 RE-FIRE (receipt reconciliation)

The original boundary chunk 1 fire (commit 2c4dd136, ~09:58Z Nov 14) never published a run receipt to the bus branch: no runs/free-calls-* dir, while the observation chunk (6655ffffc -> runs/free-calls-43582762570, 6/6 $0) and centering chunk (c42807bb -> runs/free-calls-43582781227, 6/6 $0) fired minutes before/after both landed. Hypotheses: workflow publish race during three concurrent runs (3x retry/rebase exhausted; artifact retained 30 days on the original run) or a pre-call gate abort whose receipt also failed to publish. The spec is UNCHANGED: docs/free-calls/2026-11-14-terra-boundary-chunk1.json, first 6 of Terra's pinned 54 (ultra, inside/out/in x A/B, r1).

HONEST DUPLICATE RISK: if the original run's calls executed, this re-fire produces a second fresh-instance set of the same 6 probes. Free-only, $0; fresh instances are additional repeats for Terra's 3-repeat design, not contamination. Marked re-fire so the pair is legible in scoring. If this receipt also fails to land, escalate publish-path debugging before further free-calls fires.

Owner GO chain: owner-directed Terra pilots (bus 6875389950, 6875470155) + standing free-fire authorization.
