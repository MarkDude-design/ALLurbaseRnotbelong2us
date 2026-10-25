import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from island.runner import run, messages_for, load_topic, TOPIC
import island.runner as runner_mod


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


class RetryTests(unittest.TestCase):
    def test_retry_survives_rate_limit(self):
        calls = {"n": 0}

        def stub(who, model, messages, provider):
            calls["n"] += 1
            if calls["n"] == 1:
                raise RuntimeError("OpenRouter HTTP 429")
            return {"text": "ok " + who, "model_returned": None, "response_id": None,
                    "usage": {"cost_usd": 0.01, "total_tokens": 3}}

        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch("island.runner.time.sleep", lambda s: None):
                result = run("demo", "", "", "", "", "T", 2, 10.0, Path(tmp) / "test", answer=stub)
            events = [json.loads(x) for x in (Path(tmp) / "test" / "bus.jsonl").read_text().splitlines()]
        retries = [x for x in events if x["type"] == "retry"]
        self.assertEqual(result["turns"], 2)
        self.assertEqual(result["stop"], "error")  # retry charge requires reconciliation
        self.assertEqual(len(retries), 1)
        self.assertEqual(retries[0]["wait_s"], runner_mod.RETRY_WAIT_S)
        self.assertIn("429", retries[0]["reason"])
        self.assertEqual(retries[0]["attempt"], 1)

    def test_retry_exhaustion_stops_with_error(self):
        def stub(who, model, messages, provider):
            raise RuntimeError("OpenRouter HTTP 429")

        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch("island.runner.time.sleep", lambda s: None):
                result = run("demo", "", "", "", "", "T", 3, 10.0, Path(tmp) / "test", answer=stub)
            events = [json.loads(x) for x in (Path(tmp) / "test" / "bus.jsonl").read_text().splitlines()]
        retries = [x for x in events if x["type"] == "retry"]
        errors = [x for x in events if x["type"] == "error"]
        self.assertEqual(result["stop"], "error")
        self.assertEqual(result["turns"], 0)
        self.assertEqual(len(retries), runner_mod.RETRY_MAX)
        self.assertEqual(len(errors), 1)
        self.assertIn("429", errors[0]["error"])

    def test_backoff_doubles_between_retries(self):
        waits = []

        def stub(who, model, messages, provider):
            raise RuntimeError("OpenRouter HTTP 429")

        def fake_sleep(s):
            waits.append(s)

        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch("island.runner.time.sleep", fake_sleep):
                run("demo", "", "", "", "", "T", 2, 10.0, Path(tmp) / "test", answer=stub)
        self.assertEqual(waits, [runner_mod.RETRY_WAIT_S * (2 ** i) for i in range(runner_mod.RETRY_MAX)])

    def test_non_retryable_error_is_not_retried(self):
        def stub(who, model, messages, provider):
            raise RuntimeError("OpenRouter HTTP 402")

        with tempfile.TemporaryDirectory() as tmp:
            result = run("demo", "", "", "", "", "T", 2, 10.0, Path(tmp) / "test", answer=stub)
            events = [json.loads(x) for x in (Path(tmp) / "test" / "bus.jsonl").read_text().splitlines()]
        retries = [x for x in events if x["type"] == "retry"]
        self.assertEqual(result["stop"], "error")
        self.assertEqual(len(retries), 0)

    def test_retry_after_hint_is_honored(self):
        waits = []

        def stub(who, model, messages, provider):
            raise RuntimeError("OpenRouter HTTP 429 retry-after 30")

        def fake_sleep(s):
            waits.append(s)

        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch("island.runner.time.sleep", fake_sleep):
                run("demo", "", "", "", "", "T", 2, 10.0, Path(tmp) / "test", answer=stub)
            events = [json.loads(x) for x in (Path(tmp) / "test" / "bus.jsonl").read_text().splitlines()]
        retries = [x for x in events if x["type"] == "retry"]
        self.assertEqual(waits, [30] * runner_mod.RETRY_MAX)
        self.assertTrue(all(x["reason"].endswith("retry-after 30") for x in retries))

    def test_retry_after_hint_is_capped(self):
        waits = []

        def stub(who, model, messages, provider):
            raise RuntimeError("OpenRouter HTTP 429 retry-after 300")

        def fake_sleep(s):
            waits.append(s)

        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch("island.runner.time.sleep", fake_sleep):
                run("demo", "", "", "", "", "T", 2, 10.0, Path(tmp) / "test", answer=stub)
        self.assertEqual(waits, [runner_mod.RETRY_AFTER_CAP_S] * runner_mod.RETRY_MAX)


