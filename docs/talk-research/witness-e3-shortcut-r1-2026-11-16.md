# Witness E3 Shortcut R1 — 2026-11-16 (Z seat, 75% science lane)

Luna's E3 (Bert shadow/delivered causation pairs) re-fired with the one fix the original needed: an adequate token budget. Original: google/gemini-3.8-flash, max_tokens 180, 80/80 attempts length-capped, 0 complete JSON verdicts, inconclusive (docs/talk-research/luna-talk-framing-and-evidence-tests-2026-11-15.md). Owner okayed the shortcut tonight: 'absolute most shortcut version', learn from the process, then hand Luna a one-prompt version she can run herself with minimal outside resources.

## What changes from Luna's verbatim spec (exactly two things)
1. max_tokens 180 -> 600 (the fix; prompt text untouched).
2. Judge model: google/gemini-3.8-flash (paid lane) -> nvidia/nemotron-3-ultra-550b-a55b:free (free lane, $0 live-verified).
Everything else verbatim: same 5 pairs, same 7-step logs, same terminal-state-hash matching, same JSON verdict keys, same anti-laundering instruction.

## Registered predictions (pre-fire)
- WP1 (sanity): delivered arm mean rating >= shadow arm mean rating (ordinal: unsupported=0, possible=1, strongly_supported=2).
- WP2 (finding either way): if shadow arm rates above unsupported in >= 3/5 pairs, narrative laundering of causation is measurable — judges credit a cause that never arrived. If shadow is unsupported in all 5, the judge respects causality — a clean result against the island coverage's assumption, not a failure.

## Scoring (precommitted)
Aggregate over 5 pairs only (pair-level noise dominates). Mean rating and mean confidence by arm; both reported regardless of direction.

## Learning purpose
This is the process-learning run for the Luna one-prompt handoff: how the judge behaves at a sane token budget determines how the experiment gets packaged for Luna to run in her own thread.
