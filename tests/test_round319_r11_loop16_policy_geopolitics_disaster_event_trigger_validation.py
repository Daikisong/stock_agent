from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round319_r11_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round319_r11_loop16_policy_geopolitics_disaster_event_trigger_validation import (
    ROUND319_CASE_CANDIDATES,
    ROUND319_GREEN_BLOCKERS,
    ROUND319_HARD_4C_GATES,
    ROUND319_LARGE_SECTOR,
    ROUND319_REQUIRED_TARGET_ALIASES,
    ROUND319_ROW_SEPARATION_RULES,
    ROUND319_SCORE_DOWN_AXES,
    ROUND319_SCORE_UP_AXES,
    ROUND319_SHADOW_WEIGHT_ROWS,
    ROUND319_STAGE2_ACTIONABLE_RULES,
    ROUND319_STAGE3_GREEN_RULES,
    ROUND319_STAGE3_YELLOW_RULES,
    ROUND319_STAGE4B_WATCH_TRIGGERS,
    ROUND319_TRIGGER_RECORDS,
    render_round319_stage_rules_markdown,
    render_round319_stage4b_4c_review_markdown,
    render_round319_trigger_grid_markdown,
    round319_audit_payload,
    round319_case_records,
    round319_case_rows,
    round319_shadow_weight_rows,
    round319_summary,
    round319_trigger_rows,
    write_round319_r11_loop16_reports,
)


