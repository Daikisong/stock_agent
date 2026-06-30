import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3DeepClaimsReachStageTests(unittest.TestCase):
    def test_at_least_five_stage_rows_include_claim_and_score_ids(self):
        rows = [row for row in census_v3_artifacts()["stage_rows"] if row.get("accepted_claim_ids") and row.get("score_contribution_ids")]
        self.assertGreaterEqual(len(rows), 5)


if __name__ == "__main__":
    unittest.main()
