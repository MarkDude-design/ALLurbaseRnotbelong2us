"""Z Desk tests: demo runs, cap validation, secret red-line, verdict parsing."""
import json
import re
import unittest
from unittest import mock
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


class ZDeskPaceTests(unittest.TestCase):
    """Mark's dialing doctrine (Oct 25 2026): pace 'half' = wait the previous
    consult's duration before the next call — a 50% syscall speed cut."""

    @staticmethod
    def fake_clock(step=5.0):
        state = {"now": 100.0}

        def monotonic():
            state["now"] += step
            return state["now"]
        return monotonic

    def test_pace_half_between_agents(self):
        # 2 agents -> 2 calls -> 1 pace wait of 5.0s before the second call.
        waits = []
        with TemporaryDirectory() as tmp:
            outdir = Path(tmp) / "desk"
            with mock.patch("island.z_desk.time.sleep", lambda s: waits.append(s)), \
                 mock.patch("island.z_desk.time.monotonic", self.fake_clock(5.0)):
                result = z_desk.run("demo", ["diff", "man"],
                                    {"diff": "dmodel", "man": "mmodel"},
                                    BRIEF, 1.0, outdir)
            lines = [json.loads(x) for x in
                     (outdir / "bus.jsonl").read_text(encoding="utf-8").splitlines()]
        paces = [e for e in lines if e["type"] == "pace"]
        self.assertEqual(result["stop"], "completed")
        self.assertEqual(waits, [5.0])
        self.assertEqual([p["wait_s"] for p in paces], [5.0])
        self.assertEqual(paces[0]["agent"], "man")
        self.assertEqual(lines[0].get("pace"), "half")

    def test_pace_off_dials_back_to_back(self):
        waits = []
        with TemporaryDirectory() as tmp:
            outdir = Path(tmp) / "desk"
            with mock.patch("island.z_desk.time.sleep", lambda s: waits.append(s)), \
                 mock.patch("island.z_desk.time.monotonic", self.fake_clock(5.0)):
                result = z_desk.run("demo", ["diff", "man"],
                                    {"diff": "dmodel", "man": "mmodel"},
                                    BRIEF, 1.0, outdir, pace="off")
            lines = [json.loads(x) for x in
                     (outdir / "bus.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(result["stop"], "completed")
        self.assertEqual(waits, [])
        self.assertEqual([e for e in lines if e["type"] == "pace"], [])
        self.assertEqual(lines[0].get("pace"), "off")

    def test_invalid_pace_fails(self):
        with self.assertRaises(ValueError):
            z_desk.run("demo", ["diff"], {"diff": "dmodel", "man": "mmodel"},
                       BRIEF, 1.0, "runs/never-created", pace="turbo")


class ZDeskPreflightTests(unittest.TestCase):
    """Meraki preflight (issue #9, comment 6401118055): no free-text workflow
    input may land in shell source, and returned costs must be usable as spend
    receipts. Static, offline, no network."""

    def test_workflow_inputs_not_interpolated_in_shell(self):
        # Every dynamic input reaches the shell only as an env var VALUE, so a
        # metacharacter-shaped input stays literal data, never executable.
        # Pin it: no ${{ }} expression may appear inside any run: block.
        yml = Path(".github/workflows/z-desk.yml").read_text(encoding="utf-8")
        in_run_block = False
        run_indent = 0
        offenders = []
        for line in yml.splitlines():
            if not in_run_block:
                m = re.match(r"^(\s*)run: \|\s*$", line)
                if m:
                    in_run_block = True
                    run_indent = len(m.group(1))
                continue
            if line.strip() and len(line) - len(line.lstrip()) <= run_indent:
                in_run_block = False
                continue
            if "${{" in line:
                offenders.append(line.strip())
        self.assertEqual(offenders, [])

    def test_unusable_cost_receipts_refused(self):
        # negative / NaN / inf / bool costs are not valid spend receipts
        for bad_cost in (-0.01, float("nan"), float("inf"), True):
            def answer(agent, model, messages, provider, bad=bad_cost):
                return {"text": "ok", "model_returned": None, "response_id": None,
                        "usage": {"cost_usd": bad, "total_tokens": 1}}
            with TemporaryDirectory() as tmp:
                outdir = Path(tmp) / "desk"
                result = z_desk.run("demo", ["diff"],
                                    {"diff": "dmodel", "man": "mmodel"},
                                    BRIEF, 1.0, outdir, answer=answer)
                lines = [json.loads(x) for x in
                         (outdir / "bus.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(result["stop"], "error")
            self.assertEqual([e for e in lines if e["type"] == "consult"], [])
            self.assertEqual(len([e for e in lines if e["type"] == "error"]), 1)

    def test_shell_metacharacter_model_ids_refused(self):
        # model IDs are data, never shell source (Meraki preflight #1, data side)
        for bad in ("sh -c x", "a;b", "$(x)", "a`b", "x y", "a\nb"):
            with self.assertRaises(ValueError):
                z_desk.run("demo", ["diff"], {"diff": bad, "man": "mmodel"},
                           BRIEF, 1.0, "runs/never-created")


if __name__ == "__main__":
    unittest.main()
