"""Round-127 R8 Loop-7 platform/content/software/security pack.

Round 127 tightens the R8 platform/content/software/security pack. It separates
AI features, game IP, ad recovery, security demand, and platform scale from
actual repeat revenue evidence: ARR, billings, bookings, ad revenue, churn,
customer retention, OPM, FCF, workflow integration, operational trust, privacy,
youth-safety, and ad-quality evidence.

This module is calibration/report material only. Production feature
engineering, scoring, staging, and RedTeam code must not import it.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import CaseDataQuality, E2RCaseRecord, PriceValidation
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture


ROUND127_SOURCE_ROUND_PATH = "docs/round/round_127.md"
ROUND127_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round127_r8_loop7_platform_content_sw_security"
ROUND127_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r8_loop7_round127.jsonl"
ROUND127_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round127_r8_loop7_v7.csv"


@dataclass(frozen=True)
class Round127ScoreWeightDraft:
    eps_fcf: int | str
    structural_visibility: int | str
    bottleneck_pricing: int | str
    market_mispricing: int | str
    valuation: int | str
    capital_allocation: int | str
    information_confidence: int | str

    def as_dict(self) -> dict[str, int | str]:
        return {
            "eps_fcf": self.eps_fcf,
            "structural_visibility": self.structural_visibility,
            "bottleneck_pricing": self.bottleneck_pricing,
            "market_mispricing": self.market_mispricing,
            "valuation": self.valuation,
            "capital_allocation": self.capital_allocation,
            "information_confidence": self.information_confidence,
        }


@dataclass(frozen=True)
class Round127BaseScoreAxis:
    axis_id: str
    weight: int
    stage2_evidence: tuple[str, ...]
    stage3_evidence: tuple[str, ...]
    hard_redteam: tuple[str, ...]
    normalization_point: str


@dataclass(frozen=True)
class Round127ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round127ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop7_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round127CaseCandidate:
    case_id: str
    target_id: str
    symbol: str
    company_name: str
    market: str
    case_type: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    alignment_hint: str
    price_validation_status: str
    source_refs: tuple[str, ...]
    notes: str
    secondary_archetypes: tuple[E2RArchetype, ...] = ()

    @property
    def expected_group(self) -> str:
        return self.case_type


GATE_WEIGHT = Round127ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate")
GATE_INFO5_WEIGHT = Round127ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", 5)
CAP_WEIGHT = Round127ScoreWeightDraft("cap", "cap", "cap", "cap", "cap", "cap", "+")


ROUND127_BASE_SCORE_AXES: tuple[Round127BaseScoreAxis, ...] = (
    Round127BaseScoreAxis(
        "arr_billings_bookings_ad_revenue_contract_value",
        24,
        ("arr_growth", "billings_growth", "bookings_growth", "ad_revenue_growth", "contract_value", "guidance_raise"),
        ("repeat_revenue_growth", "renewal_strength", "net_retention_rate", "ad_arpu", "contract_renewal"),
        ("arr_miss", "guidance_miss", "bookings_cut", "revenue_miss"),
        "AI feature, user count, or ad tier launch remains Stage 1 until repeat revenue or contract value is verified.",
    ),
    Round127BaseScoreAxis(
        "recurrence_retention_workflow_lock_in",
        20,
        ("low_churn", "customer_retention", "workflow_integration", "paid_product_adoption"),
        ("workflow_lock_in", "renewal", "seat_churn_low", "customer_expansion"),
        ("seat_churn", "license_downsell", "workflow_lockin_failure", "age_verification_friction"),
        "Green needs repeated usage and workflow lock-in, not one product launch or one viral title.",
    ),
    Round127BaseScoreAxis(
        "ai_cloud_security_platform_bottleneck",
        14,
        ("ai_workload_customer_count", "hyperscaler_ai_orders", "sase_firewall_demand", "frontier_model_customer_flag"),
        ("capacity_constraint", "software_security_mix", "ai_workload_attach", "security_platform_lock_in"),
        ("customer_concentration", "capex_burden", "security_demand_bubble", "order_to_revenue_delay"),
        "AI/cloud/security demand gets credit only when it creates billable bottleneck or platform lock-in.",
    ),
    Round127BaseScoreAxis(
        "opm_fcf_gross_margin_conversion",
        12,
        ("opm_improvement", "gross_margin_stable", "fcf_margin", "margin_confirmed"),
        ("fcf_conversion", "rule_of_40", "compute_cost_controlled", "gross_margin_stable"),
        ("gross_margin_pressure", "agent_cost_overrun", "margin_miss", "restructuring_cost"),
        "AI revenue is not enough if compute cost, capex, or restructuring absorbs the economics.",
    ),
    Round127BaseScoreAxis(
        "market_mispricing_rerating_gap",
        10,
        ("legacy_frame_shift", "old_saas_frame", "legacy_cdn_reframe", "ad_platform_reframe"),
        ("valuation_frame_shift", "platform_monetization", "new_repeat_revenue_frame"),
        ("narrative_fully_priced", "price_failed_after_beat", "premium_multiple_guidance_miss"),
        "Rerating room exists only when the market still uses the old frame while repeat economics are improving.",
    ),
    Round127BaseScoreAxis(
        "valuation_room_4b_margin",
        8,
        ("valuation_room", "multiple_not_saturated", "price_path_not_overextended"),
        ("price_path_alignment", "revision_support", "valuation_still_reasonable"),
        ("valuation_saturation", "strong_results_stock_stalls", "ai_software_narrative_crowded", "short_term_price_spike"),
        "High-quality AI/platform evidence can still be 4B-watch if valuation moved first.",
    ),
    Round127BaseScoreAxis(
        "operational_trust_legal_privacy_disclosure",
        12,
        ("disclosure_confidence_score", "privacy_risk_low", "ad_quality_clean", "operational_trust_intact"),
        ("legal_stability", "security_incident_absent", "customer_terms_verified", "ad_quality_controls_verified"),
        ("security_outage", "privacy_lawsuit", "youth_safety_lawsuit", "scam_ad_lawsuit", "copyright_lawsuit", "disclosure_confidence_low"),
        "Operational trust and legal/data quality are not side notes; they can cap or break Stage 3.",
    ),
)


ROUND127_SCORE_TARGETS: tuple[Round127ScoreTarget, ...] = (
    Round127ScoreTarget(
        "PLATFORM_SOFTWARE_INTERNET",
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(18, 18, 7, 15, 13, 1, 5),
        ("portal_growth", "messenger_ecosystem", "commerce_platform_growth", "ad_platform_recovery", "user_growth"),
        ("arpu_growth", "recurring_revenue", "opm_improvement", "governance_clean", "ad_quality_clean"),
        ("platform_monetization", "fcf_conversion", "regulatory_risk_low", "privacy_risk_low"),
        ("platform_multiple_crowded", "user_count_story_overpriced", "legal_risk_ignored"),
        ("privacy_lawsuit", "founder_legal_case", "regulatory_investigation", "trust_damage", "scam_ad_lawsuit"),
        ("arpu_growth", "recurring_revenue", "opm_improvement", "fcf_conversion", "governance_clean"),
        ("governance", "privacy", "legal_overhang", "youth_safety", "ad_quality"),
        ("governance", "privacy", "ad_quality", "youth_safety"),
        "Platform Green needs monetization and trust, not user count alone.",
    ),
    Round127ScoreTarget(
        "B2B_SAAS_ERP_WORKFLOW",
        E2RArchetype.B2B_SAAS_ERP_WORKFLOW,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round127ScoreWeightDraft(20, 23, 7, 15, 13, 1, 5),
        ("cloud_erp_transition", "b2b_saas_growth", "sme_cloud_conversion", "pe_operational_improvement"),
        ("arr_growth", "recurring_revenue_ratio", "low_churn", "customer_lock_in", "opm_improvement"),
        ("fcf_conversion", "net_retention_rate", "workflow_lock_in", "valuation_frame_shift"),
        ("b2b_saas_premium_crowded", "pe_event_premium_overread"),
        ("churn_spike", "si_revenue_reversion", "opm_decline", "regulatory_approval_failure"),
        ("arr_growth", "recurring_revenue_ratio", "low_churn", "customer_lock_in", "fcf_conversion"),
        ("churn", "si_revenue_mix", "regulatory_approval", "event_premium"),
        ("churn", "si_revenue", "regulatory", "pe_event_premium"),
        "B2B SaaS/ERP can be Green only when repeat revenue, churn, lock-in, OPM, and FCF are visible.",
    ),
    Round127ScoreTarget(
        "ENTERPRISE_AI_ONTOLOGY_WORKFLOW",
        E2RArchetype.ENTERPRISE_AI_ONTOLOGY_WORKFLOW,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round127ScoreWeightDraft(23, 23, 10, 16, 9, 0, 6),
        ("enterprise_ai_platform", "ontology_workflow", "private_data_integration", "ai_action_layer"),
        ("paid_ai_contract", "total_contract_value", "government_revenue_growth", "commercial_revenue_growth", "auditable_workflow"),
        ("repeat_contract", "workflow_lock_in", "opm_improvement", "fcf_conversion", "rule_of_40"),
        ("ai_software_narrative_crowded", "valuation_saturation", "strong_results_stock_stalls"),
        ("ai_compute_cost_surge", "government_contract_risk", "auditability_failure", "model_dependency", "political_risk"),
        ("paid_ai_contract", "total_contract_value", "auditable_workflow", "workflow_lock_in", "fcf_conversion"),
        ("valuation_crowding", "government_customer", "ai_cost", "model_dependency", "auditability_failure"),
        ("valuation", "government_customer", "ai_cost", "auditability", "workflow_lock_in"),
        "Enterprise AI ontology is Green-capable only when AI becomes contracted, auditable workflow with OPM and FCF.",
    ),
    Round127ScoreTarget(
        "GOVERNMENT_AI_PROGRAM_OF_RECORD",
        E2RArchetype.GOVERNMENT_AI_PROGRAM_OF_RECORD,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(23, 24, 11, 15, 10, 0, 6),
        ("government_ai_pilot", "defense_ai_software", "public_sector_ai_contract", "maven_or_defense_ai_flag"),
        ("program_of_record", "government_program_budget", "official_procurement", "long_term_contract", "total_contract_value"),
        ("recurring_government_software_revenue", "commercial_expansion", "auditable_workflow", "fcf_conversion"),
        ("government_ai_contractor_premium_overheated", "program_of_record_fully_priced"),
        ("budget_cut", "contract_cancellation", "political_risk", "auditability_failure", "ethics_review"),
        ("program_of_record", "government_program_budget", "official_procurement", "auditable_workflow", "fcf_conversion"),
        ("political_risk", "budget_cycle", "government_customer_concentration", "auditability_failure"),
        ("government_budget", "program_of_record", "auditability", "customer_concentration"),
        "Government AI becomes higher-quality only when pilot work turns into a funded program of record.",
    ),
    Round127ScoreTarget(
        "CLOUD_AI_SOFTWARE_INFRA",
        E2RArchetype.CLOUD_AI_SOFTWARE_INFRA,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round127ScoreWeightDraft(22, 23, 9, 16, 10, 0, 5),
        ("enterprise_ai_platform", "ai_workflow_automation", "agentic_ai_platform", "private_data_integration"),
        ("paid_ai_contract", "total_contract_value", "government_revenue_growth", "commercial_revenue_growth", "revenue_per_employee"),
        ("auditable_workflow", "repeat_contract", "fcf_conversion", "opm_improvement", "rule_of_40"),
        ("ai_software_narrative_crowded", "valuation_saturation", "strong_results_stock_stalls"),
        ("ai_compute_cost_surge", "government_contract_risk", "auditability_failure", "model_dependency"),
        ("paid_ai_contract", "total_contract_value", "auditable_workflow", "opm_improvement", "fcf_conversion"),
        ("valuation_crowding", "government_customer", "ai_cost", "model_dependency"),
        ("valuation", "government_customer", "ai_cost", "auditability"),
        "Cloud AI software needs actual contracts, auditable workflow, and FCF, not AI demos.",
    ),
    Round127ScoreTarget(
        "EDGE_AI_CLOUD_INFRASTRUCTURE",
        E2RArchetype.EDGE_AI_CLOUD_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(20, 21, 12, 14, 9, 2, 5),
        ("edge_ai_cloud_contract", "distributed_inference", "frontier_model_provider", "cdn_to_cloud_transition"),
        ("long_term_ai_cloud_contract", "cloud_infrastructure_services_revenue", "frontier_model_customer", "revenue_contribution"),
        ("repeat_ai_cloud_revenue", "margin_confirmed", "capex_controlled", "fcf_conversion", "customer_concentration_low"),
        ("edge_ai_cloud_contract_premium_crowded", "legacy_cdn_reframe_overheated"),
        ("capex_burden", "ai_customer_concentration", "margin_miss", "legacy_cdn_decline", "customer_undisclosed"),
        ("long_term_ai_cloud_contract", "revenue_contribution", "margin_confirmed", "capex_controlled", "fcf_conversion"),
        ("capex", "customer_concentration", "legacy_cdn_decline", "margin_miss", "undisclosed_customer"),
        ("capex", "customer_concentration", "legacy_decline", "margin"),
        "Edge AI cloud is Watch-to-Green: a long contract is useful, but margin, capex, FCF, and customer concentration still gate promotion.",
    ),
    Round127ScoreTarget(
        "AI_SOFTWARE_APPLICATION",
        E2RArchetype.AI_SOFTWARE_APPLICATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(20, 19, 9, 15, 12, 0, 5),
        ("ai_application_launch", "enterprise_ai_adoption", "api_usage_growth"),
        ("paid_customer_growth", "api_revenue", "workflow_integration", "total_contract_value"),
        ("repeat_paid_usage", "fcf_conversion", "compute_cost_controlled", "auditable_workflow"),
        ("ai_app_narrative_crowded", "valuation_before_margin_proof", "rule_of_40_fully_priced"),
        ("compute_cost_spike", "model_dependency", "copyright_lawsuit", "data_privacy_lawsuit"),
        ("paid_usage", "api_revenue", "workflow_integration", "compute_cost_controlled", "fcf_conversion"),
        ("compute_cost", "model_dependency", "copyright", "data_privacy", "free_user_growth_only"),
        ("compute_cost", "model_dependency", "4b_crowding"),
        "AI applications need paid usage and unit economics, not feature announcements.",
    ),
    Round127ScoreTarget(
        "LEGACY_SAAS_AI_REINFORCEMENT",
        E2RArchetype.LEGACY_SAAS_AI_REINFORCEMENT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(20, 21, 8, 14, 11, 0, 6),
        ("ai_agent_launch", "copilot_launch", "workflow_ai_feature", "agentforce_like_arr"),
        ("ai_arr", "ai_attach_rate", "customer_adoption", "productivity_roi", "seat_churn_measured"),
        ("ai_reinforces_workflow_lock_in", "seat_churn_low", "gross_margin_stable", "fcf_conversion"),
        ("legacy_saas_ai_narrative_overheated", "agent_revenue_too_small_for_multiple"),
        ("ai_substitutes_existing_seat_model", "license_downsell", "gross_margin_pressure", "agent_cost_overrun", "workflow_lockin_failure"),
        ("ai_arr", "ai_attach_rate", "seat_churn_low", "gross_margin_stable", "workflow_lock_in"),
        ("ai_arr_too_small", "seat_churn", "license_downsell", "gross_margin_pressure", "agent_cost_overrun"),
        ("ai_arr", "attach_rate", "seat_churn", "gross_margin", "workflow_lock_in"),
        "Legacy SaaS AI reinforcement is Watch-to-Green only when AI attach grows without seat churn or margin damage.",
    ),
    Round127ScoreTarget(
        "LEGACY_SAAS_AI_DISRUPTION_OVERLAY",
        E2RArchetype.LEGACY_SAAS_AI_DISRUPTION_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("ai_agent_launch", "copilot_launch", "workflow_ai_feature", "agentforce_like_arr"),
        ("ai_arr", "ai_attach_rate", "customer_adoption", "productivity_roi", "seat_churn_measured"),
        ("ai_reinforces_workflow_lock_in", "seat_churn_low", "gross_margin_stable", "fcf_conversion"),
        ("legacy_saas_ai_narrative_overheated", "agent_revenue_too_small_for_multiple"),
        ("ai_substitutes_existing_seat_model", "license_downsell", "gross_margin_pressure", "agent_cost_overrun", "workflow_lockin_failure"),
        (),
        ("seat_churn", "license_downsell", "gross_margin_pressure", "agent_cost_overrun", "workflow_lockin_failure"),
        ("seat_churn", "license_downsell", "gross_margin", "ai_cost", "workflow_lock_in"),
        "Legacy SaaS AI is a RedTeam overlay: AI can reinforce workflow lock-in, but it can also cannibalize seats and margins.",
        gate_only=True,
    ),
    Round127ScoreTarget(
        "OBSERVABILITY_AI_OPERATIONS",
        E2RArchetype.OBSERVABILITY_AI_OPERATIONS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(21, 22, 8, 15, 10, 0, 5),
        ("ai_workload_monitoring", "aiops", "sre_agent", "security_analyst_agent"),
        ("arr_growth", "ai_monitoring_customer_growth", "guidance_raise", "observability_revenue_growth"),
        ("net_retention_rate", "fcf_conversion", "ai_workload_attach", "usage_resilience"),
        ("observability_ai_premium_crowded", "ai_operations_multiple_saturated"),
        ("cloud_optimization", "net_retention_slowdown", "usage_slowdown", "guidance_cut"),
        ("arr_growth", "net_retention_rate", "ai_workload_attach", "fcf_conversion"),
        ("cloud_optimization", "net_retention", "usage_slowdown", "4b"),
        ("cloud_optimization", "net_retention", "usage"),
        "Observability AI can be Watch-to-Green only when AI workload monitoring becomes ARR and FCF.",
    ),
    Round127ScoreTarget(
        "OBSERVABILITY_GUIDANCE_RISK",
        E2RArchetype.OBSERVABILITY_GUIDANCE_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("arr_guidance_miss", "net_new_arr_slowdown", "conservative_guidance", "price_failed_after_beat"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("observability_growth_priced_before_arr",),
        ("arr_miss", "net_new_arr_slowdown", "guidance_miss", "growth_target_uncertainty", "valuation_compression"),
        (),
        ("arr_miss", "guidance_miss", "net_new_arr_slowdown", "valuation_compression"),
        ("arr", "guidance", "net_new_arr", "valuation"),
        "Observability guidance risk is a gate-only overlay because earnings beats can still fail if ARR or guidance is weak.",
        gate_only=True,
    ),
    Round127ScoreTarget(
        "CONTACT_CENTER_AI_AUTOMATION",
        E2RArchetype.CONTACT_CENTER_AI_AUTOMATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(19, 20, 8, 14, 13, 0, 5),
        ("ccaas_ai_agent_assist", "contact_center_automation", "seat_expansion"),
        ("enterprise_contract", "seat_expansion", "retention_rate", "opm_improvement", "aht_reduction"),
        ("workflow_embedded", "low_churn", "enterprise_retention", "fcf_conversion", "roi_verified"),
        ("contact_center_ai_crowded",),
        ("churn_spike", "it_budget_cut", "privacy_event", "automation_roi_failure"),
        ("enterprise_contract", "seat_expansion", "low_churn", "retention_rate", "opm_improvement"),
        ("churn", "it_budget_cut", "privacy", "roi_failure"),
        ("churn", "it_budget", "privacy", "roi"),
        "Contact-center AI needs enterprise retention and workflow economics.",
    ),
    Round127ScoreTarget(
        "GAME_CONTENT_IP",
        E2RArchetype.GAME_CONTENT_IP,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(18, 16, 6, 13, 10, 0, 5),
        ("new_title_announcement", "ip_expansion", "preorder_rumor", "user_growth"),
        ("bookings_growth", "sell_through", "preorder_actual", "launch_date_confirmed", "live_service_monetization"),
        ("repeat_ip_portfolio", "global_monetization", "single_ip_risk_low", "op_eps_revision"),
        ("single_ip_valuation_crowded", "launch_expectations_saturated"),
        ("game_delay", "booking_deferral", "development_cost_inflation", "single_ip_revenue_risk"),
        ("bookings_growth", "sell_through", "live_service_monetization", "repeat_ip_portfolio"),
        ("single_ip", "game_delay", "booking_deferral", "development_cost", "bookings_cut"),
        ("single_ip", "delay", "bookings", "development_cost"),
        "Game IP is Watch unless bookings and repeat monetization are proven.",
    ),
    Round127ScoreTarget(
        "SINGLE_IP_RELEASE_EVENT_PREMIUM",
        E2RArchetype.SINGLE_IP_RELEASE_EVENT_PREMIUM,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(10, 8, 4, 10, 6, 0, 5),
        ("preorder_rumor", "single_title_delay", "mega_ip_release_window", "affiliate_leak"),
        ("preorder_actual", "launch_date_confirmed", "bookings_guidance", "development_cost_known"),
        ("successful_launch", "bookings_conversion", "live_service_monetization", "single_ip_risk_low"),
        ("single_ip_event_premium_crowded", "preorder_rumor_priced_before_bookings"),
        ("release_delay", "booking_deferral", "development_cost_inflation", "single_title_revenue_risk", "preorder_not_confirmed"),
        ("preorder_actual", "launch_execution", "bookings_conversion", "repeat_monetization"),
        ("preorder_rumor", "release_delay", "single_ip_revenue_ratio", "development_cost", "bookings_unverified"),
        ("single_ip", "preorder", "delay", "bookings", "development_cost"),
        "Single-IP preorder or delay events can move price, but they are not structural IP portfolio evidence.",
    ),
    Round127ScoreTarget(
        "UGC_GAME_PLATFORM_SAFETY",
        E2RArchetype.UGC_GAME_PLATFORM_SAFETY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(17, 14, 5, 12, 8, 0, 5),
        ("ugc_platform_dau_growth", "safety_feature_rollout", "communication_engagement"),
        ("bookings_growth", "dau_growth", "age_verification_impact_measured", "content_monitoring_scaled"),
        ("safety_compliance", "bookings_resilience", "user_growth_resilience"),
        ("ugc_platform_scale_narrative_crowded",),
        ("child_safety_litigation", "age_verification_friction", "bookings_guide_cut", "user_growth_slowdown"),
        ("bookings_resilience", "safety_compliance", "user_growth_resilience"),
        ("child_safety", "age_verification", "bookings_cut", "regulatory_ban"),
        ("child_safety", "age_verification", "bookings", "regulation"),
        "UGC platforms need bookings after safety friction; DAU alone is not Green evidence.",
    ),
    Round127ScoreTarget(
        "MEDIA_AD_CONTENT_CYCLE",
        E2RArchetype.MEDIA_AD_CONTENT_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(16, 14, 6, 12, 9, 0, 5),
        ("ad_market_recovery", "global_ad_budget_growth", "content_cycle_rebound"),
        ("ad_revenue_growth", "budget_resilience", "opm_improvement", "client_budget_stable"),
        ("repeat_platform_ad_revenue", "budget_resilience", "ai_disruption_low"),
        ("ad_cycle_recovery_overpriced",),
        ("client_budget_cut", "ai_disintermediation", "profit_drop", "dividend_cut", "workforce_reduction"),
        ("ad_revenue_growth", "opm_improvement", "budget_resilience"),
        ("ad_cycle", "client_budget_cut", "ai_disruption", "traditional_agency_margin"),
        ("ad_cycle", "client_budget", "ai_disruption", "guidance_miss"),
        "Traditional media/ad cycle rebounds stay capped unless structural ad-tech economics are proven.",
    ),
    Round127ScoreTarget(
        "ADTECH_PLATFORM_PREMIUM",
        E2RArchetype.ADTECH_PLATFORM_PREMIUM,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(18, 18, 7, 14, 8, 0, 5),
        ("ctv_growth", "retail_media_growth", "ai_ad_platform_growth", "kokai_platform_adoption"),
        ("revenue_growth", "customer_retention", "platform_adoption", "guidance_confirmed"),
        ("premium_valuation_justified_by_growth", "fcf_conversion", "budget_resilience"),
        ("adtech_premium_crowded", "premium_multiple_guidance_miss"),
        ("revenue_miss", "guidance_miss", "platform_transition_failure", "premium_valuation_drawdown"),
        ("revenue_growth", "retention", "platform_adoption", "fcf_conversion"),
        ("revenue_miss", "guidance_miss", "premium_valuation", "transition_failure"),
        ("revenue_miss", "guidance", "premium_valuation"),
        "Ad-tech premium needs durable growth; under premium valuation, revenue or guidance misses are hard warnings.",
    ),
    Round127ScoreTarget(
        "STREAMING_AD_PLATFORM",
        E2RArchetype.STREAMING_AD_PLATFORM,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(20, 21, 8, 14, 11, 0, 5),
        ("ad_tier_user_growth", "streaming_ad_inventory", "ctv_ad_platform"),
        ("ad_tier_users", "ad_revenue_growth", "ad_arpu", "own_ad_tech", "ad_supported_signup_mix"),
        ("subscription_ad_hybrid", "arpu_expansion", "privacy_risk_low", "fcf_support"),
        ("streaming_ad_multiple_crowded", "ad_tier_growth_fully_priced", "privacy_risk_ignored"),
        ("privacy_lawsuit", "dark_pattern_allegation", "child_data_collection", "ad_load_churn"),
        ("ad_tier_users", "ad_revenue_growth", "ad_arpu", "privacy_risk_low", "own_ad_tech"),
        ("privacy", "ad_arpu_saturation", "ad_load", "subscriber_churn", "dark_pattern"),
        ("privacy", "ad_arpu", "ad_load", "churn"),
        "Streaming ad platforms can improve, but privacy and ad ARPU are hard gates.",
    ),
    Round127ScoreTarget(
        "CYBERSECURITY_AI_THREAT_DEMAND",
        E2RArchetype.CYBERSECURITY_AI_THREAT_DEMAND,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(21, 21, 10, 14, 11, 0, 5),
        ("ai_ransomware", "ai_driven_cyber_threat", "security_budget_increase", "sase_firewall_demand"),
        ("billings_growth", "arr_growth", "guidance_raise", "renewal_rate", "opm_improvement"),
        ("security_platform_lock_in", "renewal_strength", "operational_trust_intact", "fcf_conversion"),
        ("ai_security_narrative_crowded", "threat_demand_fully_priced"),
        ("global_outage", "customer_lawsuit", "renewal_rate_down", "trust_damage", "security_demand_bubble"),
        ("billings_growth", "arr_growth", "renewal_strength", "operational_trust_intact", "fcf_conversion"),
        ("situational_demand_bubble", "renewal_risk", "outage", "trust_damage"),
        ("billings", "arr", "renewal", "operational_trust"),
        "AI threat demand is useful only when it becomes billings, ARR, renewal strength, and FCF.",
    ),
    Round127ScoreTarget(
        "AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER",
        E2RArchetype.AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(21, 21, 13, 13, 9, 2, 5),
        ("ai_networking_orders", "hyperscaler_ai_orders", "data_center_switching_orders", "silicon_optics_security_reframe"),
        ("ai_infrastructure_orders", "data_center_switching_orders", "guidance_raise", "software_security_mix", "order_to_revenue_conversion"),
        ("revenue_conversion", "opm_conversion", "fcf_conversion", "software_security_mix", "legacy_mix_stable"),
        ("ai_networking_order_premium_crowded", "orders_priced_before_margin"),
        ("restructuring_cost", "workforce_reduction", "legacy_networking_mix", "margin_conversion_unverified", "order_to_revenue_delay"),
        ("ai_infrastructure_orders", "guidance_raise", "opm_conversion", "fcf_conversion", "software_security_mix"),
        ("restructuring_cost", "legacy_networking_mix", "margin_conversion_unverified", "customer_concentration", "order_to_revenue_delay"),
        ("orders", "software_security_mix", "margin", "legacy_mix", "restructuring"),
        "AI networking crossover is Watch-to-Green only when orders convert into software/security mix, margin, and FCF.",
    ),
    Round127ScoreTarget(
        "SECURITY_IDENTITY_DEEPFAKE",
        E2RArchetype.SECURITY_IDENTITY_DEEPFAKE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round127ScoreWeightDraft(20, 20, 10, 14, 11, 0, 5),
        ("cybersecurity_demand", "identity_threat", "deepfake_regulation", "ai_cyber_threat"),
        ("arr_growth", "billings_growth", "customer_diversification", "low_churn", "opm_improvement"),
        ("security_platform_lock_in", "renewal_strength", "operational_trust_intact"),
        ("security_multiple_crowded", "outage_risk_ignored"),
        ("global_outage", "faulty_update", "customer_lawsuit", "renewal_rate_down", "trust_damage"),
        ("arr_growth", "billings_growth", "low_churn", "customer_retention", "operational_trust_intact"),
        ("outage", "lawsuit", "renewal_risk", "trust_damage"),
        ("outage", "customer_lawsuit", "renewal", "trust_damage"),
        "Security ARR is not enough; operational reliability is a hard gate.",
    ),
    Round127ScoreTarget(
        "SECURITY_OPERATIONAL_TRUST_OVERLAY",
        E2RArchetype.SECURITY_OPERATIONAL_TRUST_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("operational_trust_event", "security_update_failure", "platform_outage"),
        ("customer_damage_quantified", "recovery_plan", "retention_impact_measured"),
        ("not_applicable_gate_only",),
        ("trust_risk_underpriced",),
        ("global_outage", "affected_devices", "customer_lawsuit", "shareholder_lawsuit", "renewal_risk"),
        (),
        ("outage", "affected_devices", "customer_damage", "lawsuit", "renewal_risk"),
        ("outage", "customer_damage", "lawsuit", "renewal"),
        "Operational trust break is a hard 4C overlay for software/security platforms.",
        gate_only=True,
    ),
    Round127ScoreTarget(
        "PLATFORM_GOVERNANCE_LEGAL_RISK",
        E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_INFO5_WEIGHT,
        ("founder_legal_case", "mna_legal_dispute", "antitrust_lawsuit", "youth_safety_lawsuit"),
        ("risk_resolved", "fine_or_business_change_quantified", "governance_discount_measured"),
        ("overhang_resolved_and_core_fcf_improves",),
        ("legal_risk_underpriced", "valuation_expands_before_resolution"),
        ("guilty_verdict", "large_fine", "forced_business_change", "governance_discount_widens"),
        (),
        ("founder_legal_case", "mna_legal_dispute", "regulatory_investigation", "youth_safety", "antitrust"),
        ("founder", "mna", "regulation", "youth_safety", "antitrust"),
        "Governance/legal risk is a RedTeam gate, not a positive score bucket.",
        gate_only=True,
    ),
    Round127ScoreTarget(
        "PLATFORM_AD_TRUST_OVERLAY",
        E2RArchetype.PLATFORM_AD_TRUST_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("scam_ad_lawsuit", "ad_quality_risk", "consumer_protection_lawsuit"),
        ("ad_quality_controls_verified", "lawsuit_cost_quantified", "revenue_quality_clean"),
        ("not_applicable_gate_only",),
        ("scam_ad_risk_underpriced",),
        ("consumer_protection_lawsuit", "ad_trust_damage", "revenue_quality_questioned", "regulatory_investigation"),
        (),
        ("scam_ads", "consumer_protection", "ad_quality", "platform_trust"),
        ("scam_ads", "ad_quality", "consumer_lawsuit"),
        "Ad revenue must pass quality filters; scam-ad revenue is RedTeam evidence.",
        gate_only=True,
    ),
    Round127ScoreTarget(
        "PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY",
        E2RArchetype.PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("privacy_lawsuit", "child_data_collection", "dark_pattern_allegation", "youth_safety_lawsuit", "age_verification_order"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("privacy_youth_safety_risk_underpriced",),
        ("privacy_lawsuit", "child_data_collection", "dark_pattern_allegation", "age_verification_order", "algorithm_modification_order", "addictive_design_claim"),
        (),
        ("privacy_lawsuit", "child_data_collection", "dark_pattern", "age_verification", "youth_safety"),
        ("privacy", "child_data", "dark_pattern", "age_verification", "youth_safety"),
        "Privacy and youth-safety issues are RedTeam gates for platform, streaming, ad, and UGC growth.",
        gate_only=True,
    ),
    Round127ScoreTarget(
        "GENERATIVE_AI_IP_RISK",
        E2RArchetype.GENERATIVE_AI_IP_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        Round127ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", 6),
        ("generative_ai_training_data", "content_license", "open_source_dependency"),
        ("licensed_dataset", "rights_cleared_revenue", "enterprise_contract"),
        ("rights_cleared_repeat_revenue", "liability_risk_low"),
        ("genai_ip_story_overheated",),
        ("copyright_lawsuit", "license_gap", "privacy_lawsuit", "opensource_supply_chain_risk"),
        ("licensed_data", "rights_cleared_revenue", "enterprise_contract", "liability_risk_low"),
        ("copyright", "license_risk", "privacy", "training_data"),
        ("copyright", "license", "training_data"),
        "Generative AI IP is a RedTeam overlay; rights and revenue must be proven.",
        gate_only=True,
    ),
    Round127ScoreTarget(
        "METAVERSE_NFT_THEME",
        E2RArchetype.METAVERSE_NFT_THEME,
        Round10ThemePosture.REDTEAM_FIRST,
        Round127ScoreWeightDraft(5, 5, 5, 6, 5, 0, 3),
        ("metaverse_nft_theme", "token_content_launch", "virtual_goods_user_growth"),
        ("regulated_revenue", "repeat_paid_usage", "non_token_cash_flow"),
        ("durable_non_token_revenue", "fcf_conversion", "regulatory_risk_low"),
        ("metaverse_nft_liquidity_bubble",),
        ("liquidity_collapse", "token_volume_collapse", "regulatory_action", "revenue_absent"),
        ("repeat_paid_usage", "regulated_revenue", "fcf_conversion"),
        ("liquidity", "token_volume", "regulation", "revenue_absent"),
        ("no_revenue_model", "liquidity_collapse"),
        "Metaverse/NFT remains Red/Watch before real repeat revenue.",
    ),
    Round127ScoreTarget(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        CAP_WEIGHT,
        ("arr_or_contract_disclosure_missing_key_fields", "security_incident_detail_missing", "customer_terms_undisclosed"),
        ("confidence_cap_detected",),
        ("stage3_cap_until_arr_contract_or_incident_details_verified",),
        ("not_applicable_cap_only",),
        ("arr_missing", "customer_contract_missing", "customer_name_missing", "security_incident_detail_missing", "privacy_lawsuit_detail_missing"),
        (),
        ("arr_missing", "contract_terms_missing", "customer_undisclosed", "security_incident_detail_missing", "disclosure_confidence_low"),
        ("disclosure_confidence", "arr", "contract_terms", "security_incident", "privacy_lawsuit"),
        "Missing ARR, contract, customer, impairment, lawsuit, or security-incident detail caps Stage 3 confidence.",
    ),
)


ROUND127_CASE_CANDIDATES: tuple[Round127CaseCandidate, ...] = (
    Round127CaseCandidate(
        "douzone_bizon_eqt_cloud_erp_case",
        "B2B_SAAS_ERP_WORKFLOW",
        "012510",
        "Douzone Bizon EQT cloud ERP case",
        "KR",
        "success_candidate",
        None,
        date(2025, 11, 7),
        None,
        None,
        None,
        ("cloud_erp_transition", "b2b_saas_growth", "sme_customer_lock_in", "operating_improvement_plan"),
        ("regulatory_approval_needed", "arr_unverified", "churn_unverified", "event_premium_risk"),
        "b2b_saas_success_candidate_price_backfill_needed",
        "needs_price_backfill",
        ("round_127.md Reuters EQT Douzone Bizon",),
        "EQT deal is useful evidence for B2B SaaS/ERP quality, but ARR, churn, OPM, and FCF still gate Green.",
    ),
    Round127CaseCandidate(
        "palantir_q4_2025_ai_revenue_case",
        "GOVERNMENT_AI_PROGRAM_OF_RECORD",
        "PLTR",
        "Palantir Q4 2025 AI revenue and contract value",
        "US",
        "structural_success",
        None,
        date(2026, 2, 3),
        None,
        None,
        None,
        ("record_revenue", "total_contract_value", "government_revenue_growth", "commercial_revenue_growth", "ontology_workflow_flag", "program_of_record_flag", "auditability_flag", "rule_of_40"),
        ("valuation_saturation", "government_customer_risk", "political_risk"),
        "government_and_commercial_ai_contract_success",
        "needs_price_backfill",
        ("round_127.md MarketWatch Palantir Q4 2025",),
        "AI is treated as structural only because revenue, contract value, government adoption, and commercial workflow evidence are present.",
        (E2RArchetype.ENTERPRISE_AI_ONTOLOGY_WORKFLOW, E2RArchetype.CLOUD_AI_SOFTWARE_INFRA),
    ),
    Round127CaseCandidate(
        "palantir_q1_2026_fastest_growth_case",
        "ENTERPRISE_AI_ONTOLOGY_WORKFLOW",
        "PLTR",
        "Palantir Q1 2026 fastest growth but 4B watch",
        "US",
        "4b_watch",
        None,
        date(2026, 5, 4),
        None,
        date(2026, 5, 4),
        None,
        ("revenue_growth_85pct", "commercial_revenue_growth", "government_revenue_growth", "ontology_workflow_flag"),
        ("after_hours_decline_despite_results", "valuation_saturation", "ai_software_crowding"),
        "ai_software_4b_valuation",
        "needs_price_backfill",
        ("round_127.md MarketWatch Palantir Q1 2026",),
        "Strong revenue can still be 4B-watch when multiple expansion is saturated.",
        (E2RArchetype.AI_SOFTWARE_APPLICATION, E2RArchetype.CROWDED_RERATING_4B_WATCH),
    ),
    Round127CaseCandidate(
        "akamai_frontier_model_ai_cloud_deal_case",
        "EDGE_AI_CLOUD_INFRASTRUCTURE",
        "AKAM",
        "Akamai frontier model AI cloud infrastructure deal",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 8),
        None,
        date(2026, 5, 8),
        None,
        ("edge_cloud_contract_value", "edge_cloud_contract_duration_years", "frontier_model_customer_flag", "cloud_infrastructure_services_revenue"),
        ("customer_disclosed_flag_missing", "cloud_capex_amount_unverified", "ai_customer_concentration", "cdn_legacy_revenue_change"),
        "edge_ai_cloud_contract_aligned_4b_watch",
        "needs_price_backfill",
        ("round_127.md Barrons Akamai frontier model AI cloud deal",),
        "A long AI cloud contract can reframe a legacy CDN business, but margin, capex, customer concentration, and FCF must be checked.",
    ),
    Round127CaseCandidate(
        "akamai_ai_cloud_revenue_contribution_case",
        "EDGE_AI_CLOUD_INFRASTRUCTURE",
        "AKAM",
        "Akamai AI cloud quarterly revenue contribution estimate",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 13),
        None,
        date(2026, 5, 13),
        None,
        ("edge_cloud_contract_value", "cloud_infrastructure_services_revenue", "revenue_contribution", "frontier_model_customer_flag"),
        ("customer_disclosed_flag_missing", "cloud_capex_amount_unverified", "margin_unverified", "ai_customer_concentration"),
        "edge_ai_cloud_revenue_contribution_watch",
        "needs_price_backfill",
        ("round_127.md Barrons Akamai AI cloud revenue contribution",),
        "Estimated quarterly revenue contribution improves Stage 2 evidence, but margin, capex, customer concentration, and FCF still gate promotion.",
    ),
    Round127CaseCandidate(
        "datadog_q1_2026_ai_observability_case",
        "OBSERVABILITY_AI_OPERATIONS",
        "DDOG",
        "Datadog Q1 2026 AI observability",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 7),
        None,
        None,
        None,
        ("observability_revenue_growth", "ai_workload_monitoring", "guidance_raise", "arr_growth"),
        ("cloud_optimization_risk", "net_retention_unverified", "ai_operations_premium_valuation"),
        "observability_ai_aligned",
        "needs_price_backfill",
        ("round_127.md Barrons Datadog observability",),
        "Datadog is a Watch-to-Green candidate only if AI workload monitoring converts into ARR, retention, and FCF.",
    ),
    Round127CaseCandidate(
        "dynatrace_q4_2026_arr_guidance_case",
        "OBSERVABILITY_GUIDANCE_RISK",
        "DT",
        "Dynatrace ARR and guidance risk after earnings beat",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 13),
        ("observability_revenue", "earnings_beat", "subscription_revenue_growth"),
        ("arr_miss_flag", "guidance_miss_flag", "net_new_arr_change", "valuation_compression"),
        "observability_guidance_failed",
        "needs_price_backfill",
        ("round_127.md Barrons Dynatrace ARR guidance risk",),
        "Observability evidence can be real, but ARR/guidance weakness can still break the price path under premium valuation.",
        (E2RArchetype.OBSERVABILITY_AI_OPERATIONS,),
    ),
    Round127CaseCandidate(
        "fortinet_q1_2026_security_billings_case",
        "CYBERSECURITY_AI_THREAT_DEMAND",
        "FTNT",
        "Fortinet Q1 2026 security billings",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 7),
        None,
        None,
        None,
        ("security_billings_growth", "security_arr_growth", "opm_improvement", "renewal_strength"),
        ("outage_risk_unverified", "renewal_rate_unverified", "security_multiple_crowded"),
        "security_billings_aligned_candidate",
        "needs_price_backfill",
        ("round_127.md Barrons Fortinet billings",),
        "Security software can be Watch-to-Green when billings, ARR, renewal, and operational trust are visible together.",
        (E2RArchetype.SECURITY_IDENTITY_DEEPFAKE,),
    ),
    Round127CaseCandidate(
        "cisco_ai_infrastructure_orders_case",
        "AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER",
        "CSCO",
        "Cisco AI infrastructure orders and restructuring watch",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 13),
        None,
        None,
        None,
        ("ai_infrastructure_orders", "hyperscaler_ai_orders", "data_center_switching_orders", "guidance_raise", "software_security_mix"),
        ("restructuring_cost", "workforce_reduction", "legacy_networking_mix", "margin_conversion_unverified"),
        "ai_networking_software_infra_crossover_stage2_restructuring_watch",
        "needs_price_backfill",
        ("round_127.md Reuters Cisco AI infrastructure orders",),
        "AI networking orders support Stage 2 only when orders convert into software/security mix, revenue, margin, and FCF after restructuring costs.",
        (E2RArchetype.AI_NETWORKING_SWITCHING_INFRA, E2RArchetype.CLOUD_AI_SOFTWARE_INFRA),
    ),
    Round127CaseCandidate(
        "netflix_ad_tier_250m_case",
        "STREAMING_AD_PLATFORM",
        "NFLX",
        "Netflix ad tier 250m and privacy watch",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 13),
        None,
        None,
        None,
        ("ad_tier_users", "ad_revenue_growth", "own_adtech_flag", "ad_supported_signup_mix"),
        ("privacy_lawsuit", "dark_pattern_allegation", "ad_arpu_unverified"),
        "streaming_ad_platform_aligned_privacy_watch",
        "needs_price_backfill",
        ("round_127.md The Verge Netflix ad ambitions",),
        "Netflix ad tier can be structural, but privacy/data litigation keeps RedTeam active.",
    ),
    Round127CaseCandidate(
        "trade_desk_revenue_miss_case",
        "ADTECH_PLATFORM_PREMIUM",
        "TTD",
        "The Trade Desk premium valuation revenue miss",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 2, 13),
        ("programmatic_adtech", "ctv_growth", "retail_media_growth"),
        ("revenue_miss", "premium_valuation_miss", "large_drawdown", "growth_slowdown"),
        "adtech_premium_miss",
        "needs_price_backfill",
        ("round_127.md Barron's Trade Desk revenue miss",),
        "Ad-tech can be structural, but premium valuation makes revenue or guide misses a 4C watch.",
    ),
    Round127CaseCandidate(
        "crowdstrike_outage_shareholder_case",
        "SECURITY_OPERATIONAL_TRUST_OVERLAY",
        "CRWD",
        "CrowdStrike outage shareholder case",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 7, 31),
        ("security_arr_platform", "enterprise_customer_base"),
        ("global_outage", "affected_device_count", "shareholder_lawsuit", "trust_damage", "large_drawdown"),
        "security_trust_break_hard_4c",
        "needs_price_backfill",
        ("round_127.md Reuters CrowdStrike shareholder lawsuit",),
        "Security ARR does not protect Stage 3 if operational trust breaks.",
        (E2RArchetype.SECURITY_IDENTITY_DEEPFAKE,),
    ),
    Round127CaseCandidate(
        "kakao_founder_legal_overhang_case",
        "PLATFORM_GOVERNANCE_LEGAL_RISK",
        "035720",
        "Kakao founder legal overhang and acquittal",
        "KR",
        "4b_watch",
        None,
        date(2024, 7, 1),
        None,
        date(2025, 10, 21),
        None,
        ("platform_assets", "messenger_ecosystem", "legal_overhang_resolved_by_acquittal"),
        ("founder_legal_case", "mna_legal_dispute", "governance_discount", "regulatory_investigation"),
        "legal_overhang_watch_resolved_by_acquittal",
        "needs_price_backfill",
        ("round_127.md Reuters Kakao founder legal case",),
        "Platform moat is not enough while founder/M&A legal overhang pressures the valuation frame.",
    ),
    Round127CaseCandidate(
        "roblox_safety_forecast_cut_case",
        "UGC_GAME_PLATFORM_SAFETY",
        "RBLX",
        "Roblox safety measures and forecast cut",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 1),
        ("ugc_game_platform", "user_growth"),
        ("child_safety_regulation", "age_verification_friction", "bookings_forecast_cut", "user_growth_slowdown"),
        "ugc_platform_safety_4c",
        "needs_price_backfill",
        ("round_127.md Reuters Roblox safety forecast cut",),
        "UGC game platforms cannot be scored on user scale alone when safety controls cut bookings.",
    ),
    Round127CaseCandidate(
        "take_two_gta_preorder_rumor_case",
        "SINGLE_IP_RELEASE_EVENT_PREMIUM",
        "TTWO",
        "Take-Two GTA VI preorder rumor",
        "US",
        "event_premium",
        None,
        None,
        None,
        date(2026, 5, 14),
        None,
        ("single_ip_large_title", "preorder_event_flag", "release_expectation"),
        ("single_ip_revenue_ratio", "bookings_unverified", "release_risk"),
        "single_ip_event_premium",
        "needs_price_backfill",
        ("round_127.md GTA VI preorder rumor",),
        "Preorder rumors can move price, but they are not recurring IP portfolio evidence before bookings and launch quality are visible.",
    ),
    Round127CaseCandidate(
        "wpp_ad_forecast_cut_case",
        "MEDIA_AD_CONTENT_CYCLE",
        "WPP",
        "WPP global ad forecast cut",
        "UK",
        "4b_watch",
        None,
        None,
        None,
        date(2025, 6, 9),
        None,
        ("traditional_ad_agency", "global_ad_revenue"),
        ("client_budget_cut", "trade_uncertainty", "ad_growth_forecast_cut"),
        "traditional_ad_agency_4c_watch",
        "needs_price_backfill",
        ("round_127.md Reuters WPP ad forecast cut",),
        "Ad recovery is cyclical unless budget resilience and structural ad-tech economics are proven.",
    ),
    Round127CaseCandidate(
        "netflix_texas_privacy_lawsuit_case",
        "PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY",
        "NFLX",
        "Netflix Texas privacy lawsuit",
        "US",
        "4b_watch",
        None,
        None,
        None,
        date(2026, 5, 11),
        None,
        ("streaming_ad_platform", "ad_tier_users", "own_adtech_flag"),
        ("privacy_lawsuit", "dark_pattern_allegation", "child_data_collection_flag", "platform_trust_damage"),
        "platform_legal_overhang_privacy_4c_watch",
        "needs_price_backfill",
        ("round_127.md Reuters Netflix Texas privacy lawsuit",),
        "Streaming ad growth remains RedTeam-constrained when privacy and dark-pattern allegations affect platform trust.",
        (E2RArchetype.STREAMING_AD_PLATFORM,),
    ),
    Round127CaseCandidate(
        "meta_scam_ads_lawsuit_case",
        "PLATFORM_AD_TRUST_OVERLAY",
        "META",
        "Meta scam ads lawsuit",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 11),
        ("ad_platform_scale", "ai_ad_targeting"),
        ("scam_ad_lawsuit", "consumer_protection_lawsuit", "ad_quality_risk", "platform_trust_damage"),
        "platform_ad_trust_4c_watch",
        "needs_price_backfill",
        ("round_127.md Reuters Meta scam ads lawsuit",),
        "Ad revenue must pass a quality filter; scam-ad allegations are RedTeam evidence.",
        (E2RArchetype.MEDIA_AD_CONTENT_CYCLE, E2RArchetype.PLATFORM_SOFTWARE_INTERNET),
    ),
    Round127CaseCandidate(
        "meta_youth_safety_trial_case",
        "PLATFORM_PRIVACY_YOUTH_SAFETY_OVERLAY",
        "META",
        "Meta youth safety trial",
        "US",
        "4b_watch",
        None,
        None,
        None,
        date(2026, 5, 13),
        None,
        ("platform_scale", "ad_platform_scale"),
        ("youth_safety_lawsuit", "age_verification_friction", "algorithm_modification", "platform_design_risk"),
        "youth_safety_platform_risk",
        "needs_price_backfill",
        ("round_127.md Reuters Meta youth safety trial",),
        "Large-platform growth must be discounted when youth safety remedies can change product mechanics.",
        (E2RArchetype.PLATFORM_SOFTWARE_INTERNET,),
    ),
    Round127CaseCandidate(
        "legacy_saas_ai_disruption_case",
        "LEGACY_SAAS_AI_DISRUPTION_OVERLAY",
        "LEGACY_SAAS_REF",
        "Legacy SaaS AI disruption versus reinforcement watch",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 14),
        ("ai_agent_launch", "legacy_saas_seat_model", "workflow_ai_feature"),
        ("ai_substitutes_existing_seat_model", "license_downsell", "gross_margin_pressure", "agent_cost_overrun", "workflow_lockin_failure"),
        "legacy_saas_ai_disruption",
        "missing_direct_symbol_mapping",
        ("round_127.md Reuters Breakingviews SaaSpocalypse",),
        "Legacy SaaS AI must prove reinforcement, not seat/license cannibalization.",
        (E2RArchetype.AI_SOFTWARE_APPLICATION,),
    ),
    Round127CaseCandidate(
        "salesforce_agentforce_arr_case",
        "LEGACY_SAAS_AI_REINFORCEMENT",
        "CRM",
        "Salesforce Agentforce ARR but mix and margin verification needed",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 14),
        None,
        None,
        None,
        ("ai_arr", "ai_attach_rate", "agentforce_like_arr", "workflow_ai_feature"),
        ("ai_arr_too_small", "seat_churn_unverified", "gross_margin_impact_unverified", "agent_cost_overrun_risk"),
        "legacy_saas_ai_reinforcement_watch",
        "needs_price_backfill",
        ("round_127.md Reuters Breakingviews SaaSpocalypse",),
        "Agent ARR is useful Stage 2 evidence, but total mix, seat churn, gross margin, and workflow lock-in still gate promotion.",
        (E2RArchetype.AI_SOFTWARE_APPLICATION, E2RArchetype.LEGACY_SAAS_AI_DISRUPTION_OVERLAY),
    ),
)


ROUND127_PRICE_FIELDS: tuple[str, ...] = (
    "case_id",
    "symbol",
    "company_name",
    "primary_archetype",
    "secondary_archetypes",
    "stage1_date",
    "stage2_date",
    "stage3_date",
    "stage4b_date",
    "stage4c_date",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_price",
    "peak_date",
    "MFE_30D",
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_30D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "drawdown_after_peak",
    "below_stage2_price_flag",
    "below_stage3_price_flag",
    "arr_growth",
    "subscription_revenue_growth",
    "recurring_revenue_ratio",
    "churn_rate",
    "net_retention_rate",
    "customer_count",
    "large_customer_concentration",
    "op_margin_change",
    "fcf_margin",
    "ai_revenue_contribution",
    "ai_arr",
    "ai_attach_rate",
    "ai_contract_value",
    "total_contract_value",
    "rule_of_40",
    "compute_cost_ratio",
    "model_dependency_flag",
    "ai_workflow_integration_flag",
    "ontology_workflow_flag",
    "auditability_flag",
    "program_of_record_flag",
    "government_program_budget_flag",
    "maven_or_defense_ai_flag",
    "revenue_per_employee",
    "government_revenue_growth",
    "commercial_revenue_growth",
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
    "sre_agent_revenue_flag",
    "security_analyst_agent_flag",
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
    "daily_active_users",
    "monthly_active_users",
    "communication_engagement_change",
    "single_ip_revenue_ratio",
    "game_delay_flag",
    "preorder_event_flag",
    "platform_safety_flag",
    "age_verification_flag",
    "content_monitoring_flag",
    "regulatory_ban_flag",
    "ad_revenue_growth",
    "ad_arpu",
    "ad_tier_users",
    "ad_supported_signup_mix",
    "own_adtech_flag",
    "client_budget_cut_flag",
    "ad_growth_forecast_cut",
    "ai_production_disruption_flag",
    "privacy_lawsuit_flag",
    "scam_ad_lawsuit_flag",
    "ad_quality_risk_flag",
    "high_risk_ad_revenue_estimate",
    "child_data_collection_flag",
    "dark_pattern_allegation_flag",
    "autoplay_restriction_flag",
    "security_billings_growth",
    "security_arr_growth",
    "ai_threat_demand_flag",
    "sase_revenue_growth",
    "firewall_revenue_growth",
    "security_outage_flag",
    "affected_device_count",
    "customer_lawsuit_flag",
    "shareholder_lawsuit_flag",
    "renewal_rate",
    "incident_recovery_days",
    "trust_damage_flag",
    "founder_legal_case_flag",
    "governance_overhang_flag",
    "mna_legal_dispute_flag",
    "regulatory_investigation_flag",
    "youth_safety_lawsuit_flag",
    "age_verification_order_flag",
    "algorithm_modification_order_flag",
    "addictive_design_claim_flag",
    "infinite_scroll_restriction_flag",
    "antitrust_lawsuit_flag",
    "copyright_lawsuit_flag",
    "training_data_risk_flag",
    "license_risk_flag",
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
    "price_validation_status",
    "review_notes",
)


ROUND127_RISK_OVERLAYS: tuple[str, ...] = (
    "AI_SOFTWARE_REVENUE_ALIGNED",
    "GOVERNMENT_AI_PROGRAM_ALIGNED",
    "AI_SOFTWARE_4B_VALUATION",
    "B2B_SAAS_STRUCTURAL_SUCCESS",
    "ENTERPRISE_AI_WORKFLOW_ALIGNED",
    "LEGACY_SAAS_AI_REINFORCEMENT",
    "LEGACY_SAAS_AI_DISRUPTION",
    "EDGE_AI_CLOUD_CONTRACT_ALIGNED",
    "OBSERVABILITY_AI_ALIGNED",
    "OBSERVABILITY_GUIDANCE_FAILED",
    "CYBERSECURITY_AI_THREAT_DEMAND_ALIGNED",
    "AI_NETWORKING_SOFTWARE_INFRA_CROSSOVER_STAGE2_RESTRUCTURING_WATCH",
    "STREAMING_AD_PLATFORM_ALIGNED",
    "ADTECH_PREMIUM_MISS",
    "SECURITY_TRUST_BREAK",
    "UGC_PLATFORM_SAFETY_4C",
    "SINGLE_IP_EVENT_PREMIUM",
    "PLATFORM_LEGAL_OVERHANG",
    "SCAM_AD_TRUST_BREAK",
    "PRIVACY_YOUTH_SAFETY_GATE",
    "DISCLOSURE_CONFIDENCE_CAP",
)


def round127_target_for(target_id: str) -> Round127ScoreTarget | None:
    for target in ROUND127_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round127_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND127_CASE_CANDIDATES:
        target = round127_target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
        stage4b_evidence = candidate.evidence_fields if candidate.case_type == "4b_watch" or candidate.stage4b_date else ()
        stage4c_evidence = candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" or candidate.stage4c_date else ()
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market=candidate.market,
            sector_raw=candidate.target_id,
            primary_archetype=target.canonical_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=target.large_sector.value,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                f"Round127 R8 Loop-7 case for {candidate.target_id}; "
                "user count, AI feature, game title, ad-cycle, and security-demand narratives are separated from repeat revenue and trust evidence."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage2_signals or field in target.green_conditions),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage3_conditions),
            stage4b_evidence=stage4b_evidence,
            stage4c_evidence=stage4c_evidence,
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"failed_rerating", "event_premium", "overheat", "4b_watch", "4c_thesis_break", "one_off"}
                else None
            ),
            score_price_alignment=_score_price_alignment(candidate),
            rerating_result=_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint=_score_weight_hint(target),
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_cross_evidence_for_green",
                "user_count_is_not_green_evidence_alone",
                "ai_feature_is_not_revenue",
                "new_title_expectation_is_not_bookings",
                "security_demand_is_not_operational_trust",
                "ad_revenue_must_pass_quality_filter",
                "arr_arpu_bookings_opm_fcf_churn_and_legal_stability_required_for_green",
                "do_not_invent_arr_arpu_bookings_churn_fcf_customer_damage_lawsuit_or_stage_prices",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.75 if candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.2,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round127_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND127_SCORE_TARGETS:
        weights = target.score_weight.as_dict()
        rows.append(
            {
                "target_id": target.target_id,
                "large_sector": target.large_sector.value,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "eps_fcf": str(weights["eps_fcf"]),
                "structural_visibility": str(weights["structural_visibility"]),
                "bottleneck_pricing": str(weights["bottleneck_pricing"]),
                "market_mispricing": str(weights["market_mispricing"]),
                "valuation": str(weights["valuation"]),
                "capital_allocation": str(weights["capital_allocation"]),
                "information_confidence": str(weights["information_confidence"]),
                "stage1_signals": "|".join(target.stage1_signals),
                "stage2_signals": "|".join(target.stage2_signals),
                "stage3_conditions": "|".join(target.stage3_conditions),
                "stage4b_conditions": "|".join(target.stage4b_conditions),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "loop7_penalty_axes": "|".join(target.loop7_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round127_base_score_axis_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "axis_id": axis.axis_id,
            "weight": str(axis.weight),
            "stage2_evidence": "|".join(axis.stage2_evidence),
            "stage3_evidence": "|".join(axis.stage3_evidence),
            "hard_redteam": "|".join(axis.hard_redteam),
            "normalization_point": axis.normalization_point,
            "production_scoring_changed": "false",
        }
        for axis in ROUND127_BASE_SCORE_AXES
    )


def round127_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND127_CASE_CANDIDATES:
        target = round127_target_for(candidate.target_id)
        assert target is not None
        rows.append(
            {
                "case_id": candidate.case_id,
                "target_id": candidate.target_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "market": candidate.market,
                "case_type": candidate.case_type,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "stage1_date": candidate.stage1_date.isoformat() if candidate.stage1_date else "",
                "stage2_date": candidate.stage2_date.isoformat() if candidate.stage2_date else "",
                "stage3_date": candidate.stage3_date.isoformat() if candidate.stage3_date else "",
                "stage4b_date": candidate.stage4b_date.isoformat() if candidate.stage4b_date else "",
                "stage4c_date": candidate.stage4c_date.isoformat() if candidate.stage4c_date else "",
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "alignment_hint": candidate.alignment_hint,
                "price_validation_status": candidate.price_validation_status,
                "production_input": "false",
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round127_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "red_flags": "|".join(target.red_flags),
            "loop7_penalty_axes": "|".join(target.loop7_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND127_SCORE_TARGETS
    )


def round127_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round127_backfill": "true"} for field in ROUND127_PRICE_FIELDS)


def round127_summary() -> dict[str, int | bool]:
    records = round127_case_records()
    return {
        "target_count": len(ROUND127_SCORE_TARGETS),
        "base_score_axis_count": len(ROUND127_BASE_SCORE_AXES),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND127_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND127_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND127_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND127_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round127_r8_loop7_reports(
    *,
    output_directory: str | Path = ROUND127_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND127_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND127_DEFAULT_SCORE_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = Path(cases_path)
    score_profiles = Path(score_profile_path)
    cases.parent.mkdir(parents=True, exist_ok=True)
    score_profiles.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "score_profiles": score_profiles,
        "summary": output / "round127_r8_loop7_platform_content_sw_security_summary.md",
        "case_matrix": output / "round127_r8_loop7_case_matrix.csv",
        "stage_date_plan": output / "round127_r8_loop7_stage_date_plan.csv",
        "base_score_axes": output / "round127_r8_loop7_base_score_axes.csv",
        "green_guardrails": output / "round127_r8_loop7_green_guardrails.md",
        "risk_overlays": output / "round127_r8_loop7_risk_overlays.md",
        "price_validation_plan": output / "round127_r8_loop7_price_validation_plan.md",
        "price_fields": output / "round127_r8_loop7_price_fields.csv",
    }
    _write_case_jsonl(round127_case_records(), cases)
    _write_rows(round127_score_profile_rows(), score_profiles)
    _write_rows(round127_base_score_axis_rows(), paths["base_score_axes"])
    _write_rows(round127_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round127_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round127_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round127_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round127_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round127_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round127_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round127_summary_markdown() -> str:
    summary = round127_summary()
    lines = [
        "# Round 127 R8 Loop-7 Platform/Content/SW/Security Summary",
        "",
        "Round 127 is calibration material only. It does not change production scoring.",
        "",
        "## Counts",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Core Rule",
            "",
            "User count, AI feature launches, new-title expectations, ad-cycle recovery, cybersecurity demand, NFT, and metaverse tags are not Stage 3 evidence by themselves.",
            "Green requires repeat revenue evidence such as ARR, ARPU, bookings, OPM, FCF, low churn, operational trust, legal stability, and ad-quality confidence.",
            "",
            "## R8 v7 Base Score Axes",
            "",
        ]
    )
    for axis in ROUND127_BASE_SCORE_AXES:
        lines.append(f"- {axis.axis_id}: {axis.weight}점 / {axis.normalization_point}")
    lines.extend(
        [
            "",
            "Example: an AI product launch is Stage 1 evidence. A paid enterprise contract with recurring usage, controlled compute cost, and FCF conversion can support higher stages.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round127_green_guardrail_markdown() -> str:
    lines = [
        "# Round 127 R8 Loop-7 Green Guardrails",
        "",
        "- Do not apply R8 Loop-7 v7.0 weights to production scoring yet.",
        "- Do not use case records as candidate-generation input.",
        "- Do not treat user count, AI feature, new game title, ad recovery, security demand, NFT, or metaverse theme as Green evidence alone.",
        "- Require repeat revenue, ARR/ARPU/bookings, OPM, FCF, low churn, customer retention, operational trust, and legal stability for Green.",
        "- Scam ads, privacy lawsuits, youth-safety issues, founder legal cases, security outages, and single-title delays are RedTeam gates.",
        "- Do not invent ARR, ARPU, bookings, churn, FCF, customer-damage, lawsuit, or stage-price fields.",
        "",
        "간단한 예시: 보안 회사가 ARR이 커도 전 세계 장애와 대형 고객 소송이 생기면 Green 유지가 아니라 4C 확인 대상입니다.",
    ]
    return "\n".join(lines) + "\n"


def render_round127_risk_overlay_markdown() -> str:
    lines = ["# Round 127 R8 Loop-7 Risk Overlays", ""]
    for overlay in ROUND127_RISK_OVERLAYS:
        lines.append(f"- {overlay}")
    lines.extend(
        [
            "",
            "These overlays are diagnostic calibration labels. They are not production score inputs.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round127_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 127 R8 Loop-7 Price Validation Plan",
        "",
        "For every case, backfill stage prices and forward MFE/MAE before applying score-weight changes.",
        "",
        "## Priority Cases",
    ]
    for row in round127_case_candidate_rows():
        stage_date = row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or row["stage1_date"] or "date_needed"
        lines.append(f"- {row['case_id']}: {stage_date} / {row['alignment_hint']}")
    lines.extend(
        [
            "",
            "## Required Validation Fields",
            "",
            ", ".join(ROUND127_PRICE_FIELDS),
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round127CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "aligned"
    if candidate.case_type in {"4c_thesis_break", "failed_rerating", "overheat"}:
        return "false_positive_score"
    if candidate.case_type == "event_premium":
        return "price_moved_without_evidence"
    return "unknown"


def _rerating_result(candidate: Round127CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "4b_watch":
        return "unknown"
    if candidate.case_type == "event_premium":
        return "event_premium"
    return "unknown"


def _score_weight_hint(target: Round127ScoreTarget) -> dict[str, float]:
    weights = target.score_weight.as_dict()
    return {
        "eps_fcf": _numeric_weight(weights["eps_fcf"]),
        "visibility": _numeric_weight(weights["structural_visibility"]),
        "bottleneck": _numeric_weight(weights["bottleneck_pricing"]),
        "mispricing": _numeric_weight(weights["market_mispricing"]),
        "valuation": _numeric_weight(weights["valuation"]),
        "capital_allocation": _numeric_weight(weights["capital_allocation"]),
    }


def _numeric_weight(value: int | str) -> float:
    if isinstance(value, int):
        return float(value)
    return 0.0


def _write_case_jsonl(records: Iterable[E2RCaseRecord], path: Path) -> None:
    with path.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record.as_dict(), ensure_ascii=False, sort_keys=True))
            fh.write("\n")


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> None:
    rows = tuple(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
