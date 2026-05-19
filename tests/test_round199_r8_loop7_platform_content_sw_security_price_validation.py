import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round199_r8_loop7_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round199_r8_loop7_platform_content_sw_security_price_validation import (
    ROUND199_CASE_CANDIDATES,
    ROUND199_GREEN_FORBIDDEN_PATTERNS,
    ROUND199_GREEN_REQUIRED_FIELDS,
    ROUND199_HARD_4C_GATES,
    ROUND199_PRICE_BACKFILL_FIELDS,
    ROUND199_REQUIRED_TARGET_ALIASES,
    render_round199_green_gate_review_markdown,
    render_round199_stage4b_4c_review_markdown,
    round199_audit_payload,
    round199_case_records,
    round199_case_rows,
    round199_price_backfill_field_rows,
    round199_score_adjustment_rows,
    round199_summary,
    write_round199_r8_loop7_reports,
)


class Round199R8Loop7PlatformContentSwSecurityPriceValidationTests(unittest.TestCase):
    def test_round199_targets_are_existing_canonical_archetypes(self):
        self.assertGreaterEqual(len(ROUND199_REQUIRED_TARGET_ALIASES), 20)
        self.assertEqual(
            ROUND199_REQUIRED_TARGET_ALIASES["B2B_SAAS_ERP_WORKFLOW"],
            E2RArchetype.B2B_SAAS_ERP_WORKFLOW.value,
        )
        self.assertEqual(
            ROUND199_REQUIRED_TARGET_ALIASES["SOVEREIGN_KOREAN_AI_MODEL"],
            E2RArchetype.SOVEREIGN_KOREAN_AI_MODEL.value,
        )
        self.assertEqual(
            ROUND199_REQUIRED_TARGET_ALIASES["PLATFORM_GOVERNANCE_LEGAL_RISK"],
            E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK.value,
        )
        for canonical in ROUND199_REQUIRED_TARGET_ALIASES.values():
            self.assertIsInstance(E2RArchetype(canonical), E2RArchetype)

    def test_case_records_validate_and_remain_shadow_only(self):
        records = {record.case_id: record for record in round199_case_records()}

        self.assertEqual(len(records), 7)
        self.assertEqual(records["douzone_bizon_eqt_cloud_erp_stage2_watch"].case_type, "success_candidate")
        self.assertEqual(records["samsung_sds_kkr_ai_cloud_cb_4b_watch"].case_type, "success_candidate")
        self.assertEqual(records["kakao_openai_partnership_governance_legal_event_watch"].case_type, "failed_rerating")
        self.assertEqual(records["shiftup_stellar_blade_ipo_single_ip_overheat_watch"].case_type, "overheat")
        self.assertEqual(records["hybe_newjeans_bang_legal_governance_4c_watch"].case_type, "failed_rerating")
        for record in records.values():
            self.assertIn("production_scoring_changed_false", record.green_guardrails)
            self.assertIn("candidate_generation_input_false", record.green_guardrails)
            self.assertIn("shadow_weight_only_true", record.green_guardrails)
            self.assertEqual(record.price_validation.price_validation_status, "needs_ohlc_backfill")

    def test_b2b_saas_ai_cloud_and_naver_are_stage2_not_forced_green(self):
        rows = {row["case_id"]: row for row in round199_case_rows()}
        douzone = rows["douzone_bizon_eqt_cloud_erp_stage2_watch"]
        sds = rows["samsung_sds_kkr_ai_cloud_cb_4b_watch"]
        naver = rows["naver_webtoon_hyperclova_platform_ai_ip_stage2_watch"]

        self.assertEqual(douzone["stage2_date"], "2025-11-07")
        self.assertEqual(douzone["stage3_date"], "")
        self.assertIn("arr_unverified", douzone["red_flag_fields"])
        self.assertEqual(sds["stage2_date"], "2026-04-15")
        self.assertEqual(sds["stage4b_date"], "2026-04-15")
        self.assertEqual(sds["score_price_alignment"], "price_moved_without_evidence")
        self.assertIn("cb_dilution_watch", sds["red_flag_fields"])
        self.assertEqual(naver["stage2_date"], "2024-06-17")
        self.assertEqual(naver["stage3_date"], "")
        self.assertIn("mau_without_arpu", naver["red_flag_fields"])

    def test_partnership_game_ipo_and_governance_cases_block_green(self):
        rows = {row["case_id"]: row for row in round199_case_rows()}
        kakao = rows["kakao_openai_partnership_governance_legal_event_watch"]
        krafton = rows["krafton_inzoi_adk_ai_first_game_ip_stage2_watch"]
        shiftup = rows["shiftup_stellar_blade_ipo_single_ip_overheat_watch"]
        hybe = rows["hybe_newjeans_bang_legal_governance_4c_watch"]

        self.assertEqual(kakao["stage1_date"], "2025-02-04")
        self.assertEqual(kakao["stage2_date"], "")
        self.assertEqual(kakao["stage4b_date"], "2025-02-04")
        self.assertIn("partnership_headline_only", kakao["red_flag_fields"])
        self.assertEqual(krafton["stage2_date"], "2025-04-01")
        self.assertIn("game_launch_first_week_only", krafton["red_flag_fields"])
        self.assertEqual(shiftup["case_type"], "overheat")
        self.assertEqual(shiftup["stage4b_date"], "2024-07-11")
        self.assertIn("single_ip_dependence", shiftup["red_flag_fields"])
        self.assertEqual(hybe["stage4c_date"], "2025-03-21")
        self.assertEqual(hybe["hard_4c_confirmed"], "false")
        self.assertIn("founder_legal_risk", hybe["red_flag_fields"])

    def test_green_gate_requires_repeat_economics_and_blocks_event_only_patterns(self):
        required = set(ROUND199_GREEN_REQUIRED_FIELDS)
        forbidden = set(ROUND199_GREEN_FORBIDDEN_PATTERNS)
        adjustments = {row["axis"]: row for row in round199_score_adjustment_rows()}
        markdown = render_round199_green_gate_review_markdown()

        self.assertIn("recurring_revenue_or_bookings_confirmed", required)
        self.assertIn("arr_arpu_paid_usage_or_billings_confirmed", required)
        self.assertIn("fcf_conversion_visible", required)
        self.assertIn("privacy_security_governance_trust_passed", required)
        self.assertIn("ai_feature_only", forbidden)
        self.assertIn("partnership_headline_only", forbidden)
        self.assertIn("game_launch_first_week_only", forbidden)
        self.assertIn("ipo_first_month_rally", forbidden)
        self.assertEqual(adjustments["recurring_revenue"]["points"], "5")
        self.assertEqual(adjustments["ai_feature_only"]["points"], "-5")
        self.assertEqual(adjustments["founder_legal_risk"]["points"], "-5")
        self.assertIn("Do not apply these weights to production scoring yet", markdown)

    def test_price_backfill_fields_include_r8_repeat_revenue_and_trust_inputs(self):
        fields = {row["field"] for row in round199_price_backfill_field_rows()}

        self.assertGreaterEqual(len(ROUND199_PRICE_BACKFILL_FIELDS), 50)
        for field in (
            "arr_proxy",
            "billings",
            "bookings",
            "paid_usage",
            "arpu",
            "retention_rate",
            "churn_rate",
            "opm",
            "fcf_conversion",
            "ai_revenue_conversion",
            "founder_legal_risk_flag",
            "privacy_security_incident_flag",
            "hard_4c_confirmed",
        ):
            self.assertIn(field, fields)

    def test_stage4b_4c_review_contains_platform_trust_hard_gates(self):
        review = render_round199_stage4b_4c_review_markdown()

        self.assertIn("privacy_breach", ROUND199_HARD_4C_GATES)
        self.assertIn("security_outage", ROUND199_HARD_4C_GATES)
        self.assertIn("founder_or_major_shareholder_legal_break", ROUND199_HARD_4C_GATES)
        self.assertIn("game_launch_failure", ROUND199_HARD_4C_GATES)
        self.assertIn("privacy/security/founder legal risk can block Green", review)
        self.assertIn("hybe_newjeans_bang_legal_governance_4c_watch", review)

    def test_summary_and_audit_payload_are_calibration_only(self):
        summary = round199_summary()
        payload = round199_audit_payload()

        self.assertEqual(summary["case_candidate_count"], len(ROUND199_CASE_CANDIDATES))
        self.assertEqual(summary["stage3_case_count"], 0)
        self.assertEqual(summary["hard_4c_case_count"], 0)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertFalse(summary["candidate_generation_input"])
        self.assertTrue(summary["shadow_weight_only"])
        self.assertIn("do_not_use_round199_cases_as_candidate_generation_input", payload["what_not_to_change"])
        self.assertIn("do_not_treat_ai_partnership_model_release_mau_game_launch_ipo_or_mna_as_green_evidence", payload["what_not_to_change"])

    def test_cli_parser_and_writer_outputs(self):
        parser = build_parser()
        args = parser.parse_args(["--output-directory", "out", "--cases", "cases.jsonl", "--audit", "audit.json"])

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.audit, "audit.json")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = write_round199_r8_loop7_reports(
                output_directory=root / "out",
                cases_path=root / "cases.jsonl",
                audit_path=root / "audit.json",
            )
            for path in paths.values():
                self.assertTrue(path.exists(), path)
            records = load_case_library(root / "cases.jsonl")
            self.assertEqual(len(records), 7)
            self.assertIn("Stage 3-Green", paths["summary"].read_text(encoding="utf-8"))
            self.assertIn("recurring_revenue", paths["score_adjustments"].read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
