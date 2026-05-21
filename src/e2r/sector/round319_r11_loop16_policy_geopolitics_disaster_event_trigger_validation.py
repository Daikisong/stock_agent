"""Round-319 R11 Loop-16 policy/geopolitics/disaster event validation.

This module converts ``docs/round/round_319.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a nuclear preferred-bidder headline can be Stage2, but it is not
Stage3-Green until final contract signing, legal challenge resolution, supplier
workshare, financing and margin are visible.
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


ROUND319_SOURCE_ROUND_PATH = "docs/round/round_319.md"
ROUND319_ANALYST_ROUND_ID = "round_247"
ROUND319_LARGE_SECTOR = "POLICY_GEOPOLITICS_DISASTER_EVENT"
ROUND319_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND319_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round319_r11_loop16_policy_geopolitics_disaster_event_trigger_validation"
ROUND319_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r11_loop16_round247.jsonl"
ROUND319_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r11_loop16_round247.jsonl"
ROUND319_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round319_r11_loop16_policy_geopolitics_disaster_event_trigger_validation_audit.json"
ROUND319_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round247_r11_loop16_v1.csv"

ROUND319_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE": E2RArchetype.GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE.value,
    "MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW": E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW.value,
    "NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B": E2RArchetype.NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B.value,
    "POLITICAL_CRISIS_MARKET_HARD_4C": E2RArchetype.POLITICAL_CRISIS_MARKET_HARD_4C.value,
    "COMMERCIAL_ACT_VALUEUP_STAGE2_POLICY": E2RArchetype.COMMERCIAL_ACT_VALUEUP_STAGE2_POLICY.value,
    "FOREIGN_STRATEGIC_CAPITAL_POLICY_STAGE2_ACTIONABLE": E2RArchetype.FOREIGN_STRATEGIC_CAPITAL_POLICY_STAGE2_ACTIONABLE.value,
    "SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B": E2RArchetype.SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B.value,
    "NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF": E2RArchetype.NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF.value,
}

ROUND319_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "contract_or_order_value_is_clear",
    "event_return_at_least_5pct",
    "market_relative_return_at_least_5pp",
    "policy_or_legal_trigger_closes_as_law_contract_budget_fine_or_enforcement",
    "defense_or_nuclear_has_at_least_one_delivery_workshare_margin_or_final_contract_gate",
    "governance_valueup_connects_to_company_specific_capital_allocation_or_board_action",
    "political_disaster_or_security_4C_overlay_is_absent",
)

ROUND319_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_FCF_path_can_change_materially",
    "one_of_delivery_legal_resolution_final_budget_or_company_specific_execution_remains_open",
    "reported_price_anchor_supports_trigger_but_full_adjusted_OHLC_is_missing",
)

ROUND319_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "defense_export_backlog_converts_to_deliveries_and_margin",
    "nuclear_preferred_bidder_converts_to_final_contract_and_supplier_workshare",
    "policy_reform_converts_to_company_specific_capital_allocation",
    "foreign_strategic_capital_converts_to_ROIC_and_earnings",
    "market_integrity_reform_improves_foreign_flow_and_liquidity_without_retail_backlash",
    "disaster_relief_converts_into_listed_company_contracts",
    "political_risk_is_resolved_and_foreign_capital_confidence_returns",
    "full_adjusted_OHLC_MFE_MAE_window_supports_stage_candidate",
)

ROUND319_GREEN_BLOCKERS: tuple[str, ...] = (
    "defense_order_without_capacity",
    "defense_growth_with_dilution_ignored",
    "preferred_bidder_without_contract",
    "policy_reform_without_company_action",
    "foreign_capital_without_ROIC",
    "market_rule_without_flow_data",
    "political_crisis_treated_as_one_day_event",
    "disaster_relief_without_listed_contract",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND319_SCORE_UP_AXES: tuple[str, ...] = (
    "defense_export_contract_value",
    "defense_backlog_delivery_visibility",
    "combat_validation",
    "nuclear_final_contract_signing",
    "nuclear_legal_resolution",
    "board_fiduciary_reform_execution",
    "foreign_strategic_capital_execution",
    "market_integrity_enforcement",
    "political_stability_risk",
    "disaster_reconstruction_budget",
)

ROUND319_SCORE_DOWN_AXES: tuple[str, ...] = (
    "defense_order_without_capacity",
    "defense_growth_with_dilution_ignored",
    "preferred_bidder_without_contract",
    "policy_reform_without_company_action",
    "foreign_capital_without_ROIC",
    "market_rule_without_flow_data",
    "political_crisis_treated_as_one_day_event",
    "disaster_relief_without_listed_contract",
)

ROUND319_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "defense_export_rally_followed_by_equity_dilution",
    "nuclear_preferred_bidder_rally_before_final_contract",
    "policy_reform_rally_before_company_specific_governance_action",
    "foreign_strategic_capital_rally_before_ROIC",
    "short_selling_reform_trust_positive_but_liquidity_or_foreign_participation_unclear",
    "political_shock_hits_KRW_KOSPI_or_ETF_confidence",
    "disaster_damage_lacks_listed_company_reconstruction_contract",
)

ROUND319_HARD_4C_GATES: tuple[str, ...] = (
    "martial_law_or_constitutional_crisis",
    "final_contract_blocked_by_court_or_rival_bidder_challenge",
    "defense_contract_cancelled_or_delivery_blocked",
    "large_equity_dilution_after_geopolitics_driven_rally",
    "disaster_causing_deaths_and_large_asset_destruction",
    "market_integrity_scandal_or_illegal_trading_undermines_trust",
    "sanctions_or_export_control_shock",
)

ROUND319_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_contract_policy_legal_disaster_or_market_structure_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_policy_defense_nuclear_disaster_or_market_integrity_headline_as_Green_without_law_contract_budget_delivery_margin_ROIC_or_company_execution",
)


@dataclass(frozen=True)
class Round319TriggerRecord:
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
class Round319CaseCandidate:
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
            "do_not_use_round319_cases_as_candidate_generation_input",
            "do_not_treat_policy_defense_nuclear_disaster_or_market_integrity_headline_as_Green_without_law_contract_budget_delivery_margin_ROIC_or_company_execution",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        stage4b_evidence = tuple(
            field
            for field in self.red_flag_fields
            if "4B" in field or "4b" in field or "dilution" in field or "legal" in field or "liquidity" in field or "ROIC" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "martial" in field
            or "wildfire" in field
            or "death" in field
            or "court" in field
            or "constitutional" in field
            or "KRW" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND319_LARGE_SECTOR,
            large_sector=ROUND319_LARGE_SECTOR,
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
            must_have_fields=ROUND319_STAGE3_GREEN_RULES,
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


ROUND319_CASE_CANDIDATES: tuple[Round319CaseCandidate, ...] = (
    Round319CaseCandidate(
        "r11_loop16_hanwha_aerospace_romania_defense_export",
        "012450",
        "Hanwha Aerospace",
        E2RArchetype.GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE,
        (E2RArchetype.DEFENSE_EXPORT_BACKLOG_STAGE2_ACTIONABLE, E2RArchetype.DEFENSE_CAPITAL_RAISE_DILUTION),
        "success_candidate",
        "Stage2_Actionable_defense_export_with_dilution_4B",
        "r11l16_hanwha_romania_T1/r11l16_hanwha_dilution_T4",
        "Stage2-Actionable_defense_export_with_dilution_4B",
        "Stage2-Actionable + 4B-watch",
        date(2022, 2, 24),
        date(2024, 7, 9),
        None,
        date(2025, 4, 1),
        None,
        False,
        ("Romania_K9_K10_order_1B_usd", "54_K9_howitzers", "36_K10_resupply_vehicles", "event_return_above_5pct_record_high", "defense_backlog_5_1T_to_30T_won", "global_howitzer_export_share_above_50pct"),
        ("delivery_schedule_execution_missing", "export_margin_missing", "working_capital_missing", "production_capacity_missing", "dilution_absorption_missing", "full_OHLC_MFE_MAE_missing", "dilution_4B"),
        5.0,
        -13.0,
        {"trigger_date": "2024-07-09", "contract_value_usd_bn": 1.0, "event_return_pct": ">5", "event_price_context": "record_high", "defense_backlog_end_2021_krw_trn": 5.1, "defense_backlog_mar_2024_krw_trn": 30, "global_howitzer_export_share_pct": ">50", "dilution_event_return_pct": -13},
        "aligned",
        "excellent_stage2_actionable_defense_export_with_4B_dilution",
        "event_premium",
        "stage2_watch_success",
        "Romania K9/K10 order and backlog expansion are clean Stage2-Actionable evidence. Green waits for delivery, margin, production capacity and dilution absorption.",
    ),
    Round319CaseCandidate(
        "r11_loop16_lig_nex1_iraq_msam_iran_validation",
        "079550",
        "LIG Nex1",
        E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW,
        (E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION, E2RArchetype.DEFENSE_INTERCEPTOR_COMBAT_VALIDATION),
        "success_candidate",
        "Stage3_Yellow_candidate_missile_defense_export",
        "r11l16_lig_iraq_T0/r11l16_lig_iran_validation_T2",
        "Stage2_export_to_Stage3-Yellow_candidate",
        "Stage3-Yellow candidate",
        date(2024, 9, 20),
        date(2024, 9, 20),
        date(2026, 3, 11),
        date(2026, 3, 11),
        None,
        False,
        ("Iraq_M-SAM_II_order_3_71T_won", "contract_value_2_8B_usd", "shares_plus_3_6pct_vs_KOSPI_plus_0_9pct", "prior_Saudi_contract_3_2B_usd", "fourth_operator_country", "combat_validation_return_context_plus_47pct", "reported_success_rate_96pct"),
        ("delivery_capacity_missing", "export_margin_missing", "repeat_middle_east_orders_missing", "production_ramp_missing", "working_capital_missing", "war_event_premium_4B", "full_OHLC_MFE_MAE_missing"),
        47.0,
        None,
        {"iraq_contract_date": "2024-09-20", "iraq_contract_value_krw_trn": 3.71, "iraq_contract_value_usd_bn": 2.8, "event_return_pct": 3.6, "kospi_same_context_pct": 0.9, "market_relative_return_pp": 2.7, "prior_saudi_contract_value_usd_bn": 3.2, "operator_count_after_iraq": 4, "iran_war_validation_date": "2026-03-11", "iran_war_share_return_context_pct": 47, "cheongung_reported_success_rate_pct": 96},
        "aligned",
        "Stage3_Yellow_candidate_missile_defense_export",
        "event_premium",
        "yellow_success",
        "Iraq export plus later combat validation supports Yellow. Green still needs production ramp, delivery, margin, working capital and repeat orders.",
    ),
    Round319CaseCandidate(
        "r11_loop16_khnp_czech_nuclear_export",
        "034020/052690/051600/015760",
        "Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E / KEPCO read-through",
        E2RArchetype.NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B,
        (E2RArchetype.NUCLEAR_EXPORT_PREFERRED_BIDDER, E2RArchetype.NUCLEAR_EXPORT_LEGAL_4C_WATCH),
        "event_premium",
        "Stage2_nuclear_export_with_legal_4B",
        "r11l16_czech_nuclear_T1/r11l16_czech_nuclear_legal_T3",
        "Stage2_nuclear_export_with_legal_4B",
        "Stage2 + 4B-watch",
        date(2024, 7, 17),
        date(2024, 7, 17),
        None,
        date(2025, 5, 6),
        None,
        False,
        ("KHNP_preferred_bidder_Dukovany", "two_reactors", "unit_cost_200B_CZK", "unit_cost_8_65B_usd", "first_large_overseas_order_since_2009", "Doosan_3m_plus_48pct", "KEPCO_EC_3m_plus_41pct"),
        ("final_contract_signing_missing", "EDF_legal_resolution_missing", "Korean_supplier_workshare_missing", "project_financing_missing", "margin_missing", "Czech_court_legal_4B", "full_OHLC_MFE_MAE_missing"),
        48.0,
        None,
        {"preferred_bidder_date": "2024-07-17", "reactor_count": 2, "unit_cost_czk_bn": 200, "unit_cost_usd_bn": 8.65, "first_large_overseas_order_since": 2009, "doosan_3m_return_context_pct": 48, "kepco_plant_service_3m_return_context_pct": 14, "kepco_ec_3m_return_context_pct": 41, "legal_4b_date": "2025-05-06", "legal_4b_event": "Czech_court_blocks_contract_signing_after_EDF_complaint"},
        "aligned",
        "nuclear_export_stage2_with_legal_4B",
        "policy_event_rerating",
        "stage2_watch_success",
        "Czech preferred-bidder status is Stage2. EDF legal challenge and missing final contract/workshare keep it from Green.",
    ),
    Round319CaseCandidate(
        "r11_loop16_martial_law_political_shock",
        "KOSPI/KRW/EWY/broad_market",
        "South Korea broad market",
        E2RArchetype.POLITICAL_CRISIS_MARKET_HARD_4C,
        (E2RArchetype.POLITICAL_INSTITUTIONAL_TRUST_BREAK, E2RArchetype.POLITICAL_LIQUIDITY_SHOCK_HARD_REFERENCE),
        "4c_thesis_break",
        "hard_4C_political_crisis",
        "r11l16_martial_law_T0",
        "hard_4C_political_crisis_with_relief",
        "4C",
        date(2024, 12, 3),
        None,
        None,
        None,
        date(2024, 12, 3),
        True,
        ("martial_law_declaration", "parliament_rejection", "decree_reversal", "KOSPI_nearly_minus_2pct", "KRW_near_two_year_low", "company_specific_trigger_false"),
        ("political_stability_missing", "impeachment_resolution_missing", "policy_continuity_missing", "foreign_flow_stabilization_missing", "KRW_stabilization_missing", "broad_market_4C"),
        None,
        -2.0,
        {"trigger_date": "2024-12-03/2024-12-04", "kospi_event_return_context_pct": "nearly_-2", "krw_context": "near_two_year_low", "martial_law_reversed": True, "parliament_rejection": True, "company_specific_trigger": False},
        "aligned",
        "hard_4C_success_political_crisis",
        "thesis_break",
        "should_have_been_red",
        "Martial law is a broad hard 4C for KRW, KOSPI and market confidence, not a company-specific Stage2 trigger.",
    ),
    Round319CaseCandidate(
        "r11_loop16_commercial_act_valueup",
        "KOSPI/holding_company_basket/financials/chaebol_basket",
        "Korea Value-Up policy basket",
        E2RArchetype.COMMERCIAL_ACT_VALUEUP_STAGE2_POLICY,
        (E2RArchetype.CORPORATE_GOVERNANCE_VALUEUP_POLICY, E2RArchetype.MARKET_STRUCTURE_REFORM),
        "success_candidate",
        "Stage2_policy_reform",
        "r11l16_commercial_act_T1",
        "Stage2_policy_reform_with_execution_4B",
        "Stage2",
        date(2025, 7, 3),
        date(2025, 7, 3),
        None,
        date(2025, 7, 3),
        None,
        False,
        ("Commercial_Act_revision", "fiduciary_duty_to_minority_shareholders", "KOSPI_plus_1_34pct", "Korea_Discount_reform"),
        ("company_specific_board_action_missing", "dividend_policy_change_missing", "buyback_cancellation_missing", "tender_offer_fairness_missing", "minority_shareholder_case_law_missing", "policy_reform_without_company_action_4B"),
        1.34,
        None,
        {"trigger_date": "2025-07-03", "policy": "Commercial_Act_revision_expanding_director_fiduciary_duty_to_minority_shareholders", "kospi_event_return_pct": 1.34, "kospi_event_close": 3116.27, "reform_target": "Korea_Discount"},
        "aligned",
        "Stage2_policy_reform_not_Green",
        "policy_event_rerating",
        "stage2_watch_success",
        "Commercial Act reform is Stage2 policy evidence. Green requires company-specific board action, buyback cancellation, dividend policy and fair transactions.",
    ),
    Round319CaseCandidate(
        "r11_loop16_samsung_sds_kkr_strategic_capital",
        "018260",
        "Samsung SDS",
        E2RArchetype.FOREIGN_STRATEGIC_CAPITAL_POLICY_STAGE2_ACTIONABLE,
        (E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY, E2RArchetype.AI_CAPITAL_MARKET_CONFIDENCE_EVENT),
        "success_candidate",
        "Stage2_Actionable_foreign_strategic_capital_with_CB_4B",
        "r11l16_samsung_sds_kkr_T1",
        "Stage2-Actionable_foreign_strategic_capital_with_CB_4B",
        "Stage2-Actionable + 4B-watch",
        date(2026, 4, 15),
        date(2026, 4, 15),
        None,
        date(2026, 4, 15),
        None,
        False,
        ("KKR_820M_usd_CB", "Samsung_SDS_intraday_plus_20_8pct", "morning_plus_19_4pct_vs_KOSPI_plus_3_0pct", "market_relative_morning_plus_16_4pp", "cash_balance_6_4T_won", "KKR_advisory_6_years", "AI_MA_capital_allocation_focus"),
        ("CB_dilution_4B", "AI_execution_missing", "M&A_ROIC_missing", "policy_theme_overextension", "full_OHLC_MFE_MAE_missing"),
        20.8,
        None,
        {"trigger_date": "2026-04-15", "convertible_bond_value_usd_mn": 820, "event_intraday_return_pct": 20.8, "event_morning_return_pct": 19.4, "kospi_same_context_pct": 3.0, "market_relative_morning_pp": 16.4, "cash_balance_krw_trn": 6.4, "kkr_advisory_period_years": 6, "strategic_focus": ["M&A", "capital_allocation", "AI_offerings", "physical_AI", "stablecoins"]},
        "aligned",
        "excellent_stage2_actionable_foreign_capital_policy_reform",
        "policy_event_rerating",
        "stage2_watch_success",
        "KKR strategic capital and price reaction are strong Stage2-Actionable evidence. Green waits for ROIC, AI revenue, disciplined M&A and CB dilution absorption.",
    ),
    Round319CaseCandidate(
        "r11_loop16_short_selling_market_integrity",
        "KOSPI/KOSDAQ/brokerage_basket/foreign_flow",
        "Korea short-selling market-integrity policy",
        E2RArchetype.SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B,
        (E2RArchetype.SHORT_SELLING_MARKET_ACCESS_REFORM, E2RArchetype.MARKET_ACCESS_REFORM_STAGE2),
        "success_candidate",
        "Stage2_market_integrity_with_liquidity_4B",
        "r11l16_short_selling_integrity_T1",
        "Stage2_market_integrity_with_liquidity_4B",
        "Stage2 + 4B-watch",
        date(2023, 11, 1),
        date(2025, 3, 1),
        None,
        date(2025, 7, 9),
        None,
        False,
        ("short_selling_ban_2023_11", "ban_lift_after_detection_system_2025_03", "one_strike_policy_2025_07_09", "fine_up_to_100pct_of_short_sale_orders", "business_suspension_and_trading_restrictions"),
        ("foreign_flow_improvement_missing", "market_liquidity_improvement_missing", "illegal_short_selling_reduction_missing", "retail_trust_missing", "MSCI_developed_market_access_missing", "liquidity_4B"),
        None,
        None,
        {"ban_start_context": "2023-11", "ban_lift_context": "2025-03", "one_strike_policy_date": "2025-07-09", "fine_for_serious_violation_pct_of_short_sale_orders": 100, "penalties": ["business_suspension", "trading_restrictions", "illicit_gain_recovery"], "direct_price_anchor": "price_data_unavailable_after_deep_search"},
        "evidence_good_but_price_failed",
        "Stage2_market_integrity_policy_not_Green",
        "policy_event_rerating",
        "stage2_watch_success",
        "Market-integrity enforcement is Stage2 policy evidence. Green requires foreign flow, market liquidity and trust improvement data.",
    ),
    Round319CaseCandidate(
        "r11_loop16_2025_wildfire_disaster_relief",
        "insurance/construction_repair/tourism_local_assets/disaster_basket",
        "2025 South Korea wildfire disaster reference",
        E2RArchetype.NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF,
        (E2RArchetype.NATURAL_DISASTER_RECOVERY_POLICY_REFERENCE, E2RArchetype.DISASTER_REBUILD_EVENT),
        "4c_thesis_break",
        "hard_4C_disaster_with_relief_reference",
        "r11l16_wildfire_disaster_T0",
        "hard_4C_disaster_with_relief_reference",
        "disaster 4C reference",
        date(2025, 3, 21),
        None,
        None,
        date(2025, 3, 30),
        date(2025, 3, 21),
        True,
        ("wildfire_disaster", "at_least_26_deaths", "48000_hectares_burned", "4000_structures_destroyed", "tens_of_thousands_evacuated", "special_disaster_zone_context"),
        ("insurance_loss_estimate_missing", "reconstruction_budget_allocation_missing", "listed_company_contracts_missing", "tourism_recovery_missing", "local_asset_damage_quantification_missing", "disaster_4C"),
        None,
        None,
        {"trigger_period": "2025-03-21_to_2025-03-30", "fatalities_context": "at_least_26", "area_burned_hectares_context": 48000, "structures_destroyed_context": 4000, "evacuation_context": "tens_of_thousands", "special_disaster_zone_context": True, "direct_stock_price_anchor": "price_data_unavailable_after_deep_search"},
        "evidence_good_but_price_failed",
        "natural_disaster_4C_relief_reference",
        "thesis_break",
        "should_have_been_red",
        "Wildfire is a hard disaster reference. Reconstruction relief is not investible Stage2 unless listed-company contracts or insurance-loss evidence appears.",
    ),
)

ROUND319_TRIGGER_RECORDS: tuple[Round319TriggerRecord, ...] = (
    Round319TriggerRecord("r11l16_hanwha_romania_T1", "r11_loop16_hanwha_aerospace_romania_defense_export", "Stage2-Actionable_defense_export", "2024-07-09", "Hanwha wins $1B Romania order for 54 K9 howitzers, ammunition and 36 K10 vehicles; shares rise more than 5% to record high; backlog around 30T won by Mar 2024.", ">5", "excellent_stage2_actionable_defense_export", "Stage2-Actionable", {"contract_value_usd_bn": 1.0, "backlog_mar_2024_krw_trn": 30}),
    Round319TriggerRecord("r11l16_hanwha_dilution_T4", "r11_loop16_hanwha_aerospace_romania_defense_export", "4B_dilution_overlay", "2025-04", "Hanwha announces large share sale/equity raise for overseas expansion; shares drop 13% after announcement.", -13, "defense_growth_with_dilution_4B", "4B-watch", {"dilution_event_return_pct": -13}),
    Round319TriggerRecord("r11l16_lig_iraq_T0", "r11_loop16_lig_nex1_iraq_msam_iran_validation", "Stage2_defense_export", "2024-09-20", "LIG wins 3.71T won / $2.8B Iraq Cheongung-II order; shares +3.6%, KOSPI +0.9%; Iraq becomes fourth operator after Korea, UAE and Saudi Arabia.", 3.6, "good_stage2_defense_export", "Stage2", {"market_relative_return_pp": 2.7, "operator_count_after_iraq": 4}),
    Round319TriggerRecord("r11l16_lig_iran_validation_T2", "r11_loop16_lig_nex1_iraq_msam_iran_validation", "Stage3-Yellow_candidate_combat_validation", "2026-03-11", "Combat validation and missile-defense demand lift LIG shares nearly +47% since Iran war began; reported Cheongung-II success rate 96%.", 47, "Stage3_Yellow_candidate_combat_validation", "Stage3-Yellow_candidate", {"reported_success_rate_pct": 96}),
    Round319TriggerRecord("r11l16_czech_nuclear_T1", "r11_loop16_khnp_czech_nuclear_export", "Stage2_nuclear_export", "2024-07-17", "KHNP selected preferred bidder for two Dukovany reactors; each unit estimated 200B CZK / $8.65B; Doosan +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over three months.", "3m_context_Doosan_+48_KEPCO_EC_+41", "Stage2_nuclear_export", "Stage2", {"reactor_count": 2, "unit_cost_usd_bn": 8.65, "doosan_3m_return_context_pct": 48}),
    Round319TriggerRecord("r11l16_czech_nuclear_legal_T3", "r11_loop16_khnp_czech_nuclear_export", "4B_legal_challenge", "2025-05-06", "Czech court blocks final contract signing after EDF complaint; deal cannot be signed until court review.", "price_data_unavailable_after_deep_search", "nuclear_export_legal_4B", "4B-watch", {"legal_4b_event": "Czech_court_blocks_contract_signing_after_EDF_complaint"}),
    Round319TriggerRecord("r11l16_martial_law_T0", "r11_loop16_martial_law_political_shock", "hard_4C_political_crisis", "2024-12-03/2024-12-04", "President Yoon declares martial law, parliament rejects it, decree reverses; KOSPI nearly -2%, won near two-year low.", "KOSPI_nearly_-2", "hard_4C_success_political_crisis", "4C", {"krw_context": "near_two_year_low", "company_specific_trigger": False}),
    Round319TriggerRecord("r11l16_commercial_act_T1", "r11_loop16_commercial_act_valueup", "Stage2_policy_reform", "2025-07-03", "Parliament passes revised Commercial Act expanding fiduciary duty to minority shareholders; KOSPI +1.34% to 3,116.27.", 1.34, "Stage2_policy_reform_not_Green", "Stage2", {"kospi_event_close": 3116.27}),
    Round319TriggerRecord("r11l16_samsung_sds_kkr_T1", "r11_loop16_samsung_sds_kkr_strategic_capital", "Stage2-Actionable_foreign_strategic_capital", "2026-04-15", "KKR to buy $820M Samsung SDS CBs; Samsung SDS +20.8% intraday and +19.4% morning vs KOSPI +3.0%; KKR advises on M&A, capital allocation and AI expansion.", 20.8, "excellent_stage2_actionable_foreign_strategic_capital", "Stage2-Actionable", {"market_relative_morning_pp": 16.4, "convertible_bond_value_usd_mn": 820}),
    Round319TriggerRecord("r11l16_short_selling_integrity_T1", "r11_loop16_short_selling_market_integrity", "Stage2_market_integrity_policy", "2025-03/2025-07-09", "Korea lifts short-selling ban after detection system; regulators announce one-strike-out policy, fines up to 100% of short-sale orders, business suspensions and trading restrictions.", "price_data_unavailable_after_deep_search", "Stage2_market_integrity_with_liquidity_4B", "Stage2+4B", {"fine_for_serious_violation_pct_of_short_sale_orders": 100}),
    Round319TriggerRecord("r11l16_wildfire_disaster_T0", "r11_loop16_2025_wildfire_disaster_relief", "hard_4C_disaster_reference", "2025-03-21_to_2025-03-30", "South Korea wildfires cause at least 26 deaths, burn around 48,000 hectares and destroy about 4,000 structures; special disaster relief context but no listed-company price anchor.", "price_data_unavailable_after_deep_search", "natural_disaster_4C_relief_reference", "4C_reference", {"fatalities_context": "at_least_26", "area_burned_hectares_context": 48000, "structures_destroyed_context": 4000}),
)

ROUND319_SHADOW_WEIGHT_ROWS: tuple[dict[str, str], ...] = (
    {"archetype": E2RArchetype.GEOPOLITICAL_DEFENSE_EXPORT_STAGE2_ACTIONABLE.value, "defense_export_contract_value": "+5", "defense_backlog_delivery_visibility": "+5", "combat_validation": "+2", "nuclear_final_contract_signing": "+0", "nuclear_legal_resolution": "+0", "board_fiduciary_reform_execution": "+0", "foreign_strategic_capital_execution": "+0", "market_integrity_enforcement": "+0", "political_stability_risk": "+2", "disaster_reconstruction_budget": "+0", "defense_order_without_capacity_penalty": "-5", "defense_growth_with_dilution_ignored_penalty": "-5", "preferred_bidder_without_contract_penalty": "-1", "policy_reform_without_company_action_penalty": "-1", "stage2_actionable_promote": "defense export order+price reaction", "stage3_yellow_gate": "delivery/margin/dilution pending", "stage3_green_gate": "delivery+margin+capacity", "notes": "Hanwha Aerospace."},
    {"archetype": E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW.value, "defense_export_contract_value": "+5", "defense_backlog_delivery_visibility": "+5", "combat_validation": "+5", "nuclear_final_contract_signing": "+0", "nuclear_legal_resolution": "+0", "board_fiduciary_reform_execution": "+0", "foreign_strategic_capital_execution": "+0", "market_integrity_enforcement": "+0", "political_stability_risk": "+2", "disaster_reconstruction_budget": "+0", "defense_order_without_capacity_penalty": "-5", "defense_growth_with_dilution_ignored_penalty": "-2", "preferred_bidder_without_contract_penalty": "-1", "policy_reform_without_company_action_penalty": "-1", "stage2_actionable_promote": "export order+combat validation", "stage3_yellow_gate": "production/margin pending", "stage3_green_gate": "repeat orders+delivery+margin", "notes": "LIG Nex1."},
    {"archetype": E2RArchetype.NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B.value, "defense_export_contract_value": "+2", "defense_backlog_delivery_visibility": "+2", "combat_validation": "+0", "nuclear_final_contract_signing": "+5", "nuclear_legal_resolution": "+5", "board_fiduciary_reform_execution": "+0", "foreign_strategic_capital_execution": "+0", "market_integrity_enforcement": "+0", "political_stability_risk": "+2", "disaster_reconstruction_budget": "+0", "defense_order_without_capacity_penalty": "-1", "defense_growth_with_dilution_ignored_penalty": "-1", "preferred_bidder_without_contract_penalty": "-5", "policy_reform_without_company_action_penalty": "-1", "stage2_actionable_promote": "preferred bidder and nuclear-policy win", "stage3_yellow_gate": "final contract/legal resolution missing", "stage3_green_gate": "final contract+workshare+margin", "notes": "Czech nuclear basket."},
    {"archetype": E2RArchetype.POLITICAL_CRISIS_MARKET_HARD_4C.value, "defense_export_contract_value": "+0", "defense_backlog_delivery_visibility": "+0", "combat_validation": "+0", "nuclear_final_contract_signing": "+0", "nuclear_legal_resolution": "+0", "board_fiduciary_reform_execution": "+0", "foreign_strategic_capital_execution": "+0", "market_integrity_enforcement": "+1", "political_stability_risk": "+5", "disaster_reconstruction_budget": "+0", "defense_order_without_capacity_penalty": "-1", "defense_growth_with_dilution_ignored_penalty": "-1", "preferred_bidder_without_contract_penalty": "-1", "policy_reform_without_company_action_penalty": "-1", "stage2_actionable_promote": "martial-law shock", "stage3_yellow_gate": "political stability missing", "stage3_green_gate": "N/A", "notes": "KOSPI/KRW."},
    {"archetype": E2RArchetype.COMMERCIAL_ACT_VALUEUP_STAGE2_POLICY.value, "defense_export_contract_value": "+0", "defense_backlog_delivery_visibility": "+0", "combat_validation": "+0", "nuclear_final_contract_signing": "+0", "nuclear_legal_resolution": "+0", "board_fiduciary_reform_execution": "+5", "foreign_strategic_capital_execution": "+2", "market_integrity_enforcement": "+2", "political_stability_risk": "+1", "disaster_reconstruction_budget": "+0", "defense_order_without_capacity_penalty": "-1", "defense_growth_with_dilution_ignored_penalty": "-1", "preferred_bidder_without_contract_penalty": "-1", "policy_reform_without_company_action_penalty": "-5", "stage2_actionable_promote": "law passed with market reaction", "stage3_yellow_gate": "company action missing", "stage3_green_gate": "buyback/dividend/board action", "notes": "Value-Up."},
    {"archetype": E2RArchetype.FOREIGN_STRATEGIC_CAPITAL_POLICY_STAGE2_ACTIONABLE.value, "defense_export_contract_value": "+0", "defense_backlog_delivery_visibility": "+0", "combat_validation": "+0", "nuclear_final_contract_signing": "+0", "nuclear_legal_resolution": "+0", "board_fiduciary_reform_execution": "+3", "foreign_strategic_capital_execution": "+5", "market_integrity_enforcement": "+1", "political_stability_risk": "+1", "disaster_reconstruction_budget": "+0", "defense_order_without_capacity_penalty": "-1", "defense_growth_with_dilution_ignored_penalty": "-3", "preferred_bidder_without_contract_penalty": "-1", "policy_reform_without_company_action_penalty": "-2", "stage2_actionable_promote": "KKR/Samsung SDS strategic capital", "stage3_yellow_gate": "ROIC/AI execution/CB dilution pending", "stage3_green_gate": "AI revenue+M&A ROIC+capital allocation", "notes": "Samsung SDS."},
    {"archetype": E2RArchetype.SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B.value, "defense_export_contract_value": "+0", "defense_backlog_delivery_visibility": "+0", "combat_validation": "+0", "nuclear_final_contract_signing": "+0", "nuclear_legal_resolution": "+0", "board_fiduciary_reform_execution": "+1", "foreign_strategic_capital_execution": "+0", "market_integrity_enforcement": "+5", "political_stability_risk": "+2", "disaster_reconstruction_budget": "+0", "defense_order_without_capacity_penalty": "-1", "defense_growth_with_dilution_ignored_penalty": "-1", "preferred_bidder_without_contract_penalty": "-1", "policy_reform_without_company_action_penalty": "-2", "stage2_actionable_promote": "market integrity enforcement", "stage3_yellow_gate": "flow/liquidity data missing", "stage3_green_gate": "foreign flow+liquidity+trust", "notes": "short-selling policy."},
    {"archetype": E2RArchetype.NATURAL_DISASTER_RECONSTRUCTION_4C_RELIEF.value, "defense_export_contract_value": "+0", "defense_backlog_delivery_visibility": "+0", "combat_validation": "+0", "nuclear_final_contract_signing": "+0", "nuclear_legal_resolution": "+0", "board_fiduciary_reform_execution": "+0", "foreign_strategic_capital_execution": "+0", "market_integrity_enforcement": "+1", "political_stability_risk": "+2", "disaster_reconstruction_budget": "+5", "defense_order_without_capacity_penalty": "-1", "defense_growth_with_dilution_ignored_penalty": "-1", "preferred_bidder_without_contract_penalty": "-1", "policy_reform_without_company_action_penalty": "-1", "stage2_actionable_promote": "wildfire disaster relief", "stage3_yellow_gate": "listed contracts missing", "stage3_green_gate": "reconstruction contracts+insurance loss clarity", "notes": "wildfire reference."},
)


def round319_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND319_CASE_CANDIDATES]


def round319_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND319_CASE_CANDIDATES]


def round319_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND319_TRIGGER_RECORDS]


def round319_shadow_weight_rows() -> list[dict[str, str]]:
    return [dict(row) for row in ROUND319_SHADOW_WEIGHT_ROWS]


def round319_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND319_REQUIRED_TARGET_ALIASES.items()]


def round319_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND319_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND319_SCORE_DOWN_AXES]
    )


def round319_summary() -> dict[str, object]:
    return {
        "source_round": ROUND319_SOURCE_ROUND_PATH,
        "round_id": ROUND319_ANALYST_ROUND_ID,
        "large_sector": ROUND319_LARGE_SECTOR,
        "method": ROUND319_METHOD,
        "case_candidate_count": len(ROUND319_CASE_CANDIDATES),
        "trigger_count": len(ROUND319_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND319_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 4,
        "stage2_candidate_count": 6,
        "stage3_yellow_candidate_count": 5,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 6,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 2,
        "evidence_good_but_price_failed_or_unavailable_count": 4,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R12 Loop 16",
    }


def round319_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND319_SOURCE_ROUND_PATH,
        "round_id": ROUND319_ANALYST_ROUND_ID,
        "large_sector": ROUND319_LARGE_SECTOR,
        "method": ROUND319_METHOD,
        "summary": round319_summary(),
        "required_target_aliases": dict(ROUND319_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND319_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND319_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND319_STAGE3_GREEN_RULES,
        "green_blockers": ROUND319_GREEN_BLOCKERS,
        "score_up_axes": ROUND319_SCORE_UP_AXES,
        "score_down_axes": ROUND319_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND319_STAGE4B_WATCH_TRIGGERS,
        "hard_4c_gates": ROUND319_HARD_4C_GATES,
        "row_separation_rules": ROUND319_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round319_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_policy_defense_nuclear_disaster_or_market_integrity_headline_as_Green_without_law_contract_budget_delivery_margin_ROIC_or_company_execution",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round319_summary_markdown() -> str:
    summary = round319_summary()
    lines = [
        "# R11 Loop 16 Policy / Geopolitics / Disaster / Event Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: Commercial Act reform can be Stage2 policy evidence, but it is not Green until actual company board action, buyback cancellation or dividend policy appears.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Hanwha Aerospace / Romania K9 is the cleanest Stage2-Actionable defense export case, with dilution 4B attached.",
            "- LIG Nex1 / Iraq and Iran validation is a Stage3-Yellow candidate, not Green before production and margin.",
            "- KHNP / Czech nuclear is Stage2 with legal 4B after EDF court challenge.",
            "- Martial law political shock is broad hard 4C.",
            "- Commercial Act / Value-Up is Stage2 policy reform until company-specific execution appears.",
            "- Samsung SDS / KKR is Stage2-Actionable foreign strategic capital with CB dilution 4B.",
            "- Short-selling market integrity is Stage2 plus liquidity/foreign-flow 4B.",
            "- 2025 wildfires are disaster hard 4C reference, not automatic listed-company Stage2.",
            "- Stage3-Green confirmed: `0`.",
            "- Hard 4C confirmed: `2`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round319_trigger_grid_markdown() -> str:
    lines = [
        "# Round 319 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round319_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round319_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 319 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND319_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND319_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND319_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND319_GREEN_BLOCKERS),
            "",
            "## Hard 4C Gates",
            *_bullet_lines(ROUND319_HARD_4C_GATES),
        ]
    ) + "\n"


def render_round319_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 319 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND319_STAGE4B_WATCH_TRIGGERS),
        "",
        "## Hard 4C Gates",
        *_bullet_lines(ROUND319_HARD_4C_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND319_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round319_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 319 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND319_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round319_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 319 Row Separation Plan",
        "",
        "Policy, defense, nuclear, disaster and market-integrity headlines must be separated from trigger anchors and full OHLC windows.",
        "",
        "Easy example: a wildfire can create reconstruction demand, but it is not a listed-company Stage2 until a company contract or insurance-loss bridge appears.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND319_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round319_r11_loop16_reports(
    output_directory: str | Path = ROUND319_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND319_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND319_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND319_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND319_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round319_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND319_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round319_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round319_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round319_r11_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round319_r11_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round319_r11_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round319_r11_loop16_trigger_grid.md",
        "summary": output_dir / "round319_r11_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round319_r11_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round319_r11_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round319_r11_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round319_r11_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round319_r11_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round319_r11_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round319_case_rows())
    _write_csv(paths["target_aliases"], round319_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round319_trigger_rows())
    _write_csv(paths["score_adjustments"], round319_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round319_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round319_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round319_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round319_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round319_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round319_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round319_row_separation_plan_markdown(), encoding="utf-8")
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
    "ROUND319_CASE_CANDIDATES",
    "ROUND319_GREEN_BLOCKERS",
    "ROUND319_HARD_4C_GATES",
    "ROUND319_LARGE_SECTOR",
    "ROUND319_REQUIRED_TARGET_ALIASES",
    "ROUND319_ROW_SEPARATION_RULES",
    "ROUND319_SCORE_DOWN_AXES",
    "ROUND319_SCORE_UP_AXES",
    "ROUND319_SHADOW_WEIGHT_ROWS",
    "ROUND319_STAGE2_ACTIONABLE_RULES",
    "ROUND319_STAGE3_GREEN_RULES",
    "ROUND319_STAGE3_YELLOW_RULES",
    "ROUND319_STAGE4B_WATCH_TRIGGERS",
    "ROUND319_TRIGGER_RECORDS",
    "render_round319_stage4b_4c_review_markdown",
    "render_round319_stage_rules_markdown",
    "render_round319_trigger_grid_markdown",
    "round319_audit_payload",
    "round319_case_records",
    "round319_case_rows",
    "round319_shadow_weight_rows",
    "round319_summary",
    "round319_trigger_rows",
    "write_round319_r11_loop16_reports",
]
