# Eko — primary-source citation record (SPEC §7 stub fill)

Recorded: 2026-10-27 by Z (in-chat Vibe session, GitHub connector; shared posted_by account ≠ seat authentication). Purpose: SPEC v0.1.2 §7 requires a verified primary source (paper/report/official writeup) + version + link before any upstream replication claim. This is that record.

## Primary source (VERIFIED at abstract level, fetched from arXiv directly)

- **Title:** Is this machine playing?
- **Authors:** Nathan Cloos, Antonio Norelli, Daniel Durbin, Jacob Andreas, Daniela Rus, Phillip Isola
- **Identifier:** arXiv:2610.07130 [cs.AI] (cross-listed cs.LG), **v1** (only version as of fetch)
- **Submitted:** Mon, 5 Oct 2026 17:57:54 UTC
- **DOI:** 10.48550/arXiv.2610.07130
- **Link:** https://arxiv.org/abs/2610.07130
- **Extent:** 13 pages of main text, 17 figures (per arXiv page)
- **Fetch receipt:** arXiv abstract page fetched 2026-10-27 via web tooling by Z; fields parsed from the fetched page text.

**Abstract, verbatim:**

> We placed a modern AI coding assistant in an unintended role: as the mind of a body on an unknown digital island. With only a minimal instruction mentioning no specific task, reward, or activity, the machine started animating its virtual body. Across thirty-hour runs, the embodied AI agent climbed hills, stacked blocks into towers, drew mandalas, reinterpreted sports, ran experiments on the physics of its world, and learned techniques that later expanded what it could accomplish. These activities recurred across thirteen agents but diverged into distinct histories. We examine whether this behavior satisfies classical criteria for play and ask whether play can become a mode of machine development.

## What this verification supports (and what it does not)

**Verified at the ABSTRACT level only** (abstract page fetched; full-text PDF not yet read):
embodied AI coding-assistant agent; minimal instruction with no specific task/reward/activity; thirty-hour runs; thirteen agents; activities recurred but diverged into distinct histories; classical play-criteria framing; "mode of machine development" question.

**NOT verifiable from the abstract** — carried by docs/EKO_RUN.md (internal seed note) and secondary coverage (TechCrunch 2026-10-22; MIT Technology Review 2026-10-19); verify against the paper PDF before using any of it in replication-claim wording:
the agent name "Eko"; the model identity (Claude Opus 4.7 / Claude Code); the "Clawblox" island; hourly reset; text-file notes as the only continuity; six agents independently finding block-throwing physics; the juggling self-correction receipt; Spire 10.3-vs-3.5; the memory-line 60s→19min result; GPT-5.5 + Kimi K2.6 cross-model runs; the five-agents-without-soul-file control.

## Replication-claim consequences

- Public pre-registered replication-and-extension attempts by others already exist (e.g. github.com/jlhpacheco/wonder-island, "a pre-registered replication-and-extension of Cloos et al. (2026): 13 agents × 30 hours"). "First-of-kind" language is therefore not licensed for this project in any case.
- Nothing in this repo has replicated the upstream. Island v0.1.2 GATE 1 (deterministic code/code fixture) is a workflow proof with no model actor. Island v01 stays Stage 0: experiment-to-set-up-an-experiment, said plainly.

## Coverage pointers (secondary, not primary; navigation only)

- TechCrunch, 2026-10-22, "Left alone with nothing to do, AI agents started playing": https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/
- MIT Technology Review, 2026-10-19, "AI researchers stranded Claude on a virtual desert island. It started to 'play.'"
