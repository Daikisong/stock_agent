from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round280_r11_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round280_r11_loop13_policy_geopolitical_disaster_event_price_validation import (
    ROUND280_CASE_CANDIDATES,
    ROUND280_GREEN_FORBIDDEN_PATTERNS,
    ROUND280_GREEN_REQUIRED_FIELDS,
    ROUND280_HARD_4C_GATES,
    ROUND280_LARGE_SECTOR,
    ROUND280_PRICE_VALIDATION_FIELDS,
    ROUND280_REQUIRED_TARGET_ALIASES,
    ROUND280_SHADOW_WEIGHT_ROWS,
    ROUND280_STAGE4B_WATCH_TRIGGERS,
    render_round280_green_gate_review_markdown,
    render_round280_stage4b_4c_review_markdown,
    round280_audit_payload,
    round280_case_records,
    round280_case_rows,
    round280_deep_sub_archetype_rows,
    round280_shadow_weight_rows,
    round280_summary,
    write_round280_r11_loop13_reports,
)


class Round280R11Loop13PolicyGeopoliticalDisasterEventPriceValidationTests(unittest.TestCase):
    def test_round280_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND280_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND280_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND280_REQUIRED_TARGET_ALIASES["POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE"],
            E2RArchetype.POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE.value,
        )
        self.assertEqual(
            ROUND280_REQUIRED_TARGET_ALIASES["MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C"],
            E2RArchetype.MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C.value,
        )
        self.assertEqual(
            ROUND280_REQUIRED_TARGET_ALIASES["CHINA_FAB_EXPORT_LICENSE_RELIEF"],
            E2RArchetype.CHINA_FAB_EXPORT_LICENSE_RELIEF.value,
        )

    def test_round280_archetype_definitions_capture_r11_loop13_gates(self) -> None:
        political = archetype_definition(E2RArchetype.POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE)
        middle_east = archetype_definition(E2RArchetype.MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C)
        ai_windfall = archetype_definition(E2RArchetype.AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT)
        labor = archetype_definition(E2RArchetype.SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION)
        tariff = archetype_definition(E2RArchetype.US_KOREA_TARIFF_POLICY_4C_WATCH)
        china_fab = archetype_definition(E2RArchetype.CHINA_FAB_EXPORT_LICENSE_RELIEF)
        climate = archetype_definition(E2RArchetype.CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE)

        self.assertIn("martial law", political.stage4c_thesis_break_signals)
        self.assertIn("KRW 1500 breach", middle_east.stage4c_thesis_break_signals)
        self.assertIn("AI fiscal redistribution comment treated as company Green", ai_windfall.false_positive_patterns)
        self.assertIn("labor relief treated as Green before production continuity", labor.false_positive_patterns)
        self.assertIn("tariff cut treated as Green without margin bridge", tariff.false_positive_patterns)
        self.assertIn("annual license treated as multiyear Green", china_fab.false_positive_patterns)
        self.assertIn("disaster rebuild story without loss assessment", climate.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round280_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND280_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_true_for_macro_geopolitical_political_disaster_reference", record.green_guardrails)
            self.assertIn("do_not_use_round280_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round280_summary()
        self.assertEqual(summary["round_id"], "round_208")
        self.assertEqual(summary["large_sector"], "POLICY_GEOPOLITICS_DISASTER_EVENT")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["policy_relief_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 3)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 1)
        self.assertEqual(summary["stage4c_watch_count"], 6)
        self.assertEqual(summary["price_moved_without_evidence_count"], 1)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_policy_geopolitical_disaster_cases_keep_event_anchors_separate_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND280_CASE_CANDIDATES}
        martial = by_id["r11_loop13_martial_law_korea_discount_political_shock"]
        iran = by_id["r11_loop13_iran_middle_east_energy_fx_macro_hard_4c"]
        ai_bonus = by_id["r11_loop13_ai_bonus_fiscal_redistribution_event"]
        strike = by_id["r11_loop13_samsung_strike_emergency_arbitration_supply_chain"]
        rare = by_id["r11_loop13_china_rare_earth_export_control_supply_chain"]
        tariff = by_id["r11_loop13_us_korea_tariff_auto_semis_pharma_policy"]
        fab = by_id["r11_loop13_samsung_sk_china_fab_tool_license_relief"]
        wildfire = by_id["r11_loop13_2025_south_korea_wildfires_disaster_reference"]

        self.assertEqual(martial.primary_archetype, E2RArchetype.POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE)
        self.assertEqual(martial.extra_price_metrics["stock_market_stabilisation_fund_krw_trn"], 10.0)
        self.assertEqual(martial.extra_price_metrics["martial_law_duration_hours"], 6)
        self.assertEqual(martial.event_mae_pct, -1.4)
        self.assertTrue(martial.hard_4c_confirmed)

        self.assertEqual(iran.primary_archetype, E2RArchetype.MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C)
        self.assertEqual(iran.stage4c_price_anchor, 5093.54)
        self.assertEqual(iran.extra_price_metrics["kospi_close_mae_pct"], -12.06)
        self.assertEqual(iran.extra_price_metrics["won_intraday_low_per_usd"], 1505.8)
        self.assertEqual(iran.extra_price_metrics["middle_east_oil_purchase_share_pct"], 70)
        self.assertEqual(iran.extra_price_metrics["hyundai_motor_event_mae_pct"], -15.8)
        self.assertTrue(iran.hard_4c_confirmed)

        self.assertEqual(ai_bonus.primary_archetype, E2RArchetype.AI_WINDFALL_FISCAL_REDISTRIBUTION_EVENT)
        self.assertEqual(ai_bonus.extra_price_metrics["samsung_event_mae_pct"], -3.5)
        self.assertFalse(ai_bonus.extra_price_metrics["corporate_profit_seizure_confirmed"])
        self.assertEqual(ai_bonus.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(strike.primary_archetype, E2RArchetype.SYSTEMIC_LABOR_SUPPLY_CHAIN_INTERVENTION)
        self.assertEqual(strike.extra_price_metrics["threatened_workers"], 45000)
        self.assertEqual(strike.extra_price_metrics["one_day_direct_loss_krw_trn"], 1.0)
        self.assertEqual(strike.extra_price_metrics["samsung_export_share_pct"], 22.8)
        self.assertFalse(strike.hard_4c_confirmed)

        self.assertEqual(rare.primary_archetype, E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C)
        self.assertEqual(rare.extra_price_metrics["processed_rare_earths_china_share_pct"], 90)
        self.assertEqual(rare.extra_price_metrics["heavy_rare_earth_exports_decline_since_controls_pct"], -50)
        self.assertEqual(rare.extra_price_metrics["advanced_semiconductor_license_policy"], "case_by_case")
        self.assertIn("Hanwha Ocean", rare.extra_price_metrics["korea_affected_companies_context"])

        self.assertEqual(tariff.primary_archetype, E2RArchetype.US_KOREA_TARIFF_POLICY_4C_WATCH)
        self.assertEqual(tariff.extra_price_metrics["auto_tariff_new_pct"], 15)
        self.assertEqual(tariff.extra_price_metrics["hyundai_event_mae_pct"], -4.5)
        self.assertEqual(tariff.extra_price_metrics["kia_event_mae_pct"], -6.6)
        self.assertEqual(tariff.extra_price_metrics["strategic_us_investment_commitment_usd_bn"], 350)
        self.assertEqual(tariff.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(fab.primary_archetype, E2RArchetype.CHINA_FAB_EXPORT_LICENSE_RELIEF)
        self.assertTrue(fab.extra_price_metrics["annual_approval_system"])
        self.assertFalse(fab.extra_price_metrics["multi_year_visibility_confirmed"])
        self.assertEqual(fab.extra_price_metrics["license_period"], "2026_annual_license")

        self.assertEqual(wildfire.primary_archetype, E2RArchetype.CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE)
        self.assertEqual(wildfire.extra_price_metrics["fatalities_final_context"], 32)
        self.assertEqual(wildfire.extra_price_metrics["area_burned_hectares"], 104000)
        self.assertTrue(wildfire.hard_4c_confirmed)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND280_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND280_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND280_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round280_shadow_weight_rows()}
        deep_rows = round280_deep_sub_archetype_rows()
        green_markdown = render_round280_green_gate_review_markdown()
        stage_markdown = render_round280_stage4b_4c_review_markdown()

        self.assertIn("policy_law_budget_execution_confirmed", required)
        self.assertIn("labor_production_continuity_confirmed", required)
        self.assertIn("tariff_cut_without_margin_bridge", forbidden)
        self.assertIn("disaster_rebuild_story_without_loss_assessment", forbidden)
        self.assertIn("AI_chip_rally_then_redistribution_tax_comment_selloff", ROUND280_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fx_disorderly_move_or_won_1500_breach", ROUND280_HARD_4C_GATES)
        self.assertIn("fx_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Iran", stage_markdown)
        self.assertIn("hard-4C", stage_markdown)
        self.assertEqual(len(ROUND280_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["US_KOREA_TARIFF_POLICY_4C_WATCH"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE"]["disaster_loss_exposure"], "+5")
        self.assertTrue(any("martial law" in row["terms"] for row in deep_rows))
        self.assertTrue(any("2025 wildfires" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round280_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_280.md")
        self.assertEqual(audit["round_id"], "round_208")
        self.assertEqual(audit["large_sector"], ROUND280_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round280_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round280_r11_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round280_case_rows()
            self.assertEqual(len(records), len(ROUND280_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND280_CASE_CANDIDATES))
            self.assertIn("AI windfall", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("policy_law_budget_execution_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("MIDDLE_EAST_ENERGY_FX_MACRO_HARD_4C", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("fx_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[1]["extra_price_metrics"])["kospi_close_mae_pct"], -12.06)


if __name__ == "__main__":
    unittest.main()
