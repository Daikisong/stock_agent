import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round74_r8_loop3_report import build_parser
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round74_r8_loop3_platform_content_sw_security import (
    ROUND74_CASE_CANDIDATES,
    ROUND74_PRICE_FIELDS,
    ROUND74_SCORE_TARGETS,
    render_round74_green_guardrail_markdown,
    render_round74_price_validation_plan_markdown,
    render_round74_risk_overlay_markdown,
    render_round74_summary_markdown,
    round74_case_candidate_rows,
    round74_case_records,
    round74_price_field_rows,
    round74_score_profile_rows,
    round74_stage_date_rows,
    round74_summary,
    target_for,
    write_round74_r8_loop3_reports,
)


class Round74R8Loop3PlatformContentSwSecurityTests(unittest.TestCase):
    def test_round74_targets_cover_r8_loop3_archetypes(self):
        labels = {target.target_id for target in ROUND74_SCORE_TARGETS}

        self.assertEqual(len(labels), 17)
        for label in (
            "PLATFORM_SOFTWARE_INTERNET",
            "B2B_SAAS_ERP_WORKFLOW",
            "CLOUD_AI_SOFTWARE_INFRA",
            "AI_SOFTWARE_APPLICATION",
            "OBSERVABILITY_AI_OPERATIONS",
            "CONTACT_CENTER_AI_AUTOMATION",
            "GAME_CONTENT_IP",
            "UGC_GAME_PLATFORM_SAFETY",
            "MEDIA_AD_CONTENT_CYCLE",
            "ADTECH_PLATFORM_PREMIUM",
            "STREAMING_AD_PLATFORM",
            "SECURITY_IDENTITY_DEEPFAKE",
            "SECURITY_OPERATIONAL_TRUST_OVERLAY",
            "PLATFORM_GOVERNANCE_LEGAL_RISK",
            "PLATFORM_AD_TRUST_OVERLAY",
            "GENERATIVE_AI_IP_RISK",
            "METAVERSE_NFT_THEME",
        ):
            self.assertIn(label, labels)
        for target in ROUND74_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY)
            self.assertFalse(target.production_scoring_changed)

    def test_green_possible_targets_are_repeat_revenue_guardrailed(self):
        b2b = target_for("B2B_SAAS_ERP_WORKFLOW")
        cloud = target_for("CLOUD_AI_SOFTWARE_INFRA")

        assert b2b is not None
        assert cloud is not None
        self.assertEqual(b2b.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("arr_growth", b2b.green_conditions)
        self.assertIn("low_churn", b2b.green_conditions)
        self.assertIn("churn", b2b.red_flags)
        self.assertEqual(cloud.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("paid_ai_contract", cloud.green_conditions)
        self.assertIn("ai_cost", cloud.loop3_penalty_axes)

    def test_ai_game_and_ugc_themes_are_not_green_by_default(self):
        ai = target_for("AI_SOFTWARE_APPLICATION")
        game = target_for("GAME_CONTENT_IP")
        ugc = target_for("UGC_GAME_PLATFORM_SAFETY")
        nft = target_for("METAVERSE_NFT_THEME")

        for target in (ai, game, ugc):
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        assert nft is not None
        self.assertEqual(nft.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("paid_usage", ai.green_conditions)
        self.assertIn("booking_deferral", game.stage4c_conditions)
        self.assertIn("child_safety", ugc.red_flags)
        self.assertIn("revenue_absent", nft.red_flags)

    def test_overlay_targets_are_gate_only(self):
        for target_id in (
            "GENERATIVE_AI_IP_RISK",
            "SECURITY_OPERATIONAL_TRUST_OVERLAY",
            "PLATFORM_GOVERNANCE_LEGAL_RISK",
            "PLATFORM_AD_TRUST_OVERLAY",
        ):
            target = target_for(target_id)
            assert target is not None
            self.assertTrue(target.gate_only)
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
            self.assertEqual(target.score_weight.eps_fcf, "gate")

        trust = target_for("SECURITY_OPERATIONAL_TRUST_OVERLAY")
        ad_trust = target_for("PLATFORM_AD_TRUST_OVERLAY")
        assert trust is not None
        assert ad_trust is not None
        self.assertIn("global_outage", trust.stage4c_conditions)
        self.assertIn("scam_ads", ad_trust.red_flags)

    def test_required_round74_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round74_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND74_CASE_CANDIDATES))
        self.assertEqual(rows["douzone_bizon_eqt_cloud_erp_case"]["target_id"], "B2B_SAAS_ERP_WORKFLOW")
        self.assertEqual(rows["douzone_bizon_eqt_cloud_erp_case"]["stage2_date"], "2025-11-07")
        self.assertEqual(rows["palantir_q4_2025_ai_revenue_case"]["target_id"], "CLOUD_AI_SOFTWARE_INFRA")
        self.assertEqual(rows["palantir_q4_2025_ai_revenue_case"]["stage2_date"], "2026-02-03")
        self.assertEqual(rows["palantir_q1_2026_fastest_growth_case"]["stage4b_date"], "2026-05-05")
        self.assertEqual(rows["datadog_q1_2026_ai_observability_case"]["stage2_date"], "2026-05-07")
        self.assertEqual(rows["fortinet_q1_2026_security_billings_case"]["stage2_date"], "2026-05-07")
        self.assertEqual(rows["netflix_ad_tier_250m_case"]["stage2_date"], "2026-05-13")
        self.assertEqual(rows["trade_desk_revenue_miss_case"]["target_id"], "ADTECH_PLATFORM_PREMIUM")
        self.assertEqual(rows["trade_desk_revenue_miss_case"]["stage4c_date"], "2025-02-13")
        self.assertEqual(rows["crowdstrike_outage_shareholder_case"]["target_id"], "SECURITY_OPERATIONAL_TRUST_OVERLAY")
        self.assertEqual(rows["crowdstrike_outage_shareholder_case"]["stage4c_date"], "2024-07-31")
        self.assertEqual(rows["delta_crowdstrike_lawsuit_case"]["stage4c_date"], "2024-10-25")
        self.assertEqual(rows["kakao_founder_legal_overhang_case"]["stage4b_date"], "2025-10-21")
        self.assertEqual(rows["roblox_safety_forecast_cut_case"]["target_id"], "UGC_GAME_PLATFORM_SAFETY")
        self.assertEqual(rows["roblox_safety_forecast_cut_case"]["stage4c_date"], "2026-05-01")
        self.assertEqual(rows["take_two_gta_delay_case"]["stage4b_date"], "2025-05-02")
        self.assertEqual(rows["take_two_gta_preorder_rumor_case"]["case_type"], "event_premium")
        self.assertEqual(rows["take_two_gta_preorder_rumor_case"]["stage4b_date"], "2026-05-14")
        self.assertEqual(rows["wpp_ad_forecast_cut_case"]["stage4b_date"], "2025-06-09")
        self.assertEqual(rows["wpp_profit_drop_ai_disruption_case"]["stage4c_date"], "2025-08-07")
        self.assertEqual(rows["netflix_texas_privacy_lawsuit_case"]["stage4b_date"], "2026-05-11")
        self.assertEqual(rows["meta_scam_ads_lawsuit_case"]["stage4c_date"], "2026-05-11")
        self.assertEqual(rows["meta_youth_safety_trial_case"]["stage4b_date"], "2026-05-13")

    def test_case_records_validate_and_keep_round74_guardrails(self):
        records = round74_case_records()

        self.assertEqual(len(records), len(ROUND74_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("user_count_is_not_green_evidence_alone", record.green_guardrails)
            self.assertIn("ai_feature_is_not_revenue", record.green_guardrails)
            self.assertIn("new_title_expectation_is_not_bookings", record.green_guardrails)
            self.assertIn("security_demand_is_not_operational_trust", record.green_guardrails)
            self.assertIn("ad_revenue_must_pass_quality_filter", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["palantir_q4_2025_ai_revenue_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["crowdstrike_outage_shareholder_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["roblox_safety_forecast_cut_case"].score_price_alignment, "false_positive_score")
        self.assertEqual(by_id["take_two_gta_preorder_rumor_case"].rerating_result, "event_premium")

    def test_score_profile_rows_match_round74_weight_table(self):
        rows = {row["target_id"]: row for row in round74_score_profile_rows()}

        self.assertEqual(rows["PLATFORM_SOFTWARE_INTERNET"]["eps_fcf"], "18")
        self.assertEqual(rows["B2B_SAAS_ERP_WORKFLOW"]["structural_visibility"], "23")
        self.assertEqual(rows["CLOUD_AI_SOFTWARE_INFRA"]["eps_fcf"], "22")
        self.assertEqual(rows["OBSERVABILITY_AI_OPERATIONS"]["structural_visibility"], "22")
        self.assertEqual(rows["UGC_GAME_PLATFORM_SAFETY"]["valuation"], "9")
        self.assertEqual(rows["ADTECH_PLATFORM_PREMIUM"]["market_mispricing"], "14")
        self.assertEqual(rows["SECURITY_OPERATIONAL_TRUST_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["PLATFORM_AD_TRUST_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["METAVERSE_NFT_THEME"]["information_confidence"], "3")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round74_stage_date_rows()}
        fields = {row["field"] for row in round74_price_field_rows()}

        self.assertIn("arr_growth", rows["B2B_SAAS_ERP_WORKFLOW"]["stage2"])
        self.assertIn("paid_ai_contract", rows["CLOUD_AI_SOFTWARE_INFRA"]["stage2"])
        self.assertIn("ai_monitoring_customer_growth", rows["OBSERVABILITY_AI_OPERATIONS"]["stage2"])
        self.assertIn("bookings_guide_cut", rows["UGC_GAME_PLATFORM_SAFETY"]["stage4c"])
        self.assertIn("revenue_miss", rows["ADTECH_PLATFORM_PREMIUM"]["stage4c"])
        self.assertIn("global_outage", rows["SECURITY_OPERATIONAL_TRUST_OVERLAY"]["stage4c"])
        self.assertIn("consumer_protection_lawsuit", rows["PLATFORM_AD_TRUST_OVERLAY"]["stage4c"])
        for field in (
            "stage2_price",
            "below_stage2_price_flag",
            "arr_growth",
            "net_retention_rate",
            "ai_revenue_contribution",
            "total_contract_value",
            "revenue_per_employee",
            "observability_revenue",
            "ai_workload_customer_count",
            "cloud_optimization_risk_flag",
            "bookings_growth",
            "communication_engagement_change",
            "preorder_event_flag",
            "ad_tier_users",
            "dark_pattern_allegation_flag",
            "security_billings_growth",
            "security_arr_growth",
            "affected_device_count",
            "customer_lawsuit_flag",
            "founder_legal_case_flag",
            "youth_safety_lawsuit_flag",
            "copyright_lawsuit_flag",
            "generative_ai_ip_risk_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND74_PRICE_FIELDS))

    def test_summary_and_markdown_explain_r8_loop3_guardrails(self):
        summary = round74_summary()
        summary_md = render_round74_summary_markdown()
        guardrails = render_round74_green_guardrail_markdown()
        overlays = render_round74_risk_overlay_markdown()
        price_plan = render_round74_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 17)
        self.assertEqual(summary["case_candidate_count"], 18)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 4)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["stage4b_case_count"], 7)
        self.assertEqual(summary["stage4c_case_count"], 6)
        self.assertEqual(summary["green_possible_count"], 2)
        self.assertEqual(summary["watch_yellow_first_count"], 10)
        self.assertEqual(summary["redteam_first_count"], 5)
        self.assertEqual(summary["gate_only_target_count"], 4)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("Round 74", summary_md)
        self.assertIn("Do not apply R8 Loop-3 v3.0 weights", guardrails)
        self.assertIn("SECURITY_TRUST_BREAK", overlays)
        self.assertIn("crowdstrike_outage_shareholder_case", price_plan)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round74_r8_loop3_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r8_loop3_round74.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round74_r8_loop3_v3.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND74_CASE_CANDIDATES))

    def test_cli_argument_parser_supports_paths(self):
        args = build_parser().parse_args(
            [
                "--output-directory",
                "out",
                "--cases",
                "cases.jsonl",
                "--score-profiles",
                "scores.csv",
            ]
        )

        self.assertEqual(args.output_directory, "out")
        self.assertEqual(args.cases, "cases.jsonl")
        self.assertEqual(args.score_profiles, "scores.csv")

    def test_production_scoring_modules_do_not_import_round74_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round74_r8_loop3_platform_content_sw_security", text)


if __name__ == "__main__":
    unittest.main()
