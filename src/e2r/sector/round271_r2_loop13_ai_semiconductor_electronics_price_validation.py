"""Round-271 R2 Loop-13 AI/semiconductor/electronics validation pack.

Round 271 converts ``docs/round/round_271.md`` into structured,
calibration-only case records. It does not change production scoring.

Easy example: buying 260,000 Nvidia Blackwell chips is not automatically
Stage 3 for Korean listed companies. R2 Green needs customer qualification,
mass production, repeat orders, margin, FCF and export-control/labor gates to
clear.
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


ROUND271_SOURCE_ROUND_PATH = "docs/round/round_271.md"
ROUND271_ANALYST_ROUND_ID = "round_199"
ROUND271_LARGE_SECTOR = "AI_SEMICONDUCTOR_ELECTRONICS"
ROUND271_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round271_r2_loop13_ai_semiconductor_electronics_price_validation"
ROUND271_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop13_round271.jsonl"
ROUND271_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round271_r2_loop13_ai_semiconductor_electronics_price_validation_audit.json"

ROUND271_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B": E2RArchetype.HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B.value,
    "SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C": E2RArchetype.SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C.value,
    "HBM_EQUIPMENT_CARVEOUT_NOT_GREEN": E2RArchetype.HBM_EQUIPMENT_CARVEOUT_NOT_GREEN.value,
    "AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2": E2RArchetype.AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2.value,
    "SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT": E2RArchetype.SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT.value,
    "STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN": E2RArchetype.STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN.value,
    "NVIDIA_BLACKWELL_DOMESTIC_AI_INFRA_STAGE2": E2RArchetype.NVIDIA_BLACKWELL_DOMESTIC_AI_INFRA_STAGE2.value,
    "CHINA_FAB_EXPORT_CONTROL_4C_WATCH": E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH.value,
}

ROUND271_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "customer_qualification_confirmed",
    "mass_production_or_shipment_started",
    "equipment_or_material_order_backlog_confirmed",
    "delivered_order_book_or_recurring_order_confirmed",
    "op_gross_margin_fcf_improvement_confirmed",
    "capex_roi_or_utilization_confirmed",
    "china_fab_export_control_risk_passed",
    "labor_production_disruption_risk_passed",
    "price_path_after_evidence",
)

ROUND271_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ai_keyword_only",
    "hbm_rumor_only",
    "foundry_policy_only",
    "ipo_oversubscription_only",
    "unlisted_merger_only",
    "strategic_stake_only",
    "blackwell_chip_consumption_only",
    "equipment_carveout_only",
    "china_fab_exposure_unresolved",
    "labor_strike_unresolved",
)

ROUND271_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "hbm_ai_memory_one_year_3x_to_5x",
    "market_cap_one_trillion_milestone_headline",
    "ipo_oversubscription_100x_to_600x",
    "pe_40x_before_listed_delivery_record",
    "spinoff_rumor_plus_15pct_confirmation_sell_the_news",
    "ai_chip_merger_or_nvidia_infra_basket_rally_before_revenue",
    "policy_foundry_headline_basket_priced_before_operator_utilization",
)

ROUND271_HARD_4C_GATES: tuple[str, ...] = (
    "hbm_qualification_failure",
    "customer_shipment_delay",
    "ai_chip_order_cancellation",
    "mass_production_failure",
    "china_fab_equipment_license_denial",
    "export_control_escalation",
    "labor_strike_causing_production_halt",
    "equipment_order_cancellation",
    "ipo_lockup_or_delivery_failure",
    "foundry_utilization_failure",
)

ROUND271_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_anchor",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "mfe_30d",
    "mae_30d",
    "earnings_anchor",
    "policy_capex_anchor",
    "ipo_valuation_anchor",
    "export_control_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round271ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round271ShadowWeightRow:
    archetype: E2RArchetype
    hbm_volume_certification: int
    customer_qualification: int
    mass_production_readiness: int
    equipment_order_backlog: int
    delivered_order_book: int
    gross_margin_visibility: int
    op_revision_quality: int
    labor_operational_resilience: int
    china_fab_export_control_clearance: int
    capex_roi_bridge: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "hbm_volume_certification": _signed(self.hbm_volume_certification),
            "customer_qualification": _signed(self.customer_qualification),
            "mass_production_readiness": _signed(self.mass_production_readiness),
            "equipment_order_backlog": _signed(self.equipment_order_backlog),
            "delivered_order_book": _signed(self.delivered_order_book),
            "gross_margin_visibility": _signed(self.gross_margin_visibility),
            "op_revision_quality": _signed(self.op_revision_quality),
            "labor_operational_resilience": _signed(self.labor_operational_resilience),
            "china_fab_export_control_clearance": _signed(self.china_fab_export_control_clearance),
            "capex_roi_bridge": _signed(self.capex_roi_bridge),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round271DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round271CaseCandidate:
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
    peak_return_from_stage3_pct: float | None
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


ROUND271_SCORE_ADJUSTMENTS: tuple[Round271ScoreAdjustment, ...] = (
    Round271ScoreAdjustment("HBM_volume_certification", 5, "raise", "HBM은 고객 인증과 출하량이 확인될 때 강하게 본다."),
    Round271ScoreAdjustment("customer_qualification", 5, "raise", "AI 반도체는 고객 qualification이 Stage 2와 Stage 3를 가른다."),
    Round271ScoreAdjustment("mass_production_readiness", 5, "raise", "양산 준비와 shipment가 keyword보다 중요하다."),
    Round271ScoreAdjustment("equipment_order_backlog", 5, "raise", "장비주는 실제 order backlog가 있어야 한다."),
    Round271ScoreAdjustment("delivered_order_book", 5, "raise", "배송·검수된 order book이 있어야 매출 경로가 닫힌다."),
    Round271ScoreAdjustment("gross_margin_visibility", 5, "raise", "고마진 약속보다 실제 gross margin visibility가 중요하다."),
    Round271ScoreAdjustment("OP_revision_quality", 4, "raise", "OP revision이 EPS/FCF 체급 변화의 핵심이다."),
    Round271ScoreAdjustment("labor_operational_resilience", 5, "raise", "노사/생산중단 리스크를 통과해야 Green이 가능하다."),
    Round271ScoreAdjustment("China_fab_export_control_clearance", 5, "raise", "중국 fab 노출은 HBM 호황 속에서도 hard gate다."),
    Round271ScoreAdjustment("capex_ROI_bridge", 4, "raise", "AI capex는 생산성·매출·FCF bridge가 있을 때만 긍정이다."),
    Round271ScoreAdjustment("AI_chip_keyword_only", -5, "lower", "AI칩 keyword만으로는 Green 금지다."),
    Round271ScoreAdjustment("policy_foundry_headline_only", -5, "lower", "foundry 정책 headline은 operator/utilization 전 Green이 아니다."),
    Round271ScoreAdjustment("IPO_oversubscription_only", -5, "lower", "IPO 청약 경쟁률은 납품·마진 증거가 아니다."),
    Round271ScoreAdjustment("strategic_equity_or_unlisted_merger_only", -5, "lower", "비상장 합병과 전략지분은 상장사 EPS가 아니다."),
    Round271ScoreAdjustment("equipment_carveout_without_orders", -4, "lower", "장비 분사는 실제 수주 전 Stage 2에 머문다."),
    Round271ScoreAdjustment("capex_consumption_without_EPS", -4, "lower", "칩을 사는 이벤트와 EPS가 늘어나는 이벤트를 분리한다."),
    Round271ScoreAdjustment("HBM_rumor_without_customer_qualification", -5, "lower", "HBM rumor는 고객 인증 전 감점한다."),
    Round271ScoreAdjustment("China_fab_exposure", -5, "lower", "중국 fab 노출이 열려 있으면 Green을 막는다."),
    Round271ScoreAdjustment("labor_strike_unresolved", -5, "lower", "노동쟁의 생산중단 리스크가 열려 있으면 Green을 막는다."),
)


ROUND271_SHADOW_WEIGHT_ROWS: tuple[Round271ShadowWeightRow, ...] = (
    Round271ShadowWeightRow(E2RArchetype.HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B, 5, 5, 5, 3, 4, 5, 5, 4, 4, 3, -1, 5, 4, "SK Hynix remains aligned but is now 4B after massive MFE."),
    Round271ShadowWeightRow(E2RArchetype.SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C, 5, 5, 5, 3, 4, 5, 4, 5, 5, 4, -3, 5, 5, "Samsung recovery needs HBM volume/margin and labor risk clearance."),
    Round271ShadowWeightRow(E2RArchetype.HBM_EQUIPMENT_CARVEOUT_NOT_GREEN, 3, 4, 4, 5, 5, 5, 3, 2, 3, 3, -4, 5, 4, "Hanwha Precision carve-out requires actual HBM equipment orders and revenue."),
    Round271ShadowWeightRow(E2RArchetype.AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2, 2, 4, 5, 1, 4, 5, 2, 2, 3, 4, -5, 5, 4, "Rebellions/Sapeon needs customer deployment and listed revenue bridge."),
    Round271ShadowWeightRow(E2RArchetype.SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT, 2, 4, 4, 5, 5, 5, 3, 2, 3, 4, -5, 5, 4, "TeraView IPO is Stage 2 but oversubscription/P-E overheat requires delivery proof."),
    Round271ShadowWeightRow(E2RArchetype.STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN, 1, 2, 3, 2, 2, 4, 2, 2, 4, 5, -5, 4, 4, "Foundry policy needs operator/utilization/customer contracts."),
    Round271ShadowWeightRow(E2RArchetype.NVIDIA_BLACKWELL_DOMESTIC_AI_INFRA_STAGE2, 1, 2, 3, 0, 0, 3, 2, 2, 2, 5, -4, 4, 3, "Blackwell consumption is not EPS without productivity/cloud revenue bridge."),
    Round271ShadowWeightRow(E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH, 0, 0, 0, 0, 0, 2, 0, 2, 5, 0, 0, 4, 5, "China fab exposure remains R2 hard-gate candidate."),
)


ROUND271_DEEP_SUB_ARCHETYPES: tuple[Round271DeepSubArchetype, ...] = (
    Round271DeepSubArchetype("HBM memory", E2RArchetype.HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B, ("SK Hynix", "HBM supply scarcity", "Nvidia supply chain", "massive MFE", "4B-watch")),
    Round271DeepSubArchetype("Samsung catch-up", E2RArchetype.SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C, ("Samsung Electronics", "HBM lag", "China curbs", "Tesla foundry relief", "labor strike")),
    Round271DeepSubArchetype("HBM equipment carve-out", E2RArchetype.HBM_EQUIPMENT_CARVEOUT_NOT_GREEN, ("Hanwha Precision Machinery", "Hanwha Vision", "HBM equipment", "spin-off", "sell-the-news")),
    Round271DeepSubArchetype("AI chip design", E2RArchetype.AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2, ("Rebellions", "Sapeon", "SK Telecom", "SK Hynix", "NPU", "unlisted merger")),
    Round271DeepSubArchetype("inspection IPO", E2RArchetype.SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT, ("TeraView", "terahertz inspection", "Samsung stake", "600x oversubscription", "P/E 40x")),
    Round271DeepSubArchetype("foundry policy", E2RArchetype.STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN, ("4.5T won foundry", "12-inch 40nm", "fabless", "defense chips", "operator utilization")),
    Round271DeepSubArchetype("AI infra consumption", E2RArchetype.NVIDIA_BLACKWELL_DOMESTIC_AI_INFRA_STAGE2, ("Nvidia Blackwell", "260000 chips", "Samsung", "SK", "Hyundai", "Naver")),
    Round271DeepSubArchetype("export-control overlay", E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH, ("Samsung China fab", "SK Hynix China fab", "Hana Micron", "Hanmi Semiconductor", "authorisation revocation")),
)


ROUND271_CASE_CANDIDATES: tuple[Round271CaseCandidate, ...] = (
    Round271CaseCandidate(
        case_id="r2_loop13_sk_hynix_hbm_success_now_4b",
        symbol="000660",
        company_name="SK Hynix",
        primary_archetype=E2RArchetype.HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B,
        secondary_archetypes=(E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.STRUCTURAL_SUCCESS_NOW_4B),
        case_type="structural_success",
        round_case_type="structural_success_4B_watch",
        stage1_date=date(2024, 3, 1),
        stage2_date=date(2024, 7, 11),
        stage3_date=date(2024, 7, 24),
        stage4b_date=date(2026, 5, 14),
        stage4c_date=None,
        stage3_decision="hbm_volume_customer_demand_op_revision_supply_squeeze_and_price_path_aligned_but_current_state_is_4b_watch_after_massive_mfe",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("q2_2024_op_5_47tn_krw", "hbm_shipments_expected_more_than_double", "nvidia_supply_chain_exposure", "reported_ytd_return_2024_july_70pct"),
        red_flag_fields=("reported_return_2025_274pct", "reported_return_2026_min_200pct", "market_cap_2026_942bn_usd", "market_cap_milestone_4b_watch"),
        price_data_source="Reuters reported return / earnings anchors",
        reported_price_anchor="Market cap about $942B by 2026-05-14; under $100B about 16 months earlier",
        reported_return_anchor="Q2 2024 OP 5.47T KRW; 2024 July YTD +70%; 2025 +274%; 2026 >+200%",
        event_mfe_pct=274.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=842.0,
        extra_price_metrics={"q2_2024_op_krw_trn": 5.47, "q2_2024_op_status": "highest_since_2018", "hbm_shipments_next_year": "expected_to_more_than_double", "reported_ytd_return_2024_july_pct": 70.0, "reported_return_2025_pct": 274.0, "reported_return_2026_min_pct": 200.0, "market_cap_2026_may_usd_bn": 942.0, "market_cap_mfe_from_under_100b_pct": 842.0},
        score_price_alignment="aligned",
        round_alignment_label="aligned_but_now_4B",
        rerating_result="true_rerating",
        round_rerating_label="true_HBM_memory_structural_rerating",
        stage_failure_type="green_success",
        round_stage_failure_label="stage3_success_now_4b_watch",
        price_validation_status="reported_anchor_not_full_ohlc",
        notes="SK Hynix는 R2 structural success benchmark지만, 현재는 신규 Green보다 4B-watch다.",
    ),
    Round271CaseCandidate(
        case_id="r2_loop13_samsung_hbm_lag_labor_4c_watch",
        symbol="005930",
        company_name="Samsung Electronics",
        primary_archetype=E2RArchetype.SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C,
        secondary_archetypes=(E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH),
        case_type="success_candidate",
        round_case_type="success_candidate_thesis_break_watch",
        stage1_date=date(2024, 7, 5),
        stage2_date=date(2024, 7, 5),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 7, 30),
        stage3_decision="memory_recovery_is_stage2_but_hbm_volume_margin_china_curb_and_labor_risk_must_clear_before_green",
        stage4b_status="4B-watch/labor-profit-sharing",
        hard_4c_confirmed=False,
        evidence_fields=("q2_2024_op_estimate_10_4tn_krw", "q2_2024_revenue_estimate_74tn_krw", "memory_price_recovery", "tesla_chip_sourcing_relief"),
        red_flag_fields=("q2_2025_op_decline_55pct", "chip_division_profit_decline_93_8pct", "hbm_shipment_delay", "china_curbs", "labor_strike_unresolved"),
        price_data_source="Reuters earnings / labor anchors",
        reported_price_anchor="Q2 2025 stock +0.7%, matching KOSPI, despite OP -55% because Tesla deal gave relief",
        reported_return_anchor="Q2 2024 OP 10.4T KRW vs 0.67T prior year; Q2 2025 OP 4.7T KRW",
        event_mfe_pct=0.7,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"q2_2024_op_estimate_krw_trn": 10.4, "q2_2024_prior_year_op_krw_trn": 0.67, "q2_2024_op_growth_multiple": 15.52, "q2_2024_revenue_estimate_krw_trn": 74.0, "q2_2024_revenue_growth_pct": 23.0, "lseg_smartestimate_krw_trn": 8.8, "q2_2025_op_krw_trn": 4.7, "q2_2025_op_decline_pct": -55.0, "chip_division_profit_q2_2025_krw_trn": 0.4, "chip_division_profit_prior_year_krw_trn": 6.5, "chip_division_profit_decline_pct": -93.8, "stock_reaction_q2_2025_pct": 0.7, "kospi_same_context_pct": 0.7, "tesla_chip_sourcing_deal_usd_bn": 16.5, "strike_possible_workers": 50000.0, "strike_duration_days": 18.0, "one_day_direct_loss_estimate_krw_trn": 1.0},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="success_candidate_plus_thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="Samsung_memory_recovery_but_HBM_lag_and_labor_gate",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="recovery_not_green_until_HBM_volume_margin_and_labor_risk_clear",
        price_validation_status="reported_anchor_not_full_ohlc",
        notes="메모리 회복은 Stage 2지만 HBM lag, China curbs, 노동 리스크가 Green을 막는다.",
    ),
    Round271CaseCandidate(
        case_id="r2_loop13_hanwha_precision_hbm_equipment_carveout",
        symbol="012450_parent",
        company_name="Hanwha Precision Machinery / Hanwha Aerospace parent",
        primary_archetype=E2RArchetype.HBM_EQUIPMENT_CARVEOUT_NOT_GREEN,
        secondary_archetypes=(E2RArchetype.HBM_BONDER_EQUIPMENT_ORDER, E2RArchetype.EVENT_PREMIUM),
        case_type="failed_rerating",
        round_case_type="failed_rerating_success_candidate",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 5),
        stage3_date=None,
        stage4b_date=date(2024, 4, 5),
        stage4c_date=None,
        stage3_decision="hbm_equipment_carveout_is_stage2_not_green_until_actual_hbm_equipment_orders_margin_listed_vehicle_and_cash_flow_bridge_confirm",
        stage4b_status="4B-watch/sell-the-news",
        hard_4c_confirmed=False,
        evidence_fields=("hanwha_precision_hbm_equipment_development", "spin_off_business_revenue_share_16pct", "new_industrial_solutions_value_2tn_krw"),
        red_flag_fields=("spinoff_speculation_plus_15pct", "confirmation_event_minus_8pct", "actual_hbm_equipment_order_revenue_unconfirmed", "equipment_carveout_without_orders"),
        price_data_source="Reuters spin-off/event-return anchor",
        reported_price_anchor="Media report +15%; official confirmation -8%",
        reported_return_anchor="Spin-off businesses contributed about 16% revenue; new industrial-solutions company estimated around 2T KRW",
        event_mfe_pct=15.0,
        event_mae_pct=-8.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"media_report_pre_event_mfe_pct": 15.0, "confirmation_event_mae_pct": -8.0, "spin_off_business_revenue_share_pct": 16.0, "new_industrial_solutions_estimated_value_krw_trn": 2.0, "defense_business_estimated_value_krw_trn": 10.0, "parent_market_cap_context_krw_trn": 11.0, "hbm_equipment_development_confirmed": True, "actual_hbm_equipment_order_revenue_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="failed_rerating_stage2",
        rerating_result="event_premium",
        round_rerating_label="HBM_equipment_carveout_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="carveout_value_unlock_not_order_revenue_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="HBM 장비 분사는 Stage 2지만 실제 장비 주문·매출 bridge 전에는 Green이 아니다.",
    ),
    Round271CaseCandidate(
        case_id="r2_loop13_rebellions_sapeon_ai_chip_merger",
        symbol="SKT/SK_Hynix_readthrough_unlisted",
        company_name="Rebellions / Sapeon Korea",
        primary_archetype=E2RArchetype.AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2,
        secondary_archetypes=(E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE,),
        case_type="success_candidate",
        round_case_type="success_candidate_insufficient_price_data",
        stage1_date=date(2024, 6, 12),
        stage2_date=date(2024, 8, 18),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="unlisted_ai_chip_merger_is_stage2_not_listed_green_until_tapeout_customer_deployment_mass_production_revenue_and_margin_confirm",
        stage4b_status="4B-watch-if-listed-readthrough-rallies-before-revenue",
        hard_4c_confirmed=False,
        evidence_fields=("rebellions_sapeon_merger", "sk_telecom_sk_hynix_shareholder_readthrough", "total_funding_225mn_usd", "npu_data_center_llm_chip_focus"),
        red_flag_fields=("unlisted_merger_only", "listed_revenue_bridge_unconfirmed", "mass_production_unconfirmed", "customer_order_unconfirmed"),
        price_data_source="Reuters AI-chip merger anchors",
        reported_price_anchor="Direct company unlisted; listed shareholder earnings bridge not confirmed",
        reported_return_anchor="Rebellions funding over $225M after $15M Wa'ed Ventures investment",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"merged_companies": "Rebellions + Sapeon Korea", "listed_shareholder_readthrough": "SK Telecom|SK Hynix", "total_funding_rebellions_usd_mn": 225.0, "waed_ventures_investment_usd_mn": 15.0, "target_market_share_timeline": "2-3 years", "npu_focus": True},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_insufficient_price_data",
        rerating_result="unknown",
        round_rerating_label="Korean_AI_chip_design_unlisted_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="merger_not_mass_production_revenue_green",
        price_validation_status="unlisted_company_no_direct_ohlc",
        notes="비상장 AI chip 합병은 Stage 2지만 상장사 EPS bridge 전에는 Green이 아니다.",
    ),
    Round271CaseCandidate(
        case_id="r2_loop13_teraview_kosdaq_semiconductor_inspection_ipo",
        symbol="new_KOSDAQ_foreign_listing",
        company_name="TeraView",
        primary_archetype=E2RArchetype.SEMICONDUCTOR_INSPECTION_KOSDAQ_IPO_OVERHEAT,
        secondary_archetypes=(E2RArchetype.IPO_EVENT_PREMIUM, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="overheat",
        round_case_type="overheat_success_candidate",
        stage1_date=date(2025, 12, 8),
        stage2_date=date(2025, 12, 8),
        stage3_date=None,
        stage4b_date=date(2025, 12, 8),
        stage4c_date=None,
        stage3_decision="semiconductor_inspection_ipo_is_stage2_not_green_until_delivered_order_book_recurring_service_customer_diversification_and_margin_durability_confirm",
        stage4b_status="4B-watch/IPO-overheat",
        hard_4c_confirmed=False,
        evidence_fields=("terahertz_semiconductor_inspection", "samsung_customer_and_10pct_stake", "regional_revenue_share_60pct", "margin_forecast_60_to_70pct"),
        red_flag_fields=("ipo_oversubscription_600x", "implied_pe_40x", "listed_delivery_record_unconfirmed", "customer_concentration_watch"),
        price_data_source="MarketWatch IPO anchor",
        reported_price_anchor="Listing price 8,000 KRW; implied P/E about 40x",
        reported_return_anchor="40B KRW offering, $240M valuation, 600x oversubscription, Samsung 10% stake",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=8000.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=8000.0,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"ipo_offering_krw_bn": 40.0, "ipo_offering_usd_mn": 27.0, "implied_valuation_usd_mn": 240.0, "oversubscription_multiple": 600.0, "listing_price_krw": 8000.0, "implied_pe": 40.0, "samsung_stake_pct": 10.0, "regional_revenue_share_pct": 60.0, "margin_forecast_pct": "60-70", "order_book_growth_forecast_pct": 100.0},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="overheat_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="semiconductor_inspection_IPO_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="IPO_demand_not_delivery_margin_green",
        price_validation_status="reported_ipo_anchor_not_full_ohlc",
        notes="검사장비 story는 Stage 2지만 600x 청약과 P/E 40x는 납품·마진 전 4B다.",
    ),
    Round271CaseCandidate(
        case_id="r2_loop13_korea_state_foundry_policy",
        symbol="foundry_fabless_basket",
        company_name="Korea state-private foundry policy basket",
        primary_archetype=E2RArchetype.STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN,
        secondary_archetypes=(E2RArchetype.PRICE_ONLY_POLICY_RALLY,),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_relief",
        stage1_date=date(2025, 12, 10),
        stage2_date=date(2025, 12, 10),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="foundry_policy_proposal_is_stage2_not_green_until_final_budget_operator_utilization_customer_contracts_margin_and_capex_roi_confirm",
        stage4b_status="4B-watch-if-policy-basket-rallies-before-utilization",
        hard_4c_confirmed=False,
        evidence_fields=("proposed_foundry_investment_4_5tn_krw", "12_inch_40nm_facility", "domestic_fabless_support", "defense_chip_import_dependence_99pct"),
        red_flag_fields=("foundry_policy_only", "operator_unconfirmed", "customer_contract_unconfirmed", "utilization_margin_unconfirmed"),
        price_data_source="Reuters foundry-policy anchor",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="4.5T KRW / $3.06B foundry proposal; 12-inch 40nm facility",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"proposed_foundry_investment_krw_trn": 4.5, "proposed_foundry_investment_usd_bn": 3.06, "wafer_size": "12-inch", "process_node": "40nm", "target_users": "domestic fabless / essential chips", "defense_chip_import_dependence_pct": 99.0, "operator_confirmed": False, "customer_contract_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_policy_relief",
        rerating_result="policy_event_rerating",
        round_rerating_label="state_foundry_policy_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="policy_proposal_not_utilization_margin_green",
        price_validation_status="policy_anchor_not_full_ohlc",
        notes="정책 foundry는 Stage 2 relief지만 operator, utilization, 고객계약 전 Green이 아니다.",
    ),
    Round271CaseCandidate(
        case_id="r2_loop13_nvidia_blackwell_korea_ai_infra",
        symbol="Samsung/SK/Hyundai/Naver/Kakao_ecosystem",
        company_name="Nvidia Blackwell Korea AI infrastructure buyers",
        primary_archetype=E2RArchetype.NVIDIA_BLACKWELL_DOMESTIC_AI_INFRA_STAGE2,
        secondary_archetypes=(E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE),
        case_type="event_premium",
        round_case_type="success_candidate_event_premium",
        stage1_date=date(2025, 10, 31),
        stage2_date=date(2025, 10, 31),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="blackwell_chip_consumption_is_stage2_not_green_until_ai_factory_productivity_cloud_revenue_process_efficiency_and_capex_roi_confirm",
        stage4b_status="4B-watch-if-ai-infra-basket-rallies-before-eps",
        hard_4c_confirmed=False,
        evidence_fields=("nvidia_blackwell_260000_chips_to_korea", "government_ai_infra_50000_chips", "samsung_sk_hyundai_each_up_to_50000_chips", "naver_60000_chips"),
        red_flag_fields=("blackwell_chip_consumption_only", "direct_supplier_revenue_to_korean_listed_companies_false", "capex_roi_unconfirmed"),
        price_data_source="Reuters Nvidia Blackwell supply anchor",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="Nvidia to supply more than 260,000 Blackwell AI chips to South Korea",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"total_blackwell_chips_to_korea": 260000.0, "government_ai_infra_chips": 50000.0, "samsung_chips_up_to": 50000.0, "sk_chips_up_to": 50000.0, "hyundai_chips_up_to": 50000.0, "naver_chips": 60000.0, "direct_supplier_revenue_to_korean_listed_companies": False, "capex_roi_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_event_premium",
        rerating_result="event_premium",
        round_rerating_label="AI_infra_chip_consumption_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="capex_consumption_not_eps_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Blackwell 칩을 사는 이벤트는 Stage 2다. 생산성·cloud revenue·capex ROI 전에는 EPS 증거가 아니다.",
    ),
    Round271CaseCandidate(
        case_id="r2_loop13_china_fab_export_control_basket",
        symbol="005930/000660/067310/042700",
        company_name="Samsung / SK Hynix / Hana Micron / Hanmi China-fab export-control basket",
        primary_archetype=E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH,
        secondary_archetypes=(E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="failed_rerating",
        round_case_type="4C-watch",
        stage1_date=date(2025, 8, 29),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 1),
        stage3_decision="china_fab_export_control_is_redteam_overlay_not_green_and_not_hard_4c_until_license_denial_or_revenue_impairment_confirms",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("us_authorisation_revocation", "samsung_china_dram_exposure_more_than_one_third", "sk_hynix_china_dram_nand_exposure_30_to_40pct"),
        red_flag_fields=("china_fab_exposure_unresolved", "export_control_escalation_watch", "samsung_event_minus_2_3pct", "sk_hynix_event_minus_4_4pct", "hanmi_event_minus_4_4pct"),
        price_data_source="Reuters export-control event-return anchor",
        reported_price_anchor="Samsung -2.3%; SK Hynix -4.4%; Hana Micron -1.7%; Hanmi -4.4%; KOSPI -0.7%",
        reported_return_anchor="U.S. revokes authorisations for Samsung/SK Hynix China fabs",
        event_mfe_pct=None,
        event_mae_pct=-4.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"samsung_event_mae_pct": -2.3, "sk_hynix_event_mae_pct": -4.4, "hana_micron_event_mae_pct": -1.7, "hanmi_semiconductor_event_mae_pct": -4.4, "kospi_same_context_pct": -0.7, "samsung_relative_underperformance_pp": -1.6, "sk_hynix_relative_underperformance_pp": -3.7, "hanmi_relative_underperformance_pp": -3.7, "samsung_china_dram_exposure": "more_than_one_third", "sk_hynix_china_dram_nand_exposure_pct": "30-40"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="China_fab_export_control_overlay",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4C_watch_not_hard_4C",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="중국 fab 수출통제는 hard 4C 확정은 아니지만 R2 Green을 막는 강한 4C-watch다.",
    ),
)


def round271_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("hbm", "shipment", "mass_production", "order", "margin", "op", "fcf", "qualification", "revenue")
    for candidate in ROUND271_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND271_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round271 R2 Loop-13 AI/semiconductor/electronics price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "4b" in field.lower()
                or "ipo" in field.lower()
                or "oversubscription" in field.lower()
                or "market_cap" in field.lower()
                or "return_2025" in field.lower()
                or "spinoff" in field.lower()
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "4c" in field.lower()
                or "delay" in field.lower()
                or "curb" in field.lower()
                or "strike" in field.lower()
                or "export_control" in field.lower()
                or "china_fab" in field.lower()
                or "failure" in field.lower()
            ),
            must_have_fields=ROUND271_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4b_watch", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND271_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_ai_hbm_foundry_ipo_policy_or_blackwell_keywords_as_green_alone",
                *ROUND271_GREEN_REQUIRED_FIELDS,
                *ROUND271_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_return_from_stage3=candidate.peak_return_from_stage3_pct,
                mfe_30d=candidate.event_mfe_pct,
                mae_30d=candidate.event_mae_pct,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=candidate.stage2_price_anchor is not None
                or candidate.stage4b_price_anchor is not None
                or candidate.stage4c_price_anchor is not None
                or candidate.event_mfe_pct is not None
                or candidate.event_mae_pct is not None,
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage3_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round271_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND271_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "source_sector": "R2",
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
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
                "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
                "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
                "peak_return_from_stage3_pct": _float_text(candidate.peak_return_from_stage3_pct),
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
        )
    return tuple(rows)


def round271_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND271_SCORE_ADJUSTMENTS)


def round271_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND271_SHADOW_WEIGHT_ROWS)


def round271_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND271_DEEP_SUB_ARCHETYPES)


def round271_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round271_price_validation": "true"} for field in ROUND271_PRICE_VALIDATION_FIELDS)


def round271_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round271_label": label, "canonical_archetype": canonical} for label, canonical in ROUND271_REQUIRED_TARGET_ALIASES.items())


def round271_summary() -> dict[str, int | bool | str]:
    cases = ROUND271_CASE_CANDIDATES
    return {
        "source_round": ROUND271_SOURCE_ROUND_PATH,
        "round_id": ROUND271_ANALYST_ROUND_ID,
        "large_sector": ROUND271_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None),
        "price_data_unavailable_count": sum(1 for case in cases if case.price_validation_status == "price_data_unavailable_after_deep_search"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "aligned_count": sum(1 for case in cases if case.score_price_alignment == "aligned"),
        "target_archetype_count": len(ROUND271_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND271_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND271_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": False,
    }


def round271_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND271_SOURCE_ROUND_PATH,
        "round_id": ROUND271_ANALYST_ROUND_ID,
        "large_sector": ROUND271_LARGE_SECTOR,
        "summary": round271_summary(),
        "target_aliases": dict(ROUND271_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND271_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND271_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND271_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND271_HARD_4C_GATES),
        "deep_sub_archetypes": round271_deep_sub_archetype_rows(),
        "shadow_weights": round271_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round271_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_ai_hbm_foundry_ipo_policy_or_blackwell_keywords_as_green_alone",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round271_summary_markdown() -> str:
    summary = round271_summary()
    lines = [
        "# Round 271 R2 Loop 13 AI Semiconductor Electronics Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- structural_success: {summary['structural_success_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- price_data_unavailable: {summary['price_data_unavailable_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- aligned: {summary['aligned_count']}",
        f"- full_adjusted_ohlc_complete: {str(summary['full_adjusted_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND271_CASE_CANDIDATES:
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
            "- R2 Stage 3 is not the word AI, HBM, foundry, inspection equipment, IPO, policy, or Blackwell.",
            "- SK Hynix remains the clean structural success benchmark, but current state is 4B-watch.",
            "- Samsung recovery is Stage 2 while HBM lag, China curbs and labor strike risk remain open.",
            "- Hanwha Precision, Rebellions/Sapeon, TeraView and Korea foundry policy are Stage 2/watch items before orders, utilization, margin and revenue bridge.",
            "- Nvidia Blackwell Korea supply is AI-infra consumption, not Korean listed-company EPS proof by itself.",
            "- China fab export-control is 4C-watch, not hard 4C until license denial or revenue impairment confirms.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round271_green_gate_review_markdown() -> str:
    lines = ["# Round 271 R2 Loop 13 Green Gate Review", "", "Do not apply these weights to production scoring yet.", "", "## Required Fields", ""]
    lines.extend(f"- {field}" for field in ROUND271_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND271_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `HBM`이라는 단어만으로는 Green이 아니다. 고객 인증, 양산, shipment, margin이 필요하다.",
            "- `Blackwell 칩을 산다`는 AI infra Stage 2일 수 있지만, 상장사 EPS 증거는 아니다.",
            "- `IPO 600배 청약`은 납품·마진 증거가 아니라 4B-watch 신호다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round271_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 271 R2 Loop 13 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND271_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND271_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B는 HBM/AI/IPO/정책 가격이 실제 주문, 양산, 마진보다 먼저 간 상태다.",
            "- 4C-watch는 HBM lag, China fab, 노동 리스크처럼 Green을 막는 위험이다.",
            "- 이번 라운드에서는 hard 4C를 확정하지 않고 watch로 둔다.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND271_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.stage4c_date:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round271_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 271 R2 Loop 13 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND271_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round271_r2_loop13_reports(
    output_directory: str | Path = ROUND271_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND271_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND271_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round271_case_records(), cases_path),
        "audit": _write_json(round271_audit_payload(), audit_path),
        "summary": output / "round271_r2_loop13_price_validation_summary.md",
        "case_matrix": output / "round271_r2_loop13_case_matrix.csv",
        "target_aliases": output / "round271_r2_loop13_target_aliases.csv",
        "score_adjustments": output / "round271_r2_loop13_score_adjustments.csv",
        "shadow_weights": output / "round271_r2_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round271_r2_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round271_r2_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round271_r2_loop13_green_gate_review.md",
        "price_validation_plan": output / "round271_r2_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round271_r2_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round271_summary_markdown(), encoding="utf-8")
    _write_csv(round271_case_rows(), paths["case_matrix"])
    _write_csv(round271_target_alias_rows(), paths["target_aliases"])
    _write_csv(round271_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round271_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round271_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round271_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round271_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round271_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round271_stage4b_4c_review_markdown(), encoding="utf-8")
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
    return f"{value:+d}" if isinstance(value, int) else str(value)
