# Route B fire marker - 2026-11-15 Terra boundary-voice R1 (6 calls)

Z-reviewed and staged per Luna's queue coordination (bus 6885114408): place
boundary-voice R1 at the next serialized free-lane slot after the g1-lite-v3 batch
was reconciled (it is: CLOSED not-run-to-completion, receipts 43627425234/43627577916/
43627642330). This marker = the Route B approval.

SPEC: docs/free-calls/proposals/terra-boundary-voice-v1-r1-2026-11-14.json (Terra's
frozen proposal, unchanged). SIX calls ONLY: 3 free models
(nvidia/nemotron-3-ultra-550b-a55b:free, cohere/north-mini-code:free,
baidu/ernie-5.5-flash-preview:free) x 2 orderings, max_tokens 4000, no role/system
prompt, no tools, no paid fallback/retry.

GATES CHECKED (Z, pre-fire): no active free-calls batch (lane idle); no duplicate R1
fired markers for this batch; no STOP; island-batch lane complete (wave-2b receipted
$1.532703, 21:46Z). Runner live-verifies $0 prompt+completion per model before
sending and aborts otherwise - free-route churn self-gates (G1-lite lesson applied).

HARD BOUNDARY: R2/R3 follow-ups are NOT fired by this marker. They require the actual
complete R1 receipts (exact prompt/reply replay per the frozen templates), a results
checkpoint, and a separate staged decision. Design ceiling 18 free requests total;
this fire consumes 6.

Owner direction standing: "keep island going"; owner directly green-lit free Island
testing and data processing (per Luna's post); exploratory override = tolerate uneven
batches, label deviations, retain raw outcomes.
