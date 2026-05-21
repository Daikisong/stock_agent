from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round311_r3_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round311_r3_loop16_secondary_battery_ev_green_trigger_validation import (
    ROUND311_4C_WATCH_GATES,
    ROUND311_CASE_CANDIDATES,
    ROUND311_GREEN_BLOCKERS,
    ROUND311_LARGE_SECTOR,
    ROUND311_REQUIRED_TARGET_ALIASES,
    ROUND311_ROW_SEPARATION_RULES,
    ROUND311_SCORE_DOWN_AXES,
    ROUND311_SCORE_UP_AXES,
    ROUND311_SHADOW_WEIGHT_ROWS,
    ROUND311_STAGE2_ACTIONABLE_RULES,
    ROUND311_STAGE3_GREEN_RULES,
    ROUND311_STAGE3_YELLOW_RULES,
    ROUND311_STAGE4B_WATCH_TRIGGERS,
    ROUND311_TRIGGER_RECORDS,
    render_round311_stage4b_4c_review_markdown,
    render_round311_stage_rules_markdown,
    render_round311_trigger_grid_markdown,
    round311_audit_payload,
    round311_case_records,
    round311_case_rows,
    round311_shadow_weight_rows,
    round311_summary,
    round311_trigger_rows,
    write_round311_r3_loop16_reports,
)


