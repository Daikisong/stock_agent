"""Round-292 R10 Loop-14 construction/real-estate/building-materials pack.

This module converts ``docs/round/round_292.md`` into calibration-only case
records and reports. It does not change production scoring, candidate
generation, or StageClassifier thresholds.

Easy example: a $6B EPC order can move a stock on announcement day. It is not
Stage 3-Green until advance payment, cost lock-in, working capital, claim risk,
and completion margin are visible.
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


ROUND292_SOURCE_ROUND_PATH = "docs/round/round_292.md"
ROUND292_ANALYST_ROUND_ID = "round_220"
ROUND292_LARGE_SECTOR = "CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS"
ROUND292_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round292_r10_loop14_construction_real_estate_building_materials_price_validation"
ROUND292_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop14_round292.jsonl"
ROUND292_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round292_r10_loop14_construction_real_estate_building_materials_price_validation_audit.json"

ROUND292_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "PF_LIQUIDITY_HARD_4C_WATCH": E2RArchetype.PF_LIQUIDITY_HARD_4C_WATCH.value,
    "REAL_ESTATE_POLICY_STAGE2_NOT_GREEN": E2RArchetype.REAL_ESTATE_POLICY_STAGE2_NOT_GREEN.value,
    "CONSTRUCTION_SAFETY_HARD_4C": E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C.value,
    "OVERSEAS_EPC_ORDER_4B_WATCH": E2RArchetype.OVERSEAS_EPC_ORDER_4B_WATCH.value,
    "NUCLEAR_CONSTRUCTION_EXPORT_STAGE2": E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2.value,
    "BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING": E2RArchetype.BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING.value,
    "BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM": E2RArchetype.BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM.value,
    "US_LOCALIZATION_CAPEX_FALSE_POSITIVE": E2RArchetype.US_LOCALIZATION_CAPEX_FALSE_POSITIVE.value,
}

ROUND292_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "PF_repayment_visibility_confirmed",
    "presale_absorption_confirmed",
    "construction_cost_margin_confirmed",
    "unbilled_receivables_control_confirmed",
    "safety_quality_trust_confirmed",
    "completion_margin_visibility_confirmed",
    "working_capital_advance_payment_confirmed",
    "final_contract_signing_confirmed",
    "building_material_ASP_volume_confirmed",
    "capex_IRR_funding_clarity_confirmed",
    "price_path_after_evidence",
)

ROUND292_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "order_value_headline_only",
    "policy_support_headline_only",
    "property_supply_policy_only",
    "preferred_bidder_without_final_contract",
    "tariff_relief_without_ASP_margin",
    "capex_localization_without_IRR",
    "housing_price_rally_without_presales",
    "backlog_without_PF_cashflow",
    "safety_risk_unresolved",
)

ROUND292_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "overseas_EPC_mega_order_plus_5_to_10pct",
    "nuclear_preferred_bidder_plus_30_to_50pct",
    "anti_dumping_tariff_relief_rally",
    "government_property_supply_policy_rally",
    "rate_cut_expectation_property_rerating",
    "localization_capex_headline_before_IRR",
)

ROUND292_HARD_4C_GATES: tuple[str, ...] = (
    "PF_workout_or_debt_rescheduling",
    "PF_liquidity_support_dependence",
    "fatal_construction_safety_event",
    "major_defect_reconstruction_or_compensation",
    "pre_sale_failure_or_unsold_inventory_spike",
    "cost_overrun_or_unbilled_receivables_surge",
    "final_contract_blocked_by_legal_challenge",
    "capex_funding_gap_or_dilution",
)

ROUND292_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "reported_event_price_anchor",
    "PF_delinquency_anchor",
    "support_package_anchor",
    "policy_LTV_anchor",
    "safety_event_fact_anchor",
    "order_value_anchor",
    "legal_challenge_anchor",
    "building_material_spread_anchor",
    "capex_funding_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round292ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round292ShadowWeightRow:
    archetype: E2RArchetype
    pf_repayment_visibility: int
    presale_absorption: int
    construction_cost_margin: int
    unbilled_receivables_control: int
    safety_quality_trust: int
    completion_margin_visibility: int
    working_capital_advance_payment: int
    final_contract_signing: int
    building_material_asp_volume: int
    capex_irr_funding_clarity: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "PF_repayment_visibility": _signed(self.pf_repayment_visibility),
            "presale_absorption": _signed(self.presale_absorption),
            "construction_cost_margin": _signed(self.construction_cost_margin),
            "unbilled_receivables_control": _signed(self.unbilled_receivables_control),
            "safety_quality_trust": _signed(self.safety_quality_trust),
            "completion_margin_visibility": _signed(self.completion_margin_visibility),
            "working_capital_advance_payment": _signed(self.working_capital_advance_payment),
            "final_contract_signing": _signed(self.final_contract_signing),
            "building_material_ASP_volume": _signed(self.building_material_asp_volume),
            "capex_IRR_funding_clarity": _signed(self.capex_irr_funding_clarity),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round292DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round292CaseCandidate:
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


ROUND292_SCORE_ADJUSTMENTS: tuple[Round292ScoreAdjustment, ...] = (
    Round292ScoreAdjustment("PF_repayment_visibility", 5, "raise", "수주잔고보다 PF 상환과 refinancing visibility가 먼저다."),
    Round292ScoreAdjustment("presale_absorption", 5, "raise", "분양률과 미분양 감소가 현금회수의 출발점이다."),
    Round292ScoreAdjustment("construction_cost_margin", 5, "raise", "건설은 원가율이 닫혀야 이익이 현금으로 남는다."),
    Round292ScoreAdjustment("unbilled_receivables_control", 5, "raise", "미청구공사 증가는 EPC/건설 4C-watch다."),
    Round292ScoreAdjustment("safety_quality_trust", 5, "raise", "건설 안전과 품질 신뢰는 hard gate다."),
    Round292ScoreAdjustment("completion_margin_visibility", 5, "raise", "해외 EPC 수주는 completion margin이 닫혀야 한다."),
    Round292ScoreAdjustment("working_capital_advance_payment", 5, "raise", "advance payment와 working capital 통제가 EPC 본체다."),
    Round292ScoreAdjustment("final_contract_signing", 4, "raise", "preferred bidder는 최종계약이 아니다."),
    Round292ScoreAdjustment("building_material_ASP_volume", 5, "raise", "건자재는 ASP, 물량, 원가, 재고가 같이 필요하다."),
    Round292ScoreAdjustment("capex_IRR_funding_clarity", 5, "raise", "localization capex는 IRR과 funding clarity가 필요하다."),
    Round292ScoreAdjustment("order_value_headline_only", -5, "lower", "수주금액 headline은 Stage 2일 수 있지만 Green은 아니다."),
    Round292ScoreAdjustment("policy_support_headline_only", -5, "lower", "정책지원 headline만으로 PF cashflow를 만들지 않는다."),
    Round292ScoreAdjustment("preferred_bidder_without_final_contract", -5, "lower", "우선협상대상자는 확정 매출과 다르다."),
    Round292ScoreAdjustment("tariff_relief_without_ASP_margin", -5, "lower", "반덤핑 관세는 ASP와 margin으로 내려와야 한다."),
    Round292ScoreAdjustment("capex_localization_without_IRR", -5, "lower", "미국 공장 투자는 IRR과 자금조달 전에는 false positive가 될 수 있다."),
    Round292ScoreAdjustment("safety_risk_unresolved", -5, "lower", "안전 리스크 미해소는 Green을 막는다."),
)


ROUND292_SHADOW_WEIGHT_ROWS: tuple[Round292ShadowWeightRow, ...] = (
    Round292ShadowWeightRow(E2RArchetype.PF_LIQUIDITY_HARD_4C_WATCH, 5, 5, 5, 5, 3, 2, 5, 1, 1, 4, 0, 5, 5, "Taeyoung/PF shows backlog is not Green if PF repayment/refinancing fails."),
    Round292ShadowWeightRow(E2RArchetype.REAL_ESTATE_POLICY_STAGE2_NOT_GREEN, 4, 5, 5, 4, 2, 2, 3, 1, 2, 2, -5, 5, 4, "Seoul property policy needs permits, starts, presales and PF cashflow."),
    Round292ShadowWeightRow(E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C, 3, 3, 4, 4, 5, 4, 3, 1, 1, 3, 0, 4, 5, "HDC/Gwangju confirms fatal quality/safety events override backlog."),
    Round292ShadowWeightRow(E2RArchetype.OVERSEAS_EPC_ORDER_4B_WATCH, 2, 0, 5, 5, 3, 5, 5, 5, 1, 3, -5, 5, 4, "Samsung E&A Fadhili order needs advance payment, working capital and completion margin."),
    Round292ShadowWeightRow(E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2, 2, 0, 5, 5, 3, 5, 5, 5, 1, 4, -5, 5, 4, "Czech nuclear preferred bidder needs final contract and legal clearance."),
    Round292ShadowWeightRow(E2RArchetype.BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING, 1, 3, 4, 2, 1, 1, 1, 0, 5, 2, 0, 4, 4, "Hyundai Steel weak rebar demand shows ASP/volume must lead materials scoring."),
    Round292ShadowWeightRow(E2RArchetype.BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM, 1, 2, 4, 2, 1, 1, 1, 0, 5, 2, -5, 5, 3, "Anti-dumping tariff relief needs ASP, volume and spread confirmation."),
    Round292ShadowWeightRow(E2RArchetype.US_LOCALIZATION_CAPEX_FALSE_POSITIVE, 1, 1, 4, 3, 1, 2, 3, 2, 4, 5, 0, 5, 4, "Hyundai Steel U.S. plant shows capex headline needs funding clarity and IRR."),
)


ROUND292_DEEP_SUB_ARCHETYPES: tuple[Round292DeepSubArchetype, ...] = (
    Round292DeepSubArchetype("PF / 부동산 금융", E2RArchetype.PF_LIQUIDITY_HARD_4C_WATCH, ("Taeyoung E&C", "PF delinquency", "40.6T support", "1T to 5T syndicated loan", "profitable project sorting")),
    Round292DeepSubArchetype("부동산 정책", E2RArchetype.REAL_ESTATE_POLICY_STAGE2_NOT_GREEN, ("Seoul LTV", "Gangnam", "Seocho", "Songpa", "Yongsan", "state land supply")),
    Round292DeepSubArchetype("건설 안전", E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C, ("HDC Hyundai Development", "Gwangju Hwajeong I-Park", "fatal collapse", "substandard materials", "brand safety trust")),
    Round292DeepSubArchetype("해외 EPC", E2RArchetype.OVERSEAS_EPC_ORDER_4B_WATCH, ("Samsung E&A", "Saudi Aramco Fadhili", "$6B order", "completion margin", "working capital")),
    Round292DeepSubArchetype("원전 건설수출", E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2, ("KHNP", "Czech nuclear", "Doosan Enerbility", "KEPCO E&C", "EDF legal challenge")),
    Round292DeepSubArchetype("건자재 약수요", E2RArchetype.BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING, ("Hyundai Steel", "rebar price decline", "net-profit estimate cut", "weak construction demand")),
    Round292DeepSubArchetype("건자재 관세 relief", E2RArchetype.BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM, ("Hyundai Steel", "POSCO", "Chinese steel plate", "27.91-38.02% tariff", "ASP margin")),
    Round292DeepSubArchetype("미국 현지화 CAPEX", E2RArchetype.US_LOCALIZATION_CAPEX_FALSE_POSITIVE, ("Hyundai Steel", "$6B U.S. plant", "funding clarity", "IRR", "tariff saving")),
)


ROUND292_CASE_CANDIDATES: tuple[Round292CaseCandidate, ...] = (
    Round292CaseCandidate(
        case_id="r10_loop14_taeyoung_pf_liquidity_hard_watch",
        symbol="009410",
        company_name="Taeyoung Engineering & Construction / PF liquidity reference",
        primary_archetype=E2RArchetype.PF_LIQUIDITY_HARD_4C_WATCH,
        secondary_archetypes=(E2RArchetype.REAL_ESTATE_PF_LIQUIDITY_4C_WATCH, E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK),
        case_type="4c_thesis_break",
        round_case_type="PF hard 4C-watch",
        stage1_date=date(2023, 12, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 5, 13),
        stage3_decision="backlog_is_not_green_if_PF_repayment_refinancing_cashflow_fails",
        stage4b_status="hard-4C-watch/PF-liquidity",
        hard_4c_confirmed=True,
        evidence_fields=("government_support_package_40_6trn_krw", "pf_delinquency_2_70pct", "syndicated_loan_1_to_5trn_krw"),
        red_flag_fields=("PF_workout_or_debt_rescheduling", "PF_liquidity_support_dependence", "backlog_without_PF_cashflow"),
        price_data_source="Reuters PF liquidity and restructuring anchors",
        reported_event_return_anchor="Direct adjusted OHLC unavailable; PF delinquency and support-package anchors used",
        reported_event_price_anchor="40.6T KRW support package, PF delinquency 2.70%, syndicated loan 1T to 5T KRW",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"government_support_package_krw_trn": 40.6, "government_support_package_usd_bn": 30.3, "pf_delinquency_end_2021_pct": 0.37, "pf_delinquency_end_2022_pct": 1.19, "pf_delinquency_end_2023_pct": 2.70, "syndicated_loan_initial_krw_trn": 1, "syndicated_loan_max_krw_trn": 5},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="PF_LIQUIDITY_HARD_4C_WATCH",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="backlog_not_green_if_PF_cashflow_fails",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="PF liquidity is a hard watch because backlog cannot protect equity if refinancing and cash collection fail.",
    ),
    Round292CaseCandidate(
        case_id="r10_loop14_seoul_property_policy_stage2_not_green",
        symbol="construction_developers_REITs_basket",
        company_name="Seoul property policy / construction-developer basket",
        primary_archetype=E2RArchetype.REAL_ESTATE_POLICY_STAGE2_NOT_GREEN,
        secondary_archetypes=(E2RArchetype.SEOUL_PROPERTY_POLICY_EVENT_PREMIUM, E2RArchetype.HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF),
        case_type="event_premium",
        round_case_type="policy_stage2 + 4B-watch",
        stage1_date=date(2025, 3, 19),
        stage2_date=date(2025, 9, 7),
        stage3_date=None,
        stage4b_date=date(2025, 10, 23),
        stage4c_date=None,
        stage3_decision="policy_supply_headline_needs_permits_starts_presales_PF_refinancing_cost_margin_and_cash_collection",
        stage4b_status="4B-watch/policy-before-cashflow",
        hard_4c_confirmed=False,
        evidence_fields=("permit_zone_districts", "ltv_cut_50_to_40pct", "state_land_supply_channel", "bok_rate_2_50pct"),
        red_flag_fields=("property_supply_policy_only", "housing_price_rally_without_presales", "policy_support_headline_only"),
        price_data_source="Reuters Seoul property-curb and BOK housing-risk anchors",
        reported_event_return_anchor="Direct construction-stock anchor unavailable; policy and macro anchors used",
        reported_event_price_anchor="LTV 50% to 40%, permit zones, state-land supply plan, BOK policy rate 2.50%",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"permit_zone_districts": ["Gangnam", "Seocho", "Songpa", "Yongsan"], "permit_requirement_until": "2025-09-30", "ltv_before_pct": 50, "ltv_after_pct": 40, "state_land_supply_channel": "Korea Land & Housing Corporation and other state-run companies", "bok_policy_rate_context_pct": 2.50, "kospi_context_2025_ytd_pct": 62, "stage3_conditions": ["building permits", "starts", "pre-sale absorption", "PF refinancing", "cost margin", "cash collection"]},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="policy_stage2_not_green",
        rerating_result="policy_event_rerating",
        round_rerating_label="REAL_ESTATE_POLICY_STAGE2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="policy_supply_headline_not_presale_cashflow_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Property policy is Stage 2 until permits, starts, presales, PF refinancing, margin and cash collection confirm.",
    ),
    Round292CaseCandidate(
        case_id="r10_loop14_hdc_gwangju_construction_safety_hard_4c",
        symbol="294870",
        company_name="HDC Hyundai Development",
        primary_archetype=E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C,
        secondary_archetypes=(E2RArchetype.CONSTRUCTION_SAFETY_HARD_REFERENCE, E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY),
        case_type="4c_thesis_break",
        round_case_type="hard 4C / construction safety trust break",
        stage1_date=date(2022, 1, 11),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2022, 3, 14),
        stage3_decision="fatal_quality_safety_event_overrides_housing_backlog_and_brand_premium",
        stage4b_status="hard-4C/fatal-construction-safety-event",
        hard_4c_confirmed=True,
        evidence_fields=("fatalities_6", "faulty_construction_methods", "substandard_materials", "chairman_resignation"),
        red_flag_fields=("fatal_construction_safety_event", "major_defect_reconstruction_or_compensation", "safety_risk_unresolved"),
        price_data_source="Gwangju Hwajeong I-Park collapse public reference; adjusted OHLC unavailable",
        reported_event_return_anchor="Direct adjusted OHLC unavailable; safety and quality facts used",
        reported_event_price_anchor="6 fatalities, substandard materials, unauthorized slab-change context",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fatalities": 6, "investigation_findings": ["faulty construction methods", "substandard materials"], "unauthorized_slab_change_context": "39th floor slab reportedly 35cm vs planned 15cm", "chairman_resignation": True, "prior_2021_gwangju_collapse_association": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="CONSTRUCTION_SAFETY_HARD_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="fatal_quality_safety_event_overrides_housing_backlog",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Fatal construction-quality event overrides housing backlog and brand premium.",
    ),
    Round292CaseCandidate(
        case_id="r10_loop14_samsung_ena_fadhili_epc_order_4b",
        symbol="028050",
        company_name="Samsung E&A",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_ORDER_4B_WATCH,
        secondary_archetypes=(E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN, E2RArchetype.OVERSEAS_EPC_MEGA_ORDER),
        case_type="success_candidate",
        round_case_type="success_candidate + event_premium",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 3),
        stage3_date=None,
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        stage3_decision="mega_order_is_stage2_until_advance_payment_cost_lock_working_capital_claim_risk_and_completion_margin_confirm",
        stage4b_status="4B-watch/order-day-premium-before-completion-margin",
        hard_4c_confirmed=False,
        evidence_fields=("contract_value_6bn_usd", "project_total_7_7bn_usd", "event_mfe_8_5pct", "completion_target_2027_11"),
        red_flag_fields=("order_value_headline_only", "EPC_backlog_without_margin", "cost_overrun_or_unbilled_receivables_surge"),
        price_data_source="WSJ Samsung E&A Fadhili order event anchor",
        reported_event_return_anchor="Samsung E&A +8.5% while KOSPI -1.4%",
        reported_event_price_anchor="Event price 26,750 KRW; KB target price 35,000 KRW",
        event_mfe_pct=8.5,
        event_mae_pct=None,
        stage2_price_anchor=26750.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=26750.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"contract_value_usd_bn": 6.0, "project_total_value_usd_bn": 7.7, "samsung_contract_share_of_project_pct": 77.9, "event_price_krw": 26750, "event_mfe_pct": 8.5, "kospi_same_context_pct": -1.4, "relative_outperformance_pp": 9.9, "target_price_krw": 35000, "target_upside_from_event_price_pct": 30.8, "gas_capacity_increase_pct": 60, "sulfur_production_increase_tpd": 2300, "completion_target": "2027-11"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="OVERSEAS_EPC_ORDER_STAGE2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="order_value_not_completion_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Mega-order is Stage 2; advance payment, cost lock-in, working capital and completion margin are required.",
    ),
    Round292CaseCandidate(
        case_id="r10_loop14_czech_nuclear_construction_export_stage2",
        symbol="034020/052690/051600/KEPCO_KHNP_readthrough",
        company_name="Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KHNP",
        primary_archetype=E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2,
        secondary_archetypes=(E2RArchetype.NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2, E2RArchetype.NUCLEAR_EPC_EXPORT_STAGE2),
        case_type="success_candidate",
        round_case_type="success_candidate + legal 4C-watch",
        stage1_date=date(2024, 7, 17),
        stage2_date=date(2024, 7, 17),
        stage3_date=None,
        stage4b_date=date(2024, 7, 17),
        stage4c_date=date(2025, 5, 6),
        stage3_decision="preferred_bidder_is_stage2_until_final_contract_legal_clearance_package_allocation_margin_and_funding_confirm",
        stage4b_status="4B-watch/nuclear-export-premium-before-final-contract",
        hard_4c_confirmed=False,
        evidence_fields=("khnp_preferred_bidder", "doosan_3m_gain_48pct", "kepco_ec_3m_gain_41pct", "court_blocked_contract_18bn_usd_min"),
        red_flag_fields=("preferred_bidder_without_final_contract", "final_contract_blocked_by_legal_challenge", "legal_challenge_party_EDF"),
        price_data_source="Reuters Czech nuclear preferred-bidder and legal-challenge anchors",
        reported_event_return_anchor="Doosan Enerbility +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over three months",
        reported_event_price_anchor="Two reactors, 200B CZK per unit, $8.65B per unit estimate; court later blocked at least $18B signing",
        event_mfe_pct=48.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"reactors": 2, "estimated_cost_per_unit_czk_bn": 200, "estimated_cost_per_unit_usd_bn": 8.65, "khnp_status": "preferred_bidder", "first_major_overseas_nuclear_order_since": 2009, "doosan_enerbility_3m_gain_pct": 48, "kepco_plant_se_3m_gain_pct": 14, "kepco_ec_3m_gain_pct": 41, "court_blocked_contract_value_usd_bn_min": 18, "legal_challenge_party": "EDF", "final_contract_signed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="NUCLEAR_CONSTRUCTION_EXPORT_STAGE2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="preferred_bidder_not_final_contract_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Preferred bidder is not booked margin until final contract and legal challenge clear.",
    ),
    Round292CaseCandidate(
        case_id="r10_loop14_hyundai_steel_rebar_weak_construction_demand",
        symbol="004020",
        company_name="Hyundai Steel",
        primary_archetype=E2RArchetype.BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING,
        secondary_archetypes=(E2RArchetype.CONSTRUCTION_MATERIAL_DEMAND_BREAK, E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK),
        case_type="failed_rerating",
        round_case_type="failed_rerating / weak construction demand",
        stage1_date=date(2024, 6, 21),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 6, 21),
        stage3_decision="building_material_green_needs_ASP_volume_cost_inventory_and_starts_not_weak_rebar_demand",
        stage4b_status="4C-watch/rebar-demand-profit-cut",
        hard_4c_confirmed=False,
        evidence_fields=("event_price_29000_krw", "event_mae_minus_1_2pct", "rebar_price_decline_expected_minus_10pct", "net_profit_estimate_cut_minus_73pct"),
        red_flag_fields=("construction_material_demand_collapse", "rebar_price_decline", "net_profit_estimate_cut"),
        price_data_source="MarketWatch/Dow Jones Hyundai Steel weak-demand anchor",
        reported_event_return_anchor="Hyundai Steel -1.2% to 29,000 KRW",
        reported_event_price_anchor="Net-profit estimate cut 73% to 215B KRW, target price 30,000 KRW",
        event_mfe_pct=None,
        event_mae_pct=-1.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=29000.0,
        extra_price_metrics={"event_price_krw": 29000, "event_mae_pct": -1.2, "rebar_price_decline_expected_pct": -10, "net_profit_estimate_after_cut_krw_bn": 215, "net_profit_estimate_cut_pct": -73, "implied_prior_net_profit_estimate_krw_bn": 796.3, "target_price_krw": 30000, "target_price_cut_pct": -14},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="failed_rerating",
        rerating_result="no_rerating",
        round_rerating_label="BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING",
        stage_failure_type="false_yellow",
        round_stage_failure_label="construction_demand_rebar_price_down",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Weak construction demand and rebar-price decline damaged earnings estimates.",
    ),
    Round292CaseCandidate(
        case_id="r10_loop14_hyundai_posco_steel_plate_antidumping_event",
        symbol="004020/005490",
        company_name="Hyundai Steel / POSCO Holdings",
        primary_archetype=E2RArchetype.BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK, E2RArchetype.CONSTRUCTION_MATERIAL_DEMAND_BREAK),
        case_type="event_premium",
        round_case_type="event_premium / policy relief",
        stage1_date=date(2025, 2, 20),
        stage2_date=date(2025, 2, 20),
        stage3_date=None,
        stage4b_date=date(2025, 2, 20),
        stage4c_date=None,
        stage3_decision="tariff_relief_is_stage2_until_ASP_volume_utilization_raw_material_cost_inventory_and_margin_confirm",
        stage4b_status="4B-watch/tariff-relief-rally-before-spread",
        hard_4c_confirmed=False,
        evidence_fields=("anti_dumping_tariff_27_91_to_38_02pct", "hyundai_steel_plus_5_8pct", "posco_plus_3_9pct", "chinese_share_49pct"),
        red_flag_fields=("tariff_relief_without_ASP_margin", "construction_demand_weakness", "spread_reversal"),
        price_data_source="Reuters steel-plate anti-dumping event anchor",
        reported_event_return_anchor="Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%",
        reported_event_price_anchor="Tariff range 27.91-38.02%, 2024 Chinese steel imports $10.4B, share 49%",
        event_mfe_pct=5.8,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"anti_dumping_tariff_pct": "27.91-38.02", "chinese_steel_imports_2024_usd_bn": 10.4, "chinese_share_of_korean_steel_imports_pct": 49, "hyundai_steel_event_mfe_pct": 5.8, "posco_event_mfe_pct": 3.9, "kospi_same_context_pct": -0.7, "hyundai_relative_outperformance_pp": 6.5, "posco_relative_outperformance_pp": 4.6, "steel_product_use": ["shipbuilding", "construction"]},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_policy_relief",
        rerating_result="event_premium",
        round_rerating_label="BUILDING_MATERIAL_TARIFF_RELIEF_STAGE2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="tariff_relief_not_ASP_volume_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Tariff relief is not Green until ASP, volume, utilization and spread improve.",
    ),
    Round292CaseCandidate(
        case_id="r10_loop14_hyundai_steel_us_plant_capex_false_positive",
        symbol="004020",
        company_name="Hyundai Steel",
        primary_archetype=E2RArchetype.US_LOCALIZATION_CAPEX_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY, E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK),
        case_type="failed_rerating",
        round_case_type="false_positive_score / localization capex",
        stage1_date=date(2025, 3, 24),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 22),
        stage3_decision="localization_capex_needs_funding_clarity_IRR_tariff_saving_demand_offtake_utilization_and_FCF",
        stage4b_status="4C-watch/capex-backlash-before-IRR",
        hard_4c_confirmed=False,
        evidence_fields=("us_plant_6bn_usd", "hyundai_group_package_21bn_usd", "stock_decline_more_than_21pct", "funding_unclear"),
        red_flag_fields=("capex_localization_without_IRR", "capex_funding_gap_or_dilution", "weak_domestic_demand", "tariff_policy_uncertainty"),
        price_data_source="Reuters Hyundai Steel U.S. plant investor backlash anchor",
        reported_event_return_anchor="Hyundai Steel shares drop more than 21% after U.S. plant announcement",
        reported_event_price_anchor="$6B U.S. plant, $21B Hyundai group package, half potentially funded by borrowing",
        event_mfe_pct=None,
        event_mae_pct=-21.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"us_plant_investment_usd_bn": 6, "hyundai_group_us_package_usd_bn": 21, "stock_decline_after_announcement_pct": -21, "funding_plan_context": "half via borrowing; possible POSCO equity input", "risk_factors": ["unclear funding details", "tariff-policy uncertainty", "weak domestic demand", "cheap Chinese imports", "labour disputes"]},
        score_price_alignment="false_positive_score",
        round_alignment_label="false_positive_score",
        rerating_result="no_rerating",
        round_rerating_label="US_LOCALIZATION_CAPEX_FALSE_POSITIVE",
        stage_failure_type="false_yellow",
        round_stage_failure_label="localization_capex_without_IRR_funding_clarity",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Localization capex is not Green without funding clarity, IRR and tariff-saving proof.",
    ),
)


def round292_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND292_CASE_CANDIDATES:
        stage3_terms = ("margin", "cash", "contract", "PF", "presale", "safety", "ASP", "IRR", "funding", "completion")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND292_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round292 R10 Loop-14 construction/real-estate/building-materials price validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in (*candidate.evidence_fields, *ROUND292_GREEN_REQUIRED_FIELDS) if any(token.lower() in field.lower() for token in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("rally", "premium", "order", "policy", "preferred", "tariff", "capex"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("pf", "fatal", "safety", "weak", "decline", "block", "funding", "dilution", "defect"))),
            must_have_fields=ROUND292_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4b_watch", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND292_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "hard_4c_confirmed_true_for_construction_safety_and_PF_liquidity_reference",
                "do_not_use_round292_cases_as_candidate_generation_input",
                "do_not_treat_order_policy_preferred_bidder_tariff_or_capex_headlines_as_green_alone",
                *ROUND292_GREEN_REQUIRED_FIELDS,
                *ROUND292_GREEN_FORBIDDEN_PATTERNS,
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


def round292_case_rows() -> tuple[dict[str, str], ...]:
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
        for candidate in ROUND292_CASE_CANDIDATES
    )


def round292_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND292_SCORE_ADJUSTMENTS)


def round292_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND292_SHADOW_WEIGHT_ROWS)


def round292_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND292_DEEP_SUB_ARCHETYPES)


def round292_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round292_price_validation": "true"} for field in ROUND292_PRICE_VALIDATION_FIELDS)


def round292_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round292_label": label, "canonical_archetype": canonical} for label, canonical in ROUND292_REQUIRED_TARGET_ALIASES.items())


def round292_summary() -> dict[str, int | bool | str]:
    cases = ROUND292_CASE_CANDIDATES
    return {
        "source_round": ROUND292_SOURCE_ROUND_PATH,
        "round_id": ROUND292_ANALYST_ROUND_ID,
        "large_sector": ROUND292_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "target_archetype_count": len(ROUND292_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND292_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND292_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round292_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND292_SOURCE_ROUND_PATH,
        "round_id": ROUND292_ANALYST_ROUND_ID,
        "large_sector": ROUND292_LARGE_SECTOR,
        "summary": round292_summary(),
        "target_aliases": dict(ROUND292_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND292_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND292_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND292_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND292_HARD_4C_GATES),
        "score_adjustments": list(round292_score_adjustment_rows()),
        "shadow_weights": list(round292_shadow_weight_rows()),
        "deep_sub_archetypes": list(round292_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND292_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round292_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_order_policy_preferred_bidder_tariff_or_capex_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round292_summary_markdown() -> str:
    summary = round292_summary()
    lines = [
        "# Round 292 R10 Loop 14 Construction Real Estate Building Materials Price Validation",
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
    for case in ROUND292_CASE_CANDIDATES:
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
            "- PF liquidity and construction safety are hard gates before backlog or policy support.",
            "- Property policy, nuclear preferred-bidder status, tariff relief and localization capex are Stage 2/event signals until cashflow closes.",
            "- Overseas EPC order value is useful, but Green requires margin, advance payment, working capital and claim-risk evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round292_green_gate_review_markdown() -> str:
    lines = [
        "# Round 292 R10 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R10 Stage 3-Green is not `order`, `policy`, `preferred bidder`, `tariff relief`, or `localization capex`. It requires PF repayment, presales, cost margin, safety trust, EPC completion margin, ASP/volume, capex IRR, and price path after evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND292_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND292_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND292_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `$6B EPC order` is Stage 2 until margin and working capital close.",
            "- `LTV/supply policy` is not builder Green until permits, starts, presales and PF cashflow appear.",
            "- `fatal apartment collapse` is hard 4C because safety trust breaks before valuation.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round292_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 292 R10 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND292_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND292_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND292_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round292_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 292 R10 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, PF repayment, presales, construction margins, safety remediation, final contracts, ASP/volume, capex IRR or FCF where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND292_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND292_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_event_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round292_r10_loop14_reports(
    output_directory: str | Path = ROUND292_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND292_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND292_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round292_case_records(), cases_path),
        "audit": _write_json(round292_audit_payload(), audit_path),
        "summary": output / "round292_r10_loop14_price_validation_summary.md",
        "case_matrix": output / "round292_r10_loop14_case_matrix.csv",
        "target_aliases": output / "round292_r10_loop14_target_aliases.csv",
        "score_adjustments": output / "round292_r10_loop14_score_adjustments.csv",
        "shadow_weights": output / "round292_r10_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round292_r10_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round292_r10_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round292_r10_loop14_green_gate_review.md",
        "price_validation_plan": output / "round292_r10_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round292_r10_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round292_summary_markdown(), encoding="utf-8")
    _write_csv(round292_case_rows(), paths["case_matrix"])
    _write_csv(round292_target_alias_rows(), paths["target_aliases"])
    _write_csv(round292_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round292_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round292_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round292_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round292_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round292_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round292_stage4b_4c_review_markdown(), encoding="utf-8")
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
