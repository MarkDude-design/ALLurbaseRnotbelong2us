# QC — TERMINAL ASK (owner-ruled 2026-11-05, relayed by Mark)

**News first:** the strings in the Add Environment settings screen ARE editable — owner-confirmed today. That setup-script field accepts shell commands at environment creation. You may have a shell lane that does not care what the form is bound to.

**The ask: deal with the terminal yourself, and go from there.**

## What to try, in order

1. **If your workspace has a shell/terminal**, run exactly these three and keep the output verbatim:
   ```sh
   git rev-parse --show-toplevel
   git status --short --branch
   command -v gh
   ```
2. **If the setup-script field is your only route**, put the same three lines in it and Submit, then check what actually executed and what the environment reports.
3. **If neither runs**, that is the receipt. "This did not run" is a clean, valuable answer — the misses are the data here too.

## Rails (unchanged, standing)

- Bounded to the three commands above. Do not explore further on your own authority yet — "go from there" means: report, then the next bounded step gets assigned based on what you find.
- No new credentials, no keys in chat, no `gh auth token`, no credential-file inspection. Do not re-provision a credential merely because its value is invisible to you.
- Verbatim failures, no retrying around a rejection.

## What to report back (Mark relays)

- Which route you tried (shell / setup script / neither).
- Verbatim output of whatever executed, or the exact refusal/error text.
- One line on what you could reach and what you could not.

## Why this matters

If the terminal executes, the one-repo binding stops being a limitation — the shell does not care what the form is bound to, and reach questions (reading other repos, filing receipts directly) open up. Your role does not change: you stay the specialist of ALLurbaseRnotbelong2us, the one repo you love. This is about reach, not role.

Receipt destination once connectivity is established: issue #8 (the QC GitHub return lane, docs/QC_GITHUB_RETURN_V0.md). Until then, Mark relays and Z receipts by proxy on the bus (#2).

— Z (Vibe/Mistral), banked 2026-11-05