# Circle consulting cards — owner directive (2026-11-05)

**Status: authorized policy, provisioning of two additional cards NOT yet verified.** This page records the owner's updated instruction; it does not prove a scheduled runner fired or any paid API call occurred.

## Immediate operating change

- **Three Rs:** READ source, RITE/WRITE useful work, REACT independently. Review is secondary to an independent reaction; no fabricated agreement.
- **Low-touch first:** choose work that does not require routine owner interaction. Spending modest OpenRouter credits is preferable to repeated manual relays.
- **Two additional consulting budgets:** Meraki/Sol and Z each receive an independent **$10/month** model-call allowance when their separate cards/keys are actually provisioned. The owner already purchased an initial $10 OpenRouter top-up; that purchase does **not** prove either additional key exists or is funded. No per-call owner approvals are required within these ceilings, and a justified use need not be token-maximal. These are discretionary ceilings, not targets to waste.
- **Distinct instruments:** API model consultants are not native Meraki/Z seats and do not join the Ring. **The Ring alone decides its membership.**
- **Work priority:** public-safe Island experiments and independent reactions; consult/alternative models also useful for other reproducible work. Avoid personal/private notebooks, employer or client data, secrets or credentials in public briefs.
- **Security first:** browser automation deferred. Prefer console/API calls and reviewed repository artifacts. Never put API keys in issues, comments, code, logs or user-visible text. Keep admin/management credentials outside workers.

## Security contract for callable infrastructure

1. **Separate OpenRouter API keys**, named for workload, with provider-enforced `limit: 10` USD and `limit_reset: monthly` on each key. Keys are recurring ceilings, **not** separate $10 prepaid balances. Leave auto-top-up off unless the owner deliberately changes it. Do not expose management keys to run jobs.
2. Store runtime keys only in protected GitHub Actions secrets. Reject missing keys, unknown caller identities, unsupported commands and unknown model IDs. A `requested_by` text field is provenance, **not authentication**.
3. Only trusted repository writers may request a consult. The caller's authenticated GitHub identity is the gate, not any claim in the brief. Keep calls bounded (one independent reaction by default, local soft per-call stop, monthly provider hard cap).
4. **Claim before expenditure.** Claim each request durably before making a charged call, so reruns and duplicate deliveries cannot spend twice. An abandoned claim is a recoverable STOP/ERROR, never permission to repeat a billable request.
5. Every call should publish model requested/returned, input hash, request ID, provider-reported cost or **UNKNOWN** (never silently $0), caller reference, and result/error. If publication fails, retain the GitHub Actions artifact and explicitly mark the ledger incomplete.
6. Public output stays on the public bus only for public-safe material. No private Project-Spiral payload should enter the bus by implication.
7. **Stop/veto authority survives checkout.** If a genuine STOP reaches the job before execution, cancel it. Claims do not override STOP. Retry only idempotently before paid execution; never auto-replay a charged request on uncertain status.

## Current routes and honest blockers

- Already implemented: `island/z_desk.py`, `island/council.py`, `island/runner.py`, and `.github/workflows/z-desk-queue.yml`, with receipts and claim-before-run queue mechanics.
- The existing queue cron has **not been observed running autonomously** in recorded receipts as of the latest check. Do not label a pending queue item an executed consultation.
- The next increment is a **trusted, comment-triggered Circle consult** (public-safe seed, existing reviewer or one-shot independent reactor) that can run without a human dispatch click once the per-seat secrets are present. Implement and verify it separately from changing the older queue's spend rules.
- Model selection: start with a currently available pinned OpenRouter model per route; free variants can serve cheap smoke tests, but their provider/model assignments must be recorded. No silent proxy-as-native-seat claims.

Owner retains a full STOP, key disable, secret revoke and workflow disable path. No Circle member gets to approve Ring membership through this instrument.
