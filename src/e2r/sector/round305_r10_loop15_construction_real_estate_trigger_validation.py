"""Round-305 R10 Loop-15 construction/real-estate/building-material trigger pack.

This module converts ``docs/round/round_305.md`` into calibration-only case
records, trigger rows, shadow weights, and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a $6B overseas EPC order can be Stage 2 evidence, but it is not
Stage 3-Green until project margin, cash collection, and cost-overrun control
are visible. A PF support package is similar: it can keep a builder alive, but
it is not earnings recovery until bad projects, impairments, and refinancing
terms are cleaned up.
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


ROUND305_SOURCE_ROUND_PATH = "docs/round/round_305.md"
ROUND305_ANALYST_ROUND_ID = "round_233"
ROUND305_LARGE_SECTOR = "CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS"
ROUND305_METHOD = "trigger_level_backtest_v1"
ROUND305_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round305_r10_loop15_construction_real_estate_trigger_validation"
ROUND305_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop15_round233.jsonl"
ROUND305_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r10_loop15_round233.jsonl"
ROUND305_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round305_r10_loop15_construction_real_estate_trigger_validation_audit.json"
ROUND305_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round233_r10_loop15_v1.csv"

ROUND305_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE": E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE.value,
    "NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B": E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B.value,
    "REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH": E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH.value,
    "HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY": E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY.value,
    "CONSTRUCTION_QUALITY_SAFETY_HARD_4C": E2RArchetype.CONSTRUCTION_QUALITY_SAFETY_HARD_4C.value,
    "BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING": E2RArchetype.BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING.value,
    "BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH": E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH.value,
}

ROUND305_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "contract_value_is_meaningful_vs_annual_wins_or_backlog",
    "market_relative_event_return_exceeds_5pp_or_sector_basket_reacts",
    "customer_scope_completion_schedule_or_policy_amount_is_specific",
    "final_contract_or_award_is_preferred_over_preferred_bidder_only",
    "reported_event_anchor_is_recorded_without_inventing_full_ohlc",
)

ROUND305_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "EPC_margin_cash_collection_or_cost_overrun_partially_visible",
    "nuclear_contract_signed_but_work_allocation_or_legal_cleanup_pending",
    "housing_permits_starts_or_presales_visible_but_PF_repayment_pending",
    "PF_restructuring_terms_visible_but_impairment_or_cashflow_pending",
    "building_material_ASP_or_spread_recovery_visible_but_demand_duration_pending",
)

ROUND305_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "EPC_backlog_to_OP_cashflow_conversion_visible",
    "project_margin_cash_collection_and_cost_overrun_risk_controlled",
    "nuclear_final_contract_legal_clearance_work_split_and_payment_schedule_visible",
    "housing_policy_converts_to_starts_presales_unsold_absorption_and_PF_repayment",
    "PF_cleanup_refinancing_and_impairment_resolution_visible",
    "construction_quality_safety_overhang_cleared",
    "full_window_mfe_mae_is_available_and_supportive",
)

ROUND305_GREEN_BLOCKERS: tuple[str, ...] = (
    "headline_order_without_margin",
    "preferred_bidder_without_final_contract",
    "policy_support_without_project_cashflow",
    "housing_supply_headline_without_starts",
    "PF_liquidity_without_impairment_cleanup",
    "construction_material_demand_assumption_only",
    "large_project_without_legal_clearance",
    "construction_quality_or_safety_hard_gate_active",
)

ROUND305_SCORE_UP_AXES: tuple[str, ...] = (
    "contract_value_vs_annual_backlog",
    "project_margin_visibility",
    "cash_collection_schedule",
    "cost_overrun_delay_control",
    "final_contract_signed_not_preferred_bidder",
    "legal_appeal_clearance",
    "housing_starts_presale_rate",
    "PF_restructuring_completion",
    "construction_quality_safety_trust",
    "building_material_spread_visibility",
)

ROUND305_SCORE_DOWN_AXES: tuple[str, ...] = (
    "headline_order_without_margin",
    "preferred_bidder_without_final_contract",
    "policy_support_without_project_cashflow",
    "housing_supply_headline_without_starts",
    "PF_liquidity_without_impairment_cleanup",
    "construction_material_demand_assumption_only",
    "large_project_without_legal_clearance",
)

ROUND305_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "large_EPC_order_rally_before_margin_or_cash_collection",
    "preferred_bidder_basket_rerating_before_final_contract",
    "builder_liquidity_support_rally_before_PF_cleanup",
    "housing_supply_policy_rally_before_starts_and_presales",
    "construction_quality_relief_bounce_before_trust_repair",
)

ROUND305_HARD_4C_GATES: tuple[str, ...] = (
    "fatal_construction_quality_or_safety_event",
    "PF_default_workout_or_debt_rescheduling",
    "project_cancellation_legal_block_or_final_contract_failure",
    "cost_overrun_causing_margin_collapse",
    "presale_failure_or_unsold_inventory_spike",
    "building_material_ASP_or_spread_collapse",
)


@dataclass(frozen=True)
class Round305ShadowWeightRow:
    archetype: E2RArchetype
    contract_value_vs_annual_backlog: int
    project_margin_visibility: int
    cash_collection_schedule: int
    cost_overrun_delay_control: int
    final_contract_signed_not_preferred_bidder: int
    legal_appeal_clearance: int
    housing_starts_presale_rate: int
    pf_restructuring_completion: int
    construction_quality_safety_trust: int
    building_material_spread_visibility: int
    headline_order_without_margin_penalty: int
    preferred_bidder_without_final_contract_penalty: int
    policy_support_without_project_cashflow_penalty: int
    housing_supply_headline_without_starts_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "contract_value_vs_annual_backlog": _signed(self.contract_value_vs_annual_backlog),
            "project_margin_visibility": _signed(self.project_margin_visibility),
            "cash_collection_schedule": _signed(self.cash_collection_schedule),
            "cost_overrun_delay_control": _signed(self.cost_overrun_delay_control),
            "final_contract_signed_not_preferred_bidder": _signed(self.final_contract_signed_not_preferred_bidder),
            "legal_appeal_clearance": _signed(self.legal_appeal_clearance),
            "housing_starts_presale_rate": _signed(self.housing_starts_presale_rate),
            "pf_restructuring_completion": _signed(self.pf_restructuring_completion),
            "construction_quality_safety_trust": _signed(self.construction_quality_safety_trust),
            "building_material_spread_visibility": _signed(self.building_material_spread_visibility),
            "headline_order_without_margin_penalty": _signed(self.headline_order_without_margin_penalty),
            "preferred_bidder_without_final_contract_penalty": _signed(self.preferred_bidder_without_final_contract_penalty),
            "policy_support_without_project_cashflow_penalty": _signed(self.policy_support_without_project_cashflow_penalty),
            "housing_supply_headline_without_starts_penalty": _signed(self.housing_supply_headline_without_starts_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round305TriggerRecord:
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
class Round305CaseCandidate:
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
            "do_not_use_round305_cases_as_candidate_generation_input",
            "do_not_treat_construction_policy_or_order_headline_as_green",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND305_LARGE_SECTOR,
            large_sector=ROUND305_LARGE_SECTOR,
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
            must_have_fields=ROUND305_STAGE2_ACTIONABLE_RULES + ROUND305_STAGE3_YELLOW_RULES + ROUND305_STAGE3_GREEN_RULES,
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
            data_quality=CaseDataQuality(False, True, False, 0.66),
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


ROUND305_SHADOW_WEIGHT_ROWS: tuple[Round305ShadowWeightRow, ...] = (
    Round305ShadowWeightRow(E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE, 5, 5, 5, 5, 4, 3, 0, 1, 3, 1, -5, -2, -2, -1, "contract value+relative strength", "margin/cash collection pending", "backlog-to-OP+cash conversion", "Samsung E&A Fadhili template."),
    Round305ShadowWeightRow(E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B, 4, 4, 4, 5, 5, 5, 0, 0, 4, 1, -4, -5, -2, -1, "preferred bidder+sector rerating", "final contract/legal/work split pending", "contract+work allocation+margin", "Czech nuclear basket."),
    Round305ShadowWeightRow(E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH, 0, 2, 4, 3, 0, 0, 3, 5, 3, 2, -2, -1, -5, -3, "PF stress/support", "impairment cleanup pending", "PF cleanup+cashflow recovery", "Taeyoung/PF template."),
    Round305ShadowWeightRow(E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY, 0, 3, 3, 2, 0, 0, 5, 4, 3, 2, -1, -1, -4, -5, "supply policy/reconstruction", "starts/presales pending", "starts+presales+margin", "Seoul housing policy Stage2."),
    Round305ShadowWeightRow(E2RArchetype.CONSTRUCTION_QUALITY_SAFETY_HARD_4C, 0, 1, 2, 5, 0, 0, 1, 2, 5, 1, -1, -1, -1, -1, "safety/quality incident", "trust recovery pending", "safety cleared+orders recovered", "HDC hard 4C reference."),
    Round305ShadowWeightRow(E2RArchetype.BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING, 0, 3, 2, 2, 0, 0, 4, 2, 2, 5, -2, -1, -2, -2, "rebar/ASP demand cut", "spread recovery pending", "ASP+volume+spread recovery", "Hyundai Steel rebar weak-demand case."),
    Round305ShadowWeightRow(E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH, 0, 2, 4, 2, 0, 0, 3, 5, 3, 2, -2, -1, -5, -4, "liquidity support", "project cashflow pending", "PF cleanup+margin recovery", "Builder policy relief false-positive watch."),
)

ROUND305_TRIGGER_RECORDS: tuple[Round305TriggerRecord, ...] = (
    Round305TriggerRecord("r10l15_samsungea_fadhili_T1", "r10_loop15_samsung_ea_fadhili", "Stage2-Actionable", date(2024, 4, 3), "Samsung E&A signs around $6B Saudi Aramco Fadhili contract; shares +8.5% to KRW26,750 while KOSPI -1.4%", 8.5, "excellent_stage2_actionable", "Stage3-Yellow_candidate", {"contract_value_usd_bn": 6.0, "aramco_total_package_usd_bn": 7.7, "event_price_high_krw": 26750, "kospi_same_context_pct": -1.4, "market_relative_return_pp": 9.9, "average_annual_contract_wins_krw_trn": 8.6}),
    Round305TriggerRecord("r10l15_gsenc_fadhili_T0", "r10_loop15_gsenc_fadhili_overlay", "Stage2_evidence", date(2024, 4, 2), "Aramco awards Fadhili EPC contracts to Samsung E&A, GS E&C and Nesma; $7.7B total package", "price_data_unavailable_after_deep_search", "Stage2_evidence_not_actionable_without_company_price", "Stage2", {"aramco_total_package_usd_bn": 7.7, "project_capacity_before_bcf_per_day": 2.5, "project_capacity_after_bcf_per_day": 4.0, "completion_target": "2027-11"}),
    Round305TriggerRecord("r10l15_czech_nuclear_T1", "r10_loop15_czech_nuclear_construction_basket", "Stage2-Actionable", date(2024, 7, 17), "Czech government selects KHNP preferred bidder for two reactors; Doosan +48%, KEPCO Plant S&E +14%, KEPCO E&C +41% over three months", "Doosan +48 / KEPCO PSE +14 / KEPCO E&C +41 over 3M", "Stage2_promote_candidate", "Stage2-Actionable", {"reactors_count": 2, "preferred_bidder": "KHNP", "doosan_3m_return_pct": 48, "kepco_plant_se_3m_return_pct": 14, "kepco_ec_3m_return_pct": 41}),
    Round305TriggerRecord("r10l15_czech_nuclear_T3", "r10_loop15_czech_nuclear_construction_basket", "4B-watch", date(2025, 5, 6), "Czech court temporarily halts signing of $18B KHNP nuclear contract after EDF complaint", "price_data_unavailable_after_deep_search", "legal_4B_watch", "4B-watch", {"court_halt_date": "2025-05-06", "contract_signed_date": "2025-06-04", "signed_contract_value_czk_bn": 407, "signed_contract_value_usd_bn": 18.7}),
    Round305TriggerRecord("r10l15_taeyoung_pf_T2", "r10_loop15_taeyoung_pf_restructuring", "4C-watch", date(2024, 5, 13), "FSS tightens PF restructuring; real estate PF delinquency rises to 2.70% end-2023 from 0.37% end-2021; 1T loan expandable to 5T", "price_data_unavailable_after_deep_search", "PF_4C_watch", "4C-watch", {"pf_delinquency_end_2021_pct": 0.37, "pf_delinquency_end_2023_pct": 2.70, "syndicated_loan_initial_krw_trn": 1.0, "syndicated_loan_max_krw_trn": 5.0}),
    Round305TriggerRecord("r10l15_seoul_housing_T1", "r10_loop15_seoul_housing_supply_reconstruction", "Stage2_policy", date(2024, 8, 16), "Seoul home prices +0.76% in July 2024, fastest since Dec 2019; government plans 400k homes over six years", "price_data_unavailable_after_deep_search", "success_candidate_stage2_policy", "Stage2", {"seoul_price_july_2024_mom_pct": 0.76, "planned_homes_over_6y": 400000, "fastest_since": "2019-12"}),
    Round305TriggerRecord("r10l15_hdc_gwangju_T0", "r10_loop15_hdc_gwangju_quality_hard_4c", "hard_4C", date(2022, 1, 11), "Gwangju Hwajeong I-Park exterior wall collapse kills six; faulty construction and substandard materials later identified", "price_data_unavailable_after_deep_search", "hard_4c_success", "4C", {"fatalities": 6, "investigation_findings": ["faulty_construction_methods", "substandard_building_materials", "unauthorized_structural_change"]}),
    Round305TriggerRecord("r10l15_hyundai_steel_rebar_T1", "r10_loop15_hyundai_steel_rebar_weak_construction_demand", "failed_rerating", date(2024, 6, 21), "Rebar price expected -10%, net profit estimate cut 73% to KRW215B, target cut 14%, shares -1.2% at KRW29,000", -1.2, "failed_rerating_4C_watch", "4C-watch", {"entry_price_anchor_krw": 29000, "expected_rebar_price_decline_pct": -10, "net_profit_estimate_cut_pct": -73, "net_profit_estimate_after_cut_krw_bn": 215}),
    Round305TriggerRecord("r10l15_builder_support_T0", "r10_loop15_builder_liquidity_support_false_positive_watch", "Stage2_relief", date(2024, 3, 27), "KRW40.6T support package for SMEs/builders is survival relief; project cashflow and PF cleanup are still missing", "price_data_unavailable_after_deep_search", "policy_relief_not_Green", "Stage2_relief", {"support_package_2024_03_krw_trn": 40.6, "additional_public_sector_investment_2024_h2_krw_trn": 15, "pf_restructuring_ongoing": True}),
)

ROUND305_CASE_CANDIDATES: tuple[Round305CaseCandidate, ...] = (
    Round305CaseCandidate("r10_loop15_samsung_ea_fadhili", "028050", "Samsung E&A", E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE, (E2RArchetype.OVERSEAS_EPC_ORDER_4B_WATCH, E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN), "success_candidate", "Stage2_Actionable_to_Stage3_Yellow_candidate", "T1/T2", "Stage2-Actionable", "Stage2-Actionable / Stage3-Yellow candidate", date(2024, 4, 3), date(2024, 4, 3), None, date(2024, 4, 3), None, False, ("contract_value_6B_USD", "Aramco_Fadhili_total_package_7_7B_USD", "event_return_plus_8_5pct", "market_relative_return_plus_9_9pp", "average_annual_contract_wins_8_6T_KRW"), ("gross_margin_missing", "cost_overrun_visibility_missing", "cash_collection_schedule_missing", "Saudi_execution_delay_risk", "backlog_to_OP_conversion_missing"), 8.5, None, {"contract_value_usd_bn": 6.0, "aramco_total_package_usd_bn": 7.7, "event_price_high_krw": 26750, "kospi_same_context_pct": -1.4, "market_relative_return_pp": 9.9, "completion_target": "2027-11"}, "aligned", "Stage2_promote_candidate", "unknown", "stage2_watch_success", "Large overseas EPC contract plus strong relative price reaction makes Samsung E&A Stage2-Actionable; Green requires margin and cashflow."),
    Round305CaseCandidate("r10_loop15_gsenc_fadhili_overlay", "006360", "GS E&C", E2RArchetype.OVERSEAS_EPC_MEGA_ORDER_STAGE2_ACTIONABLE, (E2RArchetype.OVERSEAS_EPC_ORDER_4B_WATCH, E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH), "success_candidate", "Stage2_overseas_EPC_evidence", "T0/T1", "Stage2_evidence", "Stage2 overseas EPC evidence", date(2024, 4, 2), date(2024, 4, 2), None, date(2024, 4, 2), None, False, ("Fadhili_EPC_package_participation", "Aramco_total_package_7_7B_USD", "capacity_expansion_2_5_to_4_0_bcf_per_day", "completion_target_2027_11"), ("GS_specific_contract_value_missing", "event_return_missing", "project_margin_missing", "cash_collection_missing", "domestic_PF_quality_overlay"), None, None, {"aramco_total_package_usd_bn": 7.7, "project_capacity_before_bcf_per_day": 2.5, "project_capacity_after_bcf_per_day": 4.0, "completion_target": "2027-11"}, "unknown", "Stage2_evidence_but_not_actionable_without_company_price", "unknown", "stage2_watch_success", "GS E&C has package-level Stage2 EPC evidence, but company-specific contract value, price reaction, margin and domestic overlays remain open."),
    Round305CaseCandidate("r10_loop15_czech_nuclear_construction_basket", "034020/051600/052690/015760_readthrough", "Doosan Enerbility / KEPCO Plant S&E / KEPCO E&C / KHNP", E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2_WITH_LEGAL_4B, (E2RArchetype.NUCLEAR_CONSTRUCTION_EXPORT_STAGE2, E2RArchetype.NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2), "success_candidate", "Stage2_Actionable_with_legal_4B_overlay", "T1/T4", "Stage2-Actionable+4B-watch", "Stage2-Actionable + legal 4B-watch", date(2024, 7, 17), date(2024, 7, 17), None, date(2025, 5, 6), None, False, ("KHNP_preferred_bidder", "two_reactors", "first_major_overseas_nuclear_since_2009", "Doosan_plus_48pct_3m", "signed_contract_18_7B_USD_after_legal_clearance"), ("listed_company_work_share_missing", "EPC_or_design_margin_missing", "payment_schedule_missing", "legal_appeal_resolution_needed", "construction_start_missing"), 48.0, None, {"reactors_count": 2, "unit_cost_estimate_czk_bn": 200, "signed_contract_value_czk_bn": 407, "signed_contract_value_usd_bn": 18.7, "kepco_plant_se_3m_return_pct": 14, "kepco_ec_3m_return_pct": 41}, "aligned", "Stage2_promote_candidate_with_legal_4B_overlay", "event_premium", "stage2_watch_success", "Preferred bidder and supplier basket rerating are Stage2-Actionable, but legal appeal, final work split and margin are Yellow/Green gates."),
    Round305CaseCandidate("r10_loop15_taeyoung_pf_restructuring", "009410", "Taeyoung E&C / PF restructuring reference", E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH, (E2RArchetype.PF_LIQUIDITY_HARD_4C_WATCH, E2RArchetype.REAL_ESTATE_PF_LIQUIDITY_4C_WATCH), "4b_watch", "4C_watch_with_policy_relief", "T0/T2", "4C-watch", "4C-watch / restructuring", date(2023, 12, 1), None, None, date(2024, 5, 13), date(2024, 5, 13), False, ("debt_rescheduling_awareness", "support_package_40_6T_KRW", "PF_delinquency_2_70pct", "syndicated_loan_1T_to_5T_KRW"), ("PF_project_profitability_reassessment_missing", "debt_restructuring_terms_missing", "impairment_size_missing", "cashflow_after_workout_missing", "new_order_access_missing"), None, None, {"support_package_krw_trn": 40.6, "pf_delinquency_end_2021_pct": 0.37, "pf_delinquency_end_2023_pct": 2.70, "syndicated_loan_initial_krw_trn": 1.0, "syndicated_loan_max_krw_trn": 5.0}, "unknown", "thesis_break_watch", "thesis_break", "should_have_been_red", "PF liquidity support is relief, not earnings recovery; impairment cleanup and restructuring terms are required."),
    Round305CaseCandidate("r10_loop15_seoul_housing_supply_reconstruction", "000720/047040/006360/375500/housing_developer_basket", "Hyundai E&C / Daewoo E&C / GS E&C / DL E&C basket", E2RArchetype.HOUSING_SUPPLY_RECONSTRUCTION_STAGE2_POLICY, (E2RArchetype.REAL_ESTATE_POLICY_STAGE2_NOT_GREEN, E2RArchetype.HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF), "success_candidate", "Stage2_policy_mixed", "T1/T3", "Stage2_policy", "Stage2 policy", date(2024, 8, 16), date(2024, 8, 16), None, date(2025, 3, 19), None, False, ("Seoul_price_plus_0_76pct", "400k_homes_over_6y", "LTV_cut_50_to_40pct", "state_land_supply", "reconstruction_regulation_simplification"), ("building_permits_missing", "housing_starts_missing", "presale_rate_missing", "unsold_inventory_absorption_missing", "PF_refinancing_missing", "construction_margin_missing"), None, None, {"seoul_price_july_2024_mom_pct": 0.76, "planned_homes_over_6y": 400000, "ltv_cut_from_pct": 50, "ltv_cut_to_pct": 40}, "missed_due_to_score", "Stage2_policy_not_Green", "event_premium", "stage2_watch_success", "Housing supply and reconstruction policy are Stage2 only until permits, starts, presales and PF repayment are visible."),
    Round305CaseCandidate("r10_loop15_hdc_gwangju_quality_hard_4c", "294870", "HDC Hyundai Development", E2RArchetype.CONSTRUCTION_QUALITY_SAFETY_HARD_4C, (E2RArchetype.CONSTRUCTION_SAFETY_HARD_4C, E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY), "4c_thesis_break", "hard_4c_reference", "T0/T1", "hard_4C", "4C", date(2022, 1, 11), None, None, None, date(2022, 1, 11), True, ("Gwangju_Hwajeong_IPark_collapse", "six_fatalities", "faulty_construction_methods", "substandard_building_materials", "unauthorized_structural_change"), ("fatal_construction_quality_event", "brand_trust_collapse", "permit_or_order_risk", "compensation_and_reconstruction_cost"), None, None, {"fatalities": 6, "incident_date": "2022-01-11", "investigation_findings": ["faulty_construction_methods", "substandard_building_materials", "unauthorized_structural_change"]}, "false_positive_score", "hard_4c_success_quality_safety", "thesis_break", "should_have_been_red", "Construction quality and safety failure is R10 hard 4C and must override backlog or policy positives."),
    Round305CaseCandidate("r10_loop15_hyundai_steel_rebar_weak_construction_demand", "004020", "Hyundai Steel / rebar building-material read-through", E2RArchetype.BUILDING_MATERIAL_WEAK_DEMAND_FAILED_RERATING, (E2RArchetype.CONSTRUCTION_MATERIAL_DEMAND_BREAK, E2RArchetype.BUILDING_MATERIALS_DEMAND_BREAK), "failed_rerating", "failed_rerating_4C_watch", "T1", "failed_rerating", "4C-watch / failed rerating", date(2024, 6, 21), None, None, date(2024, 6, 21), date(2024, 6, 21), False, ("rebar_price_expected_minus_10pct", "net_profit_estimate_cut_73pct", "target_price_cut_14pct", "shares_minus_1_2pct_at_29000_KRW"), ("construction_starts_recovery_missing", "rebar_ASP_recovery_missing", "raw_material_spread_missing", "inventory_drawdown_missing", "infrastructure_order_pull_missing"), None, -1.2, {"entry_price_anchor_krw": 29000, "expected_rebar_price_decline_pct": -10, "net_profit_estimate_after_cut_krw_bn": 215, "net_profit_estimate_cut_pct": -73, "target_price_after_krw": 30000, "target_price_cut_pct": -14}, "evidence_good_but_price_failed", "failed_rerating_4C_watch", "no_rerating", "false_yellow", "Weak construction-material demand and rebar ASP pressure are failed-rerating triggers."),
    Round305CaseCandidate("r10_loop15_builder_liquidity_support_false_positive_watch", "builder_basket", "Korean builder liquidity support basket", E2RArchetype.BUILDER_LIQUIDITY_SUPPORT_FALSE_POSITIVE_WATCH, (E2RArchetype.HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF, E2RArchetype.REAL_ESTATE_PF_RESTRUCTURING_4C_WATCH), "event_premium", "Stage2_relief_false_positive_watch", "T0/T1", "Stage2_relief", "Stage2 relief / false-positive watch", date(2024, 3, 27), date(2024, 3, 27), None, date(2024, 5, 13), None, False, ("support_package_40_6T_KRW", "additional_public_sector_investment_15T_KRW", "PF_restructuring_ongoing"), ("project_profitability_missing", "presale_rate_missing", "PF_maturity_extension_terms_missing", "gross_margin_missing", "cash_collection_missing", "debt_ratio_stabilization_missing"), None, None, {"support_package_2024_03_krw_trn": 40.6, "additional_public_sector_investment_2024_h2_krw_trn": 15, "pf_restructuring_ongoing": True}, "false_positive_score", "policy_relief_not_Green", "event_premium", "false_yellow", "Builder liquidity support is survival relief; project cashflow, presales, PF cleanup and margins are required for Stage3."),
)


def round305_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(case.to_case_record() for case in ROUND305_CASE_CANDIDATES)


def round305_summary() -> dict[str, object]:
    return {
        "source_round": ROUND305_SOURCE_ROUND_PATH,
        "round_id": ROUND305_ANALYST_ROUND_ID,
        "large_sector": ROUND305_LARGE_SECTOR,
        "method": ROUND305_METHOD,
        "case_candidate_count": len(ROUND305_CASE_CANDIDATES),
        "trigger_count": len(ROUND305_TRIGGER_RECORDS),
        "stage2_actionable_candidate_count": 2,
        "stage2_policy_or_relief_count": 3,
        "stage3_yellow_candidate_count": 3,
        "stage3_green_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 5,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 1,
        "failed_rerating_count": 1,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "full_adjusted_ohlc_complete": False,
        "shadow_weight_only": True,
    }


def round305_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(case.as_row() for case in ROUND305_CASE_CANDIDATES)


def round305_trigger_rows() -> tuple[dict[str, str], ...]:
    return tuple(trigger.as_row() for trigger in ROUND305_TRIGGER_RECORDS)


def round305_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"requested_alias": key, "canonical_archetype": value} for key, value in ROUND305_REQUIRED_TARGET_ALIASES.items())


def round305_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND305_SHADOW_WEIGHT_ROWS)


def round305_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    up_points = {
        "contract_value_vs_annual_backlog": "+5",
        "project_margin_visibility": "+5",
        "cash_collection_schedule": "+5",
        "cost_overrun_delay_control": "+5",
        "final_contract_signed_not_preferred_bidder": "+5",
        "legal_appeal_clearance": "+4",
        "housing_starts_presale_rate": "+5",
        "PF_restructuring_completion": "+5",
        "construction_quality_safety_trust": "+5",
        "building_material_spread_visibility": "+4",
    }
    down_points = {
        "headline_order_without_margin": "-5",
        "preferred_bidder_without_final_contract": "-5",
        "policy_support_without_project_cashflow": "-5",
        "housing_supply_headline_without_starts": "-4",
        "PF_liquidity_without_impairment_cleanup": "-5",
        "construction_material_demand_assumption_only": "-4",
        "large_project_without_legal_clearance": "-4",
    }
    rows = []
    for axis in ROUND305_SCORE_UP_AXES:
        rows.append({"axis": axis, "points": up_points[axis], "direction": "raise", "reason": "R10 construction/real-estate/building-material trigger quality axis"})
    for axis in ROUND305_SCORE_DOWN_AXES:
        rows.append({"axis": axis, "points": down_points[axis], "direction": "lower", "reason": "R10 order, policy, PF or material-demand false-positive blocker"})
    return tuple(rows)


def round305_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND305_SOURCE_ROUND_PATH,
        "round_id": ROUND305_ANALYST_ROUND_ID,
        "large_sector": ROUND305_LARGE_SECTOR,
        "method": ROUND305_METHOD,
        "summary": round305_summary(),
        "target_archetypes": dict(ROUND305_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND305_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND305_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND305_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND305_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND305_SCORE_UP_AXES),
        "score_down_axes": list(ROUND305_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND305_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND305_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_apply_round305_shadow_weights_to_production_scoring_yet",
            "do_not_use_round305_cases_as_candidate_generation_input",
            "do_not_treat_construction_policy_or_order_headline_as_green",
            "do_not_downgrade_stage_candidate_only_because_full_ohlc_is_missing",
        ],
    }


def render_round305_summary_markdown() -> str:
    summary = round305_summary()
    lines = [
        "# Round 305 R10 Loop 15 Construction/Real Estate/Building Materials Trigger Validation",
        "",
        "이번 라운드는 수주, 부동산 정책, PF 지원, 건자재 수요를 실제 margin/cashflow 증거와 분리한다.",
        "",
        "쉬운 예: `40.6조원 지원책`은 건설사가 당장 숨을 쉬게 해주는 산소마스크다. 하지만 프로젝트 현금흐름과 PF 정리가 없으면 체력이 좋아진 것은 아니다.",
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
        "stage2_policy_or_relief_count",
        "stage3_yellow_candidate_count",
        "stage3_green_confirmed_count",
        "stage4b_watch_count",
        "stage4c_watch_count",
        "hard_4c_case_count",
        "failed_rerating_count",
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
            "- Samsung E&A / Fadhili is the cleanest Stage2-Actionable case, with a large contract and strong relative price reaction.",
            "- GS E&C / Fadhili remains Stage2 evidence only because company-specific contract value, price reaction and margin are missing.",
            "- Czech nuclear construction basket is Stage2-Actionable with legal 4B overlay; preferred bidder is not final cashflow.",
            "- Taeyoung/PF restructuring is 4C-watch with policy relief; support is not Green until PF cleanup and cashflow are visible.",
            "- Seoul housing supply/reconstruction is Stage2 policy, not Green before permits, starts, presales and PF repayment.",
            "- HDC Gwangju collapse is a hard construction-quality 4C reference.",
            "- Hyundai Steel rebar weak demand is failed rerating for building-material demand/spread.",
            "- Builder liquidity support is a false-positive watch because survival relief is not earnings recovery.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round305_trigger_grid_markdown() -> str:
    lines = [
        "# Round 305 Trigger Grid",
        "",
        "| trigger_id | case_id | date | type | outcome | promote_to | evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for trigger in ROUND305_TRIGGER_RECORDS:
        lines.append(
            f"| {trigger.trigger_id} | {trigger.case_id} | {trigger.trigger_date.isoformat()} | {trigger.trigger_type} | {trigger.trigger_outcome_label} | {trigger.promote_to} | {trigger.evidence_available} |"
        )
    return "\n".join(lines) + "\n"


def render_round305_stage_rules_markdown() -> str:
    lines = ["# Round 305 Stage Rules", "", "Do not apply these weights to production scoring yet.", "", "## Stage2-Actionable", ""]
    lines.extend(f"- {rule}" for rule in ROUND305_STAGE2_ACTIONABLE_RULES)
    lines.extend(["", "## Stage3-Yellow", ""])
    lines.extend(f"- {rule}" for rule in ROUND305_STAGE3_YELLOW_RULES)
    lines.extend(["", "## Stage3-Green", ""])
    lines.extend(f"- {rule}" for rule in ROUND305_STAGE3_GREEN_RULES)
    lines.extend(["", "## Green Blockers", ""])
    lines.extend(f"- {rule}" for rule in ROUND305_GREEN_BLOCKERS)
    return "\n".join(lines) + "\n"


def render_round305_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 305 4B/4C Review",
        "",
        "이번 라운드에서 Stage3-Green 확정은 없다. EPC 수주, 원전 preferred bidder, 주택공급 정책, PF 지원은 4B/false-positive watch가 필요하고, 건설 품질·안전 사고는 hard 4C다.",
        "",
        "## 4B Watch",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND305_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {item}" for item in ROUND305_HARD_4C_GATES)
    lines.extend(["", "## Confirmed Hard 4C", "", "- HDC Gwangju Hwajeong I-Park collapse"])
    return "\n".join(lines) + "\n"


def render_round305_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round 305 Price Validation Plan",
            "",
            "- reported_event_anchor_not_full_ohlc 상태를 유지한다.",
            "- full adjusted OHLC가 없다는 이유로 Stage2-Actionable, Stage3-Yellow candidate, 4B-watch 또는 4C 후보를 강등하지 않는다.",
            "- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.",
            "- 다음 단계에서는 trigger date 기준 30/90/180일 MFE/MAE, EPC margin, cash collection, legal clearance, housing starts, presale rate, PF cleanup, rebar ASP/spread를 채운다.",
            "",
        ]
    )


def write_round305_r10_loop15_reports(
    *,
    output_directory: str | Path = ROUND305_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND305_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND305_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND305_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND305_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round305_case_records(), cases_path),
        "triggers": write_round305_triggers(triggers_path),
        "audit": _write_json(round305_audit_payload(), audit_path),
        "weight_profile": _write_csv(round305_shadow_weight_rows(), weight_profile_path),
        "summary": output / "round305_r10_loop15_trigger_validation_summary.md",
        "case_matrix": output / "round305_r10_loop15_case_matrix.csv",
        "trigger_grid": output / "round305_r10_loop15_trigger_grid.csv",
        "target_aliases": output / "round305_r10_loop15_target_aliases.csv",
        "score_adjustments": output / "round305_r10_loop15_score_adjustments.csv",
        "shadow_weights": output / "round305_r10_loop15_shadow_weights.csv",
        "stage_rules": output / "round305_r10_loop15_stage_rules.md",
        "trigger_grid_md": output / "round305_r10_loop15_trigger_grid.md",
        "price_validation_plan": output / "round305_r10_loop15_price_validation_plan.md",
        "stage4b_4c_review": output / "round305_r10_loop15_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round305_summary_markdown(), encoding="utf-8")
    _write_csv(round305_case_rows(), paths["case_matrix"])
    _write_csv(round305_trigger_rows(), paths["trigger_grid"])
    _write_csv(round305_target_alias_rows(), paths["target_aliases"])
    _write_csv(round305_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round305_shadow_weight_rows(), paths["shadow_weights"])
    paths["stage_rules"].write_text(render_round305_stage_rules_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round305_trigger_grid_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round305_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round305_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def write_round305_triggers(path: str | Path = ROUND305_DEFAULT_TRIGGERS_PATH) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(trigger.as_dict(), ensure_ascii=False, sort_keys=True) for trigger in ROUND305_TRIGGER_RECORDS]
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