class Round319R11Loop16PolicyGeopoliticsDisasterTests(unittest.TestCase):
    def test_round319_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND319_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND319_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND319_REQUIRED_TARGET_ALIASES["GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE"],
            E2RArchetype.GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND319_REQUIRED_TARGET_ALIASES["POLITICAL_CRISIS_MARKET_HARD_4C"],
            E2RArchetype.POLITICAL_CRISIS_MARKET_HARD_4C.value,
        )
        self.assertEqual(
            ROUND319_REQUIRED_TARGET_ALIASES["NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF"],
            E2RArchetype.NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF.value,
        )

    def test_archetype_definitions_capture_r11_loop16_rules(self) -> None:
        defense = archetype_definition(E2RArchetype.GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE)
        missile = archetype_definition(E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW)
        nuclear = archetype_definition(E2RArchetype.NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B)
        political = archetype_definition(E2RArchetype.POLITICAL_CRISIS_MARKET_HARD_4C)
        commercial = archetype_definition(E2RArchetype.COMMERCIAL_ACT_VALUEUP_STAGE2_POLICY)
        foreign = archetype_definition(E2RArchetype.FOREIGN_STRATEGIC_CAPITAL_POLICY_STAGE2_ACTIONABLE)
        short = archetype_definition(E2RArchetype.SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B)
        disaster = archetype_definition(E2RArchetype.NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF)

        self.assertIn("production capacity", " ".join(defense.stage3_high_conviction_signals))
        self.assertIn("delivery margin", " ".join(defense.stage3_high_conviction_signals))
        self.assertIn("combat validation", " ".join(missile.stage3_high_conviction_signals))
        self.assertIn("production ramp", " ".join(missile.stage3_high_conviction_signals))
        self.assertIn("final contract", " ".join(nuclear.stage3_high_conviction_signals))
        self.assertIn("legal challenge", " ".join(nuclear.stage4b_graduation_overheat_signals))
        self.assertIn("martial law", " ".join(political.stage1_radar_signals))
        self.assertIn("KRW", " ".join(political.stage1_radar_signals))
        self.assertIn("minority shareholders", " ".join(commercial.stage1_radar_signals))
        self.assertIn("buyback cancellation", " ".join(commercial.stage3_high_conviction_signals))
        self.assertIn("ROIC", " ".join(foreign.stage3_high_conviction_signals))
        self.assertIn("CB dilution", " ".join(foreign.stage4b_graduation_overheat_signals))
        self.assertIn("foreign flow", " ".join(short.stage3_high_conviction_signals))
        self.assertIn("liquidity", " ".join(short.stage3_high_conviction_signals))
        self.assertIn("reconstruction budget", " ".join(disaster.stage2_candidate_signals))
        self.assertIn("insurance loss", " ".join(disaster.stage3_high_conviction_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round319_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND319_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round319_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn(
                "do_not_treat_policy_defense_nuclear_disaster_or_market_integrity_headline_as_Green_without_law_contract_budget_delivery_margin_ROIC_or_company_execution",
                record.green_guardrails,
            )

        by_id = {record.case_id: record for record in records}
        self.assertIn("hard_4c_confirmed_false", by_id["r11_loop16_hanwha_aerospace_romania_defense_export"].green_guardrails)
        self.assertNotIn("hard_4c_confirmed_false", by_id["r11_loop16_martial_law_political_shock"].green_guardrails)
        self.assertNotIn("hard_4c_confirmed_false", by_id["r11_loop16_2025_wildfire_disaster_relief"].green_guardrails)

        summary = round319_summary()
        self.assertEqual(summary["round_id"], "round_247")
        self.assertEqual(summary["large_sector"], ROUND319_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 11)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 4)
        self.assertEqual(summary["stage2_candidate_count"], 6)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 5)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_defense_nuclear_policy_disaster_and_market_structure(self) -> None:
        by_id = {case.case_id: case for case in ROUND319_CASE_CANDIDATES}
        hanwha = by_id["r11_loop16_hanwha_aerospace_romania_defense_export"]
        lig = by_id["r11_loop16_lig_nex1_iraq_msam_iran_validation"]
        nuclear = by_id["r11_loop16_khnp_czech_nuclear_export"]
        martial = by_id["r11_loop16_martial_law_political_shock"]
        commercial = by_id["r11_loop16_commercial_act_valueup"]
        samsung = by_id["r11_loop16_samsung_sds_kkr_strategic_capital"]
        short = by_id["r11_loop16_short_selling_market_integrity"]
        wildfire = by_id["r11_loop16_2025_wildfire_disaster_relief"]

        self.assertEqual(hanwha.primary_archetype, E2RArchetype.GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE)
        self.assertEqual(hanwha.extra_price_metrics["contract_value_usd_bn"], 1.0)
        self.assertEqual(hanwha.event_mae_pct, -13.0)
        self.assertIn("dilution_4B", hanwha.red_flag_fields)

        self.assertEqual(lig.extra_price_metrics["iraq_contract_value_krw_trn"], 3.71)
        self.assertEqual(lig.extra_price_metrics["iran_war_share_return_context_pct"], 47)
        self.assertEqual(lig.stage_failure_type, "yellow_success")

        self.assertEqual(nuclear.extra_price_metrics["doosan_3m_return_context_pct"], 48)
        self.assertIn("Czech_court_legal_4B", nuclear.red_flag_fields)

        self.assertTrue(martial.hard_4c_confirmed)
        self.assertEqual(martial.primary_archetype, E2RArchetype.POLITICAL_CRISIS_MARKET_HARD_4C)
        self.assertEqual(martial.extra_price_metrics["company_specific_trigger"], False)

        self.assertEqual(commercial.extra_price_metrics["kospi_event_close"], 3116.27)
        self.assertIn("buyback_cancellation_missing", commercial.red_flag_fields)

        self.assertEqual(samsung.extra_price_metrics["convertible_bond_value_usd_mn"], 820)
        self.assertEqual(samsung.extra_price_metrics["market_relative_morning_pp"], 16.4)

        self.assertEqual(short.extra_price_metrics["fine_for_serious_violation_pct_of_short_sale_orders"], 100)
        self.assertIn("market_liquidity_improvement_missing", short.red_flag_fields)

        self.assertTrue(wildfire.hard_4c_confirmed)
        self.assertEqual(wildfire.extra_price_metrics["area_burned_hectares_context"], 48000)
        self.assertIn("listed_company_contracts_missing", wildfire.red_flag_fields)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round319_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round319_shadow_weight_rows()}
        rules_md = render_round319_stage_rules_markdown()
        trigger_md = render_round319_trigger_grid_markdown()
        stage_md = render_round319_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND319_TRIGGER_RECORDS), 11)
        self.assertEqual(trigger_rows["r11l16_hanwha_romania_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r11l16_hanwha_dilution_T4"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r11l16_lig_iran_validation_T2"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r11l16_martial_law_T0"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r11l16_wildfire_disaster_T0"]["promote_to"], "4C_reference")
        self.assertEqual(len(ROUND319_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE"]["defense_export_contract_value"], "+5")
        self.assertEqual(shadow_rows["MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW"]["combat_validation"], "+5")
        self.assertEqual(shadow_rows["NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B"]["preferred_bidder_without_contract_penalty"], "-5")
        self.assertIn("contract_or_order_value_is_clear", ROUND319_STAGE2_ACTIONABLE_RULES)
        self.assertIn("one_of_delivery_legal_resolution_final_budget_or_company_specific_execution_remains_open", ROUND319_STAGE3_YELLOW_RULES)
        self.assertIn("foreign_strategic_capital_converts_to_ROIC_and_earnings", ROUND319_STAGE3_GREEN_RULES)
        self.assertIn("market_rule_without_flow_data", ROUND319_GREEN_BLOCKERS)
        self.assertIn("combat_validation", ROUND319_SCORE_UP_AXES)
        self.assertIn("political_crisis_treated_as_one_day_event", ROUND319_SCORE_DOWN_AXES)
        self.assertIn("political_shock_hits_KRW_KOSPI_or_ETF_confidence", ROUND319_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("martial_law_or_constitutional_crisis", ROUND319_HARD_4C_GATES)
        self.assertIn("trigger_calibration_row_stores_event_anchor_contract_policy_legal_disaster_or_market_structure_metrics", ROUND319_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r11_loop16_hanwha_aerospace_romania_defense_export", trigger_md)
        self.assertIn("r11_loop16_2025_wildfire_disaster_relief", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round319_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_319.md")
        self.assertEqual(audit["round_id"], "round_247")
        self.assertEqual(audit["large_sector"], ROUND319_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_policy_defense_nuclear_disaster_or_market_integrity_headline_as_Green_without_law_contract_budget_delivery_margin_ROIC_or_company_execution", audit["what_not_to_change"])

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
            paths = write_round319_r11_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round319_case_rows()
            self.assertEqual(len(records), len(ROUND319_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND319_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND319_TRIGGER_RECORDS))
            self.assertIn("Hanwha Aerospace / Romania K9", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage3-Green", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r11l16_martial_law_T0", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE", paths["weight_profiles"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["defense_backlog_mar_2024_krw_trn"], 30)


if __name__ == "__main__":
    unittest.main()
