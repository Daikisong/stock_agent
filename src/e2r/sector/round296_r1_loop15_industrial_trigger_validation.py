"""Round-296 R1 Loop-15 industrial trigger-level validation pack.

This module converts ``docs/round/round_296.md`` into calibration-only case
records, trigger rows, and reports. It does not change production scoring,
staging, or candidate generation.

Easy example: Hyundai Rotem on 2024-04-09 was not just a defense headline.
Shipment, OP estimate beat, revenue contribution, target upside, and market
relative strength appeared together. That trigger can be Stage2-Actionable or
Stage3-Yellow, while final Stage3-Green still waits for delivery margin and
cash collection.
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


ROUND296_SOURCE_ROUND_PATH = "docs/round/round_296.md"
ROUND296_ANALYST_ROUND_ID = "round_224"
ROUND296_LARGE_SECTOR = "INDUSTRIALS_ORDERS_INFRASTRUCTURE"
ROUND296_METHOD = "trigger_level_backtest_v1"
ROUND296_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round296_r1_loop15_industrial_trigger_validation"
ROUND296_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop15_round296.jsonl"
ROUND296_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r1_loop15_round296.jsonl"
ROUND296_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round296_r1_loop15_industrial_trigger_validation_audit.json"

ROUND296_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "DEFENSE_EXPORT_STAGE2_ACTIONABLE": E2RArchetype.DEFENSE_EXPORT_STAGE2_ACTIONABLE.value,
    "MISSILE_DEFENSE_ORDER_4B_TIMING": E2RArchetype.MISSILE_DEFENSE_ORDER_4B_TIMING.value,
    "DEFENSE_BACKLOG_DILUTION_OVERLAY": E2RArchetype.DEFENSE_BACKLOG_DILUTION_OVERLAY.value,
    "SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE": E2RArchetype.SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE.value,
    "GRID_EQUIPMENT_US_GROWTH_STAGE2_PROMOTE": E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2_PROMOTE.value,
    "OVERSEAS_EPC_ORDER_STAGE2_YELLOW": E2RArchetype.OVERSEAS_EPC_ORDER_STAGE2_YELLOW.value,
    "NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2": E2RArchetype.NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2.value,
}

ROUND296_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "shipment_delivery_calloff_or_revenue_contribution_confirmed",
    "op_estimate_or_revenue_forecast_beats_consensus_by_20pct_plus",
    "market_relative_strength_on_evidence_day_5pp_plus",
    "backlog_duration_or_repeat_order_visibility_confirmed",
    "asp_price_index_or_target_revision_confirmed",
    "binding_order_or_delivery_evidence_not_mou_or_preferred_bidder_only",
)

ROUND296_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "real_order_contract_shipment_or_approval_confirmed",
    "op_eps_or_revenue_contribution_quantified",
    "trigger_day_relative_strength_is_strong",
    "margin_cash_collection_final_delivery_or_legal_clearance_still_pending",
)

ROUND296_GREEN_BLOCKERS: tuple[str, ...] = (
    "full_trigger_level_ohlc_missing",
    "delivery_margin_unconfirmed",
    "cash_collection_unconfirmed",
    "working_capital_or_claim_risk_unresolved",
    "final_contract_or_legal_clearance_pending",
    "4b_overlay_requires_sizing_down_rule",
)

ROUND296_SCORE_UP_AXES: tuple[str, ...] = (
    "shipment_revenue_contribution",
    "op_estimate_vs_consensus",
    "relative_strength_on_evidence_day",
    "backlog_duration_quality",
    "pricing_power_index_or_ASP",
    "target_price_revision_with_estimate_raise",
    "export_contract_repeatability",
    "stage3_plus_4b_overlay_handling",
)

ROUND296_SCORE_DOWN_AXES: tuple[str, ...] = (
    "order_value_only",
    "preferred_bidder_only",
    "mou_or_partnership_only",
    "target_price_raise_without_price_strength",
    "event_pop_without_margin_visibility",
    "sector_hype_without_company_estimate",
)

ROUND296_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "six_to_twelve_month_plus_60_to_100pct_then_target_downgrade_or_hold",
    "YTD_double_plus_then_large_share_sale_CB_or_capital_raise",
    "event_trigger_is_control_MA_governance_premium_not_operating_margin",
    "new_order_pipeline_alive_but_valuation_burden_clear",
)

ROUND296_HARD_4C_GATES: tuple[str, ...] = (
    "signed_contract_collapse",
    "export_license_sanction_or_legal_block",
    "major_cost_overrun_or_claim",
    "dilution_financing_after_overheat",
    "preferred_bidder_cancellation",
    "final_contract_blocked_by_court_or_regulator",
)


@dataclass(frozen=True)
class Round296ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round296ShadowWeightRow:
    archetype: E2RArchetype
    shipment_revenue_contribution: int
    op_estimate_vs_consensus: int
    relative_strength_on_evidence_day: int
    backlog_duration_quality: int
    pricing_power_index_or_asp: int
    target_revision_with_estimate_raise: int
    export_contract_repeatability: int
    stage3_plus_4b_overlay_handling: int
    order_value_only_penalty: int
    preferred_bidder_only_penalty: int
    mou_only_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "shipment_revenue_contribution": _signed(self.shipment_revenue_contribution),
            "op_estimate_vs_consensus": _signed(self.op_estimate_vs_consensus),
            "relative_strength_on_evidence_day": _signed(self.relative_strength_on_evidence_day),
            "backlog_duration_quality": _signed(self.backlog_duration_quality),
            "pricing_power_index_or_asp": _signed(self.pricing_power_index_or_asp),
            "target_revision_with_estimate_raise": _signed(self.target_revision_with_estimate_raise),
            "export_contract_repeatability": _signed(self.export_contract_repeatability),
            "stage3_plus_4b_overlay_handling": _signed(self.stage3_plus_4b_overlay_handling),
            "order_value_only_penalty": _signed(self.order_value_only_penalty),
            "preferred_bidder_only_penalty": _signed(self.preferred_bidder_only_penalty),
            "mou_only_penalty": _signed(self.mou_only_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round296TriggerRecord:
    trigger_id: str
    case_id: str
    trigger_type: str
    trigger_date: date
    evidence_available: str
    entry_price_krw: float | None
    event_return_pct: float | str | None
    market_relative_return_pp: float | str | None
    trigger_outcome_label: str
    promote_to: str

    def as_dict(self) -> dict[str, object]:
        return {
            "trigger_id": self.trigger_id,
            "case_id": self.case_id,
            "trigger_type": self.trigger_type,
            "trigger_date": self.trigger_date.isoformat(),
            "evidence_available": self.evidence_available,
            "entry_price_krw": self.entry_price_krw,
            "event_return_pct": self.event_return_pct,
            "market_relative_return_pp": self.market_relative_return_pp,
            "trigger_outcome_label": self.trigger_outcome_label,
            "promote_to": self.promote_to,
        }

    def as_row(self) -> dict[str, str]:
        return {key: _value_text(value) for key, value in self.as_dict().items()}


@dataclass(frozen=True)
class Round296CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    round_case_type: str
    best_trigger: str
    best_trigger_type: str
    stage_candidate: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    hard_4c_confirmed: bool
    trigger_outcome_label: str
    stage_gate_correction: str
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    event_mfe_pct: float | None
    event_mae_pct: float | None
    market_relative_return_pp: float | None
    stage1_price_anchor: float | None
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


ROUND296_SCORE_ADJUSTMENTS: tuple[Round296ScoreAdjustment, ...] = (
    Round296ScoreAdjustment("shipment_revenue_contribution", 5, "raise", "실제 출하와 매출 기여는 단순 수주 headline보다 강하다."),
    Round296ScoreAdjustment("op_estimate_vs_consensus", 5, "raise", "OP 추정치가 consensus 대비 20% 이상 높으면 Stage2-Actionable 승격 후보가 된다."),
    Round296ScoreAdjustment("relative_strength_on_evidence_day", 5, "raise", "증거가 나온 날 시장 대비 +5pp 이상이면 trigger 품질이 높다."),
    Round296ScoreAdjustment("backlog_duration_quality", 4, "raise", "3년치 backlog 같은 duration evidence는 단순 order보다 강하다."),
    Round296ScoreAdjustment("pricing_power_index_or_ASP", 4, "raise", "조선 선가 지수나 전력기기 ASP처럼 가격 지표가 같이 붙으면 visibility가 좋아진다."),
    Round296ScoreAdjustment("target_price_revision_with_estimate_raise", 3, "raise", "target 상향은 추정치 상향과 같이 있을 때만 의미가 크다."),
    Round296ScoreAdjustment("export_contract_repeatability", 4, "raise", "Saudi 이후 Iraq처럼 반복 수출 계약은 Stage2 강도를 높인다."),
    Round296ScoreAdjustment("stage3_plus_4b_overlay_handling", 5, "raise", "좋은 Stage3 후보를 4B 때문에 취소하지 말고 overlay로 병기한다."),
    Round296ScoreAdjustment("order_value_only", -5, "lower", "계약금액만 있고 margin, cash, delivery가 없으면 Green 금지다."),
    Round296ScoreAdjustment("preferred_bidder_only", -4, "lower", "preferred bidder는 final contract와 legal clearance 전까지 Green이 아니다."),
    Round296ScoreAdjustment("mou_or_partnership_only", -5, "lower", "MOU나 partnership은 계약·매출이 아니므로 Actionable 승격을 제한한다."),
)


ROUND296_SHADOW_WEIGHT_ROWS: tuple[Round296ShadowWeightRow, ...] = (
    Round296ShadowWeightRow(E2RArchetype.DEFENSE_EXPORT_STAGE2_ACTIONABLE, 5, 5, 5, 4, 2, 3, 5, 4, -5, -3, -5, "shipment+OP beat+relative strength", "delivery+margin pending", "delivery+margin+cash collection", "Hyundai Rotem trigger should promote Stage2 to Stage3-Yellow."),
    Round296ShadowWeightRow(E2RArchetype.MISSILE_DEFENSE_ORDER_4B_TIMING, 3, 3, 4, 4, 2, 2, 5, 5, -4, -3, -5, "repeat export order+relative strength", "combat validation pending", "delivery+margin+follow-on orders", "LIG 4B should be trim if new orders remain."),
    Round296ShadowWeightRow(E2RArchetype.DEFENSE_BACKLOG_DILUTION_OVERLAY, 3, 4, 4, 5, 2, 2, 5, 5, -4, -3, -5, "order+backlog expansion", "strong backlog but dilution risk", "delivery+cash+no dilution", "Hanwha Aerospace requires Stage3 plus 4B overlay."),
    Round296ShadowWeightRow(E2RArchetype.SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE, 2, 2, 5, 5, 5, 2, 4, 3, -4, -2, -5, "orders+price index+backlog duration", "margin/labor/steel pending", "delivery margin confirmed", "Shipbuilding basket trigger should be promoted."),
    Round296ShadowWeightRow(E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2_PROMOTE, 2, 3, 3, 4, 5, 4, 3, 2, -4, -2, -5, "US revenue mix+forecast raise+target revision", "needs price confirmation", "margin+backlog+capacity", "LS Electric needs full-window retest after immediate price fail."),
    Round296ShadowWeightRow(E2RArchetype.OVERSEAS_EPC_ORDER_STAGE2_YELLOW, 2, 2, 5, 4, 2, 3, 3, 3, -5, -3, -5, "large order+relative strength+target upside", "advance payment/cost lock pending", "completion margin+cash collection", "Samsung E&A supports Yellow not Green."),
    Round296ShadowWeightRow(E2RArchetype.NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2, 1, 1, 2, 4, 1, 2, 3, 2, -4, -5, -5, "preferred bidder+project scale", "legal/final contract pending", "final contract+legal clearance+C/F visibility", "Czech nuclear should not become Green before contract."),
)


ROUND296_TRIGGER_RECORDS: tuple[Round296TriggerRecord, ...] = (
    Round296TriggerRecord("r1l15_hyundai_rotem_T2", "r1_loop15_hyundai_rotem_k2_poland", "Stage2-Actionable", date(2024, 4, 9), "18 K2 shipments to Poland, Q1 OP estimate +85% YoY, consensus beat, 270B won export revenue contribution", 41300, 9.3, 9.6, "excellent_stage2_promote_candidate", "Stage3-Yellow"),
    Round296TriggerRecord("r1l15_lig_nex1_T2", "r1_loop15_lig_nex1_msam", "4B-watch", date(2024, 7, 2), "1H share gain 69%, KOSPI 5.4%, downgrade to Hold", 195700, -11, None, "4B_valid_but_not_hard_exit", "4B_trim"),
    Round296TriggerRecord("r1l15_lig_nex1_T3", "r1_loop15_lig_nex1_msam", "Stage2-Actionable", date(2024, 9, 20), "Iraq 3.71T won / $2.8B Cheongung-II order after Saudi $3.2B order", None, 3.6, 2.7, "good_entry_candidate", "Stage2-Actionable"),
    Round296TriggerRecord("r1l15_hanwha_aero_T1", "r1_loop15_hanwha_aerospace_k9_backlog_dilution", "Stage2-Actionable", date(2024, 7, 9), "Romania $1B K9/K10 order, backlog 5.1T to 30T won", None, 5.0, None, "Stage3_Yellow_candidate", "Stage3-Yellow"),
    Round296TriggerRecord("r1l15_hanwha_aero_T4", "r1_loop15_hanwha_aerospace_k9_backlog_dilution", "4B-watch", date(2025, 3, 21), "3.6T won share sale, 605,000 won issue price, 16% discount, YTD more than doubled", 605000, -13, None, "4B_success_dilution_overlay", "4B"),
    Round296TriggerRecord("r1l15_shipbuilding_T1", "r1_loop15_shipbuilding_order_price_basket", "Stage2-Actionable", date(2024, 3, 14), "global shipbuilding orders +18% YoY, Korea 50% share, newbuilding price index up, 3-year backlog", None, "Samsung Heavy +16 / Hanwha Ocean +13 / HD HHI +11", "15.5/12.5/10.5", "Stage2_promote_candidate", "Stage3-Yellow_candidate"),
    Round296TriggerRecord("r1l15_ls_electric_T2", "r1_loop15_ls_electric_us_grid", "Stage2-Actionable_candidate", date(2024, 7, 1), "U.S. revenue share forecast 20%, revenue forecast raised 4-22%, target raised 87%", 208500, -5.4, None, "evidence_good_but_price_failed_retest_required", "pending_full_ohlc"),
    Round296TriggerRecord("r1l15_samsung_ena_T2", "r1_loop15_samsung_ena_fadhili", "Stage3-Yellow_candidate", date(2024, 4, 3), "$6B Fadhili order, +60% gas capacity, target upside 30.8%, event relative +9.9pp", 26750, 8.5, 9.9, "Stage3_Yellow_candidate", "Stage3-Yellow"),
    Round296TriggerRecord("r1l15_czech_nuclear_T1", "r1_loop15_czech_nuclear_doosan", "Stage2-Actionable_with_legal_watch", date(2024, 7, 17), "KHNP preferred bidder, two reactors, first large overseas nuclear order since 2009, related names already +14 to +48 over 3 months", None, "Doosan +48 3M / KEPCO E&C +41 3M / KEPCO Plant +14 3M", None, "prepriced_event_premium_with_legal_4c_watch", "Stage2-Actionable_only"),
)


ROUND296_CASE_CANDIDATES: tuple[Round296CaseCandidate, ...] = (
    Round296CaseCandidate(
        case_id="r1_loop15_hyundai_rotem_k2_poland",
        symbol="064350",
        company_name="Hyundai Rotem",
        primary_archetype=E2RArchetype.DEFENSE_EXPORT_STAGE2_ACTIONABLE,
        secondary_archetypes=(E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE),
        case_type="success_candidate",
        round_case_type="Stage2_promote_candidate / Stage3-Yellow candidate",
        best_trigger="T2/T3",
        best_trigger_type="Stage2-Actionable_to_Stage3-Yellow",
        stage_candidate="Stage3-Yellow",
        stage1_date=date(2022, 1, 1),
        stage2_date=date(2024, 4, 9),
        stage3_date=date(2024, 4, 9),
        stage4b_date=None,
        stage4c_date=None,
        hard_4c_confirmed=False,
        trigger_outcome_label="Stage2_promote_candidate",
        stage_gate_correction="shipment + OP estimate beat + revenue contribution + relative strength should upgrade Stage2 to Stage3-Yellow",
        evidence_fields=("K2_Poland_shipment_18_units", "Q1_OP_estimate_plus_85pct_YoY", "consensus_OP_beat_33_1pct", "Poland_K2_revenue_270B_KRW", "event_relative_strength_9_6pp"),
        red_flag_fields=("delivery_margin_pending", "follow_on_contract_pending_at_T2", "4B_watch_after_YTD_rally"),
        price_data_source="WSJ Hyundai Rotem event price and estimate anchor; Reuters Poland second contract confirmation",
        reported_price_anchor="41,300 KRW after +9.3% event move",
        reported_return_anchor="+9.3% vs KOSPI -0.3%, relative +9.6pp",
        event_mfe_pct=9.3,
        event_mae_pct=None,
        market_relative_return_pp=9.6,
        stage1_price_anchor=None,
        stage2_price_anchor=41300,
        stage3_price_anchor=41300,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"entry_price_anchor_krw": 41300, "event_mfe_pct": 9.3, "kospi_same_context_pct": -0.3, "market_relative_return_pp": 9.6, "op_estimate_yoy_growth_pct": 85, "op_estimate_krw_bn": 59.10, "consensus_op_krw_bn": 44.40, "op_estimate_vs_consensus_pct": 33.1, "poland_k2_revenue_krw_bn": 270, "target_price_krw": 47500, "target_upside_from_event_price_pct": 15.0, "poland_second_contract_value_usd_bn": 6.5, "poland_second_contract_units": 180, "poland_local_production_units": 61},
        score_price_alignment="missed_due_to_score",
        round_alignment_label="missed_structural_risk",
        rerating_result="unknown",
        round_rerating_label="Stage2_promote_to_Stage3_Yellow_candidate",
        stage_failure_type="missed_structural",
        round_stage_failure_label="plain_stage2_understates_shipment_OP_estimate_relative_strength",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Shipment, OP estimate beat, revenue contribution and relative strength make this stronger than plain Stage 2.",
    ),
    Round296CaseCandidate(
        case_id="r1_loop15_lig_nex1_msam",
        symbol="079550",
        company_name="LIG Nex1",
        primary_archetype=E2RArchetype.MISSILE_DEFENSE_ORDER_4B_TIMING,
        secondary_archetypes=(E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, E2RArchetype.THEME_VALUATION_OVERHEAT),
        case_type="success_candidate",
        round_case_type="Stage3-Yellow + 4B timing audit",
        best_trigger="T3",
        best_trigger_type="Stage2-Actionable",
        stage_candidate="Stage2-Actionable",
        stage1_date=date(2024, 2, 1),
        stage2_date=date(2024, 9, 20),
        stage3_date=date(2026, 3, 11),
        stage4b_date=date(2024, 7, 2),
        stage4c_date=None,
        hard_4c_confirmed=False,
        trigger_outcome_label="Stage2_promote_candidate_with_4B_overlay",
        stage_gate_correction="export order after prior large orders should upgrade Stage2 to Stage2-Actionable; 4B should be trim not hard exit when new order pipeline remains",
        evidence_fields=("Iraq_M_SAM_II_order_3_71T_KRW", "Saudi_prior_order_3_2B_USD", "combat_validation_reported_gain_47pct"),
        red_flag_fields=("1H_gain_69pct_valuation_burden", "downgrade_to_hold", "4B_should_be_trim_not_hard_exit"),
        price_data_source="MarketWatch downgrade anchor, Reuters Iraq order anchor, FT combat-validation anchor",
        reported_price_anchor="T2 close 195,700 KRW after -11%; T3 +3.6%",
        reported_return_anchor="Iraq order +3.6% vs KOSPI +0.9%; earlier 4B -11%",
        event_mfe_pct=3.6,
        event_mae_pct=-11.0,
        market_relative_return_pp=2.7,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=195700,
        stage4c_price_anchor=None,
        extra_price_metrics={"iraq_order_value_krw_trn": 3.71, "iraq_order_value_usd_bn": 2.8, "saudi_prior_order_usd_bn": 3.2, "four_country_operator_context": True, "t2_4b_date": "2024-07-02", "t2_4b_event_mae_pct": -11, "t2_4b_close_price_krw": 195700, "t2_pre_event_1h_gain_pct": 69, "t2_kospi_1h_gain_pct": 5.4, "t4_combat_validation_reported_gain_pct": 47},
        score_price_alignment="missed_due_to_score",
        round_alignment_label="Stage2_promote_candidate_with_4B_overlay",
        rerating_result="unknown",
        round_rerating_label="4B_trim_not_hard_exit",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="4B_too_early_if_used_as_full_exit",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="4B was valid as a trim signal, but repeat export orders kept the pipeline alive.",
    ),
    Round296CaseCandidate(
        case_id="r1_loop15_hanwha_aerospace_k9_backlog_dilution",
        symbol="012450",
        company_name="Hanwha Aerospace",
        primary_archetype=E2RArchetype.DEFENSE_BACKLOG_DILUTION_OVERLAY,
        secondary_archetypes=(E2RArchetype.DEFENSE_BACKLOG_DILUTION_4B, E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG),
        case_type="structural_success",
        round_case_type="Stage3 + 4B overlay",
        best_trigger="T1/T2",
        best_trigger_type="Stage2-Actionable_to_Stage3-Yellow",
        stage_candidate="Stage3-Yellow + 4B-watch",
        stage1_date=date(2022, 1, 1),
        stage2_date=date(2024, 7, 9),
        stage3_date=date(2024, 7, 9),
        stage4b_date=date(2025, 3, 21),
        stage4c_date=date(2025, 3, 27),
        hard_4c_confirmed=False,
        trigger_outcome_label="Stage3_Yellow_with_4B_overlay",
        stage_gate_correction="do not cancel Stage3 because of 4B; attach dilution overlay and adjust position",
        evidence_fields=("Romania_order_1B_USD", "K9_54_units", "K10_36_units", "backlog_5_1T_to_30T_KRW", "global_howitzer_share_over_50pct"),
        red_flag_fields=("share_sale_3_6T_KRW", "discount_to_prior_close_16pct", "FSS_filing_revision_order"),
        price_data_source="Reuters Romania order/backlog anchor and FT share-sale dilution anchor",
        reported_price_anchor="T1 +5% record high; T4 share sale -13%",
        reported_return_anchor="Romania order +5%; later share-sale event -13%",
        event_mfe_pct=5.0,
        event_mae_pct=-13.0,
        market_relative_return_pp=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=605000,
        stage4c_price_anchor=None,
        extra_price_metrics={"romania_order_value_usd_bn": 1.0, "k9_howitzers": 54, "k10_resupply_vehicles": 36, "contract_end": "2029-07", "backlog_end_2021_krw_trn": 5.1, "backlog_march_2024_krw_trn": 30, "backlog_growth_multiple": 5.88, "t1_event_mfe_pct": 5.0, "share_sale_krw_trn": 3.6, "share_sale_usd_bn": 2.5, "offer_price_krw": 605000, "discount_to_prior_close_pct": 16, "t4_event_mae_pct": -13},
        score_price_alignment="missed_due_to_score",
        round_alignment_label="aligned_if_stage3_plus_4b_overlay_allowed",
        rerating_result="true_rerating",
        round_rerating_label="Stage3_Yellow_with_4B_overlay",
        stage_failure_type="yellow_success",
        round_stage_failure_label="4B_overlay_should_not_cancel_stage3_backlog_evidence",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Order/backlog can be Stage3-Yellow; dilution is 4B overlay, not Stage3 cancellation.",
    ),
    Round296CaseCandidate(
        case_id="r1_loop15_shipbuilding_order_price_basket",
        symbol="010140/042660/329180/010620",
        company_name="Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy / HD Hyundai Mipo",
        primary_archetype=E2RArchetype.SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE,
        secondary_archetypes=(E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG, E2RArchetype.SHIPBUILDING_MERGER_MASGA_4B),
        case_type="success_candidate",
        round_case_type="Stage2-Actionable / event_premium",
        best_trigger="T1/T2",
        best_trigger_type="Stage2-Actionable_to_Stage3-Yellow",
        stage_candidate="Stage2-Actionable_to_Stage3-Yellow",
        stage1_date=date(2024, 3, 1),
        stage2_date=date(2024, 3, 14),
        stage3_date=date(2024, 3, 14),
        stage4b_date=date(2025, 8, 27),
        stage4c_date=None,
        hard_4c_confirmed=False,
        trigger_outcome_label="Stage2_promote_candidate",
        stage_gate_correction="orders + price index + backlog duration + relative strength should upgrade from Stage2 to Stage3-Yellow candidate",
        evidence_fields=("global_new_orders_yoy_plus_18pct", "Korea_global_order_share_50pct", "newbuilding_price_index_181_81", "backlog_duration_3_years"),
        red_flag_fields=("delivery_margin_pending", "labor_cost_pending", "steel_cost_pending", "MASGA_event_premium_watch"),
        price_data_source="WSJ shipbuilding order/share-price/newbuilding price anchor and Reuters HD HHI/Mipo merger anchor",
        reported_price_anchor="Samsung Heavy 9,210 KRW, Hanwha Ocean 27,450 KRW, HD HHI 122,900 KRW",
        reported_return_anchor="Samsung Heavy +16%, Hanwha Ocean +13%, HD HHI +11%; later HD HHI +11.3%, HD Mipo +14.6%",
        event_mfe_pct=16.0,
        event_mae_pct=None,
        market_relative_return_pp=15.5,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_heavy_event_mfe_pct": 16, "samsung_heavy_event_price_krw": 9210, "hanwha_ocean_event_mfe_pct": 13, "hanwha_ocean_event_price_krw": 27450, "hd_hhi_event_mfe_pct": 11, "hd_hhi_event_price_krw": 122900, "kospi_same_context_pct": 0.5, "global_new_orders_yoy_pct": 18, "korea_global_order_share_pct": 50, "china_global_order_share_pct": 41, "newbuilding_price_index": 181.81, "newbuilding_price_index_weekly_change_pct": 0.2, "backlog_duration_context_years": 3, "t4_hd_hhi_mfe_pct": 11.3, "t4_hd_mipo_mfe_pct": 14.6},
        score_price_alignment="missed_due_to_score",
        round_alignment_label="Stage2_promote_candidate",
        rerating_result="unknown",
        round_rerating_label="order_price_backlog_duration_promote",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="plain_stage2_understates_order_pricing_backlog_combo",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Order momentum, newbuilding price index, backlog duration and broad relative strength should not remain plain Stage 2.",
    ),
    Round296CaseCandidate(
        case_id="r1_loop15_ls_electric_us_grid",
        symbol="010120",
        company_name="LS Electric",
        primary_archetype=E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2_PROMOTE,
        secondary_archetypes=(E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2, E2RArchetype.GRID_TRANSFORMER_SHORTAGE),
        case_type="success_candidate",
        round_case_type="evidence_good_but_price_failed_then_promote_candidate",
        best_trigger="T2_pending_full_ohlc",
        best_trigger_type="Stage2-Actionable_candidate",
        stage_candidate="Stage2_promote_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 7, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        hard_4c_confirmed=False,
        trigger_outcome_label="evidence_good_but_price_failed_then_Stage2_promote_candidate",
        stage_gate_correction="immediate event price failure should not kill structural trigger; re-test with full OHLC",
        evidence_fields=("US_revenue_share_forecast_20pct", "target_price_raise_87pct", "revenue_forecast_raise_4_to_22pct", "GSU_transformer_demand_growth_274pct"),
        red_flag_fields=("immediate_price_failed_minus_5_4pct", "target_price_raise_without_price_strength", "full_window_retest_required"),
        price_data_source="MarketWatch LS Electric target/revenue mix anchor and Reuters U.S. transformer shortage anchor",
        reported_price_anchor="208,500 KRW after -5.4% event move",
        reported_return_anchor="target +87% but same-day price -5.4%",
        event_mfe_pct=None,
        event_mae_pct=-5.4,
        market_relative_return_pp=None,
        stage1_price_anchor=None,
        stage2_price_anchor=208500,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"entry_price_anchor_krw": 208500, "event_mae_pct": -5.4, "us_revenue_share_2022_pct": "below_5", "us_revenue_share_2024_forecast_pct": 20, "revenue_forecast_raise_2024_2026_pct": "4-22", "target_price_before_krw": 150000, "target_price_after_krw": 280000, "target_raise_pct": 86.7, "target_upside_from_event_price_pct": 34.3, "gsu_transformer_demand_growth_2019_2025_pct": 274, "substation_transformer_demand_growth_2019_2025_pct": 116, "transformer_price_5y_growth_pct": 80},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="inconclusive_but_promote_candidate",
        rerating_result="unknown",
        round_rerating_label="US_grid_stage2_promote_needs_full_window_retest",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="immediate_price_failure_not_enough_to_reject_structural_trigger",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Immediate price failed, but structural U.S. grid trigger needs full-window retest before rejection.",
    ),
    Round296CaseCandidate(
        case_id="r1_loop15_samsung_ena_fadhili",
        symbol="028050",
        company_name="Samsung E&A",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_ORDER_STAGE2_YELLOW,
        secondary_archetypes=(E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL, E2RArchetype.ORDER_HEADLINE_NOT_MARGIN_GREEN),
        case_type="success_candidate",
        round_case_type="Stage2-Actionable / Stage3-Yellow candidate",
        best_trigger="T1/T2",
        best_trigger_type="Stage2-Actionable_to_Stage3-Yellow",
        stage_candidate="Stage3-Yellow",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 3),
        stage3_date=date(2024, 4, 3),
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        hard_4c_confirmed=False,
        trigger_outcome_label="Stage3_Yellow_candidate",
        stage_gate_correction="large order + relative strength + target upside supports Yellow, not Green",
        evidence_fields=("Fadhili_contract_6B_USD", "event_relative_strength_9_9pp", "target_upside_30_8pct", "completion_target_2027_11"),
        red_flag_fields=("advance_payment_missing", "cost_lock_in_missing", "working_capital_pending", "completion_margin_pending"),
        price_data_source="WSJ Samsung E&A Fadhili order event price anchor",
        reported_price_anchor="26,750 KRW after +8.5% event move",
        reported_return_anchor="+8.5% vs KOSPI -1.4%, relative +9.9pp",
        event_mfe_pct=8.5,
        event_mae_pct=None,
        market_relative_return_pp=9.9,
        stage1_price_anchor=None,
        stage2_price_anchor=26750,
        stage3_price_anchor=26750,
        stage4b_price_anchor=26750,
        stage4c_price_anchor=None,
        extra_price_metrics={"entry_price_anchor_krw": 26750, "event_mfe_pct": 8.5, "kospi_same_context_pct": -1.4, "market_relative_return_pp": 9.9, "contract_value_usd_bn": 6.0, "project_total_value_usd_bn": 7.7, "gas_capacity_increase_pct": 60, "sulfur_production_increase_tpd": 2300, "completion_target": "2027-11", "target_price_krw": 35000, "target_upside_from_event_price_pct": 30.8, "stage3_green_gate_missing": ["advance_payment", "cost_lock_in", "working_capital", "completion_margin"]},
        score_price_alignment="missed_due_to_score",
        round_alignment_label="Stage2_promote_candidate",
        rerating_result="unknown",
        round_rerating_label="Stage3_Yellow_not_Green_EPC_execution_gate",
        stage_failure_type="yellow_success",
        round_stage_failure_label="mega_order_relative_strength_target_upside_supports_yellow",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Mega-order plus relative strength and target upside supports Stage3-Yellow, not Green.",
    ),
    Round296CaseCandidate(
        case_id="r1_loop15_czech_nuclear_doosan",
        symbol="034020/052690/051600",
        company_name="Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E",
        primary_archetype=E2RArchetype.NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2,
        secondary_archetypes=(E2RArchetype.NUCLEAR_SMR_GRID_POLICY, E2RArchetype.NUCLEAR_EXPORT_LEGAL_4C_WATCH),
        case_type="event_premium",
        round_case_type="Stage2_promote_candidate + legal_4C_watch",
        best_trigger="T0/T1_if_preferred_bidder_probability_scored",
        best_trigger_type="Stage2-Actionable_with_legal_watch",
        stage_candidate="Stage2-Actionable_with_legal_watch",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 7, 17),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 5, 6),
        hard_4c_confirmed=False,
        trigger_outcome_label="event_premium_with_legal_4C_watch",
        stage_gate_correction="preferred bidder can be Stage2-Actionable, but if most price move occurred before formal evidence, mark pre-pricing risk",
        evidence_fields=("KHNP_preferred_bidder", "two_reactors", "first_major_overseas_nuclear_since_2009", "Doosan_3m_gain_48pct"),
        red_flag_fields=("preferred_bidder_only", "final_contract_signed_false", "Westinghouse_EDF_legal_challenge", "court_blocked_signing"),
        price_data_source="Reuters Czech nuclear preferred-bidder and legal challenge anchors",
        reported_price_anchor="Doosan +48%, KEPCO E&C +41%, KEPCO Plant S&E +14% over 3 months before/around event",
        reported_return_anchor="pre-priced preferred bidder event; at least $18B contract signing later blocked by court",
        event_mfe_pct=48.0,
        event_mae_pct=None,
        market_relative_return_pp=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"khnp_status": "preferred_bidder", "reactors": 2, "estimated_cost_per_unit_czk_bn": 200, "estimated_cost_per_unit_usd_bn": 8.65, "first_major_overseas_nuclear_order_since": 2009, "doosan_enerbility_3m_gain_pct": 48, "kepco_ec_3m_gain_pct": 41, "kepco_plant_se_3m_gain_pct": 14, "court_blocked_contract_value_usd_bn_min": 18, "legal_challenge_parties": ["Westinghouse", "EDF"], "final_contract_signed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_legal_4C_watch",
        rerating_result="event_premium",
        round_rerating_label="preferred_bidder_not_final_contract_green",
        stage_failure_type="false_yellow",
        round_stage_failure_label="preferred_bidder_prepriced_legal_gate_pending",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Preferred bidder is Stage2-Actionable at most; final contract and legal clearance are required for Green.",
    ),
)


def round296_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(_case_record(case) for case in ROUND296_CASE_CANDIDATES)


def round296_summary() -> dict[str, object]:
    cases = ROUND296_CASE_CANDIDATES
    triggers = ROUND296_TRIGGER_RECORDS
    return {
        "source_round": ROUND296_SOURCE_ROUND_PATH,
        "round_id": ROUND296_ANALYST_ROUND_ID,
        "large_sector": ROUND296_LARGE_SECTOR,
        "method": ROUND296_METHOD,
        "case_candidate_count": len(cases),
        "trigger_count": len(triggers),
        "stage2_promote_candidate_count": sum(1 for case in cases if "Stage2" in case.best_trigger_type or "Stage2" in case.stage_candidate or "Stage2" in case.trigger_outcome_label),
        "stage3_yellow_candidate_count": sum(1 for case in cases if "Stage3-Yellow" in case.stage_candidate or "Stage3_Yellow" in case.trigger_outcome_label),
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.round_case_type),
        "legal_4c_watch_count": sum(1 for case in cases if "legal" in case.round_case_type.lower() or "legal" in case.stage_candidate.lower()),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "missed_due_to_score_count": sum(1 for case in cases if case.score_price_alignment == "missed_due_to_score"),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "full_adjusted_ohlc_complete": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round296_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(_case_row(case) for case in ROUND296_CASE_CANDIDATES)


def round296_trigger_rows() -> tuple[dict[str, str], ...]:
    return tuple(trigger.as_row() for trigger in ROUND296_TRIGGER_RECORDS)


def round296_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND296_REQUIRED_TARGET_ALIASES.items())


def round296_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND296_SCORE_ADJUSTMENTS)


def round296_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND296_SHADOW_WEIGHT_ROWS)


def round296_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND296_SOURCE_ROUND_PATH,
        "round_id": ROUND296_ANALYST_ROUND_ID,
        "large_sector": ROUND296_LARGE_SECTOR,
        "method": ROUND296_METHOD,
        "summary": round296_summary(),
        "target_aliases": dict(ROUND296_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND296_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND296_STAGE3_YELLOW_RULES),
        "green_blockers": list(ROUND296_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND296_SCORE_UP_AXES),
        "score_down_axes": list(ROUND296_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND296_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND296_HARD_4C_GATES),
        "case_ids": [case.case_id for case in ROUND296_CASE_CANDIDATES],
        "trigger_ids": [trigger.trigger_id for trigger in ROUND296_TRIGGER_RECORDS],
        "what_not_to_change": [
            "do_not_apply_round296_shadow_weights_to_production_scoring_yet",
            "do_not_use_round296_cases_as_candidate_generation_input",
            "do_not_force_stage3_green_without_full_ohlc_and_margin_cash_confirmation",
            "do_not_downgrade_stage_candidate_merely_because_full_ohlc_is_missing",
            "do_not_treat_preferred_bidder_or_MOU_as_final_contract",
        ],
    }


def render_round296_summary_markdown() -> str:
    summary = round296_summary()
    lines = [
        "# Round 296 R1 Loop 15 Industrial Trigger-Level Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- method: {summary['method']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- triggers: {summary['trigger_count']}",
        f"- Stage2 promote candidates: {summary['stage2_promote_candidate_count']}",
        f"- Stage3-Yellow candidates: {summary['stage3_yellow_candidate_count']}",
        f"- Stage3-Green confirmed: {summary['stage3_green_confirmed_count']}",
        f"- 4B watch cases: {summary['stage4b_watch_count']}",
        f"- legal 4C watch cases: {summary['legal_4c_watch_count']}",
        "- price_validation_completed: partial_with_reported_event_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | best trigger | candidate | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND296_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.best_trigger,
                    case.stage_candidate,
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
            "- Hyundai Rotem is the clearest missed-structural risk: shipment, OP estimate beat, revenue contribution and relative strength appeared together.",
            "- LIG Nex1 shows 4B can be a trim signal rather than a hard exit when new order pipeline remains.",
            "- Hanwha Aerospace needs Stage3-Yellow plus dilution 4B overlay, not Stage3 cancellation.",
            "- Shipbuilding basket moves beyond plain Stage2 when orders, pricing, backlog duration and sector relative strength align.",
            "- LS Electric needs full-window retest because immediate price failed despite strong U.S. grid evidence.",
            "- Samsung E&A supports Stage3-Yellow, but EPC cash, working capital and completion margin block Green.",
            "- Czech nuclear remains Stage2 plus legal 4C-watch until final contract and legal clearance.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round296_trigger_grid_markdown() -> str:
    company_by_case = {case.case_id: case.company_name for case in ROUND296_CASE_CANDIDATES}
    lines = [
        "# Round 296 Trigger Grid",
        "",
        "Trigger-level validation separates candidate quality from full OHLC completion. For example, a reported +9.3% event move can support Stage2-Actionable while full 90D/180D MFE is still marked missing.",
        "",
        "| trigger | case | company | type | date | evidence | event return | relative | promote_to |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for trigger in ROUND296_TRIGGER_RECORDS:
        lines.append(
            f"| {trigger.trigger_id} | {trigger.case_id} | {company_by_case.get(trigger.case_id, '')} | {trigger.trigger_type} | {trigger.trigger_date.isoformat()} | "
            f"{trigger.evidence_available} | {_value_text(trigger.event_return_pct)} | {_value_text(trigger.market_relative_return_pp)} | {trigger.promote_to} |"
        )
    return "\n".join(lines) + "\n"


def render_round296_stage_rules_markdown() -> str:
    lines = [
        "# Round 296 Stage2-Actionable / Stage3-Yellow Rules",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Stage2-Actionable Promotion Rules",
        "",
    ]
    lines.extend(f"- {rule}" for rule in ROUND296_STAGE2_ACTIONABLE_RULES)
    lines.extend(["", "## Stage3-Yellow Rules", ""])
    lines.extend(f"- {rule}" for rule in ROUND296_STAGE3_YELLOW_RULES)
    lines.extend(["", "## Green Blockers", ""])
    lines.extend(f"- {rule}" for rule in ROUND296_GREEN_BLOCKERS)
    lines.extend(["", "## Easy Examples", ""])
    lines.extend(
        [
            "- `preferred bidder` is Stage2 at most until final contract and legal clearance.",
            "- `$6B EPC order` can be Yellow when price reacts strongly, but Green waits for completion margin and cash collection.",
            "- `target +87%` with same-day -5.4% is not rejected; it needs full-window retest.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round296_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 296 R1 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND296_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND296_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "이번 R1 Loop 15에서 hard 4C 확정은 없다. Czech nuclear legal block, Hanwha dilution/disclosure, shipbuilding sanctions are watch items.",
            "",
            "## Case Review",
            "",
            "| case | company | 4B date | 4C watch | hard 4C | interpretation |",
            "|---|---|---|---|---|---|",
        ]
    )
    for case in ROUND296_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.company_name} | {_date_text(case.stage4b_date)} | {_date_text(case.stage4c_date)} | "
            f"{str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round296_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 296 R1 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_event_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Stage candidates are not downgraded merely because full OHLC is missing.",
        "- Do not invent 30D/90D/180D/1Y MFE/MAE, delivery margin, cash collection, legal clearance, or final contract data.",
        "",
        "## Case Anchors",
        "",
        "| case | data source | reported anchor | status |",
        "|---|---|---|---|",
    ]
    for case in ROUND296_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round296_r1_loop15_reports(
    output_directory: str | Path = ROUND296_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND296_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND296_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND296_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round296_case_records(), cases_path),
        "triggers": write_round296_triggers(triggers_path),
        "audit": _write_json(round296_audit_payload(), audit_path),
        "summary": output / "round296_r1_loop15_trigger_validation_summary.md",
        "case_matrix": output / "round296_r1_loop15_case_matrix.csv",
        "trigger_grid": output / "round296_r1_loop15_trigger_grid.csv",
        "target_aliases": output / "round296_r1_loop15_target_aliases.csv",
        "score_adjustments": output / "round296_r1_loop15_score_adjustments.csv",
        "shadow_weights": output / "round296_r1_loop15_shadow_weights.csv",
        "stage_rules": output / "round296_r1_loop15_stage_rules.md",
        "trigger_grid_md": output / "round296_r1_loop15_trigger_grid.md",
        "price_validation_plan": output / "round296_r1_loop15_price_validation_plan.md",
        "stage4b_4c_review": output / "round296_r1_loop15_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round296_summary_markdown(), encoding="utf-8")
    _write_csv(round296_case_rows(), paths["case_matrix"])
    _write_csv(round296_trigger_rows(), paths["trigger_grid"])
    _write_csv(round296_target_alias_rows(), paths["target_aliases"])
    _write_csv(round296_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round296_shadow_weight_rows(), paths["shadow_weights"])
    paths["stage_rules"].write_text(render_round296_stage_rules_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round296_trigger_grid_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round296_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round296_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def write_round296_triggers(path: str | Path = ROUND296_DEFAULT_TRIGGERS_PATH) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(trigger.as_dict(), ensure_ascii=False, sort_keys=True) for trigger in ROUND296_TRIGGER_RECORDS]
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return target


def _case_record(case: Round296CaseCandidate) -> E2RCaseRecord:
    return E2RCaseRecord(
        case_id=case.case_id,
        symbol=case.symbol,
        company_name=case.company_name,
        market="KR",
        sector_raw=ROUND296_LARGE_SECTOR,
        primary_archetype=case.primary_archetype,
        expected_group=case.expected_group,
        large_sector=ROUND296_LARGE_SECTOR,
        secondary_archetypes=case.secondary_archetypes,
        case_type=case.case_type,
        stage1_date=case.stage1_date,
        stage2_date=case.stage2_date,
        stage3_date=case.stage3_date,
        stage4b_date=case.stage4b_date,
        stage4c_date=case.stage4c_date,
        evidence_summary=case.notes,
        stage1_evidence=case.evidence_fields if case.stage1_date else (),
        stage2_evidence=case.evidence_fields if case.stage2_date else (),
        stage3_evidence=case.evidence_fields if case.stage3_date else (),
        stage4b_evidence=case.red_flag_fields if case.stage4b_date else (),
        stage4c_evidence=case.red_flag_fields if case.stage4c_date else (),
        must_have_fields=ROUND296_STAGE2_ACTIONABLE_RULES + ROUND296_STAGE3_YELLOW_RULES,
        red_flag_fields=case.red_flag_fields,
        key_evidence_fields=case.evidence_fields,
        false_positive_reason=case.round_stage_failure_label,
        score_price_alignment=case.score_price_alignment,
        rerating_result=case.rerating_result,
        stage_failure_type=case.stage_failure_type,
        price_pattern=case.round_alignment_label,
        score_weight_hint={},
        green_guardrails=(
            "production_scoring_changed_false",
            "candidate_generation_input_false",
            "shadow_weight_only_true",
            "full_adjusted_ohlc_complete_false",
            "stage_candidate_not_downgraded_for_missing_full_ohlc",
            "do_not_use_round296_cases_as_candidate_generation_input",
            "do_not_force_stage3_green_without_margin_cash_followthrough",
        ),
        notes=case.notes,
        price_validation=PriceValidation(
            stage1_price=case.stage1_price_anchor,
            stage2_price=case.stage2_price_anchor,
            stage3_price=case.stage3_price_anchor,
            stage4b_price=case.stage4b_price_anchor,
            stage4c_price=case.stage4c_price_anchor,
            mfe_30d=case.event_mfe_pct,
            mae_30d=case.event_mae_pct,
            price_validation_status=case.price_validation_status,
        ),
        data_quality=CaseDataQuality(official_data_available=False, report_data_available=True, price_data_available=False, stage_dates_confidence=0.7),
    )


def _case_row(case: Round296CaseCandidate) -> dict[str, str]:
    return {
        "case_id": case.case_id,
        "symbol": case.symbol,
        "company_name": case.company_name,
        "primary_archetype": case.primary_archetype.value,
        "secondary_archetypes": "|".join(item.value for item in case.secondary_archetypes),
        "case_type": case.case_type,
        "round_case_type": case.round_case_type,
        "best_trigger": case.best_trigger,
        "best_trigger_type": case.best_trigger_type,
        "stage_candidate": case.stage_candidate,
        "stage1_date": _date_text(case.stage1_date),
        "stage2_date": _date_text(case.stage2_date),
        "stage3_date": _date_text(case.stage3_date),
        "stage4b_date": _date_text(case.stage4b_date),
        "stage4c_date": _date_text(case.stage4c_date),
        "hard_4c_confirmed": str(case.hard_4c_confirmed).lower(),
        "trigger_outcome_label": case.trigger_outcome_label,
        "stage_gate_correction": case.stage_gate_correction,
        "evidence_fields": "|".join(case.evidence_fields),
        "red_flag_fields": "|".join(case.red_flag_fields),
        "price_data_source": case.price_data_source,
        "reported_price_anchor": case.reported_price_anchor,
        "reported_return_anchor": case.reported_return_anchor,
        "event_mfe_pct": _float_text(case.event_mfe_pct),
        "event_mae_pct": _float_text(case.event_mae_pct),
        "market_relative_return_pp": _float_text(case.market_relative_return_pp),
        "score_price_alignment": case.score_price_alignment,
        "round_alignment_label": case.round_alignment_label,
        "rerating_result": case.rerating_result,
        "round_rerating_label": case.round_rerating_label,
        "stage_failure_type": case.stage_failure_type,
        "round_stage_failure_label": case.round_stage_failure_label,
        "price_validation_status": case.price_validation_status,
        "extra_price_metrics": json.dumps(case.extra_price_metrics, ensure_ascii=False, sort_keys=True),
        "notes": case.notes,
    }


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


def _value_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:g}"
    return str(value)
