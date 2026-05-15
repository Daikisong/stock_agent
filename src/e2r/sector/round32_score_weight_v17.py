"""Round-32 cases_v14 expansion and score-weight v1.7 hypotheses.

Round 32 fills thinner archetype families: general trading/resource
infrastructure, LNG/energy distribution, OLED supply chain, electronic
components, digital healthcare, commodity memory, LNG/gas utilities, and AI
chip/foundry fabric. It is report-only calibration material. Production
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


ROUND32_SOURCE_ROUND_PATH = "docs/round/round_32.md"
ROUND32_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round32_score_weight_v17"
ROUND32_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_v14_round32.jsonl"
ROUND32_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round32_v17.csv"


@dataclass(frozen=True)
class Round32ScoreWeightDraft:
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
class Round32ScoreTarget:
    target_id: str
    large_sector: Round10LargeSector
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round32ScoreWeightDraft
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
class Round32CaseCandidate:
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


ROUND32_SCORE_TARGETS: tuple[Round32ScoreTarget, ...] = (
    Round32ScoreTarget(
        "GENERAL_TRADING_RESOURCE_INFRA",
        Round10LargeSector.MATERIALS_SPREAD_STRATEGIC,
        E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round32ScoreWeightDraft(17, 19, 12, 15, 18, 8, 5),
        ("resource_trading", "energy_project_rights", "offtake_keyword", "capital_return"),
        ("long_term_offtake", "project_equity", "diversified_fcf", "shareholder_return"),
        ("roe_fcf_improvement", "capital_allocation_execution", "conglomerate_discount_narrowing"),
        ("long_term_offtake", "project_equity", "diversified_fcf", "shareholder_return", "roe_fcf_improvement"),
        ("commodity_price", "fx", "project_execution", "conglomerate_discount", "low_margin_trading"),
        ("project_delay", "commodity_price_reversal", "no_capital_return", "conglomerate_discount_persistent"),
        "Trading houses are Green-possible only when project rights, long-term contracts, FCF, and capital allocation are source-backed.",
    ),
    Round32ScoreTarget(
        "LNG_ENERGY_TRADING_DISTRIBUTION",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.COMMODITY_SPREAD,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round32ScoreWeightDraft(18, 15, 16, 10, 10, 2, 5),
        ("lng_lpg_distribution", "refining_margin", "energy_trading", "inventory_gain"),
        ("long_term_supply_contract", "procurement_stability", "pass_through_visible", "operating_margin_not_inventory_only"),
        ("fcf_improvement", "geopolitical_risk_controlled", "tariff_risk_controlled"),
        ("long_term_supply_contract", "procurement_stability", "pass_through_visible", "fcf_improvement"),
        ("energy_price", "inventory_loss", "tariff", "geopolitics", "pass_through_failure"),
        ("inventory_loss", "tariff_reversal", "geopolitical_disruption", "refining_spread_normalization"),
        "LNG distribution needs long-term supply and pass-through evidence; refining or oil-price rebounds stay cycle-capped.",
    ),
    Round32ScoreTarget(
        "DISPLAY_OLED_SUPPLYCHAIN",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.SEMI_EQUIPMENT_CAPEX,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round32ScoreWeightDraft(19, 18, 12, 13, 11, 0, 5),
        ("oled_transition", "panel_customer_adoption", "display_capex", "lcd_exit"),
        ("customer_oled_adoption", "oled_order_or_supply", "lcd_restructuring", "opm_improvement"),
        ("customer_diversification", "capex_cycle_risk_low", "panel_price_risk_low"),
        ("customer_oled_adoption", "oled_order_or_supply", "lcd_restructuring", "opm_improvement"),
        ("panel_price_competition", "capex_cycle", "customer_concentration", "china_price_competition"),
        ("panel_price_drop", "capex_delay", "customer_order_cut", "china_price_competition"),
        "OLED has structural penetration, but Green requires durable orders and margin support beyond one display CAPEX wave.",
    ),
    Round32ScoreTarget(
        "ELECTRONIC_COMPONENTS_MLCC_SENSOR",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AUTO_MOBILITY_COMPONENTS,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round32ScoreWeightDraft(19, 17, 13, 12, 11, 1, 5),
        ("mlcc_sensor_component", "smartphone_component", "auto_component", "ai_server_component"),
        ("customer_diversification", "high_value_component_demand", "capex_to_revenue_conversion", "opm_improvement"),
        ("technology_lead", "inventory_cycle_controlled", "component_price_pressure_low"),
        ("customer_diversification", "high_value_component_demand", "capex_to_revenue_conversion", "opm_improvement"),
        ("inventory_cycle", "customer_concentration", "china_supply_chain", "component_price_pressure", "rare_earth_dependency"),
        ("inventory_glut", "customer_order_cut", "supply_chain_disruption", "component_price_drop"),
        "MLCC/sensors/components can become Green only when customer mix, revenue conversion, and inventory discipline are visible.",
    ),
    Round32ScoreTarget(
        "DIGITAL_HEALTHCARE_REMOTE_MEDICINE",
        Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE,
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round32ScoreWeightDraft(18, 18, 8, 13, 12, 1, 6),
        ("remote_medicine", "digital_health_platform", "hospital_workflow", "wearable_health"),
        ("hospital_or_insurer_contract", "recurring_subscription", "reimbursement_visible", "real_patient_usage"),
        ("unit_economics_visible", "data_security_controlled", "clinical_liability_controlled"),
        ("hospital_or_insurer_contract", "recurring_subscription", "reimbursement_visible", "unit_economics_visible"),
        ("regulation", "reimbursement", "data_security", "unit_economics", "clinical_liability"),
        ("reimbursement_failure", "regulatory_reversal", "data_security_incident", "unit_economics_break"),
        "Digital healthcare needs contracts, reimbursement, recurring revenue, and unit economics before Green-like interpretation.",
    ),
    Round32ScoreTarget(
        "COMMODITY_MEMORY_GENERAL_SEMI",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.MEMORY_HBM_CAPACITY,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round32ScoreWeightDraft(22, 16, 17, 13, 10, 0, 5),
        ("dram_nand_price_recovery", "commodity_memory", "ai_server_memory_demand", "earnings_turnaround"),
        ("memory_price_increase", "inventory_decline", "op_eps_revision", "ai_server_demand"),
        ("supply_discipline", "hbm_gap_not_ignored", "long_term_visibility_above_spot"),
        ("memory_price_increase", "inventory_decline", "op_eps_revision", "supply_discipline"),
        ("cycle", "hbm_lag", "supply_rebound", "ai_capex_slowdown", "spot_rebound_only"),
        ("memory_price_decline", "supply_rebound", "ai_capex_slowdown", "hbm_customer_validation_failure"),
        "Commodity DRAM/NAND can drive EPS recovery, but structural visibility is lower than HBM without long-term allocation evidence.",
    ),
    Round32ScoreTarget(
        "ENERGY_UTILITY_LNG_GAS",
        Round10LargeSector.BATTERY_EV_GREEN,
        E2RArchetype.UTILITIES_REGULATED_TARIFF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round32ScoreWeightDraft(17, 18, 6, 12, 10, 5, 5),
        ("lng_utility", "gas_distribution", "tariff_normalization", "receivables_recovery"),
        ("tariff_normalization", "receivables_recovery", "lng_procurement_stability", "fcf_improvement"),
        ("debt_stabilization", "dividend_capacity", "regulatory_regime_supportive"),
        ("tariff_normalization", "receivables_recovery", "lng_procurement_stability", "fcf_improvement"),
        ("tariff_regulation", "debt", "lng_price", "receivables", "policy_risk"),
        ("tariff_freeze", "receivables_growth", "debt_burden", "cost_pass_through_failure"),
        "Gas/LNG utilities are Watch-first because tariff, receivables, debt, and policy can dominate EPS recovery.",
    ),
    Round32ScoreTarget(
        "AI_CHIP_FABRIC_INFRA",
        Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS,
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round32ScoreWeightDraft(18, 15, 12, 14, 11, 0, 5),
        ("ai_chip", "system_semiconductor", "neuromorphic", "foundry_deal"),
        ("customer_contract", "mass_production_revenue", "foundry_packaging_memory_link", "op_eps_conversion"),
        ("customer_validation", "yield_cost_controlled", "direct_revenue_exposure"),
        ("customer_contract", "mass_production_revenue", "customer_validation", "op_eps_conversion"),
        ("no_revenue", "customer_validation", "yield", "theme_overheat", "unclear_equity_exposure"),
        ("customer_validation_failure", "yield_issue", "no_revenue_model", "theme_unwind"),
        "AI-chip related stocks stay RedTeam-first unless direct exposure, customer validation, mass production revenue, and EPS conversion are proven.",
    ),
)


ROUND32_CASE_CANDIDATES: tuple[Round32CaseCandidate, ...] = (
    Round32CaseCandidate("berkshire_japan_sogo_shosha_long_term_rerating_candidate", "GENERAL_TRADING_RESOURCE_INFRA", "JP_SOGO", "일본 종합상사 장기 리레이팅 후보", "JP", "success_candidate", ("resource_project_rights", "diversified_fcf", "shareholder_return"), ("commodity_price", "conglomerate_discount"), "Sogo shosha reference case needs project rights, FCF, and capital-allocation validation."),
    Round32CaseCandidate("posco_international_alaska_lng_20y_contract_candidate", "GENERAL_TRADING_RESOURCE_INFRA", "047050", "POSCO International Alaska LNG 20년 계약", "KR", "success_candidate", ("long_term_offtake", "project_equity", "steel_supply_linkage"), ("project_execution", "fx"), "Long-term LNG plus project participation is stronger than plain trading revenue."),
    Round32CaseCandidate("trading_house_commodity_cycle_counterexample", "GENERAL_TRADING_RESOURCE_INFRA", "TRADING_CYCLE", "종합상사 상품가격 사이클 반례", "GLOBAL", "failed_rerating", ("resource_trading",), ("commodity_price", "low_margin_trading"), "Commodity-price revenue without FCF/capital allocation should stay capped."),
    Round32CaseCandidate("conglomerate_discount_no_capital_return_counterexample", "GENERAL_TRADING_RESOURCE_INFRA", "CONGLO_NORETURN", "복합기업 할인 자본배분 부재 반례", "GLOBAL", "failed_rerating", ("conglomerate_discount",), ("no_capital_return", "conglomerate_discount_persistent"), "Discount can remain justified without cancellation, dividends, or FCF improvement."),
    Round32CaseCandidate("posco_international_lng_long_term_offtake_candidate", "LNG_ENERGY_TRADING_DISTRIBUTION", "047050_LNG", "POSCO International LNG 장기 offtake", "KR", "success_candidate", ("long_term_supply_contract", "procurement_stability"), ("geopolitics", "pass_through_failure"), "LNG long-term supply can support Watch-to-Green if pass-through and FCF are visible."),
    Round32CaseCandidate("sk_innovation_refining_recovery_watch", "LNG_ENERGY_TRADING_DISTRIBUTION", "096770", "SK Innovation 정제마진 회복 Watch", "KR", "cyclical_success", ("refining_margin", "operating_margin_not_inventory_only"), ("inventory_loss", "refining_spread_normalization"), "Refining recovery is useful but remains cycle-capped until structural margin evidence appears."),
    Round32CaseCandidate("lng_tariff_geopolitics_4c", "LNG_ENERGY_TRADING_DISTRIBUTION", "LNG_GEO_4C", "LNG 관세 지정학 4C", "GLOBAL", "4c_thesis_break", ("lng_lpg_distribution",), ("tariff_reversal", "geopolitical_disruption"), "Tariff or geopolitics can break LNG distribution visibility."),
    Round32CaseCandidate("energy_price_inventory_loss_counterexample", "LNG_ENERGY_TRADING_DISTRIBUTION", "ENERGY_INV_LOSS", "에너지가격 재고손실 반례", "GLOBAL", "failed_rerating", ("energy_trading",), ("inventory_loss", "energy_price"), "Inventory gains/losses must not be annualized as structural FCF."),
    Round32CaseCandidate("apple_all_iphone_oled_transition_candidate", "DISPLAY_OLED_SUPPLYCHAIN", "OLED_IPHONE", "Apple 전모델 OLED 전환 후보", "GLOBAL", "success_candidate", ("customer_oled_adoption", "oled_transition"), ("panel_price_competition", "customer_concentration"), "OLED penetration is Stage 1/2 evidence; orders and margins still need validation."),
    Round32CaseCandidate("lg_display_lcd_exit_oled_focus_candidate", "DISPLAY_OLED_SUPPLYCHAIN", "034220", "LG Display LCD 매각 OLED 집중", "KR", "success_candidate", ("lcd_restructuring", "oled_order_or_supply"), ("capex_cycle", "panel_price_competition"), "LCD exit can improve mix if OLED margin and demand are source-backed."),
    Round32CaseCandidate("oled_capex_cycle_counterexample", "DISPLAY_OLED_SUPPLYCHAIN", "OLED_CAPEX_CYCLE", "OLED CAPEX 사이클 반례", "KR", "failed_rerating", ("display_capex",), ("capex_cycle", "customer_order_cut"), "One display equipment cycle is not enough for Green."),
    Round32CaseCandidate("oled_panel_price_competition_4c", "DISPLAY_OLED_SUPPLYCHAIN", "OLED_PRICE_4C", "OLED 패널 가격경쟁 4C", "GLOBAL", "4c_thesis_break", ("oled_transition",), ("panel_price_drop", "china_price_competition"), "OLED penetration can still fail if panel prices and margins collapse."),
    Round32CaseCandidate("murata_capex_mna_component_growth_candidate", "ELECTRONIC_COMPONENTS_MLCC_SENSOR", "6981.T", "Murata CAPEX M&A 전자부품 성장", "JP", "success_candidate", ("mlcc_sensor_component", "customer_diversification", "capex_to_revenue_conversion"), ("rare_earth_dependency", "inventory_cycle"), "Component growth needs customer mix and revenue conversion, not CAPEX headline alone."),
    Round32CaseCandidate("tdk_silicon_anode_component_candidate", "ELECTRONIC_COMPONENTS_MLCC_SENSOR", "6762.T", "TDK 실리콘 음극재 전자부품 후보", "JP", "success_candidate", ("high_value_component_demand", "technology_lead"), ("component_price_pressure", "customer_concentration"), "High-value component demand can support Watch-to-Green when margins and customers are visible."),
    Round32CaseCandidate("mlcc_inventory_cycle_counterexample", "ELECTRONIC_COMPONENTS_MLCC_SENSOR", "MLCC_INV", "MLCC 재고 사이클 반례", "GLOBAL", "failed_rerating", ("mlcc_sensor_component",), ("inventory_glut", "component_price_drop"), "MLCC cycle rebound should be capped when inventory is rising."),
    Round32CaseCandidate("rare_earth_supply_chain_risk_4c", "ELECTRONIC_COMPONENTS_MLCC_SENSOR", "RARE_EARTH_4C", "희토류 공급망 리스크 4C", "GLOBAL", "4c_thesis_break", ("auto_component",), ("supply_chain_disruption", "rare_earth_dependency"), "Rare-earth or China supply-chain disruption can break component visibility."),
    Round32CaseCandidate("samsung_xealth_digital_health_platform_candidate", "DIGITAL_HEALTHCARE_REMOTE_MEDICINE", "005930_XEALTH", "Samsung Xealth 디지털헬스 플랫폼", "KR", "success_candidate", ("digital_health_platform", "hospital_workflow"), ("regulation", "data_security"), "Platform integration is positive only if contracts, usage, and economics are visible."),
    Round32CaseCandidate("teladoc_subscription_virtual_care_reference", "DIGITAL_HEALTHCARE_REMOTE_MEDICINE", "TDOC", "Teladoc 구독형 원격진료 참고", "US", "success_candidate", ("recurring_subscription", "real_patient_usage"), ("unit_economics", "reimbursement"), "Subscription reference case needs unit-economics and payer validation."),
    Round32CaseCandidate("telemedicine_no_reimbursement_counterexample", "DIGITAL_HEALTHCARE_REMOTE_MEDICINE", "REMOTE_NOREIMB", "원격의료 수가 부재 반례", "GLOBAL", "failed_rerating", ("remote_medicine",), ("reimbursement_failure", "regulatory_reversal"), "Remote-care usage without reimbursement cannot support Green."),
    Round32CaseCandidate("remote_care_unit_economics_4c", "DIGITAL_HEALTHCARE_REMOTE_MEDICINE", "REMOTE_UNIT_4C", "원격진료 unit economics 4C", "GLOBAL", "4c_thesis_break", ("real_patient_usage",), ("unit_economics_break", "clinical_liability"), "High usage can still fail if contribution margin or liability breaks."),
    Round32CaseCandidate("samsung_commodity_memory_price_recovery_candidate", "COMMODITY_MEMORY_GENERAL_SEMI", "005930_MEM", "Samsung 범용메모리 가격회복 후보", "KR", "cyclical_success", ("memory_price_increase", "op_eps_revision", "ai_server_demand"), ("hbm_lag", "supply_rebound"), "Commodity memory EPS recovery is meaningful but lower-visibility than HBM allocation."),
    Round32CaseCandidate("samsung_hbm_lag_counterexample", "COMMODITY_MEMORY_GENERAL_SEMI", "005930_HBM_LAG", "Samsung HBM lag 반례", "KR", "failed_rerating", ("commodity_memory",), ("hbm_lag", "hbm_customer_validation_failure"), "HBM lag can cap rerating despite DRAM/NAND recovery."),
    Round32CaseCandidate("simple_dram_spot_rebound_counterexample", "COMMODITY_MEMORY_GENERAL_SEMI", "DRAM_SPOT", "단순 DRAM spot 반등 반례", "GLOBAL", "failed_rerating", ("dram_nand_price_recovery",), ("spot_rebound_only", "cycle"), "Spot rebound alone is not structural visibility."),
    Round32CaseCandidate("ai_capex_slowdown_memory_4c", "COMMODITY_MEMORY_GENERAL_SEMI", "AI_CAPEX_MEM_4C", "AI CAPEX 둔화 메모리 4C", "GLOBAL", "4c_thesis_break", ("ai_server_memory_demand",), ("ai_capex_slowdown", "memory_price_decline"), "AI capex slowdown can break memory price and revision path."),
    Round32CaseCandidate("kogas_tariff_normalization_candidate", "ENERGY_UTILITY_LNG_GAS", "036460", "KOGAS 요금정상화 후보", "KR", "success_candidate", ("tariff_normalization", "receivables_recovery"), ("debt", "policy_risk"), "Gas utility recovery needs tariff, receivables, debt, and FCF evidence."),
    Round32CaseCandidate("lng_long_term_supply_candidate", "ENERGY_UTILITY_LNG_GAS", "LNG_SUPPLY", "LNG 장기공급 유틸리티 후보", "GLOBAL", "success_candidate", ("lng_procurement_stability", "fcf_improvement"), ("lng_price", "tariff_regulation"), "Long-term LNG supply is useful only when cost pass-through is visible."),
    Round32CaseCandidate("tariff_freeze_debt_4c", "ENERGY_UTILITY_LNG_GAS", "TARIFF_DEBT_4C", "요금동결 부채 4C", "KR", "4c_thesis_break", ("lng_utility",), ("tariff_freeze", "debt_burden"), "Tariff freeze and debt burden can block utility rerating."),
    Round32CaseCandidate("lng_price_spike_receivables_counterexample", "ENERGY_UTILITY_LNG_GAS", "LNG_RECV", "LNG 가격급등 미수금 반례", "KR", "failed_rerating", ("gas_distribution",), ("receivables_growth", "cost_pass_through_failure"), "Rising receivables are not FCF improvement."),
    Round32CaseCandidate("samsung_tesla_foundry_deal_candidate", "AI_CHIP_FABRIC_INFRA", "005930_TESLA", "Samsung Tesla foundry deal 후보", "KR", "success_candidate", ("customer_contract", "foundry_deal", "direct_revenue_exposure"), ("yield", "customer_validation"), "Foundry deal is positive only if validation, yield, and revenue conversion are visible."),
    Round32CaseCandidate("openai_samsung_sk_memory_partnership_candidate", "AI_CHIP_FABRIC_INFRA", "AI_MEMORY_PARTNER", "OpenAI Samsung SK memory partnership 후보", "KR", "success_candidate", ("foundry_packaging_memory_link", "customer_contract"), ("theme_overheat", "unclear_equity_exposure"), "AI ecosystem partnership needs direct revenue exposure before score credit."),
    Round32CaseCandidate("ai_chip_related_stock_no_revenue_counterexample", "AI_CHIP_FABRIC_INFRA", "AI_CHIP_NOREV", "AI칩 관련주 무매출 반례", "KR", "failed_rerating", ("ai_chip",), ("no_revenue", "unclear_equity_exposure"), "Related-stock label is not score evidence without contract or revenue."),
    Round32CaseCandidate("foundry_yield_customer_validation_4c", "AI_CHIP_FABRIC_INFRA", "FOUNDRY_YIELD_4C", "파운드리 수율 고객검증 4C", "GLOBAL", "4c_thesis_break", ("system_semiconductor",), ("customer_validation_failure", "yield_issue"), "Yield or validation failure can break AI-chip/foundry thesis."),
)


def target_for(target_id: str) -> Round32ScoreTarget | None:
    for target in ROUND32_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round32_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND32_CASE_CANDIDATES:
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
                f"Round32 v1.7 calibration candidate for {candidate.target_id}; "
                "stage dates, prices, and numeric evidence remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.green_conditions),
            stage3_evidence=(),
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


def round32_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND32_SCORE_TARGETS:
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


def round32_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND32_CASE_CANDIDATES:
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


def round32_summary() -> dict[str, int | bool]:
    records = round32_case_records()
    positive = sum(1 for record in records if record.case_type in {"success_candidate", "structural_success", "cyclical_success"})
    stage4c = sum(1 for record in records if record.case_type == "4c_thesis_break")
    stage4b = sum(1 for record in records if record.case_type == "4b_watch")
    return {
        "target_count": len(ROUND32_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": positive,
        "counterexample_or_risk_count": len(records) - positive,
        "stage4b_case_count": stage4b,
        "stage4c_case_count": stage4c,
        "green_possible_count": sum(1 for target in ROUND32_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND32_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND32_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round32_score_weight_reports(
    *,
    output_directory: str | Path = ROUND32_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND32_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND32_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round32_score_weight_v17_summary.md",
        "case_matrix": output / "round32_case_candidate_matrix.csv",
        "green_guardrails": output / "round32_green_guardrail_review.md",
        "energy_cycle": output / "round32_energy_cycle_review.md",
        "memory_split": output / "round32_memory_hbm_split_review.md",
        "ai_chip_revenue_gate": output / "round32_ai_chip_revenue_gate_review.md",
        "price_validation_plan": output / "round32_price_validation_plan.md",
    }
    _write_case_jsonl(round32_case_records(), cases)
    _write_rows(round32_score_profile_rows(), score_profiles)
    _write_rows(round32_case_candidate_rows(), paths["case_matrix"])
    paths["summary"].write_text(render_round32_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round32_green_guardrail_markdown(), encoding="utf-8")
    paths["energy_cycle"].write_text(render_round32_energy_cycle_markdown(), encoding="utf-8")
    paths["memory_split"].write_text(render_round32_memory_split_markdown(), encoding="utf-8")
    paths["ai_chip_revenue_gate"].write_text(render_round32_ai_chip_revenue_gate_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round32_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round32_summary_markdown() -> str:
    summary = round32_summary()
    lines = [
        "# Round-32 Score-Weight v1.7 Summary",
        "",
        f"- source_round: `{ROUND32_SOURCE_ROUND_PATH}`",
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
        "- Round 32 adds v1.7 calibration cases and target weights only.",
        "- Example: a trading house is not scored because revenue is large; it needs resource rights, long-term contracts, FCF, and capital allocation.",
        "- Example: commodity DRAM/NAND can create EPS recovery, but its visibility is lower than HBM unless supply discipline and long-term allocation are source-backed.",
        "- Example: AI-chip related stocks stay RedTeam-first until customer validation, yield, mass-production revenue, and EPS conversion are visible.",
        "- Theme names, case IDs, policy labels, CAPEX headlines, and price rallies are not score evidence by themselves.",
    ]
    return "\n".join(lines) + "\n"


def render_round32_green_guardrail_markdown() -> str:
    lines = [
        "# Round-32 Green Guardrail Review",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "|---|---|---|---|",
    ]
    for target in ROUND32_SCORE_TARGETS:
        lines.append(
            "| "
            f"{target.target_id} | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "- Do not apply v1.7 weights to production scoring yet.",
            "- Do not use case IDs or theme labels as candidate-generation input.",
            "- Do not invent stage dates, prices, contract amounts, LNG volumes, tariff outcomes, OLED margins, MLCC inventory levels, reimbursement status, HBM approval, or foundry yield.",
            "- Do not lower Stage 3-Green thresholds to improve recall.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round32_energy_cycle_markdown() -> str:
    return "\n".join(
        [
            "# Round-32 Energy Cycle Review",
            "",
            "Round 32 separates long-term LNG/offtake evidence from short-lived refining, oil-price, and inventory-cycle effects.",
            "",
            "## Watch-to-Green Evidence",
            "- Long-term LNG or LPG supply contract.",
            "- Procurement stability and price pass-through.",
            "- FCF improvement that is not only inventory gain.",
            "- Tariff and receivables path visible for utilities.",
            "",
            "## Cycle / 4C Risks",
            "- Refining spread normalization.",
            "- Inventory loss or receivables growth.",
            "- Tariff freeze, policy reversal, or geopolitics.",
            "- Debt burden that blocks shareholder return or FCF.",
        ]
    ) + "\n"


def render_round32_memory_split_markdown() -> str:
    return "\n".join(
        [
            "# Round-32 Commodity Memory / HBM Split Review",
            "",
            "Commodity DRAM/NAND and HBM should not receive the same visibility credit.",
            "",
            "## Commodity Memory",
            "- Strong EPS credit when prices, inventory, and OP/EPS revisions improve.",
            "- Lower structural visibility when evidence is only spot price or near-term cycle recovery.",
            "",
            "## HBM-Like Evidence Needed For Higher Conviction",
            "- Customer allocation, supply discipline, or long-term visibility beyond spot recovery.",
            "- HBM customer validation and capacity bottleneck evidence.",
            "- Multi-period consensus revision rather than one quarter of price rebound.",
        ]
    ) + "\n"


def render_round32_ai_chip_revenue_gate_markdown() -> str:
    return "\n".join(
        [
            "# Round-32 AI Chip Revenue Gate Review",
            "",
            "AI-chip and system-semiconductor tags are RedTeam-first until direct revenue exposure is proven.",
            "",
            "## Evidence That Can Help",
            "- Customer contract or foundry deal with economics.",
            "- Mass-production revenue rather than tape-out only.",
            "- Customer validation, yield, and cost path.",
            "- Foundry, packaging, memory, or AI infrastructure linkage that maps to OP/EPS.",
            "",
            "## Green Blockers",
            "- Related-stock label without clear equity or revenue exposure.",
            "- PoC, MOU, or tape-out without customer revenue.",
            "- Yield issue, customer validation failure, or theme overheat.",
        ]
    ) + "\n"


def render_round32_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round-32 Price Validation Plan",
            "",
            "1. Backfill tradable case price paths where symbols exist.",
            "2. Keep synthetic, global reference, and theme counterexamples as `needs_price_backfill` or `missing_price_data`.",
            "3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.",
            "4. Run shadow score-price alignment before any production scoring change.",
            "",
            "## Priority Validation",
            "- Trading/resource: long-term contracts and capital return versus commodity cycle and conglomerate discount.",
            "- Energy/LNG/gas: pass-through and FCF versus tariff, receivables, inventory, and geopolitics.",
            "- OLED/components: customer orders and margins versus CAPEX, price competition, inventory, and supply chain risk.",
            "- Digital healthcare and AI chip: recurring revenue, reimbursement, contracts, validation, yield, and EPS conversion before Green-like interpretation.",
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
    "ROUND32_CASE_CANDIDATES",
    "ROUND32_DEFAULT_CASES_PATH",
    "ROUND32_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND32_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND32_SCORE_TARGETS",
    "ROUND32_SOURCE_ROUND_PATH",
    "Round32CaseCandidate",
    "Round32ScoreTarget",
    "Round32ScoreWeightDraft",
    "render_round32_ai_chip_revenue_gate_markdown",
    "render_round32_energy_cycle_markdown",
    "render_round32_green_guardrail_markdown",
    "render_round32_memory_split_markdown",
    "render_round32_price_validation_plan_markdown",
    "render_round32_summary_markdown",
    "round32_case_candidate_rows",
    "round32_case_records",
    "round32_score_profile_rows",
    "round32_summary",
    "target_for",
    "write_round32_score_weight_reports",
]
