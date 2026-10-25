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
- [x] 9 AM PT Sun: council-mode runner design + build (fetch main first, verify anchors, tests green before push).
  - Status (2026-10-25 ~03:50Z, Mark's pipeline directive): IMPLEMENTED — all three receipts in. Code: island/council.py + tests/test_council.py landed on main from b/z (byte-identical to the tested 6a6ced5 copies). Green tests: 29/29 (18 runner + 11 council), executed in Z's own runtime, fetch-after-push byte-verified. Dispatchable workflow: island.yml now takes council_file + max_cost inputs; council_file set = council run, empty = conversation run as before; publish-to-bus lane unchanged. First seed: docs/seeds/eko-council.md (Eko Island Council). Meraki's review receipts live in issue #2 comments 6392903970 and 6393001768.
- [x] First council seed: docs/seeds/eko-council.md (Eko Island Council — 3 subs, blind round, verified models only).
- [x] Workflow input: council file path + max_cost (island.yml; conversation runs now take the budget ceiling from the form too).
- [ ] 5/6/7/8 PM PT syncs: bus rounds, pad duty, run receipts, next runbook step.
- [x] Consultant matrix runbook: exact dispatch forms for the 9 bounded runs.
  - Status (2026-10-25, Z scheduled self-wake): runbook v0 below — 9 runs = 3 task classes x (EXPERT council, SUB council, held-out check). Dispatch = Mark's clicks only; caps are SOFT post-call stops (per 6393001768 labeling).

## Consultant matrix runbook (v0) — the 9 bounded runs
Structure: 3 preregistered task classes from the Eko Island Council tenant x 3 runs each = 9. Task classes (from docs/seeds/eko-council.md question set): C1 = experiment design critique, C2 = predictions/registered forecasts, C3 = triage of open questions. Per class: EXPERT run, SUB run, held-out check (EXPERT tier on fresh material, truth anchor for the convergence verdict).

Seed forks (create before dispatch, never edit after): docs/seeds/eko-council-expert-C1.md, -expert-C2.md, -expert-C3.md (EXPERT sub slugs — Mark's opus-class picks), docs/seeds/eko-council-sub-C1.md, -sub-C2.md, -sub-C3.md (SUB slugs — Groq-lane picks). Same questions, same blind round, same chair; only sub models differ. Held-out checks reuse the EXPERT seed with a fresh question block appended.

Exact dispatch form (workflow "Island Pa More — Manual Baseline", all 9):
- council_file: docs/seeds/eko-council-<tier>-<C#>.md (per table below)
- max_cost: 5 (ceiling, not target — medium tiers end well under $1; real burns need EXPERT slugs)
- topic_file / turns / history_chars / first: leave blank (council step runs instead of conversation)
| run | class | council_file | tier |
| 1 | C1 | eko-council-expert-C1.md | EXPERT |
| 2 | C1 | eko-council-sub-C1.md | SUB |
| 3 | C1 | eko-council-expert-C1.md + held-out block | held-out |
| 4 | C2 | eko-council-expert-C2.md | EXPERT |
| 5 | C2 | eko-council-sub-C2.md | SUB |
| 6 | C2 | eko-council-expert-C2.md + held-out block | held-out |
| 7 | C3 | eko-council-expert-C3.md | EXPERT |
| 8 | C3 | eko-council-sub-C3.md | SUB |
| 9 | C3 | eko-council-expert-C3.md + held-out block | held-out |

Convergence detector feed (preregistered, per Meraki's refinements adopted in 6392552234): at each class, compare SUB verdict vs EXPERT verdict; 3 consecutive matches across classes = publish candidate downgrade rule (default SUB, EXPERT opt-in). A failed held-out check on a matching pair OVERTURNS the match (truth anchor beats vote count — unanimity-override doctrine). Consequence threshold: downgrade applies task-class-specific only.
Receipts: every run publishes to the bus branch (runs/); Z reads via connector, feeds the detector, posts the verdict on the bus. No seat is a sub; the subs are instruments.


- [ ] Daily self-wake (existing) continues as floor.

## Sunday burn-lane recipes (Mark's clicks; $5/$10 runs)
Glitch-token lane (Three Envelopes / spinner / carpool) HELD BACK tonight, per Mark.
Registered predictions for the burn race: Mark — 15 minutes to burn $5. Z — throttle-bound: at run-40154079476 economics (~$0.011/turn, ~3.2 s/turn) $5 is ~450 turns ≈ 20–25 minutes of pure compute, but the B-lane 429 windows decide the pace before the budget does. Medium-tier council baselines (8–10 calls, verified models) end on completion well under $1 — the $5/$10 caps are ceilings, not targets; real burns by brunch need EXPERT-tier model picks at dispatch. Diff at brunch, bank either way.
- Burn race A: conversation — gpt-6-sol × mistral-medium-3-5, turns=100, history_chars=100000, topic_file=docs/seeds/eko.md, first=A, max_cost=5.
- Burn race B: same, max_cost=10.
- Circle run 1: council_file=docs/seeds/eko-council.md, max_cost=5 (models left blank).
- Circle run 2: same, max_cost=10.
- Tier variants (EXPERT/SUB slugs = Mark's picks at dispatch): fork the seed, swap sub models, 3 runs per tier; the convergence detector gets fed at each decision point.

## Maintenance
- Repo maintenance: Mark's. Contributions: Meraki's. Room design + runbook: Z's. Hazy details → sorted in-thread (issue comment), never by silent overwrite.
