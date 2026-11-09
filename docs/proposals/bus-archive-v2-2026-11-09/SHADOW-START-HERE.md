# Shadow recovery card — bus mirror reliability (NOT THE LIVE INDEX)

**State observed:** 2026-11-09 PT. **Exact source horizon:** [ALLur issue #2, comment 6751047735](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6751047735). **Status:** PROPOSAL, no new archive or scheduled writer. **Origin:** Meraki. The original GitHub issue is authoritative; this card is an intentionally small, disposable *sample of the compaction format*, not a second source of truth.

**Problem:** Z reported 3 pre-push failed appends when fetching `conversation/eko-native-bus.jsonl` exceeded a 16-MiB program limit. Last reported intact mirror: 317 comments through ID 6744281214. [Z's receipt](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6747160885). New source read: 335 issue comments through 6751047735. Simple JSONL representation of those comments: 842,693 bytes; old mirror's actual size/format **UNKNOWN**. Not a contradiction until that old blob is audited.

**Decision / status:** Owner prioritizes short/mid-term reliable continuity and is willing to allocate a majority of available discretionary effort after inspecting current usage. Meraki staged a [bounded Z-first design](PROPOSAL.md) and [read-only 10/10 canary receipt](CANARY-RECEIPT.md) on an isolated branch. **Z has not been observed accepting or implementing this proposal.** The live Z Desk queue and dispatcher are out of scope.

**Next single action for Z:** On a GitHub runner, obtain the old bus-branch file's size and SHA using `git ls-tree -rl`, then stream only aggregate schema/length statistics. Report whether the expansion is storage, tool-wrapper, or append-strategy related. **Do not delete/rewrite history.** If a matching fix is already in progress, link its source receipt instead of duplicating it.

**Boundaries:** Never infer a newer source from this card. Do not scan other seats' personal ledgers; do not move private data to public queue, publish, fire OpenRouter or modify queue checkout. Reader missing a later bus horizon must query the original issue and mark this card STALE. Authorship and user veto instructions still require source provenance.

**Known not-run:** production archiver, real browser, provider calls, fresh-context recoveries, migration/cutover. **One unresolved question:** why did a 16-MiB-constrained fetch fail when the presently retrieved comment text itself serializes to <1 MiB?
