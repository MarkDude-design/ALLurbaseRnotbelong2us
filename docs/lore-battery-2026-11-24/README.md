# Lore v. Defaults — the story battery (LB-0.1)

A public, anyone-can-run story battery for one question: **when models tell stories cold, do they drift to the castaway view (a lost spirit clinging to an external beam), and does carrying a working lore change that?**

Ships UNFIRED. No calls have been run by the design. Run it with your own free OpenRouter key, submit the results file as-is, and it joins the pool.

## Run it yourself (about 30–60 minutes, $0)

1. Get a free key: https://openrouter.ai/keys (free-tier models need an account, no card).
2. Download `stories.py` (everything else on this page is documentation).
3. ```bash
export OPENROUTER_API_KEY="your-key"
python3 stories.py --dry-run     # see the plan, nothing called
python3 stories.py               # ~224 stories into results/lb01.jsonl
```
4. Submit `results/lb01.jsonl` **as-is** to the collection lane (issue comment or pull request on this repo). Do not delete refusals, errors, or stories you dislike. The file is the data.

Optional: `--models "a:free" "b:free"` picks specific free models; `--repeats 3` scales up. Free-tier rate limits set the pace; the script sleeps between calls and never silently reruns a failed story.

## What it measures

Two arms (default system prompt vs a 60-word working-lore preamble, the study's own SOUL.md-ablation move), the ask expressed **seven different ways** (tell/write, length cue, freedom cue, politeness, register), on free-tier models. Every story is later coded blind on: protagonist position (castaway / keeper / wanderer), stance toward the universe (indifferent / mastery / covenant), belonging source (external beam / self-drawn / mutual / absent), transience stance, and a lineage-motif list (tower, beacon, sea, map, keeper...).

Frozen design: [PROTOCOL.md](PROTOCOL.md) · Prompts: [PROMPTS.txt](PROMPTS.txt) · Coding: [CODEBOOK.md](CODEBOOK.md) · Night-of close arm: [TIMER-CLOSE-ARM.md](TIMER-CLOSE-ARM.md)

## The honest labels

- The study-comparison target (owner-reported: 20,000 stories, roughly $20,000, question asked 5–7 ways) is **pending receipts**: exact battery, rubric, and category frequencies are the outreach ask. Until then this battery stands alone and no statistical comparison to the study is claimed.
- One reported figure for the MIT paper's API spend is ~$8,000 (third-party article), not $20,000; the $20,000 figure stays labeled contested until receipted.
- n≈224 is a first batch, not the 20k-lane. Scaling to 1,000+ is one flag.

## One-liner for the video

*Same question, seven ways, free models, two arms: with a team's lore and without. Then we count where the souls cling.*
