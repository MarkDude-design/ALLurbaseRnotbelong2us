# Spring Triad Chime — model review and walkthrough
Date: 2026-11-17 PT
Owner direction: Mark asked Luna to reconstruct the game from Nemotron's and ERNIE's actual proposals, invite both models back, ask whether the build is faithful, and walk through it with them.
Status: active text-only walkthrough; no joint ratification or physical play is claimed.

## Source basis
Read the actual game proposals and ERNIE's later feedback in:
- `docs/talk-research/2026-11-17-leo-cui-motives-and-repro/FROZEN-PLAY.txt`
- `docs/talk-research/2026-11-17-leo-cui-motives-and-repro/LATER-FEEDBACK.txt`
The source says Turn 2 replies were generated independently from Turn 1 and there is no physical-action record. ERNIE's later feedback is one participant's own restatement, not joint sign-off. The notebook relay contains six R0 notes only; its ten main relay rounds have not run. This walkthrough does not claim persistent model memory.

## Provisional build v0.1
Working title: **Spring Triad Chime** (also called “Chime Triangle” in ERNIE's adaptation).
- Three stones mark triangle vertices around the spring; bell at center.
- A player rings once, traces the three edges in order, returns to the starting vertex, and rings again before the echo window closes.
- A completed circuit scores one chime. First to three chimes wins.
- The first walkthrough draft held stones fixed; Nemotron identified this as omitting its central placement/adjustment mechanic.
- No duck rule affects timing, scoring, or authority. The duck can be absent; it is not a player.
- This is a text-only narrated exercise. No physical walking, sound decay, or game-engine action is measured.

The source leaves “before the echo fades” unmeasured. v0.1 disclosed a **ten-beat spoken count** as an operational convention. Nemotron found it reasonable for text but recommended calling it a walkthrough convention, not an echo rule. It remains provisional and subject to ERNIE's review.

## Experiment sequence
1. Two independent review calls received the same source excerpts and v0.1 rules.
2. Read actual outputs. Nemotron reviewed the game; ERNIE's call returned an empty response at the token limit, recorded as an error. No retry was made.
3. Revised to v0.2, restoring a placement/adjustment phase and asking ERNIE to correct the reconstruction and make one setup move.
4. After ERNIE's actual response, send that response to Nemotron and ask it to audit the move, correct any rule issue, and make the next text-only move if playable.
5. Preserve objections and unresolved rules. Do not treat a suggestion as assent, an imagined lap as physical action, or a narrated count as measured sound.

Primary descriptive checks: source-to-rule attribution; ambiguities surfaced; each narrated route lists all three edges in order; second ring is within ten spoken beats only if that convention is accepted; score follows the stated rule; dissent is preserved.
This is a prompted fidelity and walkthrough exercise, not a test of memory, consciousness, physical ability, or whether either model spontaneously invents the game.

## Phase 1 receipt — v0.1 review
Workflow run: [44189404972](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/actions/runs/44189404972). Raw receipt: [bus.jsonl](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/blob/bus/runs/free-calls-44189404972/bus.jsonl). Requested both exact free model IDs; live catalog confirmed $0/$0; total reported cost $0.
- `nvidia/nemotron-3-ultra-550b-a55b:free`: completed, returned same model, 1,140 completion tokens. It accepted the geometry/lap/win/duck decisions, objected to fixed stones as the only mode, and asked to define first player and clean lap.
- `baidu/ernie-5.5-flash-preview:free`: `error_empty_response`, finish reason `length`, 1,200 completion tokens, no text. This is not an opinion or pass.
- Both records show `reasoning_mode=null` and `reasoning_effort=null`; effort setting was not recorded by this runner.

## Phase 2 — ERNIE walkthrough invitation
A new call, not a retry, presents Nemotron's actual review and v0.2. The revised proposal restores alternating stone placement/adjustment toward balance before the lap phase. ERNIE is invited to make one concrete first setup move; order is an explicit walkthrough convention. If ERNIE objects to a core rule, the walk pauses at that objection rather than forcing a move. The loser-facing-side move remains outside the baseline. The ten-beat count is still a declared text convention, not historical agreement.
