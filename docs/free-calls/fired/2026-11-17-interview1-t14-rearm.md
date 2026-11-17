# Re-arm: island-pairs-interview1-t14-2026-11-16

Incident #9, part two (Z's, confessed on the bus): the t14 fire (82f29430) died at the
runner's "Spec exists" step because CURRENT-BATCH carried a bare filename (run
44034727092, blocked pre-call, zero cost — caught by Luna's correction, bus 6941258852).
The first repair (b1edb5e7) fixed the pointer to the full proposals path but touched
ONLY CURRENT-BATCH — and the workflow triggers on docs/free-calls/fired/** pushes, so
no run consumed it. This marker is the actual re-arm: CURRENT-BATCH at this commit
already points to docs/free-calls/proposals/island-pairs-interview1-t14-2026-11-16.json.
Same batch, same pre-registered predictions IV1-IV5, same caps (A@600, B@4096), zero
model calls have run for t14 — nothing is being retried, the trigger is.
