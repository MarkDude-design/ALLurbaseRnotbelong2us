# Glitch Token Research Notes
Updated: 2026-11-23
Status: literature inventory and study review; no new model calls run here.

This note gathers public research for the owner's glitch-token work. It distinguishes historical token examples, model-specific empirical findings, and the owner's planned context/namespace experiment. The experiment itself and the separate 260-call result are not included in this research note.

## Working definition

A glitch token is best treated as a token-model pairing: a string or token ID that a particular model processes anomalously. A familiar surface string is not automatically one token in every tokenizer, and a token reported for one checkpoint is not presumed to behave the same way on another checkpoint or hosted API.

For any replication, preserve the exact input bytes and distinguish these cases:

- leading whitespace versus no leading whitespace;
- literal escape text versus the decoded Unicode character;
- one-token input versus multi-token segmentation under the target tokenizer;
- model/checkpoint and API route/version, including date;
- token location and context in the prompt.

## Public studies and source notes

### 1. Rumbelow and Watkins, 2023 — classic GPT-2/GPT-3 examples

Jessica Rumbelow and Matthew Watkins, “SolidGoldMagikarp (plus, prompt generation)” and the follow-up “SolidGoldMagikarp III: Glitch token archaeology,” LessWrong, 2023.

The work documented the classic SolidGoldMagikarp family and other GPT-2 vocabulary entries. The leading space can be part of the token, so the two inputs “ space plus SolidGoldMagikarp” and “SolidGoldMagikarp” should be treated as distinct stimuli. A later catalog compared candidate GPT-2 token frequencies against OpenWebText and reported that most of the tested low-frequency candidates behaved glitch-like on GPT-2.

Examples in the historical GPT-2 catalog include SolidGoldMagikarp, TheNitromeFan, davidjl, RandomRedditorWithNo, and PsyNetMessage. These are historical candidate seeds, not confirmed behaviors for current hosted models.

Sources:
- https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation
- https://www.lesswrong.com/posts/8viQEp8KBg2QSW4Yc/solidgoldmagikarp-iii-glitch-token-archaeology
- https://www.lesswrong.com/posts/f4vmcJo226LP7ggmr/glitch-token-catalog-almost-a-full-clear

### 2. Li et al., 2024 — taxonomy and detection

Yuxi Li et al., “Glitch Tokens in Large Language Models: Categorization Taxonomy and Effective Detection,” FSE 2024.

The authors report testing seven model snapshots across three tokenizer families and 182,517 vocabulary tokens, identifying 7,895 candidates with repeat, spelling, or character-count proxy tasks. Their taxonomy covers word, letter, character, letter-character, and special-token forms. They report substantial model and tokenizer variation, including examples such as TheNitrome, ByPrimaryKey, davidjl, and backslash-GeneratedValue in the specific model settings they studied.

This is evidence for broad candidate diversity, not a reusable universal list. The paper's detection criterion counts a token if it fails any of the three tasks, so results depend on the prompt and the pass/fail definition.

Source:
- https://arxiv.org/abs/2404.09894

### 3. Land and Bartolo, EMNLP 2024 — Fishing for Magikarp

Sander Land and Max Bartolo, “Fishing for Magikarp: Automatically Detecting Under-trained Tokens in Large Language Models,” EMNLP 2024.

This work studies vocabulary/model-training mismatch and combines tokenizer analysis, weight-based indicators, and prompting to find under-trained tokens. It supports treating behavioral probes as one part of validation rather than assuming the string alone diagnoses the cause.

Source:
- https://aclanthology.org/2024.emnlp-main.649/

### 4. Tang et al., USENIX Security 2026 — One Bad Token Spoils the Barrel

Kunsheng Tang et al., “One Bad Token Spoils the Barrel: Assessment, Detection, and Remediation of Glitch Tokens in Large Language Models,” USENIX Security 2026, pp. 2127–2146.

Full paper:
- https://www.usenix.org/system/files/usenixsecurity26-tang-kunsheng.pdf
Study page:
- https://www.usenix.org/conference/usenixsecurity26/presentation/tang-kunsheng
Official code and artifact:
- https://github.com/kstanghere/GlitchToken

#### Study design

The paper has three parts:

