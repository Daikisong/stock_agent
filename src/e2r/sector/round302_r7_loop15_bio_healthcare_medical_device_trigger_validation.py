"""Round-302 R7 Loop-15 bio/healthcare trigger validation pack.

This module converts ``docs/round/round_302.md`` into calibration-only case
records, trigger rows, and reports. It does not change production scoring,
staging, or candidate generation.

Easy example: FDA approval is useful evidence, but it is not Stage 3-Green by
itself. The path needs launch, adoption, sales or royalty conversion, and a
clean patent/litigation gate.
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


ROUND302_SOURCE_ROUND_PATH = "docs/round/round_302.md"
ROUND302_ANALYST_ROUND_ID = "round_230"
ROUND302_LARGE_SECTOR = "BIO_HEALTHCARE_MEDICAL_DEVICE"
ROUND302_METHOD = "trigger_level_backtest_v1"
ROUND302_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round302_r7_loop15_bio_healthcare_medical_device_trigger_validation"
ROUND302_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_loop15_round230.jsonl"
ROUND302_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r7_loop15_round230.jsonl"
ROUND302_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round302_r7_loop15_bio_healthcare_medical_device_trigger_validation_audit.json"
ROUND302_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round230_r7_loop15_v1.csv"

ROUND302_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN": E2RArchetype.SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN.value,
    "SC_FORMULATION_PATENT_4C_WATCH": E2RArchetype.SC_FORMULATION_PATENT_4C_WATCH.value,
    "BIOPHARMA_TARIFF_LOCALIZATION_STAGE2": E2RArchetype.BIOPHARMA_TARIFF_LOCALIZATION_STAGE2.value,
    "CDMO_LOCALIZATION_EVIDENCE_GOOD_PRICE_FAILED": E2RArchetype.CDMO_LOCALIZATION_EVIDENCE_GOOD_PRICE_FAILED.value,
    "VACCINE_CDMO_MA_STAGE2_ACTIONABLE": E2RArchetype.VACCINE_CDMO_MA_STAGE2_ACTIONABLE.value,
    "AESTHETIC_TOXIN_US_LAUNCH_STAGE2": E2RArchetype.AESTHETIC_TOXIN_US_LAUNCH_STAGE2.value,
    "AESTHETIC_DEVICE_MA_CONTROL_PREMIUM": E2RArchetype.AESTHETIC_DEVICE_MA_CONTROL_PREMIUM.value,
    "BIOSIMILAR_PATENT_LITIGATION_4C_WATCH": E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH.value,
    "PRIVATE_BIOTECH_LO_REFERENCE": E2RArchetype.PRIVATE_BIOTECH_LO_REFERENCE.value,
}

ROUND302_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "pivotal_or_noninferiority_result_is_public",
    "fda_approval_or_launch_timing_is_visible",
    "cdmo_or_vaccine_ma_has_capacity_and_price_reaction",
    "biopharma_localization_has_company_specific_facility_or_policy_support",
    "event_or_market_relative_price_reaction_is_recorded",
    "private_license_total_value_is_separated_from_upfront",
)

ROUND302_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "approval_launch_and_adoption_guidance_are_visible_but_one_gate_remains",
    "early_sales_visible_but_issuer_royalty_or_margin_bridge_pending",
    "cdmo_utilization_or_customer_transfer_partly_visible_but_margin_pending",
    "aesthetic_launch_has_channel_data_but_sellthrough_or_margin_pending",
)

ROUND302_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "actual_product_sales_after_approval_are_visible",
    "issuer_royalty_or_revenue_recognition_is_visible",
    "patent_litigation_or_launch_delay_risk_is_cleared",
    "cdmo_customer_order_utilization_and_margin_are_visible",
    "clinic_or_hospital_adoption_sellthrough_and_margin_are_visible",
    "full_window_mfe_mae_is_available_and_supportive",
)

ROUND302_GREEN_BLOCKERS: tuple[str, ...] = (
    "trial_result_only",
    "fda_approval_without_launch_or_revenue",
    "factory_acquisition_without_utilization",
    "cdmo_capacity_headline_only",
    "total_lo_value_without_upfront_and_milestone_probability",
    "biosimilar_approval_without_patent_clearance",
    "aesthetic_launch_without_clinic_sellthrough",
    "policy_support_without_company_order_or_margin",
    "private_company_reference_used_as_public_candidate",
)

ROUND302_SCORE_UP_AXES: tuple[str, ...] = (
    "fda_approval_to_launch_conversion",
    "actual_product_sales_after_approval",
    "royalty_recognition_visibility",
    "adoption_rate_guidance",
    "patent_litigation_clearance",
    "cdmo_order_backlog_utilization",
    "tariff_localization_margin_benefit",
    "ma_integration_and_utilization",
    "biosimilar_launch_settlement",
    "clinic_adoption_sellthrough",
)

ROUND302_SCORE_DOWN_AXES: tuple[str, ...] = (
    "fda_trial_result_only",
    "product_approval_without_revenue",
    "cdmo_capacity_headline_only",
    "factory_acquisition_without_utilization",
    "total_lo_value_without_upfront",
    "biosimilar_approval_without_patent_clearance",
    "aesthetic_launch_without_sellthrough",
    "policy_support_without_company_order",
)

ROUND302_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "fda_approval_headline_rerates_before_actual_sales_or_royalty",
    "cdmo_capacity_or_factory_headline_rerates_before_utilization",
    "ma_announcement_price_pop_before_integration_or_backlog",
    "aesthetic_product_launch_without_clinic_sellthrough",
    "lo_total_value_headline_without_upfront_or_probability",
)

ROUND302_HARD_4C_GATES: tuple[str, ...] = (
    "fda_crl_or_approval_rejection",
    "patent_injunction_or_confirmed_launch_delay",
    "biosimilar_litigation_blocks_launch",
    "product_safety_issue_or_recall",
    "cdmo_customer_cancellation",
    "facility_utilization_collapse",
    "clinical_trial_failure",
    "reimbursement_failure",
)


@dataclass(frozen=True)
class Round302ShadowWeightRow:
    archetype: E2RArchetype
    fda_approval_to_launch_conversion: int
    actual_product_sales_after_approval: int
    royalty_recognition_visibility: int
    adoption_rate_guidance: int
    patent_litigation_clearance: int
    cdmo_order_backlog_utilization: int
    tariff_localization_margin_benefit: int
    ma_integration_utilization: int
    biosimilar_launch_settlement: int
    clinic_adoption_sellthrough: int
    trial_result_only_penalty: int
    approval_without_revenue_penalty: int
    cdmo_capacity_headline_only_penalty: int
    total_lo_value_without_upfront_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "fda_approval_to_launch_conversion": _signed(self.fda_approval_to_launch_conversion),
            "actual_product_sales_after_approval": _signed(self.actual_product_sales_after_approval),
            "royalty_recognition_visibility": _signed(self.royalty_recognition_visibility),
            "adoption_rate_guidance": _signed(self.adoption_rate_guidance),
            "patent_litigation_clearance": _signed(self.patent_litigation_clearance),
            "cdmo_order_backlog_utilization": _signed(self.cdmo_order_backlog_utilization),
            "tariff_localization_margin_benefit": _signed(self.tariff_localization_margin_benefit),
            "ma_integration_utilization": _signed(self.ma_integration_utilization),
            "biosimilar_launch_settlement": _signed(self.biosimilar_launch_settlement),
            "clinic_adoption_sellthrough": _signed(self.clinic_adoption_sellthrough),
            "trial_result_only_penalty": _signed(self.trial_result_only_penalty),
            "approval_without_revenue_penalty": _signed(self.approval_without_revenue_penalty),
            "cdmo_capacity_headline_only_penalty": _signed(self.cdmo_capacity_headline_only_penalty),
            "total_lo_value_without_upfront_penalty": _signed(self.total_lo_value_without_upfront_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round302TriggerRecord:
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
class Round302CaseCandidate:
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
            "do_not_use_round302_cases_as_candidate_generation_input",
            "do_not_treat_fda_factory_lo_or_launch_headline_as_green",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND302_LARGE_SECTOR,
            large_sector=ROUND302_LARGE_SECTOR,
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
            must_have_fields=ROUND302_STAGE2_ACTIONABLE_RULES + ROUND302_STAGE3_YELLOW_RULES + ROUND302_STAGE3_GREEN_RULES,
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
                stage2_price=None,
                mfe_30d=self.event_mfe_pct if self.event_mfe_pct and self.event_mfe_pct > 0 else None,
                mae_30d=self.event_mae_pct if self.event_mae_pct and self.event_mae_pct < 0 else None,
                price_validation_status="reported_event_anchor_not_full_ohlc",
            ),
            data_quality=CaseDataQuality(False, True, False, 0.7),
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


ROUND302_SHADOW_WEIGHT_ROWS: tuple[Round302ShadowWeightRow, ...] = (
    Round302ShadowWeightRow(E2RArchetype.SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN, 5, 5, 5, 4, 5, 1, 1, 1, 1, 1, -4, -3, -2, -2, "trial+launch+adoption guidance", "royalty/patent pending", "approval+sales+royalty", "Alteogen/Qlex ladder template."),
    Round302ShadowWeightRow(E2RArchetype.SC_FORMULATION_PATENT_4C_WATCH, 2, 2, 4, 2, 5, 0, 0, 0, 0, 0, -2, -2, -1, -1, "patent challenge identified", "injunction/launch delay pending", "litigation cleared", "Patent overlay must be cleared before Green confirmation."),
    Round302ShadowWeightRow(E2RArchetype.BIOPHARMA_TARIFF_LOCALIZATION_STAGE2, 2, 2, 1, 1, 2, 5, 5, 4, 1, 0, -2, -2, -5, -2, "policy support or factory acquisition", "utilization/order/margin pending", "utilization+tariff saving+orders", "Samsung Bio/Celltrion localization template."),
    Round302ShadowWeightRow(E2RArchetype.CDMO_LOCALIZATION_EVIDENCE_GOOD_PRICE_FAILED, 1, 1, 0, 0, 2, 5, 5, 4, 1, 0, -2, -2, -5, -2, "facility acquisition with weak price reaction", "utilization pending", "order conversion and price recovery", "Evidence-good price-failed row stays Stage2 until conversion."),
    Round302ShadowWeightRow(E2RArchetype.VACCINE_CDMO_MA_STAGE2_ACTIONABLE, 1, 1, 0, 0, 2, 5, 3, 5, 1, 0, -2, -2, -4, -2, "M&A+price response", "integration/backlog pending", "utilization+margin", "SK Bioscience IDT template."),
    Round302ShadowWeightRow(E2RArchetype.AESTHETIC_TOXIN_US_LAUNCH_STAGE2, 4, 3, 1, 2, 3, 0, 0, 1, 1, 5, -3, -4, -1, -1, "FDA approval+launch", "clinic adoption/revenue pending", "sell-through+market share+margin", "Hugel Letybo Stage2 template."),
    Round302ShadowWeightRow(E2RArchetype.AESTHETIC_DEVICE_MA_CONTROL_PREMIUM, 1, 2, 0, 0, 1, 1, 0, 5, 0, 4, -2, -2, -2, -2, "M&A/control premium", "public operating data unavailable", "post-acquisition growth not public", "Jeisys control premium separation."),
    Round302ShadowWeightRow(E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH, 2, 2, 1, 1, 5, 0, 0, 1, 5, 0, -2, -3, -1, -1, "patent lawsuit", "settlement/launch date pending", "launch after clearance", "Samsung Bioepis/Amgen 4C-watch."),
    Round302ShadowWeightRow(E2RArchetype.PRIVATE_BIOTECH_LO_REFERENCE, 1, 1, 1, 0, 2, 0, 0, 1, 0, 0, -2, -2, -1, -5, "LO total value/upfront split", "trial progress pending", "not applicable", "Private reference only; not public candidate evidence."),
)

ROUND302_TRIGGER_RECORDS: tuple[Round302TriggerRecord, ...] = (
    Round302TriggerRecord("r7l15_alteogen_T1", "r7_loop15_alteogen_keytruda_qlex", "Stage2-Actionable", date(2024, 11, 19), "Merck SC Keytruda non-inferior to IV; injection 2-3 minutes vs IV about 30 minutes; Alteogen enzyme used", "Merck +1.8 premarket / Alteogen OHLC unavailable", "Stage2_Actionable", "Stage2-Actionable", {"merck_event_return_pct": 1.8, "injection_time_minutes": "2-3", "iv_infusion_time_minutes": 30}),
    Round302TriggerRecord("r7l15_alteogen_T2", "r7_loop15_alteogen_keytruda_qlex", "Stage3-Yellow", date(2025, 3, 27), "Merck launch plan, FDA decision date, expected 30-40% Keytruda adoption within two years", "price_data_unavailable_after_deep_search", "Stage3_Yellow_candidate", "Stage3-Yellow", {"launch_plan_date": "2025-10-01", "expected_peak_adoption_pct": "30-40", "keytruda_2024_sales_usd_bn": 30}),
    Round302TriggerRecord("r7l15_alteogen_T3", "r7_loop15_alteogen_keytruda_qlex", "Stage3-Green_candidate", date(2025, 9, 19), "FDA approves Keytruda Qlex; 1-2 minute injection; U.S. availability late September", "price_data_unavailable_after_deep_search", "Stage3_Green_candidate", "Stage3-Green_candidate", {"fda_approval": True, "brand_name": "Keytruda Qlex", "qlex_q1_2026_sales_usd_mn": 128}),
    Round302TriggerRecord("r7l15_alteogen_T5", "r7_loop15_alteogen_halozyme_patent_watch", "4C-watch", date(2025, 3, 5), "Halozyme patent challenge risk over enzyme used in injectable Keytruda", "price_data_unavailable_after_deep_search", "patent_4C_watch_not_hard", "4C-watch", {"patent_counterparty": "Halozyme", "launch_delay_confirmed": False}),
    Round302TriggerRecord("r7l15_samsungbio_T0", "r7_loop15_samsung_biologics_tariff_localization", "Stage2-Actionable", date(2025, 5, 21), "Korea pledges biopharma support under U.S. tariff pressure; pharma sector +3.97%; Samsung Biologics +6.23%", 6.23, "Stage2_policy_actionable", "Stage2-Actionable", {"pharma_sector_event_return_pct": 3.97, "samsung_biologics_event_return_pct": 6.23}),
    Round302TriggerRecord("r7l15_samsungbio_T1", "r7_loop15_samsung_biologics_tariff_localization", "evidence_good_but_price_failed", date(2025, 12, 22), "Samsung Biologics buys first U.S. drug production facility from GSK for $280M; shares -0.4% vs KOSPI +2%", -0.4, "evidence_good_but_price_failed", "Stage2_only", {"market_relative_return_pp": -2.4, "us_facility_acquisition_value_usd_mn": 280, "facility_capacity_liters": 60000}),
    Round302TriggerRecord("r7l15_celltrion_T2", "r7_loop15_celltrion_us_factory_tariff_hedge", "Stage2_localization", date(2025, 9, 23), "Celltrion U.S. subsidiary acquires ImClone Systems from Eli Lilly for $330M to hedge U.S. tariff risk", "price_data_unavailable_after_deep_search", "success_candidate_stage2", "Stage2", {"imclone_acquisition_value_usd_mn": 330, "us_expansion_investment_krw_bn": 700}),
    Round302TriggerRecord("r7l15_skbio_T1", "r7_loop15_sk_bioscience_idt_biologika", "Stage2-Actionable", date(2024, 6, 27), "SK Bioscience buys 60% of Germany's IDT Biologika for 339B won / $243.75M; shares +11.7%", 11.7, "Stage2_promote_candidate", "Stage2-Actionable", {"stake_acquired_pct": 60, "deal_value_krw_bn": 339, "deal_value_usd_mn": 243.75}),
    Round302TriggerRecord("r7l15_hugel_T1", "r7_loop15_hugel_letybo_us_launch", "Stage2_product_launch", date(2025, 3, 1), "Letybo launched/arriving in U.S. market as FDA-approved neuromodulator and lower-cost Botox competitor", "price_data_unavailable_after_deep_search", "success_candidate_stage2", "Stage2", {"estimated_letybo_price_usd_per_unit": "9-12", "claimed_discount_pct_context": 30}),
    Round302TriggerRecord("r7l15_jeisys_T1", "r7_loop15_jeisys_archimed_aesthetic_device_ma", "event_premium_control_premium", date(2024, 9, 11), "ArchiMed acquires Jeisys Medical for roughly $742M; revenue +44% CAGR and adjusted pretax earnings +45% CAGR through FY2023", "price_data_unavailable_after_deep_search", "control_premium_not_operating_Green", "4B-watch", {"acquisition_value_usd_mn": 742, "revenue_cagr_through_fy2023_pct": 44, "adjusted_pretax_earnings_cagr_pct": 45}),
    Round302TriggerRecord("r7l15_samsungbioepis_T1", "r7_loop15_samsung_bioepis_amgen_patent_litigation", "4C-watch", date(2024, 8, 13), "Amgen sues Samsung Bioepis over 34 Prolia/Xgeva biosimilar patents, seeks to block manufacturing/sales", "price_data_unavailable_after_deep_search", "biosimilar_patent_litigation_4C_watch", "4C-watch", {"patents_asserted_count": 34, "prolia_us_sales_usd_bn": 2.7, "xgeva_us_sales_usd_bn": 1.5, "hard_4c_confirmed": False}),
)

ROUND302_CASE_CANDIDATES: tuple[Round302CaseCandidate, ...] = (
    Round302CaseCandidate("r7_loop15_alteogen_keytruda_qlex", "196170", "Alteogen", E2RArchetype.SC_FORMULATION_ROYALTY_STAGE2_TO_GREEN, (E2RArchetype.BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE, E2RArchetype.PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY), "success_candidate", "Stage3_Yellow_to_Green_candidate", "T2/T3/T4", "Stage3-Yellow_to_Green_candidate", "Stage3-Yellow_to_Green_candidate", date(2024, 1, 1), date(2024, 11, 19), date(2025, 3, 27), date(2025, 9, 19), None, False, ("SC_Keytruda_noninferiority", "launch_plan_Oct_2025", "expected_adoption_30_40pct", "FDA_approval_Keytruda_Qlex", "Qlex_Q1_2026_sales_128M_USD"), ("Alteogen_royalty_rate_visibility_missing", "commercial_royalty_recognition_missing", "patent_dispute_outcome_missing", "regional_launch_timing_missing", "Merck_switch_rate_actual_missing"), 1.8, None, {"t1_merck_event_return_pct": 1.8, "injection_time_minutes": "2-3", "iv_infusion_time_minutes": 30, "keytruda_2024_sales_usd_bn": 30, "expected_peak_adoption_pct": "30-40", "qlex_q1_2026_sales_usd_mn": 128, "alteogen_direct_ohlc_status": "price_data_unavailable_after_deep_search"}, "aligned", "Stage3_Yellow_to_Green_candidate", "true_rerating", "yellow_success", "Non-inferiority is Stage2; launch/adoption plan is Yellow; FDA approval plus early sales is Green candidate pending royalty and patent risk."),
    Round302CaseCandidate("r7_loop15_alteogen_halozyme_patent_watch", "196170", "Alteogen / Merck / Halozyme", E2RArchetype.SC_FORMULATION_PATENT_4C_WATCH, (E2RArchetype.PATENT_CHALLENGE_OVERLAY, E2RArchetype.PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY), "4b_watch", "4c_watch", "T0/T1", "4C-watch_overlay", "4C-watch", date(2025, 3, 5), None, None, date(2025, 3, 5), date(2025, 3, 5), False, ("Halozyme_patent_challenge", "Merck_patent_petitions", "Merck_no_launch_delay_statement"), ("launch_delay_confirmed_false", "injunction_not_confirmed", "patent_dispute_outcome_missing"), None, None, {"patent_counterparty": "Halozyme", "merck_patent_petitions": True, "launch_delay_confirmed": False, "merck_no_delay_statement": True, "hard_4c_confirmed": False}, "unknown", "4C_watch_not_hard", "thesis_break", "should_have_been_red", "Patent challenge is 4C-watch, but no hard 4C while launch delay or injunction is absent."),
    Round302CaseCandidate("r7_loop15_samsung_biologics_tariff_localization", "207940", "Samsung Biologics", E2RArchetype.BIOPHARMA_TARIFF_LOCALIZATION_STAGE2, (E2RArchetype.CDMO_LOCALIZATION_EVIDENCE_GOOD_PRICE_FAILED, E2RArchetype.BIO_CMO_US_LOCALIZATION_STAGE2), "success_candidate", "Stage2_policy_evidence_good_but_price_failed", "T0/T1", "Stage2_policy_to_evidence_good_but_price_failed", "Stage2", date(2025, 5, 21), date(2025, 5, 21), None, date(2025, 12, 22), None, False, ("biopharma_policy_support", "Samsung_Biologics_plus_6_23pct", "GSK_US_facility_280M_USD", "Rockville_60000L_capacity"), ("customer_transfer_missing", "facility_utilization_missing", "incremental_CDMO_order_missing", "margin_visibility_missing", "tariff_saving_quantification_missing"), 6.23, -0.4, {"pharma_sector_event_return_pct": 3.97, "samsung_biologics_event_return_pct": 6.23, "us_facility_acquisition_value_usd_mn": 280, "facility_capacity_liters": 60000, "facility_location": "Rockville_Maryland", "t1_samsung_biologics_return_pct": -0.4, "t1_kospi_return_pct": 2.0, "market_relative_return_pp": -2.4}, "evidence_good_but_price_failed", "Stage2_policy_to_evidence_good_but_price_failed", "policy_event_rerating", "stage2_watch_success", "Policy support is actionable; the later U.S. facility acquisition needs utilization and order conversion."),
    Round302CaseCandidate("r7_loop15_celltrion_us_factory_tariff_hedge", "068270", "Celltrion", E2RArchetype.BIOPHARMA_TARIFF_LOCALIZATION_STAGE2, (E2RArchetype.BIOSIMILAR_US_TARIFF_HEDGE_STAGE2, E2RArchetype.BIOPHARMA_US_FACTORY_TARIFF_HEDGE), "success_candidate", "success_candidate_stage2", "T1/T2/T3", "Stage2_localization", "Stage2_localization", date(2025, 5, 1), date(2025, 7, 29), None, None, None, False, ("US_factory_preferred_bidder", "planned_700B_KRW_investment", "ImClone_acquisition_330M_USD", "US_expansion_700B_KRW"), ("commercial_production_transfer_missing", "US_facility_utilization_missing", "tariff_saving_missing", "gross_margin_missing", "product_launch_timing_missing"), None, None, {"preferred_bidder_date": "2025-07-29", "planned_acquisition_operation_investment_krw_bn": 700, "imclone_acquisition_value_usd_mn": 330, "us_expansion_investment_krw_bn": 700, "us_expansion_investment_usd_mn": 478}, "aligned", "Stage2_localization_success_candidate", "unknown", "stage2_watch_success", "U.S. factory tariff hedge is Stage2; Green requires product transfer, utilization and margin."),
    Round302CaseCandidate("r7_loop15_sk_bioscience_idt_biologika", "302440", "SK Bioscience", E2RArchetype.VACCINE_CDMO_MA_STAGE2_ACTIONABLE, (E2RArchetype.VACCINE_CDMO_M_AND_A_STAGE2, E2RArchetype.VACCINE_CDMO_MA_EVENT_PREMIUM), "success_candidate", "Stage2_promote_candidate", "T1/T2", "Stage2-Actionable", "Stage2-Actionable", date(2024, 1, 1), date(2024, 6, 27), None, date(2024, 6, 27), None, False, ("IDT_Biologika_60pct_stake", "deal_value_339B_KRW", "deal_value_243_75M_USD", "event_return_plus_11_7pct", "first_major_MA_since_IPO"), ("integration_plan_missing", "CDMO_order_backlog_missing", "facility_utilization_missing", "margin_contribution_missing", "new_customer_wins_missing"), 11.7, None, {"stake_acquired_pct": 60, "deal_value_krw_bn": 339, "deal_value_usd_mn": 243.75, "event_return_pct": 11.7, "first_major_ma_since_ipo": True, "idt_remaining_stake_holder": "Klocke Gruppe 40%"}, "missed_due_to_score", "Stage2_Actionable_CDMO_MA", "event_premium", "stage2_watch_success", "Vaccine/CDMO M&A with +11.7% price response is Stage2-Actionable; Green requires backlog, utilization and margin."),
    Round302CaseCandidate("r7_loop15_hugel_letybo_us_launch", "145020", "Hugel", E2RArchetype.AESTHETIC_TOXIN_US_LAUNCH_STAGE2, (E2RArchetype.BOTULINUM_TOXIN_US_LAUNCH, E2RArchetype.AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2), "success_candidate", "success_candidate_stage2", "T0/T1", "Stage2_product_launch", "Stage2_product_launch", date(2024, 2, 1), date(2025, 3, 1), None, None, None, False, ("FDA_approval_glabellar_lines", "US_launch_context", "lower_cost_Botox_competitor", "estimated_price_9_12_USD_per_unit"), ("US_clinic_adoption_missing", "distributor_sellthrough_missing", "market_share_missing", "price_realization_missing", "margin_after_discount_missing"), None, None, {"fda_approval_context": "moderate-to-severe_glabellar_lines", "us_launch_context_date": "2025-03", "estimated_letybo_price_usd_per_unit": "9-12", "botox_price_usd_per_unit_context": "12-18", "claimed_discount_pct_context": 30}, "aligned", "Stage2_product_launch_not_Yellow", "unknown", "stage2_watch_success", "Aesthetic toxin approval/launch is Stage2; clinic adoption, sell-through and margin are needed for Yellow."),
    Round302CaseCandidate("r7_loop15_jeisys_archimed_aesthetic_device_ma", "287410", "Jeisys Medical", E2RArchetype.AESTHETIC_DEVICE_MA_CONTROL_PREMIUM, (E2RArchetype.AESTHETIC_EBD_GLOBAL_BUYOUT, E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT), "event_premium", "event_premium_control_premium", "T1/T2", "Stage2_structural_but_4B_control_premium", "Stage2_structural_but_4B_control_premium", date(2024, 1, 1), date(2024, 9, 11), None, date(2024, 9, 11), None, False, ("ArchiMed_acquisition_742M_USD", "EBD_market_2032e_16B_USD", "revenue_CAGR_44pct", "adjusted_pretax_earnings_CAGR_45pct"), ("delisting_process", "public_market_tracking_unavailable", "control_premium_dominates", "post_buyout_operating_data_unavailable"), None, None, {"acquisition_value_usd_mn": 742, "prior_close_price_krw": 12860, "global_ebd_market_prior_year_usd_bn": 4.5, "global_ebd_market_2032e_usd_bn": 16, "revenue_cagr_through_fy2023_pct": 44, "adjusted_pretax_earnings_cagr_pct": 45, "delisting_process": True}, "false_positive_score", "event_premium_control_premium_not_operating_Green", "event_premium", "false_yellow", "Aesthetic-device market is structural, but tender/delisting control premium dominates the public trigger."),
    Round302CaseCandidate("r7_loop15_samsung_bioepis_amgen_patent_litigation", "207940_readthrough/Samsung_Bioepis", "Samsung Bioepis / Amgen", E2RArchetype.BIOSIMILAR_PATENT_LITIGATION_4C_WATCH, (E2RArchetype.BIOSIMILAR_PATENT_LITIGATION, E2RArchetype.BIOSIMILAR_COMMERCIALIZATION), "4b_watch", "4c_watch", "T1", "4C-watch", "4C-watch", date(2024, 8, 13), None, None, date(2024, 8, 13), date(2024, 8, 13), False, ("Amgen_patent_lawsuit", "34_patents_asserted", "Prolia_Xgeva_biosimilars", "block_sale_manufacture_request"), ("patent_clearance_missing", "settlement_missing", "launch_delay_risk", "monetary_damages_risk"), None, None, {"litigation_counterparty": "Amgen", "patents_asserted_count": 34, "products": ["Prolia biosimilar", "Xgeva biosimilar"], "prolia_us_sales_usd_bn": 2.7, "xgeva_us_sales_usd_bn": 1.5, "requested_relief": ["block_making", "block_selling", "monetary_damages"], "hard_4c_confirmed": False}, "unknown", "biosimilar_patent_litigation_4C_watch", "thesis_break", "should_have_been_red", "Biosimilar approval or filing is not Green without patent clearance or settlement."),
    Round302CaseCandidate("r7_loop15_adel_sanofi_private_reference", "private_reference", "ADEL / Sanofi", E2RArchetype.PRIVATE_BIOTECH_LO_REFERENCE, (E2RArchetype.KOREAN_BIOTECH_TECH_EXPORT_STAGE2, E2RArchetype.BIOTECH_LICENSE_MILESTONE_PLATFORM), "event_premium", "private_reference", "T1", "LO_reference_not_KRX_case", "N/A_private", date(2025, 12, 15), None, None, None, None, False, ("Sanofi_partnership_1_04B_USD_total_value", "upfront_payment_80M_USD", "ADEL_Y01_early_stage_human_trials"), ("listed_price_anchor_absent", "private_company_reference_only", "trial_progress_pending", "milestone_probability_missing"), None, None, {"deal_value_usd_bn": 1.04, "upfront_payment_usd_mn": 80, "drug_candidate": "ADEL-Y01", "trial_stage": "early-stage human trials in U.S.", "listed_price_anchor": "N/A_private_company"}, "unknown", "private_reference_for_LO_total_value_vs_upfront", "unknown", "unknown", "Use as LO calibration reference only: total deal value must be separated from upfront and milestone probability."),
)


def round302_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(case.to_case_record() for case in ROUND302_CASE_CANDIDATES)


def round302_summary() -> dict[str, object]:
    return {
        "source_round": ROUND302_SOURCE_ROUND_PATH,
        "round_id": ROUND302_ANALYST_ROUND_ID,
        "large_sector": ROUND302_LARGE_SECTOR,
        "method": ROUND302_METHOD,
        "case_candidate_count": len(ROUND302_CASE_CANDIDATES),
        "trigger_count": len(ROUND302_TRIGGER_RECORDS),
        "stage2_actionable_candidate_count": 3,
        "stage3_yellow_candidate_count": 1,
        "stage3_green_candidate_count": 1,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 4,
        "stage4c_watch_count": 3,
        "hard_4c_case_count": 0,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "full_adjusted_ohlc_complete": False,
        "shadow_weight_only": True,
    }


def round302_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(case.as_row() for case in ROUND302_CASE_CANDIDATES)


def round302_trigger_rows() -> tuple[dict[str, str], ...]:
    return tuple(trigger.as_row() for trigger in ROUND302_TRIGGER_RECORDS)


def round302_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"requested_alias": key, "canonical_archetype": value} for key, value in ROUND302_REQUIRED_TARGET_ALIASES.items())


def round302_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND302_SHADOW_WEIGHT_ROWS)


def round302_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    up_points = {
        "fda_approval_to_launch_conversion": "+5",
        "actual_product_sales_after_approval": "+5",
        "royalty_recognition_visibility": "+5",
        "adoption_rate_guidance": "+4",
        "patent_litigation_clearance": "+5",
        "cdmo_order_backlog_utilization": "+5",
        "tariff_localization_margin_benefit": "+4",
        "ma_integration_and_utilization": "+4",
        "biosimilar_launch_settlement": "+5",
        "clinic_adoption_sellthrough": "+4",
    }
    down_points = {
        "fda_trial_result_only": "-4",
        "product_approval_without_revenue": "-3",
        "cdmo_capacity_headline_only": "-5",
        "factory_acquisition_without_utilization": "-4",
        "total_lo_value_without_upfront": "-5",
        "biosimilar_approval_without_patent_clearance": "-5",
        "aesthetic_launch_without_sellthrough": "-4",
        "policy_support_without_company_order": "-4",
    }
    rows = []
    for axis in ROUND302_SCORE_UP_AXES:
        rows.append({"axis": axis, "points": up_points[axis], "direction": "raise", "reason": "R7 healthcare trigger quality axis"})
    for axis in ROUND302_SCORE_DOWN_AXES:
        rows.append({"axis": axis, "points": down_points[axis], "direction": "lower", "reason": "R7 approval, capacity, LO, policy or launch headline blocker"})
    return tuple(rows)


def round302_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND302_SOURCE_ROUND_PATH,
        "round_id": ROUND302_ANALYST_ROUND_ID,
        "large_sector": ROUND302_LARGE_SECTOR,
        "method": ROUND302_METHOD,
        "summary": round302_summary(),
        "target_archetypes": dict(ROUND302_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND302_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND302_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND302_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND302_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND302_SCORE_UP_AXES),
        "score_down_axes": list(ROUND302_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND302_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND302_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_apply_round302_shadow_weights_to_production_scoring_yet",
            "do_not_use_round302_cases_as_candidate_generation_input",
            "do_not_treat_fda_factory_lo_or_launch_headline_as_green",
            "do_not_downgrade_stage_candidate_only_because_full_ohlc_is_missing",
        ],
    }


def render_round302_summary_markdown() -> str:
    summary = round302_summary()
    lines = [
        "# Round 302 R7 Loop 15 Bio/Healthcare/Medical Device Trigger Validation",
        "",
        "이번 라운드는 FDA 승인, CDMO 공장, LO, 의료기기 M&A를 한 덩어리로 보지 않고 trigger별로 분리한다.",
        "",
        "쉬운 예: FDA 승인은 제품이 문을 통과한 것이고, Green은 실제 환자/의사 채택과 매출 또는 로열티가 확인되는 단계다.",
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
        "stage3_yellow_candidate_count",
        "stage3_green_candidate_count",
        "stage3_green_confirmed_count",
        "stage4b_watch_count",
        "stage4c_watch_count",
        "hard_4c_case_count",
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
            "- Alteogen/Qlex는 non-inferiority에서 Stage2, launch/adoption plan에서 Yellow, FDA approval + early sales에서 Green candidate다.",
            "- Alteogen/Halozyme은 patent 4C-watch이며, launch delay나 injunction 전에는 hard 4C가 아니다.",
            "- Samsung Biologics와 Celltrion의 U.S. localization은 utilization, order, margin 전에는 Stage2다.",
            "- SK Bioscience/IDT는 M&A + +11.7% price reaction으로 Stage2-Actionable이다.",
            "- Hugel/Letybo는 FDA-approved U.S. launch지만 clinic adoption, sell-through, margin 전에는 Yellow가 아니다.",
            "- Jeisys/ArchiMed는 structural aesthetic-device evidence가 있어도 public trigger는 control-premium M&A다.",
            "- Samsung Bioepis/Amgen은 biosimilar patent 4C-watch다.",
            "- ADEL/Sanofi는 private reference이며 total LO value와 upfront를 분리하는 데만 쓴다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round302_trigger_grid_markdown() -> str:
    lines = [
        "# Round 302 Trigger Grid",
        "",
        "| trigger_id | case_id | date | type | outcome | promote_to | evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for trigger in ROUND302_TRIGGER_RECORDS:
        lines.append(
            f"| {trigger.trigger_id} | {trigger.case_id} | {trigger.trigger_date.isoformat()} | {trigger.trigger_type} | {trigger.trigger_outcome_label} | {trigger.promote_to} | {trigger.evidence_available} |"
        )
    return "\n".join(lines) + "\n"


def render_round302_stage_rules_markdown() -> str:
    lines = ["# Round 302 Stage Rules", "", "Do not apply these weights to production scoring yet.", "", "## Stage2-Actionable", ""]
    lines.extend(f"- {rule}" for rule in ROUND302_STAGE2_ACTIONABLE_RULES)
    lines.extend(["", "## Stage3-Yellow", ""])
    lines.extend(f"- {rule}" for rule in ROUND302_STAGE3_YELLOW_RULES)
    lines.extend(["", "## Stage3-Green", ""])
    lines.extend(f"- {rule}" for rule in ROUND302_STAGE3_GREEN_RULES)
    lines.extend(["", "## Green Blockers", ""])
    lines.extend(f"- {rule}" for rule in ROUND302_GREEN_BLOCKERS)
    return "\n".join(lines) + "\n"


def render_round302_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 302 4B/4C Review",
        "",
        "이번 라운드에서 확정 Green과 hard 4C는 없다. approval, capacity, LO headline의 4B/4C-watch를 분리한다.",
        "",
        "## 4B Watch",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND302_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## 4C Gates", ""])
    lines.extend(f"- {item}" for item in ROUND302_HARD_4C_GATES)
    return "\n".join(lines) + "\n"


def render_round302_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round 302 Price Validation Plan",
            "",
            "- reported_event_anchor_not_full_ohlc 상태를 유지한다.",
            "- full adjusted OHLC가 없다는 이유로 Stage2/Yellow/Green 후보를 강등하지 않는다.",
            "- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.",
            "- 다음 단계에서는 trigger date 기준 30/90/180일 MFE/MAE, below-entry, launch adoption, royalty recognition, utilization, settlement, clinic sell-through를 채운다.",
            "",
        ]
    )


def write_round302_r7_loop15_reports(
    *,
    output_directory: str | Path = ROUND302_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND302_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND302_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND302_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND302_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round302_case_records(), cases_path),
        "triggers": write_round302_triggers(triggers_path),
        "audit": _write_json(round302_audit_payload(), audit_path),
        "weight_profile": _write_csv(round302_shadow_weight_rows(), weight_profile_path),
        "summary": output / "round302_r7_loop15_trigger_validation_summary.md",
        "case_matrix": output / "round302_r7_loop15_case_matrix.csv",
        "trigger_grid": output / "round302_r7_loop15_trigger_grid.csv",
        "target_aliases": output / "round302_r7_loop15_target_aliases.csv",
        "score_adjustments": output / "round302_r7_loop15_score_adjustments.csv",
        "shadow_weights": output / "round302_r7_loop15_shadow_weights.csv",
        "stage_rules": output / "round302_r7_loop15_stage_rules.md",
        "trigger_grid_md": output / "round302_r7_loop15_trigger_grid.md",
        "price_validation_plan": output / "round302_r7_loop15_price_validation_plan.md",
        "stage4b_4c_review": output / "round302_r7_loop15_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round302_summary_markdown(), encoding="utf-8")
    _write_csv(round302_case_rows(), paths["case_matrix"])
    _write_csv(round302_trigger_rows(), paths["trigger_grid"])
    _write_csv(round302_target_alias_rows(), paths["target_aliases"])
    _write_csv(round302_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round302_shadow_weight_rows(), paths["shadow_weights"])
    paths["stage_rules"].write_text(render_round302_stage_rules_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round302_trigger_grid_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round302_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round302_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def write_round302_triggers(path: str | Path = ROUND302_DEFAULT_TRIGGERS_PATH) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(trigger.as_dict(), ensure_ascii=False, sort_keys=True) for trigger in ROUND302_TRIGGER_RECORDS]
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
