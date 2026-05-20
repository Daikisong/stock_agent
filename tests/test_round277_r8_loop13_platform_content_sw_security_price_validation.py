from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round277_r8_loop13_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round277_r8_loop13_platform_content_sw_security_price_validation import (
    ROUND277_CASE_CANDIDATES,
    ROUND277_GREEN_FORBIDDEN_PATTERNS,
    ROUND277_GREEN_REQUIRED_FIELDS,
    ROUND277_HARD_4C_GATES,
    ROUND277_LARGE_SECTOR,
    ROUND277_PRICE_VALIDATION_FIELDS,
    ROUND277_REQUIRED_TARGET_ALIASES,
    ROUND277_SHADOW_WEIGHT_ROWS,
    ROUND277_STAGE4B_WATCH_TRIGGERS,
    render_round277_green_gate_review_markdown,
    render_round277_stage4b_4c_review_markdown,
    round277_audit_payload,
    round277_case_records,
    round277_case_rows,
    round277_deep_sub_archetype_rows,
    round277_shadow_weight_rows,
    round277_summary,
    write_round277_r8_loop13_reports,
)


class Round277R8Loop13PlatformContentSwSecurityPriceValidationTests(unittest.TestCase):
    def test_round277_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND277_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND277_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND277_REQUIRED_TARGET_ALIASES["DATA_SOVEREIGNTY_PLATFORM_4C_WATCH"],
            E2RArchetype.DATA_SOVEREIGNTY_PLATFORM_4C_WATCH.value,
        )
        self.assertEqual(
            ROUND277_REQUIRED_TARGET_ALIASES["GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN"],
            E2RArchetype.GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN.value,
        )
        self.assertEqual(
            ROUND277_REQUIRED_TARGET_ALIASES["CYBERSECURITY_TRUST_HARD_4C"],
            E2RArchetype.CYBERSECURITY_TRUST_HARD_4C.value,
        )

    def test_round277_archetype_definitions_capture_r8_loop13_gates(self) -> None:
        data = archetype_definition(E2RArchetype.DATA_SOVEREIGNTY_PLATFORM_4C_WATCH)
        webtoon = archetype_definition(E2RArchetype.GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN)
        kakao = archetype_definition(E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_4C_WATCH)
        hybe = archetype_definition(E2RArchetype.KPOP_IP_GOVERNANCE_4C_WATCH)
        game = archetype_definition(E2RArchetype.GAME_IP_MONETIZATION_IPO_STAGE2)
        cloud = archetype_definition(E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE)
        india = archetype_definition(E2RArchetype.EMERGING_MARKET_GAME_PLATFORM_OPTION)
        cyber = archetype_definition(E2RArchetype.CYBERSECURITY_TRUST_HARD_4C)

        self.assertIn("data governance cleared", data.stage3_high_conviction_signals)
        self.assertIn("MAU-only platform scored as parent EPS", webtoon.false_positive_patterns)
        self.assertIn("founder arrest", kakao.stage4c_thesis_break_signals)
        self.assertIn("artist IP headline treated as Green while governance/legal risk remains", hybe.false_positive_patterns)
        self.assertIn("multi-title durability", game.stage3_high_conviction_signals)
        self.assertIn("IPO valuation break", cloud.stage4c_thesis_break_signals)
        self.assertIn("downloads without ARPU", india.false_positive_patterns)
        self.assertIn("revenue forecast cut", cyber.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round277_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND277_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round277_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round277_summary()
        self.assertEqual(summary["round_id"], "round_205")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["watch_count"], 3)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 4)
        self.assertEqual(summary["stage4c_watch_count"], 6)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["target_archetype_count"], 8)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["hard_4c_confirmed"])

    def test_naver_kakao_hybe_cases_are_governance_or_parent_bridge_guarded(self) -> None:
        by_id = {case.case_id: case for case in ROUND277_CASE_CANDIDATES}
        line = by_id["r8_loop13_naver_line_yahoo_data_sovereignty_watch"]
        webtoon = by_id["r8_loop13_naver_webtoon_entertainment_ipo"]
        kakao = by_id["r8_loop13_kakao_sm_founder_legal_governance"]
        hybe = by_id["r8_loop13_hybe_ador_bang_legal_ip_governance"]

        self.assertEqual(line.primary_archetype, E2RArchetype.DATA_SOVEREIGNTY_PLATFORM_4C_WATCH)
        self.assertEqual(line.extra_price_metrics["buyback_value_jpy_bn"], 150.0)
        self.assertEqual(line.extra_price_metrics["voting_rights_decline_pp"], -1.92)
        self.assertIn("data_governance_clearance_unconfirmed", line.red_flag_fields)

        self.assertEqual(webtoon.primary_archetype, E2RArchetype.GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN)
        self.assertEqual(webtoon.event_mfe_pct, 14.3)
        self.assertEqual(webtoon.extra_price_metrics["monthly_active_users_mn"], 170.0)
        self.assertEqual(webtoon.extra_price_metrics["webtoon_2023_net_loss_usd_mn"], 145.0)
        self.assertFalse(webtoon.extra_price_metrics["naver_parent_value_bridge_confirmed"])

        self.assertEqual(kakao.primary_archetype, E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_4C_WATCH)
        self.assertEqual(kakao.event_mae_pct, -3.4)
        self.assertEqual(kakao.extra_price_metrics["prosecutor_sought_sentence_years"], 15)
        self.assertIn("founder_legal_overhang_unresolved", kakao.red_flag_fields)

        self.assertEqual(hybe.primary_archetype, E2RArchetype.KPOP_IP_GOVERNANCE_4C_WATCH)
        self.assertEqual(hybe.event_mae_pct, -8.0)
        self.assertEqual(hybe.extra_price_metrics["alleged_profit_arrangement_krw_bn"], 190.0)
        self.assertFalse(hybe.extra_price_metrics["governance_legal_clearance_confirmed"])

    def test_shiftup_lgcns_krafton_and_skt_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND277_CASE_CANDIDATES}
        shiftup = by_id["r8_loop13_shiftup_game_ip_ipo_overheat"]
        lgcns = by_id["r8_loop13_lg_cns_ai_cloud_ipo_quality_gate"]
        krafton = by_id["r8_loop13_krafton_india_game_platform_option"]
        skt = by_id["r8_loop13_skt_data_breach_cybersecurity_hard_4c"]

        self.assertEqual(shiftup.primary_archetype, E2RArchetype.GAME_IP_MONETIZATION_IPO_STAGE2)
        self.assertEqual(shiftup.extra_price_metrics["op_margin_2023_pct"], 65.7)
        self.assertFalse(shiftup.extra_price_metrics["post_ipo_multititle_durability_confirmed"])
        self.assertEqual(shiftup.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(lgcns.primary_archetype, E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE)
        self.assertEqual(lgcns.extra_price_metrics["cloud_ai_sales_share_9m2024_pct"], 54.0)
        self.assertEqual(lgcns.extra_price_metrics["debut_mae_vs_ipo_pct"], -3.23)
        self.assertEqual(lgcns.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(krafton.primary_archetype, E2RArchetype.EMERGING_MARKET_GAME_PLATFORM_OPTION)
        self.assertEqual(krafton.extra_price_metrics["bgmi_downloads_mn"], 240.0)
        self.assertEqual(krafton.extra_price_metrics["india_tech_fund_total_usd_mn"], 666.0)
        self.assertTrue(krafton.extra_price_metrics["regulatory_data_security_watch"])

        self.assertEqual(skt.primary_archetype, E2RArchetype.CYBERSECURITY_TRUST_HARD_4C)
        self.assertTrue(skt.hard_4c_confirmed)
        self.assertEqual(skt.event_mae_pct, -8.5)
        self.assertEqual(skt.extra_price_metrics["pipc_fine_krw_bn"], 134.0)
        self.assertEqual(skt.extra_price_metrics["possible_total_compensation_krw_trn"], 2.3)
        self.assertEqual(skt.rerating_result, "thesis_break")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND277_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND277_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND277_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round277_shadow_weight_rows()}
        deep_rows = round277_deep_sub_archetype_rows()
        green_markdown = render_round277_green_gate_review_markdown()
        stage_markdown = render_round277_stage4b_4c_review_markdown()

        self.assertIn("paid_conversion_confirmed", required)
        self.assertIn("cybersecurity_internal_control_confirmed", required)
        self.assertIn("MAU_only", forbidden)
        self.assertIn("data_breach_or_internal_control_failure", forbidden)
        self.assertIn("IPO_debut_plus_10_to_15pct_before_unit_economics", ROUND277_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("revenue_forecast_cut_from_trust_event", ROUND277_HARD_4C_GATES)
        self.assertIn("cybersecurity_trust_cost_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("SK Telecom", stage_markdown)
        self.assertIn("hard 4C", stage_markdown)
        self.assertEqual(len(ROUND277_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["CYBERSECURITY_TRUST_HARD_4C"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Webtoon" in row["terms"] for row in deep_rows))
        self.assertTrue(any("SK Telecom" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round277_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_277.md")
        self.assertEqual(audit["round_id"], "round_205")
        self.assertEqual(audit["large_sector"], ROUND277_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["hard_4c_confirmed"])
        self.assertIn("do_not_use_round277_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round277_r8_loop13_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round277_case_rows()
            self.assertEqual(len(records), len(ROUND277_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND277_CASE_CANDIDATES))
            self.assertIn("Webtoon", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("paid_conversion_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("CYBERSECURITY_TRUST_HARD_4C", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("platform_monetization_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[1]["extra_price_metrics"])["monthly_active_users_mn"], 170.0)


if __name__ == "__main__":
    unittest.main()
