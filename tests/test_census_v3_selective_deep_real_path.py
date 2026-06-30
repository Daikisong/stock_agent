import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3SelectiveDeepRealPathTests(unittest.TestCase):
    def test_selective_deep_counts_clear_minimums(self):
        metrics = census_v3_artifacts()["leaf_audit"]["metrics"]
        self.assertGreaterEqual(metrics["research_brain_plan_count"], 30)
        self.assertGreaterEqual(metrics["source_task_count"], 50)
        self.assertGreaterEqual(metrics["source_task_execution_count"], 30)
        self.assertGreaterEqual(metrics["accepted_claim_count"], 10)
        self.assertGreaterEqual(metrics["score_contribution_count"], 5)
        self.assertGreaterEqual(metrics["deterministic_stage_output_count"], 5)


if __name__ == "__main__":
    unittest.main()
