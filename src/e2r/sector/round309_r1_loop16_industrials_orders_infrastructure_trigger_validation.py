"""Round-309 R1 Loop-16 industrial orders and infrastructure validation pack.

This module converts ``docs/round/round_309.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a USD 6B EPC order can become Stage2-Actionable when the contract
size and event price reaction are clear. It still cannot become Stage3-Green
until margin, cash collection and cost-overrun evidence are visible.
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


ROUND309_SOURCE_ROUND_PATH = "docs/round/round_309.md"
ROUND309_ANALYST_ROUND_ID = "round_237"
ROUND309_LARGE_SECTOR = "INDUSTRIALS_ORDERS_INFRASTRUCTURE"
ROUND309_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND309_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round309_r1_loop16_industrials_orders_infrastructure_trigger_validation"
ROUND309_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop16_round237.jsonl"
ROUND309_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r1_loop16_round237.jsonl"
ROUND309_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round309_r1_loop16_industrials_orders_infrastructure_trigger_validation_audit.json"
ROUND309_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round237_r1_loop16_v1.csv"

ROUND309_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE": E2RArchetype.OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE.value,
    "GRID_TRANSFORMER_DATA_CENTER_STAGE2": E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_STAGE2.value,
    "SHIPBUILDING_MERGER_SCALE_STAGE2_WITH_INTEGRATION_4B": E2RArchetype.SHIPBUILDING_MERGER_SCALE_STAGE2_WITH_INTEGRATION_4B.value,
    "SHIPBUILDING_CONTRACT_WIN_STAGE2_ACTIONABLE": E2RArchetype.SHIPBUILDING_CONTRACT_WIN_STAGE2_ACTIONABLE.value,
    "SHIPBUILDING_ORDER_CANCELLATION_4C": E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_4C.value,
    "GEOPOLITICAL_SANCTION_SHIPBUILDING_4C_WATCH": E2RArchetype.GEOPOLITICAL_SANCTION_SHIPBUILDING_4C_WATCH.value,
    "ROBOTICS_STRATEGIC_CONTROL_STAGE2_WITH_ORDER_GATE": E2RArchetype.ROBOTICS_STRATEGIC_CONTROL_STAGE2_WITH_ORDER_GATE.value,
    "DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED": E2RArchetype.DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED.value,
    "AEROSPACE_EXPORT_CONTRACT_STAGE2": E2RArchetype.AEROSPACE_EXPORT_CONTRACT_STAGE2.value,
}

ROUND309_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "signed_contract_value_large_vs_annual_order_wins_or_backlog",
    "event_return_at_least_5pct",
    "market_relative_return_at_least_5pp",
    "buyer_scope_delivery_and_capacity_impact_specific",
    "company_specific_order_or_backlog_not_only_demand_cycle",
    "ASP_ship_price_or_transformer_price_pass_through_possible",
    "no_4c_overlay_cancellation_sanction_or_legal_dispute",
)

ROUND309_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_FCF_path_can_change_materially",
    "one_of_margin_cash_delivery_integration_capacity_still_open",
    "price_reaction_or_relative_strength_supports_the_trigger",
    "case_is_not_order_cancellation_sanction_or_price_muted_MA",
)

ROUND309_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "gross_margin_or_delivery_margin_confirmed",
    "cash_collection_or_working_capital_confirmed",
    "backlog_to_revenue_to_OP_conversion_confirmed",
    "capacity_or_integration_synergy_confirmed",
    "full_OHLC_backfill_supports_price_path",
    "4B_4C_overlay_cleared_or_contained",
)

ROUND309_GREEN_BLOCKERS: tuple[str, ...] = (
    "headline_order_without_margin",
    "transformer_demand_without_company_margin",
    "shipbuilding_order_without_delivery_margin",
    "merger_announcement_without_integration",
    "strategic_stake_without_orders",
    "MA_without_customer_orders",
    "geopolitical_opportunity_without_sanction_check",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND309_SCORE_UP_AXES: tuple[str, ...] = (
    "signed_contract_value_vs_backlog",
    "market_relative_event_strength",
    "grid_transformer_backlog_capacity",
    "shipbuilding_newbuilding_price_backlog",
    "merger_integration_synergy",
    "robotics_order_revenue_bridge",
    "geopolitical_sanction_overlay",
    "data_center_cooling_order_conversion",
)

ROUND309_SCORE_DOWN_AXES: tuple[str, ...] = (
    "headline_order_without_margin",
    "transformer_demand_without_company_margin",
    "shipbuilding_order_without_delivery_margin",
    "merger_announcement_without_integration",
    "strategic_stake_without_orders",
    "MA_without_customer_orders",
    "geopolitical_opportunity_without_sanction_check",
)

ROUND309_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "mega_order_rally_before_margin_and_cash_proof",
    "transformer_shortage_story_before_company_capacity_and_margin",
    "shipbuilding_merger_or_contract_rally_before_delivery_margin",
    "strategic_stake_or_MA_rerating_before_orders",
    "geopolitical_optionalities_ignore_sanction_scope",
)

ROUND309_4C_WATCH_GATES: tuple[str, ...] = (
    "order_cancellation",
    "customer_unilateral_termination",
    "arbitration_or_legal_dispute",
    "sanctions_blocking_business_with_key_market",
    "cost_overrun_destroying_EPC_margin",
    "ship_delivery_delay_or_cancellation",
    "strategic_MA_integration_failure",
    "transformer_capacity_expansion_failure_or_input_cost_squeeze",
)

ROUND309_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_what_happened_and_stage_candidate",
    "trigger_calibration_row_stores_event_anchor_contract_value_and_reported_return",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
)


@dataclass(frozen=True)
class Round309ShadowWeightRow:
    archetype: E2RArchetype
    signed_contract_value_vs_backlog: int
    market_relative_event_strength: int
    grid_transformer_backlog_capacity: int
    shipbuilding_newbuilding_price_backlog: int
    merger_integration_synergy: int
    robotics_order_revenue_bridge: int
    geopolitical_sanction_overlay: int
    data_center_cooling_order_conversion: int
    headline_order_without_margin_penalty: int
    transformer_demand_without_company_margin_penalty: int
    shipbuilding_order_without_delivery_margin_penalty: int
    merger_announcement_without_integration_penalty: int
    strategic_stake_without_orders_penalty: int
    ma_without_customer_orders_penalty: int
    geopolitical_opportunity_without_sanction_check_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "signed_contract_value_vs_backlog": _signed(self.signed_contract_value_vs_backlog),
            "market_relative_event_strength": _signed(self.market_relative_event_strength),
            "grid_transformer_backlog_capacity": _signed(self.grid_transformer_backlog_capacity),
            "shipbuilding_newbuilding_price_backlog": _signed(self.shipbuilding_newbuilding_price_backlog),
            "merger_integration_synergy": _signed(self.merger_integration_synergy),
            "robotics_order_revenue_bridge": _signed(self.robotics_order_revenue_bridge),
            "geopolitical_sanction_overlay": _signed(self.geopolitical_sanction_overlay),
            "data_center_cooling_order_conversion": _signed(self.data_center_cooling_order_conversion),
            "headline_order_without_margin_penalty": _signed(self.headline_order_without_margin_penalty),
            "transformer_demand_without_company_margin_penalty": _signed(self.transformer_demand_without_company_margin_penalty),
            "shipbuilding_order_without_delivery_margin_penalty": _signed(self.shipbuilding_order_without_delivery_margin_penalty),
            "merger_announcement_without_integration_penalty": _signed(self.merger_announcement_without_integration_penalty),
            "strategic_stake_without_orders_penalty": _signed(self.strategic_stake_without_orders_penalty),
            "MA_without_customer_orders_penalty": _signed(self.ma_without_customer_orders_penalty),
            "geopolitical_opportunity_without_sanction_check_penalty": _signed(self.geopolitical_opportunity_without_sanction_check_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round309TriggerRecord:
    trigger_id: str
    case_id: str
    trigger_type: str
    trigger_date: str
    evidence_available: str
    event_return_pct: float | str | None
    trigger_outcome_label: str
    promote_to: str
    extra_metrics: Mapping[str, object]

    def as_dict(self) -> dict[str, object]:
        return {
            "trigger_id": self.trigger_id,
            "case_id": self.case_id,
            "trigger_type": self.trigger_type,
            "trigger_date": self.trigger_date,
            "evidence_available": self.evidence_available,
            "event_return_pct": self.event_return_pct,
            "trigger_outcome_label": self.trigger_outcome_label,
            "promote_to": self.promote_to,
            "extra_metrics": dict(self.extra_metrics),
        }

    def as_row(self) -> dict[str, str]:
        row = {key: _value_text(value) for key, value in self.as_dict().items() if key != "extra_metrics"}
        row["extra_metrics"] = json.dumps(self.extra_metrics, ensure_ascii=False, sort_keys=True)
        return row


@dataclass(frozen=True)
class Round309CaseCandidate:
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
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    event_mfe_pct: float | None
    event_mae_pct: float | None
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, object]
    score_price_alignment: str
    round_alignment_label: str
    rerating_result: str
    stage_failure_type: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type

    def to_case_record(self) -> E2RCaseRecord:
        guardrails = [
            "production_scoring_changed_false",
            "candidate_generation_input_false",
            "shadow_weight_only_true",
            "full_adjusted_ohlc_complete_false",
            "stage_candidate_not_downgraded_for_missing_full_ohlc",
            "do_not_use_round309_cases_as_candidate_generation_input",
            "do_not_treat_order_merger_transformer_robotics_or_cooling_headline_as_green",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND309_LARGE_SECTOR,
            large_sector=ROUND309_LARGE_SECTOR,
            primary_archetype=self.primary_archetype,
            secondary_archetypes=self.secondary_archetypes,
            expected_group=self.expected_group,
            case_type=self.case_type,
            stage1_date=self.stage1_date,
            stage2_date=self.stage2_date,
            stage3_date=self.stage3_date,
            stage4b_date=self.stage4b_date,
            stage4c_date=self.stage4c_date,
            evidence_summary=self.notes,
            stage1_evidence=self.evidence_fields,
            stage2_evidence=self.evidence_fields if self.stage2_date else (),
            stage3_evidence=(),
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4b" in field or "integration" in field or "overheat" in field),
            stage4c_evidence=tuple(
                field
                for field in (*self.red_flag_fields, *self.evidence_fields)
                if "4c" in field or "cancellation" in field or "sanction" in field or "arbitration" in field
            ),
            must_have_fields=ROUND309_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.case_type in {"event_premium", "4b_watch", "4c_thesis_break", "failed_rerating"} else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern="reported_event_anchor_only",
            score_weight_hint={},
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(
                stage1_price=self.stage1_price_anchor,
                stage2_price=self.stage2_price_anchor,
                stage4b_price=self.stage4b_price_anchor,
                stage4c_price=self.stage4c_price_anchor,
                mfe_30d=self.event_mfe_pct,
                mae_30d=self.event_mae_pct,
                price_validation_status="price_data_unavailable_after_deep_search",
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.76 if not self.stage4c_date else 0.82,
            ),
        )

    def as_row(self) -> dict[str, str]:
        return {
            "case_id": self.case_id,
            "symbol": self.symbol,
            "company_name": self.company_name,
            "primary_archetype": self.primary_archetype.value,
            "secondary_archetypes": "|".join(archetype.value for archetype in self.secondary_archetypes),
            "case_type": self.case_type,
            "round_case_type": self.round_case_type,
            "best_trigger": self.best_trigger,
            "best_trigger_type": self.best_trigger_type,
            "stage_candidate": self.stage_candidate,
            "stage1_date": _date_text(self.stage1_date),
            "stage2_date": _date_text(self.stage2_date),
            "stage3_date": _date_text(self.stage3_date),
            "stage4b_date": _date_text(self.stage4b_date),
            "stage4c_date": _date_text(self.stage4c_date),
            "hard_4c_confirmed": str(self.hard_4c_confirmed).lower(),
            "evidence_fields": "|".join(self.evidence_fields),
            "red_flag_fields": "|".join(self.red_flag_fields),
            "event_mfe_pct": _value_text(self.event_mfe_pct),
            "event_mae_pct": _value_text(self.event_mae_pct),
            "stage1_price_anchor": _value_text(self.stage1_price_anchor),
            "stage2_price_anchor": _value_text(self.stage2_price_anchor),
            "stage4b_price_anchor": _value_text(self.stage4b_price_anchor),
            "stage4c_price_anchor": _value_text(self.stage4c_price_anchor),
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND309_CASE_CANDIDATES: tuple[Round309CaseCandidate, ...] = (
    Round309CaseCandidate(
        case_id="r1_loop16_samsung_ea_fadhili",
        symbol="028050",
        company_name="Samsung E&A",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE,
        secondary_archetypes=(E2RArchetype.OVERSEAS_EPC_ORDER_STAGE2_YELLOW, E2RArchetype.ORDER_HEADLINE_NOT_MARGIN_GREEN),
        case_type="success_candidate",
        round_case_type="overseas_epc_stage2_actionable_yellow_candidate",
        best_trigger="r1l16_samsungea_fadhili_T1",
        best_trigger_type="Stage2-Actionable_to_Stage3-Yellow_candidate",
        stage_candidate="Stage2-Actionable / Stage3-Yellow candidate",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 3),
        stage3_date=None,
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("contract_value_usd_6bn", "aramco_total_package_usd_7_7bn", "event_return_8_5pct", "market_relative_9_9pp", "average_annual_contract_wins_8_6tn_krw", "completion_target_2027_11"),
        red_flag_fields=("gross_margin_missing", "cash_collection_missing", "cost_overrun_visibility_missing", "Saudi_execution_delay_risk", "backlog_to_OP_conversion_missing"),
        event_mfe_pct=8.5,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=26750,
        stage4b_price_anchor=26750,
        stage4c_price_anchor=None,
        extra_price_metrics={"contract_value_usd_bn": 6.0, "aramco_total_package_usd_bn": 7.7, "event_price_high_krw": 26750, "event_return_pct": 8.5, "kospi_same_context_pct": -1.4, "market_relative_return_pp": 9.9, "average_annual_contract_wins_2017_2023_krw_trn": 8.6, "completion_target": "2027-11"},
        score_price_alignment="aligned",
        round_alignment_label="excellent_stage2_actionable",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        notes="Large signed EPC contract plus strong relative price reaction. Green requires margin, cash collection, cost overrun and backlog-to-OP conversion.",
    ),
    Round309CaseCandidate(
        case_id="r1_loop16_ls_electric_us_transformer",
        symbol="010120",
        company_name="LS Electric",
        primary_archetype=E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_STAGE2,
        secondary_archetypes=(E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2, E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2),
        case_type="success_candidate",
        round_case_type="grid_transformer_stage2_event_price_not_confirmed",
        best_trigger="r1l16_lselectric_transformer_T1",
        best_trigger_type="Stage2_event_to_Actionable_candidate",
        stage_candidate="Stage2 event / Actionable candidate pending margin",
        stage1_date=date(2024, 7, 1),
        stage2_date=date(2025, 11, 1),
        stage3_date=None,
        stage4b_date=date(2026, 5, 11),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("us_revenue_share_2024e_20pct", "target_price_raise_87pct", "contract_value_usd_312mn", "525kV_transformer_contract", "data_center_end_market", "GSU_demand_growth_274pct", "lead_time_4_years"),
        red_flag_fields=("LS_specific_backlog_missing", "capacity_expansion_missing", "ASP_margin_missing", "copper_GOES_cost_pass_through_missing", "delivery_execution_missing"),
        event_mfe_pct=None,
        event_mae_pct=-5.4,
        stage1_price_anchor=208500,
        stage2_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"t0_price_krw": 208500, "t0_event_return_pct": -5.4, "us_revenue_share_2022_pct": "<5", "us_revenue_share_2024e_pct": 20, "target_price_raise_pct": 87, "target_price_krw": 280000, "t1_contract_value_usd_mn": 312, "us_gsu_transformer_demand_growth_since_2019_pct": 274, "us_substation_transformer_demand_growth_since_2019_pct": 116, "transformer_price_rise_5y_pct": 80, "large_transformer_lead_time_years": 4},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="Stage2_grid_event_not_Green",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        notes="Grid transformer demand is structural, but LS-specific backlog, capacity, margin and delivery gates remain open.",
    ),
    Round309CaseCandidate(
        case_id="r1_loop16_hd_hyundai_heavy_mipo_merger",
        symbol="329180/010620",
        company_name="HD Hyundai Heavy Industries / HD Hyundai Mipo",
        primary_archetype=E2RArchetype.SHIPBUILDING_MERGER_SCALE_STAGE2_WITH_INTEGRATION_4B,
        secondary_archetypes=(E2RArchetype.SHIPBUILDING_MERGER_MASGA_4B, E2RArchetype.US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION),
        case_type="4b_watch",
        round_case_type="shipbuilding_merger_stage2_actionable_integration_4b",
        best_trigger="r1l16_hhi_mipo_merger_T1",
        best_trigger_type="Stage2-Actionable_with_integration_4B",
        stage_candidate="Stage2-Actionable + 4B-watch",
        stage1_date=date(2025, 8, 27),
        stage2_date=date(2025, 8, 27),
        stage3_date=None,
        stage4b_date=date(2025, 8, 27),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("merger_for_us_shipbuilding_expansion", "hhi_event_return_11_3pct", "mipo_event_return_14_6pct", "both_record_highs", "share_exchange_ratio_specific", "MASGA_optionalities"),
        red_flag_fields=("merger_completion_missing", "US_contract_awards_missing", "integration_synergy_missing", "yard_capacity_utilization_missing", "margin_after_integration_missing", "4b_integration_overlay_required"),
        event_mfe_pct=14.6,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hd_hyundai_heavy_event_return_pct": 11.3, "hd_hyundai_mipo_event_return_pct": 14.6, "event_price_status": "both_record_highs", "share_exchange_ratio": "1_HD_Hyundai_Mipo_share_for_1.04059146_HD_Hyundai_Heavy_shares"},
        score_price_alignment="aligned",
        round_alignment_label="Stage2_Actionable_with_4B_integration_overlay",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        notes="Merger and U.S. shipbuilding optionality are actionable, but integration and customer-order conversion remain gates.",
    ),
    Round309CaseCandidate(
        case_id="r1_loop16_shipbuilding_contract_win_basket",
        symbol="010140/042660/329180",
        company_name="Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy",
        primary_archetype=E2RArchetype.SHIPBUILDING_CONTRACT_WIN_STAGE2_ACTIONABLE,
        secondary_archetypes=(E2RArchetype.SHIPBUILDING_BACKLOG_PRICE_STAGE2_ACTIONABLE, E2RArchetype.SHIPBUILDING_CONTRACT_CYCLE_4B),
        case_type="success_candidate",
        round_case_type="shipbuilding_contract_win_stage2_actionable_basket",
        best_trigger="r1l16_shipbuilding_basket_T1",
        best_trigger_type="Stage2-Actionable_basket",
        stage_candidate="Stage2-Actionable basket / Stage3-Yellow candidate pending delivery margin",
        stage1_date=date(2024, 3, 1),
        stage2_date=date(2024, 3, 1),
        stage3_date=None,
        stage4b_date=date(2024, 3, 1),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("samsung_heavy_event_return_16pct", "hanwha_ocean_event_return_13pct", "hd_hyundai_heavy_event_return_11pct", "korea_global_shipbuilding_order_share_50pct", "newbuilding_price_index_rising"),
        red_flag_fields=("company_specific_order_backlog_missing", "steel_cost_pass_through_missing", "delivery_schedule_missing", "gross_margin_missing", "working_capital_missing", "customer_cancellation_risk"),
        event_mfe_pct=16.0,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_heavy_event_return_pct": 16, "hanwha_ocean_event_return_pct": 13, "hd_hyundai_heavy_event_return_pct": 11, "korea_global_shipbuilding_order_share_feb_pct": 50, "newbuilding_price_index_trend": "rising"},
        score_price_alignment="aligned",
        round_alignment_label="Stage2_promote_candidate_basket",
        rerating_result="cyclical_rerating",
        stage_failure_type="stage2_watch_success",
        notes="Contract wins and ship-price momentum are actionable; delivery margin, steel cost and working capital are Green gates.",
    ),
    Round309CaseCandidate(
        case_id="r1_loop16_samsung_heavy_zvezda_cancellation",
        symbol="010140",
        company_name="Samsung Heavy Industries",
        primary_archetype=E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_4C,
        secondary_archetypes=(E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_HARD_4C, E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="order_cancellation_4c_watch",
        best_trigger="r1l16_samsungheavy_zvezda_T1",
        best_trigger_type="4C_watch_order_cancellation",
        stage_candidate="4C-watch",
        stage1_date=date(2020, 1, 1),
        stage2_date=date(2020, 1, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 6, 18),
        hard_4c_confirmed=False,
        evidence_fields=("cancelled_order_value_4_85tn_krw", "cancelled_order_value_3_54bn_usd", "icebreaker_LNG_carrier_blocks", "icebreaker_shuttle_tanker_parts", "Zvezda_counterparty", "Singapore_arbitration"),
        red_flag_fields=("order_cancellation", "counterparty_unilateral_termination", "arbitration", "Russia_Ukraine_uncertainty", "4c_watch_required"),
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"cancelled_order_value_krw_trn": 4.85, "cancelled_order_value_usd_bn": 3.54, "cancelled_scope": ["10_icebreaker_LNG_carrier_parts_blocks", "7_icebreaker_shuttle_tanker_parts_blocks"], "counterparty": "Zvezda", "arbitration": "Singapore"},
        score_price_alignment="aligned",
        round_alignment_label="order_cancellation_4C_watch",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        notes="Large shipbuilding order cancellation is an R1 4C-watch trigger; do not keep cancelled backlog as visibility.",
    ),
    Round309CaseCandidate(
        case_id="r1_loop16_hanwha_ocean_china_sanctions",
        symbol="042660/329180_readthrough",
        company_name="Hanwha Ocean / HD Hyundai Heavy read-through",
        primary_archetype=E2RArchetype.GEOPOLITICAL_SANCTION_SHIPBUILDING_4C_WATCH,
        secondary_archetypes=(E2RArchetype.SHIPBUILDING_GEOPOLITICAL_SANCTION_4C, E2RArchetype.NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B),
        case_type="4c_thesis_break",
        round_case_type="shipbuilding_geopolitical_sanction_4c_watch",
        best_trigger="r1l16_hanwhaocean_china_T1",
        best_trigger_type="4C_watch_geopolitical_sanction",
        stage_candidate="4C-watch",
        stage1_date=date(2025, 10, 14),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 10, 14),
        hard_4c_confirmed=False,
        evidence_fields=("five_us_linked_units_sanctioned", "hanwha_ocean_event_return_minus_5_8pct", "hd_hyundai_heavy_event_return_minus_4_1pct", "US_China_port_fees_context", "Hanwha_Philly_Shipyard_context"),
        red_flag_fields=("China_sanctions", "geopolitical_4c_watch", "sanction_scope_unclear", "contract_protection_missing", "maritime_conflict_overlay"),
        event_mfe_pct=None,
        event_mae_pct=-5.8,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"sanctioned_units_count": 5, "hanwha_ocean_event_return_pct": -5.8, "hd_hyundai_heavy_event_return_pct": -4.1, "policy_context": ["U.S._China_port_fees", "U.S._shipbuilding_probe", "Hanwha_Philly_Shipyard", "U.S._maritime_capacity_rebuild"]},
        score_price_alignment="aligned",
        round_alignment_label="geopolitical_4C_watch",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        notes="U.S. shipbuilding optionality carries China sanction and geopolitical overlay; Green needs contract protection and sanction clarity.",
    ),
    Round309CaseCandidate(
        case_id="r1_loop16_rainbow_robotics_samsung_control",
        symbol="277810",
        company_name="Rainbow Robotics",
        primary_archetype=E2RArchetype.ROBOTICS_STRATEGIC_CONTROL_STAGE2_WITH_ORDER_GATE,
        secondary_archetypes=(E2RArchetype.ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM, E2RArchetype.INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION),
        case_type="success_candidate",
        round_case_type="robotics_strategic_control_stage2_with_order_gate",
        best_trigger="r1l16_rainbow_samsung_T1",
        best_trigger_type="Stage2_strategic_control_with_order_gate",
        stage_candidate="Stage2 strategic control / Yellow blocked until orders",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 12, 30),
        stage3_date=None,
        stage4b_date=date(2024, 12, 30),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("Samsung_largest_shareholder", "additional_stake_267bn_krw", "additional_stake_181mn_usd", "prior_stake_14_71pct", "Future_Robotics_Office"),
        red_flag_fields=("Samsung_factory_deployment_missing", "external_robot_orders_missing", "unit_economics_missing", "recurring_service_revenue_missing", "supply_chain_capacity_missing", "strategic_stake_without_orders"),
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_additional_stake_krw_bn": 267, "samsung_additional_stake_usd_mn": 181, "samsung_prior_stake_pct": 14.71, "future_robotics_office": True},
        score_price_alignment="unknown",
        round_alignment_label="Stage2_strategic_control_not_Green",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        notes="Samsung control stake is Stage2, not revenue. Robot orders, deployment and unit economics are required before Yellow.",
    ),
    Round309CaseCandidate(
        case_id="r1_loop16_samsung_flaktgroup_datacenter_cooling",
        symbol="005930",
        company_name="Samsung Electronics / FlaktGroup",
        primary_archetype=E2RArchetype.DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED,
        secondary_archetypes=(E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE, E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED),
        case_type="failed_rerating",
        round_case_type="data_center_cooling_ma_stage2_price_muted",
        best_trigger="r1l16_samsung_flakt_T1",
        best_trigger_type="Stage2_MA_price_muted",
        stage_candidate="Stage2 M&A / Green blocked",
        stage1_date=date(2025, 5, 14),
        stage2_date=date(2025, 5, 14),
        stage3_date=None,
        stage4b_date=date(2025, 5, 14),
        stage4c_date=None,
        hard_4c_confirmed=False,
        evidence_fields=("FlaktGroup_acquisition_1_5bn_eur", "FlaktGroup_acquisition_1_68bn_usd", "AI_data_center_cooling_focus", "HVAC_commercial_cooling", "Samsung_event_return_0_7pct"),
        red_flag_fields=("data_center_cooling_orders_missing", "integration_margin_missing", "global_customer_wins_missing", "capex_ROI_missing", "recurring_service_revenue_missing", "price_muted"),
        event_mfe_pct=0.7,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"acquisition_value_eur_bn": 1.5, "acquisition_value_usd_bn": 1.68, "event_return_pct": 0.7, "market_pushback": ["not_chip_business_MA", "not_game_changing_deal", "appliance_HVAC_reinforcement"]},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_muted",
        rerating_result="no_rerating",
        stage_failure_type="false_yellow",
        notes="Data-center cooling M&A is real evidence, but Samsung's muted price reaction and missing customer orders block Green.",
    ),
)


ROUND309_TRIGGER_RECORDS: tuple[Round309TriggerRecord, ...] = (
    Round309TriggerRecord("r1l16_samsungea_fadhili_T1", "r1_loop16_samsung_ea_fadhili", "Stage2-Actionable", "2024-04-03", "Samsung E&A signs around $6B Saudi Aramco Fadhili contract; shares +8.5% to KRW26,750 while KOSPI -1.4%", 8.5, "excellent_stage2_actionable", "Stage3-Yellow_candidate", {"contract_value_usd_bn": 6.0, "market_relative_return_pp": 9.9}),
    Round309TriggerRecord("r1l16_lselectric_transformer_T1", "r1_loop16_ls_electric_us_transformer", "Stage2_event", "2025-11/2026-05-11", "LS Electric $312M U.S. utility contract for 525kV transformers to data center; U.S. transformer demand and prices sharply higher", "price_data_unavailable_after_deep_search", "Stage2_grid_event_not_Green", "Stage2", {"contract_value_usd_mn": 312, "transformer_price_rise_5y_pct": 80, "large_transformer_lead_time_years": 4}),
    Round309TriggerRecord("r1l16_hhi_mipo_merger_T1", "r1_loop16_hd_hyundai_heavy_mipo_merger", "Stage2-Actionable+4B-watch", "2025-08-27", "HD Hyundai Heavy to merge with HD Hyundai Mipo for U.S. shipbuilding expansion; HHI +11.3%, Mipo +14.6%, both record highs", "HHI +11.3 / Mipo +14.6", "Stage2_Actionable_with_4B_integration_overlay", "Stage2-Actionable+4B", {"hd_hyundai_heavy_event_return_pct": 11.3, "hd_hyundai_mipo_event_return_pct": 14.6}),
    Round309TriggerRecord("r1l16_shipbuilding_basket_T1", "r1_loop16_shipbuilding_contract_win_basket", "Stage2-Actionable_basket", "2024-03", "South Korean shipbuilders rally on brisk contract wins; Samsung Heavy +16%, Hanwha Ocean +13%, HD Hyundai Heavy +11%; Korea 50% of February global orders", "16/13/11", "Stage2_promote_candidate_basket", "Stage2-Actionable", {"samsung_heavy_event_return_pct": 16, "hanwha_ocean_event_return_pct": 13, "hd_hyundai_heavy_event_return_pct": 11}),
    Round309TriggerRecord("r1l16_samsungheavy_zvezda_T1", "r1_loop16_samsung_heavy_zvezda_cancellation", "4C-watch", "2025-06-18", "Samsung Heavy cancels 4.85T won / $3.54B Zvezda icebreaker LNG/shuttle tanker orders and pursues arbitration", "price_data_unavailable_after_deep_search", "order_cancellation_4C_watch", "4C-watch", {"cancelled_order_value_krw_trn": 4.85, "cancelled_order_value_usd_bn": 3.54, "arbitration": "Singapore"}),
    Round309TriggerRecord("r1l16_hanwhaocean_china_T1", "r1_loop16_hanwha_ocean_china_sanctions", "4C-watch", "2025-10-14", "China sanctions five U.S.-linked Hanwha Ocean subsidiaries; Hanwha Ocean -5.8%, HD Hyundai Heavy -4.1%", -5.8, "geopolitical_4C_watch", "4C-watch", {"sanctioned_units_count": 5, "hd_hyundai_heavy_event_return_pct": -4.1}),
    Round309TriggerRecord("r1l16_rainbow_samsung_T1", "r1_loop16_rainbow_robotics_samsung_control", "Stage2_strategic_control", "2024-12-30", "Samsung becomes largest shareholder of Rainbow Robotics via 267B won additional stake and creates Future Robotics Office", "price_data_unavailable_after_deep_search", "Stage2_strategic_control_not_Green", "Stage2", {"samsung_additional_stake_krw_bn": 267, "samsung_prior_stake_pct": 14.71}),
    Round309TriggerRecord("r1l16_samsung_flakt_T1", "r1_loop16_samsung_flaktgroup_datacenter_cooling", "Stage2_MA_price_muted", "2025-05-14", "Samsung buys FlaktGroup for EUR1.5B / $1.68B to strengthen AI data-center cooling; shares +0.7%", 0.7, "evidence_good_but_price_muted", "Stage2_only", {"acquisition_value_eur_bn": 1.5, "acquisition_value_usd_bn": 1.68}),
)


ROUND309_SHADOW_WEIGHT_ROWS: tuple[Round309ShadowWeightRow, ...] = (
    Round309ShadowWeightRow(E2RArchetype.OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE, 5, 4, 0, 0, 0, 0, 2, 0, -5, -1, -1, -1, -1, 0, -1, "large signed contract+relative strength", "margin/cash missing", "backlog-to-OP+cash", "Samsung E&A Fadhili."),
    Round309ShadowWeightRow(E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_STAGE2, 2, 2, 5, 0, 0, 0, 1, 1, -2, -5, -1, -1, -1, 0, -1, "transformer shortage+data-center order", "company margin/capacity missing", "backlog+capacity+ASP margin", "LS Electric U.S. transformer."),
    Round309ShadowWeightRow(E2RArchetype.SHIPBUILDING_MERGER_SCALE_STAGE2_WITH_INTEGRATION_4B, 1, 4, 0, 5, 5, 0, 4, 0, -2, -1, -4, -5, -1, 0, -2, "merger+record-high rally", "integration/U.S. contracts pending", "synergy+contracts+margin", "HD Hyundai Heavy/Mipo."),
    Round309ShadowWeightRow(E2RArchetype.SHIPBUILDING_CONTRACT_WIN_STAGE2_ACTIONABLE, 3, 5, 0, 5, 1, 0, 3, 0, -3, -1, -5, -2, -1, 0, -2, "sector order wins+price momentum", "delivery margin missing", "delivery+steel cost+margin", "Shipbuilding basket."),
    Round309ShadowWeightRow(E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_4C, 0, 0, 0, 2, 0, 0, 5, 0, -1, -1, -1, -1, -1, 0, -1, "order cancellation/arbitration", "damages recovery pending", "N/A", "Samsung Heavy Zvezda."),
    Round309ShadowWeightRow(E2RArchetype.GEOPOLITICAL_SANCTION_SHIPBUILDING_4C_WATCH, 0, 0, 0, 3, 0, 0, 5, 0, -1, -1, -2, -1, -1, 0, -5, "sanctions/port-fee conflict", "scope clarity pending", "N/A", "Hanwha Ocean China sanctions."),
    Round309ShadowWeightRow(E2RArchetype.ROBOTICS_STRATEGIC_CONTROL_STAGE2_WITH_ORDER_GATE, 0, 2, 0, 0, 1, 5, 1, 0, -1, -1, -1, -1, -5, 0, -1, "strategic shareholder/future office", "orders/deployment missing", "robot orders+unit economics", "Rainbow Robotics."),
    Round309ShadowWeightRow(E2RArchetype.DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED, 1, 1, 1, 0, 3, 0, 1, 5, -1, -2, -1, -2, -1, -4, -1, "M&A for data-center cooling", "orders/integration margin missing", "cooling orders+margin", "Samsung FlaktGroup."),
    Round309ShadowWeightRow(E2RArchetype.AEROSPACE_EXPORT_CONTRACT_STAGE2, 4, 3, 0, 0, 0, 0, 2, 0, -4, -1, -1, -1, -1, 0, -1, "signed aerospace export contract", "delivery/margin missing", "delivery+cash+approval continuity", "No case in R1 Loop16; target retained for next aerospace round."),
)


def round309_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND309_CASE_CANDIDATES]


def round309_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND309_CASE_CANDIDATES]


def round309_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND309_TRIGGER_RECORDS]


def round309_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND309_SHADOW_WEIGHT_ROWS]


def round309_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND309_REQUIRED_TARGET_ALIASES.items()]


def round309_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND309_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND309_SCORE_DOWN_AXES]
    )


def round309_summary() -> dict[str, object]:
    return {
        "source_round": ROUND309_SOURCE_ROUND_PATH,
        "round_id": ROUND309_ANALYST_ROUND_ID,
        "large_sector": ROUND309_LARGE_SECTOR,
        "method": ROUND309_METHOD,
        "case_candidate_count": len(ROUND309_CASE_CANDIDATES),
        "trigger_count": len(ROUND309_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND309_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 3,
        "stage2_event_candidate_count": 3,
        "stage3_yellow_candidate_count": 4,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 4,
        "stage4c_watch_count": 2,
        "hard_4c_case_count": 0,
        "evidence_good_but_price_muted_count": 2,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round309_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND309_SOURCE_ROUND_PATH,
        "round_id": ROUND309_ANALYST_ROUND_ID,
        "large_sector": ROUND309_LARGE_SECTOR,
        "method": ROUND309_METHOD,
        "summary": round309_summary(),
        "required_target_aliases": dict(ROUND309_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND309_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND309_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND309_STAGE3_GREEN_RULES,
        "green_blockers": ROUND309_GREEN_BLOCKERS,
        "score_up_axes": ROUND309_SCORE_UP_AXES,
        "score_down_axes": ROUND309_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND309_STAGE4B_WATCH_TRIGGERS,
        "stage4c_watch_gates": ROUND309_4C_WATCH_GATES,
        "row_separation_rules": ROUND309_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round309_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_order_merger_transformer_robotics_or_cooling_headline_as_green",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round309_summary_markdown() -> str:
    summary = round309_summary()
    lines = [
        "# R1 Loop 16 Industrials / Orders / Infrastructure Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: Samsung E&A's Fadhili order can be Stage2-Actionable because contract value and relative price reaction are clear. It is not Stage3-Green until margin and cash conversion are verified.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Signed order, merger, transformer shortage, robotics stake, or cooling M&A headlines are not enough for Green.",
            "- Stage2-Actionable needs contract size, event strength, company-specific backlog and no 4C overlay.",
            "- Stage3-Green confirmed: `0`.",
            "- Case rows, trigger rows and OHLC backfill rows must stay separate.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round309_trigger_grid_markdown() -> str:
    lines = [
        "# Round 309 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round309_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round309_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 309 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND309_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND309_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND309_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND309_GREEN_BLOCKERS),
            "",
            "## 4C Watch Gates",
            *_bullet_lines(ROUND309_4C_WATCH_GATES),
        ]
    ) + "\n"


def render_round309_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 309 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND309_STAGE4B_WATCH_TRIGGERS),
        "",
        "## 4C Watch Gates",
        *_bullet_lines(ROUND309_4C_WATCH_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND309_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round309_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 309 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND309_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round309_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 309 Row Separation Plan",
        "",
        "Case evidence, trigger anchors and full OHLC windows must be separate rows.",
        "",
        "Easy example: LS Electric can be a valid Stage2 grid event even if 30D/90D OHLC is not backfilled yet. It still cannot become Green without company backlog, capacity and margin.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND309_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round309_r1_loop16_reports(
    output_directory: str | Path = ROUND309_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND309_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND309_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND309_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND309_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round309_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND309_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round309_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round309_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round309_r1_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round309_r1_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round309_r1_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round309_r1_loop16_trigger_grid.md",
        "summary": output_dir / "round309_r1_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round309_r1_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round309_r1_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round309_r1_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round309_r1_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round309_r1_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round309_r1_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round309_case_rows())
    _write_csv(paths["target_aliases"], round309_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round309_trigger_rows())
    _write_csv(paths["score_adjustments"], round309_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round309_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round309_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round309_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round309_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round309_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round309_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round309_row_separation_plan_markdown(), encoding="utf-8")
    return paths


def _write_csv(path: Path, rows: Iterable[Mapping[str, str]]) -> None:
    rows = list(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _write_jsonl(path: Path, rows: Iterable[Mapping[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _signed(value: int) -> str:
    return f"{value:+d}" if value else "+0"


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    return str(value)


def _bullet_lines(items: Iterable[str]) -> list[str]:
    return [f"- {item}" for item in items]


__all__ = [
    "ROUND309_4C_WATCH_GATES",
    "ROUND309_CASE_CANDIDATES",
    "ROUND309_GREEN_BLOCKERS",
    "ROUND309_LARGE_SECTOR",
    "ROUND309_REQUIRED_TARGET_ALIASES",
    "ROUND309_ROW_SEPARATION_RULES",
    "ROUND309_SCORE_DOWN_AXES",
    "ROUND309_SCORE_UP_AXES",
    "ROUND309_SHADOW_WEIGHT_ROWS",
    "ROUND309_STAGE2_ACTIONABLE_RULES",
    "ROUND309_STAGE3_GREEN_RULES",
    "ROUND309_STAGE3_YELLOW_RULES",
    "ROUND309_STAGE4B_WATCH_TRIGGERS",
    "ROUND309_TRIGGER_RECORDS",
    "render_round309_stage4b_4c_review_markdown",
    "render_round309_stage_rules_markdown",
    "render_round309_trigger_grid_markdown",
    "round309_audit_payload",
    "round309_case_records",
    "round309_case_rows",
    "round309_shadow_weight_rows",
    "round309_summary",
    "round309_trigger_rows",
    "write_round309_r1_loop16_reports",
]
