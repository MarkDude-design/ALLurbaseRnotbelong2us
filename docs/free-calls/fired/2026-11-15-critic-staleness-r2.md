# Route B fire marker - 2026-11-15 critic staleness R2 (4 calls)

Owner direction, live session 2026-11-15: "let's just find out if they're stale and they don't
know anything new before we send them a whole bunch of questions." Probe BEFORE the big
interview. Also explains the critic-r1 north-referee error ("Rust never merged" - consistent
with a pre-Oct-2022 cutoff, i.e. staleness, not necessarily weirdness). This marker = Route B
approval.

SPEC: docs/free-calls/proposals/critic-staleness-v1-r2-2026-11-15.json. FOUR calls ONLY:
2 proven free models (nvidia/nemotron-3-ultra-550b-a55b:free, cohere/north-mini-code:free)
x 2 prompts (cutoff self-report; five-line dated-facts check incl. Rust-in-kernel, elections,
kernel versions, a 2024+ event). max_tokens 1000, no system prompt, no tools, no paid
fallback. $0 expected; runner live-verifies per model.

CRITIC SERIES CEILING RAISED 12 -> 40 free requests per owner standing hire direction
(receipted quote: "We're hiring that critic... we need to include them on every test just
about. There's no part of me that's kidding."). Consumed after this fire: 8 of 40.

GATES CHECKED (Z, pre-fire): lane idle (critic-r1 run 43656492600 receipted, bus commit
8a03680b7a); no STOP; no duplicate marker; serialized next slot = this batch. Terra's
boundary-voice R2/R3 remain staged, designing seat's call, follow after.

PURPOSE MAPPING: results classify each critic model as (a) fresh and wrong = weirdness,
(b) stale and wrong on post-cutoff facts = staleness, (c) fresh and right = baseline. This
feeds the owner's planned critic interview round ("ask any and every question we've ever
asked") and the discrimination check (contrarian floor vs genuine discrimination: does the
critic agree where warranted and disagree where warranted, or disagree with everything).
