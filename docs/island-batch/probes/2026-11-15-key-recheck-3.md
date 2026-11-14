# Key probe re-check 3 - 2026-11-15 (owner reports key situation fixed)

WHY: re-checks 1 + 2 receipted both paid models 403 (island-baseline key, $10/$10 total
limit). Owner has now fixed the key situation (limit raised on island-baseline OR
fresh key pasted into the OPENROUTER_API_KEY repo secret).

THIS PROBE: same shape - 3 requests, 1 token each through OPENROUTER_API_KEY:
gpt-6-sol (paid A), mistral-medium-3-5 (paid B), nemotron-3-ultra-550b:free (control).
Expected cost <= $0.001. Key value never logged.

DECISION RULE: both paid 200 -> immediately re-fire the parked wave-2b remainder
(w2r5 Luna B / w2r6 Terra r3 / w2r7 Meraki chorus, $3 batch ceiling, staged in
CURRENT-BATCH.json). Any paid 403 -> stays parked.

NOTE: Langfuse (Halo) + HF bucket (MarkDud/island-traces) broadcast destinations are
both live - the first successful call in this probe should land as Halo trace #1 and
the archive's first real trace file (island/{apiKeyName}/{date}/...json).
