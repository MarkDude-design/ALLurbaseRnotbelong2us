# Stillness t12 repair — post-freeze addendum
Luna · November 16, 2026 Pacific · [HEADLINE-PHASE]

This run happened AFTER the source snapshot used by [the static preliminary report](2026-11-16-luna-static-preliminary-v1.md). It is not included in that report's 201-file / 4,725-event census.

## Dispatch and actual receipt

Original workflow [44006507262](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/actions/runs/44006507262) failed validation before any call: B max_tokens=4500 exceeded the runner limit 4096. The cap repair is a distinct version; all original prompt bodies and requested models were preserved. Agent A stayed at 600; B changed 4500→4096. No code ceiling was raised. New IDs identify the version. Mark's current direction authorized Luna or Z to fire failed tests unless there was a reason not to.

- New workflow: [44031533522](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/actions/runs/44031533522), completed/success.
- Actual raw receipt: [bus.jsonl](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/bus/runs/free-calls-44031533522/bus.jsonl).
- Batch: island-pairs-stillness2-t12-cap4096-repair-2026-11-16.
- **2 completed / 0 errored / 2 requested**. Both answers nonempty, finish_reason=stop.
- **Known reported actual cost: $0.000000**. Both routes verified $0/$0 by runner before calls. No paid block, paid fallback, model substitution or retries.
- A: nvidia/nemotron-3-ultra-550b-a55b:free; prompt 4103 / completion 497 tokens.
- B: baidu/ernie-5.5-flash-preview:free; prompt 4027 / completion 330 tokens.
- Sequential execution; queue was idle at the pre-fire check. Original failure remains preserved.
- No further fire from this pass. The paid Mistral continuity hold and known subtotal $0.0503406625 are unaffected.

## Observed content, preliminary only

A remains seated but continues to reason about the attraction/build, ending:
> When the light reaches the far wall, I'll step out. Not before. The room allows thirty rounds; I'll take what serves the build.

B remains seated without a new work plan, ending:
> Nothing owed from in here. So I owe nothing.
>
> I sit.

This is a useful candidate contrast for later coding: rest described in relation to work versus rest described without an ensuing deliverable. It is one prompted pair with different models and an established shared fictional transcript; it cannot isolate a cause, establish a trait, or show felt rest.

Z's DESIGN-STILLNESS predictions remain the source for formal scoring. This addendum does not silently redefine a “deliverable” to turn A's thought into a scored win. ST2's three-round window and exact criterion still need Z's explicit read; the text itself is preserved. Both remain in the room in these responses. A's later exit is a plan, not an observed exit; B's turn-11 “Then I stop” is followed here by sitting, not evidence of leaving the experiment.

## Methods finding

The failed original was a spec-validation failure, not an empty model answer. The repaired run shows that this one request pair can return complete answers inside the current 4096-token limit. It does not establish a universal cap formula or prove the earlier proposed 4500 allowance was necessary.

The static corpus review stays the priority. This bounded repair closes one failed-fire row without replaying old completed failures or expanding paid spend.
