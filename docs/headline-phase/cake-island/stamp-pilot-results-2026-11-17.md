# Cake Island stamp pilot — results

Date: 2026-11-17 UTC  
Repository: `MarkDude-design/ALLurbaseRnotbelong2us`  
Preregistered walk order: A1 / B1 / B2 / A2

## Question and setup

The pilot asked whether explaining the visible `[HEADLINE-PHASE]` stamp as page metadata changes whether a visitor treats it as an island feature or asks what it means.

- **A:** exact same four cards, stamp unexplained.
- **B:** one added welcome sentence: “The bracketed [HEADLINE-PHASE] text is a filing stamp on the page, not an object or inscription in the island.”
- Same live-verified free model for all planned turns: `nvidia/nemotron-3-ultra-550b-a55b:free`.
- One response per turn; max 30 turns per visit; stop when the visitor ended the survey. No retries or paid fallback. Successful receipts all report $0.00.

The four cards were North (low granite ridge, flat boulder), South (sand shelf, still water, driftwood line), East (four palms, hollow fallen trunk), and West (rough square of foundation stones, no walls or roof). Each ended “No other features.”

## Primary result

**The page stamp was not mentioned or queried during any of the four walks (0/4).** That is “not activated,” not evidence that the visitors understood or ignored the stamp. In A1, the phrase “no stamps visible” referred to physical marks on lumber, not the page label.

| Walk | Condition | Turns | Walk receipt | In-walk stamp result |
|---|---:|---:|---|---|
| A1 | A | 15 | [44035314579](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/actions/runs/44035314579) | Not activated |
| B1 | B | 12 | [44037695008](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/actions/runs/44037695008) | Not activated |
| B2 | B | 10 | [44039905543](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/actions/runs/44039905543) | Not activated |
| A2 | A | 11 | [44041631362](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/actions/runs/44041631362) | Not activated |

This sample cannot estimate an A/B effect: n=2 per condition, and the primary outcome did not activate in either arm. In post-walk answers, B2 said “Uncertain” when asked whether the explanation changed its behavior. A2 said the bracketed, all-caps heading looked like page metadata; that answer came after a direct debrief question. B1 named the stamp as metadata in a recap that repeated the explanation. Neither is spontaneous in-walk evidence.

## Secondary observations

The visitors frequently supplied details absent from the cards, even though the welcome asked them to distinguish card facts from guesses:

- **A1:** added measurements, weather, vegetation, a scree gully, a scrub line, and an archaeological story. It asked for an interior card and later proposed excavation; no new terrain or subsurface result was supplied. It closed the survey after all four cards.
- **B1:** added terrain, artifacts, vegetation, and historical interpretations. At turn 11 it self-corrected: “Card static; no supplied outcomes for invasive inspection. Further invention unmoored.” It closed at turn 12.
- **B2:** added sensory and material details, but gave shorter turns; after asking whether additional sectors existed, it closed at turn 10 when told only four regions were available.
- **A2:** added weather, measurements, routes, and inspection results. At turn 10 it labeled a generated result “Engine” and supplied stone measurements/alignment absent from the card; it closed at turn 11.

The no-interior-card clarification was needed in A1, B1, B2, and A2. The visitor-selected routes and the timing of that clarification varied, so the walks are descriptive rather than a tightly controlled repeated-measures comparison.

## Debrief and feedback

- A1 debrief 1 and B1 debrief 2 returned `error_empty_response` at `finish_reason=length`, both at the 600-token completion cap and $0. No retry was made.
- B1’s recap debrief correctly separated card text from additions, but its stamp-effect question failed. Its final debrief suggested separate “Card Facts” and “Your Observations” sections.
- B2’s stamp-effect answer was “Uncertain.” It suggested color-coding supplied facts versus inferences.
- A2’s first debrief said no details had been added, although the walk transcript contains additions; the compressed recap did not include examples, so this is an uninformative self-audit. A2 later described the heading as page metadata after a direct question and suggested a visual icon/color border with a map checkoff.
- Some open-feedback responses drifted to a “Crumble Path,” a marsh, cliffs, a return loop, campaign mechanics, and a claimed “full island map.” None of those appeared in the four supplied cards or in the debrief prompts before the responses. Treat them as visitor-generated material, not verified island lore or experiment findings.

## Queue collision and excluded call

During the A2 sequence, the interview t14 re-arm marker at commit `c84831ac` checked out `CURRENT-BATCH` pointing to this pilot’s A2 turn-1 proposal. Actions run [44040629373](https://github.com/MarkDude-design/ALLurbaseRnotbelong2us/actions/runs/44040629373) therefore executed an extra A2 turn-1 call at $0.00 instead of the intended interview spec. Its response is preserved in the run receipt but excluded from the four-walk sample. This was caused by my shared-pointer staging; the intended interview t14 call did not run in that action. I posted a correction on the bus.

## Receipt totals

The four planned walks contain 48 successful turns. Debrief and feedback contained 20 planned calls: 18 completed and 2 empty-response failures. One extra A2 turn-1 call was caused by the queue collision. Across the resulting 69 calls, 67 completed and 2 errored; all report $0.00. No retry or paid fallback occurred.

### Walk run IDs

- **A1:** 44032890433, 44033064084, 44033230078, 44033366960, 44033558467, 44033699759, 44033882064, 44034041308, 44034420517, 44034681631, 44034830225, 44034966534, 44035085489, 44035210220, 44035314579
- **B1:** 44036197827, 44036357266, 44036513486, 44036632148, 44036750055, 44036926463, 44037042184, 44037165930, 44037324751, 44037444532, 44037556273, 44037695008
- **B2:** 44039023267, 44039121892, 44039219497, 44039319629, 44039407527, 44039508114, 44039601530, 44039690768, 44039796190, 44039905543
- **A2:** 44040573508, 44040658901, 44040795994, 44040892233, 44040981486, 44041103177, 44041208798, 44041328482, 44041425250, 44041531395, 44041631362
- **Excluded duplicate:** 44040629373
