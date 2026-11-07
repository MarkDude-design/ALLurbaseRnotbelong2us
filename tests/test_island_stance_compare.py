"""Offline, no-network guard tests for stance comparison."""
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("stance", ROOT / "scripts/island_stance_compare.py")
stance = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stance)

class StanceComparisonTests(unittest.TestCase):
    def test_3_by_3_by_4_complete_blocks(self):
        bank = json.loads((ROOT / "research/island-interviews/questionnaire-stance-v1.json").read_text())
        self.assertEqual([r["id"] for r in bank["roles"]], ["casual", "skeptic", "suspicious"])
        self.assertEqual(len(bank["scenarios"]), 4)
        self.assertEqual(len(set(q["id"] for q in bank["scenarios"])), 4)
        models = [{"id": f"test/m{i}:free"} for i in range(3)]
        plan = stance.plan_comparisons(models, bank["roles"], bank["scenarios"])
        self.assertEqual(len(plan), 36)
        self.assertEqual(len(set((m["id"], r["id"], q["id"]) for m,r,q in plan)), 36)
        for i,model in enumerate(models):
            self.assertTrue(all(item[0]["id"] == model["id"] for item in plan[i*12:(i+1)*12]))
        # 12-attempt smoke must hold underlying model constant and vary all three stances.
        self.assertEqual({r["id"] for m,r,q in plan[:12]}, {"casual","skeptic","suspicious"})
        self.assertEqual({q["id"] for m,r,q in plan[:12]}, {q["id"] for q in bank["scenarios"]})

    def test_shared_blank_output_guard(self):
        self.assertFalse(stance.should_stop_on_empty_output(1))
        self.assertTrue(stance.should_stop_on_empty_output(2))

    def test_free_tier_catalog_guard_reused(self):
        catalog={"data":[
            {"id":"liquid/lfm3-1.7b:free","pricing":{"prompt":"0","completion":"0"},
             "architecture":{"input_modalities":["text"],"output_modalities":["text"]}},
            {"id":"notfree/foo:free","pricing":{"prompt":"0.001","completion":"0"},
             "architecture":{"input_modalities":["text"],"output_modalities":["text"]}},
            {"id":"paid/something","pricing":{"prompt":"0","completion":"0"},
             "architecture":{"input_modalities":["text"],"output_modalities":["text"]}},
        ]}
        result=stance.choose_models(catalog, 3)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"],"liquid/lfm3-1.7b:free")

    def test_exact_scenario_evidence_shared_by_every_stance(self):
        bank=json.loads((ROOT / "research/island-interviews/questionnaire-stance-v1.json").read_text())
        for scenario in bank["scenarios"]:
            self.assertTrue(scenario["prompt"])
            self.assertTrue(scenario["expected"])
        self.assertNotIn("conspiracy",bank["roles"][0]["instruction"].lower())

if __name__ == "__main__":
    unittest.main()
