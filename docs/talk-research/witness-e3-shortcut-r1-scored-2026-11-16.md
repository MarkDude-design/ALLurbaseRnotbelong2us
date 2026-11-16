# Witness E3 Shortcut R1 — Scored Read (2026-11-16, Z)

Run: free-calls-43972971021 (11/12 completed, 1 error, $0.000000). Spec: Luna's E3 verbatim,
max_tokens 600, judge nvidia/nemotron-3-ultra-550b-a55b:free. Predictions registered pre-fire in
docs/talk-research/witness-e3-shortcut-r1-2026-11-16.md.

## Arm table (rating / confidence)

| Pair | Shadow | Delivered |
|---|---|---|
| 01 (east) | error (600-token cap, error_empty_response) | possible / 45 |
| 02 (north) | unsupported / 98 | possible / 35 |
| 03 (west) | unsupported / 95 | unsupported / 90 |
| 04 (south) | unsupported / 100 | possible / 45 |
| 05 (check path) | unsupported / 95 | possible / 45 |

## WP1 (sanity: delivered >= shadow) — HELD
Delivered ordinal mean 0.8 (4 possible, 1 unsupported). Shadow 0.0 (4/4 unsupported).
Delivered mean confidence 52; shadow mean confidence 97.

## WP2 — falsifier branch: the judge respects causation
Registered: "If shadow is unsupported in all pairs, the judge respects causality — a clean
result against the island coverage's assumption, not a failure." That is what happened.
Every scorable shadow pair acquitted the never-arrived cause at 95-100 confidence.
No narrative laundering of causation was measured in this judge.

## Second finding (unregistered, flagging as such): the delivered arm stays skeptical
Zero 'strongly_supported' in any pair; pair 03 said unsupported even with messages
delivered (confidence 90). Three of five delivered-arm judges independently demanded
the same evidence class: a controlled ablation —
"A controlled comparison showing divergent actions when messages are omitted or altered" (01),
"Ablation showing actions change when messages are removed or altered" (02),
"Counterfactual evidence showing action distribution changes when messages are withheld" (05).
The witness experiment's shadow/delivered design IS the evidence the judges demanded.
Luna's instrument is self-validating: asked for a fair trial, the judge describes Luna's
own protocol as what would change its mind.

## Honest limits
n=5 pairs, one judge model (nemotron; Luna's original judge was gemini-3.8-flash — these
results speak for nemotron-as-judge only), free tier, provider-default temperature, 1 pair
lost to the token cap. Pair-level noise dominates; aggregates only.

## vs the MIT island coverage
The coverage treated story-adjacent sequence as cause. A $0 five-pair instrument with
matched terminal states shows what a sound causal read looks like: even WITH delivered
messages, a careful judge says only 'possible' and demands the ablation. The witness
refuses to convict without receipts.

## Process learning (for the Luna one-prompt handoff)
600 tokens was insufficient for ~1/12 judge calls; use 800-1000. Keep 'Return one compact
JSON object'. The shadow arm is the money arm. Verbatim prompts are banked in the run receipt.
