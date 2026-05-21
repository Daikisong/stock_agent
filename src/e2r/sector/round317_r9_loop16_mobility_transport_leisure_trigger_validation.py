"""Round-317 R9 Loop-16 mobility, transport and leisure validation.

This module converts ``docs/round/round_317.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: Hyundai's hybrid/value-up investor day is strong Stage2 evidence.
It is not Stage3-Green until hybrid mix, tariff absorption, OP margin and FCF
are visible as of the replay date.
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


ROUND317_SOURCE_ROUND_PATH = "docs/round/round_317.md"
ROUND317_ANALYST_ROUND_ID = "round_245"
ROUND317_LARGE_SECTOR = "MOBILITY_TRANSPORT_LEISURE"
ROUND317_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND317_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round317_r9_loop16_mobility_transport_leisure_trigger_validation"
ROUND317_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r9_loop16_round245.jsonl"
ROUND317_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r9_loop16_round245.jsonl"
ROUND317_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round317_r9_loop16_mobility_transport_leisure_trigger_validation_audit.json"
ROUND317_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round245_r9_loop16_v1.csv"

ROUND317_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE": E2RArchetype.AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE.value,
    "AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE": E2RArchetype.AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE.value,
    "AUTO_ROBOTICS_OPTIONALITY_STAGE2_WITH_LABOR_4B": E2RArchetype.AUTO_ROBOTICS_OPTIONALITY_STAGE2_WITH_LABOR_4B.value,
    "AUTO_EXPORT_LOGISTICS_DISRUPTION_4C_WATCH": E2RArchetype.AUTO_EXPORT_LOGISTICS_DISRUPTION_4C_WATCH.value,
    "AIRLINE_CONSOLIDATION_STAGE2_WITH_INTEGRATION_4B": E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2_WITH_INTEGRATION_4B.value,
    "AVIATION_SAFETY_HARD_4C": E2RArchetype.AVIATION_SAFETY_HARD_4C.value,
    "CHINA_TOURISM_LEISURE_STAGE2_EVENT": E2RArchetype.CHINA_TOURISM_LEISURE_STAGE2_EVENT.value,
    "CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B": E2RArchetype.CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B.value,
}

ROUND317_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_at_least_5pct_or_market_relative_return_at_least_5pp",
    "sales_ASP_or_OP_margin_target_is_quantified",
    "buyback_dividend_or_capital_return_is_quantified",
    "US_local_capacity_directly_links_to_tariff_hedge",
    "tourism_event_has_spending_yield_drop_or_RevPAR_evidence_before_Yellow",
    "freight_event_has_rate_duration_or_contract_mix_before_Yellow",
    "safety_accident_route_disruption_tariff_or_labor_4B_4C_overlay_is_not_dominant_for_positive_candidate",
)

ROUND317_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_FCF_path_can_change_materially",
    "one_of_tariff_utilization_safety_yield_labor_or_freight_duration_gate_remains_open",
    "reported_price_anchor_supports_trigger_but_full_adjusted_OHLC_is_missing",
)

ROUND317_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "hybrid_EREV_sales_mix_converts_to_OP_margin",
    "tariff_exposure_is_offset_by_US_localization",
    "robotics_optionality_converts_to_measurable_productivity_or_sales",
    "airline_consolidation_produces_route_cost_and_yield_synergy",
    "tourism_policy_converts_to_spending_yield_and_margin",
    "freight_spike_converts_to_contract_rate_earnings_across_quarters",
    "safety_regulatory_and_route_disruption_issues_are_resolved",
    "full_adjusted_OHLC_MFE_MAE_window_supports_stage_candidate",
)

ROUND317_GREEN_BLOCKERS: tuple[str, ...] = (
    "EV_or_hybrid_headline_without_margin",
    "tariff_relief_without_actual_savings",
    "localization_capex_without_utilization_or_ROI",
    "robotics_hype_without_unit_economics_or_labor_agreement",
    "airline_merger_without_integration_synergy",
    "fatal_safety_incident_treated_as_one_off",
    "tourism_policy_without_spending_yield_or_margin",
    "freight_spike_without_contract_duration",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND317_SCORE_UP_AXES: tuple[str, ...] = (
    "hybrid_mix_margin_conversion",
    "shareholder_return_execution",
    "tariff_absorption_localization",
    "us_capacity_utilization",
    "robotics_commercialization",
    "logistics_route_resilience",
    "airline_safety_trust",
    "airline_integration_synergy",
    "tourism_spend_margin",
    "freight_rate_duration",
)

ROUND317_SCORE_DOWN_AXES: tuple[str, ...] = (
    "ev_headline_without_margin",
    "tariff_relief_without_savings",
    "robotics_hype_without_unit_economics",
    "localization_capex_without_roi",
    "airline_merger_without_integration",
    "tourism_policy_without_yield",
    "freight_spike_without_contract_duration",
    "safety_incident_treated_as_one_off",
)

ROUND317_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "tariff_rate_headline_looks_like_relief_but_stock_falls",
    "localization_capex_rallies_before_ROI_is_proven",
    "robotics_optionality_rallies_before_unit_economics_and_labor_agreement",
    "airline_merger_completed_before_integration_synergy",
    "tourism_policy_rallies_before_spending_yield",
    "freight_rates_spike_before_contract_duration",
)

ROUND317_4C_WATCH_GATES: tuple[str, ...] = (
    "fatal_aviation_accident",
    "national_safety_inspection_or_fleet_grounding",
    "route_disruption_causing_delivery_delay_and_cost_spike",
    "tariff_cost_directly_hitting_profit",
    "logistics_route_closure_or_war_risk_insurance_surge",
    "merger_blocked_or_fare_regulation_undermines_synergy",
    "tourism_safety_or_image_shock",
)

ROUND317_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_tariff_hybrid_robotics_airline_tourism_or_freight_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_hybrid_tariff_localization_robotics_airline_tourism_or_freight_headline_as_Green_without_margin_utilization_synergy_yield_or_contract_duration",
)


@dataclass(frozen=True)
class Round317TriggerRecord:
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
class Round317CaseCandidate:
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
            "do_not_use_round317_cases_as_candidate_generation_input",
            "do_not_treat_hybrid_tariff_localization_robotics_airline_tourism_or_freight_headline_as_Green_without_margin_utilization_synergy_yield_or_contract_duration",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND317_LARGE_SECTOR,
            large_sector=ROUND317_LARGE_SECTOR,
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
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4B" in field or "4b" in field or "normalization" in field or "labor" in field or "yield" in field),
            stage4c_evidence=tuple(
                field
                for field in (*self.red_flag_fields, *self.evidence_fields)
                if "4C" in field
                or "4c" in field
                or "tariff" in field
                or "safety" in field
                or "fatal" in field
                or "route" in field
                or "logistics" in field
                or "crash" in field
            ),
            must_have_fields=ROUND317_STAGE3_GREEN_RULES,
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
                stage_dates_confidence=0.82,
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
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND317_CASE_CANDIDATES: tuple[Round317CaseCandidate, ...] = (
    Round317CaseCandidate(
        "r9_loop16_hyundai_hybrid_valueup",
        "005380/000270",
        "Hyundai Motor / Kia",
        E2RArchetype.AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE,
        (E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN, E2RArchetype.HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW),
        "success_candidate",
        "Stage2_Actionable_to_Yellow_candidate",
        "r9l16_hyundai_hybrid_valueup_T1",
        "Stage2-Actionable_to_Stage3-Yellow_candidate",
        "Stage2-Actionable",
        date(2024, 8, 28),
        date(2024, 8, 28),
        None,
        None,
        None,
        False,
        ("2030_sales_target_5_55M", "hybrid_target_1_33M_by_2028", "4T_won_buyback", "35pct_profit_return", "close_plus_4_7pct"),
        ("hybrid_mix_margin_missing", "EREV_launch_sales_missing", "US_tariff_absorption_missing", "China_competition_response_missing", "full_OHLC_MFE_MAE_missing"),
        5.0,
        None,
        {"trigger_date": "2024-08-28", "hyundai_global_sales_target_2030_mn_units": 5.55, "sales_target_increase_vs_2023_pct": 30, "hybrid_sales_target_2028_mn_units": 1.33, "hybrid_sales_target_raise_pct": 40, "buyback_2025_2027_krw_trn": 4, "buyback_2025_2027_usd_bn": 3, "profit_return_ratio_pct": 35, "event_intraday_return_pct": 5, "event_close_return_pct": 4.7, "op_margin_target_2027_pct": "9-10", "op_margin_target_2030_pct": ">10"},
        "aligned",
        "excellent_stage2_actionable_hybrid_valueup",
        "policy_event_rerating",
        "stage2_watch_success",
        "Powertrain strategy, buyback, margin target and price reaction align. Yellow requires hybrid mix margin and tariff absorption.",
    ),
    Round317CaseCandidate(
        "r9_loop16_hyundai_kia_tariff_localization",
        "005380/000270/004020",
        "Hyundai Motor / Kia / Hyundai Steel",
        E2RArchetype.AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE,
        (E2RArchetype.AUTO_TARIFF_MARGIN_4C_WATCH, E2RArchetype.AUTO_LOCALIZATION_CAPEX_OPERATIONAL_4C),
        "4b_watch",
        "4C_tariff_shock_with_Stage2_localization_hedge",
        "r9l16_hyundai_kia_tariff_T0",
        "4C_tariff_shock_with_Stage2_localization_hedge",
        "4C-watch + Stage2 hedge",
        date(2025, 3, 25),
        date(2025, 3, 25),
        None,
        date(2025, 3, 25),
        date(2025, 3, 26),
        False,
        ("US_auto_tariff_25pct", "US_Korea_auto_tariff_15pct", "Hyundai_Group_US_investment_21B", "Louisiana_steel_plant_5_8B", "Hyundai_2025_tariff_cost_4_1T_won"),
        ("tariff_cost_directly_hitting_profit", "actual_tariff_savings_missing", "US_plant_utilization_missing", "steel_localization_ROI_missing", "Hyundai_Steel_capex_4B"),
        7.5,
        -6.6,
        {"tariff_25pct_announcement_date": "2025-03-26", "tariff_25pct_rate": 25, "localization_trigger_date": "2025-03-25", "hyundai_group_us_investment_usd_bn": 21, "hyundai_steel_louisiana_investment_usd_bn": 5.8, "hyundai_steel_capacity_mn_tons": 2.7, "hyundai_localization_event_return_pct": 7.5, "kia_localization_event_return_pct": 4.3, "trade_deal_date": "2025-07-31", "trade_deal_auto_tariff_pct": 15, "hyundai_trade_deal_event_return_pct": -4.5, "kia_trade_deal_event_return_pct": -6.6, "hyundai_2025_tariff_cost_krw_trn": 4.1, "hyundai_2025_tariff_cost_usd_bn": 2.87},
        "aligned",
        "tariff_4C_with_localization_hedge",
        "policy_event_rerating",
        "should_have_been_red",
        "Tariff remains 4C even after 15% deal; U.S. localization is hedge only if savings and margin prove out.",
    ),
    Round317CaseCandidate(
        "r9_loop16_hyundai_boston_dynamics_robotics",
        "005380/000270",
        "Hyundai Motor / Kia / Boston Dynamics",
        E2RArchetype.AUTO_ROBOTICS_OPTIONALITY_STAGE2_WITH_LABOR_4B,
        (E2RArchetype.ROBOTICS_OPTIONALITY_STAGE2_WITH_4B, E2RArchetype.FUTURE_MOBILITY_AI_ROBOTICS_CAPEX),
        "success_candidate",
        "Stage2_robotics_optionality_with_labor_4B",
        "r9l16_hyundai_robotics_T2",
        "Stage2_robotics_optionality_with_labor_4B",
        "Stage2 + 4B-watch",
        date(2026, 1, 22),
        date(2026, 2, 11),
        None,
        date(2026, 1, 22),
        None,
        False,
        ("Atlas_deployment_target_2028", "Atlas_annual_production_target_30000", "Hyundai_plus_5_9pct", "Kia_plus_4_6pct"),
        ("robot_unit_economics_missing", "factory_productivity_gain_missing", "labor_agreement_missing", "capex_ROI_missing", "commercial_customer_sales_missing"),
        5.9,
        None,
        {"atlas_deployment_target_year": 2028, "atlas_annual_production_target_units": 30000, "robotics_event_date": "2026-02-11", "hyundai_event_return_pct": 5.9, "kia_event_return_pct": 4.6, "labor_warning_date": "2026-01-22", "labor_warning": "employment_shock_and_union_approval_required"},
        "aligned",
        "Stage2_robotics_optionality_with_4B_labor_overlay",
        "event_premium",
        "stage2_watch_success",
        "Robotics optionality has price reaction, but unit economics, labor agreement and capex ROI are gates.",
    ),
    Round317CaseCandidate(
        "r9_loop16_hyundai_glovis_export_disruption",
        "005380/086280",
        "Hyundai Motor / Hyundai Glovis",
        E2RArchetype.AUTO_EXPORT_LOGISTICS_DISRUPTION_4C_WATCH,
        (E2RArchetype.AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH, E2RArchetype.AUTO_LOGISTICS_GEOPOLITICAL_DISRUPTION),
        "4b_watch",
        "4C_watch_export_logistics",
        "r9l16_hyundai_glovis_route_T0",
        "4C_watch_export_logistics",
        "4C-watch",
        date(2026, 4, 3),
        None,
        None,
        date(2026, 4, 3),
        date(2026, 4, 3),
        False,
        ("Europe_North_Africa_export_disruption", "Hyundai_minus_1_2pct", "Glovis_minus_0_7pct", "KOSPI_plus_2_7pct", "Middle_East_shipments_minus_49pct"),
        ("route_access_restriction", "fuel_cost", "delivery_delay", "temporary_cargo_storage", "parts_supplier_pressure"),
        None,
        -3.9,
        {"trigger_date": "2026-04-03", "hyundai_event_return_pct": -1.2, "hyundai_glovis_event_return_pct": -0.7, "kospi_same_context_pct": 2.7, "hyundai_market_relative_pp": -3.9, "glovis_market_relative_pp": -3.4, "hyundai_march_global_sales_yoy_pct": -2.3, "middle_east_shipments_yoy_pct": -49},
        "aligned",
        "auto_export_logistics_4C_watch",
        "thesis_break",
        "should_have_been_red",
        "Route disruption, fuel cost and cargo storage cut against auto/export margin.",
    ),
    Round317CaseCandidate(
        "r9_loop16_korean_air_asiana_consolidation",
        "003490/020560/180640/298690",
        "Korean Air / Asiana / Jin Air / Air Busan",
        E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2_WITH_INTEGRATION_4B,
        (E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2, E2RArchetype.AIRLINE_CONSOLIDATION_INTEGRATION),
        "success_candidate",
        "Stage2_airline_consolidation_with_4B_integration",
        "r9l16_korean_air_asiana_T1",
        "Stage2_airline_consolidation_with_4B_integration",
        "Stage2",
        date(2024, 12, 12),
        date(2024, 12, 12),
        None,
        date(2024, 12, 12),
        None,
        False,
        ("Asiana_takeover_1_3B_usd", "Korean_Air_stake_63_88pct", "international_capacity_rank_12", "full_integration_target_2027", "Jin_Air_LCC_integration"),
        ("direct_price_anchor_missing", "route_rationalization_savings_missing", "fare_regulation_impact_missing", "mileage_program_integration_missing", "labor_integration_missing"),
        None,
        None,
        {"takeover_completion_date": "2024-12-12", "deal_value_usd_bn": 1.3, "korean_air_asiana_stake_pct": 63.88, "international_capacity_rank_context": 12, "full_integration_target_year": 2027, "lcc_integration": ["Jin_Air", "Air_Busan", "Air_Seoul"], "direct_price_anchor": "price_data_unavailable_after_deep_search"},
        "unknown",
        "Stage2_airline_consolidation_not_Green",
        "unknown",
        "stage2_watch_success",
        "Consolidation is real but integration, fare regulation, mileage, labor and LCC synergy are gates.",
    ),
    Round317CaseCandidate(
        "r9_loop16_jeju_air_crash_safety_4c",
        "089590",
        "Jeju Air",
        E2RArchetype.AVIATION_SAFETY_HARD_4C,
        (E2RArchetype.AIRLINE_SAFETY_HARD_4C, E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C),
        "4c_thesis_break",
        "hard_4C_aviation_safety",
        "r9l16_jeju_air_crash_T0",
        "hard_4C_aviation_safety",
        "4C",
        date(2024, 12, 29),
        None,
        None,
        None,
        date(2024, 12, 30),
        True,
        ("Muan_crash_179_fatalities", "Jeju_Air_minus_15_7pct", "market_cap_erased_95_7B_won", "B737_800_safety_inspection", "booking_cancellation_risk"),
        ("final_accident_report_missing", "compensation_cost_missing", "booking_recovery_missing", "safety_remediation_missing", "regulatory_penalty_missing"),
        None,
        -15.7,
        {"incident_date": "2024-12-29", "stock_reaction_date": "2024-12-30", "fatalities": 179, "survivors": 2, "aircraft_type": "Boeing_737-800", "airport": "Muan_International_Airport", "intraday_event_return_pct": -15.7, "market_cap_erased_krw_bn": 95.7, "record_low": True, "safety_inspection_scope": "all_Boeing_737-800_aircraft_in_South_Korea", "booking_cancellation_risk": True},
        "aligned",
        "hard_4C_success_aviation_safety",
        "thesis_break",
        "should_have_been_red",
        "Fatal crash, safety inspection and booking cancellations are hard aviation-safety 4C.",
    ),
    Round317CaseCandidate(
        "r9_loop16_china_tourism_leisure_transport",
        "034230/008770/069960/travel_airline_basket",
        "Paradise / Hotel Shilla / Hyundai Department Store / travel-airline basket",
        E2RArchetype.CHINA_TOURISM_LEISURE_STAGE2_EVENT,
        (E2RArchetype.TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE, E2RArchetype.CHINA_TOURISM_LEISURE_EVENT_PREMIUM),
        "event_premium",
        "Stage2_leisure_event_with_airline_margin_4B",
        "r9l16_china_tourism_leisure_T1",
        "Stage2_leisure_event_with_airline_margin_4B",
        "Stage2 event",
        date(2025, 8, 6),
        date(2025, 8, 6),
        None,
        date(2025, 8, 26),
        None,
        False,
        ("visa_free_entry_start_2025_09_29", "Hotel_Shilla_plus_4_8pct", "Paradise_plus_2_9pct", "Hyundai_Department_Store_plus_7_1pct", "flight_capacity_105pct_pre_pandemic"),
        ("actual_arrivals_missing", "casino_drop_amount_missing", "hotel_RevPAR_missing", "duty_free_margin_missing", "airline_yield_missing", "route_oversupply_4B"),
        7.1,
        None,
        {"announcement_date": "2025-08-06", "pilot_start_date": "2025-09-29", "pilot_end_date": "2026-06", "visa_free_stay_days": 15, "hyundai_department_store_event_return_pct": 7.1, "hotel_shilla_event_return_pct": 4.8, "paradise_event_return_pct": 2.9, "hankook_cosmetics_event_return_pct": 9.9, "china_korea_flight_capacity_vs_pre_pandemic_pct": 105},
        "aligned",
        "Stage2_leisure_event_not_Green",
        "event_premium",
        "stage2_watch_success",
        "Visa-free policy moves leisure names, but spending, hotel/casino/duty-free margin and airline yield are gates.",
    ),
    Round317CaseCandidate(
        "r9_loop16_hmm_red_sea_freight_beta",
        "011200",
        "HMM / container shipping read-through",
        E2RArchetype.CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B,
        (E2RArchetype.CONTAINER_FREIGHT_CYCLICAL_STAGE2_4B, E2RArchetype.RED_SEA_FREIGHT_CYCLE_4B_4C),
        "cyclical_success",
        "cyclical_freight_beta_with_4B_normalization",
        "r9l16_hmm_redsea_T0",
        "cyclical_Stage2_freight_beta_with_4B_normalization",
        "cyclical Stage2",
        date(2024, 7, 3),
        date(2024, 7, 3),
        None,
        date(2026, 2, 5),
        None,
        False,
        ("Red_Sea_rerouting", "global_vessel_capacity_tied_5_9pct", "Freightos_index_plus_40pct", "Maersk_minus_5_5pct_on_normalization"),
        ("direct_HMM_price_anchor_missing", "HMM_contract_freight_rates_missing", "spot_vs_contract_mix_missing", "fuel_cost_missing", "Suez_route_resumption_timing_missing"),
        40.0,
        -5.5,
        {"stage2_reference_date": "2024-07-03", "global_vessel_capacity_tied_pct": "5-9", "freightos_index_six_week_return_pct": 40, "red_sea_insurance_premium_context": "around_0.7pct_to_1pct_of_ship_value", "normalization_reference_date": "2026-02-05", "maersk_event_return_pct": -5.5, "direct_hmm_price_anchor": "price_data_unavailable_after_deep_search"},
        "unknown",
        "cyclical_freight_beta_not_Green",
        "cyclical_rerating",
        "stage2_watch_success",
        "Freight-rate spike is cyclical unless HMM contract-rate duration and route-normalization risk are resolved.",
    ),
)

ROUND317_TRIGGER_RECORDS: tuple[Round317TriggerRecord, ...] = (
    Round317TriggerRecord("r9l16_hyundai_hybrid_valueup_T1", "r9_loop16_hyundai_hybrid_valueup", "Stage2-Actionable", "2024-08-28", "Hyundai targets 5.55M 2030 global sales, doubles hybrid lineup, raises 2028 hybrid target to 1.33M, announces up to 4T won buyback and 35% profit return; shares close +4.7%.", 4.7, "excellent_stage2_actionable_hybrid_valueup", "Stage2-Actionable", {"buyback_krw_trn": 4, "hybrid_sales_target_2028_mn_units": 1.33}),
    Round317TriggerRecord("r9l16_hyundai_kia_tariff_T0", "r9_loop16_hyundai_kia_tariff_localization", "4C-watch_auto_tariff", "2025-03-26/2025-07-31", "U.S. auto tariff shock and later 15% tariff deal pressure Hyundai/Kia; Hyundai -4.5%, Kia -6.6% after 15% trade deal; tariff cost 4.1T won in 2025.", "Hyundai -4.5 / Kia -6.6", "auto_tariff_4C_watch", "4C-watch", {"trade_deal_auto_tariff_pct": 15, "hyundai_2025_tariff_cost_krw_trn": 4.1}),
    Round317TriggerRecord("r9l16_hyundai_kia_localization_T1", "r9_loop16_hyundai_kia_tariff_localization", "Stage2_localization_hedge", "2025-03-25", "Hyundai Group $21B U.S. investment and Hyundai Steel $5.8B Louisiana plant; Hyundai +7.5%, Kia +4.3% on expected sourcing/localization benefit.", "Hyundai +7.5 / Kia +4.3", "Stage2_tariff_hedge", "Stage2", {"hyundai_group_us_investment_usd_bn": 21, "hyundai_steel_capacity_mn_tons": 2.7}),
    Round317TriggerRecord("r9l16_hyundai_robotics_T2", "r9_loop16_hyundai_boston_dynamics_robotics", "Stage2_robotics_optionality", "2026-02-11", "Boston Dynamics CEO step-down fuels commercialization expectations; Hyundai +5.9%, Kia +4.6%; Atlas deployment/30,000 annual units target but labor 4B.", "Hyundai +5.9 / Kia +4.6", "Stage2_robotics_with_labor_4B", "Stage2+4B", {"atlas_annual_production_target_units": 30000}),
    Round317TriggerRecord("r9l16_hyundai_glovis_route_T0", "r9_loop16_hyundai_glovis_export_disruption", "4C-watch_logistics_disruption", "2026-04-03", "Hyundai warns exports to Europe/North Africa disrupted by Middle East conflict; Glovis cannot access some routes; Hyundai -1.2%, Glovis -0.7%, KOSPI +2.7%.", "Hyundai -1.2 / Glovis -0.7", "auto_export_logistics_4C_watch", "4C-watch", {"hyundai_market_relative_pp": -3.9}),
    Round317TriggerRecord("r9l16_korean_air_asiana_T1", "r9_loop16_korean_air_asiana_consolidation", "Stage2_airline_consolidation", "2024-12-12/2025-03-11", "Korean Air completes $1.3B Asiana takeover for 63.88% stake; Asiana subsidiary until 2027; Jin Air to absorb Air Busan/Air Seoul.", "price_data_unavailable_after_deep_search", "Stage2_airline_consolidation_not_Green", "Stage2", {"deal_value_usd_bn": 1.3, "stake_pct": 63.88}),
    Round317TriggerRecord("r9l16_jeju_air_crash_T0", "r9_loop16_jeju_air_crash_safety_4c", "hard_4C_aviation_safety", "2024-12-29/2024-12-30", "Jeju Air crash at Muan killed 179; shares plunged as much as 15.7% to record low, erasing 95.7B won market cap; B737-800 inspections ordered.", -15.7, "hard_4C_success_aviation_safety", "4C", {"fatalities": 179, "market_cap_erased_krw_bn": 95.7}),
    Round317TriggerRecord("r9l16_china_tourism_leisure_T1", "r9_loop16_china_tourism_leisure_transport", "Stage2_leisure_event", "2025-08-06/2025-09-29", "South Korea offers visa-free entry for Chinese tourist groups; Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%; airline route capacity already 105% of pre-pandemic.", "Hyundai Dept +7.1 / Hotel Shilla +4.8 / Paradise +2.9", "Stage2_leisure_event_with_airline_margin_4B", "Stage2", {"flight_capacity_vs_pre_pandemic_pct": 105}),
    Round317TriggerRecord("r9l16_hmm_redsea_T0", "r9_loop16_hmm_red_sea_freight_beta", "cyclical_Stage2_freight_beta", "2024-07-03/2026-02-05", "Red Sea rerouting ties up 5-9% global vessel capacity and Freightos index rises 40%; later Maersk warns overcapacity and route normalization could pressure 2026 earnings, shares -5.5%.", "HMM unavailable / Freightos +40 / Maersk -5.5", "cyclical_freight_beta_with_normalization_4B", "Stage2_cyclical+4B", {"freightos_index_six_week_return_pct": 40, "maersk_event_return_pct": -5.5}),
)

ROUND317_SHADOW_WEIGHT_ROWS: tuple[dict[str, str], ...] = (
    {"archetype": E2RArchetype.AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE.value, "hybrid_mix_margin_conversion": "+5", "shareholder_return_execution": "+4", "tariff_absorption_localization": "+2", "us_capacity_utilization": "+2", "robotics_commercialization": "+1", "logistics_route_resilience": "+1", "airline_safety_trust": "+1", "airline_integration_synergy": "+0", "tourism_spend_margin": "+0", "freight_rate_duration": "+0", "ev_headline_without_margin_penalty": "-4", "tariff_relief_without_savings_penalty": "-2", "robotics_hype_without_unit_economics_penalty": "-1", "localization_capex_without_roi_penalty": "-1", "stage2_actionable_promote": "hybrid/value-up event", "stage3_yellow_gate": "margin/tariff conversion pending", "stage3_green_gate": "hybrid mix+OP margin+buyback execution", "notes": "Hyundai investor day."},
    {"archetype": E2RArchetype.AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE.value, "hybrid_mix_margin_conversion": "+2", "shareholder_return_execution": "+1", "tariff_absorption_localization": "+5", "us_capacity_utilization": "+5", "robotics_commercialization": "+0", "logistics_route_resilience": "+3", "airline_safety_trust": "+1", "airline_integration_synergy": "+0", "tourism_spend_margin": "+0", "freight_rate_duration": "+0", "ev_headline_without_margin_penalty": "-2", "tariff_relief_without_savings_penalty": "-5", "robotics_hype_without_unit_economics_penalty": "-1", "localization_capex_without_roi_penalty": "-4", "stage2_actionable_promote": "tariff shock and localization hedge", "stage3_yellow_gate": "actual savings missing", "stage3_green_gate": "U.S. utilization+tariff savings", "notes": "Hyundai/Kia."},
    {"archetype": E2RArchetype.AUTO_ROBOTICS_OPTIONALITY_STAGE2_WITH_LABOR_4B.value, "hybrid_mix_margin_conversion": "+1", "shareholder_return_execution": "+0", "tariff_absorption_localization": "+1", "us_capacity_utilization": "+2", "robotics_commercialization": "+5", "logistics_route_resilience": "+1", "airline_safety_trust": "+1", "airline_integration_synergy": "+0", "tourism_spend_margin": "+0", "freight_rate_duration": "+0", "ev_headline_without_margin_penalty": "-1", "tariff_relief_without_savings_penalty": "-1", "robotics_hype_without_unit_economics_penalty": "-5", "localization_capex_without_roi_penalty": "-3", "stage2_actionable_promote": "robotics commercialization optionality", "stage3_yellow_gate": "unit economics/labor agreement missing", "stage3_green_gate": "productivity gain+external sales", "notes": "Hyundai/Boston Dynamics."},
    {"archetype": E2RArchetype.AUTO_EXPORT_LOGISTICS_DISRUPTION_4C_WATCH.value, "hybrid_mix_margin_conversion": "+0", "shareholder_return_execution": "+0", "tariff_absorption_localization": "+2", "us_capacity_utilization": "+1", "robotics_commercialization": "+0", "logistics_route_resilience": "+5", "airline_safety_trust": "+1", "airline_integration_synergy": "+0", "tourism_spend_margin": "+0", "freight_rate_duration": "+1", "ev_headline_without_margin_penalty": "-1", "tariff_relief_without_savings_penalty": "-1", "robotics_hype_without_unit_economics_penalty": "-1", "localization_capex_without_roi_penalty": "-1", "stage2_actionable_promote": "route disruption hits export margin", "stage3_yellow_gate": "route normalization missing", "stage3_green_gate": "N/A", "notes": "Hyundai/Glovis."},
    {"archetype": E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2_WITH_INTEGRATION_4B.value, "hybrid_mix_margin_conversion": "+0", "shareholder_return_execution": "+0", "tariff_absorption_localization": "+0", "us_capacity_utilization": "+0", "robotics_commercialization": "+0", "logistics_route_resilience": "+1", "airline_safety_trust": "+3", "airline_integration_synergy": "+5", "tourism_spend_margin": "+2", "freight_rate_duration": "+0", "ev_headline_without_margin_penalty": "-1", "tariff_relief_without_savings_penalty": "-1", "robotics_hype_without_unit_economics_penalty": "-1", "localization_capex_without_roi_penalty": "-1", "stage2_actionable_promote": "airline consolidation", "stage3_yellow_gate": "synergy/fare/labor gates missing", "stage3_green_gate": "route and LCC synergy", "notes": "Korean Air/Asiana."},
    {"archetype": E2RArchetype.AVIATION_SAFETY_HARD_4C.value, "hybrid_mix_margin_conversion": "+0", "shareholder_return_execution": "+0", "tariff_absorption_localization": "+0", "us_capacity_utilization": "+0", "robotics_commercialization": "+0", "logistics_route_resilience": "+1", "airline_safety_trust": "+5", "airline_integration_synergy": "+0", "tourism_spend_margin": "+1", "freight_rate_duration": "+0", "ev_headline_without_margin_penalty": "-1", "tariff_relief_without_savings_penalty": "-1", "robotics_hype_without_unit_economics_penalty": "-1", "localization_capex_without_roi_penalty": "-1", "stage2_actionable_promote": "fatal crash/safety trust", "stage3_yellow_gate": "remediation and booking recovery missing", "stage3_green_gate": "N/A", "notes": "Jeju Air."},
    {"archetype": E2RArchetype.CHINA_TOURISM_LEISURE_STAGE2_EVENT.value, "hybrid_mix_margin_conversion": "+0", "shareholder_return_execution": "+0", "tariff_absorption_localization": "+0", "us_capacity_utilization": "+0", "robotics_commercialization": "+0", "logistics_route_resilience": "+1", "airline_safety_trust": "+1", "airline_integration_synergy": "+0", "tourism_spend_margin": "+5", "freight_rate_duration": "+0", "ev_headline_without_margin_penalty": "-1", "tariff_relief_without_savings_penalty": "-1", "robotics_hype_without_unit_economics_penalty": "-1", "localization_capex_without_roi_penalty": "-1", "stage2_actionable_promote": "visa-free tourism event", "stage3_yellow_gate": "spending/yield missing", "stage3_green_gate": "arrivals+spending+margin", "notes": "Paradise/Hotel Shilla."},
    {"archetype": E2RArchetype.CONTAINER_SHIPPING_FREIGHT_BETA_STAGE2_WITH_NORMALIZATION_4B.value, "hybrid_mix_margin_conversion": "+0", "shareholder_return_execution": "+0", "tariff_absorption_localization": "+0", "us_capacity_utilization": "+0", "robotics_commercialization": "+0", "logistics_route_resilience": "+4", "airline_safety_trust": "+1", "airline_integration_synergy": "+0", "tourism_spend_margin": "+0", "freight_rate_duration": "+5", "ev_headline_without_margin_penalty": "-1", "tariff_relief_without_savings_penalty": "-1", "robotics_hype_without_unit_economics_penalty": "-1", "localization_capex_without_roi_penalty": "-1", "stage2_actionable_promote": "freight-rate spike", "stage3_yellow_gate": "contract duration/normalization missing", "stage3_green_gate": "contract rates+duration", "notes": "HMM/Red Sea."},
)


def round317_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND317_CASE_CANDIDATES]


def round317_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND317_CASE_CANDIDATES]


def round317_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND317_TRIGGER_RECORDS]


def round317_shadow_weight_rows() -> list[dict[str, str]]:
    return [dict(row) for row in ROUND317_SHADOW_WEIGHT_ROWS]


def round317_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND317_REQUIRED_TARGET_ALIASES.items()]


def round317_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND317_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND317_SCORE_DOWN_AXES]
    )


def round317_summary() -> dict[str, object]:
    return {
        "source_round": ROUND317_SOURCE_ROUND_PATH,
        "round_id": ROUND317_ANALYST_ROUND_ID,
        "large_sector": ROUND317_LARGE_SECTOR,
        "method": ROUND317_METHOD,
        "case_candidate_count": len(ROUND317_CASE_CANDIDATES),
        "trigger_count": len(ROUND317_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND317_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 4,
        "stage2_candidate_count": 6,
        "stage3_yellow_candidate_count": 6,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 6,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 1,
        "evidence_good_but_price_failed_or_unavailable_count": 2,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R10 Loop 16",
    }


def round317_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND317_SOURCE_ROUND_PATH,
        "round_id": ROUND317_ANALYST_ROUND_ID,
        "large_sector": ROUND317_LARGE_SECTOR,
        "method": ROUND317_METHOD,
        "summary": round317_summary(),
        "required_target_aliases": dict(ROUND317_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND317_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND317_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND317_STAGE3_GREEN_RULES,
        "green_blockers": ROUND317_GREEN_BLOCKERS,
        "score_up_axes": ROUND317_SCORE_UP_AXES,
        "score_down_axes": ROUND317_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND317_STAGE4B_WATCH_TRIGGERS,
        "stage4c_watch_gates": ROUND317_4C_WATCH_GATES,
        "row_separation_rules": ROUND317_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round317_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_hybrid_tariff_localization_robotics_airline_tourism_or_freight_headline_as_Green_without_margin_utilization_synergy_yield_or_contract_duration",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round317_summary_markdown() -> str:
    summary = round317_summary()
    lines = [
        "# R9 Loop 16 Mobility / Transport / Leisure Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: tourism visa-free policy can move Hotel Shilla or Paradise, but it is not Green until spending, RevPAR, casino drop and margin are visible.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Hyundai hybrid/value-up is the cleanest Stage2-Actionable case.",
            "- Hyundai/Kia tariff exposure is 4C-watch, while U.S. localization is only a Stage2 hedge until savings are proven.",
            "- Hyundai/Boston Dynamics robotics is Stage2 optionality with labor/capex 4B.",
            "- Hyundai/Glovis logistics disruption and Jeju Air safety crash are negative 4C paths.",
            "- Korean Air/Asiana consolidation, China tourism and HMM freight beta remain Stage2 until synergy, spending/yield or contract duration closes.",
            "- Stage3-Green confirmed: `0`.",
            "- Hard 4C confirmed: `1`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round317_trigger_grid_markdown() -> str:
    lines = [
        "# Round 317 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round317_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round317_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 317 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND317_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND317_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND317_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND317_GREEN_BLOCKERS),
            "",
            "## 4C Watch Gates",
            *_bullet_lines(ROUND317_4C_WATCH_GATES),
        ]
    ) + "\n"


def render_round317_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 317 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND317_STAGE4B_WATCH_TRIGGERS),
        "",
        "## 4C Watch Gates",
        *_bullet_lines(ROUND317_4C_WATCH_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND317_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round317_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 317 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND317_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round317_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 317 Row Separation Plan",
        "",
        "Case evidence, trigger anchors and full OHLC windows must be separate rows.",
        "",
        "Easy example: Red Sea freight spike is Stage2 cyclical evidence. It is not Green until contract rates and route-normalization risk are visible.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND317_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round317_r9_loop16_reports(
    output_directory: str | Path = ROUND317_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND317_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND317_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND317_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND317_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round317_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND317_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round317_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round317_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round317_r9_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round317_r9_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round317_r9_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round317_r9_loop16_trigger_grid.md",
        "summary": output_dir / "round317_r9_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round317_r9_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round317_r9_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round317_r9_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round317_r9_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round317_r9_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round317_r9_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round317_case_rows())
    _write_csv(paths["target_aliases"], round317_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round317_trigger_rows())
    _write_csv(paths["score_adjustments"], round317_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round317_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round317_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round317_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round317_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round317_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round317_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round317_row_separation_plan_markdown(), encoding="utf-8")
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
    "ROUND317_4C_WATCH_GATES",
    "ROUND317_CASE_CANDIDATES",
    "ROUND317_GREEN_BLOCKERS",
    "ROUND317_LARGE_SECTOR",
    "ROUND317_REQUIRED_TARGET_ALIASES",
    "ROUND317_ROW_SEPARATION_RULES",
    "ROUND317_SCORE_DOWN_AXES",
    "ROUND317_SCORE_UP_AXES",
    "ROUND317_SHADOW_WEIGHT_ROWS",
    "ROUND317_STAGE2_ACTIONABLE_RULES",
    "ROUND317_STAGE3_GREEN_RULES",
    "ROUND317_STAGE3_YELLOW_RULES",
    "ROUND317_STAGE4B_WATCH_TRIGGERS",
    "ROUND317_TRIGGER_RECORDS",
    "render_round317_stage4b_4c_review_markdown",
    "render_round317_stage_rules_markdown",
    "render_round317_trigger_grid_markdown",
    "round317_audit_payload",
    "round317_case_records",
    "round317_case_rows",
    "round317_shadow_weight_rows",
    "round317_summary",
    "round317_trigger_rows",
    "write_round317_r9_loop16_reports",
]
