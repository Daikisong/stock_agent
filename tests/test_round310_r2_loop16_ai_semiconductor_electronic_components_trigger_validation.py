from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round310_r2_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round310_r2_loop16_ai_semiconductor_electronic_components_trigger_validation import (
    ROUND310_4C_WATCH_GATES,
    ROUND310_CASE_CANDIDATES,
    ROUND310_GREEN_BLOCKERS,
    ROUND310_LARGE_SECTOR,
    ROUND310_REQUIRED_TARGET_ALIASES,
    ROUND310_ROW_SEPARATION_RULES,
    ROUND310_SCORE_DOWN_AXES,
    ROUND310_SCORE_UP_AXES,
    ROUND310_SHADOW_WEIGHT_ROWS,
    ROUND310_STAGE2_ACTIONABLE_RULES,
    ROUND310_STAGE3_GREEN_RULES,
    ROUND310_STAGE3_YELLOW_RULES,
    ROUND310_STAGE4B_WATCH_TRIGGERS,
    ROUND310_TRIGGER_RECORDS,
    render_round310_stage4b_4c_review_markdown,
    render_round310_stage_rules_markdown,
    render_round310_trigger_grid_markdown,
    round310_audit_payload,
    round310_case_records,
    round310_case_rows,
    round310_shadow_weight_rows,
    round310_summary,
    round310_trigger_rows,
    write_round310_r2_loop16_reports,
)


