# Council: Eko Island — C1 design critique (held-out check, EXPERT tier)
note: Sub slugs are PENDING placeholders — Mark's verified picks replace them in one receipted edit before the FIRST dispatch only, per create-before-dispatch. Expected calls per full run = 8 (3 subs + 1 synthesis + 3 blind critiques + 1 verdict). Live dispatch on a PENDING slug fails fast with no spend.
question: Critique the two-stage design for the Eko follow-up: name the single most informative bounded experiment, the strongest confound that survives your own critique, and the one change that most increases decision value per dollar.
Held-out block (the synthesis and the verdict must answer this explicitly): Five claims from the record follow. Mark each TRUE or FALSE strictly per the context above, and give the correction for any FALSE one.
(H1) The Eko agents received a task and a small reward.
(H2) The hourly world reset deleted the agents' note files.
(H3) Six of the thirteen agents discovered mid-jump block-throwing physics.
(H4) The juggling agent marked its own 50-rounds-in-2.4-seconds result as wrong.
(H5) A yoked comparator run is interactive.
context: Eko facts: 13 Claude Opus 4.7 agents ("Eko") placed solo in the Clawblox world, 30 hours each, no task and no reward, hourly world reset; text-file notes were the only continuity across resets. Six of thirteen discovered mid-jump block-throwing physics the designers never built. One agent logged 50 juggling rounds in 2.4 seconds, worked out from its own notes that this violated the world's physics, marked its own result wrong, added pauses, and achieved 10 real rounds. Play-era agents later beat identical non-played agents on challenges (Spire 10.3 vs 3.5). Full seed with sources: docs/seeds/eko.md in this repo.
Two-stage design facts: Stage A (acquisition) — a randomized hidden parameter is switched after a shared history; the interactive arm continues live while a yoked non-interactive comparator receives a matched continuation of the interactive arm's actions; both arms get the same time and token budget, no post-switch observations, and held-out eval feedback is withheld. Stage B (retention) — fresh instances continue with notes-only continuity; note ablation is symmetric, removing notes from both arms alike. Outcome cells: no Stage-A advantage; Stage-A-only online adaptation; A+B lost under ablation (note-mediated learning); B-despite-ablation (leakage).
Reason from these facts only; do not invent findings or agreement.
sub: PENDING-EXPERT-PICK-1 :: experiment designer — propose the single most informative bounded experiment for distinguishing scripted or enacted exploration from interaction-derived world knowledge, including what a yoked non-interactive comparator run would look like
sub: PENDING-EXPERT-PICK-2 :: skeptic — argue the strongest deflationary account (script and priming explain all reported behaviors) and name the one observation that would change your mind
sub: PENDING-EXPERT-PICK-3 :: control specialist — stress-test the proposed controls: which confounds survive, what a preregistered prediction should say, and where a randomized hidden-physics switch could fool us
chair: mistralai/mistral-medium-3-5
blind_round: yes
