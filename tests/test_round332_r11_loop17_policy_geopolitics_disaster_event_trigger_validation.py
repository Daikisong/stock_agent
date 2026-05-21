from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round332_r11_loop17_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round332_r11_loop17_policy_geopolitics_disaster_event_trigger_validation import (
    ROUND332_CASE_CANDIDATES,
    ROUND332_GREEN_BLOCKERS,
    ROUND332_HARD_4C_GATES,
    ROUND332_LARGE_SECTOR,
    ROUND332_REQUIRED_TARGET_ALIASES,
    ROUND332_ROW_SEPARATION_RULES,
    ROUND332_SCORE_DOWN_AXES,
    ROUND332_SCORE_UP_AXES,
    ROUND332_SHADOW_WEIGHT_ROWS,
    ROUND332_STAGE2_ACTIONABLE_RULES,
    ROUND332_STAGE3_GREEN_RULES,
    ROUND332_STAGE3_YELLOW_RULES,
    ROUND332_STAGE4B_WATCH_TRIGGERS,
    ROUND332_TRIGGER_RECORDS,
    render_round332_stage4b_4c_review_markdown,
    render_round332_stage_rules_markdown,
    render_round332_trigger_grid_markdown,
    round332_audit_payload,
    round332_case_records,
    round332_case_rows,
    round332_shadow_weight_rows,
    round332_summary,
    round332_trigger_rows,
    write_round332_r11_loop17_reports,
)


