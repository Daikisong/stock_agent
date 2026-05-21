"""Round-330 R9 Loop-17 mobility, transport and leisure validation.

This module converts ``docs/round/round_330.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a visa-free tourism headline can be Stage2 when hotel/casino/
department-store stocks react. It still cannot become Green until visitor
volume turns into basket size, occupancy and OP as of the replay date.
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


ROUND330_SOURCE_ROUND_PATH = "docs/round/round_330.md"
ROUND330_ANALYST_ROUND_ID = "round_258"
ROUND330_LOOP_NAME = "R9 Loop 17"
ROUND330_LARGE_SECTOR = "MOBILITY_TRANSPORT_LEISURE"
ROUND330_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND330_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round330_r9_loop17_mobility_transport_leisure_trigger_validation"
ROUND330_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r9_loop17_round258.jsonl"
ROUND330_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r9_loop17_round258.jsonl"
ROUND330_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round330_r9_loop17_mobility_transport_leisure_trigger_validation_audit.json"
ROUND330_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round258_r9_loop17_v1.csv"

ROUND330_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE": E2RArchetype.AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE.value,
    "AUTO_TARIFF_LOCALIZATION_4B": E2RArchetype.AUTO_TARIFF_LOCALIZATION_4B.value,
    "MOBILITY_ROBOTICS_AI_FACTORY_STAGE2_OVERHEAT": E2RArchetype.MOBILITY_ROBOTICS_AI_FACTORY_STAGE2_OVERHEAT.value,
    "AIRLINE_CONSOLIDATION_STAGE2_NO_PRICE": E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2_NO_PRICE.value,
    "LCC_SAFETY_TRUST_HARD_4C": E2RArchetype.LCC_SAFETY_TRUST_HARD_4C.value,
    "CHINA_TOURISM_LEISURE_STAGE2_ACTIONABLE": E2RArchetype.CHINA_TOURISM_LEISURE_STAGE2_ACTIONABLE.value,
    "MARINE_AFTERMARKET_IPO_STAGE2_ACTIONABLE": E2RArchetype.MARINE_AFTERMARKET_IPO_STAGE2_ACTIONABLE.value,
    "SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE": E2RArchetype.SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE.value,
}

ROUND330_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_at_least_5pct_or_clear_reported_positive_price_anchor",
    "hybrid_production_capacity_route_visitor_or_shipping_demand_is_specific",
    "buyback_dividend_IPO_merger_or_deal_value_is_numeric",
    "margin_path_connects_to_hybrid_mix_yield_load_factor_retrofit_or_contract_backlog",
    "tariff_safety_fuel_FX_capex_or_cycle_4B_is_identified",
    "price_reaction_aligns_with_evidence",
    "repeat_revenue_or_profit_path_exists",
)

ROUND330_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "hybrid_sales_margin_and_US_localization_cost_are_confirmed",
    "buyback_or_dividend_execution_continues",
    "robotics_deployment_creates_productivity_or_revenue_signal",
    "airline_consolidation_produces_yield_cost_or_load_factor_improvement",
    "tourism_visitor_volume_converts_into_basket_size_and_OP",
    "marine_aftermarket_demand_produces_recurring_margin",
    "shipbuilding_merger_converts_into_US_naval_or_icebreaker_contracts",
    "safety_trust_4C_is_contained_and_bookings_recover",
)

ROUND330_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "Stage2_trigger_converts_into_recurring_EPS_OP_or_FCF",
    "tariff_fuel_FX_capex_safety_4B_is_reduced",
    "transportation_demand_shows_volume_and_yield",
    "robotics_AI_optionality_becomes_measurable_productivity_or_revenue",
    "IPO_or_merger_execution_proves_margin_and_backlog",
    "full_window_MFE_MAE_is_favorable",
)

ROUND330_GREEN_BLOCKERS: tuple[str, ...] = (
    "auto_growth_without_tariff_adjustment",
    "robotics_AI_without_revenue_or_productivity",
    "airline_merger_without_synergy_yield_or_load_factor",
    "tourism_headline_without_basket_size_and_OP",
    "marine_IPO_without_cycle_or_overhang_adjustment",
    "shipbuilding_merger_without_US_naval_or_icebreaker_contract",
    "safety_event_ignored",
    "localization_without_execution",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND330_SCORE_UP_AXES: tuple[str, ...] = (
    "hybrid_mix_margin",
    "shareholder_return_auto",
    "robotics_AI_mobility_optionality",
    "airline_consolidation_synergy",
    "safety_trust_risk",
    "inbound_tourism_policy",
    "marine_aftermarket_demand",
    "shipbuilding_US_naval_demand",
)

ROUND330_SCORE_DOWN_AXES: tuple[str, ...] = (
    "auto_growth_without_tariff_adjustment_penalty",
    "robotics_AI_without_revenue_penalty",
    "airline_merger_without_synergy_penalty",
    "tourism_headline_without_basket_size_penalty",
    "IPO_without_cycle_risk_penalty",
    "shipbuilding_merger_without_contract_penalty",
    "safety_event_ignored_penalty",
    "localization_without_execution_penalty",
)

ROUND330_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "US_auto_tariff_reset",
    "hybrid_strategy_without_actual_margin",
    "robotics_AI_capex_without_revenue",
    "airline_merger_without_synergy",
    "fuel_or_FX_shock",
    "tourism_policy_without_basket_size",
    "shipping_IPO_or_merger_cycle_overheat",
    "fatal_safety_accident_inspection_cancellation",
)

ROUND330_HARD_4C_GATES: tuple[str, ...] = (
    "fatal_safety_accident_with_stock_crash_and_system_wide_inspection",
    "regulatory_grounding_or_flight_suspension",
    "large_compensation_and_booking_collapse",
    "production_plant_shutdown_from_legal_or_safety_event",
    "tariff_shock_causing_structural_export_margin_break",
    "merger_failure_after_consolidation_premium",
)

ROUND330_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_reported_event_anchor_tariff_deal_IPO_merger_safety_or_tourism_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
    "do_not_treat_auto_tourism_airline_IPO_or_shipbuilding_headline_as_Green_without_margin_yield_basket_contract_productivity_or_price_path",
)


@dataclass(frozen=True)
class Round330TriggerRecord:
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
class Round330ShadowWeightRow:
    archetype: E2RArchetype
    hybrid_mix_margin: int
    shareholder_return_auto: int
    robotics_ai_mobility_optionality: int
    airline_consolidation_synergy: int
    safety_trust_risk: int
    inbound_tourism_policy: int
    marine_aftermarket_demand: int
    shipbuilding_us_naval_demand: int
    auto_growth_without_tariff_adjustment_penalty: int
    robotics_ai_without_revenue_penalty: int
    airline_merger_without_synergy_penalty: int
    tourism_headline_without_basket_size_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "hybrid_mix_margin": _signed(self.hybrid_mix_margin),
            "shareholder_return_auto": _signed(self.shareholder_return_auto),
            "robotics_AI_mobility_optionality": _signed(self.robotics_ai_mobility_optionality),
            "airline_consolidation_synergy": _signed(self.airline_consolidation_synergy),
            "safety_trust_risk": _signed(self.safety_trust_risk),
            "inbound_tourism_policy": _signed(self.inbound_tourism_policy),
            "marine_aftermarket_demand": _signed(self.marine_aftermarket_demand),
            "shipbuilding_US_naval_demand": _signed(self.shipbuilding_us_naval_demand),
            "auto_growth_without_tariff_adjustment_penalty": _signed(self.auto_growth_without_tariff_adjustment_penalty),
            "robotics_AI_without_revenue_penalty": _signed(self.robotics_ai_without_revenue_penalty),
            "airline_merger_without_synergy_penalty": _signed(self.airline_merger_without_synergy_penalty),
            "tourism_headline_without_basket_size_penalty": _signed(self.tourism_headline_without_basket_size_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round330CaseCandidate:
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
            "do_not_use_round330_cases_as_candidate_generation_input",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_auto_tourism_airline_IPO_or_shipbuilding_headline_as_Green_without_margin_yield_basket_contract_productivity_or_price_path",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")

        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "tariff" in field
            or "capex" in field
            or "cycle" in field
            or "overhang" in field
            or "synergy" in field
            or "basket" in field
            or "contract" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "fatal" in field
            or "safety" in field
            or "crash" in field
            or "booking" in field
            or "cancellation" in field
            or "market_cap_wiped" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND330_LARGE_SECTOR,
            large_sector=ROUND330_LARGE_SECTOR,
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
            must_have_fields=ROUND330_STAGE3_GREEN_RULES,
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
            price_validation=PriceValidation(price_validation_status="price_data_unavailable_after_deep_search"),
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
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND330_CASE_CANDIDATES: tuple[Round330CaseCandidate, ...] = (
    Round330CaseCandidate(
        "r9_loop17_hyundai_hybrid_valueup",
        "005380",
        "Hyundai Motor",
        E2RArchetype.AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE,
        (E2RArchetype.AUTO_HYBRID_SHAREHOLDER_RETURN, E2RArchetype.HYBRID_MIX_SHAREHOLDER_RETURN_STAGE2_YELLOW),
        "success_candidate",
        "Stage2_Actionable_auto_hybrid_valueup",
        "r9l17_hyundai_hybrid_T1",
        "Stage2-Actionable_auto_hybrid_valueup",
        "Stage2-Actionable",
        date(2024, 8, 28),
        date(2024, 8, 28),
        None,
        None,
        None,
        False,
        ("2030_sales_target_5_55M_units", "sales_growth_vs_2023_30pct", "hybrid_target_1_33M_by_2028", "hybrid_target_raise_40pct", "buyback_2025_2027_krw_4T", "shareholder_return_ratio_35pct", "close_plus_4_7pct"),
        ("US_tariff_localization_4B", "hybrid_margin_confirmation_missing", "Georgia_localization_cost_4B", "China_weakness_4B", "full_OHLC_MFE_MAE_missing"),
        {"trigger_date": "2024-08-28", "global_sales_target_2030_mn_units": 5.55, "sales_growth_vs_2023_pct": 30, "hybrid_sales_target_2028_mn_units": 1.33, "hybrid_target_raise_pct": 40, "buyback_2025_2027_krw_trn": 4.0, "shareholder_return_ratio_pct": 35, "event_return_intraday_pct": 5.0, "event_return_close_pct": 4.7},
        "aligned",
        "excellent_stage2_actionable_hybrid_valueup",
        "policy_event_rerating",
        "stage2_watch_success",
        "Hybrid strategy and shareholder return aligned with price reaction; tariff/localization and margin remain gates.",
    ),
    Round330CaseCandidate(
        "r9_loop17_hyundai_kia_us_auto_tariff",
        "005380/000270/012330",
        "Hyundai Motor / Kia / Hyundai Mobis",
        E2RArchetype.AUTO_TARIFF_LOCALIZATION_4B,
        (E2RArchetype.AUTO_TARIFF_LOCALIZATION, E2RArchetype.AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE),
        "4b_watch",
        "4B_auto_tariff_localization_risk",
        "r9l17_auto_tariff_T0",
        "4B_auto_tariff_margin_reset",
        "4B-watch",
        date(2025, 7, 31),
        None,
        None,
        date(2025, 7, 31),
        None,
        False,
        ("US_Korea_trade_deal_auto_tariff_15pct", "Hyundai_minus_4_5pct", "Kia_minus_6_6pct", "lost_2_5pct_tariff_advantage_vs_Japan", "tariff_uncertainty_partly_reduced"),
        ("margin_reset_4B", "localization_cost_4B", "tariff_finality_still_pending", "US_capacity_mix_4B", "supplier_pass_through_4B"),
        {"trigger_date": "2025-07-31", "us_auto_tariff_rate_pct": 15, "hyundai_event_return_pct": -4.5, "kia_event_return_pct": -6.6, "lost_tariff_advantage_vs_japan_pct": 2.5, "relief_trigger_date": "2026-01-27", "hyundai_early_drop_pct": -4.8, "hyundai_relief_return_pct": 1.1, "kia_early_drop_pct": -6.0, "kia_relief_return_pct": -1.0},
        "aligned",
        "tariff_4B_not_hard_4C",
        "no_rerating",
        "should_have_been_red",
        "Tariff reset remains a margin 4B, not a hard 4C while localization and negotiated rate remain manageable.",
    ),
    Round330CaseCandidate(
        "r9_loop17_hyundai_kia_robotics_ai_factory",
        "005380/000270",
        "Hyundai Motor / Kia / Boston Dynamics",
        E2RArchetype.MOBILITY_ROBOTICS_AI_FACTORY_STAGE2_OVERHEAT,
        (E2RArchetype.AUTO_ROBOTICS_OPTIONALITY_STAGE2_WITH_LABOR_4B, E2RArchetype.FUTURE_MOBILITY_AI_ROBOTICS_CAPEX),
        "success_candidate",
        "Stage2_mobility_robotics_AI_factory_overheat",
        "r9l17_hyundai_robotics_T2",
        "Stage2_robotics_AI_mobility_overheat",
        "Stage2 overheat / Yellow candidate",
        date(2026, 2, 11),
        date(2026, 2, 25),
        None,
        date(2026, 2, 25),
        None,
        False,
        ("Saemangeum_investment_krw_10T", "Saemangeum_investment_usd_7B", "Hyundai_plus_10_5pct", "Kia_plus_15pct", "robotics_AI_data_center_hydrogen", "Boston_Dynamics", "robot_capacity_target_30000_units_2028"),
        ("capex_ROI_missing_4B", "robot_revenue_missing", "productivity_missing", "AI_chip_depreciation_4B", "policy_location_risk_4B"),
        {"ceo_change_trigger_date": "2026-02-11", "hyundai_ceo_change_event_return_pct": 5.9, "kia_ceo_change_event_return_pct": 4.6, "saemangeum_trigger_date": "2026-02-25", "saemangeum_investment_krw_trn": 10, "saemangeum_investment_usd_bn": 7, "hyundai_saemangeum_event_return_pct": 10.5, "kia_saemangeum_event_return_pct": 15, "robot_capacity_target_annual_units_2028": 30000},
        "aligned",
        "Stage2_robotics_AI_optional_overheat_not_Green",
        "event_premium",
        "stage2_watch_success",
        "Robotics/AI optionality moved stocks, but commercialization, productivity and capex ROI are missing.",
    ),
    Round330CaseCandidate(
        "r9_loop17_korean_air_asiana_consolidation",
        "003490/020560/180640/089590",
        "Korean Air / Asiana / Jin Air / Air Busan",
        E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2_NO_PRICE,
        (E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2, E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2_WITH_INTEGRATION_4B),
        "success_candidate",
        "Stage2_airline_consolidation_no_direct_price",
        "r9l17_korean_air_asiana_T1",
        "Stage2_airline_consolidation_no_price",
        "Stage2",
        date(2024, 12, 12),
        date(2024, 12, 12),
        None,
        date(2024, 12, 12),
        None,
        False,
        ("deal_value_usd_1_3B", "Asiana_stake_63_88pct", "world_12th_by_international_capacity", "full_integration_target_2027", "Jin_Air_LCC_integration"),
        ("route_remedies_4B", "mileage_integration_4B", "labor_integration_4B", "fuel_FX_4B", "fare_cap_scrutiny_4B", "direct_price_unavailable"),
        {"completion_date": "2024-12-12", "deal_value_usd_bn": 1.3, "korean_air_asiana_stake_pct": 63.88, "global_capacity_rank_context": 12, "full_integration_target": 2027, "lcc_integration": "Jin_Air_to_absorb_Air_Busan_Air_Seoul", "direct_price_anchor": "price_data_unavailable_after_deep_search"},
        "unknown",
        "Stage2_airline_consolidation_no_price",
        "unknown",
        "stage2_watch_success",
        "Airline consolidation is structural, but synergy/yield/load-factor and direct stock-price validation are missing.",
    ),
    Round330CaseCandidate(
        "r9_loop17_jeju_air_crash_hard_4c",
        "089590",
        "Jeju Air",
        E2RArchetype.LCC_SAFETY_TRUST_HARD_4C,
        (E2RArchetype.AVIATION_SAFETY_HARD_4C, E2RArchetype.AIRLINE_SAFETY_HARD_4C),
        "4c_thesis_break",
        "hard_4C_LCC_safety_trust_break",
        "r9l17_jeju_air_crash_T0",
        "hard_4C_airline_safety_trust_break",
        "4C",
        date(2024, 12, 30),
        None,
        None,
        None,
        date(2024, 12, 30),
        True,
        ("fatalities_179", "intraday_minus_15_7pct", "record_low", "market_cap_wiped_krw_95_7B", "system_wide_airline_safety_inspection", "B737_800_review", "booking_cancellations"),
        ("compensation_finality_required_4C", "booking_recovery_required_4C", "load_factor_recovery_required_4C", "safety_audit_completion_required_4C", "brand_trust_repair_required_4C"),
        {"trigger_date": "2024-12-30", "fatalities": 179, "intraday_event_return_pct": -15.7, "market_cap_wiped_krw_bn": 95.7, "price_context": "record_low", "regulatory_response": ["system_wide_airline_safety_inspection", "Boeing_737_800_review", "Jeju_Air_safety_rating_review"]},
        "aligned",
        "hard_4C_success_airline_safety",
        "thesis_break",
        "should_have_been_red",
        "Fatal crash, record-low stock reaction, market cap wipeout and system-wide safety inspection confirm hard 4C.",
    ),
    Round330CaseCandidate(
        "r9_loop17_china_visa_free_leisure_basket",
        "008770/034230/069960/123690/travel_basket",
        "Hotel Shilla / Paradise / Hyundai Department Store / Hankook Cosmetics",
        E2RArchetype.CHINA_TOURISM_LEISURE_STAGE2_ACTIONABLE,
        (E2RArchetype.CHINA_TOURISM_LEISURE_STAGE2_EVENT, E2RArchetype.TOURISM_VISA_WAIVER_STAGE2_ACTIONABLE),
        "success_candidate",
        "Stage2_Actionable_leisure_inbound_tourism",
        "r9l17_china_leisure_T1",
        "Stage2-Actionable_inbound_leisure_policy",
        "Stage2-Actionable",
        date(2025, 8, 6),
        date(2025, 8, 6),
        None,
        date(2025, 8, 6),
        None,
        False,
        ("visa_free_period_2025_09_29_to_2026_06", "Hyundai_Department_Store_plus_7_1pct", "Hotel_Shilla_plus_4_8pct", "Paradise_plus_2_9pct", "Hankook_Cosmetics_plus_9_9pct", "Chinese_tour_groups_3_plus_can_stay_15_days"),
        ("temporary_policy_window_4B", "low_spend_tourism_4B", "geopolitical_protest_4B", "basket_size_missing", "OP_conversion_missing"),
        {"trigger_date": "2025-08-06", "visa_free_period": "2025-09-29_to_2026-06", "hyundai_department_store_event_return_pct": 7.1, "hotel_shilla_event_return_pct": 4.8, "paradise_event_return_pct": 2.9, "hankook_cosmetics_event_return_pct": 9.9, "pilot_rule": "Chinese_tour_groups_3_or_more_can_stay_15_days"},
        "aligned",
        "excellent_stage2_actionable_inbound_leisure",
        "event_premium",
        "stage2_watch_success",
        "Policy and leisure stock reaction aligned; basket size and OP conversion remain gates.",
    ),
    Round330CaseCandidate(
        "r9_loop17_hd_hyundai_marine_solution_ipo",
        "443060",
        "HD Hyundai Marine Solution",
        E2RArchetype.MARINE_AFTERMARKET_IPO_STAGE2_ACTIONABLE,
        (E2RArchetype.MARINE_MRO_RECURRING_SERVICE, E2RArchetype.SHIP_MRO_RECURRING_PLATFORM),
        "success_candidate",
        "Stage2_Actionable_marine_aftermarket_IPO",
        "r9l17_hd_hyundai_marine_ipo_T1",
        "Stage2-Actionable_marine_aftermarket_IPO",
        "Stage2-Actionable",
        date(2024, 5, 8),
        date(2024, 5, 8),
        None,
        date(2024, 5, 8),
        None,
        False,
        ("issue_price_krw_83400", "debut_open_price_krw_119900", "early_trading_plus_44pct", "close_price_krw_163900", "close_plus_97pct", "ipo_raise_krw_742_26B", "ipo_raise_usd_546M", "ship_repair_after_sales_retrofit_green_vessel_servicing"),
        ("KKR_overhang_4B", "valuation_4B", "shipping_cycle_4B", "parent_control_4B", "recurring_margin_missing"),
        {"ipo_date": "2024-05-08", "issue_price_krw": 83400, "debut_open_price_krw": 119900, "early_trading_return_pct": 44, "close_price_krw": 163900, "close_return_pct": 97, "ipo_raise_krw_bn": 742.26, "ipo_raise_usd_mn": 546, "market_cap_close_krw_trn": 7.29},
        "aligned",
        "excellent_stage2_actionable_marine_aftermarket_IPO",
        "event_premium",
        "stage2_watch_success",
        "IPO and aftermarket demand price reaction aligned; shipping cycle and KKR overhang remain 4B.",
    ),
    Round330CaseCandidate(
        "r9_loop17_hd_hyundai_heavy_mipo_masga_merger",
        "329180/010620",
        "HD Hyundai Heavy Industries / HD Hyundai Mipo",
        E2RArchetype.SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE,
        (E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG, E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG),
        "success_candidate",
        "Stage2_Actionable_shipbuilding_transport_infra_merger",
        "r9l17_hd_hyundai_mipo_merger_T1",
        "Stage2-Actionable_shipbuilding_transport_infra_merger",
        "Stage2-Actionable",
        date(2025, 8, 27),
        date(2025, 8, 27),
        None,
        date(2025, 8, 27),
        None,
        False,
        ("HD_Hyundai_Heavy_plus_11_3pct", "HD_Hyundai_Mipo_plus_14_6pct", "both_record_highs", "share_exchange_ratio_1_04059146", "merger_launch_target_2025_12", "MASGA_US_Korea_shipbuilding_cooperation", "naval_icebreaker_K_defense_logic"),
        ("merger_execution_4B", "US_contract_conversion_missing", "valuation_exchange_ratio_dispute_4B", "defense_cycle_risk_4B", "backlog_margin_missing"),
        {"trigger_date": "2025-08-27", "hd_hyundai_heavy_event_return_pct": 11.3, "hd_hyundai_mipo_event_return_pct": 14.6, "price_context": "both_record_highs", "share_exchange_ratio": "1_Mipo_share_for_1.04059146_HD_Hyundai_Heavy_shares", "merger_launch_target": "2025-12", "strategic_logic": ["MASGA", "US_Korea_shipbuilding_cooperation", "naval_vessel_demand", "icebreaker_demand", "K_defence_shipbuilding"]},
        "aligned",
        "excellent_stage2_actionable_shipbuilding_merger",
        "event_premium",
        "stage2_watch_success",
        "MASGA/U.S.-Korea shipbuilding trigger aligned with stock reaction; actual contract and merger execution are Yellow gates.",
    ),
)

ROUND330_TRIGGER_RECORDS: tuple[Round330TriggerRecord, ...] = (
    Round330TriggerRecord("r9l17_hyundai_hybrid_T1", "r9_loop17_hyundai_hybrid_valueup", "Stage2-Actionable_auto_hybrid_valueup", "2024-08-28", "2030 sales, hybrid target raise, buyback and shareholder-return ratio were public.", 4.7, "excellent_stage2_actionable_hybrid_valueup", "Stage2-Actionable", {"event_return_intraday_pct": 5.0, "buyback_2025_2027_krw_trn": 4.0}),
    Round330TriggerRecord("r9l17_auto_tariff_T0", "r9_loop17_hyundai_kia_us_auto_tariff", "4B_auto_tariff_margin_reset", "2025-07-31", "U.S.-Korea trade deal sets 15% auto import tariff and removes Korea tariff edge.", "Hyundai_-4.5_Kia_-6.6", "auto_tariff_4B", "4B-watch", {"us_auto_tariff_rate_pct": 15, "lost_tariff_advantage_vs_japan_pct": 2.5}),
    Round330TriggerRecord("r9l17_hyundai_robotics_T2", "r9_loop17_hyundai_kia_robotics_ai_factory", "Stage2_robotics_AI_mobility_overheat", "2026-02-25", "Saemangeum robotics, AI data-center and hydrogen investment reports.", "Hyundai_+10.5_Kia_+15", "Stage2_robotics_AI_optional_overheat", "Stage2_promote_candidate", {"saemangeum_investment_krw_trn": 10, "saemangeum_investment_usd_bn": 7}),
    Round330TriggerRecord("r9l17_korean_air_asiana_T1", "r9_loop17_korean_air_asiana_consolidation", "Stage2_airline_consolidation_no_price", "2024-12-12", "Korean Air completed Asiana acquisition and LCC integration plan was visible.", "price_data_unavailable_after_deep_search", "airline_consolidation_stage2_no_price", "Stage2", {"deal_value_usd_bn": 1.3, "korean_air_asiana_stake_pct": 63.88}),
    Round330TriggerRecord("r9l17_jeju_air_crash_T0", "r9_loop17_jeju_air_crash_hard_4c", "hard_4C_airline_safety_trust_break", "2024-12-30", "Fatal crash, record-low price reaction, market-cap wipeout and safety inspection.", -15.7, "hard_4C_success_airline_safety", "4C", {"fatalities": 179, "market_cap_wiped_krw_bn": 95.7}),
    Round330TriggerRecord("r9l17_china_leisure_T1", "r9_loop17_china_visa_free_leisure_basket", "Stage2-Actionable_inbound_leisure_policy", "2025-08-06", "Visa-free Chinese group-tour policy drove department-store/hotel/casino/cosmetics basket.", "HyundaiDept_+7.1_HotelShilla_+4.8_Paradise_+2.9_HankookCosmetics_+9.9", "excellent_stage2_actionable_inbound_leisure", "Stage2-Actionable", {"hyundai_department_store_event_return_pct": 7.1, "hotel_shilla_event_return_pct": 4.8, "paradise_event_return_pct": 2.9, "hankook_cosmetics_event_return_pct": 9.9}),
    Round330TriggerRecord("r9l17_hd_hyundai_marine_ipo_T1", "r9_loop17_hd_hyundai_marine_solution_ipo", "Stage2-Actionable_marine_aftermarket_IPO", "2024-05-08", "HD Hyundai Marine IPO opened sharply higher and closed at 163,900 won.", 97, "excellent_stage2_actionable_marine_aftermarket_IPO", "Stage2-Actionable", {"entry_price_krw": 163900, "issue_price_krw": 83400, "ipo_raise_krw_bn": 742.26}),
    Round330TriggerRecord("r9l17_hd_hyundai_mipo_merger_T1", "r9_loop17_hd_hyundai_heavy_mipo_masga_merger", "Stage2-Actionable_shipbuilding_transport_infra_merger", "2025-08-27", "HD Hyundai Heavy/Mipo merger targets U.S.-Korea shipbuilding cooperation and MASGA.", "HDHeavy_+11.3_Mipo_+14.6", "excellent_stage2_actionable_shipbuilding_merger", "Stage2-Actionable", {"hd_hyundai_heavy_event_return_pct": 11.3, "hd_hyundai_mipo_event_return_pct": 14.6}),
)

ROUND330_SHADOW_WEIGHT_ROWS: tuple[Round330ShadowWeightRow, ...] = (
    Round330ShadowWeightRow(E2RArchetype.AUTO_HYBRID_VALUEUP_STAGE2_ACTIONABLE, 5, 5, 1, 0, 1, 0, 0, 0, -5, -1, -1, -1, "Hyundai hybrid+buyback +4.7%", "tariff/localization margin gate", "hybrid margin+buyback execution", "Hyundai."),
    Round330ShadowWeightRow(E2RArchetype.AUTO_TARIFF_LOCALIZATION_4B, 1, 0, 0, 0, 1, 0, 0, 0, -5, -1, -1, -1, "U.S. tariff hits Hyundai/Kia", "negative 4B", "tariff relief+localized margin", "Hyundai/Kia."),
    Round330ShadowWeightRow(E2RArchetype.MOBILITY_ROBOTICS_AI_FACTORY_STAGE2_OVERHEAT, 1, 1, 5, 0, 1, 0, 0, 0, -1, -5, -1, -1, "Hyundai/Kia robotics AI rally", "capex/revenue missing", "robot deployment+productivity", "Hyundai/Kia."),
    Round330ShadowWeightRow(E2RArchetype.AIRLINE_CONSOLIDATION_STAGE2_NO_PRICE, 0, 0, 0, 5, 3, 2, 0, 0, -1, -1, -5, -1, "Korean Air/Asiana consolidation", "price unavailable", "route yield+cost synergy", "Korean Air."),
    Round330ShadowWeightRow(E2RArchetype.LCC_SAFETY_TRUST_HARD_4C, 0, 0, 0, 0, 5, 0, 0, 0, -1, -1, -1, -1, "Jeju Air fatal crash hard 4C", "recovery missing", "safety audit+booking recovery", "Jeju Air."),
    Round330ShadowWeightRow(E2RArchetype.CHINA_TOURISM_LEISURE_STAGE2_ACTIONABLE, 0, 0, 0, 1, 1, 5, 0, 0, -1, -1, -1, -5, "visa-free tourism leisure rally", "basket/OP gate", "visitor+basket+OP", "Hotel Shilla/Paradise."),
    Round330ShadowWeightRow(E2RArchetype.MARINE_AFTERMARKET_IPO_STAGE2_ACTIONABLE, 0, 0, 0, 0, 0, 0, 5, 2, -1, -1, -1, -1, "HD Hyundai Marine IPO +97%", "cycle/overhang", "recurring retrofit margin", "HD Hyundai Marine."),
    Round330ShadowWeightRow(E2RArchetype.SHIPBUILDING_MERGER_US_NAVAL_STAGE2_ACTIONABLE, 0, 0, 0, 1, 0, 0, 1, 5, -1, -1, -2, -1, "HD Heavy/Mipo MASGA merger", "contract/execution gate", "U.S. naval contracts+merger execution", "HD Hyundai Heavy/Mipo."),
)


def round330_case_records() -> tuple[E2RCaseRecord, ...]:
    records = tuple(candidate.to_case_record() for candidate in ROUND330_CASE_CANDIDATES)
    for record in records:
        record.validate()
    return records


def round330_case_rows() -> list[dict[str, str]]:
    return [candidate.as_row() for candidate in ROUND330_CASE_CANDIDATES]


def round330_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND330_TRIGGER_RECORDS]


def round330_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND330_SHADOW_WEIGHT_ROWS]


def round330_summary() -> dict[str, object]:
    return {
        "source_round": ROUND330_SOURCE_ROUND_PATH,
        "round_id": ROUND330_ANALYST_ROUND_ID,
        "loop_name": ROUND330_LOOP_NAME,
        "large_sector": ROUND330_LARGE_SECTOR,
        "method": ROUND330_METHOD,
        "case_candidate_count": len(ROUND330_CASE_CANDIDATES),
        "trigger_count": len(ROUND330_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND330_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": sum(1 for case in ROUND330_CASE_CANDIDATES if "Actionable" in case.stage_candidate),
        "stage2_candidate_count": sum(1 for case in ROUND330_CASE_CANDIDATES if "Stage2" in case.stage_candidate),
        "stage3_yellow_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": sum(1 for case in ROUND330_CASE_CANDIDATES if case.stage4b_date is not None),
        "hard_4c_case_count": sum(1 for case in ROUND330_CASE_CANDIDATES if case.hard_4c_confirmed),
        "price_unavailable_count": sum(1 for case in ROUND330_CASE_CANDIDATES if case.score_price_alignment == "unknown"),
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R10 Loop 17",
    }


def round330_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND330_SOURCE_ROUND_PATH,
        "round_id": ROUND330_ANALYST_ROUND_ID,
        "large_sector": ROUND330_LARGE_SECTOR,
        "method": ROUND330_METHOD,
        "summary": round330_summary(),
        "target_archetypes": dict(ROUND330_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND330_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND330_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND330_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND330_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND330_SCORE_UP_AXES),
        "score_down_axes": list(ROUND330_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND330_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND330_HARD_4C_GATES),
        "row_separation_rules": list(ROUND330_ROW_SEPARATION_RULES),
        "shadow_weights": round330_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_change_production_scoring",
            "do_not_use_round330_cases_as_candidate_generation_input",
            "do_not_force_Stage3_Green",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_auto_tourism_airline_IPO_or_shipbuilding_headline_as_Green_without_margin_yield_basket_contract_productivity_or_price_path",
        ],
    }


def render_round330_summary_markdown() -> str:
    summary = round330_summary()
    lines = [
        "# Round 330 R9 Loop 17 Mobility Transport Leisure Trigger Validation",
        "",
        f"- source_round: `{ROUND330_SOURCE_ROUND_PATH}`",
        f"- analyst_round_id: `{ROUND330_ANALYST_ROUND_ID}`",
        f"- large_sector: `{ROUND330_LARGE_SECTOR}`",
        f"- method: `{ROUND330_METHOD}`",
        f"- case candidates: `{summary['case_candidate_count']}`",
        f"- triggers: `{summary['trigger_count']}`",
        f"- Stage2-Actionable candidates: `{summary['stage2_actionable_candidate_count']}`",
        f"- Stage2 candidates: `{summary['stage2_candidate_count']}`",
        f"- Stage3-Green confirmed: `{summary['stage3_green_confirmed_count']}`",
        "- production_scoring_changed: `false`",
        "- candidate_generation_input: `false`",
        "- shadow_weight_only: `true`",
        "",
        "## 핵심 결론",
        "",
        "- Hyundai hybrid/value-up은 R9 auto의 가장 좋은 Stage2-Actionable이다. 그래도 tariff/localization margin gate가 남아 있다.",
        "- Hyundai/Kia tariff는 4B다. 15% 관세는 불확실성을 줄였지만 export-margin edge를 재설정한다.",
        "- Hyundai/Kia robotics AI는 Stage2 overheat / Yellow 후보이다. robot revenue, productivity and capex ROI가 필요하다.",
        "- Korean Air/Asiana는 Stage2 consolidation no-price다. synergy, yield, load factor와 직접 가격 anchor가 필요하다.",
        "- Jeju Air fatal crash는 hard 4C다. safety/trust break는 성장 논리를 끊는다.",
        "- China tourism, HD Hyundai Marine IPO, HD Hyundai Heavy/Mipo merger는 Stage2-Actionable이지만 basket/OP, recurring margin, actual contracts가 Yellow gate다.",
    ]
    return "\n".join(lines) + "\n"


def render_round330_trigger_grid_markdown() -> str:
    lines = [
        "# Round 330 R9 Loop 17 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | date | event_return | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round330_trigger_rows():
        lines.append(
            f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |"
        )
    return "\n".join(lines) + "\n"


def render_round330_stage_rules_markdown() -> str:
    sections = [
        ("Stage2-Actionable Rules", ROUND330_STAGE2_ACTIONABLE_RULES),
        ("Stage3-Yellow Rules", ROUND330_STAGE3_YELLOW_RULES),
        ("Stage3-Green Rules", ROUND330_STAGE3_GREEN_RULES),
        ("Green Blockers", ROUND330_GREEN_BLOCKERS),
        ("Score Up Axes", ROUND330_SCORE_UP_AXES),
        ("Score Down Axes", ROUND330_SCORE_DOWN_AXES),
        ("Row Separation Rules", ROUND330_ROW_SEPARATION_RULES),
    ]
    lines = ["# Round 330 R9 Loop 17 Stage Rules", "", "Do not apply these weights to production scoring yet.", ""]
    for title, values in sections:
        lines.extend([f"## {title}", ""])
        lines.extend(f"- `{value}`" for value in values)
        lines.append("")
    return "\n".join(lines)


def render_round330_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 330 R9 Loop 17 Stage 4B / 4C Review", "", "## 4B Watch", ""]
    lines.extend(f"- `{item}`" for item in ROUND330_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- `{item}`" for item in ROUND330_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND330_CASE_CANDIDATES:
        lines.append(f"- `{case.case_id}`: {case.stage_candidate}; {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round330_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 330 R9 Loop 17 Price Validation Plan",
        "",
        "Full adjusted OHLC is not complete. Reported event anchors are retained, but MFE/MAE, peak and drawdown are not invented.",
        "",
        "| case_id | status | event anchor | next backfill |",
        "| --- | --- | --- | --- |",
    ]
    for case in ROUND330_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | price_data_unavailable_after_deep_search | {json.dumps(case.extra_price_metrics, ensure_ascii=False, sort_keys=True)} | adjusted OHLC backfill required |"
        )
    return "\n".join(lines) + "\n"


def write_round330_r9_loop17_reports(
    *,
    output_directory: str | Path = ROUND330_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND330_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND330_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND330_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND330_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    cases_path = Path(cases_path)
    triggers_path = Path(triggers_path)
    audit_path = Path(audit_path)
    weight_profile_path = Path(weight_profile_path)

    cases = write_case_library(round330_case_records(), cases_path)
    triggers = _write_jsonl(triggers_path, (trigger.as_dict() for trigger in ROUND330_TRIGGER_RECORDS))
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(json.dumps(round330_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    weights = _write_csv(weight_profile_path, round330_shadow_weight_rows())

    paths = {
        "cases": cases,
        "triggers": triggers,
        "audit": audit_path,
        "weight_profile": weights,
        "case_rows_csv": output_directory / "case_rows.csv",
        "trigger_rows_csv": output_directory / "trigger_rows.csv",
        "summary": output_directory / "round330_summary.md",
        "trigger_grid_md": output_directory / "trigger_grid.md",
        "stage_rules": output_directory / "stage_rules.md",
        "stage4b_4c_review": output_directory / "stage4b_4c_review.md",
        "price_validation_plan": output_directory / "price_validation_plan.md",
    }
    _write_csv(paths["case_rows_csv"], round330_case_rows())
    _write_csv(paths["trigger_rows_csv"], round330_trigger_rows())
    paths["summary"].write_text(render_round330_summary_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round330_trigger_grid_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round330_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round330_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round330_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def _write_jsonl(path: str | Path, rows: Iterable[Mapping[str, object]]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    return path


def _write_csv(path: str | Path, rows: Iterable[Mapping[str, object]]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path


def _signed(value: int) -> str:
    return f"{value:+d}"


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


__all__ = [
    "ROUND330_CASE_CANDIDATES",
    "ROUND330_GREEN_BLOCKERS",
    "ROUND330_HARD_4C_GATES",
    "ROUND330_LARGE_SECTOR",
    "ROUND330_REQUIRED_TARGET_ALIASES",
    "ROUND330_ROW_SEPARATION_RULES",
    "ROUND330_SCORE_DOWN_AXES",
    "ROUND330_SCORE_UP_AXES",
    "ROUND330_SHADOW_WEIGHT_ROWS",
    "ROUND330_STAGE2_ACTIONABLE_RULES",
    "ROUND330_STAGE3_GREEN_RULES",
    "ROUND330_STAGE3_YELLOW_RULES",
    "ROUND330_STAGE4B_WATCH_TRIGGERS",
    "ROUND330_TRIGGER_RECORDS",
    "render_round330_stage4b_4c_review_markdown",
    "render_round330_stage_rules_markdown",
    "render_round330_trigger_grid_markdown",
    "round330_audit_payload",
    "round330_case_records",
    "round330_case_rows",
    "round330_shadow_weight_rows",
    "round330_summary",
    "round330_trigger_rows",
    "write_round330_r9_loop17_reports",
]
