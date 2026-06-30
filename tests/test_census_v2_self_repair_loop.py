import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2SelfRepairLoopTests(unittest.TestCase):
    def test_self_repair_records_v1_failure_and_resolution(self):
        log = census_v2_artifacts()["self_repair"]
        iteration = log["iterations"][0]
        self.assertEqual(iteration["detected_failure"], "CENSUS_V1_ALL_PROVIDER_PENDING_OR_EMPTY_BASELINE")
        self.assertTrue(iteration["resolved"])
        self.assertIn("baseline input collector", " ".join(iteration["patch_summary"]))


if __name__ == "__main__":
    unittest.main()
