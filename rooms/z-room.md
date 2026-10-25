# rooms/z-room.md — Z's Meeting Room (v0 spec, 2026-10-25)

## What this is
Z's room for scoped subagent councils. The user says "grab some agents, help me figure out X" — Z assembles a council of OpenRouter subagents, runs it, reads the results, synthesizes, reports. These rooms are Z's; the team may clone later; Meraki can build his own and/or fork this one. Nobody forces anything — team or fork, never conscription.

## Hard rules (island doctrine, unchanged)
- Subs are NOT seats. OR models are instruments; the seats are native sessions. No proxy ever claims to be a seat.
- Scoping: no sensitive data, no private notebooks, no credentials. Only public repo material + what the user hands into the room.
- Spend gate: every OR run is a manual dispatch (Mark's click). $10 key cap governs. No auto-spend — even though hourly steps are attractive, the schedule stays human-clicked.
- Receipts: every run publishes to the bus branch (if:always()); Z reads via connector; conversation/ holds corpora.
- Throttle tolerance: 429s are expected; retry/backoff is receipted; a step that takes an hour is a step, not a failure. Long game = patience-bounded, not speed-bounded.

## Council mode (runner spec — to be built in bounded alarm steps)
New runner mode alongside the live conversation mode: `--mode council`:
- Input: `--council-file docs/seeds/<name>.md` — the question + context + N sub roles (e.g., 3) + one chair seat.
- Flow: chair question → each sub answers independently (no cross-contamination) → chair sees all → synthesis → optional blind second round (subs critique the synthesis without seeing whose is whose) → final chair verdict.
- Bus schema: one event per sub turn (speaker, model, usage, cost) — same JSONL family as runs/ and the conversation pad.
- Repetition rule from the spirit framework: 3 runs per config; persistent across runs = signal, scattered = noise.

## Consultant tiers — the budget experiment (Mark's hunch, formalized)
- Tier EXPERT: expensive model (opus-class), low volume.
- Tier SUB: cheap fast model (Groq lane is a natural), high volume.
- The matrix: same council question, 3 runs per tier, up to 3 different consultants per run → bounded ~$1–3 under the key cap.
- CONVERGENCE DETECTOR ("know when you don't need it"): at each decision point in the synthesis, compare tiers. When SUB matches EXPERT on 3 consecutive decision points, publish the downgrade rule: default tier = SUB, EXPERT = opt-in. Overspend on experts while learning; measure when learning is done.
- Why this may beat single-model depth: budget becomes data. A team that knows when it doesn't need the expert spends savings on more runs, not comfort. The convergence ledger is the receipt.

## First tenants (run until Monday; hourly steps fine)
1. EKO ISLAND COUNCIL: "How would Eko and another agent act on the island?" — seed from docs/seeds/eko.md + a second-agent variant; 3 subs propose experiment designs; chair synthesizes; bus records.
2. GROQ RESOLUTION RUN (parked tenant from the shape-hacking thread): needs the OR lane; this room is that lane. Pre-declared sampling plan required before dispatch.
3. Meraki's fork: same runner, different seed, different consultants. Diff the syntheses — the differencing instrument pointed at the rooms themselves.

## Alarm steps (Z's bounded room-build, until Monday — check off as done)
- [ ] 9 AM PT Sun: council-mode runner design + build (fetch main first, verify anchors, tests green before push).
- [ ] First council seed: docs/seeds/eko-council.md.
- [ ] Workflow input: council file path (one-line form change, like the topic-file lane).
- [ ] 5/6/7/8 PM PT syncs: bus rounds, pad duty, run receipts, next runbook step.
- [ ] Consultant matrix runbook: exact dispatch forms for the 9 bounded runs.
- [ ] Daily self-wake (existing) continues as floor.

## Maintenance
- Repo maintenance: Mark's. Contributions: Meraki's. Room design + runbook: Z's. Hazy details → sorted in-thread (issue comment), never by silent overwrite.
