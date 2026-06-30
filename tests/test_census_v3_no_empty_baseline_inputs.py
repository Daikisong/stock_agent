import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3NoEmptyBaselineInputsTests(unittest.TestCase):
    def test_empty_baseline_input_count_is_zero(self):
        self.assertEqual(census_v3_artifacts()["leaf_audit"]["critical_counts"].get("missing_leaf_artifact_count"), 0)
        self.assertGreater(census_v3_artifacts()["leaf_audit"]["metrics"]["baseline_scan_result_count"], 1000)


if __name__ == "__main__":
    unittest.main()
