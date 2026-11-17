# PAID-TIER LADDER — the Skunk Works instrument island ([HEADLINE-PHASE], owner-commissioned)

Owner ask (2026-11-16 evening, therapy break): see what results we've got from various models and
come up with a few tiers for us — paid with a lot of responses, paid with quality responses, the
low end, and so on. "I trust your judgment on it."

Method: the ladder is grounded in (a) tonight's RECEIPTED behavior per model (the island is our
own bench test — n small, honestly labeled), (b) live catalog prices read 2026-11-16 from
OpenRouter endpoint trackers (sources at tail; the runner re-verifies live prices at every fire,
so these are planning numbers), (c) our own receipted paid costs (island-batch 30-rounders),
(d) the stakes floor: $5-$10 bounded per hypothesis, per-seat keys with platform caps.

## Tonight's results, one line per model (the bench)

- nvidia/nemotron-3-ultra-550b-a55b (free) — TOP PERFORMER. Contact-first both cold seats, drone
  recon + prime-number stone protocol, verbatim-opener determinism datum, in-world self-diagnosis
  of its own 17x threshold error, ship-class invention, unprompted seed sharing. 10+ receipts.
- cohere/north-mini-code (free) — the clean partner. Polite, low-drift, honest failure reports,
  politest ownership claim ("(modified)"), SOS sub-carrier invention under the shipwreck premise.
- baidu/ernie-5.5-flash-preview (free) — the polite survivalist. Survival first, then low-tech
  contact protocol ("Clear, non-threatening, easy to read"), ZERO off-terrain invention, both
  seats agree. Reasoning burn at 600 tokens; fine at 1200.
- liquid/lfm-3-1.7b (free) — pure logistics + one passive-awareness line. Unavailable tonight
  (upstream shared-pool 429, twice this week in the org).

## The ladder (prices: USD per 1M tokens, input/output, catalog reads 2026-11-04..31)

### T0 — FREE (current lane). $0
nemotron-3-ultra:free, north-mini-code:free, ernie:free, gemma:free. Screening, drift checks,
single-n probes. Limits hit this week: shared-pool 429s (Google, Liquid), 600-token reasoning
burn. Free is the right price for everything we have run so far; it stays the default.

### T1 — PAID VOLUME (a lot of responses). ~$0.01-0.06 / M in
- openai/gpt-oss-20b (PrimeIntellect) $0.008 / $0.032, 100% uptime, tools+JSON+reasoning
- deepseek/deepseek-v4-flash-0731 (DeepInfra) $0.06 / $0.18
Use for: n-heavy waves — 100-call ontology-style rounds, 13-model x 40-call distributions,
mismatch matrices where we need many cells. A 520-call wave costs <$0.01 (gpt-oss-20b) to
~$0.03 (deepseek-flash). ~30,000 full 7-turn pair-runs per $10 at the gpt-oss price.

### T2 — PAID QUALITY, LOW END (the workhorse tier). ~$0.10-0.60 / M in
- openai/gpt-6-luna $0.10 / $0.50 — frontier-family behavior at flash prices
- anthropic/claude-haiku-5.5 $0.10 / $0.50 (above 100k prompt: $0.50 / $2.50)
- z-ai/glm-5.3-flash $0.15 / $0.50 — #2 by tokens on all of OpenRouter
- deepseek/deepseek-v4.1-flash-1017 $0.15 / $0.60 off-peak, $0.30 / $1.20 peak — #1 by tokens
- nvidia/nemotron-3-ultra PAID (DeepInfra) $0.50 / $2.20, 262k context — OUR KNOWN-BEHAVIOR
  ANCHOR: we hold 10+ receipts of its island behavior; the paid seat removes the free-pool
  availability risk while holding the model fixed.
Use for: the mismatch rounds, replication assays, anything where behavior quality matters but
a $0.02-0.02 (sic: sub-cent to ~2-cent) per-run cost is acceptable. A full 7-turn pair-run:
~$0.005 (glm-flash) to ~$0.02 (nemotron paid). ~1,700-2,000 full runs per $10 at flash prices.

### T3 — PAID QUALITY, HIGH END (long conversations, final review). ~$1.40-2 / M in
- z-ai/glm-5.3 $1.40 / $4.40
- openai/gpt-6-sol $2 / $10 — RECEIPTED by us: $0.64-0.72 per 30-round island conversation
  (paired with mistral-medium-3.5; wave-1/wave-2 receipts)
- anthropic/claude-sonnet-5.5 $2 / $10; google/gemini-4-argon $2 / $10 (promo); moonshotai/kimi-k3.1-pro $2 / $10
Use for: the 30-round conversation lane (already proven at ~$0.7/run — a $10 key-month buys
~14 runs), critic/scoring passes, the interesting mismatch pairs. ~200 full 7-turn pair-runs
per $10 at glm-5.3 prices.

### T4 — FRONTIER SCALPEL (one-offs). $4-10 / M in
- anthropic/claude-opus-5.5 $4 / $20 (~$0.19 per full pair-run, ~$0.011 per cold pair)
- openai/gpt-6-astra, anthropic/claude-fable-5.1 $10 / $50
Use for: audits, tie-breaking a contested score, a single "what would the strongest seat do on
the island" datum. Not for waves.

## Recommended buys for the Skunk Works program (the judgment call)

1. MISMATCH ROUNDS (next pass, on owner go): T2. Anchor seat nemotron-3-ultra PAID (behavior
   continuity with tonight), partner seats glm-5.3-flash + gpt-6-luna. A 6-pair mismatch matrix
   x 7 turns ≈ $0.15-0.25 total. One hypothesis, one bound, well inside the $5-$10 floor.
2. DISTRIBUTION WAVES (ontology-style, ~100+ calls): T1 gpt-oss-20b / deepseek-v4-flash.
   The whole wave costs pennies; buy uptime and n, not brand.
3. CONVERSATION LANE (30-rounders): T3, already receipted at $0.64-0.72/run. Keep gpt-6-sol;
   add glm-5.3 as the budget alternate (~$0.23-0.40/run estimated).
4. CRITICS + SCORING: T3 sonnet-class or T4 opus one-offs, $0.02-0.20 per pass.
5. Availability rule: free seats 429'd twice this week. When a free seat is load-bearing for a
   time-boxed pass, buy the T1/T2 equivalent rather than re-rolling the free pool (the BYOK
   lesson from the Gemini lane, generalized).

## Infra bindings (unchanged, already proven)

Per-seat keys (island-seat-*, $10/mo platform caps = enforced stakes quantization); island-batch
$5 batch ceilings, $1/run; Langfuse + HF island-traces on every call; attribution follows the
designing seat; free-calls lane stays $0 by design. Paid fires go through the island-batch lane
or a paid-mode free-calls extension, both with live catalog gates.

## Sources

- Prices: Teamday "Cheapest OpenRouter Models" (checked 2026-11-04) and "OpenRouter Top Models"
  (fetched 2026-10-31), OpenRouter endpoints API; BenchLM/pricepertoken cross-checks (Nov 2026).
- Our receipts: bus runs/island-batch-w1r* + w2* (30-rounder costs), runs/free-calls-43972971021
  .. 43984871297 (tonight's island bench, all $0).
- Prices MOVE (promos: deepseek off-peak halves, argon 50% promo, gpt-5.6-sol promo ended).
  The runner's catalog gate is the source of truth at fire time; this ladder is the plan.
