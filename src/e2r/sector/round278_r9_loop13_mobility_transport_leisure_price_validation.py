"""Round-278 R9 Loop-13 mobility/transport/leisure validation pack.

This module converts ``docs/round/round_278.md`` into calibration-only case
records and reports. It does not change production scoring, candidate
generation, or StageClassifier thresholds.

Easy example: Kia's US sales grew, but tariff cost cut operating profit. That is
not Stage 3-Green; R9 needs margin after tariff, mix, price pass-through and FCF.
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


ROUND278_SOURCE_ROUND_PATH = "docs/round/round_278.md"
ROUND278_ANALYST_ROUND_ID = "round_206"
ROUND278_LARGE_SECTOR = Round10LargeSector.MOBILITY_TRANSPORT_LEISURE.value
ROUND278_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round278_r9_loop13_mobility_transport_leisure_price_validation"
ROUND278_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r9_loop13_round278.jsonl"
ROUND278_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round278_r9_loop13_mobility_transport_leisure_price_validation_audit.json"

ROUND278_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2": E2RArchetype.HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2.value,
    "AUTO_TARIFF_MARGIN_4C_WATCH": E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH.value,
    "INDIA_AUTO_IPO_CAPITAL_RECYCLING": E2RArchetype.INDIA_AUTO_IPO_CAPITAL_RECYCLING.value,
    "AIRLINE_CONSOLIDATION_STAGE2": E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2.value,
    "AVIATION_SAFETY_HARD_4C": E2RArchetype.AVIATION_SAFETY_HARD_4C.value,
    "AUTO_PARTS_PORTFOLIO_RECYCLING": E2RArchetype.AUTO_PARTS_PORTFOLIO_RECYCLING.value,
    "RED_SEA_FREIGHT_CYCLE_4B_4C": E2RArchetype.RED_SEA_FREIGHT_CYCLE_4B_4C.value,
    "CHINA_TOURISM_LEISURE_EVENT_PREMIUM": E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM.value,
}

ROUND278_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "OP_margin_after_tariff_confirmed",
    "hybrid_SUV_mix_quality_confirmed",
    "price_pass_through_confirmed",
    "shareholder_return_execution_confirmed",
    "integration_synergy_realization_confirmed",
    "fleet_capex_ROI_confirmed",
    "aviation_safety_trust_confirmed",
    "freight_rate_durability_confirmed",
    "booking_occupancy_conversion_confirmed",
    "asset_sale_ROIC_confirmed",
    "OP_FCF_conversion_confirmed",
    "price_path_after_evidence",
)

ROUND278_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "unit_sales_without_margin",
    "IPO_valuation_without_parent_ROI",
    "tourist_flow_headline_only",
    "freight_rate_spike_only",
    "fleet_order_without_ROI",
    "exploratory_asset_sale_only",
    "tariff_exposure_unhedged",
    "fatal_safety_event",
    "booking_without_margin",
)

ROUND278_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "hybrid_shareholder_return_event_plus_5pct_before_margin",
    "tourism_travel_basket_plus_20pct_before_booking_margin",
    "freight_rate_cycle_short_rally",
    "airline_consolidation_premium_before_integration",
    "aircraft_order_headline_before_ROI",
    "India_IPO_valuation_before_parent_capital_return_bridge",
    "asset_sale_exploration_before_final_value",
)

ROUND278_HARD_4C_GATES: tuple[str, ...] = (
    "fatal_crash_or_safety_inspection",
    "tariff_cost_crushing_margin",
    "airline_integration_failure",
    "fleet_capex_overhang_with_weak_demand",
    "tourism_cancellation_shock",
    "shipping_route_normalization_collapsing_freight_rates",
    "asset_sale_failure_after_price_premium",
    "IPO_debut_failure_if_used_as_parent_valueup_thesis",
)

ROUND278_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "deal_or_policy_value_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "tariff_margin_anchor",
    "safety_trust_anchor",
    "freight_or_booking_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round278ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round278ShadowWeightRow:
    archetype: E2RArchetype
    op_margin_after_tariff: int
    hybrid_suv_mix_quality: int
    price_pass_through: int
    shareholder_return_execution: int
    integration_synergy_realization: int
    fleet_capex_roi: int
    aviation_safety_trust: int
    freight_rate_durability: int
    booking_occupancy_conversion: int
    asset_sale_roic: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "op_margin_after_tariff": _signed(self.op_margin_after_tariff),
            "hybrid_suv_mix_quality": _signed(self.hybrid_suv_mix_quality),
            "price_pass_through": _signed(self.price_pass_through),
            "shareholder_return_execution": _signed(self.shareholder_return_execution),
            "integration_synergy_realization": _signed(self.integration_synergy_realization),
            "fleet_capex_ROI": _signed(self.fleet_capex_roi),
            "aviation_safety_trust": _signed(self.aviation_safety_trust),
            "freight_rate_durability": _signed(self.freight_rate_durability),
            "booking_occupancy_conversion": _signed(self.booking_occupancy_conversion),
            "asset_sale_ROIC": _signed(self.asset_sale_roic),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round278DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round278CaseCandidate:
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
    event_mfe_pct: float | None
    event_mae_pct: float | None
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


ROUND278_SCORE_ADJUSTMENTS: tuple[Round278ScoreAdjustment, ...] = (
    Round278ScoreAdjustment("OP_margin_after_tariff", 5, "raise", "판매량보다 관세 이후 OP margin이 먼저다."),
    Round278ScoreAdjustment("hybrid_SUV_mix_quality", 5, "raise", "하이브리드/SUV mix가 ASP와 margin으로 닫혀야 한다."),
    Round278ScoreAdjustment("price_pass_through", 5, "raise", "관세와 비용을 가격에 전가할 수 있어야 한다."),
    Round278ScoreAdjustment("shareholder_return_execution", 4, "raise", "자사주·배당은 실제 실행과 FCF 재원이 필요하다."),
    Round278ScoreAdjustment("integration_synergy_realization", 5, "raise", "항공 합병은 통합 시너지와 노선 수익성이 확인되어야 한다."),
    Round278ScoreAdjustment("fleet_capex_ROI", 5, "raise", "항공기 주문은 성장투자이면서 capex 부담이다."),
    Round278ScoreAdjustment("aviation_safety_trust", 5, "raise", "항공 안전 신뢰는 hard gate다."),
    Round278ScoreAdjustment("freight_rate_durability", 5, "raise", "해운은 spot 운임이 아니라 contract durability가 필요하다."),
    Round278ScoreAdjustment("booking_occupancy_conversion", 5, "raise", "관광객 headline은 booking, occupancy, ADR, margin으로 검증해야 한다."),
    Round278ScoreAdjustment("asset_sale_ROIC", 4, "raise", "자산매각은 deal value와 proceeds use가 확인되어야 한다."),
    Round278ScoreAdjustment("unit_sales_without_margin", -5, "lower", "판매량만 좋고 OP가 깨지면 Green이 아니다."),
    Round278ScoreAdjustment("IPO_valuation_without_parent_ROI", -5, "lower", "자회사 IPO valuation은 모회사 ROIC/환원 연결고리 전에는 부족하다."),
    Round278ScoreAdjustment("tourist_flow_headline_only", -5, "lower", "관광객 수만으로 소비·마진을 만들지 않는다."),
    Round278ScoreAdjustment("freight_rate_spike_only", -5, "lower", "운임 spike는 cycle일 수 있으므로 구조적 Green을 제한한다."),
    Round278ScoreAdjustment("fatal_safety_event", -5, "lower", "사망 사고는 safety trust hard 4C다."),
)

ROUND278_SHADOW_WEIGHT_ROWS: tuple[Round278ShadowWeightRow, ...] = (
    Round278ShadowWeightRow(E2RArchetype.HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2, 5, 5, 5, 4, 0, 1, 2, 0, 0, 0, -2, 4, 4, "Hyundai Motor is Stage 2 until tariff-adjusted margin and FCF close."),
    Round278ShadowWeightRow(E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH, 5, 2, 5, 0, 0, 0, 0, 0, 0, 0, -5, 4, 5, "Kia shows unit sales can fail when tariff cost crushes OP."),
    Round278ShadowWeightRow(E2RArchetype.INDIA_AUTO_IPO_CAPITAL_RECYCLING, 2, 3, 1, 4, 0, 0, 0, 0, 0, 3, -5, 5, 4, "India IPO is capital recycling, not parent Green without proceeds use and ROIC."),
    Round278ShadowWeightRow(E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2, 0, 0, 0, 0, 5, 5, 5, 0, 2, 0, -4, 5, 5, "Korean Air/Asiana needs integration synergy, fleet ROI and safety trust."),
    Round278ShadowWeightRow(E2RArchetype.AVIATION_SAFETY_HARD_4C, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 5, "Jeju Air confirms fatal crash is hard 4C."),
    Round278ShadowWeightRow(E2RArchetype.AUTO_PARTS_PORTFOLIO_RECYCLING, 0, 2, 0, 2, 0, 0, 0, 0, 0, 4, -4, 5, 4, "Hyundai Mobis lighting sale needs final value and proceeds use."),
    Round278ShadowWeightRow(E2RArchetype.RED_SEA_FREIGHT_CYCLE_4B_4C, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, -5, 5, 5, "HMM/Pan Ocean Red Sea benefit is cycle until contract rate durability is shown."),
    Round278ShadowWeightRow(E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM, 0, 0, 0, 0, 0, 0, 1, 0, 5, 0, -5, 5, 4, "China tourism headlines need booking, occupancy, ADR and margin conversion."),
)

ROUND278_DEEP_SUB_ARCHETYPES: tuple[Round278DeepSubArchetype, ...] = (
    Round278DeepSubArchetype("자동차 하이브리드·주주환원", E2RArchetype.HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2, ("Hyundai Motor", "hybrid lineup doubling", "EREV", "Georgia plant", "buyback", "dividend policy")),
    Round278DeepSubArchetype("자동차 관세 마진 4C-watch", E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH, ("Kia", "US tariff", "tariff hit", "unit sales", "OP margin")),
    Round278DeepSubArchetype("인도 자동차 IPO 자본재활용", E2RArchetype.INDIA_AUTO_IPO_CAPITAL_RECYCLING, ("Hyundai Motor India", "IPO", "stake sale", "parent capital return", "SUV mix")),
    Round278DeepSubArchetype("항공 합병 Stage 2", E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2, ("Korean Air", "Asiana", "LCC integration", "Boeing 103 aircraft", "GE engine deal")),
    Round278DeepSubArchetype("항공 안전 hard 4C", E2RArchetype.AVIATION_SAFETY_HARD_4C, ("Jeju Air", "fatal crash", "safety inspection", "consumer trust")),
    Round278DeepSubArchetype("자동차부품 포트폴리오 재활용", E2RArchetype.AUTO_PARTS_PORTFOLIO_RECYCLING, ("Hyundai Mobis", "lighting business", "OPmobility", "deal value", "proceeds use")),
    Round278DeepSubArchetype("Red Sea 해운 운임 cycle", E2RArchetype.RED_SEA_FREIGHT_CYCLE_4B_4C, ("HMM", "Pan Ocean", "Red Sea rerouting", "Suez return", "freight rate durability")),
    Round278DeepSubArchetype("중국 관광·레저 event premium", E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM, ("Lotte Tour", "Yellow Balloon", "Hotel Shilla", "Paradise", "visa-free", "booking margin")),
)

ROUND278_CASE_CANDIDATES: tuple[Round278CaseCandidate, ...] = (
    Round278CaseCandidate(
        case_id="r9_loop13_hyundai_motor_hybrid_shareholder_return_tariff_watch",
        symbol="005380",
        company_name="Hyundai Motor",
        primary_archetype=E2RArchetype.HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2,
        secondary_archetypes=(E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN, E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE),
        case_type="success_candidate",
        round_case_type="success_candidate + tariff 4C-watch",
        stage1_date=date(2024, 8, 28),
        stage2_date=date(2024, 8, 28),
        stage3_date=None,
        stage4b_date=date(2024, 8, 28),
        stage4c_date=date(2025, 4, 24),
        stage3_decision="hybrid_shareholder_return_is_stage2_until_tariff_margin_pass_through_and_fcf_confirm",
        stage4b_status="4B-watch/shareholder-return-event-before-tariff-margin",
        hard_4c_confirmed=False,
        evidence_fields=("global_sales_target_5_55mn", "hybrid_sales_target_1_33mn", "buyback_4trn_krw", "dividend_floor_2500_krw", "domestic_investment_24_3trn_krw"),
        red_flag_fields=("tariff_exposure_unhedged", "OP_margin_after_tariff_unconfirmed", "price_pass_through_unconfirmed"),
        price_data_source="Reuters Hyundai investor-day / domestic investment / Q1 tariff anchors",
        reported_price_anchor="Hyundai strategy event +5% intraday and +4.7% close; later Q1 tariff watch -0.5%",
        reported_return_anchor="Hybrid/shareholder-return event worked, but tariff margin remains open",
        event_mfe_pct=5.0,
        event_mae_pct=-0.5,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hyundai_event_intraday_mfe_pct": 5.0, "hyundai_event_close_mfe_pct": 4.7, "global_sales_target_2030_mn": 5.55, "growth_vs_2023_pct": 30, "hybrid_sales_target_2028_mn": 1.33, "ev_sales_target_2030_mn": 2.0, "buyback_2025_2027_krw_trn": 4.0, "minimum_quarterly_dividend_krw": 2500, "profit_return_target_pct": 35, "domestic_investment_2025_krw_trn": 24.3, "domestic_investment_growth_pct": 19, "q1_2025_op_krw_trn": 3.6, "q1_2025_op_growth_pct": 2, "us_sales_share_context": "about_one_third_global_sales", "q1_earnings_event_mae_pct": -0.5},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4C_watch",
        rerating_result="unknown",
        round_rerating_label="hybrid_shareholder_return_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="hybrid_strategy_not_green_until_tariff_margin_FCF",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Strong Stage 2 mobility case, but Green waits for OP margin after tariff, price pass-through and FCF.",
    ),
    Round278CaseCandidate(
        case_id="r9_loop13_kia_us_tariff_margin_break",
        symbol="000270",
        company_name="Kia Corp",
        primary_archetype=E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH,
        secondary_archetypes=(E2RArchetype.AUTO_TARIFF_MARGIN_SHOCK, E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE),
        case_type="success_candidate",
        round_case_type="evidence_good_but_price_failed / auto tariff 4C-watch",
        stage1_date=date(2025, 4, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 7, 25),
        stage3_decision="unit_sales_are_not_green_when_tariff_cost_crushes_margin",
        stage4b_status="4C-watch/tariff-margin-break",
        hard_4c_confirmed=False,
        evidence_fields=("us_sales_growth_5pct", "q2_op_2_76trn_krw"),
        red_flag_fields=("unit_sales_without_margin", "tariff_cost_crushing_margin", "q2_op_decline_24pct"),
        price_data_source="Reuters Kia Q2 tariff anchor",
        reported_price_anchor="Tariff hit 786B KRW, OP -24%, shares -1.7%",
        reported_return_anchor="US sales +5% failed to offset tariff margin hit",
        event_mfe_pct=None,
        event_mae_pct=-1.7,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"q2_tariff_hit_krw_bn": 786, "q2_tariff_hit_usd_mn": 570, "q2_op_krw_trn": 2.76, "q2_op_decline_pct": -24, "us_sales_growth_pct": 5, "event_mae_pct": -1.7, "tariff_hit_as_share_of_q2_op_pct": 28.5},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="unknown",
        round_rerating_label="auto_tariff_margin_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="unit_sales_not_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Kia is the simple example: unit sales grew, but tariff cost broke OP margin.",
    ),
    Round278CaseCandidate(
        case_id="r9_loop13_hyundai_motor_india_ipo_capital_recycling",
        symbol="005380/HYUN.NS",
        company_name="Hyundai Motor / Hyundai Motor India",
        primary_archetype=E2RArchetype.INDIA_AUTO_IPO_CAPITAL_RECYCLING,
        secondary_archetypes=(E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN, E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN),
        case_type="failed_rerating",
        round_case_type="failed_rerating / capital recycling watch",
        stage1_date=date(2024, 10, 8),
        stage2_date=date(2024, 10, 14),
        stage3_date=None,
        stage4b_date=date(2024, 10, 14),
        stage4c_date=date(2024, 10, 22),
        stage3_decision="IPO_monetization_is_stage2_until_parent_proceeds_use_ROIC_and_shareholder_return_bridge",
        stage4b_status="4B-watch/IPO-valuation-before-parent-ROI",
        hard_4c_confirmed=False,
        evidence_fields=("ipo_value_3_3bn_usd", "parent_stake_sale_17_5pct", "target_valuation_19bn_usd", "shares_offered_142_1947mn"),
        red_flag_fields=("IPO_valuation_without_parent_ROI", "IPO_debut_failure_if_used_as_parent_valueup_thesis", "listing_discount"),
        price_data_source="Reuters Hyundai India IPO and debut anchors",
        reported_price_anchor="Offer 1960 INR, morning trade 1882.10 INR, debut down as much as -6%",
        reported_return_anchor="India IPO was capital recycling, but failed debut blocks parent Green",
        event_mfe_pct=None,
        event_mae_pct=-6.0,
        stage2_price_anchor=1960.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=1960.0,
        stage4c_price_anchor=1882.10,
        extra_price_metrics={"ipo_value_usd_bn": 3.3, "parent_stake_sale_pct": 17.5, "target_valuation_usd_bn": 19, "valuation_as_parent_market_cap_pct": 40, "shares_offered_mn": 142.1947, "offer_price_inr": 1960, "listing_price_inr": 1934, "morning_trade_price_inr": 1882.10, "listing_discount_pct": -1.33, "debut_mae_pct": -6.0, "valuation_debut_inr_trn": 1.53, "market_share_india_pct": 15},
        score_price_alignment="false_positive_score",
        round_alignment_label="failed_rerating_watch",
        rerating_result="no_rerating",
        round_rerating_label="India_auto_capital_recycling_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="IPO_valuation_not_parent_green",
        price_validation_status="reported_ipo_anchor_not_full_ohlc",
        notes="Subsidiary IPO is useful only if proceeds use and parent capital-return bridge are visible.",
    ),
    Round278CaseCandidate(
        case_id="r9_loop13_korean_air_asiana_consolidation_fleet_capex_watch",
        symbol="003490/020560/180640",
        company_name="Korean Air / Asiana / Jin Air",
        primary_archetype=E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2,
        secondary_archetypes=(E2RArchetype.AIRLINE_CONSOLIDATION_INTEGRATION, E2RArchetype.LCC_CONSOLIDATION_INTEGRATION),
        case_type="success_candidate",
        round_case_type="success_candidate + fleet capex watch",
        stage1_date=date(2024, 11, 29),
        stage2_date=date(2024, 12, 12),
        stage3_date=None,
        stage4b_date=date(2025, 8, 25),
        stage4c_date=None,
        stage3_decision="airline_consolidation_is_stage2_until_integration_margin_fleet_ROI_and_safety_trust_confirm",
        stage4b_status="4B-watch/fleet-capex-before-ROI",
        hard_4c_confirmed=False,
        evidence_fields=("asiana_stake_63_88pct", "deal_value_1_8trn_krw", "international_capacity_rank_12", "boeing_aircraft_order_103_units", "ge_engine_deal_13_7bn_usd"),
        red_flag_fields=("fleet_order_without_ROI", "integration_synergy_unconfirmed", "aviation_safety_trust_unconfirmed"),
        price_data_source="Reuters Korean Air-Asiana acquisition / branding / Boeing order anchors",
        reported_price_anchor="1.8T KRW acquisition, 63.88% Asiana stake, 103 Boeing aircraft order",
        reported_return_anchor="Consolidation is Stage 2; fleet capex ROI and integration remain gates",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"deal_value_krw_trn": 1.8, "deal_value_usd_bn": 1.3, "asiana_stake_acquired_pct": 63.88, "combined_passenger_capacity_share_context": "just_over_half_of_south_korea_capacity", "international_capacity_rank_context": 12, "boeing_aircraft_order_units": 103, "ge_engine_purchase_maintenance_deal_usd_bn": 13.7, "frequent_flyer_program_review_due": "2025-06 plan submission to KFTC"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4B_watch",
        rerating_result="unknown",
        round_rerating_label="airline_consolidation_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="merger_completion_not_integration_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Korean Air/Asiana is Stage 2; Green needs integration synergy, fleet ROI, safety trust and margin.",
    ),
    Round278CaseCandidate(
        case_id="r9_loop13_jeju_air_fatal_crash_aviation_safety_hard_4c",
        symbol="089590",
        company_name="Jeju Air",
        primary_archetype=E2RArchetype.AVIATION_SAFETY_HARD_4C,
        secondary_archetypes=(E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C, E2RArchetype.AIRLINE_TRAVEL_CYCLE),
        case_type="4c_thesis_break",
        round_case_type="4C-thesis-break / aviation safety hard 4C",
        stage1_date=date(2024, 12, 29),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 30),
        stage3_decision="fatal_aviation_accident_is_hard_4c_not_a_positive_stage_source",
        stage4b_status="hard-4C/fatal-aviation-safety-trust-break",
        hard_4c_confirmed=True,
        evidence_fields=("muan_fatal_crash", "fatalities_179", "government_emergency_safety_inspection", "event_low_6920_krw"),
        red_flag_fields=("fatal_safety_event", "fatal_crash_or_safety_inspection", "consumer_trust_collapse"),
        price_data_source="Reuters Jeju Air crash and event-price anchor",
        reported_price_anchor="Jeju Air -15.7% intraday to 6,920 KRW, market-cap wipeout 95.7B KRW",
        reported_return_anchor="Fatal crash and emergency safety inspection confirm hard 4C",
        event_mfe_pct=None,
        event_mae_pct=-15.7,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=6920.0,
        extra_price_metrics={"fatalities": 179, "event_low_price_krw": 6920, "event_intraday_mae_pct": -15.7, "event_midday_mae_pct": -8.5, "market_cap_wipeout_krw_bn": 95.7, "ak_holdings_mae_pct": -12, "hanatour_mae_pct": -7, "very_good_tour_mae_pct": -11},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="aviation_safety_hard_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="fatal_safety_event",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="A fatal aviation accident breaks safety trust; demand recovery language cannot override it.",
    ),
    Round278CaseCandidate(
        case_id="r9_loop13_hyundai_mobis_lighting_portfolio_recycling",
        symbol="012330",
        company_name="Hyundai Mobis lighting business",
        primary_archetype=E2RArchetype.AUTO_PARTS_PORTFOLIO_RECYCLING,
        secondary_archetypes=(E2RArchetype.AUTO_PARTS_PORTFOLIO_RESTRUCTURING, E2RArchetype.AUTO_MOBILITY_COMPONENTS),
        case_type="success_candidate",
        round_case_type="success_candidate / asset recycling",
        stage1_date=date(2025, 12, 1),
        stage2_date=date(2026, 1, 27),
        stage3_date=None,
        stage4b_date=date(2026, 1, 27),
        stage4c_date=None,
        stage3_decision="exploratory_asset_sale_is_stage2_until_final_value_proceeds_use_and_remaining_ROIC_confirm",
        stage4b_status="4B-watch/asset-sale-exploration-before-final-value",
        hard_4c_confirmed=False,
        evidence_fields=("opmobility_exploratory_agreement", "lighting_revenue_over_1bn_eur", "final_agreement_expected_within_2026"),
        red_flag_fields=("exploratory_asset_sale_only", "deal_value_unconfirmed", "proceeds_use_unconfirmed"),
        price_data_source="Reuters OPmobility / Hyundai Mobis lighting business anchor",
        reported_price_anchor="Exploratory agreement; Hyundai Mobis lighting revenue estimated above EUR 1B per year",
        reported_return_anchor="Deal value and proceeds use are not disclosed",
        event_mfe_pct=1.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"potential_transaction_status": "exploratory_agreement", "financial_terms_disclosed": False, "final_agreement_expected": "within_2026", "hyundai_mobis_lighting_revenue_context_eur_bn": 1.0, "opmobility_exterior_lighting_9m2025_sales_eur_bn": 4.0, "opmobility_early_trading_mfe_pct": 1.0, "deal_value_confirmed": False, "proceeds_use_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_insufficient_price_data",
        rerating_result="unknown",
        round_rerating_label="auto_parts_portfolio_recycling_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="exploratory_sale_not_ROIC_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Asset recycling is Stage 2 until final deal value, proceeds use and remaining-business ROIC are proven.",
    ),
    Round278CaseCandidate(
        case_id="r9_loop13_hmm_pan_ocean_red_sea_freight_cycle_watch",
        symbol="011200/028670",
        company_name="HMM / Pan Ocean",
        primary_archetype=E2RArchetype.RED_SEA_FREIGHT_CYCLE_4B_4C,
        secondary_archetypes=(E2RArchetype.SHIPPING_FREIGHT_CYCLE, E2RArchetype.SHIPPING_FREIGHT_NORMALIZATION_4C),
        case_type="cyclical_success",
        round_case_type="cyclical_success + Red Sea 4B/4C-watch",
        stage1_date=date(2024, 6, 1),
        stage2_date=date(2024, 6, 25),
        stage3_date=None,
        stage4b_date=date(2025, 10, 9),
        stage4c_date=date(2025, 12, 4),
        stage3_decision="freight_rate_cycle_is_not_structural_green_without_contract_rate_durability_and_capacity_floor",
        stage4b_status="4B-watch/Red-Sea-cycle-then-Suez-normalization-risk",
        hard_4c_confirmed=False,
        evidence_fields=("hmm_event_mfe_2_9pct", "pan_ocean_event_mfe_3_9pct", "red_sea_rerouting", "suez_return_transition_60_90_days"),
        red_flag_fields=("freight_rate_spike_only", "shipping_route_normalization_collapsing_freight_rates", "freight_rate_durability_unconfirmed"),
        price_data_source="MarketWatch Korean shipping event anchors + Reuters Red Sea/Suez reopening risk anchors",
        reported_price_anchor="HMM +2.9%, Pan Ocean +3.9%; later Suez return risk and Hapag-Lloyd profit -50%",
        reported_return_anchor="Freight rally is cyclical until contract durability is proven",
        event_mfe_pct=3.9,
        event_mae_pct=-2.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hmm_event_mfe_2024_06_25_pct": 2.9, "hmm_event_mfe_2024_06_28_pct": 2.9, "pan_ocean_event_mfe_2024_06_28_pct": 3.9, "maersk_ceasefire_event_mae_pct": -2.0, "suez_return_transition_period_days": "60-90", "hapag_lloyd_9m_net_profit_decline_pct": -50, "freight_rate_durability_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="cyclical_success_4B_watch",
        rerating_result="cyclical_rerating",
        round_rerating_label="Red_Sea_freight_cycle_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="freight_rate_cycle_not_structural_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Red Sea rerouting can create cyclical success, but Green is restricted without contract freight durability.",
    ),
    Round278CaseCandidate(
        case_id="r9_loop13_china_tourism_leisure_event_premium",
        symbol="032350/104620/034230/008770/004170",
        company_name="China tourism / leisure basket",
        primary_archetype=E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.TOURISM_REDIRECT_POLICY_EVENT, E2RArchetype.CASINO_DUTYFREE_TOURISM),
        case_type="event_premium",
        round_case_type="event_premium + 4B-watch",
        stage1_date=date(2025, 8, 6),
        stage2_date=date(2025, 8, 6),
        stage3_date=None,
        stage4b_date=date(2025, 11, 21),
        stage4c_date=None,
        stage3_decision="tourist_flow_headline_is_not_green_until_booking_occupancy_ADR_casino_drop_and_margin_confirm",
        stage4b_status="4B-watch/tourism-basket-rally-before-booking-margin",
        hard_4c_confirmed=False,
        evidence_fields=("china_group_visa_free_policy", "tourism_basket_rally", "jeju_stay_extension_31_57h"),
        red_flag_fields=("tourist_flow_headline_only", "booking_without_margin", "actual_booking_margin_unconfirmed"),
        price_data_source="Reuters China visa-free and China-Japan tourism rerouting anchors",
        reported_price_anchor="Lotte Tour >20%, Yellow Balloon +24%, Hyundai Department +7.1%, Hotel Shilla +4.8%",
        reported_return_anchor="Policy/reroute event premium; booking, occupancy, ADR and margin are required",
        event_mfe_pct=24.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"visa_free_start": "2025-09-29", "visa_free_end": "2026-06", "visa_free_stay_days": 15, "hyundai_department_store_mfe_pct": 7.1, "hotel_shilla_mfe_pct": 4.8, "paradise_mfe_pct": 2.9, "hankook_cosmetics_mfe_pct": 9.9, "lotte_tour_rerouting_mfe_pct": 20, "yellow_balloon_rerouting_mfe_pct": 24, "shinsegae_rerouting_mfe_pct": 6, "adora_usual_jeju_stay_hours": 9, "adora_new_jeju_stay_hours": "31-57", "actual_booking_margin_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="China_tourism_leisure_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="tourist_flow_headline_not_booking_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Tourism policy can move prices, but Green requires booking, occupancy, ADR, casino drop and margin.",
    ),
)


def round278_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND278_CASE_CANDIDATES:
        stage3_terms = ("margin", "pass_through", "fcf", "roi", "booking", "occupancy", "freight_rate_durability", "safety_trust")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND278_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round278 R9 Loop-13 mobility/transport/leisure price validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in (*candidate.evidence_fields, *ROUND278_GREEN_REQUIRED_FIELDS) if any(token in field.lower() for token in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("premium", "rally", "ipo", "freight", "fleet", "asset", "shareholder", "tourism"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("tariff", "fatal", "safety", "crash", "normalization", "failure", "margin", "cancellation"))),
            must_have_fields=ROUND278_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4b_watch", "4c_thesis_break"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND278_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "hard_4c_confirmed_true_for_aviation_safety",
                "do_not_use_round278_cases_as_candidate_generation_input",
                "do_not_treat_unit_sales_ipo_tourism_freight_fleet_or_asset_sale_headline_as_green_alone",
                *ROUND278_GREEN_REQUIRED_FIELDS,
                *ROUND278_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
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


def round278_case_rows() -> tuple[dict[str, str], ...]:
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
            "reported_price_anchor": candidate.reported_price_anchor,
            "reported_return_anchor": candidate.reported_return_anchor,
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
        for candidate in ROUND278_CASE_CANDIDATES
    )


def round278_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND278_SCORE_ADJUSTMENTS)


def round278_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND278_SHADOW_WEIGHT_ROWS)


def round278_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND278_DEEP_SUB_ARCHETYPES)


def round278_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round278_price_validation": "true"} for field in ROUND278_PRICE_VALIDATION_FIELDS)


def round278_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round278_label": label, "canonical_archetype": canonical} for label, canonical in ROUND278_REQUIRED_TARGET_ALIASES.items())


def round278_summary() -> dict[str, int | bool | str]:
    cases = ROUND278_CASE_CANDIDATES
    return {
        "source_round": ROUND278_SOURCE_ROUND_PATH,
        "round_id": ROUND278_ANALYST_ROUND_ID,
        "large_sector": ROUND278_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "cyclical_success_count": sum(1 for case in cases if case.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "target_archetype_count": len(ROUND278_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND278_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND278_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round278_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND278_SOURCE_ROUND_PATH,
        "round_id": ROUND278_ANALYST_ROUND_ID,
        "large_sector": ROUND278_LARGE_SECTOR,
        "summary": round278_summary(),
        "target_aliases": dict(ROUND278_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND278_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND278_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND278_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND278_HARD_4C_GATES),
        "score_adjustments": list(round278_score_adjustment_rows()),
        "shadow_weights": list(round278_shadow_weight_rows()),
        "deep_sub_archetypes": list(round278_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND278_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round278_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_unit_sales_ipo_tourism_freight_fleet_or_asset_sale_headline_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round278_summary_markdown() -> str:
    summary = round278_summary()
    lines = [
        "# Round 278 R9 Loop 13 Mobility Transport Leisure Price Validation",
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
        f"- cyclical_success: {summary['cyclical_success_count']}",
        f"- event_premium: {summary['event_premium_count']}",
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
    for case in ROUND278_CASE_CANDIDATES:
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
            "- Hyundai Motor is Stage 2; Green needs OP margin after tariff, price pass-through and FCF.",
            "- Kia is the margin-break example: unit sales are not enough when tariff cost crushes OP.",
            "- Korean Air/Asiana is consolidation Stage 2 until integration synergy, fleet ROI and safety trust are visible.",
            "- Jeju Air is the hard 4C reference because fatal safety events break aviation trust.",
            "- HMM/Pan Ocean and China tourism are event/cycle paths until durability or booking-margin evidence appears.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round278_green_gate_review_markdown() -> str:
    lines = [
        "# Round 278 R9 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R9 Stage 3-Green is not `unit sales`, `IPO valuation`, `tourist flow`, `freight spike`, `fleet order`, or `asset-sale exploration`. It requires margin, ROI, safety trust, booking conversion, durability and FCF.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND278_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND278_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND278_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Kia US sales +5%` is not Green because tariff cost hit OP by 786B KRW.",
            "- `Lotte Tour +20%` is event premium until booking, occupancy, ADR and margin appear.",
            "- `Jeju Air fatal crash` is hard 4C because aviation safety trust is core evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round278_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 278 R9 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND278_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND278_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND278_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round278_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 278 R9 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, margin, booking, freight durability, safety remediation, ROI or FCF where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND278_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND278_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round278_r9_loop13_reports(
    output_directory: str | Path = ROUND278_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND278_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND278_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round278_case_records(), cases_path),
        "audit": _write_json(round278_audit_payload(), audit_path),
        "summary": output / "round278_r9_loop13_price_validation_summary.md",
        "case_matrix": output / "round278_r9_loop13_case_matrix.csv",
        "target_aliases": output / "round278_r9_loop13_target_aliases.csv",
        "score_adjustments": output / "round278_r9_loop13_score_adjustments.csv",
        "shadow_weights": output / "round278_r9_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round278_r9_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round278_r9_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round278_r9_loop13_green_gate_review.md",
        "price_validation_plan": output / "round278_r9_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round278_r9_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round278_summary_markdown(), encoding="utf-8")
    _write_csv(round278_case_rows(), paths["case_matrix"])
    _write_csv(round278_target_alias_rows(), paths["target_aliases"])
    _write_csv(round278_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round278_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round278_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round278_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round278_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round278_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round278_stage4b_4c_review_markdown(), encoding="utf-8")
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
