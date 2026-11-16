# FIRED: luna-small-continuity-r1-2026-11-16

Owner GO: Mark's direct authorization in chat on 2026-11-16: give Luna dispatch control, use cheaper calls first, and proceed with several rounds; aim for $1–$2 in actual experiment spend, with the separate $5 burn deferred.

Proposal: docs/island-batch/proposals/luna-small-continuity-r1-2026-11-16.md
Frozen stimulus: docs/seeds/island-luna-memory-ontology-30r-2026-11-14.md (blob 799f30d18609846fcc316cafbbb6c7065e0a5d7b)
Manifest: docs/island-batch/CURRENT-BATCH.json at triggering commit; 8 sessions x 30 turns, same Mistral Small 3.2 endpoint in A/B slots, four A-first and four B-first, 100000-char history.
Route qualification: runs/key-probe-20261116T224805Z/receipt.md; Mistral Small 3.2 returned HTTP 200 via Venice at reported cost $0.0000011875 for the one-token check.
Budget: $0.15 soft/run; $1.20 batch ceiling; owner key cap remains the hard boundary. Sequential. Record all errors/unknowns and actual costs; no hidden model fallback.
Experiment scope: same-endpoint alternating conversation with transcript supplied each turn. Not two independently authenticated agents and not persistent-memory evidence.
