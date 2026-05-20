from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round238_r8_loop10_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector
from e2r.sector.round238_r8_loop10_platform_content_sw_security_price_validation import (
    ROUND238_CASE_CANDIDATES,
    ROUND238_GREEN_FORBIDDEN_PATTERNS,
    ROUND238_GREEN_REQUIRED_FIELDS,
    ROUND238_HARD_4C_GATES,
    ROUND238_PRICE_VALIDATION_FIELDS,
    ROUND238_REQUIRED_TARGET_ALIASES,
    ROUND238_SCORE_ADJUSTMENTS,
    ROUND238_SHADOW_WEIGHT_ROWS,
    ROUND238_STAGE4B_WATCH_TRIGGERS,
    render_round238_green_gate_review_markdown,
    render_round238_stage4b_4c_review_markdown,
    round238_audit_payload,
    round238_case_records,
    round238_case_rows,
    round238_summary,
    write_round238_r8_loop10_reports,
)


class Round238R8Loop10PlatformContentSwSecurityPriceValidationTests(unittest.TestCase):
    def test_round238_targets_map_to_existing_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND238_REQUIRED_TARGET_ALIASES), 13)
        self.assertTrue(set(ROUND238_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND238_REQUIRED_TARGET_ALIASES["AI_SOFTWARE_PARTNERSHIP_EVENT"],
            E2RArchetype.AI_SOFTWARE_APPLICATION.value,
        )
        self.assertEqual(
            ROUND238_REQUIRED_TARGET_ALIASES["GAME_IP_REPEAT_MONETIZATION"],
            E2RArchetype.GAME_CONTENT_IP_REPEAT_MONETIZATION.value,
        )
        self.assertEqual(
            ROUND238_REQUIRED_TARGET_ALIASES["GAME_IP_IPO_PREMIUM"],
            E2RArchetype.SINGLE_IP_RELEASE_EVENT_PREMIUM.value,
        )

    def test_case_records_validate_and_keep_calibration_guardrails(self) -> None:
        records = round238_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY.value)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("full_ohlc_complete_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)

        summary = round238_summary()
        self.assertEqual(summary["analyst_round_id"], "round_166")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 3)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["failed_rerating_count"], 2)
        self.assertEqual(summary["overheat_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["strong_4c_watch_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["full_ohlc_complete"])

    def test_douzone_and_shiftup_are_stage2_watch_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND238_CASE_CANDIDATES}
        douzone = by_id["r8_loop10_douzone_eqt_b2b_saas_stage2_watch"]
        shiftup = by_id["r8_loop10_shiftup_single_ip_repeat_monetization_watch"]

        self.assertEqual(douzone.primary_archetype, E2RArchetype.B2B_SAAS_ERP_WORKFLOW)
        self.assertEqual(douzone.stage2_date.isoformat(), "2025-11-07")
        self.assertIsNone(douzone.stage3_date)
        self.assertEqual(douzone.extra_price_metrics["eqt_investment_usd_mn"], 930.0)
        self.assertEqual(douzone.extra_price_metrics["stake_pct"], 37.6)
        self.assertIn("arr_unverified", douzone.red_flag_fields)

        self.assertEqual(shiftup.primary_archetype, E2RArchetype.GAME_CONTENT_IP_REPEAT_MONETIZATION)
        self.assertEqual(shiftup.stage2_date.isoformat(), "2024-07-01")
        self.assertIsNone(shiftup.stage3_date)
        self.assertEqual(shiftup.extra_price_metrics["opm_2023_pct"], 65.7)
        self.assertEqual(shiftup.extra_price_metrics["stellar_blade_total_sales_mn"], 3.0)
        self.assertIn("single_ip_dependence", shiftup.red_flag_fields)

    def test_ai_cloud_webtoon_and_kakao_events_are_not_green(self) -> None:
        by_id = {case.case_id: case for case in ROUND238_CASE_CANDIDATES}
        samsung_sds = by_id["r8_loop10_samsung_sds_ai_cloud_kkr_event_premium"]
        lg_cns = by_id["r8_loop10_lg_cns_ipo_cloud_ai_price_failed"]
        webtoon = by_id["r8_loop10_naver_webtoon_ipo_disney_ip_watch"]
        kakao = by_id["r8_loop10_kakao_openai_partnership_price_only_rally"]

        self.assertEqual(samsung_sds.case_type, "event_premium")
        self.assertEqual(samsung_sds.round_case_type, "success_candidate_4b_watch")
        self.assertEqual(samsung_sds.primary_archetype, E2RArchetype.AI_CLOUD_CAPITAL_ALLOCATION)
        self.assertEqual(samsung_sds.stage4b_date.isoformat(), "2026-04-15")
        self.assertEqual(samsung_sds.mfe_1d, 20.8)
        self.assertEqual(samsung_sds.extra_price_metrics["relative_outperformance_pp"], 17.8)
        self.assertEqual(samsung_sds.extra_price_metrics["combined_liquidity_krw_tn"], 7.607)
        self.assertEqual(samsung_sds.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(lg_cns.case_type, "failed_rerating")
        self.assertEqual(lg_cns.round_case_type, "evidence_good_but_price_failed")
        self.assertEqual(lg_cns.stage2_price_anchor, 61900.0)
        self.assertEqual(lg_cns.mae_1d, -3.55)
        self.assertEqual(lg_cns.extra_price_metrics["morning_market_value_krw_tn"], 5.79)
        self.assertEqual(lg_cns.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(webtoon.primary_archetype, E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION)
        self.assertEqual(webtoon.extra_price_metrics["disney_event_mfe_pct"], 62.0)
        self.assertEqual(webtoon.extra_price_metrics["pre_disney_post_ipo_drawdown_pct"], -55.0)
        self.assertEqual(webtoon.extra_price_metrics["disney_event_revenue_usd_mn"], 348.3)
        self.assertEqual(webtoon.extra_price_metrics["mau_context_mn"], 155.0)
        self.assertIn("mau_without_arpu", webtoon.red_flag_fields)

        self.assertEqual(kakao.case_type, "overheat")
        self.assertEqual(kakao.primary_archetype, E2RArchetype.AI_SOFTWARE_APPLICATION)
        self.assertEqual(kakao.stage4b_date.isoformat(), "2025-02-04")
        self.assertEqual(kakao.extra_price_metrics["two_session_return_pct"], 6.8)
        self.assertIn("partnership_headline_only", kakao.red_flag_fields)

    def test_security_and_governance_cases_feed_redteam_not_positive_scoring(self) -> None:
        by_id = {case.case_id: case for case in ROUND238_CASE_CANDIDATES}
        skt = by_id["r8_loop10_skt_data_breach_operational_trust_4c_watch"]
        hybe = by_id["r8_loop10_hybe_founder_legal_governance_4c_watch"]

        self.assertEqual(skt.primary_archetype, E2RArchetype.SECURITY_OPERATIONAL_TRUST_OVERLAY)
        self.assertEqual(skt.case_type, "4c_thesis_break")
        self.assertFalse(skt.hard_4c_confirmed)
        self.assertEqual(skt.stage4c_date.isoformat(), "2025-04-28")
        self.assertEqual(skt.mae_1d, -8.5)
        self.assertEqual(skt.extra_price_metrics["affected_users_mn"], 23.0)
        self.assertEqual(skt.extra_price_metrics["security_investment_krw_bn"], 700.0)
        self.assertEqual(skt.extra_price_metrics["pipc_fine_krw_bn"], 134.8)
        self.assertEqual(skt.round_case_type, "strong_4c_watch_operational_trust_break")
        self.assertIn("privacy_breach_or_security_outage", skt.red_flag_fields)

        self.assertEqual(hybe.primary_archetype, E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK)
        self.assertEqual(hybe.case_type, "failed_rerating")
        self.assertEqual(hybe.stage4c_date.isoformat(), "2026-04-21")
        self.assertFalse(hybe.extra_price_metrics["hard_4c_confirmed"])
        self.assertEqual(hybe.extra_price_metrics["alleged_profit_krw_bn"], 190.0)
        self.assertEqual(hybe.round_case_type, "governance_legal_4c_watch")
        self.assertIn("founder_legal_risk", hybe.red_flag_fields)

    def test_green_gate_4b_4c_and_shadow_weights_are_explicit(self) -> None:
        required = set(ROUND238_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND238_GREEN_FORBIDDEN_PATTERNS)
        review = render_round238_green_gate_review_markdown()
        stage_review = render_round238_stage4b_4c_review_markdown()
        weights = {row.archetype: row for row in ROUND238_SHADOW_WEIGHT_ROWS}

        self.assertIn("recurring_revenue_or_bookings", required)
        self.assertIn("paid_usage_or_arpu_or_arr_proxy", required)
        self.assertIn("ai_partnership_headline_only", forbidden)
        self.assertIn("game_first_week_sales_only", forbidden)
        self.assertIn("data_breach_revenue_cut", ROUND238_HARD_4C_GATES)
        self.assertIn("ai_partnership_spike_before_paid_usage", ROUND238_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("Do not apply these weights to production scoring yet.", review)
        self.assertIn("r8_loop10_skt_data_breach_operational_trust_4c_watch", stage_review)
        self.assertEqual(weights[E2RArchetype.B2B_SAAS_ERP_WORKFLOW].recurring_revenue, 5)
        self.assertEqual(weights[E2RArchetype.AI_CLOUD_CAPITAL_ALLOCATION].event_penalty, -5)
        self.assertEqual(weights[E2RArchetype.SECURITY_OPERATIONAL_TRUST_OVERLAY].security_privacy_trust, 5)

    def test_price_fields_and_score_axes_cover_r8_loop10(self) -> None:
        fields = set(ROUND238_PRICE_VALIDATION_FIELDS)
        axes = {item.axis for item in ROUND238_SCORE_ADJUSTMENTS}

        self.assertIn("transaction_or_capital_anchor", fields)
        self.assertIn("trust_or_legal_risk_anchor", fields)
        self.assertIn("recurring_revenue", axes)
        self.assertIn("security_privacy_trust", axes)
        self.assertIn("paid_usage_conversion", axes)
        self.assertIn("privacy_security_trust_break", axes)
        self.assertIn("data_breach_revenue_cut", axes)

    def test_audit_payload_marks_non_production_round(self) -> None:
        audit = round238_audit_payload()

        self.assertEqual(audit["source_round"], "docs/round/round_238.md")
        self.assertEqual(audit["analyst_round_id"], "round_166")
        self.assertEqual(audit["large_sector"], Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY.value)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertIn("do_not_use_round238_cases_as_candidate_generation_input", audit["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self) -> None:
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round238_r8_loop10_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round238_case_rows()
            self.assertEqual(len(records), len(ROUND238_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND238_CASE_CANDIDATES))
            self.assertIn("더존비즈온", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("ai_partnership_headline_only", paths["score_adjustments"].read_text(encoding="utf-8"))
            self.assertIn("B2B_SAAS_ERP_WORKFLOW", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("data_breach_revenue_cut", paths["stage4b_4c_review"].read_text(encoding="utf-8"))
            self.assertEqual(rows[2]["round_case_type"], "evidence_good_but_price_failed")
            self.assertEqual(json.loads(rows[1]["extra_price_metrics"])["event_mfe_pct"], 20.8)


if __name__ == "__main__":
    unittest.main()
