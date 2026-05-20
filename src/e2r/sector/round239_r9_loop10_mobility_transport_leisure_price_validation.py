"""Round-239 R9 Loop-10 mobility/transport/leisure price validation pack.

Round 239 is calibration/evaluation material only. It turns
``docs/round/round_239.md`` into case-library records and guardrail reports.

Easy example: a new Europe route allocation can make an airline visible at
Stage 2. It is not Stage 3-Green until load factor, route yield, aircraft and
crew costs, FCF after capex, and safety/service execution are visible.
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


ROUND239_SOURCE_ROUND_PATH = "docs/round/round_239.md"
ROUND239_ANALYST_ROUND_ID = "round_167"
ROUND239_LARGE_SECTOR = Round10LargeSector.MOBILITY_TRANSPORT_LEISURE
ROUND239_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round239_r9_loop10_mobility_transport_leisure_price_validation"
ROUND239_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r9_loop10_round239.jsonl"
ROUND239_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round239_r9_loop10_mobility_transport_leisure_price_validation_audit.json"

ROUND239_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "FUTURE_MOBILITY_AI_ROBOTICS_CAPEX": E2RArchetype.FUTURE_MOBILITY_AI_ROBOTICS_CAPEX.value,
    "AUTO_PARTS_QUALITY_RECALL_4C": E2RArchetype.AUTO_PARTS_QUALITY_RECALL_4C.value,
    "RAIL_EXPORT_ORDER_TO_DELIVERY": E2RArchetype.RAIL_EXPORT_ORDER_TO_DELIVERY.value,
    "LCC_LONG_HAUL_ROUTE_ALLOCATION": E2RArchetype.LCC_LONG_HAUL_ROUTE_ALLOCATION.value,
    "LCC_CONSOLIDATION_INTEGRATION": E2RArchetype.LCC_CONSOLIDATION_INTEGRATION.value,
    "SHIPPING_DRY_BULK_CYCLE": E2RArchetype.SHIPPING_DRY_BULK_CYCLE.value,
    "TOURISM_REDIRECT_EVENT_PREMIUM": E2RArchetype.TOURISM_REDIRECT_EVENT_PREMIUM.value,
    "AIRLINE_SAFETY_OPERATIONAL_TRUST_4C": E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
}

ROUND239_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "unit_economics",
    "fcf_after_capex",
    "utilization_or_load_factor",
    "route_yield_or_contract_margin",
    "contract_delivery_or_fleet_productivity",
    "safety_quality_operational_trust_passed",
    "labor_integration_maintenance_risk_passed",
    "tourist_spend_occupancy_or_casino_drop",
    "freight_rate_floor_and_contract_coverage",
    "price_path_after_evidence",
)

ROUND239_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "future_mobility_capex_headline_only",
    "robotics_ai_city_theme_only",
    "route_allocation_without_yield",
    "fleet_count_without_margin",
    "tourism_redirect_event_only",
    "freight_rate_cycle_only",
    "quality_recall_issue",
    "fatal_safety_accident",
)

ROUND239_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "future_mobility_investment_rally_before_revenue",
    "tourism_reroute_rally_before_spend",
    "lcc_route_rally_before_load_factor",
    "fleet_integration_rally_before_synergy",
    "shipping_cycle_rerating_before_freight_floor",
    "robotics_ai_hydrogen_headline_valuation_expansion",
)

ROUND239_HARD_4C_GATES: tuple[str, ...] = (
    "fatal_safety_accident",
    "operational_trust_break",
    "quality_recall_with_earnings_or_reputation_damage",
    "route_launch_failure",
    "fleet_integration_failure",
    "labor_disruption_blocking_deployment",
    "capex_overrun",
    "fcf_deterioration",
    "freight_rate_collapse",
    "tourist_spend_failure",
    "casino_utilization_collapse",
    "consumer_trust_shock",
)

ROUND239_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "mfe_event",
    "mae_event",
    "contract_or_investment_anchor",
    "fleet_or_capacity_anchor",
    "tourism_or_safety_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round239ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round239ShadowWeightRow:
    archetype: E2RArchetype
    unit_economics: int
    fcf_after_capex: int
    utilization: int
    contract_delivery: int
    route_yield: int
    fleet_synergy: int
    safety_trust: int
    quality_recall_control: int
    tourist_spend: int
    event_penalty: int
    cycle_normalization_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "unit_economics": _signed(self.unit_economics),
            "fcf_after_capex": _signed(self.fcf_after_capex),
            "utilization": _signed(self.utilization),
            "contract_delivery": _signed(self.contract_delivery),
            "route_yield": _signed(self.route_yield),
            "fleet_synergy": _signed(self.fleet_synergy),
            "safety_trust": _signed(self.safety_trust),
            "quality_recall_control": _signed(self.quality_recall_control),
            "tourist_spend": _signed(self.tourist_spend),
            "event_penalty": _signed(self.event_penalty),
            "cycle_normalization_redteam": _signed(self.cycle_normalization_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round239CaseCandidate:
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
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str | bool]
    score_price_alignment: str
    round_score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND239_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND239_SCORE_ADJUSTMENTS: tuple[Round239ScoreAdjustment, ...] = (
    Round239ScoreAdjustment("unit_economics", 5, "raise", "R9는 수요보다 한 대/한 노선/한 계약이 실제로 돈을 버는지가 핵심이다."),
    Round239ScoreAdjustment("fcf_after_capex", 5, "raise", "미래모빌리티·항공·철도 투자는 capex 이후 FCF가 확인돼야 Stage 3를 검토한다."),
    Round239ScoreAdjustment("utilization", 5, "raise", "항공기·선박·열차·로봇은 가동률과 생산성이 이익으로 닫혀야 한다."),
    Round239ScoreAdjustment("contract_delivery_schedule", 4, "raise", "철도/인프라 수주는 납품·마진·현금회수 일정이 있어야 품질이 생긴다."),
    Round239ScoreAdjustment("load_factor_with_yield", 5, "raise", "항공 노선은 탑승률만이 아니라 yield와 비용이 같이 필요하다."),
    Round239ScoreAdjustment("route_profitability", 5, "raise", "장거리 LCC는 노선권보다 노선 손익이 Stage 3 증거다."),
    Round239ScoreAdjustment("fleet_integration_synergy", 4, "raise", "LCC 통합은 fleet count보다 integration synergy와 서비스 품질이 중요하다."),
    Round239ScoreAdjustment("maintenance_safety_trust", 5, "raise", "운송 섹터는 safety trust가 깨지면 수요 논리가 바로 훼손된다."),
    Round239ScoreAdjustment("quality_recall_control", 5, "raise", "자동차부품은 품질/recall 비용 통제가 Green 전제다."),
    Round239ScoreAdjustment("tourist_spend_conversion", 5, "raise", "관광주는 입국자 수보다 spend, occupancy, casino drop, OPM으로 확인한다."),
    Round239ScoreAdjustment("casino_drop_and_hold", 4, "raise", "카지노/복합리조트는 drop과 hold가 실제 OP로 이어져야 한다."),
    Round239ScoreAdjustment("freight_rate_floor", 4, "raise", "해운은 운임 반등보다 floor와 contract coverage가 있어야 한다."),
    Round239ScoreAdjustment("future_mobility_capex_headline", -5, "lower", "AI/robotics 투자설만으로는 robot/software revenue가 아니다."),
    Round239ScoreAdjustment("robotics_ai_city_theme_only", -5, "lower", "AI city/hydrogen/robotics 테마만 있으면 4B/event premium으로 둔다."),
    Round239ScoreAdjustment("route_allocation_without_yield", -4, "lower", "노선 배정만 있고 yield/load factor가 없으면 Stage 2에 머문다."),
    Round239ScoreAdjustment("fleet_count_without_margin", -4, "lower", "fleet count는 integration cost와 margin 확인 전 Green 증거가 아니다."),
    Round239ScoreAdjustment("tourism_redirect_event_only", -5, "lower", "관광 reroute 기대만으로는 spend/occupancy가 아니다."),
    Round239ScoreAdjustment("freight_rate_cycle_only", -5, "lower", "운임 사이클만으로 구조적 Green을 주지 않는다."),
    Round239ScoreAdjustment("quality_recall_issue", -5, "lower", "품질/recall은 자동차부품 RedTeam 입력이다."),
    Round239ScoreAdjustment("safety_trust_break", -5, "lower", "fatal accident나 안전 신뢰 붕괴는 hard 4C 후보가 된다."),
    Round239ScoreAdjustment("labor_disruption_risk", -4, "lower", "노동 갈등이 deployment를 막으면 미래모빌리티 capex 점수를 낮춘다."),
    Round239ScoreAdjustment("capex_without_fcf", -4, "lower", "capex만 있고 FCF bridge가 없으면 4B-watch다."),
)


ROUND239_SHADOW_WEIGHT_ROWS: tuple[Round239ShadowWeightRow, ...] = (
    Round239ShadowWeightRow(E2RArchetype.FUTURE_MOBILITY_AI_ROBOTICS_CAPEX, 3, 5, 4, 2, 0, 0, 3, 2, 0, -5, 2, 5, 4, "Hyundai/Kia AI/robotics capex is Stage 2 and 4B-watch before robot/software revenue."),
    Round239ShadowWeightRow(E2RArchetype.AUTO_PARTS_QUALITY_RECALL_4C, 4, 5, 4, 3, 0, 0, 5, 5, 0, -2, 3, 4, 5, "Hyundai Mobis ICCU defect requires quality/reputation RedTeam."),
    Round239ShadowWeightRow(E2RArchetype.RAIL_EXPORT_ORDER_TO_DELIVERY, 5, 5, 5, 5, 0, 0, 4, 3, 0, -2, 3, 3, 4, "Hyundai Rotem rail order is Stage 2 until delivery/margin/cash collection confirm."),
    Round239ShadowWeightRow(E2RArchetype.LCC_LONG_HAUL_ROUTE_ALLOCATION, 5, 5, 5, 2, 5, 3, 5, 3, 0, -4, 3, 5, 4, "T'way Europe routes require load factor/yield and cost control before Green."),
    Round239ShadowWeightRow(E2RArchetype.LCC_CONSOLIDATION_INTEGRATION, 5, 5, 5, 2, 5, 5, 5, 3, 0, -3, 3, 4, 4, "Jin/Air Busan/Air Seoul integration is Stage 2 until synergy and safety/service quality confirm."),
    Round239ShadowWeightRow(E2RArchetype.SHIPPING_DRY_BULK_CYCLE, 4, 5, 4, 2, 0, 0, 2, 0, 0, -5, 5, 5, 4, "Pan Ocean is cyclical success; freight floor/FCF/deleveraging required."),
    Round239ShadowWeightRow(E2RArchetype.TOURISM_REDIRECT_EVENT_PREMIUM, 4, 4, 4, 0, 0, 0, 3, 0, 5, -5, 4, 5, 4, "Lotte Tour/Yellow Balloon redirect rally is event premium until spend/occupancy/casino drop confirm."),
    Round239ShadowWeightRow(E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 5, 5, 5, "Jeju Air fatal crash is hard 4C."),
)


ROUND239_CASE_CANDIDATES: tuple[Round239CaseCandidate, ...] = (
    Round239CaseCandidate(
        case_id="r9_loop10_hyundai_kia_future_mobility_capex_4b",
        symbol="005380/000270",
        company_name="현대차/기아",
        primary_archetype=E2RArchetype.FUTURE_MOBILITY_AI_ROBOTICS_CAPEX,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="success_candidate",
        round_case_type="success_candidate_event_premium_labor_capex_watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 2, 25),
        stage3_date=None,
        stage4b_date=date(2026, 2, 25),
        stage4c_date=date(2026, 1, 22),
        stage3_decision="future_mobility_capex_is_stage2_until_robot_software_revenue_utilization_fcf_and_labor_pass_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("hyundai_event_mfe_10_5pct", "kia_event_mfe_15pct", "saemangeum_investment_10tn_krw", "domestic_investment_125_2tn_krw", "nvidia_ai_chips_50000", "robotics_capacity_30000_units_by_2028"),
        red_flag_fields=("future_mobility_capex_headline_only", "robotics_ai_city_theme_only", "labor_disruption_risk", "software_revenue_unverified", "fcf_after_capex_unverified"),
        price_data_source="Reuters investment/event-return/labor-risk anchors",
        reported_price_anchor="Hyundai +10.5%; Kia +15.0% on future-mobility investment report",
        reported_return_anchor="10T KRW Saemangeum report; 125.2T KRW domestic investment plan; up to 50,000 Nvidia chips",
        mfe_1d=15.0,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hyundai_event_mfe_1d_pct": 10.5, "kia_event_mfe_1d_pct": 15.0, "saemangeum_investment_krw_tn": 10.0, "hyundai_group_domestic_investment_2026_2030_krw_tn": 125.2, "nvidia_ai_chip_allocation": 50000.0, "robotics_capacity_target_annual_units": 30000.0, "robotics_capacity_target_year": 2028.0, "georgia_factory_capacity_target_units": 500000.0},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="event_premium_success_candidate",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Future-mobility capex is Stage 2 and 4B-watch; robot/software revenue and FCF are required before Green.",
    ),
    Round239CaseCandidate(
        case_id="r9_loop10_hyundai_mobis_iccu_quality_recall_watch",
        symbol="012330",
        company_name="현대모비스",
        primary_archetype=E2RArchetype.AUTO_PARTS_QUALITY_RECALL_4C,
        secondary_archetypes=(E2RArchetype.AUTO_MOBILITY_COMPONENTS,),
        case_type="4c_thesis_break",
        round_case_type="4c_watch_evidence_good_but_quality_failed",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 5, 1),
        stage3_decision="ev_parts_exposure_cannot_be_green_while_recurring_iccu_recall_threatens_earnings_and_reputation",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("event_price_225500_krw", "event_mae_minus_0_7pct", "target_price_265000_krw", "target_cut_12pct", "iccu_defect", "hyundai_kia_ev_recall"),
        red_flag_fields=("quality_recall_issue", "earnings_reputation_damage_watch", "recurring_iccu_defect", "ev_component_exposure_not_green"),
        price_data_source="WSJ/MarketWatch Market Talk price and recall-risk anchor",
        reported_price_anchor="225,500 KRW, -0.7%; target cut 12% to 265,000 KRW",
        reported_return_anchor="implied prior target about 301,136 KRW; target upside from event price +17.5%",
        mfe_1d=None,
        mae_1d=-0.7,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=225500.0,
        extra_price_metrics={"event_price_krw": 225500.0, "event_mae_pct": -0.7, "target_price_krw": 265000.0, "target_cut_pct": -12.0, "implied_prior_target_krw": 301136.0, "target_upside_from_event_price_pct": 17.5, "recall_issue": "Integrated Control Charging Unit defect", "hyundai_kia_ev_recall": True},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="EV-parts exposure cannot become Green while recurring ICCU defect threatens earnings and reputation.",
    ),
    Round239CaseCandidate(
        case_id="r9_loop10_hyundai_rotem_morocco_rail_order",
        symbol="064350",
        company_name="현대로템",
        primary_archetype=E2RArchetype.RAIL_EXPORT_ORDER_TO_DELIVERY,
        secondary_archetypes=(),
        case_type="success_candidate",
        round_case_type="success_candidate_rail_export_order",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 2, 26),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="rail_export_order_is_stage2_until_delivery_margin_working_capital_and_cash_collection_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("morocco_total_168_trains", "morocco_program_2_9bn_usd", "hyundai_rotem_order_2_2tn_krw", "hyundai_rotem_order_1_54bn_usd", "hyundai_train_count_110", "order_share_53_1pct"),
        red_flag_fields=("delivery_schedule_unverified", "margin_unverified", "working_capital_unverified", "cash_collection_unverified"),
        price_data_source="Reuters rail-contract evidence",
        reported_price_anchor="Stock OHLC unavailable after deep search",
        reported_return_anchor="2.2T KRW / $1.54B order for 110 urban trains; 53.1% of Morocco program value",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"morocco_total_train_purchase": 168.0, "morocco_total_program_value_usd_bn": 2.9, "hyundai_rotem_order_krw_tn": 2.2, "hyundai_rotem_order_usd_bn": 1.54, "hyundai_train_count": 110.0, "hyundai_order_share_of_total_program_pct": 53.1, "alstom_high_speed_trains": 18.0, "caf_intercity_trains": 40.0, "morocco_network_target_cities": 43.0, "morocco_population_coverage_target_pct": 87.0},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Rail export order is Stage 2; delivery, margin, working capital and cash collection are required before Green.",
    ),
    Round239CaseCandidate(
        case_id="r9_loop10_tway_europe_route_allocation",
        symbol="091810",
        company_name="티웨이항공",
        primary_archetype=E2RArchetype.LCC_LONG_HAUL_ROUTE_ALLOCATION,
        secondary_archetypes=(E2RArchetype.AIRLINE_TRAVEL_CYCLE,),
        case_type="success_candidate",
        round_case_type="success_candidate_long_haul_lcc_route_allocation",
        stage1_date=date(2024, 2, 1),
        stage2_date=date(2024, 3, 7),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="route_allocation_is_stage2_until_load_factor_yield_lease_crew_fuel_and_safety_execution_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("paris_rome_barcelona_frankfurt_routes", "five_a330_200_aircraft", "korean_air_100_pilots", "maintenance_support", "growth_target_30_40pct"),
        red_flag_fields=("route_allocation_without_yield", "load_factor_unverified", "crew_cost_unverified", "fuel_cost_unverified", "safety_service_execution_unverified"),
        price_data_source="Reuters route-allocation evidence",
        reported_price_anchor="Stock OHLC unavailable after deep search",
        reported_return_anchor="Paris/Rome/Barcelona/Frankfurt routes; five A330-200 aircraft; 100 pilots; +30~40% growth target",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"new_europe_route_count": 4.0, "korean_air_support_aircraft_count": 5.0, "korean_air_support_pilots": 100.0, "maintenance_support": True, "growth_expectation_low_pct": 30.0, "growth_expectation_high_pct": 40.0, "existing_a330_300_count": 3.0},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Route allocation is Stage 2; load factor, yield, aircraft cost, crew cost, fuel and safety/service execution are required before Green.",
    ),
    Round239CaseCandidate(
        case_id="r9_loop10_jin_air_air_busan_air_seoul_integration",
        symbol="272450/298690/Asiana_LCC_exposure",
        company_name="진에어/에어부산/에어서울",
        primary_archetype=E2RArchetype.LCC_CONSOLIDATION_INTEGRATION,
        secondary_archetypes=(E2RArchetype.AIRLINE_INTEGRATION_SCALE,),
        case_type="success_candidate",
        round_case_type="success_candidate_lcc_consolidation_integration",
        stage1_date=date(2024, 11, 1),
        stage2_date=date(2024, 11, 29),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="lcc_consolidation_is_stage2_until_integration_cost_route_optimization_load_factor_yield_and_safety_quality_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("combined_lcc_aircraft_58", "jeju_air_aircraft_42", "tway_aircraft_39", "capacity_share_8pct", "single_brand_plan"),
        red_flag_fields=("fleet_count_without_margin", "integration_cost_unverified", "route_profitability_unverified", "safety_service_quality_unverified"),
        price_data_source="Reuters LCC integration evidence",
        reported_price_anchor="Jin Air or Air Busan OHLC unavailable after deep search",
        reported_return_anchor="combined 58 aircraft, +38.1% vs Jeju Air fleet, +48.7% vs T'way fleet; 8% capacity share",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"combined_lcc_aircraft": 58.0, "jeju_air_aircraft": 42.0, "tway_aircraft": 39.0, "combined_lcc_aircraft_advantage_vs_jeju_pct": 38.1, "combined_lcc_aircraft_advantage_vs_tway_pct": 48.7, "combined_capacity_share_nov_2024_pct": 8.0},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="LCC consolidation is Stage 2; integration cost, route optimization, load factor/yield and safety/service quality are required before Green.",
    ),
    Round239CaseCandidate(
        case_id="r9_loop10_pan_ocean_dry_bulk_cycle",
        symbol="028670",
        company_name="팬오션",
        primary_archetype=E2RArchetype.SHIPPING_DRY_BULK_CYCLE,
        secondary_archetypes=(E2RArchetype.SHIPPING_FREIGHT_CYCLE,),
        case_type="cyclical_success",
        round_case_type="cyclical_success_dry_bulk_lng_fleet_expansion",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 5, 31),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="dry_bulk_fleet_expansion_is_stage2_cycle_until_freight_floor_contract_coverage_fcf_and_deleveraging_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("event_price_4615_krw", "event_mae_minus_0_2pct", "target_price_6700_krw", "target_upside_45_2pct", "op_forecast_536bn_krw", "op_growth_forecast_39pct", "lng_carrier_addition_2h"),
        red_flag_fields=("freight_rate_cycle_only", "price_failed_on_target_raise", "freight_floor_unverified", "contract_coverage_unverified", "deleveraging_unverified"),
        price_data_source="WSJ/MarketWatch Market Talk shipping anchor",
        reported_price_anchor="4,615 KRW, -0.2%; target 6,700 KRW",
        reported_return_anchor="target raise +3.1%; target upside +45.2%; 2024 OP forecast 536B KRW, +39%",
        mfe_1d=None,
        mae_1d=-0.2,
        stage1_price_anchor=None,
        stage2_price_anchor=4615.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_price_krw": 4615.0, "event_mae_pct": -0.2, "target_price_krw": 6700.0, "target_price_before_krw": 6500.0, "target_raise_pct": 3.1, "target_upside_from_event_price_pct": 45.2, "op_forecast_2024_krw_bn": 536.0, "op_growth_forecast_pct": 39.0, "implied_prior_op_krw_bn": 385.6, "lng_carrier_addition": "more LNG carriers due in 2H"},
        score_price_alignment="evidence_good_but_price_failed",
        round_score_price_alignment="cyclical_success_evidence_good_but_price_failed",
        rerating_result="cyclical_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Dry bulk/fleet expansion is Stage 2/cycle; freight-rate floor, contract coverage, FCF and deleveraging are required before Green.",
    ),
    Round239CaseCandidate(
        case_id="r9_loop10_lotte_tour_yellow_balloon_china_japan_redirect",
        symbol="032350/104620/004170",
        company_name="롯데관광개발/노랑풍선/신세계",
        primary_archetype=E2RArchetype.TOURISM_REDIRECT_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="event_premium",
        round_case_type="event_premium_price_moved_without_evidence",
        stage1_date=date(2025, 11, 17),
        stage2_date=date(2025, 11, 21),
        stage3_date=None,
        stage4b_date=date(2025, 11, 21),
        stage4c_date=None,
        stage3_decision="tourism_redirect_is_stage1_2_event_until_arrivals_spend_occupancy_casino_drop_adr_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("lotte_tour_mfe_20pct_plus", "yellow_balloon_mfe_24pct", "shinsegae_mfe_6pct", "adora_magic_city_japan_stop_cancel", "jeju_stay_extended"),
        red_flag_fields=("tourism_redirect_event_only", "tourist_spend_unverified", "occupancy_unverified", "casino_drop_unverified", "event_premium_watch"),
        price_data_source="Reuters tourism-redirect event anchor",
        reported_price_anchor="Lotte Tour +20%+, Yellow Balloon +24%, Shinsegae +6%",
        reported_return_anchor="Adora Magic City cancels Fukuoka/Nagasaki stops and extends Jeju stay; early signs only",
        mfe_1d=24.0,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"lotte_tour_event_mfe_pct": 20.0, "yellow_balloon_event_mfe_pct": 24.0, "shinsegae_event_mfe_pct": 6.0, "historical_context_china_tourist_jump_2013_pct": 50.0, "redirect_status": "early_signs_only"},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="event_premium",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="China-Japan redirect expectation drove price before actual arrivals, occupancy, casino drop, ADR and FCF.",
    ),
    Round239CaseCandidate(
        case_id="r9_loop10_jeju_air_fatal_crash_hard_4c",
        symbol="089590",
        company_name="제주항공",
        primary_archetype=E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C,
        secondary_archetypes=(E2RArchetype.AIRLINE_TRAVEL_CYCLE,),
        case_type="4c_thesis_break",
        round_case_type="hard_4c_operational_safety_trust_break",
        stage1_date=date(2023, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 30),
        stage3_decision="fatal_crash_is_hard_4c_and_blocks_travel_demand_green",
        stage4b_status="hard_4c",
        hard_4c_confirmed=True,
        evidence_fields=("fatalities_179", "jeju_air_event_mae_15_7pct", "event_low_6920_krw", "market_cap_wipeout_95_7bn_krw", "booking_shock", "travel_agency_cancellation_shock"),
        red_flag_fields=("fatal_safety_accident", "operational_trust_break", "consumer_trust_shock", "booking_cancellation", "hard_4c_confirmed"),
        price_data_source="Reuters crash/price/travel-agency anchors",
        reported_price_anchor="Jeju Air -15.7% intraday to 6,920 KRW; market cap wipeout up to 95.7B KRW",
        reported_return_anchor="179 fatalities; package cancellations doubled and bookings halved for one operator",
        mfe_1d=None,
        mae_1d=-15.7,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=6920.0,
        extra_price_metrics={"jeju_air_event_mae_1d_pct": -15.7, "event_low_price_krw": 6920.0, "implied_pre_event_reference_price_krw": 8209.0, "market_cap_wipeout_krw_bn": 95.7, "fatalities": 179.0, "ak_holdings_mae_pct": -12.0, "korean_air_mae_pct": -1.3, "asiana_mae_pct": -0.8, "air_busan_mfe_pct": 15.0, "jin_air_initial_mfe_pct": 5.4, "tway_air_initial_mfe_pct": 7.3, "hanatour_mae_pct": -7.0, "very_good_tour_mae_pct": -11.0, "tour_package_cancellations": "doubled_for_one_operator", "bookings": "halved_for_one_operator"},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Fatal crash is hard 4C and blocks travel-demand Green.",
    ),
)


def round239_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND239_CASE_CANDIDATES:
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
                "Round239 R9 Loop-10 mobility/transport/leisure price-path "
                "validation case. Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "event" in field or "investment" in field or "route" in field or "tourism" in field or "capacity" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "op_forecast" in field
                or "contract" in field
                or "order" in field
                or "load_factor" in field
                or "yield" in field
                or "fcf" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "mfe" in field or "event" in field or "headline" in field or "premium" in field or "price" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "fatal" in field
                or "safety" in field
                or "quality" in field
                or "recall" in field
                or "trust" in field
                or "labor" in field
                or "booking" in field
            ),
            must_have_fields=ROUND239_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND239_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_capex_route_fleet_tourism_or_freight_headline_as_green_alone",
                *ROUND239_GREEN_REQUIRED_FIELDS,
                *ROUND239_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.stage2_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round239_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND239_CASE_CANDIDATES:
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
                "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
                "score_price_alignment": candidate.score_price_alignment,
                "round_score_price_alignment": candidate.round_score_price_alignment,
                "rerating_result": candidate.rerating_result,
                "stage_failure_type": candidate.stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round239_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND239_SCORE_ADJUSTMENTS)


def round239_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND239_SHADOW_WEIGHT_ROWS)


def round239_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round239_price_validation": "true"} for field in ROUND239_PRICE_VALIDATION_FIELDS)


def round239_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round239_label": label, "canonical_archetype": canonical} for label, canonical in ROUND239_REQUIRED_TARGET_ALIASES.items())


def round239_summary() -> dict[str, int | bool | str]:
    cases = ROUND239_CASE_CANDIDATES
    return {
        "source_round": ROUND239_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND239_ANALYST_ROUND_ID,
        "large_sector": ROUND239_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for case in cases if case.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "target_archetype_count": len(ROUND239_REQUIRED_TARGET_ALIASES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round239_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND239_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND239_ANALYST_ROUND_ID,
        "large_sector": ROUND239_LARGE_SECTOR.value,
        "summary": round239_summary(),
        "target_aliases": dict(ROUND239_REQUIRED_TARGET_ALIASES),
        "round_case_types": {case.case_id: case.round_case_type for case in ROUND239_CASE_CANDIDATES},
        "green_required_fields": list(ROUND239_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND239_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND239_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND239_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_use_round239_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_capex_route_fleet_tourism_or_freight_headline_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "keep_jeju_air_fatal_crash_as_hard_4c_reference_case",
        ],
    }


def render_round239_summary_markdown() -> str:
    summary = round239_summary()
    lines = [
        "# Round 239 R9 Loop 10 Mobility Transport Leisure Price Validation",
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
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND239_CASE_CANDIDATES:
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
            "- Hyundai/Kia future mobility is Stage 2 + 4B-watch, not automatic Green.",
            "- Hyundai Mobis and Jeju Air show why quality/safety trust gates matter in R9.",
            "- Rotem rail, T'way routes, and LCC consolidation are Stage 2 until delivery, yield, utilization, and FCF confirm.",
            "- Pan Ocean and tourism redirect rallies are cycle/event premium until freight floor or spend conversion confirms.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round239_green_gate_review_markdown() -> str:
    lines = [
        "# Round 239 R9 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND239_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND239_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `new Europe route allocation` is Stage 2.",
            "- `new Europe route allocation + load factor + yield + fuel/crew cost control + FCF` can support Stage 3 review.",
            "- `fatal crash + booking shock` is hard 4C, even if travel demand had been recovering.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round239_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 239 R9 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND239_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND239_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND239_CASE_CANDIDATES:
        if case.stage4b_status in {"watch", "hard_4c"} or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round239_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 239 R9 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: true",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND239_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round239_r9_loop10_reports(
    output_directory: str | Path = ROUND239_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND239_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND239_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)

    paths = {
        "cases": write_case_library(round239_case_records(), cases_path),
        "audit": _write_json(round239_audit_payload(), audit_path),
        "summary": output / "round239_r9_loop10_price_validation_summary.md",
        "case_matrix": output / "round239_r9_loop10_case_matrix.csv",
        "target_aliases": output / "round239_r9_loop10_target_aliases.csv",
        "score_adjustments": output / "round239_r9_loop10_score_adjustments.csv",
        "shadow_weights": output / "round239_r9_loop10_shadow_weights.csv",
        "price_validation_fields": output / "round239_r9_loop10_price_validation_fields.csv",
        "green_gate_review": output / "round239_r9_loop10_green_gate_review.md",
        "price_validation_plan": output / "round239_r9_loop10_price_validation_plan.md",
        "stage4b_4c_review": output / "round239_r9_loop10_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round239_summary_markdown(), encoding="utf-8")
    _write_csv(round239_case_rows(), paths["case_matrix"])
    _write_csv(round239_target_alias_rows(), paths["target_aliases"])
    _write_csv(round239_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round239_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round239_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round239_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round239_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round239_stage4b_4c_review_markdown(), encoding="utf-8")
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
