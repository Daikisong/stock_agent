from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round323_r2_loop17_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round323_r2_loop17_ai_semiconductor_electronics import (
    ROUND323_CASE_CANDIDATES,
    ROUND323_GREEN_BLOCKERS,
    ROUND323_HARD_4C_GATES,
    ROUND323_LARGE_SECTOR,
    ROUND323_REQUIRED_TARGET_ALIASES,
    ROUND323_ROW_SEPARATION_RULES,
    ROUND323_SCORE_DOWN_AXES,
    ROUND323_SCORE_UP_AXES,
    ROUND323_SHADOW_WEIGHT_ROWS,
    ROUND323_STAGE2_ACTIONABLE_RULES,
    ROUND323_STAGE3_GREEN_RULES,
    ROUND323_STAGE3_YELLOW_RULES,
    ROUND323_STAGE4B_WATCH_TRIGGERS,
    ROUND323_TRIGGER_RECORDS,
    render_round323_stage_rules_markdown,
    render_round323_stage4b_4c_review_markdown,
    render_round323_trigger_grid_markdown,
    round323_audit_payload,
    round323_case_records,
    round323_case_rows,
    round323_shadow_weight_rows,
    round323_summary,
    round323_trigger_rows,
    write_round323_r2_loop17_reports,
)


