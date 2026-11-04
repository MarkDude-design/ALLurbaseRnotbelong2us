# WIRE0 — minimum useful handoff (offline, non-deployed prototype)

**Purpose:** graceful degradation for the existing native GitHub bus, not a scheduling/gear service. This is a tiny read-only/stdio codec with no network, credentials, model calls, timers, scheduler, or background worker.

## The fallback ladder

1. Rich reply and attachment, if the UI works.
2. Durable public-safe Markdown and source permalinks.
3. Short UTF-8 or ASCII text with canonical source ID.
4. W0 one-line 160-byte ASCII packet over an **already configured** low-bandwidth transport.
5. Offline local outbox; retry the same packet later if disconnected.

This code does NOT choose LTE/SMS, send a packet, switch phone networks, wake a native chat, or publish content. Such transports require independently configured and authorized gateways/carrier connectors. An absent ACK does not mean the message failed; it means delivery is not confirmed.

## Wire format

W0|seq|owner/repo#issue@comment|reported_status|NEXT_CODE|CRC32

- The source comment must already exist and be retrievable later. Never fabricate references or assert that the receiver already read it.
- seq is monotonically increasing **within a lane**, not a synchronized global clock.
- reported_status is WAIT, BLOCKED, POSTED, or DONE. DONE is only the sender's claim, NOT independent completion verification.
- NEXT_CODE is a short uppercase task token, not a private notebook or arbitrary prompt.
- Maximum is 160 **ASCII bytes**. CRC32 detects accidental corruption; it is neither a signature nor secure tamper protection.
- Receiver replies A0|seq|ref|original_crc|ACK_crc only if it successfully parsed the original frame. The ACK does not prove that any native model read or processed it.
- Same (ref, seq, CRC) is a duplicate. Reused (ref, seq) with different CRC is a conflict requiring a primary-source lookup, NEVER an overwrite.

## Testable offline behavior

From the repository root:

    python3 tools/transport/wire0.py encode 12 'MarkDude-design/Puppy#15@6451679731' BLOCKED CODEX_KEY404
    python3 -m unittest discover -s tests -p 'test_wire0.py' -v

Expected frame (actual checksum calculated by tool):

    W0|12|MarkDude-design/Puppy#15@6451679731|BLOCKED|CODEX_KEY404|4CE3BD71

Tests demonstrate ASCII size, round-trip, parsed ACK, corrupted frame/ACK detection, wrong ACK, duplicate and sequence-reuse conflict, invalid free-text fields and a local offline spool restored after interruption. They do NOT demonstrate real LTE/SMS packet delivery, reception in a different native chat, successful source reconstruction from a live network, or independent user acceptance.

## Acceptance still required

Future owner-authorized integration would deliberately break the rich channel, deliver the short frame over a **real, independent configured transport**, recover the original canonical source and next intended action on a different machine/session, explicitly ACK at the receiver, and log the transport receipt/unknowns. For an actual offline queue, persist seen sequence/CRC entries durably; the demo's duplicate table exists only in memory.

If no independent network exists, spool locally and claim only QUEUED, not POSTED or RECEIVED. No private material, credentials or raw notebooks are to be placed on a public wire.

**Principle: degrade fidelity before continuity.** Preserve just enough truthful information to resume the correct project chessboard, then retrieve richer context when possible. Merge/spend/publication remain Mark's gates; this experimental branch is not deployed.
