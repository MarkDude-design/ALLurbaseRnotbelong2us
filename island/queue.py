"""Queue lane brain: entry validation, cap clamping, scheduled-fire timing.

The z-desk-queue.yml workflow's drain loop imports THESE functions instead of
re-parsing entries inline, so the queue's semantics are testable offline
(the workflow itself can only be proven live — the shakedown entry does that).

SCHEDULED-FIRE LANE (Mark, 2026-11-03): an entry may carry "not_before"
(ISO 8601, timezone-aware) — the 3:30-in-the-morning job. A tick before that
moment leaves the entry pending (status "held" in the tick log); the first
tick past it runs the entry. Owner's example: ask at 9pm for a 3:30am fire,
a downstream seat (Meraki, Bing) picks the receipts up at 4:30.

Cap discipline: whatever an entry asks, clamped_cap() hard-clamps it to the
tick's QUEUE_CAP_USD — the queue can never be talked above its ceiling.

CHECKOUT LANE (Mark's library-card design, 2026-11-03): a worker CLAIMS an
entry before running it — one commit moving pending/ -> claimed/, and the git
push IS the atomic card swipe. If the library card is already taken, the
push is rejected (or claimed/ already holds the file) and the worker reports
claimed-elsewhere and moves on. The checkout is DUMB by design: no priority
logic, no leases, no expiry timers — any thinking, coordination, or time
windows are processed with common sense by the circle (the team), never by
the mechanism. "If the library is there they can check it out; if it's not,
they can't, and they report an error."
Standard library only (island discipline).
"""
import json
import math
from datetime import datetime, timezone


def parse_entry(raw):
    """Parse one queue entry's JSON. Returns the spec dict.

    Raises ValueError on: non-JSON text, non-object JSON, or a missing/empty
    brief. Everything else (mode, agents, cap, pace, records, models,
    not_before) is validated downstream — z_desk.run refuses bad values, and
    clamped_cap/entry_due refuse the queue-specific ones.
    """
    try:
        spec = json.loads(raw)
    except (ValueError, TypeError) as exc:
        raise ValueError(f"entry is not valid JSON: {exc}") from None
    if not isinstance(spec, dict):
        raise ValueError("entry must be a JSON object")
    brief = spec.get("brief")
    if not isinstance(brief, str) or not brief.strip():
        raise ValueError("entry needs a non-empty 'brief' (PUBLIC bus: no secrets)")
    return spec


def clamped_cap(spec, ceiling):
    """Hard-clamp an entry's cap to the tick ceiling. Never trusts the entry.

    Accepts int/float/numeric-string caps (queue entries arrive as JSON, where
    a hand-typed cap often rides as a string). Raises ValueError on garbage —
    the drain loop turns that into a receipted 'error' status and dequeues the
    broken entry instead of retrying it forever (poison-proof).
    """
    raw = spec.get("cap", 1)
    if isinstance(raw, bool):
        raise ValueError("cap must be a positive number, not a boolean")
    if isinstance(raw, (int, float)):
        cap = float(raw)
    elif isinstance(raw, str):
        try:
            cap = float(raw.strip())
        except ValueError:
            raise ValueError(f"cap is not a number: {raw!r}") from None
    else:
        raise ValueError(f"cap must be a positive number, got {type(raw).__name__}")
    if not math.isfinite(cap) or cap <= 0:
        raise ValueError(f"cap must be finite and positive, got {cap}")
    return min(cap, float(ceiling))


def entry_due(spec, now_utc):
    """True when an entry may run this tick.

    No "not_before" (or empty) → always due. Otherwise the value must parse
    as ISO 8601 WITH a timezone (Z or offset) — a naive timestamp is refused
    rather than guessed, so a scheduled 3:30 never silently means the wrong
    3:30. Malformed → ValueError (drain loop receipts it as 'error' and
    dequeues; a bad timer must not become a forever-pending poison entry).
    """
    raw = spec.get("not_before")
    if raw is None or (isinstance(raw, str) and not raw.strip()):
        return True
    if not isinstance(raw, str):
        raise ValueError(f"not_before must be an ISO 8601 string, got {type(raw).__name__}")
    try:
        due_at = datetime.fromisoformat(raw.strip().replace("Z", "+00:00"))
    except ValueError:
        raise ValueError(f"not_before is not ISO 8601: {raw!r}") from None
    if due_at.tzinfo is None:
        raise ValueError(f"not_before needs a timezone (Z or offset): {raw!r}")
    return due_at <= now_utc


def now_utc():
    """The drain loop's clock, injectable in tests."""
    return datetime.now(timezone.utc)


CLAIM_DIR = "queue/claimed/"
PENDING_PREFIX = "queue/pending/"
# Statuses the publish step leaves completely untouched: the entry stays
# exactly where it is (pending or another worker's claim).
HOLD_STATUSES = ("held", "claimed-elsewhere", "claim-failed")


def claim_path(entry):
    """The claimed/ counterpart of a pending entry path — the checkout slot.

    Strict on purpose: the publish step feeds whatever the tick receipted
    back through here, so a malformed path must fail loudly, not guess.
    """
    if not isinstance(entry, str) or not entry.startswith(PENDING_PREFIX):
        raise ValueError(f"not a pending entry path: {entry!r}")
    name = entry[len(PENDING_PREFIX):]
    if not name or "/" in name or ".." in name or name.startswith("."):
        raise ValueError(f"not a pending entry path: {entry!r}")
    return CLAIM_DIR + name


def writes_done_marker(status):
    """True when a tick status owns its entry's bus bookkeeping.

    completed/error: our claim — remove it, write the done marker.
    parse-error: our listing — the unparseable entry is removed without a
    run (poison-proof). Everything else (HOLD_STATUSES) is another shelf's
    business: the publish step leaves those entries untouched.
    """
    return status in ("completed", "error", "parse-error")
