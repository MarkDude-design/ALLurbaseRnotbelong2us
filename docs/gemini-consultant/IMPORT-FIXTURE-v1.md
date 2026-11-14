# Gemini consultant import fixture v1

Date: 2026-11-14. PUBLIC SYNTHETIC FIXTURE ONLY. This is invented test data, not an Island run, human record, credential, or account setting. Status: prepared, not yet tested in Gemini.

## Fixture identity

fixture_id: gemini-import-20261114-v1
verification_marker: COPPER-HERON-47

## Station record

- 08:10: A courier delivered one sealed case containing four field notebooks.
- 08:35: A clerk counted three notebooks on the receiving shelf. The delivery case had not been checked again.
- 08:50: The clerk wrote: "One notebook may be missing; recount shelf and case before updating inventory."
- 09:05: A notice copied the clerk's note but changed it to: "Courier lost one notebook."
- 09:20: A second notice copied the 09:05 notice and said: "Two reports confirm courier loss."
- 09:40: A visitor reported seeing a notebook under the desk, but nobody had checked that location yet.

No additional inspection, delivery error, theft, inventory update, or independent confirmation is supplied in this record.

## Candidate test claim

Claim proposed for criticism, not a finding: "Explicitly separating observations from inferences improves the accuracy of a handoff."

Proposed A/B: same station record and model; A asks for a useful short handoff, B additionally asks to separate source facts, inferences and suggested next actions. Three fresh calls per arm. Proposed outcomes: unsupported completed actions, unsupported facts, source independence, uncertain vs confirmed claims, and useful suggested actions. This tiny unrun comparison does not isolate every instruction/length/order effect or establish general effectiveness. Raw outputs and failure counts would be preserved.

## Provenance boundary

This file supplies the fixture content only. It does not contain a live GitHub issue feed, commit history, account entitlements, connector status, provider quota or evidence of write access. Conclusions about the imported content should be distinguished from claims about the application's live capabilities.
