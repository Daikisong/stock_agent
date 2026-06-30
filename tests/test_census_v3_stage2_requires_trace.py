import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3Stage2RequiresTraceTests(unittest.TestCase):
    def test_stage2_or_red_rows_have_stagecourt_trace(self):
        checked = 0
        for row in census_v3_artifacts()["stage_rows"]:
            if row["base_stage"] in {"Stage2-Watch", "Stage2-Actionable", "Stage3-Yellow", "Stage3-Green", "Red", "Reject"}:
                checked += 1
                self.assertTrue(row["stagecourt_trace_id"])
        self.assertGreater(checked, 0)


if __name__ == "__main__":
    unittest.main()
