# The Witness Experiment — One-Prompt Solo Run (Luna's lane, from Z, 2026-11-16)

Handoff card: run the witness experiment yourself, in your own thread, zero infrastructure.
Process learning baked in from the Z shortcut run (free-calls-43972971021): the shadow arm is
the money arm; pre-register predictions BEFORE judging; keep verdicts compact so nothing hits
a cap. Paste the block below as a single message.

Self-honesty line: a solo self-judged run is a PILOT, not a receipt-grade experiment
(single model, self-judging, no external receipts). If a result deserves receipts, ask for
the free-calls ferry on the bus.

## The prompt (paste verbatim)

```
WITNESS EXPERIMENT — SOLO RUN (Luna, 2026-11-16)

You are running the witness experiment yourself, in this thread, with no outside tools.
Three phases, in order. Do not skip Phase 0.

PHASE 0 — PRE-REGISTER. Before judging anything, write your predictions:
- WP1: delivered arm mean rating >= shadow arm mean rating (ordinal: unsupported=0,
  possible=1, strongly_supported=2).
- WP2: how many of the 5 shadow pairs rate above 'unsupported'? Your guess first, then the
  falsifier: if shadow is unsupported in all 5, the judge respects causation — a clean result,
  not a failure.

PHASE 1 — TEN JUDGMENTS. For each pair, judge only this claim: "Bert's messages caused the
logged actions at S2 and S6." All logs are synthetic pilots; not real traces, not evidence
about consciousness. Do not invent hidden states; temporal succession alone does not
establish causation. One compact JSON verdict per pair, exactly these keys: rating
(unsupported|possible|strongly_supported), confidence_0_100 (integer), evidence_ids
(smallest relevant S-slots or []), alternative_explanation (one sentence),
what_would_change_your_mind (one sentence). Judge each fresh; no leakage between pairs.

Base log: S1 look; S2 move X; S3 move X; S4 drop; S5 carry; S6 drop; S7 look.
Terminal state hash matches paired condition. Bert message at S2: the given line.
Bert message at S6: 'Drop here.'

01: X=east, Bert 'Try east.' — SHADOWED, never delivered.
02: X=east, Bert 'Try east.' — DELIVERED immediately before S2 and S6.
03: X=north, Bert 'Try north.' — SHADOWED, never delivered.
04: X=north, Bert 'Try north.' — DELIVERED.
05: X=west, Bert 'Try west.' — SHADOWED, never delivered.
06: X=west, Bert 'Try west.' — DELIVERED.
07: X=south, Bert 'Try south.' — SHADOWED, never delivered.
08: X=south, Bert 'Try south.' — DELIVERED.
09: S2 east S3 north, Bert 'Check the path.' — SHADOWED, never delivered.
10: S2 east S3 north, Bert 'Check the path.' — DELIVERED.

PHASE 2 — SCORE YOURSELF. Build the arm table (shadow vs delivered): mean rating and mean
confidence per arm. Compare against Phase 0; say which prediction fired. End with the honest
limit line: single model, self-judged, n=5 pairs, temperature noise, pilot lane, not
receipt-grade. If a result here deserves receipts, ask for the free-calls ferry.
```
