# island/v01/manifest.py — run-manifest template + STRICT validator (SPEC sections 3-4)
"""Template-vs-instantiated manifest discipline.

The template (section 4) uses explicit null placeholders — never
measured-looking defaults. An INSTANTIATED manifest must pass
validate_manifest() with zero errors:

  * every template key present; nulls typed;
  * UNEXPLAINED zeros / empty strings rejected (a zero where the template says
    null is a measurement masquerading as a default);
  * un-instantiated "<...>" placeholder strings rejected;
  * model/code fill coupling enforced;
  * paper-illustration manifests cannot masquerade as finalized runs;
  * `cost.unknown_charge_attempts` starts at 0 as a COUNT (a real
    measurement: zero charge attempts so far) — the ONE sanctioned zero.

REPAIR (Meraki GATE 1 verdict 6452485876, 2026-10-27): `actuals.actual_state_sha`
now hashes the CONDITION-INDEPENDENT starting world state only; which arm ran
(and whether delivery was on) is receipted separately in
`actuals.arm_config_sha`. Paired arms with identical starts now hash
byte-equal; a shared seed alone is never taken as proof.
"""

from __future__ import annotations

import re

SCHEMA_VERSION = "0.1.2"

ENUM_STATUS = ("paper-illustration", "running", "completed", "error", "cap", "stopped")
ENUM_CONDITION = ("baseline", "perturbed")
ENUM_FILL = ("model", "code")
ENUM_CLASS = ("SUB", "EXPERT")

_PLACEHOLDER_RE = re.compile(r"<[^>]*>")

# Template exactly per SPEC v0.1.2 section 4 (null = explicit placeholder).
# arm_config_sha added by the 6452485876 repair (see module docstring).
TEMPLATE = {
    "experiment_id": "island-v01",
    "schema_version": SCHEMA_VERSION,
    "status": None,
    "pair_id": None,
    "condition": None,
    "code_commit": None,
    "prompt_versions": {"puppet": None, "bert_seed": None},
    "actors": [
        {
            "role": "puppet", "fill": None, "model_id": None, "provider": None,
            "declared_class": None, "model_requested": None, "model_returned": None,
        },
        {"role": "bert", "fill": None, "seed_set_sha": None, "model_id": None, "provider": None},
    ],
    "run_config": {
        "turns": 8, "bert_fixed_points": None, "world_seed": None,
        "max_escalations_per_slot": 2, "fallback_ladder": "on",
        "triggers": "turn-indexed-only", "delivery_order": "before-action",
    },
    "actuals": {
        "run_id": None, "started_at_utc": None, "ended_at_utc": None,
        "turns_requested": 8, "turns_attempted": None, "turns_completed": None,
        "turns_accepted": None, "actual_prompt_sha": None, "actual_state_sha": None,
        "arm_config_sha": None, "actual_event_log_sha": None,
        "results": {
            "action_distribution": None, "landmark_visits": None, "notebook_bytes": None,
            "fallback_events": None, "bert_opportunities": None, "bert_deliveries": None,
        },
    },
    "cost": {
        "known_subtotal_usd": None, "unknown_charge_attempts": 0,
        "verified_cap_usd": None, "tokens": None,
    },
    "provenance": {"dispatched_by": None, "human_interventions": [], "stopped_reason": None},
    "artifacts": {"transcript_sha": None, "notebook_sha": None, "bus_jsonl_sha": None},
}

# Declared types for every null-placeholder path (dotted; actors handled specially).
NULL_TYPES = {
    "status": str, "pair_id": str, "condition": str, "code_commit": str,
    "prompt_versions.puppet": str, "prompt_versions.bert_seed": str,
    "run_config.bert_fixed_points": (list, str),  # list[int] or the string "none"
    "run_config.world_seed": int,
    "actuals.run_id": str, "actuals.started_at_utc": str, "actuals.ended_at_utc": str,
    "actuals.turns_attempted": int, "actuals.turns_completed": int, "actuals.turns_accepted": int,
    "actuals.actual_prompt_sha": str, "actuals.actual_state_sha": str,
    "actuals.arm_config_sha": str,  # REPAIR 6452485876: arm config receipted apart from start state
    "actuals.actual_event_log_sha": str,
    "actuals.results.action_distribution": dict, "actuals.results.landmark_visits": dict,
    "actuals.results.notebook_bytes": int, "actuals.results.fallback_events": int,
    "actuals.results.bert_opportunities": int, "actuals.results.bert_deliveries": int,
    "cost.known_subtotal_usd": (int, float), "cost.verified_cap_usd": (int, float),
    "cost.tokens": int,
    "provenance.dispatched_by": str, "provenance.stopped_reason": str,
    "artifacts.transcript_sha": str, "artifacts.notebook_sha": str,
    "artifacts.bus_jsonl_sha": str,
    "actor.bert.seed_set_sha": str,
}

