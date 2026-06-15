from datetime import date
import unittest
from unittest.mock import patch

from e2r.models import ScoreSnapshot
from e2r.red_team import RedTeamAssessment
from e2r.stage_gate_diagnostics import diagnose_stage_gates, promotion_band


class StageGateDiagnosticsTests(unittest.TestCase):
    def test_reports_failed_stage2_and_stage3_gates(self):
        score = ScoreSnapshot(
            symbol="267260",
            as_of_date=date(2023, 8, 1),
            eps_fcf_explosion_score=20,
            earnings_visibility_score=12,
            bottleneck_pricing_score=8,
            market_mispricing_score=10,
            valuation_rerating_score=9,
            capital_allocation_score=1,
            information_confidence_score=2,
            risk_penalty=0,
            total_score=62,
            diagnostic_scores={"score_valid": 100, "revision_score": 100, "contract_quality": 40, "one_off_shortage_risk": 0},
        )

        diag = diagnose_stage_gates(score, RedTeamAssessment.empty("267260", date(2023, 8, 1)))

        self.assertFalse(diag.stage2_gate_passed)
        self.assertFalse(diag.stage3_green_gate_passed)
        self.assertIn("failed_stage2_total_score", diag.failed_gate_names)
        self.assertIn("failed_stage3_bottleneck", diag.failed_gate_names)
        self.assertIn("failed_structural_visibility_quality", diag.failed_gate_names)
        self.assertEqual(diag.sector_profile, "GENERIC")
        self.assertEqual(diag.values_vs_thresholds["failed_stage3_revision"]["passed"], True)

    def test_reports_price_only_and_emerging_theme_guards_as_searchable_gates(self):
        score = ScoreSnapshot(
            symbol="005930",
            as_of_date=date(2026, 6, 8),
            eps_fcf_explosion_score=20,
            earnings_visibility_score=20,
            bottleneck_pricing_score=20,
            market_mispricing_score=15,
            valuation_rerating_score=15,
            capital_allocation_score=5,
            information_confidence_score=5,
            risk_penalty=0,
            total_score=95,
            diagnostic_scores={
                "revision_score": 90,
                "score_valid": 100,
                "structural_visibility_quality": 90,
                "contract_quality": 90,
                "price_only_blowoff_score": 80,
                "snippet_only_green_block": 100,
                "emerging_theme_active": 100,
                "llm_deep_research_completed": 0,
                "green_unlock_evidence_score": 0,
                "date_unverified_snippet_news_count_capped": 1,
                "report_date_confidence": 0,
            },
        )

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "calibrated"}):
            diag = diagnose_stage_gates(score, RedTeamAssessment.empty("005930", date(2026, 6, 8)))

        self.assertIn("failed_positive_stage_price_only_blowoff", diag.failed_gate_names)
        self.assertIn("failed_snippet_only_green_block", diag.failed_gate_names)
        self.assertIn("failed_emerging_theme_deep_research", diag.failed_gate_names)
        self.assertIn("failed_emerging_theme_green_unlock_evidence", diag.failed_gate_names)
        self.assertIn("failed_emerging_theme_date_verified_evidence", diag.failed_gate_names)
        self.assertFalse(diag.stage3_green_gate_passed)

    def test_invalid_score_is_reported_as_pending_not_stage1(self):
        score = ScoreSnapshot(
            symbol="005930",
            as_of_date=date(2026, 6, 12),
            eps_fcf_explosion_score=0,
            earnings_visibility_score=0,
            bottleneck_pricing_score=0,
            market_mispricing_score=0,
            valuation_rerating_score=0,
            capital_allocation_score=0,
            information_confidence_score=0,
            risk_penalty=0,
            total_score=0,
            diagnostic_scores={
                "score_valid": 0.0,
                "score_blocked_by_score_gap": 100.0,
                "raw_score_total_before_score_gap_block": 68.9,
            },
        )

        diag = diagnose_stage_gates(score, RedTeamAssessment.empty("005930", date(2026, 6, 12)))

        self.assertEqual(diag.failed_gate_names, ("failed_score_validity",))
        self.assertEqual(diag.promotion_band, "Score Pending")
        self.assertEqual(promotion_band(score), "Score Pending")


if __name__ == "__main__":
    unittest.main()
