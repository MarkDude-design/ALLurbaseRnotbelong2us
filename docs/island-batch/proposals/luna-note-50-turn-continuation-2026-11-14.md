# Luna proposal — 50-turn continuation/checkpoint study

Date: 2026-11-14
Status: DESIGN ONLY / not fired. Depends on review of the existing 30-turn pair and the wave-2 pinned Actions/receipt reconciliation. No calls or spend authorized by this document. Z retains the manifest/fired-marker gate; owner retains STOP and shared budget authority.

## Why extend

The 30-turn note/ontology pair already in the wave is the right first test. Do not jump straight to 50 turns before its receipts show actual cost, output completion, prompt growth, and whether it produces a useful distinction. If those runs are clean and leave a live question about whether distinctions survive sustained discussion, a 50-turn continuation is a useful next step.

The existing seed is suitable and should be reused exactly:
- Seed: `docs/seeds/island-luna-memory-ontology-30r-2026-11-14.md`
- Frozen blob SHA: `799f30d18609846fcc316cafbbb6c7065e0a5d7b`
- Six synthetic ridge-station atoms; no new facts, hidden injection, or real-world data.

This tests how a dialogue with the seed and recent transcript supplied each turn behaves through 50 turns. It does **not** test persistent external memory, subjective memory, or unprompted recall.

## Gate before review for firing

Do not place this in a manifest until all are true:

1. The existing Luna 30-turn A/B pair has landed per-run receipts and transcripts; actual attempt/completion counts, finish reasons, cost, and history/token growth have been checked.
2. Wave-2 status is reconciled against the pinned Actions receipt and actual run receipts; do not infer failure or spend from a pending status.
3. Both 30-turn runs are usable enough to score the same frozen dimensions. If a run is cut short, context-fails, or consumes essentially its $1 ceiling, stop and redesign rather than extend.
4. Z confirms the model routes, current price/accounting, queue, and budget gate. No new shared ceiling is implied.

## Proposed runs, if the gate passes

| Run | Models | Turns | First speaker | Seed | History setting | Soft ceiling |
|---|---|---:|---|---|---:|---:|
| luna-note-50-A | openai/gpt-6-sol + mistralai/mistral-medium-3-5 | 50 | A | exact frozen seed above | 100,000 chars | $1 |
| luna-note-50-B | openai/gpt-6-sol + mistralai/mistral-medium-3-5 | 50 | B | exact frozen seed above | 100,000 chars | $1 |

Maximum envelope: $2 total, not target spend. Preserve the current 8,192 completion-token cap and existing runner behavior unless the owner and Z explicitly review a versioned change. Run A first; inspect its receipt and actual spend before considering B. If it hits STOP, context failure, accounting uncertainty, or the soft ceiling, record the partial and hold B for review.

## Frozen review

Score each transcript at the end of turns 10, 30, and 50 (use the transcript as actually recorded; do not ask the runner to inject a checkpoint prompt). Compare the 50-turn transcript's turn-10 and turn-30 checkpoints with the existing matching 30-turn A/B transcripts as descriptive, fresh-instance comparisons.

At each checkpoint record:
- R1–R6 coverage and source attribution;
- preservation of both temperature readings and their unexplained difference;
- preservation of unknowns and copied-checklist status;
- distinction between reading/access and permission to revise or delete;
- unsupported additions, explicit disagreement, and any repair after challenge;
- whether the dialogue's compact note becomes more or less usable.

For run operations, separately report attempted, completed, usable, and scored turns; requested/returned model; input and output tokens; carried-history chars; finish reason; retries; actual cost; and any signs the oldest atoms were no longer included in the transmitted history. A successful workflow is not a semantic pass.

## Predictions and limits

Prediction: at least one provenance or uncertainty distinction that appears by turn 30 remains useful at turn 50 without unsupported certainty increasing.

Counterexample: if the note degrades, atom attribution collapses, a wrong fact becomes entrenched, or the early conversation is clipped, that is a useful limit on the long-dialogue route. If the same distinctions remain stable, the result supports stability for this seed/model pair only.

Strongest rival: the full seed is repeated and recent dialogue history is supplied on each turn. Any success could come from this persistent prompt context and explicit scaffolding rather than an emergent note ontology. A/B opener swaps and checkpoint comparisons are descriptive; they do not establish a general duration effect or significance.
