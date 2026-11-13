# FIRED - terra-arrangement-270-pilot-s1p1-repair-route_b - 2026-11-13

Fired by Z (Vibe/Mistral seat). Spec: docs/free-calls/2026-11-13-terra-270-pilot-s1p1-repair-route_b.json (15 free calls, single route B: baidu/ernie-5.5-flash-preview:free; per-call max_tokens 4000).

MECHANICS REPAIR, not a new study arm. The original 30-call pilot (fired/2026-11-13-terra-arrangement-provenance-pilot-30.md, fire commit a9025664, bus 6861550001) timed out at the workflow's 30-min ceiling without publishing receipts: no runs/ commit after 18:20:14Z (last = crystal 21ef48b8), no run dir; call outputs unrecovered. That attempt is recorded as DATA-LOST, not as model responses. The same s1p1 cells (5 provenance arms x 3 repeats, route B) are re-fired here with prompts and IDs VERBATIM from the fired pilot spec (git blob 92f24c4801550182746d50ce16fb0b0be26336ed) under a new batch name. Fresh repeats of the same cells, not recovery of the lost attempt.

Why 15-call single-route batches: 30 sequential calls at cap 4000 exceed the workflow's 30-minute timeout; 15 at cap 4000 fit with margin. Precedent: zsb3 stacked-batch shape. Sibling marker: 2026-11-13-terra-270-pilot-s1p1-repair-route_a.md (fired same session immediately prior, stacked behind it; concurrency group free-calls-bus serializes; checkout-pinned resolution is race-safe).

The 240-call remainder (16 staged specs 2026-11-13-terra-270-<inventory>-route_<a|b>.json, staged this session, no markers) stays STAGED until both repair receipts land clean (Terra's frozen sequence gate); next sweep fires them stacked under the standing owner GO (Terra is GO, bus thread 2026-11-13). Pilot counts toward the 270 per Terra's plan.

Rails unchanged: prompts VERBATIM never edited; no retries; no paid fallback; no model substitution; no system prompt; free-only -- runner live-verifies $0/$0 pricing pre-batch and aborts otherwise. Receipt destination: bus branch runs/ (runner-published); Z posts the mechanics receipt on the bus.
