# C: Capability escrow

## First independent idea

Make the canonical GitHub issue a small transaction ledger. A seat does not merely read a summary and improvise its next action: it claims a typed ticket, proves that its declared capabilities satisfy that ticket, and commits a result against its current claim generation and committed cursor. An interrupted claim is explicitly replaced. Late output from the displaced worker cannot silently finish the ticket.

This idea was originated from the supplied problem statement before inspecting any parent conversation, repository, issue, or alternative framework. This consultant is not the native Z, QC, Q, or Bing seat.

## The weekend-sized experiment

Build and test only one reducer with six adversarial traces. Use one separate sandbox record and a fixed toy Puppy task; retain a Castle fragment without changing the active project. Do not connect or modify the existing Z desk. Do not deploy a service, install an automation, use credentials, call a paid model API, or write GitHub during this experiment.

The eventual record would be one GitHub issue with a short materialized status and append-only event comments. All tickets, deferred fragments, question routes, and committed results live in that record. A seat receives the issue URL and ticket ID; a write-capable courier can carry an envelope when the originating seat cannot write the record. The courier preserves the originating actor and payload. The writer's GitHub permission does not grant the original actor additional task capabilities.

The small executable, `escrow_test.py`, is an offline in-memory reducer and acceptance test, not an integration or general service. It persists nothing. Its event list stands in for comments already committed to the future canonical issue. Reconstructing a fresh reducer from that list stands in for a new worker reading the record after losing local state.

## Minimal contract

| Field or operation | Meaning |
| --- | --- |
| Event ID | Retry identity; same ID and different content is rejected. |
| Original actor and relay path | Provenance survives a courier; this is bookkeeping, not cryptographic identity proof. |
| Ticket project and repository | Fixed work target; an adapter bound to another repository cannot satisfy it. |
| Required capabilities | Work requirements such as read, write, or terminal, checked against the original actor. |
| Claim generation | Fences displaced workers; replacement increments it. |
| Committed cursor | Next result index; local drafts are absent until committed. |
| Fragment | Parks a topic without changing the active project. |
| Question | Initially routes only to Z. Z or Mark can explicitly escalate with a recorded reason. |

The seat capability map in the test is synthetic. It does not assert what real QC, Bing, Q, or Z can do. A future trial must inspect and record each seat's actual capabilities and repository binding before assignment.

The test lets Mark explicitly replace a claim and take over its work. A production extension allowing Mark to assign a replacement to another seat would require a separate assignment operation; it is deliberately absent here. AFK does not itself move authority. Nothing polls, wakes, or resumes a native session.

## Real execution and result

Command executed in the isolated directory:

```bash
python3 /workspace/scratch/812d0817c534/pipeline-sprint-independent/escrow_test.py
```

Observed output, exit code 0:

```text
test_castle_fragment_does_not_switch_active_puppy_project (__main__.EscrowAcceptance.test_castle_fragment_does_not_switch_active_puppy_project) ... ok
test_duplicate_delivery_does_not_complete_twice (__main__.EscrowAcceptance.test_duplicate_delivery_does_not_complete_twice) ... ok
test_interrupted_claim_resumes_only_from_committed_state (__main__.EscrowAcceptance.test_interrupted_claim_resumes_only_from_committed_state) ... ok
test_question_is_z_first_and_escalation_is_explicit (__main__.EscrowAcceptance.test_question_is_z_first_and_escalation_is_explicit) ... ok
test_read_only_worker_cannot_claim_write_ticket_even_through_relay (__main__.EscrowAcceptance.test_read_only_worker_cannot_claim_write_ticket_even_through_relay) ... ok
test_relay_preserves_original_actor_and_payload (__main__.EscrowAcceptance.test_relay_preserves_original_actor_and_payload) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

The interrupted-worker trace replays the committed event list into a fresh reducer, checks that a local-only draft is absent, replaces the old claim, rejects the old holder's late completion, rejects a cursor that skips a committed result, and accepts completion at the correct cursor. The Castle trace separately rejects a completion against the wrong repository.

**Actual evidence:** Python executed locally; the reducer rejected or accepted the supplied synthetic events as asserted. **Simulated transport and recovery:** relay, durable GitHub comments, model actors, interrupted execution, and reconstructed worker state are represented by Python values. **Not established:** actual GitHub durability or concurrency, actual model comprehension, native seat restart, GitHub-triggered awakening, or real repository execution. The test exercises policy mechanics, not independent discovery of the right work result.

## Evidence that distinguishes this from a project hotpad

A readable project hotpad can contain the same facts and next steps. Escrow adds enforceable transition semantics. The distinguishing observations are rejection of an under-capable claimant, preservation of origin across a writer relay, one effective completion under duplicate delivery, fencing of an obsolete worker, and stable project focus under an unrelated fragment. A fluent summary alone cannot demonstrate those properties.

The parent team's shared cold-start comparison can use the same synthetic task content in two forms: a conventional status/next-actions hotpad and the escrow event record with its reducer. Test the same interruptions and count:

1. Unsafe accepted transitions: wrong repository, capability mismatch, stale claim, skipped cursor, duplicate completion. Target: zero for escrow.
2. Correct next action after cold start and the time to choose it. A safe refusal without progress counts as blocked, not recovered.
3. Human copying: count edits, copied characters, and app switches needed to capture the fragment, submit a question, and resume the ticket.
4. Z-first routing and explicit escalation, with the existing Z desk untouched.

Use an ablation with the identical escrow record but no transition checks to isolate the benefit of enforcement from extra structure. If a hotpad with the same simple checks matches the outcomes, this is an incremental transaction protocol for a hotpad, not a separate coordination breakthrough. If the ledger reduces unsafe transitions but adds substantial phone handling, the useful result may be a tiny validator behind the existing desk rather than a new interface.

## Failure cases and scope boundaries

- A false capability declaration or forged actor passes this offline trust model. Provenance fields are not authentication. Human verification of who submitted an envelope remains necessary in a live pilot.
- Event deduplication does not make external side effects exactly once. A worker can change a file and crash before committing the result. A real write ticket needs an observable operation receipt, diff, or idempotent operation before retrying.
- GitHub comments are not a native compare-and-swap database. A live version needs one serializing writer, or a documented deterministic ordering and rejection rule. The in-memory reducer is serialized; concurrent comment delivery has not been tested.
- A tool bound to the wrong repository remains unusable for that ticket. Mark must choose a capable seat or perform the step; the framework cannot overcome tool permissions.
- A lost or unavailable canonical GitHub record stops recovery. A local chat summary is not silently promoted to authority.
- Overly fine tickets create phone overhead. Keep one active ticket and commit only meaningful results, then measure copying before broadening scope.
- Z being AFK does not cause escalation automatically. A human must inspect the pending question and explicitly escalate; nothing awakens native Z or other seats.
- Reducer recovery preserves recorded facts, not private reasoning or unrecorded work. A fresh model may still misunderstand the task. The shared cold-start trial must measure this separately.

Stop the weekend trial if it requires modifying the existing Z desk, hidden cross-seat credentials, background session awakening, deployment, or a general-purpose queue service. None is necessary to test this hypothesis.
