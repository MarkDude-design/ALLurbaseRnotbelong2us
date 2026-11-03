# QC: resume GitHub delivery from the existing workspace

Prepared 2026-11-03 by Meraki. Status: READY FOR QC; NOT EXECUTED IN QC'S WORKSPACE.

Mark identified the target as the **Qwen Coder workspace** on November 3. His goal is direct GitHub work with fewer manual transfers. This packet is a narrow connectivity task, not a change to the scientific or creative assignments.

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
2. Use the existing approved GitHub connection. If using the already configured `gh` CLI, `gh auth status` is suitable; do not run `gh auth token`, print environment variables, inspect credential files, or place credentials in URLs. Do not re-provision a credential merely because its value is invisible.
3. Read issue #8 and identify its latest comment ID. Verify repository access through the actual API/connector rather than public web search. If no authorized connection is available, return BLOCKED with the missing capability. Do not ask Mark to paste a key into chat.
4. Write one short, public-safe receipt to issue #8 using the existing Issues-write capability. With `gh`, write the receipt to a local UTF-8 file and use:
   ```sh
   gh issue comment 8 -R MarkDude-design/ALLurbaseRnotbelong2us --body-file /absolute/path/to/receipt.md
   ```
   A host's purpose-built GitHub connector is equally acceptable. Do not add an extra API key or router for this test.
5. Fetch the returned comment by its server-assigned ID and compare the body with the intended receipt. Report its URL and actual transport. Stop after this receipt. No repeat authentication-test loop.
6. On the next normal workspace restart, try reading that same receipt using the retained approved connection. This is the persistence check; do not restart or alter a running session solely for this task.

Suggested receipt fields:
```text
seat_claimed: QC / Qwen Coder (workspace-declared)
transport: actual tool or CLI used
read_up_to: actual latest issue-8 comment ID
did: read/comment/readback, with actual results
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
