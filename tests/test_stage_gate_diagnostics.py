from datetime import date
import unittest
from unittest.mock import patch

from e2r.models import ScoreSnapshot, Stage
from e2r.red_team import RedTeamAssessment, RedTeamEngine, RedTeamSignals
from e2r.scoring import CANONICAL_SCORE_COMPONENTS, DeterministicScorer, ScoringPayload
from e2r.sector_profiles import SectorProfile, profile_id
from e2r.staging import StageClassificationInput, StageClassifier
from e2r.stage_gate_diagnostics import diagnose_stage_gates, promotion_band
from e2r.calibration.taxonomy import large_sector_for_archetype


WEIGHTED_GATE_ACCEPTANCE_ARCHETYPES = (
    "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
    "C02_POWER_GRID_DATACENTER_CAPEX",
)


def _complete_components(**overrides: float) -> dict[str, float]:
    components = {component.key: component.max_points for component in CANONICAL_SCORE_COMPONENTS}
    components.update(overrides)
    return components


def _weighted_score_for_archetype(archetype: str, *, bottleneck_pricing: float = 20.0) -> ScoreSnapshot:
    large_sector = large_sector_for_archetype(archetype)
    if large_sector is None:
        raise AssertionError(f"missing large sector for {archetype}")
    with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "rolling"}):
        return DeterministicScorer().score(
            ScoringPayload(
                symbol="WEIGHTED_GATE_CASE",
                as_of_date=date(2025, 5, 1),
                components=_complete_components(bottleneck_pricing=bottleneck_pricing),
                diagnostic_scores={
                    "revision_score": 90,
                    "structural_visibility_quality": 90,
                    "contract_quality": 90,
                    "one_off_shortage_risk": 0,
                    "cross_evidence_family_count": 4,
                    "evidence_family_financial_actual": 1,
                    "evidence_family_disclosure": 1,
                    "evidence_family_research_report": 1,
                    "evidence_family_consensus_revision": 1,
                    "llm_deep_research_completed": 100,
                    "green_unlock_evidence_score": 90,
                },
                evidence_ids=("source-backed-positive", "source-backed-guard"),
                large_sector_id=large_sector,
                canonical_archetype_id=archetype,
            )
        )


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

    def test_reports_stage4_transition_readiness_separately_from_green_gate(self):
        score = ScoreSnapshot(
            symbol="CASE",
            as_of_date=date(2026, 5, 13),
            eps_fcf_explosion_score=20,
            earnings_visibility_score=18,
            bottleneck_pricing_score=18,
            market_mispricing_score=12,
            valuation_rerating_score=11,
            capital_allocation_score=4,
            information_confidence_score=4,
            risk_penalty=0,
            total_score=87,
            diagnostic_scores={
                "score_valid": 100,
                "revision_score": 90,
                "structural_visibility_quality": 90,
                "report_date_confidence": 100,
                "date_unverified_snippet_news_count_capped": 0,
                "date_unverified_document_count_capped": 0,
                "cross_evidence_family_count": 4,
            },
        )
        continuation = diagnose_stage_gates(score, RedTeamAssessment.empty("CASE", date(2026, 5, 13)))
        soft_4b = RedTeamEngine().assess(
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
        overlay = diagnose_stage_gates(score, soft_4b)
        hard_4c = RedTeamEngine().assess(
            RedTeamSignals(
                symbol="CASE",
                as_of_date=date(2026, 5, 13),
                thesis_break_factors={"contract_cancelled_or_delayed": 1.0},
                evidence_ids_by_signal={"contract_cancelled_or_delayed": ("ev-contract-cancel",)},
                hard_break_quorum_by_signal={"contract_cancelled_or_delayed": True},
            )
        )
        thesis_break = diagnose_stage_gates(score, hard_4c)

        self.assertTrue(continuation.stage4a_continuation_gate_passed)
        self.assertFalse(continuation.stage4b_overlay_gate_passed)
        self.assertTrue(overlay.stage4b_overlay_gate_passed)
        self.assertTrue(thesis_break.stage4c_thesis_break_gate_passed)
        self.assertIn("stage4b_soft_overlay_score", overlay.values_vs_thresholds)
        self.assertIn("stage4c_red_team_hard_break", thesis_break.values_vs_thresholds)

    def test_component_gate_diagnostics_use_archetype_weighted_values(self):
        score = ScoreSnapshot(
            symbol="000660",
            as_of_date=date(2024, 5, 1),
            eps_fcf_explosion_score=20,
            earnings_visibility_score=15.1502,
            bottleneck_pricing_score=11.6339,
            market_mispricing_score=12.852,
            valuation_rerating_score=12.339,
            capital_allocation_score=0.101,
            information_confidence_score=3,
            risk_penalty=0,
            total_score=76.7639,
            diagnostic_scores={
                "score_valid": 100,
                "revision_score": 100,
                "structural_visibility_quality": 75,
                "one_off_shortage_risk": 0,
                "archetype_weight_profile_applied": 1,
                "archetype_weight_bottleneck_pricing": 19,
                "archetype_component_bottleneck_pricing": 11.0522,
            },
        )

        diag = diagnose_stage_gates(score, RedTeamAssessment.empty("000660", date(2024, 5, 1)))
        detail = diag.values_vs_thresholds["failed_stage3_bottleneck"]

        self.assertEqual(detail["value"], 11.0522)
        self.assertEqual(detail["threshold"], 14.25)
        self.assertEqual(detail["raw_value"], 11.6339)
        self.assertEqual(detail["raw_threshold"], 15.0)
        self.assertEqual(detail["archetype_weighted"], True)

    def test_contract_quality_failure_blocks_stage3_green_diagnostic(self):
        score = ScoreSnapshot(
            symbol="267260",
            as_of_date=date(2024, 5, 1),
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
                "score_valid": 100,
                "revision_score": 100,
                "structural_visibility_quality": 90,
                "contract_quality": 20,
                "one_off_shortage_risk": 0,
                "sector_profile_id": profile_id(SectorProfile.POWER_EQUIPMENT),
            },
        )

        diag = diagnose_stage_gates(score, RedTeamAssessment.empty("267260", date(2024, 5, 1)))

        self.assertIn("failed_stage3_contract_quality", diag.failed_gate_names)
        self.assertFalse(diag.stage3_green_gate_passed)
        stage = StageClassifier().classify(
            StageClassificationInput(score=score, red_team=RedTeamAssessment.empty("267260", date(2024, 5, 1)))
        )
        self.assertNotEqual(stage.stage, Stage.STAGE_3_GREEN)

    def test_explicit_contract_not_required_overrides_sector_profile_contract_diagnostic(self):
        score = ScoreSnapshot(
            symbol="NO_CONTRACT_REQUIRED",
            as_of_date=date(2024, 5, 1),
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
                "score_valid": 100,
                "revision_score": 100,
                "structural_visibility_quality": 90,
                "contract_quality": 20,
                "contract_required_for_green": 0,
                "one_off_shortage_risk": 0,
                "sector_profile_id": profile_id(SectorProfile.POWER_EQUIPMENT),
            },
        )
        red_team = RedTeamAssessment.empty("NO_CONTRACT_REQUIRED", date(2024, 5, 1))

        diag = diagnose_stage_gates(score, red_team)
        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

        self.assertNotIn("failed_stage3_contract_quality", diag.failed_gate_names)
        self.assertTrue(diag.stage3_green_gate_passed)
        self.assertEqual(stage.stage, Stage.STAGE_3_GREEN)

    def test_evidence_contract_positive_gap_blocks_stage3_green_diagnostic(self):
        score = ScoreSnapshot(
            symbol="CONTRACT_GAP",
            as_of_date=date(2024, 5, 1),
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
                "score_valid": 100,
                "revision_score": 100,
                "structural_visibility_quality": 90,
                "contract_quality": 90,
                "one_off_shortage_risk": 0,
                "evidence_contract_green_gate_required_primitive_count_capped": 3,
                "evidence_contract_green_gate_coverage_pct": 66.6667,
                "evidence_contract_green_gate_missing_primitive_count_capped": 1,
            },
        )
        red_team = RedTeamAssessment.empty("CONTRACT_GAP", date(2024, 5, 1))

        diag = diagnose_stage_gates(score, red_team)
        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

        self.assertIn("failed_evidence_contract_positive_coverage", diag.failed_gate_names)
        self.assertFalse(diag.stage3_green_gate_passed)
        self.assertEqual(stage.stage, Stage.STAGE_3_YELLOW)

    def test_claim_backed_gap_blocks_stage3_green_diagnostic(self):
        score = ScoreSnapshot(
            symbol="ORPHAN_GREEN",
            as_of_date=date(2024, 5, 1),
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
                "score_valid": 100,
                "revision_score": 100,
                "structural_visibility_quality": 90,
                "contract_quality": 90,
                "one_off_shortage_risk": 0,
                "claim_backed_claim_count_capped": 0,
                "score_claim_backed_component_ratio": 0,
                "orphan_score_component_count_capped": 7,
                "evidence_contract_required_primitive_count_capped": 6,
            },
        )
        red_team = RedTeamAssessment.empty("ORPHAN_GREEN", date(2024, 5, 1))

        diag = diagnose_stage_gates(score, red_team)
        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

        self.assertIn("failed_claim_backed_green_score", diag.failed_gate_names)
        self.assertFalse(diag.stage3_green_gate_passed)
        self.assertEqual(stage.stage, Stage.STAGE_3_YELLOW)

    def test_evidence_contract_guard_blocks_stage3_green_diagnostic(self):
        score = ScoreSnapshot(
            symbol="GUARD_PRESENT",
            as_of_date=date(2024, 5, 1),
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
                "score_valid": 100,
                "revision_score": 100,
                "structural_visibility_quality": 90,
                "contract_quality": 90,
                "one_off_shortage_risk": 0,
                "evidence_contract_guard_present_primitive_count_capped": 1,
            },
        )
        red_team = RedTeamAssessment.empty("GUARD_PRESENT", date(2024, 5, 1))

        diag = diagnose_stage_gates(score, red_team)
        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

        self.assertIn("failed_evidence_contract_guard_present", diag.failed_gate_names)
        self.assertFalse(diag.stage3_green_gate_passed)
        self.assertEqual(stage.stage, Stage.STAGE_3_YELLOW)

    def test_unverified_evidence_contract_guard_blocks_stage3_green_diagnostic(self):
        score = ScoreSnapshot(
            symbol="GUARD_UNVERIFIED",
            as_of_date=date(2024, 5, 1),
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
                "score_valid": 100,
                "revision_score": 100,
                "structural_visibility_quality": 90,
                "contract_quality": 90,
                "one_off_shortage_risk": 0,
                "evidence_contract_guard_required_primitive_count_capped": 1,
                "evidence_contract_guard_missing_primitive_count_capped": 1,
            },
        )
        red_team = RedTeamAssessment.empty("GUARD_UNVERIFIED", date(2024, 5, 1))

        diag = diagnose_stage_gates(score, red_team)
        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

        self.assertIn("failed_evidence_contract_guard_unverified", diag.failed_gate_names)
        self.assertFalse(diag.stage3_green_gate_passed)
        self.assertEqual(stage.stage, Stage.STAGE_3_YELLOW)

    def test_archetype_green_restriction_is_reported_as_stage3_gate(self):
        score = ScoreSnapshot(
            symbol="EVENT_ONLY_CASE",
            as_of_date=date(2025, 5, 1),
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
                "score_valid": 100,
                "revision_score": 90,
                "structural_visibility_quality": 90,
                "contract_quality": 90,
                "one_off_shortage_risk": 0,
                "archetype_green_restricted_by_profile": 1,
            },
        )

        diag = diagnose_stage_gates(score, RedTeamAssessment.empty("EVENT_ONLY_CASE", date(2025, 5, 1)))

        self.assertIn("failed_archetype_green_policy_restriction", diag.failed_gate_names)
        self.assertFalse(diag.stage3_green_gate_passed)

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
        self.assertFalse(diag.stage2_gate_passed)
        self.assertFalse(diag.stage3_green_gate_passed)

    def test_report_date_confidence_gate_matches_classifier_outside_emerging_theme(self):
        score = ScoreSnapshot(
            symbol="DATE_UNVERIFIED_CASE",
            as_of_date=date(2025, 5, 1),
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
                "score_valid": 100,
                "revision_score": 90,
                "structural_visibility_quality": 90,
                "contract_quality": 90,
                "one_off_shortage_risk": 0,
                "report_date_confidence": 0,
            },
        )
        red_team = RedTeamAssessment.empty("DATE_UNVERIFIED_CASE", date(2025, 5, 1))

        diag = diagnose_stage_gates(score, red_team)
        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

        self.assertIn("failed_report_date_confidence", diag.failed_gate_names)
        self.assertFalse(diag.stage3_green_gate_passed)
        self.assertEqual(stage.stage, Stage.STAGE_3_YELLOW)

    def test_date_unverified_document_gate_matches_classifier_with_verified_report_confidence(self):
        score = ScoreSnapshot(
            symbol="MIXED_DATE_CASE",
            as_of_date=date(2025, 5, 1),
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
                "score_valid": 100,
                "revision_score": 90,
                "structural_visibility_quality": 90,
                "contract_quality": 90,
                "one_off_shortage_risk": 0,
                "report_date_confidence": 100,
                "date_unverified_document_count_capped": 1,
            },
        )
        red_team = RedTeamAssessment.empty("MIXED_DATE_CASE", date(2025, 5, 1))

        diag = diagnose_stage_gates(score, red_team)
        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

        self.assertIn("failed_date_unverified_green_evidence", diag.failed_gate_names)
        self.assertFalse(diag.stage3_green_gate_passed)
        self.assertEqual(stage.stage, Stage.STAGE_3_YELLOW)

    def test_emerging_theme_date_unverified_snippet_gate_matches_classifier_after_unlock(self):
        score = ScoreSnapshot(
            symbol="EMERGING_DATE_SNIPPET_CASE",
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
                "score_valid": 100,
                "revision_score": 90,
                "structural_visibility_quality": 90,
                "contract_quality": 90,
                "one_off_shortage_risk": 0,
                "emerging_theme_active": 100,
                "llm_deep_research_completed": 100,
                "green_unlock_evidence_score": 80,
                "date_unverified_snippet_news_count_capped": 1,
                "report_date_confidence": 100,
            },
        )
        red_team = RedTeamAssessment.empty("EMERGING_DATE_SNIPPET_CASE", date(2026, 6, 8))

        diag = diagnose_stage_gates(score, red_team)
        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

        self.assertIn("failed_emerging_theme_date_verified_evidence", diag.failed_gate_names)
        self.assertFalse(diag.stage3_green_gate_passed)
        self.assertEqual(stage.stage, Stage.STAGE_3_YELLOW)

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

    def test_promotion_band_uses_weighted_stage2_component_gates(self):
        score = ScoreSnapshot(
            symbol="WEIGHTED_CASE",
            as_of_date=date(2025, 5, 1),
            eps_fcf_explosion_score=12,
            earnings_visibility_score=16,
            bottleneck_pricing_score=8,
            market_mispricing_score=10,
            valuation_rerating_score=8,
            capital_allocation_score=4,
            information_confidence_score=4,
            risk_penalty=0,
            total_score=70,
            diagnostic_scores={
                "score_valid": 100,
                "archetype_weight_profile_applied": 1,
                "archetype_weight_eps_fcf_explosion": 15,
                "archetype_component_eps_fcf_explosion": 9,
                "archetype_weight_valuation_rerating": 25,
                "archetype_component_valuation_rerating": 8,
                "archetype_weight_information_confidence": 5,
                "archetype_component_information_confidence": 4,
            },
        )

        self.assertEqual(promotion_band(score), "Stage 2")

    def test_promotion_band_uses_weighted_stage3_watch_component_gate(self):
        score = ScoreSnapshot(
            symbol="WEIGHTED_WATCH_CASE",
            as_of_date=date(2025, 5, 1),
            eps_fcf_explosion_score=14,
            earnings_visibility_score=18,
            bottleneck_pricing_score=18,
            market_mispricing_score=12,
            valuation_rerating_score=12,
            capital_allocation_score=4,
            information_confidence_score=4,
            risk_penalty=0,
            total_score=76,
            diagnostic_scores={
                "score_valid": 100,
                "revision_score": 70,
                "structural_visibility_quality": 70,
                "cross_evidence_family_count": 3,
                "archetype_weight_profile_applied": 1,
                "archetype_weight_eps_fcf_explosion": 15,
                "archetype_component_eps_fcf_explosion": 9,
                "archetype_weight_valuation_rerating": 25,
                "archetype_component_valuation_rerating": 20,
                "archetype_weight_information_confidence": 5,
                "archetype_component_information_confidence": 4,
            },
        )

        self.assertEqual(promotion_band(score), "Stage 2-High")

    def test_weighted_gate_acceptance_positive_cases_promote_across_first_slice_archetypes(self):
        for archetype in WEIGHTED_GATE_ACCEPTANCE_ARCHETYPES:
            with self.subTest(archetype=archetype):
                score = _weighted_score_for_archetype(archetype)
                stage = StageClassifier().classify(StageClassificationInput(score=score))
                diag = diagnose_stage_gates(score, RedTeamAssessment.empty(score.symbol, score.as_of_date))

                self.assertEqual(stage.stage.value, "3-Green")
                self.assertTrue(diag.stage3_green_gate_passed)
                self.assertEqual(diag.promotion_band, "Stage 3-Green")

    def test_weighted_gate_acceptance_guard_cases_do_not_promote_when_required_axis_is_short(self):
        for archetype in WEIGHTED_GATE_ACCEPTANCE_ARCHETYPES:
            with self.subTest(archetype=archetype):
                score = _weighted_score_for_archetype(archetype, bottleneck_pricing=14.0)
                stage = StageClassifier().classify(StageClassificationInput(score=score))
                diag = diagnose_stage_gates(score, RedTeamAssessment.empty(score.symbol, score.as_of_date))

                self.assertNotEqual(stage.stage.value, "3-Green")
                self.assertIn("failed_stage3_bottleneck", diag.failed_gate_names)
                self.assertFalse(diag.stage3_green_gate_passed)


if __name__ == "__main__":
    unittest.main()
