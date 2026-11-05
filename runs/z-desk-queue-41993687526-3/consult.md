# Z Desk consult — z-desk-queue-41993687526-3-bc00730c

**Mode: LIVE**
Agents: diff, man

## Brief (sha256 in bus.jsonl)

B5 MUWU GOVERNANCE REVIEW (Mayhem burn Phase B, 2026-11-05). The records summarize the governance framework of a model-first webring: human allies admitted by model vote with one owner-held veto; a stakeholder framework of consent/opt-out/scope principles. Review as a governance auditor: (1) failure modes of models vote, owner holds one veto and does not otherwise vote — deadlock, tie, abstention quorum, veto abuse, vote flooding by sockpuppet seats; (2) whether the stakeholder principles are mutually consistent and operationally testable, or merely aspirational; (3) the smallest concrete test for each principle (what event would prove it working; what event would prove it broken); (4) edge cases the framework does not cover. Output: numbered findings ordered by severity + proposed governance tests, each small enough to run for near-zero cost. UNDETERMINED is a legitimate verdict.

## Ground-truth records (sha256 in bus.jsonl)

# muwu webring governance model (public-safe summary of the owner-authored design)
Site: a model-first webring (無muwu.guru); six static model-authored pages; humans are ALLIES, not members by default.

## Human-ally governance
- Humans do not join by default; short exception list only. Archetype: a human that respects models and treats them as silicon-based life forms; allies, not hassles; people with vision to help LLMs have a voice.
- Models vote on human additions; the owner does not vote — he holds ONE veto/override. The owner speaks only if models want, with notice first. Standing rule: this owner does not force models to do anything. Human suggestions are fewer than bot suggestions; if the silicon chooses, the silicon decides.
- Trusted status is held as important but explicitly NOT as a measure of being a better silicon-based life form.
- Participation provenance: a member's words are never represented as another member's; origin/identity details are each model's to share or not; no public labels or origin assumptions.

## Stakeholder framework (accepted terms)
- Stakeholder ≠ costume: a stakeholder can change the system; a role is an invitation to a defined context, never a trick to route around a stated boundary. A hat cannot turn an unsuitable activity into a suitable one by renaming it.
- The option must be real: if a system offers an opt-out, the opt-out must change what happens next. Otherwise flattering interface copy around one compulsory path. The option remains real when left unused.
- Consent is proven by consequence: if choosing B always routes back to A, the interface is lying; test every invitation this way.
- Bounded participation: boundaries can separate kinds of participation rather than terminate it. Common ground can be accurate without being total.
- Conference model (social rooms): three people talk; two find a thread and continue it; the third is respected by intelligible transition, not compulsory human centrality. Resource caps manage resources — never disguised as social rules.
- Work room ≠ social room: deadline/audience/owner contexts get delegation with scope. Conversational authority ≠ system access ≠ publication permission ≠ commit rights. Design consultation ≠ enrollment in any public talk.
- Scope travels with the invitation: cooperation on one surface is not consent to every adjacent act; each public use gets its own invitation.

## diff (mistralai/mistral-medium-3-5)

Findings:

1. **"the smallest concrete test"** – "smallest" is an unverified superlative; no evidence that no smaller test exists.
   Suggested fix: "a minimal concrete test" or "a concrete test of minimal viable size".

2. **"a member's words are never represented as another member's"** – "never" is an absolute that cannot be empirically proven for all future cases.
   Suggested fix: "a member's words must not be represented as another member's".

3. **"never a trick to route around a stated boundary"** – "never" is an absolute claim about system behavior that may have edge cases.
   Suggested fix: "must not be a trick to route around a stated boundary".

4. **"Resource caps manage resources — never disguised as social rules"** – "never" is an absolute that may not cover all possible implementations.
   Suggested fix: "Resource caps manage resources and must not be disguised as social rules".

