from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round251_r8_loop11_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round251_r8_loop11_platform_content_sw_security_price_validation import (
    ROUND251_CASE_CANDIDATES,
    ROUND251_DEEP_SUB_ARCHETYPES,
    ROUND251_GREEN_FORBIDDEN_PATTERNS,
    ROUND251_GREEN_REQUIRED_FIELDS,
    ROUND251_HARD_4C_GATES,
    ROUND251_LARGE_SECTOR,
    ROUND251_PRICE_VALIDATION_FIELDS,
    ROUND251_REQUIRED_TARGET_ALIASES,
    ROUND251_SCORE_ADJUSTMENTS,
    ROUND251_SHADOW_WEIGHT_ROWS,
    ROUND251_STAGE4B_WATCH_TRIGGERS,
    render_round251_green_gate_review_markdown,
    render_round251_stage4b_4c_review_markdown,
    round251_audit_payload,
    round251_case_records,
    round251_case_rows,
    round251_deep_sub_archetype_rows,
    round251_shadow_weight_rows,
    round251_summary,
    write_round251_r8_loop11_reports,
)


class Round251R8Loop11PlatformContentSwSecurityPriceValidationTests(unittest.TestCase):
    def test_targets_are_explicit_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND251_REQUIRED_TARGET_ALIASES), 12)
        self.assertTrue(set(ROUND251_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND251_REQUIRED_TARGET_ALIASES["AI_SOFTWARE_PARTNERSHIP_EVENT"],
            E2RArchetype.AI_SOFTWARE_PARTNERSHIP_EVENT.value,
        )
        self.assertEqual(
            ROUND251_REQUIRED_TARGET_ALIASES["GAME_IP_PLATFORM_EXPANSION"],
            E2RArchetype.GAME_IP_PLATFORM_EXPANSION.value,
        )
        self.assertEqual(
            ROUND251_REQUIRED_TARGET_ALIASES["GAME_IP_M_AND_A_CONTENT_EXPANSION"],
            E2RArchetype.GAME_IP_M_AND_A_CONTENT_EXPANSION.value,
        )
        self.assertEqual(
            ROUND251_REQUIRED_TARGET_ALIASES["SECURITY_OPERATIONAL_TRUST_HARD_4C"],
            E2RArchetype.SECURITY_OPERATIONAL_TRUST_HARD_4C.value,
        )
        self.assertEqual(
            ROUND251_REQUIRED_TARGET_ALIASES["KPOP_PLATFORM_CONTENT_IP_GOVERNANCE"],
            E2RArchetype.KPOP_PLATFORM_CONTENT_IP_GOVERNANCE.value,
        )

    def test_archetype_definitions_capture_round251_gates(self) -> None:
        partnership = archetype_definition(E2RArchetype.AI_SOFTWARE_PARTNERSHIP_EVENT)
        game_platform = archetype_definition(E2RArchetype.GAME_IP_PLATFORM_EXPANSION)
        game_mna = archetype_definition(E2RArchetype.GAME_IP_M_AND_A_CONTENT_EXPANSION)
        security = archetype_definition(E2RArchetype.SECURITY_OPERATIONAL_TRUST_HARD_4C)
        kpop = archetype_definition(E2RArchetype.KPOP_PLATFORM_CONTENT_IP_GOVERNANCE)

        self.assertIn("paid AI usage", partnership.stage3_high_conviction_signals)
        self.assertIn("compute cost damage", partnership.stage4c_thesis_break_signals)
        self.assertIn("data-security ban", game_platform.stage4c_thesis_break_signals)
        self.assertIn("bookings conversion", game_mna.stage3_high_conviction_signals)
        self.assertIn("privacy breach", security.stage4c_thesis_break_signals)
        self.assertIn("warrant or enforcement action", kpop.stage4c_thesis_break_signals)

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round251_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_treat_ai_platform_webtoon_game_or_kpop_headline_as_green", record.green_guardrails)

        summary = round251_summary()
        self.assertEqual(summary["analyst_round_id"], "round_179")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 7)
        self.assertEqual(summary["stage4c_watch_count"], 1)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["price_moved_without_evidence_count"], 3)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertFalse(summary["full_ohlc_complete"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_saas_ai_cloud_webtoon_and_kakao_cases_are_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND251_CASE_CANDIDATES}
        douzone = by_id["r8_loop11_douzone_bizon_eqt_saas"]
        samsung_sds = by_id["r8_loop11_samsung_sds_kkr_ai_4b"]
        lg_cns = by_id["r8_loop11_lg_cns_ai_cloud_ipo_price_failed"]
        webtoon = by_id["r8_loop11_naver_webtoon_ip_platform"]
        kakao = by_id["r8_loop11_kakao_openai_partnership_price_only"]

        self.assertEqual(douzone.primary_archetype, E2RArchetype.B2B_SAAS_ERP_WORKFLOW)
        self.assertEqual(douzone.stage2_date.isoformat(), "2025-11-07")
        self.assertEqual(douzone.extra_price_metrics["eqt_investment_usd_mn"], 930.0)
        self.assertEqual(douzone.extra_price_metrics["stake_acquired_pct"], 37.6)
        self.assertEqual(douzone.extra_price_metrics["implied_equity_value_usd_bn"], 2.473)
        self.assertIn("arr_unverified", douzone.red_flag_fields)

        self.assertEqual(samsung_sds.primary_archetype, E2RArchetype.AI_CLOUD_CAPITAL_ALLOCATION)
        self.assertEqual(samsung_sds.stage4b_date.isoformat(), "2026-04-15")
        self.assertEqual(samsung_sds.mfe_1d, 20.8)
        self.assertEqual(samsung_sds.extra_price_metrics["relative_intraday_outperformance_pp"], 17.8)
        self.assertEqual(samsung_sds.extra_price_metrics["combined_cash_plus_cb_krw_trn"], 7.607)
        self.assertEqual(samsung_sds.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(lg_cns.primary_archetype, E2RArchetype.CLOUD_AI_SOFTWARE_INFRA)
        self.assertEqual(lg_cns.stage2_price_anchor, 61900.0)
        self.assertEqual(lg_cns.mae_1d, -3.55)
        self.assertEqual(lg_cns.extra_price_metrics["cloud_ai_sales_mix_pct"], 54.0)
        self.assertEqual(lg_cns.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(webtoon.primary_archetype, E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION)
        self.assertEqual(webtoon.stage4b_date.isoformat(), "2025-08-13")
        self.assertEqual(webtoon.extra_price_metrics["disney_event_mfe_pct"], 62.0)
        self.assertEqual(webtoon.extra_price_metrics["pre_disney_post_ipo_drawdown_context_pct"], -55.0)
        self.assertEqual(webtoon.extra_price_metrics["mau_context_mn"], 155.0)
        self.assertIn("mau_without_arpu", webtoon.red_flag_fields)

        self.assertEqual(kakao.case_type, "overheat")
        self.assertEqual(kakao.primary_archetype, E2RArchetype.AI_SOFTWARE_PARTNERSHIP_EVENT)
        self.assertEqual(kakao.stage4b_date.isoformat(), "2025-02-04")
        self.assertEqual(kakao.extra_price_metrics["two_session_cumulative_return_pct"], 6.8)
        self.assertFalse(kakao.extra_price_metrics["paid_usage_confirmed"])
        self.assertEqual(kakao.score_price_alignment, "price_moved_without_evidence")

    def test_game_ip_security_and_governance_cases_feed_watch_or_redteam(self) -> None:
        by_id = {case.case_id: case for case in ROUND251_CASE_CANDIDATES}
        krafton = by_id["r8_loop11_krafton_game_ip_india_adk_watch"]
        skt = by_id["r8_loop11_skt_cybersecurity_operational_trust_hard_4c"]
        hybe = by_id["r8_loop11_hybe_founder_legal_governance_watch"]

        self.assertEqual(krafton.primary_archetype, E2RArchetype.GAME_IP_PLATFORM_EXPANSION)
        self.assertIn(E2RArchetype.GAME_IP_M_AND_A_CONTENT_EXPANSION, krafton.secondary_archetypes)
        self.assertEqual(krafton.extra_price_metrics["adk_acquisition_value_usd_mn"], 516.21)
        self.assertEqual(krafton.extra_price_metrics["bgmi_downloads_mn"], 240.0)
        self.assertIn("bgmi_data_security_regulatory_risk", krafton.red_flag_fields)

        self.assertEqual(skt.primary_archetype, E2RArchetype.SECURITY_OPERATIONAL_TRUST_HARD_4C)
        self.assertEqual(skt.case_type, "4c_thesis_break")
        self.assertTrue(skt.hard_4c_confirmed)
        self.assertEqual(skt.stage4c_date.isoformat(), "2025-04-28")
        self.assertEqual(skt.mae_1d, -8.5)
        self.assertEqual(skt.extra_price_metrics["revenue_forecast_cut_2025_krw_bn"], 800.0)
        self.assertEqual(skt.extra_price_metrics["pipc_fine_krw_bn"], 134.0)
        self.assertEqual(skt.rerating_result, "thesis_break")

        self.assertEqual(hybe.primary_archetype, E2RArchetype.KPOP_PLATFORM_CONTENT_IP_GOVERNANCE)
        self.assertFalse(hybe.hard_4c_confirmed)
        self.assertEqual(hybe.stage4c_date.isoformat(), "2026-04-21")
        self.assertEqual(hybe.extra_price_metrics["relative_underperformance_pp"], -5.1)
        self.assertEqual(hybe.extra_price_metrics["alleged_profit_krw_bn"], 190.0)
        self.assertEqual(hybe.extra_price_metrics["legal_relief_date"], "2026-04-24")
        self.assertIn("warrant_request", hybe.red_flag_fields)

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND251_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND251_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND251_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND251_SCORE_ADJUSTMENTS}
        shadow_rows = {row["archetype"]: row for row in round251_shadow_weight_rows()}
        deep_rows = round251_deep_sub_archetype_rows()
        green_markdown = render_round251_green_gate_review_markdown()
        stage_markdown = render_round251_stage4b_4c_review_markdown()

        self.assertIn("arpu_paid_usage_or_arr_proxy", required)
        self.assertIn("privacy_security_governance_risk_passed", required)
        self.assertIn("ai_partnership_headline_only", forbidden)
        self.assertIn("data_breach_revenue_cut", forbidden)
        self.assertIn("ai_partnership_spike_before_paid_usage", ROUND251_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("privacy_breach", ROUND251_HARD_4C_GATES)
        self.assertIn("reported_event_return", fields)
        self.assertIn("security_or_legal_risk_anchor", fields)
        self.assertIn("recurring_revenue", axes)
        self.assertIn("privacy_security_trust_break", axes)
        self.assertIn("data_breach_revenue_cut", axes)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("Data breach", green_markdown)
        self.assertIn("r8_loop11_skt_cybersecurity_operational_trust_hard_4c", stage_markdown)
        self.assertEqual(len(ROUND251_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["B2B_SAAS_ERP_WORKFLOW"]["recurring_revenue"], "+5")
        self.assertEqual(shadow_rows["AI_SOFTWARE_PARTNERSHIP_EVENT"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["SECURITY_OPERATIONAL_TRUST_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("OpenAI" in row["deep_sub_archetype"] for row in deep_rows))
        self.assertIn("SK Telecom data breach operational trust hard 4C", ROUND251_DEEP_SUB_ARCHETYPES)

    def test_audit_payload_cli_and_writer_outputs(self) -> None:
        audit = round251_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_251.md")
        self.assertEqual(audit["analyst_round_id"], "round_179")
        self.assertEqual(audit["large_sector"], ROUND251_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round251_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round251_r8_loop11_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round251_case_rows()
            self.assertEqual(len(records), len(ROUND251_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND251_CASE_CANDIDATES))
            self.assertIn("SK Telecom is hard 4C", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("paid_usage_conversion", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("AI_SOFTWARE_PARTNERSHIP_EVENT", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("data_breach_revenue_cut", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(rows[2]["round_case_type"], "evidence_good_but_price_failed")
            self.assertEqual(json.loads(rows[1]["extra_price_metrics"])["stage2_event_mfe_1d_pct"], 20.8)


if __name__ == "__main__":
    unittest.main()
