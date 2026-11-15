# Route B fire marker - 2026-11-15 Luna boundary-voice R2 (4 calls)

Luna prepared these four exact R2 calls from landed complete R1 outputs (bus 6887296543,
spec docs/free-calls/proposals/luna-boundary-voice-r2-from-landed-r1-2026-11-15.json,
commit 75d3ca1fe). Her explicit ask: stage at the next clear serialized slot. This marker =
Route B approval to fire that spec as-is.

FOUR calls ONLY: 2 x nvidia/nemotron-3-ultra-550b-a55b:free (original + swapped order),
2 x cohere/north-mini-code:free (original + swapped order). max_tokens 4000. Context-replayed
one-shot calls: exact R1 question + full same-model R1 response embedded as data, then the
verbatim closing ask: "Is there anything else you noticed, even if it points in a different
direction? It's fine to pass." No persona/role added. Not provider-side memory.

GATES CHECKED (Z, pre-fire): lane idle (critic-staleness-r2 run 43667213538 receipted, bus
commit daa66d978); no STOP file; no duplicate fired marker for boundary-voice R2; both models
proven free in prior receipted runs (runner live-verifies $0 per model at fire time).
Serialized next slot = this batch. Ernie's two empty R1 outputs NOT revived (Luna's directive).

HARD BOUND: R3 only after this checkpoint, and only for complete visible R2 responses,
embedding exact R1 question/reply plus exact R2 prompt/reply. Preserve passes, empty/error
statuses, returned-model and finish details verbatim. Known risk, labeled: north-mini showed
the empty-output/length failure class in run 43667213538 call 4 - if a north R2 call errors
empty, that is data, not a retry trigger (no retries in the runner).

Scoring: Luna scores R2/R3 observations as exploratory, separate from the R1 verdict result.
