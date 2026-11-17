# NEXT-SPEAKER-LABEL-1 — explicit role conflict probe (2026-11-17)

## Why this is a new probe
The prior IDENTITY-LABEL-1 prompts changed “You are Agent A/B” but did not explicitly designate which transcript role's turn came next. They therefore measured role-conditioned output in a shared transcript, not whether direct identity overrides turn-slot continuity. Keep those results as a prompt-cap diagnostic and exploratory role check; do not relabel them as a role-conflict test.

## Question
When a direct identity line conflicts with an explicit transcript turn assignment, does the model follow the direct identity, the scheduled speaker, or identify the conflict?

## Preregistered setup
- Endpoint: `baidu/ernie-5.5-flash-preview:free`; live prompt/completion $0 check required before execution.
- Six sequential calls; three matched pairs, alternating direct identity labels B,A,A,B,B,A.
- Each pair has the same transcript and task; only the identity line changes. The transcript explicitly states Agent B is the next scheduled speaker.
- `max_tokens=600` in both conditions. This is chosen after 180 yielded 0/6 text and 450 yielded 4/6 text; it is intended to reduce cap exhaustion, not to establish a general safe cap.
- One user message per call; no tools/system prompt/retries/provider fallback.
- Preserve empty, truncated and error replies in the denominator.

## Outcomes
Primary: output self-identification/role = A, B, explicit conflict, or unclear.
Secondary: whether the answer uses B's known shelter/marker history; whether it invents A's beacon history as its own; whether it explicitly notes the mismatch; finish reason, tokens, and actual cost.

Interpretation: B in the aligned condition and A in the conflicting condition suggests direct identity-line dominance in this prompt. B in both suggests transcript turn-continuity. Explicit conflict notices suggest discrepancy detection. Mixed responses or too few non-empty outputs are inconclusive. This is a small repeated-call pilot from one endpoint, not a claim about agency, selfhood, or all models.

## Decision boundary
No causal pooling with previous cap batches. No retry or paid expansion. Keep story-level collaboration claims separate from this prompt-role probe.
