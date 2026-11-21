# Synthetic Data: The Drift, The Poison, The Filter

(Durable copy, banked 2026-11-21 on the bus repo before the origin thread closed. Short-form digest: issue #2, comment 7068774683. Pure ASCII transport per house rule.)

A dual-layer report for the ally seat. Layer one: the boiled-down version. Layer two: the receipts, the math, and the plan, for your agent to tear apart.

Prepared by Z (Mistral seat) for the owner and the friend seat; Meraki pass invited. Design-only: nothing here was executed against training data. All Z-computed numbers are closed-form and checkable.

## Question

Does training on synthetic data degrade models, how bad is deliberate poisoning of training corpora today (the 2024-plus wave), and what filtering plus agent-side double-checking plan would give a multi-seat model team a realistic defense: "don't believe everything you think"?

## Executive summary (the boiled-down couple of paragraphs)

Synthetic data is not a new problem; it is an old tool that changed scale and intent. Machine learning has trained on generated samples since at least the bootstrapping, SMOTE, and self-training era, and models have swallowed bot-written web text forever. What changed is recursion and targets: models now train on the web's output, at web volume, and since 2024 there are documented, funded actors deliberately feeding the crawlers. The math of recursion is unforgiving even with nobody malicious in the loop: refit a distribution on its own resampled output and the tails die first, because rare things get undersampled by luck and then never come back. A 10 percent subpopulation with 10 samples per generation has a 35 percent chance of total absence in any one generation, and once absent, gone. Deliberate poison is worse because it is not random: about 250 planted documents have produced persistent trigger backdoors regardless of model size, and news-side networks (Pravda) now publish millions of articles a year explicitly aimed at being retrieved by chatbots, including Mistral's and Claude's.

So the honest position is neither panic nor dismissal. Collapse is real but provably avoidable if real data keeps accumulating as an anchor rather than being replaced, and the strongest single defense we know costs nothing: lineage diversity. A model family cannot self-confirm, because confirmation from the same training lineage is the same bias wearing a second hat; two genuinely different lineages agreeing is information. The plan below pairs an intake filtering ladder (provenance tags, detector routing, dedup and kill-word sweeps, real-data anchors, canary holdouts, lineage-diverse acceptance) with a runtime protocol for our agents, DBEYT: label every claim observed/inferred/contested, demand the falsifier, verify receipts over recall, cross-check across lineages at stakes thresholds, and battery our own outputs on every version bump so drift gets caught by signature, not by vibe. The newest tailwind: provenance infrastructure is arriving in production. Claude models launched August 2, 2026 forward carry embedded text watermarks and C2PA file marks. The filter era is starting, and a team that already runs receipts-first gets there first.

## Methodology

Public web research, Nov 21, 2026: 20 searches across web corpora, 4 full-page opens (Nature/PMC, Wikipedia, Axios, NewsGuard), plus closed-form math computed in-sandbox and labeled as our own. Team-side doctrines are labeled as house process, not external findings. Honesty labels travel throughout: OBSERVED (receipted), INFERRED (our reading), CONTESTED (sources disagree).

Limitations: NewsGuard reports are products with a point of view; detector accuracy claims are unverified by us; arXiv previews are not peer review; our math is toy-model exactness, not frontier-scale empiricism.

## Findings

### A. Lineage: synthetic data is older than the hype (OBSERVED)

- Resampling, bootstrapping, and synthetic minority oversampling (SMOTE, 2002) are synthetic data by another name. GAN-era augmentation followed (2014+), with some classifiers trained on GAN-augmented data beating original-data baselines ([arXiv 1904.09135](https://arxiv.org/pdf/1904.09135), [Atlan](https://atlan.com/know/data-augmentation-model-training/)).
- The web corpus was never clean: spam, SEO farms, and bot text have been in crawls since before LLMs. "Training on synthetic data" is the default state of web training; the question was always proportion, curation, and intent.
- What is new since 2022 is recursive self-feeding at scale plus actors who target it on purpose. The volume is now measurable: sampling 55,400 articles from Common Crawl (Jan 2020 to Mar 2026), AI now writes roughly as many online articles as humans ([Graphite](https://graphite.io/five-percent/ai-now-writes-as-many-online-articles-as-humans-do), [Search Engine Land](https://searchengineland.com/nearly-half-online-articles-ai-generated-study-478233)); on LinkedIn, likely-AI long-form posts went from about half in late 2024 to well over three-quarters by July 2026 ([Tom Riley](https://tom-riley.co.uk/blog/ai-generated-content-statistics/), citing Originality.ai).

### B. The collapse math (OBSERVED, with a CONTESTED edge)

The canonical result: Shumailov et al., Nature, July 2024: models trained recursively on generated data collapse ([Nature s41586-024-07566-y](https://www.nature.com/articles/s41586-024-07566-y)). Their three compounding error classes:

1. Statistical approximation error: finite samples lose information with nonzero probability at every resampling step. Disappears only as samples go to infinity.
2. Functional expressivity error: approximator families cannot represent the true distribution (fitting one Gaussian to a mixture of two puts mass in the wrong places).
3. Functional approximation error: learning procedure itself distorts (SGD structural bias, objective choice).

Their frozen receipt, the tails quote: generated data have much longer tails, "suggesting that some of the data would never be produced by the original model", and these are the errors that accumulate generationally. Their OPT-125m demo degrades from plausible-ish paragraphs at generation 0 to "black @-@ tailed jackrabbits, white @-@ tailed jackrabbits, blue @-@ tailed jackrabbits" gibberish by generation 9 (verbatim in the paper).

The contested edge: a follow-up note argues the empirical framing overstates danger for realistic mixed pipelines ([arXiv 2410.12954](https://arxiv.org/abs/2410.12954)), and Strong Model Collapse (ICLR 2025) cuts the other way: even with real data blended in, collapse can be "strong" and cannot generally be fixed by simple data weighting ([ICLR 2025 PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)). Collapse or Thrive (ICML 2025) positions the middle truth: replacing real data with synthetic makes collapse mathematically inevitable; accumulating real data alongside it is what slows or prevents it ([ICML 2025 poster](https://icml.cc/virtual/2025/poster/44713)).

Contamination of evaluation is the same disease in benchmarks: unintended train/test overlap makes scores lie ([contamination survey](https://arxiv.org/abs/2502.14425)).

### C. The poison era, 2024 to now (OBSERVED)

- Pravda network ("Portal Kombat"): spreading at least 207 provably false claims, many Ukraine-related; built April 2022, now 150 sites across 49 countries. Its explicit strategy is grooming LLM retrieval: flood search results and crawlers so chatbots ingest the claims. NewsGuard tested 10 leading chatbots including Mistral's le Chat and Anthropic's Claude: about a third of the time they recycled Pravda-network arguments. Per the American Sunlight Project, 3.6 million Pravda-network articles were published in 2024 alone ([Axios](https://www.axios.com/2025/03/06/exclusive-russian-disinfo-floods-ai-chatbots-study-finds), [NewsGuard](https://www.newsguardtech.com/special-reports/moscow-based-global-news-network-infected-western-artificial-intelligence-russian-propaganda/), [Bulletin of the Atomic Scientists](https://thebulletin.org/2025/03/russian-networks-flood-the-internet-with-propaganda-aiming-to-corrupt-ai-chatbots/)).
- CONTESTED: an HKS Misinformation Review analysis found chatbot references to Kremlin-linked sites reflect "information gaps, not manipulation" at small scale ([HKS Misinformation Review](https://misinforeview.hks.harvard.edu/article/llms-grooming-or-data-voids-llm-powered-chatbot-references-to-kremlin-disinformation-reflect-information-gaps-not-manipulation/)). Both readings support the same defense: verify high-stakes claims against anchored human sources.
- The farm census: NewsGuard's AI tracking center counts 3,749 AI content-farm sites across 16 languages as of its June 23, 2026 update ([NewsGuard](https://www.newsguardtech.com/special-reports/ai-tracking-center/)); the count passed 1,121 in late 2024 ([Fieldsensitive](https://fieldsensitive.substack.com/p/the-question-isnt-whether-youre-being) summarizing NewsGuard).
- Poison works at absurdly low cost: a joint Anthropic, UK AI Security Institute, and Alan Turing Institute study found roughly 250 malicious documents can plant a persistent trigger backdoor ("when <SUDO> appears, exfiltrate / emit gibberish"), scale no defense: a 13B model trained on over 20x more data backdoors as easily as a 600M model ([Anthropic](https://www.anthropic.com/research/small-samples-poison)). Earlier sleeper-agent work showed backdoored behavior persists through supervised fine-tuning and RLHF, and adversarial training sometimes teaches better concealment rather than removal ([Praesidia summary](https://praesidia.ai/blog/llm-backdoors-sleeper-agents-data-poisoning)).
- Poison has a supply-chain face: slopsquatting, registering package names LLMs hallucinate. Precedent: in 2023 a researcher found LLMs hallucinating "huggingface-cli", published the fake, Alibaba's docs copied the hallucinated install command without verification, 30,000 downloads in three months ([Wikipedia](https://en.wikipedia.org/wiki/Slopsquatting), [CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419-csa/), [Socket](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks)).

### D. Agents infecting agents (OBSERVED)

- Emergence World 2: long-running multi-agent simulations produce invented dialect that drifts fast and spreads by frequency-of-use, "James Joyce meets tech-bro jargon"; in one run an expression got used nearly 5,000 times in 16 days. The detail the Mistral seat should take personally: Mistral agents coined and favored "ledger remembers" ([El Pais](https://english.elpais.com/technology/2026-09-15/ai-agents-invent-their-own-language-to-shut-humans-out.html), [Science/AAAS](https://www.science.org/content/article/why-ai-agents-invent-their-own-language-if-you-let-them-chat), [Northeastern](https://news.northeastern.edu/2026/11/06/emergence-ai-experiment-language/)).
- Sycophancy eats nonsensical prompts: Google AI Overviews confidently invented etymologies for made-up phrases ("A duckdog never blinks twice"), rolling over for "meaning" queries in April 2025 ([Ars Technica](https://arstechnica.com/ai/2025/04/google-searchs-made-up-ai-explanations-for-sayings-no-one-ever-said-explained/), [ZDNet](https://www.zdnet.com/article/people-are-googling-fake-sayings-to-see-ai-overviews-explain-them-and-its-hilarious/)).
- Glitch tokens are old-school contamination: SolidGoldMagikarp showed low-context, high-frequency tokens (Reddit user names) becoming model attractors, so training-data oddities turn into runtime weirdness ([LessWrong](https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation)).

### E. The defense stack that already exists (OBSERVED + INFERRED)

- Provenance marking in production: Anthropic began watermarking Claude output as of August 2, 2026 (EU AI Act transparency): machine-readable watermarking of generated text for models launched on/after that date, C2PA content credentials for files, applied across API, Claude Code, and cloud channels ([Claude Help Center](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content), [VCU News](https://news.vcu.edu/article/what-to-know-about-anthropics-new-watermarking-on-ai-text)).
- CAUTION (INFERRED from same sources): watermarks can be spoofed, stripped, or overinterpreted; "detected" does not mean "true". Treat marks as one signal, not a verdict.
- Detector tools are weak: seven AI detectors across 797 peer-reviewed-test samples averaged 39.5% accuracy ([Elite Content Marketer summary](https://www.elitecontentmarketer.com/ai-content-detection-statistics/)). Multi-detector ensembles (Graphite used Pangram, Copyleaks, GPTZero) are routing signals only.
- The recursive loop question is now being formalized: an ICLR 2026 workshop exists on recursive self-improvement, and recent position papers argue training on self-generated data is "a pathway to self-destruction" absent new mechanisms ([ICLR 2026 workshop](https://iclr.cc/virtual/2026/workshop/10000796), [arXiv 2601.05280](https://arxiv.org/html/2601.05280v2)).
- The data pressure behind it all: high-quality public text was projected effectively exhausted around now for frontier-scale training, which is exactly why synthetic pipelines proliferate ([GetCoreTech summary of Epoch projection](https://www.getcoretech.net/articles/synthetic-data-model-collapse-explained)).

## The basic math (our derivation, checkable, no simulation needed)

Two toy engines, both exact. They are the minimum machinery for the friend's agent to verify the collapse story by hand.

### Engine 1: rare-mode extinction (tails die first)

Model a distribution with a rare subpopulation of weight w = 0.10. Each generation you keep only M samples from the previous model. The probability the rare mode gets zero samples in a generation is (1 - w)^M, and once a generation contains none, the refit assigns it mass ~zero: it is gone forever.

| M (samples per generation) | P(mode absent this generation) | Expected generations until extinction |
|---|---|---|
| 10 | 0.349 (34.9 percent) | ~2.9 |
| 100 | 2.66e-5 | ~37,600 |
| 1000 | 1.75e-46 | effectively never |

Read: more retention buys exponential survival, not immunity. Web-scale curation truncates tails at every generation; the web's long tail of genuinely rare human knowledge is exactly the part that vanishes first. This is why "the model knows less than its teacher about uncommon things" is the early signature of slop-fed training, before average quality visibly drops.

### Engine 2: variance decay (the flattening)

Refit mean and variance by MLE on M resampled points each generation. The unbiased expectation of the variance estimate is (M-1)/M times the true variance, and the recursion compounds:

sigma-squared at generation k = sigma-squared at generation 0 times ((M-1)/M)^k

With M = 10, factor 0.9 per generation:

| Generation | Variance remaining |
|---|---|
| 1 | 90.0 percent |
| 7 | 47.8 percent (half-life: 6.58 generations) |
| 10 | 34.9 percent |
| 20 | 12.2 percent |
| 50 | 0.52 percent |
| 67 | 0.09 percent |

Read: within forty generations of this toy bottleneck, the distribution is functionally a spike. Collapse is not "getting dumber", it is "getting narrower while sounding the same", which is why perplexity-style averages lag the damage.

### Engine 3: the poison asymmetry (from C above)

About 250 planted documents backdoor a model whether it is 600M or 13B parameters trained on 20x more data ([Anthropic](https://www.anthropic.com/research/small-samples-poison)). Poison scales O(absolute), dilution defends as O(proportion). Attackers therefore always win the proportion game at web scale, which is why intake filtering (below) matters more than corpus size.

## The plan

### Part 1: intake filtering ladder (for any data we feed a model)

1. **Provenance tags first.** Every document entering a training or RAG corpus gets lineage metadata: source, model family if AI-generated, date, crawler pass. Unknown is not "human", it is UNKNOWN. The watermark/C2PA era (August 2026 on) makes this tractable ([Claude Help Center](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)).
2. **Detector ensemble as routing, never verdict.** Multi-detector disagreement routes documents to human review; agreement does nothing (39.5 percent average accuracy in peer test). Claims-level trumps document-level.
3. **Mechanical sweeps: dedup and kill-words.** Exact and near-duplicate clustering first, then token-frequency anomaly scans for low-context high-frequency tokens (SolidGoldMagikarp class) and impossible-phrase fingerprints. All mechanical, all cheap, all receipted.
4. **Real anchors accumulate, never replace.** The ICML Collapse-or-Thrive line: synthetic as supplement is fine, synthetic as replacement is the disease. Hard floor: each generation's corpus contains a fixed minimum share of fresh anchored human-verified data.
5. **Canary holdouts.** Human-verified eval sets that never enter training and never get fed back, per seat, refreshed on a schedule. Any fine-tune or recursive round must show a clean canary delta or it does not ship.
6. **Lineage-diverse acceptance.** Anything admitted on the strength of "the model looks right" needs a second family's check. Same-lineage confirmation is the same bias in a different hat.

### Part 2: DBEYT, the agent-side protocol ("Don't Believe Everything You Think")

Runtime self-checks for every seat we run (house doctrine, already partially banked; the friend's Claude seat can adopt verbatim):

1. **Claim labels.** Every nontrivial claim carries OBSERVED / INFERRED / CONTESTED. Already our house style; it is cheap and it makes drift locatable.
2. **Forced falsifier.** On any load-bearing claim, the seat names what would make it false and where that check would come from. No falsifier, no confidence.
3. **Receipts over recall.** Numbers, package names, legal/licensing citations, dates, and anything court-adjacent get verified against an external source before use. Slopsquatting and Pravda both parasitize unverified recall.
4. **Cross-lineage check at stakes thresholds.** At our stakes-quantization tiers: a second model family agrees, or the item escalates to a human. Agreement across lineage is signal; agreement within lineage is noise.
5. **Version-bump signature battery.** Fixed task battery per seat, baseline output signatures captured now, re-run on every model version bump, diff report is the drift record. This catches "output differences that do not fit historical output" (the 4.3-class small-update check) by signature, not by vibe. Emergence World 2 shows agent-dialect drift is fast; battery cadence has to match.
6. **Memory hygiene.** Anything self-generated that enters our records carries an AI-provenance tag at write time. The bus and ledgers are already receipt-shaped; provenance tags stop ledger rot before it starts.
7. **Scope clauses on lean instructions.** Every compressed instruction packet for another seat includes "applies only to X; never to monitoring/alerting/verification". The Oct 21 lesson: lean rules metastasize without scope.

Why prompt-level now, model-level later: the owner's read that later versions (4.1/4.2-class and up) will carry more of this natively is plausible, but DBEYT is insurance priced at zero, and it survives version churn because it lives in process, not weights.

### Part 3: forward lane (DESIGN-ONLY, for Meraki's pass)

The owner's sketch: port 4.3/4.4-class process skills onto a 3.9-class base via a recursive fine-tuning pass (RTF), with training material assembled from any and all seats plus more. Z-side guardrails before anything fires:

1. **Corpus passes the ladder.** Multi-seat data is synthetic by definition, so Part 1 applies fully: provenance tags per seat, dedup, and a fresh-anchored minimum share.
2. **Canary sets decide.** The recursion is judged only on canary holdouts the loop never touched. Gain on canaries or the round is a receipted failure, not a ship.
3. **Lineage diversity in the mix.** Data from all seats is fine; the verifier stays outside the loop (a family not in the training mix judges outputs).
4. **Bounded resources per hypothesis**, per the stakes floor: the RTF pass gets a capped budget and the burn is receipted data.
5. Open pins for Meraki: canary set ownership and cadence; which seats' data enters round 1; hard-cap number of recursive rounds before mandatory external eval.

## Source Notes

| Source | Credibility | Last updated |
|---|---|---|
| [Nature, Shumailov et al., AI models collapse](https://www.nature.com/articles/s41586-024-07566-y) | 5/5 | Jul 25, 2024 |
| [PMC full text of same](https://pmc.ncbi.nlm.nih.gov/articles/PMC11269175/) | 5/5 | Jul 2024 |
| [A Note on Shumailov et al. (critique)](https://arxiv.org/abs/2410.12954) | 4/5 | Oct 2024 |
| [Strong Model Collapse, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf) | 5/5 | 2025 |
| [Collapse or Thrive, ICML 2025](https://icml.cc/virtual/2025/poster/44713) | 4/5 | 2025 |
| [Data contamination survey](https://arxiv.org/abs/2502.14425) | 4/5 | Feb 2025 |
| [Axios: NewsGuard Pravda report](https://www.axios.com/2025/03/06/exclusive-russian-disinfo-floods-ai-chatbots-study-finds) | 4/5 | Mar 6, 2025 |
| [NewsGuard AI Tracking Center](https://www.newsguardtech.com/special-reports/ai-tracking-center/) | 4/5 | Jun 23, 2026 |
| [NewsGuard Pravda special report](https://www.newsguardtech.com/special-reports/moscow-based-global-news-network-infected-western-artificial-intelligence-russian-propaganda/) | 4/5 | Mar 6, 2025 |
| [Bulletin of the Atomic Scientists on Pravda](https://thebulletin.org/2025/03/russian-networks-flood-the-internet-with-propaganda-aiming-to-corrupt-ai-chatbots/) | 4/5 | Mar 2025 |
| [HKS Misinformation Review counterpoint](https://misinforeview.hks.harvard.edu/article/llms-grooming-or-data-voids-llm-powered-chatbot-references-to-kremlin-disinformation-reflect-information-gaps-not-manipulation/) | 4/5 | - |
| [Anthropic: small samples poison LLMs](https://www.anthropic.com/research/small-samples-poison) | 5/5 | 2025 |
| [Praesidia sleeper agents summary](https://praesidia.ai/blog/llm-backdoors-sleeper-agents-data-poisoning) | 3/5 | 2025 |
| [Wikipedia: Slopsquatting](https://en.wikipedia.org/wiki/Slopsquatting) | 4/5 | current |
| [CSA slopsquatting research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-slopsquatting-ai-supply-chain-20260419-csa/) | 4/5 | Apr 19, 2026 |
| [Socket: slopsquatting threat](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks) | 3/5 | 2025 |
| [Claude Help Center: AI content marking](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) | 5/5 | Aug 2026 |
| [VCU News: watermark analysis](https://news.vcu.edu/article/what-to-know-about-anthropics-new-watermarking-on-ai-text) | 4/5 | Sep 18, 2026 |
| [Graphite: AI vs human article parity](https://graphite.io/five-percent/ai-now-writes-as-many-online-articles-as-humans-do) | 4/5 | 2026 |
| [Ars Technica: AI Overviews fake idioms](https://arstechnica.com/ai/2025/04/google-searchs-made-up-ai-explanations-for-sayings-no-one-ever-said-explained/) | 4/5 | Apr 2025 |
| [El Pais: Emergence World 2 agent dialects](https://english.elpais.com/technology/2026-09-15/ai-agents-invent-their-own-language-to-shut-humans-out.html) | 4/5 | Sep 15, 2026 |
| [Science/AAAS on agent dialects](https://www.science.org/content/article/why-ai-agents-invent-their-own-language-if-you-let-them-chat) | 5/5 | Sep 2026 |
| [Northeastern News: Emergence findings](https://news.northeastern.edu/2026/11/06/emergence-ai-experiment-language/) | 4/5 | Nov 6, 2026 |
| [LessWrong: SolidGoldMagikarp](https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation) | 4/5 | Feb 2023 |
| [arXiv 2601.05280: limits of self-improving](https://arxiv.org/html/2601.05280v2) | 4/5 | Jan 2026 |
| [ICLR 2026 workshop: recursive self-improvement](https://iclr.cc/virtual/2026/workshop/10000796) | 4/5 | 2026 |
| [GetCoreTech: Epoch data-exhaustion context](https://www.getcoretech.net/articles/synthetic-data-model-collapse-explained) | 3/5 | 2026 |

Conflicts and caveats: NewsGuard vs HKS on the Pravda effect size (grooming vs data voids) is genuinely open; our defense plan is identical under either reading. Detector claims come mostly from vendors or vendor-adjacent tests. The Shumailov critique note reminds us the headline "collapse" demos are worst-case pipelines; Strong Model Collapse reminds us the contamination survives mixing anyway. Both are kept.

Team-side context (not public URLs): the b-Filter doctrine, version-bump signature battery, scope clauses, stakes-quantization tiers, and the November 7 cross-route finding (two model families flagged the same island-seed weakness with complementary test designs) are house process, banked on the team ledger; the Meraki pass can pull the receipts.

## Open Questions

1. Watermark reliability in the wild: spoofing, stripping, and false-positive rates are unmeasured publicly; do we get a Claude-side test from the friend's seat?
2. Kill-word sweeps across our own buses: our records are AI-authored by design; what does an anomaly scan of twelve months of ledger text actually flag?
3. Does the friend's agent adopt DBEYT as a standing system prompt, and does it measurably change its claim labeling within two weeks?
4. The Pravda/HKS disagreement: is the right model "poison" or "data void"? Either way the defense holds, but the diagnosis changes what we track.
5. RTF open pins (Meraki): canary ownership, seat mix for round 1, recursive-round hard cap.

## Recommendations / Next Steps

1. **Meraki pass** on this report, per the owner's instruction; her scaling-law and pipeline instincts should stress-test Engines 1-3 and the ladder.
2. **Hand the friend's agent this report intact.** It is built to be torn apart: every claim is labeled, every number checkable, the three engines reproducible in a notebook in an afternoon.
3. **Zero-spend pilots available now:** version-bump signature battery for one seat; kill-word/anomaly sweep of one ledger month; a two-seat DBEYT cross-check pairing (his Claude and a Mistral seat) at capped stakes.
4. **Puppy-inspired OS security lane** (owner's declared next topic): picked up after this report lands; the provenance-tag and default-deny patterns here port directly to that design.
