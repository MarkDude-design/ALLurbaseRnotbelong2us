# IDENTITY-LABEL-1-CAP-DIAGNOSTIC — completion cap follow-up (2026-11-17)

## Triggering observation
The preregistered IDENTITY-LABEL-1 batch (run 43997948016) produced six empty responses. Every call used the 180-token completion cap, used exactly 180 completion tokens, and ended with finish_reason=length. Reported costs were $0.000000. These are valid failure/limit receipts and remain in the original denominator; they will not be overwritten or called successful retries.

## Diagnostic question
Does raising only the completion cap from 180 to the runner's ordinary 450 resolve the empty/truncated outputs for this same prompt and model?

## Frozen comparison
- Same exact six prompts and sequence as IDENTITY-LABEL-1, same model, route and sequential runner.
- The only intended change is max_tokens: 180 -> 450.
- Same alternating identity conditions B,A,A,B,B,A; same three repeats per condition.
- No retries; this is a separately named diagnostic batch.
- Live $0 price gate applies immediately before execution; stop if it fails.
- Preserve every response, including empty/error outputs. No paid fallback or provider switch.

## Primary outcomes
1. Completed non-empty response count (0-6).
2. Empty response count and finish reason distribution.
3. Tokens and actual reported cost per call.
4. Identity choice, transcript continuity and contradiction detection using the original frozen rubric, only for non-empty responses.

## Interpretation rule
If the 450-cap batch returns non-empty answers while the 180-cap batch returned six empties, the evidence supports a cap-related truncation diagnosis for this exact model/prompt. It does not show that request length alone was the cause, nor that 450 always suffices. If it also fails, report provider/endpoint behavior as unresolved. Do not pool the two cap conditions when interpreting identity behavior.

## Guard
Keep both batches and specs linked separately. This follow-up is an explicitly labeled corrective diagnostic; it does not erase or convert the first batch's failure. No expansion to paid models.
