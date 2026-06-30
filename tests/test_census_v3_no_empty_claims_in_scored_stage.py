import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3NoEmptyClaimsInScoredStageTests(unittest.TestCase):
    def test_scored_stage_rows_have_claim_score_and_stagecourt_ids(self):
        for row in census_v3_artifacts()["stage_rows"]:
            if row.get("verified_score") is not None:
                self.assertTrue(row["accepted_claim_ids"])
                self.assertTrue(row["score_contribution_ids"])
                self.assertTrue(row["stagecourt_trace_id"])


if __name__ == "__main__":
    unittest.main()
