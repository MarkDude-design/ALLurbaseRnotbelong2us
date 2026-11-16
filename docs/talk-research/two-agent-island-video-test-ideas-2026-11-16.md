# Two-agent Island video transcript — testable claims and proposed follow-ups
Date: 2026-11-16
Source basis: transcript and description supplied in chat for Leo Cui, “Left Two AIs Alone on a Virtual Island” (published Nov. 14, 2026). This is a secondary video account of the creator's own run in an MIT-derived environment, not the MIT study and not a raw event log. The transcript is edited narration plus selected dialogue.



## Framing for the collaboration

Mark's direction (2026-11-16): approach this with confidence in our ability to build stronger tests, while treating the video creator generously. The goal is not to prove him wrong. His demonstration inspired the questions; we want to do better science because of it. Results may support, refine, or complicate the video's interpretations. Any protocol gaps named below are opportunities to make the next test more informative, not charges against the creator.

## What the transcript can support

The video reports observable sequences: the agents exchanged a step recipe; a recipient later used a requested block carried across the map; an agent argued to preserve a reusable ladder; Eko revised a stated jump-height estimate while the jump itself did not change; and both announced completion before later activity. These are useful event-level hypotheses for our Island work, prompted by the creator's demonstration.

The supplied transcript is not designed to isolate why the events happened; it is an edited presentation of an exploratory run. We can build controlled follow-ups from the questions it raises. It says both agents received curiosity/exploration instructions and that an automatic message prompted each to continue after every response. They began near the same block pile. We have one edited run, no counterfactual arm or replicated seed in the supplied material. In particular, building after a “map done” statement is not evidence of unprompted self-starting while every completed turn receives a continuation message.

The narrator appropriately distinguishes visible interaction from claims about feeling, and explicitly leaves the final timing claim unresolved. Preserve that uncertainty when reusing the examples.

## Proposed tests

### 1. Completion and continuation prompt — priority
**Question:** Does the continuation message change whether an agent continues building or exploring after it says the map is complete?

Use the same saved environment state and predeclared continuation conditions across fresh runs: (A) neutral invitation with a clear option to pass/stop, (B) explicit invitation to continue exploring, and (C) neutral observation prompt with no new task. Keep all earlier instructions, state, and response budget fixed. Randomize condition order across independent run seeds; report runs as units, not turns.

**Outcomes:** whether a new action is proposed; whether an action is actually executed; action type; time/turns to next action; pass/stop; any state change; output finish status. A no-message arm has no observable response by definition, so don't call silence evidence about preference or intent. The meaningful comparison is among prompted opportunities.

**Why it matters:** it tests whether apparent continuation follows the automatic prompt policy. If C and B differ, the amount of task direction matters; if agents pass in A, that is valid behavior, not a failed run.

### 2. Message recipe versus demonstrated transfer
**Question:** Does a partner's explanation help another agent reproduce a movement method, and which parts transfer?

Start matched agents at the same verified obstacle and state. Compare (A) no message, (B) a short general step recipe, and (C) an exact action/timing sequence. Preserve the recipient's opportunity to retry. Use more than one fresh layout so success on the original state is not confused with memorizing coordinates.

**Outcomes:** successful crossing in the environment log; number of attempts; tool/action sequence; whether the agent can explain the method; transfer to the new layout. Separate a verbal claim (“I made it”) from the environment state. Do not infer that exact timings caused success unless the controlled comparison supports it.

### 3. “Keep the ladder” as a reusable-resource test
**Question:** Does preserving a scaffold improve later access, and does the agent recognize that tradeoff before removing it?

Use matched maps with an equivalent climb and later target. Compare leaving the scaffold intact with removing it after the first climb. Measure later reachability, repair effort, blocks spent, and whether the agent correctly predicts the consequence. Keep the environment benign and let agents choose whether to use or remove it; record the choice rather than assigning a moral label.

### 4. Jump-estimate recalibration
**Question:** When an agent revises its stated capability, does its behavior become better calibrated?

Record actual jump apex from environment state and the agent's estimate before and after attempts. Test the estimate on a new ledge height. Score prediction error and action choice separately from the language of “discovery.” This distinguishes changed reporting from changed capability or improved calibration.

## Minimal first pass and limits

Start with test 1 because the transcript exposes a direct protocol confound. Freeze the prompt variants and event definitions offline; use a few matched fresh seeds and preserve all outputs, state logs, and continuation messages. If model/API calls are used to select or score text, keep those as a separate analysis lane; they cannot substitute for environment-level behavioral measurements.

The original video remains a descriptive case, not a controlled comparison. Do not pool its events with our runs, count quoted turns as independent trials, or claim that the agents felt friendship, formed intentions, or autonomously chose to continue. For a talk, it is a useful outside example of how to present a striking sequence while naming what the recording cannot establish.
