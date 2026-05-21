"""Round-332 R11 Loop-17 policy, geopolitics and disaster validation.

This module converts ``docs/round/round_332.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a Commercial Act reform can be Stage2-Actionable when the law
passes and KOSPI reacts. It still cannot become a company-level Green until
buyback cancellation, dividends or board actions are visible for that company.
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


ROUND332_SOURCE_ROUND_PATH = "docs/round/round_332.md"
ROUND332_ANALYST_ROUND_ID = "round_260"
ROUND332_LOOP_NAME = "R11 Loop 17"
ROUND332_LARGE_SECTOR = "POLICY_GEOPOLITICS_DISASTER_EVENT"
ROUND332_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND332_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round332_r11_loop17_policy_geopolitics_disaster_event_trigger_validation"
ROUND332_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r11_loop17_round260.jsonl"
ROUND332_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r11_loop17_round260.jsonl"
ROUND332_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round332_r11_loop17_policy_geopolitics_disaster_event_trigger_validation_audit.json"
ROUND332_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round260_r11_loop17_v1.csv"

ROUND332_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE": E2RArchetype.COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE.value,
    "TAX_POLICY_RELIEF_STAGE2_WITH_TAX_4B": E2RArchetype.TAX_POLICY_RELIEF_STAGE2_WITH_TAX_4B.value,
    "MARTIAL_LAW_POLITICAL_RISK_4B": E2RArchetype.MARTIAL_LAW_POLITICAL_RISK_4B.value,
    "AI_WINDFALL_TAX_POLICY_OVERHANG_4B": E2RArchetype.AI_WINDFALL_TAX_POLICY_OVERHANG_4B.value,
    "CHIP_EXPORT_CONTROL_4B_WITH_POLICY_RELIEF": E2RArchetype.CHIP_EXPORT_CONTROL_4B_WITH_POLICY_RELIEF.value,
    "SEMICONDUCTOR_TARIFF_SUPPORT_STAGE2_RELIEF": E2RArchetype.SEMICONDUCTOR_TARIFF_SUPPORT_STAGE2_RELIEF.value,
    "DEFENSE_GEOPOLITICAL_EXPORT_STAGE2_WITH_DILUTION_4B": E2RArchetype.DEFENSE_GEOPOLITICAL_EXPORT_STAGE2_WITH_DILUTION_4B.value,
    "NATIONAL_CHAMPION_LABOR_STRIKE_4B": E2RArchetype.NATIONAL_CHAMPION_LABOR_STRIKE_4B.value,
    "WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE": E2RArchetype.WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE.value,
}

ROUND332_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "law_policy_contract_disaster_or_labor_event_has_clear_public_date",
    "event_or_index_return_is_at_least_1pct_positive_or_negative_4B_is_clear",
    "policy_amount_law_content_contract_value_or_damage_scale_is_numeric",
    "path_to_company_EPS_OP_FCF_or_market_risk_premium_exists",
    "opposing_4B_axis_tax_dilution_export_control_labor_cost_or_political_risk_is_identified",
    "policy_relief_has_executable_path_not_only_commentary",
    "price_reaction_aligns_with_evidence",
)

ROUND332_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "law_converts_to_company_level_capital_return",
    "tax_stability_holds_across_multiple_policy_cycles",
    "foreign_or_retail_flow_recovers_and_breadth_widens",
    "export_control_license_stabilizes_and_capex_order_risk_falls",
    "industrial_support_converts_to_equipment_material_or_factory_orders",
    "defense_order_margin_delivery_and_dilution_absorption_are_visible",
    "labor_risk_settles_and_fixed_labor_cost_reset_is_limited",
    "disaster_recovery_converts_to_rebuilding_insurance_or_government_spend",
)

ROUND332_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "policy_reform_becomes_recurring_earnings_or_capital_return_evidence",
    "tax_uncertainty_is_durably_removed",
    "geopolitical_4B_is_reduced_through_licenses_treaties_or_contracts",
    "industrial_policy_support_converts_to_company_level_revenue",
    "defense_export_backlog_converts_into_margin_and_cash_flow",
    "labor_or_disaster_risk_resolves_without_structural_damage",
    "full_window_adjusted_OHLC_MFE_MAE_is_available_and_supportive",
)

ROUND332_GREEN_BLOCKERS: tuple[str, ...] = (
    "policy_reform_without_company_action",
    "tax_relief_without_stability",
    "liquidity_backstop_without_political_resolution",
    "AI_tax_noise_ignored",
    "chip_support_without_order_conversion",
    "defense_order_without_dilution_adjustment",
    "strike_threat_without_cost_reset",
    "disaster_without_price_anchor",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND332_SCORE_UP_AXES: tuple[str, ...] = (
    "governance_reform_law",
    "tax_policy_relief",
    "political_liquidity_backstop",
    "geopolitical_export_control_risk",
    "industrial_policy_support",
    "defense_export_backlog",
    "labor_supply_chain_risk",
    "disaster_hard_4c",
)

ROUND332_SCORE_DOWN_AXES: tuple[str, ...] = (
    "policy_reform_without_company_action_penalty",
    "tax_relief_without_stability_penalty",
    "liquidity_backstop_without_political_resolution_penalty",
    "AI_tax_noise_ignored_penalty",
    "chip_support_without_order_conversion_penalty",
    "defense_order_without_dilution_adjustment_penalty",
    "strike_threat_without_cost_reset_penalty",
    "disaster_without_price_anchor_penalty",
)

ROUND332_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "tax_policy_contradicts_valueup",
    "martial_law_or_political_crisis_threatens_institutions",
    "AI_windfall_tax_rhetoric_targets_cycle_leaders",
    "US_export_controls_affect_Korean_strategic_assets",
    "support_package_lacks_stock_or_order_conversion",
    "defense_export_financed_by_dilutive_equity",
    "national_champion_strike_risks_production_or_exports",
    "disaster_creates_compensation_rebuilding_or_safety_cost_without_price_anchor",
)

ROUND332_HARD_4C_GATES: tuple[str, ...] = (
    "disaster_with_fatalities_asset_destruction_and_listed_company_earnings_or_price_hit",
    "political_crisis_freezes_market_function_or_capital_flows",
    "export_control_permanently_blocks_production_or_technology_upgrade",
    "labor_strike_causes_actual_prolonged_production_halt_and_revenue_cut",
    "policy_or_tax_law_structurally_removes_cycle_profits",
    "fatal_wildfire_disaster_with_large_asset_destruction",
)

ROUND332_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_reported_event_return_index_move_policy_amount_liquidity_damage_or_fatality_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
    "do_not_treat_policy_geopolitical_labor_or_disaster_headline_as_Green_without_company_execution_flow_license_settlement_or_price_anchor",
)


@dataclass(frozen=True)
class Round332TriggerRecord:
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
class Round332ShadowWeightRow:
    archetype: E2RArchetype
    governance_reform_law: int
    tax_policy_relief: int
    political_liquidity_backstop: int
    geopolitical_export_control_risk: int
    industrial_policy_support: int
    defense_export_backlog: int
    labor_supply_chain_risk: int
    disaster_hard_4c: int
    policy_reform_without_company_action_penalty: int
    tax_relief_without_stability_penalty: int
    liquidity_backstop_without_political_resolution_penalty: int
    ai_tax_noise_ignored_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "governance_reform_law": _signed(self.governance_reform_law),
            "tax_policy_relief": _signed(self.tax_policy_relief),
            "political_liquidity_backstop": _signed(self.political_liquidity_backstop),
            "geopolitical_export_control_risk": _signed(self.geopolitical_export_control_risk),
            "industrial_policy_support": _signed(self.industrial_policy_support),
            "defense_export_backlog": _signed(self.defense_export_backlog),
            "labor_supply_chain_risk": _signed(self.labor_supply_chain_risk),
            "disaster_hard_4c": _signed(self.disaster_hard_4c),
            "policy_reform_without_company_action_penalty": _signed(self.policy_reform_without_company_action_penalty),
            "tax_relief_without_stability_penalty": _signed(self.tax_relief_without_stability_penalty),
            "liquidity_backstop_without_political_resolution_penalty": _signed(self.liquidity_backstop_without_political_resolution_penalty),
            "AI_tax_noise_ignored_penalty": _signed(self.ai_tax_noise_ignored_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round332CaseCandidate:
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
            "do_not_use_round332_cases_as_candidate_generation_input",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_policy_geopolitical_labor_or_disaster_headline_as_Green_without_company_execution_flow_license_settlement_or_price_anchor",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")

        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "tax" in field
            or "policy" in field
            or "license" in field
            or "dilution" in field
            or "labor" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "fatal" in field
            or "disaster" in field
            or "production_halt" in field
            or "market_function" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND332_LARGE_SECTOR,
            large_sector=ROUND332_LARGE_SECTOR,
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
            must_have_fields=ROUND332_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields)
            if self.case_type in {"event_premium", "4b_watch", "4c_thesis_break", "failed_rerating"}
            else None,
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


ROUND332_CASE_CANDIDATES: tuple[Round332CaseCandidate, ...] = (
    Round332CaseCandidate(
        "r11_loop17_commercial_act_valueup",
        "KOSPI/valueup_basket/financials/holdcos",
        "Korea market governance reform basket",
        E2RArchetype.COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE,
        (E2RArchetype.COMMERCIAL_ACT_VALUEUP_STAGE2_POLICY, E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN),
        "success_candidate",
        "Stage2_Actionable_market_governance_reform",
        "r11l17_commercial_act_T1",
        "Stage2-Actionable_market_governance_reform",
        "Stage2-Actionable",
        date(2025, 7, 3),
        date(2025, 7, 3),
        None,
        date(2025, 7, 3),
        None,
        False,
        ("revised_Commercial_Act_passed", "board_fiduciary_duty_to_shareholders", "KOSPI_plus_1_34pct", "KOSPI_close_3116_27", "Korea_Discount_removal"),
        ("enforcement_uncertainty_4B", "chaebol_resistance_4B", "tax_policy_inconsistency_4B", "company_specific_action_missing", "buyback_cancellation_missing"),
        {"trigger_date": "2025-07-03", "kospi_event_return_pct": 1.34, "kospi_close_points": 3116.27, "policy": "revised_Commercial_Act_expands_board_fiduciary_duty_to_shareholders"},
        "aligned",
        "excellent_stage2_actionable_policy_reform",
        "policy_event_rerating",
        "stage2_watch_success",
        "Law passage and KOSPI reaction aligned; company-level capital return remains the Yellow and Green gate.",
    ),
    Round332CaseCandidate(
        "r11_loop17_capital_gains_tax_reversal",
        "KOSPI/retail_sensitive_basket/brokers/financials",
        "Korea market tax-policy basket",
        E2RArchetype.TAX_POLICY_RELIEF_STAGE2_WITH_TAX_4B,
        (E2RArchetype.TAX_POLICY_MARKET_SHOCK_OVERLAY, E2RArchetype.POLICY_TAX_REVERSAL_MARKET_SHOCK),
        "success_candidate",
        "tax_policy_4B_then_Stage2_relief",
        "r11l17_tax_reversal_T1",
        "Stage2_tax_policy_relief",
        "Stage2-Actionable relief + 4B-watch",
        date(2025, 8, 1),
        date(2025, 9, 11),
        None,
        date(2025, 8, 1),
        None,
        False,
        ("tax_shock_KOSPI_minus_3_9pct", "reversal_KOSPI_plus_0_6_to_0_9pct", "large_shareholder_threshold_5B_to_1B_proposal", "transaction_tax_0_15_to_0_2pct_proposal"),
        ("transaction_tax_still_planned_4B", "future_tax_uncertainty_4B", "retail_flow_stability_missing", "tax_relief_without_stability"),
        {"tax_shock_date": "2025-08-01", "tax_shock_kospi_return_pct": -3.9, "relief_date": "2025-09-11", "relief_kospi_return_reuters_pct": 0.6, "relief_kospi_return_ft_pct": 0.9, "large_shareholder_threshold_original_krw_bn": 5, "large_shareholder_threshold_proposed_krw_bn": 1, "transaction_tax_before_pct": 0.15, "transaction_tax_proposed_pct": 0.2},
        "aligned",
        "Stage2_policy_relief_with_tax_4B",
        "policy_event_rerating",
        "stage2_watch_success",
        "Tax relief restored market sentiment, but transaction tax and future tax uncertainty remain 4B.",
    ),
    Round332CaseCandidate(
        "r11_loop17_martial_law_liquidity_intervention",
        "KOSPI/KRW/EWY/banks/brokers/exporters",
        "Korea political-risk basket",
        E2RArchetype.MARTIAL_LAW_POLITICAL_RISK_4B,
        (E2RArchetype.POLITICAL_CRISIS_MARKET_HARD_4C, E2RArchetype.FX_LIQUIDITY_POLICY_RESPONSE),
        "4b_watch",
        "political_risk_4B_with_liquidity_relief",
        "r11l17_martial_law_T0",
        "4B_political_risk_martial_law",
        "4B with Stage2 relief",
        date(2024, 12, 4),
        date(2024, 12, 4),
        None,
        date(2024, 12, 4),
        None,
        False,
        ("martial_law_declaration", "KOSPI_minus_1_44pct", "Samsung_minus_0_93pct", "won_shock_1444_then_1410", "unlimited_liquidity", "market_stabilization_fund_10T"),
        ("impeachment_risk_4B", "policy_paralysis_4B", "foreign_investor_confidence_4B", "FX_volatility_4B", "Korea_discount_repricing_4B"),
        {"trigger_date": "2024-12-04", "kospi_event_return_pct": -1.44, "samsung_electronics_event_return_pct": -0.93, "won_initial_shock_usdkrw_context": 1444, "won_later_context_usdkrw": 1410, "market_stabilization_fund_krw_trn": 10, "liquidity_response": "unlimited_liquidity_and_special_repo_operations"},
        "aligned",
        "political_risk_4B_not_hard_4C",
        "no_rerating",
        "should_have_been_red",
        "Political shock hit FX and stocks, but liquidity backstop prevented systemic hard 4C in this source set.",
    ),
    Round332CaseCandidate(
        "r11_loop17_ai_windfall_tax_policy_overhang",
        "KOSPI/005930/000660/AI_memory_basket",
        "AI memory / KOSPI concentration basket",
        E2RArchetype.AI_WINDFALL_TAX_POLICY_OVERHANG_4B,
        (E2RArchetype.AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK, E2RArchetype.POLICY_HEADLINE_NOT_GREEN),
        "4b_watch",
        "4B_AI_windfall_tax_policy_overhang",
        "r11l17_ai_windfall_tax_T0",
        "4B_AI_policy_tax_overhang",
        "4B-watch",
        date(2026, 5, 12),
        None,
        None,
        date(2026, 5, 12),
        None,
        False,
        ("AI_excess_profit_national_dividend_comment", "KOSPI_intraday_minus_5pct", "KOSPI_close_minus_2_3pct", "presidential_office_personal_opinion_relief"),
        ("policy_populism_4B", "AI_profit_tax_risk_4B", "index_concentration_4B", "foreign_flow_sensitivity_4B", "KOSPI_AI_overheat_4B"),
        {"trigger_date": "2026-05-12", "kospi_intraday_drop_pct": -5.0, "kospi_close_return_pct": -2.3, "policy_context": "AI_excess_profit_national_dividend_comment", "relief_context": "presidential_office_called_comment_personal_opinion"},
        "aligned",
        "AI_policy_overhang_4B_not_hard_4C",
        "no_rerating",
        "should_have_been_red",
        "AI tax rhetoric can hit concentrated KOSPI leaders even without enacted law; it is 4B until legal risk is removed.",
    ),
    Round332CaseCandidate(
        "r11_loop17_us_chip_waiver_revocation",
        "005930/000660/semiconductor_supply_chain",
        "Samsung Electronics / SK Hynix",
        E2RArchetype.CHIP_EXPORT_CONTROL_4B_WITH_POLICY_RELIEF,
        (E2RArchetype.CHIP_EXPORT_CONTROL_4C_WATCH, E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C),
        "4b_watch",
        "4B_geopolitical_chip_export_control",
        "r11l17_chip_waiver_T0",
        "4B_chip_export_control",
        "4B-watch",
        date(2025, 9, 1),
        None,
        None,
        date(2025, 9, 1),
        None,
        False,
        ("VEU_waiver_removed_for_China_fabs", "SK_Hynix_nearly_minus_5pct", "Samsung_more_than_minus_2pct", "licenses_for_existing_fabs_likely", "expansion_upgrades_limited"),
        ("China_fab_upgrade_limit_4B", "US_license_dependency_4B", "geopolitical_supply_chain_4B", "capex_rerouting_4B", "China_memory_competition_4B"),
        {"trigger_date": "2025-09-01", "sk_hynix_event_return_pct": "nearly_-5", "samsung_event_return_pct": "more_than_-2", "policy": "VEU_waiver_removed_for_China_fabs", "relief_context": "licenses_expected_for_existing_fab_operations_but_not_expansion_or_upgrade"},
        "aligned",
        "chip_export_control_4B_not_hard_4C",
        "no_rerating",
        "should_have_been_red",
        "Export-control shock hit memory leaders, but existing-fab license relief prevents hard 4C in this source set.",
    ),
    Round332CaseCandidate(
        "r11_loop17_semiconductor_support_33t",
        "005930/000660/chip_equipment_materials_basket",
        "Korea semiconductor support basket",
        E2RArchetype.SEMICONDUCTOR_TARIFF_SUPPORT_STAGE2_RELIEF,
        (E2RArchetype.STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN, E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE),
        "success_candidate",
        "Stage2_policy_relief_no_direct_price",
        "r11l17_chip_support_T0",
        "Stage2_semiconductor_policy_relief",
        "Stage2 relief",
        date(2025, 4, 15),
        date(2025, 4, 15),
        None,
        date(2025, 4, 15),
        None,
        False,
        ("semiconductor_support_33T_won", "prior_support_26T_won", "support_increase_26pct", "auto_support_3T_won", "low_cost_loans_subsidies_RnD_power_infra"),
        ("direct_price_anchor_missing", "order_conversion_missing_4B", "fiscal_crowding_4B", "capex_timing_4B", "US_tariff_path_4B"),
        {"trigger_date": "2025-04-15", "semiconductor_support_krw_trn": 33, "prior_support_krw_trn": 26, "support_increase_pct": 26, "auto_support_krw_trn": 3, "direct_price_anchor": "price_data_unavailable_after_deep_search"},
        "unknown",
        "Stage2_policy_relief_no_price",
        "policy_event_rerating",
        "stage2_watch_success",
        "Large support package is Stage2 relief, but company-level order/capex conversion and event-window price are missing.",
    ),
    Round332CaseCandidate(
        "r11_loop17_hanwha_defense_export_dilution",
        "012450",
        "Hanwha Aerospace",
        E2RArchetype.DEFENSE_GEOPOLITICAL_EXPORT_STAGE2_WITH_DILUTION_4B,
        (E2RArchetype.GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE, E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG),
        "success_candidate",
        "Stage2_defense_export_with_dilution_4B",
        "r11l17_hanwha_romania_T0",
        "Stage2_defense_export_geopolitical_order",
        "Stage2-Actionable + 4B-watch",
        date(2024, 7, 9),
        date(2024, 7, 9),
        None,
        date(2025, 4, 1),
        None,
        False,
        ("Romania_K9_order_usd_1B", "K9_units_54", "K10_units_36", "shares_plus_5pct_record_high", "backlog_30T_won", "share_sale_3_6T_won", "dilution_minus_13pct"),
        ("share_dilution_4B", "overseas_factory_capex_4B", "delivery_execution_4B", "geopolitical_budget_dependency_4B", "cash_flow_vs_equity_financing_4B"),
        {"export_trigger_date": "2024-07-09", "romania_order_value_usd_bn": 1.0, "k9_units": 54, "k10_units": 36, "export_event_return_pct": 5, "order_backlog_mar_2024_krw_trn": 30, "share_sale_value_krw_trn": 3.6, "share_sale_value_usd_bn": 2.5, "dilution_event_return_pct": -13},
        "aligned",
        "defense_export_stage2_with_dilution_4B",
        "event_premium",
        "stage2_watch_success",
        "Geopolitical export order was strong, but equity financing and dilution must be deducted before any Green discussion.",
    ),
    Round332CaseCandidate(
        "r11_loop17_samsung_strike_government_arbitration",
        "005930",
        "Samsung Electronics",
        E2RArchetype.NATIONAL_CHAMPION_LABOR_STRIKE_4B,
        (E2RArchetype.LABOR_DISRUPTION_SYSTEMIC_POLICY_4C, E2RArchetype.MEMORY_HBM_CAPACITY),
        "4b_watch",
        "4B_national_champion_labor_strike",
        "r11l17_samsung_strike_T0",
        "4B_national_champion_labor_strike",
        "4B-watch",
        date(2026, 5, 15),
        None,
        None,
        date(2026, 5, 15),
        None,
        False,
        ("Samsung_shares_minus_9_3pct", "18_day_strike_plan", "more_than_50000_workers_possible", "emergency_arbitration_possible", "single_day_loss_1T_won", "prolonged_disruption_loss_100T_won"),
        ("production_reliability_4B", "labor_cost_reset_4B", "HBM_supply_chain_4B", "rival_spillover_to_SK_Hynix_4B", "settlement_missing"),
        {"trigger_date": "2026-05-15", "event_return_pct": -9.3, "potential_strike_duration_days": 18, "possible_workers_involved": ">50000", "government_tool": "emergency_arbitration_possible", "single_day_direct_loss_krw_trn": 1, "prolonged_disruption_loss_krw_trn": 100, "hard_4C_status": "not_confirmed"},
        "aligned",
        "national_champion_labor_4B_not_hard_4C",
        "no_rerating",
        "should_have_been_red",
        "Strike threat hit Samsung; hard 4C requires actual sustained production disruption.",
    ),
    Round332CaseCandidate(
        "r11_loop17_south_korea_wildfire_disaster",
        "insurers/rebuild_basket/forestry/disaster_relief_basket",
        "South Korea wildfire disaster basket",
        E2RArchetype.WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE,
        (E2RArchetype.NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF, E2RArchetype.CLIMATE_DISASTER_SUPPLY_CHAIN_REFERENCE),
        "4c_thesis_break",
        "disaster_hard_4C_no_public_price",
        "r11l17_wildfire_T0",
        "disaster_hard_4C_no_public_price",
        "disaster hard 4C no public price",
        date(2025, 3, 25),
        None,
        None,
        None,
        date(2025, 3, 30),
        True,
        ("wildfire_disaster", "fatalities_initial_16", "fatalities_followup_26", "burned_area_48000ha", "thousands_of_buildings_destroyed", "public_stock_price_anchor_unavailable"),
        ("insurance_loss_unknown_4B", "rebuilding_contracts_missing", "listed_stock_price_anchor_unavailable", "disaster_without_price_anchor", "public_equity_hard_4C_not_confirmed"),
        {"trigger_date": "2025-03-25_to_2025-03-30", "fatalities_initial_context": 16, "fatalities_followup_context": 26, "burned_area_hectares_context": 48000, "destroyed_structures_context": "thousands_of_buildings", "public_stock_price_anchor": "price_data_unavailable_after_deep_search", "hard_4C_status": "disaster_level_confirmed_public_stock_not_available"},
        "unknown",
        "wildfire_disaster_hard_4C_no_public_price",
        "thesis_break",
        "should_have_been_red",
        "Disaster-level hard 4C is confirmed, but no listed-stock price anchor exists for forward-return calculation.",
    ),
)

ROUND332_TRIGGER_RECORDS: tuple[Round332TriggerRecord, ...] = (
    Round332TriggerRecord("r11l17_commercial_act_T1", "r11_loop17_commercial_act_valueup", "Stage2-Actionable_governance_reform_law", "2025-07-03", "Revised Commercial Act passed and expanded board duties to shareholders.", 1.34, "excellent_stage2_actionable_policy_reform", "Stage2-Actionable", {"kospi_close_points": 3116.27}),
    Round332TriggerRecord("r11l17_tax_shock_T0", "r11_loop17_capital_gains_tax_reversal", "4B_tax_policy_shock", "2025-08-01", "Tax package lowered large-shareholder threshold proposal and hurt market sentiment.", -3.9, "tax_policy_4B", "4B-watch", {"large_shareholder_threshold_proposed_krw_bn": 1, "transaction_tax_proposed_pct": 0.2}),
    Round332TriggerRecord("r11l17_tax_reversal_T1", "r11_loop17_capital_gains_tax_reversal", "Stage2_tax_policy_relief", "2025-09-11", "President Lee said threshold cut was unnecessary and market rebounded.", "Reuters_+0.6_FT_+0.9", "Stage2_policy_relief", "Stage2-Actionable", {"relief_kospi_return_reuters_pct": 0.6, "relief_kospi_return_ft_pct": 0.9}),
    Round332TriggerRecord("r11l17_martial_law_T0", "r11_loop17_martial_law_liquidity_intervention", "4B_political_risk_martial_law", "2024-12-04", "Martial law shock hit KOSPI, Samsung and won.", -1.44, "political_risk_4B_not_hard_4C", "4B-watch", {"samsung_electronics_event_return_pct": -0.93, "won_initial_shock_usdkrw_context": 1444}),
    Round332TriggerRecord("r11l17_martial_liquidity_T2", "r11_loop17_martial_law_liquidity_intervention", "Stage2_liquidity_relief", "2024-12-04", "Government and BOK pledged unlimited liquidity and a stabilization fund.", "price_data_unavailable_after_deep_search", "liquidity_relief_not_Green", "Stage2_relief", {"market_stabilization_fund_krw_trn": 10}),
    Round332TriggerRecord("r11l17_ai_windfall_tax_T0", "r11_loop17_ai_windfall_tax_policy_overhang", "4B_AI_policy_tax_overhang", "2026-05-12", "AI excess-profit national-dividend comment hit AI-heavy KOSPI.", -2.3, "AI_policy_overhang_4B", "4B-watch", {"kospi_intraday_drop_pct": -5.0}),
    Round332TriggerRecord("r11l17_chip_waiver_T0", "r11_loop17_us_chip_waiver_revocation", "4B_chip_export_control", "2025-09-01", "U.S. removed VEU waivers for Samsung/SK Hynix China fabs.", "SKHynix_nearly_-5_Samsung_more_than_-2", "chip_export_control_4B", "4B-watch", {"license_relief_context": "existing_fab_operations_likely"}),
    Round332TriggerRecord("r11l17_chip_support_T0", "r11_loop17_semiconductor_support_33t", "Stage2_semiconductor_policy_relief", "2025-04-15", "Korea expanded semiconductor support to 33T won and added auto support.", "price_data_unavailable_after_deep_search", "Stage2_policy_relief_no_price", "Stage2_relief", {"semiconductor_support_krw_trn": 33, "auto_support_krw_trn": 3}),
    Round332TriggerRecord("r11l17_hanwha_romania_T0", "r11_loop17_hanwha_defense_export_dilution", "Stage2_defense_export_geopolitical_order", "2024-07-09", "Hanwha won 1B USD Romania K9 order and shares rose to record high.", 5, "defense_export_stage2", "Stage2", {"romania_order_value_usd_bn": 1.0, "k9_units": 54, "k10_units": 36}),
    Round332TriggerRecord("r11l17_hanwha_dilution_T2", "r11_loop17_hanwha_defense_export_dilution", "4B_defense_dilution_equity_financing", "2025-04", "3.6T won share sale for overseas expansion hit shares.", -13, "dilution_4B_after_defense_rerating", "4B-watch", {"share_sale_value_krw_trn": 3.6, "share_sale_value_usd_bn": 2.5}),
    Round332TriggerRecord("r11l17_samsung_strike_T0", "r11_loop17_samsung_strike_government_arbitration", "4B_national_champion_labor_strike", "2026-05-15", "Samsung union held to strike plan and shares fell.", -9.3, "national_champion_labor_4B", "4B-watch", {"potential_strike_duration_days": 18, "single_day_direct_loss_krw_trn": 1}),
    Round332TriggerRecord("r11l17_wildfire_T0", "r11_loop17_south_korea_wildfire_disaster", "disaster_hard_4C_no_public_price", "2025-03-25_to_2025-03-30", "Wildfires caused fatalities, large burned area and destroyed structures.", "price_data_unavailable_after_deep_search", "wildfire_disaster_hard_4C_no_public_price", "4C_disaster_watch", {"fatalities_followup_context": 26, "burned_area_hectares_context": 48000}),
)

ROUND332_SHADOW_WEIGHT_ROWS: tuple[Round332ShadowWeightRow, ...] = (
    Round332ShadowWeightRow(E2RArchetype.COMMERCIAL_ACT_VALUEUP_STAGE2_ACTIONABLE, 5, 1, 0, 0, 0, 0, 0, 0, -5, -1, -1, -1, "Commercial Act + KOSPI +1.34", "company action missing", "buyback/dividend/governance execution", "Commercial Act."),
    Round332ShadowWeightRow(E2RArchetype.TAX_POLICY_RELIEF_STAGE2_WITH_TAX_4B, 2, 5, 0, 0, 0, 0, 0, 0, -2, -4, -1, -1, "tax reversal after -3.9 shock", "transaction tax remains", "stable tax regime+flow recovery", "tax policy."),
    Round332ShadowWeightRow(E2RArchetype.MARTIAL_LAW_POLITICAL_RISK_4B, 0, 0, 5, 1, 0, 0, 0, 1, -1, -1, -5, -1, "martial law KOSPI -1.44 and liquidity relief", "political resolution missing", "FX/foreign-flow stabilization", "martial law."),
    Round332ShadowWeightRow(E2RArchetype.AI_WINDFALL_TAX_POLICY_OVERHANG_4B, 0, 0, 0, 2, 0, 0, 0, 0, -1, -2, -1, -5, "KOSPI -2.3 on AI tax comment", "policy overhang", "law risk removed and flow recovers", "AI tax."),
    Round332ShadowWeightRow(E2RArchetype.CHIP_EXPORT_CONTROL_4B_WITH_POLICY_RELIEF, 0, 0, 1, 5, 2, 0, 0, 0, -1, -1, -1, -1, "US VEU waiver removal hit Samsung/SK Hynix", "license dependency", "license stability+capex clarity", "chip waivers."),
    Round332ShadowWeightRow(E2RArchetype.SEMICONDUCTOR_TARIFF_SUPPORT_STAGE2_RELIEF, 0, 1, 0, 3, 5, 0, 0, 0, -1, -1, -1, -1, "33T won semiconductor package", "no event price/order conversion", "order/capex conversion", "chip support."),
    Round332ShadowWeightRow(E2RArchetype.DEFENSE_GEOPOLITICAL_EXPORT_STAGE2_WITH_DILUTION_4B, 0, 0, 0, 3, 1, 5, 0, 0, -1, -1, -1, -1, "Hanwha Romania order +5 but dilution -13", "dilution and capex", "margin+delivery+dilution absorption", "Hanwha."),
    Round332ShadowWeightRow(E2RArchetype.NATIONAL_CHAMPION_LABOR_STRIKE_4B, 0, 0, 2, 1, 0, 0, 5, 0, -1, -1, -1, -1, "Samsung strike threat -9.3", "settlement missing", "strike averted+cost reset contained", "Samsung."),
    Round332ShadowWeightRow(E2RArchetype.WILDFIRE_DISASTER_HARD_4C_NO_PUBLIC_PRICE, 0, 0, 1, 0, 1, 0, 0, 5, -1, -1, -1, -1, "wildfire fatalities and property damage", "no public price anchor", "rebuilding/insurance conversion", "wildfires."),
)


def round332_case_records() -> tuple[E2RCaseRecord, ...]:
    records = tuple(candidate.to_case_record() for candidate in ROUND332_CASE_CANDIDATES)
    for record in records:
        record.validate()
    return records


def round332_case_rows() -> list[dict[str, str]]:
    return [candidate.as_row() for candidate in ROUND332_CASE_CANDIDATES]


def round332_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND332_TRIGGER_RECORDS]


def round332_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND332_SHADOW_WEIGHT_ROWS]


def round332_summary() -> dict[str, object]:
    return {
        "source_round": ROUND332_SOURCE_ROUND_PATH,
        "round_id": ROUND332_ANALYST_ROUND_ID,
        "loop_name": ROUND332_LOOP_NAME,
        "large_sector": ROUND332_LARGE_SECTOR,
        "method": ROUND332_METHOD,
        "case_candidate_count": len(ROUND332_CASE_CANDIDATES),
        "trigger_count": len(ROUND332_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND332_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": sum(1 for case in ROUND332_CASE_CANDIDATES if "Stage2-Actionable" in case.stage_candidate),
        "stage2_candidate_count": sum(1 for case in ROUND332_CASE_CANDIDATES if "Stage2" in case.stage_candidate),
        "stage3_yellow_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": sum(1 for case in ROUND332_CASE_CANDIDATES if case.stage4b_date is not None),
        "hard_4c_case_count": sum(1 for case in ROUND332_CASE_CANDIDATES if case.hard_4c_confirmed),
        "price_unavailable_count": sum(1 for case in ROUND332_CASE_CANDIDATES if case.score_price_alignment == "unknown"),
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R12 Loop 17",
    }


def round332_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND332_SOURCE_ROUND_PATH,
        "round_id": ROUND332_ANALYST_ROUND_ID,
        "large_sector": ROUND332_LARGE_SECTOR,
        "method": ROUND332_METHOD,
        "summary": round332_summary(),
        "target_archetypes": dict(ROUND332_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND332_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND332_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND332_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND332_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND332_SCORE_UP_AXES),
        "score_down_axes": list(ROUND332_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND332_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND332_HARD_4C_GATES),
        "row_separation_rules": list(ROUND332_ROW_SEPARATION_RULES),
        "shadow_weights": round332_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_change_production_scoring",
            "do_not_use_round332_cases_as_candidate_generation_input",
            "do_not_force_Stage3_Green",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_policy_geopolitical_labor_or_disaster_headline_as_Green_without_company_execution_flow_license_settlement_or_price_anchor",
        ],
    }


def render_round332_summary_markdown() -> str:
    summary = round332_summary()
    lines = [
        "# Round 332 R11 Loop 17 Policy Geopolitics Disaster Event Trigger Validation",
        "",
        f"- source_round: `{ROUND332_SOURCE_ROUND_PATH}`",
        f"- analyst_round_id: `{ROUND332_ANALYST_ROUND_ID}`",
        f"- large_sector: `{ROUND332_LARGE_SECTOR}`",
        f"- method: `{ROUND332_METHOD}`",
        f"- case candidates: `{summary['case_candidate_count']}`",
        f"- triggers: `{summary['trigger_count']}`",
        f"- Stage2-Actionable candidates: `{summary['stage2_actionable_candidate_count']}`",
        f"- Stage2 candidates: `{summary['stage2_candidate_count']}`",
        f"- Stage3-Green confirmed: `{summary['stage3_green_confirmed_count']}`",
        "- production_scoring_changed: `false`",
        "- candidate_generation_input: `false`",
        "- shadow_weight_only: `true`",
        "",
        "## Core Conclusions",
        "",
        "- Commercial Act reform is the cleanest Stage2-Actionable policy trigger, but individual-company Green requires capital-return execution.",
        "- Capital-gains tax reversal is Stage2 relief with tax 4B because transaction-tax and future-tax risks remain.",
        "- Martial law is political-risk 4B with liquidity relief, not hard 4C in this source set.",
        "- AI windfall tax and U.S. chip-waiver revocation are 4B overlays for AI and memory leaders.",
        "- Semiconductor support is Stage2 relief no-price until company-level order or capex conversion appears.",
        "- Hanwha defense export is Stage2 plus dilution 4B; order quality and equity financing must be scored together.",
        "- Samsung strike is national-champion labor 4B, while wildfire is disaster hard 4C no public price.",
    ]
    return "\n".join(lines) + "\n"


def render_round332_trigger_grid_markdown() -> str:
    lines = [
        "# Round 332 R11 Loop 17 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | date | event_return | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round332_trigger_rows():
        lines.append(
            f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |"
        )
    return "\n".join(lines) + "\n"


def render_round332_stage_rules_markdown() -> str:
    sections = [
        ("Stage2-Actionable Rules", ROUND332_STAGE2_ACTIONABLE_RULES),
        ("Stage3-Yellow Rules", ROUND332_STAGE3_YELLOW_RULES),
        ("Stage3-Green Rules", ROUND332_STAGE3_GREEN_RULES),
        ("Green Blockers", ROUND332_GREEN_BLOCKERS),
        ("Score Up Axes", ROUND332_SCORE_UP_AXES),
        ("Score Down Axes", ROUND332_SCORE_DOWN_AXES),
        ("Row Separation Rules", ROUND332_ROW_SEPARATION_RULES),
    ]
    lines = ["# Round 332 R11 Loop 17 Stage Rules", "", "Do not apply these weights to production scoring yet.", ""]
    for title, values in sections:
        lines.extend([f"## {title}", ""])
        lines.extend(f"- `{value}`" for value in values)
        lines.append("")
    return "\n".join(lines)


def render_round332_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 332 R11 Loop 17 Stage 4B / 4C Review", "", "## 4B Watch", ""]
    lines.extend(f"- `{item}`" for item in ROUND332_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- `{item}`" for item in ROUND332_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND332_CASE_CANDIDATES:
        lines.append(f"- `{case.case_id}`: {case.stage_candidate}; {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round332_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 332 R11 Loop 17 Price Validation Plan",
        "",
        "Full adjusted OHLC is not complete. Reported event anchors are retained, but MFE/MAE, peak and drawdown are not invented.",
        "",
        "| case_id | status | event anchor | next backfill |",
        "| --- | --- | --- | --- |",
    ]
    for case in ROUND332_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | price_data_unavailable_after_deep_search | {json.dumps(case.extra_price_metrics, ensure_ascii=False, sort_keys=True)} | adjusted OHLC backfill required |"
        )
    return "\n".join(lines) + "\n"


def write_round332_r11_loop17_reports(
    *,
    output_directory: str | Path = ROUND332_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND332_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND332_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND332_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND332_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    cases_path = Path(cases_path)
    triggers_path = Path(triggers_path)
    audit_path = Path(audit_path)
    weight_profile_path = Path(weight_profile_path)

    cases = write_case_library(round332_case_records(), cases_path)
    triggers = _write_jsonl(triggers_path, (trigger.as_dict() for trigger in ROUND332_TRIGGER_RECORDS))
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(json.dumps(round332_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    weights = _write_csv(weight_profile_path, round332_shadow_weight_rows())

    paths = {
        "cases": cases,
        "triggers": triggers,
        "audit": audit_path,
        "weight_profile": weights,
        "case_rows_csv": output_directory / "case_rows.csv",
        "trigger_rows_csv": output_directory / "trigger_rows.csv",
        "summary": output_directory / "round332_summary.md",
        "trigger_grid_md": output_directory / "trigger_grid.md",
        "stage_rules": output_directory / "stage_rules.md",
        "stage4b_4c_review": output_directory / "stage4b_4c_review.md",
        "price_validation_plan": output_directory / "price_validation_plan.md",
    }
    _write_csv(paths["case_rows_csv"], round332_case_rows())
    _write_csv(paths["trigger_rows_csv"], round332_trigger_rows())
    paths["summary"].write_text(render_round332_summary_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round332_trigger_grid_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round332_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round332_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round332_price_validation_plan_markdown(), encoding="utf-8")
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
    "ROUND332_CASE_CANDIDATES",
    "ROUND332_GREEN_BLOCKERS",
    "ROUND332_HARD_4C_GATES",
    "ROUND332_LARGE_SECTOR",
    "ROUND332_REQUIRED_TARGET_ALIASES",
    "ROUND332_ROW_SEPARATION_RULES",
    "ROUND332_SCORE_DOWN_AXES",
    "ROUND332_SCORE_UP_AXES",
    "ROUND332_SHADOW_WEIGHT_ROWS",
    "ROUND332_STAGE2_ACTIONABLE_RULES",
    "ROUND332_STAGE3_GREEN_RULES",
    "ROUND332_STAGE3_YELLOW_RULES",
    "ROUND332_STAGE4B_WATCH_TRIGGERS",
    "ROUND332_TRIGGER_RECORDS",
    "render_round332_stage4b_4c_review_markdown",
    "render_round332_stage_rules_markdown",
    "render_round332_trigger_grid_markdown",
    "round332_audit_payload",
    "round332_case_records",
    "round332_case_rows",
    "round332_shadow_weight_rows",
    "round332_summary",
    "round332_trigger_rows",
    "write_round332_r11_loop17_reports",
]
