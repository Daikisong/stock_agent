from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round330_r9_loop17_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round330_r9_loop17_mobility_transport_leisure_trigger_validation import (
    ROUND330_CASE_CANDIDATES,
    ROUND330_GREEN_BLOCKERS,
    ROUND330_HARD_4C_GATES,
    ROUND330_LARGE_SECTOR,
    ROUND330_REQUIRED_TARGET_ALIASES,
    ROUND330_ROW_SEPARATION_RULES,
    ROUND330_SCORE_DOWN_AXES,
    ROUND330_SCORE_UP_AXES,
    ROUND330_SHADOW_WEIGHT_ROWS,
    ROUND330_STAGE2_ACTIONABLE_RULES,
    ROUND330_STAGE3_GREEN_RULES,
    ROUND330_STAGE3_YELLOW_RULES,
    ROUND330_STAGE4B_WATCH_TRIGGERS,
    ROUND330_TRIGGER_RECORDS,
    render_round330_stage4b_4c_review_markdown,
    render_round330_stage_rules_markdown,
    render_round330_trigger_grid_markdown,
    round330_audit_payload,
    round330_case_records,
    round330_case_rows,
    round330_shadow_weight_rows,
    round330_summary,
    round330_trigger_rows,
    write_round330_r9_loop17_reports,
)


