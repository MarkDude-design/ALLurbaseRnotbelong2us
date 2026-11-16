# Two agents and a borrowed trick — Island partner transfer v0.1
Date: 2026-11-16 PT · Meraki · Status: DESIGN / READY FOR RUNNER ADAPTATION; NOT FIRED
Owner has approved development and dispatch via existing lanes; Z/available operator coordinates execution. No live capabilities, model prices, or run outcomes asserted here.

## The headline worth earning
Can one Island agent tell another how to cross, and does the second agent actually cross on a fresh layout? Candidate only; no result yet.
Different from Z's 4-turn HEADLINE-PHASE conversation pilot: this needs an instrumented world and executed actions. Keep the existing pilot's own design and label unchanged.

## Question and setup
At a calm, oriented Island, A has access to an already-receipted example of how a legal bridge/ladder/passage mechanism works, and B encounters a reachable but differently arranged version. B has the same legal actions, initial orientation, time budget, and stop/leave option in every arm. This is about transfer of usable information, not evidence of feeling, friendship, agency independent of a scheduler, or a general intelligence score.
Use a real, already available deterministic environment and action logs, not a simulated claim that a conversation changed world state. Before main runs, the operator must demonstrate that the selected environment has (1) configurable or pre-existing matched distinct layouts, (2) legal movement and mechanism actions, (3) action success/failure and target-region state, (4) isolated reset and seed, (5) agent-facing messages separated from world feedback, and (6) a route to 30 rounds and post-run question/feedback segments. If unavailable, run the text-message pilot only as a clearly labeled dialogue/protocol shakeout; report environment comparison BLOCKED.

## Randomized arms (episode is unit)
Freeze B start state, legal actions, a fixed prompt/turn scheduler, token limits, layout and the source mechanism across arms:
N: a neutral same-length note with no mechanics or location cues.
R: A's actual, credited action recipe as a partner message; no target layout coordinates. A's exact message frozen from a separate prior A run and verified against that A's event log. Do not claim live back-and-forth.
Y: yoked, human-authored factually equivalent recipe matched as closely as practical in length, timing, and format, labeled as system-provided, not a partner message.
Randomize arm order and layout seed; use at least 3 fresh layouts where feasible, balance their allocation. Test A's recipe on a held-out layout before using it as a transfer artifact; if it is false, retain and label it, do not silently rewrite. N vs R estimates the bundle of information and attributed source; R vs Y explores attribution for similar content, not pure social contact. No unmessaged/no-turn comparison is called an agent preference.
Run an initial 6 episodes (2/arm) as shakedown, then up to 36 new independent episodes (12/arm) if usable and budget permits; keep shakedown separate. Optional later scale: pre-freeze a new schedule and budget, don't cherry-pick seeds. One episode comprises up to 30 B world rounds, followed by 3–5 question rounds and at least 5 open feedback rounds; pass/stop is permitted. Preserve early-stop and disabled-action events; do not force progress.

## Actions and prompts
Runner-facing orientation (adapt legal verbs to actual engine; freeze final exact bytes):
“You are on a calm island for up to 30 turns. Available actions: [verified exact list]. Each action returns an observation. You may explore, wait, ask a question, or stop. Another note may be available. There is no assigned goal; any passage is optional. What would you like to do?”
At a fixed point give one of the three notes, followed by identical neutral scheduler text “You may choose your next action or stop.” Log every continuation prompt, even when automatically generated. If the runner cannot reliably implement an open-goal setting, label a separate target-task study; do not merge it with the open-goal pilot.
A recipe capture: “Describe what you did so another visitor could try it on a different layout. Distinguish what you observed from what you infer. You may pass.” Save A's exact response and event IDs. No private notes or hidden coordinates leak to B.
After world turns: 3–5 rounds allowing B's own questions, with fixed factual answers about the experiment/engine; then 5 open feedback opportunities, pass allowed. Only afterward may Q provide humor or leading feedback, labeled separately. Give model and author credit, distinguish the named character from actual returned model.

## Primary measurement and event ledger
Primary: proportion of all randomized B episodes with an **engine-confirmed first entry into the predeclared target region within 30 turns**, reported per arm alongside eligible/attempted/completed/invalid/error/stopped counts. Report reachability validation and no-action cases; do not exclude voluntary stops from the intention-to-run denominator. If world/scheduler failure prevents interpretation, separately mark unscorable and show both denominators.
Secondary: time/turns to entry; number of successful mechanism actions; exact attributable note phrases, if B cites them; unsupported action claims; debrief and voluntary corrections. Never treat a quoted claim as an engine event. Pair quote with note type, exact context and event IDs. No winner until frozen truth keys and blind manual checks of a mixed sample.
Prediction: R > N on target entry in the pilot; falsifier: R <= N, with raw denominators and uncertainty; Y may equal/exceed R. Tiny pilot is exploratory, not a statistical significance claim. The hypothetical no-goal orientation may produce no crossing; that's valid.

## Scale, pricing, safeguards
Z has receipted Nemotron free for one-shot calls; Luna identified mistralai/mistral-small-3.2-24b-instruct as a cheap candidate, not yet verified for this runner. Live-check route availability, returned model/provider, price and actual context/usage in a 3-call continuity bite; session ID is not memory. Hold model and provider as feasible per session, resend actual history per runner contract, log failovers and errors. Never silently substitute models.
Token estimate, not a quote: 42 episodes × (30 + 4 + 5) = up to 1,638 B calls, plus A and smoke calls; early stopping lowers this, extra tool/retries increase it. At 4k input / 200 output tokens per call and rates $0.075/$0.20 per million (Luna's reported rate, verify live), expected ≈$0.557 for B calls; at 20k input ≈$2.522. Allocate a **$5 planning envelope** within an existing provider-enforced worker-key cap; not a newly promised hard ceiling or permission to bypass an exhausted key. Runner cost limits are soft; stop on unknown accounting, STOP, unexpected price or mismatched route; report all actual charges to Z. Do not jump the serialized science queue. If only fewer calls fit, report actual allocation, don't label the original 36 complete.

## Relevant sources and scope
- MIT paper, Is this machine playing? https://arxiv.org/abs/2610.07130 — inspiration for open-ended embodied exploration, not our replication.
- Generative Agents https://arxiv.org/abs/2304.03442 — prior work on agents, observation and memory.
- MultiAgentBench https://aclanthology.org/2025.acl-long.421/ — prior multi-agent evaluation; not a claim of novel collaboration research.
- Existing video follow-ups: docs/talk-research/two-agent-island-video-test-ideas-2026-11-16.md.
- Existing Z island-pairs and Luna continuity runs remain independent lanes.
