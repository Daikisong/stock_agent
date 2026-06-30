import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3NoBlindStageCopyTests(unittest.TestCase):
    def test_scored_stage_rows_have_stagecourt_trace_not_previous_stage_only(self):
        for row in census_v3_artifacts()["stage_rows"]:
            if row.get("verified_score") is not None:
                self.assertTrue(row["stagecourt_trace_id"])


if __name__ == "__main__":
    unittest.main()
