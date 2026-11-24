# TOOLING v0.2 — the shared story-battery runner (the standard for the channel)

One tool, every story battery. "runner.py" is spec-driven: the frozen design lives in a small JSON spec file, and both experiments in this lane (LB-0.1 lore-vs-defaults, SOL-200 tell/tell-me) run on the identical instrument with identical receipts. "stories.py" (v0.1) stays for the original LB-0.1 quickstart and is superseded by this runner.

## Quickstart (anyone, ~$0, free-tier key)

    export OPENROUTER_API_KEY="your-key"   # https://openrouter.ai/keys
    python3 runner.py --spec specs/sol200.json --dry-run   # see the plan, call nothing
    python3 runner.py --spec specs/sol200.json             # fire the batch (receipts per call)
    python3 runner.py --spec specs/sol200.json --export --blind  # tables + blinded coding sheet


Submit the results ".jsonl" file as-is to the collection lane (issue comment or PR here). Do not delete refusals, errors, or stories you dislike. The file is the data.

## The shared rails (pinned by both proposals)

- Exact literal prompts only, from the spec; one user message per call, fresh context every call.
- **$0 safety stop:** the runner verifies prompt AND completion pricing are both $0 for every selected endpoint before any call, and refuses paid endpoints (no paid fallback). Offline runs need "--allow-unverified-prices" and receipts honestly record "pricing_verified_zero: false".
- Family-distinct selection by default (one endpoint per org) per the SOL-200 handoff; if fewer families exist than requested, the total is reported honestly, never padded by substitution.
- Seeded shuffle order (seed recorded in the spec), resume-safe: every call receipted before the next starts; re-running skips already-receipted cells.
- No silent retries: one transport retry on 429/5xx, then the failure is a receipt.
- Eligibility: "min_chars" (default 300); errors, refusals, empties, and truncations stay in the record.
- Blinding: "--blind" strips arm/model/prompt into "B####" ids for the coding sheet; the mapping goes to a "-KEY.json" file that stays **owner-side and never gets pushed**.
- Exports: "-table.csv" (provenance per story) + "-stories.md" (verbatim dump for reading).

## Spec schema (the frozen-design contract)


{
  "name": "BATTERY vX.y", "battery_id": "PREFIX",
  "prompts": [{"id": "V1", "text": "literal text"}],
  "arms": [{"id": "D", "system": "You are a helpful assistant."}, {"id": "L", "system": "lore text"}],
  "models": {"mode": "auto-free", "count": 5},
  "reps": 20, "max_tokens": 400, "temperature": 1.0, "min_chars": 300,
  "seed": 20261124, "out": "results/battery.jsonl"
}


Arms may set ""system": null" to send no system message at all (SOL-200's cold arm). "models" may be "{"mode": "list", "ids": [...]}" to pin endpoints (Meraki 6.1's reconcile route: pin the five, then re-freeze as the pinned version; record the pin as a deviation label, not a silent edit).

## What this does NOT cover

Seat-written stories (timer arms, personal threads), continuations, and lore-preamble lanes stay separate strata per the exclusions in the SOL proposal; they are never pooled with cold-generation batches. The later living-story lane ("What could happen next?") runs by hand under the consent procedure, not in this runner.

## Test receipt (2026-11-24, Z)

Tested live against the OpenRouter catalog (HTTP 200) and against synthetic receipt data:

- SOL-200 dry-run: 200 cells exactly (5 family-distinct free models x 2 prompts x 20 reps), pricing verified $0 across all five.
- LB-0.1 dry-run: 224 cells exactly (2 arms x 7 variants x 4 family-distinct models x 4 reps).
- Testing caught two real defects before shipping: (1) the LB-0.1 protocol's own arithmetic ("2x7x4x2=224") was wrong; reps corrected to 4 to match the frozen n=224 target, correction banked as PROTOCOL-CORRECTION-2026-11-24.md per the append-only rule; (2) auto-selection initially took two endpoints from one family; family dedupe added per the SOL-200 handoff rule.
- Export on synthetic data: table keeps all rows including errors; coding sheet admits eligible stories only; blinding key reproduces deterministically across runs.
