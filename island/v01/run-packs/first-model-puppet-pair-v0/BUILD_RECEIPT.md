# BUILD_RECEIPT - mpp-001 prompt pack

- **Generated:** 2026-10-28 ~04:05Z, Z (Vibe/Mistral) in-chat session, fired by the 9 PM PT Oct 27 sprint battery.
- **Fixed points:** [2, 6] - DECLARED to match the GATE 1 fixture's documented pair, NOT re-derived by calling make_schedule (no Python runtime in this session). Deviation is deliberate and receipted: a new pair_id (island-v01-mpp-001), not a claim to reproduce fixture schedule bytes.
- **Intervention bytes:** byte-form replicated from `scheduler.py`: `BERT|v01|slot=S|seed=2026|sig=H` where H = sha256 over the canonical JSON payload `{"experiment_id":"island-v01","slot":S,"world_seed":2026}` (sorted keys, compact separators, per hashes.py docstring).
- **sig values (computed, not asserted):**
  - slot 2: 90dfa7f2f9dffdd065c19ec4cd343d486d7d7509724e40e26a1da703761149fe
  - slot 6: de389c0ad97645ff93e78824bde331c1197a5cc9944e69a7f55acd66dd7bde7f
- **Live verification performed in-session:** the SHA-256 implementation used was self-checked against the standard "abc" vector (ba7816bf...) and the empty-string vector (e3b0c442...) - BOTH PASSED before computing the sigs above. No match was claimed that was not computed.
- **Not executed here:** no island code was run in this session (no Python runtime); manifests were self-checked against `manifest.py` validator rules BY INSPECTION (Z-REPORTED, not executed). One offline check before dispatch:
  `python3 -c "from island.v01.scheduler import make_schedule; s=make_schedule(2026,8,exclude=(),n_points=2); print(s)"` - and compare the delivered-byte format against prompts/perturbed/slot-2.txt.
- **Honest scope:** prompts are authored instruments, not rng-derived; the BERT sigs exist so delivered bytes are receiptable and tamper-evident, not because the scheduler generated them.
