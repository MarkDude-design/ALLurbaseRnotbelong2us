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
