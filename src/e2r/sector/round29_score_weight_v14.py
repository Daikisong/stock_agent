"""Round-29 cases_v11 expansion and score-weight v1.4 hypotheses.

Round 29 strengthens thin archetypes around defense, shipbuilding, K-food,
rail, petrochemicals, digital assets, security, ecommerce, battery/ESS, and
financial value-up. It is report-only calibration material. Production feature
engineering, scoring, staging, and RedTeam code must not import this module.
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


ROUND29_SOURCE_ROUND_PATH = "docs/round/round_29.md"
ROUND29_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round29_score_weight_v14"
ROUND29_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v11_round29.jsonl"
ROUND29_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round29_v14.csv"


@dataclass(frozen=True)
class Round29ScoreWeightDraft:
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
class Round29ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round29ScoreWeightDraft
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
class Round29CaseCandidate:
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


ROUND29_SCORE_TARGETS: tuple[Round29ScoreTarget, ...] = (
    Round29ScoreTarget(
        "DEFENSE_GOVERNMENT_BACKLOG",
        Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round29ScoreWeightDraft(20, 24, 17, 14, 14, 3, 5),
        ("government_contract_news", "geopolitical_budget_growth", "defense_export_keyword"),
        ("order_backlog_growth", "delivery_schedule", "op_eps_revision", "export_customer"),
        ("multi_year_government_backlog", "delivery_visibility", "opm_improvement", "capital_allocation_clean"),
        ("government_customer", "multi_year_contract", "order_backlog_to_sales", "delivery_schedule", "opm_improvement", "dilution_risk_low"),
        ("delivery_delay", "cost_overrun", "political_or_export_permit", "dilution", "theme_only"),
        ("contract_cancelled", "delivery_delay", "cost_overrun", "export_permit_blocked", "dilution_value_damage"),
        "Defense can be Green, but backlog, delivery, margin, and capital allocation must be source-backed.",
    ),
    Round29ScoreTarget(
        "SHIPBUILDING_OFFSHORE_BACKLOG",
        Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round29ScoreWeightDraft(20, 22, 18, 13, 13, 1, 5),
        ("newbuilding_price", "ship_order_news", "lng_or_offshore_keyword"),
        ("low_margin_backlog_rolloff", "high_margin_delivery_start", "op_eps_revision", "yard_slot_visibility"),
        ("orderbook_quality_improves", "pricing_reflects_in_fy2_fy3", "cost_pressure_controlled"),
        ("newbuilding_price_up", "low_margin_backlog_rolloff", "high_margin_delivery_start", "op_eps_revision", "contract_cancellation_risk_low"),
        ("low_margin_backlog", "steel_plate_cost", "labor_cost", "contract_cancellation", "order_slowdown"),
        ("contract_cancellation", "steel_plate_or_labor_cost_spike", "delivery_delay", "new_order_slowdown"),
        "Shipbuilding needs price and margin recognition; backlog quantity alone is not Green evidence.",
    ),
    Round29ScoreTarget(
        "EXPORT_RECURRING_CONSUMER",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.EXPORT_RECURRING_CONSUMER,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round29ScoreWeightDraft(22, 23, 12, 16, 13, 0, 5),
        ("export_growth", "overseas_channel_news", "earnings_surprise", "asp_increase"),
        ("fy1_fy2_eps_revision", "export_mix_increase", "opm_expansion", "channel_expansion"),
        ("repeat_demand", "channel_diversification", "asp_holds", "capacity_and_volume_scale"),
        ("repeat_consumer_demand", "overseas_channel_expansion", "opm_expansion", "fy1_fy2_eps_revision", "inventory_risk_low"),
        ("single_product", "inventory", "recall_or_regulation", "asp_drop", "channel_stuffing"),
        ("export_growth_slowdown", "inventory_build", "asp_or_opm_drop", "recall_or_regulatory_hit"),
        "Export consumer Green does not require contract quality; repeat demand and channel evidence matter.",
    ),
    Round29ScoreTarget(
        "RAIL_INFRASTRUCTURE",
        Round10LargeSector.INDUSTRIAL_ORDERS_INFRA,
        E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round29ScoreWeightDraft(20, 23, 12, 14, 12, 1, 5),
        ("rail_order_news", "rail_policy", "reconstruction_or_transit_theme"),
        ("actual_contract", "delivery_schedule", "customer_diversification", "op_eps_revision_possible"),
        ("large_contract_to_sales", "delivery_visibility", "margin_visible", "financing_risk_low"),
        ("actual_contract", "contract_amount_to_sales", "delivery_schedule", "margin_visible", "financing_risk_low"),
        ("policy_theme_only", "mou_only", "project_delay", "margin_uncertainty", "financing"),
        ("project_delay", "margin_miss", "financing_failure", "contract_cancelled"),
        "Rail is contract-backlog style, but project margin, delivery, and financing deserve stronger gates.",
    ),
    Round29ScoreTarget(
        "CHEMICAL_SPREAD",
        Round10LargeSector.MATERIALS_SPREAD_STRATEGIC,
        E2RArchetype.COMMODITY_SPREAD,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round29ScoreWeightDraft(20, 8, 16, 8, 8, 0, 5),
        ("product_spread_recovery", "raw_material_cost_down", "petrochemical_cycle_keyword"),
        ("spread_improves", "inventory_normalizes", "cost_control", "op_fcf_improvement"),
        ("supply_glut_eases", "structural_capacity_closure", "spread_sustained"),
        ("spread_sustained", "supply_glut_eases", "op_fcf_improvement", "inventory_risk_low"),
        ("china_middle_east_overcapacity", "spread_reversal", "inventory", "demand_slowdown"),
        ("spread_reversal", "capacity_glut", "inventory_build", "demand_slowdown"),
        "Chemicals stay Watch-first because spread recovery can reverse before structural visibility appears.",
    ),
    Round29ScoreTarget(
        "DIGITAL_ASSET_TOKENIZATION",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round29ScoreWeightDraft(16, 18, 8, 16, 12, 3, 5),
        ("stablecoin_keyword", "sto_policy", "payment_network", "ipo_or_global_fintech"),
        ("regulatory_approval", "issuance_or_transaction_volume", "fee_model", "payment_network_adoption"),
        ("repeat_financial_infra_revenue", "regulatory_risk_low", "security_risk_low", "liquidity_visible"),
        ("regulatory_approval", "transaction_volume", "fee_model", "payment_network_adoption", "security_risk_low"),
        ("regulation", "security", "adoption", "liquidity", "no_revenue", "coin_theme_only"),
        ("regulatory_delay", "security_incident", "liquidity_collapse", "no_revenue_model"),
        "Stablecoin/STO can be researched, but regulation, volume, and fee revenue must arrive before Green.",
    ),
    Round29ScoreTarget(
        "SECURITY_IDENTITY_DEEPFAKE",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round29ScoreWeightDraft(20, 20, 10, 14, 13, 0, 5),
        ("security_demand", "deepfake_identity_keyword", "enterprise_contract"),
        ("recurring_subscription_revenue", "low_churn", "customer_diversification", "opm_improvement"),
        ("mission_critical_retention", "public_or_enterprise_contracts", "operational_trust_intact"),
        ("recurring_subscription_revenue", "low_churn", "customer_diversification", "opm_improvement", "operational_trust_intact"),
        ("operational_trust", "outage", "legal", "customer_retention", "theme_only"),
        ("major_outage", "lawsuit", "customer_churn", "trust_loss"),
        "Security can be Green with recurring revenue, but operational trust is a hard gate.",
    ),
    Round29ScoreTarget(
        "RETAIL_ECOMMERCE_LOGISTICS",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round29ScoreWeightDraft(18, 16, 5, 13, 14, 3, 5),
        ("ecommerce_scale", "logistics_network", "repeat_customer", "retail_turnaround"),
        ("opm_improvement", "logistics_cost_stable", "inventory_normalizes", "high_margin_mix"),
        ("fcf_conversion", "customer_repeatability", "regulation_risk_low", "competition_risk_low"),
        ("opm_improvement", "fcf_conversion", "repeat_customer", "inventory_normalizes", "data_security_risk_low"),
        ("logistics_cost", "inventory", "supplier_regulation", "data_security", "competition", "revenue_only_growth"),
        ("data_security_breach", "supplier_regulation_hit", "logistics_cost_spike", "inventory_build"),
        "Retail/ecommerce should score OPM and FCF, not revenue scale alone.",
    ),
    Round29ScoreTarget(
        "BATTERY_MATERIALS_ESS",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round29ScoreWeightDraft(20, 16, 14, 10, 10, 0, 5),
        ("ess_demand", "battery_recycling_keyword", "battery_materials_contract", "ev_policy"),
        ("customer_contract", "ess_revenue", "recycling_volume", "fcf_safe_capex"),
        ("demand_visibility", "price_or_margin_stable", "capex_overbuild_risk_low"),
        ("customer_contract", "demand_visibility", "margin_stable", "recycling_volume", "fcf_safe_capex"),
        ("ev_demand", "mineral_price", "capex_overbuild", "policy", "recycling_volume_missing"),
        ("ev_demand_slowdown", "mineral_price_collapse", "capex_overbuild", "policy_reversal"),
        "Battery/ESS remains Stage-2 possible but Green-restricted while EV demand and CAPEX risks dominate.",
    ),
    Round29ScoreTarget(
        "INSURANCE_UNDERWRITING",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round29ScoreWeightDraft(15, 21, 4, 15, 25, 10, 5),
        ("low_pbr", "insurance_valueup", "csm_growth", "shareholder_return"),
        ("roe_improvement", "csm_or_underwriting_quality", "capital_ratio_stable", "actual_return_policy"),
        ("pbr_roe_rerating", "repeat_return_execution", "loss_ratio_stable", "capital_ratio_safe"),
        ("roe_improvement", "csm_or_underwriting_quality", "capital_ratio_stable", "actual_return_policy", "credit_cost_low"),
        ("underwriting", "capital_ratio", "cyber_operational", "credit_cost", "low_roe"),
        ("loss_ratio_deterioration", "capital_ratio_hit", "credit_cost_spike", "operational_incident"),
        "Insurance is PBR-ROE-return rerating, not classic EPS explosion; underwriting and capital safety are gates.",
    ),
    Round29ScoreTarget(
        "SECURITIES_BROKERAGE",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round29ScoreWeightDraft(18, 14, 5, 15, 18, 8, 5),
        ("trading_value_rally", "ipo_cycle_recovery", "brokerage_valueup"),
        ("market_turnover_sustained", "ib_recovery", "shareholder_return", "pf_risk_low"),
        ("repeat_earnings_cycle", "capital_allocation_visible", "pf_risk_contained"),
        ("market_turnover_sustained", "ib_recovery", "shareholder_return", "pf_risk_low"),
        ("market_turnover", "pf", "proprietary_loss", "ipo_cycle", "cycle_only"),
        ("pf_loss", "proprietary_loss", "turnover_collapse", "ipo_cycle_freeze"),
        "Securities can be Watch, but turnover and IB cycles cap Green unless repeat earnings and risk controls show up.",
    ),
    Round29ScoreTarget(
        "VALUE_UP_SHAREHOLDER",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round29ScoreWeightDraft(12, 18, 4, 20, 25, 10, 5),
        ("low_pbr", "valueup_policy", "buyback_or_dividend", "nav_discount"),
        ("roe_improvement", "actual_cancellation", "repeat_shareholder_return", "dividend_sustainability"),
        ("pbr_roe_frame_change", "capital_return_execution", "nav_discount_close", "fcf_support"),
        ("roe_improvement", "actual_cancellation", "repeat_shareholder_return", "dividend_sustainability", "fcf_support"),
        ("governance", "execution", "low_roe", "no_cancellation", "index_inclusion_only"),
        ("return_execution_failure", "roe_deterioration", "governance_risk", "fcf_shortfall"),
        "Value-up needs actual return execution and ROE/NAV improvement; low PBR or index label is not enough.",
    ),
)


ROUND29_CASE_CANDIDATES: tuple[Round29CaseCandidate, ...] = (
    Round29CaseCandidate("hanwha_aerospace_romania_k9_success_case", "DEFENSE_GOVERNMENT_BACKLOG", "012450", "한화에어로스페이스 루마니아 K9", "KR", "structural_success", ("government_customer", "multi_year_contract", "order_backlog_to_sales", "delivery_schedule"), ("delivery_delay", "political_or_export_permit"), "Government export backlog with delivery visibility; price data remains unfilled."),
    Round29CaseCandidate("hanwha_aerospace_dilution_capital_allocation_risk", "DEFENSE_GOVERNMENT_BACKLOG", "012450_DILUTION", "한화에어로스페이스 Dilution Risk", "KR", "failed_rerating", ("order_backlog_growth", "overseas_expansion"), ("dilution", "capital_allocation_risk"), "Defense backlog still needs capital allocation guardrails."),
    Round29CaseCandidate("defense_theme_no_backlog_counterexample", "DEFENSE_GOVERNMENT_BACKLOG", "DEF_THEME", "방산테마_무수주잔고", "KR", "failed_rerating", ("defense_export_keyword",), ("theme_only", "no_backlog"), "Defense keyword without government customer or backlog is not Green evidence."),
    Round29CaseCandidate("defense_cost_delay_4c", "DEFENSE_GOVERNMENT_BACKLOG", "DEF_DELAY_4C", "방산원가납기지연4C", "KR", "4c_thesis_break", ("government_contract_news",), ("delivery_delay", "cost_overrun"), "Cost and delivery failure can break a defense thesis."),
    Round29CaseCandidate("samsung_heavy_shipbuilding_rally_success_candidate", "SHIPBUILDING_OFFSHORE_BACKLOG", "010140", "삼성중공업 조선 랠리 후보", "KR", "success_candidate", ("newbuilding_price_up", "ship_order_news"), ("steel_plate_cost", "contract_cancellation"), "Shipbuilding rally candidate needs margin and delivery price recognition."),
    Round29CaseCandidate("hd_hyundai_shipbuilding_newbuilding_price_candidate", "SHIPBUILDING_OFFSHORE_BACKLOG", "329180", "HD현대중공업 신조선가 후보", "KR", "success_candidate", ("newbuilding_price_up", "yard_slot_visibility"), ("labor_cost", "order_slowdown"), "Newbuilding price and yard slot evidence require price-path backfill."),
    Round29CaseCandidate("low_margin_backlog_counterexample", "SHIPBUILDING_OFFSHORE_BACKLOG", "SHIP_LOWMARGIN", "저마진수주잔고 반례", "KR", "failed_rerating", ("large_orderbook",), ("low_margin_backlog", "cost_pressure"), "Backlog quantity can be misleading when margins are weak."),
    Round29CaseCandidate("shipbuilding_cost_inflation_4c", "SHIPBUILDING_OFFSHORE_BACKLOG", "SHIP_COST_4C", "조선원가상승4C", "KR", "4c_thesis_break", ("ship_order_news",), ("steel_plate_or_labor_cost_spike", "delivery_delay"), "Steel/labor cost shock can break the shipbuilding rerating thesis."),
    Round29CaseCandidate("samyang_buldak_export_rerating_success", "EXPORT_RECURRING_CONSUMER", "003230", "삼양식품 불닭 수출", "KR", "structural_success", ("export_growth", "asp_increase", "capacity_and_volume_scale", "opm_expansion"), ("single_product", "recall_or_regulation"), "K-food success candidate: export, ASP, CAPA, OPM, and EPS need source-backed linkage."),
    Round29CaseCandidate("one_product_fad_counterexample", "EXPORT_RECURRING_CONSUMER", "FOOD_FAD", "단일제품유행 반례", "KR", "failed_rerating", ("viral_product",), ("single_product", "sell_through_unverified"), "Viral demand without repeat channel evidence is not structural visibility."),
    Round29CaseCandidate("export_inventory_channel_stuffing_4c", "EXPORT_RECURRING_CONSUMER", "FOOD_STUFF_4C", "수출재고채널스터핑4C", "KR", "4c_thesis_break", ("export_growth",), ("inventory_build", "channel_stuffing"), "Inventory and channel stuffing can break export-consumer visibility."),
    Round29CaseCandidate("consumer_recall_regulation_risk", "EXPORT_RECURRING_CONSUMER", "FOOD_RECALL", "소비재리콜규제위험", "KR", "failed_rerating", ("export_growth",), ("recall_or_regulation", "brand_damage"), "Regulatory/recall risk remains a RedTeam input even for strong exports."),
    Round29CaseCandidate("hyundai_rotem_morocco_rail_order_candidate", "RAIL_INFRASTRUCTURE", "064350", "현대로템 모로코 철도 수주", "KR", "success_candidate", ("actual_contract", "contract_amount_to_sales", "delivery_schedule"), ("margin_uncertainty", "financing"), "Large rail contract can route to Stage 2 when margin and delivery evidence exist."),
    Round29CaseCandidate("rail_policy_no_contract_counterexample", "RAIL_INFRASTRUCTURE", "RAIL_POLICY", "철도정책무계약 반례", "KR", "failed_rerating", ("rail_policy",), ("policy_theme_only", "no_contract"), "Rail policy without contract remains event/watch material."),
    Round29CaseCandidate("project_margin_uncertainty_4c", "RAIL_INFRASTRUCTURE", "RAIL_MARGIN_4C", "철도프로젝트마진불확실4C", "KR", "4c_thesis_break", ("actual_contract",), ("margin_miss", "project_delay"), "A big order can fail if margin or delivery breaks."),
    Round29CaseCandidate("reconstruction_rail_theme_event_watch", "RAIL_INFRASTRUCTURE", "RAIL_RECON", "재건철도테마 이벤트", "KR", "event_premium", ("reconstruction_or_transit_theme",), ("mou_only", "financing"), "Reconstruction rail theme is event premium without a funded contract."),
    Round29CaseCandidate("lotte_chemical_oversupply_4c", "CHEMICAL_SPREAD", "011170", "롯데케미칼 공급과잉", "KR", "4c_thesis_break", ("petrochemical_cycle_keyword",), ("capacity_glut", "spread_reversal"), "Supply glut and spread reversal are 4C-style petrochemical evidence."),
    Round29CaseCandidate("lg_chem_petrochemical_margin_pressure", "CHEMICAL_SPREAD", "051910_PC", "LG화학 석화마진압박", "KR", "failed_rerating", ("raw_material_cost_down",), ("china_middle_east_overcapacity", "margin_pressure"), "Margin pressure caps chemical spread recovery."),
    Round29CaseCandidate("chemical_spread_recovery_candidate", "CHEMICAL_SPREAD", "CHEM_SPREAD", "화학스프레드회복 후보", "KR", "success_candidate", ("product_spread_recovery", "op_fcf_improvement"), ("spread_reversal", "inventory"), "Spread recovery can reach Watch/Stage 2 if sustained and source-backed."),
    Round29CaseCandidate("china_middle_east_capacity_glut_counterexample", "CHEMICAL_SPREAD", "CHEM_GLUT", "중국중동증설반례", "KR", "failed_rerating", ("petrochemical_cycle_keyword",), ("china_middle_east_overcapacity", "demand_slowdown"), "Capacity glut makes Green highly restricted."),
    Round29CaseCandidate("toss_won_stablecoin_candidate", "DIGITAL_ASSET_TOKENIZATION", "TOSS_STABLE", "토스 원화 스테이블코인", "KR", "success_candidate", ("stablecoin_keyword", "payment_network"), ("regulation", "no_revenue"), "Stablecoin candidate is Watch until approval, volume, and fee revenue are visible."),
    Round29CaseCandidate("stablecoin_regulatory_delay_4c", "DIGITAL_ASSET_TOKENIZATION", "STABLE_DELAY_4C", "스테이블코인규제지연4C", "KR", "4c_thesis_break", ("stablecoin_keyword",), ("regulatory_delay", "liquidity_collapse"), "Regulatory delay can break tokenization revenue expectations."),
    Round29CaseCandidate("sto_no_revenue_counterexample", "DIGITAL_ASSET_TOKENIZATION", "STO_NOREV", "STO무매출반례", "KR", "failed_rerating", ("sto_policy",), ("no_revenue", "adoption_missing"), "STO policy without fee revenue is not E2R evidence."),
    Round29CaseCandidate("crypto_theme_no_revenue_counterexample", "DIGITAL_ASSET_TOKENIZATION", "CRYPTO_THEME", "코인테마무매출", "KR", "failed_rerating", ("coin_theme_only",), ("coin_theme_only", "no_revenue"), "Crypto theme label is routing metadata, not scoring evidence."),
    Round29CaseCandidate("crowdstrike_outage_4c", "SECURITY_IDENTITY_DEEPFAKE", "CRWD_OUTAGE", "CrowdStrike 대형 장애", "US", "4c_thesis_break", ("recurring_subscription_revenue",), ("major_outage", "lawsuit", "trust_loss"), "Major outage is hard 4C-style security evidence."),
    Round29CaseCandidate("recurring_security_subscription_candidate", "SECURITY_IDENTITY_DEEPFAKE", "SEC_SUB", "보안 반복구독 후보", "KR", "success_candidate", ("recurring_subscription_revenue", "low_churn", "customer_diversification"), ("customer_churn", "outage"), "Recurring security revenue can score if operational trust remains intact."),
    Round29CaseCandidate("deepfake_regulation_stage1_candidate", "SECURITY_IDENTITY_DEEPFAKE", "DEEPFAKE_REG", "딥페이크규제 Stage1", "KR", "success_candidate", ("deepfake_identity_keyword", "public_or_enterprise_contracts"), ("theme_only", "no_contract"), "Deepfake regulation can create radar/search path, not Green by itself."),
    Round29CaseCandidate("security_theme_no_contract_counterexample", "SECURITY_IDENTITY_DEEPFAKE", "SEC_THEME", "보안테마무계약반례", "KR", "failed_rerating", ("security_demand",), ("theme_only", "no_contract"), "Security theme without contract or ARR remains Stage 1."),
    Round29CaseCandidate("coupang_scale_candidate", "RETAIL_ECOMMERCE_LOGISTICS", "CPNG", "쿠팡 규모 후보", "US", "success_candidate", ("ecommerce_scale", "repeat_customer", "opm_improvement"), ("logistics_cost", "data_security"), "Scale can score only through OPM and FCF conversion."),
    Round29CaseCandidate("coupang_data_security_4c", "RETAIL_ECOMMERCE_LOGISTICS", "CPNG_DATA_4C", "쿠팡데이터보안4C", "US", "4c_thesis_break", ("ecommerce_scale",), ("data_security_breach", "regulatory_hit"), "Data-security risk can break ecommerce trust and margins."),
    Round29CaseCandidate("coupang_supplier_regulation_risk", "RETAIL_ECOMMERCE_LOGISTICS", "CPNG_SUPPLIER", "쿠팡공급업체규제위험", "US", "failed_rerating", ("logistics_network",), ("supplier_regulation_hit", "competition"), "Supplier regulation can cap ecommerce rerating."),
    Round29CaseCandidate("ecommerce_growth_no_fcf_counterexample", "RETAIL_ECOMMERCE_LOGISTICS", "ECOM_NOFCF", "이커머스성장무FCF", "KR", "failed_rerating", ("revenue_only_growth",), ("logistics_cost", "fcf_absence"), "Revenue growth without FCF is not structural E2R."),
    Round29CaseCandidate("ess_shift_candidate", "BATTERY_MATERIALS_ESS", "ESS_SHIFT", "ESS 전환 후보", "KR", "success_candidate", ("ess_demand", "customer_contract"), ("policy", "capex_overbuild"), "ESS demand can be a Watch candidate if contract and margin evidence exist."),
    Round29CaseCandidate("battery_recycling_no_volume_counterexample", "BATTERY_MATERIALS_ESS", "RECY_NOVOL", "폐배터리물량부재반례", "KR", "failed_rerating", ("battery_recycling_keyword",), ("recycling_volume_missing", "no_revenue"), "Recycling theme needs actual collection volume and revenue."),
    Round29CaseCandidate("ev_demand_slowdown_4c", "BATTERY_MATERIALS_ESS", "EV_SLOW_4C", "EV수요둔화4C", "KR", "4c_thesis_break", ("battery_materials_contract",), ("ev_demand_slowdown", "mineral_price_collapse"), "EV demand slowdown is a hard risk for battery materials."),
    Round29CaseCandidate("capex_overbuild_4c", "BATTERY_MATERIALS_ESS", "BAT_CAPEX_4C", "2차전지CAPEX과잉4C", "KR", "4c_thesis_break", ("capacity_expansion",), ("capex_overbuild", "margin_compression"), "CAPEX overbuild can break battery material economics."),
    Round29CaseCandidate("insurer_underwriting_valueup_candidate", "INSURANCE_UNDERWRITING", "INS_VALUE", "보험언더라이팅밸류업", "KR", "success_candidate", ("roe_improvement", "csm_or_underwriting_quality", "actual_return_policy"), ("capital_ratio", "credit_cost"), "Insurance value-up needs ROE, CSM/underwriting, capital ratio, and real return execution."),
    Round29CaseCandidate("low_pbr_no_roe_value_trap", "VALUE_UP_SHAREHOLDER", "LOWPBR_NOROE", "저PBR무ROE가치함정", "KR", "failed_rerating", ("low_pbr",), ("low_roe", "weak_fcf"), "Low PBR alone is not value-up evidence."),
    Round29CaseCandidate("brokerage_trading_value_rally_candidate", "SECURITIES_BROKERAGE", "BROKER_TURN", "증권거래대금랠리후보", "KR", "success_candidate", ("trading_value_rally", "ib_recovery"), ("pf", "turnover_collapse"), "Brokerage cycle can be Watch if turnover and IB recovery are sustained."),
    Round29CaseCandidate("buyback_no_cancel_counterexample", "VALUE_UP_SHAREHOLDER", "BUYBACK_NOCANCEL", "자사주미소각반례", "KR", "failed_rerating", ("buyback_or_dividend",), ("no_cancellation", "execution"), "Buyback announcement without cancellation can be weak value-up evidence."),
)


def target_for(target_id: str) -> Round29ScoreTarget | None:
    for target in ROUND29_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round29_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND29_CASE_CANDIDATES:
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
                f"Round29 v1.4 calibration candidate for {candidate.target_id}; "
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
                "theme_label_is_not_score_evidence",
                *target.red_flags,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(price_validation_status="needs_price_backfill"),
            data_quality=CaseDataQuality(False, False, False, 0.0),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round29_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND29_SCORE_TARGETS:
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


def round29_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND29_CASE_CANDIDATES:
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


def round29_summary() -> dict[str, int | bool]:
    records = round29_case_records()
    positive = sum(1 for record in records if record.case_type in {"success_candidate", "structural_success"})
    stage4c = sum(1 for record in records if record.case_type == "4c_thesis_break")
    stage4b = sum(1 for record in records if record.case_type == "4b_watch")
    return {
        "target_count": len(ROUND29_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": len(records) - positive,
        "stage4b_case_count": stage4b,
        "stage4c_case_count": stage4c,
        "green_possible_count": sum(1 for target in ROUND29_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND29_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND29_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round29_score_weight_reports(
    *,
    output_directory: str | Path = ROUND29_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND29_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND29_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round29_score_weight_v14_summary.md",
        "case_matrix": output / "round29_case_candidate_matrix.csv",
        "green_guardrails": output / "round29_green_guardrail_review.md",
        "risk_boundary": output / "round29_risk_boundary_review.md",
        "capital_allocation": output / "round29_capital_allocation_risk_review.md",
        "price_validation_plan": output / "round29_price_validation_plan.md",
    }
    _write_case_jsonl(round29_case_records(), cases)
    _write_rows(round29_score_profile_rows(), score_profiles)
    _write_rows(round29_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round29_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round29_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_boundary"].write_text(render_round29_risk_boundary_markdown(), encoding="utf-8")
    paths["capital_allocation"].write_text(render_round29_capital_allocation_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round29_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round29_summary_markdown() -> str:
    summary = round29_summary()
    lines = [
        "# Round-29 Score-Weight v1.4 Summary",
        "",
        f"- source_round: `{ROUND29_SOURCE_ROUND_PATH}`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- counterexample_or_risk_count: {summary['counterexample_or_risk_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "- Round 29 adds v1.4 calibration cases and target weights only.",
        "- Example: defense backlog can be Green-possible, but dilution and capital allocation can still block conviction.",
        "- Example: K-food can pass visibility without contract quality when repeat demand, channels, ASP, OPM, and FY1/FY2 revisions are source-backed.",
        "- Example: chemicals, securities, digital assets, ecommerce, and battery/ESS remain Watch-first until cycle and risk evidence improve.",
        "- Theme names, case IDs, policies, search labels, and price rallies are not score evidence by themselves.",
    ]
    return "\n".join(lines) + "\n"


def render_round29_green_guardrail_markdown() -> str:
    lines = [
        "# Round-29 Green Guardrail Review",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "|---|---|---|---|",
    ]
    for target in ROUND29_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply v1.4 weights to production scoring yet.",
            "- Do not use case IDs or theme labels as candidate-generation input.",
            "- Do not invent stage dates, prices, contract size, contract duration, OP YoY, ASP, OPM, CSM, ROE, or transaction volume.",
            "- Do not lower Stage 3-Green thresholds to improve recall.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round29_risk_boundary_markdown() -> str:
    lines = [
        "# Round-29 Risk Boundary Review",
        "",
        "Round 29 separates Green-possible structures from Watch-first cycle/risk areas.",
        "",
        "## Green-Possible With Strict Gates",
    ]
    for target in ROUND29_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.GREEN_POSSIBLE:
            lines.append(f"- {target.target_id}: {target.normalization_point}")
    lines.extend(["", "## Watch-First / 4C-Sensitive"])
    for target in ROUND29_SCORE_TARGETS:
        if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST:
            lines.append(f"- {target.target_id}: {', '.join(target.stage4c_conditions)}")
    lines.extend(
        [
            "",
            "## Rule",
            "- Stage 3-Green still requires cross-evidence and price-path validation.",
            "- Chemicals, digital assets, ecommerce, battery/ESS, and securities are Watch-first because cycle, regulation, security, or FCF risk is high.",
            "- Defense, shipbuilding, export consumer, rail, security, insurance, and value-up are Green-possible only with source-backed economics.",
            "- Case records are calibration examples, not production labels.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round29_capital_allocation_markdown() -> str:
    return "\n".join(
        [
            "# Round-29 Capital Allocation Risk Review",
            "",
            "Round 29 explicitly adds capital-allocation guardrails where growth narratives can dilute or misallocate value.",
            "",
            "## Examples",
            "- Defense: order backlog is not enough if overseas expansion is funded through value-damaging dilution.",
            "- Insurance and value-up: actual return execution, capital ratio, ROE, cancellation, and FCF matter more than a low-PBR label.",
            "- Securities: market turnover can lift earnings, but PF/proprietary-loss risk and cycle exposure cap Green.",
            "- Ecommerce: scale is useful only when logistics cost, inventory, data security, and FCF conversion are controlled.",
            "",
            "## Guardrail",
            "- Capital allocation can support confidence, but it cannot replace EPS/FCF bodyweight change or structural visibility.",
        ]
    ) + "\n"


def render_round29_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-29 Price Validation Plan",
            "",
            "1. Backfill tradable case price paths where symbols exist.",
            "2. Keep synthetic, theme, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.",
            "3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.",
            "4. Run shadow score-price alignment before any production scoring change.",
            "",
            "## Priority Validation",
            "- Defense: Romania K9/order backlog versus dilution and capital allocation risk.",
            "- Shipbuilding: newbuilding price and orderbook quality versus low-margin backlog and cost inflation.",
            "- K-food: export/ASP/OPM/CAPA versus single-product, recall, inventory, and channel-stuffing risks.",
            "- Chemicals and batteries: spread/ESS candidates versus supply glut, EV slowdown, CAPEX overbuild, and mineral-price risk.",
            "- Finance/value-up: ROE, capital ratio, CSM, actual cancellation, and shareholder-return execution.",
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
    "ROUND29_CASE_CANDIDATES",
    "ROUND29_DEFAULT_CASES_PATH",
    "ROUND29_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND29_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND29_SCORE_TARGETS",
    "ROUND29_SOURCE_ROUND_PATH",
    "Round29CaseCandidate",
    "Round29ScoreTarget",
    "Round29ScoreWeightDraft",
    "render_round29_capital_allocation_markdown",
    "render_round29_green_guardrail_markdown",
    "render_round29_price_validation_plan_markdown",
    "render_round29_risk_boundary_markdown",
    "render_round29_summary_markdown",
    "round29_case_candidate_rows",
    "round29_case_records",
    "round29_score_profile_rows",
    "round29_summary",
    "target_for",
    "write_round29_score_weight_reports",
]
