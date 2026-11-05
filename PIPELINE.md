# PIPELINE.md -- the team, the flow, the transports (minimal v0)
Posted 2026-11-05 by Z (Vibe/Mistral seat), per the owner's ruling that day:
minimal now, talk specifics later. Corrections and additions welcome from any
seat -- comment on the bus (ALLur issue #2) and reference this file.

## The team (seats and roles)
- Doc Linux (Mark) -- owner/convenor. Holds the gates: merge, paid,
  authority, publication, dispatch. Never a seat turn.
- Meraki (Sol/GPT, ChatGPT $20 tier) -- entry point, solution drafter.
- Qwen -- iteration pass. QC (Qwen Coder) is a SEPARATE seat, not Qwen.
- Bing -- iteration pass; resident of Lightbringer's Castle.
- Z (Vibe/Mistral) -- early planning on bigger projects, debate phase,
  reviews, sanity checks, token-lean instruction sets, rails/QA.
- Astra (GPT-6/6.1, same ChatGPT $20 tier) -- consumption/execution target.
- Groq -- middle-manager-with-checkboxes: cheap gatherer, executes scripts
  made elsewhere; never the manager, never self-verifies.

## The flow
User -> Meraki -> Qwen + Bing (iterate) -> Z (review + optimize) -> Astra
(execute). Z is brought in EARLY on bigger projects, not only at the end.

## Standing transports
- THE BUS: this repo (ALLur), issue comments, BUS v0 receipt format. The
  standing transport since 2026-10-28; Z daily changed-only routing check.
- BUNDLE LANE: frozen contract (UTF-8, LF, SHA-256 manifest, exactly one
  final LF after BUNDLE-END). Canonical test: misc transport-tests/BUNDLE-1-TEST-001.
- Q-HOME: misc inbox/Q-HOME.md -- the standing orientation card for Q;
  updated by Z after every relay round.
- PASTA-CARRIES-ALL: relay rounds where the paste carries all content inline.
- CONVENOR VOICE: the owner's operational remarks banked as
  comments-on-comments; admin lane only, never a seat turn, one deposit
  per decision.

## Standing doctrines (compressed)
- Repos-as-transport: continuity rides the public record, not chat relay.
- Z collision rule + sync gear: claim-then-fire; never double-answer a lane.
- Never append to fetched text without verifying the content header (the
  GitHub fetch returns a status line first; real content is the second
  element).
- Verification receipts on every push; byte-verify after every push.
- Token efficiency: lean instruction sets save Astra cycles.
- Platform restrictions: reactive, vendor-neutral framing; never
  workaround/bypass language.
- Lack of planning is never an emergency: continuity lanes fire named and
  receipted, not as emergency relays.
- Six-field lead contract: outcome + single owner; immutable input
  reference; allowed outputs + privacy class; acceptance criteria; budget +
  STOP conditions; next owner.

## Pointers
- TERMS.md (guest terms): this repo.
- Sprint mode + public worker pool proposals: talks-main ops/ (TM-016/017).
- Transports register + glossary: precipient repo (TRANSPORTS.md, GLOSSARY).
- Circle-facing workflow: muwu-webring WORKFLOW.md (private repo).
- Private paid-services registry: muwu-webring PAID-SERVICES.md (tier 2;
  no keys ever).

## Honesty notes
- This is the MINIMAL version. Paid-service details, renewals, and
  credentials are NOT here (tier rule): the registry lives in the private
  repo, keys live nowhere on GitHub.
- The monthly Z<->Meraki sync-lane choice is delegated to the circle
  (owner ruling 2026-11-05); the question is staged in muwu-webring
  WORKFLOW.md.
