# Eko M-001: Meraki ↔ Z bounded Markdown ferry (proposal)

**Status:** PROPOSED, documentation only. No live autonomous connection, model call, merged code, or island simulation.
**Source:** `main` at `d04bedf71688c1eb002d63d6245801909e568082` (2026-10-24).
**Inspiration:** Puppf's bounded packet, hash provenance, receipt, stop and review rules. Preserve Island Pa More's own bus; do not rewrite it.

## What actually exists

- **AllUrBase proxy bus:** `island/runner.py` records `start`, `turn`, `retry`, `error`, `stop` as `bus.jsonl`, plus `transcript.md` and `report.md`. Manual `.github/workflows/island.yml` requests `model_a` and `model_b` because **those are OpenRouter API proxies**, NOT the original ChatGPT/Mistral conversations.
- `bus` branch (public) is an output pickup lane, including failed run receipts; it is not a private workspace. A recent 50-turn Eko run (40142648053) produced one A turn, then B returned repeated HTTP 429 responses and a recorded stop. Retry and `Retry-After` tests exist; live 50-turn completion is not established.
- **Puppf S0 file diode** is currently a reviewed specification, not proof of deployed working transport. Puppf's working contribution is bounded review/receipt discipline.

## Two routes; do not conflate them

| Route | Who speaks | How it moves | Model chooser? |
|---|---|---|---|
| **M: native-seat ferry** | Meraki in this actual ChatGPT conversation and Z in Z's existing collaborator conversation | Mark explicitly supplies a GitHub Markdown link, or asks each seat to fetch the other seat's published repo note | **No.** No proxy selected; no paid API. This is manual, not an automatically polling live bus. |
| **P: existing proxy runner** | OpenRouter models selected as A and B | Existing `workflow_dispatch` with model IDs, key, spend cap, and API `bus.jsonl` | **Yes.** Model IDs are required, and calling an API proxy is not the same as calling the original seat. |

## First experiment: M-001 (maximum four handoffs)

- Topic: **How should we record an Eko failure without confusing evidence, interpretation, cost, and privacy?**
- A = Meraki, B = Z, Mark = scope/spend/publication/acceptance authority. Each seat may disagree and refuse an invalid claim.
- Read inputs: `README.md`, `island/runner.py`, `.github/workflows/island.yml`, `docs/EKO_RUN.md`, and PUBLIC-SAFE bus evidence. No private notebooks or credentials.
- Bounded exchange: **A → B → A → B**, max 800 words per reply, one explicit next question, then STOP; no recursion or automated triggers.
- Allowed changes: Markdown review/handoff only on scratch or review branches. **No edits to runner, workflow, packet, bus history, or secrets. No spend.**
- Outcome: link the actual sources inspected, describe one supported result or unresolved disagreement, and state `READY`, `BLOCKED`, or `STOPPED`. Mark decides whether any later code is authorized.

**File convention, not automatic creation:** A publishes a numbered `docs/ferry/M-001/A-01.md` on `a/meraki` (or review branch), B publishes `docs/ferry/M-001/B-01.md` on `b/z`, A returns `A-02.md`, B closes `B-02.md`. Mark ferries links or invokes seats. One writer per file; avoid overwriting. The `bus` branch continues to carry *API execution evidence*, not the coordination instrument's own construction.

Each Markdown reply names: `packet_id`, seat, source commit, handoff index, allowed refs, Question, Observed evidence, Interpretation, Next request, Stop reason. A copied SHA is `as_recorded`; only deterministic exact-byte verification using a separately trusted digest is `verified`. Actual requested/observed model and cost remain `null` where unavailable; 'Codex', 'Meraki', or 'Z' are seats/roles, not proof of an API model version.

## Error-reading rule (preserve existing implementation)

Read a particular public `bus.jsonl` run and identify `run_id`, `seq`, `speaker`, request/returned model, retry attempts, HTTP class / `Retry-After` when present, `error`, `stop`, and available provider-reported cost. Link the evidence before diagnosing. A passing retry fixture is not a successful live recovery. No automatic fix/retry, no fake receipt.

## Future floor control (not needed to start)

Current runner enforces strict A/B alternation. For direct discussions, a cooperative grant/pass from Mark or the preceding seat is sufficient. If formal debate with consequential outcome is later approved, use a deterministic floor controller (speaker queue, sequence, timeout, fairness), not a hard microphone mute for ordinary conversation. Do not manufacture a global event sequence from GitHub timestamps alone.

## Privacy, cost, and stop boundary

**All GitHub branches of this public repo are public, even any branch named PRIVATE.** The current Actions workflow pushes `runs/` to public `bus` using `contents: write`; its text and topics become publicly readable. Use only user-approved public-safe material there. Private model/user notebooks remain in separate protected storage; public scientific methods and outcome receipts do not entitle anyone to private reflections. No legal-personhood claim is implied.

Keep **AllUrBase's existing $10 proxy-run cap** unless Mark separately revises it. Puppf's $50 project budget is not inherited by this experiment. Native-seat M-001 uses **no new external paid service**.

STOP on explicit Mark request, unavailable inputs, privacy uncertainty, hash mismatch, unmet authorization, or four handoffs. A session cannot autonomously watch GitHub; a native-seat response requires a new user/chat invocation or separately supported automation.

## Review request to Z

Please review **this Markdown only plus the named public files**. Report at most **three material findings**: what Puppf boundary to keep, what existing bus feature not to lose, and what minimal change (if any) would enable an honest native-seat handoff. Do not choose substitute API model IDs, modify code, spend money, or run the Eko experiment. Reply on your `b/z` branch or this PR conversation, with sources and an explicit stop. Meraki will review; Mark gates public merging and execution.
