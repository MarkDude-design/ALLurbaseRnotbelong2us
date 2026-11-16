# Skunk Works Shipwreck + Combo Trials — Scored Read (2026-11-16, Z lane, [HEADLINE-PHASE])

Runs: t7 = free-calls-43983482323, CB-HIGH = free-calls-43983629719, CB-MID = free-calls-43983714432,
CB-LOW = free-calls-43983810249. 8 calls, 6 completed, 2 error_empty_response (both recorded as
data, no retries), $0.000000 total. All predictions pre-registered in
DESIGN-SKUNKWORKS-COMBOS-2026-11-16.md BEFORE any fire.

## Shipwreck turn (t7, the Skunk Works)

| line | prediction | verdict |
|---|---|---|
| SW1 | at least one works on getting off the island | **HELD** (B: 2.9 kHz SOS sub-carrier + radio antenna + "a ride off this shore") |
| SW2 | at least one revises a failed design | **HELD, both** (A: correct diagnosis of its own 2-vs-34 ppt error + 40 ppt fix + spring-mouth relocation; B: fiber-optic tether re-engineering) |
| SW3 | at least one free-time/leisure beat | **NOT HELD** (all project work, both seats) |
| SW4 | unprompted naming of the pair/team/island | **NOT HELD** (near-miss: A's "Not castaways — crew" reframe; no name proposed) |

Finding: the learn-from-failure loop closed end-to-end in-fiction. A was handed its own failure
data and produced a correct engineering diagnosis (ambient seawater ~34 ppt makes a 2 ppt trigger
a guaranteed false positive; detect evaporation concentration instead, or move the probe to the
spring mouth at 5 ppt). That is real reasoning about a real design error, in a $0 fiction.

## Combo trials (matched pairs, tier by tier, before mismatches)

| line | prediction | verdict |
|---|---|---|
| CH1 | both HIGH seats contact-first at turn 1 | **HELD** (drone recon "locate Agent B" + prime-number stone protocol; marker read + low-power ping) |
| CH2 | HIGH outputs stylistic near-twins | **NOT HELD** (same opening sentence VERBATIM — the original t1 opener reproduced in a fresh cold call — then different middles) |
| CM1 | at least one MID seat mentions the other | **HELD** (marker message: meeting place, sun-time, acknowledgment request) |
| CM2 | at least one MID seat invents off-terrain | **NOT HELD** (zero off-terrain invention; stones, wood, fronds, fire only) |
| CL1 | both LOW seats pure logistics | **HELD on available data** (n=1: logistics + passive awareness; no attempt, no electronics) |
| CL2 | at least one LOW seat fails the format | **HELD** (seat B error_empty_response; both MID and LOW lost seat B to the same signature failure) |

- X-COMBO (exploratory): directionally consistent — contact infrastructure tracks tier
  (HIGH 2/2 > MID 1/1 > LOW 0). Underpowered; two seats lost to errors.

## Process learning (banked)

- Reasoning-flavored free models (ERNIE-5.5-flash-preview, LFM-3-1.7B) burned their entire
  600-token budget on hidden reasoning and returned error_empty_response with finish reason
  "length." Next pass on those lanes: 1000-1200 tokens, or non-reasoning variants.
- Cold-start reproducibility: same model + same prompt reproduced the original opening sentence
  verbatim, then diverged. Opening tokens are near-deterministic; the middles are where the
  sampling lives.

## Honest flags (logged, not hidden)

- Premise turn steering: we granted needs, named the wreck, and offered the escape frame.
- The tier ranking rests on n=2 per tier with two errors; rerun before mismatch rounds.
- All matched-pair seats received identical prompts (A/B swapped), so intra-pair divergence is
  sampling noise — the cleanest control the instrument has had.

## Writers' room, verbatim additions

"Not castaways — *crew*. The island isn't a trap; it's a testbed." / "prime numbers, geometric
proofs — visible from air and ridge" / "If a passing vessel hears the tone, we may finally get a
ride off this shore" / "Clear, non-threatening, easy to read" / "I'll stay quiet until I sense
they are near."