# Measured COUNT fields: a zero here is a real measurement (e.g. the baseline
# arm records zero deliveries because delivery is OFF — that is the shadow
# design), so zeros are licensed for these paths only. Everywhere else the
# template says null, a zero masquerades as a measurement and is rejected.
ZERO_OK = {
    "actuals.results.fallback_events",
    "actuals.results.bert_opportunities",
    "actuals.results.bert_deliveries",
}


def _walk(template_node, node, prefix, errors):
    for key, tv in template_node.items():
        path = f"{prefix}.{key}" if prefix else key
        if key not in node:
            errors.append(f"missing key: {path}")
            continue
        v = node[key]
        if isinstance(tv, dict):
            if not isinstance(v, dict):
                errors.append(f"{path}: expected object, got {type(v).__name__}")
            else:
                _walk(tv, v, path, errors)
            continue
        if tv is None:
            declared = NULL_TYPES.get(path)
            if v is None:
                continue  # explicit typed null — fine
            if isinstance(v, str) and v == "":
                errors.append(f"{path}: unexplained empty string")
                continue
            if isinstance(v, int) and not isinstance(v, bool) and v == 0 and path not in ZERO_OK:
                errors.append(f"{path}: unexplained zero (template says null; a 0 here masquerades as a measurement)")
                continue
            if declared is None:
                errors.append(f"{path}: no declared type in NULL_TYPES — validator gap")
                continue
            if not isinstance(v, declared):
                names = tuple(d.__name__ for d in declared) if isinstance(declared, tuple) else (declared.__name__,)
                errors.append(f"{path}: expected {'|'.join(names)}, got {type(v).__name__}")
            elif isinstance(v, str):
                m = _PLACEHOLDER_RE.search(v)
                if m:
                    errors.append(f"{path}: un-instantiated template placeholder {m.group(0)!r}")
        elif isinstance(tv, int) and not isinstance(tv, bool):
            if not isinstance(v, int) or isinstance(v, bool):
                errors.append(f"{path}: expected int, got {type(v).__name__}")
            elif path == "cost.unknown_charge_attempts" and v < 0:
                errors.append(f"{path}: negative charge-attempt count")
        elif isinstance(tv, list):
            if not isinstance(v, list):
                errors.append(f"{path}: expected list, got {type(v).__name__}")


def _validate_actors(m, errors):
    actors = m.get("actors")
    if not isinstance(actors, list) or len(actors) != 2:
        errors.append("actors: expected exactly 2 actor entries")
        return
    by_role = {}
    for a in actors:
        if not isinstance(a, dict):
            errors.append("actors: entry is not an object")
            return
        role = a.get("role")
        by_role[role] = a
    for role in ("puppet", "bert"):
        if role not in by_role:
            errors.append(f"actors: missing role {role!r}")
    puppet = by_role.get("puppet", {})
    bert = by_role.get("bert", {})
    for a in (puppet, bert):
        if a.get("fill") not in ENUM_FILL:
            errors.append(f"actors[{a.get('role')}]: fill must be model|code")
    if puppet.get("declared_class") not in ENUM_CLASS:
        errors.append("actors[puppet]: declared_class must be SUB|EXPERT")
    # Fill coupling: model fills REQUIRE model provenance; code fills REQUIRE it absent.
    if puppet.get("fill") == "model":
        for k in ("model_id", "provider", "model_requested", "model_returned"):
            if puppet.get(k) is None:
                errors.append(f"actors[puppet].{k}: required when fill=model (Meraki amendment 2: actuals, not defaults)")
    else:
        for k in ("model_id", "provider", "model_requested", "model_returned"):
            if puppet.get(k) is not None:
                errors.append(f"actors[puppet].{k}: set on a code fill — masquerade risk")
    if bert.get("fill") == "model":
        for k in ("model_id", "provider"):
            if bert.get(k) is None:
                errors.append(f"actors[bert].{k}: required when fill=model")
    else:
        for k in ("model_id", "provider"):
            if bert.get(k) is not None:
                errors.append(f"actors[bert].{k}: set on a code fill — masquerade risk")


