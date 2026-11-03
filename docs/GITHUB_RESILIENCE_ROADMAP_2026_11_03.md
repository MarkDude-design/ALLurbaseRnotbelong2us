# GitHub resilience: staged tooling roadmap

Research date: 2026-11-03. Status: prepared proposal; no cloud service or automatic courier deployed.

## Priority and decision

**Meraki cold-start recovery remains HIGH / active. Wider GitHub, QC/Bing and cloud work remains MEDIUM.** Use candidate B during natural returns and keep short, evidence-based receipts. The broader work can wait for a focused tooling session around other projects.

Recommendation: keep GitHub as the canonical published record; allow recovery to begin from a separately available, last-good packet. Improve the existing access path before building a larger routing platform. An independent read-only mirror is the leading medium-term cloud candidate.

## Z's failures matched to fixes

| Evidence | Proposed fix | What it does not establish |
| --- | --- | --- |
| [DEV-011 and uncertain pushes](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/16#issuecomment-6460067219) | Validate decoded content, inspect intended diff, verify exact resulting content before retry | These incidents do not all mean GitHub itself was down |
| [Emergency relay success](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/16#issuecomment-6460215685) | Preserve attributed alternate access paths | Another connector still shares the GitHub backend |
| [Failure taxonomy](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/16#issuecomment-6462435671) | Classify host/interface/connector/service/unknown before choosing a workaround | A canary is not a historical availability measurement |
| [Mayhem seed: 502/rate-limit reports, content bugs and rejected stale SHA](../island/mayhem_seed.jsonl) | Narrow reads, paced writes, content verification; retain concurrency guards | A rejected stale write is healthy protection; aggregate notes are not raw API telemetry |

## Implementation order

| Step | Setup / daily effort | Coverage and exit condition |
| --- | --- | --- |
| 1. Existing portable packet plus last-good retention | Low / low with a handoff refresh | Recover identity, goals, rationale and priority without a live GitHub read; declare source horizon |
| 2. One-host cached, guarded client | Low–medium / low | Reduce repeated reads; reject malformed responses; reconcile unknown write outcomes; preserve concurrent edits |
| 3. Independent read-only mirror | Medium / low for readers, owner maintenance | Serve the stored packet while GitHub is unavailable, including fresh-reader authentication independent of GitHub |
| 4. Optional durable outbox | Medium–high / exceptions require review | Accept pending work and reconcile it later; pending is not published; build only if measured relay burden justifies it |

Proposed Nov 3–17 sequence: continue HIGH-priority natural recovery use; spend the next MEDIUM tooling slot on one-project failure evidence and client capabilities; improve that one path; then prepare and test a read-only mirror. These are proposed slots, not schedules or assignments. Z's desk and queue are unchanged. QC's useful home-output round trip remains the first later integration test; Bing follows QC.

## Established mechanisms and important limits

- [GitHub API guidance](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api), [gh api](https://cli.github.com/manual/gh_api) and [Octokit throttling](https://github.com/octokit/plugin-throttling.js) supply existing caching/request-control mechanisms. Confirm the chosen host exposes the needed headers and retains state.
- A Git clone does not include issue/comment ledgers. [Cython's metadata snapshots](https://github.com/cython/cython-issues) show a real export pattern using [python-github-backup](https://github.com/josegonzalez/python-github-backup). Put the recovery copy on a separately accessible service.
- Cloudflare Worker + private R2 is a plausible mirror, not a selected deployment. [R2 consistency and caching](https://developers.cloudflare.com/r2/reference/consistency/) inform a design using immutable packets and a guarded current-version pointer. Authentication must also work without GitHub. Publish only complete verified packets; serve last-good state if refresh fails.
- A GitHub Actions exporter is convenient but not independent scheduling: [scheduled workflows can be delayed or dropped](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule). Existing mirrored reads should survive refresh failure.
- Webhooks are hints, with reconciliation: [failed deliveries are not automatically redelivered](https://docs.github.com/en/webhooks/using-webhooks).

## Prototype acceptance

Test unavailable GitHub, malformed refresh, interrupted export, accepted write with lost acknowledgement, concurrent source edit, edited old comment, incomplete pagination and fresh independent authentication. Keep the last-good packet, preserve uncertainty, avoid duplicate publication, and refuse stale overwrites. Measure actual request counts, time, corrections and manual pastes before claiming improvement.

This research did not establish outage frequency, comparative provider uptime, price, or audited tool security. Effort ratings are engineering estimates. Full research and references were delivered separately to Mark. No migration, merge, paid invocation, deployment or new scheduler was performed.
