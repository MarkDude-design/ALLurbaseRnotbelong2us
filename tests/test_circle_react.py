import json
import tempfile
import unittest
from pathlib import Path

from island.circle_react import parse_command, run, validate_key_info


GOOD_KEY = {"data": {"limit": 10, "limit_reset": "monthly",
                     "limit_remaining": 8.23, "is_management_key": False}}
SEED = "A frozen, public-safe hypothetical island setup, with no observations."


class CircleReactTests(unittest.TestCase):
    def test_command_exact_and_no_bundled_args(self):
        self.assertEqual(parse_command("/circle-react demo circle-island-react-v0"),
                         ("demo", "circle-island-react-v0"))
        for bad in ("/circle-react meraki arbitrary", "/circle-react z circle-island-react-v0; echo x",
                    "/circle-react demo circle-island-react-v0\nSECOND",
                    "/circle-react bogus circle-island-react-v0"):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    parse_command(bad)

    def test_key_metadata_provider_cap(self):
        self.assertEqual(validate_key_info(GOOD_KEY)["limit_usd"], 10)
        for bad in (
            {"data": {"limit": 10, "limit_reset": None, "limit_remaining": 10}},
            {"data": {"limit": 20, "limit_reset": "monthly", "limit_remaining": 10}},
            {"data": {"limit": True, "limit_reset": "monthly", "limit_remaining": 10}},
            {"data": {"limit": 10, "limit_reset": "monthly", "limit_remaining": 0}},
            {"data": {"limit": 10, "limit_reset": "monthly", "limit_remaining": 10,
                      "is_management_key": True}},
            {},
        ):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    validate_key_info(bad)

    def test_demo_is_synthetic_and_receipted(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = str(Path(tmp) / "demo")
            result = run("demo", SEED, folder, "123")
            self.assertEqual(result["status"], "completed")
            self.assertEqual(result["known_cost_usd"], 0)
            events = [json.loads(s) for s in Path(folder, "bus.jsonl").read_text().splitlines()]
            self.assertIn("demo", [e["type"] for e in events])
            self.assertEqual(events[-1]["type"], "stop")
            self.assertIn("SYNTHETIC DEMO", Path(folder, "reaction.md").read_text())

    def test_guard_refuses_paid_call_without_provider_cap(self):
        invoked = []
        def fake_answer(*args):
            invoked.append(True)
            raise AssertionError("must not call")
        with tempfile.TemporaryDirectory() as tmp:
            res = run("meraki", SEED, str(Path(tmp) / "guard"), "124",
                      key_info={"data": {"limit": 100, "limit_reset": "monthly",
                                         "limit_remaining": 100}},
                      answer=fake_answer)
            self.assertEqual(res["status"], "key_guard_refused")
            self.assertEqual(invoked, [])

    def test_paid_reaction_has_cost_and_model_receipts(self):
        def fake_answer(model, messages, provider, max_tokens):
            self.assertEqual(model, "openai/gpt-6-luna")
            self.assertIn("falsifiably", messages[0]["content"])
            return {"text": "Make an independent comparison.", "response_id": "fake-id",
                    "model_returned": model, "usage": {
                        "cost_usd": 0.21, "prompt_tokens": 9,
                        "completion_tokens": 10, "total_tokens": 19}}
        with tempfile.TemporaryDirectory() as tmp:
            folder = str(Path(tmp) / "live")
            res = run("meraki", SEED, folder, "125", key_info=GOOD_KEY,
                      answer=fake_answer)
            self.assertEqual(res["status"], "completed")
            self.assertAlmostEqual(res["known_cost_usd"], 0.21)
            events = [json.loads(s) for s in Path(folder, "bus.jsonl").read_text().splitlines()]
            self.assertTrue(any(e.get("type") == "key_guard" for e in events))
            self.assertTrue(any(e.get("response_id") == "fake-id" for e in events))

    def test_failed_call_is_unknown_and_never_retried(self):
        seen = []
        def fail(*args):
            seen.append(1)
            raise RuntimeError("network uncertainty")
        with tempfile.TemporaryDirectory() as tmp:
            res = run("z", SEED, str(Path(tmp) / "fail"), "126", key_info=GOOD_KEY,
                      answer=fail)
            self.assertIn("unknown_charge", res["status"])
            self.assertEqual(res["unknown_charge_attempts"], 1)
            self.assertEqual(len(seen), 1)


if __name__ == "__main__":
    unittest.main()
