import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3LifecycleRefreshRequiredTests(unittest.TestCase):
    def test_source_pending_rows_have_no_verified_score(self):
        for row in census_v3_artifacts()["stage_rows"]:
            if row["census_status"] == "PENDING_SOURCE":
                self.assertIsNone(row["verified_score"])


if __name__ == "__main__":
    unittest.main()
