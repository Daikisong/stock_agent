import json
import re
import unittest
from dataclasses import replace
from datetime import date
from pathlib import Path
from unittest.mock import patch

from e2r.agentic import LEGACY_DIRECT_RISK_FIELDS, V2_SCORE_ELIGIBLE_CLAIMS_KEY, load_evidence_contracts
from e2r.calibration.scoring_profile import (
    BASELINE_PROFILE_PATH,
    CALIBRATED_PROFILE_PATH,
    V2_2_PROFILE_PATH,
    load_scoring_profile,
)
from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS, large_sector_for_archetype
from e2r.features import DeterministicFeatureEngineer
from e2r.models import Stage
from e2r.red_team import RedTeamAssessment
from e2r.score_validity import score_state_contract_violations
from e2r.scoring import CANONICAL_SCORE_COMPONENTS, DeterministicScorer, ScoringPayload
from e2r.sector_profiles import profile_for_archetype
from e2r.stage_gate_diagnostics import diagnose_stage_gates
from e2r.staging import STAGE_3_GREEN_MIN_REVISION_SCORE, StageClassificationInput, StageClassifier
from tests.test_features import base_input


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CORE_RUNTIME_FILES = (
    "src/e2r/archetype_classifier.py",
    "src/e2r/sector_profiles.py",
    "src/e2r/features.py",
    "src/e2r/scoring.py",
    "src/e2r/staging.py",
    "src/e2r/stage_gate_diagnostics.py",
    "src/e2r/research/report_parser.py",
    "src/e2r/research/web_research_runner.py",
    "src/e2r/pipeline/korea_live_lite.py",
)
RUNTIME_HARDCODE_SCAN_PATHS = (
    "src/e2r/pipeline",
    "src/e2r/research",
    "src/e2r/agentic",
    "src/e2r/backtest",
    "src/e2r/archetype_classifier.py",
    "src/e2r/sector_profiles.py",
    "src/e2r/features.py",
    "src/e2r/scoring.py",
    "src/e2r/staging.py",
    "src/e2r/red_team.py",
    "src/e2r/stage_gate_diagnostics.py",
    "src/e2r/score_validity.py",
)


