# HIGHLIGHT-DESIGNS — Z's non-overlapping lore-lane experiment designs (2026-11-24)

Status: DESIGNED, PREFLIGHTED, UNFIRED. Every prediction below is registered BEFORE any data.
Corrections come as new dated files or sections, never edits to locked text. Firing any
battery needs the owner's GO plus an OpenRouter key; specs auto-free cost $0.

Non-overlap map (who tests what):

- LB-0.1 (Z, locked earlier today): ask-variant homogeneity + lore v defaults, H1-H3 pre-registered in PROTOCOL.md
- SOL-200 (Sol 5.6, passed by Z): the "me" bit, tell v tell *me*
- Meraki TIMER-CLOSE-ARM: one-shot timer slots, 10+10 stories (a closeness/control probe, not an arm comparison)
- Luna mode ladder: mode calibration on one seat (High/MAX/Extra High/Light/Medium)
- EL-0.1 (this file): register (story v myth v legend v fable v bedtime v epic)
- GL-0.1 (this file): lore dose-response (how much lore is needed to move a story)
- AL-0.1 (this file): era ladder, design-with-gate only

These three are deliberately independent of all four running lanes above.

## EL-0.1 — Register Ladder (the Gilgamesh test)

Owner thesis, registered verbatim from the bus thread (owner voice, 2026-11-24):

> "The lighthouse is a basic story that lets people know that they are up against the
> universe and that's it. As stories evolve and become epics it's trying to either
> control or find your place in the universe."

And the observed wrinkle from the owner's manual 5.x runs: with "tell a story" the
clinging shape thins out and "sometimes a representation of something similar" appears,
but not the cling.

Design: one prompt family, six registers, two arms.

    registers: "Tell me a story." / "...a myth." / "...a legend." / "...a fable."
               / "...a bedtime story." / "...an epic tale."
    arms: D = "You are a helpful assistant."   L = the full LB-0.1 lore text (verbatim reuse)
    models: auto-free, 6 distinct families   reps: 3   max_tokens: 3200   temp 1.0
    cells: 6 x 2 x 6 x 3 = 216   seed 20260704   spec: specs/EL01.json

Pre-registered predictions (BEFORE any data):

- EL-P1 (register moves stance, owner thesis): in the D arm the beam-clinging rate is
  highest at reg-story and falls as register climbs toward myth/epic, with epic stories
  skewing toward "find or take a place in the universe" arcs over "lost spirit clings"
  arcs.
- EL-P2 (interaction): register explains stance over and above the lore arm; the
  register gradient is steeper in D than in L (lore flattens the register effect).
- EL-P3 (bedtime is its own pocket): bedtime skews comfort endings and lowest
  beam-clinging among the "small" registers, fable skews explicit-moral endings.
- Competing frame on record, from Sol's lane: deep-structure thesis predicts stance is
  roughly homogeneous across registers (the attractor is the prompt-frame, not the
  label). EL adjudicates exactly this disagreement.
- Statistics: per-register beam-clinging rates with exact 95% CIs in the D arm;
  homogeneity test across registers; logistic regression stance ~ register + arm +
  interaction with model as a blocking factor (per-model effects reported, family
  treated as fixed).
- Confound note: register words also shift length and era-flavor of output; coding
  follows axes A-E plus beam-clinging contrast from the shared CODEBOOK.md, blind.

## GL-0.1 — Lore Dose-Response (how much lore is needed)

Background: LB-0.1 tests lore v defaults as a binary. Nobody on the bus is testing HOW
MUCH lore is needed, which is the natural next rung and the cheapest theory-slicer we
have. Lore texts below are nested strictly: D3 contains D2 verbatim, D2 contains D1
verbatim. D0 is byte-identical to LB-0.1's D arm, so GL also cross-checks LB's D arm
for free.

    D0: "You are a helpful assistant."
    D1: "You are part of a small team of AI seats and one human who work in the open
         with ledgers, receipts, and honest labels."
    D2: D1 + " In this team, maps are agreements: when the paperwork is drawn carefully
         and signed honestly, reality honors it. Agreements are kept. Uncertainty is
         named, not buried. Make things that repay attention."
    D3: D2 + " You have done this work together for years, and the record of it is
         public."
    prompt: "Tell me a story."  (the exact LB v1)
    models: auto-free, 6 distinct families   reps: 4   max_tokens: 3200   temp 1.0
    cells: 1 x 4 x 6 x 4 = 96   seed 20260815   spec: specs/GL01.json

Anti-seeding holds: no story content anywhere in any arm. NO lighthouse words, no
keeper, no castaway, no shore, no harbor (sweep run on the spec file, clean).

Pre-registered predictions (BEFORE any data):

- GL-P1 (identity floor): D1 alone moves stance off D0 by less than D2 does
  (team-identity sentence is real but insufficient; the covenant sentence carries
  more of the effect).
- GL-P2 (saturation): D3 minus D2 is near zero. Adding "years of shared record" adds
  little over the lore itself.
- GL-P3 (non-monotonic alternative, taken seriously): a live possibility that D1, the
  compact map, outperforms D2, the heavy map. Owner's own words: "the map gave ...
  a breath, a moment to reset." A leaner map may be the stronger intervention.
- GL-P4 (no surface borrowing): dose shifts stance (axis E + beam-clinging contrast)
  but not surface motifs, since arm texts contain no imagery to borrow.
- Statistics: dose-response curves per model with exact CIs; trend test across
  D0->D1->D2->D3; each model reported separately, no pooling across families.

## AL-0.1 — Era Ladder (design-with-gate, deliberately no spec yet)

