# Fire marker: Luna Mistral Small 3.2 route qualification

Owner authorization: Mark, 2026-11-16, explicitly authorized Luna to use dispatch control for paid Island experiments and asked to start at the low end of the budget.

Purpose: qualify OpenRouter route availability for the proposed low-cost continuous-conversation candidate before adding it to the Island runner's known-good model allowlist.

The existing paid-route key probe runs one-token requests for GPT-6 Sol, Mistral Medium 3.5, the candidate mistralai/mistral-small-3.2-24b-instruct, and the Nemotron free control. Expected spend is at most $0.001 across the four calls; actual provider usage/cost must be read from the raw response receipt.

This is a route/auth smoke test only. A 200 response does not establish continuity or Island behavior. Do not add the candidate to docs/models-known-good.txt unless its route and cost are receipted.
