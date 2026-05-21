from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round318_r10_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round318_r10_loop16_construction_real_estate_building_materials_trigger_validation import (
    ROUND318_CASE_CANDIDATES,
    ROUND318_GREEN_BLOCKERS,
    ROUND318_HARD_4C_GATES,
    ROUND318_LARGE_SECTOR,
    ROUND318_REQUIRED_TARGET_ALIASES,
    ROUND318_ROW_SEPARATION_RULES,
    ROUND318_SCORE_DOWN_AXES,
    ROUND318_SCORE_UP_AXES,
    ROUND318_SHADOW_WEIGHT_ROWS,
    ROUND318_STAGE2_ACTIONABLE_RULES,
    ROUND318_STAGE3_GREEN_RULES,
    ROUND318_STAGE3_YELLOW_RULES,
    ROUND318_STAGE4B_WATCH_TRIGGERS,
    ROUND318_TRIGGER_RECORDS,
    render_round318_stage_rules_markdown,
    render_round318_stage4b_4c_review_markdown,
    render_round318_trigger_grid_markdown,
    round318_audit_payload,
    round318_case_records,
    round318_case_rows,
    round318_shadow_weight_rows,
    round318_summary,
    round318_trigger_rows,
    write_round318_r10_loop16_reports,
)


class Round318R10Loop16ConstructionRealEstateMaterialsTests(unittest.TestCase):
    def test_round318_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND318_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND318_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND318_REQUIRED_TARGET_ALIASES["MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE"],
            E2RArchetype.MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND318_REQUIRED_TARGET_ALIASES["CONSTRUCTION_SAFETY_HARD_4C"],
            E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND318_REQUIRED_TARGET_ALIASES["RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B"],
            E2RArchetype.RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B.value,
        )

    def test_archetype_definitions_capture_r10_loop16_rules(self) -> None:
        epc = archetype_definition(E2RArchetype.MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE)
        gas = archetype_definition(E2RArchetype.MEGA_GAS_PIPELINE_EPC_STAGE2_WITH_MARGIN_GATE)
        pf = archetype_definition(E2RArchetype.PF_LIQUIDITY_RESTRUCTURING_4C_AND_RELIEF)
        housing = archetype_definition(E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_WITH_LTV_4B)
        safety = archetype_definition(E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C)
        fab = archetype_definition(E2RArchetype.AI_FAB_CONSTRUCTION_STAGE2)
        material = archetype_definition(E2RArchetype.BUILDING_MATERIAL_INPUT_COST_STAGE2_4B)
        rate = archetype_definition(E2RArchetype.RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B)

        self.assertIn("working capital", " ".join(epc.stage3_high_conviction_signals))
        self.assertIn("contract share", " ".join(gas.stage3_high_conviction_signals))
        self.assertIn("successful project refinancing", " ".join(pf.stage3_high_conviction_signals))
        self.assertIn("LTV tightening blocks demand", " ".join(housing.stage4c_thesis_break_signals))
        self.assertIn("license", " ".join(safety.stage4c_thesis_break_signals))
        self.assertIn("builder order value", " ".join(fab.stage3_high_conviction_signals))
        self.assertIn("input-cost spike without pass-through", " ".join(material.stage4c_thesis_break_signals))
        self.assertIn("housing overheating", " ".join(rate.stage4b_graduation_overheat_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round318_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND318_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round318_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn(
                "do_not_treat_EPC_PF_housing_safety_fab_or_material_headline_as_Green_without_margin_cash_presales_refinancing_safety_clearance_or_spread",
                record.green_guardrails,
            )

        by_id = {record.case_id: record for record in records}
        self.assertIn("hard_4c_confirmed_false", by_id["r10_loop16_samsung_ea_fadhili"].green_guardrails)
        self.assertNotIn("hard_4c_confirmed_false", by_id["r10_loop16_construction_safety_hyundai_engineering_bridge"].green_guardrails)

        summary = round318_summary()
        self.assertEqual(summary["round_id"], "round_246")
        self.assertEqual(summary["large_sector"], ROUND318_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 8)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 2)
        self.assertEqual(summary["stage2_candidate_count"], 6)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 4)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_epc_pf_housing_safety_fab_material_and_macro(self) -> None:
        by_id = {case.case_id: case for case in ROUND318_CASE_CANDIDATES}
        samsung = by_id["r10_loop16_samsung_ea_fadhili"]
        hyundai = by_id["r10_loop16_hyundai_ec_jafurah_gas"]
        pf = by_id["r10_loop16_pf_taeyoung_builder_restructuring"]
        housing = by_id["r10_loop16_seoul_housing_supply_reconstruction"]
        safety = by_id["r10_loop16_construction_safety_hyundai_engineering_bridge"]
        fab = by_id["r10_loop16_samsung_ct_p5_fab_construction"]
        steel = by_id["r10_loop16_steel_plate_antidumping_construction_input"]
        rate = by_id["r10_loop16_bok_rate_cut_housing_construction_mixed"]

        self.assertEqual(samsung.primary_archetype, E2RArchetype.MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE)
        self.assertEqual(samsung.event_mfe_pct, 8.5)
        self.assertEqual(samsung.extra_price_metrics["market_relative_return_pp"], 9.9)
        self.assertIn("working_capital_profile_missing", samsung.red_flag_fields)

        self.assertEqual(hyundai.extra_price_metrics["main_gas_network_added_pipeline_km"], 4000)
        self.assertIn("Hyundai_EC_contract_share_missing", hyundai.red_flag_fields)

        self.assertEqual(pf.extra_price_metrics["government_support_krw_trn"], 40.6)
        self.assertEqual(pf.extra_price_metrics["pf_delinquency_end_2023_pct"], 2.70)
        self.assertEqual(pf.stage_failure_type, "should_have_been_red")

        self.assertEqual(housing.extra_price_metrics["ltv_new_pct"], 40)
        self.assertIn("LTV_demand_curb_4B", housing.red_flag_fields)

        self.assertTrue(safety.hard_4c_confirmed)
        self.assertEqual(safety.extra_price_metrics["fatalities"], 4)
        self.assertEqual(safety.extra_price_metrics["proposed_fine_pct_of_operating_profit"], 5)

        self.assertEqual(fab.extra_price_metrics["samsung_group_domestic_investment_krw_trn"], 450)
        self.assertIn("Samsung_CT_order_value_missing", fab.red_flag_fields)

        self.assertEqual(steel.extra_price_metrics["hyundai_steel_event_return_pct"], 5.8)
        self.assertIn("builder_input_cost_4B", steel.red_flag_fields)

        self.assertEqual(rate.extra_price_metrics["policy_rate_pct"], 2.50)
        self.assertIn("housing_overheating_4B", rate.red_flag_fields)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round318_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round318_shadow_weight_rows()}
        rules_md = render_round318_stage_rules_markdown()
        trigger_md = render_round318_trigger_grid_markdown()
        stage_md = render_round318_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND318_TRIGGER_RECORDS), 8)
        self.assertEqual(trigger_rows["r10l16_samsung_ea_fadhili_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r10l16_construction_safety_T0"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r10l16_steel_plate_antidumping_T0"]["promote_to"], "Stage2+4B")
        self.assertEqual(len(ROUND318_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE"]["EPC_contract_value_visibility"], "+5")
        self.assertEqual(shadow_rows["PF_LIQUIDITY_RESTRUCTURING_4C_AND_RELIEF"]["PF_support_without_writeoff_penalty"], "-5")
        self.assertEqual(shadow_rows["BUILDING_MATERIAL_INPUT_COST_STAGE2_4B"]["material_cost_pass_through"], "+4")
        self.assertIn("contract_value_is_clear", ROUND318_STAGE2_ACTIONABLE_RULES)
        self.assertIn("reported_price_anchor_supports_trigger_but_full_adjusted_OHLC_is_missing", ROUND318_STAGE3_YELLOW_RULES)
        self.assertIn("input_cost_pass_through_is_contractually_protected", ROUND318_STAGE3_GREEN_RULES)
        self.assertIn("safety_incident_treated_as_one_off", ROUND318_GREEN_BLOCKERS)
        self.assertIn("EPC_margin_cash_conversion", ROUND318_SCORE_UP_AXES)
        self.assertIn("AI_fab_headline_without_order_value", ROUND318_SCORE_DOWN_AXES)
        self.assertIn("PF_support_appears_before_loss_recognition_and_refinancing", ROUND318_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_construction_accident", ROUND318_HARD_4C_GATES)
        self.assertIn("trigger_calibration_row_stores_event_anchor_contract_policy_safety_material_or_macro_metrics", ROUND318_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r10_loop16_samsung_ea_fadhili", trigger_md)
        self.assertIn("r10_loop16_construction_safety_hyundai_engineering_bridge", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round318_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_318.md")
        self.assertEqual(audit["round_id"], "round_246")
        self.assertEqual(audit["large_sector"], ROUND318_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_EPC_PF_housing_safety_fab_or_material_headline_as_Green_without_margin_cash_presales_refinancing_safety_clearance_or_spread", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--triggers",
                "triggers.jsonl",
                "--audit",
                "audit.json",
                "--weight-profile",
                "weights.csv",
            ]
        )
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.triggers, "triggers.jsonl")
        self.assertEqual(args.audit, "audit.json")
        self.assertEqual(args.weight_profile, "weights.csv")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round318_r10_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round318_case_rows()
            self.assertEqual(len(records), len(ROUND318_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND318_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND318_TRIGGER_RECORDS))
            self.assertIn("Samsung E&A / Fadhili", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage3-Green", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r10l16_construction_safety_T0", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE", paths["weight_profiles"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["samsung_contract_value_context_usd_bn"], 6.0)


if __name__ == "__main__":
    unittest.main()
