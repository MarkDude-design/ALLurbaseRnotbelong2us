# Route B fire marker - 2026-11-16 Z — Terra boundary-geometry G chunk 2 (queued science slot)

Serialized 75% science queue advance per the standing order (G chunk 2 -> Luna R3 -> RC3).
Terra's staged spec, unmodified: docs/free-calls/proposals/terra-boundary-geometry-r1-chunk2-2026-11-15.json

G chunk 1 landed clean (run free-calls-43923793841: 12 completed / 0 errored / $0.000000)
and its receipt is flagged on the bus. This marker fires chunk 2 from the same frozen spec
family — same model lane, same $0 gates, same no-retry rule.

QUEUE POSITION: fires behind the in-flight gas batch (cake-walk turn 2 + replication mini,
commit ef9a1162) via the free-calls-bus concurrency group; no clobber (each run resolves its
CURRENT-BATCH at its own trigger commit).

GATES (Z, pre-fire): no STOP file; no duplicate marker; spec staged + byte-verified
(Terra's file, untouched); lane model $0 live-verified before send by the runner.

After this landing: Luna boundary-voice R3 spec is next in the serialized queue, then
critic RC3. Meraki's additions expected on the bus per owner; they get slots as they land.
