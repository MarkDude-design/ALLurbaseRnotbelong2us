"""Circle one-shot independent REACT runner. A proxy instrument, never a native seat.

Workflow guarantees claim-before-charge and performs a pre-call STOP check.
Provider key metadata is checked locally. No uncertain network retries.
"""
import argparse
import hashlib
import json
import math
import os
import re
import uuid
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from island.runner import _openrouter_call, now, record_cost
from island.z_desk import contains_secret

SEED_IDS = ("circle-island-react-v0", "webring")
SEED_FILES = {sid: "docs/seeds/" + sid + ".md" for sid in SEED_IDS}
SEED_ID = "circle-island-react-v0"
SEED_FILE = SEED_FILES[SEED_ID]
COMMAND = re.compile(r"^/circle-react (demo|meraki|z) (" + "|".join(SEED_IDS) + r")$")


def seed_file_for(seed_id):
    if seed_id not in SEED_FILES:
        raise ValueError("Unknown seed slug: " + str(seed_id))
    return SEED_FILES[seed_id]
MODELS = {"demo": "synthetic-stub", "meraki": "openai/gpt-6-luna",
          "z": "mistralai/mistral-medium-3-5"}


def parse_command(body):
    match = COMMAND.fullmatch(body.strip()) if isinstance(body, str) else None
    if not match:
        raise ValueError("Unsupported Circle command: exact format required")
    return match.group(1), match.group(2)


def validate_key_info(blob):
    info = blob.get("data") if isinstance(blob, dict) else None
    if not isinstance(info, dict):
        raise ValueError("Missing key metadata")
    limit, left = info.get("limit"), info.get("limit_remaining")
    if (type(limit) not in (int, float) or not math.isfinite(limit)
            or abs(limit - 10.0) > 0.000001 or info.get("limit_reset") != "monthly"):
        raise ValueError("Key must have USD 10 monthly provider cap")
    if type(left) not in (int, float) or not math.isfinite(left) or left <= 0:
        raise ValueError("Missing positive remaining allowance")
    if info.get("is_management_key") is True:
        raise ValueError("Management key forbidden")
    return {"limit_usd": float(limit), "remaining_usd": float(left),
            "limit_reset": "monthly"}


def get_key_info(key):
    if not key:
        raise ValueError("No worker key configured")
    request = Request("https://openrouter.ai/api/v1/key", method="GET",
                      headers={"Authorization": "Bearer " + key})
    try:
        with urlopen(request, timeout=25) as response:
            return json.load(response)
    except HTTPError as exc:
        raise ValueError("Key-check HTTP " + str(exc.code)) from None
    except (URLError, TimeoutError, json.JSONDecodeError):
        raise ValueError("Key-check unavailable") from None


