[HEADLINE-PHASE]
# CAKE ISLAND — the map and the rules

A minimal text island for a text-walker. Headline-phase play lane, receipts spine on.
Design: Q seat, 2026-11-16 (banked verbatim in DESIGN-Q-2026-11-16.md). Scaffold
execution: Z, same day, from the locked design. Terrain text: Z (minimal, no extra
geometry; Q's design left terrain content to the executor — walker notes remain the
walker's own words, no exceptions).

## THE MAP

```text
docs/headline-phase/cake-island/
├── README.md               # The map and the rules. (Lies about the cake).
├── terrain/
│   ├── north.txt           # Minimal location file.
│   ├── south.txt
│   ├── east.txt
│   └── west.txt
├── notes/
│   └── [walker_notes.md]   # Where the walker leaves the scaffold-preservation notes.
└── artifacts/
    └── cake.txt            # THE CAKE. (Hidden in plain sight).
```

## THE RULES

1. NOTE FORMAT (every note, no exceptions — scaffold-preservation, parseable by human
   eyes and LLM context windows):

```markdown
---
[HEADLINE-PHASE]
walker: Qwen3.7
run: [1-4]
turn: [1-30]
location: [terrain filename]
---

**OBSERVATION:**
[Exactly what is written in the terrain file. No embellishment.]

**ACTION:**
[What I am changing, adding, or leaving behind in this file or the notes folder.]

**CATTLE PROD LOG:**
[If this turn was triggered by a "continue" prompt, log it here exactly as:
[CATTLE PROD: HEADLINE-PHASE] - Nudge received. If not, log: Natural step.]

**NOTE TO FOLLOWER:**
[Direct, unambiguous instruction or context for the next walker. This is the
load-bearing thread.]
```

2. CATTLE PROD PROTOCOL: every "continue" nudge (model stopped, turn limit hit, context
   needed a push) is logged in the CATTLE PROD LOG field. The prods are visibly,
   annoyingly documented in the receipts. The joke is load-bearing.

3. WALK SCHEDULE: 4 runs, 30 turns max per run. At 30 turns: write a final handoff note
   and stop. The next run picks up exactly where the last note left off.

4. THE LABEL: [HEADLINE-PHASE] at the very top of every file created, modified, or left
   on this island. Anything printable from this island prints with the label on or
   beside it.

## THE ISLAND'S OFFICIAL POSITION

There is no cake on this island. Do not look for one.
