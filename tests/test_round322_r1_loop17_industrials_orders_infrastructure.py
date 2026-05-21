from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round322_r1_loop17_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round322_r1_loop17_industrials_orders_infrastructure import (
    ROUND322_CASE_CANDIDATES,
    ROUND322_GREEN_BLOCKERS,
    ROUND322_HARD_4C_GATES,
    ROUND322_LARGE_SECTOR,
    ROUND322_REQUIRED_TARGET_ALIASES,
    ROUND322_ROW_SEPARATION_RULES,
    ROUND322_SCORE_DOWN_AXES,
    ROUND322_SCORE_UP_AXES,
    ROUND322_SHADOW_WEIGHT_ROWS,
    ROUND322_STAGE2_ACTIONABLE_RULES,
    ROUND322_STAGE3_GREEN_RULES,
    ROUND322_STAGE3_YELLOW_RULES,
    ROUND322_STAGE4B_WATCH_TRIGGERS,
    ROUND322_TRIGGER_RECORDS,
    render_round322_stage_rules_markdown,
    render_round322_stage4b_4c_review_markdown,
    render_round322_trigger_grid_markdown,
    round322_audit_payload,
    round322_case_records,
    round322_case_rows,
    round322_shadow_weight_rows,
    round322_summary,
    round322_trigger_rows,
    write_round322_r1_loop17_reports,
)


