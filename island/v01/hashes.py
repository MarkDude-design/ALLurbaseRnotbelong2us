# island/v01/hashes.py — byte-exact hashing for reproducible artifacts
"""Canonical JSON + SHA-256 helpers.

Every artifact hash in the fixture is taken over EXACT bytes produced by
these functions, so any runner on any machine hashing the same objects gets
the same digest (SPEC section 6: "reproducible hashes from exact bytes").
"""

from __future__ import annotations

import hashlib
import json
from typing import Any, Iterable


def canonical_json_bytes(obj: Any) -> bytes:
    """Deterministic UTF-8 JSON: sorted keys, compact separators, no whitespace.

    Floats are avoided on purpose; the fixture uses ints only.
    """
    return json.dumps(
        obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256_hex_of_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def sha256_hex_of_obj(obj: Any) -> str:
    return sha256_hex_of_bytes(canonical_json_bytes(obj))


def event_log_bytes(events: Iterable[dict]) -> bytes:
    """JSONL: one canonical event object per line, newline-terminated.

    The exact byte layout is part of the hash contract; do not change it
    without bumping schema_version.
    """
    return b"".join(canonical_json_bytes(e) + b"\n" for e in events)


def sha256_hex_of_file(path) -> str:
    with open(path, "rb") as fh:
        return sha256_hex_of_bytes(fh.read())
