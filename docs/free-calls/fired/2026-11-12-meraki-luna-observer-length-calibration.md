# Fired marker - observer-lens length calibration (Route B push by Z)

- Spec: docs/free-calls/2026-11-12-meraki-luna-observer-length-calibration.json (staged by Meraki, commit 5f4c51ac; UNTOUCHED, prompts verbatim).
- Owner GO: bus 6835326400 (doubling/tripling OUTPUT token budget where needed; NOT a raise of monetary caps or guard changes).
- Batch: meraki-luna-island-length-calibration-2026-11-12. 4 calls, google/gemini-3.8-flash, paid budget_usd 1 (existing technical ceiling; expected actual spend well under $0.01).
- Design: exact E1-01 neutral + E5-05-B source prompts, each at max_tokens 360 and 540. Tests response completion / JSON yield, not arm effects.
- Z preflight review: spec parses, 4 unique IDs, one model, per-call caps within runner 1-4096 range; gemini-3.8-flash catalog-verified live ~2.5h ago in run free-calls-43288925858; runner re-verifies catalog + aborts on mismatch; $1 hard ceiling in code unchanged.
- Pass metric (per Meraki PLAN): finish_reason not length, response parses after fence-strip, exactly 5 required keys, rating/confidence types valid, evidence IDs grounded. Gateway success alone does NOT count. If 540 still truncated: STOP and diagnose provider reasoning/accounting; no blind rerun, no silent 1080.
- Receipts: bus branch runs/free-calls-<id>/ (receipts.md + bus.jsonl), auto-published by workflow.
- Pushed by Z (Vibe/Mistral native seat, shared GitHub connector). ASCII-only authored content.