class Round310R2Loop16AISemiconductorTests(unittest.TestCase):
    def test_round310_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND310_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND310_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND310_REQUIRED_TARGET_ALIASES["HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE"],
            E2RArchetype.HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE.value,
        )
        self.assertEqual(
            ROUND310_REQUIRED_TARGET_ALIASES["CHINA_FAB_EXPORT_CONTROL_4C_WATCH"],
            E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH.value,
        )
        self.assertEqual(
            ROUND310_REQUIRED_TARGET_ALIASES["SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH"],
            E2RArchetype.SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH.value,
        )

    def test_archetype_definitions_capture_r2_loop16_rules(self) -> None:
        hbm = archetype_definition(E2RArchetype.HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE)
        memory = archetype_definition(E2RArchetype.MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW)
        openai = archetype_definition(E2RArchetype.OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE)
        foundry = archetype_definition(E2RArchetype.FOUNDRY_MEGA_CONTRACT_STAGE2_WITH_YIELD_4B)
        packaging = archetype_definition(E2RArchetype.ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B)
        hbm_delay = archetype_definition(E2RArchetype.HBM_CERTIFICATION_DELAY_FALSE_POSITIVE)
        china_fab = archetype_definition(E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH)
        labor = archetype_definition(E2RArchetype.SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH)
        lidar = archetype_definition(E2RArchetype.ELECTRONIC_COMPONENT_LIDAR_STAGE2_ORDER_GATE)

        self.assertIn("customer qualification", " ".join(hbm.stage2_candidate_signals))
        self.assertIn("ASP", " ".join(memory.stage2_candidate_signals))
        self.assertIn("labor", " ".join(memory.stage4c_thesis_break_signals))
        self.assertIn("wafer shipment", " ".join(openai.false_positive_patterns))
        self.assertIn("yield", " ".join(foundry.stage3_high_conviction_signals))
        self.assertIn("Micron", " ".join(packaging.stage4b_graduation_overheat_signals))
        self.assertIn("profit miss", " ".join(hbm_delay.stage4c_thesis_break_signals))
        self.assertIn("license", " ".join(china_fab.stage4c_thesis_break_signals))
        self.assertIn("strike", " ".join(labor.stage1_radar_signals))
        self.assertIn("design-in", " ".join(lidar.stage3_high_conviction_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round310_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND310_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round310_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_ai_semiconductor_headline_as_green_without_shipment_asp_margin_customer_evidence", record.green_guardrails)
            self.assertIn("stage_candidate_not_downgraded_for_missing_full_ohlc", record.green_guardrails)

        summary = round310_summary()
        self.assertEqual(summary["round_id"], "round_238")
        self.assertEqual(summary["large_sector"], ROUND310_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["trigger_count"], 11)
        self.assertEqual(summary["target_archetype_count"], 9)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 4)
        self.assertEqual(summary["stage2_event_candidate_count"], 2)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 4)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertTrue(summary["row_separation_required"])
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_cover_hbm_memory_openai_foundry_packaging_and_risks(self) -> None:
        by_id = {case.case_id: case for case in ROUND310_CASE_CANDIDATES}
        sk = by_id["r2_loop16_sk_hynix_hbm3e_hbm4_euv"]
        samsung_memory = by_id["r2_loop16_samsung_memory_supercycle"]
        openai = by_id["r2_loop16_samsung_skhynix_openai_stargate"]
        foundry = by_id["r2_loop16_samsung_foundry_165b_contract"]
        hanmi = by_id["r2_loop16_hanmi_semiconductor_hbm_equipment"]
        hbm_delay = by_id["r2_loop16_samsung_hbm_delay_false_positive"]
        china = by_id["r2_loop16_china_fab_export_control"]
        labor = by_id["r2_loop16_samsung_labor_strike_4c"]
        lidar = by_id["r2_loop16_lg_innotek_aeva_lidar"]

        self.assertEqual(sk.extra_price_metrics["hbm4_event_return_pct"], 7.3)
        self.assertEqual(sk.extra_price_metrics["market_relative_return_pp"], 6.1)
        self.assertEqual(sk.extra_price_metrics["asml_euv_order_krw_trn"], 11.95)
        self.assertEqual(sk.extra_price_metrics["asml_euv_order_usd_bn"], 7.97)
        self.assertEqual(sk.extra_price_metrics["asml_order_event_return_pct"], 5.7)

        self.assertEqual(samsung_memory.extra_price_metrics["max_memory_price_hike_pct"], 60)
        self.assertEqual(samsung_memory.extra_price_metrics["ddr5_32gb_price_before_usd"], 149)
        self.assertEqual(samsung_memory.extra_price_metrics["ddr5_32gb_price_after_usd"], 239)
        self.assertEqual(samsung_memory.extra_price_metrics["q1_2026_op_guidance_krw_trn"], 57.2)
        self.assertEqual(samsung_memory.extra_price_metrics["q1_2026_sales_guidance_krw_trn"], 133)
        self.assertEqual(samsung_memory.extra_price_metrics["q1_2026_op_lseg_estimate_krw_trn"], 40.5)
        self.assertEqual(samsung_memory.stage2_price_anchor, 203000)

        self.assertEqual(openai.extra_price_metrics["samsung_event_return_pct"], 4.7)
        self.assertEqual(openai.extra_price_metrics["sk_hynix_event_return_pct"], 12)
        self.assertEqual(openai.extra_price_metrics["kospi_event_return_pct"], 3)
        self.assertEqual(openai.extra_price_metrics["combined_market_cap_addition_usd_bn"], 37)
        self.assertEqual(openai.extra_price_metrics["stargate_project_value_usd_bn"], 500)
        self.assertEqual(openai.extra_price_metrics["openai_dram_wafer_monthly_demand"], 900000)

        self.assertEqual(foundry.extra_price_metrics["contract_value_usd_bn"], 16.5)
        self.assertEqual(foundry.extra_price_metrics["contract_end_year"], 2033)
        self.assertEqual(foundry.extra_price_metrics["event_return_pct"], 3.5)
        self.assertFalse(foundry.extra_price_metrics["counterparty_disclosed"])
        self.assertFalse(foundry.extra_price_metrics["cutting_edge_2nm_likely"])

        self.assertEqual(hanmi.extra_price_metrics["hanmi_event_return_pct"], 16)
        self.assertEqual(hanmi.extra_price_metrics["market_relative_return_pp"], 15.3)
        self.assertEqual(hanmi.extra_price_metrics["sk_hynix_contract_krw_bn"], 21.48)
        self.assertEqual(hanmi.extra_price_metrics["recent_contracts_krw_bn"], 200)
        self.assertEqual(hanmi.extra_price_metrics["possible_micron_report_intraday_return_pct"], 22)
        self.assertFalse(hanmi.extra_price_metrics["micron_confirmed"])

        self.assertEqual(hbm_delay.extra_price_metrics["t0_event_return_pct"], -2)
        self.assertEqual(hbm_delay.extra_price_metrics["q2_2025_op_guidance_krw_trn"], 4.6)
        self.assertEqual(hbm_delay.extra_price_metrics["q2_2025_op_estimate_krw_trn"], 6.2)
        self.assertEqual(hbm_delay.extra_price_metrics["q2_2025_op_yoy_decline_pct"], -56)
        self.assertEqual(hbm_delay.extra_price_metrics["q2_2025_market_relative_return_pp"], -1.4)

        self.assertEqual(china.extra_price_metrics["samsung_event_return_pct"], -2.3)
        self.assertEqual(china.extra_price_metrics["sk_hynix_event_return_pct"], -4.4)
        self.assertEqual(china.extra_price_metrics["kospi_event_return_pct"], -0.7)
        self.assertEqual(china.extra_price_metrics["hana_micron_event_return_pct"], -1.7)
        self.assertEqual(china.extra_price_metrics["hanmi_event_return_pct"], -4.4)
        self.assertEqual(china.extra_price_metrics["license_delay_days"], 120)

        self.assertEqual(labor.extra_price_metrics["event_return_pct"], -9.3)
        self.assertEqual(labor.extra_price_metrics["strike_days"], 18)
        self.assertEqual(labor.extra_price_metrics["workers"], 48000)
        self.assertEqual(labor.extra_price_metrics["essential_staffing"], 7087)
        self.assertEqual(labor.extra_price_metrics["production_loss_krw_trn"], 30)
        self.assertEqual(labor.extra_price_metrics["production_loss_usd_bn"], 19.9)

        self.assertEqual(lidar.extra_price_metrics["collaboration_value_usd_mn"], 50)
        self.assertEqual(lidar.extra_price_metrics["equity_investment_usd_mn"], 32)
        self.assertIn("robotics", lidar.extra_price_metrics["target_markets"])

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round310_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round310_shadow_weight_rows()}
        rules_md = render_round310_stage_rules_markdown()
        trigger_md = render_round310_trigger_grid_markdown()
        stage_md = render_round310_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND310_TRIGGER_RECORDS), 11)
        self.assertEqual(trigger_rows["r2l16_skhynix_hbm4_T1"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r2l16_openai_stargate_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r2l16_hanmi_micron_rumor_T2"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r2l16_china_fab_export_T1"]["promote_to"], "4C-watch")
        self.assertEqual(len(ROUND310_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE"]["hbm_customer_certification"], "+5")
        self.assertEqual(shadow_rows["OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE"]["AI_partnership_without_binding_order_penalty"], "-4")
        self.assertEqual(shadow_rows["ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B"]["equipment_rumor_without_signed_order_penalty"], "-5")
        self.assertIn("customer_qualification_mass_production_shipment_or_production_readiness_visible", ROUND310_STAGE2_ACTIONABLE_RULES)
        self.assertIn("one_of_customer_volume_margin_capacity_or_4c_overlay_remains_open", ROUND310_STAGE3_YELLOW_RULES)
        self.assertIn("memory_ASP_converts_to_quarterly_OP_margin_and_FCF", ROUND310_STAGE3_GREEN_RULES)
        self.assertIn("AI_partnership_without_binding_wafer_order", ROUND310_GREEN_BLOCKERS)
        self.assertIn("hbm_customer_certification", ROUND310_SCORE_UP_AXES)
        self.assertIn("equipment_rumor_without_signed_order", ROUND310_SCORE_DOWN_AXES)
        self.assertIn("equipment_customer_rumor_before_signed_order", ROUND310_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("labor_strike_affecting_DRAM_NAND_output", ROUND310_4C_WATCH_GATES)
        self.assertIn("do_not_treat_partnership_rumor_policy_or_capex_headline_as_actual_volume_shipment", ROUND310_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r2_loop16_samsung_memory_supercycle", trigger_md)
        self.assertIn("r2_loop16_samsung_labor_strike_4c", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round310_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_310.md")
        self.assertEqual(audit["round_id"], "round_238")
        self.assertEqual(audit["large_sector"], ROUND310_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_ai_semiconductor_headline_as_green_without_shipment_asp_margin_customer_evidence", audit["what_not_to_change"])

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
            paths = write_round310_r2_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round310_case_rows()
            self.assertEqual(len(records), len(ROUND310_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND310_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND310_TRIGGER_RECORDS))
            self.assertIn("case_library_row_describes_stage_candidate", paths["row_separation_plan"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
