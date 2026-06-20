from datetime import date
from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch

from e2r.calibration.archetype_weight_profile import (
    build_archetype_weight_profile_payload,
    load_archetype_weight_profile,
    write_archetype_weight_runtime_profile,
)
from e2r.calibration.scoring_profile import ScoringProfile
from e2r.calibration.taxonomy import large_sector_for_archetype
from e2r.models import Stage
from e2r.red_team import RedTeamAssessment
from e2r.scoring import ArchetypeClassificationError, CANONICAL_SCORE_COMPONENTS, DeterministicScorer, ScoringPayload
from e2r.staging import StageClassificationInput, StageClassifier


def complete_components(**overrides):
    components = {component.key: component.max_points for component in CANONICAL_SCORE_COMPONENTS}
    components.update(overrides)
    return components


def runtime_profile(path: Path) -> ScoringProfile:
    return ScoringProfile(
        profile_id="test_v2_2",
        profile_status="test",
        thresholds={
            "stage2_total_min": 65.0,
            "stage2_eps_fcf_min": 10.0,
            "stage2_valuation_min": 7.0,
            "stage2_information_confidence_min": 3.0,
            "stage3_yellow_total_min": 75.0,
            "stage3_green_total_min": 87.0,
            "stage3_green_eps_fcf_min": 17.0,
            "stage3_green_visibility_min": 15.0,
            "stage3_green_bottleneck_min": 15.0,
            "stage3_green_mispricing_min": 10.0,
            "stage3_green_valuation_min": 10.0,
            "stage3_green_revision_min": 55.0,
            "stage3_green_structural_visibility_min": 45.0,
        },
        adjustments={},
        guardrails={
            "rolling_calibration_enabled": True,
            "archetype_weight_runtime_enabled": True,
            "archetype_weight_profile_path": str(path),
            "archetype_classification_required": True,
            "archetype_large_sector_fallback_allowed": False,
            "price_only_blowoff_blocks_positive_stage": True,
            "full_4b_requires_non_price_evidence": True,
            "hard_4c_thesis_break_routes_to_4c": True,
        },
    )


