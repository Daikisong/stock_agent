import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3SourceTimelineCompleteTests(unittest.TestCase):
    def test_source_timeline_count_equals_stage_rows(self):
        artifacts = census_v3_artifacts()
        self.assertEqual(len(artifacts["timelines"]), len(artifacts["stage_rows"]))


if __name__ == "__main__":
    unittest.main()
