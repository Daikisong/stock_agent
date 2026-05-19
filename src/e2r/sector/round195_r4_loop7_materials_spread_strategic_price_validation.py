"""Round-195 R4 Loop-7 materials/spread/strategic resources validation pack.

Round 195 is a calibration-only layer for R4 materials, commodity spread,
strategic metals, lithium, polysilicon, and event-premium cases. It records why
commodity price spikes, tender offers, restructuring hopes, and unconfirmed
media reports must be separated from structural EPS/FCF rerating.

Simple example: a petrochemical restructuring plan can be Stage 2 watch. It is
not Stage 3-Green until product spread, operating rate, OPM, working-capital
cash flow, and EPS/FCF revision are visible as-of the case date.

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


ROUND195_SOURCE_ROUND_PATH = "docs/round/round_195.md"
ROUND195_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round195_r4_loop7_materials_spread_strategic_price_validation"
ROUND195_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r4_loop7_round195.jsonl"
ROUND195_DEFAULT_AUDIT_PATH = (
    "data/sector_taxonomy/round195_r4_loop7_materials_spread_strategic_price_validation_audit.json"
)

ROUND195_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "REFINING_OIL_SPREAD": E2RArchetype.REFINING_OIL_SPREAD.value,
    "CHEMICAL_SPREAD": E2RArchetype.CHEMICAL_SPREAD.value,
    "PETROCHEMICAL_RESTRUCTURING_KOREA": E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA.value,
    "COMMODITY_SPREAD_CYCLE_NOT_STRUCTURAL": E2RArchetype.COMMODITY_SPREAD_CYCLE_NOT_STRUCTURAL.value,
    "NONFERROUS_STRATEGIC_METALS": E2RArchetype.NONFERROUS_STRATEGIC_METALS.value,
    "RARE_METALS_STRATEGIC_MATERIALS": E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS.value,
    "RARE_METALS_PRICE_FLOOR_OFFTAKE": E2RArchetype.RARE_METALS_PRICE_FLOOR_OFFTAKE.value,
    "LITHIUM_BATTERY_RAW_MATERIAL": E2RArchetype.LITHIUM_BATTERY_RAW_MATERIAL.value,
    "LITHIUM_CYCLE_OVERLAY": E2RArchetype.LITHIUM_CYCLE_OVERLAY.value,
    "POLYSILICON_NON_CHINA_SUPPLY_OPTION": E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION.value,
    "COPPER_PROCESSING_PLUS_DEFENSE": E2RArchetype.COPPER_PROCESSING_PLUS_DEFENSE.value,
    "EVENT_PREMIUM_GOVERNANCE_OVERLAY": E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY.value,
    "COMMODITY_PRICE_4C_OVERLAY": E2RArchetype.COMMODITY_PRICE_4C_OVERLAY.value,
}

ROUND195_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "actual_product_spread",
    "cost_curve_advantage",
    "supply_discipline_or_capacity_shutdown_confirmed",
    "inventory_not_building",
    "fcf_conversion_or_cashflow_improvement",
    "price_floor_or_offtake_or_long_term_contract",
    "medium_term_eps_revision",
    "capex_and_dilution_risk_passed",
)

ROUND195_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "commodity_price_spike",
    "tender_offer_premium",
    "governance_battle",
    "policy_support_expectation",
    "unconfirmed_media_report",
    "restructuring_plan_only",
    "lithium_or_polysilicon_price_event",
    "geopolitical_refining_margin_spike",
)

ROUND195_STAGE4B_STATUSES: tuple[str, ...] = ("none", "watch", "elevated", "graduated")

ROUND195_HARD_4C_GATES: tuple[str, ...] = (
    "spread_reversal",
    "china_oversupply",
    "middle_east_capacity_overhang",
    "inventory_build",
    "ncc_shutdown",
    "contract_sale_tender_event_failure",
    "regulator_revision_order",
    "large_share_issuance_or_dilution",
    "commodity_price_decline",
    "project_capex_overrun",
    "offtake_absent",
    "fcf_deterioration",
)

ROUND195_PRICE_BACKFILL_FIELDS: tuple[str, ...] = (
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
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_5D",
    "MAE_20D",
    "MAE_30D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "MAE_2Y",
    "drawdown_after_peak",
    "relative_strength_vs_kospi",
    "relative_strength_vs_refining_basket",
    "relative_strength_vs_petrochemical_basket",
    "relative_strength_vs_strategic_metals_basket",
    "actual_product_spread",
    "crack_spread",
    "naphtha_ethylene_spread",
    "operating_rate",
    "capacity_shutdown_confirmed",
    "supply_discipline_confirmed",
    "inventory_normalization",
    "working_capital_cashflow",
    "fcf_after_working_capital",
    "price_floor_or_offtake",
    "cost_curve_advantage",
    "capex_commitment",
    "dilution_or_share_issuance_flag",
    "tender_offer_or_governance_premium_flag",
    "unconfirmed_media_report_flag",
    "commodity_price_event_flag",
    "stage4b_status",
    "hard_4c_confirmed",
)


@dataclass(frozen=True)
class Round195ScoreAdjustment:
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
class Round195CaseCandidate:
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
        return Round10LargeSector.MATERIALS_SPREAD_STRATEGIC

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND195_SCORE_ADJUSTMENTS: tuple[Round195ScoreAdjustment, ...] = (
    Round195ScoreAdjustment("actual_product_spread", 4, "raise", "가격 이벤트가 아니라 실제 제품 spread를 확인한다."),
    Round195ScoreAdjustment("fcf_after_working_capital", 4, "raise", "재고와 운전자본 뒤에 남는 FCF가 중요하다."),
    Round195ScoreAdjustment("supply_discipline_confirmed", 4, "raise", "공급규율이 확인될 때만 commodity cycle을 구조화한다."),
    Round195ScoreAdjustment("capacity_shutdown_confirmed", 3, "raise", "구조조정은 실제 shut-down/가동중단이 확인되어야 강해진다."),
    Round195ScoreAdjustment("price_floor_or_offtake", 4, "raise", "가격 floor와 offtake가 있으면 전략자원 visibility가 올라간다."),
    Round195ScoreAdjustment("cost_curve_advantage", 3, "raise", "원가곡선 우위가 없으면 가격 하락 때 이익이 무너진다."),
    Round195ScoreAdjustment("strategic_customer_or_government_offtake", 3, "raise", "전략광물은 정부/고객 offtake가 있어야 Stage 2 이상이다."),
    Round195ScoreAdjustment("inventory_normalization", 3, "raise", "재고 정상화는 spread 지속성의 핵심이다."),
    Round195ScoreAdjustment("capital_return_from_cashflow", 2, "raise", "현금흐름 기반 환원은 cycle과 구조 변화를 구분한다."),
    Round195ScoreAdjustment("commodity_price_up_only", -5, "lower", "원자재 가격 상승만으로 Stage 3를 만들지 않는다."),
    Round195ScoreAdjustment("restructuring_plan_without_margin", -3, "lower", "구조조정 계획만 있고 spread/OPM이 없으면 Stage 2 watch다."),
    Round195ScoreAdjustment("policy_support_without_fcf", -3, "lower", "정책 지원은 FCF 전까지 event premium이다."),
    Round195ScoreAdjustment("tender_offer_or_governance_premium", -4, "lower", "공개매수/경영권 분쟁 프리미엄은 구조적 EPS/FCF와 분리한다."),
    Round195ScoreAdjustment("unconfirmed_media_report", -4, "lower", "미확인 SpaceX/매각 보도는 Green 근거가 아니다."),
    Round195ScoreAdjustment("capacity_cut_expectation_only", -3, "lower", "기대만 있고 실제 capacity shutdown이 없으면 제한한다."),
    Round195ScoreAdjustment("lithium_price_event", -4, "lower", "리튬 가격 이벤트는 cycle/event premium으로 본다."),
    Round195ScoreAdjustment("refining_margin_geopolitical_shock", -3, "lower", "전쟁성 정제마진 spike는 구조적 Green이 아니다."),
    Round195ScoreAdjustment("customer_or_contract_unconfirmed", -3, "lower", "고객/계약 미확인은 disclosure confidence cap이다."),
    Round195ScoreAdjustment("capex_heavy_project_pre_revenue", -3, "lower", "대규모 CAPEX 프로젝트는 매출/FCF 전에는 부담이다."),
)


ROUND195_CASE_CANDIDATES: tuple[Round195CaseCandidate, ...] = (
    Round195CaseCandidate(
        case_id="lotte_chemical_petrochemical_loss_restructuring_watch",
        symbol="011170",
        company_name="롯데케미칼",
        primary_archetype=E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA,
        secondary_archetypes=(E2RArchetype.CHEMICAL_SPREAD, E2RArchetype.COMMODITY_PRICE_4C_OVERLAY),
        case_type="4c_thesis_break",
        stage1_date=None,
        stage2_date=date(2025, 11, 26),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 2, 7),
        stage3_decision="deferred_until_spread_opm_fcf_eps_after_capacity_shutdown",
        stage4b_status="watch",
        hard_4c_confirmed=True,
        evidence_fields=("petrochemical_restructuring_plan", "daesan_ncc_capacity_cut_direction", "government_support_package"),
        red_flag_fields=("2024_operating_loss_expanded", "china_middle_east_oversupply", "spread_reversal_risk", "fcf_unverified"),
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Restructuring can be Stage 2 relief, but 2024 loss and oversupply block Stage 3 before spread, OPM, and FCF improve.",
    ),
    Round195CaseCandidate(
        case_id="lg_chem_petrochemical_spread_failed_rerating_watch",
        symbol="051910",
        company_name="LG화학",
        primary_archetype=E2RArchetype.CHEMICAL_SPREAD,
        secondary_archetypes=(E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA, E2RArchetype.COMMODITY_PRICE_4C_OVERLAY),
        case_type="failed_rerating",
        stage1_date=None,
        stage2_date=date(2025, 12, 19),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 2, 7),
        stage3_decision="forbidden_until_actual_spread_operating_rate_feedstock_fcf",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("petrochemical_restructuring_plan_submitted", "bottoming_spread_expectation"),
        red_flag_fields=(
            "2024_operating_profit_down_63_75pct",
            "petrochemical_operating_loss",
            "china_middle_east_oversupply",
            "yeosu_ncc_feedstock_halt_watch",
        ),
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        stage_failure_type="false_green",
        price_validation_status="needs_ohlc_backfill",
        notes="Spread recovery hope is not enough; feedstock security, operating rate, OPM, and FCF must be visible.",
    ),
    Round195CaseCandidate(
        case_id="sk_innovation_refining_margin_cyclical_success_not_structural",
        symbol="096770",
        company_name="SK이노베이션",
        primary_archetype=E2RArchetype.REFINING_OIL_SPREAD,
        secondary_archetypes=(
            E2RArchetype.LNG_ENERGY_TRADING_DISTRIBUTION,
            E2RArchetype.COMMODITY_SPREAD_CYCLE_NOT_STRUCTURAL,
        ),
        case_type="cyclical_success",
        stage1_date=date(2025, 4, 30),
        stage2_date=date(2026, 5, 13),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_refining_margin_is_cyclical_until_multi_quarter_fcf_return",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("q1_2026_operating_profit_2_2t_krw", "refining_margin_recovery", "earnings_turnaround"),
        red_flag_fields=("refining_recovery_take_time_warning", "geopolitical_margin_spike_risk", "petrochemical_battery_losses"),
        score_price_alignment="aligned",
        rerating_result="cyclical_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Refining turnaround can be Stage 2/cyclical success, but war or supply-disruption margin is not structural Green.",
    ),
    Round195CaseCandidate(
        case_id="korea_zinc_governance_event_vs_critical_minerals_stage2",
        symbol="010130",
        company_name="고려아연",
        primary_archetype=E2RArchetype.NONFERROUS_STRATEGIC_METALS,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY, E2RArchetype.RARE_METALS_PRICE_FLOOR_OFFTAKE),
        case_type="event_premium",
        stage1_date=date(2024, 9, 13),
        stage2_date=date(2025, 12, 15),
        stage3_date=None,
        stage4b_date=date(2024, 9, 13),
        stage4c_date=date(2024, 11, 6),
        stage3_decision="deferred_until_financing_capex_offtake_margin_fcf_and_dilution_risk",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("critical_minerals_processing_plant_us_support", "non_china_strategic_metals_supply_chain", "tender_offer_event"),
        red_flag_fields=("governance_battle_event_premium", "large_share_issuance_revision_order", "capex_heavy_project_pre_revenue", "dilution_risk"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Strategic metals plant is Stage 2 watch, while tender offer, buyback, and share issuance are event-premium/4B-4C monitoring.",
    ),
    Round195CaseCandidate(
        case_id="posco_holdings_lithium_resource_security_cycle_watch",
        symbol="005490",
        company_name="POSCO홀딩스",
        primary_archetype=E2RArchetype.LITHIUM_BATTERY_RAW_MATERIAL,
        secondary_archetypes=(E2RArchetype.RARE_METALS_PRICE_FLOOR_OFFTAKE, E2RArchetype.LITHIUM_CYCLE_OVERLAY),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2025, 11, 11),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_lithium_margin_offtake_fcf_project_execution",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("minres_lithium_jv_30pct_stake", "wodgina_mt_marion_spodumene_exposure", "raw_material_security"),
        red_flag_fields=("lithium_price_cycle", "project_execution_risk", "downstream_margin_unverified", "fcf_unverified"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Lithium resource security can be Stage 2, but lithium price rebound alone is not Stage 3 without margin, offtake, and FCF.",
    ),
    Round195CaseCandidate(
        case_id="oci_holdings_spacex_polysilicon_unconfirmed_event_premium",
        symbol="010060",
        company_name="OCI홀딩스",
        primary_archetype=E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION,
        secondary_archetypes=(E2RArchetype.POLYSILICON_REPORT_NOT_CONTRACT, E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY),
        case_type="event_premium",
        stage1_date=date(2026, 4, 14),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="forbidden_unconfirmed_spacex_media_report_without_contract_terms",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("spacex_polysilicon_talks_media_report", "non_china_polysilicon_option", "china_polysilicon_capacity_cut_news"),
        red_flag_fields=("company_could_not_confirm_report", "customer_confirmation_absent", "volume_price_duration_missing", "polysilicon_price_event"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="unknown",
        price_validation_status="needs_ohlc_backfill",
        notes="SpaceX and non-China polysilicon are only Stage 1 attention before confirmed contract, volume, price, duration, margin, and FCF.",
    ),
    Round195CaseCandidate(
        case_id="poongsan_copper_defense_sale_rumor_event_break",
        symbol="103140",
        company_name="풍산",
        primary_archetype=E2RArchetype.COPPER_PROCESSING_PLUS_DEFENSE,
        secondary_archetypes=(E2RArchetype.DEFENSE_AMMO_EVENT_PREMIUM, E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY),
        case_type="event_premium",
        stage1_date=date(2026, 4, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2026, 4, 3),
        stage4c_date=date(2026, 4, 9),
        stage3_decision="forbidden_sale_rumor_without_actual_contract_margin_fcf",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("hanwha_poongsan_ammunition_sale_rumor", "copper_defense_premium", "event_day_price_watch"),
        red_flag_fields=("hanwha_review_stopped", "poongsan_denied_sale_plan", "unconfirmed_restructuring", "event_thesis_break"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Copper plus defense theme is not Green when the sale rumor is denied before actual orders, margin, export contract, and FCF.",
    ),
)


def round195_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND195_CASE_CANDIDATES:
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
                "Round195 R4 Loop-7 materials/spread price-path validation case. "
                "This is calibration-only and must not be used for candidate generation."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "report" in field or "event" in field or "rumor" in field or "expectation" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=(),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "price" in field or "premium" in field or "tender" in field or "event" in field or "lithium" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "loss" in field
                or "oversupply" in field
                or "halt" in field
                or "revision" in field
                or "dilution" in field
                or "denied" in field
                or "break" in field
            ),
            must_have_fields=ROUND195_GREEN_REQUIRED_FIELDS,
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
                "actual_product_spread_delta": 4.0,
                "fcf_after_working_capital_delta": 4.0,
                "supply_discipline_confirmed_delta": 4.0,
                "price_floor_or_offtake_delta": 4.0,
                "cost_curve_advantage_delta": 3.0,
                "commodity_price_up_only_delta": -5.0,
                "tender_offer_or_governance_premium_delta": -4.0,
                "unconfirmed_media_report_delta": -4.0,
                "lithium_price_event_delta": -4.0,
                "capex_heavy_project_pre_revenue_delta": -3.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "needs_ohlc_backfill_true",
                "do_not_invent_price_or_stage_dates",
                *ROUND195_GREEN_REQUIRED_FIELDS,
                *ROUND195_GREEN_FORBIDDEN_PATTERNS,
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


def round195_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND195_CASE_CANDIDATES:
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


def round195_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND195_SCORE_ADJUSTMENTS)


def round195_price_backfill_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round195_backfill": "true"} for field in ROUND195_PRICE_BACKFILL_FIELDS)


def round195_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round195_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND195_REQUIRED_TARGET_ALIASES.items()
    )


def round195_summary() -> dict[str, int | bool]:
    cases = round195_case_records()
    return {
        "case_candidate_count": len(cases),
        "required_target_count": len(ROUND195_REQUIRED_TARGET_ALIASES),
        "score_adjustment_count": len(ROUND195_SCORE_ADJUSTMENTS),
        "price_backfill_field_count": len(ROUND195_PRICE_BACKFILL_FIELDS),
        "cyclical_success_count": sum(1 for case in cases if case.case_type == "cyclical_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in ROUND195_CASE_CANDIDATES if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in ROUND195_CASE_CANDIDATES if case.stage3_date),
        "stage4b_watch_or_elevated_count": sum(
            1 for case in ROUND195_CASE_CANDIDATES if case.stage4b_status in {"watch", "elevated"}
        ),
        "needs_ohlc_backfill_count": sum(1 for case in ROUND195_CASE_CANDIDATES if case.price_validation_status == "needs_ohlc_backfill"),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "needs_ohlc_backfill": True,
    }


def write_round195_r4_loop7_reports(
    *,
    output_directory: str | Path = ROUND195_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND195_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND195_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = write_case_library(round195_case_records(), cases_path)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "audit_json": audit,
        "summary": output / "round195_r4_loop7_price_validation_summary.md",
        "case_matrix": output / "round195_r4_loop7_case_matrix.csv",
        "target_aliases": output / "round195_r4_loop7_target_aliases.csv",
        "score_adjustments": output / "round195_r4_loop7_score_adjustments.csv",
        "price_backfill_fields": output / "round195_r4_loop7_price_backfill_fields.csv",
        "green_gate_review": output / "round195_r4_loop7_green_gate_review.md",
        "price_backfill_plan": output / "round195_r4_loop7_price_backfill_plan.md",
        "stage4b_4c_review": output / "round195_r4_loop7_stage4b_4c_review.md",
    }
    audit.write_text(json.dumps(round195_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round195_case_rows(), paths["case_matrix"])
    _write_rows(round195_target_alias_rows(), paths["target_aliases"])
    _write_rows(round195_score_adjustment_rows(), paths["score_adjustments"])
    _write_rows(round195_price_backfill_field_rows(), paths["price_backfill_fields"])
    paths["summary"].write_text(render_round195_summary_markdown(), encoding="utf-8")
    paths["green_gate_review"].write_text(render_round195_green_gate_review_markdown(), encoding="utf-8")
    paths["price_backfill_plan"].write_text(render_round195_price_backfill_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round195_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def round195_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND195_SOURCE_ROUND_PATH,
        "large_sector": Round10LargeSector.MATERIALS_SPREAD_STRATEGIC.value,
        "summary": round195_summary(),
        "target_aliases": list(round195_target_alias_rows()),
        "green_required_fields": list(ROUND195_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND195_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_statuses": list(ROUND195_STAGE4B_STATUSES),
        "hard_4c_gates": list(ROUND195_HARD_4C_GATES),
        "score_adjustments": list(round195_score_adjustment_rows()),
        "case_ids": [case.case_id for case in ROUND195_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round195_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_commodity_price_or_event_premium_as_green_evidence",
            "do_not_invent_prices_stage_dates_spreads_offtake_margins_or_fcf",
        ],
    }


def render_round195_summary_markdown() -> str:
    summary = round195_summary()
    lines = [
        "# Round-195 R4 Loop-7 Price-Path Validation Summary",
        "",
        f"- source_round: `{ROUND195_SOURCE_ROUND_PATH}`",
        "- large_sector: `MATERIALS_SPREAD_STRATEGIC`",
        "- scope: Korean petrochemical, refining, strategic metals, lithium, polysilicon, and copper-defense event validation",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- score_adjustment_count: {summary['score_adjustment_count']}",
        f"- price_backfill_field_count: {summary['price_backfill_field_count']}",
        f"- cyclical_success_count: {summary['cyclical_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
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
        "- R4는 commodity/event false Green 차단이 핵심이다.",
        "- 롯데케미칼과 LG화학은 구조조정 계획만으로 Green이 아니라 spread, OPM, FCF 확인 전 Stage 2/Watch다.",
        "- SK이노베이션 정유 반전은 cyclical success일 수 있지만, 전쟁성 margin spike는 구조적 Green이 아니다.",
        "- 고려아연은 경영권 event premium과 critical minerals Stage 2 evidence를 분리해야 한다.",
        "- POSCO홀딩스 리튬 지분 확보는 Stage 2 후보지만, 리튬 가격 반등은 Green 근거가 아니다.",
        "- OCI홀딩스 SpaceX 보도와 풍산 방산부문 매각 보도는 미확정 event premium으로 본다.",
        "",
        "쉬운 예: `as_of_date=2026-04-14`에 OCI-SpaceX 보도가 있어도 회사와 고객이 확인하지 않았으면 Stage 3-Green이 아니다. 확인된 계약, 물량, 가격, 기간, 마진, FCF가 필요하다.",
    ]
    return "\n".join(lines) + "\n"


def render_round195_green_gate_review_markdown() -> str:
    lines = [
        "# Round-195 R4 Loop-7 Green Gate Review",
        "",
        "## Green Required Evidence",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND195_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Green Forbidden Patterns", ""])
    lines.extend(f"- `{field}`" for field in ROUND195_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "| --- | --- | ---: | --- |"])
    for adjustment in ROUND195_SCORE_ADJUSTMENTS:
        lines.append(f"| `{adjustment.axis}` | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these weights to production scoring yet.",
            "- Do not use Round195 cases as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds to force promotion.",
            "- Do not invent spreads, offtake, capacity shutdown, margins, stage prices, or MFE/MAE.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round195_price_backfill_plan_markdown() -> str:
    lines = [
        "# Round-195 R4 Loop-7 Price Backfill Plan",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND195_PRICE_BACKFILL_FIELDS)
    lines.extend(["", "## Priority Cases", "", "| case | stage marker | current status | 4B status | hard 4C |", "| --- | --- | --- | --- | --- |"])
    for case in ROUND195_CASE_CANDIDATES:
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
            "- Split event-premium price paths from structural Stage 2 price paths.",
            "- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round195_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round-195 R4 Loop-7 Stage 4B / 4C Review",
        "",
        "## 4B Status Definitions",
        "",
        "- `watch`: commodity, restructuring, tender-offer, or unconfirmed media narrative may be running ahead of FCF.",
        "- `elevated`: inventories, dilution, spread reversal, CAPEX, or event failure becomes material.",
        "- `graduated`: spread peak or event premium is already accepted and new evidence has less rerating power.",
        "",
        "## Hard 4C Gates",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND195_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C confirmed | interpretation |", "| --- | --- | --- | --- |"])
    for case in ROUND195_CASE_CANDIDATES:
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
    "ROUND195_CASE_CANDIDATES",
    "ROUND195_DEFAULT_AUDIT_PATH",
    "ROUND195_DEFAULT_CASES_PATH",
    "ROUND195_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND195_GREEN_FORBIDDEN_PATTERNS",
    "ROUND195_GREEN_REQUIRED_FIELDS",
    "ROUND195_HARD_4C_GATES",
    "ROUND195_PRICE_BACKFILL_FIELDS",
    "ROUND195_REQUIRED_TARGET_ALIASES",
    "ROUND195_SCORE_ADJUSTMENTS",
    "ROUND195_SOURCE_ROUND_PATH",
    "ROUND195_STAGE4B_STATUSES",
    "Round195CaseCandidate",
    "Round195ScoreAdjustment",
    "render_round195_green_gate_review_markdown",
    "render_round195_price_backfill_plan_markdown",
    "render_round195_stage4b_4c_review_markdown",
    "render_round195_summary_markdown",
    "round195_audit_payload",
    "round195_case_records",
    "round195_case_rows",
    "round195_price_backfill_field_rows",
    "round195_score_adjustment_rows",
    "round195_summary",
    "round195_target_alias_rows",
    "write_round195_r4_loop7_reports",
]
