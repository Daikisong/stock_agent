"""Round-253 R10 Loop-11 construction/real-estate/materials validation pack.

This pack converts ``docs/round/round_253.md`` into calibration-only case
records, shadow weights, and guardrail reports. Production scoring is not
changed.

Easy example: Samsung E&A's Fadhili contract is a strong Stage 2 event.
It is still not Stage 3-Green until progress revenue, margin, working
capital, and cash collection are visible.
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


ROUND253_SOURCE_ROUND_PATH = "docs/round/round_253.md"
ROUND253_ANALYST_ROUND_ID = "round_181"
ROUND253_LARGE_SECTOR = Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS.value
ROUND253_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round253_r10_loop11_construction_real_estate_materials_price_validation"
ROUND253_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop11_round253.jsonl"
ROUND253_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round253_r10_loop11_construction_real_estate_materials_price_validation_audit.json"

ROUND253_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "OVERSEAS_EPC_MEGA_ORDER": E2RArchetype.OVERSEAS_EPC_MEGA_ORDER.value,
    "GAS_INFRA_DELIVERY_VALIDATION": E2RArchetype.GAS_INFRA_DELIVERY_VALIDATION.value,
    "AI_DATA_CENTER_REAL_ASSET": E2RArchetype.AI_DATA_CENTER_REAL_ASSET.value,
    "HOUSING_POLICY_SUPPLY_EVENT": E2RArchetype.HOUSING_POLICY_SUPPLY_EVENT.value,
    "REAL_ESTATE_PF_CREDIT_BREAK": E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK.value,
    "CONSTRUCTION_SAFETY_REGULATORY_4C": E2RArchetype.CONSTRUCTION_SAFETY_REGULATORY_4C.value,
    "BUILDING_MATERIALS_DEMAND_CYCLE": E2RArchetype.BUILDING_MATERIALS_DEMAND_CYCLE.value,
    "PORT_INFRA_DELIVERY": E2RArchetype.PORT_INFRA_DELIVERY.value,
}

ROUND253_DEEP_SUB_ARCHETYPES: tuple[str, ...] = (
    "Samsung E&A / GS E&C overseas EPC: Fadhili contract size, project duration, margin, working capital",
    "Hyundai E&C gas infrastructure: Aramco Jafurah main gas network and company-level package validation",
    "SK/AWS Ulsan AI data center: tenant, power, water, permitting, capex per share",
    "OpenAI / Samsung SDS / SK Telecom Korea data centers: initial MW, JV, tenant economics",
    "Samsung C&T / Samsung Heavy floating data center: concept-to-cashflow validation",
    "Seoul housing policy: LTV tightening, state-owned land supply, reconstruction simplification",
    "Taeyoung / PF basket: delinquency spike, liquidity support, debt-reschedule risk",
    "POSCO E&C / DL Construction safety: fatality regulation, site shutdown, license revocation risk",
    "Hyundai Steel rebar proxy: construction demand weakness, estimate cuts, spread pressure",
    "Daewoo E&C Grand Faw Port: completed docks, operation schedule, container capacity, cash collection",
)

ROUND253_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "signed_contract_or_delivery_milestone",
    "progress_revenue_visibility",
    "OPM_or_gross_margin_visibility",
    "working_capital_control",
    "cash_collection_quality",
    "PF_or_funding_cost_risk_passed",
    "tenant_occupancy_NOI_AFFO_visibility",
    "power_water_permitting_secured",
    "safety_quality_hard_risk_absent",
    "price_path_after_evidence",
)

ROUND253_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "contract_headline_only",
    "policy_supply_headline_only",
    "data_center_theme_without_tenant",
    "preferred_project_without_company_margin",
    "PF_relief_policy_only",
    "working_capital_worsening",
    "safety_incident",
    "fatality_recurrence",
    "building_material_demand_weakness",
    "low_margin_EPC_order",
)

ROUND253_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "large_EPC_contract_announcement_5_to_10pct_jump",
    "AI_data_center_headline_basket_rally",
    "housing_reconstruction_policy_rally",
    "PF_relief_basket_rally_before_balance_sheet_repair",
    "development_plan_without_completion",
    "margin_or_working_capital_visibility_weak",
)

ROUND253_HARD_4C_GATES: tuple[str, ...] = (
    "PF_workout_or_debt_restructuring",
    "PF_delinquency_spike",
    "presales_failure_or_unsold_inventory",
    "working_capital_spike",
    "order_cancellation_or_payment_delay",
    "low_margin_EPC_loss",
    "fatal_construction_accident",
    "repeated_site_shutdown",
    "license_revocation_risk",
    "tenant_absence",
    "power_water_permitting_failure",
    "AFFO_integrity_impairment",
    "capex_dilution",
)

ROUND253_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_1d",
    "event_mae_1d",
    "relative_outperformance_pp",
    "contract_policy_safety_or_pf_anchor",
    "tenant_noi_affo_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round253ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round253ShadowWeightRow:
    archetype: E2RArchetype
    signed_contract: int
    progress_revenue: int
    epc_margin: int
    cash_collection: int
    working_capital: int
    handover_milestone: int
    tenant_noi_affo: int
    power_water_permitting: int
    pf_cleanup: int
    safety_trust: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "signed_contract": _signed(self.signed_contract),
            "progress_revenue": _signed(self.progress_revenue),
            "epc_margin": _signed(self.epc_margin),
            "cash_collection": _signed(self.cash_collection),
            "working_capital": _signed(self.working_capital),
            "handover_milestone": _signed(self.handover_milestone),
            "tenant_noi_affo": _signed(self.tenant_noi_affo),
            "power_water_permitting": _signed(self.power_water_permitting),
            "pf_cleanup": _signed(self.pf_cleanup),
            "safety_trust": _signed(self.safety_trust),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round253CaseCandidate:
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
    round_rerating_result: str
    stage_failure_type: str
    round_stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND253_LARGE_SECTOR

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND253_SCORE_ADJUSTMENTS: tuple[Round253ScoreAdjustment, ...] = (
    Round253ScoreAdjustment("signed_contract", 5, "raise", "R10 수주는 signed contract 이후에야 Stage 2로 강해진다."),
    Round253ScoreAdjustment("progress_revenue_visibility", 5, "raise", "공정률과 진행매출이 보여야 계약 headline이 실적 evidence가 된다."),
    Round253ScoreAdjustment("EPC_margin_visibility", 5, "raise", "대형 EPC는 계약금액보다 OPM/gross margin 확인이 중요하다."),
    Round253ScoreAdjustment("cash_collection_quality", 5, "raise", "공사 매출은 현금회수로 닫혀야 FCF 체급 변화가 된다."),
    Round253ScoreAdjustment("working_capital_control", 5, "raise", "운전자본 악화는 대형 수주를 4C로 바꿀 수 있다."),
    Round253ScoreAdjustment("handover_milestone", 4, "raise", "Grand Faw dock completion처럼 인도 milestone은 단순 계획보다 높게 본다."),
    Round253ScoreAdjustment("tenant_NOI_AFFO_visibility", 5, "raise", "데이터센터 real asset은 tenant와 NOI/AFFO가 보여야 한다."),
    Round253ScoreAdjustment("power_water_permitting_secured", 4, "raise", "전력·용수·인허가 없이는 AI data center가 테마에 머문다."),
    Round253ScoreAdjustment("PF_credit_cleanup", 5, "raise", "PF cleanup은 건설주 credit risk 해소의 필수 확인축이다."),
    Round253ScoreAdjustment("safety_quality_trust", 5, "raise", "건설 안전 신뢰가 깨지면 수주잔고보다 hard gate가 먼저다."),
    Round253ScoreAdjustment("contract_headline_only", -5, "lower", "계약 headline만으로 Stage 3-Green을 만들지 않는다."),
    Round253ScoreAdjustment("policy_supply_headline_only", -5, "lower", "주택공급 정책은 분양률·마진·PF 안정 전 Green 근거가 아니다."),
    Round253ScoreAdjustment("data_center_theme_without_tenant", -5, "lower", "tenant 없는 data center 테마는 Stage 1/2에 묶는다."),
    Round253ScoreAdjustment("preferred_project_without_company_margin", -4, "lower", "상장사 package와 margin이 없으면 국가 프로젝트 headline은 제한한다."),
    Round253ScoreAdjustment("PF_relief_policy_only", -5, "lower", "PF 지원책은 crisis relief이지 rerating evidence가 아니다."),
    Round253ScoreAdjustment("working_capital_worsening", -5, "lower", "운전자본 급증은 EPC/건설 hard 4C 후보 신호다."),
    Round253ScoreAdjustment("safety_incident", -5, "lower", "안전사고는 R10 Green을 차단한다."),
    Round253ScoreAdjustment("fatality_recurrence", -5, "lower", "반복 사망사고는 벌금·면허 리스크를 만든다."),
    Round253ScoreAdjustment("building_material_demand_weakness", -4, "lower", "철근/건자재 수요 약화는 건자재 Green을 막는다."),
)

ROUND253_SHADOW_WEIGHT_ROWS: tuple[Round253ShadowWeightRow, ...] = (
    Round253ShadowWeightRow(E2RArchetype.OVERSEAS_EPC_MEGA_ORDER, 5, 5, 5, 5, 5, 3, 0, 0, 0, 3, -3, 5, 4, "Fadhili is Stage 2 and 4B-watch until margin and cash collection confirm."),
    Round253ShadowWeightRow(E2RArchetype.GAS_INFRA_DELIVERY_VALIDATION, 5, 5, 5, 5, 5, 4, 0, 0, 0, 3, -2, 4, 4, "Jafurah milestone is Stage 2 until Hyundai E&C package, margin and FCF confirm."),
    Round253ShadowWeightRow(E2RArchetype.AI_DATA_CENTER_REAL_ASSET, 3, 2, 3, 4, 4, 0, 5, 5, 0, 3, -5, 5, 4, "AI data center needs tenant, NOI/AFFO, power/water and permitting."),
    Round253ShadowWeightRow(E2RArchetype.HOUSING_POLICY_SUPPLY_EVENT, 2, 2, 3, 3, 3, 0, 0, 0, 4, 2, -5, 5, 4, "Housing policy is not Green before presales, margin, PF and FCF confirm."),
    Round253ShadowWeightRow(E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2, 0, 3, 5, "PF delinquency spike and liquidity support are hard 4C/crisis relief."),
    Round253ShadowWeightRow(E2RArchetype.CONSTRUCTION_SAFETY_REGULATORY_4C, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 3, 5, "Repeated fatal accidents create fine/license risk and block Green."),
    Round253ShadowWeightRow(E2RArchetype.BUILDING_MATERIALS_DEMAND_CYCLE, 2, 0, 4, 4, 4, 0, 0, 0, 3, 2, -4, 4, 4, "Rebar weakness needs demand, spread and margin stabilization."),
    Round253ShadowWeightRow(E2RArchetype.PORT_INFRA_DELIVERY, 5, 5, 5, 5, 5, 5, 0, 0, 0, 3, -2, 3, 4, "Grand Faw dock completion is Stage 2 but needs backlog, margin and cash collection."),
)

ROUND253_CASE_CANDIDATES: tuple[Round253CaseCandidate, ...] = (
    Round253CaseCandidate(
        case_id="r10_loop11_samsung_ea_fadhili_epc_4b",
        symbol="028050",
        company_name="Samsung E&A",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_MEGA_ORDER,
        secondary_archetypes=(E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_4b_watch",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 3),
        stage3_date=None,
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        stage3_decision="mega_epc_contract_is_stage2_until_progress_revenue_opm_working_capital_and_cash_collection_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("signed_contract_6bn_usd", "total_fadhili_package_7_7bn_usd", "capacity_increase_60pct", "completion_expected_2027_11", "event_mfe_8_5pct"),
        red_flag_fields=("contract_headline_only", "EPC_margin_unverified", "working_capital_unverified", "cash_collection_unverified"),
        price_data_source="WSJ/Reuters contract and event-return anchors",
        reported_price_anchor="26,750 KRW after +8.5% intraday move",
        reported_return_anchor="$6B Samsung E&A contract; $7.7B Fadhili package; KOSPI -1.4%",
        mfe_1d=8.5,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=26750.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=26750.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"implied_prior_price_krw": 24654.0, "kospi_same_context_pct": -1.4, "relative_outperformance_pp": 9.9, "contract_value_usd_bn": 6.0, "total_fadhili_package_usd_bn": 7.7, "contract_share_of_total_pct": 77.9, "capacity_before_bcf_d": 2.5, "capacity_after_bcf_d": 4.0, "capacity_increase_pct": 60.0, "target_price_krw": 35000.0, "target_upside_from_event_price_pct": 30.8},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="success_candidate_event_premium",
        rerating_result="event_premium",
        round_rerating_result="overseas_EPC_mega_order_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_contract_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Mega EPC contract is Stage 2 and 4B-watch; margin, progress revenue and cash collection are required before Green.",
    ),
    Round253CaseCandidate(
        case_id="r10_loop11_hyundai_enc_jafurah_gas_infra",
        symbol="000720",
        company_name="Hyundai E&C",
        primary_archetype=E2RArchetype.GAS_INFRA_DELIVERY_VALIDATION,
        secondary_archetypes=(E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA,),
        case_type="success_candidate",
        round_case_type="success_candidate_gas_infra_delivery_watch",
        stage1_date=date(2024, 6, 30),
        stage2_date=date(2024, 6, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="gas_infra_project_milestone_is_stage2_until_company_package_margin_and_cashflow_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("aramco_contract_package_over_25bn_usd", "jafurah_reserves_229tcf", "first_phase_output_450mcf_d", "main_gas_network_4000km", "capacity_boost_3_2bcf_d"),
        red_flag_fields=("company_package_unverified", "EPC_margin_unverified", "cashflow_unverified", "Saudi_payment_risk"),
        price_data_source="Reuters Aramco/Jafurah project anchors",
        reported_price_anchor="Hyundai E&C stock OHLC unavailable after deep search",
        reported_return_anchor="Aramco >$25B package; Jafurah first phase 450M cf/d; network +4,000km",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"aramco_contract_package_usd_bn": 25.0, "jafurah_project_value_usd_bn": 100.0, "jafurah_raw_gas_reserves_tcf": 229.0, "jafurah_condensate_billion_barrels": 75.0, "target_sales_gas_2030_bcf_d": 2.0, "first_phase_output_mcf_d": 450.0, "first_phase_vs_2030_target_pct": 22.5, "main_gas_network_addition_km": 4000.0, "main_gas_network_capacity_boost_bcf_d": 3.2, "stage2_validation_date": "2025-12-02"},
        score_price_alignment="unknown",
        round_score_price_alignment="success_candidate",
        rerating_result="unknown",
        round_rerating_result="gas_infra_EPC_delivery_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_project_milestone_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Jafurah is gas-infra Stage 2; Hyundai E&C package, margin and cashflow are required before Green.",
    ),
    Round253CaseCandidate(
        case_id="r10_loop11_ai_data_center_real_asset",
        symbol="SK_group/Samsung_SDS/SK_Telecom/Samsung_CT/Samsung_Heavy",
        company_name="SK/AWS·OpenAI·Samsung data-center real asset basket",
        primary_archetype=E2RArchetype.AI_DATA_CENTER_REAL_ASSET,
        secondary_archetypes=(E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_event_premium",
        stage1_date=date(2025, 6, 20),
        stage2_date=date(2025, 10, 1),
        stage3_date=None,
        stage4b_date=date(2025, 6, 20),
        stage4c_date=None,
        stage3_decision="AI_data_center_headline_is_stage2_until_tenant_noi_affo_power_water_permitting_and_capex_per_share_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("sk_aws_7tn_krw", "aws_component_4bn_usd", "initial_capacity_100mw", "potential_expansion_1gw", "openai_samsung_sk_20mw", "floating_data_center_partners"),
        red_flag_fields=("data_center_theme_without_tenant", "NOI_AFFO_unverified", "power_water_permitting_unverified", "capex_per_share_unverified"),
        price_data_source="Reuters/AP data-center investment and partnership anchors",
        reported_price_anchor="Construction-related stock OHLC unavailable after deep search",
        reported_return_anchor="7T KRW / $5.11B Ulsan AI data center; 100MW initial, possible 1GW; OpenAI Korea initial 20MW",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"sk_aws_investment_krw_trn": 7.0, "sk_aws_investment_usd_bn": 5.11, "aws_component_usd_bn": 4.0, "initial_capacity_mw": 100.0, "potential_expansion_gw": 1.0, "capacity_expansion_multiple": 10.0, "full_operation_target_year": 2029.0, "openai_samsung_sk_initial_capacity_mw": 20.0, "construction_start_target": "2026-03", "floating_data_center_partners": ["Samsung C&T", "Samsung Heavy", "OpenAI"]},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="success_candidate_event_premium",
        rerating_result="event_premium",
        round_rerating_result="AI_data_center_real_asset_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_headline_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="AI data-center real asset is Stage 2; tenant, NOI/AFFO, power/water/permitting and capex per share are required.",
    ),
    Round253CaseCandidate(
        case_id="r10_loop11_seoul_housing_policy_supply_watch",
        symbol="housing_construction_basket",
        company_name="Seoul housing policy / construction basket",
        primary_archetype=E2RArchetype.HOUSING_POLICY_SUPPLY_EVENT,
        secondary_archetypes=(E2RArchetype.PRICE_ONLY_POLICY_RALLY, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_policy_watch",
        stage1_date=date(2025, 9, 7),
        stage2_date=date(2025, 9, 7),
        stage3_date=None,
        stage4b_date=date(2025, 9, 7),
        stage4c_date=None,
        stage3_decision="housing_policy_is_stage1_2_until_presales_margin_pf_stability_land_cost_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ltv_50_to_40pct", "state_owned_land_development", "reconstruction_rule_simplification", "affordable_housing_supply_expansion"),
        red_flag_fields=("policy_supply_headline_only", "LTV_tightening_demand_shock", "presales_unverified", "PF_stability_unverified", "FCF_unverified"),
        price_data_source="Reuters housing-policy evidence",
        reported_price_anchor="Housing basket OHLC unavailable after deep search",
        reported_return_anchor="LTV in Gangnam/Yongsan reduced from 50% to 40%; supply/reconstruction support",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ltv_before_pct": 50.0, "ltv_after_pct": 40.0, "ltv_reduction_pp": -10.0, "ltv_reduction_relative_pct": -20.0, "affected_districts": ["Gangnam", "Yongsan"], "policy_mix": "demand_control_plus_supply_support"},
        score_price_alignment="price_moved_without_evidence",
        round_score_price_alignment="event_premium_policy_watch",
        rerating_result="policy_event_rerating",
        round_rerating_result="housing_supply_policy_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_type="stage1_or_stage2_attention_only",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Housing policy is event premium; presales, margin, PF stability, land cost and FCF are required before Green.",
    ),
    Round253CaseCandidate(
        case_id="r10_loop11_pf_credit_break_taeyoung_basket",
        symbol="009410/construction_PF_basket",
        company_name="Taeyoung / construction PF stress basket",
        primary_archetype=E2RArchetype.REAL_ESTATE_PF_CREDIT_BREAK,
        secondary_archetypes=(E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT, E2RArchetype.PF_CREDIT_REDTEAM_OVERLAY),
        case_type="4c_thesis_break",
        round_case_type="hard_4c_pf_credit_break",
        stage1_date=date(2023, 12, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 5, 13),
        stage3_decision="PF_debt_reschedule_liquidity_support_and_delinquency_spike_are_hard_4c_not_green",
        stage4b_status="hard_4c",
        hard_4c_confirmed=True,
        evidence_fields=("government_support_40_6tn_krw", "PF_delinquency_0_37_to_2_70pct", "syndicated_loan_1tn_expandable_5tn", "project_assessment_tightened"),
        red_flag_fields=("PF_workout_or_debt_restructuring", "PF_delinquency_spike", "PF_relief_policy_only", "liquidity_crisis"),
        price_data_source="Reuters PF stress/policy-support anchors",
        reported_price_anchor="Taeyoung stock OHLC unavailable after deep search",
        reported_return_anchor="PF delinquency 0.37% to 2.70%; +629.7%; 40.6T KRW support; 1T loan expandable to 5T",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"government_support_package_krw_trn": 40.6, "pf_delinquency_2021_pct": 0.37, "pf_delinquency_2022_pct": 1.19, "pf_delinquency_2023_pct": 2.70, "pf_delinquency_increase_2021_to_2023_pp": 2.33, "pf_delinquency_increase_2021_to_2023_pct": 629.7, "pf_delinquency_increase_2022_to_2023_pct": 126.9, "syndicated_loan_initial_krw_trn": 1.0, "syndicated_loan_max_krw_trn": 5.0, "loan_expandability_multiple": 5.0},
        score_price_alignment="false_positive_score",
        round_score_price_alignment="thesis_break",
        rerating_result="thesis_break",
        round_rerating_result="PF_credit_break",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="hard_4C",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="PF delinquency spike and liquidity support are hard 4C/crisis relief, not Green.",
    ),
    Round253CaseCandidate(
        case_id="r10_loop11_posco_dl_construction_safety_regulation",
        symbol="POSCO_EC/DL_Construction_exposure",
        company_name="POSCO E&C / DL Construction safety regulation basket",
        primary_archetype=E2RArchetype.CONSTRUCTION_SAFETY_REGULATORY_4C,
        secondary_archetypes=(E2RArchetype.WORKPLACE_FATALITY_REGULATORY_4C, E2RArchetype.OPERATIONAL_TRUST_HARD_4C),
        case_type="failed_rerating",
        round_case_type="4c_watch_operating_license_risk",
        stage1_date=date(2025, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 15),
        stage3_decision="construction_safety_regulation_is_4c_watch_and_green_blocker_until_remediation_and_license_risk_clear",
        stage4b_status="4c_watch",
        hard_4c_confirmed=False,
        evidence_fields=("posco_ec_sites_halted_103", "dl_construction_execs_resigned_80", "fine_up_to_5pct_op", "license_revocation_risk", "construction_death_rate_15_9_per_100k"),
        red_flag_fields=("safety_incident", "fatality_recurrence", "repeated_site_shutdown", "license_revocation_risk", "fine_up_to_5pct_operating_profit"),
        price_data_source="Reuters safety-regulation / operational evidence anchors",
        reported_price_anchor="Direct listed event OHLC unavailable after deep search",
        reported_return_anchor="103 sites halted; about 80 executives resigned; recurring fatality firms may face fines up to 5% of OP",
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
        round_rerating_result="operational_safety_redteam",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="4C_watch_not_company_hard_4C_yet",
        price_validation_status="direct_listed_event_ohlc_unavailable",
        notes="Safety regulation is 4C-watch; repeated fatalities become hard 4C if fines, license risk or site shutdown materially impair business.",
    ),
    Round253CaseCandidate(
        case_id="r10_loop11_hyundai_steel_rebar_construction_demand_watch",
        symbol="004020",
        company_name="Hyundai Steel / rebar construction demand proxy",
        primary_archetype=E2RArchetype.BUILDING_MATERIALS_DEMAND_CYCLE,
        secondary_archetypes=(E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_UNPROVEN,),
        case_type="failed_rerating",
        round_case_type="4c_watch_building_material_demand_cycle",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 6, 21),
        stage3_decision="rebar_price_decline_and_profit_estimate_cut_block_building_material_green",
        stage4b_status="4c_watch",
        hard_4c_confirmed=False,
        evidence_fields=("event_price_29000_krw", "event_mae_minus_1_2pct", "target_cut_14pct", "net_profit_forecast_cut_73pct", "rebar_price_expected_decline_10pct"),
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
        score_price_alignment="evidence_good_but_price_failed",
        round_score_price_alignment="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_result="building_materials_demand_cycle_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_type="should_have_been_yellow_or_red",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Rebar and construction-demand weakness block building-material Green until demand, spread and margin stabilize.",
    ),
    Round253CaseCandidate(
        case_id="r10_loop11_daewoo_enc_grand_faw_port_delivery",
        symbol="047040",
        company_name="Daewoo E&C",
        primary_archetype=E2RArchetype.PORT_INFRA_DELIVERY,
        secondary_archetypes=(E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_UNPROVEN,),
        case_type="success_candidate",
        round_case_type="success_candidate_infrastructure_delivery",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 11, 12),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="dock_completion_is_stage2_until_additional_epc_backlog_margin_and_cash_collection_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("five_docks_completed", "operation_start_2026", "capacity_3_5m_containers_by_2028", "development_road_17bn_usd"),
        red_flag_fields=("additional_backlog_unverified", "margin_unverified", "cash_collection_unverified", "Iraq_payment_or_security_risk"),
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
        round_rerating_result="port_infrastructure_delivery_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_type="stage2_delivery_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Dock completion is stronger than a mere order headline, but additional backlog, margin and cash collection are required before Stage 3.",
    ),
)


def round253_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND253_CASE_CANDIDATES:
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
                "Round253 R10 Loop-11 construction/real-estate/materials "
                "price-path validation case. Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(field for field in candidate.evidence_fields if "policy" in field or "contract" in field or "center" in field or "PF" in field),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if "margin" in field or "cash" in field or "NOI" in field or "AFFO" in field),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "event" in field or "headline" in field or "policy" in field or "contract" in field),
            stage4c_evidence=tuple(field for field in candidate.red_flag_fields if "PF" in field or "safety" in field or "fatality" in field or "shutdown" in field or "demand" in field or "tenant" in field or "working_capital" in field),
            must_have_fields=ROUND253_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "failed_rerating", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND253_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_contract_policy_data_center_pf_relief_or_safety_headline_as_green",
                *ROUND253_GREEN_REQUIRED_FIELDS,
                *ROUND253_GREEN_FORBIDDEN_PATTERNS,
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


def round253_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND253_CASE_CANDIDATES:
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
                "round_rerating_result": candidate.round_rerating_result,
                "stage_failure_type": candidate.stage_failure_type,
                "round_stage_failure_type": candidate.round_stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round253_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND253_SCORE_ADJUSTMENTS)


def round253_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND253_SHADOW_WEIGHT_ROWS)


def round253_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round253_price_validation": "true"} for field in ROUND253_PRICE_VALIDATION_FIELDS)


def round253_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round253_label": label, "canonical_archetype": canonical} for label, canonical in ROUND253_REQUIRED_TARGET_ALIASES.items())


def round253_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple({"deep_sub_archetype": item, "source_round": ROUND253_SOURCE_ROUND_PATH} for item in ROUND253_DEEP_SUB_ARCHETYPES)


def round253_summary() -> dict[str, int | bool | str]:
    cases = ROUND253_CASE_CANDIDATES
    return {
        "source_round": ROUND253_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND253_ANALYST_ROUND_ID,
        "large_sector": ROUND253_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "thesis_break_watch_count": sum(1 for case in cases if case.round_score_price_alignment == "thesis_break_watch"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "target_archetype_count": len(ROUND253_REQUIRED_TARGET_ALIASES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round253_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND253_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND253_ANALYST_ROUND_ID,
        "large_sector": ROUND253_LARGE_SECTOR,
        "summary": round253_summary(),
        "target_aliases": dict(ROUND253_REQUIRED_TARGET_ALIASES),
        "round_case_types": {case.case_id: case.round_case_type for case in ROUND253_CASE_CANDIDATES},
        "green_required_fields": list(ROUND253_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND253_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND253_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND253_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_use_round253_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_contract_policy_data_center_pf_relief_or_safety_headline_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "keep_pf_credit_break_as_hard_4c_reference",
            "keep_safety_regulation_as_4c_watch_until_fines_license_or_site_shutdown_impair_business",
        ],
    }


def render_round253_summary_markdown() -> str:
    summary = round253_summary()
    lines = [
        "# Round 253 R10 Loop 11 Construction Real Estate Materials Price Validation",
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
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- full_adjusted_ohlc_complete: {str(summary['full_adjusted_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round_type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND253_CASE_CANDIDATES:
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
            "- Samsung E&A Fadhili and Hyundai E&C Jafurah are Stage 2, not automatic Green.",
            "- AI data-center real asset and Seoul housing policy remain event/policy watch until cash-flow evidence appears.",
            "- PF credit break is confirmed hard 4C; safety regulation is 4C-watch until business impairment is confirmed.",
            "- Hyundai Steel rebar weakness is a demand-cycle Green blocker.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round253_green_gate_review_markdown() -> str:
    lines = [
        "# Round 253 R10 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND253_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND253_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `signed contract` is Stage 2.",
            "- `signed contract + progress revenue + margin + working-capital control + cash collection` can support Stage 3 review.",
            "- `PF delinquency spike` is hard 4C. It is not a rerating source.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round253_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 253 R10 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND253_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND253_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND253_CASE_CANDIDATES:
        if case.stage4b_status in {"watch", "hard_4c"} or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round253_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 253 R10 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- hard_4c_confirmed: true",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND253_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def render_round253_deep_sub_archetypes_markdown() -> str:
    lines = ["# Round 253 R10 Deep Sub-Archetypes", ""]
    lines.extend(f"- {item}" for item in ROUND253_DEEP_SUB_ARCHETYPES)
    return "\n".join(lines) + "\n"


def write_round253_r10_loop11_reports(
    output_directory: str | Path = ROUND253_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND253_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND253_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)

    paths = {
        "cases": write_case_library(round253_case_records(), cases_path),
        "audit": _write_json(round253_audit_payload(), audit_path),
        "summary": output / "round253_r10_loop11_price_validation_summary.md",
        "case_matrix": output / "round253_r10_loop11_case_matrix.csv",
        "target_aliases": output / "round253_r10_loop11_target_aliases.csv",
        "deep_sub_archetypes": output / "round253_r10_loop11_deep_sub_archetypes.csv",
        "score_adjustments": output / "round253_r10_loop11_score_adjustments.csv",
        "shadow_weights": output / "round253_r10_loop11_shadow_weights.csv",
        "price_validation_fields": output / "round253_r10_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round253_r10_loop11_green_gate_review.md",
        "price_validation_plan": output / "round253_r10_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round253_r10_loop11_stage4b_4c_review.md",
        "deep_sub_archetype_notes": output / "round253_r10_loop11_deep_sub_archetypes.md",
    }
    paths["summary"].write_text(render_round253_summary_markdown(), encoding="utf-8")
    _write_csv(round253_case_rows(), paths["case_matrix"])
    _write_csv(round253_target_alias_rows(), paths["target_aliases"])
    _write_csv(round253_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round253_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round253_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round253_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round253_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round253_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round253_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["deep_sub_archetype_notes"].write_text(render_round253_deep_sub_archetypes_markdown(), encoding="utf-8")
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
