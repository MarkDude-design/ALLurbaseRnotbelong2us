"""Offline guard tests for the Island interview runner."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("interviews", ROOT / "scripts/island_model_interviews.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

class InterviewGuardTests(unittest.TestCase):
    def test_only_verified_free_text_models_are_selected(self):
        def m(identifier, prompt="0", completion="0", inputs=None, outputs=None):
            return {"id": identifier, "name": identifier,
                    "pricing": {"prompt": prompt, "completion": completion},
                    "architecture": {"input_modalities": inputs or ["text"],
                                     "output_modalities": outputs or ["text"]}}
        examples = {"data": [
            m("liquid/lfm3-1.7b:free"),
            m("foo/model:free", prompt="0.00001"),
            m("foo/model-paid"),
            m("foo/embedding:free"),
            m("foo/image:free", inputs=["image"], outputs=["image"]),
            m("google/gemma-4-31b-it:free"),
            m("foo/bad-price:free", completion=None),
        ]}
        result = runner.choose_models(examples, 12)
        self.assertEqual([x["id"] for x in result],
                         ["liquid/lfm3-1.7b:free", "google/gemma-4-31b-it:free"])
        self.assertEqual(runner.choose_models(examples, 1)[0]["id"],
                         "liquid/lfm3-1.7b:free")

    def test_frozen_panels(self):
        bank = json.loads((ROOT / "research/island-interviews/questionnaire-v1.json").read_text())
        self.assertEqual(sorted(bank["waves"]), ["1", "2", "3"])
        ids = []
        for wave in bank["waves"].values():
            self.assertEqual(len(wave), 8)
            ids.extend(q["id"] for q in wave)
            self.assertTrue(all(q["prompt"].strip() for q in wave))
        self.assertEqual(len(ids), len(set(ids)))

    def test_early_stop_on_two_empty_visible_replies(self):
        self.assertFalse(runner.should_stop_on_empty_output(0))
        self.assertFalse(runner.should_stop_on_empty_output(1))
        self.assertTrue(runner.should_stop_on_empty_output(2))
        self.assertTrue(runner.should_stop_on_empty_output(3))

    def test_provider_error_metadata_redacted(self):
        raw = json.dumps({"error":{"code":429,"metadata":{
            "provider_name":"Liquid", "limit_source":"upstream_provider_shared_pool",
            "provider_error_code":"model_rate_limit_exceeded",
            "retry_after_seconds":1,
            "user_id":"sensitive-account-identifier",
            "raw":"anything-private"}}}).encode()
        safe = runner.safe_http_error_excerpt(raw, 429)
        self.assertNotIn("sensitive-account-identifier", safe)
        self.assertNotIn("anything-private", safe)
        self.assertEqual(json.loads(safe)["http_status"],429)
        self.assertEqual(json.loads(safe)["limit_source"],"upstream_provider_shared_pool")

    def test_missing_usage_cost_is_not_zero(self):
        self.assertIsNone(runner.as_float(None))
        self.assertEqual(runner.as_float("0"), 0.0)
        self.assertEqual(runner.extract_text({"choices": [{"message": {"content": "NOTEBOOK"}}]}),
                         "NOTEBOOK")
        self.assertEqual(runner.extract_text({"choices": []}), "")

if __name__ == "__main__":
    unittest.main()