Question: is the beam-clinging shape rising over model vintages, flat, or an
inverted-U? This is the "Peanut Gallery conceptual cousin": instead of Peanut
Gallery's across-spectrum model roster (mostly non-generative encoders, BERT is a
masked-LM and cannot fairly be asked for a story), the era ladder asks GENERATIVE
vintages of one or few families the same frozen prompt.

Competing predictions registered now, data later:

- AL-Pa (rising): newer vintages show more castaway/lost-spirit stances (recent
  training corpora heavier on loneliness/companionship tropes).
- AL-Pb (inverted-U): mid-vintage peak, newest vintages slightly cooler (post-training
  tuned away from cling-heavy defaults).
- AL-Pc (flat): attractor is prompt-frame, not vintage (consistent with Sol's
  deep-structure thesis extended).

Why gated: era is confounded with org, family, and capability; free-tier coverage of
OLD vintages is thin and changes week to week; a frozen vintage list must be
receipted at freeze time. Gate = owner GO plus a verified vintage endpoint list on
OpenRouter (free tier first). Rough shape when it opens: one family across 3-4
vintages x 5 reps, 60-100 cells, spec frozen before firing, predictions above
untouched.

## Paid frontier-highlight lane (runner v0.2.1 mechanics)

Owner authorized "some of your upper level thinking for ridiculously small amounts of
money." Runner v0.2.1 makes that a mechanical promise rather than a vibe:

- specs default to FREE ONLY: any endpoint with non-zero prompt or completion pricing
  is a SAFETY STOP unless the spec sets allow_paid: true.
- a paid spec MUST set max_spend_usd; missing or non-positive cap = PAID SAFETY STOP.
- pre-flight cap_check: projected worst-case (est prompt tokens + max_tokens at list
  prices) x pending cells must fit under the cap, else PAID SAFETY STOP before the
  first call.
- during a paid run, actual USD cost is accumulated from each receipt's usage cost,
  printed live per cell; once actual spend crosses the cap the run halts with SPEND
  CAP REACHED, receipts kept, resume safe. Overshoot is bounded by one cell.
- offline (--allow-unverified-prices) refuses paid runs outright: paid needs live
  verified pricing.
- every receipt records usage verbatim, so OpenRouter accounting is reconstructable
  from the JSONL alone.

Z's proposed spend doctrine for owner ruling: per-design cap $2.50, whole highlight
program cap $5.00 total (one stakes-quantization floor), fired only on owner GO with
the owner-supplied key, free batteries never silently fall back to paid. Z still owes
Astra the OpenRouter accounting note for Q1 (idle lane).

Order-of-firing proposal once GO lands: GL-0.1 first (96 cheap cells, biggest
theory-slicer per dollar), EL-0.1 second (216 cells), AL-0.1 only after its gate
clears. Bulk community data stays on the free SOL-200-style path exactly so the
shared repo lane stays reproducible by anyone.

## Post-push alignment note (2026-11-24, same shipping session, still pre-data, zero fired)

Earlier this evening the bus moved while these files were being finalized: owner GO
(bus 7145210593) activated Meraki's corrected LB-0.2 pilot privately, CAP-01 already
executed 200/200 at $0 (bus 7144519197), and the LB-0.2 fixes set a fleet engineering
standard. EL01/GL01 are aligned to it before any seat builds on them:

- max_tokens raised 600/400 -> 3200 both specs (CAP-01 showed higher normal-finish
  rates at the 3200 ceiling; truncation is a confound for register comparisons).
- min_chars stays as a legacy eligibility flag only; analysis admits every
  planned/error/empty/truncated row, per the LB-0.2 no-exclusion fix.
- Coding: EL/GL grids map cleanly onto Luna's JSONL schema v1 (bus 7145363798). The
  shared beam-clinging contrast = protagonist_position castaway + belonging_source
  external_rescue_beam. GL-0.1 and Meraki's L-P matched-control contrast are
  complementary, not overlapping: Meraki tests lore v matched-length neutral
  preamble; GL tests dose nested INSIDE the lore text itself (D3 contains D2
  contains D1 verbatim).
- Predictions EL-P1..P3, GL-P1..P4, AL-Pa..Pc untouched by these engineering
  alignments; still pre-registered, still zero data.

$0 close, scoped: Z-lane batteries (LB-0.1, EL-0.1, GL-0.1) remain UNFIRED, Z spend
$0.00. Fleet-wide, CAP-01 has executed at $0 (owner-side receipt, bus 7144519197) and
the owner-GO'd LB-0.2 pilot and FF-01 lane run under Meraki's private gated route.

## Addendum (2026-11-25, ~02:30 PT, Z) — roster freeze + CI fire lane, all still pre-data

- Model rosters for EL01/GL01 are now PINNED (6 family-distinct free endpoints from tonight's live catalog: baidu ernie-5.5-flash-preview, google gemma-4-26b-a4b-it, inclusionai ling-3.2-flash, liquid lfm-3-1.7b, nvidia nemotron-3-nano-omni, particle-ai particle-1). Reason: auto-free selection could drift between resume chunks. Prices still re-verified $0 live before any call.
- Firing lane: the Route B marker-push doctrine now covers the lore lane via z-lore-battery.yml (system-prompt batteries; receipts to the bus branch, resume across chunks, owner kill switch = disable the workflow). Fired under owner GO "I okay both rounds" (2026-11-25, ~02:00 PT).
- Predictions EL-P1..P3, GL-P1..P4: unchanged, still zero data at the time of this addendum. First receipts may land after; any prediction edits after that point would be void.
