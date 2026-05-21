from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round317_r9_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round317_r9_loop16_mobility_transport_leisure_trigger_validation import (
    ROUND317_4C_WATCH_GATES,
    ROUND317_CASE_CANDIDATES,
    ROUND317_GREEN_BLOCKERS,
    ROUND317_LARGE_SECTOR,
    ROUND317_REQUIRED_TARGET_ALIASES,
    ROUND317_ROW_SEPARATION_RULES,
    ROUND317_SCORE_DOWN_AXES,
    ROUND317_SCORE_UP_AXES,
    ROUND317_SHADOW_WEIGHT_ROWS,
    ROUND317_STAGE2_ACTIONABLE_RULES,
    ROUND317_STAGE3_GREEN_RULES,
    ROUND317_STAGE3_YELLOW_RULES,
    ROUND317_STAGE4B_WATCH_TRIGGERS,
    ROUND317_TRIGGER_RECORDS,
    render_round317_stage4b_4c_review_markdown,
    render_round317_stage_rules_markdown,
    render_round317_trigger_grid_markdown,
    round317_audit_payload,
    round317_case_records,
    round317_case_rows,
    round317_shadow_weight_rows,
    round317_summary,
    round317_trigger_rows,
    write_round317_r9_loop16_reports,
)


class Round317R9Loop16MobilityTransportLeisureTests(unittest.TestCase):
    def test_round317_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND317_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND317_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND317_REQUIRED_TARGET_ALIASES["AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE"],
            E2RArchetype.AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND317_REQUIRED_TARGET_ALIASES["AVIATION_SAFETY_HARD_4C"],
            E2RArchetype.AVIATION_SAFETY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND317_REQUIRED_TARGET_ALIASES["CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B"],
            E2RArchetype.CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B.value,
        )

    def test_archetype_definitions_capture_round317_mobility_rules(self) -> None:
        hybrid = archetype_definition(E2RArchetype.AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE)
        tariff = archetype_definition(E2RArchetype.AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE)
        robotics = archetype_definition(E2RArchetype.AUTO_ROBOTICS_OPTIONALITY_STAGE2_WITH_LABOR_4B)
        logistics = archetype_definition(E2RArchetype.AUTO_EXPORT_LOGISTICS_DISRUPTION_4C_WATCH)
        airline = archetype_definition(E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2_WITH_INTEGRATION_4B)
        safety = archetype_definition(E2RArchetype.AVIATION_SAFETY_HARD_4C)
        tourism = archetype_definition(E2RArchetype.CHINA_TOURISM_LEISURE_STAGE2_EVENT)
        freight = archetype_definition(E2RArchetype.CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B)

        self.assertIn("hybrid mix converts to OP margin", " ".join(hybrid.stage3_high_conviction_signals))
        self.assertIn("tariff cost directly hits profit", " ".join(tariff.stage4c_thesis_break_signals))
        self.assertIn("labor agreement", " ".join(robotics.stage3_high_conviction_signals))
        self.assertIn("delivery delay", " ".join(logistics.stage4c_thesis_break_signals))
        self.assertIn("integration synergy", " ".join(airline.stage3_high_conviction_signals))
        self.assertIn("fatal aviation accident", " ".join(safety.stage4c_thesis_break_signals))
        self.assertIn("casino drop", " ".join(tourism.stage3_high_conviction_signals))
        self.assertIn("contract freight rates", " ".join(freight.stage3_high_conviction_signals))

    def test_case_records_validate_and_remain_calibration_only(self) -> None:
        records = round317_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND317_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round317_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn(
                "do_not_treat_hybrid_tariff_localization_robotics_airline_tourism_or_freight_headline_as_Green_without_margin_utilization_synergy_yield_or_contract_duration",
                record.green_guardrails,
            )

        summary = round317_summary()
        self.assertEqual(summary["round_id"], "round_245")
        self.assertEqual(summary["large_sector"], ROUND317_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 4)
        self.assertEqual(summary["stage2_candidate_count"], 6)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 6)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])

    def test_case_metrics_separate_hybrid_tariff_robotics_airline_tourism_and_freight(self) -> None:
        by_id = {case.case_id: case for case in ROUND317_CASE_CANDIDATES}
        hybrid = by_id["r9_loop16_hyundai_hybrid_valueup"]
        tariff = by_id["r9_loop16_hyundai_kia_tariff_localization"]
        robotics = by_id["r9_loop16_hyundai_boston_dynamics_robotics"]
        glovis = by_id["r9_loop16_hyundai_glovis_export_disruption"]
        airline = by_id["r9_loop16_korean_air_asiana_consolidation"]
        jeju = by_id["r9_loop16_jeju_air_crash_safety_4c"]
        tourism = by_id["r9_loop16_china_tourism_leisure_transport"]
        hmm = by_id["r9_loop16_hmm_red_sea_freight_beta"]

        self.assertEqual(hybrid.extra_price_metrics["hybrid_sales_target_2028_mn_units"], 1.33)
        self.assertEqual(hybrid.extra_price_metrics["buyback_2025_2027_krw_trn"], 4)
        self.assertIn("hybrid_mix_margin_missing", hybrid.red_flag_fields)

        self.assertEqual(tariff.extra_price_metrics["trade_deal_auto_tariff_pct"], 15)
        self.assertEqual(tariff.extra_price_metrics["hyundai_trade_deal_event_return_pct"], -4.5)
        self.assertIn("tariff_cost_directly_hitting_profit", tariff.red_flag_fields)

        self.assertEqual(robotics.extra_price_metrics["atlas_annual_production_target_units"], 30000)
        self.assertIn("labor_agreement_missing", robotics.red_flag_fields)

        self.assertEqual(glovis.extra_price_metrics["hyundai_market_relative_pp"], -3.9)
        self.assertEqual(glovis.rerating_result, "thesis_break")

        self.assertEqual(airline.extra_price_metrics["korean_air_asiana_stake_pct"], 63.88)
        self.assertEqual(airline.score_price_alignment, "unknown")

        self.assertTrue(jeju.hard_4c_confirmed)
        self.assertEqual(jeju.extra_price_metrics["fatalities"], 179)
        self.assertEqual(jeju.event_mae_pct, -15.7)

        self.assertEqual(tourism.extra_price_metrics["china_korea_flight_capacity_vs_pre_pandemic_pct"], 105)
        self.assertIn("airline_yield_missing", tourism.red_flag_fields)

        self.assertEqual(hmm.extra_price_metrics["freightos_index_six_week_return_pct"], 40)
        self.assertEqual(hmm.rerating_result, "cyclical_rerating")

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round317_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round317_shadow_weight_rows()}
        rules_md = render_round317_stage_rules_markdown()
        trigger_md = render_round317_trigger_grid_markdown()
        stage_md = render_round317_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND317_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r9l16_hyundai_hybrid_valueup_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r9l16_jeju_air_crash_T0"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r9l16_hmm_redsea_T0"]["promote_to"], "Stage2_cyclical+4B")
        self.assertEqual(len(ROUND317_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE"]["hybrid_mix_margin_conversion"], "+5")
        self.assertEqual(shadow_rows["CHINA_TOURISM_LEISURE_STAGE2_EVENT"]["tourism_spend_margin"], "+5")
        self.assertEqual(shadow_rows["CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B"]["freight_rate_duration"], "+5")
        self.assertIn("event_return_at_least_5pct_or_market_relative_return_at_least_5pp", ROUND317_STAGE2_ACTIONABLE_RULES)
        self.assertIn("one_of_tariff_utilization_safety_yield_labor_or_freight_duration_gate_remains_open", ROUND317_STAGE3_YELLOW_RULES)
        self.assertIn("tourism_policy_converts_to_spending_yield_and_margin", ROUND317_STAGE3_GREEN_RULES)
        self.assertIn("tariff_relief_without_actual_savings", ROUND317_GREEN_BLOCKERS)
        self.assertIn("freight_rate_duration", ROUND317_SCORE_UP_AXES)
        self.assertIn("safety_incident_treated_as_one_off", ROUND317_SCORE_DOWN_AXES)
        self.assertIn("robotics_optionality_rallies_before_unit_economics_and_labor_agreement", ROUND317_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_aviation_accident", ROUND317_4C_WATCH_GATES)
        self.assertIn("trigger_calibration_row_stores_event_anchor_tariff_hybrid_robotics_airline_tourism_or_freight_metrics", ROUND317_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r9_loop16_hyundai_hybrid_valueup", trigger_md)
        self.assertIn("r9_loop16_jeju_air_crash_safety_4c", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round317_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_317.md")
        self.assertEqual(audit["round_id"], "round_245")
        self.assertEqual(audit["large_sector"], ROUND317_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_change_production_scoring", audit["what_not_to_change"])

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
            paths = write_round317_r9_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            self.assertEqual(len(load_case_library(root / "cases.jsonl")), 8)

            summary_text = paths["summary"].read_text(encoding="utf-8")
            self.assertIn("Hyundai hybrid/value-up", summary_text)
            self.assertIn("Stage3-Green confirmed: `0`", summary_text)

        self.assertEqual(len(round317_case_rows()), 8)


if __name__ == "__main__":
    unittest.main()
