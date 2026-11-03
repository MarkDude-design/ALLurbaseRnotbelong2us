"""Queue lane brain tests: entry parsing, cap clamping, scheduled-fire timing.

Offline, stdlib only. The workflow's drain loop imports island.queue, so
these tests pin the queue's semantics without a live tick; the shakedown
entry proves the lane end to end on the bus."""
import json
import unittest
from datetime import datetime, timedelta, timezone

from island import queue

SPEC = {"brief": "Queue shakedown: lane test, zero spend.", "mode": "demo"}


class ParseEntryTests(unittest.TestCase):
    def test_valid_entry(self):
        spec = queue.parse_entry(json.dumps(SPEC))
        self.assertEqual(spec["brief"], SPEC["brief"])

    def test_bad_json_refused(self):
        with self.assertRaises(ValueError):
            queue.parse_entry("not json at all")

    def test_non_object_refused(self):
        with self.assertRaises(ValueError):
            queue.parse_entry(json.dumps(["a", "list"]))

    def test_missing_or_empty_brief_refused(self):
        for bad in ('{"mode": "demo"}', '{"brief": ""}', '{"brief": "   "}',
                    '{"brief": 42}'):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    queue.parse_entry(bad)


class ClampedCapTests(unittest.TestCase):
    def test_numeric_caps(self):
        for raw, want in ((1, 1.0), (0.5, 0.5), ("1", 1.0), (" 0.25 ", 0.25),
                          (2.0, 1.0), ("5", 1.0)):
            with self.subTest(raw=raw):
                self.assertEqual(queue.clamped_cap({**SPEC, "cap": raw}, 1.0), want)

    def test_garbage_caps_refused(self):
        for bad in ("cheap", None, True, False, [1], {}, "nan", "inf",
                    0, -1, "0"):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    queue.clamped_cap({**SPEC, "cap": bad}, 1.0)

    def test_missing_cap_defaults_to_ceiling(self):
        self.assertEqual(queue.clamped_cap(SPEC, 1.0), 1.0)
        self.assertEqual(queue.clamped_cap(SPEC, 0.75), 0.75)


class EntryDueTests(unittest.TestCase):
    NOW = datetime(2026, 11, 3, 15, 30, tzinfo=timezone.utc)

    def test_no_not_before_always_due(self):
        for spec in (SPEC, {**SPEC, "not_before": ""}, {**SPEC, "not_before": None}):
            with self.subTest(spec=spec):
                self.assertTrue(queue.entry_due(spec, self.NOW))

    def test_past_is_due_and_future_is_not(self):
        past = (self.NOW - timedelta(minutes=60)).isoformat()
        future = (self.NOW + timedelta(minutes=60)).isoformat()
        self.assertTrue(queue.entry_due({**SPEC, "not_before": past}, self.NOW))
        self.assertFalse(queue.entry_due({**SPEC, "not_before": future}, self.NOW))
        # the 3:30-in-the-morning job: enqueued at 21:00, fires after 03:30Z
        fire_at = "2026-11-04T03:30:00Z"
        self.assertFalse(queue.entry_due({**SPEC, "not_before": fire_at},
                                         datetime(2026, 11, 4, 2, 30, tzinfo=timezone.utc)))
        self.assertTrue(queue.entry_due({**SPEC, "not_before": fire_at},
                                        datetime(2026, 11, 4, 4, 30, tzinfo=timezone.utc)))

    def test_malformed_or_naive_not_before_refused(self):
        for bad in ("3:30am", "2026-11-04", "2026-11-04T03:30:00", 42,
                    "2026-13-40T99:99:99Z"):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    queue.entry_due({**SPEC, "not_before": bad}, self.NOW)

    def test_offset_forms_accepted(self):
        for good in ("2026-11-03T15:30:00Z", "2026-11-03T15:30:00+00:00",
                     "2026-11-03T08:30:00-07:00"):
            with self.subTest(good=good):
                self.assertTrue(queue.entry_due({**SPEC, "not_before": good}, self.NOW))


if __name__ == "__main__":
    unittest.main()
