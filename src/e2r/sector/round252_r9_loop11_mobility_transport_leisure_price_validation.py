"""Round-252 R9 Loop-11 mobility/transport/leisure price validation pack.

This pack converts ``docs/round/round_252.md`` into calibration-only case
records, shadow weights, and guardrail reports. Production scoring is not
changed.

Easy example: a hybrid strategy day can move Hyundai Motor, but R9 Stage
3-Green waits for tariff-adjusted margin, logistics stability, and FCF.
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


ROUND252_SOURCE_ROUND_PATH = "docs/round/round_252.md"
ROUND252_ANALYST_ROUND_ID = "round_180"
ROUND252_LARGE_SECTOR = Round10LargeSector.MOBILITY_TRANSPORT_LEISURE.value
ROUND252_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round252_r9_loop11_mobility_transport_leisure_price_validation"
ROUND252_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r9_loop11_round252.jsonl"
ROUND252_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round252_r9_loop11_mobility_transport_leisure_price_validation_audit.json"

ROUND252_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "AUTO_HYBRID_SHAREHOLDER_RETURN": E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN.value,
    "AUTO_TARIFF_MARGIN_SHOCK": E2RArchetype.AUTO_TARIFF_MARGIN_SHOCK.value,
    "AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION": E2RArchetype.AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION.value,
    "AIRLINE_CONSOLIDATION_INTEGRATION": E2RArchetype.AIRLINE_CONSOLIDATION_INTEGRATION.value,
    "AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C": E2RArchetype.AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C.value,
    "AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C": E2RArchetype.AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C.value,
    "SHIPPING_FREIGHT_RATE_CYCLE": E2RArchetype.SHIPPING_FREIGHT_CYCLE.value,
    "TOURISM_REDIRECT_POLICY_EVENT": E2RArchetype.TOURISM_REDIRECT_POLICY_EVENT.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
    "CYCLICAL_SUCCESS": E2RArchetype.CYCLICAL_SUCCESS.value,
}

ROUND252_DEEP_SUB_ARCHETYPES: tuple[str, ...] = (
    "Hyundai Motor / Kia hybrid mix expansion",
    "EV slowdown response",
    "shareholder return / buyback",
    "U.S. tariff margin shock",
    "U.S. / Georgia localization",
    "Hyundai Glovis Middle East / Hormuz / Red Sea route disruption",
    "vehicle export logistics",
    "fuel cost / route diversion / port congestion",
    "Korean Air / Asiana consolidation",
    "Jin Air / Air Busan / Air Seoul integration",
    "Asiana cargo sale",
    "capacity / route optimization / antitrust remedy",
    "airline safety trust",
    "Kumho Tire factory fire",
    "Daejeon auto-parts supplier fire",
    "plant fire / production loss / customer supply disruption",
    "operational safety hard gate",
    "Pan Ocean dry bulk / LNG carrier addition",
    "Red Sea freight rate cycle",
    "freight normalization risk",
    "Lotte Tour / Yellow Balloon tourism redirect",
    "Jeju cruise reroute",
    "China visa-free group tourism",
    "arrivals vs spend / casino drop / hotel occupancy",
)

ROUND252_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "unit_economics_confirmed",
    "tariff_adjusted_margin_confirmed",
    "fcf_after_capex_confirmed",
    "route_yield_confirmed",
    "load_factor_confirmed",
    "fleet_utilization_confirmed",
    "logistics_cost_and_delivery_delay_controlled",
    "supply_chain_continuity_confirmed",
    "safety_quality_operational_trust_passed",
    "tourist_spend_occupancy_casino_drop_opm_confirmed",
    "price_path_after_evidence",
)

ROUND252_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "strategy_day_only",
    "shareholder_return_without_margin",
    "tariff_relief_headline_only",
    "fleet_count_without_yield",
    "merger_without_synergy",
    "tourism_policy_only",
    "freight_rate_spike_only",
    "factory_fire_or_supply_disruption",
    "workplace_fatality",
    "logistics_disruption",
)

ROUND252_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "strategy_day_shareholder_return_price_spike",
    "airline_consolidation_premium_before_synergy",
    "lcc_fleet_scale_before_yield",
    "tourism_policy_basket_rally_before_spend",
    "freight_rate_spike_before_rate_floor",
    "demand_narrative_ignores_logistics_cost",
)

ROUND252_HARD_4C_GATES: tuple[str, ...] = (
    "tariff_cost_causing_op_collapse",
    "factory_fire",
    "production_suspension",
    "fatal_workplace_accident",
    "airline_fatal_or_major_safety_accident",
    "supply_chain_disruption_to_key_customers",
    "logistics_route_closure",
    "fuel_cost_shock",
    "route_launch_failure",
    "merger_integration_failure",
    "tourist_spend_failure",
    "freight_rate_normalization_collapse",
)

ROUND252_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "tariff_or_margin_anchor",
    "logistics_or_supply_chain_anchor",
    "fleet_yield_load_factor_anchor",
    "safety_or_factory_risk_anchor",
    "tourism_spend_or_policy_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round252ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round252ShadowWeightRow:
    archetype: E2RArchetype
    unit_economics: int
    tariff_adjusted_margin: int
    hybrid_mix_profitability: int
    fcf_after_capex: int
    route_yield: int
    load_factor: int
    fleet_utilization: int
    logistics_cost_control: int
    supply_chain_continuity: int
    safety_trust: int
    tourist_spend: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "unit_economics": _signed(self.unit_economics),
            "tariff_adjusted_margin": _signed(self.tariff_adjusted_margin),
            "hybrid_mix_profitability": _signed(self.hybrid_mix_profitability),
            "fcf_after_capex": _signed(self.fcf_after_capex),
            "route_yield": _signed(self.route_yield),
            "load_factor": _signed(self.load_factor),
            "fleet_utilization": _signed(self.fleet_utilization),
            "logistics_cost_control": _signed(self.logistics_cost_control),
            "supply_chain_continuity": _signed(self.supply_chain_continuity),
            "safety_trust": _signed(self.safety_trust),
            "tourist_spend": _signed(self.tourist_spend),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round252CaseCandidate:
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


ROUND252_SCORE_ADJUSTMENTS: tuple[Round252ScoreAdjustment, ...] = (
    Round252ScoreAdjustment("unit_economics", 5, "raise", "R9는 판매량보다 단위경제성이 Stage 3 visibility다."),
    Round252ScoreAdjustment("tariff_adjusted_margin", 5, "raise", "자동차는 관세 이후 OPM이 지켜져야 한다."),
    Round252ScoreAdjustment("hybrid_mix_profitability", 4, "raise", "하이브리드 mix가 ASP·OPM으로 닫혀야 한다."),
    Round252ScoreAdjustment("fcf_after_capex", 5, "raise", "전략 투자와 자사주는 FCF로 유지돼야 한다."),
    Round252ScoreAdjustment("route_yield", 5, "raise", "항공은 fleet count보다 route yield가 중요하다."),
    Round252ScoreAdjustment("load_factor", 5, "raise", "통합 항공사는 load factor가 synergy 확인 축이다."),
    Round252ScoreAdjustment("fleet_utilization", 5, "raise", "차량·항공·해운 모두 utilization이 margin으로 연결된다."),
    Round252ScoreAdjustment("logistics_cost_control", 5, "raise", "중동 물류 차질은 수요가 좋아도 delivery와 비용을 깨뜨린다."),
    Round252ScoreAdjustment("supply_chain_continuity", 5, "raise", "공장 화재나 공급망 사고는 생산 continuity를 직접 훼손한다."),
    Round252ScoreAdjustment("safety_trust", 5, "raise", "항공·부품·타이어는 안전과 운영 신뢰가 hard gate다."),
    Round252ScoreAdjustment("tourist_spend_conversion", 5, "raise", "관광은 방문객 수보다 spend, occupancy, casino drop, OPM이 중요하다."),
    Round252ScoreAdjustment("strategy_day_only", -4, "lower", "전략 발표만으로 Stage 3-Green을 만들지 않는다."),
    Round252ScoreAdjustment("shareholder_return_without_margin", -4, "lower", "주주환원은 margin과 FCF가 없으면 Stage 2에 머문다."),
    Round252ScoreAdjustment("tariff_relief_headline_only", -5, "lower", "관세 완화 headline은 실제 margin 안정 전 event다."),
    Round252ScoreAdjustment("fleet_count_without_yield", -4, "lower", "fleet scale은 yield와 load factor가 없으면 Green 증거가 아니다."),
    Round252ScoreAdjustment("merger_without_synergy", -5, "lower", "항공 통합은 synergy, debt, service quality 확인 전 Green 금지다."),
    Round252ScoreAdjustment("tourism_policy_only", -5, "lower", "무비자·관광정책만으로 spend/OPM을 대체하지 않는다."),
    Round252ScoreAdjustment("freight_rate_spike_only", -5, "lower", "운임 급등은 rate floor와 FCF 전 cyclical이다."),
    Round252ScoreAdjustment("factory_fire_or_supply_disruption", -5, "lower", "공장 화재와 생산중단은 수요논리를 즉시 훼손한다."),
    Round252ScoreAdjustment("workplace_fatality", -5, "lower", "사망사고는 supply-chain safety hard gate다."),
    Round252ScoreAdjustment("logistics_disruption", -5, "lower", "route closure와 delivery delay는 R9 thesis-break watch다."),
)

ROUND252_SHADOW_WEIGHT_ROWS: tuple[Round252ShadowWeightRow, ...] = (
    Round252ShadowWeightRow(E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN, 5, 4, 5, 5, 0, 0, 0, 3, 3, 3, 0, -3, 4, 3, "Hyundai hybrid/shareholder return is Stage 2 until margin and FCF confirm."),
    Round252ShadowWeightRow(E2RArchetype.AUTO_TARIFF_MARGIN_SHOCK, 5, 5, 3, 5, 0, 0, 0, 2, 3, 3, 0, 0, 3, 5, "U.S. tariffs hit Kia OP and auto stock prices; strong 4C-watch."),
    Round252ShadowWeightRow(E2RArchetype.AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION, 4, 4, 2, 4, 0, 0, 0, 5, 5, 3, 0, 0, 4, 5, "Middle East logistics disruption directly hit Hyundai/Glovis relative returns."),
    Round252ShadowWeightRow(E2RArchetype.AIRLINE_CONSOLIDATION_INTEGRATION, 5, 3, 0, 5, 5, 5, 5, 3, 3, 5, 0, -4, 5, 4, "Korean Air/Asiana needs yield/load factor/synergy and safety quality before Green."),
    Round252ShadowWeightRow(E2RArchetype.AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 3, 5, "Kumho Tire factory fire is direct-listed hard 4C."),
    Round252ShadowWeightRow(E2RArchetype.AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 3, 5, "Daejeon supplier fire is sector hard 4C for Hyundai/Kia supplier network."),
    Round252ShadowWeightRow(E2RArchetype.SHIPPING_FREIGHT_CYCLE, 4, 0, 0, 5, 0, 0, 4, 4, 3, 2, 0, -5, 5, 4, "Pan Ocean freight-cycle benefit needs rate floor/contract coverage/FCF."),
    Round252ShadowWeightRow(E2RArchetype.TOURISM_REDIRECT_POLICY_EVENT, 3, 0, 0, 4, 0, 0, 3, 2, 2, 3, 5, -5, 5, 4, "Tourism policy/redirect rally is event premium until spend/OPM confirm."),
)

ROUND252_CASE_CANDIDATES: tuple[Round252CaseCandidate, ...] = (
    Round252CaseCandidate(
        case_id="r9_loop11_hyundai_hybrid_shareholder_return",
        symbol="005380",
        company_name="Hyundai Motor",
        primary_archetype=E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN,
        secondary_archetypes=(E2RArchetype.AUTO_HYBRID_VALUEUP, E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN),
        case_type="success_candidate",
        round_case_type="success_candidate_hybrid_shareholder_return_stage2",
        stage1_date=date(2024, 8, 28),
        stage2_date=date(2024, 8, 28),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stage2_not_green_until_hybrid_mix_tariff_adjusted_margin_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("hybrid_mix_expansion", "buyback_program_4tn_krw", "quarterly_dividend_floor_2500_krw", "profit_return_policy_35pct", "global_sales_target_5_55m"),
        red_flag_fields=("tariff_adjusted_margin_unverified", "fcf_after_capex_unverified", "north_america_margin_unverified", "logistics_risk_watch"),
        price_data_source="Reuters investor-day / event-return anchor",
        reported_price_anchor="shares intraday +5.0%, close +4.7%",
        reported_return_anchor="buyback up to 4T won over 2025-2027 and hybrid sales target 1.33M by 2028",
        mfe_1d=5.0,
        mae_1d=None,
        event_close_return=4.7,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_mfe_1d_pct": 5.0, "event_close_return_pct": 4.7, "buyback_program_krw_trn": 4.0, "quarterly_dividend_floor_krw": 2500.0, "profit_return_policy_pct": 35.0, "global_sales_target_2030_mn": 5.55, "target_growth_vs_2023_pct": 30.0, "hybrid_sales_target_2028_mn": 1.33, "ev_sales_target_2030_mn": 2.0},
        round_score_price_alignment="success_candidate",
        score_price_alignment="unknown",
        round_rerating_result="hybrid_shareholder_return_watch",
        rerating_result="unknown",
        round_stage_failure_type="stage2_strategy_not_green",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Strong Stage 2; hybrid mix, tariff-adjusted margin and FCF required before Green.",
    ),
    Round252CaseCandidate(
        case_id="r9_loop11_hyundai_kia_us_tariff_margin_shock",
        symbol="005380/000270",
        company_name="Hyundai Motor / Kia",
        primary_archetype=E2RArchetype.AUTO_TARIFF_MARGIN_SHOCK,
        secondary_archetypes=(E2RArchetype.AUTO_TARIFF_LOCALIZATION, E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE),
        case_type="failed_rerating",
        round_case_type="4c_watch_us_tariff_margin_shock",
        stage1_date=date(2025, 3, 27),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 3, 27),
        stage3_decision="tariff_cost_hits_margin_so_green_blocked_until_tariff_adjusted_margin_stabilizes",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("us_auto_tariff_25pct", "us_auto_exports_34_7bn_usd", "us_share_of_korea_auto_exports_49pct", "kia_q2_tariff_hit_786bn_krw", "kia_op_decline_24pct"),
        red_flag_fields=("tariff_cost_causing_op_decline", "trade_deal_still_hit_share_prices", "export_margin_shock", "localization_unverified"),
        price_data_source="Reuters tariff / earnings / trade-deal anchors",
        reported_price_anchor="Hyundai > -4%, Kia > -3%; later Hyundai -4.5%, Kia -6.6%",
        reported_return_anchor="Kia Q2 2025 tariff hit 786B won / $570M and OP declined 24% YoY",
        mfe_1d=None,
        mae_1d=-6.6,
        event_close_return=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hyundai_mar27_mae_pct": -4.0, "kia_mar27_mae_pct": -3.0, "us_auto_exports_2024_usd_bn": 34.7, "us_share_of_korea_auto_exports_pct": 49.0, "kia_q2_2025_tariff_hit_krw_bn": 786.0, "kia_q2_2025_tariff_hit_usd_mn": 570.0, "kia_q2_2025_op_krw_trn": 2.76, "kia_q2_op_decline_pct": -24.0, "kia_earnings_event_mae_pct": -1.7, "trade_deal_tariff_pct": 15.0, "hyundai_trade_deal_mae_pct": -4.5, "kia_trade_deal_mae_pct": -6.6},
        round_score_price_alignment="thesis_break_watch",
        score_price_alignment="false_positive_score",
        round_rerating_result="auto_tariff_margin_shock",
        rerating_result="thesis_break",
        round_stage_failure_type="4C_watch_not_hard_4C",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Tariff cost directly hit OP and stock reaction; 4C-watch until tariff-adjusted margins stabilize.",
    ),
    Round252CaseCandidate(
        case_id="r9_loop11_hyundai_glovis_middle_east_logistics_disruption",
        symbol="005380/086280",
        company_name="Hyundai Motor / Hyundai Glovis",
        primary_archetype=E2RArchetype.AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION,
        secondary_archetypes=(E2RArchetype.LOGISTICS_PARCEL_FREIGHT, E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE),
        case_type="failed_rerating",
        round_case_type="4c_watch_middle_east_logistics_disruption",
        stage1_date=date(2026, 3, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 4, 3),
        stage3_decision="logistics_route_disruption_blocks_green_until_cost_and_delivery_stability_recover",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("middle_east_route_disruption", "hyundai_exports_to_europe_north_africa_disrupted", "glovis_route_access_limited", "middle_east_shipments_decline_49pct"),
        red_flag_fields=("logistics_disruption", "delivery_delay_risk", "fuel_cost_risk", "route_diversion"),
        price_data_source="Reuters logistics-disruption / event-return anchor",
        reported_price_anchor="Hyundai -1.2%, Glovis -0.7% vs KOSPI +2.7%",
        reported_return_anchor="Middle East shipments -49%, some shipments diverted to Sri Lanka",
        mfe_1d=None,
        mae_1d=-1.2,
        event_close_return=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hyundai_event_mae_pct": -1.2, "glovis_event_mae_pct": -0.7, "kospi_same_context_pct": 2.7, "hyundai_relative_underperformance_pp": -3.9, "glovis_relative_underperformance_pp": -3.4, "hyundai_march_global_sales": 358759.0, "hyundai_march_sales_decline_pct": -2.3, "domestic_sales_decline_pct": -2.0, "overseas_sales_decline_pct": -2.4, "middle_east_shipments_decline_pct": -49.0, "route_disruption": "Europe/North Africa via Middle East", "temporary_hub": "Sri Lanka mentioned as diverted intermediate hub"},
        round_score_price_alignment="thesis_break_watch",
        score_price_alignment="false_positive_score",
        round_rerating_result="auto_export_logistics_disruption_watch",
        rerating_result="thesis_break",
        round_stage_failure_type="geopolitical_logistics_4C_watch",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Middle East logistics disruption hit auto export chain; Green requires logistics cost and delivery stability.",
    ),
    Round252CaseCandidate(
        case_id="r9_loop11_korean_air_asiana_consolidation",
        symbol="003490/020560/272450/298690",
        company_name="Korean Air / Asiana / Jin Air / Air Busan",
        primary_archetype=E2RArchetype.AIRLINE_CONSOLIDATION_INTEGRATION,
        secondary_archetypes=(E2RArchetype.AIRLINE_INTEGRATION_SCALE, E2RArchetype.LCC_CONSOLIDATION_INTEGRATION),
        case_type="success_candidate",
        round_case_type="success_candidate_airline_consolidation_stage2",
        stage1_date=date(2020, 1, 1),
        stage2_date=date(2024, 12, 12),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stage2_merger_not_green_until_yield_load_factor_cost_synergy_debt_and_safety_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("asiana_stake_63_88pct_acquired", "deal_value_1_3bn_usd", "international_capacity_rank_12", "combined_lcc_58_aircraft"),
        red_flag_fields=("yield_unverified", "load_factor_unverified", "cost_synergy_unverified", "debt_refinancing_unverified", "safety_service_quality_watch"),
        price_data_source="Reuters merger / fleet / integration anchors",
        reported_price_anchor="full OHLC unavailable after deep search",
        reported_return_anchor="Korean Air acquired 63.88% Asiana stake for about $1.3B; combined LCC fleet around 58 aircraft",
        mfe_1d=None,
        mae_1d=None,
        event_close_return=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"deal_value_usd_bn": 1.3, "korean_air_asiana_stake_pct": 63.88, "integration_timeline_years": 2.0, "international_capacity_rank": 12.0, "combined_lcc_aircraft": 58.0, "jeju_air_aircraft": 42.0, "tway_aircraft": 39.0, "combined_lcc_aircraft_advantage_vs_jeju_pct": 38.1, "combined_lcc_aircraft_advantage_vs_tway_pct": 48.7, "combined_lcc_capacity_share_nov_2024_pct": 8.0},
        round_score_price_alignment="success_candidate",
        score_price_alignment="unknown",
        round_rerating_result="airline_consolidation_integration_watch",
        rerating_result="unknown",
        round_stage_failure_type="stage2_merger_not_green",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Airline merger is Stage 2; load factor, yield, cost synergy, debt and safety/service quality required before Green.",
    ),
    Round252CaseCandidate(
        case_id="r9_loop11_kumho_tire_gwangju_factory_fire_hard_4c",
        symbol="073240",
        company_name="Kumho Tire",
        primary_archetype=E2RArchetype.AUTO_SUPPLIER_FACTORY_FIRE_HARD_4C,
        secondary_archetypes=(E2RArchetype.TIRE_AUTO_COMPONENT_SPREAD, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        round_case_type="hard_4c_factory_fire_supply_disruption",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 5, 17),
        stage3_decision="factory_fire_suspended_nearly_20pct_global_capacity_so_demand_thesis_breaks",
        stage4b_status="none",
        hard_4c_confirmed=True,
        evidence_fields=("gwangju_factory_fire", "production_suspended", "annual_capacity_12m_tires", "nearly_20pct_global_capacity", "revenue_target_at_risk"),
        red_flag_fields=("factory_fire", "production_suspension", "supply_chain_disruption_to_key_customers", "revenue_target_cut_risk", "workplace_injuries"),
        price_data_source="Reuters fire / production / event-return anchors",
        reported_price_anchor="shares -8%",
        reported_return_anchor="Gwangju plant 12M tires/year and nearly 20% of global capacity; production suspended",
        mfe_1d=None,
        mae_1d=-8.0,
        event_close_return=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_mae_pct": -8.0, "annual_capacity_mn_tires": 12.0, "share_of_global_capacity_pct": 20.0, "production_status": "suspended", "fire_extinguished_pct": "90-95 by May 19 report", "revenue_target_before_fire": "increase 10pct to 5T won", "customers": "Hyundai Motor|Volkswagen Group|Mercedes-Benz", "initial_injuries": "1 employee and 2 firefighters"},
        round_score_price_alignment="thesis_break",
        score_price_alignment="false_positive_score",
        round_rerating_result="tire_factory_supply_disruption",
        rerating_result="thesis_break",
        round_stage_failure_type="hard_4C",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Factory fire suspended nearly 20% of global capacity; direct-listed hard 4C.",
    ),
    Round252CaseCandidate(
        case_id="r9_loop11_daejeon_auto_parts_supplier_fire_sector_hard_4c",
        symbol="005380/000270_supply_chain_exposure",
        company_name="Anjun Industrial / Hyundai-Kia supplier network",
        primary_archetype=E2RArchetype.AUTO_PARTS_WORKPLACE_SAFETY_HARD_4C,
        secondary_archetypes=(E2RArchetype.TRANSPORT_SAFETY_REGULATORY_OVERLAY, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        round_case_type="sector_hard_4c_workplace_safety_supply_chain_risk",
        stage1_date=date(2026, 3, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 3, 20),
        stage3_decision="fatal_supplier_fire_blocks_green_for_affected_supply_chain_until_safety_and_continuity_are_verified",
        stage4b_status="none",
        hard_4c_confirmed=True,
        evidence_fields=("daejeon_auto_parts_factory_fire", "14_deaths", "60_injuries", "engine_valve_supplier", "hyundai_kia_supplier_network"),
        red_flag_fields=("fatal_workplace_accident", "supplier_production_interruption", "customer_supply_chain_risk", "direct_listed_mapping_unavailable"),
        price_data_source="Reuters workplace-safety / supplier anchor",
        reported_price_anchor="direct listed ticker not available",
        reported_return_anchor="14 deaths, 60 injuries, 25 serious injuries; Anjun supplies Hyundai/Kia",
        mfe_1d=None,
        mae_1d=None,
        event_close_return=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fatalities": 14.0, "injuries": 60.0, "serious_injuries": 25.0, "minor_injuries": 35.0, "owner": "Anjun Industrial", "product": "engine valves", "listed_exposure": "Hyundai Motor / Kia supplier network"},
        round_score_price_alignment="thesis_break",
        score_price_alignment="false_positive_score",
        round_rerating_result="auto_parts_workplace_safety_break",
        rerating_result="thesis_break",
        round_stage_failure_type="sector_hard_4C_direct_listed_mapping_unavailable",
        stage_failure_type="should_have_been_red",
        price_validation_status="sector_hard_4c_direct_listed_mapping_unavailable",
        notes="Unlisted supplier, but Hyundai/Kia supply-chain safety hard gate.",
    ),
    Round252CaseCandidate(
        case_id="r9_loop11_pan_ocean_shipping_freight_cycle",
        symbol="028670",
        company_name="Pan Ocean",
        primary_archetype=E2RArchetype.SHIPPING_FREIGHT_CYCLE,
        secondary_archetypes=(E2RArchetype.SHIPPING_DRY_BULK_CYCLE, E2RArchetype.CYCLICAL_SUCCESS),
        case_type="cyclical_success",
        round_case_type="cyclical_success_freight_normalization_watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 5, 1),
        stage3_date=None,
        stage4b_date=date(2025, 1, 1),
        stage4c_date=None,
        stage3_decision="stage2_cycle_not_green_until_rate_floor_contract_coverage_fcf_and_deleveraging_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("op_forecast_2024_536bn_krw", "op_growth_forecast_39pct", "target_price_raise_to_6700_krw", "lng_carrier_additions", "red_sea_freight_cycle"),
        red_flag_fields=("freight_rate_spike_only", "red_sea_route_normalization_risk", "freight_rate_downside_20_25pct", "overcapacity_risk"),
        price_data_source="WSJ Market Talk / Reuters freight-cycle anchors",
        reported_price_anchor="Pan Ocean 4,615 won, -0.2%",
        reported_return_anchor="target upside +45.2%, OP forecast +39%, but rate normalization can cut freight rates 20-25%",
        mfe_1d=None,
        mae_1d=-0.2,
        event_close_return=None,
        stage2_price_anchor=4615.0,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_price_krw": 4615.0, "event_mae_pct": -0.2, "target_price_krw": 6700.0, "target_price_before_krw": 6500.0, "target_raise_pct": 3.1, "target_upside_from_event_price_pct": 45.2, "op_forecast_2024_krw_bn": 536.0, "op_growth_forecast_pct": 39.0, "implied_prior_op_krw_bn": 385.6, "freight_rate_downside_if_red_sea_normalizes_pct": "20-25"},
        round_score_price_alignment="cyclical_success",
        score_price_alignment="unknown",
        round_rerating_result="shipping_freight_cycle_watch",
        rerating_result="cyclical_rerating",
        round_stage_failure_type="stage2_cycle_not_green",
        stage_failure_type="yellow_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Freight-cycle benefit is Stage 2/cyclical; rate floor, contract coverage, FCF and deleveraging required before Green.",
    ),
    Round252CaseCandidate(
        case_id="r9_loop11_lotte_tour_yellow_balloon_tourism_redirect",
        symbol="032350/104620/004170/tourism_basket",
        company_name="Lotte Tour / Yellow Balloon / Shinsegae / tourism basket",
        primary_archetype=E2RArchetype.TOURISM_REDIRECT_POLICY_EVENT,
        secondary_archetypes=(E2RArchetype.TOURISM_REDIRECT_EVENT_PREMIUM, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_tourism_redirect_policy_watch",
        stage1_date=date(2025, 8, 6),
        stage2_date=date(2025, 9, 29),
        stage3_date=None,
        stage4b_date=date(2025, 11, 21),
        stage4c_date=None,
        stage3_decision="stage2_event_not_green_until_spend_occupancy_casino_drop_hold_and_opm_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("china_group_tourist_visa_free_policy", "china_japan_cruise_reroute", "lotte_tour_above_20pct", "yellow_balloon_24pct", "jeju_stay_extended"),
        red_flag_fields=("tourism_policy_only", "tourist_spend_unverified", "hotel_occupancy_unverified", "casino_drop_unverified", "policy_fade_risk"),
        price_data_source="Reuters tourism policy / redirect event anchors",
        reported_price_anchor="Lotte Tour > +20%, Yellow Balloon +24%, Shinsegae +6%",
        reported_return_anchor="China visa-free group tourism and cruise reroute drove basket rally before spend/OPM proof",
        mfe_1d=24.0,
        mae_1d=None,
        event_close_return=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hyundai_department_event_mfe_pct": 7.1, "hotel_shilla_event_mfe_pct": 4.8, "paradise_event_mfe_pct": 2.9, "hankook_cosmetics_event_mfe_pct": 9.9, "visa_free_period": "2025-09-29_to_2026-06", "visa_free_stay_days": 15.0, "group_condition": "3+ Chinese tourists", "lotte_tour_redirect_mfe_pct": 20.0, "yellow_balloon_redirect_mfe_pct": 24.0, "shinsegae_redirect_mfe_pct": 6.0, "usual_jeju_schedule_hours": 9.0, "new_jeju_schedule_hours": "31-57"},
        round_score_price_alignment="event_premium",
        score_price_alignment="price_moved_without_evidence",
        round_rerating_result="tourism_redirect_policy_watch",
        rerating_result="event_premium",
        round_stage_failure_type="stage2_event_not_green",
        stage_failure_type="false_yellow",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Tourism policy/redirect event is Stage 2 and 4B; spend, occupancy, casino drop/hold and OPM required before Green.",
    ),
)


def round252_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND252_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND252_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round252 R9 Loop-11 mobility/transport/leisure price validation case. Calibration-only; not production scoring input.",
            stage1_evidence=tuple(field for field in candidate.evidence_fields if "policy" in field or "strategy" in field or "hybrid" in field or "route" in field or "fire" in field),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if "margin" in field or "fcf" in field or "yield" in field or "load_factor" in field or "spend" in field),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "price" in field or "rally" in field or "premium" in field or "spike" in field or "policy" in field or "freight" in field),
            stage4c_evidence=tuple(field for field in candidate.red_flag_fields if "tariff" in field or "fire" in field or "fatal" in field or "disruption" in field or "safety" in field or "suspension" in field or "margin" in field),
            must_have_fields=ROUND252_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=("; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "failed_rerating", "4c_thesis_break"} else None),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND252_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_mfe_mae_margin_fcf_yield_load_factor_or_spend",
                "do_not_treat_strategy_day_shareholder_return_merger_tourism_policy_or_freight_spike_as_green",
                f"round_case_type={candidate.round_case_type}",
                f"round_score_price_alignment={candidate.round_score_price_alignment}",
                f"round_rerating_result={candidate.round_rerating_result}",
                f"round_stage_failure_type={candidate.round_stage_failure_type}",
                *ROUND252_GREEN_REQUIRED_FIELDS,
                *ROUND252_GREEN_FORBIDDEN_PATTERNS,
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
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round252_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND252_CASE_CANDIDATES:
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


def round252_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND252_SCORE_ADJUSTMENTS)


def round252_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND252_SHADOW_WEIGHT_ROWS)


def round252_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round252_price_validation": "true"} for field in ROUND252_PRICE_VALIDATION_FIELDS)


def round252_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round252_label": label, "canonical_archetype": canonical} for label, canonical in ROUND252_REQUIRED_TARGET_ALIASES.items())


def round252_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple({"deep_sub_archetype": item, "large_sector": ROUND252_LARGE_SECTOR} for item in ROUND252_DEEP_SUB_ARCHETYPES)


def round252_summary() -> dict[str, int | bool | str]:
    cases = ROUND252_CASE_CANDIDATES
    return {
        "source_round": ROUND252_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND252_ANALYST_ROUND_ID,
        "large_sector": ROUND252_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "cyclical_success_count": sum(1 for case in cases if case.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "thesis_break_watch_count": sum(1 for case in cases if case.round_score_price_alignment == "thesis_break_watch"),
        "target_archetype_count": len(ROUND252_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND252_DEEP_SUB_ARCHETYPES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round252_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND252_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND252_ANALYST_ROUND_ID,
        "large_sector": ROUND252_LARGE_SECTOR,
        "summary": round252_summary(),
        "target_aliases": dict(ROUND252_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetypes": list(ROUND252_DEEP_SUB_ARCHETYPES),
        "green_required_fields": list(ROUND252_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND252_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND252_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND252_HARD_4C_GATES),
        "case_ids": [case.case_id for case in ROUND252_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_use_round252_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_strategy_day_shareholder_return_merger_tourism_policy_or_freight_spike_as_green",
            "do_not_ignore_tariff_logistics_factory_fire_workplace_safety_or_airline_safety_hard_gates",
            "do_not_invent_ohlc_stage_prices_mfe_mae_margin_fcf_yield_load_factor_or_spend",
        ],
    }


def render_round252_summary_markdown() -> str:
    summary = round252_summary()
    lines = [
        "# Round 252 R9 Loop 11 Mobility Transport Leisure Price Validation",
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
        f"- failed_rerating: {summary['failed_rerating_count']}",
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
    for case in ROUND252_CASE_CANDIDATES:
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
            "- Hyundai Motor is Stage 2; hybrid mix, tariff-adjusted margin and FCF are required before Green.",
            "- Hyundai/Kia tariff shock is 4C-watch because tariff cost reached OP and share-price anchors.",
            "- Hyundai/Glovis logistics disruption is 4C-watch because route closure can break delivery and cost.",
            "- Korean Air/Asiana consolidation is Stage 2; yield, load factor, synergy, debt and safety decide promotion.",
            "- Kumho Tire factory fire is hard 4C because production capacity and revenue target were directly impaired.",
            "- Daejeon supplier fire is sector hard 4C for Hyundai/Kia supply-chain safety.",
            "- Pan Ocean is cyclical_success, not structural Green before rate floor, FCF and deleveraging.",
            "- Tourism redirect is event premium before spend, occupancy, casino drop/hold and OPM.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round252_green_gate_review_markdown() -> str:
    lines = [
        "# Round 252 R9 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND252_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND252_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND252_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Shareholder return` is not Green until tariff-adjusted margin and FCF appear.",
            "- `Airline merger` is not enough without route yield, load factor and cost synergy.",
            "- `Tourism visa-free policy` is event premium until spend, occupancy, casino drop and OPM confirm.",
            "- `Factory fire with production suspension` is hard 4C because supply continuity is broken.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round252_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 252 R9 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND252_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND252_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | 4C date | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND252_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.stage4b_status} | {_date_text(case.stage4c_date)} | "
            f"{str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round252_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 252 R9 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- hard_4c_confirmed: true",
        "- Do not invent OHLC, peak, MFE, MAE, stage prices, margin, FCF, yield, load factor, tourist spend, or safety costs.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND252_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND252_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def render_round252_deep_sub_archetypes_markdown() -> str:
    lines = [
        "# Round 252 R9 Deep Sub-Archetypes",
        "",
        "These labels describe research coverage. They are not production scoring inputs.",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND252_DEEP_SUB_ARCHETYPES)
    return "\n".join(lines) + "\n"


def write_round252_r9_loop11_reports(
    output_directory: str | Path = ROUND252_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND252_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND252_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round252_case_records(), cases_path),
        "audit": _write_json(round252_audit_payload(), audit_path),
        "summary": output / "round252_r9_loop11_price_validation_summary.md",
        "case_matrix": output / "round252_r9_loop11_case_matrix.csv",
        "target_aliases": output / "round252_r9_loop11_target_aliases.csv",
        "deep_sub_archetypes": output / "round252_r9_loop11_deep_sub_archetypes.csv",
        "score_adjustments": output / "round252_r9_loop11_score_adjustments.csv",
        "shadow_weights": output / "round252_r9_loop11_shadow_weights.csv",
        "price_validation_fields": output / "round252_r9_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round252_r9_loop11_green_gate_review.md",
        "price_validation_plan": output / "round252_r9_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round252_r9_loop11_stage4b_4c_review.md",
        "deep_sub_archetype_review": output / "round252_r9_loop11_deep_sub_archetypes.md",
    }
    paths["summary"].write_text(render_round252_summary_markdown(), encoding="utf-8")
    _write_csv(round252_case_rows(), paths["case_matrix"])
    _write_csv(round252_target_alias_rows(), paths["target_aliases"])
    _write_csv(round252_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round252_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round252_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round252_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round252_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round252_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round252_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["deep_sub_archetype_review"].write_text(render_round252_deep_sub_archetypes_markdown(), encoding="utf-8")
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