class Round323R2Loop17AISemiconductorTests(unittest.TestCase):
    def test_round323_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND323_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND323_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND323_REQUIRED_TARGET_ALIASES["HBM_FIRST_MOVER_STAGE2_ACTIONABLE"],
            E2RArchetype.HBM_FIRST_MOVER_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND323_REQUIRED_TARGET_ALIASES["OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE"],
            E2RArchetype.OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND323_REQUIRED_TARGET_ALIASES["LABOR_SUPPLY_DISRUPTION_4B"],
            E2RArchetype.LABOR_SUPPLY_DISRUPTION_4B.value,
        )

    def test_archetype_definitions_capture_r2_loop17_rules(self) -> None:
        hbm3e = archetype_definition(E2RArchetype.HBM_FIRST_MOVER_STAGE2_ACTIONABLE)
        hbm4 = archetype_definition(E2RArchetype.HBM4_CERTIFICATION_STAGE3_YELLOW_CANDIDATE)
        openai = archetype_definition(E2RArchetype.OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE)
        samsung = archetype_definition(E2RArchetype.SAMSUNG_HBM_CATCHUP_STAGE2_WITH_LABOR_4B)
        hanmi = archetype_definition(E2RArchetype.HBM_PACKAGING_EQUIPMENT_STAGE2_ACTIONABLE)
        price_failed = archetype_definition(E2RArchetype.MEMORY_EARNINGS_GOOD_BUT_PRICE_FAILED)
        export_control = archetype_definition(E2RArchetype.CHINA_EXPORT_CONTROL_4B)
        labor = archetype_definition(E2RArchetype.LABOR_SUPPLY_DISRUPTION_4B)

        self.assertIn("12-layer HBM3E", " ".join(hbm3e.stage1_radar_signals))
        self.assertIn("customer order volume", " ".join(hbm3e.stage3_high_conviction_signals))
        self.assertIn("HBM4 certification", " ".join(hbm4.stage1_radar_signals))
        self.assertIn("Nvidia", " ".join(hbm4.stage3_high_conviction_signals))
        self.assertIn("900,000 DRAM wafers", " ".join(openai.stage1_radar_signals))
        self.assertIn("binding order", " ".join(openai.stage3_high_conviction_signals))
        self.assertIn("labor", " ".join(samsung.stage1_radar_signals))
        self.assertIn("TSV-TC bonder", " ".join(hanmi.stage1_radar_signals))
        self.assertIn("repeat order", " ".join(hanmi.stage3_high_conviction_signals))
        self.assertIn("record profit", " ".join(price_failed.stage1_radar_signals))
        self.assertIn("commodity memory", " ".join(price_failed.stage4c_thesis_break_signals))
        self.assertIn("China fab", " ".join(export_control.stage1_radar_signals))
        self.assertIn("license", " ".join(export_control.stage3_high_conviction_signals))
        self.assertIn("DRAM", " ".join(labor.stage1_radar_signals))
        self.assertIn("NAND", " ".join(labor.stage4c_thesis_break_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round323_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND323_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round323_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", record.green_guardrails)

        summary = round323_summary()
        self.assertEqual(summary["source_round"], "docs/round/round_323.md")
        self.assertEqual(summary["round_id"], "round_251")
        self.assertEqual(summary["large_sector"], ROUND323_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 8)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 3)
        self.assertEqual(summary["stage2_candidate_count"], 5)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 4)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["strong_4c_case_count"], 0)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_capture_hbm_stage2_price_failed_and_4b_patterns(self) -> None:
        by_id = {case.case_id: case for case in ROUND323_CASE_CANDIDATES}
        hbm3e = by_id["r2_loop17_sk_hynix_hbm3e_mass_production"]
        hbm4 = by_id["r2_loop17_sk_hynix_hbm4_certification"]
        openai = by_id["r2_loop17_openai_stargate_memory_loi"]
        samsung = by_id["r2_loop17_samsung_hbm_catchup_nvidia_amd"]
        hanmi = by_id["r2_loop17_hanmi_semiconductor_hbm_packaging"]
        price_failed = by_id["r2_loop17_sk_hynix_record_profit_price_failed"]
        export_control = by_id["r2_loop17_us_export_control_china_fabs"]
        labor = by_id["r2_loop17_samsung_labor_memory_supply_4b"]

        self.assertEqual(hbm3e.extra_price_metrics["capacity_uplift_vs_8_layer_pct"], 50)
        self.assertEqual(hbm3e.stage_candidate, "Stage2-Actionable")

        self.assertEqual(hbm4.extra_price_metrics["event_return_pct"], 7.3)
        self.assertTrue(hbm4.extra_price_metrics["customer_specific_base_die"])
        self.assertEqual(hbm4.stage_failure_type, "yellow_success")

        self.assertEqual(openai.extra_price_metrics["project_value_context_usd_bn"], 500)
        self.assertEqual(openai.extra_price_metrics["openai_dram_wafer_demand_per_month"], 900000)
        self.assertIn("LOI_not_binding_final_order", openai.red_flag_fields)

        self.assertEqual(samsung.extra_price_metrics["samsung_hbm_share_context_pct"], 22)
        self.assertEqual(samsung.extra_price_metrics["sk_hynix_hbm_share_context_pct"], 57)
        self.assertIn("labor_cost_resolution_missing", samsung.red_flag_fields)

        self.assertEqual(hanmi.extra_price_metrics["hanmi_event_return_pct"], 16)
        self.assertEqual(hanmi.extra_price_metrics["sk_hynix_supply_deal_krw_bn"], 21.48)

        self.assertEqual(price_failed.score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(price_failed.extra_price_metrics["event_return_pct"], -4)
        self.assertEqual(price_failed.stage_candidate, "no_actionable")

        self.assertEqual(export_control.extra_price_metrics["effective_delay_days"], 120)
        self.assertEqual(export_control.stage_candidate, "4B-watch")

        self.assertEqual(labor.extra_price_metrics["event_return_pct"], -9.3)
        self.assertFalse(labor.extra_price_metrics["hard_4c"])

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round323_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round323_shadow_weight_rows()}
        rules_md = render_round323_stage_rules_markdown()
        trigger_md = render_round323_trigger_grid_markdown()
        stage_md = render_round323_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND323_TRIGGER_RECORDS), 8)
        self.assertEqual(trigger_rows["r2l17_skh_hbm3e_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r2l17_skh_hbm4_T1"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r2l17_openai_stargate_T1"]["promote_to"], "Stage2-Actionable+4B")
        self.assertEqual(trigger_rows["r2l17_skh_record_profit_T0"]["promote_to"], "no_actionable")
        self.assertEqual(trigger_rows["r2l17_us_export_control_T0"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r2l17_samsung_labor_T0"]["promote_to"], "4B-watch")
        self.assertEqual(len(ROUND323_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE"]["loi_without_final_order_penalty"], "-4")
        self.assertEqual(shadow_rows["MEMORY_EARNINGS_GOOD_BUT_PRICE_FAILED"]["market_relative_return"], "-5")
        self.assertIn("HBM_memory_demand_or_packaging_equipment_trigger_is_company_specific", ROUND323_STAGE2_ACTIONABLE_RULES)
        self.assertIn("yield_ASP_margin_capacity_or_binding_order_gate_partly_open", ROUND323_STAGE3_YELLOW_RULES)
        self.assertIn("full_window_MFE_MAE_is_available_and_supportive", ROUND323_STAGE3_GREEN_RULES)
        self.assertIn("LOI_without_binding_order", ROUND323_GREEN_BLOCKERS)
        self.assertIn("hbm_mass_production", ROUND323_SCORE_UP_AXES)
        self.assertIn("labor_supply_stability", ROUND323_SCORE_DOWN_AXES)
        self.assertIn("Samsung_labor_strike_with_possible_DRAM_NAND_supply_impact", ROUND323_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("binding_order_failure_after_LOI", ROUND323_HARD_4C_GATES)
        self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", ROUND323_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r2_loop17_openai_stargate_memory_loi", trigger_md)
        self.assertIn("r2_loop17_samsung_labor_memory_supply_4b", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round323_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_323.md")
        self.assertEqual(audit["round_id"], "round_251")
        self.assertEqual(audit["large_sector"], ROUND323_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_HBM_mass_production_certification_LOI_or_record_profit_as_Green_without_volume_yield_ASP_margin_capacity_and_risk_resolution", audit["what_not_to_change"])

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

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_round323_r2_loop17_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            loaded = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(loaded), 8)
            self.assertIn("Stage3-Green confirmed: `0`", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("full adjusted OHLC", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertGreater(len(round323_case_rows()), 0)


if __name__ == "__main__":
    unittest.main()
