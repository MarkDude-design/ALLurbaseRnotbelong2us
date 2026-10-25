#!/bin/sh
# Full 9-run audition matrix, sequential, stop on first error. Zero fields.
# Usage: sh scripts/run-matrix.sh [max_cost_usd_per_run]
# Requires OPENROUTER_API_KEY exported (the capped council-runs key).
# Rerun semantics: every run uses the SAME method — same seed, same models,
# same prompts, same pipeline (parse -> 3 sub answers -> synthesis ->
# 3 blind critiques -> verdict -> receipts). Only the models' own sampling
# varies between runs. Live time = model latency (~seconds per call, 8 calls)
# plus any 429 retry backoff; demo mode is instant.
set -e
if [ -z "$OPENROUTER_API_KEY" ]; then
  echo "export OPENROUTER_API_KEY first (the capped council-runs key)" >&2
  exit 1
fi
cap="${1:-1}"
for stem in expert-C1 expert-C2 expert-C3 sub-C1 sub-C2 sub-C3 \
            heldout-C1 heldout-C2 heldout-C3; do
  echo "=== matrix run: $stem ==="
  sh scripts/run.sh "$stem" "$cap"
done
echo "matrix complete - per-run receipts under runs/<timestamp>-<stem>/"
