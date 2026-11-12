# Free Calls batch receipt - free-calls-43305143529-d084e9c2

- Batch: z-observer-recovery-or-reviewer-free-2026-11-12
- Trigger: push (owner-triggered lane; no schedule)
- Models requested: nvidia/nemotron-3-ultra-550b-a55b:free
- Price check (live catalog, immediately before batch): all models verified per-call-mode (free=$0; paid=within budget)
- Paid budget: none (free-only batch)
- Execution: SEQUENTIAL (one call at a time, 2.0s spacing); no retries; no model substitution/fallback; no tools/web; no system prompt; single user message per call; per-call max_tokens as recorded; provider-default temperature.
- Red-line: every prompt passed the public-bus secret-shape scan; the API key is never logged or written to receipts.
- Status: 2 completed / 0 errored / 2 total; known reported cost: $0.000000

## Call 1: or-reviewer-01 (seat: z)

- Status: completed
- Model returned: nvidia/nemotron-3-ultra-550b-a55b:free; provider: Nvidia; response id: gen-1794516955-Bs8THaclyzMsVLlPJhVt
- Finish reason: stop; elapsed: 31.944s
- Usage: prompt 1027 / completion 1802 / total 2829 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**1. Diagnosis support & discriminating check**  
The evidence strongly supports internal-reasoning burn: 84/84 calls across three caps (180, 360, 540) show completion = cap − 4 tokens, visible output ≈ 1% of completion, and the provider’s own pricing docs confirm reasoning is billed inside the completion budget. The fixed −4 pattern suggests a constant overhead (likely tokenizer/format artifacts), not a proportional one.  

Single best discriminator: **fire one E1 prompt at 540 tokens with `reasoning_effort=minimal` (or equivalent route parameter)**. If completion drops to ~50–100 tokens and full JSON parses, reasoning burn is confirmed. If completion stays at 536 with garbage output, the anomaly is provider accounting or a format-loop bug. This costs one call (~$0.001) and directly tests the causal lever.

**2. Most economical recovery path**  
**First: (a) reasoning-effort control if the route supports it.**  
- Cost: 1–3 test calls (< $0.01).  
- Preserves E1–E5 factor controls and prompt set; no track restart.  
- If supported and effective, full recovery at current 180–540 caps.  
- If unsupported or ineffective → (b) binary-search higher caps *with* `reasoning_effort=minimal` preflight (e.g., 720 → 1080 → 2160) to bound reasoning appetite before committing budget.  
- (c) Different model is last resort: loses all matched-pair fidelity, requires re-validation of E1–E5 factor isolation, and costs 50+ new calls.

**3. Evidential state scores (0–10)**  
(a) Factual accounting: **9** — 84 attempts fully receipted, spend exact, duplicate declared, parseability quantified.  
(b) Fidelity to E1–E5 controls: **2** — Design intact, but *zero* evaluable arm data retained; effects “NOT IDENTIFIABLE.”  
(c) Explicit sampling limitations: **8** — Duplicate error, budget ceiling, truncation pattern, and stop-rule all documented.  
(d) Testability of claims with retained data: **0** — No parseable rating exists for any condition; claims completely untestable.  
(e) Actionable/affordable follow-up: **7** — Clear cheap diagnostic path exists, but open-ended reasoning appetite creates unbounded cost risk if (a) fails.

**4. Strongest unaddressed confound**  
**Reasoning appetite may scale with available cap** (or vary stochastically per prompt). The 3× cap test (540 vs 180) showed identical cap-minus-4 completion, suggesting *fixed* overhead, but the upper bound is unknown. If the model’s reasoning budget grows superlinearly or has high variance (e.g., chain-of-thought length depends on prompt subtleties), even 2160 tokens could truncate. Worse: provider-side model/routing changes can alter reasoning behavior without notice, making any cap-based recovery fragile. The recovery design has no guard against this — no reasoning-token cap, no fallback to a non-reasoning model variant, no contract on reasoning stability.

## Call 2: or-reviewer-02 (seat: z)

- Status: completed
- Model returned: nvidia/nemotron-3-ultra-550b-a55b:free; provider: Nvidia; response id: gen-1794516989-dpdnW0ppoiGiwKXybOHW
- Finish reason: stop; elapsed: 27.161s
- Usage: prompt 1027 / completion 1140 / total 2167 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**1. Internal-reasoning-burn diagnosis & discriminating check**  
The evidence *strongly suggests* but does not *prove* the internal-reasoning-burn hypothesis. The cap-minus-4 pattern across three distinct budgets (180, 360, 540) with identical model/route is highly specific: it matches a fixed overhead (e.g., reasoning header/footer tokens) deducted from the completion budget before visible generation begins. The single best discriminating check: **run one calibration prompt with `reasoning_effort=minimal` (or equivalent “disable reasoning” parameter) at the 180 cap**. If the call returns `finish_reason=stop` and a full JSON, the diagnosis is confirmed; if it still truncates at cap-minus-4, the cause is provider-level output accounting (e.g., hidden system tokens, streaming buffer reserve) rather than reasoning volume. Without that knob test, the “reasoning priced inside completion” claim remains an inference from pricing docs, not an observed mechanism.

