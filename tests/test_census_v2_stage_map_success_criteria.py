import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2StageMapSuccessCriteriaTests(unittest.TestCase):
    def test_stage_map_has_meaningful_buckets_and_real_score_evidence(self):
        artifacts = census_v2_artifacts()
        metrics = artifacts["audit"]["v2_metrics"]
        self.assertLessEqual(metrics["unknown_rate"], 0.05)
        self.assertLess(metrics["provider_pending_rate"], 0.30)
        self.assertGreaterEqual(metrics["status_bucket_count"], 4)
        self.assertGreaterEqual(metrics["base_stage_bucket_count"], 3)
        self.assertGreater(metrics["accepted_claim_total"], 0)
        self.assertGreater(metrics["score_contribution_total"], 0)
        self.assertGreater(metrics["source_task_count"], 0)


if __name__ == "__main__":
    unittest.main()
