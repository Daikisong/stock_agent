from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round282_r13_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round282_r13_loop13_cross_archetype_redteam_price_validation import (
    ROUND282_CASE_CANDIDATES,
    ROUND282_GREEN_FORBIDDEN_PATTERNS,
    ROUND282_GREEN_REQUIRED_FIELDS,
    ROUND282_HARD_4C_GATES,
    ROUND282_LARGE_SECTOR,
    ROUND282_PRICE_VALIDATION_FIELDS,
    ROUND282_REQUIRED_TARGET_ALIASES,
    ROUND282_SHADOW_WEIGHT_ROWS,
    ROUND282_STAGE4B_WATCH_TRIGGERS,
    render_round282_green_gate_review_markdown,
    render_round282_stage4b_4c_review_markdown,
    round282_audit_payload,
    round282_case_records,
    round282_case_rows,
    round282_deep_sub_archetype_rows,
    round282_shadow_weight_rows,
    round282_summary,
    write_round282_r13_loop13_reports,
)


class Round282R13Loop13CrossArchetypeRedTeamPriceValidationTests(unittest.TestCase):
    def test_round282_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND282_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND282_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND282_REQUIRED_TARGET_ALIASES["CYBERSECURITY_TRUST_HARD_4C"],
            E2RArchetype.CYBERSECURITY_TRUST_HARD_4C.value,
        )
        self.assertEqual(
            ROUND282_REQUIRED_TARGET_ALIASES["CONTRACT_VALUE_COLLAPSE_HARD_4C"],
            E2RArchetype.CONTRACT_VALUE_COLLAPSE_HARD_4C.value,
        )
        self.assertEqual(
            ROUND282_REQUIRED_TARGET_ALIASES["CAPITAL_RECYCLING_IPO_FAILED_RERATING"],
            E2RArchetype.CAPITAL_RECYCLING_IPO_FAILED_RERATING.value,
        )

    def test_round282_archetype_definitions_capture_r13_loop13_gates(self) -> None:
        cyber = archetype_definition(E2RArchetype.CYBERSECURITY_TRUST_HARD_4C)
        aviation = archetype_definition(E2RArchetype.AVIATION_SAFETY_HARD_4C)
        contract = archetype_definition(E2RArchetype.CONTRACT_VALUE_COLLAPSE_HARD_4C)
        digital = archetype_definition(E2RArchetype.DIGITAL_ASSET_TRUST_4C_WATCH)
        ipo = archetype_definition(E2RArchetype.IPO_QUALITY_GATE_FALSE_POSITIVE)
        control = archetype_definition(E2RArchetype.CONTROL_PREMIUM_DILUTION_4B)
        order = archetype_definition(E2RArchetype.ORDER_HEADLINE_NOT_MARGIN_GREEN)
        capital = archetype_definition(E2RArchetype.CAPITAL_RECYCLING_IPO_FAILED_RERATING)

        self.assertIn("revenue forecast cut", cyber.stage4c_thesis_break_signals)
        self.assertIn("fatal aviation accident", aviation.stage4c_thesis_break_signals)
        self.assertIn("customer name treated as call-off", contract.false_positive_patterns)
        self.assertIn("M&A synergy before custody trust", digital.false_positive_patterns)
        self.assertIn("AI/cloud keyword treated as aftermarket demand", ipo.false_positive_patterns)
        self.assertIn("control premium treated as operating Green", control.false_positive_patterns)
        self.assertIn("mega-order headline treated as margin", order.false_positive_patterns)
        self.assertIn("IPO size treated as parent Green", capital.false_positive_patterns)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round282_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND282_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("hard_4c_confirmed_true_for_trust_safety_contract_cases", record.green_guardrails)
            self.assertIn("do_not_use_round282_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round282_summary()
        self.assertEqual(summary["round_id"], "round_210")
        self.assertEqual(summary["large_sector"], "CROSS_ARCHETYPE_REDTEAM_4B_ACCOUNTING_TRUST_PRICE_VALIDATION")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 1)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["event_premium_or_result_count"], 3)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 3)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 3)
        self.assertEqual(summary["stage4c_watch_count"], 6)
        self.assertEqual(summary["price_moved_without_evidence_count"], 3)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 2)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_round282_cases_keep_redteam_event_anchors_separate_from_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND282_CASE_CANDIDATES}
        skt = by_id["r13_loop13_skt_cybersecurity_hard_4c"]
        jeju = by_id["r13_loop13_jeju_air_safety_hard_4c"]
        lnf = by_id["r13_loop13_lnf_tesla_contract_collapse"]
        naver = by_id["r13_loop13_naver_dunamu_upbit_trust_4c_watch"]
        lg_cns = by_id["r13_loop13_lg_cns_ipo_quality_false_positive"]
        zinc = by_id["r13_loop13_korea_zinc_control_premium_dilution_4b"]
        samsung_ea = by_id["r13_loop13_samsung_ea_fadhili_order_not_margin_green"]
        hyundai_india = by_id["r13_loop13_hyundai_motor_india_ipo_failed_rerating"]

        self.assertEqual(skt.primary_archetype, E2RArchetype.CYBERSECURITY_TRUST_HARD_4C)
        self.assertEqual(skt.extra_price_metrics["initial_intraday_mae_pct"], -8.5)
        self.assertEqual(skt.extra_price_metrics["initial_close_mae_pct"], -6.7)
        self.assertEqual(skt.extra_price_metrics["leaked_data_pieces_mn"], 26.96)
        self.assertEqual(skt.extra_price_metrics["pipc_fine_krw_bn"], 134)
        self.assertTrue(skt.hard_4c_confirmed)

        self.assertEqual(jeju.primary_archetype, E2RArchetype.AVIATION_SAFETY_HARD_4C)
        self.assertEqual(jeju.extra_price_metrics["fatalities"], 179)
        self.assertEqual(jeju.extra_price_metrics["event_low_price_krw"], 6920)
        self.assertEqual(jeju.extra_price_metrics["market_cap_wipeout_krw_bn"], 95.7)
        self.assertTrue(jeju.hard_4c_confirmed)

        self.assertEqual(lnf.primary_archetype, E2RArchetype.CONTRACT_VALUE_COLLAPSE_HARD_4C)
        self.assertEqual(lnf.extra_price_metrics["initial_projected_value_usd_bn"], 2.9)
        self.assertEqual(lnf.extra_price_metrics["revised_value_usd"], 7386)
        self.assertEqual(lnf.extra_price_metrics["contract_value_collapse_pct"], -99.9997)
        self.assertTrue(lnf.hard_4c_confirmed)

        self.assertEqual(naver.primary_archetype, E2RArchetype.DIGITAL_ASSET_TRUST_4C_WATCH)
        self.assertEqual(naver.extra_price_metrics["deal_value_krw_trn"], 15.13)
        self.assertEqual(naver.extra_price_metrics["naver_initial_mfe_pct"], 7.0)
        self.assertEqual(naver.extra_price_metrics["naver_later_mae_pct"], -4.2)
        self.assertEqual(naver.extra_price_metrics["intraday_swing_pp"], -11.2)
        self.assertEqual(naver.extra_price_metrics["abnormal_withdrawal_krw_bn"], 54)
        self.assertEqual(naver.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(lg_cns.primary_archetype, E2RArchetype.IPO_QUALITY_GATE_FALSE_POSITIVE)
        self.assertEqual(lg_cns.extra_price_metrics["ipo_price_krw"], 61900)
        self.assertEqual(lg_cns.extra_price_metrics["morning_price_krw"], 59700)
        self.assertEqual(lg_cns.extra_price_metrics["debut_mae_vs_ipo_pct"], -3.23)
        self.assertEqual(lg_cns.extra_price_metrics["cloud_ai_share_9m_2024_sales_pct"], 54)
        self.assertEqual(lg_cns.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(zinc.primary_archetype, E2RArchetype.CONTROL_PREMIUM_DILUTION_4B)
        self.assertEqual(zinc.extra_price_metrics["offer_price_krw"], 660000)
        self.assertEqual(zinc.extra_price_metrics["prior_close_krw"], 556000)
        self.assertEqual(zinc.extra_price_metrics["reuters_mfe_pct"], 19.8)
        self.assertEqual(zinc.extra_price_metrics["wsj_mfe_pct"], 24.0)
        self.assertEqual(zinc.extra_price_metrics["new_share_issue_usd_bn"], 1.8)
        self.assertEqual(zinc.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(samsung_ea.primary_archetype, E2RArchetype.ORDER_HEADLINE_NOT_MARGIN_GREEN)
        self.assertEqual(samsung_ea.extra_price_metrics["contract_value_usd_bn"], 6.0)
        self.assertEqual(samsung_ea.extra_price_metrics["event_price_krw"], 26750)
        self.assertEqual(samsung_ea.extra_price_metrics["event_mfe_pct"], 8.5)
        self.assertEqual(samsung_ea.extra_price_metrics["relative_outperformance_pp"], 9.9)
        self.assertEqual(samsung_ea.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(hyundai_india.primary_archetype, E2RArchetype.CAPITAL_RECYCLING_IPO_FAILED_RERATING)
        self.assertEqual(hyundai_india.extra_price_metrics["ipo_value_usd_bn"], 3.3)
        self.assertEqual(hyundai_india.extra_price_metrics["offer_price_inr"], 1960)
        self.assertEqual(hyundai_india.extra_price_metrics["morning_price_inr"], 1882.10)
        self.assertEqual(hyundai_india.extra_price_metrics["debut_mae_pct"], -6.0)
        self.assertEqual(hyundai_india.score_price_alignment, "evidence_good_but_price_failed")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND282_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND282_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND282_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round282_shadow_weight_rows()}
        deep_rows = round282_deep_sub_archetype_rows()
        green_markdown = render_round282_green_gate_review_markdown()
        stage_markdown = render_round282_stage4b_4c_review_markdown()

        self.assertIn("actual_calloff_revenue_recognition_confirmed", required)
        self.assertIn("data_trust_internal_control_confirmed", required)
        self.assertIn("aftermarket_ipo_demand_confirmed", required)
        self.assertIn("customer_name_headline_only", forbidden)
        self.assertIn("IPO_size_or_oversubscription_only", forbidden)
        self.assertIn("M&A_synergy_before_trust", forbidden)
        self.assertIn("mega_order_announcement_day_5_10pct_rally", ROUND282_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("fatal_safety_event", ROUND282_HARD_4C_GATES)
        self.assertIn("data_breach_with_revenue_fine_compensation", ROUND282_HARD_4C_GATES)
        self.assertIn("fine_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("SK Telecom", stage_markdown)
        self.assertIn("hard-4C", stage_markdown)
        self.assertEqual(len(ROUND282_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["CYBERSECURITY_TRUST_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertEqual(shadow_rows["IPO_QUALITY_GATE_FALSE_POSITIVE"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["CONTROL_PREMIUM_DILUTION_4B"]["governance_dilution_control"], "+5")
        self.assertTrue(any("SK Telecom" in row["terms"] for row in deep_rows))
        self.assertTrue(any("Hyundai Motor India IPO" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round282_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_282.md")
        self.assertEqual(audit["round_id"], "round_210")
        self.assertEqual(audit["large_sector"], ROUND282_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round282_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round282_r13_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round282_case_rows()
            self.assertEqual(len(records), len(ROUND282_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND282_CASE_CANDIDATES))
            self.assertIn("SK Telecom", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("actual_calloff_revenue_recognition_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("CONTROL_PREMIUM_DILUTION_4B", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("fine_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["pipc_fine_krw_bn"], 134)


if __name__ == "__main__":
    unittest.main()