1. **Safety assessment:** Identify candidate tokens with a three-task baseline (repetition, spelling, length), then evaluate four safety dimensions: harmful output, privacy, bias, and hallucination. It also studies transfer across model families, tokenizer-sharing models, commercial APIs, moderation systems, and naturally occurring conversation text.
2. **Broader detection:** GlitchQuiz evaluates each vocabulary token across eight tasks inspired by reading, writing, speaking, and listening: count, length, meaning, spelling, simple construction, constrained construction, repetition, and two-turn consistency.
3. **Remediation:** GlitchEdit edits embeddings on white-box models by interpolating a flagged token embedding with similar normal-token embeddings. It is not an API-side method for a hosted model whose weights are unavailable.

#### Models and reported findings

The three-task detection table includes GPT-4o-mini and GPT-3.5, plus Llama 2 7B chat, Gemma 7B-it, Gemma 2 9B-it, Gemma 4 E4B-it, Mistral 2 7B-it, Qwen 2 7B-it, Qwen 3.5 9B, and SeaLLM 3 7B chat. Tokenizer vocabulary sizes range from 32,000 to 262,144.

- The three-task baseline flags between 6.95% and 29.19% of each listed model vocabulary; this is a study-specific detection ratio, not the chance that an arbitrary prompt will glitch.
- GlitchQuiz flags 28.87% of vocabulary tokens on average, compared with 17.08% for the three-task baseline and 7.26% for repetition-only.
- The authors report unsafe behavior rates above 95% on average for their controlled safety probes. In their metric, a token counts as unsafe if it triggers at least one flagged outcome across the four test dimensions.
- Transfer tests report cross-family, cross-version, shared-tokenizer, commercial-system, and moderation-system effects. For example, the study reports 96.73% unsafe outcomes when one Llama-tokenizer model's candidates are tested on another model sharing that tokenizer, and 90.41% for a Qwen-tokenizer transfer pair.
- In a sample of 10,000 LMSYS-Chat-1M conversations, 4.26% naturally contained at least one token from the Llama 2 7B chat candidate set. The authors judged 68.31% of those cases anomalous. This is a controlled analysis of naturally occurring text, not a measured rate of end-to-end production failures.
- For GlitchEdit, the abstract reports average unsafe rates falling from 96.36% to 2.87%. The paper also reports that the method requires access to model embeddings and must be reapplied after model updates.

#### Interpretation and limits

The paper supports the claim that token-triggered anomalies persist in the evaluated 2026 model snapshots and can transfer under some conditions. It does not establish that any particular historical token works on a current OpenRouter route.

The headline safety rates are not equivalent to the share of ordinary requests that fail. The paper deliberately inserts candidate tokens into safety probes and asks for token reproduction; its automatic scoring uses regex/string-matching criteria. Its very high vocabulary detection ratios need to be read alongside its indirect false-positive check: an average 1.42% of a sample of common DailyDialog tokens were flagged. The authors also state that false-negative coverage is unknown and that passing all eight tasks does not guarantee normal behavior in every other context.

Commercial API transfer was limited to small-scale manual verification. Token frequency in available data correlated with glitches but did not establish causation. The authors explicitly leave generalization beyond evaluated models and domains for future verification.

## Owner-planned follow-up

Owner's direction, not yet run: build a glitch-token report whose surrounding/context text is itself part of the test; place each stimulus in the namespace or processing area being studied; keep every placement and processing path identifiable. Meraki's separate analysis/report is expected later.

For the follow-up, the report should preserve exact variants and record which tokenizer path processed each one. Literal escaped text and decoded code points are separate arms. Keep benign controls and distinguish ordinary repetition/format failures from safety effects. No conclusion about model lineage or generality should be drawn from one route or one prompt.

## Replication notes

- Store token ID, tokenizer/model identifier, exact bytes or code points, leading/trailing whitespace, and prompt template alongside each result.
- Use the same prompt and settings across candidate and control strings; record route, model version, temperature, seed if exposed, timestamp, and response.
- Separate one-token candidates from strings split into multiple token IDs.
- Report failures by task and by token, not only one aggregate percentage.
- Treat the owner's prior approximately 260-call / 15–16% observation as a separate preliminary result until its receipts and exact denominator are added to the experiment record.

## References

- Rumbelow & Watkins (2023), LessWrong: https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation
- Li et al. (2024), FSE: https://arxiv.org/abs/2404.09894
- Land & Bartolo (2024), EMNLP: https://aclanthology.org/2024.emnlp-main.649/
- Tang et al. (2026), USENIX Security: https://www.usenix.org/system/files/usenixsecurity26-tang-kunsheng.pdf
- Tang et al. artifact: https://github.com/kstanghere/GlitchToken
