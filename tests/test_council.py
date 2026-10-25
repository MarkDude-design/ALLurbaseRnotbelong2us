import json
import os
import tempfile
import unittest
from pathlib import Path

from island.council import run_council, load_council


SEED = """# Council: test island
question: How would Eko and another agent act on the island?
context: Eko facts only.
sub: model/sub-one :: experiment designer
sub: model/sub-two :: skeptic
chair: model/chair
blind_round: yes
"""


def stub_answer(text="x", cost_usd=0.01):
    def answer(who, model, messages, provider):
        return {"text": text, "model_returned": None, "response_id": None,
                "usage": {"cost_usd": cost_usd, "total_tokens": 1}}
    return answer


class CouncilSeedTests(unittest.TestCase):
    def test_seed_parses(self):
        with tempfile.TemporaryDirectory() as tmp:
            seed = Path(tmp) / "council.md"
            seed.write_text(SEED, encoding="utf-8")
            council = load_council(str(seed))
        self.assertEqual(council["title"], "Council: test island")
        self.assertIn("Eko", council["question"])
        self.assertEqual(len(council["subs"]), 2)
        self.assertEqual(council["subs"][0]["model"], "model/sub-one")
        self.assertEqual(council["subs"][1]["brief"], "skeptic")
        self.assertEqual(council["chair_model"], "model/chair")
        self.assertTrue(council["blind_round"])

    def test_missing_seed_fails_cleanly(self):
        with self.assertRaises(SystemExit):
            load_council("/tmp/no-such-council-42.md")

    def test_seed_without_subs_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            seed = Path(tmp) / "council.md"
            seed.write_text("question: Q\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                load_council(str(seed))

    def test_seed_without_question_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            seed = Path(tmp) / "council.md"
            seed.write_text("sub: m :: brief\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                load_council(str(seed))


class CouncilRunTests(unittest.TestCase):
    def council(self, blind_round=True):
        return {"title": "t", "question": "Q?", "context": "c",
                "chair_model": "m/chair", "blind_round": blind_round,
                "subs": [{"model": "m/1", "brief": "alpha"},
                         {"model": "m/2", "brief": "beta"}]}

    def test_demo_run_event_sequence(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "council"
            result = run_council("demo", self.council(), 10.0, folder)
            events = [json.loads(x) for x in (folder / "bus.jsonl").read_text().splitlines()]
            transcript = (folder / "transcript.md").read_text()
            report = (folder / "report.md").read_text()
        phases = [e["phase"] for e in events if e["type"] == "turn"]
        self.assertEqual(result["stop"], "completed")
        self.assertEqual(result["subs"], 2)
        self.assertEqual(result["critiques"], 2)
        self.assertEqual(phases, ["sub", "sub", "synthesis",
                                  "critique", "critique", "verdict"])
        self.assertEqual(events[0]["type"], "start")
        self.assertTrue(events[0]["blind_round"])
        self.assertEqual(events[-1]["type"], "stop")
        self.assertIn("SYNTHETIC", transcript)
        self.assertIn("council-demo", report)

    def test_subs_do_not_see_each_other(self):
        captured = []

        def answer(who, model, messages, provider):
            captured.append((who, messages[0]["content"] + "\n" + messages[1]["content"]))
            return stub_answer("text-of-" + who)(who, model, messages, provider)

        with tempfile.TemporaryDirectory() as tmp:
            run_council("demo", self.council(blind_round=False), 10.0,
                        Path(tmp) / "council", answer=answer)
        subs = [c for who, c in captured if who.startswith("sub")]
        chair = [c for who, c in captured if who == "chair"]
        self.assertEqual(len(subs), 2)
        self.assertIn("alpha", subs[0])
        self.assertNotIn("beta", subs[0])
        self.assertIn("beta", subs[1])
        self.assertNotIn("alpha", subs[1])
        self.assertEqual(len(chair), 2)  # synthesis + verdict
        self.assertIn("text-of-sub1", chair[0])  # chair sees the answers
        self.assertIn("text-of-sub2", chair[0])

    def test_blind_critique_sees_synthesis_not_sub_answers(self):
        captured = []

        def answer(who, model, messages, provider):
            captured.append((who, messages[1]["content"]))
            return stub_answer("text-of-" + who)(who, model, messages, provider)

        with tempfile.TemporaryDirectory() as tmp:
            run_council("demo", self.council(blind_round=True), 10.0,
                        Path(tmp) / "council", answer=answer)
        sub_calls = [c for who, c in captured if who.startswith("sub")]
        self.assertEqual(len(sub_calls), 4)  # 2 subs + 2 blind critiques
        for critique in sub_calls[2:]:
            self.assertIn("text-of-chair", critique)
            self.assertNotIn("text-of-sub1", critique)
            self.assertNotIn("text-of-sub2", critique)

    def test_budget_soft_stop_after_call(self):
        # Budget is a SOFT, post-call stop: spend is checked between calls, so
        # total spend may exceed max_cost_usd by at most one call's cost
        # (here: $1.00 cap, two $0.60 calls -> $1.20). A hard ceiling would need
        # a provider-side bound or pre-call reservation.
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "council"
            result = run_council("demo", self.council(blind_round=True), 1.0,
                                 folder, answer=stub_answer(cost_usd=0.6))
            events = [json.loads(x) for x in (folder / "bus.jsonl").read_text().splitlines()]
        self.assertEqual(result["stop"], "local_budget_reached")
        self.assertEqual(result["subs"], 2)
        self.assertEqual(result["critiques"], 0)
        self.assertGreater(result["totals"]["cost_usd"], 1.0)
        self.assertEqual(events[-1]["type"], "stop")

    def test_non_retryable_error_stops_council(self):
        def answer(who, model, messages, provider):
            raise RuntimeError("OpenRouter HTTP 402")

        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "council"
            result = run_council("demo", self.council(), 10.0, folder, answer=answer)
            events = [json.loads(x) for x in (folder / "bus.jsonl").read_text().splitlines()]
        errors = [e for e in events if e["type"] == "error"]
        retries = [e for e in events if e["type"] == "retry"]
        self.assertEqual(result["stop"], "error")
        self.assertEqual(result["subs"], 0)
        self.assertEqual(len(errors), 1)
        self.assertEqual(len(retries), 0)

    def test_invalid_budget_fails(self):
        with self.assertRaises(ValueError):
            run_council("demo", self.council(), 11, Path("/tmp/x-invalid-council"))

    def test_live_rejects_absent_key(self):
        old = os.environ.pop("OPENROUTER_API_KEY", None)
        try:
            with self.assertRaises(ValueError):
                run_council("live", self.council(), 1.0, Path("/tmp/x-invalid-live"))
        finally:
            if old is not None:
                os.environ["OPENROUTER_API_KEY"] = old


if __name__ == "__main__":
    unittest.main()