class ArchetypeWeightRuntimeTests(unittest.TestCase):
    def test_weight_payload_has_100_point_profiles(self):
        payload = build_archetype_weight_profile_payload()

        self.assertIn("C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", payload["archetype_weights"])
        self.assertIn("C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", payload["archetype_weights"])
        self.assertIn("C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", payload["archetype_weights"])
        for row in payload["archetype_weights"].values():
            self.assertAlmostEqual(sum(row["weights"].values()), 100.0, places=4)

    def test_write_profile_adds_v12_price_path_support(self):
        with tempfile.TemporaryDirectory() as tmp:
            aggregate_path = Path(tmp) / "aggregate.json"
            aggregate_path.write_text(
                json.dumps(
                    [
                        {
                            "group_name": "canonical_archetype_id",
                            "group_value": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
                            "row_count": 77,
                            "unique_case_count": 30,
                            "unique_symbol_count": 18,
                            "positive_case_count": 12,
                            "counterexample_count": 8,
                            "good_stage2_count": 20,
                            "bad_stage2_count": 3,
                            "avg_stage2_MFE90": 55.0,
                            "avg_stage2_MAE90": -10.0,
                        }
                    ]
                ),
                encoding="utf-8",
            )

            result = write_archetype_weight_runtime_profile(
                aggregate_metrics_path=aggregate_path,
                output_path=Path(tmp) / "profile.json",
                report_path=Path(tmp) / "report.md",
            )

            profile = load_archetype_weight_profile(result["profile_path"])
            match = profile.match(
                canonical_archetype_id="C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
                large_sector_id=None,
            )
            self.assertIsNotNone(match)
            self.assertEqual(match.support["row_count"], 77)
            self.assertIn("K-food/K-beauty", Path(result["report_path"]).read_text(encoding="utf-8"))

    def test_scorer_uses_archetype_specific_weighted_total(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.json"
            profile_path.write_text(
                json.dumps(build_archetype_weight_profile_payload(), ensure_ascii=False),
                encoding="utf-8",
            )
            payload = ScoringPayload(
                symbol="TEST",
                as_of_date=date(2026, 5, 14),
                components=complete_components(
                    eps_fcf_explosion=16.0,
                    earnings_visibility=18.0,
                    bottleneck_pricing=10.0,
                    market_mispricing=10.0,
                    valuation_rerating=9.0,
                    capital_allocation=2.0,
                    information_confidence=4.0,
                ),
                large_sector_id="L5_CONSUMER_BRAND_DISTRIBUTION",
                canonical_archetype_id="C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
            )

            with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                score = DeterministicScorer().score(payload)

            self.assertGreater(score.total_score, sum(payload.components.values()))
            self.assertEqual(score.diagnostic_scores["archetype_weight_profile_applied"], 1.0)
            self.assertEqual(score.diagnostic_scores["archetype_weight_match_is_archetype"], 1.0)
            self.assertIn("archetype_weight:C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", score.scoring_version)

    def test_c08_semiconductor_test_socket_uses_canonical_weight_without_fallback(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.json"
            profile_path.write_text(
                json.dumps(build_archetype_weight_profile_payload(), ensure_ascii=False),
                encoding="utf-8",
            )
            payload = ScoringPayload(
                symbol="SEMI_SOCKET",
                as_of_date=date(2026, 5, 14),
                components=complete_components(
                    eps_fcf_explosion=15.0,
                    earnings_visibility=17.0,
                    bottleneck_pricing=12.0,
                    market_mispricing=10.0,
                    valuation_rerating=9.0,
                    capital_allocation=3.0,
                    information_confidence=4.0,
                ),
                large_sector_id="L2_AI_SEMICONDUCTOR_ELECTRONICS",
                canonical_archetype_id="C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
            )

            with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                score = DeterministicScorer().score(payload)

            self.assertEqual(score.diagnostic_scores["archetype_weight_profile_applied"], 1.0)
            self.assertEqual(score.diagnostic_scores["archetype_weight_match_is_archetype"], 1.0)
            self.assertNotIn("archetype_weight_canonical_missing_large_sector_fallback", score.diagnostic_scores)
            self.assertNotIn("archetype_weight_fallback_used", score.diagnostic_scores)
            self.assertIn("archetype_weight:C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", score.scoring_version)

    def test_kbeauty_green_can_use_non_contract_visibility_but_industrial_requires_contract_if_marked(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.json"
            profile_path.write_text(
                json.dumps(build_archetype_weight_profile_payload(), ensure_ascii=False),
                encoding="utf-8",
            )
            kbeauty_payload = ScoringPayload(
                symbol="KBEAUTY",
                as_of_date=date(2026, 5, 14),
                components=complete_components(
                    eps_fcf_explosion=18.0,
                    earnings_visibility=19.0,
                    bottleneck_pricing=15.0,
                    market_mispricing=13.0,
                    valuation_rerating=12.0,
                    capital_allocation=5.0,
                    information_confidence=5.0,
                ),
                diagnostic_scores={
                    "revision_score": 70.0,
                    "structural_visibility_quality": 55.0,
                    "contract_quality": 0.0,
                    "contract_required_for_green": 0.0,
                },
                large_sector_id="L5_CONSUMER_BRAND_DISTRIBUTION",
                canonical_archetype_id="C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
            )
            industrial_payload = ScoringPayload(
                symbol="IND",
                as_of_date=date(2026, 5, 14),
                components=kbeauty_payload.components,
                diagnostic_scores={
                    "revision_score": 70.0,
                    "structural_visibility_quality": 55.0,
                    "contract_quality": 20.0,
                    "contract_required_for_green": 1.0,
                },
                large_sector_id="L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
                canonical_archetype_id="C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
            )
            red_team_low = RedTeamAssessment.empty("KBEAUTY", date(2026, 5, 14))
            red_team_ind = RedTeamAssessment.empty("IND", date(2026, 5, 14))

            with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                kbeauty_score = DeterministicScorer().score(kbeauty_payload)
                industrial_score = DeterministicScorer().score(industrial_payload)
            with patch("e2r.staging.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                kbeauty_stage = StageClassifier().classify(
                    StageClassificationInput(score=kbeauty_score, red_team=red_team_low)
                )
                industrial_stage = StageClassifier().classify(
                    StageClassificationInput(score=industrial_score, red_team=red_team_ind)
                )

            self.assertEqual(kbeauty_stage.stage, Stage.STAGE_3_GREEN)
            self.assertNotEqual(industrial_stage.stage, Stage.STAGE_3_GREEN)

    def test_redteam_guardrail_archetypes_do_not_unlock_green_from_high_scores(self):
        guardrail_archetypes = (
            "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
            "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
            "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
            "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
        )

        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.json"
            profile_path.write_text(
                json.dumps(build_archetype_weight_profile_payload(), ensure_ascii=False),
                encoding="utf-8",
            )

            for canonical_archetype_id in guardrail_archetypes:
                with self.subTest(canonical_archetype_id=canonical_archetype_id):
                    payload = ScoringPayload(
                        symbol="GUARD",
                        as_of_date=date(2026, 5, 14),
                        components=complete_components(
                            eps_fcf_explosion=20.0,
                            earnings_visibility=20.0,
                            bottleneck_pricing=20.0,
                            market_mispricing=15.0,
                            valuation_rerating=15.0,
                            capital_allocation=5.0,
                            information_confidence=5.0,
                        ),
                        diagnostic_scores={
                            "revision_score": 100.0,
                            "structural_visibility_quality": 100.0,
                            "contract_quality": 100.0,
                            "contract_required_for_green": 0.0,
                        },
                        large_sector_id="L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
                        canonical_archetype_id=canonical_archetype_id,
                    )
                    red_team = RedTeamAssessment.empty("GUARD", date(2026, 5, 14))

                    with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                        score = DeterministicScorer().score(payload)
                    with patch("e2r.staging.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

                    self.assertEqual(score.diagnostic_scores["archetype_green_restricted_by_profile"], 1.0)
                    self.assertNotEqual(stage.stage, Stage.STAGE_3_GREEN)

    def test_conditional_green_policies_require_but_can_unlock_with_conversion_evidence(self):
        conditional_archetypes = (
            "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
            "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
            "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
            "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
            "C11_BATTERY_ORDERBOOK_RERATING",
            "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
            "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
            "C15_MATERIAL_SPREAD_SUPERCYCLE",
            "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
            "C19_BRAND_RETAIL_INVENTORY_MARGIN",
            "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION",
            "C27_CONTENT_IP_GLOBAL_MONETIZATION",
            "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
            "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
            "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
        )
        high_components = complete_components(
            eps_fcf_explosion=20.0,
            earnings_visibility=20.0,
            bottleneck_pricing=20.0,
            market_mispricing=15.0,
            valuation_rerating=15.0,
            capital_allocation=5.0,
            information_confidence=5.0,
        )
        base_diagnostics = {
            "revision_score": 100.0,
            "structural_visibility_quality": 100.0,
            "contract_quality": 100.0,
            "contract_required_for_green": 0.0,
        }
        unlock_diagnostics = {
            **base_diagnostics,
            "actual_profit_conversion_score": 80.0,
            "fcf_quality_score": 80.0,
            "domain_specific_evidence_score": 75.0,
            "research_axis_bridge_present_count_capped": 5.0,
            "research_axis_bridge_margin": 100.0,
            "research_axis_bridge_capital_return": 100.0,
            "research_axis_bridge_bio_commercialization": 100.0,
        }

        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.json"
            profile_path.write_text(
                json.dumps(build_archetype_weight_profile_payload(), ensure_ascii=False),
                encoding="utf-8",
            )

            for canonical_archetype_id in conditional_archetypes:
                with self.subTest(canonical_archetype_id=canonical_archetype_id):
                    blocked_payload = ScoringPayload(
                        symbol="COND_BLOCKED",
                        as_of_date=date(2026, 5, 14),
                        components=high_components,
                        diagnostic_scores=base_diagnostics,
                        large_sector_id=large_sector_for_archetype(canonical_archetype_id),
                        canonical_archetype_id=canonical_archetype_id,
                    )
                    unlocked_payload = ScoringPayload(
                        symbol="COND_UNLOCKED",
                        as_of_date=date(2026, 5, 14),
                        components=high_components,
                        diagnostic_scores=unlock_diagnostics,
                        large_sector_id=large_sector_for_archetype(canonical_archetype_id),
                        canonical_archetype_id=canonical_archetype_id,
                    )
                    blocked_red_team = RedTeamAssessment.empty("COND_BLOCKED", date(2026, 5, 14))
                    unlocked_red_team = RedTeamAssessment.empty("COND_UNLOCKED", date(2026, 5, 14))

                    with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                        blocked_score = DeterministicScorer().score(blocked_payload)
                        unlocked_score = DeterministicScorer().score(unlocked_payload)
                    with patch("e2r.staging.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                        blocked_stage = StageClassifier().classify(
                            StageClassificationInput(score=blocked_score, red_team=blocked_red_team)
                        )
                        unlocked_stage = StageClassifier().classify(
                            StageClassificationInput(score=unlocked_score, red_team=unlocked_red_team)
                        )

                    self.assertEqual(blocked_score.diagnostic_scores["archetype_green_policy_unlock_required"], 1.0)
                    self.assertEqual(blocked_score.diagnostic_scores["archetype_green_restricted_by_profile"], 1.0)
                    self.assertNotEqual(blocked_stage.stage, Stage.STAGE_3_GREEN)
                    self.assertEqual(unlocked_score.diagnostic_scores["archetype_green_policy_unlock_required"], 1.0)
                    self.assertGreaterEqual(
                        unlocked_score.diagnostic_scores["archetype_green_policy_unlock_evidence"],
                        60.0,
                    )
                    self.assertEqual(unlocked_score.diagnostic_scores["archetype_green_restricted_by_profile"], 0.0)
                    self.assertEqual(unlocked_stage.stage, Stage.STAGE_3_GREEN)

    def test_absolute_green_block_policies_stay_blocked_even_with_unlock_evidence(self):
        absolute_block_archetypes = (
            "C14_EV_DEMAND_SLOWDOWN_4B_4C",
            "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
            "C24_BIO_TRIAL_DATA_EVENT_RISK",
            "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
            "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
            "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
            "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
            "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
        )
        high_components = complete_components(
            eps_fcf_explosion=20.0,
            earnings_visibility=20.0,
            bottleneck_pricing=20.0,
            market_mispricing=15.0,
            valuation_rerating=15.0,
            capital_allocation=5.0,
            information_confidence=5.0,
        )
        unlock_diagnostics = {
            "revision_score": 100.0,
            "structural_visibility_quality": 100.0,
            "contract_quality": 100.0,
            "contract_required_for_green": 0.0,
            "actual_profit_conversion_score": 100.0,
            "fcf_quality_score": 100.0,
            "domain_specific_evidence_score": 100.0,
            "green_unlock_evidence_score": 100.0,
        }

        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.json"
            profile_path.write_text(
                json.dumps(build_archetype_weight_profile_payload(), ensure_ascii=False),
                encoding="utf-8",
            )

            for canonical_archetype_id in absolute_block_archetypes:
                with self.subTest(canonical_archetype_id=canonical_archetype_id):
                    payload = ScoringPayload(
                        symbol="ABS_BLOCK",
                        as_of_date=date(2026, 5, 14),
                        components=high_components,
                        diagnostic_scores=unlock_diagnostics,
                        large_sector_id=large_sector_for_archetype(canonical_archetype_id),
                        canonical_archetype_id=canonical_archetype_id,
                    )
                    red_team = RedTeamAssessment.empty("ABS_BLOCK", date(2026, 5, 14))

                    with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                        score = DeterministicScorer().score(payload)
                    with patch("e2r.staging.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

                    self.assertEqual(score.diagnostic_scores["archetype_green_policy_absolute_block"], 1.0)
                    self.assertEqual(score.diagnostic_scores["archetype_green_restricted_by_profile"], 1.0)
                    self.assertNotEqual(stage.stage, Stage.STAGE_3_GREEN)

    def test_red_watch_policy_can_unlock_only_with_source_backed_green_bridge(self):
        high_components = complete_components(
            eps_fcf_explosion=20.0,
            earnings_visibility=20.0,
            bottleneck_pricing=20.0,
            market_mispricing=15.0,
            valuation_rerating=15.0,
            capital_allocation=5.0,
            information_confidence=5.0,
        )
        source_backed_bridge_diagnostics = {
            "revision_score": 100.0,
            "structural_visibility_quality": 100.0,
            "contract_quality": 100.0,
            "contract_required_for_green": 0.0,
            "actual_profit_conversion_score": 100.0,
            "fcf_quality_score": 100.0,
            "domain_specific_evidence_score": 100.0,
            "green_unlock_evidence_score": 100.0,
            "source_backed_green_bridge_raw": 92.0,
            "research_axis_bridge_guard_risk": 0.0,
            "research_axis_bridge_guard_risk_penalty_points": 0.0,
            "research_axis_bridge_present_count_capped": 5.0,
        }

        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.json"
            profile_path.write_text(
                json.dumps(build_archetype_weight_profile_payload(), ensure_ascii=False),
                encoding="utf-8",
            )

            for canonical_archetype_id in (
                "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
                "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
            ):
                with self.subTest(canonical_archetype_id=canonical_archetype_id):
                    payload = ScoringPayload(
                        symbol="SOURCE_BRIDGE",
                        as_of_date=date(2026, 5, 14),
                        components=high_components,
                        diagnostic_scores=source_backed_bridge_diagnostics,
                        large_sector_id=large_sector_for_archetype(canonical_archetype_id),
                        canonical_archetype_id=canonical_archetype_id,
                    )
                    red_team = RedTeamAssessment.empty("SOURCE_BRIDGE", date(2026, 5, 14))

                    with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                        score = DeterministicScorer().score(payload)
                    with patch("e2r.staging.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

                    self.assertEqual(score.diagnostic_scores["archetype_green_policy_absolute_block"], 1.0)
                    self.assertEqual(score.diagnostic_scores["archetype_green_policy_source_backed_override"], 1.0)
                    self.assertEqual(score.diagnostic_scores["archetype_green_restricted_by_profile"], 0.0)
                    self.assertEqual(stage.stage, Stage.STAGE_3_GREEN)

            for canonical_archetype_id in (
                "C24_BIO_TRIAL_DATA_EVENT_RISK",
                "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
            ):
                with self.subTest(canonical_archetype_id=canonical_archetype_id):
                    payload = ScoringPayload(
                        symbol="STRICT_GUARD",
                        as_of_date=date(2026, 5, 14),
                        components=high_components,
                        diagnostic_scores=source_backed_bridge_diagnostics,
                        large_sector_id=large_sector_for_archetype(canonical_archetype_id),
                        canonical_archetype_id=canonical_archetype_id,
                    )
                    red_team = RedTeamAssessment.empty("STRICT_GUARD", date(2026, 5, 14))

                    with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                        score = DeterministicScorer().score(payload)
                    with patch("e2r.staging.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))

                    self.assertEqual(score.diagnostic_scores["archetype_green_policy_source_backed_override"], 0.0)
                    self.assertEqual(score.diagnostic_scores["archetype_green_restricted_by_profile"], 1.0)
                    self.assertNotEqual(stage.stage, Stage.STAGE_3_GREEN)

    def test_unknown_archetype_is_rejected_instead_of_fallback(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.json"
            profile_path.write_text(
                json.dumps(build_archetype_weight_profile_payload(), ensure_ascii=False),
                encoding="utf-8",
            )
            payload = ScoringPayload(
                symbol="UNKNOWN",
                as_of_date=date(2026, 5, 14),
                components=complete_components(eps_fcf_explosion=10.0),
                large_sector_id="L5_CONSUMER_BRAND_DISTRIBUTION",
                canonical_archetype_id="UNKNOWN_ARCHETYPE",
            )

            with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                with self.assertRaisesRegex(ArchetypeClassificationError, "unknown canonical_archetype_id"):
                    DeterministicScorer().score(payload)

    def test_missing_archetype_scope_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.json"
            profile_path.write_text(
                json.dumps(build_archetype_weight_profile_payload(), ensure_ascii=False),
                encoding="utf-8",
            )
            payload = ScoringPayload(
                symbol="NO_SCOPE",
                as_of_date=date(2026, 5, 14),
                components=complete_components(eps_fcf_explosion=10.0),
            )

            with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                with self.assertRaisesRegex(ArchetypeClassificationError, "large_sector_id is required"):
                    DeterministicScorer().score(payload)

    def test_unknown_canonical_archetype_does_not_fallback_to_large_sector(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.json"
            profile_path.write_text(
                json.dumps(build_archetype_weight_profile_payload(), ensure_ascii=False),
                encoding="utf-8",
            )
            payload = ScoringPayload(
                symbol="SECTOR_ONLY",
                as_of_date=date(2026, 5, 14),
                components=complete_components(eps_fcf_explosion=10.0),
                large_sector_id="L5_CONSUMER_BRAND_DISTRIBUTION",
                canonical_archetype_id="UNKNOWN_ARCHETYPE",
            )

            with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                with self.assertRaisesRegex(ArchetypeClassificationError, "unknown canonical_archetype_id"):
                    DeterministicScorer().score(payload)

    def test_large_sector_must_match_canonical_archetype(self):
        with tempfile.TemporaryDirectory() as tmp:
            profile_path = Path(tmp) / "profile.json"
            profile_path.write_text(
                json.dumps(build_archetype_weight_profile_payload(), ensure_ascii=False),
                encoding="utf-8",
            )
            payload = ScoringPayload(
                symbol="MISMATCH",
                as_of_date=date(2026, 5, 14),
                components=complete_components(eps_fcf_explosion=10.0),
                large_sector_id="L5_CONSUMER_BRAND_DISTRIBUTION",
                canonical_archetype_id="C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
            )

            with patch("e2r.scoring.get_active_scoring_profile", return_value=runtime_profile(profile_path)):
                with self.assertRaisesRegex(ArchetypeClassificationError, "does not match"):
                    DeterministicScorer().score(payload)


if __name__ == "__main__":
    unittest.main()
