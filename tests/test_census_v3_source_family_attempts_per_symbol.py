import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3SourceFamilyAttemptsPerSymbolTests(unittest.TestCase):
    def test_every_timeline_records_source_family_attempts(self):
        for timeline in census_v3_artifacts()["timelines"]:
            self.assertGreaterEqual(len(timeline["source_family_attempts"]), 5)


if __name__ == "__main__":
    unittest.main()
