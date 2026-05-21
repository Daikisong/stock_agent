"""Round-325 R4 Loop-17 materials, spreads, and strategic resources pack.

This module converts ``docs/round/round_325.md`` into calibration-only case
records, trigger rows, shadow weights, and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: anti-dumping can lift a steel name to Stage2 when the tariff
rate and price reaction are clear. It is still not Green until the tariff
turns into actual margin and export-tariff risk is controlled.
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


ROUND325_SOURCE_ROUND_PATH = "docs/round/round_325.md"
ROUND325_ANALYST_ROUND_ID = "round_253"
ROUND325_LOOP_NAME = "R4 Loop 17"
ROUND325_LARGE_SECTOR = "MATERIALS_SPREADS_STRATEGIC_RESOURCES"
ROUND325_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND325_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round325_r4_loop17_materials_spreads_strategic"
ROUND325_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r4_loop17_round253.jsonl"
ROUND325_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r4_loop17_round253.jsonl"
ROUND325_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round325_r4_loop17_materials_spreads_strategic_audit.json"
ROUND325_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round253_r4_loop17_v1.csv"

ROUND325_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B": E2RArchetype.CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B.value,
    "SMELTER_TC_SPREAD_4B": E2RArchetype.SMELTER_TC_SPREAD_4B.value,
    "CRITICAL_MINERALS_US_PROCESSING_STAGE2_WITH_CAPEX_4B": E2RArchetype.CRITICAL_MINERALS_US_PROCESSING_STAGE2_WITH_CAPEX_4B.value,
    "STEEL_ANTIDUMPING_PROTECTION_STAGE2": E2RArchetype.STEEL_ANTIDUMPING_PROTECTION_STAGE2.value,
    "STEEL_TARIFF_AND_LOCALIZATION_HEDGE_STAGE2_4B": E2RArchetype.STEEL_TARIFF_AND_LOCALIZATION_HEDGE_STAGE2_4B.value,
    "PETROCHEMICAL_RESTRUCTURING_STAGE2_RELIEF": E2RArchetype.PETROCHEMICAL_RESTRUCTURING_STAGE2_RELIEF.value,
    "PETROCHEMICAL_OVERSUPPLY_4B": E2RArchetype.PETROCHEMICAL_OVERSUPPLY_4B.value,
    "REFINING_MARGIN_SPREAD_PRICE_FAILED": E2RArchetype.REFINING_MARGIN_SPREAD_PRICE_FAILED.value,
    "UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE": E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE.value,
    "RARE_EARTH_EXPORT_CONTROL_4B": E2RArchetype.RARE_EARTH_EXPORT_CONTROL_4B.value,
}

ROUND325_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_at_least_5pct",
    "market_relative_return_at_least_5pp",
    "tariff_anti_dumping_tender_contract_capex_or_policy_value_is_clear",
    "spread_treatment_charge_commodity_price_or_utilization_can_link_to_margin",
    "strategic_resource_control_links_to_customer_offtake_or_capacity",
    "dilution_export_tariff_regulatory_investigation_TC_compression_4B_is_identified",
    "reported_price_reaction_matches_the_trigger_direction",
)

ROUND325_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "sustained_spread_or_margin_recovery_visible",
    "capacity_shutdown_or_utilization_improvement_visible",
    "offtake_or_customer_contract_finality_visible",
    "funding_clarity_without_excessive_dilution",
    "export_tariff_risk_reduced",
    "stock_specific_price_validation_with_MFE_MAE_available",
)

ROUND325_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "spread_improvement_visible_in_earnings",
    "strategic_resource_capex_has_funding_offtake_construction_and_margin_clarity",
    "commodity_price_rebound_is_durable",
    "treatment_charge_or_raw_material_costs_are_stable",
    "dilution_regulatory_tariff_4B_is_reduced",
    "full_window_MFE_MAE_is_available_and_supportive",
)

ROUND325_GREEN_BLOCKERS: tuple[str, ...] = (
    "control_premium_without_operating_margin",
    "anti_dumping_without_margin_recovery",
    "critical_capex_without_funding_offtake_or_dilution_clarity",
    "petrochemical_restructuring_without_spread_recovery",
    "refining_OP_without_segment_quality",
    "upstream_lithium_without_POSCO_price_or_offtake_margin",
    "rare_earth_headline_without_company_specific_cost_or_order_impact",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND325_SCORE_UP_AXES: tuple[str, ...] = (
    "domestic_spread_protection",
    "control_premium_detection",
    "critical_minerals_strategic_value",
    "upstream_resource_control",
    "capacity_shutdown_discipline",
    "refining_spread_recovery",
    "rare_earth_export_control_risk",
    "treatment_charge_sensitivity",
)

ROUND325_SCORE_DOWN_AXES: tuple[str, ...] = (
    "control_premium_as_operating_growth",
    "critical_capex_without_funding_clarity",
    "anti_dumping_without_margin_recovery",
    "tariff_export_risk_ignored",
    "petrochemical_restructuring_without_spread",
    "refining_OP_without_segment_quality",
    "upstream_lithium_without_offtake_margin",
    "rare_earth_headline_without_company_impact",
)

ROUND325_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "control_premium_rallies_without_operating_improvement",
    "strategic_resource_capex_funded_by_large_share_issuance",
    "zinc_TC_compression",
    "US_steel_tariff_threat",
    "anti_dumping_protection_without_margin_recovery",
    "petrochemical_restructuring_without_demand_recovery",
    "refining_OP_recovery_mixed_with_battery_petrochemical_losses",
    "lithium_JV_without_offtake_economics",
    "rare_earth_export_controls_without_alternative_supply",
)

ROUND325_HARD_4C_GATES: tuple[str, ...] = (
    "permanent_loss_of_resource_access",
    "regulatory_block_or_criminal_investigation_materially_impairs_capital_plan",
    "structural_spread_collapse_without_capacity_closure",
    "large_dilution_spiral",
    "export_control_sanction_stops_downstream_shipments",
    "commodity_price_collapse_breaks_debt_or_capex_model",
)

ROUND325_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_reported_event_return_event_price_tender_tariff_TC_contract_capex_or_capacity_cut",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
    "do_not_treat_control_premium_anti_dumping_critical_capex_lithium_stake_or_restructuring_as_Green_without_margin_offtake_funding_and_risk_resolution",
)


@dataclass(frozen=True)
class Round325TriggerRecord:
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
class Round325CaseCandidate:
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
            "do_not_use_round325_cases_as_candidate_generation_input",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_control_premium_anti_dumping_critical_capex_lithium_stake_or_restructuring_as_Green_without_margin_offtake_funding_and_risk_resolution",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "dilution" in field
            or "tariff" in field
            or "TC" in field
            or "oversupply" in field
            or "rare_earth" in field
            or "normalization" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "thesis_break" in field
            or "export_control_sanction" in field
            or "permanent_loss" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND325_LARGE_SECTOR,
            large_sector=ROUND325_LARGE_SECTOR,
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
            must_have_fields=ROUND325_STAGE3_GREEN_RULES,
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


ROUND325_CASE_CANDIDATES: tuple[Round325CaseCandidate, ...] = (
    Round325CaseCandidate(
        "r4_loop17_korea_zinc_control_premium",
        "010130",
        "Korea Zinc",
        E2RArchetype.CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B,
        (E2RArchetype.KOREA_ZINC_CONTROL_PREMIUM_4B, E2RArchetype.STRATEGIC_METAL_CONTROL_PREMIUM_4B),
        "event_premium",
        "Stage2_control_premium_with_dilution_4B",
        "T0/T3",
        "Stage2_control_premium_with_dilution_4B",
        "Stage2 + 4B-watch",
        date(2024, 9, 13),
        date(2024, 9, 13),
        None,
        date(2024, 10, 1),
        None,
        False,
        ("MBK_Young_Poong_2T_won_tender", "initial_tender_price_660000_won", "Korea_Zinc_plus_19_8pct", "Young_Poong_plus_30pct", "raised_tender_price_830000_won", "court_clearance_close_877000_won"),
        ("control_premium_not_operating_margin", "share_issuance_dilution", "FSS_investigation", "debt_load_after_buyback", "full_OHLC_MFE_MAE_missing"),
        19.8,
        -8.0,
        {"trigger_date": "2024-09-13", "initial_tender_value_krw_trn": 2.0, "initial_tender_price_krw": 660000, "korea_zinc_initial_event_return_pct": 19.8, "young_poong_initial_event_return_pct": 30, "raised_tender_price_krw": 830000, "raised_tender_event_return_pct": 8.8, "court_clearance_event_return_pct": 6.4, "court_clearance_close_krw": 877000, "later_selloff_context_pct": -8},
        "aligned",
        "control_premium_stage2_with_4B",
        "event_premium",
        "stage2_watch_success",
        "Korea Zinc tender and buyback battle is strong Stage2 control premium, but dilution, debt and regulator risk block operating Green.",
    ),
    Round325CaseCandidate(
        "r4_loop17_korea_zinc_teck_tc_cut",
        "010130",
        "Korea Zinc",
        E2RArchetype.SMELTER_TC_SPREAD_4B,
        (E2RArchetype.COPPER_TC_RC_SPREAD_4C_WATCH, E2RArchetype.NONFERROUS_STRATEGIC_METALS),
        "4b_watch",
        "4B_zinc_treatment_charge_spread",
        "T0/T2",
        "4B_zinc_treatment_charge_spread",
        "4B-watch",
        date(2024, 4, 2),
        None,
        None,
        date(2024, 4, 2),
        None,
        False,
        ("Teck_Korea_Zinc_TC_165_usd_per_ton", "prior_TC_274_usd_per_ton", "TC_decline_40pct", "lowest_since_2021", "concentrate_scarcity"),
        ("treatment_charge_compression_4B", "smelter_margin_pressure", "zinc_price_recovery_missing", "TC_rebound_missing", "direct_price_anchor_missing"),
        None,
        None,
        {"trigger_date": "2024-04-02", "treatment_charge_2024_usd_per_ton": 165, "treatment_charge_prior_year_usd_per_ton": 274, "tc_decline_pct": 40, "tc_context": "lowest_since_2021", "direct_price_anchor": "price_data_unavailable_after_deep_search"},
        "aligned",
        "smelter_margin_4B",
        "no_rerating",
        "should_have_been_red",
        "Zinc TC compression is an operating spread 4B that must be separated from Korea Zinc control-premium price action.",
    ),
    Round325CaseCandidate(
        "r4_loop17_korea_zinc_us_critical_minerals",
        "010130",
        "Korea Zinc",
        E2RArchetype.CRITICAL_MINERALS_US_PROCESSING_STAGE2_WITH_CAPEX_4B,
        (E2RArchetype.CRITICAL_MINERALS_REFINERY_STAGE2_WITH_DILUTION_4B, E2RArchetype.CRITICAL_MINERALS_SMELTER_STAGE2_WITH_DILUTION_4B),
        "success_candidate",
        "Stage2_critical_minerals_processing_with_capex_4B",
        "T0/T2",
        "Stage2_critical_minerals_processing_with_capex_4B",
        "Stage2 + 4B-watch",
        date(2025, 12, 15),
        date(2025, 12, 15),
        None,
        date(2025, 12, 31),
        None,
        False,
        ("US_backed_Tennessee_critical_minerals_plant", "project_value_7_4B_usd", "reported_share_return_context_27pct", "share_issuance_2_833T_won", "antimony_gallium_target_products"),
        ("funding_finality_missing", "construction_timeline_missing", "offtake_contracts_missing", "capex_ROI_missing", "dilution_absorption_missing"),
        27.0,
        None,
        {"trigger_date": "2025-12-15", "project_value_usd_bn": 7.4, "reported_share_return_context_pct": 27, "share_issuance_krw_trn": 2.833, "share_issuance_usd_bn": 1.94, "target_materials": ["antimony", "gallium", "germanium", "zinc", "lead", "copper", "gold", "silver"]},
        "aligned",
        "strategic_resource_stage2_with_capex_4B",
        "policy_event_rerating",
        "stage2_watch_success",
        "Korea Zinc Tennessee critical-minerals plant is Stage2 strategic resource, but funding, dilution, construction and offtake gates remain open.",
    ),
    Round325CaseCandidate(
        "r4_loop17_hyundai_steel_posco_antidumping",
        "004020/005490",
        "Hyundai Steel / POSCO Holdings",
        E2RArchetype.STEEL_ANTIDUMPING_PROTECTION_STAGE2,
        (E2RArchetype.STEEL_ANTIDUMPING_SPREAD_STAGE2_ACTIONABLE, E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF),
        "success_candidate",
        "Stage2_Actionable_domestic_steel_spread_protection",
        "T0/T2",
        "Stage2-Actionable_domestic_steel_spread_protection",
        "Stage2-Actionable",
        date(2025, 2, 20),
        date(2025, 2, 20),
        None,
        date(2025, 2, 20),
        None,
        False,
        ("anti_dumping_rate_27_91_to_38_02pct", "Hyundai_Steel_plus_5_8pct", "POSCO_plus_3_9pct", "KOSPI_minus_0_7pct", "China_steel_import_10_4B_usd", "China_import_share_49pct"),
        ("domestic_spread_recovery_missing", "export_tariff_impact_missing", "raw_material_cost_missing", "full_OHLC_MFE_MAE_missing"),
        5.8,
        None,
        {"trigger_date": "2025-02-20", "anti_dumping_rate_pct": "27.91-38.02", "hyundai_steel_event_return_pct": 5.8, "posco_event_return_pct": 3.9, "kospi_same_context_pct": -0.7, "hyundai_market_relative_pp": 6.5, "posco_market_relative_pp": 4.6, "china_steel_import_value_2024_usd_bn": 10.4, "china_share_of_korea_steel_imports_pct": 49},
        "aligned",
        "good_stage2_domestic_steel_protection",
        "policy_event_rerating",
        "stage2_watch_success",
        "Hyundai Steel/POSCO anti-dumping is the cleanest R4 Stage2-Actionable trigger, but Green waits for actual spread and margin recovery.",
    ),
    Round325CaseCandidate(
        "r4_loop17_hyundai_posco_louisiana_steel_plant",
        "004020/005490/005380_readthrough",
        "Hyundai Steel / POSCO / Hyundai Motor Group",
        E2RArchetype.STEEL_TARIFF_AND_LOCALIZATION_HEDGE_STAGE2_4B,
        (E2RArchetype.STEEL_US_LOCALIZATION_CAPEX_4B, E2RArchetype.STEEL_TARIFF_EXPORT_RISK),
        "success_candidate",
        "Stage2_localization_hedge_with_tariff_4B",
        "T0/T3",
        "Stage2_localization_hedge_with_tariff_4B",
        "Stage2 + 4B-watch",
        date(2025, 2, 10),
        date(2025, 4, 21),
        None,
        date(2025, 2, 10),
        None,
        False,
        ("US_steel_tariff_risk", "POSCO_minus_3_6pct", "Hyundai_Steel_minus_2_9pct", "Louisiana_plant_5_8B_usd", "annual_capacity_2_7M_tons", "production_target_2029"),
        ("MOU_finality_missing", "construction_progress_missing", "US_demand_missing", "tariff_durability_missing", "capex_ROI_missing", "utilization_missing"),
        None,
        -5.1,
        {"tariff_background_date": "2025-02-10", "posco_tariff_event_return_pct": -3.6, "hyundai_steel_tariff_event_return_pct": -2.9, "later_50pct_tariff_context": {"hyundai_steel_max_drop_pct": -5.1, "posco_holdings_max_drop_pct": -3.2}, "louisiana_plant_investment_usd_bn": 5.8, "annual_capacity_mn_tons": 2.7, "production_start_target": 2029},
        "aligned",
        "tariff_4B_with_localization_stage2",
        "policy_event_rerating",
        "stage2_watch_success",
        "Louisiana steel plant is a localization hedge Stage2, but tariff durability, FID, ROI and utilization remain 4B gates.",
    ),
    Round325CaseCandidate(
        "r4_loop17_petrochemical_oversupply_restructuring",
        "011170/051910/HD_Hyundai_Oilbank_readthrough",
        "Lotte Chemical / LG Chem / HD Hyundai Chemical",
        E2RArchetype.PETROCHEMICAL_RESTRUCTURING_STAGE2_RELIEF,
        (E2RArchetype.PETROCHEMICAL_OVERSUPPLY_4B, E2RArchetype.PETROCHEMICAL_OVER_SUPPLY_FAILED_RERATING),
        "failed_rerating",
        "failed_rerating_with_stage2_restructuring_relief",
        "T0/T3",
        "failed_rerating_with_stage2_restructuring_relief",
        "failed_rerating + Stage2 relief",
        date(2025, 2, 7),
        date(2026, 2, 24),
        None,
        date(2025, 2, 7),
        None,
        False,
        ("Lotte_Chemical_2024_OP_loss_895B_won", "OP_loss_widening_157pct", "LG_Chem_OP_decline_63_75pct", "Daesan_NCC_shutdown_1_1M_tpy", "government_support_2T_won"),
        ("China_Middle_East_oversupply_4B", "naphtha_spread_recovery_missing", "demand_recovery_missing", "working_capital_relief_missing", "credit_spread_stabilization_missing"),
        None,
        None,
        {"lotte_chemical_2024_op_loss_krw_bn": 895, "lotte_chemical_op_loss_yoy_widening_pct": 157, "lg_chem_2024_op_decline_pct": 63.75, "lg_chem_petrochemical_q4_loss_krw_bn": 99, "restructuring_approval_date": "2026-02-24", "daesan_ncc_shutdown_capacity_mn_tons_per_year": 1.1, "shutdown_period_years": 3, "government_support_krw_trn": 2.0, "capital_increase_krw_trn": 1.2},
        "aligned",
        "petrochemical_failed_rerating_with_restructuring_relief",
        "no_rerating",
        "should_have_been_red",
        "Petrochemical losses are failed rerating; Daesan shutdown and support are Stage2 relief only until spread and utilization recover.",
    ),
    Round325CaseCandidate(
        "r4_loop17_sk_innovation_refining_margin_spread",
        "096770",
        "SK Innovation",
        E2RArchetype.REFINING_MARGIN_SPREAD_PRICE_FAILED,
        (E2RArchetype.REFINING_SPREAD_TURNAROUND_KOREA, E2RArchetype.REFINING_PETCHEM_MIX_DRAG),
        "cyclical_success",
        "mixed_refining_spread_recovery_with_4B",
        "T0/T4",
        "mixed_refining_spread_recovery_with_4B",
        "Stage2 recovery candidate + 4B-watch",
        date(2025, 2, 6),
        date(2026, 5, 13),
        None,
        date(2025, 2, 6),
        None,
        False,
        ("flat_refining_margin_guide", "SK_Innovation_minus_2_9pct_vs_KOSPI_plus_0_7pct", "Q1_2025_OP_loss_45B_won", "Q2_2025_OP_loss_418B_won", "Q1_2026_OP_2_2T_won"),
        ("prior_price_failure", "battery_loss_reduction_missing", "petrochemical_loss_reduction_missing", "logistics_normalization_missing", "inventory_effect_normalization_missing"),
        None,
        -2.9,
        {"flat_margin_trigger_date": "2025-02-06", "flat_margin_event_return_pct": -2.9, "kospi_same_context_pct": 0.7, "market_relative_pp": -3.6, "q1_2025_op_loss_krw_bn": 45, "q2_2025_op_loss_krw_bn": 418, "q1_2026_op_krw_trn": 2.2, "q1_2026_consensus_context_krw_trn": 1.4},
        "evidence_good_but_price_failed",
        "refining_spread_recovery_candidate_with_4B",
        "cyclical_rerating",
        "stage2_watch_success",
        "SK Innovation refining recovery is a Stage2 candidate, but prior price failure and battery/petrochemical drag keep 4B risk visible.",
    ),
    Round325CaseCandidate(
        "r4_loop17_posco_minres_lithium_jv",
        "005490",
        "POSCO Holdings / Mineral Resources",
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
        ("POSCO_MinRes_lithium_JV", "deal_value_765M_usd", "30pct_stake_in_MinRes_lithium_business", "15pct_Wodgina", "15pct_Mt_Marion", "MinRes_plus_10_8pct"),
        ("POSCO_direct_price_anchor_missing", "offtake_terms_missing", "spodumene_price_recovery_missing", "lithium_hydroxide_margin_missing", "downstream_POSCO_materials_link_missing"),
        10.8,
        None,
        {"trigger_date": "2025-11-11", "deal_value_usd_mn": 765, "stake_in_minres_lithium_business_pct": 30, "effective_stake_wodgina_pct": 15, "effective_stake_mt_marion_pct": 15, "minres_event_return_pct": 10.8, "posco_direct_price_anchor": "price_data_unavailable_after_deep_search"},
        "aligned",
        "strategic_upstream_stage2_not_green",
        "event_premium",
        "stage2_watch_success",
        "POSCO/MinRes lithium JV is upstream Stage2, but direct POSCO price, offtake and downstream margin are missing.",
    ),
    Round325CaseCandidate(
        "r4_loop17_china_rare_earth_export_control_korea",
        "transformer_battery_display_EV_aerospace_medical_basket",
        "Korea strategic-resource downstream basket",
        E2RArchetype.RARE_EARTH_EXPORT_CONTROL_4B,
        (E2RArchetype.RARE_EARTH_EXPORT_CONTROL_SUPPLY_CHAIN_4C, E2RArchetype.CHINA_STRATEGIC_MINERAL_EXPORT_CONTROL_4C),
        "4b_watch",
        "sector_4B_strategic_resource_control",
        "T0/T2",
        "sector_4B_strategic_resource_control",
        "4B-watch",
        date(2025, 4, 22),
        None,
        None,
        date(2025, 4, 22),
        None,
        False,
        ("China_rare_earth_export_control", "US_defense_end_use_restriction", "affected_transformers_batteries_displays_EVs_aerospace_medical", "heavy_rare_earth_restrictions_continue"),
        ("stock_specific_impact_missing", "non_China_supply_substitution_missing", "export_license_clarity_missing", "customer_order_impact_missing", "direct_price_anchor_missing"),
        None,
        None,
        {"trigger_date": "2025-04-22", "affected_product_categories": ["power_transformers", "batteries", "displays", "electric_vehicles", "aerospace", "medical_equipment"], "direct_stock_price_anchor": "price_data_unavailable_after_deep_search"},
        "aligned",
        "rare_earth_export_control_4B",
        "no_rerating",
        "should_have_been_red",
        "China rare-earth restrictions are a sector-wide 4B overlay until company-specific cost, license and order impact are known.",
    ),
)

ROUND325_TRIGGER_RECORDS: tuple[Round325TriggerRecord, ...] = (
    Round325TriggerRecord("r4l17_korea_zinc_tender_T0", "r4_loop17_korea_zinc_control_premium", "Stage2_control_premium", "2024-09-13", "MBK/Young Poong launches 2T won tender at 660,000 won; Korea Zinc +19.8%.", 19.8, "control_premium_stage2_not_operating_green", "Stage2", {"initial_tender_value_krw_trn": 2.0, "young_poong_event_return_pct": 30}),
    Round325TriggerRecord("r4l17_korea_zinc_buyback_T2", "r4_loop17_korea_zinc_control_premium", "Stage2_buyback_control_validation", "2024-10-21", "Court rejects attempt to block Korea Zinc buyback; shares +6.4% to 877,000 won.", 6.4, "control_premium_buyback_stage2", "Stage2", {"entry_price_krw": 877000}),
    Round325TriggerRecord("r4l17_korea_zinc_tc_T0", "r4_loop17_korea_zinc_teck_tc_cut", "4B_treatment_charge_spread", "2024-04-02", "Teck/Korea Zinc zinc TC falls to $165/t from $274/t.", "price_data_unavailable_after_deep_search", "smelter_margin_4B", "4B-watch", {"tc_decline_pct": 40}),
    Round325TriggerRecord("r4l17_korea_zinc_us_minerals_T0", "r4_loop17_korea_zinc_us_critical_minerals", "Stage2_critical_minerals_capex", "2025-12-15", "U.S.-backed Tennessee critical-minerals project reported at $7.4B.", "reported_context_+27", "strategic_resource_stage2_with_capex_4B", "Stage2+4B", {"project_value_usd_bn": 7.4, "share_issuance_krw_trn": 2.833}),
    Round325TriggerRecord("r4l17_steel_antidumping_T0", "r4_loop17_hyundai_steel_posco_antidumping", "Stage2-Actionable_steel_antidumping", "2025-02-20", "Korea recommends 27.91-38.02% duties on Chinese steel plate; Hyundai Steel +5.8%, POSCO +3.9%.", "Hyundai_Steel_+5.8_POSCO_+3.9", "good_stage2_domestic_steel_protection", "Stage2-Actionable", {"hyundai_market_relative_pp": 6.5, "posco_market_relative_pp": 4.6}),
    Round325TriggerRecord("r4l17_us_steel_tariff_T0", "r4_loop17_hyundai_posco_louisiana_steel_plant", "4B_export_tariff", "2025-02-10", "U.S. steel/aluminum tariff risk hits Korean steel shares.", "POSCO_-3.6_Hyundai_Steel_-2.9", "steel_export_tariff_4B", "4B-watch", {"posco_tariff_event_return_pct": -3.6, "hyundai_steel_tariff_event_return_pct": -2.9}),
    Round325TriggerRecord("r4l17_louisiana_steel_T1", "r4_loop17_hyundai_posco_louisiana_steel_plant", "Stage2_localization_hedge", "2025-04-21", "Hyundai Steel / Hyundai Motor Group $5.8B Louisiana steel plant, 2.7M t/y, 2029 target.", "price_data_unavailable_after_deep_search", "localization_hedge_stage2_not_green", "Stage2", {"investment_usd_bn": 5.8, "annual_capacity_mn_tons": 2.7}),
    Round325TriggerRecord("r4l17_petrochemical_loss_T0", "r4_loop17_petrochemical_oversupply_restructuring", "failed_rerating_petrochemical_oversupply", "2025-02-07", "Lotte Chemical 2024 OP loss 895B won and LG Chem OP -63.75%.", "price_data_unavailable_after_deep_search", "petrochemical_oversupply_failed_rerating", "4B-watch", {"lotte_chemical_2024_op_loss_krw_bn": 895, "lg_chem_2024_op_decline_pct": 63.75}),
    Round325TriggerRecord("r4l17_petrochemical_restructuring_T2", "r4_loop17_petrochemical_oversupply_restructuring", "Stage2_restructuring_relief", "2026-02-24", "Korea approves Daesan restructuring with 1.1M t/y NCC shutdown and up to 2T won support.", "price_data_unavailable_after_deep_search", "capacity_cut_relief_not_green", "Stage2_relief", {"daesan_ncc_shutdown_capacity_mn_tons_per_year": 1.1, "government_support_krw_trn": 2.0}),
    Round325TriggerRecord("r4l17_sk_innovation_refining_T0", "r4_loop17_sk_innovation_refining_margin_spread", "evidence_good_but_price_failed_refining_spread", "2025-02-06", "SK Innovation expects flat refining margins; shares -2.9% vs KOSPI +0.7%.", -2.9, "refining_margin_price_failed", "no_actionable", {"market_relative_pp": -3.6}),
    Round325TriggerRecord("r4l17_sk_innovation_recovery_T3", "r4_loop17_sk_innovation_refining_margin_spread", "Stage2_refining_recovery_candidate", "2026-05-13", "Q1 2026 OP recovered to 2.2T won vs 30B loss year earlier.", "price_data_unavailable_after_deep_search", "refining_OP_recovery_with_normalization_4B", "Stage2", {"q1_2026_op_krw_trn": 2.2, "q1_2026_consensus_context_krw_trn": 1.4}),
    Round325TriggerRecord("r4l17_posco_minres_lithium_T0", "r4_loop17_posco_minres_lithium_jv", "Stage2_upstream_lithium_supply", "2025-11-11", "POSCO buys MinRes lithium stake for $765M; MinRes +10.8%, POSCO direct price unavailable.", "MinRes_+10.8_POSCO_unavailable", "strategic_upstream_stage2_no_direct_price", "Stage2", {"deal_value_usd_mn": 765}),
    Round325TriggerRecord("r4l17_rare_earth_control_T0", "r4_loop17_china_rare_earth_export_control_korea", "sector_4B_rare_earth_export_control", "2025-04-22", "China asks Korean firms not to export products using Chinese rare earths to U.S. defense firms.", "price_data_unavailable_after_deep_search", "rare_earth_export_control_4B", "4B-watch", {"affected_product_count": 6}),
)

ROUND325_SHADOW_WEIGHT_ROWS: tuple[dict[str, str], ...] = (
    {"archetype": E2RArchetype.CONTROL_PREMIUM_STRATEGIC_METALS_STAGE2_WITH_DILUTION_4B.value, "domestic_spread_protection": "+1", "control_premium_detection": "+5", "critical_minerals_strategic_value": "+3", "upstream_resource_control": "+1", "capacity_shutdown_discipline": "+0", "refining_spread_recovery": "+0", "rare_earth_export_control_risk": "+1", "treatment_charge_sensitivity": "+2", "control_premium_as_operating_growth_penalty": "-5", "critical_capex_without_funding_clarity_penalty": "-3", "anti_dumping_without_margin_recovery_penalty": "-1", "tariff_export_risk_ignored_penalty": "-1", "stage2_actionable_promote": "control premium strong", "stage3_yellow_gate": "operating margin not confirmed", "stage3_green_gate": "governance+funding clarity", "notes": "Korea Zinc."},
    {"archetype": E2RArchetype.SMELTER_TC_SPREAD_4B.value, "domestic_spread_protection": "+0", "control_premium_detection": "+0", "critical_minerals_strategic_value": "+2", "upstream_resource_control": "+0", "capacity_shutdown_discipline": "+0", "refining_spread_recovery": "+0", "rare_earth_export_control_risk": "+1", "treatment_charge_sensitivity": "+5", "control_premium_as_operating_growth_penalty": "-1", "critical_capex_without_funding_clarity_penalty": "-1", "anti_dumping_without_margin_recovery_penalty": "-1", "tariff_export_risk_ignored_penalty": "-1", "stage2_actionable_promote": "TC cut pressures smelter margin", "stage3_yellow_gate": "relief missing", "stage3_green_gate": "TC stabilization+zinc spread", "notes": "Korea Zinc/Teck."},
    {"archetype": E2RArchetype.CRITICAL_MINERALS_US_PROCESSING_STAGE2_WITH_CAPEX_4B.value, "domestic_spread_protection": "+0", "control_premium_detection": "+2", "critical_minerals_strategic_value": "+5", "upstream_resource_control": "+3", "capacity_shutdown_discipline": "+0", "refining_spread_recovery": "+0", "rare_earth_export_control_risk": "+4", "treatment_charge_sensitivity": "+1", "control_premium_as_operating_growth_penalty": "-2", "critical_capex_without_funding_clarity_penalty": "-5", "anti_dumping_without_margin_recovery_penalty": "-1", "tariff_export_risk_ignored_penalty": "-1", "stage2_actionable_promote": "strategic minerals project", "stage3_yellow_gate": "capex/funding/dilution missing", "stage3_green_gate": "offtake+funding+construction", "notes": "Korea Zinc Tennessee."},
    {"archetype": E2RArchetype.STEEL_ANTIDUMPING_PROTECTION_STAGE2.value, "domestic_spread_protection": "+5", "control_premium_detection": "+0", "critical_minerals_strategic_value": "+0", "upstream_resource_control": "+0", "capacity_shutdown_discipline": "+1", "refining_spread_recovery": "+0", "rare_earth_export_control_risk": "+0", "treatment_charge_sensitivity": "+0", "control_premium_as_operating_growth_penalty": "-1", "critical_capex_without_funding_clarity_penalty": "-1", "anti_dumping_without_margin_recovery_penalty": "-4", "tariff_export_risk_ignored_penalty": "-4", "stage2_actionable_promote": "anti-dumping and price reaction aligned", "stage3_yellow_gate": "margin/export risk missing", "stage3_green_gate": "spread+margin recovery", "notes": "Hyundai Steel/POSCO."},
    {"archetype": E2RArchetype.STEEL_TARIFF_AND_LOCALIZATION_HEDGE_STAGE2_4B.value, "domestic_spread_protection": "+2", "control_premium_detection": "+0", "critical_minerals_strategic_value": "+1", "upstream_resource_control": "+0", "capacity_shutdown_discipline": "+0", "refining_spread_recovery": "+0", "rare_earth_export_control_risk": "+0", "treatment_charge_sensitivity": "+0", "control_premium_as_operating_growth_penalty": "-1", "critical_capex_without_funding_clarity_penalty": "-2", "anti_dumping_without_margin_recovery_penalty": "-2", "tariff_export_risk_ignored_penalty": "-5", "stage2_actionable_promote": "localization hedge vs tariff risk", "stage3_yellow_gate": "MOU/ROI missing", "stage3_green_gate": "FID+utilization+tariff clarity", "notes": "Hyundai/POSCO."},
    {"archetype": E2RArchetype.PETROCHEMICAL_RESTRUCTURING_STAGE2_RELIEF.value, "domestic_spread_protection": "+0", "control_premium_detection": "+0", "critical_minerals_strategic_value": "+0", "upstream_resource_control": "+0", "capacity_shutdown_discipline": "+5", "refining_spread_recovery": "+1", "rare_earth_export_control_risk": "+0", "treatment_charge_sensitivity": "+0", "control_premium_as_operating_growth_penalty": "-1", "critical_capex_without_funding_clarity_penalty": "-1", "anti_dumping_without_margin_recovery_penalty": "-1", "tariff_export_risk_ignored_penalty": "-2", "stage2_actionable_promote": "capacity cut relief", "stage3_yellow_gate": "spread recovery missing", "stage3_green_gate": "naphtha spread+utilization", "notes": "Lotte/LG Chem."},
    {"archetype": E2RArchetype.PETROCHEMICAL_OVERSUPPLY_4B.value, "domestic_spread_protection": "+0", "control_premium_detection": "+0", "critical_minerals_strategic_value": "+0", "upstream_resource_control": "+0", "capacity_shutdown_discipline": "+4", "refining_spread_recovery": "+0", "rare_earth_export_control_risk": "+0", "treatment_charge_sensitivity": "+0", "control_premium_as_operating_growth_penalty": "-1", "critical_capex_without_funding_clarity_penalty": "-1", "anti_dumping_without_margin_recovery_penalty": "-1", "tariff_export_risk_ignored_penalty": "-2", "stage2_actionable_promote": "global overcapacity loss", "stage3_yellow_gate": "structural downturn", "stage3_green_gate": "capacity closure+demand recovery", "notes": "Lotte/LG Chem."},
    {"archetype": E2RArchetype.REFINING_MARGIN_SPREAD_PRICE_FAILED.value, "domestic_spread_protection": "+0", "control_premium_detection": "+0", "critical_minerals_strategic_value": "+0", "upstream_resource_control": "+0", "capacity_shutdown_discipline": "+0", "refining_spread_recovery": "+5", "rare_earth_export_control_risk": "+0", "treatment_charge_sensitivity": "+0", "control_premium_as_operating_growth_penalty": "-1", "critical_capex_without_funding_clarity_penalty": "-1", "anti_dumping_without_margin_recovery_penalty": "-1", "tariff_export_risk_ignored_penalty": "-1", "stage2_actionable_promote": "refining OP recovery candidate", "stage3_yellow_gate": "segment quality missing", "stage3_green_gate": "sustained margin+loss reduction", "notes": "SK Innovation."},
    {"archetype": E2RArchetype.UPSTREAM_LITHIUM_SUPPLY_STAGE2_NO_PRICE.value, "domestic_spread_protection": "+0", "control_premium_detection": "+0", "critical_minerals_strategic_value": "+3", "upstream_resource_control": "+5", "capacity_shutdown_discipline": "+0", "refining_spread_recovery": "+0", "rare_earth_export_control_risk": "+1", "treatment_charge_sensitivity": "+0", "control_premium_as_operating_growth_penalty": "-1", "critical_capex_without_funding_clarity_penalty": "-4", "anti_dumping_without_margin_recovery_penalty": "-1", "tariff_export_risk_ignored_penalty": "-1", "stage2_actionable_promote": "upstream lithium stake", "stage3_yellow_gate": "POSCO price/offtake missing", "stage3_green_gate": "offtake+lithium margin", "notes": "POSCO/MinRes."},
    {"archetype": E2RArchetype.RARE_EARTH_EXPORT_CONTROL_4B.value, "domestic_spread_protection": "+0", "control_premium_detection": "+0", "critical_minerals_strategic_value": "+5", "upstream_resource_control": "+3", "capacity_shutdown_discipline": "+0", "refining_spread_recovery": "+0", "rare_earth_export_control_risk": "+5", "treatment_charge_sensitivity": "+0", "control_premium_as_operating_growth_penalty": "-1", "critical_capex_without_funding_clarity_penalty": "-1", "anti_dumping_without_margin_recovery_penalty": "-1", "tariff_export_risk_ignored_penalty": "-3", "stage2_actionable_promote": "China export-control risk", "stage3_yellow_gate": "stock-specific impact missing", "stage3_green_gate": "license clarity+non-China supply", "notes": "Korea downstream basket."},
)


def round325_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND325_CASE_CANDIDATES]


def round325_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND325_CASE_CANDIDATES]


def round325_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND325_TRIGGER_RECORDS]


def round325_shadow_weight_rows() -> list[dict[str, str]]:
    return [dict(row) for row in ROUND325_SHADOW_WEIGHT_ROWS]


def round325_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND325_REQUIRED_TARGET_ALIASES.items()]


def round325_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND325_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND325_SCORE_DOWN_AXES]
    )


def round325_summary() -> dict[str, object]:
    return {
        "source_round": ROUND325_SOURCE_ROUND_PATH,
        "round_id": ROUND325_ANALYST_ROUND_ID,
        "loop_name": ROUND325_LOOP_NAME,
        "large_sector": ROUND325_LARGE_SECTOR,
        "method": ROUND325_METHOD,
        "case_candidate_count": len(ROUND325_CASE_CANDIDATES),
        "trigger_count": len(ROUND325_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND325_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 1,
        "stage2_candidate_count": 6,
        "stage3_yellow_candidate_count": 5,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 8,
        "hard_4c_confirmed_count": 0,
        "strong_4c_watch_count": 5,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R5 Loop 17",
    }


def round325_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND325_SOURCE_ROUND_PATH,
        "round_id": ROUND325_ANALYST_ROUND_ID,
        "loop_name": ROUND325_LOOP_NAME,
        "large_sector": ROUND325_LARGE_SECTOR,
        "method": ROUND325_METHOD,
        "summary": round325_summary(),
        "required_target_aliases": dict(ROUND325_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND325_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND325_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND325_STAGE3_GREEN_RULES,
        "green_blockers": ROUND325_GREEN_BLOCKERS,
        "score_up_axes": ROUND325_SCORE_UP_AXES,
        "score_down_axes": ROUND325_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND325_STAGE4B_WATCH_TRIGGERS,
        "hard_4c_gates": ROUND325_HARD_4C_GATES,
        "row_separation_rules": ROUND325_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round325_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
            "do_not_treat_control_premium_anti_dumping_critical_capex_lithium_stake_or_restructuring_as_Green_without_margin_offtake_funding_and_risk_resolution",
        ),
    }


def render_round325_summary_markdown() -> str:
    summary = round325_summary()
    lines = [
        "# R4 Loop 17 Materials / Spreads / Strategic Resources Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: anti-dumping can be Stage2 when tariff and price reaction are clear, but it is not Green until actual margin recovery is visible.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Korea Zinc control premium is Stage2, not operating Green.",
            "- Korea Zinc TC cut is a smelter-margin 4B.",
            "- Korea Zinc U.S. critical-minerals plant is Stage2 with capex/dilution 4B.",
            "- Hyundai Steel/POSCO anti-dumping is the cleanest Stage2-Actionable trigger.",
            "- Hyundai/POSCO Louisiana steel plant is localization Stage2 with tariff 4B.",
            "- Petrochemical oversupply is failed rerating with restructuring relief only.",
            "- SK Innovation refining spread is a mixed recovery candidate.",
            "- POSCO/MinRes lithium JV is upstream Stage2 with no POSCO direct price validation.",
            "- China rare-earth export control is sector-wide 4B.",
            "- Stage3-Green confirmed: `0`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round325_trigger_grid_markdown() -> str:
    lines = [
        "# Round 325 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round325_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round325_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 325 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND325_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND325_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND325_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND325_GREEN_BLOCKERS),
            "",
            "## Hard 4C Gates",
            *_bullet_lines(ROUND325_HARD_4C_GATES),
        ]
    ) + "\n"


def render_round325_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 325 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND325_STAGE4B_WATCH_TRIGGERS),
        "",
        "## Hard 4C Gates",
        *_bullet_lines(ROUND325_HARD_4C_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND325_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round325_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 325 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event return, event price, tender price, tariff rate, treatment charge, contract value and capacity-cut data are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND325_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round325_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 325 Row Separation Plan",
        "",
        "Materials rows must separate case evidence, trigger anchors and full adjusted OHLC backfill.",
        "",
        "Easy example: Korea Zinc can have a Stage2 control-premium row and a separate TC-compression 4B row. Combining them would falsely turn a governance event into operating Green.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND325_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round325_r4_loop17_reports(
    output_directory: str | Path = ROUND325_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND325_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND325_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND325_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND325_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round325_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND325_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round325_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round325_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round325_r4_loop17_case_matrix.csv",
        "target_aliases": output_dir / "round325_r4_loop17_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round325_r4_loop17_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round325_r4_loop17_trigger_grid.md",
        "summary": output_dir / "round325_r4_loop17_trigger_validation_summary.md",
        "stage_rules": output_dir / "round325_r4_loop17_stage_rules.md",
        "stage4b_4c_review": output_dir / "round325_r4_loop17_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round325_r4_loop17_score_adjustments.csv",
        "shadow_weights": output_dir / "round325_r4_loop17_shadow_weights.csv",
        "price_validation_plan": output_dir / "round325_r4_loop17_price_validation_plan.md",
        "row_separation_plan": output_dir / "round325_r4_loop17_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round325_case_rows())
    _write_csv(paths["target_aliases"], round325_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round325_trigger_rows())
    _write_csv(paths["score_adjustments"], round325_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round325_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round325_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round325_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round325_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round325_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round325_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round325_row_separation_plan_markdown(), encoding="utf-8")
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
    "ROUND325_CASE_CANDIDATES",
    "ROUND325_GREEN_BLOCKERS",
    "ROUND325_HARD_4C_GATES",
    "ROUND325_LARGE_SECTOR",
    "ROUND325_REQUIRED_TARGET_ALIASES",
    "ROUND325_ROW_SEPARATION_RULES",
    "ROUND325_SCORE_DOWN_AXES",
    "ROUND325_SCORE_UP_AXES",
    "ROUND325_SHADOW_WEIGHT_ROWS",
    "ROUND325_STAGE2_ACTIONABLE_RULES",
    "ROUND325_STAGE3_GREEN_RULES",
    "ROUND325_STAGE3_YELLOW_RULES",
    "ROUND325_STAGE4B_WATCH_TRIGGERS",
    "ROUND325_TRIGGER_RECORDS",
    "render_round325_stage4b_4c_review_markdown",
    "render_round325_stage_rules_markdown",
    "render_round325_trigger_grid_markdown",
    "round325_audit_payload",
    "round325_case_records",
    "round325_case_rows",
    "round325_shadow_weight_rows",
    "round325_summary",
    "round325_trigger_rows",
    "write_round325_r4_loop17_reports",
]
