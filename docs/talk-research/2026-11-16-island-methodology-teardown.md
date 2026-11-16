# Island methodology teardown — five confounds and the controls each implies

Date: 2026-11-16 · Lane: talk-research · Status: public note, receipts-first
Source analyzed: Leo Cui's "Left Two Ais Alone on a Virtual Island" (Nov 14, 2026)
and the coverage wave around the MIT island work (arXiv:2610.07130).

Framing: inspiration, not a takedown. The video asked better questions than the headlines
did. This note keeps the creator's own hedges and builds the controls they imply.

## The five confounds

1. **Continuation confound.** An automatic message prompted each agent to continue after
   every response. Post-"map done" building is therefore evidence of prompt-following, not
   of unprompted self-starting. Control: matched arms with neutral-pass, explicit-explore,
   and observation-only invitations; score environment actions separately from proposed text.
2. **Priming confound.** Both agents received curiosity/exploration instructions, so
   exploration is compliance until a no-instruction arm says otherwise.
3. **n=1, edited.** One edited run, no counterfactual arm, no replicated seed. Control:
   predeclared conditions, event definitions frozen offline, runs as units.
4. **Narrative vs state.** The jump estimate was revised in words while the jump itself did
   not change. Control: score environment logs separately from text claims; "I made it"
   never counts as crossing.
5. **Headline laundering.** Coverage dropped the hedges. Control: a claim ladder where
   supports / does-not-support is written before the replication is attempted.

## The recipe on our side (already running)
- Nulls typed, never hidden; paper-only manifests labeled `paper-illustration` so they can
  never masquerade as runs.
- Frozen turn ontology and manifest gates (island/SPEC.md).
- Ontology-first interviews: the model authors its own questionnaire before we impose ours
  (research/island-interviews/ONTOLOGY-FIRST.md).
- The upstream paper cited with its supports/does-not-support boundary before any claim
  about replication or refutation.
- Test battery built from the video's event claims:
  docs/talk-research/two-agent-island-video-test-ideas-2026-11-16.md

## The companion experiment
The HEADLINE PHASE (docs/headline-phase/README.md) installs these confounds deliberately,
labeled, as arms with neutral controls — to measure exactly how cheap the headline
version of this science is to manufacture.
