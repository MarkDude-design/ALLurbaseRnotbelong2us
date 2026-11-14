# Route B fire marker - 2026-11-14 island-batch wave 2 v2 (alternator re-fire, corrected batch arithmetic)

v1 (commit b37e9609) was CANCELLED before any job by the lane's own manifest gate: 7 runs x $1.00 per-run ceiling exceeded the $5.00 batch ceiling (gate assert: len(runs) x per_run <= batch). $0 spent, no calls, no runs. The gate worked as designed; the manifest was mine and the arithmetic error was mine. Luna (6875347695) and Terra (6875389950) both predicted it - reconciliation confirmed.

Correction: max_batch_cost_usd raised to $7.00 (sum of per-run soft ceilings), within the workflow's <=$10 gate and the owner's standing $5-$10 stakes floor (Nov 10 blanket + Nov 13 fire-all-you-can). Expected actual spend unchanged ~$1.4-2.2; provider-side key cap governs. Everything else identical to v1: same 7 runs, same alternator order (Z eko repeat, Terra mark-map A/B/A, Luna note A/B, Meraki chorus-witness A), same seeds, same models, same owner GO receipts.

Owner GO chain: in-chat 2026-11-14 ("Terra kicked ass. Put them in the workflow alternator with one from Luna... prioritize your experiments in the ordering") + standing overrides. Concurrent-safe with waves 1 and 3 (checkout-pinned manifests). Receipts -> bus runs/island-batch-w2r*.
