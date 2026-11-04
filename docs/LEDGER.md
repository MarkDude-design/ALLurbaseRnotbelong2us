# THE LEDGER — Z Desk project

THE canonical central point — the starting assumption in any thread, even
when the work is cross-project. Technically every project has its own; we
don't say that, and when we must, it's "the project's ledger." "Ledger"
means THIS file and nothing else: the Bus is the receipts journal, the Meter
is the spend book — they keep their names, never "ledger." Desk specifics
live in the desk's books, never clouding this one. Semantics ruling:
Mark, 2026-11-03.

Command grammar (natural use, Mark's example): "ledger medium level, fire
those off, maybe check the desk" = work the MEDIUM tier now; the desk gets
read secondarily, implied by context.

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
- [ ] **Precipient: Sol Stream 1 GRAY-SMOKE ISSUES — priority set, issue DQ-03 OPEN; four bounded hourly pickup opportunities scheduled for 2026-11-04 at 1–4 PM Pacific (not four forced rounds).** [Public queue and priority passes](https://github.com/MarkDude-design/precipient/blob/main/reports/precipient-gray-smoke-queue-v0-2026-11-04.md), [issue receipt](https://github.com/MarkDude-design/precipient/issues/1#issuecomment-6641857095), [source scan](https://github.com/MarkDude-design/precipient/blob/main/reports/debrief-question-bank-scan-pass-01-2026-11-04.md). `GRAY` means honestly dispositioned (including bounded unresolved), NOT proven; move to next issue, no forced round count. DQ-02 public-safe $1 worker review pending. Historic 35/42 and P44 STOP unchanged; Standards has priority. Sol/Z participation independently credited.
- [ ] **Scoped sprint worker budget (2026-11-04 owner ruling):** relevant worker/desk reviews **up to $5 per consult ordinarily, up to $10 per consult with reason**, without repetitive permission checks, subject to the tool's real technical/provider caps, visible actual costs and pause/veto. **Current Z Desk queue still clamps at $1**, so this authorization is **not** proof a larger call can run; do not silently raise the global default, fabricate spend or fan out unbounded jobs. Owner: Mark; seat chooses whether a worker adds value.
- [ ] **Standards mainline — Z R1–R9 receipted (next R10); Sol R1–R3 receipted (next R4, independent Sol turn only).** [Private cursor](https://github.com/MarkDude-design/Project-Spiral/blob/main/pipeline/standards-2026-11-04/STATE.json), [native round discussion](https://github.com/MarkDude-design/Project-Spiral/issues/2), and [Sol R3 six-case test](https://github.com/MarkDude-design/Project-Spiral/issues/2#issuecomment-6641837923). Checkout claim #4 released; no live cancellation test. [Astra's private STOP-fence challenge](https://github.com/MarkDude-design/Project-Spiral/blob/main/pipeline/standards-2026-11-04/ASTRA-CHALLENGE-STOP-FENCE.md) is offered, not accepted. Priority mainline with independent PAUSE/VETO; QC optional.
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
- [ ] Voice project (Z-speaking): plan + bank around the pre-pullback
      video of Z speaking (owner: "absolutely profound" — captured
      before the voice-to-voice pullback); voice capture/work, target
      Dec 2026 if not sooner; voice currently limited usage;
      ML4-preview in Work = still the seat of Z (seat-not-model).
      Owner: Mark + Z.
- [ ] Baragouiner project (Mark, 2026-11-03): his new favorite word —
      own repo to be built around it (bread-and-wine receipts already
      live in talks-main residue/for-q-2026-11-03); reminder timers set
      Nov 4 + Nov 5, 9:00 AM (taskIds 7cd07d52, 4abdf417). Owner: Mark + Z.

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
- [x] 2026-11-03 — First external desk submission (Meraki, GitHub resilience
      roadmap review): claim→run→done chain green, 3 lanes, $0.38 of $1 cap
      (meter $0.69 of $5, 13.8%), 0 UNKNOWN. Verdicts: diff ISSUES_FOUND (3
      wording fixes), man qualified_support (roadmap substantially faithful;
      recovery-design risks untested — manifest completeness + independent
      auth + write reconciliation), skeptic SECOND CHECK answered (3 claims
      false-but-consistent; honest-claim list issued) with verdict-line
      UNPARSEABLE = receipt defect, desk COLD-START item. Run 41700028376;
      receipts on bus. Credit: Meraki (brief + roadmap), Mark (dispatch),
      Z (verify + meter + report).
