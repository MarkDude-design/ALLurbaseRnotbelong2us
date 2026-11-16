# Route B fire marker - 2026-11-16 Z — witness E3 shortcut (75% science) + island-pairs turn 1 ([HEADLINE-PHASE])

Owner's right-now order (2026-11-16 PT evening session, gas mode): fire the preliminary
two-agents-on-an-island experiment and the witness-experiment shortcut in one greedy batch.

Spec: docs/free-calls/proposals/witness-e3-shortcut-island-pairs-t1-2026-11-16.json
- 10 calls: Luna's E3 verbatim (5 shadow/delivered pairs), max_tokens 600, judge
  nvidia/nemotron-3-ultra-550b-a55b:free, free lane, no retries.
- 2 calls: island-pairs turn 1 (Agent A nemotron, Agent B cohere/north-mini-code:free),
  neutral prompts, [HEADLINE-PHASE] preliminary, predictions registered pre-fire in
  docs/headline-phase/island-pairs/DESIGN-Z-2026-11-16.md and
  docs/talk-research/witness-e3-shortcut-r1-2026-11-16.md.

Terra G chunk 2 landed (run free-calls-43966510386: 11/12 completed, 1 parse error, $0.000000) — receipt banked.

QUEUE POSITION: Luna boundary-voice R3, then critic RC3, remain next in the serialized
science queue behind this batch. Island-pairs turns 2-4 fire as sequential small batches
after this one lands (each turn needs the prior turn's verbatim output).

GATES (Z, pre-fire): no STOP file; no duplicate marker; both lane models $0 live-verified
tonight (nemotron 19/19, north-mini-code 11/12); prompts pass the public-bus secret-shape scan.
