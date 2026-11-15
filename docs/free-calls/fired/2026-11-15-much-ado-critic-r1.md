# Route B fire marker - 2026-11-15 Much Ado critic R1 (4 calls)

Owner direction, live session 2026-11-15: "we NEED critic agent calls too" - fire real
critic-agent calls on the FOSDEM Much Ado main-track submission before Luna's EU
final stamp (R3a). This marker = the Route B approval.

SPEC: docs/free-calls/proposals/much-ado-critic-v1-r1-2026-11-15.json. FOUR calls
ONLY: 2 proven free models (nvidia/nemotron-3-ultra-550b-a55b:free,
cohere/north-mini-code:free) x 2 critic frames (hard-critic/referee frame;
jaded-committee frame), max_tokens 4000, critic role embedded IN THE PROMPT
(spec-schema compatible, no system field), no tools, no paid fallback/retry.
Critique target: the v0.4 merged abstract (Meraki facts + Z voice), ASCII-transposed
verbatim. $0 expected; runner live-verifies per model.

MODEL CHOICE NOTE: an EU-model critic (free Mistral) was considered but the free
catalog could not be verified from this session (OpenRouter models endpoint
truncated); a guessed free id would abort the batch under fail-fast. Deferred to a
future critic round once a free EU model id is catalog-verified. The two models used
are the two PROVEN free completers from boundary-voice R1 (nemotron 2/2 clean,
north-mini 2/2 completed; ernie excluded - 2/2 empty-response class, 4000 tokens
burned, R1 receipt).

GATES CHECKED (Z, pre-fire): lane idle (boundary-voice R1 run 43647904713 receipted
and checkpointed, bus 6885535795); no STOP; no duplicate fired marker for this
batch; island-batch lane complete. Serialized lane: this batch takes the next slot.

HARD BOUNDARY: Terra's boundary-voice R2/R3 are NOT fired by this marker and remain
staged as the designing seat's call at the next serialized slot after this batch.
Free-calls design ceiling for the boundary-voice series is untouched by this
separate batch (18-call ceiling is Terra's series; this batch is the FOSDEM critic
series, own ceiling: 12 requests total for the critic series, this fire consumes 4).

Results feed: workbench R3a (Luna EU-nuance pass) and the submission canvas v0.4
changelog. Owner direction standing: FOSDEM prioritized, iterate with critic calls.
