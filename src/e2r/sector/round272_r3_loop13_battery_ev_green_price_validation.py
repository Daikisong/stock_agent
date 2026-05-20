"""Round-272 R3 Loop-13 battery/EV/green price-validation pack.

Round 272 converts ``docs/round/round_272.md`` into structured,
calibration-only case records. It does not change production scoring.

Easy example: a Tesla battery-material contract headline is not Stage 3 by
itself. R3 Green needs actual call-off, GWh/material volume, delivery,
utilization, ex-subsidy OP, margin/FCF, safety and policy gates to clear.
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


ROUND272_SOURCE_ROUND_PATH = "docs/round/round_272.md"
ROUND272_ANALYST_ROUND_ID = "round_200"
ROUND272_LARGE_SECTOR = "BATTERY_EV_GREEN"
ROUND272_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round272_r3_loop13_battery_ev_green_price_validation"
ROUND272_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop13_round272.jsonl"
ROUND272_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round272_r3_loop13_battery_ev_green_price_validation_audit.json"

ROUND272_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE": E2RArchetype.EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE.value,
    "ESS_LFP_CONTRACT_STAGE2_NOT_GREEN": E2RArchetype.ESS_LFP_CONTRACT_STAGE2_NOT_GREEN.value,
    "IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE": E2RArchetype.IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE.value,
    "BATTERY_PARENT_CAPITAL_RECYCLING": E2RArchetype.BATTERY_PARENT_CAPITAL_RECYCLING.value,
    "ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM": E2RArchetype.ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM.value,
    "PRECURSOR_IPO_OVERHEAT_DEMAND_BREAK": E2RArchetype.PRECURSOR_IPO_OVERHEAT_DEMAND_BREAK.value,
    "BATTERY_SAFETY_HARD_REFERENCE": E2RArchetype.BATTERY_SAFETY_HARD_REFERENCE.value,
    "FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN": E2RArchetype.FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN.value,
}

ROUND272_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "signed_contract_and_actual_calloff",
    "gwh_or_material_volume_disclosed",
    "delivery_start_or_revenue_recognition_confirmed",
    "utilization_improvement_confirmed",
    "ex_subsidy_op_quality_confirmed",
    "margin_and_fcf_improvement_confirmed",
    "counterparty_ev_or_ess_program_health_confirmed",
    "battery_safety_quality_risk_clear",
    "non_china_sourcing_or_feoc_compliance_if_relevant",
    "price_path_after_evidence",
)

ROUND272_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "tesla_customer_name_only",
    "gm_or_ford_customer_name_only",
    "contract_value_without_calloff",
    "reported_deal_without_company_confirmation",
    "ira_subsidy_driven_op_only",
    "policy_support_only",
    "ipo_vertical_integration_story_only",
    "battery_safety_incident_unresolved",
    "feoc_policy_relief_without_contracts",
    "capital_recycling_without_roic",
)

ROUND272_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "tesla_ess_lfp_headline_short_term_rally",
    "ira_or_feoc_policy_basket_rally_before_contracts",
    "battery_recycler_or_precursor_ipo_premium",
    "subsidy_benefit_op_growth_then_valuation_expansion",
    "capital_recycling_parent_value_up_rerating",
    "reported_contract_before_company_confirmation",
)

ROUND272_HARD_4C_GATES: tuple[str, ...] = (
    "contract_value_collapse",
    "customer_program_cancellation",
    "actual_calloff_failure",
    "order_cancellation",
    "subsidy_removal_exposes_near_zero_op",
    "battery_fire_or_fatal_safety_incident",
    "quality_failure_or_recall",
    "feoc_non_compliance",
    "non_china_sourcing_failure",
    "counterparty_production_yield_failure",
)

ROUND272_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "contract_value_usd_bn",
    "contract_value_collapse_pct",
    "gwh_volume_disclosed",
    "ex_ira_op_quality",
    "policy_support_anchor",
    "safety_event_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round272ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round272ShadowWeightRow:
    archetype: E2RArchetype
    actual_calloff: int
    gwh_volume_disclosed: int
    delivery_start: int
    utilization_visibility: int
    ex_subsidy_op_quality: int
    margin_fcf_visibility: int
    counterparty_program_health: int
    battery_safety_quality: int
    non_china_sourcing_certification: int
    capital_allocation_roic: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "actual_calloff": _signed(self.actual_calloff),
            "gwh_volume_disclosed": _signed(self.gwh_volume_disclosed),
            "delivery_start": _signed(self.delivery_start),
            "utilization_visibility": _signed(self.utilization_visibility),
            "ex_subsidy_op_quality": _signed(self.ex_subsidy_op_quality),
            "margin_fcf_visibility": _signed(self.margin_fcf_visibility),
            "counterparty_program_health": _signed(self.counterparty_program_health),
            "battery_safety_quality": _signed(self.battery_safety_quality),
            "non_china_sourcing_certification": _signed(self.non_china_sourcing_certification),
            "capital_allocation_roic": _signed(self.capital_allocation_roic),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round272DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round272CaseCandidate:
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


ROUND272_SCORE_ADJUSTMENTS: tuple[Round272ScoreAdjustment, ...] = (
    Round272ScoreAdjustment("actual_calloff", 5, "raise", "계약금액보다 실제 call-off가 더 중요하다."),
    Round272ScoreAdjustment("GWh_volume_disclosed", 5, "raise", "ESS/배터리는 GWh 또는 소재 물량이 있어야 Stage 3에 가까워진다."),
    Round272ScoreAdjustment("delivery_start", 5, "raise", "납품 시작이나 매출 인식이 확인되어야 한다."),
    Round272ScoreAdjustment("utilization_visibility", 5, "raise", "라인 가동률이 확인되어야 EPS/FCF 경로가 닫힌다."),
    Round272ScoreAdjustment("ex_subsidy_OP_quality", 5, "raise", "IRA 같은 보조금을 뺀 OP 품질을 본다."),
    Round272ScoreAdjustment("margin_and_FCF_visibility", 5, "raise", "매출보다 마진과 FCF가 Green 핵심이다."),
    Round272ScoreAdjustment("counterparty_program_health", 5, "raise", "Tesla 4680처럼 고객 프로그램 리스크를 따로 본다."),
    Round272ScoreAdjustment("battery_safety_quality", 5, "raise", "배터리는 안전·품질 문제가 hard gate다."),
    Round272ScoreAdjustment("non_China_sourcing_certification", 4, "raise", "FEOC/graphite는 실제 탈중국 공급과 인증이 필요하다."),
    Round272ScoreAdjustment("capital_allocation_ROIC", 4, "raise", "지분매각은 ROIC와 부채감축이 확인될 때만 긍정이다."),
    Round272ScoreAdjustment("customer_name_headline_only", -5, "lower", "Tesla/GM/Ford 이름만으로는 Green 금지다."),
    Round272ScoreAdjustment("contract_value_without_calloff", -5, "lower", "계약금액만 있고 call-off가 없으면 4C가 될 수 있다."),
    Round272ScoreAdjustment("reported_deal_without_confirmation", -5, "lower", "회사 확인 없는 보도는 event premium이다."),
    Round272ScoreAdjustment("subsidy_adjusted_profit_dependency", -5, "lower", "보조금 의존 OP는 품질 게이트에서 감점한다."),
    Round272ScoreAdjustment("IPO_vertical_integration_story_only", -4, "lower", "IPO/수직계열화 story는 수요·마진 증거가 아니다."),
    Round272ScoreAdjustment("policy_support_without_contracts", -5, "lower", "정책 지원만으로 회사 Green을 만들지 않는다."),
    Round272ScoreAdjustment("capital_recycling_without_ROIC", -4, "lower", "지분매각만 있고 ROIC가 없으면 Stage 2에 머문다."),
    Round272ScoreAdjustment("battery_safety_incident", -5, "lower", "안전 사고가 열려 있으면 Green을 막는다."),
    Round272ScoreAdjustment("counterparty_4680_or_EV_program_risk", -5, "lower", "고객 EV/4680 프로그램이 흔들리면 계약 품질이 깨진다."),
)


ROUND272_SHADOW_WEIGHT_ROWS: tuple[Round272ShadowWeightRow, ...] = (
    Round272ShadowWeightRow(E2RArchetype.EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE, 5, 5, 5, 5, 3, 5, 5, 4, 3, 2, 0, 4, 5, "L&F/Tesla proves customer-name contract can hard-break without call-off."),
    Round272ShadowWeightRow(E2RArchetype.ESS_LFP_CONTRACT_STAGE2_NOT_GREEN, 5, 5, 5, 5, 4, 5, 4, 4, 4, 2, -3, 5, 4, "LGES/Tesla ESS is Stage 2 until GWh/margin/utilization prove out."),
    Round272ShadowWeightRow(E2RArchetype.IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE, 3, 3, 4, 5, 5, 5, 4, 3, 3, 3, -4, 4, 5, "LGES Q2 shows reported OP must be adjusted for IRA tax credit."),
    Round272ShadowWeightRow(E2RArchetype.BATTERY_PARENT_CAPITAL_RECYCLING, 2, 0, 0, 1, 3, 4, 2, 2, 3, 5, -4, 4, 4, "LG Chem stake sale needs ROIC/debt reduction/shareholder return proof."),
    Round272ShadowWeightRow(E2RArchetype.ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM, 4, 5, 5, 4, 3, 4, 4, 3, 3, 1, -5, 5, 3, "Samsung SDI reported ESS deal is not Green without company confirmation."),
    Round272ShadowWeightRow(E2RArchetype.PRECURSOR_IPO_OVERHEAT_DEMAND_BREAK, 4, 4, 4, 5, 3, 5, 4, 3, 4, 2, -5, 5, 5, "EcoPro Materials needs utilization/margin, not IPO/vertical-integration story."),
    Round272ShadowWeightRow(E2RArchetype.BATTERY_SAFETY_HARD_REFERENCE, 0, 0, 0, 0, 0, 0, 0, 5, 2, 0, 0, 3, 5, "Aricell/S-Connect shows battery safety/quality hard gate."),
    Round272ShadowWeightRow(E2RArchetype.FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN, 2, 2, 2, 3, 3, 4, 4, 3, 5, 3, -5, 4, 4, "FEOC/graphite policy is relief until actual supply contracts and certification."),
)


ROUND272_DEEP_SUB_ARCHETYPES: tuple[Round272DeepSubArchetype, ...] = (
    Round272DeepSubArchetype("EV battery-material contract collapse", E2RArchetype.EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE, ("L&F", "Tesla 4680", "high-nickel cathode", "$2.9B to $7,386", "hard 4C")),
    Round272DeepSubArchetype("ESS LFP contract Stage 2", E2RArchetype.ESS_LFP_CONTRACT_STAGE2_NOT_GREEN, ("LG Energy Solution", "Tesla reported by WSJ", "$4.3B", "2027-2030", "GWh missing")),
    Round272DeepSubArchetype("IRA subsidy quality", E2RArchetype.IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE, ("LGES Q2 2025", "OP 492B won", "ex-IRA OP 1.4B won", "stock -2.3%")),
    Round272DeepSubArchetype("parent capital recycling", E2RArchetype.BATTERY_PARENT_CAPITAL_RECYCLING, ("LG Chem", "LGES stake sale", "2T won", "price return swap", "ROIC needed")),
    Round272DeepSubArchetype("unconfirmed ESS report", E2RArchetype.ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM, ("Samsung SDI", "Tesla ESS report", ">3T won", "nothing decided")),
    Round272DeepSubArchetype("precursor IPO overheat", E2RArchetype.PRECURSOR_IPO_OVERHEAT_DEMAND_BREAK, ("EcoPro Materials", "precursor", "IPO", "-11%", "119,200 won")),
    Round272DeepSubArchetype("battery safety hard reference", E2RArchetype.BATTERY_SAFETY_HARD_REFERENCE, ("Aricell", "S-Connect", "23 deaths", "quality failures", "15-year sentence")),
    Round272DeepSubArchetype("FEOC graphite policy relief", E2RArchetype.FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN, ("China graphite", "FEOC", "9.7T won support", "policy not Green")),
)


ROUND272_CASE_CANDIDATES: tuple[Round272CaseCandidate, ...] = (
    Round272CaseCandidate(
        case_id="r3_loop13_lnf_tesla_4680_contract_collapse",
        symbol="066970",
        company_name="L&F",
        primary_archetype=E2RArchetype.EV_BATTERY_MATERIAL_CONTRACT_COLLAPSE,
        secondary_archetypes=(E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="4c_thesis_break",
        round_case_type="hard_4C_contract_collapse",
        stage1_date=date(2023, 2, 1),
        stage2_date=date(2023, 2, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 29),
        stage3_decision="initial_tesla_contract_headline_failed_actual_calloff; no_stage3",
        stage4b_status="none",
        hard_4c_confirmed=True,
        evidence_fields=("tesla_4680_high_nickel_cathode_supply_deal", "initial_contract_projection_2_9bn_usd", "supply_period_2024_01_to_2025_12"),
        red_flag_fields=("contract_value_collapse_to_7386_usd", "actual_calloff_failure", "tesla_4680_production_yield_issue", "ev_demand_slowdown", "cybertruck_demand_weakness"),
        price_data_source="Reuters contract-collapse anchor",
        reported_price_anchor="$2.9B projected contract value reduced to $7,386",
        reported_return_anchor="contract value collapse -99.9997%; full OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"initial_contract_projection_usd_bn": 2.9, "revised_contract_value_usd": 7386.0, "contract_value_collapse_pct": -99.9997, "supply_period": "2024-01_to_2025-12", "application": "Tesla 4680 high-nickel cathode materials"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="EV_battery_material_contract_quality_failure",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C",
        price_validation_status="reported_contract_anchor_not_full_ohlc",
        notes="Tesla 이름과 계약금액만으로 Green을 주면 안 된다. 실제 call-off가 실패하면 계약은 hard 4C가 된다.",
    ),
    Round272CaseCandidate(
        case_id="r3_loop13_lges_tesla_lfp_ess_stage2",
        symbol="373220",
        company_name="LG Energy Solution",
        primary_archetype=E2RArchetype.ESS_LFP_CONTRACT_STAGE2_NOT_GREEN,
        secondary_archetypes=(E2RArchetype.ESS_LFP_GRID_STORAGE, E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT),
        case_type="success_candidate",
        round_case_type="success_candidate_stage2_not_green",
        stage1_date=date(2025, 7, 25),
        stage2_date=date(2025, 7, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="good_ess_lfp_contract_but_green_requires_gwh_shipment_utilization_margin_ex_subsidy_op_and_fcf",
        stage4b_status="4B-watch-if-contract-headline-rerates-before-GWh-margin",
        hard_4c_confirmed=False,
        evidence_fields=("4_3bn_usd_lfp_battery_supply_contract", "tesla_reported_by_wsj", "contract_period_2027_08_to_2030_07", "extension_option_up_to_7_years"),
        red_flag_fields=("actual_gwh_volume_not_disclosed", "margin_not_disclosed", "customer_not_named_by_lges", "ev_demand_slowdown_context"),
        price_data_source="Reuters / WSJ contract and event-return anchors",
        reported_price_anchor="$4.3B ESS LFP contract; customer reported as Tesla by WSJ",
        reported_return_anchor="LGES shares +0.6% after announcement",
        event_mfe_pct=0.6,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"contract_value_usd_bn": 4.3, "extension_option_years": 7.0, "event_mfe_pct": 0.6, "actual_gwh_volume": "not_disclosed", "margin": "not_disclosed"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="ESS_LFP_contract_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="contract_without_volume_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="좋은 Stage 2 계약이지만 GWh, 납품, 가동률, 마진, 보조금 제외 OP 전에는 Green이 아니다.",
    ),
    Round272CaseCandidate(
        case_id="r3_loop13_lges_ira_subsidy_op_quality_gate",
        symbol="373220",
        company_name="LG Energy Solution",
        primary_archetype=E2RArchetype.IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE,
        secondary_archetypes=(E2RArchetype.BATTERY_TAX_CREDIT_QUALITY_OVERLAY, E2RArchetype.US_BATTERY_LOCALIZATION),
        case_type="failed_rerating",
        round_case_type="evidence_good_but_quality_gate_failed",
        stage1_date=date(2025, 7, 25),
        stage2_date=date(2025, 7, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 7, 25),
        stage3_decision="headline_op_beat_is_not_green_when_ex_ira_tax_credit_op_quality_is_weak",
        stage4b_status="4B-watch/subsidy-quality",
        hard_4c_confirmed=False,
        evidence_fields=("q2_2025_op_492bn_krw", "q2_2024_op_195bn_krw", "reported_op_growth_152_3pct"),
        red_flag_fields=("ex_ira_tax_credit_op_only_1_4bn_krw", "ex_ira_share_of_reported_op_0_28pct", "shares_minus_2_3pct", "us_tariff_and_ev_subsidy_end_risk"),
        price_data_source="Reuters earnings and subsidy-quality anchor",
        reported_price_anchor="Reported OP 492B won, but ex-IRA OP only 1.4B won",
        reported_return_anchor="shares -2.3% despite OP +152.3% YoY",
        event_mfe_pct=None,
        event_mae_pct=-2.3,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"q2_2025_op_krw_bn": 492.0, "q2_2024_op_krw_bn": 195.0, "op_growth_pct": 152.3, "ex_ira_tax_credit_op_krw_bn": 1.4, "ex_ira_share_of_reported_op_pct": 0.28, "event_mae_pct": -2.3},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        round_rerating_label="subsidy_adjusted_OP_quality_gate",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="headline_profit_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="겉보기 OP보다 보조금 제외 OP를 봐야 한다. 예: 492B OP 중 ex-IRA OP가 1.4B면 Green 품질이 아니다.",
    ),
    Round272CaseCandidate(
        case_id="r3_loop13_lgchem_lges_stake_sale_capital_recycling",
        symbol="051910",
        company_name="LG Chem",
        primary_archetype=E2RArchetype.BATTERY_PARENT_CAPITAL_RECYCLING,
        secondary_archetypes=(E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE, E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate_capital_recycling_watch",
        stage1_date=date(2025, 10, 1),
        stage2_date=date(2025, 10, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stake_sale_is_stage2_not_green_until_debt_reduction_roic_shareholder_return_and_battery_material_margin_confirm",
        stage4b_status="4B-watch/capital-recycling-parent-value-up",
        hard_4c_confirmed=False,
        evidence_fields=("2tn_krw_lges_stake_sale", "1_43bn_usd_value", "price_return_swap", "stake_falls_2_5pp_to_79_4pct"),
        red_flag_fields=("capital_recycling_without_roic", "forced_sale_perception_watch", "battery_material_capex_roi_unconfirmed", "shareholder_return_unconfirmed"),
        price_data_source="Reuters stake-sale anchor",
        reported_price_anchor="LG Chem to sell 2T won / $1.43B worth of LGES shares",
        reported_return_anchor="Full adjusted OHLC unavailable in this pass",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"stake_sale_krw_trn": 2.0, "stake_sale_usd_bn": 1.43, "stake_reduction_pp": 2.5, "post_sale_lges_stake_pct": 79.4, "transaction_method": "price_return_swap"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_capital_recycling_watch",
        rerating_result="unknown",
        round_rerating_label="parent_battery_value_recycling_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stake_sale_not_roic_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="지분매각은 Green이 아니라 자본재활용 Stage 2다. ROIC와 부채감축, 주주환원, 소재마진이 확인되어야 한다.",
    ),
    Round272CaseCandidate(
        case_id="r3_loop13_samsung_sdi_tesla_ess_unconfirmed_report",
        symbol="006400",
        company_name="Samsung SDI",
        primary_archetype=E2RArchetype.ESS_REPORT_UNCONFIRMED_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.ESS_LFP_GRID_STORAGE, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE),
        case_type="event_premium",
        round_case_type="event_premium_unconfirmed_report",
        stage1_date=date(2025, 11, 3),
        stage2_date=date(2025, 11, 3),
        stage3_date=None,
        stage4b_date=date(2025, 11, 3),
        stage4c_date=None,
        stage3_decision="press_report_and_unnamed_source_are_not_green_without_signed_final_contract_gwh_and_margin",
        stage4b_status="4B-watch/reported-contract-before-confirmation",
        hard_4c_confirmed=False,
        evidence_fields=("reported_tesla_ess_deal_over_3tn_krw", "reported_2_11bn_usd_value", "reported_three_year_supply"),
        red_flag_fields=("samsung_sdi_said_nothing_decided", "tesla_no_comment", "actual_signed_contract_false", "reported_deal_without_confirmation"),
        price_data_source="Reuters report-based anchor",
        reported_price_anchor="Reported >3T won / $2.11B ESS deal, but company said nothing decided",
        reported_return_anchor="Full adjusted OHLC unavailable in this pass",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"reported_contract_value_krw_trn": 3.0, "reported_contract_value_usd_bn": 2.11, "reported_supply_period_years": 3.0, "actual_signed_contract": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium",
        rerating_result="event_premium",
        round_rerating_label="ESS_headline_unconfirmed_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="report_not_contract",
        price_validation_status="reported_deal_not_confirmed",
        notes="회사가 '결정된 것 없다'고 한 보도는 signed contract가 아니다. Green 대신 event premium으로 둔다.",
    ),
    Round272CaseCandidate(
        case_id="r3_loop13_ecopro_materials_precursor_demand_break",
        symbol="450080",
        company_name="EcoPro Materials",
        primary_archetype=E2RArchetype.PRECURSOR_IPO_OVERHEAT_DEMAND_BREAK,
        secondary_archetypes=(E2RArchetype.PRECURSOR_SUPPLY_CHAIN_SHOCK, E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT),
        case_type="failed_rerating",
        round_case_type="failed_rerating_precursor_demand_break",
        stage1_date=date(2023, 11, 1),
        stage2_date=date(2023, 11, 1),
        stage3_date=None,
        stage4b_date=date(2023, 11, 1),
        stage4c_date=date(2024, 6, 14),
        stage3_decision="ipo_and_vertical_integration_are_not_green_without_customer_order_utilization_margin_and_fcf",
        stage4b_status="4B-watch/IPO-overheat",
        hard_4c_confirmed=False,
        evidence_fields=("cathode_precursor_ipo", "vertical_integration_story", "ipo_raise_419bn_krw"),
        red_flag_fields=("shares_minus_11pct_to_119200_krw", "weak_ev_demand", "mineral_price_pressure", "utilization_margin_unconfirmed"),
        price_data_source="MarketWatch price anchor + IPO/company context",
        reported_price_anchor="EcoPro Materials shares -11% to 119,200 won on 2024-06-14",
        reported_return_anchor="Implied pre-event price about 133,933 won",
        event_mfe_pct=None,
        event_mae_pct=-11.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=119200.0,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"event_date": "2024-06-14", "event_price_krw": 119200.0, "event_mae_pct": -11.0, "implied_pre_event_price_krw": 133933.0, "ipo_raise_krw_bn": 419.0},
        score_price_alignment="false_positive_score",
        round_alignment_label="failed_rerating",
        rerating_result="theme_overheat",
        round_rerating_label="precursor_vertical_integration_overheat",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="IPO_story_without_demand_margin",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="IPO와 수직계열화 story는 고객주문, 가동률, 마진, FCF를 대신하지 못한다.",
    ),
    Round272CaseCandidate(
        case_id="r3_loop13_aricell_sconnect_battery_safety_hard_reference",
        symbol="S-Connect_readthrough/battery_safety_basket",
        company_name="Aricell / S-Connect",
        primary_archetype=E2RArchetype.BATTERY_SAFETY_HARD_REFERENCE,
        secondary_archetypes=(E2RArchetype.BATTERY_SAFETY_INDUSTRIAL_ACCIDENT_OVERLAY, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="4c_thesis_break",
        round_case_type="hard_4C_safety_reference",
        stage1_date=date(2024, 6, 24),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 6, 24),
        stage3_decision="battery_safety_quality_failure_is_a_hard_gate_not_positive_evidence",
        stage4b_status="none",
        hard_4c_confirmed=True,
        evidence_fields=("hwaseong_lithium_battery_factory_fire", "aricell_plant", "battery_units_in_warehouse_35000"),
        red_flag_fields=("23_workers_killed", "s_connect_reported_minus_23pct", "quality_failures", "temporary_worker_safety_failure", "ceo_sentence_15_years"),
        price_data_source="FT / Reuters safety and legal anchors",
        reported_price_anchor="S-Connect reportedly -23%; 23 deaths; CEO and senior executive sentenced to 15 years",
        reported_return_anchor="fatal safety event; full OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=-23.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"fatalities": 23.0, "battery_units_in_warehouse": 35000.0, "s_connect_reported_mae_pct": -23.0, "ceo_sentence_years": 15.0, "son_executive_sentence_years": 15.0, "legal_validation_date": "2025-09-23"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="battery_safety_quality_hard_reference",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C_reference",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="배터리 업종에서 안전·품질 사고는 매출 성장보다 먼저 보는 hard gate다.",
    ),
    Round272CaseCandidate(
        case_id="r3_loop13_feoc_graphite_policy_relief",
        symbol="battery_supply_chain_basket",
        company_name="Korea FEOC / graphite supply-chain policy relief basket",
        primary_archetype=E2RArchetype.FEOC_GRAPHITE_POLICY_RELIEF_NOT_GREEN,
        secondary_archetypes=(E2RArchetype.BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY, E2RArchetype.PRICE_ONLY_POLICY_RALLY),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_relief",
        stage1_date=date(2024, 4, 26),
        stage2_date=date(2024, 5, 8),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="policy_support_is_stage2_relief_not_green_until_non_china_supply_customer_certification_margin_and_fcf_confirm",
        stage4b_status="4B-watch/policy-relief-before-contracts",
        hard_4c_confirmed=False,
        evidence_fields=("china_battery_grade_graphite_share_over_99pct", "china_synthetic_graphite_share_69pct", "korea_support_package_9_7tn_krw", "cheap_state_loans_and_tax_incentives"),
        red_flag_fields=("company_level_contracts_unconfirmed", "non_china_sourcing_unconfirmed", "customer_certification_unconfirmed", "policy_support_without_contracts"),
        price_data_source="FT / WSJ policy anchors",
        reported_price_anchor="Korea announced 9.7T won / $7.14B battery supply-chain support package",
        reported_return_anchor="Policy anchor; company-level price path unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"china_battery_grade_graphite_share_pct": 99.0, "china_synthetic_graphite_share_pct": 69.0, "korea_support_package_krw_trn": 9.7, "korea_support_package_usd_bn": 7.14, "company_level_contracts_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_policy_relief",
        rerating_result="policy_event_rerating",
        round_rerating_label="FEOC_graphite_supply_chain_relief",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="policy_not_supply_margin_green",
        price_validation_status="policy_anchor_not_full_ohlc",
        notes="FEOC/graphite 정책은 섹터 relief다. 실제 탈중국 공급계약, 고객 인증, 마진 전에는 회사 Green이 아니다.",
    ),
)


def round272_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("calloff", "gwh", "delivery", "utilization", "margin", "fcf", "ex_ira", "sourcing")
    for candidate in ROUND272_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND272_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round272 R3 Loop-13 battery/EV/green price-validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "4b" in field.lower()
                or "headline" in field.lower()
                or "ipo" in field.lower()
                or "policy" in field.lower()
                or "reported_deal" in field.lower()
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "collapse" in field.lower()
                or "failure" in field.lower()
                or "fire" in field.lower()
                or "fatal" in field.lower()
                or "quality" in field.lower()
                or "4c" in field.lower()
                or "minus" in field.lower()
            ),
            must_have_fields=ROUND272_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND272_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_tesla_ess_lfp_ira_feoc_or_battery_material_keywords_as_green_alone",
                *ROUND272_GREEN_REQUIRED_FIELDS,
                *ROUND272_GREEN_FORBIDDEN_PATTERNS,
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
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round272_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND272_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "source_sector": "R3",
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


def round272_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND272_SCORE_ADJUSTMENTS)


def round272_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND272_SHADOW_WEIGHT_ROWS)


def round272_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND272_DEEP_SUB_ARCHETYPES)


def round272_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round272_price_validation": "true"} for field in ROUND272_PRICE_VALIDATION_FIELDS)


def round272_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round272_label": label, "canonical_archetype": canonical} for label, canonical in ROUND272_REQUIRED_TARGET_ALIASES.items())


def round272_summary() -> dict[str, int | bool | str]:
    cases = ROUND272_CASE_CANDIDATES
    return {
        "source_round": ROUND272_SOURCE_ROUND_PATH,
        "round_id": ROUND272_ANALYST_ROUND_ID,
        "large_sector": ROUND272_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_reference_count": sum(1 for case in cases if case.case_type == "4c_thesis_break"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None),
        "price_data_unavailable_count": sum(1 for case in cases if case.price_validation_status == "price_data_unavailable_after_deep_search"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "aligned_count": sum(1 for case in cases if case.score_price_alignment == "aligned"),
        "target_archetype_count": len(ROUND272_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND272_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND272_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round272_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND272_SOURCE_ROUND_PATH,
        "round_id": ROUND272_ANALYST_ROUND_ID,
        "large_sector": ROUND272_LARGE_SECTOR,
        "summary": round272_summary(),
        "target_aliases": dict(ROUND272_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND272_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND272_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND272_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND272_HARD_4C_GATES),
        "deep_sub_archetypes": round272_deep_sub_archetype_rows(),
        "shadow_weights": round272_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round272_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_tesla_ess_lfp_ira_feoc_or_battery_material_keywords_as_green_alone",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round272_summary_markdown() -> str:
    summary = round272_summary()
    lines = [
        "# Round 272 R3 Loop 13 Battery EV Green Price Validation",
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
        f"- hard_4c_reference: {summary['hard_4c_reference_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch/hard cases: {summary['stage4c_watch_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- evidence_good_but_price_failed: {summary['evidence_good_but_price_failed_count']}",
        f"- full_adjusted_ohlc_complete: {str(summary['full_adjusted_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND272_CASE_CANDIDATES:
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
            "- R3 Stage 3 is not the word Tesla, ESS, LFP, IRA, graphite, policy, or battery material.",
            "- L&F/Tesla is hard 4C because the contract value collapsed from $2.9B to $7,386.",
            "- LGES/Tesla LFP ESS is Stage 2, not Green, until GWh, shipment, utilization, margin, ex-subsidy OP and FCF confirm.",
            "- LGES Q2 shows headline OP can fail quality gates when ex-IRA OP is nearly absent.",
            "- Samsung SDI/Tesla ESS is event premium while company confirmation is missing.",
            "- Aricell/S-Connect is a battery safety hard reference: safety/quality can override growth narratives.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round272_green_gate_review_markdown() -> str:
    lines = ["# Round 272 R3 Loop 13 Green Gate Review", "", "Do not apply these weights to production scoring yet.", "", "## Required Fields", ""]
    lines.extend(f"- {field}" for field in ROUND272_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND272_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `Tesla 계약`이라는 말만으로는 Green이 아니다. 실제 call-off와 납품량이 필요하다.",
            "- `OP가 늘었다`도 보조금 제외 OP가 0에 가까우면 품질 게이트를 통과하지 못한다.",
            "- `정책 지원`은 섹터 relief일 수 있지만 회사별 계약·인증·마진 전에는 Green이 아니다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round272_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 272 R3 Loop 13 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND272_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND272_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B는 Tesla/ESS/FEOC 같은 headline 가격이 실제 GWh, margin, FCF보다 먼저 간 상태다.",
            "- 4C는 계약 붕괴, call-off 실패, 안전 사고, 보조금 제거 후 OP 붕괴처럼 논리가 깨지는 상태다.",
            "- 이번 라운드의 hard 4C는 L&F/Tesla contract collapse와 Aricell/S-Connect safety reference다.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND272_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.stage4c_date:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round272_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 272 R3 Loop 13 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND272_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round272_r3_loop13_reports(
    output_directory: str | Path = ROUND272_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND272_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND272_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round272_case_records(), cases_path),
        "audit": _write_json(round272_audit_payload(), audit_path),
        "summary": output / "round272_r3_loop13_price_validation_summary.md",
        "case_matrix": output / "round272_r3_loop13_case_matrix.csv",
        "target_aliases": output / "round272_r3_loop13_target_aliases.csv",
        "score_adjustments": output / "round272_r3_loop13_score_adjustments.csv",
        "shadow_weights": output / "round272_r3_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round272_r3_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round272_r3_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round272_r3_loop13_green_gate_review.md",
        "price_validation_plan": output / "round272_r3_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round272_r3_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round272_summary_markdown(), encoding="utf-8")
    _write_csv(round272_case_rows(), paths["case_matrix"])
    _write_csv(round272_target_alias_rows(), paths["target_aliases"])
    _write_csv(round272_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round272_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round272_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round272_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round272_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round272_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round272_stage4b_4c_review_markdown(), encoding="utf-8")
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
