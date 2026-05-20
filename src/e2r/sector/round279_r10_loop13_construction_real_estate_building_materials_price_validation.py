"""Round-279 R10 Loop-13 construction/real-estate/building-materials pack.

This module converts ``docs/round/round_279.md`` into calibration-only case
records and reports. It does not change production scoring, candidate
generation, or StageClassifier thresholds.

Easy example: a 40.6T KRW builder support package is useful relief, but it is
not Stage 3-Green by itself. Green needs project-level refinancing, presales,
margin, working-capital control, and cash collection.
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


ROUND279_SOURCE_ROUND_PATH = "docs/round/round_279.md"
ROUND279_ANALYST_ROUND_ID = "round_207"
ROUND279_LARGE_SECTOR = "CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS"
ROUND279_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round279_r10_loop13_construction_real_estate_building_materials_price_validation"
ROUND279_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop13_round279.jsonl"
ROUND279_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round279_r10_loop13_construction_real_estate_building_materials_price_validation_audit.json"

ROUND279_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "REAL_ESTATE_PF_LIQUIDITY_4C_WATCH": E2RArchetype.REAL_ESTATE_PF_LIQUIDITY_4C_WATCH.value,
    "OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN": E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN.value,
    "NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2": E2RArchetype.NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2.value,
    "CONSTRUCTION_MATERIAL_DEMAND_BREAK": E2RArchetype.CONSTRUCTION_MATERIAL_DEMAND_BREAK.value,
    "SEOUL_PROPERTY_POLICY_EVENT_PREMIUM": E2RArchetype.SEOUL_PROPERTY_POLICY_EVENT_PREMIUM.value,
    "CONSTRUCTION_SAFETY_HARD_REFERENCE": E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE.value,
    "STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK": E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK.value,
    "HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF": E2RArchetype.HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF.value,
}

ROUND279_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "PF_refinancing_success_confirmed",
    "project_profitability_filter_confirmed",
    "pre_sale_ratio_confirmed",
    "unsold_inventory_reduction_confirmed",
    "EPC_margin_visibility_confirmed",
    "working_capital_control_confirmed",
    "unbilled_receivables_control_confirmed",
    "final_contract_signed_confirmed",
    "legal_appeal_clearance_confirmed",
    "construction_safety_trust_confirmed",
    "building_material_demand_spread_confirmed",
    "price_path_after_evidence",
)

ROUND279_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "order_headline_only",
    "preferred_bidder_only",
    "policy_support_only",
    "tariff_relief_only",
    "rate_cut_property_expectation_only",
    "housing_price_rebound_without_cashflow",
    "PF_support_without_profitability",
    "EPC_backlog_without_margin",
    "safety_incident_unresolved",
)

ROUND279_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "overseas_EPC_order_day_plus_5_to_10pct_before_margin",
    "nuclear_preferred_bidder_basket_plus_40pct_before_final_contract",
    "anti_dumping_tariff_short_rally_before_spread",
    "PF_support_headline_builder_rebound",
    "rate_cut_and_property_price_expectation_prepricing",
)

ROUND279_HARD_4C_GATES: tuple[str, ...] = (
    "PF_default_workout_or_debt_rescheduling",
    "project_financing_delinquency_spike",
    "fatal_construction_site_accident",
    "EPC_contract_cancellation",
    "sovereign_legal_appeal_blocking_contract",
    "cost_overrun_or_unbilled_receivables_surge",
    "pre_sale_failure_or_unsold_inventory_spike",
    "rate_cuts_blocked_by_property_household_debt",
    "construction_material_demand_collapse",
)

ROUND279_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "policy_or_project_value_anchor",
    "PF_delinquency_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "safety_trust_anchor",
    "legal_appeal_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round279ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round279ShadowWeightRow:
    archetype: E2RArchetype
    pf_refinancing_success: int
    project_profitability_filter: int
    pre_sale_ratio: int
    unsold_inventory_reduction: int
    epc_margin_visibility: int
    working_capital_control: int
    unbilled_receivables_control: int
    final_contract_signed: int
    legal_appeal_clearance: int
    construction_safety_trust: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "pf_refinancing_success": _signed(self.pf_refinancing_success),
            "project_profitability_filter": _signed(self.project_profitability_filter),
            "pre_sale_ratio": _signed(self.pre_sale_ratio),
            "unsold_inventory_reduction": _signed(self.unsold_inventory_reduction),
            "EPC_margin_visibility": _signed(self.epc_margin_visibility),
            "working_capital_control": _signed(self.working_capital_control),
            "unbilled_receivables_control": _signed(self.unbilled_receivables_control),
            "final_contract_signed": _signed(self.final_contract_signed),
            "legal_appeal_clearance": _signed(self.legal_appeal_clearance),
            "construction_safety_trust": _signed(self.construction_safety_trust),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round279DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round279CaseCandidate:
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
    direct_listed_hard_4c_confirmed: bool
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


ROUND279_SCORE_ADJUSTMENTS: tuple[Round279ScoreAdjustment, ...] = (
    Round279ScoreAdjustment("PF_refinancing_success", 5, "raise", "PF 지원이 아니라 실제 차환 성공을 봐야 한다."),
    Round279ScoreAdjustment("project_profitability_filter", 5, "raise", "지원 대상 프로젝트가 수익성 있는지 확인해야 한다."),
    Round279ScoreAdjustment("pre_sale_ratio", 5, "raise", "분양률이 현금회수의 출발점이다."),
    Round279ScoreAdjustment("unsold_inventory_reduction", 5, "raise", "미분양 감소 없이는 주택 Green이 어렵다."),
    Round279ScoreAdjustment("EPC_margin_visibility", 5, "raise", "해외 EPC 수주는 마진이 닫혀야 한다."),
    Round279ScoreAdjustment("working_capital_control", 5, "raise", "건설은 운전자본과 현금회수가 늦으면 이익이 훼손된다."),
    Round279ScoreAdjustment("unbilled_receivables_control", 5, "raise", "미청구공사 증가는 EPC/건설 4C-watch다."),
    Round279ScoreAdjustment("final_contract_signed", 5, "raise", "preferred bidder는 최종계약이 아니다."),
    Round279ScoreAdjustment("legal_appeal_clearance", 5, "raise", "원전/인프라는 법적 이의제기가 해소되어야 한다."),
    Round279ScoreAdjustment("construction_safety_trust", 5, "raise", "사망 안전사고는 hard gate다."),
    Round279ScoreAdjustment("order_headline_only", -5, "lower", "수주 headline은 Stage 2일 수 있지만 Green은 아니다."),
    Round279ScoreAdjustment("preferred_bidder_only", -5, "lower", "우선협상대상자는 최종계약과 다르다."),
    Round279ScoreAdjustment("policy_support_only", -5, "lower", "정책지원만으로 현금흐름을 만들지 않는다."),
    Round279ScoreAdjustment("tariff_relief_only", -5, "lower", "반덤핑 관세는 relief이지 건자재 실수요 증거가 아니다."),
    Round279ScoreAdjustment("safety_incident_unresolved", -5, "lower", "안전 사고가 풀리지 않으면 수주보다 먼저 차단한다."),
)

ROUND279_SHADOW_WEIGHT_ROWS: tuple[Round279ShadowWeightRow, ...] = (
    Round279ShadowWeightRow(E2RArchetype.REAL_ESTATE_PF_LIQUIDITY_4C_WATCH, 5, 5, 5, 5, 1, 5, 5, 1, 2, 3, 0, 4, 5, "PF support is relief; refinancing, presale, profitability and cash collection are core gates."),
    Round279ShadowWeightRow(E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN, 1, 3, 0, 0, 5, 5, 5, 5, 4, 4, -5, 5, 5, "Fadhili shows order headline is not EPC margin/cashflow Green."),
    Round279ShadowWeightRow(E2RArchetype.NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2, 1, 3, 0, 0, 5, 5, 5, 5, 5, 4, -5, 5, 5, "Czech nuclear needs final contract, legal clearance, funding and EPC margin."),
    Round279ShadowWeightRow(E2RArchetype.CONSTRUCTION_MATERIAL_DEMAND_BREAK, 2, 3, 2, 2, 1, 4, 3, 2, 2, 3, 0, 4, 4, "Hyundai Steel shows weak construction demand can break material margins."),
    Round279ShadowWeightRow(E2RArchetype.SEOUL_PROPERTY_POLICY_EVENT_PREMIUM, 5, 5, 5, 5, 0, 4, 4, 0, 0, 2, -5, 5, 4, "Property/rate-cut headlines need presale, inventory, PF and cashflow proof."),
    Round279ShadowWeightRow(E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 3, 5, "Fatal worksite accidents are hard reference for R10."),
    Round279ShadowWeightRow(E2RArchetype.HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF, 5, 5, 5, 5, 1, 5, 5, 1, 1, 3, -5, 4, 4, "Builder support package is relief until project cashflow proves out."),
    Round279ShadowWeightRow(E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK, 2, 3, 2, 2, 1, 4, 3, 2, 2, 3, -5, 5, 4, "Tariff relief is not Green without construction demand, spread and export-risk control."),
)

ROUND279_DEEP_SUB_ARCHETYPES: tuple[Round279DeepSubArchetype, ...] = (
    Round279DeepSubArchetype("PF / 주택", E2RArchetype.REAL_ESTATE_PF_LIQUIDITY_4C_WATCH, ("Taeyoung E&C", "PF delinquency", "40.6T support", "syndicated loan 1T to 5T", "profitable projects only")),
    Round279DeepSubArchetype("해외 EPC", E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN, ("Samsung E&A", "GS E&C", "Saudi Aramco Fadhili", "$7.7B", "EPC margin", "working capital")),
    Round279DeepSubArchetype("원전 인프라", E2RArchetype.NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2, ("KHNP", "Doosan Enerbility", "KEPCO E&C", "Czech nuclear", "Westinghouse appeal", "preferred bidder not final contract")),
    Round279DeepSubArchetype("건자재 / 철강", E2RArchetype.CONSTRUCTION_MATERIAL_DEMAND_BREAK, ("Hyundai Steel", "rebar price -10%", "net-profit cut -73%", "construction demand", "steel plate competition")),
    Round279DeepSubArchetype("부동산 정책", E2RArchetype.SEOUL_PROPERTY_POLICY_EVENT_PREMIUM, ("Gangnam", "Seocho", "Songpa", "Yongsan", "household debt", "BOK rate cuts")),
    Round279DeepSubArchetype("건설 안전", E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE, ("Anseong highway collapse", "fatal construction-site accident", "five 50m steel structures", "safety trust")),
    Round279DeepSubArchetype("건설사 유동성", E2RArchetype.HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF, ("builder liquidity package", "loan guarantees", "market stabilising fund", "housing supply", "PF restructuring")),
    Round279DeepSubArchetype("철강 반덤핑", E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK, ("Hyundai Steel", "POSCO", "27.91-38.02% tariff", "Chinese steel imports", "US tariff export risk")),
)

ROUND279_CASE_CANDIDATES: tuple[Round279CaseCandidate, ...] = (
    Round279CaseCandidate(
        case_id="r10_loop13_real_estate_pf_taeyoung_liquidity_watch",
        symbol="009410/builders_PF_basket",
        company_name="Taeyoung E&C reference / Korea real-estate PF",
        primary_archetype=E2RArchetype.REAL_ESTATE_PF_LIQUIDITY_4C_WATCH,
        secondary_archetypes=(E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK, E2RArchetype.PF_RESTRUCTURING_RELIEF_KOREA),
        case_type="4b_watch",
        round_case_type="4C-watch + policy_relief",
        stage1_date=date(2023, 12, 1),
        stage2_date=date(2024, 3, 27),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 5, 13),
        stage3_decision="PF_support_is_liquidity_relief_not_cashflow_green",
        stage4b_status="4C-watch/PF-delinquency-and-liquidity-relief",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("government_support_40_6trn_krw", "pf_delinquency_2_70pct", "syndicated_loan_1_to_5trn_krw", "profitable_project_filter"),
        red_flag_fields=("PF_support_without_profitability", "PF_default_workout_or_debt_rescheduling", "project_financing_delinquency_spike"),
        price_data_source="Reuters PF/liquidity support and FSS restructuring anchors",
        reported_price_anchor="40.6T KRW support; PF delinquency rose from 0.37% to 2.70%",
        reported_return_anchor="Policy support is relief, not project cashflow Green",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"government_support_krw_trn": 40.6, "pf_delinquency_end_2021_pct": 0.37, "pf_delinquency_end_2022_pct": 1.19, "pf_delinquency_end_2023_pct": 2.70, "pf_delinquency_increase_2021_to_2023_pct": 629.7, "pf_delinquency_increase_2022_to_2023_pct": 126.9, "syndicated_loan_initial_krw_trn": 1.0, "syndicated_loan_max_krw_trn": 5.0},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch_plus_policy_relief",
        rerating_result="credit_relief_rally",
        round_rerating_label="real_estate_PF_liquidity_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="liquidity_support_not_cashflow_green",
        price_validation_status="sector_policy_anchor_not_full_ohlc",
        notes="PF support is relief; Green waits for refinancing, presales, profitability and cash collection.",
    ),
    Round279CaseCandidate(
        case_id="r10_loop13_samsung_ena_gs_fadhili_epc_order_stage2",
        symbol="028050/006360",
        company_name="Samsung E&A / GS E&C Fadhili EPC",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN,
        secondary_archetypes=(E2RArchetype.OVERSEAS_EPC_MEGA_ORDER, E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG),
        case_type="success_candidate",
        round_case_type="success_candidate + event_premium",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 3),
        stage3_date=None,
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        stage3_decision="overseas_EPC_order_is_stage2_until_margin_working_capital_and_cash_collection_confirm",
        stage4b_status="4B-watch/order-headline-rally-before-EPC-margin",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("project_total_7_7bn_usd", "samsung_estimated_contract_6bn_usd", "capacity_2_5_to_4_0_bscfd", "completion_target_2027_11"),
        red_flag_fields=("order_headline_only", "EPC_backlog_without_margin", "working_capital_control_unconfirmed", "unbilled_receivables_control_unconfirmed"),
        price_data_source="Reuters Aramco Fadhili contract + WSJ Samsung E&A event-return anchor",
        reported_price_anchor="Samsung E&A +8.5% to 26,750 KRW while KOSPI -1.4%",
        reported_return_anchor="Mega-order event premium; EPC margin and cashflow required",
        event_mfe_pct=8.5,
        event_mae_pct=None,
        stage2_price_anchor=26750.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=26750.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"project_total_value_usd_bn": 7.7, "samsung_estimated_contract_value_usd_bn": 6.0, "samsung_contract_share_of_total_pct": 77.9, "fadhili_capacity_before_bscfd": 2.5, "fadhili_capacity_after_bscfd": 4.0, "capacity_increase_pct": 60.0, "additional_sulphur_tpd": 2300, "completion_target": "2027-11", "samsung_event_price_krw": 26750, "samsung_event_mfe_pct": 8.5, "implied_prior_price_krw": 24654, "kospi_same_context_pct": -1.4, "relative_outperformance_pp": 9.9, "target_price_krw": 35000, "target_upside_from_event_price_pct": 30.8},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="overseas_EPC_mega_order_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="order_headline_not_EPC_margin_cash_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Large EPC order is Stage 2; Green needs margin, working capital, receivables and cash collection.",
    ),
    Round279CaseCandidate(
        case_id="r10_loop13_czech_nuclear_infra_preferred_bidder_legal_watch",
        symbol="034020/052690/051600/015760",
        company_name="Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KEPCO Czech nuclear basket",
        primary_archetype=E2RArchetype.NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2,
        secondary_archetypes=(E2RArchetype.NUCLEAR_EPC_EXPORT_STAGE2, E2RArchetype.NUCLEAR_EXPORT_LEGAL_4C_WATCH, E2RArchetype.NUCLEAR_INFRA_EPC_EXPORT),
        case_type="success_candidate",
        round_case_type="success_candidate + legal 4C-watch",
        stage1_date=date(2024, 7, 17),
        stage2_date=date(2024, 7, 17),
        stage3_date=None,
        stage4b_date=date(2024, 7, 17),
        stage4c_date=date(2024, 10, 30),
        stage3_decision="preferred_bidder_is_stage2_until_final_contract_legal_clearance_margin_and_funding_confirm",
        stage4b_status="4B-watch/preferred-bidder-rally-before-final-contract",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("estimated_unit_cost_200czk_bn", "project_context_18bn_usd", "doosan_3m_return_48pct", "westinghouse_edf_appeals"),
        red_flag_fields=("preferred_bidder_only", "legal_appeal_clearance_unconfirmed", "final_contract_signed_unconfirmed"),
        price_data_source="Reuters Czech nuclear preferred-bidder and appeal anchors",
        reported_price_anchor="Doosan +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over three months",
        reported_return_anchor="Preferred bidder drove price first; legal and final contract gates remain",
        event_mfe_pct=48.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"estimated_unit_cost_czk_bn": 200, "estimated_unit_cost_usd_bn": 8.65, "project_context_max_usd_bn": 18, "doosan_enerbility_3m_return_pct": 48, "kepco_plant_service_3m_return_pct": 14, "kepco_ec_3m_return_pct": 41, "final_contract_signed": False, "appeal_parties": ["Westinghouse", "EDF"], "temporary_contract_block": True, "first_reactor_target_context": 2036},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4C_watch",
        rerating_result="unknown",
        round_rerating_label="nuclear_infra_preferred_bidder_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="preferred_bidder_not_final_contract_green",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Czech nuclear is a strong Stage 2 candidate, but preferred bidder is not final contract.",
    ),
    Round279CaseCandidate(
        case_id="r10_loop13_hyundai_steel_construction_material_demand_break",
        symbol="004020",
        company_name="Hyundai Steel",
        primary_archetype=E2RArchetype.CONSTRUCTION_MATERIAL_DEMAND_BREAK,
        secondary_archetypes=(E2RArchetype.BUILDING_MATERIALS_DEMAND_BREAK, E2RArchetype.BUILDING_MATERIALS_DEMAND_CYCLE, E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK),
        case_type="success_candidate",
        round_case_type="evidence_good_but_price_failed + tariff relief watch",
        stage1_date=date(2024, 6, 21),
        stage2_date=date(2025, 2, 20),
        stage3_date=None,
        stage4b_date=date(2025, 2, 20),
        stage4c_date=date(2024, 6, 21),
        stage3_decision="tariff_relief_is_not_green_without_demand_spread_inventory_and_FCF",
        stage4b_status="4C-watch/demand-break-then-4B-watch/tariff-relief",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("rebar_price_decline_10pct", "net_profit_estimate_cut_73pct", "anti_dumping_tariff_27_91_to_38_02pct"),
        red_flag_fields=("construction_material_demand_collapse", "tariff_relief_only", "spread_recovery_unconfirmed"),
        price_data_source="MarketWatch Hyundai Steel demand-risk anchor + Reuters steel anti-dumping anchor",
        reported_price_anchor="Weak demand -1.2% to 29,000 KRW; later anti-dumping relief +5.8%",
        reported_return_anchor="Demand evidence was negative; tariff relief did not prove spread/FCF",
        event_mfe_pct=5.8,
        event_mae_pct=-1.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=29000.0,
        extra_price_metrics={"weak_demand_event_date": "2024-06-21", "hyundai_steel_price_krw": 29000, "weak_demand_event_mae_pct": -1.2, "expected_rebar_price_decline_2024_pct": -10, "net_profit_estimate_after_cut_krw_bn": 215, "net_profit_estimate_cut_pct": -73, "implied_prior_net_profit_estimate_krw_bn": 796.3, "target_price_krw": 30000, "target_price_cut_pct": -14, "target_upside_from_event_price_pct": 3.4, "anti_dumping_tariff_pct": "27.91-38.02", "anti_dumping_event_mfe_pct": 5.8, "kospi_anti_dumping_context_pct": -0.7},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed_then_relief",
        rerating_result="unknown",
        round_rerating_label="construction_material_demand_break_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="policy_tariff_relief_not_spread_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Hyundai Steel shows demand break first; later tariff relief is not Green without demand and spread.",
    ),
    Round279CaseCandidate(
        case_id="r10_loop13_seoul_property_policy_ratecut_macro_gate",
        symbol="residential_developers_REITs_construction_finance_basket",
        company_name="Seoul property policy / rate-cut macroprudential basket",
        primary_archetype=E2RArchetype.SEOUL_PROPERTY_POLICY_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF, E2RArchetype.HOUSING_POLICY_SUPPLY_EVENT, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium + macroprudential 4C-watch",
        stage1_date=date(2024, 7, 18),
        stage2_date=date(2025, 3, 19),
        stage3_date=None,
        stage4b_date=date(2025, 3, 19),
        stage4c_date=date(2025, 11, 27),
        stage3_decision="property_policy_and_rate_cut_expectation_are_not_developer_cashflow_green",
        stage4b_status="4B-watch/property-rate-cut-expectation-before-presale-cashflow",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("seoul_house_price_mom_0_38pct", "land_transaction_permit_areas", "household_debt_1927_3trn_krw", "bok_rate_2_50pct"),
        red_flag_fields=("rate_cut_property_expectation_only", "housing_price_rebound_without_cashflow", "rate_cuts_blocked_by_property_household_debt"),
        price_data_source="Reuters property policy / BOK macroprudential anchors",
        reported_price_anchor="Policy macro anchor; no full adjusted OHLC",
        reported_return_anchor="Property/rate-cut expectations remain macro event premium",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"seoul_house_price_mom_june_2024_pct": 0.38, "korea_house_price_mom_june_2024_pct": 0.04, "land_transaction_permit_areas": ["Gangnam", "Seocho", "Songpa", "Yongsan"], "permit_rule_end_date": "2025-09-30", "median_seoul_apartment_price_krw_bn": 1.0, "median_seoul_price_5y_change": "doubled", "household_debt_2024_krw_trn": 1927.3, "household_debt_2024_growth_pct": 2.2, "bok_rate_nov_2025_pct": 2.50},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_macroprudential_watch",
        rerating_result="event_premium",
        round_rerating_label="property_policy_rate_cut_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="property_policy_not_developer_cashflow_green",
        price_validation_status="policy_macro_anchor_not_full_ohlc",
        notes="Seoul property policy is event premium; developer Green needs presales, PF refinancing, margin and FCF.",
    ),
    Round279CaseCandidate(
        case_id="r10_loop13_anseong_highway_construction_safety_reference",
        symbol="civil_engineering_construction_safety_basket",
        company_name="Anseong highway construction collapse reference",
        primary_archetype=E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE,
        secondary_archetypes=(E2RArchetype.CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C, E2RArchetype.WORKPLACE_FATALITY_REGULATORY_4C),
        case_type="4c_thesis_break",
        round_case_type="hard 4C reference",
        stage1_date=date(2025, 2, 25),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 2, 25),
        stage3_decision="fatal_construction_site_accident_is_hard_reference_not_positive_stage_source",
        stage4b_status="hard-4C/fatal-construction-safety-trust-break",
        hard_4c_confirmed=True,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("fatalities_3", "injured_6", "critically_injured_5", "five_50m_steel_structures_collapsed"),
        red_flag_fields=("fatal_construction_site_accident", "safety_incident_unresolved", "construction_safety_trust_break"),
        price_data_source="Reuters construction-site collapse safety anchor",
        reported_price_anchor="No direct listed price anchor; sector safety hard reference",
        reported_return_anchor="Fatal worksite event confirms construction safety hard gate",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_date": "2025-02-25", "fatalities": 3, "injured": 6, "critically_injured": 5, "collapsed_steel_structures": 5, "structure_length_meters": 50, "hard_4c_reference": True, "direct_listed_hard_4c_confirmed": False},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="construction_safety_hard_reference",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="fatal_worksite_safety_gate",
        price_validation_status="sector_safety_reference",
        notes="Fatal construction-site event is a hard reference even when listed-company price data is unavailable.",
    ),
    Round279CaseCandidate(
        case_id="r10_loop13_builder_liquidity_package_policy_relief",
        symbol="000720/006360/047040/375500/009410_basket",
        company_name="Korean builders liquidity support package",
        primary_archetype=E2RArchetype.HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF,
        secondary_archetypes=(E2RArchetype.PF_RESTRUCTURING_RELIEF, E2RArchetype.HOUSING_SUPPLY_POLICY_EVENT, E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_relief",
        stage1_date=date(2024, 3, 27),
        stage2_date=date(2024, 3, 27),
        stage3_date=None,
        stage4b_date=date(2024, 3, 27),
        stage4c_date=None,
        stage3_decision="builder_liquidity_package_is_policy_relief_until_profitable_project_cashflow_confirms",
        stage4b_status="4B-watch/policy-relief-before-project-cashflow",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("support_package_40_6trn_krw", "loan_guarantees", "market_stabilising_fund", "profitable_real_estate_projects"),
        red_flag_fields=("policy_support_only", "PF_support_without_profitability", "pre_sale_ratio_unconfirmed"),
        price_data_source="Reuters builders support / housing supply policy anchors",
        reported_price_anchor="40.6T KRW support package; policy relief anchor",
        reported_return_anchor="Support is Stage 2 relief until project cashflow proves out",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"support_package_krw_trn": 40.6, "support_tools": ["loan guarantees", "lower interest rates", "expanded guarantees", "additional loans", "market stabilising fund"], "target_projects": "profitable real-estate projects", "housing_supply_policy": True, "pf_restructuring_policy": True, "household_debt_control_policy": True},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_policy_relief",
        rerating_result="credit_relief_rally",
        round_rerating_label="builder_liquidity_relief_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="policy_support_not_project_cashflow_green",
        price_validation_status="policy_relief_anchor_not_full_ohlc",
        notes="Builder support package is Stage 2 relief, not Green before profitable-project cashflow.",
    ),
    Round279CaseCandidate(
        case_id="r10_loop13_steel_plate_anti_dumping_construction_relief",
        symbol="004020/005490/building_steel_basket",
        company_name="Hyundai Steel / POSCO Holdings / construction steel plate basket",
        primary_archetype=E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK,
        secondary_archetypes=(E2RArchetype.CONSTRUCTION_MATERIAL_DEMAND_BREAK, E2RArchetype.BUILDING_MATERIALS_PRICE_COST),
        case_type="event_premium",
        round_case_type="event_premium_policy_relief",
        stage1_date=date(2025, 2, 20),
        stage2_date=date(2025, 2, 20),
        stage3_date=None,
        stage4b_date=date(2025, 2, 20),
        stage4c_date=date(2025, 2, 20),
        stage3_decision="anti_dumping_relief_is_not_green_without_construction_demand_spread_and_FCF",
        stage4b_status="4B-watch/tariff-relief-and-4C-watch/export-tariff-risk",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("anti_dumping_tariff_27_91_to_38_02pct", "chinese_steel_imports_10_4bn_usd", "china_share_49pct", "hyundai_plus_5_8pct"),
        red_flag_fields=("tariff_relief_only", "u_s_tariff_export_risk", "construction_material_demand_collapse"),
        price_data_source="Reuters steel plate anti-dumping anchor",
        reported_price_anchor="Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%",
        reported_return_anchor="Tariff relief can move price, but not prove demand/spread/FCF",
        event_mfe_pct=5.8,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"anti_dumping_tariff_pct": "27.91-38.02", "chinese_steel_imports_2024_usd_bn": 10.4, "chinese_share_of_total_steel_imports_pct": 49, "hyundai_steel_event_mfe_pct": 5.8, "posco_event_mfe_pct": 3.9, "kospi_same_context_pct": -0.7, "hyundai_relative_outperformance_pp": 6.5, "posco_relative_outperformance_pp": 4.6, "u_s_tariff_export_risk": True},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_policy_relief",
        rerating_result="event_premium",
        round_rerating_label="construction_steel_material_relief_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="anti_dumping_relief_not_demand_spread_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Anti-dumping relief is event premium; Green needs actual construction demand, spread and FCF.",
    ),
)


def round279_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND279_CASE_CANDIDATES:
        stage3_terms = ("pf", "pre_sale", "unsold", "profitability", "margin", "working_capital", "receivables", "contract", "appeal", "safety", "spread", "cash")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND279_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round279 R10 Loop-13 construction/real-estate/building-materials price validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in (*candidate.evidence_fields, *ROUND279_GREEN_REQUIRED_FIELDS) if any(token in field.lower() for token in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("rally", "premium", "policy", "preferred", "tariff", "order", "support"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("pf", "fatal", "safety", "appeal", "demand", "debt", "tariff", "collapse", "unbilled"))),
            must_have_fields=ROUND279_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "4b_watch", "4c_thesis_break"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND279_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "direct_listed_hard_4c_confirmed_false",
                "hard_4c_confirmed_true_for_sector_safety_reference",
                "do_not_use_round279_cases_as_candidate_generation_input",
                "do_not_treat_policy_support_order_preferred_bidder_property_price_or_tariff_relief_as_green_alone",
                *ROUND279_GREEN_REQUIRED_FIELDS,
                *ROUND279_GREEN_FORBIDDEN_PATTERNS,
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


def round279_case_rows() -> tuple[dict[str, str], ...]:
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
            "direct_listed_hard_4c_confirmed": str(candidate.direct_listed_hard_4c_confirmed).lower(),
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
        for candidate in ROUND279_CASE_CANDIDATES
    )


def round279_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND279_SCORE_ADJUSTMENTS)


def round279_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND279_SHADOW_WEIGHT_ROWS)


def round279_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND279_DEEP_SUB_ARCHETYPES)


def round279_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round279_price_validation": "true"} for field in ROUND279_PRICE_VALIDATION_FIELDS)


def round279_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round279_label": label, "canonical_archetype": canonical} for label, canonical in ROUND279_REQUIRED_TARGET_ALIASES.items())


def round279_summary() -> dict[str, int | bool | str]:
    cases = ROUND279_CASE_CANDIDATES
    return {
        "source_round": ROUND279_SOURCE_ROUND_PATH,
        "round_id": ROUND279_ANALYST_ROUND_ID,
        "large_sector": ROUND279_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "policy_relief_count": sum(1 for case in cases if "policy" in case.round_case_type.lower() or "relief" in case.round_case_type.lower()),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "direct_listed_hard_4c_case_count": sum(1 for case in cases if case.direct_listed_hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "target_archetype_count": len(ROUND279_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND279_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND279_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
        "direct_listed_hard_4c_confirmed": any(case.direct_listed_hard_4c_confirmed for case in cases),
    }


def round279_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND279_SOURCE_ROUND_PATH,
        "round_id": ROUND279_ANALYST_ROUND_ID,
        "large_sector": ROUND279_LARGE_SECTOR,
        "summary": round279_summary(),
        "target_aliases": dict(ROUND279_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND279_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND279_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND279_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND279_HARD_4C_GATES),
        "score_adjustments": list(round279_score_adjustment_rows()),
        "shadow_weights": list(round279_shadow_weight_rows()),
        "deep_sub_archetypes": list(round279_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND279_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round279_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_policy_support_order_preferred_bidder_property_price_or_tariff_relief_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round279_summary_markdown() -> str:
    summary = round279_summary()
    lines = [
        "# Round 279 R10 Loop 13 Construction Real Estate Building Materials Price Validation",
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
        f"- policy_relief: {summary['policy_relief_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- direct_listed_hard_4c: {summary['direct_listed_hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND279_CASE_CANDIDATES:
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
            "- PF support and builder liquidity are relief, not Green, until project cashflow proves out.",
            "- Overseas EPC mega-orders are Stage 2 until EPC margin, working capital and receivables are visible.",
            "- Czech nuclear preferred-bidder status is Stage 2; final contract and legal clearance remain gates.",
            "- Anti-dumping and property/rate-cut headlines can move price, but do not prove spread, presales or FCF.",
            "- Fatal construction-site safety events are hard references for R10 RedTeam gates.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round279_green_gate_review_markdown() -> str:
    lines = [
        "# Round 279 R10 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R10 Stage 3-Green is not `PF support`, `order headline`, `preferred bidder`, `property price rebound`, `rate-cut expectation`, or `tariff relief`. It requires refinancing, presales, EPC margin, working capital, final contract, spread, safety trust and FCF.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND279_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND279_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND279_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Samsung E&A +8.5% on Fadhili order` is not Green until EPC margin and cash collection are visible.",
            "- `Czech nuclear preferred bidder` is not final contract; legal appeals can keep it in 4C-watch.",
            "- `40.6T KRW builder support` is relief, like oxygen. It is not proof the project can run and repay debt.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round279_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 279 R10 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND279_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND279_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | direct listed hard 4C | interpretation |", "|---|---|---|---|---|---|"])
    for case in ROUND279_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {str(case.direct_listed_hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round279_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 279 R10 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, PF cashflow, EPC margin, legal clearance, presales, spread, safety remediation or FCF where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND279_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND279_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round279_r10_loop13_reports(
    output_directory: str | Path = ROUND279_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND279_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND279_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round279_case_records(), cases_path),
        "audit": _write_json(round279_audit_payload(), audit_path),
        "summary": output / "round279_r10_loop13_price_validation_summary.md",
        "case_matrix": output / "round279_r10_loop13_case_matrix.csv",
        "target_aliases": output / "round279_r10_loop13_target_aliases.csv",
        "score_adjustments": output / "round279_r10_loop13_score_adjustments.csv",
        "shadow_weights": output / "round279_r10_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round279_r10_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round279_r10_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round279_r10_loop13_green_gate_review.md",
        "price_validation_plan": output / "round279_r10_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round279_r10_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round279_summary_markdown(), encoding="utf-8")
    _write_csv(round279_case_rows(), paths["case_matrix"])
    _write_csv(round279_target_alias_rows(), paths["target_aliases"])
    _write_csv(round279_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round279_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round279_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round279_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round279_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round279_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round279_stage4b_4c_review_markdown(), encoding="utf-8")
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
