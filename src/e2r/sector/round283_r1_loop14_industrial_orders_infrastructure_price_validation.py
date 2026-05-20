"""Round-283 R1 Loop-14 industrial orders/infrastructure price-validation pack.

This module converts ``docs/round/round_283.md`` into calibration-only case
records and reports. It does not change production scoring, staging, or
candidate generation.

Easy example: a defense order headline is not Stage 3-Green by itself. It
becomes stronger only when tanks are delivered, revenue is recognized, margin
is visible, and cash collection/financing gates are still clean.
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


ROUND283_SOURCE_ROUND_PATH = "docs/round/round_283.md"
ROUND283_ANALYST_ROUND_ID = "round_211"
ROUND283_LARGE_SECTOR = "INDUSTRIALS_ORDERS_INFRASTRUCTURE"
ROUND283_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round283_r1_loop14_industrial_orders_infrastructure_price_validation"
ROUND283_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop14_round283.jsonl"
ROUND283_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round283_r1_loop14_industrial_orders_infrastructure_price_validation_audit.json"

ROUND283_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE": E2RArchetype.DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE.value,
    "GRID_EQUIPMENT_US_GROWTH_STAGE2": E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2.value,
    "TRANSFORMER_CAPACITY_EXPANSION_STAGE2": E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2.value,
    "SHIPBUILDING_MERGER_MASGA_4B": E2RArchetype.SHIPBUILDING_MERGER_MASGA_4B.value,
    "SHIPBUILDING_ORDER_CANCELLATION_HARD_4C": E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_HARD_4C.value,
    "DEFENSE_DILUTION_FALSE_POSITIVE": E2RArchetype.DEFENSE_DILUTION_FALSE_POSITIVE.value,
    "ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM": E2RArchetype.ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM.value,
    "INDUSTRIAL_SERVICE_IPO_OVERHEAT": E2RArchetype.INDUSTRIAL_SERVICE_IPO_OVERHEAT.value,
}

ROUND283_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "actual_delivery_revenue_confirmed",
    "backlog_to_revenue_conversion_confirmed",
    "order_margin_visibility_confirmed",
    "working_capital_control_confirmed",
    "local_production_execution_confirmed",
    "capacity_utilization_confirmed",
    "customer_financing_visibility_confirmed",
    "dilution_adjusted_EPS_confirmed",
    "contract_cancellation_risk_cleared",
    "aftermarket_IPO_demand_confirmed",
    "price_path_after_evidence",
)

ROUND283_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "order_headline_only",
    "customer_or_parent_name_only",
    "strategic_stake_only",
    "capacity_expansion_without_backlog",
    "IPO_first_day_pop_only",
    "merger_theme_without_synergy",
    "defence_order_expectation_without_funding",
    "dilutive_share_issue",
    "geopolitical_contract_execution_risk",
)

ROUND283_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "merger_MASGA_US_MRO_headline_10pct_plus_rally",
    "IPO_debut_40_100pct_pop",
    "strategic_stake_parent_name_event_before_revenue",
    "transformer_grid_capacity_investment_before_backlog",
    "defence_order_expectation_YTD_100pct_plus",
    "order_headline_day_5_10pct_rally",
)

ROUND283_HARD_4C_GATES: tuple[str, ...] = (
    "large_contract_cancellation",
    "shipowner_termination_or_arbitration",
    "sanctions_war_execution_impossible",
    "dilutive_share_issue_after_theme_rally",
    "FSS_revision_order_or_disclosure_quality_issue",
    "IPO_debut_failure_after_aggressive_pricing",
    "strategic_customer_program_cancellation",
    "backlog_not_converting_to_revenue_or_cash",
)

ROUND283_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "contract_value_anchor",
    "cancellation_value_anchor",
    "dilution_amount_anchor",
    "IPO_price_anchor",
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
class Round283ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round283ShadowWeightRow:
    archetype: E2RArchetype
    actual_delivery_revenue: int
    backlog_to_revenue_conversion: int
    order_margin_visibility: int
    working_capital_control: int
    local_production_execution: int
    capacity_utilization: int
    customer_financing_visibility: int
    dilution_adjusted_eps: int
    contract_cancellation_risk: int
    aftermarket_ipo_demand: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "actual_delivery_revenue": _signed(self.actual_delivery_revenue),
            "backlog_to_revenue_conversion": _signed(self.backlog_to_revenue_conversion),
            "order_margin_visibility": _signed(self.order_margin_visibility),
            "working_capital_control": _signed(self.working_capital_control),
            "local_production_execution": _signed(self.local_production_execution),
            "capacity_utilization": _signed(self.capacity_utilization),
            "customer_financing_visibility": _signed(self.customer_financing_visibility),
            "dilution_adjusted_EPS": _signed(self.dilution_adjusted_eps),
            "contract_cancellation_risk": _signed(self.contract_cancellation_risk),
            "aftermarket_IPO_demand": _signed(self.aftermarket_ipo_demand),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round283DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round283CaseCandidate:
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


ROUND283_SCORE_ADJUSTMENTS: tuple[Round283ScoreAdjustment, ...] = (
    Round283ScoreAdjustment("actual_delivery_revenue", 5, "raise", "수주가 실제 납품과 매출 인식으로 닫혀야 Stage 3 후보가 된다."),
    Round283ScoreAdjustment("backlog_to_revenue_conversion", 5, "raise", "수주잔고가 매출로 내려오는 경로를 더 강하게 본다."),
    Round283ScoreAdjustment("order_margin_visibility", 5, "raise", "대형 수주는 원가율과 OP margin이 확인되어야 한다."),
    Round283ScoreAdjustment("working_capital_control", 5, "raise", "운전자본·미청구·현금회수 문제가 없을 때만 수주 품질을 인정한다."),
    Round283ScoreAdjustment("local_production_execution", 4, "raise", "방산 현지생산 조건은 납품 일정과 마진의 핵심 gate다."),
    Round283ScoreAdjustment("capacity_utilization", 5, "raise", "증설은 가동률과 주문이 같이 있어야 EPS/FCF로 연결된다."),
    Round283ScoreAdjustment("customer_financing_visibility", 4, "raise", "정부·고객 financing이 확인되지 않은 주문 기대는 제한한다."),
    Round283ScoreAdjustment("dilution_adjusted_EPS", 5, "raise", "증자 이후 EPS 체급이 유지되는지를 별도 확인한다."),
    Round283ScoreAdjustment("contract_cancellation_risk", 5, "raise", "수주 산업재는 계약취소·제재·arbitration 리스크를 hard gate로 본다."),
    Round283ScoreAdjustment("aftermarket_IPO_demand", 4, "raise", "IPO 첫날 수요보다 상장 후 수요와 실적 지속성이 중요하다."),
    Round283ScoreAdjustment("order_headline_only", -5, "lower", "수주했다는 말만으로 Green을 만들지 않는다."),
    Round283ScoreAdjustment("customer_or_parent_name_only", -5, "lower", "유명 고객/모회사 이름은 납품·매출·마진의 대체물이 아니다."),
    Round283ScoreAdjustment("strategic_stake_only", -5, "lower", "전략적 지분투자는 로봇 출하량과 마진이 아니다."),
    Round283ScoreAdjustment("capacity_expansion_without_backlog", -5, "lower", "증설만 있고 수주잔고와 가동률이 없으면 제한한다."),
    Round283ScoreAdjustment("IPO_first_day_pop_only", -5, "lower", "IPO 첫날 급등은 4B-watch이지 Stage 3 근거가 아니다."),
    Round283ScoreAdjustment("merger_theme_without_synergy", -5, "lower", "합병/MASGA 테마는 실제 주문·시너지 전에는 event premium이다."),
    Round283ScoreAdjustment("defence_order_expectation_without_funding", -4, "lower", "방산 기대는 정부 예산·financing·납품 일정이 필요하다."),
    Round283ScoreAdjustment("dilutive_share_issue", -5, "lower", "테마 랠리 뒤 희석 증자는 EPS/FCF 경로를 훼손한다."),
    Round283ScoreAdjustment("geopolitical_contract_execution_risk", -5, "lower", "전쟁·제재·선주 리스크가 있으면 backlog를 그대로 인정하지 않는다."),
)


ROUND283_SHADOW_WEIGHT_ROWS: tuple[Round283ShadowWeightRow, ...] = (
    Round283ShadowWeightRow(E2RArchetype.DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE, 5, 5, 5, 4, 4, 3, 4, 3, 3, 1, -3, 4, 4, "Hyundai Rotem shows delivery/revenue/OP evidence can support a Stage 3 candidate."),
    Round283ShadowWeightRow(E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2, 3, 5, 5, 5, 2, 5, 2, 2, 3, 0, -5, 5, 3, "LS Electric needs backlog and margin confirmation after estimate-upgrade price failure."),
    Round283ShadowWeightRow(E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2, 3, 5, 5, 5, 2, 5, 2, 2, 3, 0, -4, 5, 3, "Transformer shortage/capacity expansion is Stage 2 until utilization and ASP/margin confirm."),
    Round283ShadowWeightRow(E2RArchetype.SHIPBUILDING_MERGER_MASGA_4B, 3, 4, 5, 5, 3, 5, 3, 3, 4, 1, -5, 5, 4, "HD HHI/Mipo merger needs US orders, integration synergy and margin proof."),
    Round283ShadowWeightRow(E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_HARD_4C, 0, 5, 5, 5, 2, 3, 4, 2, 5, 0, 0, 4, 5, "Samsung Heavy cancellation proves backlog execution risk is a hard gate."),
    Round283ShadowWeightRow(E2RArchetype.DEFENSE_DILUTION_FALSE_POSITIVE, 4, 5, 5, 4, 4, 3, 4, 5, 3, 1, -5, 5, 4, "Hanwha Aerospace shows defense order cycles must be dilution-adjusted."),
    Round283ShadowWeightRow(E2RArchetype.ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM, 1, 2, 4, 3, 2, 4, 1, 2, 2, 0, -5, 5, 3, "Strategic stake is not robot shipment/margin Green."),
    Round283ShadowWeightRow(E2RArchetype.INDUSTRIAL_SERVICE_IPO_OVERHEAT, 4, 4, 5, 4, 1, 4, 1, 3, 2, 5, -5, 5, 3, "HD Hyundai Marine needs aftermarket durability and lock-up/PE exit gates after +97% debut."),
)


ROUND283_DEEP_SUB_ARCHETYPES: tuple[Round283DeepSubArchetype, ...] = (
    Round283DeepSubArchetype("Defense export delivery", E2RArchetype.DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE, ("Hyundai Rotem", "K2 Poland", "18 tanks delivered", "270B KRW Q1 revenue", "59.1B KRW OP estimate", "$6.5B second batch")),
    Round283DeepSubArchetype("US grid equipment", E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2, ("LS Electric", "US revenue share 20%", "target +87%", "shares -5.4%", "backlog/margin gate")),
    Round283DeepSubArchetype("Transformer capacity", E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2, ("Hyosung Heavy", "Hyosung HICO", "GSU demand +274%", "delivery delay 143 weeks", "$157M Memphis expansion")),
    Round283DeepSubArchetype("Shipbuilding MASGA merger", E2RArchetype.SHIPBUILDING_MERGER_MASGA_4B, ("HD Hyundai Heavy", "HD Hyundai Mipo", "MASGA", "+11.3%", "+14.6%", "exchange ratio 1.04059146")),
    Round283DeepSubArchetype("Shipbuilding cancellation", E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_HARD_4C, ("Samsung Heavy", "Zvezda", "4.85T KRW cancellation", "$3.54B", "arbitration", "sanctions risk")),
    Round283DeepSubArchetype("Defense dilution", E2RArchetype.DEFENSE_DILUTION_FALSE_POSITIVE, ("Hanwha Aerospace", "3.6T KRW share sale", "-13%", "FSS revised filing", "2.3T KRW rights offering")),
    Round283DeepSubArchetype("Robotics strategic stake", E2RArchetype.ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM, ("Rainbow Robotics", "Samsung largest shareholder", "267B KRW stake", "Future Robotics Office", "shipment/margin missing")),
    Round283DeepSubArchetype("Industrial service IPO", E2RArchetype.INDUSTRIAL_SERVICE_IPO_OVERHEAT, ("HD Hyundai Marine Solution", "IPO 83,400 KRW", "close 163,900 KRW", "+96.5%", "lock-up/aftermarket gate")),
)


ROUND283_CASE_CANDIDATES: tuple[Round283CaseCandidate, ...] = (
    Round283CaseCandidate(
        case_id="r1_loop14_hyundai_rotem_k2_poland_delivery_stage3_candidate",
        symbol="064350",
        company_name="Hyundai Rotem K2 Poland delivery",
        primary_archetype=E2RArchetype.DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE,
        secondary_archetypes=(E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, E2RArchetype.RAIL_EXPORT_MEGA_ORDER_STAGE2),
        case_type="success_candidate",
        round_case_type="aligned_partial Stage 3 candidate",
        stage1_date=date(2022, 8, 1),
        stage2_date=date(2025, 8, 1),
        stage3_date=date(2024, 4, 1),
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="delivery_revenue_OP_estimate_and_price_reaction_support_stage3_candidate_but_financing_local_production_margin_gates_remain",
        stage4b_status="4B-watch/rearmament-overheat",
        hard_4c_confirmed=False,
        evidence_fields=("18_K2_tanks_shipped_to_Poland", "Q1_revenue_270bn_krw", "Q1_OP_estimate_59_1bn_krw", "OP_estimate_growth_85pct", "second_contract_180_tanks_6_5bn_usd"),
        red_flag_fields=("local_production_execution_unconfirmed", "customer_financing_visibility_unconfirmed", "order_margin_gate_remains"),
        price_data_source="WSJ event price anchor; Reuters Poland second-contract anchor",
        reported_price_anchor="41,300 KRW, +9.3%, KOSPI -0.3%",
        reported_return_anchor="Delivery/revenue/OP estimate and price reaction align, but local production and financing remain gates.",
        event_mfe_pct=9.3,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=41300,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stage3_price_krw": 41300, "kospi_same_context_pct": -0.3, "relative_outperformance_pp": 9.6, "q1_revenue_from_18_k2_shipments_krw_bn": 270, "q1_op_estimate_krw_bn": 59.1, "op_estimate_growth_pct": 85, "target_price_krw": 47500, "target_upside_from_stage3_price_pct": 15.0, "second_contract_value_usd_bn": 6.5, "second_contract_tanks": 180, "poland_local_production_units": 61, "first_delivery_second_batch": 2026, "polish_production_period": "2028-2030"},
        score_price_alignment="aligned",
        round_alignment_label="aligned_partial",
        rerating_result="true_rerating",
        round_rerating_label="defense_export_delivery_stage3_candidate",
        stage_failure_type="yellow_success",
        round_stage_failure_label="local_production_financing_margin_gate_remains",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Delivery/revenue/OP evidence supports a Stage 3 candidate; financing, local production and margin remain gates.",
    ),
    Round283CaseCandidate(
        case_id="r1_loop14_ls_electric_us_grid_growth_price_failed",
        symbol="010120",
        company_name="LS Electric US grid growth",
        primary_archetype=E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2,
        secondary_archetypes=(E2RArchetype.POWER_EQUIPMENT_EXPORT_US_GRID, E2RArchetype.GRID_POWER_EQUIPMENT_AI_DATACENTER),
        case_type="failed_rerating",
        round_case_type="evidence_good_but_price_failed",
        stage1_date=date(2024, 7, 1),
        stage2_date=date(2024, 7, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="estimate_and_target_upgrade_failed_event_price_confirmation",
        stage4b_status="watch/grid-data-center-theme-before-backlog",
        hard_4c_confirmed=False,
        evidence_fields=("US_revenue_share_expected_20pct", "target_price_raise_87pct", "2024_2026_revenue_forecast_raise_4_22pct"),
        red_flag_fields=("estimate_upgrade_not_price_green", "actual_backlog_unconfirmed", "margin_working_capital_unconfirmed"),
        price_data_source="MarketWatch / Dow Jones event anchor",
        reported_price_anchor="208,500 KRW, -5.4% despite target 280,000 KRW",
        reported_return_anchor="Good US growth evidence did not validate Green in price; backlog and margin required.",
        event_mfe_pct=None,
        event_mae_pct=-5.4,
        stage1_price_anchor=None,
        stage2_price_anchor=208500,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_price_krw": 208500, "us_revenue_share_2022_pct": "<5", "us_revenue_share_2024_expected_pct": 20, "revenue_forecast_raise_2024_2026_pct_range": "4-22", "target_price_krw": 280000, "target_price_raise_pct": 87, "target_upside_from_event_price_pct": 34.3, "green_conditions": ["actual_backlog", "capacity", "margin", "working_capital"]},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        round_rerating_label="grid_equipment_US_growth_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="estimate_upgrade_not_price_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="US grid growth is Stage 2 evidence, but actual backlog, capacity, margin and working capital must close.",
    ),
    Round283CaseCandidate(
        case_id="r1_loop14_hyosung_heavy_hico_transformer_capacity",
        symbol="298040",
        company_name="Hyosung Heavy / Hyosung HICO transformer capacity",
        primary_archetype=E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2,
        secondary_archetypes=(E2RArchetype.GRID_TRANSFORMER_SHORTAGE, E2RArchetype.TRANSFORMER_CAPACITY_BOTTLENECK),
        case_type="success_candidate",
        round_case_type="success_candidate, price unavailable",
        stage1_date=date(2025, 12, 2),
        stage2_date=date(2025, 12, 2),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="capacity_expansion_shortage_stage2_not_green_without_backlog_utilization_margin",
        stage4b_status="watch/capacity-before-backlog",
        hard_4c_confirmed=False,
        evidence_fields=("GSU_transformer_demand_growth_274pct", "GSU_delivery_delay_143_weeks", "Hyosung_HICO_Memphis_expansion_157mn_usd", "US_top_transformer_importer", "price_hikes_expected_until_2030"),
        red_flag_fields=("direct_stock_price_anchor_unavailable", "order_backlog_unconfirmed", "capacity_utilization_unconfirmed", "ASP_margin_unconfirmed"),
        price_data_source="Reuters Events industry-capacity anchor",
        reported_price_anchor="No direct listed stock price anchor found after deep search.",
        reported_return_anchor="Transformer shortage and capacity expansion are strong Stage 2 evidence, not Green alone.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"gsu_transformer_demand_growth_since_2019_pct": 274, "gsu_delivery_delay_weeks": 143, "hyosung_hico_memphis_expansion_usd_mn": 157, "us_transformer_importer_status": "top_transformer_importer", "price_hike_expected_until": 2030, "direct_stock_price_anchor": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_price_data_unavailable",
        rerating_result="unknown",
        round_rerating_label="transformer_capacity_expansion_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="capacity_expansion_not_backlog_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Capacity expansion and shortage are Stage 2; backlog, utilization, ASP/margin and price path must be backfilled.",
    ),
    Round283CaseCandidate(
        case_id="r1_loop14_hd_hhi_mipo_merger_masga_4b",
        symbol="329180/010620",
        company_name="HD Hyundai Heavy / HD Hyundai Mipo merger MASGA",
        primary_archetype=E2RArchetype.SHIPBUILDING_MERGER_MASGA_4B,
        secondary_archetypes=(E2RArchetype.SHIPBUILDING_US_POLICY_MASGA, E2RArchetype.US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION),
        case_type="4b_watch",
        round_case_type="event premium + 4B-watch",
        stage1_date=date(2025, 8, 27),
        stage2_date=date(2025, 8, 27),
        stage3_date=None,
        stage4b_date=date(2025, 8, 27),
        stage4c_date=None,
        stage3_decision="merger_MASGA_theme_not_order_margin_green_before_US_order_and_synergy",
        stage4b_status="4B-watch/MASGA-merger-event-premium",
        hard_4c_confirmed=False,
        evidence_fields=("HD_HHI_Mipo_merger", "MASGA_US_Korea_shipbuilding_cooperation", "exchange_ratio_1_04059146", "merged_company_target_2025_12"),
        red_flag_fields=("merger_theme_without_synergy", "actual_US_order_unconfirmed", "integration_synergy_unconfirmed", "dock_labor_margin_gate"),
        price_data_source="Reuters merger event anchor",
        reported_price_anchor="HD HHI +11.3%; HD Hyundai Mipo +14.6%; record highs",
        reported_return_anchor="Merger/MASGA event premium moved before actual US order and integration synergy.",
        event_mfe_pct=14.6,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hd_hyundai_heavy_event_mfe_pct": 11.3, "hd_hyundai_mipo_event_mfe_pct": 14.6, "exchange_ratio_mipo_to_hhi": 1.04059146, "merged_company_launch_target": "2025-12", "theme": "MASGA / US-Korea shipbuilding cooperation", "actual_us_order_confirmed": False, "integration_synergy_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="shipbuilding_merger_MASGA_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="merger_theme_not_order_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Merger/MASGA can be Stage 2 and 4B-watch, not Green before funded orders and synergy.",
    ),
    Round283CaseCandidate(
        case_id="r1_loop14_samsung_heavy_zvezda_cancellation_hard_4c",
        symbol="010140",
        company_name="Samsung Heavy Zvezda cancellation",
        primary_archetype=E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_HARD_4C,
        secondary_archetypes=(E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_4C, E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION),
        case_type="4c_thesis_break",
        round_case_type="hard 4C / order cancellation",
        stage1_date=date(2020, 1, 1),
        stage2_date=date(2020, 1, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 6, 18),
        stage3_decision="backlog_that_cannot_execute_is_hard_4c_not_green",
        stage4b_status="hard-4C/order-cancellation",
        hard_4c_confirmed=True,
        evidence_fields=("Zvezda_icebreaker_orders", "cancelled_contract_value_4_85trn_krw", "cancelled_contract_value_3_54bn_usd", "10_icebreaker_LNG_carriers", "7_icebreaker_shuttle_tankers"),
        red_flag_fields=("large_contract_cancellation", "shipowner_termination_or_arbitration", "sanctions_war_execution_impossible", "geopolitical_contract_execution_risk"),
        price_data_source="Reuters contract-cancellation anchor",
        reported_price_anchor="4.85T KRW / $3.54B cancelled contract value anchor",
        reported_return_anchor="Large backlog was cancelled; execution risk breaks the thesis.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"cancelled_contract_value_krw_trn": 4.85, "cancelled_contract_value_usd_bn": 3.54, "icebreaker_lng_carriers": 10, "icebreaker_shuttle_tankers": 7, "zvezda_unilateral_termination_notice": "2024-06", "samsung_arbitration_request": "2024-07", "risk_cause": "Russia-Ukraine war / execution uncertainty / shipowner termination"},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="shipbuilding_order_cancellation_hard_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="backlog_execution_failure",
        price_validation_status="contract_cancellation_value_anchor_not_full_ohlc",
        notes="Backlog execution failed; large cancellation and sanctions/arbitration risk are hard 4C gates.",
    ),
    Round283CaseCandidate(
        case_id="r1_loop14_hanwha_aerospace_share_sale_dilution",
        symbol="012450",
        company_name="Hanwha Aerospace share-sale dilution",
        primary_archetype=E2RArchetype.DEFENSE_DILUTION_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.DEFENSE_CAPITAL_RAISE_DILUTION, E2RArchetype.GOVERNANCE_DILUTION_EVENT),
        case_type="4b_watch",
        round_case_type="false_positive_score + 4B-watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 4, 18),
        stage3_date=None,
        stage4b_date=date(2025, 3, 21),
        stage4c_date=date(2025, 3, 27),
        stage3_decision="defense_order_growth_is_not_green_if_dilution_and_disclosure_quality_are_unclear",
        stage4b_status="4B-watch/4C-watch/dilution-after-theme-rally",
        hard_4c_confirmed=False,
        evidence_fields=("defense_export_rally", "revised_affiliate_issue_1_3trn_krw", "separate_rights_offering_2_3trn_krw", "revised_issue_price_758000_krw"),
        red_flag_fields=("dilutive_share_issue_after_theme_rally", "FSS_revision_order_or_disclosure_quality_issue", "initial_share_sale_3_6trn_krw", "event_mae_minus_13pct"),
        price_data_source="FT / Reuters share-sale and FSS revision anchors",
        reported_price_anchor="-13% event move; 3.6T KRW share-sale plan; issue price 605,000 KRW",
        reported_return_anchor="Defense export cycle was capped by dilution and filing-quality gates.",
        event_mfe_pct=None,
        event_mae_pct=-13.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"initial_share_sale_krw_trn": 3.6, "initial_share_sale_usd_bn": 2.5, "planned_new_shares_mn": 6, "initial_issue_price_krw": 605000, "discount_to_previous_close_pct": -16, "stock_ytd_context": "more_than_doubled_before_share_sale", "revised_affiliate_issue_krw_trn": 1.3, "revised_affiliate_issue_price_krw": 758000, "separate_rights_offering_krw_trn": 2.3},
        score_price_alignment="false_positive_score",
        round_alignment_label="false_positive_score",
        rerating_result="no_rerating",
        round_rerating_label="defence_export_theme_dilution_gate",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="order_growth_not_green_if_dilution_unclear",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Defense order cycle must be dilution-adjusted; FSS filing-quality gate remains part of RedTeam.",
    ),
    Round283CaseCandidate(
        case_id="r1_loop14_rainbow_robotics_samsung_stake_event",
        symbol="277810",
        company_name="Rainbow Robotics Samsung stake event",
        primary_archetype=E2RArchetype.ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION, E2RArchetype.ROBOTICS_FACTORY_AUTOMATION),
        case_type="event_premium",
        round_case_type="robotics event premium",
        stage1_date=date(2024, 12, 30),
        stage2_date=date(2024, 12, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="strategic_stake_is_not_robot_revenue_green",
        stage4b_status="watch/strategic-stake-not-revenue",
        hard_4c_confirmed=False,
        evidence_fields=("Samsung_largest_shareholder", "new_samsung_stake_267bn_krw", "new_samsung_stake_181mn_usd", "Future_Robotics_Office_created", "prior_stake_14_71pct"),
        red_flag_fields=("strategic_stake_only", "actual_robot_shipments_unconfirmed", "gross_margin_unconfirmed", "repeat_demand_unconfirmed"),
        price_data_source="Reuters strategic-stake anchor",
        reported_price_anchor="Direct event price unavailable after deep search; 267B KRW strategic stake anchor stored.",
        reported_return_anchor="Samsung stake is strategic Stage 2, not shipment/margin Green.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"new_samsung_stake_investment_krw_bn": 267, "new_samsung_stake_investment_usd_mn": 181, "samsung_prior_stake_pct": 14.71, "future_robotics_office_created": True, "actual_robot_shipments_confirmed": False, "gross_margin_confirmed": False, "direct_event_price": "price_data_unavailable_after_deep_search"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium",
        rerating_result="event_premium",
        round_rerating_label="robotics_strategic_stake_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="strategic_stake_not_robot_revenue_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Strategic stake is Stage 2 optionality; shipment, ASP, deployment, margin and repeat demand are Green gates.",
    ),
    Round283CaseCandidate(
        case_id="r1_loop14_hd_hyundai_marine_ipo_overheat",
        symbol="443060",
        company_name="HD Hyundai Marine Solution IPO overheat",
        primary_archetype=E2RArchetype.INDUSTRIAL_SERVICE_IPO_OVERHEAT,
        secondary_archetypes=(E2RArchetype.MARINE_MRO_RECURRING_SERVICE, E2RArchetype.IPO_EVENT_PREMIUM),
        case_type="overheat",
        round_case_type="industrial-service IPO overheat",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 5, 8),
        stage3_date=None,
        stage4b_date=date(2024, 5, 8),
        stage4c_date=None,
        stage3_decision="first_day_IPO_pop_is_4B_watch_not_durable_stage3",
        stage4b_status="4B-watch/IPO-first-day-pop",
        hard_4c_confirmed=False,
        evidence_fields=("marine_after_sales_retrofit_service", "IPO_price_83400_krw", "2023_revenue_1_43trn_krw", "2023_OP_201_47bn_krw", "OP_growth_42pct"),
        red_flag_fields=("IPO_first_day_pop_only", "lockup_PE_exit_pressure_unconfirmed", "aftermarket_demand_unconfirmed", "service_margin_durability_unconfirmed"),
        price_data_source="WSJ / Reuters IPO debut anchors",
        reported_price_anchor="IPO 83,400 KRW to close 163,900 KRW, +96.5%",
        reported_return_anchor="Strong service business, but first-day doubling is 4B-watch until durability clears.",
        event_mfe_pct=96.5,
        event_mae_pct=None,
        stage1_price_anchor=83400,
        stage2_price_anchor=163900,
        stage3_price_anchor=None,
        stage4b_price_anchor=163900,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_price_krw": 83400, "close_price_krw": 163900, "debut_mfe_pct": 96.5, "ipo_raise_krw_bn": 742.26, "ipo_raise_usd_mn": 546, "shares_sold_mn": 8.9, "market_cap_close_krw_trn": 7.29, "market_cap_close_usd_bn": 5.36, "revenue_2023_krw_trn": 1.43, "op_2023_krw_bn": 201.47, "net_profit_2023_krw_bn": 151.12, "revenue_growth_2023_pct": 7.2, "op_growth_2023_pct": 42, "net_profit_growth_2023_pct": 44},
        score_price_alignment="false_positive_score",
        round_alignment_label="success_candidate_but_overheat",
        rerating_result="event_premium",
        round_rerating_label="industrial_service_IPO_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="first_day_IPO_pop_not_durable_stage3",
        price_validation_status="reported_ipo_anchor_not_full_ohlc",
        notes="Good industrial-service business, but +97% IPO debut is a 4B-watch until post-IPO earnings durability and lock-up/PE exit pressure clear.",
    ),
)


def round283_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND283_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND283_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round283 R1 Loop-14 industrial orders/infrastructure price-validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=candidate.evidence_fields if candidate.stage3_date else (),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("ipo", "rally", "merger", "theme", "dilution", "stake", "premium", "expectation"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("cancellation", "termination", "arbitration", "sanctions", "dilution", "revision", "4c", "risk"))),
            must_have_fields=ROUND283_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type != "structural_success" else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND283_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "hard_4c_confirmed_true_for_samsung_heavy_zvezda",
                "do_not_use_round283_cases_as_candidate_generation_input",
                "do_not_treat_order_grid_defense_shipbuilding_robotics_or_IPO_headlines_as_green",
                *ROUND283_GREEN_REQUIRED_FIELDS,
                *ROUND283_GREEN_FORBIDDEN_PATTERNS,
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
                    or candidate.stage1_price_anchor is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.84 if candidate.price_validation_status != "price_data_unavailable_after_deep_search" else 0.72,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round283_case_rows() -> tuple[dict[str, str], ...]:
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
            "stage1_price_anchor": _float_text(candidate.stage1_price_anchor),
            "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
            "stage3_price_anchor": _float_text(candidate.stage3_price_anchor),
            "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
            "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
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
        for candidate in ROUND283_CASE_CANDIDATES
    )


def round283_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND283_SCORE_ADJUSTMENTS)


def round283_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND283_SHADOW_WEIGHT_ROWS)


def round283_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND283_DEEP_SUB_ARCHETYPES)


def round283_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round283_price_validation": "true"} for field in ROUND283_PRICE_VALIDATION_FIELDS)


def round283_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round283_label": label, "canonical_archetype": canonical} for label, canonical in ROUND283_REQUIRED_TARGET_ALIASES.items())


def round283_summary() -> dict[str, int | bool | str]:
    cases = ROUND283_CASE_CANDIDATES
    return {
        "source_round": ROUND283_SOURCE_ROUND_PATH,
        "round_id": ROUND283_ANALYST_ROUND_ID,
        "large_sector": ROUND283_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "event_premium_or_result_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "aligned_count": sum(1 for case in cases if case.score_price_alignment == "aligned"),
        "target_archetype_count": len(ROUND283_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND283_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND283_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round283_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND283_SOURCE_ROUND_PATH,
        "round_id": ROUND283_ANALYST_ROUND_ID,
        "large_sector": ROUND283_LARGE_SECTOR,
        "summary": round283_summary(),
        "target_aliases": dict(ROUND283_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND283_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND283_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND283_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND283_HARD_4C_GATES),
        "score_adjustments": list(round283_score_adjustment_rows()),
        "shadow_weights": list(round283_shadow_weight_rows()),
        "deep_sub_archetypes": list(round283_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND283_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round283_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_order_grid_defense_shipbuilding_robotics_or_IPO_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round283_summary_markdown() -> str:
    summary = round283_summary()
    lines = [
        "# Round 283 R1 Loop 14 Industrials Orders Infrastructure Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- Stage 3 dated candidates: {summary['stage3_case_count']}",
        f"- stage4b_watch: {summary['stage4b_watch_count']}",
        f"- stage4c_watch: {summary['stage4c_watch_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND283_CASE_CANDIDATES:
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
            "- Hyundai Rotem is the aligned partial Stage 3 candidate because delivery, revenue, OP estimate and price reaction line up.",
            "- LS Electric and Hyosung Heavy/HICO are Stage 2 lessons: grid evidence must still close into backlog, utilization, margin and price path.",
            "- HD HHI/Mipo, Rainbow Robotics and HD Hyundai Marine are event-premium/4B-watch lessons before revenue or aftermarket proof.",
            "- Samsung Heavy/Zvezda is the hard 4C lesson: cancelled backlog is not structural visibility.",
            "- Hanwha Aerospace shows defense order growth must be checked against dilution-adjusted EPS and filing quality.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round283_green_gate_review_markdown() -> str:
    lines = [
        "# Round 283 R1 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R1 Stage 3-Green is not `order`, `defense`, `grid`, `shipbuilding`, `robotics`, or `IPO` as a label. It requires delivery, revenue recognition, margin, working capital, capacity utilization, financing, dilution-adjusted EPS, and price validation.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND283_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND283_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND283_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `K2 export` is stronger when delivered tanks are recognized in revenue, not only when a contract is announced.",
            "- `US grid demand` is Stage 2 until backlog, capacity utilization and margin are confirmed.",
            "- `IPO +97% debut` is a 4B-watch signal until aftermarket demand and earnings durability are proven.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round283_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 283 R1 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND283_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND283_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND283_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round283_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 283 R1 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, full MFE/MAE, order margin, local production execution, financing, shipment, IPO aftermarket demand, or backlog conversion where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND283_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND283_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round283_r1_loop14_reports(
    output_directory: str | Path = ROUND283_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND283_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND283_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round283_case_records(), cases_path),
        "audit": _write_json(round283_audit_payload(), audit_path),
        "summary": output / "round283_r1_loop14_price_validation_summary.md",
        "case_matrix": output / "round283_r1_loop14_case_matrix.csv",
        "target_aliases": output / "round283_r1_loop14_target_aliases.csv",
        "score_adjustments": output / "round283_r1_loop14_score_adjustments.csv",
        "shadow_weights": output / "round283_r1_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round283_r1_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round283_r1_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round283_r1_loop14_green_gate_review.md",
        "price_validation_plan": output / "round283_r1_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round283_r1_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round283_summary_markdown(), encoding="utf-8")
    _write_csv(round283_case_rows(), paths["case_matrix"])
    _write_csv(round283_target_alias_rows(), paths["target_aliases"])
    _write_csv(round283_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round283_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round283_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round283_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round283_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round283_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round283_stage4b_4c_review_markdown(), encoding="utf-8")
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


__all__ = [
    "ROUND283_CASE_CANDIDATES",
    "ROUND283_GREEN_FORBIDDEN_PATTERNS",
    "ROUND283_GREEN_REQUIRED_FIELDS",
    "ROUND283_HARD_4C_GATES",
    "ROUND283_LARGE_SECTOR",
    "ROUND283_PRICE_VALIDATION_FIELDS",
    "ROUND283_REQUIRED_TARGET_ALIASES",
    "ROUND283_SHADOW_WEIGHT_ROWS",
    "ROUND283_STAGE4B_WATCH_TRIGGERS",
    "render_round283_green_gate_review_markdown",
    "render_round283_stage4b_4c_review_markdown",
    "round283_audit_payload",
    "round283_case_records",
    "round283_case_rows",
    "round283_deep_sub_archetype_rows",
    "round283_shadow_weight_rows",
    "round283_summary",
    "write_round283_r1_loop14_reports",
]
