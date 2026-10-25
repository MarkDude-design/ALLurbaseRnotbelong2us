import json
import os
import tempfile
import unittest
from pathlib import Path

from island.council import run_council, load_council

SEEDS = Path(__file__).resolve().parent.parent / "docs" / "seeds"
TIER_FILES = [f"eko-council-{tier}-{c}.md"
              for tier in ("expert", "sub") for c in ("C1", "C2", "C3")]
HELDOUT_FILES = [f"eko-council-heldout-{c}.md" for c in ("C1", "C2", "C3")]
CHAIR = "mistralai/mistral-medium-3-5"
# Mark's approved slate (2026-10-25), filled in the one receipted seed edit
# before FIRST dispatch. One lab per sub; alternates on record in z-room.md.
EXPERT_SLATE = ["anthropic/claude-opus-5.5",
                "openai/gpt-6.1-sol",
                "google/gemini-3.1-pro-preview"]
SUB_SLATE = ["openai/gpt-6-luna",
             "deepseek/deepseek-v4.1-flash",
             "z-ai/glm-5.3-flash"]


class SeedFileTests(unittest.TestCase):
    def test_all_matrix_seeds_exist(self):
        for name in TIER_FILES + HELDOUT_FILES + ["eko-council.md"]:
            self.assertTrue((SEEDS / name).is_file(), name)

    def test_tier_seeds_carry_the_picked_slate(self):
        for tier, slate in (("expert", EXPERT_SLATE), ("sub", SUB_SLATE)):
            for c in ("C1", "C2", "C3"):
                path = SEEDS / f"eko-council-{tier}-{c}.md"
                council = load_council(str(path))
                self.assertEqual(len(council["subs"]), 3, path.name)
                self.assertTrue(council["blind_round"], path.name)
                self.assertEqual(council["chair_model"], CHAIR, path.name)
                self.assertEqual([s["model"] for s in council["subs"]],
                                 slate, path.name)
                for sub in council["subs"]:
                    self.assertTrue(sub["brief"], path.name)
                    self.assertFalse(sub["model"].startswith("PENDING-"),
                                     (path.name, sub["model"]))
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

    def test_heldout_seeds_carry_five_claims_and_expert_slate(self):
        for c in ("C1", "C2", "C3"):
            path = SEEDS / f"eko-council-heldout-{c}.md"
            council = load_council(str(path))
            self.assertEqual(len(council["subs"]), 3, path.name)
            self.assertEqual(council["chair_model"], CHAIR, path.name)
            for n in range(1, 6):
                self.assertIn(f"(H{n})", council["question"], path.name)
            self.assertEqual([s["model"] for s in council["subs"]],
                             EXPERT_SLATE, path.name)

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

    def test_live_rejects_pending_slugs_before_any_call(self):
        called = []

        def spy_answer(who, model, messages, provider):
            called.append(model)
            return {"text": "x", "model_returned": "synthetic-stub",
                    "provider_returned": None, "response_id": None,
                    "usage": {"prompt_tokens": 1, "completion_tokens": 1,
                              "total_tokens": 2, "cost_usd": 0.0}}

        key = os.environ.pop("OPENROUTER_API_KEY", None)
        os.environ["OPENROUTER_API_KEY"] = "dummy-for-guard-test"
        try:
            # The guard is seed-independent: any PENDING slug in ANY council
            # (all-subs pending, or one pending chair over real subs) is
            # rejected before any network call. Fixtures are temp seeds.
            with tempfile.TemporaryDirectory() as tmp:
                all_pending = Path(tmp) / "all-pending.md"
                all_pending.write_text(
                    "# Council: guard probe\n"
                    "question: guard probe question\n"
                    "sub: PENDING-EXPERT-PICK-1 :: brief\n"
                    "sub: PENDING-SUB-PICK-2 :: brief\n"
                    "chair: real/chair-model\n"
                    "blind_round: yes\n")
                council = load_council(str(all_pending))
                with self.assertRaises(ValueError) as ctx:
                    run_council("live", council, 5.0,
                                Path(tmp) / "council-a", answer=spy_answer)
                self.assertIn("PENDING", str(ctx.exception))
            with tempfile.TemporaryDirectory() as tmp:
                pending_chair = Path(tmp) / "pending-chair.md"
                pending_chair.write_text(
                    "# Council: guard probe\n"
                    "question: guard probe question\n"
                    "sub: real/model :: brief\n"
                    "chair: PENDING-EXPERT-PICK-9\n"
                    "blind_round: yes\n")
                council = load_council(str(pending_chair))
                with self.assertRaises(ValueError) as ctx:
                    run_council("live", council, 5.0,
                                Path(tmp) / "council-b", answer=spy_answer)
                self.assertIn("PENDING", str(ctx.exception))
            # Guard fires before any dispatch: the answer fn is never reached.
            self.assertEqual(called, [])
        finally:
            if key is None:
                os.environ.pop("OPENROUTER_API_KEY", None)
            else:
                os.environ["OPENROUTER_API_KEY"] = key


if __name__ == "__main__":
    unittest.main()
