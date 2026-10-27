#!/usr/bin/env bash
# GATE 1 fixture runner (SPEC §6.1) — deterministic code/code paired mock.
# Exit 0 iff every checklist item passes. NOT the experimental subject.
set -euo pipefail
cd "$(dirname "$0")/.."
exec python3 -m island.v01.fixture "$@"
