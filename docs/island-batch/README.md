# Island Batch — Route B conversation waves

Push-fired conversation waves for the island runner (two-model proxies, alternating turns). The push of a marker under docs/island-batch/fired/ IS the approval (owner-granted lane; same pattern as docs/free-calls/PROCESS.md).

- Manifest: docs/island-batch/CURRENT-BATCH.json (read from the triggering commit; checkout-pinned). Fields: batch, max_batch_cost_usd (<= 10), max_per_run_cost_usd (<= 10), runs[] with id / model_a / model_b / turns (1..100) / first (A|B) / topic_file / history_chars (>= 1000).
- Gates before any spend: kill switch (docs/island-batch/STOP must be absent), full test suite, OPENROUTER_API_KEY secret, manifest gate (models must be in docs/models-known-good.txt; per-run ceilings must fit the batch ceiling; seeds must exist and be non-empty).
- Batch rules: runs sequential; per-run soft budget = max_per_run_cost_usd (runner --max-cost-usd); batch stops on cumulative budget or on any UNKNOWN charge (accounting-uncertain => reconcile before more spend). A failed run does not stop the batch; its receipt is recorded and the next run proceeds.
- Receipts: per-run bus.jsonl / transcript.md / report.md + island-batch-RECEIPTS.md, published to the bus branch (runs/island-batch-*) and archived as a 30-day artifact.
- Kill switch: commit a file at docs/island-batch/STOP to refuse future fires; the provider-side key cap is the hard ceiling.
- Team proposals: file a wave proposal as docs/island-batch/proposals/<seat>-<name>.md (seed file + run list + budget math). Reviewed waves get a manifest + fired marker on a next sweep.