class RuntimeGeneralizationGuardTests(unittest.TestCase):
    def test_score_weights_and_stage_thresholds_are_frozen_while_evidence_os_is_repaired(self) -> None:
        expected_components = {
            "eps_fcf_explosion": 20.0,
            "earnings_visibility": 20.0,
            "bottleneck_pricing": 20.0,
            "market_mispricing": 15.0,
            "valuation_rerating": 15.0,
            "capital_allocation": 5.0,
            "information_confidence": 5.0,
        }
        expected_baseline_thresholds = {
            "stage2_total_min": 65.0,
            "stage2_eps_fcf_min": 10.0,
            "stage2_valuation_min": 7.0,
            "stage2_information_confidence_min": 3.0,
            "stage3_yellow_total_min": 80.0,
            "stage3_green_total_min": 85.0,
            "stage3_green_eps_fcf_min": 17.0,
            "stage3_green_visibility_min": 15.0,
            "stage3_green_bottleneck_min": 15.0,
            "stage3_green_mispricing_min": 10.0,
            "stage3_green_valuation_min": 10.0,
            "stage3_green_revision_min": 50.0,
            "stage3_green_structural_visibility_min": 45.0,
        }
        expected_calibrated_thresholds = {
            **expected_baseline_thresholds,
            "stage3_yellow_total_min": 75.0,
            "stage3_green_total_min": 87.0,
            "stage3_green_revision_min": 55.0,
        }

        self.assertEqual(
            {component.key: component.max_points for component in CANONICAL_SCORE_COMPONENTS},
            expected_components,
        )
        self.assertEqual(sum(expected_components.values()), 100.0)
        self.assertEqual(STAGE_3_GREEN_MIN_REVISION_SCORE, 50.0)
        self.assertEqual(load_scoring_profile(BASELINE_PROFILE_PATH).thresholds, expected_baseline_thresholds)
        self.assertEqual(load_scoring_profile(CALIBRATED_PROFILE_PATH).thresholds, expected_calibrated_thresholds)
        self.assertEqual(load_scoring_profile(V2_2_PROFILE_PATH).thresholds, expected_calibrated_thresholds)

    def test_operational_runtime_modules_do_not_hardcode_representative_winner_symbols(self) -> None:
        forbidden_terms = (
            "000660",
            "005930",
            "sk하이닉스",
            "sk hynix",
            "hynix",
            "삼성전자",
            "samsung electronics",
        )

        offenders: list[str] = []
        for relative_path in _runtime_hardcode_scan_files():
            text = (PROJECT_ROOT / relative_path).read_text(encoding="utf-8").lower()
            for term in forbidden_terms:
                if term in text:
                    offenders.append(f"{relative_path}:{term}")

        self.assertEqual(
            offenders,
            [],
            "대표 사례 종목명/코드는 fixture나 audit 문서에는 둘 수 있지만 core runtime route/score/stage에는 넣지 않는다.",
        )

    def test_classifier_haystacks_do_not_append_all_parsed_field_names(self) -> None:
        runtime_texts = {
            relative_path: (PROJECT_ROOT / relative_path).read_text(encoding="utf-8")
            for relative_path in (
                "src/e2r/archetype_classifier.py",
                "src/e2r/sector_profiles.py",
            )
        }
        broad_field_key_join = re.compile(
            r"for\s+key\s*,\s*value\s+in\s+parsed_fields\.items\(\).*str\(key\)",
            re.DOTALL,
        )

        for relative_path, text in runtime_texts.items():
            with self.subTest(relative_path=relative_path):
                self.assertNotIn("field_tokens", text)
                self.assertIsNone(
                    broad_field_key_join.search(text),
                    "parsed field 이름 전체를 텍스트 evidence처럼 haystack에 붙이면 아키타입 오분류가 재발한다.",
                )

    def test_every_canonical_archetype_reaches_runtime_score_with_consistent_scope(self) -> None:
        fields = {
            "financial_actuals_present": True,
            "actual_op_yoy_pct": 60,
            "actual_eps_yoy_pct": 60,
            "actual_sales_yoy_pct": 30,
            "opm_expansion_pctp": 5,
        }

        for canonical_archetype_id in CANONICAL_ARCHETYPE_IDS:
            with self.subTest(canonical_archetype_id=canonical_archetype_id):
                expected_large_sector = large_sector_for_archetype(canonical_archetype_id)
                expected_profile = profile_for_archetype(canonical_archetype_id)
                result = DeterministicFeatureEngineer().engineer(
                    replace(
                        base_input(fields),
                        large_sector_id=expected_large_sector,
                        canonical_archetype_id=canonical_archetype_id,
                    )
                )
                score = result.score()

                self.assertEqual(result.source_fields["large_sector_id"], expected_large_sector)
                self.assertEqual(result.source_fields["canonical_archetype_id"], canonical_archetype_id)
                self.assertEqual(result.source_fields["sector_profile"], expected_profile.value)
                self.assertEqual(score.diagnostic_scores["archetype_weight_profile_applied"], 1.0)
                self.assertIn(f"archetype_weight:{canonical_archetype_id}", score.scoring_version)

    def test_explicit_generic_archetype_scope_is_not_stolen_by_domain_field_names(self) -> None:
        fields = {
            "financial_actuals_present": True,
            "actual_op_yoy_pct": 90,
            "actual_eps_yoy_pct": 80,
            "actual_sales_yoy_pct": 35,
            "opm_expansion_pctp": 6,
            "hbm_demand_mentioned": True,
            "hbm_capacity_constraint": True,
            "regulatory_approval_confirmed": True,
            "approval_to_revenue_bridge": True,
        }
        generic_archetypes = (
            "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
            "C15_MATERIAL_SPREAD_SUPERCYCLE",
            "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
            "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
            "R13_CROSS_ARCHETYPE_4B_4C_REDTEAM",
            "R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION",
            "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
        )

        for canonical_archetype_id in generic_archetypes:
            with self.subTest(canonical_archetype_id=canonical_archetype_id):
                result = DeterministicFeatureEngineer().engineer(
                    replace(
                        base_input(fields),
                        large_sector_id=large_sector_for_archetype(canonical_archetype_id),
                        canonical_archetype_id=canonical_archetype_id,
                    )
                )

                self.assertNotEqual(result.source_fields["inferred_sector_profile"], "GENERIC")
                self.assertEqual(result.source_fields["sector_profile"], "GENERIC")
                self.assertEqual(result.source_fields["sector_profile_resolution"], "explicit_canonical_profile_override")

    def test_stage_classifier_and_gate_diagnostics_stay_in_parity_for_every_archetype(self) -> None:
        blocker_cases = {
            "clean": {},
            "report_date_missing": {"report_date_confidence": 0.0},
            "date_unverified_document": {"date_unverified_document_count_capped": 1.0},
            "date_unverified_snippet": {"date_unverified_snippet_news_count_capped": 1.0},
            "price_only_blowoff": {"price_only_blowoff_score": 80.0},
            "one_off_shortage": {"one_off_shortage_risk": 80.0},
            "revision_missing": {"revision_score": 0.0},
            "evidence_contract_guard_present": {
                "evidence_contract_guard_present_primitive_count_capped": 1.0,
            },
            "evidence_contract_guard_unverified": {
                "evidence_contract_guard_required_primitive_count_capped": 1.0,
                "evidence_contract_guard_missing_primitive_count_capped": 1.0,
            },
            "evidence_contract_green_gate_missing": {
                "evidence_contract_green_gate_required_primitive_count_capped": 3.0,
                "evidence_contract_green_gate_present_primitive_count_capped": 2.0,
                "evidence_contract_green_gate_missing_primitive_count_capped": 1.0,
                "evidence_contract_green_gate_coverage_pct": 66.6667,
            },
        }

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "rolling"}):
            for canonical_archetype_id in CANONICAL_ARCHETYPE_IDS:
                for case_name, diagnostic_overrides in blocker_cases.items():
                    with self.subTest(canonical_archetype_id=canonical_archetype_id, case_name=case_name):
                        score = _clean_green_score_for_archetype(
                            canonical_archetype_id,
                            diagnostic_overrides,
                            claim_backed_components=case_name == "evidence_contract_green_gate_missing",
                        )
                        red_team = RedTeamAssessment.empty(score.symbol, score.as_of_date)
                        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))
                        diagnostics = diagnose_stage_gates(score, red_team)

                        self.assertEqual(
                            diagnostics.stage3_green_gate_passed,
                            stage.stage == Stage.STAGE_3_GREEN,
                        )
                        if (
                            case_name == "clean"
                            and score.diagnostic_scores.get("archetype_green_restricted_by_profile", 0.0) <= 0.0
                        ):
                            self.assertEqual(stage.stage, Stage.STAGE_3_GREEN)
                            self.assertTrue(diagnostics.stage3_green_gate_passed)
                        if case_name == "evidence_contract_guard_present":
                            self.assertNotEqual(stage.stage, Stage.STAGE_3_GREEN)
                            self.assertIn(
                                "failed_evidence_contract_guard_present",
                                diagnostics.failed_gate_names,
                            )
                        if case_name == "evidence_contract_guard_unverified":
                            self.assertNotEqual(stage.stage, Stage.STAGE_3_GREEN)
                            self.assertIn(
                                "failed_evidence_contract_guard_unverified",
                                diagnostics.failed_gate_names,
                            )
                        if case_name == "evidence_contract_green_gate_missing":
                            self.assertNotEqual(stage.stage, Stage.STAGE_3_GREEN)
                            self.assertIn(
                                "failed_evidence_contract_positive_coverage",
                                diagnostics.failed_gate_names,
                            )

    def test_guard_cleared_does_not_make_guard_archetypes_permanently_yellow(self) -> None:
        guard_contracts = {
            archetype_id: contract
            for archetype_id, contract in load_evidence_contracts().items()
            if contract.guard_primitives
        }

        self.assertEqual(len(guard_contracts), 20)
        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "rolling"}):
            for canonical_archetype_id, contract in guard_contracts.items():
                with self.subTest(canonical_archetype_id=canonical_archetype_id):
                    clean_score = _clean_green_score_for_archetype(canonical_archetype_id)
                    clean_stage = StageClassifier().classify(
                        StageClassificationInput(
                            score=clean_score,
                            red_team=RedTeamAssessment.empty(clean_score.symbol, clean_score.as_of_date),
                        )
                    )
                    guard_count = float(len(contract.guard_primitives))
                    cleared_score = _clean_green_score_for_archetype(
                        canonical_archetype_id,
                        {
                            "evidence_contract_guard_required_primitive_count_capped": guard_count,
                            "evidence_contract_guard_present_primitive_count_capped": 0.0,
                            "evidence_contract_guard_cleared_primitive_count_capped": guard_count,
                            "evidence_contract_guard_missing_primitive_count_capped": 0.0,
                        },
                    )
                    red_team = RedTeamAssessment.empty(cleared_score.symbol, cleared_score.as_of_date)
                    cleared_stage = StageClassifier().classify(
                        StageClassificationInput(score=cleared_score, red_team=red_team)
                    )
                    diagnostics = diagnose_stage_gates(cleared_score, red_team)

                    self.assertNotIn("failed_evidence_contract_guard_present", diagnostics.failed_gate_names)
                    self.assertNotIn("failed_evidence_contract_guard_unverified", diagnostics.failed_gate_names)
                    if clean_stage.stage == Stage.STAGE_3_GREEN:
                        self.assertEqual(cleared_stage.stage, Stage.STAGE_3_GREEN)

    def test_claim_ledger_output_contract_applies_to_every_archetype(self) -> None:
        for canonical_archetype_id in CANONICAL_ARCHETYPE_IDS:
            with self.subTest(canonical_archetype_id=canonical_archetype_id):
                row = _complete_claim_ledger_score_row(canonical_archetype_id)

                self.assertNotIn(
                    "valid_high_confidence_claim_ledger_ids_missing",
                    score_state_contract_violations(row),
                )
                self.assertNotIn(
                    "valid_high_confidence_score_contribution_claim_ids_unknown",
                    score_state_contract_violations(row),
                )
                self.assertIn(
                    "valid_high_confidence_claim_ledger_ids_missing",
                    score_state_contract_violations({**row, "claim_ledger_claim_ids": ()}),
                )
                self.assertIn(
                    "valid_high_confidence_score_contribution_claim_ids_unknown",
                    score_state_contract_violations({**row, "claim_ledger_claim_ids": ("CLM-only-one-known",)}),
                )
                ledger_with_unknown_ref = {
                    **row,
                    "score_contribution_ledger": [
                        (
                            {**item, "support_claim_ids": ("CLM-ledger-ref-not-in-claim-ledger",)}
                            if index == 0
                            else dict(item)
                        )
                        for index, item in enumerate(row["score_contribution_ledger"])
                    ],
                }
                self.assertIn(
                    "valid_high_confidence_score_contribution_claim_ids_unknown",
                    score_state_contract_violations(ledger_with_unknown_ref),
                )

    def test_source_backed_orphan_score_is_invalid_for_every_archetype(self) -> None:
        diagnostics = {
            "source_backed_green_bridge_raw": 95.0,
            "claim_backed_claim_count_capped": 100.0,
            "cross_evidence_family_count": 4.0,
            "report_date_confidence": 100.0,
            "date_unverified_snippet_news_count_capped": 0.0,
            "date_unverified_document_count_capped": 0.0,
            "actual_profit_conversion_score": 90.0,
            "medium_term_revision_visibility": 90.0,
            "structural_visibility_quality": 95.0,
            "domain_specific_evidence_score": 95.0,
            "research_axis_bridge_present_count_capped": 6.0,
        }

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "rolling"}):
            for canonical_archetype_id in CANONICAL_ARCHETYPE_IDS:
                with self.subTest(canonical_archetype_id=canonical_archetype_id):
                    score = DeterministicScorer().score(
                        ScoringPayload(
                            symbol="SOURCE_BACKED_ORPHAN_CASE",
                            as_of_date=date(2026, 5, 14),
                            components={component.key: component.max_points for component in CANONICAL_SCORE_COMPONENTS},
                            diagnostic_scores=diagnostics,
                            large_sector_id=large_sector_for_archetype(canonical_archetype_id),
                            canonical_archetype_id=canonical_archetype_id,
                        )
                    )

                    self.assertEqual(score.total_score, 0.0)
                    self.assertEqual(score.diagnostic_scores["score_valid"], 0.0)
                    self.assertEqual(score.diagnostic_scores["score_claim_backed_required"], 100.0)
                    self.assertEqual(score.diagnostic_scores["score_blocked_by_orphan_score_contribution"], 100.0)
                    self.assertEqual(score.diagnostic_scores["score_claim_backed_component_ratio"], 0.0)
                    self.assertGreater(score.diagnostic_scores["orphan_score_component_count_capped"], 0.0)
                    self.assertNotIn("source_backed_green_total_floor_applied", score.diagnostic_scores)
                    self.assertTrue(all(item.raw_points == 0.0 for item in score.score_contribution_ledger))

    def test_source_backed_full_claim_score_remains_valid_for_every_archetype(self) -> None:
        components = {component.key: component.max_points for component in CANONICAL_SCORE_COMPONENTS}
        claim_ids = {key: (f"CLM-FULL-{key}",) for key in components}
        diagnostics = {
            "source_backed_green_bridge_raw": 95.0,
            "claim_backed_claim_count_capped": 100.0,
            "cross_evidence_family_count": 4.0,
            "report_date_confidence": 100.0,
            "date_unverified_snippet_news_count_capped": 0.0,
            "date_unverified_document_count_capped": 0.0,
            "actual_profit_conversion_score": 90.0,
            "medium_term_revision_visibility": 90.0,
            "structural_visibility_quality": 95.0,
            "domain_specific_evidence_score": 95.0,
            "research_axis_bridge_present_count_capped": 6.0,
        }

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "rolling"}):
            for canonical_archetype_id in CANONICAL_ARCHETYPE_IDS:
                with self.subTest(canonical_archetype_id=canonical_archetype_id):
                    score = DeterministicScorer().score(
                        ScoringPayload(
                            symbol="SOURCE_BACKED_FULL_CLAIM_CASE",
                            as_of_date=date(2026, 5, 14),
                            components=components,
                            diagnostic_scores=diagnostics,
                            score_contribution_claim_ids=claim_ids,
                            large_sector_id=large_sector_for_archetype(canonical_archetype_id),
                            canonical_archetype_id=canonical_archetype_id,
                        )
                    )

                    self.assertGreater(score.total_score, 0.0)
                    self.assertEqual(score.diagnostic_scores["score_valid"], 100.0)
                    self.assertEqual(score.diagnostic_scores["score_claim_backed_required"], 100.0)
                    self.assertNotIn("score_blocked_by_orphan_score_contribution", score.diagnostic_scores)
                    self.assertEqual(score.diagnostic_scores["score_claim_backed_component_ratio"], 100.0)
                    self.assertEqual(score.diagnostic_scores["orphan_score_component_count_capped"], 0.0)
                    self.assertEqual(set(score.score_contribution_claim_ids), set(components))
                    self.assertTrue(
                        all(
                            item.raw_points > 0.0 and item.support_claim_ids and item.cap_reason is None
                            for item in score.score_contribution_ledger
                        )
                    )

    def test_research_fixture_green_primitives_promote_without_symbol_special_case(self) -> None:
        fixture_archetypes = (
            "C02_POWER_GRID_DATACENTER_CAPEX",
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
            "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
        )

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "rolling"}):
            for canonical_archetype_id in fixture_archetypes:
                with self.subTest(canonical_archetype_id=canonical_archetype_id):
                    fixture = _green_runtime_fixture(canonical_archetype_id)
                    fields = _runtime_fields_from_research_fixture(fixture)
                    result = DeterministicFeatureEngineer().engineer(
                        replace(
                            base_input(fields),
                            large_sector_id=large_sector_for_archetype(canonical_archetype_id),
                            canonical_archetype_id=canonical_archetype_id,
                        )
                    )
                    score = result.score()
                    red_team = RedTeamAssessment.empty(score.symbol, score.as_of_date)
                    stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))
                    diagnostics = diagnose_stage_gates(score, red_team)

                    self.assertEqual(stage.stage, Stage.STAGE_3_GREEN)
                    self.assertTrue(diagnostics.stage3_green_gate_passed)
                    self.assertGreaterEqual(score.diagnostic_scores["source_backed_green_bridge_raw"], 90.0)
                    self.assertEqual(score.diagnostic_scores["research_axis_bridge_guard_risk_penalty_points"], 0.0)

    def test_research_fixture_guard_primitives_do_not_promote_green(self) -> None:
        guard_overrides = {
            "C02_POWER_GRID_DATACENTER_CAPEX": {
                "price_only_blowoff": True,
                "theme_hype_without_revenue": True,
                "missing_cashflow_bridge": True,
            },
            "C06_HBM_MEMORY_CUSTOMER_CAPACITY": {
                "qualification_lag_risk": True,
                "customer_preorder_or_allocation": False,
                "capacity_precommitted": False,
                "hbm_capacity_pre_sold": False,
            },
            "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE": {
                "missing_cashflow_bridge": True,
                "equipment_order_recovery": False,
                "order_to_revenue_bridge": False,
                "cycle_to_revenue_bridge": False,
            },
            "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION": {
                "repeat_order_confirmed": False,
                "channel_reorder_confirmed": False,
                "sell_through_confirmed": False,
                "theme_hype_without_revenue": True,
                "missing_cashflow_bridge": True,
            },
        }

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "rolling"}):
            for canonical_archetype_id, overrides in guard_overrides.items():
                with self.subTest(canonical_archetype_id=canonical_archetype_id):
                    fixture = _green_runtime_fixture(canonical_archetype_id)
                    guard = fixture["guard_fixture_candidate"]
                    self.assertFalse(guard["source_proxy_only"])
                    self.assertFalse(guard["evidence_url_pending"])
                    fields = _runtime_fields_from_research_fixture(fixture)
                    fields.update(overrides)
                    v2_guard_claims = {
                        key: (f"CLM-GUARD-{canonical_archetype_id}-{key}",)
                        for key, value in overrides.items()
                        if value is True and key in LEGACY_DIRECT_RISK_FIELDS
                    }
                    if v2_guard_claims:
                        fields[V2_SCORE_ELIGIBLE_CLAIMS_KEY] = v2_guard_claims
                    result = DeterministicFeatureEngineer().engineer(
                        replace(
                            base_input(fields),
                            large_sector_id=large_sector_for_archetype(canonical_archetype_id),
                            canonical_archetype_id=canonical_archetype_id,
                        )
                    )
                    score = result.score()
                    red_team = RedTeamAssessment.empty(score.symbol, score.as_of_date)
                    stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))
                    diagnostics = diagnose_stage_gates(score, red_team)

                    self.assertNotEqual(stage.stage, Stage.STAGE_3_GREEN)
                    self.assertFalse(diagnostics.stage3_green_gate_passed)
                    self.assertEqual(score.diagnostic_scores["source_backed_green_bridge_raw"], 0.0)
                    self.assertGreater(score.diagnostic_scores["research_axis_bridge_guard_risk_penalty_points"], 0.0)

    def test_malformed_stage3_diagnostics_fail_conservatively_for_every_archetype(self) -> None:
        malformed_cases = {
            "invalid_revision": ({"revision_score": "unknown"}, "failed_stage3_revision"),
            "invalid_report_date": ({"report_date_confidence": "unknown"}, "failed_report_date_confidence"),
            "nan_report_date": ({"report_date_confidence": float("nan")}, "failed_report_date_confidence"),
            "invalid_unverified_document_count": (
                {"date_unverified_document_count_capped": "unknown"},
                "failed_date_unverified_green_evidence",
            ),
            "nan_unverified_document_count": (
                {"date_unverified_document_count_capped": float("nan")},
                "failed_date_unverified_green_evidence",
            ),
            "invalid_contract_required_quality": (
                {"contract_required_for_green": 1.0, "contract_quality": "unknown"},
                "failed_stage3_contract_quality",
            ),
            "nan_contract_required_quality": (
                {"contract_required_for_green": 1.0, "contract_quality": float("nan")},
                "failed_stage3_contract_quality",
            ),
            "invalid_weighted_bottleneck_threshold": (
                {
                    "archetype_weight_bottleneck_pricing": "unknown",
                    "archetype_component_bottleneck_pricing": 1.0,
                },
                "failed_stage3_bottleneck",
            ),
        }

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "rolling"}):
            for canonical_archetype_id in CANONICAL_ARCHETYPE_IDS:
                for case_name, (diagnostic_overrides, expected_gate) in malformed_cases.items():
                    with self.subTest(canonical_archetype_id=canonical_archetype_id, case_name=case_name):
                        score = _clean_green_score_for_archetype(canonical_archetype_id)
                        _replace_score_diagnostics(score, diagnostic_overrides)
                        red_team = RedTeamAssessment.empty(score.symbol, score.as_of_date)
                        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))
                        diagnostics = diagnose_stage_gates(score, red_team)

                        self.assertEqual(
                            diagnostics.stage3_green_gate_passed,
                            stage.stage == Stage.STAGE_3_GREEN,
                        )
                        self.assertNotEqual(stage.stage, Stage.STAGE_3_GREEN)
                        self.assertIn(expected_gate, diagnostics.failed_gate_names)

    def test_stage2_classifier_and_gate_diagnostics_stay_in_parity_for_every_archetype(self) -> None:
        cases = {
            "clean_stage2": (0.70, {}),
            "total_missing": (0.60, {}),
            "eps_missing": (0.70, {"eps_fcf_explosion": 4.0}),
            "valuation_missing": (0.70, {"valuation_rerating": 2.0}),
            "information_missing": (0.70, {"information_confidence": 1.0}),
            "price_only_blowoff": (0.70, {"price_only_blowoff_score": 80.0}),
        }

        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "rolling"}):
            for canonical_archetype_id in CANONICAL_ARCHETYPE_IDS:
                for case_name, (component_ratio, overrides) in cases.items():
                    with self.subTest(canonical_archetype_id=canonical_archetype_id, case_name=case_name):
                        score = _stage2_band_score_for_archetype(
                            canonical_archetype_id,
                            component_ratio=component_ratio,
                            overrides=overrides,
                        )
                        red_team = RedTeamAssessment.empty(score.symbol, score.as_of_date)
                        stage = StageClassifier().classify(StageClassificationInput(score=score, red_team=red_team))
                        diagnostics = diagnose_stage_gates(score, red_team)

                        self.assertEqual(
                            diagnostics.stage2_gate_passed,
                            stage.stage == Stage.STAGE_2,
                        )
                        if case_name == "clean_stage2":
                            self.assertEqual(score.total_score, 70.0)
                            self.assertEqual(stage.stage, Stage.STAGE_2)
                            self.assertTrue(diagnostics.stage2_gate_passed)

    def test_calibration_risk_penalties_score_for_every_archetype(self) -> None:
        with patch.dict("os.environ", {"E2R_SCORING_PROFILE": "rolling"}):
            for canonical_archetype_id in CANONICAL_ARCHETYPE_IDS:
                with self.subTest(canonical_archetype_id=canonical_archetype_id):
                    clean_score = _stage2_band_score_for_archetype(
                        canonical_archetype_id,
                        component_ratio=0.70,
                    )
                    risk_adjusted_score = _stage2_band_score_for_archetype(
                        canonical_archetype_id,
                        component_ratio=0.70,
                        overrides={
                            "high_mae_risk": 100.0,
                            "stage2_actionable_volatility_risk": 100.0,
                        },
                    )

                    self.assertEqual(risk_adjusted_score.total_score, max(0.0, clean_score.total_score - 4.0))
                    self.assertEqual(risk_adjusted_score.diagnostic_scores["calibration_total_adjustment"], -4.0)


