from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round264_r8_loop12_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round264_r8_loop12_platform_content_sw_security_price_validation import (
    ROUND264_CASE_CANDIDATES,
    ROUND264_DEEP_SUB_ARCHETYPES,
    ROUND264_GREEN_FORBIDDEN_PATTERNS,
    ROUND264_GREEN_REQUIRED_FIELDS,
    ROUND264_HARD_4C_GATES,
    ROUND264_LARGE_SECTOR,
    ROUND264_PRICE_VALIDATION_FIELDS,
    ROUND264_REQUIRED_TARGET_ALIASES,
    ROUND264_SCORE_ADJUSTMENTS,
    ROUND264_SHADOW_WEIGHT_ROWS,
    ROUND264_STAGE4B_WATCH_TRIGGERS,
    render_round264_green_gate_review_markdown,
    render_round264_stage4b_4c_review_markdown,
    round264_audit_payload,
    round264_case_records,
    round264_case_rows,
    round264_deep_sub_archetype_rows,
    round264_shadow_weight_rows,
    round264_summary,
    write_round264_r8_loop12_reports,
)


class Round264R8Loop12PlatformContentSwSecurityPriceValidationTests(unittest.TestCase):
    def test_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND264_REQUIRED_TARGET_ALIASES), 7)
        self.assertTrue(set(ROUND264_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND264_REQUIRED_TARGET_ALIASES["GAME_IP_IPO_SINGLE_TITLE_RISK"],
            E2RArchetype.GAME_IP_IPO_SINGLE_TITLE_RISK.value,
        )
        self.assertEqual(
            ROUND264_REQUIRED_TARGET_ALIASES["KIDS_CONTENT_IP_IPO_EVENT_PREMIUM"],
            E2RArchetype.KIDS_CONTENT_IP_IPO_EVENT_PREMIUM.value,
        )
        self.assertEqual(
            ROUND264_REQUIRED_TARGET_ALIASES["KPOP_IP_CHINA_OPTIONALITY"],
            E2RArchetype.KPOP_IP_CHINA_OPTIONALITY.value,
        )
        self.assertEqual(
            ROUND264_REQUIRED_TARGET_ALIASES["DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE"],
            E2RArchetype.DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE.value,
        )
        self.assertEqual(
            ROUND264_REQUIRED_TARGET_ALIASES["TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C"],
            E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C.value,
        )

    def test_archetype_definitions_capture_round264_gates(self) -> None:
        game_ipo = archetype_definition(E2RArchetype.GAME_IP_IPO_SINGLE_TITLE_RISK)
        kids_ip = archetype_definition(E2RArchetype.KIDS_CONTENT_IP_IPO_EVENT_PREMIUM)
        kpop_china = archetype_definition(E2RArchetype.KPOP_IP_CHINA_OPTIONALITY)
        digital_mna = archetype_definition(E2RArchetype.DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE)
        ecommerce = archetype_definition(E2RArchetype.ECOMMERCE_PLATFORM_DATA_BREACH_4C)
        game_governance = archetype_definition(E2RArchetype.GAME_STUDIO_M_AND_A_GOVERNANCE_4C)
        telecom = archetype_definition(E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C)

        self.assertIn("live-service retention", game_ipo.stage3_high_conviction_signals)
        self.assertIn("IPO valuation before repeat hit proof", game_ipo.stage4b_graduation_overheat_signals)
        self.assertIn("repeat-hit generation", kids_ip.stage3_high_conviction_signals)
        self.assertIn("China reopening expectation priced before ticket revenue", kpop_china.stage4b_graduation_overheat_signals)
        self.assertIn("abnormal withdrawal", digital_mna.stage4c_thesis_break_signals)
        self.assertIn("major data breach", ecommerce.stage4c_thesis_break_signals)
        self.assertIn("M&A governance dispute", game_governance.stage4c_thesis_break_signals)
        self.assertIn("revenue guidance cut", telecom.stage4c_thesis_break_signals)

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round264_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_ipo_hit_title_single_ip_mna_or_china_optional_headline_as_green", record.green_guardrails)

        summary = round264_summary()
        self.assertEqual(summary["analyst_round_id"], "round_192")
        self.assertEqual(summary["case_candidate_count"], 7)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["stage4c_watch_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_game_kids_kpop_and_platform_deal_cases_are_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND264_CASE_CANDIDATES}
        shift_up = by_id["r8_loop12_shift_up_game_ip_ipo_single_title_watch"]
        pinkfong = by_id["r8_loop12_pinkfong_kids_content_ip_ipo_event"]
        sm = by_id["r8_loop12_sm_tencent_kpop_china_optionality"]
        naver = by_id["r8_loop12_naver_dunamu_platform_merger_trust_gate"]

        self.assertEqual(shift_up.primary_archetype, E2RArchetype.GAME_IP_IPO_SINGLE_TITLE_RISK)
        self.assertEqual(shift_up.stage2_date.isoformat(), "2024-06-27")
        self.assertEqual(shift_up.extra_price_metrics["op_margin_2023_pct"], 65.7)
        self.assertEqual(shift_up.extra_price_metrics["ipo_valuation_to_revenue_2023"], 20.7)
        self.assertEqual(shift_up.extra_price_metrics["tencent_post_ipo_stake_pct"], 35.0)
        self.assertIn("single_title_concentration", shift_up.red_flag_fields)

        self.assertEqual(pinkfong.primary_archetype, E2RArchetype.KIDS_CONTENT_IP_IPO_EVENT_PREMIUM)
        self.assertEqual(pinkfong.mfe_1d, 62.0)
        self.assertEqual(pinkfong.extra_price_metrics["close_price_krw"], 41550.0)
        self.assertEqual(pinkfong.extra_price_metrics["op_margin_pct"], 19.3)
        self.assertEqual(pinkfong.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(sm.primary_archetype, E2RArchetype.KPOP_IP_CHINA_OPTIONALITY)
        self.assertEqual(sm.extra_price_metrics["stake_sold_pct"], 9.7)
        self.assertEqual(sm.extra_price_metrics["transaction_value_krw_bn"], 243.0)
        self.assertEqual(sm.extra_price_metrics["implied_sm_equity_value_krw_trn"], 2.51)
        self.assertEqual(sm.extra_price_metrics["kakao_kakaoent_control_stake_pct"], 42.0)
        self.assertIn("ticket_revenue_unverified", sm.red_flag_fields)

        self.assertEqual(naver.primary_archetype, E2RArchetype.DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE)
        self.assertEqual(naver.mfe_1d, 7.0)
        self.assertEqual(naver.mae_1d, -4.2)
        self.assertEqual(naver.extra_price_metrics["abnormal_withdrawal_krw_bn"], 54.0)
        self.assertIn("exchange_trust_unresolved", naver.red_flag_fields)

    def test_trust_governance_and_telecom_cases_feed_redteam(self) -> None:
        by_id = {case.case_id: case for case in ROUND264_CASE_CANDIDATES}
        coupang = by_id["r8_loop12_coupang_platform_data_breach_reference"]
        krafton = by_id["r8_loop12_krafton_unknown_worlds_subnautica_governance_watch"]
        skt = by_id["r8_loop12_skt_cybersecurity_operational_trust_hard_4c"]

        self.assertEqual(coupang.primary_archetype, E2RArchetype.ECOMMERCE_PLATFORM_DATA_BREACH_4C)
        self.assertEqual(coupang.symbol, "CPNG_non_KRX")
        self.assertEqual(coupang.mae_1d, -4.0)
        self.assertEqual(coupang.mfe_1d, 9.2)
        self.assertEqual(coupang.extra_price_metrics["breach_affected_accounts_mn"], 33.7)
        self.assertEqual(coupang.extra_price_metrics["retained_data_share_pct"], 0.0091)
        self.assertIn("non_krx_reference_gap", coupang.red_flag_fields)

        self.assertEqual(krafton.primary_archetype, E2RArchetype.GAME_STUDIO_M_AND_A_GOVERNANCE_4C)
        self.assertEqual(krafton.stage4c_date.isoformat(), "2026-03-16")
        self.assertEqual(krafton.extra_price_metrics["unknown_worlds_acquisition_upfront_usd_mn"], 500.0)
        self.assertEqual(krafton.extra_price_metrics["earnout_at_issue_usd_mn"], 250.0)
        self.assertIn("mna_governance_dispute", krafton.red_flag_fields)

        self.assertEqual(skt.primary_archetype, E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C)
        self.assertTrue(skt.hard_4c_confirmed)
        self.assertEqual(skt.stage4c_date.isoformat(), "2025-04-28")
        self.assertEqual(skt.mae_1d, -8.5)
        self.assertEqual(skt.extra_price_metrics["revenue_forecast_cut_2025_krw_bn"], 800.0)
        self.assertEqual(skt.extra_price_metrics["possible_all_victim_compensation_cost_krw_trn"], 2.3)
        self.assertEqual(skt.rerating_result, "thesis_break")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND264_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND264_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND264_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND264_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round264_shadow_weight_rows()}
        deep_rows = round264_deep_sub_archetype_rows()
        green_markdown = render_round264_green_gate_review_markdown()
        stage_markdown = render_round264_stage4b_4c_review_markdown()

        self.assertIn("paid_user_or_active_user_retention", required)
        self.assertIn("cybersecurity_data_governance_risk_passed", required)
        self.assertIn("ipo_pop_only", forbidden)
        self.assertIn("data_breach_unresolved", forbidden)
        self.assertIn("ipo_first_day_50pct_plus_spike", ROUND264_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("cybersecurity_breach_with_revenue_guidance_cut", ROUND264_HARD_4C_GATES)
        self.assertIn("trust_security_or_governance_anchor", fields)
        self.assertIn("paid_user_retention", axes)
        self.assertIn("cybersecurity_revenue_cut", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("M&A deal value", green_markdown)
        self.assertIn("r8_loop12_skt_cybersecurity_operational_trust_hard_4c", stage_markdown)
        self.assertEqual(len(ROUND264_SHADOW_WEIGHT_ROWS), 7)
        self.assertEqual(shadow_rows["GAME_IP_IPO_SINGLE_TITLE_RISK"]["repeat_hit"], "+5")
        self.assertEqual(shadow_rows["DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE"]["platform_trust"], "+5")
        self.assertEqual(shadow_rows["TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Subnautica" in row["deep_sub_archetype"] for row in deep_rows))
        self.assertIn("SK Telecom USIM data breach / direct KRX cybersecurity hard 4C", ROUND264_DEEP_SUB_ARCHETYPES)

    def test_audit_payload_cli_and_writer_outputs(self) -> None:
        audit = round264_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_264.md")
        self.assertEqual(audit["analyst_round_id"], "round_192")
        self.assertEqual(audit["large_sector"], ROUND264_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round264_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round264_r8_loop12_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round264_case_rows()
            self.assertEqual(len(records), len(ROUND264_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND264_CASE_CANDIDATES))
            self.assertIn("SK Telecom is direct KRX hard 4C", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("paid_user_retention", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("GAME_IP_IPO_SINGLE_TITLE_RISK", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("cybersecurity_breach_with_revenue_guidance_cut", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(rows[1]["round_alignment_label"], "event_premium")
            self.assertEqual(json.loads(rows[3]["extra_price_metrics"])["abnormal_withdrawal_krw_bn"], 54.0)


if __name__ == "__main__":
    unittest.main()
