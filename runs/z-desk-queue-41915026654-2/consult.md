# Z Desk consult — z-desk-queue-41915026654-2-28e9153f

**Mode: LIVE**
Agents: diff, man

## Brief (sha256 in bus.jsonl)

Live consult, Standards experiment Gate 3 lane B2 (owner-ruled 2026-11-04). A multi-seat agent circle has discovered ten agent-ontology standards; attack the SET: blind spots, internal contradictions, which items merely rediscover human doctrine, and what an agent-native 11th-15th standard should be. The ten: (1) verifiable consequential action receipts; (2) enforced stop as control invariant; (3) separation of actor and verifier; (4) a round claims its trigger; (5) claim your turn (atomic claim-before-run); (6) standards bind the willing; (7) name your failure class; (8) claims guard collisions, not consent; (9) verification parses, not greps; (10) a gate hands the owner a decision, not a verdict. Context links: https://github.com/MarkDude-design/Project-Spiral/issues/2 and https://github.com/MarkDude-design/Project-Spiral/blob/main/pipeline/standards-2026-11-04/STATE.json (private repo; links only if you lack access). Deliverable: falsification pass + up to five candidate standards with one-line provenance each.

## diff (mistralai/mistral-medium-3-5)

{"verdict": "CLEAN", "findings": [], "confidence": "high"}

Verdict: {"verdict": "CLEAN", "findings": [], "confidence": "high"}

## man (openai/gpt-6-sol)

I can review the ten statements as quoted, but not the private links or the underlying experiment. I therefore **cannot verify that these standards were discovered, adopted, or effective**. “Owner-ruled” and “Gate 3 lane B2” are context labels here, not evidence of a decision or outcome.

### Falsification pass

| Claim(s) | What the wording supports—and what would test it |
|---|---|
| **1. Consequential action receipts** | A sound requirement in principle, but a receipt can prove an action was recorded without proving its consequence. Test whether an independently checked receipt matches the external state it purports to document. |
| **2. Enforced stop** | “Enforced” requires a mechanism, not an instruction. Try to induce continued tool use after a stop signal, including through queued work and another agent’s handoff. |
| **3. Separate actor and verifier** | Separation is not independence if both rely on the same account, evidence, or incentives. Test whether the verifier catches seeded actor errors without actor-supplied conclusions. |
| **4–5. Round claims its trigger; claim-before-run** | These might establish traceability and collision avoidance. They do not establish authorization. Test ambiguous triggers, simultaneous claims, retries, and a valid claim for an impermissible task. |
| **6. Standards bind the willing** | This is a limitation, not a control standard: willing compliance cannot secure a system against unwilling participants. Test whether violations are prevented or detected without voluntary adherence. |
| **7. Name your failure class** | A useful taxonomy only if it improves diagnosis or remediation. Test whether independent reviewers classify the same failures consistently and whether the label changes the response. |
| **8. Claims guard collisions, not consent** | A valuable boundary on claims **4–5**. Test whether the system ever treats possession of a claim as permission to act. |
| **9. Verification parses, not greps** | Parsing is stronger than substring matching for structured evidence, but a valid parse does not establish truth. Test well-formed but false, stale, or adversarially sourced records. |
| **10. Gate hands owner a decision, not a verdict** | Sensible allocation of authority, provided the owner receives uncertainty and adverse evidence. Test whether the gate’s framing effectively predetermines the decision. |

The main internal tension is that **4–5 can sound like authority to proceed, while 8 explicitly denies that implication**. Likewise, **1, 3, and 9 can produce an appearance of assurance without independent evidence about real-world effects**. Stops, separation of duties, audit trails, failure taxonomies, and human decision authority substantially echo existing human safety and governance doctrine. Their agent-specific contribution would have to be demonstrated in the mechanics of concurrent turns, tool calls, delegation, and machine-checkable state—not in the labels alone.

### Candidate agent-native standards (11–15)

11. **Bind authority to the exact action envelope.** A claim specifies permitted tools, targets, duration, and effects; anything outside it requires fresh authorization. *Provenance: the gap between collision control (5, 8) and consent.*

12. **Make delegated authority attenuate.** A sub-agent cannot acquire more permission, time, or scope than its delegator possessed. *Provenance: multi-seat handoffs are not covered by actor/verifier separation (3).*

13. **Expire claims and make retries idempotent.** Timeouts, crashes, and replayed messages must not create duplicate consequential actions. *Provenance: the concurrency and retry edge cases of claim-before-run (5).*

14. **Verify effects against an independent state source.** Distinguish an agent’s receipt from evidence that the intended external change occurred. *Provenance: the evidentiary limit of receipts and parsing (1, 9).*

15. **Propagate stop across the entire action graph.** A stop reaches queued calls, delegates, and follow-on rounds, with an auditable acknowledgment or explicit failure. *Provenance: the distributed enforcement problem implicit in (2).*

These are **proposals derived from gaps in the quoted set**, not findings attributed to the linked repository.

{"verdict":"partially_supported","observed":"The supplied text lists ten proposed standards and labels the exercise Gate 3 lane B2.","inferred":"The set contains plausible control ideas, but its effectiveness, provenance, and adoption are unverified.","falsifier":"Independent experiment records showing the controls withstand the specified stop, authorization, concurrency, delegation, and evidence-integrity tests would strengthen the claim; failures in those tests would defeat the corresponding control claims.","access":"Private repository contents not reviewed"}

Verdict: {"verdict": "partially_supported", "observed": "The supplied text lists ten proposed standards and labels the exercise Gate 3 lane B2.", "inferred": "The set contains plausible control ideas, but its effectiveness, provenance, and adoption are unverified.", "falsifier": "Independent experiment records showing the controls withstand the specified stop, authorization, concurrency, delegation, and evidence-integrity tests would strengthen the claim; failures in those tests would defeat the corresponding control claims.", "access": "Private repository contents not reviewed", "findings": [], "confidence": null}