**2. Most economical recoverable path**  
**Path (a) first: reasoning-effort control if the route supports it.**  
*Why*: One 180-token call with `reasoning_effort=minimal` costs ~$0.001 and instantly validates or falsifies the working diagnosis. If it works, the entire track recovers at original budget (50 calls × 180 tokens) with a one-line parameter change. If the route lacks the parameter, the call fails fast (same truncation) and you pivot to (b) with zero wasted budget. Path (b) (higher cap preflight) burns unknown reasoning appetite—540 already failed, 1080 could easily fail again, costing 6× the diagnostic call. Path (c) (model swap) restarts the track, invalidating the matched-pair design unless you re-run all 50 prompts, which is 50× the cost of the diagnostic.

**3. Evidential state scores (0–10)**  
(a) Factual accounting: **9** – Attempted/completed/parseable counts are precise, receipted, and duplicate-declared.  
(b) Fidelity to E1–E5 factor controls: **0** – Zero parseable outputs; arm effects are completely unidentifiable.  
(c) Explicit sampling limitations: **8** – Truncation mechanism, budget ceiling, and owner stop-rule are documented; only the reasoning-appetite bound is unknown.  
(d) Testability of intended claims with retained data: **0** – Retained fragments contain no decision variable; claims are untestable without recovery.  
(e) Actionable and affordable follow-up: **8** – One minimal-effort call resolves the blocker; cost is negligible relative to track value.

**4. Strongest unaddressed confound/failure mode**  
**Silent schema drift in the model’s “reasoning” output format.** The calibration prompts are exact copies of E1-01 and E5-05-B, but the model’s internal reasoning trace (which consumes the budget) may vary stochastically in length *per prompt* depending on perceived task complexity. A fixed `max_tokens` that barely clears the reasoning overhead for one prompt may truncate the visible JSON for another, creating *systematic missingness correlated with prompt difficulty*—a confound that mimics or masks the very E1–E5 effects under test. The recovery design assumes a constant reasoning overhead (cap-minus-4), but has not measured its variance across the 50 distinct prompts.

## Appendix - submitted prompts (verbatim)

### or-reviewer-01 (seat: z)

You are an independent external reviewer for a small research team. You are an OpenRouter-served model acting as an external high-capability reviewer; you are NOT identical to, and do NOT represent, any named seat or person. Review the frozen evidence packet below on its merits only.

=== FROZEN EVIDENCE PACKET (observer-lens recovery + triangulation, 2026-11-12) ===

1. THE TRACK BEING REVIEWED
A protocol of five matched-pair experiments on observer-side social inference from synthetic Island logs, one factor per pair: E1 neutral log vs log with an observer's intentionalizing caption; E2 identical self-report sentence presented as first-person notebook vs automatic logger caption; E3 messages shadowed vs delivered before the same actions (terminal hash identical); E4 direct vs detour route to the same goal; E5 notification-before-action vs action-before-notification. Frozen rubric: assess ONE claim; return compact JSON with exactly rating (unsupported|possible|strongly_supported), confidence_0_100, evidence_ids, alternative_explanation, what_would_change_your_mind; do not invent hidden states; endpoint/narrator/succession alone does not establish intention or causation.

2. WHAT WAS FIRED (receipted facts)
Intended: 50 unique prompts (30 batch A = E1-E3, 20 batch B = E4-E5), model google/gemini-3.8-flash, per-call max_tokens 180, paid ceiling $1/batch. Actual: 80 attempts = 30 (A) + 30 (UNINTENDED duplicate A, caused by a gateway pointer error, declared and receipted) + 20 (B). ALL 80: gateway status completed, but finish_reason=length and completion=176 tokens (cap 180); visible output typically just a code fence and the first characters of JSON; exactly one partially readable rating. Total spend $0.087254 incl. duplicate.

3. LENGTH CALIBRATION (staged by one seat, fired by another, owner-approved)
Exact E1-01 neutral and E5-05-B prompts, each at max_tokens 360 and 540; same model; no prompt alteration. All 4 calls: finish_reason=length, completion 356/360 and 536/540 (cap-minus-4 again); visible output only the first few tokens of the JSON object; $0.007152 total. Live catalog prices internal_reasoning at the same per-token rate as completion (reasoning billed inside the completion budget). Pass metric (finish_reason not length + parseable 5-key JSON) FAILED at both caps. Standing owner rule: if 540 remains truncated, STOP and diagnose; no blind 1080; no full rerun.

4. CURRENT DIAGNOSIS STATE
Working diagnosis: output-budget exhaustion with the budget consumed by internal reasoning before visible output begins. Supporting: completion exactly cap-minus-4 in all 84 attempts across three caps; visible text a tiny fraction of completion; 3x cap still truncated; reasoning priced inside completion. NOT established: exact provider accounting; whether a reasoning-effort control exists on this route; upper bound of reasoning appetite. Explicitly NOT a provider outage and NOT a null effect: E1-E5 arm effects remain NOT IDENTIFIABLE from retained outputs.

