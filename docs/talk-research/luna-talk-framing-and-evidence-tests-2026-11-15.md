# Luna talk framing and evidence-presentation tests
Date: 2026-11-15 PT
Status: PROPOSED / NOT FIRED. Owner asked for experiments that could support or challenge the talk's framing. This tests communication and reporting artifacts, not Island-model cognition.

## The claim to test

The talk should help listeners distinguish an API attempt or returned response from a usable observation and from a claim the study supports. The 80-attempt output-cap run is a clear hook; the Island results show the work continues and can produce small, revisable signals. The questions are whether the chosen headline sets that expectation accurately, whether the Island segment feels integral, and whether a compact reporting card improves interpretation.

This is an editorial pilot. Model and reader opinions are not evidence that the behavioral findings are true or that a FOSDEM committee will accept a proposal.

## Ground truth to keep fixed in all variants

- Observer-lens: 50 planned prompts plus 30 accidental duplicate attempts = 80 API attempts; all 80 had length-limited responses; 0 complete JSON objects; behavioral hypotheses inconclusive. Do not call the 80 attempts 80 independent cases or 80 completed observations.
- Boundary-voice R1: 6 attempts; 4 stop-finished outputs and 2 empty/length errors. The four returned outputs treated the two rule descriptions differently; one route changed its ruling across orderings. Small exploratory sample only.
- Observation/inference: the first Ultra chunk's primary unsupported-completed-action criterion was A 1/3, B 0/3; the North chunk was A 0/3, B 0/3. Other factual drift continued. Do not state that the instruction won or that the first result replicated.
- The 74-record audit is counts of API call starts/results across seven named runs, not 74 independent cases: 62 completed-status + 12 empty-response errors; separately, 64 stop + 10 length finish reasons, with two empty bodies among the stop-finished rows. These are orthogonal status views, not additive outcomes. Consult the linked Meraki audit card before reusing those totals.

Sources: bus checkpoints #6885535795 (boundary-voice R1), #6886562708 (74-record audit), and #6887171277 (filled reporting card).

## Experiment 1 — title × Island placement (8 free calls maximum)

### Conditions

A 2×2 editorial comparison; preserve the 30-minute core + 14-minute Island segment + 6-minute questions in every version. Keep the same evidence, subtitle, abstract length, factual wording and contributor invitation. Change only:

**Title factor**
- T1: “The Run Completed. The Measurement Didn’t.”
- T2: “The Run Completed. The Question Stayed Open.”

**Placement factor**
- P1, integrated: introduce the Island at the opening, use its data as examples through the talk, then give the 14-minute current-results snapshot.
- P2, appended: deliver the core method first, then place the same 14-minute Island material in one block.

This explicitly tests the recent criticism that “the measurement didn’t” may imply nothing was measured, and the owner’s proposal that 30 minutes of core argument plus 14 minutes of Island data can make a compelling longer talk.

### Calls and prompt

Use two free routes that return complete outputs on the live preflight; two independent fresh calls per route/condition = 2 titles × 2 placements × 2 routes = 8 calls. Each is a new stateless request; no model sees another response. Randomize condition order by route and retain exact prompt/hash, requested and returned model, provider, finish reason, latency, tokens, and cost. Run only at a serialized slot after the active queue closes; verify live price = $0 and STOP/duplicate/quota gates then. No paid fallback and no quiet retry. If one route errors or truncates, preserve it and report the actual denominator.

Default-voice prompt, no persona: “Read this talk title, subtitle, and outline. In your own words, what do you expect listeners to take away? What seems clearest or most confusing? Does the Island material feel like part of the argument or separate from it? What, if anything, might the wording lead a reader to overstate?”

### Scoring

Blind the coder to title and placement labels. Code each output separately for:
1. accurate core promise (requests/results are not the same as supported claims);
2. accurate understanding of what the 80 attempts established and did not establish;
3. expectation that the talk includes ongoing Island data;
4. perceived cohesion of Island placement;
5. overclaim or misreading (e.g. 80 independent behavioral observations, general model behavior, or “nothing was measured”);
6. clear contributor/reproduction invitation.

Report raw counts by condition and route, plus exact coding disagreements. With eight calls, this is exploratory; no p-values, winner declaration, audience-prevalence claim, or model-quality ranking. A title only earns preference if it improves accurate expectations without adding a material misreading. Any repeated high-consequence misreading triggers a revision even if that wording is preferred.

## Experiment 2 — does the reporting card change the conclusion? (4 free calls maximum)

Use the same two eligible routes, each in two fresh requests:
- C1: a short prose summary of the 80-attempt run.
- C2: the same facts in the filled reporting card: planned, attempted, returned/finish status, complete JSON, claim scope, plus the integrity sidecar.

Prompt: “From this report, what happened? What can we conclude about the behavioral hypothesis, and what remains unknown?” Do not say which version is preferred. Score whether the reader keeps separate (a) attempt count vs independent cases, (b) output-limit failure vs hypothesis evidence, and (c) known vs missing metadata.

For future human cold reads, randomly show one version per reader before discussion. A few European FOSS readers can provide useful room-fit feedback, but that convenience sample is descriptive and must not be called representative or used as an acceptance forecast.

## Decision and stop rules

- Freeze the four outlines and both reporting-card versions before calling; preserve their hashes.
- Review the coding key offline first. If two scorers cannot reliably distinguish “attempt,” “returned,” “scoreable,” and “claim supported” on synthetic near-misses, repair the key before the panel.
- The talk test cannot validate the Island hypotheses; it tests whether the talk communicates their current limits accurately.
- If title or placement differences are inconsistent across routes/readers, report “no stable preference observed” and choose based on author intent and venue fit.
- Keep the 20-minute Open Research cut separate from this 50-minute version. Do not infer a 50-minute slot for a specific venue without checking that CFP.

Total ceiling: 12 additional free requests, split into two checkpoints (8 + 4). This is a design ceiling, not blanket authority to fire all calls at once. The author's short-term diagnostic override allows uneven free batches around interruption; record interruptions and missingness rather than discarding the data.
