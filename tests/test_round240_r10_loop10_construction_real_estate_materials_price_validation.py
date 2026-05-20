from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round240_r10_loop10_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round240_r10_loop10_construction_real_estate_materials_price_validation import (
    ROUND240_CASE_CANDIDATES,
    ROUND240_GREEN_FORBIDDEN_PATTERNS,
    ROUND240_GREEN_REQUIRED_FIELDS,
    ROUND240_HARD_4C_GATES,
    ROUND240_PRICE_VALIDATION_FIELDS,
    ROUND240_REQUIRED_TARGET_ALIASES,
    ROUND240_SCORE_ADJUSTMENTS,
    ROUND240_SHADOW_WEIGHT_ROWS,
    ROUND240_STAGE4B_WATCH_TRIGGERS,
    render_round240_green_gate_review_markdown,
    render_round240_stage4b_4c_review_markdown,
    round240_audit_payload,
    round240_case_records,
    round240_case_rows,
    round240_summary,
    write_round240_r10_loop10_reports,
)


class Round240R10Loop10ConstructionRealEstateMaterialsPriceValidationTests(unittest.TestCase):
    def test_round240_targets_map_to_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND240_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND240_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND240_REQUIRED_TARGET_ALIASES["NUCLEAR_INFRA_EPC_EXPORT"],
            E2RArchetype.NUCLEAR_INFRA_EPC_EXPORT.value,
        )
        self.assertEqual(
            ROUND240_REQUIRED_TARGET_ALIASES["CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C"],
            E2RArchetype.CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C.value,
        )
        self.assertEqual(
            ROUND240_REQUIRED_TARGET_ALIASES["EVIDENCE_GOOD_BUT_PRICE_UNPROVEN"],
            E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_UNPROVEN.value,
        )

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round240_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)

        summary = round240_summary()
        self.assertEqual(summary["analyst_round_id"], "round_168")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertEqual(summary["hard_4c_case_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_new_r10_archetype_definitions_are_available(self) -> None:
        nuclear = archetype_definition(E2RArchetype.NUCLEAR_INFRA_EPC_EXPORT)
        pf = archetype_definition(E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK)
        safety = archetype_definition(E2RArchetype.CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C)
        data_center = archetype_definition(E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT)

        self.assertIn("listed-company package amount", nuclear.stage3_high_conviction_signals)
        self.assertIn("PF workout", pf.stage4c_thesis_break_signals)
        self.assertIn("not a Green source; PF credit break is a 4C gate", pf.stage3_high_conviction_signals)
        self.assertIn("fatal construction accident", safety.stage4c_thesis_break_signals)
        self.assertIn("tenant contract", data_center.stage3_high_conviction_signals)
        self.assertIn("data-center label without tenant", data_center.false_positive_patterns)

    def test_czech_nuclear_and_daewoo_port_are_stage2_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND240_CASE_CANDIDATES}
        nuclear = by_id["r10_loop10_czech_nuclear_infra_korea_epc"]
        daewoo = by_id["r10_loop10_daewoo_enc_grand_faw_port_delivery"]

        self.assertEqual(nuclear.primary_archetype, E2RArchetype.NUCLEAR_INFRA_EPC_EXPORT)
        self.assertEqual(nuclear.stage1_date.isoformat(), "2024-07-17")
        self.assertEqual(nuclear.stage2_date.isoformat(), "2025-06-04")
        self.assertEqual(nuclear.stage4c_date.isoformat(), "2025-05-06")
        self.assertIsNone(nuclear.stage3_date)
        self.assertEqual(nuclear.extra_price_metrics["doosan_3m_mfe_pct"], 48.0)
        self.assertEqual(nuclear.extra_price_metrics["kepco_ec_3m_mfe_pct"], 41.0)
        self.assertEqual(nuclear.extra_price_metrics["czech_contract_value_usd_bn"], 18.7)
        self.assertIn("margin_unverified", nuclear.red_flag_fields)

        self.assertEqual(daewoo.primary_archetype, E2RArchetype.PORT_INFRA_DELIVERY)
        self.assertEqual(daewoo.stage2_date.isoformat(), "2024-11-12")
        self.assertEqual(daewoo.extra_price_metrics["completed_docks"], 5.0)
        self.assertEqual(daewoo.extra_price_metrics["maximum_capacity_target_mn_containers"], 3.5)
        self.assertEqual(daewoo.extra_price_metrics["development_road_project_value_usd_bn"], 17.0)
        self.assertIn("cash_collection_unverified", daewoo.red_flag_fields)

    def test_housing_policy_and_ai_data_center_are_event_premium_until_cashflow(self) -> None:
        by_id = {case.case_id: case for case in ROUND240_CASE_CANDIDATES}
        housing = by_id["r10_loop10_seoul_housing_policy_supply_watch"]
        data_center = by_id["r10_loop10_ai_data_center_real_asset_event"]

        self.assertEqual(housing.primary_archetype, E2RArchetype.HOUSING_POLICY_SUPPLY_EVENT)
        self.assertEqual(housing.case_type, "event_premium")
        self.assertEqual(housing.extra_price_metrics["ltv_before_pct"], 50.0)
        self.assertEqual(housing.extra_price_metrics["ltv_after_pct"], 40.0)
        self.assertEqual(housing.extra_price_metrics["ltv_reduction_relative_pct"], -20.0)
        self.assertEqual(housing.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("housing_supply_policy_only", housing.red_flag_fields)

        self.assertEqual(data_center.primary_archetype, E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT)
        self.assertEqual(data_center.stage4b_date.isoformat(), "2025-06-20")
        self.assertEqual(data_center.extra_price_metrics["sk_aws_investment_krw_trn"], 7.0)
        self.assertEqual(data_center.extra_price_metrics["initial_capacity_mw"], 100.0)
        self.assertEqual(data_center.extra_price_metrics["capacity_expansion_potential_multiple"], 10.0)
        self.assertEqual(data_center.extra_price_metrics["kakao_event_mfe_pct"], 11.0)
        self.assertIn("data_center_theme_without_tenant", data_center.red_flag_fields)

    def test_pf_and_construction_safety_cases_are_hard_4c(self) -> None:
        by_id = {case.case_id: case for case in ROUND240_CASE_CANDIDATES}
        pf = by_id["r10_loop10_taeyoung_pf_credit_hard_4c"]
        bridge = by_id["r10_loop10_hyundai_engineering_bridge_collapse_sector_hard_4c"]

        self.assertEqual(pf.primary_archetype, E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK)
        self.assertTrue(pf.hard_4c_confirmed)
        self.assertEqual(pf.stage4c_date.isoformat(), "2024-05-13")
        self.assertEqual(pf.extra_price_metrics["pf_delinquency_2021_pct"], 0.37)
        self.assertEqual(pf.extra_price_metrics["pf_delinquency_2023_pct"], 2.70)
        self.assertEqual(pf.extra_price_metrics["pf_delinquency_increase_2021_to_2023_pct"], 629.7)
        self.assertEqual(pf.extra_price_metrics["government_support_package_krw_trn"], 40.6)
        self.assertIn("pf_workout_or_debt_reschedule", pf.red_flag_fields)

        self.assertEqual(bridge.primary_archetype, E2RArchetype.CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C)
        self.assertTrue(bridge.hard_4c_confirmed)
        self.assertEqual(bridge.stage4c_date.isoformat(), "2025-02-25")
        self.assertEqual(bridge.extra_price_metrics["fatalities"], 4.0)
        self.assertEqual(bridge.extra_price_metrics["injuries"], 6.0)
        self.assertEqual(bridge.extra_price_metrics["workers_fell"], 10.0)
        self.assertEqual(bridge.price_validation_status, "not_direct_listed_stock_price_unavailable")
        self.assertIn("fatal_construction_accident", bridge.red_flag_fields)

    def test_safety_regulation_and_rebar_weakness_are_4c_watch(self) -> None:
        by_id = {case.case_id: case for case in ROUND240_CASE_CANDIDATES}
        safety = by_id["r10_loop10_posco_dl_construction_safety_regulation"]
        rebar = by_id["r10_loop10_hyundai_steel_rebar_construction_demand_watch"]

        self.assertEqual(safety.primary_archetype, E2RArchetype.WORKPLACE_FATALITY_REGULATORY_4C)
        self.assertFalse(safety.hard_4c_confirmed)
        self.assertEqual(safety.extra_price_metrics["posco_ec_sites_halted"], 103.0)
        self.assertEqual(safety.extra_price_metrics["dl_construction_executives_resigned"], 80.0)
        self.assertEqual(safety.extra_price_metrics["proposed_fine_pct_of_operating_profit"], 5.0)
        self.assertIn("license_revocation_risk", safety.red_flag_fields)

        self.assertEqual(rebar.primary_archetype, E2RArchetype.BUILDING_MATERIALS_DEMAND_CYCLE)
        self.assertFalse(rebar.hard_4c_confirmed)
        self.assertEqual(rebar.stage4c_price_anchor, 29000.0)
        self.assertEqual(rebar.mae_1d, -1.2)
        self.assertEqual(rebar.extra_price_metrics["net_profit_forecast_cut_pct"], -73.0)
        self.assertEqual(rebar.extra_price_metrics["implied_prior_net_profit_forecast_krw_bn"], 796.3)
        self.assertEqual(rebar.extra_price_metrics["rebar_price_expected_decline_pct"], -10.0)
        self.assertIn("building_material_demand_weakness", rebar.red_flag_fields)

    def test_green_gate_4b_4c_and_shadow_weights_are_explicit(self) -> None:
        required = set(ROUND240_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND240_GREEN_FORBIDDEN_PATTERNS)
        review = render_round240_green_gate_review_markdown()
        stage_review = render_round240_stage4b_4c_review_markdown()
        weights = {row.archetype: row for row in ROUND240_SHADOW_WEIGHT_ROWS}

        self.assertIn("cash_flow_after_working_capital", required)
        self.assertIn("margin_or_noi_affo_visibility", required)
        self.assertIn("preferred_bidder_only", forbidden)
        self.assertIn("safety_accident_or_fatality", forbidden)
        self.assertIn("pf_workout_or_debt_reschedule", ROUND240_HARD_4C_GATES)
        self.assertIn("fatal_construction_accident", ROUND240_HARD_4C_GATES)
        self.assertIn("data_center_theme_rally_before_tenant_noi_affo", ROUND240_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("r10_loop10_hyundai_engineering_bridge_collapse_sector_hard_4c", stage_review)
        self.assertEqual(weights[E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK].hard_4c_sensitivity, 5)
        self.assertEqual(weights[E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT].event_penalty, -5)

    def test_price_fields_and_score_axes_cover_r10_loop10(self) -> None:
        fields = set(ROUND240_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND240_SCORE_ADJUSTMENTS}

        self.assertIn("pf_or_safety_anchor", fields)
        self.assertIn("tenant_or_noi_affo_anchor", fields)
        self.assertIn("cash_flow_after_working_capital", axes)
        self.assertIn("tenant_contract_quality", axes)
        self.assertIn("PF_relief_policy_only", axes)
        self.assertIn("workplace_fatality_repeated", axes)

    def test_audit_payload_marks_non_production_round(self) -> None:
        audit = round240_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_240.md")
        self.assertEqual(audit["analyst_round_id"], "round_168")
        self.assertEqual(audit["large_sector"], Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("keep_pf_credit_break_and_fatal_construction_accident_as_hard_4c_references", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round240_r10_loop10_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round240_case_rows()
            self.assertEqual(len(records), len(ROUND240_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND240_CASE_CANDIDATES))
            self.assertIn("현대엔지니어링", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("PF_relief_policy_only", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("fatal_construction_accident", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(rows[3]["round_score_price_alignment"], "thesis_break")
            self.assertEqual(json.loads(rows[4]["extra_price_metrics"])["fatalities"], 4.0)


if __name__ == "__main__":
    unittest.main()
