# QC: reconnect GitHub delivery in the Qwen Coder workspace

Prepared 2026-11-03 by Meraki. Status: READY FOR QC; NOT EXECUTED IN QC'S WORKSPACE.

Mark identified the target as the **Qwen Coder workspace** on November 3. His goal is direct GitHub work with fewer manual transfers. This packet is a narrow connectivity task, not a change to the scientific or creative assignments.

## Owner clarification — default flow and connection recovery

Mark's November 3 follow-up sets the default routing: **agent → Z → Meraki/Mark when escalation is needed**. An empowered agent may still consult Meraki directly; this default keeps routine questions from expanding the coordination flow. Routine work within recorded authority continues without a new permission request.

Z owns the desk and first-line questions. Its successful consult tests are an available basis for quality checks before consequential work and review afterwards. This is a routing/design decision, not a claim that every task already has an automatic preflight or postflight check. Checks should be proportionate to the task.

Mark reports that the earlier GUI setup was tied to one repository, could not be changed there, and was eventually deleted. The exact deleted component and current workspace state are unverified. **Do not assume the previous connection still exists.** He also reports that a pasted terminal command was interpreted successfully; establish which operations actually execute before claiming shell access.

Immediate sequence:
1. Re-establish QC's supported GitHub route and deliver one useful receipt.
2. Check connection retention on the next normal restart.
3. Test Bing's new GitHub integration after QC is on track. The new integration is owner-reported; current read/write behavior still needs a fresh receipt.
4. Tune Q's route separately.

Use one canonical GitHub work record, with three possible ways to reach it:
- the agent's supported native GitHub connection;
- a transparent Z relay when the agent cannot publish;
- a supported hosted MCP/worker route if it solves a measured limitation.

The default endpoint simplifies setup; each task still names its repository, input refs and output destination. A default must not recreate the old unchangeable repository binding. Extra storage or cloud components remain optional transport/runtime choices, with the canonical record kept explicit.

## Reuse the proven route

Repository: `MarkDude-design/ALLurbaseRnotbelong2us`.
Return destination: [issue #8](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/8).
Read the issue's latest comments before acting.

Historical evidence:
- [Direct comment and push report](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/8#issuecomment-6395516921).
- [Independent verification](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/8#issuecomment-6395616008).
- [Substantive code publication verified](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/8#issuecomment-6396552327).
- Review branch `coder/api-billing-stub` was re-read on November 3 at `f2a147714b79f829dfc896b7db1ca997b97ca46e`. It remains the old dry-run implementation, not a live dispatcher.

These establish a past working transport. They do not prove that today's workspace still has its credential, that it persists after restart, or that the requested safety corrections were implemented.

## One bounded task, when opened in QC's workspace

1. Identify the actual workspace and tools. If shell is exposed, check:
   ```sh
   git rev-parse --show-toplevel
   git status --short --branch
   command -v gh
   ```
   Missing checkout or shell is a reported capability result; it need not prevent a GitHub connector from working.
2. Check whether an approved GitHub connection remains available after the reported deletion. If it is absent or still bound to the wrong repository, report the exact setup limitation to Z; use the supported reconnection flow when authorized, rather than retrying the old binding. If using an already configured `gh` CLI, `gh auth status` is suitable; do not run `gh auth token`, print environment variables, inspect credential files, or place credentials in URLs. Do not re-provision a credential merely because its value is invisible.
3. Read issue #8 and identify its latest comment ID. Verify repository access through the actual API/connector rather than public web search. If no authorized connection is available, return BLOCKED with the missing capability to Z. Z may carry a clearly attributed receipt into the canonical issue using the established relay lane; label it RELAYED, not a verified direct QC write. Do not ask Mark to paste a key into chat.
4. If direct publication is available, write one short, public-safe receipt to issue #8 using the approved Issues-write capability. With `gh`, write the receipt to a local UTF-8 file and use:
   ```sh
   gh issue comment 8 -R MarkDude-design/ALLurbaseRnotbelong2us --body-file /absolute/path/to/receipt.md
   ```
   A host's purpose-built GitHub connector is equally acceptable. Do not add an extra API key or router for this test.
5. For a direct write, fetch the returned comment by its server-assigned ID and compare the body with the intended receipt. Report its URL and actual transport. Stop after this receipt. No repeat authentication-test loop.
6. On the next normal workspace restart, try reading that same receipt using the retained approved connection. This is the persistence check; do not restart or alter a running session solely for this task.

Suggested receipt fields:
```text
seat_claimed: QC / Qwen Coder (workspace-declared)
transport: actual tool or CLI used
read_up_to: actual latest issue-8 comment ID
did: read/comment/readback, with actual results
delivery: direct | relayed | not_delivered
credential_persistence: untested | retained_after_restart | missing_after_restart
blocked: precise missing capability, or none
next: one useful repository task
usage: null unless the caller exposes actual usage
cost: null unless the caller exposes actual cost
```

A shared GitHub account authenticates the account, not the underlying model. Secret values never belong in the receipt.

## Scope

This connectivity packet permits the bounded issue-8 return when Mark dispatches it to QC. It does not authorize a merge, workflow execution, paid model call, deployment, new credential, account-policy change, or unrelated issue. The prior fresh-reader packet `docs/TO_QC.md` remains a separate read-only assignment; do not spoil its initial independent read by opening interpretive material early.

After the first successful round trip, use normal useful task outputs rather than more HELLO tests. Existing branch corrections can resume under their recorded task and publication authority. The earlier orphan gitlink branch remains unrelated.

## Standard hosted route if the connection is missing

First inspect the workspace's supported GitHub or remote-MCP connection mechanism. GitHub maintains a hosted MCP server at `https://api.githubcopilot.com/mcp/`; compatible clients can use approved OAuth or a securely stored repository-scoped token. Verify the host's real authentication support. A URL alone cannot add MCP support to a host.

For multiple tool servers, Cloudflare MCP server portals provide a managed single endpoint, selected tools, Access authentication and request logs. The portal is a possible consolidation layer, not a prerequisite for this first GitHub receipt and not a worker runtime.

Provisioning uses an administrator's separate credential through a secret manager. Each runtime receives its own revocable, limited grant; it does not receive the Cloudflare administration key. Keep GitHub access restricted by the upstream credential; merely hiding tools does not restrict that credential's repository permissions.

Reference specifications:
- [GitHub hosted MCP server](https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md)
- [Cloudflare MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/)
- [Development Container specification](https://containers.dev/overview)

No new platform, worker implementation, or live test is claimed by this document.
