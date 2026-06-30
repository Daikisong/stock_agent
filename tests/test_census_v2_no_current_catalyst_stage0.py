import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2NoCurrentCatalystStage0Tests(unittest.TestCase):
    def test_no_current_catalyst_is_stage0_not_red(self):
        rows = [
            row
            for row in census_v2_artifacts()["stage_rows"]
            if row["investigation_status"] == "NO_CURRENT_CATALYST"
        ]
        self.assertGreater(len(rows), 0)
        self.assertTrue(all(row["base_stage"] == "Stage0" for row in rows))
        self.assertTrue(all(row["verified_score"] is None for row in rows))


if __name__ == "__main__":
    unittest.main()
