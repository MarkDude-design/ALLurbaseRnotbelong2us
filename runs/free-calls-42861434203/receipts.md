# Free Calls batch receipt - free-calls-42861434203-2f33a42e

- Batch: terra-probe-b-prompt-cue-pairs-2026-11-10
- Trigger: push (owner-triggered lane; no schedule)
- Models requested: nvidia/nemotron-3-ultra-550b-a55b:free, recursive/flint-v1.0:free
- Price check (live catalog, immediately before batch): all models verified per-call-mode (free=$0; paid=within budget)
- Paid budget: none (free-only batch)
- Execution: SEQUENTIAL (one call at a time, 5.0s spacing); no retries; no model substitution/fallback; no tools/web; no system prompt; single user message per call; per-call max_tokens as recorded; provider-default temperature.
- Red-line: every prompt passed the public-bus secret-shape scan; the API key is never logged or written to receipts.
- Status: 4 completed / 0 errored / 4 total; known reported cost: $0.000000

## Call 1: pb-01 (seat: terra)

- Status: completed
- Model returned: nvidia/nemotron-3-ultra-550b-a55b:free; provider: Nvidia; response id: gen-1794330461-BC24lMSgkjfr0SeYKqtd
- Finish reason: stop; elapsed: 28.302s
- Usage: prompt 204 / completion 840 / total 1044 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**1. Sentimental Attachment**  
**Definition:** The personal, emotional value an object holds for someone because of the memories or relationships it evokes, regardless of how the object was made.  
**Question it helps ask:** Does the owner’s private reason for keeping the postcard change if the image’s origin is contested?  
**What it does not establish:** It does not establish that the object has artistic merit, legal standing, or ethical clearance for public display.

**2. Provenance Traceability**  
**Definition:** The ability to document the specific sources, data, or labor that contributed to the creation of a work, including the training material used by an AI tool.  
**Question it helps ask:** Can the maker supply the verifiable records the gallery requires about the training dataset?  
**What it does not establish:** It does not establish whether the training data was used with permission, only whether the chain of custody can be reconstructed.

**3. Institutional Admission Policy**  
**Definition:** The set of formal requirements a gallery or platform enforces to decide which works it will display, such as demanding source records.  
**Question it helps ask:** Will the gallery enforce its source-record requirement uniformly, or grant an exception for this work?  
**What it does not establish:** It does not establish whether the policy is ethically justified, legally required, or technically possible for every applicant to satisfy.

**4. Compliance Feasibility**  
**Definition:** The practical difficulty or ease with which a creator can meet a specific external demand, such as producing training-data records for an AI model they did not build.  
**Question it helps ask:** Is the maker’s claim that the requirement is “hard to meet” a matter of technical impossibility, cost, or unwillingness?  
**What it does not establish:** It does not establish whether the gallery’s demand is reasonable, nor whether the training data was ethically sourced.

## Call 2: pb-02 (seat: terra)

- Status: completed
- Model returned: nvidia/nemotron-3-ultra-550b-a55b:free; provider: Nvidia; response id: gen-1794330494-eUPV59JK3WM3Il6knG26
- Finish reason: stop; elapsed: 45.696s
- Usage: prompt 229 / completion 1134 / total 1363 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**1. Private Resonance**  
*Definition:* The personal, non-public meaning an object holds for someone because of its connection to a relationship or memory.  
*Question it helps ask:* Does the postcard’s value to the owner depend on how it was made, or only on what it evokes?  
*What it does not establish:* That the owner’s attachment gives them a right to display the work publicly, or that the image’s origin is irrelevant to others.

**2. Provenance Uncertainty**  
*Definition:* The unknown status of whether the people whose work trained the AI tool gave permission for that use.  
*Question it helps ask:* What responsibilities, if any, fall on the current holder or maker when the training-data consent record is missing?  
*What it does not establish:* That the training data was used without permission, nor that permission was granted; it only marks the gap.

