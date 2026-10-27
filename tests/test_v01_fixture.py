"""GATE 1 fixture acceptance tests (SPEC v0.1.2 §6.1) — stdlib unittest only.

Run: python3 -m unittest tests.test_v01_fixture -v
or:  python3 -m unittest discover -s tests -p "test_v01_fixture.py"

Every §6.1 checklist item is asserted positive, plus anti-masquerade
negative tests for the strict manifest validator (SPEC §3).
"""

import json
import tempfile
import unittest
from pathlib import Path

from island.v01 import fixture as fixture_mod
from island.v01.fixture import run_fixture
from island.v01.hashes import sha256_hex_of_bytes
from island.v01.manifest import TEMPLATE, validate_manifest
from island.v01.scheduler import make_schedule

REPORT = None


def _report():
    global REPORT
    if REPORT is None:
        REPORT = run_fixture()
    return REPORT


def _valid_manifest():
    return json.loads(json.dumps(_report()["manifests"]["baseline"]))


class PositiveChecklist(unittest.TestCase):
    """The §6.1 acceptance checklist — every item must pass."""

    @classmethod
    def setUpClass(cls):
        cls.report = _report()

    def test_1_paired_scheduler_proof(self):
        c = self.report["checklist"]["paired_scheduler"]
        self.assertTrue(c["pass"], c)
        fp = self.report["force_plan"]
        s1 = make_schedule(self.report["world_seed"], self.report["turns"], exclude=fp.keys())
        s2 = make_schedule(self.report["world_seed"], self.report["turns"], exclude=fp.keys())
        self.assertEqual(s1, s2)  # regenerates deterministically from the seed alone

    def test_2_baseline_shadow_events(self):
        c = self.report["checklist"]["baseline_shadow"]
        self.assertTrue(c["pass"], c)
        m = self.report["manifests"]["baseline"]
        self.assertEqual(m["actuals"]["results"]["bert_deliveries"], 0)
        self.assertEqual(m["actuals"]["results"]["bert_opportunities"],
                         len(m["run_config"]["bert_fixed_points"]))

    def test_3_perturbed_delivery_bytes(self):
        c = self.report["checklist"]["perturbed_delivery"]
        self.assertTrue(c["pass"], c)
        m = self.report["manifests"]["perturbed"]
        self.assertEqual(m["actuals"]["results"]["bert_deliveries"],
                         len(m["run_config"]["bert_fixed_points"]))

    def test_4_fallback_exercised(self):
        c = self.report["checklist"]["fallback_exercised"]
        self.assertTrue(c["pass"], c)
        self.assertGreaterEqual(c["evidence"]["baseline_fallbacks"], 1)
        self.assertGreaterEqual(c["evidence"]["perturbed_fallbacks"], 1)

    def test_5_terminal_failure_slot_counting(self):
        c = self.report["checklist"]["terminal_failure"]
        self.assertTrue(c["pass"], c)
        for arm in ("baseline", "perturbed"):
            m = self.report["manifests"][arm]["actuals"]
            ev = c["evidence"][arm]
            self.assertEqual(len(ev["terminal_slots"]), 1)
            # Exhausted slot receipted as attempted/completed, excluded from accepted.
            self.assertEqual(m["turns_attempted"], m["turns_requested"])
            self.assertEqual(m["turns_requested"], m["turns_completed"])
            self.assertEqual(m["turns_accepted"], m["turns_attempted"] - 1)

    def test_6_notebook_isolation(self):
        c = self.report["checklist"]["notebook_isolation"]
        self.assertTrue(c["pass"], c)
        self.assertFalse(c["evidence"]["shadow_shas_in_baseline_notebook"])

    def test_7_manifests_validate_green(self):
        c = self.report["checklist"]["manifests_valid"]
        self.assertTrue(c["pass"], c)
        self.assertEqual(c["evidence"], {"baseline_errors": [], "perturbed_errors": []})

    def test_8_hashes_reproducible(self):
        c = self.report["checklist"]["hashes_reproducible"]
        self.assertTrue(c["pass"], c)
        for arm in ("baseline", "perturbed"):
            self.assertEqual(c["evidence"][arm]["first"], c["evidence"][arm]["rerun"])

    def test_all_pass_and_honest_fields(self):
        self.assertTrue(self.report["all_pass"])
        for arm in ("baseline", "perturbed"):
            m = self.report["manifests"][arm]
            self.assertEqual(m["status"], "completed")
            self.assertEqual(m["actors"][0]["fill"], "code")
            self.assertEqual(m["actors"][1]["fill"], "code")
            # Honest nulls: unmeasured things stay null, never zeros.
            self.assertIsNone(m["cost"]["known_subtotal_usd"])
            self.assertIsNone(m["cost"]["tokens"])
            self.assertEqual(m["cost"]["unknown_charge_attempts"], 0)  # the ONE sanctioned zero (measured count)
            self.assertIsNone(m["actuals"]["results"]["landmark_visits"])
            self.assertIsNone(m["artifacts"]["bus_jsonl_sha"])
            self.assertTrue(m["actuals"]["run_id"].startswith("v01-fixture-"))


