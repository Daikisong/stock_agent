import unittest

from e2r.production.cutover_v2 import _stage_distribution_report_v2


class CutoverV2MeaningfulStageSplitTests(unittest.TestCase):
    def test_stage_split_reports_provider_pending_and_reject_slice(self):
        report = _stage_distribution_report_v2(
            base={
                "output_artifacts": {"daily_watchlist": {"rows": []}},
                "operator_digest": {"rows": [{"section": "Stage2-Watch"}]},
                "score_meaning_audit": {"summary": {"deterministic_scorer_output_count": 50, "stagecourt_trace_count": 50, "score_without_claim_count": 0}},
            },
            provider_matrix={"rows": [{"blocking_cutover": True}]},
        )
        self.assertEqual(report["summary"]["status"], "MEANINGFUL_STAGE_SPLIT_PASS")
        self.assertGreaterEqual(report["summary"]["ProviderPending_count"], 1)
        self.assertGreaterEqual(report["summary"]["Reject_Red_count"], 1)


if __name__ == "__main__":
    unittest.main()
