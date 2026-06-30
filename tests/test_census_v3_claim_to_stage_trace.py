import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3ClaimToStageTraceTests(unittest.TestCase):
    def test_every_stage_row_has_trace_contract(self):
        artifacts = census_v3_artifacts()
        traces = {row["symbol"]: row for row in artifacts["trace_rows"]}
        self.assertEqual(len(traces), len(artifacts["stage_rows"]))
        for row in artifacts["stage_rows"]:
            self.assertIn(row["symbol"], traces)
            self.assertEqual(row["claim_to_stage_trace_id"], traces[row["symbol"]]["trace_id"])


if __name__ == "__main__":
    unittest.main()
