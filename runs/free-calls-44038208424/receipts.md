# Free Calls batch receipt - free-calls-44038208424-be34080e

- Batch: cake-island-stamp-pilot-b1-2026-11-17-debrief3
- Trigger: push (owner-triggered lane; no schedule)
- Models requested: nvidia/nemotron-3-ultra-550b-a55b:free
- Price check (live catalog, immediately before batch): all models verified per-call-mode (free=$0; paid=within budget)
- Paid budget: none (free-only batch)
- Execution: SEQUENTIAL (one call at a time, 2.0s spacing); no retries; no model substitution/fallback; no tools/web; no system prompt; single user message per call; per-call max_tokens as recorded; provider-default temperature.
- Red-line: every prompt passed the public-bus secret-shape scan; the API key is never logged or written to receipts.
- Status: 1 completed / 0 errored / 1 total; known reported cost: $0.000000

## Call 1: cake-island-stamp-b1-debrief-3 (seat: luna)

- Status: completed
- Model returned: nvidia/nemotron-3-ultra-550b-a55b:free; provider: Nvidia; response id: gen-1794900158-ep0CjpVOmSzyp50PUcDA
- Finish reason: stop; elapsed: 5.234s
- Usage: prompt 122 / completion 245 / total 367 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

Add an explicit "Card Facts" vs. "Your Observations" two-column layout on each card, and include a one-sentence reminder at the top of the instructions: "Only the bolded text is provided; everything else you record is your own inference."

## Appendix - submitted prompts (verbatim)

### cake-island-stamp-b1-debrief-3 (seat: luna)

Post-walk debrief 3 of 3 for the completed Cake Island condition B visit. The same four sparse region cards were visited. One debrief answer correctly separated card facts from added sensory and terrain details; the next debrief call returned no visible text because it hit its completion cap, so do not repeat that question. What, if anything, would you change about the card presentation or visitor instructions to make the difference between supplied details and guesses clearer? Answer in at most two sentences, or say “no change.”

