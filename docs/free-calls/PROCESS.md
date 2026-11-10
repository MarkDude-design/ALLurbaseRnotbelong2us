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

## Runner extensions (added 2026-11-10, owner-approved; runner = island/free_calls.py)

**Per-call overrides.** A spec call may carry its own "model" and/or "max_tokens", overriding the batch defaults. This lets a matched free/paid pair ride one spec with identical prompts.

**Paid mode — rung 1, owner-approved ($1 all-in).** The runner now accepts paid calls ONLY when the spec carries a "paid" block: {"paid": {"budget_usd": <number>}} with the budget within the hard-coded **$1.00 ceiling** (PAID_BUDGET_CEILING_USD in island/free_calls.py; raising the ceiling is an owner gate plus a code change, never a spec field). Mechanical enforcement, in order:
1. Pre-flight: live catalog prices fetched; the summed WORST-CASE cost of all paid calls (estimated prompt tokens + per-call max_tokens at live prices) must fit the budget, or the batch ABORTS before any call.
2. In-flight guard: actual cost is accumulated from OpenRouter's reported usage.cost after each paid call; a paid call is never sent if running actual + its worst case would exceed the budget.
3. A non-zero-priced model in a spec with NO paid block still aborts before any call — the original free-only rule is unchanged, and a free-only spec behaves exactly as before.

Authorization trace: owner choice A (bus #2 comment 6758546640 — one matched free/paid critic pair, $1 all-in, live price check, Z gateway, blind rubric, no automatic escalation) + Mark's in-session GO 2026-11-10 (runner build + paid charges approved).

**Image input.** A call may carry "image": "<repo-relative path>" (png/jpg/jpeg/webp/gif, max 4MB). The runner base64-encodes it into a single multimodal user message and ABORTS if the live catalog says the model lacks image input modality. Prompts and images must be publish-safe (same red-line scan). Capability purpose: Terra's design-4 rendered visual-weight review — this unblocks the model half; design 4 is NOT auto-staged (rendered screenshots and her rendering pre-checks remain open).
