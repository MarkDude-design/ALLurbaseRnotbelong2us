# Circle REACT v0 — pre-provisioning handoff (2026-11-05)

Status: STAGED ON A FEATURE BRANCH; no new API call, no triggered workflow observed. This is an implementation proposal, not proof that it runs in GitHub Actions.

## What Z's commentary establishes

Z's latest note on ALLur issue #2, comment 6666154502, confirms that the original OPENROUTER_API_KEY worked in the Mayhem burn and should remain untouched. The new Meraki and Z card secrets were not yet proven installed. Two earlier /circle-react comments on issue #16 were inert because no comment-trigger workflow existed; they do not run retroactively. The held F4 queue entry belongs to the existing Z Desk lane and is not part of this change.

## What is staged

- .github/workflows/circle-react.yml — owner-login-only issue-comment hook, issue #16 only
- island/circle_react.py — independent single-response consultant, not a native Circle seat
- tests/test_circle_react.py — zero-spend fixture and guard tests
- docs/seeds/circle-island-react-v0.md — pre-existing public-safe seed, unchanged

The only accepted NEW comments are:
- /circle-react demo circle-island-react-v0
- /circle-react meraki circle-island-react-v0
- /circle-react z circle-island-react-v0

No arbitrary code, model IDs, prompts, paths or credentials are parsed from comments. Meraki and Z are cost routes, not proof of native-seat authentication. Public-safe material only; the private Spiral repository is out of scope.

## Guards

1. Claims are committed to the public bus branch before any charge; an existing claim prevents a second execution of the same comment ID. Claim-push failure must stop before model use.
2. A fresh STOP check requires issue #16 still open, no circle-stop label, and no later /circle-stop from the owner's GitHub login. This check occurs before the model call; an in-flight call cannot be undone retroactively.
3. In live mode, GET https://openrouter.ai/api/v1/key must show a normal inference key, a $10 USD limit, monthly reset, and positive remaining allowance; otherwise no model is called. This uses the worker key and never exposes a management key to the job.
4. There is no automatic replay after network errors with uncertain billing. Cost receipts preserve UNKNOWN as UNKNOWN, not zero.
5. Every completed runner writes bus.jsonl, reaction.md and report.md. Publication to the bus branch is attempted; GitHub Actions artifacts back up local results.

The existing manual Island runner and existing Z queue remain untouched. No automatic browser access is added.

## Minimum owner actions

1. Create two OpenRouter keys, each with monthly-reset $10 cap.
2. Paste their values directly into repository Actions secrets OPENROUTER_KEY_MERAKI and OPENROUTER_KEY_Z. Never put actual values in a message, issue or commit.
3. Say only "both secrets installed". The previously proven OPENROUTER_API_KEY remains unchanged.

## Acceptance tests after reviewed merge

- One fresh DEMO comment; inspect an actual GitHub Actions run and zero-cost synthetic receipt.
- One fresh live comment; check key metadata, requested/returned model, seed hash, response ID, cost or UNKNOWN, and run stop.
- Retry/duplicate same comment ID; no new charge because claimed.
- Explicit planned STOP exercise: after claim and before API call, gate must refuse.
- At the next stage, use the already-added 10-turn option in island.yml for five paired turns of the two-model conversation; this is a different experiment than the one-shot React call.

## Honest limits

The workflow exists on a feature branch, not yet active on the default branch. The tests have been written but have not been mechanically executed in this session. GitHub webhook liveness is still unproven. A shared GitHub login authenticates the account, not the native Meraki or Z seat. Expanding direct Circle use requires an actual trusted caller identity/transport. No Ring membership changes.
