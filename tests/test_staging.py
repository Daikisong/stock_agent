from datetime import date
import unittest
from unittest.mock import patch

from e2r.models import Stage
from e2r.red_team import RedTeamEngine, RedTeamSignals
from e2r.scoring import DeterministicScorer, ScoringPayload
from e2r.staging import StageClassificationInput, StageClassifier


def make_score(
    symbol="CASE",
    as_of_date=date(2026, 5, 13),
    diagnostic_scores=None,
    claim_backed_components=False,
    **components,
):
    defaults = {
        "eps_fcf_explosion": 12.0,
        "earnings_visibility": 13.0,
        "bottleneck_pricing": 12.0,
        "market_mispricing": 9.0,
        "valuation_rerating": 10.0,
        "capital_allocation": 4.0,
        "information_confidence": 5.0,
    }
    defaults.update(components)
    score_contribution_claim_ids = (
        {key: (f"CLM-{key}",) for key, value in defaults.items() if float(value) > 0.0}
        if claim_backed_components
        else {}
    )
    with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "calibrated"}):
        return DeterministicScorer().score(
            ScoringPayload(
                symbol=symbol,
                as_of_date=as_of_date,
                components=defaults,
                diagnostic_scores=diagnostic_scores or {},
                evidence_ids=("ev-score",),
                score_contribution_claim_ids=score_contribution_claim_ids,
            )
        )


