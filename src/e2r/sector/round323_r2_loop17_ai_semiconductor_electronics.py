"""Round-323 R2 Loop-17 AI semiconductor trigger validation pack.

This module converts ``docs/round/round_323.md`` into calibration-only case
records, trigger rows, shadow weights, and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: SK Hynix 12-layer HBM3E mass production can be Stage2-Actionable
when the event return is strong, but it is not Stage3-Green until customer
volume, yield, ASP, margin, capacity allocation and full OHLC validation exist.
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


ROUND323_SOURCE_ROUND_PATH = "docs/round/round_323.md"
ROUND323_ANALYST_ROUND_ID = "round_251"
ROUND323_LOOP_NAME = "R2 Loop 17"
ROUND323_LARGE_SECTOR = "AI_SEMICONDUCTOR_ELECTRONIC_COMPONENTS"
ROUND323_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND323_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round323_r2_loop17_ai_semiconductor_electronics"
ROUND323_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop17_round251.jsonl"
ROUND323_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r2_loop17_round251.jsonl"
ROUND323_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round323_r2_loop17_ai_semiconductor_electronics_audit.json"
ROUND323_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round251_r2_loop17_v1.csv"

ROUND323_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "HBM_FIRST_MOVER_STAGE2_ACTIONABLE": E2RArchetype.HBM_FIRST_MOVER_STAGE2_ACTIONABLE.value,
    "HBM4_CERTIFICATION_STAGE3_YELLOW_CANDIDATE": E2RArchetype.HBM4_CERTIFICATION_STAGE3_YELLOW_CANDIDATE.value,
    "OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE": E2RArchetype.OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE.value,
    "SAMSUNG_HBM_CATCHUP_STAGE2_WITH_LABOR_4B": E2RArchetype.SAMSUNG_HBM_CATCHUP_STAGE2_WITH_LABOR_4B.value,
    "HBM_PACKAGING_EQUIPMENT_STAGE2_ACTIONABLE": E2RArchetype.HBM_PACKAGING_EQUIPMENT_STAGE2_ACTIONABLE.value,
    "MEMORY_EARNINGS_GOOD_BUT_PRICE_FAILED": E2RArchetype.MEMORY_EARNINGS_GOOD_BUT_PRICE_FAILED.value,
    "CHINA_EXPORT_CONTROL_4B": E2RArchetype.CHINA_EXPORT_CONTROL_4B.value,
    "LABOR_SUPPLY_DISRUPTION_4B": E2RArchetype.LABOR_SUPPLY_DISRUPTION_4B.value,
}

ROUND323_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "reported_event_return_at_least_5pct_or_strong_market_relative_return",
    "HBM_memory_demand_or_packaging_equipment_trigger_is_company_specific",
    "mass_production_certification_LOI_order_or_equipment_supply_evidence_exists",
    "price_validation_uses_reported_event_anchor_only_until_adjusted_OHLC_backfill",
    "4B_overlay_is_recorded_when_LOI_labor_export_control_or_customer_concentration_is_unresolved",
)

ROUND323_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "customer_certification_or_supply_demand_is_specific",
    "EPS_OP_or_HBM_mix_path_likely_changes",
    "yield_ASP_margin_capacity_or_binding_order_gate_partly_open",
    "full_Green_fatal_blocker_absent",
)

ROUND323_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "binding_customer_order_or_confirmed_volume_exists",
    "HBM_yield_ASP_gross_margin_and_capacity_allocation_are_visible",
    "shipment_schedule_and_payment_terms_are_confirmed_where_relevant",
    "labor_and_export_control_risks_are_contained",
    "commodity_memory_price_and_PC_smartphone_demand_do_not_break_the_thesis",
    "full_window_MFE_MAE_is_available_and_supportive",
)

ROUND323_GREEN_BLOCKERS: tuple[str, ...] = (
    "mass_production_without_customer_order_volume",
    "HBM4_certification_without_top_customer_volume",
    "LOI_without_binding_order",
    "HBM_catchup_without_large_volume_or_yield",
    "equipment_order_without_repeat_order_or_customer_diversification",
    "record_profit_with_negative_event_return",
    "China_export_control_ignored",
    "labor_disruption_ignored",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND323_SCORE_UP_AXES: tuple[str, ...] = (
    "hbm_mass_production",
    "hbm4_certification",
    "customer_binding_demand",
    "hbm_wafer_allocation",
    "packaging_equipment_orders",
    "market_relative_return",
    "hbm_yield_margin",
)

ROUND323_SCORE_DOWN_AXES: tuple[str, ...] = (
    "china_fab_license_risk",
    "labor_supply_stability",
    "earnings_without_price_validation_penalty",
    "loi_without_final_order_penalty",
    "hbm_catchup_without_volume_penalty",
    "commodity_memory_ignored_penalty",
)

ROUND323_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "OpenAI_Stargate_LOI_before_binding_order",
    "Samsung_HBM_catchup_before_volume_yield_and_labor_resolution",
    "Hanmi_HBM_equipment_customer_concentration_before_repeat_orders",
    "record_profit_day_with_negative_stock_reaction",
    "China_fab_license_or_export_control_change",
    "Samsung_labor_strike_with_possible_DRAM_NAND_supply_impact",
)

ROUND323_HARD_4C_GATES: tuple[str, ...] = (
    "customer_allocation_loss_or_HBM_qualification_failure",
    "binding_order_failure_after_LOI",
    "HBM_yield_or_ASP_break",
    "commodity_memory_price_collapse",
    "export_control_blocks_fab_upgrade_or_output",
    "strike_causes_confirmed_shipment_delay",
)

ROUND323_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_reported_event_return_market_relative_return_customer_and_supply_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
    "do_not_treat_HBM_mass_production_certification_LOI_or_record_profit_as_Green_without_volume_yield_ASP_margin_capacity_and_risk_resolution",
)


@dataclass(frozen=True)
class Round323TriggerRecord:
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
class Round323CaseCandidate:
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
    strong_4c_confirmed: bool
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
            "do_not_use_round323_cases_as_candidate_generation_input",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_HBM_mass_production_certification_LOI_or_record_profit_as_Green_without_volume_yield_ASP_margin_capacity_and_risk_resolution",
        ]
        if not self.strong_4c_confirmed:
            guardrails.append("strong_4c_confirmed_false")
        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "LOI" in field
            or "labor" in field
            or "export_control" in field
            or "price_failed" in field
            or "customer_concentration" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "thesis_break" in field
            or "qualification_failure" in field
            or "binding_order_failure" in field
            or "confirmed_shipment_delay" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND323_LARGE_SECTOR,
            large_sector=ROUND323_LARGE_SECTOR,
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
            must_have_fields=ROUND323_STAGE3_GREEN_RULES,
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
            "strong_4c_confirmed": str(self.strong_4c_confirmed).lower(),
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


ROUND323_CASE_CANDIDATES: tuple[Round323CaseCandidate, ...] = (
    Round323CaseCandidate(
        "r2_loop17_sk_hynix_hbm3e_mass_production",
        "000660",
        "SK Hynix",
        E2RArchetype.HBM_FIRST_MOVER_STAGE2_ACTIONABLE,
        (E2RArchetype.HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE, E2RArchetype.MEMORY_HBM_CAPACITY),
        "success_candidate",
        "Stage2_Actionable_HBM_mass_production",
        "T1",
        "12-layer_HBM3E_mass_production",
        "Stage2-Actionable",
        date(2024, 9, 26),
        date(2024, 9, 26),
        None,
        date(2024, 9, 26),
        None,
        False,
        ("12_layer_HBM3E_mass_production", "event_return_gt_9pct", "KOSPI_plus_1_7pct", "capacity_uplift_vs_8_layer_50pct"),
        ("customer_order_volume_missing", "HBM_yield_missing", "HBM_ASP_missing", "gross_margin_missing", "capacity_allocation_missing", "full_OHLC_MFE_MAE_missing"),
        9.0,
        None,
        {"trigger_date": "2024-09-26", "event_return_pct": ">9", "kospi_same_context_pct": 1.7, "product": "12-layer_HBM3E", "capacity_uplift_vs_8_layer_pct": 50},
        "aligned",
        "excellent_stage2_actionable_HBM_mass_production",
        "event_premium",
        "stage2_watch_success",
        "12-layer HBM3E mass production has strong Stage2 validation, but customer volume, yield, ASP and margin are still Green gates.",
    ),
    Round323CaseCandidate(
        "r2_loop17_sk_hynix_hbm4_certification",
        "000660",
        "SK Hynix",
        E2RArchetype.HBM4_CERTIFICATION_STAGE3_YELLOW_CANDIDATE,
        (E2RArchetype.HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE, E2RArchetype.MEMORY_HBM_CAPACITY),
        "success_candidate",
        "Stage3_Yellow_candidate_HBM4_certification",
        "T1",
        "12-layer_HBM4_certification",
        "Stage3-Yellow candidate",
        date(2025, 9, 12),
        date(2025, 9, 12),
        date(2025, 9, 12),
        date(2025, 9, 12),
        None,
        False,
        ("12_layer_HBM4", "HBM4_certification", "customer_specific_base_die", "event_return_7_3pct", "expected_hbm_share_2026_low_60pct_range"),
        ("Nvidia_or_top_customer_confirmed_volume_missing", "HBM4_yield_missing", "HBM4_ASP_missing", "gross_margin_missing", "capacity_ramp_missing", "full_OHLC_MFE_MAE_missing"),
        7.3,
        None,
        {"trigger_date": "2025-09-12", "event_return_pct": 7.3, "kospi_same_context_pct": 1.2, "product": "12-layer_HBM4", "expected_hbm_share_2026_context": "low_60pct_range", "customer_specific_base_die": True},
        "aligned",
        "Stage3_Yellow_candidate_HBM4_first_mover",
        "event_premium",
        "yellow_success",
        "HBM4 certification is Yellow-candidate evidence, not Green without Nvidia/top-customer volume, yield, ASP and capacity ramp.",
    ),
    Round323CaseCandidate(
        "r2_loop17_openai_stargate_memory_loi",
        "000660/005930",
        "SK Hynix / Samsung Electronics",
        E2RArchetype.OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE,
        (E2RArchetype.OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE, E2RArchetype.AI_INFRA_MEMORY_SUPPLY_MOU_4B),
        "success_candidate",
        "Stage2_Actionable_memory_demand_with_4B",
        "T1/T2",
        "OpenAI_Stargate_memory_LOI",
        "Stage2-Actionable + 4B-watch",
        date(2025, 10, 2),
        date(2025, 10, 2),
        None,
        date(2025, 10, 2),
        None,
        False,
        ("OpenAI_Stargate_LOI", "project_value_context_500B_usd", "SK_Hynix_close_plus_10pct", "Samsung_close_plus_3_5pct", "900000_DRAM_wafers_per_month", "demand_gt_2x_current_HBM_capacity"),
        ("LOI_not_binding_final_order", "capacity_allocation_missing", "yield_missing", "pricing_missing", "delivery_schedule_missing", "full_OHLC_MFE_MAE_missing"),
        10.0,
        None,
        {"trigger_date": "2025-10-02", "project_value_context_usd_bn": 500, "sk_hynix_intraday_return_pct": 12, "sk_hynix_close_return_pct": 10, "samsung_intraday_return_pct": 5, "samsung_close_return_pct": 3.5, "openai_dram_wafer_demand_per_month": 900000, "demand_vs_current_hbm_capacity": ">2x"},
        "aligned",
        "excellent_stage2_actionable_demand_shock_with_4B",
        "event_premium",
        "stage2_watch_success",
        "OpenAI Stargate is a powerful demand shock, but LOI/final-order separation must cap Green until binding terms and delivery economics exist.",
    ),
    Round323CaseCandidate(
        "r2_loop17_samsung_hbm_catchup_nvidia_amd",
        "005930",
        "Samsung Electronics",
        E2RArchetype.SAMSUNG_HBM_CATCHUP_STAGE2_WITH_LABOR_4B,
        (E2RArchetype.HBM_CATCHUP_LATE_STAGE2, E2RArchetype.SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C),
        "success_candidate",
        "Stage2_HBM_catchup_with_labor_4B",
        "T0/T2",
        "Nvidia_AMD_HBM4_catchup",
        "Stage2 + 4B-watch",
        date(2026, 1, 26),
        date(2026, 1, 26),
        None,
        date(2026, 3, 18),
        None,
        False,
        ("Nvidia_HBM4_catchup", "AMD_MI455X_HBM4_and_EPYC_DDR5_MOU", "Samsung_event_return_2_2pct", "SK_Hynix_same_context_minus_2_9pct", "Samsung_HBM_share_context_22pct"),
        ("large_volume_Nvidia_shipments_missing", "AMD_order_volume_missing", "HBM4_yield_missing", "gross_margin_missing", "labor_cost_resolution_missing", "full_OHLC_MFE_MAE_missing"),
        2.2,
        -2.9,
        {"nvidia_trigger_date": "2026-01-26", "amd_mou_date": "2026-03-18", "samsung_event_return_pct": 2.2, "sk_hynix_same_context_return_pct": -2.9, "amd_product_context": "Instinct_MI455X_HBM4_and_EPYC_DDR5", "samsung_hbm_share_context_pct": 22, "sk_hynix_hbm_share_context_pct": 57},
        "aligned",
        "Stage2_HBM_catchup_not_Green",
        "event_premium",
        "stage2_watch_success",
        "Samsung HBM catch-up is Stage2 evidence, but it is not first-mover Green before large volume, yield, margin and labor risk are resolved.",
    ),
    Round323CaseCandidate(
        "r2_loop17_hanmi_semiconductor_hbm_packaging",
        "042700",
        "Hanmi Semiconductor",
        E2RArchetype.HBM_PACKAGING_EQUIPMENT_STAGE2_ACTIONABLE,
        (E2RArchetype.ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B, E2RArchetype.HBM_EQUIPMENT_STAGE2_ACTIONABLE),
        "success_candidate",
        "Stage2_Actionable_HBM_packaging_equipment",
        "T0/T2",
        "TSV_TC_bonder_HBM_packaging_order",
        "Stage2-Actionable + 4B-watch",
        date(2024, 3, 26),
        date(2024, 3, 26),
        None,
        date(2024, 3, 26),
        None,
        False,
        ("TSV_TC_bonder_for_HBM_packaging", "Hanmi_event_return_16pct", "SK_Hynix_supply_deal_21_48B_krw", "recent_contract_wins_200B_krw", "China_export_control_selloff_minus_4_4pct"),
        ("repeat_order_visibility_missing", "customer_diversification_missing", "gross_margin_missing", "capacity_missing", "export_control_impact_missing", "full_OHLC_MFE_MAE_missing"),
        16.0,
        -4.4,
        {"trigger_date": "2024-03-26", "hanmi_event_return_pct": 16, "sk_hynix_same_context_return_pct": 4.3, "kospi_same_context_pct": 0.7, "sk_hynix_supply_deal_krw_bn": 21.48, "recent_contract_wins_context_krw_bn": 200, "equipment": "TSV_TC_bonder_for_HBM_packaging", "china_export_control_selloff_pct": -4.4},
        "aligned",
        "excellent_stage2_actionable_HBM_equipment_with_4B",
        "event_premium",
        "stage2_watch_success",
        "Hanmi is a clean HBM packaging Stage2 anchor, but repeat order, customer diversification, margin and export-control impact gate Green.",
    ),
    Round323CaseCandidate(
        "r2_loop17_sk_hynix_record_profit_price_failed",
        "000660",
        "SK Hynix",
        E2RArchetype.MEMORY_EARNINGS_GOOD_BUT_PRICE_FAILED,
        (E2RArchetype.MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW, E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED),
        "failed_rerating",
        "record_profit_price_failed",
        "T0",
        "record_profit_but_negative_event_return",
        "no_actionable",
        date(2025, 1, 23),
        None,
        None,
        date(2025, 1, 23),
        None,
        False,
        ("operating_profit_q4_2024_8_1T_krw", "HBM_share_of_DRAM_revenue_40pct", "HBM_sales_outlook_double_this_year", "event_return_minus_4pct"),
        ("price_failed_record_profit", "commodity_memory_price_decline", "smartphone_PC_demand_weakness", "Chinese_competition", "post_rally_profit_taking", "full_OHLC_MFE_MAE_missing"),
        None,
        -4.0,
        {"trigger_date": "2025-01-23", "operating_profit_q4_2024_krw_trn": 8.1, "operating_profit_q4_2024_usd_bn": 5.64, "hbm_share_of_dram_revenue_pct": 40, "hbm_sales_outlook": "double_this_year", "event_return_pct": -4},
        "evidence_good_but_price_failed",
        "record_profit_price_failed_not_actionable",
        "no_rerating",
        "false_yellow",
        "Record profit was strong evidence, but the negative event return and commodity memory risks mean it must not be promoted as actionable.",
    ),
    Round323CaseCandidate(
        "r2_loop17_us_export_control_china_fabs",
        "005930/000660/067310/042700",
        "Samsung / SK Hynix / Hana Micron / Hanmi Semiconductor",
        E2RArchetype.CHINA_EXPORT_CONTROL_4B,
        (E2RArchetype.SEMICONDUCTOR_EXPORT_CONTROL_4C_WATCH, E2RArchetype.CHIP_EXPORT_CONTROL_4C_WATCH),
        "4b_watch",
        "China_export_control_4B",
        "T0/T2",
        "US_export_control_China_fabs",
        "4B-watch",
        date(2025, 9, 1),
        None,
        None,
        date(2025, 9, 1),
        None,
        False,
        ("US_export_control_China_fab_license_change", "Samsung_minus_2_3pct", "SK_Hynix_minus_4_4pct", "Hanmi_minus_4_4pct", "Hana_Micron_minus_1_7pct", "effective_delay_120_days"),
        ("annual_license_stability_missing", "upgrade_permission_missing", "China_fab_maintenance_missing", "capex_shift_to_Korea_missing", "supply_disruption_quantification_missing"),
        None,
        -4.4,
        {"trigger_date": "2025-09-01", "samsung_event_return_pct": -2.3, "sk_hynix_event_return_pct": -4.4, "kospi_same_context_pct": -0.7, "hana_micron_event_return_pct": -1.7, "hanmi_semiconductor_event_return_pct": -4.4, "samsung_china_dram_output_exposure": ">1/3", "sk_hynix_china_dram_nand_output_exposure_pct": "30-40", "effective_delay_days": 120},
        "aligned",
        "export_control_4B_success",
        "unknown",
        "stage2_watch_success",
        "China fab export-control changes are a 4B overlay for AI memory, not a positive Green source.",
    ),
    Round323CaseCandidate(
        "r2_loop17_samsung_labor_memory_supply_4b",
        "005930",
        "Samsung Electronics",
        E2RArchetype.LABOR_SUPPLY_DISRUPTION_4B,
        (E2RArchetype.SEMICONDUCTOR_LABOR_SUPPLY_CHAIN_4C, E2RArchetype.SAMSUNG_HBM_CATCHUP_STAGE2_WITH_LABOR_4B),
        "4b_watch",
        "labor_supply_4B_not_hard_4C",
        "T0/T2",
        "Samsung_labor_memory_supply_disruption",
        "4B-watch",
        date(2026, 5, 15),
        None,
        None,
        date(2026, 5, 15),
        None,
        False,
        ("planned_strike_18_days", "nearly_48000_workers", "possible_DRAM_supply_impact_4pct", "possible_NAND_supply_impact_3pct", "court_injunction_essential_workers"),
        ("strike_not_settled", "bonus_demand_unresolved", "DRAM_NAND_supply_impact_possible", "labor_cost_resolution_missing", "hard_4c_false", "full_OHLC_MFE_MAE_missing"),
        None,
        -9.3,
        {"trigger_date": "2026-05-15", "event_return_pct": -9.3, "planned_strike_days": 18, "workers_context": "nearly_48000", "bonus_demand": "remove_bonus_cap_and_15pct_operating_profit_pool", "possible_dram_supply_impact_pct": 4, "possible_nand_supply_impact_pct": 3, "court_injunction_essential_workers": True, "hard_4c": False},
        "aligned",
        "labor_supply_4B_not_hard_4C",
        "unknown",
        "stage2_watch_success",
        "Samsung labor disruption is 4B until confirmed shipment delay or hard production break; court injunction is not a full settlement.",
    ),
)

ROUND323_TRIGGER_RECORDS: tuple[Round323TriggerRecord, ...] = (
    Round323TriggerRecord("r2l17_skh_hbm3e_T1", "r2_loop17_sk_hynix_hbm3e_mass_production", "Stage2-Actionable_HBM3E_mass_production", "2024-09-26", "12-layer HBM3E mass production; SK Hynix >9% vs KOSPI +1.7%.", ">9", "excellent_stage2_actionable_HBM_mass_production", "Stage2-Actionable", {"market_relative_pp": ">7", "capacity_uplift_vs_8_layer_pct": 50}),
    Round323TriggerRecord("r2l17_skh_hbm4_T1", "r2_loop17_sk_hynix_hbm4_certification", "Stage3-Yellow_candidate_HBM4_certification", "2025-09-12", "12-layer HBM4 certification and customer-specific base die; SK Hynix +7.3%.", 7.3, "Stage3_Yellow_candidate_HBM4_first_mover", "Stage3-Yellow_candidate", {"market_relative_pp": 6.1, "customer_specific_base_die": True}),
    Round323TriggerRecord("r2l17_openai_stargate_T1", "r2_loop17_openai_stargate_memory_loi", "Stage2-Actionable_memory_demand_with_4B", "2025-10-02", "OpenAI Stargate memory LOI; SK Hynix closes +10%, Samsung +3.5%.", "SK_Hynix_close_+10_Samsung_close_+3.5", "excellent_stage2_actionable_demand_shock_with_4B", "Stage2-Actionable+4B", {"openai_dram_wafer_demand_per_month": 900000, "demand_vs_current_hbm_capacity": ">2x"}),
    Round323TriggerRecord("r2l17_samsung_hbm4_nvidia_T0", "r2_loop17_samsung_hbm_catchup_nvidia_amd", "Stage2_HBM_catchup", "2026-01-26", "Samsung HBM4 catch-up headline; Samsung +2.2%, SK Hynix -2.9%.", 2.2, "Stage2_HBM_catchup_not_Green", "Stage2", {"sk_hynix_same_context_return_pct": -2.9, "samsung_hbm_share_context_pct": 22}),
    Round323TriggerRecord("r2l17_hanmi_hbm_equipment_T0", "r2_loop17_hanmi_semiconductor_hbm_packaging", "Stage2-Actionable_HBM_packaging", "2024-03-26", "Hanmi TSV-TC bonder HBM packaging order context; Hanmi +16% vs KOSPI +0.7%.", 16, "excellent_stage2_actionable_HBM_equipment_with_4B", "Stage2-Actionable", {"market_relative_pp": 15.3, "sk_hynix_supply_deal_krw_bn": 21.48}),
    Round323TriggerRecord("r2l17_skh_record_profit_T0", "r2_loop17_sk_hynix_record_profit_price_failed", "evidence_good_but_price_failed", "2025-01-23", "Record Q4 operating profit and HBM mix, but stock falls 4%.", -4, "record_profit_price_failed_not_actionable", "no_actionable", {"operating_profit_q4_2024_krw_trn": 8.1, "hbm_share_of_dram_revenue_pct": 40}),
    Round323TriggerRecord("r2l17_us_export_control_T0", "r2_loop17_us_export_control_china_fabs", "4B_export_control", "2025-09-01", "U.S. export-control / China fab license risk; memory and equipment names fall.", "Samsung_-2.3_SKH_-4.4_Hanmi_-4.4_Hana_-1.7", "export_control_4B_success", "4B-watch", {"effective_delay_days": 120}),
    Round323TriggerRecord("r2l17_samsung_labor_T0", "r2_loop17_samsung_labor_memory_supply_4b", "4B_labor_supply_disruption", "2026-05-15", "Samsung labor strike risk; Samsung -9.3%, possible DRAM/NAND supply impact.", -9.3, "labor_supply_4B_not_hard_4C", "4B-watch", {"planned_strike_days": 18, "possible_dram_supply_impact_pct": 4, "possible_nand_supply_impact_pct": 3}),
)

ROUND323_SHADOW_WEIGHT_ROWS: tuple[dict[str, str], ...] = (
    {"archetype": E2RArchetype.HBM_FIRST_MOVER_STAGE2_ACTIONABLE.value, "hbm_mass_production": "+5", "hbm4_certification": "+2", "customer_binding_demand": "+4", "hbm_wafer_allocation": "+4", "packaging_equipment_orders": "+1", "market_relative_return": "+5", "hbm_yield_margin": "+5", "china_fab_license_risk": "+2", "labor_supply_stability": "+1", "earnings_without_price_validation_penalty": "-2", "loi_without_final_order_penalty": "-1", "hbm_catchup_without_volume_penalty": "-1", "commodity_memory_ignored_penalty": "-3", "stage2_actionable_promote": "12-layer HBM3E mass production", "stage3_yellow_gate": "customer economics incomplete", "stage3_green_gate": "customer volume+yield+ASP+margin", "notes": "SK Hynix HBM3E."},
    {"archetype": E2RArchetype.HBM4_CERTIFICATION_STAGE3_YELLOW_CANDIDATE.value, "hbm_mass_production": "+4", "hbm4_certification": "+5", "customer_binding_demand": "+4", "hbm_wafer_allocation": "+4", "packaging_equipment_orders": "+1", "market_relative_return": "+5", "hbm_yield_margin": "+5", "china_fab_license_risk": "+2", "labor_supply_stability": "+1", "earnings_without_price_validation_penalty": "-2", "loi_without_final_order_penalty": "-1", "hbm_catchup_without_volume_penalty": "-1", "commodity_memory_ignored_penalty": "-3", "stage2_actionable_promote": "HBM4 certification", "stage3_yellow_gate": "certification plus price validation", "stage3_green_gate": "top-customer volume+yield+ASP", "notes": "SK Hynix HBM4."},
    {"archetype": E2RArchetype.OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE.value, "hbm_mass_production": "+4", "hbm4_certification": "+3", "customer_binding_demand": "+5", "hbm_wafer_allocation": "+5", "packaging_equipment_orders": "+1", "market_relative_return": "+4", "hbm_yield_margin": "+4", "china_fab_license_risk": "+1", "labor_supply_stability": "+1", "earnings_without_price_validation_penalty": "-1", "loi_without_final_order_penalty": "-4", "hbm_catchup_without_volume_penalty": "-1", "commodity_memory_ignored_penalty": "-2", "stage2_actionable_promote": "OpenAI demand shock", "stage3_yellow_gate": "LOI not binding", "stage3_green_gate": "binding order+delivery economics", "notes": "OpenAI Stargate."},
    {"archetype": E2RArchetype.SAMSUNG_HBM_CATCHUP_STAGE2_WITH_LABOR_4B.value, "hbm_mass_production": "+3", "hbm4_certification": "+4", "customer_binding_demand": "+4", "hbm_wafer_allocation": "+3", "packaging_equipment_orders": "+0", "market_relative_return": "+2", "hbm_yield_margin": "+5", "china_fab_license_risk": "+2", "labor_supply_stability": "+5", "earnings_without_price_validation_penalty": "-1", "loi_without_final_order_penalty": "-1", "hbm_catchup_without_volume_penalty": "-5", "commodity_memory_ignored_penalty": "-3", "stage2_actionable_promote": "Samsung catch-up", "stage3_yellow_gate": "volume/yield incomplete", "stage3_green_gate": "large volume+yield+labor resolution", "notes": "Samsung HBM catch-up."},
    {"archetype": E2RArchetype.HBM_PACKAGING_EQUIPMENT_STAGE2_ACTIONABLE.value, "hbm_mass_production": "+3", "hbm4_certification": "+2", "customer_binding_demand": "+3", "hbm_wafer_allocation": "+3", "packaging_equipment_orders": "+5", "market_relative_return": "+5", "hbm_yield_margin": "+4", "china_fab_license_risk": "+3", "labor_supply_stability": "+1", "earnings_without_price_validation_penalty": "-1", "loi_without_final_order_penalty": "-1", "hbm_catchup_without_volume_penalty": "-2", "commodity_memory_ignored_penalty": "-2", "stage2_actionable_promote": "TSV-TC bonder order", "stage3_yellow_gate": "repeat order/customer mix", "stage3_green_gate": "repeat order+margin+diversification", "notes": "Hanmi Semiconductor."},
    {"archetype": E2RArchetype.MEMORY_EARNINGS_GOOD_BUT_PRICE_FAILED.value, "hbm_mass_production": "+3", "hbm4_certification": "+2", "customer_binding_demand": "+3", "hbm_wafer_allocation": "+2", "packaging_equipment_orders": "+0", "market_relative_return": "-5", "hbm_yield_margin": "+4", "china_fab_license_risk": "+3", "labor_supply_stability": "+1", "earnings_without_price_validation_penalty": "-5", "loi_without_final_order_penalty": "-1", "hbm_catchup_without_volume_penalty": "-1", "commodity_memory_ignored_penalty": "-5", "stage2_actionable_promote": "blocked", "stage3_yellow_gate": "price failed", "stage3_green_gate": "not allowed until price/revision recovery", "notes": "SK Hynix record profit day."},
    {"archetype": E2RArchetype.CHINA_EXPORT_CONTROL_4B.value, "hbm_mass_production": "+0", "hbm4_certification": "+0", "customer_binding_demand": "+0", "hbm_wafer_allocation": "+0", "packaging_equipment_orders": "+1", "market_relative_return": "-5", "hbm_yield_margin": "+1", "china_fab_license_risk": "+5", "labor_supply_stability": "+1", "earnings_without_price_validation_penalty": "-1", "loi_without_final_order_penalty": "-1", "hbm_catchup_without_volume_penalty": "-1", "commodity_memory_ignored_penalty": "-2", "stage2_actionable_promote": "none", "stage3_yellow_gate": "4B overlay", "stage3_green_gate": "license stability required", "notes": "China fab export control."},
    {"archetype": E2RArchetype.LABOR_SUPPLY_DISRUPTION_4B.value, "hbm_mass_production": "+0", "hbm4_certification": "+0", "customer_binding_demand": "+0", "hbm_wafer_allocation": "+0", "packaging_equipment_orders": "+0", "market_relative_return": "-4", "hbm_yield_margin": "+2", "china_fab_license_risk": "+0", "labor_supply_stability": "+5", "earnings_without_price_validation_penalty": "-1", "loi_without_final_order_penalty": "-1", "hbm_catchup_without_volume_penalty": "-2", "commodity_memory_ignored_penalty": "-1", "stage2_actionable_promote": "none", "stage3_yellow_gate": "4B overlay", "stage3_green_gate": "labor settlement required", "notes": "Samsung labor supply."},
)


def round323_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND323_CASE_CANDIDATES]


def round323_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND323_CASE_CANDIDATES]


def round323_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND323_TRIGGER_RECORDS]


def round323_shadow_weight_rows() -> list[dict[str, str]]:
    return [dict(row) for row in ROUND323_SHADOW_WEIGHT_ROWS]


def round323_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND323_REQUIRED_TARGET_ALIASES.items()]


def round323_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND323_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND323_SCORE_DOWN_AXES]
    )


def round323_summary() -> dict[str, object]:
    return {
        "source_round": ROUND323_SOURCE_ROUND_PATH,
        "round_id": ROUND323_ANALYST_ROUND_ID,
        "loop_name": ROUND323_LOOP_NAME,
        "large_sector": ROUND323_LARGE_SECTOR,
        "method": ROUND323_METHOD,
        "case_candidate_count": len(ROUND323_CASE_CANDIDATES),
        "trigger_count": len(ROUND323_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND323_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 3,
        "stage2_candidate_count": 5,
        "stage3_yellow_candidate_count": 4,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 6,
        "stage4c_watch_count": 0,
        "strong_4c_case_count": 0,
        "evidence_good_but_price_failed_count": 1,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R3 Loop 17",
    }


def round323_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND323_SOURCE_ROUND_PATH,
        "round_id": ROUND323_ANALYST_ROUND_ID,
        "loop_name": ROUND323_LOOP_NAME,
        "large_sector": ROUND323_LARGE_SECTOR,
        "method": ROUND323_METHOD,
        "summary": round323_summary(),
        "required_target_aliases": dict(ROUND323_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND323_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND323_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND323_STAGE3_GREEN_RULES,
        "green_blockers": ROUND323_GREEN_BLOCKERS,
        "score_up_axes": ROUND323_SCORE_UP_AXES,
        "score_down_axes": ROUND323_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND323_STAGE4B_WATCH_TRIGGERS,
        "hard_4c_gates": ROUND323_HARD_4C_GATES,
        "row_separation_rules": ROUND323_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round323_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
            "do_not_treat_HBM_mass_production_certification_LOI_or_record_profit_as_Green_without_volume_yield_ASP_margin_capacity_and_risk_resolution",
        ),
    }


def render_round323_summary_markdown() -> str:
    summary = round323_summary()
    lines = [
        "# R2 Loop 17 AI Semiconductor / Electronic Components Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: OpenAI Stargate demand can be Stage2-Actionable, but a LOI is not a binding order, so Green remains blocked until volume, price and delivery economics are confirmed.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- SK Hynix HBM3E mass production is Stage2-Actionable, not Green before customer volume/yield/ASP/margin.",
            "- SK Hynix HBM4 certification is a Stage3-Yellow candidate, not Green before top-customer volume and capacity ramp.",
            "- OpenAI Stargate memory LOI is a demand shock with 4B overlay because the order is not binding.",
            "- Samsung HBM catch-up is Stage2 with labor and volume/yield gates.",
            "- Hanmi Semiconductor is HBM packaging Stage2-Actionable with customer concentration and export-control gates.",
            "- SK Hynix record profit with negative event return is evidence-good but price-failed.",
            "- China export control and Samsung labor disruption are 4B overlays, not positive Green evidence.",
            "- Stage3-Green confirmed: `0`.",
            "- Strong 4C case count: `0`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round323_trigger_grid_markdown() -> str:
    lines = [
        "# Round 323 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round323_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round323_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 323 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND323_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND323_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND323_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND323_GREEN_BLOCKERS),
            "",
            "## Hard 4C Gates",
            *_bullet_lines(ROUND323_HARD_4C_GATES),
        ]
    ) + "\n"


def render_round323_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 323 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND323_STAGE4B_WATCH_TRIGGERS),
        "",
        "## Hard 4C Gates",
        *_bullet_lines(ROUND323_HARD_4C_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND323_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round323_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 323 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available; full adjusted OHLC backfill remains required before full-window MFE/MAE claims. Reported event returns and event prices are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND323_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round323_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 323 Row Separation Plan",
        "",
        "AI semiconductor rows must separate case evidence, trigger anchors and full adjusted OHLC backfill.",
        "",
        "Easy example: SK Hynix record profit is good evidence, but a -4% event reaction means it stays evidence-good/price-failed until later price and revision evidence repairs it.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND323_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round323_r2_loop17_reports(
    output_directory: str | Path = ROUND323_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND323_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND323_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND323_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND323_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round323_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND323_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round323_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round323_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round323_r2_loop17_case_matrix.csv",
        "target_aliases": output_dir / "round323_r2_loop17_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round323_r2_loop17_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round323_r2_loop17_trigger_grid.md",
        "summary": output_dir / "round323_r2_loop17_trigger_validation_summary.md",
        "stage_rules": output_dir / "round323_r2_loop17_stage_rules.md",
        "stage4b_4c_review": output_dir / "round323_r2_loop17_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round323_r2_loop17_score_adjustments.csv",
        "shadow_weights": output_dir / "round323_r2_loop17_shadow_weights.csv",
        "price_validation_plan": output_dir / "round323_r2_loop17_price_validation_plan.md",
        "row_separation_plan": output_dir / "round323_r2_loop17_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round323_case_rows())
    _write_csv(paths["target_aliases"], round323_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round323_trigger_rows())
    _write_csv(paths["score_adjustments"], round323_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round323_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round323_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round323_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round323_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round323_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round323_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round323_row_separation_plan_markdown(), encoding="utf-8")
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
    "ROUND323_CASE_CANDIDATES",
    "ROUND323_GREEN_BLOCKERS",
    "ROUND323_HARD_4C_GATES",
    "ROUND323_LARGE_SECTOR",
    "ROUND323_REQUIRED_TARGET_ALIASES",
    "ROUND323_ROW_SEPARATION_RULES",
    "ROUND323_SCORE_DOWN_AXES",
    "ROUND323_SCORE_UP_AXES",
    "ROUND323_SHADOW_WEIGHT_ROWS",
    "ROUND323_STAGE2_ACTIONABLE_RULES",
    "ROUND323_STAGE3_GREEN_RULES",
    "ROUND323_STAGE3_YELLOW_RULES",
    "ROUND323_STAGE4B_WATCH_TRIGGERS",
    "ROUND323_TRIGGER_RECORDS",
    "render_round323_stage4b_4c_review_markdown",
    "render_round323_stage_rules_markdown",
    "render_round323_trigger_grid_markdown",
    "round323_audit_payload",
    "round323_case_records",
    "round323_case_rows",
    "round323_shadow_weight_rows",
    "round323_summary",
    "round323_trigger_rows",
    "write_round323_r2_loop17_reports",
]
