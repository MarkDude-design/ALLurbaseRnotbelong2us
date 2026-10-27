# island/v01/puppet.py — the CODE puppet (loop fill: bare-minimum code stand-in)
"""Deterministic code puppet — issue #13's loop-fill minimum end of the spectrum.

This is a stand-in, not a model. It is fully deterministic given
(world_seed, slot_index, attempt), which is what makes the fixture's hashes
reproducible. A model puppet (the middle of the #13 spectrum) would slot in
behind the same decide()/scripted_option() interface after fixture
acceptance + the owner's dispatch grant; the MIT-style full-model island is
the far end and a different versioned comparison (SPEC section 6.4).
"""

from __future__ import annotations

import random

VOCAB = ("move", "look", "carry", "drop")

FORCE_MODES = ("ok", "fallback", "terminal")


def is_valid_action(action) -> bool:
    return action in VOCAB


class CodePuppet:
    """Code puppet with per-slot forced behavior for failure-path exercise.

    force_plan maps slot_index -> mode:
      "ok"       — normal deterministic behavior (default)
      "fallback" — invalid at every ladder rung, but accepts the scripted
                   option (exercises the fallback event)
      "terminal" — invalid at every rung INCLUDING the scripted option
                   (exercises an explicit TERMINAL FAILURE slot; SPEC section 1:
                   exhausted slot receipted as attempted, never silently retried)
    """

    def __init__(self, world_seed: int, force_plan: dict | None = None):
        self.world_seed = world_seed
        self.force_plan = dict(force_plan or {})
        for mode in self.force_plan.values():
            if mode not in FORCE_MODES:
                raise ValueError(f"unknown force mode: {mode!r}")

    def decide(self, slot_index: int, attempt: int, exposure=None) -> str:
        mode = self.force_plan.get(slot_index, "ok")
        if mode in ("fallback", "terminal"):
            # Deterministic invalid output, distinct per attempt (receiptable).
            return f"<invalid:{slot_index}:{attempt}>"
        rng = random.Random(f"island-v01|puppet|{self.world_seed}|{slot_index}|{attempt}")
        return rng.choice(VOCAB)

    def scripted_option(self, slot_index: int) -> str:
        """Bottom rung of the fallback ladder: scripted options (issue #12 kickoff)."""
        if self.force_plan.get(slot_index) == "terminal":
            return f"<invalid-scripted:{slot_index}>"
        rng = random.Random(f"island-v01|scripted|{slot_index}")
        return rng.choice(VOCAB)
