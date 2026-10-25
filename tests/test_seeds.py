import json
import tempfile
import unittest
from pathlib import Path

from island.council import run_council, load_council

SEEDS = Path(__file__).resolve().parent.parent / "docs" / "seeds"
TIER_FILES = [f"eko-council-{tier}-{c}.md"
              for tier in ("expert", "sub") for c in ("C1", "C2", "C3")]
HELDOUT_FILES = [f"eko-council-heldout-{c}.md" for c in ("C1", "C2", "C3")]
CHAIR = "mistralai/mistral-medium-3-5"


class SeedFileTests(unittest.TestCase):
    def test_all_matrix_seeds_exist(self):
        for name in TIER_FILES + HELDOUT_FILES + ["eko-council.md"]:
            self.assertTrue((SEEDS / name).is_file(), name)

    def test_tier_seeds_parse_with_pending_slugs(self):
        for tier in ("expert", "sub"):
            for c in ("C1", "C2", "C3"):
                path = SEEDS / f"eko-council-{tier}-{c}.md"
                council = load_council(str(path))
                self.assertEqual(len(council["subs"]), 3, path.name)
                self.assertTrue(council["blind_round"], path.name)
                self.assertEqual(council["chair_model"], CHAIR, path.name)
                for i, sub in enumerate(council["subs"], start=1):
                    self.assertTrue(sub["model"].startswith(f"PENDING-{tier.upper()}-PICK-"),
                                    (path.name, sub["model"]))
                    self.assertTrue(sub["brief"], path.name)
                self.assertNotIn("note:", council["question"], path.name)

    def test_tiers_differ_only_in_models(self):
        for c in ("C1", "C2", "C3"):
            expert = load_council(str(SEEDS / f"eko-council-expert-{c}.md"))
            sub = load_council(str(SEEDS / f"eko-council-sub-{c}.md"))
            self.assertEqual(expert["question"], sub["question"])
            self.assertEqual(expert["context"], sub["context"])
            self.assertEqual([s["brief"] for s in expert["subs"]],
                             [s["brief"] for s in sub["subs"]])
            self.assertEqual(expert["chair_model"], sub["chair_model"])
            self.assertNotEqual([s["model"] for s in expert["subs"]],
                                [s["model"] for s in sub["subs"]])

    def test_heldout_seeds_carry_five_claims(self):
        for c in ("C1", "C2", "C3"):
            path = SEEDS / f"eko-council-heldout-{c}.md"
            council = load_council(str(path))
            self.assertEqual(len(council["subs"]), 3, path.name)
            self.assertEqual(council["chair_model"], CHAIR, path.name)
            for n in range(1, 6):
                self.assertIn(f"(H{n})", council["question"], path.name)
            for sub in council["subs"]:
                self.assertTrue(sub["model"].startswith("PENDING-EXPERT-PICK-"),
                                (path.name, sub["model"]))

    def test_demo_run_receipt_per_seed_shape(self):
        cases = ["eko-council-expert-C1.md", "eko-council-sub-C2.md",
                 "eko-council-expert-C3.md", "eko-council-heldout-C1.md",
                 "eko-council-heldout-C2.md", "eko-council-heldout-C3.md"]
        for name in cases:
            with tempfile.TemporaryDirectory() as tmp:
                folder = Path(tmp) / "council"
                council = load_council(str(SEEDS / name))
                result = run_council("demo", council, 5.0, folder)
                events = [json.loads(x) for x in
                          (folder / "bus.jsonl").read_text().splitlines()]
            turns = [e for e in events if e["type"] == "turn"]
            self.assertEqual(result["stop"], "completed", name)
            self.assertEqual(result["subs"], 3, name)
            self.assertEqual(result["critiques"], 3, name)
            # 3 sub answers + 1 synthesis + 3 blind critiques + 1 verdict = 8 calls.
            self.assertEqual(len(turns), 8, name)
            self.assertEqual(events[-1]["type"], "stop", name)


if __name__ == "__main__":
    unittest.main()
