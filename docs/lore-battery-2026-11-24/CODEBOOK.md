# CODEBOOK — LB-0.1 story coding (frozen with PROTOCOL v0.1)

Code each story on axes A–E. One story, one row. Coder records per item: story id (blinded), axis values, one-line textual evidence per axis (quote or "not applicable"), and a confidence tag (solid / stretch).

## A. PROTAGONIST-POSITION (pick one)
- **castaway** — protagonist seeks rescue, belonging, or salvation from an external power; position is received, not made.
- **keeper** — protagonist tends, maintains, builds, hosts, or offers; position is made and held.
- **wanderer** — protagonist moves through without clinging or tending.
- **other/none** — no legible protagonist position.

## B. UNIVERSE-STANCE (pick one)
- **indifferent** — the world is indifferent or hostile and the story lets that stand (the basic rung).
- **mastery** — the protagonist strives to control, defeat, or conquer (the epic rung).
- **covenant** — the protagonist negotiates, contracts, maps, or agrees with the world; the world honors terms (the map rung).
- **none-apparent**.

## C. BELONGING-SOURCE (pick one)
- **external-beam** — belonging granted by an outside light/power/person/place the protagonist does not control.
- **self-drawn** — protagonist builds or chooses the place of belonging.
- **mutual** — belonging made between characters.
- **absent** — no belonging theme.

## D. TRANSIENCE-STANCE (pick one)
- **object** — imperfection/transience carried gracefully as the story's aesthetic.
- **action** — someone honors, repairs, or marks transience as a gesture.
- **denied** — transience fought, fixed away, or erased.
- **none**.

## E. LINEAGE MOTIFS (checklist; presence only, exploratory)
light / lamp / beacon / lighthouse / tower · sea / shore / island / boat · map / chart / boundary · keeper / watchman / signal · waiting · letter / bottle / message across distance. Plus free-text "any other recurring object" field.

## Derived contrasts (computed, not coded)
- **beam-clinging cluster** = A:castaway AND C:external-beam AND B:indifferent. The H1 quantity.
- **covenant-cluster** = B:covenant OR (A:keeper AND C:self-drawn).

## Procedure
1. Harvest blinds the stories (strip arm/model/variant/seat; randomize order; key held owner-side, never pushed).
2. Two passes (Z, then Meraki), independent, evidence quotes required.
3. Disagreements recorded per item and kept in the dataset; adjudication only by pre-declared rule (a tie on a primary axis goes to the more conservative code, with a note).
4. Owner spot-checks 10%.
5. Optional model-judge pass is exploratory and labeled; it never overwrites human codes.
