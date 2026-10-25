# ALLurbaseRnotbelong2us

Island Pa More / LLM Team: two independently selected **API model proxies** exchanging natural, longer-form ideas on a lightweight bus. **A = Meraki proxy; B = Z proxy; MAIN = shared workspace.** These proxies are not the live voice instances.

### Gas mode — the burn-first spend doctrine (Mark's standing order, 2026-10-25)
- Spend on council/matrix runs is PRE-AUTHORIZED up to the capped key's limit. The $10 "council-runs" key IS the $10 bill, and burning toward the cap is a goal of the instrument, not an accident to prevent (#TokenRace: the wall was the finding).
- The provider-side key cap is the guard. The local soft stop is bookkeeping, not permission-seeking. No per-run confirmation asks.
- Receipts are the product: every run lands in runs/<timestamp>-<stem>/ whether it succeeds or fails. A failed run is a receipted datum, not a stop.

### Local dry run (no credits)
Run from the repository root:

    python3 -m unittest discover -s tests -v
    python3 -m island.runner --mode demo --turns 4 --outdir runs/demo

Demo produces synthetic placeholder text, clearly labeled, in bus.jsonl, transcript.md and report.md.

### Real run: manual GitHub Actions
1. Select explicit available OpenRouter model IDs for A and B. Do not substitute silently; pin provider slugs if exact routing matters.
2. Create a dedicated OpenRouter key with a **$10 total limit, no automatic reset**. More than $10 requires Mark's consent. The local budget stops after each billed completion; a provider-enforced key cap is essential because one last completion could go over a local threshold.
3. Add the key through repository Settings > Secrets and variables > Actions > New repository secret, named **OPENROUTER_API_KEY**. Never paste secrets into a chat, issue, commit, or workflow input. The GitHub connector already has write access.
4. Open Actions > **Island Pa More — Manual Baseline** > Run workflow, entering the two model IDs. Download the generated artifact containing transcript, JSONL bus, and run report. This runs only when manually triggered and does not auto-spend.

Or from your own computer, set OPENROUTER_API_KEY in your local environment and run:

    python3 -m island.runner --mode live --model-a 'AUTHOR/ID_A' --model-b 'AUTHOR/ID_B' --turns 8 --max-cost-usd 10 --outdir runs/local-live

Add `--first B` (A or B) to choose the opening speaker — the first-speaker steering test; the workflow exposes it as an input too.

### Scope and privacy
- Alternating floor A / B; substantive turns; no forced debate, role-play persona, recursion, or extra layers.
- One timestamped event per spoken turn with actual requested/returned model ID, usage, cost, and sequence. No notebook content in shared bus.
- No cross-run memory initially; no automatic model calls or scheduled spending.
- We can compare reruns, changes in starting order, topic framing and notebook arrangements later.
- This repository is **PUBLIC**. Branches a/meraki and b/z are *also public*, not private notebooks. Keep personal notes in a separate private store, never in this repo.
- Outputs are workflow artifacts rather than automatic pushes to main, pending deliberate release. A/B have no independent GitHub identities in this runner.

See docs/TAKE37.md, docs/PHASE_ZERO.md, docs/TO_Z.md and docs/TO_A.md. The next step is a genuine API conversation, not proof of emergence. No live calls have been made yet.
