import unittest

from e2r.census.census_audit import audit_census_mode


class CensusV2SourcePendingNotRedTests(unittest.TestCase):
    def test_source_pending_red_is_critical(self):
        audit = audit_census_mode(
            eligible_symbols=["005930"],
            stage_status_rows=[
                {
                    "symbol": "005930",
                    "census_status": "PENDING_SOURCE",
                    "base_stage": "Red",
                    "score_valid_status": "NOT_SCORED",
                    "stage_confidence": "INSUFFICIENT_EVIDENCE",
                }
            ],
            report_line_counts=(10,),
        )
        self.assertGreater(audit["critical_counts"]["source_pending_marked_red_count"], 0)


if __name__ == "__main__":
    unittest.main()
