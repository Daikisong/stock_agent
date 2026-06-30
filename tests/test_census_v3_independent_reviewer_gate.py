import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3IndependentReviewerGateTests(unittest.TestCase):
    def test_all_reviewers_pass_with_zero_critical_count(self):
        for key in ("reviewer_a", "reviewer_b", "reviewer_c"):
            reviewer = census_v3_artifacts()[key]
            self.assertEqual(reviewer["verdict"], "PASS")
            self.assertEqual(reviewer["critical_count"], 0)


if __name__ == "__main__":
    unittest.main()
