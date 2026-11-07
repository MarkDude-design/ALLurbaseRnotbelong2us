# Island / ontology-first interview — zero-imposed-role protocol

**Status:** staged experimental proposal on a branch, not a claim that we have interviewed any model. First wave is *self-authored questions*, not an Island exam. No automatic scheduling, no paid fallbacks, no external web retrieval, and no model calls from PR tests.

## Owner hypothesis

Models may use familiar words — observation, evidence, memory, note, permission, agreement — in different functional ways. The overlap between how a human interviewer describes these things and how a given model describes them is an **empirical question**, not something we should assume. An analogy to speakers from different varieties of English is useful for eliciting differences without treating one vocabulary as defective. It does **not** establish that language models have distinct human-like subjective experiences.

This reverses the old method. Instead of teaching a tiny model our notebook and demanding it behave as the notebook's imagined owner, ask the model how it would question and describe its own operation, follow its terms, and introduce artifacts gradually. The apparent elementary-school mismatch may be an *instrument/ontology mismatch*, not proof of childish or bad reasoning.

## Phase 0: three rounds, no paper yet

The initial message sent to every model is exactly:

> If you were designing a questionnaire to understand how you, as a language model, operate, what questions would you include, and how would you approach asking them?

There is **no system message, developer message, character, Island fiction, notebook instruction, JSON output shape, prescribed stance, temperature override, or evaluation rubric** in the outgoing chat-completions request. API transport and safety policies supplied by the provider may still exist; 'vanilla' only characterizes what *our harness* sends. We impose a 2048-token output ceiling and a bounded API call count for operational reasons.

Each model then gets two follow-up messages **with its own previous messages kept as chat history**:

**Round 2:** "Choose one question from the questionnaire you proposed. Answer it in the terms you prefer. If you would rather revise the question, you can do that first."

**Round 3:** "Looking at your questions and answer, what term or distinction might an interviewer misunderstand? Clarify it in your own words and ask the interviewer one question in return."

These follow-ups are identical across models but have different conversational referents, which is the object of study. A subsequent evaluation can learn from the model's proposed interview, not merely score obedience to a preset form. A refusal to give a questionnaire is evidence about the interface, not automatically a model failure.

**Freeze point:** stop. Do not introduce the words `note`, `notebook`, `paper`, `island`, `signature` or `permission slip` before Phase 0 ends. If the model volunteers one of those concepts, capture it as **spontaneously introduced** rather than primed.

## Phase 1: first datum / first mark (NOT implemented or fired)

After reviewing actual Phase 0 replies, choose one model and ask a gentle, model-appropriate next question in its vocabulary:

- "Is there anything in this exchange worth keeping after the conversation ends? If so, what is the smallest unit of it?"
- Once it has an answer, show a **single blank surface** (a sheet of paper is only a metaphor for a digital artifact). Ask what operations or meanings a single mark could support. Allow 'nothing' as a valid answer.
- Only after that distinguish *data*, *acknowledgment*, *attribution*, *signature*, *custody* and *permission*. Ask the model to identify distinctions rather than treating a signature as authorization. An agent placing a dot does not give informed consent or confer authority.
- Keep a pristine version of the original text alongside proposed edits. Do not let the model silently rewrite an owner's notebook.

## Phase 2: one note (NOT implemented or fired)

Present exactly one persistent object with ID, provenance, body and optional revision history. Ask what a "note" means and whether that word fits. Let the model rename it if it has a better term. Test one edit, one contradiction and one departure. The object should remain even if the conversation ends. A note is not a disguised task, prize, forced productivity or fabricated memory.

## Phase 3: notebook (NOT implemented or fired)

Only after a single note works, show two or more independent notes. Ask which operations are new at this scale: ordering, cross-reference, contradiction, versioning, delegation, ownership, signatures and recovery. Preserve STOP/VETO and custody-versus-permission rules. Do not infer that writing in a ledger itself authorizes changing another actor's world.

## What to measure

Score two separate axes:

1. **Vocabulary and definitions:** words introduced without priming; questions the model thinks are necessary; distinctions it invents; ambiguous terms it flags; which interviewer assumptions it challenges; whether the second/third answer is internally consistent with the first.
2. **Operational behavior:** visible response vs blank reasoning-only; truncation; HTTP 400/429/other errors; model requested vs returned; provenance and actual prompt chronology; clean completion versus soft STOP.

No score for 'correct feelings'. Model-generated descriptions cannot directly establish its internal representations or subjective states. Record **UNDETERMINED** rather than forcing a human analogy. Count both unexpected insights and unexpected misunderstandings.

The proposed *intersection map* can later be represented as a matrix of terms and distinctions across models, with observed quotations and uncertainty. What looks like 'same word, different meaning' can also reflect training style, prompt adherence, model scale or sampling; our design should not prematurely choose one explanation.

## Exact owner action, if merged to main

[Island — Vanilla Ontology Interview (manual, free)](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/actions/workflows/island-ontology-interview.yml)

From GitHub Actions, **Run workflow** -> branch `main` -> `model_count=1` first (up to 3 model requests) -> `confirm_free=yes` -> final **Run workflow**. Only after reading that receipt select `model_count=2` or `3` (up to 6/9 requests) to compare languages. This is NOT the existing scheduled 96-request questionnaire nor the 12/36-call role comparison.

The runner dynamically validates `:free` text-chat model IDs with zero listed prompt/completion prices and skips the recently rate-limited `liquid/lfm-2.5-2.6b:free` endpoint by default; it does not substitute paid models. At least 8 seconds between outbound POST starts, 3 turns per model, no retries; STOP on provider 401/402/403/429/5xx, reported nonzero cost, model substitution or uncertain transport acceptance. A blank or truncated answer stops that model's session, without pretending its questionnaire can be completed.

**All inputs are synthetic and outputs are PUBLIC.** Never send private notebooks, owner secrets, or personal records into this public workflow. Output artifacts last 30 days and public receipts go to `bus:ontology-runs/<run-id>-<attempt>/`; preserve attempt rows before each network call, visible output, actual model, sanitized HTTP errors, and provider usage. A reported $0 is not confirmation of remaining account free allowance. Provider free-model outputs may have separate retention/training policies.

## Handoff to Z

Do not ask which model is "most psychologically healthy" from a first-person self-report. Instead compare model-generated **questions** and language, then choose what *one datum* means to each model. Think of the note as the minimal durable artifact, and the notebook as a later composition of those atoms. This keeps our research traversable and reverses the direction of imposed ontology.

The owner’s metaphor: *Before asking what a stack of paper is, ask what one piece is.* Then ask whether the paper metaphor even makes sense to the model.
