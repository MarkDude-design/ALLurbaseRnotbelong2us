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
            self.assertEqual(events[-1]["type"], "stop")
            self.assertIn("SYNTHETIC", (folder / "transcript.md").read_text())

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