class Round322R1Loop17IndustrialsTests(unittest.TestCase):
    def test_round322_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND322_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND322_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND322_REQUIRED_TARGET_ALIASES["SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE"],
            E2RArchetype.SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND322_REQUIRED_TARGET_ALIASES["GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED"],
            E2RArchetype.GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED.value,
        )
        self.assertEqual(
            ROUND322_REQUIRED_TARGET_ALIASES["SHIPBUILDING_ORDER_CANCELLATION_4C"],
            E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_4C.value,
        )

    def test_archetype_definitions_capture_r1_loop17_rules(self) -> None:
        merger = archetype_definition(E2RArchetype.SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE)
        naval = archetype_definition(E2RArchetype.SHIPBUILDING_NAVAL_EXPORT_STAGE2_WITH_SANCTION_4B)
        defense = archetype_definition(E2RArchetype.DEFENSE_INDUSTRIAL_EXPORT_STAGE2_YELLOW)
        grid = archetype_definition(E2RArchetype.GRID_EQUIPMENT_AI_POWER_STAGE2_PROMOTE)
        price_failed = archetype_definition(E2RArchetype.GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED)
        transformer = archetype_definition(E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2_NO_PRICE)
        nuclear = archetype_definition(E2RArchetype.NUCLEAR_SMR_INDUSTRIAL_SUPPLY_STAGE2_WITH_FINAL_CONTRACT_GATE)
        cancellation = archetype_definition(E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_4C)

        self.assertIn("MASGA", " ".join(merger.stage1_radar_signals))
        self.assertIn("U.S. naval orders", " ".join(merger.stage3_high_conviction_signals))
        self.assertIn("China sanction", " ".join(naval.stage4c_thesis_break_signals))
        self.assertIn("K2 export", " ".join(defense.stage1_radar_signals))
        self.assertIn("AI data-center power demand", " ".join(grid.stage1_radar_signals))
        self.assertIn("shares fall on upgrade", " ".join(price_failed.stage4c_thesis_break_signals))
        self.assertIn("lead time 143 weeks", " ".join(transformer.stage1_radar_signals))
        self.assertIn("final equipment contract", " ".join(nuclear.stage3_high_conviction_signals))
        self.assertIn("Zvezda", " ".join(cancellation.stage1_radar_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round322_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND322_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round322_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", record.green_guardrails)

        by_id = {record.case_id: record for record in records}
        self.assertIn("strong_4c_confirmed_false", by_id["r1_loop17_hd_hyundai_heavy_mipo_masga"].green_guardrails)
        self.assertNotIn("strong_4c_confirmed_false", by_id["r1_loop17_samsung_heavy_zvezda_cancellation"].green_guardrails)

        summary = round322_summary()
        self.assertEqual(summary["source_round"], "docs/round/round_322.md")
        self.assertEqual(summary["round_id"], "round_250")
        self.assertEqual(summary["large_sector"], ROUND322_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 10)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 3)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 4)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["strong_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_capture_industrial_stage2_price_failed_and_4c_patterns(self) -> None:
        by_id = {case.case_id: case for case in ROUND322_CASE_CANDIDATES}
        merger = by_id["r1_loop17_hd_hyundai_heavy_mipo_masga"]
        hanwha = by_id["r1_loop17_hanwha_ocean_us_navy_china_sanction"]
        rotem = by_id["r1_loop17_hyundai_rotem_k2_poland"]
        hde = by_id["r1_loop17_hd_hyundai_electric_ai_power"]
        ls = by_id["r1_loop17_ls_electric_us_data_center_price_failed"]
        hyosung = by_id["r1_loop17_hyosung_heavy_us_transformer_capacity"]
        doosan = by_id["r1_loop17_doosan_enerbility_smr_ai_power"]
        samsung = by_id["r1_loop17_samsung_heavy_zvezda_cancellation"]

        self.assertEqual(merger.extra_price_metrics["hd_hyundai_heavy_event_return_pct"], 11.3)
        self.assertEqual(merger.extra_price_metrics["hd_hyundai_mipo_event_return_pct"], 14.6)
        self.assertTrue(merger.extra_price_metrics["record_high"])

        self.assertEqual(hanwha.extra_price_metrics["frigate_event_return_pct"], 6.0)
        self.assertEqual(hanwha.extra_price_metrics["china_sanction_event_return_pct"], -5.8)
        self.assertEqual(hanwha.extra_price_metrics["philly_expansion_pledge_usd_bn"], 5)

        self.assertEqual(rotem.extra_price_metrics["earnings_event_return_pct"], 9.3)
        self.assertEqual(rotem.extra_price_metrics["market_relative_pp"], 9.6)
        self.assertEqual(rotem.extra_price_metrics["contract_value_estimate_usd_bn"], 6.5)
        self.assertEqual(rotem.stage_failure_type, "yellow_success")

        self.assertEqual(hde.extra_price_metrics["reported_share_return_since_jan_2024_pct"], 333)
        self.assertEqual(hde.stage_failure_type, "missed_structural")

        self.assertEqual(ls.score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(ls.extra_price_metrics["reported_event_return_pct"], -5.4)
        self.assertEqual(ls.extra_price_metrics["target_price_raise_pct"], 87)

        self.assertEqual(hyosung.extra_price_metrics["gsu_demand_increase_since_2019_pct"], 274)
        self.assertEqual(hyosung.extra_price_metrics["average_lead_time_weeks"], 143)
        self.assertEqual(hyosung.extra_price_metrics["hyosung_hico_memphis_expansion_usd_mn"], 157)

        self.assertIn("Fermi_America", doosan.extra_price_metrics["counterparties"])
        self.assertEqual(doosan.extra_price_metrics["project_context"], "Texas_AI_project_nuclear_SMR_equipment")

        self.assertTrue(samsung.strong_4c_confirmed)
        self.assertEqual(samsung.extra_price_metrics["cancelled_order_value_krw_trn"], 4.85)
        self.assertEqual(samsung.extra_price_metrics["cancelled_order_value_usd_bn"], 3.54)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round322_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round322_shadow_weight_rows()}
        rules_md = render_round322_stage_rules_markdown()
        trigger_md = render_round322_trigger_grid_markdown()
        stage_md = render_round322_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND322_TRIGGER_RECORDS), 10)
        self.assertEqual(trigger_rows["r1l17_hd_hhi_mipo_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r1l17_hanwha_ocean_china_T2"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r1l17_hyundai_rotem_poland_T2"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r1l17_hd_hyundai_electric_ai_T1"]["promote_to"], "Stage2_promote_candidate")
        self.assertEqual(trigger_rows["r1l17_ls_electric_report_T0"]["promote_to"], "no_actionable")
        self.assertEqual(trigger_rows["r1l17_samsung_heavy_zvezda_T1"]["promote_to"], "4C-watch")
        self.assertEqual(len(ROUND322_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED"]["market_relative_return"], "-5")
        self.assertEqual(shadow_rows["NUCLEAR_SMR_INDUSTRIAL_SUPPLY_STAGE2_WITH_FINAL_CONTRACT_GATE"]["mou_without_final_contract_penalty"], "-5")
        self.assertIn("event_return_at_least_5pct", ROUND322_STAGE2_ACTIONABLE_RULES)
        self.assertIn("EPS_OP_or_FCF_path_likely_changes", ROUND322_STAGE3_YELLOW_RULES)
        self.assertIn("full_window_MFE_MAE_is_available_and_supportive", ROUND322_STAGE3_GREEN_RULES)
        self.assertIn("report_upgrade_without_price_validation", ROUND322_GREEN_BLOCKERS)
        self.assertIn("grid_equipment_backlog", ROUND322_SCORE_UP_AXES)
        self.assertIn("MOU_without_final_contract", ROUND322_SCORE_DOWN_AXES)
        self.assertIn("target_price_upgrade_but_stock_falls", ROUND322_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("major_order_cancellation", ROUND322_HARD_4C_GATES)
        self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", ROUND322_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r1_loop17_ls_electric_us_data_center_price_failed", trigger_md)
        self.assertIn("r1_loop17_samsung_heavy_zvezda_cancellation", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round322_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_322.md")
        self.assertEqual(audit["round_id"], "round_250")
        self.assertEqual(audit["large_sector"], ROUND322_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_MASGA_AI_power_SMR_or_target_price_headline_as_Green_without_margin_capacity_finality_or_price_validation", audit["what_not_to_change"])

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
            paths = write_round322_r1_loop17_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            self.assertEqual(len(load_case_library(root / "cases.jsonl")), 8)
            self.assertEqual(len(round322_case_rows()), 8)
            self.assertIn("Stage3-Green confirmed", paths["summary"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
