from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round299_r4_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round299_r4_loop15_materials_spread_strategic_trigger_validation import (
    ROUND299_CASE_CANDIDATES,
    ROUND299_GREEN_BLOCKERS,
    ROUND299_HARD_4C_GATES,
    ROUND299_LARGE_SECTOR,
    ROUND299_REQUIRED_TARGET_ALIASES,
    ROUND299_SCORE_DOWN_AXES,
    ROUND299_SCORE_UP_AXES,
    ROUND299_SHADOW_WEIGHT_ROWS,
    ROUND299_STAGE2_ACTIONABLE_RULES,
    ROUND299_STAGE3_GREEN_RULES,
    ROUND299_STAGE3_YELLOW_RULES,
    ROUND299_STAGE4B_WATCH_TRIGGERS,
    ROUND299_TRIGGER_RECORDS,
    render_round299_stage_rules_markdown,
    render_round299_stage4b_4c_review_markdown,
    render_round299_trigger_grid_markdown,
    round299_audit_payload,
    round299_case_records,
    round299_case_rows,
    round299_shadow_weight_rows,
    round299_summary,
    round299_trigger_rows,
    write_round299_r4_loop15_reports,
)


class Round299R4Loop15MaterialsSpreadStrategicTriggerValidationTests(unittest.TestCase):
    def test_round299_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND299_REQUIRED_TARGET_ALIASES), 10)
        self.assertTrue(set(ROUND299_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND299_REQUIRED_TARGET_ALIASES["GRAPHITE_TARIFF_STAGE2_ACTIONABLE"],
            E2RArchetype.GRAPHITE_TARIFF_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND299_REQUIRED_TARGET_ALIASES["KOREA_ZINC_CONTROL_PREMIUM_4B"],
            E2RArchetype.KOREA_ZINC_CONTROL_PREMIUM_4B.value,
        )
        self.assertEqual(
            ROUND299_REQUIRED_TARGET_ALIASES["CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C"],
            E2RArchetype.CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C.value,
        )

    def test_archetype_definitions_capture_r4_loop15_rules(self) -> None:
        graphite = archetype_definition(E2RArchetype.GRAPHITE_TARIFF_STAGE2_ACTIONABLE)
        steel = archetype_definition(E2RArchetype.STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE)
        weak_steel = archetype_definition(E2RArchetype.STEEL_WEAK_DEMAND_FAILED_RERATING)
        capex = archetype_definition(E2RArchetype.LOCALIZATION_CAPEX_FALSE_POSITIVE)
        zinc_control = archetype_definition(E2RArchetype.KOREA_ZINC_CONTROL_PREMIUM_4B)
        zinc_refinery = archetype_definition(E2RArchetype.CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B)
        copper = archetype_definition(E2RArchetype.COPPER_TCRC_SPREAD_4C_WATCH)
        export_control = archetype_definition(E2RArchetype.CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C)

        self.assertIn("non-China graphite capacity and quality certification partly visible", graphite.stage2_candidate_signals)
        self.assertIn("ASP, volume, utilization", steel.stage3_high_conviction_signals)
        self.assertIn("net-profit estimate cut", weak_steel.stage4c_thesis_break_signals)
        self.assertIn("localization capex headline treated as tariff hedge Green", capex.false_positive_patterns)
        self.assertIn("control premium treated as operating rerating", zinc_control.false_positive_patterns)
        self.assertIn("funding, offtake, IRR, governance, and dilution gates visible", zinc_refinery.stage2_candidate_signals)
        self.assertIn("copper price rally treated as smelter margin", copper.false_positive_patterns)
        self.assertIn("customer certification failure", export_control.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round299_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND299_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round299_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_commodity_control_premium_or_capex_headline_as_green", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_false", record.green_guardrails)

        summary = round299_summary()
        self.assertEqual(summary["round_id"], "round_227")
        self.assertEqual(summary["large_sector"], ROUND299_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1")
        self.assertEqual(summary["case_candidate_count"], 10)
        self.assertEqual(summary["trigger_count"], 11)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 4)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 3)
        self.assertEqual(summary["stage3_green_candidate_count"], 0)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 4)
        self.assertEqual(summary["stage4c_watch_count"], 5)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_spread_policy_and_control_premium(self) -> None:
        by_id = {case.case_id: case for case in ROUND299_CASE_CANDIDATES}
        graphite = by_id["r4_loop15_posco_future_m_graphite_tariff"]
        lithium = by_id["r4_loop15_catl_yichun_lithium_event"]
        supply = by_id["r4_loop15_posco_minres_lithium_jv"]
        steel = by_id["r4_loop15_hyundai_posco_steel_antidumping"]
        weak = by_id["r4_loop15_hyundai_steel_weak_demand"]
        capex = by_id["r4_loop15_hyundai_steel_us_localization_capex"]
        tender = by_id["r4_loop15_korea_zinc_control_premium"]
        refinery = by_id["r4_loop15_korea_zinc_us_critical_minerals_smelter"]
        copper = by_id["r4_loop15_copper_tcrc_smelt_margin_watch"]
        controls = by_id["r4_loop15_china_strategic_mineral_export_controls"]

        self.assertEqual(graphite.primary_archetype, E2RArchetype.GRAPHITE_TARIFF_STAGE2_ACTIONABLE)
        self.assertEqual(graphite.extra_price_metrics["us_graphite_antidumping_tariff_pct"], 93.5)
        self.assertEqual(graphite.stage_candidate, "Stage2-Actionable_to_Stage3-Yellow_candidate")

        self.assertEqual(lithium.primary_archetype, E2RArchetype.LITHIUM_PRICE_EVENT_PREMIUM)
        self.assertEqual(lithium.score_price_alignment, "price_moved_without_evidence")
        self.assertEqual(lithium.extra_price_metrics["cme_lithium_carbonate_august_rally_pct"], 27)

        self.assertEqual(supply.primary_archetype, E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_SECURITY_STAGE2)
        self.assertEqual(supply.extra_price_metrics["minres_deal_value_usd_mn"], 765)
        self.assertEqual(supply.extra_price_metrics["posco_effective_interest_wodgina_pct"], 15)

        self.assertEqual(steel.primary_archetype, E2RArchetype.STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE)
        self.assertEqual(steel.extra_price_metrics["hyundai_market_relative_pp"], 6.5)
        self.assertIn("ASP_recovery_missing", steel.red_flag_fields)

        self.assertEqual(weak.primary_archetype, E2RArchetype.STEEL_WEAK_DEMAND_FAILED_RERATING)
        self.assertEqual(weak.extra_price_metrics["net_profit_estimate_cut_pct"], -73)
        self.assertEqual(weak.rerating_result, "thesis_break")

        self.assertEqual(capex.primary_archetype, E2RArchetype.LOCALIZATION_CAPEX_FALSE_POSITIVE)
        self.assertEqual(capex.extra_price_metrics["stock_decline_since_announcement_pct"], -21.2)
        self.assertEqual(capex.score_price_alignment, "false_positive_score")

        self.assertEqual(tender.primary_archetype, E2RArchetype.KOREA_ZINC_CONTROL_PREMIUM_4B)
        self.assertEqual(tender.extra_price_metrics["offer_price_krw"], 660000)
        self.assertEqual(tender.rerating_result, "event_premium")

        self.assertEqual(refinery.primary_archetype, E2RArchetype.CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B)
        self.assertEqual(refinery.extra_price_metrics["us_refinery_investment_usd_bn"], 7.4)
        self.assertFalse(refinery.extra_price_metrics["funding_plan_finalized"])

        self.assertEqual(copper.primary_archetype, E2RArchetype.COPPER_TCRC_SPREAD_4C_WATCH)
        self.assertEqual(copper.extra_price_metrics["tcrc_market_condition"], "unsustainable")
        self.assertEqual(copper.rerating_result, "thesis_break")

        self.assertEqual(controls.primary_archetype, E2RArchetype.CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C)
        self.assertIn("graphite", controls.extra_price_metrics["controlled_materials"])
        self.assertFalse(controls.extra_price_metrics["hard_4c_confirmed_for_specific_krx_name"])

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round299_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round299_shadow_weight_rows()}
        rules_md = render_round299_stage_rules_markdown()
        trigger_md = render_round299_trigger_grid_markdown()
        stage_md = render_round299_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND299_TRIGGER_RECORDS), 11)
        self.assertEqual(trigger_rows["r4l15_poscofm_graphite_T1"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r4l15_steel_antidumping_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r4l15_koreazinc_refinery_T3"]["promote_to"], "4B-watch")
        self.assertEqual(len(ROUND299_SHADOW_WEIGHT_ROWS), 10)
        self.assertEqual(shadow_rows["GRAPHITE_TARIFF_STAGE2_ACTIONABLE"]["tariff_rate_and_import_share"], "+5")
        self.assertEqual(shadow_rows["STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE"]["spread_margin_visibility"], "+5")
        self.assertEqual(shadow_rows["KOREA_ZINC_CONTROL_PREMIUM_4B"]["control_premium_separation"], "+5")
        self.assertIn("tariff_rate_antidumping_duty_or_import_share_is_numeric", ROUND299_STAGE2_ACTIONABLE_RULES)
        self.assertIn("capacity_customer_qualification_offtake_funding_or_irr_gate_still_pending", ROUND299_STAGE3_YELLOW_RULES)
        self.assertIn("operating_fcf_improves_not_just_control_premium", ROUND299_STAGE3_GREEN_RULES)
        self.assertIn("control_premium_as_operating_green", ROUND299_GREEN_BLOCKERS)
        self.assertIn("tcrc_smelt_margin", ROUND299_SCORE_UP_AXES)
        self.assertIn("metal_price_without_spread", ROUND299_SCORE_DOWN_AXES)
        self.assertIn("control_premium_rally_20_to_30pct", ROUND299_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("tcrc_collapse_breaks_smelter_margin", ROUND299_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("Korea Zinc", trigger_md)
        self.assertIn("strong 4B/4C-watch", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round299_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_299.md")
        self.assertEqual(audit["round_id"], "round_227")
        self.assertEqual(audit["large_sector"], ROUND299_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_commodity_price_or_control_premium_as_green", audit["what_not_to_change"])

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
            paths = write_round299_r4_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round299_case_rows()
            self.assertEqual(len(records), len(ROUND299_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND299_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND299_TRIGGER_RECORDS))
            self.assertIn("Korea Zinc", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2-Actionable", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r4l15_steel_antidumping_T1", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("GRAPHITE_TARIFF_STAGE2_ACTIONABLE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("COPPER_TCRC_SPREAD_4C_WATCH", paths["weight_profile"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["us_graphite_antidumping_tariff_pct"], 93.5)


if __name__ == "__main__":
    unittest.main()