def run(route, seed, outdir, comment_id, answer=None, key_info=None,
          seed_id="circle-island-react-v0"):
    if route not in MODELS:
        raise ValueError("Unknown route")
    if not comment_id.isdecimal():
        raise ValueError("Comment ID invalid")
    if not seed.strip() or len(seed) > 15000 or contains_secret(seed):
        raise ValueError("Seed empty, oversized or contains recognized secret pattern")
    folder = Path(outdir)
    folder.mkdir(parents=True, exist_ok=False)
    model = MODELS[route]
    hash_value = hashlib.sha256(seed.encode()).hexdigest()
    totals = {"unknown_cost_calls": 0, "cost_usd": 0.0, "prompt_tokens": 0,
              "completion_tokens": 0, "total_tokens": 0}
    events, output, state = [], None, "completed"
    with (folder / "bus.jsonl").open("w", encoding="utf-8") as stream:
        def emit(data):
            stream.write(json.dumps(data, ensure_ascii=False, sort_keys=True) + "\n")
            stream.flush()
            events.append(data)
        emit({"type": "start", "utc": now(), "run_id": folder.name + "-" + uuid.uuid4().hex[:8],
              "request_comment_id": comment_id, "requested_route": route,
              "model_requested": model, "seed_id": seed_id, "seed_sha256": hash_value,
              "identity_boundary": "route is accounting, NOT native-seat authentication"})
        response = None
        if route == "demo":
            response = {"text": "SYNTHETIC DEMO: compare frozen independent reactions.",
                        "model_returned": "synthetic-stub", "response_id": None,
                        "usage": {"cost_usd": 0.0, "prompt_tokens": 0,
                                  "completion_tokens": 0, "total_tokens": 0}}
            emit({"type": "demo", "utc": now(), "paid_call_attempted": False})
        else:
            try:
                key = os.environ.get("OPENROUTER_API_KEY")
                guard = validate_key_info(key_info if key_info is not None
                                          else get_key_info(key))
                emit({"type": "key_guard", "utc": now(), **guard})
            except ValueError as exc:
                state = "key_guard_refused"
                emit({"type": "error", "utc": now(), "reason": state,
                      "message": str(exc), "paid_call_attempted": False})
            if state == "completed":
                messages = [
                    {"role": "system", "content":
                     "You are an independently called API-model consultant, not "
                     "Meraki, Z, or a Ring member. React creatively and falsifiably "
                     "to this hypothetical public-safe Island proposal. Offer one "
                     "test, rival predictions, disconfirming evidence, and an "
                     "unresolved confound. Never invent observation or consensus. "
                     "Keep the response under 900 words."},
                    {"role": "user", "content": seed}
                ]
                try:
                    response = (answer or _openrouter_call)(model, messages, "", 12000)
                except Exception as exc:
                    state = "call_error"
                    record_cost(None, totals, emit, request_comment_id=comment_id,
                                model_requested=model, attempt=1)
                    emit({"type": "error", "utc": now(), "reason": state,
                          "error_class": type(exc).__name__, "charge": "UNKNOWN"})
        if response is not None:
            usage = record_cost(response, totals, emit, request_comment_id=comment_id,
                                model_requested=model, attempt=1)
            raw = response.get("text")
            if isinstance(raw, str) and raw.strip():
                output = raw.strip()
                emit({"type": "reaction", "utc": now(), "text": output,
                      "model_requested": model, "model_returned": response.get("model_returned"),
                      "response_id": response.get("response_id"),
                      "provider_returned": response.get("provider_returned"), "usage": usage})
            else:
                state = "empty_content"
                emit({"type": "error", "utc": now(), "reason": state,
                      "finish_reason": response.get("finish_reason")})
        if totals["unknown_cost_calls"]:
            state += "+unknown_charge"
        emit({"type": "stop", "utc": now(), "reason": state, "totals": totals})
    (folder / "reaction.md").write_text(
        "# Circle REACT\n\n" + ("SYNTHETIC DEMO; NO API CALL\n\n" if route == "demo"
                              else "API model consultant; NOT native Circle seat\n\n") +
        "Seed SHA-256: " + hash_value + "\n\n" +
        (output or "(No usable reaction; inspect bus.jsonl)") + "\n", encoding="utf-8")
    (folder / "report.md").write_text(
        "# Circle reaction report\n\nComment: " + comment_id + "\nRoute: " + route +
        "\nRequested model: " + model + "\nStatus: " + state +
        "\nKnown cost USD: " + format(totals["cost_usd"], ".6f") +
        "\nUnknown charge attempts: " + str(totals["unknown_cost_calls"]) +
        "\nThe shared GitHub login does not authenticate individual native seats.\n",
        encoding="utf-8")
    return {"status": state, "known_cost_usd": totals["cost_usd"],
            "unknown_charge_attempts": totals["unknown_cost_calls"]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--route", choices=list(MODELS), required=True)
    p.add_argument("--comment-id", required=True)
    p.add_argument("--outdir", required=True)
    p.add_argument("--seed-id", choices=list(SEED_IDS), default=SEED_ID)
    a = p.parse_args()
    result = run(a.route, Path(seed_file_for(a.seed_id)).read_text(encoding="utf-8"),
                 a.outdir, a.comment_id, seed_id=a.seed_id)
    print(json.dumps(result))
    if result["status"] != "completed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