class ArtifactsAndCLI(unittest.TestCase):

    def test_outdir_artifacts_written(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "fx"
            rep = run_fixture(outdir=str(out))
            self.assertTrue(rep["all_pass"])
            for name in ("events.baseline.jsonl", "events.perturbed.jsonl",
                         "notebook.baseline.txt", "notebook.perturbed.txt",
                         "run-manifest.baseline.json", "run-manifest.perturbed.json",
                         "FIXTURE_REPORT.json"):
                self.assertTrue((out / name).exists(), name)
            log_bytes = (out / "events.baseline.jsonl").read_bytes()
            self.assertEqual(
                rep["manifests"]["baseline"]["actuals"]["actual_event_log_sha"],
                sha256_hex_of_bytes(log_bytes),
            )

    def test_cli_exit_code_zero(self):
        with tempfile.TemporaryDirectory() as td:
            rc = fixture_mod.main(["--outdir", str(Path(td) / "cli")])
        self.assertEqual(rc, 0)


class ValidatorAntiMasquerade(unittest.TestCase):
    """SPEC §3: template-vs-instantiated discipline — negatives must be rejected."""

    def test_rejects_unexplained_zero(self):
        m = _valid_manifest()
        m["cost"]["known_subtotal_usd"] = 0  # zero where template says null
        errs = validate_manifest(m)
        self.assertTrue(any("unexplained zero" in e for e in errs), errs)

    def test_rejects_empty_string(self):
        m = _valid_manifest()
        m["actuals"]["run_id"] = ""
        errs = validate_manifest(m)
        self.assertTrue(any("empty string" in e for e in errs), errs)

    def test_rejects_placeholder_template(self):
        m = _valid_manifest()
        m["pair_id"] = "<uuid>"
        errs = validate_manifest(m)
        self.assertTrue(any("un-instantiated template placeholder" in e for e in errs), errs)

    def test_rejects_paper_masquerade(self):
        m = _valid_manifest()
        m["status"] = "paper-illustration"  # keeps real-run actuals — masquerade
        errs = validate_manifest(m)
        self.assertTrue(any("paper-illustration manifest" in e for e in errs), errs)

    def test_rejects_model_fill_without_provenance(self):
        m = _valid_manifest()
        m["actors"][0]["fill"] = "model"  # but no model_id/provider/requested/returned
        errs = validate_manifest(m)
        self.assertTrue(any("required when fill=model" in e for e in errs), errs)

    def test_rejects_code_fill_with_model_fields(self):
        m = _valid_manifest()
        m["actors"][0]["model_id"] = "gpt-fake"
        errs = validate_manifest(m)
        self.assertTrue(any("set on a code fill" in e for e in errs), errs)

    def test_rejects_bad_delivery_order(self):
        m = _valid_manifest()
        m["run_config"]["delivery_order"] = "after-action"  # violates FROZEN §2
        errs = validate_manifest(m)
        self.assertTrue(any("delivery_order" in e for e in errs), errs)

    def test_rejects_schema_drift(self):
        m = _valid_manifest()
        m["schema_version"] = "0.9.9"
        errs = validate_manifest(m)
        self.assertTrue(any("schema_version" in e for e in errs), errs)

    def test_rejects_missing_key(self):
        m = _valid_manifest()
        del m["artifacts"]
        errs = validate_manifest(m)
        self.assertTrue(any("missing key" in e for e in errs), errs)

    def test_template_is_not_a_valid_instance(self):
        # The template keeps explicit nulls (never measured-looking defaults),
        # and is itself rejected as an instantiated manifest.
        self.assertIsNone(TEMPLATE["cost"]["known_subtotal_usd"])
        self.assertIsNone(TEMPLATE["actuals"]["turns_attempted"])
        self.assertEqual(TEMPLATE["cost"]["unknown_charge_attempts"], 0)  # measured count
        self.assertTrue(validate_manifest(TEMPLATE))


if __name__ == "__main__":
    unittest.main()