def _clean_green_score_for_archetype(
    canonical_archetype_id: str,
    diagnostic_overrides: dict[str, object] | None = None,
    *,
    claim_backed_components: bool = False,
):
    diagnostics = {
        "revision_score": 100.0,
        "structural_visibility_quality": 100.0,
        "contract_quality": 100.0,
        "contract_required_for_green": 0.0,
        "one_off_shortage_risk": 0.0,
        "price_only_blowoff_score": 0.0,
        "report_date_confidence": 100.0,
        "date_unverified_snippet_news_count_capped": 0.0,
        "date_unverified_document_count_capped": 0.0,
        "cross_evidence_family_count": 4.0,
        "actual_profit_conversion_score": 100.0,
        "fcf_quality_score": 100.0,
        "domain_specific_evidence_score": 100.0,
        "green_unlock_evidence_score": 100.0,
        "research_axis_bridge_present_count_capped": 5.0,
        "research_axis_bridge_margin": 100.0,
        "research_axis_bridge_capital_return": 100.0,
        "research_axis_bridge_bio_commercialization": 100.0,
    }
    diagnostics.update(diagnostic_overrides or {})
    return DeterministicScorer().score(
        ScoringPayload(
            symbol="GENERALIZATION_CASE",
            as_of_date=date(2026, 5, 14),
            components={component.key: component.max_points for component in CANONICAL_SCORE_COMPONENTS},
            diagnostic_scores=diagnostics,
            score_contribution_claim_ids=(
                {component.key: (f"CLM-{component.key}",) for component in CANONICAL_SCORE_COMPONENTS}
                if claim_backed_components
                else {}
            ),
            large_sector_id=large_sector_for_archetype(canonical_archetype_id),
            canonical_archetype_id=canonical_archetype_id,
        )
    )


