"""Round-267 R11 Loop-12 policy/geopolitical/disaster/event pack.

This module converts ``docs/round/round_267.md`` into calibration-only case
records and reports. It does not change production scoring, staging, or
candidate generation.

Easy example: a government supplementary budget can be Stage 2 relief. It is
not company Stage 3-Green until the relief closes into company revenue, margin,
EPS/FCF, FX stability, and price-after-evidence confirmation.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import CaseDataQuality, E2RCaseRecord, PriceValidation, write_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector


ROUND267_SOURCE_ROUND_PATH = "docs/round/round_267.md"
ROUND267_ANALYST_ROUND_ID = "round_195"
ROUND267_ANALYST_LARGE_SECTOR = "POLICY_GEOPOLITICAL_DISASTER_EVENT"
ROUND267_LARGE_SECTOR = Round10LargeSector.POLICY_GEOPOLITICAL_EVENT
ROUND267_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round267_r11_loop12_policy_geopolitical_event_price_validation"
ROUND267_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r11_loop12_round267.jsonl"
ROUND267_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round267_r11_loop12_policy_geopolitical_event_price_validation_audit.json"

ROUND267_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "LABOR_DISRUPTION_SYSTEMIC_POLICY_4C": E2RArchetype.LABOR_DISRUPTION_SYSTEMIC_POLICY_4C.value,
    "GEOPOLITICAL_ENERGY_MACRO_HARD_4C": E2RArchetype.GEOPOLITICAL_ENERGY_MACRO_HARD_4C.value,
    "FISCAL_POLICY_RELIEF_NOT_GREEN": E2RArchetype.FISCAL_POLICY_RELIEF_NOT_GREEN.value,
    "AI_CAPITAL_MARKET_CONFIDENCE_EVENT": E2RArchetype.AI_CAPITAL_MARKET_CONFIDENCE_EVENT.value,
    "STABLECOIN_FX_POLICY_OVERHEAT": E2RArchetype.STABLECOIN_FX_POLICY_OVERHEAT.value,
    "RARE_EARTH_END_USE_RESTRICTION_4C": E2RArchetype.RARE_EARTH_END_USE_RESTRICTION_4C.value,
    "CRITICAL_MINERALS_POLICY_RELIEF": E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF.value,
    "REGIONAL_POLICY_CAPEX_EVENT_PREMIUM": E2RArchetype.REGIONAL_POLICY_CAPEX_EVENT_PREMIUM.value,
}

ROUND267_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "policy_budget_law_or_binding_action_confirmed",
    "company_revenue_eps_fcf_bridge_exists",
    "capital_inflow_or_fx_stability_confirmed",
    "supply_chain_license_or_end_use_clearance_confirmed",
    "regulated_revenue_or_fee_bridge_confirmed",
    "capex_roi_and_customer_contract_confirmed",
    "operational_continuity_and_labor_risk_cleared",
    "energy_security_cost_shock_absent_or_hedged",
    "price_path_after_evidence",
)

ROUND267_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_headline_only",
    "macro_relief_only",
    "index_milestone_only",
    "stablecoin_theme_only",
    "rare_earth_policy_letter_only",
    "critical_mineral_hotline_only",
    "regional_capex_media_report_only",
    "strike_unresolved",
    "geopolitical_energy_shock_unresolved",
)

ROUND267_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "policy_capex_or_budget_headline_plus_10pct_rally",
    "stablecoin_basket_two_to_three_times",
    "kospi_7000_sidecar_rally",
    "samsung_one_trillion_fomo",
    "securities_rally_before_earnings_bridge",
    "rare_earth_theme_before_license",
    "regional_capex_policy_rally_before_roi",
    "policy_relief_rally_before_company_margin",
)

ROUND267_HARD_4C_GATES: tuple[str, ...] = (
    "systemic_labor_disruption",
    "emergency_arbitration",
    "semiconductor_production_halt",
    "geopolitical_energy_chokepoint_closure",
    "kospi_historic_crash",
    "krw_disorderly_depreciation",
    "stablecoin_capital_outflow",
    "rare_earth_end_use_license_denial",
    "critical_mineral_export_block",
    "policy_capex_roi_failure",
)

ROUND267_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "index_anchor",
    "fx_anchor",
    "policy_amount_anchor",
    "supply_chain_anchor",
    "labor_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d_or_event",
    "mae_1d_or_event",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round267ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round267ShadowWeightRow:
    archetype: E2RArchetype
    systemic_operational_risk: int
    energy_security: int
    fx_stability: int
    policy_funding_quality: int
    fiscal_room_without_new_debt: int
    actual_supply_contract: int
    regulated_revenue: int
    capital_flow_confirmation: int
    emergency_policy_response: int
    event_penalty: int
    four_b_watch_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "systemic_operational_risk": _signed(self.systemic_operational_risk),
            "energy_security": _signed(self.energy_security),
            "fx_stability": _signed(self.fx_stability),
            "policy_funding_quality": _signed(self.policy_funding_quality),
            "fiscal_room_without_new_debt": _signed(self.fiscal_room_without_new_debt),
            "actual_supply_contract": _signed(self.actual_supply_contract),
            "regulated_revenue": _signed(self.regulated_revenue),
            "capital_flow_confirmation": _signed(self.capital_flow_confirmation),
            "emergency_policy_response": _signed(self.emergency_policy_response),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.four_b_watch_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round267DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round267CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    round_case_type: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    stage3_decision: str
    stage4b_status: str
    hard_4c_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    mfe_event: float | None
    mae_event: float | None
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str | bool | list[str]]
    score_price_alignment: str
    round_score_price_alignment: str
    rerating_result: str
    round_rerating_result: str
    stage_failure_type: str
    round_stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND267_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND267_SCORE_ADJUSTMENTS: tuple[Round267ScoreAdjustment, ...] = (
    Round267ScoreAdjustment("systemic_operational_risk", 5, "raise", "삼성전자 파업처럼 기업 이슈가 국가 수출과 AI 공급망 리스크가 될 수 있다."),
    Round267ScoreAdjustment("energy_security", 5, "raise", "중동 에너지 쇼크는 지수, 원화, 자동차, 반도체, 항공을 동시에 흔드는 hard 4C다."),
    Round267ScoreAdjustment("FX_stability", 5, "raise", "stablecoin과 중동 충격은 원화 안정 없이는 Green 검토가 어렵다는 예시다."),
    Round267ScoreAdjustment("policy_funding_quality", 5, "raise", "추경처럼 재원과 금액이 확인된 정책만 headline보다 높게 본다."),
    Round267ScoreAdjustment("fiscal_room_without_new_debt", 4, "raise", "AI 세수 windfall로 추가 국채 없이 집행되는 정책은 relief 품질이 더 높다."),
    Round267ScoreAdjustment("actual_supply_contract", 5, "raise", "희토류/critical minerals는 hotline보다 실제 공급계약과 재고가 중요하다."),
    Round267ScoreAdjustment("regulated_revenue_confirmation", 5, "raise", "stablecoin 테마는 발행허가, 준비금수익, 수수료 수익이 확인되어야 한다."),
    Round267ScoreAdjustment("capital_flow_confirmation", 5, "raise", "KOSPI 7,000 같은 이벤트도 실제 외국인 자금유입과 지속성을 분리해야 한다."),
    Round267ScoreAdjustment("emergency_policy_response_speed", 4, "raise", "에너지·노동·공급망 충격에서는 정책 대응 속도가 Stage 2 relief 품질을 좌우한다."),
    Round267ScoreAdjustment("policy_headline_only", -5, "lower", "정책 headline만 있고 회사 EPS/FCF bridge가 없으면 Green 금지다."),
    Round267ScoreAdjustment("CAPEX_report_only", -5, "lower", "Saemangeum처럼 CAPEX 보도로 가격이 먼저 뛰면 ROI부터 확인한다."),
    Round267ScoreAdjustment("stablecoin_theme_only", -5, "lower", "regulated revenue 없이 2~3배 오른 stablecoin basket은 4B-watch다."),
    Round267ScoreAdjustment("fiscal_spending_without_company_bridge", -4, "lower", "재정지출만 있고 회사 마진 개선이 없으면 relief일 뿐이다."),
    Round267ScoreAdjustment("relief_budget_without_margin_effect", -4, "lower", "고유가 추경도 정유·항공·소비주의 margin bridge가 없으면 Green 근거가 아니다."),
    Round267ScoreAdjustment("index_rally_without_EPS_bridge", -5, "lower", "KOSPI 7,000 지수 milestone은 개별기업 Stage 3-Green과 다르다."),
    Round267ScoreAdjustment("rare_earth_policy_without_contract", -5, "lower", "희토류 정책완화는 실제 offtake, 재고, end-use 허가 전까지 relief다."),
    Round267ScoreAdjustment("labor_disruption_unresolved", -5, "lower", "파업·긴급조정 risk가 열려 있으면 AI/반도체 긍정증거를 RedTeam이 제한해야 한다."),
    Round267ScoreAdjustment("energy_shock_unhedged", -5, "lower", "에너지 shock이 hedge되지 않으면 비용·FX gate를 통과하지 못한다."),
)


ROUND267_SHADOW_WEIGHT_ROWS: tuple[Round267ShadowWeightRow, ...] = (
    Round267ShadowWeightRow(E2RArchetype.LABOR_DISRUPTION_SYSTEMIC_POLICY_4C, 5, 1, 2, 3, 2, 0, 0, 2, 5, 0, 4, 5, "Samsung strike risk can become national export and chip supply-chain 4C-watch."),
    Round267ShadowWeightRow(E2RArchetype.GEOPOLITICAL_ENERGY_MACRO_HARD_4C, 3, 5, 5, 4, 3, 0, 0, 4, 5, 0, 5, 5, "Middle East/Iran shock is hard 4C for oil-import-dependent Korea."),
    Round267ShadowWeightRow(E2RArchetype.FISCAL_POLICY_RELIEF_NOT_GREEN, 2, 4, 4, 5, 5, 0, 0, 3, 5, -4, 4, 4, "Budget and AI fiscal room are relief, not company Green."),
    Round267ShadowWeightRow(E2RArchetype.AI_CAPITAL_MARKET_CONFIDENCE_EVENT, 2, 1, 3, 3, 3, 0, 0, 5, 3, -5, 5, 4, "KOSPI 7,000 is confidence Stage 2 plus 4B overheat watch."),
    Round267ShadowWeightRow(E2RArchetype.STABLECOIN_FX_POLICY_OVERHEAT, 1, 0, 5, 2, 1, 0, 5, 2, 3, -5, 5, 5, "Stablecoin basket rallied before regulated revenue while FX risk rose."),
    Round267ShadowWeightRow(E2RArchetype.RARE_EARTH_END_USE_RESTRICTION_4C, 2, 3, 3, 4, 2, 5, 0, 3, 4, 0, 4, 5, "Rare-earth sanctions/end-use restrictions are strategic supply-chain 4C-watch."),
    Round267ShadowWeightRow(E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF, 1, 3, 3, 5, 3, 5, 0, 3, 4, -5, 4, 4, "Critical-minerals policy is relief until actual supply contracts and inventory confirm."),
    Round267ShadowWeightRow(E2RArchetype.REGIONAL_POLICY_CAPEX_EVENT_PREMIUM, 2, 2, 2, 3, 2, 0, 0, 2, 3, -5, 5, 4, "Hyundai Saemangeum CAPEX headline requires ROI/utilization/FCF bridge."),
)


ROUND267_DEEP_SUB_ARCHETYPES: tuple[Round267DeepSubArchetype, ...] = (
    Round267DeepSubArchetype("반도체 노동·공급망", E2RArchetype.LABOR_DISRUPTION_SYSTEMIC_POLICY_4C, ("Samsung strike", "50,000 workers", "emergency arbitration", "AI supply-chain disruption")),
    Round267DeepSubArchetype("지정학·에너지 hard 4C", E2RArchetype.GEOPOLITICAL_ENERGY_MACRO_HARD_4C, ("Middle East / Iran", "KOSPI -12.06%", "KRW 17-year low", "autos chips airlines drawdown")),
    Round267DeepSubArchetype("재정·에너지 relief", E2RArchetype.FISCAL_POLICY_RELIEF_NOT_GREEN, ("26.2T won supplementary budget", "no new treasury issuance", "10.1T high-oil-price measures", "AI fiscal room")),
    Round267DeepSubArchetype("AI 자본시장 confidence", E2RArchetype.AI_CAPITAL_MARKET_CONFIDENCE_EVENT, ("KOSPI 7000", "Samsung $1T", "sidecar rally", "foreign buying 3.1T won")),
    Round267DeepSubArchetype("stablecoin FX gate", E2RArchetype.STABLECOIN_FX_POLICY_OVERHEAT, ("won stablecoin", "Kakao Pay >2x", "57T won stablecoin trading", "capital outflow risk")),
    Round267DeepSubArchetype("희토류 end-use restriction", E2RArchetype.RARE_EARTH_END_USE_RESTRICTION_4C, ("China sanction warning", "U.S. defense end-use", "transformers batteries displays", "license gate")),
    Round267DeepSubArchetype("critical minerals relief", E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF, ("17 monitored minerals", "250B won overseas mining", "FORGE", "China hotline")),
    Round267DeepSubArchetype("지역 CAPEX event premium", E2RArchetype.REGIONAL_POLICY_CAPEX_EVENT_PREMIUM, ("Hyundai Saemangeum", "10T won capex", "AI data center", "ROI gate")),
)


ROUND267_CASE_CANDIDATES: tuple[Round267CaseCandidate, ...] = (
    Round267CaseCandidate(
        case_id="r11_loop12_samsung_strike_systemic_policy_4c_watch",
        symbol="005930/000660/KOSPI",
        company_name="Samsung Electronics strike / systemic chip policy risk",
        primary_archetype=E2RArchetype.LABOR_DISRUPTION_SYSTEMIC_POLICY_4C,
        secondary_archetypes=(E2RArchetype.HBM_SUPPLY_CHAIN_LABOR_DISRUPTION_OVERLAY, E2RArchetype.MEMORY_HBM_CAPACITY),
        case_type="failed_rerating",
        round_case_type="4c_watch_systemic_labor_policy_risk",
        stage1_date=date(2026, 5, 12),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 15),
        stage3_decision="systemic_labor_disruption_is_red_team_4c_watch_not_positive_ai_chip_stage",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("labor_negotiations_fail", "planned_18_day_strike", "more_than_50000_workers", "government_emergency_arbitration_discussion", "chip_export_ai_supply_chain_risk"),
        red_flag_fields=("systemic_labor_disruption", "strike_unresolved", "semiconductor_production_halt_risk", "national_export_supply_chain_risk"),
        price_data_source="Reuters labor-strike/government-intervention anchors",
        reported_price_anchor="Samsung shares down as much as -9.3%; 18-day strike plan; >50,000 workers could join",
        reported_return_anchor="One-day halt up to 1T won direct loss; prolonged disruption up to 100T won economic damage",
        mfe_event=None,
        mae_event=-9.3,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_event_mae_pct": -9.3, "strike_start_target": "2026-05-21", "planned_strike_duration_days": 18, "potential_workers_involved": 50000, "one_day_direct_loss_estimate_krw_trn": 1.0, "prolonged_economic_damage_estimate_krw_trn": 100.0, "hard_4c_status": "not_confirmed"},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="labor_disruption_systemic_policy_4C_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="company_operational_risk_becomes_macro_policy_gate",
        price_validation_status="reported_stock_anchor_not_full_ohlc",
        notes="Samsung strike risk is company operational risk that can become national export and AI supply-chain policy gate.",
    ),
    Round267CaseCandidate(
        case_id="r11_loop12_middle_east_iran_energy_macro_hard_4c",
        symbol="KOSPI/KRW/005930/000660/005380/003490",
        company_name="Middle East / Iran geopolitical energy shock",
        primary_archetype=E2RArchetype.GEOPOLITICAL_ENERGY_MACRO_HARD_4C,
        secondary_archetypes=(E2RArchetype.GEOPOLITICAL_ENERGY_SECURITY_HARD_4C, E2RArchetype.MACRO_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="macro_hard_4c",
        stage1_date=date(2026, 3, 4),
        stage2_date=date(2026, 3, 31),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 3, 4),
        stage3_decision="middle_east_iran_energy_shock_is_macro_hard_4c_for_oil_import_dependent_korea",
        stage4b_status="hard_4c",
        hard_4c_confirmed=True,
        evidence_fields=("kospi_minus_12_06pct", "kospi_close_5093_54", "krw_1505_8_per_usd", "market_cap_wipeout_817_6tn_krw", "autos_chips_airlines_drawdown", "supplementary_budget_relief"),
        red_flag_fields=("geopolitical_energy_chokepoint_closure", "kospi_historic_crash", "krw_disorderly_depreciation", "market_wide_crash", "energy_shock_unhedged"),
        price_data_source="Reuters macro-market/FX/fiscal-response anchors",
        reported_price_anchor="KOSPI -12.06% to 5,093.54; KRW touched 1,505.8/USD; $553.82B market cap wiped out over two days",
        reported_return_anchor="Hyundai -15.8%, Samsung -11.7%, SK Hynix -9.6%, Korean Air -7.9%",
        mfe_event=None,
        mae_event=-12.06,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=5093.54,
        extra_price_metrics={"kospi_20260304_mae_pct": -12.06, "kospi_20260304_close": 5093.54, "market_cap_wipeout_2d_krw_trn": 817.6, "market_cap_wipeout_2d_usd_bn": 553.82, "krw_20260304_low_per_usd": 1505.8, "hyundai_motor_mae_pct": -15.8, "samsung_electronics_mae_pct": -11.7, "sk_hynix_mae_pct": -9.6, "korean_air_mae_pct": -7.9, "kospi_20260323_mae_pct": -6.49, "kospi_20260323_close": 5405.75, "krw_20260323_per_usd": 1517.3, "foreign_selling_krw_trn": 3.7, "retail_buying_krw_trn": 7.0, "supplementary_budget_krw_trn": 26.2},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break",
        rerating_result="thesis_break",
        round_rerating_result="geopolitical_energy_macro_hard_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="macro_hard_4C",
        price_validation_status="reported_market_and_stock_anchor_not_full_ohlc",
        notes="Confirmed R11 hard 4C: energy chokepoint shock hit index, FX, autos, airlines and chips simultaneously.",
    ),
    Round267CaseCandidate(
        case_id="r11_loop12_energy_saving_oil_budget_policy_relief",
        symbol="refiners/airlines/autos/consumers/KOSPI",
        company_name="Energy-saving campaign and oil-price supplementary budget",
        primary_archetype=E2RArchetype.FISCAL_POLICY_RELIEF_NOT_GREEN,
        secondary_archetypes=(E2RArchetype.POLICY_RELIEF_RESPONSE, E2RArchetype.GEOPOLITICAL_ENERGY_MACRO_HARD_4C),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_relief",
        stage1_date=date(2026, 3, 24),
        stage2_date=date(2026, 3, 31),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="energy_budget_relief_is_stage2_until_sector_margin_and_fcf_bridge_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("energy_saving_campaign", "lng_saving_14000_tons_per_day", "26_2tn_won_supplementary_budget", "10_1tn_won_high_oil_measures", "5tn_won_refiner_support"),
        red_flag_fields=("relief_budget_without_margin_effect", "macro_relief_only", "energy_shock_unhedged"),
        price_data_source="Reuters energy-saving campaign / supplementary-budget anchors",
        reported_price_anchor="LNG saving target up to 14,000 tons/day; 26.2T won budget with 10.1T won high-oil-price measures",
        reported_return_anchor="Policy relief anchor only; sector margin bridge still required",
        mfe_event=None,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"energy_saving_practices": 12, "top_oil_consuming_companies_requested": 50, "nuclear_reactors_to_restart": 5, "lng_saving_target_tons_per_day": 14000, "average_daily_lng_power_usage_tons": 69000, "lng_saving_share_pct": 20.3, "supplementary_budget_krw_trn": 26.2, "high_oil_price_measures_krw_trn": 10.1, "refiner_loss_support_krw_trn": 5.0, "consumer_voucher_budget_krw_trn": 4.8, "growth_boost_expected_pp": 0.2, "new_bond_issuance": False},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate_policy_relief",
        rerating_result="unknown",
        round_rerating_result="energy_policy_relief_not_company_green",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="policy_relief_not_margin_FCF",
        price_validation_status="policy_anchor_not_company_ohlc",
        notes="Energy and fiscal response is relief; company Green requires margin and FCF bridge.",
    ),
    Round267CaseCandidate(
        case_id="r11_loop12_kospi_7000_ai_capital_confidence_4b",
        symbol="KOSPI/005930/000660/securities/financials",
        company_name="KOSPI 7,000 AI capital-market confidence event",
        primary_archetype=E2RArchetype.AI_CAPITAL_MARKET_CONFIDENCE_EVENT,
        secondary_archetypes=(E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.POLICY_CONFIDENCE_EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_plus_4b_watch",
        stage1_date=date(2026, 5, 6),
        stage2_date=date(2026, 5, 6),
        stage3_date=None,
        stage4b_date=date(2026, 5, 6),
        stage4c_date=None,
        stage3_decision="index_confidence_event_is_not_individual_company_green_without_eps_bridge",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("kospi_7000_breakout", "foreign_buying_3_1tn_won", "samsung_one_trillion_market_cap", "sidecar_level_index_rally", "securities_plus_13_5pct"),
        red_flag_fields=("index_rally_without_EPS_bridge", "index_milestone_only", "chip_concentration_fomo", "securities_rally_before_earnings_bridge"),
        price_data_source="Reuters KOSPI 7000 / sector-return anchor",
        reported_price_anchor="KOSPI +6.45% close 7,384.56; intraday +7.06% to 7,426.60",
        reported_return_anchor="Samsung +14.4%, SK Hynix +10.6%, securities +13.5%, foreigners bought 3.1T won",
        mfe_event=6.45,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=7384.56,
        stage3_price_anchor=None,
        stage4b_price_anchor=7384.56,
        stage4c_price_anchor=None,
        extra_price_metrics={"kospi_close": 7384.56, "kospi_event_mfe_pct": 6.45, "kospi_intraday_high": 7426.60, "kospi_intraday_mfe_pct": 7.06, "samsung_mfe_pct": 14.4, "sk_hynix_mfe_pct": 10.6, "samsung_market_cap_milestone_usd_trn": 1.0, "samsung_sk_hynix_kospi_weight_pct": 44.0, "foreign_net_purchase_krw_trn": 3.1, "foreign_net_purchase_usd_bn": 2.13, "securities_firms_mfe_pct": 13.5, "financial_groups_mfe_pct": 4.2},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_result="AI_capital_market_confidence_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_type="index_confidence_not_company_green",
        price_validation_status="reported_index_and_sector_anchor_not_full_ohlc",
        notes="Index confidence is Stage 2; sidecar-level rally and chip concentration require 4B-watch.",
    ),
    Round267CaseCandidate(
        case_id="r11_loop12_ai_fiscal_room_policy_relief",
        symbol="KOSPI/chip_fiscal_policy_beneficiaries",
        company_name="AI boom fiscal room / tax-windfall policy relief",
        primary_archetype=E2RArchetype.FISCAL_POLICY_RELIEF_NOT_GREEN,
        secondary_archetypes=(E2RArchetype.AI_WINDFALL_TAX_POLICY_CONFIDENCE_SHOCK, E2RArchetype.POLICY_RELIEF_RESPONSE),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_relief",
        stage1_date=date(2026, 5, 13),
        stage2_date=date(2026, 5, 13),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="ai_fiscal_room_is_macro_relief_until_company_eps_fcf_bridge_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("fitch_fiscal_room_due_ai_boom", "chip_export_tax_windfall", "stock_rally_tax_windfall", "no_new_treasury_bonds", "26_2tn_won_extra_budget"),
        red_flag_fields=("fiscal_spending_without_company_bridge", "macro_relief_only", "policy_confidence_watch"),
        price_data_source="Reuters Fitch fiscal-space / supplementary-budget anchors",
        reported_price_anchor="26.2T won extra budget funded by excess tax revenue from chip exports and stock rally; no new treasury bonds",
        reported_return_anchor="Fiscal relief anchor, not company OHLC",
        mfe_event=None,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fitch_policy_view": "active fiscal spending room due AI boom", "debt_context_pct_of_gdp": 50.0, "extra_budget_krw_trn": 26.2, "funding_source": "excess tax revenue from chip exports and stock-market rally", "new_treasury_bonds": False, "government_spending_2026_after_budget_krw_trn": 752.1, "spending_growth_vs_2025_pct": 11.8, "fiscal_deficit_after_budget_pct_gdp": 3.8, "debt_to_gdp_after_budget_pct": 50.6},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate_policy_relief",
        rerating_result="unknown",
        round_rerating_result="AI_fiscal_space_relief_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="macro_policy_relief_not_company_green",
        price_validation_status="policy_anchor_not_company_ohlc",
        notes="Fiscal room is macro relief, not company Green, until EPS/FCF bridge exists.",
    ),
    Round267CaseCandidate(
        case_id="r11_loop12_stablecoin_fx_policy_overheat",
        symbol="Kakao_Pay/LG_CNS/Aton/ME2ON/KRW",
        company_name="Stablecoin policy overheat / FX gate",
        primary_archetype=E2RArchetype.STABLECOIN_FX_POLICY_OVERHEAT,
        secondary_archetypes=(E2RArchetype.FX_LIQUIDITY_STABLECOIN_OUTFLOW, E2RArchetype.THEME_VALUATION_OVERHEAT),
        case_type="overheat",
        round_case_type="overheat_plus_4c_watch",
        stage1_date=date(2025, 6, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 6, 1),
        stage4c_date=date(2025, 6, 18),
        stage3_decision="stablecoin_basket_is_price_moved_without_regulated_revenue_and_fx_guardrails",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("won_stablecoin_policy_expectation", "digital_asset_reform", "margin_loans_20_5tn_won", "stablecoin_trading_57tn_won", "bok_fx_capital_flow_warning"),
        red_flag_fields=("stablecoin_theme_only", "stablecoin_capital_outflow", "regulated_revenue_unconfirmed", "issuer_license_unconfirmed", "reserve_income_unconfirmed"),
        price_data_source="FT stablecoin-return / Reuters BOK FX-concern anchors",
        reported_price_anchor="Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x before license or fee revenue",
        reported_return_anchor="Q1 dollar-backed stablecoin trading 57T won / $42B; >$19B capital outflow context",
        mfe_event=200.0,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kakao_pay_mfe_pct": 100.0, "lg_cns_mfe_pct": 70.0, "aton_mfe_pct": 80.0, "me2on_mfe_pct": 200.0, "margin_loans_krw_trn": 20.5, "stablecoin_trading_q1_krw_trn": 57.0, "stablecoin_trading_q1_usd_bn": 42.0, "capital_outflow_context_usd_bn": 19.0, "proposed_minimum_issuer_equity_krw_mn": 500.0, "issuer_license_confirmed": False, "reserve_income_confirmed": False, "fee_revenue_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="price_moved_without_evidence",
        rerating_result="theme_overheat",
        round_rerating_result="stablecoin_policy_overheat_FX_gate",
        stage_failure_type="false_yellow",
        round_stage_failure_type="4B_before_regulated_revenue",
        price_validation_status="reported_basket_anchor_not_full_ohlc",
        notes="Stablecoin-related stocks moved 2~3x before regulated revenue; FX outflow risk remains 4C-watch.",
    ),
    Round267CaseCandidate(
        case_id="r11_loop12_rare_earth_critical_minerals_policy_overlay",
        symbol="transformers/batteries/displays/EV/aerospace/medical_equipment_basket",
        company_name="Rare-earth end-use restriction and critical-minerals policy relief",
        primary_archetype=E2RArchetype.RARE_EARTH_END_USE_RESTRICTION_4C,
        secondary_archetypes=(E2RArchetype.CRITICAL_MINERALS_POLICY_RELIEF, E2RArchetype.STRATEGIC_SUPPLY_CHAIN_EXPORT_CONTROL_EVENT),
        case_type="failed_rerating",
        round_case_type="4c_watch_plus_policy_relief",
        stage1_date=date(2025, 4, 22),
        stage2_date=date(2026, 2, 5),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 22),
        stage3_decision="rare_earth_restriction_is_supply_chain_4c_watch_and_policy_relief_is_not_green_without_supply_contracts",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("china_rare_earth_end_use_letters", "us_defense_customer_restriction", "sanction_warning", "17_critical_minerals_monitoring", "250bn_won_overseas_mining_support", "forge_participation"),
        red_flag_fields=("rare_earth_policy_letter_only", "strategic_supply_chain_sanction", "critical_mineral_export_block", "end_use_license_unconfirmed"),
        price_data_source="Reuters rare-earth restriction / critical-minerals policy anchors",
        reported_price_anchor="China letters warned Korean firms about products using Chinese rare earths sold to U.S. defense firms",
        reported_return_anchor="Korea monitors 17 critical minerals and sets 250B won overseas-mining support",
        mfe_event=None,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"affected_sectors": ["power transformers", "batteries", "displays", "electric vehicles", "aerospace", "medical equipment"], "sanction_warning": True, "critical_minerals_monitored": 17, "overseas_mining_support_krw_bn": 250.0, "overseas_mining_support_usd_mn": 172.35, "policy_tools": ["China hotline", "China joint committee", "U.S.-led FORGE participation", "cooperation with Vietnam and Laos"], "forge_chair_period": "until June 2026"},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch_plus_policy_relief",
        rerating_result="thesis_break",
        round_rerating_result="rare_earth_supply_chain_4C_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="policy_relief_not_supply_contract_green",
        price_validation_status="policy_supply_chain_anchor_not_company_ohlc",
        notes="Supply-chain restriction is 4C-watch; policy relief is not Green without actual supply contracts.",
    ),
    Round267CaseCandidate(
        case_id="r11_loop12_hyundai_saemangeum_regional_capex_event",
        symbol="005380/000270/Hyundai_group_ecosystem",
        company_name="Hyundai Saemangeum AI/hydrogen regional CAPEX",
        primary_archetype=E2RArchetype.REGIONAL_POLICY_CAPEX_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.AI_DATA_CENTER_REAL_ASSET_KOREA, E2RArchetype.HYDROGEN_FUELCELL_CAPEX_OPTIONALITY),
        case_type="event_premium",
        round_case_type="event_premium_success_candidate",
        stage1_date=date(2026, 2, 25),
        stage2_date=date(2026, 2, 25),
        stage3_date=None,
        stage4b_date=date(2026, 2, 25),
        stage4c_date=None,
        stage3_decision="regional_capex_headline_is_not_green_until_roi_customer_contract_utilization_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("hyundai_saemangeum_media_report", "10tn_won_investment_over_five_years", "ai_data_center_robotics_hydrogen_infra", "hyundai_plus_10_5pct", "kia_plus_15pct"),
        red_flag_fields=("CAPEX_report_only", "regional_capex_media_report_only", "capex_roi_unconfirmed", "customer_contract_unconfirmed"),
        price_data_source="Reuters regional investment / event-return anchor",
        reported_price_anchor="Media reports of 10T won investment drove Hyundai +10.5% and Kia +15%",
        reported_return_anchor="Group domestic investment plan 125.2T won from 2026 to 2030; ROI and earnings bridge unconfirmed",
        mfe_event=15.0,
        mae_event=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"potential_investment_krw_trn": 10.0, "potential_investment_usd_bn": 7.0, "investment_period_years": 5, "group_domestic_investment_plan_krw_trn": 125.2, "project_themes": ["robotics", "AI data center", "hydrogen infrastructure", "AI factory", "autonomous driving", "smart factories"], "hyundai_mfe_pct": 10.5, "kia_mfe_pct": 15.0, "relative_kia_vs_hyundai_pp": 4.5, "nvidia_ai_chip_context": 50000, "robot_capacity_target_units_annual_by_2028": 30000},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_result="regional_policy_CAPEX_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_type="capex_headline_not_ROI_green",
        price_validation_status="reported_stock_anchor_not_full_ohlc",
        notes="Regional CAPEX headline moved Hyundai/Kia before ROI, utilization or FCF bridge.",
    ),
)


def round267_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND267_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round267 R11 Loop-12 policy/geopolitical/disaster/event price-validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if "eps" in field or "fcf" in field or "bridge" in field),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "rally" in field or "fomo" in field or "theme" in field or "price" in field or "overheat" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "4c" in field
                or "shock" in field
                or "crash" in field
                or "outflow" in field
                or "disruption" in field
                or "sanction" in field
                or "depreciation" in field
            ),
            must_have_fields=ROUND267_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND267_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_policy_geopolitical_disaster_fx_energy_labor_stablecoin_or_capex_headline_as_green",
                *ROUND267_GREEN_REQUIRED_FIELDS,
                *ROUND267_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_event,
                mae_30d=candidate.mae_event,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.mfe_event is not None
                    or candidate.mae_event is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.88 if candidate.stage2_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round267_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND267_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "primary_archetype": candidate.primary_archetype.value,
                "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
                "case_type": candidate.case_type,
                "round_case_type": candidate.round_case_type,
                "stage1_date": _date_text(candidate.stage1_date),
                "stage2_date": _date_text(candidate.stage2_date),
                "stage3_date": _date_text(candidate.stage3_date),
                "stage4b_date": _date_text(candidate.stage4b_date),
                "stage4c_date": _date_text(candidate.stage4c_date),
                "stage3_decision": candidate.stage3_decision,
                "stage4b_status": candidate.stage4b_status,
                "hard_4c_confirmed": str(candidate.hard_4c_confirmed).lower(),
                "price_data_source": candidate.price_data_source,
                "reported_price_anchor": candidate.reported_price_anchor,
                "reported_return_anchor": candidate.reported_return_anchor,
                "mfe_event": _float_text(candidate.mfe_event),
                "mae_event": _float_text(candidate.mae_event),
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
                "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
                "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
                "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
                "score_price_alignment": candidate.score_price_alignment,
                "round_score_price_alignment": candidate.round_score_price_alignment,
                "rerating_result": candidate.rerating_result,
                "round_rerating_result": candidate.round_rerating_result,
                "stage_failure_type": candidate.stage_failure_type,
                "round_stage_failure_type": candidate.round_stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round267_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND267_SCORE_ADJUSTMENTS)


def round267_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND267_SHADOW_WEIGHT_ROWS)


def round267_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND267_DEEP_SUB_ARCHETYPES)


def round267_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round267_price_validation": "true"} for field in ROUND267_PRICE_VALIDATION_FIELDS)


def round267_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round267_label": label, "canonical_archetype": canonical} for label, canonical in ROUND267_REQUIRED_TARGET_ALIASES.items())


def round267_summary() -> dict[str, int | bool | str]:
    cases = ROUND267_CASE_CANDIDATES
    return {
        "source_round": ROUND267_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND267_ANALYST_ROUND_ID,
        "analyst_large_sector": ROUND267_ANALYST_LARGE_SECTOR,
        "large_sector": ROUND267_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "policy_relief_count": sum(1 for case in cases if "policy_relief" in case.round_case_type),
        "target_archetype_count": len(ROUND267_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND267_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND267_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round267_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND267_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND267_ANALYST_ROUND_ID,
        "analyst_large_sector": ROUND267_ANALYST_LARGE_SECTOR,
        "large_sector": ROUND267_LARGE_SECTOR.value,
        "summary": round267_summary(),
        "target_aliases": dict(ROUND267_REQUIRED_TARGET_ALIASES),
        "round_case_types": {case.case_id: case.round_case_type for case in ROUND267_CASE_CANDIDATES},
        "green_required_fields": list(ROUND267_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND267_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND267_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND267_HARD_4C_GATES),
        "deep_sub_archetypes": round267_deep_sub_archetype_rows(),
        "shadow_weights": round267_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round267_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_policy_geopolitical_disaster_fx_energy_labor_stablecoin_or_capex_headline_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "keep_middle_east_iran_energy_shock_as_macro_hard_4c_reference",
        ],
    }


def render_round267_summary_markdown() -> str:
    summary = round267_summary()
    lines = [
        "# Round 267 R11 Loop 12 Policy Geopolitical Disaster Event Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- analyst_round_id: {summary['analyst_round_id']}",
        f"- analyst_large_sector: {summary['analyst_large_sector']}",
        f"- canonical_large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- policy_relief_count: {summary['policy_relief_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND267_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.case_type,
                    case.round_case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    str(case.hard_4c_confirmed).lower(),
                    case.round_score_price_alignment,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Middle East / Iran energy shock is the confirmed hard 4C reference for this pack.",
            "- Samsung strike, stablecoin FX, and rare-earth restriction are 4C-watch overlays, not positive Green evidence.",
            "- Energy-saving, AI fiscal room, and critical-minerals policies are relief until company EPS/FCF bridges are visible.",
            "- KOSPI 7,000 and Hyundai Saemangeum are event-premium examples: price moved before company evidence fully closed.",
            "- Easy example: `10T won CAPEX headline + stock +10%` is 4B-watch; `CAPEX + customer contract + utilization + FCF` is the bundle required before deeper Stage review.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round267_green_gate_review_markdown() -> str:
    lines = [
        "# Round 267 R11 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND267_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND267_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `AI fiscal room + supplementary budget` can be Stage 2 policy relief.",
            "- `budget + company margin stabilization + EPS/FCF bridge + price after evidence` is the kind of bundle required before Stage 3 review.",
            "- `stablecoin policy + 2x basket rally before license revenue` is 4B-watch, not Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round267_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 267 R11 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND267_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND267_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND267_CASE_CANDIDATES:
        if case.stage4b_status in {"watch", "hard_4c"} or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round267_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 267 R11 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: true",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND267_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def render_round267_deep_sub_archetypes_markdown() -> str:
    lines = ["# Round 267 Deep Sub-Archetypes", "", "| category | archetype | terms |", "|---|---|---|"]
    for row in ROUND267_DEEP_SUB_ARCHETYPES:
        lines.append(f"| {row.category} | {row.primary_archetype.value} | {', '.join(row.terms)} |")
    return "\n".join(lines) + "\n"


def write_round267_r11_loop12_reports(
    output_directory: str | Path = ROUND267_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND267_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND267_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round267_case_records(), cases_path),
        "audit": _write_json(round267_audit_payload(), audit_path),
        "summary": output / "round267_r11_loop12_price_validation_summary.md",
        "case_matrix": output / "round267_r11_loop12_case_matrix.csv",
        "target_aliases": output / "round267_r11_loop12_target_aliases.csv",
        "score_adjustments": output / "round267_r11_loop12_score_adjustments.csv",
        "shadow_weights": output / "round267_r11_loop12_shadow_weights.csv",
        "deep_sub_archetypes": output / "round267_r11_loop12_deep_sub_archetypes.csv",
        "deep_sub_archetypes_md": output / "round267_r11_loop12_deep_sub_archetypes.md",
        "price_validation_fields": output / "round267_r11_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round267_r11_loop12_green_gate_review.md",
        "price_validation_plan": output / "round267_r11_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round267_r11_loop12_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round267_summary_markdown(), encoding="utf-8")
    _write_csv(round267_case_rows(), paths["case_matrix"])
    _write_csv(round267_target_alias_rows(), paths["target_aliases"])
    _write_csv(round267_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round267_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round267_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round267_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round267_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round267_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round267_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["deep_sub_archetypes_md"].write_text(render_round267_deep_sub_archetypes_markdown(), encoding="utf-8")
    return paths


def _write_json(payload: object, path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def _write_csv(rows: Iterable[dict[str, str]], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    rows = tuple(rows)
    if not rows:
        target.write_text("", encoding="utf-8")
        return target
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _float_text(value: float | None) -> str:
    return "" if value is None else f"{value:g}"


def _signed(value: int) -> str:
    return f"{value:+d}"
