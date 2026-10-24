import json
import os
import tempfile
import unittest
from pathlib import Path
from island.runner import run, messages_for


class BaselineTests(unittest.TestCase):
    def test_offline_turns_and_receipts(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "test"
            result = run("demo", "", "", "", "", "Topic", 5, 10.0, folder)
            events = [json.loads(x) for x in (folder / "bus.jsonl").read_text().splitlines()]
            self.assertEqual(result["turns"], 5)
            self.assertEqual([x["speaker"] for x in events if x["type"] == "turn"],
                             ["A", "B", "A", "B", "A"])
            self.assertEqual(events[0].get("first_speaker"), "A")
            self.assertEqual(events[0].get("history_chars"), 28000)
            self.assertEqual(events[-1]["type"], "stop")
            self.assertIn("SYNTHETIC", (folder / "transcript.md").read_text())

    def test_first_speaker_b_swaps_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp) / "test"
            result = run("demo", "", "", "", "", "Topic", 4, 10.0, folder, first="B")
            events = [json.loads(x) for x in (folder / "bus.jsonl").read_text().splitlines()]
            self.assertEqual(result["turns"], 4)
            self.assertEqual([x["speaker"] for x in events if x["type"] == "turn"],
                             ["B", "A", "B", "A"])
            self.assertEqual(events[0].get("first_speaker"), "B")

    def test_invalid_first_speaker_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                run("demo", "", "", "", "", "T", 2, 10.0, Path(tmp) / "test", first="C")

    def test_history_chars_truncates_oldest_keeps_newest(self):
        history = [{"speaker": "A" if i % 2 == 0 else "B",
                   "text": f"turn {i} " + "word " * 10} for i in range(40)]
        messages = messages_for("B", history, "T", history_chars=2000)
        content = messages[1]["content"]
        self.assertLess(len(content), 2500)
        self.assertNotIn("turn 0 ", content)
        self.assertIn("turn 39 ", content)

    def test_invalid_history_chars_fails(self):
        with self.assertRaises(ValueError):
            run("demo", "", "", "", "", "T", 2, 10.0, Path("/tmp/x-invalid"),
                history_chars=10)

    def test_messages_include_previous_turns(self):
        messages = messages_for("B", [{"speaker": "A", "text": "What is calibration?"}], "T")
        self.assertIn("What is calibration?", messages[1]["content"])

    def test_spend_stop_is_retrospective(self):
        def stub(*args):
            return {"text": "test", "model_returned": None, "response_id": None,
                    "usage": {"cost_usd": .51, "total_tokens": 2}}
        with tempfile.TemporaryDirectory() as tmp:
            result = run("demo", "", "", "", "", "T", 10, 1.0, Path(tmp) / "test", answer=stub)
            self.assertEqual(result["turns"], 2)
            self.assertEqual(result["stop"], "local_budget_reached")
            self.assertGreater(result["totals"]["cost_usd"], 1.0)

    def test_invalid_spend_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                run("demo", "", "", "", "", "T", 2, 11, Path(tmp) / "test")

    def test_live_rejects_absent_key(self):
        old = os.environ.pop("OPENROUTER_API_KEY", None)
        try:
            with tempfile.TemporaryDirectory() as tmp:
                with self.assertRaises(ValueError):
                    run("live", "author/a", "author/b", "", "", "T", 2, 1,
                        Path(tmp) / "test")
        finally:
            if old is not None:
                os.environ["OPENROUTER_API_KEY"] = old
