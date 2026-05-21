from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round324_r3_loop17_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round324_r3_loop17_secondary_battery_ev_green import (
    ROUND324_CASE_CANDIDATES,
    ROUND324_GREEN_BLOCKERS,
    ROUND324_HARD_4C_GATES,
    ROUND324_LARGE_SECTOR,
    ROUND324_REQUIRED_TARGET_ALIASES,
    ROUND324_ROW_SEPARATION_RULES,
    ROUND324_SCORE_DOWN_AXES,
    ROUND324_SCORE_UP_AXES,
    ROUND324_SHADOW_WEIGHT_ROWS,
    ROUND324_STAGE2_ACTIONABLE_RULES,
    ROUND324_STAGE3_GREEN_RULES,
    ROUND324_STAGE3_YELLOW_RULES,
    ROUND324_STAGE4B_WATCH_TRIGGERS,
    ROUND324_TRIGGER_RECORDS,
    render_round324_stage_rules_markdown,
    render_round324_stage4b_4c_review_markdown,
    render_round324_trigger_grid_markdown,
    round324_audit_payload,
    round324_case_records,
    round324_case_rows,
    round324_shadow_weight_rows,
    round324_summary,
    round324_trigger_rows,
    write_round324_r3_loop17_reports,
)


class Round324R3Loop17BatteryEVGreenTests(unittest.TestCase):
    def test_round324_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND324_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND324_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND324_REQUIRED_TARGET_ALIASES["ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE"],
            E2RArchetype.ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE.value,
        )
        self.assertEqual(
            ROUND324_REQUIRED_TARGET_ALIASES["EV_CONTRACT_CANCELLATION_4C"],
            E2RArchetype.EV_CONTRACT_CANCELLATION_4C.value,
        )
        self.assertEqual(
            ROUND324_REQUIRED_TARGET_ALIASES["UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE"],
            E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE.value,
        )

    def test_archetype_definitions_capture_r3_loop17_rules(self) -> None:
        ess = archetype_definition(E2RArchetype.ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE)
        cancellation = archetype_definition(E2RArchetype.EV_CONTRACT_CANCELLATION_4C)
        sk_on = archetype_definition(E2RArchetype.SK_ON_ESS_PIVOT_STAGE2_WITH_PARENT_READTHROUGH)
        lithium = archetype_definition(E2RArchetype.LITHIUM_PRICE_REBOUND_CYCLICAL_STAGE2)
        solid = archetype_definition(E2RArchetype.SOLID_STATE_TIMELINE_STAGE2_YELLOW_CANDIDATE)
        ampc = archetype_definition(E2RArchetype.IRA_AMPC_EARNINGS_WITH_POLICY_4B)
        dilution = archetype_definition(E2RArchetype.CAPITAL_RAISE_DILUTION_4B)
        upstream = archetype_definition(E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE)

        self.assertIn("LFP grid-storage demand", " ".join(ess.stage1_radar_signals))
        self.assertIn("Freudenberg", " ".join(cancellation.stage1_radar_signals))
        self.assertIn("expected revenue loss", " ".join(cancellation.stage4c_thesis_break_signals))
        self.assertIn("Flatiron Energy", " ".join(sk_on.stage1_radar_signals))
        self.assertIn("parent readthrough", " ".join(sk_on.false_positive_patterns))
        self.assertIn("CATL Yichun mine suspension", " ".join(lithium.stage1_radar_signals))
        self.assertIn("cathode ASP", " ".join(lithium.stage3_high_conviction_signals))
        self.assertIn("all-solid-state battery timeline", " ".join(solid.stage1_radar_signals))
        self.assertIn("pilot yield", " ".join(solid.stage3_high_conviction_signals))
        self.assertIn("AMPC", " ".join(ampc.stage1_radar_signals))
        self.assertIn("ex-AMPC", " ".join(ampc.stage2_candidate_signals))
        self.assertIn("offering price cut", " ".join(dilution.stage1_radar_signals))
        self.assertIn("MinRes lithium JV", " ".join(upstream.stage1_radar_signals))
        self.assertIn("direct KRX price anchor", " ".join(upstream.stage2_candidate_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round324_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND324_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round324_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", record.green_guardrails)

        by_id = {record.case_id: record for record in records}
        self.assertNotIn("strong_4c_confirmed_false", by_id["r3_loop17_lges_ford_freudenberg_cancellation"].green_guardrails)
        self.assertIn("strong_4c_confirmed_false", by_id["r3_loop17_samsung_sdi_ess_lfp"].green_guardrails)

        summary = round324_summary()
        self.assertEqual(summary["source_round"], "docs/round/round_324.md")
        self.assertEqual(summary["round_id"], "round_252")
        self.assertEqual(summary["large_sector"], ROUND324_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 1)
        self.assertEqual(summary["stage2_candidate_count"], 5)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 4)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["strong_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_capture_stage2_policy_cyclical_dilution_and_4c_patterns(self) -> None:
        by_id = {case.case_id: case for case in ROUND324_CASE_CANDIDATES}
        ess = by_id["r3_loop17_samsung_sdi_ess_lfp"]
        lges_cancel = by_id["r3_loop17_lges_ford_freudenberg_cancellation"]
        sk_on = by_id["r3_loop17_sk_on_ess_flatiron_ford_jv"]
        lithium = by_id["r3_loop17_lithium_rebound_posco_future_m_lnf"]
        solid = by_id["r3_loop17_samsung_sdi_solid_state_timeline"]
        ampc = by_id["r3_loop17_lges_ira_ampc_earnings"]
        dilution = by_id["r3_loop17_samsung_sdi_capital_raise_dilution"]
        upstream = by_id["r3_loop17_posco_minres_lithium_jv"]

        self.assertEqual(ess.extra_price_metrics["contract_value_usd_bn"], 1.36)
        self.assertEqual(ess.extra_price_metrics["market_relative_return_pp"], 6.2)
        self.assertEqual(ess.stage_candidate, "Stage2-Actionable")

        self.assertTrue(lges_cancel.strong_4c_confirmed)
        self.assertEqual(lges_cancel.extra_price_metrics["expected_revenue_loss_krw_trn"], 13.5)
        self.assertEqual(lges_cancel.stage_candidate, "4C")

        self.assertEqual(sk_on.extra_price_metrics["ess_volume_gwh"], 7.2)
        self.assertEqual(sk_on.extra_price_metrics["direct_price_anchor"], "price_data_unavailable_unlisted_subsidiary")

        self.assertEqual(lithium.case_type, "cyclical_success")
        self.assertEqual(lithium.extra_price_metrics["lnf_event_return_pct"], 10)
        self.assertEqual(lithium.rerating_result, "cyclical_rerating")

        self.assertEqual(solid.extra_price_metrics["event_price_krw"], 405500)
        self.assertEqual(solid.stage_failure_type, "yellow_success")

        self.assertEqual(ampc.extra_price_metrics["operating_margin_ex_ampc_pct"], 0.03)
        self.assertEqual(ampc.score_price_alignment, "false_positive_score")

        self.assertEqual(dilution.extra_price_metrics["offering_price_cut_pct"], 14)
        self.assertEqual(dilution.stage_candidate, "4B-watch")

        self.assertEqual(upstream.extra_price_metrics["deal_value_usd_mn"], 765)
        self.assertEqual(upstream.extra_price_metrics["direct_posco_price_anchor"], "price_data_unavailable_after_deep_search")

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round324_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round324_shadow_weight_rows()}
        rules_md = render_round324_stage_rules_markdown()
        trigger_md = render_round324_trigger_grid_markdown()
        stage_md = render_round324_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND324_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r3l17_samsung_sdi_ess_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r3l17_lges_ford_cancel_T0"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r3l17_lges_freudenberg_cancel_T2"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r3l17_lithium_rebound_T0"]["promote_to"], "Stage2_cyclical")
        self.assertEqual(trigger_rows["r3l17_samsung_sdi_solid_state_T0"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r3l17_samsung_sdi_capital_raise_T1"]["promote_to"], "4B-watch")
        self.assertEqual(len(ROUND324_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["EV_CONTRACT_CANCELLATION_4C"]["ev_contract_backlog_without_cancellation_check_penalty"], "-5")
        self.assertEqual(shadow_rows["IRA_AMPC_EARNINGS_WITH_POLICY_4B"]["ampc_credit_dependency_ignored_penalty"], "-5")
        self.assertIn("contract_value_supply_volume_policy_credit_or_production_timeline_is_clear", ROUND324_STAGE2_ACTIONABLE_RULES)
        self.assertIn("gross_margin_or_non_credit_operating_margin_improves", ROUND324_STAGE3_YELLOW_RULES)
        self.assertIn("solid_state_moves_from_timeline_to_customer_revenue", ROUND324_STAGE3_GREEN_RULES)
        self.assertIn("AMPC_credit_dependency_ignored", ROUND324_GREEN_BLOCKERS)
        self.assertIn("ESS_LFP_contract_visibility", ROUND324_SCORE_UP_AXES)
        self.assertIn("capital_raise_dilution_ignored", ROUND324_SCORE_DOWN_AXES)
        self.assertIn("AMPC_driven_profit_with_weak_underlying_margin", ROUND324_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("large_OEM_contract_cancellation", ROUND324_HARD_4C_GATES)
        self.assertIn("do_not_create_MFE_MAE_without_full_adjusted_OHLC", ROUND324_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r3_loop17_lges_ford_freudenberg_cancellation", trigger_md)
        self.assertIn("r3_loop17_lges_ira_ampc_earnings", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round324_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_324.md")
        self.assertEqual(audit["round_id"], "round_252")
        self.assertEqual(audit["large_sector"], ROUND324_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_backtest_v1_after_redteam")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_ESS_contract_AMPC_profit_lithium_rebound_solid_state_timeline_or_dilution_as_Green_without_customer_margin_utilization_revenue_and_risk_resolution", audit["what_not_to_change"])

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

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_round324_r3_loop17_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            loaded = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(loaded), 8)
            self.assertIn("Stage3-Green confirmed: `0`", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("full adjusted OHLC", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertGreater(len(round324_case_rows()), 0)


if __name__ == "__main__":
    unittest.main()
