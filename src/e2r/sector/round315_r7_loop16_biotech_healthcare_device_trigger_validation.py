"""Round-315 R7 Loop-16 biotech, healthcare and medical-device validation.

This module converts ``docs/round/round_315.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: FDA approval can be strong Stage2 evidence. It is still not
Stage3-Green until partner sales, royalty/milestone economics, manufacturing
quality and full price-window evidence are visible as of the replay date.
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


ROUND315_SOURCE_ROUND_PATH = "docs/round/round_315.md"
ROUND315_ANALYST_ROUND_ID = "round_243"
ROUND315_LARGE_SECTOR = "BIO_HEALTHCARE_MEDICAL_DEVICE"
ROUND315_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND315_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round315_r7_loop16_biotech_healthcare_device_trigger_validation"
ROUND315_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_loop16_round243.jsonl"
ROUND315_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r7_loop16_round243.jsonl"
ROUND315_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round315_r7_loop16_biotech_healthcare_device_trigger_validation_audit.json"
ROUND315_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round243_r7_loop16_v1.csv"

ROUND315_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "SC_FORMULATION_PLATFORM_STAGE3_YELLOW": E2RArchetype.SC_FORMULATION_PLATFORM_STAGE3_YELLOW.value,
    "BIOPHARMA_TARIFF_POLICY_SUPPORT_STAGE2": E2RArchetype.BIOPHARMA_TARIFF_POLICY_SUPPORT_STAGE2.value,
    "CDMO_US_FACILITY_EXPANSION_STAGE2_PRICE_MUTED": E2RArchetype.CDMO_US_FACILITY_EXPANSION_STAGE2_PRICE_MUTED.value,
    "VACCINE_CDMO_MA_STAGE2_ACTIONABLE": E2RArchetype.VACCINE_CDMO_MA_STAGE2_ACTIONABLE.value,
    "BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE": E2RArchetype.BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE.value,
    "ONCOLOGY_APPROVAL_STAGE2_WITH_MANUFACTURING_4B": E2RArchetype.ONCOLOGY_APPROVAL_STAGE2_WITH_MANUFACTURING_4B.value,
    "BIOSIMILAR_PATENT_LITIGATION_4C_WATCH": E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH.value,
    "AESTHETIC_MEDICAL_DEVICE_PE_BUYOUT_STAGE2": E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_BUYOUT_STAGE2.value,
    "PHARMA_TARIFF_4B_4C_WATCH": E2RArchetype.PHARMA_TARIFF_4B_4C_WATCH.value,
}

ROUND315_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "FDA_EMA_MFDS_approval_or_pivotal_trial_success_exists",
    "partner_product_launch_or_sales_started",
    "royalty_or_milestone_economics_confirmed",
    "event_return_at_least_5pct",
    "CDMO_or_MA_deal_value_and_capacity_are_specific",
    "US_or_EU_facility_links_to_tariff_hedge_or_customer_proximity",
    "no_patent_CRL_FDA_inspection_or_manufacturing_defect_overlay_for_positive_candidate",
)

ROUND315_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_FCF_path_can_change_materially",
    "one_of_royalty_utilization_manufacturing_patent_or_launch_timing_gate_remains_open",
    "reported_price_anchor_supports_trigger_but_full_adjusted_OHLC_is_missing",
    "case_is_not_pure_policy_facility_buyout_or_filing_headline",
)

ROUND315_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "regulatory_approval_converts_to_revenue_royalty_or_milestone",
    "partner_launch_and_adoption_are_visible",
    "CDMO_facility_utilization_and_margin_are_visible",
    "FDA_inspection_or_manufacturing_observations_are_resolved",
    "patent_litigation_is_settled_or_launch_timing_is_clear",
    "tariff_hedge_translates_into_protected_gross_margin",
    "full_adjusted_OHLC_MFE_MAE_window_supports_stage_candidate",
)

ROUND315_GREEN_BLOCKERS: tuple[str, ...] = (
    "approval_without_economics",
    "facility_acquisition_without_utilization",
    "policy_support_without_backlog",
    "biotech_MA_without_ROIC",
    "biosimilar_filing_without_patent_clearance",
    "control_premium_delisting_without_public_forward_return",
    "tariff_headline_without_margin_protection",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND315_SCORE_UP_AXES: tuple[str, ...] = (
    "regulatory_approval_to_sales_bridge",
    "royalty_milestone_visibility",
    "CDMO_capacity_utilization",
    "US_localization_tariff_hedge",
    "MA_price_reaction",
    "partner_product_adoption",
    "patent_litigation_resolution",
    "manufacturing_inspection_cleanliness",
)

ROUND315_SCORE_DOWN_AXES: tuple[str, ...] = (
    "approval_without_economics",
    "facility_acquisition_without_utilization",
    "policy_support_without_backlog",
    "biotech_MA_without_ROIC",
    "biosimilar_filing_without_patent_clearance",
    "control_premium_delisting_without_public_forward_return",
    "tariff_headline_without_margin_protection",
)

ROUND315_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "approval_headline_appears_before_royalty_or_sales_economics",
    "CDMO_facility_is_acquired_before_utilization_and_client_transfer_are_known",
    "MA_rally_appears_before_post_deal_backlog_and_ROIC",
    "biosimilar_filing_appears_before_patent_clearance",
    "FDA_CRL_appears_due_manufacturing_or_inspection_issue",
    "tariff_policy_drives_localization_before_actual_margin_protection",
)

ROUND315_4C_WATCH_GATES: tuple[str, ...] = (
    "FDA_complete_response_letter_from_efficacy_safety_or_data_integrity",
    "manufacturing_inspection_observation_blocks_approval",
    "patent_lawsuit_blocks_biosimilar_launch",
    "trial_failure_or_endpoint_miss",
    "product_recall_or_safety_event",
    "CDMO_FDA_warning_letter_or_batch_failure",
    "tariff_shock_not_offset_by_US_facility",
)

ROUND315_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_approval_sales_facility_MA_litigation_or_tariff_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_approval_facility_MA_filing_buyout_or_tariff_headline_as_Green_without_royalty_sales_utilization_patent_clearance_or_margin",
)


@dataclass(frozen=True)
class Round315ShadowWeightRow:
    archetype: E2RArchetype
    regulatory_approval_to_sales_bridge: int
    royalty_milestone_visibility: int
    cdmo_capacity_utilization: int
    us_localization_tariff_hedge: int
    ma_price_reaction: int
    partner_product_adoption: int
    patent_litigation_resolution: int
    manufacturing_inspection_cleanliness: int
    approval_without_economics_penalty: int
    facility_acquisition_without_utilization_penalty: int
    policy_support_without_backlog_penalty: int
    biotech_ma_without_roic_penalty: int
    biosimilar_filing_without_patent_clearance_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "regulatory_approval_to_sales_bridge": _signed(self.regulatory_approval_to_sales_bridge),
            "royalty_milestone_visibility": _signed(self.royalty_milestone_visibility),
            "CDMO_capacity_utilization": _signed(self.cdmo_capacity_utilization),
            "US_localization_tariff_hedge": _signed(self.us_localization_tariff_hedge),
            "MA_price_reaction": _signed(self.ma_price_reaction),
            "partner_product_adoption": _signed(self.partner_product_adoption),
            "patent_litigation_resolution": _signed(self.patent_litigation_resolution),
            "manufacturing_inspection_cleanliness": _signed(self.manufacturing_inspection_cleanliness),
            "approval_without_economics_penalty": _signed(self.approval_without_economics_penalty),
            "facility_acquisition_without_utilization_penalty": _signed(self.facility_acquisition_without_utilization_penalty),
            "policy_support_without_backlog_penalty": _signed(self.policy_support_without_backlog_penalty),
            "biotech_MA_without_ROIC_penalty": _signed(self.biotech_ma_without_roic_penalty),
            "biosimilar_filing_without_patent_clearance_penalty": _signed(self.biosimilar_filing_without_patent_clearance_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round315TriggerRecord:
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
class Round315CaseCandidate:
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
            "do_not_use_round315_cases_as_candidate_generation_input",
            "do_not_treat_approval_facility_MA_filing_buyout_or_tariff_headline_as_Green_without_royalty_sales_utilization_patent_clearance_or_margin",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND315_LARGE_SECTOR,
            large_sector=ROUND315_LARGE_SECTOR,
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
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4B" in field or "4b" in field or "CRL" in field or "tariff" in field or "utilization" in field),
            stage4c_evidence=tuple(
                field
                for field in (*self.red_flag_fields, *self.evidence_fields)
                if "4C" in field
                or "4c" in field
                or "CRL" in field
                or "patent" in field
                or "lawsuit" in field
                or "inspection" in field
                or "tariff" in field
            ),
            must_have_fields=ROUND315_STAGE3_GREEN_RULES,
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
                stage1_price=self.stage1_price_anchor,
                stage2_price=self.stage2_price_anchor,
                stage3_price=self.stage2_price_anchor if self.stage3_date else None,
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


ROUND315_CASE_CANDIDATES: tuple[Round315CaseCandidate, ...] = (
    Round315CaseCandidate(
        "r7_loop16_alteogen_keytruda_sc",
        "196170",
        "Alteogen / Merck Keytruda Qlex",
        E2RArchetype.SC_FORMULATION_PLATFORM_STAGE3_YELLOW,
        (E2RArchetype.SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN, E2RArchetype.SC_FORMULATION_PATENT_4C_WATCH),
        "success_candidate",
        "Stage3_Yellow_candidate_platform_to_product",
        "r7l16_alteogen_keytruda_T2",
        "Stage3-Yellow_candidate",
        "Stage3-Yellow candidate",
        date(2024, 11, 19),
        date(2025, 9, 19),
        date(2025, 9, 19),
        date(2025, 9, 19),
        None,
        False,
        ("SC_Keytruda_non_inferior_trial", "FDA_Keytruda_Qlex_approval", "Keytruda_2024_sales_usd_30bn", "expected_SC_adoption_30_40pct", "Qlex_Q1_2026_sales_usd_128mn"),
        ("royalty_rate_not_disclosed", "direct_Alteogen_price_anchor_missing", "Halozyme_patent_challenge_risk", "full_adjusted_OHLC_MFE_MAE_missing"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"t0_trial_date": "2024-11-19", "t1_launch_plan_date": "2025-03-27", "t2_fda_approval_date": "2025-09-19", "t3_sales_validation_date": "2026-04-30", "keytruda_2024_sales_usd_bn": 30, "expected_sc_adoption_pct": "30-40", "qlex_q1_2026_sales_usd_mn": 128},
        "aligned",
        "Stage3_Yellow_candidate_platform_to_product",
        "unknown",
        "yellow_success",
        "Product validation is strong, but royalty economics and direct KRX price anchor remain Green gates.",
    ),
    Round315CaseCandidate(
        "r7_loop16_samsung_biologics_policy_support",
        "207940",
        "Samsung Biologics / Korea biopharma policy support",
        E2RArchetype.BIOPHARMA_TARIFF_POLICY_SUPPORT_STAGE2,
        (E2RArchetype.BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM, E2RArchetype.BIOPHARMA_TARIFF_LOCALIZATION_STAGE2),
        "success_candidate",
        "Stage2_policy_support",
        "r7l16_samsungbio_policy_T0",
        "Stage2_policy_support",
        "Stage2",
        date(2025, 5, 21),
        date(2025, 5, 21),
        None,
        date(2025, 5, 21),
        None,
        False,
        ("government_biopharma_support_pledge", "pharma_sector_plus_3_97pct", "samsung_biologics_plus_6_23pct", "korea_pharma_exports_2024_usd_9_59bn", "us_share_exports_16pct"),
        ("tariff_details_missing", "US_manufacturing_plan_missing", "FDA_inspection_outcome_missing", "new_CDMO_order_backlog_missing", "policy_support_without_backlog_4B"),
        6.23,
        None,
        None,
        None,
        None,
        None,
        {"trigger_date": "2025-05-21", "pharma_sector_event_return_pct": 3.97, "samsung_biologics_event_return_pct": 6.23, "celltrion_event_return_pct": 0.35, "kospi_event_return_pct": 0.99, "market_relative_return_pp": 5.24, "korea_pharma_exports_2024_usd_bn": 9.59, "us_share_of_korea_pharma_exports_pct": 16},
        "aligned",
        "Stage2_policy_support_not_Green",
        "policy_event_rerating",
        "stage2_watch_success",
        "Policy support moved the stock and sector, but backlog, utilization and tariff details are not closed.",
    ),
    Round315CaseCandidate(
        "r7_loop16_samsung_biologics_gsk_us_facility",
        "207940",
        "Samsung Biologics / GSK U.S. facility",
        E2RArchetype.CDMO_US_FACILITY_EXPANSION_STAGE2_PRICE_MUTED,
        (E2RArchetype.CDMO_LOCALIZATION_EVIDENCE_GOOD_PRICE_FAILED, E2RArchetype.CDMO_US_TARIFF_HEDGE_STAGE2),
        "success_candidate",
        "evidence_good_but_price_muted",
        "r7l16_samsungbio_gsk_T0",
        "Stage2_facility_expansion_price_muted",
        "Stage2",
        date(2025, 12, 22),
        date(2025, 12, 22),
        None,
        date(2025, 12, 22),
        None,
        False,
        ("GSK_US_facility_acquisition_usd_280mn", "Rockville_Maryland_facility", "facility_capacity_60000L", "shares_minus_0_4pct", "market_plus_2pct"),
        ("deal_closing_missing", "capacity_upgrade_plan_missing", "client_transfer_missing", "utilization_missing", "margin_accretion_missing", "evidence_good_but_price_muted_4B"),
        None,
        -0.4,
        None,
        None,
        None,
        None,
        {"trigger_date": "2025-12-22", "acquisition_value_usd_mn": 280, "facility_capacity_liters": 60000, "event_return_pct": -0.4, "market_context_pct": 2.0, "market_relative_return_pp": -2.4},
        "evidence_good_but_price_failed",
        "evidence_good_but_price_muted",
        "unknown",
        "stage2_watch_success",
        "U.S. capacity is strategic, but the event underperformed the market and utilization remains the Green gate.",
    ),
    Round315CaseCandidate(
        "r7_loop16_sk_bioscience_idt_biologika",
        "302440",
        "SK Bioscience / IDT Biologika",
        E2RArchetype.VACCINE_CDMO_MA_STAGE2_ACTIONABLE,
        (E2RArchetype.VACCINE_CDMO_M_AND_A_STAGE2, E2RArchetype.VACCINE_CDMO_MA_EVENT_PREMIUM),
        "success_candidate",
        "Stage2_Actionable_MA",
        "r7l16_skbioscience_idt_T0",
        "Stage2-Actionable_MA",
        "Stage2-Actionable",
        date(2024, 6, 27),
        date(2024, 6, 27),
        None,
        date(2024, 6, 27),
        None,
        False,
        ("IDT_Biologika_60pct_stake", "deal_value_krw_339bn", "deal_value_usd_243_75mn", "first_major_MA_since_2021_IPO", "shares_plus_11_7pct"),
        ("IDT_utilization_missing", "contract_backlog_missing", "vaccine_demand_durability_missing", "integration_margin_missing", "post_acquisition_ROIC_missing"),
        11.7,
        None,
        None,
        None,
        None,
        None,
        {"trigger_date": "2024-06-27", "stake_acquired_pct": 60, "deal_value_krw_bn": 339, "deal_value_usd_mn": 243.75, "event_return_pct": 11.7, "first_major_ma_since_ipo": True},
        "aligned",
        "excellent_stage2_actionable_MA",
        "unknown",
        "stage2_watch_success",
        "Clear M&A value and strong price reaction create Stage2-Actionable, but utilization and backlog are Yellow gates.",
    ),
    Round315CaseCandidate(
        "r7_loop16_celltrion_us_factory_localization",
        "068270",
        "Celltrion / U.S. factory localization",
        E2RArchetype.BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE,
        (E2RArchetype.BIOPHARMA_TARIFF_LOCALIZATION_STAGE2, E2RArchetype.BIOSIMILAR_US_TARIFF_HEDGE_STAGE2),
        "success_candidate",
        "Stage2_US_localization_with_capex_gate",
        "r7l16_celltrion_us_factory_T0",
        "Stage2_US_localization_with_capex_gate",
        "Stage2",
        date(2025, 7, 29),
        date(2025, 7, 29),
        None,
        date(2025, 11, 19),
        None,
        False,
        ("US_factory_preferred_bidder", "planned_initial_investment_krw_700bn", "ImClone_acquisition_usd_330mn", "US_factory_expansion_krw_700bn", "expansion_usd_478mn"),
        ("direct_Celltrion_price_anchor_missing", "US_factory_utilization_missing", "tariff_avoidance_effect_missing", "biosimilar_margin_missing", "capex_ROIC_missing"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"preferred_bidder_date": "2025-07-29", "planned_initial_investment_krw_bn": 700, "possible_additional_investment_krw_bn": "300-700", "imclone_acquisition_value_usd_mn": 330, "expansion_investment_krw_bn": 700, "expansion_investment_usd_mn": 478},
        "evidence_good_but_price_failed",
        "Stage2_US_localization_not_Green",
        "unknown",
        "stage2_watch_success",
        "U.S. localization is a tariff hedge, but utilization, margin and capex ROIC are missing.",
    ),
    Round315CaseCandidate(
        "r7_loop16_yuhan_lazertinib_jnj_rybrevant",
        "000100",
        "Yuhan / J&J Rybrevant lazertinib",
        E2RArchetype.ONCOLOGY_APPROVAL_STAGE2_WITH_MANUFACTURING_4B,
        (E2RArchetype.ONCOLOGY_LICENSE_ROYALTY_STAGE2, E2RArchetype.MANUFACTURING_INSPECTION_CRL_OVERLAY),
        "success_candidate",
        "Stage2_approval_with_manufacturing_4B",
        "r7l16_yuhan_lazertinib_T0",
        "Stage2_approval_with_4B",
        "Stage2 + 4B-watch",
        date(2024, 8, 20),
        date(2024, 8, 20),
        None,
        date(2024, 12, 16),
        None,
        False,
        ("FDA_Rybrevant_lazertinib_approval", "first_line_EGFR_mutated_advanced_NSCLC", "EGFR_mutation_US_NSCLC_10_15pct", "Rybrevant_peak_sales_over_usd_5bn", "SC_Rybrevant_CRL_manufacturing_observations"),
        ("Yuhan_royalty_rate_missing", "lazertinib_milestone_revenue_missing", "commercial_launch_sales_missing", "SC_Rybrevant_resolution_missing", "manufacturing_inspection_CRL_4B"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"approval_date": "2024-08-20", "egfr_mutation_us_nsclc_pct": "10-15", "rybrevant_peak_sales_expectation_usd_bn": ">5", "sc_crl_date": "2024-12-16", "crl_reason": "manufacturing_facility_inspection_observations", "crl_not_related_to": ["formulation", "efficacy", "safety"]},
        "evidence_good_but_price_failed",
        "approval_stage2_with_manufacturing_4B",
        "unknown",
        "stage2_watch_success",
        "Approval is strong, but issuer economics and SC manufacturing resolution remain open gates.",
    ),
    Round315CaseCandidate(
        "r7_loop16_samsung_bioepis_amgen_litigation",
        "207940_readthrough",
        "Samsung Bioepis / Amgen Prolia-Xgeva litigation",
        E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH,
        (E2RArchetype.BIOSIMILAR_PATENT_LITIGATION, E2RArchetype.PATENT_CHALLENGE_OVERLAY),
        "4b_watch",
        "4C_watch_patent_litigation",
        "r7l16_samsung_bioepis_amgen_T1",
        "4C-watch_patent_litigation",
        "4C-watch",
        date(2024, 8, 13),
        date(2024, 8, 13),
        None,
        None,
        date(2024, 8, 13),
        False,
        ("biosimilar_US_approval_application", "Amgen_lawsuit", "alleged_patents_34", "Prolia_US_sales_prior_year_usd_2_7bn", "Xgeva_US_sales_prior_year_usd_1_5bn"),
        ("settlement_missing", "launch_date_missing", "patent_resolution_missing", "price_erosion_missing", "market_share_capture_missing", "patent_litigation_4C_watch"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"trigger_date": "2024-08-13", "alleged_patents": 34, "prolia_us_sales_prior_year_usd_bn": 2.7, "xgeva_us_sales_prior_year_usd_bn": 1.5},
        "aligned",
        "biosimilar_patent_litigation_4C_watch",
        "unknown",
        "stage2_watch_success",
        "Biosimilar market opportunity is large, but patent litigation blocks launch-timing confidence.",
    ),
    Round315CaseCandidate(
        "r7_loop16_jeisys_archimed_medical_device_buyout",
        "287410",
        "Jeisys Medical / ArchiMed",
        E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_BUYOUT_STAGE2,
        (E2RArchetype.AESTHETIC_DEVICE_MA_CONTROL_PREMIUM, E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT),
        "event_premium",
        "Stage2_medical_device_MA_with_control_premium_4B",
        "r7l16_jeisys_archimed_T0",
        "Stage2_MA_control_premium",
        "Stage2 M&A",
        date(2024, 9, 11),
        date(2024, 9, 11),
        None,
        date(2024, 9, 11),
        None,
        False,
        ("ArchiMed_buyout_usd_742mn", "reported_share_close_krw_12860", "energy_based_devices", "wrinkle_scar_body_hair_removal_applications"),
        ("delisting_process", "control_premium", "private_equity_ownership", "public_market_exit", "operating_Green_not_applicable"),
        None,
        None,
        None,
        12860,
        12860,
        None,
        {"trigger_date": "2024-09-11", "acquisition_value_usd_mn": 742, "reported_share_close_krw": 12860, "device_type": "energy_based_devices", "full_ohlc_status": "not_applicable_after_buyout"},
        "aligned",
        "Stage2_MA_not_operating_Green",
        "event_premium",
        "stage2_watch_success",
        "The buyout validates device demand, but control premium and delisting are not operating Stage3 evidence.",
    ),
    Round315CaseCandidate(
        "r7_loop16_pharma_tariff_localization",
        "207940/068270/302440/pharma_basket",
        "Korea pharma tariff localization basket",
        E2RArchetype.PHARMA_TARIFF_4B_4C_WATCH,
        (E2RArchetype.BIOPHARMA_TARIFF_LOCALIZATION_STAGE2, E2RArchetype.BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE),
        "4b_watch",
        "4B_4C_policy_shock_with_Stage2_localization_hedge",
        "r7l16_pharma_tariff_T0",
        "4B_4C_policy_shock",
        "4B/4C-watch + Stage2 hedge",
        date(2025, 9, 26),
        date(2025, 9, 26),
        None,
        date(2025, 9, 26),
        date(2025, 9, 26),
        False,
        ("branded_drug_import_tariff_100pct_context", "US_manufacturing_exception", "Asian_pharma_stocks_fell", "localization_hedge_examples"),
        ("final_tariff_rate_missing", "US_plant_certification_missing", "product_transfer_missing", "margin_protection_missing", "tariff_headline_without_margin_protection_4B_4C"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"trigger_date": "2025-09-26", "tariff_rate_context_pct": 100, "tariff_scope": "branded_drug_imports_unless_US_manufacturing_started", "localization_hedge_examples": ["Samsung_Biologics_US_facility", "Celltrion_US_factory", "SK_Bioscience_IDT_Biologika"]},
        "aligned",
        "pharma_tariff_4B_4C_with_localization_hedge",
        "policy_event_rerating",
        "stage2_watch_success",
        "Tariff shock makes localization valuable, but certification, product transfer and margin protection remain unresolved.",
    ),
)


ROUND315_TRIGGER_RECORDS: tuple[Round315TriggerRecord, ...] = (
    Round315TriggerRecord("r7l16_alteogen_keytruda_T2", "r7_loop16_alteogen_keytruda_sc", "Stage3-Yellow_candidate", "2025-09-19/2026-04-30", "FDA approved Merck Keytruda Qlex; Merck expects 30-40% adoption within two years; Qlex generated $128M sales in Q1 2026; Alteogen enzyme used with Keytruda SC.", "price_data_unavailable_after_deep_search", "Stage3_Yellow_candidate_platform_to_product", "Stage3-Yellow_candidate", {"qlex_q1_2026_sales_usd_mn": 128}),
    Round315TriggerRecord("r7l16_samsungbio_policy_T0", "r7_loop16_samsung_biologics_policy_support", "Stage2_policy_support", "2025-05-21", "Korea pledges biopharma support; pharma sector +3.97%, Samsung Biologics +6.23%, Celltrion +0.35%, KOSPI +0.99%.", 6.23, "Stage2_policy_support_not_Green", "Stage2", {"market_relative_return_pp": 5.24}),
    Round315TriggerRecord("r7l16_samsungbio_gsk_T0", "r7_loop16_samsung_biologics_gsk_us_facility", "Stage2_facility_price_muted", "2025-12-22", "Samsung Biologics buys first U.S. facility from GSK for $280M; 60,000L drug substance capacity; shares -0.4% vs market +2%.", -0.4, "evidence_good_but_price_muted", "Stage2", {"facility_capacity_liters": 60000}),
    Round315TriggerRecord("r7l16_skbioscience_idt_T0", "r7_loop16_sk_bioscience_idt_biologika", "Stage2-Actionable_MA", "2024-06-27", "SK Bioscience acquires 60% of IDT Biologika for 339B won / $243.75M; first major M&A since IPO; shares +11.7% morning trade.", 11.7, "excellent_stage2_actionable_MA", "Stage2-Actionable", {"deal_value_krw_bn": 339}),
    Round315TriggerRecord("r7l16_celltrion_us_factory_T0", "r7_loop16_celltrion_us_factory_localization", "Stage2_US_localization", "2025-07-29/2025-11-19", "Celltrion selected as preferred bidder for U.S. facility, acquired ImClone from Eli Lilly for $330M, and planned up to 700B won / $478M U.S. factory expansion.", "price_data_unavailable_after_deep_search", "Stage2_US_localization_not_Green", "Stage2", {"expansion_investment_krw_bn": 700}),
    Round315TriggerRecord("r7l16_yuhan_lazertinib_T0", "r7_loop16_yuhan_lazertinib_jnj_rybrevant", "Stage2_approval_with_4B", "2024-08-20/2024-12-16", "FDA approved Rybrevant + lazertinib for first-line EGFR-mutated NSCLC; later FDA declined SC Rybrevant due manufacturing inspection observations.", "price_data_unavailable_after_deep_search", "approval_stage2_with_manufacturing_4B", "Stage2+4B", {"rybrevant_peak_sales_expectation_usd_bn": ">5"}),
    Round315TriggerRecord("r7l16_samsung_bioepis_amgen_T1", "r7_loop16_samsung_bioepis_amgen_litigation", "4C-watch_patent_litigation", "2024-08-13", "Amgen sues Samsung Bioepis over proposed Prolia/Xgeva biosimilars, alleging infringement of 34 patents; Prolia/Xgeva U.S. sales exceeded $4.2B prior year.", "price_data_unavailable_after_deep_search", "biosimilar_patent_litigation_4C_watch", "4C-watch", {"alleged_patents": 34}),
    Round315TriggerRecord("r7l16_jeisys_archimed_T0", "r7_loop16_jeisys_archimed_medical_device_buyout", "Stage2_MA_control_premium", "2024-09-11", "ArchiMed acquires Jeisys Medical for about $742M; shares closed at 12,860 won; EBD aesthetic devices but delisting/control premium overlay.", "control_premium_not_forward_OHLC", "Stage2_MA_not_operating_Green", "Stage2+4B", {"reported_share_close_krw": 12860}),
    Round315TriggerRecord("r7l16_pharma_tariff_T0", "r7_loop16_pharma_tariff_localization", "4B_4C_policy_shock", "2025-09-26", "100% branded-drug tariff threat unless U.S. manufacturing has started; Asian pharma stocks fall; Korean localization becomes hedge.", "price_data_unavailable_after_deep_search", "pharma_tariff_4B_4C_with_localization_hedge", "4B/4C-watch", {"tariff_rate_context_pct": 100}),
)


ROUND315_SHADOW_WEIGHT_ROWS: tuple[Round315ShadowWeightRow, ...] = (
    Round315ShadowWeightRow(E2RArchetype.SC_FORMULATION_PLATFORM_STAGE3_YELLOW, 5, 5, 1, 0, 0, 5, 4, 3, -5, -1, -1, -1, -1, "partner approval+sales validation", "royalty/direct price missing", "royalty+sales+OHLC", "Alteogen/Keytruda Qlex."),
    Round315ShadowWeightRow(E2RArchetype.BIOPHARMA_TARIFF_POLICY_SUPPORT_STAGE2, 1, 0, 3, 5, 2, 0, 1, 2, -2, -2, -4, -1, -1, "policy support+sector rally", "backlog/utilization missing", "tariff hedge+backlog+margin", "Samsung Biologics policy."),
    Round315ShadowWeightRow(E2RArchetype.CDMO_US_FACILITY_EXPANSION_STAGE2_PRICE_MUTED, 1, 0, 5, 5, 0, 0, 1, 4, -2, -5, -1, -2, -1, "U.S. facility/capacity", "utilization and price support missing", "client transfer+utilization+margin", "Samsung Biologics GSK facility."),
    Round315ShadowWeightRow(E2RArchetype.VACCINE_CDMO_MA_STAGE2_ACTIONABLE, 1, 0, 5, 2, 5, 1, 1, 3, -1, -3, -1, -4, -1, "M&A+price reaction", "utilization/backlog missing", "post-deal utilization+margin", "SK Bioscience IDT."),
    Round315ShadowWeightRow(E2RArchetype.BIOPHARMA_US_LOCALIZATION_STAGE2_WITH_CAPEX_GATE, 1, 0, 4, 5, 1, 1, 1, 4, -1, -5, -1, -4, -1, "U.S. localization", "capex ROI/utilization missing", "tariff shield+facility margin", "Celltrion."),
    Round315ShadowWeightRow(E2RArchetype.ONCOLOGY_APPROVAL_STAGE2_WITH_MANUFACTURING_4B, 5, 5, 0, 0, 1, 4, 1, 5, -5, -1, -1, -1, -1, "FDA approval+partner launch", "royalty/SC manufacturing missing", "royalty+sales+manufacturing resolution", "Yuhan/lazertinib."),
    Round315ShadowWeightRow(E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH, 2, 2, 0, 0, 0, 0, 5, 2, -3, -1, -1, -1, -5, "biosimilar opportunity", "patent settlement missing", "N/A", "Samsung Bioepis/Amgen."),
    Round315ShadowWeightRow(E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_BUYOUT_STAGE2, 1, 0, 1, 0, 4, 1, 0, 1, -1, -1, -1, -3, -1, "medical-device M&A", "delisting/control premium", "installed base+consumables if public", "Jeisys/ArchiMed."),
    Round315ShadowWeightRow(E2RArchetype.PHARMA_TARIFF_4B_4C_WATCH, 0, 0, 3, 5, 1, 0, 1, 4, -1, -4, -3, -2, -1, "tariff shock/localization hedge", "final tariff and margin protection missing", "certified U.S. production+margin", "pharma tariff basket."),
)


def round315_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND315_CASE_CANDIDATES]


def round315_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND315_CASE_CANDIDATES]


def round315_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND315_TRIGGER_RECORDS]


def round315_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND315_SHADOW_WEIGHT_ROWS]


def round315_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND315_REQUIRED_TARGET_ALIASES.items()]


def round315_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND315_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND315_SCORE_DOWN_AXES]
    )


def round315_summary() -> dict[str, object]:
    return {
        "source_round": ROUND315_SOURCE_ROUND_PATH,
        "round_id": ROUND315_ANALYST_ROUND_ID,
        "large_sector": ROUND315_LARGE_SECTOR,
        "method": ROUND315_METHOD,
        "case_candidate_count": len(ROUND315_CASE_CANDIDATES),
        "trigger_count": len(ROUND315_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND315_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 3,
        "stage2_policy_or_localization_candidate_count": 4,
        "stage3_yellow_candidate_count": 1,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 6,
        "stage4c_watch_count": 3,
        "hard_4c_case_count": 0,
        "evidence_good_but_price_failed_or_muted_count": 3,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R8 Loop 16",
    }


def round315_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND315_SOURCE_ROUND_PATH,
        "round_id": ROUND315_ANALYST_ROUND_ID,
        "large_sector": ROUND315_LARGE_SECTOR,
        "method": ROUND315_METHOD,
        "summary": round315_summary(),
        "required_target_aliases": dict(ROUND315_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND315_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND315_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND315_STAGE3_GREEN_RULES,
        "green_blockers": ROUND315_GREEN_BLOCKERS,
        "score_up_axes": ROUND315_SCORE_UP_AXES,
        "score_down_axes": ROUND315_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND315_STAGE4B_WATCH_TRIGGERS,
        "stage4c_watch_gates": ROUND315_4C_WATCH_GATES,
        "row_separation_rules": ROUND315_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round315_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_approval_facility_MA_filing_buyout_or_tariff_headline_as_Green_without_royalty_sales_utilization_patent_clearance_or_margin",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round315_summary_markdown() -> str:
    summary = round315_summary()
    lines = [
        "# R7 Loop 16 Bio / Healthcare / Medical Device Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: FDA approval is Stage2 evidence. It becomes Green only after royalty, sales, utilization, patent and manufacturing gates close.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Alteogen / Keytruda Qlex is the strongest Stage3-Yellow candidate, but direct KRX price and royalty economics are missing.",
            "- SK Bioscience / IDT Biologika is Stage2-Actionable because deal value and +11.7% event reaction are visible.",
            "- Samsung Biologics, Celltrion and pharma tariff cases are Stage2 localization or policy hedge until utilization and margin close.",
            "- Samsung Bioepis / Amgen litigation and Yuhan / SC Rybrevant manufacturing observation remain 4B/4C-watch gates.",
            "- Stage3-Green confirmed: `0`.",
            "- Hard 4C confirmed: `0`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round315_trigger_grid_markdown() -> str:
    lines = [
        "# Round 315 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round315_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round315_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 315 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND315_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND315_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND315_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND315_GREEN_BLOCKERS),
            "",
            "## 4C Watch Gates",
            *_bullet_lines(ROUND315_4C_WATCH_GATES),
        ]
    ) + "\n"


def render_round315_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 315 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND315_STAGE4B_WATCH_TRIGGERS),
        "",
        "## 4C Watch Gates",
        *_bullet_lines(ROUND315_4C_WATCH_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND315_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round315_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 315 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND315_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round315_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 315 Row Separation Plan",
        "",
        "Case evidence, trigger anchors and full OHLC windows must be separate rows.",
        "",
        "Easy example: a CDMO U.S. facility acquisition is Stage2 evidence. It is not Green until utilization, client transfer and margin are visible.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND315_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round315_r7_loop16_reports(
    output_directory: str | Path = ROUND315_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND315_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND315_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND315_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND315_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round315_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND315_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round315_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round315_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round315_r7_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round315_r7_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round315_r7_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round315_r7_loop16_trigger_grid.md",
        "summary": output_dir / "round315_r7_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round315_r7_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round315_r7_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round315_r7_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round315_r7_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round315_r7_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round315_r7_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round315_case_rows())
    _write_csv(paths["target_aliases"], round315_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round315_trigger_rows())
    _write_csv(paths["score_adjustments"], round315_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round315_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round315_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round315_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round315_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round315_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round315_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round315_row_separation_plan_markdown(), encoding="utf-8")
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
    "ROUND315_4C_WATCH_GATES",
    "ROUND315_CASE_CANDIDATES",
    "ROUND315_GREEN_BLOCKERS",
    "ROUND315_LARGE_SECTOR",
    "ROUND315_REQUIRED_TARGET_ALIASES",
    "ROUND315_ROW_SEPARATION_RULES",
    "ROUND315_SCORE_DOWN_AXES",
    "ROUND315_SCORE_UP_AXES",
    "ROUND315_SHADOW_WEIGHT_ROWS",
    "ROUND315_STAGE2_ACTIONABLE_RULES",
    "ROUND315_STAGE3_GREEN_RULES",
    "ROUND315_STAGE3_YELLOW_RULES",
    "ROUND315_STAGE4B_WATCH_TRIGGERS",
    "ROUND315_TRIGGER_RECORDS",
    "render_round315_stage4b_4c_review_markdown",
    "render_round315_stage_rules_markdown",
    "render_round315_trigger_grid_markdown",
    "round315_audit_payload",
    "round315_case_records",
    "round315_case_rows",
    "round315_shadow_weight_rows",
    "round315_summary",
    "round315_trigger_rows",
    "write_round315_r7_loop16_reports",
]
