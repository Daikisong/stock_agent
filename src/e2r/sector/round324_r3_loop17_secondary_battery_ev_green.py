"""Round-324 R3 Loop-17 battery, EV, and green-energy validation pack.

This module converts ``docs/round/round_324.md`` into calibration-only case
records, trigger rows, shadow weights, and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: Samsung SDI's ESS LFP contract can be Stage2-Actionable because
contract value, line conversion and event return are clear. It is not Green
until customer, delivery, utilization, margin and full OHLC validation exist.
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


ROUND324_SOURCE_ROUND_PATH = "docs/round/round_324.md"
ROUND324_ANALYST_ROUND_ID = "round_252"
ROUND324_LOOP_NAME = "R3 Loop 17"
ROUND324_LARGE_SECTOR = "SECONDARY_BATTERY_EV_GREEN"
ROUND324_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND324_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round324_r3_loop17_secondary_battery_ev_green"
ROUND324_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop17_round252.jsonl"
ROUND324_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r3_loop17_round252.jsonl"
ROUND324_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round324_r3_loop17_secondary_battery_ev_green_audit.json"
ROUND324_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round252_r3_loop17_v1.csv"

ROUND324_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE": E2RArchetype.ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE.value,
    "EV_CONTRACT_CANCELLATION_4C": E2RArchetype.EV_CONTRACT_CANCELLATION_4C.value,
    "SK_ON_ESS_PIVOT_STAGE2_WITH_PARENT_READTHROUGH": E2RArchetype.SK_ON_ESS_PIVOT_STAGE2_WITH_PARENT_READTHROUGH.value,
    "LITHIUM_PRICE_REBOUND_CYCLICAL_STAGE2": E2RArchetype.LITHIUM_PRICE_REBOUND_CYCLICAL_STAGE2.value,
    "SOLID_STATE_TIMELINE_STAGE2_YELLOW_CANDIDATE": E2RArchetype.SOLID_STATE_TIMELINE_STAGE2_YELLOW_CANDIDATE.value,
    "IRA_AMPC_EARNINGS_WITH_POLICY_4B": E2RArchetype.IRA_AMPC_EARNINGS_WITH_POLICY_4B.value,
    "CAPITAL_RAISE_DILUTION_4B": E2RArchetype.CAPITAL_RAISE_DILUTION_4B.value,
    "UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE": E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE.value,
}

ROUND324_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_at_least_5pct",
    "market_relative_return_at_least_5pp",
    "contract_value_supply_volume_policy_credit_or_production_timeline_is_clear",
    "EV_line_utilization_recovery_or_ESS_line_conversion_link_exists",
    "customer_delivery_margin_gate_is_identified",
    "contract_cancellation_subsidy_rollback_dilution_lithium_reversal_4B_absent",
    "commodity_material_case_has_possible_ASP_or_margin_bridge",
)

ROUND324_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "binding_customer_and_delivery_schedule_visible",
    "ESS_or_EV_line_utilization_recovery_visible",
    "gross_margin_or_non_credit_operating_margin_improves",
    "solid_state_pilot_yield_or_customer_adoption_visible",
    "capex_dilution_or_policy_credit_overhang_partly_resolved",
)

ROUND324_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "ESS_or_EV_contract_is_final_and_delivery_starts",
    "factory_utilization_and_margin_recover",
    "non_credit_operating_margin_is_positive_and_durable",
    "lithium_or_cathode_rebound_converts_to_ASP_and_margin",
    "solid_state_moves_from_timeline_to_customer_revenue",
    "capex_dilution_and_contract_cancellation_risks_are_resolved",
    "full_window_MFE_MAE_is_available_and_supportive",
)

ROUND324_GREEN_BLOCKERS: tuple[str, ...] = (
    "ESS_headline_without_customer_margin_delivery",
    "EV_contract_backlog_without_cancellation_check",
    "AMPC_credit_dependency_ignored",
    "solid_state_timeline_without_revenue",
    "lithium_rebound_without_durability",
    "capital_raise_dilution_ignored",
    "unlisted_subsidiary_readthrough_overstated",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND324_SCORE_UP_AXES: tuple[str, ...] = (
    "ESS_LFP_contract_visibility",
    "line_conversion_utilization",
    "contract_cancellation_risk",
    "lithium_price_inventory_rebound",
    "solid_state_commercialization_timeline",
    "non_credit_operating_margin",
    "upstream_lithium_supply_control",
    "market_relative_return",
)

ROUND324_SCORE_DOWN_AXES: tuple[str, ...] = (
    "EV_contract_backlog_without_cancellation_check",
    "AMPC_credit_dependency_ignored",
    "ESS_headline_without_customer_margin",
    "solid_state_timeline_without_revenue",
    "lithium_rebound_without_durability",
    "capital_raise_dilution_ignored",
    "unlisted_subsidiary_readthrough_overstated",
)

ROUND324_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "ESS_contract_before_customer_margin_delivery",
    "AMPC_driven_profit_with_weak_underlying_margin",
    "capital_raise_or_offering_price_cut",
    "lithium_price_rebound_from_temporary_mine_license_event",
    "unlisted_subsidiary_event_over_read_into_parent",
    "solid_state_timeline_without_revenue",
)

ROUND324_HARD_4C_GATES: tuple[str, ...] = (
    "large_OEM_contract_cancellation",
    "repeated_contract_cancellation_across_customers",
    "factory_utilization_thesis_break",
    "EV_subsidy_rollback_causing_permanent_demand_reset",
    "capex_or_dilution_spiral",
    "safety_recall_or_fire_defect_with_compensation",
)

ROUND324_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_reported_event_return_market_relative_return_contract_value_and_policy_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
    "do_not_treat_ESS_contract_AMPC_profit_lithium_rebound_solid_state_timeline_or_dilution_as_Green_without_customer_margin_utilization_revenue_and_risk_resolution",
)


@dataclass(frozen=True)
class Round324TriggerRecord:
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
class Round324CaseCandidate:
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
    strong_4c_confirmed: bool
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
            "do_not_use_round324_cases_as_candidate_generation_input",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_ESS_contract_AMPC_profit_lithium_rebound_solid_state_timeline_or_dilution_as_Green_without_customer_margin_utilization_revenue_and_risk_resolution",
        ]
        if not self.strong_4c_confirmed:
            guardrails.append("strong_4c_confirmed_false")
        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "AMPC" in field
            or "dilution" in field
            or "lithium" in field
            or "timeline" in field
            or "parent_readthrough" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "cancellation" in field
            or "thesis_break" in field
            or "contract_quality_break" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND324_LARGE_SECTOR,
            large_sector=ROUND324_LARGE_SECTOR,
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
            stage3_evidence=self.evidence_fields if self.stage3_date else (),
            stage4b_evidence=stage4b_evidence,
            stage4c_evidence=stage4c_evidence,
            must_have_fields=ROUND324_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.case_type in {"event_premium", "4b_watch", "4c_thesis_break", "failed_rerating", "overheat"} else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern="reported_event_anchor_only",
            score_weight_hint={},
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(
                mfe_30d=self.event_mfe_pct,
                mae_30d=self.event_mae_pct,
                price_validation_status="price_data_unavailable_after_deep_search",
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8,
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
            "strong_4c_confirmed": str(self.strong_4c_confirmed).lower(),
            "evidence_fields": "|".join(self.evidence_fields),
            "red_flag_fields": "|".join(self.red_flag_fields),
            "event_mfe_pct": _value_text(self.event_mfe_pct),
            "event_mae_pct": _value_text(self.event_mae_pct),
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND324_CASE_CANDIDATES: tuple[Round324CaseCandidate, ...] = (
    Round324CaseCandidate(
        "r3_loop17_samsung_sdi_ess_lfp",
        "006400",
        "Samsung SDI",
        E2RArchetype.ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE,
        (E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, E2RArchetype.ESS_LFP_CONTRACT_STAGE2_NOT_GREEN),
        "success_candidate",
        "Stage2_Actionable_ESS_LFP_line_conversion",
        "T1/T3",
        "Stage2-Actionable_ESS_LFP_contract",
        "Stage2-Actionable",
        date(2025, 12, 9),
        date(2025, 12, 9),
        None,
        date(2025, 12, 9),
        None,
        False,
        ("Samsung_SDI_America_LFP_ESS_contract", "contract_value_gt_2T_won", "contract_value_1_36B_usd", "event_return_6_1pct", "KOSPI_minus_0_1pct", "existing_US_EV_lines_to_ESS_LFP"),
        ("customer_name_missing", "firm_delivery_schedule_missing", "LFP_margin_missing", "line_conversion_cost_missing", "ESS_repeat_orders_missing", "full_OHLC_MFE_MAE_missing"),
        6.1,
        None,
        {"trigger_date": "2025-12-09", "contract_value_krw_trn": ">2.0", "contract_value_usd_bn": 1.36, "delivery_period": "3_years_from_2027", "event_return_pct": 6.1, "kospi_same_context_pct": -0.1, "market_relative_return_pp": 6.2, "line_conversion": "existing_US_EV_lines_to_ESS_LFP"},
        "aligned",
        "excellent_stage2_actionable_ESS_pivot",
        "event_premium",
        "stage2_watch_success",
        "Samsung SDI ESS LFP is the cleanest R3 Stage2-Actionable anchor, but customer, delivery, margin and line-conversion execution remain Green gates.",
    ),
    Round324CaseCandidate(
        "r3_loop17_lges_ford_freudenberg_cancellation",
        "373220",
        "LG Energy Solution",
        E2RArchetype.EV_CONTRACT_CANCELLATION_4C,
        (E2RArchetype.EV_BATTERY_CONTRACT_CANCELLATION_HARD_4C, E2RArchetype.EV_BATTERY_CONTRACT_QUALITY_BREAK),
        "4c_thesis_break",
        "4C_EV_contract_cancellation",
        "T0/T3",
        "4C_EV_contract_cancellation",
        "4C",
        date(2025, 12, 17),
        None,
        None,
        None,
        date(2025, 12, 17),
        True,
        ("Ford_contract_cancellation_9_6T_won", "Freudenberg_contract_cancellation_3_9T_won", "expected_revenue_loss_13_5T_won", "LGES_minus_7_6pct", "European_plant_utilization_delay"),
        ("large_OEM_contract_cancellation_4C", "repeated_contract_cancellation_across_customers", "replacement_orders_missing", "European_plant_utilization_missing", "ESS_line_conversion_missing", "margin_recovery_missing"),
        None,
        -7.6,
        {"ford_cancellation_date": "2025-12-17", "ford_contract_value_krw_trn": 9.6, "ford_contract_value_usd_bn": 6.5, "ford_event_return_pct": -7.6, "kospi_same_context_pct": -1.4, "market_relative_return_pp": -6.2, "freudenberg_cancellation_date": "2025-12-26", "freudenberg_contract_value_krw_trn": 3.9, "freudenberg_contract_value_usd_bn": 2.7, "expected_revenue_loss_krw_trn": 13.5},
        "aligned",
        "hard_4C_contract_quality_break",
        "thesis_break",
        "should_have_been_red",
        "Repeated Ford/Freudenberg cancellations are a hard 4C contract-quality and utilization break.",
    ),
    Round324CaseCandidate(
        "r3_loop17_sk_on_ess_flatiron_ford_jv",
        "096770_readthrough",
        "SK On / SK Innovation readthrough",
        E2RArchetype.SK_ON_ESS_PIVOT_STAGE2_WITH_PARENT_READTHROUGH,
        (E2RArchetype.SK_ON_RESTRUCTURING_ESS_PIVOT_STAGE2, E2RArchetype.BATTERY_JV_RESTRUCTURING_RELIEF_STAGE2_WITH_FINANCIAL_4B),
        "success_candidate",
        "Stage2_ESS_pivot_with_4B_restructuring",
        "T0/T3",
        "Stage2_ESS_pivot_with_4B_restructuring",
        "Stage2 + 4B-watch",
        date(2025, 9, 3),
        date(2025, 9, 3),
        None,
        date(2025, 12, 11),
        None,
        False,
        ("Flatiron_Energy_7_2GWh_LFP_ESS", "supply_period_2026_2030", "Georgia_EV_lines_to_ESS", "Ford_JV_split", "SK_On_Q3_2025_OP_loss_124_8B_won"),
        ("direct_price_unavailable_unlisted_subsidiary", "SK_On_margin_recovery_missing", "parent_SK_Innovation_valuation_impact_missing", "Tennessee_plant_utilization_missing", "fixed_cost_reduction_missing"),
        None,
        None,
        {"flatiron_deal_date": "2025-09-03", "ess_volume_gwh": 7.2, "supply_period": "2026-2030", "technology": "LFP_ESS", "georgia_line_conversion": True, "ford_jv_split_date": "2025-12-11", "original_ford_sk_investment_usd_bn": 11.4, "sk_on_q3_2025_operating_loss_krw_bn": 124.8, "direct_price_anchor": "price_data_unavailable_unlisted_subsidiary"},
        "aligned",
        "Stage2_ESS_pivot_with_parent_readthrough_unavailable",
        "event_premium",
        "stage2_watch_success",
        "SK On ESS pivot is Stage2 evidence, but parent readthrough, losses and JV restructuring keep a 4B overlay.",
    ),
    Round324CaseCandidate(
        "r3_loop17_lithium_rebound_posco_future_m_lnf",
        "003670/066970/006400/373220",
        "POSCO Future M / L&F / Samsung SDI / LGES",
        E2RArchetype.LITHIUM_PRICE_REBOUND_CYCLICAL_STAGE2,
        (E2RArchetype.LITHIUM_SUPPLY_SHOCK_CYCLICAL_STAGE2, E2RArchetype.BATTERY_MATERIAL_LITHIUM_BETA_EVENT_PREMIUM),
        "cyclical_success",
        "cyclical_Stage2_lithium_rebound",
        "T0/T2",
        "cyclical_Stage2_lithium_rebound",
        "cyclical Stage2",
        date(2025, 8, 11),
        date(2025, 8, 11),
        None,
        date(2025, 8, 11),
        None,
        False,
        ("CATL_Yichun_lithium_mine_suspension", "POSCO_Future_M_plus_8_3pct", "L_and_F_plus_10pct", "Samsung_SDI_plus_3_2pct", "LGES_plus_2_8pct", "lithium_price_drawdown_up_to_90pct_from_2022_peak"),
        ("lithium_price_sustained_rebound_missing", "CATL_license_nonrenewal_missing", "cathode_ASP_recovery_missing", "inventory_valuation_gain_missing", "customer_volume_missing", "margin_recovery_missing"),
        10.0,
        None,
        {"trigger_date": "2025-08-11", "catalyst": "CATL_Yichun_lithium_mine_license_expiry_and_suspension", "posco_future_m_event_return_pct": 8.3, "lnf_event_return_pct": 10, "samsung_sdi_event_return_pct": 3.2, "lges_event_return_pct": 2.8, "kospi_same_context_pct": -0.1, "lithium_price_drawdown_from_2022_peak_pct": "up_to_90"},
        "aligned",
        "cyclical_lithium_stage2_not_green",
        "cyclical_rerating",
        "stage2_watch_success",
        "Lithium rebound produced a strong basket move, but CATL license and oversupply risk keep it cyclical Stage2, not Green.",
    ),
    Round324CaseCandidate(
        "r3_loop17_samsung_sdi_solid_state_timeline",
        "006400",
        "Samsung SDI",
        E2RArchetype.SOLID_STATE_TIMELINE_STAGE2_YELLOW_CANDIDATE,
        (E2RArchetype.SOLID_STATE_BATTERY_TIMELINE, E2RArchetype.SPECULATIVE_BATTERY_TECH),
        "success_candidate",
        "Stage3_Yellow_candidate_solid_state_timeline",
        "T0/T3",
        "Stage3-Yellow_candidate_solid_state_timeline",
        "Stage3-Yellow candidate",
        date(2024, 3, 7),
        date(2024, 3, 7),
        date(2024, 3, 7),
        date(2024, 3, 7),
        None,
        False,
        ("all_solid_state_mass_production_2027", "event_return_11pct", "event_price_405500_won", "large_cylindrical_2025", "LFP_2026"),
        ("pilot_yield_missing", "customer_adoption_missing", "solid_state_ASP_missing", "luxury_EV_order_volume_missing", "mass_production_cost_missing", "actual_revenue_missing"),
        11.0,
        None,
        {"trigger_date": "2024-03-07", "event_return_pct": 11, "event_price_krw": 405500, "kospi_same_context_pct": 0.3, "solid_state_mass_production_target": 2027, "large_cylindrical_mass_production_target": 2025, "lfp_mass_production_target": 2026},
        "aligned",
        "solid_state_stage2_yellow_candidate_not_green",
        "event_premium",
        "yellow_success",
        "Solid-state timeline is a Yellow candidate after a strong event reaction, but Green requires pilot yield, customer adoption and revenue.",
    ),
    Round324CaseCandidate(
        "r3_loop17_lges_ira_ampc_earnings",
        "373220",
        "LG Energy Solution",
        E2RArchetype.IRA_AMPC_EARNINGS_WITH_POLICY_4B,
        (E2RArchetype.IRA_SUBSIDY_DEPENDENCE_QUALITY_GATE, E2RArchetype.BATTERY_TAX_CREDIT_QUALITY_OVERLAY),
        "4b_watch",
        "Stage2_earnings_with_policy_credit_4B",
        "T0/T2",
        "Stage2_earnings_with_policy_credit_4B",
        "Stage2 + 4B-watch",
        date(2025, 7, 7),
        date(2025, 7, 7),
        None,
        date(2025, 7, 7),
        None,
        False,
        ("Q2_OP_492B_won", "operating_profit_yoy_plus_152pct", "sales_yoy_minus_9_7pct", "OP_ex_AMPC_1_4B_won", "operating_margin_ex_AMPC_0_03pct", "event_return_2_4pct"),
        ("AMPC_credit_dependency_4B", "non_credit_operating_margin_missing", "EV_line_utilization_missing", "ESS_revenue_mix_missing", "AMPC_durability_missing", "tariff_policy_stability_missing"),
        2.4,
        None,
        {"trigger_date": "2025-07-07", "operating_profit_q2_2025_krw_bn": 492, "operating_profit_yoy_pct": 152, "sales_yoy_pct": -9.7, "operating_profit_ex_ampc_krw_bn": 1.4, "operating_margin_ex_ampc_pct": 0.03, "event_return_pct": 2.4},
        "false_positive_score",
        "earnings_good_but_policy_credit_4B",
        "no_rerating",
        "false_yellow",
        "LGES headline profit improved, but ex-AMPC margin near zero means this is policy-credit 4B, not Green.",
    ),
    Round324CaseCandidate(
        "r3_loop17_samsung_sdi_capital_raise_dilution",
        "006400",
        "Samsung SDI",
        E2RArchetype.CAPITAL_RAISE_DILUTION_4B,
        (E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY, E2RArchetype.STRATEGIC_CAPITAL_WITH_DILUTION_4B),
        "4b_watch",
        "4B_capital_raise_dilution",
        "T0/T2",
        "4B_capital_raise_dilution",
        "4B-watch",
        date(2025, 4, 9),
        None,
        None,
        date(2025, 4, 9),
        None,
        False,
        ("capital_raise_2T_won", "new_shares_11821000", "offering_price_cut_14pct", "169200_to_146200_won", "YTD_minus_29_5pct", "GM_JV_and_Hungary_capex"),
        ("capital_raise_dilution_4B", "capex_ROI_missing", "factory_utilization_missing", "GM_JV_volume_missing", "Hungary_margin_missing", "EV_demand_recovery_missing"),
        None,
        -1.0,
        {"trigger_date": "2025-04-09", "capital_raise_krw_trn": 2.0, "capital_raise_usd_bn": 1.4, "new_shares_count": 11821000, "offering_price_old_krw": 169200, "offering_price_new_krw": 146200, "offering_price_cut_pct": 14, "event_return_pct": -1, "kospi_same_context_pct": -0.5, "ytd_return_context_pct": -29.5, "use_of_proceeds": ["US_GM_joint_venture", "Hungary_factory_expansion", "battery_capacity_capex"]},
        "aligned",
        "capital_raise_4B",
        "unknown",
        "stage2_watch_success",
        "Samsung SDI capital raise is growth capex funding, but discounted issuance and weak EV demand make it a dilution 4B overlay.",
    ),
    Round324CaseCandidate(
        "r3_loop17_posco_minres_lithium_jv",
        "005490_battery_material_readthrough",
        "POSCO / MinRes lithium JV",
        E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE,
        (E2RArchetype.LITHIUM_MINE_JV_STRATEGIC_RESOURCE_STAGE2, E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2),
        "success_candidate",
        "Stage2_upstream_lithium_supply_no_direct_price",
        "T0/T2",
        "Stage2_upstream_lithium_supply_no_direct_price",
        "Stage2",
        date(2025, 11, 11),
        date(2025, 11, 11),
        None,
        date(2025, 11, 11),
        None,
        False,
        ("POSCO_MinRes_lithium_JV", "deal_value_765M_usd", "30pct_stake_in_lithium_business", "15pct_Wodgina", "15pct_Mt_Marion", "MinRes_plus_10_8pct"),
        ("direct_POSCO_price_anchor_missing", "offtake_terms_missing", "lithium_price_recovery_missing", "hydroxide_conversion_margin_missing", "POSCO_materials_revenue_link_missing", "capital_intensity_missing"),
        10.8,
        None,
        {"trigger_date": "2025-11-11", "deal_value_usd_mn": 765, "stake_in_minres_lithium_business_pct": 30, "effective_stakes": ["15pct_Wodgina", "15pct_Mt_Marion"], "minres_event_return_pct": 10.8, "direct_posco_price_anchor": "price_data_unavailable_after_deep_search"},
        "aligned",
        "Stage2_upstream_lithium_supply_not_Green",
        "event_premium",
        "stage2_watch_success",
        "POSCO/MinRes is strategic upstream lithium Stage2, but direct KRX price, offtake and margin are missing.",
    ),
)

ROUND324_TRIGGER_RECORDS: tuple[Round324TriggerRecord, ...] = (
    Round324TriggerRecord("r3l17_samsung_sdi_ess_T1", "r3_loop17_samsung_sdi_ess_lfp", "Stage2-Actionable_ESS_LFP_contract", "2025-12-09", "Samsung SDI America LFP ESS contract above 2T won, +6.1% vs KOSPI -0.1%.", 6.1, "excellent_stage2_actionable_ESS_pivot", "Stage2-Actionable", {"market_relative_pp": 6.2, "contract_value_usd_bn": 1.36}),
    Round324TriggerRecord("r3l17_lges_ford_cancel_T0", "r3_loop17_lges_ford_freudenberg_cancellation", "4C_contract_cancellation", "2025-12-17", "Ford cancels 9.6T won / $6.5B EV battery supply deal; LGES -7.6%.", -7.6, "hard_4C_contract_quality_break", "4C", {"market_relative_pp": -6.2, "ford_contract_value_krw_trn": 9.6}),
    Round324TriggerRecord("r3l17_lges_freudenberg_cancel_T2", "r3_loop17_lges_ford_freudenberg_cancellation", "4C_contract_cancellation_escalation", "2025-12-26", "Freudenberg 3.9T won / $2.7B contract also cancelled.", "price_data_unavailable_after_deep_search", "contract_cancellation_escalation", "4C", {"freudenberg_contract_value_krw_trn": 3.9, "expected_revenue_loss_krw_trn": 13.5}),
    Round324TriggerRecord("r3l17_sk_on_flatiron_T0", "r3_loop17_sk_on_ess_flatiron_ford_jv", "Stage2_ESS_pivot", "2025-09-03", "SK On signs Flatiron Energy deal for up to 7.2GWh LFP ESS batteries.", "price_data_unavailable_unlisted_subsidiary", "Stage2_ESS_pivot_parent_readthrough_unavailable", "Stage2", {"ess_volume_gwh": 7.2, "supply_period": "2026-2030"}),
    Round324TriggerRecord("r3l17_lithium_rebound_T0", "r3_loop17_lithium_rebound_posco_future_m_lnf", "cyclical_Stage2_lithium_rebound", "2025-08-11", "CATL mine suspension drives POSCO Future M +8.3% and L&F +10%.", "POSCO_Future_M_+8.3_L&F_+10", "cyclical_lithium_stage2_not_green", "Stage2_cyclical", {"kospi_same_context_pct": -0.1}),
    Round324TriggerRecord("r3l17_samsung_sdi_solid_state_T0", "r3_loop17_samsung_sdi_solid_state_timeline", "Stage3-Yellow_candidate_solid_state_timeline", "2024-03-07", "Samsung SDI sets 2027 all-solid-state timeline; shares +11% to 405,500 won.", 11, "solid_state_yellow_candidate_not_green", "Stage3-Yellow_candidate", {"entry_price_krw": 405500, "kospi_same_context_pct": 0.3}),
    Round324TriggerRecord("r3l17_lges_ampc_T0", "r3_loop17_lges_ira_ampc_earnings", "Stage2_earnings_policy_credit_4B", "2025-07-07", "Q2 OP +152% YoY, but ex-AMPC OP only 1.4B won and margin 0.03%.", 2.4, "earnings_good_but_policy_credit_4B", "Stage2+4B", {"operating_profit_ex_ampc_krw_bn": 1.4, "operating_margin_ex_ampc_pct": 0.03}),
    Round324TriggerRecord("r3l17_samsung_sdi_capital_raise_T1", "r3_loop17_samsung_sdi_capital_raise_dilution", "4B_capital_raise_dilution", "2025-04-09", "Samsung SDI cuts 2T won share-sale price by 14%.", -1, "capital_raise_dilution_4B", "4B-watch", {"offering_price_cut_pct": 14, "ytd_return_context_pct": -29.5}),
    Round324TriggerRecord("r3l17_posco_minres_lithium_T0", "r3_loop17_posco_minres_lithium_jv", "Stage2_upstream_lithium_supply_no_price", "2025-11-11", "POSCO buys MinRes lithium stake for $765M; MinRes +10.8%, POSCO direct price unavailable.", "MinRes_+10.8_POSCO_unavailable", "Stage2_upstream_lithium_no_direct_price", "Stage2", {"deal_value_usd_mn": 765}),
)

ROUND324_SHADOW_WEIGHT_ROWS: tuple[dict[str, str], ...] = (
    {"archetype": E2RArchetype.ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE.value, "ess_lfp_contract_visibility": "+5", "line_conversion_utilization": "+5", "contract_cancellation_risk": "+1", "lithium_price_inventory_rebound": "+0", "solid_state_commercialization_timeline": "+1", "non_credit_operating_margin": "+3", "upstream_lithium_supply_control": "+0", "market_relative_return": "+4", "ev_contract_backlog_without_cancellation_check_penalty": "-2", "ampc_credit_dependency_ignored_penalty": "-2", "ess_headline_without_customer_margin_penalty": "-4", "solid_state_timeline_without_revenue_penalty": "-1", "stage2_actionable_promote": "ESS LFP contract with +6.1% event return", "stage3_yellow_gate": "customer/margin/delivery missing", "stage3_green_gate": "customer+margin+delivery", "notes": "Samsung SDI."},
    {"archetype": E2RArchetype.EV_CONTRACT_CANCELLATION_4C.value, "ess_lfp_contract_visibility": "+0", "line_conversion_utilization": "+0", "contract_cancellation_risk": "+5", "lithium_price_inventory_rebound": "+0", "solid_state_commercialization_timeline": "+0", "non_credit_operating_margin": "+2", "upstream_lithium_supply_control": "+0", "market_relative_return": "+3", "ev_contract_backlog_without_cancellation_check_penalty": "-5", "ampc_credit_dependency_ignored_penalty": "-1", "ess_headline_without_customer_margin_penalty": "-1", "solid_state_timeline_without_revenue_penalty": "-1", "stage2_actionable_promote": "blocked by cancellation", "stage3_yellow_gate": "utilization break", "stage3_green_gate": "replacement orders+utilization recovery", "notes": "LGES."},
    {"archetype": E2RArchetype.SK_ON_ESS_PIVOT_STAGE2_WITH_PARENT_READTHROUGH.value, "ess_lfp_contract_visibility": "+4", "line_conversion_utilization": "+5", "contract_cancellation_risk": "+2", "lithium_price_inventory_rebound": "+0", "solid_state_commercialization_timeline": "+0", "non_credit_operating_margin": "+3", "upstream_lithium_supply_control": "+0", "market_relative_return": "+1", "ev_contract_backlog_without_cancellation_check_penalty": "-2", "ampc_credit_dependency_ignored_penalty": "-2", "ess_headline_without_customer_margin_penalty": "-4", "solid_state_timeline_without_revenue_penalty": "-1", "stage2_actionable_promote": "ESS pivot with unlisted subsidiary", "stage3_yellow_gate": "parent readthrough missing", "stage3_green_gate": "ESS revenue+margin+parent contribution", "notes": "SK On."},
    {"archetype": E2RArchetype.LITHIUM_PRICE_REBOUND_CYCLICAL_STAGE2.value, "ess_lfp_contract_visibility": "+0", "line_conversion_utilization": "+0", "contract_cancellation_risk": "+1", "lithium_price_inventory_rebound": "+5", "solid_state_commercialization_timeline": "+0", "non_credit_operating_margin": "+2", "upstream_lithium_supply_control": "+3", "market_relative_return": "+4", "ev_contract_backlog_without_cancellation_check_penalty": "-1", "ampc_credit_dependency_ignored_penalty": "-1", "ess_headline_without_customer_margin_penalty": "-1", "solid_state_timeline_without_revenue_penalty": "-1", "stage2_actionable_promote": "lithium mine suspension triggered materials rally", "stage3_yellow_gate": "durability missing", "stage3_green_gate": "lithium price sustained+cathode margin", "notes": "POSCO Future M/L&F."},
    {"archetype": E2RArchetype.SOLID_STATE_TIMELINE_STAGE2_YELLOW_CANDIDATE.value, "ess_lfp_contract_visibility": "+1", "line_conversion_utilization": "+1", "contract_cancellation_risk": "+0", "lithium_price_inventory_rebound": "+0", "solid_state_commercialization_timeline": "+5", "non_credit_operating_margin": "+2", "upstream_lithium_supply_control": "+0", "market_relative_return": "+5", "ev_contract_backlog_without_cancellation_check_penalty": "-1", "ampc_credit_dependency_ignored_penalty": "-1", "ess_headline_without_customer_margin_penalty": "-1", "solid_state_timeline_without_revenue_penalty": "-5", "stage2_actionable_promote": "strong technology timeline rally", "stage3_yellow_gate": "revenue/yield missing", "stage3_green_gate": "pilot yield+customer adoption", "notes": "Samsung SDI."},
    {"archetype": E2RArchetype.IRA_AMPC_EARNINGS_WITH_POLICY_4B.value, "ess_lfp_contract_visibility": "+0", "line_conversion_utilization": "+1", "contract_cancellation_risk": "+1", "lithium_price_inventory_rebound": "+0", "solid_state_commercialization_timeline": "+0", "non_credit_operating_margin": "+5", "upstream_lithium_supply_control": "+0", "market_relative_return": "+1", "ev_contract_backlog_without_cancellation_check_penalty": "-2", "ampc_credit_dependency_ignored_penalty": "-5", "ess_headline_without_customer_margin_penalty": "-1", "solid_state_timeline_without_revenue_penalty": "-1", "stage2_actionable_promote": "headline profit credit-dependent", "stage3_yellow_gate": "underlying margin missing", "stage3_green_gate": "non-credit margin+utilization", "notes": "LGES."},
    {"archetype": E2RArchetype.CAPITAL_RAISE_DILUTION_4B.value, "ess_lfp_contract_visibility": "+1", "line_conversion_utilization": "+2", "contract_cancellation_risk": "+1", "lithium_price_inventory_rebound": "+0", "solid_state_commercialization_timeline": "+0", "non_credit_operating_margin": "+2", "upstream_lithium_supply_control": "+0", "market_relative_return": "-2", "ev_contract_backlog_without_cancellation_check_penalty": "-1", "ampc_credit_dependency_ignored_penalty": "-1", "ess_headline_without_customer_margin_penalty": "-1", "solid_state_timeline_without_revenue_penalty": "-1", "stage2_actionable_promote": "blocked by dilution", "stage3_yellow_gate": "dilution/capex ROI missing", "stage3_green_gate": "capex ROI+utilization", "notes": "Samsung SDI."},
    {"archetype": E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE.value, "ess_lfp_contract_visibility": "+0", "line_conversion_utilization": "+0", "contract_cancellation_risk": "+1", "lithium_price_inventory_rebound": "+3", "solid_state_commercialization_timeline": "+0", "non_credit_operating_margin": "+2", "upstream_lithium_supply_control": "+5", "market_relative_return": "+1", "ev_contract_backlog_without_cancellation_check_penalty": "-1", "ampc_credit_dependency_ignored_penalty": "-1", "ess_headline_without_customer_margin_penalty": "-1", "solid_state_timeline_without_revenue_penalty": "-1", "stage2_actionable_promote": "upstream lithium stake", "stage3_yellow_gate": "POSCO direct price unavailable", "stage3_green_gate": "offtake+margin+lithium recovery", "notes": "POSCO/MinRes."},
)


def round324_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND324_CASE_CANDIDATES]


def round324_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND324_CASE_CANDIDATES]


def round324_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND324_TRIGGER_RECORDS]


def round324_shadow_weight_rows() -> list[dict[str, str]]:
    return [dict(row) for row in ROUND324_SHADOW_WEIGHT_ROWS]


def round324_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND324_REQUIRED_TARGET_ALIASES.items()]


def round324_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND324_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND324_SCORE_DOWN_AXES]
    )


def round324_summary() -> dict[str, object]:
    return {
        "source_round": ROUND324_SOURCE_ROUND_PATH,
        "round_id": ROUND324_ANALYST_ROUND_ID,
        "loop_name": ROUND324_LOOP_NAME,
        "large_sector": ROUND324_LARGE_SECTOR,
        "method": ROUND324_METHOD,
        "case_candidate_count": len(ROUND324_CASE_CANDIDATES),
        "trigger_count": len(ROUND324_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND324_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 1,
        "stage2_candidate_count": 5,
        "stage3_yellow_candidate_count": 4,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 5,
        "stage4c_watch_count": 1,
        "strong_4c_case_count": 1,
        "policy_credit_4b_count": 1,
        "cyclical_stage2_count": 1,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R4 Loop 17",
    }


def round324_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND324_SOURCE_ROUND_PATH,
        "round_id": ROUND324_ANALYST_ROUND_ID,
        "loop_name": ROUND324_LOOP_NAME,
        "large_sector": ROUND324_LARGE_SECTOR,
        "method": ROUND324_METHOD,
        "summary": round324_summary(),
        "required_target_aliases": dict(ROUND324_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND324_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND324_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND324_STAGE3_GREEN_RULES,
        "green_blockers": ROUND324_GREEN_BLOCKERS,
        "score_up_axes": ROUND324_SCORE_UP_AXES,
        "score_down_axes": ROUND324_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND324_STAGE4B_WATCH_TRIGGERS,
        "hard_4c_gates": ROUND324_HARD_4C_GATES,
        "row_separation_rules": ROUND324_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round324_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
            "do_not_treat_ESS_contract_AMPC_profit_lithium_rebound_solid_state_timeline_or_dilution_as_Green_without_customer_margin_utilization_revenue_and_risk_resolution",
        ),
    }


def render_round324_summary_markdown() -> str:
    summary = round324_summary()
    lines = [
        "# R3 Loop 17 Secondary Battery / EV / Green Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: an ESS contract can promote Stage2 when contract value and event return are clear, but it is not Green until customer, utilization and margin are confirmed.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Samsung SDI ESS LFP is the cleanest Stage2-Actionable anchor.",
            "- LGES Ford/Freudenberg cancellations are a strong 4C contract-quality break.",
            "- SK On ESS pivot is Stage2, but parent readthrough and losses remain 4B.",
            "- POSCO Future M / L&F lithium rebound is cyclical Stage2, not Green.",
            "- Samsung SDI solid-state timeline is a Stage3-Yellow candidate, not Green before pilot yield and revenue.",
            "- LGES AMPC earnings are policy-credit 4B because ex-AMPC margin is near zero.",
            "- Samsung SDI capital raise is dilution 4B.",
            "- POSCO / MinRes lithium JV is Stage2 no-price until direct KRX price, offtake and margin are available.",
            "- Stage3-Green confirmed: `0`.",
            "- Strong 4C case count: `1`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round324_trigger_grid_markdown() -> str:
    lines = [
        "# Round 324 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round324_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round324_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 324 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND324_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND324_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND324_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND324_GREEN_BLOCKERS),
            "",
            "## Hard 4C Gates",
            *_bullet_lines(ROUND324_HARD_4C_GATES),
        ]
    ) + "\n"


def render_round324_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 324 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND324_STAGE4B_WATCH_TRIGGERS),
        "",
        "## Hard 4C Gates",
        *_bullet_lines(ROUND324_HARD_4C_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND324_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round324_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 324 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available; full adjusted OHLC backfill remains required before full-window MFE/MAE claims. Reported event returns and event prices are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND324_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round324_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 324 Row Separation Plan",
        "",
        "Battery rows must separate case evidence, trigger anchors and full adjusted OHLC backfill.",
        "",
        "Easy example: LGES AMPC earnings may look strong, but if ex-AMPC margin is 0.03%, the row must show policy-credit 4B instead of Green.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND324_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round324_r3_loop17_reports(
    output_directory: str | Path = ROUND324_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND324_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND324_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND324_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND324_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round324_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND324_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round324_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round324_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round324_r3_loop17_case_matrix.csv",
        "target_aliases": output_dir / "round324_r3_loop17_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round324_r3_loop17_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round324_r3_loop17_trigger_grid.md",
        "summary": output_dir / "round324_r3_loop17_trigger_validation_summary.md",
        "stage_rules": output_dir / "round324_r3_loop17_stage_rules.md",
        "stage4b_4c_review": output_dir / "round324_r3_loop17_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round324_r3_loop17_score_adjustments.csv",
        "shadow_weights": output_dir / "round324_r3_loop17_shadow_weights.csv",
        "price_validation_plan": output_dir / "round324_r3_loop17_price_validation_plan.md",
        "row_separation_plan": output_dir / "round324_r3_loop17_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round324_case_rows())
    _write_csv(paths["target_aliases"], round324_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round324_trigger_rows())
    _write_csv(paths["score_adjustments"], round324_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round324_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round324_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round324_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round324_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round324_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round324_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round324_row_separation_plan_markdown(), encoding="utf-8")
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


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    return str(value)


def _bullet_lines(items: Iterable[str]) -> list[str]:
    return [f"- {item}" for item in items]


__all__ = [
    "ROUND324_CASE_CANDIDATES",
    "ROUND324_GREEN_BLOCKERS",
    "ROUND324_HARD_4C_GATES",
    "ROUND324_LARGE_SECTOR",
    "ROUND324_REQUIRED_TARGET_ALIASES",
    "ROUND324_ROW_SEPARATION_RULES",
    "ROUND324_SCORE_DOWN_AXES",
    "ROUND324_SCORE_UP_AXES",
    "ROUND324_SHADOW_WEIGHT_ROWS",
    "ROUND324_STAGE2_ACTIONABLE_RULES",
    "ROUND324_STAGE3_GREEN_RULES",
    "ROUND324_STAGE3_YELLOW_RULES",
    "ROUND324_STAGE4B_WATCH_TRIGGERS",
    "ROUND324_TRIGGER_RECORDS",
    "render_round324_stage4b_4c_review_markdown",
    "render_round324_stage_rules_markdown",
    "render_round324_trigger_grid_markdown",
    "round324_audit_payload",
    "round324_case_records",
    "round324_case_rows",
    "round324_shadow_weight_rows",
    "round324_summary",
    "round324_trigger_rows",
    "write_round324_r3_loop17_reports",
]
