import unittest

from e2r.research_brain.v4_production_orchestrator import run_research_brain_v4_production_shadow
from e2r.research_brain.v4_schemas import ProductionShadowV4Config
from research_brain_v4_test_helpers import RealStubPlannerProviderV4, load_v4_matrix


class ResearchBrainV4DailyWatchlistTests(unittest.TestCase):
    def test_verified_score_requires_claim_contribution_and_stagecourt(self):
        result = run_research_brain_v4_production_shadow(
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="real",
                source_acquisition="frozen_real_source_snapshot",
                universe_limit=6,
                planner_success_limit=6,
            ),
            v1_archetype_matrix=load_v4_matrix(),
            planner_provider=RealStubPlannerProviderV4(),
        )
        summary = result["watchlist_report"]["summary"]
        self.assertEqual(summary["fake_provider_output_count"], 0)
        self.assertGreaterEqual(summary["deterministic_scorer_output_count"], 1)
        for row in result["watchlist_report"]["rows"]:
            if row["verified_score"] is None:
                continue
            self.assertTrue(row["accepted_claim_ids"])
            self.assertTrue(row["score_contribution_ids"])
            self.assertTrue(row["stage_court_trace"])


if __name__ == "__main__":
    unittest.main()
