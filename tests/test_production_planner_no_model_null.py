import unittest

from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class ProductionPlannerNoModelNullTests(unittest.TestCase):
    def test_model_null_blocks_ready_instead_of_being_ignored(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        self.assertGreaterEqual(bundle["planner_provider_report"]["summary"]["planner_provider_model_null_count"], 0)
        self.assertFalse(bundle["shadow_latest"]["production_ready"])


if __name__ == "__main__":
    unittest.main()
