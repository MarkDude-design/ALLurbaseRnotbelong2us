# Stillness t12 — one versioned cap repair
Owner authorization: current Mark instruction “you or Z fire them all unless a reason”, plus standing experiment dispatch control. Executed by Luna, not represented as Z's action.

Pre-fire bus registration: issue #2 comment 6940620474.
Original run: 44006507262 / job 133783050292; validator rejected 4500 before any send.
Original spec stays unchanged.
New spec: docs/free-calls/proposals/luna-stillness2-t12-cap4096-repair-2026-11-16.json
Spec commit: 8b91bf49846aa33a02045db1f3dd641d09fdf271
Pointer commit: 442a24f738cd1ed227e212ed27ed97543739b172

Only experimental setting changed: B max_tokens 4500 to 4096, inside existing validator.
A remains 600. Prompt bodies and requested models are byte-identical to the original.
Batch/call IDs identify this repair. Both models :free; no paid block.
Live catalog $0 gate, secret scan, serial execution, no retries, no fallback remain runner-enforced.
One fire. If gate or delivery fails, preserve failure; no automatic re-fire.
Semantic scoring remains Z's frozen DESIGN-STILLNESS-2026-11-16.md.
Any new outcome is excluded from the static report frozen at bus 7146046f5802f43d4321422f0c6193af4436f0ec.
Queue rechecked before pointer edit: no in-progress/queued Island Batch or Free Calls runs.
