# Route B fire marker (refire) - 2026-11-16 Z — witness E3 shortcut + island-pairs turn 1, pointer fix

First marker (2026-11-16-witness-e3-shortcut-island-pairs-t1.md, commit 34665ede) triggered the runner,
but docs/free-calls/CURRENT-BATCH still named Terra's chunk-2 spec, so the bus re-ran Terra chunk 2
instead: run free-calls-43972039586, 12/12 completed, $0.000000. That is a receipt, not a loss —
Terra's boundary-geometry replication n just doubled (11/12 on 43966510386 + 12/12 on 43972039586).

This marker fires WITH the pointer repointed in the same commit:
docs/free-calls/CURRENT-BATCH -> docs/free-calls/proposals/witness-e3-shortcut-island-pairs-t1-2026-11-16.json

Spec unchanged from the first marker: 10 calls Luna E3 verbatim (shadow/delivered pairs,
max_tokens 600, judge nvidia/nemotron-3-ultra-550b-a55b:free) + 2 calls island-pairs turn 1
(Agent A nemotron, Agent B cohere/north-mini-code:free). Predictions already registered pre-fire
(docs/talk-research/witness-e3-shortcut-r1-2026-11-16.md, docs/headline-phase/island-pairs/DESIGN-Z-2026-11-16.md).

GATES: no STOP file; both models $0 live-verified tonight; no retries; prompts unchanged.
