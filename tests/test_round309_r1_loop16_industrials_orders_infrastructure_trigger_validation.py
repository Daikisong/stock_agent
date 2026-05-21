from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round309_r1_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round309_r1_loop16_industrials_orders_infrastructure_trigger_validation import (
    ROUND309_4C_WATCH_GATES,
    ROUND309_CASE_CANDIDATES,
    ROUND309_GREEN_BLOCKERS,
    ROUND309_LARGE_SECTOR,
    ROUND309_REQUIRED_TARGET_ALIASES,
    ROUND309_ROW_SEPARATION_RULES,
    ROUND309_SCORE_DOWN_AXES,
    ROUND309_SCORE_UP_AXES,
    ROUND309_SHADOW_WEIGHT_ROWS,
    ROUND309_STAGE2_ACTIONABLE_RULES,
    ROUND309_STAGE3_GREEN_RULES,
    ROUND309_STAGE3_YELLOW_RULES,
    ROUND309_STAGE4B_WATCH_TRIGGERS,
    ROUND309_TRIGGER_RECORDS,
    render_round309_stage4b_4c_review_markdown,
    render_round309_stage_rules_markdown,
    render_round309_trigger_grid_markdown,
    round309_audit_payload,
    round309_case_records,
    round309_case_rows,
    round309_shadow_weight_rows,
    round309_summary,
    round309_trigger_rows,
    write_round309_r1_loop16_reports,
)


