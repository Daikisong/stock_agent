import unittest

from e2r.production.cutover_v3 import _stage_distribution_report_v3
from tests.cutover_v3_test_helpers import fake_a2, fake_provider_matrix, fake_v3_base


class CutoverV3StageSplitMultidayTests(unittest.TestCase):
    def test_stage_split_uses_live_rows_and_replay_guard_slices(self):
        bases = [fake_v3_base(f"2026-06-{day:02d}") for day in range(24, 29)]
        report = _stage_distribution_report_v3(
            base_bundles=bases,
            provider_matrix=fake_provider_matrix(),
            a2=fake_a2(),
            multiday={"summary": {"status": "MULTIDAY_SHADOW_PASS"}},
        )
        self.assertEqual(report["summary"]["status"], "MEANINGFUL_STAGE_SPLIT_PASS")
        self.assertEqual(report["summary"]["deterministic_scorer_output_count"], 100)
        self.assertGreaterEqual(report["summary"]["YellowPending_count"], 1)
        self.assertGreaterEqual(report["summary"]["RiskReview_or_Reject_count"], 1)


if __name__ == "__main__":
    unittest.main()
