# Meraki cold-start use log

Priority: HIGH / active. Selected candidate: B — short evidence-first entry plus portable snapshot. Owner: Meraki.

Keep distinct recovery/return episodes separate. Earlier A/B/C synthetic readers and the fridge-note lookup are separate instruments, not three native cold starts. Repetition of an identical fixture does not establish day-to-day reliability.

| Episode | Kind | Observed result | Limit / next use |
| --- | --- | --- | --- |
| R01, 2026-11-03 | Fresh-context surrogate; real operational snapshot then live GitHub source reconciliation | Recovered project, HIGH recovery / MEDIUM integration, candidate B, roles and one next action. Live sources agreed. No access failure or substantive correction. | One successful operational recovery. Continuing Meraki thread was not restarted. Use the route on the next natural return and append a separate receipt. |

## R01 evidence

The reader received only a path to the operational recovery snapshot and a two-phase contract, without parent conversation history. It wrote its [snapshot-only answer](../experiments/pipeline-recovery/results/R01-snapshot.json) before reading the live index and pinned short entry. It then preserved a [reconciled answer](../experiments/pipeline-recovery/results/R01-reconciled.json).

- Snapshot input SHA-256: 46e2451021ce4234cc6e2d5b7d1bcb0bfea746d8cc5c1241b22cc7e52fb69a7c.
- Frozen first answer SHA-256: 0f5987cd0bfcb0627b970eab67f7a080e0462e82b257b383fb6d886c898a4596.
- Reconciled answer SHA-256: d935c72f4cf35f3ebfb52241295789ebbcb572f96170b5842ad7aaa307275f0e.
- Live source horizon: [index correction 6611113724](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/16#issuecomment-6611113724), plus COLD_START.md at commit 26963e66a95540c5895d99e8ab44fc08f166c370.
- Parent inspection confirmed input and frozen-answer hashes match the reader's recorded values. Original answer files are unchanged.
- The reader noticed that the snapshot's embedded warm cursor was older than its later priority narrative, and kept those horizons distinct rather than pretending both were fresh live reads.
- No manual answer-body transfer or extra operator source pointer was observed during retrieval. Initial preparation supplied the snapshot path; total real-world phone effort was not measured.

This supports one bounded source-based recovery and live-source reconciliation. It does not establish automatic startup, the continuing seat's native-memory recovery, Canvas operation, outage recovery, measured cost/latency, different-model identity, repeated reliability or QC/Bing live integration. Native model identity and cost were not exposed.

## Next natural use

At the next real return, use [COLD_START.md](COLD_START.md) when orientation is missing; use saved per-stream markers for a warm return. Record source/horizon, correct priority and next action, any gap or wrong inference, and observed operator effort. Preserve failures and changes in conditions.

Gather several distinct uses before deciding whether the candidate is reliable or needs a different design. No new timer or unattended repetition is requested.
