"""Round-24 cases_v06 expansion and score-weight v0.9 hypotheses.

Round 24 sharpens thin archetypes and risk boundaries. It is report-only
calibration material. Production feature engineering, scoring, staging, and
RedTeam code must not import this module.
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


ROUND24_SOURCE_ROUND_PATH = "docs/round/round_24.md"
ROUND24_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round24_score_weight_v09"
ROUND24_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v06_round24.jsonl"
ROUND24_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round24_v09.csv"


@dataclass(frozen=True)
class Round24ScoreWeightDraft:
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
class Round24ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round24ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    normalization_point: str

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round24CaseCandidate:
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


ROUND24_SCORE_TARGETS: tuple[Round24ScoreTarget, ...] = (
    Round24ScoreTarget(
        "RAIL_INFRASTRUCTURE",
        Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round24ScoreWeightDraft(20, 23, 12, 14, 12, 1, 5),
        ("rail_order", "national_infra_budget", "overseas_tender", "reconstruction_theme"),
        ("signed_contract", "delivery_schedule", "contract_amount_to_sales", "op_revision"),
        ("backlog_visibility", "margin_confirmed", "financing_risk_low", "fy1_fy2_op_revision"),
        ("signed_contract", "delivery_schedule", "margin_visibility", "op_revision", "financing_risk_low"),
        ("policy_theme_only", "mou_only", "margin_uncertainty", "project_delay", "financing_risk"),
        ("rail_order_fully_priced", "project_expectation_crowded"),
        ("project_delay", "margin_damage", "financing_failure", "contract_cancellation"),
        "Rail is order-driven like industrial backlog, but margin and delivery risk must be stricter than simple contract headlines.",
    ),
    Round24ScoreTarget(
        "CLOUD_AI_SOFTWARE_INFRA",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round24ScoreWeightDraft(20, 23, 8, 16, 14, 0, 5),
        ("cloud_transition", "erp_saas_demand", "ai_feature_launch", "b2b_customer_growth"),
        ("recurring_revenue_growth", "arpu_up", "opm_improvement", "retention_confirmed"),
        ("customer_lock_in", "fcf_conversion", "pricing_power", "old_si_or_legacy_software_frame"),
        ("recurring_revenue", "arpu", "retention", "opm_or_fcf_improvement", "ai_cost_control"),
        ("ai_feature_only", "ai_cost_overrun", "churn", "si_revenue_only", "opm_decline"),
        ("saas_ai_narrative_overheated", "multiple_saturation"),
        ("churn", "ai_cost_overrun", "opm_decline", "competition_intensifies"),
        "Cloud/SaaS can be Green, but AI wording is only Stage 1 unless recurring revenue, OPM, and FCF improve.",
    ),
    Round24ScoreTarget(
        "CRO_CLINICAL_SERVICE",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round24ScoreWeightDraft(18, 20, 8, 12, 12, 0, 5),
        ("clinical_trial_count_growth", "pharma_rd_growth", "order_backlog_growth"),
        ("sales_op_growth", "customer_diversification", "repeat_service_revenue"),
        ("multi_year_backlog", "customer_portfolio_diversified", "funding_cycle_stable", "fcf_conversion"),
        ("service_backlog", "customer_diversification", "repeat_clinical_service_revenue", "opm_improvement", "funding_cycle_stable"),
        ("biotech_funding_cycle_down", "customer_concentration", "trial_delay", "low_margin_backlog", "customer_budget_cut"),
        ("biotech_rd_expectation_overheated", "service_multiple_saturation"),
        ("clinical_trial_cut", "customer_budget_cut", "order_cancellation", "forecast_cut"),
        "CRO is more scoreable than pre-revenue biotech, but weaker than CDMO because customer R&D funding can break visibility.",
    ),
    Round24ScoreTarget(
        "RETAIL_ECOMMERCE_LOGISTICS",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round24ScoreWeightDraft(18, 16, 5, 13, 14, 3, 5),
        ("revenue_growth", "store_or_logistics_expansion", "listing_or_stake_event", "same_store_sales_recovery"),
        ("opm_improvement", "inventory_normalization", "logistics_cost_stable", "fy1_fy2_op_revision"),
        ("repeat_customer_base", "cost_leverage", "fcf_improvement", "supplier_regulation_low"),
        ("opm_improvement", "inventory_normalization", "cost_leverage", "fcf_improvement", "regulatory_risk_low"),
        ("logistics_cost", "inventory", "supplier_regulation", "data_security", "fresh_ecommerce_loss"),
        ("consumer_recovery_priced", "logistics_scale_priced"),
        ("supplier_regulation", "data_breach", "logistics_cost_spike", "inventory_build", "opm_decline"),
        "Retail/e-commerce must be scored through OPM and FCF, not revenue growth alone.",
    ),
    Round24ScoreTarget(
        "SOLAR_TARIFF_SUPPLYCHAIN",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round24ScoreWeightDraft(18, 17, 12, 12, 10, 0, 5),
        ("solar_policy", "tariff_change", "us_factory_investment", "subsidy_expectation"),
        ("utilization_up", "component_supply_stable", "op_fcf_improvement", "customer_demand_visible"),
        ("tariff_risk_low", "supply_chain_stable", "margin_visible", "durable_customer_demand"),
        ("utilization_up", "component_supply_stable", "tariff_risk_low", "op_fcf_improvement"),
        ("tariff", "customs", "subsidy", "supply_chain", "forced_labor_import_detention"),
        ("policy_benefit_priced", "solar_tariff_theme_crowded"),
        ("customs_detention", "component_delay", "subsidy_cut", "factory_furlough", "margin_damage"),
        "Solar is policy-sensitive: policy benefit is not Green until utilization, supply chain, tariff, and OP/FCF evidence align.",
    ),
    Round24ScoreTarget(
        "INSURANCE_UNDERWRITING_CYCLE",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round24ScoreWeightDraft(15, 21, 4, 15, 25, 10, 5),
        ("low_pbr", "value_up_disclosure", "loss_ratio_improvement", "dividend_or_buyback_expectation"),
        ("roe_improvement", "csm_growth", "capital_ratio_stable", "shareholder_return_execution"),
        ("pbr_roe_frame_change", "repeat_shareholder_return", "underwriting_profit_stable", "credit_risk_low"),
        ("roe_improvement", "csm_or_loss_ratio_stability", "capital_ratio_stable", "shareholder_return_execution", "credit_risk_low"),
        ("underwriting", "capital_ratio", "cyber_operational", "credit_cost", "low_pbr_only"),
        ("pbr_normalized", "insurance_value_up_crowded", "return_expectation_priced"),
        ("loss_ratio_worsens", "capital_ratio_down", "cyber_operational_risk", "credit_cost_up", "shareholder_return_retreat"),
        "Insurance is PBR-ROE-return rerating, not EPS explosion; underwriting, capital, and cyber resilience are gates.",
    ),
    Round24ScoreTarget(
        "DIGITAL_HEALTHCARE_AI",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round24ScoreWeightDraft(18, 17, 8, 13, 12, 0, 7),
        ("clinical_ai_paper", "ai_diagnosis_model", "workflow_ai", "remote_healthcare_policy"),
        ("external_validation", "regulatory_clearance", "hospital_adoption", "paid_usage"),
        ("reimbursement_or_paid_usage", "hospital_workflow_embedded", "revenue_or_op_conversion", "liability_risk_low"),
        ("external_clinical_validation", "regulatory_clearance", "hospital_adoption", "reimbursement_or_paid_usage", "revenue_or_op_conversion"),
        ("paper_only", "poc_only", "no_reimbursement", "liability", "clinical_validation_gap"),
        ("medical_ai_theme_overheated", "valuation_priced_before_revenue"),
        ("regulatory_rejection", "liability_event", "hospital_adoption_failure", "reimbursement_denial"),
        "Medical AI remains Watch-to-Green: papers and PoCs are Stage 1 until paid workflow and revenue evidence appear.",
    ),
    Round24ScoreTarget(
        "SECURITY_IDENTITY_DEEPFAKE",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round24ScoreWeightDraft(20, 20, 10, 14, 13, 0, 5),
        ("security_threat_growth", "deepfake_regulation", "identity_or_cctv_demand", "government_security_budget"),
        ("recurring_subscription", "customer_retention", "opm_improvement", "enterprise_or_government_contract"),
        ("mission_critical_lock_in", "low_churn", "customer_diversification", "fcf_conversion", "operational_trust_intact"),
        ("recurring_subscription", "low_churn", "customer_diversification", "opm_improvement", "no_major_outage"),
        ("operational_trust", "outage", "legal", "customer_retention", "contract_absence"),
        ("security_theme_crowded", "deepfake_regulation_priced"),
        ("major_outage", "legal_claim", "customer_churn", "contract_loss", "trust_break"),
        "Security can be Green, but operational trust is a hard gate because one outage can become 4C.",
    ),
    Round24ScoreTarget(
        "BATTERY_RECYCLING_ESS_SHIFT",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round24ScoreWeightDraft(20, 16, 14, 10, 10, 0, 5),
        ("ess_shift", "battery_recycling_policy", "solid_state_theme", "ev_supply_chain_news"),
        ("customer_contract", "utilization_up", "fcf_disciplined_capex", "ess_revenue_visible"),
        ("long_term_contract", "price_pass_through", "demand_durable", "valuation_room"),
        ("customer_contract", "utilization_up", "fcf_disciplined_capex", "demand_durable"),
        ("ev_demand", "mineral_price", "capex_overbuild", "policy", "no_commercialization"),
        ("battery_theme_overheated", "ess_transition_priced"),
        ("ev_demand_slowdown", "mineral_price_down", "capa_overbuild", "margin_compression", "commercialization_delay"),
        "Battery recycling/ESS is Watch-first; ESS transition can help, but EV demand and CAPA overbuild risk cap Green.",
    ),
    Round24ScoreTarget(
        "SECURITIES_BROKERAGE_CYCLE",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round24ScoreWeightDraft(18, 14, 5, 15, 18, 8, 5),
        ("trading_value_growth", "equity_market_rally", "ipo_ib_recovery_expectation", "vc_exit_expectation"),
        ("brokerage_revenue_growth", "ib_fee_growth", "capital_ratio_stable", "op_eps_revision"),
        ("repeat_turnover_or_ib_recovery", "pf_risk_low", "roe_structure_improves", "shareholder_return_capacity"),
        ("brokerage_revenue_growth", "ib_pipeline", "capital_ratio_stable", "pf_risk_low", "roe_improvement"),
        ("market_turnover", "pf", "proprietary_loss", "ipo_cycle", "vc_exit_market_weakness"),
        ("market_turnover_peak", "brokerage_group_overheated", "ipo_expectation_priced"),
        ("trading_value_collapse", "pf_loss", "proprietary_loss", "capital_ratio_down", "ipo_pipeline_delay"),
        "Brokerage remains Watch-first because turnover and IPO recovery can reverse faster than banks or insurers.",
    ),
)


ROUND24_CASE_CANDIDATES: tuple[Round24CaseCandidate, ...] = (
    Round24CaseCandidate("hyundai_rotem_morocco_rail_order_success_candidate", "RAIL_INFRASTRUCTURE", "064350", "현대로템 모로코 철도 수주", "KR", "success_candidate", ("signed_contract", "large_rail_order", "delivery_schedule"), ("project_delay", "margin_uncertainty"), "Large signed rail order can reach candidate status after margin and delivery backfill."),
    Round24CaseCandidate("rail_policy_no_contract_counterexample", "RAIL_INFRASTRUCTURE", "RAIL_POLICY", "철도정책_무계약", "KR", "failed_rerating", ("rail_policy",), ("policy_theme_only", "no_contract"), "Policy without contract stays event/watch."),
    Round24CaseCandidate("reconstruction_rail_theme_event_watch", "RAIL_INFRASTRUCTURE", "RAIL_RECON", "재건철도테마", "KR", "event_premium", ("reconstruction_theme",), ("mou_only", "no_delivery_schedule"), "Reconstruction theme is routing evidence, not score evidence."),
    Round24CaseCandidate("rail_project_margin_delay_4c", "RAIL_INFRASTRUCTURE", "RAIL_DELAY_4C", "철도프로젝트마진납기리스크", "KR", "4c_thesis_break", ("rail_project_backlog",), ("project_delay", "margin_damage"), "Delivery delay or margin damage can break rail backlog thesis."),
    Round24CaseCandidate("douzone_bizon_cloud_erp_candidate", "CLOUD_AI_SOFTWARE_INFRA", "012510", "더존비즈온 클라우드 ERP", "KR", "success_candidate", ("cloud_erp", "recurring_revenue", "smb_lock_in"), ("ai_cost_overrun", "churn"), "Cloud ERP candidate needs OPM and FCF backfill."),
    Round24CaseCandidate("ai_feature_no_fcf_counterexample", "CLOUD_AI_SOFTWARE_INFRA", "AI_SW_NO_FCF", "AI기능_무현금흐름", "KR", "failed_rerating", ("ai_feature_launch",), ("no_paid_usage", "no_fcf"), "AI feature without paid usage is not structural evidence."),
    Round24CaseCandidate("cloud_cost_margin_pressure_4c", "CLOUD_AI_SOFTWARE_INFRA", "CLOUD_MARGIN_4C", "클라우드비용_마진압박", "KR", "4c_thesis_break", ("cloud_growth",), ("ai_cost_overrun", "opm_decline"), "Cloud growth can break if AI/cloud costs destroy margin."),
    Round24CaseCandidate("saas_churn_counterexample", "CLOUD_AI_SOFTWARE_INFRA", "SAAS_CHURN", "SaaS churn", "US", "failed_rerating", ("subscription_revenue",), ("churn", "retention_down"), "Subscription label needs retention evidence."),
    Round24CaseCandidate("cro_revenue_backlog_candidate", "CRO_CLINICAL_SERVICE", "CRO_BACKLOG", "CRO 매출수주잔고", "KR", "success_candidate", ("service_backlog", "clinical_service_revenue"), ("customer_budget_cut", "funding_cycle"), "CRO can score when backlog converts to revenue."),
    Round24CaseCandidate("charles_river_funding_crunch_4c", "CRO_CLINICAL_SERVICE", "CRL", "Charles River funding crunch", "US", "4c_thesis_break", ("biotech_service_revenue",), ("biotech_funding_cycle_down", "forecast_cut"), "Funding crunch can turn CRO visibility into 4C."),
    Round24CaseCandidate("biotech_customer_budget_cut_counterexample", "CRO_CLINICAL_SERVICE", "CRO_BUDGET_CUT", "바이오고객예산축소", "US", "failed_rerating", ("clinical_volume",), ("customer_budget_cut", "volume_without_margin"), "Clinical volume is insufficient if customer budgets decline."),
    Round24CaseCandidate("cro_customer_diversification_success_candidate", "CRO_CLINICAL_SERVICE", "CRO_DIVERSIFIED", "CRO 고객다변화", "KR", "success_candidate", ("customer_diversification", "repeat_service_revenue"), ("funding_cycle", "customer_concentration"), "Diversified customers can improve CRO visibility."),
    Round24CaseCandidate("coupang_logistics_scale_candidate", "RETAIL_ECOMMERCE_LOGISTICS", "CPNG", "Coupang logistics scale", "US", "success_candidate", ("logistics_scale", "repeat_customer_base"), ("logistics_cost", "supplier_regulation"), "Logistics scale candidate requires OPM/FCF proof."),
    Round24CaseCandidate("coupang_farfetch_loss_counterexample", "RETAIL_ECOMMERCE_LOGISTICS", "CPNG_FARFETCH", "Coupang Farfetch loss", "US", "failed_rerating", ("revenue_growth",), ("acquisition_loss", "developing_offerings_loss"), "Revenue growth can be offset by acquisition and new-business losses."),
    Round24CaseCandidate("coupang_supplier_regulation_risk", "RETAIL_ECOMMERCE_LOGISTICS", "CPNG_REG", "Coupang supplier regulation risk", "US", "failed_rerating", ("platform_scale",), ("supplier_regulation", "payment_delay"), "Supplier pressure is not structural margin quality."),
    Round24CaseCandidate("ecommerce_fresh_loss_counterexample", "RETAIL_ECOMMERCE_LOGISTICS", "FRESH_LOSS", "신선식품이커머스적자", "KR", "failed_rerating", ("ecommerce_sales_growth",), ("fresh_delivery_loss", "logistics_cost_up"), "Fresh e-commerce sales without FCF remains Watch."),
    Round24CaseCandidate("qcells_us_supply_chain_candidate", "SOLAR_TARIFF_SUPPLYCHAIN", "009830", "한화솔루션 Qcells 미국공급망", "KR", "success_candidate", ("us_factory_investment", "solar_policy"), ("customs_detention", "component_delay"), "US supply-chain candidate needs utilization and component-flow backfill."),
    Round24CaseCandidate("qcells_customs_detention_4c", "SOLAR_TARIFF_SUPPLYCHAIN", "QCELLS_CUSTOMS", "Qcells 통관억류", "KR", "4c_thesis_break", ("solar_factory_capacity",), ("customs_detention", "factory_furlough"), "Customs detention can break solar policy-benefit thesis."),
    Round24CaseCandidate("solar_subsidy_dependency_counterexample", "SOLAR_TARIFF_SUPPLYCHAIN", "SOLAR_SUBSIDY", "태양광보조금의존", "KR", "failed_rerating", ("subsidy_expectation",), ("subsidy_dependency", "policy_reversal"), "Subsidy expectation alone is not Green evidence."),
    Round24CaseCandidate("solar_component_tariff_risk", "SOLAR_TARIFF_SUPPLYCHAIN", "SOLAR_TARIFF", "태양광부품관세리스크", "KR", "failed_rerating", ("solar_component_supply",), ("tariff", "component_delay"), "Tariff and component risk cap rerating."),
    Round24CaseCandidate("samsung_fire_underwriting_valueup_candidate", "INSURANCE_UNDERWRITING_CYCLE", "000810", "삼성화재 underwriting value-up", "KR", "success_candidate", ("loss_ratio_stability", "roe", "shareholder_return"), ("loss_ratio_worsens", "capital_ratio_down"), "Insurance candidate needs CSM/K-ICS and return execution backfill."),
    Round24CaseCandidate("sgi_guarantee_insurance_candidate", "INSURANCE_UNDERWRITING_CYCLE", "031210", "서울보증보험 보증보험", "KR", "success_candidate", ("guarantee_insurance", "recurring_premium"), ("cyber_operational_risk", "credit_cost"), "Guarantee insurance candidate requires credit and cyber controls."),
    Round24CaseCandidate("sgi_ransomware_operational_risk_4c", "INSURANCE_UNDERWRITING_CYCLE", "031210_RANSOM", "서울보증보험 랜섬웨어", "KR", "4c_thesis_break", ("guarantee_insurance",), ("cyber_operational_risk", "service_outage"), "Cyber operation failure can break financial infrastructure thesis."),
    Round24CaseCandidate("low_pbr_insurer_no_capital_return_counterexample", "INSURANCE_UNDERWRITING_CYCLE", "INS_LOW_PBR", "저PBR보험_환원부재", "KR", "failed_rerating", ("low_pbr",), ("capital_return_limited", "low_roe"), "Low PBR without return execution is value trap risk."),
    Round24CaseCandidate("mammography_ai_workflow_candidate", "DIGITAL_HEALTHCARE_AI", "328130", "Mammography AI workflow", "KR", "success_candidate", ("external_validation", "medical_imaging_ai"), ("no_reimbursement", "subgroup_validation_gap"), "Clinical AI needs paid workflow and revenue conversion."),
    Round24CaseCandidate("medical_ai_no_reimbursement_counterexample", "DIGITAL_HEALTHCARE_AI", "MED_AI_NO_PAY", "의료AI_수가부재", "KR", "failed_rerating", ("clinical_ai_paper",), ("no_reimbursement", "no_paid_usage"), "No reimbursement blocks Green."),
    Round24CaseCandidate("hospital_ai_poc_no_revenue_counterexample", "DIGITAL_HEALTHCARE_AI", "HOSP_AI_POC", "병원AI_PoC_무매출", "KR", "failed_rerating", ("poc", "hospital_trial"), ("poc_only", "no_revenue_conversion"), "PoC without revenue remains Stage 1/2."),
    Round24CaseCandidate("medical_ai_liability_risk_4c", "DIGITAL_HEALTHCARE_AI", "MED_AI_LIABILITY", "의료AI책임리스크", "KR", "4c_thesis_break", ("medical_ai_response",), ("liability", "clinical_validation_gap"), "Liability or validation failure can break medical AI thesis."),
    Round24CaseCandidate("recurring_security_subscription_candidate", "SECURITY_IDENTITY_DEEPFAKE", "SEC_SUB", "보안반복구독", "KR", "success_candidate", ("recurring_subscription", "customer_retention"), ("major_outage", "legal_claim"), "Security subscription can score with retention and no major outage."),
    Round24CaseCandidate("crowdstrike_outage_4c", "SECURITY_IDENTITY_DEEPFAKE", "CRWD", "CrowdStrike outage", "US", "4c_thesis_break", ("security_subscription",), ("major_outage", "legal_claim"), "Major outage is hard 4C risk even for recurring security revenue."),
    Round24CaseCandidate("deepfake_regulation_stage1_candidate", "SECURITY_IDENTITY_DEEPFAKE", "DEEPFAKE_REG", "딥페이크규제Stage1", "KR", "success_candidate", ("deepfake_regulation", "security_demand"), ("contract_absence", "theme_only"), "Deepfake regulation is Stage 1 until contracts or subscription revenue appear."),
    Round24CaseCandidate("security_theme_no_contract_counterexample", "SECURITY_IDENTITY_DEEPFAKE", "SEC_THEME", "보안테마_무계약", "KR", "failed_rerating", ("security_theme",), ("contract_absence", "theme_only"), "Security theme without contract is not score evidence."),
    Round24CaseCandidate("ess_shift_candidate", "BATTERY_RECYCLING_ESS_SHIFT", "ESS_SHIFT", "ESS 전환 후보", "KR", "success_candidate", ("ess_shift", "customer_contract"), ("ev_demand_slowdown", "capex_overbuild"), "ESS shift can be a candidate if customers and utilization are visible."),
    Round24CaseCandidate("ev_demand_slowdown_4c", "BATTERY_RECYCLING_ESS_SHIFT", "EV_SLOW_4C", "EV수요둔화4C", "KR", "4c_thesis_break", ("ev_battery_capacity",), ("ev_demand_slowdown", "margin_compression"), "EV slowdown can break battery CAPA thesis."),
    Round24CaseCandidate("battery_recycling_no_volume_counterexample", "BATTERY_RECYCLING_ESS_SHIFT", "RECYCLING_NO_VOL", "폐배터리물량부재", "KR", "failed_rerating", ("battery_recycling_policy",), ("no_volume", "no_commercialization"), "Recycling policy without volume is not structural evidence."),
    Round24CaseCandidate("solid_state_no_commercialization_counterexample", "BATTERY_RECYCLING_ESS_SHIFT", "SOLID_NO_COMM", "전고체무상용화", "KR", "failed_rerating", ("solid_state_theme",), ("commercialization_delay", "no_revenue_conversion"), "Solid-state theme remains Watch before commercialization."),
    Round24CaseCandidate("brokerage_trading_value_rally_candidate", "SECURITIES_BROKERAGE_CYCLE", "BROKER_TURNOVER", "거래대금회복_증권사", "KR", "success_candidate", ("trading_value_growth", "brokerage_revenue_growth"), ("turnover_peak", "pf_loss"), "Brokerage candidate requires revenue and PF risk confirmation."),
    Round24CaseCandidate("securities_pf_loss_4c", "SECURITIES_BROKERAGE_CYCLE", "BROKER_PF_4C", "증권사_PF손실", "KR", "4c_thesis_break", ("brokerage_balance_sheet",), ("pf_loss", "capital_ratio_down"), "PF loss can override trading-value recovery."),
    Round24CaseCandidate("ipo_pipeline_recovery_candidate", "SECURITIES_BROKERAGE_CYCLE", "IPO_PIPE", "IPO파이프라인회복", "KR", "success_candidate", ("ipo_pipeline", "ib_fee_growth"), ("pipeline_delay", "market_turnover_peak"), "IPO recovery needs actual fee conversion."),
    Round24CaseCandidate("vc_exit_market_weakness_counterexample", "SECURITIES_BROKERAGE_CYCLE", "VC_EXIT_WEAK", "VC회수시장부진", "KR", "failed_rerating", ("vc_portfolio",), ("exit_market_weakness", "valuation_markdown"), "VC recovery expectation without exits stays Watch."),
)


def target_for(target_id: str) -> Round24ScoreTarget | None:
    for target in ROUND24_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round24_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND24_CASE_CANDIDATES:
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
                f"Round24 v0.9 calibration candidate for {candidate.target_id}; "
                "stage dates, prices, and numeric evidence remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.green_conditions),
            stage3_evidence=(),
            stage4b_evidence=candidate.evidence_fields if candidate.case_type == "4b_watch" else (),
            stage4c_evidence=candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" else (),
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type not in {"success_candidate", "structural_success"} else None,
            score_price_alignment="unknown",
            rerating_result="event_premium" if candidate.case_type == "event_premium" else "unknown",
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


def round24_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND24_SCORE_TARGETS:
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
                "stage4b_conditions": "|".join(target.stage4b_conditions),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round24_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND24_CASE_CANDIDATES:
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


def round24_summary() -> dict[str, int | bool]:
    records = round24_case_records()
    positive = sum(1 for record in records if record.case_type in {"success_candidate", "structural_success"})
    stage4c = sum(1 for record in records if record.case_type == "4c_thesis_break")
    return {
        "target_count": len(ROUND24_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": len(records) - positive,
        "stage4c_case_count": stage4c,
        "green_possible_count": sum(1 for target in ROUND24_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND24_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round24_score_weight_reports(
    *,
    output_directory: str | Path = ROUND24_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND24_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND24_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round24_score_weight_v09_summary.md",
        "case_matrix": output / "round24_case_candidate_matrix.csv",
        "green_guardrails": output / "round24_green_guardrail_review.md",
        "risk_boundary": output / "round24_risk_boundary_review.md",
        "price_validation_plan": output / "round24_price_validation_plan.md",
    }
    _write_case_jsonl(round24_case_records(), cases)
    _write_rows(round24_score_profile_rows(), score_profiles)
    _write_rows(round24_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round24_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round24_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_boundary"].write_text(render_round24_risk_boundary_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round24_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round24_summary_markdown() -> str:
    summary = round24_summary()
    lines = [
        "# Round-24 Score-Weight v0.9 Summary",
        "",
        f"- source_round: `{ROUND24_SOURCE_ROUND_PATH}`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- counterexample_or_risk_count: {summary['counterexample_or_risk_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "- Round 24 expands v0.9 calibration, not production scoring.",
        "- Example: rail orders need signed contract, delivery schedule, margin visibility, and OP revision.",
        "- Example: cloud/SaaS needs recurring revenue, retention, OPM, and FCF; AI feature wording alone is Stage 1.",
        "- Example: security can be structural, but a major outage is hard 4C risk.",
        "- Theme names, case IDs, policies, PoCs, and revenue growth headlines are not score evidence by themselves.",
    ]
    return "\n".join(lines) + "\n"


def render_round24_green_guardrail_markdown() -> str:
    lines = [
        "# Round-24 Green Guardrail Review",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "|---|---|---|---|",
    ]
    for target in ROUND24_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply v0.9 weights to production scoring yet.",
            "- Do not score policies, AI features, PoCs, revenue headlines, or theme labels without source-backed economics.",
            "- Do not invent stage dates, prices, margins, retention, FCF, reimbursement, or contract values.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round24_risk_boundary_markdown() -> str:
    lines = [
        "# Round-24 Risk Boundary Review",
        "",
        "Round 24 makes several archetypes more precise without loosening Green.",
        "",
        "## Green-Possible With Strict Gates",
    ]
    for target in ROUND24_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.GREEN_POSSIBLE:
            lines.append(f"- {target.target_id}: {target.normalization_point}")
    lines.extend(
        [
            "",
            "## Watch-First / 4C-Sensitive",
        ]
    )
    for target in ROUND24_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST:
            lines.append(f"- {target.target_id}: {', '.join(target.stage4c_conditions)}")
    lines.extend(
        [
            "",
            "## Rule",
            "- Stage 3-Green still requires cross-evidence and price-path validation.",
            "- Security outages, cyber-operational failures, and clinical liability events are hard 4C-style thesis-break examples.",
            "- 4C cases are thesis-break examples for future calibration, not production labels.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round24_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-24 Price Validation Plan",
            "",
            "1. Backfill tradable case price paths where symbols exist.",
            "2. Keep policy, synthetic, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.",
            "3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.",
            "4. Run shadow score-price alignment before production scoring changes.",
            "",
            "## Priority Validation",
            "- Rail: signed contract versus delivery, financing, and margin realization.",
            "- Cloud/SaaS: recurring revenue and FCF versus AI-cost or churn pressure.",
            "- Insurance/securities: ROE, capital, PF, cyber, and market-cycle boundaries.",
            "- Solar/battery: policy benefit versus customs, subsidy, EV demand, and CAPA risks.",
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
    "ROUND24_CASE_CANDIDATES",
    "ROUND24_DEFAULT_CASES_PATH",
    "ROUND24_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND24_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND24_SCORE_TARGETS",
    "ROUND24_SOURCE_ROUND_PATH",
    "Round24CaseCandidate",
    "Round24ScoreTarget",
    "Round24ScoreWeightDraft",
    "render_round24_green_guardrail_markdown",
    "render_round24_price_validation_plan_markdown",
    "render_round24_risk_boundary_markdown",
    "render_round24_summary_markdown",
    "round24_case_candidate_rows",
    "round24_case_records",
    "round24_score_profile_rows",
    "round24_summary",
    "target_for",
    "write_round24_score_weight_reports",
]
