"""Round-25 cases_v07 expansion and score-weight v1.0 hypotheses.

Round 25 adds AI data-center cooling and tightens several 4C/4B boundaries.
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


ROUND25_SOURCE_ROUND_PATH = "docs/round/round_25.md"
ROUND25_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round25_score_weight_v10"
ROUND25_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v07_round25.jsonl"
ROUND25_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round25_v10.csv"


@dataclass(frozen=True)
class Round25ScoreWeightDraft:
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
class Round25ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round25ScoreWeightDraft
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
class Round25CaseCandidate:
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


ROUND25_SCORE_TARGETS: tuple[Round25ScoreTarget, ...] = (
    Round25ScoreTarget(
        "AI_DATA_CENTER_COOLING",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round25ScoreWeightDraft(21, 22, 22, 13, 12, 0, 5),
        ("liquid_cooling_keyword", "high_density_server_heat", "ai_datacenter_capex", "hvac_or_ess_link"),
        ("customer_datacenter_capex_link", "confirmed_order_or_delivery", "cooling_bottleneck", "op_eps_revision"),
        ("direct_capex_link", "delivery_or_service_revenue", "cooling_bottleneck_position", "repeat_service_revenue"),
        ("customer_datacenter_capex_link", "confirmed_order_or_delivery", "cooling_bottleneck", "repeat_service_revenue", "op_eps_revision"),
        ("liquid_cooling_theme_only", "no_customer_order", "ai_capex_delay", "low_margin_project", "customer_concentration"),
        ("ai_cooling_narrative_crowded", "orders_fully_priced", "capex_pull_forward"),
        ("ai_capex_delay", "project_margin_damage", "customer_order_delay", "service_attach_failure"),
        "AI cooling is Green-possible only when cooling bottleneck evidence turns into orders, delivery, service revenue, and OP revision.",
    ),
    Round25ScoreTarget(
        "SECURITY_IDENTITY_DEEPFAKE",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round25ScoreWeightDraft(20, 20, 10, 14, 13, 0, 5),
        ("security_threat_growth", "deepfake_regulation", "identity_or_cctv_demand", "government_security_budget"),
        ("recurring_subscription", "customer_retention", "opm_improvement", "enterprise_or_government_contract"),
        ("mission_critical_lock_in", "low_churn", "customer_diversification", "fcf_conversion", "operational_trust_intact"),
        ("recurring_subscription", "low_churn", "customer_diversification", "opm_improvement", "no_major_outage"),
        ("operational_trust", "outage", "legal", "customer_retention", "contract_absence"),
        ("security_theme_crowded", "deepfake_regulation_priced"),
        ("major_outage", "legal_claim", "customer_churn", "contract_loss", "trust_break"),
        "Security can be structural, but operational trust is a hard gate because one outage can become 4C.",
    ),
    Round25ScoreTarget(
        "CRO_CLINICAL_SERVICE",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round25ScoreWeightDraft(18, 20, 8, 12, 12, 0, 5),
        ("clinical_trial_count_growth", "pharma_rd_growth", "order_backlog_growth"),
        ("sales_op_growth", "customer_diversification", "repeat_service_revenue"),
        ("multi_year_backlog", "customer_portfolio_diversified", "funding_cycle_stable", "high_margin_service_mix"),
        ("service_backlog", "customer_diversification", "repeat_clinical_service_revenue", "opm_improvement", "funding_cycle_stable"),
        ("biotech_funding_cycle_down", "customer_concentration", "trial_delay", "low_margin_backlog", "customer_budget_cut"),
        ("biotech_rd_expectation_overheated", "service_multiple_saturation"),
        ("clinical_trial_cut", "customer_budget_cut", "order_cancellation", "forecast_cut"),
        "CRO is Watch-to-Green: stronger than pre-revenue biotech, weaker than CDMO due funding-cycle exposure.",
    ),
    Round25ScoreTarget(
        "SOLAR_TARIFF_SUPPLYCHAIN",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round25ScoreWeightDraft(18, 17, 12, 12, 10, 0, 5),
        ("solar_policy", "tariff_change", "us_factory_investment", "subsidy_expectation"),
        ("utilization_up", "component_supply_stable", "op_fcf_improvement", "customer_demand_visible"),
        ("tariff_risk_low", "supply_chain_stable", "margin_visible", "durable_customer_demand"),
        ("utilization_up", "component_supply_stable", "tariff_risk_low", "op_fcf_improvement", "long_term_demand"),
        ("tariff", "customs", "subsidy", "supply_chain", "forced_labor_import_detention"),
        ("policy_benefit_priced", "solar_tariff_theme_crowded"),
        ("customs_detention", "component_delay", "subsidy_cut", "factory_furlough", "margin_damage"),
        "Solar remains Watch-first: policy benefit can be overwhelmed by tariff, customs, subsidy, and supply-chain failures.",
    ),
    Round25ScoreTarget(
        "RETAIL_ECOMMERCE_LOGISTICS",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round25ScoreWeightDraft(18, 16, 5, 13, 14, 3, 5),
        ("revenue_growth", "store_or_logistics_expansion", "same_store_sales_recovery", "pb_mix"),
        ("opm_improvement", "inventory_normalization", "logistics_cost_stable", "fy1_fy2_op_revision"),
        ("repeat_customer_base", "cost_leverage", "fcf_improvement", "supplier_regulation_low"),
        ("opm_improvement", "inventory_normalization", "cost_leverage", "fcf_improvement", "regulatory_risk_low"),
        ("logistics_cost", "inventory", "supplier_regulation", "data_security", "fresh_ecommerce_loss"),
        ("consumer_recovery_priced", "logistics_scale_priced"),
        ("supplier_regulation", "data_breach", "logistics_cost_spike", "inventory_build", "opm_decline"),
        "Retail/e-commerce is Watch-first because revenue growth is weak evidence without OPM and FCF.",
    ),
    Round25ScoreTarget(
        "INSURANCE_UNDERWRITING_CYCLE",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round25ScoreWeightDraft(15, 21, 4, 15, 25, 10, 5),
        ("low_pbr", "value_up_disclosure", "loss_ratio_improvement", "dividend_or_buyback_expectation"),
        ("roe_improvement", "csm_growth", "capital_ratio_stable", "shareholder_return_execution"),
        ("pbr_roe_frame_change", "repeat_shareholder_return", "underwriting_profit_stable", "credit_risk_low"),
        ("roe_improvement", "csm_or_loss_ratio_stability", "capital_ratio_stable", "shareholder_return_execution", "credit_risk_low"),
        ("underwriting", "capital_ratio", "cyber_operational", "credit_cost", "low_pbr_only"),
        ("pbr_normalized", "insurance_value_up_crowded", "return_expectation_priced"),
        ("loss_ratio_worsens", "capital_ratio_down", "cyber_operational_risk", "credit_cost_up", "shareholder_return_retreat"),
        "Insurance is PBR-ROE-return rerating, not EPS explosion; underwriting, capital, and cyber resilience are gates.",
    ),
    Round25ScoreTarget(
        "DIGITAL_HEALTHCARE_AI",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round25ScoreWeightDraft(18, 17, 8, 13, 12, 0, 7),
        ("clinical_ai_paper", "ai_diagnosis_model", "workflow_ai", "remote_healthcare_policy"),
        ("external_validation", "regulatory_clearance", "hospital_adoption", "paid_usage"),
        ("reimbursement_or_paid_usage", "hospital_workflow_embedded", "revenue_or_op_conversion", "liability_risk_low"),
        ("external_clinical_validation", "regulatory_clearance", "hospital_adoption", "reimbursement_or_paid_usage", "revenue_or_op_conversion"),
        ("paper_only", "poc_only", "no_reimbursement", "liability", "clinical_validation_gap"),
        ("medical_ai_theme_overheated", "valuation_priced_before_revenue"),
        ("regulatory_rejection", "liability_event", "hospital_adoption_failure", "reimbursement_denial"),
        "Medical AI remains Watch-to-Green: papers and PoCs are Stage 1 until paid workflow and revenue evidence appear.",
    ),
    Round25ScoreTarget(
        "BATTERY_RECYCLING_ESS_SHIFT",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round25ScoreWeightDraft(20, 16, 14, 10, 10, 0, 5),
        ("ess_shift", "battery_recycling_policy", "solid_state_theme", "ev_supply_chain_news"),
        ("customer_contract", "utilization_up", "fcf_disciplined_capex", "ess_revenue_visible"),
        ("long_term_contract", "price_pass_through", "demand_durable", "valuation_room"),
        ("customer_contract", "utilization_up", "fcf_disciplined_capex", "demand_durable"),
        ("ev_demand", "mineral_price", "capex_overbuild", "policy", "no_commercialization"),
        ("battery_theme_overheated", "ess_transition_priced"),
        ("ev_demand_slowdown", "mineral_price_down", "capa_overbuild", "margin_compression", "commercialization_delay"),
        "Battery recycling/ESS is Watch-first; ESS transition can help, but EV demand and CAPA overbuild risk cap Green.",
    ),
    Round25ScoreTarget(
        "SECURITIES_BROKERAGE_CYCLE",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round25ScoreWeightDraft(18, 14, 5, 15, 18, 8, 5),
        ("trading_value_growth", "equity_market_rally", "ipo_ib_recovery_expectation", "vc_exit_expectation"),
        ("brokerage_revenue_growth", "ib_fee_growth", "capital_ratio_stable", "op_eps_revision"),
        ("repeat_turnover_or_ib_recovery", "pf_risk_low", "roe_structure_improves", "shareholder_return_capacity"),
        ("brokerage_revenue_growth", "ib_pipeline", "capital_ratio_stable", "pf_risk_low", "roe_improvement"),
        ("market_turnover", "pf", "proprietary_loss", "ipo_cycle", "vc_exit_market_weakness"),
        ("market_turnover_peak", "brokerage_group_overheated", "ipo_expectation_priced"),
        ("trading_value_collapse", "pf_loss", "proprietary_loss", "capital_ratio_down", "ipo_pipeline_delay"),
        "Brokerage remains Watch-first because turnover and IPO recovery can reverse faster than banks or insurers.",
    ),
    Round25ScoreTarget(
        "MEMORY_HBM_CAPACITY",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.MEMORY_HBM_CAPACITY,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round25ScoreWeightDraft(24, 21, 19, 15, 12, 0, 5),
        ("hbm_demand", "memory_price_increase", "earnings_turnaround"),
        ("fy1_fy2_fy3_revision", "dram_nand_hbm_pricing", "supply_discipline", "customer_supply_preorder"),
        ("long_term_contract_or_prepayment", "price_band", "capacity_constraint", "multi_year_revision", "cyclical_discount_removed"),
        ("hbm_demand", "supply_discipline", "medium_term_revision", "capacity_constraint", "long_term_contract_or_prepayment"),
        ("capex_reversal", "cycle_peak", "crowding", "price_only_memory_rally", "customer_ai_capex_slowdown"),
        ("one_to_two_year_price_surge", "market_cap_multiple_saturation", "customer_price_resistance", "capex_expansion", "global_crowding"),
        ("memory_price_down", "supply_glut", "customer_ai_capex_slowdown", "consensus_revision_down"),
        "HBM remains Green-possible, but successful rerating must automatically turn on 4B-watch diagnostics.",
    ),
)


ROUND25_CASE_CANDIDATES: tuple[Round25CaseCandidate, ...] = (
    Round25CaseCandidate("ecolab_coolit_ai_liquid_cooling_candidate", "AI_DATA_CENTER_COOLING", "ECL_COOLIT", "Ecolab/CoolIT AI liquid cooling", "US", "success_candidate", ("customer_datacenter_capex_link", "cooling_bottleneck", "confirmed_order_or_delivery"), ("customer_concentration", "project_margin"), "AI cooling candidate needs delivery, service revenue, and OP revision backfill."),
    Round25CaseCandidate("liquid_cooling_theme_no_order_counterexample", "AI_DATA_CENTER_COOLING", "COOLING_THEME", "액체냉각테마_무수주", "KR", "failed_rerating", ("liquid_cooling_keyword",), ("liquid_cooling_theme_only", "no_customer_order"), "Cooling keyword without order is not score evidence."),
    Round25CaseCandidate("ai_capex_delay_cooling_4c", "AI_DATA_CENTER_COOLING", "COOL_CAPEX_4C", "AI_CAPEX지연_냉각", "US", "4c_thesis_break", ("cooling_project_pipeline",), ("ai_capex_delay", "customer_order_delay"), "AI CAPEX delay can break cooling backlog assumptions."),
    Round25CaseCandidate("low_margin_hvac_project_counterexample", "AI_DATA_CENTER_COOLING", "HVAC_LOW_MARGIN", "저마진HVAC프로젝트", "KR", "failed_rerating", ("hvac_project_revenue",), ("low_margin_project", "no_service_revenue"), "Low-margin equipment project is not structural cooling evidence."),
    Round25CaseCandidate("recurring_security_subscription_candidate", "SECURITY_IDENTITY_DEEPFAKE", "SEC_SUB", "보안반복구독", "KR", "success_candidate", ("recurring_subscription", "customer_retention"), ("major_outage", "legal_claim"), "Security subscription can score with retention and no major outage."),
    Round25CaseCandidate("crowdstrike_outage_4c", "SECURITY_IDENTITY_DEEPFAKE", "CRWD", "CrowdStrike outage", "US", "4c_thesis_break", ("security_subscription",), ("major_outage", "legal_claim"), "Major outage is hard 4C risk even for recurring security revenue."),
    Round25CaseCandidate("deepfake_regulation_stage1_candidate", "SECURITY_IDENTITY_DEEPFAKE", "DEEPFAKE_REG", "딥페이크규제Stage1", "KR", "success_candidate", ("deepfake_regulation", "security_demand"), ("contract_absence", "theme_only"), "Deepfake regulation is Stage 1 until contracts or subscription revenue appear."),
    Round25CaseCandidate("security_theme_no_contract_counterexample", "SECURITY_IDENTITY_DEEPFAKE", "SEC_THEME", "보안테마_무계약", "KR", "failed_rerating", ("security_theme",), ("contract_absence", "theme_only"), "Security theme without contract is not score evidence."),
    Round25CaseCandidate("cro_revenue_backlog_candidate", "CRO_CLINICAL_SERVICE", "CRO_BACKLOG", "CRO 매출수주잔고", "KR", "success_candidate", ("service_backlog", "clinical_service_revenue"), ("customer_budget_cut", "funding_cycle"), "CRO can score when backlog converts to revenue."),
    Round25CaseCandidate("charles_river_funding_crunch_4c", "CRO_CLINICAL_SERVICE", "CRL", "Charles River funding crunch", "US", "4c_thesis_break", ("biotech_service_revenue",), ("biotech_funding_cycle_down", "forecast_cut"), "Funding crunch can turn CRO visibility into 4C."),
    Round25CaseCandidate("biotech_customer_budget_cut_counterexample", "CRO_CLINICAL_SERVICE", "CRO_BUDGET_CUT", "바이오고객예산축소", "US", "failed_rerating", ("clinical_volume",), ("customer_budget_cut", "volume_without_margin"), "Clinical volume is insufficient if customer budgets decline."),
    Round25CaseCandidate("cro_customer_diversification_success_candidate", "CRO_CLINICAL_SERVICE", "CRO_DIVERSIFIED", "CRO 고객다변화", "KR", "success_candidate", ("customer_diversification", "repeat_service_revenue"), ("funding_cycle", "customer_concentration"), "Diversified customers can improve CRO visibility."),
    Round25CaseCandidate("qcells_us_supply_chain_candidate", "SOLAR_TARIFF_SUPPLYCHAIN", "009830", "한화솔루션 Qcells 미국공급망", "KR", "success_candidate", ("us_factory_investment", "solar_policy"), ("customs_detention", "component_delay"), "US supply-chain candidate needs utilization and component-flow backfill."),
    Round25CaseCandidate("qcells_customs_detention_4c", "SOLAR_TARIFF_SUPPLYCHAIN", "QCELLS_CUSTOMS", "Qcells 통관억류", "KR", "4c_thesis_break", ("solar_factory_capacity",), ("customs_detention", "factory_furlough"), "Customs detention can break solar policy-benefit thesis."),
    Round25CaseCandidate("solar_subsidy_dependency_counterexample", "SOLAR_TARIFF_SUPPLYCHAIN", "SOLAR_SUBSIDY", "태양광보조금의존", "KR", "failed_rerating", ("subsidy_expectation",), ("subsidy_dependency", "policy_reversal"), "Subsidy expectation alone is not Green evidence."),
    Round25CaseCandidate("solar_component_tariff_risk", "SOLAR_TARIFF_SUPPLYCHAIN", "SOLAR_TARIFF", "태양광부품관세리스크", "KR", "failed_rerating", ("solar_component_supply",), ("tariff", "component_delay"), "Tariff and component risk cap rerating."),
    Round25CaseCandidate("convenience_store_pb_efficiency_candidate", "RETAIL_ECOMMERCE_LOGISTICS", "CONV_PB", "편의점_PB효율", "KR", "success_candidate", ("same_store_sales_recovery", "pb_mix", "opm_improvement"), ("rent_labor_pressure", "competition"), "Convenience stores need store economics and OPM."),
    Round25CaseCandidate("ecommerce_logistics_scale_candidate", "RETAIL_ECOMMERCE_LOGISTICS", "ECOM_SCALE", "이커머스물류규모", "KR", "success_candidate", ("logistics_scale", "repeat_customer_base"), ("logistics_cost", "supplier_regulation"), "Scale must convert into cost leverage and FCF."),
    Round25CaseCandidate("ecommerce_fresh_loss_counterexample", "RETAIL_ECOMMERCE_LOGISTICS", "FRESH_LOSS", "신선식품이커머스적자", "KR", "failed_rerating", ("ecommerce_sales_growth",), ("fresh_delivery_loss", "logistics_cost_up"), "Fresh e-commerce sales without FCF remains Watch."),
    Round25CaseCandidate("supplier_regulation_margin_risk", "RETAIL_ECOMMERCE_LOGISTICS", "SUPPLIER_REG", "공급업체규제마진리스크", "KR", "failed_rerating", ("platform_scale",), ("supplier_regulation", "payment_delay"), "Supplier pressure is not structural margin quality."),
    Round25CaseCandidate("samsung_fire_underwriting_valueup_candidate", "INSURANCE_UNDERWRITING_CYCLE", "000810", "삼성화재 underwriting value-up", "KR", "success_candidate", ("loss_ratio_stability", "roe", "shareholder_return"), ("loss_ratio_worsens", "capital_ratio_down"), "Insurance candidate needs CSM/K-ICS and return execution backfill."),
    Round25CaseCandidate("db_insurance_loss_ratio_candidate", "INSURANCE_UNDERWRITING_CYCLE", "005830", "DB손해보험 손해율", "KR", "success_candidate", ("loss_ratio_stability", "roe", "capital_ratio"), ("underwriting_deterioration", "return_retreat"), "Loss ratio and ROE candidate."),
    Round25CaseCandidate("low_pbr_insurer_no_capital_return_counterexample", "INSURANCE_UNDERWRITING_CYCLE", "INS_LOW_PBR", "저PBR보험_환원부재", "KR", "failed_rerating", ("low_pbr",), ("capital_return_limited", "low_roe"), "Low PBR without return execution is value trap risk."),
    Round25CaseCandidate("insurance_cyber_operational_risk_4c", "INSURANCE_UNDERWRITING_CYCLE", "INS_CYBER_4C", "보험사이버운영리스크", "KR", "4c_thesis_break", ("insurance_infrastructure",), ("cyber_operational_risk", "service_outage"), "Cyber operation failure can break insurance/financial infrastructure thesis."),
    Round25CaseCandidate("medical_ai_external_validation_candidate", "DIGITAL_HEALTHCARE_AI", "MED_AI_VALID", "의료AI외부검증", "KR", "success_candidate", ("external_clinical_validation", "medical_imaging_ai"), ("no_reimbursement", "clinical_validation_gap"), "Clinical AI needs paid workflow and revenue conversion."),
    Round25CaseCandidate("medical_ai_no_reimbursement_counterexample", "DIGITAL_HEALTHCARE_AI", "MED_AI_NO_PAY", "의료AI_수가부재", "KR", "failed_rerating", ("clinical_ai_paper",), ("no_reimbursement", "no_paid_usage"), "No reimbursement blocks Green."),
    Round25CaseCandidate("hospital_ai_poc_no_revenue_counterexample", "DIGITAL_HEALTHCARE_AI", "HOSP_AI_POC", "병원AI_PoC_무매출", "KR", "failed_rerating", ("poc", "hospital_trial"), ("poc_only", "no_revenue_conversion"), "PoC without revenue remains Stage 1/2."),
    Round25CaseCandidate("medical_ai_liability_risk_4c", "DIGITAL_HEALTHCARE_AI", "MED_AI_LIABILITY", "의료AI책임리스크", "KR", "4c_thesis_break", ("medical_ai_response",), ("liability", "clinical_validation_gap"), "Liability or validation failure can break medical AI thesis."),
    Round25CaseCandidate("ess_shift_candidate", "BATTERY_RECYCLING_ESS_SHIFT", "ESS_SHIFT", "ESS 전환 후보", "KR", "success_candidate", ("ess_shift", "customer_contract"), ("ev_demand_slowdown", "capex_overbuild"), "ESS shift can be a candidate if customers and utilization are visible."),
    Round25CaseCandidate("ev_demand_slowdown_4c", "BATTERY_RECYCLING_ESS_SHIFT", "EV_SLOW_4C", "EV수요둔화4C", "KR", "4c_thesis_break", ("ev_battery_capacity",), ("ev_demand_slowdown", "margin_compression"), "EV slowdown can break battery CAPA thesis."),
    Round25CaseCandidate("battery_recycling_no_volume_counterexample", "BATTERY_RECYCLING_ESS_SHIFT", "RECYCLING_NO_VOL", "폐배터리물량부재", "KR", "failed_rerating", ("battery_recycling_policy",), ("no_volume", "no_commercialization"), "Recycling policy without volume is not structural evidence."),
    Round25CaseCandidate("solid_state_no_commercialization_counterexample", "BATTERY_RECYCLING_ESS_SHIFT", "SOLID_NO_COMM", "전고체무상용화", "KR", "failed_rerating", ("solid_state_theme",), ("commercialization_delay", "no_revenue_conversion"), "Solid-state theme remains Watch before commercialization."),
    Round25CaseCandidate("brokerage_trading_value_rally_candidate", "SECURITIES_BROKERAGE_CYCLE", "BROKER_TURNOVER", "거래대금회복_증권사", "KR", "success_candidate", ("trading_value_growth", "brokerage_revenue_growth"), ("turnover_peak", "pf_loss"), "Brokerage candidate requires revenue and PF risk confirmation."),
    Round25CaseCandidate("securities_pf_loss_4c", "SECURITIES_BROKERAGE_CYCLE", "BROKER_PF_4C", "증권사_PF손실", "KR", "4c_thesis_break", ("brokerage_balance_sheet",), ("pf_loss", "capital_ratio_down"), "PF loss can override trading-value recovery."),
    Round25CaseCandidate("ipo_pipeline_recovery_candidate", "SECURITIES_BROKERAGE_CYCLE", "IPO_PIPE", "IPO파이프라인회복", "KR", "success_candidate", ("ipo_pipeline", "ib_fee_growth"), ("pipeline_delay", "market_turnover_peak"), "IPO recovery needs actual fee conversion."),
    Round25CaseCandidate("vc_exit_market_weakness_counterexample", "SECURITIES_BROKERAGE_CYCLE", "VC_EXIT_WEAK", "VC회수시장부진", "KR", "failed_rerating", ("vc_portfolio",), ("exit_market_weakness", "valuation_markdown"), "VC recovery expectation without exits stays Watch."),
    Round25CaseCandidate("sk_hynix_hbm_success_case", "MEMORY_HBM_CAPACITY", "000660", "SK하이닉스 HBM", "KR", "structural_success", ("hbm_demand", "supply_discipline", "medium_term_revision"), ("capex_reversal", "memory_price_down"), "HBM structural success candidate; exact price path must be source-filled."),
    Round25CaseCandidate("sk_hynix_4b_crowding_watch", "MEMORY_HBM_CAPACITY", "000660", "SK하이닉스 4B crowding", "KR", "4b_watch", ("one_to_two_year_price_surge", "global_crowding", "market_cap_multiple_saturation"), ("capex_reversal", "revision_slowdown"), "Successful HBM rerating needs 4B-watch after large price move."),
    Round25CaseCandidate("simple_dram_rebound_counterexample", "MEMORY_HBM_CAPACITY", "DRAM_REBOUND", "단순DRAM반등", "KR", "failed_rerating", ("memory_price_rebound",), ("no_medium_term_revision", "cycle_only"), "Simple DRAM rebound is cyclical unless medium-term evidence exists."),
    Round25CaseCandidate("ai_capex_cut_memory_4c", "MEMORY_HBM_CAPACITY", "MEMORY_CAPEX_4C", "AI_CAPEX둔화_메모리", "KR", "4c_thesis_break", ("hbm_exposure",), ("customer_ai_capex_slowdown", "memory_price_down"), "Customer AI CAPEX slowdown is a hard memory risk."),
)


def target_for(target_id: str) -> Round25ScoreTarget | None:
    for target in ROUND25_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round25_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND25_CASE_CANDIDATES:
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
                f"Round25 v1.0 calibration candidate for {candidate.target_id}; "
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


def round25_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND25_SCORE_TARGETS:
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


def round25_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND25_CASE_CANDIDATES:
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


def round25_summary() -> dict[str, int | bool]:
    records = round25_case_records()
    positive = sum(1 for record in records if record.case_type in {"success_candidate", "structural_success"})
    stage4c = sum(1 for record in records if record.case_type == "4c_thesis_break")
    stage4b = sum(1 for record in records if record.case_type == "4b_watch")
    return {
        "target_count": len(ROUND25_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": len(records) - positive,
        "stage4b_case_count": stage4b,
        "stage4c_case_count": stage4c,
        "green_possible_count": sum(1 for target in ROUND25_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND25_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round25_score_weight_reports(
    *,
    output_directory: str | Path = ROUND25_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND25_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND25_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round25_score_weight_v10_summary.md",
        "case_matrix": output / "round25_case_candidate_matrix.csv",
        "green_guardrails": output / "round25_green_guardrail_review.md",
        "stage4b_watch": output / "round25_stage4b_watch_review.md",
        "risk_boundary": output / "round25_risk_boundary_review.md",
        "price_validation_plan": output / "round25_price_validation_plan.md",
    }
    _write_case_jsonl(round25_case_records(), cases)
    _write_rows(round25_score_profile_rows(), score_profiles)
    _write_rows(round25_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round25_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round25_green_guardrail_markdown(), encoding="utf-8")
    paths["stage4b_watch"].write_text(render_round25_stage4b_watch_markdown(), encoding="utf-8")
    paths["risk_boundary"].write_text(render_round25_risk_boundary_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round25_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round25_summary_markdown() -> str:
    summary = round25_summary()
    lines = [
        "# Round-25 Score-Weight v1.0 Summary",
        "",
        f"- source_round: `{ROUND25_SOURCE_ROUND_PATH}`",
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
        "- Round 25 expands v1.0 calibration, not production scoring.",
        "- Example: AI cooling needs direct data-center CAPEX linkage, orders, delivery, service revenue, and OP revision.",
        "- Example: security SaaS can have recurring revenue, but a major outage is hard 4C evidence.",
        "- Example: HBM can be Green, but successful rerating must turn on 4B-watch after crowding or multiple saturation.",
        "- Theme names, case IDs, policies, PoCs, and revenue growth headlines are not score evidence by themselves.",
    ]
    return "\n".join(lines) + "\n"


def render_round25_green_guardrail_markdown() -> str:
    lines = [
        "# Round-25 Green Guardrail Review",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "|---|---|---|---|",
    ]
    for target in ROUND25_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply v1.0 weights to production scoring yet.",
            "- Do not score policies, AI features, PoCs, revenue headlines, or theme labels without source-backed economics.",
            "- Do not invent stage dates, prices, margins, retention, FCF, reimbursement, or contract values.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round25_stage4b_watch_markdown() -> str:
    hbm = target_for("MEMORY_HBM_CAPACITY")
    cooling = target_for("AI_DATA_CENTER_COOLING")
    lines = [
        "# Round-25 4B Watch Review",
        "",
        "Round 25 keeps Green strict while making successful AI/HBM rerating monitoring explicit.",
        "",
        "## MEMORY_HBM_CAPACITY",
    ]
    if hbm:
        lines.extend(f"- {item}" for item in hbm.stage4b_conditions)
    lines.append("")
    lines.append("## AI_DATA_CENTER_COOLING")
    if cooling:
        lines.extend(f"- {item}" for item in cooling.stage4b_conditions)
    lines.extend(
        [
            "",
            "## Rule",
            "- Price-only warning remains `price_only_4b_watch`, not full evidence-based 4B.",
            "- Full 4B requires crowding, saturation, order slowdown, revision slowdown, capex reversal, or other deterioration evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round25_risk_boundary_markdown() -> str:
    lines = [
        "# Round-25 Risk Boundary Review",
        "",
        "Round 25 separates Green-possible structures from Watch-first or 4C-heavy structures.",
        "",
        "## Green-Possible With Strict Gates",
    ]
    for target in ROUND25_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.GREEN_POSSIBLE:
            lines.append(f"- {target.target_id}: {target.normalization_point}")
    lines.extend(["", "## Watch-First / 4C-Sensitive"])
    for target in ROUND25_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST:
            lines.append(f"- {target.target_id}: {', '.join(target.stage4c_conditions)}")
    lines.extend(
        [
            "",
            "## Rule",
            "- Stage 3-Green still requires cross-evidence and price-path validation.",
            "- Security outages, medical liability, solar customs detention, funding crunch, and AI CAPEX cuts are hard 4C-style examples.",
            "- 4B/4C cases are calibration examples, not production labels.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round25_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-25 Price Validation Plan",
            "",
            "1. Backfill tradable case price paths where symbols exist.",
            "2. Keep policy, synthetic, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.",
            "3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.",
            "4. Run shadow score-price alignment before production scoring changes.",
            "",
            "## Priority Validation",
            "- AI cooling: order/delivery/service revenue versus AI CAPEX delay and project margin damage.",
            "- Security: recurring subscription versus major outage and legal trust break.",
            "- HBM: structural EPS success versus crowding, market-cap saturation, and capex reversal.",
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
    "ROUND25_CASE_CANDIDATES",
    "ROUND25_DEFAULT_CASES_PATH",
    "ROUND25_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND25_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND25_SCORE_TARGETS",
    "ROUND25_SOURCE_ROUND_PATH",
    "Round25CaseCandidate",
    "Round25ScoreTarget",
    "Round25ScoreWeightDraft",
    "render_round25_green_guardrail_markdown",
    "render_round25_price_validation_plan_markdown",
    "render_round25_risk_boundary_markdown",
    "render_round25_stage4b_watch_markdown",
    "render_round25_summary_markdown",
    "round25_case_candidate_rows",
    "round25_case_records",
    "round25_score_profile_rows",
    "round25_summary",
    "target_for",
    "write_round25_score_weight_reports",
]
