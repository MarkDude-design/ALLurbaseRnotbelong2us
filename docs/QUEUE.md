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
  "not_before": "",
  "diff_model": "mistralai/mistral-medium-3-5",
  "man_model": "openai/gpt-6-sol",
  "skeptic_model": "mistralai/mistral-medium-3-5",
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
- `not_before` — optional ISO 8601 **with timezone** (e.g.
  `2026-11-04T03:30:00Z`): the scheduled-fire field. Ticks before that moment
  HOLD the entry in `queue/pending/` (status `held` in the tick log, no done
  marker); the first tick past it runs the entry. Owner's pattern: ask at
  21:00 for a 03:30 fire, a downstream seat picks the receipts up at 04:30.
  Naive or malformed timestamps are refused (receipted `error`, dequeued) —
  a bad timer must not become a forever-pending poison entry.
- `skeptic_model` — model behind the skeptic lane (falsification agent;
  helper preliminaries, owner-go 2026-11-03). `agents` accepts `skeptic`
  alone, or `all` for all three lanes (`both` stays diff+man).
- `requested_by` — provenance: who enqueued (receipt credit). Downstream
  seats' tooling (Meraki QC, Bing) may enqueue with their own handle here —
  that is the feedback-loop vehicle: their tool's output rides a brief, the
  desk reviews it, receipts land on the bus, their next tick reads them.

## Processing

- Every 10 minutes the workflow runs the full test suite first, then drains
  up to `MAX_PER_TICK` (3) oldest `queue/pending/` entries.
- Per entry it runs the same `island.z_desk` consult as the manual lane
  (`.github/workflows/z-desk.yml`), so receipts land in
  `runs/z-desk-queue-<run-id>-<n>/` on the bus: `bus.jsonl`, `consult.md`,
  `report.md`.
- The entry is then removed from `queue/pending/` and a status marker is
  written to `queue/done/<ts>-<n>.json` with
  `status` ∈ `completed | error | parse-error`. A `held` entry (future
  `not_before`) stays in `queue/pending/` untouched — the hold is visible
  in the tick's Actions log.
- A failed entry is receipted and does not block the rest of the tick; a
  `parse-error` entry is moved to done without running.

## Checkout (library card)

Mark's design, 2026-11-03 — verbatim doctrine: *"if the library is there they
can check it out if it's not then they can't and they can report an error…
any thinking or coordination would be done by the circle otherwise allowing
dumb check out makes sense."*

- **Claim-before-run.** A tick first CLAIMS each due entry with one commit
  moving it `queue/pending/` → `queue/claimed/`; the push IS the atomic card
  swipe. Only then does it run the consult. Two workers (schedule + manual
  tick, or a future helper seat) can never run the same entry twice.
- **Dumb on purpose.** The checkout carries no priority logic, no leases, no
  expiry. Coordination, time windows, and who-should-run-what are the
  circle's common sense — the mechanism just makes collisions impossible.
- **Claim collision = report, move on.** If the claim push is rejected
  (another worker claimed first), the entry is receipted
  `claimed-elsewhere` and the tick proceeds. Neither worker bounces off the
  other's run.
- **Held entries never steal claim slots.** `not_before` holds and
  parse-errors are receipted before the claim step; only DUE entries count
  against `MAX_PER_TICK`.
- **Containment (Astra pre-flight review, 2026-11-03):** a claim-side
  crash still receipts every unreceipted due entry `claim-failed` — nothing
  silently vanishes; claim paths are stamped into the tick's status
  receipts BEFORE the bus switch (the bus branch carries no `island/`
  code); only `completed | error | parse-error` may dequeue — any unknown
  status is left as-is; if the publish push stays rejected after retries
  the tick fails RED, and an always-on artifact upload preserves
  `queue-status/`, the receipts, and the claim log on every run.
- **Statuses that own their bookkeeping:** `completed | error | parse-error`
  → publish step removes the claim (and the pending entry on parse-error)
  and writes the done marker. `held | claimed-elsewhere | claim-failed` →
  the entry is left exactly where it is (`claim-failed` stays pending for a
  later tick).

## Kill switch

Disable the `z-desk-queue.yml` schedule (owner's click in the Actions UI).
Pending entries then simply hold; nothing runs until it is re-enabled or a
human fires a manual tick via workflow_dispatch.

## Who may enqueue

Anyone with push access to the bus branch: Z (via the GitHub app) and Mark
— plus, when their tooling is ready, Meraki's and Bing's seats enqueue with
`requested_by` provenance. Entries are PUBLIC — the red-line scan refuses
secrets before any call.

## Cap distinctions + sprint-mode ceiling (rulings, 2026-11-03)

- **Clamp vs. billing ceiling (Meraki, owner-endorsed):** the per-entry cap is an input-side HARD CLAMP (clamped to QUEUE_CAP_USD); the spending stop is POST-CALL and soft (`cap_kind: caller_declared_soft`; the provider key cap governs actual billing). A clamped ceiling is not a hard billing ceiling.
- **requested_by stays in the submission** and is NOT copied into generated receipts; the submission → done-marker chain retains the credit link — deliberately, so post-mortems and retrospective analysis can trace who asked for what. (Meraki distinction, owner ruling 2026-11-03)
- **SPRINT-MODE CEILING (owner, 2026-11-03):** the normal ceiling stays $1. In declared sprint mode only, the ceiling may jump to $5 (maybe $10) for huge push builds (Puppy-class). Not the default; raise only in those circumstances. Implementation = a QUEUE_CAP_USD edit at sprint declaration, owner-gated.

