import json
import os
import tempfile
import unittest
from pathlib import Path

from island.mayhem_meter import (CLASSES, STATUSES, counts, demo, record,
                                 read_events, render, replay_bus)


class MeterTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.log = Path(self.tmp.name) / "meter.jsonl"
        self.addCleanup(self.tmp.cleanup)

    def test_record_roundtrip(self):
        ev = record(self.log, "Z", "push", "OK", "TRANSPORT",
                    "sha 05cb4ba", cost=0.0, note="mayhem standard v0.1 posted")
        events = read_events(self.log)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["actor"], "Z")
        self.assertEqual(events[0]["status"], "OK")
        self.assertEqual(events[0]["class"], "TRANSPORT")
        self.assertEqual(events[0]["cost"], 0.0)
        self.assertIn("ts", events[0])
        self.assertTrue(ev["ts"].endswith("Z"))

    def test_enum_validation(self):
        with self.assertRaises(ValueError):
            record(self.log, "Z", "push", "MAYBE", "TRANSPORT", "sha")
        with self.assertRaises(ValueError):
            record(self.log, "Z", "push", "OK", "NATURAL_DISASTER", "sha")

    def test_cost_law(self):
        record(self.log, "Z", "fetch", "OK", "TOOLING", "sha", cost=0.0)
        events = read_events(self.log)
        self.assertEqual(events[0]["cost"], 0.0)  # zero is data, recorded
        with self.assertRaises(ValueError):
            record(self.log, "Z", "fetch", "OK", "TOOLING", "sha", cost=-0.01)
        with self.assertRaises(ValueError):
            record(self.log, "Z", "fetch", "OK", "TOOLING", "sha",
                   cost=float("nan"))
        with self.assertRaises(ValueError):
            record(self.log, "Z", "fetch", "OK", "TOOLING", "sha", cost=True)

    def test_evidence_never_omitted(self):
        with self.assertRaises(ValueError):
            record(self.log, "Z", "push", "OK", "FIDELITY", "  ")

    def test_extensions(self):
        record(self.log, "Bing", "sit", "OK", "FIDELITY", "datum relay",
               cost=0.0, x_bing_grin=True)
        ev = read_events(self.log)[0]
        self.assertTrue(ev.get("x_bing_grin"))
        with self.assertRaises(ValueError):
            record(self.log, "Bing", "sit", "OK", "FIDELITY", "datum",
                   ts="FAKE-TS")  # shadows core ts — refused
        with self.assertRaises(ValueError):
            record(self.log, "Bing", "sit", "OK", "FIDELITY", "datum",
                   bing_grin=True)  # not x_-prefixed — refused

    def test_honest_null(self):
        record(self.log, "Z", "scan", "NULL", "TOOLING",
               "13 repos: API 502s, retried, queued", cost=0.0)
        c = counts(self.log)
        self.assertEqual(c["by_status"]["NULL"], 1)

    def test_counts_and_render(self):
        record(self.log, "diff", "consult", "OK", "TOOLING", "r1", cost=0.01)
        record(self.log, "man", "consult", "ERROR", "TRANSPORT", "r1 timeout")
        record(self.log, "man", "consult", "ERROR", "TOOLING", "r1 retry")
        c = counts(self.log)
        self.assertEqual(c["events"], 3)
        self.assertEqual(c["by_status"]["OK"], 1)
        self.assertEqual(c["by_status"]["ERROR"], 2)
        self.assertEqual(c["cost_usd"], 0.01)
        text = render(self.log)
        self.assertIn("TRANSPORT", text)
        self.assertIn("Misses are kept", text)

    def test_replay_bus(self):
        bus = Path(self.tmp.name) / "bus.jsonl"
        events = [
            {"type": "start", "utc": "t0", "run_id": "r1"},
            {"type": "consult", "utc": "t1", "agent": "diff", "ts": "t1",
             "usage": {"cost_usd": 0.012},
             "verdict": {"verdict": "CLEAN"}},
            {"type": "retry", "utc": "t2", "agent": "man", "attempt": 1,
             "reason": "502 upstream"},
            {"type": "error", "utc": "t3", "agent": "man",
             "error": "connection timeout"},
            {"type": "stop", "utc": "t4", "reason": "completed"},
        ]
        bus.write_text("\n".join(json.dumps(e) for e in events) + "\n",
                       encoding="utf-8")
        written = replay_bus(bus, self.log, "run r1")
        self.assertEqual(written, 3)
        c = counts(self.log)
        self.assertEqual(c["by_status"]["OK"], 1)
        self.assertEqual(c["by_status"]["ERROR"], 2)
        self.assertEqual(c["by_class"]["TRANSPORT"], 1)
        self.assertEqual(c["cost_usd"], 0.012)

    def test_demo_deterministic_and_scale(self):
        demo(self.log, 50, seed=42)
        c1 = counts(self.log)
        other = Path(self.tmp.name) / "other.jsonl"
        demo(other, 50, seed=42)
        c2 = counts(other)
        self.assertEqual(c1["events"], 50)
        self.assertEqual(c1["by_status"]["OK"], c2["by_status"]["OK"])
        self.assertEqual(c1["by_status"]["ERROR"], c2["by_status"]["ERROR"])
        self.assertEqual(c1["by_class"]["FIDELITY"],
                         c2["by_class"]["FIDELITY"])
        self.assertGreater(c1["by_status"]["ERROR"], 0)  # failures counted, not hidden


if __name__ == "__main__":
    unittest.main()
