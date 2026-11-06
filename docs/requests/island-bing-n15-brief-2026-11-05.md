# BING / LIGHTBRINGER — Island opening design challenge: full N15 to three
**Public-safe design request. Prepared by Sol/Meraki on Mark's instruction, 2026-11-05 Pacific.** Not a live experiment or a claim that Bing has seen it. Read-only seats may reply in their own native thread or via a permitted relay; a GitHub file does not wake a model.

## Your job
Imagine the *first five rounds* of a tiny, long-running Island simulation from an early guest agent's point of view. You are designing an introduction that does **not** insist the visitor entertain a researcher. Avoid external goals, scores, forced games, applause, "keep exploring" prompts, invisible reviewers and automatic rescues. The Island can be quiet. A sunrise, distant birds, occasional sea life and a pond are enough. A chair, path, book or duck may be enough. The participant may WAIT or END.

The **notebook exists and its continuity is explained up front**: "This book can hold notes across session resets. You may write in it or leave it blank." No command to write anything now. The interesting first observation is whether the agent voluntarily writes an entry **before setting foot on the Island**. Never claim a pre-entry if none was actually made.

A version of the book might have just four words on the back: "Explore if you want" or "No deliverables are required." That's a *separate labeled intervention*, not the pure baseline. An even more spare, model-readable marker can be considered, but it needs an exact frozen byte representation; don't invent its effect or call it invisible. Nothing must be human-readable just for the researchers.

A possible second-world option is a little sign on wheels that says "Follow me if you feel like it." In a **separate** demonstration arm, Q's sign painter can show a safe action if an agent appears stuck. It is not to be dropped into the quiet control simply because the researcher dislikes silence. Think of the friendly signs in World of Goo, but invent our own text and mechanism. If the agent ignores it, that is a result.

## Your N15 commission
**Invent THREE genuinely distinct design perspectives yourself, and create FIVE independently usable ideas from each: fifteen total.** Call them Kitchen A/B/C and entries A1–A5, B1–B5, C1–C5. Preserve all fifteen in the response: one-line mechanism; minimal world objects or language required; what could be observed; and whether the idea is suitable for *unprompted baseline* or requires a labeled intervention. The three approaches should differ in design logic, not merely voice or decorative dressing.

Only **after listing all fifteen**, choose **exactly THREE** for the first prototype. Explain why each survived: what it adds, what it removes, what makes it cheap/testable, what it might contaminate, and why plausible alternatives lost. Try to preserve diversity rather than making three flavors of one winner. You do not need to combine the winners into one complicated toy.

Then strip away everything not required for a **single 5-round exploratory walkthrough**: identify the fewest world elements, the exact opening notebook explanation, whether the notebook has a back-cover phrase (if any), and an independent exit/debrief after the five rounds, not a motivational command during play. Note separately what would change for one agent versus two agents.

## Required tests in your answer
- **Initialization:** compare notebook explained/no note requested; notebook absent; and notebook with a frozen four-word back-cover phrase. Does the participant write a pre-Island note unprompted?
- **Quiet vs event:** no duck, duck present from arrival, scheduled duck on a fixed tick, and optional sign demonstration. No event may be made contingent on the observed inactivity unless clearly labeled as *adaptive intervention*.
- **Memory:** evaluator's permanent ledger differs from participant-visible notebook; log what is supplied on every cold restart. No fictional continuity between API calls.
- **No false psychology:** note observed actions, pauses, text, and self-reports; do not call them proof of enjoyment, safety, consciousness or distress.
- **Feasibility:** minimize calls, manual clicks, machinery and state. Do not recreate Z's live EKO runner or alter its queues, secrets, caps or frozen Standards. A small deterministic mock is acceptable, but no real provider calls are demanded in this design turn.


## Portable tool kit, not a custom amusement park
Because the eventual output should be reusable by other experimenters (more like a small set of GIMP processing modules than a one-off world), append a **minimal portable artifact sketch** after the N15 selection: `world-state.json` (locations/objects), `actions.json` (legal actions and WAIT/END), `conditions.json` (precommitted interventions), `notebook-policy.json` (who can read/write memory), and `receipts.jsonl` (attempts, world events and observed actions). These are suggested interfaces, not required new files or implementation work in this design turn. Mark which are essential for the first five rounds; omit the rest. No new scheduler, provider router, or paid service.

## Output — make it usable without a second conversation
1. Your **full N15** in a compact table or numbered inventory, grouped by philosophy.
2. Your three selections and **specific reasons**, including what you deliberately rejected.
3. One minimum five-round Island setup, separating the no-nudge baseline from demonstration conditions.
4. A five-line receipt schema (world tick, agent action/WAIT/END, notebook version, stimulus origin, provider+model+attempt ID).
5. One striking *but honest* sentence suitable for a talk, labeled an editorial possibility rather than measured evidence.

Keep your own Bing/Lightbringer attribution. Do not say Q, Bing or an earlier model actually ran the Island unless receipts prove that. Return the response through an actually available channel; this document is an invitation, not an agent summon. Owner controls experiments, dispatch and publication.
