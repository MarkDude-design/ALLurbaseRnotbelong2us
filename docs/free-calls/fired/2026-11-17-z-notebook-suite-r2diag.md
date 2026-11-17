# z-notebook-suite-r2diag-2026-11-17

Owner-authorized Z dispatch (standing envelope rule, pre-registered in DESIGN-NOTEBOOK-SUITE-2026-11-17.md and the r2 design addendum): one cap-600 diagnostic per empty round.
Trigger: run 44195495657 returned error_empty_response on notebook-cr-r2-b (finish=length @4096) and notebook-oc1-voice (finish=length @300); NN r2 and LBN r2 completed clean.
Spec: docs/free-calls/proposals/z-notebook-suite-r2diag-2026-11-17.json
One fire, two calls, prompts identical to the r2 spec verbatim; caps raised to 600 (diagnostic label in spec). This is a diagnostic, not a retry-of-record: whichever rounds stay empty stay scored-as-empty for the suite; a filled diagnostic unblocks the chained record only as a labeled diagnostic receipt.
Complete fire rule: spec + full-path CURRENT-BATCH repoint + marker in this ONE commit.
Free-only live catalog price gate; serial; no retries/fallback; all failures preserved. Expected $0.000000.
