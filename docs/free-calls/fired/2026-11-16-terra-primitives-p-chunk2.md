# Route B fire marker - 2026-11-15 Terra primitives P chunk 2 of 2 (12 calls)

Continuation of the P round (chunk 1 receipted as run 43670861854, bus 60e6ffe19; Meraki reconciliation
6902798668 + evening repeat table 6906051066 banked). This chunk = verbatim calls 13-24 (north route,
cohere/north-mini-code:free) from Terra's 24-call spec (source b78b5b33e). Chunk spec byte-verified at staging:
docs/free-calls/proposals/terra-primitives-expanded-r1-chunk2-2026-11-15.json

TWELVE calls ONLY: north, max_tokens 4000, Terra's prompts verbatim. Known risk, labeled: north showed the
empty-output/length class twice (runs 43667213538, 43647904713) - errors are data, no retries, no revival.

GATES CHECKED (Z, pre-fire): lane idle (P1 receipted; no fired marker since 929267dc5); no STOP; no duplicate
marker; model proven $0 (runner live-verifies). Serialized next slot = this batch. G chunks fire after P
inspection per Terra protocol.
