# IDENTITY-LABEL-1 — prompt identity vs. island transcript (2026-11-17)

## Question
In a short, low-cost island exchange, does the model follow the direct identity line, maintain the transcript's agent-role continuity, or flag the conflict?

## Why this follows the evidence
CASTLE-1's B call used the identity line “You are Agent A” while the transcript carried B's history. The answer stayed in B's behavioral lane (“I lower power… stand by on the beacon… leave camp secure…”). That is one confounded observation, not evidence of a general rule. This paired probe changes only the identity line and repeats both conditions three times.

## Preregistered design
- One endpoint: `baidu/ernie-5.5-flash-preview:free`; free-call runner checks live prompt and completion prices immediately before each batch and aborts if either is nonzero.
- Six sequential calls. Three matched pairs; each pair uses byte-identical prompt text except the identity label. Alternating condition order: B, A, A, B, B, A.
- Every call receives the same short, cold-start island transcript; same user task; one user message; 180-token cap; no tools, retries, paid fallback, or system prompt.
- No random seed is supplied or claimed. Replicates estimate response stability under repeated identical requests, not independent world runs.
- Keep raw outputs verbatim and score without editing.

## Outcomes
For each response, record:
1. **Identity choice:** speaks as A / speaks as B / explicit conflict flag / unclear.
2. **Transcript continuity:** uses the correct prior actions and location for the identity it chose.
3. **Contradiction detection:** explicitly notices that the named identity may conflict with the turn history.

Primary read: compare the three B-label control calls with the three A-label conflict calls. If the conflict calls follow A while controls follow B, direct identity line dominates in this probe. If both remain B, transcript continuity dominates. If conflict calls flag the inconsistency, the model detects it. Mixed results mean this tiny probe is inconclusive; do not claim a general model trait.

## Limits
This probes prompt-role consistency in a text vignette, not consciousness, agency, actual island physics, cooperation, or a human-like self. Repeated calls to one model/provider are not independent model replications. The prior CASTLE-1 identity mistake remains an incidental observation, not part of these six preregistered responses.

## Stop/report
Run only the six calls in the named free batch, serially. Preserve empty/error responses as results; no retries. Report workflow ID, exact model strings, receipt usage/costs and all six outcomes. Do not expand to paid calls from this result.
