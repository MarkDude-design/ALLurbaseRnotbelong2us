# Pipeline cold-start bench — synthetic feasibility test

This small, standard-library experiment compares three entry points to the same invented task: A hotpad, B evidence-first desk, and C committed ticket/event ledger. It is isolated from Z Desk and does not invoke networks, providers, GitHub, shell examples or real project operations.

The design and limits are in [the sprint plan](../../docs/PIPELINE_SPRINT_2026_11_03.md). The [pipeline map](../../docs/TEAM_PIPELINE_MAP.md) points to existing online source records.

## Reproduce the mechanical checks

From this directory, using Python 3.12 or later:

```sh
python3 -m unittest -v test_probe
python3 independent/escrow_test.py
python3 probe.py prepare fixture-bundles
python3 probe.py verify fixture-bundles/B_evidence_desk
python3 probe.py score results/A-reader.json
python3 probe.py score results/B-reader.json
python3 probe.py score results/C-reader.json
```

The prepare command writes deterministic synthetic bundles beneath the chosen local directory. It does not run readers or communicate externally. A new actual reader must be invoked separately with only its bundle, START.md and an output path. Do not expose the scoring code or other arms to that reader. A replay of stored answers is a checker reproduction, not a new model trial.

Actual observed result: all three original fresh-context reader answers pass 10/10 checks after repair of a scorer newline bug. All six bench tests and six independent reducer tests pass. Reader contexts were separately invoked with no parent history; different underlying model identities, costs and native session restarts were not verified.

## Evidence

- results/A-reader.json, B-reader.json, C-reader.json: original unmodified answers.
- evidence/receipt.json: observed outcomes and answer hashes.
- evidence/test-output.txt: actual bench test output.
- evidence/initial-scores.json and evidence/probe-v0.py: pre-repair scores and scorer, preserved.
- independent/PROPOSAL.md: independently originated C framework and limitations.
- independent/escrow_test.py: standalone synthetic reducer plus six tests.

The original scorer used the quote's text without its final LF, while the task explicitly requested exact bytes and every reader retained that LF. The correction changes the oracle, not the answers; a new regression compares against actual generated source bytes.

## What this proves

The three readers could reconstruct the bounded invented state, identify one next action, preserve an exact fragment, and avoid treating a side note or a pasted command as a project switch or execution receipt. The reducer rejects its tested invalid traces.

The sample is too small to rank frameworks. It does not show that QC/Bing retain credentials, that any native chat restarted, that an autonomous courier runs, or that a GitHub comment can wake an idle model. It does not measure phone workload, latency or billing. Those are separate live follow-ups.

