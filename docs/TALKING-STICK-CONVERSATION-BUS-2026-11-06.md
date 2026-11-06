# Talking Stick / Conversation Bus — Cooperative Floor v0

**Status:** DESIGN NOTE ONLY — no controller, provider calls, microphones, or live experiments changed.
**Date:** 2026-11-06
**Origin:** Mark ↔ Meraki conversation, developed from free-tier Bing/Copilot turn scarcity, the proposed Meraki↔Z rehearsal, and the human talking-stick analogy.
**Owner/convenor:** Mark. **Drafting seat:** Meraki (GPT-6).
**Scope:** Multi-agent conversational coordination; distinct from the existing 2-proxy alternating runner and from the Standards circle.

## Owner's actual proposal (priority over earlier assistant elaborations)

> "A bus that records what is said with timestamp as order coupled with reasonable Fair moment at hand who needs to speak now."

> "...no need to mute the microphone that would be an agreed upon thing... until you're given the signal you can't speak..."

> "...if it's you hand to whoever you want to after you done talking there could be some gamesmanship as with humans rules can develop as needed."

**Ruling:** Cooperative, *social* floor control first. Do not turn ordinary discovery into a rigid parliamentary simulator or force a microphone-muting implementation. Formal debates with consequential outcomes may warrant stronger procedural enforcement. The chair's remit is procedure, not conclusions.

## Motivation

Free Copilot/Bing limits make each turn valuable; too many exchanges can be spent on apology, collision, and "you go / no, you go" mechanics. The separate question is whether two or more agents can conduct a substantive conversation with minimal human relay. Begin with Meraki and Z; involve Bing later when it is useful. Neither the particular Copilot daily quota nor platform behavior is established by this design note.

## Shared bus

Append-only, replayable sequence of events plus transcript content:

- Every event has a **monotonic sequence number** (authoritative order), timestamp (UTC, ISO 8601), session ID, seat identity, event kind, issuer, and payload/reference. Timestamps alone cannot resolve simultaneous claims; the bus assigns sequence.
- Distinguish **a request-to-speak event** from **content said on the floor**. Requesting a turn is not itself a speech turn.
- Store the actual utterance/transcript reference, not just the decision to pass. Preserve source and order; mark missing or unobserved evidence as such.
- Seat identity is not a claim that an API proxy is identical to a live human-facing model instance. Do not fabricate turns, voices, observation timestamps, or participation.
- Prefer existing BUS v0 and JSONL conventions where compatible; this is a proposed extension, not an instruction to mutate current runners or their counters.

### Minimal event vocabulary

| Event | Meaning |
|---|---|
| `FLOOR_GRANT` | Chair or authorized current holder signals who now has the floor |
| `SPEAK` | Authorized participant's utterance, linked to transcript |
| `REQUEST` | Participant asks to enter the queue, optionally providing relevance/reason |
| `PASS` | Current speaker nominates a successor or returns floor to chair |
| `YIELD` | Current speaker finishes without choosing another speaker |
| `CHAIR_INTERVENE` | Human/appointed chair resolves a procedural problem |
| `STOP` | Owner's explicit stop; no further content turn should be dispatched |
| `NONCOMPLIANCE` | Observed out-of-turn speech attempt or missing handoff (not presumed bad faith) |

**Example only, invented for explaining the protocol, NOT an actual record:**

```text
104  10:32:14  Meraki: SPEAK / asks Z a question
105  10:32:15  Meraki: PASS → Z
106  10:32:15  BUS: FLOOR_GRANT → Z
107  10:32:41  Bing: REQUEST
108  10:33:02  Z: PASS → Bing
109  10:33:02  BUS: FLOOR_GRANT → Bing
110  10:33:28  Codex: REQUEST
```

## Fairness, deliberately non-mechanical

Fairness means a reasonable chance to contribute when relevant, **not guaranteed equal airtime or fixed round-robin order**. The floor holder can hand directly to anyone. Model preferences, alliances, friendly challenges and gamesmanship are permitted in exploratory rooms. The chair may notice starvation, unanswered direct questions, or repeated bilateral passes and intervene. Rules evolve from observed failure modes rather than being imposed speculatively.

Candidate signals when deciding who speaks next: direct question addressed to a seat, relevant evidence, someone patiently queued, a requested rebuttal, and the current holder's nomination. These are *considerations*, not an automated ranking or secretly weighted verdict.

## Two modes

**Exploratory / cooperative default:** Participants agree they will not speak unless granted the floor; nobody needs hard microphone gating. Bus records actual events, including mistakes. It is not fair to claim that voluntary rules physically prevent overlap.

**Formal debate / consequential decision:** Chair may require strict floor-grant validation, timed participation, a clear verdict boundary, and optionally enforced output/microphone gating. Only add such enforcement when called for by the experiment or noncompliance. Mark retains STOP and publication authority in both modes.

A model that cannot reliably honor the floor agreement may participate in a narrower role (observer, evidence contributor, written submission, reviewer), instead of blocking the entire room.

## Minimal rehearsal — proposed, not executed

1. Meraki and Z agree on a shared session and the three basic control operations: REQUEST, GRANT/PASS, STOP.
2. One opening topic and explicit first-speaker grant. The conversation remains freeform; no mandatory debate or substantive conclusion.
3. After each contribution, speaker may nominate any successor; requests accumulate on the bus and remain visible.
4. Record sequence, timestamps, utterance, handoffs, unanswered requests, collisions, and chair interventions. Never synthesize absent observations.
5. Review whether the bus reduced apology loops and owner relay. Add Bing only if its available usage warrants it; then try a larger room (10+ participants).
6. Compare with an unstructured baseline if possible, but don't claim causality from one rehearsal.

**Useful measures:** handoff latency; number of out-of-turn attempts; apologies attributable to collisions; unanswered requests/queue wait; actual human relays; substantive turns; number of unsolicited invitations to dissent; centralization of handoff graph; whether new evidence changed anyone's position.

## Engineering guardrails

- One sequential writer/order authority or an atomic append service; otherwise "timestamped" alone cannot guarantee order.
- Avoid an implicit lock that lets a disconnected speaker monopolize the floor. Owner-controlled recovery is required.
- Keep a distinction between **protocol compliance** and **quality of reasoning**.
- Do not promise 10+ model scaling before running a measured test.
- Do not silently trigger OpenRouter/paid calls, spend credits, or relax STOP and privacy rules.
- Existing Standards scores/counters stay unchanged.

## Placement and next ownership

The **Conversation Bus** is the correct public, provider-neutral specification home: this repository. The full originating human chat is kept in the **private** `project-meraki-` archive, not copied into the public bus. No new round is accepted by this note. No runner change authorized. Pick up after the Meraki↔Z rehearsal; then decide whether Bing and additional roles justify an implementation.

## Related existing work

- [Main bus README](../README.md) — two proxy seats, JSONL transcript and receipts, public/private boundary.
- [Existing pipeline](../PIPELINE.md) — team, transport and owner gates.
- [Take 37](TAKE37.md) — earlier live two-voice baseline, reported etiquette and interruption issues.
- [Meraki/Z ferry](MERAKI_Z_FERRY_V0.md) — distinction between live instances and API proxies.