class Round332R11Loop17PolicyGeopoliticsDisasterTests(unittest.TestCase):
    def test_round332_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND332_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND332_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND332_REQUIRED_TARGET_ALIASES["COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE"],
            E2RArchetype.COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND332_REQUIRED_TARGET_ALIASES["MARTIAL_LAW_POLITICAL_RISK_4B"],
            E2RArchetype.MARTIAL_LAW_POLITICAL_RISK_4B.value,
        )
        self.assertEqual(
            ROUND332_REQUIRED_TARGET_ALIASES["WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE"],
            E2RArchetype.WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE.value,
        )

    def test_archetype_definitions_capture_round332_rules(self) -> None:
        commercial = archetype_definition(E2RArchetype.COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE)
        tax = archetype_definition(E2RArchetype.TAX_POLICY_RELIEF_STAGE2_WITH_TAX_4B)
        martial = archetype_definition(E2RArchetype.MARTIAL_LAW_POLITICAL_RISK_4B)
        ai_tax = archetype_definition(E2RArchetype.AI_WINDFALL_TAX_POLICY_OVERHANG_4B)
        chip = archetype_definition(E2RArchetype.CHIP_EXPORT_CONTROL_4B_WITH_POLICY_RELIEF)
        support = archetype_definition(E2RArchetype.SEMICONDUCTOR_TARIFF_SUPPORT_STAGE2_RELIEF)
        defense = archetype_definition(E2RArchetype.DEFENSE_GEOPOLITICAL_EXPORT_STAGE2_WITH_DILUTION_4B)
        labor = archetype_definition(E2RArchetype.NATIONAL_CHAMPION_LABOR_STRIKE_4B)
        disaster = archetype_definition(E2RArchetype.WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE)

        self.assertIn("minority shareholders", " ".join(commercial.stage2_candidate_signals))
        self.assertIn("company-level buyback cancellation", " ".join(commercial.stage3_high_conviction_signals))
        self.assertIn("transaction tax", " ".join(tax.stage4b_graduation_overheat_signals))
        self.assertIn("martial law", " ".join(martial.stage1_radar_signals))
        self.assertIn("liquidity backstop without political resolution", " ".join(martial.stage4b_graduation_overheat_signals))
        self.assertIn("AI windfall tax", " ".join(ai_tax.stage1_radar_signals))
        self.assertIn("VEU waiver revocation", " ".join(chip.stage1_radar_signals))
        self.assertIn("company-level order conversion", " ".join(support.stage3_high_conviction_signals))
        self.assertIn("dilution absorption", " ".join(defense.stage3_high_conviction_signals))
        self.assertIn("government arbitration", " ".join(labor.stage1_radar_signals))
        self.assertIn("fatal disaster", " ".join(disaster.stage4c_thesis_break_signals))
        self.assertIn("public-stock price anchor", " ".join(disaster.false_positive_patterns))

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round332_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND332_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round332_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", record.green_guardrails)

        summary = round332_summary()
        self.assertEqual(summary["round_id"], "round_260")
        self.assertEqual(summary["loop_name"], "R11 Loop 17")
        self.assertEqual(summary["large_sector"], ROUND332_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 9)
        self.assertEqual(summary["trigger_count"], 12)
        self.assertEqual(summary["target_archetype_count"], 9)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 3)
        self.assertEqual(summary["stage2_candidate_count"], 5)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 8)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["price_unavailable_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])

    def test_case_metrics_separate_policy_tax_political_chip_defense_labor_and_disaster(self) -> None:
        by_id = {case.case_id: case for case in ROUND332_CASE_CANDIDATES}
        commercial = by_id["r11_loop17_commercial_act_valueup"]
        tax = by_id["r11_loop17_capital_gains_tax_reversal"]
        martial = by_id["r11_loop17_martial_law_liquidity_intervention"]
        ai_tax = by_id["r11_loop17_ai_windfall_tax_policy_overhang"]
        chip = by_id["r11_loop17_us_chip_waiver_revocation"]
        support = by_id["r11_loop17_semiconductor_support_33t"]
        hanwha = by_id["r11_loop17_hanwha_defense_export_dilution"]
        strike = by_id["r11_loop17_samsung_strike_government_arbitration"]
        wildfire = by_id["r11_loop17_south_korea_wildfire_disaster"]

        self.assertEqual(commercial.extra_price_metrics["kospi_event_return_pct"], 1.34)
        self.assertEqual(commercial.extra_price_metrics["kospi_close_points"], 3116.27)
        self.assertIn("company_specific_action_missing", commercial.red_flag_fields)

        self.assertEqual(tax.extra_price_metrics["tax_shock_kospi_return_pct"], -3.9)
        self.assertEqual(tax.extra_price_metrics["relief_kospi_return_ft_pct"], 0.9)
        self.assertEqual(tax.extra_price_metrics["large_shareholder_threshold_proposed_krw_bn"], 1)

        self.assertEqual(martial.extra_price_metrics["kospi_event_return_pct"], -1.44)
        self.assertEqual(martial.extra_price_metrics["market_stabilization_fund_krw_trn"], 10)
        self.assertFalse(martial.hard_4c_confirmed)

        self.assertEqual(ai_tax.extra_price_metrics["kospi_intraday_drop_pct"], -5.0)
        self.assertEqual(ai_tax.extra_price_metrics["kospi_close_return_pct"], -2.3)

        self.assertEqual(chip.extra_price_metrics["sk_hynix_event_return_pct"], "nearly_-5")
        self.assertIn("US_license_dependency_4B", chip.red_flag_fields)

        self.assertEqual(support.extra_price_metrics["semiconductor_support_krw_trn"], 33)
        self.assertEqual(support.score_price_alignment, "unknown")

        self.assertEqual(hanwha.extra_price_metrics["romania_order_value_usd_bn"], 1.0)
        self.assertEqual(hanwha.extra_price_metrics["dilution_event_return_pct"], -13)
        self.assertIn("share_dilution_4B", hanwha.red_flag_fields)

        self.assertEqual(strike.extra_price_metrics["event_return_pct"], -9.3)
        self.assertEqual(strike.extra_price_metrics["single_day_direct_loss_krw_trn"], 1)

        self.assertTrue(wildfire.hard_4c_confirmed)
        self.assertEqual(wildfire.extra_price_metrics["fatalities_followup_context"], 26)
        self.assertEqual(wildfire.extra_price_metrics["burned_area_hectares_context"], 48000)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round332_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round332_shadow_weight_rows()}
        rules_md = render_round332_stage_rules_markdown()
        trigger_md = render_round332_trigger_grid_markdown()
        stage_md = render_round332_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND332_TRIGGER_RECORDS), 12)
        self.assertEqual(trigger_rows["r11l17_commercial_act_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r11l17_tax_shock_T0"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r11l17_tax_reversal_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r11l17_wildfire_T0"]["promote_to"], "4C_disaster_watch")
        self.assertEqual(len(ROUND332_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE"]["governance_reform_law"], "+5")
        self.assertEqual(shadow_rows["CHIP_EXPORT_CONTROL_4B_WITH_POLICY_RELIEF"]["geopolitical_export_control_risk"], "+5")
        self.assertEqual(shadow_rows["WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE"]["disaster_hard_4c"], "+5")
        self.assertIn("law_policy_contract_disaster_or_labor_event_has_clear_public_date", ROUND332_STAGE2_ACTIONABLE_RULES)
        self.assertIn("industrial_support_converts_to_equipment_material_or_factory_orders", ROUND332_STAGE3_YELLOW_RULES)
        self.assertIn("tax_uncertainty_is_durably_removed", ROUND332_STAGE3_GREEN_RULES)
        self.assertIn("AI_tax_noise_ignored", ROUND332_GREEN_BLOCKERS)
        self.assertIn("labor_supply_chain_risk", ROUND332_SCORE_UP_AXES)
        self.assertIn("disaster_without_price_anchor_penalty", ROUND332_SCORE_DOWN_AXES)
        self.assertIn("US_export_controls_affect_Korean_strategic_assets", ROUND332_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_wildfire_disaster_with_large_asset_destruction", ROUND332_HARD_4C_GATES)
        self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", ROUND332_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r11_loop17_commercial_act_valueup", trigger_md)
        self.assertIn("r11_loop17_south_korea_wildfire_disaster", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round332_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_332.md")
        self.assertEqual(audit["round_id"], "round_260")
        self.assertEqual(audit["large_sector"], ROUND332_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_change_production_scoring", audit["what_not_to_change"])
        self.assertIn("do_not_use_round332_cases_as_candidate_generation_input", audit["what_not_to_change"])

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
            paths = write_round332_r11_loop17_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round332_case_rows()
            self.assertEqual(len(records), len(ROUND332_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND332_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND332_TRIGGER_RECORDS))
            self.assertIn("Commercial Act", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r11l17_wildfire_T0", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("AI_WINDFALL_TAX_POLICY_OVERHANG_4B", paths["weight_profile"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
