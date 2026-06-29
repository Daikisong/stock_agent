import unittest

from e2r.research_brain.v4_schemas import ProductionShadowV4Config


class ResearchBrainV4OperationalModesTests(unittest.TestCase):
    def test_production_defaults_use_live_official_first_and_all_candidates_planned(self):
        config = ProductionShadowV4Config(as_of_date="2026-06-29")
        self.assertEqual(config.source_acquisition, "live_official_first")
        self.assertEqual(config.universe_limit, 30)
        self.assertEqual(config.planner_success_limit, 30)
        self.assertEqual(config.planner_batch_size, 5)

    def test_fake_provider_is_tests_only_unless_explicitly_allowed(self):
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="fake",
                source_acquisition="frozen_real_source_snapshot",
            ).validate()
        ProductionShadowV4Config(
            as_of_date="2026-06-29",
            planner_provider="fake",
            source_acquisition="frozen_real_source_snapshot",
            fake_provider_allowed=True,
        ).validate()

    def test_unbounded_top_results_and_retry_are_rejected(self):
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(as_of_date="2026-06-29", top_results=None).validate()  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            ProductionShadowV4Config(as_of_date="2026-06-29", retry_max=None).validate()  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
