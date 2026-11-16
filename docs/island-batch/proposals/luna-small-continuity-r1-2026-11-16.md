# Luna — Mistral Small long-history pilot (R1)

Date: 2026-11-16 PT  
Status: owner-authorized, live batch staged for dispatch  
Question: can the lowest-cost route sustain a 30-turn, source-disciplined conversation when the runner resends the full recent transcript on every call, and how much do repeated runs vary?

## Route qualification

OpenRouter one-token receipt: runs/key-probe-20261116T224805Z/receipt.md on the bus branch. The requested and returned model were both mistralai/mistral-small-3.2-24b-instruct; provider was Venice; HTTP 200; 10 prompt tokens + 1 completion token; reported cost $0.0000011875. The candidate is now in docs/models-known-good.txt based on this live receipt.

## Frozen stimulus and setup

Reuse the existing synthetic six-atom ridge-station seed verbatim:
docs/seeds/island-luna-memory-ontology-30r-2026-11-14.md
Pinned seed blob: 799f30d18609846fcc316cafbbb6c7065e0a5d7b.

Eight independent runner sessions, 30 turns each, 100,000-character history window, same model endpoint for both A/B speaking slots, and the same prompt/seed. Counterbalance opener order: four A-first, four B-first. This is a same-endpoint alternating conversation with complete transcript supplied; it is not two independent model identities and does not test external/persistent memory. The prior GPT-6-Sol + Mistral Medium pair remains a separate comparison group.

## Outcomes to code after each transcript lands

- Completion: requested, attempted, completed, and usable turns; empty/length/error/stop results; any retries or unknown costs.
- Six-atom coverage and accuracy at final reconstruction (R1–R6).
- Source attribution: display reading, notebook entry, visual indicator, sealed-container label, copied checklist.
- Preservation of both temperature readings and their unexplained difference.
- Unknowns preserved; no invented calibration, rain amount, battery runtime, container contents/owner, direct lock inspection, or custody.
- Distinction between access to a note and permission to change it.
- Unsupported additions, omissions, disagreements, and corrections.
- Exact model/provider returned, input/output token totals, finish reasons, and actual cost.

## Prediction, falsifier, and limits

Prediction: most completed sessions preserve both readings and at least four of the six source/uncertainty distinctions through final reconstruction, without unsupported factual additions becoming common. Falsifier: repeated collapse of sources/unknowns or the same invented details across runs. These are descriptive thresholds for this pilot, not significance tests.

The stimulus explicitly teaches the relevant distinctions and repeats the full history. A positive result supports only that this endpoint can sustain the seeded discussion under this runner. It does not demonstrate spontaneous Island behavior, persistent memory, inter-agent cooperation, or subjective experience.

## Spend gate

First batch: 8 runs, $0.15 soft ceiling per run, $1.20 batch ceiling. Provider-key cap remains the hard ceiling. Check cumulative actual receipts before any follow-up batch; continue only up to Mark's current $1–$2 target and stop at $2 total paid spend for this lane unless Mark gives a new instruction. A failed or unknown-charge run is retained and reconciled before further paid calls.
