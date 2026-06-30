import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3ReportNotSourceOfTruthTests(unittest.TestCase):
    def test_acceptance_numbers_match_leaf_audit_not_report_memory(self):
        audit = census_v3_artifacts()["leaf_audit"]
        self.assertEqual(audit["critical_counts"]["report_leaf_mismatch_count"], 0)
        self.assertEqual(audit["metrics"]["accepted_claim_count"], len(census_v3_artifacts()["accepted_claims"]))


if __name__ == "__main__":
    unittest.main()
