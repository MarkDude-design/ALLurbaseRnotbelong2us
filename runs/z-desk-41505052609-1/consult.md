# Z Desk consult — z-desk-41505052609-1-718d4da7

**Mode: LIVE**
Agents: diff, man

## Brief (sha256 in bus.jsonl)

Z STYLE GUIDE v0.1 (excerpt) — review this brief as the consult subject.  THE PRIME RULE — FIDELITY SUPersedes STYLE: banked verbatim is out of style's reach. Owner quotes and seat replies are preserved exactly as relayed — garbles kept (Bryant, Yahoo scout), dictation commas kept, cut-offs kept. Style governs our AUTHORED prose only. A quote is a fossil; the guide dresses the museum, never the fossil.  1. Punctuation - Oxford comma, adopted: red, white, and blue. - COMMA BUMPS: doubled or stray commas from relay/paste artifacts are corrected in authored text at the proof pass. Every push gets a read-back before commit. - Spaced em dash — like this — never a double hyphen. - One space after a period. Straight quotes only in repo files; no smart quotes. - Ellipses live inside verbatim quotes and nowhere else.  2. Capitalization - Seats are proper nouns: Q, Bing, Meraki, Z, Astra, Terra. Sol is Meraki's engine, not a separate seat. - Load-bearing status words ALL-CAPS when they carry ruling weight: FIRED, HELD, POSTED, VERBATIM, UNCONFIRMED, UNDETERMINED, ADOPTED, PENDING, TONIGHT. - Document titles: UPPERCASE-SKELETON-YYYY-MM-DD.md. Section headers: Title Case; one H1 per file, H2 sections.  Check for: absolutes that outrun the evidence, arithmetic that needs re-adding, and any place the guide contradicts itself.

**ERROR** diff: No usable text response; see cost_receipt for known or UNKNOWN charge

## man (openai/gpt-6-sol)

**Verdict: Mostly coherent, with one workflow contradiction and several rules that need narrower wording.**

- **OBSERVED:** The prime rule explicitly exempts banked verbatim material from style edits. That resolves apparent conflicts with the straight-quote, comma, capitalization, and ellipsis rules *when those features occur inside preserved quotes*. A proof pass must not “fix” a relay artifact in a banked quote.
- **OBSERVED:** “Every push gets a read-back before commit” reverses the usual sequence: a commit precedes a push. If the intended control is pre-commit review, say “Every change gets a read-back before commit.”
- **INFERRED, not established:** “Straight quotes only in repo files” may conflict with preserving owner quotes containing smart quotes. The prime rule suggests verbatim wins, but making that exception explicit would prevent an editor from normalizing a fossil.
- **Needs a boundary:** Define when relayed text becomes “banked verbatim,” and whether an owner or seat reply pasted into authored prose remains protected. Otherwise the proof-pass comma rule could be applied inconsistently.
- **Absolutes to test:** “Every push,” “one H1 per file,” and “ellipses ... nowhere else” are broad. A commit/push log and sample files could falsify compliance; a legitimate quoted excerpt containing an ellipsis outside a designated verbatim block would test the last rule’s scope. The excerpt supplies no compliance evidence.
- **Arithmetic:** None to re-add.

{"verdict":"NEEDS_REVISION","supported":"The quoted prime rule establishes precedence for banked verbatim over authored-prose style.","observed_issue":"The read-back instruction says before commit but attaches that requirement to every push.","inferred_risk":"The boundary of banked verbatim and its exception to repo-wide straight-quote rules are not explicit.","arithmetic":"None."}

Verdict: {"verdict": "UNPARSEABLE", "supported": "The quoted prime rule establishes precedence for banked verbatim over authored-prose style.", "observed_issue": "The read-back instruction says before commit but attaches that requirement to every push.", "inferred_risk": "The boundary of banked verbatim and its exception to repo-wide straight-quote rules are not explicit.", "arithmetic": "None.", "findings": [], "confidence": null}

