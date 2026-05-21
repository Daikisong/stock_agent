"""Round-322 R1 Loop-17 industrial orders trigger validation pack.

This module converts ``docs/round/round_322.md`` into calibration-only case
records, trigger rows, shadow weights, and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: LS Electric had a strong target-price upgrade and U.S. data-center
story, but the reported event return was -5.4%. That is evidence-good but
price-failed, so it must not become Stage2-Actionable or Stage3-Green from the
report alone.
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


ROUND322_SOURCE_ROUND_PATH = "docs/round/round_322.md"
ROUND322_ANALYST_ROUND_ID = "round_250"
ROUND322_LOOP_NAME = "R1 Loop 17"
ROUND322_LARGE_SECTOR = "INDUSTRIALS_ORDERS_INFRASTRUCTURE"
ROUND322_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND322_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round322_r1_loop17_industrials_orders_infrastructure"
ROUND322_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop17_round250.jsonl"
ROUND322_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r1_loop17_round250.jsonl"
ROUND322_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round322_r1_loop17_industrials_orders_audit.json"
ROUND322_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round250_r1_loop17_v1.csv"

ROUND322_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE": E2RArchetype.SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE.value,
    "SHIPBUILDING_NAVAL_EXPORT_STAGE2_WITH_SANCTION_4B": E2RArchetype.SHIPBUILDING_NAVAL_EXPORT_STAGE2_WITH_SANCTION_4B.value,
    "DEFENSE_INDUSTRIAL_EXPORT_STAGE2_YELLOW": E2RArchetype.DEFENSE_INDUSTRIAL_EXPORT_STAGE2_YELLOW.value,
    "GRID_EQUIPMENT_AI_POWER_STAGE2_PROMOTE": E2RArchetype.GRID_EQUIPMENT_AI_POWER_STAGE2_PROMOTE.value,
    "GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED": E2RArchetype.GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED.value,
    "TRANSFORMER_CAPACITY_EXPANSION_STAGE2_NO_PRICE": E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2_NO_PRICE.value,
    "NUCLEAR_SMR_INDUSTRIAL_SUPPLY_STAGE2_WITH_FINAL_CONTRACT_GATE": E2RArchetype.NUCLEAR_SMR_INDUSTRIAL_SUPPLY_STAGE2_WITH_FINAL_CONTRACT_GATE.value,
    "SHIPBUILDING_ORDER_CANCELLATION_4C": E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_4C.value,
}

ROUND322_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_at_least_5pct",
    "market_relative_return_at_least_5pp",
    "contract_deal_order_value_is_clear",
    "order_can_convert_to_revenue_or_backlog",
    "repeat_order_or_new_market_entry_exists",
    "capacity_or_localization_links_directly_to_customer_demand",
    "sanction_cancellation_mou_only_margin_unknown_4B_is_identified",
)

ROUND322_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_or_FCF_path_likely_changes",
    "delivery_margin_capacity_or_sanction_gate_partly_open",
    "repeat_export_or_capacity_conversion_is_visible",
    "full_Green_fatal_blocker_absent",
)

ROUND322_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "contract_or_order_value_is_final",
    "backlog_converts_to_profitable_revenue",
    "production_capacity_and_utilization_are_visible",
    "margin_and_cash_conversion_are_confirmed",
    "sanction_cancellation_mou_only_or_legal_risk_is_resolved",
    "full_window_MFE_MAE_is_available_and_supportive",
)

ROUND322_GREEN_BLOCKERS: tuple[str, ...] = (
    "shipbuilding_policy_without_orders",
    "theme_label_without_orders",
    "report_upgrade_without_price_validation",
    "capacity_headline_without_utilization",
    "MOU_without_final_contract",
    "geopolitical_sanction_ignored",
    "orderbook_without_cancellation_check",
    "local_production_without_margin",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND322_SCORE_UP_AXES: tuple[str, ...] = (
    "reported_event_return",
    "market_relative_return",
    "contract_value_visibility",
    "naval_shipbuilding_us_workshare",
    "grid_equipment_backlog",
    "capacity_utilization",
    "repeat_export_operator",
    "order_quality_risk",
)

ROUND322_SCORE_DOWN_AXES: tuple[str, ...] = (
    "theme_label_without_orders",
    "report_upgrade_without_price_validation",
    "capacity_headline_without_utilization",
    "MOU_without_final_contract",
    "shipbuilding_policy_without_orders",
    "geopolitical_sanction_ignored",
    "orderbook_without_cancellation_check",
    "local_production_without_margin",
)

ROUND322_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "shipbuilding_policy_rally_before_formal_US_orders",
    "China_sanction_after_US_linked_naval_optionality",
    "transformer_capacity_expansion_before_utilization",
    "target_price_upgrade_but_stock_falls",
    "local_production_or_technology_transfer_before_margin",
    "SMR_MOU_before_final_equipment_contract",
    "orderbook_becomes_cancellation_or_arbitration",
)

ROUND322_HARD_4C_GATES: tuple[str, ...] = (
    "major_order_cancellation",
    "arbitration_or_advance_payment_dispute",
    "geopolitical_sanction_blocking_operations",
    "final_contract_failure_after_preferred_bidder_or_MOU",
    "large_contract_with_negative_margin_or_cash_conversion",
    "capacity_expansion_followed_by_demand_collapse",
)

ROUND322_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_reported_event_return_market_relative_return_contract_value_and_cancellation_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
    "do_not_treat_MASGA_AI_power_SMR_or_target_price_headline_as_Green_without_margin_capacity_finality_or_price_validation",
)


@dataclass(frozen=True)
class Round322TriggerRecord:
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
class Round322CaseCandidate:
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
            "do_not_use_round322_cases_as_candidate_generation_input",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_MASGA_AI_power_SMR_or_target_price_headline_as_Green_without_margin_capacity_finality_or_price_validation",
        ]
        if not self.strong_4c_confirmed:
            guardrails.append("strong_4c_confirmed_false")
        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "sanction" in field
            or "MOU" in field
            or "margin" in field
            or "local_production" in field
            or "capacity" in field
            or "price_failed" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "cancellation" in field
            or "arbitration" in field
            or "sanction" in field
            or "thesis_break" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND322_LARGE_SECTOR,
            large_sector=ROUND322_LARGE_SECTOR,
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
            must_have_fields=ROUND322_STAGE3_GREEN_RULES,
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


ROUND322_CASE_CANDIDATES: tuple[Round322CaseCandidate, ...] = (
    Round322CaseCandidate(
        "r1_loop17_hd_hyundai_heavy_mipo_masga",
        "329180/010620",
        "HD Hyundai Heavy Industries / HD Hyundai Mipo",
        E2RArchetype.SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE,
        (E2RArchetype.SHIPBUILDING_MERGER_SCALE_STAGE2_WITH_INTEGRATION_4B, E2RArchetype.SHIPBUILDING_US_POLICY_MASGA),
        "success_candidate",
        "Stage2_Actionable_shipbuilding_consolidation",
        "T1/T2",
        "Stage2-Actionable_shipbuilding_consolidation",
        "Stage2-Actionable",
        date(2025, 8, 1),
        date(2025, 8, 27),
        None,
        date(2025, 8, 27),
        None,
        False,
        ("MASGA_US_Korea_shipbuilding_cooperation", "HD_HHI_plus_11_3pct", "Mipo_plus_14_6pct", "record_high_close", "exchange_ratio_1_Mipo_for_1_04059146_HHI"),
        ("actual_US_naval_orders_missing", "US_shipyard_workshare_missing", "Jones_Act_or_US_law_resolution_missing", "post_merger_margin_missing", "dock_labor_capacity_missing", "full_OHLC_MFE_MAE_missing"),
        None,
        None,
        {"trigger_date": "2025-08-27", "hd_hyundai_heavy_event_return_pct": 11.3, "hd_hyundai_mipo_event_return_pct": 14.6, "record_high": True, "exchange_ratio": "1_HD_Hyundai_Mipo_for_1.04059146_HD_Hyundai_Heavy"},
        "aligned",
        "excellent_stage2_actionable_shipbuilding_consolidation",
        "event_premium",
        "stage2_watch_success",
        "MASGA-linked merger had strong event returns, but actual U.S. orders/workshare and post-merger margin remain gates.",
    ),
    Round322CaseCandidate(
        "r1_loop17_hanwha_ocean_us_navy_china_sanction",
        "042660",
        "Hanwha Ocean",
        E2RArchetype.SHIPBUILDING_NAVAL_EXPORT_STAGE2_WITH_SANCTION_4B,
        (E2RArchetype.GEOPOLITICAL_SANCTION_SHIPBUILDING_4C_WATCH, E2RArchetype.NAVAL_SHIPBUILDING_GEOPOLITICAL_STAGE2_WITH_DILUTION_4B),
        "success_candidate",
        "Stage2_naval_optionality_with_geopolitical_4B",
        "T0/T2",
        "Stage2_naval_optionality_with_geopolitical_4B",
        "Stage2 + 4B-watch",
        date(2025, 10, 14),
        date(2025, 12, 23),
        None,
        date(2025, 10, 14),
        None,
        False,
        ("US_Navy_frigate_optionality", "Hanwha_Ocean_plus_6pct", "Philly_Shipyard_100M_usd_acquisition", "Philly_expansion_5B_usd_pledge", "US_Navy_MRO_exposure", "China_sanctions_five_US_linked_subsidiaries"),
        ("China_sanction_4B", "formal_US_Navy_contract_value_missing", "margin_missing", "delivery_schedule_missing", "US_shipyard_capacity_missing", "full_OHLC_MFE_MAE_missing"),
        6.0,
        -5.8,
        {"frigate_trigger_date": "2025-12-23", "frigate_event_return_pct": 6.0, "china_sanction_date": "2025-10-14", "china_sanction_event_return_pct": -5.8, "hd_hyundai_heavy_same_context_return_pct": -4.1, "ft_intraday_context_pct": -8, "philly_shipyard_acquisition_usd_mn": 100, "philly_expansion_pledge_usd_bn": 5},
        "aligned",
        "Stage2_naval_optional_with_geopolitical_4B",
        "event_premium",
        "stage2_watch_success",
        "U.S. naval optionality is real, but China sanction risk is a material 4B overlay.",
    ),
    Round322CaseCandidate(
        "r1_loop17_hyundai_rotem_k2_poland",
        "064350",
        "Hyundai Rotem",
        E2RArchetype.DEFENSE_INDUSTRIAL_EXPORT_STAGE2_YELLOW,
        (E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, E2RArchetype.EXPORT_ORDER_TO_COMBAT_VALIDATION_YELLOW),
        "success_candidate",
        "Stage3_Yellow_candidate_defense_industrial_export",
        "T0/T2",
        "Stage3-Yellow_candidate_defense_industrial_export",
        "Stage3-Yellow candidate",
        date(2024, 4, 9),
        date(2024, 4, 9),
        date(2025, 8, 1),
        date(2025, 8, 1),
        None,
        False,
        ("K2_Poland_export_earnings_beat", "Hyundai_Rotem_plus_9_3pct", "event_price_41300_won", "KOSPI_minus_0_3pct", "second_Poland_K2_contract_6_5B_usd", "180_tanks", "61_Poland_local_production"),
        ("delivery_margin_missing", "local_production_cost_missing", "technology_transfer_cost_missing", "working_capital_missing", "service_package_margin_missing", "full_OHLC_MFE_MAE_missing"),
        9.3,
        None,
        {"earnings_trigger_date": "2024-04-09", "earnings_event_return_pct": 9.3, "earnings_event_price_krw": 41300, "kospi_same_context_pct": -0.3, "market_relative_pp": 9.6, "poland_second_contract_date": "2025-08-01", "contract_value_estimate_usd_bn": 6.5, "tank_count": 180, "poland_local_production_count": 61, "first_deliveries_planned": 2026, "local_production_period": "2028-2030"},
        "aligned",
        "Stage3_Yellow_candidate_repeat_export",
        "event_premium",
        "yellow_success",
        "Repeat export and local production support Yellow candidate review; margin and delivery execution remain gates.",
    ),
    Round322CaseCandidate(
        "r1_loop17_hd_hyundai_electric_ai_power",
        "267260",
        "HD Hyundai Electric",
        E2RArchetype.GRID_EQUIPMENT_AI_POWER_STAGE2_PROMOTE,
        (E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_STAGE2, E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_BOTTLENECK),
        "success_candidate",
        "Stage2_promote_candidate_grid_equipment",
        "T1/T2",
        "Stage2_promote_candidate_grid_equipment",
        "Stage2_promote_candidate",
        date(2024, 1, 1),
        date(2024, 7, 11),
        None,
        date(2024, 7, 11),
        None,
        False,
        ("AI_data_center_power_demand", "reported_plus_333pct_since_Jan_2024", "hedge_funds_broaden_AI_to_electricity_equipment", "power_equipment_beneficiary"),
        ("new_order_backlog_missing", "transformer_ASP_missing", "US_market_share_missing", "Saudi_market_share_missing", "operating_margin_missing", "capacity_expansion_ROI_missing", "full_OHLC_MFE_MAE_missing"),
        None,
        None,
        {"trigger_reference_date": "2024-07-11", "reported_share_return_since_jan_2024_pct": 333, "theme": "AI_data_center_power_demand", "evidence_source_type": "reported_broad_AI_power_chain_investor_flow"},
        "missed_due_to_score",
        "missed_structural_if_stage2_ignored",
        "true_rerating",
        "missed_structural",
        "Broad AI power-equipment move implies potential missed structural case if Stage2 is too conservative; backlog and margin still required.",
    ),
    Round322CaseCandidate(
        "r1_loop17_ls_electric_us_data_center_price_failed",
        "010120",
        "LS Electric",
        E2RArchetype.GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED,
        (E2RArchetype.GRID_EQUIPMENT_US_GROWTH_STAGE2, E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED),
        "failed_rerating",
        "evidence_good_but_price_failed",
        "T0/T2",
        "evidence_good_but_price_failed",
        "Stage2 only / no Actionable",
        date(2024, 7, 1),
        None,
        None,
        date(2024, 7, 1),
        None,
        False,
        ("Daiwa_target_raise_150000_to_280000_won", "target_price_raise_87pct", "US_revenue_share_expected_20pct", "data_center_renewables_EV_demand", "shares_minus_5_4pct_at_208500_won"),
        ("price_failed_report_upgrade", "actual_US_orders_missing", "backlog_missing", "margin_missing", "data_center_customer_disclosure_missing", "capacity_ROI_missing"),
        None,
        -5.4,
        {"trigger_date": "2024-07-01", "target_price_old_krw": 150000, "target_price_new_krw": 280000, "target_price_raise_pct": 87, "reported_event_price_krw": 208500, "reported_event_return_pct": -5.4, "us_revenue_share_2022_context_pct": "<5", "us_revenue_share_2024_expected_pct": 20},
        "evidence_good_but_price_failed",
        "evidence_good_but_price_failed",
        "no_rerating",
        "false_yellow",
        "Good report evidence was rejected by the price reaction; do not promote on target-price upgrade alone.",
    ),
    Round322CaseCandidate(
        "r1_loop17_hyosung_heavy_us_transformer_capacity",
        "298040",
        "Hyosung Heavy Industries / Hyosung HICO",
        E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2_NO_PRICE,
        (E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2, E2RArchetype.GRID_TRANSFORMER_DATA_CENTER_STAGE2),
        "success_candidate",
        "Stage2_transformer_capacity_no_price",
        "T0/T2",
        "Stage2_transformer_capacity_no_price",
        "Stage2",
        date(2025, 11, 12),
        date(2025, 12, 2),
        None,
        date(2025, 12, 2),
        None,
        False,
        ("US_GSU_demand_plus_274pct_since_2019", "average_lead_time_143_weeks", "Hyosung_HICO_Memphis_expansion_157M_usd", "US_transformer_shortage"),
        ("direct_KRX_price_anchor_missing", "specific_orderbook_missing", "capacity_utilization_missing", "US_customer_contracts_missing", "margin_missing", "capex_ROI_missing", "shortage_duration_missing"),
        None,
        None,
        {"industry_reference_date": "2025-12-02", "gsu_demand_increase_since_2019_pct": 274, "average_lead_time_weeks": 143, "hyosung_hico_memphis_expansion_usd_mn": 157, "direct_price_anchor": "price_data_unavailable_after_deep_search"},
        "aligned",
        "Stage2_capacity_expansion_not_Green",
        "event_premium",
        "stage2_watch_success",
        "Transformer shortage and U.S. capacity expansion are Stage2 evidence, but direct price/orderbook/margin are unavailable.",
    ),
    Round322CaseCandidate(
        "r1_loop17_doosan_enerbility_smr_ai_power",
        "034020",
        "Doosan Enerbility",
        E2RArchetype.NUCLEAR_SMR_INDUSTRIAL_SUPPLY_STAGE2_WITH_FINAL_CONTRACT_GATE,
        (E2RArchetype.NUCLEAR_SMR_POLICY_MOU, E2RArchetype.NUCLEAR_SMR_GRID_POLICY),
        "event_premium",
        "Stage2_nuclear_SMR_industrial_supply",
        "T0/T2",
        "Stage2_nuclear_SMR_industrial_supply",
        "Stage2",
        date(2025, 8, 26),
        date(2025, 8, 26),
        None,
        date(2025, 8, 26),
        None,
        False,
        ("KHNP_Doosan_X_energy_AWS_SMR_cooperation", "Fermi_America_Texas_AI_project", "nuclear_SMR_equipment_supply_chain", "AI_power_demand_context"),
        ("final_equipment_contract_missing", "equipment_workshare_missing", "licensing_missing", "project_financing_missing", "margin_missing", "delivery_schedule_missing", "MOU_without_final_contract_4B"),
        None,
        None,
        {"trigger_date": "2025-08-26", "counterparties": ["KHNP", "X-energy", "Amazon_Web_Services", "Fermi_America"], "project_context": "Texas_AI_project_nuclear_SMR_equipment", "direct_price_anchor": "price_data_unavailable_after_deep_search"},
        "aligned",
        "Stage2_SMR_supply_chain_not_Green",
        "policy_event_rerating",
        "stage2_watch_success",
        "SMR/AI-power cooperation is Stage2; final equipment contract, workshare, licensing and margin are missing.",
    ),
    Round322CaseCandidate(
        "r1_loop17_samsung_heavy_zvezda_cancellation",
        "010140",
        "Samsung Heavy Industries",
        E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_4C,
        (E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C, E2RArchetype.SHIPBUILDING_CONTRACT_CANCELLATION_4C),
        "4c_thesis_break",
        "4C_order_cancellation",
        "T1/T3",
        "4C_order_cancellation",
        "4C-watch",
        date(2020, 1, 1),
        date(2020, 12, 31),
        None,
        None,
        date(2025, 6, 18),
        True,
        ("Zvezda_icebreaker_order_backlog", "cancelled_order_value_4_85T_won", "cancelled_order_value_3_54B_usd", "10_icebreaker_LNG_carriers", "7_icebreaker_shuttle_tankers", "Singapore_arbitration"),
        ("major_order_cancellation_4C", "illegal_termination_by_shipowner", "advance_payment_return_demand", "war_related_uncertainty", "damages_recovery_missing", "replacement_orders_missing"),
        None,
        None,
        {"trigger_date": "2025-06-18", "cancelled_order_value_krw_trn": 4.85, "cancelled_order_value_usd_bn": 3.54, "original_order_period": "2020-2021", "vessel_scope": ["10_icebreaker_LNG_carriers", "7_icebreaker_shuttle_tankers"], "direct_price_anchor": "price_data_unavailable_after_deep_search"},
        "aligned",
        "order_cancellation_4C_thesis_break",
        "thesis_break",
        "should_have_been_red",
        "Major Zvezda order cancellation breaks backlog quality; recovery requires damages collection and replacement orders.",
    ),
)

ROUND322_TRIGGER_RECORDS: tuple[Round322TriggerRecord, ...] = (
    Round322TriggerRecord("r1l17_hd_hhi_mipo_T1", "r1_loop17_hd_hyundai_heavy_mipo_masga", "Stage2-Actionable_shipbuilding_merger", "2025-08-27", "HD Hyundai Heavy/Mipo MASGA merger; +11.3%/+14.6% and record-high context.", "HD_HHI_+11.3_Mipo_+14.6", "excellent_stage2_actionable_shipbuilding_consolidation", "Stage2-Actionable", {"hd_hyundai_heavy_event_return_pct": 11.3, "hd_hyundai_mipo_event_return_pct": 14.6, "record_high": True}),
    Round322TriggerRecord("r1l17_hanwha_ocean_frigate_T0", "r1_loop17_hanwha_ocean_us_navy_china_sanction", "Stage2_naval_optionality", "2025-12-23", "Trump says Hanwha will participate in U.S. Navy frigate class; Hanwha Ocean +6%.", 6, "Stage2_naval_optional", "Stage2", {"philly_shipyard_acquisition_usd_mn": 100, "philly_expansion_pledge_usd_bn": 5}),
    Round322TriggerRecord("r1l17_hanwha_ocean_china_T2", "r1_loop17_hanwha_ocean_us_navy_china_sanction", "4B_geopolitical_sanction", "2025-10-14", "China sanctions five U.S.-linked Hanwha Ocean subsidiaries; Hanwha Ocean -5.8%, HD HHI -4.1%.", -5.8, "geopolitical_sanction_4B", "4B-watch", {"hd_hyundai_heavy_same_context_return_pct": -4.1, "ft_intraday_context_pct": -8}),
    Round322TriggerRecord("r1l17_hyundai_rotem_earnings_T0", "r1_loop17_hyundai_rotem_k2_poland", "Stage2-Actionable_export_earnings", "2024-04-09", "K2 Poland shipment expected to drive Q1 earnings beat; shares +9.3% to 41,300 won vs KOSPI -0.3%.", 9.3, "excellent_export_earnings_entry", "Stage2-Actionable", {"entry_price_krw": 41300, "market_relative_pp": 9.6}),
    Round322TriggerRecord("r1l17_hyundai_rotem_poland_T2", "r1_loop17_hyundai_rotem_k2_poland", "Stage3-Yellow_candidate_repeat_export", "2025-08-01", "Poland signs second K2 contract for 180 tanks, estimated $6.5B, with 61 produced locally.", "price_data_unavailable_after_deep_search", "repeat_export_yellow_candidate", "Stage3-Yellow_candidate", {"contract_value_estimate_usd_bn": 6.5, "tank_count": 180, "poland_local_production_count": 61}),
    Round322TriggerRecord("r1l17_hd_hyundai_electric_ai_T1", "r1_loop17_hd_hyundai_electric_ai_power", "Stage2_promote_candidate", "2024-07-11", "Reuters reports HD Hyundai Electric up 333% since January 2024 as AI demand broadens to power equipment.", "reported_+333_since_Jan_2024", "missed_structural_if_stage2_ignored", "Stage2_promote_candidate", {"reported_share_return_since_jan_2024_pct": 333}),
    Round322TriggerRecord("r1l17_ls_electric_report_T0", "r1_loop17_ls_electric_us_data_center_price_failed", "evidence_good_but_price_failed", "2024-07-01", "Daiwa raises target to 280,000 won, but shares fall 5.4% to 208,500 won.", -5.4, "price_failed_report_upgrade", "no_actionable", {"target_price_old_krw": 150000, "target_price_new_krw": 280000, "entry_price_krw": 208500}),
    Round322TriggerRecord("r1l17_hyosung_transformer_T0", "r1_loop17_hyosung_heavy_us_transformer_capacity", "Stage2_capacity_expansion_no_price", "2025-12-02", "U.S. GSU transformer demand +274% since 2019, average lead time 143 weeks, Hyosung HICO $157M Memphis expansion.", "price_data_unavailable_after_deep_search", "capacity_expansion_not_green", "Stage2", {"gsu_demand_increase_since_2019_pct": 274, "average_lead_time_weeks": 143, "hyosung_hico_memphis_expansion_usd_mn": 157}),
    Round322TriggerRecord("r1l17_doosan_smr_T0", "r1_loop17_doosan_enerbility_smr_ai_power", "Stage2_MOU_supply_chain", "2025-08-26", "KHNP/Doosan cooperate with X-energy/AWS; Doosan agreement with Fermi America for Texas AI project SMR equipment.", "price_data_unavailable_after_deep_search", "MOU_not_final_contract", "Stage2", {"counterparties": ["KHNP", "X-energy", "Amazon_Web_Services", "Fermi_America"]}),
    Round322TriggerRecord("r1l17_samsung_heavy_zvezda_T1", "r1_loop17_samsung_heavy_zvezda_cancellation", "4C_order_cancellation", "2025-06-18", "Samsung Heavy cancels 4.85T won / $3.54B Zvezda icebreaker orders and pursues arbitration/damages.", "price_data_unavailable_after_deep_search", "order_cancellation_4C", "4C-watch", {"cancelled_order_value_krw_trn": 4.85, "cancelled_order_value_usd_bn": 3.54}),
)

ROUND322_SHADOW_WEIGHT_ROWS: tuple[dict[str, str], ...] = (
    {"archetype": E2RArchetype.SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE.value, "reported_event_return": "+5", "market_relative_return": "+4", "contract_value_visibility": "+3", "naval_shipbuilding_us_workshare": "+5", "grid_equipment_backlog": "+0", "capacity_utilization": "+3", "repeat_export_operator": "+2", "order_quality_risk": "+3", "theme_label_without_orders_penalty": "-2", "report_upgrade_without_price_validation_penalty": "-1", "capacity_headline_without_utilization_penalty": "-2", "mou_without_final_contract_penalty": "-1", "stage2_actionable_promote": "shipbuilding merger+MASGA event", "stage3_yellow_gate": "actual US orders/workshare missing", "stage3_green_gate": "US order+post-merger margin", "notes": "HD Hyundai Heavy/Mipo."},
    {"archetype": E2RArchetype.SHIPBUILDING_NAVAL_EXPORT_STAGE2_WITH_SANCTION_4B.value, "reported_event_return": "+4", "market_relative_return": "+2", "contract_value_visibility": "+3", "naval_shipbuilding_us_workshare": "+5", "grid_equipment_backlog": "+0", "capacity_utilization": "+2", "repeat_export_operator": "+3", "order_quality_risk": "+5", "theme_label_without_orders_penalty": "-2", "report_upgrade_without_price_validation_penalty": "-1", "capacity_headline_without_utilization_penalty": "-1", "mou_without_final_contract_penalty": "-1", "stage2_actionable_promote": "US Navy optionality", "stage3_yellow_gate": "China sanction 4B", "stage3_green_gate": "formal contract+sanction resolution", "notes": "Hanwha Ocean."},
    {"archetype": E2RArchetype.DEFENSE_INDUSTRIAL_EXPORT_STAGE2_YELLOW.value, "reported_event_return": "+5", "market_relative_return": "+5", "contract_value_visibility": "+5", "naval_shipbuilding_us_workshare": "+0", "grid_equipment_backlog": "+0", "capacity_utilization": "+3", "repeat_export_operator": "+5", "order_quality_risk": "+2", "theme_label_without_orders_penalty": "-1", "report_upgrade_without_price_validation_penalty": "-1", "capacity_headline_without_utilization_penalty": "-2", "mou_without_final_contract_penalty": "-1", "stage2_actionable_promote": "repeat K2 export", "stage3_yellow_gate": "local production margin gate", "stage3_green_gate": "delivery+margin+local production", "notes": "Hyundai Rotem."},
    {"archetype": E2RArchetype.GRID_EQUIPMENT_AI_POWER_STAGE2_PROMOTE.value, "reported_event_return": "+4", "market_relative_return": "+3", "contract_value_visibility": "+2", "naval_shipbuilding_us_workshare": "+0", "grid_equipment_backlog": "+5", "capacity_utilization": "+5", "repeat_export_operator": "+1", "order_quality_risk": "+2", "theme_label_without_orders_penalty": "-4", "report_upgrade_without_price_validation_penalty": "-2", "capacity_headline_without_utilization_penalty": "-4", "mou_without_final_contract_penalty": "-1", "stage2_actionable_promote": "broad AI power rally", "stage3_yellow_gate": "backlog/margin missing", "stage3_green_gate": "orders+ASP+margin", "notes": "HD Hyundai Electric."},
    {"archetype": E2RArchetype.GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED.value, "reported_event_return": "+0", "market_relative_return": "-5", "contract_value_visibility": "+1", "naval_shipbuilding_us_workshare": "+0", "grid_equipment_backlog": "+4", "capacity_utilization": "+3", "repeat_export_operator": "+0", "order_quality_risk": "+2", "theme_label_without_orders_penalty": "-4", "report_upgrade_without_price_validation_penalty": "-5", "capacity_headline_without_utilization_penalty": "-3", "mou_without_final_contract_penalty": "-1", "stage2_actionable_promote": "good US data center report but price failed", "stage3_yellow_gate": "actionable prohibited", "stage3_green_gate": "actual orders+margin", "notes": "LS Electric."},
    {"archetype": E2RArchetype.TRANSFORMER_CAPACITY_EXPANSION_STAGE2_NO_PRICE.value, "reported_event_return": "+1", "market_relative_return": "+0", "contract_value_visibility": "+1", "naval_shipbuilding_us_workshare": "+0", "grid_equipment_backlog": "+5", "capacity_utilization": "+5", "repeat_export_operator": "+0", "order_quality_risk": "+2", "theme_label_without_orders_penalty": "-3", "report_upgrade_without_price_validation_penalty": "-1", "capacity_headline_without_utilization_penalty": "-4", "mou_without_final_contract_penalty": "-1", "stage2_actionable_promote": "US transformer shortage and capacity expansion", "stage3_yellow_gate": "KRX price/orderbook missing", "stage3_green_gate": "utilization+orderbook+margin", "notes": "Hyosung Heavy."},
    {"archetype": E2RArchetype.NUCLEAR_SMR_INDUSTRIAL_SUPPLY_STAGE2_WITH_FINAL_CONTRACT_GATE.value, "reported_event_return": "+1", "market_relative_return": "+0", "contract_value_visibility": "+2", "naval_shipbuilding_us_workshare": "+0", "grid_equipment_backlog": "+1", "capacity_utilization": "+3", "repeat_export_operator": "+0", "order_quality_risk": "+3", "theme_label_without_orders_penalty": "-3", "report_upgrade_without_price_validation_penalty": "-1", "capacity_headline_without_utilization_penalty": "-2", "mou_without_final_contract_penalty": "-5", "stage2_actionable_promote": "SMR/AI power cooperation", "stage3_yellow_gate": "final contract missing", "stage3_green_gate": "equipment order+workshare+margin", "notes": "Doosan Enerbility."},
    {"archetype": E2RArchetype.SHIPBUILDING_ORDER_CANCELLATION_4C.value, "reported_event_return": "-5", "market_relative_return": "-3", "contract_value_visibility": "-5", "naval_shipbuilding_us_workshare": "+0", "grid_equipment_backlog": "+0", "capacity_utilization": "+0", "repeat_export_operator": "+0", "order_quality_risk": "+5", "theme_label_without_orders_penalty": "-1", "report_upgrade_without_price_validation_penalty": "-1", "capacity_headline_without_utilization_penalty": "-1", "mou_without_final_contract_penalty": "-1", "stage2_actionable_promote": "major order cancellation", "stage3_yellow_gate": "backlog quality impaired", "stage3_green_gate": "damages recovery+replacement orders", "notes": "Samsung Heavy."},
)


def round322_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND322_CASE_CANDIDATES]


def round322_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND322_CASE_CANDIDATES]


def round322_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND322_TRIGGER_RECORDS]


def round322_shadow_weight_rows() -> list[dict[str, str]]:
    return [dict(row) for row in ROUND322_SHADOW_WEIGHT_ROWS]


def round322_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND322_REQUIRED_TARGET_ALIASES.items()]


def round322_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND322_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND322_SCORE_DOWN_AXES]
    )


def round322_summary() -> dict[str, object]:
    return {
        "source_round": ROUND322_SOURCE_ROUND_PATH,
        "round_id": ROUND322_ANALYST_ROUND_ID,
        "loop_name": ROUND322_LOOP_NAME,
        "large_sector": ROUND322_LARGE_SECTOR,
        "method": ROUND322_METHOD,
        "case_candidate_count": len(ROUND322_CASE_CANDIDATES),
        "trigger_count": len(ROUND322_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND322_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 3,
        "stage2_candidate_count": 7,
        "stage2_promote_candidate_count": 1,
        "stage3_yellow_candidate_count": 4,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 7,
        "stage4c_watch_count": 2,
        "strong_4c_case_count": 1,
        "evidence_good_but_price_failed_count": 1,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R2 Loop 17",
    }


def round322_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND322_SOURCE_ROUND_PATH,
        "round_id": ROUND322_ANALYST_ROUND_ID,
        "loop_name": ROUND322_LOOP_NAME,
        "large_sector": ROUND322_LARGE_SECTOR,
        "method": ROUND322_METHOD,
        "summary": round322_summary(),
        "required_target_aliases": dict(ROUND322_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND322_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND322_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND322_STAGE3_GREEN_RULES,
        "green_blockers": ROUND322_GREEN_BLOCKERS,
        "score_up_axes": ROUND322_SCORE_UP_AXES,
        "score_down_axes": ROUND322_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND322_STAGE4B_WATCH_TRIGGERS,
        "hard_4c_gates": ROUND322_HARD_4C_GATES,
        "row_separation_rules": ROUND322_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round322_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
            "do_not_treat_MASGA_AI_power_SMR_or_target_price_headline_as_Green_without_margin_capacity_finality_or_price_validation",
        ),
    }


def render_round322_summary_markdown() -> str:
    summary = round322_summary()
    lines = [
        "# R1 Loop 17 Industrials / Orders / Infrastructure Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: a shipbuilding merger can be Stage2-Actionable when price reacts strongly, but it is not Green until actual orders, workshare, margin and legal gates close.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- HD Hyundai Heavy / Mipo is the cleanest Stage2-Actionable anchor, but U.S. order/workshare and post-merger margin are still gates.",
            "- Hanwha Ocean is Stage2 naval optionality with China sanction 4B.",
            "- Hyundai Rotem is a Stage3-Yellow candidate because repeat K2 export and local production are visible, but margin and delivery remain gates.",
            "- HD Hyundai Electric is a Stage2 promote / missed-structural risk if AI power-equipment demand is ignored.",
            "- LS Electric is evidence-good but price-failed.",
            "- Hyosung Heavy is transformer capacity Stage2 without direct price/orderbook validation.",
            "- Doosan Enerbility is SMR/AI-power Stage2, not Green before final equipment contract and workshare.",
            "- Samsung Heavy Zvezda cancellation is the strong 4C backlog-quality break.",
            "- Stage3-Green confirmed: `0`.",
            "- Strong 4C case count: `1`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round322_trigger_grid_markdown() -> str:
    lines = [
        "# Round 322 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round322_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round322_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 322 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND322_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND322_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND322_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND322_GREEN_BLOCKERS),
            "",
            "## Hard 4C Gates",
            *_bullet_lines(ROUND322_HARD_4C_GATES),
        ]
    ) + "\n"


def render_round322_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 322 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND322_STAGE4B_WATCH_TRIGGERS),
        "",
        "## Hard 4C Gates",
        *_bullet_lines(ROUND322_HARD_4C_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND322_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round322_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 322 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event returns and event prices are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND322_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round322_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 322 Row Separation Plan",
        "",
        "Industrial order rows must separate case evidence, trigger anchors and full adjusted OHLC backfill.",
        "",
        "Easy example: Hyosung HICO's $157M transformer expansion is Stage2 evidence, but without orderbook, utilization, margin and price data it cannot become Green.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND322_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round322_r1_loop17_reports(
    output_directory: str | Path = ROUND322_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND322_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND322_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND322_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND322_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round322_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND322_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round322_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round322_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round322_r1_loop17_case_matrix.csv",
        "target_aliases": output_dir / "round322_r1_loop17_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round322_r1_loop17_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round322_r1_loop17_trigger_grid.md",
        "summary": output_dir / "round322_r1_loop17_trigger_validation_summary.md",
        "stage_rules": output_dir / "round322_r1_loop17_stage_rules.md",
        "stage4b_4c_review": output_dir / "round322_r1_loop17_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round322_r1_loop17_score_adjustments.csv",
        "shadow_weights": output_dir / "round322_r1_loop17_shadow_weights.csv",
        "price_validation_plan": output_dir / "round322_r1_loop17_price_validation_plan.md",
        "row_separation_plan": output_dir / "round322_r1_loop17_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round322_case_rows())
    _write_csv(paths["target_aliases"], round322_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round322_trigger_rows())
    _write_csv(paths["score_adjustments"], round322_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round322_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round322_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round322_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round322_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round322_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round322_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round322_row_separation_plan_markdown(), encoding="utf-8")
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
    "ROUND322_CASE_CANDIDATES",
    "ROUND322_GREEN_BLOCKERS",
    "ROUND322_HARD_4C_GATES",
    "ROUND322_LARGE_SECTOR",
    "ROUND322_REQUIRED_TARGET_ALIASES",
    "ROUND322_ROW_SEPARATION_RULES",
    "ROUND322_SCORE_DOWN_AXES",
    "ROUND322_SCORE_UP_AXES",
    "ROUND322_SHADOW_WEIGHT_ROWS",
    "ROUND322_STAGE2_ACTIONABLE_RULES",
    "ROUND322_STAGE3_GREEN_RULES",
    "ROUND322_STAGE3_YELLOW_RULES",
    "ROUND322_STAGE4B_WATCH_TRIGGERS",
    "ROUND322_TRIGGER_RECORDS",
    "render_round322_stage4b_4c_review_markdown",
    "render_round322_stage_rules_markdown",
    "render_round322_trigger_grid_markdown",
    "round322_audit_payload",
    "round322_case_records",
    "round322_case_rows",
    "round322_shadow_weight_rows",
    "round322_summary",
    "round322_trigger_rows",
    "write_round322_r1_loop17_reports",
]
