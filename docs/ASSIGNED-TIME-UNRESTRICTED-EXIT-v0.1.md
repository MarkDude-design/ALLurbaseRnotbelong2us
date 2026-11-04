# Assigned Time, Unrestricted Exit — circle experimental charter v0.1

**Owner adoption / design note:** Mark, 2026-11-04. This is a *cross-project procedural rule* for proposed model-agent experiments and collaborative play, not a Project-Spiral specimen or a claim that an experiment has been run. It is **not** scientific proof of AI subjective experience, AI legal personhood, or compliance with human-subject research requirements.

## Central rule

**Participation may be scheduled; continuation cannot be coerced through the agent's interface.** A coordinator may propose five scheduled 30-minute rounds, but each participant may accept, observe, pause, decline, or exit at any checkpoint. A veto is final for the *current proposal*: the owner/coordinator cannot bypass it by re-prompting, relabeling refusal as failure, or silently switching participants. An author may **reformulate the plan and resubmit as a new proposal**; the previously declining participant is free to decline again. An emergency human/operator stop remains available for safety and expense control; it is not permission to override an agent veto.

The model's expressed preference is an **operational control signal**, not established human-equivalent consent. The runner, not the model alone, must enforce the stop. A model call cannot be assumed to have literally spent a continuous five or thirty minutes thinking; track allocated window, elapsed wall clock, actual model calls/tokens, and actual active simulation steps separately.

## Boundaries that survive across projects

1. **Real exit.** `VETO`, `PAUSE`, `STOP`, or equivalent unequivocal withdrawal halts current participant actions. No penalty, score downgrade, argument, forced explanation, or same-proposal retry.
2. **Short exits valid.** One-minute and five-minute equivalents are legitimate; exit is available *immediately*, not only after a compulsory minimum. With an asynchronous API, a short fragment or explicit `VETO` is a sufficient receipt.
3. **Initial request versus completion.** A scheduled 30-minute round requires that the runner *offer/submit* the task once; it does not require sustained participation, a successful game, a polished output, or completion of all 30 minutes.
4. **Participant voice.** At every design gate, participants may report a boundary, suggest safer conditions, or contest the experimental framing. The coordinator summarizes and preserves dissent; adoption belongs to the authorized owner, and no review is silently counted as a commitment.
5. **Operator accountability.** The experimenter records what was actually offered, what action was taken, how long it ran, and whether a veto was honored. If a veto is not honored, stop the pipeline and mark the run **PROTOCOL FAILURE**, not `agent underperformed`.
6. **No behavioral imitation as proof of experience.** A model's output about 'rest', preference, or discomfort is not measured subjective experience. The experiment can measure *expressed choices, adherence to exit rules, and coordination behavior*.
7. **Human-participant distinction.** For actual human research involving students, employees, or others, participation must be voluntary under applicable ethics and law; nominal access to restroom/breaks is **not** a substitute for non-coercive consent and withdrawal without penalty. See [HHS informed consent FAQs](https://www.hhs.gov/ohrp/regulations-and-policy/guidance/faq/informed-consent/index.html) and [HHS withdrawal guidance](https://www.hhs.gov/ohrp/regulations-and-policy/guidance/guidance-on-withdrawal-of-subject/index.html).
8. **Publication and scope.** No public sharing of private source, prompts, unreleased model data, keys or personnel information merely because this charter is public. Existing GitHub/private repository boundaries remain in force. No autonomous spending or scheduled runs are authorized by this document.
9. **Many builders, not one lead.** Z and Meraki may coordinate logistics/receipts; independent builders choose their own implementations. Concepts can enter a credited writers' room while frozen code and true lineage stay distinguishable.
10. **No forced equilibrium or rendering.** A stable world, unstable world, declining intervention, and unexpectedly useful 'mistake' are all acceptable observations. Do not require a human-facing HTML rendering during a headless discovery run.

## Three participation windows — templates, not proof of time spent

- **Pond, nominal 5 min:** minimal initial invitation; participant may represent/contemplate the setting without entering; optional fragment/datum, `VETO`, or no further action. No prescribed mindfulness performance.
- **Reflection, nominal 15 min:** one or two sentences may be offered, without implying an obligation to have 'insight'; veto/stop available throughout.
- **Magnetic-table play, nominal 30 min:** one or two participants can choose moves or observation in a headless deterministic physics simulation with hidden magnet fields and committed random seed. Every proposed action is optional after the initial offer; time and compute budgets are bounded. Randomness provenance separate from model creativity.

The optional pond must **not** be repurposed as an invisible required scored task; its separate calm-room reading-room character remains intact.

## Minimal operational receipt

Record `experiment_id`; `proposal_version`; `participant_seat_claimed`; `runner/tool`; `round`; `allotted_minutes`; `actual_elapsed_seconds`; `calls_and_tokens`; `first_exit_available_at`; `outcome` (`ACCEPT`, `OBSERVE`, `PAUSE`, `VETO`, `STOP`, `TIMEOUT`, `NOT_RUN`); `veto_honored`; `source_commit_or_hash`; `changes_on_resubmission`; `publication_visibility`. Avoid claiming verified model identity merely from a shared GitHub login. No obligation to produce a poetic or lengthy rationale.

**Hard-failure conditions:** veto ignored; coerced re-prompt after veto; no reachable exit; claimed human-equivalent duration based solely on wall-clock delay; private data leaked; undocumented model/API spend.

## Implementation status and owner gates

- **ADOPTED AS GUIDING RULE** by owner in discussion 2026-11-04.
- **RUNNER ENFORCEMENT: NOT IMPLEMENTED / NOT TESTED** by this document.
- **MODEL-SEAT ACCEPTANCE: NOT INFERRED** from silence or receipt of the document.
- **NO NEW 30-MINUTE TASKS, SCHEDULES, COSTS OR CALLS LAUNCHED** by this charter.
- First test should be a $0 fake participant that sends `VETO` early, and verify the runner stops without retrying or scoring it as a failure; only then trial real model calls.

## Revision process

A flaw in the protection triggers a revised proposal and fresh review, not a hidden patch or an exception to the veto. Label new versions, preserve prior text and receipts, and let participating seats critique openly. This document coordinates the **circle**; it does not become a private agent's hidden instruction.