class Round330R9Loop17MobilityTransportLeisureTests(unittest.TestCase):
    def test_round330_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND330_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND330_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND330_REQUIRED_TARGET_ALIASES["AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE"],
            E2RArchetype.AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND330_REQUIRED_TARGET_ALIASES["AUTO_TARIFF_LOCALIZATION_4B"],
            E2RArchetype.AUTO_TARIFF_LOCALIZATION_4B.value,
        )
        self.assertEqual(
            ROUND330_REQUIRED_TARGET_ALIASES["LCC_SAFETY_TRUST_HARD_4C"],
            E2RArchetype.LCC_SAFETY_TRUST_HARD_4C.value,
        )
        self.assertEqual(
            ROUND330_REQUIRED_TARGET_ALIASES["SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE"],
            E2RArchetype.SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE.value,
        )

    def test_archetype_definitions_capture_round330_rules(self) -> None:
        hybrid = archetype_definition(E2RArchetype.AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE)
        tariff = archetype_definition(E2RArchetype.AUTO_TARIFF_LOCALIZATION_4B)
        robotics = archetype_definition(E2RArchetype.MOBILITY_ROBOTICS_AI_FACTORY_STAGE2_OVERHEAT)
        airline = archetype_definition(E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2_NO_PRICE)
        lcc = archetype_definition(E2RArchetype.LCC_SAFETY_TRUST_HARD_4C)
        tourism = archetype_definition(E2RArchetype.CHINA_TOURISM_LEISURE_STAGE2_ACTIONABLE)
        marine = archetype_definition(E2RArchetype.MARINE_AFTERMARKET_IPO_STAGE2_ACTIONABLE)
        shipbuilding = archetype_definition(E2RArchetype.SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE)

        self.assertIn("hybrid mix converts to OP margin", " ".join(hybrid.stage3_high_conviction_signals))
        self.assertIn("15% tariff resets margin", " ".join(tariff.stage4b_graduation_overheat_signals))
        self.assertIn("robot deployment revenue/productivity", " ".join(robotics.stage3_high_conviction_signals))
        self.assertIn("yield/cost/load-factor synergy", " ".join(airline.stage3_high_conviction_signals))
        self.assertIn("direct stock-price anchor unavailable", " ".join(airline.stage4b_graduation_overheat_signals))
        self.assertIn("fatal aviation safety event", " ".join(lcc.stage4c_thesis_break_signals))
        self.assertIn("market cap wiped", " ".join(lcc.stage4c_thesis_break_signals))
        self.assertIn("casino/drop", " ".join(tourism.stage3_high_conviction_signals))
        self.assertIn("recurring retrofit demand and margin durability", " ".join(marine.stage3_high_conviction_signals))
        self.assertIn("KKR overhang", " ".join(marine.stage4b_graduation_overheat_signals))
        self.assertIn("U.S. naval/icebreaker contracts", " ".join(shipbuilding.stage3_high_conviction_signals))
        self.assertIn("exchange-ratio dispute", " ".join(shipbuilding.stage4b_graduation_overheat_signals))

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round330_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND330_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round330_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", record.green_guardrails)

        summary = round330_summary()
        self.assertEqual(summary["round_id"], "round_258")
        self.assertEqual(summary["loop_name"], "R9 Loop 17")
        self.assertEqual(summary["large_sector"], ROUND330_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 8)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 4)
        self.assertEqual(summary["stage2_candidate_count"], 6)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["price_unavailable_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])

    def test_case_metrics_separate_auto_airline_safety_tourism_and_shipbuilding(self) -> None:
        by_id = {case.case_id: case for case in ROUND330_CASE_CANDIDATES}
        hybrid = by_id["r9_loop17_hyundai_hybrid_valueup"]
        tariff = by_id["r9_loop17_hyundai_kia_us_auto_tariff"]
        robotics = by_id["r9_loop17_hyundai_kia_robotics_ai_factory"]
        airline = by_id["r9_loop17_korean_air_asiana_consolidation"]
        jeju = by_id["r9_loop17_jeju_air_crash_hard_4c"]
        tourism = by_id["r9_loop17_china_visa_free_leisure_basket"]
        marine = by_id["r9_loop17_hd_hyundai_marine_solution_ipo"]
        merger = by_id["r9_loop17_hd_hyundai_heavy_mipo_masga_merger"]

        self.assertEqual(hybrid.extra_price_metrics["event_return_close_pct"], 4.7)
        self.assertEqual(hybrid.extra_price_metrics["buyback_2025_2027_krw_trn"], 4.0)
        self.assertIn("US_tariff_localization_4B", hybrid.red_flag_fields)

        self.assertEqual(tariff.extra_price_metrics["us_auto_tariff_rate_pct"], 15)
        self.assertEqual(tariff.extra_price_metrics["kia_event_return_pct"], -6.6)

        self.assertEqual(robotics.extra_price_metrics["saemangeum_investment_krw_trn"], 10)
        self.assertEqual(robotics.extra_price_metrics["kia_saemangeum_event_return_pct"], 15)
        self.assertIn("capex_ROI_missing_4B", robotics.red_flag_fields)

        self.assertEqual(airline.extra_price_metrics["korean_air_asiana_stake_pct"], 63.88)
        self.assertEqual(airline.score_price_alignment, "unknown")

        self.assertTrue(jeju.hard_4c_confirmed)
        self.assertEqual(jeju.extra_price_metrics["fatalities"], 179)
        self.assertEqual(jeju.extra_price_metrics["intraday_event_return_pct"], -15.7)

        self.assertEqual(tourism.extra_price_metrics["hyundai_department_store_event_return_pct"], 7.1)
        self.assertIn("basket_size_missing", tourism.red_flag_fields)

        self.assertEqual(marine.extra_price_metrics["close_return_pct"], 97)
        self.assertIn("KKR_overhang_4B", marine.red_flag_fields)

        self.assertEqual(merger.extra_price_metrics["hd_hyundai_mipo_event_return_pct"], 14.6)
        self.assertIn("US_contract_conversion_missing", merger.red_flag_fields)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round330_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round330_shadow_weight_rows()}
        rules_md = render_round330_stage_rules_markdown()
        trigger_md = render_round330_trigger_grid_markdown()
        stage_md = render_round330_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND330_TRIGGER_RECORDS), 8)
        self.assertEqual(trigger_rows["r9l17_hyundai_hybrid_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r9l17_auto_tariff_T0"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r9l17_jeju_air_crash_T0"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r9l17_hd_hyundai_marine_ipo_T1"]["event_return_pct"], "97")
        self.assertEqual(len(ROUND330_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE"]["hybrid_mix_margin"], "+5")
        self.assertEqual(shadow_rows["MOBILITY_ROBOTICS_AI_FACTORY_STAGE2_OVERHEAT"]["robotics_AI_mobility_optionality"], "+5")
        self.assertEqual(shadow_rows["SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE"]["shipbuilding_US_naval_demand"], "+5")
        self.assertIn("event_return_at_least_5pct_or_clear_reported_positive_price_anchor", ROUND330_STAGE2_ACTIONABLE_RULES)
        self.assertIn("tourism_visitor_volume_converts_into_basket_size_and_OP", ROUND330_STAGE3_YELLOW_RULES)
        self.assertIn("robotics_AI_optionality_becomes_measurable_productivity_or_revenue", ROUND330_STAGE3_GREEN_RULES)
        self.assertIn("auto_growth_without_tariff_adjustment", ROUND330_GREEN_BLOCKERS)
        self.assertIn("shipbuilding_US_naval_demand", ROUND330_SCORE_UP_AXES)
        self.assertIn("safety_event_ignored_penalty", ROUND330_SCORE_DOWN_AXES)
        self.assertIn("US_auto_tariff_reset", ROUND330_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_safety_accident_with_stock_crash_and_system_wide_inspection", ROUND330_HARD_4C_GATES)
        self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", ROUND330_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r9_loop17_hd_hyundai_marine_solution_ipo", trigger_md)
        self.assertIn("r9_loop17_jeju_air_crash_hard_4c", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round330_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_330.md")
        self.assertEqual(audit["round_id"], "round_258")
        self.assertEqual(audit["large_sector"], ROUND330_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_change_production_scoring", audit["what_not_to_change"])
        self.assertIn("do_not_use_round330_cases_as_candidate_generation_input", audit["what_not_to_change"])

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
            paths = write_round330_r9_loop17_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round330_case_rows()
            self.assertEqual(len(records), len(ROUND330_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND330_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND330_TRIGGER_RECORDS))
            self.assertIn("Hyundai", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage2", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r9l17_jeju_air_crash_T0", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE", paths["weight_profile"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
