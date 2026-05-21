from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round321_r13_loop16_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round321_r13_loop16_cross_archetype_redteam_price_validation import (
    ROUND321_CASE_CANDIDATES,
    ROUND321_GREEN_BLOCKERS,
    ROUND321_HARD_4C_GATES,
    ROUND321_LARGE_SECTOR,
    ROUND321_REQUIRED_TARGET_ALIASES,
    ROUND321_ROW_SEPARATION_RULES,
    ROUND321_SCORE_DOWN_AXES,
    ROUND321_SCORE_UP_AXES,
    ROUND321_SHADOW_WEIGHT_ROWS,
    ROUND321_STAGE2_ACTIONABLE_RULES,
    ROUND321_STAGE3_GREEN_RULES,
    ROUND321_STAGE3_YELLOW_RULES,
    ROUND321_STAGE4B_WATCH_TRIGGERS,
    ROUND321_TRIGGER_RECORDS,
    render_round321_stage_rules_markdown,
    render_round321_stage4b_4c_review_markdown,
    render_round321_trigger_grid_markdown,
    round321_audit_payload,
    round321_case_records,
    round321_case_rows,
    round321_shadow_weight_rows,
    round321_summary,
    round321_trigger_rows,
    write_round321_r13_loop16_reports,
)


class Round321R13Loop16CrossRedTeamTests(unittest.TestCase):
    def test_round321_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND321_REQUIRED_TARGET_ALIASES), 9)
        self.assertTrue(set(ROUND321_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND321_REQUIRED_TARGET_ALIASES["CROSS_STAGE2_ACTIONABLE_CONFIRMED"],
            E2RArchetype.CROSS_STAGE2_ACTIONABLE_CONFIRMED.value,
        )
        self.assertEqual(
            ROUND321_REQUIRED_TARGET_ALIASES["GOOD_EVIDENCE_PRICE_FAILED"],
            E2RArchetype.GOOD_EVIDENCE_PRICE_FAILED.value,
        )
        self.assertEqual(
            ROUND321_REQUIRED_TARGET_ALIASES["TARIFF_RELIEF_THAT_STILL_SELLOFF"],
            E2RArchetype.TARIFF_RELIEF_THAT_STILL_SELLOFF.value,
        )

    def test_archetype_definitions_capture_r13_loop16_rules(self) -> None:
        actionable = archetype_definition(E2RArchetype.CROSS_STAGE2_ACTIONABLE_CONFIRMED)
        price_failed = archetype_definition(E2RArchetype.GOOD_EVIDENCE_PRICE_FAILED)
        contract = archetype_definition(E2RArchetype.CONTRACT_VALUE_WITH_MARGIN_GATE)
        dilution = archetype_definition(E2RArchetype.GROWTH_WITH_DILUTION_4B)
        export = archetype_definition(E2RArchetype.EXPORT_ORDER_TO_COMBAT_VALIDATION_YELLOW)
        legal = archetype_definition(E2RArchetype.POLICY_OR_PREFERRED_BIDDER_WITH_LEGAL_4B)
        security = archetype_definition(E2RArchetype.SECURITY_TRUST_BREAK_HARD_4C)
        tariff = archetype_definition(E2RArchetype.TARIFF_RELIEF_THAT_STILL_SELLOFF)
        foreign = archetype_definition(E2RArchetype.FOREIGN_STRATEGIC_CAPITAL_WITH_CB_4B)

        self.assertIn("reported event return", " ".join(actionable.stage1_radar_signals))
        self.assertIn("market-relative", " ".join(actionable.stage2_candidate_signals))
        self.assertIn("below issue price", " ".join(price_failed.stage4c_thesis_break_signals))
        self.assertIn("margin", " ".join(contract.stage3_high_conviction_signals))
        self.assertIn("working capital", " ".join(contract.stage3_high_conviction_signals))
        self.assertIn("capital raise", " ".join(dilution.stage1_radar_signals))
        self.assertIn("dilution-adjusted EPS", " ".join(dilution.stage3_high_conviction_signals))
        self.assertIn("combat validation", " ".join(export.stage1_radar_signals))
        self.assertIn("Stage3-Yellow", " ".join(export.stage3_high_conviction_signals))
        self.assertIn("preferred bidder", " ".join(legal.stage1_radar_signals))
        self.assertIn("final contract", " ".join(legal.stage3_high_conviction_signals))
        self.assertIn("data breach", " ".join(security.stage1_radar_signals))
        self.assertIn("spending decline", " ".join(security.stage4c_thesis_break_signals))
        self.assertIn("same-day selloff", " ".join(tariff.stage1_radar_signals))
        self.assertIn("margin damage", " ".join(tariff.stage4c_thesis_break_signals))
        self.assertIn("convertible bond", " ".join(foreign.stage1_radar_signals))
        self.assertIn("M&A ROIC", " ".join(foreign.stage3_high_conviction_signals))

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round321_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND321_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round321_cases_as_candidate_generation_input", record.green_guardrails)
            self.assertIn("do_not_treat_news_size_as_entry_quality_without_price_conversion_dilution_legal_margin_trust_or_tariff_gates", record.green_guardrails)

        by_id = {record.case_id: record for record in records}
        self.assertIn("hard_4c_confirmed_false", by_id["r13_loop16_samsung_sds_kkr_cross_redteam"].green_guardrails)
        self.assertNotIn("hard_4c_confirmed_false", by_id["r13_loop16_coupang_security_delivery_cross_redteam"].green_guardrails)

        summary = round321_summary()
        self.assertEqual(summary["round_id"], "round_249")
        self.assertEqual(summary["large_sector"], ROUND321_LARGE_SECTOR)
        self.assertEqual(summary["method"], "trigger_level_redteam_v1")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["trigger_count"], 9)
        self.assertEqual(summary["target_archetype_count"], 9)
        self.assertEqual(summary["stage2_actionable_candidate_count"], 3)
        self.assertEqual(summary["stage2_candidate_count"], 5)
        self.assertEqual(summary["stage3_yellow_candidate_count"], 5)
        self.assertEqual(summary["stage3_green_confirmed_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 6)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])

    def test_case_metrics_capture_stage2_price_failed_4b_and_4c_patterns(self) -> None:
        by_id = {case.case_id: case for case in ROUND321_CASE_CANDIDATES}
        sds = by_id["r13_loop16_samsung_sds_kkr_cross_redteam"]
        ea = by_id["r13_loop16_samsung_ea_fadhili_cross_redteam"]
        hanwha = by_id["r13_loop16_hanwha_export_dilution_cross_redteam"]
        lig = by_id["r13_loop16_lig_nex1_export_yellow_cross_redteam"]
        lgcns = by_id["r13_loop16_lg_cns_ipo_false_positive_cross_redteam"]
        coupang = by_id["r13_loop16_coupang_security_delivery_cross_redteam"]
        tariff = by_id["r13_loop16_hyundai_kia_tariff_redteam"]
        nuclear = by_id["r13_loop16_czech_nuclear_legal_gate_cross_redteam"]

        self.assertEqual(sds.primary_archetype, E2RArchetype.FOREIGN_STRATEGIC_CAPITAL_WITH_CB_4B)
        self.assertEqual(sds.extra_price_metrics["event_return_intraday_pct"], 20.8)
        self.assertEqual(sds.extra_price_metrics["market_relative_morning_pp"], 16.4)
        self.assertEqual(sds.extra_price_metrics["cb_value_usd_mn"], 820)

        self.assertEqual(ea.extra_price_metrics["contract_value_context_usd_bn"], 6.0)
        self.assertEqual(ea.extra_price_metrics["event_price_krw"], 26750)
        self.assertEqual(ea.extra_price_metrics["market_relative_return_pp"], 9.9)

        self.assertEqual(hanwha.extra_price_metrics["contract_value_usd_bn"], 1.0)
        self.assertEqual(hanwha.extra_price_metrics["capital_raise_plan_krw_trn"], 3.6)
        self.assertEqual(hanwha.extra_price_metrics["dilution_event_return_pct"], -13)

        self.assertEqual(lig.extra_price_metrics["contract_value_krw_trn"], 3.71)
        self.assertEqual(lig.extra_price_metrics["operator_count_after_iraq"], 4)
        self.assertEqual(lig.stage_failure_type, "yellow_success")

        self.assertEqual(lgcns.score_price_alignment, "evidence_good_but_price_failed")
        self.assertEqual(lgcns.extra_price_metrics["issue_price_krw"], 61900)
        self.assertEqual(lgcns.extra_price_metrics["debut_later_price_krw"], 59700)

        self.assertTrue(coupang.hard_4c_confirmed)
        self.assertEqual(coupang.extra_price_metrics["affected_users_mn"], 34)
        self.assertEqual(coupang.extra_price_metrics["coupang_return_since_breach_pct"], -34)
        self.assertEqual(coupang.extra_price_metrics["daily_spending_change_pct"], -6.3)

        self.assertEqual(tariff.extra_price_metrics["tariff_rate_after_deal_pct"], 15)
        self.assertEqual(tariff.extra_price_metrics["hyundai_event_return_pct"], -4.5)
        self.assertEqual(tariff.extra_price_metrics["kia_event_return_pct"], -6.6)

        self.assertEqual(nuclear.extra_price_metrics["project_value_context_usd_bn"], 18)
        self.assertEqual(nuclear.extra_price_metrics["legal_4b_date"], "2025-05-06")
        self.assertIn("final_contract", nuclear.extra_price_metrics["stage3_gate_missing"])

    def test_trigger_rows_shadow_rules_and_reports_are_explicit(self) -> None:
        trigger_rows = {row["trigger_id"]: row for row in round321_trigger_rows()}
        shadow_rows = {row["archetype"]: row for row in round321_shadow_weight_rows()}
        rules_md = render_round321_stage_rules_markdown()
        trigger_md = render_round321_trigger_grid_markdown()
        stage_md = render_round321_stage4b_4c_review_markdown()

        self.assertEqual(len(ROUND321_TRIGGER_RECORDS), 9)
        self.assertEqual(trigger_rows["r13l16_samsung_sds_kkr_T1"]["promote_to"], "Stage2-Actionable")
        self.assertEqual(trigger_rows["r13l16_hanwha_dilution_T3"]["promote_to"], "4B-watch")
        self.assertEqual(trigger_rows["r13l16_lig_iraq_T0"]["promote_to"], "Stage3-Yellow_candidate")
        self.assertEqual(trigger_rows["r13l16_lg_cns_ipo_T1"]["promote_to"], "no_actionable")
        self.assertEqual(trigger_rows["r13l16_coupang_breach_T1"]["promote_to"], "4C")
        self.assertEqual(trigger_rows["r13l16_hyundai_kia_tariff_T1"]["promote_to"], "4C-watch")
        self.assertEqual(trigger_rows["r13l16_czech_nuclear_legal_T2"]["promote_to"], "4B-watch")
        self.assertEqual(len(ROUND321_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["CROSS_STAGE2_ACTIONABLE_CONFIRMED"]["reported_event_return"], "+5")
        self.assertEqual(shadow_rows["GOOD_EVIDENCE_PRICE_FAILED"]["ipo_demand_without_post_listing_strength_penalty"], "-5")
        self.assertEqual(shadow_rows["TARIFF_RELIEF_THAT_STILL_SELLOFF"]["market_relative_return"], "-5")
        self.assertIn("event_return_at_least_5pct", ROUND321_STAGE2_ACTIONABLE_RULES)
        self.assertIn("margin_or_cash_conversion_visibility_improves", ROUND321_STAGE3_YELLOW_RULES)
        self.assertIn("full_OHLC_MFE_MAE_window_supports_candidate", ROUND321_STAGE3_GREEN_RULES)
        self.assertIn("preferred_bidder_without_contract", ROUND321_GREEN_BLOCKERS)
        self.assertIn("tariff_margin_reality", ROUND321_SCORE_UP_AXES)
        self.assertIn("policy_or_trade_relief_headline", ROUND321_SCORE_DOWN_AXES)
        self.assertIn("tariff_relief_headline_followed_by_stock_selloff", ROUND321_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("customer_trust_breach_with_user_or_spending_deterioration", ROUND321_HARD_4C_GATES)
        self.assertIn("trigger_calibration_row_stores_event_anchor_return_contract_value_legal_or_selloff_metrics", ROUND321_ROW_SEPARATION_RULES)
        self.assertIn("Do not apply these weights to production scoring yet.", rules_md)
        self.assertIn("r13_loop16_lg_cns_ipo_false_positive_cross_redteam", trigger_md)
        self.assertIn("r13_loop16_hyundai_kia_tariff_redteam", stage_md)

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round321_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_321.md")
        self.assertEqual(audit["round_id"], "round_249")
        self.assertEqual(audit["large_sector"], ROUND321_LARGE_SECTOR)
        self.assertEqual(audit["method"], "trigger_level_redteam_v1")
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_treat_news_size_as_entry_quality_without_price_conversion_dilution_legal_margin_trust_or_tariff_gates", audit["what_not_to_change"])

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
            paths = write_round321_r13_loop16_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                triggers_path=root / "triggers.jsonl",
                audit_path=root / "audit.json",
                weight_profile_path=root / "weights.csv",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round321_case_rows()
            self.assertEqual(len(records), len(ROUND321_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND321_CASE_CANDIDATES))
            self.assertEqual(len(paths["triggers"].read_text(encoding="utf-8").splitlines()), len(ROUND321_TRIGGER_RECORDS))


if __name__ == "__main__":
    unittest.main()
