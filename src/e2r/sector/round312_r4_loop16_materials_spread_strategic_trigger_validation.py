"""Round-312 R4 Loop-16 materials, spread and strategic-resources validation.

This module converts ``docs/round/round_312.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a steel anti-dumping duty can be Stage2 relief when domestic
spread improves. It is still not Green until ASP, volume, margin and export
tariff absorption are visible in company evidence.
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


ROUND312_SOURCE_ROUND_PATH = "docs/round/round_312.md"
ROUND312_ANALYST_ROUND_ID = "round_240"
ROUND312_LARGE_SECTOR = "MATERIALS_SPREAD_STRATEGIC_RESOURCES"
ROUND312_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND312_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round312_r4_loop16_materials_spread_strategic_trigger_validation"
ROUND312_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r4_loop16_round240.jsonl"
ROUND312_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r4_loop16_round240.jsonl"
ROUND312_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round312_r4_loop16_materials_spread_strategic_trigger_validation_audit.json"
ROUND312_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round240_r4_loop16_v1.csv"

ROUND312_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF": E2RArchetype.STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF.value,
    "STEEL_US_LOCALIZATION_CAPEX_4B": E2RArchetype.STEEL_US_LOCALIZATION_CAPEX_4B.value,
    "PETROCHEMICAL_OVER_SUPPLY_FAILED_RERATING": E2RArchetype.PETROCHEMICAL_OVER_SUPPLY_FAILED_RERATING.value,
    "PETROCHEMICAL_CAPACITY_RESTRUCTURING_STAGE2_RELIEF": E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING_STAGE2_RELIEF.value,
    "CRITICAL_MINERALS_REFINERY_STAGE2_WITH_DILUTION_4B": E2RArchetype.CRITICAL_MINERALS_REFINERY_STAGE2_WITH_DILUTION_4B.value,
    "LITHIUM_MINE_JV_STRATEGIC_RESOURCE_STAGE2": E2RArchetype.LITHIUM_MINE_JV_STRATEGIC_RESOURCE_STAGE2.value,
    "LITHIUM_PRICE_BETA_CYCLICAL_STAGE2": E2RArchetype.LITHIUM_PRICE_BETA_CYCLICAL_STAGE2.value,
    "COPPER_TC_RC_SPREAD_4C_WATCH": E2RArchetype.COPPER_TC_RC_SPREAD_4C_WATCH.value,
    "SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2": E2RArchetype.SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2.value,
}

ROUND312_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "commodity_price_or_policy_change_links_to_company_ASP_or_margin",
    "event_return_at_least_5pct_or_market_relative_return_at_least_5pp",
    "supply_restriction_has_duration_not_one_day_headline",
    "strategic_resource_investment_links_to_offtake_customer_government_funding_or_margin",
    "restructuring_has_actual_capacity_shutdown_or_merger_execution",
    "no_dilution_governance_export_tariff_or_TC_RC_4B_4C_overlay",
)

ROUND312_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_FCF_path_can_change_materially",
    "one_of_spread_margin_offtake_capacity_cut_dilution_or_commercialization_gate_remains_open",
    "reported_price_anchor_or_relative_strength_supports_trigger",
    "case_is_not_pure_commodity_beta_capex_optional_or_restructuring_plan",
)

ROUND312_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "commodity_price_or_policy_change_converts_to_gross_margin_and_OP",
    "strategic_resource_investment_has_clear_offtake_or_customer_demand",
    "dilution_governance_overhang_is_resolved_or_priced",
    "restructuring_results_in_real_capacity_cut_and_spread_improvement",
    "lithium_copper_or_steel_spread_is_durable_across_quarters",
    "commercialization_contract_and_customer_adoption_are_visible_for_new_materials",
    "full_adjusted_OHLC_MFE_MAE_path_supports_stage_candidate",
)

ROUND312_GREEN_BLOCKERS: tuple[str, ...] = (
    "commodity_price_headline_without_margin",
    "tariff_policy_without_spread_proof",
    "strategic_resource_capex_without_offtake",
    "restructuring_plan_without_shutdown",
    "petrochemical_recovery_without_capacity_cut",
    "lithium_JV_without_issuer_price_anchor",
    "copper_bull_without_TC_RC",
    "sodium_ion_TAM_without_customer_contract",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND312_SCORE_UP_AXES: tuple[str, ...] = (
    "domestic_spread_recovery",
    "tariff_exposure_absorption",
    "actual_capacity_cut",
    "naphtha_spread_recovery",
    "strategic_resource_offtake",
    "dilution_governance_overlay",
    "lithium_price_duration",
    "smelter_TC_RC_margin",
    "commercialization_contract",
)

ROUND312_SCORE_DOWN_AXES: tuple[str, ...] = (
    "commodity_price_headline_without_margin",
    "tariff_policy_without_spread_proof",
    "strategic_resource_capex_without_offtake",
    "restructuring_plan_without_shutdown",
    "petrochemical_recovery_without_capacity_cut",
    "lithium_JV_without_price_anchor",
    "copper_bull_without_TCRC",
)

ROUND312_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "strategic_mineral_investment_requires_large_share_issuance",
    "commodity_price_spike_has_no_margin_confirmation",
    "plant_localization_capex_reverses_price_intraday",
    "restructuring_plan_announced_before_shutdown_execution",
    "lithium_mine_suspension_can_reverse_after_license_renewal",
    "copper_price_rises_while_TC_RC_collapses",
)

ROUND312_4C_WATCH_GATES: tuple[str, ...] = (
    "export_tariff_destroys_spread",
    "commodity_spread_collapse",
    "smelter_TC_RC_negative_economics",
    "dilutive_issuance_under_control_battle",
    "petrochemical_oversupply_persistent_operating_loss",
    "strategic_mine_acquisition_without_offtake_and_falling_price",
    "regulatory_or_court_investigation_into_share_issuance_or_governance",
)

ROUND312_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_policy_spread_contract_capacity_loss_or_tariff_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_commodity_price_capex_restructuring_or_strategic_resource_headline_as_margin_offtake_or_FCF",
)


@dataclass(frozen=True)
class Round312ShadowWeightRow:
    archetype: E2RArchetype
    domestic_spread_recovery: int
    tariff_exposure_absorption: int
    actual_capacity_cut: int
    naphtha_spread_recovery: int
    strategic_resource_offtake: int
    dilution_governance_overlay: int
    lithium_price_duration: int
    smelter_tcrc_margin: int
    commercialization_contract: int
    commodity_price_headline_without_margin_penalty: int
    tariff_policy_without_spread_proof_penalty: int
    strategic_resource_capex_without_offtake_penalty: int
    restructuring_plan_without_shutdown_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "domestic_spread_recovery": _signed(self.domestic_spread_recovery),
            "tariff_exposure_absorption": _signed(self.tariff_exposure_absorption),
            "actual_capacity_cut": _signed(self.actual_capacity_cut),
            "naphtha_spread_recovery": _signed(self.naphtha_spread_recovery),
            "strategic_resource_offtake": _signed(self.strategic_resource_offtake),
            "dilution_governance_overlay": _signed(self.dilution_governance_overlay),
            "lithium_price_duration": _signed(self.lithium_price_duration),
            "smelter_TC_RC_margin": _signed(self.smelter_tcrc_margin),
            "commercialization_contract": _signed(self.commercialization_contract),
            "commodity_price_headline_without_margin_penalty": _signed(self.commodity_price_headline_without_margin_penalty),
            "tariff_policy_without_spread_proof_penalty": _signed(self.tariff_policy_without_spread_proof_penalty),
            "strategic_resource_capex_without_offtake_penalty": _signed(self.strategic_resource_capex_without_offtake_penalty),
            "restructuring_plan_without_shutdown_penalty": _signed(self.restructuring_plan_without_shutdown_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round312TriggerRecord:
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
class Round312CaseCandidate:
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
            "do_not_use_round312_cases_as_candidate_generation_input",
            "do_not_treat_commodity_price_strategic_resource_capex_or_restructuring_headline_as_green_without_spread_margin_offtake_or_FCF",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND312_LARGE_SECTOR,
            large_sector=ROUND312_LARGE_SECTOR,
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
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4b" in field or "dilution" in field or "governance" in field or "capex" in field),
            stage4c_evidence=tuple(
                field
                for field in (*self.red_flag_fields, *self.evidence_fields)
                if "4c" in field or "tariff" in field or "oversupply" in field or "loss" in field or "TC_RC" in field or "spread" in field
            ),
            must_have_fields=ROUND312_STAGE3_GREEN_RULES,
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
                stage_dates_confidence=0.78 if not self.stage4c_date else 0.84,
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


ROUND312_CASE_CANDIDATES: tuple[Round312CaseCandidate, ...] = (
    Round312CaseCandidate(
        "r4_loop16_hyundai_steel_posco_tariff_antidumping",
        "004020/005490",
        "Hyundai Steel / POSCO Holdings",
        E2RArchetype.STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF,
        (E2RArchetype.STEEL_TARIFF_EXPORT_RISK, E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF),
        "event_premium",
        "mixed_tariff_4C_and_antidumping_relief",
        "r4l16_steel_us_tariff_T0/r4l16_steel_antidumping_T1",
        "4C_tariff_shock_plus_Stage2_antidumping_relief",
        "4C-watch + Stage2 relief",
        date(2025, 2, 10),
        date(2025, 2, 20),
        None,
        date(2025, 2, 10),
        date(2025, 2, 10),
        False,
        ("us_steel_aluminum_tariff_25pct", "POSCO_tariff_minus_3_6pct_230500_krw", "Hyundai_Steel_tariff_minus_2_9pct", "Korea_antidumping_27_91_to_38_02pct", "Hyundai_Steel_antidumping_plus_5_8pct", "POSCO_antidumping_plus_3_9pct"),
        ("export_margin_4c_watch", "domestic_ASP_recovery_missing", "import_volume_reduction_missing", "raw_material_cost_pass_through_missing", "quarterly_steel_spread_missing"),
        5.8,
        -3.6,
        230500,
        None,
        None,
        230500,
        {"us_steel_aluminum_tariff_pct": 25, "posco_tariff_event_return_pct": -3.6, "posco_tariff_event_price_krw": 230500, "hyundai_steel_tariff_event_return_pct": -2.9, "kospi_tariff_context_pct": -0.5, "china_steel_plate_antidumping_rate_pct": "27.91-38.02", "hyundai_steel_antidumping_event_return_pct": 5.8, "posco_antidumping_event_return_pct": 3.9, "kospi_antidumping_context_pct": -0.7, "china_steel_import_value_2024_usd_bn": 10.4, "china_share_of_korea_steel_imports_pct": 49},
        "aligned",
        "mixed_tariff_4C_and_antidumping_relief",
        "event_premium",
        "stage2_watch_success",
        "U.S. tariff hurts export spread while Korea anti-dumping supports domestic spread. They must be scored separately.",
    ),
    Round312CaseCandidate(
        "r4_loop16_hyundai_steel_louisiana_capex",
        "004020",
        "Hyundai Steel",
        E2RArchetype.STEEL_US_LOCALIZATION_CAPEX_4B,
        (E2RArchetype.SPECIALTY_STEEL_US_LOCALIZATION_OPTION, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE),
        "failed_rerating",
        "capex_localization_price_reversal_4B",
        "r4l16_hyundai_steel_louisiana_T1",
        "Stage2_capex_with_4B_ROI_gate",
        "Stage2 capex + 4B-watch",
        date(2025, 3, 25),
        date(2025, 3, 25),
        None,
        date(2025, 3, 25),
        None,
        False,
        ("5_8bn_usd_louisiana_plant", "2_7mn_tonnes_annual_capacity", "hyundai_group_21bn_usd_us_investment", "initial_event_return_plus_5pct", "late_session_return_minus_4_4pct"),
        ("capex_ROI_missing", "tariff_savings_missing", "steel_margin_missing", "customer_offtake_terms_missing", "price_reversal_4b"),
        5.0,
        -4.4,
        None,
        None,
        None,
        None,
        {"plant_investment_usd_bn": 5.8, "annual_capacity_mn_tons": 2.7, "initial_event_return_pct": 5, "late_session_event_return_pct": -4.4, "hyundai_motor_event_return_pct": 7.5, "kia_event_return_pct": 4.3, "hyundai_group_us_investment_usd_bn": 21},
        "evidence_good_but_price_failed",
        "capex_localization_price_reversal_4B",
        "no_rerating",
        "should_have_been_red",
        "Localization capex is not Green before utilization, tariff savings, customer offtake and capex ROI.",
    ),
    Round312CaseCandidate(
        "r4_loop16_lgchem_lotte_petrochemical_oversupply",
        "051910/011170",
        "LG Chem / Lotte Chemical",
        E2RArchetype.PETROCHEMICAL_OVER_SUPPLY_FAILED_RERATING,
        (E2RArchetype.PETROCHEMICAL_SPREAD_COLLAPSE_4C, E2RArchetype.CHEMICAL_SPREAD),
        "failed_rerating",
        "failed_rerating_spread_4C_watch",
        "r4l16_petrochem_oversupply_T0",
        "4C_watch_failed_spread",
        "4C-watch",
        date(2025, 2, 7),
        None,
        None,
        None,
        date(2025, 2, 7),
        False,
        ("Lotte_Chemical_2024_OP_loss_895bn_krw", "Lotte_loss_yoy_plus_157pct", "LG_Chem_2024_OP_minus_63_75pct", "LG_Chem_petrochemical_Q4_loss_99bn_krw", "China_Middle_East_oversupply"),
        ("petrochemical_oversupply", "operating_loss", "naphtha_spread_recovery_missing", "capacity_cut_missing", "China_demand_weak"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"lotte_chemical_2024_op_loss_krw_bn": 895, "lotte_chemical_op_loss_yoy_pct": 157, "lotte_loss_context": "largest_operating_loss_since_2011", "lg_chem_2024_op_krw_bn": 916.8, "lg_chem_op_yoy_pct": -63.75, "lg_chem_op_context": "lowest_since_2019", "lg_chem_petrochemical_q4_loss_krw_bn": 99},
        "aligned",
        "failed_rerating_spread_4C_watch",
        "thesis_break",
        "should_have_been_red",
        "Petrochemical oversupply and spread collapse are failed-rerating evidence until capacity cut and spread recovery appear.",
    ),
    Round312CaseCandidate(
        "r4_loop16_lotte_hdhyundai_petrochemical_restructuring",
        "011170/HD_Hyundai_Chemical_readthrough",
        "Lotte Chemical / HD Hyundai Chemical",
        E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING_STAGE2_RELIEF,
        (E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING, E2RArchetype.PETROCHEMICAL_RESTRUCTURING_STAGE2_NOT_GREEN),
        "success_candidate",
        "Stage2_restructuring_relief",
        "r4l16_petrochem_restructuring_T0",
        "Stage2_restructuring_relief",
        "Stage2 relief",
        date(2025, 11, 26),
        date(2025, 11, 26),
        None,
        date(2025, 11, 26),
        None,
        False,
        ("Lotte_Daesan_spinoff", "HD_Hyundai_Chemical_merger_plan", "government_capacity_cut_target_25pct", "national_capacity_cut_3_7mn_tons_per_year", "Lotte_Daesan_capacity_1_1mn_tons", "HD_Hyundai_capacity_0_85mn_tons"),
        ("actual_capacity_shutdown_missing", "naphtha_spread_recovery_missing", "operating_loss_reduction_missing", "tax_legal_support_missing", "restructuring_plan_without_shutdown"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"lotte_daesan_capacity_mn_tons": 1.1, "hd_hyundai_chemical_capacity_mn_tons": 0.85, "government_capacity_cut_target_pct": 25, "national_capacity_cut_target_mn_tons_per_year": 3.7},
        "unknown",
        "Stage2_relief_not_Green",
        "unknown",
        "stage2_watch_success",
        "Petrochemical restructuring is Stage2 relief, not Yellow or Green until actual shutdown and spread recovery confirm.",
    ),
    Round312CaseCandidate(
        "r4_loop16_korea_zinc_tennessee_critical_minerals",
        "010130/000670",
        "Korea Zinc / YoungPoong",
        E2RArchetype.CRITICAL_MINERALS_REFINERY_STAGE2_WITH_DILUTION_4B,
        (E2RArchetype.CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B, E2RArchetype.STRATEGIC_METALS_DILUTION_GOVERNANCE),
        "4b_watch",
        "Stage2_strategic_resource_with_governance_4B",
        "r4l16_koreazinc_refinery_T0/r4l16_koreazinc_court_T2",
        "Stage2_strategic_resource_with_dilution_4B",
        "Stage2 + 4B-watch",
        date(2025, 12, 16),
        date(2025, 12, 16),
        None,
        date(2025, 12, 16),
        None,
        False,
        ("Tennessee_critical_minerals_refinery_7_4bn_usd", "new_share_sale_1_9bn_usd", "US_government_led_JV_10pct_stake", "injunction_event_minus_13pct", "court_rejection_relief_plus_5pct", "YoungPoong_minus_10_5pct"),
        ("dilution", "control_battle", "governance_risk", "offtake_missing", "refinery_economics_missing", "fairness_of_terms_missing"),
        5.0,
        -13.0,
        None,
        None,
        None,
        None,
        {"refinery_project_value_usd_bn": 7.4, "new_share_sale_value_usd_bn": 1.9, "us_government_led_jv_stake_pct": 10, "injunction_news_event_return_pct": -13, "court_rejection_date": "2025-12-24", "korea_zinc_relief_event_return_pct": 5, "young_poong_relief_event_return_pct": -10.5},
        "aligned",
        "Stage2_strategic_resource_with_governance_4B",
        "event_premium",
        "stage2_watch_success",
        "Critical minerals refinery is strategic Stage2, but dilution and governance remain 4B overlays.",
    ),
    Round312CaseCandidate(
        "r4_loop16_posco_minres_lithium_jv",
        "005490",
        "POSCO Holdings / Mineral Resources",
        E2RArchetype.LITHIUM_MINE_JV_STRATEGIC_RESOURCE_STAGE2,
        (E2RArchetype.LITHIUM_RESOURCE_INTEGRATION_STAGE2, E2RArchetype.LITHIUM_BATTERY_RAW_MATERIAL),
        "success_candidate",
        "Stage2_strategic_resource_downcycle",
        "r4l16_posco_minres_T0",
        "Stage2_strategic_resource_downcycle",
        "Stage2",
        date(2025, 11, 11),
        date(2025, 11, 11),
        None,
        date(2025, 11, 11),
        None,
        False,
        ("MinRes_lithium_business_30pct_stake", "transaction_value_765mn_usd", "indirect_Wodgina_15pct", "indirect_Mt_Marion_15pct", "MinRes_event_return_plus_10_8pct", "spodumene_880_vs_2022_peak_over_6000"),
        ("POSCO_price_anchor_missing", "offtake_terms_missing", "lithium_hydroxide_margin_missing", "mine_cost_curve_missing", "battery_material_customer_demand_missing"),
        10.8,
        None,
        None,
        None,
        None,
        None,
        {"transaction_value_usd_mn": 765, "stake_in_minres_lithium_business_pct": 30, "indirect_stake_wodgina_pct": 15, "indirect_stake_mt_marion_pct": 15, "minres_event_return_pct": 10.8, "posco_direct_price_anchor": "price_data_unavailable_after_deep_search", "spodumene_mid_june_low_usd_per_ton": 610, "spodumene_august_rebound_usd_per_ton": 880, "spodumene_2022_peak_usd_per_ton": ">6000"},
        "evidence_good_but_price_failed",
        "Stage2_strategic_resource_not_Green",
        "unknown",
        "stage2_watch_success",
        "Lithium mine stake improves resource security, but POSCO price anchor, offtake economics and lithium margin are missing.",
    ),
    Round312CaseCandidate(
        "r4_loop16_catl_yichun_korea_lithium_beta",
        "003670/066970/006400/373220",
        "POSCO Future M / L&F / Samsung SDI / LGES",
        E2RArchetype.LITHIUM_PRICE_BETA_CYCLICAL_STAGE2,
        (E2RArchetype.LITHIUM_PRICE_EVENT_PREMIUM, E2RArchetype.BATTERY_MATERIAL_LITHIUM_BETA_EVENT_PREMIUM),
        "cyclical_success",
        "cyclical_lithium_beta_event_premium",
        "r4l16_catl_lithium_T0",
        "cyclical_Stage2_event_premium",
        "cyclical Stage2",
        date(2025, 8, 11),
        date(2025, 8, 11),
        None,
        date(2025, 8, 11),
        None,
        False,
        ("CATL_Yichun_mine_suspension", "license_expiry_2025_08_09", "lithium_futures_plus_8pct", "POSCO_Future_M_plus_8_3pct", "L_and_F_plus_10pct", "Samsung_SDI_plus_3_2pct", "LGES_plus_2_8pct"),
        ("license_renewal_risk", "sustained_lithium_price_rebound_missing", "cathode_ASP_pass_through_missing", "inventory_write_down_reversal_missing", "material_margin_recovery_missing"),
        10.0,
        None,
        None,
        None,
        None,
        None,
        {"catl_mine": "Yichun_Jianxiawo", "license_expiry_date": "2025-08-09", "lithium_futures_event_return_pct": 8, "posco_future_m_event_return_pct": 8.3, "l_and_f_event_return_pct": 10, "samsung_sdi_event_return_pct": 3.2, "lges_event_return_pct": 2.8, "lithium_price_decline_from_2022_peak_pct": 90, "mine_capacity_lce_tons_per_year": 46000, "forecast_global_output_share_2025_pct": 3},
        "aligned",
        "cyclical_lithium_beta_not_Green",
        "cyclical_rerating",
        "stage2_watch_success",
        "Lithium beta rally is not Green unless company-specific cathode ASP, inventory reversal and margin recovery appear.",
    ),
    Round312CaseCandidate(
        "r4_loop16_copper_tcrc_spread_watch",
        "copper_smelter_basket/010130_readthrough/LS_MnM_private_readthrough",
        "Copper smelter spread basket",
        E2RArchetype.COPPER_TC_RC_SPREAD_4C_WATCH,
        (E2RArchetype.COPPER_TCRC_SPREAD_4C_WATCH, E2RArchetype.NONFERROUS_STRATEGIC_METALS),
        "4c_thesis_break",
        "4C_watch_spread_compression",
        "r4l16_copper_tcrc_T1",
        "4C_watch_spread_compression",
        "4C-watch",
        date(2025, 10, 15),
        None,
        None,
        None,
        date(2025, 10, 15),
        False,
        ("Japan_Spain_South_Korea_warning", "TC_RC_unsustainable", "tight_concentrate_supply", "China_smelting_capacity_expansion", "smelters_processing_at_zero_or_loss"),
        ("copper_bull_without_TC_RC", "smelter_margin_squeeze", "concentrate_shortage", "TC_RC_negative_economics", "direct_KRX_price_anchor_missing"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"countries_warning": ["Japan", "Spain", "South_Korea"], "issue": "copper_treatment_refining_charges_unsustainable", "drivers": ["tight_copper_concentrate_supply", "China_smelting_capacity_expansion", "smelters_processing_at_zero_or_loss", "negative_TC_RC_risk"]},
        "aligned",
        "copper_price_not_equal_smelter_margin",
        "thesis_break",
        "should_have_been_red",
        "Copper price strength does not equal smelter margin when TC/RC collapses.",
    ),
    Round312CaseCandidate(
        "r4_loop16_lgchem_sinopec_sodium_ion_materials",
        "051910",
        "LG Chem / Sinopec",
        E2RArchetype.SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2,
        (E2RArchetype.SODIUM_ION_NEXTGEN_MATERIALS, E2RArchetype.SODIUM_ION_SUBSTITUTION_OVERLAY),
        "success_candidate",
        "Stage2_material_optionality",
        "r4l16_lgchem_sinopec_sodium_T0",
        "Stage2_material_optionality",
        "Stage2 optionality",
        date(2025, 11, 4),
        date(2025, 11, 4),
        None,
        date(2025, 11, 4),
        None,
        False,
        ("Sinopec_LG_Chem_sodium_ion_partnership", "ESS_and_low_speed_EV_target", "China_market_10GWh_2025_to_292GWh_2034", "China_global_output_share_2030_over_90pct"),
        ("commercialization_timeline_missing", "customer_contract_missing", "material_ASP_missing", "gross_margin_missing", "plant_capacity_missing", "China_policy_dependence"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"partner": "Sinopec", "technology": "sodium_ion_battery_materials", "target_markets": ["energy_storage_systems", "low_speed_EVs", "China", "global"], "china_sodium_ion_market_2025_gwh": 10, "china_sodium_ion_market_2034_gwh": 292, "china_global_output_share_2030_pct": ">90"},
        "unknown",
        "Stage2_optionality_not_Green",
        "unknown",
        "stage2_watch_success",
        "Sodium-ion material partnership is optionality until commercialization and customer contracts appear.",
    ),
)


ROUND312_TRIGGER_RECORDS: tuple[Round312TriggerRecord, ...] = (
    Round312TriggerRecord("r4l16_steel_us_tariff_T0", "r4_loop16_hyundai_steel_posco_tariff_antidumping", "4C-watch", "2025-02-10", "Planned 25% U.S. steel/aluminum tariffs; POSCO -3.6% to 230,500 won, Hyundai Steel -2.9%, KOSPI -0.5%", "POSCO -3.6 / Hyundai Steel -2.9", "tariff_export_spread_4C_watch", "4C-watch", {"posco_tariff_event_price_krw": 230500}),
    Round312TriggerRecord("r4l16_steel_antidumping_T1", "r4_loop16_hyundai_steel_posco_tariff_antidumping", "Stage2_relief", "2025-02-20", "Korea recommends 27.91-38.02% anti-dumping duties on Chinese steel plates; Hyundai Steel +5.8%, POSCO +3.9%, KOSPI -0.7%", "Hyundai Steel +5.8 / POSCO +3.9", "domestic_spread_relief", "Stage2_relief", {"hyundai_steel_antidumping_event_return_pct": 5.8, "posco_antidumping_event_return_pct": 3.9}),
    Round312TriggerRecord("r4l16_hyundai_steel_louisiana_T1", "r4_loop16_hyundai_steel_louisiana_capex", "Stage2_capex_with_4B", "2025-03-25", "Hyundai Steel announces $5.8B Louisiana plant with 2.7M tonnes capacity; shares initially +5% then -4.4%", -4.4, "capex_ROI_4B_price_reversal", "4B-watch", {"initial_event_return_pct": 5, "plant_investment_usd_bn": 5.8}),
    Round312TriggerRecord("r4l16_petrochem_oversupply_T0", "r4_loop16_lgchem_lotte_petrochemical_oversupply", "4C-watch", "2025-02-07", "Lotte Chemical 2024 OP loss 895B won, +157% YoY; LG Chem OP -63.75% YoY, petrochemical Q4 loss 99B won", "price_data_unavailable_after_deep_search", "failed_rerating_spread_4C_watch", "4C-watch", {"lotte_chemical_2024_op_loss_krw_bn": 895}),
    Round312TriggerRecord("r4l16_petrochem_restructuring_T0", "r4_loop16_lotte_hdhyundai_petrochemical_restructuring", "Stage2_relief", "2025-11-26", "Lotte Daesan spinoff and HD Hyundai Chemical merger plan; government seeks up to 25% capacity cut and 3.7M tons/year reduction", "price_data_unavailable_after_deep_search", "restructuring_relief_not_Green", "Stage2_relief", {"national_capacity_cut_target_mn_tons_per_year": 3.7}),
    Round312TriggerRecord("r4l16_koreazinc_refinery_T0", "r4_loop16_korea_zinc_tennessee_critical_minerals", "Stage2+4B", "2025-12-16", "$7.4B Tennessee critical minerals refinery; $1.9B share sale to U.S. government-led JV; Korea Zinc -13% after injunction news", -13, "strategic_resource_with_dilution_4B", "Stage2+4B", {"refinery_project_value_usd_bn": 7.4, "new_share_sale_value_usd_bn": 1.9}),
    Round312TriggerRecord("r4l16_koreazinc_court_T2", "r4_loop16_korea_zinc_tennessee_critical_minerals", "relief_validation", "2025-12-24", "Court rejects injunction; Korea Zinc up as much as 5%, YoungPoong down 10.5%", "Korea Zinc +5 / YoungPoong -10.5", "legal_relief_but_governance_4B_remains", "Stage2_relief", {"korea_zinc_relief_event_return_pct": 5, "young_poong_relief_event_return_pct": -10.5}),
    Round312TriggerRecord("r4l16_posco_minres_T0", "r4_loop16_posco_minres_lithium_jv", "Stage2_strategic_resource", "2025-11-11", "POSCO buys 30% stake in part of MinRes lithium business for $765M; indirect 15% stakes in Wodgina and Mt Marion; MinRes +10.8%", "MinRes +10.8 / POSCO unavailable", "Stage2_strategic_resource_not_Green", "Stage2", {"transaction_value_usd_mn": 765}),
    Round312TriggerRecord("r4l16_catl_lithium_T0", "r4_loop16_catl_yichun_korea_lithium_beta", "cyclical_Stage2", "2025-08-11", "CATL Yichun mine suspension; lithium futures +8%, POSCO Future M +8.3%, L&F +10%, Samsung SDI +3.2%, LGES +2.8%", "POSCO Future M +8.3 / L&F +10", "cyclical_lithium_beta", "Stage2_cyclical", {"lithium_futures_event_return_pct": 8, "l_and_f_event_return_pct": 10}),
    Round312TriggerRecord("r4l16_copper_tcrc_T1", "r4_loop16_copper_tcrc_spread_watch", "4C-watch", "2025-10-15", "Japan, Spain and South Korea warn copper TC/RCs are unsustainable amid tight concentrate supply and China smelting expansion", "price_data_unavailable_after_deep_search", "copper_spread_4C_watch", "4C-watch", {"issue": "copper_treatment_refining_charges_unsustainable"}),
    Round312TriggerRecord("r4l16_lgchem_sinopec_sodium_T0", "r4_loop16_lgchem_sinopec_sodium_ion_materials", "Stage2_optionality", "2025-11-04", "Sinopec and LG Chem agree to jointly develop sodium-ion battery materials; China sodium-ion market expected 10GWh in 2025 to 292GWh in 2034", "price_data_unavailable_after_deep_search", "Stage2_material_optionality_not_Green", "Stage2", {"china_sodium_ion_market_2034_gwh": 292}),
)


ROUND312_SHADOW_WEIGHT_ROWS: tuple[Round312ShadowWeightRow, ...] = (
    Round312ShadowWeightRow(E2RArchetype.STEEL_TARIFF_4C_AND_ANTIDUMPING_RELIEF, 5, 5, 0, 0, 0, 1, 0, 0, 0, -2, -4, -1, -1, "anti-dumping/tariff event", "actual spread missing", "ASP+spread+margin", "Hyundai Steel/POSCO tariff vs anti-dumping."),
    Round312ShadowWeightRow(E2RArchetype.STEEL_US_LOCALIZATION_CAPEX_4B, 2, 5, 0, 0, 0, 2, 0, 0, 0, -2, -3, -4, -1, "U.S. plant capex", "capex ROI missing", "utilization+tariff savings+margin", "Hyundai Steel Louisiana."),
    Round312ShadowWeightRow(E2RArchetype.PETROCHEMICAL_OVER_SUPPLY_FAILED_RERATING, 0, 0, 4, 5, 0, 1, 0, 0, 0, -3, -1, -1, -5, "oversupply/losses", "capacity cuts missing", "N/A", "LG Chem/Lotte oversupply."),
    Round312ShadowWeightRow(E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING_STAGE2_RELIEF, 0, 0, 5, 5, 0, 1, 0, 0, 0, -2, -1, -1, -5, "restructuring plan", "shutdown/spread missing", "capacity cut+spread recovery", "Lotte/HD Hyundai."),
    Round312ShadowWeightRow(E2RArchetype.CRITICAL_MINERALS_REFINERY_STAGE2_WITH_DILUTION_4B, 0, 0, 0, 0, 5, 5, 2, 2, 2, -2, -1, -5, -1, "critical minerals refinery", "offtake/governance missing", "offtake+margin+dilution clarity", "Korea Zinc."),
    Round312ShadowWeightRow(E2RArchetype.LITHIUM_MINE_JV_STRATEGIC_RESOURCE_STAGE2, 0, 0, 0, 0, 5, 2, 5, 0, 2, -5, -1, -5, -1, "lithium mine stake", "offtake/margin missing", "offtake+hydroxide margin", "POSCO/MinRes."),
    Round312ShadowWeightRow(E2RArchetype.LITHIUM_PRICE_BETA_CYCLICAL_STAGE2, 0, 0, 0, 0, 2, 0, 5, 0, 0, -5, -1, -2, -1, "lithium price spike", "duration/margin missing", "cathode ASP+margin", "CATL/POSCO Future M/L&F."),
    Round312ShadowWeightRow(E2RArchetype.COPPER_TC_RC_SPREAD_4C_WATCH, 0, 0, 0, 0, 2, 1, 0, 5, 0, -5, -1, -2, -1, "copper TC/RC compression", "margin recovery missing", "N/A", "copper smelter spread."),
    Round312ShadowWeightRow(E2RArchetype.SODIUM_ION_MATERIAL_OPTIONALITY_STAGE2, 0, 0, 0, 0, 2, 0, 1, 0, 5, -2, -1, -3, -1, "sodium-ion material partnership", "commercialization missing", "customer contract+margin", "LG Chem/Sinopec."),
)


def round312_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND312_CASE_CANDIDATES]


def round312_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND312_CASE_CANDIDATES]


def round312_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND312_TRIGGER_RECORDS]


def round312_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND312_SHADOW_WEIGHT_ROWS]


def round312_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND312_REQUIRED_TARGET_ALIASES.items()]


def round312_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND312_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND312_SCORE_DOWN_AXES]
    )


def round312_summary() -> dict[str, object]:
    return {
        "source_round": ROUND312_SOURCE_ROUND_PATH,
        "round_id": ROUND312_ANALYST_ROUND_ID,
        "large_sector": ROUND312_LARGE_SECTOR,
        "method": ROUND312_METHOD,
        "case_candidate_count": len(ROUND312_CASE_CANDIDATES),
        "trigger_count": len(ROUND312_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND312_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 2,
        "stage2_event_candidate_count": 5,
        "stage3_yellow_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 5,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 0,
        "evidence_good_but_price_failed_or_muted_count": 3,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round312_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND312_SOURCE_ROUND_PATH,
        "round_id": ROUND312_ANALYST_ROUND_ID,
        "large_sector": ROUND312_LARGE_SECTOR,
        "method": ROUND312_METHOD,
        "summary": round312_summary(),
        "required_target_aliases": dict(ROUND312_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND312_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND312_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND312_STAGE3_GREEN_RULES,
        "green_blockers": ROUND312_GREEN_BLOCKERS,
        "score_up_axes": ROUND312_SCORE_UP_AXES,
        "score_down_axes": ROUND312_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND312_STAGE4B_WATCH_TRIGGERS,
        "stage4c_watch_gates": ROUND312_4C_WATCH_GATES,
        "row_separation_rules": ROUND312_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round312_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_commodity_price_strategic_resource_capex_or_restructuring_headline_as_green_without_spread_margin_offtake_or_FCF",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round312_summary_markdown() -> str:
    summary = round312_summary()
    lines = [
        "# R4 Loop 16 Materials / Spread / Strategic Resources Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: copper price can rise while smelter TC/RC collapses. In that case a copper headline is not company margin evidence.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Commodity price, policy, capex, restructuring and strategic-resource headlines must be separated from company spread, margin, offtake and FCF.",
            "- Stage3-Green confirmed: `0`.",
            "- Strong 4B/4C watch items: U.S. steel tariffs, petrochemical oversupply, Korea Zinc dilution/governance and copper TC/RC compression.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round312_trigger_grid_markdown() -> str:
    lines = [
        "# Round 312 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round312_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round312_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 312 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND312_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND312_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND312_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND312_GREEN_BLOCKERS),
            "",
            "## 4C Watch Gates",
            *_bullet_lines(ROUND312_4C_WATCH_GATES),
        ]
    ) + "\n"


def render_round312_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 312 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND312_STAGE4B_WATCH_TRIGGERS),
        "",
        "## 4C Watch Gates",
        *_bullet_lines(ROUND312_4C_WATCH_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND312_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round312_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 312 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND312_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round312_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 312 Row Separation Plan",
        "",
        "Case evidence, trigger anchors and full OHLC windows must be separate rows.",
        "",
        "Easy example: a lithium mine suspension can move POSCO Future M and L&F. It is still only cyclical Stage2 until cathode ASP, inventory reversal and material margin are confirmed.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND312_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round312_r4_loop16_reports(
    output_directory: str | Path = ROUND312_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND312_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND312_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND312_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND312_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round312_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND312_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round312_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round312_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round312_r4_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round312_r4_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round312_r4_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round312_r4_loop16_trigger_grid.md",
        "summary": output_dir / "round312_r4_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round312_r4_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round312_r4_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round312_r4_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round312_r4_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round312_r4_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round312_r4_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round312_case_rows())
    _write_csv(paths["target_aliases"], round312_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round312_trigger_rows())
    _write_csv(paths["score_adjustments"], round312_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round312_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round312_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round312_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round312_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round312_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round312_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round312_row_separation_plan_markdown(), encoding="utf-8")
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
    "ROUND312_4C_WATCH_GATES",
    "ROUND312_CASE_CANDIDATES",
    "ROUND312_GREEN_BLOCKERS",
    "ROUND312_LARGE_SECTOR",
    "ROUND312_REQUIRED_TARGET_ALIASES",
    "ROUND312_ROW_SEPARATION_RULES",
    "ROUND312_SCORE_DOWN_AXES",
    "ROUND312_SCORE_UP_AXES",
    "ROUND312_SHADOW_WEIGHT_ROWS",
    "ROUND312_STAGE2_ACTIONABLE_RULES",
    "ROUND312_STAGE3_GREEN_RULES",
    "ROUND312_STAGE3_YELLOW_RULES",
    "ROUND312_STAGE4B_WATCH_TRIGGERS",
    "ROUND312_TRIGGER_RECORDS",
    "render_round312_stage4b_4c_review_markdown",
    "render_round312_stage_rules_markdown",
    "render_round312_trigger_grid_markdown",
    "round312_audit_payload",
    "round312_case_records",
    "round312_case_rows",
    "round312_shadow_weight_rows",
    "round312_summary",
    "round312_trigger_rows",
    "write_round312_r4_loop16_reports",
]
