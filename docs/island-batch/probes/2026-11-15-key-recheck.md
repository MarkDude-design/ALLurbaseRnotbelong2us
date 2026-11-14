# Key probe re-check - 2026-11-15 (post-key-fix)

WHY: the 2026-11-14 probe (runs/key-probe-20261114T171700Z) receipted both paid models
returning HTTP 403 "Key limit exceeded (total limit). $10.00 of $10.00 used; does not
reset" - the OPENROUTER_API_KEY secret's key had hit its lifetime spend limit. The owner
has since worked the keys (2026-11-15 evening session). This probe receipts whether the
key situation is now clear.

THIS PROBE: same shape as the 2026-11-14 probe - 3 requests of 1 token each through the
OPENROUTER_API_KEY secret: gpt-6-sol, mistral-medium-3-5, plus nemotron-ultra:free as a
working-auth control. Expected cost <= $0.001. Key value is never logged.

DECISION RULE: if both paid models return 200, the parked wave-2b remainder (w2r5 Luna B,
w2r6 Terra r3, w2r7 Meraki chorus - already staged in CURRENT-BATCH.json, $3 ceiling)
re-fires immediately after this probe. If either paid model still 403s, the batch stays
parked and the owner is notified.

NOTE: Langfuse (project Halo) is now wired via OpenRouter broadcast logging - these probe
calls should appear as Halo's first traces if the wiring is live.
