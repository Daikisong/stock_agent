from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round325_r4_loop17_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round325_r4_loop17_materials_spreads_strategic import (
    ROUND325_CASE_CANDIDATES,
    ROUND325_GREEN_BLOCKERS,
    ROUND325_HARD_4C_GATES,
    ROUND325_LARGE_SECTOR,
    ROUND325_REQUIRED_TARGET_ALIASES,
    ROUND325_ROW_SEPARATION_RULES,
    ROUND325_SCORE_DOWN_AXES,
    ROUND325_SCORE_UP_AXES,
    ROUND325_SHADOW_WEIGHT_ROWS,
    ROUND325_STAGE2_ACTIONABLE_RULES,
    ROUND325_STAGE3_GREEN_RULES,
    ROUND325_STAGE3_YELLOW_RULES,
    ROUND325_STAGE4B_WATCH_TRIGGERS,
    ROUND325_TRIGGER_RECORDS,
    render_round325_stage_rules_markdown,
    render_round325_stage4b_4c_review_markdown,
    render_round325_trigger_grid_markdown,
    round325_audit_payload,
    round325_case_records,
    round325_case_rows,
    round325_shadow_weight_rows,
    round325_summary,
    round325_trigger_rows,
    write_round325_r4_loop17_reports,
)


class Round325R4Loop17MaterialsSpreadsStrategicTests(unittest.TestCase):
    def test_round325_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND325_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND325_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND325_REQUIRED_TARGET_ALIASES["CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B"],
            E2RArchetype.CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B.value,
        )
        self.assertEqual(
            ROUND325_REQUIRED_TARGET_ALIASES["STEEL_ANTIDUMPING_PROTECTION_STAGE2"],
            E2RArchetype.STEEL_ANTIDUMPING_PROTECTION_STAGE2.value,
        )
        self.assertEqual(
            ROUND325_REQUIRED_TARGET_ALIASES["RARE_EARTH_EXPORT_CONTROL_4B"],
            E2RArchetype.RARE_EARTH_EXPORT_CONTROL_4B.value,
        )

    def test_archetype_definitions_capture_r4_loop17_rules(self) -> None:
        control = archetype_definition(E2RArchetype.CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B)
        tc = archetype_definition(E2RArchetype.SMELTER_TC_SPREAD_4B)
        critical = archetype_definition(E2RArchetype.CRITICAL_MINERALS_US_PROCESSING_STAGE2_WITH_CAPEX_4B)
        steel = archetype_definition(E2RArchetype.STEEL_ANTIDUMPING_PROTECTION_STAGE2)
        localization = archetype_definition(E2RArchetype.STEEL_TARIFF_AND_LOCALIZATION_HEDGE_STAGE2_4B)
        petro = archetype_definition(E2RArchetype.PETROCHEMICAL_RESTRUCTURING_STAGE2_RELIEF)
        refining = archetype_definition(E2RArchetype.REFINING_MARGIN_SPREAD_PRICE_FAILED)
        rare = archetype_definition(E2RArchetype.RARE_EARTH_EXPORT_CONTROL_4B)

        self.assertIn("control premium", " ".join(control.stage1_radar_signals))
        self.assertIn("share issuance dilution", " ".join(control.stage4c_thesis_break_signals))
        self.assertIn("zinc treatment charge cut", " ".join(tc.stage1_radar_signals))
        self.assertIn("TC compression", " ".join(tc.false_positive_patterns))
        self.assertIn("Tennessee", " ".join(critical.stage1_radar_signals))
        self.assertIn("offtake", " ".join(critical.stage3_high_conviction_signals))
        self.assertIn("Chinese steel plate anti-dumping", " ".join(steel.stage1_radar_signals))
        self.assertIn("export tariff risk", " ".join(steel.false_positive_patterns))
        self.assertIn("Louisiana steel plant", " ".join(localization.stage1_radar_signals))
        self.assertIn("Daesan restructuring", " ".join(petro.stage1_radar_signals))
        self.assertIn("segment quality", " ".join(refining.false_positive_patterns))
        self.assertIn("U.S. defense end-use restriction", " ".join(rare.stage1_radar_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round325_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND325_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round325_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", record.green_guardrails)

        summary = round325_summary()
        self.assertEqual(summary["source_round"], "docs/round/round_325.md")
        self.assertEqual(summary["round_id"], "round_253")
        self.assertEqual(summary["large_sector"], ROUND325_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["trigger_count"], 13)
        self.assertEqual(summary["target_archetype_count"], 10)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 1)
        self.assertEqual(summary["stage2_candidate_count"], 6)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 5)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 8)
        self.assertEqual(summary["hard_4c_confirmed_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_capture_control_tc_steel_petrochemical_and_rare_earth_patterns(self) -> None:
        by_id = {case.case_id: case for case in ROUND325_CASE_CANDIDATES}
        control = by_id["r4_loop17_korea_zinc_control_premium"]
        tc = by_id["r4_loop17_korea_zinc_teck_tc_cut"]
        critical = by_id["r4_loop17_korea_zinc_us_critical_minerals"]
        steel = by_id["r4_loop17_hyundai_steel_posco_antidumping"]
        louisiana = by_id["r4_loop17_hyundai_posco_louisiana_steel_plant"]
        petro = by_id["r4_loop17_petrochemical_oversupply_restructuring"]
        refining = by_id["r4_loop17_sk_innovation_refining_margin_spread"]
        lithium = by_id["r4_loop17_posco_minres_lithium_jv"]
        rare = by_id["r4_loop17_china_rare_earth_export_control_korea"]

        self.assertEqual(control.extra_price_metrics["initial_tender_value_krw_trn"], 2.0)
        self.assertEqual(control.extra_price_metrics["korea_zinc_initial_event_return_pct"], 19.8)
        self.assertEqual(control.stage_candidate, "Stage2 + 4B-watch")

        self.assertEqual(tc.extra_price_metrics["treatment_charge_2024_usd_per_ton"], 165)
        self.assertEqual(tc.extra_price_metrics["tc_decline_pct"], 40)
        self.assertEqual(tc.stage_candidate, "4B-watch")

        self.assertEqual(critical.extra_price_metrics["project_value_usd_bn"], 7.4)
        self.assertEqual(critical.extra_price_metrics["share_issuance_krw_trn"], 2.833)

        self.assertEqual(steel.extra_price_metrics["hyundai_steel_event_return_pct"], 5.8)
        self.assertEqual(steel.extra_price_metrics["hyundai_market_relative_pp"], 6.5)
        self.assertEqual(steel.stage_candidate, "Stage2-Actionable")

        self.assertEqual(louisiana.extra_price_metrics["louisiana_plant_investment_usd_bn"], 5.8)
        self.assertEqual(louisiana.extra_price_metrics["production_start_target"], 2029)

        self.assertEqual(petro.case_type, "failed_rerating")
        self.assertEqual(petro.extra_price_metrics["lotte_chemical_2024_op_loss_krw_bn"], 895)
        self.assertEqual(petro.rerating_result, "no_rerating")

        self.assertEqual(refining.score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(refining.extra_price_metrics["q1_2026_op_krw_trn"], 2.2)

        self.assertEqual(lithium.extra_price_metrics["deal_value_usd_mn"], 765)
        self.assertEqual(lithium.extra_price_metrics["posco_direct_price_anchor"], "price_data_unavailable_after_deep_search")

        self.assertEqual(rare.stage_candidate, "4B-watch")
        self.assertIn("electric_vehicles", rare.extra_price_metrics["affected_product_categories"])

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round325_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round325_shadow_weight_rows()}
        rules_md = render_round325_stage_rules_markdown()
        trigger_md = render_round325_trigger_grid_markdown()
        stage_md = render_round325_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND325_TRIGGER_RECORDS), 13)
        self.assertEqual(trigger_rows["r4l17_steel_antidumping_T0"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r4l17_korea_zinc_tc_T0"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r4l17_louisiana_steel_T1"]["promote_to"], "Stage2")
        self.assertEqual(trigger_rows["r4l17_petrochemical_restructuring_T2"]["promote_to"], "Stage2_relief")
        self.assertEqual(trigger_rows["r4l17_sk_innovation_refining_T0"]["promote_to"], "no_actionable")
        self.assertEqual(trigger_rows["r4l17_rare_earth_control_T0"]["promote_to"], "4B-watch")
        self.assertEqual(len(ROUND325_SHADOW_WEIGHT_ROWS), 10)
        self.assertEqual(shadow_rows["STEEL_ANTIDUMPING_PROTECTION_STAGE2"]["domestic_spread_protection"], "+5")
        self.assertEqual(shadow_rows["CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B"]["control_premium_as_operating_growth_penalty"], "-5")
        self.assertIn("tariff_anti_dumping_tender_contract_capex_or_policy_value_is_clear", ROUND325_STAGE2_ACTIONABLE_RULES)
        self.assertIn("funding_clarity_without_excessive_dilution", ROUND325_STAGE3_YELLOW_RULES)
        self.assertIn("spread_improvement_visible_in_earnings", ROUND325_STAGE3_GREEN_RULES)
        self.assertIn("control_premium_without_operating_margin", ROUND325_GREEN_BLOCKERS)
        self.assertIn("domestic_spread_protection", ROUND325_SCORE_UP_AXES)
        self.assertIn("control_premium_as_operating_growth", ROUND325_SCORE_DOWN_AXES)
        self.assertIn("zinc_TC_compression", ROUND325_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("large_dilution_spiral", ROUND325_HARD_4C_GATES)
        self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", ROUND325_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r4_loop17_hyundai_steel_posco_antidumping", trigger_md)
        self.assertIn("r4_loop17_china_rare_earth_export_control_korea", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round325_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_325.md")
        self.assertEqual(audit["round_id"], "round_253")
        self.assertEqual(audit["large_sector"], ROUND325_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_control_premium_anti_dumping_critical_capex_lithium_stake_or_restructuring_as_Green_without_margin_offtake_funding_and_risk_resolution", audit["what_not_to_change"])

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
            paths = write_round325_r4_loop17_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            loaded = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(loaded), 9)
            self.assertIn("Stage3-Green confirmed: `0`", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Full adjusted OHLC", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertGreater(len(round325_case_rows()), 0)


if __name__ == "__main__":
    unittest.main()
