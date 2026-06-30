import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3RepairCannotLoosenThresholdsTests(unittest.TestCase):
    def test_hard_gate_thresholds_still_visible_in_audit(self):
        critical = census_v3_artifacts()["leaf_audit"]["critical_counts"]
        self.assertIn("single_stage_bucket_count", critical)
        self.assertIn("accepted_claim_total_zero_count", critical)


if __name__ == "__main__":
    unittest.main()