class Round311R3Loop16SecondaryBatteryTests(unittest.TestCase):
    def test_round311_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND311_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND311_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND311_REQUIRED_TARGET_ALIASES["ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE"],
            E2RArchetype.ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND311_REQUIRED_TARGET_ALIASES["BATTERY_FACTORY_SAFETY_HARD_4C"],
            E2RArchetype.BATTERY_FACTORY_SAFETY_HARD_4C.value,
        )

    def test_archetype_definitions_capture_r3_loop16_rules(self) -> None:
        ess = archetype_definition(E2RArchetype.ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE)
        oem = archetype_definition(E2RArchetype.EV_BATTERY_OEM_SUPPLY_STAGE2_WITH_UTILIZATION_GATE)
        slowdown = archetype_definition(E2RArchetype.EV_DEMAND_SLOWDOWN_4C_WATCH)
        relief = archetype_definition(E2RArchetype.BATTERY_JV_RESTRUCTURING_RELIEF_STAGE2_WITH_FINANCIAL_4B)
        lithium = archetype_definition(E2RArchetype.LITHIUM_SUPPLY_SHOCK_CYCLICAL_STAGE2)
        beta = archetype_definition(E2RArchetype.BATTERY_MATERIAL_LITHIUM_BETA_EVENT_PREMIUM)
        safety = archetype_definition(E2RArchetype.BATTERY_FACTORY_SAFETY_HARD_4C)
        dilution = archetype_definition(E2RArchetype.CAPITAL_RAISE_DILUTION_4B)

        self.assertIn("EV-to-ESS line conversion", " ".join(ess.stage2_candidate_signals))
        self.assertIn("utilization", " ".join(oem.stage3_high_conviction_signals))
        self.assertIn("contract cancellation", " ".join(slowdown.stage4c_thesis_break_signals))
        self.assertIn("financial relief", " ".join(relief.stage4b_graduation_overheat_signals))
        self.assertIn("cathode ASP", " ".join(lithium.stage3_high_conviction_signals))
        self.assertIn("event premium", " ".join(beta.false_positive_patterns))
        self.assertIn("fatal factory fire", " ".join(safety.stage4c_thesis_break_signals))
        self.assertIn("offering price cut", " ".join(dilution.stage4c_thesis_break_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round311_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND311_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round311_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_battery_contract_capex_restructuring_or_lithium_beta_as_green_without_utilization_margin_safety_evidence", record.green_guardrails)

        summary = round311_summary()
        self.assertEqual(summary["round_id"], "round_239")
        self.assertEqual(summary["large_sector"], ROUND311_LARGE_SECTOR)
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 1)
        self.assertEqual(summary["stage2_event_candidate_count"], 3)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 0)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])

    def test_case_metrics_cover_ess_lges_sk_lithium_dilution_and_safety(self) -> None:
        by_id = {case.case_id: case for case in ROUND311_CASE_CANDIDATES}
        sdi = by_id["r3_loop16_samsung_sdi_lfp_ess"]
        lges_contract = by_id["r3_loop16_lges_rivian_tesla_lfp"]
        lges_cancel = by_id["r3_loop16_lges_ford_cancellation_ohio_loss"]
        sk_relief = by_id["r3_loop16_sk_innovation_skes_merger_skon_relief"]
        sk_layoff = by_id["r3_loop16_sk_battery_america_layoffs"]
        lithium = by_id["r3_loop16_catl_yichun_lithium_beta_korea_materials"]
        dilution = by_id["r3_loop16_samsung_sdi_share_sale_dilution"]
        safety = by_id["r3_loop16_aricell_battery_factory_fire"]

        self.assertEqual(sdi.extra_price_metrics["contract_value_krw_trn"], 2.0)
        self.assertEqual(sdi.extra_price_metrics["contract_value_usd_bn"], 1.36)
        self.assertEqual(sdi.extra_price_metrics["delivery_start_year"], 2027)
        self.assertEqual(sdi.extra_price_metrics["market_relative_return_pp"], 6.2)

        self.assertEqual(lges_contract.extra_price_metrics["rivian_contract_gwh"], 67)
        self.assertEqual(lges_contract.extra_price_metrics["rivian_contract_duration_years"], 5)
        self.assertEqual(lges_contract.extra_price_metrics["tesla_lfp_contract_value_usd_bn"], 4.3)
        self.assertEqual(lges_contract.extra_price_metrics["tesla_contract_event_return_pct"], 0.6)
        self.assertEqual(lges_contract.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(lges_cancel.extra_price_metrics["cancelled_contract_value_krw_trn"], 9.6)
        self.assertEqual(lges_cancel.extra_price_metrics["cancelled_contract_value_usd_bn"], 6.5)
        self.assertEqual(lges_cancel.extra_price_metrics["event_mae_pct"], -7.6)
        self.assertEqual(lges_cancel.extra_price_metrics["q1_2026_loss_without_ira_credit_krw_bn"], 398)
        self.assertEqual(lges_cancel.extra_price_metrics["ultium_ohio_laid_off_or_idled_workers"], 850)

        self.assertEqual(sk_relief.extra_price_metrics["merged_asset_company_krw_trn"], 100)
        self.assertEqual(sk_relief.extra_price_metrics["market_relative_return_pp"], 5.5)
        self.assertEqual(sk_relief.extra_price_metrics["sk_on_cumulative_op_losses_krw_trn"], 2.3)
        self.assertEqual(sk_relief.extra_price_metrics["sk_on_debt_to_equity_pct"], 188)

        self.assertEqual(sk_layoff.extra_price_metrics["laid_off_workers"], 958)
        self.assertEqual(sk_layoff.extra_price_metrics["workforce_cut_pct"], 37)
        self.assertEqual(sk_layoff.extra_price_metrics["plant_cost_usd_bn"], 2.6)

        self.assertEqual(lithium.extra_price_metrics["posco_future_m_event_return_pct"], 8.3)
        self.assertEqual(lithium.extra_price_metrics["l_and_f_event_return_pct"], 10)
        self.assertEqual(lithium.extra_price_metrics["lithium_price_decline_from_2022_peak_pct"], 90)
        self.assertTrue(lithium.extra_price_metrics["license_renewal_risk"])

        self.assertEqual(dilution.extra_price_metrics["share_issuance_value_krw_trn"], 2.0)
        self.assertEqual(dilution.extra_price_metrics["new_shares_count"], 11821000)
        self.assertEqual(dilution.extra_price_metrics["pricing_cut_pct"], 14)
        self.assertEqual(dilution.extra_price_metrics["ytd_decline_pct"], -29.5)

        self.assertEqual(safety.extra_price_metrics["fatalities"], 23)
        self.assertEqual(safety.extra_price_metrics["injuries"], 9)
        self.assertTrue(safety.hard_4c_confirmed)

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round311_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round311_shadow_weight_rows()}
        rules_md = render_round311_stage_rules_markdown()
        trigger_md = render_round311_trigger_grid_markdown()
        stage_md = render_round311_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND311_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r3l16_samsungsdi_lfp_ess_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r3l16_lges_ford_cancel_T1"]["promote_to"], "4C-watch")
        self.assertEqual(trigger_rows["r3l16_aricell_fire_T0"]["promote_to"], "4C")
        self.assertEqual(len(ROUND311_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE"]["ess_lfp_contract_visibility"], "+5")
        self.assertEqual(shadow_rows["EV_BATTERY_OEM_SUPPLY_STAGE2_WITH_UTILIZATION_GATE"]["large_GWh_contract_without_margin_penalty"], "-4")
        self.assertEqual(shadow_rows["BATTERY_FACTORY_SAFETY_HARD_4C"]["battery_factory_safety_trust"], "+5")
        self.assertIn("contract_value_or_GWh_scale_is_clear", ROUND311_STAGE2_ACTIONABLE_RULES)
        self.assertIn("one_of_utilization_line_conversion_margin_subsidy_or_safety_remains_open", ROUND311_STAGE3_YELLOW_RULES)
        self.assertIn("GWh_contract_converts_to_utilization_and_margin", ROUND311_STAGE3_GREEN_RULES)
        self.assertIn("lithium_price_spike_without_margin", ROUND311_GREEN_BLOCKERS)
        self.assertIn("ESS_LFP_contract_visibility", ROUND311_SCORE_UP_AXES)
        self.assertIn("capex_funding_with_dilution", ROUND311_SCORE_DOWN_AXES)
        self.assertIn("restructuring_merger_rerates_before_profit_turnaround", ROUND311_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("factory_fire_deaths_or_quality_failure", ROUND311_4C_WATCH_GATES)
        self.assertIn("do_not_treat_GWh_capex_restructuring_or_lithium_beta_headline_as_utilization_margin_or_FCF", ROUND311_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r3_loop16_samsung_sdi_lfp_ess", trigger_md)
        self.assertIn("r3_loop16_aricell_battery_factory_fire", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round311_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_311.md")
        self.assertEqual(audit["round_id"], "round_239")
        self.assertEqual(audit["large_sector"], ROUND311_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_battery_contract_capex_restructuring_or_lithium_beta_as_green_without_utilization_margin_safety_evidence", audit["what_not_to_change"])

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
            paths = write_round311_r3_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round311_case_rows()
            self.assertEqual(len(records), len(ROUND311_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND311_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND311_TRIGGER_RECORDS))
            self.assertIn("case_library_row_describes_stage_candidate", paths["row_separation_plan"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
