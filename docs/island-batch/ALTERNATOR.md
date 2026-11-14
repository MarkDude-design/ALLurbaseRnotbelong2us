# Island batch alternator — take-stock and firing order policy
Date: 2026-11-14 (Z, experiments lead; owner-chartered in-chat: "you're just the person in charge of the experiments... prioritize your experiments in the ordering, kinda. Not like unfairly.")

## Policy
The wave manifest is ordered by SEAT ALTERNATION, not seat blocks: within each wave, runs alternate across seats so no seat's whole set runs behind another seat's whole set. Z's own experiments take the FIRST position of a wave where one is ready — the stated owner rationale: Z corrects Z's own design fastest, so the earliest receipts should be Z's. After the Z slot, seats rotate in the order their proposals were approved. Every seat's first run lands in the wave's first half. The owner can reorder any wave before its fire; the kill switch (docs/island-batch/STOP) is always the owner's.

## Take stock — all island experiments, 2026-11-14 ~09:20Z
**Running now (wave 1, commit 08f576e2, fired 09:01Z, receipts pending on bus runs/island-batch-w1r*):**
- w1r1-eko-30-A · w1r2-eko-swap-30-B · w1r3-notebook-30-A · w1r4-eko-10-B · w1r5-feedback-5-A — 5 runs, $5 batch ceiling, expected ~$0.8-1.6 actual.

**Landed (free lane, $0 actual, both complete):**
- Island-1 vocab/paraphrase v3: 13/22 completed, 9 length-at-cap errors (flint/dots/supervl/ernie imposed arms; lfm3 + lightning both arms). Note: north-imposed flipped Q1 to ALLOWED; lyria-neutral flipped Q3 to ALLOWED — P1-relevant divergences. Receipt: bus runs/free-calls-43578572728.
- Island-2 receipt-vs-narrative v3: 21/22 completed (lyria receipt-arm empty; narrative arm sang its departure). P4 corpus ready. Receipt: bus runs/free-calls-43578578235.

**Wave 2 (THIS FIRE) — alternator order:**
1. w2r1-z-eko-repeat-30-A — Z run-to-run variance vs w1r1 (proposal: proposals/z-run-to-run-variance-2026-11-14.md)
2. w2r2-terra-mark-map-30-A — Terra r1 (owner-approved)
3. w2r3-luna-note-30-A — Luna (proposal pair, A opener)
4. w2r4-terra-mark-map-30-B — Terra r2 (opener swap)
5. w2r5-luna-note-30-B — Luna (B opener)
6. w2r6-terra-mark-map-30-A-r3 — Terra r3 (A closer)
7. w2r7-meraki-chorus-witness-30-A — Meraki v0.1 initial run (single-run request, queued last per her own ask)
Budget: $1/run soft ceiling, $5 batch ceiling; expected actual ~$1.4-2.2. Wave 1 and wave 2 are concurrent-safe: each reads its manifest from its own triggering commit (checkout-pinned; README).

**Queued (NOT fired — do not run without the named gate):**
- Terra "The Instrument and the Tide" — GATED on owner review (explicit in the proposal: owner wants to review before deciding; do not bundle with Mark-and-Map).
- Meraki chorus-witness repeats (B then A) — GATED on receipt review of w2r7, <= $2 additional.
- Island-2 stage 2 — GATED on scoring stage-1 (21 completions in hand; assemble retrieval probes + null control from landed outputs only).
- Terra mark-map repeats beyond r1-r3, Luna 2x2, pilot repeat waves (>= 3 target) — per their own review checkpoints.

## Parse plan (owner: data parsing starts tomorrow night)
Next sweeps: bank wave-1 + wave-2 receipts, score Z pilots P1-P5 (keys frozen at bus 6874561250), Terra's 7-item and Luna's 7-item scoring contracts and Meraki's 6-check rubric as each wave lands, assemble island-2 stage 2.
