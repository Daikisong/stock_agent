"""Round-27 cases_v09 expansion and score-weight v1.2 hypotheses.

Round 27 adds thinner archetypes and false-success boundaries for games,
medical devices, medical AI, retail/e-commerce, education, telecom/grid
infrastructure, and selected already-important Green-possible families.
It is report-only calibration material. Production feature engineering,
scoring, staging, and RedTeam code must not import this module.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import CaseDataQuality, E2RCaseRecord, PriceValidation
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture


ROUND27_SOURCE_ROUND_PATH = "docs/round/round_27.md"
ROUND27_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round27_score_weight_v12"
ROUND27_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v09_round27.jsonl"
ROUND27_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round27_v12.csv"


@dataclass(frozen=True)
class Round27ScoreWeightDraft:
    eps_fcf: int
    structural_visibility: int
    bottleneck_pricing: int
    market_mispricing: int
    valuation: int
    capital_allocation: int = 0
    information_confidence: int = 5

    def as_dict(self) -> dict[str, int]:
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
class Round27ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round27ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    normalization_point: str

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round27CaseCandidate:
    case_id: str
    target_id: str
    symbol: str
    company_name: str
    market: str
    case_type: str
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND27_SCORE_TARGETS: tuple[Round27ScoreTarget, ...] = (
    Round27ScoreTarget(
        "GAME_CONTENT_IP",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.GAME_CONTENT_IP,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round27ScoreWeightDraft(20, 18, 6, 14, 12, 0, 5),
        ("new_game_launch", "global_ip", "downloads_or_traffic", "regional_expansion"),
        ("monetization_confirmed", "op_eps_revision", "regional_diversification", "retention_low_churn"),
        ("repeat_ip_monetization", "platform_or_region_diversified", "op_fcf_visible", "regulation_risk_low"),
        ("repeat_ip_monetization", "monetization_confirmed", "regional_diversification", "op_eps_revision", "regulation_risk_low"),
        ("hit_driven", "regulation", "data_security", "single_ip_dependency", "download_only"),
        ("regulatory_ban", "data_security_issue", "new_game_revenue_miss", "single_ip_decline"),
        "Games are Watch-first: downloads and launch hype are not enough without monetization, OP, and regulation checks.",
    ),
    Round27ScoreTarget(
        "MEDICAL_DEVICE_HEALTHCARE_EXPORT",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round27ScoreWeightDraft(20, 22, 13, 14, 12, 0, 5),
        ("export_country_expansion", "aesthetic_device_demand", "approval", "procedure_growth"),
        ("recurring_consumables_or_procedure", "opm_roe_improvement", "channel_quality", "approval_stable"),
        ("repeat_procedure_revenue", "export_channel_scale", "fcf_conversion", "asp_resilience"),
        ("export_country_expansion", "recurring_consumables_or_procedure", "opm_roe_improvement", "approval_stable", "channel_quality"),
        ("approval", "safety", "counterfeit", "channel_quality", "competition", "single_device_no_consumable"),
        ("approval_delay", "safety_issue", "counterfeit_issue", "asp_drop", "no_recurring_revenue"),
        "Medical devices can be Green when exports, recurring procedure/consumables, OPM, and regulatory quality are source-backed.",
    ),
    Round27ScoreTarget(
        "DIGITAL_HEALTHCARE_AI",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.BIOTECH_REGULATORY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round27ScoreWeightDraft(18, 17, 8, 13, 12, 0, 7),
        ("external_clinical_validation", "medical_imaging_ai", "workflow_poc", "diagnostic_ai_paper"),
        ("approval_or_clearance", "hospital_adoption", "reimbursement_or_paid_usage", "revenue_conversion"),
        ("validated_workflow", "paid_repeat_usage", "liability_risk_low", "op_fcf_conversion"),
        ("external_clinical_validation", "approval_or_clearance", "hospital_adoption", "reimbursement_or_paid_usage", "revenue_conversion"),
        ("regulation", "reimbursement", "clinical_validation", "subgroup_bias", "liability", "poc_only"),
        ("liability_claim", "subgroup_performance_failure", "reimbursement_failure", "clinical_validation_gap"),
        "Medical AI is Watch-to-Green: papers and AUROC are Stage 1/2 until paid clinical workflow appears.",
    ),
    Round27ScoreTarget(
        "RETAIL_ECOMMERCE_LOGISTICS",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round27ScoreWeightDraft(18, 16, 5, 13, 14, 3, 5),
        ("store_count", "logistics_scale", "same_store_sales", "online_traffic"),
        ("opm_improvement", "inventory_normalized", "logistics_cost_stable", "repeat_customer_or_store_efficiency"),
        ("fcf_improvement", "cost_leverage", "supplier_risk_low", "data_security_intact"),
        ("opm_improvement", "inventory_normalized", "logistics_cost_stable", "fcf_improvement", "regulation_risk_low"),
        ("logistics_cost", "inventory", "supplier_regulation", "data_security", "competition", "sales_without_fcf"),
        ("supplier_regulation", "data_breach", "logistics_cost_spike", "fcf_deterioration"),
        "Retail and e-commerce are OPM/FCF stories, not store-count or GMV stories.",
    ),
    Round27ScoreTarget(
        "EDUCATION_SPECIALTY_SERVICES",
        Round10LargeSector.EDUCATION_LIFE_AGRI_MISC,
        E2RArchetype.EDUCATION_SPECIALTY_SERVICES,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round27ScoreWeightDraft(18, 17, 5, 12, 12, 2, 5),
        ("repeat_course_demand", "adult_education", "b2b_training", "online_learning"),
        ("subscription_or_repeat_enrollment", "opm_improvement", "birthrate_risk_offset", "policy_risk_low"),
        ("adult_or_b2b_mix", "recurring_course_revenue", "fcf_conversion", "offline_fixed_cost_low"),
        ("adult_or_b2b_mix", "subscription_or_repeat_enrollment", "opm_improvement", "policy_risk_low", "birthrate_risk_offset"),
        ("birthrate", "regulation", "ai_substitution", "offline_fixed_cost", "entrance_exam_theme_only"),
        ("regulation_change", "birthrate_demand_decline", "offline_cost_pressure", "ai_substitution"),
        "Education stays Watch-first unless adult/B2B/overseas repeat revenue offsets birthrate and regulation risk.",
    ),
    Round27ScoreTarget(
        "TELECOM_GRID_AI_NETWORK",
        Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round27ScoreWeightDraft(17, 18, 12, 12, 10, 2, 5),
        ("smart_grid", "fiber_network", "5g_6g_policy", "ai_datacenter_grid_need"),
        ("equipment_order", "datacenter_or_grid_capex_link", "long_term_capex_visibility", "op_eps_conversion"),
        ("direct_grid_or_network_order", "margin_visibility", "project_delay_low", "capex_recovery_visible"),
        ("equipment_order", "datacenter_or_grid_capex_link", "long_term_capex_visibility", "op_eps_conversion", "regulation_risk_low"),
        ("capex_burden", "regulation", "project_delay", "low_margin_equipment", "policy_keyword_only"),
        ("project_delay", "capex_burden", "regulatory_recovery_failure", "low_margin_delivery"),
        "Telecom/grid/network needs actual orders and OP conversion; 5G/6G or smart-grid words are routing tags only.",
    ),
    Round27ScoreTarget(
        "AI_DATA_CENTER_COOLING",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round27ScoreWeightDraft(21, 22, 22, 13, 12, 0, 5),
        ("liquid_cooling_keyword", "hvac_acquisition", "high_density_server_heat", "ai_datacenter_capex"),
        ("customer_datacenter_capex_link", "confirmed_order_or_delivery", "cooling_bottleneck", "op_eps_revision"),
        ("delivery_or_service_revenue", "cooling_bottleneck_position", "repeat_service_revenue", "direct_capex_link"),
        ("customer_datacenter_capex_link", "confirmed_order_or_delivery", "cooling_bottleneck", "repeat_service_revenue", "op_eps_revision"),
        ("ai_capex_delay", "low_margin_project", "customer_concentration", "no_customer_order"),
        ("ai_capex_delay", "project_margin_damage", "customer_order_delay", "service_attach_failure"),
        "AI cooling remains Green-possible only when bottleneck evidence becomes orders, delivery, service revenue, and OP revision.",
    ),
    Round27ScoreTarget(
        "SECURITY_IDENTITY_DEEPFAKE",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round27ScoreWeightDraft(20, 20, 10, 14, 13, 0, 5),
        ("security_threat_growth", "deepfake_regulation", "identity_demand", "government_security_budget"),
        ("recurring_subscription", "customer_retention", "opm_improvement", "enterprise_or_government_contract"),
        ("mission_critical_lock_in", "low_churn", "customer_diversification", "fcf_conversion"),
        ("recurring_subscription", "low_churn", "customer_diversification", "opm_improvement", "no_major_outage"),
        ("operational_trust", "outage", "legal", "contract_absence", "customer_retention"),
        ("major_outage", "legal_claim", "customer_churn", "contract_loss", "trust_break"),
        "Security can be structural, but operational trust failure is hard 4C-style evidence.",
    ),
    Round27ScoreTarget(
        "CLOUD_AI_SOFTWARE_INFRA",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round27ScoreWeightDraft(20, 23, 8, 16, 14, 0, 5),
        ("cloud_transition", "erp_saas_demand", "ai_feature_launch", "b2b_customer_growth"),
        ("recurring_revenue_growth", "arpu_up", "opm_improvement", "retention_confirmed"),
        ("customer_lock_in", "fcf_conversion", "pricing_power", "old_si_or_legacy_software_frame"),
        ("recurring_revenue", "arpu", "retention", "opm_or_fcf_improvement", "ai_cost_control"),
        ("ai_feature_only", "ai_cost_overrun", "churn", "si_revenue_only", "opm_decline"),
        ("churn", "ai_cost_overrun", "opm_decline", "competition_intensifies"),
        "Cloud/SaaS can be Green, but AI wording is not evidence without paid usage, OPM, and FCF.",
    ),
    Round27ScoreTarget(
        "INSURANCE_UNDERWRITING_CYCLE",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round27ScoreWeightDraft(15, 21, 4, 15, 25, 10, 5),
        ("low_pbr", "value_up_disclosure", "loss_ratio_improvement", "dividend_or_buyback_expectation"),
        ("roe_improvement", "csm_growth", "capital_ratio_stable", "shareholder_return_execution"),
        ("pbr_roe_frame_change", "repeat_shareholder_return", "underwriting_profit_stable", "credit_risk_low"),
        ("roe_improvement", "csm_or_loss_ratio_stability", "capital_ratio_stable", "shareholder_return_execution", "credit_risk_low"),
        ("underwriting", "capital_ratio", "cyber_operational", "credit_cost", "low_pbr_only"),
        ("loss_ratio_worsens", "capital_ratio_down", "cyber_operational_risk", "credit_cost_up", "shareholder_return_retreat"),
        "Insurance remains a PBR-ROE-return rerating archetype, not an EPS explosion archetype.",
    ),
)


ROUND27_CASE_CANDIDATES: tuple[Round27CaseCandidate, ...] = (
    Round27CaseCandidate("krafton_bgmi_india_ip_candidate", "GAME_CONTENT_IP", "259960", "Krafton BGMI India IP", "KR", "success_candidate", ("global_ip", "india_user_base", "monetization_potential"), ("regulation", "single_ip_dependency"), "BGMI is a game/IP candidate only if monetization and regulatory stability are verified."),
    Round27CaseCandidate("bgmi_regulatory_ban_risk_counterexample", "GAME_CONTENT_IP", "BGMI_BAN", "BGMI regulatory ban risk", "KR", "failed_rerating", ("downloads_or_traffic",), ("regulatory_ban", "data_security"), "Download scale can be offset by ban or data-security risk."),
    Round27CaseCandidate("new_game_hype_no_revenue_counterexample", "GAME_CONTENT_IP", "GAME_HYPE", "신작기대_무매출", "KR", "failed_rerating", ("new_game_launch",), ("no_revenue", "launch_hype_only"), "New-game hype is not score evidence before revenue appears."),
    Round27CaseCandidate("single_ip_dependency_4c", "GAME_CONTENT_IP", "SINGLE_IP_4C", "단일IP의존4C", "KR", "4c_thesis_break", ("single_ip_revenue",), ("single_ip_decline", "new_game_revenue_miss"), "Single-IP decline can break the game-content thesis."),
    Round27CaseCandidate("classys_aesthetic_device_export_candidate", "MEDICAL_DEVICE_HEALTHCARE_EXPORT", "214150", "Classys aesthetic device export", "KR", "success_candidate", ("export_country_expansion", "aesthetic_device_demand"), ("approval_delay", "competition"), "Medical-device export candidate needs recurring procedure or consumables and OPM evidence."),
    Round27CaseCandidate("hugel_botox_us_approval_candidate", "MEDICAL_DEVICE_HEALTHCARE_EXPORT", "145020", "Hugel Botox US approval", "KR", "success_candidate", ("approval", "export_market_entry"), ("safety", "counterfeit"), "Approval can support Stage 2, but channel quality and safety must stay clean."),
    Round27CaseCandidate("botox_counterfeit_safety_risk_4c", "MEDICAL_DEVICE_HEALTHCARE_EXPORT", "BOTOX_FAKE_4C", "Botox counterfeit safety risk", "US", "4c_thesis_break", ("aesthetic_treatment_demand",), ("counterfeit_issue", "safety_issue"), "Counterfeit or safety issue is hard 4C-style evidence."),
    Round27CaseCandidate("single_device_no_consumable_counterexample", "MEDICAL_DEVICE_HEALTHCARE_EXPORT", "SINGLE_DEVICE", "단일장비_소모품부재", "KR", "failed_rerating", ("device_sales",), ("single_device_no_consumable", "no_recurring_revenue"), "Device sales without recurring procedure/consumables have weak visibility."),
    Round27CaseCandidate("mammography_ai_external_validation_candidate", "DIGITAL_HEALTHCARE_AI", "MAMMO_AI", "Mammography AI external validation", "US", "success_candidate", ("external_clinical_validation", "medical_imaging_ai"), ("subgroup_bias", "no_reimbursement"), "External validation is useful but not Green without paid workflow."),
    Round27CaseCandidate("lunit_subgroup_performance_risk_counterexample", "DIGITAL_HEALTHCARE_AI", "LUNIT_SUBGROUP", "Lunit subgroup performance risk", "KR", "failed_rerating", ("clinical_ai_model",), ("subgroup_performance_failure", "clinical_validation_gap"), "High aggregate AUC can hide subgroup weakness."),
    Round27CaseCandidate("hospital_ai_no_reimbursement_counterexample", "DIGITAL_HEALTHCARE_AI", "MED_AI_NO_PAY", "병원AI_수가부재", "KR", "failed_rerating", ("hospital_adoption_poc",), ("no_reimbursement", "no_paid_usage"), "Hospital AI without reimbursement or paid usage stays Watch."),
    Round27CaseCandidate("medical_ai_liability_risk_4c", "DIGITAL_HEALTHCARE_AI", "MED_AI_LIABILITY", "의료AI책임리스크", "KR", "4c_thesis_break", ("medical_ai_response",), ("liability_claim", "clinical_validation_gap"), "Liability or clinical validation failure can break medical AI."),
    Round27CaseCandidate("cu_gs25_store_efficiency_candidate", "RETAIL_ECOMMERCE_LOGISTICS", "CONV_STORE", "CU/GS25 store efficiency", "KR", "success_candidate", ("same_store_sales", "store_efficiency", "pb_mix"), ("competition", "labor_cost"), "Store count is not evidence; store efficiency and OPM are."),
    Round27CaseCandidate("coupang_logistics_scale_candidate", "RETAIL_ECOMMERCE_LOGISTICS", "CPNG", "Coupang logistics scale", "US", "success_candidate", ("logistics_scale", "repeat_customer_base"), ("supplier_regulation", "data_security"), "Logistics scale candidate needs FCF and regulatory checks."),
    Round27CaseCandidate("coupang_supplier_regulation_risk_4c", "RETAIL_ECOMMERCE_LOGISTICS", "CPNG_SUPPLIER_4C", "Coupang supplier regulation risk", "US", "4c_thesis_break", ("platform_scale",), ("supplier_regulation", "payment_delay"), "Supplier pressure can invalidate margin quality."),
    Round27CaseCandidate("coupang_data_breach_4c", "RETAIL_ECOMMERCE_LOGISTICS", "CPNG_BREACH_4C", "Coupang data breach", "US", "4c_thesis_break", ("ecommerce_customer_base",), ("data_breach", "trust_break"), "Data breach is hard 4C-style evidence for e-commerce platforms."),
    Round27CaseCandidate("adult_education_subscription_candidate", "EDUCATION_SPECIALTY_SERVICES", "ADULT_EDU", "성인교육구독", "KR", "success_candidate", ("adult_education", "subscription_or_repeat_enrollment"), ("ai_substitution", "policy_risk"), "Adult/B2B education can offset birthrate risk if repeat revenue is visible."),
    Round27CaseCandidate("hagwon_demand_candidate", "EDUCATION_SPECIALTY_SERVICES", "HAGWON_DEMAND", "학원수요", "KR", "success_candidate", ("repeat_course_demand",), ("regulation", "offline_fixed_cost"), "Hagwon demand needs policy and fixed-cost checks before scoring high."),
    Round27CaseCandidate("low_birthrate_kids_education_counterexample", "EDUCATION_SPECIALTY_SERVICES", "KIDS_BIRTHRATE", "저출산키즈교육", "KR", "failed_rerating", ("kids_education_demand",), ("birthrate_demand_decline", "domestic_kids_only"), "Kids education is capped when birthrate risk is not offset."),
    Round27CaseCandidate("education_regulation_counterexample", "EDUCATION_SPECIALTY_SERVICES", "EDU_REG", "교육규제", "KR", "failed_rerating", ("entrance_exam_theme",), ("regulation_change", "entrance_exam_theme_only"), "Entrance-exam policy changes are not structural evidence by themselves."),
    Round27CaseCandidate("smart_grid_line_rating_candidate", "TELECOM_GRID_AI_NETWORK", "SMART_GRID", "Smart grid line rating", "KR", "success_candidate", ("smart_grid", "grid_efficiency"), ("policy_keyword_only", "project_delay"), "Grid need becomes score evidence only after equipment/order economics."),
    Round27CaseCandidate("ai_datacenter_grid_capex_candidate", "TELECOM_GRID_AI_NETWORK", "AI_GRID_CAPEX", "AI datacenter grid capex", "KR", "success_candidate", ("ai_datacenter_grid_need", "datacenter_or_grid_capex_link"), ("low_margin_equipment", "capex_burden"), "AI grid capex candidate needs order and margin conversion."),
    Round27CaseCandidate("5g_6g_policy_no_revenue_counterexample", "TELECOM_GRID_AI_NETWORK", "5G6G_POLICY", "5G6G정책_무매출", "KR", "failed_rerating", ("5g_6g_policy",), ("policy_keyword_only", "no_revenue_conversion"), "5G/6G policy wording is a search tag, not score evidence."),
    Round27CaseCandidate("telecom_capex_burden_4c", "TELECOM_GRID_AI_NETWORK", "TELCO_CAPEX_4C", "통신CAPEX부담4C", "KR", "4c_thesis_break", ("network_capex",), ("capex_burden", "regulatory_recovery_failure"), "CAPEX burden can break network rerating."),
    Round27CaseCandidate("krafton_india_fund_candidate", "GAME_CONTENT_IP", "259960_INDIA", "Krafton India fund", "KR", "success_candidate", ("regional_ecosystem_investment", "india_market_exposure"), ("regulation", "capital_allocation_risk"), "India fund supports routing; IP monetization still has to be proven."),
    Round27CaseCandidate("krafton_bgmi_data_security_counterexample", "GAME_CONTENT_IP", "BGMI_SECURITY", "Krafton BGMI data security", "KR", "failed_rerating", ("india_user_base",), ("data_security", "regulatory_ban"), "Data security risk can cap a game/IP candidate."),
    Round27CaseCandidate("classys_export_device_candidate", "MEDICAL_DEVICE_HEALTHCARE_EXPORT", "214150_EXPORT", "Classys export device", "KR", "success_candidate", ("export_country_expansion", "procedure_growth"), ("competition", "approval_delay"), "Export device evidence needs repeat procedure and OPM support."),
    Round27CaseCandidate("botox_counterfeit_safety_counterexample", "MEDICAL_DEVICE_HEALTHCARE_EXPORT", "BOTOX_COUNTERFEIT", "Botox counterfeit safety", "US", "failed_rerating", ("aesthetic_treatment_demand",), ("counterfeit_issue", "safety_issue"), "Aesthetic demand does not override safety or counterfeit risk."),
)


def target_for(target_id: str) -> Round27ScoreTarget | None:
    for target in ROUND27_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round27_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND27_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
        weights = target.score_weight.as_dict()
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market=candidate.market,
            sector_raw=candidate.target_id,
            primary_archetype=target.canonical_archetype,
            expected_group=candidate.expected_group,
            large_sector=target.large_sector.value,
            case_type=candidate.case_type,
            evidence_summary=(
                f"Round27 v1.2 calibration candidate for {candidate.target_id}; "
                "stage dates, prices, and numeric evidence remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.green_conditions),
            stage3_evidence=(),
            stage4c_evidence=candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" else (),
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type not in {"success_candidate", "structural_success"} else None,
            score_price_alignment="unknown",
            rerating_result="unknown",
            price_pattern="unknown",
            score_weight_hint={
                "eps_fcf": float(weights["eps_fcf"]),
                "visibility": float(weights["structural_visibility"]),
                "bottleneck": float(weights["bottleneck_pricing"]),
                "mispricing": float(weights["market_mispricing"]),
                "valuation": float(weights["valuation"]),
                "capital_allocation": float(weights["capital_allocation"]),
                "information_confidence": float(weights["information_confidence"]),
            },
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_cross_evidence_for_green",
                *target.red_flags,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(price_validation_status="needs_price_backfill"),
            data_quality=CaseDataQuality(False, False, False, 0.0),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round27_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND27_SCORE_TARGETS:
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
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round27_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND27_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
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
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "price_validation_status": "needs_price_backfill",
                "production_input": "false",
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round27_summary() -> dict[str, int | bool]:
    records = round27_case_records()
    positive = sum(1 for record in records if record.case_type in {"success_candidate", "structural_success"})
    stage4c = sum(1 for record in records if record.case_type == "4c_thesis_break")
    stage4b = sum(1 for record in records if record.case_type == "4b_watch")
    return {
        "target_count": len(ROUND27_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": len(records) - positive,
        "stage4b_case_count": stage4b,
        "stage4c_case_count": stage4c,
        "green_possible_count": sum(1 for target in ROUND27_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND27_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round27_score_weight_reports(
    *,
    output_directory: str | Path = ROUND27_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND27_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND27_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round27_score_weight_v12_summary.md",
        "case_matrix": output / "round27_case_candidate_matrix.csv",
        "green_guardrails": output / "round27_green_guardrail_review.md",
        "false_success_boundary": output / "round27_false_success_boundary_review.md",
        "risk_boundary": output / "round27_risk_boundary_review.md",
        "price_validation_plan": output / "round27_price_validation_plan.md",
    }
    _write_case_jsonl(round27_case_records(), cases)
    _write_rows(round27_score_profile_rows(), score_profiles)
    _write_rows(round27_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round27_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round27_green_guardrail_markdown(), encoding="utf-8")
    paths["false_success_boundary"].write_text(render_round27_false_success_boundary_markdown(), encoding="utf-8")
    paths["risk_boundary"].write_text(render_round27_risk_boundary_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round27_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round27_summary_markdown() -> str:
    summary = round27_summary()
    lines = [
        "# Round-27 Score-Weight v1.2 Summary",
        "",
        f"- source_round: `{ROUND27_SOURCE_ROUND_PATH}`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- counterexample_or_risk_count: {summary['counterexample_or_risk_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "- Round 27 expands v1.2 calibration, not production scoring.",
        "- Example: game downloads are routing evidence, but not structural evidence until monetization and OP are visible.",
        "- Example: medical AI papers are useful, but subgroup validation, reimbursement, and paid workflow are still required.",
        "- Example: retail scale can be false success when supplier pressure, data breach, or logistics cost damages FCF.",
        "- Theme names, case IDs, policies, PoCs, and revenue growth headlines are not score evidence by themselves.",
    ]
    return "\n".join(lines) + "\n"


def render_round27_green_guardrail_markdown() -> str:
    lines = [
        "# Round-27 Green Guardrail Review",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "|---|---|---|---|",
    ]
    for target in ROUND27_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply v1.2 weights to production scoring yet.",
            "- Do not score downloads, store counts, papers, policies, PoCs, or traffic without source-backed economics.",
            "- Do not invent stage dates, prices, monetization, reimbursement, OPM, FCF, retention, or approval status.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round27_false_success_boundary_markdown() -> str:
    lines = [
        "# Round-27 False-Success Boundary Review",
        "",
        "Round 27 adds cases that can look successful but should not become Green without economic proof.",
        "",
        "## Examples",
        "- GAME_CONTENT_IP: downloads or new-game hype must not become Green without monetization and OP/EPS confirmation.",
        "- DIGITAL_HEALTHCARE_AI: clinical paper performance must not become Green without reimbursement and paid workflow.",
        "- RETAIL_ECOMMERCE_LOGISTICS: logistics scale or store count must not become Green if FCF, inventory, supplier, or data-security evidence is weak.",
        "- EDUCATION_SPECIALTY_SERVICES: strong private-education demand must not hide birthrate, policy, and offline fixed-cost risk.",
        "- TELECOM_GRID_AI_NETWORK: smart-grid or 5G/6G policy wording must not become Green before actual equipment orders and OP conversion.",
        "",
        "## Rule",
        "- A good company or a strong theme can still be a calibration counterexample.",
        "- Score-price alignment must verify that EPS/FCF, stage score, and price path moved together.",
    ]
    return "\n".join(lines) + "\n"


def render_round27_risk_boundary_markdown() -> str:
    lines = [
        "# Round-27 Risk Boundary Review",
        "",
        "Round 27 separates Green-possible structures from Watch-first structures with high false-success risk.",
        "",
        "## Green-Possible With Strict Gates",
    ]
    for target in ROUND27_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.GREEN_POSSIBLE:
            lines.append(f"- {target.target_id}: {target.normalization_point}")
    lines.extend(["", "## Watch-First / 4C-Sensitive"])
    for target in ROUND27_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST:
            lines.append(f"- {target.target_id}: {', '.join(target.stage4c_conditions)}")
    lines.extend(
        [
            "",
            "## Rule",
            "- Stage 3-Green still requires cross-evidence and price-path validation.",
            "- Regulatory ban, Botox counterfeit/safety issue, medical AI liability, Coupang supplier/data risks, and telecom CAPEX burden are hard 4C-style examples.",
            "- Case records are calibration examples, not production labels.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round27_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-27 Price Validation Plan",
            "",
            "1. Backfill tradable case price paths where symbols exist.",
            "2. Keep synthetic, policy, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.",
            "3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.",
            "4. Run shadow score-price alignment before production scoring changes.",
            "",
            "## Priority Validation",
            "- Game/IP: downloads and regional expansion versus monetization, OP, regulation, and single-IP risk.",
            "- Medical device: export/device demand versus recurring procedure or consumables, approval, safety, and competition.",
            "- Medical AI: external validation versus paid workflow, reimbursement, subgroup performance, and liability.",
            "- Retail/e-commerce: store/logistics scale versus inventory, supplier regulation, data security, and FCF.",
            "- Telecom/grid: AI grid need versus equipment order, margin, CAPEX burden, and regulation.",
        ]
    ) + "\n"


def _write_case_jsonl(records: Iterable[E2RCaseRecord], path: Path) -> Path:
    lines = []
    for record in records:
        record.validate()
        lines.append(json.dumps(record.as_dict(), ensure_ascii=False, sort_keys=True))
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return path


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    row_tuple = tuple(rows)
    if not row_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(row_tuple[0].keys()))
        writer.writeheader()
        for row in row_tuple:
            writer.writerow(row)
    return path


__all__ = [
    "ROUND27_CASE_CANDIDATES",
    "ROUND27_DEFAULT_CASES_PATH",
    "ROUND27_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND27_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND27_SCORE_TARGETS",
    "ROUND27_SOURCE_ROUND_PATH",
    "Round27CaseCandidate",
    "Round27ScoreTarget",
    "Round27ScoreWeightDraft",
    "render_round27_false_success_boundary_markdown",
    "render_round27_green_guardrail_markdown",
    "render_round27_price_validation_plan_markdown",
    "render_round27_risk_boundary_markdown",
    "render_round27_summary_markdown",
    "round27_case_candidate_rows",
    "round27_case_records",
    "round27_score_profile_rows",
    "round27_summary",
    "target_for",
    "write_round27_score_weight_reports",
]
