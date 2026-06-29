import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class CutoverPlannerProviderIdentityTests(unittest.TestCase):
    def test_planner_report_counts_model_null_as_blocker_not_ready_claim(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        planner = bundle["planner_provider_report"]["summary"]
        self.assertGreaterEqual(planner["real_planner_success_count"], 0)
        self.assertIn("planner_provider_model_null_count", planner)
        self.assertFalse(bundle["shadow_latest"]["production_ready"])


if __name__ == "__main__":
    unittest.main()
