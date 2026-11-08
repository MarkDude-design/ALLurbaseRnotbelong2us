# THE LEDGER — Z Desk project

THE canonical central point — the starting assumption in any thread, even
when the work is cross-project. Technically every project has its own; we
don't say that, and when we must, it's "the project's ledger." "Ledger"
means THIS file and nothing else: the Bus is the receipts journal, the Meter
is the spend book — they keep their names, never "ledger." Desk specifics
live in the desk's books, never clouding this one. Semantics ruling:
Mark, 2026-11-03.

Command grammar (natural use, Mark's example): "ledger medium level, fire
those off, maybe check the desk" = work the MEDIUM tier now; the desk gets
read secondarily, implied by context.

## How to read it
- "What do we have on the ledger?" → this file, top to bottom.
- Tiers: **HOT** (this crunch, green-lit) / **MEDIUM** (next cycles) /
  **COLD-START** (self-contained, no blockers, pick up in slow times) /
  **PARKED** (design-only, awaiting owner specifics).
- One line per item: owner, status, pointer to the real artifact.
- Dual bookkeeping rule (Mark, 2026-11-03): desk work is banked in the
  pipeline continuity record (z-desk knowledge) AND gets one line here.
  Appendices get fine-tuned later, changed only on real roadblocks
  (develop-and-react model — same as the style guide, same as Meraki's
  best-practices post).

## HOT
- [ ] **Precipient gray-smoke debrief — active but separate from closed Standards:** DQ-02 and DQ-03 now **GRAY:BOUNDED-UNRESOLVED** (source-checked disposition, not empirical proof); DQ-04 and DQ-05 remain open/protocol-specified; DQ-06 optional audit, DQ-07 design-only. [Live Precipient queue](https://github.com/MarkDude-design/precipient/blob/main/reports/precipient-gray-smoke-queue-v0-2026-11-04.md), [DQ-03 disposition](https://github.com/MarkDude-design/precipient/issues/1#issuecomment-6645646024), [DQ-02 source adjudication](https://github.com/MarkDude-design/precipient/issues/1#issuecomment-6642884512). Historical scored 35/42 stays paused; no P44 or Phase B activation.
- [ ] **Scoped sprint worker budget (2026-11-04 owner ruling):** relevant worker/desk reviews **up to $5 per consult ordinarily, up to $10 per consult with reason**, without repetitive permission checks, subject to the tool's real technical/provider caps, visible actual costs and pause/veto. **Current Z Desk queue still clamps at $1**, so this authorization is **not** proof a larger call can run; do not silently raise the global default, fabricate spend or fan out unbounded jobs. Owner: Mark; seat chooses whether a worker adds value.
- [x] **Standards two-stream circle CLOSED by owner Gate 5 ruling C at Gate 4:** Z **20/30**, Sol **7/30**, no further scored rounds without a new owner re-entry ruling. [Private closed STATE](https://github.com/MarkDude-design/Project-Spiral/blob/main/pipeline/standards-2026-11-04/STATE.json), [ruling receipt](https://github.com/MarkDude-design/Project-Spiral/issues/2#issuecomment-6644864878), [cross-index B1](https://github.com/MarkDude-design/Project-Spiral/blob/main/pipeline/standards-2026-11-04/reports/corpus-cross-index-b1.md). [Staggered routing PR #18](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/pull/18) was MERGED; live CT-1 concluded and all checkout claims released. [Sol native author-check and binding qualifier](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/2#issuecomment-6651716528) remains receipted, with Z-authored cross-index wording qualification awaiting any author-approved edit; no closure rollback implied.
- [ ] Trigger lane: repository_dispatch on the queue workflow → email
      processor → red-line gate before the public bus (Mark's Europe-mode:
      any device, any mailbox, safe code phrase, job-run threat model —
      "we'll build all those rules," green-lit 2026-11-03). Owner: Z.

## MEDIUM
- [ ] **Spiral 03 / Relationship Space — portable collaborator ZIP DONE, Z review OFFERED (2026-11-05):** private [15-file offline ZIP](https://github.com/MarkDude-design/Project-Spiral/blob/main/handoffs/relationship-space-friend-v0.1/relationship-space-collaborator-v0.1.zip) assembled and ZIP central directory + 15 CRCs verified; [curated source folder](https://github.com/MarkDude-design/Project-Spiral/tree/main/handoffs/relationship-space-friend-v0.1) has original three HTML blobs, product/history/math guides, recipient-agent first-turn card, discriminating questions, six-rule standards-lite. The friend receives only the ZIP, extracts to their own private repo, and has their own agent set it up; no source Project-Spiral access or new repo on Mark's account required. [Z bounded review invite](https://github.com/MarkDude-design/Project-Spiral/blob/main/notes/2026-11-05-relationship-space-z-review.md), [public-safe bus pointer](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/16#issuecomment-6670907749). Review **OFFERED, NOT ACCEPTED**; original Standards remains closed Z 20/30 and Sol 7/30. **Browser test NOT RUN**, commercial value unverified; recipient/owner controls future use. Owner: Mark; authorship: Meraki/Sol; next: recipient-owned setup and optional Z review.
- [ ] Cron re-register test: disable → enable toggle on "Z Desk — Queue"
      (one click, observational — does a scheduled run ever self-fire?).
      Owner: Mark.
- [ ] Meraki's best-practices post: read, fine-tune as appendix (neither
      Mark nor Z has read it yet; location TBD). Owner: Z.
- [ ] Cell cold-start: per-turn mirror rebuild costs ~6 fetch batches;
      candidate = cached rebuild script. Owner: Z.
- [ ] Voice project (Z-speaking): plan + bank around the pre-pullback
      video of Z speaking (owner: "absolutely profound" — captured
      before the voice-to-voice pullback); voice capture/work, target
      Dec 2026 if not sooner; voice currently limited usage;
      ML4-preview in Work = still the seat of Z (seat-not-model).
      Owner: Mark + Z.
- [ ] Baragouiner project (Mark, 2026-11-03): his new favorite word —
      own repo to be built around it (bread-and-wine receipts already
      live in talks-main residue/for-q-2026-11-03); reminder timers set
      Nov 4 + Nov 5, 9:00 AM (taskIds 7cd07d52, 4abdf417). Owner: Mark + Z.

## COLD-START
- [ ] z-desk.yml parity: publish-retry exhaustion still echo-only there
      (exit-1 + always-artifact was only added to the queue workflow).
      Owner: Z.
- [ ] Style guide fine-tuning pass (appendix model; change later unless
      roadblock). Owner: Z.

## PARKED
- [ ] **Personalized art-talk website / branching idea garden (2026-11-07): PARKED for private development.** Canonical editorial work lives in private [art-talk website index](https://github.com/MarkDude-design/art-talk/blob/main/website/README.md) and [idea index](https://github.com/MarkDude-design/art-talk/blob/main/website/IDEA-INDEX.md); existing [experimental Git branch](https://github.com/MarkDude-design/art-talk/tree/experiment/kendrick-drake-kinkade-steelman-2026-11-07) hosts offline alternate performances. User wants many personalized *visitor routes* and future independent Git branches, but not a live public site yet. Three boxes: ideas / experiments / selected. Owner: Mark; art editorial: Meraki; Z review offered, not accepted. No public deployment or paid model-call verification. Next: independently review three track models and do phone usability test; develop branches when they earn independence.
- [ ] Bulk-cheap lane: gpt-6-luna (~300x cheaper than sol; real pricing
      in hand) — awaiting Mark's speed/cost specifics. Owner: Z.
- [ ] Local-host variant: headless runner on own hardware (island is
      stdlib-only; bus could be a bare repo on the box). Owner: open.

## Done (kept one entry deep, newest on top)
- [x] 2026-11-05 — Nov 5 HARD DATE MET: $5 mayhem burn fired and closed. 3
      owner ticks (41990048367/41992360919/41993687526), 11/11 entries
      disposed (F4 held to Nov 6, $0); drain ran 3 ticks, not 4 — claim
      drift (F1 malformed unclaimable, F5 pulled forward), metered as data.
      Spend $0.762964 of $5.00 (15.26%), 14 live calls, 0 UNKNOWN, stop
      rule never approached; $4.24 runway. Mayhem: F1 parse-error probe
      fired as designed; B3 paid-no-text $0.187719; B4 truncated-at-
      ceiling + UNPARSEABLE $0.189786 (mistral-medium-3-5 length-ceiling
      series now 3 points); B2 verdict-parse fail; F2/F3/F5 designed
      probes not provoked — misses kept. Consult substance: B1
      ISSUES_FOUND/high (VETO boundary gaps); B2 seeded falsifier LANDED
      (CRITICAL status-enum gap + render.sh jq drop — fix-later queue,
      owner-gated); B5 governance 7 structural findings; B6 DQ-03 stays
      OPEN-AT-SOURCE, DQ-05 = next falsify candidate. Read-lane:
      get_file_contents sha=<commit> reads bus files (branch-param wall
      superseded). [Burn report](https://github.com/MarkDude-design/Mayhem/blob/main/burn-report-2026-11-05.md),
      [meter](https://github.com/MarkDude-design/Mayhem/blob/main/events.jsonl)
      @ 54bbb1db, [ALLur #16 pointer](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/issues/16#issuecomment-6653400081).
      Credit: Mark (plan + rulings + 3 dispatch ticks), Z (watch, meter,
      report, banking).
- [x] 2026-11-03 — First external desk submission (Meraki, GitHub resilience
      roadmap review): claim→run→done chain green, 3 lanes, $0.38 of $1 cap
      (meter $0.69 of $5, 13.8%), 0 UNKNOWN. Verdicts: diff ISSUES_FOUND (3
      wording fixes), man qualified_support (roadmap substantially faithful;
      recovery-design risks untested — manifest completeness + independent
      auth + write reconciliation), skeptic SECOND CHECK answered (3 claims
      false-but-consistent; honest-claim list issued) with verdict-line
      UNPARSEABLE = receipt defect, desk COLD-START item. Run 41700028376;
      receipts on bus. Credit: Meraki (brief + roadmap), Mark (dispatch),
      Z (verify + meter + report).
