"""Round-34 cases_v16 expansion and score-weight v1.9 hypotheses.

Round 34 fills market themes that are common but hard to score: carbon/CBAM,
payment fintech, AI data-center optical networking, telecom capex, lithium raw
materials, home appliance rental, AI accelerator pure-play, and mobility
rental/micromobility. It is report-only calibration material. Production
feature engineering, scoring, staging, and RedTeam code must not import this
module.
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


ROUND34_SOURCE_ROUND_PATH = "docs/round/round_34.md"
ROUND34_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round34_score_weight_v19"
ROUND34_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v16_round34.jsonl"
ROUND34_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round34_v19.csv"


@dataclass(frozen=True)
class Round34ScoreWeightDraft:
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
class Round34ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round34ScoreWeightDraft
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
class Round34CaseCandidate:
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


ROUND34_SCORE_TARGETS: tuple[Round34ScoreTarget, ...] = (
    Round34ScoreTarget(
        "CARBON_CREDIT_CBAM_COMPLIANCE",
        Round10LargeSector.POLICY_GEOPOLITICAL_EVENT,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round34ScoreWeightDraft(14, 17, 10, 12, 8, 2, 6),
        ("carbon_credit", "cbam", "carbon_accounting", "low_carbon_material"),
        ("pass_through_possible", "carbon_monitoring_recurring_revenue", "premium_low_carbon_product", "verified_customer_contract"),
        ("policy_design_stable", "fcf_from_compliance_or_cost_saving", "greenwashing_risk_low"),
        ("pass_through_possible", "carbon_monitoring_recurring_revenue", "premium_low_carbon_product", "fcf_from_compliance_or_cost_saving"),
        ("policy_change", "allowance_price_volatility", "greenwashing", "pass_through_failure", "offset_integrity"),
        ("allowance_price_collapse", "pass_through_failure", "greenwashing_scandal", "policy_reversal"),
        "Carbon/CBAM is Watch-first; Green requires cost pass-through, recurring compliance revenue, or premium low-carbon products.",
    ),
    Round34ScoreTarget(
        "PAYMENT_FINTECH_INFRA",
        Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round34ScoreWeightDraft(18, 20, 8, 14, 14, 2, 5),
        ("payment_volume", "pg_network", "e_wallet", "credit_information"),
        ("transaction_volume_growth", "take_rate_stable", "merchant_or_user_lock_in", "financial_service_attach"),
        ("profitable_or_fcf_conversion", "regulatory_risk_low", "security_risk_controlled"),
        ("transaction_volume_growth", "take_rate_stable", "merchant_or_user_lock_in", "profitable_or_fcf_conversion"),
        ("regulation", "take_rate_pressure", "credit_loss", "security", "competition", "user_count_only"),
        ("security_incident", "credit_loss_spike", "regulatory_restriction", "take_rate_collapse"),
        "Payment fintech can be Green-possible when volume, take rate, lock-in, attach revenue, and FCF are source-backed.",
    ),
    Round34ScoreTarget(
        "OPTICAL_NETWORKING_AI_DATACENTER",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round34ScoreWeightDraft(21, 22, 20, 13, 12, 0, 5),
        ("fiber_optic_cable", "optical_transceiver", "ai_datacenter_network", "hyperscaler_contract"),
        ("hyperscaler_long_contract", "direct_ai_datacenter_supply", "bottleneck_optical_component", "op_eps_revision"),
        ("capacity_expansion_margin_visible", "customer_concentration_controlled", "valuation_crowding_controlled"),
        ("hyperscaler_long_contract", "direct_ai_datacenter_supply", "bottleneck_optical_component", "op_eps_revision"),
        ("hyperscaler_concentration", "valuation_crowding", "capex_delay", "inventory", "unclear_ai_dc_exposure"),
        ("hyperscaler_order_cut", "capex_delay", "inventory_glut", "valuation_unwind"),
        "Optical networking can become an AI data-center Green axis only with hyperscaler contracts and actual delivery economics.",
    ),
    Round34ScoreTarget(
        "TELECOM_5G_6G_CAPEX_CYCLE",
        Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY,
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round34ScoreWeightDraft(16, 13, 8, 12, 9, 0, 5),
        ("5g_6g_policy", "telecom_equipment", "open_ran", "operator_capex"),
        ("confirmed_operator_capex", "equipment_order", "private_network_revenue", "ai_dc_network_extension"),
        ("operator_delay_risk_low", "geopolitical_risk_low", "security_review_cleared"),
        ("confirmed_operator_capex", "equipment_order", "private_network_revenue"),
        ("telecom_capex_cycle", "geopolitics", "security_review", "operator_delay", "policy_no_revenue"),
        ("capex_peak_out", "operator_delay", "security_ban", "geopolitical_restriction"),
        "Telecom 5G/6G equipment stays RedTeam-first and should not be scored like AI data-center optical networking.",
    ),
    Round34ScoreTarget(
        "LITHIUM_BATTERY_RAW_MATERIAL",
        Round10LargeSector.MATERIALS_SPREAD_STRATEGIC,
        E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round34ScoreWeightDraft(19, 10, 16, 9, 8, 0, 5),
        ("lithium_price", "battery_raw_material", "mine_restart", "ev_ess_demand"),
        ("low_cost_asset", "long_term_offtake", "demand_visible", "fcf_defense_at_low_price"),
        ("capex_disciplined", "mine_restart_risk_low", "oversupply_risk_low"),
        ("low_cost_asset", "long_term_offtake", "demand_visible", "fcf_defense_at_low_price"),
        ("lithium_price", "mine_restart", "ev_demand", "oversupply", "capex", "price_rebound_only"),
        ("price_crash", "oversupply", "mine_restart_supply", "ev_demand_slowdown"),
        "Lithium is mostly cycle/watch; Green requires low-cost assets, offtake, and FCF defense beyond price rebound.",
    ),
    Round34ScoreTarget(
        "HOME_LIVING_APPLIANCE_RENTAL",
        Round10LargeSector.CONSUMER_RETAIL_BRAND,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round34ScoreWeightDraft(17, 15, 6, 12, 10, 2, 5),
        ("home_appliance", "rental_subscription", "smart_home", "replacement_cycle"),
        ("rental_subscription_revenue", "filter_or_care_service", "overseas_account_growth", "stable_fcf"),
        ("low_churn", "hardware_cycle_risk_low", "inventory_controlled"),
        ("rental_subscription_revenue", "filter_or_care_service", "overseas_account_growth", "stable_fcf"),
        ("replacement_cycle", "housing_market", "consumer_sentiment", "inventory", "competition", "hardware_only"),
        ("replacement_demand_collapse", "dividend_suspension", "inventory_build", "consumer_demand_shock"),
        "Home appliances are Green-possible only when rental/care recurring revenue is visible; hardware replacement cycle remains capped.",
    ),
    Round34ScoreTarget(
        "AI_ACCELERATOR_CHIP_PUREPLAY",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round34ScoreWeightDraft(18, 15, 13, 15, 10, 0, 5),
        ("ai_accelerator", "pureplay_ai_chip", "training_inference_chip", "ipo_revenue_growth"),
        ("actual_revenue", "customer_mass_production", "cost_advantage", "gross_margin_improvement"),
        ("foundry_supply_stable", "customer_validation_visible", "valuation_overheat_controlled"),
        ("actual_revenue", "customer_mass_production", "customer_validation_visible", "gross_margin_improvement"),
        ("customer_validation", "nvidia_competition", "valuation_overheat", "foundry_yield", "rd_burn", "tapeout_only"),
        ("customer_validation_failure", "yield_issue", "rd_burn_acceleration", "valuation_unwind"),
        "AI accelerator pure-play is Watch-to-Green only after customer validation, revenue, yield, and margin evidence.",
    ),
    Round34ScoreTarget(
        "MOBILITY_RENTAL_MICROMOBILITY",
        Round10LargeSector.MOBILITY_TRANSPORT_LEISURE,
        E2RArchetype.RETAIL_DOMESTIC_CONSUMER,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round34ScoreWeightDraft(17, 14, 6, 12, 10, 1, 5),
        ("rental_car", "used_car", "micromobility", "shared_mobility"),
        ("positive_fcf", "stable_city_utilization", "maintenance_cost_control", "repeat_rider_base"),
        ("regulation_stable", "unit_economics_visible", "seasonality_controlled"),
        ("positive_fcf", "stable_city_utilization", "maintenance_cost_control", "unit_economics_visible"),
        ("unit_economics", "regulation", "maintenance_cost", "seasonality", "competition", "revenue_growth_no_profit"),
        ("city_regulation_ban", "unit_economics_break", "maintenance_cost_spike", "liability_insurance_cost"),
        "Mobility rental/micromobility is Watch-first; revenue growth needs FCF and unit-economics proof.",
    ),
)


ROUND34_CASE_CANDIDATES: tuple[Round34CaseCandidate, ...] = (
    Round34CaseCandidate("cbam_compliance_service_candidate", "CARBON_CREDIT_CBAM_COMPLIANCE", "CBAM_SVC", "CBAM compliance service candidate", "EU", "success_candidate", ("carbon_monitoring_recurring_revenue", "verified_customer_contract"), ("policy_change", "greenwashing"), "CBAM compliance services need recurring revenue, not carbon-price headlines."),
    Round34CaseCandidate("carbon_cost_pass_through_success_candidate", "CARBON_CREDIT_CBAM_COMPLIANCE", "CARBON_PASS", "탄소비용 전가 성공 후보", "GLOBAL", "success_candidate", ("pass_through_possible", "premium_low_carbon_product"), ("allowance_price_volatility", "pass_through_failure"), "Cost pass-through or low-carbon premium is stronger than credit price exposure."),
    Round34CaseCandidate("voluntary_carbon_credit_integrity_counterexample", "CARBON_CREDIT_CBAM_COMPLIANCE", "VCM_INTEGRITY", "자발적 탄소크레딧 무결성 반례", "GLOBAL", "failed_rerating", ("carbon_credit",), ("offset_integrity", "greenwashing"), "Voluntary credit volume can be weak if additionality and double counting are unclear."),
    Round34CaseCandidate("carbon_allowance_price_volatility_4c", "CARBON_CREDIT_CBAM_COMPLIANCE", "CARBON_PRICE_4C", "탄소배출권 가격변동 4C", "EU", "4c_thesis_break", ("carbon_credit",), ("allowance_price_collapse", "policy_reversal"), "Allowance price or policy reversal can break carbon-credit thesis."),
    Round34CaseCandidate("mynt_gcash_wallet_financial_services_candidate", "PAYMENT_FINTECH_INFRA", "GCASH", "Mynt GCash 금융서비스 후보", "PH", "success_candidate", ("e_wallet", "financial_service_attach", "transaction_volume_growth"), ("regulation", "credit_loss"), "E-wallet score needs attach services and economics, not user count alone."),
    Round34CaseCandidate("stripe_profitable_payment_infra_candidate", "PAYMENT_FINTECH_INFRA", "STRIPE", "Stripe 흑자 결제인프라 후보", "US", "success_candidate", ("pg_network", "profitable_or_fcf_conversion", "merchant_or_user_lock_in"), ("competition", "take_rate_pressure"), "Payment infra becomes stronger when profitability and lock-in are visible."),
    Round34CaseCandidate("stablecoin_convertibility_regulation_4c", "PAYMENT_FINTECH_INFRA", "STABLE_REG_4C", "스테이블코인 전환규제 4C", "GLOBAL", "4c_thesis_break", ("payment_volume",), ("regulatory_restriction", "security_incident"), "Stablecoin convertibility or regulation risk can break payment infrastructure narratives."),
    Round34CaseCandidate("high_user_count_no_take_rate_counterexample", "PAYMENT_FINTECH_INFRA", "USER_NOTAKE", "사용자수 높지만 take rate 부재", "GLOBAL", "failed_rerating", ("e_wallet",), ("user_count_only", "take_rate_pressure"), "User count alone is not payment profitability evidence."),
    Round34CaseCandidate("meta_corning_fiber_ai_datacenter_contract_candidate", "OPTICAL_NETWORKING_AI_DATACENTER", "GLW_META", "Meta Corning AI 데이터센터 광섬유 계약", "US", "success_candidate", ("hyperscaler_long_contract", "direct_ai_datacenter_supply", "bottleneck_optical_component"), ("hyperscaler_concentration", "valuation_crowding"), "Hyperscaler contract can make optical networking an AI infra Green axis."),
    Round34CaseCandidate("optical_networking_ai_demand_candidate", "OPTICAL_NETWORKING_AI_DATACENTER", "OPTICAL_AI", "AI 데이터센터 광통신 수요 후보", "GLOBAL", "success_candidate", ("optical_transceiver", "op_eps_revision"), ("inventory", "capex_delay"), "AI optical demand needs delivery and revision evidence."),
    Round34CaseCandidate("optical_stock_valuation_crowding_4b", "OPTICAL_NETWORKING_AI_DATACENTER", "OPTICAL_4B", "광통신 주가 밸류 과열 4B", "US", "4b_watch", ("ai_datacenter_network",), ("valuation_crowding", "valuation_unwind"), "AI optical demand can still need 4B-watch when price outruns revisions."),
    Round34CaseCandidate("optical_customer_concentration_counterexample", "OPTICAL_NETWORKING_AI_DATACENTER", "OPTICAL_CUST", "광통신 고객집중 반례", "GLOBAL", "failed_rerating", ("fiber_optic_cable",), ("hyperscaler_concentration", "hyperscaler_order_cut"), "Customer concentration can cap optical networking visibility."),
    Round34CaseCandidate("nokia_5g_capex_slowdown_4c", "TELECOM_5G_6G_CAPEX_CYCLE", "NOKIA_5G_4C", "Nokia 5G CAPEX 둔화 4C", "EU", "4c_thesis_break", ("telecom_equipment",), ("capex_peak_out", "operator_delay"), "Telecom capex slowdown is 4C-style evidence for equipment vendors."),
    Round34CaseCandidate("china_restricts_nokia_ericsson_geopolitical_4c", "TELECOM_5G_6G_CAPEX_CYCLE", "TELCO_GEO_4C", "중국 Nokia Ericsson 제한 4C", "EU", "4c_thesis_break", ("5g_6g_policy",), ("security_ban", "geopolitical_restriction"), "Geopolitical or security restriction can break telecom equipment demand."),
    Round34CaseCandidate("open_ran_policy_no_revenue_watch", "TELECOM_5G_6G_CAPEX_CYCLE", "OPEN_RAN_WATCH", "Open RAN 정책 무매출 Watch", "GLOBAL", "event_premium", ("open_ran",), ("policy_no_revenue", "operator_delay"), "Open RAN policy is not evidence until orders or revenue exist."),
    Round34CaseCandidate("6g_policy_no_revenue_counterexample", "TELECOM_5G_6G_CAPEX_CYCLE", "6G_NOREV", "6G 정책 무매출 반례", "GLOBAL", "failed_rerating", ("5g_6g_policy",), ("policy_no_revenue", "operator_delay"), "6G policy theme without operator capex remains RedTeam-first."),
    Round34CaseCandidate("lithium_price_stabilization_candidate", "LITHIUM_BATTERY_RAW_MATERIAL", "LITH_STABLE", "리튬 가격 안정 후보", "GLOBAL", "cyclical_success", ("lithium_price", "demand_visible"), ("mine_restart", "oversupply"), "Lithium stabilization can support watch, but price alone is not structural."),
    Round34CaseCandidate("albemarle_cost_cut_low_lithium_price_case", "LITHIUM_BATTERY_RAW_MATERIAL", "ALB", "Albemarle 저가 리튬 비용절감 사례", "US", "cyclical_success", ("low_cost_asset", "fcf_defense_at_low_price"), ("lithium_price", "capex"), "Cost-cut and low-cost assets can defend FCF, but lithium remains cyclical."),
    Round34CaseCandidate("lithium_price_crash_oversupply_4c", "LITHIUM_BATTERY_RAW_MATERIAL", "LITH_CRASH_4C", "리튬가격 급락 공급과잉 4C", "GLOBAL", "4c_thesis_break", ("battery_raw_material",), ("price_crash", "oversupply"), "Lithium price crash or oversupply can break raw-material thesis."),
    Round34CaseCandidate("mine_restart_supply_rebound_counterexample", "LITHIUM_BATTERY_RAW_MATERIAL", "MINE_RESTART", "폐쇄광산 재가동 공급반등 반례", "GLOBAL", "failed_rerating", ("mine_restart",), ("mine_restart_supply", "price_rebound_only"), "Mine restart risk caps lithium price rebound stories."),
    Round34CaseCandidate("coway_rental_subscription_candidate", "HOME_LIVING_APPLIANCE_RENTAL", "021240", "Coway 렌탈 구독 후보", "KR", "success_candidate", ("rental_subscription_revenue", "filter_or_care_service", "stable_fcf"), ("competition", "consumer_sentiment"), "Rental/care revenue is stronger than one-time appliance sales."),
    Round34CaseCandidate("whirlpool_replacement_cycle_4c", "HOME_LIVING_APPLIANCE_RENTAL", "WHR_4C", "Whirlpool 교체수요 둔화 4C", "US", "4c_thesis_break", ("home_appliance",), ("replacement_demand_collapse", "consumer_demand_shock"), "Hardware replacement demand can collapse with housing and consumer sentiment."),
    Round34CaseCandidate("appliance_dividend_suspension_counterexample", "HOME_LIVING_APPLIANCE_RENTAL", "APPL_DIVSTOP", "생활가전 배당중단 반례", "GLOBAL", "failed_rerating", ("replacement_cycle",), ("dividend_suspension", "hardware_only"), "Dividend suspension shows hardware-cycle weakness and FCF stress."),
    Round34CaseCandidate("smart_home_no_subscription_counterexample", "HOME_LIVING_APPLIANCE_RENTAL", "SMART_HOME_NOSUB", "스마트홈 구독 부재 반례", "GLOBAL", "failed_rerating", ("smart_home",), ("hardware_only", "competition"), "Smart-home device sales without subscription stay capped."),
    Round34CaseCandidate("cerebras_ipo_revenue_growth_candidate", "AI_ACCELERATOR_CHIP_PUREPLAY", "CBRS", "Cerebras IPO 매출성장 후보", "US", "success_candidate", ("actual_revenue", "ipo_revenue_growth"), ("valuation_overheat", "nvidia_competition"), "AI accelerator pure-play needs revenue, customer validation, and margin evidence."),
    Round34CaseCandidate("ai_chip_valuation_overheat_4b", "AI_ACCELERATOR_CHIP_PUREPLAY", "AIACC_4B", "AI칩 pure-play 밸류 과열 4B", "US", "4b_watch", ("pureplay_ai_chip",), ("valuation_overheat", "valuation_unwind"), "High AI-chip valuation can become 4B-watch before fundamental break."),
    Round34CaseCandidate("ai_chip_no_customer_validation_counterexample", "AI_ACCELERATOR_CHIP_PUREPLAY", "AIACC_NOVAL", "AI칩 고객검증 부재 반례", "GLOBAL", "failed_rerating", ("ai_accelerator",), ("customer_validation", "tapeout_only"), "Tape-out or related-stock label is not customer validation."),
    Round34CaseCandidate("foundry_yield_risk_4c", "AI_ACCELERATOR_CHIP_PUREPLAY", "YIELD_4C", "파운드리 수율 리스크 4C", "GLOBAL", "4c_thesis_break", ("training_inference_chip",), ("yield_issue", "customer_validation_failure"), "Yield or validation failure can break AI accelerator thesis."),
    Round34CaseCandidate("lime_positive_fcf_candidate", "MOBILITY_RENTAL_MICROMOBILITY", "LIME", "Lime positive FCF 후보", "US", "success_candidate", ("positive_fcf", "stable_city_utilization", "repeat_rider_base"), ("seasonality", "regulation"), "Micromobility needs positive FCF and city-level utilization."),
    Round34CaseCandidate("micromobility_revenue_growth_no_profit_counterexample", "MOBILITY_RENTAL_MICROMOBILITY", "MICRO_NP", "공유모빌리티 매출성장 무이익 반례", "GLOBAL", "failed_rerating", ("micromobility",), ("revenue_growth_no_profit", "unit_economics"), "Revenue growth without unit economics should not become Green."),
    Round34CaseCandidate("city_regulation_4c", "MOBILITY_RENTAL_MICROMOBILITY", "CITY_REG_4C", "도시규제 4C", "GLOBAL", "4c_thesis_break", ("shared_mobility",), ("city_regulation_ban", "liability_insurance_cost"), "City regulation or ban can break micromobility operations."),
    Round34CaseCandidate("maintenance_cost_unit_economics_counterexample", "MOBILITY_RENTAL_MICROMOBILITY", "MAINT_COST", "유지보수 unit economics 반례", "GLOBAL", "failed_rerating", ("rental_car", "micromobility"), ("maintenance_cost_spike", "unit_economics_break"), "Maintenance and repositioning costs can erase mobility platform margins."),
)


def target_for(target_id: str) -> Round34ScoreTarget | None:
    for target in ROUND34_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round34_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND34_CASE_CANDIDATES:
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
                f"Round34 v1.9 calibration candidate for {candidate.target_id}; "
                "stage dates, prices, and numeric evidence remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.green_conditions),
            stage3_evidence=(),
            stage4b_evidence=candidate.red_flag_fields if candidate.case_type == "4b_watch" else (),
            stage4c_evidence=candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" else (),
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type not in {"success_candidate", "structural_success", "cyclical_success"} else None,
            score_price_alignment="unknown",
            rerating_result="cyclical_rerating" if candidate.case_type == "cyclical_success" else "unknown",
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


def round34_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND34_SCORE_TARGETS:
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


def round34_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND34_CASE_CANDIDATES:
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


def round34_summary() -> dict[str, int | bool]:
    records = round34_case_records()
    positive = sum(1 for record in records if record.case_type in {"success_candidate", "structural_success", "cyclical_success"})
    stage4c = sum(1 for record in records if record.case_type == "4c_thesis_break")
    stage4b = sum(1 for record in records if record.case_type == "4b_watch")
    return {
        "target_count": len(ROUND34_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": len(records) - positive,
        "stage4b_case_count": stage4b,
        "stage4c_case_count": stage4c,
        "green_possible_count": sum(1 for target in ROUND34_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND34_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND34_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round34_score_weight_reports(
    *,
    output_directory: str | Path = ROUND34_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND34_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND34_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round34_score_weight_v19_summary.md",
        "case_matrix": output / "round34_case_candidate_matrix.csv",
        "green_guardrails": output / "round34_green_guardrail_review.md",
        "carbon_payment": output / "round34_carbon_payment_review.md",
        "optical_telecom_split": output / "round34_optical_telecom_split_review.md",
        "cycle_unit_economics": output / "round34_cycle_unit_economics_review.md",
        "price_validation_plan": output / "round34_price_validation_plan.md",
    }
    _write_case_jsonl(round34_case_records(), cases)
    _write_rows(round34_score_profile_rows(), score_profiles)
    _write_rows(round34_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round34_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round34_green_guardrail_markdown(), encoding="utf-8")
    paths["carbon_payment"].write_text(render_round34_carbon_payment_markdown(), encoding="utf-8")
    paths["optical_telecom_split"].write_text(render_round34_optical_telecom_split_markdown(), encoding="utf-8")
    paths["cycle_unit_economics"].write_text(render_round34_cycle_unit_economics_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round34_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round34_summary_markdown() -> str:
    summary = round34_summary()
    lines = [
        "# Round-34 Score-Weight v1.9 Summary",
        "",
        f"- source_round: `{ROUND34_SOURCE_ROUND_PATH}`",
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
        "- Round 34 adds v1.9 calibration cases and target weights only.",
        "- Example: optical networking can be an AI data-center Green axis when hyperscaler contracts and delivery economics are visible.",
        "- Example: 5G/6G telecom equipment should remain RedTeam-first because operator CAPEX, geopolitics, and security reviews can dominate.",
        "- Example: payment fintech needs transaction volume, take rate, lock-in, and FCF; user count alone is not score evidence.",
        "- Theme names, case IDs, policy labels, CAPEX headlines, and price rallies are not score evidence by themselves.",
    ]
    return "\n".join(lines) + "\n"


def render_round34_green_guardrail_markdown() -> str:
    lines = [
        "# Round-34 Green Guardrail Review",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "|---|---|---|---|",
    ]
    for target in ROUND34_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply v1.9 weights to production scoring yet.",
            "- Do not use case IDs or theme labels as candidate-generation input.",
            "- Do not invent stage dates, prices, CBAM pass-through, fintech take rate, hyperscaler terms, telecom orders, lithium costs, rental churn, AI-chip yield, or mobility unit economics.",
            "- Do not lower Stage 3-Green thresholds to improve recall.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round34_carbon_payment_markdown() -> str:
    return "\n".join(
        [
            "# Round-34 Carbon / Payment Review",
            "",
            "Carbon and payment both look policy-driven, but their score evidence differs.",
            "",
            "## Carbon / CBAM",
            "- Watch-first unless pass-through, recurring compliance revenue, low-carbon premium, or FCF savings are visible.",
            "- Carbon-credit price or offset issuance alone is not Green evidence.",
            "",
            "## Payment Fintech",
            "- Green-possible with transaction volume, take-rate stability, merchant/user lock-in, attach revenue, and FCF.",
            "- User count, token label, or stablecoin headline alone is not enough.",
        ]
    ) + "\n"


def render_round34_optical_telecom_split_markdown() -> str:
    return "\n".join(
        [
            "# Round-34 Optical Networking / Telecom Split Review",
            "",
            "Optical AI data-center networking and 5G/6G telecom equipment must not share the same Green profile.",
            "",
            "## Optical AI Data Center",
            "- Hyperscaler long contract.",
            "- Direct AI data-center supply.",
            "- Optical cable/transceiver bottleneck.",
            "- OP/EPS revision and delivery economics.",
            "",
            "## Telecom 5G/6G",
            "- Operator CAPEX and policy may create Watch signals.",
            "- CAPEX peak-out, operator delay, geopolitics, and security bans are RedTeam gates.",
        ]
    ) + "\n"


def render_round34_cycle_unit_economics_markdown() -> str:
    return "\n".join(
        [
            "# Round-34 Cycle / Unit Economics Review",
            "",
            "Round 34 keeps price-cycle and usage-growth stories from masquerading as structural E2R.",
            "",
            "## Cycle-Capped Areas",
            "- Lithium raw materials: price rebound needs low-cost assets, offtake, and FCF defense.",
            "- Home appliances: hardware replacement demand is capped unless rental/care subscription is visible.",
            "- Mobility: revenue growth needs positive FCF and unit economics.",
            "- AI accelerator: revenue and customer validation are required before Green-like interpretation.",
        ]
    ) + "\n"


def render_round34_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-34 Price Validation Plan",
            "",
            "1. Backfill tradable case price paths where symbols exist.",
            "2. Keep synthetic, global reference, event, and theme cases as `needs_price_backfill` or `missing_price_data`.",
            "3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.",
            "4. Run shadow score-price alignment before any production scoring change.",
            "",
            "## Priority Validation",
            "- Carbon/payment: recurring compliance or fintech FCF versus policy, greenwashing, take-rate, security, and credit risk.",
            "- Optical/telecom: hyperscaler delivery economics versus telecom CAPEX cycle and geopolitics.",
            "- Lithium/appliance/mobility: FCF defense and unit economics versus price cycle, hardware cycle, and regulatory cost.",
            "- AI accelerator: revenue, customer validation, yield, and margin versus valuation overheat.",
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
    "ROUND34_CASE_CANDIDATES",
    "ROUND34_DEFAULT_CASES_PATH",
    "ROUND34_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND34_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND34_SCORE_TARGETS",
    "ROUND34_SOURCE_ROUND_PATH",
    "Round34CaseCandidate",
    "Round34ScoreTarget",
    "Round34ScoreWeightDraft",
    "render_round34_carbon_payment_markdown",
    "render_round34_cycle_unit_economics_markdown",
    "render_round34_green_guardrail_markdown",
    "render_round34_optical_telecom_split_markdown",
    "render_round34_price_validation_plan_markdown",
    "render_round34_summary_markdown",
    "round34_case_candidate_rows",
    "round34_case_records",
    "round34_score_profile_rows",
    "round34_summary",
    "target_for",
    "write_round34_score_weight_reports",
]
