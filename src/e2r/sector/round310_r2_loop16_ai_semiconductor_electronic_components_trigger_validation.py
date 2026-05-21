"""Round-310 R2 Loop-16 AI semiconductor and electronic components pack.

This module converts ``docs/round/round_310.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: an OpenAI/Stargate partnership can be Stage2-Actionable because
it shows demand direction. It still cannot become Stage3-Green until binding
wafer orders, shipment schedules, ASP and payment terms are visible.
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


ROUND310_SOURCE_ROUND_PATH = "docs/round/round_310.md"
ROUND310_ANALYST_ROUND_ID = "round_238"
ROUND310_LARGE_SECTOR = "AI_SEMICONDUCTOR_ELECTRONIC_COMPONENTS"
ROUND310_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND310_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round310_r2_loop16_ai_semiconductor_electronic_components_trigger_validation"
ROUND310_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop16_round238.jsonl"
ROUND310_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r2_loop16_round238.jsonl"
ROUND310_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round310_r2_loop16_ai_semiconductor_electronic_components_trigger_validation_audit.json"
ROUND310_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round238_r2_loop16_v1.csv"

ROUND310_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE": E2RArchetype.HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE.value,
    "MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW": E2RArchetype.MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW.value,
    "OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE": E2RArchetype.OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE.value,
    "FOUNDRY_MEGA_CONTRACT_STAGE2_WITH_YIELD_4B": E2RArchetype.FOUNDRY_MEGA_CONTRACT_STAGE2_WITH_YIELD_4B.value,
    "ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B": E2RArchetype.ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B.value,
    "HBM_CERTIFICATION_DELAY_FALSE_POSITIVE": E2RArchetype.HBM_CERTIFICATION_DELAY_FALSE_POSITIVE.value,
    "CHINA_FAB_EXPORT_CONTROL_4C_WATCH": E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH.value,
    "SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH": E2RArchetype.SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH.value,
    "ELECTRONIC_COMPONENT_LIDAR_STAGE2_ORDER_GATE": E2RArchetype.ELECTRONIC_COMPONENT_LIDAR_STAGE2_ORDER_GATE.value,
}

ROUND310_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "customer_qualification_mass_production_shipment_or_production_readiness_visible",
    "ASP_contract_price_OP_guidance_or_estimate_revision_visible",
    "event_return_at_least_5pct_or_market_relative_return_at_least_5pp",
    "equipment_order_capex_or_capacity_directly_tied_to_HBM_AI_memory_or_sensors",
    "partnership_is_separated_from_binding_order_or_volume_shipment",
    "no_unresolved_4c_overlay_certification_export_control_labor_or_yield_failure",
)

ROUND310_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_FCF_path_can_change_materially",
    "one_of_customer_volume_margin_capacity_or_4c_overlay_remains_open",
    "reported_price_anchor_or_relative_strength_supports_trigger",
    "case_is_not_pure_partnership_rumor_or_policy_relief",
)

ROUND310_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "HBM_customer_qualification_plus_volume_shipment_confirmed",
    "memory_ASP_converts_to_quarterly_OP_margin_and_FCF",
    "equipment_repeat_orders_or_customer_broadening_confirmed",
    "foundry_node_yield_utilization_and_margin_confirmed",
    "export_control_and_labor_output_continuity_cleared",
    "full_adjusted_OHLC_MFE_MAE_path_supports_stage_candidate",
)

ROUND310_GREEN_BLOCKERS: tuple[str, ...] = (
    "HBM_headline_without_customer_certification",
    "foundry_contract_without_node_yield_or_customer_identity",
    "AI_partnership_without_binding_wafer_order",
    "equipment_rumor_without_signed_order",
    "capex_without_installation_yield_or_customer_allocation",
    "component_partnership_without_design_in",
    "memory_supercycle_without_labor_export_control_and_inventory_overlay",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND310_SCORE_UP_AXES: tuple[str, ...] = (
    "hbm_customer_certification",
    "hbm_mass_production_shipment",
    "memory_asp_contract_power",
    "op_estimate_guidance_beat",
    "euv_capacity_commitment",
    "advanced_packaging_order_visibility",
    "binding_ai_infra_purchase",
    "export_license_stability",
    "labor_output_continuity",
)

ROUND310_SCORE_DOWN_AXES: tuple[str, ...] = (
    "hbm_headline_without_customer_certification",
    "foundry_contract_without_node_yield",
    "ai_partnership_without_binding_order",
    "equipment_rumor_without_signed_order",
)

ROUND310_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "HBM_rumor_or_test_speculation_before_customer_certification",
    "foundry_mega_contract_before_node_yield_customer_and_utilization_evidence",
    "equipment_customer_rumor_before_signed_order",
    "AI_infra_partnership_before_binding_wafer_order",
    "memory_supercycle_valuation_surge_before_labor_export_control_and_inventory_risks_clear",
    "component_partnership_before_design_in_and_revenue",
)

ROUND310_4C_WATCH_GATES: tuple[str, ...] = (
    "HBM_qualification_failure_or_customer_rejection",
    "export_license_revocation_limiting_China_fab_upgrade",
    "labor_strike_affecting_DRAM_NAND_output",
    "foundry_yield_failure_or_fab_utilization_loss",
    "inventory_write_down_from_unsold_HBM",
    "customer_cancellation_or_delayed_qualification",
)

ROUND310_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_price_reaction_and_reported_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_partnership_rumor_policy_or_capex_headline_as_actual_volume_shipment",
)


@dataclass(frozen=True)
class Round310ShadowWeightRow:
    archetype: E2RArchetype
    hbm_customer_certification: int
    hbm_mass_production_shipment: int
    memory_asp_contract_power: int
    op_estimate_guidance_beat: int
    euv_capacity_commitment: int
    advanced_packaging_order_visibility: int
    binding_ai_infra_purchase: int
    export_license_stability: int
    labor_output_continuity: int
    hbm_headline_without_customer_certification_penalty: int
    foundry_contract_without_node_yield_penalty: int
    ai_partnership_without_binding_order_penalty: int
    equipment_rumor_without_signed_order_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "hbm_customer_certification": _signed(self.hbm_customer_certification),
            "hbm_mass_production_shipment": _signed(self.hbm_mass_production_shipment),
            "memory_asp_contract_power": _signed(self.memory_asp_contract_power),
            "op_estimate_guidance_beat": _signed(self.op_estimate_guidance_beat),
            "euv_capacity_commitment": _signed(self.euv_capacity_commitment),
            "advanced_packaging_order_visibility": _signed(self.advanced_packaging_order_visibility),
            "binding_ai_infra_purchase": _signed(self.binding_ai_infra_purchase),
            "export_license_stability": _signed(self.export_license_stability),
            "labor_output_continuity": _signed(self.labor_output_continuity),
            "hbm_headline_without_customer_certification_penalty": _signed(self.hbm_headline_without_customer_certification_penalty),
            "foundry_contract_without_node_yield_penalty": _signed(self.foundry_contract_without_node_yield_penalty),
            "AI_partnership_without_binding_order_penalty": _signed(self.ai_partnership_without_binding_order_penalty),
            "equipment_rumor_without_signed_order_penalty": _signed(self.equipment_rumor_without_signed_order_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round310TriggerRecord:
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
class Round310CaseCandidate:
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
            "do_not_use_round310_cases_as_candidate_generation_input",
            "do_not_treat_ai_semiconductor_headline_as_green_without_shipment_asp_margin_customer_evidence",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND310_LARGE_SECTOR,
            large_sector=ROUND310_LARGE_SECTOR,
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
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4b" in field or "rumor" in field or "overheat" in field),
            stage4c_evidence=tuple(
                field
                for field in (*self.red_flag_fields, *self.evidence_fields)
                if "4c" in field or "delay" in field or "strike" in field or "export" in field or "failure" in field
            ),
            must_have_fields=ROUND310_STAGE3_GREEN_RULES,
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


ROUND310_CASE_CANDIDATES: tuple[Round310CaseCandidate, ...] = (
    Round310CaseCandidate(
        "r2_loop16_sk_hynix_hbm3e_hbm4_euv",
        "000660",
        "SK Hynix",
        E2RArchetype.HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE,
        (E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.MEMORY_HBM_CAPACITY_LEADER),
        "success_candidate",
        "hbm_leadership_stage2_to_yellow_green_candidate",
        "r2l16_skhynix_hbm4_T1/r2l16_skhynix_asml_T2",
        "Stage3-Yellow_to_Green_candidate",
        "Stage3-Yellow candidate / Green deferred",
        date(2024, 9, 26),
        date(2024, 9, 26),
        date(2025, 9, 12),
        date(2026, 5, 14),
        None,
        False,
        ("HBM3E_mass_production", "HBM4_internal_certification", "sample_shipment", "ASML_EUV_order_11_95tn_krw", "Yongin_M15X_HBM_advanced_DRAM_capacity", "event_return_7_3pct", "market_relative_6_1pp"),
        ("full_OHLC_MFE_MAE_missing", "multi_quarter_HBM_margin_missing", "customer_concentration_risk", "EUV_installation_schedule_missing", "HBM4_customer_volume_shipment_missing", "4b_valuation_overheat_watch"),
        7.3,
        None,
        None,
        None,
        None,
        None,
        {"hbm3e_mass_production_date": "2024-09-26", "hbm3e_event_return_pct": ">9", "hbm4_certification_date": "2025-09-12", "hbm4_event_return_pct": 7.3, "kospi_hbm4_context_pct": 1.2, "market_relative_return_pp": 6.1, "asml_euv_order_date": "2026-03-24", "asml_euv_order_krw_trn": 11.95, "asml_euv_order_usd_bn": 7.97, "asml_order_event_return_pct": 5.7, "capacity_targets": ["Yongin", "M15X", "HBM", "advanced_DRAM"]},
        "aligned",
        "excellent_stage2_to_yellow_green_candidate",
        "unknown",
        "yellow_success",
        "Sample to certification to capacity evidence is strong. Green still needs volume shipment, margin, customer concentration and full OHLC validation.",
    ),
    Round310CaseCandidate(
        "r2_loop16_samsung_memory_supercycle",
        "005930",
        "Samsung Electronics",
        E2RArchetype.MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW,
        (E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        "success_candidate",
        "memory_supercycle_stage3_yellow_candidate_with_4b_overlay",
        "r2l16_samsung_memory_T1",
        "Stage3-Yellow_candidate",
        "Stage3-Yellow candidate / 4B overlay",
        date(2025, 11, 17),
        date(2025, 11, 17),
        date(2026, 4, 7),
        date(2026, 5, 6),
        None,
        False,
        ("memory_price_hike_up_to_60pct", "DDR5_32GB_149_to_239_usd", "Q1_2026_OP_guidance_57_2tn_krw", "sales_guidance_133tn_krw", "LSEG_estimate_40_5tn_krw", "record_profit_event_return_5pct", "event_price_203000_krw", "May_2026_event_return_14_4pct"),
        ("full_OHLC_MFE_MAE_missing", "HBM_Nvidia_volume_certification_missing", "strike_risk_unresolved", "energy_cost_absorption_missing", "memory_price_sustainability_missing", "4b_index_crowding_overlay"),
        14.4,
        None,
        None,
        203000,
        None,
        None,
        {"max_memory_price_hike_pct": 60, "ddr5_32gb_price_before_usd": 149, "ddr5_32gb_price_after_usd": 239, "q1_2026_op_guidance_krw_trn": 57.2, "q1_2026_sales_guidance_krw_trn": 133, "q1_2026_op_lseg_estimate_krw_trn": 40.5, "record_profit_event_return_pct": 5, "record_profit_event_price_krw": 203000, "may_2026_event_return_pct": 14.4, "kospi_may_2026_event_return_pct": 6.45},
        "aligned",
        "Stage3_Yellow_candidate_with_4B_overheat_overlay",
        "unknown",
        "yellow_success",
        "ASP and OP guidance beat make this a Yellow candidate. Labor, export-control, HBM certification and inventory overlays block confirmed Green.",
    ),
    Round310CaseCandidate(
        "r2_loop16_samsung_skhynix_openai_stargate",
        "005930/000660",
        "Samsung Electronics / SK Hynix",
        E2RArchetype.OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE,
        (E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE, E2RArchetype.CONTRACT_HEADLINE_STAGE2_NOT_GREEN),
        "success_candidate",
        "openai_stargate_stage2_actionable_not_green",
        "r2l16_openai_stargate_T1",
        "Stage2-Actionable_demand_trigger",
        "Stage2-Actionable demand trigger",
        date(2025, 10, 2),
        date(2025, 10, 2),
        None,
        date(2025, 10, 2),
        None,
        False,
        ("OpenAI_Stargate_partnership", "Samsung_event_return_4_7pct", "SK_Hynix_event_return_12pct", "KOSPI_event_return_3pct", "combined_market_cap_addition_37bn_usd", "Stargate_project_500bn_usd", "OpenAI_DRAM_wafer_monthly_demand_900000"),
        ("binding_PO_missing", "wafer_allocation_missing", "HBM_ASP_missing", "delivery_schedule_missing", "customer_payment_terms_missing", "AI_partnership_without_binding_order"),
        12.0,
        None,
        None,
        None,
        None,
        None,
        {"samsung_event_return_pct": 4.7, "sk_hynix_event_return_pct": 12, "kospi_event_return_pct": 3, "combined_market_cap_addition_usd_bn": 37, "stargate_project_value_usd_bn": 500, "openai_dram_wafer_monthly_demand": 900000, "korea_data_center_capacity_mw_each": 20},
        "aligned",
        "Stage2_Actionable_AI_infra_demand_not_Green",
        "unknown",
        "stage2_watch_success",
        "AI infrastructure demand is actionable, but partnership evidence must not be scored as shipped wafers or recognized revenue.",
    ),
    Round310CaseCandidate(
        "r2_loop16_samsung_foundry_165b_contract",
        "005930",
        "Samsung Electronics",
        E2RArchetype.FOUNDRY_MEGA_CONTRACT_STAGE2_WITH_YIELD_4B,
        (E2RArchetype.CONTRACT_HEADLINE_STAGE2_NOT_GREEN, E2RArchetype.STATE_FOUNDRY_POLICY_RELIEF_NOT_GREEN),
        "4b_watch",
        "foundry_mega_contract_stage2_with_yield_4b",
        "r2l16_samsung_foundry_T1",
        "Stage2_with_yield_4B",
        "Stage2 + 4B-watch",
        date(2025, 7, 28),
        date(2025, 7, 28),
        None,
        date(2025, 7, 28),
        None,
        False,
        ("foundry_contract_16_5bn_usd", "contract_end_year_2033", "event_return_3_5pct", "global_company_customer_undisclosed"),
        ("customer_identity_missing", "node_details_missing", "yield_missing", "Texas_fab_utilization_missing", "gross_margin_missing", "payment_schedule_missing", "foundry_contract_without_node_yield"),
        3.5,
        None,
        None,
        None,
        None,
        None,
        {"contract_value_usd_bn": 16.5, "contract_end_year": 2033, "event_return_pct": 3.5, "counterparty_disclosed": False, "cutting_edge_2nm_likely": False, "yield_issue_reason": True},
        "aligned",
        "Stage2_contract_with_4B_yield_gate",
        "event_premium",
        "stage2_watch_success",
        "Large foundry contract is real Stage2 evidence. Without node, yield, utilization and margin it remains 4B-watch, not Green.",
    ),
    Round310CaseCandidate(
        "r2_loop16_hanmi_semiconductor_hbm_equipment",
        "042700",
        "Hanmi Semiconductor",
        E2RArchetype.ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B,
        (E2RArchetype.SEMI_EQUIPMENT_CAPEX, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        "success_candidate",
        "advanced_packaging_equipment_stage2_with_rumor_4b",
        "r2l16_hanmi_hbm_T0/r2l16_hanmi_micron_rumor_T2",
        "Stage2-Actionable_plus_rumor_4B",
        "Stage2-Actionable + rumor 4B",
        date(2024, 3, 26),
        date(2024, 3, 28),
        None,
        date(2024, 3, 28),
        None,
        False,
        ("HBM_advanced_packaging_equipment", "TSV_TC_bonder", "SK_Hynix_contract_21_48bn_krw", "recent_contracts_around_200bn_krw", "Hanmi_event_return_16pct", "market_relative_15_3pp", "possible_Micron_report_intraday_22pct"),
        ("confirmed_Micron_customer_missing", "repeat_orders_missing", "TSMC_Nvidia_supply_chain_volume_missing", "equipment_margin_missing", "customer_concentration_reduction_missing", "equipment_rumor_without_signed_order"),
        22.0,
        None,
        None,
        None,
        None,
        None,
        {"hanmi_event_return_pct": 16, "sk_hynix_context_return_pct": 4.3, "kospi_context_return_pct": 0.7, "market_relative_return_pp": 15.3, "sk_hynix_contract_krw_bn": 21.48, "recent_contracts_krw_bn": 200, "possible_micron_report_intraday_return_pct": 22, "micron_confirmed": False},
        "aligned",
        "Stage2_Actionable_with_rumor_4B",
        "unknown",
        "stage2_watch_success",
        "Signed SK Hynix order and strong price reaction are actionable. Unconfirmed Micron customer rumor is 4B-watch until signed order and margin evidence arrive.",
    ),
    Round310CaseCandidate(
        "r2_loop16_samsung_hbm_delay_false_positive",
        "005930",
        "Samsung Electronics",
        E2RArchetype.HBM_CERTIFICATION_DELAY_FALSE_POSITIVE,
        (E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.THESIS_BREAK_4C),
        "4c_thesis_break",
        "hbm_certification_delay_4c_watch_false_positive",
        "r2l16_samsung_hbm_delay_T0",
        "4C_watch_HBM_certification_delay",
        "4C-watch",
        date(2024, 5, 24),
        None,
        None,
        None,
        date(2024, 5, 24),
        False,
        ("HBM3_HBM3E_Nvidia_test_delay", "heat_power_issue", "Samsung_disputed_specifics", "Q2_2025_OP_guidance_4_6tn_krw", "LSEG_estimate_6_2tn_krw", "YoY_OP_decline_56pct", "chip_division_OP_decline_over_90pct"),
        ("HBM_certification_delay", "customer_qualification_failure_watch", "profit_miss", "inventory_write_down_watch", "AI_China_curb_profit_miss_watch"),
        None,
        -2.0,
        None,
        None,
        None,
        None,
        {"t0_event_return_pct": -2, "q2_2025_op_guidance_krw_trn": 4.6, "q2_2025_op_estimate_krw_trn": 6.2, "q2_2025_op_yoy_decline_pct": -56, "chip_division_op_decline_context_pct": ">90", "q2_2025_event_return_pct": -0.2, "q2_2025_kospi_return_pct": 1.2, "q2_2025_market_relative_return_pp": -1.4},
        "aligned",
        "HBM_certification_delay_4C_watch",
        "thesis_break",
        "should_have_been_red",
        "HBM qualification delay and later profit miss are Red Team overlays. They block Samsung memory Green unless resolved by customer volume shipment and margin recovery.",
    ),
    Round310CaseCandidate(
        "r2_loop16_china_fab_export_control",
        "005930/000660/067310/042700",
        "Samsung / SK Hynix / Hana Micron / Hanmi Semiconductor",
        E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH,
        (E2RArchetype.CHIP_EXPORT_CONTROL_4C_WATCH, E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C),
        "4c_thesis_break",
        "china_fab_export_control_4c_watch",
        "r2l16_china_fab_export_T1",
        "4C_watch_export_control",
        "4C-watch",
        date(2025, 9, 1),
        None,
        None,
        None,
        date(2025, 9, 1),
        False,
        ("US_authorization_revocation", "Samsung_event_return_minus_2_3pct", "SK_Hynix_event_return_minus_4_4pct", "KOSPI_minus_0_7pct", "Samsung_China_DRAM_over_33pct", "SK_China_DRAM_NAND_30_40pct", "license_delay_120_days"),
        ("export_license_revocation", "China_fab_upgrade_ceiling", "stranded_capex_risk", "production_impairment_watch", "customer_shipment_disruption_watch"),
        None,
        -4.4,
        None,
        None,
        None,
        None,
        {"samsung_event_return_pct": -2.3, "sk_hynix_event_return_pct": -4.4, "kospi_event_return_pct": -0.7, "samsung_market_relative_return_pp": -1.6, "sk_hynix_market_relative_return_pp": -3.7, "hana_micron_event_return_pct": -1.7, "hanmi_event_return_pct": -4.4, "samsung_china_dram_exposure_pct": ">33", "sk_china_dram_nand_exposure_pct": "30-40", "license_delay_days": 120},
        "aligned",
        "China_fab_export_control_4C_watch",
        "thesis_break",
        "should_have_been_red",
        "China fab license risk is not positive evidence. It must be carried as 4C-watch against memory/HBM rerating.",
    ),
    Round310CaseCandidate(
        "r2_loop16_samsung_labor_strike_4c",
        "005930",
        "Samsung Electronics",
        E2RArchetype.SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH,
        (E2RArchetype.LABOR_DISRUPTION_SYSTEMIC_POLICY_4C, E2RArchetype.MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW),
        "4c_thesis_break",
        "semiconductor_labor_strike_4c_watch",
        "r2l16_samsung_strike_T1",
        "4C_watch_labor_output_risk",
        "4C-watch",
        date(2026, 5, 15),
        None,
        None,
        None,
        date(2026, 5, 15),
        False,
        ("labor_strike_18_days", "event_return_minus_9_3pct", "potential_workers_over_50000", "workers_48000", "essential_staffing_7087", "DRAM_cut_3_4pct", "NAND_cut_2_3pct", "production_loss_30tn_krw"),
        ("labor_output_disruption", "customer_delivery_risk", "DRAM_NAND_supply_reduction", "government_arbitration_risk", "memory_supercycle_labor_overlay"),
        None,
        -9.3,
        None,
        None,
        None,
        None,
        {"event_return_pct": -9.3, "strike_days": 18, "potential_workers": ">50000", "workers": 48000, "essential_staffing": 7087, "dram_cut_pct": "3-4", "nand_cut_pct": "2-3", "production_loss_krw_trn": 30, "production_loss_usd_bn": 19.9},
        "aligned",
        "semiconductor_labor_strike_4C_watch",
        "thesis_break",
        "should_have_been_red",
        "A labor strike that threatens DRAM/NAND output blocks memory Green until output and delivery continuity are verified.",
    ),
    Round310CaseCandidate(
        "r2_loop16_lg_innotek_aeva_lidar",
        "011070",
        "LG Innotek / Aeva",
        E2RArchetype.ELECTRONIC_COMPONENT_LIDAR_STAGE2_ORDER_GATE,
        (E2RArchetype.AUTO_MOBILITY_COMPONENTS, E2RArchetype.ROBOTICS_FACTORY_AUTOMATION),
        "success_candidate",
        "electronic_component_lidar_stage2_order_gate",
        "r2l16_lginnotek_aeva_T1",
        "Stage2_component_diversification_not_Green",
        "Stage2 order-gate",
        date(2025, 7, 29),
        date(2025, 7, 29),
        None,
        date(2025, 7, 29),
        None,
        False,
        ("Aeva_collaboration_50mn_usd", "LG_Innotek_equity_investment_32mn_usd", "single_digit_stake", "vehicle_industrial_robotics_consumer_AR_markets"),
        ("KRX_price_anchor_missing", "design_in_missing", "mass_production_order_missing", "customer_launch_missing", "sensor_ASP_margin_missing", "module_integration_revenue_missing", "component_partnership_without_design_in"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"collaboration_value_usd_mn": 50, "equity_investment_usd_mn": 32, "stake": "single_digit", "target_markets": ["vehicles", "industrial_equipment", "robotics", "consumer_electronics", "AR_headsets"], "krx_price_anchor": "price_data_unavailable_after_deep_search"},
        "unknown",
        "Stage2_component_diversification_not_Green",
        "unknown",
        "stage2_watch_success",
        "Sensor collaboration and equity investment are Stage2 diversification evidence. Green needs design-in, launch, ASP/margin and module revenue.",
    ),
)


ROUND310_TRIGGER_RECORDS: tuple[Round310TriggerRecord, ...] = (
    Round310TriggerRecord("r2l16_skhynix_hbm4_T1", "r2_loop16_sk_hynix_hbm3e_hbm4_euv", "Stage3-Yellow", "2025-09-12", "HBM4 internal certification and production readiness; shares +7.3% while KOSPI +1.2%", 7.3, "excellent_stage2_to_yellow_green_candidate", "Stage3-Yellow_candidate", {"market_relative_return_pp": 6.1}),
    Round310TriggerRecord("r2l16_skhynix_asml_T2", "r2_loop16_sk_hynix_hbm3e_hbm4_euv", "Stage3-Yellow_validation", "2026-03-24", "ASML EUV order 11.95T won / $7.97B for Yongin/M15X HBM and advanced DRAM capacity; shares +5.7%", 5.7, "capacity_validation", "Stage3-Yellow_candidate", {"asml_euv_order_krw_trn": 11.95, "asml_euv_order_usd_bn": 7.97}),
    Round310TriggerRecord("r2l16_samsung_memory_T1", "r2_loop16_samsung_memory_supercycle", "Stage3-Yellow", "2026-04-07", "Q1 2026 OP guidance 57.2T won and sales 133T won beat estimates; shares +5% to KRW203,000", 5, "Stage3_Yellow_candidate_with_4B_overheat_overlay", "Stage3-Yellow_candidate", {"record_profit_event_price_krw": 203000}),
    Round310TriggerRecord("r2l16_openai_stargate_T1", "r2_loop16_samsung_skhynix_openai_stargate", "Stage2-Actionable", "2025-10-02", "OpenAI Stargate partnership; Samsung +4.7%, SK Hynix +12%, KOSPI +3%, market cap +$37B", "Samsung +4.7 / SK Hynix +12", "Stage2_Actionable_AI_infra_demand_not_Green", "Stage2-Actionable", {"combined_market_cap_addition_usd_bn": 37, "stargate_project_value_usd_bn": 500, "openai_dram_wafer_monthly_demand": 900000}),
    Round310TriggerRecord("r2l16_samsung_foundry_T1", "r2_loop16_samsung_foundry_165b_contract", "Stage2+4B", "2025-07-28", "Samsung foundry $16.5B global-company deal through 2033; shares +3.5%; node/yield/customer undisclosed", 3.5, "Stage2_contract_with_4B_yield_gate", "Stage2", {"contract_value_usd_bn": 16.5, "contract_end_year": 2033}),
    Round310TriggerRecord("r2l16_hanmi_hbm_T0", "r2_loop16_hanmi_semiconductor_hbm_equipment", "Stage2-Actionable", "2024-03-26/2024-03-28", "Hanmi HBM equipment order context; Hanmi +16%, SK Hynix +4.3%, KOSPI +0.7%", 16, "Stage2_Actionable_with_rumor_4B", "Stage2-Actionable", {"market_relative_return_pp": 15.3, "sk_hynix_contract_krw_bn": 21.48}),
    Round310TriggerRecord("r2l16_hanmi_micron_rumor_T2", "r2_loop16_hanmi_semiconductor_hbm_equipment", "4B-watch", "2024-03-28", "Possible Micron deal media report, intraday +22%, but Micron customer not confirmed", 22, "equipment_rumor_4B_watch", "4B-watch", {"micron_confirmed": False}),
    Round310TriggerRecord("r2l16_samsung_hbm_delay_T0", "r2_loop16_samsung_hbm_delay_false_positive", "4C-watch", "2024-05-24", "Samsung HBM3/HBM3E Nvidia test delay with heat/power issue reports; shares -2%", -2, "HBM_certification_delay_4C_watch", "4C-watch", {"samsung_disputed_specifics": True}),
    Round310TriggerRecord("r2l16_china_fab_export_T1", "r2_loop16_china_fab_export_control", "4C-watch", "2025-09-01", "U.S. revokes China fab authorizations; Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7%", "Samsung -2.3 / SK Hynix -4.4", "China_fab_export_control_4C_watch", "4C-watch", {"license_delay_days": 120, "hana_micron_event_return_pct": -1.7, "hanmi_event_return_pct": -4.4}),
    Round310TriggerRecord("r2l16_samsung_strike_T1", "r2_loop16_samsung_labor_strike_4c", "4C-watch", "2026-05-15", "Samsung labor strike, shares -9.3%, 18 days and DRAM/NAND output risk", -9.3, "semiconductor_labor_strike_4C_watch", "4C-watch", {"workers": 48000, "essential_staffing": 7087, "production_loss_krw_trn": 30}),
    Round310TriggerRecord("r2l16_lginnotek_aeva_T1", "r2_loop16_lg_innotek_aeva_lidar", "Stage2", "2025-07-29", "LG Innotek/Aeva $50M collaboration and $32M equity investment; no KRX price anchor found", "price_data_unavailable_after_deep_search", "Stage2_component_diversification_not_Green", "Stage2", {"collaboration_value_usd_mn": 50, "equity_investment_usd_mn": 32}),
)


ROUND310_SHADOW_WEIGHT_ROWS: tuple[Round310ShadowWeightRow, ...] = (
    Round310ShadowWeightRow(E2RArchetype.HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE, 5, 5, 4, 4, 4, 2, 3, 3, 2, -5, -1, -2, -1, "qualification+shipment+capacity", "volume/margin/concentration open", "customer volume shipment+margin+OHLC", "SK Hynix HBM leadership."),
    Round310ShadowWeightRow(E2RArchetype.MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW, 2, 3, 5, 5, 2, 0, 2, 2, 3, -3, -1, -1, -1, "ASP+OP beat", "risk overlays open", "durable ASP+OP+labor/export clear", "Samsung memory ASP."),
    Round310ShadowWeightRow(E2RArchetype.OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE, 2, 2, 3, 2, 1, 1, 5, 1, 1, -2, -1, -4, -1, "AI infra demand signal", "binding order missing", "wafer allocation+payment", "OpenAI Stargate."),
    Round310ShadowWeightRow(E2RArchetype.FOUNDRY_MEGA_CONTRACT_STAGE2_WITH_YIELD_4B, 0, 0, 1, 2, 3, 0, 1, 2, 1, -1, -5, -1, -1, "large foundry contract", "node/yield missing", "node+yield+utilization", "Samsung foundry."),
    Round310ShadowWeightRow(E2RArchetype.ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B, 2, 2, 1, 2, 1, 5, 1, 1, 1, -2, -1, -1, -5, "signed equipment order", "rumor/customer concentration", "repeat orders+margin", "Hanmi Semiconductor."),
    Round310ShadowWeightRow(E2RArchetype.HBM_CERTIFICATION_DELAY_FALSE_POSITIVE, -5, -4, 0, -4, 0, 0, 0, 2, 1, -5, -1, -1, -1, "qualification delay blocks", "negative overlay", "N/A", "Samsung HBM delay."),
    Round310ShadowWeightRow(E2RArchetype.CHINA_FAB_EXPORT_CONTROL_4C_WATCH, 0, 0, 0, 0, 0, 1, 0, 5, 1, -1, -2, -1, -1, "license stability gate", "export restriction risk", "N/A", "China fab export control."),
    Round310ShadowWeightRow(E2RArchetype.SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH, 0, 0, 2, -3, 0, 0, 0, 1, 5, -1, -1, -1, -1, "output continuity gate", "labor disruption risk", "N/A", "Samsung labor strike."),
    Round310ShadowWeightRow(E2RArchetype.ELECTRONIC_COMPONENT_LIDAR_STAGE2_ORDER_GATE, 0, 1, 1, 1, 0, 0, 0, 1, 1, -1, -1, -1, -1, "component collaboration", "design-in/order missing", "design-in+launch+margin", "LG Innotek/Aeva."),
)


def round310_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND310_CASE_CANDIDATES]


def round310_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND310_CASE_CANDIDATES]


def round310_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND310_TRIGGER_RECORDS]


def round310_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND310_SHADOW_WEIGHT_ROWS]


def round310_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND310_REQUIRED_TARGET_ALIASES.items()]


def round310_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND310_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND310_SCORE_DOWN_AXES]
    )


def round310_summary() -> dict[str, object]:
    return {
        "source_round": ROUND310_SOURCE_ROUND_PATH,
        "round_id": ROUND310_ANALYST_ROUND_ID,
        "large_sector": ROUND310_LARGE_SECTOR,
        "method": ROUND310_METHOD,
        "case_candidate_count": len(ROUND310_CASE_CANDIDATES),
        "trigger_count": len(ROUND310_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND310_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 4,
        "stage2_event_candidate_count": 2,
        "stage3_yellow_candidate_count": 4,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 5,
        "stage4c_watch_count": 3,
        "hard_4c_case_count": 0,
        "evidence_good_but_price_failed_count": 3,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round310_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND310_SOURCE_ROUND_PATH,
        "round_id": ROUND310_ANALYST_ROUND_ID,
        "large_sector": ROUND310_LARGE_SECTOR,
        "method": ROUND310_METHOD,
        "summary": round310_summary(),
        "required_target_aliases": dict(ROUND310_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND310_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND310_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND310_STAGE3_GREEN_RULES,
        "green_blockers": ROUND310_GREEN_BLOCKERS,
        "score_up_axes": ROUND310_SCORE_UP_AXES,
        "score_down_axes": ROUND310_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND310_STAGE4B_WATCH_TRIGGERS,
        "stage4c_watch_gates": ROUND310_4C_WATCH_GATES,
        "row_separation_rules": ROUND310_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round310_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_ai_semiconductor_headline_as_green_without_shipment_asp_margin_customer_evidence",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round310_summary_markdown() -> str:
    summary = round310_summary()
    lines = [
        "# R2 Loop 16 AI Semiconductor / Electronic Components Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: SK Hynix HBM4 certification can be a Stage3-Yellow candidate because sample/certification/capacity evidence is visible. It is not confirmed Green until volume shipment, margin, customer concentration and full OHLC validation clear.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- HBM, memory ASP, OpenAI/Stargate, foundry, packaging equipment, export-control, labor and sensor partnership rows must stay separate.",
            "- Stage2-Actionable needs event evidence and direct economic bridge, not only AI semiconductor wording.",
            "- Stage3-Green confirmed: `0`.",
            "- OHLC backfill missing should not downgrade valid Stage2 or Yellow candidates.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round310_trigger_grid_markdown() -> str:
    lines = [
        "# Round 310 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round310_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round310_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 310 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND310_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND310_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND310_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND310_GREEN_BLOCKERS),
            "",
            "## 4C Watch Gates",
            *_bullet_lines(ROUND310_4C_WATCH_GATES),
        ]
    ) + "\n"


def render_round310_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 310 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND310_STAGE4B_WATCH_TRIGGERS),
        "",
        "## 4C Watch Gates",
        *_bullet_lines(ROUND310_4C_WATCH_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND310_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round310_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 310 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND310_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round310_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 310 Row Separation Plan",
        "",
        "Case evidence, trigger anchors and full OHLC windows must be separate rows.",
        "",
        "Easy example: LG Innotek/Aeva can be Stage2 because collaboration and equity investment are real. It still cannot become Green without design-in, production order, customer launch and margin evidence.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND310_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round310_r2_loop16_reports(
    output_directory: str | Path = ROUND310_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND310_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND310_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND310_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND310_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round310_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND310_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round310_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round310_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round310_r2_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round310_r2_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round310_r2_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round310_r2_loop16_trigger_grid.md",
        "summary": output_dir / "round310_r2_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round310_r2_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round310_r2_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round310_r2_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round310_r2_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round310_r2_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round310_r2_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round310_case_rows())
    _write_csv(paths["target_aliases"], round310_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round310_trigger_rows())
    _write_csv(paths["score_adjustments"], round310_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round310_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round310_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round310_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round310_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round310_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round310_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round310_row_separation_plan_markdown(), encoding="utf-8")
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
    "ROUND310_4C_WATCH_GATES",
    "ROUND310_CASE_CANDIDATES",
    "ROUND310_GREEN_BLOCKERS",
    "ROUND310_LARGE_SECTOR",
    "ROUND310_REQUIRED_TARGET_ALIASES",
    "ROUND310_ROW_SEPARATION_RULES",
    "ROUND310_SCORE_DOWN_AXES",
    "ROUND310_SCORE_UP_AXES",
    "ROUND310_SHADOW_WEIGHT_ROWS",
    "ROUND310_STAGE2_ACTIONABLE_RULES",
    "ROUND310_STAGE3_GREEN_RULES",
    "ROUND310_STAGE3_YELLOW_RULES",
    "ROUND310_STAGE4B_WATCH_TRIGGERS",
    "ROUND310_TRIGGER_RECORDS",
    "render_round310_stage4b_4c_review_markdown",
    "render_round310_stage_rules_markdown",
    "render_round310_trigger_grid_markdown",
    "round310_audit_payload",
    "round310_case_records",
    "round310_case_rows",
    "round310_shadow_weight_rows",
    "round310_summary",
    "round310_trigger_rows",
    "write_round310_r2_loop16_reports",
]
