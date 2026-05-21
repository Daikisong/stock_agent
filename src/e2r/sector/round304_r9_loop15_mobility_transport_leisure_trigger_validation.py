"""Round-304 R9 Loop-15 mobility/transport/leisure trigger validation pack.

This module converts ``docs/round/round_304.md`` into calibration-only case
records, trigger rows, shadow weights, and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a hybrid sales target and buyback can be Stage 2 evidence, but
it is not Stage 3-Green until actual hybrid mix, ASP/margin, tariff absorption,
and buyback execution are visible. Likewise, a fatal airline accident is not a
temporary price dip; it is a hard 4C trust-break gate.
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


ROUND304_SOURCE_ROUND_PATH = "docs/round/round_304.md"
ROUND304_ANALYST_ROUND_ID = "round_232"
ROUND304_LARGE_SECTOR = "MOBILITY_TRANSPORT_LEISURE"
ROUND304_METHOD = "trigger_level_backtest_v1"
ROUND304_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round304_r9_loop15_mobility_transport_leisure_trigger_validation"
ROUND304_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r9_loop15_round232.jsonl"
ROUND304_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r9_loop15_round232.jsonl"
ROUND304_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round304_r9_loop15_mobility_transport_leisure_trigger_validation_audit.json"
ROUND304_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round232_r9_loop15_v1.csv"

ROUND304_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW": E2RArchetype.HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW.value,
    "AUTO_TARIFF_MARGIN_4C_WATCH": E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH.value,
    "ROBOTICS_OPTIONALITY_STAGE2_WITH_4B": E2RArchetype.ROBOTICS_OPTIONALITY_STAGE2_WITH_4B.value,
    "AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C": E2RArchetype.AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C.value,
    "AIRLINE_CONSOLIDATION_STAGE2": E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2.value,
    "AIRLINE_SAFETY_HARD_4C": E2RArchetype.AIRLINE_SAFETY_HARD_4C.value,
    "TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE": E2RArchetype.TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE.value,
    "CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B": E2RArchetype.CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B.value,
}

ROUND304_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "hybrid_target_buyback_margin_target_or_tariff_pivot_is_quantified",
    "robotics_deployment_schedule_or_factory_capex_is_visible",
    "airline_merger_closing_has_integration_timeline_and_remedy_path",
    "visa_policy_or_freight_rate_event_has_multi_stock_or_index_price_confirmation",
    "event_day_or_reported_anchor_price_reaction_is_recorded_without_inventing_full_ohlc",
)

ROUND304_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "actual_vehicle_sales_mix_margin_or_shareholder_return_execution_partially_visible",
    "robotics_orders_or_factory_deployment_visible_but_unit_economics_pending",
    "airline_synergy_yield_or_load_factor_visible_but_integration_risk_remains",
    "tourism_arrivals_spending_or_yield_visible_but_policy_durability_pending",
    "freight_rates_convert_to_earnings_but_contract_mix_or_normalization_risk_remains",
)

ROUND304_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "hybrid_mix_margin_tariff_absorption_and_buyback_execution_all_visible",
    "robotics_external_orders_unit_economics_and_recurring_revenue_visible",
    "airline_integration_synergy_load_factor_yield_and_safety_trust_visible",
    "tourism_arrivals_spending_ADR_dutyfree_casino_and_airline_yield_convert_to_FCF",
    "freight_rate_duration_contract_mix_FCF_cash_return_and_capacity_discipline_visible",
    "full_window_mfe_mae_is_available_and_supportive",
)

ROUND304_GREEN_BLOCKERS: tuple[str, ...] = (
    "EV_growth_or_hybrid_target_headline_only",
    "shareholder_return_announcement_without_execution",
    "robotics_demo_or_factory_capex_without_orders",
    "localization_capex_without_workforce_compliance_and_safety",
    "airline_merger_closing_without_yield_load_factor_or_synergy",
    "fatal_airline_safety_event",
    "visa_policy_without_actual_spending_or_yield",
    "freight_spot_spike_without_contract_mix_or_duration",
)

ROUND304_SCORE_UP_AXES: tuple[str, ...] = (
    "hybrid_mix_margin_visibility",
    "actual_vehicle_sales_mix",
    "shareholder_return_execution",
    "tariff_absorption_capacity",
    "robotics_deployment_order_visibility",
    "localization_workforce_compliance",
    "airline_integration_synergy",
    "aviation_safety_trust",
    "tourism_spending_conversion",
    "freight_rate_duration_contract_mix",
)

ROUND304_SCORE_DOWN_AXES: tuple[str, ...] = (
    "ev_growth_headline_only",
    "localization_capex_headline_only",
    "robotics_optional_value_without_orders",
    "merger_closing_without_synergy",
    "fatal_safety_event",
    "visa_policy_without_spending",
    "freight_rate_spike_without_contract_mix",
)

ROUND304_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "robotics_optionality_rerates_before_orders_or_unit_economics",
    "airline_consolidation_premium_priced_before_synergy",
    "tourism_basket_prices_policy_before_spend_conversion",
    "freight_rate_spike_annualized_before_contract_duration",
    "hybrid_buyback_rerating_before_tariff_adjusted_margin",
)

ROUND304_HARD_4C_GATES: tuple[str, ...] = (
    "fatal_airline_safety_accident",
    "booking_cancellations_and_consumer_trust_collapse",
    "tariff_cost_crushing_OP_margin",
    "localization_workforce_visa_safety_or_compliance_break",
    "freight_normalization_and_overcapacity_after_spot_spike",
)


@dataclass(frozen=True)
class Round304ShadowWeightRow:
    archetype: E2RArchetype
    hybrid_mix_margin_visibility: int
    actual_vehicle_sales_mix: int
    shareholder_return_execution: int
    tariff_absorption_capacity: int
    robotics_deployment_order_visibility: int
    localization_workforce_compliance: int
    airline_integration_synergy: int
    aviation_safety_trust: int
    tourism_spending_conversion: int
    freight_rate_duration_contract_mix: int
    ev_growth_headline_only_penalty: int
    localization_capex_headline_only_penalty: int
    robotics_optional_value_without_orders_penalty: int
    merger_closing_without_synergy_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "hybrid_mix_margin_visibility": _signed(self.hybrid_mix_margin_visibility),
            "actual_vehicle_sales_mix": _signed(self.actual_vehicle_sales_mix),
            "shareholder_return_execution": _signed(self.shareholder_return_execution),
            "tariff_absorption_capacity": _signed(self.tariff_absorption_capacity),
            "robotics_deployment_order_visibility": _signed(self.robotics_deployment_order_visibility),
            "localization_workforce_compliance": _signed(self.localization_workforce_compliance),
            "airline_integration_synergy": _signed(self.airline_integration_synergy),
            "aviation_safety_trust": _signed(self.aviation_safety_trust),
            "tourism_spending_conversion": _signed(self.tourism_spending_conversion),
            "freight_rate_duration_contract_mix": _signed(self.freight_rate_duration_contract_mix),
            "ev_growth_headline_only_penalty": _signed(self.ev_growth_headline_only_penalty),
            "localization_capex_headline_only_penalty": _signed(self.localization_capex_headline_only_penalty),
            "robotics_optional_value_without_orders_penalty": _signed(self.robotics_optional_value_without_orders_penalty),
            "merger_closing_without_synergy_penalty": _signed(self.merger_closing_without_synergy_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round304TriggerRecord:
    trigger_id: str
    case_id: str
    trigger_type: str
    trigger_date: date
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
            "trigger_date": self.trigger_date.isoformat(),
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
class Round304CaseCandidate:
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
            "do_not_use_round304_cases_as_candidate_generation_input",
            "do_not_treat_mobility_transport_leisure_headline_as_green",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND304_LARGE_SECTOR,
            large_sector=ROUND304_LARGE_SECTOR,
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
            stage1_evidence=self.evidence_fields if self.stage1_date else (),
            stage2_evidence=self.evidence_fields if self.stage2_date else (),
            stage3_evidence=self.evidence_fields if self.stage3_date else (),
            stage4b_evidence=self.red_flag_fields if self.stage4b_date else (),
            stage4c_evidence=self.red_flag_fields if self.stage4c_date else (),
            must_have_fields=ROUND304_STAGE2_ACTIONABLE_RULES + ROUND304_STAGE3_YELLOW_RULES + ROUND304_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.red_flag_fields else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern=self.round_alignment_label,
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(
                mfe_30d=self.event_mfe_pct if self.event_mfe_pct and self.event_mfe_pct > 0 else None,
                mae_30d=self.event_mae_pct if self.event_mae_pct and self.event_mae_pct < 0 else None,
                price_validation_status="reported_event_anchor_not_full_ohlc",
            ),
            data_quality=CaseDataQuality(False, True, False, 0.67),
        )

    def as_row(self) -> dict[str, str]:
        return {
            "case_id": self.case_id,
            "symbol": self.symbol,
            "company_name": self.company_name,
            "primary_archetype": self.primary_archetype.value,
            "secondary_archetypes": ";".join(item.value for item in self.secondary_archetypes),
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
            "evidence_fields": ";".join(self.evidence_fields),
            "red_flag_fields": ";".join(self.red_flag_fields),
            "event_mfe_pct": _value_text(self.event_mfe_pct),
            "event_mae_pct": _value_text(self.event_mae_pct),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "price_validation_status": "reported_event_anchor_not_full_ohlc",
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "notes": self.notes,
        }


ROUND304_SHADOW_WEIGHT_ROWS: tuple[Round304ShadowWeightRow, ...] = (
    Round304ShadowWeightRow(E2RArchetype.HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW, 5, 5, 4, 4, 0, 2, 0, 1, 0, 0, -5, -2, -1, -1, "hybrid target+buyback+margin target", "actual mix/margin pending", "hybrid sales+margin+buyback execution", "Hyundai hybrid investor-day trigger."),
    Round304ShadowWeightRow(E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH, 4, 4, 2, 5, 0, 3, 0, 1, 0, 0, -5, -2, -1, -1, "tariff hit or EV target cut", "hybrid offset pending", "tariff absorption+hybrid margin", "Kia tariff and EV cut case."),
    Round304ShadowWeightRow(E2RArchetype.ROBOTICS_OPTIONALITY_STAGE2_WITH_4B, 1, 1, 1, 2, 5, 3, 0, 1, 0, 0, -2, -2, -5, -1, "robotics deployment/commercialization trigger", "orders/unit economics pending", "external orders+unit economics", "Hyundai/Boston Dynamics."),
    Round304ShadowWeightRow(E2RArchetype.AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C, 2, 2, 1, 5, 1, 5, 0, 2, 0, 0, -2, -5, -2, -1, "localization capex plus operational risk", "visa/workforce/safety pending", "stable local production+compliance", "Hyundai Georgia localization."),
    Round304ShadowWeightRow(E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2, 0, 0, 0, 1, 0, 0, 5, 5, 3, 0, -1, -1, -1, -4, "airline merger closing", "synergy/yield/load factor pending", "synergy+yield+load factor", "Korean Air-Asiana consolidation."),
    Round304ShadowWeightRow(E2RArchetype.AIRLINE_SAFETY_HARD_4C, 0, 0, 0, 1, 0, 0, 1, 5, 3, 0, -1, -1, -1, -1, "safety accident", "investigation/remediation pending", "safety trust recovery", "Jeju Air hard 4C."),
    Round304ShadowWeightRow(E2RArchetype.TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE, 0, 0, 0, 0, 0, 0, 1, 2, 5, 0, -1, -1, -1, -1, "visa policy+multi-stock rally", "arrivals/spending/yield pending", "spending/ADR/yield conversion", "Chinese tourism leisure basket."),
    Round304ShadowWeightRow(E2RArchetype.CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B, 0, 0, 2, 0, 0, 0, 0, 1, 0, 5, -1, -1, -1, -1, "freight-rate spike/capacity disruption", "HMM earnings/contract mix pending", "sustained rates+earnings+cash return", "HMM Red Sea freight cycle."),
)

ROUND304_TRIGGER_RECORDS: tuple[Round304TriggerRecord, ...] = (
    Round304TriggerRecord("r9l15_hyundai_hybrid_T1", "r9_loop15_hyundai_hybrid_shareholder_return", "Stage2-Actionable", date(2024, 8, 28), "Hyundai raises hybrid target by 40% to 1.33M by 2028, 14 hybrid models, 4T won buyback, 35% shareholder return target", 4.7, "Stage2_promote_candidate", "Stage3-Yellow_candidate", {"hybrid_target_2028_units_mn": 1.33, "hybrid_target_raise_pct": 40, "buyback_2025_2027_krw_trn": 4, "shareholder_return_target_pct": 35, "op_margin_target_2027_pct_range": "9-10"}),
    Round304TriggerRecord("r9l15_kia_tariff_T3", "r9_loop15_kia_ev_cut_hybrid_tariff", "4C-watch", date(2025, 7, 25), "Kia Q2 tariff hit 786B won / $570M, OP -24% to 2.76T won, shares -1.7%", -1.7, "tariff_margin_4C_watch", "4C-watch", {"tariff_hit_krw_bn": 786, "tariff_hit_usd_mn": 570, "op_krw_trn": 2.76, "op_yoy_pct": -24}),
    Round304TriggerRecord("r9l15_hyundai_robotics_T2", "r9_loop15_hyundai_boston_dynamics_robotics", "Stage2-Actionable+4B-watch", date(2026, 2, 11), "Boston Dynamics CEO change spurs commercialization expectation; Hyundai +5.9%, Kia +4.6%", 5.9, "Stage2_robotics_optionality", "Stage2-Actionable", {"hyundai_event_return_pct": 5.9, "kia_event_return_pct": 4.6}),
    Round304TriggerRecord("r9l15_hyundai_robotics_T3", "r9_loop15_hyundai_boston_dynamics_robotics", "Stage2-Actionable+4B-watch", date(2026, 3, 4), "AI data-center and robot-factory investment plan; robotics event return +11%", 11.0, "robotics_4B_overlay", "4B-watch", {"ai_robot_factory_investment_krw_trn": 9, "robotics_event_return_pct": 11, "hyundai_2026_ytd_return_to_mar3_pct": 99}),
    Round304TriggerRecord("r9l15_hyundai_georgia_T1", "r9_loop15_hyundai_georgia_localization_operational_4c", "4C-watch", date(2025, 9, 4), "ICE raid detains 475 people at Hyundai-LG Georgia battery construction site; project and diplomatic risk", "price_data_unavailable_after_deep_search", "localization_operational_4C_watch", "4C-watch", {"detained_workers_count": 475, "georgia_project_usd_bn": 7.6, "additional_expansion_usd_bn": 2.7, "target_capacity_2028_units": 500000}),
    Round304TriggerRecord("r9l15_koreanair_asiana_T1", "r9_loop15_korean_air_asiana_consolidation", "Stage2_consolidation", date(2024, 12, 12), "Korean Air completes $1.3B Asiana acquisition, 63.88% stake, integration planned by 2027", "price_data_unavailable_after_deep_search", "success_candidate_stage2", "Stage2", {"acquisition_value_usd_bn": 1.3, "stake_pct": 63.88, "cargo_sale_krw_bn": 470, "integration_target_year": 2027}),
    Round304TriggerRecord("r9l15_jejuair_crash_T0", "r9_loop15_jeju_air_crash_safety_4c", "hard_4C", date(2024, 12, 30), "Jeju Air crash kills 179; shares down as much as 15.7% to 6,920 won, 95.7B won market cap loss", -15.7, "hard_4c_success", "4C", {"fatalities": 179, "survivors": 2, "intraday_low_krw": 6920, "market_cap_loss_krw_bn": 95.7, "domestic_cancellations_count": 33000, "international_cancellations_count": 34000}),
    Round304TriggerRecord("r9l15_china_tourism_T1", "r9_loop15_china_tourism_travel_leisure", "Stage2-Actionable", date(2025, 8, 6), "China tourist group visa-free policy; Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%", "7.1/4.8/2.9/9.9", "Stage2_promote_candidate", "Stage2-Actionable", {"hyundai_dept_return_pct": 7.1, "hotel_shilla_return_pct": 4.8, "paradise_return_pct": 2.9, "hankook_cosmetics_return_pct": 9.9, "visa_free_stay_days": 15, "china_visitor_share_2024_pct": 28}),
    Round304TriggerRecord("r9l15_hmm_redsea_T1", "r9_loop15_hmm_red_sea_freight_cycle", "cyclical_Stage2", date(2024, 7, 3), "Red Sea rerouting ties 5-9% global capacity; Freightos index +40% to $5,068; rates from $1,200 to $4,500", "HMM price unavailable", "cyclical_success_event_premium", "Stage2_cyclical", {"freightos_index_usd_per_40ft": 5068, "six_week_change_pct": 40, "capacity_tied_pct_range": "5-9", "rate_multiple_from_pre_crisis": 3.75}),
    Round304TriggerRecord("r9l15_hmm_suez_T3", "r9_loop15_hmm_red_sea_freight_cycle", "4B-watch", date(2026, 2, 5), "Suez return and overcapacity may release 6-7% capacity; Maersk 2026 EBITDA guidance far below 2025", "HMM price unavailable", "shipping_cycle_4B_watch", "4B-watch", {"suez_return_capacity_release_pct_range": "6-7", "maersk_2025_ebitda_usd_bn": 9.53, "maersk_2026_ebitda_guidance_usd_bn_range": "4.5-7.0"}),
)

ROUND304_CASE_CANDIDATES: tuple[Round304CaseCandidate, ...] = (
    Round304CaseCandidate("r9_loop15_hyundai_hybrid_shareholder_return", "005380", "Hyundai Motor", E2RArchetype.HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW, (E2RArchetype.AUTO_TARIFF_HYBRID_MIX_STAGE2, E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN), "success_candidate", "Stage2_Actionable_Stage3_Yellow_candidate", "T1", "Stage2-Actionable", "Stage2-Actionable / Stage3-Yellow candidate", date(2024, 8, 28), date(2024, 8, 28), None, date(2024, 8, 28), None, False, ("hybrid_target_raise_40pct", "1_33M_hybrid_units_by_2028", "4T_KRW_buyback", "35pct_shareholder_return", "2027_OP_margin_target_9_10pct", "event_return_plus_4_7pct"), ("actual_hybrid_sales_mix_missing", "ASP_margin_by_powertrain_missing", "buyback_execution_missing", "tariff_absorption_missing", "US_localization_margin_missing"), 4.7, None, {"hybrid_models_count": 14, "quarterly_dividend_floor_krw": 2500}, "missed_due_to_score", "Stage2_promote_candidate", "unknown", "stage2_watch_success", "Hybrid target, buyback and margin target make Hyundai Stage2-Actionable, but actual mix and tariff-adjusted margin are Green gates."),
    Round304CaseCandidate("r9_loop15_kia_ev_cut_hybrid_tariff", "000270", "Kia", E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH, (E2RArchetype.AUTO_TARIFF_HYBRID_MIX_STAGE2, E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE), "4b_watch", "EV_target_cut_hybrid_pivot_tariff_4C_watch", "T3", "4C-watch", "4C-watch / Stage2 hybrid pivot", date(2025, 4, 9), date(2025, 4, 9), None, date(2025, 7, 25), date(2025, 7, 25), False, ("EV_target_cut_21_25pct", "hybrid_target_993k_units", "tariff_hit_786B_KRW", "OP_yoy_minus_24pct", "US_sales_plus_5pct"), ("tariff_absorption_missing", "OP_decline_despite_sales_growth", "EV_growth_thesis_softened", "hybrid_offset_not_yet_margin_proven"), None, -1.7, {"ev_target_prior_units_mn": 1.6, "ev_target_new_units_mn": 1.26, "hybrid_target_units": 993000, "tariff_hit_krw_bn": 786, "op_krw_trn": 2.76}, "unknown", "thesis_break_watch", "thesis_break", "should_have_been_red", "Kia's EV target cut is a soft thesis break and the tariff hit is a 4C-watch until hybrid mix offsets margin."),
    Round304CaseCandidate("r9_loop15_hyundai_boston_dynamics_robotics", "005380", "Hyundai Motor / Boston Dynamics", E2RArchetype.ROBOTICS_OPTIONALITY_STAGE2_WITH_4B, (E2RArchetype.FUTURE_MOBILITY_AI_ROBOTICS_CAPEX, E2RArchetype.THEME_VALUATION_OVERHEAT), "success_candidate", "Stage2_Actionable_with_4B_overlay", "T2/T3", "Stage2-Actionable+4B-watch", "Stage2-Actionable + 4B-watch", date(2026, 2, 11), date(2026, 2, 11), None, date(2026, 3, 4), None, False, ("Boston_Dynamics_commercialization_trigger", "Atlas_demo", "2028_factory_deployment_plan", "9T_KRW_AI_robot_factory_investment", "robotics_event_return_plus_11pct"), ("robot_unit_economics_missing", "factory_deployment_success_missing", "external_customer_orders_missing", "recurring_robot_revenue_missing", "valuation_vs_auto_core_missing"), 11.0, None, {"boston_dynamics_indirect_stake_pct": 27.9, "hyundai_2026_ytd_return_to_mar3_pct": 99}, "missed_due_to_score", "Stage2_promote_candidate_with_4B", "event_premium", "stage2_watch_success", "Robotics optionality is Stage2, while a large price move before orders and unit economics is 4B-watch."),
    Round304CaseCandidate("r9_loop15_hyundai_georgia_localization_operational_4c", "005380/373220_readthrough", "Hyundai Motor / LG Energy Solution Georgia JV", E2RArchetype.AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C, (E2RArchetype.AUTO_US_LOCALIZATION_LABOR_VISA_RISK, E2RArchetype.AUTO_TARIFF_LOCALIZATION), "4b_watch", "localization_capex_operational_4C_watch", "T1", "4C-watch", "4C-watch", date(2025, 9, 4), None, None, date(2025, 9, 4), date(2025, 9, 4), False, ("Georgia_project_7_6B_USD", "battery_JV_localization", "detained_workers_475", "capacity_target_500k_by_2028"), ("workforce_visa_compliance_break", "worker_deaths_and_safety_risk", "plant_delay_risk", "diplomatic_risk", "localization_margin_unproven"), None, None, {"detained_workers_count": 475, "worker_deaths_since_2022": 3, "serious_injuries_more_than_dozen": True}, "unknown", "localization_capex_operational_4C_watch", "thesis_break", "should_have_been_red", "US localization capex is not positive evidence until workforce, visa, safety and stable production gates close."),
    Round304CaseCandidate("r9_loop15_korean_air_asiana_consolidation", "003490/020560", "Korean Air / Asiana Airlines", E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2, (E2RArchetype.AIRLINE_CONSOLIDATION_INTEGRATION, E2RArchetype.AIRLINE_REMEDY_ROUTE_CARGO_STAGE2), "success_candidate", "success_candidate_stage2", "T1", "Stage2_consolidation", "Stage2", date(2024, 12, 12), date(2024, 12, 12), None, date(2024, 12, 12), None, False, ("acquisition_completed", "stake_63_88pct", "integration_target_2027", "cargo_sale_470B_KRW"), ("cost_synergy_missing", "route_yield_improvement_missing", "load_factor_missing", "LCC_integration_missing", "frequent_flyer_integration_missing", "debt_reduction_missing"), None, None, {"acquisition_value_usd_bn": 1.3, "stake_pct": 63.88, "cargo_sale_krw_bn": 470}, "aligned", "success_candidate_stage2", "unknown", "stage2_watch_success", "Merger closing is Stage2; Green needs route yield, load factor, cost synergy and safety trust."),
    Round304CaseCandidate("r9_loop15_jeju_air_crash_safety_4c", "089590", "Jeju Air", E2RArchetype.AIRLINE_SAFETY_HARD_4C, (E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C, E2RArchetype.AVIATION_SAFETY_HARD_4C), "4c_thesis_break", "hard_4c_reference", "T0", "hard_4C", "4C", date(2024, 12, 30), None, None, None, date(2024, 12, 30), True, ("fatal_accident", "179_fatalities", "share_intraday_minus_15_7pct", "market_cap_loss_95_7B_KRW", "domestic_and_international_cancellations"), ("fatal_airline_safety_accident", "booking_cancellations", "consumer_trust_collapse", "regulatory_investigation"), None, -15.7, {"fatalities": 179, "survivors": 2, "intraday_low_krw": 6920, "market_cap_loss_krw_bn": 95.7}, "false_positive_score", "hard_4c_success", "thesis_break", "should_have_been_red", "Jeju Air crash is hard 4C; travel demand evidence cannot override a fatal safety trust break."),
    Round304CaseCandidate("r9_loop15_china_tourism_travel_leisure", "008770/069960/034230/123690/travel_airline_basket", "China tourism/leisure basket", E2RArchetype.TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE, (E2RArchetype.CASINO_DUTYFREE_TOURISM_POLICY_KOREA, E2RArchetype.TOURISM_POLICY_EVENT), "success_candidate", "Stage2_Actionable_policy_event", "T1", "Stage2-Actionable", "Stage2-Actionable", date(2025, 8, 6), date(2025, 8, 6), None, date(2025, 8, 6), None, False, ("China_group_visa_free_policy", "multi_stock_basket_rally", "15_day_visa_free_stay", "China_visitor_share_28pct", "flight_capacity_105pct_pre_pandemic"), ("actual_arrivals_missing", "airline_yield_missing", "hotel_ADR_missing", "duty_free_sales_missing", "casino_drop_missing", "foreign_card_spending_missing"), 9.9, None, {"hyundai_dept_return_pct": 7.1, "hotel_shilla_return_pct": 4.8, "paradise_return_pct": 2.9, "hankook_cosmetics_return_pct": 9.9}, "missed_due_to_score", "Stage2_promote_candidate", "event_premium", "stage2_watch_success", "Visa waiver and basket rally are Stage2; actual arrivals, spending and yield are Green gates."),
    Round304CaseCandidate("r9_loop15_hmm_red_sea_freight_cycle", "011200", "HMM", E2RArchetype.CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B, (E2RArchetype.SHIPPING_FREIGHT_CYCLE_KOREA, E2RArchetype.SHIPPING_FREIGHT_NORMALIZATION_4C), "cyclical_success", "cyclical_success_event_premium", "T1/T3", "cyclical_Stage2+4B-watch", "Stage2 cyclical + 4B-watch", date(2024, 7, 3), date(2024, 7, 3), None, date(2026, 2, 5), None, False, ("Freightos_index_5068_USD_per_40ft", "six_week_change_plus_40pct", "global_capacity_tied_5_9pct", "rate_multiple_3_75x"), ("HMM_spot_contract_mix_missing", "quarterly_OP_missing", "cash_return_missing", "capacity_discipline_missing", "Suez_normalization_risk", "overcapacity_risk"), None, None, {"freightos_index_usd_per_40ft": 5068, "rate_multiple_from_pre_crisis": 3.75, "suez_return_capacity_release_pct_range": "6-7"}, "aligned", "cyclical_success_event_premium", "cyclical_rerating", "stage2_watch_success", "Red Sea freight spike is cyclical Stage2; Suez normalization and overcapacity make 4B-watch necessary."),
)


def round304_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(case.to_case_record() for case in ROUND304_CASE_CANDIDATES)


def round304_summary() -> dict[str, object]:
    return {
        "source_round": ROUND304_SOURCE_ROUND_PATH,
        "round_id": ROUND304_ANALYST_ROUND_ID,
        "large_sector": ROUND304_LARGE_SECTOR,
        "method": ROUND304_METHOD,
        "case_candidate_count": len(ROUND304_CASE_CANDIDATES),
        "trigger_count": len(ROUND304_TRIGGER_RECORDS),
        "stage2_actionable_candidate_count": 5,
        "stage3_yellow_candidate_count": 1,
        "stage3_green_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 4,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 1,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "full_adjusted_ohlc_complete": False,
        "shadow_weight_only": True,
    }


def round304_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(case.as_row() for case in ROUND304_CASE_CANDIDATES)


def round304_trigger_rows() -> tuple[dict[str, str], ...]:
    return tuple(trigger.as_row() for trigger in ROUND304_TRIGGER_RECORDS)


def round304_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"requested_alias": key, "canonical_archetype": value} for key, value in ROUND304_REQUIRED_TARGET_ALIASES.items())


def round304_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND304_SHADOW_WEIGHT_ROWS)


def round304_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    up_points = {
        "hybrid_mix_margin_visibility": "+5",
        "actual_vehicle_sales_mix": "+5",
        "shareholder_return_execution": "+4",
        "tariff_absorption_capacity": "+5",
        "robotics_deployment_order_visibility": "+5",
        "localization_workforce_compliance": "+5",
        "airline_integration_synergy": "+5",
        "aviation_safety_trust": "+5",
        "tourism_spending_conversion": "+5",
        "freight_rate_duration_contract_mix": "+5",
    }
    down_points = {
        "ev_growth_headline_only": "-5",
        "localization_capex_headline_only": "-5",
        "robotics_optional_value_without_orders": "-5",
        "merger_closing_without_synergy": "-4",
        "fatal_safety_event": "-5",
        "visa_policy_without_spending": "-4",
        "freight_rate_spike_without_contract_mix": "-5",
    }
    rows = []
    for axis in ROUND304_SCORE_UP_AXES:
        rows.append({"axis": axis, "points": up_points[axis], "direction": "raise", "reason": "R9 mobility/transport/leisure trigger quality axis"})
    for axis in ROUND304_SCORE_DOWN_AXES:
        rows.append({"axis": axis, "points": down_points[axis], "direction": "lower", "reason": "R9 headline, safety, policy or cyclical false-positive blocker"})
    return tuple(rows)


def round304_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND304_SOURCE_ROUND_PATH,
        "round_id": ROUND304_ANALYST_ROUND_ID,
        "large_sector": ROUND304_LARGE_SECTOR,
        "method": ROUND304_METHOD,
        "summary": round304_summary(),
        "target_archetypes": dict(ROUND304_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND304_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND304_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND304_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND304_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND304_SCORE_UP_AXES),
        "score_down_axes": list(ROUND304_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND304_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND304_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_apply_round304_shadow_weights_to_production_scoring_yet",
            "do_not_use_round304_cases_as_candidate_generation_input",
            "do_not_treat_mobility_transport_leisure_headline_as_green",
            "do_not_downgrade_stage_candidate_only_because_full_ohlc_is_missing",
        ],
    }


def render_round304_summary_markdown() -> str:
    summary = round304_summary()
    lines = [
        "# Round 304 R9 Loop 15 Mobility/Transport/Leisure Trigger Validation",
        "",
        "이번 라운드는 자동차, 로봇, 항공, 여행, 해운 headline을 실제 EPS/FCF 지속 증거와 분리한다.",
        "",
        "쉬운 예: `비자 면제`는 손님이 올 수 있다는 신호다. Green은 실제 입국자, 객단가, 호텔 ADR, 면세점 매출, 항공 yield가 확인될 때다.",
        "",
        "## Summary",
        "",
    ]
    for key in (
        "round_id",
        "large_sector",
        "case_candidate_count",
        "trigger_count",
        "stage2_actionable_candidate_count",
        "stage3_yellow_candidate_count",
        "stage3_green_confirmed_count",
        "stage4b_watch_count",
        "stage4c_watch_count",
        "hard_4c_case_count",
        "production_scoring_changed",
        "candidate_generation_input",
        "full_adjusted_ohlc_complete",
        "shadow_weight_only",
    ):
        lines.append(f"- {key}: {summary[key]}")
    lines.extend(
        [
            "",
            "## Core Findings",
            "",
            "- Hyundai hybrid/shareholder-return trigger is Stage2-Actionable and Stage3-Yellow candidate, but actual hybrid mix, ASP/margin, tariff absorption and buyback execution are Green gates.",
            "- Kia tariff hit and EV target cut are 4C-watch until hybrid mix offsets tariff-adjusted margin.",
            "- Hyundai/Boston Dynamics robotics is Stage2-Actionable with 4B overlay; orders and unit economics are required before Green.",
            "- Hyundai Georgia localization is operational 4C-watch; capex does not count until workforce, visa, safety and compliance are closed.",
            "- Korean Air/Asiana is Stage2 consolidation; route yield, load factor, LCC integration and debt/synergy must follow.",
            "- Jeju Air crash is hard 4C and blocks travel-demand Green logic.",
            "- China tourism visa-waiver basket is Stage2-Actionable; actual spending/yield evidence is required.",
            "- HMM/Red Sea freight is cyclical Stage2 + 4B-watch, not structural Green without contract mix and duration.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round304_trigger_grid_markdown() -> str:
    lines = [
        "# Round 304 Trigger Grid",
        "",
        "| trigger_id | case_id | date | type | outcome | promote_to | evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for trigger in ROUND304_TRIGGER_RECORDS:
        lines.append(
            f"| {trigger.trigger_id} | {trigger.case_id} | {trigger.trigger_date.isoformat()} | {trigger.trigger_type} | {trigger.trigger_outcome_label} | {trigger.promote_to} | {trigger.evidence_available} |"
        )
    return "\n".join(lines) + "\n"


def render_round304_stage_rules_markdown() -> str:
    lines = ["# Round 304 Stage Rules", "", "Do not apply these weights to production scoring yet.", "", "## Stage2-Actionable", ""]
    lines.extend(f"- {rule}" for rule in ROUND304_STAGE2_ACTIONABLE_RULES)
    lines.extend(["", "## Stage3-Yellow", ""])
    lines.extend(f"- {rule}" for rule in ROUND304_STAGE3_YELLOW_RULES)
    lines.extend(["", "## Stage3-Green", ""])
    lines.extend(f"- {rule}" for rule in ROUND304_STAGE3_GREEN_RULES)
    lines.extend(["", "## Green Blockers", ""])
    lines.extend(f"- {rule}" for rule in ROUND304_GREEN_BLOCKERS)
    return "\n".join(lines) + "\n"


def render_round304_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 304 4B/4C Review",
        "",
        "이번 라운드에서 Stage3-Green 확정은 없다. Robotics optionality, tourism policy, freight-rate spike는 4B-watch가 필요하고, fatal airline accident는 hard 4C다.",
        "",
        "## 4B Watch",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND304_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {item}" for item in ROUND304_HARD_4C_GATES)
    lines.extend(["", "## Confirmed Hard 4C", "", "- Jeju Air fatal safety accident"])
    return "\n".join(lines) + "\n"


def render_round304_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round 304 Price Validation Plan",
            "",
            "- reported_event_anchor_not_full_ohlc 상태를 유지한다.",
            "- full adjusted OHLC가 없다는 이유로 Stage2-Actionable, Stage3-Yellow candidate, 4B-watch 또는 4C 후보를 강등하지 않는다.",
            "- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.",
            "- 다음 단계에서는 trigger date 기준 30/90/180일 MFE/MAE, below-entry, hybrid mix, tariff-adjusted margin, robot orders, airline yield, tourism spend, freight contract mix를 채운다.",
            "",
        ]
    )


def write_round304_r9_loop15_reports(
    *,
    output_directory: str | Path = ROUND304_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND304_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND304_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND304_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND304_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round304_case_records(), cases_path),
        "triggers": write_round304_triggers(triggers_path),
        "audit": _write_json(round304_audit_payload(), audit_path),
        "weight_profile": _write_csv(round304_shadow_weight_rows(), weight_profile_path),
        "summary": output / "round304_r9_loop15_trigger_validation_summary.md",
        "case_matrix": output / "round304_r9_loop15_case_matrix.csv",
        "trigger_grid": output / "round304_r9_loop15_trigger_grid.csv",
        "target_aliases": output / "round304_r9_loop15_target_aliases.csv",
        "score_adjustments": output / "round304_r9_loop15_score_adjustments.csv",
        "shadow_weights": output / "round304_r9_loop15_shadow_weights.csv",
        "stage_rules": output / "round304_r9_loop15_stage_rules.md",
        "trigger_grid_md": output / "round304_r9_loop15_trigger_grid.md",
        "price_validation_plan": output / "round304_r9_loop15_price_validation_plan.md",
        "stage4b_4c_review": output / "round304_r9_loop15_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round304_summary_markdown(), encoding="utf-8")
    _write_csv(round304_case_rows(), paths["case_matrix"])
    _write_csv(round304_trigger_rows(), paths["trigger_grid"])
    _write_csv(round304_target_alias_rows(), paths["target_aliases"])
    _write_csv(round304_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round304_shadow_weight_rows(), paths["shadow_weights"])
    paths["stage_rules"].write_text(render_round304_stage_rules_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round304_trigger_grid_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round304_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round304_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def write_round304_triggers(path: str | Path = ROUND304_DEFAULT_TRIGGERS_PATH) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(trigger.as_dict(), ensure_ascii=False, sort_keys=True) for trigger in ROUND304_TRIGGER_RECORDS]
    target.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return target


def _write_json(payload: Mapping[str, object], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def _write_csv(rows: Iterable[Mapping[str, object]], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    rows_tuple = tuple(rows)
    with target.open("w", encoding="utf-8", newline="") as handle:
        if not rows_tuple:
            handle.write("")
            return target
        writer = csv.DictWriter(handle, fieldnames=list(rows_tuple[0].keys()))
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow({key: _value_text(value) for key, value in row.items()})
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def _signed(value: int) -> str:
    if value > 0:
        return f"+{value}"
    return str(value)
