#!/usr/bin/env python3
"""API/billing lane stub — Route C dry-run packet builder (no network, no spend).

Per docs/Q_CIRCLE_ONBOARDING.md:
  * This module NEVER calls a paid API. It only builds/validates a dry-run
    packet that a human must approve before any dispatch.
  * Two distinct budget controls are tracked separately and must not be
    conflated:
      - provider_key_cap_usd : owner's per-key cap at the provider (hard)
      - local_soft_stop_usd  : runner-side post-call cost stop (soft)
  * Cost is reported honestly: 0 only when truly zero, otherwise unknown.
  * Credentials never appear in packets, prompts, logs, or code.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass, field, asdict

ALLOWED_ISSUE = 8  # allowlisted issue only (Route C rule)
_TOKEN_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9]{36}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-or-v1-[A-Za-z0-9]{32,}"),
]


def contains_secret(text: str) -> bool:
    """Red-line check: reject packets carrying token-shaped strings."""
    return any(p.search(text or "") for p in _TOKEN_PATTERNS)


@dataclass
class DryRunPacket:
    model_slug: str
    task: str
    read_up_to_comment_id: int
    transport: str = "openrouter (pending human dispatch)"
    provider_key_cap_usd: float | None = None
    local_soft_stop_usd: float | None = None
    estimated_cost_usd: str = "unknown"  # honest default; never guess silently
    approval_status: str = "PENDING_HUMAN"  # nothing auto-posts
    seat: str = "Q-worker"
    speaker: str = "qwen API consultant (untrusted output)"

    def fingerprint(self) -> str:
        blob = json.dumps(asdict(self), sort_keys=True).encode()
        return hashlib.sha256(blob).hexdigest()[:16]

    def validate(self) -> list[str]:
        errs: list[str] = []
        if self.read_up_to_comment_id <= 0:
            errs.append("read_up_to_comment_id must reference a real comment")
        if ALLOWED_ISSUE != 8:  # defensive, keeps intent explicit
            errs.append("only the allowlisted issue may be referenced")
        if contains_secret(self.task):
            errs.append("packet contains token-shaped secret; refuse")
        if self.provider_key_cap_usd is not None and self.local_soft_stop_usd is not None:
            if self.local_soft_stop_usd > self.provider_key_cap_usd:
                errs.append(
                    "local soft stop exceeds provider key cap "
                    "(soft stop cannot outrun the hard cap)"
                )
        return errs


def build_packet(task: str, read_up_to_comment_id: int,
                 model_slug: str = "qwen3-max",
                 provider_key_cap_usd: float = 10.0,
                 local_soft_stop_usd: float = 1.0) -> dict:
    pkt = DryRunPacket(
        model_slug=model_slug,
        task=task,
        read_up_to_comment_id=read_up_to_comment_id,
        provider_key_cap_usd=provider_key_cap_usd,
        local_soft_stop_usd=local_soft_stop_usd,
    )
    errs = pkt.validate()
    if errs:
        raise ValueError("; ".join(errs))
    return asdict(pkt) | {"fingerprint": pkt.fingerprint()}


if __name__ == "__main__":
    # Self-test only. No HTTP, no keys, no spend.
    demo = build_packet(
        task="Draft a BUS v0 status reply summarizing billing-lane guardrails.",
        read_up_to_comment_id=6395613122,
    )
    print(json.dumps(demo, indent=2))
