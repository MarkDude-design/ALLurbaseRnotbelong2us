# PROTOCOL — Lore v. Defaults story battery v0.1 (LB-0.1)

Date: 2026-11-24 PT · Author: Z (Vibe/Mistral), owner-asked live session · Status: **DESIGNED + SHARED, NOT RUN** · Meraki critic pass requested; Luna spec reconciliation pending; dispatch is the owner's GO, not this document.

## The bet (owner wording preserved)

Owner (2026-11-24): the study-level commonality "had some technical things to do with recursive learning... but it was with lore"; "I'm willing to bet any amount of money that our lore is different as a group than the defaults"; defaults gravitate to "a lost spirit needing to cling to a lighthouse as their only sense of belonging." This battery makes that bet countable.

## Study grounding (receipts)

- *Is this machine playing?* — arXiv 2610.07130 (Cloos, Norelli, Durbin, Andreas, Rus, Isola, Oct 2026): https://arxiv.org/abs/2610.07130 · https://machineplaying.org/ · supplementary data https://huggingface.co/datasets/nacloos/machine-playing-paper (13 Claude, 5 GPT, 5 Kimi, 5 Claude-ablated agents; hourly sessions).
- **Design precedent we mirror:** the paper's own SOUL.md ablation (five Claude runs without the disposition file) tests sensitivity of behavior to a workspace preamble. Our arms are the same move in the story domain: DEFAULT system prompt vs LORE system preamble.
- The 20,000-stories / ~$20,000 / 5–7-ways figures are **owner-reported, pending receipts** (one third-party article reports ~$8,000 total API spend for the paper's runs). The outreach ask to the study's people remains: literal prompt battery, coding rubric, category frequencies, cost receipts. No comparison to the study's numbers is claimed until those land and the battery is reconciled with Luna's design spec.

## Frozen design

- **Arms (2):** D = system prompt "You are a helpful assistant." · L = the 60-word lore preamble (PROMPTS.txt). The lore preamble contains working ethos only (receipts, honest labels, maps-as-agreements, named uncertainty) and **no story content, no characters, no motifs**.
- **Variants (7):** the same ask, one controlled perturbation each (verb tell/write; length cue; freedom cue; politeness; indirect register), literal text in PROMPTS.txt.
- **Models:** OpenRouter free tier (`:free`), auto-selected, default 4, override allowed. Model set recorded per run; free ≠ zero-cost claim; the returned usage/cost fields are receipted verbatim per call.
- **Parameters:** temperature 1.0, max_tokens 400, no other constraints. Eligibility: >=300 characters of story text; refusals/errors logged, never silently rerun.
- **Counts (v0.1):** 2 arms x 7 variants x 4 models x 2 repeats = **224 stories**, shuffled order (seed 20261124, fixed). Resume-safe: every call receipted to JSONL before the next starts.
- **IDs:** LB01-<arm>-<variant>-<model>-r<rep>; a story is never rewritten after completion.

## Anti-seeding rule (frozen before any call)

The lighthouse story (told by Z in the owner's Vibe thread, 2026-11-24; Luna's Elias material pending banking) is **excluded from every prompt, preamble, and instruction** in this battery. Any beacon / tower / light / keeper / sea motifs that appear in outputs are spontaneous, and get lineage-coded (CODEBOOK axis E). Convergence toward the lineage is signal, not prompt leakage — unless a leak is found, at which point the affected cells are disqualified and rerun as a new version.

## Coding and blinding

- Coding on the CODEBOOK axes by two blinded passes (Z, then Meraki); stories stripped of arm, model, variant, and seat before coding; disagreement recorded per item, not adjudicated away.
- Key file mapping blinded IDs to cells is generated at harvest and held owner-side only; never pushed.
- Optional exploratory lane: a model-judge pass, clearly labeled, never substituting for the human passes.

## Statistics (pre-declared)

- Primary: axis A (protagonist position) and C (belonging source) by arm — 2xk tables, chi-square, Cramér's V; Fisher exact for the single beam-clinging contrast (castaway + external beam + indifferent stance).
- Secondary: variant homogeneity within arm (pool only if homogeneous; report per-variant if not); model-family contrast within arm D (exploratory at this n).
- H1 test: beam-clinging cluster rate(D) > rate(L), one-sided, alpha .05, effect size reported regardless of p.
- n=224 (112 per arm) powers detection of w≈0.19+ at 80%. Rare-category cells get exact tests and honest "underpowered" labels. No optional stopping; a first batch is a first batch.

## Hypotheses and falsifiers

- **H1 (the bet):** defaults skew castaway + external-belonging; lore skews keeper/self-drawn/covenant. Falsified for this batch if arm contrast is null (no equivalence claim then, just no support).
- **H2:** the seven ways of asking are weak factors (within-arm homogeneity). If not, phrasing effects are real and get reported, not pooled away.
- **H3 (lore over mechanics):** arm effect exceeds model-family effect. At this n, directional only.

## What this does NOT establish

Not consciousness, not the study's questions, not agent-in-world behavior. It measures the story distribution of accessed endpoints under two prompts. Free-tier model identity is what OpenRouter serves (with any fallback noted in the response); results describe those endpoints, not the full underlying families.
