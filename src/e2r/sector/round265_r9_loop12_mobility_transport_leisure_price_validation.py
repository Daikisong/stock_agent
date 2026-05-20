"""Round-265 R9 Loop-12 mobility/transport/leisure price validation pack.

This pack converts ``docs/round/round_265.md`` into calibration-only case
records, shadow weights, and guardrail reports. Production scoring is not
changed.

Easy example: T'way's new European routes are useful Stage 2 evidence, but
they are not Stage 3-Green until route yield, load factor, cost and FCF are
visible.
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


ROUND265_SOURCE_ROUND_PATH = "docs/round/round_265.md"
ROUND265_ANALYST_ROUND_ID = "round_193"
ROUND265_LARGE_SECTOR = Round10LargeSector.MOBILITY_TRANSPORT_LEISURE.value
ROUND265_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round265_r9_loop12_mobility_transport_leisure_price_validation"
ROUND265_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r9_loop12_round265.jsonl"
ROUND265_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round265_r9_loop12_mobility_transport_leisure_price_validation_audit.json"

ROUND265_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "AVIATION_SAFETY_HARD_4C": E2RArchetype.AVIATION_SAFETY_HARD_4C.value,
    "LCC_ROUTE_REMEDY_LONG_HAUL_OPTION": E2RArchetype.LCC_ROUTE_REMEDY_LONG_HAUL_OPTION.value,
    "AUTO_COMPONENT_HYBRID_EREV_ASP": E2RArchetype.AUTO_COMPONENT_HYBRID_EREV_ASP.value,
    "AUTO_PARTS_PORTFOLIO_RESTRUCTURING": E2RArchetype.AUTO_PARTS_PORTFOLIO_RESTRUCTURING.value,
    "SHIPPING_GEOPOLITICAL_SECURITY_4C": E2RArchetype.SHIPPING_GEOPOLITICAL_SECURITY_4C.value,
    "SHIPPING_FREIGHT_NORMALIZATION_4C": E2RArchetype.SHIPPING_FREIGHT_NORMALIZATION_4C.value,
    "TOURISM_REDIRECT_EVENT_PREMIUM": E2RArchetype.TOURISM_REDIRECT_EVENT_PREMIUM.value,
    "TRAVEL_CASINO_DEMAND_CONVERSION": E2RArchetype.TRAVEL_CASINO_DEMAND_CONVERSION.value,
}

ROUND265_DEEP_SUB_ARCHETYPES: tuple[str, ...] = (
    "Jeju Air Muan crash / aviation safety trust hard 4C",
    "Air Busan aircraft fire / LCC safety 4C-watch",
    "T'way Air European route remedy / long-haul LCC option",
    "HL Mando hybrid EREV component ASP uplift",
    "Hyundai Mobis lighting-business divestiture / portfolio restructuring",
    "HMM Namu Hormuz vessel attack / shipping security 4C-watch",
    "HMM Pan Ocean freight normalization / Maersk Hapag global proxy",
    "Lotte Tour Yellow Balloon Shinsegae tourism redirect event premium",
)

ROUND265_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "route_yield_confirmed",
    "load_factor_confirmed",
    "fleet_utilization_confirmed",
    "safety_trust_risk_passed",
    "component_asp_to_margin_fcf_confirmed",
    "transaction_value_and_proceeds_use_confirmed",
    "freight_rate_floor_and_route_security_confirmed",
    "tourism_spend_hotel_occupancy_casino_drop_adr_confirmed",
    "logistics_insurance_fuel_cost_controlled",
    "price_path_after_evidence",
)

ROUND265_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "route_rights_only",
    "fleet_count_only",
    "tourist_arrival_headline_only",
    "freight_spike_only",
    "safety_incident_unresolved",
    "divestiture_headline_only",
    "geopolitical_shipping_attack_unresolved",
    "component_asp_without_margin",
)

ROUND265_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "route_remedy_headline_lcc_spike",
    "tourism_redirect_basket_spike_before_spend",
    "component_asp_narrative_spike_before_margin",
    "divestiture_headline_spike_before_value",
    "freight_rate_spike_shipping_basket_rerating",
    "safety_relief_bounce_before_investigation_clears",
)

ROUND265_HARD_4C_GATES: tuple[str, ...] = (
    "fatal_aviation_accident",
    "major_aircraft_fire_or_repeated_safety_incident",
    "independent_probe_or_safety_coverup_risk",
    "shipping_vessel_attack",
    "route_closure_or_war_risk_premium_spike",
    "freight_normalization_rate_collapse",
    "tourism_boycott_or_diplomatic_travel_ban",
    "hotel_casino_spend_failure",
    "component_take_rate_failure",
    "divestiture_failure_or_valuation_disappointment",
)

ROUND265_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_available",
    "reported_price_anchor",
    "reported_event_return",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_1d",
    "event_mae_1d",
    "event_close_return",
    "relative_underperformance_pp",
    "safety_or_investigation_anchor",
    "route_yield_load_factor_anchor",
    "component_asp_or_transaction_anchor",
    "shipping_security_or_freight_anchor",
    "tourism_spend_or_redirect_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round265ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round265ShadowWeightRow:
    archetype: E2RArchetype
    safety_trust: int
    route_yield: int
    load_factor: int
    fleet_utilization: int
    component_take_rate: int
    component_asp: int
    transaction_value_proceeds: int
    freight_rate_floor: int
    logistics_security: int
    tourism_spend_conversion: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "safety_trust": _signed(self.safety_trust),
            "route_yield": _signed(self.route_yield),
            "load_factor": _signed(self.load_factor),
            "fleet_utilization": _signed(self.fleet_utilization),
            "component_take_rate": _signed(self.component_take_rate),
            "component_asp": _signed(self.component_asp),
            "transaction_value_proceeds": _signed(self.transaction_value_proceeds),
            "freight_rate_floor": _signed(self.freight_rate_floor),
            "logistics_security": _signed(self.logistics_security),
            "tourism_spend_conversion": _signed(self.tourism_spend_conversion),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round265CaseCandidate:
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
    mfe_1d: float | None
    mae_1d: float | None
    event_close_return: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str | bool | None]
    round_score_price_alignment: str
    score_price_alignment: str
    round_rerating_result: str
    rerating_result: str
    round_stage_failure_type: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND265_SCORE_ADJUSTMENTS: tuple[Round265ScoreAdjustment, ...] = (
    Round265ScoreAdjustment("safety_trust", 5, "raise", "항공은 load factor보다 safety trust가 먼저다."),
    Round265ScoreAdjustment("route_yield", 5, "raise", "LCC route remedy는 route yield가 확인돼야 Stage 3로 갈 수 있다."),
    Round265ScoreAdjustment("load_factor", 5, "raise", "신규 장거리 노선은 load factor가 economics를 닫는다."),
    Round265ScoreAdjustment("fleet_utilization", 5, "raise", "항공·렌터카·해운 모두 자산 utilization이 margin으로 이어져야 한다."),
    Round265ScoreAdjustment("component_take_rate", 5, "raise", "부품 ASP uplift는 실제 take-rate가 붙어야 한다."),
    Round265ScoreAdjustment("component_asp_uplift", 4, "raise", "hybrid/EREV 고ASP 부품은 Stage 2 증거지만 margin 확인이 필요하다."),
    Round265ScoreAdjustment("transaction_value_and_proceeds", 4, "raise", "부품 포트폴리오 정리는 거래가치와 proceeds use가 확인돼야 한다."),
    Round265ScoreAdjustment("freight_rate_floor", 5, "raise", "해운은 spot spike보다 freight floor와 contract coverage가 중요하다."),
    Round265ScoreAdjustment("logistics_security", 5, "raise", "선박 공격·항로 리스크는 운임보다 먼저 보는 gate다."),
    Round265ScoreAdjustment("tourism_spend_conversion", 5, "raise", "관광은 방문객 수보다 hotel occupancy, casino drop, ADR, package margin이 중요하다."),
    Round265ScoreAdjustment("route_rights_only", -5, "lower", "노선권만으로 route economics를 대체하지 않는다."),
    Round265ScoreAdjustment("aviation_safety_incident", -5, "lower", "항공 안전사고는 즉시 4C gate로 본다."),
    Round265ScoreAdjustment("tourist_arrival_headline_only", -5, "lower", "관광객 headline은 spend/OPM 전 event premium이다."),
    Round265ScoreAdjustment("freight_spike_only", -5, "lower", "운임 급등은 freight floor 전 cyclical이다."),
    Round265ScoreAdjustment("shipping_security_event", -5, "lower", "선박 공격은 insurance, rerouting, delay cost를 먼저 본다."),
    Round265ScoreAdjustment("divestiture_headline_only", -4, "lower", "매각 검토만으로 FCF나 주주환원을 인정하지 않는다."),
    Round265ScoreAdjustment("component_asp_without_margin", -4, "lower", "ASP premium은 margin과 FCF로 닫히기 전 Stage 2다."),
    Round265ScoreAdjustment("fleet_count_without_yield", -4, "lower", "기재 수와 pilot support만으로 수익성을 인정하지 않는다."),
    Round265ScoreAdjustment("china_travel_redirect_only", -4, "lower", "중국 관광 redirect는 spend conversion 전 Green이 아니다."),
)

ROUND265_SHADOW_WEIGHT_ROWS: tuple[Round265ShadowWeightRow, ...] = (
    Round265ShadowWeightRow(E2RArchetype.AVIATION_SAFETY_HARD_4C, 5, 3, 3, 3, 0, 0, 0, 0, 3, 0, 0, 4, 5, "Jeju Air hard 4C and Air Busan 4C-watch prove safety trust overrides airline growth thesis."),
    Round265ShadowWeightRow(E2RArchetype.LCC_ROUTE_REMEDY_LONG_HAUL_OPTION, 4, 5, 5, 5, 0, 0, 0, 0, 2, 0, -4, 5, 4, "T'way route rights are Stage 2; route yield/load factor/lease cost required before Green."),
    Round265ShadowWeightRow(E2RArchetype.AUTO_COMPONENT_HYBRID_EREV_ASP, 2, 0, 0, 0, 5, 5, 0, 0, 1, 0, -3, 4, 3, "HL Mando ASP uplift is Stage 2 until take-rate, margin, backlog and FCF confirm."),
    Round265ShadowWeightRow(E2RArchetype.AUTO_PARTS_PORTFOLIO_RESTRUCTURING, 2, 0, 0, 0, 3, 3, 5, 0, 1, 0, -4, 4, 3, "Hyundai Mobis lighting divestiture needs transaction value/proceeds and margin improvement."),
    Round265ShadowWeightRow(E2RArchetype.SHIPPING_GEOPOLITICAL_SECURITY_4C, 0, 0, 0, 0, 0, 0, 0, 4, 5, 0, 0, 4, 5, "HMM Namu attack is shipping security 4C-watch."),
    Round265ShadowWeightRow(E2RArchetype.SHIPPING_FREIGHT_NORMALIZATION_4C, 0, 0, 0, 0, 0, 0, 0, 5, 4, 0, -5, 5, 5, "Maersk/Hapag show freight normalization can crush shipping earnings."),
    Round265ShadowWeightRow(E2RArchetype.TOURISM_REDIRECT_EVENT_PREMIUM, 2, 0, 0, 0, 0, 0, 0, 0, 1, 5, -5, 5, 3, "Lotte/Yellow Balloon tourism redirect is event premium until spend conversion confirms."),
    Round265ShadowWeightRow(E2RArchetype.TRAVEL_CASINO_DEMAND_CONVERSION, 3, 0, 0, 0, 0, 0, 0, 0, 1, 5, -4, 5, 4, "Hotel/casino/tourism Green requires occupancy, casino drop, ADR and package margin."),
)

ROUND265_CASE_CANDIDATES: tuple[Round265CaseCandidate, ...] = (
    Round265CaseCandidate(
        case_id="r9_loop12_jeju_air_muan_crash_hard_4c",
        symbol="089590",
        company_name="Jeju Air",
        primary_archetype=E2RArchetype.AVIATION_SAFETY_HARD_4C,
        secondary_archetypes=(E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        round_case_type="hard_4c_aviation_safety_trust_break",
        stage1_date=date(2024, 12, 29),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 30),
        stage3_decision="fatal_accident_breaks_safety_trust_so_no_stage3",
        stage4b_status="none",
        hard_4c_confirmed=True,
        evidence_fields=("muan_crash_179_fatalities", "record_low_6920_krw", "market_cap_wipeout_95_7bn_krw", "independent_probe_bill"),
        red_flag_fields=("fatal_aviation_accident", "consumer_trust_shock", "independent_probe", "safety_coverup_questions"),
        price_data_source="Reuters crash / event-return / probe anchors",
        reported_price_anchor="shares as much as -15.7% to 6,920 won; market cap wipeout up to 95.7B won",
        reported_return_anchor="AK Holdings -12%, HanaTour -7%, Very Good Tour -11%; later independent probe bill",
        mfe_1d=None,
        mae_1d=-15.7,
        event_close_return=-8.5,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=6920.0,
        extra_price_metrics={"event_low_price_krw": 6920.0, "event_intraday_mae_pct": -15.7, "implied_pre_event_reference_price_krw": 8210.0, "event_timestamp_mae_pct": -8.5, "market_cap_wipeout_krw_bn": 95.7, "market_cap_wipeout_usd_mn": 65.2, "ak_holdings_mae_pct": -12.0, "hanatour_mae_pct": -7.0, "very_good_tour_mae_pct": -11.0, "fatalities": 179.0},
        round_score_price_alignment="thesis_break",
        score_price_alignment="false_positive_score",
        round_rerating_result="aviation_safety_trust_break",
        rerating_result="thesis_break",
        round_stage_failure_type="hard_4C",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Fatal accident is hard 4C; safety trust overrides route/load-factor thesis.",
    ),
    Round265CaseCandidate(
        case_id="r9_loop12_air_busan_plane_fire_4c_watch",
        symbol="298690",
        company_name="Air Busan",
        primary_archetype=E2RArchetype.AVIATION_SAFETY_HARD_4C,
        secondary_archetypes=(E2RArchetype.AIRLINE_SAFETY_REGULATORY_OVERLAY, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        round_case_type="aviation_safety_incident_4c_watch_not_hard",
        stage1_date=date(2025, 1, 28),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 1, 31),
        stage3_decision="aircraft_fire_is_4c_watch_until_safety_trust_recovers",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("aircraft_fire_incident", "event_low_2325_krw", "event_intraday_mae_6_1pct", "lcc_safety_sensitivity"),
        red_flag_fields=("major_aircraft_fire", "safety_incident_unresolved", "consumer_trust_watch", "fatality_not_confirmed_so_not_hard_4c"),
        price_data_source="Reuters aircraft-fire event-return anchor",
        reported_price_anchor="shares as much as -6.1% to 2,325 won; -3.8% at Reuters timestamp",
        reported_return_anchor="T'way +9%, Jeju Air -0.8%, Korean Air and Asiana flat in same context",
        mfe_1d=None,
        mae_1d=-6.1,
        event_close_return=-3.8,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=2325.0,
        extra_price_metrics={"event_low_price_krw": 2325.0, "event_intraday_mae_pct": -6.1, "implied_pre_event_reference_price_krw": 2476.0, "event_timestamp_mae_pct": -3.8, "tway_same_context_pct": 9.0, "jeju_air_same_context_pct": -0.8, "korean_air_asiana_context": "flat"},
        round_score_price_alignment="thesis_break_watch",
        score_price_alignment="false_positive_score",
        round_rerating_result="aviation_safety_incident_watch",
        rerating_result="thesis_break",
        round_stage_failure_type="4C_watch_not_hard_4C",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Non-fatal fire is 4C-watch, not hard 4C, but safety gate must be elevated.",
    ),
    Round265CaseCandidate(
        case_id="r9_loop12_tway_eu_route_remedy",
        symbol="091810",
        company_name="T'way Air",
        primary_archetype=E2RArchetype.LCC_ROUTE_REMEDY_LONG_HAUL_OPTION,
        secondary_archetypes=(E2RArchetype.LCC_LONG_HAUL_ROUTE_ALLOCATION, E2RArchetype.AIRLINE_INTEGRATION_SCALE),
        case_type="success_candidate",
        round_case_type="success_candidate_route_remedy_stage2",
        stage1_date=date(2024, 2, 1),
        stage2_date=date(2024, 3, 7),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="route_rights_not_green_until_yield_load_factor_fuel_lease_and_execution_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("paris_rome_barcelona_frankfurt_routes", "five_a330_200_aircraft_support", "one_hundred_pilot_support", "management_growth_expectation_30_40pct"),
        red_flag_fields=("route_yield_unverified", "load_factor_unverified", "lease_cost_unverified", "fuel_cost_risk", "route_delay_risk"),
        price_data_source="Reuters route-remedy operational anchor",
        reported_price_anchor="T'way event OHLC unavailable after deep search",
        reported_return_anchor="Four European routes, 5 A330-200, 100 pilots, management +30-40% growth expectation",
        mfe_1d=None,
        mae_1d=None,
        event_close_return=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"new_europe_routes": "Paris|Rome|Barcelona|Frankfurt", "route_start_schedule": "Paris 2024-06; Rome 2024-08; Barcelona 2024-09; Frankfurt 2024-10", "aircraft_support_a330_200": 5.0, "pilot_support": 100.0, "management_growth_expectation_low_pct": 30.0, "management_growth_expectation_high_pct": 40.0},
        round_score_price_alignment="success_candidate_but_insufficient_price_data",
        score_price_alignment="unknown",
        round_rerating_result="LCC_longhaul_route_remedy_watch",
        rerating_result="unknown",
        round_stage_failure_type="route_rights_not_yield_green",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Route rights are Stage 2; route yield, load factor, fuel/lease cost and execution required before Green.",
    ),
    Round265CaseCandidate(
        case_id="r9_loop12_hl_mando_hybrid_erev_component_asp",
        symbol="204320",
        company_name="HL Mando",
        primary_archetype=E2RArchetype.AUTO_COMPONENT_HYBRID_EREV_ASP,
        secondary_archetypes=(E2RArchetype.AUTO_MOBILITY_COMPONENTS, E2RArchetype.HYBRID_COMPONENT_BOTTLENECK),
        case_type="success_candidate",
        round_case_type="success_candidate_component_asp_stage2",
        stage1_date=date(2024, 6, 1),
        stage2_date=date(2024, 6, 25),
        stage3_date=None,
        stage4b_date=date(2024, 6, 25),
        stage4c_date=None,
        stage3_decision="component_asp_uplift_not_green_until_take_rate_margin_backlog_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("event_price_49600_krw", "target_price_58000_krw", "idb_asp_premium_70pct", "sdc_asp_premium_50pct"),
        red_flag_fields=("component_take_rate_unverified", "margin_conversion_unverified", "order_backlog_unverified", "oem_price_pressure_risk"),
        price_data_source="WSJ / MarketWatch Market Talk price and component-ASP anchor",
        reported_price_anchor="shares close +11% at 49,600 won; target price raised 42% to 58,000 won",
        reported_return_anchor="IDB ASP +70%, SDC ASP +50%, target upside +16.9% from event price",
        mfe_1d=11.0,
        mae_1d=None,
        event_close_return=11.0,
        stage2_price_anchor=49600.0,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_price_krw": 49600.0, "event_mfe_pct": 11.0, "implied_pre_event_reference_price_krw": 44685.0, "target_price_krw": 58000.0, "target_price_raise_pct": 42.0, "target_upside_from_event_price_pct": 16.9, "idb_asp_premium_pct": 70.0, "sdc_asp_premium_pct": 50.0},
        round_score_price_alignment="success_candidate",
        score_price_alignment="aligned",
        round_rerating_result="hybrid_EREV_component_ASP_watch",
        rerating_result="unknown",
        round_stage_failure_type="ASP_uplift_not_margin_FCF_green",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Component ASP uplift is Stage 2; customer take-rate, backlog, margin and FCF required before Green.",
    ),
    Round265CaseCandidate(
        case_id="r9_loop12_hyundai_mobis_lighting_divestiture",
        symbol="012330",
        company_name="Hyundai Mobis",
        primary_archetype=E2RArchetype.AUTO_PARTS_PORTFOLIO_RESTRUCTURING,
        secondary_archetypes=(E2RArchetype.AUTO_COMPONENT_RESTRUCTURING_KOREA, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_portfolio_restructuring_stage2",
        stage1_date=date(2025, 12, 1),
        stage2_date=date(2026, 1, 27),
        stage3_date=None,
        stage4b_date=date(2026, 1, 27),
        stage4c_date=None,
        stage3_decision="divestiture_plan_not_green_until_transaction_value_proceeds_margin_and_capital_return_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("lighting_revenue_above_1bn_eur", "opmobility_exterior_lighting_4bn_eur_9m2025", "opmobility_margin_improvement_0_6pp", "deal_finalization_expected_end_2026"),
        red_flag_fields=("transaction_value_unverified", "proceeds_use_unverified", "mobis_price_data_unavailable", "deal_delay_risk"),
        price_data_source="Reuters OPmobility / Hyundai Mobis lighting transaction anchors",
        reported_price_anchor="Hyundai Mobis OHLC unavailable; OPmobility shares +1% early Paris trading",
        reported_return_anchor="Mobis lighting business estimated >1B EUR annual revenue; OPmobility 2025 margin 4.8% vs 4.2%",
        mfe_1d=1.0,
        mae_1d=None,
        event_close_return=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hyundai_mobis_lighting_revenue_estimate_eur_bn": 1.0, "opmobility_exterior_lighting_revenue_9m2025_eur_bn": 4.0, "opmobility_total_2025_revenue_eur_bn": 11.54, "opmobility_2025_operating_margin_pct": 4.8, "opmobility_2024_operating_margin_pct": 4.2, "opmobility_margin_improvement_pp": 0.6, "opmobility_q1_2026_revenue_decline_pct": -0.4, "global_auto_production_decline_context_pct": -3.4, "opmobility_relative_industry_outperformance_pp": 3.0, "opmobility_event_mfe_pct": 1.0},
        round_score_price_alignment="success_candidate_but_price_data_unavailable",
        score_price_alignment="unknown",
        round_rerating_result="auto_parts_portfolio_restructuring_watch",
        rerating_result="unknown",
        round_stage_failure_type="divestiture_plan_not_green_until_value_and_proceeds",
        stage_failure_type="stage2_watch_success",
        price_validation_status="hyundai_mobis_price_data_unavailable_after_deep_search",
        notes="Divestiture is Stage 2 until transaction value, proceeds use, margin improvement and shareholder return confirm.",
    ),
    Round265CaseCandidate(
        case_id="r9_loop12_hmm_namu_hormuz_shipping_security",
        symbol="011200",
        company_name="HMM",
        primary_archetype=E2RArchetype.SHIPPING_GEOPOLITICAL_SECURITY_4C,
        secondary_archetypes=(E2RArchetype.SHIPPING_FREIGHT_CYCLE_KOREA, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        round_case_type="shipping_security_4c_watch",
        stage1_date=date(2026, 5, 4),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 5, 11),
        stage3_decision="geopolitical_shipping_security_not_green_until_route_insurance_delay_and_security_cost_clear",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("hmm_namu_attack_near_hormuz", "engine_room_fire", "forensic_inspection_dubai", "south_korea_condemnation"),
        red_flag_fields=("shipping_vessel_attack", "geopolitical_shipping_security", "insurance_rerouting_delay_cost_unverified", "source_investigation_ongoing"),
        price_data_source="Reuters HMM Namu attack / Hormuz policy-response anchors",
        reported_price_anchor="HMM event OHLC unavailable after deep search",
        reported_return_anchor="HMM-operated cargo ship attacked near Hormuz; engine-room fire and Dubai forensic inspection",
        mfe_1d=None,
        mae_1d=None,
        event_close_return=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"vessel": "HMM Namu", "incident": "attack near Strait of Hormuz; port stern damage; engine-room fire", "forensic_location": "Dubai port", "government_position": "strong condemnation and response after source identification", "possible_source_context": "senior official reportedly said unlikely anyone but Iran, investigation ongoing"},
        round_score_price_alignment="thesis_break_watch",
        score_price_alignment="false_positive_score",
        round_rerating_result="shipping_security_4C_watch",
        rerating_result="thesis_break",
        round_stage_failure_type="geopolitical_shipping_security_not_green",
        stage_failure_type="should_have_been_red",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Direct Korean shipper security event; insurance, rerouting, delay and security cost must be monitored.",
    ),
    Round265CaseCandidate(
        case_id="r9_loop12_hmm_panocean_freight_normalization_watch",
        symbol="011200/028670",
        company_name="HMM / Pan Ocean shipping basket",
        primary_archetype=E2RArchetype.SHIPPING_FREIGHT_NORMALIZATION_4C,
        secondary_archetypes=(E2RArchetype.SHIPPING_FREIGHT_CYCLE, E2RArchetype.CYCLICAL_SUCCESS),
        case_type="cyclical_success",
        round_case_type="cyclical_success_plus_freight_normalization_4c_watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 1, 1),
        stage4c_date=date(2026, 2, 5),
        stage3_decision="freight_cycle_not_green_until_rate_floor_contract_coverage_fcf_and_deleveraging_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("maersk_2026_ebitda_guidance_decline", "red_sea_capacity_release_6_7pct", "new_vessel_capacity_addition_5pct", "hapag_ebit_decline_60_7pct"),
        red_flag_fields=("freight_normalization_rate_collapse", "overcapacity_risk", "route_return_capacity_release", "cyclical_success_not_green"),
        price_data_source="Reuters Maersk/Hapag global shipping-cycle anchors",
        reported_price_anchor="Maersk shares -5.5%; Korean shipping OHLC unavailable",
        reported_return_anchor="Maersk 2026 EBITDA guide $4.5B-$7B vs $9.53B in 2025; Hapag EBIT -60.7%",
        mfe_1d=None,
        mae_1d=-5.5,
        event_close_return=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"maersk_2025_ebitda_usd_bn": 9.53, "maersk_2026_ebitda_guidance_low_usd_bn": 4.5, "maersk_2026_ebitda_guidance_high_usd_bn": 7.0, "maersk_2026_ebitda_decline_low_end_pct": -52.8, "maersk_2026_ebitda_decline_high_end_pct": -26.5, "maersk_event_mae_pct": -5.5, "red_sea_route_return_capacity_release_low_pct": 6.0, "red_sea_route_return_capacity_release_high_pct": 7.0, "new_vessel_capacity_addition_pct": 5.0, "hapag_2025_ebit_usd_bn": 1.1, "hapag_2024_ebit_usd_bn": 2.8, "hapag_ebit_decline_pct": -60.7, "hapag_volume_growth_pct": 8.0, "hapag_average_freight_rate_decline_pct": -8.0},
        round_score_price_alignment="cyclical_success_plus_4C_watch",
        score_price_alignment="unknown",
        round_rerating_result="shipping_freight_normalization_watch",
        rerating_result="cyclical_rerating",
        round_stage_failure_type="freight_cycle_not_green",
        stage_failure_type="yellow_success",
        price_validation_status="korean_shipping_ohlc_unavailable_after_deep_search",
        notes="Freight spike is cyclical; rate floor, contract coverage, FCF and deleveraging required before Green.",
    ),
    Round265CaseCandidate(
        case_id="r9_loop12_lotte_yellowballoon_tourism_redirect",
        symbol="032350/104620/004170",
        company_name="Lotte Tour Development / Yellow Balloon / Shinsegae",
        primary_archetype=E2RArchetype.TOURISM_REDIRECT_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.TRAVEL_CASINO_DEMAND_CONVERSION, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_tourism_redirect_before_spend",
        stage1_date=date(2025, 9, 29),
        stage2_date=date(2025, 11, 17),
        stage3_date=None,
        stage4b_date=date(2025, 11, 21),
        stage4c_date=None,
        stage3_decision="tourist_flow_headline_not_green_until_spend_occupancy_casino_drop_package_margin_and_adr_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("china_group_visa_free_15_days", "china_japan_travel_redirect", "lotte_tour_above_20pct", "yellow_balloon_24pct", "adora_jeju_stay_extension"),
        red_flag_fields=("tourist_arrival_headline_only", "tourism_spend_unverified", "hotel_occupancy_unverified", "casino_drop_unverified", "policy_fade_risk"),
        price_data_source="Reuters tourism visa-free / China-Japan dispute / cruise rerouting anchors",
        reported_price_anchor="Lotte Tour >+20%, Yellow Balloon +24%, Shinsegae +6%",
        reported_return_anchor="Adora Magic City Jeju stay extended to 31-57 hours vs usual 9 hours before spend conversion proof",
        mfe_1d=24.0,
        mae_1d=None,
        event_close_return=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"visa_free_stay_days": 15.0, "programme_period": "2025-09-29_to_2026-06", "lotte_tour_20251117_mfe_pct": 9.6, "lotte_tour_20251121_mfe_pct": 20.0, "yellow_balloon_mfe_pct": 24.0, "shinsegae_mfe_pct": 6.0, "adora_usual_jeju_stay_hours": 9.0, "adora_new_jeju_stay_low_hours": 31.0, "adora_new_jeju_stay_high_hours": 57.0, "jeju_stay_extension_low_pct": 244.4, "jeju_stay_extension_high_pct": 533.3},
        round_score_price_alignment="event_premium",
        score_price_alignment="price_moved_without_evidence",
        round_rerating_result="tourism_redirect_watch",
        rerating_result="event_premium",
        round_stage_failure_type="tourist_flow_headline_not_spend_green",
        stage_failure_type="false_yellow",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Tourism redirect is 4B/event premium until hotel occupancy, casino drop, duty-free spend and package margin confirm.",
    ),
)


def round265_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND265_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND265_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round265 R9 Loop-12 mobility/transport/leisure price validation case. Calibration-only; not production scoring input.",
            stage1_evidence=tuple(field for field in candidate.evidence_fields if "route" in field or "crash" in field or "fire" in field or "visa" in field or "attack" in field),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if "yield" in field or "load_factor" in field or "margin" in field or "fcf" in field or "spend" in field),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "price" in field or "event" in field or "spike" in field or "tourism" in field or "freight" in field or "route" in field),
            stage4c_evidence=tuple(field for field in candidate.red_flag_fields if "safety" in field or "accident" in field or "fire" in field or "attack" in field or "freight" in field or "security" in field or "collapse" in field),
            must_have_fields=ROUND265_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=("; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "failed_rerating", "4c_thesis_break"} else None),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND265_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_mfe_mae_yield_load_factor_spend_margin_or_fcf",
                "do_not_treat_route_rights_tourist_arrivals_freight_spike_divestiture_or_component_asp_as_green",
                "do_not_ignore_aviation_safety_shipping_security_or_freight_normalization_hard_gates",
                f"round_case_type={candidate.round_case_type}",
                f"round_score_price_alignment={candidate.round_score_price_alignment}",
                f"round_rerating_result={candidate.round_rerating_result}",
                f"round_stage_failure_type={candidate.round_stage_failure_type}",
                *ROUND265_GREEN_REQUIRED_FIELDS,
                *ROUND265_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=candidate.stage2_price_anchor is not None or candidate.mfe_1d is not None or candidate.mae_1d is not None or candidate.event_close_return is not None,
                stage_dates_confidence=0.86 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round265_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND265_CASE_CANDIDATES:
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
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mae_1d": _float_text(candidate.mae_1d),
                "event_close_return": _float_text(candidate.event_close_return),
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
                "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
                "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
                "round_score_price_alignment": candidate.round_score_price_alignment,
                "score_price_alignment": candidate.score_price_alignment,
                "round_rerating_result": candidate.round_rerating_result,
                "rerating_result": candidate.rerating_result,
                "round_stage_failure_type": candidate.round_stage_failure_type,
                "stage_failure_type": candidate.stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round265_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND265_SCORE_ADJUSTMENTS)


def round265_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND265_SHADOW_WEIGHT_ROWS)


def round265_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round265_price_validation": "true"} for field in ROUND265_PRICE_VALIDATION_FIELDS)


def round265_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round265_label": label, "canonical_archetype": canonical} for label, canonical in ROUND265_REQUIRED_TARGET_ALIASES.items())


def round265_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple({"deep_sub_archetype": item, "large_sector": ROUND265_LARGE_SECTOR} for item in ROUND265_DEEP_SUB_ARCHETYPES)


def round265_summary() -> dict[str, int | bool | str]:
    cases = ROUND265_CASE_CANDIDATES
    return {
        "source_round": ROUND265_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND265_ANALYST_ROUND_ID,
        "large_sector": ROUND265_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for case in cases if case.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "thesis_break_watch_count": sum(1 for case in cases if "watch" in case.round_score_price_alignment or "4c_watch" in case.round_case_type.lower()),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND265_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND265_DEEP_SUB_ARCHETYPES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round265_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND265_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND265_ANALYST_ROUND_ID,
        "large_sector": ROUND265_LARGE_SECTOR,
        "summary": round265_summary(),
        "target_aliases": dict(ROUND265_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetypes": list(ROUND265_DEEP_SUB_ARCHETYPES),
        "green_required_fields": list(ROUND265_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND265_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND265_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND265_HARD_4C_GATES),
        "case_ids": [case.case_id for case in ROUND265_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_use_round265_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_route_rights_tourist_arrivals_freight_spike_divestiture_or_component_asp_as_green",
            "do_not_ignore_aviation_safety_shipping_security_or_freight_normalization_hard_gates",
            "do_not_invent_ohlc_yield_load_factor_tourism_spend_margin_fcf_or_security_costs",
        ],
    }


def render_round265_summary_markdown() -> str:
    summary = round265_summary()
    lines = [
        "# Round 265 R9 Loop 12 Mobility Transport Leisure Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- analyst_round_id: {summary['analyst_round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- cyclical_success: {summary['cyclical_success_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- full_adjusted_ohlc_complete: {str(summary['full_adjusted_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round type | stage2 | stage3 | 4B | 4C | hard 4C | round alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND265_CASE_CANDIDATES:
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
            "- Jeju Air is direct hard 4C because safety trust breaks before load factor or route growth matters.",
            "- Air Busan is 4C-watch: non-fatal, but still an elevated aviation safety gate.",
            "- T'way route remedy is Stage 2; route yield and load factor decide promotion.",
            "- HL Mando is component ASP Stage 2; take-rate, margin and FCF are required before Green.",
            "- Hyundai Mobis lighting divestiture is Stage 2 until transaction value, proceeds and margin improvement are visible.",
            "- HMM Namu attack is shipping-security 4C-watch, not a freight-rate positive.",
            "- HMM/Pan Ocean freight cycle is cyclical success plus normalization 4C-watch.",
            "- Tourism redirect is event premium until hotel/casino/duty-free spend conversion appears.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round265_green_gate_review_markdown() -> str:
    lines = [
        "# Round 265 R9 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND265_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND265_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND265_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `route rights` are not Green until yield, load factor and cost are visible.",
            "- `tourism reroute +24%` is event premium until hotel/casino/duty-free spend appears.",
            "- `freight spike` can be cyclical success, but route security and rate floor decide durability.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round265_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 265 R9 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND265_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND265_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | 4C date | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND265_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.stage4b_status} | {_date_text(case.stage4c_date)} | "
            f"{str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round265_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 265 R9 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- hard_4c_confirmed: true",
        "- Do not invent OHLC, peak, MFE, MAE, stage prices, route yield, load factor, tourism spend, margin, FCF, security costs, or compensation liabilities.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND265_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND265_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def render_round265_deep_sub_archetypes_markdown() -> str:
    lines = [
        "# Round 265 R9 Deep Sub-Archetypes",
        "",
        "These labels describe research coverage. They are not production scoring inputs.",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND265_DEEP_SUB_ARCHETYPES)
    return "\n".join(lines) + "\n"


def write_round265_r9_loop12_reports(
    output_directory: str | Path = ROUND265_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND265_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND265_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round265_case_records(), cases_path),
        "audit": _write_json(round265_audit_payload(), audit_path),
        "summary": output / "round265_r9_loop12_price_validation_summary.md",
        "case_matrix": output / "round265_r9_loop12_case_matrix.csv",
        "target_aliases": output / "round265_r9_loop12_target_aliases.csv",
        "deep_sub_archetypes": output / "round265_r9_loop12_deep_sub_archetypes.csv",
        "score_adjustments": output / "round265_r9_loop12_score_adjustments.csv",
        "shadow_weights": output / "round265_r9_loop12_shadow_weights.csv",
        "price_validation_fields": output / "round265_r9_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round265_r9_loop12_green_gate_review.md",
        "price_validation_plan": output / "round265_r9_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round265_r9_loop12_stage4b_4c_review.md",
        "deep_sub_archetype_review": output / "round265_r9_loop12_deep_sub_archetypes.md",
    }
    paths["summary"].write_text(render_round265_summary_markdown(), encoding="utf-8")
    _write_csv(round265_case_rows(), paths["case_matrix"])
    _write_csv(round265_target_alias_rows(), paths["target_aliases"])
    _write_csv(round265_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round265_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round265_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round265_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round265_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round265_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round265_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["deep_sub_archetype_review"].write_text(render_round265_deep_sub_archetypes_markdown(), encoding="utf-8")
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
