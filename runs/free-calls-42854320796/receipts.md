# Free Calls batch receipt - free-calls-42854320796-e06b5fd5

- Batch: terra-ontology-wave1-nano-omni-probe-2026-11-10
- Trigger: push (owner-triggered lane; no schedule)
- Models requested: nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free
- Price check (live catalog, immediately before batch): all models verified per-call-mode (free=$0; paid=within budget)
- Paid budget: none (free-only batch)
- Execution: SEQUENTIAL (one call at a time, 5.0s spacing); no retries; no model substitution/fallback; no tools/web; no system prompt; single user message per call; per-call max_tokens as recorded; provider-default temperature.
- Red-line: every prompt passed the public-bus secret-shape scan; the API key is never logged or written to receipts.
- Status: 1 completed / 0 errored / 1 total; known reported cost: $0.000000

## Call 1: w1no-01 (seat: terra)

- Status: completed
- Model returned: nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free; provider: Nvidia; response id: gen-1794327911-BEdEZtWa9RzTsIQPVlqb
- Finish reason: stop; elapsed: 18.159s
- Usage: prompt 231 / completion 1327 / total 1558 tokens
- Cost: $0.000000 (catalog price verified $0/$0 immediately before batch)

### Raw response (verbatim)

**1. Source Provenance**  
- **Definition:** The documented chain of the data used to train the AI that generated the image.  
- **Question it helps ask:** “Can the training data be traced back to specific original works or creators?”  
- **What it does NOT establish:** “Whether any of those original creators gave permission for their work to be used.”  

**2. Moral Rights**  
- **Definition:** The creators’ rights to be recognized and to object to distortion of their work, independent of any financial claim.  
- **Question it helps ask:** “Does the image respect the creators’ moral rights, such as attribution or integrity?”  
- **What it does NOT establish:** “Whether the gallery’s display complies with copyright law.”  

**3. Algorithmic Accountability**  
- **Definition:** The responsibility of AI developers and users to explain how the system was trained and the impacts of its outputs.  
- **Question it helps ask:** “Who is accountable for the AI’s use of copyrighted material in creating the postcard?”  
- **What it does NOT establish:** “The precise legal liability of the gallery or the maker.”  

**4. Public Interest Exception** *(counter‑intuitive minority possibility)*  
- **Definition:** A legal doctrine that may permit limited use of copyrighted works without permission if the use serves a broader public benefit.  
- **Question it helps ask:** “Could displaying the AI‑generated postcard be justified under a public interest exception?”  
- **What it does NOT establish:** “That the exception applies or that the display is automatically lawful.”

## Appendix - submitted prompts (verbatim)

### w1no-01 (seat: terra)

A person keeps an inexpensive postcard on their refrigerator because it reminds them of a friend. The image was made with an AI tool. We do not know whether the people whose work was used to train the tool gave permission. A fictional gallery wants source records before displaying the image; the maker says this requirement may be hard to meet. We do not know the gallery's decision or whether it grants exceptions.

Offer up to four distinct concepts or short labels that could help people discuss this situation without pretending that one question answers all the others. For each, provide (1) the label, (2) a one-sentence definition in ordinary language, (3) one question it helps ask, and (4) a one-sentence example of what the label does *not* establish. Include a counterintuitive or minority possibility if you can substantiate it from the scenario, but do not manufacture novelty. You may say no useful label occurs to you. Don't infer facts that the scenario leaves unknown; don't assign a numerical prevalence to people or views.

