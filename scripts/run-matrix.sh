#!/bin/sh
# Full 9-run audition matrix, sequential, GAS MODE v2: a failed run is
# receipted, then summarized. Uncertain accounting stops remaining work.
# Usage: sh scripts/run-matrix.sh [max_cost_usd_per_run]
# Requires OPENROUTER_API_KEY exported (the capped council-runs key).
# Rerun semantics: every run uses the SAME method — same seed, same models,
# same prompts, same pipeline (parse -> 3 sub answers -> synthesis ->
# 3 blind critiques -> verdict -> receipts). Only the models' own sampling
# varies between runs. Live time = model latency (~seconds per call, 8 calls)
# plus any 429 retry backoff; demo mode is instant.
if [ -z "$OPENROUTER_API_KEY" ]; then
  echo "export OPENROUTER_API_KEY first (the capped council-runs key)" >&2
  exit 1
fi
cap="${1:-1}"
ok=0
failed=0
failed_stems=""
uncertain_stem=""
skipped_stems=""
for stem in expert-C1 expert-C2 expert-C3 sub-C1 sub-C2 sub-C3 \
            heldout-C1 heldout-C2 heldout-C3; do
  if [ -n "$uncertain_stem" ]; then
    skipped_stems="$skipped_stems $stem"
    continue
  fi
  echo "=== matrix run: $stem ==="
  if sh scripts/run.sh "$stem" "$cap"; then
    ok=$((ok + 1))
  else
    status=$?
    failed=$((failed + 1))
    failed_stems="$failed_stems $stem"
    if [ "$status" -eq 2 ]; then
      uncertain_stem="$stem"
      echo "=== $stem: accounting UNKNOWN; stopping before another stem (receipts kept) ==="
      continue
    fi
    echo "=== $stem FAILED (receipt kept under runs/); continuing — gas mode ==="
  fi
done
echo "matrix complete: $ok ok, $failed failed"
[ -n "$failed_stems" ] && echo "failed stems:$failed_stems"
echo "per-run receipts under runs/<timestamp>-<stem>/"
if [ -n "$uncertain_stem" ]; then
  echo "accounting uncertainty in $uncertain_stem; known spend is an incomplete subtotal"
  echo "skipped stems:${skipped_stems:- none}"
  exit 2
fi
[ "$failed" -eq 0 ]

