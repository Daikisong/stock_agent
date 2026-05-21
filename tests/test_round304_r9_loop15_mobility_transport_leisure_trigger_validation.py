from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round304_r9_loop15_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round304_r9_loop15_mobility_transport_leisure_trigger_validation import (
    ROUND304_CASE_CANDIDATES,
    ROUND304_GREEN_BLOCKERS,
    ROUND304_HARD_4C_GATES,
    ROUND304_LARGE_SECTOR,
    ROUND304_REQUIRED_TARGET_ALIASES,
    ROUND304_SCORE_DOWN_AXES,
    ROUND304_SCORE_UP_AXES,
    ROUND304_SHADOW_WEIGHT_ROWS,
    ROUND304_STAGE2_ACTIONABLE_RULES,
    ROUND304_STAGE3_GREEN_RULES,
    ROUND304_STAGE3_YELLOW_RULES,
    ROUND304_STAGE4B_WATCH_TRIGGERS,
    ROUND304_TRIGGER_RECORDS,
    render_round304_stage_rules_markdown,
    render_round304_stage4b_4c_review_markdown,
    render_round304_trigger_grid_markdown,
    round304_audit_payload,
    round304_case_records,
    round304_case_rows,
    round304_shadow_weight_rows,
    round304_summary,
    round304_trigger_rows,
    write_round304_r9_loop15_reports,
)


