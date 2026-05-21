from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round306_r11_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round306_r11_loop15_policy_geopolitical_event_trigger_validation import (
    ROUND306_CASE_CANDIDATES,
    ROUND306_GREEN_BLOCKERS,
    ROUND306_HARD_4C_GATES,
    ROUND306_LARGE_SECTOR,
    ROUND306_REQUIRED_TARGET_ALIASES,
    ROUND306_SCORE_DOWN_AXES,
    ROUND306_SCORE_UP_AXES,
    ROUND306_SHADOW_WEIGHT_ROWS,
    ROUND306_STAGE2_ACTIONABLE_RULES,
    ROUND306_STAGE3_GREEN_RULES,
    ROUND306_STAGE3_YELLOW_RULES,
    ROUND306_STAGE4B_WATCH_TRIGGERS,
    ROUND306_TRIGGER_RECORDS,
    render_round306_stage4b_4c_review_markdown,
    render_round306_stage_rules_markdown,
    render_round306_trigger_grid_markdown,
    round306_audit_payload,
    round306_case_records,
    round306_case_rows,
    round306_shadow_weight_rows,
    round306_summary,
    round306_trigger_rows,
    write_round306_r11_loop15_reports,
)


class Round306R11Loop15PolicyGeopoliticalEventTriggerValidationTests(unittest.TestCase):
    def test_round306_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND306_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND306_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND306_REQUIRED_TARGET_ALIASES["DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE"],
            E2RArchetype.DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND306_REQUIRED_TARGET_ALIASES["CHIP_EXPORT_CONTROL_4C_WATCH"],
            E2RArchetype.CHIP_EXPORT_CONTROL_4C_WATCH.value,
        )
        self.assertEqual(
            ROUND306_REQUIRED_TARGET_ALIASES["NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B"],
            E2RArchetype.NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B.value,
        )

    def test_archetype_definitions_capture_r11_loop15_rules(self) -> None:
        defense = archetype_definition(E2RArchetype.DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE)
        rotem = archetype_definition(E2RArchetype.GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW)
        export_control = archetype_definition(E2RArchetype.CHIP_EXPORT_CONTROL_4C_WATCH)
        strike = archetype_definition(E2RArchetype.SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH)
        politics = archetype_definition(E2RArchetype.POLITICAL_SYSTEM_SHOCK_MARKET_4C)
        hormuz = archetype_definition(E2RArchetype.HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF)
        naval = archetype_definition(E2RArchetype.NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B)
        disaster = archetype_definition(E2RArchetype.NATURAL_DISASTER_RECOVERY_STAGE2_REFERENCE)

        self.assertIn("cash collection", " ".join(defense.stage3_high_conviction_signals))
        self.assertIn("delivery-to-revenue", " ".join(rotem.stage2_candidate_signals))
        self.assertIn("upgrade ceiling", " ".join(export_control.stage1_radar_signals))
        self.assertIn("DRAM or NAND supply reduction", " ".join(strike.stage4c_thesis_break_signals))
        self.assertIn("false-break relief", " ".join(politics.false_positive_patterns))
        self.assertIn("alternative supply routes", " ".join(hormuz.false_positive_patterns))
        self.assertIn("formal U.S. Navy contract", " ".join(naval.stage3_high_conviction_signals))
        self.assertIn("listed-equity trigger", " ".join(disaster.stage2_candidate_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round306_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND306_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round306_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_policy_geopolitics_or_disaster_headline_as_green", record.green_guardrails)

        by_id = {record.case_id: record for record in records}
        self.assertIn("hard_4c_confirmed_false", by_id["r11_loop15_hanwha_aerospace_romania_k9"].green_guardrails)
        self.assertNotIn("hard_4c_confirmed_false", by_id["r11_loop15_martial_law_political_shock"].green_guardrails)

        summary = round306_summary()
        self.assertEqual(summary["round_id"], "round_234")
        self.assertEqual(summary["large_sector"], ROUND306_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 10)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 3)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 3)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_defense_policy_relief_and_hard_4c(self) -> None:
        by_id = {case.case_id: case for case in ROUND306_CASE_CANDIDATES}
        hanwha = by_id["r11_loop15_hanwha_aerospace_romania_k9"]
        rotem = by_id["r11_loop15_hyundai_rotem_poland_k2"]
        export_curbs = by_id["r11_loop15_samsung_skhynix_us_china_export_curbs"]
        strike = by_id["r11_loop15_samsung_labor_strike_risk"]
        politics = by_id["r11_loop15_martial_law_political_shock"]
        hormuz = by_id["r11_loop15_hormuz_energy_security_market_shock"]
        naval = by_id["r11_loop15_hanwha_ocean_us_naval_shipbuilding"]
        wildfire = by_id["r11_loop15_2025_korea_wildfires_disaster_reference"]

        self.assertEqual(hanwha.primary_archetype, E2RArchetype.DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE)
        self.assertEqual(hanwha.event_mfe_pct, 5.0)
        self.assertEqual(hanwha.extra_price_metrics["defense_backlog_mar_2024_krw_trn"], 30)

        self.assertEqual(rotem.primary_archetype, E2RArchetype.GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW)
        self.assertEqual(rotem.event_mfe_pct, 9.3)
        self.assertEqual(rotem.extra_price_metrics["market_relative_return_pp"], 9.6)
        self.assertEqual(rotem.extra_price_metrics["second_contract_value_usd_bn"], 6.5)

        self.assertEqual(export_curbs.primary_archetype, E2RArchetype.CHIP_EXPORT_CONTROL_4C_WATCH)
        self.assertEqual(export_curbs.event_mae_pct, -4.4)
        self.assertIn("china_fab_upgrade_ceiling", export_curbs.red_flag_fields)

        self.assertEqual(strike.primary_archetype, E2RArchetype.SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH)
        self.assertEqual(strike.extra_price_metrics["potential_dram_supply_reduction_pct"], 4)

        self.assertTrue(politics.hard_4c_confirmed)
        self.assertEqual(politics.extra_price_metrics["korea_etf_trimmed_loss_pct"], -1.7)

        self.assertEqual(hormuz.primary_archetype, E2RArchetype.HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF)
        self.assertEqual(hormuz.extra_price_metrics["alternative_route_crude_secured_mn_barrels"], 273)
        self.assertIn("energy_supply_relief_not_growth", hormuz.red_flag_fields)

        self.assertEqual(naval.primary_archetype, E2RArchetype.NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B)
        self.assertEqual(naval.extra_price_metrics["hanwha_ocean_2025_ytd_return_pct"], 139)
        self.assertEqual(naval.score_price_alignment, "false_positive_score")

        self.assertEqual(wildfire.primary_archetype, E2RArchetype.NATURAL_DISASTER_RECOVERY_STAGE2_REFERENCE)
        self.assertEqual(wildfire.extra_price_metrics["reported_burned_area_hectares_reuters"], 48000)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round306_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round306_shadow_weight_rows()}
        rules_md = render_round306_stage_rules_markdown()
        trigger_md = render_round306_trigger_grid_markdown()
        stage_md = render_round306_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND306_TRIGGER_RECORDS), 10)
        self.assertEqual(trigger_rows["r11l15_hanwha_k9_romania_T1"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r11l15_martial_law_T0"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r11l15_hormuz_T2"]["promote_to"], "Stage2_relief")
        self.assertEqual(len(ROUND306_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE"]["signed_defense_contract_value"], "+5")
        self.assertEqual(shadow_rows["GROUND_WEAPON_EXPORT_DELIVERY_STAGE2_YELLOW"]["delivery_to_revenue_conversion"], "+5")
        self.assertEqual(shadow_rows["HORMUZ_ENERGY_SECURITY_4C_WITH_POLICY_RELIEF"]["policy_relief_without_earnings_penalty"], "-5")
        self.assertIn("policy_or_geopolitical_headline_closes_into_signed_contract_or_delivery", ROUND306_STAGE2_ACTIONABLE_RULES)
        self.assertIn("naval_shipbuilding_policy_optionality_visible_but_formal_contract_or_tech_transfer_pending", ROUND306_STAGE3_YELLOW_RULES)
        self.assertIn("labor_export_control_political_and_energy_risks_are_cleared", ROUND306_STAGE3_GREEN_RULES)
        self.assertIn("political_false_break_as_structural", ROUND306_GREEN_BLOCKERS)
        self.assertIn("signed_defense_contract_value", ROUND306_SCORE_UP_AXES)
        self.assertIn("energy_supply_relief_as_growth", ROUND306_SCORE_DOWN_AXES)
        self.assertIn("naval_nuclear_sub_story_rises_before_formal_US_Navy_contract_or_tech_transfer_terms", ROUND306_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("martial_law_or_political_system_shock", ROUND306_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r11_loop15_hanwha_ocean_us_naval_shipbuilding", trigger_md)
        self.assertIn("r11_loop15_martial_law_political_shock", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round306_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_306.md")
        self.assertEqual(audit["round_id"], "round_234")
        self.assertEqual(audit["large_sector"], ROUND306_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_policy_geopolitics_or_disaster_headline_as_green", audit["what_not_to_change"])

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
            paths = write_round306_r11_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round306_case_rows()
            self.assertEqual(len(records), len(ROUND306_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND306_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND306_TRIGGER_RECORDS))


if __name__ == "__main__":
    unittest.main()
