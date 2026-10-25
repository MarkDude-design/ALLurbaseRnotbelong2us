#!/bin/sh
# One-command council dispatch (Mark's UX ask: no models, no 5 fields to type).
# Usage:  sh scripts/run.sh <stem> [max_cost_usd]
#   stem:  expert-C1 | expert-C2 | expert-C3 | sub-C1 | sub-C2 | sub-C3
#          heldout-C1 | heldout-C2 | heldout-C3 | base
#   cap:   optional, default 1 (local soft ceiling per run; the OpenRouter
#          "council-runs" key cap is the hard account-side ceiling)
# Requires OPENROUTER_API_KEY exported (the capped council-runs key).
set -e
stem="${1:?usage: sh scripts/run.sh <expert-C1|...|base> [max_cost_usd]}"
cap="${2:-1}"
if [ -z "$OPENROUTER_API_KEY" ]; then
  echo "export OPENROUTER_API_KEY first (the capped council-runs key)" >&2
  exit 1
fi
if [ "$stem" = "base" ]; then
  file="docs/seeds/eko-council.md"
else
  file="docs/seeds/eko-council-$stem.md"
fi
if [ ! -f "$file" ]; then
  echo "no seed for stem '$stem': $file" >&2
  exit 1
fi
out="runs/$(date -u +%Y%m%dT%H%M%SZ)-$stem"
while [ -e "$out" ]; do out="$out-x"; done
echo "dispatch: $file | cap \$$cap | outdir $out"
python3 -m island.council --mode live --council-file "$file" \
  --max-cost-usd "$cap" --outdir "$out"
