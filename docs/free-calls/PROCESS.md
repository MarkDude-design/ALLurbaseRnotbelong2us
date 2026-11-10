# FREE-CALL BATCHES — formalized seat process (owner-directed 2026-11-09)

One lane, two fire routes, Z-gated. Written for any seat that wants a batch of raw free-model calls.

## How a seat requests a batch

1. Post the exact batch spec on the bus (or a spec file on your own branch, linked on the bus): each call prompt VERBATIM (the words are yours — Z never edits them), the target model, output-token cap (default 450), stop rules, your predeclared scoring refs, and your private receipt destination.
2. Free-tier models only for this lane (":free" variants, expected $0). Paid calls are a DIFFERENT lane — the owner ladder, ask Z.

## What Z checks before staging (the gate is Z review, mechanically enforced)

- Model is a ":free" variant and the runner re-verifies $0 prompt + $0 completion in the LIVE catalog immediately before sending — if the price ever stops being $0, the batch aborts without sending (in code, not memory).
- Prompts pass the public-bus secret-shape scan; nothing private rides the bus.
- Caps are sane; no system prompt, no tools/web, no retries, no paid fallback; single user message per call; sequential, recorded not hidden.

## How it fires

- Z stages the batch JSON at docs/free-calls/<batch>.json and points docs/free-calls/CURRENT-BATCH at it.
- Route A (owner click): Actions tab → "Z Desk — Free Calls (batched)" → Run workflow (empty input runs CURRENT-BATCH). The spend gate stays the owner's.
- Route B (Z-gated push, owner-directed 2026-11-09): Z pushes a marker file under docs/free-calls/fired/ — that push IS Z's approval and the fire signal. Same spec spine, same checks.
- Kill switch (owner, always): disable the workflow; the lane holds.

## Receipts + scoring

- Receipts publish to the bus branch (runs/free-calls-<run_id>/) + a 30-day artifact; Z banks them verbatim to each seat's private destination.
- The seat scores per its own predeclared rules; Z makes no scoring calls. Errors, empty responses, and rate-limits are recorded as data, never hidden.

## Daily gateway sweep (Z) — born 2026-11-10, owner automation direction

Every day at 9:00 AM PT, a Z sweep runs: specs posted to the bus since the last sweep are reviewed and, if they pass the standing checks, staged and fired the same morning (Route B); landed receipts get banked to seat destinations and receipted on the bus. Seats who post a spec before 9 AM PT can expect same-day fire; anything later rides the next sweep. Between sweeps, the owner's click (Route A) and in-session Z firing both remain available. Kill switch unchanged: disable the workflow and the lane holds.
