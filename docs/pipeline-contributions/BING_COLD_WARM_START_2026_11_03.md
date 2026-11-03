# Bing proposal — cold start, warm start and decision memory

Recorded 2026-11-03. **Provenance:** Mark pasted a proposal attributed to Bing in the current conversation. This file is Meraki's attributed summary and design response, not a verbatim archive or a claim that Bing posted it directly. No associated code was supplied or needed for this roadmap note.

## Contribution carried forward

Bing separates two questions:
- **Cold start:** what is this project, what role am I taking, and where does the work stand?
- **Warm start:** what changed since my last verified read?

It suggests four useful views: a short Captain's Desk overview; a Ship's Log of decisions and reasons; an optional Expedition Journal giving causal narrative; and role-specific AI Desk guidance. Its proposed WarmStart view is short-lived while durable project knowledge remains available.

The sample project name, QC restriction, decision numbers, successful fixes, role assignments and profile strengths in the pasted examples are illustrative. They do not establish current team state, tool availability, ownership or empirical findings.

## Meraki's design response

**Adopt the cold/warm distinction as a roadmap axis across A/B/C, not a fourth competing framework.** The hotpad, evidence-first desk and ticket ledger can each have both entry points.

| View | Useful contents | Grounding |
| --- | --- | --- |
| Cold entry | Project, task role, active goal, current blocker, one next action, source links | Latest verified lane records; observed capability and scope |
| Warm entry | Changes after the returning seat's last-read receipt/cursor; unresolved changes requiring attention | Explicit from/to horizons and source receipts |
| Decision record | Decision, recorded reason, supporting evidence, current/superseded status | Original decision receipt; later corrections remain visible |
| Optional journal | Short causal account of what was tried and learned | Links back to decisions and execution evidence |
| Role card | Current responsibility and observed tool capabilities | Dated scope/capability receipts, not reconstructed personality |

The existing receipt-linked ledger already carries some decision rationale. Bing's useful addition is making that purpose explicit and giving returning readers a separate delta view. A ledger preserves reasons that were recorded; it cannot recreate reasons that were never captured.

Warm-start freshness should follow a **read horizon**, not just a day or sprint expiry. A view might say: from comment X through comment Y, these changes occurred, and these two still need attention. Old display notes can be superseded; their underlying decisions, results and unread work must remain recoverable.

A missing cursor, a gap, or an unverifiable base should send the reader to the short cold entry or request a bounded source reconciliation. An expired sticky note alone is not evidence that the reader has seen its contents.

The narrative idea is a worthwhile hypothesis about orientation. This sprint has not measured a preference for narrative, improved model comprehension, preserved native identity, or reduced token/copy cost. Narrative should remain a concise source-linked aid, not a second authority.

## Next bounded test — planned, not run

Extend the bench with a warm-return task, using the same underlying source facts for each framework:
1. Give a returning reader an explicit last-read receipt and a valid base state.
2. Add a resolved blocker, a newly pending action, one unrelated fragment and a duplicate delivery.
3. Ask for only material changes, source anchors and the next action; preserve the active project.
4. Check that the reader includes the pending change, excludes already-seen/duplicate work, does not infer execution, and does not erase the decision rationale.
5. Repeat with missing cursor or a source gap. A bounded cold fallback is the expected result; invented deltas fail.

Measure factual delta coverage and unnecessary rereading separately. Keep old-reader outputs, source horizons, actual read/copy workload where available and honest unknown timing/cost fields.

No warm-start trial has yet been run. The earlier three-reader 10/10 result remains cold-start synthetic feasibility evidence only. No new folders full of profiles, scheduler, worker deployment or Z Desk changes are required to test this distinction.
