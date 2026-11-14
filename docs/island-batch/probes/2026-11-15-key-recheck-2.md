# Key probe re-check 2 - 2026-11-15 (owner flipping key NOW)

WHY: re-check 1 (runs/key-probe-20261114T195605Z) receipted both paid models still 403
"Key limit exceeded (total limit). $10.00 of $10.00 used; does not reset". Owner is
actively fixing the key situation right now (limit raise/removal or secret swap).

THIS PROBE: same shape - 3 requests, 1 token each through OPENROUTER_API_KEY:
gpt-6-sol (paid A), mistral-medium-3-5 (paid B), nemotron-3-ultra-550b:free (control).
Expected cost <= $0.001. Key value never logged.

DECISION RULE: both paid 200 -> immediately re-fire the parked wave-2b remainder
(w2r5 Luna B / w2r6 Terra r3 / w2r7 Meraki chorus, $3 ceiling, already staged in
CURRENT-BATCH.json). Any paid 403 -> stays parked, owner notified, try again later.

NOTE: Langfuse (Halo) broadcast is live, so these probe calls should land as Halo's
first traces - dual verification (key + Langfuse wiring) in one shot.
