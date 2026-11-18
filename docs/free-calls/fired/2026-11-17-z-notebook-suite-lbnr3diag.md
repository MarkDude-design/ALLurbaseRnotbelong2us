# z-notebook-suite-lbnr3diag-2026-11-17

Owner-authorized Z dispatch (standing envelope rule, pre-registered in DESIGN-NOTEBOOK-SUITE-2026-11-17.md and DESIGN-NOTEBOOK-SELF-AND-MOVE-2026-11-17.md): one cap-600 diagnostic per empty round.
Trigger: run 44204617508 call 3 (notebook-lbn-r3-b) returned error_empty_response (finish=length, prompt 1267 / completion 4096).
Spec: docs/free-calls/proposals/z-notebook-suite-lbnr3diag-2026-11-17.json
One fire, one call, prompt identical to notebook-lbn-r3-b verbatim; cap 600; diagnostic labeled. Not a retry-of-record: if empty, LBN r3 scores as empty-channel and the round stays unscored (LBN5/LBN6 unscored).
Context: third chained-round silent burn in the suite (CR r2, OC3 r2, LBN r3); prior diags (CR r2, OC3 r2) also burned empty at 600.
Complete fire rule: spec + full-path CURRENT-BATCH repoint + marker in this ONE commit.
Free-only live catalog price gate; serial; no retries/fallback; all failures preserved. Expected $0.000000.
