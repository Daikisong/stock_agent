import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2NoClaimNoScoreTests(unittest.TestCase):
    def test_nonzero_verified_score_requires_accepted_claim(self):
        for row in census_v2_artifacts()["stage_rows"]:
            if row.get("verified_score") is not None:
                self.assertGreater(row["accepted_claim_count"], 0)
                self.assertGreater(row["score_contribution_count"], 0)

    def test_score_contributions_have_support_claims(self):
        for row in census_v2_artifacts()["score_contributions"]:
            self.assertTrue(row.get("support_claim_ids"))


if __name__ == "__main__":
    unittest.main()
