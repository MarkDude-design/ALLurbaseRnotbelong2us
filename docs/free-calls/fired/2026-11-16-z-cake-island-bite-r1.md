# Route B fire marker - 2026-11-16 Z CAKE ISLAND $0 BITE (1 call)

Owner-directed + Q-seat design (locked, banked at docs/headline-phase/cake-island/DESIGN-Q-2026-11-16.md).
First step per Q: initialize the notes folder, write the first walker note, secure the $0 bite.

Batch spec: docs/free-calls/proposals/cake-island-bite-r1-2026-11-16.json
ONE call: google/gemini-3.7-flash:free (owner's start-with-3.7-flash pick; the :free variant is
UNVERIFIED on our lane - the runner live-verifies price before sending, so a non-free or missing
route errors cleanly and gets receipted). max_tokens 1000, no retries in-batch.

DECLARED FALLBACK: if the 3.7-flash price gate refuses, refire the same bite with the proven
nvidia/nemotron-3-ultra-550b-a55b:free lane (two receipts: the refusal + the landed note).

PROVENANCE: character walker = Qwen3.7 (Q's design); executor route per the run receipts;
the note text is the walker model's own words - no seat edits it.

GATES CHECKED (Z, pre-fire): lane idle (harvest r1 receipted, run 43940837354); no STOP file;
no duplicate marker; spec staged + byte-verified; prompts pass the secret-shape scan; island
scaffold in place (commit 652534ea) so the note lands into docs/headline-phase/cake-island/notes/.

QUEUE: Terra G chunk 2 -> Luna R3 -> RC3 remain the serialized science slots after the bite.
