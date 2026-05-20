"""Round-291 R9 Loop-14 mobility/transport/leisure validation pack.

This module converts ``docs/round/round_291.md`` into calibration-only case
records and reports. It does not change production scoring, candidate
generation, or StageClassifier thresholds.

Easy example: a visa-free tourism headline can move hotel/casino stocks. It is
not Stage 3-Green until spend-per-head, hotel ADR/occupancy, casino drop, and
margin are visible.
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


ROUND291_SOURCE_ROUND_PATH = "docs/round/round_291.md"
ROUND291_ANALYST_ROUND_ID = "round_219"
ROUND291_LARGE_SECTOR = Round10LargeSector.MOBILITY_TRANSPORT_LEISURE.value
ROUND291_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round291_r9_loop14_mobility_transport_leisure_price_validation"
ROUND291_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r9_loop14_round291.jsonl"
ROUND291_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round291_r9_loop14_mobility_transport_leisure_price_validation_audit.json"

ROUND291_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "AUTO_TARIFF_HYBRID_MIX_STAGE2": E2RArchetype.AUTO_TARIFF_HYBRID_MIX_STAGE2.value,
    "AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH": E2RArchetype.AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH.value,
    "AIRLINE_CONSOLIDATION_STAGE2": E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2.value,
    "AIRLINE_REMEDY_ROUTE_CARGO_STAGE2": E2RArchetype.AIRLINE_REMEDY_ROUTE_CARGO_STAGE2.value,
    "AVIATION_SAFETY_HARD_4C": E2RArchetype.AVIATION_SAFETY_HARD_4C.value,
    "OVERSEAS_AUTO_IPO_FAILED_RERATING": E2RArchetype.OVERSEAS_AUTO_IPO_FAILED_RERATING.value,
    "CHINA_TOURISM_LEISURE_EVENT_PREMIUM": E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM.value,
    "CONTAINER_SHIPPING_RATE_EVENT_PREMIUM": E2RArchetype.CONTAINER_SHIPPING_RATE_EVENT_PREMIUM.value,
    "USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE": E2RArchetype.USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE.value,
}

ROUND291_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "tariff_pass_through_confirmed",
    "hybrid_mix_margin_confirmed",
    "local_production_hedge_confirmed",
    "route_security_continuity_confirmed",
    "logistics_cost_control_confirmed",
    "load_factor_yield_confirmed",
    "aviation_safety_trust_confirmed",
    "integration_synergy_execution_confirmed",
    "tourist_spend_per_head_confirmed",
    "freight_rate_durability_confirmed",
    "price_path_after_evidence",
)

ROUND291_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "tariff_relief_headline_only",
    "visitor_count_only",
    "merger_completion_only",
    "route_rights_without_load_factor",
    "cargo_asset_purchase_without_customer_retention",
    "freight_spot_rate_only",
    "overseas_IPO_size_only",
    "EV_or_hybrid_mix_without_margin",
    "safety_risk_unresolved",
)

ROUND291_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "tariff_relief_headline_auto_rally",
    "china_tourism_visa_free_basket_rally",
    "freight_spot_rate_spike",
    "airline_merger_completion_before_synergy",
    "route_cargo_remedy_before_margin",
    "overseas_subsidiary_IPO_valuation_parent_rerating",
)

ROUND291_HARD_4C_GATES: tuple[str, ...] = (
    "fatal_aviation_safety_event",
    "route_disruption_blocks_high_margin_exports",
    "tariff_shock_not_passed_through",
    "major_fuel_cost_spike_without_surcharge_recovery",
    "airline_integration_failure_or_safety_inspection_escalation",
    "tourism_arrivals_without_spend_conversion",
    "freight_rate_normalization_after_spot_rally",
    "overseas_IPO_weak_debut_plus_weak_first_earnings",
)

ROUND291_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "reported_event_price_anchor",
    "operating_profit_anchor",
    "tariff_cost_anchor",
    "deal_value_anchor",
    "passenger_freight_capacity_anchor",
    "visitor_data_anchor",
    "market_cap_wipeout_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round291ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round291ShadowWeightRow:
    archetype: E2RArchetype
    tariff_pass_through: int
    hybrid_mix_margin: int
    local_production_hedge: int
    route_security_continuity: int
    logistics_cost_control: int
    load_factor_yield: int
    aviation_safety_trust: int
    integration_synergy_execution: int
    tourist_spend_per_head: int
    freight_rate_durability: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "tariff_pass_through": _signed(self.tariff_pass_through),
            "hybrid_mix_margin": _signed(self.hybrid_mix_margin),
            "local_production_hedge": _signed(self.local_production_hedge),
            "route_security_continuity": _signed(self.route_security_continuity),
            "logistics_cost_control": _signed(self.logistics_cost_control),
            "load_factor_yield": _signed(self.load_factor_yield),
            "aviation_safety_trust": _signed(self.aviation_safety_trust),
            "integration_synergy_execution": _signed(self.integration_synergy_execution),
            "tourist_spend_per_head": _signed(self.tourist_spend_per_head),
            "freight_rate_durability": _signed(self.freight_rate_durability),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round291DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round291CaseCandidate:
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
    reported_event_return_anchor: str
    reported_event_price_anchor: str
    event_mfe_pct: float | None
    event_mae_pct: float | None
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, object]
    score_price_alignment: str
    round_alignment_label: str
    rerating_result: str
    round_rerating_label: str
    stage_failure_type: str
    round_stage_failure_label: str
    price_validation_status: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND291_SCORE_ADJUSTMENTS: tuple[Round291ScoreAdjustment, ...] = (
    Round291ScoreAdjustment("tariff_pass_through", 5, "raise", "관세 relief가 아니라 가격전가와 margin 회복이 핵심이다."),
    Round291ScoreAdjustment("hybrid_mix_margin", 5, "raise", "hybrid/high-margin mix가 OP margin으로 닫혀야 한다."),
    Round291ScoreAdjustment("local_production_hedge", 5, "raise", "현지생산 hedge가 관세와 물류비를 줄이는지 봐야 한다."),
    Round291ScoreAdjustment("route_security_continuity", 5, "raise", "자동차·해운은 항로 안정성이 margin의 하부 구조다."),
    Round291ScoreAdjustment("logistics_cost_control", 5, "raise", "rerouting과 보관비가 OP를 훼손하지 않아야 한다."),
    Round291ScoreAdjustment("load_factor_yield", 5, "raise", "항공은 탑승률보다 yield와 비용을 같이 봐야 한다."),
    Round291ScoreAdjustment("aviation_safety_trust", 5, "raise", "항공 안전 신뢰는 hard gate다."),
    Round291ScoreAdjustment("integration_synergy_execution", 5, "raise", "항공 통합은 완료보다 synergy 실행이 중요하다."),
    Round291ScoreAdjustment("tourist_spend_per_head", 5, "raise", "관광객 수는 객단가와 margin으로 검증해야 한다."),
    Round291ScoreAdjustment("freight_rate_durability", 5, "raise", "spot 운임보다 contract-rate durability가 중요하다."),
    Round291ScoreAdjustment("tariff_relief_headline_only", -5, "lower", "관세 인하 headline만으로 margin 회복을 만들지 않는다."),
    Round291ScoreAdjustment("visitor_count_only", -5, "lower", "입국자 수만으로 소비·마진을 만들지 않는다."),
    Round291ScoreAdjustment("merger_completion_only", -5, "lower", "합병 완료는 synergy와 yield 전에는 Stage 2다."),
    Round291ScoreAdjustment("route_rights_without_load_factor", -5, "lower", "노선권만으로 항공 수익성을 만들지 않는다."),
    Round291ScoreAdjustment("cargo_asset_purchase_without_customer_retention", -5, "lower", "화물 자산 인수는 고객 유지와 utilization이 필요하다."),
    Round291ScoreAdjustment("freight_spot_rate_only", -5, "lower", "spot 운임 spike는 cycle일 수 있다."),
    Round291ScoreAdjustment("overseas_IPO_size_only", -5, "lower", "해외 IPO 규모만으로 parent rerating을 만들지 않는다."),
    Round291ScoreAdjustment("EV_or_hybrid_mix_without_margin", -4, "lower", "EV/hybrid mix는 margin 확인 전에는 부족하다."),
    Round291ScoreAdjustment("safety_risk_unresolved", -5, "lower", "안전 리스크 미해소는 Green을 막는다."),
)


ROUND291_SHADOW_WEIGHT_ROWS: tuple[Round291ShadowWeightRow, ...] = (
    Round291ShadowWeightRow(E2RArchetype.AUTO_TARIFF_HYBRID_MIX_STAGE2, 5, 5, 5, 2, 3, 0, 1, 1, 0, 0, -5, 4, 4, "Hyundai/Kia tariff case needs pass-through and hybrid/high-margin mix proof."),
    Round291ShadowWeightRow(E2RArchetype.AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH, 3, 3, 3, 5, 5, 0, 1, 1, 0, 2, 0, 4, 5, "Hyundai/Glovis shows route disruption and logistics cost are mobility hard gates."),
    Round291ShadowWeightRow(E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2, 1, 0, 0, 3, 4, 5, 5, 5, 1, 1, -5, 4, 4, "Korean Air/Asiana needs yield, load factor, LCC consolidation and integration cost proof."),
    Round291ShadowWeightRow(E2RArchetype.AIRLINE_REMEDY_ROUTE_CARGO_STAGE2, 1, 0, 0, 3, 4, 5, 5, 4, 1, 2, -5, 5, 4, "T'way/Air Incheon route/cargo remedy needs aircraft utilization and customer retention."),
    Round291ShadowWeightRow(E2RArchetype.AVIATION_SAFETY_HARD_4C, 0, 0, 0, 2, 2, 4, 5, 3, 2, 0, 0, 4, 5, "Jeju Air confirms fatal safety event overrides demand/valuation."),
    Round291ShadowWeightRow(E2RArchetype.OVERSEAS_AUTO_IPO_FAILED_RERATING, 4, 4, 5, 3, 3, 0, 1, 2, 0, 0, -5, 5, 4, "Hyundai India IPO needs aftermarket demand and first-earnings validation."),
    Round291ShadowWeightRow(E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM, 0, 0, 0, 1, 1, 2, 3, 1, 5, 0, -5, 5, 3, "Tourism policy rally needs spend-per-head, occupancy, drop amount and margin."),
    Round291ShadowWeightRow(E2RArchetype.CONTAINER_SHIPPING_RATE_EVENT_PREMIUM, 0, 0, 0, 5, 5, 0, 1, 1, 0, 5, -5, 5, 4, "Red Sea freight spike is Stage 2 until contract-rate durability and route security hold."),
    Round291ShadowWeightRow(E2RArchetype.USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE, 1, 0, 0, 5, 5, 0, 1, 1, 0, 4, 0, 4, 4, "Used-car export shock shows destination demand and route availability are linked."),
)


ROUND291_DEEP_SUB_ARCHETYPES: tuple[Round291DeepSubArchetype, ...] = (
    Round291DeepSubArchetype("자동차 관세·하이브리드 mix", E2RArchetype.AUTO_TARIFF_HYBRID_MIX_STAGE2, ("Hyundai Motor", "Kia", "US tariff", "hybrid mix", "Genesis", "local production hedge")),
    Round291DeepSubArchetype("자동차 중동 물류 차질", E2RArchetype.AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH, ("Hyundai Motor", "Hyundai Glovis", "Middle East route", "Europe exports", "North Africa exports", "intermediate hubs")),
    Round291DeepSubArchetype("항공 통합 Stage 2", E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2, ("Korean Air", "Asiana", "63.88% stake", "international capacity", "LCC consolidation", "frequent flyer")),
    Round291DeepSubArchetype("항공 remedy route/cargo", E2RArchetype.AIRLINE_REMEDY_ROUTE_CARGO_STAGE2, ("T'way Air", "Air Incheon", "Europe routes", "A330-200", "Asiana Cargo", "freighters")),
    Round291DeepSubArchetype("항공 안전 hard 4C", E2RArchetype.AVIATION_SAFETY_HARD_4C, ("Jeju Air", "Muan crash", "179 fatalities", "safety inspection", "market-cap wipeout")),
    Round291DeepSubArchetype("해외 자동차 IPO 실패", E2RArchetype.OVERSEAS_AUTO_IPO_FAILED_RERATING, ("Hyundai Motor India", "HYUN.NS", "weak debut", "first earnings", "Red Sea export disruption")),
    Round291DeepSubArchetype("중국 관광·레저 event premium", E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM, ("Paradise", "Hotel Shilla", "Hyundai Department Store", "Hankook Cosmetics", "visa-free", "visitor spend")),
    Round291DeepSubArchetype("컨테이너 운임 event premium", E2RArchetype.CONTAINER_SHIPPING_RATE_EVENT_PREMIUM, ("HMM", "Red Sea", "Freightos", "Hapag-Lloyd", "Maersk", "Suez normalization")),
    Round291DeepSubArchetype("중고차 수출 물류 4C reference", E2RArchetype.USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE, ("used-car exporters", "Incheon storage", "Dubai", "Strait of Hormuz", "Hyundai Glovis", "HMM")),
)


ROUND291_CASE_CANDIDATES: tuple[Round291CaseCandidate, ...] = (
    Round291CaseCandidate(
        case_id="r9_loop14_hyundai_kia_us_tariff_hybrid_mix",
        symbol="005380/000270",
        company_name="Hyundai Motor / Kia",
        primary_archetype=E2RArchetype.AUTO_TARIFF_HYBRID_MIX_STAGE2,
        secondary_archetypes=(E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH, E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN, E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE),
        case_type="success_candidate",
        round_case_type="success_candidate + 4C-watch",
        stage1_date=date(2025, 4, 1),
        stage2_date=date(2025, 10, 30),
        stage3_date=None,
        stage4b_date=date(2025, 10, 30),
        stage4c_date=date(2025, 7, 31),
        stage3_decision="tariff_relief_and_hybrid_mix_are_stage2_until_pass_through_local_production_incentive_control_mix_margin_and_fcf_confirm",
        stage4b_status="4B-watch/tariff-relief-rally-before-margin-proof",
        hard_4c_confirmed=False,
        evidence_fields=("tariff_new_15pct", "q3_2025_tariff_cost_1_8trn_krw", "hyundai_q3_event_plus_2_7pct", "us_retail_sales_growth_12_7pct", "us_hybrid_sales_share_20pct"),
        red_flag_fields=("tariff_relief_headline_only", "tariff_shock_not_passed_through", "EV_or_hybrid_mix_without_margin", "lost_FTA_advantage_vs_japan"),
        price_data_source="Reuters auto-tariff deal and Hyundai Q3 earnings anchors",
        reported_event_return_anchor="Hyundai -4.5%, Kia -6.6% on tariff deal; later Hyundai +2.7% on Q3 relief/mix",
        reported_event_price_anchor="Q3 OP 2.5T KRW, tariff cost 1.8T KRW, revenue 46.7T KRW",
        event_mfe_pct=2.7,
        event_mae_pct=-6.6,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hyundai_tariff_deal_event_mae_pct": -4.5, "kia_tariff_deal_event_mae_pct": -6.6, "tariff_prior_pct": 25, "tariff_new_pct": 15, "lost_fta_advantage_vs_japan_pct": 2.5, "q3_2025_op_krw_trn": 2.5, "q3_2025_op_yoy_pct": -29, "q3_2025_tariff_cost_krw_trn": 1.8, "q2_2025_tariff_cost_krw_bn": 828, "q3_2025_revenue_krw_trn": 46.7, "q3_2025_revenue_yoy_pct": 8.8, "hyundai_q3_event_mfe_pct": 2.7, "us_retail_sales_growth_pct": 12.7, "us_hybrid_sales_share_pct": 20, "europe_eco_friendly_sales_share_pct": 49},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4C_watch",
        rerating_result="unknown",
        round_rerating_label="AUTO_TARIFF_HYBRID_MIX_STAGE2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="tariff_relief_not_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Tariff relief plus hybrid mix is Stage 2; Green needs pass-through, local hedge, incentive control, margin and FCF.",
    ),
    Round291CaseCandidate(
        case_id="r9_loop14_hyundai_glovis_middle_east_logistics_4c_watch",
        symbol="005380/086280",
        company_name="Hyundai Motor / Hyundai Glovis",
        primary_archetype=E2RArchetype.AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH,
        secondary_archetypes=(E2RArchetype.AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION, E2RArchetype.SHIPPING_GEOPOLITICAL_SECURITY_4C),
        case_type="4b_watch",
        round_case_type="thesis_break_watch / Middle East route disruption",
        stage1_date=date(2026, 3, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 4, 3),
        stage3_decision="vehicle_demand_and_hybrid_mix_are_not_green_when_middle_east_routes_delivery_timing_and_high_margin_exports_are_impaired",
        stage4b_status="4C-watch/route-disruption-high-margin-market-loss",
        hard_4c_confirmed=False,
        evidence_fields=("hyundai_event_minus_1_2pct", "glovis_event_minus_0_7pct", "kospi_plus_2_7pct", "middle_east_shipments_minus_49pct", "q1_2026_op_minus_31pct"),
        red_flag_fields=("route_disruption_blocks_high_margin_exports", "route_security_continuity_unconfirmed", "logistics_cost_control_unconfirmed", "delivery_delay"),
        price_data_source="Reuters Hyundai export disruption and Q1 earnings anchors",
        reported_event_return_anchor="Hyundai -1.2%, Hyundai Glovis -0.7% while KOSPI +2.7%; Q1 OP -31%",
        reported_event_price_anchor="Q1 OP 2.5T KRW; raw-material cost impact 200B KRW; Middle East/Africa 8% wholesale share",
        event_mfe_pct=None,
        event_mae_pct=-1.2,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hyundai_event_mae_pct": -1.2, "hyundai_glovis_event_mae_pct": -0.7, "kospi_same_context_pct": 2.7, "hyundai_relative_underperformance_pp": -3.9, "glovis_relative_underperformance_pp": -3.4, "middle_east_shipments_decline_pct": -49, "hyundai_march_global_sales_yoy_pct": -2.3, "q1_2026_op_krw_trn": 2.5, "q1_2026_op_yoy_pct": -31, "q1_raw_material_cost_impact_krw_bn": 200, "middle_east_africa_wholesale_sales_share_2025_pct": 8, "hybrid_share_total_shipments_q1_2026_pct": 18, "us_hybrid_share_q1_2026_pct": 25},
        score_price_alignment="unknown",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="route_disruption_high_margin_market_loss",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Middle East route disruption is a 4C-watch gate because delivery delays and logistics cost hit high-margin exports.",
    ),
    Round291CaseCandidate(
        case_id="r9_loop14_korean_air_asiana_integration_stage2",
        symbol="003490/020560",
        company_name="Korean Air / Asiana Airlines",
        primary_archetype=E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2,
        secondary_archetypes=(E2RArchetype.AIRLINE_CONSOLIDATION_INTEGRATION, E2RArchetype.LCC_CONSOLIDATION_INTEGRATION),
        case_type="success_candidate",
        round_case_type="success_candidate / airline consolidation Stage 2",
        stage1_date=date(2020, 11, 1),
        stage2_date=date(2024, 12, 12),
        stage3_date=None,
        stage4b_date=date(2024, 12, 12),
        stage4c_date=None,
        stage3_decision="merger_completion_and_record_revenue_are_stage2_until_integration_cost_yield_load_factor_lcc_consolidation_and_safety_quality_confirm",
        stage4b_status="4B-watch/merger-synergy-before-integration-proof",
        hard_4c_confirmed=False,
        evidence_fields=("asiana_stake_63_88pct", "acquisition_value_1_3bn_usd", "international_capacity_rank_12", "revenue_2024_16trn_krw", "op_2024_2trn_krw"),
        red_flag_fields=("merger_completion_only", "integration_synergy_unconfirmed", "load_factor_yield_unconfirmed", "fuel_cost_watch"),
        price_data_source="Reuters Korean Air-Asiana completion and 2024 annual earnings anchors",
        reported_event_return_anchor="Direct event return unavailable; integration and 2024 earnings anchors used",
        reported_event_price_anchor="63.88% Asiana stake, $1.3B deal, 2024 revenue 16T KRW, OP 2T KRW",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"acquisition_value_usd_bn": 1.3, "asiana_stake_pct": 63.88, "integration_period_years_context": 2, "international_capacity_rank_context": 12, "revenue_2024_krw_trn": 16, "revenue_2024_yoy_pct": 10.6, "op_2024_krw_trn": 2, "op_2024_yoy_pct": 22.5, "q4_cargo_revenue_yoy_pct": 9, "q4_passenger_revenue_yoy_pct": -3, "stage3_conditions": ["integration cost", "route optimization", "load factor", "yield", "LCC consolidation", "safety/service quality"]},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_price_data_unavailable",
        rerating_result="unknown",
        round_rerating_label="AIRLINE_CONSOLIDATION_STAGE2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="merger_completion_not_yield_synergy_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Airline consolidation is Stage 2 until yield, load factor, integration cost, LCC consolidation and safety quality close.",
    ),
    Round291CaseCandidate(
        case_id="r9_loop14_tway_air_incheon_airline_remedy_stage2",
        symbol="091810/Air_Incheon_unlisted",
        company_name="T'way Air / Air Incheon",
        primary_archetype=E2RArchetype.AIRLINE_REMEDY_ROUTE_CARGO_STAGE2,
        secondary_archetypes=(E2RArchetype.LCC_ROUTE_REMEDY_LONG_HAUL_OPTION, E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2),
        case_type="success_candidate",
        round_case_type="success_candidate + execution watch",
        stage1_date=date(2024, 3, 7),
        stage2_date=date(2024, 8, 7),
        stage3_date=None,
        stage4b_date=date(2024, 8, 7),
        stage4c_date=None,
        stage3_decision="route_rights_and_cargo_assets_are_stage2_until_load_factor_yield_aircraft_utilization_cargo_customer_retention_and_maintenance_reliability_confirm",
        stage4b_status="4B-watch/route-cargo-remedy-before-operating-margin",
        hard_4c_confirmed=False,
        evidence_fields=("tway_new_eu_routes", "leased_a330_200_aircraft_5", "pilot_support_100", "asiana_cargo_sale_470bn_krw", "asiana_cargo_11_freighters"),
        red_flag_fields=("route_rights_without_load_factor", "cargo_asset_purchase_without_customer_retention", "maintenance_reliability_unconfirmed", "aircraft_utilization_unconfirmed"),
        price_data_source="Reuters T'way Europe-route remedy and Air Incheon cargo-sale anchors",
        reported_event_return_anchor="Direct event return unavailable; route/cargo remedy assets used as Stage 2 anchors",
        reported_event_price_anchor="Europe routes, 5 A330-200 aircraft, 100 pilots, Asiana Cargo sale 470B KRW",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"tway_new_eu_routes": ["Paris", "Rome", "Barcelona", "Frankfurt"], "route_start_period": "2024-06_to_2024-10", "leased_a330_200_aircraft": 5, "pilot_support_count": 100, "tway_2024_growth_target_pct": "30-40", "asiana_cargo_sale_krw_bn": 470, "asiana_cargo_sale_usd_mn": 342, "asiana_cargo_freighters": 11, "asiana_cargo_cities": 25, "asiana_cargo_countries": 12, "stage3_conditions": ["load_factor", "yield", "aircraft_utilization", "cargo_customer_retention", "maintenance_reliability"]},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_execution_watch",
        rerating_result="unknown",
        round_rerating_label="AIRLINE_REMEDY_ROUTE_CARGO_STAGE2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="route_rights_and_cargo_assets_not_operating_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Route rights and cargo assets are Stage 2; Green needs load factor, yield, utilization and customer retention.",
    ),
    Round291CaseCandidate(
        case_id="r9_loop14_jeju_air_safety_hard_4c",
        symbol="089590",
        company_name="Jeju Air",
        primary_archetype=E2RArchetype.AVIATION_SAFETY_HARD_4C,
        secondary_archetypes=(E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C, E2RArchetype.AIRLINE_TRAVEL_CYCLE),
        case_type="4c_thesis_break",
        round_case_type="hard 4C / aviation safety trust break",
        stage1_date=date(2024, 12, 29),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 30),
        stage3_decision="fatal_aviation_safety_event_overrides_travel_demand_yield_and_valuation_logic",
        stage4b_status="hard-4C/fatal-aviation-safety-event",
        hard_4c_confirmed=True,
        evidence_fields=("muan_fatal_crash", "fatalities_179", "jeju_air_event_minus_15_7pct", "market_cap_wipeout_95_7bn_krw", "safety_inspection_ordered"),
        red_flag_fields=("fatal_aviation_safety_event", "safety_risk_unresolved", "consumer_trust_collapse", "market_cap_wipeout"),
        price_data_source="Reuters Jeju Air crash event-price anchor",
        reported_event_return_anchor="Jeju Air -15.7% intraday; -8.5% mid-session; AK Holdings -12%",
        reported_event_price_anchor="Event low 6,920 KRW; market-cap wipeout up to 95.7B KRW",
        event_mfe_pct=None,
        event_mae_pct=-15.7,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=6920.0,
        extra_price_metrics={"fatalities": 179, "event_low_price_krw": 6920, "event_intraday_mae_pct": -15.7, "event_mid_session_mae_pct": -8.5, "market_cap_wipeout_krw_bn": 95.7, "market_cap_wipeout_usd_mn": 65.2, "ak_holdings_event_mae_pct": -12, "safety_inspection_ordered": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="AVIATION_SAFETY_HARD_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="fatal_safety_event_overrides_travel_demand",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Fatal safety event is hard 4C and overrides travel-demand or valuation recovery language.",
    ),
    Round291CaseCandidate(
        case_id="r9_loop14_hyundai_india_ipo_failed_rerating",
        symbol="005380/HYUN.NS",
        company_name="Hyundai Motor / Hyundai Motor India",
        primary_archetype=E2RArchetype.OVERSEAS_AUTO_IPO_FAILED_RERATING,
        secondary_archetypes=(E2RArchetype.INDIA_AUTO_IPO_CAPITAL_RECYCLING, E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE),
        case_type="failed_rerating",
        round_case_type="failed_rerating / overseas auto IPO quality gate",
        stage1_date=date(2024, 10, 14),
        stage2_date=date(2024, 10, 14),
        stage3_date=None,
        stage4b_date=date(2024, 10, 14),
        stage4c_date=date(2024, 10, 22),
        stage3_decision="large_india_ipo_and_market_share_are_not_green_when_debut_first_earnings_domestic_sales_and_exports_fail",
        stage4b_status="4B-watch/IPO-valuation-before-aftermarket-and-first-earnings",
        hard_4c_confirmed=False,
        evidence_fields=("ipo_value_3_3bn_usd", "parent_stake_sale_17_5pct", "offer_price_1960_inr", "market_share_india_15pct"),
        red_flag_fields=("overseas_IPO_size_only", "overseas_IPO_weak_debut_plus_weak_first_earnings", "domestic_sales_decline", "exports_decline"),
        price_data_source="Reuters Hyundai Motor India IPO debut and Q2 earnings anchors",
        reported_event_return_anchor="Debut down as much as -6%; Q2 profit -16.5%, domestic sales -6%, exports -17%",
        reported_event_price_anchor="Offer 1,960 INR, listing 1,934 INR, morning trade 1,882.10 INR",
        event_mfe_pct=None,
        event_mae_pct=-6.0,
        stage1_price_anchor=None,
        stage2_price_anchor=1960.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=1960.0,
        stage4c_price_anchor=1882.10,
        extra_price_metrics={"ipo_value_usd_bn": 3.3, "parent_stake_sale_pct": 17.5, "target_valuation_usd_bn": 19, "offer_price_inr": 1960, "listing_price_inr": 1934, "morning_trade_price_inr": 1882.10, "debut_mae_pct": -6.0, "valuation_debut_inr_trn": 1.53, "valuation_debut_usd_bn": 18.2, "market_share_india_pct": 15, "ipo_oversubscription": "more_than_2x", "q2_profit_decline_pct": -16.5, "q2_profit_inr_bn": 13.38, "domestic_sales_decline_pct": -6, "exports_decline_pct": -17, "q2_revenue_inr_bn": 169.61, "q2_revenue_decline_pct": -7.5, "volume_decline_pct": -9},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="failed_rerating",
        rerating_result="no_rerating",
        round_rerating_label="OVERSEAS_AUTO_IPO_QUALITY_GATE",
        stage_failure_type="false_yellow",
        round_stage_failure_label="IPO_size_and_India_growth_not_aftermarket_margin_green",
        price_validation_status="reported_ipo_anchor_not_full_ohlc",
        notes="India growth and IPO size failed debut and first-earnings validation.",
    ),
    Round291CaseCandidate(
        case_id="r9_loop14_china_tourism_leisure_basket",
        symbol="034230/008770/069960/123690",
        company_name="Paradise / Hotel Shilla / Hyundai Department Store / Hankook Cosmetics",
        primary_archetype=E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.CASINO_DUTYFREE_TOURISM, E2RArchetype.TOURISM_REDIRECT_POLICY_EVENT),
        case_type="event_premium",
        round_case_type="event_premium + 4B-watch",
        stage1_date=date(2025, 3, 20),
        stage2_date=date(2025, 8, 6),
        stage3_date=None,
        stage4b_date=date(2025, 8, 6),
        stage4c_date=None,
        stage3_decision="visa_free_visitor_count_is_stage2_until_spend_per_head_casino_drop_hotel_adr_occupancy_and_margin_confirm",
        stage4b_status="4B-watch/tourism-policy-rally-before-spend-margin",
        hard_4c_confirmed=False,
        evidence_fields=("visa_free_chinese_group_tour_policy", "visitors_2024_16_4mn", "chinese_visitor_share_28pct", "tourism_basket_event_rally"),
        red_flag_fields=("visitor_count_only", "tourism_arrivals_without_spend_conversion", "casino_drop_amount_unconfirmed", "hotel_adr_occupancy_unconfirmed"),
        price_data_source="Reuters China group-tourist visa-free and leisure-stock reaction anchors",
        reported_event_return_anchor="Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%",
        reported_event_price_anchor="2024 foreign visitors 16.4M, Chinese share 28%, 2025 target 18.5M",
        event_mfe_pct=9.9,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"visa_free_start": "2025-09-29", "visa_free_end": "2026-06", "visitors_2024_mn": 16.4, "visitors_2024_yoy_growth_pct": 48, "chinese_visitor_share_2024_pct": 28, "visitor_target_2025_mn": 18.5, "hyundai_department_store_event_mfe_pct": 7.1, "hotel_shilla_event_mfe_pct": 4.8, "paradise_event_mfe_pct": 2.9, "hankook_cosmetics_event_mfe_pct": 9.9, "casino_drop_amount_confirmed": False, "hotel_adr_occupancy_confirmed": False, "tourist_spend_per_head_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="CHINA_TOURISM_LEISURE_EVENT_STAGE2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="visitor_count_not_spend_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Visitor count and policy rally need spend-per-head, casino drop, hotel ADR/occupancy and margin conversion.",
    ),
    Round291CaseCandidate(
        case_id="r9_loop14_hmm_red_sea_freight_rate_event_premium",
        symbol="011200",
        company_name="HMM / container-shipping read-through",
        primary_archetype=E2RArchetype.CONTAINER_SHIPPING_RATE_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.RED_SEA_FREIGHT_CYCLE_4B_4C, E2RArchetype.SHIPPING_FREIGHT_CYCLE, E2RArchetype.SHIPPING_FREIGHT_NORMALIZATION_4C),
        case_type="event_premium",
        round_case_type="event_premium + 4B-watch",
        stage1_date=date(2024, 5, 1),
        stage2_date=date(2024, 7, 3),
        stage3_date=None,
        stage4b_date=date(2024, 7, 3),
        stage4c_date=date(2025, 10, 9),
        stage3_decision="freight_spot_rate_spike_is_stage2_until_contract_rate_mix_fuel_cost_vessel_utilization_route_security_and_cash_yield_confirm",
        stage4b_status="4B-watch/freight-spot-rate-cycle-before-contract-durability",
        hard_4c_confirmed=False,
        evidence_fields=("global_vessel_capacity_tied_5_9pct", "freightos_spot_index_plus_40pct", "freightos_spot_index_5068_usd", "maersk_ceasefire_event_minus_2pct"),
        red_flag_fields=("freight_spot_rate_only", "freight_rate_normalization_after_spot_rally", "rate_normalization_risk", "contract_rate_mix_unconfirmed"),
        price_data_source="Reuters Hapag-Lloyd / Maersk Red Sea freight-rate cycle anchors",
        reported_event_return_anchor="Freightos spot index +40% in six weeks; Maersk -2% on Suez/Red Sea normalization expectations",
        reported_event_price_anchor="Freightos spot index $5,068; vessel capacity tied 5-9%",
        event_mfe_pct=40.0,
        event_mae_pct=-2.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"global_vessel_capacity_tied_pct": "5-9", "freightos_spot_index_6w_growth_pct": 40, "freightos_spot_index_usd": 5068, "global_container_demand_growth_2024_pct": "3-4", "maersk_ceasefire_event_mae_pct": -2, "rate_normalization_risk": True, "hmm_direct_event_price": "price_data_unavailable_after_deep_search", "stage3_conditions": ["contract_rate_mix", "fuel_cost", "vessel_utilization", "route_security", "cash_yield"]},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="CONTAINER_SHIPPING_RATE_EVENT_STAGE2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="freight_rate_spike_not_durable_yield_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Spot freight-rate spike is cyclical until contract mix, vessel utilization and route security prove durability.",
    ),
    Round291CaseCandidate(
        case_id="r9_loop14_korea_used_car_export_logistics_shock",
        symbol="used_car_exporters/HMM/Hyundai_Glovis_readthrough",
        company_name="Korea used-car export logistics reference",
        primary_archetype=E2RArchetype.USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE,
        secondary_archetypes=(E2RArchetype.AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION, E2RArchetype.CONTAINER_SHIPPING_RATE_EVENT_PREMIUM),
        case_type="4c_thesis_break",
        round_case_type="4C-reference / used-car export route disruption",
        stage1_date=date(2026, 3, 24),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 3, 24),
        stage3_decision="export_demand_is_not_green_when_destination_route_availability_storage_and_shipping_flow_are_blocked",
        stage4b_status="4C-reference/destination-route-disruption",
        hard_4c_confirmed=False,
        evidence_fields=("korea_used_car_exports_883000_units", "middle_east_share_more_than_one_third", "incheon_storage_middle_east_bound_share_80pct", "hmm_containers_stuck_near_mumbai"),
        red_flag_fields=("route_disruption_blocks_high_margin_exports", "destination_demand_route_disruption", "storage_congestion", "containers_stuck"),
        price_data_source="Reuters used-car export logistics shock anchor",
        reported_event_return_anchor="Listed direct price unavailable; route/destination logistics reference used",
        reported_event_price_anchor="Korea used-car exports 883,000 units; more than one-third to Middle East; storage-bound share around 80%",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"japan_korea_used_car_exports_usd_bn": 19, "korea_used_car_exports_units": 883000, "korea_used_car_exports_middle_east_share_pct": "more_than_one_third", "incheon_storage_middle_east_bound_share_pct": 80, "stuck_storage_share_context_pct": 70, "exporter_revenue_tied_to_uae_krw_bn": 6.6, "hmm_containers_stuck_near": "Mumbai", "listed_direct_price": "price_data_unavailable_after_deep_search", "use_as_transport_logistics_4c_reference": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="demand_destination_route_disruption",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Destination demand and route availability must both clear for export logistics.",
    ),
)


def round291_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND291_CASE_CANDIDATES:
        stage3_terms = ("margin", "yield", "load", "spend", "durability", "pass_through", "hedge", "security", "synergy", "fcf")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND291_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round291 R9 Loop-14 mobility/transport/leisure price validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in (*candidate.evidence_fields, *ROUND291_GREEN_REQUIRED_FIELDS) if any(token in field.lower() for token in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("rally", "premium", "ipo", "freight", "tourism", "merger", "remedy", "tariff"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("fatal", "safety", "route", "tariff", "weak", "decline", "normalization", "disruption", "trust", "failure"))),
            must_have_fields=ROUND291_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4b_watch", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND291_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "hard_4c_confirmed_true_for_Jeju_Air_aviation_safety",
                "do_not_use_round291_cases_as_candidate_generation_input",
                "do_not_treat_tariff_tourism_merger_route_freight_or_IPO_headlines_as_green_alone",
                *ROUND291_GREEN_REQUIRED_FIELDS,
                *ROUND291_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.event_mfe_pct,
                mae_30d=candidate.event_mae_pct,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.event_mfe_pct is not None
                    or candidate.event_mae_pct is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round291_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(
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
            "reported_event_return_anchor": candidate.reported_event_return_anchor,
            "reported_event_price_anchor": candidate.reported_event_price_anchor,
            "event_mfe_pct": _float_text(candidate.event_mfe_pct),
            "event_mae_pct": _float_text(candidate.event_mae_pct),
            "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": candidate.score_price_alignment,
            "round_alignment_label": candidate.round_alignment_label,
            "rerating_result": candidate.rerating_result,
            "round_rerating_label": candidate.round_rerating_label,
            "stage_failure_type": candidate.stage_failure_type,
            "round_stage_failure_label": candidate.round_stage_failure_label,
            "price_validation_status": candidate.price_validation_status,
            "evidence_fields": "|".join(candidate.evidence_fields),
            "red_flag_fields": "|".join(candidate.red_flag_fields),
            "notes": candidate.notes,
        }
        for candidate in ROUND291_CASE_CANDIDATES
    )


def round291_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND291_SCORE_ADJUSTMENTS)


def round291_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND291_SHADOW_WEIGHT_ROWS)


def round291_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND291_DEEP_SUB_ARCHETYPES)


def round291_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round291_price_validation": "true"} for field in ROUND291_PRICE_VALIDATION_FIELDS)


def round291_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round291_label": label, "canonical_archetype": canonical} for label, canonical in ROUND291_REQUIRED_TARGET_ALIASES.items())


def round291_summary() -> dict[str, int | bool | str]:
    cases = ROUND291_CASE_CANDIDATES
    return {
        "source_round": ROUND291_SOURCE_ROUND_PATH,
        "round_id": ROUND291_ANALYST_ROUND_ID,
        "large_sector": ROUND291_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "watch_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "unknown_alignment_count": sum(1 for case in cases if case.score_price_alignment == "unknown"),
        "target_archetype_count": len(ROUND291_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND291_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND291_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round291_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND291_SOURCE_ROUND_PATH,
        "round_id": ROUND291_ANALYST_ROUND_ID,
        "large_sector": ROUND291_LARGE_SECTOR,
        "summary": round291_summary(),
        "target_aliases": dict(ROUND291_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND291_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND291_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND291_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND291_HARD_4C_GATES),
        "score_adjustments": list(round291_score_adjustment_rows()),
        "shadow_weights": list(round291_shadow_weight_rows()),
        "deep_sub_archetypes": list(round291_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND291_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round291_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_tariff_tourism_merger_route_freight_or_IPO_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round291_summary_markdown() -> str:
    summary = round291_summary()
    lines = [
        "# Round 291 R9 Loop 14 Mobility Transport Leisure Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- watch rows: {summary['watch_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND291_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.round_case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    case.round_alignment_label,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Hyundai/Kia tariff relief plus hybrid mix is Stage 2 until tariff pass-through, local production hedge, margin and FCF close.",
            "- Hyundai/Glovis shows route security and logistics cost can become auto/export 4C-watch gates.",
            "- Korean Air/Asiana and T'way/Air Incheon are Stage 2 until yield, load factor, cargo retention and integration execution are visible.",
            "- Jeju Air is the hard 4C reference because fatal safety events override travel-demand logic.",
            "- Hyundai India shows large overseas IPO size does not prove parent rerating when debut and first earnings fail.",
            "- China tourism and HMM/Red Sea are event premiums until spend conversion and freight durability are proven.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round291_green_gate_review_markdown() -> str:
    lines = [
        "# Round 291 R9 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R9 Stage 3-Green is not `tariff relief`, `hybrid`, `airline merger`, `route rights`, `China tourists`, `freight spike`, or `overseas IPO`. It requires tariff pass-through, margin, route security, yield, safety trust, spend-per-head, freight durability, OP/FCF, and price path after evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND291_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND291_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND291_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Hyundai tariff falls from 25% to 15%` is not Green; margin after tariff and incentives must recover.",
            "- `China visitors +48%` is useful, but Green needs spend-per-head, hotel ADR/occupancy and casino drop.",
            "- `Jeju Air fatal crash` is hard 4C because safety trust breaks before any demand thesis.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round291_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 291 R9 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND291_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND291_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND291_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round291_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 291 R9 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, tariff pass-through, margin, route recovery, yield, safety trust, spend conversion, freight durability, OP/FCF or ROIC where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND291_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND291_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_event_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round291_r9_loop14_reports(
    output_directory: str | Path = ROUND291_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND291_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND291_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round291_case_records(), cases_path),
        "audit": _write_json(round291_audit_payload(), audit_path),
        "summary": output / "round291_r9_loop14_price_validation_summary.md",
        "case_matrix": output / "round291_r9_loop14_case_matrix.csv",
        "target_aliases": output / "round291_r9_loop14_target_aliases.csv",
        "score_adjustments": output / "round291_r9_loop14_score_adjustments.csv",
        "shadow_weights": output / "round291_r9_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round291_r9_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round291_r9_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round291_r9_loop14_green_gate_review.md",
        "price_validation_plan": output / "round291_r9_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round291_r9_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round291_summary_markdown(), encoding="utf-8")
    _write_csv(round291_case_rows(), paths["case_matrix"])
    _write_csv(round291_target_alias_rows(), paths["target_aliases"])
    _write_csv(round291_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round291_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round291_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round291_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round291_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round291_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round291_stage4b_4c_review_markdown(), encoding="utf-8")
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
    return f"+{value}" if value > 0 else str(value)
