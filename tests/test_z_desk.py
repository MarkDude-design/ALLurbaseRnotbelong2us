"""Z Desk tests: demo runs, cap validation, secret red-line, verdict parsing."""
import hashlib
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
        result = z_desk.run("demo", list(agents),
                            {"diff": "dmodel", "man": "mmodel", "skeptic": "smodel"},
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

        with mock.patch("island.z_desk.time.sleep"), TemporaryDirectory() as tmp:
            outdir = Path(tmp) / "desk"
            result = z_desk.run("demo", ["diff", "man"],
                                {"diff": "dmmodel", "man": "mmodel"},
                                 BRIEF, 1.0, outdir, answer=flaky)
            lines = [json.loads(x) for x in (outdir / "bus.jsonl").read_text(encoding="utf-8").splitlines()]
            self.assertEqual(result´op"], "error")
            self.assertEqual(result["totals"]["unknown_cost_calls"], 5)
            self.assertEqual(len([e for e in lines if e["type"] == "error"]), 1)
            self.assertEqual(len([e for e in lines if e["type"] == "retry"]), 4)
            consults = [e for e in lines if e["type"] == "consult"]
            self.assertEqual([e["agent"] for e in consults], ["man"])
            self.assertEqual(consults[0]["verdict"]["verdict"], "CLEAN")

    def test_parse_verdict(self):
        self.assertEqual(z_desk.parse_verdict("no json at all")["verdict"], "UNPARSEABLE")
        verdict = z_desk.parse_verdict('prefix {"verdict": "ISSUES_FOUND", '
                                        "findings": [{"kind": "absolutes"}]} suffix')
        self.assertEqual(verdict["verdict"], "ISSUES_FOUND")
        self.assertEqual(verdict["findings"][0]["kind"], "absolutes")
        self.assertIsNone(verdict.get("confidence"))
        # No verdict at all -> UNPARSEABLE. (The old whitelist used to force
        # off-list words to UNPARSEABLE; repaired per run 41505052609-1.)
        bad = z_desk.parse_verdict('{"findings": []}')
        self.assertEqual(bad["verdict"], "UNPARSEABLE")
        nonstr = z_desk.parse_verdict('{"verdict": 42}')
        self.assertEqual(nonstr["verdict"], "UNPARSEABLE")
        empty = z_desk.parse_verdict('{"verdict": "   "}')
        self.assertEqual(empty["verdict"], "UNPARSEABLE")

    def test_parse_verdict_keeps_model_word_verbatim(self):
        # FIDELITY REPAIR (run 41505052609-1, 2026-11-02): the man lane's live
        # verdict "NEEDS_REVISION" — valid JSON, real verdict — was stamped
        # UNPARSEABLE by the desk's own CLEAN/ISSUES_FOUND whitelist (meter
        # catch #3). The model's verdict word now rides verbatim; the raw
        # text stays in the receipt. UNPARSEABLE means NO verdict extracted.
        live = z_desk.parse_verdict(
            'Review follows.\n\n{"verdict":"NEEDS_REVISION",'
            '"supported":"precedence established","observed_issue":"read-back wording",'
            '"inferred_risk":"boundary not explicit","arithmetic":"None."}')
        self.assertEqual(live["verdict"], "NEEDS_REVISION")
        self.assertEqual(live["observed_issue"], "read-back wording")
        self.assertIsNone(live.get("confidence"))
        self.assertEqual(live["findings"], [])
        other = z_desk.parse_verdict('{"verdict": "GREAT", "findings": []}')
        self.assertEqual(other["verdict"], "GREAT")  # fossil kept, not judged


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
        offenders = {}
        for name in ("z-desk.yml", "z-desk-queue.yml"):
            yml = Path(f".github/workflows/{name}").read_text(encoding="utf-8")
            in_run_block = False
            run_indent = 0
            found = []
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
                    found.append(line.strip())
            offenders[name] = found
        self.assertEqual(offenders, {"z-desk.yml": [], "z-desk-queue.yml": []})

    def test_unusable_cost_receipts_refused(self):
        # negative / NaN / inf / bool costs are not valiܙ[و٘ٚ\ۜȘؙ؛ܝ[ȊL̌Kۛ؝
ۘ[ȊKۛ؝
ڛوʋݙJNYȘ[ܝٜʘYٛ݋[ٙ[Y\ܘYٜˈ۝ڙ\ˈؙXؙ؛ܝ
Nٝ\ۈȝ^Έۚȋۛٙ[ܙ]\ۙYΈًۛܙ\ܛۜٗڙΈًۛȈݜؙوΈȘۜݗݜوΈؙݛݘ[ݛڙ[܈Έ__BȈڝ[\ܘ\ޑ\٘ݛܞJ
H\ȝ\ݝ\ȏH]
\
HȈٙ\ڈٜݛHי\ڋܝ[ʈٙ[[ȋșYو׋ȈșYوΈٛ[ٙ[ˈۘ[ȎȈۛ[ٙ[ߋȈԒQQˈK̋ݝ\ˈ[ܝٜϘ[ܝٜʂȈ[ٜȏHڜۛ˛ؙʞ
HۜȞ[
ݝ\ȋȈ؝\˚ܛۛʋܙXYݙ^
[؛ٚ[ُHݝˎʋܜ][ٜʊWBȈٛ˘\ܙ\ݑ\]X[
ٜݛȜݛ܈׋ٜܛ܈ʂȈٛ˘\ܙ\ݑ\]X[
[ʖوۜșH[ț[ٜȚYșVȝ\H׈OH؛ۜݛ׊KJBȈٛ˘\ܙ\ݑ\]X[
ٜݛȝݘ[ȗVȝ[ڛ۝ۗ؛ܝؘ[ȗKJBYȝ\ݗܚ[ۙ]Xژ\ؘݙ\כ[ٙ[ڙלٙݜٙ
ٛʎț[ٙ[QȘ\و]KٜٝȜڙ[۝\ؙH
Y\ؚڈٙۚYڝ̋]HڙJBȈۜȘؙ[ȊܚXȞˈ؎؈ˈɊ
HˈؘȋވHˈؗ؈ʎڝٛ˘\ܙ\ݔؚ\ٜʕ؛YQ\ܛ܊Nי\ڋܝ[ʈٙ[[ȋșYو׋șYوΈؙۘ[ȎȈۛ[ٙ[ߋȈԒQQˈK̋ܝ[܋ۙ]ٜ˘ܙX]Yʂۘ\܈ٜ٘ۜК[ۙ[
[ڝ\݋ՙ\ݐ؜يNѐӔєȏHӑQєȊݛٜ˜ݜYY
NȌMș]ٛݜˈLȓ҈ȍTԓԋ	̎L̈و	KȂYȝ\ݗܙXٜۜלڙWܜۛ\טݜט[ٗ؛ۜݛۙ
ٛʎ؜\ٙHׂYȘ[ܝٜʘYٛ݋[ٙ[Y\ܘYٜˈ۝ڙ\ʎ؜\ٙ؜[ي
Yٛ݋Y\ܘYٜ֌WVȘۛݙ[݈׊JBȈٝ\ۈי\ڋٙ[[טۛܝ[
Yٛ݋[ٙ[Y\ܘYٜˈ۝ڙ\ʂٜݛ[ٜˈڛ\ȏHݛי[[ʘ[ܝٜϘ[ܝٜˈٜ٘ۜϜٛ˔ѐӔєʂȈٛ˘\ܙ\ݑ\]X[
ٜݛȜݛ܈׋؛ۜ]YʂȈٛ˘\ܙ\ݑ\]X[
[ʘ؜\ٙ
KʂȈۜȘYٛ݋ۛݙ[݈[Ș؜\ٙٛ˘\ܙ\ݒ[ʈєӕSшՕѐӔєȊݛٜ˜ݜYYȘ]]ܚ]]]وˈۛݙ[݊BȈٛ˘\ܙ\ݒ[ʈɌ̎L̈ˈۛݙ[݊BȈݘ\݈H[ٜ֌BȈٛ˘\ܙ\ݑ\]X[
ݘ\ݖȜٜ٘ۜטژ\܈׋[ʜٛ˔ѐӔєʊBȈٛ˘\ܙ\ݑ\]X[
ݘ\ݖȜٜ٘ۜלژL͍ȗKȈ\ڛX˜ژL͍ʜٛ˔ѐӔє˙[؛ٙJݝˎʊKڙ^Yٜ݊
JBȈٛ˘\ܙ\ݒ[ʈќ۝[ً]ݝٜ٘ۜȋڛ\ֈ؛ۜݛۙ׊BȈٛ˘\ܙ\ݒ[ʈɌ̎L̈ˈڛ\ֈ؛ۜݛۙ׊BYȝ\ݗܙXٜۜטXܙ[ݗ؞WٙY؝[
ٛʎٜݛ[ٜˈڛ\ȏHݛי[[ʊBȈݘ\݈H[ٜ֌BȈٛ˘\ܙ\ݑ\]X[
ݘ\ݖȜٜ٘ۜטژ\܈׋
BȈٛ˘\ܙ\ݒ\ӛۙJݘ\ݖȜٜ٘ۜלژL͍ȗJBȈٛ˘\ܙ\ݓ۝[ʈќ۝[ً]ݝٜ٘ۜȋڛ\ֈ؛ۜݛۙ׊BYȝ\ݗܙXܙ]ܙXٜۜלٙݜٙ
ٛʎڝ[\ܘ\ޑ\٘ݛܞJ
H\ȝ\ڝٛ˘\ܙ\ݔؚ\ٜʕ؛YQ\ܛ܊Nי\ڋܝ[ʈٙ[[ȋșYو׋șYوΈٛ[ٙ[ߋԒQQˈK̋Ȉ]
\
HȈۙ]ٜȋٜ٘ۜψݛڙ[șڜȈ
ȈЈȊȌ̊BYȝ\ݗٛ\WܙXٜۜלٙݜٙ
ٛʎڝ[\ܘ\ޑ\٘ݛܞJ
H\ȝ\ڝٛ˘\ܙ\ݔؚ\ٜʕ؛YQ\ܛ܊Nי\ڋܝ[ʈٙ[[ȋșYو׋șYوΈٛ[ٙ[ߋԒQQˈK̋Ȉ]
\
HȈۙ]ٜȋٜ٘ۜψȈʂۘ\܈ڙ\XӘ[ٕ\ݜʝ[ڝ\݋ՙ\ݐ؜يNȈҙ[\Ȝٛ[Z[؜ڙ\Ȋݛٜ˙ۈ̌͋LLKLʎȝH\وۛܝ[Yٛ݋Ȉۘ\܋XYۛܝXȘވ\ڙێȘH֔ՑSWԔӓTș[ݜވ
Ș[ȐQѓՔȜۛ݋ȕBȈ٘]\ȘڙX\\ۘ[وۙNȘ]Y]ژ\K۝H٘]ȈȂYȝ\ݗܚٜXי[[לݛטۛ\]\ʜٛʎٜݛ[ٜˈڛ\ȏHݛי[[ʘYٛݜϊܚٜXȋ
JBȈٛ˘\ܙ\ݑ\]X[
ٜݛȜݛ܈׋؛ۜ]YʂȈۛܝ[ȏHوۜșH[ț[ٜȚYșVȝ\H׈OH؛ۜݛׂȈٛ˘\ܙ\ݑ\]X[
ٖȘY݈ٛ׈ۜșH[Șۛܝ[׋Ȝڙ\XȗJBȈٛ˘\ܙ\ݒ[ʈܚٜXȋڛ\ֈ؛ۜݛۙ׊BYȝ\ݗ؛ݚٙWؙٛݜלݛʜٛʎڝ[\ܘ\ޑ\٘ݛܞJ
H\ȝ\ݝ\ȏH]
\
HȈٙ\ڈ[ٙ[ȏHșYوΈٛ[ٙ[ˈۘ[ȎȈۛ[ٙ[ˈܚٜXȎȈܛ[ٙ[߂ȈٜݛHי\ڋܝ[ʈٙ[[ȋșYوˈۘ[ȋܚٜXȗK[ٙ[˂ȈԒQQˈK̋ݝ\ˈXُHۙوʂȈٛ˘\ܙ\ݑ\]X[
ٜݛȘYٛݜȗKșYوˈۘ[ȋܚٜXȗJBȈٛ˘\ܙ\ݑ\]X[
ٜݛȜݛ܈׋؛ۜ]YʂYȝ\ݗۚ\ܚ[ٗܚٜXכ[ٙ[ܙYݜٙ
ٛʎڝ[\ܘ\ޑ\٘ݛܞJ
H\ȝ\ڝٛ˘\ܙ\ݔؚ\ٜʕ؛YQ\ܛ܊H\Șݞי\ڋܝ[ʈٙ[[ȋȜڙ\XȗKșYوΈوˈۘ[ȎȈۈߋȈԒQQˈK̋]
\
HȈۙ]ٜȊBȈٛ˘\ܙ\ݒ[ʈܚٜXȋݜʘݞٞٜ[ۊJBYȝ\ݗܚٜXך[טYٛݜלٙڜݜފٛʎٛ˘\ܙ\ݒ[ʈܚٜXȋי\ڋБѓՔʂȈٛ˘\ܙ\ݒ[ʈܚٜXȋי\ڋԖTՑSWԔӓTʂȈٛ˘\ܙ\ݒ[ʈѐSыPՕPӓԒTՑSՈˈי\ڋԒєPה֔ՑSJBYȝ\ݗؘYؙٛݗܝ[ܙYݜٙ
ٛʎڝ[\ܘ\ޑ\٘ݛܞJ
H\ȝ\ڝٛ˘\ܙ\ݔؚ\ٜʕ؛YQ\ܛ܊Nי\ڋܝ[ʈٙ[[ȋșژؙ\ڜڈ׋șYوΈوߋԒQQˈK̋Ȉ]
\
HȈۙ]ٜȊB؛\܈X[Ԝۛ\ؚ[XU\ݜʝ[ڝ\݋ՙ\ݐ؜يNȈԝ[ȍ̍͌̎LˌH
̌͋LLKLˈڛȘ\ۊNșYو[وڙ\XȜܙ[Z\ٜٚX݈ԓӈؚ[XH[ȝHޜݙ[Hۛ\țX[ɜȜۛ\ۛHؚYܘ[YH\[ݜȘۛXYݙHYوȸ%[وX[ɜț]وٜH[ٙYڝHؙٛYԓӂȈؚ݈٘]Yۈݙ\ٚX݈ȚٞKȕHؚ[XH\ț۝ț]\؛[Ș[ٙKȈȂYȝ\ݗ؛ݚٙWܜۛ\לܙ[ݚWܘڙ[XJٛʎۜț؛YKۛ\[Ȟי\ڋԖTՑSWԔӓT˚][\ʊNٛ˘\ܙ\ݒ[ʉȝٜٚX݈ɋۛ\؛YJBȈٛ˘\ܙ\ݒ[ʉșڛٚ[ٜȉˈۛ\؛YJBȈٛ˘\ܙ\ݒ[ʉȘۛٚY[ؙHɋۛ\؛YJB؛\܈ٜٚXݑ^ؘݚ[۔ٜZ\ՙ\ݜʝ[ڝ\݋ՙ\ݐ؜يNȈіАՒSӈєRTȊݛȍ̍͌̎LˌJNȜݜڛًX]؜و؛[ؙY[ؚ݂٘Ȉؘ[ΈHTՈ\ܙXXۙHؚ݈٘ڝHݜڛو	ݙ\ٚX݉ȝڛ܋ȑؙٛYԓӂȈ[وۜوݜݚ]َțۋ]ٜٚX݈ژ\\Ȝݘ^Hۙ\ݛHSԐTԑPPӑKȈȂYȝ\ݗٙ[ؙYݙ\ٚXݗܘ\ܙY
ٛʎ^H
	Л؛\ڜȚ\ًככؘܛۗɂȈ	ވݙ\ٚX݈ΈҔԕQTבӕSшˈٚ[ٚ[ٜȎȖވښ[وΈؘܛ۝]\ȋ		Ȝ][ݙHΈ؛ڝوˈܜۘۙ[HΈэH۝][\Yˈ		Ȝݙٙ\ݙYٚ^ΈٛݜțوڝوߗK؛ۙڙ[ؙHΈښYڈߗؘ	ʂȈȏHי\ڋܘ\ܙWݙ\ٚX݊^
BȈٛ˘\ܙ\ݑ\]X[
ֈݙ\ٚX݈׋ҔԕQTבӕSшʂȈٛ˘\ܙ\ݑ\]X[
ֈ؛ۙڙ[ؙH׋ښYڈʂȈٛ˘\ܙ\ݑ\]X[
ֈٚ[ٚ[ٜȗV̗VȚڛو׋ؘܛ۝]\ȊBYȝ\ݗܜۜٗݚ]؜ؘٜם[יڛ؛ݙ\ٚX݊ٛʎ^H
	ә]ژ܈؞HȜ[ۙYȍHH[ȜۜوܘXٜ˗כɂȈ	њ[؛ڙXڎכވݙ\ٚX݈ΈГPSȋٚ[ٚ[ٜȎȖ׋؛ۙڙ[ؙHΈۙY][H߉ʂȈȏHי\ڋܘ\ܙWݙ\ٚX݊^
BȈٛ˘\ܙ\ݑ\]X[
ֈݙ\ٚX݈׋ГPSȊBȈٛ˘\ܙ\ݑ\]X[
ֈ؛ۙڙ[ؙH׋ۙY][HʂYȝ\ݗۘ\ݗݙ\ٚXݗۘڙXݗݚ[܊ٛʎ^H
	ވݙ\ٚX݈ΈђTԕˈٚ[ٚ[ٜȎȖןHZYH		ވݙ\ٚX݈ΈԑPӓшˈٚ[ٚ[ٜȎȖ׋؛ۙڙ[ؙHΈ݈ۛ߉ʂȈȏHי\ڋܘ\ܙWݙ\ٚX݊^
BȈٛ˘\ܙ\ݑ\]X[
ֈݙ\ٚX݈׋ԑPӓшʂYȝ\ݗ؜ؘٜך[ܚYWܝڛٜיכ۝؛ۙݜٗݚWܘ؛ʜٛʎ^H
	ވݙ\ٚX݈ΈҔԕQTבӕSшˈٚ[ٚ[ٜȎȖވښ[وΈ۝\ȋ		Ȝ][ݙHΈݚHٝ͟H؜ȝܛۙȋܜۘۙ[HΈ؜ؘو[Ȝݜڛوˈ		Ȝݙٙ\ݙYٚ^ΈۛۙHߗK؛ۙڙ[ؙHΈ݈ۛ߉ʂȈȏHי\ڋܘ\ܙWݙ\ٚX݊^
BȈٛ˘\ܙ\ݑ\]X[
ֈݙ\ٚX݈׋ҔԕQTבӕSшʂȈٛ˘\ܙ\ݑ\]X[
ֈٚ[ٚ[ٜȗV̗VȜ][ݙH׋ݚHٝ͟H؜ȝܛۙȊBYȝ\ݗۘڙXݗݚ]ݝݙ\ٚXݗڙ^Wܝ[ݛܘ\ܙXXۙJٛʎȜݛȍ̍͌̎LˌHX[ț[وژ\NșؙٛYԓӋۘZ[HݜڛٜȘ\Țٞ\˂Ȉ^H
	ؘܛۗވЛڝوXؙ\YΈГӕБPՑQˈ		Ȟٜۈٝڙ\ȎȈГӔБPՑQˈܛ[ۙYܛݜȎȍ_Wؘ	ʂȈȏHי\ڋܘ\ܙWݙ\ٚX݊^
BȈٛ˘\ܙ\ݑ\]X[
ֈݙ\ٚX݈׋ՓԐTԑPPӑHʂȈٛ˘\ܙ\ݑ\]X[
ֈٚ[ٚ[ٜȗK׊BȈٛ˘\ܙ\ݒ\ӛۙJֈ؛ۙڙ[ؙH׊BYȗכ؛YW׈OHחۘZ[חȎ[ڝ\݋ۘZ[ʊB