class Round304R9Loop15MobilityTransportLeisureTriggerValidationTests(unittest.TestCase):
    def test_round304_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND304_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND304_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND304_REQUIRED_TARGET_ALIASES["HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW"],
            E2RArchetype.HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW.value,
        )
        self.assertEqual(
            ROUND304_REQUIRED_TARGET_ALIASES["AIRLINE_SAFETY_HARD_4C"],
            E2RArchetype.AIRLINE_SAFETY_HARD_4C.value,
        )
        self.assertEqual(
            ROUND304_REQUIRED_TARGET_ALIASES["CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B"],
            E2RArchetype.CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B.value,
        )

    def test_archetype_definitions_capture_r9_loop15_rules(self) -> None:
        hybrid = archetype_definition(E2RArchetype.HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW)
        robotics = archetype_definition(E2RArchetype.ROBOTICS_OPTIONALITY_STAGE2_WITH_4B)
        localization = archetype_definition(E2RArchetype.AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C)
        airline = archetype_definition(E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2)
        safety = archetype_definition(E2RArchetype.AIRLINE_SAFETY_HARD_4C)
        tourism = archetype_definition(E2RArchetype.TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE)
        freight = archetype_definition(E2RArchetype.CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B)

        self.assertIn("actual hybrid sales mix", " ".join(hybrid.stage3_high_conviction_signals))
        self.assertIn("robot unit economics", " ".join(robotics.stage3_high_conviction_signals))
        self.assertIn("immigration raid", " ".join(localization.stage4c_thesis_break_signals))
        self.assertIn("route yield and load factor", " ".join(airline.stage3_high_conviction_signals))
        self.assertIn("fatal safety accident", " ".join(safety.stage4c_thesis_break_signals))
        self.assertIn("foreign-card spending", " ".join(tourism.stage3_high_conviction_signals))
        self.assertIn("contract mix", " ".join(freight.false_positive_patterns))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round304_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND304_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round304_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_mobility_transport_leisure_headline_as_green", record.green_guardrails)

        by_id = {record.case_id: record for record in records}
        self.assertIn("hard_4c_confirmed_false", by_id["r9_loop15_hyundai_hybrid_shareholder_return"].green_guardrails)
        self.assertNotIn("hard_4c_confirmed_false", by_id["r9_loop15_jeju_air_crash_safety_4c"].green_guardrails)

        summary = round304_summary()
        self.assertEqual(summary["round_id"], "round_232")
        self.assertEqual(summary["large_sector"], ROUND304_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 10)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 5)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 1)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_separate_stage2_4b_and_hard_4c(self) -> None:
        by_id = {case.case_id: case for case in ROUND304_CASE_CANDIDATES}
        hyundai = by_id["r9_loop15_hyundai_hybrid_shareholder_return"]
        kia = by_id["r9_loop15_kia_ev_cut_hybrid_tariff"]
        robotics = by_id["r9_loop15_hyundai_boston_dynamics_robotics"]
        georgia = by_id["r9_loop15_hyundai_georgia_localization_operational_4c"]
        korean_air = by_id["r9_loop15_korean_air_asiana_consolidation"]
        jeju = by_id["r9_loop15_jeju_air_crash_safety_4c"]
        tourism = by_id["r9_loop15_china_tourism_travel_leisure"]
        hmm = by_id["r9_loop15_hmm_red_sea_freight_cycle"]

        self.assertEqual(hyundai.primary_archetype, E2RArchetype.HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW)
        self.assertEqual(hyundai.event_mfe_pct, 4.7)
        self.assertIn("actual_hybrid_sales_mix_missing", hyundai.red_flag_fields)

        self.assertEqual(kia.primary_archetype, E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH)
        self.assertEqual(kia.extra_price_metrics["tariff_hit_krw_bn"], 786)
        self.assertEqual(kia.stage_failure_type, "should_have_been_red")

        self.assertEqual(robotics.primary_archetype, E2RArchetype.ROBOTICS_OPTIONALITY_STAGE2_WITH_4B)
        self.assertEqual(robotics.extra_price_metrics["boston_dynamics_indirect_stake_pct"], 27.9)
        self.assertIn("external_customer_orders_missing", robotics.red_flag_fields)

        self.assertEqual(georgia.primary_archetype, E2RArchetype.AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C)
        self.assertEqual(georgia.extra_price_metrics["detained_workers_count"], 475)

        self.assertEqual(korean_air.primary_archetype, E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2)
        self.assertEqual(korean_air.extra_price_metrics["stake_pct"], 63.88)

        self.assertEqual(jeju.primary_archetype, E2RArchetype.AIRLINE_SAFETY_HARD_4C)
        self.assertTrue(jeju.hard_4c_confirmed)
        self.assertEqual(jeju.event_mae_pct, -15.7)

        self.assertEqual(tourism.primary_archetype, E2RArchetype.TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE)
        self.assertEqual(tourism.extra_price_metrics["hankook_cosmetics_return_pct"], 9.9)

        self.assertEqual(hmm.primary_archetype, E2RArchetype.CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B)
        self.assertEqual(hmm.rerating_result, "cyclical_rerating")
        self.assertIn("Suez_normalization_risk", hmm.red_flag_fields)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round304_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round304_shadow_weight_rows()}
        rules_md = render_round304_stage_rules_markdown()
        trigger_md = render_round304_trigger_grid_markdown()
        stage_md = render_round304_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND304_TRIGGER_RECORDS), 10)
        self.assertEqual(trigger_rows["r9l15_hyundai_hybrid_T1"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r9l15_jejuair_crash_T0"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r9l15_hmm_suez_T3"]["promote_to"], "4B-watch")
        self.assertEqual(len(ROUND304_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW"]["hybrid_mix_margin_visibility"], "+5")
        self.assertEqual(shadow_rows["AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C"]["localization_capex_headline_only_penalty"], "-5")
        self.assertEqual(shadow_rows["TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE"]["tourism_spending_conversion"], "+5")
        self.assertIn("hybrid_target_buyback_margin_target_or_tariff_pivot_is_quantified", ROUND304_STAGE2_ACTIONABLE_RULES)
        self.assertIn("freight_rates_convert_to_earnings_but_contract_mix_or_normalization_risk_remains", ROUND304_STAGE3_YELLOW_RULES)
        self.assertIn("airline_integration_synergy_load_factor_yield_and_safety_trust_visible", ROUND304_STAGE3_GREEN_RULES)
        self.assertIn("fatal_airline_safety_event", ROUND304_GREEN_BLOCKERS)
        self.assertIn("hybrid_mix_margin_visibility", ROUND304_SCORE_UP_AXES)
        self.assertIn("freight_rate_spike_without_contract_mix", ROUND304_SCORE_DOWN_AXES)
        self.assertIn("freight_rate_spike_annualized_before_contract_duration", ROUND304_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_airline_safety_accident", ROUND304_HARD_4C_GATES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r9_loop15_hyundai_boston_dynamics_robotics", trigger_md)
        self.assertIn("Jeju Air fatal safety accident", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round304_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_304.md")
        self.assertEqual(audit["round_id"], "round_232")
        self.assertEqual(audit["large_sector"], ROUND304_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_mobility_transport_leisure_headline_as_green", audit["what_not_to_change"])

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
            paths = write_round304_r9_loop15_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round304_case_rows()
            self.assertEqual(len(records), len(ROUND304_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND304_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND304_TRIGGER_RECORDS))
            self.assertIn("Hyundai hybrid/shareholder-return", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("Stage3-Green", paths["stage_rules"].read_text(encoding="utf-8"))
            self.assertIn("r9l15_hmm_suez_T3", paths["trigger_grid_md"].read_text(encoding="utf-8"))
            self.assertIn("ROBOTICS_OPTIONALITY_STAGE2_WITH_4B", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B", paths["weight_profile"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["hybrid_models_count"], 14)


if __name__ == "__main__":
    unittest.main()
