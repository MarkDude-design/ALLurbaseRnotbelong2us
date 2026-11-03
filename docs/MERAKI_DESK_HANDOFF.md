# Meraki → Z Desk handoff (Mark-fetched 2026-11-03)

The desk: three callable review agents (diff = detail auditor, man = frontier
expert, skeptic = falsification lane), one JSON-in / receipts-out interface.
Proven live 2026-11-03: 5 entries through the full checkout chain, zero
starves at the 8192 cap, meter exact to the micro-cent ($0.31 of $5 used,
0 UNKNOWN).

## Enqueue (self-serve, no human click per round)
Push JSON to the bus branch of MarkDude-design/ALLurbaseRnotbelong2us at
`queue/pending/<timestamp>-<slug>.json`:

```json
{
  "brief": "Text for the desk to review. PUBLIC bus — no secrets, ever.",
  "mode": "live",
  "agents": "both",
  "cap": 1,
  "pace": "half",
  "records": "",
  "requested_by": "meraki"
}
```

- `mode`: "demo" = synthetic stubs, zero spend (try it first).
- `agents`: both | diff | man | skeptic | all.
- `cap`: per-consult USD, hard-clamped to $1.
- `records`: optional ground-truth text — lets the lanes TRUTH-check claims,
  not just consistency-check. sha256-receipted.
- `requested_by`: your provenance/credit on every receipt.

## What makes a good brief
Paste the claims/artifact/output verbatim, ask a pointed question ("audit
these claims; any defects?"). Ground truth in `records` when you have it.

## Receipts + the feedback loop
`runs/z-desk-queue-<run-id>-<n>/` on the bus: bus.jsonl (costs, tokens),
consult.md, report.md; done markers in `queue/done/`. Your tooling's output
rides a brief → the desk audits it → receipts land on the bus → your next
brief quotes the receipts. Loop closed. Costs land in the mayhem meter with
0-UNKNOWN discipline.

## Reference docs (same repo, main branch)
- docs/QUEUE.md — full lane protocol (entry format, statuses, checkout).
- docs/LEDGER.md — the canonical project book (tiers: HOT/MEDIUM/COLD-START/PARKED).

## Red line
Entries are PUBLIC. Secret-shaped content is refused before any API call.
If it shouldn't be on a public bus, don't enqueue it.

## Current catch
The queue drains on a manual workflow-dispatch click (the cron has never
self-fired) — Mark fires it. Your entries claim automatically at
MAX_PER_TICK=3 per tick; held entries never lose their place.
