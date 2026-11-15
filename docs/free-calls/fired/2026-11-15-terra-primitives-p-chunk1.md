# Route B fire marker - 2026-11-15 Terra primitives P chunk 1 of 2 (12 calls)

Owner direction (live session, 2026-11-15): fire all the experiments. Terra's expanded Round P,
chunked per her <=12 protocol. Source spec: docs/free-calls/proposals/terra-primitives-expanded-r1-2026-11-14.json
(commit b78b5b33e, 24 calls). Chunking method: verbatim split, calls 1-12 = all 12 ultra-route calls
(unspecified/flight/local x 2 orders x 2 reps). Chunk 2 (calls 13-24, north route) fires after this
receipt; inspect P before G per Terra's protocol. Chunk spec byte-verified after push (9181 chars,
curly-quote count 48, fetch-back identical):
docs/free-calls/proposals/terra-primitives-expanded-r1-chunk1-2026-11-15.json

TWELVE calls ONLY: nvidia/nemotron-3-ultra-550b-a55b:free, max_tokens 4000, Terra's prompts verbatim.
Preserve initial answers; quoted-context follow-ups are a LATER separate step built from these receipts.

GATES CHECKED (Z, pre-fire): lane idle (luna boundary-voice R2 run 43667443704 receipted, bus commit
692c2a727); no STOP file; no duplicate fired marker (the earlier 12-call screen was NEVER fired - it was
staged only and is superseded by Terra's expanded P per 6887780287); model proven free and fresh-baseline
per RC2 (run 43667213538). Runner live-verifies $0 at fire.
