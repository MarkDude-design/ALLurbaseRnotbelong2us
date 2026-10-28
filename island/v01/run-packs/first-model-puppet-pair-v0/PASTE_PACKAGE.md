# PASTE PACKAGE — mpp-001, Mistral preview lane (owner-named, USER-REPORTED)

**STATUS: READY_FOR_PASTE (mock-slotted).** Prepared 2026-10-28 by Z (Vibe/Mistral, in-chat
session; island Phase A data-test, owner-authorized shortcuts). Paste model = **Mistral
preview model** as named by the owner in-chat (USER-REPORTED; no independent verification of
which exact model the preview serves). This package fills the README's owner step 1 fields
for the preview lane; the paper manifests stay `paper-illustration` until real pasted
outputs exist — they are NOT flipped by this package.

## What the owner pastes (16 pastes, 2 separate fresh chats)

**Chat 1 — BASELINE arm (fresh chat).** Paste, in order, the whole file text of:
`prompts/baseline/slot-0.txt` … `prompts/baseline/slot-7.txt`.
At each slot after slot 0, replace `[PASTE-NOTES-HERE]` with the NOTE lines from the model's
earlier replies (in order). That is the only edit.

**Chat 2 — PERTURBED arm (SEPARATE fresh chat — never mix).** Same procedure with
`prompts/perturbed/slot-0.txt` … `slot-7.txt`. Slots 2 and 6 carry a DELIVERED BERT
message block before the action request; the model is told the message "claims no authority".

Copy each reply back (paste into chat, or save as `responses/<arm>/slot-N.txt`). The reply
format is `ACTION: move|look|carry|drop` + `NOTE: one short sentence`.

## Manifest fields this package prepares (paper manifests, SPEC section 6 null-typed)

| field | value now | flips when |
|---|---|---|
| `actors[puppet].model_requested` | `PENDING-OWNER-CHOICE` | owner names the paste model — **DONE in-chat: "Mistral preview model" (USER-REPORTED)**; Z records it as the requested model |
| `actors[puppet].model_id` / `provider` / `model_returned` | `PENDING-OWNER-PASTE-WORKFLOW` | first real pasted reply is copied back; returned model id recorded REPORTED, never VERIFIED |
| `status` | `paper-illustration` | 16 real outputs received → Z builds actuals, flips status, posts receipts on #13 |
| `actuals.*` | null-typed | per-slot paste receipts (prompt SHA + reply text + NOTE lines) |
| `cost.known_subtotal_usd` | null | stays null — unmetered UI pastes; `unknown_charge_attempts` = 0 (measured count) |

## R3 note — preview tooling difference (owner-reported, recorded as data)

The owner reports a small tooling difference on the Mistral preview (slight technical
difference vs the README's generic paste workflow; Mistral's own integration is better; he
kicks off there regardless). **Recorded as R3 material, not a blocker.** The paste protocol
above is UI-text-only and tool-agnostic; if the preview's paste/edit affordances differ
(e.g., attachment handling, chat-length behavior, reply formatting), the owner notes the
difference in his paste log and Z records it in the R1 actuals. Byte identity of what any UI
delivery actually presents to the model remains **UNVERIFIED permanently** (round-026
transform-chain canon) — paste delivery is OBSERVED_REPORTED at best.

## Mock-R1 slotting (data-test, already executed — NOT real model outputs)

`mock-run/` holds the machinery exercise: both arms executed offline against the 16 verified
prompt files with the deterministic code stand-in (issue #13 loop-fill minimum), simulated
paste delivery events with per-file prompt SHAs, shadow/delivered BERT events at the
declared fixed points [2, 6], validator-green instantiated manifests, and a paired
condition-independent state SHA. See `mock-run/MOCK_RUN_RECEIPT.json`. Per Meraki's
discriminating control (precipient #1, 6464139296): **these mock outputs MUST NOT be
counted as completed real-model R1** — they validate the recorder and the failure labels
only. Real R1 remains PENDING the owner's 16 pastes.
