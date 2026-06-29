import unittest

from e2r.research_brain.v4_production_orchestrator import run_multi_day_shadow_v4
from e2r.research_brain.v4_schemas import ProductionShadowV4Config
from research_brain_v4_test_helpers import RealStubPlannerProviderV4, load_v4_matrix


class ResearchBrainV4MultiDayShadowTests(unittest.TestCase):
    def test_five_day_shadow_uses_real_provider_and_no_fake_provider(self):
        multi = run_multi_day_shadow_v4(
            base_config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="frozen_real_source_snapshot",
                universe_limit=3,
                planner_success_limit=3,
            ),
            v1_archetype_matrix=load_v4_matrix(),
            planner_provider_factory=RealStubPlannerProviderV4,
        )
        summary = multi["summary"]
        self.assertEqual(summary["five_day_run_count"], 5)
        self.assertGreaterEqual(summary["real_provider_success_count_total"], 15)
        self.assertEqual(summary["repeat_run_count"], 3)
        self.assertEqual(summary["fake_provider_used_total"], 0)
        self.assertEqual(summary["repeated_frozen_run_variance"], 0)
        self.assertEqual(len(multi["repeat_rows"]), 3)
        self.assertEqual({row["repeat_mode"] for row in multi["repeat_rows"]}, {"frozen_real_planner_snapshot"})
        self.assertEqual(len({row["watchlist_signature"] for row in multi["repeat_rows"]}), 1)


if __name__ == "__main__":
    unittest.main()
