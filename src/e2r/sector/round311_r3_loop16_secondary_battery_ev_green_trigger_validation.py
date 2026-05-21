"""Round-311 R3 Loop-16 secondary battery, EV and green validation pack.

This module converts ``docs/round/round_311.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a USD 1.36B LFP ESS contract can be Stage2-Actionable when
contract size, delivery period, U.S. line conversion and price reaction are
clear. It still cannot become Stage3-Green until ESS margin, retrofit yield,
repeat orders and utilization are verified.
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


ROUND311_SOURCE_ROUND_PATH = "docs/round/round_311.md"
ROUND311_ANALYST_ROUND_ID = "round_239"
ROUND311_LARGE_SECTOR = "SECONDARY_BATTERY_EV_GREEN"
ROUND311_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND311_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round311_r3_loop16_secondary_battery_ev_green_trigger_validation"
ROUND311_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop16_round239.jsonl"
ROUND311_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r3_loop16_round239.jsonl"
ROUND311_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round311_r3_loop16_secondary_battery_ev_green_trigger_validation_audit.json"
ROUND311_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round239_r3_loop16_v1.csv"

ROUND311_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE": E2RArchetype.ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE.value,
    "EV_BATTERY_OEM_SUPPLY_STAGE2_WITH_UTILIZATION_GATE": E2RArchetype.EV_BATTERY_OEM_SUPPLY_STAGE2_WITH_UTILIZATION_GATE.value,
    "EV_DEMAND_SLOWDOWN_4C_WATCH": E2RArchetype.EV_DEMAND_SLOWDOWN_4C_WATCH.value,
    "BATTERY_JV_RESTRUCTURING_RELIEF_STAGE2_WITH_FINANCIAL_4B": E2RArchetype.BATTERY_JV_RESTRUCTURING_RELIEF_STAGE2_WITH_FINANCIAL_4B.value,
    "LITHIUM_SUPPLY_SHOCK_CYCLICAL_STAGE2": E2RArchetype.LITHIUM_SUPPLY_SHOCK_CYCLICAL_STAGE2.value,
    "BATTERY_MATERIAL_LITHIUM_BETA_EVENT_PREMIUM": E2RArchetype.BATTERY_MATERIAL_LITHIUM_BETA_EVENT_PREMIUM.value,
    "BATTERY_FACTORY_SAFETY_HARD_4C": E2RArchetype.BATTERY_FACTORY_SAFETY_HARD_4C.value,
    "CAPITAL_RAISE_DILUTION_4B": E2RArchetype.CAPITAL_RAISE_DILUTION_4B.value,
}

ROUND311_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "contract_value_or_GWh_scale_is_clear",
    "delivery_period_and_production_facility_are_clear",
    "event_return_at_least_5pct_or_market_relative_return_at_least_5pp",
    "EV_line_to_ESS_line_conversion_or_utilization_defense_is_visible",
    "customer_demand_links_to_model_platform_or_ESS_infrastructure_use_case",
    "no_dilution_cancellation_safety_or_subsidy_4c_overlay",
)

ROUND311_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_FCF_path_can_change_materially",
    "one_of_utilization_line_conversion_margin_subsidy_or_safety_remains_open",
    "reported_price_anchor_or_relative_strength_supports_trigger",
    "case_is_not_pure_lithium_beta_restructuring_relief_or_capex_funding",
)

ROUND311_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "GWh_contract_converts_to_utilization_and_margin",
    "ESS_line_conversion_yield_is_stable",
    "profit_survives_without_IRA_or_subsidy_credit",
    "OEM_cancellation_risk_is_low",
    "lithium_rebound_converts_to_inventory_reversal_and_ASP_margin",
    "safety_quality_hard_gate_is_clear",
    "full_adjusted_OHLC_MFE_MAE_path_supports_stage_candidate",
)

ROUND311_GREEN_BLOCKERS: tuple[str, ...] = (
    "EV_growth_headline_without_utilization",
    "large_GWh_contract_without_margin",
    "ESS_pivot_without_line_yield",
    "lithium_price_spike_without_margin",
    "restructuring_relief_without_profit",
    "capex_funding_with_dilution",
    "OEM_contract_cancellation_or_plant_idling",
    "battery_factory_fire_quality_or_death_event",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND311_SCORE_UP_AXES: tuple[str, ...] = (
    "ESS_LFP_contract_visibility",
    "US_line_conversion_utilization",
    "OEM_contract_cancellation_risk",
    "IRA_tax_credit_dependency",
    "battery_JV_financial_structure",
    "lithium_price_beta_duration",
    "battery_factory_safety_trust",
)

ROUND311_SCORE_DOWN_AXES: tuple[str, ...] = (
    "EV_growth_headline_without_utilization",
    "large_GWh_contract_without_margin",
    "ESS_pivot_without_line_yield",
    "lithium_price_spike_without_margin",
    "restructuring_relief_without_profit",
    "capex_funding_with_dilution",
)

ROUND311_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "EV_demand_slowdown_with_capex_funding_priced_as_growth",
    "ESS_conversion_headline_rerates_before_line_yield_and_margin",
    "lithium_price_spike_rerates_materials_before_cathode_margin",
    "restructuring_merger_rerates_before_profit_turnaround",
    "GWh_contract_rerates_before_customer_production_plan_and_call_off",
    "share_issuance_funds_capex_while_stock_price_falls",
)

ROUND311_4C_WATCH_GATES: tuple[str, ...] = (
    "OEM_battery_contract_cancellation",
    "EV_model_cancellation_causing_plant_idling",
    "subsidy_expiry_causing_demand_cliff_or_loss_exposure",
    "factory_fire_deaths_or_quality_failure",
    "line_utilization_collapse",
    "capital_raise_under_falling_share_price",
    "customer_concentration_loss",
)

ROUND311_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_contract_value_loss_or_safety_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_GWh_capex_restructuring_or_lithium_beta_headline_as_utilization_margin_or_FCF",
)


@dataclass(frozen=True)
class Round311ShadowWeightRow:
    archetype: E2RArchetype
    ess_lfp_contract_visibility: int
    us_line_conversion_utilization: int
    oem_contract_cancellation_risk: int
    ira_tax_credit_dependency: int
    battery_jv_financial_structure: int
    lithium_price_beta_duration: int
    battery_factory_safety_trust: int
    ev_growth_headline_without_utilization_penalty: int
    large_gwh_contract_without_margin_penalty: int
    ess_pivot_without_line_yield_penalty: int
    lithium_price_spike_without_margin_penalty: int
    restructuring_relief_without_profit_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "ess_lfp_contract_visibility": _signed(self.ess_lfp_contract_visibility),
            "US_line_conversion_utilization": _signed(self.us_line_conversion_utilization),
            "OEM_contract_cancellation_risk": _signed(self.oem_contract_cancellation_risk),
            "IRA_tax_credit_dependency": _signed(self.ira_tax_credit_dependency),
            "battery_JV_financial_structure": _signed(self.battery_jv_financial_structure),
            "lithium_price_beta_duration": _signed(self.lithium_price_beta_duration),
            "battery_factory_safety_trust": _signed(self.battery_factory_safety_trust),
            "EV_growth_headline_without_utilization_penalty": _signed(self.ev_growth_headline_without_utilization_penalty),
            "large_GWh_contract_without_margin_penalty": _signed(self.large_gwh_contract_without_margin_penalty),
            "ESS_pivot_without_line_yield_penalty": _signed(self.ess_pivot_without_line_yield_penalty),
            "lithium_price_spike_without_margin_penalty": _signed(self.lithium_price_spike_without_margin_penalty),
            "restructuring_relief_without_profit_penalty": _signed(self.restructuring_relief_without_profit_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round311TriggerRecord:
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
class Round311CaseCandidate:
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
            "do_not_use_round311_cases_as_candidate_generation_input",
            "do_not_treat_battery_contract_capex_restructuring_or_lithium_beta_as_green_without_utilization_margin_safety_evidence",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND311_LARGE_SECTOR,
            large_sector=ROUND311_LARGE_SECTOR,
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
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4b" in field or "dilution" in field or "utilization" in field),
            stage4c_evidence=tuple(
                field
                for field in (*self.red_flag_fields, *self.evidence_fields)
                if "4c" in field or "cancellation" in field or "fire" in field or "layoff" in field or "loss" in field or "safety" in field
            ),
            must_have_fields=ROUND311_STAGE3_GREEN_RULES,
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
                stage_dates_confidence=0.78 if not self.stage4c_date else 0.86,
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


ROUND311_CASE_CANDIDATES: tuple[Round311CaseCandidate, ...] = (
    Round311CaseCandidate(
        "r3_loop16_samsung_sdi_lfp_ess",
        "006400",
        "Samsung SDI",
        E2RArchetype.ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE,
        (E2RArchetype.ESS_LFP_GRID_STORAGE_KOREA, E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT_KOREA),
        "success_candidate",
        "ess_lfp_stage2_actionable_line_conversion",
        "r3l16_samsungsdi_lfp_ess_T1",
        "Stage2-Actionable",
        "Stage2-Actionable / Yellow deferred",
        date(2025, 12, 10),
        date(2025, 12, 10),
        None,
        date(2025, 12, 10),
        None,
        False,
        ("contract_value_2tn_krw", "contract_value_1_36bn_usd", "delivery_start_2027", "contract_duration_3_years", "LFP_prismatic_ESS", "US_EV_line_to_ESS_line_conversion", "event_return_6_1pct", "market_relative_6_2pp"),
        ("customer_identity_missing", "ESS_margin_missing", "line_retrofit_yield_missing", "repeat_order_visibility_missing", "US_facility_utilization_missing", "ESS_pivot_without_line_yield"),
        6.1,
        None,
        None,
        None,
        None,
        None,
        {"contract_value_krw_trn": 2.0, "contract_value_usd_bn": 1.36, "delivery_start_year": 2027, "contract_duration_years": 3, "battery_type": "LFP_prismatic_ESS", "line_conversion": "existing_U.S._EV_lines_to_ESS_lines", "event_return_pct": 6.1, "kospi_same_context_pct": -0.1, "market_relative_return_pp": 6.2},
        "aligned",
        "excellent_stage2_actionable_ESS_conversion",
        "unknown",
        "stage2_watch_success",
        "ESS contract plus U.S. line conversion and strong relative price reaction make this clean Stage2-Actionable. Margin and retrofit yield are Green gates.",
    ),
    Round311CaseCandidate(
        "r3_loop16_lges_rivian_tesla_lfp",
        "373220",
        "LG Energy Solution",
        E2RArchetype.EV_BATTERY_OEM_SUPPLY_STAGE2_WITH_UTILIZATION_GATE,
        (E2RArchetype.US_BATTERY_LOCALIZATION, E2RArchetype.ESS_TESLA_MEGAPACK_SUPPLY_CHAIN),
        "success_candidate",
        "ev_battery_oem_supply_stage2_price_muted",
        "r3l16_lges_rivian_T0/r3l16_lges_tesla_lfp_T1",
        "Stage2_supply_contract_with_utilization_gate",
        "Stage2 / utilization gate",
        date(2024, 11, 7),
        date(2024, 11, 7),
        None,
        date(2025, 7, 30),
        None,
        False,
        ("Rivian_67GWh_contract", "Rivian_5_year_contract", "4695_cylindrical_cell", "Tesla_LFP_ESS_4_3bn_usd", "2027_08_to_2030_07_supply_period", "US_factories_expected", "Tesla_contract_event_return_0_6pct"),
        ("ESS_line_utilization_missing", "LFP_margin_missing", "customer_take_or_pay_terms_missing", "production_ramp_schedule_missing", "IRA_credit_dependency", "large_GWh_contract_without_margin"),
        0.6,
        None,
        None,
        None,
        None,
        None,
        {"rivian_contract_gwh": 67, "rivian_contract_duration_years": 5, "cell_type_rivian": "4695_cylindrical", "target_model": "Rivian_R2", "tesla_lfp_contract_value_usd_bn": 4.3, "tesla_supply_period": "2027-08_to_2030-07", "tesla_contract_event_return_pct": 0.6},
        "evidence_good_but_price_failed",
        "Stage2_contract_price_muted",
        "unknown",
        "stage2_watch_success",
        "Rivian and Tesla contracts are real Stage2 evidence, but muted price reaction and open utilization/margin gates block Yellow and Green.",
    ),
    Round311CaseCandidate(
        "r3_loop16_lges_ford_cancellation_ohio_loss",
        "373220",
        "LG Energy Solution",
        E2RArchetype.EV_DEMAND_SLOWDOWN_4C_WATCH,
        (E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C, E2RArchetype.BATTERY_TAX_CREDIT_QUALITY_OVERLAY),
        "4c_thesis_break",
        "ev_demand_cancellation_utilization_4c_watch",
        "r3l16_lges_ford_cancel_T1",
        "4C_watch_demand_cancellation_utilization",
        "4C-watch",
        date(2025, 12, 17),
        None,
        None,
        None,
        date(2025, 12, 18),
        False,
        ("Ford_cancelled_9_6tn_krw_contract", "cancelled_contract_6_5bn_usd", "LGES_event_return_minus_7_6pct", "market_relative_minus_6_2pp", "Q1_2026_OP_loss_208bn_krw", "loss_without_IRA_credit_398bn_krw", "Ohio_Ultium_850_layoffs_or_idled", "restart_date_uncertain"),
        ("OEM_contract_cancellation", "plant_idling", "IRA_tax_credit_dependency", "operating_loss", "demand_slowdown_4c_watch", "customer_model_cancellation"),
        None,
        -7.6,
        None,
        None,
        None,
        None,
        {"cancelled_contract_value_krw_trn": 9.6, "cancelled_contract_value_usd_bn": 6.5, "event_mae_pct": -7.6, "kospi_same_context_pct": -1.4, "market_relative_return_pp": -6.2, "q1_2026_op_loss_krw_bn": 208, "q1_2026_loss_without_ira_credit_krw_bn": 398, "ultium_ohio_laid_off_or_idled_workers": 850, "restart_date_status": "uncertain"},
        "aligned",
        "demand_cancellation_4C_watch",
        "thesis_break",
        "should_have_been_red",
        "Contract cancellation, operating loss and Ohio idling make this a direct 4C-watch against EV battery utilization.",
    ),
    Round311CaseCandidate(
        "r3_loop16_sk_innovation_skes_merger_skon_relief",
        "096770",
        "SK Innovation / SK On",
        E2RArchetype.BATTERY_JV_RESTRUCTURING_RELIEF_STAGE2_WITH_FINANCIAL_4B,
        (E2RArchetype.EV_BATTERY_JV_RESTRUCTURING, E2RArchetype.TURNAROUND_COST_RESTRUCTURING),
        "4b_watch",
        "battery_jv_financial_relief_not_profit_green",
        "r3l16_sk_inno_skes_T1",
        "Stage2_relief_with_financial_4B",
        "Stage2 relief + 4B-watch",
        date(2024, 7, 17),
        date(2024, 8, 27),
        None,
        date(2024, 8, 27),
        None,
        False,
        ("SK_Innovation_SK_ES_merger", "merged_asset_company_100tn_krw", "SK_Innovation_event_return_5pct", "market_relative_5_5pp", "SK_On_cumulative_OP_losses_2_3tn_krw", "SK_On_debt_to_equity_188pct", "SK_ES_2023_OP_1_3tn_krw"),
        ("SK_On_profitability_missing", "battery_shipment_recovery_missing", "factory_utilization_missing", "customer_order_visibility_missing", "debt_ratio_improvement_after_merger_missing", "restructuring_relief_without_profit"),
        5.0,
        None,
        None,
        None,
        None,
        None,
        {"merged_asset_company_krw_trn": 100, "event_return_pct": 5, "kospi_same_context_pct": -0.5, "market_relative_return_pp": 5.5, "sk_on_cumulative_op_losses_krw_trn": 2.3, "sk_on_debt_to_equity_pct": 188, "sk_es_2023_op_krw_trn": 1.3},
        "aligned",
        "Stage2_financial_relief_not_Green",
        "event_premium",
        "stage2_watch_success",
        "The merger supports SK On's balance sheet, but financial relief is not battery profit turnaround.",
    ),
    Round311CaseCandidate(
        "r3_loop16_sk_battery_america_layoffs",
        "096770_readthrough",
        "SK Battery America / SK On read-through",
        E2RArchetype.EV_DEMAND_SLOWDOWN_4C_WATCH,
        (E2RArchetype.BATTERY_SUPPLY_CHAIN_DEMAND_SHOCK, E2RArchetype.CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK),
        "4c_thesis_break",
        "utilization_customer_demand_4c_watch",
        "r3l16_sk_georgia_layoff_T1",
        "4C_watch_utilization_customer_demand",
        "4C-watch",
        date(2026, 3, 6),
        None,
        None,
        None,
        date(2026, 3, 6),
        False,
        ("SK_Battery_America_layoffs_958_workers", "workforce_cut_37pct", "remaining_workers_1600", "Georgia_plant_cost_2_6bn_usd", "Ford_F150_Lightning_customer_model", "Ford_EV_strategy_shift"),
        ("large_layoffs", "plant_utilization_risk", "customer_model_cancellation", "replacement_customer_missing", "ESS_conversion_missing", "direct_KRX_price_anchor_missing"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"laid_off_workers": 958, "workforce_cut_pct": 37, "remaining_workers": 1600, "plant_cost_usd_bn": 2.6, "customer_model": "Ford_F-150_Lightning", "ford_ev_strategy_change": "cancel_fully_electric_version_for_extended_range_version"},
        "aligned",
        "customer_demand_utilization_4C_watch",
        "thesis_break",
        "should_have_been_red",
        "Layoffs tied to Ford EV strategy shift are a utilization 4C-watch, not an EV recovery signal.",
    ),
    Round311CaseCandidate(
        "r3_loop16_catl_yichun_lithium_beta_korea_materials",
        "003670/066970/006400/373220",
        "POSCO Future M / L&F / Samsung SDI / LGES",
        E2RArchetype.LITHIUM_SUPPLY_SHOCK_CYCLICAL_STAGE2,
        (E2RArchetype.BATTERY_MATERIAL_LITHIUM_BETA_EVENT_PREMIUM, E2RArchetype.COMMODITY_SPREAD),
        "cyclical_success",
        "lithium_supply_shock_cyclical_stage2",
        "r3l16_catl_lithium_beta_T1",
        "cyclical_Stage2_with_4B_watch",
        "cyclical Stage2 / event premium",
        date(2025, 8, 11),
        date(2025, 8, 11),
        None,
        date(2025, 8, 11),
        None,
        False,
        ("CATL_Yichun_lithium_mine_suspension", "POSCO_Future_M_event_return_8_3pct", "L_and_F_event_return_10pct", "Samsung_SDI_event_return_3_2pct", "LGES_event_return_2_8pct", "lithium_price_decline_from_2022_peak_90pct"),
        ("CATL_license_renewal_possible", "CATL_no_material_operational_impact_claim", "sustained_lithium_price_rebound_missing", "cathode_ASP_pass_through_missing", "inventory_write_down_reversal_missing", "lithium_price_spike_without_margin"),
        10.0,
        None,
        None,
        None,
        None,
        None,
        {"posco_future_m_event_return_pct": 8.3, "l_and_f_event_return_pct": 10, "samsung_sdi_event_return_pct": 3.2, "lges_event_return_pct": 2.8, "lithium_price_decline_from_2022_peak_pct": 90, "catl_material_impact_claim": "no_material_operational_impact", "license_renewal_risk": True},
        "aligned",
        "cyclical_lithium_beta_event_premium",
        "cyclical_rerating",
        "stage2_watch_success",
        "The lithium supply shock moved materials, but without cathode ASP and margin evidence this is cyclical Stage2, not Green.",
    ),
    Round311CaseCandidate(
        "r3_loop16_samsung_sdi_share_sale_dilution",
        "006400",
        "Samsung SDI",
        E2RArchetype.CAPITAL_RAISE_DILUTION_4B,
        (E2RArchetype.US_BATTERY_LOCALIZATION_DILUTION, E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT),
        "4b_watch",
        "capital_raise_dilution_capex_funding_4b",
        "r3l16_samsungsdi_share_sale_T1",
        "4B_dilution_capex_funding",
        "4B-watch",
        date(2025, 3, 1),
        None,
        None,
        date(2025, 4, 9),
        None,
        False,
        ("share_issuance_value_2tn_krw", "new_shares_11821000", "offering_price_cut_14pct", "revised_price_146200_krw", "event_return_minus_1pct", "YTD_decline_29_5pct", "GM_JV_Hungary_expansion_use_of_proceeds"),
        ("capex_funding_with_dilution", "falling_share_price", "demand_uncertainty", "margin_missing", "utilization_missing"),
        None,
        -1.0,
        None,
        None,
        None,
        None,
        {"share_issuance_value_krw_trn": 2.0, "new_shares_count": 11821000, "original_offering_price_krw": 169200, "revised_offering_price_krw": 146200, "pricing_cut_pct": 14, "event_return_pct": -1, "kospi_same_context_pct": -0.5, "ytd_decline_pct": -29.5, "use_of_proceeds": ["GM_U.S._joint_venture", "Hungary_factory_expansion", "capacity_investment"]},
        "aligned",
        "capital_raise_dilution_4B",
        "event_premium",
        "false_yellow",
        "Capex funding must be scored with dilution and demand uncertainty. It is not growth evidence by itself.",
    ),
    Round311CaseCandidate(
        "r3_loop16_aricell_battery_factory_fire",
        "096630_readthrough",
        "Aricell / S-Connect read-through",
        E2RArchetype.BATTERY_FACTORY_SAFETY_HARD_4C,
        (E2RArchetype.OPERATIONAL_SAFETY_HARD_4C, E2RArchetype.THESIS_BREAK_4C),
        "4c_thesis_break",
        "hard_4c_safety_quality",
        "r3l16_aricell_fire_T0",
        "hard_4C_safety_quality",
        "4C",
        date(2024, 6, 24),
        None,
        None,
        None,
        date(2024, 6, 24),
        True,
        ("Aricell_battery_factory_fire", "fatalities_23", "injuries_9", "S_Connect_majority_owner", "quality_failures", "rushed_production", "temporary_unskilled_workers", "emergency_training_failure"),
        ("hard_4c_safety_quality", "factory_fire", "deaths", "quality_failure", "regulatory_trust_break", "customer_trust_break"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"fatalities": 23, "injuries": 9, "company": "Aricell", "majority_owner": "S-Connect", "quality_failure_findings": ["failed_April_quality_inspection", "rushed_production_to_meet_deadline", "temporary_unskilled_workers", "overheating_defects", "lack_of_emergency_escape_training"]},
        "aligned",
        "hard_4C_success_battery_safety",
        "thesis_break",
        "should_have_been_red",
        "Fatal battery factory fire, quality failures and safety-training failures are hard 4C safety evidence.",
    ),
)


ROUND311_TRIGGER_RECORDS: tuple[Round311TriggerRecord, ...] = (
    Round311TriggerRecord("r3l16_samsungsdi_lfp_ess_T1", "r3_loop16_samsung_sdi_lfp_ess", "Stage2-Actionable", "2025-12-10", "Samsung SDI America signs >2T won / $1.36B LFP ESS supply deal; deliveries from 2027 for 3 years; shares +6.1% vs KOSPI -0.1%", 6.1, "excellent_stage2_actionable_ESS_conversion", "Stage2-Actionable", {"market_relative_return_pp": 6.2, "contract_value_krw_trn": 2.0, "contract_value_usd_bn": 1.36}),
    Round311TriggerRecord("r3l16_lges_rivian_T0", "r3_loop16_lges_rivian_tesla_lfp", "Stage2_supply_contract", "2024-11-07", "LGES Arizona signs 67GWh / 5-year 4695 cylindrical battery supply deal for Rivian R2", "price_data_unavailable_after_deep_search", "Stage2_contract_utilization_gate", "Stage2", {"rivian_contract_gwh": 67, "rivian_contract_duration_years": 5}),
    Round311TriggerRecord("r3l16_lges_tesla_lfp_T1", "r3_loop16_lges_rivian_tesla_lfp", "Stage2_supply_contract_price_muted", "2025-07-30", "LGES signs $4.3B LFP battery supply deal believed to be Tesla ESS; stock +0.6%", 0.6, "Stage2_contract_price_muted", "Stage2", {"tesla_lfp_contract_value_usd_bn": 4.3}),
    Round311TriggerRecord("r3l16_lges_ford_cancel_T1", "r3_loop16_lges_ford_cancellation_ohio_loss", "4C-watch", "2025-12-18", "Ford cancels 9.6T won / $6.5B LGES EV battery supply deal; LGES -7.6% vs KOSPI -1.4%", -7.6, "demand_cancellation_4C_watch", "4C-watch", {"market_relative_return_pp": -6.2, "q1_2026_op_loss_krw_bn": 208}),
    Round311TriggerRecord("r3l16_sk_inno_skes_T1", "r3_loop16_sk_innovation_skes_merger_skon_relief", "Stage2_relief", "2024-08-27", "SK Innovation shareholders approve SK E&S merger to support SK On; shares +5% vs KOSPI -0.5%; SK On cumulative losses 2.3T won", 5, "Stage2_financial_relief_not_Green", "Stage2_relief", {"market_relative_return_pp": 5.5, "sk_on_cumulative_op_losses_krw_trn": 2.3}),
    Round311TriggerRecord("r3l16_sk_georgia_layoff_T1", "r3_loop16_sk_battery_america_layoffs", "4C-watch", "2026-03-06", "SK Battery America lays off 958 workers / 37% workforce at Georgia plant after Ford EV strategy shift away from F-150 Lightning", "price_data_unavailable_after_deep_search", "customer_demand_utilization_4C_watch", "4C-watch", {"laid_off_workers": 958, "workforce_cut_pct": 37}),
    Round311TriggerRecord("r3l16_catl_lithium_beta_T1", "r3_loop16_catl_yichun_lithium_beta_korea_materials", "cyclical_Stage2", "2025-08-11", "CATL suspends Yichun lithium mine after license expiry; POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%", "POSCO Future M +8.3 / L&F +10 / Samsung SDI +3.2 / LGES +2.8", "cyclical_lithium_beta_event_premium", "Stage2_cyclical", {"posco_future_m_event_return_pct": 8.3, "l_and_f_event_return_pct": 10}),
    Round311TriggerRecord("r3l16_samsungsdi_share_sale_T1", "r3_loop16_samsung_sdi_share_sale_dilution", "4B-watch", "2025-04-09", "Samsung SDI cuts 2T won share-sale price by 14%; shares -1%, KOSPI -0.5%, stock -29.5% YTD", -1, "capital_raise_dilution_4B", "4B-watch", {"pricing_cut_pct": 14, "ytd_decline_pct": -29.5}),
    Round311TriggerRecord("r3l16_aricell_fire_T0", "r3_loop16_aricell_battery_factory_fire", "hard_4C", "2024-06-24/2024-08-23", "Aricell battery fire killed 23 and injured 9; police cited quality failures, rushed production, temporary workers and safety-training failures", "price_data_unavailable_after_deep_search", "hard_4C_success_battery_safety", "4C", {"fatalities": 23, "injuries": 9}),
)


ROUND311_SHADOW_WEIGHT_ROWS: tuple[Round311ShadowWeightRow, ...] = (
    Round311ShadowWeightRow(E2RArchetype.ESS_LFP_LINE_CONVERSION_STAGE2_ACTIONABLE, 5, 5, 2, 3, 1, 1, 2, -3, -3, -4, -1, -1, "ESS contract+line conversion", "margin/retrofit yield missing", "ESS margin+utilization+repeat order", "Samsung SDI LFP ESS."),
    Round311ShadowWeightRow(E2RArchetype.EV_BATTERY_OEM_SUPPLY_STAGE2_WITH_UTILIZATION_GATE, 2, 5, 4, 4, 2, 1, 2, -5, -4, -2, -1, -1, "GWh/OEM contract", "utilization/margin missing", "utilization+margin+customer schedule", "LGES Rivian/Tesla."),
    Round311ShadowWeightRow(E2RArchetype.EV_DEMAND_SLOWDOWN_4C_WATCH, 0, 4, 5, 5, 3, 0, 2, -5, -2, -1, -1, -2, "contract cancellation/idling", "demand recovery pending", "N/A", "LGES Ford/SK layoffs."),
    Round311ShadowWeightRow(E2RArchetype.BATTERY_JV_RESTRUCTURING_RELIEF_STAGE2_WITH_FINANCIAL_4B, 0, 2, 3, 2, 5, 0, 1, -3, -2, -1, -1, -5, "merger/financial relief", "profitability missing", "SK On breakeven+debt improvement", "SK Innovation/SK E&S."),
    Round311ShadowWeightRow(E2RArchetype.LITHIUM_SUPPLY_SHOCK_CYCLICAL_STAGE2, 1, 0, 1, 0, 0, 5, 1, -1, -1, -1, -5, -1, "lithium supply shock", "cathode margin missing", "sustained lithium rebound+margin", "CATL/POSCO Future M/L&F."),
    Round311ShadowWeightRow(E2RArchetype.BATTERY_MATERIAL_LITHIUM_BETA_EVENT_PREMIUM, 0, 0, 1, 0, 0, 5, 1, -1, -1, -1, -5, -1, "materials rally", "inventory/ASP pass-through missing", "ASP+margin recovery", "POSCO Future M/L&F event premium."),
    Round311ShadowWeightRow(E2RArchetype.BATTERY_FACTORY_SAFETY_HARD_4C, 0, 0, 2, 0, 1, 0, 5, -1, -1, -1, -1, -1, "fire/death/quality failure", "remediation missing", "N/A", "Aricell hard 4C."),
    Round311ShadowWeightRow(E2RArchetype.CAPITAL_RAISE_DILUTION_4B, 1, 2, 2, 2, 3, 0, 1, -2, -2, -2, -1, -4, "capex funding with dilution", "demand/margin missing", "capex utilization+margin", "Samsung SDI share sale."),
)


def round311_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND311_CASE_CANDIDATES]


def round311_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND311_CASE_CANDIDATES]


def round311_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND311_TRIGGER_RECORDS]


def round311_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND311_SHADOW_WEIGHT_ROWS]


def round311_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND311_REQUIRED_TARGET_ALIASES.items()]


def round311_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND311_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND311_SCORE_DOWN_AXES]
    )


def round311_summary() -> dict[str, object]:
    return {
        "source_round": ROUND311_SOURCE_ROUND_PATH,
        "round_id": ROUND311_ANALYST_ROUND_ID,
        "large_sector": ROUND311_LARGE_SECTOR,
        "method": ROUND311_METHOD,
        "case_candidate_count": len(ROUND311_CASE_CANDIDATES),
        "trigger_count": len(ROUND311_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND311_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 1,
        "stage2_event_candidate_count": 3,
        "stage3_yellow_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 4,
        "stage4c_watch_count": 3,
        "hard_4c_case_count": 1,
        "evidence_good_but_price_muted_count": 2,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round311_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND311_SOURCE_ROUND_PATH,
        "round_id": ROUND311_ANALYST_ROUND_ID,
        "large_sector": ROUND311_LARGE_SECTOR,
        "method": ROUND311_METHOD,
        "summary": round311_summary(),
        "required_target_aliases": dict(ROUND311_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND311_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND311_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND311_STAGE3_GREEN_RULES,
        "green_blockers": ROUND311_GREEN_BLOCKERS,
        "score_up_axes": ROUND311_SCORE_UP_AXES,
        "score_down_axes": ROUND311_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND311_STAGE4B_WATCH_TRIGGERS,
        "stage4c_watch_gates": ROUND311_4C_WATCH_GATES,
        "row_separation_rules": ROUND311_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round311_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_battery_contract_capex_restructuring_or_lithium_beta_as_green_without_utilization_margin_safety_evidence",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round311_summary_markdown() -> str:
    summary = round311_summary()
    lines = [
        "# R3 Loop 16 Secondary Battery / EV / Green Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: Samsung SDI's LFP ESS contract is Stage2-Actionable because contract value, delivery period, line conversion and price reaction are visible. It is not Green until ESS margin, line-retrofit yield and repeat orders are verified.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- EV cell contracts, ESS conversion, lithium beta, restructuring relief, dilution and safety incidents must be separated.",
            "- GWh or capex headline is not utilization, margin or FCF.",
            "- Stage3-Green confirmed: `0`.",
            "- Battery factory fire and quality failure are hard 4C safety evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round311_trigger_grid_markdown() -> str:
    lines = [
        "# Round 311 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round311_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round311_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 311 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND311_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND311_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND311_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND311_GREEN_BLOCKERS),
            "",
            "## 4C Watch Gates",
            *_bullet_lines(ROUND311_4C_WATCH_GATES),
        ]
    ) + "\n"


def render_round311_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 311 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND311_STAGE4B_WATCH_TRIGGERS),
        "",
        "## 4C Watch Gates",
        *_bullet_lines(ROUND311_4C_WATCH_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND311_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round311_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 311 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND311_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round311_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 311 Row Separation Plan",
        "",
        "Case evidence, trigger anchors and full OHLC windows must be separate rows.",
        "",
        "Easy example: a lithium mine suspension can be a cyclical Stage2 event for materials. It is not Green until company-specific cathode ASP, inventory reversal and margin evidence appear.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND311_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round311_r3_loop16_reports(
    output_directory: str | Path = ROUND311_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND311_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND311_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND311_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND311_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round311_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND311_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round311_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round311_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round311_r3_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round311_r3_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round311_r3_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round311_r3_loop16_trigger_grid.md",
        "summary": output_dir / "round311_r3_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round311_r3_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round311_r3_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round311_r3_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round311_r3_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round311_r3_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round311_r3_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round311_case_rows())
    _write_csv(paths["target_aliases"], round311_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round311_trigger_rows())
    _write_csv(paths["score_adjustments"], round311_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round311_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round311_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round311_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round311_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round311_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round311_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round311_row_separation_plan_markdown(), encoding="utf-8")
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
    "ROUND311_4C_WATCH_GATES",
    "ROUND311_CASE_CANDIDATES",
    "ROUND311_GREEN_BLOCKERS",
    "ROUND311_LARGE_SECTOR",
    "ROUND311_REQUIRED_TARGET_ALIASES",
    "ROUND311_ROW_SEPARATION_RULES",
    "ROUND311_SCORE_DOWN_AXES",
    "ROUND311_SCORE_UP_AXES",
    "ROUND311_SHADOW_WEIGHT_ROWS",
    "ROUND311_STAGE2_ACTIONABLE_RULES",
    "ROUND311_STAGE3_GREEN_RULES",
    "ROUND311_STAGE3_YELLOW_RULES",
    "ROUND311_STAGE4B_WATCH_TRIGGERS",
    "ROUND311_TRIGGER_RECORDS",
    "render_round311_stage4b_4c_review_markdown",
    "render_round311_stage_rules_markdown",
    "render_round311_trigger_grid_markdown",
    "round311_audit_payload",
    "round311_case_records",
    "round311_case_rows",
    "round311_shadow_weight_rows",
    "round311_summary",
    "round311_trigger_rows",
    "write_round311_r3_loop16_reports",
]
