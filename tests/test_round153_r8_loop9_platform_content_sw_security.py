import tempfile
from pathlib import Path
import unittest

from e2r.cli.build_round153_r8_loop9_report import build_parser
from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import load_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture
from e2r.sector.round153_r8_loop9_platform_content_sw_security import (
    ROUND153_CASE_CANDIDATES,
    ROUND153_PRICE_FIELDS,
    ROUND153_SCORE_TARGETS,
    render_round153_green_guardrail_markdown,
    render_round153_price_validation_plan_markdown,
    render_round153_risk_overlay_markdown,
    render_round153_summary_markdown,
    round153_base_score_axis_rows,
    round153_case_candidate_rows,
    round153_case_records,
    round153_price_field_rows,
    round153_score_profile_rows,
    round153_stage_date_rows,
    round153_summary,
    round153_target_for,
    write_round153_r8_loop9_reports,
)


class Round153R8Loop9PlatformContentSwSecurityTests(unittest.TestCase):
    def test_round153_targets_cover_r8_loop9_archetypes(self):
        labels = {target.target_id for target in ROUND153_SCORE_TARGETS}

        self.assertEqual(len(labels), 28)
        for label in (
            "PLATFORM_SOFTWARE_INTERNET",
            "B2B_SAAS_ERP_WORKFLOW",
            "ENTERPRISE_AI_ONTOLOGY_WORKFLOW",
            "GOVERNMENT_AI_PROGRAM_OF_RECORD",
            "CLOUD_AI_SOFTWARE_INFRA",
            "EDGE_AI_CLOUD_INFRASTRUCTURE",
            "AI_SOFTWARE_APPLICATION",
            "LEGACY_SAAS_AI_REINFORCEMENT",
            "LEGACY_SAAS_AI_DISRUPTION_OVERLAY",
            "OBSERVABILITY_AI_OPERATIONS",
            "OBSERVABILITY_GUIDANCE_RISK",
            "CONTACT_CENTER_AI_AUTOMATION",
            "GAME_CONTENT_IP",
            "SINGLE_IP_RELEASE_EVENT_PREMIUM",
            "UGC_GAME_PLATFORM_SAFETY",
            "MEDIA_AD_CONTENT_CYCLE",
            "ADTECH_PLATFORM_PREMIUM",
            "STREAMING_AD_PLATFORM",
            "CYBERSECURITY_AI_THREAT_DEMAND",
            "AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER",
            "SECURITY_IDENTITY_DEEPFAKE",
            "SECURITY_OPERATIONAL_TRUST_OVERLAY",
            "PLATFORM_GOVERNANCE_LEGAL_RISK",
            "PLATFORM_AD_TRUST_OVERLAY",
            "PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY",
            "GENERATIVE_AI_IP_RISK",
            "METAVERSE_NFT_THEME",
            "DISCLOSURE_CONFIDENCE_CAP",
        ):
            self.assertIn(label, labels)
        for target in ROUND153_SCORE_TARGETS:
            self.assertEqual(target.large_sector, Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY)
            self.assertFalse(target.production_scoring_changed)
        self.assertEqual(E2RArchetype.EDGE_AI_CLOUD_INFRASTRUCTURE.value, "EDGE_AI_CLOUD_INFRASTRUCTURE")
        self.assertEqual(E2RArchetype.ENTERPRISE_AI_ONTOLOGY_WORKFLOW.value, "ENTERPRISE_AI_ONTOLOGY_WORKFLOW")
        self.assertEqual(E2RArchetype.GOVERNMENT_AI_PROGRAM_OF_RECORD.value, "GOVERNMENT_AI_PROGRAM_OF_RECORD")
        self.assertEqual(E2RArchetype.LEGACY_SAAS_AI_REINFORCEMENT.value, "LEGACY_SAAS_AI_REINFORCEMENT")
        self.assertEqual(E2RArchetype.LEGACY_SAAS_AI_DISRUPTION_OVERLAY.value, "LEGACY_SAAS_AI_DISRUPTION_OVERLAY")
        self.assertEqual(E2RArchetype.OBSERVABILITY_GUIDANCE_RISK.value, "OBSERVABILITY_GUIDANCE_RISK")
        self.assertEqual(E2RArchetype.CYBERSECURITY_AI_THREAT_DEMAND.value, "CYBERSECURITY_AI_THREAT_DEMAND")
        self.assertEqual(E2RArchetype.AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER.value, "AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER")
        self.assertEqual(E2RArchetype.SINGLE_IP_RELEASE_EVENT_PREMIUM.value, "SINGLE_IP_RELEASE_EVENT_PREMIUM")
        self.assertEqual(E2RArchetype.PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY.value, "PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY")
        self.assertEqual(E2RArchetype.DISCLOSURE_CONFIDENCE_CAP.value, "DISCLOSURE_CONFIDENCE_CAP")

    def test_green_possible_targets_are_repeat_revenue_guardrailed(self):
        b2b = round153_target_for("B2B_SAAS_ERP_WORKFLOW")
        enterprise = round153_target_for("ENTERPRISE_AI_ONTOLOGY_WORKFLOW")
        government = round153_target_for("GOVERNMENT_AI_PROGRAM_OF_RECORD")
        cloud = round153_target_for("CLOUD_AI_SOFTWARE_INFRA")
        edge = round153_target_for("EDGE_AI_CLOUD_INFRASTRUCTURE")
        legacy_reinforcement = round153_target_for("LEGACY_SAAS_AI_REINFORCEMENT")
        cyber = round153_target_for("CYBERSECURITY_AI_THREAT_DEMAND")
        ai_networking = round153_target_for("AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER")

        assert b2b is not None
        assert enterprise is not None
        assert government is not None
        assert cloud is not None
        assert edge is not None
        assert legacy_reinforcement is not None
        assert cyber is not None
        assert ai_networking is not None
        self.assertEqual(b2b.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("arr_growth", b2b.green_conditions)
        self.assertIn("low_churn", b2b.green_conditions)
        self.assertIn("churn", b2b.red_flags)
        self.assertEqual(enterprise.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("auditable_workflow", enterprise.green_conditions)
        self.assertIn("workflow_lock_in", enterprise.stage3_conditions)
        self.assertEqual(cloud.posture, Round10ThemePosture.GREEN_POSSIBLE)
        self.assertIn("paid_ai_contract", cloud.green_conditions)
        self.assertIn("ai_cost", cloud.loop9_penalty_axes)
        self.assertEqual(edge.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("long_term_ai_cloud_contract", edge.green_conditions)
        self.assertIn("capex", edge.loop9_penalty_axes)
        self.assertEqual(government.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("program_of_record", government.green_conditions)
        self.assertIn("government_program_budget", government.green_conditions)
        self.assertEqual(legacy_reinforcement.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("ai_arr", legacy_reinforcement.green_conditions)
        self.assertIn("license_downsell", legacy_reinforcement.red_flags)
        self.assertEqual(cyber.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("billings_growth", cyber.stage2_signals)
        self.assertIn("outage", cyber.red_flags)
        self.assertEqual(ai_networking.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        self.assertIn("software_security_mix", ai_networking.green_conditions)
        self.assertIn("restructuring_cost", ai_networking.red_flags)

    def test_ai_game_and_ugc_themes_are_not_green_by_default(self):
        ai = round153_target_for("AI_SOFTWARE_APPLICATION")
        game = round153_target_for("GAME_CONTENT_IP")
        single_ip = round153_target_for("SINGLE_IP_RELEASE_EVENT_PREMIUM")
        ugc = round153_target_for("UGC_GAME_PLATFORM_SAFETY")
        nft = round153_target_for("METAVERSE_NFT_THEME")

        for target in (ai, game, single_ip, ugc):
            assert target is not None
            self.assertEqual(target.posture, Round10ThemePosture.WATCH_YELLOW_FIRST)
        assert nft is not None
        self.assertEqual(nft.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertIn("paid_usage", ai.green_conditions)
        self.assertIn("booking_deferral", game.stage4c_conditions)
        assert single_ip is not None
        self.assertIn("preorder_actual", single_ip.stage2_signals)
        self.assertIn("preorder_rumor", single_ip.red_flags)
        self.assertIn("child_safety", ugc.red_flags)
        self.assertIn("revenue_absent", nft.red_flags)

    def test_overlay_targets_are_gate_only(self):
        for target_id in (
            "GENERATIVE_AI_IP_RISK",
            "LEGACY_SAAS_AI_DISRUPTION_OVERLAY",
            "OBSERVABILITY_GUIDANCE_RISK",
            "SECURITY_OPERATIONAL_TRUST_OVERLAY",
            "PLATFORM_GOVERNANCE_LEGAL_RISK",
            "PLATFORM_AD_TRUST_OVERLAY",
            "PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY",
        ):
            target = round153_target_for(target_id)
            assert target is not None
            self.assertTrue(target.gate_only)
            self.assertEqual(target.posture, Round10ThemePosture.REDTEAM_FIRST)
            self.assertEqual(target.score_weight.eps_fcf, "gate")

        trust = round153_target_for("SECURITY_OPERATIONAL_TRUST_OVERLAY")
        ad_trust = round153_target_for("PLATFORM_AD_TRUST_OVERLAY")
        privacy = round153_target_for("PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY")
        observability_risk = round153_target_for("OBSERVABILITY_GUIDANCE_RISK")
        legacy = round153_target_for("LEGACY_SAAS_AI_DISRUPTION_OVERLAY")
        assert trust is not None
        assert ad_trust is not None
        assert privacy is not None
        assert observability_risk is not None
        assert legacy is not None
        self.assertIn("global_outage", trust.stage4c_conditions)
        self.assertIn("scam_ads", ad_trust.red_flags)
        self.assertIn("privacy_lawsuit", privacy.red_flags)
        self.assertIn("guidance_miss", observability_risk.red_flags)
        self.assertIn("license_downsell", legacy.red_flags)

    def test_disclosure_confidence_cap_is_cap_only(self):
        cap = round153_target_for("DISCLOSURE_CONFIDENCE_CAP")

        assert cap is not None
        self.assertEqual(cap.posture, Round10ThemePosture.REDTEAM_FIRST)
        self.assertFalse(cap.gate_only)
        self.assertEqual(cap.score_weight.eps_fcf, "cap")
        self.assertEqual(cap.score_weight.information_confidence, "+")
        self.assertIn("disclosure_confidence_low", cap.red_flags)

    def test_required_round153_cases_are_present_with_stage_dates(self):
        rows = {row["case_id"]: row for row in round153_case_candidate_rows()}

        self.assertEqual(len(rows), len(ROUND153_CASE_CANDIDATES))
        self.assertEqual(rows["douzone_bizon_eqt_cloud_erp_case"]["target_id"], "B2B_SAAS_ERP_WORKFLOW")
        self.assertEqual(rows["douzone_bizon_eqt_cloud_erp_case"]["stage2_date"], "2025-11-07")
        self.assertEqual(rows["palantir_q4_2025_ai_revenue_case"]["target_id"], "GOVERNMENT_AI_PROGRAM_OF_RECORD")
        self.assertEqual(rows["palantir_q4_2025_ai_revenue_case"]["stage2_date"], "2026-02-03")
        self.assertEqual(rows["palantir_q1_2026_fastest_growth_case"]["target_id"], "ENTERPRISE_AI_ONTOLOGY_WORKFLOW")
        self.assertEqual(rows["palantir_q1_2026_fastest_growth_case"]["stage4b_date"], "2026-05-04")
        self.assertEqual(rows["akamai_frontier_model_ai_cloud_deal_case"]["target_id"], "EDGE_AI_CLOUD_INFRASTRUCTURE")
        self.assertEqual(rows["akamai_frontier_model_ai_cloud_deal_case"]["stage2_date"], "2026-05-08")
        self.assertEqual(rows["akamai_frontier_model_ai_cloud_deal_case"]["stage4b_date"], "2026-05-08")
        self.assertEqual(rows["akamai_ai_cloud_revenue_contribution_case"]["target_id"], "EDGE_AI_CLOUD_INFRASTRUCTURE")
        self.assertEqual(rows["akamai_ai_cloud_revenue_contribution_case"]["stage2_date"], "2026-05-13")
        self.assertEqual(rows["akamai_ai_cloud_revenue_contribution_case"]["stage4b_date"], "2026-05-13")
        self.assertEqual(rows["datadog_q1_2026_ai_observability_case"]["stage2_date"], "2026-05-07")
        self.assertEqual(rows["dynatrace_q4_2026_arr_guidance_case"]["target_id"], "OBSERVABILITY_GUIDANCE_RISK")
        self.assertEqual(rows["dynatrace_q4_2026_arr_guidance_case"]["stage4c_date"], "2026-05-13")
        self.assertEqual(rows["fortinet_q1_2026_security_billings_case"]["target_id"], "CYBERSECURITY_AI_THREAT_DEMAND")
        self.assertEqual(rows["fortinet_q1_2026_security_billings_case"]["stage2_date"], "2026-05-07")
        self.assertEqual(rows["cisco_ai_infrastructure_orders_case"]["target_id"], "AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER")
        self.assertEqual(rows["cisco_ai_infrastructure_orders_case"]["stage2_date"], "2026-05-13")
        self.assertEqual(rows["netflix_ad_tier_250m_case"]["stage2_date"], "2026-05-13")
        self.assertEqual(rows["trade_desk_revenue_miss_case"]["target_id"], "ADTECH_PLATFORM_PREMIUM")
        self.assertEqual(rows["trade_desk_revenue_miss_case"]["stage4c_date"], "2025-02-13")
        self.assertEqual(rows["crowdstrike_outage_shareholder_case"]["target_id"], "SECURITY_OPERATIONAL_TRUST_OVERLAY")
        self.assertEqual(rows["crowdstrike_outage_shareholder_case"]["stage4c_date"], "2024-07-31")
        self.assertEqual(rows["kakao_founder_legal_overhang_case"]["stage4b_date"], "2025-10-21")
        self.assertEqual(rows["roblox_safety_forecast_cut_case"]["target_id"], "UGC_GAME_PLATFORM_SAFETY")
        self.assertEqual(rows["roblox_safety_forecast_cut_case"]["stage4c_date"], "2026-05-01")
        self.assertEqual(rows["take_two_gta_preorder_rumor_case"]["target_id"], "SINGLE_IP_RELEASE_EVENT_PREMIUM")
        self.assertEqual(rows["take_two_gta_preorder_rumor_case"]["case_type"], "event_premium")
        self.assertEqual(rows["take_two_gta_preorder_rumor_case"]["stage4b_date"], "2026-05-14")
        self.assertEqual(rows["wpp_ad_forecast_cut_case"]["stage4b_date"], "2025-06-09")
        self.assertNotIn("wpp_profit_drop_ai_disruption_case", rows)
        self.assertEqual(rows["netflix_texas_privacy_lawsuit_case"]["target_id"], "PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY")
        self.assertEqual(rows["netflix_texas_privacy_lawsuit_case"]["stage4b_date"], "2026-05-11")
        self.assertEqual(rows["meta_scam_ads_lawsuit_case"]["stage4c_date"], "2026-05-11")
        self.assertEqual(rows["meta_youth_safety_trial_case"]["target_id"], "PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY")
        self.assertEqual(rows["meta_youth_safety_trial_case"]["stage4b_date"], "2026-05-13")
        self.assertEqual(rows["legacy_saas_ai_disruption_case"]["target_id"], "LEGACY_SAAS_AI_DISRUPTION_OVERLAY")
        self.assertEqual(rows["legacy_saas_ai_disruption_case"]["stage4c_date"], "2026-05-14")
        self.assertEqual(rows["salesforce_agentforce_arr_case"]["target_id"], "LEGACY_SAAS_AI_REINFORCEMENT")
        self.assertEqual(rows["salesforce_agentforce_arr_case"]["stage2_date"], "2026-05-14")

    def test_case_records_validate_and_keep_round153_guardrails(self):
        records = round153_case_records()

        self.assertEqual(len(records), len(ROUND153_CASE_CANDIDATES))
        for record in records:
            record.validate()
            self.assertFalse(record.data_quality.price_data_available)
            self.assertIn("do_not_use_case_as_candidate_input", record.green_guardrails)
            self.assertIn("user_count_is_not_green_evidence_alone", record.green_guardrails)
            self.assertIn("ai_feature_is_not_revenue", record.green_guardrails)
            self.assertIn("new_title_expectation_is_not_bookings", record.green_guardrails)
            self.assertIn("security_demand_is_not_operational_trust", record.green_guardrails)
            self.assertIn("ad_revenue_must_pass_quality_filter", record.green_guardrails)
            self.assertIn("arr_arpu_bookings_opm_fcf_churn_and_legal_stability_required_for_green", record.green_guardrails)
        by_id = {record.case_id: record for record in records}
        self.assertEqual(by_id["palantir_q4_2025_ai_revenue_case"].score_price_alignment, "aligned")
        self.assertEqual(by_id["palantir_q4_2025_ai_revenue_case"].primary_archetype.value, "GOVERNMENT_AI_PROGRAM_OF_RECORD")
        self.assertIn(
            E2RArchetype.ENTERPRISE_AI_ONTOLOGY_WORKFLOW,
            by_id["palantir_q4_2025_ai_revenue_case"].secondary_archetypes,
        )
        self.assertEqual(by_id["crowdstrike_outage_shareholder_case"].rerating_result, "thesis_break")
        self.assertEqual(by_id["roblox_safety_forecast_cut_case"].score_price_alignment, "false_positive_score")
        self.assertEqual(by_id["take_two_gta_preorder_rumor_case"].rerating_result, "event_premium")
        self.assertEqual(by_id["take_two_gta_preorder_rumor_case"].primary_archetype.value, "SINGLE_IP_RELEASE_EVENT_PREMIUM")
        self.assertEqual(by_id["legacy_saas_ai_disruption_case"].primary_archetype.value, "LEGACY_SAAS_AI_DISRUPTION_OVERLAY")
        self.assertEqual(by_id["salesforce_agentforce_arr_case"].primary_archetype.value, "LEGACY_SAAS_AI_REINFORCEMENT")
        self.assertEqual(by_id["fortinet_q1_2026_security_billings_case"].primary_archetype.value, "CYBERSECURITY_AI_THREAT_DEMAND")
        self.assertEqual(by_id["cisco_ai_infrastructure_orders_case"].primary_archetype.value, "AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER")
        self.assertIn(
            E2RArchetype.AI_NETWORKING_SWITCHING_INFRA,
            by_id["cisco_ai_infrastructure_orders_case"].secondary_archetypes,
        )
        self.assertIn(
            E2RArchetype.CLOUD_AI_SOFTWARE_INFRA,
            by_id["cisco_ai_infrastructure_orders_case"].secondary_archetypes,
        )
        self.assertEqual(by_id["akamai_frontier_model_ai_cloud_deal_case"].primary_archetype.value, "EDGE_AI_CLOUD_INFRASTRUCTURE")
        self.assertEqual(by_id["dynatrace_q4_2026_arr_guidance_case"].primary_archetype.value, "OBSERVABILITY_GUIDANCE_RISK")

    def test_score_profile_rows_match_round153_weight_table(self):
        rows = {row["target_id"]: row for row in round153_score_profile_rows()}

        self.assertEqual(rows["PLATFORM_SOFTWARE_INTERNET"]["eps_fcf"], "18")
        self.assertEqual(rows["B2B_SAAS_ERP_WORKFLOW"]["structural_visibility"], "23")
        self.assertEqual(rows["ENTERPRISE_AI_ONTOLOGY_WORKFLOW"]["eps_fcf"], "23")
        self.assertEqual(rows["ENTERPRISE_AI_ONTOLOGY_WORKFLOW"]["information_confidence"], "6")
        self.assertEqual(rows["GOVERNMENT_AI_PROGRAM_OF_RECORD"]["structural_visibility"], "24")
        self.assertEqual(rows["GOVERNMENT_AI_PROGRAM_OF_RECORD"]["information_confidence"], "6")
        self.assertEqual(rows["CLOUD_AI_SOFTWARE_INFRA"]["eps_fcf"], "22")
        self.assertEqual(rows["CLOUD_AI_SOFTWARE_INFRA"]["valuation"], "10")
        self.assertEqual(rows["EDGE_AI_CLOUD_INFRASTRUCTURE"]["bottleneck_pricing"], "12")
        self.assertEqual(rows["EDGE_AI_CLOUD_INFRASTRUCTURE"]["valuation"], "9")
        self.assertEqual(rows["LEGACY_SAAS_AI_REINFORCEMENT"]["structural_visibility"], "21")
        self.assertEqual(rows["LEGACY_SAAS_AI_REINFORCEMENT"]["information_confidence"], "6")
        self.assertEqual(rows["LEGACY_SAAS_AI_DISRUPTION_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["OBSERVABILITY_AI_OPERATIONS"]["structural_visibility"], "22")
        self.assertEqual(rows["OBSERVABILITY_AI_OPERATIONS"]["valuation"], "10")
        self.assertEqual(rows["OBSERVABILITY_GUIDANCE_RISK"]["gate_only"], "true")
        self.assertEqual(rows["SINGLE_IP_RELEASE_EVENT_PREMIUM"]["eps_fcf"], "10")
        self.assertEqual(rows["UGC_GAME_PLATFORM_SAFETY"]["valuation"], "8")
        self.assertEqual(rows["ADTECH_PLATFORM_PREMIUM"]["market_mispricing"], "14")
        self.assertEqual(rows["ADTECH_PLATFORM_PREMIUM"]["valuation"], "8")
        self.assertEqual(rows["STREAMING_AD_PLATFORM"]["valuation"], "11")
        self.assertEqual(rows["CYBERSECURITY_AI_THREAT_DEMAND"]["eps_fcf"], "21")
        self.assertEqual(rows["CYBERSECURITY_AI_THREAT_DEMAND"]["valuation"], "11")
        self.assertEqual(rows["AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER"]["bottleneck_pricing"], "13")
        self.assertEqual(rows["AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER"]["capital_allocation"], "2")
        self.assertEqual(rows["SECURITY_IDENTITY_DEEPFAKE"]["valuation"], "11")
        self.assertEqual(rows["SECURITY_OPERATIONAL_TRUST_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["PLATFORM_AD_TRUST_OVERLAY"]["eps_fcf"], "gate")
        self.assertEqual(rows["PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY"]["gate_only"], "true")
        self.assertEqual(rows["METAVERSE_NFT_THEME"]["information_confidence"], "3")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["eps_fcf"], "cap")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["information_confidence"], "+")
        self.assertEqual(rows["DISCLOSURE_CONFIDENCE_CAP"]["gate_only"], "false")
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_stage_date_and_price_field_plans_are_explicit(self):
        rows = {row["target_id"]: row for row in round153_stage_date_rows()}
        fields = {row["field"] for row in round153_price_field_rows()}

        self.assertIn("arr_growth", rows["B2B_SAAS_ERP_WORKFLOW"]["stage2"])
        self.assertIn("auditable_workflow", rows["ENTERPRISE_AI_ONTOLOGY_WORKFLOW"]["stage2"])
        self.assertIn("program_of_record", rows["GOVERNMENT_AI_PROGRAM_OF_RECORD"]["stage2"])
        self.assertIn("paid_ai_contract", rows["CLOUD_AI_SOFTWARE_INFRA"]["stage2"])
        self.assertIn("ai_arr", rows["LEGACY_SAAS_AI_REINFORCEMENT"]["stage2"])
        self.assertIn("seat_churn_measured", rows["LEGACY_SAAS_AI_DISRUPTION_OVERLAY"]["stage2"])
        self.assertIn("long_term_ai_cloud_contract", rows["EDGE_AI_CLOUD_INFRASTRUCTURE"]["stage2"])
        self.assertIn("ai_monitoring_customer_growth", rows["OBSERVABILITY_AI_OPERATIONS"]["stage2"])
        self.assertIn("billings_growth", rows["CYBERSECURITY_AI_THREAT_DEMAND"]["stage2"])
        self.assertIn("software_security_mix", rows["AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER"]["stage2"])
        self.assertIn("restructuring_cost", rows["AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER"]["stage4c"])
        self.assertIn("guidance_miss", rows["OBSERVABILITY_GUIDANCE_RISK"]["stage4c"])
        self.assertIn("preorder_actual", rows["SINGLE_IP_RELEASE_EVENT_PREMIUM"]["stage2"])
        self.assertIn("bookings_guide_cut", rows["UGC_GAME_PLATFORM_SAFETY"]["stage4c"])
        self.assertIn("revenue_miss", rows["ADTECH_PLATFORM_PREMIUM"]["stage4c"])
        self.assertIn("global_outage", rows["SECURITY_OPERATIONAL_TRUST_OVERLAY"]["stage4c"])
        self.assertIn("consumer_protection_lawsuit", rows["PLATFORM_AD_TRUST_OVERLAY"]["stage4c"])
        self.assertIn("age_verification_order", rows["PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY"]["stage4c"])
        self.assertIn("stage3_cap_until_arr_contract_or_incident_details_verified", rows["DISCLOSURE_CONFIDENCE_CAP"]["stage3"])
        for field in (
            "stage2_price",
            "below_stage2_price_flag",
            "arr_growth",
            "net_retention_rate",
            "ai_revenue_contribution",
            "ai_arr",
            "ai_attach_rate",
            "total_contract_value",
            "revenue_per_employee",
            "government_revenue_growth",
            "commercial_revenue_growth",
            "ontology_workflow_flag",
            "program_of_record_flag",
            "government_program_budget_flag",
            "maven_or_defense_ai_flag",
            "seat_churn_flag",
            "license_downsell_flag",
            "gross_margin_impact_from_ai",
            "agent_cost_overrun_flag",
            "workflow_lockin_failure_flag",
            "ai_arr_too_small_flag",
            "edge_cloud_contract_value",
            "edge_cloud_contract_duration_years",
            "frontier_model_customer_flag",
            "customer_disclosed_flag",
            "cloud_infrastructure_services_revenue",
            "cdn_legacy_revenue_change",
            "edge_inference_revenue_flag",
            "cloud_capex_amount",
            "ai_customer_concentration",
            "observability_revenue",
            "observability_arr",
            "ai_workload_customer_count",
            "cloud_optimization_risk_flag",
            "arr_miss_flag",
            "guidance_miss_flag",
            "net_new_arr_change",
            "ai_infrastructure_orders",
            "hyperscaler_ai_orders",
            "data_center_switching_orders",
            "software_security_mix",
            "silicon_optics_revenue_mix",
            "order_to_revenue_conversion",
            "margin_conversion_flag",
            "restructuring_cost",
            "workforce_reduction",
            "legacy_networking_mix",
            "bookings_growth",
            "communication_engagement_change",
            "preorder_event_flag",
            "ad_tier_users",
            "ad_growth_forecast_cut",
            "ai_production_disruption_flag",
            "dark_pattern_allegation_flag",
            "autoplay_restriction_flag",
            "security_billings_growth",
            "security_arr_growth",
            "ai_threat_demand_flag",
            "sase_revenue_growth",
            "firewall_revenue_growth",
            "affected_device_count",
            "customer_lawsuit_flag",
            "founder_legal_case_flag",
            "youth_safety_lawsuit_flag",
            "age_verification_order_flag",
            "algorithm_modification_order_flag",
            "addictive_design_claim_flag",
            "infinite_scroll_restriction_flag",
            "copyright_lawsuit_flag",
            "generative_ai_ip_risk_flag",
            "opendart_rcept_no",
            "opendart_detail_fetched_flag",
            "disclosure_confidence_score",
            "detail_parser_confidence",
            "disclosure_signal_class",
            "routine_disclosure_flag",
            "risk_disclosure_flag",
            "high_signal_disclosure_flag",
            "score_price_alignment",
        ):
            self.assertIn(field, fields)
        self.assertEqual(len(fields), len(ROUND153_PRICE_FIELDS))

    def test_base_score_axes_match_round153_weight_table(self):
        rows = {row["axis_id"]: row for row in round153_base_score_axis_rows()}

        self.assertEqual(len(rows), 7)
        self.assertEqual(rows["arr_billings_bookings_ad_revenue_contract_value"]["weight"], "24")
        self.assertIn("guidance_raise", rows["arr_billings_bookings_ad_revenue_contract_value"]["stage2_evidence"])
        self.assertIn("bookings_cut", rows["arr_billings_bookings_ad_revenue_contract_value"]["hard_redteam"])
        self.assertEqual(rows["recurrence_retention_workflow_lock_in"]["weight"], "20")
        self.assertIn("workflow_lock_in", rows["recurrence_retention_workflow_lock_in"]["stage3_evidence"])
        self.assertEqual(rows["ai_cloud_security_platform_bottleneck"]["weight"], "14")
        self.assertIn("software_security_mix", rows["ai_cloud_security_platform_bottleneck"]["stage3_evidence"])
        self.assertEqual(rows["opm_fcf_gross_margin_conversion"]["weight"], "12")
        self.assertEqual(rows["market_mispricing_rerating_gap"]["weight"], "8")
        self.assertEqual(rows["valuation_room_4b_margin"]["weight"], "8")
        self.assertEqual(rows["operational_trust_legal_privacy_disclosure"]["weight"], "14")
        self.assertIn("security_outage", rows["operational_trust_legal_privacy_disclosure"]["hard_redteam"])
        for row in rows.values():
            self.assertEqual(row["production_scoring_changed"], "false")

    def test_summary_and_markdown_explain_r8_loop9_guardrails(self):
        summary = round153_summary()
        summary_md = render_round153_summary_markdown()
        guardrails = render_round153_green_guardrail_markdown()
        overlays = render_round153_risk_overlay_markdown()
        price_plan = render_round153_price_validation_plan_markdown()

        self.assertEqual(summary["target_count"], 28)
        self.assertEqual(summary["base_score_axis_count"], 7)
        self.assertEqual(summary["case_candidate_count"], 21)
        self.assertEqual(summary["structural_success_count"], 1)
        self.assertEqual(summary["success_candidate_count"], 8)
        self.assertEqual(summary["event_premium_count"], 1)
        self.assertEqual(summary["stage4b_case_count"], 8)
        self.assertEqual(summary["stage4c_case_count"], 6)
        self.assertEqual(summary["green_possible_count"], 3)
        self.assertEqual(summary["watch_yellow_first_count"], 16)
        self.assertEqual(summary["redteam_first_count"], 9)
        self.assertEqual(summary["gate_only_target_count"], 7)
        self.assertFalse(summary["production_scoring_changed"])
        self.assertIn("Round 153", summary_md)
        self.assertIn("Do not apply R8 Loop-9 v9.0 weights", guardrails)
        self.assertIn("SECURITY_TRUST_BREAK", overlays)
        self.assertIn("GOVERNMENT_AI_PROGRAM_ALIGNED", overlays)
        self.assertIn("EDGE_AI_CLOUD_CONTRACT_ALIGNED", overlays)
        self.assertIn("OBSERVABILITY_GUIDANCE_FAILED", overlays)
        self.assertIn("ENTERPRISE_AI_WORKFLOW_ALIGNED", overlays)
        self.assertIn("CYBERSECURITY_AI_THREAT_DEMAND_ALIGNED", overlays)
        self.assertIn("AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER_STAGE2_RESTRUCTURING_WATCH", overlays)
        self.assertIn("LEGACY_SAAS_AI_DISRUPTION", overlays)
        self.assertIn("PRIVACY_YOUTH_SAFETY_GATE", overlays)
        self.assertIn("DISCLOSURE_CONFIDENCE_CAP", overlays)
        self.assertIn("crowdstrike_outage_shareholder_case", price_plan)
        self.assertIn("akamai_ai_cloud_revenue_contribution_case", price_plan)
        self.assertIn("cisco_ai_infrastructure_orders_case", price_plan)
        self.assertIn("salesforce_agentforce_arr_case", price_plan)
        self.assertIn("R8 v9 Base Score Axes", summary_md)

    def test_report_writer_outputs_cases_and_reports(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = write_round153_r8_loop9_reports(
                output_directory=Path(tmp) / "out",
                cases_path=Path(tmp) / "cases_r8_loop9_round153.jsonl",
                score_profile_path=Path(tmp) / "score_weight_profiles_round153_r8_loop9_v9.csv",
            )

            self.assertTrue(paths["cases"].exists())
            self.assertTrue(paths["score_profiles"].exists())
            self.assertTrue(paths["summary"].exists())
            self.assertTrue(paths["case_matrix"].exists())
            self.assertTrue(paths["stage_date_plan"].exists())
            self.assertTrue(paths["base_score_axes"].exists())
            self.assertTrue(paths["green_guardrails"].exists())
            self.assertTrue(paths["risk_overlays"].exists())
            self.assertTrue(paths["price_validation_plan"].exists())
            self.assertTrue(paths["price_fields"].exists())
            self.assertEqual(len(load_case_library(paths["cases"])), len(ROUND153_CASE_CANDIDATES))

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

    def test_production_scoring_modules_do_not_import_round153_pack(self):
        for path in (
            "src/e2r/features.py",
            "src/e2r/staging.py",
            "src/e2r/red_team.py",
            "src/e2r/pipeline/e2r_standard_flow.py",
        ):
            text = Path(path).read_text(encoding="utf-8")
            self.assertNotIn("round153_r8_loop9_platform_content_sw_security", text)


if __name__ == "__main__":
    unittest.main()
