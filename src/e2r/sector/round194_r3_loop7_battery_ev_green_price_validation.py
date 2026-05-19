"""Round-194 R3 Loop-7 battery/EV/green price-path validation pack.

Round 194 is a calibration-only layer for R3 battery, EV, ESS, and green
energy cases. It records why this archetype family should mostly block false
Stage 3-Green outcomes until contracts become GWh volume, shipments, margin,
FCF, and EPS/FCF revision.

Simple example: an ESS headline can route a stock to Stage 1 or Stage 2. It is
not Stage 3-Green until the same as-of evidence also shows customer call-off,
utilization, OPM/FCF, and durable EV/ESS demand.

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


ROUND194_SOURCE_ROUND_PATH = "docs/round/round_194.md"
ROUND194_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round194_r3_loop7_battery_ev_green_price_validation"
ROUND194_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop7_round194.jsonl"
ROUND194_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round194_r3_loop7_battery_ev_green_price_validation_audit.json"

ROUND194_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BATTERY_MATERIALS_CAPEX_OVERHEAT": E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT.value,
    "CATHODE_LONG_CONTRACT_VISIBILITY": E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY.value,
    "LITHIUM_RESOURCE_SECURITY_KOREA": E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA.value,
    "BATTERY_EQUIPMENT_CAPEX_CYCLE": E2RArchetype.BATTERY_EQUIPMENT_CAPEX_CYCLE.value,
    "BATTERY_RECYCLING_ESS_SHIFT": E2RArchetype.BATTERY_RECYCLING_ESS_SHIFT.value,
    "ESS_LFP_GRID_STORAGE": E2RArchetype.ESS_LFP_GRID_STORAGE.value,
    "EV_TO_ESS_CAPACITY_REDEPLOYMENT": E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT.value,
    "EV_BATTERY_JV_RESTRUCTURING": E2RArchetype.EV_BATTERY_JV_RESTRUCTURING.value,
    "BATTERY_CONTRACT_CANCELLATION_4C": E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C.value,
    "BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE": E2RArchetype.BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE.value,
    "BATTERY_TAX_CREDIT_QUALITY_OVERLAY": E2RArchetype.BATTERY_TAX_CREDIT_QUALITY_OVERLAY.value,
    "BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY": E2RArchetype.BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY.value,
    "SEPARATOR_EV_DEMAND_CYCLE": E2RArchetype.SEPARATOR_EV_DEMAND_CYCLE.value,
    "COPPER_FOIL_EV_DEMAND_CYCLE": E2RArchetype.COPPER_FOIL_EV_DEMAND_CYCLE.value,
    "LITHIUM_CYCLE_OVERLAY": E2RArchetype.LITHIUM_CYCLE_OVERLAY.value,
    "EVENT_LITHIUM_PRICE_RALLY": E2RArchetype.EVENT_LITHIUM_PRICE_RALLY.value,
}

ROUND194_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "binding_contract",
    "gwh_or_tonnage_volume",
    "customer_calloff_or_shipment",
    "utilization_rate",
    "opm_or_gross_margin_improvement",
    "fcf_after_capex",
    "eps_fcf_revision",
    "ev_or_ess_demand_durability",
    "tax_credit_quality_separated_from_underlying_profit",
)

ROUND194_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ev_theme",
    "ess_theme",
    "capa_announcement",
    "customer_name_only",
    "unconfirmed_media_report",
    "lithium_price_spike",
    "ipo_premium",
    "contract_value_without_actual_order",
    "operating_loss_ex_tax_credit",
)

ROUND194_STAGE4B_STATUSES: tuple[str, ...] = ("none", "watch", "elevated", "graduated")

ROUND194_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "contract_value_reduction",
    "customer_model_cancelled",
    "customer_ev_strategy_retreat",
    "take_or_pay_absent",
    "gwh_calloff_decline",
    "capex_cut_or_factory_delay",
    "utilization_collapse",
    "opm_collapse",
    "fcf_deterioration",
    "inventory_or_receivables_increase",
    "operating_loss_ex_ampc",
    "ev_demand_recovery_delay",
)

ROUND194_PRICE_BACKFILL_FIELDS: tuple[str, ...] = (
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
    "MFE_30D",
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_30D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "MAE_2Y",
    "drawdown_after_peak",
    "relative_strength_vs_kospi",
    "relative_strength_vs_battery_materials_basket",
    "relative_strength_vs_ess_basket",
    "relative_strength_vs_ev_battery_basket",
    "contract_binding_quality",
    "gwh_volume_visibility",
    "customer_order_calloff",
    "take_or_pay_flag",
    "shipment_evidence",
    "utilization_rate",
    "opm_margin_visibility",
    "fcf_after_capex",
    "eps_fcf_revision",
    "ess_revenue_conversion",
    "ev_demand_durability",
    "customer_quality",
    "tax_credit_quality",
    "ampc_dependency",
    "operating_profit_ex_ampc",
    "capa_announcement_flag",
    "contract_value_without_actual_order_flag",
    "unconfirmed_media_report_flag",
    "lithium_price_event_flag",
    "ipo_theme_premium_flag",
    "group_vertical_integration_story_flag",
    "inventory_or_receivables_risk",
    "stage4b_status",
    "hard_4c_confirmed",
)


@dataclass(frozen=True)
class Round194ScoreAdjustment:
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
class Round194CaseCandidate:
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
        return Round10LargeSector.BATTERY_EV_GREEN

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND194_SCORE_ADJUSTMENTS: tuple[Round194ScoreAdjustment, ...] = (
    Round194ScoreAdjustment("contract_binding_quality", 4, "raise", "계약 headline보다 실제 구속력과 take-or-pay를 본다."),
    Round194ScoreAdjustment("gwh_volume_visibility", 4, "raise", "GWh/톤수 물량이 있어야 매출 경로를 계산할 수 있다."),
    Round194ScoreAdjustment("customer_order_calloff", 4, "raise", "고객 주문 call-off와 출하 증거가 없으면 Stage 3를 막는다."),
    Round194ScoreAdjustment("opm_margin_visibility", 4, "raise", "ESS/EV 전환이 OPM 또는 gross margin으로 내려오는지 본다."),
    Round194ScoreAdjustment("fcf_after_capex", 4, "raise", "CAPEX 뒤 FCF가 남는지 확인한다."),
    Round194ScoreAdjustment("ess_revenue_conversion", 3, "raise", "ESS 전환은 매출 인식이 확인될 때 강해진다."),
    Round194ScoreAdjustment("utilization_rate", 3, "raise", "공장 가동률은 CAPA announcement의 반대편 검증축이다."),
    Round194ScoreAdjustment("customer_quality", 3, "raise", "고객의 모델/전략/신용도가 계약 지속성을 좌우한다."),
    Round194ScoreAdjustment("tax_credit_quality", 2, "raise", "AMPC/세액공제는 본업 이익과 분리해서 본다."),
    Round194ScoreAdjustment("ev_theme", -5, "lower", "EV 성장 테마만으로 Stage 3를 만들지 않는다."),
    Round194ScoreAdjustment("capa_announcement", -4, "lower", "CAPA는 비용이 먼저 나갈 수 있으므로 매출/마진/FCF 전에는 감점한다."),
    Round194ScoreAdjustment("customer_name_only", -4, "lower", "Tesla/Ford 같은 고객명만으로는 충분하지 않다."),
    Round194ScoreAdjustment("non_binding_supply_mou", -4, "lower", "비구속 MOU는 Stage 1 라우팅에 가깝다."),
    Round194ScoreAdjustment("policy_subsidy_expectation", -3, "lower", "정책/보조금 기대는 본업 수익성과 분리한다."),
    Round194ScoreAdjustment("lithium_price_event", -3, "lower", "리튬 가격 이벤트는 구조적 Green이 아니라 cycle/event일 수 있다."),
    Round194ScoreAdjustment("ipo_theme_premium", -4, "lower", "IPO 수급과 그룹 스토리는 price-only 위험이다."),
    Round194ScoreAdjustment("group_vertical_integration_story", -3, "lower", "내재화 스토리는 외부 고객/OPM/FCF 전에는 제한한다."),
    Round194ScoreAdjustment("ess_media_report_unconfirmed", -3, "lower", "미확정 ESS 보도는 disclosure confidence cap을 건다."),
    Round194ScoreAdjustment("tax_credit_without_operating_profit", -3, "lower", "AMPC 제외 적자는 Green block에 가깝다."),
)


ROUND194_CASE_CANDIDATES: tuple[Round194CaseCandidate, ...] = (
    Round194CaseCandidate(
        case_id="lg_energy_solution_ess_lfp_stage2_ev_contract_4c_watch",
        symbol="373220",
        company_name="LG에너지솔루션",
        primary_archetype=E2RArchetype.ESS_LFP_GRID_STORAGE,
        secondary_archetypes=(
            E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT,
            E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C,
            E2RArchetype.BATTERY_TAX_CREDIT_QUALITY_OVERLAY,
        ),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2025, 7, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 26),
        stage3_decision="deferred_until_gwh_shipments_utilization_opm_fcf_eps_revision",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=(
            "tesla_lfp_ess_contract_4_3b_usd",
            "us_factory_ess_supply",
            "ev_to_ess_capacity_redeployment",
            "contract_period_2027_08_to_2030_07",
        ),
        red_flag_fields=(
            "ev_demand_slowdown",
            "q4_operating_loss",
            "capex_cut_30pct",
            "ford_freudenberg_contract_loss_watch",
            "ampc_dependency",
            "fcf_after_capex_unverified",
        ),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="ESS LFP contract can support Stage 2, but EV contract loss and margin/FCF gaps keep Stage 3 deferred.",
    ),
    Round194CaseCandidate(
        case_id="lnf_tesla_cathode_contract_value_reduction_hard_4c",
        symbol="066970",
        company_name="L&F",
        primary_archetype=E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY,
        secondary_archetypes=(E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C,),
        case_type="4c_thesis_break",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 29),
        stage3_decision="forbidden_contract_headline_until_calloff_volume_margin_eps",
        stage4b_status="elevated",
        hard_4c_confirmed=True,
        evidence_fields=("tesla_high_nickel_cathode_supply_deal", "customer_name_tesla", "contract_headline"),
        red_flag_fields=(
            "contract_value_reduction_hard_4c",
            "tesla_4680_ramp_failure",
            "customer_calloff_absent",
            "ev_demand_slowdown",
            "take_or_pay_absent",
        ),
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="false_green",
        price_validation_status="needs_ohlc_backfill",
        notes="Tesla customer and contract value were not enough; value reduction from headline contract to near-zero is a hard 4C calibration case.",
    ),
    Round194CaseCandidate(
        case_id="sk_innovation_sk_on_ev_thesis_break_ess_pivot_watch",
        symbol="096770",
        company_name="SK이노베이션/SK온",
        primary_archetype=E2RArchetype.EV_BATTERY_JV_RESTRUCTURING,
        secondary_archetypes=(E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, E2RArchetype.ESS_LFP_GRID_STORAGE),
        case_type="failed_rerating",
        stage1_date=None,
        stage2_date=date(2025, 9, 3),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 7, 1),
        stage3_decision="forbidden_until_ess_value_utilization_profit_fcf_debt_visibility",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("flatiron_ess_lfp_7_2gwh", "ev_line_to_ess_conversion", "sk_es_merger_financing_relief"),
        red_flag_fields=(
            "ten_quarters_losses",
            "net_debt_surge",
            "emergency_management",
            "contract_value_undisclosed",
            "loss_making_battery_unit",
        ),
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="SK On ESS pivot is Stage 2 watch, but the earlier EV battery thesis had debt/loss evidence close to 4C-watch.",
    ),
    Round194CaseCandidate(
        case_id="samsung_sdi_tesla_ess_unconfirmed_stage1_only",
        symbol="006400",
        company_name="삼성SDI",
        primary_archetype=E2RArchetype.ESS_LFP_GRID_STORAGE,
        secondary_archetypes=(E2RArchetype.BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE,),
        case_type="success_candidate",
        stage1_date=date(2025, 11, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 3, 5),
        stage3_decision="forbidden_unconfirmed_media_report_and_ev_loss",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("tesla_ess_media_report", "reported_three_year_3t_krw_ess_purchase"),
        red_flag_fields=(
            "company_said_not_decided",
            "unconfirmed_media_report",
            "ev_demand_sluggish_until_2026h1",
            "q4_operating_loss",
        ),
        score_price_alignment="unknown",
        rerating_result="event_premium",
        stage_failure_type="unknown",
        price_validation_status="needs_ohlc_backfill",
        notes="The Tesla ESS report is only Stage 1 attention because company confirmation, volume call-off, margin, and EPS/FCF are missing.",
    ),
    Round194CaseCandidate(
        case_id="sk_iet_separator_ev_demand_cycle_4c_watch",
        symbol="361610",
        company_name="SK아이이테크놀로지",
        primary_archetype=E2RArchetype.SEPARATOR_EV_DEMAND_CYCLE,
        secondary_archetypes=(E2RArchetype.EV_BATTERY_JV_RESTRUCTURING,),
        case_type="failed_rerating",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 5, 15),
        stage3_decision="forbidden_until_separator_utilization_customer_shipments_opm_fcf",
        stage4b_status="elevated",
        hard_4c_confirmed=False,
        evidence_fields=("separator_required_material", "panasonic_ev_battery_customer_reference"),
        red_flag_fields=(
            "sale_review",
            "ev_demand_weakening",
            "sk_on_financial_distress",
            "separator_utilization_unverified",
            "customer_capex_cut_risk",
        ),
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Separator demand is not structural Green when final EV demand, customer finances, utilization, and OPM are weakening.",
    ),
    Round194CaseCandidate(
        case_id="posco_future_m_lithium_event_and_ford_shock_false_green_guard",
        symbol="003670",
        company_name="포스코퓨처엠",
        primary_archetype=E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY,
        secondary_archetypes=(E2RArchetype.LITHIUM_CYCLE_OVERLAY, E2RArchetype.EVENT_LITHIUM_PRICE_RALLY),
        case_type="overheat",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 16),
        stage3_decision="forbidden_lithium_event_without_order_margin_fcf",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("long_term_cathode_contract_story", "lithium_price_event", "posco_group_raw_material_integration"),
        red_flag_fields=(
            "ford_ev_model_cancellation_shock",
            "customer_ev_strategy_retreat",
            "lithium_price_event_not_structural",
            "opm_fcf_unverified",
        ),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="theme_overheat",
        stage_failure_type="false_green",
        price_validation_status="needs_ohlc_backfill",
        notes="Lithium price spikes and contract headlines must be separated from actual customer orders, margin, and FCF.",
    ),
    Round194CaseCandidate(
        case_id="ecopro_materials_precursor_ipo_theme_overheat_guard",
        symbol="450080",
        company_name="에코프로머티리얼즈",
        primary_archetype=E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT,
        secondary_archetypes=(E2RArchetype.LITHIUM_CYCLE_OVERLAY,),
        case_type="overheat",
        stage1_date=date(2023, 11, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 16),
        stage3_decision="forbidden_group_vertical_integration_without_external_customer_opm_fcf",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("precursor_supply_chain_story", "ecopro_group_vertical_integration", "ipo_theme_premium"),
        red_flag_fields=(
            "external_customer_absent",
            "utilization_unverified",
            "opm_fcf_unverified",
            "ford_ev_supply_chain_shock",
            "group_story_without_price_spread",
        ),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="theme_overheat",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Precursor and group integration stories are not Stage 3 without outside customers, utilization, OPM, FCF, and spread evidence.",
    ),
)


def round194_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND194_CASE_CANDIDATES:
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
                "Round194 R3 Loop-7 battery/EV/ESS price-path validation case. "
                "This is calibration-only and must not be used for candidate generation."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "story" in field or "report" in field or "theme" in field or "event" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=(),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "lithium" in field or "ipo" in field or "theme" in field or "overheat" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "contract" in field
                or "cancellation" in field
                or "reduction" in field
                or "loss" in field
                or "demand" in field
                or "distress" in field
                or "shock" in field
            ),
            must_have_fields=ROUND194_GREEN_REQUIRED_FIELDS,
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
                "contract_binding_quality_delta": 4.0,
                "gwh_volume_visibility_delta": 4.0,
                "customer_order_calloff_delta": 4.0,
                "opm_margin_visibility_delta": 4.0,
                "fcf_after_capex_delta": 4.0,
                "ev_theme_delta": -5.0,
                "capa_announcement_delta": -4.0,
                "customer_name_only_delta": -4.0,
                "lithium_price_event_delta": -3.0,
                "tax_credit_without_operating_profit_delta": -3.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "needs_ohlc_backfill_true",
                "do_not_invent_price_or_stage_dates",
                *ROUND194_GREEN_REQUIRED_FIELDS,
                *ROUND194_GREEN_FORBIDDEN_PATTERNS,
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


def round194_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND194_CASE_CANDIDATES:
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


def round194_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND194_SCORE_ADJUSTMENTS)


def round194_price_backfill_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round194_backfill": "true"} for field in ROUND194_PRICE_BACKFILL_FIELDS)


def round194_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round194_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND194_REQUIRED_TARGET_ALIASES.items()
    )


def round194_summary() -> dict[str, int | bool]:
    cases = round194_case_records()
    return {
        "case_candidate_count": len(cases),
        "required_target_count": len(ROUND194_REQUIRED_TARGET_ALIASES),
        "score_adjustment_count": len(ROUND194_SCORE_ADJUSTMENTS),
        "price_backfill_field_count": len(ROUND194_PRICE_BACKFILL_FIELDS),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in ROUND194_CASE_CANDIDATES if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in ROUND194_CASE_CANDIDATES if case.stage3_date),
        "stage4b_watch_or_elevated_count": sum(
            1 for case in ROUND194_CASE_CANDIDATES if case.stage4b_status in {"watch", "elevated"}
        ),
        "needs_ohlc_backfill_count": sum(1 for case in ROUND194_CASE_CANDIDATES if case.price_validation_status == "needs_ohlc_backfill"),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "needs_ohlc_backfill": True,
    }


def write_round194_r3_loop7_reports(
    *,
    output_directory: str | Path = ROUND194_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND194_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND194_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = write_case_library(round194_case_records(), cases_path)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "audit_json": audit,
        "summary": output / "round194_r3_loop7_price_validation_summary.md",
        "case_matrix": output / "round194_r3_loop7_case_matrix.csv",
        "target_aliases": output / "round194_r3_loop7_target_aliases.csv",
        "score_adjustments": output / "round194_r3_loop7_score_adjustments.csv",
        "price_backfill_fields": output / "round194_r3_loop7_price_backfill_fields.csv",
        "green_gate_review": output / "round194_r3_loop7_green_gate_review.md",
        "price_backfill_plan": output / "round194_r3_loop7_price_backfill_plan.md",
        "stage4b_4c_review": output / "round194_r3_loop7_stage4b_4c_review.md",
    }
    audit.write_text(json.dumps(round194_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round194_case_rows(), paths["case_matrix"])
    _write_rows(round194_target_alias_rows(), paths["target_aliases"])
    _write_rows(round194_score_adjustment_rows(), paths["score_adjustments"])
    _write_rows(round194_price_backfill_field_rows(), paths["price_backfill_fields"])
    paths["summary"].write_text(render_round194_summary_markdown(), encoding="utf-8")
    paths["green_gate_review"].write_text(render_round194_green_gate_review_markdown(), encoding="utf-8")
    paths["price_backfill_plan"].write_text(render_round194_price_backfill_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round194_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def round194_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND194_SOURCE_ROUND_PATH,
        "large_sector": Round10LargeSector.BATTERY_EV_GREEN.value,
        "summary": round194_summary(),
        "target_aliases": list(round194_target_alias_rows()),
        "green_required_fields": list(ROUND194_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND194_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_statuses": list(ROUND194_STAGE4B_STATUSES),
        "hard_4c_gates": list(ROUND194_HARD_4C_GATES),
        "score_adjustments": list(round194_score_adjustment_rows()),
        "case_ids": [case.case_id for case in ROUND194_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round194_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_ev_ess_capa_or_customer_name_as_green_evidence",
            "do_not_invent_prices_stage_dates_shipments_margins_or_fcf",
        ],
    }


def render_round194_summary_markdown() -> str:
    summary = round194_summary()
    lines = [
        "# Round-194 R3 Loop-7 Price-Path Validation Summary",
        "",
        f"- source_round: `{ROUND194_SOURCE_ROUND_PATH}`",
        "- large_sector: `BATTERY_EV_GREEN`",
        "- scope: Korean EV battery, ESS pivot, cathode, separator, lithium event, and battery-material false-Green prevention",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- score_adjustment_count: {summary['score_adjustment_count']}",
        f"- price_backfill_field_count: {summary['price_backfill_field_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- overheat_count: {summary['overheat_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
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
        "- R3는 현재 Stage 3-Green을 많이 찾는 라운드가 아니라 false Green을 막는 라운드다.",
        "- LG에너지솔루션은 ESS LFP 계약으로 Stage 2는 가능하지만, EV 계약 손실과 OPM/FCF 공백 때문에 Stage 3는 보류한다.",
        "- L&F의 Tesla 계약가치 붕괴는 계약 headline이 실제 call-off와 매출로 내려오지 않을 때 생기는 hard 4C 사례다.",
        "- 삼성SDI의 미확정 Tesla ESS 보도는 회사 확인 전 Stage 1 attention에 머문다.",
        "- 포스코퓨처엠과 에코프로머티리얼즈는 리튬 이벤트/IPO/그룹 스토리와 구조적 EPS/FCF evidence를 분리해야 한다.",
        "",
        "쉬운 예: `as_of_date=2025-11-03`에 Tesla ESS 보도가 있어도 회사가 '결정된 것 없음'이라고 하면 Stage 3-Green 근거가 아니다. 계약 확인, GWh, 출하, OPM, FCF가 보여야 한다.",
    ]
    return "\n".join(lines) + "\n"


def render_round194_green_gate_review_markdown() -> str:
    lines = [
        "# Round-194 R3 Loop-7 Green Gate Review",
        "",
        "## Green Required Evidence",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND194_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Green Forbidden Patterns", ""])
    lines.extend(f"- `{field}`" for field in ROUND194_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "| --- | --- | ---: | --- |"])
    for adjustment in ROUND194_SCORE_ADJUSTMENTS:
        lines.append(f"| `{adjustment.axis}` | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these weights to production scoring yet.",
            "- Do not use Round194 cases as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds to force promotion.",
            "- Do not invent GWh, shipments, utilization, OPM, FCF, stage prices, or MFE/MAE.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round194_price_backfill_plan_markdown() -> str:
    lines = [
        "# Round-194 R3 Loop-7 Price Backfill Plan",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND194_PRICE_BACKFILL_FIELDS)
    lines.extend(["", "## Priority Cases", "", "| case | stage marker | current status | 4B status | hard 4C |", "| --- | --- | --- | --- | --- |"])
    for case in ROUND194_CASE_CANDIDATES:
        stage_marker = case.stage3_date or case.stage2_date or case.stage4c_date or case.stage1_date
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
            "- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round194_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round-194 R3 Loop-7 Stage 4B / 4C Review",
        "",
        "## 4B Status Definitions",
        "",
        "- `watch`: price, lithium, ESS, or customer narrative may be running ahead of OPM/FCF.",
        "- `elevated`: order reduction, utilization decline, inventory, AMPC dependence, or ASP pressure becomes material.",
        "- `graduated`: rerating is mostly accepted and incremental evidence no longer changes the frame.",
        "",
        "## Hard 4C Gates",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND194_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C confirmed | interpretation |", "| --- | --- | --- | --- |"])
    for case in ROUND194_CASE_CANDIDATES:
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
    "ROUND194_CASE_CANDIDATES",
    "ROUND194_DEFAULT_AUDIT_PATH",
    "ROUND194_DEFAULT_CASES_PATH",
    "ROUND194_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND194_GREEN_FORBIDDEN_PATTERNS",
    "ROUND194_GREEN_REQUIRED_FIELDS",
    "ROUND194_HARD_4C_GATES",
    "ROUND194_PRICE_BACKFILL_FIELDS",
    "ROUND194_REQUIRED_TARGET_ALIASES",
    "ROUND194_SCORE_ADJUSTMENTS",
    "ROUND194_SOURCE_ROUND_PATH",
    "ROUND194_STAGE4B_STATUSES",
    "Round194CaseCandidate",
    "Round194ScoreAdjustment",
    "render_round194_green_gate_review_markdown",
    "render_round194_price_backfill_plan_markdown",
    "render_round194_stage4b_4c_review_markdown",
    "render_round194_summary_markdown",
    "round194_audit_payload",
    "round194_case_records",
    "round194_case_rows",
    "round194_price_backfill_field_rows",
    "round194_score_adjustment_rows",
    "round194_summary",
    "round194_target_alias_rows",
    "write_round194_r3_loop7_reports",
]
