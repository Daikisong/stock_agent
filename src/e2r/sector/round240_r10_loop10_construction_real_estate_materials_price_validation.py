"""Round-240 R10 Loop-10 construction/real-estate/materials price validation pack.

Round 240 is calibration/evaluation material only. It turns
``docs/round/round_240.md`` into case-library records and guardrail reports.

Easy example: a signed nuclear project can be Stage 2. It is not Stage
3-Green until the listed supplier's package amount, margin, working capital,
and cash collection are visible.
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


ROUND240_SOURCE_ROUND_PATH = "docs/round/round_240.md"
ROUND240_ANALYST_ROUND_ID = "round_168"
ROUND240_LARGE_SECTOR = Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS
ROUND240_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round240_r10_loop10_construction_real_estate_materials_price_validation"
ROUND240_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop10_round240.jsonl"
ROUND240_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round240_r10_loop10_construction_real_estate_materials_price_validation_audit.json"

ROUND240_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "NUCLEAR_INFRA_EPC_EXPORT": E2RArchetype.NUCLEAR_INFRA_EPC_EXPORT.value,
    "PORT_INFRA_DELIVERY": E2RArchetype.PORT_INFRA_DELIVERY.value,
    "HOUSING_POLICY_SUPPLY_EVENT": E2RArchetype.HOUSING_POLICY_SUPPLY_EVENT.value,
    "REAL_ESTATE_PF_CREDIT_BREAK": E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK.value,
    "CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C": E2RArchetype.CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C.value,
    "WORKPLACE_FATALITY_REGULATORY_4C": E2RArchetype.WORKPLACE_FATALITY_REGULATORY_4C.value,
    "AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT": E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT.value,
    "BUILDING_MATERIALS_DEMAND_CYCLE": E2RArchetype.BUILDING_MATERIALS_DEMAND_CYCLE.value,
    "PRICE_ONLY_POLICY_RALLY": E2RArchetype.PRICE_ONLY_POLICY_RALLY.value,
    "EVIDENCE_GOOD_BUT_PRICE_UNPROVEN": E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_UNPROVEN.value,
}

ROUND240_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "listed_company_contract_or_delivery_milestone",
    "margin_or_noi_affo_visibility",
    "cash_flow_after_working_capital",
    "pf_or_funding_cost_risk_passed",
    "cost_control_and_progress_revenue_visibility",
    "tenant_occupancy_or_utilization_verified",
    "capex_per_share_or_dilution_passed",
    "safety_quality_hard_risk_absent",
    "price_path_after_evidence",
)

ROUND240_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "preferred_bidder_only",
    "contract_headline_only",
    "pf_relief_policy_only",
    "housing_supply_policy_only",
    "data_center_theme_without_tenant",
    "asset_headline_without_noi_affo",
    "epc_backlog_without_margin",
    "safety_accident_or_fatality",
    "working_capital_or_funding_cost_break",
)

ROUND240_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "preferred_bidder_rally_before_supplier_margin",
    "large_epc_order_rally_before_cash_collection",
    "pf_support_rally_before_balance_sheet_repair",
    "data_center_theme_rally_before_tenant_noi_affo",
    "housing_policy_rally_before_presales_margin_fcf",
    "reit_or_real_asset_yield_rally_before_affo_integrity",
)

ROUND240_HARD_4C_GATES: tuple[str, ...] = (
    "pf_workout_or_debt_reschedule",
    "pf_delinquency_spike",
    "bridge_loan_rollover_failure",
    "fatal_construction_accident",
    "repeated_workplace_fatality",
    "site_shutdown",
    "license_revocation_risk",
    "low_margin_epc_loss",
    "payment_delay_or_order_cancellation",
    "tenant_absence",
    "power_water_permitting_failure",
    "affo_integrity_break",
    "capex_dilution",
)

ROUND240_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "mfe_3m_reported",
    "contract_or_policy_anchor",
    "pf_or_safety_anchor",
    "tenant_or_noi_affo_anchor",
    "building_material_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round240ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round240ShadowWeightRow:
    archetype: E2RArchetype
    cash_flow_after_wc: int
    epc_margin: int
    project_cost_control: int
    progress_revenue: int
    handover_milestone: int
    pf_cleanup: int
    funding_cost: int
    tenant_noi_affo: int
    safety_trust: int
    event_penalty: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "cash_flow_after_wc": _signed(self.cash_flow_after_wc),
            "epc_margin": _signed(self.epc_margin),
            "project_cost_control": _signed(self.project_cost_control),
            "progress_revenue": _signed(self.progress_revenue),
            "handover_milestone": _signed(self.handover_milestone),
            "pf_cleanup": _signed(self.pf_cleanup),
            "funding_cost": _signed(self.funding_cost),
            "tenant_noi_affo": _signed(self.tenant_noi_affo),
            "safety_trust": _signed(self.safety_trust),
            "event_penalty": _signed(self.event_penalty),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round240CaseCandidate:
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
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str | bool | list[str]]
    score_price_alignment: str
    round_score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND240_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND240_SCORE_ADJUSTMENTS: tuple[Round240ScoreAdjustment, ...] = (
    Round240ScoreAdjustment("cash_flow_after_working_capital", 5, "raise", "R10 수주는 운전자본 이후 현금흐름이 닫혀야 강해진다."),
    Round240ScoreAdjustment("EPC_margin_visibility", 5, "raise", "해외 EPC/원전/항만은 계약금액보다 마진과 현금회수가 핵심이다."),
    Round240ScoreAdjustment("project_cost_control", 5, "raise", "공사비·인건비·금융비용 통제가 Stage 3 전제다."),
    Round240ScoreAdjustment("progress_revenue_visibility", 4, "raise", "공정률과 진행매출 가시성이 없는 backlog는 Stage 2에 머문다."),
    Round240ScoreAdjustment("handover_milestone", 4, "raise", "Grand Faw dock completion처럼 인도 milestone은 단순 수주보다 높게 본다."),
    Round240ScoreAdjustment("PF_credit_cleanup", 5, "raise", "PF cleanup이 확인될 때만 건설 credit risk가 풀린다."),
    Round240ScoreAdjustment("funding_cost_control", 5, "raise", "PF·REIT·data center는 funding cost가 FCF/AFFO를 흔든다."),
    Round240ScoreAdjustment("tenant_contract_quality", 5, "raise", "데이터센터는 임차인 계약이 있어야 real asset evidence가 된다."),
    Round240ScoreAdjustment("NOI_AFFO_visibility", 5, "raise", "부동산/데이터센터는 NOI/AFFO per share가 Stage 3 핵심이다."),
    Round240ScoreAdjustment("power_water_permitting_secured", 4, "raise", "전력·용수·인허가가 빠진 data center는 headline이다."),
    Round240ScoreAdjustment("safety_quality_trust", 5, "raise", "건설 안전 신뢰가 깨지면 수주보다 4C gate가 우선한다."),
    Round240ScoreAdjustment("contract_headline_only", -5, "lower", "수주 headline만으로는 margin/cash collection이 아니다."),
    Round240ScoreAdjustment("preferred_bidder_only", -4, "lower", "우선협상대상자는 signed contract와 supplier package 전 Stage 2 이전 신호다."),
    Round240ScoreAdjustment("PF_relief_policy_only", -5, "lower", "PF 지원책은 crisis relief이지 Green 근거가 아니다."),
    Round240ScoreAdjustment("housing_supply_policy_only", -4, "lower", "주택공급 정책은 분양률·원가율·PF·FCF 전 Green이 아니다."),
    Round240ScoreAdjustment("data_center_theme_without_tenant", -5, "lower", "데이터센터 테마는 tenant/NOI/AFFO 전 Stage 1/2다."),
    Round240ScoreAdjustment("asset_headline_without_NOI_AFFO", -5, "lower", "자산 보유 headline은 AFFO integrity 전 Green이 아니다."),
    Round240ScoreAdjustment("EPC_backlog_without_margin", -5, "lower", "저마진 EPC backlog는 오히려 4C가 될 수 있다."),
    Round240ScoreAdjustment("low_margin_order_risk", -4, "lower", "대형 수주라도 원가율·마진이 약하면 감점한다."),
    Round240ScoreAdjustment("capex_per_share_dilution", -4, "lower", "capex가 주당 AFFO/FCF를 희석하면 Stage 3를 막는다."),
    Round240ScoreAdjustment("quality_safety_incident", -5, "lower", "붕괴·품질·안전사고는 hard 4C 입력이다."),
    Round240ScoreAdjustment("workplace_fatality_repeated", -5, "lower", "반복 사망사고와 면허 리스크는 건설 Green을 차단한다."),
    Round240ScoreAdjustment("building_material_demand_weakness", -4, "lower", "철근·건자재 수요 약화는 건자재 Green을 막는다."),
)


ROUND240_SHADOW_WEIGHT_ROWS: tuple[Round240ShadowWeightRow, ...] = (
    Round240ShadowWeightRow(E2RArchetype.NUCLEAR_INFRA_EPC_EXPORT, 5, 5, 5, 4, 4, 0, 4, 0, 3, -4, 4, "Preferred bidder/signed contract is Stage 2 until listed-company margin and cashflow confirm."),
    Round240ShadowWeightRow(E2RArchetype.PORT_INFRA_DELIVERY, 5, 5, 4, 4, 5, 0, 3, 0, 3, -3, 4, "Grand Faw dock completion is delivery Stage 2; margin and cash collection required."),
    Round240ShadowWeightRow(E2RArchetype.HOUSING_POLICY_SUPPLY_EVENT, 3, 2, 3, 2, 0, 4, 4, 0, 2, -5, 4, "Housing policy is Stage 1/2 until presales, margin, PF and FCF confirm."),
    Round240ShadowWeightRow(E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK, 5, 0, 0, 0, 0, 5, 5, 0, 2, -5, 5, "PF delinquency spike and debt reschedule are hard 4C."),
    Round240ShadowWeightRow(E2RArchetype.CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, "Fatal construction accident is sector hard 4C."),
    Round240ShadowWeightRow(E2RArchetype.WORKPLACE_FATALITY_REGULATORY_4C, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, "Recurring fatal accidents create fine/license risk and block Green."),
    Round240ShadowWeightRow(E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT, 4, 0, 4, 2, 0, 0, 5, 5, 3, -5, 4, "Data center requires tenant, NOI/AFFO, power/water and capex per share."),
    Round240ShadowWeightRow(E2RArchetype.BUILDING_MATERIALS_DEMAND_CYCLE, 4, 4, 3, 0, 0, 3, 4, 0, 2, -4, 4, "Rebar/building-material weakness blocks Green until demand and margin stabilize."),
)


ROUND240_CASE_CANDIDATES: tuple[Round240CaseCandidate, ...] = (
    Round240CaseCandidate(
        case_id="r10_loop10_czech_nuclear_infra_korea_epc",
        symbol="034020/052690/051600/015760",
        company_name="두산에너빌리티/한전기술/한전KPS/한국전력",
        primary_archetype=E2RArchetype.NUCLEAR_INFRA_EPC_EXPORT,
        secondary_archetypes=(E2RArchetype.PRICE_ONLY_POLICY_RALLY, E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_UNPROVEN),
        case_type="success_candidate",
        round_case_type="success_candidate_legal_watch",
        stage1_date=date(2024, 7, 17),
        stage2_date=date(2025, 6, 4),
        stage3_date=None,
        stage4b_date=date(2024, 7, 17),
        stage4c_date=date(2025, 5, 6),
        stage3_decision="signed_contract_is_stage2_until_listed_supplier_package_margin_working_capital_and_cash_collection_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("preferred_bidder", "signed_contract_407bn_koruna", "contract_value_18_7bn_usd", "two_reactors", "doosan_3m_mfe_48pct", "kepco_ec_3m_mfe_41pct"),
        red_flag_fields=("preferred_bidder_only", "legal_challenge_watch", "listed_supplier_package_unverified", "margin_unverified", "cash_collection_unverified"),
        price_data_source="Reuters/AP nuclear-contract and sector-return anchors",
        reported_price_anchor="Doosan Enerbility +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% around preferred-bidder period",
        reported_return_anchor="407B koruna / $18.7B for two Dukovany reactors; first trial operation expected 2036",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"doosan_3m_mfe_pct": 48.0, "kepco_plant_se_3m_mfe_pct": 14.0, "kepco_ec_3m_mfe_pct": 41.0, "czech_contract_value_koruna_bn": 407.0, "czech_contract_value_usd_bn": 18.7, "prior_contract_expectation_usd_bn": 17.56, "reactor_count": 2.0, "unit_cost_context_koruna_bn": 200.0, "unit_cost_context_usd_bn": 8.65, "first_trial_operation_expected_year": 2036.0, "second_trial_operation_expected_year": 2038.0},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="success_candidate_legal_watch",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_sector_return_not_full_ohlc",
        notes="Preferred bidder to signed contract is Stage 2; supplier package, margin and cash collection required before Green.",
    ),
    Round240CaseCandidate(
        case_id="r10_loop10_daewoo_enc_grand_faw_port_delivery",
        symbol="047040",
        company_name="대우건설",
        primary_archetype=E2RArchetype.PORT_INFRA_DELIVERY,
        secondary_archetypes=(E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_UNPROVEN,),
        case_type="success_candidate",
        round_case_type="success_candidate_infrastructure_delivery",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 11, 12),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="dock_completion_is_stage2_until_new_revenue_backlog_margin_and_cash_collection_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("five_docks_completed", "operation_start_2026", "capacity_3_5m_containers_by_2028", "development_road_17bn_usd"),
        red_flag_fields=("new_order_unverified", "margin_unverified", "cash_collection_unverified", "iraq_payment_or_security_risk"),
        price_data_source="Reuters infrastructure-delivery anchor",
        reported_price_anchor="Daewoo E&C stock OHLC unavailable after deep search",
        reported_return_anchor="Five docks completed; operation planned 2026; 3.5M container capacity by 2028; $17B Development Road project",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"completed_docks": 5.0, "operation_start_target_year": 2026.0, "maximum_capacity_target_mn_containers": 3.5, "capacity_target_year": 2028.0, "development_road_project_value_usd_bn": 17.0},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Dock completion is stronger than an order headline, but additional backlog, margin and cash collection are required before Stage 3.",
    ),
    Round240CaseCandidate(
        case_id="r10_loop10_seoul_housing_policy_supply_watch",
        symbol="housing_construction_basket",
        company_name="서울 주택공급/대출규제 건설 바스켓",
        primary_archetype=E2RArchetype.HOUSING_POLICY_SUPPLY_EVENT,
        secondary_archetypes=(E2RArchetype.PRICE_ONLY_POLICY_RALLY, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_policy_watch",
        stage1_date=date(2025, 3, 19),
        stage2_date=date(2025, 9, 7),
        stage3_date=None,
        stage4b_date=date(2025, 9, 7),
        stage4c_date=None,
        stage3_decision="housing_policy_is_stage1_2_until_presales_margin_pf_stability_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ltv_50_to_40pct", "permit_zone_tightening", "state_land_development", "reconstruction_rule_simplification"),
        red_flag_fields=("housing_supply_policy_only", "ltv_tightening_demand_shock", "presales_unverified", "pf_stability_unverified", "fcf_unverified"),
        price_data_source="Reuters housing-policy evidence",
        reported_price_anchor="Housing basket OHLC unavailable after deep search",
        reported_return_anchor="LTV tightened from 50% to 40%; permit-zone tightening in Gangnam/Seocho/Songpa/Yongsan",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ltv_before_pct": 50.0, "ltv_after_pct": 40.0, "ltv_reduction_pp": -10.0, "ltv_reduction_relative_pct": -20.0, "affected_districts": ["Gangnam", "Yongsan", "Gangnam/Seocho/Songpa/Yongsan permit zone"], "policy_mix": "demand_control_plus_supply_support"},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="event_premium_policy_watch",
        rerating_result="policy_event_rerating",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Housing policy is Stage 1/2; presales, margin, PF stability and FCF are required before Green.",
    ),
    Round240CaseCandidate(
        case_id="r10_loop10_taeyoung_pf_credit_hard_4c",
        symbol="009410/PF_basket",
        company_name="태영건설/건설 PF 스트레스",
        primary_archetype=E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK,
        secondary_archetypes=(E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,),
        case_type="4c_thesis_break",
        round_case_type="hard_4c_pf_credit_break",
        stage1_date=date(2023, 12, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 5, 13),
        stage3_decision="pf_debt_reschedule_and_delinquency_spike_are_hard_4c_not_liquidity_green",
        stage4b_status="hard_4c",
        hard_4c_confirmed=True,
        evidence_fields=("pf_delinquency_0_37_to_2_70pct", "government_support_40_6tn_krw", "syndicated_loan_1tn_expandable_5tn", "project_assessment_toughened"),
        red_flag_fields=("pf_workout_or_debt_reschedule", "pf_delinquency_spike", "liquidity_crisis", "pf_relief_policy_only"),
        price_data_source="Reuters PF stress/policy-support anchors",
        reported_price_anchor="Taeyoung stock OHLC unavailable after deep search",
        reported_return_anchor="PF delinquency 0.37% to 2.70%; +629.7%; 1T loan expandable to 5T; 40.6T support package",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"pf_delinquency_2021_pct": 0.37, "pf_delinquency_2022_pct": 1.19, "pf_delinquency_2023_pct": 2.70, "pf_delinquency_increase_2021_to_2023_pp": 2.33, "pf_delinquency_increase_2021_to_2023_pct": 629.7, "pf_delinquency_increase_2022_to_2023_pct": 126.9, "syndicated_loan_initial_krw_trn": 1.0, "syndicated_loan_max_krw_trn": 5.0, "loan_expandability_multiple": 5.0, "government_support_package_krw_trn": 40.6},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Debt reschedule and PF delinquency spike are hard 4C; liquidity support is relief, not Green.",
    ),
    Round240CaseCandidate(
        case_id="r10_loop10_hyundai_engineering_bridge_collapse_sector_hard_4c",
        symbol="unlisted_Hyundai_Engineering/sector_exposure",
        company_name="현대엔지니어링 교량 붕괴 섹터 케이스",
        primary_archetype=E2RArchetype.CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C,
        secondary_archetypes=(E2RArchetype.OPERATIONAL_TRUST_BREAK,),
        case_type="4c_thesis_break",
        round_case_type="sector_hard_4c_direct_listed_mapping_unclear",
        stage1_date=date(2025, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 2, 25),
        stage3_decision="fatal_bridge_collapse_is_sector_hard_4c_even_when_direct_listed_mapping_is_unclear",
        stage4b_status="hard_4c",
        hard_4c_confirmed=True,
        evidence_fields=("fatalities_4", "injuries_6", "workers_fell_10", "highway_bridge_collapse", "hyundai_engineering_site"),
        red_flag_fields=("fatal_construction_accident", "operational_trust_break", "site_safety_failure", "direct_listed_mapping_unclear"),
        price_data_source="Reuters/AP/Washington Post safety-event evidence",
        reported_price_anchor="Hyundai Engineering is not directly listed; stock OHLC unavailable",
        reported_return_anchor="4 killed, 6 injured, 10 workers fell; partially constructed highway bridge collapse",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fatalities": 4.0, "injuries": 6.0, "workers_fell": 10.0, "critical_injuries": 5.0, "listed_stock_mapping": "unclear_not_direct_listed_vehicle", "event_type": "partially constructed highway bridge collapse"},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="not_direct_listed_stock_price_unavailable",
        notes="Fatal bridge collapse is sector hard 4C; direct listed mapping is unclear.",
    ),
    Round240CaseCandidate(
        case_id="r10_loop10_posco_dl_construction_safety_regulation",
        symbol="POSCO_EC/DL_Construction_exposure",
        company_name="포스코이앤씨/DL건설 안전 규제",
        primary_archetype=E2RArchetype.WORKPLACE_FATALITY_REGULATORY_4C,
        secondary_archetypes=(E2RArchetype.CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C,),
        case_type="4c_thesis_break",
        round_case_type="4c_watch_recurring_fatality_regulation",
        stage1_date=date(2025, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 15),
        stage3_decision="recurring_fatal_accidents_and_site_shutdowns_are_4c_watch_and_green_blockers",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("posco_ec_sites_halted_103", "dl_construction_execs_resigned_80", "fine_up_to_5pct_op", "license_revocation_risk", "construction_death_rate_15_9_per_100k"),
        red_flag_fields=("repeated_workplace_fatality", "site_shutdown", "license_revocation_risk", "fine_up_to_5pct_operating_profit"),
        price_data_source="Reuters safety-regulation evidence",
        reported_price_anchor="Direct listed event OHLC unavailable after deep search",
        reported_return_anchor="103 sites halted; about 80 executives resigned; fine up to 5% of operating profit",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"korea_industrial_death_rate_per_100k": 3.9, "oecd_average_death_rate_per_100k": 2.6, "relative_excess_vs_oecd_pct": 50.0, "korea_construction_death_rate_per_100k": 15.9, "workplace_deaths_2024": 589.0, "construction_share": "nearly_half", "posco_ec_sites_halted": 103.0, "dl_construction_executives_resigned": 80.0, "proposed_fine_pct_of_operating_profit": 5.0, "license_revocation_risk": True},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="direct_listed_event_ohlc_unavailable",
        notes="Recurring fatal accidents and site shutdowns require 4C-watch and safety-trust gate.",
    ),
    Round240CaseCandidate(
        case_id="r10_loop10_ai_data_center_real_asset_event",
        symbol="SK_group/Samsung_SDS/SK_Telecom/Samsung_CT/Samsung_Heavy_related",
        company_name="SK/AWS·OpenAI·삼성 데이터센터 real asset",
        primary_archetype=E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM, E2RArchetype.PRICE_ONLY_POLICY_RALLY),
        case_type="success_candidate",
        round_case_type="success_candidate_event_premium",
        stage1_date=date(2025, 6, 20),
        stage2_date=date(2025, 10, 1),
        stage3_date=None,
        stage4b_date=date(2025, 6, 20),
        stage4c_date=None,
        stage3_decision="data_center_investment_is_stage1_2_until_tenant_noi_affo_power_water_permitting_and_capex_per_share_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("sk_aws_7tn_krw", "initial_capacity_100mw", "potential_expansion_1gw", "openai_samsung_sk_20mw", "kakao_mfe_11pct", "lg_cns_mfe_9pct"),
        red_flag_fields=("data_center_theme_without_tenant", "asset_headline_without_noi_affo", "power_water_permitting_unverified", "capex_per_share_unverified"),
        price_data_source="Reuters/AP investment and event-return anchors",
        reported_price_anchor="SK Hynix >+3%, Kakao +11%, LG CNS +9% on AI data-center event",
        reported_return_anchor="7T KRW / $5.11B Ulsan AI data center; 100MW by 2029; possible 1GW expansion",
        mfe_1d=11.0,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"sk_aws_investment_krw_trn": 7.0, "sk_aws_investment_usd_bn": 5.11, "aws_component_usd_bn": 4.0, "initial_capacity_mw": 100.0, "potential_expansion_gw": 1.0, "capacity_expansion_potential_multiple": 10.0, "construction_start_planned": "2025-09", "full_operation_planned_year": 2029.0, "openai_samsung_sk_initial_capacity_mw": 20.0, "sk_hynix_event_mfe_pct": 3.0, "kakao_event_mfe_pct": 11.0, "lg_cns_event_mfe_pct": 9.0, "floating_data_center_collaboration": True},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="event_premium_success_candidate",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="AI data-center investment is Stage 1/2; tenant, NOI/AFFO, power/water/permitting and capex per share required before Green.",
    ),
    Round240CaseCandidate(
        case_id="r10_loop10_hyundai_steel_rebar_construction_demand_watch",
        symbol="004020",
        company_name="현대제철/철근 건설수요 proxy",
        primary_archetype=E2RArchetype.BUILDING_MATERIALS_DEMAND_CYCLE,
        secondary_archetypes=(E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_UNPROVEN,),
        case_type="4c_thesis_break",
        round_case_type="4c_watch_building_material_demand_cycle",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 6, 21),
        stage3_decision="rebar_price_decline_and_profit_estimate_cut_block_building_material_green",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("event_price_29000_krw", "event_mae_minus_1_2pct", "net_profit_forecast_cut_73pct", "rebar_price_expected_decline_10pct", "target_cut_14pct"),
        red_flag_fields=("building_material_demand_weakness", "net_profit_estimate_cut", "rebar_price_decline", "construction_demand_weakness"),
        price_data_source="MarketWatch reported price/target/estimate anchor",
        reported_price_anchor="29,000 KRW, -1.2%; target 30,000 KRW",
        reported_return_anchor="2024 net-profit forecast cut 73% to 215B KRW; rebar price expected -10%",
        mfe_1d=None,
        mae_1d=-1.2,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=29000.0,
        extra_price_metrics={"event_price_krw": 29000.0, "event_mae_pct": -1.2, "implied_pre_event_reference_price_krw": 29352.0, "target_price_krw": 30000.0, "target_cut_pct": -14.0, "implied_prior_target_krw": 34884.0, "target_upside_from_event_price_pct": 3.45, "net_profit_forecast_2024_krw_bn": 215.0, "net_profit_forecast_cut_pct": -73.0, "implied_prior_net_profit_forecast_krw_bn": 796.3, "rebar_price_expected_decline_pct": -10.0},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Rebar and construction-demand weakness block building-material Green until demand, spread and margin stabilize.",
    ),
)


def round240_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND240_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round240 R10 Loop-10 construction/real-estate/materials "
                "price-path validation case. Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(field for field in candidate.evidence_fields if "policy" in field or "preferred" in field or "event" in field or "data_center" in field),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if "margin" in field or "cash" in field or "noi" in field or "affo" in field),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "mfe" in field or "event" in field or "policy" in field or "headline" in field or "preferred" in field),
            stage4c_evidence=tuple(field for field in candidate.red_flag_fields if "pf" in field or "fatal" in field or "safety" in field or "shutdown" in field or "demand" in field or "tenant" in field),
            must_have_fields=ROUND240_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND240_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_contract_policy_data_center_or_pf_relief_headline_as_green",
                *ROUND240_GREEN_REQUIRED_FIELDS,
                *ROUND240_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.stage2_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round240_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND240_CASE_CANDIDATES:
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
                "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
                "score_price_alignment": candidate.score_price_alignment,
                "round_score_price_alignment": candidate.round_score_price_alignment,
                "rerating_result": candidate.rerating_result,
                "stage_failure_type": candidate.stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round240_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND240_SCORE_ADJUSTMENTS)


def round240_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND240_SHADOW_WEIGHT_ROWS)


def round240_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round240_price_validation": "true"} for field in ROUND240_PRICE_VALIDATION_FIELDS)


def round240_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round240_label": label, "canonical_archetype": canonical} for label, canonical in ROUND240_REQUIRED_TARGET_ALIASES.items())


def round240_summary() -> dict[str, int | bool | str]:
    cases = ROUND240_CASE_CANDIDATES
    return {
        "source_round": ROUND240_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND240_ANALYST_ROUND_ID,
        "large_sector": ROUND240_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "target_archetype_count": len(ROUND240_REQUIRED_TARGET_ALIASES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round240_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND240_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND240_ANALYST_ROUND_ID,
        "large_sector": ROUND240_LARGE_SECTOR.value,
        "summary": round240_summary(),
        "target_aliases": dict(ROUND240_REQUIRED_TARGET_ALIASES),
        "round_case_types": {case.case_id: case.round_case_type for case in ROUND240_CASE_CANDIDATES},
        "green_required_fields": list(ROUND240_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND240_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND240_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND240_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_use_round240_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_contract_policy_data_center_pf_relief_or_safety_headline_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "keep_pf_credit_break_and_fatal_construction_accident_as_hard_4c_references",
        ],
    }


def render_round240_summary_markdown() -> str:
    summary = round240_summary()
    lines = [
        "# Round 240 R10 Loop 10 Construction Real Estate Materials Price Validation",
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
        f"- event_premium: {summary['event_premium_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND240_CASE_CANDIDATES:
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
            "- Czech nuclear and Grand Faw Port are Stage 2 evidence, not automatic Green.",
            "- Seoul housing policy and AI data-center events stay event/policy premium until company-level cash-flow evidence appears.",
            "- PF credit break and fatal construction accident are hard 4C references.",
            "- Workplace safety regulation and Hyundai Steel rebar weakness are 4C-watch blockers for R10 Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round240_green_gate_review_markdown() -> str:
    lines = [
        "# Round 240 R10 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND240_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND240_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `preferred bidder` is Stage 1/2.",
            "- `signed contract + listed supplier package + margin + cash collection` can support Stage 3 review.",
            "- `PF workout` or `fatal construction accident` is hard 4C, not a rerating source.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round240_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 240 R10 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND240_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND240_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND240_CASE_CANDIDATES:
        if case.stage4b_status in {"watch", "hard_4c"} or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round240_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 240 R10 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: true",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND240_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round240_r10_loop10_reports(
    output_directory: str | Path = ROUND240_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND240_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND240_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)

    paths = {
        "cases": write_case_library(round240_case_records(), cases_path),
        "audit": _write_json(round240_audit_payload(), audit_path),
        "summary": output / "round240_r10_loop10_price_validation_summary.md",
        "case_matrix": output / "round240_r10_loop10_case_matrix.csv",
        "target_aliases": output / "round240_r10_loop10_target_aliases.csv",
        "score_adjustments": output / "round240_r10_loop10_score_adjustments.csv",
        "shadow_weights": output / "round240_r10_loop10_shadow_weights.csv",
        "price_validation_fields": output / "round240_r10_loop10_price_validation_fields.csv",
        "green_gate_review": output / "round240_r10_loop10_green_gate_review.md",
        "price_validation_plan": output / "round240_r10_loop10_price_validation_plan.md",
        "stage4b_4c_review": output / "round240_r10_loop10_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round240_summary_markdown(), encoding="utf-8")
    _write_csv(round240_case_rows(), paths["case_matrix"])
    _write_csv(round240_target_alias_rows(), paths["target_aliases"])
    _write_csv(round240_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round240_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round240_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round240_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round240_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round240_stage4b_4c_review_markdown(), encoding="utf-8")
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
