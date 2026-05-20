from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.cli.build_round290_r8_loop14_report import build_parser
from e2r.sector.archetypes import E2RArchetype, archetype_definition
from e2r.sector.case_library import load_case_library
from e2r.sector.round290_r8_loop14_platform_content_sw_security_price_validation import (
    ROUND290_CASE_CANDIDATES,
    ROUND290_GREEN_FORBIDDEN_PATTERNS,
    ROUND290_GREEN_REQUIRED_FIELDS,
    ROUND290_HARD_4C_GATES,
    ROUND290_LARGE_SECTOR,
    ROUND290_PRICE_VALIDATION_FIELDS,
    ROUND290_REQUIRED_TARGET_ALIASES,
    ROUND290_SHADOW_WEIGHT_ROWS,
    ROUND290_STAGE4B_WATCH_TRIGGERS,
    render_round290_green_gate_review_markdown,
    render_round290_stage4b_4c_review_markdown,
    round290_audit_payload,
    round290_case_records,
    round290_case_rows,
    round290_deep_sub_archetype_rows,
    round290_shadow_weight_rows,
    round290_summary,
    write_round290_r8_loop14_reports,
)


class Round290R8Loop14PlatformContentSwSecurityPriceValidationTests(unittest.TestCase):
    def test_round290_targets_are_exact_canonical_archetypes(self) -> None:
        canonical_values = {item.value for item in E2RArchetype}

        self.assertEqual(len(ROUND290_REQUIRED_TARGET_ALIASES), 8)
        self.assertTrue(set(ROUND290_REQUIRED_TARGET_ALIASES.values()).issubset(canonical_values))
        self.assertEqual(
            ROUND290_REQUIRED_TARGET_ALIASES["WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE"],
            E2RArchetype.WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE.value,
        )
        self.assertEqual(
            ROUND290_REQUIRED_TARGET_ALIASES["KPOP_IP_CONTRACT_GOVERNANCE_4C"],
            E2RArchetype.KPOP_IP_CONTRACT_GOVERNANCE_4C.value,
        )
        self.assertEqual(
            ROUND290_REQUIRED_TARGET_ALIASES["CYBERSECURITY_TRUST_HARD_4C_REFERENCE"],
            E2RArchetype.CYBERSECURITY_TRUST_HARD_4C_REFERENCE.value,
        )

    def test_round290_archetype_definitions_capture_loop14_gates(self) -> None:
        webtoon = archetype_definition(E2RArchetype.WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE)
        kakao = archetype_definition(E2RArchetype.KAKAO_PLATFORM_GOVERNANCE_4C_WATCH)
        hybe = archetype_definition(E2RArchetype.KPOP_IP_CONTRACT_GOVERNANCE_4C)
        shiftup = archetype_definition(E2RArchetype.GAME_IP_IPO_STAGE2_QUALITY_GATE)
        ncsoft = archetype_definition(E2RArchetype.LEGACY_GAME_TURNAROUND_BUYBACK_4B)
        lgcns = archetype_definition(E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE)
        douzone = archetype_definition(E2RArchetype.ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2)
        skt = archetype_definition(E2RArchetype.CYBERSECURITY_TRUST_HARD_4C_REFERENCE)

        self.assertIn("paid conversion / ARPU", webtoon.stage3_high_conviction_signals)
        self.assertIn("revenue guide miss", webtoon.stage4c_thesis_break_signals)
        self.assertIn("founder arrest", kakao.stage4c_thesis_break_signals)
        self.assertIn("artist contract continuity", hybe.stage3_high_conviction_signals)
        self.assertIn("live-service retention", shiftup.stage3_high_conviction_signals)
        self.assertIn("buyback without business recovery", ncsoft.stage4c_thesis_break_signals)
        self.assertIn("weak IPO debut", lgcns.stage4c_thesis_break_signals)
        self.assertIn("ARR retention", douzone.stage3_high_conviction_signals)
        self.assertIn("revenue forecast cut", skt.stage4c_thesis_break_signals)

    def test_case_records_validate_and_are_calibration_only(self) -> None:
        records = round290_case_records()
        for record in records:
            record.validate()
            self.assertEqual(record.large_sector, ROUND290_LARGE_SECTOR)
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertIn("full_adjusted_ohlc_complete_false", record.green_guardrails)
            self.assertIn("do_not_use_round290_cases_as_candidate_generation_input", record.green_guardrails)

        summary = round290_summary()
        self.assertEqual(summary["round_id"], "round_218")
        self.assertEqual(summary["case_candidate_count"], 8)
        self.assertEqual(summary["success_candidate_count"], 2)
        self.assertEqual(summary["event_premium_count"], 2)
        self.assertEqual(summary["failed_rerating_count"], 1)
        self.assertEqual(summary["watch_count"], 2)
        self.assertEqual(summary["hard_4c_case_count"], 1)
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["stage4b_watch_count"], 5)
        self.assertEqual(summary["stage4c_watch_count"], 4)
        self.assertEqual(summary["price_moved_without_evidence_count"], 2)
        self.assertEqual(summary["evidence_good_but_price_failed_count"], 1)
        self.assertEqual(summary["false_positive_score_count"], 1)
        self.assertEqual(summary["unknown_alignment_count"], 4)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertFalse(summary["full_adjusted_ohlc_complete"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertTrue(summary["direct_KRX_hard_4c_confirmed"])

    def test_platform_content_cases_are_not_green_without_specific_gates(self) -> None:
        by_id = {case.case_id: case for case in ROUND290_CASE_CANDIDATES}
        webtoon = by_id["r8_loop14_naver_webtoon_ipo_aftermarket_gate"]
        kakao = by_id["r8_loop14_kakao_platform_governance_sm_case"]
        hybe = by_id["r8_loop14_hybe_ador_newjeans_ip_governance"]

        self.assertEqual(webtoon.primary_archetype, E2RArchetype.WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE)
        self.assertEqual(webtoon.event_mfe_pct, 14.3)
        self.assertEqual(webtoon.event_mae_pct, -15.0)
        self.assertEqual(webtoon.extra_price_metrics["monthly_active_users_mn"], 170.0)
        self.assertEqual(webtoon.score_price_alignment, "price_moved_without_evidence")
        self.assertIn("IPO_pop_only", webtoon.red_flag_fields)

        self.assertEqual(kakao.primary_archetype, E2RArchetype.KAKAO_PLATFORM_GOVERNANCE_4C_WATCH)
        self.assertEqual(kakao.event_mae_pct, -3.4)
        self.assertEqual(kakao.extra_price_metrics["prosecutor_sought_sentence_years"], 15)
        self.assertIn("governance_legal_risk_unresolved", kakao.red_flag_fields)

        self.assertEqual(hybe.primary_archetype, E2RArchetype.KPOP_IP_CONTRACT_GOVERNANCE_4C)
        self.assertEqual(hybe.event_mae_pct, -8.0)
        self.assertTrue(hybe.extra_price_metrics["newjeans_contract_dispute_persistence"])
        self.assertIn("artist_fandom_without_contract_stability", hybe.red_flag_fields)

    def test_game_software_and_security_cases_are_separated(self) -> None:
        by_id = {case.case_id: case for case in ROUND290_CASE_CANDIDATES}
        shiftup = by_id["r8_loop14_shift_up_game_ip_ipo_quality_gate"]
        ncsoft = by_id["r8_loop14_ncsoft_earnings_buyback_turnaround"]
        lgcns = by_id["r8_loop14_lg_cns_ai_cloud_ipo_false_positive"]
        douzone = by_id["r8_loop14_douzone_bizon_eqt_enterprise_sw_stage2"]
        skt = by_id["r8_loop14_sk_telecom_cybersecurity_trust_hard_4c"]

        self.assertEqual(shiftup.primary_archetype, E2RArchetype.GAME_IP_IPO_STAGE2_QUALITY_GATE)
        self.assertEqual(shiftup.extra_price_metrics["op_margin_2023_pct"], 65.7)
        self.assertIn("live_service_retention", shiftup.extra_price_metrics["stage3_conditions"])

        self.assertEqual(ncsoft.primary_archetype, E2RArchetype.LEGACY_GAME_TURNAROUND_BUYBACK_4B)
        self.assertEqual(ncsoft.event_mfe_pct, 14.0)
        self.assertFalse(ncsoft.extra_price_metrics["new_title_retention_confirmed"])
        self.assertEqual(ncsoft.score_price_alignment, "price_moved_without_evidence")

        self.assertEqual(lgcns.primary_archetype, E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE)
        self.assertEqual(lgcns.extra_price_metrics["cloud_ai_sales_share_9m2024_pct"], 54.0)
        self.assertEqual(lgcns.extra_price_metrics["debut_mae_vs_ipo_pct"], -3.23)
        self.assertEqual(lgcns.score_price_alignment, "evidence_good_but_price_failed")

        self.assertEqual(douzone.primary_archetype, E2RArchetype.ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2)
        self.assertEqual(douzone.extra_price_metrics["eqt_investment_usd_mn"], 930.0)
        self.assertFalse(douzone.extra_price_metrics["arr_retention_confirmed"])

        self.assertEqual(skt.primary_archetype, E2RArchetype.CYBERSECURITY_TRUST_HARD_4C_REFERENCE)
        self.assertTrue(skt.hard_4c_confirmed)
        self.assertEqual(skt.event_mae_pct, -8.5)
        self.assertEqual(skt.extra_price_metrics["pipc_fine_krw_bn"], 134.0)
        self.assertEqual(skt.rerating_result, "thesis_break")

    def test_green_gate_4b_4c_shadow_and_deep_rows_are_explicit(self) -> None:
        required = set(ROUND290_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND290_GREEN_FORBIDDEN_PATTERNS)
        fields = set(ROUND290_PRICE_VALIDATION_FIELDS)
        shadow_rows = {row["archetype"]: row for row in round290_shadow_weight_rows()}
        deep_rows = round290_deep_sub_archetype_rows()
        green_markdown = render_round290_green_gate_review_markdown()
        stage_markdown = render_round290_stage4b_4c_review_markdown()

        self.assertIn("paid_conversion_arpu_confirmed", required)
        self.assertIn("data_trust_internal_control_confirmed", required)
        self.assertIn("MAU_headline_only", forbidden)
        self.assertIn("PE_control_premium_without_ARR", forbidden)
        self.assertIn("platform_MAU_before_paid_conversion", ROUND290_STAGE4B_WATCH_TRIGGERS)
        self.assertIn("major_data_breach_or_customer_trust_break", ROUND290_HARD_4C_GATES)
        self.assertIn("data_breach_cost_anchor", fields)
        self.assertIn("Do not apply these weights to production scoring yet.", green_markdown)
        self.assertIn("SK Telecom", stage_markdown)
        self.assertIn("hard 4C", stage_markdown)
        self.assertEqual(len(ROUND290_SHADOW_WEIGHT_ROWS), 8)
        self.assertEqual(shadow_rows["WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE"]["event_penalty"], "-5")
        self.assertEqual(shadow_rows["CYBERSECURITY_TRUST_HARD_4C_REFERENCE"]["hard_4c_sensitivity"], "+5")
        self.assertTrue(any("Webtoon" in row["terms"] for row in deep_rows))
        self.assertTrue(any("SK Telecom" in row["terms"] for row in deep_rows))

    def test_summary_audit_cli_and_writer_outputs(self) -> None:
        audit = round290_audit_payload()
        self.assertEqual(audit["source_round"], "docs/round/round_290.md")
        self.assertEqual(audit["round_id"], "round_218")
        self.assertEqual(audit["large_sector"], ROUND290_LARGE_SECTOR)
        self.assertFalse(audit["summary"]["production_scoring_changed"])
        self.assertFalse(audit["summary"]["candidate_generation_input"])
        self.assertTrue(audit["summary"]["shadow_weight_only"])
        self.assertTrue(audit["summary"]["direct_KRX_hard_4c_confirmed"])
        self.assertIn("do_not_use_round290_cases_as_candidate_generation_input", audit["what_not_to_change"])

        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])
        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            paths = write_round290_r8_loop14_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)

            records = load_case_library(paths["cases"])
            rows = round290_case_rows()
            self.assertEqual(len(records), len(ROUND290_CASE_CANDIDATES))
            self.assertEqual(len(rows), len(ROUND290_CASE_CANDIDATES))
            self.assertIn("Webtoon", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("paid_conversion_arpu_confirmed", paths["green_gate_review"].read_text(encoding="utf-8"))
            self.assertIn("CYBERSECURITY_TRUST_HARD_4C_REFERENCE", paths["shadow_weights"].read_text(encoding="utf-8"))
            self.assertIn("data_breach_cost_anchor", paths["price_validation_plan"].read_text(encoding="utf-8"))
            self.assertEqual(json.loads(rows[0]["extra_price_metrics"])["monthly_active_users_mn"], 170.0)


if __name__ == "__main__":
    unittest.main()
