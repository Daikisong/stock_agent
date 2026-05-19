"""Round-205 R1 Loop-8 industrial order and infrastructure price validation.

Round 205 is calibration/evaluation material only. It adds defense,
shipbuilding, MRO, sanction, IPO-premium, and merger-event price-path anchors
from ``docs/round/round_205.md``.

Simple example: HD Hyundai Marine Solution rising about 96% on the first
listed day is a real price path. It is not by itself Stage 3-Green evidence,
because the required backlog, margin, delivery, and EPS conversion evidence is
not yet present as-of that event date.
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


ROUND205_SOURCE_ROUND_PATH = "docs/round/round_205.md"
ROUND205_LARGE_SECTOR = Round10LargeSector.INDUSTRIAL_ORDERS_INFRA
ROUND205_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round205_r1_loop8_industrial_infra_price_validation"
ROUND205_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop8_round205.jsonl"
ROUND205_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round205_r1_loop8_industrial_infra_price_validation_audit.json"

ROUND205_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "DEFENSE_GOVERNMENT_BACKLOG": E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG.value,
    "DEFENSE_LOCAL_PRODUCTION_PLATFORM": E2RArchetype.DEFENSE_LOCAL_PRODUCTION_PLATFORM.value,
    "DEFENSE_INTERCEPTOR_COMBAT_VALIDATION": E2RArchetype.DEFENSE_INTERCEPTOR_COMBAT_VALIDATION.value,
    "DEFENSE_AIRCRAFT_EXPORT_BACKLOG": E2RArchetype.DEFENSE_AIRCRAFT_EXPORT_BACKLOG.value,
    "SHIPBUILDING_OFFSHORE_BACKLOG": E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG.value,
    "SHIP_MRO_RECURRING_PLATFORM": E2RArchetype.SHIP_MRO_RECURRING_PLATFORM.value,
    "GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY": E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY.value,
    "CONTRACT_BACKLOG_INDUSTRIAL": E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "CROWDING_4B_WATCH": E2RArchetype.CROWDED_RERATING_4B_WATCH.value,
    "CROWDED_RERATING_4B_WATCH": E2RArchetype.CROWDED_RERATING_4B_WATCH.value,
    "STRUCTURAL_SUCCESS_BUT_4B_WATCH": E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
    "THESIS_BREAK_4C": E2RArchetype.THESIS_BREAK_4C.value,
}

ROUND205_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "contract_amount_confirmed",
    "contract_duration_or_delivery_schedule_confirmed",
    "actual_delivery_or_revenue_recognition_confirmed",
    "opm_or_eps_revision_confirmed",
    "backlog_quality_confirmed",
    "price_path_after_evidence",
    "sanction_financing_dilution_margin_risk_passed",
)

ROUND205_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "order_headline_only",
    "ipo_first_day_rally",
    "mou_or_preliminary_policy_event",
    "record_high_on_policy_event",
    "contract_without_margin_visibility",
    "policy_theme_only",
)

ROUND205_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "stage3_after_2x_to_5x_return",
    "new_contracts_are_consensus",
    "market_cap_or_record_high_headline",
    "large_capital_raise_or_convertible_bond",
    "ipo_first_day_50_to_100pct_rally",
    "policy_merger_or_mou_record_high",
)

ROUND205_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "financing_failure",
    "delivery_delay_to_earnings_downgrade",
    "sanction_revenue_disruption",
    "margin_collapse",
    "accounting_or_disclosure_trust_break",
    "fatal_safety_or_quality_issue",
)

ROUND205_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_price",
    "reported_mfe_minimum_pct",
    "mfe_1d",
    "mfe_1d_secondary",
    "mae_1d",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round205ScoreAdjustment:
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
class Round205CaseCandidate:
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
    reported_mfe_minimum_pct: float | None
    mfe_1d: float | None
    mfe_1d_secondary: float | None
    mae_1d: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    peak_price_anchor: float | None
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND205_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND205_SCORE_ADJUSTMENTS: tuple[Round205ScoreAdjustment, ...] = (
    Round205ScoreAdjustment("contract_amount_to_sales", 4, "raise", "계약금액/매출 비율이 확인된 수주형 사례를 더 강하게 본다."),
    Round205ScoreAdjustment("delivery_schedule", 4, "raise", "납품 일정이 있어야 수주가 매출로 이어질 수 있다."),
    Round205ScoreAdjustment("order_to_revenue_conversion", 5, "raise", "수주 헤드라인보다 실제 매출 전환을 보상한다."),
    Round205ScoreAdjustment("op_eps_revision", 5, "raise", "수주가 OP/EPS 상향으로 연결될 때 Stage 3 근거가 된다."),
    Round205ScoreAdjustment("government_backlog", 4, "raise", "정부 고객과 다년 backlog는 방산 visibility를 높인다."),
    Round205ScoreAdjustment("combat_validation", 3, "raise", "실전 검증은 방공/요격체계 수요 확률을 높인다."),
    Round205ScoreAdjustment("local_production_or_technology_transfer", 3, "raise", "현지생산/기술이전은 방산 수주 지속성을 높인다."),
    Round205ScoreAdjustment("price_path_alignment", 5, "raise", "Stage 2/3 증거 이후 가격경로가 맞는지 검증한다."),
    Round205ScoreAdjustment("order_headline_only", -4, "lower", "수주 기사만 있고 마진·납품·EPS가 없으면 Green 금지다."),
    Round205ScoreAdjustment("ipo_first_day_rally", -5, "lower", "IPO 첫날 급등은 수주/FCF 증거가 아니므로 4B-watch다."),
    Round205ScoreAdjustment("mou_or_preliminary_policy_event", -4, "lower", "MOU·정책 예비 이벤트는 매출 전환 전까지 Stage 1/2에 둔다."),
    Round205ScoreAdjustment("record_high_on_policy_event", -3, "lower", "정책/합병 이벤트 신고가는 evidence-before-price가 아닐 수 있다."),
    Round205ScoreAdjustment("contract_without_margin_visibility", -3, "lower", "계약이 있어도 마진 visibility가 없으면 Green을 막는다."),
    Round205ScoreAdjustment("geopolitical_exposure_unpriced", -3, "lower", "제재·지정학 리스크가 매출을 흔들 수 있으면 RedTeam에 반영한다."),
)


ROUND205_CASE_CANDIDATES: tuple[Round205CaseCandidate, ...] = (
    Round205CaseCandidate(
        case_id="r1_loop8_hyundai_rotem_k2_aligned",
        symbol="064350",
        company_name="현대로템",
        primary_archetype=E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,
        secondary_archetypes=(E2RArchetype.DEFENSE_LOCAL_PRODUCTION_PLATFORM,),
        case_type="structural_success",
        stage1_date=date(2024, 4, 9),
        stage2_date=date(2024, 4, 9),
        stage3_date=date(2024, 4, 9),
        stage4b_date=date(2025, 8, 1),
        stage4c_date=None,
        stage3_decision="aligned_defense_government_backlog_with_local_production_and_later_large_mfe",
        stage4b_status="elevated",
        hard_4c_confirmed=False,
        evidence_fields=("k2_export_backlog", "government_customer", "local_production_platform", "delivery_schedule", "op_eps_revision", "reported_stage3_price_41300"),
        red_flag_fields=("post_large_mfe_crowding_watch", "new_orders_becoming_consensus"),
        price_data_source="WSJ/FT reported price and return anchors",
        reported_price_anchor="WSJ reported trading price 41,300 KRW",
        reported_return_anchor="FT reported more than sixfold one-year subperiod",
        reported_mfe_minimum_pct=500.0,
        mfe_1d=None,
        mfe_1d_secondary=None,
        mae_1d=None,
        stage2_price_anchor=41300.0,
        stage3_price_anchor=41300.0,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="green_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="K2 export and local-production visibility align with the later reported multi-bagger price path; after the large run it becomes 4B-watch/elevated.",
    ),
    Round205CaseCandidate(
        case_id="r1_loop8_hanwha_aerospace_mfe_4b",
        symbol="012450",
        company_name="한화에어로스페이스",
        primary_archetype=E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH,
        secondary_archetypes=(E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="structural_success",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 3, 21),
        stage4c_date=None,
        stage3_decision="structural_defense_success_but_by_reported_peak_it_is_4b_watch_not_fresh_green",
        stage4b_status="elevated",
        hard_4c_confirmed=False,
        evidence_fields=("defense_export_backlog", "government_customer", "multi_year_delivery", "op_eps_revision", "reported_price_path_187500_to_1435000"),
        red_flag_fields=("reported_large_mfe_665pct", "one_day_mae_after_capital_event", "crowding_watch"),
        price_data_source="reported market price path anchor",
        reported_price_anchor="187,500 KRW to 1,435,000 KRW",
        reported_return_anchor="reported MFE +665.3%; one-day MAE -13%",
        reported_mfe_minimum_pct=665.3,
        mfe_1d=None,
        mfe_1d_secondary=None,
        mae_1d=-13.0,
        stage2_price_anchor=None,
        stage3_price_anchor=187500.0,
        stage4b_price_anchor=1435000.0,
        stage4c_price_anchor=None,
        peak_price_anchor=1435000.0,
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="green_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Aligned defense rerating benchmark; the post-MFE posture is 4B-watch/elevated unless backlog/EPS thesis breaks.",
    ),
    Round205CaseCandidate(
        case_id="r1_loop8_lig_nex1_cheongung_watch",
        symbol="079550",
        company_name="LIG넥스원",
        primary_archetype=E2RArchetype.DEFENSE_INTERCEPTOR_COMBAT_VALIDATION,
        secondary_archetypes=(E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,),
        case_type="success_candidate",
        stage1_date=date(2024, 9, 19),
        stage2_date=date(2024, 9, 19),
        stage3_date=None,
        stage4b_date=date(2026, 3, 11),
        stage4c_date=None,
        stage3_decision="stage2_watch_success_until_interceptor_contract_and_eps_conversion_are_complete",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("cheongung_export_deal", "combat_validation", "government_customer", "reported_war_period_return_47pct"),
        red_flag_fields=("stage3_contract_duration_incomplete", "eps_conversion_needs_confirmation"),
        price_data_source="reported event and war-period return anchors",
        reported_price_anchor="Iraq deal event +3.6% one day; later war-period +47%",
        reported_return_anchor="+3.6% one day; +47% war-period",
        reported_mfe_minimum_pct=47.0,
        mfe_1d=3.6,
        mfe_1d_secondary=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Combat validation improves the watch case, but Stage 3 needs contract duration, backlog, and OP/EPS conversion evidence.",
    ),
    Round205CaseCandidate(
        case_id="r1_loop8_kai_fa50_stage2",
        symbol="047810",
        company_name="한국항공우주",
        primary_archetype=E2RArchetype.DEFENSE_AIRCRAFT_EXPORT_BACKLOG,
        secondary_archetypes=(E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,),
        case_type="success_candidate",
        stage1_date=date(2025, 6, 4),
        stage2_date=date(2025, 6, 4),
        stage3_date=None,
        stage4b_date=date(2026, 3, 11),
        stage4c_date=None,
        stage3_decision="stage2_watch_success_until_fa50_delivery_margin_and_eps_path_are_confirmed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("fa50_export_backlog", "government_customer", "aircraft_delivery_schedule", "reported_stock_tripled_1y"),
        red_flag_fields=("margin_visibility_needed", "delivery_schedule_to_revenue_needed"),
        price_data_source="reported one-year return anchor",
        reported_price_anchor="stock about tripled over one year",
        reported_return_anchor="reported MFE about +200%",
        reported_mfe_minimum_pct=200.0,
        mfe_1d=None,
        mfe_1d_secondary=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Aircraft export backlog is a valid Stage 2 watch case; Green waits for margin, delivery, and EPS visibility.",
    ),
    Round205CaseCandidate(
        case_id="r1_loop8_hd_hyundai_marine_ipo_premium",
        symbol="443060",
        company_name="HD현대마린솔루션",
        primary_archetype=E2RArchetype.SHIP_MRO_RECURRING_PLATFORM,
        secondary_archetypes=(E2RArchetype.PRICE_ONLY_RALLY, E2RArchetype.EVENT_PREMIUM),
        case_type="overheat",
        stage1_date=date(2024, 5, 8),
        stage2_date=date(2024, 5, 8),
        stage3_date=None,
        stage4b_date=date(2024, 5, 8),
        stage4c_date=None,
        stage3_decision="ipo_first_day_premium_is_not_structural_green_without_mro_revenue_and_margin_path",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ship_mro_platform", "ipo_first_day_price_path", "reported_first_day_close_163900"),
        red_flag_fields=("ipo_first_day_rally", "price_before_evidence", "mro_recurring_revenue_needs_confirmation"),
        price_data_source="reported IPO first-day price anchor",
        reported_price_anchor="IPO price 83,400 KRW; first-day close 163,900 KRW",
        reported_return_anchor="first-day close +96.5%",
        reported_mfe_minimum_pct=96.5,
        mfe_1d=96.5,
        mfe_1d_secondary=None,
        mae_1d=None,
        stage2_price_anchor=83400.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=163900.0,
        stage4c_price_anchor=None,
        peak_price_anchor=163900.0,
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="MRO can become recurring visibility, but IPO first-day repricing itself is event premium and must not create Green.",
    ),
    Round205CaseCandidate(
        case_id="r1_loop8_hanwha_ocean_china_sanction",
        symbol="042660",
        company_name="한화오션",
        primary_archetype=E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION_OVERLAY,
        secondary_archetypes=(E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG, E2RArchetype.THESIS_BREAK_4C),
        case_type="4b_watch",
        stage1_date=date(2025, 10, 14),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 10, 14),
        stage3_decision="sanction_watch_is_redteam_overlay_not_hard_4c_until_revenue_or_financing_disruption_is_confirmed",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("shipbuilding_backlog_context", "china_sanction_event", "reported_one_day_drop"),
        red_flag_fields=("geopolitical_exposure_unpriced", "sanction_revenue_disruption_watch", "financing_or_contract_disruption_needs_confirmation"),
        price_data_source="reported sanction-event one-day return anchor",
        reported_price_anchor="China sanction event one-day return",
        reported_return_anchor="-5.8% one day",
        reported_mfe_minimum_pct=None,
        mfe_1d=None,
        mfe_1d_secondary=None,
        mae_1d=-5.8,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        score_price_alignment="unknown",
        rerating_result="no_rerating",
        stage_failure_type="unknown",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="This is a 4C-watch overlay. Hard 4C requires confirmed revenue disruption, financing failure, or contract cancellation.",
    ),
    Round205CaseCandidate(
        case_id="r1_loop8_hd_hyundai_heavy_mipo_merger_4b",
        symbol="329180/010620",
        company_name="HD현대중공업/HD현대미포",
        primary_archetype=E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="success_candidate",
        stage1_date=date(2025, 8, 27),
        stage2_date=date(2025, 8, 27),
        stage3_date=None,
        stage4b_date=date(2025, 8, 27),
        stage4c_date=None,
        stage3_decision="shipbuilding_policy_or_merger_event_is_stage2_watch_until_margin_and_orderbook_conversion_are_verified",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("shipbuilding_backlog_cycle", "merger_or_policy_event", "reported_heavy_plus_11_3pct", "reported_mipo_plus_14_6pct"),
        red_flag_fields=("record_high_on_policy_event", "price_before_margin_conversion", "merger_event_premium_watch"),
        price_data_source="reported merger-event one-day return anchors",
        reported_price_anchor="HD Hyundai Heavy +11.3%; HD Hyundai Mipo +14.6%",
        reported_return_anchor="+11.3% and +14.6% one day",
        reported_mfe_minimum_pct=14.6,
        mfe_1d=11.3,
        mfe_1d_secondary=14.6,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        score_price_alignment="unknown",
        rerating_result="policy_event_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Shipbuilding can be a valid Stage 2 watch, but a merger/policy event rally is not fresh Green before orderbook quality and margin conversion are confirmed.",
    ),
)


def round205_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND205_CASE_CANDIDATES:
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
                "Round205 R1 Loop-8 industrial orders, defense backlog, "
                "shipbuilding/MRO, sanction, IPO premium, and merger-event "
                "price-path validation case. Calibration-only."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "event" in field or "reported" in field or "deal" in field or "backlog" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "backlog" in field
                or "delivery" in field
                or "op_eps" in field
                or "government_customer" in field
                or "local_production" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "mfe" in field
                or "rally" in field
                or "crowding" in field
                or "record_high" in field
                or "ipo" in field
                or "price_before" in field
                or "event_premium" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "sanction" in field
                or "disruption" in field
                or "cancellation" in field
                or "failure" in field
                or "margin_collapse" in field
            ),
            must_have_fields=ROUND205_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"overheat", "event_premium", "4b_watch", "4c_thesis_break", "failed_rerating"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={
                "contract_amount_to_sales_delta": 4.0,
                "delivery_schedule_delta": 4.0,
                "order_to_revenue_conversion_delta": 5.0,
                "op_eps_revision_delta": 5.0,
                "government_backlog_delta": 4.0,
                "combat_validation_delta": 3.0,
                "local_production_or_technology_transfer_delta": 3.0,
                "price_path_alignment_delta": 5.0,
                "order_headline_only_delta": -4.0,
                "ipo_first_day_rally_delta": -5.0,
                "mou_or_preliminary_policy_event_delta": -4.0,
                "record_high_on_policy_event_delta": -3.0,
                "contract_without_margin_visibility_delta": -3.0,
                "geopolitical_exposure_unpriced_delta": -3.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_order_headline_ipo_mou_policy_or_record_high_event_as_green_evidence",
                *ROUND205_GREEN_REQUIRED_FIELDS,
                *ROUND205_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_price=candidate.peak_price_anchor,
                peak_return_from_stage3=candidate.reported_mfe_minimum_pct,
                mfe_30d=candidate.mfe_1d,
                mfe_1y=candidate.reported_mfe_minimum_pct,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.85 if candidate.stage3_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round205_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND205_CASE_CANDIDATES:
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
                "reported_mfe_minimum_pct": _float_text(candidate.reported_mfe_minimum_pct),
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mfe_1d_secondary": _float_text(candidate.mfe_1d_secondary),
                "mae_1d": _float_text(candidate.mae_1d),
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


def round205_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND205_SCORE_ADJUSTMENTS)


def round205_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round205_price_validation": "true"} for field in ROUND205_PRICE_VALIDATION_FIELDS)


def round205_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round205_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND205_REQUIRED_TARGET_ALIASES.items()
    )


def round205_summary() -> dict[str, int | bool | str]:
    records = round205_case_records()
    return {
        "case_candidate_count": len(records),
        "required_target_count": len(ROUND205_REQUIRED_TARGET_ALIASES),
        "score_adjustment_count": len(ROUND205_SCORE_ADJUSTMENTS),
        "price_validation_field_count": len(ROUND205_PRICE_VALIDATION_FIELDS),
        "structural_success_count": sum(1 for case in records if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in records if case.case_type == "success_candidate"),
        "overheat_or_watch_count": sum(1 for case in records if case.case_type in {"overheat", "4b_watch"}),
        "hard_4c_case_count": sum(1 for case in ROUND205_CASE_CANDIDATES if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in ROUND205_CASE_CANDIDATES if case.stage3_date),
        "stage4b_watch_or_elevated_count": sum(
            1 for case in ROUND205_CASE_CANDIDATES if case.stage4b_status in {"watch", "elevated"}
        ),
        "reported_price_anchor_count": sum(
            1 for case in ROUND205_CASE_CANDIDATES if case.price_validation_status != "needs_ohlc_backfill"
        ),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
    }


def write_round205_r1_loop8_reports(
    *,
    output_directory: str | Path = ROUND205_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND205_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND205_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = write_case_library(round205_case_records(), cases_path)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "audit_json": audit,
        "summary": output / "round205_r1_loop8_price_validation_summary.md",
        "case_matrix": output / "round205_r1_loop8_case_matrix.csv",
        "target_aliases": output / "round205_r1_loop8_target_aliases.csv",
        "score_adjustments": output / "round205_r1_loop8_score_adjustments.csv",
        "price_validation_fields": output / "round205_r1_loop8_price_validation_fields.csv",
        "green_gate_review": output / "round205_r1_loop8_green_gate_review.md",
        "price_validation_plan": output / "round205_r1_loop8_price_validation_plan.md",
        "stage4b_4c_review": output / "round205_r1_loop8_stage4b_4c_review.md",
    }
    audit.write_text(json.dumps(round205_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round205_case_rows(), paths["case_matrix"])
    _write_rows(round205_target_alias_rows(), paths["target_aliases"])
    _write_rows(round205_score_adjustment_rows(), paths["score_adjustments"])
    _write_rows(round205_price_validation_field_rows(), paths["price_validation_fields"])
    paths["summary"].write_text(render_round205_summary_markdown(), encoding="utf-8")
    paths["green_gate_review"].write_text(render_round205_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round205_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round205_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def round205_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND205_SOURCE_ROUND_PATH,
        "large_sector": ROUND205_LARGE_SECTOR.value,
        "summary": round205_summary(),
        "target_aliases": list(round205_target_alias_rows()),
        "green_required_fields": list(ROUND205_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND205_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND205_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND205_HARD_4C_GATES),
        "score_adjustments": list(round205_score_adjustment_rows()),
        "case_ids": [case.case_id for case in ROUND205_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round205_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_order_headline_ipo_mou_policy_or_record_high_event_as_green_evidence",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
            "keep_full_ohlc_complete_false_until_official_backfill_is_done",
        ],
    }


def render_round205_summary_markdown() -> str:
    summary = round205_summary()
    lines = [
        "# Round-205 R1 Loop-8 Price-Path Validation Summary",
        "",
        f"- source_round: `{ROUND205_SOURCE_ROUND_PATH}`",
        f"- large_sector: `{ROUND205_LARGE_SECTOR.value}`",
        "- scope: defense backlog, combat validation, aircraft export, shipbuilding/MRO, IPO premium, sanction watch, and merger-event price anchors",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- score_adjustment_count: {summary['score_adjustment_count']}",
        f"- price_validation_field_count: {summary['price_validation_field_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- overheat_or_watch_count: {summary['overheat_or_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- stage3_case_count: {summary['stage3_case_count']}",
        f"- stage4b_watch_or_elevated_count: {summary['stage4b_watch_or_elevated_count']}",
        f"- reported_price_anchor_count: {summary['reported_price_anchor_count']}",
        "- production_scoring_changed: false",
        "- candidate_generation_input: false",
        "- shadow_weight_only: true",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Interpretation",
        "",
        "- 현대로템과 한화에어로스페이스는 방산 backlog/납품 visibility가 실제 큰 가격경로와 맞았던 aligned benchmark다.",
        "- LIG넥스원과 한국항공우주는 Stage 2 watch 성공 사례지만, Stage 3-Green에는 계약기간·납품·마진·EPS 전환 확인이 더 필요하다.",
        "- HD현대마린솔루션 IPO 첫날 급등은 MRO 플랫폼 가능성과 별개로 price-before-evidence 이벤트다.",
        "- 한화오션 중국 제재는 hard 4C가 아니라 4C-watch다. 매출 차질, 금융 실패, 계약 취소가 확인되어야 hard 4C다.",
        "- HD현대중공업/현대미포 이벤트 급등은 조선 Stage 2 watch 가능성이지만, 합병/정책 이벤트만으로 Green은 만들지 않는다.",
        "",
        "쉬운 예: `as_of_date=2024-05-08`에 IPO 첫날 96% 급등이 보여도, 그날 확인 가능한 MRO 반복매출·마진·EPS 상향이 없으면 Stage 3-Green 근거가 아니라 이벤트 프리미엄이다.",
    ]
    return "\n".join(lines) + "\n"


def render_round205_green_gate_review_markdown() -> str:
    lines = [
        "# Round-205 R1 Loop-8 Green Gate Review",
        "",
        "## Green Required Evidence",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND205_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Green Forbidden Patterns", ""])
    lines.extend(f"- `{field}`" for field in ROUND205_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "| --- | --- | ---: | --- |"])
    for adjustment in ROUND205_SCORE_ADJUSTMENTS:
        lines.append(f"| `{adjustment.axis}` | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these weights to production scoring yet.",
            "- Do not use Round205 cases as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds to force promotion.",
            "- Do not invent full OHLC, stage prices, or MFE/MAE when only reported anchors exist.",
            "- Do not treat order headlines, IPO rallies, MOU/policy events, or record-high event moves as Green evidence alone.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round205_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-205 R1 Loop-8 Price Validation Plan",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND205_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | price data source | reported anchor | status |", "| --- | --- | --- | --- |"])
    for case in ROUND205_CASE_CANDIDATES:
        lines.append(
            f"| `{case.case_id}` | {case.price_data_source} | {case.reported_return_anchor} | `{case.price_validation_status}` |"
        )
    lines.extend(
        [
            "",
            "## Backfill Rule",
            "",
            "- Use reported media anchors only for fields they explicitly support.",
            "- Keep full OHLC unavailable until official or adjusted daily price backfill is done.",
            "- Separate Stage 2 watch, Stage 3 anchor, 4B event, and 4C-watch event.",
            "- Do not promote event price jumps to Green without backlog, delivery, margin, and OP/EPS evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round205_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round-205 R1 Loop-8 Stage 4B / 4C Review",
        "",
        "## 4B Watch Triggers",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND205_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- `{field}`" for field in ROUND205_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## R1 Loop-8 Interpretation",
            "",
            "- Stage 3 이후 2~5배 이상 오른 방산 성공주는 신규 Green보다 4B-watch/elevated로 본다.",
            "- IPO 첫날 50~100% 급등은 반복매출·마진·EPS 전환 전까지 이벤트 프리미엄이다.",
            "- 제재 뉴스는 4C-watch일 수 있지만, 매출 차질·계약취소·금융 실패가 확인되어야 hard 4C다.",
            "- 정책/합병/MOU 이벤트 신고가는 orderbook quality와 margin conversion이 확인되기 전까지 Green 근거가 아니다.",
            "",
            "## Case Review",
            "",
            "| case | 4B status | hard 4C confirmed | interpretation |",
            "| --- | --- | --- | --- |",
        ]
    )
    for case in ROUND205_CASE_CANDIDATES:
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


def _float_text(value: float | None) -> str:
    return "" if value is None else str(value)


__all__ = [
    "ROUND205_CASE_CANDIDATES",
    "ROUND205_DEFAULT_AUDIT_PATH",
    "ROUND205_DEFAULT_CASES_PATH",
    "ROUND205_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND205_GREEN_FORBIDDEN_PATTERNS",
    "ROUND205_GREEN_REQUIRED_FIELDS",
    "ROUND205_HARD_4C_GATES",
    "ROUND205_PRICE_VALIDATION_FIELDS",
    "ROUND205_REQUIRED_TARGET_ALIASES",
    "ROUND205_SCORE_ADJUSTMENTS",
    "ROUND205_SOURCE_ROUND_PATH",
    "ROUND205_STAGE4B_WATCH_TRIGGERS",
    "Round205CaseCandidate",
    "Round205ScoreAdjustment",
    "render_round205_green_gate_review_markdown",
    "render_round205_price_validation_plan_markdown",
    "render_round205_stage4b_4c_review_markdown",
    "render_round205_summary_markdown",
    "round205_audit_payload",
    "round205_case_records",
    "round205_case_rows",
    "round205_price_validation_field_rows",
    "round205_score_adjustment_rows",
    "round205_summary",
    "round205_target_alias_rows",
    "write_round205_r1_loop8_reports",
]
