from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round253_r10_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round253_r10_loop11_construction_real_estate_materials_price_validation import (
    ROUND253_CASE_CANDIDATES,
    ROUND253_DEEP_SUB_ARCHETYPES,
    ROUND253_GREEN_FORBIDDEN_PATTERNS,
    ROUND253_GREEN_REQUIRED_FIELDS,
    ROUND253_HARD_4C_GATES,
    ROUND253_LARGE_SECTOR,
    ROUND253_PRICE_VALIDATION_FIELDS,
    ROUND253_REQUIRED_TARGET_ALIASES,
    ROUND253_SCORE_ADJUSTMENTS,
    ROUND253_SHADOW_WEIGHT_ROWS,
    ROUND253_STAGE4B_WATCH_TRIGGERS,
    render_round253_green_gate_review_markdown,
    render_round253_stage4b_4c_review_markdown,
    round253_audit_payload,
    round253_case_records,
    round253_case_rows,
    round253_deep_sub_archetype_rows,
    round253_shadow_weight_rows,
    round253_summary,
    write_round253_r10_loop11_reports,
)


class Round253R10Loop11ConstructionRealEstateMaterialsPriceValidationTests(unittest.TestCase):
    def test_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND253_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND253_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND253_REQUIRED_TARGET_ALIASES["OVERSEAS_EPC_MEGA_ORDER"],
            E2RArchetype.OVERSEAS_EPC_MEGA_ORDER.value,
        )
        self.assertEqual(
            ROUND253_REQUIRED_TARGET_ALIASES["GAS_INFRA_DELIVERY_VALIDATION"],
            E2RArchetype.GAS_INFRA_DELIVERY_VALIDATION.value,
        )
        self.assertEqual(
            ROUND253_REQUIRED_TARGET_ALIASES["AI_DATA_CENTER_REAL_ASSET"],
            E2RArchetype.AI_DATA_CENTER_REAL_ASSET.value,
        )
        self.assertEqual(
            ROUND253_REQUIRED_TARGET_ALIASES["CONSTRUCTION_SAFETY_REGULATORY_4C"],
            E2RArchetype.CONSTRUCTION_SAFETY_REGULATORY_4C.value,
        )

    def test_archetype_definitions_capture_round253_gates(self) -> None:
        overseas = archetype_definition(E2RArchetype.OVERSEAS_EPC_MEGA_ORDER)
        gas = archetype_definition(E2RArchetype.GAS_INFRA_DELIVERY_VALIDATION)
        ai_dc = archetype_definition(E2RArchetype.AI_DATA_CENTER_REAL_ASSET)
        safety = archetype_definition(E2RArchetype.CONSTRUCTION_SAFETY_REGULATORY_4C)

        self.assertIn("progress revenue", overseas.stage3_high_conviction_signals)
        self.assertIn("working-capital control", overseas.stage3_high_conviction_signals)
        self.assertIn("company-level package margin", gas.stage3_high_conviction_signals)
        self.assertIn("Saudi payment risk", gas.stage4c_thesis_break_signals)
        self.assertIn("tenant contract", ai_dc.stage3_high_conviction_signals)
        self.assertIn("power/water/permitting failure", ai_dc.stage4c_thesis_break_signals)
        self.assertIn("license revocation risk", safety.stage4c_thesis_break_signals)
        self.assertIn("safety regulation is a Green blocker", safety.stage3_high_conviction_signals)

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round253_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_contract_policy_data_center_pf_relief_or_safety_headline_as_green", record.green_guardrails)

        summary = round253_summary()
        self.assertEqual(summary["analyst_round_id"], "round_181")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["stage4c_watch_count"], 2)
        self.assertEqual(summary["thesis_break_watch_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_epc_gas_ai_and_port_cases_are_stage2_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND253_CASE_CANDIDATES}
        samsung = by_id["r10_loop11_samsung_ea_fadhili_epc_4b"]
        hyundai = by_id["r10_loop11_hyundai_enc_jafurah_gas_infra"]
        ai_dc = by_id["r10_loop11_ai_data_center_real_asset"]
        daewoo = by_id["r10_loop11_daewoo_enc_grand_faw_port_delivery"]

        self.assertEqual(samsung.primary_archetype, E2RArchetype.OVERSEAS_EPC_MEGA_ORDER)
        self.assertEqual(samsung.stage2_date.isoformat(), "2024-04-03")
        self.assertEqual(samsung.stage4b_date.isoformat(), "2024-04-03")
        self.assertIsNone(samsung.stage3_date)
        self.assertEqual(samsung.stage2_price_anchor, 26750.0)
        self.assertEqual(samsung.mfe_1d, 8.5)
        self.assertEqual(samsung.extra_price_metrics["contract_value_usd_bn"], 6.0)
        self.assertEqual(samsung.extra_price_metrics["contract_share_of_total_pct"], 77.9)
        self.assertEqual(samsung.extra_price_metrics["capacity_increase_pct"], 60.0)
        self.assertIn("cash_collection_unverified", samsung.red_flag_fields)

        self.assertEqual(hyundai.primary_archetype, E2RArchetype.GAS_INFRA_DELIVERY_VALIDATION)
        self.assertEqual(hyundai.stage2_date.isoformat(), "2024-06-30")
        self.assertEqual(hyundai.extra_price_metrics["aramco_contract_package_usd_bn"], 25.0)
        self.assertEqual(hyundai.extra_price_metrics["jafurah_raw_gas_reserves_tcf"], 229.0)
        self.assertEqual(hyundai.extra_price_metrics["first_phase_vs_2030_target_pct"], 22.5)
        self.assertEqual(hyundai.extra_price_metrics["main_gas_network_addition_km"], 4000.0)
        self.assertIn("company_package_unverified", hyundai.red_flag_fields)

        self.assertEqual(ai_dc.primary_archetype, E2RArchetype.AI_DATA_CENTER_REAL_ASSET)
        self.assertEqual(ai_dc.stage4b_date.isoformat(), "2025-06-20")
        self.assertEqual(ai_dc.extra_price_metrics["sk_aws_investment_krw_trn"], 7.0)
        self.assertEqual(ai_dc.extra_price_metrics["aws_component_usd_bn"], 4.0)
        self.assertEqual(ai_dc.extra_price_metrics["initial_capacity_mw"], 100.0)
        self.assertEqual(ai_dc.extra_price_metrics["capacity_expansion_multiple"], 10.0)
        self.assertIn("data_center_theme_without_tenant", ai_dc.red_flag_fields)

        self.assertEqual(daewoo.primary_archetype, E2RArchetype.PORT_INFRA_DELIVERY)
        self.assertEqual(daewoo.stage2_date.isoformat(), "2024-11-12")
        self.assertEqual(daewoo.extra_price_metrics["completed_docks"], 5.0)
        self.assertEqual(daewoo.extra_price_metrics["maximum_capacity_target_mn_containers"], 3.5)
        self.assertEqual(daewoo.extra_price_metrics["development_road_project_value_usd_bn"], 17.0)
        self.assertIn("cash_collection_unverified", daewoo.red_flag_fields)

    def test_policy_pf_safety_and_rebar_cases_keep_r10_green_blockers(self) -> None:
        by_id = {case.case_id: case for case in ROUND253_CASE_CANDIDATES}
        housing = by_id["r10_loop11_seoul_housing_policy_supply_watch"]
        pf = by_id["r10_loop11_pf_credit_break_taeyoung_basket"]
        safety = by_id["r10_loop11_posco_dl_construction_safety_regulation"]
        rebar = by_id["r10_loop11_hyundai_steel_rebar_construction_demand_watch"]

        self.assertEqual(housing.primary_archetype, E2RArchetype.HOUSING_POLICY_SUPPLY_EVENT)
        self.assertEqual(housing.case_type, "event_premium")
        self.assertEqual(housing.extra_price_metrics["ltv_before_pct"], 50.0)
        self.assertEqual(housing.extra_price_metrics["ltv_after_pct"], 40.0)
        self.assertEqual(housing.extra_price_metrics["ltv_reduction_relative_pct"], -20.0)
        self.assertEqual(housing.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("policy_supply_headline_only", housing.red_flag_fields)

        self.assertEqual(pf.primary_archetype, E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK)
        self.assertTrue(pf.hard_4c_confirmed)
        self.assertEqual(pf.stage4c_date.isoformat(), "2024-05-13")
        self.assertEqual(pf.extra_price_metrics["pf_delinquency_2021_pct"], 0.37)
        self.assertEqual(pf.extra_price_metrics["pf_delinquency_2023_pct"], 2.70)
        self.assertEqual(pf.extra_price_metrics["pf_delinquency_increase_2021_to_2023_pct"], 629.7)
        self.assertEqual(pf.extra_price_metrics["government_support_package_krw_trn"], 40.6)
        self.assertIn("PF_relief_policy_only", pf.red_flag_fields)

        self.assertEqual(safety.primary_archetype, E2RArchetype.CONSTRUCTION_SAFETY_REGULATORY_4C)
        self.assertFalse(safety.hard_4c_confirmed)
        self.assertEqual(safety.extra_price_metrics["posco_ec_sites_halted"], 103.0)
        self.assertEqual(safety.extra_price_metrics["dl_construction_executives_resigned"], 80.0)
        self.assertEqual(safety.extra_price_metrics["proposed_fine_pct_of_operating_profit"], 5.0)
        self.assertIn("license_revocation_risk", safety.red_flag_fields)

        self.assertEqual(rebar.primary_archetype, E2RArchetype.BUILDING_MATERIALS_DEMAND_CYCLE)
        self.assertFalse(rebar.hard_4c_confirmed)
        self.assertEqual(rebar.stage4c_price_anchor, 29000.0)
        self.assertEqual(rebar.mae_1d, -1.2)
        self.assertEqual(rebar.extra_price_metrics["target_cut_pct"], -14.0)
        self.assertEqual(rebar.extra_price_metrics["net_profit_forecast_cut_pct"], -73.0)
        self.assertEqual(rebar.extra_price_metrics["rebar_price_expected_decline_pct"], -10.0)
        self.assertEqual(rebar.score_price_alignment, "evidence_good_but_price_failed")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND253_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND253_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND253_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND253_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round253_shadow_weight_rows()}
        deep_rows = round253_deep_sub_archetype_rows()
        green_markdown = render_round253_green_gate_review_markdown()
        stage_markdown = render_round253_stage4b_4c_review_markdown()

        self.assertIn("progress_revenue_visibility", required)
        self.assertIn("tenant_occupancy_NOI_AFFO_visibility", required)
        self.assertIn("contract_headline_only", forbidden)
        self.assertIn("data_center_theme_without_tenant", forbidden)
        self.assertIn("large_EPC_contract_announcement_5_to_10pct_jump", ROUND253_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("PF_workout_or_debt_restructuring", ROUND253_HARD_4C_GATES)
        self.assertIn("license_revocation_risk", ROUND253_HARD_4C_GATES)
        self.assertIn("tenant_noi_affo_anchor", fields)
        self.assertIn("cash_collection_quality", axes)
        self.assertIn("PF_relief_policy_only", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("PF delinquency spike", green_markdown)
        self.assertIn("r10_loop11_pf_credit_break_taeyoung_basket", stage_markdown)
        self.assertEqual(len(ROUND253_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["OVERSEAS_EPC_MEGA_ORDER"]["signed_contract"], "+5")
        self.assertEqual(shadow_rows["AI_DATA_CENTER_REAL_ASSET"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["REAL_ESTATE_PF_CREDIT_BREAK"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Jafurah" in row["deep_sub_archetype"] for row in deep_rows))
        self.assertIn("Hyundai Steel rebar proxy: construction demand weakness, estimate cuts, spread pressure", ROUND253_DEEP_SUB_ARCHETYPES)

    def test_audit_payload_cli_and_writer_outputs(self) -> None:
        audit = round253_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_253.md")
        self.assertEqual(audit["analyst_round_id"], "round_181")
        self.assertEqual(audit["large_sector"], ROUND253_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round253_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round253_r10_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round253_case_rows()
            self.assertEqual(len(records), len(ROUND253_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND253_CASE_CANDIDATES))
            self.assertIn("Samsung E&A Fadhili and Hyundai E&C Jafurah are Stage 2", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("cash_collection_quality", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("AI_DATA_CENTER_REAL_ASSET", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("license_revocation_risk", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(rows[0]["round_score_price_alignment"], "success_candidate_event_premium")
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["contract_value_usd_bn"], 6.0)

    def test_production_modules_do_not_import_round253(self) -> None:
        forbidden = "round253_r10_loop11_construction_real_estate_materials_price_validation"
        for rel_path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(rel_path).read_text(encoding="utf-8")
            self.assertNotIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
