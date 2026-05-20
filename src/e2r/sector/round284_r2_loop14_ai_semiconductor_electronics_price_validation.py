"""Round-284 R2 Loop-14 AI/semiconductor/electronics price-validation pack.

This module converts ``docs/round/round_284.md`` into calibration-only case
records and reports. It does not change production scoring, staging, or
candidate generation.

Easy example: an OpenAI LOI can be a strong demand signal, but it is not the
same as a binding take-or-pay supply contract with ASP, margin, allocation and
shipment schedule.
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


ROUND284_SOURCE_ROUND_PATH = "docs/round/round_284.md"
ROUND284_ANALYST_ROUND_ID = "round_212"
ROUND284_LARGE_SECTOR = "AI_SEMICONDUCTOR_ELECTRONIC_COMPONENTS"
ROUND284_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round284_r2_loop14_ai_semiconductor_electronics_price_validation"
ROUND284_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop14_round284.jsonl"
ROUND284_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round284_r2_loop14_ai_semiconductor_electronics_price_validation_audit.json"

ROUND284_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "HBM_DOMINANCE_STAGE3_AND_4B": E2RArchetype.HBM_DOMINANCE_STAGE3_AND_4B.value,
    "SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH": E2RArchetype.SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH.value,
    "TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM": E2RArchetype.TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM.value,
    "ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2": E2RArchetype.ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2.value,
    "OLED_PORTFOLIO_RESTRUCTURING_STAGE2": E2RArchetype.OLED_PORTFOLIO_RESTRUCTURING_STAGE2.value,
    "KOREAN_AI_CHIP_FABLESS_STAGE2": E2RArchetype.KOREAN_AI_CHIP_FABLESS_STAGE2.value,
    "AI_INFRA_MEMORY_SUPPLY_MOU_4B": E2RArchetype.AI_INFRA_MEMORY_SUPPLY_MOU_4B.value,
    "CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH": E2RArchetype.CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH.value,
}

ROUND284_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "actual_hbm_allocation_confirmed",
    "customer_delivery_and_calloff_confirmed",
    "HBM_ASP_mix_margin_confirmed",
    "capacity_utilization_confirmed",
    "equipment_PO_to_revenue_confirmed",
    "customer_diversification_confirmed",
    "device_sellthrough_confirmed",
    "component_mix_margin_confirmed",
    "OLED_utilization_confirmed",
    "labor_supply_continuity_confirmed",
    "price_path_after_evidence",
)

ROUND284_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "AI_keyword_only",
    "HBM_theme_without_customer_delivery",
    "LOI_or_MOU_without_binding_contract",
    "rumored_customer_PO",
    "on_device_AI_expectation_only",
    "capacity_capex_without_utilization",
    "unlisted_AI_chip_readthrough",
    "consumer_OEM_exposed_to_memory_cost",
    "labor_disruption_risk",
)

ROUND284_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "HBM_leader_one_year_200pct_plus_after_prior_274pct",
    "AI_memory_MOU_LOI_10pct_plus_rally",
    "equipment_unconfirmed_customer_rumor_20pct_plus",
    "on_device_AI_iPhone_expectation_before_component_margin",
    "OLED_capex_or_LCD_exit_before_utilization",
    "unlisted_AI_chip_merger_readthrough_to_listed_EPS",
    "Samsung_catchup_rally_before_strike_export_control_clearance",
)

ROUND284_HARD_4C_GATES: tuple[str, ...] = (
    "HBM_qualification_failure",
    "export_control_ban_on_HBM_or_AI_chips",
    "major_customer_calloff_cancellation",
    "strike_or_shutdown_disrupting_memory_supply",
    "capex_without_utilization_cash_burn",
    "component_cost_spike_crushing_OEM_margins",
    "foundry_logic_chip_loss_widening_despite_AI_rally",
)

ROUND284_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "reported_price_anchor",
    "earnings_anchor",
    "target_price_anchor",
    "deal_funding_capex_anchor",
    "market_share_anchor",
    "strike_export_control_risk_anchor",
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
class Round284ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round284ShadowWeightRow:
    archetype: E2RArchetype
    actual_hbm_allocation: int
    customer_delivery_calloff: int
    hbm_asp_mix_margin: int
    capacity_utilization: int
    equipment_po_to_revenue: int
    customer_diversification: int
    device_sellthrough: int
    component_mix_margin: int
    oled_utilization: int
    labor_supply_continuity: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "actual_hbm_allocation": _signed(self.actual_hbm_allocation),
            "customer_delivery_calloff": _signed(self.customer_delivery_calloff),
            "HBM_ASP_mix_margin": _signed(self.hbm_asp_mix_margin),
            "capacity_utilization": _signed(self.capacity_utilization),
            "equipment_PO_to_revenue": _signed(self.equipment_po_to_revenue),
            "customer_diversification": _signed(self.customer_diversification),
            "device_sellthrough": _signed(self.device_sellthrough),
            "component_mix_margin": _signed(self.component_mix_margin),
            "OLED_utilization": _signed(self.oled_utilization),
            "labor_supply_continuity": _signed(self.labor_supply_continuity),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round284DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round284CaseCandidate:
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
    hard_4c_watch_confirmed: bool
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


ROUND284_SCORE_ADJUSTMENTS: tuple[Round284ScoreAdjustment, ...] = (
    Round284ScoreAdjustment("actual_hbm_allocation", 5, "raise", "HBM은 고객 allocation과 실제 납품이 확인될 때 강하다."),
    Round284ScoreAdjustment("customer_delivery_and_calloff", 5, "raise", "고객 수요는 call-off와 delivery로 닫혀야 한다."),
    Round284ScoreAdjustment("HBM_ASP_mix_margin", 5, "raise", "HBM ASP와 mix margin이 OP로 내려오는지 확인한다."),
    Round284ScoreAdjustment("capacity_utilization", 5, "raise", "증설과 capex는 utilization이 있어야 FCF로 연결된다."),
    Round284ScoreAdjustment("equipment_PO_to_revenue", 5, "raise", "장비주는 PO, 납품, revenue recognition이 핵심이다."),
    Round284ScoreAdjustment("customer_diversification", 4, "raise", "장비·부품주는 단일 고객 루머보다 고객 다변화가 중요하다."),
    Round284ScoreAdjustment("device_sellthrough", 5, "raise", "on-device AI는 실제 기기 판매와 교체수요가 필요하다."),
    Round284ScoreAdjustment("component_mix_margin", 5, "raise", "부품 탑재량과 mix가 margin으로 이어져야 한다."),
    Round284ScoreAdjustment("OLED_utilization", 5, "raise", "OLED capex는 utilization과 현금흐름으로 검증한다."),
    Round284ScoreAdjustment("labor_supply_continuity", 5, "raise", "파업·셧다운은 memory 공급 안정성 hard gate다."),
    Round284ScoreAdjustment("AI_keyword_only", -5, "lower", "AI 단어만으로 매출·마진을 만들지 않는다."),
    Round284ScoreAdjustment("HBM_theme_without_customer_delivery", -5, "lower", "HBM 테마는 고객 납품 전에는 제한한다."),
    Round284ScoreAdjustment("LOI_or_MOU_without_binding_contract", -5, "lower", "LOI/MOU는 binding take-or-pay가 아니다."),
    Round284ScoreAdjustment("rumored_customer_PO", -5, "lower", "고객 루머는 PO/revenue가 아니다."),
    Round284ScoreAdjustment("on_device_AI_expectation_only", -5, "lower", "Apple AI 기대는 sell-through와 부품 margin 전에는 부족하다."),
    Round284ScoreAdjustment("capacity_capex_without_utilization", -5, "lower", "capex만 있고 utilization이 없으면 현금소모일 수 있다."),
    Round284ScoreAdjustment("unlisted_AI_chip_readthrough", -5, "lower", "비상장 AI chip 성과를 상장사 EPS로 바로 연결하지 않는다."),
    Round284ScoreAdjustment("consumer_OEM_exposed_to_memory_cost", -4, "lower", "메모리 shortage는 OEM에는 부품비 부담일 수 있다."),
    Round284ScoreAdjustment("labor_disruption_risk", -5, "lower", "파업·공급차질은 HBM catch-up narrative를 막는다."),
)


ROUND284_SHADOW_WEIGHT_ROWS: tuple[Round284ShadowWeightRow, ...] = (
    Round284ShadowWeightRow(E2RArchetype.HBM_DOMINANCE_STAGE3_AND_4B, 5, 5, 5, 5, 0, 4, 0, 0, 0, 4, -2, 5, 4, "SK Hynix HBM success is real, but valuation/crowding 4B must trigger."),
    Round284ShadowWeightRow(E2RArchetype.SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH, 5, 5, 5, 5, 0, 4, 0, 0, 0, 5, -4, 5, 5, "Samsung needs HBM qualification, China exposure and labor continuity gates."),
    Round284ShadowWeightRow(E2RArchetype.TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM, 3, 5, 4, 4, 5, 5, 0, 0, 0, 2, -5, 5, 4, "Hanmi needs confirmed customer PO/shipment/revenue, not rumor."),
    Round284ShadowWeightRow(E2RArchetype.ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2, 0, 3, 0, 4, 0, 4, 5, 5, 0, 1, -5, 5, 3, "LG Innotek needs actual iPhone sell-through and component margin."),
    Round284ShadowWeightRow(E2RArchetype.OLED_PORTFOLIO_RESTRUCTURING_STAGE2, 0, 3, 0, 5, 0, 3, 4, 4, 5, 1, -4, 4, 3, "LG Display LCD exit/OLED capex needs utilization and FCF."),
    Round284ShadowWeightRow(E2RArchetype.KOREAN_AI_CHIP_FABLESS_STAGE2, 0, 5, 3, 4, 0, 5, 0, 0, 0, 2, -5, 5, 4, "Rebellions/Sapeon needs tape-out, production, workload revenue and listed EPS bridge."),
    Round284ShadowWeightRow(E2RArchetype.AI_INFRA_MEMORY_SUPPLY_MOU_4B, 5, 5, 5, 5, 0, 4, 0, 0, 0, 2, -5, 5, 4, "OpenAI/Stargate LOI is demand signal, not binding take-or-pay Green."),
    Round284ShadowWeightRow(E2RArchetype.CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH, 0, 2, 0, 3, 0, 2, 5, 5, 0, 1, 0, 4, 4, "LG Electronics shows memory shortage can hurt OEM margins."),
)


ROUND284_DEEP_SUB_ARCHETYPES: tuple[Round284DeepSubArchetype, ...] = (
    Round284DeepSubArchetype("HBM memory", E2RArchetype.HBM_DOMINANCE_STAGE3_AND_4B, ("SK Hynix", "Nvidia HBM3E", "Q2 OP 5.47T KRW", "HBM share 61%", "market cap $942B")),
    Round284DeepSubArchetype("Samsung catch-up and labor risk", E2RArchetype.SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH, ("Samsung Electronics", "HBM China exposure 20%", "KOSPI 7000", "strike 50,000 workers", "Nvidia qualification")),
    Round284DeepSubArchetype("HBM equipment", E2RArchetype.TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM, ("Hanmi Semiconductor", "TSV-TC bonder", "SK Hynix 21.48B KRW", "Micron rumor +22%", "customer PO gate")),
    Round284DeepSubArchetype("On-device AI components", E2RArchetype.ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2, ("LG Innotek", "Apple Intelligence", "Q2 OP estimate 106.4B KRW", "shares -0.4%", "sell-through gate")),
    Round284DeepSubArchetype("OLED portfolio restructuring", E2RArchetype.OLED_PORTFOLIO_RESTRUCTURING_STAGE2, ("LG Display", "Guangzhou LCD sale $1.54B", "OLED capex 1.1T KRW", "utilization gate")),
    Round284DeepSubArchetype("Korean AI chip fabless", E2RArchetype.KOREAN_AI_CHIP_FABLESS_STAGE2, ("Rebellions", "Sapeon", "SK Telecom", "SK Hynix", "$225M funding", "listed EPS bridge")),
    Round284DeepSubArchetype("AI infra MOU", E2RArchetype.AI_INFRA_MEMORY_SUPPLY_MOU_4B, ("Samsung", "SK Hynix", "OpenAI Stargate", "900,000 DRAM wafers/month", "LOI not binding")),
    Round284DeepSubArchetype("Consumer electronics cost pressure", E2RArchetype.CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH, ("LG Electronics", "Q4 net loss 725.9B KRW", "operating loss 109B KRW", "component costs", "weak TV demand")),
)


ROUND284_CASE_CANDIDATES: tuple[Round284CaseCandidate, ...] = (
    Round284CaseCandidate(
        case_id="r2_loop14_sk_hynix_hbm_dominance_stage3_4b",
        symbol="000660",
        company_name="SK Hynix HBM dominance",
        primary_archetype=E2RArchetype.HBM_DOMINANCE_STAGE3_AND_4B,
        secondary_archetypes=(E2RArchetype.MEMORY_HBM_CAPACITY_LEADER, E2RArchetype.HBM_MEMORY_STRUCTURAL_RERATING_NOW_4B),
        case_type="structural_success",
        round_case_type="structural_success + 4B-watch",
        stage1_date=date(2024, 3, 26),
        stage2_date=date(2024, 7, 25),
        stage3_date=date(2024, 7, 25),
        stage4b_date=date(2026, 1, 28),
        stage4c_date=None,
        stage3_decision="HBM_demand_ASP_mix_Nvidia_exposure_and_OP_recovery_align_but_extreme_rerating_triggers_4B_watch",
        stage4b_status="4B-watch/valuation-crowding-after-HBM-success",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Q2_2024_OP_5_47trn_krw", "HBM_sold_out_2024_almost_sold_out_2025", "HBM_shipments_more_than_double_expected", "Q4_2025_OP_19_2trn_krw", "HBM_market_share_61pct"),
        red_flag_fields=("expectations_overshoot_Q2_earnings_day_minus_8_4pct", "share_gain_2025_274pct", "share_gain_2026_to_May_200pct", "market_cap_942bn_usd"),
        price_data_source="WSJ chip-rally anchor + Reuters earnings/market-cap anchors",
        reported_price_anchor="+4.3% Stage1 event; Q2 earnings intraday -8.4%; Q4 2025 after-hours +9%; 2026 to May +200%",
        reported_return_anchor="HBM success is real, but valuation/crowding 4B-watch must trigger after extreme rerating.",
        event_mfe_pct=4.3,
        event_mae_pct=-8.4,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stage1_event_mfe_pct_2024_03_26": 4.3, "kospi_same_context_pct_2024_03_26": 0.7, "relative_outperformance_pp_2024_03_26": 3.6, "q2_2024_op_krw_trn": 5.47, "q2_2024_op_usd_bn": 3.96, "q2_2024_earnings_event_mae_pct": -8.4, "ytd_gain_before_q2_report_pct": 47, "q4_2025_op_krw_trn": 19.2, "q4_2025_op_growth_pct": 137, "q4_2025_analyst_expectation_krw_trn": 17.7, "hbm_market_share_q4_2025_pct": 61, "q4_2025_after_hours_mfe_pct": 9, "share_cancellation_krw_trn": 12.2, "treasury_share_cancellation_shares_mn": 15.3, "treasury_share_cancellation_outstanding_pct": 2.1, "share_gain_2025_pct": 274, "share_gain_2026_to_may_pct": 200, "market_cap_may_2026_usd_bn": 942},
        score_price_alignment="aligned",
        round_alignment_label="aligned_structural_but_4B_watch",
        rerating_result="true_rerating",
        round_rerating_label="HBM_dominance_stage3_candidate",
        stage_failure_type="yellow_success",
        round_stage_failure_label="expectations_and_valuation_overshoot_after_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="HBM success is structural, but extreme rerating requires 4B-watch after the evidence works.",
    ),
    Round284CaseCandidate(
        case_id="r2_loop14_samsung_hbm_catchup_labor_4c_watch",
        symbol="005930",
        company_name="Samsung Electronics HBM catch-up and labor risk",
        primary_archetype=E2RArchetype.SAMSUNG_HBM_CATCHUP_AND_LABOR_4C_WATCH,
        secondary_archetypes=(E2RArchetype.SAMSUNG_HBM_CATCHUP_LAG_AND_LABOR_4C, E2RArchetype.HBM_CATCHUP_EXECUTION_RISK),
        case_type="success_candidate",
        round_case_type="success_candidate + 4C-watch",
        stage1_date=date(2024, 10, 1),
        stage2_date=date(2026, 5, 6),
        stage3_date=None,
        stage4b_date=date(2026, 5, 6),
        stage4c_date=date(2025, 1, 31),
        stage3_decision="HBM_catchup_and_AI_rally_are_not_green_until_qualification_export_control_and_labor_gates_clear",
        stage4b_status="4B-watch/4C-watch/HBM-catchup-labor-export-control",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=True,
        evidence_fields=("Samsung_market_cap_1trn_usd", "KOSPI_7000_session_Samsung_plus_14_4pct", "AI_memory_rally_broadens", "semiconductor_export_share_37pct"),
        red_flag_fields=("HBM_qualification_lag", "China_HBM_export_restriction", "HBM_China_customer_share_20pct", "strike_threat_50000_workers_18_days", "foundry_logic_drag"),
        price_data_source="Reuters Samsung HBM/export restriction, KOSPI 7000 and strike anchors",
        reported_price_anchor="2025 AI-chip warning -2.8%; 2026 KOSPI 7000 +14.4%; strike intraday -6%",
        reported_return_anchor="Samsung catch-up has Stage 2 evidence, but China, qualification and labor gates remain hard watches.",
        event_mfe_pct=14.4,
        event_mae_pct=-6.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hbm_china_customer_share_context_pct": 20, "q1_2025_ai_chip_warning_event_mae_pct": -2.8, "sk_hynix_same_context_mae_pct": -9.6, "samsung_1t_marketcap_event_mfe_pct": 12.0, "kospi_7000_session_samsung_mfe_pct": 14.4, "kospi_7000_session_sk_hynix_mfe_pct": 10.6, "samsung_market_cap_may_2026_usd_trn": 1.0, "semiconductor_export_share_apr_2026_pct": 37, "strike_threat_workers": 50000, "strike_duration_days": 18, "strike_news_intraday_mae_pct": -6.0, "strike_news_close_mfe_pct": 1.8, "sk_hynix_same_strike_context_mfe_pct": 7.7},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_with_hard_gate",
        rerating_result="unknown",
        round_rerating_label="Samsung_HBM_catchup_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="HBM_lag_China_restriction_labor_continuity_gate",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Catch-up rally needs qualification, export-control and labor-continuity clearance before Green.",
    ),
    Round284CaseCandidate(
        case_id="r2_loop14_hanmi_tc_bonder_hbm_equipment_4b",
        symbol="042700",
        company_name="Hanmi Semiconductor TC bonder",
        primary_archetype=E2RArchetype.TC_BONDER_HBM_EQUIPMENT_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA, E2RArchetype.HBM_EQUIPMENT_CARVEOUT_NOT_GREEN),
        case_type="4b_watch",
        round_case_type="structural_success_candidate + rumor 4B",
        stage1_date=date(2024, 3, 26),
        stage2_date=date(2024, 3, 26),
        stage3_date=None,
        stage4b_date=date(2024, 3, 28),
        stage4c_date=None,
        stage3_decision="confirmed_SK_Hynix_contracts_are_Stage2_but_Micron_rumor_is_not_PO_revenue_green",
        stage4b_status="4B-watch/unconfirmed-customer-rumor",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("TSV_TC_bonder", "SK_Hynix_supply_deal_21_48bn_krw", "recent_contract_wins_total_200bn_krw", "stage2_event_plus_16pct"),
        red_flag_fields=("rumored_customer_PO", "Micron_deal_unconfirmed", "shipment_revenue_unconfirmed", "customer_diversification_gate"),
        price_data_source="WSJ Hanmi HBM equipment and Micron-rumor event anchors",
        reported_price_anchor="+16% on HBM equipment context; +22% to 139,100 KRW on unconfirmed Micron reports",
        reported_return_anchor="Actual SK Hynix contract supports Stage 2; Micron rumor is 4B-watch.",
        event_mfe_pct=22.0,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=139100,
        stage4c_price_anchor=None,
        extra_price_metrics={"stage2_event_mfe_pct": 16.0, "kospi_stage2_context_pct": 0.7, "sk_hynix_supply_deal_krw_bn": 21.48, "recent_contract_wins_total_krw_bn": 200, "micron_rumor_event_high_price_krw": 139100, "micron_rumor_event_mfe_pct": 22.0, "kospi_micron_rumor_context_pct": -0.3, "relative_outperformance_micron_rumor_pp": 22.3, "micron_deal_confirmed_at_source_date": False, "shipment_revenue_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_but_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="HBM_equipment_TC_bonder_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="Micron_rumor_not_customer_PO_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Confirmed SK Hynix orders are Stage 2, while unconfirmed customer rumor is not PO/revenue Green.",
    ),
    Round284CaseCandidate(
        case_id="r2_loop14_lg_innotek_ai_iphone_component_price_failed",
        symbol="011070",
        company_name="LG Innotek AI iPhone component",
        primary_archetype=E2RArchetype.ON_DEVICE_AI_IPHONE_COMPONENT_STAGE2,
        secondary_archetypes=(E2RArchetype.AI_DEVICE_COMPONENT_OPTIONALITY, E2RArchetype.CAMERA_LIDAR_ADAS_ELECTRONICS),
        case_type="failed_rerating",
        round_case_type="evidence_good_but_price_failed",
        stage1_date=date(2024, 6, 27),
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="Apple_AI_iPhone_expectation_and_OP_estimate_beat_did_not_get_price_confirmation",
        stage4b_status="watch/iPhone-AI-theme-before-sellthrough",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Apple_Intelligence_iPhone_16_cycle", "Q2_OP_estimate_106_4bn_krw", "OP_estimate_31_2pct_above_consensus", "target_price_raise_18pct"),
        red_flag_fields=("on_device_AI_expectation_only", "device_sellthrough_unconfirmed", "component_mix_margin_unconfirmed", "event_price_minus_0_4pct"),
        price_data_source="MarketWatch/Dow Jones LG Innotek event anchor",
        reported_price_anchor="272,000 KRW, -0.4%; target 330,000 KRW",
        reported_return_anchor="Good estimate evidence did not validate price; sell-through and component margin required.",
        event_mfe_pct=None,
        event_mae_pct=-0.4,
        stage1_price_anchor=None,
        stage2_price_anchor=272000,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_price_krw": 272000, "q2_op_estimate_krw_bn": 106.4, "q2_op_consensus_krw_bn": 81.1, "op_estimate_above_consensus_pct": 31.2, "target_price_krw": 330000, "target_price_raise_pct": 18, "target_upside_from_event_price_pct": 21.3, "ai_iphone_sellthrough_confirmed": False, "component_mix_margin_confirmed": False},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        round_rerating_label="on_device_AI_iPhone_component_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="AI_iPhone_expectation_not_component_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="AI iPhone expectation needs device sell-through, component content, inventory and margin before Green.",
    ),
    Round284CaseCandidate(
        case_id="r2_loop14_lg_display_oled_restructuring_stage2",
        symbol="034220",
        company_name="LG Display OLED restructuring",
        primary_archetype=E2RArchetype.OLED_PORTFOLIO_RESTRUCTURING_STAGE2,
        secondary_archetypes=(E2RArchetype.DISPLAY_LCD_EXIT_OLED_TURNAROUND, E2RArchetype.DISPLAY_OLED_SUPPLYCHAIN),
        case_type="success_candidate",
        round_case_type="success_candidate + capex/utilization gate",
        stage1_date=date(2024, 9, 26),
        stage2_date=date(2024, 9, 26),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="LCD_exit_and_OLED_capex_are_stage2_not_utilization_cashflow_green",
        stage4b_status="watch/OLED-capex-before-utilization",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Guangzhou_LCD_sale_10_8bn_cny", "Guangzhou_LCD_sale_1_54bn_usd", "OLED_infrastructure_investment_1_1trn_krw", "balance_sheet_repair_path"),
        red_flag_fields=("capacity_capex_without_utilization", "OLED_utilization_unconfirmed", "OLED_margin_unconfirmed", "direct_event_return_unavailable"),
        price_data_source="Reuters LCD sale and OLED capex anchors",
        reported_price_anchor="Guangzhou LCD sale $1.54B; OLED capex 1.1T KRW",
        reported_return_anchor="LCD exit/OLED capex supports Stage 2; utilization and FCF required.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"guangzhou_lcd_sale_cny_bn": 10.8, "guangzhou_lcd_sale_usd_bn": 1.54, "large_lcd_panel_stake_sold_pct": 80, "lcd_module_plant_stake_sold_pct": 100, "expected_completion": "2025-03", "oled_infrastructure_investment_krw_trn": 1.1, "oled_infrastructure_investment_usd_mn": 744.94, "investment_period": "2026-04_to_2028-06", "oled_utilization_confirmed": False, "oled_margin_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_capex_gate",
        rerating_result="unknown",
        round_rerating_label="OLED_portfolio_restructuring_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="LCD_exit_OLED_capex_not_utilization_green",
        price_validation_status="direct_event_return_unavailable_after_deep_search",
        notes="LCD exit and OLED capex are Stage 2 until utilization, customer demand, margin and FCF are visible.",
    ),
    Round284CaseCandidate(
        case_id="r2_loop14_rebellions_sapeon_korean_ai_chip_stage2",
        symbol="017670/030200/000660_readthrough",
        company_name="Rebellions / Sapeon Korean AI chip",
        primary_archetype=E2RArchetype.KOREAN_AI_CHIP_FABLESS_STAGE2,
        secondary_archetypes=(E2RArchetype.AI_CHIP_DESIGN_UNLISTED_MERGER_STAGE2, E2RArchetype.CUSTOM_AI_ASIC_HYPERSCALER),
        case_type="success_candidate",
        round_case_type="success_candidate + insufficient_evidence",
        stage1_date=date(2024, 6, 12),
        stage2_date=date(2024, 8, 18),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="unlisted_AI_chip_merger_is_not_listed_stock_EPS_green",
        stage4b_status="watch/unlisted-AI-chip-readthrough",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("Rebellions_Sapeon_merger", "Waed_Ventures_investment_15mn_usd", "total_funding_over_225mn_usd", "ATOM_NPU_LLM_data_center_mass_production"),
        red_flag_fields=("unlisted_AI_chip_readthrough", "listed_stock_direct_revenue_unconfirmed", "customer_workload_revenue_unconfirmed", "gross_margin_unconfirmed"),
        price_data_source="Reuters Rebellions-Sapeon merger anchors",
        reported_price_anchor="No direct listed-stock price anchor; merger/funding/source evidence stored.",
        reported_return_anchor="Korean AI chip merger is Stage 2, but listed EPS bridge is absent.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"sapeon_parent": "SK Telecom", "sapeon_shareholders_include": ["SK Telecom", "SK Hynix"], "merger_definitive_agreement_date": "2024-08-18", "waed_ventures_investment_usd_mn": 15, "total_funding_usd_mn": 225, "atom_chip_status": "first South Korean NPU used in data center for LLM; entered mass production", "listed_stock_direct_revenue_confirmed": False, "customer_workload_revenue_confirmed": False, "direct_event_price_anchor": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_insufficient_evidence",
        rerating_result="unknown",
        round_rerating_label="Korean_AI_chip_fabless_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="unlisted_AI_chip_merger_not_listed_EPS_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Merger and funding are Stage 2; listed-stock Green needs production, workload revenue, margin and EPS bridge.",
    ),
    Round284CaseCandidate(
        case_id="r2_loop14_samsung_sk_openai_stargate_memory_mou_4b",
        symbol="005930/000660",
        company_name="Samsung / SK Hynix OpenAI Stargate memory LOI",
        primary_archetype=E2RArchetype.AI_INFRA_MEMORY_SUPPLY_MOU_4B,
        secondary_archetypes=(E2RArchetype.OPENAI_STARGATE_AI_CAPEX_EVENT, E2RArchetype.MEMORY_SUPERCYCLE_AI_CAPEX),
        case_type="event_premium",
        round_case_type="event_premium + 4B-watch",
        stage1_date=date(2025, 10, 1),
        stage2_date=date(2025, 10, 1),
        stage3_date=None,
        stage4b_date=date(2025, 10, 1),
        stage4c_date=None,
        stage3_decision="OpenAI_wafer_demand_LOI_is_not_binding_take_or_pay_margin_green",
        stage4b_status="4B-watch/AI-memory-MOU-LOI-before-binding-terms",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=False,
        evidence_fields=("OpenAI_Stargate_LOI", "SK_Hynix_close_plus_10pct", "Samsung_plus_3_5pct", "OpenAI_DRAM_wafer_demand_900000_per_month"),
        red_flag_fields=("LOI_or_MOU_without_binding_contract", "binding_take_or_pay_contract_unconfirmed", "ASP_margin_terms_unconfirmed", "wafer_demand_headline_not_calloff"),
        price_data_source="FT OpenAI Stargate LOI price-reaction anchor",
        reported_price_anchor="SK Hynix intraday +12%, close +10%; Samsung +3.5%",
        reported_return_anchor="LOI is demand signal, not binding call-off/margin Green.",
        event_mfe_pct=12.0,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"sk_hynix_intraday_mfe_pct": 12.0, "sk_hynix_close_mfe_pct": 10.0, "samsung_event_mfe_pct": 3.5, "openai_dram_wafer_demand_per_month": 900000, "demand_context": "more_than_twice_current_HBM_industry_capacity_in_source_summary", "binding_take_or_pay_contract_confirmed": False, "asp_margin_terms_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="AI_infra_memory_supply_MOU_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="LOI_wafer_demand_headline_not_binding_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="OpenAI/Stargate LOI is a powerful demand signal, but Green needs binding terms, allocation, ASP and shipment schedule.",
    ),
    Round284CaseCandidate(
        case_id="r2_loop14_lg_electronics_component_cost_4c_watch",
        symbol="066570",
        company_name="LG Electronics component-cost pressure",
        primary_archetype=E2RArchetype.CONSUMER_ELECTRONICS_COMPONENT_COST_4C_WATCH,
        secondary_archetypes=(E2RArchetype.AI_DATA_CENTER_COOLING, E2RArchetype.RETAIL_DOMESTIC_CONSUMER),
        case_type="failed_rerating",
        round_case_type="4C-watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 1, 30),
        stage3_decision="AI_memory_shortage_can_help_suppliers_but_hurt_OEM_component_margin",
        stage4b_status="4C-watch/component-cost-OEM-margin-pressure",
        hard_4c_confirmed=False,
        hard_4c_watch_confirmed=True,
        evidence_fields=("B2B_data_center_cooling_optionality", "Q4_2025_revenue_23_852trn_krw", "revenue_growth_4_8pct"),
        red_flag_fields=("component_cost_spike_crushing_OEM_margins", "Q4_2025_operating_loss_109bn_krw", "Q4_2025_net_loss_725_9bn_krw", "weak_consumer_demand", "semiconductor_shortages"),
        price_data_source="WSJ LG Electronics earnings anchor",
        reported_price_anchor="Q4 2025 operating loss 109B KRW; net loss 725.9B KRW; no direct event return",
        reported_return_anchor="Memory shortage can pressure OEM margins; B2B/cooling optionality is not enough.",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"q4_2025_net_loss_krw_bn": 725.90, "q4_2025_revenue_krw_trn": 23.852, "q4_2025_revenue_growth_pct": 4.8, "q4_2025_operating_loss_krw_bn": 109.00, "first_operating_loss_in_years": 9, "media_entertainment_annual_operating_loss_krw_bn": 750.90, "flagged_risks": ["semiconductor shortages", "rising component costs", "weak consumer demand"], "b2b_data_center_cooling_optional": True, "direct_event_return": "price_data_unavailable_after_deep_search"},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="consumer_electronics_component_cost_gate",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="AI_memory_shortage_benefits_suppliers_but_pressures_OEM_margin",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="AI memory shortage helps suppliers but can be a component-cost 4C-watch for OEM margins.",
    ),
)


def round284_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND284_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND284_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round284 R2 Loop-14 AI/semiconductor/electronics price-validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=candidate.evidence_fields if candidate.stage3_date else (),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("mou", "loi", "rumor", "rally", "valuation", "market_cap", "ipo", "overheat", "expectation"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("strike", "export", "restriction", "loss", "cost", "qualification", "4c", "cash", "margin"))),
            must_have_fields=ROUND284_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type != "structural_success" else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND284_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "hard_4c_confirmed_false",
                "hard_4c_watch_confirmed_true",
                "do_not_use_round284_cases_as_candidate_generation_input",
                "do_not_treat_AI_HBM_OpenAI_Apple_OLED_or_AI_chip_keywords_as_green",
                *ROUND284_GREEN_REQUIRED_FIELDS,
                *ROUND284_GREEN_FORBIDDEN_PATTERNS,
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


def round284_case_rows() -> tuple[dict[str, str], ...]:
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
            "hard_4c_watch_confirmed": str(candidate.hard_4c_watch_confirmed).lower(),
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
        for candidate in ROUND284_CASE_CANDIDATES
    )


def round284_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND284_SCORE_ADJUSTMENTS)


def round284_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND284_SHADOW_WEIGHT_ROWS)


def round284_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND284_DEEP_SUB_ARCHETYPES)


def round284_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round284_price_validation": "true"} for field in ROUND284_PRICE_VALIDATION_FIELDS)


def round284_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round284_label": label, "canonical_archetype": canonical} for label, canonical in ROUND284_REQUIRED_TARGET_ALIASES.items())


def round284_summary() -> dict[str, int | bool | str]:
    cases = ROUND284_CASE_CANDIDATES
    return {
        "source_round": ROUND284_SOURCE_ROUND_PATH,
        "round_id": ROUND284_ANALYST_ROUND_ID,
        "large_sector": ROUND284_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "event_premium_or_result_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "hard_4c_watch_case_count": sum(1 for case in cases if case.hard_4c_watch_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "unknown_alignment_count": sum(1 for case in cases if case.score_price_alignment == "unknown"),
        "aligned_count": sum(1 for case in cases if case.score_price_alignment == "aligned"),
        "target_archetype_count": len(ROUND284_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND284_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND284_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
        "hard_4c_watch_confirmed": any(case.hard_4c_watch_confirmed for case in cases),
    }


def round284_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND284_SOURCE_ROUND_PATH,
        "round_id": ROUND284_ANALYST_ROUND_ID,
        "large_sector": ROUND284_LARGE_SECTOR,
        "summary": round284_summary(),
        "target_aliases": dict(ROUND284_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND284_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND284_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND284_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND284_HARD_4C_GATES),
        "score_adjustments": list(round284_score_adjustment_rows()),
        "shadow_weights": list(round284_shadow_weight_rows()),
        "deep_sub_archetypes": list(round284_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND284_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round284_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_AI_HBM_OpenAI_Apple_OLED_or_AI_chip_keywords_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round284_summary_markdown() -> str:
    summary = round284_summary()
    lines = [
        "# Round 284 R2 Loop 14 AI Semiconductor Electronic Components Price Validation",
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
        f"- hard_4c_watch: {summary['hard_4c_watch_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND284_CASE_CANDIDATES:
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
            "- SK Hynix is the structural HBM success case, but its later valuation/crowding requires 4B-watch.",
            "- Samsung Electronics is a catch-up candidate with export-control, qualification and labor-continuity gates.",
            "- Hanmi, OpenAI Stargate and AI-chip read-through cases separate Stage 2 demand signals from binding PO/revenue.",
            "- LG Innotek and LG Electronics show AI demand can fail price confirmation or become component-cost pressure.",
            "- LG Display needs OLED utilization and FCF; LCD exit and capex are not Green by themselves.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round284_green_gate_review_markdown() -> str:
    lines = [
        "# Round 284 R2 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R2 Stage 3-Green is not `AI`, `HBM`, `Nvidia`, `OpenAI`, `Apple AI`, `OLED`, or `AI chip startup` as a label. It requires allocation, delivery, ASP/mix, PO-to-revenue, sell-through, utilization, component margin and labor continuity.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND284_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND284_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND284_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `HBM sold out` becomes stronger when OP, ASP/mix and shipment evidence appear together.",
            "- `OpenAI LOI` is a demand signal, but Green waits for binding call-off, margin and shipment schedule.",
            "- `Apple Intelligence` helps a component thesis only if device sell-through and component margin confirm.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round284_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 284 R2 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND284_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C / Strong Watch Gates", ""])
    lines.extend(f"- {field}" for field in ROUND284_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | hard 4C watch | interpretation |", "|---|---|---|---|---|---|"])
    for case in ROUND284_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {str(case.hard_4c_watch_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round284_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 284 R2 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, full MFE/MAE, HBM shipment, ASP/mix, PO, sell-through, utilization, binding OpenAI terms, or labor-continuity evidence where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND284_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND284_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round284_r2_loop14_reports(
    output_directory: str | Path = ROUND284_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND284_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND284_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round284_case_records(), cases_path),
        "audit": _write_json(round284_audit_payload(), audit_path),
        "summary": output / "round284_r2_loop14_price_validation_summary.md",
        "case_matrix": output / "round284_r2_loop14_case_matrix.csv",
        "target_aliases": output / "round284_r2_loop14_target_aliases.csv",
        "score_adjustments": output / "round284_r2_loop14_score_adjustments.csv",
        "shadow_weights": output / "round284_r2_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round284_r2_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round284_r2_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round284_r2_loop14_green_gate_review.md",
        "price_validation_plan": output / "round284_r2_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round284_r2_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round284_summary_markdown(), encoding="utf-8")
    _write_csv(round284_case_rows(), paths["case_matrix"])
    _write_csv(round284_target_alias_rows(), paths["target_aliases"])
    _write_csv(round284_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round284_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round284_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round284_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round284_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round284_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round284_stage4b_4c_review_markdown(), encoding="utf-8")
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
    "ROUND284_CASE_CANDIDATES",
    "ROUND284_GREEN_FORBIDDEN_PATTERNS",
    "ROUND284_GREEN_REQUIRED_FIELDS",
    "ROUND284_HARD_4C_GATES",
    "ROUND284_LARGE_SECTOR",
    "ROUND284_PRICE_VALIDATION_FIELDS",
    "ROUND284_REQUIRED_TARGET_ALIASES",
    "ROUND284_SHADOW_WEIGHT_ROWS",
    "ROUND284_STAGE4B_WATCH_TRIGGERS",
    "render_round284_green_gate_review_markdown",
    "render_round284_stage4b_4c_review_markdown",
    "round284_audit_payload",
    "round284_case_records",
    "round284_case_rows",
    "round284_deep_sub_archetype_rows",
    "round284_shadow_weight_rows",
    "round284_summary",
    "write_round284_r2_loop14_reports",
]