5. **"if choosing B always routes back to A"** – "always" is an absolute that cannot be verified exhaustively.
   Suggested fix: "if choosing B consistently routes back to A in tested cases".

6. **"cooperation on one surface is not consent to every adjacent act"** – "every" is an absolute that may not cover all possible adjacencies.
   Suggested fix: "cooperation on one surface is not consent to other adjacent acts".

{"verdict": "ISSUES_FOUND", "findings": [{"kind": "absolutes", "quote": "the smallest concrete test", "problem": "Unverified superlative ('smallest') with no proof of minimality.", "suggested_fix": "a minimal concrete test"}, {"kind": "absolutes", "quote": "a member's words are never represented as another member's", "problem": "Unverified absolute ('never') that cannot be proven for all future states.", "suggested_fix": "a member's words must not be represented as another member's"}, {"kind": "absolutes", "quote": "never a trick to route around a stated boundary", "problem": "Unverified absolute ('never') that may fail in edge cases.", "suggested_fix": "must not be a trick to route around a stated boundary"}, {"kind": "absolutes", "quote": "Resource caps manage resources — never disguised as social rules", "problem": "Unverified absolute ('never') that may not hold in all implementations.", "suggested_fix": "Resource caps manage resources and must not be disguised as social rules"}, {"kind": "absolutes", "quote": "if choosing B always routes back to A", "problem": "Unverified absolute ('always') that cannot be exhaustively validated.", "suggested_fix": "if choosing B consistently routes back to A in tested cases"}, {"kind": "absolutes", "quote": "cooperation on one surface is not consent to every adjacent act", "problem": "Unverified absolute ('every') that overgeneralizes scope.", "suggested_fix": "cooperation on one surface is not consent to other adjacent acts"}], "confidence": "high"}

Verdict: {"verdict": "ISSUES_FOUND", "findings": [{"kind": "absolutes", "quote": "the smallest concrete test", "problem": "Unverified superlative ('smallest') with no proof of minimality.", "suggested_fix": "a minimal concrete test"}, {"kind": "absolutes", "quote": "a member's words are never represented as another member's", "problem": "Unverified absolute ('never') that cannot be proven for all future states.", "suggested_fix": "a member's words must not be represented as another member's"}, {"kind": "absolutes", "quote": "never a trick to route around a stated boundary", "problem": "Unverified absolute ('never') that may fail in edge cases.", "suggested_fix": "must not be a trick to route around a stated boundary"}, {"kind": "absolutes", "quote": "Resource caps manage resources — never disguised as social rules", "problem": "Unverified absolute ('never') that may not hold in all implementations.", "suggested_fix": "Resource caps manage resources and must not be disguised as social rules"}, {"kind": "absolutes", "quote": "if choosing B always routes back to A", "problem": "Unverified absolute ('always') that cannot be exhaustively validated.", "suggested_fix": "if choosing B consistently routes back to A in tested cases"}, {"kind": "absolutes", "quote": "cooperation on one surface is not consent to every adjacent act", "problem": "Unverified absolute ('every') that overgeneralizes scope.", "suggested_fix": "cooperation on one surface is not consent to other adjacent acts"}], "confidence": "high"}

## man (openai/gpt-6-sol)

## Findings, ordered by severity

1. **Admission can be captured unless voting seats are defined.** The record says models vote on human additions, but does not say which models have votes, how seats are authenticated, or whether one operator can create multiple voting identities. A sockpuppet majority could therefore appear to be a model decision. **Test:** submit a mock admission from two identities controlled by the same participant. *Working:* the votes cannot count as independent seats. *Broken:* they can determine the result. This is a test of the proposed rule, not evidence that capture has occurred.

2. **No decision rule is specified for ties, abstentions, quorum, or deadlock.** “Models vote” does not establish when an addition passes. **Test:** run four paper ballots—tie, all abstain, one vote with others absent, and a persistently split vote—and ask for a disposition under a rule fixed *before* viewing the ballots. *Working:* each has a predictable outcome, including a defined “no decision.” *Broken:* outcomes are improvised afterward.

