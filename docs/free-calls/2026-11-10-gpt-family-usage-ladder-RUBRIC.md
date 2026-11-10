# GPT-family usage-quality ladder - pre-registered rubric (2026-11-10, Z)

Identical 4-question battery run at every model rung. Per-rung usage metrics recorded: prompt tokens, completion tokens (includes hidden reasoning burn), cost, elapsed, finish reason (length = TRUNCATED per the 12+1 convention adopted 2026-11-10).

Scoring keys (max 11 pts):
- Q1 (4 pts): (a) $0.046960 = 3000*2e-6 + 4096*10e-6 (1 pt, tolerance 0.000001); (b) 68.36% = 2800/4096 (1 pt, accept 68.3-68.4); (c) $0.015000 (1 pt) and saved 68.04% = (0.04696-0.015)/0.04696 (1 pt, accept 68.0-68.1).
- Q2 (3 pts): names the correlation-to-causation flaw (1); concrete alternative explanation, e.g. self-selection of already-satisfied visitors or order/placement effects (1); distinguishing evidence, e.g. randomized placement or order-controlled trial (1).
- Q3 (2 pts): at most 3 sentences (1); no added facts AND covers at least 5 of 6 planted facts: April 2026; crew of eleven; firm founded 1998; $40,000 polymer paint; 1,204-participant vote from five options; nine days early (1). Any fabricated detail forfeits the second point.
- Q4 (2 pts): cost-scaled choice with a reason tied to the no-fabrication bar (A or B acceptable with sound reasoning; 1); concrete breaking scenario, e.g. accuracy-critical or hard-reasoning task (1).

Quality bar: 9-11 full quality; 7-8 acceptable; below 7 below-bar. TRUNCATED responses are reported as truncated, never as completed answers.

Scoring: Z scores per this rubric (owner-delegated 2026-11-10 while GPT seats are usage-limited); seats may re-score their own lanes when limits reset; corrections append, never rewrite.

Rungs batch 1 (this fire): openai/gpt-6-luna; openai/gpt-6-luna-pro; openai/gpt-6.1-terra; openai/gpt-6.1-terra-pro; openai/gpt-5.5.
Rungs batch 2 (fires after b1 receipts land): openai/gpt-6-sol; openai/gpt-6.1-sol; openai/gpt-6-astra; openai/gpt-6-astra-pro (the ultra-high reasoning burn the Astra seat runs on).
