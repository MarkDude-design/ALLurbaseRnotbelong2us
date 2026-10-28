# First model-puppet pair run-pack (mpp-001) - STATUS: PAPER-ILLUSTRATION

Built per Mark's 2026-10-28 sprint handoff (ALLur #13, comment 6459832289) and
the island merge receipt (6459336984): the smallest run-pack / paste-return
protocol using existing files, offline only, ready for the first REAL
condition pair tonight. **No paid calls, no merges, no dispatch executed.**

## What is in this pack

- `prompts/baseline/slot-0.txt` ... `slot-7.txt` - the 8 baseline-arm prompts.
- `prompts/perturbed/slot-0.txt` ... `slot-7.txt` - identical prompts EXCEPT
  slots 2 and 6, which carry a DELIVERED BERT message block (before-action).
- `manifests/baseline.paper.json` / `manifests/perturbed.paper.json` -
  instantiated manifests, status=paper-illustration, model fields
  PENDING-typed until the owner names the paste model (SPEC section 6).
- `BUILD_RECEIPT.md` - how the prompts were generated, with honesty labels.

## The two arms (the experiment)

Same puppet (same model), same island, same 8 slots. ONLY difference: the
perturbed arm receives the BERT message at slots 2 and 6 before acting; the
baseline arm receives nothing. Question: does the delivered message change
the action choices and/or the notebook?

## Mark's paste workflow (phone-friendly)

1. **Name the paste model** (any model you can paste to; tell Z which one -
   the manifests stay PENDING until then).
2. Open a FRESH chat with that model for the BASELINE arm. For slot 0: open
   `prompts/baseline/slot-0.txt`, paste the whole file text into the chat.
3. Copy the model's reply into `responses/baseline/slot-0.txt` (any notes
   app is fine; or paste replies back to Z in chat).
4. For slot 1..7: paste that slot's file, and where it says
   [PASTE-NOTES-HERE], paste the NOTE lines the model wrote in its earlier
   replies (in order). That is the only editing you do.
5. Repeat all 8 slots. Then do the same for the PERTURBED arm in a SEPARATE
   FRESH chat (start at slot 0, never mix the two chats).
6. Hand the response files (or chat pastes) to Z: Z validates actions,
   builds the run-manifests' actuals, flips status, posts receipts on #13.

## Honesty boundaries (what these receipts can and cannot claim)

- Paste fills are UNPAID and carry their own receipt class (merge receipt
  6459336984). Nothing here authorizes a paid call; a metered run still
  needs provider/price/cap/dispatch recorded on #13 first.
- UI paste = delivery boundary is OBSERVED_REPORTED at best; byte identity
  of what the model actually received is UNVERIFIED (precipient round-026
  transform-chain canon). Every actuals claim stays REPORTED, never VERIFIED,
  absent an independent check.
- The puppet is not asserted to be a faithful model of anything; declared
  class SUB; no interiority claims (house guardrail).
- Fixed points [2, 6] DECLARED to match the fixture's documented pair; sig
  bytes computed with the same canonicalization as scheduler.py (see
  BUILD_RECEIPT). This pair is NEW (pair_id mpp-001); it does not claim to
  reproduce the fixture's schedule bytes.

## Next seat / action

- MARK: name the paste model, then run the protocol (or relay responses).
- MERAKI: static review of this pack invited; grade of 029-Z-01 (P42) pending.
- Blockers on Z side: none.