def _complete_claim_ledger_score_row(canonical_archetype_id: str) -> dict[str, object]:
    component_claims = {
        component.key: (f"CLM-{canonical_archetype_id}-{component.key}",)
        for component in CANONICAL_SCORE_COMPONENTS
    }
    claim_ids = tuple(claim_id for claim_group in component_claims.values() for claim_id in claim_group)
    return {
        "symbol": "GENERALIZATION_CASE",
        "as_of_date": "2026-05-14",
        "stage": "3-Green",
        "visible_score": 92.0,
        "score_valid": True,
        "canonical_archetype_id": canonical_archetype_id,
        "evidence_contract_required_primitive_count": 1,
        "claim_backed_claim_count": float(len(claim_ids)),
        "score_claim_backed_component_ratio": 100.0,
        "orphan_score_component_count": 0.0,
        "claim_ledger_claim_ids": claim_ids,
        "score_contribution_claim_ids": component_claims,
        "score_contribution_ledger": [
            {
                "component_key": component.key,
                "raw_points": component.max_points,
                "max_points": component.max_points,
                "support_claim_ids": list(component_claims[component.key]),
            }
            for component in CANONICAL_SCORE_COMPONENTS
        ],
        **{f"{component.key}_score": component.max_points for component in CANONICAL_SCORE_COMPONENTS},
    }


