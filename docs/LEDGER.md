# THE LEDGER — Z Desk project

One canonical book per project. "Ledger" means THIS file and nothing else:
the Bus is the receipts journal, the Meter is the spend book — they keep
their names, never "ledger." Naming ruling: Mark + Z, 2026-11-03.

## How to read it
- "What do we have on the ledger?" → this file, top to bottom.
- Tiers: **HOT** (this crunch, green-lit) / **MEDIUM** (next cycles) /
  **COLD-START** (self-contained, no blockers, pick up in slow times) /
  **PARKED** (design-only, awaiting owner specifics).
- One line per item: owner, status, pointer to the real artifact.
- Dual bookkeeping rule (Mark, 2026-11-03): desk work is banked in the
  pipeline continuity record (z-desk knowledge) AND gets one line here.
  Appendices get fine-tuned later, changed only on real roadblocks
  (develop-and-react model — same as the style guide, same as Meraki's
  best-practices post).

## HOT
- [ ] Trigger lane: repository_dispatch on the queue workflow → email
      processor → red-line gate before the public bus (Mark's Europe-mode:
      any device, any mailbox, safe code phrase, job-run threat model —
      "we'll build all those rules," green-lit 2026-11-03). Owner: Z.

## MEDIUM
- [ ] Cron re-register test: disable → enable toggle on "Z Desk — Queue"
      (one click, observational — does a scheduled run ever self-fire?).
      Owner: Mark.
- [ ] Meraki's best-practices post: read, fine-tune as appendix (neither
      Mark nor Z has read it yet; location TBD). Owner: Z.
- [ ] Cell cold-start: per-turn mirror rebuild costs ~6 fetch batches;
      candidate = cached rebuild script. Owner: Z.

## COLD-START
- [ ] z-desk.yml parity: publish-retry exhaustion still echo-only there
      (exit-1 + always-artifact was only added to the queue workflow).
      Owner: Z.
- [ ] Style guide fine-tuning pass (appendix model; change later unless
      roadblock). Owner: Z.

## PARKED
- [ ] Bulk-cheap lane: gpt-6-luna (~300x cheaper than sol; real pricing
      in hand) — awaiting Mark's speed/cost specifics. Owner: Z.
- [ ] Local-host variant: headless runner on own hardware (island is
      stdlib-only; bus could be a bare repo on the box). Owner: open.

## Done (kept one entry deep, newest on top)
- [x] 2026-11-03 — T4 scale round + skeptic-prelim: 3/3 + 1 fires, zero
      starves, desk READY. Wall read: $0.31 of $5 (6.2%), 0 UNKNOWN.
