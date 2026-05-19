"""Round-227 R10 Loop-9 construction/real-estate/materials validation pack.

Round 227 converts ``docs/round/round_227.md`` into a calibration-only case
pack. It is intentionally not a production scoring change.

Easy example: ``Samsung E&A wins a large Saudi EPC contract and the stock
jumps`` can be Stage 2 plus 4B-watch. It is not Stage 3-Green until EPC margin,
progress revenue, cash collection, and working-capital control are visible as
of the case date.
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


ROUND227_SOURCE_ROUND_PATH = "docs/round/round_227.md"
ROUND227_LARGE_SECTOR = Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS
ROUND227_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round227_r10_loop9_construction_real_estate_materials_price_validation"
ROUND227_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop9_round227.jsonl"
ROUND227_DEFAULT_AUDIT_PATH = (
    "data/sector_taxonomy/round227_r10_loop9_construction_real_estate_materials_price_validation_audit.json"
)

ROUND227_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "OVERSEAS_EPC_CONTRACT_BACKLOG": E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA.value,
    "EPC_LOW_MARGIN_ORDER_OVERLAY": E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY.value,
    "SAUDI_GAS_INFRA_BACKLOG": E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA.value,
    "PF_CREDIT_REDTEAM_OVERLAY": E2RArchetype.PF_CREDIT_REDTEAM_OVERLAY.value,
    "HOUSING_POLICY_SUPPLY_EVENT": E2RArchetype.POLICY_LOCAL_REAL_ESTATE_THEME.value,
    "SEOUL_RECONSTRUCTION_POLICY_EVENT": E2RArchetype.RESIDENTIAL_HOUSING_CYCLE.value,
    "CONSTRUCTION_SAFETY_OPERATIONAL_TRUST_4C": E2RArchetype.OPERATIONAL_TRUST_HARD_4C.value,
    "WORKPLACE_FATALITY_REGULATORY_4C": E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY.value,
    "AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT": E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT.value,
    "FLOATING_DATA_CENTER_CONSTRUCTION_EVENT": E2RArchetype.AI_INFRA_REAL_ASSET_THEME_OVERLAY.value,
    "BUILDING_MATERIALS_DEMAND_CYCLE": E2RArchetype.BUILDING_MATERIALS_CYCLE.value,
    "REBAR_CONSTRUCTION_DEMAND_4C_WATCH": E2RArchetype.BUILDING_MATERIALS_VOLUME_FAILURE.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
}

ROUND227_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "company_level_order_or_lease_confirmed",
    "margin_or_noi_affo_confirmed",
    "cash_flow_after_working_capital_confirmed",
    "pf_and_funding_cost_risk_passed",
    "project_progress_or_cost_ratio_stable",
    "tenant_occupancy_or_utilization_confirmed",
    "capex_per_share_or_dilution_passed",
    "safety_quality_trust_passed",
    "price_path_after_evidence",
)

ROUND227_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "contract_headline_only",
    "pf_relief_policy_only",
    "housing_supply_policy_only",
    "real_estate_rebound_theme_only",
    "data_center_theme_without_tenant",
    "asset_headline_without_noi_affo",
    "epc_backlog_without_margin",
    "low_margin_order_risk",
    "capex_per_share_dilution",
    "quality_safety_incident",
    "workplace_fatality_repeated",
    "building_material_demand_weakness",
)

ROUND227_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "large_overseas_epc_award_day_rally",
    "pf_support_policy_relief_rally",
    "housing_supply_policy_rally",
    "reconstruction_policy_event_rally",
    "data_center_theme_basket_rally",
    "reit_rate_cut_expectation_rally",
    "disaster_rebuild_or_reconstruction_price_first_move",
)

ROUND227_HARD_4C_GATES: tuple[str, ...] = (
    "pf_workout_or_debt_reschedule",
    "pf_delinquency_spike",
    "unsold_inventory_or_presale_failure",
    "construction_cost_ratio_spike",
    "working_capital_deterioration",
    "order_cancellation_or_client_payment_delay",
    "low_margin_epc_loss_recognition",
    "apartment_or_bridge_collapse",
    "repeated_workplace_fatality_or_site_shutdown",
    "license_suspension_or_cancellation_risk",
    "tenant_absent_or_no_binding_lease",
    "power_water_or_permitting_failure",
    "affo_integrity_break",
    "capex_dilution",
    "building_material_demand_collapse",
)

ROUND227_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "relative_outperformance_pp",
    "contract_or_policy_anchor",
    "pf_credit_anchor",
    "safety_anchor",
    "tenant_noi_affo_anchor",
    "building_material_demand_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round227ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round227ShadowWeightRow:
    archetype: E2RArchetype
    cash_flow_after_wc: int
    epc_margin: int
    project_cost_control: int
    progress_revenue: int
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
            "pf_cleanup": _signed(self.pf_cleanup),
            "funding_cost": _signed(self.funding_cost),
            "tenant_noi_affo": _signed(self.tenant_noi_affo),
            "safety_trust": _signed(self.safety_trust),
            "event_penalty": _signed(self.event_penalty),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round227CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
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
    extra_price_metrics: Mapping[str, float | str | bool]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND227_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND227_SCORE_ADJUSTMENTS: tuple[Round227ScoreAdjustment, ...] = (
    Round227ScoreAdjustment("cash_flow_after_working_capital", 5, "raise", "R10은 수주가 현금회수와 working capital 이후 FCF로 닫혀야 한다."),
    Round227ScoreAdjustment("epc_margin_visibility", 5, "raise", "대형 EPC는 계약금액보다 마진과 공정률 가시성이 중요하다."),
    Round227ScoreAdjustment("project_cost_control", 5, "raise", "원가율 통제 없이는 수주잔고가 오히려 손실 리스크가 된다."),
    Round227ScoreAdjustment("progress_revenue_visibility", 4, "raise", "공정률 매출과 인도 milestone은 headline보다 강한 증거다."),
    Round227ScoreAdjustment("handover_milestone", 4, "raise", "완공/인도 확인은 Stage 2에서 Stage 3로 넘어가기 전 필수 확인축이다."),
    Round227ScoreAdjustment("pf_credit_cleanup", 5, "raise", "PF 부실 정리와 우량 프로젝트 분리가 확인될 때만 credit relief를 인정한다."),
    Round227ScoreAdjustment("funding_cost_control", 5, "raise", "건설·부동산은 조달비용이 FCF와 배당 커버리지를 결정한다."),
    Round227ScoreAdjustment("tenant_contract_quality", 5, "raise", "데이터센터는 임차계약이 있어야 현금흐름 후보가 된다."),
    Round227ScoreAdjustment("noi_affo_visibility", 5, "raise", "자산 headline이 아니라 NOI/AFFO와 주당 현금흐름을 본다."),
    Round227ScoreAdjustment("power_water_permitting_secured", 4, "raise", "AI 데이터센터는 전력·물·인허가가 병목이다."),
    Round227ScoreAdjustment("safety_quality_trust", 5, "raise", "건설 안전·품질 신뢰는 Green의 전제 조건이다."),
    Round227ScoreAdjustment("contract_headline_only", -5, "lower", "수주 headline만으로 Stage 3-Green을 만들지 않는다."),
    Round227ScoreAdjustment("pf_relief_policy_only", -5, "lower", "PF 지원책은 relief이지 체급 변화 증거가 아니다."),
    Round227ScoreAdjustment("housing_supply_policy_only", -4, "lower", "공급정책만으로 분양률·마진·FCF를 알 수 없다."),
    Round227ScoreAdjustment("data_center_theme_without_tenant", -5, "lower", "임차인 없는 데이터센터 테마는 price-only rally가 되기 쉽다."),
    Round227ScoreAdjustment("asset_headline_without_noi_affo", -5, "lower", "자산 보유 headline은 NOI/AFFO 전까지 제한한다."),
    Round227ScoreAdjustment("epc_backlog_without_margin", -5, "lower", "수주잔고가 많아도 저마진이면 Stage 3가 아니다."),
    Round227ScoreAdjustment("low_margin_order_risk", -4, "lower", "저마진 EPC는 현금흐름 부담으로 바뀔 수 있다."),
    Round227ScoreAdjustment("capex_per_share_dilution", -4, "lower", "CAPEX가 주당 현금흐름을 희석하면 Green을 막는다."),
    Round227ScoreAdjustment("quality_safety_incident", -5, "lower", "붕괴·품질사고는 hard RedTeam 입력이다."),
    Round227ScoreAdjustment("workplace_fatality_repeated", -5, "lower", "반복 사망사고와 현장중단은 operational trust 4C gate다."),
    Round227ScoreAdjustment("building_material_demand_weakness", -4, "lower", "철근·건자재 수요 약화는 margin과 EPS를 동시에 깎을 수 있다."),
)


ROUND227_SHADOW_WEIGHT_ROWS: tuple[Round227ShadowWeightRow, ...] = (
    Round227ShadowWeightRow(E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA, 5, 5, 5, 4, 0, 3, 0, 2, -3, 4, "Large EPC is Stage 2; Stage 3 requires margin, progress revenue, and cash collection."),
    Round227ShadowWeightRow(E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY, 5, 5, 5, 4, 0, 3, 0, 2, -4, 5, "Low-margin orders are a cap unless cost control and working capital are proven."),
    Round227ShadowWeightRow(E2RArchetype.PF_CREDIT_REDTEAM_OVERLAY, 5, 0, 0, 0, 5, 5, 0, 2, -5, 5, "PF delinquency spike and debt reschedule are hard 4C inputs."),
    Round227ShadowWeightRow(E2RArchetype.POLICY_LOCAL_REAL_ESTATE_THEME, 3, 2, 3, 2, 4, 4, 0, 2, -5, 4, "Housing policy is Stage 1/2 until presales, margin, PF, and FCF confirm."),
    Round227ShadowWeightRow(E2RArchetype.OPERATIONAL_TRUST_HARD_4C, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, "Bridge collapse and direct fatal safety events block Green."),
    Round227ShadowWeightRow(E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY, 0, 0, 0, 0, 0, 0, 0, 5, 0, 5, "Recurring fatal accidents create fine/license/site shutdown risk."),
    Round227ShadowWeightRow(E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT, 4, 0, 4, 2, 0, 5, 5, 3, -5, 4, "Data-center real asset needs tenant, NOI/AFFO, power/water, and capex per share."),
    Round227ShadowWeightRow(E2RArchetype.BUILDING_MATERIALS_CYCLE, 4, 4, 3, 0, 3, 4, 0, 2, -4, 4, "Building-material demand weakness blocks Green until demand and margin stabilize."),
)


ROUND227_CASE_CANDIDATES: tuple[Round227CaseCandidate, ...] = (
    Round227CaseCandidate(
        case_id="r10_loop9_samsung_ea_gs_fadhili_epc",
        symbol="028050/006360",
        company_name="삼성E&A / GS건설",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA,
        secondary_archetypes=(E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 3),
        stage3_date=None,
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        stage3_decision="epc_award_is_stage2_until_margin_progress_revenue_cash_collection_and_working_capital_are_visible",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("fadhili_epc_7_7bn_usd", "samsung_ea_contract_about_6bn_usd", "samsung_ea_event_mfe_8_5pct", "relative_outperformance_9_9pp", "capacity_increase_60pct", "completion_2027_11"),
        red_flag_fields=("contract_headline_only", "epc_backlog_without_margin", "low_margin_order_risk", "working_capital_unverified", "cash_collection_unverified"),
        price_data_source="WSJ/Reuters reported contract and price anchors",
        reported_price_anchor="Samsung E&A 26,750 KRW and +8.5% event move",
        reported_return_anchor="KOSPI same context -1.4%; relative outperformance +9.9pp",
        mfe_1d=8.5,
        mae_1d=None,
        stage2_price_anchor=26750.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=26750.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"implied_pre_event_reference_price": 24654.0, "kospi_same_context_pct": -1.4, "relative_outperformance_pp": 9.9, "aramco_total_fadhili_contracts_usd_bn": 7.7, "samsung_ea_contract_estimate_usd_bn": 6.0, "samsung_share_of_total_project_pct": 77.9, "capacity_increase_pct": 60.0, "kb_target_price": 35000.0, "target_upside_from_event_peak_pct": 30.8},
        score_price_alignment="aligned",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="대형 Fadhili EPC는 Stage 2 후보지만, 마진·공정률·현금회수·working capital 확인 전 Stage 3-Green은 금지한다.",
    ),
    Round227CaseCandidate(
        case_id="r10_loop9_hyundai_ec_jafurah_gas_infra",
        symbol="000720",
        company_name="현대건설",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA,
        secondary_archetypes=(E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY,),
        case_type="success_candidate",
        stage1_date=date(2024, 6, 1),
        stage2_date=date(2024, 6, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="sovereign_gas_infra_backlog_is_stage2_until_margin_progress_revenue_and_cash_recovery_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("aramco_contract_package_above_25bn_usd", "jafurah_reserves_229tcf", "main_gas_network_4000km", "added_capacity_3_2bscfd", "target_2030_vs_first_phase_344_4pct"),
        red_flag_fields=("price_anchor_unavailable", "epc_margin_unverified", "project_delay_watch", "cost_overrun_watch", "client_payment_delay_watch"),
        price_data_source="Reuters contract/infrastructure evidence",
        reported_price_anchor="Hyundai E&C event-day OHLC unavailable after deep search",
        reported_return_anchor="Aramco >$25B Jafurah/main gas package; network +4,000km and +3.2B scf/day",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"aramco_contract_package_usd_bn": 25.0, "jafurah_reserves_tcf": 229.0, "jafurah_condensates_bbl_bn": 75.0, "jafurah_sales_gas_target_bscfd": 2.0, "main_gas_network_added_capacity_bscfd": 3.2, "main_gas_network_added_pipeline_km": 4000.0, "jafurah_first_phase_output_mmcfd": 450.0, "target_2030_vs_first_phase_pct": 344.4},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="사우디 가스 인프라 수주는 Stage 2 후보지만 회사별 주가 앵커와 마진·현금회수가 아직 없다.",
    ),
    Round227CaseCandidate(
        case_id="r10_loop9_taeyoung_pf_credit_hard_4c",
        symbol="009410/PF_basket",
        company_name="태영건설 / 건설 PF stress",
        primary_archetype=E2RArchetype.PF_CREDIT_REDTEAM_OVERLAY,
        secondary_archetypes=(E2RArchetype.PF_RESTRUCTURING_RELIEF, E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA),
        case_type="4c_thesis_break",
        stage1_date=date(2023, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2023, 12, 1),
        stage3_decision="pf_workout_and_liquidity_support_are_redteam_relief_not_positive_green_evidence",
        stage4b_status="not_applicable",
        hard_4c_confirmed=True,
        evidence_fields=("government_support_package_40_6tn_krw", "pf_delinquency_0_37_to_2_70pct", "syndicated_loan_1tn_to_5tn"),
        red_flag_fields=("pf_workout_or_debt_reschedule", "pf_delinquency_spike", "liquidity_stress", "credit_contagion", "support_is_relief_not_green"),
        price_data_source="Reuters PF stress/policy-support anchors",
        reported_price_anchor="Taeyoung event-day stock OHLC unavailable after deep search",
        reported_return_anchor="PF delinquency 0.37% to 2.70%; support package 40.6T KRW",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"government_support_package_krw_tn": 40.6, "pf_delinquency_2021_pct": 0.37, "pf_delinquency_2022_pct": 1.19, "pf_delinquency_2023_pct": 2.7, "pf_delinquency_increase_2021_to_2023_pp": 2.33, "pf_delinquency_increase_2021_to_2023_pct": 629.7, "pf_delinquency_increase_2022_to_2023_pct": 126.9, "syndicated_loan_initial_krw_tn": 1.0, "syndicated_loan_max_krw_tn": 5.0, "loan_expandability_multiple": 5.0},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="PF 채무재조정과 연체율 급등은 hard 4C다. 정책지원은 Green 증거가 아니라 RedTeam relief다.",
    ),
    Round227CaseCandidate(
        case_id="r10_loop9_seoul_housing_supply_policy_watch",
        symbol="housing_construction_basket",
        company_name="서울 주택공급 / 재건축 정책 basket",
        primary_archetype=E2RArchetype.POLICY_LOCAL_REAL_ESTATE_THEME,
        secondary_archetypes=(E2RArchetype.RESIDENTIAL_HOUSING_CYCLE, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        stage1_date=date(2024, 8, 16),
        stage2_date=date(2025, 9, 7),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="housing_supply_policy_is_stage1_or_stage2_until_presales_margin_pf_stability_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("seoul_home_price_monthly_plus_0_76pct", "planned_new_homes_above_400k", "ltv_50_to_40pct", "reconstruction_rule_simplification"),
        red_flag_fields=("housing_supply_policy_only", "presales_unverified", "cost_ratio_unverified", "pf_stability_unverified", "ltv_tightening_demand_shock_watch"),
        price_data_source="Reuters housing-policy and property-price evidence",
        reported_price_anchor="Construction basket OHLC unavailable after deep search",
        reported_return_anchor="Seoul home prices +0.76% monthly; LTV 50% to 40%; supply >400k homes",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"seoul_home_price_monthly_change_pct": 0.76, "national_house_transaction_index_monthly_change_pct": 0.15, "planned_new_homes": 400000.0, "annualized_supply_target_homes": 66667.0, "ltv_before_pct": 50.0, "ltv_after_pct": 40.0, "ltv_reduction_pp": -10.0, "ltv_reduction_relative_pct": -20.0},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="policy_event_rerating",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="주택공급·재건축 정책은 관심 이벤트지만, 분양률·원가율·PF 안정·FCF 전에는 Green이 아니다.",
    ),
    Round227CaseCandidate(
        case_id="r10_loop9_hyundai_engineering_bridge_collapse_watch",
        symbol="unlisted_Hyundai_Engineering",
        company_name="현대엔지니어링 / 천안 교량 붕괴",
        primary_archetype=E2RArchetype.OPERATIONAL_TRUST_HARD_4C,
        secondary_archetypes=(E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY,),
        case_type="4c_thesis_break",
        stage1_date=date(2025, 2, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 2, 25),
        stage3_decision="fatal_bridge_collapse_is_redteam_safety_input_and_not_positive_stage_evidence",
        stage4b_status="not_applicable",
        hard_4c_confirmed=True,
        evidence_fields=("cheonan_bridge_collapse", "fatalities_4", "injuries_6", "workers_fell_10", "hyundai_engineering_site_charge"),
        red_flag_fields=("apartment_or_bridge_collapse", "fatal_safety_incident", "operational_trust_break", "direct_listed_vehicle_unclear"),
        price_data_source="Washington Post safety-event evidence",
        reported_price_anchor="Direct listed stock mapping unclear; OHLC unavailable",
        reported_return_anchor="4 killed, 6 injured, 10 workers fell",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fatalities": 4.0, "injuries": 6.0, "critical_injuries": 5.0, "workers_fell": 10.0, "listed_stock_mapping": "unclear_not_direct_listed_vehicle"},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="not_direct_listed_stock_price_unavailable",
        notes="직접 상장사는 아니지만 건설 안전 신뢰 4C 게이트를 검증하는 사례다.",
    ),
    Round227CaseCandidate(
        case_id="r10_loop9_posco_ec_dl_construction_safety_regulation",
        symbol="POSCO_EC/DL_Construction_exposure",
        company_name="POSCO E&C / DL Construction 안전 규제",
        primary_archetype=E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY,
        secondary_archetypes=(E2RArchetype.OPERATIONAL_TRUST_HARD_4C,),
        case_type="4c_thesis_break",
        stage1_date=date(2025, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 15),
        stage3_decision="repeated_fatal_accident_and_site_shutdown_are_operational_trust_4c_inputs",
        stage4b_status="not_applicable",
        hard_4c_confirmed=True,
        evidence_fields=("construction_death_rate_15_9_per_100k", "posco_ec_103_sites_halted", "dl_construction_80_execs_resigned", "fine_up_to_5pct_op", "license_revocation_risk"),
        red_flag_fields=("repeated_workplace_fatality_or_site_shutdown", "license_suspension_or_cancellation_risk", "quality_safety_incident", "operational_trust_break"),
        price_data_source="Reuters safety-regulation evidence anchors",
        reported_price_anchor="Direct listed event OHLC unavailable",
        reported_return_anchor="103 sites halted, about 80 executives resigned, fine up to 5% of operating profit",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"korea_industrial_death_rate_per_100k": 3.9, "oecd_average_death_rate_per_100k": 2.6, "relative_excess_vs_oecd_pct": 50.0, "korea_construction_death_rate_per_100k": 15.9, "workplace_deaths_2024": 589.0, "construction_share": "nearly_half", "posco_ec_sites_halted": 103.0, "dl_construction_executives_resigned": 80.0, "proposed_fine_pct_of_operating_profit": 5.0, "license_revocation_risk": True},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="direct_listed_event_ohlc_unavailable",
        notes="반복 사망사고·현장중단·벌금·면허 리스크는 R10에서 Green을 막는 operational trust 4C다.",
    ),
    Round227CaseCandidate(
        case_id="r10_loop9_ai_data_center_real_asset_event",
        symbol="SK_group/Samsung_SDS/SK_Telecom/Samsung_CT/Samsung_Heavy_related",
        company_name="SK/AWS·OpenAI·Samsung C&T 데이터센터",
        primary_archetype=E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT,
        secondary_archetypes=(E2RArchetype.AI_INFRA_REAL_ASSET_THEME_OVERLAY, E2RArchetype.DATA_CENTER_POWER_WATER_PERMITTING, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        stage1_date=date(2025, 6, 20),
        stage2_date=date(2025, 10, 1),
        stage3_date=None,
        stage4b_date=date(2025, 6, 20),
        stage4c_date=None,
        stage3_decision="data_center_real_asset_is_stage2_until_tenant_noi_affo_power_water_permitting_and_capex_per_share_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("sk_aws_investment_7tn_krw", "aws_component_4bn_usd", "initial_capacity_100mw", "potential_expansion_1gw", "kakao_event_mfe_11pct", "lg_cns_event_mfe_9pct", "openai_samsung_sk_initial_capacity_20mw"),
        red_flag_fields=("data_center_theme_without_tenant", "asset_headline_without_noi_affo", "power_water_permitting_unverified", "capex_per_share_dilution_watch", "tenant_contract_quality_unverified"),
        price_data_source="Reuters/AP investment and event-return anchors",
        reported_price_anchor="SK Hynix >+3%, Kakao +11%, LG CNS +9% reported event anchors",
        reported_return_anchor="SK/AWS 7T KRW; 100MW initial capacity; possible 1GW expansion",
        mfe_1d=11.0,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"sk_aws_investment_krw_tn": 7.0, "sk_aws_investment_usd_bn": 5.11, "aws_component_usd_bn": 4.0, "initial_capacity_mw": 100.0, "potential_expansion_gw": 1.0, "capacity_expansion_potential_multiple": 10.0, "construction_start_planned": "2025-09", "full_operation_planned_year": 2029.0, "openai_samsung_sk_initial_capacity_mw": 20.0, "sk_hynix_event_mfe_pct": 3.0, "kakao_event_mfe_pct": 11.0, "lg_cns_event_mfe_pct": 9.0, "floating_data_center_collaboration": True},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="데이터센터 real asset은 구조 후보지만 tenant, NOI/AFFO, 전력·물·인허가, capex per share 전에는 Stage 3가 아니다.",
    ),
    Round227CaseCandidate(
        case_id="r10_loop9_hyundai_steel_rebar_construction_demand_watch",
        symbol="004020",
        company_name="현대제철 / 철근·건자재 수요 proxy",
        primary_archetype=E2RArchetype.BUILDING_MATERIALS_CYCLE,
        secondary_archetypes=(E2RArchetype.BUILDING_MATERIALS_VOLUME_FAILURE,),
        case_type="4c_thesis_break",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 6, 21),
        stage3_decision="weak_construction_demand_and_rebar_price_decline_block_materials_green_until_demand_margin_stabilize",
        stage4b_status="not_applicable",
        hard_4c_confirmed=False,
        evidence_fields=("event_price_29000_krw", "event_mae_minus_1_2pct", "net_profit_forecast_cut_73pct", "rebar_price_expected_decline_10pct", "target_cut_14pct"),
        red_flag_fields=("building_material_demand_weakness", "rebar_price_decline", "net_profit_forecast_cut", "construction_demand_slowdown", "shipbuilding_steel_plate_competition_watch"),
        price_data_source="MarketWatch reported price/target/estimate anchor",
        reported_price_anchor="29,000 KRW and -1.2% event move",
        reported_return_anchor="2024 net profit forecast -73%; target price -14%; rebar price expected -10%",
        mfe_1d=None,
        mae_1d=-1.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=29000.0,
        extra_price_metrics={"event_price_anchor": 29000.0, "event_mae_pct": -1.2, "implied_pre_event_reference_price": 29352.0, "target_price": 30000.0, "target_cut_pct": -14.0, "implied_prior_target": 34884.0, "target_upside_from_event_price_pct": 3.45, "net_profit_forecast_2024_krw_bn": 215.0, "net_profit_forecast_cut_pct": -73.0, "implied_prior_net_profit_forecast_krw_bn": 796.3, "rebar_price_expected_decline_pct": -10.0},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="철근·건자재 수요 약화는 건설 cycle 4C-watch다. 수요·spread·margin 안정 전 Green은 막는다.",
    ),
)


def round227_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND227_CASE_CANDIDATES:
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
                "Round227 R10 Loop-9 construction/real-estate/materials price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "policy" in field or "price" in field or "contract" in field or "capacity" in field or "fatal" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "margin" in field or "cash" in field or "noi" in field or "affo" in field or "tenant" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "event" in field or "mfe" in field or "policy" in field or "headline" in field or "rally" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "pf" in field
                or "fatal" in field
                or "safety" in field
                or "collapse" in field
                or "license" in field
                or "demand" in field
                or "working_capital" in field
            ),
            must_have_fields=ROUND227_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND227_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_epc_pf_housing_or_data_center_headline_as_green_alone",
                *ROUND227_GREEN_REQUIRED_FIELDS,
                *ROUND227_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
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
                    or candidate.stage4c_price_anchor is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                ),
                stage_dates_confidence=0.8 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round227_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND227_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
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
                "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
                "score_price_alignment": candidate.score_price_alignment,
                "rerating_result": candidate.rerating_result,
                "stage_failure_type": candidate.stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round227_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND227_SCORE_ADJUSTMENTS)


def round227_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND227_SHADOW_WEIGHT_ROWS)


def round227_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round227_price_validation": "true"} for field in ROUND227_PRICE_VALIDATION_FIELDS)


def round227_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round227_label": label, "canonical_archetype": canonical} for label, canonical in ROUND227_REQUIRED_TARGET_ALIASES.items())


def round227_summary() -> dict[str, int | bool | str]:
    cases = ROUND227_CASE_CANDIDATES
    return {
        "source_round": ROUND227_SOURCE_ROUND_PATH,
        "large_sector": ROUND227_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "target_archetype_count": len(ROUND227_REQUIRED_TARGET_ALIASES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
    }


def round227_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND227_SOURCE_ROUND_PATH,
        "large_sector": ROUND227_LARGE_SECTOR.value,
        "summary": round227_summary(),
        "target_aliases": dict(ROUND227_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND227_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND227_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND227_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND227_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_use_round227_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_epc_pf_housing_or_data_center_headline_as_green",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round227_summary_markdown() -> str:
    summary = round227_summary()
    lines = [
        "# Round 227 R10 Loop 9 Construction Real Estate Materials Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | stage2 | stage3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND227_CASE_CANDIDATES:
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
                    case.score_price_alignment,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Samsung E&A/GS E&C and Hyundai E&C are Stage 2 EPC/gas-infra watch cases, not Stage 3-Green.",
            "- Taeyoung/PF stress is a hard 4C reference point.",
            "- Housing supply policy and AI data-center headlines are event premium until company-level cash flow appears.",
            "- Construction safety events and building-material demand weakness block unsafe Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round227_green_gate_review_markdown() -> str:
    lines = [
        "# Round 227 R10 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND227_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND227_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `EPC 수주 $6B + 주가 +8.5%` can create Stage 2/4B-watch.",
            "- `EPC 수주 + 마진 + 공정률 매출 + 현금회수 + working capital 안정` is the bundle that can support deeper Stage review.",
            "- `PF workout` or `fatal construction accident` is 4C/RedTeam input, not positive evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round227_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 227 R10 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND227_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND227_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- PF workout or debt reschedule is a thesis-break input, not positive Green evidence.",
            "- Fatal bridge/apartment collapse and repeated workplace fatality are operational-trust 4C inputs.",
            "- Data-center headline rallies stay capped until tenant, NOI/AFFO, power, water, permitting, and capex-per-share pass.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND227_CASE_CANDIDATES:
        if case.stage4b_status == "watch" or case.stage4c_date or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round227_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 227 R10 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND227_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round227_r10_loop9_reports(
    output_directory: str | Path = ROUND227_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND227_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND227_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round227_case_records(), cases_path),
        "audit": _write_json(round227_audit_payload(), audit_path),
        "summary": output / "round227_r10_loop9_price_validation_summary.md",
        "case_matrix": output / "round227_r10_loop9_case_matrix.csv",
        "target_aliases": output / "round227_r10_loop9_target_aliases.csv",
        "score_adjustments": output / "round227_r10_loop9_score_adjustments.csv",
        "shadow_weights": output / "round227_r10_loop9_shadow_weights.csv",
        "price_validation_fields": output / "round227_r10_loop9_price_validation_fields.csv",
        "green_gate_review": output / "round227_r10_loop9_green_gate_review.md",
        "price_validation_plan": output / "round227_r10_loop9_price_validation_plan.md",
        "stage4b_4c_review": output / "round227_r10_loop9_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round227_summary_markdown(), encoding="utf-8")
    _write_csv(round227_case_rows(), paths["case_matrix"])
    _write_csv(round227_target_alias_rows(), paths["target_aliases"])
    _write_csv(round227_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round227_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round227_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round227_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round227_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round227_stage4b_4c_review_markdown(), encoding="utf-8")
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
