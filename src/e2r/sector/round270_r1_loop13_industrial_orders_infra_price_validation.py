"""Round-270 R1 Loop-13 industrial orders/infrastructure validation pack.

Round 270 converts ``docs/round/round_270.md`` into structured,
calibration-only case records. It does not change production scoring.

Easy example: a shipbuilder can jump 15% on a merger or MASGA headline, but
that is not Stage 3. R1 Green needs the chain to close as contract -> delivery
-> margin -> working capital -> cash collection, with sanction/counterparty risk
cleared.
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


ROUND270_SOURCE_ROUND_PATH = "docs/round/round_270.md"
ROUND270_ANALYST_ROUND_ID = "round_198"
ROUND270_LARGE_SECTOR = "INDUSTRIAL_ORDERS_INFRA"
ROUND270_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round270_r1_loop13_industrial_orders_infra_price_validation"
ROUND270_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop13_round270.jsonl"
ROUND270_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round270_r1_loop13_industrial_orders_infra_price_validation_audit.json"

ROUND270_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION": E2RArchetype.US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION.value,
    "SHIPBUILDING_GEOPOLITICAL_SANCTION_4C": E2RArchetype.SHIPBUILDING_GEOPOLITICAL_SANCTION_4C.value,
    "SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C": E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C.value,
    "RAIL_EXPORT_MEGA_ORDER_STAGE2": E2RArchetype.RAIL_EXPORT_MEGA_ORDER_STAGE2.value,
    "MARINE_AFTERMARKET_RECURRING_SERVICE": E2RArchetype.MARINE_AFTERMARKET_RECURRING_SERVICE.value,
    "INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION": E2RArchetype.INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION.value,
    "DEFENSE_AEROSPACE_EXPORT_OPTIONALITY": E2RArchetype.DEFENSE_AEROSPACE_EXPORT_OPTIONALITY.value,
    "SHIPBUILDING_CONTRACT_CYCLE_4B": E2RArchetype.SHIPBUILDING_CONTRACT_CYCLE_4B.value,
}

ROUND270_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "final_contract_signed",
    "delivery_schedule_or_construction_milestone_confirmed",
    "backlog_margin_quality_confirmed",
    "working_capital_advance_payment_receivables_checked",
    "cash_collection_confirmed",
    "counterparty_sanction_legal_export_control_risk_passed",
    "recurring_service_revenue_and_margin_confirmed",
    "integration_synergy_and_fcf_confirmed",
    "actual_robot_order_and_revenue_confirmed",
    "price_path_after_evidence",
)

ROUND270_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "order_headline_only",
    "mou_only",
    "merger_headline_only",
    "ipo_pop_only",
    "strategic_stake_only",
    "defense_sector_ytd_rally_only",
    "us_shipbuilding_policy_theme_only",
    "contract_cancellation_present",
    "sanction_legal_counterparty_risk_unresolved",
)

ROUND270_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "shipbuilder_order_cycle_day_move_plus_10_to_16pct",
    "ipo_day_plus_40_to_100pct",
    "merger_masga_headline_record_high",
    "defense_stock_ytd_plus_50_to_130pct",
    "strategic_equity_stake_robotics_rerating",
    "us_shipbuilding_policy_priced_before_award",
    "sector_order_cycle_priced_before_company_cash_conversion",
)

ROUND270_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "counterparty_illegal_termination",
    "sanctioned_customer_or_subsidiary",
    "arbitration_or_advance_payment_dispute",
    "export_control_or_port_fee_retaliation",
    "delivery_impossible_due_war_or_sanctions",
    "shipyard_safety_or_labor_stoppage",
    "mna_integration_failure",
    "ipo_proceeds_misuse_or_aftermarket_margin_collapse",
    "robotics_order_failure_after_strategic_investment",
)

ROUND270_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "mfe_30d",
    "mae_30d",
    "contract_value_anchor",
    "order_or_ipo_or_merger_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round270ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round270ShadowWeightRow:
    archetype: E2RArchetype
    final_contract_quality: int
    delivery_schedule: int
    backlog_margin_quality: int
    cash_collection: int
    counterparty_sanction_check: int
    recurring_service_revenue: int
    aftermarket_margin: int
    naval_mro_award: int
    integration_synergy: int
    actual_robot_order_revenue: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "final_contract_quality": _signed(self.final_contract_quality),
            "delivery_schedule": _signed(self.delivery_schedule),
            "backlog_margin_quality": _signed(self.backlog_margin_quality),
            "cash_collection": _signed(self.cash_collection),
            "counterparty_sanction_check": _signed(self.counterparty_sanction_check),
            "recurring_service_revenue": _signed(self.recurring_service_revenue),
            "aftermarket_margin": _signed(self.aftermarket_margin),
            "naval_mro_award": _signed(self.naval_mro_award),
            "integration_synergy": _signed(self.integration_synergy),
            "actual_robot_order_revenue": _signed(self.actual_robot_order_revenue),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round270DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round270CaseCandidate:
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


ROUND270_SCORE_ADJUSTMENTS: tuple[Round270ScoreAdjustment, ...] = (
    Round270ScoreAdjustment("final_contract_quality", 5, "raise", "수주 금액보다 최종 계약 질과 이행 가능성이 중요하다."),
    Round270ScoreAdjustment("delivery_schedule_visibility", 5, "raise", "납품·공정 일정이 있어야 매출 인식 경로가 닫힌다."),
    Round270ScoreAdjustment("backlog_margin_quality", 5, "raise", "수주잔고가 있어도 마진이 안 보이면 Green이 아니다."),
    Round270ScoreAdjustment("cash_collection_quality", 5, "raise", "산업재는 현금회수까지 확인해야 FCF 체급 변화가 된다."),
    Round270ScoreAdjustment("counterparty_sanction_check", 5, "raise", "러시아·중국 제재처럼 거래상대방 리스크는 hard gate다."),
    Round270ScoreAdjustment("recurring_service_revenue", 4, "raise", "선박 after-market은 반복 서비스 매출이 확인될 때 가치를 둔다."),
    Round270ScoreAdjustment("aftermarket_margin_visibility", 4, "raise", "서비스 매출도 마진 지속성이 없으면 IPO pop에 그친다."),
    Round270ScoreAdjustment("naval_MRO_contract_award", 5, "raise", "U.S. naval/MRO option은 실제 award가 나와야 Stage 3 후보가 된다."),
    Round270ScoreAdjustment("integration_synergy_realization", 4, "raise", "합병은 통합 시너지와 FCF가 확인되어야 한다."),
    Round270ScoreAdjustment("actual_robot_order_revenue", 5, "raise", "전략 지분투자는 로봇 주문·매출로 전환되어야 한다."),
    Round270ScoreAdjustment("order_headline_only", -5, "lower", "수주 headline만으로는 Green 금지다."),
    Round270ScoreAdjustment("MOU_or_merger_headline_only", -5, "lower", "MOU·합병 headline은 Stage 2 이상으로 자동 승격하지 않는다."),
    Round270ScoreAdjustment("IPO_pop_only", -5, "lower", "IPO 첫날 급등은 4B-watch이지 Green 근거가 아니다."),
    Round270ScoreAdjustment("defense_sector_rerating_only", -4, "lower", "방산 섹터 랠리는 회사별 납품·마진 증거와 분리한다."),
    Round270ScoreAdjustment("strategic_equity_investment_only", -4, "lower", "전략 지분투자는 매출이 아니므로 로봇 Green을 만들 수 없다."),
    Round270ScoreAdjustment("US_shipbuilding_policy_theme_only", -4, "lower", "MASGA 정책협력 기대는 실제 계약 전까지 Stage 2/4B-watch다."),
    Round270ScoreAdjustment("counterparty_sanction_risk", -5, "lower", "제재·상대방 리스크가 열려 있으면 Green을 막는다."),
    Round270ScoreAdjustment("contract_cancellation_risk", -5, "lower", "수주취소는 R1 hard 4C다."),
    Round270ScoreAdjustment("geopolitical_port_fee_risk", -4, "lower", "항만 수수료·제재 보복은 조선 Green gate에 포함한다."),
)


ROUND270_SHADOW_WEIGHT_ROWS: tuple[Round270ShadowWeightRow, ...] = (
    Round270ShadowWeightRow(E2RArchetype.US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION, 4, 4, 5, 5, 5, 2, 2, 5, 5, 0, -5, 5, 5, "HD Hyundai Heavy/Mipo merger is Stage 2; actual U.S. awards and integration needed."),
    Round270ShadowWeightRow(E2RArchetype.SHIPBUILDING_GEOPOLITICAL_SANCTION_4C, 4, 4, 5, 5, 5, 2, 2, 5, 3, 0, 0, 4, 5, "Hanwha Ocean U.S. option is good but China sanctions create 4C-watch."),
    Round270ShadowWeightRow(E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 3, 5, "Samsung Heavy Zvezda cancellation is hard 4C."),
    Round270ShadowWeightRow(E2RArchetype.RAIL_EXPORT_MEGA_ORDER_STAGE2, 5, 5, 5, 5, 4, 1, 1, 0, 0, 0, -5, 4, 4, "Hyundai Rotem Morocco order needs delivery, localization, margin, FX and cash collection."),
    Round270ShadowWeightRow(E2RArchetype.MARINE_AFTERMARKET_RECURRING_SERVICE, 3, 3, 4, 5, 3, 5, 5, 2, 2, 0, -5, 5, 3, "HD Hyundai Marine after-market model is attractive but IPO pop is 4B."),
    Round270ShadowWeightRow(E2RArchetype.INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION, 2, 2, 3, 4, 2, 3, 3, 0, 4, 5, -4, 5, 4, "Rainbow/Samsung stake is Stage 2 until robot orders/revenue/margin confirm."),
    Round270ShadowWeightRow(E2RArchetype.DEFENSE_AEROSPACE_EXPORT_OPTIONALITY, 5, 5, 5, 5, 4, 1, 1, 0, 0, 0, -4, 5, 4, "KAI needs company-specific contracts/delivery/cash collection; sector rally is not Green."),
    Round270ShadowWeightRow(E2RArchetype.SHIPBUILDING_CONTRACT_CYCLE_4B, 4, 4, 5, 5, 4, 2, 2, 0, 1, 0, -5, 5, 4, "Broad shipbuilder rally is cyclical success but not individual Stage 3."),
)


ROUND270_DEEP_SUB_ARCHETYPES: tuple[Round270DeepSubArchetype, ...] = (
    Round270DeepSubArchetype("조선·해양 MASGA", E2RArchetype.US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION, ("HD Hyundai Heavy", "HD Hyundai Mipo", "MASGA", "U.S. naval", "icebreaker", "merger")),
    Round270DeepSubArchetype("조선 지정학 4C-watch", E2RArchetype.SHIPBUILDING_GEOPOLITICAL_SANCTION_4C, ("Hanwha Ocean", "Philly Shipyard", "U.S. Navy MRO", "China sanctions", "five subsidiaries")),
    Round270DeepSubArchetype("수주취소 hard 4C", E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C, ("Samsung Heavy", "Zvezda", "icebreaker LNG carrier", "contract cancellation", "arbitration")),
    Round270DeepSubArchetype("철도 수출", E2RArchetype.RAIL_EXPORT_MEGA_ORDER_STAGE2, ("Hyundai Rotem", "Morocco ONCF", "World Cup", "110 urban trains", "delivery margin cash")),
    Round270DeepSubArchetype("선박 after-market", E2RArchetype.MARINE_AFTERMARKET_RECURRING_SERVICE, ("HD Hyundai Marine Solution", "ship repair", "retrofit", "after-sales service", "IPO 4B")),
    Round270DeepSubArchetype("산업 로봇 옵션", E2RArchetype.INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION, ("Rainbow Robotics", "Samsung largest shareholder", "Future Robotics Office", "actual robot order")),
    Round270DeepSubArchetype("항공우주 방산 옵션", E2RArchetype.DEFENSE_AEROSPACE_EXPORT_OPTIONALITY, ("KAI", "FA-50", "KF-21", "Europe rearmament", "sector rally")),
    Round270DeepSubArchetype("조선 broad cycle", E2RArchetype.SHIPBUILDING_CONTRACT_CYCLE_4B, ("Samsung Heavy", "Hanwha Ocean", "HD Hyundai Heavy", "Clarksons", "newbuilding prices")),
)


ROUND270_CASE_CANDIDATES: tuple[Round270CaseCandidate, ...] = (
    Round270CaseCandidate(
        case_id="r1_loop13_hd_hyundai_heavy_mipo_masga_merger",
        symbol="329180/010620",
        company_name="HD Hyundai Heavy Industries / HD Hyundai Mipo",
        primary_archetype=E2RArchetype.US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM, E2RArchetype.SHIPBUILDING_CONTRACT_CYCLE_4B),
        case_type="success_candidate",
        stage1_date=date(2025, 8, 1),
        stage2_date=date(2025, 8, 27),
        stage3_date=None,
        stage4b_date=date(2025, 8, 27),
        stage4c_date=None,
        stage3_decision="merger_and_masga_headline_are_stage2_not_green_until_actual_us_awards_margin_fcf_and_integration_synergy_confirm",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("hd_hyundai_heavy_mipo_merger", "exchange_ratio_1_to_1_04059146", "us_naval_icebreaker_auxiliary_ship_demand", "masga_us_shipbuilding_cooperation"),
        red_flag_fields=("record_high_rally_before_us_revenue_bridge", "merger_headline_only", "integration_synergy_unconfirmed", "actual_us_awards_unconfirmed"),
        price_data_source="Reuters reported merger/event-return anchors",
        reported_price_anchor="HD Hyundai Heavy +11.3%; HD Hyundai Mipo +14.6%; both record highs",
        reported_return_anchor="U.S. shipbuilding sector support commitment $150B; total investment package $350B",
        event_mfe_pct=14.6,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hd_hyundai_heavy_event_mfe_pct": 11.3, "hd_hyundai_mipo_event_mfe_pct": 14.6, "exchange_ratio": "1 HD Hyundai Mipo share for 1.04059146 HD Hyundai Heavy shares", "us_shipbuilding_support_commitment_usd_bn": 150.0, "us_total_investment_package_usd_bn": 350.0, "merger_completion_target": "2025-12"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="US_naval_shipbuilding_consolidation_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="merger_headline_not_contract_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="합병과 MASGA는 강한 Stage 2지만 실제 U.S. award, 통합 시너지, 마진, FCF 전에는 Green이 아니다.",
    ),
    Round270CaseCandidate(
        case_id="r1_loop13_hanwha_ocean_us_mro_china_sanction_watch",
        symbol="042660",
        company_name="Hanwha Ocean",
        primary_archetype=E2RArchetype.SHIPBUILDING_GEOPOLITICAL_SANCTION_4C,
        secondary_archetypes=(E2RArchetype.SHIPBUILDING_CONTRACT_CYCLE_4B, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 4, 28),
        stage3_date=None,
        stage4b_date=date(2025, 4, 28),
        stage4c_date=date(2025, 10, 14),
        stage3_decision="us_mro_and_philly_shipyard_option_are_stage2_but_china_sanction_risk_must_clear_before_green",
        stage4b_status="4B-watch/4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("philly_shipyard_acquisition", "us_navy_mro_option", "reported_ytd_return_139pct", "trump_frigate_comment_plus_6pct"),
        red_flag_fields=("china_sanctions_five_us_linked_subsidiaries", "sanction_event_close_minus_5_8pct", "intraday_over_minus_8pct", "geopolitical_retaliation_risk"),
        price_data_source="Reuters/AP/MarketWatch reported anchors",
        reported_price_anchor="YTD +139%; Trump frigate comment +6%; sanction close -5.8%, intraday over -8%",
        reported_return_anchor="Philly Shipyard acquisition $100M; planned Philly investment $5B; five sanctioned U.S.-linked subsidiaries",
        event_mfe_pct=6.0,
        event_mae_pct=-8.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"reported_ytd_return_2025_pct": 139.0, "trump_frigate_comment_event_mfe_pct": 6.0, "china_sanction_event_close_mae_pct": -5.8, "china_sanction_event_intraday_mae_pct": -8.0, "hd_hyundai_heavy_same_context_mae_pct": -4.1, "philly_shipyard_acquisition_usd_mn": 100.0, "planned_philly_investment_usd_bn": 5.0, "sanctioned_us_linked_subsidiaries": 5.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_with_geopolitical_4C_watch",
        rerating_result="unknown",
        round_rerating_label="US_shipbuilding_MRO_option_with_China_sanction_risk",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="strategic_option_not_green_until_contracts_and_geopolitical_clearance",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="U.S. MRO option은 좋지만 중국 제재가 열려 있어 Green이 아니라 4C-watch를 병행한다.",
    ),
    Round270CaseCandidate(
        case_id="r1_loop13_samsung_heavy_zvezda_cancellation_hard_4c",
        symbol="010140",
        company_name="Samsung Heavy Industries",
        primary_archetype=E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C,
        secondary_archetypes=(E2RArchetype.CONTRACT_QUALITY_HARD_4C, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        stage1_date=date(2020, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 6, 18),
        stage3_decision="contract_headline_failed_actual_execution_due_counterparty_and_war_sanction_context",
        stage4b_status="none",
        hard_4c_confirmed=True,
        evidence_fields=("zvezda_icebreaker_lng_carrier_orders", "ten_icebreaker_lng_carriers", "seven_icebreaker_shuttle_tankers"),
        red_flag_fields=("cancelled_orders_4_85tn_krw", "shipowner_unilateral_termination", "russia_ukraine_uncertainty", "arbitration_damages_pursuit"),
        price_data_source="Reuters cancellation anchor",
        reported_price_anchor="4.85T KRW / $3.54B Zvezda orders cancelled",
        reported_return_anchor="10 icebreaker LNG carriers and 7 icebreaker shuttle tankers cancelled",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"cancelled_orders_krw_trn": 4.85, "cancelled_orders_usd_bn": 3.54, "cancelled_lng_icebreaker_carriers": 10.0, "cancelled_icebreaker_shuttle_tankers": 7.0, "contract_origin_years": "2020-2021", "legal_response": "arbitration / damages pursuit"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="shipbuilding_contract_quality_failure",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C",
        price_validation_status="reported_contract_anchor_not_full_ohlc",
        notes="수주금액이 커도 제재·상대방·인도 가능성이 깨지면 hard 4C다.",
    ),
    Round270CaseCandidate(
        case_id="r1_loop13_hyundai_rotem_morocco_oncf_rail_order",
        symbol="064350",
        company_name="Hyundai Rotem",
        primary_archetype=E2RArchetype.RAIL_EXPORT_MEGA_ORDER_STAGE2,
        secondary_archetypes=(E2RArchetype.ORDER_TO_REVENUE_CONVERSION, E2RArchetype.STAGE2_EVIDENCE_NOT_GREEN),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 2, 26),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="morocco_oncf_mega_order_is_stage2_not_green_until_delivery_localization_financing_margin_fx_and_cash_collection_confirm",
        stage4b_status="4B-watch-if-order-headline-priced-before-delivery",
        hard_4c_confirmed=False,
        evidence_fields=("morocco_oncf_double_decker_order", "order_value_2_2tn_krw", "110_urban_trains", "world_cup_rail_expansion"),
        red_flag_fields=("delivery_margin_cash_collection_unconfirmed", "localization_financing_fx_unknown"),
        price_data_source="Reuters order anchors",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="2.2T KRW / $1.54B order; 110 of 168 Morocco trains; total package $2.9B",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"order_value_krw_trn": 2.2, "order_value_usd_bn": 1.54, "hyundai_rotem_supply_units": 110.0, "morocco_total_train_purchase_units": 168.0, "morocco_total_package_usd_bn": 2.9, "hyundai_rotem_unit_share_pct": 65.5, "hyundai_rotem_order_share_of_total_value_pct": 53.1},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="rail_export_mega_order_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="order_not_delivery_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="철도 대형 수주는 좋은 Stage 2지만 납품·현지화·금융조건·마진·현금회수가 필요하다.",
    ),
    Round270CaseCandidate(
        case_id="r1_loop13_hd_hyundai_marine_solution_ipo_aftermarket",
        symbol="443060",
        company_name="HD Hyundai Marine Solution",
        primary_archetype=E2RArchetype.MARINE_AFTERMARKET_RECURRING_SERVICE,
        secondary_archetypes=(E2RArchetype.IPO_EVENT_PREMIUM, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="overheat",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 5, 8),
        stage3_date=None,
        stage4b_date=date(2024, 5, 8),
        stage4c_date=None,
        stage3_decision="marine_aftermarket_service_is_interesting_but_ipo_pop_is_not_green_without_recurring_revenue_margin_durability_and_roi",
        stage4b_status="4B-watch/IPO-pop",
        hard_4c_confirmed=False,
        evidence_fields=("marine_aftermarket_recurring_service", "revenue_2023_1_43tn_krw", "op_2023_201_47bn_krw", "op_margin_2023_14_1pct"),
        red_flag_fields=("ipo_close_plus_96_5pct", "ipo_pop_only", "market_cap_to_op_36_2x", "kk_or_pe_overhang_watch"),
        price_data_source="WSJ / Reuters Breakingviews IPO anchors",
        reported_price_anchor="IPO price 83,400 KRW; open 119,900; close 163,900; close +96.5%",
        reported_return_anchor="2023 revenue 1.43T KRW; OP 201.47B; OP margin 14.1%",
        event_mfe_pct=96.5,
        event_mae_pct=None,
        stage2_price_anchor=163900.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=163900.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_price_krw": 83400.0, "open_price_krw": 119900.0, "close_price_krw": 163900.0, "open_return_pct": 43.8, "close_return_pct": 96.5, "ipo_raise_krw_bn": 742.26, "ipo_raise_usd_mn": 546.0, "market_cap_close_krw_trn": 7.29, "revenue_2023_krw_trn": 1.43, "op_2023_krw_bn": 201.47, "net_profit_2023_krw_bn": 151.12, "op_growth_2023_pct": 42.0, "net_profit_growth_2023_pct": 44.0, "op_margin_2023_pct": 14.1, "market_cap_to_revenue_2023": 5.1, "market_cap_to_op_2023": 36.2},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_but_4B_overheat",
        rerating_result="event_premium",
        round_rerating_label="marine_aftermarket_recurring_service_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="IPO_pop_not_green",
        price_validation_status="reported_ipo_anchor_not_full_ohlc",
        notes="After-market 사업은 좋지만 IPO 첫날 +96.5%는 증거보다 가격이 먼저 간 4B다.",
    ),
    Round270CaseCandidate(
        case_id="r1_loop13_rainbow_robotics_samsung_strategic_equity",
        symbol="277810",
        company_name="Rainbow Robotics",
        primary_archetype=E2RArchetype.INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION,
        secondary_archetypes=(E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        stage1_date=date(2024, 12, 30),
        stage2_date=date(2024, 12, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="samsung_strategic_equity_is_stage2_option_not_green_until_robot_orders_revenue_margin_and_deployment_confirm",
        stage4b_status="4B-watch-if-robotics-theme-priced-before-revenue",
        hard_4c_confirmed=False,
        evidence_fields=("samsung_largest_shareholder", "new_stake_267bn_krw", "previous_stake_14_71pct", "future_robotics_office"),
        red_flag_fields=("strategic_equity_investment_only", "actual_robot_order_revenue_unconfirmed", "unit_economics_unknown"),
        price_data_source="Reuters strategic-equity anchor",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="Samsung newly takes 267B KRW / $181M stake; previous stake 14.71%",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_new_stake_value_krw_bn": 267.0, "samsung_new_stake_value_usd_mn": 181.0, "samsung_previous_stake_pct": 14.71, "future_robotics_office": True, "actual_robot_order_revenue_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_but_insufficient_price_data",
        rerating_result="event_premium",
        round_rerating_label="industrial_robotics_strategic_option_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="equity_option_not_order_revenue_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="삼성 지분투자는 전략 option이지 로봇 매출이 아니다. 주문·매출·마진 확인 전 Green 금지다.",
    ),
    Round270CaseCandidate(
        case_id="r1_loop13_kai_defense_aerospace_export_optionality",
        symbol="047810",
        company_name="Korea Aerospace Industries",
        primary_archetype=E2RArchetype.DEFENSE_AEROSPACE_EXPORT_OPTIONALITY,
        secondary_archetypes=(E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH, E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG),
        case_type="success_candidate",
        stage1_date=date(2025, 3, 1),
        stage2_date=date(2025, 3, 18),
        stage3_date=None,
        stage4b_date=date(2025, 3, 18),
        stage4c_date=None,
        stage3_decision="defense_aerospace_optionality_is_stage2_not_company_green_until_actual_contracts_aircraft_delivery_margin_and_cash_collection_confirm",
        stage4b_status="4B-watch/defense-sector-rally",
        hard_4c_confirmed=False,
        evidence_fields=("europe_rearmament", "kai_ytd_return_55pct", "potential_korean_defense_orders_154tn_krw", "fa50_kf21_export_optionality"),
        red_flag_fields=("defense_sector_rerating_only", "company_specific_contract_delivery_margin_unconfirmed", "sector_rally_before_cash_collection"),
        price_data_source="FT defense-stock return/order-optionality anchor",
        reported_price_anchor="KAI +55% YTD in defense-stock rally context",
        reported_return_anchor="Potential Korean defense orders 154T KRW / $106B; Hanwha +134%, Hyundai Rotem +123%",
        event_mfe_pct=55.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kai_ytd_return_2025_pct": 55.0, "hyundai_rotem_ytd_return_2025_pct": 123.0, "hanwha_aerospace_ytd_return_2025_pct": 134.0, "potential_korean_defense_orders_krw_trn": 154.0, "potential_korean_defense_orders_usd_bn": 106.0, "actual_kai_contract_delivery_margin_confirmed_in_source": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="defense_aerospace_export_optionality_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="sector_rerating_not_company_stage3",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="KAI는 방산 항공우주 option이지만 섹터 랠리만으로 회사별 Stage 3가 되지는 않는다.",
    ),
    Round270CaseCandidate(
        case_id="r1_loop13_korean_shipbuilders_contract_cycle_4b",
        symbol="010140/042660/329180",
        company_name="Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy broad shipbuilding basket",
        primary_archetype=E2RArchetype.SHIPBUILDING_CONTRACT_CYCLE_4B,
        secondary_archetypes=(E2RArchetype.CYCLICAL_SUCCESS, E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH),
        case_type="cyclical_success",
        stage1_date=date(2024, 3, 1),
        stage2_date=date(2024, 3, 14),
        stage3_date=None,
        stage4b_date=date(2024, 3, 14),
        stage4c_date=None,
        stage3_decision="broad_shipbuilding_order_cycle_is_positive_but_individual_green_requires_backlog_mix_steel_cost_labor_margin_and_cash_conversion",
        stage4b_status="4B-watch/sector-cycle",
        hard_4c_confirmed=False,
        evidence_fields=("global_shipbuilding_order_cycle_resumes", "south_korea_global_orders_share_50pct", "clarksons_newbuilding_price_index_181_81", "sector_day_rally"),
        red_flag_fields=("sector_order_cycle_not_individual_green", "margin_cash_conversion_unconfirmed", "day_move_plus_11_to_16pct"),
        price_data_source="WSJ Market Talk / Clarksons order-cycle anchor",
        reported_price_anchor="Samsung Heavy +16% to 9,210; Hanwha Ocean +13% to 27,450; HD Hyundai Heavy +11% to 122,900",
        reported_return_anchor="Korea 50% of February global orders; China 41%; Clarksons index 181.81",
        event_mfe_pct=16.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_heavy_event_price_krw": 9210.0, "samsung_heavy_event_mfe_pct": 16.0, "hanwha_ocean_event_price_krw": 27450.0, "hanwha_ocean_event_mfe_pct": 13.0, "hd_hyundai_heavy_event_price_krw": 122900.0, "hd_hyundai_heavy_event_mfe_pct": 11.0, "kospi_same_context_pct": 0.5, "samsung_relative_outperformance_pp": 15.5, "hanwha_relative_outperformance_pp": 12.5, "hyundai_relative_outperformance_pp": 10.5, "south_korea_global_orders_share_pct": 50.0, "china_global_orders_share_pct": 41.0, "clarksons_newbuilding_price_index": 181.81, "clarksons_weekly_change_pct": 0.2},
        score_price_alignment="unknown",
        round_alignment_label="cyclical_success_4B_watch",
        rerating_result="cyclical_rerating",
        round_rerating_label="shipbuilding_contract_cycle_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="sector_order_cycle_not_individual_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="조선 broad cycle은 긍정이지만 +11~16% 당일 급등은 개별 마진/현금 전환 전 4B-watch다.",
    ),
)


def round270_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("delivery", "revenue", "margin", "cash", "fcf", "recurring", "service", "award", "integration")
    for candidate in ROUND270_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND270_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round270 R1 Loop-13 industrial orders/infrastructure price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "4b" in field.lower()
                or "rally" in field.lower()
                or "ipo" in field.lower()
                or "record" in field.lower()
                or "ytd" in field.lower()
                or "cycle" in field.lower()
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "cancellation" in field.lower()
                or "sanction" in field.lower()
                or "termination" in field.lower()
                or "arbitration" in field.lower()
                or "failure" in field.lower()
                or "risk" in field.lower()
            ),
            must_have_fields=ROUND270_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4b_watch", "4c_thesis_break", "cyclical_success"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND270_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_order_mou_merger_ipo_policy_or_sector_rally_as_green_alone",
                *ROUND270_GREEN_REQUIRED_FIELDS,
                *ROUND270_GREEN_FORBIDDEN_PATTERNS,
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
                price_data_available=candidate.stage2_price_anchor is not None
                or candidate.stage4b_price_anchor is not None
                or candidate.stage4c_price_anchor is not None
                or candidate.event_mfe_pct is not None
                or candidate.event_mae_pct is not None,
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round270_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND270_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "source_sector": "R1",
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
                "event_mfe_pct": _float_text(candidate.event_mfe_pct),
                "event_mae_pct": _float_text(candidate.event_mae_pct),
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
                "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
                "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
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


def round270_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND270_SCORE_ADJUSTMENTS)


def round270_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND270_SHADOW_WEIGHT_ROWS)


def round270_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND270_DEEP_SUB_ARCHETYPES)


def round270_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round270_price_validation": "true"} for field in ROUND270_PRICE_VALIDATION_FIELDS)


def round270_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round270_label": label, "canonical_archetype": canonical} for label, canonical in ROUND270_REQUIRED_TARGET_ALIASES.items())


def round270_summary() -> dict[str, int | bool | str]:
    cases = ROUND270_CASE_CANDIDATES
    return {
        "source_round": ROUND270_SOURCE_ROUND_PATH,
        "round_id": ROUND270_ANALYST_ROUND_ID,
        "large_sector": ROUND270_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for case in cases if case.case_type == "cyclical_success"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.stage4b_status),
        "stage4c_watch_or_hard_count": sum(1 for case in cases if case.stage4c_date is not None),
        "price_data_unavailable_count": sum(1 for case in cases if case.price_validation_status == "price_data_unavailable_after_deep_search"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND270_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND270_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND270_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round270_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND270_SOURCE_ROUND_PATH,
        "round_id": ROUND270_ANALYST_ROUND_ID,
        "large_sector": ROUND270_LARGE_SECTOR,
        "summary": round270_summary(),
        "target_aliases": dict(ROUND270_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND270_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND270_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND270_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND270_HARD_4C_GATES),
        "deep_sub_archetypes": round270_deep_sub_archetype_rows(),
        "shadow_weights": round270_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round270_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_order_mou_merger_ipo_policy_or_sector_rally_as_green_alone",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round270_summary_markdown() -> str:
    summary = round270_summary()
    lines = [
        "# Round 270 R1 Loop 13 Industrial Orders / Infrastructure Price Validation",
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
        f"- cyclical_success: {summary['cyclical_success_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C watch/hard cases: {summary['stage4c_watch_or_hard_count']}",
        f"- price_data_unavailable: {summary['price_data_unavailable_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- target_archetype_count: {summary['target_archetype_count']}",
        f"- full_adjusted_ohlc_complete: {str(summary['full_adjusted_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND270_CASE_CANDIDATES:
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
            "- R1 Stage 3 is not an order, MOU, merger, IPO, policy cooperation, or sector rally headline.",
            "- HD Hyundai Heavy/Mipo is Stage 2 plus 4B-watch: the merger/MASGA price move came before actual U.S. awards and FCF.",
            "- Hanwha Ocean combines U.S. MRO option with China-sanction 4C-watch.",
            "- Samsung Heavy Zvezda cancellation is the hard 4C reference case for contract quality.",
            "- Hyundai Rotem Morocco is a strong rail-export Stage 2, but delivery/margin/cash collection remain open.",
            "- HD Hyundai Marine shows recurring-service potential, but IPO +96.5% is 4B before durability proof.",
            "- Rainbow Robotics is a strategic equity option, not robot revenue.",
            "- KAI and the broad shipbuilding basket show sector optionality/cycle, not company-specific Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round270_green_gate_review_markdown() -> str:
    lines = ["# Round 270 R1 Loop 13 Green Gate Review", "", "Do not apply these weights to production scoring yet.", "", "## Required Fields", ""]
    lines.extend(f"- {field}" for field in ROUND270_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND270_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `수주 발표`는 Stage 2 후보일 수 있지만, `납품 + 마진 + 현금회수`가 없으면 Stage 3가 아니다.",
            "- `합병/MASGA`는 좋아 보여도 실제 U.S. award와 FCF가 확인되기 전에는 4B-watch다.",
            "- `IPO 첫날 +96%`는 사업모델이 좋아도 가격이 증거보다 먼저 간 상태다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round270_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 270 R1 Loop 13 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND270_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND270_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B는 가격이나 이벤트 프리미엄이 납품, 마진, 현금 증거보다 먼저 간 상태다.",
            "- hard 4C는 원래 수주/정책 논리가 취소, 제재, 중재, 인도불능 등으로 훼손된 상태다.",
            "- Hanwha Ocean은 4C-watch이고, Samsung Heavy Zvezda cancellation은 hard 4C다.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND270_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.stage4c_date:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round270_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 270 R1 Loop 13 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND270_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round270_r1_loop13_reports(
    output_directory: str | Path = ROUND270_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND270_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND270_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round270_case_records(), cases_path),
        "audit": _write_json(round270_audit_payload(), audit_path),
        "summary": output / "round270_r1_loop13_price_validation_summary.md",
        "case_matrix": output / "round270_r1_loop13_case_matrix.csv",
        "target_aliases": output / "round270_r1_loop13_target_aliases.csv",
        "score_adjustments": output / "round270_r1_loop13_score_adjustments.csv",
        "shadow_weights": output / "round270_r1_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round270_r1_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round270_r1_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round270_r1_loop13_green_gate_review.md",
        "price_validation_plan": output / "round270_r1_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round270_r1_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round270_summary_markdown(), encoding="utf-8")
    _write_csv(round270_case_rows(), paths["case_matrix"])
    _write_csv(round270_target_alias_rows(), paths["target_aliases"])
    _write_csv(round270_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round270_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round270_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round270_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round270_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round270_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round270_stage4b_4c_review_markdown(), encoding="utf-8")
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