class Round309R1Loop16IndustrialsOrdersInfrastructureTests(unittest.TestCase):
    def test_round309_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND309_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND309_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND309_REQUIRED_TARGET_ALIASES["OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE"],
            E2RArchetype.OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND309_REQUIRED_TARGET_ALIASES["DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED"],
            E2RArchetype.DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED.value,
        )
        self.assertEqual(
            ROUND309_REQUIRED_TARGET_ALIASES["AEROSPACE_EXPORT_CONTRACT_STAGE2"],
            E2RArchetype.AEROSPACE_EXPORT_CONTRACT_STAGE2.value,
        )

    def test_archetype_definitions_capture_r1_loop16_rules(self) -> None:
        epc = archetype_definition(E2RArchetype.OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE)
        grid = archetype_definition(E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_STAGE2)
        merger = archetype_definition(E2RArchetype.SHIPBUILDING_MERGER_SCALE_STAGE2_WITH_INTEGRATION_4B)
        cancellation = archetype_definition(E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_4C)
        sanction = archetype_definition(E2RArchetype.GEOPOLITICAL_SANCTION_SHIPBUILDING_4C_WATCH)
        robotics = archetype_definition(E2RArchetype.ROBOTICS_STRATEGIC_CONTROL_STAGE2_WITH_ORDER_GATE)
        cooling = archetype_definition(E2RArchetype.DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED)
        aerospace = archetype_definition(E2RArchetype.AEROSPACE_EXPORT_CONTRACT_STAGE2)

        self.assertIn("cash collection", " ".join(epc.stage3_high_conviction_signals))
        self.assertIn("transformer", " ".join(grid.stage2_candidate_signals))
        self.assertIn("integration synergy", " ".join(merger.stage3_high_conviction_signals))
        self.assertIn("Singapore arbitration", " ".join(cancellation.stage4c_thesis_break_signals))
        self.assertIn("sanctioned subsidiary", " ".join(sanction.stage4c_thesis_break_signals))
        self.assertIn("external robot orders", " ".join(robotics.stage3_high_conviction_signals))
        self.assertIn("price muted", " ".join(cooling.stage4b_graduation_overheat_signals))
        self.assertIn("delivery revenue", " ".join(aerospace.stage3_high_conviction_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round309_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND309_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round309_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_order_merger_transformer_robotics_or_cooling_headline_as_green", record.green_guardrails)
            self.assertIn("stage_candidate_not_downgraded_for_missing_full_ohlc", record.green_guardrails)

        summary = round309_summary()
        self.assertEqual(summary["round_id"], "round_237")
        self.assertEqual(summary["large_sector"], ROUND309_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 8)
        self.assertEqual(summary["target_archetype_count"], 9)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 3)
        self.assertEqual(summary["stage2_event_candidate_count"], 3)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertTrue(summary["row_separation_required"])
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_cover_orders_mergers_transformers_sanctions_and_cooling(self) -> None:
        by_id = {case.case_id: case for case in ROUND309_CASE_CANDIDATES}
        samsung_ea = by_id["r1_loop16_samsung_ea_fadhili"]
        ls = by_id["r1_loop16_ls_electric_us_transformer"]
        merger = by_id["r1_loop16_hd_hyundai_heavy_mipo_merger"]
        basket = by_id["r1_loop16_shipbuilding_contract_win_basket"]
        zvezda = by_id["r1_loop16_samsung_heavy_zvezda_cancellation"]
        sanction = by_id["r1_loop16_hanwha_ocean_china_sanctions"]
        robotics = by_id["r1_loop16_rainbow_robotics_samsung_control"]
        cooling = by_id["r1_loop16_samsung_flaktgroup_datacenter_cooling"]

        self.assertEqual(samsung_ea.extra_price_metrics["contract_value_usd_bn"], 6.0)
        self.assertEqual(samsung_ea.extra_price_metrics["market_relative_return_pp"], 9.9)
        self.assertEqual(samsung_ea.stage2_price_anchor, 26750)

        self.assertEqual(ls.extra_price_metrics["t1_contract_value_usd_mn"], 312)
        self.assertEqual(ls.extra_price_metrics["us_gsu_transformer_demand_growth_since_2019_pct"], 274)
        self.assertEqual(ls.extra_price_metrics["large_transformer_lead_time_years"], 4)
        self.assertEqual(ls.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(merger.extra_price_metrics["hd_hyundai_heavy_event_return_pct"], 11.3)
        self.assertEqual(merger.extra_price_metrics["hd_hyundai_mipo_event_return_pct"], 14.6)
        self.assertEqual(merger.case_type, "4b_watch")

        self.assertEqual(basket.extra_price_metrics["samsung_heavy_event_return_pct"], 16)
        self.assertEqual(basket.extra_price_metrics["hanwha_ocean_event_return_pct"], 13)
        self.assertEqual(basket.extra_price_metrics["korea_global_shipbuilding_order_share_feb_pct"], 50)

        self.assertEqual(zvezda.extra_price_metrics["cancelled_order_value_krw_trn"], 4.85)
        self.assertEqual(zvezda.extra_price_metrics["cancelled_order_value_usd_bn"], 3.54)
        self.assertFalse(zvezda.hard_4c_confirmed)

        self.assertEqual(sanction.extra_price_metrics["sanctioned_units_count"], 5)
        self.assertEqual(sanction.event_mae_pct, -5.8)
        self.assertFalse(sanction.hard_4c_confirmed)

        self.assertEqual(robotics.extra_price_metrics["samsung_additional_stake_krw_bn"], 267)
        self.assertEqual(robotics.extra_price_metrics["samsung_prior_stake_pct"], 14.71)
        self.assertIn("strategic_stake_without_orders", robotics.red_flag_fields)

        self.assertEqual(cooling.extra_price_metrics["acquisition_value_eur_bn"], 1.5)
        self.assertEqual(cooling.extra_price_metrics["acquisition_value_usd_bn"], 1.68)
        self.assertEqual(cooling.event_mfe_pct, 0.7)
        self.assertEqual(cooling.score_price_alignment, "evidence_good_but_price_failed")

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round309_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round309_shadow_weight_rows()}
        rules_md = render_round309_stage_rules_markdown()
        trigger_md = render_round309_trigger_grid_markdown()
        stage_md = render_round309_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND309_TRIGGER_RECORDS), 8)
        self.assertEqual(trigger_rows["r1l16_samsungea_fadhili_T1"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r1l16_hhi_mipo_merger_T1"]["promote_to"], "Stage2-Actionable+4B")
        self.assertEqual(trigger_rows["r1l16_hanwhaocean_china_T1"]["promote_to"], "4C-watch")
        self.assertEqual(len(ROUND309_SHADOW_WEIGHT_ROWS), 9)
        self.assertEqual(shadow_rows["OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE"]["signed_contract_value_vs_backlog"], "+5")
        self.assertEqual(shadow_rows["GRID_TRANSFORMER_DATA_CENTER_STAGE2"]["transformer_demand_without_company_margin_penalty"], "-5")
        self.assertEqual(shadow_rows["DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED"]["MA_without_customer_orders_penalty"], "-4")
        self.assertIn("signed_contract_value_large_vs_annual_order_wins_or_backlog", ROUND309_STAGE2_ACTIONABLE_RULES)
        self.assertIn("one_of_margin_cash_delivery_integration_capacity_still_open", ROUND309_STAGE3_YELLOW_RULES)
        self.assertIn("backlog_to_revenue_to_OP_conversion_confirmed", ROUND309_STAGE3_GREEN_RULES)
        self.assertIn("strategic_stake_without_orders", ROUND309_GREEN_BLOCKERS)
        self.assertIn("market_relative_event_strength", ROUND309_SCORE_UP_AXES)
        self.assertIn("geopolitical_opportunity_without_sanction_check", ROUND309_SCORE_DOWN_AXES)
        self.assertIn("strategic_stake_or_MA_rerating_before_orders", ROUND309_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("arbitration_or_legal_dispute", ROUND309_4C_WATCH_GATES)
        self.assertIn("ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown", ROUND309_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r1_loop16_samsung_ea_fadhili", trigger_md)
        self.assertIn("r1_loop16_hanwha_ocean_china_sanctions", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round309_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_309.md")
        self.assertEqual(audit["round_id"], "round_237")
        self.assertEqual(audit["large_sector"], ROUND309_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_order_merger_transformer_robotics_or_cooling_headline_as_green", audit["what_not_to_change"])

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
            paths = write_round309_r1_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round309_case_rows()
            self.assertEqual(len(records), len(ROUND309_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND309_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND309_TRIGGER_RECORDS))
            self.assertIn("case_library_row_describes_what_happened", paths["row_separation_plan"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
