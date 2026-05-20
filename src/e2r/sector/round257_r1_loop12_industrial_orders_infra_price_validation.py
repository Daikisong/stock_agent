"""Round-257 R1 Loop-12 industrial orders/infrastructure validation pack.

Round 257 converts ``docs/round/round_257.md`` into structured,
calibration-only case records. It does not change production scoring.

Easy example: a defense order is not Stage 3 by itself. For R1, the chain has
to close as order -> delivery -> revenue -> margin -> cash collection -> repeat
orders. If a company announces a large factory or rights offering before those
steps are proven, it remains Stage 2 or 4B-watch, not Green.
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


ROUND257_SOURCE_ROUND_PATH = "docs/round/round_257.md"
ROUND257_ROUND_ID = "round_185"
ROUND257_LARGE_SECTOR = "INDUSTRIAL_ORDERS_INFRA"
ROUND257_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round257_r1_loop12_industrial_orders_infra_price_validation"
ROUND257_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop12_round257.jsonl"
ROUND257_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round257_r1_loop12_industrial_orders_infra_price_validation_audit.json"

ROUND257_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "DEFENSE_EXPORT_BACKLOG_COMPOUNDING": E2RArchetype.DEFENSE_EXPORT_BACKLOG_COMPOUNDING.value,
    "MISSILE_DEFENSE_COMBAT_VALIDATION": E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION.value,
    "ARMORED_VEHICLE_DELIVERY_TO_REVENUE": E2RArchetype.ARMORED_VEHICLE_DELIVERY_TO_REVENUE.value,
    "GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK": E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK.value,
    "US_GRID_EQUIPMENT_LOCALIZATION": E2RArchetype.US_GRID_EQUIPMENT_LOCALIZATION.value,
    "OVERSEAS_EPC_MEGA_ORDER": E2RArchetype.OVERSEAS_EPC_MEGA_ORDER.value,
    "POLICY_CAPEX_FALSE_POSITIVE": E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE.value,
    "DILUTION_AFTER_RERATING_4B": E2RArchetype.DILUTION_AFTER_RERATING_4B.value,
}

ROUND257_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "confirmed_order",
    "delivery_schedule_confirmed",
    "delivery_to_revenue_or_progress_revenue_confirmed",
    "opm_or_gross_margin_confirmed",
    "working_capital_receivables_cash_collection_stable",
    "local_production_economics_confirmed",
    "capex_dilution_risk_passed",
    "repeat_customer_aftermarket_mro_revenue_confirmed",
    "price_path_after_evidence",
)

ROUND257_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "contract_headline_only",
    "policy_capex_only",
    "factory_investment_only",
    "local_production_margin_unknown",
    "dilution_shock_present",
    "working_capital_deterioration",
    "geopolitical_headline_only",
)

ROUND257_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "contract_announcement_plus_5_to_10pct",
    "record_high_after_defense_order",
    "large_capital_raise_after_rerating",
    "geopolitical_defense_rally_plus_30_to_50pct",
    "large_backlog_without_delivery_margin",
    "epc_mega_order_before_margin_cash_collection",
    "grid_shortage_theme_before_margin_delivery",
    "local_production_priced_before_profitability",
)

ROUND257_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "export_license_failure",
    "customer_budget_cancellation",
    "delivery_delay",
    "local_production_margin_failure",
    "working_capital_blowout",
    "large_dilution_without_clear_roi",
    "policy_capex_failure",
    "factory_ramp_failure",
    "geopolitical_customer_payment_risk",
    "epc_loss_recognition",
)

ROUND257_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "mfe_30d",
    "mae_30d",
    "contract_value_anchor",
    "backlog_anchor",
    "dilution_anchor",
    "policy_capex_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round257ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round257ShadowWeightRow:
    archetype: E2RArchetype
    confirmed_order: int
    delivery_to_revenue: int
    backlog_compounding: int
    local_production_economics: int
    mro_aftermarket: int
    production_capacity: int
    cash_collection: int
    working_capital: int
    repeat_customer: int
    price_path_alignment: int
    event_penalty: int
    dilution_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "confirmed_order": _signed(self.confirmed_order),
            "delivery_to_revenue": _signed(self.delivery_to_revenue),
            "backlog_compounding": _signed(self.backlog_compounding),
            "local_production_economics": _signed(self.local_production_economics),
            "mro_aftermarket": _signed(self.mro_aftermarket),
            "production_capacity": _signed(self.production_capacity),
            "cash_collection": _signed(self.cash_collection),
            "working_capital": _signed(self.working_capital),
            "repeat_customer": _signed(self.repeat_customer),
            "price_path_alignment": _signed(self.price_path_alignment),
            "event_penalty": _signed(self.event_penalty),
            "dilution_redteam": _signed(self.dilution_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round257DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round257CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    source_sector: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
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
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    peak_price_anchor: float | None
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


ROUND257_SCORE_ADJUSTMENTS: tuple[Round257ScoreAdjustment, ...] = (
    Round257ScoreAdjustment("confirmed_order", 5, "raise", "확정 수주는 Stage 1 headline보다 강한 Stage 2 증거다."),
    Round257ScoreAdjustment("delivery_to_revenue", 5, "raise", "납품이 매출로 내려와야 Stage 3 후보가 된다."),
    Round257ScoreAdjustment("backlog_compounding", 5, "raise", "수주잔고가 누적되고 반복 고객이 확인되면 visibility가 오른다."),
    Round257ScoreAdjustment("local_production_economics", 4, "raise", "현지생산은 마진과 수익성이 확인될 때만 긍정이다."),
    Round257ScoreAdjustment("MRO_or_aftermarket_revenue", 4, "raise", "MRO·aftermarket은 방산·인프라 수주의 반복성을 높인다."),
    Round257ScoreAdjustment("production_capacity_visibility", 4, "raise", "생산 슬롯·CAPA 가시성은 납품 가능성을 높인다."),
    Round257ScoreAdjustment("cash_collection_quality", 5, "raise", "EPC·방산·전력기기는 현금회수가 핵심이다."),
    Round257ScoreAdjustment("working_capital_control", 5, "raise", "운전자본이 망가지면 수주는 이익이 되어도 FCF가 안 된다."),
    Round257ScoreAdjustment("repeat_export_customer", 4, "raise", "반복 해외 고객은 일회성 order risk를 낮춘다."),
    Round257ScoreAdjustment("price_path_alignment", 5, "raise", "증거 이후 가격경로가 따라와야 score-price alignment가 생긴다."),
    Round257ScoreAdjustment("contract_headline_only", -5, "lower", "수주 headline만으로는 Green 금지다."),
    Round257ScoreAdjustment("policy_capex_without_funding", -5, "lower", "정책 CAPEX는 자금조달·수요·마진이 없으면 false positive다."),
    Round257ScoreAdjustment("local_production_without_margin", -4, "lower", "현지생산은 마진 불명확 시 감점한다."),
    Round257ScoreAdjustment("defense_rally_without_delivery", -4, "lower", "전쟁·방산 rally가 납품·마진보다 앞서면 4B-watch다."),
    Round257ScoreAdjustment("EPC_order_without_working_capital", -5, "lower", "EPC 수주는 운전자본·공정률·마진 전 Stage 2다."),
    Round257ScoreAdjustment("capacity_expansion_without_order", -4, "lower", "CAPA 증설만 있고 firm order가 없으면 Green 차단이다."),
    Round257ScoreAdjustment("dilution_after_rerating", -5, "lower", "리레이팅 후 대형 증자는 4B/dilution watch다."),
    Round257ScoreAdjustment("unconfirmed_geopolitical_replenishment", -4, "lower", "지정학 보충수요는 실제 주문 전까지 과신하면 안 된다."),
    Round257ScoreAdjustment("input_cost_unknown", -3, "lower", "구리·GOES·후판·원가 미확인은 마진 리스크다."),
)


ROUND257_SHADOW_WEIGHT_ROWS: tuple[Round257ShadowWeightRow, ...] = (
    Round257ShadowWeightRow(E2RArchetype.DEFENSE_EXPORT_BACKLOG_COMPOUNDING, 5, 5, 5, 4, 4, 4, 5, 5, 4, 5, -2, 5, 5, 4, "Hanwha shows strong Stage 2 but delivery/margin/cash collection and dilution must clear."),
    Round257ShadowWeightRow(E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION, 5, 4, 5, 4, 5, 5, 5, 4, 5, 5, -2, 2, 5, 4, "LIG Nex1 has Iraq/Saudi orders and geopolitical validation, but replenishment/margin must confirm."),
    Round257ShadowWeightRow(E2RArchetype.ARMORED_VEHICLE_DELIVERY_TO_REVENUE, 5, 5, 5, 4, 4, 4, 5, 5, 5, 5, -2, 2, 4, 4, "Hyundai Rotem has delivery-to-revenue evidence; local production economics remain key."),
    Round257ShadowWeightRow(E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK, 5, 4, 4, 2, 2, 5, 5, 5, 4, 4, -2, 1, 4, 4, "LS Electric benefits from data-center transformer bottleneck but needs margin/input-cost/delivery proof."),
    Round257ShadowWeightRow(E2RArchetype.US_GRID_EQUIPMENT_LOCALIZATION, 4, 3, 4, 4, 2, 5, 4, 5, 4, 3, -3, 2, 4, 4, "Hyosung/HICO capacity localization is Stage 2 until utilization/order book/FCF confirm."),
    Round257ShadowWeightRow(E2RArchetype.OVERSEAS_EPC_MEGA_ORDER, 5, 5, 4, 2, 1, 3, 5, 5, 4, 5, -5, 2, 5, 5, "Samsung E&A shows EPC contract headline is not Green without margin/cash collection."),
    Round257ShadowWeightRow(E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE, 2, 1, 1, 1, 0, 3, 3, 5, 1, 5, -5, 4, 5, 5, "Hyundai Steel U.S. plant is policy CAPEX false positive due funding and strategy uncertainty."),
    Round257ShadowWeightRow(E2RArchetype.DILUTION_AFTER_RERATING_4B, 0, 0, 0, 0, 0, 2, 3, 5, 0, 4, -5, 5, 5, 4, "Hanwha capital raise after rerating requires 4B/dilution penalty."),
)


ROUND257_DEEP_SUB_ARCHETYPES: tuple[Round257DeepSubArchetype, ...] = (
    Round257DeepSubArchetype("방산 수주잔고", E2RArchetype.DEFENSE_EXPORT_BACKLOG_COMPOUNDING, ("Hanwha Aerospace", "Romania K9", "K10", "land-defense backlog", "dilution watch")),
    Round257DeepSubArchetype("미사일 방어", E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION, ("LIG Nex1", "Iraq Cheongung-II", "M-SAM II", "Saudi order", "geopolitical 4B-watch")),
    Round257DeepSubArchetype("전차 납품", E2RArchetype.ARMORED_VEHICLE_DELIVERY_TO_REVENUE, ("Hyundai Rotem", "Poland K2", "18 tanks shipped", "second contract", "local production margin")),
    Round257DeepSubArchetype("전력망 변압기", E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK, ("LS Electric", "525kV transformer", "U.S. data center", "GSU demand", "lead time")),
    Round257DeepSubArchetype("미국 현지화", E2RArchetype.US_GRID_EQUIPMENT_LOCALIZATION, ("Hyosung HICO", "U.S. grid-equipment localization", "143 weeks lead time", "factory utilization")),
    Round257DeepSubArchetype("해외 EPC", E2RArchetype.OVERSEAS_EPC_MEGA_ORDER, ("Samsung E&A", "Saudi Aramco Fadhili", "progress revenue", "working capital")),
    Round257DeepSubArchetype("정책 CAPEX 반례", E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE, ("Hyundai Steel", "Louisiana plant", "funding unclear", "tariff hedge", "drawdown")),
    Round257DeepSubArchetype("증자 4B", E2RArchetype.DILUTION_AFTER_RERATING_4B, ("Hanwha Aerospace", "3.6T capital raise", "rights offering", "FSS revision order")),
)


ROUND257_CASE_CANDIDATES: tuple[Round257CaseCandidate, ...] = (
    Round257CaseCandidate(
        case_id="r1_loop12_hanwha_aerospace_romania_k9_dilution_watch",
        symbol="012450",
        company_name="Hanwha Aerospace",
        source_sector="R1",
        primary_archetype=E2RArchetype.DEFENSE_EXPORT_BACKLOG_COMPOUNDING,
        secondary_archetypes=(E2RArchetype.DILUTION_AFTER_RERATING_4B, E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH),
        case_type="success_candidate",
        stage1_date=date(2022, 1, 1),
        stage2_date=date(2024, 7, 10),
        stage3_date=None,
        stage4b_date=date(2024, 7, 10),
        stage4c_date=None,
        stage3_decision="backlog_compounding_is_strong_but_delivery_margin_working_capital_local_production_cash_collection_required_before_green",
        stage4b_status="4B-watch/dilution",
        hard_4c_confirmed=False,
        evidence_fields=("romania_k9_order_1_38tn_krw", "54_k9_36_k10_ammunition_support", "contract_until_2029_07", "land_defense_backlog_5_1tn_to_30tn"),
        red_flag_fields=("record_high_event_rally", "capital_raise_3_6tn_krw", "capital_raise_event_mae_minus_13pct", "dilution_after_rerating"),
        price_data_source="Reuters order / event-return / dilution anchors",
        reported_price_anchor="Shares rose more than 5% to a record high; later capital raise shock -13%",
        reported_return_anchor="Romania K9 1.38T KRW / $1.0B; backlog 5.1T -> about 30T KRW",
        mfe_1d=5.0,
        mae_1d=-13.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"romania_contract_krw_trn": 1.38, "romania_contract_usd_bn": 1.0, "k9_howitzers": 54.0, "k10_resupply_vehicles": 36.0, "contract_end_year": 2029.0, "stage2_event_mfe_pct": 5.0, "market_same_context_pct": -0.1, "relative_outperformance_pp": 5.1, "backlog_end_2021_krw_trn": 5.1, "backlog_march_2024_krw_trn": 30.0, "backlog_growth_pct": 488.2, "capital_raise_initial_krw_trn": 3.6, "capital_raise_initial_usd_bn": 2.46, "capital_raise_event_mae_pct": -13.0, "revised_rights_offering_krw_trn": 2.3, "affiliate_share_issue_krw_trn": 1.3},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_with_4B_dilution_watch",
        rerating_result="unknown",
        round_rerating_label="defense_backlog_compounding_but_capital_raise_risk",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_strong_not_green_until_delivery_margin_cash",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="방산 수주잔고는 강하지만 대형 증자와 현금회수 리스크가 있어 Green 전 4B-watch를 병행한다.",
    ),
    Round257CaseCandidate(
        case_id="r1_loop12_lig_nex1_iraq_cheongung_missile_defense",
        symbol="079550",
        company_name="LIG Nex1",
        source_sector="R1",
        primary_archetype=E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION,
        secondary_archetypes=(E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH,),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 9, 20),
        stage3_date=None,
        stage4b_date=date(2026, 1, 1),
        stage4c_date=None,
        stage3_decision="iraq_order_and_combat_validation_are_stage2_but_delivery_missile_production_rate_margin_replenishment_and_cash_collection_required",
        stage4b_status="4B-watch/geopolitical",
        hard_4c_confirmed=False,
        evidence_fields=("iraq_missile_system_order_3_71tn_krw", "saudi_prior_msam_order", "cheongung_cost_advantage", "production_cycle_advantage"),
        red_flag_fields=("geopolitical_defense_rally_without_delivery", "unconfirmed_replenishment_demand", "margin_cash_collection_unknown"),
        price_data_source="Reuters Iraq order anchor / FT geopolitical rerating anchor",
        reported_price_anchor="Iraq order +3.6% vs KOSPI +0.9%; Iran-war context nearly +47%",
        reported_return_anchor="Iraq order 3.71T KRW / $2.8B; prior Saudi $3.2B order",
        mfe_1d=3.6,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"iraq_contract_krw_trn": 3.71, "iraq_contract_usd_bn": 2.8, "event_mfe_pct": 3.6, "kospi_same_context_pct": 0.9, "relative_outperformance_pp": 2.7, "saudi_prior_contract_usd_bn": 3.2, "iran_war_return_context_pct": 47.0, "cheongung_unit_price_usd_mn": 1.1, "patriot_pac3_unit_price_usd_mn": 3.7, "relative_cost_advantage_pct": 70.3, "lig_scalable_months_low": 9.0, "lig_scalable_months_high": 12.0, "patriot_cycle_years_low": 4.0, "patriot_cycle_years_high": 6.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_geopolitical_4B_watch",
        rerating_result="unknown",
        round_rerating_label="missile_defense_export_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_order_not_green_until_delivery_margin_replenishment",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Iraq/Saudi 수주와 전투검증 서사는 강하지만 지정학 rally가 실적보다 앞서면 4B-watch다.",
    ),
    Round257CaseCandidate(
        case_id="r1_loop12_hyundai_rotem_k2_poland_delivery_to_revenue",
        symbol="064350",
        company_name="Hyundai Rotem",
        source_sector="R1",
        primary_archetype=E2RArchetype.ARMORED_VEHICLE_DELIVERY_TO_REVENUE,
        secondary_archetypes=(E2RArchetype.ORDER_TO_REVENUE_CONVERSION, E2RArchetype.STAGE2_EVIDENCE_NOT_GREEN),
        case_type="success_candidate",
        stage1_date=date(2022, 1, 1),
        stage2_date=date(2024, 4, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="delivery_to_revenue_evidence_is_better_than_order_headline_but_second_batch_margin_local_production_working_capital_and_cash_collection_required",
        stage4b_status="4B-watch-if-second-K2-contract-priced-before-local-economics",
        hard_4c_confirmed=False,
        evidence_fields=("18_k2_tanks_shipped_to_poland", "k2_export_revenue_270bn_krw", "q1_op_forecast_plus_85pct", "second_180_tank_contract"),
        red_flag_fields=("local_production_margin_unknown", "working_capital_unknown", "cash_collection_unknown"),
        price_data_source="WSJ price/earnings anchor + Reuters second-contract anchor",
        reported_price_anchor="Shares +9.3% to 41,300 KRW",
        reported_return_anchor="Q1 OP +85% forecast; 18 K2 tanks; second 180-tank contract about $6.5B",
        mfe_1d=9.3,
        mae_1d=None,
        stage2_price_anchor=41300.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"event_mfe_pct": 9.3, "kospi_same_context_pct": -0.3, "relative_outperformance_pp": 9.6, "q1_op_forecast_krw_bn": 59.1, "q1_op_growth_forecast_pct": 85.0, "consensus_op_krw_bn": 44.4, "op_forecast_vs_consensus_pct": 33.1, "k2_tanks_shipped_to_poland": 18.0, "k2_export_revenue_q1_krw_bn": 270.0, "second_contract_tanks": 180.0, "second_contract_value_usd_bn": 6.5, "local_production_tanks": 61.0, "first_deliveries_year": 2026.0, "polish_production_period": "2028-2030"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="armored_vehicle_delivery_to_revenue_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_delivery_evidence_not_green_until_margin_cash",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="납품→매출 증거가 있어 품질 높은 Stage 2지만 현지생산 마진·현금회수 전 Green은 보류다.",
    ),
    Round257CaseCandidate(
        case_id="r1_loop12_ls_electric_us_datacenter_transformer",
        symbol="010120",
        company_name="LS Electric",
        source_sector="R1",
        primary_archetype=E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK,
        secondary_archetypes=(E2RArchetype.GRID_POWER_EQUIPMENT_AI_DATACENTER, E2RArchetype.TRANSFORMER_CAPACITY_BOTTLENECK),
        case_type="success_candidate",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 11, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="data_center_transformer_contract_is_stage2_but_delivery_margin_input_cost_pass_through_and_cash_collection_required",
        stage4b_status="4B-watch-if-grid-shortage-theme-priced-before-delivery",
        hard_4c_confirmed=False,
        evidence_fields=("312mn_usd_us_utility_contract", "525kv_transformers", "data_center_end_demand", "delivery_2027_2029", "gsu_demand_plus_274pct"),
        red_flag_fields=("price_data_unavailable_after_deep_search", "copper_goes_cost_unknown", "delivery_margin_cash_collection_unknown"),
        price_data_source="Reuters transformer-shortage / LS Electric contract anchor",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="$312M U.S. utility contract for 525kV transformers; U.S. GSU demand +274%",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"contract_value_usd_mn": 312.0, "voltage_kv": 525.0, "delivery_start_year": 2027.0, "delivery_end_year": 2029.0, "us_gsu_transformer_demand_growth_pct": 274.0, "us_substation_transformer_demand_growth_pct": 116.0, "transformer_price_increase_5y_pct": 80.0, "large_transformer_lead_time_years": 4.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_insufficient_price_data",
        rerating_result="unknown",
        round_rerating_label="grid_transformer_data_center_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_contract_not_green_until_margin_delivery_cash",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="미국 데이터센터 변압기 bottleneck은 강한 Stage 2지만 납품·마진·원가 전가·현금회수 확인이 필요하다.",
    ),
    Round257CaseCandidate(
        case_id="r1_loop12_hyosung_hico_us_grid_equipment_localization",
        symbol="298040",
        company_name="Hyosung Heavy / Hyosung HICO",
        source_sector="R1",
        primary_archetype=E2RArchetype.US_GRID_EQUIPMENT_LOCALIZATION,
        secondary_archetypes=(E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK,),
        case_type="success_candidate",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 12, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="us_localization_capex_is_stage2_but_firm_orders_utilization_margin_and_fcf_required_before_green",
        stage4b_status="4B-watch-if-localization-capex-priced-before-profitability",
        hard_4c_confirmed=False,
        evidence_fields=("hyosung_hico_us_investment_157mn_usd", "gsu_transformer_lead_time_143_weeks", "us_grid_shortage", "data_center_manufacturing_ev_demand"),
        red_flag_fields=("capacity_expansion_without_order", "factory_ramp_risk", "input_cost_unknown", "price_data_unavailable_after_deep_search"),
        price_data_source="Reuters grid-equipment localization anchor",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="$157M Hyosung HICO U.S. investment; GSU lead time around 143 weeks",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"hyosung_hico_us_investment_usd_mn": 157.0, "gsu_transformer_demand_growth_pct": 274.0, "gsu_lead_time_weeks": 143.0, "drivers": "renewable generation|data centers|manufacturing|EVs|aging grid modernization"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_capex_watch",
        rerating_result="unknown",
        round_rerating_label="U.S._grid_equipment_localization_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_capacity_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="미국 현지화 CAPA는 Stage 2다. firm order·가동률·마진·FCF가 없으면 Green이 아니다.",
    ),
    Round257CaseCandidate(
        case_id="r1_loop12_samsung_ea_fadhili_epc_stage2",
        symbol="028050",
        company_name="Samsung E&A",
        source_sector="R1",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_MEGA_ORDER,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM, E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3),
        case_type="event_premium",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 4, 3),
        stage3_date=None,
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        stage3_decision="saudi_fadhili_mega_order_is_stage2_but_progress_revenue_margin_working_capital_and_cash_collection_required_before_green",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("fadhili_contract_about_6bn_usd", "aramco_total_project_7_7bn_usd", "capacity_increase_60pct", "completion_expected_2027_11"),
        red_flag_fields=("epc_mega_order_before_margin_cash_collection", "working_capital_unknown", "progress_revenue_unknown"),
        price_data_source="WSJ contract / event-return anchor",
        reported_price_anchor="Shares +8.5% to 26,750 KRW",
        reported_return_anchor="Estimated $6B Fadhili contract; KOSPI -1.4%",
        mfe_1d=8.5,
        mae_1d=None,
        stage2_price_anchor=26750.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=26750.0,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"event_price_krw": 26750.0, "event_mfe_pct": 8.5, "implied_prior_price_krw": 24654.0, "kospi_same_context_pct": -1.4, "relative_outperformance_pp": 9.9, "contract_value_usd_bn": 6.0, "aramco_total_project_usd_bn": 7.7, "contract_share_pct": 77.9, "capacity_increase_pct": 60.0, "target_price_krw": 35000.0, "target_upside_pct": 30.8},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="EPC_mega_order_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="contract_stage2_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="EPC mega-order와 +8.5% rally는 Stage 2/4B-watch다. 공정률·마진·현금회수 전 Green은 금지다.",
    ),
    Round257CaseCandidate(
        case_id="r1_loop12_hyundai_steel_us_policy_capex_false_positive",
        symbol="004020",
        company_name="Hyundai Steel",
        source_sector="R1",
        primary_archetype=E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.FALSE_POSITIVE_SCORE, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE),
        case_type="failed_rerating",
        stage1_date=date(2025, 3, 1),
        stage2_date=date(2025, 3, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 22),
        stage3_decision="policy_capex_and_tariff_hedge_are_not_green_without_funding_customer_demand_margin_and_fcf",
        stage4b_status="4C-watch-not-hard-4C",
        hard_4c_confirmed=False,
        evidence_fields=("us_louisiana_plant_5_8bn_usd", "annual_capacity_2_7mn_tonnes", "hyundai_group_us_package_21bn_usd", "tariff_hedge_narrative"),
        red_flag_fields=("funding_unclear", "announcement_plus_5_reversed_to_minus_4_4", "post_announcement_drawdown_minus_21_2", "policy_capex_without_funding"),
        price_data_source="Reuters U.S. steel plant / funding-uncertainty anchors",
        reported_price_anchor="Initial >+5% reversed to -4.4%; later -21.2%",
        reported_return_anchor="$5.8B plant, 2.7M tonnes annual capacity, funding unclear",
        mfe_1d=5.0,
        mae_1d=-4.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"plant_investment_usd_bn": 5.8, "annual_capacity_mn_tonnes": 2.7, "group_us_investment_package_usd_bn": 21.0, "announcement_initial_mfe_pct": 5.0, "announcement_session_mae_pct": -4.4, "post_announcement_drawdown_pct": -21.2, "posco_same_period_pct": -18.3, "kospi_same_period_pct": -5.5, "relative_underperformance_vs_kospi_pp": -15.7, "funding_plan": "50% borrowing; remaining funding unclear", "potential_posco_equity": "under discussion"},
        score_price_alignment="false_positive_score",
        round_alignment_label="false_positive_score_prevention",
        rerating_result="no_rerating",
        round_rerating_label="policy_capex_failed_rerating",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="policy_capex_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="정책 CAPEX와 관세 hedge 서사만으로는 Green이 아니다. 자금조달·고객수요·마진·FCF가 빠져 실패 반례다.",
    ),
    Round257CaseCandidate(
        case_id="r1_loop12_hanwha_aerospace_capital_raise_dilution_4b",
        symbol="012450",
        company_name="Hanwha Aerospace",
        source_sector="R1",
        primary_archetype=E2RArchetype.DILUTION_AFTER_RERATING_4B,
        secondary_archetypes=(E2RArchetype.GOVERNANCE_DILUTION_EVENT, E2RArchetype.DEFENSE_EXPORT_BACKLOG_COMPOUNDING),
        case_type="4b_watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 3, 21),
        stage3_date=None,
        stage4b_date=date(2025, 3, 27),
        stage4c_date=None,
        stage3_decision="large_capital_raise_after_defense_rerating_is_4b_watch_until_roi_fcf_per_share_and_capital_discipline_are_clear",
        stage4b_status="4B-watch/dilution",
        hard_4c_confirmed=False,
        evidence_fields=("capital_raise_3_6tn_krw", "overseas_production_expansion", "drones_engines_defense_technologies", "affiliate_issue_and_rights_offering"),
        red_flag_fields=("capital_raise_event_mae_minus_13pct", "fss_revision_order", "dilution_after_rerating", "investor_questioned_necessity"),
        price_data_source="Reuters capital-raise / dilution anchors",
        reported_price_anchor="3.6T KRW raise triggered -13%; affiliate issue price 758,000 KRW/share",
        reported_return_anchor="Revised 2.3T rights offering plus 1.3T affiliate share issue",
        mfe_1d=None,
        mae_1d=-13.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"initial_capital_raise_krw_trn": 3.6, "initial_capital_raise_usd_bn": 2.46, "capital_raise_event_mae_pct": -13.0, "revised_affiliate_share_issue_krw_trn": 1.3, "affiliate_issue_price_krw": 758000.0, "separate_rights_offering_krw_trn": 2.3, "total_revised_related_raise_krw_trn": 3.6, "use_of_proceeds": "drones|engines|overseas defense expansion|production capacity"},
        score_price_alignment="unknown",
        round_alignment_label="4B_watch",
        rerating_result="event_premium",
        round_rerating_label="defense_rerating_dilution_risk",
        stage_failure_type="false_yellow",
        round_stage_failure_label="dilution_after_rerating",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="방산 리레이팅 후 대형 증자는 4B/dilution watch다. ROI와 FCF per share가 확인되기 전 긍정 증거로 쓰면 안 된다.",
    ),
)


def round257_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("delivery", "revenue", "opm", "gross_margin", "margin", "cash", "working_capital", "fcf", "mro", "repeat")
    for candidate in ROUND257_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND257_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round257 R1 Loop-12 industrial orders/infrastructure price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "4b" in field.lower()
                or "rally" in field.lower()
                or "record" in field.lower()
                or "dilution" in field.lower()
                or "capital_raise" in field.lower()
                or "policy" in field.lower()
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "failure" in field.lower()
                or "delay" in field.lower()
                or "blowout" in field.lower()
                or "cancellation" in field.lower()
                or "unclear" in field.lower()
                or "unknown" in field.lower()
            ),
            must_have_fields=ROUND257_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND257_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_order_or_capex_headlines_as_green_alone",
                *ROUND257_GREEN_REQUIRED_FIELDS,
                *ROUND257_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_price=candidate.peak_price_anchor,
                peak_return_from_stage3=candidate.peak_return_from_stage3_pct,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=candidate.stage2_price_anchor is not None
                or candidate.stage4b_price_anchor is not None
                or candidate.stage4c_price_anchor is not None
                or candidate.mfe_1d is not None
                or candidate.mae_1d is not None,
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round257_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND257_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "source_sector": candidate.source_sector,
                "primary_archetype": candidate.primary_archetype.value,
                "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
                "case_type": candidate.case_type,
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
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
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
        )
    return tuple(rows)


def round257_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND257_SCORE_ADJUSTMENTS)


def round257_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND257_SHADOW_WEIGHT_ROWS)


def round257_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND257_DEEP_SUB_ARCHETYPES)


def round257_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round257_price_validation": "true"} for field in ROUND257_PRICE_VALIDATION_FIELDS)


def round257_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round257_label": label, "canonical_archetype": canonical} for label, canonical in ROUND257_REQUIRED_TARGET_ALIASES.items())


def round257_summary() -> dict[str, int | bool | str]:
    cases = ROUND257_CASE_CANDIDATES
    return {
        "source_round": ROUND257_SOURCE_ROUND_PATH,
        "round_id": ROUND257_ROUND_ID,
        "large_sector": ROUND257_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "watch_4b_case_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.stage4b_status),
        "price_data_unavailable_count": sum(1 for case in cases if case.price_validation_status == "price_data_unavailable_after_deep_search"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "target_archetype_count": len(ROUND257_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND257_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND257_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": False,
    }


def round257_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND257_SOURCE_ROUND_PATH,
        "round_id": ROUND257_ROUND_ID,
        "large_sector": ROUND257_LARGE_SECTOR,
        "summary": round257_summary(),
        "target_aliases": dict(ROUND257_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND257_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND257_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND257_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND257_HARD_4C_GATES),
        "deep_sub_archetypes": round257_deep_sub_archetype_rows(),
        "shadow_weights": round257_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round257_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_order_or_capex_headlines_as_green_alone",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round257_summary_markdown() -> str:
    summary = round257_summary()
    lines = [
        "# Round 257 R1 Loop 12 Industrial Orders / Infrastructure Price Validation",
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
        f"- event_premium: {summary['event_premium_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- 4B-watch case_type: {summary['watch_4b_case_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- price_data_unavailable: {summary['price_data_unavailable_count']}",
        f"- false_positive_score: {summary['false_positive_score_count']}",
        f"- target_archetype_count: {summary['target_archetype_count']}",
        f"- deep_sub_archetype_count: {summary['deep_sub_archetype_count']}",
        f"- shadow_weight_row_count: {summary['shadow_weight_row_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND257_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.case_type,
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
            "- R1 Stage 3 is not an order headline. It needs delivery, revenue, margin, cash collection, and repeat order evidence.",
            "- Hanwha Aerospace, LIG Nex1, and Hyundai Rotem are strong Stage 2 examples, but delivery/margin/cash gates remain.",
            "- LS Electric and Hyosung HICO are grid bottleneck Stage 2 cases with insufficient full OHLC in this pass.",
            "- Samsung E&A is EPC Stage 2 plus 4B-watch before progress revenue, margin, and working capital proof.",
            "- Hyundai Steel is the policy-CAPEX false-positive example: funding and FCF uncertainty blocked rerating.",
            "- No hard 4C is forced in this round; 4C-watch remains separate from hard 4C.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round257_green_gate_review_markdown() -> str:
    lines = [
        "# Round 257 R1 Loop 12 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND257_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND257_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `수주 발표`는 Stage 2 후보일 수 있지만, `납품 + 매출 + 마진 + 현금회수`가 닫혀야 Stage 3 근거가 된다.",
            "- `미국 공장 투자`는 좋아 보이지만 자금조달과 가동률이 없으면 Hyundai Steel처럼 false positive가 될 수 있다.",
            "- `대형 증자`는 좋은 수주잔고가 있어도 4B/dilution watch를 켠다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round257_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 257 R1 Loop 12 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND257_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND257_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B means price or event premium has run ahead of delivery, margin, cash, or dilution evidence.",
            "- 4C means the original order or policy thesis is damaged by cancellation, funding failure, margin failure, or execution failure.",
            "- 4C-watch is not hard 4C until actual contract, customer, funding, margin, or cash disruption is confirmed.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND257_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.stage4c_date:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round257_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 257 R1 Loop 12 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND257_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round257_r1_loop12_reports(
    output_directory: str | Path = ROUND257_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND257_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND257_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round257_case_records(), cases_path),
        "audit": _write_json(round257_audit_payload(), audit_path),
        "summary": output / "round257_r1_loop12_price_validation_summary.md",
        "case_matrix": output / "round257_r1_loop12_case_matrix.csv",
        "target_aliases": output / "round257_r1_loop12_target_aliases.csv",
        "score_adjustments": output / "round257_r1_loop12_score_adjustments.csv",
        "shadow_weights": output / "round257_r1_loop12_shadow_weights.csv",
        "deep_sub_archetypes": output / "round257_r1_loop12_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round257_r1_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round257_r1_loop12_green_gate_review.md",
        "price_validation_plan": output / "round257_r1_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round257_r1_loop12_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round257_summary_markdown(), encoding="utf-8")
    _write_csv(round257_case_rows(), paths["case_matrix"])
    _write_csv(round257_target_alias_rows(), paths["target_aliases"])
    _write_csv(round257_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round257_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round257_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round257_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round257_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round257_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round257_stage4b_4c_review_markdown(), encoding="utf-8")
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