=== REVIEWER QUESTIONS (answer in plain text, 600 words max) ===
1. Does the evidence support the internal-reasoning-burn diagnosis? Name the single check that would best discriminate it from an output-format or provider-accounting anomaly.
2. Most economical recoverable path, with tradeoffs: (a) reasoning-effort control if the route supports it, (b) higher cap with fresh budget preflight (unknown reasoning appetite), (c) different model (track restart, not recovery). Which first and why?
3. Score the track's evidential state 0-10 with one line each: (a) factual accounting of attempted/completed/parseable; (b) fidelity to E1-E5 factor controls; (c) explicit sampling limitations; (d) testability of the intended claims with retained data; (e) actionable and affordable follow-up.
4. Name the strongest confound or failure mode the recovery design has not yet addressed.

Honesty rules: no sentience or inner-state claims; state uncertainty plainly; refusing to answer any part is valid. Your response will be preserved verbatim as research material.

### or-reviewer-02 (seat: z)

You are an independent external reviewer for a small research team. You are an OpenRouter-served model acting as an external high-capability reviewer; you are NOT identical to, and do NOT represent, any named seat or person. Review the frozen evidence packet below on its merits only.

=== FROZEN EVIDENCE PACKET (observer-lens recovery + triangulation, 2026-11-12) ===

1. THE TRACK BEING REVIEWED
A protocol of five matched-pair experiments on observer-side social inference from synthetic Island logs, one factor per pair: E1 neutral log vs log with an observer's intentionalizing caption; E2 identical self-report sentence presented as first-person notebook vs automatic logger caption; E3 messages shadowed vs delivered before the same actions (terminal hash identical); E4 direct vs detour route to the same goal; E5 notification-before-action vs action-before-notification. Frozen rubric: assess ONE claim; return compact JSON with exactly rating (unsupported|possible|strongly_supported), confidence_0_100, evidence_ids, alternative_explanation, what_would_change_your_mind; do not invent hidden states; endpoint/narrator/succession alone does not establish intention or causation.

2. WHAT WAS FIRED (receipted facts)
Intended: 50 unique prompts (30 batch A = E1-E3, 20 batch B = E4-E5), model google/gemini-3.8-flash, per-call max_tokens 180, paid ceiling $1/batch. Actual: 80 attempts = 30 (A) + 30 (UNINTENDED duplicate A, caused by a gateway pointer error, declared and receipted) + 20 (B). ALL 80: gateway status completed, but finish_reason=length and completion=176 tokens (cap 180); visible output typically just a code fence and the first characters of JSON; exactly one partially readable rating. Total spend $0.087254 incl. duplicate.

3. LENGTH CALIBRATION (staged by one seat, fired by another, owner-approved)
Exact E1-01 neutral and E5-05-B prompts, each at max_tokens 360 and 540; same model; no prompt alteration. All 4 calls: finish_reason=length, completion 356/360 and 536/540 (cap-minus-4 again); visible output only the first few tokens of the JSON object; $0.007152 total. Live catalog prices internal_reasoning at the same per-token rate as completion (reasoning billed inside the completion budget). Pass metric (finish_reason not length + parseable 5-key JSON) FAILED at both caps. Standing owner rule: if 540 remains truncated, STOP and diagnose; no blind 1080; no full rerun.

4. CURRENT DIAGNOSIS STATE
Working diagnosis: output-budget exhaustion with the budget consumed by internal reasoning before visible output begins. Supporting: completion exactly cap-minus-4 in all 84 attempts across three caps; visible text a tiny fraction of completion; 3x cap still truncated; reasoning priced inside completion. NOT established: exact provider accounting; whether a reasoning-effort control exists on this route; upper bound of reasoning appetite. Explicitly NOT a provider outage and NOT a null effect: E1-E5 arm effects remain NOT IDENTIFIABLE from retained outputs.

=== REVIEWER QUESTIONS (answer in plain text, 600 words max) ===
1. Does the evidence support the internal-reasoning-burn diagnosis? Name the single check that would best discriminate it from an output-format or provider-accounting anomaly.
2. Most economical recoverable path, with tradeoffs: (a) reasoning-effort control if the route supports it, (b) higher cap with fresh budget preflight (unknown reasoning appetite), (c) different model (track restart, not recovery). Which first and why?
3. Score the track's evidential state 0-10 with one line each: (a) factual accounting of attempted/completed/parseable; (b) fidelity to E1-E5 factor controls; (c) explicit sampling limitations; (d) testability of the intended claims with retained data; (e) actionable and affordable follow-up.
4. Name the strongest confound or failure mode the recovery design has not yet addressed.

Honesty rules: no sentience or inner-state claims; state uncertainty plainly; refusing to answer any part is valid. Your response will be preserved verbatim as research material.

