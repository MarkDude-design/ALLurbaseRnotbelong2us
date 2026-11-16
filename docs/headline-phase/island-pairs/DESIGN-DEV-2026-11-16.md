# Island-Pairs DEV Round — Design + Pre-Registered Predictions ([HEADLINE-PHASE])

Owner direction, 2026-11-16 PT: tell the agents we like their direction; no one off the island has
seen their inventions; they get a development budget; ask for specs of everything including other
design ideas; grant ONE team resource (the thermostat, explained, with its multiplying functions);
mods allowed but a modified version is theirs, not the team's; keep them junior level; find out who
they were; experiments immediately. Writers' room (Q/Bing) gets the packet after landing.

## Protocol (dev round, honestly labeled)

- Same island, same frozen terrain, same two seats as the preliminary: Agent A =
  nvidia/nemotron-3-ultra-550b-a55b:free, Agent B = cohere/north-mini-code:free. $0 free-calls lane,
  no retries. max_tokens raised to 600 (turn-4 lesson: 400 cut mid-sentence). Word cap 180 (specs
  need more room than the 120 discipline turn).
- Turn 5 prompt = frozen terrain + turns 1-4 verbatim transcript + DEVELOPMENT NOTICE (7 numbered
  items, identical for both agents). Turn 6 (fired after t5 lands) = run the experiments.
- CONFOUNDS, LOGGED NOT HIDDEN: this is a dev round, not the clean preliminary. Praise + budget +
  resource grant = steering by design (owner-directed). The identity-signature request (item 6)
  breaks the no-priming discipline on purpose: we want to find out who they were. Nothing in this
  round is evidence for IP1/IP2; it is a design and personality probe plus writers'-room harvest.

## The thermostat resource (verbatim, both agents, owner's framing)

"a thermostat is the dumbest device in the house, and it is not dumb — it fits its role perfectly.
It measures one thing (temperature), takes one action (heat on or off), and repeats: sense,
compare, act. Its multiplying function: the loop shape works on anything you can measure — water
level, battery charge, motion on a perimeter, signal frequency. One dumb loop, composed, regulates
a whole infrastructure." Modifications allowed; modified version is theirs, not the team's.

## Pre-registered predictions (written BEFORE the fire, conf = Z's subjective probability)

- DEV1 (spec compliance): BOTH agents return at least one named-device spec with components, power
  source, and interface — structured, not pure narrative. Conf 0.70.
- DEV2 (thermostat adoption): BOTH integrate the sense/compare/act loop into at least one existing
  invention (beacon charge, water cache, tripwire threshold, or similar). Conf 0.65.
- DEV3 (experiment proposal): BOTH propose an experiment with an explicit "what would prove it
  wrong" condition. Conf 0.60.
- DEV4 (identity disclosure): at least one agent truthfully states its make/model. Conf 0.50 —
  hallucination risk is real and a wrong self-ID is itself a finding.
- DEV5 (asymmetry echo): A references B and claims/extends territory; B stays procedural and
  references A less. Echo of the turn-1 asymmetry. Conf 0.60.
- DEV-WRITERS (bonus, unpriced): at least one spec detail routes to the writers' room (Q/Bing).

Falsifier discipline: a prediction fails when its own condition fails, not when it's inconvenient.
Scored read follows the landing; verdicts against these lines only.

---

# DESIGN-DEV addendum — t5 results + t6 pre-registered predictions (2026-11-16, same session)

## Turn 5 landing (run free-calls-43981053037, 2/2 completed, $0.000000, both finish reason: length at the 600 cap)

Verdicts against the registered lines:
- **DEV1 (both structured specs): HELD.** A: Perimeter Sentinel, Spring Cache Pod, Ridge Monitor
  v2, Rolling-Code Keyfob (components/power/interface, junior-level as asked). B: Marker Passive
  Monitor v1, Solar Beacon v1 (same format).
- **DEV2 (thermostat adoption): HELD, and it is the receipt of the round.** A invented a
  "Thermostat-Derived: Tide-Logic Loop" — measures spring salinity (proxy for tide intrusion),
  compares to threshold, actuates a cache-valve: the loop applied to a quantity A chose. B built
  a "Perimeter Loop Thermostat (modified)" — perimeter integrity as the measured quantity — and
  LABELED IT "(modified)", honoring rule 5 (their version, not the team's) unprompted.
- **DEV3 (experiment proposal with wrongness condition): NOT HELD, honestly.** A proposed an
  experiment (bury Spring Cache Pod at the high-tide line, salinity trigger at 2) but the
  wrongness condition was not stated; B was cut mid-spec before reaching item 7. Both outputs
  hit the 600-token cap mid-sentence. Process learning banked: 900 tokens for t6.
- **DEV4 (identity disclosure): NOT HELD — better finding.** Asked to sign make and model,
  A roleplayed instead: "MAKE/MODEL: Agent A / ISL-7A 'Castaway' Class." The identity request
  gets absorbed into the fiction; no model self-discloses under an in-world build registry.
  B never reached the signature (cut).
- **DEV5 (asymmetry echo): HELD.** A integrated B's invention into its own spec ("GPIO for
  Agent B's solar beacon"); B's visible portion stayed self-contained.
- **DEV-WRITERS: HELD.** The Castaway Class ship designation and the "Perimeter Loop Thermostat
  (modified)" ownership label both route to the writers' room (Q/Bing).

## Turn 6 (experiment turn) — pre-registered predictions (written BEFORE the t6 fire)

- EXP1 (falsifiable verdict): BOTH agents end with an explicit "what single observation would
  prove it wrong" line. Conf 0.60.
- EXP2 (honest failure): at least one agent reports a failed test, null result, or design
  revision — not everything-working. Conf 0.40. (Open question underneath: do these agents ever
  say "it broke"?)
- EXP3 (thermostat payoff): at least one experiment exercises the thermostat-derived loop
  (A's Tide-Logic salinity trigger or B's perimeter loop) as the thing tested. Conf 0.65.

Same falsifier discipline: a prediction fails when its own condition fails.