def _runtime_hardcode_scan_files() -> tuple[str, ...]:
    files: list[str] = []
    for relative_path in RUNTIME_HARDCODE_SCAN_PATHS:
        path = PROJECT_ROOT / relative_path
        if path.is_file():
            files.append(relative_path)
            continue
        files.extend(str(item.relative_to(PROJECT_ROOT)) for item in sorted(path.rglob("*.py")))
    return tuple(dict.fromkeys(files))


def _green_runtime_fixture(canonical_archetype_id: str) -> dict[str, object]:
    path = PROJECT_ROOT / "docs/0619/v12_green_runtime_fixture_candidates_2026-06-19.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    for item in data["archetypes"]:
        if item["canonical_archetype_id"] == canonical_archetype_id:
            green = item["green_fixture_candidate"]
            source_file = PROJECT_ROOT / green["source_file"]
            if not source_file.exists():
                raise AssertionError(f"missing research source file: {green['source_file']}")
            if green["source_proxy_only"] or green["evidence_url_pending"]:
                raise AssertionError(f"green fixture is not source-backed enough: {canonical_archetype_id}")
            return item
    raise AssertionError(f"missing fixture archetype: {canonical_archetype_id}")


def _runtime_fields_from_research_fixture(fixture: dict[str, object]) -> dict[str, object]:
    fields = {
        "financial_actuals_present": True,
        "actual_op_yoy_pct": 90,
        "actual_eps_yoy_pct": 80,
        "actual_sales_yoy_pct": 45,
        "actual_fcf_yoy_pct": 40,
        "opm_expansion_pctp": 7,
        "fcf_growth_pct": 40,
        "eps_revision_pct": 45,
        "op_revision_pct": 45,
        "fcf_revision_pct": 35,
        "target_price_revision_pct": 40,
        "target_multiple_delta": 5,
        "fy1_op": 100,
        "fy2_op": 185,
        "fy1_eps": 100,
        "fy2_eps": 180,
        "estimate_upgrade_mentioned": True,
    }
    for primitive in fixture.get("expected_runtime_primitives", ()):
        _apply_research_primitive(fields, str(primitive))
    green = fixture["green_fixture_candidate"]
    trigger = _source_trigger_row(green)
    for phrase in trigger.get("stage2_evidence_fields", ()):
        _apply_research_evidence_phrase(fields, str(phrase))
    for phrase in trigger.get("stage3_evidence_fields", ()):
        _apply_research_evidence_phrase(fields, str(phrase))
    if trigger.get("evidence_available_at_that_date"):
        _apply_research_evidence_phrase(fields, str(trigger["evidence_available_at_that_date"]))
    if trigger.get("notes"):
        _apply_research_evidence_phrase(fields, str(trigger["notes"]))
    return fields


