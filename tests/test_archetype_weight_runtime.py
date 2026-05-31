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