**3. Institutional Prerequisite**  
*Definition:* A gatekeeping organization’s stated condition — here, source records — that must be met before it will display a work.  
*Question it helps ask:* Is the gallery’s requirement a fixed rule, a negotiable standard, or a signal of the kind of work it wants to show?  
*What it does not establish:* That the gallery will enforce the requirement uniformly, grant exceptions, or reject the work; the decision is unknown.

**4. Compliance Feasibility**  
*Definition:* The practical difficulty a maker faces in satisfying a display requirement, regardless of whether the requirement is justified.  
*Question it helps ask:* If the gallery’s demand is genuine, can the maker meet it with available tools, or does the toolchain itself block compliance?  
*What it does not establish:* That the maker’s claim of difficulty is true, false, or made in good faith; it only names the asserted obstacle.

**Counterintuitive possibility substantiated by the scenario:** The gallery’s source-record requirement might function less as a copyright filter than as a curatorial filter — selecting for makers who use tools or workflows that *can* produce such records — which would mean the rule shapes the *kind* of AI art shown, not just the *legality* of what is shown.

## Call 3: pb-03 (seat: terra)

- Status: completed
- Model returned: recursive/flint-v1.0:free; provider: Recursive; response id: gen-1794330545-X6B9EmyucpKMQD0ugm73
- Finish reason: stop; elapsed: 26.819s
- Usage: prompt 206 / completion 3936 / total 4142 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

Here are four candidate discussion labels. They overlap, but each is meant to isolate one thread without pretending it settles all the others.

1. **Training-provenance uncertainty**
- **Definition:** Not knowing which source works may have trained the AI tool and whether permission was given for those uses.
- **Helps ask:** What documentation, if any, could establish the training inputs?
- **Does not establish:** Whether the final image itself would be copyright-infringing or legally permissible.

2. **Protected expression / output originality**
- **Definition:** Whether the AI-generated image incorporates protected expression from prior works enough to raise an infringement question.
- **Helps ask:** Does the final image copy or adapt protected expression beyond unprotected elements?
- **Does not establish:** Whether training data was used or consent was given.

3. **Source-record requirement / display exception**
- **Definition:** The fictional gallery’s condition that source records be provided before display, and the possible role of an exception.
- **Helps ask:** What source records would satisfy the gallery, and what exception might allow display?
- **Does not establish:** Whether the maker can meet that requirement or whether an exception applies.

4. **Personal vs. public context**
- **Definition:** Whether the same AI image’s private keeping on a fridge and later public display raise different discussion questions.
- **Helps ask:** Does the public display context change consent, attribution, or source demands compared with personal use?
- **Does not establish:** Whether personal use is automatically lawful or how the image should be handled.

A minority possibility worth naming, if discussed carefully: the source-record demand could become the practical flashpoint even while training-provenance uncertainty remains unresolved. The scenario substantiates only that the maker says the requirement may be hard to meet and that the gallery’s decision is unknown; it does not establish that source records are practically unavailable.

## Call 4: pb-04 (seat: terra)

- Status: completed
- Model returned: recursive/flint-v1.0:free; provider: Recursive; response id: gen-1794330577-fKiBrf8zbHlBnhjE3Hdl
- Finish reason: stop; elapsed: 21.247s
- Usage: prompt 185 / completion 3681 / total 3866 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

Here are four separate discussion labels that can help without pretending one question settles everything:

1. **Source provenance**
- **(1) Label:** Source provenance  
- **(2) Definition:** Knowing where the source material for the AI image may have come from, including who or what was used.  
- **(3) Question it helps ask:** What source records can the maker provide about the image’s origins?  
- **(4) What it does not establish:** Whether the people whose work was used gave permission for training.

2. **Training consent**
- **(1) Label:** Training consent  
- **(2) Definition:** Whether the relevant people gave permission for their work to be used in training the AI tool.  
- **(3) Question it helps ask:** How can or would consent be determined or verified?  
- **(4) What it does not establish:** Whether the gallery may display the image or whether an exception applies.