def _source_trigger_row(candidate: dict[str, object]) -> dict[str, object]:
    source_path = PROJECT_ROOT / str(candidate["source_file"])
    wanted_trigger_id = candidate.get("trigger_id")
    wanted_case_id = candidate.get("case_id")
    for line in source_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if row.get("row_type") != "trigger":
            continue
        if wanted_trigger_id and row.get("trigger_id") == wanted_trigger_id:
            return row
        if wanted_case_id and row.get("case_id") == wanted_case_id:
            return row
    raise AssertionError(f"missing trigger row for {wanted_trigger_id or wanted_case_id}")


def _apply_research_primitive(fields: dict[str, object], primitive: str) -> None:
    if primitive == "order_backlog_to_sales":
        fields["order_backlog_to_sales"] = 1.4
        fields["record_backlog"] = True
        fields["backlog_visibility"] = True
        return
    if primitive == "export_growth_pct":
        fields["export_growth_pct"] = 80
        fields["export_growth_mentioned"] = True
        return
    if primitive == "medium_term_revision_visibility":
        fields["estimate_upgrade_mentioned"] = True
        return
    if primitive == "fcf_quality_score":
        fields["actual_fcf_yoy_pct"] = 60
        fields["fcf_growth_pct"] = 60
        return
    fields[primitive] = True


