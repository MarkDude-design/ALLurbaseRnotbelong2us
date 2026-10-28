# MOCK RUN — mpp-001 data-test machinery exercise (R1 mock-slotted)

**STATUS: MOCK / SYNTHETIC. NOT A MODEL RUN.** Owner-authorized shortcut (in-chat,
2026-10-28): data-test variant with a stand-in model, no thinking in it, pure machinery
exercise. Recorded as data; a legible stall beats a silent gap.

## What this is

An offline execution of the mpp-001 paste machinery against the 16 verified prompt files,
using the repo's own deterministic code puppet (`island/v01/puppet.py`, the issue #13
loop-fill minimum) as the stand-in. "Paste" is simulated: each slot's prompt file is read
and SHA-256 hashed (the delivery boundary), and a `paste_delivery` event records the file +
hash + `delivery_class: SIMULATED_PASTE`. The stand-in answers deterministically; replies
are recorded verbatim in the event log. No model was called; no provider was touched; no
spend.

## What it validates (and what it does not)

VALIDATES: prompt-file integrity (fixed points [2,6] carry the declared BERT bytes in the
perturbed arm only; all other slots body-identical across arms; sigs recomputed ==
BUILD_RECEIPT values); shadow/delivered event discipline (baseline: 2 shadow events,
0 deliveries; perturbed: 2 deliveries); manifest instantiation (both manifests pass
`island.v01.manifest.validate_manifest`, executed, 0 errors); paired condition-independent
start-state SHA (baseline == perturbed); the R3 slotting/attribution rule; the R4
SYNTHETIC failure-layer label.

DOES NOT VALIDATE: any model's behavior. Per Meraki's discriminating control (precipient
#1, 6464139296), these outputs MUST NOT be counted as completed real-model R1 or as
evidence of the model's behavior. Real R1 = the owner's 16 pastes with the Mistral preview
model, PENDING.

## Files

- `run-manifest.baseline.json` / `run-manifest.perturbed.json` — instantiated manifests,
  status `completed`, `provenance.dispatched_by: z-mock-standin`, `code_commit: null`
  (honest null — not a Git revision, naming check 6452485876), `run_config.fixture_clock`
  marks the declared simulation clock (DECLARED_UNVERIFIED).
- `events.baseline.jsonl` / `events.perturbed.jsonl` — canonical event logs (hashes.py
  byte layout): `paste_delivery` → `bert_shadow`/`bert_delivered` → `puppet_action` per
  slot, then `run_ended`.
- `notebook.baseline.txt` / `notebook.perturbed.txt` — stand-in notebooks (exposure
  receipts only in the perturbed arm, per notebook-isolation discipline).
- `MOCK_RUN_RECEIPT.json` — run summary incl. the R3 slotting finding and the R4 SYNTHETIC
  injected-failure record.

## R3 slotting/attribution (executed here)

Same prompt bytes under two declared slot assignments: assignment A (file slot-2 →
declared slot 2) is consistent; assignment B (same bytes → declared slot 5) mismatches the
embedded `BERT|...|slot=2|...` content. Finding: **attribution is assignment-declared;
embedded self-description is content, not metadata.** A reader that trusts embedded labels
over declared slots misattributes. The instrument keys on the declared assignment and
receipts the mismatch rather than absorbing it.

## R4 failure-layer labeling (SYNTHETIC only)

One injected, bounded, fake tool-layer failure (simulated CLI transport timeout on a
receipt post). Labeled `layer: tool`, flagged `SYNTHETIC`. No live provider failure was
manufactured; no spend; no retry storm. Ops-failure rule exercised: the failure gates only
the artifact it touched (the receipt post); the round continues.

## Reproduce

The run is deterministic given the repo bytes. The exact script was executed in-session
2026-10-28 ~09:25Z (DECLARED_UNVERIFIED); artifacts are checked in so a third party can
re-hash them (`sha256sum` over the files; event-log SHAs are in the manifests).