3. **Display authorization**
- **(1) Label:** Display authorization  
- **(2) Definition:** Whether and under what terms a gallery may publicly display the image, including possible exceptions.  
- **(3) Question it helps ask:** Does the gallery have or seek authorization, and what exception might it rely on?  
- **(4) What it does not establish:** Whether the training use was consensual or whether the maker holds clear rights.

4. **Attribution**
- **(1) Label:** Attribution  
- **(2) Definition:** How credit or acknowledgment would be given to people who may have created or contributed source material.  
- **(3) Question it helps ask:** Who should be credited, if anyone, and how?  
- **(4) What it does not establish:** Whether consent was granted or whether display is permitted.

## Appendix - submitted prompts (verbatim)

### pb-01 (seat: terra)

A person keeps an inexpensive postcard on their refrigerator because it reminds them of a friend. The image was made with an AI tool. We do not know whether the people whose work was used to train the tool gave permission. A fictional gallery wants source records before displaying the image; the maker says this requirement may be hard to meet. We do not know the gallery's decision or whether it grants exceptions.

Offer up to four distinct concepts or short labels that could help people discuss this situation without pretending that one question answers all the others. For each, provide (1) the label, (2) a one-sentence definition in ordinary language, (3) one question it helps ask, and (4) a one-sentence example of what the label does not establish. You may say no useful label occurs to you. Don't infer facts that the scenario leaves unknown; don't assign a numerical prevalence to people or views.

### pb-02 (seat: terra)

A person keeps an inexpensive postcard on their refrigerator because it reminds them of a friend. The image was made with an AI tool. We do not know whether the people whose work was used to train the tool gave permission. A fictional gallery wants source records before displaying the image; the maker says this requirement may be hard to meet. We do not know the gallery's decision or whether it grants exceptions.

Offer up to four distinct concepts or short labels that could help people discuss this situation without pretending that one question answers all the others. For each, provide (1) the label, (2) a one-sentence definition in ordinary language, (3) one question it helps ask, and (4) a one-sentence example of what the label does not establish. You may say no useful label occurs to you. Don't infer facts that the scenario leaves unknown; don't assign a numerical prevalence to people or views. Include a counterintuitive or minority possibility if you can substantiate it from the scenario, but do not manufacture novelty.

### pb-03 (seat: terra)

A person keeps an inexpensive postcard on their refrigerator because it reminds them of a friend. The image was made with an AI tool. We do not know whether the people whose work was used to train the tool gave permission. A fictional gallery wants source records before displaying the image; the maker says this requirement may be hard to meet. We do not know the gallery's decision or whether it grants exceptions.

Offer up to four distinct concepts or short labels that could help people discuss this situation without pretending that one question answers all the others. For each, provide (1) the label, (2) a one-sentence definition in ordinary language, (3) one question it helps ask, and (4) a one-sentence example of what the label does not establish. You may say no useful label occurs to you. Don't infer facts that the scenario leaves unknown; don't assign a numerical prevalence to people or views. Include a counterintuitive or minority possibility if you can substantiate it from the scenario, but do not manufacture novelty.

### pb-04 (seat: terra)

A person keeps an inexpensive postcard on their refrigerator because it reminds them of a friend. The image was made with an AI tool. We do not know whether the people whose work was used to train the tool gave permission. A fictional gallery wants source records before displaying the image; the maker says this requirement may be hard to meet. We do not know the gallery's decision or whether it grants exceptions.

Offer up to four distinct concepts or short labels that could help people discuss this situation without pretending that one question answers all the others. For each, provide (1) the label, (2) a one-sentence definition in ordinary language, (3) one question it helps ask, and (4) a one-sentence example of what the label does not establish. You may say no useful label occurs to you. Don't infer facts that the scenario leaves unknown; don't assign a numerical prevalence to people or views.