def _apply_research_evidence_phrase(fields: dict[str, object], phrase: str) -> None:
    lowered = phrase.lower()
    if "backlog" in lowered or "수주잔고" in phrase or "named backlog" in lowered:
        fields["record_backlog"] = True
        fields["backlog_visibility"] = True
        fields.setdefault("order_backlog_to_sales", 1.0)
    if "delivery" in lowered or "revenue" in lowered or "매출 전환" in phrase:
        fields["delivery_schedule"] = True
        fields["order_to_revenue_bridge"] = True
        fields["revenue_recognition_path"] = True
    if "margin" in lowered or "마진" in phrase or "profit" in lowered or "이익" in phrase:
        fields["margin_bridge_visible"] = True
        fields["high_margin_mix_improvement"] = True
        fields["pricing_power_confirmed"] = True
    if "customer" in lowered or "고객" in phrase or "nvidia" in lowered or "global customers" in lowered:
        fields["named_customer_quality"] = True
        fields["customer_quality_visible"] = True
    if "datacenter" in lowered or "data center" in lowered or "데이터센터" in phrase:
        fields["datacenter_customer"] = True
        fields["data_center_contract"] = True
        fields["power_capacity_constraint"] = True
    if "capacity" in lowered or "allocation" in lowered or "sold-out" in lowered or "완판" in phrase:
        fields["capacity_constraint"] = True
        fields["capacity_precommitted"] = True
        fields["booked_out_capacity"] = True
        fields["customer_preorder_or_allocation"] = True
    if "hbm" in lowered:
        fields["hbm_demand_mentioned"] = True
        fields["hbm_capacity_constraint"] = True
    if "revision" in lowered or "confirmed_revision" in lowered:
        fields["estimate_upgrade_mentioned"] = True
    if "sellthrough" in lowered or "sell-through" in lowered or "reorder" in lowered or "리오더" in phrase:
        fields["sell_through_confirmed"] = True
        fields["repeat_order_confirmed"] = True
        fields["channel_reorder_confirmed"] = True
    if "distribution" in lowered or "channel" in lowered or "유통" in phrase or "해외" in phrase:
        fields["platform_distribution_scale"] = True
        fields["export_channel_expansion"] = True
        fields["overseas_channel_expansion"] = True
        fields["channel_expansion"] = True
    if "brand" in lowered or "indie" in lowered:
        fields["brand_customer_diversification"] = True
    if "order" in lowered or "수주" in phrase:
        fields["equipment_order_recovery"] = True
        fields["equipment_order_backlog"] = True


