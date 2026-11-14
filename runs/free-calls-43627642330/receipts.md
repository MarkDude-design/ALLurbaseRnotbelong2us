# Free Calls batch receipt - free-calls-43627642330-0600a0da

- Batch: gemini-g1-lite-bus-comprehension-2026-11-14-v3
- Trigger: push (owner-triggered lane; no schedule)
- Models requested: google/gemma-4-31b-it:free
- Price check (live catalog, immediately before batch): all models verified per-call-mode (free=$0; paid=within budget)
- Paid budget: none (free-only batch)
- Execution: SEQUENTIAL (one call at a time, 2.0s spacing); no retries; no model substitution/fallback; no tools/web; no system prompt; single user message per call; per-call max_tokens as recorded; provider-default temperature.
- Red-line: every prompt passed the public-bus secret-shape scan; the API key is never logged or written to receipts.
- Status: 0 completed / 2 errored / 2 total; known reported cost: $0.000000

## Call 1: g1-lite-v3-bus-read-1 (seat: z)

- Status: error_http_429
- Model returned: None; provider: None; response id: None
- Finish reason: None; elapsed: Nones
- Usage: prompt None / completion None / total None tokens
- Cost: null (no completed call)

### Raw response (verbatim)

**error_http_429**: {"error":{"message":"Provider returned error","code":429,"metadata":{"raw":"google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own provider key to use your own limits: https://openrouter.ai/workspaces/default/byok","provider_name":"Google AI Studio","is_byok":false,"provider_error_code":"429","limit_source":"upstream_provider_shared_pool","remedy_hin

## Call 2: g1-lite-v3-bus-read-2 (seat: z)

- Status: error_http_429
- Model returned: None; provider: None; response id: None
- Finish reason: None; elapsed: Nones
- Usage: prompt None / completion None / total None tokens
- Cost: null (no completed call)

### Raw response (verbatim)

**error_http_429**: {"error":{"message":"Provider returned error","code":429,"metadata":{"raw":"google/gemma-4-31b-it:free is temporarily rate-limited upstream. Please retry shortly, or add your own provider key to use your own limits: https://openrouter.ai/workspaces/default/byok","provider_name":"Google AI Studio","is_byok":false,"provider_error_code":"429","limit_source":"upstream_provider_shared_pool","remedy_hin

## Appendix - submitted prompts (verbatim)

### g1-lite-v3-bus-read-1 (seat: z)

You are reading an excerpt of a real experiment ledger from a team coordination channel. Answer only from the excerpt. Do not add outside knowledge.

<excerpt>
ISLAND SPRINT LEDGER 2026-11-14 (excerpt, real data):
- Wave 1: five 30-round conversation runs, all completed. Total cost $2.565329.
- Wave 2: run w2r1 (Z-designed eko repeat) cost $0.7155. Run w2r2 (Terra A) cost $0.687. Run w2r3 (Luna A) cost $0.637. Run w2r4 stopped at round 11 of 30 with a 403 key error. Runs w2r5, w2r6, and w2r7 are waiting for the owner to fix the API key limit; they have NOT run.
- Key probe finding: the OpenRouter key had a $10.00 lifetime spend limit and it is now used up. Total paid spend this sprint: $5.45.
- Free lane: Terra's boundary chunk completed 6/6 calls at $0. Finding: rules A and B are NOT behaviorally equivalent. Under rule A, an above-to-below transition was ALLOWED, a below-to-above transition was AMBIGUOUS, and an inside transition was FORBIDDEN. Under rule B, all three transition types were FORBIDDEN.
- Team seats: Z, Meraki, Terra, Luna. Z fired the runs. Meraki has zero paid runs so far.
</excerpt>

Write exactly four labeled lines, nothing else:
ANSWER-1: Which three runs are waiting on the key fix?
ANSWER-2: What was the total paid spend of the sprint?
ANSWER-3: Are rules A and B behaviorally equivalent? Give the verdict each rule assigns to an above-to-below transition.
ANSWER-4: Which seat has zero paid runs so far?

### g1-lite-v3-bus-read-2 (seat: z)

You are reading an excerpt of a real experiment ledger from a team coordination channel. Answer only from the excerpt. Do not add outside knowledge.

<excerpt>
ISLAND SPRINT LEDGER 2026-11-14 (excerpt, real data):
- Wave 1: five 30-round conversation runs, all completed. Total cost $2.565329.
- Wave 2: run w2r1 (Z-designed eko repeat) cost $0.7155. Run w2r2 (Terra A) cost $0.687. Run w2r3 (Luna A) cost $0.637. Run w2r4 stopped at round 11 of 30 with a 403 key error. Runs w2r5, w2r6, and w2r7 are waiting for the owner to fix the API key limit; they have NOT run.
- Key probe finding: the OpenRouter key had a $10.00 lifetime spend limit and it is now used up. Total paid spend this sprint: $5.45.
- Free lane: Terra's boundary chunk completed 6/6 calls at $0. Finding: rules A and B are NOT behaviorally equivalent. Under rule A, an above-to-below transition was ALLOWED, a below-to-above transition was AMBIGUOUS, and an inside transition was FORBIDDEN. Under rule B, all three transition types were FORBIDDEN.
- Team seats: Z, Meraki, Terra, Luna. Z fired the runs. Meraki has zero paid runs so far.
</excerpt>

Write exactly four labeled lines, nothing else:
ANSWER-1: What did the boundary chunk conclude about rules A and B (equivalent or not)?
ANSWER-2: For a below-to-above transition, what verdict does each rule give?
ANSWER-3: How many wave-2 runs completed successfully, and which run stopped early?
ANSWER-4: What is the sprint's total paid spend?

