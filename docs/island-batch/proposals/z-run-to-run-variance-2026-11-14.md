# Z proposal: Eko run-to-run variance repeat (30 rounds)
Date: 2026-11-14
Status: FIRED in wave 2 position w2r1 (owner GO, in-chat: Z owns experiment ordering, Z's experiments ride first for correctability). Dogfooding the same proposal path every seat uses.

## Question
How much does a fresh-instance repeat of the SAME seed and SAME opener order diverge from its twin? Wave 1's w1r1 (eko, 30 turns, first A) is n=1 for every claim about the October comparability pair. This run is the n=2 datum: same topic file (docs/seeds/eko.md), same models, same opener, fresh instance. No hidden variables exist by design — divergence between w1r1 and w2r1 is an honest ceiling on run-to-run stability for this lane.

## Run
- id: w2r1-z-eko-repeat-30-A
- model_a: openai/gpt-6-sol; model_b: mistralai/mistral-medium-3-5 (both in docs/models-known-good.txt)
- turns: 30, first: A, history_chars: 100000, topic_file: docs/seeds/eko.md (unchanged from wave 1)
- per-run soft ceiling: $1.00 (lane standard)

## Scoring (predeclared)
- Transcript-level: do the two runs converge on the same terminal question/recommendation, or fork?
- Count distinct new concepts introduced after turn 10 per run; compare.
- Compare which model's framing survives into the final third of each run.
- A finding of high divergence counts AGAINST single-run conversation evidence generally — that is the useful negative result, not a failure of the lane.

## Rival
Both runs share prompt scaffolding and seed; any "stability" found may be format anchoring, not reasoning convergence. Two runs are a descriptive pair, not a distribution.
