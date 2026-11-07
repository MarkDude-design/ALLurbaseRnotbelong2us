"""Offline guard tests: no injected ontology, no persona, independent model sessions."""
import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("ontology", ROOT / "scripts/island_ontology_interview.py")
ontology = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ontology)

class OntologyInterviewTests(unittest.TestCase):
    def test_first_contact_is_single_unframed_user_prompt(self):
        m = ontology.messages_for_round([], ontology.OPENING)
        self.assertEqual(m, [{"role":"user","content":ontology.OPENING}])
        self.assertNotIn("notebook", ontology.OPENING.lower())
        self.assertNotIn("island", ontology.OPENING.lower())
        self.assertNotIn("note", ontology.OPENING.lower())
        self.assertNotIn("paper", ontology.OPENING.lower())

    def test_followups_use_the_models_actual_prior_words(self):
        h = [{"role":"user","content":ontology.OPENING},
             {"role":"assistant","content":"I would ask about confidence and evidence."}]
        m = ontology.messages_for_round(h, ontology.FOLLOWUPS[0])
        self.assertEqual(m[:2],h)
        self.assertEqual(m[-1]["role"],"user")
        self.assertEqual(len(m),3)
        self.assertNotIn("notebook", ontology.FOLLOWUPS[0].lower())
        self.assertNotIn("paper", ontology.FOLLOWUPS[1].lower())

    def test_rejects_hidden_system_or_persona_seed(self):
        with self.assertRaises(ValueError):
            ontology.messages_for_round([{"role":"system","content":"You are a skeptic"}], ontology.OPENING)
        with self.assertRaises(ValueError):
            ontology.messages_for_round([{"role":"developer","content":"You are on an island"}], ontology.OPENING)

    def test_catalog_honors_free_pricing_and_rate_limited_exclusion(self):
        def model(mid, price="0"):
            return {"id":mid,"pricing":{"prompt":price,"completion":"0"},
                    "architecture":{"input_modalities":["text"],"output_modalities":["text"]}}
        catalog = {"data":[
            model("liquid/lfm-2.5-2.6b:free"),
            model("liquid/lfm-3-1.7b:free"),
            model("google/gemma-4-26b-a4b-it:free"),
            model("paid/model", price=".01")
        ]}
        selected = ontology.choose_interview_models(
            catalog,2,excluded=[ontology.KNOWN_UPSTREAM_429])
        self.assertEqual([m["id"] for m in selected],
                         ["liquid/lfm-3-1.7b:free","google/gemma-4-26b-a4b-it:free"])

    def test_usage_is_whitelisted_for_public_receipt(self):
        usage={"prompt_tokens":19,"completion_tokens":20,"cost":0,
               "completion_tokens_details":{"reasoning_tokens":15,"user_id":"NOPE"},
               "user_id":"PRIVATE_METADATA","internal_request":"NOPE"}
        clean=ontology.clean_usage(usage)
        self.assertEqual(clean["reasoning_tokens"],15)
        self.assertNotIn("PRIVATE_METADATA",json.dumps(clean))
        self.assertNotIn("NOPE",json.dumps(clean))

    def test_three_rounds_only_and_no_future_artifact_leak(self):
        self.assertEqual(len(ontology.PROMPTS),3)
        terms = " ".join(ontology.PROMPTS).lower()
        for taboo in ("island","notebook","piece of paper","permission slip"):
            self.assertNotIn(taboo,terms)

if __name__=="__main__":
    unittest.main()
