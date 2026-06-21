from datetime import date
import unittest

from e2r.red_team import RedTeamEngine, RedTeamRiskLevel, RedTeamSignals, Soft4BStatus


class RedTeamEngineTests(unittest.TestCase):
    def test_soft_4b_score_uses_weighted_factors(self):
        signals = RedTeamSignals(
            symbol="CASE",
            as_of_date=date(2026, 5, 13),
            soft_4b_factors={
                "return_since_stage3": 1.0,
                "return_12_24m": 1.0,
                "extreme_forward_valuation": 1.0,
                "revision_slowdown": 0.5,
                "market_crowding": 0.5,
            },
            evidence_ids_by_signal={
                "return_since_stage3": ("ev-price-runup",),
                "revision_slowdown": ("ev-revision-slowdown",),
            },
        )

        assessment = RedTeamEngine().assess(signals)

        self.assertEqual(assessment.soft_4b_score, 60.0)
        self.assertEqual(assessment.soft_4b_status, Soft4BStatus.WATCH)
        self.assertEqual(assessment.thesis_break_score, 0.0)
        self.assertEqual(assessment.risk_level, RedTeamRiskLevel.LOW)
        self.assertFalse(assessment.has_hard_break)
        self.assertIn("ev-price-runup", assessment.evidence_ids)
        self.assertIn("ev-revision-slowdown", assessment.evidence_ids)

    def test_soft_4b_status_splits_watch_elevated_and_graduated(self):
        engine = RedTeamEngine()

        watch = engine.assess(
            RedTeamSignals(
                symbol="CASE",
                as_of_date=date(2026, 5, 13),
                soft_4b_factors={"return_since_stage3": 1.0, "return_12_24m": 1.0, "extreme_forward_valuation": 1.0, "revision_slowdown": 0.75},
            )
        )
        elevated = engine.assess(
            RedTeamSignals(
                symbol="CASE",
                as_of_date=date(2026, 5, 13),
                soft_4b_factors={"return_since_stage3": 1.0, "return_12_24m": 1.0, "extreme_forward_valuation": 1.0, "revision_slowdown": 1.0, "market_crowding": 0.5},
            )
        )
        graduated = engine.assess(
            RedTeamSignals(
                symbol="CASE",
                as_of_date=date(2026, 5, 13),
                soft_4b_factors={"return_since_stage3": 1.0, "return_12_24m": 1.0, "extreme_forward_valuation": 1.0, "revision_slowdown": 1.0, "backlog_contract_slowdown": 1.0},
            )
        )

        self.assertEqual(watch.soft_4b_status, Soft4BStatus.WATCH)
        self.assertEqual(elevated.soft_4b_status, Soft4BStatus.ELEVATED)
        self.assertEqual(graduated.soft_4b_status, Soft4BStatus.GRADUATED)

    def test_thesis_break_factors_create_findings(self):
        signals = RedTeamSignals(
            symbol="CASE",
            as_of_date=date(2026, 5, 13),
            thesis_break_factors={
                "eps_fcf_revision_down": 1.0,
                "backlog_or_rpo_decline": 1.0,
                "opm_decline": 1.0,
            },
            evidence_ids_by_signal={
                "eps_fcf_revision_down": ("ev-eps-down",),
                "backlog_or_rpo_decline": ("ev-backlog-down",),
            },
        )

        assessment = RedTeamEngine().assess(signals)

        self.assertEqual(assessment.thesis_break_score, 45.0)
        self.assertEqual(assessment.risk_level, RedTeamRiskLevel.HIGH)
        self.assertFalse(assessment.has_hard_break)
        self.assertEqual({finding.risk_type for finding in assessment.findings}, {
            "eps_fcf_revision_down",
            "backlog_or_rpo_decline",
            "opm_decline",
        })
        self.assertIn("ev-eps-down", assessment.evidence_ids)

    def test_hard_break_signal_overrides_score_threshold(self):
        signals = RedTeamSignals(
            symbol="CASE",
            as_of_date=date(2026, 5, 13),
            thesis_break_factors={"accounting_or_trust_issue": 1.0},
            evidence_ids_by_signal={"accounting_or_trust_issue": ("ev-accounting",)},
        )

        assessment = RedTeamEngine().assess(signals)

        self.assertTrue(assessment.has_hard_break)
        self.assertEqual(assessment.risk_level, RedTeamRiskLevel.HARD_BREAK)
        self.assertTrue(assessment.findings[0].is_hard_break)

    def test_unknown_signal_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown thesis_break_factors"):
            RedTeamSignals(
                symbol="CASE",
                as_of_date=date(2026, 5, 13),
                thesis_break_factors={"not_a_rule": 1.0},
            )


if __name__ == "__main__":
    unittest.main()
