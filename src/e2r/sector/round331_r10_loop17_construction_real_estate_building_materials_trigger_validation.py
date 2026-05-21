"""Round-331 R10 Loop-17 construction and real-estate validation.

This module converts ``docs/round/round_331.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a 6B USD overseas EPC contract can be Stage2-Actionable when
the stock reacts. It still cannot become Green until margin, progress billing,
schedule and cash collection are visible as of the replay date.
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


ROUND331_SOURCE_ROUND_PATH = "docs/round/round_331.md"
ROUND331_ANALYST_ROUND_ID = "round_259"
ROUND331_LOOP_NAME = "R10 Loop 17"
ROUND331_LARGE_SECTOR = "CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS"
ROUND331_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND331_DEFAULT_OUTPUT_DIRECTORY = (
    "output/e2r_round331_r10_loop17_construction_real_estate_building_materials_trigger_validation"
)
ROUND331_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop17_round259.jsonl"
ROUND331_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r10_loop17_round259.jsonl"
ROUND331_DEFAULT_AUDIT_PATH = (
    "data/sector_taxonomy/round331_r10_loop17_construction_real_estate_building_materials_trigger_validation_audit.json"
)
ROUND331_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round259_r10_loop17_v1.csv"

ROUND331_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE": E2RArchetype.OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE.value,
    "NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B": E2RArchetype.NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B.value,
    "HOUSING_SUPPLY_RECONSTRUCTION_POLICY_STAGE2_NO_PRICE": E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_POLICY_STAGE2_NO_PRICE.value,
    "REAL_ESTATE_PF_RESTRUCTURING_4B": E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4B.value,
    "CONSTRUCTION_HOLDCO_VALUEUP_FAILED_RERATING": E2RArchetype.CONSTRUCTION_HOLDCO_VALUEUP_FAILED_RERATING.value,
    "CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE": E2RArchetype.CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE.value,
    "BUILDER_LIQUIDITY_SUPPORT_STAGE2_RELIEF": E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_STAGE2_RELIEF.value,
}

ROUND331_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_at_least_5pct_or_market_relative_return_at_least_5pp",
    "contract_policy_support_or_deal_value_is_numeric",
    "revenue_path_connects_to_EPC_backlog_progress_billing_pre_sale_cash_PF_rollover_rental_or_yield",
    "cost_schedule_PF_safety_or_legal_4B_is_identified",
    "price_reaction_aligns_with_evidence",
    "not_just_preferred_bidder_final_contract_or_high_probability_conversion_path_exists",
    "recurring_margin_or_cash_conversion_path_exists",
)

ROUND331_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "EPC_progress_billing_margin_and_receivables_are_visible",
    "nuclear_final_contract_scope_and_legal_clearance_are_visible",
    "housing_policy_converts_to_permits_pre_sales_and_builder_backlog",
    "PF_restructuring_shows_bad_project_cleanup_and_refinancing",
    "builder_liquidity_support_converts_to_pre_sale_cash_recovery",
    "valueup_case_has_board_action_or_is_capped_below_Green",
    "construction_safety_case_has_regulatory_closure_before_positive_recovery",
)

ROUND331_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "Stage2_trigger_converts_into_recurring_EPS_OP_or_FCF",
    "contract_or_policy_trigger_has_margin_cash_collection_and_schedule_evidence",
    "PF_or_liquidity_relief_has_loss_cleanup_and_refinancing_evidence",
    "legal_safety_and_governance_4B_risks_are_reduced",
    "full_window_adjusted_OHLC_MFE_MAE_is_available_and_supportive",
)

ROUND331_GREEN_BLOCKERS: tuple[str, ...] = (
    "preferred_bidder_without_final_contract",
    "policy_without_builder_price",
    "liquidity_support_without_loss_cleanup",
    "overseas_EPC_without_margin_visibility",
    "valueup_without_board_action",
    "construction_safety_ignored",
    "housing_price_rally_without_affordability",
    "rate_cut_hope_without_refinancing",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND331_SCORE_UP_AXES: tuple[str, ...] = (
    "overseas_EPC_contract_value",
    "market_relative_contract_reaction",
    "nuclear_infra_EPC_optionality",
    "housing_supply_policy",
    "PF_restructuring_recognition",
    "liquidity_relief",
    "capital_return_governance",
    "construction_safety_risk",
)

ROUND331_SCORE_DOWN_AXES: tuple[str, ...] = (
    "preferred_bidder_without_final_contract_penalty",
    "policy_without_builder_price_penalty",
    "liquidity_support_without_loss_cleanup_penalty",
    "overseas_EPC_without_margin_visibility_penalty",
    "valueup_without_board_action_penalty",
    "construction_safety_ignored_penalty",
    "rate_cut_hope_without_refinancing_penalty",
)

ROUND331_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "preferred_bidder_premium_before_final_contract",
    "legal_appeal_or_competition_review_delay",
    "policy_without_builder_price_or_pre_sales",
    "liquidity_support_without_bad_project_cleanup",
    "overseas_EPC_contract_before_margin_and_cash_conversion",
    "activist_valueup_failure_or_board_action_missing",
    "rate_cut_hope_without_refinancing",
)

ROUND331_HARD_4C_GATES: tuple[str, ...] = (
    "fatal_construction_collapse",
    "work_suspension_or_regulatory_sanction",
    "contract_cancellation_or_schedule_failure",
    "PF_default_cascade_or_builder_workout",
    "legal_block_on_nuclear_final_contract",
    "governance_vote_blocks_valueup_and_price_breaks",
)

ROUND331_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_reported_event_contract_policy_support_legal_safety_or_valueup_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
    "do_not_treat_construction_headline_as_Green_without_margin_final_contract_permits_PF_cleanup_board_action_or_safety_clearance",
)


@dataclass(frozen=True)
class Round331TriggerRecord:
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
class Round331ShadowWeightRow:
    archetype: E2RArchetype
    overseas_epc_contract_value: int
    market_relative_contract_reaction: int
    nuclear_infra_epc_optionality: int
    housing_supply_policy: int
    pf_restructuring_recognition: int
    liquidity_relief: int
    capital_return_governance: int
    construction_safety_risk: int
    preferred_bidder_without_final_contract_penalty: int
    policy_without_builder_price_penalty: int
    liquidity_support_without_loss_cleanup_penalty: int
    overseas_epc_without_margin_visibility_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "overseas_EPC_contract_value": _signed(self.overseas_epc_contract_value),
            "market_relative_contract_reaction": _signed(self.market_relative_contract_reaction),
            "nuclear_infra_EPC_optionality": _signed(self.nuclear_infra_epc_optionality),
            "housing_supply_policy": _signed(self.housing_supply_policy),
            "PF_restructuring_recognition": _signed(self.pf_restructuring_recognition),
            "liquidity_relief": _signed(self.liquidity_relief),
            "capital_return_governance": _signed(self.capital_return_governance),
            "construction_safety_risk": _signed(self.construction_safety_risk),
            "preferred_bidder_without_final_contract_penalty": _signed(self.preferred_bidder_without_final_contract_penalty),
            "policy_without_builder_price_penalty": _signed(self.policy_without_builder_price_penalty),
            "liquidity_support_without_loss_cleanup_penalty": _signed(self.liquidity_support_without_loss_cleanup_penalty),
            "overseas_EPC_without_margin_visibility_penalty": _signed(self.overseas_epc_without_margin_visibility_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round331CaseCandidate:
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
            "do_not_use_round331_cases_as_candidate_generation_input",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_construction_headline_as_Green_without_margin_final_contract_permits_PF_cleanup_board_action_or_safety_clearance",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")

        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "legal" in field
            or "PF" in field
            or "margin" in field
            or "support" in field
            or "board" in field
            or "policy" in field
            or "contract" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "fatal" in field
            or "collapse" in field
            or "safety" in field
            or "default" in field
            or "workout" in field
            or "sanction" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND331_LARGE_SECTOR,
            large_sector=ROUND331_LARGE_SECTOR,
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
            must_have_fields=ROUND331_STAGE3_GREEN_RULES,
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


ROUND331_CASE_CANDIDATES: tuple[Round331CaseCandidate, ...] = (
    Round331CaseCandidate(
        "r10_loop17_samsung_ena_fadhili_epc",
        "028050",
        "Samsung E&A",
        E2RArchetype.OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE,
        (E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE, E2RArchetype.MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE),
        "success_candidate",
        "Stage2_Actionable_overseas_EPC_mega_contract",
        "r10l17_samsung_ena_fadhili_T1",
        "Stage2-Actionable_overseas_EPC_mega_contract",
        "Stage2-Actionable",
        date(2024, 4, 3),
        date(2024, 4, 3),
        None,
        date(2024, 4, 3),
        None,
        False,
        ("Fadhili_gas_project_contract_usd_6B", "total_project_usd_7_7B", "event_return_plus_8_5pct", "market_relative_plus_9_9pp", "event_price_krw_26750", "gas_capacity_up_60pct", "capacity_4bcf_per_day", "completion_2027_11"),
        ("cost_overrun_4B", "schedule_delay_4B", "change_order_4B", "receivables_4B", "EPC_margin_visibility_missing", "full_OHLC_MFE_MAE_missing"),
        {"trigger_date": "2024-04-03", "contract_value_usd_bn": 6.0, "total_project_value_usd_bn": 7.7, "event_return_pct": 8.5, "event_price_krw": 26750, "kospi_return_pct": -1.4, "market_relative_return_pp": 9.9, "gas_capacity_increase_pct": 60, "capacity_bcf_per_day": 4, "completion_target": "2027-11"},
        "aligned",
        "excellent_stage2_actionable_overseas_EPC_contract",
        "event_premium",
        "stage2_watch_success",
        "A 6B USD EPC contract and +8.5% reaction support Stage2-Actionable, but Green needs progress billing, EPC margin and cash collection.",
    ),
    Round331CaseCandidate(
        "r10_loop17_czech_nuclear_epc",
        "034020/051600/052690/015760",
        "Doosan Enerbility / KEPCO Plant S&E / KEPCO E&C / KEPCO readthrough",
        E2RArchetype.NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B,
        (E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B, E2RArchetype.NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2),
        "success_candidate",
        "Stage2_nuclear_EPC_preferred_bidder_legal_4B",
        "r10l17_czech_nuclear_T1",
        "Stage2_nuclear_EPC_preferred_bidder",
        "Stage2_promote_candidate + 4B-watch",
        date(2024, 7, 17),
        date(2024, 7, 17),
        None,
        date(2024, 10, 1),
        None,
        False,
        ("Czech_nuclear_preferred_bidder", "Doosan_3m_plus_48pct", "KEPCO_Plant_plus_14pct", "KEPCO_EC_3m_plus_41pct", "unit_cost_czk_200B", "unit_cost_usd_8_65B"),
        ("final_contract_not_signed_4B", "EDF_Westinghouse_appeals_4B", "Czech_watchdog_review_4B", "court_challenge_4B", "margin_scope_uncertainty_4B"),
        {"trigger_date": "2024-07-17", "doosan_3m_return_pct": 48, "kepco_plant_event_return_pct": 14, "kepco_ec_3m_return_pct": 41, "unit_cost_czk_bn": 200, "unit_cost_usd_bn": 8.65, "legal_window": "2024-10_to_2025"},
        "aligned",
        "nuclear_stage2_with_legal_4B",
        "policy_event_rerating",
        "stage2_watch_success",
        "Preferred nuclear bidder evidence can promote Stage2, while final contract, legal clearance, scope and margin remain 4B gates.",
    ),
    Round331CaseCandidate(
        "r10_loop17_seoul_housing_supply_reconstruction",
        "000720/006360/047040/028050/294870/builder_basket",
        "Seoul housing supply and reconstruction builder basket",
        E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_POLICY_STAGE2_NO_PRICE,
        (E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY, E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_WITH_LTV_4B),
        "success_candidate",
        "Stage2_housing_supply_policy_no_price",
        "r10l17_housing_supply_T1",
        "Stage2_housing_supply_policy_no_price",
        "Stage2 no-price",
        date(2024, 8, 1),
        date(2024, 8, 1),
        None,
        date(2025, 9, 7),
        None,
        False,
        ("Seoul_home_price_plus_0_76pct", "housing_supply_target_400k_plus", "Gangnam_Yongsan_focus", "LTV_cut_to_40pct_from_50pct", "reconstruction_streamlining"),
        ("mortgage_tightening_4B", "household_debt_4B", "PF_funding_4B", "pre_sale_absorption_missing", "direct_builder_price_unavailable"),
        {"trigger_date": "2024-08_to_2025-09", "seoul_home_price_weekly_pct": 0.76, "housing_supply_target_units": 400000, "ltv_after_pct": 40, "ltv_before_pct": 50, "direct_builder_price_anchor": "unavailable"},
        "unknown",
        "Stage2_housing_policy_no_price",
        "policy_event_rerating",
        "stage2_watch_success",
        "Housing supply policy can create Stage2 monitoring, but builder price, permits, pre-sales and cash conversion are missing.",
    ),
    Round331CaseCandidate(
        "r10_loop17_real_estate_pf_restructuring",
        "009410/000720/006360/047040/PF_exposed_builder_basket",
        "Taeyoung / large builder PF-exposed basket",
        E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4B,
        (E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH, E2RArchetype.PF_LIQUIDITY_RESTRUCTURING_4C_AND_RELIEF),
        "4b_watch",
        "4B_real_estate_PF_restructuring_relief",
        "r10l17_pf_restructuring_T2",
        "4B_real_estate_PF_restructuring",
        "4B with relief",
        date(2023, 12, 1),
        None,
        None,
        date(2024, 5, 13),
        None,
        False,
        ("builder_support_krw_40_6T", "PF_delinquency_2022_0_37pct", "PF_delinquency_2023_1_19pct", "PF_delinquency_2024_2_70pct", "syndicated_loan_from_1T_to_5T"),
        ("bad_project_cleanup_missing_4B", "PF_refinancing_4B", "loss_recognition_4B", "PF_default_cascade_4C", "direct_price_unavailable"),
        {"support_package_krw_trn": 40.6, "pf_delinquency_2022_pct": 0.37, "pf_delinquency_2023_pct": 1.19, "pf_delinquency_2024_pct": 2.70, "syndicated_loan_before_krw_trn": 1, "syndicated_loan_after_krw_trn": 5},
        "aligned",
        "PF_restructuring_4B_relief_not_Green",
        "credit_relief_rally",
        "stage2_watch_success",
        "PF support and restructuring are visible, but rising delinquency, cleanup and refinancing keep this in 4B relief rather than Green.",
    ),
    Round331CaseCandidate(
        "r10_loop17_samsung_ct_valueup_failed",
        "028260",
        "Samsung C&T",
        E2RArchetype.CONSTRUCTION_HOLDCO_VALUEUP_FAILED_RERATING,
        (E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN, E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY),
        "failed_rerating",
        "failed_rerating_holdco_valueup",
        "r10l17_samsung_ct_valueup_T1",
        "failed_valueup_governance_vote",
        "failed_rerating + 4B-watch",
        date(2024, 3, 15),
        None,
        None,
        date(2024, 3, 15),
        None,
        False,
        ("activist_proposal_failed", "almost_minus_10pct_event_reaction", "higher_dividend_and_buyback_requested", "NPS_sided_with_management"),
        ("holding_discount_4B", "board_control_4B", "weak_capital_return_4B", "governance_discount_persists", "board_action_missing"),
        {"trigger_date": "2024-03-15", "event_return_label": "almost_-10", "activist_proposal": "failed", "NPS_vote": "management"},
        "evidence_good_but_price_failed",
        "valueup_failed_rerating",
        "no_rerating",
        "should_have_been_red",
        "Value-up evidence failed when governance vote blocked the rerating path and the stock reaction was almost -10%.",
    ),
    Round331CaseCandidate(
        "r10_loop17_highway_construction_collapse_safety",
        "Hyundai_Engineering_private/construction_safety_basket",
        "Highway construction collapse safety case",
        E2RArchetype.CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE,
        (E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C, E2RArchetype.CONSTRUCTION_QUALITY_SAFETY_HARD_4C),
        "4c_thesis_break",
        "hard_4C_construction_site_safety_no_public_price",
        "r10l17_highway_collapse_T0",
        "hard_4C_construction_safety",
        "sector/project hard 4C",
        date(2025, 2, 25),
        None,
        None,
        None,
        date(2025, 2, 25),
        True,
        ("fatal_construction_collapse", "fatalities_at_least_3_to_4", "injured_6", "several_critical", "five_50m_steel_support_structures", "public_stock_unavailable"),
        ("investigation_4C", "work_suspension_4C", "penalty_4C", "bidding_restriction_4C", "site_brand_damage_4C", "listed_stock_price_anchor_unavailable"),
        {"trigger_date": "2025-02-25", "fatalities_context": "at_least_3_to_4", "injured": 6, "critical_injuries": "several", "steel_support_structures": 5, "steel_support_height_m": 50, "public_stock_anchor": "unavailable"},
        "unknown",
        "hard_4C_success_construction_safety_no_public_price",
        "thesis_break",
        "should_have_been_red",
        "Fatal construction collapse is a hard 4C safety case; without a listed-stock anchor, it remains sector/project monitoring evidence.",
    ),
    Round331CaseCandidate(
        "r10_loop17_builder_liquidity_rate_relief",
        "builder_basket/banks_PF_readthrough",
        "Builder liquidity and rate-relief basket",
        E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_STAGE2_RELIEF,
        (E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH, E2RArchetype.PF_RESTRUCTURING_RELIEF_KOREA),
        "success_candidate",
        "Stage2_builder_liquidity_rate_relief",
        "r10l17_builder_liquidity_T1",
        "Stage2_builder_liquidity_relief",
        "Stage2 relief",
        date(2024, 3, 27),
        date(2024, 3, 27),
        None,
        date(2026, 2, 1),
        None,
        False,
        ("builder_support_krw_40_6T", "BOK_policy_rate_hold_2_50pct", "expected_rate_2_50pct", "liquidity_support_package", "PF_readthrough"),
        ("FX_weakness_4B", "housing_overheating_4B", "PF_refinancing_missing_4B", "construction_weakness_4B", "pre_sale_absorption_missing", "direct_price_unavailable"),
        {"trigger_date": "2024-03-27", "support_package_krw_trn": 40.6, "BOK_policy_rate_pct": 2.5, "expected_rate_pct": 2.5, "direct_price_anchor": "unavailable"},
        "unknown",
        "Stage2_relief_not_Green",
        "credit_relief_rally",
        "stage2_watch_success",
        "Liquidity support and rate context support Stage2 relief, but refinancing, pre-sale cash and bad-project cleanup are required before Green.",
    ),
)

ROUND331_TRIGGER_RECORDS: tuple[Round331TriggerRecord, ...] = (
    Round331TriggerRecord("r10l17_samsung_ena_fadhili_T1", "r10_loop17_samsung_ena_fadhili_epc", "Stage2-Actionable_overseas_EPC_mega_contract", "2024-04-03", "Samsung E&A won a 6B USD Fadhili gas contract; KOSPI fell while the stock rose.", 8.5, "excellent_stage2_actionable_overseas_EPC_contract", "Stage2-Actionable", {"event_price_krw": 26750, "market_relative_return_pp": 9.9, "contract_value_usd_bn": 6.0}),
    Round331TriggerRecord("r10l17_czech_nuclear_T1", "r10_loop17_czech_nuclear_epc", "Stage2_nuclear_EPC_preferred_bidder", "2024-07-17", "Czech nuclear preferred-bidder result drove Doosan/KEPCO-related rerating.", "Doosan_3m_+48_KEPCO_EC_3m_+41", "nuclear_stage2_with_legal_4B", "Stage2_promote_candidate", {"doosan_3m_return_pct": 48, "kepco_ec_3m_return_pct": 41, "unit_cost_usd_bn": 8.65}),
    Round331TriggerRecord("r10l17_czech_legal_T3", "r10_loop17_czech_nuclear_epc", "4B_nuclear_legal_final_contract_gate", "2024-10_to_2025", "Final contract, EDF/Westinghouse appeals and Czech review remained unresolved.", "price_data_unavailable_after_deep_search", "legal_4B_watch", "4B-watch", {"appeal_sources": ["EDF", "Westinghouse"], "final_contract_signed": False}),
    Round331TriggerRecord("r10l17_housing_supply_T1", "r10_loop17_seoul_housing_supply_reconstruction", "Stage2_housing_policy_no_price", "2024-08_to_2025-09", "Seoul housing acceleration, 400k+ supply target and LTV tightening were visible.", "price_data_unavailable_after_deep_search", "housing_policy_stage2_no_price", "Stage2", {"seoul_home_price_weekly_pct": 0.76, "housing_supply_target_units": 400000, "ltv_after_pct": 40}),
    Round331TriggerRecord("r10l17_pf_support_T1", "r10_loop17_builder_liquidity_rate_relief", "Stage2_builder_liquidity_relief", "2024-03-27", "40.6T won builder support and rate context created relief monitoring.", "price_data_unavailable_after_deep_search", "builder_liquidity_stage2_relief", "Stage2_relief", {"support_package_krw_trn": 40.6, "BOK_policy_rate_pct": 2.5}),
    Round331TriggerRecord("r10l17_pf_restructuring_T2", "r10_loop17_real_estate_pf_restructuring", "4B_PF_restructuring_relief", "2024-05-13", "PF delinquency and restructuring support were visible; cleanup and refinancing remained open.", "price_data_unavailable_after_deep_search", "PF_restructuring_4B_relief", "4B-watch", {"pf_delinquency_2024_pct": 2.70, "syndicated_loan_after_krw_trn": 5}),
    Round331TriggerRecord("r10l17_samsung_ct_valueup_T1", "r10_loop17_samsung_ct_valueup_failed", "failed_valueup_governance_vote", "2024-03-15", "Activist value-up proposal failed and Samsung C&T reacted almost -10%.", "almost_-10", "valueup_failed_rerating", "no_actionable", {"activist_proposal": "failed", "NPS_vote": "management"}),
    Round331TriggerRecord("r10l17_highway_collapse_T0", "r10_loop17_highway_construction_collapse_safety", "hard_4C_construction_safety", "2025-02-25", "Fatal construction collapse, work-safety investigation and unavailable listed-stock anchor.", "price_data_unavailable_after_deep_search", "hard_4C_success_construction_safety", "4C_sector_watch", {"fatalities_context": "at_least_3_to_4", "injured": 6, "steel_support_height_m": 50}),
    Round331TriggerRecord("r10l17_builder_liquidity_T1", "r10_loop17_builder_liquidity_rate_relief", "Stage2_builder_liquidity_relief", "2024-03-27", "Builder support and BOK rate hold created relief, not a Green signal.", "price_data_unavailable_after_deep_search", "Stage2_relief_not_Green", "Stage2_relief", {"support_package_krw_trn": 40.6, "BOK_policy_rate_pct": 2.5, "expected_rate_pct": 2.5}),
)

ROUND331_SHADOW_WEIGHT_ROWS: tuple[Round331ShadowWeightRow, ...] = (
    Round331ShadowWeightRow(E2RArchetype.OVERSEAS_EPC_MEGA_CONTRACT_STAGE2_ACTIONABLE, 5, 5, 0, 0, 0, 0, 0, 1, -1, -1, -1, -4, "Samsung E&A $6B +8.5 vs KOSPI -1.4", "cost/schedule margin missing", "progress billing+margin+cost control", "Samsung E&A."),
    Round331ShadowWeightRow(E2RArchetype.NUCLEAR_INFRA_EPC_STAGE2_WITH_LEGAL_4B, 2, 3, 5, 0, 0, 1, 0, 1, -5, -1, -1, -3, "Czech nuclear preferred bidder drove sector rerating", "final contract/legal 4B", "final contract+scope+margin", "Doosan/KEPCO E&C."),
    Round331ShadowWeightRow(E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_POLICY_STAGE2_NO_PRICE, 0, 0, 0, 5, 2, 2, 0, 1, -1, -4, -2, -1, "Seoul supply/reconstruction policy", "price/pre-sale missing", "permits+pre-sales+backlog", "builder basket."),
    Round331ShadowWeightRow(E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4B, 0, 0, 0, 1, 5, 4, 0, 1, -1, -2, -5, -1, "PF delinquency 2.70% and restructuring", "relief not Green", "bad-project cleanup+refinancing", "PF basket."),
    Round331ShadowWeightRow(E2RArchetype.CONSTRUCTION_HOLDCO_VALUEUP_FAILED_RERATING, 0, 0, 0, 0, 1, 0, 5, 0, -1, -1, -1, -1, "Samsung C&T activist failure -10", "board action missing", "board-approved return+cancellation", "Samsung C&T."),
    Round331ShadowWeightRow(E2RArchetype.CONSTRUCTION_SITE_SAFETY_HARD_4C_NO_PUBLIC_PRICE, 0, 0, 0, 0, 1, 0, 0, 5, -1, -1, -1, -1, "fatal construction collapse", "listed price unavailable", "regulatory closure+penalty visibility", "sector safety."),
    Round331ShadowWeightRow(E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_STAGE2_RELIEF, 0, 0, 0, 2, 4, 5, 0, 1, -1, -2, -5, -1, "40.6T builder support", "PF rollover/pre-sale missing", "refinancing+cash conversion", "builder basket."),
)


def round331_case_records() -> tuple[E2RCaseRecord, ...]:
    records = tuple(candidate.to_case_record() for candidate in ROUND331_CASE_CANDIDATES)
    for record in records:
        record.validate()
    return records


def round331_case_rows() -> list[dict[str, str]]:
    return [candidate.as_row() for candidate in ROUND331_CASE_CANDIDATES]


def round331_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND331_TRIGGER_RECORDS]


def round331_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND331_SHADOW_WEIGHT_ROWS]


def round331_summary() -> dict[str, object]:
    return {
        "source_round": ROUND331_SOURCE_ROUND_PATH,
        "round_id": ROUND331_ANALYST_ROUND_ID,
        "loop_name": ROUND331_LOOP_NAME,
        "large_sector": ROUND331_LARGE_SECTOR,
        "method": ROUND331_METHOD,
        "case_candidate_count": len(ROUND331_CASE_CANDIDATES),
        "trigger_count": len(ROUND331_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND331_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": sum(1 for case in ROUND331_CASE_CANDIDATES if "Stage2-Actionable" in case.stage_candidate),
        "stage2_candidate_count": sum(1 for case in ROUND331_CASE_CANDIDATES if "Stage2" in case.stage_candidate),
        "stage3_yellow_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": sum(1 for case in ROUND331_CASE_CANDIDATES if case.stage4b_date is not None),
        "hard_4c_case_count": sum(1 for case in ROUND331_CASE_CANDIDATES if case.hard_4c_confirmed),
        "price_unavailable_count": sum(1 for case in ROUND331_CASE_CANDIDATES if case.score_price_alignment == "unknown"),
        "evidence_good_but_price_failed_count": sum(1 for case in ROUND331_CASE_CANDIDATES if case.score_price_alignment == "evidence_good_but_price_failed"),
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R11 Loop 17",
    }


def round331_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND331_SOURCE_ROUND_PATH,
        "round_id": ROUND331_ANALYST_ROUND_ID,
        "large_sector": ROUND331_LARGE_SECTOR,
        "method": ROUND331_METHOD,
        "summary": round331_summary(),
        "target_archetypes": dict(ROUND331_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND331_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND331_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND331_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND331_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND331_SCORE_UP_AXES),
        "score_down_axes": list(ROUND331_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND331_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND331_HARD_4C_GATES),
        "row_separation_rules": list(ROUND331_ROW_SEPARATION_RULES),
        "shadow_weights": round331_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_change_production_scoring",
            "do_not_use_round331_cases_as_candidate_generation_input",
            "do_not_force_Stage3_Green",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_construction_headline_as_Green_without_margin_final_contract_permits_PF_cleanup_board_action_or_safety_clearance",
        ],
    }


def render_round331_summary_markdown() -> str:
    summary = round331_summary()
    lines = [
        "# Round 331 R10 Loop 17 Construction Real Estate Building Materials Trigger Validation",
        "",
        f"- source_round: `{ROUND331_SOURCE_ROUND_PATH}`",
        f"- analyst_round_id: `{ROUND331_ANALYST_ROUND_ID}`",
        f"- large_sector: `{ROUND331_LARGE_SECTOR}`",
        f"- method: `{ROUND331_METHOD}`",
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
        "- Samsung E&A Fadhili is Stage2-Actionable, but EPC margin, progress billing and cash collection are Green gates.",
        "- Czech nuclear is Stage2 with legal 4B. Preferred bidder evidence is not the same as final-contract cash flow.",
        "- Seoul housing policy is Stage2 no-price. Builder permits, pre-sales and cash conversion are required.",
        "- PF restructuring and builder liquidity are relief paths, not Green, until bad-project cleanup and refinancing are visible.",
        "- Samsung C&T value-up failed when board/governance action did not convert into shareholder-return evidence.",
        "- Fatal construction-site safety is a hard 4C risk case even when public stock-price anchor is unavailable.",
    ]
    return "\n".join(lines) + "\n"


def render_round331_trigger_grid_markdown() -> str:
    lines = [
        "# Round 331 R10 Loop 17 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | date | event_return | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round331_trigger_rows():
        lines.append(
            f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |"
        )
    return "\n".join(lines) + "\n"


def render_round331_stage_rules_markdown() -> str:
    sections = [
        ("Stage2-Actionable Rules", ROUND331_STAGE2_ACTIONABLE_RULES),
        ("Stage3-Yellow Rules", ROUND331_STAGE3_YELLOW_RULES),
        ("Stage3-Green Rules", ROUND331_STAGE3_GREEN_RULES),
        ("Green Blockers", ROUND331_GREEN_BLOCKERS),
        ("Score Up Axes", ROUND331_SCORE_UP_AXES),
        ("Score Down Axes", ROUND331_SCORE_DOWN_AXES),
        ("Row Separation Rules", ROUND331_ROW_SEPARATION_RULES),
    ]
    lines = ["# Round 331 R10 Loop 17 Stage Rules", "", "Do not apply these weights to production scoring yet.", ""]
    for title, values in sections:
        lines.extend([f"## {title}", ""])
        lines.extend(f"- `{value}`" for value in values)
        lines.append("")
    return "\n".join(lines)


def render_round331_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 331 R10 Loop 17 Stage 4B / 4C Review", "", "## 4B Watch", ""]
    lines.extend(f"- `{item}`" for item in ROUND331_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- `{item}`" for item in ROUND331_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND331_CASE_CANDIDATES:
        lines.append(f"- `{case.case_id}`: {case.stage_candidate}; {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round331_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 331 R10 Loop 17 Price Validation Plan",
        "",
        "Full adjusted OHLC is not complete. Reported event anchors are retained, but MFE/MAE, peak and drawdown are not invented.",
        "",
        "| case_id | status | event anchor | next backfill |",
        "| --- | --- | --- | --- |",
    ]
    for case in ROUND331_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | price_data_unavailable_after_deep_search | {json.dumps(case.extra_price_metrics, ensure_ascii=False, sort_keys=True)} | adjusted OHLC backfill required |"
        )
    return "\n".join(lines) + "\n"


def write_round331_r10_loop17_reports(
    *,
    output_directory: str | Path = ROUND331_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND331_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND331_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND331_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND331_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    cases_path = Path(cases_path)
    triggers_path = Path(triggers_path)
    audit_path = Path(audit_path)
    weight_profile_path = Path(weight_profile_path)

    cases = write_case_library(round331_case_records(), cases_path)
    triggers = _write_jsonl(triggers_path, (trigger.as_dict() for trigger in ROUND331_TRIGGER_RECORDS))
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(json.dumps(round331_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    weights = _write_csv(weight_profile_path, round331_shadow_weight_rows())

    paths = {
        "cases": cases,
        "triggers": triggers,
        "audit": audit_path,
        "weight_profile": weights,
        "case_rows_csv": output_directory / "case_rows.csv",
        "trigger_rows_csv": output_directory / "trigger_rows.csv",
        "summary": output_directory / "round331_summary.md",
        "trigger_grid_md": output_directory / "trigger_grid.md",
        "stage_rules": output_directory / "stage_rules.md",
        "stage4b_4c_review": output_directory / "stage4b_4c_review.md",
        "price_validation_plan": output_directory / "price_validation_plan.md",
    }
    _write_csv(paths["case_rows_csv"], round331_case_rows())
    _write_csv(paths["trigger_rows_csv"], round331_trigger_rows())
    paths["summary"].write_text(render_round331_summary_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round331_trigger_grid_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round331_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round331_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round331_price_validation_plan_markdown(), encoding="utf-8")
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
    "ROUND331_CASE_CANDIDATES",
    "ROUND331_GREEN_BLOCKERS",
    "ROUND331_HARD_4C_GATES",
    "ROUND331_LARGE_SECTOR",
    "ROUND331_REQUIRED_TARGET_ALIASES",
    "ROUND331_ROW_SEPARATION_RULES",
    "ROUND331_SCORE_DOWN_AXES",
    "ROUND331_SCORE_UP_AXES",
    "ROUND331_SHADOW_WEIGHT_ROWS",
    "ROUND331_STAGE2_ACTIONABLE_RULES",
    "ROUND331_STAGE3_GREEN_RULES",
    "ROUND331_STAGE3_YELLOW_RULES",
    "ROUND331_STAGE4B_WATCH_TRIGGERS",
    "ROUND331_TRIGGER_RECORDS",
    "render_round331_stage4b_4c_review_markdown",
    "render_round331_stage_rules_markdown",
    "render_round331_trigger_grid_markdown",
    "round331_audit_payload",
    "round331_case_records",
    "round331_case_rows",
    "round331_shadow_weight_rows",
    "round331_summary",
    "round331_trigger_rows",
    "write_round331_r10_loop17_reports",
]
