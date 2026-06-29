import unittest

from e2r.research_brain.v4_production_orchestrator import run_research_brain_v4_production_shadow
from e2r.research_brain.v4_schemas import ProductionShadowV4Config
from research_brain_v4_test_helpers import load_v4_matrix


class ResearchBrainV4ProviderFailurePendingTests(unittest.TestCase):
    def test_no_planner_provider_leaves_items_pending_without_verified_score(self):
        result = run_research_brain_v4_production_shadow(
            config=ProductionShadowV4Config(
                as_of_date="2026-06-29",
                planner_provider="none",
                source_acquisition="frozen_real_source_snapshot",
                universe_limit=3,
                planner_success_limit=3,
            ),
            v1_archetype_matrix=load_v4_matrix(),
        )
        for row in result["watchlist_report"]["rows"]:
            self.assertEqual(row["score_valid_status"], "PROVIDER_FAILED")
            self.assertIsNone(row["verified_score"])
            self.assertFalse(row["accepted_claim_ids"])


if __name__ == "__main__":
    unittest.main()
