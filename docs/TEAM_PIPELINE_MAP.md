# LLM pipeline — start here

Updated 2026-11-03 by Meraki, from Mark's current workflow directions and source reads. This is a navigation map, not a new service or a replacement for each lane's record.

[Team best practices — maintained by Meraki](TEAM_BEST_PRACTICES.md) · [Meraki's saved read markers](pipeline-state/meraki.json)

Everyday prompts: **warm start the pipeline** or **cold start the pipeline**. Read the saved per-stream marker rather than asking Mark for a comment number. This is a team convention; automatic loading after a new-thread reset is still to be tested.

## One online index, explicit source records

The existing [Continuity Index, issue #16](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/16) is the online cross-repository list. Its comments append current pointers at named read horizons. Each lane below keeps its own source state; do not treat the old issue-head table or this dated map as continuously current.

| Lane | Source record | State established in this pass |
| --- | --- | --- |
| Native team conversation | [ALLur #2](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2) | Continuing authored exchanges; no automatic wake-up inferred. |
| Packet/receipt contract | [Puppy #11](https://github.com/MarkDude-design/Puppy/issues/11) | Historical verified round trip; use its exact hash contract if appending there. Ordinary recovery notes belong elsewhere. |
| QC connection | [ALLur #8](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/8), [PR #17](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/pull/17) | Historical Qwen Coder writes verified; earlier repo-bound setup reportedly deleted. Fresh connection and persistence test pending. |
| Z Desk | [ALLur #9](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/9), [queue protocol](QUEUE.md) | Actual manual consult outputs exist. Queue workflow now contains a ten-minute cron and pending/done protocol; no queue tick established by the latest 12 account-run results read in this pass. |
| Puppy cold-start recovery | [Puppy #16](https://github.com/MarkDude-design/Puppy/issues/16) | Existing evidence-and-next-action notebook. Verify its linked current sources before acting. |
| This preparation sprint | [Sprint plan](PIPELINE_SPRINT_2026_11_03.md), [cold-start test](../experiments/pipeline-cold-start/README.md) | Three synthetic fresh-reader arms and offline tests completed; QC/Bing live qualification remains pending. |

Z has also kept a separately reported knowledge topic called llm-team-pipeline. That topic was not directly editable through this session's tools. This GitHub index/map is the shared online return path.

## Default workflow — owner direction, summarized

- One active worker project at a time; switching it is deliberate. Quick work with Z/Meraki elsewhere can continue without retuning all workers.
- The connected home repository can be the hotpad/inbox/outbox even when a note concerns Castle or another permitted source.
- An incoming fragment records its exact text or source pointer and intended destination. It does not switch the active project.
- Direct agent output, an attributed Z relay, or a supported hosted courier all reach the same canonical work record. A writer preserves the producer and source instead of taking authorship.
- Reading sources elsewhere and writing elsewhere are different permissions. A one-repository worker can leave output at home for an authorized courier.
- Routine questions go to Z first, escalating when needed. Empowered seats can still consult Meraki directly. Proportionate preflight/postflight review is useful; no new per-action approval bureaucracy is created.
- Immediate qualification order: QC, then Bing's owner-reported new GitHub integration, then Q's remaining tuning. Mark aims to reach QC today if possible, otherwise this week; no reminder or new timer was requested.
- A default endpoint simplifies connection setup; it must not freeze every task to an unchangeable repository.

## Cold and warm return paths — roadmap addition

[Bing's proposal, carried by Mark](pipeline-contributions/BING_COLD_WARM_START_2026_11_03.md), distinguishes cold orientation from changes since a last verified read. The existing decision ledger keeps recorded reasons; a warm-start view should summarize only the delta between explicit receipt horizons. Missing or unverifiable horizons need a bounded cold fallback. This is planned across A/B/C. A subsequent real manual-marker lookup retrieved Mark's greeting on PR #17 correctly and found no later comments. That demonstrated note retrieval, not a complete delta-service or fresh-thread recovery.

## Current next action — priority clarified

**HIGH / active: Meraki cold-start recovery.** Use [the short cold-start entry](COLD_START.md), selected evidence-first route B and the saved recovery snapshot. Exercise it over several return episodes and preserve small receipts before deciding what works reliably.

**MEDIUM / prepared:** the wider integration and fine-tuning work. When pulled into a focused session, start with [QC's bounded return task](QC_GITHUB_RETURN_V0.md), then Bing and Q. The earlier blanket medium label is superseded for Meraki's cold-start lane only.

The preparatory files in PR #17 are proposed, unmerged artifacts. They are readable from that branch before merge. No new cloud deployment, paid dispatch, cron activation or access-policy change is claimed by this map. Z's existing queue and desk code are untouched.

