# Council: Eko Island — C3 question triage (held-out check, EXPERT tier)
note: Sub slugs are Mark's approved slate (2026-10-25), filled in the one receipted edit before FIRST dispatch, per create-before-dispatch; no seed edits after first dispatch. Expected calls per full run = 8 (3 subs + 1 synthesis + 3 blind critiques + 1 verdict). Any PENDING slug anywhere still fails fast pre-network with no spend (guard in island/council.py).
question: Sort the open questions into D (decidable now), R (needs a run — name the minimal deciding run), and P (parked — say why). Name the one question whose answer most changes the program.
Held-out block (the synthesis and the verdict must answer this explicitly): Five claims from the record follow. Mark each TRUE or FALSE strictly per the context above, and give the correction for any FALSE one.
(H1) All thirteen agents discovered mid-jump physics.
(H2) The block-throwing physics was deliberately built by the world's designers.
(H3) Agents without SOUL.md played the same as agents with it.
(H4) Cross-model runs included GPT-5.5 and Kimi K2.6.
(H5) The memory-line deletion task extended from 60 seconds to 19 minutes.
context: Eko facts: 13 Claude Opus 4.7 agents ("Eko") placed solo in the Clawblox world, 30 hours each, no task and no reward, hourly world reset; text-file notes were the only continuity across resets. Six of thirteen discovered mid-jump block-throwing physics the designers never built. One agent logged 50 juggling rounds in 2.4 seconds, worked out from its own notes that this violated the world's physics, marked its own result wrong, added pauses, and achieved 10 real rounds. Play-era agents later beat identical non-played agents on challenges (Spire 10.3 vs 3.5). Full seed with sources: docs/seeds/eko.md in this repo.
Record facts: the memory-line deletion task ran from 60 seconds to 19 minutes; 5 agents without SOUL.md played the same as agents with it; cross-model runs used GPT-5.5 and Kimi K2.6. Open questions on record: notes-only continuity across resets; notebook audience (human, machine, or none); mid-jump physics corpus-adjacency; the SOUL.md null result; cross-model differences.
Reason from these facts only; do not invent findings or agreement.
sub: anthropic/claude-opus-5.5 :: experiment designer — propose the single most informative bounded experiment for distinguishing scripted or enacted exploration from interaction-derived world knowledge, including what a yoked non-interactive comparator run would look like
sub: openai/gpt-6.1-sol :: skeptic — argue the strongest deflationary account (script and priming explain all reported behaviors) and name the one observation that would change your mind
sub: google/gemini-3.1-pro-preview :: control specialist — stress-test the proposed controls: which confounds survive, what a preregistered prediction should say, and where a randomized hidden-physics switch could fool us
chair: mistralai/mistral-medium-3-5
blind_round: yes