class StageClassifierTests(unittest.TestCase):
    def test_stage_0_when_only_industry_regime_exists(self):
        snapshot = StageClassifier().classify(
            StageClassificationInput(
                score=make_score(
                    eps_fcf_explosion=1,
                    earnings_visibility=1,
                    bottleneck_pricing=1,
                    market_mispricing=1,
                    valuation_rerating=1,
                    capital_allocation=1,
                    information_confidence=1,
                ),
                theme_regime_score=75.0,
            )
        )

        self.assertEqual(snapshot.stage, Stage.STAGE_0)
        self.assertIn("industry regime", snapshot.stage_reason[0])

    def test_stage_1_when_company_event_exists_but_score_is_low(self):
        snapshot = StageClassifier().classify(
            StageClassificationInput(
                score=make_score(
                    eps_fcf_explosion=5,
                    earnings_visibility=5,
                    bottleneck_pricing=5,
                    market_mispricing=5,
                    valuation_rerating=5,
                    capital_allocation=1,
                    information_confidence=3,
                ),
                company_event_score=70.0,
            )
        )

        self.assertEqual(snapshot.stage, Stage.STAGE_1)

    def test_invalid_score_cannot_be_promoted_by_company_event(self):
        snapshot = StageClassifier().classify(
            StageClassificationInput(
                score=make_score(
                    diagnostic_scores={
                        "score_valid": 0.0,
                        "score_blocked_by_theme_route": 100.0,
                    },
                    eps_fcf_explosion=20,
                    earnings_visibility=20,
                    bottleneck_pricing=20,
                    market_mispricing=15,
                    valuation_rerating=15,
                    capital_allocation=5,
                    information_confidence=5,
                ),
                company_event_score=80.0,
                high_quality_company_event=True,
            )
        )

        self.assertEqual(snapshot.stage, Stage.STAGE_0)
        self.assertEqual(snapshot.grade, "Watch")
        self.assertIn("score was marked invalid", snapshot.stage_reason[0])

    def test_block_flag_without_score_valid_still_cannot_be_promoted(self):
        snapshot = StageClassifier().classify(
            StageClassificationInput(
                score=make_score(
                    diagnostic_scores={
                        "score_blocked_by_score_gap": 100.0,
                        "raw_score_total_before_score_gap_block": 83.0,
                    },
                    eps_fcf_explosion=20,
                    earnings_visibility=20,
                    bottleneck_pricing=20,
                    market_mispricing=15,
                    valuation_rerating=15,
                    capital_allocation=5,
                    information_confidence=5,
                ),
                company_event_score=90.0,
                high_quality_company_event=True,
            )
        )

        self.assertEqual(snapshot.stage, Stage.STAGE_0)
        self.assertEqual(snapshot.grade, "Watch")
        self.assertIn("score was marked invalid", snapshot.stage_reason[0])

    def test_archive_stage_uses_archive_grade_not_raw_score_grade(self):
        snapshot = StageClassifier().classify(
            StageClassificationInput(
                score=make_score(
                    eps_fcf_explosion=20,
                    earnings_visibility=20,
                    bottleneck_pricing=20,
                    market_mispricing=15,
                    valuation_rerating=15,
                    capital_allocation=5,
                    information_confidence=5,
                ),
                archive_requested=True,
            )
        )

        self.assertEqual(snapshot.stage, Stage.STAGE_5)
        self.assertEqual(snapshot.grade, "Archive")

    def test_stage_2_candidate_threshold(self):
        snapshot = StageClassifier().classify(StageClassificationInput(score=make_score()))

        self.assertEqual(snapshot.stage, Stage.STAGE_2)
        self.assertEqual(snapshot.grade, "B")

    def test_stage_3_green_requires_revision_and_low_red_team_risk(self):
        score = make_score(
            diagnostic_scores={"revision_score": 82.0},
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_GREEN)
        self.assertEqual(snapshot.red_team_status, "low")

    def test_stage_3_green_requires_claim_backed_components_when_audited(self):
        score = make_score(
            diagnostic_scores={
                "revision_score": 82.0,
                "claim_backed_claim_count_capped": 0.0,
                "score_claim_backed_component_ratio": 0.0,
                "orphan_score_component_count_capped": 7.0,
                "evidence_contract_required_primitive_count_capped": 6.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_stage_3_green_allows_complete_claim_backed_component_audit(self):
        score = make_score(
            claim_backed_components=True,
            diagnostic_scores={
                "revision_score": 82.0,
                "claim_backed_claim_count_capped": 12.0,
                "score_claim_backed_component_ratio": 100.0,
                "orphan_score_component_count_capped": 0.0,
                "evidence_contract_required_primitive_count_capped": 6.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_GREEN)

    def test_stage_3_green_requires_complete_positive_evidence_contract(self):
        score = make_score(
            claim_backed_components=True,
            diagnostic_scores={
                "revision_score": 82.0,
                "claim_backed_claim_count_capped": 7.0,
                "score_claim_backed_component_ratio": 100.0,
                "orphan_score_component_count_capped": 0.0,
                "evidence_contract_green_gate_required_primitive_count_capped": 2.0,
                "evidence_contract_green_gate_coverage_pct": 50.0,
                "evidence_contract_green_gate_missing_primitive_count_capped": 1.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_stage_3_green_blocks_when_evidence_contract_guard_is_present(self):
        score = make_score(
            diagnostic_scores={
                "revision_score": 82.0,
                "evidence_contract_guard_present_primitive_count_capped": 1.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_stage_3_green_blocks_when_evidence_contract_guard_is_unverified(self):
        score = make_score(
            diagnostic_scores={
                "revision_score": 82.0,
                "evidence_contract_guard_required_primitive_count_capped": 1.0,
                "evidence_contract_guard_missing_primitive_count_capped": 1.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_stage_3_green_allows_when_evidence_contract_guard_is_cleared(self):
        score = make_score(
            diagnostic_scores={
                "revision_score": 82.0,
                "evidence_contract_guard_required_primitive_count_capped": 1.0,
                "evidence_contract_guard_present_primitive_count_capped": 0.0,
                "evidence_contract_guard_cleared_primitive_count_capped": 1.0,
                "evidence_contract_guard_missing_primitive_count_capped": 0.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_GREEN)

    def test_emerging_theme_blocks_green_until_deep_research_is_complete(self):
        score = make_score(
            diagnostic_scores={"revision_score": 82.0, "emerging_theme_active": 100.0},
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_emerging_theme_can_be_green_after_deep_research_and_unlock_evidence(self):
        score = make_score(
            diagnostic_scores={
                "revision_score": 82.0,
                "emerging_theme_active": 100.0,
                "llm_deep_research_completed": 100.0,
                "green_unlock_evidence_score": 80.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_GREEN)

    def test_emerging_theme_can_be_green_after_source_backed_deep_research(self):
        score = make_score(
            claim_backed_components=True,
            diagnostic_scores={
                "revision_score": 82.0,
                "emerging_theme_active": 100.0,
                "source_backed_deep_research_completed": 100.0,
                "green_unlock_evidence_score": 80.0,
                "claim_backed_claim_count_capped": 7.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_GREEN)

    def test_date_unverified_only_evidence_blocks_green_even_outside_emerging_theme(self):
        score = make_score(
            diagnostic_scores={"revision_score": 82.0, "report_date_confidence": 0.0},
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_date_unverified_document_blocks_green_even_with_verified_report_confidence(self):
        score = make_score(
            diagnostic_scores={
                "revision_score": 82.0,
                "report_date_confidence": 100.0,
                "date_unverified_document_count_capped": 1.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_emerging_theme_date_unverified_snippet_blocks_green_after_unlock(self):
        score = make_score(
            diagnostic_scores={
                "revision_score": 82.0,
                "emerging_theme_active": 100.0,
                "llm_deep_research_completed": 100.0,
                "green_unlock_evidence_score": 80.0,
                "date_unverified_snippet_news_count_capped": 1.0,
                "report_date_confidence": 100.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_malformed_explicit_diagnostic_blocks_green_without_crashing(self):
        score = make_score(
            diagnostic_scores={
                "revision_score": 82.0,
                "report_date_confidence": 100.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )
        diagnostics = dict(score.diagnostic_scores)
        diagnostics["report_date_confidence"] = "unknown"
        object.__setattr__(score, "diagnostic_scores", diagnostics)

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_stage_3_yellow_when_score_is_high_but_green_is_incomplete(self):
        score = make_score(
            eps_fcf_explosion=20,
            earnings_visibility=17,
            bottleneck_pricing=17,
            market_mispricing=12,
            valuation_rerating=11,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_stage_3_green_requires_meaningful_revision_score(self):
        score = make_score(
            diagnostic_scores={"revision_score": 1.0},
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_stage_3_green_is_blocked_by_archetype_green_restriction(self):
        score = make_score(
            diagnostic_scores={
                "revision_score": 90.0,
                "structural_visibility_quality": 90.0,
                "archetype_green_restricted_by_profile": 1.0,
            },
            eps_fcf_explosion=20,
            earnings_visibility=20,
            bottleneck_pricing=20,
            market_mispricing=15,
            valuation_rerating=15,
            capital_allocation=5,
            information_confidence=5,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_YELLOW)

    def test_stage_3_red_when_valuation_runway_is_too_weak(self):
        score = make_score(
            diagnostic_scores={"revision_score": 80.0},
            eps_fcf_explosion=20,
            earnings_visibility=20,
            bottleneck_pricing=20,
            market_mispricing=15,
            valuation_rerating=6,
            capital_allocation=5,
            information_confidence=5,
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score))

        self.assertEqual(snapshot.stage, Stage.STAGE_3_RED)

    def test_stage_4a_when_existing_stage_3_thesis_remains_supported(self):
        score = make_score(
            diagnostic_scores={"revision_score": 80.0},
            eps_fcf_explosion=20,
            earnings_visibility=18,
            bottleneck_pricing=18,
            market_mispricing=13,
            valuation_rerating=12,
            capital_allocation=4,
            information_confidence=4,
        )

        snapshot = StageClassifier().classify(
            StageClassificationInput(
                score=score,
                previous_stage=Stage.STAGE_3_GREEN,
                thesis_ongoing=True,
            )
        )

        self.assertEqual(snapshot.stage, Stage.STAGE_4A)
        self.assertTrue(snapshot.stage_changed)

    def test_stage_4b_when_soft_exit_score_reaches_threshold(self):
        score = make_score()
        red_team = RedTeamEngine().assess(
            RedTeamSignals(
                symbol="CASE",
                as_of_date=date(2026, 5, 13),
                soft_4b_factors={
                    "return_since_stage3": 1.0,
                    "return_12_24m": 1.0,
                    "extreme_forward_valuation": 1.0,
                    "revision_slowdown": 0.5,
                    "market_crowding": 0.5,
                },
            )
        )

        snapshot = StageClassifier().classify(
            StageClassificationInput(
                score=score,
                red_team=red_team,
                previous_stage=Stage.STAGE_4A,
                thesis_ongoing=True,
            )
        )

        self.assertEqual(snapshot.stage, Stage.STAGE_4B)
        self.assertEqual(snapshot.grade, "4B-watch")

    def test_stage_4c_hard_break_overrides_high_score(self):
        score = make_score(
            diagnostic_scores={"revision_score": 90.0},
            eps_fcf_explosion=20,
            earnings_visibility=20,
            bottleneck_pricing=20,
            market_mispricing=15,
            valuation_rerating=15,
            capital_allocation=5,
            information_confidence=5,
        )
        red_team = RedTeamEngine().assess(
            RedTeamSignals(
                symbol="CASE",
                as_of_date=date(2026, 5, 13),
                thesis_break_factors={"contract_cancelled_or_delayed": 1.0},
                evidence_ids_by_signal={"contract_cancelled_or_delayed": ("ev-contract",)},
            )
        )

        snapshot = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

        self.assertEqual(snapshot.stage, Stage.STAGE_4C)
        self.assertIn("ev-contract", snapshot.evidence_ids)

    def test_classifier_rejects_red_team_data_after_score_date(self):
        score = make_score(as_of_date=date(2026, 5, 13))
        red_team = RedTeamEngine().assess(
            RedTeamSignals(
                symbol="CASE",
                as_of_date=date(2026, 5, 14),
                thesis_break_factors={"opm_decline": 1.0},
            )
        )

        with self.assertRaisesRegex(ValueError, "red_team as_of_date cannot be after score as_of_date"):
            StageClassificationInput(score=score, red_team=red_team)


if __name__ == "__main__":
    unittest.main()