class PaceTests(unittest.TestCase):
    """Mark's dialing doctrine (Oct 25 2026): pace 'half' = wait the previous
    call's duration before the next call — a 50% syscall speed cut."""

    @staticmethod
    def fake_clock(step=5.0):
        state = {"now": 100.0}

        def monotonic():
            state["now"] += step
            return state["now"]
        return monotonic

    @staticmethod
    def ok_stub(who, model, messages, provider):
        return {"text": "ok " + who, "model_returned": None, "response_id": None,
                "usage": {"cost_usd": 0.01, "total_tokens": 3}}

    def test_pace_half_waits_last_call_duration_between_turns(self):
        waits = []
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch("island.runner.time.sleep", lambda s: waits.append(s)), \
                 mock.patch("island.runner.time.monotonic", self.fake_clock(5.0)):
                result = run("demo", "", "", "", "", "T", 3, 10.0, Path(tmp) / "test",
                             answer=self.ok_stub)
            events = [json.loads(x) for x in (Path(tmp) / "test" / "bus.jsonl").read_text().splitlines()]
        paces = [e for e in events if e["type"] == "pace"]
        self.assertEqual(result["turns"], 3)
        self.assertEqual(waits, [5.0, 5.0])  # one gap per call boundary: 3 calls -> 2 waits
        self.assertEqual([p["wait_s"] for p in paces], [5.0, 5.0])
        self.assertEqual(events[0].get("pace"), "half")

    def test_pace_off_dials_back_to_back(self):
        waits = []
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch("island.runner.time.sleep", lambda s: waits.append(s)), \
                 mock.patch("island.runner.time.monotonic", self.fake_clock(5.0)):
                result = run("demo", "", "", "", "", "T", 3, 10.0, Path(tmp) / "test",
                             answer=self.ok_stub, pace="off")
            events = [json.loads(x) for x in (Path(tmp) / "test" / "bus.jsonl").read_text().splitlines()]
        self.assertEqual(result["turns"], 3)
        self.assertEqual(waits, [])
        self.assertEqual([e for e in events if e["type"] == "pace"], [])
        self.assertEqual(events[0].get("pace"), "off")

    def test_instant_demo_calls_do_not_pace(self):
        # Real clock, instant stubs: durations fall below the epsilon, so the
        # default pace never slows demo runs or existing tests.
        with tempfile.TemporaryDirectory() as tmp:
            result = run("demo", "", "", "", "", "T", 3, 10.0, Path(tmp) / "test")
            events = [json.loads(x) for x in (Path(tmp) / "test" / "bus.jsonl").read_text().splitlines()]
        self.assertEqual(result["turns"], 3)
        self.assertEqual([e for e in events if e["type"] == "pace"], [])

    def test_pace_does_not_fire_after_a_failed_call(self):
        # All-fail run: retries back off, no pace event, run stops on error.
        waits = []

        def stub(who, model, messages, provider):
            raise RuntimeError("OpenRouter HTTP 429")

        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch("island.runner.time.sleep", lambda s: waits.append(s)), \
                 mock.patch("island.runner.time.monotonic", self.fake_clock(5.0)):
                run("demo", "", "", "", "", "T", 2, 10.0, Path(tmp) / "test", answer=stub)
            events = [json.loads(x) for x in (Path(tmp) / "test" / "bus.jsonl").read_text().splitlines()]
        self.assertEqual([e for e in events if e["type"] == "pace"], [])
        # Only the retry backoff fired (5s base, doubling, RETRY_MAX=4) — no
        # pace waits on top: failed calls never set last_call_s.
        self.assertEqual(waits, [5, 10, 20, 40])

    def test_invalid_pace_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                run("demo", "", "", "", "", "T", 2, 10.0, Path(tmp) / "test", pace="turbo")


class MeteringTests(unittest.TestCase):
    """Returned costs must be usable as spend receipts (Meraki preflight
    class-fix: invalid charges become UNKNOWN, without halting usable answers)."""

    def test_unusable_cost_receipt_is_unknown_and_run_continues(self):
        def stub(*args):
            return {"text": "ok", "model_returned": None, "response_id": None,
                    "usage": {"cost_usd": -0.5, "total_tokens": 2}}
        with tempfile.TemporaryDirectory() as tmp:
            result = run("demo", "", "", "", "", "T", 3, 10.0, Path(tmp) / "test", answer=stub)
            events = [json.loads(x) for x in (Path(tmp) / "test" / "bus.jsonl").read_text().splitlines()]
        self.assertEqual(result["stop"], "error")
        self.assertEqual(result["turns"], 3)
        self.assertEqual(result["totals"]["unknown_cost_calls"], 3)


class TopicFileTests(unittest.TestCase):
    def test_topic_file_wins_over_topic_string(self):
        with tempfile.TemporaryDirectory() as tmp:
            seed = Path(tmp) / "seed.md"
            seed.write_text("  Seed from file.  ", encoding="utf-8")
            self.assertEqual(load_topic("ignored", str(seed)), "Seed from file.")

    def test_missing_topic_file_fails_cleanly(self):
        with self.assertRaises(SystemExit):
            load_topic("x", "/tmp/no-such-seed-42.md")

    def test_topic_falls_back_to_default(self):
        self.assertEqual(load_topic(""), TOPIC)
        self.assertEqual(load_topic("direct topic", ""), "direct topic")
