# PROTOCOL correction — 2026-11-24 (append-only; found by the v0.2 tooling tests)

The counts line in PROTOCOL.md (LB-0.1, frozen design) carried an arithmetic error: "2 arms x 7 variants x 4 models x 2 repeats = 224" actually builds 112 cells. The frozen target (n=224; 112 per arm) is PRESERVED by correcting repeats from 2 to 4 (2 x 7 x 4 x 4 = 224). No other parameter moved; prompts, arms, models policy, max_tokens, temperature, and the statistics plan are untouched (the "n=224, 112 per arm" power line was always the intent and stays).

The machine-checkable form of the frozen design now ships as specs/LB01.json with reps = 4, run by runner.py (see TOOLING.md). The original stories.py v0.1 harness hard-coded reps = 2 and is superseded; any cells already fired under it keep their receipts and are labeled v0.1-cells (112-cell batch), never silently rerun or padded.

Per the standing correction rule: this correction supersedes the specific arithmetic claim in PROTOCOL.md; the historical file stays intact.