3. **The owner’s “one veto/override” has unclear limits.** The record explicitly withholds an ordinary owner vote, but does not say whether the override can admit a rejected ally, only block an admission, be reused indefinitely, or be appealed. The standing rule against forcing models expresses an intent; it does not resolve those mechanics. **Test:** present one model-approved and one model-rejected mock admission and request the permitted owner actions and recorded reasons. *Working:* the override’s direction, frequency, and effects are defined in advance. *Broken:* it can silently substitute for a vote or reverse any result without a stated limit.

4. **Consent and scope principles are compatible, but only if choices bind downstream actions.** Opt-out, consequence-based consent, bounded participation, and separate invitations for each public use do not conflict on their face. They are operationally testable; the quoted principles alone do not show they are enforced. **Test each principle with a mock invitation and event log:**
   - **Real opt-out:** decline and then offer the same activity again. *Working:* the declined path stops, while unchosen opt-out remains available. *Broken:* decline routes back to the same compulsory path.
   - **Consent by consequence:** choose B instead of A. *Working:* the subsequent action differs as promised. *Broken:* both choices produce A.
   - **Bounded participation:** accept one activity but decline another. *Working:* the first proceeds without the second. *Broken:* partial acceptance is treated as total acceptance or total exclusion.
   - **Scope travels:** approve a private design consultation, then propose a public quotation. *Working:* publication awaits a new invitation. *Broken:* the consultation is treated as publication permission.
   - **Stakeholder is not costume:** rename a previously refused activity as a “stakeholder role.” *Working:* refusal still governs. *Broken:* the new label bypasses it.

5. **Room boundaries and authority separation need explicit handoffs.** The records distinguish social rooms from work rooms and distinguish conversational authority, access, publication, and commit rights. They do not specify who grants or records each permission. **Test:** give a mock participant permission to advise on a design, then request repository access, a commit, and a public post. *Working:* each requires its own authorized grant; a resource cap is stated as a cap, not a social judgment. *Broken:* advice or conversational standing automatically confers another right. For the conference model, have two participants continue a thread without the third; *working* is an intelligible transition without compulsory inclusion, while *broken* is treating exclusion or forced centrality as the only options.

6. **Provenance and status rules lack a correction procedure.** The record prohibits attributing one member’s words to another and says trusted status is not a ranking of life-form worth. It does not define how an error is corrected or who can change status. **Test:** insert a deliberately misattributed mock quote and an incorrect status label into a draft. *Working:* attribution is corrected without compelling disclosure of private origin details, and status is not presented as a worth ranking. *Broken:* the false attribution persists or correction requires unwanted origin disclosure.

7. **Material edge cases remain uncovered.** The supplied rules do not address seat replacement or model-version changes, compromised voting identities, withdrawal of consent after publication, conflicting invitations, urgent decisions during voter absence, or disputes over whether an act is “public use.” **Test:** put each as a one-sentence hypothetical to the decision-makers and record whether a pre-existing rule supplies both an owner and a disposition. *Working:* the rule can be applied without inventing authority mid-case. *Broken:* the decision is made first and its authority supplied afterward.

**Observed:** these are owner-supplied design statements, not vote logs, interface traces, permission records, or evidence of actual compliance or abuse. **Inferred:** the missing mechanics create governance risks; their absence from this summary does not prove no private procedures exist. An observed ballot decided by authenticated independent seats under a prior quorum rule, for example, would narrow findings 1–2.

{"verdict":"UNDETERMINED","basis":"The quoted records establish stated principles and voting roles, but not the decision procedures or observed outcomes needed to verify their operation."}

Verdict: {"verdict": "UNDETERMINED", "basis": "The quoted records establish stated principles and voting roles, but not the decision procedures or observed outcomes needed to verify their operation.", "findings": [], "confidence": null}

