"""Round-328 R7 Loop-17 bio/healthcare/medical-device trigger validation.

This module converts ``docs/round/round_328.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a CDMO facility acquisition can be Stage2 if deal value,
capacity and tariff-hedge logic are explicit. It still cannot become Green
until utilization, customer transfer, margin and FCF evidence appear.
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


ROUND328_SOURCE_ROUND_PATH = "docs/round/round_328.md"
ROUND328_ANALYST_ROUND_ID = "round_256"
ROUND328_LOOP_NAME = "R7 Loop 17"
ROUND328_LARGE_SECTOR = "BIO_HEALTHCARE_MEDICAL_DEVICE"
ROUND328_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND328_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round328_r7_loop17_bio_healthcare_device_trigger_validation"
ROUND328_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_loop17_round256.jsonl"
ROUND328_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r7_loop17_round256.jsonl"
ROUND328_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round328_r7_loop17_bio_healthcare_device_trigger_validation_audit.json"
ROUND328_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round256_r7_loop17_v1.csv"

ROUND328_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BIOPHARMA_POLICY_SUPPORT_STAGE2_ACTIONABLE": E2RArchetype.BIOPHARMA_POLICY_SUPPORT_STAGE2_ACTIONABLE.value,
    "CDMO_US_FACILITY_TARIFF_HEDGE_STAGE2_PRICE_FAILED": E2RArchetype.CDMO_US_FACILITY_TARIFF_HEDGE_STAGE2_PRICE_FAILED.value,
    "VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE": E2RArchetype.VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE.value,
    "BIOSIMILAR_US_LOCALIZATION_STAGE2_NO_PRICE": E2RArchetype.BIOSIMILAR_US_LOCALIZATION_STAGE2_NO_PRICE.value,
    "PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW": E2RArchetype.PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW.value,
    "AESTHETIC_TOXIN_US_FDA_STAGE2": E2RArchetype.AESTHETIC_TOXIN_US_FDA_STAGE2.value,
    "MEDICAL_AESTHETIC_DEVICE_MA_STAGE2": E2RArchetype.MEDICAL_AESTHETIC_DEVICE_MA_STAGE2.value,
    "BIOSIMILAR_PATENT_LITIGATION_4B": E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4B.value,
}

ROUND328_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_at_least_5pct_or_clear_relative_outperformance",
    "deal_approval_facility_capacity_or_product_launch_is_explicit",
    "customer_product_facility_or_indication_is_specific",
    "revenue_path_exists_through_CDMO_utilization_royalty_launch_sales_or_reimbursement",
    "patent_litigation_tariff_manufacturing_inspection_or_integration_4B_is_identified",
    "price_reaction_validates_the_evidence_when_available",
    "approval_or_MA_can_move_to_commercial_execution",
)

ROUND328_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "CDMO_utilization_orderbook_or_customer_transfer_confirms",
    "FDA_or_EMA_approval_converts_to_commercial_launch",
    "royalty_product_supply_or_reimbursement_revenue_visibility_exists",
    "patent_litigation_risk_is_contained",
    "payer_physician_or_channel_adoption_is_visible",
    "US_tariff_hedge_converts_to_margin_or_volume_benefit",
    "facility_acquisition_integration_is_on_schedule",
)

ROUND328_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "approval_or_facility_acquisition_converts_into_recurring_revenue",
    "CDMO_utilization_and_margin_are_visible",
    "platform_royalty_or_supply_economics_are_disclosed_or_inferable",
    "patent_litigation_and_manufacturing_inspection_risks_are_contained",
    "launch_sellthrough_and_reimbursement_are_confirmed",
    "full_window_MFE_MAE_is_available_and_supportive",
)

ROUND328_GREEN_BLOCKERS: tuple[str, ...] = (
    "facility_acquisition_without_utilization",
    "policy_support_without_company_specific_contract",
    "FDA_approval_without_sellthrough",
    "platform_link_without_royalty_visibility",
    "MA_reference_without_public_liquidity",
    "biosimilar_opportunity_without_patent_clearance",
    "hard_4C_without_sourced_price_anchor",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND328_SCORE_UP_AXES: tuple[str, ...] = (
    "manufacturing_asset_MA",
    "biopharma_policy_support",
    "US_localization_tariff_hedge",
    "blockbuster_platform_linkage",
    "FDA_approval_commercial_launch",
    "medical_device_MA_valuation",
    "patent_litigation_risk",
    "utilization_margin_conversion",
)

ROUND328_SCORE_DOWN_AXES: tuple[str, ...] = (
    "facility_acquisition_without_price_validation",
    "policy_support_without_company_contract",
    "FDA_approval_without_sellthrough",
    "platform_link_without_royalty_visibility",
    "MA_reference_without_public_liquidity",
    "biosimilar_opportunity_without_patent_clearance",
    "CDMO_capacity_without_utilization",
    "hard_4C_without_sourced_price_anchor",
)

ROUND328_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "FDA_approval_without_launch_sellthrough",
    "CDMO_facility_acquisition_without_utilization",
    "policy_support_without_company_specific_contract",
    "platform_link_without_royalty_economics",
    "patent_litigation_around_biosimilar_or_enzyme_platform",
    "US_pharma_tariff_policy_uncertainty",
    "medical_device_MA_delisting_or_liquidity_exit",
    "FDA_inspection_or_manufacturing_CMC_issue",
)

ROUND328_HARD_4C_GATES: tuple[str, ...] = (
    "FDA_CRL_or_approval_rejection_with_sourced_stock_crash",
    "pivotal_trial_failure",
    "manufacturing_inspection_failure_preventing_launch",
    "patent_ruling_permanently_blocking_product",
    "safety_signal_causing_withdrawal",
    "reimbursement_denial_destroying_commercial_case",
)

ROUND328_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_reported_event_return_deal_approval_facility_or_litigation_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
    "do_not_treat_policy_facility_FDA_or_patent_headline_as_Green_without_revenue_utilization_royalty_sellthrough_or_risk_closure",
)


@dataclass(frozen=True)
class Round328TriggerRecord:
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
class Round328ShadowWeightRow:
    archetype: E2RArchetype
    manufacturing_asset_ma: int
    biopharma_policy_support: int
    us_localization_tariff_hedge: int
    blockbuster_platform_linkage: int
    fda_approval_commercial_launch: int
    medical_device_ma_valuation: int
    patent_litigation_risk: int
    utilization_margin_conversion: int
    facility_acquisition_without_price_validation_penalty: int
    policy_support_without_company_contract_penalty: int
    fda_approval_without_sellthrough_penalty: int
    platform_link_without_royalty_visibility_penalty: int
    ma_reference_without_public_liquidity_penalty: int
    biosimilar_opportunity_without_patent_clearance_penalty: int
    cdmo_capacity_without_utilization_penalty: int
    hard_4c_without_sourced_price_anchor_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "manufacturing_asset_MA": _signed(self.manufacturing_asset_ma),
            "biopharma_policy_support": _signed(self.biopharma_policy_support),
            "US_localization_tariff_hedge": _signed(self.us_localization_tariff_hedge),
            "blockbuster_platform_linkage": _signed(self.blockbuster_platform_linkage),
            "FDA_approval_commercial_launch": _signed(self.fda_approval_commercial_launch),
            "medical_device_MA_valuation": _signed(self.medical_device_ma_valuation),
            "patent_litigation_risk": _signed(self.patent_litigation_risk),
            "utilization_margin_conversion": _signed(self.utilization_margin_conversion),
            "facility_acquisition_without_price_validation_penalty": _signed(self.facility_acquisition_without_price_validation_penalty),
            "policy_support_without_company_contract_penalty": _signed(self.policy_support_without_company_contract_penalty),
            "FDA_approval_without_sellthrough_penalty": _signed(self.fda_approval_without_sellthrough_penalty),
            "platform_link_without_royalty_visibility_penalty": _signed(self.platform_link_without_royalty_visibility_penalty),
            "MA_reference_without_public_liquidity_penalty": _signed(self.ma_reference_without_public_liquidity_penalty),
            "biosimilar_opportunity_without_patent_clearance_penalty": _signed(self.biosimilar_opportunity_without_patent_clearance_penalty),
            "CDMO_capacity_without_utilization_penalty": _signed(self.cdmo_capacity_without_utilization_penalty),
            "hard_4C_without_sourced_price_anchor_penalty": _signed(self.hard_4c_without_sourced_price_anchor_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round328CaseCandidate:
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
            "do_not_use_round328_cases_as_candidate_generation_input",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_policy_facility_FDA_or_patent_headline_as_Green_without_revenue_utilization_royalty_sellthrough_or_risk_closure",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")

        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "patent" in field
            or "tariff" in field
            or "FDA" in field
            or "inspection" in field
            or "sellthrough" in field
            or "utilization" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field or "4c" in field or "hard" in field or "CRL" in field or "withdrawal" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND328_LARGE_SECTOR,
            large_sector=ROUND328_LARGE_SECTOR,
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
            must_have_fields=ROUND328_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.case_type in {"event_premium", "4b_watch", "overheat", "failed_rerating"} else None,
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
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND328_CASE_CANDIDATES: tuple[Round328CaseCandidate, ...] = (
    Round328CaseCandidate(
        "r7_loop17_sk_bioscience_idt_biologika",
        "302440",
        "SK Bioscience",
        E2RArchetype.VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE,
        (E2RArchetype.VACCINE_CDMO_MA_STAGE2_ACTIONABLE, E2RArchetype.CMO_M_AND_A_TRANSITION),
        "success_candidate",
        "Stage2_Actionable_vaccine_CDMO_cross_border_MA",
        "T2",
        "Stage2-Actionable_CDMO_MA",
        "Stage2-Actionable",
        date(2024, 6, 27),
        date(2024, 6, 27),
        None,
        date(2024, 6, 27),
        None,
        False,
        ("IDT_Biologika_60pct_stake", "deal_value_krw_339B", "deal_value_usd_243_75M", "event_return_plus_11_7pct", "European_CDMO_asset", "integration_path"),
        ("integration_cost_4B", "European_cost_base_4B", "utilization_4B", "orderbook_visibility_4B", "MA_ROI_4B"),
        {"trigger_date": "2024-06-27", "stake_pct": 60, "deal_value_krw_bn": 339, "deal_value_usd_mn": 243.75, "event_return_pct": 11.7},
        "aligned",
        "excellent_stage2_actionable_CDMO_MA",
        "event_premium",
        "stage2_watch_success",
        "Majority CDMO acquisition and +11.7% event reaction support Stage2-Actionable; utilization and orderbook are still required before Yellow or Green.",
    ),
    Round328CaseCandidate(
        "r7_loop17_samsung_biologics_policy_support",
        "207940",
        "Samsung Biologics",
        E2RArchetype.BIOPHARMA_POLICY_SUPPORT_STAGE2_ACTIONABLE,
        (E2RArchetype.BIOPHARMA_POLICY_TARIFF_RELIEF, E2RArchetype.BIOPHARMA_TARIFF_POLICY_SUPPORT_STAGE2),
        "success_candidate",
        "Stage2_Actionable_biopharma_policy_support",
        "T2",
        "Stage2-Actionable_policy_support",
        "Stage2-Actionable",
        date(2025, 5, 21),
        date(2025, 5, 21),
        None,
        date(2025, 5, 21),
        None,
        False,
        ("Samsung_Biologics_plus_6_23pct", "pharma_sector_plus_3_97pct", "KOSPI_plus_0_99pct", "market_relative_plus_5_24pp", "pharma_exports_usd_9_59B", "US_export_share_16pct"),
        ("tariff_detail_uncertainty_4B", "FDA_inspection_4B", "policy_terms_unclear_4B", "company_specific_contract_not_confirmed_4B"),
        {"trigger_date": "2025-05-21", "samsung_biologics_event_return_pct": 6.23, "pharma_sector_event_return_pct": 3.97, "kospi_event_return_pct": 0.99, "market_relative_outperformance_pp": 5.24, "pharma_exports_usd_bn": 9.59, "us_export_share_pct": 16},
        "aligned",
        "good_stage2_policy_support_not_green",
        "policy_event_rerating",
        "stage2_watch_success",
        "Policy support and market-relative reaction are clear, but company-specific contract and tariff margin bridge are not yet proven.",
    ),
    Round328CaseCandidate(
        "r7_loop17_samsung_biologics_gsk_us_facility",
        "207940",
        "Samsung Biologics",
        E2RArchetype.CDMO_US_FACILITY_TARIFF_HEDGE_STAGE2_PRICE_FAILED,
        (E2RArchetype.CDMO_US_FACILITY_EXPANSION_STAGE2_PRICE_MUTED, E2RArchetype.BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE),
        "success_candidate",
        "Stage2_CDMO_US_facility_evidence_good_price_failed",
        "T2/T3",
        "Stage2_price_failed",
        "Stage2",
        date(2025, 12, 22),
        date(2025, 12, 22),
        None,
        date(2025, 12, 22),
        None,
        False,
        ("GSK_US_facility_deal_usd_280M", "facility_capacity_60000L", "US_local_manufacturing", "tariff_hedge", "long_term_US_demand", "CDMO_footprint_expansion"),
        ("capex_upgrade_cost_4B", "utilization_ramp_4B", "closing_value_adjustment_4B", "customer_transfer_4B", "tariff_benefit_uncertain_4B"),
        {"trigger_date": "2025-12-22", "deal_value_usd_mn": 280, "capacity_liters": 60000, "samsung_bio_event_return_pct": -0.4, "broader_market_event_return_pct": 2.0, "relative_event_return_pp": -2.4},
        "evidence_good_but_price_failed",
        "evidence_good_but_price_failed",
        "unknown",
        "stage2_watch_success",
        "The facility expands U.S. CDMO optionality, but the reported -2.4pp relative price reaction blocks validation.",
    ),
    Round328CaseCandidate(
        "r7_loop17_celltrion_us_factory_localization",
        "068270",
        "Celltrion",
        E2RArchetype.BIOSIMILAR_US_LOCALIZATION_STAGE2_NO_PRICE,
        (E2RArchetype.BIOSIMILAR_US_TARIFF_HEDGE_STAGE2, E2RArchetype.BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE),
        "success_candidate",
        "Stage2_US_factory_tariff_hedge_no_price",
        "T2",
        "Stage2_no_price",
        "Stage2",
        date(2025, 7, 29),
        date(2025, 7, 29),
        None,
        date(2025, 7, 29),
        None,
        False,
        ("preferred_bidder_US_factory", "planned_initial_investment_krw_700B", "ImClone_acquisition_usd_330M", "additional_expansion_krw_700B", "tariff_hedge", "biosimilar_US_localization"),
        ("facility_upgrade_cost_4B", "rebate_pressure_4B", "tariff_uncertainty_4B", "utilization_ramp_4B", "capital_intensity_4B"),
        {"preferred_bidder_date": "2025-07-29", "planned_initial_investment_krw_bn": 700, "imclone_acquisition_usd_mn": 330, "additional_expansion_krw_bn": 700, "direct_price_anchor": None},
        "unknown",
        "Stage2_US_localization_no_price",
        "unknown",
        "stage2_watch_success",
        "U.S. localization can protect biosimilar economics, but no direct price anchor and no utilization proof keep it Stage2.",
    ),
    Round328CaseCandidate(
        "r7_loop17_alteogen_keytruda_sc",
        "196170",
        "Alteogen",
        E2RArchetype.PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW,
        (E2RArchetype.SC_FORMULATION_PLATFORM_STAGE3_YELLOW, E2RArchetype.BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE),
        "success_candidate",
        "Stage3_Yellow_candidate_platform_enzyme_blockbuster",
        "T3",
        "Stage3-Yellow_candidate",
        "Stage3-Yellow candidate",
        date(2024, 11, 19),
        date(2024, 11, 19),
        date(2025, 3, 27),
        date(2025, 3, 27),
        None,
        False,
        ("Keytruda_SC_clinical_trigger", "planned_US_launch_2025_10_01", "FDA_target_action_date_2025_09_23", "Keytruda_2024_sales_nearly_usd_30B", "expected_peak_adoption_30_40pct", "SC_2min_vs_IV_30min"),
        ("Halozyme_patent_dispute_4B", "FDA_approval_timing_4B", "royalty_visibility_4B", "commercial_conversion_4B", "launch_execution_4B"),
        {"clinical_trigger_date": "2024-11-19", "launch_plan_date": "2025-03-27", "planned_us_launch_date": "2025-10-01", "fda_target_action_date": "2025-09-23", "keytruda_2024_sales_usd_bn": 30, "expected_peak_adoption_pct": "30-40", "sc_minutes": 2, "iv_minutes": 30},
        "unknown",
        "Stage3_Yellow_candidate_not_Green",
        "unknown",
        "yellow_success",
        "Blockbuster SC platform linkage is strong enough for Yellow candidate review, but royalty economics and patent containment are still required for Green.",
    ),
    Round328CaseCandidate(
        "r7_loop17_hugel_letybo_us_fda",
        "145020",
        "Hugel",
        E2RArchetype.AESTHETIC_TOXIN_US_FDA_STAGE2,
        (E2RArchetype.AESTHETIC_TOXIN_US_LAUNCH_STAGE2, E2RArchetype.BOTULINUM_US_MARKET_ENTRY),
        "success_candidate",
        "Stage2_aesthetic_toxin_US_FDA_commercial_launch",
        "T2",
        "Stage2_FDA_launch_no_price",
        "Stage2",
        date(2025, 3, 1),
        date(2025, 3, 1),
        None,
        date(2025, 3, 1),
        None,
        False,
        ("US_FDA_approval_glabellar_lines", "US_commercial_rollout_from_March_2025", "Letybo_unit_price_usd_9_to_12", "Botox_unit_price_usd_12_to_18", "dermatology_office_channel"),
        ("US_channel_execution_4B", "physician_adoption_4B", "price_competition_4B", "toxin_safety_perception_4B", "repeat_treatment_durability_4B"),
        {"commercial_rollout_date": "2025-03", "letybo_unit_price_usd": "9-12", "botox_unit_price_usd": "12-18", "direct_price_anchor": None},
        "unknown",
        "Stage2_FDA_launch_no_price",
        "unknown",
        "stage2_watch_success",
        "FDA approval and U.S. launch path are real, but physician adoption and sell-through must validate recurring revenue.",
    ),
    Round328CaseCandidate(
        "r7_loop17_jeisys_archimed_medical_aesthetic_ma",
        "287410",
        "Jeisys Medical",
        E2RArchetype.MEDICAL_AESTHETIC_DEVICE_MA_STAGE2,
        (E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_BUYOUT_STAGE2, E2RArchetype.AESTHETIC_DEVICE_MA_CONTROL_PREMIUM),
        "event_premium",
        "Stage2_medical_aesthetic_device_MA_reference",
        "T2",
        "Stage2_reference",
        "Stage2 reference",
        date(2024, 9, 11),
        date(2024, 9, 11),
        None,
        date(2024, 9, 11),
        None,
        False,
        ("Archimed_deal_value_usd_742M", "reported_close_price_krw_12860", "price_little_changed", "energy_based_devices", "radio_wave_ultrasound_laser"),
        ("delisting_process_4B", "liquidity_exit_4B", "tender_already_priced_4B", "peer_readthrough_uncertain_4B"),
        {"trigger_date": "2024-09-11", "deal_value_usd_mn": 742, "reported_close_price_krw": 12860, "event_reaction_context": "little_changed"},
        "price_moved_without_evidence",
        "MA_valuation_reference_not_actionable",
        "event_premium",
        "stage2_watch_success",
        "The takeout validates device valuation context, but delisting and liquidity exit make it a reference, not an operating Green case.",
    ),
    Round328CaseCandidate(
        "r7_loop17_samsung_bioepis_amgen_patent_litigation",
        "207940_readthrough",
        "Samsung Bioepis / Samsung Biologics read-through",
        E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4B,
        (E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH, E2RArchetype.PATENT_CHALLENGE_OVERLAY),
        "4b_watch",
        "4B_biosimilar_patent_litigation_not_4C",
        "T1",
        "4B-watch",
        "4B-watch",
        date(2024, 8, 13),
        None,
        None,
        date(2024, 8, 13),
        None,
        False,
        ("Amgen_plaintiff", "Samsung_Bioepis_defendant", "Prolia_Xgeva_biosimilars", "alleged_34_patents", "Prolia_prior_year_US_sales_usd_2_7B", "Xgeva_prior_year_US_sales_usd_1_5B"),
        ("patent_litigation_4B", "launch_delay_4B", "settlement_cost_4B", "rebate_pressure_4B", "FDA_commercial_timing_4B"),
        {"trigger_date": "2024-08-13", "asserted_patents": 34, "prolia_prior_year_us_sales_usd_bn": 2.7, "xgeva_prior_year_us_sales_usd_bn": 1.5, "direct_price_anchor": None, "hard_4c_status": "not_confirmed"},
        "aligned",
        "biosimilar_patent_litigation_4B_not_4C",
        "no_rerating",
        "should_have_been_red",
        "Patent litigation is a 4B risk overlay. It is not hard 4C without a sourced ruling, injunction or price anchor.",
    ),
)

ROUND328_TRIGGER_RECORDS: tuple[Round328TriggerRecord, ...] = (
    Round328TriggerRecord("r7l17_sk_bioscience_idt_T2", "r7_loop17_sk_bioscience_idt_biologika", "Stage2-Actionable_CDMO_MA", "2024-06-27", "reported_event_anchor", 11.7, "excellent_stage2_actionable_CDMO_MA", "Stage2-Actionable", {"stake_pct": 60, "deal_value_krw_bn": 339, "deal_value_usd_mn": 243.75}),
    Round328TriggerRecord("r7l17_samsung_bio_policy_T2", "r7_loop17_samsung_biologics_policy_support", "Stage2-Actionable_policy_support", "2025-05-21", "reported_event_anchor", 6.23, "good_stage2_policy_support_not_green", "Stage2-Actionable", {"pharma_sector_event_return_pct": 3.97, "market_relative_outperformance_pp": 5.24}),
    Round328TriggerRecord("r7l17_samsung_bio_gsk_T2", "r7_loop17_samsung_biologics_gsk_us_facility", "Stage2_CDMO_US_facility_price_failed", "2025-12-22", "reported_event_anchor", -0.4, "evidence_good_but_price_failed", "Stage2", {"deal_value_usd_mn": 280, "capacity_liters": 60000, "relative_event_return_pp": -2.4}),
    Round328TriggerRecord("r7l17_celltrion_us_factory_T2", "r7_loop17_celltrion_us_factory_localization", "Stage2_US_localization_no_price", "2025-07-29", "reported_event_anchor", "price_data_unavailable_after_deep_search", "Stage2_US_localization_no_price", "Stage2", {"planned_initial_investment_krw_bn": 700, "imclone_acquisition_usd_mn": 330}),
    Round328TriggerRecord("r7l17_alteogen_keytruda_T3", "r7_loop17_alteogen_keytruda_sc", "Stage3-Yellow_platform_enzyme_blockbuster", "2025-03-27", "reported_event_anchor", "price_data_unavailable_after_deep_search", "Stage3_Yellow_candidate_not_Green", "Stage3-Yellow", {"keytruda_2024_sales_usd_bn": 30, "expected_peak_adoption_pct": "30-40"}),
    Round328TriggerRecord("r7l17_hugel_letybo_T2", "r7_loop17_hugel_letybo_us_fda", "Stage2_aesthetic_toxin_US_FDA", "2025-03", "reported_event_anchor", "price_data_unavailable_after_deep_search", "Stage2_FDA_launch_no_price", "Stage2", {"letybo_unit_price_usd": "9-12", "botox_unit_price_usd": "12-18"}),
    Round328TriggerRecord("r7l17_jeisys_archimed_T2", "r7_loop17_jeisys_archimed_medical_aesthetic_ma", "Stage2_medical_aesthetic_device_MA_reference", "2024-09-11", "reported_event_anchor", "little_changed", "MA_valuation_reference_not_actionable", "Stage2 reference", {"deal_value_usd_mn": 742, "reported_close_price_krw": 12860}),
    Round328TriggerRecord("r7l17_bioepis_patent_T1", "r7_loop17_samsung_bioepis_amgen_patent_litigation", "4B_biosimilar_patent_litigation", "2024-08-13", "reported_event_anchor", "price_data_unavailable_after_deep_search", "biosimilar_patent_litigation_4B_not_4C", "4B-watch", {"asserted_patents": 34, "prolia_us_sales_usd_bn": 2.7, "xgeva_us_sales_usd_bn": 1.5}),
)

ROUND328_SHADOW_WEIGHT_ROWS: tuple[Round328ShadowWeightRow, ...] = (
    Round328ShadowWeightRow(E2RArchetype.VACCINE_CDMO_CROSS_BORDER_MA_STAGE2_ACTIONABLE, 5, 0, 0, 0, 0, 0, 1, 5, -2, -1, -1, -1, -1, -1, -5, -5, "IDT 60% stake +11.7%", "orderbook/utilization/margin", "recurring CDMO revenue and FCF", "SK Bioscience"),
    Round328ShadowWeightRow(E2RArchetype.BIOPHARMA_POLICY_SUPPORT_STAGE2_ACTIONABLE, 0, 4, 2, 0, 0, 0, 1, 2, -1, -4, -1, -1, -1, -1, -2, -5, "policy + market-relative rally", "company-specific contract", "policy benefit converts to margin", "Samsung Biologics policy"),
    Round328ShadowWeightRow(E2RArchetype.CDMO_US_FACILITY_TARIFF_HEDGE_STAGE2_PRICE_FAILED, 5, 0, 4, 0, 0, 0, 1, 5, -5, -1, -1, -1, -1, -1, -5, -5, "U.S. facility but price failed", "customer transfer/utilization", "margin and tariff savings", "Samsung Bio GSK"),
    Round328ShadowWeightRow(E2RArchetype.BIOSIMILAR_US_LOCALIZATION_STAGE2_NO_PRICE, 4, 0, 4, 0, 0, 0, 3, 4, -5, -1, -1, -1, -1, -5, -5, -5, "factory localization no price", "product transfer/utilization", "biosimilar margin bridge", "Celltrion"),
    Round328ShadowWeightRow(E2RArchetype.PLATFORM_ENZYME_BLOCKBUSTER_STAGE3_YELLOW, 0, 0, 0, 5, 2, 0, 5, 3, -1, -1, -2, -5, -1, -1, -1, -5, "blockbuster SC linkage", "royalty/patent/commercial launch", "royalty economics and sell-through", "Alteogen"),
    Round328ShadowWeightRow(E2RArchetype.AESTHETIC_TOXIN_US_FDA_STAGE2, 0, 0, 0, 0, 4, 0, 1, 3, -1, -1, -5, -1, -1, -1, -1, -5, "FDA approval and U.S. launch", "sell-through/physician adoption", "repeat use and margin", "Hugel"),
    Round328ShadowWeightRow(E2RArchetype.MEDICAL_AESTHETIC_DEVICE_MA_STAGE2, 0, 0, 0, 0, 0, 3, 1, 1, -1, -1, -1, -1, -4, -1, -1, -5, "M&A valuation reference", "liquidity and peer readthrough", "listed operating evidence required", "Jeisys"),
    Round328ShadowWeightRow(E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4B, 0, 0, 0, 0, 0, 0, 5, 0, -1, -1, -1, -1, -1, -5, -1, -5, "patent litigation overlay", "settlement or clearance", "not Green until clearance and launch economics", "Samsung Bioepis"),
)


def round328_case_records() -> tuple[E2RCaseRecord, ...]:
    records = tuple(candidate.to_case_record() for candidate in ROUND328_CASE_CANDIDATES)
    for record in records:
        record.validate()
    return records


def round328_case_rows() -> list[dict[str, str]]:
    return [candidate.as_row() for candidate in ROUND328_CASE_CANDIDATES]


def round328_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND328_TRIGGER_RECORDS]


def round328_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND328_SHADOW_WEIGHT_ROWS]


def round328_summary() -> dict[str, object]:
    return {
        "source_round": ROUND328_SOURCE_ROUND_PATH,
        "round_id": ROUND328_ANALYST_ROUND_ID,
        "loop_name": ROUND328_LOOP_NAME,
        "large_sector": ROUND328_LARGE_SECTOR,
        "method": ROUND328_METHOD,
        "case_candidate_count": len(ROUND328_CASE_CANDIDATES),
        "trigger_count": len(ROUND328_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND328_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": sum(1 for case in ROUND328_CASE_CANDIDATES if "Stage2-Actionable" in case.stage_candidate),
        "stage2_candidate_count": sum(1 for case in ROUND328_CASE_CANDIDATES if "Stage2" in case.stage_candidate),
        "stage3_yellow_candidate_count": sum(1 for case in ROUND328_CASE_CANDIDATES if "Yellow" in case.stage_candidate),
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": sum(1 for case in ROUND328_CASE_CANDIDATES if case.stage4b_date is not None),
        "hard_4c_case_count": sum(1 for case in ROUND328_CASE_CANDIDATES if case.hard_4c_confirmed),
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round328_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND328_SOURCE_ROUND_PATH,
        "round_id": ROUND328_ANALYST_ROUND_ID,
        "large_sector": ROUND328_LARGE_SECTOR,
        "method": ROUND328_METHOD,
        "summary": round328_summary(),
        "target_archetypes": dict(ROUND328_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND328_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND328_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND328_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND328_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND328_SCORE_UP_AXES),
        "score_down_axes": list(ROUND328_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND328_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND328_HARD_4C_GATES),
        "row_separation_rules": list(ROUND328_ROW_SEPARATION_RULES),
        "shadow_weights": round328_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_change_production_scoring",
            "do_not_use_round328_cases_as_candidate_generation_input",
            "do_not_force_Stage3_Green",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_policy_facility_FDA_or_patent_headline_as_Green_without_revenue_utilization_royalty_sellthrough_or_risk_closure",
        ],
    }


def render_round328_summary_markdown() -> str:
    summary = round328_summary()
    lines = [
        "# Round 328 R7 Loop 17 Bio Healthcare Medical Device Trigger Validation",
        "",
        f"- source_round: `{ROUND328_SOURCE_ROUND_PATH}`",
        f"- analyst_round_id: `{ROUND328_ANALYST_ROUND_ID}`",
        f"- large_sector: `{ROUND328_LARGE_SECTOR}`",
        f"- method: `{ROUND328_METHOD}`",
        f"- case candidates: `{summary['case_candidate_count']}`",
        f"- triggers: `{summary['trigger_count']}`",
        f"- Stage2-Actionable candidates: `{summary['stage2_actionable_candidate_count']}`",
        f"- Stage3-Yellow candidates: `{summary['stage3_yellow_candidate_count']}`",
        "- Stage3-Green confirmed: `0`",
        "- production_scoring_changed: `false`",
        "- candidate_generation_input: `false`",
        "- shadow_weight_only: `true`",
        "",
        "## 핵심 결론",
        "",
        "- SK Bioscience / IDT Biologika는 제조자산 M&A와 +11.7% 이벤트 반응이 있어 Stage2-Actionable이다.",
        "- Samsung Biologics 정책 지원 랠리는 Stage2-Actionable이지만 회사별 계약과 마진 브리지가 없으면 Green이 아니다.",
        "- Samsung Biologics / GSK U.S. facility는 증거는 좋지만 가격 반응이 실패해 Stage2 price-failed로 남긴다.",
        "- Celltrion U.S. localization은 tariff hedge Stage2이나 직접 가격 검증이 없다.",
        "- Alteogen / Keytruda SC는 Stage3-Yellow 후보지만 royalty economics, patent containment, launch sell-through가 남아 있다.",
        "- Hugel Letybo U.S. launch는 FDA 승인 Stage2이며 physician adoption과 sell-through가 다음 gate다.",
        "- Jeisys / Archimed는 M&A valuation reference이지 public operating Green이 아니다.",
        "- Samsung Bioepis / Amgen patent litigation은 4B risk이며, 판결/금지명령/가격 앵커 전에는 hard 4C로 확정하지 않는다.",
    ]
    return "\n".join(lines) + "\n"


def render_round328_trigger_grid_markdown() -> str:
    lines = [
        "# Round 328 R7 Loop 17 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | date | event_return | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round328_trigger_rows():
        lines.append(
            f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |"
        )
    return "\n".join(lines) + "\n"


def render_round328_stage_rules_markdown() -> str:
    sections = [
        ("Stage2-Actionable Rules", ROUND328_STAGE2_ACTIONABLE_RULES),
        ("Stage3-Yellow Rules", ROUND328_STAGE3_YELLOW_RULES),
        ("Stage3-Green Rules", ROUND328_STAGE3_GREEN_RULES),
        ("Green Blockers", ROUND328_GREEN_BLOCKERS),
        ("Score Up Axes", ROUND328_SCORE_UP_AXES),
        ("Score Down Axes", ROUND328_SCORE_DOWN_AXES),
        ("Row Separation Rules", ROUND328_ROW_SEPARATION_RULES),
    ]
    lines = ["# Round 328 R7 Loop 17 Stage Rules", "", "Do not apply these weights to production scoring yet.", ""]
    for title, values in sections:
        lines.extend([f"## {title}", ""])
        lines.extend(f"- `{value}`" for value in values)
        lines.append("")
    return "\n".join(lines)


def render_round328_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 328 R7 Loop 17 Stage 4B / 4C Review", "", "## 4B Watch", ""]
    lines.extend(f"- `{item}`" for item in ROUND328_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- `{item}`" for item in ROUND328_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND328_CASE_CANDIDATES:
        lines.append(f"- `{case.case_id}`: {case.stage_candidate}; {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round328_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 328 R7 Loop 17 Price Validation Plan",
        "",
        "Full adjusted OHLC is not complete. Do not create MFE/MAE or peak/drawdown values from reported event anchors.",
        "",
        "| case_id | status | event anchor | next backfill |",
        "| --- | --- | --- | --- |",
    ]
    for case in ROUND328_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | price_data_unavailable_after_deep_search | {json.dumps(case.extra_price_metrics, ensure_ascii=False, sort_keys=True)} | adjusted OHLC backfill required |"
        )
    return "\n".join(lines) + "\n"


def write_round328_r7_loop17_reports(
    *,
    output_directory: str | Path = ROUND328_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND328_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND328_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND328_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND328_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    cases_path = Path(cases_path)
    triggers_path = Path(triggers_path)
    audit_path = Path(audit_path)
    weight_profile_path = Path(weight_profile_path)

    cases = write_case_library(round328_case_records(), cases_path)
    triggers = _write_jsonl(triggers_path, (trigger.as_dict() for trigger in ROUND328_TRIGGER_RECORDS))
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(json.dumps(round328_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    weights = _write_csv(weight_profile_path, round328_shadow_weight_rows())

    paths = {
        "cases": cases,
        "triggers": triggers,
        "audit": audit_path,
        "weight_profile": weights,
        "case_rows_csv": output_directory / "case_rows.csv",
        "trigger_rows_csv": output_directory / "trigger_rows.csv",
        "summary": output_directory / "round328_summary.md",
        "trigger_grid_md": output_directory / "trigger_grid.md",
        "stage_rules": output_directory / "stage_rules.md",
        "stage4b_4c_review": output_directory / "stage4b_4c_review.md",
        "price_validation_plan": output_directory / "price_validation_plan.md",
    }
    _write_csv(paths["case_rows_csv"], round328_case_rows())
    _write_csv(paths["trigger_rows_csv"], round328_trigger_rows())
    paths["summary"].write_text(render_round328_summary_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round328_trigger_grid_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round328_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round328_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round328_price_validation_plan_markdown(), encoding="utf-8")
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
    "ROUND328_CASE_CANDIDATES",
    "ROUND328_GREEN_BLOCKERS",
    "ROUND328_HARD_4C_GATES",
    "ROUND328_LARGE_SECTOR",
    "ROUND328_REQUIRED_TARGET_ALIASES",
    "ROUND328_ROW_SEPARATION_RULES",
    "ROUND328_SCORE_DOWN_AXES",
    "ROUND328_SCORE_UP_AXES",
    "ROUND328_SHADOW_WEIGHT_ROWS",
    "ROUND328_STAGE2_ACTIONABLE_RULES",
    "ROUND328_STAGE3_GREEN_RULES",
    "ROUND328_STAGE3_YELLOW_RULES",
    "ROUND328_STAGE4B_WATCH_TRIGGERS",
    "ROUND328_TRIGGER_RECORDS",
    "render_round328_stage4b_4c_review_markdown",
    "render_round328_stage_rules_markdown",
    "render_round328_trigger_grid_markdown",
    "round328_audit_payload",
    "round328_case_records",
    "round328_case_rows",
    "round328_shadow_weight_rows",
    "round328_summary",
    "round328_trigger_rows",
    "write_round328_r7_loop17_reports",
]
