"""Round-318 R10 Loop-16 construction, real-estate and materials validation.

This module converts ``docs/round/round_318.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: Samsung E&A's Fadhili contract has contract value and price
reaction, so it can be Stage2-Actionable. It is still not Stage3-Green until
EPC margin, working capital, cash collection and execution progress are visible.
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


ROUND318_SOURCE_ROUND_PATH = "docs/round/round_318.md"
ROUND318_ANALYST_ROUND_ID = "round_246"
ROUND318_LARGE_SECTOR = "CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS"
ROUND318_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND318_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round318_r10_loop16_construction_real_estate_building_materials_trigger_validation"
ROUND318_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop16_round246.jsonl"
ROUND318_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r10_loop16_round246.jsonl"
ROUND318_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round318_r10_loop16_construction_real_estate_building_materials_trigger_validation_audit.json"
ROUND318_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round246_r10_loop16_v1.csv"

ROUND318_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE": E2RArchetype.MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE.value,
    "MEGA_GAS_PIPELINE_EPC_STAGE2_WITH_MARGIN_GATE": E2RArchetype.MEGA_GAS_PIPELINE_EPC_STAGE2_WITH_MARGIN_GATE.value,
    "PF_LIQUIDITY_RESTRUCTURING_4C_AND_RELIEF": E2RArchetype.PF_LIQUIDITY_RESTRUCTURING_4C_AND_RELIEF.value,
    "HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_WITH_LTV_4B": E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_WITH_LTV_4B.value,
    "CONSTRUCTION_SAFETY_HARD_4C": E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C.value,
    "AI_FAB_CONSTRUCTION_STAGE2": E2RArchetype.AI_FAB_CONSTRUCTION_STAGE2.value,
    "BUILDING_MATERIAL_INPUT_COST_STAGE2_4B": E2RArchetype.BUILDING_MATERIAL_INPUT_COST_STAGE2_4B.value,
    "RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B": E2RArchetype.RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B.value,
}

ROUND318_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "contract_value_is_clear",
    "event_return_at_least_5pct",
    "market_relative_return_at_least_5pp",
    "project_margin_or_cash_conversion_visibility_exists",
    "housing_policy_connects_to_permits_presales_or_PF_refinancing",
    "construction_safety_license_or_fatal_accident_4C_overlay_is_absent",
    "input_material_cost_pass_through_is_confirmed",
)

ROUND318_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_FCF_path_can_change_materially",
    "one_of_margin_cash_collection_permits_PF_refinancing_safety_remediation_or_material_pass_through_gate_remains_open",
    "reported_price_anchor_supports_trigger_but_full_adjusted_OHLC_is_missing",
)

ROUND318_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "EPC_backlog_converts_to_profitable_revenue_and_cash_flow",
    "project_execution_progresses_without_cost_overrun_or_claim",
    "housing_policy_converts_to_permits_pre_sales_and_PF_refinancing",
    "reconstruction_projects_start_construction",
    "construction_safety_risk_is_remediated",
    "input_cost_pass_through_is_contractually_protected",
    "full_adjusted_OHLC_MFE_MAE_window_supports_stage_candidate",
)

ROUND318_GREEN_BLOCKERS: tuple[str, ...] = (
    "contract_headline_without_margin",
    "housing_policy_without_presales",
    "PF_support_without_writeoff",
    "reconstruction_theme_without_start",
    "AI_fab_headline_without_order_value",
    "material_supplier_rally_ignoring_builder_cost",
    "safety_incident_treated_as_one_off",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND318_SCORE_UP_AXES: tuple[str, ...] = (
    "EPC_contract_value_visibility",
    "EPC_margin_cash_conversion",
    "project_execution_progress",
    "PF_refinancing_success",
    "pre_sale_recovery",
    "reconstruction_permit_conversion",
    "construction_safety_license_risk",
    "AI_fab_construction_backlog",
    "material_cost_pass_through",
)

ROUND318_SCORE_DOWN_AXES: tuple[str, ...] = (
    "contract_headline_without_margin",
    "housing_policy_without_presales",
    "PF_support_without_writeoff",
    "reconstruction_theme_without_start",
    "AI_fab_headline_without_order_value",
    "material_supplier_rally_ignoring_builder_cost",
    "safety_incident_treated_as_one_off",
)

ROUND318_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "overseas_EPC_contract_rallies_before_margin_or_cash_conversion",
    "housing_supply_policy_rallies_before_presales_and_permits",
    "PF_support_appears_before_loss_recognition_and_refinancing",
    "AI_fab_construction_story_appears_before_order_value_and_margin",
    "building_material_supplier_rally_increases_builder_input_cost",
    "fatal_construction_accident_triggers_fine_license_or_work_suspension_risk",
)

ROUND318_HARD_4C_GATES: tuple[str, ...] = (
    "debt_workout_or_PF_default",
    "PF_delinquency_spike_and_failed_refinancing",
    "fatal_construction_accident",
    "work_suspension_or_license_revocation_risk",
    "major_defect_collapse_or_safety_investigation",
    "input_cost_spike_without_pass_through",
    "housing_demand_collapse_or_pre_sale_failure",
)

ROUND318_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_contract_policy_safety_material_or_macro_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_EPC_PF_housing_safety_fab_or_material_headline_as_Green_without_margin_cash_presales_refinancing_safety_clearance_or_spread",
)


@dataclass(frozen=True)
class Round318TriggerRecord:
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
class Round318CaseCandidate:
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
            "do_not_use_round318_cases_as_candidate_generation_input",
            "do_not_treat_EPC_PF_housing_safety_fab_or_material_headline_as_Green_without_margin_cash_presales_refinancing_safety_clearance_or_spread",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND318_LARGE_SECTOR,
            large_sector=ROUND318_LARGE_SECTOR,
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
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4B" in field or "4b" in field or "LTV" in field or "input_cost" in field or "overheat" in field),
            stage4c_evidence=tuple(
                field
                for field in (*self.red_flag_fields, *self.evidence_fields)
                if "4C" in field
                or "4c" in field
                or "PF" in field
                or "fatal" in field
                or "safety" in field
                or "license" in field
                or "collapse" in field
                or "workout" in field
            ),
            must_have_fields=ROUND318_STAGE3_GREEN_RULES,
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


ROUND318_CASE_CANDIDATES: tuple[Round318CaseCandidate, ...] = (
    Round318CaseCandidate(
        "r10_loop16_samsung_ea_fadhili",
        "028050",
        "Samsung E&A",
        E2RArchetype.MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE,
        (E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE, E2RArchetype.OVERSEAS_EPC_ORDER_4B_WATCH),
        "success_candidate",
        "Stage2_Actionable_EPC_backlog",
        "r10l16_samsung_ea_fadhili_T1",
        "Stage2-Actionable_EPC_backlog",
        "Stage2-Actionable",
        date(2024, 4, 2),
        date(2024, 4, 3),
        None,
        date(2024, 4, 3),
        None,
        False,
        ("Aramco_Fadhili_contract_7_7B_usd", "Samsung_contract_context_6B_usd", "event_return_plus_8_5pct", "market_relative_plus_9_9pp", "capacity_2_5_to_4_0_bscfd", "completion_2027_11"),
        ("project_gross_margin_missing", "working_capital_profile_missing", "cost_escalation_control_missing", "claim_risk_missing", "execution_progress_missing", "full_OHLC_MFE_MAE_missing"),
        8.5,
        None,
        {"trigger_date": "2024-04-03", "aramco_total_contract_value_usd_bn": 7.7, "samsung_contract_value_context_usd_bn": 6.0, "event_price_krw": 26750, "event_return_pct": 8.5, "kospi_same_context_pct": -1.4, "market_relative_return_pp": 9.9, "fadhili_capacity_before_bscfd": 2.5, "fadhili_capacity_after_bscfd": 4.0, "completion_target": "2027-11"},
        "aligned",
        "excellent_stage2_actionable_EPC_contract",
        "event_premium",
        "stage2_watch_success",
        "Large Fadhili EPC contract and price reaction align. Green waits for EPC margin, working capital, cash collection and execution progress.",
    ),
    Round318CaseCandidate(
        "r10_loop16_hyundai_ec_jafurah_gas",
        "000720",
        "Hyundai E&C",
        E2RArchetype.MEGA_GAS_PIPELINE_EPC_STAGE2_WITH_MARGIN_GATE,
        (E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN, E2RArchetype.OVERSEAS_EPC_ORDER_4B_WATCH),
        "success_candidate",
        "Stage2_mega_gas_EPC_backlog",
        "r10l16_hyundai_ec_jafurah_T0",
        "Stage2_mega_gas_EPC",
        "Stage2",
        date(2024, 6, 30),
        date(2024, 6, 30),
        None,
        date(2024, 6, 30),
        None,
        False,
        ("Aramco_package_value_above_25B_usd", "Jafurah_sales_gas_target_2_0_bscfd", "gas_reserves_229_tcf", "main_gas_network_4000km", "added_capacity_3_2_bscfd"),
        ("Hyundai_EC_contract_share_missing", "project_margin_missing", "schedule_progress_missing", "Saudi_execution_risk_missing", "cash_conversion_missing", "full_OHLC_MFE_MAE_missing"),
        None,
        None,
        {"trigger_date": "2024-06-30", "aramco_package_value_usd_bn": ">25", "jafurah_sales_gas_target_bscfd_2030": 2.0, "jafurah_gas_reserves_tcf": 229, "jafurah_condensates_billion_barrels": 75, "main_gas_network_added_pipeline_km": 4000, "main_gas_network_added_capacity_bscfd": 3.2, "direct_hyundai_ec_price_anchor": "price_data_unavailable_after_deep_search"},
        "evidence_good_but_price_failed",
        "Stage2_mega_EPC_backlog_not_Green",
        "unknown",
        "stage2_watch_success",
        "Mega Aramco/Jafurah gas EPC evidence exists, but Hyundai E&C share, margin, direct price anchor and cash conversion are unavailable.",
    ),
    Round318CaseCandidate(
        "r10_loop16_pf_taeyoung_builder_restructuring",
        "009410/construction_basket",
        "Taeyoung E&C / Korean builders",
        E2RArchetype.PF_LIQUIDITY_RESTRUCTURING_4C_AND_RELIEF,
        (E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH, E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH),
        "failed_rerating",
        "PF_4C_watch_with_policy_relief",
        "r10l16_pf_taeyoung_T1",
        "4C_PF_liquidity_with_Stage2_policy_relief",
        "4C-watch + Stage2 relief",
        date(2023, 12, 1),
        date(2024, 3, 27),
        None,
        date(2024, 5, 13),
        None,
        False,
        ("Taeyoung_debt_rescheduling", "government_support_40_6T_won", "PF_delinquency_2_70pct", "PF_assessment_tightening", "syndicated_loan_1T_to_5T_won"),
        ("successful_project_refinancing_missing", "loss_recognition_completion_missing", "pre_sale_recovery_missing", "guarantee_exposure_reduction_missing", "builder_cashflow_recovery_missing", "PF_4C_watch_active"),
        None,
        None,
        {"support_announcement_date": "2024-03-27", "government_support_krw_trn": 40.6, "pf_restructuring_guideline_date": "2024-05-13", "pf_delinquency_end_2021_pct": 0.37, "pf_delinquency_end_2023_pct": 2.70, "syndicated_loan_initial_krw_trn": 1.0, "syndicated_loan_possible_max_krw_trn": 5.0, "direct_price_anchor": "price_data_unavailable_after_deep_search"},
        "aligned",
        "PF_4C_watch_with_policy_relief",
        "credit_relief_rally",
        "should_have_been_red",
        "PF support is relief, not Green. Write-offs, refinancing, pre-sales and builder cashflow recovery remain open.",
    ),
    Round318CaseCandidate(
        "r10_loop16_seoul_housing_supply_reconstruction",
        "000720/006360/294870/028260/housing_builder_basket",
        "Korean housing builders",
        E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_WITH_LTV_4B,
        (E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY, E2RArchetype.REAL_ESTATE_POLICY_STAGE2_NOT_GREEN),
        "event_premium",
        "mixed_supply_policy_Stage2_with_demand_4B",
        "r10l16_seoul_housing_supply_T2",
        "Stage2_supply_policy_with_LTV_4B",
        "Stage2 + 4B-watch",
        date(2024, 8, 16),
        date(2024, 8, 16),
        None,
        date(2025, 9, 7),
        None,
        False,
        ("Seoul_prices_plus_0_76pct_MoM", "new_homes_target_above_400000", "state_run_land_supply", "reconstruction_rule_streamlining", "LTV_50_to_40pct"),
        ("permits_missing", "actual_reconstruction_start_missing", "pre_sale_ratio_missing", "PF_refinancing_missing", "builder_margin_missing", "completion_cashflow_missing", "LTV_demand_curb_4B"),
        None,
        None,
        {"seoul_price_mom_july_2024_pct": 0.76, "seoul_price_context": "strongest_monthly_rise_since_2019-12", "new_homes_target_six_years": ">400000", "ltv_tightening_date": "2025-09-07", "ltv_old_pct": 50, "ltv_new_pct": 40, "direct_builder_price_anchor": "price_data_unavailable_after_deep_search"},
        "unknown",
        "mixed_supply_policy_Stage2_with_demand_4B",
        "policy_event_rerating",
        "stage2_watch_success",
        "Supply and reconstruction policy can be Stage2, but LTV tightening can hurt demand. Green requires permits, pre-sales and PF refinancing.",
    ),
    Round318CaseCandidate(
        "r10_loop16_construction_safety_hyundai_engineering_bridge",
        "Hyundai_Engineering_private/construction_basket",
        "Hyundai Engineering / construction safety read-through",
        E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C,
        (E2RArchetype.CONSTRUCTION_QUALITY_SAFETY_HARD_4C,),
        "4c_thesis_break",
        "hard_4C_construction_safety",
        "r10l16_construction_safety_T0",
        "hard_4C_construction_safety",
        "4C",
        date(2025, 2, 25),
        None,
        None,
        None,
        date(2025, 2, 25),
        True,
        ("fatal_bridge_collapse", "four_worker_deaths", "six_injuries", "Hyundai_Engineering_site", "fine_up_to_5pct_operating_profit", "license_revocation_risk"),
        ("final_investigation_result_missing", "compensation_cost_missing", "work_suspension_duration_missing", "license_impact_missing", "safety_remediation_missing", "future_bidding_penalty_missing"),
        None,
        None,
        {"incident_date": "2025-02-25", "fatalities": 4, "injuries": 6, "site_company": "Hyundai_Engineering", "direct_price_anchor": "price_data_unavailable_private_company", "policy_date": "2025-09-15", "proposed_fine_pct_of_operating_profit": 5, "license_revocation_risk": True},
        "aligned",
        "hard_4C_success_construction_safety",
        "thesis_break",
        "should_have_been_red",
        "Fatal construction accident is a hard 4C gate because it can hit license, fines, work suspension, brand and bidding.",
    ),
    Round318CaseCandidate(
        "r10_loop16_samsung_ct_p5_fab_construction",
        "028260",
        "Samsung C&T",
        E2RArchetype.AI_FAB_CONSTRUCTION_STAGE2,
        (E2RArchetype.AI_DATA_CENTER_REAL_ASSET_KOREA, E2RArchetype.AI_DATA_CENTER_POWER_CAMPUS),
        "success_candidate",
        "Stage2_AI_fab_construction",
        "r10l16_samsung_ct_p5_T1",
        "Stage2_AI_fab_construction",
        "Stage2",
        date(2025, 10, 2),
        date(2025, 11, 16),
        None,
        date(2025, 11, 16),
        None,
        False,
        ("Pyeongtaek_P5_line", "Samsung_group_domestic_investment_450T_won", "five_year_investment_plan", "mass_production_target_2028", "Samsung_CT_builder_filings"),
        ("Samsung_CT_order_value_missing", "construction_margin_missing", "schedule_progress_missing", "materials_cost_missing", "AI_memory_demand_durability_missing", "cash_collection_missing"),
        None,
        None,
        {"trigger_date": "2025-11-16", "samsung_group_domestic_investment_krw_trn": 450, "investment_period_years": 5, "project": "Pyeongtaek_P5_chip_production_line", "p5_delay_context": "delayed_since_late_2023", "mass_production_target_year": 2028, "builder_context": "Samsung_C&T_public_filings", "direct_samsung_ct_price_anchor": "price_data_unavailable_after_deep_search"},
        "evidence_good_but_price_failed",
        "Stage2_AI_fab_construction_not_Green",
        "unknown",
        "stage2_watch_success",
        "AI fab capex is a Stage2 construction backlog clue. Yellow waits for Samsung C&T order value, margin, schedule and cash collection.",
    ),
    Round318CaseCandidate(
        "r10_loop16_steel_plate_antidumping_construction_input",
        "004020/005490/construction_input_basket",
        "Hyundai Steel / POSCO / construction input basket",
        E2RArchetype.BUILDING_MATERIAL_INPUT_COST_STAGE2_4B,
        (E2RArchetype.BUILDING_MATERIAL_TARIFF_RELIEF_EVENT_PREMIUM, E2RArchetype.STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK),
        "4b_watch",
        "mixed_supplier_Stage2_builder_4B",
        "r10l16_steel_plate_antidumping_T0",
        "mixed_supplier_Stage2_builder_4B",
        "mixed Stage2/4B",
        date(2025, 2, 20),
        date(2025, 2, 20),
        None,
        date(2025, 2, 20),
        None,
        False,
        ("anti_dumping_rate_27_91_to_38_02pct", "China_steel_imports_10_4B_usd", "China_share_49pct", "Hyundai_Steel_plus_5_8pct", "POSCO_plus_3_9pct", "KOSPI_minus_0_7pct"),
        ("builder_cost_pass_through_missing", "public_project_escalation_clause_missing", "materials_cost_absorption_missing", "steel_supplier_margin_missing", "construction_contract_margin_missing", "builder_input_cost_4B"),
        5.8,
        None,
        {"trigger_date": "2025-02-20", "anti_dumping_rate_pct": "27.91-38.02", "china_steel_import_value_2024_usd_bn": 10.4, "china_share_of_korea_steel_imports_pct": 49, "hyundai_steel_event_return_pct": 5.8, "posco_event_return_pct": 3.9, "kospi_same_context_pct": -0.7, "construction_use_case": True},
        "aligned",
        "mixed_building_material_supplier_relief_builder_cost_4B",
        "event_premium",
        "stage2_watch_success",
        "Anti-dumping is positive for steel suppliers, but can be builder input-cost 4B unless pass-through and contract margin are visible.",
    ),
    Round318CaseCandidate(
        "r10_loop16_bok_rate_cut_housing_construction_mixed",
        "construction_basket/REITs/banks_readthrough",
        "Construction macro / housing rate-cut basket",
        E2RArchetype.RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B,
        (E2RArchetype.HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF, E2RArchetype.SEOUL_PROPERTY_POLICY_EVENT_PREMIUM),
        "event_premium",
        "mixed_rate_cut_relief_with_housing_4B",
        "r10l16_bok_rate_cut_housing_T0",
        "mixed_rate_cut_relief_with_housing_4B",
        "Stage2 macro relief + 4B",
        date(2025, 10, 23),
        date(2025, 10, 23),
        None,
        date(2025, 10, 23),
        None,
        False,
        ("policy_rate_2_50pct", "possible_forward_rate_2_25pct_or_lower", "four_of_six_members_open_to_cut", "KOSPI_record_context", "won_six_month_low", "construction_downturn"),
        ("PF_refinancing_missing", "mortgage_demand_recovery_missing", "pre_sale_recovery_missing", "builder_margin_recovery_missing", "rate_cut_execution_missing", "housing_overheating_4B"),
        None,
        None,
        {"trigger_date": "2025-10-23", "policy_rate_pct": 2.50, "possible_forward_rate_pct": "<=2.25", "board_members_open_to_cut": 4, "board_members_total_context": 6, "kospi_context": "fresh_record_high", "won_context": "about_six_month_low", "construction_downturn_drivers": ["labor_cost", "equipment_cost", "housing_supply_shortage", "financial_stability_risk"]},
        "unknown",
        "macro_relief_Stage2_with_housing_4B",
        "policy_event_rerating",
        "stage2_watch_success",
        "Rate-cut guidance can help PF refinancing, but housing overheating, FX pressure and construction-cost downturn keep it Stage2/4B.",
    ),
)

ROUND318_TRIGGER_RECORDS: tuple[Round318TriggerRecord, ...] = (
    Round318TriggerRecord("r10l16_samsung_ea_fadhili_T1", "r10_loop16_samsung_ea_fadhili", "Stage2-Actionable_EPC_backlog", "2024-04-03", "Samsung E&A signs around $6B Fadhili share; shares +8.5% to 26,750 won while KOSPI -1.4%; Fadhili capacity expands 2.5 to 4.0 bscfd by Nov 2027.", 8.5, "excellent_stage2_actionable_EPC_contract", "Stage2-Actionable", {"market_relative_return_pp": 9.9, "contract_value_usd_bn": 6.0}),
    Round318TriggerRecord("r10l16_hyundai_ec_jafurah_T0", "r10_loop16_hyundai_ec_jafurah_gas", "Stage2_mega_gas_EPC", "2024-06-30", "Aramco signs $25B+ Jafurah and main gas network contracts; Hyundai E&C consortium involved; direct listed-company price anchor missing.", None, "Stage2_mega_EPC_backlog_not_Green", "Stage2", {"aramco_package_value_usd_bn": ">25", "main_gas_network_added_pipeline_km": 4000}),
    Round318TriggerRecord("r10l16_pf_taeyoung_T1", "r10_loop16_pf_taeyoung_builder_restructuring", "4C_PF_liquidity_with_Stage2_policy_relief", "2024-03-27/2024-05-13", "Korea announces 40.6T won builder support; FSS tightens PF assessments; delinquency rises to 2.70% from 0.37%; syndicated loan can expand 1T to 5T won.", None, "PF_4C_watch_with_policy_relief", "4C-watch+Stage2", {"government_support_krw_trn": 40.6, "pf_delinquency_end_2023_pct": 2.70}),
    Round318TriggerRecord("r10l16_seoul_housing_supply_T2", "r10_loop16_seoul_housing_supply_reconstruction", "Stage2_supply_policy_with_LTV_4B", "2024-08-16/2025-09-07", "Seoul prices +0.76% MoM and 400,000+ home target support supply/reconstruction; Gangnam/Yongsan LTV cut 50% to 40% is demand 4B.", None, "mixed_supply_policy_Stage2_with_demand_4B", "Stage2+4B", {"new_homes_target_six_years": ">400000", "ltv_old_pct": 50, "ltv_new_pct": 40}),
    Round318TriggerRecord("r10l16_construction_safety_T0", "r10_loop16_construction_safety_hyundai_engineering_bridge", "hard_4C_construction_safety", "2025-02-25/2025-09-15", "Anseong/Cheonan bridge collapse killed 4 and injured 6; later policy proposes fines up to 5% of operating profit and license risk.", None, "hard_4C_success_construction_safety", "4C", {"fatalities": 4, "proposed_fine_pct_of_operating_profit": 5}),
    Round318TriggerRecord("r10l16_samsung_ct_p5_T1", "r10_loop16_samsung_ct_p5_fab_construction", "Stage2_AI_fab_construction", "2025-11-16", "Samsung adds P5 Pyeongtaek line within 450T won domestic investment; P5 mass production target 2028; Samsung C&T builder context but order value and margin missing.", None, "Stage2_AI_fab_construction_not_Green", "Stage2", {"investment_krw_trn": 450, "mass_production_target_year": 2028}),
    Round318TriggerRecord("r10l16_steel_plate_antidumping_T0", "r10_loop16_steel_plate_antidumping_construction_input", "mixed_supplier_Stage2_builder_4B", "2025-02-20", "Korea recommends 27.91-38.02% provisional anti-dumping duties on Chinese steel plates; Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%.", 5.8, "mixed_building_material_supplier_relief_builder_cost_4B", "Stage2+4B", {"hyundai_steel_event_return_pct": 5.8, "posco_event_return_pct": 3.9}),
    Round318TriggerRecord("r10l16_bok_rate_cut_housing_T0", "r10_loop16_bok_rate_cut_housing_construction_mixed", "mixed_rate_cut_relief_with_housing_4B", "2025-10-23", "BOK holds 2.50% but signals possible cut to 2.25% or lower; won weakness, housing overheating and construction downturn limit builder relief.", None, "macro_relief_Stage2_with_housing_4B", "Stage2+4B", {"policy_rate_pct": 2.50, "board_members_open_to_cut": 4}),
)

ROUND318_SHADOW_WEIGHT_ROWS: tuple[dict[str, str], ...] = (
    {"archetype": E2RArchetype.MIDDLE_EAST_EPC_BACKLOG_STAGE2_ACTIONABLE.value, "EPC_contract_value_visibility": "+5", "EPC_margin_cash_conversion": "+5", "project_execution_progress": "+4", "PF_refinancing_success": "+0", "pre_sale_recovery": "+0", "reconstruction_permit_conversion": "+0", "construction_safety_license_risk": "+1", "AI_fab_construction_backlog": "+0", "material_cost_pass_through": "+1", "contract_headline_without_margin_penalty": "-5", "housing_policy_without_presales_penalty": "-1", "PF_support_without_writeoff_penalty": "-1", "AI_fab_headline_without_order_value_penalty": "-1", "stage2_actionable_promote": "contract value and price reaction close", "stage3_yellow_gate": "margin/cash conversion pending", "stage3_green_gate": "EPC margin+working capital+cash collection", "notes": "Samsung E&A Fadhili."},
    {"archetype": E2RArchetype.MEGA_GAS_PIPELINE_EPC_STAGE2_WITH_MARGIN_GATE.value, "EPC_contract_value_visibility": "+5", "EPC_margin_cash_conversion": "+5", "project_execution_progress": "+4", "PF_refinancing_success": "+0", "pre_sale_recovery": "+0", "reconstruction_permit_conversion": "+0", "construction_safety_license_risk": "+1", "AI_fab_construction_backlog": "+0", "material_cost_pass_through": "+1", "contract_headline_without_margin_penalty": "-5", "housing_policy_without_presales_penalty": "-1", "PF_support_without_writeoff_penalty": "-1", "AI_fab_headline_without_order_value_penalty": "-1", "stage2_actionable_promote": "mega gas EPC package", "stage3_yellow_gate": "company share/margin missing", "stage3_green_gate": "contract share+schedule+cash conversion", "notes": "Hyundai E&C Jafurah."},
    {"archetype": E2RArchetype.PF_LIQUIDITY_RESTRUCTURING_4C_AND_RELIEF.value, "EPC_contract_value_visibility": "+0", "EPC_margin_cash_conversion": "+0", "project_execution_progress": "+0", "PF_refinancing_success": "+5", "pre_sale_recovery": "+5", "reconstruction_permit_conversion": "+1", "construction_safety_license_risk": "+1", "AI_fab_construction_backlog": "+0", "material_cost_pass_through": "+0", "contract_headline_without_margin_penalty": "-1", "housing_policy_without_presales_penalty": "-3", "PF_support_without_writeoff_penalty": "-5", "AI_fab_headline_without_order_value_penalty": "-1", "stage2_actionable_promote": "policy relief only", "stage3_yellow_gate": "write-off/refinancing pending", "stage3_green_gate": "N/A until PF cleanup", "notes": "Taeyoung/PF."},
    {"archetype": E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_WITH_LTV_4B.value, "EPC_contract_value_visibility": "+0", "EPC_margin_cash_conversion": "+0", "project_execution_progress": "+0", "PF_refinancing_success": "+4", "pre_sale_recovery": "+5", "reconstruction_permit_conversion": "+4", "construction_safety_license_risk": "+1", "AI_fab_construction_backlog": "+0", "material_cost_pass_through": "+2", "contract_headline_without_margin_penalty": "-1", "housing_policy_without_presales_penalty": "-5", "PF_support_without_writeoff_penalty": "-3", "AI_fab_headline_without_order_value_penalty": "-1", "stage2_actionable_promote": "housing supply/reconstruction policy", "stage3_yellow_gate": "permits/pre-sales/PF missing", "stage3_green_gate": "permits+pre-sales+margin+PF refinancing", "notes": "Seoul housing."},
    {"archetype": E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C.value, "EPC_contract_value_visibility": "+0", "EPC_margin_cash_conversion": "+0", "project_execution_progress": "+0", "PF_refinancing_success": "+0", "pre_sale_recovery": "+0", "reconstruction_permit_conversion": "+0", "construction_safety_license_risk": "+5", "AI_fab_construction_backlog": "+0", "material_cost_pass_through": "+0", "contract_headline_without_margin_penalty": "-2", "housing_policy_without_presales_penalty": "-2", "PF_support_without_writeoff_penalty": "-2", "AI_fab_headline_without_order_value_penalty": "-1", "stage2_actionable_promote": "N/A", "stage3_yellow_gate": "N/A", "stage3_green_gate": "N/A while hard safety active", "notes": "Hyundai Engineering bridge."},
    {"archetype": E2RArchetype.AI_FAB_CONSTRUCTION_STAGE2.value, "EPC_contract_value_visibility": "+1", "EPC_margin_cash_conversion": "+3", "project_execution_progress": "+4", "PF_refinancing_success": "+0", "pre_sale_recovery": "+0", "reconstruction_permit_conversion": "+0", "construction_safety_license_risk": "+1", "AI_fab_construction_backlog": "+4", "material_cost_pass_through": "+2", "contract_headline_without_margin_penalty": "-2", "housing_policy_without_presales_penalty": "-1", "PF_support_without_writeoff_penalty": "-1", "AI_fab_headline_without_order_value_penalty": "-4", "stage2_actionable_promote": "fab restart/capex", "stage3_yellow_gate": "order value and margin missing", "stage3_green_gate": "order value+margin+schedule+cash collection", "notes": "Samsung C&T P5."},
    {"archetype": E2RArchetype.BUILDING_MATERIAL_INPUT_COST_STAGE2_4B.value, "EPC_contract_value_visibility": "+0", "EPC_margin_cash_conversion": "+0", "project_execution_progress": "+0", "PF_refinancing_success": "+1", "pre_sale_recovery": "+1", "reconstruction_permit_conversion": "+0", "construction_safety_license_risk": "+1", "AI_fab_construction_backlog": "+0", "material_cost_pass_through": "+4", "contract_headline_without_margin_penalty": "-1", "housing_policy_without_presales_penalty": "-1", "PF_support_without_writeoff_penalty": "-1", "AI_fab_headline_without_order_value_penalty": "-1", "stage2_actionable_promote": "supplier event return", "stage3_yellow_gate": "supplier margin/builder pass-through missing", "stage3_green_gate": "spread+pass-through+demand", "notes": "Steel plate anti-dumping."},
    {"archetype": E2RArchetype.RATE_CUT_HOUSING_POLICY_MIXED_STAGE2_4B.value, "EPC_contract_value_visibility": "+0", "EPC_margin_cash_conversion": "+0", "project_execution_progress": "+0", "PF_refinancing_success": "+5", "pre_sale_recovery": "+4", "reconstruction_permit_conversion": "+2", "construction_safety_license_risk": "+1", "AI_fab_construction_backlog": "+0", "material_cost_pass_through": "+1", "contract_headline_without_margin_penalty": "-1", "housing_policy_without_presales_penalty": "-4", "PF_support_without_writeoff_penalty": "-4", "AI_fab_headline_without_order_value_penalty": "-1", "stage2_actionable_promote": "rate-cut relief", "stage3_yellow_gate": "rate cut/PF/pre-sales missing", "stage3_green_gate": "rate cut execution+PF refinancing+margin", "notes": "BOK/housing macro."},
)


def round318_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND318_CASE_CANDIDATES]


def round318_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND318_CASE_CANDIDATES]


def round318_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND318_TRIGGER_RECORDS]


def round318_shadow_weight_rows() -> list[dict[str, str]]:
    return [dict(row) for row in ROUND318_SHADOW_WEIGHT_ROWS]


def round318_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND318_REQUIRED_TARGET_ALIASES.items()]


def round318_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND318_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND318_SCORE_DOWN_AXES]
    )


def round318_summary() -> dict[str, object]:
    return {
        "source_round": ROUND318_SOURCE_ROUND_PATH,
        "round_id": ROUND318_ANALYST_ROUND_ID,
        "large_sector": ROUND318_LARGE_SECTOR,
        "method": ROUND318_METHOD,
        "case_candidate_count": len(ROUND318_CASE_CANDIDATES),
        "trigger_count": len(ROUND318_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND318_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 2,
        "stage2_candidate_count": 6,
        "stage3_yellow_candidate_count": 4,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 6,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 1,
        "evidence_good_but_price_failed_or_unavailable_count": 6,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R11 Loop 16",
    }


def round318_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND318_SOURCE_ROUND_PATH,
        "round_id": ROUND318_ANALYST_ROUND_ID,
        "large_sector": ROUND318_LARGE_SECTOR,
        "method": ROUND318_METHOD,
        "summary": round318_summary(),
        "required_target_aliases": dict(ROUND318_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND318_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND318_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND318_STAGE3_GREEN_RULES,
        "green_blockers": ROUND318_GREEN_BLOCKERS,
        "score_up_axes": ROUND318_SCORE_UP_AXES,
        "score_down_axes": ROUND318_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND318_STAGE4B_WATCH_TRIGGERS,
        "hard_4c_gates": ROUND318_HARD_4C_GATES,
        "row_separation_rules": ROUND318_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round318_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_EPC_PF_housing_safety_fab_or_material_headline_as_Green_without_margin_cash_presales_refinancing_safety_clearance_or_spread",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round318_summary_markdown() -> str:
    summary = round318_summary()
    lines = [
        "# R10 Loop 16 Construction / Real Estate / Building Materials Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: a PF support package can be Stage2 relief, but it is not Green until refinancing, write-offs, pre-sales and cashflow are actually visible.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Samsung E&A / Fadhili is the cleanest Stage2-Actionable EPC case.",
            "- Hyundai E&C / Jafurah is Stage2 mega-backlog, but company share, margin and price anchor are missing.",
            "- PF / Taeyoung is 4C-watch with policy relief, not Green.",
            "- Seoul housing supply and reconstruction policy is Stage2, but LTV tightening is demand 4B.",
            "- Construction safety fatality is hard 4C.",
            "- Samsung C&T / P5 is Stage2 AI fab construction until order value and margin are visible.",
            "- Steel plate anti-dumping is supplier Stage2 and builder input-cost 4B.",
            "- BOK rate-cut guidance is macro relief with housing-overheat 4B.",
            "- Stage3-Green confirmed: `0`.",
            "- Hard 4C confirmed: `1`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round318_trigger_grid_markdown() -> str:
    lines = [
        "# Round 318 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round318_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round318_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 318 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND318_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND318_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND318_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND318_GREEN_BLOCKERS),
            "",
            "## Hard 4C Gates",
            *_bullet_lines(ROUND318_HARD_4C_GATES),
        ]
    ) + "\n"


def render_round318_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 318 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND318_STAGE4B_WATCH_TRIGGERS),
        "",
        "## Hard 4C Gates",
        *_bullet_lines(ROUND318_HARD_4C_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND318_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round318_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 318 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND318_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round318_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 318 Row Separation Plan",
        "",
        "Case evidence, trigger anchors and full OHLC windows must be separate rows.",
        "",
        "Easy example: steel anti-dumping can lift steel suppliers, but the same event can hurt builders if input costs cannot be passed through.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND318_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round318_r10_loop16_reports(
    output_directory: str | Path = ROUND318_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND318_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND318_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND318_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND318_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round318_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND318_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round318_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round318_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round318_r10_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round318_r10_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round318_r10_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round318_r10_loop16_trigger_grid.md",
        "summary": output_dir / "round318_r10_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round318_r10_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round318_r10_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round318_r10_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round318_r10_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round318_r10_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round318_r10_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round318_case_rows())
    _write_csv(paths["target_aliases"], round318_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round318_trigger_rows())
    _write_csv(paths["score_adjustments"], round318_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round318_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round318_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round318_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round318_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round318_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round318_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round318_row_separation_plan_markdown(), encoding="utf-8")
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
    "ROUND318_CASE_CANDIDATES",
    "ROUND318_GREEN_BLOCKERS",
    "ROUND318_HARD_4C_GATES",
    "ROUND318_LARGE_SECTOR",
    "ROUND318_REQUIRED_TARGET_ALIASES",
    "ROUND318_ROW_SEPARATION_RULES",
    "ROUND318_SCORE_DOWN_AXES",
    "ROUND318_SCORE_UP_AXES",
    "ROUND318_SHADOW_WEIGHT_ROWS",
    "ROUND318_STAGE2_ACTIONABLE_RULES",
    "ROUND318_STAGE3_GREEN_RULES",
    "ROUND318_STAGE3_YELLOW_RULES",
    "ROUND318_STAGE4B_WATCH_TRIGGERS",
    "ROUND318_TRIGGER_RECORDS",
    "render_round318_stage4b_4c_review_markdown",
    "render_round318_stage_rules_markdown",
    "render_round318_trigger_grid_markdown",
    "round318_audit_payload",
    "round318_case_records",
    "round318_case_rows",
    "round318_shadow_weight_rows",
    "round318_summary",
    "round318_trigger_rows",
    "write_round318_r10_loop16_reports",
]
