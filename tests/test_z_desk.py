"""Z Desk tests: demo runs, cap validation, secret red-line, verdict parsing."""
import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from island import z_desk

BRIEF = ("Claim: the audit found 22 coded rows, zero UNRESOLVED among the displayed "
         "rows, and 31 extracted ask-lines corpus-wide.")


def run_demo(agents=("diff", "man"), brief=BRIEF, cap=1.0, **kw):
    with TemporaryDirectory() as tmp:
        outdir = Path(tmp) / "desk"
        result = z_desk.run("demo", list(agents), {"diff": "dmodel", "man": "mmodel"},
                            brief, cap, outdir, **kw)
        lines = [json.loads(x) for x in (outdir / "bus.jsonl").read_text(encoding="utf-8").splitlines()]
        files = {"report.md": (outdir / "report.md").read_text(encoding="utf-8"),
                 "consult.md": (outdir / "consult.md").read_text(encoding="utf-8")}
        return result, lines, files


class ZDeskDemoRun(unittest.TestCase):
    def test_demo_two_agents_completed(self):
        result, lines, files = run_demo()
        self.assertEqual(result["stop"], "completed")
        consults = [e for e in lines if e["type"] == "consult"]
        self.assertEqual(len(consults), 2)
        self.assertEqual({e["agent"] for e in consults}, {"diff", "man"})
        for consult in consults:
            self.assertEqual(consult["verdict"]["verdict"], "CLEAN")
            self.assertEqual(consult["usage"]["cost_usd"], 0.0)
        self.assertEqual(result["totals"]["cost_usd"], 0.0)
        self.assertIn("Stop: completed", files["report.md"])
        self.assertIn("## diff", files["consult.md"])
        self.assertIn("## man", files["consult.md"])
        self.assertIn(BRIEF, files["consult.md"])
        self.assertEqual(lines[0]["type"], "start")
        self.assertEqual(lines[-1]["type"], "stop")
        self.assertEqual(lines[-1]["reason"], "completed")
        self.assertEqual(lines[-1]["turns"], 2)
        self.assertEqual(len(lines[0]["brief_sha256"]), 64)
        self.assertEqual(lines[0]["agents"], ["diff", "man"])

    def test_single_agent(self):
        result, lines, _ = run_demo(agents=("diff",))
        self.assertEqual(result["stop"], "completed")
        self.assertEqual(len([e for e in lines if e["type"] == "consult"]), 1)
        self.assertEqual(lines[0]["agents"], ["diff"])

    def test_cap_ceiling_boundary(self):
        # $20 exactly is allowed; the provider key cap still governs above it.
        result, _, _ = run_demo(cap=20.0)
        self.assertEqual(result["stop"], "completed")

    def test_invalid_caps_refused(self):
        for bad in (0, -1, float("nan"), float("inf"), 20.5, "1", None, True):
            with self.assertRaises(ValueError):
                z_desk.run("demo", ["diff"], {"diff": "dmodel", "man": "mmodel"},
                           BRIEF, bad, "runs/never-created")

    def test_secret_brief_refused(self):
        for brief in ("paste this sk-or-v1-9f3e21c04a7b8d6e5f4c3b2a1908e7d6 now",
                      "token ghp_abcdefghijklmnopqrstuvwxyz1234567890 here",
                      "creds AKIAIOSFODNN7EXAMPLE xoxb-123"):
            with self.assertRaises(ValueError):
                z_desk.run("demo", ["diff"], {"diff": "dmodel", "man": "mmodel"},
                           brief, 1.0, "runs/never-created")

    def test_empty_and_bad_agents_refused(self):
        run = z_desk.run
        with self.assertRaises(ValueError):
            run("demo", [], {"diff": "dmodel", "man": "mmodel"}, BRIEF, 1.0, "runs/never")
        with self.assertRaises(ValueError):
            run("demo", ["sudo"], {"diff": "dmodel", "man": "mmodel"}, BRIEF, 1.0, "runs/never")
        with self.assertRaises(ValueError):
            run("demo", ["diff"], {"diff": "", "man": "mmodel"}, BRIEF, 1.0, "runs/never")
        with self.assertRaises(ValueError):
            run("demo", ["diff"], {"diff": "dmodel", "man": "mmodel"}, "  ", 1.0, "runs/never")

    def test_live_without_key_refused(self):
        import os
        key = os.environ.pop("OPENROUTER_API_KEY", None)
        try:
            with self.assertRaises(ValueError):
                z_desk.run("live", ["diff"], {"diff": "dmodel", "man": "mmodel"},
                           BRIEF, 1.0, "runs/never-created")
        finally:
            if key is not None:
                os.environ["OPENROUTER_API_KEY"] = key

    def test_agent_failure_is_receipted_not_fatal_to_peers(self):
        def flaky(agent, model, messages, provider):
            if agent == "diff":
                raise RuntimeError("OpenRouter HTTP 429")
            return z_desk.demo_consult(agent, model, messages, provider)

        with TemporaryDirectory() as tmp:
            outdir = Path(tmp) / "desk"
            result = z_desk.run("demo", ["diff", "man"],
                                {"diff": "dmodel", "man": "mmodel"},
                                BRIEF, 1.0, outdir, answer=flaky)
            lines = [json.loads(x) for x in (outdir / "bus.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(result["stop"], "error")
            self.assertEqual(len([e for e in lines if e["type"] == "error"]), 1)
            self.assertEqual(len([e for e in lines if e["type"] == "retry"]), 4)
            consults = [e for e in lines if e["type"] == "consult"]
            self.assertEqual([e["agent"] for e in consults], ["man"])
            self.assertEqual(consults[0]["verdict"]["verdict"], "CLEAN")

    def test_parse_verdict(self):
        self.assertEqual(z_desk.parse_verdict("no json at all")["verdict"], "UNPARSEABLE")
        verdict = z_desk.parse_verdict('prefix {"verdict": "ISSUES_FOUND", '
                                        '"findings": [{"kind": "absolutes"}]} suffix')
        self.assertEqual(verdict["verdict"], "ISSUES_FOUND")
        self.assertEqual(verdict["findings"][0]["kind"], "absolutes")
        self.assertIsNone(verdict.get("confidence"))
        bad = z_desk.parse_verdict('{"verdict": "GREAT", "findings": []}')
        self.assertEqual(bad["verdict"], "UNPARSEABLE")


if __name__ == "__main__":
    unittest.main()
