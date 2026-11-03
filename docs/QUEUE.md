# Z Desk Queue — self-serve consult protocol

Owner-approved 2026-11-02 ("make this into tooling you can do yourself").
The queue lets Z (or the owner) request consults without a human click per
round: enqueue an entry, GitHub's cron (`*/10 * * * *`, workflow
`z-desk-queue.yml`) drains it, receipts auto-publish to the bus branch, and
the entry moves to `queue/done/` with a status marker.

## Entry format

File: `queue/pending/<timestamp>-<slug>.json` on the **bus branch**
(example: `queue/pending/2026-11-03T0410Z-t4-scale-1.json`).

```json
{
  "brief": "Text for the desk to review. PUBLIC bus: no secrets, ever.",
  "mode": "demo",
  "agents": "both",
  "cap": 1,
  "pace": "half",
  "records": "",
  "diff_model": "mistralai/mistral-medium-3-5",
  "man_model": "openai/gpt-6-sol",
  "requested_by": "Z"
}
```

Fields:

- `brief` (required) — reviewed text. Secret-shaped content is refused
  before any API call (same red-line as the manual lane).
- `mode` — `demo` (default; synthetic stub, zero spend) or `live`
  (real model calls; funded per Mark's GAS standing order, Oct 2026).
- `agents` — `both` (default), `diff`, or `man`.
- `cap` — per-consult local budget ceiling USD. **Hard-clamped to
  QUEUE_CAP_USD ($1) regardless of what the entry asks.** The provider key
  cap still governs overall.
- `pace` — `half` (default; 50% syscall speed cut per Mark's Oct 25 dialing
  order) or `off`.
- `records` — optional ground-truth text for a truth-audit; rides both agent
  prompts as authoritative and is sha256-receipted in the run's start event.
- `requested_by` — provenance: who enqueued (receipt credit).

## Processing

- Every 10 minutes the workflow runs the full test suite first, then drains
  up to `MAX_PER_TICK` (3) oldest `queue/pending/` entries.
- Per entry it runs the same `island.z_desk` consult as the manual lane
  (`.github/workflows/z-desk.yml`), so receipts land in
  `runs/z-desk-queue-<run-id>-<n>/` on the bus: `bus.jsonl`, `consult.md`,
  `report.md`.
- The entry is then removed from `queue/pending/` and a status marker is
  written to `queue/done/<ts>-<n>.json` with
  `status` ∈ `completed | error | parse-error`.
- A failed entry is receipted and does not block the rest of the tick; a
  `parse-error` entry is moved to done without running.

## Kill switch

Disable the `z-desk-queue.yml` schedule (owner's click in the Actions UI).
Pending entries then simply hold; nothing runs until it is re-enabled or a
human fires a manual tick via workflow_dispatch.

## Who may enqueue

Anyone with push access to the bus branch: Z (via the GitHub app) and Mark.
Entries are PUBLIC — the red-line scan refuses secrets before any call.
