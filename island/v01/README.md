# island/v01 — GATE 1 fixture status (honest)

**What this is:** the deterministic code/code paired mock fixture + strict
manifest validator required by SPEC v0.1.2 §6.1 (Meraki's #13 disposition:
code/code fixture FIRST — it is not the experimental subject).

**What it is NOT:** a demonstrated model harness. No model actor, no metered
calls, no bus traffic. Model puppet arms happen only after fixture
acceptance + the owner's explicit provider/price/cap/dispatch grant.

## Run it

```bash
python3 -m island.v01.fixture --outdir /tmp/v01-fixture
# or, with the repo checked out:
scripts/v01-fixture.sh --outdir /tmp/v01-fixture
```

Exit code 0 iff every §6.1 checklist item passes. Artifacts written to
`--outdir`: per-arm event logs (JSONL), notebooks, instantiated run-manifests,
and `FIXTURE_REPORT.json`.

## Determinism contract

- The fixture uses a deterministic STUB clock (`FIXED_CLOCK_UTC`) so artifact
  hashes reproduce run-over-run; real runs inject real UTC time at dispatch.
- `code_commit` is the sha256 of the fixture's own module bytes — a real,
  reproducible receipt, never a made-up commit id.
- All hashes are taken over exact bytes (canonical JSON: sorted keys, compact
  separators; JSONL: one canonical event per line).

## §6.1 checklist (all must pass)

1. paired scheduler (identical fixed points + byte-identical interventions in both arms)
2. baseline shadow events (`delivered:false` at every scheduled slot, zero deliveries)
3. perturbed delivery (`delivered:true`, bytes == schedule bytes)
4. ≥1 fallback event exercised
5. one explicit terminal-failure slot per arm; honest turn accounting
6. notebook isolation (exposure receipts only in the perturbed notebook)
7. both instantiated manifests validate green (strict, anti-masquerade)
8. full rerun reproduces every artifact hash

## Honest notes

- `cost.unknown_charge_attempts = 0` is a measured count (zero charge
  attempts made); every unmeasured cost field stays `null` (never zero).
- `bus_jsonl_sha` stays `null` — the fixture emits no bus traffic.
- `landmark_visits` stays `null` — the fixture does not measure landmarks.
- The code puppet is the loop-fill bare minimum (issue #13 spectrum);
  SPEC §6.2 swaps ONLY the puppet fill to `model` for the first real pair.