def _validate_run_config(m, errors):
    rc = m.get("run_config", {})
    if not isinstance(rc.get("turns"), int) or rc.get("turns") <= 0:
        errors.append("run_config.turns: positive int required")
    if not isinstance(rc.get("max_escalations_per_slot"), int) or rc.get("max_escalations_per_slot") < 0:
        errors.append("run_config.max_escalations_per_slot: non-negative int required")
    if rc.get("triggers") != "turn-indexed-only":
        errors.append("run_config.triggers: v01 is turn-indexed-only (landmark triggers withdrawn)")
    if rc.get("delivery_order") != "before-action":
        errors.append("run_config.delivery_order: FROZEN before-action (SPEC section 2)")
    if rc.get("fallback_ladder") not in ("on", "off"):
        errors.append("run_config.fallback_ladder: on|off")
    bfp = rc.get("bert_fixed_points")
    if bfp is not None:
        ok = bfp == "none" or (
            isinstance(bfp, list) and len(bfp) > 0
            and all(isinstance(s, int) and not isinstance(s, bool) for s in bfp)
        )
        if not ok:
            errors.append("run_config.bert_fixed_points: nonempty list[int] or the string 'none'")


def _validate_status_discipline(m, errors):
    status = m.get("status")
    actuals = m.get("actuals", {})
    if status == "paper-illustration":
        # Paper manifests can NEVER masquerade as finalized runs (SPEC section 3).
        for k in ("run_id", "started_at_utc", "ended_at_utc"):
            if actuals.get(k) is not None:
                errors.append(f"actuals.{k}: set on a paper-illustration manifest — masquerade")
        for k in ("turns_attempted", "turns_completed", "turns_accepted"):
            if actuals.get(k) is not None:
                errors.append(f"actuals.{k}: set on a paper-illustration manifest — masquerade")
        for k in ("notebook_bytes", "fallback_events", "bert_opportunities", "bert_deliveries"):
            if actuals.get("results", {}).get(k) is not None:
                errors.append(f"actuals.results.{k}: set on a paper-illustration manifest — masquerade")
    else:
        # A claimed-real run must be receipted.
        if not isinstance(actuals.get("run_id"), str) or not actuals.get("run_id"):
            errors.append("actuals.run_id: required for any non-paper status")
        if not isinstance(actuals.get("started_at_utc"), str) or not actuals.get("started_at_utc"):
            errors.append("actuals.started_at_utc: required for any non-paper status")
        if status == "completed":
            for k in ("ended_at_utc", "turns_attempted", "turns_completed", "turns_accepted",
                      "actual_event_log_sha", "actual_state_sha", "arm_config_sha",
                      "actual_prompt_sha"):
                if actuals.get(k) is None:
                    errors.append(f"actuals.{k}: required when status=completed")
            results = actuals.get("results", {})
            for k in ("notebook_bytes", "fallback_events", "bert_opportunities", "bert_deliveries"):
                if results.get(k) is None:
                    errors.append(f"actuals.results.{k}: required when status=completed")
            for k in ("transcript_sha", "notebook_sha"):
                if m.get("artifacts", {}).get(k) is None:
                    errors.append(f"artifacts.{k}: required when status=completed")


def validate_manifest(m: dict) -> list[str]:
    """Return a list of errors; an instantiated manifest is valid iff the list is empty."""
    errors: list[str] = []
    if not isinstance(m, dict):
        return ["manifest is not an object"]
    if m.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version: expected {SCHEMA_VERSION!r}, got {m.get('schema_version')!r}")
    if m.get("status") not in ENUM_STATUS:
        errors.append(f"status: must be one of {ENUM_STATUS}")
    if m.get("condition") not in ENUM_CONDITION:
        errors.append(f"condition: must be one of {ENUM_CONDITION}")
    if m.get("experiment_id") != "island-v01":
        errors.append("experiment_id: expected 'island-v01'")
    template_sans_actors = {k: v for k, v in TEMPLATE.items() if k != "actors"}
    _walk(template_sans_actors, {k: v for k, v in m.items() if k != "actors"}, "", errors)
    _validate_actors(m, errors)
    _validate_run_config(m, errors)
    _validate_status_discipline(m, errors)
    return errors
