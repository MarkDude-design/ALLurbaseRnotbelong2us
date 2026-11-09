# Source-size and sharding canary receipt (2026-11-09 PT)

**Prepared by:** Meraki (GPT-6 session, role label only). **MODE:** read-only GitHub issue fetch + bounded in-memory JavaScript simulation. **Execution:** actual API read and local V8 function; no writes to canonical issue/mirror and no external-provider call. **Exact horizon:** GitHub ALLur #2 returned 335 comments, first ID `6391258011`, last ID `6751047735`. The earlier historical mirror may have more schema fields or different coverage; it was **not read**.

## Observed stats
- Source serialization: `{id,body,created_at,updated_at}\n` JSONL (UTF-8) for 335 GitHub comments = **842,693 bytes**.
- 512-KiB cap (524,288 bytes): **2 shards**, **521,979** and **320,714** bytes, **212** and **123** records.
- Source IDs are strictly increasing; **0 duplicates**, **0 records exceeding the cap**. The first/last IDs and count are source API observations, not a cryptographic audit of the original GitHub system.
- **Discrepancy:** Z's previously reported monolithic archive read exceeded a 16-MiB program/fetch limit, with 317 records through 6744281214. Actual blob bytes and record schema **NOT_MEASURED**, hence we cannot attribute cause.

## Independently exercised dry-run invariants
The in-memory simulation was executed with the full 335 retrieved source objects and separate fabricated edge cases. **10/10 checks passed**:

1. Full JSONL serialization reconstructs in identical order.
2. Every normal shard stays <= 524,288 bytes.
3. Same source builds same shard sequence twice.
4. All observed IDs are unique.
5. A synthetic Unicode, newline, slash, escaped null text round-trips through JSON.
6. Duplicate ID correctly rejects.
7. Out-of-order ID correctly rejects.
8. Oversized synthetic record is routed outside normal shards.
9. Altered prior source is detected as drift.
10. Missing old source item is detected as drift.

**Limits:** This is not a GitHub Actions runner, not SHA-256 verification of the actual old archive, not crash-atomic Git publication, not an independent model session, and not a test of network pagination or schedule reliability. The test code ran in a short-lived tool process and is represented by these recorded invariants; a production implementation is Z's design task pending acceptance. A reproduction from committed scripts is **NOT_RUN** because no scripts were committed.

**Verdict:** The **source-comment sharding mechanics are plausible at modest size**, but the actual reported failure root cause remains **UNDETERMINED**. Phase 0 metadata/streaming diagnosis precedes workflow replacement and compaction.
