import unittest

from e2r.census.census_backfill_plan import build_deep_backfill_plan


class CensusBackfillPlanTests(unittest.TestCase):
    def test_provider_pending_is_not_stage2plus_candidate(self):
        plan = build_deep_backfill_plan(
            [
                {
                    "symbol": "005930",
                    "base_stage": "Unknown",
                    "census_status": "PENDING_PROVIDER",
                    "provider_gaps": ["official_baseline_connector_unwired"],
                },
                {
                    "symbol": "000660",
                    "base_stage": "Stage2-Actionable",
                    "census_status": "DEEP_VERIFIED",
                    "source_gaps": [],
                },
            ],
            shard_count=10,
        )
        self.assertEqual(plan["pending_symbol_list"], ["005930"])
        self.assertEqual(plan["Stage2plus_candidate_list"], ["000660"])
        self.assertEqual(plan["expected_llm_calls"], 1)
        self.assertEqual(plan["expected_provider_calls"], 4)


if __name__ == "__main__":
    unittest.main()
