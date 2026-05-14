from datetime import date
import unittest

from e2r.backtest.stage_lifecycle_detector import StageLifecycleDetectionInput, StageLifecycleDetector
from e2r.models import Stage


class StageLifecycleDetectorTests(unittest.TestCase):
    def test_stage4a_when_stage3_evidence_remains_intact(self):
        result = StageLifecycleDetector().detect(
            StageLifecycleDetectionInput(
                symbol="267260",
                as_of_date=date(2024, 1, 1),
                previous_stage=Stage.STAGE_3_GREEN,
                stage3_evidence_intact=True,
                eps_fcf_visibility_strong=True,
                return_since_stage3=0.5,
            )
        )

        self.assertEqual(result.lifecycle_stage, Stage.STAGE_4A)
        self.assertEqual(result.status, "4A_ongoing")

    def test_price_only_4b_warning_is_not_full_4b(self):
        result = StageLifecycleDetector().detect(
            StageLifecycleDetectionInput(
                symbol="267260",
                as_of_date=date(2024, 1, 1),
                previous_stage=Stage.STAGE_3_GREEN,
                return_since_stage3=2.5,
                return_12m=1.8,
                blowoff_price_pattern=True,
            )
        )

        self.assertEqual(result.lifecycle_stage, Stage.STAGE_4A)
        self.assertEqual(result.status, "price_only_4b_watch")
        self.assertTrue(result.price_only_warning)
        self.assertFalse(result.evidence_based)

    def test_evidence_based_4b_requires_slowdown_or_crowding_evidence(self):
        result = StageLifecycleDetector().detect(
            StageLifecycleDetectionInput(
                symbol="267260",
                as_of_date=date(2024, 1, 1),
                previous_stage=Stage.STAGE_3_GREEN,
                return_since_stage3=2.5,
                valuation_rerating_score=95.0,
                revision_momentum_slowing=True,
            )
        )

        self.assertEqual(result.lifecycle_stage, Stage.STAGE_4B)
        self.assertFalse(result.price_only_warning)
        self.assertTrue(result.evidence_based)

    def test_hard_break_becomes_4c(self):
        result = StageLifecycleDetector().detect(
            StageLifecycleDetectionInput(
                symbol="SMCI",
                as_of_date=date(2024, 8, 1),
                previous_stage=Stage.STAGE_4B,
                hard_thesis_break=True,
                hard_break_reasons=("accounting_or_trust_issue",),
            )
        )

        self.assertEqual(result.lifecycle_stage, Stage.STAGE_4C)
        self.assertEqual(result.status, "hard_4c")

    def test_missing_evidence_reports_unknown(self):
        result = StageLifecycleDetector().detect(
            StageLifecycleDetectionInput(
                symbol="267260",
                as_of_date=date(2024, 1, 1),
                previous_stage=Stage.STAGE_3_GREEN,
                stage3_evidence_intact=False,
                eps_fcf_visibility_strong=False,
            )
        )

        self.assertEqual(result.status, "unknown_insufficient_evidence")
        self.assertFalse(result.evidence_based)


if __name__ == "__main__":
    unittest.main()
