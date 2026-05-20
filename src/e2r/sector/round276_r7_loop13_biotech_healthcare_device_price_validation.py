"""Round-276 R7 Loop-13 biotech/healthcare/device price-validation pack.

This module converts ``docs/round/round_276.md`` into calibration-only case
records and reports. It does not change production scoring, candidate
generation, or StageClassifier thresholds.

Easy example: FDA approval is a strong Stage 2 signal, but it is not
Stage 3-Green until prescription ramp, royalty/milestone cashflow, commercial
launch, margin, and FCF are visible.
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
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector


ROUND276_SOURCE_ROUND_PATH = "docs/round/round_276.md"
ROUND276_ANALYST_ROUND_ID = "round_204"
ROUND276_LARGE_SECTOR = Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE.value
ROUND276_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round276_r7_loop13_biotech_healthcare_device_price_validation"
ROUND276_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_loop13_round276.jsonl"
ROUND276_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round276_r7_loop13_biotech_healthcare_device_price_validation_audit.json"

ROUND276_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL": E2RArchetype.KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL.value,
    "PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY": E2RArchetype.PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY.value,
    "CDMO_US_TARIFF_HEDGE_STAGE2": E2RArchetype.CDMO_US_TARIFF_HEDGE_STAGE2.value,
    "BIOPHARMA_US_FACTORY_TARIFF_HEDGE": E2RArchetype.BIOPHARMA_US_FACTORY_TARIFF_HEDGE.value,
    "VACCINE_CDMO_M_AND_A_STAGE2": E2RArchetype.VACCINE_CDMO_M_AND_A_STAGE2.value,
    "AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT": E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT.value,
    "BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM": E2RArchetype.BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM.value,
    "VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE": E2RArchetype.VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE.value,
}

ROUND276_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "actual_prescription_ramp_confirmed",
    "royalty_milestone_cashflow_confirmed",
    "commercial_launch_execution_confirmed",
    "cdmo_capacity_utilization_confirmed",
    "customer_transfer_success_confirmed",
    "regulatory_quality_clearance_confirmed",
    "reimbursement_and_access_confirmed",
    "device_clinic_utilization_confirmed",
    "recurring_consumables_or_service_revenue_confirmed",
    "ex_policy_margin_fcf_confirmed",
    "price_path_after_evidence",
)

ROUND276_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "FDA_approval_without_sales_bridge",
    "platform_tech_without_royalty_cash",
    "CDMO_facility_acquisition_only",
    "policy_tariff_support_only",
    "M&A_without_utilization",
    "vaccine_procurement_without_demand",
    "device_takeout_not_tradeable",
    "patent_or_CRL_overhang",
)

ROUND276_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "FDA_approval_global_approval_headline_rerating",
    "SC_Keytruda_platform_enzyme_story_before_royalty",
    "CDMO_US_facility_acquisition_before_utilization",
    "M&A_announcement_plus_10pct_before_order_book",
    "policy_support_sector_rally_3_to_6pct",
    "medical_device_takeout_peer_valuation_overheat",
    "vaccine_sovereignty_narrative_before_administered_demand",
)

ROUND276_HARD_4C_GATES: tuple[str, ...] = (
    "FDA_CRL_or_approval_rejection",
    "clinical_hold_or_serious_safety_event",
    "CMC_or_manufacturing_inspection_failure",
    "patent_injunction_or_launch_delay",
    "royalty_or_milestone_non_realization",
    "CDMO_facility_underutilization",
    "vaccine_demand_collapse",
    "device_recall_or_safety_issue",
    "reimbursement_denial",
    "tariff_economics_negative_despite_US_facility",
)

ROUND276_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "commercialization_or_utilization_anchor",
    "regulatory_quality_or_patent_gate",
    "demand_or_administered_dose_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round276ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round276ShadowWeightRow:
    archetype: E2RArchetype
    prescription_ramp: int
    royalty_milestone_cashflow: int
    commercial_launch: int
    cdmo_utilization: int
    customer_transfer: int
    regulatory_quality: int
    reimbursement_access: int
    device_clinic_utilization: int
    recurring_consumables_service: int
    ex_policy_margin_fcf: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "prescription_ramp": _signed(self.prescription_ramp),
            "royalty_milestone_cashflow": _signed(self.royalty_milestone_cashflow),
            "commercial_launch": _signed(self.commercial_launch),
            "cdmo_utilization": _signed(self.cdmo_utilization),
            "customer_transfer": _signed(self.customer_transfer),
            "regulatory_quality": _signed(self.regulatory_quality),
            "reimbursement_access": _signed(self.reimbursement_access),
            "device_clinic_utilization": _signed(self.device_clinic_utilization),
            "recurring_consumables_service": _signed(self.recurring_consumables_service),
            "ex_policy_margin_fcf": _signed(self.ex_policy_margin_fcf),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round276DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round276CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    round_case_type: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    stage3_decision: str
    stage4b_status: str
    hard_4c_confirmed: bool
    hard_4c_reference_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    event_mfe_pct: float | None
    event_mae_pct: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, object]
    score_price_alignment: str
    round_alignment_label: str
    rerating_result: str
    round_rerating_label: str
    stage_failure_type: str
    round_stage_failure_label: str
    price_validation_status: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND276_SCORE_ADJUSTMENTS: tuple[Round276ScoreAdjustment, ...] = (
    Round276ScoreAdjustment("actual_prescription_ramp", 5, "raise", "신약 Green은 승인보다 실제 처방 ramp가 중요하다."),
    Round276ScoreAdjustment("royalty_milestone_cashflow", 5, "raise", "플랫폼/라이선스는 royalty와 milestone 현금흐름으로 닫혀야 한다."),
    Round276ScoreAdjustment("commercial_launch_execution", 5, "raise", "승인 이후 출시 실행과 접근성이 확인되어야 한다."),
    Round276ScoreAdjustment("CDMO_capacity_utilization", 5, "raise", "CDMO 시설은 capacity가 아니라 utilization이 Green 근거다."),
    Round276ScoreAdjustment("customer_transfer_success", 5, "raise", "미국 공장은 고객 이전과 제품 이전이 확인되어야 한다."),
    Round276ScoreAdjustment("regulatory_quality_clearance", 5, "raise", "CMC/FDA inspection과 patent gate를 통과해야 한다."),
    Round276ScoreAdjustment("reimbursement_and_access", 5, "raise", "처방·시술은 reimbursement/access가 있어야 매출로 전환된다."),
    Round276ScoreAdjustment("device_clinic_utilization", 5, "raise", "의료기기는 clinic utilization이 실제 수요다."),
    Round276ScoreAdjustment("recurring_consumables_or_service", 4, "raise", "장비 판매보다 반복 소모품/서비스 매출이 질을 만든다."),
    Round276ScoreAdjustment("ex_policy_margin_FCF", 5, "raise", "정책 지원 후에도 margin과 FCF로 닫혀야 한다."),
    Round276ScoreAdjustment("FDA_approval_without_sales_bridge", -4, "lower", "FDA approval만으로 Stage 3-Green을 만들지 않는다."),
    Round276ScoreAdjustment("platform_tech_without_royalty_cash", -5, "lower", "플랫폼 기술 headline은 royalty cash 전에는 option이다."),
    Round276ScoreAdjustment("CDMO_facility_acquisition_only", -5, "lower", "공장 인수만으로 utilization과 margin을 발명하지 않는다."),
    Round276ScoreAdjustment("policy_tariff_support_only", -5, "lower", "정책지원은 company margin bridge 전에는 event premium이다."),
    Round276ScoreAdjustment("M&A_without_utilization", -5, "lower", "M&A pop은 order book/utilization 전에는 4B-watch다."),
    Round276ScoreAdjustment("vaccine_procurement_without_demand", -5, "lower", "정부 구매가 실제 접종 수요를 뜻하지 않는다."),
    Round276ScoreAdjustment("device_takeout_not_tradeable", -3, "lower", "take-private benchmark는 상장 Stage 3 추적이 어렵다."),
    Round276ScoreAdjustment("patent_or_CRL_overhang", -5, "lower", "CRL/patent overhang은 launch ramp를 막을 수 있다."),
)


ROUND276_SHADOW_WEIGHT_ROWS: tuple[Round276ShadowWeightRow, ...] = (
    Round276ShadowWeightRow(E2RArchetype.KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL, 5, 5, 5, 0, 0, 5, 5, 0, 0, 5, -4, 4, 5, "Yuhan/lazertinib needs royalty/milestone cash and prescription ramp after FDA approval."),
    Round276ShadowWeightRow(E2RArchetype.PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY, 3, 5, 5, 0, 0, 5, 4, 0, 0, 5, -5, 5, 5, "Alteogen/SC Keytruda needs royalty cashflow, launch adoption and patent clearance."),
    Round276ShadowWeightRow(E2RArchetype.CDMO_US_TARIFF_HEDGE_STAGE2, 0, 0, 3, 5, 5, 5, 0, 0, 0, 5, -5, 4, 4, "Samsung Bio U.S. facility needs utilization, customer transfer, FDA inspection and margin."),
    Round276ShadowWeightRow(E2RArchetype.BIOPHARMA_US_FACTORY_TARIFF_HEDGE, 0, 0, 3, 5, 5, 5, 0, 0, 0, 5, -5, 4, 4, "Celltrion U.S. factory needs product transfer, tariff saving, utilization and FCF."),
    Round276ShadowWeightRow(E2RArchetype.VACCINE_CDMO_M_AND_A_STAGE2, 0, 0, 3, 5, 5, 5, 0, 0, 1, 5, -5, 5, 4, "SK Bioscience/IDT M&A needs order book, integration and utilization."),
    Round276ShadowWeightRow(E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT, 0, 0, 4, 0, 0, 4, 3, 5, 5, 5, -3, 4, 3, "Jeisys is device benchmark; peer scoring needs clinic utilization and consumables/service revenue."),
    Round276ShadowWeightRow(E2RArchetype.BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM, 0, 0, 2, 3, 2, 3, 0, 0, 0, 5, -5, 5, 4, "Policy support rally is not Green without tariff/margin bridge."),
    Round276ShadowWeightRow(E2RArchetype.VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE, 0, 0, 2, 2, 0, 4, 3, 0, 0, 5, 0, 3, 5, "SkyCovione shows approval/procurement without administered demand can fail."),
)


ROUND276_DEEP_SUB_ARCHETYPES: tuple[Round276DeepSubArchetype, ...] = (
    Round276DeepSubArchetype("신약 글로벌 승인", E2RArchetype.KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL, ("Yuhan", "lazertinib", "Rybrevant", "Lazcluze", "EGFR NSCLC", "prescription ramp")),
    Round276DeepSubArchetype("플랫폼 기술 royalty", E2RArchetype.PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY, ("Alteogen", "hyaluronidase", "SC Keytruda", "Merck", "Halozyme", "royalty")),
    Round276DeepSubArchetype("CDMO U.S. tariff hedge", E2RArchetype.CDMO_US_TARIFF_HEDGE_STAGE2, ("Samsung Biologics", "GSK Rockville", "60,000L", "FDA inspection", "utilization")),
    Round276DeepSubArchetype("Biopharma U.S. factory", E2RArchetype.BIOPHARMA_US_FACTORY_TARIFF_HEDGE, ("Celltrion", "ImClone", "Eli Lilly", "tariff hedge", "product transfer")),
    Round276DeepSubArchetype("Vaccine CDMO M&A", E2RArchetype.VACCINE_CDMO_M_AND_A_STAGE2, ("SK Bioscience", "IDT Biologika", "order book", "fill-finish", "utilization")),
    Round276DeepSubArchetype("Aesthetic device takeout", E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT, ("Jeisys", "ArchiMed", "EBD", "take-private", "clinic utilization")),
    Round276DeepSubArchetype("Biopharma policy rally", E2RArchetype.BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM, ("pharma sector", "tariff support", "Samsung Biologics", "Celltrion", "margin bridge")),
    Round276DeepSubArchetype("Vaccine demand hard reference", E2RArchetype.VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE, ("SkyCovione", "10M doses", "3,787 shots", "production suspended", "demand collapse")),
)


ROUND276_CASE_CANDIDATES: tuple[Round276CaseCandidate, ...] = (
    Round276CaseCandidate(
        case_id="r7_loop13_yuhan_lazertinib_global_fda_approval",
        symbol="000100",
        company_name="Yuhan / lazertinib / J&J Rybrevant combo",
        primary_archetype=E2RArchetype.KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL,
        secondary_archetypes=(E2RArchetype.KOREAN_NEW_DRUG_GLOBAL_APPROVAL, E2RArchetype.MANUFACTURING_INSPECTION_CRL_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate / FDA approval Stage 2",
        stage1_date=date(2024, 8, 20),
        stage2_date=date(2024, 8, 20),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 16),
        stage3_decision="fda_approval_is_stage2_until_royalty_milestone_cashflow_prescription_ramp_launch_and_margin_confirm",
        stage4b_status="royalty-ramp-watch",
        hard_4c_confirmed=False,
        hard_4c_reference_confirmed=False,
        evidence_fields=("fda_approval_rybrevant_lazertinib_first_line_egfr_nsclc", "egfr_mutation_share_us_nsclc_10_15pct", "jnj_expected_rybrevant_peak_sales_above_5bn_usd", "phase3_risk_reduction_30pct", "trial_patient_count_1074"),
        red_flag_fields=("FDA_approval_without_sales_bridge", "royalty_milestone_cashflow_unconfirmed", "prescription_ramp_unconfirmed", "subcutaneous_rybrevant_crl_manufacturing_inspection_watch"),
        price_data_source="Reuters / MarketWatch FDA approval and CRL anchors",
        reported_price_anchor="J&J Rybrevant + lazertinib FDA approval; Rybrevant peak-sales expectation above $5B",
        reported_return_anchor="Yuhan full OHLC unavailable; subcutaneous Rybrevant CRL was manufacturing-inspection related",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fda_approval_date": "2024-08-20", "approved_combo": "Rybrevant + lazertinib / Lazcluze", "indication": "first-line EGFR-mutated NSCLC", "egfr_mutation_share_us_nsclc_pct": "10-15", "jnj_expected_rybrevant_peak_sales_usd_bn": 5.0, "marketwatch_phase3_risk_reduction_pct": 30.0, "trial_patient_count_marketwatch": 1074, "subcutaneous_rybrevant_crl_date": "2024-12-16", "crl_cause": "pre-approval manufacturing facility inspection observations", "additional_clinical_studies_requested": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_price_data_unavailable",
        rerating_result="unknown",
        round_rerating_label="Korean_origin_drug_global_approval_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="FDA_approval_not_royalty_cashflow_green",
        price_validation_status="yuhan_stock_ohlc_unavailable_after_deep_search",
        notes="FDA approval is strong Stage 2; Green requires royalty/milestone cashflow and prescription ramp.",
    ),
    Round276CaseCandidate(
        case_id="r7_loop13_alteogen_merck_sc_keytruda_platform",
        symbol="196170",
        company_name="Alteogen / Merck SC Keytruda enzyme",
        primary_archetype=E2RArchetype.PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY,
        secondary_archetypes=(E2RArchetype.BIO_PLATFORM_ROYALTY_CONVERSION, E2RArchetype.PATENT_CHALLENGE_OVERLAY),
        case_type="success_candidate",
        round_case_type="structural_success_candidate + 4B-watch + 4C-watch",
        stage1_date=date(2024, 11, 19),
        stage2_date=date(2025, 3, 27),
        stage3_date=None,
        stage4b_date=date(2025, 3, 27),
        stage4c_date=date(2025, 3, 27),
        stage3_decision="platform_option_is_stage2_until_royalty_cashflow_launch_adoption_patent_clearance_and_exclusivity_confirm",
        stage4b_status="4B-watch/platform-premium-before-royalty",
        hard_4c_confirmed=False,
        hard_4c_reference_confirmed=False,
        evidence_fields=("keytruda_2024_sales_nearly_30bn_usd", "sc_keytruda_expected_adoption_30_40pct", "sc_injection_time_2_3_minutes", "iv_infusion_time_30_minutes", "fda_decision_target_2025_09_23", "planned_us_launch_2025_10_01"),
        red_flag_fields=("platform_tech_without_royalty_cash", "patent_or_CRL_overhang", "halozyme_patent_challenge_watch", "royalty_cashflow_unconfirmed", "launch_adoption_unconfirmed"),
        price_data_source="Reuters / WSJ SC Keytruda trial, launch and patent anchors",
        reported_price_anchor="Keytruda 2024 sales nearly $30B; SC adoption expected 30~40%",
        reported_return_anchor="Merck premarket +1.8% on non-inferiority; Alteogen full OHLC unavailable",
        event_mfe_pct=1.8,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"keytruda_2024_sales_usd_bn": 30.0, "sc_keytruda_expected_adoption_pct": "30-40", "sc_injection_time_minutes": "2-3", "iv_infusion_time_minutes": 30.0, "time_reduction_low_pct": 90.0, "fda_decision_target": "2025-09-23", "planned_us_launch_date": "2025-10-01", "merck_premarket_reaction_to_noninferiority_pct": 1.8, "wsj_sc_keytruda_sales_prediction_usd_bn": 6.0, "patent_challenge_watch": "Halozyme"},
        score_price_alignment="unknown",
        round_alignment_label="structural_success_candidate_but_4B_and_patent_watch",
        rerating_result="unknown",
        round_rerating_label="platform_enzyme_royalty_optionality",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="platform_option_not_royalty_cashflow_green",
        price_validation_status="alteogen_stock_ohlc_unavailable_after_deep_search",
        notes="Platform optionality is large, but royalty cashflow, patent clearance and launch adoption are required.",
    ),
    Round276CaseCandidate(
        case_id="r7_loop13_samsung_biologics_gsk_rockville_facility",
        symbol="207940",
        company_name="Samsung Biologics",
        primary_archetype=E2RArchetype.CDMO_US_TARIFF_HEDGE_STAGE2,
        secondary_archetypes=(E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY, E2RArchetype.MANUFACTURING_INSPECTION_CRL_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate + evidence_good_but_price_failed",
        stage1_date=date(2025, 5, 21),
        stage2_date=date(2025, 12, 22),
        stage3_date=None,
        stage4b_date=date(2025, 12, 22),
        stage4c_date=date(2025, 12, 22),
        stage3_decision="facility_acquisition_is_stage2_until_utilization_customer_transfer_fda_inspection_margin_and_fcf_confirm",
        stage4b_status="4B-watch/us-facility-theme-before-utilization",
        hard_4c_confirmed=False,
        hard_4c_reference_confirmed=False,
        evidence_fields=("gsk_rockville_facility_acquisition_280mn_usd", "drug_substance_capacity_60000_liters", "human_genome_sciences_100pct_stake", "expected_close_end_q1_2026"),
        red_flag_fields=("CDMO_facility_acquisition_only", "facility_utilization_unconfirmed", "customer_transfer_unconfirmed", "relative_underperformance_vs_kospi", "fda_inspection_watch"),
        price_data_source="Reuters GSK facility acquisition and sector-support anchors",
        reported_price_anchor="$280M facility acquisition; 60,000L drug-substance capacity",
        reported_return_anchor="Samsung Biologics -0.4% while KOSPI +2.0%; relative -2.4pp",
        event_mfe_pct=None,
        event_mae_pct=-0.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"facility_acquisition_usd_mn": 280.0, "facility_location": "Rockville, Maryland", "acquired_entity": "Human Genome Sciences Inc.", "stake_acquired_pct": 100.0, "drug_substance_capacity_liters": 60000, "expected_close": "around end-Q1 2026", "event_mae_pct": -0.4, "kospi_same_context_pct": 2.0, "relative_underperformance_pp": -2.4, "facility_utilization_confirmed": False, "customer_transfer_confirmed": False},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="unknown",
        round_rerating_label="CDMO_US_tariff_hedge_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="facility_acquisition_not_utilization_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="U.S. facility is Stage 2; utilization, customer transfer, FDA inspection, margin and FCF are required.",
    ),
    Round276CaseCandidate(
        case_id="r7_loop13_celltrion_us_factory_tariff_hedge",
        symbol="068270",
        company_name="Celltrion",
        primary_archetype=E2RArchetype.BIOPHARMA_US_FACTORY_TARIFF_HEDGE,
        secondary_archetypes=(E2RArchetype.BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING, E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY),
        case_type="success_candidate",
        round_case_type="success_candidate / U.S. factory tariff hedge",
        stage1_date=date(2025, 5, 1),
        stage2_date=date(2025, 7, 29),
        stage3_date=None,
        stage4b_date=date(2025, 11, 19),
        stage4c_date=date(2025, 11, 19),
        stage3_decision="factory_acquisition_and_expansion_are_stage2_until_product_transfer_utilization_tariff_saving_margin_and_fcf_confirm",
        stage4b_status="4B-watch/tariff-hedge-before-margin",
        hard_4c_confirmed=False,
        hard_4c_reference_confirmed=False,
        evidence_fields=("preferred_bidder_investment_plan_700bn_krw", "imclone_acquisition_330mn_usd", "us_factory_expansion_up_to_700bn_krw", "us_pharma_tariff_risk"),
        red_flag_fields=("CDMO_facility_acquisition_only", "product_transfer_unconfirmed", "utilization_unconfirmed", "margin_unconfirmed", "tariff_economics_unconfirmed"),
        price_data_source="Reuters Celltrion U.S. factory acquisition and expansion anchors",
        reported_price_anchor="ImClone acquisition $330M; U.S. factory expansion up to 700B KRW",
        reported_return_anchor="Product transfer, utilization and margin are not confirmed",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"preferred_bidder_investment_plan_krw_bn": 700.0, "possible_additional_investment_krw_bn": "300-700", "imclone_acquisition_usd_mn": 330.0, "us_factory_expansion_max_krw_bn": 700.0, "us_factory_expansion_max_usd_mn": 478.17, "tariff_driver": "U.S. pharmaceutical tariff risk", "product_transfer_confirmed": False, "utilization_confirmed": False, "margin_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_price_data_unavailable",
        rerating_result="unknown",
        round_rerating_label="biopharma_US_factory_tariff_hedge_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="acquisition_expansion_not_product_transfer_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Factory acquisition and expansion are Stage 2; product transfer, utilization, tariff saving and FCF are required.",
    ),
    Round276CaseCandidate(
        case_id="r7_loop13_sk_bioscience_idt_biologika_cdmomna",
        symbol="302440",
        company_name="SK Bioscience / IDT Biologika",
        primary_archetype=E2RArchetype.VACCINE_CDMO_M_AND_A_STAGE2,
        secondary_archetypes=(E2RArchetype.VACCINE_CMO_RESTRUCTURING, E2RArchetype.CMO_M_AND_A_TRANSITION),
        case_type="success_candidate",
        round_case_type="success_candidate + event_premium",
        stage1_date=date(2024, 6, 27),
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=date(2024, 6, 27),
        stage4c_date=None,
        stage3_decision="vaccine_cdmo_mna_is_stage2_until_order_book_utilization_integration_margin_and_fcf_confirm",
        stage4b_status="4B-watch/11.7pct-mna-pop-before-utilization",
        hard_4c_confirmed=False,
        hard_4c_reference_confirmed=False,
        evidence_fields=("idt_stake_acquired_60pct", "deal_value_339bn_krw", "deal_value_243_75mn_usd", "klocke_remaining_stake_40pct", "sk_bioscience_event_mfe_11_7pct"),
        red_flag_fields=("M&A_without_utilization", "order_book_unconfirmed", "utilization_unconfirmed", "post_covid_demand_reset", "integration_margin_unconfirmed"),
        price_data_source="Reuters SK Bioscience / IDT Biologika deal anchor",
        reported_price_anchor="60% IDT stake for 339B KRW / $243.75M",
        reported_return_anchor="SK Bioscience shares +11.7% in morning trading",
        event_mfe_pct=11.7,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"idt_stake_acquired_pct": 60.0, "deal_value_krw_bn": 339.0, "deal_value_usd_mn": 243.75, "klocke_remaining_stake_pct": 40.0, "ipo_context": "first_major_M&A_since_2021_IPO", "ipo_raise_2021_usd_bn": 1.33, "event_mfe_pct": 11.7, "order_book_confirmed": False, "utilization_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="vaccine_CDMO_MA_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="acquisition_not_utilization_revenue_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="European CDMO acquisition is Stage 2; order book, integration, utilization and margin are required.",
    ),
    Round276CaseCandidate(
        case_id="r7_loop13_jeisys_medical_archimed_aesthetic_device_takeout",
        symbol="Jeisys_formerly_public",
        company_name="Jeisys Medical",
        primary_archetype=E2RArchetype.AESTHETIC_MEDICAL_DEVICE_PE_TAKEOUT,
        secondary_archetypes=(E2RArchetype.AESTHETIC_EBD_GLOBAL_BUYOUT, E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT),
        case_type="success_candidate",
        round_case_type="success_candidate + takeout event",
        stage1_date=date(2024, 6, 1),
        stage2_date=date(2024, 9, 11),
        stage3_date=None,
        stage4b_date=date(2024, 9, 11),
        stage4c_date=None,
        stage3_decision="take_private_and_pe_validation_are_stage2_benchmark_not_tradeable_stage3",
        stage4b_status="4B-watch/take-private-peer-validation",
        hard_4c_confirmed=False,
        hard_4c_reference_confirmed=False,
        evidence_fields=("archimed_take_private_value_742mn_usd", "pre_delisting_close_12860_krw", "revenue_cagr_44pct", "adjusted_pretax_earnings_cagr_45pct", "global_ebd_market_growth_to_2032"),
        red_flag_fields=("device_takeout_not_tradeable", "listed_status_delisting_process", "clinic_utilization_unconfirmed", "recurring_consumables_service_unconfirmed"),
        price_data_source="WSJ Jeisys / ArchiMed take-private anchor",
        reported_price_anchor="Jeisys close 12,860 KRW before delisting process; ArchiMed take-private value about $742M",
        reported_return_anchor="Revenue CAGR 44%, adjusted pretax earnings CAGR 45%; tradable Stage 3 unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=12860.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"take_private_value_usd_mn": 742.0, "pre_delisting_close_price_krw": 12860.0, "revenue_fy2023_usd_mn": 107.0, "revenue_cagr_3y_pct": 44.0, "adjusted_pretax_earnings_fy2023_usd_mn": 31.0, "adjusted_pretax_earnings_cagr_3y_pct": 45.0, "pretax_margin_fy2023_pct": 29.0, "global_ebd_market_previous_year_usd_bn": 4.5, "global_ebd_market_2032_usd_bn": 16.0, "global_ebd_market_growth_to_2032_pct": 255.6, "listed_status_after_deal": "delisting_process"},
        score_price_alignment="aligned",
        round_alignment_label="success_candidate_takeout_event",
        rerating_result="event_premium",
        round_rerating_label="aesthetic_medical_device_revenue_earnings_benchmark",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="take_private_not_tradeable_stage3",
        price_validation_status="reported_takeout_anchor_not_full_ohlc",
        notes="Real device benchmark, but take-private means not a tradable Stage 3 row.",
    ),
    Round276CaseCandidate(
        case_id="r7_loop13_biopharma_tariff_support_policy_rally",
        symbol="207940/068270/pharma_sector",
        company_name="Samsung Biologics / Celltrion / Korean pharma sector",
        primary_archetype=E2RArchetype.BIOPHARMA_POLICY_RALLY_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.BIOPHARMA_POLICY_TARIFF_RELIEF, E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY),
        case_type="event_premium",
        round_case_type="event_premium + policy_relief",
        stage1_date=date(2025, 5, 20),
        stage2_date=date(2025, 5, 21),
        stage3_date=None,
        stage4b_date=date(2025, 5, 21),
        stage4c_date=date(2025, 5, 21),
        stage3_decision="policy_support_and_sector_rally_are_event_premium_until_tariff_exemption_company_margin_bridge_product_demand_and_fcf_confirm",
        stage4b_status="4B-watch/policy-support-sector-rally",
        hard_4c_confirmed=False,
        hard_4c_reference_confirmed=False,
        evidence_fields=("kospi_event_return_0_99pct", "pharma_sector_return_3_97pct", "samsung_biologics_return_6_23pct", "celltrion_return_0_35pct", "pharmaceutical_exports_2024_9_59bn_usd", "us_export_share_16pct"),
        red_flag_fields=("policy_tariff_support_only", "company_margin_bridge_unconfirmed", "tariff_exemption_unconfirmed", "sector_rally_not_company_green"),
        price_data_source="Reuters Korea market / policy-support anchors",
        reported_price_anchor="Pharma sector +3.97%; Samsung Biologics +6.23%; Celltrion +0.35%",
        reported_return_anchor="Policy relief, not company-level Green evidence",
        event_mfe_pct=3.97,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kospi_event_mfe_pct": 0.99, "kospi_event_close": 2627.63, "pharma_sector_mfe_pct": 3.97, "samsung_biologics_mfe_pct": 6.23, "celltrion_mfe_pct": 0.35, "foreign_net_buy_krw_bn": 113.7, "pharmaceutical_exports_2024_usd_bn": 9.59, "us_export_share_pct": 16.0, "implied_us_pharma_exports_2024_usd_bn": 1.53, "tariff_exemption_confirmed": False, "company_margin_bridge_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_policy_relief",
        rerating_result="event_premium",
        round_rerating_label="biopharma_tariff_support_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="policy_relief_not_company_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Policy support is relief, not Green; company margin and FCF bridge are required.",
    ),
    Round276CaseCandidate(
        case_id="r7_loop13_sk_bioscience_skycovione_demand_collapse_reference",
        symbol="302440_reference",
        company_name="SK Bioscience / SkyCovione",
        primary_archetype=E2RArchetype.VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE,
        secondary_archetypes=(E2RArchetype.APPROVAL_ONLY_NOT_COMMERCIALIZATION, E2RArchetype.COMMERCIALIZATION_FAILURE_OVERLAY),
        case_type="failed_rerating",
        round_case_type="vaccine demand-collapse hard reference",
        stage1_date=date(2022, 6, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2022, 11, 1),
        stage3_decision="approval_and_government_procurement_did_not_become_administered_demand",
        stage4b_status="sector-hard-reference/not-direct-hard-4C",
        hard_4c_confirmed=False,
        hard_4c_reference_confirmed=True,
        evidence_fields=("government_purchase_10mn_doses", "released_to_hospitals_600000_doses", "administered_shots_3787", "production_suspended_due_low_demand", "eu_application_withdrawn", "who_eul_delisted"),
        red_flag_fields=("vaccine_procurement_without_demand", "vaccine_demand_collapse", "production_suspended", "unused_doses_likely_discarded", "authorization_withdrawn_or_delisted"),
        price_data_source="public vaccine-demand-collapse reference",
        reported_price_anchor="10M doses purchased, 600k released, only 3,787 administered by Nov 2022",
        reported_return_anchor="Approval/procurement failed to become demand; stock OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"government_purchase_doses_mn": 10.0, "released_to_hospitals_doses": 600000, "administered_shots": 3787, "administered_share_of_released_pct": 0.63, "administered_share_of_purchased_pct": 0.038, "production_status": "indefinitely_suspended_due_low_demand", "unused_doses_likely_discarded": True, "eu_authorization_application_withdrawn": "2023-09", "who_eul_delisted": "2024-05"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="failed_rerating_reference",
        rerating_result="no_rerating",
        round_rerating_label="vaccine_approval_procurement_not_demand",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="demand_collapse_reference",
        price_validation_status="stock_ohlc_unavailable_after_deep_search",
        notes="Approval and government procurement did not become actual demand; use as vaccine demand-collapse reference.",
    ),
)


def round276_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND276_CASE_CANDIDATES:
        stage3_terms = ("prescription", "royalty", "milestone", "launch", "utilization", "transfer", "reimbursement", "clinic", "consumable", "fcf", "margin")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND276_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round276 R7 Loop-13 biotech/healthcare/device price validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(token in field.lower() for token in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("mfe", "event", "m&a", "take_private", "policy", "rally", "premium", "acquisition", "approval"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("crl", "patent", "inspection", "demand", "underutilization", "safety", "withdrawn", "delisted", "failure"))),
            must_have_fields=ROUND276_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4b_watch", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND276_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "hard_4c_confirmed_false",
                "hard_4c_reference_confirmed_true_for_vaccine_demand_and_regulatory_quality",
                "do_not_use_round276_cases_as_candidate_generation_input",
                "do_not_treat_fda_approval_cdmo_factory_platform_tech_policy_mna_or_procurement_as_green_alone",
                *ROUND276_GREEN_REQUIRED_FIELDS,
                *ROUND276_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.event_mfe_pct,
                mae_30d=candidate.event_mae_pct,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.event_mfe_pct is not None
                    or candidate.event_mae_pct is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round276_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "case_id": candidate.case_id,
            "symbol": candidate.symbol,
            "company_name": candidate.company_name,
            "primary_archetype": candidate.primary_archetype.value,
            "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
            "case_type": candidate.case_type,
            "round_case_type": candidate.round_case_type,
            "stage1_date": _date_text(candidate.stage1_date),
            "stage2_date": _date_text(candidate.stage2_date),
            "stage3_date": _date_text(candidate.stage3_date),
            "stage4b_date": _date_text(candidate.stage4b_date),
            "stage4c_date": _date_text(candidate.stage4c_date),
            "stage3_decision": candidate.stage3_decision,
            "stage4b_status": candidate.stage4b_status,
            "hard_4c_confirmed": str(candidate.hard_4c_confirmed).lower(),
            "hard_4c_reference_confirmed": str(candidate.hard_4c_reference_confirmed).lower(),
            "price_data_source": candidate.price_data_source,
            "reported_price_anchor": candidate.reported_price_anchor,
            "reported_return_anchor": candidate.reported_return_anchor,
            "event_mfe_pct": _float_text(candidate.event_mfe_pct),
            "event_mae_pct": _float_text(candidate.event_mae_pct),
            "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": candidate.score_price_alignment,
            "round_alignment_label": candidate.round_alignment_label,
            "rerating_result": candidate.rerating_result,
            "round_rerating_label": candidate.round_rerating_label,
            "stage_failure_type": candidate.stage_failure_type,
            "round_stage_failure_label": candidate.round_stage_failure_label,
            "price_validation_status": candidate.price_validation_status,
            "evidence_fields": "|".join(candidate.evidence_fields),
            "red_flag_fields": "|".join(candidate.red_flag_fields),
            "notes": candidate.notes,
        }
        for candidate in ROUND276_CASE_CANDIDATES
    )


def round276_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND276_SCORE_ADJUSTMENTS)


def round276_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND276_SHADOW_WEIGHT_ROWS)


def round276_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND276_DEEP_SUB_ARCHETYPES)


def round276_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round276_price_validation": "true"} for field in ROUND276_PRICE_VALIDATION_FIELDS)


def round276_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round276_label": label, "canonical_archetype": canonical} for label, canonical in ROUND276_REQUIRED_TARGET_ALIASES.items())


def round276_summary() -> dict[str, int | bool | str]:
    cases = ROUND276_CASE_CANDIDATES
    return {
        "source_round": ROUND276_SOURCE_ROUND_PATH,
        "round_id": ROUND276_ANALYST_ROUND_ID,
        "large_sector": ROUND276_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "hard_4c_reference_count": sum(1 for case in cases if case.hard_4c_reference_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND276_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND276_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND276_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
        "hard_4c_reference_confirmed": any(case.hard_4c_reference_confirmed for case in cases),
    }


def round276_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND276_SOURCE_ROUND_PATH,
        "round_id": ROUND276_ANALYST_ROUND_ID,
        "large_sector": ROUND276_LARGE_SECTOR,
        "summary": round276_summary(),
        "target_aliases": dict(ROUND276_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND276_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND276_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND276_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND276_HARD_4C_GATES),
        "score_adjustments": list(round276_score_adjustment_rows()),
        "shadow_weights": list(round276_shadow_weight_rows()),
        "deep_sub_archetypes": list(round276_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND276_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round276_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_fda_approval_cdmo_factory_platform_tech_policy_mna_or_procurement_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round276_summary_markdown() -> str:
    summary = round276_summary()
    lines = [
        "# Round 276 R7 Loop 13 Bio Healthcare Medical Device Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- hard_4c_reference: {summary['hard_4c_reference_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND276_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.round_case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    case.round_alignment_label,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- FDA approval and global partner validation are Stage 2 until prescription ramp and royalty/milestone cashflow appear.",
            "- CDMO and U.S. factory rows need utilization, customer transfer, regulatory quality, margin and FCF.",
            "- Aesthetic device takeout validates business quality, but take-private is not a tradable Stage 3 path.",
            "- Policy-support rallies and M&A pops are 4B/event premium before company-level economics.",
            "- SkyCovione is a demand-collapse reference: procurement is not administered demand.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round276_green_gate_review_markdown() -> str:
    lines = [
        "# Round 276 R7 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R7 Stage 3-Green is not `FDA approval`, `CDMO facility`, `platform technology`, `medical-device M&A`, `policy support`, or `government procurement`. It requires prescription ramp, royalty/milestone cash, capacity utilization, regulatory quality, device usage, reimbursement, and FCF.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND276_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND276_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND276_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Yuhan FDA approval` is Stage 2; Green needs prescription ramp and royalty cashflow.",
            "- `Samsung Bio U.S. facility` is Stage 2; Green needs utilization and customer transfer.",
            "- `SkyCovione 10M doses purchased` failed because only 3,787 shots were administered.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round276_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 276 R7 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND276_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND276_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | hard reference | interpretation |", "|---|---|---|---|---|---|"])
    for case in ROUND276_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {str(case.hard_4c_reference_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round276_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 276 R7 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, prescription ramp, royalty cashflow, utilization, reimbursement, patent clearance, administered demand, margin or FCF where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND276_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND276_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round276_r7_loop13_reports(
    output_directory: str | Path = ROUND276_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND276_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND276_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round276_case_records(), cases_path),
        "audit": _write_json(round276_audit_payload(), audit_path),
        "summary": output / "round276_r7_loop13_price_validation_summary.md",
        "case_matrix": output / "round276_r7_loop13_case_matrix.csv",
        "target_aliases": output / "round276_r7_loop13_target_aliases.csv",
        "score_adjustments": output / "round276_r7_loop13_score_adjustments.csv",
        "shadow_weights": output / "round276_r7_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round276_r7_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round276_r7_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round276_r7_loop13_green_gate_review.md",
        "price_validation_plan": output / "round276_r7_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round276_r7_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round276_summary_markdown(), encoding="utf-8")
    _write_csv(round276_case_rows(), paths["case_matrix"])
    _write_csv(round276_target_alias_rows(), paths["target_aliases"])
    _write_csv(round276_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round276_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round276_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round276_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round276_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round276_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round276_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def _write_json(payload: object, path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def _write_csv(rows: Iterable[dict[str, str]], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    rows = tuple(rows)
    if not rows:
        target.write_text("", encoding="utf-8")
        return target
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _float_text(value: float | None) -> str:
    return "" if value is None else f"{value:g}"


def _signed(value: int) -> str:
    return f"+{value}" if value > 0 else str(value)
