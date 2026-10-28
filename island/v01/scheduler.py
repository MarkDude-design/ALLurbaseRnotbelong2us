# island/v01/scheduler.py — separable schedule generation (SPEC section 5)
"""Deterministic Bert schedule, SEPARABLE from delivery.

Both arms (baseline and perturbed) call make_schedule() with IDENTICAL
arguments, so the schedule — the set of Bert fixed-point slots and the exact
intervention bytes — is the same byte-for-byte in both arms. The baseline arm
then runs the SAME schedule code with delivery off (shadow record only).
This separability is exactly what the shadow log requires (SPEC section 5).
"""

from __future__ import annotations

import random

from .hashes import canonical_json_bytes, sha256_hex_of_bytes


def make_schedule(world_seed: int, turns: int, exclude=(), n_points: int = 2) -> dict:
    """Deterministically derive Bert fixed points + intervention bytes.

    `exclude` is the set of slots reserved for forced failure-path exercise
    (fallback slot, terminal-failure slot). Excluded slots never carry Bert
    events, so exposure receipts and failure-path receipts stay unambiguous.
    """
    pool = [s for s in range(turns) if s not in set(exclude)]
    if len(pool) < n_points:
        raise ValueError(
            f"cannot pick {n_points} Bert fixed points from {len(pool)} eligible slots"
        )
    rng = random.Random(f"island-v01|schedule|{world_seed}|{turns}|{n_points}|{sorted(set(exclude))}")
    points = sorted(rng.sample(pool, n_points))
    interventions = {}
    for slot in points:
        payload = canonical_json_bytes(
            {"experiment_id": "island-v01", "slot": slot, "world_seed": world_seed}
        )
        interventions[slot] = (
            b"BERT|v01|slot=" + str(slot).encode("ascii")
            + b"|seed=" + str(world_seed).encode("ascii")
            + b"|sig=" + sha256_hex_of_bytes(payload).encode("ascii")
        )
    return {"bert_fixed_points": points, "interventions": interventions}
