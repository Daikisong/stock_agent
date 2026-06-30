import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3LastEffectiveThesisCompleteTests(unittest.TestCase):
    def test_last_effective_thesis_count_equals_stage_rows(self):
        artifacts = census_v3_artifacts()
        self.assertEqual(len(artifacts["thesis_states"]), len(artifacts["stage_rows"]))


if __name__ == "__main__":
    unittest.main()
