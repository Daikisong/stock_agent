import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class ProductionPlannerPromptResponseHashTests(unittest.TestCase):
    def test_prompt_and_response_hash_counts_are_recorded(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        summary = bundle["planner_provider_report"]["summary"]
        self.assertEqual(summary["planner_response_missing_hash_count"], 0)
        self.assertEqual(summary["planner_prompt_hash_count"], summary["planner_run_count"])


if __name__ == "__main__":
    unittest.main()