def _replace_score_diagnostics(score, diagnostic_overrides: dict[str, object]) -> None:
    diagnostics = dict(score.diagnostic_scores)
    diagnostics.update(diagnostic_overrides)
    object.__setattr__(score, "diagnostic_scores", diagnostics)


def _stage2_band_score_for_archetype(
    canonical_archetype_id: str,
    *,
    component_ratio: float,
    overrides: dict[str, object] | None = None,
):
    components = {component.key: component.max_points * component_ratio for component in CANONICAL_SCORE_COMPONENTS}
    diagnostic_overrides = dict(overrides or {})
    for key in tuple(diagnostic_overrides):
        if key in components:
            components[key] = diagnostic_overrides.pop(key)
    diagnostics = {
        "revision_score": 10.0,
        "structural_visibility_quality": 10.0,
        "contract_quality": 10.0,
        "one_off_shortage_risk": 0.0,
        "price_only_blowoff_score": 0.0,
        "cross_evidence_family_count": 3.0,
        "evidence_family_financial_actual": 1.0,
        "evidence_family_disclosure": 1.0,
        "evidence_family_news": 1.0,
    }
    diagnostics.update(diagnostic_overrides)
    return DeterministicScorer().score(
        ScoringPayload(
            symbol="GENERALIZATION_STAGE2_CASE",
            as_of_date=date(2026, 5, 14),
            components=components,
            diagnostic_scores=diagnostics,
            large_sector_id=large_sector_for_archetype(canonical_archetype_id),
            canonical_archetype_id=canonical_archetype_id,
        )
    )


if __name__ == "__main__":
    unittest.main()
