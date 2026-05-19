"""Round-201 R10 Loop-7 construction/real-estate price-path pack.

Round 201 is a calibration-only layer for Korean construction, PF credit,
overseas EPC, apartment quality/safety, real-asset data centers, REIT/AFFO,
and disaster/rebuild headline risk. It records why construction headlines
must be separated from cash flow, EPC margin, working capital, PF funding
cost, tenant contracts, NOI/AFFO, power/water permitting, capex per share,
and safety/quality trust.

Simple example: a Saudi EPC award can be Stage 2 attention. It is not
Stage 3-Green until margin, progress revenue, cost control, and cash
collection are visible as-of the case date.

This module is report/evaluation material only. Production candidate
generation, feature engineering, scoring, staging, and RedTeam code must not
import it.
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


ROUND201_SOURCE_ROUND_PATH = "docs/round/round_201.md"
ROUND201_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round201_r10_loop7_construction_real_estate_materials_price_validation"
ROUND201_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop7_round201.jsonl"
ROUND201_DEFAULT_AUDIT_PATH = (
    "data/sector_taxonomy/round201_r10_loop7_construction_real_estate_materials_price_validation_audit.json"
)

ROUND201_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "CONSTRUCTION_REAL_ESTATE_CREDIT": E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT.value,
    "CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA": E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA.value,
    "PF_RESTRUCTURING_RELIEF": E2RArchetype.PF_RESTRUCTURING_RELIEF.value,
    "PF_CREDIT_REDTEAM_OVERLAY": E2RArchetype.PF_CREDIT_REDTEAM_OVERLAY.value,
    "OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA": E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA.value,
    "EPC_LOW_MARGIN_ORDER_OVERLAY": E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY.value,
    "APARTMENT_QUALITY_SAFETY_OVERLAY": E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY.value,
    "BUILDING_MATERIALS_PRICE_COST": E2RArchetype.BUILDING_MATERIALS_PRICE_COST.value,
    "DATA_CENTER_REIT_INFRASTRUCTURE": E2RArchetype.DATA_CENTER_REIT_INFRASTRUCTURE.value,
    "AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT": E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT.value,
    "AI_DATA_CENTER_NO_REVENUE_NO_TENANT": E2RArchetype.AI_DATA_CENTER_NO_REVENUE_NO_TENANT.value,
    "DATA_CENTER_POWER_WATER_PERMITTING": E2RArchetype.DATA_CENTER_POWER_WATER_PERMITTING.value,
    "REIT_AFFO_INTEGRITY_OVERLAY": E2RArchetype.REIT_AFFO_INTEGRITY_OVERLAY.value,
    "AI_INFRA_REAL_ASSET_THEME_OVERLAY": E2RArchetype.AI_INFRA_REAL_ASSET_THEME_OVERLAY.value,
    "DISASTER_REBUILD_EVENT": E2RArchetype.DISASTER_REBUILD_EVENT.value,
}

ROUND201_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "company_level_order_or_tenant_confirmed",
    "cash_flow_after_working_capital_confirmed",
    "epc_margin_or_noi_affo_confirmed",
    "pf_and_funding_cost_risk_passed",
    "cost_ratio_or_project_progress_stable",
    "tenant_occupancy_or_utilization_confirmed",
    "capex_per_share_or_dilution_passed",
    "safety_quality_trust_passed",
    "price_path_after_cash_flow_evidence",
)

ROUND201_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "contract_headline_only",
    "pf_relief_policy_only",
    "real_estate_rebound_theme_only",
    "data_center_theme_without_tenant",
    "asset_headline_without_noi_affo",
    "reit_yield_headline_only",
    "epc_backlog_without_margin",
    "low_margin_order_risk",
    "capex_per_share_dilution",
    "quality_safety_incident",
    "workplace_fatality_repeated",
    "working_capital_worsening",
)

ROUND201_STAGE4B_STATUSES: tuple[str, ...] = ("none", "watch", "elevated", "graduated")

ROUND201_HARD_4C_GATES: tuple[str, ...] = (
    "pf_workout_or_debt_reschedule",
    "pf_delinquency_spike",
    "unsold_inventory_or_presale_failure",
    "construction_cost_ratio_spike",
    "working_capital_deterioration",
    "order_cancellation_or_client_payment_delay",
    "low_margin_epc_loss_recognition",
    "apartment_collapse_or_quality_accident",
    "repeated_workplace_fatality_or_site_shutdown",
    "license_suspension_or_cancellation_risk",
    "tenant_absent_or_no_binding_lease",
    "power_water_or_permitting_failure",
    "affo_integrity_break",
    "capex_dilution",
)

ROUND201_PRICE_BACKFILL_FIELDS: tuple[str, ...] = (
    "stage1_date",
    "stage2_date",
    "stage3_date",
    "stage4b_date",
    "stage4c_date",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_date",
    "peak_price",
    "MFE_5D",
    "MFE_20D",
    "MFE_30D",
    "MFE_60D",
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_5D",
    "MAE_20D",
    "MAE_30D",
    "MAE_60D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "MAE_2Y",
    "drawdown_after_peak",
    "relative_strength_vs_kospi",
    "relative_strength_vs_construction_basket",
    "relative_strength_vs_reit_basket",
    "relative_strength_vs_building_materials_basket",
    "relative_strength_vs_data_center_real_asset_basket",
    "contract_size",
    "epc_margin_visibility",
    "project_cost_control",
    "progress_revenue",
    "cash_collection",
    "working_capital",
    "pf_exposure",
    "pf_delinquency",
    "funding_cost",
    "unsold_inventory",
    "construction_cost_ratio",
    "tenant_contract_quality",
    "occupancy",
    "noi_affo",
    "capex_per_share",
    "power_water_permitting",
    "safety_quality_incident_flag",
    "hard_4c_confirmed",
)


@dataclass(frozen=True)
class Round201ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {
            "axis": self.axis,
            "points": str(self.points),
            "direction": self.direction,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class Round201CaseCandidate:
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
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND201_SCORE_ADJUSTMENTS: tuple[Round201ScoreAdjustment, ...] = (
    Round201ScoreAdjustment("cash_flow_after_working_capital", 5, "raise", "R10 Green은 수주가 현금흐름으로 닫힐 때 강하다."),
    Round201ScoreAdjustment("epc_margin_visibility", 5, "raise", "대형 EPC는 계약 크기보다 마진 가시성이 Stage 3의 핵심이다."),
    Round201ScoreAdjustment("project_cost_control", 4, "raise", "공정률과 원가율이 안정되어야 저마진 수주 위험을 줄인다."),
    Round201ScoreAdjustment("handover_milestone", 3, "raise", "완공·인도 milestone은 수주 headline보다 강한 Stage 2 증거다."),
    Round201ScoreAdjustment("pf_credit_cleanup", 5, "raise", "PF 부실 정리와 우량 프로젝트 분리가 확인될 때만 credit relief를 올린다."),
    Round201ScoreAdjustment("funding_cost_control", 4, "raise", "리츠·부동산은 조달비용이 배당과 AFFO를 결정한다."),
    Round201ScoreAdjustment("tenant_contract_quality", 5, "raise", "데이터센터 real asset은 임차계약이 있어야 현금흐름 후보가 된다."),
    Round201ScoreAdjustment("noi_affo_visibility", 5, "raise", "자산 headline보다 NOI/AFFO와 배당 커버리지가 중요하다."),
    Round201ScoreAdjustment("occupancy_or_utilization", 4, "raise", "공실률·가동률이 숫자로 확인되어야 자산 수익성이 보인다."),
    Round201ScoreAdjustment("power_water_permitting_secured", 4, "raise", "AI 데이터센터는 전력·물·인허가가 병목이다."),
    Round201ScoreAdjustment("safety_quality_trust", 5, "raise", "건설주는 안전·품질 신뢰가 Green의 전제다."),
    Round201ScoreAdjustment("contract_headline_only", -4, "lower", "수주 headline만으로 Stage 3-Green을 만들지 않는다."),
    Round201ScoreAdjustment("pf_relief_policy_only", -5, "lower", "PF 지원책은 relief이지 체급 변화 증거가 아니다."),
    Round201ScoreAdjustment("real_estate_rebound_theme_only", -4, "lower", "부동산 반등 테마만으로 현금흐름을 발명하지 않는다."),
    Round201ScoreAdjustment("data_center_theme_without_tenant", -5, "lower", "임차인 없는 데이터센터 테마는 Green 금지다."),
    Round201ScoreAdjustment("asset_headline_without_noi_affo", -5, "lower", "자산 보유 headline은 NOI/AFFO 전까지 제한한다."),
    Round201ScoreAdjustment("epc_backlog_without_margin", -4, "lower", "수주잔고가 많아도 마진이 없으면 Stage 3가 아니다."),
    Round201ScoreAdjustment("low_margin_order_risk", -4, "lower", "저마진 EPC는 수주가 오히려 현금흐름 부담이 될 수 있다."),
    Round201ScoreAdjustment("capex_per_share_dilution", -4, "lower", "CAPEX가 주당 AFFO/FCF를 희석하면 Green을 막는다."),
    Round201ScoreAdjustment("quality_safety_incident", -5, "lower", "아파트 붕괴·품질 사고는 hard RedTeam이다."),
    Round201ScoreAdjustment("workplace_fatality_repeated", -5, "lower", "반복 사망사고와 현장중단은 operational trust 4C gate다."),
)


ROUND201_CASE_CANDIDATES: tuple[Round201CaseCandidate, ...] = (
    Round201CaseCandidate(
        case_id="samsung_ea_fadhili_epc_backlog_stage2_watch",
        symbol="028050",
        company_name="삼성E&A",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA,
        secondary_archetypes=(E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY,),
        case_type="success_candidate",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 3),
        stage3_date=None,
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        stage3_decision="deferred_until_epc_margin_progress_revenue_cost_control_working_capital_and_cash_collection_are_visible",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("fadhili_gas_expansion_contract", "roughly_6bn_usd_contract_report", "large_epc_backlog", "2027_completion_plan"),
        red_flag_fields=("contract_headline_only", "epc_backlog_without_margin", "low_margin_order_risk", "working_capital_unverified"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Fadhili EPC award is Stage 2; Green waits for margin, progress revenue, cost control, and cash collection.",
    ),
    Round201CaseCandidate(
        case_id="hyundai_ec_jafurah_gas_infra_stage2_watch",
        symbol="000720",
        company_name="현대건설",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA,
        secondary_archetypes=(E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY,),
        case_type="success_candidate",
        stage1_date=date(2024, 6, 30),
        stage2_date=date(2024, 6, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_sovereign_contract_margin_cost_control_cash_collection_and_working_capital_are_confirmed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("aramco_jafurah_main_gas_network_contracts", "sovereign_customer", "project_scale", "gas_infrastructure_backlog"),
        red_flag_fields=("low_margin_epc", "working_capital_burden", "cost_overrun_watch", "client_payment_delay_watch"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Large Saudi gas infrastructure orders can score Stage 2, but EPC margin and cash conversion decide Stage 3.",
    ),
    Round201CaseCandidate(
        case_id="daewoo_ec_grand_faw_handover_stage2_watch",
        symbol="047040",
        company_name="대우건설",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA,
        secondary_archetypes=(E2RArchetype.INFRA_RECONSTRUCTION_POLICY,),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 11, 12),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_handover_turns_into_profit_recognition_cash_collection_and_follow_on_orders",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("grand_faw_port_handover", "five_berths_delivered", "iraq_development_road_context", "future_capacity_target"),
        red_flag_fields=("cash_collection_unverified", "iraq_political_risk", "follow_on_order_unverified", "client_payment_delay_watch"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Handover milestone is better than order headline, but Stage 3 needs profit recognition and cash collection.",
    ),
    Round201CaseCandidate(
        case_id="taeyoung_pf_workout_credit_hard_4c",
        symbol="009410",
        company_name="태영건설",
        primary_archetype=E2RArchetype.PF_RESTRUCTURING_RELIEF,
        secondary_archetypes=(E2RArchetype.PF_CREDIT_REDTEAM_OVERLAY, E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA),
        case_type="4c_thesis_break",
        stage1_date=date(2023, 12, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2023, 12, 1),
        stage3_decision="hard_blocked_by_pf_liquidity_stress_debt_reschedule_and_workout",
        stage4b_status="none",
        hard_4c_confirmed=True,
        evidence_fields=("pf_liquidity_stress", "debt_reschedule_plan", "sector_credit_contagion", "government_support_context"),
        red_flag_fields=("pf_workout_or_debt_reschedule", "pf_delinquency_spike", "funding_market_dependency", "cash_flow_break"),
        score_price_alignment="aligned",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="PF support can be relief, but debt reschedule/workout is R10 hard 4C, not Green evidence.",
    ),
    Round201CaseCandidate(
        case_id="hdc_hyundai_development_apartment_collapse_hard_4c",
        symbol="294870",
        company_name="HDC현대산업개발",
        primary_archetype=E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY,
        secondary_archetypes=(E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,),
        case_type="4c_thesis_break",
        stage1_date=date(2021, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2022, 1, 11),
        stage3_decision="hard_blocked_by_apartment_collapse_quality_safety_and_brand_trust_break",
        stage4b_status="none",
        hard_4c_confirmed=True,
        evidence_fields=("gwangju_hwajeong_ipark_collapse", "six_fatalities", "faulty_construction_method", "brand_trust_damage"),
        red_flag_fields=("apartment_collapse_or_quality_accident", "safety_quality_trust_break", "license_suspension_risk", "warranty_rebuild_cost"),
        score_price_alignment="aligned",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Apartment collapse is a hard quality/safety 4C gate; housing-cycle recovery cannot override trust break.",
    ),
    Round201CaseCandidate(
        case_id="posco_ec_dl_construction_workplace_safety_4c_watch",
        symbol="MULTI",
        company_name="POSCO E&C / DL건설",
        primary_archetype=E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY,
        secondary_archetypes=(E2RArchetype.PF_CREDIT_REDTEAM_OVERLAY,),
        case_type="4b_watch",
        stage1_date=date(2025, 9, 15),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 9, 15),
        stage4c_date=None,
        stage3_decision="blocked_until_repeated_fatality_site_shutdown_fine_license_and_operational_trust_risks_are_resolved",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("workplace_fatality_crackdown", "site_shutdown", "management_resignation", "fatal_accident_penalty_policy"),
        red_flag_fields=("workplace_fatality_repeated", "site_shutdown", "license_suspension_or_cancellation_risk", "operational_trust_watch"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Repeated fatalities and site shutdowns are RedTeam inputs because they can affect cost, license, reputation, and orders.",
    ),
    Round201CaseCandidate(
        case_id="sk_aws_ulsan_ai_data_center_real_asset_insufficient_evidence",
        symbol="MULTI",
        company_name="SK/AWS 울산 AI 데이터센터",
        primary_archetype=E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT,
        secondary_archetypes=(
            E2RArchetype.AI_DATA_CENTER_NO_REVENUE_NO_TENANT,
            E2RArchetype.DATA_CENTER_POWER_WATER_PERMITTING,
            E2RArchetype.AI_INFRA_REAL_ASSET_THEME_OVERLAY,
        ),
        case_type="success_candidate",
        stage1_date=date(2025, 6, 20),
        stage2_date=date(2026, 2, 11),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_listed_vehicle_tenant_noi_affo_power_water_capex_per_share_and_funding_cost_are_confirmed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("sk_aws_ulsan_ai_data_center_announcement", "100mw_initial_capacity", "openai_samsung_sds_sk_telecom_dc_plan", "ai_data_center_capex"),
        red_flag_fields=("data_center_theme_without_tenant", "asset_headline_without_noi_affo", "power_water_permitting_unverified", "capex_per_share_dilution_watch"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="AI data-center real asset is a strong theme, but R10 Green needs tenant, NOI/AFFO, power/water, and capex integrity.",
    ),
)


def round201_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND201_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector.value,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round201 R10 Loop-7 construction/real-estate price-path validation case. "
                "This is calibration-only and must not be used for candidate generation."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "announcement" in field
                or "context" in field
                or "support" in field
                or "stress" in field
                or "cycle" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "margin" in field
                or "cash" in field
                or "affo" in field
                or "tenant" in field
                or "profit" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "headline" in field
                or "theme" in field
                or "watch" in field
                or "announcement" in field
                or "support" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "pf" in field
                or "workout" in field
                or "accident" in field
                or "collapse" in field
                or "fatality" in field
                or "license" in field
                or "cash_flow_break" in field
                or "trust" in field
                or "permitting" in field
                or "dilution" in field
            ),
            must_have_fields=ROUND201_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={
                "cash_flow_after_working_capital_delta": 5.0,
                "epc_margin_visibility_delta": 5.0,
                "project_cost_control_delta": 4.0,
                "handover_milestone_delta": 3.0,
                "pf_credit_cleanup_delta": 5.0,
                "tenant_contract_quality_delta": 5.0,
                "noi_affo_visibility_delta": 5.0,
                "safety_quality_trust_delta": 5.0,
                "pf_relief_policy_only_delta": -5.0,
                "data_center_theme_without_tenant_delta": -5.0,
                "quality_safety_incident_delta": -5.0,
                "workplace_fatality_repeated_delta": -5.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "needs_ohlc_backfill_true",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_contract_pf_relief_data_center_reit_or_rebuild_headline_as_green_evidence",
                *ROUND201_GREEN_REQUIRED_FIELDS,
                *ROUND201_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8 if candidate.stage2_date or candidate.stage4c_date else 0.35,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round201_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND201_CASE_CANDIDATES:
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


def round201_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND201_SCORE_ADJUSTMENTS)


def round201_price_backfill_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round201_backfill": "true"} for field in ROUND201_PRICE_BACKFILL_FIELDS)


def round201_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round201_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND201_REQUIRED_TARGET_ALIASES.items()
    )


def round201_summary() -> dict[str, int | bool]:
    cases = round201_case_records()
    return {
        "case_candidate_count": len(cases),
        "required_target_count": len(ROUND201_REQUIRED_TARGET_ALIASES),
        "score_adjustment_count": len(ROUND201_SCORE_ADJUSTMENTS),
        "price_backfill_field_count": len(ROUND201_PRICE_BACKFILL_FIELDS),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "hard_4c_case_count": sum(1 for case in ROUND201_CASE_CANDIDATES if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in ROUND201_CASE_CANDIDATES if case.stage3_date),
        "stage4b_watch_or_elevated_count": sum(
            1 for case in ROUND201_CASE_CANDIDATES if case.stage4b_status in {"watch", "elevated"}
        ),
        "needs_ohlc_backfill_count": sum(
            1 for case in ROUND201_CASE_CANDIDATES if case.price_validation_status == "needs_ohlc_backfill"
        ),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "needs_ohlc_backfill": True,
    }


def write_round201_r10_loop7_reports(
    *,
    output_directory: str | Path = ROUND201_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND201_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND201_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = write_case_library(round201_case_records(), cases_path)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "audit_json": audit,
        "summary": output / "round201_r10_loop7_price_validation_summary.md",
        "case_matrix": output / "round201_r10_loop7_case_matrix.csv",
        "target_aliases": output / "round201_r10_loop7_target_aliases.csv",
        "score_adjustments": output / "round201_r10_loop7_score_adjustments.csv",
        "price_backfill_fields": output / "round201_r10_loop7_price_backfill_fields.csv",
        "green_gate_review": output / "round201_r10_loop7_green_gate_review.md",
        "price_backfill_plan": output / "round201_r10_loop7_price_backfill_plan.md",
        "stage4b_4c_review": output / "round201_r10_loop7_stage4b_4c_review.md",
    }
    audit.write_text(json.dumps(round201_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round201_case_rows(), paths["case_matrix"])
    _write_rows(round201_target_alias_rows(), paths["target_aliases"])
    _write_rows(round201_score_adjustment_rows(), paths["score_adjustments"])
    _write_rows(round201_price_backfill_field_rows(), paths["price_backfill_fields"])
    paths["summary"].write_text(render_round201_summary_markdown(), encoding="utf-8")
    paths["green_gate_review"].write_text(render_round201_green_gate_review_markdown(), encoding="utf-8")
    paths["price_backfill_plan"].write_text(render_round201_price_backfill_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round201_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def round201_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND201_SOURCE_ROUND_PATH,
        "large_sector": Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS.value,
        "summary": round201_summary(),
        "target_aliases": list(round201_target_alias_rows()),
        "green_required_fields": list(ROUND201_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND201_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_statuses": list(ROUND201_STAGE4B_STATUSES),
        "hard_4c_gates": list(ROUND201_HARD_4C_GATES),
        "score_adjustments": list(round201_score_adjustment_rows()),
        "case_ids": [case.case_id for case in ROUND201_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round201_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_contract_pf_relief_real_estate_rebound_data_center_reit_or_disaster_rebuild_headline_as_green_evidence",
            "do_not_invent_cash_flow_margin_noi_affo_tenant_power_water_capex_or_stage_prices",
            "do_not_confirm_hard_4c_without_reliable_primary_or_major_source",
        ],
    }


def render_round201_summary_markdown() -> str:
    summary = round201_summary()
    lines = [
        "# Round-201 R10 Loop-7 Price-Path Validation Summary",
        "",
        f"- source_round: `{ROUND201_SOURCE_ROUND_PATH}`",
        "- large_sector: `CONSTRUCTION_REAL_ESTATE_MATERIALS`",
        "- scope: PF credit, overseas EPC, apartment safety, AI data-center real assets, REIT/AFFO, and rebuild headline risk",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- score_adjustment_count: {summary['score_adjustment_count']}",
        f"- price_backfill_field_count: {summary['price_backfill_field_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- stage3_case_count: {summary['stage3_case_count']}",
        f"- stage4b_watch_or_elevated_count: {summary['stage4b_watch_or_elevated_count']}",
        f"- needs_ohlc_backfill_count: {summary['needs_ohlc_backfill_count']}",
        "- production_scoring_changed: false",
        "- candidate_generation_input: false",
        "- shadow_weight_only: true",
        "- needs_ohlc_backfill: true",
        "",
        "## Interpretation",
        "",
        "- R10은 수주, PF 지원, 데이터센터, 부동산 반등 headline이 가격을 먼저 밀기 쉬운 섹터다.",
        "- 삼성E&A·현대건설·대우건설은 Stage 2 후보지만, EPC margin과 cash collection 전 Green이 아니다.",
        "- 태영건설 PF workout은 R10 hard 4C 기준점이다.",
        "- HDC현대산업개발 붕괴 사고는 품질·안전 hard 4C 기준점이다.",
        "- POSCO E&C/DL건설 안전 이슈는 operational trust RedTeam watch다.",
        "- SK/AWS 데이터센터는 좋은 구조 후보지만 listed vehicle의 tenant, NOI/AFFO, power/water 전 Green이 아니다.",
        "",
        "쉬운 예: `as_of_date=2024-04-03`에 삼성E&A가 대형 수주를 받아도, 원가율과 현금 회수가 아직 없으면 Stage 3-Green이 아니라 Stage 2 watch다.",
    ]
    return "\n".join(lines) + "\n"


def render_round201_green_gate_review_markdown() -> str:
    lines = [
        "# Round-201 R10 Loop-7 Green Gate Review",
        "",
        "## Green Required Evidence",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND201_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Green Forbidden Patterns", ""])
    lines.extend(f"- `{field}`" for field in ROUND201_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "| --- | --- | ---: | --- |"])
    for adjustment in ROUND201_SCORE_ADJUSTMENTS:
        lines.append(f"| `{adjustment.axis}` | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these weights to production scoring yet.",
            "- Do not use Round201 cases as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds to force promotion.",
            "- Do not invent cash flow, EPC margin, NOI/AFFO, tenant contracts, power/water, funding cost, capex per share, stage prices, or MFE/MAE.",
            "- Do not treat contract headline, PF support, real-estate rebound, AI data-center headline, REIT yield, or disaster rebuild as Green evidence alone.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round201_price_backfill_plan_markdown() -> str:
    lines = [
        "# Round-201 R10 Loop-7 Price Backfill Plan",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND201_PRICE_BACKFILL_FIELDS)
    lines.extend(["", "## Priority Cases", "", "| case | stage marker | current status | 4B status | hard 4C |", "| --- | --- | --- | --- | --- |"])
    for case in ROUND201_CASE_CANDIDATES:
        stage_marker = case.stage3_date or case.stage2_date or case.stage4b_date or case.stage4c_date or case.stage1_date
        lines.append(
            f"| `{case.case_id}` | {_date_text(stage_marker) or 'undated'} | "
            f"{case.price_validation_status} | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} |"
        )
    lines.extend(
        [
            "",
            "## Backfill Rule",
            "",
            "- Use official OHLC data for exact MFE/MAE.",
            "- Keep unknown values null or `needs_ohlc_backfill`.",
            "- Split EPC award, handover, PF workout, safety accident, data-center announcement, and permitting dates.",
            "- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round201_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round-201 R10 Loop-7 Stage 4B / 4C Review",
        "",
        "## 4B Status Definitions",
        "",
        "- `watch`: EPC award, PF relief, data-center theme, REIT yield, or rebuild headline runs ahead of cash flow.",
        "- `elevated`: margin, PF, funding cost, permitting, tenant, AFFO, or quality risk appears after the headline.",
        "- `graduated`: good orders or policy relief stop surprising and price reaction fades.",
        "",
        "## Hard 4C Gates",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND201_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## R10 Interpretation",
            "",
            "- PF workout and debt reschedule are hard 4C, not recovery evidence.",
            "- Apartment collapse or repeated fatality is an operational trust break.",
            "- EPC backlog without margin and working-capital evidence stays Stage 2 watch.",
            "- AI data-center real asset needs tenant, NOI/AFFO, power/water, and capex integrity before Green.",
            "",
            "## Case Review",
            "",
            "| case | 4B status | hard 4C confirmed | interpretation |",
            "| --- | --- | --- | --- |",
        ]
    )
    for case in ROUND201_CASE_CANDIDATES:
        lines.append(
            f"| `{case.case_id}` | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    rows_tuple = tuple(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows_tuple[0].keys()), lineterminator="\n")
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow(dict(row))
    return path


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


__all__ = [
    "ROUND201_CASE_CANDIDATES",
    "ROUND201_DEFAULT_AUDIT_PATH",
    "ROUND201_DEFAULT_CASES_PATH",
    "ROUND201_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND201_GREEN_FORBIDDEN_PATTERNS",
    "ROUND201_GREEN_REQUIRED_FIELDS",
    "ROUND201_HARD_4C_GATES",
    "ROUND201_PRICE_BACKFILL_FIELDS",
    "ROUND201_REQUIRED_TARGET_ALIASES",
    "ROUND201_SCORE_ADJUSTMENTS",
    "ROUND201_SOURCE_ROUND_PATH",
    "ROUND201_STAGE4B_STATUSES",
    "Round201CaseCandidate",
    "Round201ScoreAdjustment",
    "render_round201_green_gate_review_markdown",
    "render_round201_price_backfill_plan_markdown",
    "render_round201_stage4b_4c_review_markdown",
    "render_round201_summary_markdown",
    "round201_audit_payload",
    "round201_case_records",
    "round201_case_rows",
    "round201_price_backfill_field_rows",
    "round201_score_adjustment_rows",
    "round201_summary",
    "round201_target_alias_rows",
    "write_round201_r10_loop7_reports",
]
