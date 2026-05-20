"""Round-289 R7 Loop-14 biotech/healthcare/device price-validation pack.

This module converts ``docs/round/round_289.md`` into calibration-only case
records and reports. It does not change production scoring, candidate
generation, or StageClassifier thresholds.

Easy example: a U.S. biologics factory acquisition is Stage 2 evidence. It is
not Stage 3-Green until utilization, tech transfer, inspection quality, margin,
and recurring customer orders are visible.
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


ROUND289_SOURCE_ROUND_PATH = "docs/round/round_289.md"
ROUND289_ANALYST_ROUND_ID = "round_217"
ROUND289_LARGE_SECTOR = Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE.value
ROUND289_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round289_r7_loop14_biotech_healthcare_device_price_validation"
ROUND289_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_loop14_round289.jsonl"
ROUND289_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round289_r7_loop14_biotech_healthcare_device_price_validation_audit.json"

ROUND289_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BIO_CMO_US_LOCALIZATION_STAGE2": E2RArchetype.BIO_CMO_US_LOCALIZATION_STAGE2.value,
    "BIOSIMILAR_US_TARIFF_HEDGE_STAGE2": E2RArchetype.BIOSIMILAR_US_TARIFF_HEDGE_STAGE2.value,
    "VACCINE_CDMO_MA_EVENT_PREMIUM": E2RArchetype.VACCINE_CDMO_MA_EVENT_PREMIUM.value,
    "BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE": E2RArchetype.BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE.value,
    "ONCOLOGY_LICENSE_ROYALTY_STAGE2": E2RArchetype.ONCOLOGY_LICENSE_ROYALTY_STAGE2.value,
    "AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2": E2RArchetype.AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2.value,
    "KOREAN_BIOTECH_TECH_EXPORT_STAGE2": E2RArchetype.KOREAN_BIOTECH_TECH_EXPORT_STAGE2.value,
    "GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE": E2RArchetype.GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE.value,
}

ROUND289_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "fda_approval_to_launch_conversion_confirmed",
    "royalty_milestone_probability_confirmed",
    "facility_utilization_confirmed",
    "fda_inspection_and_tech_transfer_confirmed",
    "cmo_recurring_order_visibility_confirmed",
    "clinical_endpoint_quality_confirmed",
    "partner_execution_quality_confirmed",
    "patent_ip_freedom_to_operate_confirmed",
    "reimbursement_and_market_access_confirmed",
    "physician_adoption_sellthrough_confirmed",
    "price_path_after_evidence",
)

ROUND289_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "FDA_headline_only",
    "facility_acquisition_only",
    "CMO_capacity_without_utilization",
    "tech_export_upfront_only",
    "early_stage_deal_without_phase2_3",
    "approval_without_reimbursement",
    "aesthetic_launch_without_doctor_adoption",
    "patent_dispute_unresolved",
    "clinical_hold_or_CRL",
)

ROUND289_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "FDA_approval_headline_before_launch_or_reimbursement",
    "tech_export_upfront_total_deal_value_only",
    "CDMO_facility_acquisition_before_utilization",
    "global_partner_name_rally_before_milestones",
    "aesthetic_us_launch_before_physician_adoption",
    "unlisted_biotech_deal_readthrough_to_listed_peers",
)

ROUND289_HARD_4C_GATES: tuple[str, ...] = (
    "FDA_CRL_or_rejection",
    "clinical_hold",
    "pivotal_trial_primary_endpoint_failure",
    "partner_termination_or_milestone_cancellation",
    "FDA_inspection_failure_at_key_facility",
    "reimbursement_failure_after_approval",
    "patent_injunction_or_freedom_to_operate_failure",
    "serious_safety_signal_or_product_recall",
)

ROUND289_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "reported_event_price_anchor",
    "deal_value_anchor",
    "facility_capacity_anchor",
    "fda_approval_anchor",
    "adoption_target_anchor",
    "clinical_failure_drawdown_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round289ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round289ShadowWeightRow:
    archetype: E2RArchetype
    fda_approval_to_launch_conversion: int
    royalty_milestone_probability: int
    facility_utilization: int
    fda_inspection_tech_transfer: int
    cmo_recurring_order_visibility: int
    clinical_endpoint_quality: int
    partner_execution_quality: int
    patent_ip_freedom_to_operate: int
    reimbursement_market_access: int
    physician_adoption_sellthrough: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "fda_approval_to_launch_conversion": _signed(self.fda_approval_to_launch_conversion),
            "royalty_milestone_probability": _signed(self.royalty_milestone_probability),
            "facility_utilization": _signed(self.facility_utilization),
            "fda_inspection_tech_transfer": _signed(self.fda_inspection_tech_transfer),
            "cmo_recurring_order_visibility": _signed(self.cmo_recurring_order_visibility),
            "clinical_endpoint_quality": _signed(self.clinical_endpoint_quality),
            "partner_execution_quality": _signed(self.partner_execution_quality),
            "patent_ip_freedom_to_operate": _signed(self.patent_ip_freedom_to_operate),
            "reimbursement_market_access": _signed(self.reimbursement_market_access),
            "physician_adoption_sellthrough": _signed(self.physician_adoption_sellthrough),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard4c_sensitivity": _signed(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round289DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round289CaseCandidate:
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
    sector_hard_4c_reference_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_event_return_anchor: str
    reported_event_price_anchor: str
    event_mfe_pct: float | None
    event_mae_pct: float | None
    stage1_price_anchor: float | None
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


ROUND289_SCORE_ADJUSTMENTS: tuple[Round289ScoreAdjustment, ...] = (
    Round289ScoreAdjustment("FDA_approval_to_launch_conversion", 5, "raise", "승인 headline은 launch와 접근성으로 닫혀야 한다."),
    Round289ScoreAdjustment("royalty_milestone_probability", 5, "raise", "기술수출과 라이선스는 마일스톤/로열티 확률이 중요하다."),
    Round289ScoreAdjustment("facility_utilization", 5, "raise", "CMO/CDMO 시설은 capacity가 아니라 가동률이 Green 근거다."),
    Round289ScoreAdjustment("FDA_inspection_and_tech_transfer", 5, "raise", "미국 공장과 바이오 생산은 inspection/tech transfer gate를 통과해야 한다."),
    Round289ScoreAdjustment("CMO_recurring_order_visibility", 5, "raise", "반복 주문과 batch slot이 있어야 매출 visibility가 생긴다."),
    Round289ScoreAdjustment("clinical_endpoint_quality", 5, "raise", "임상은 headline보다 endpoint quality가 valuation을 지탱한다."),
    Round289ScoreAdjustment("partner_execution_quality", 5, "raise", "global partner 이름보다 실제 실행력이 중요하다."),
    Round289ScoreAdjustment("patent_IP_freedom_to_operate", 5, "raise", "SC formulation과 platform tech는 patent/IP gate가 핵심이다."),
    Round289ScoreAdjustment("reimbursement_and_market_access", 5, "raise", "승인 후 보험/market access가 있어야 매출 전환이 가능하다."),
    Round289ScoreAdjustment("physician_adoption_sellthrough", 4, "raise", "의료미용은 doctor adoption과 sell-through가 실제 수요다."),
    Round289ScoreAdjustment("FDA_headline_only", -5, "lower", "FDA headline만으로 Stage 3-Green을 만들지 않는다."),
    Round289ScoreAdjustment("facility_acquisition_only", -5, "lower", "공장 인수만으로 가동률과 마진을 발명하지 않는다."),
    Round289ScoreAdjustment("CMO_capacity_without_utilization", -5, "lower", "CMO capacity는 utilization 전에는 Stage 2다."),
    Round289ScoreAdjustment("tech_export_upfront_only", -5, "lower", "upfront만 있고 Phase 2/3·마일스톤 확률이 없으면 Green이 아니다."),
    Round289ScoreAdjustment("early_stage_deal_without_phase2_3", -5, "lower", "초기 임상 기술수출은 strong option이지 Green 근거가 아니다."),
    Round289ScoreAdjustment("approval_without_reimbursement", -4, "lower", "승인 후 접근성/보험이 없으면 매출 bridge가 약하다."),
    Round289ScoreAdjustment("aesthetic_launch_without_doctor_adoption", -4, "lower", "의료미용 launch는 physician adoption 전에는 과열 가능성이 있다."),
    Round289ScoreAdjustment("patent_dispute_unresolved", -5, "lower", "patent dispute가 남으면 royalty/adoption을 유예한다."),
    Round289ScoreAdjustment("clinical_hold_or_CRL", -5, "lower", "clinical hold/CRL은 hard 4C 후보로 본다."),
)


ROUND289_SHADOW_WEIGHT_ROWS: tuple[Round289ShadowWeightRow, ...] = (
    Round289ShadowWeightRow(E2RArchetype.BIO_CMO_US_LOCALIZATION_STAGE2, 3, 1, 5, 5, 5, 2, 4, 2, 2, 0, -5, 4, 4, "Samsung Biologics shows facility acquisition is not Green without utilization and margin."),
    Round289ShadowWeightRow(E2RArchetype.BIOSIMILAR_US_TARIFF_HEDGE_STAGE2, 4, 3, 5, 5, 4, 3, 4, 3, 5, 0, -5, 4, 4, "Celltrion U.S. factory hedge needs product transfer, market share and tariff savings."),
    Round289ShadowWeightRow(E2RArchetype.VACCINE_CDMO_MA_EVENT_PREMIUM, 3, 1, 5, 5, 5, 3, 4, 2, 3, 0, -5, 5, 4, "SK Bioscience IDT acquisition needs CDMO backlog, integration and margin."),
    Round289ShadowWeightRow(E2RArchetype.BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE, 5, 5, 2, 4, 2, 5, 5, 5, 5, 4, -3, 5, 4, "Alteogen/Keytruda Qlex needs adoption, royalty and patent freedom-to-operate."),
    Round289ShadowWeightRow(E2RArchetype.ONCOLOGY_LICENSE_ROYALTY_STAGE2, 5, 5, 2, 4, 1, 5, 5, 4, 5, 0, -4, 4, 4, "Yuhan/Lazertinib needs launch uptake, royalty economics and manufacturing gate."),
    Round289ShadowWeightRow(E2RArchetype.AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2, 5, 3, 1, 3, 1, 3, 4, 3, 2, 5, -4, 5, 3, "Hugel/Letybo needs physician adoption, distributor margin and safety compliance."),
    Round289ShadowWeightRow(E2RArchetype.KOREAN_BIOTECH_TECH_EXPORT_STAGE2, 3, 5, 0, 1, 0, 5, 5, 4, 3, 0, -5, 5, 4, "ADEL/Sanofi upfront deal is Stage 2 until Phase 2/3 and royalty probability improve."),
    Round289ShadowWeightRow(E2RArchetype.GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE, 5, 5, 0, 5, 0, 5, 3, 5, 5, 0, 0, 5, 5, "Trial failure, FDA rejection or clinical hold must be hard 4C reference."),
)


ROUND289_DEEP_SUB_ARCHETYPES: tuple[Round289DeepSubArchetype, ...] = (
    Round289DeepSubArchetype("CMO/CDMO U.S. localization", E2RArchetype.BIO_CMO_US_LOCALIZATION_STAGE2, ("Samsung Biologics", "GSK Rockville", "60,000L", "FDA inspection", "utilization")),
    Round289DeepSubArchetype("Biosimilar tariff hedge", E2RArchetype.BIOSIMILAR_US_TARIFF_HEDGE_STAGE2, ("Celltrion", "ImClone", "Eli Lilly", "tariff savings", "product transfer")),
    Round289DeepSubArchetype("Vaccine CDMO M&A", E2RArchetype.VACCINE_CDMO_MA_EVENT_PREMIUM, ("SK Bioscience", "IDT Biologika", "Novavax", "CDMO backlog", "plant utilization")),
    Round289DeepSubArchetype("Blockbuster SC formulation", E2RArchetype.BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE, ("Alteogen", "Keytruda Qlex", "30-40% adoption", "royalty", "patent dispute")),
    Round289DeepSubArchetype("Oncology licensing royalty", E2RArchetype.ONCOLOGY_LICENSE_ROYALTY_STAGE2, ("Yuhan", "lazertinib", "Rybrevant", "peak sales", "manufacturing CRL")),
    Round289DeepSubArchetype("Aesthetic medical U.S. launch", E2RArchetype.AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2, ("Hugel", "Letybo", "Botulax", "physician adoption", "counterfeit safety")),
    Round289DeepSubArchetype("Korean biotech tech export", E2RArchetype.KOREAN_BIOTECH_TECH_EXPORT_STAGE2, ("ADEL", "Sanofi", "upfront", "milestone", "Phase 2/3")),
    Round289DeepSubArchetype("Global clinical/FDA hard 4C", E2RArchetype.GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE, ("HilleVax", "Corcept", "PepGen", "clinical hold", "CRL")),
)


ROUND289_CASE_CANDIDATES: tuple[Round289CaseCandidate, ...] = (
    Round289CaseCandidate(
        "r7_loop14_samsung_biologics_gsk_us_facility",
        "207940",
        "Samsung Biologics",
        E2RArchetype.BIO_CMO_US_LOCALIZATION_STAGE2,
        (E2RArchetype.CDMO_US_TARIFF_HEDGE_STAGE2, E2RArchetype.MANUFACTURING_INSPECTION_CRL_OVERLAY),
        "success_candidate",
        "evidence_good_but_price_failed",
        date(2025, 5, 1),
        date(2025, 12, 22),
        None,
        None,
        date(2025, 12, 22),
        "Stage 2 only; utilization, FDA inspection, tech transfer and recurring orders required.",
        "4C-watch: price failed and facility execution remains unproven",
        False,
        False,
        ("facility_acquisition", "facility_capacity_liters", "tariff_cap", "us_localization"),
        ("facility_acquisition_only", "CMO_capacity_without_utilization", "FDA_inspection_and_tech_transfer_unconfirmed"),
        "Reuters Samsung Biologics-GSK facility event anchor",
        "-0.4% vs KOSPI +2.0%",
        "$280M acquisition / 60,000L capacity",
        None,
        -0.4,
        None,
        None,
        None,
        None,
        None,
        {
            "acquisition_value_usd_mn": 280.0,
            "facility_location": "Rockville, Maryland",
            "facility_capacity_liters": 60000,
            "expected_close": "2026_Q1_end",
            "korean_pharma_tariff_cap_pct": 15,
            "generic_drugs_tariff_free": True,
            "kospi_same_context_pct": 2.0,
            "relative_underperformance_pp": -2.4,
            "facility_utilization_confirmed": False,
            "fda_inspection_transfer_confirmed": False,
        },
        "evidence_good_but_price_failed",
        "evidence_good_but_price_failed",
        "unknown",
        "BIO_CMO_US_LOCALIZATION_STAGE2",
        "stage2_watch_success",
        "facility_acquisition_not_utilization_margin_green",
        "partial_reported_anchor",
        "U.S. facility acquisition underperformed the market; facility utilization and margin remain the gate.",
    ),
    Round289CaseCandidate(
        "r7_loop14_celltrion_us_factory_tariff_hedge",
        "068270",
        "Celltrion",
        E2RArchetype.BIOSIMILAR_US_TARIFF_HEDGE_STAGE2,
        (E2RArchetype.BIOPHARMA_US_FACTORY_TARIFF_HEDGE, E2RArchetype.BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING),
        "success_candidate",
        "success_candidate_price_unavailable",
        date(2025, 7, 29),
        date(2025, 9, 23),
        None,
        date(2025, 11, 19),
        date(2025, 11, 19),
        "Stage 2 only; product transfer, utilization, tariff saving and market share required.",
        "4B/4C-watch: tariff hedge can rerate before execution and margin proof",
        False,
        False,
        ("factory_acquisition", "capacity_expansion", "tariff_hedge_rationale"),
        ("facility_acquisition_only", "product_transfer_unconfirmed", "us_factory_utilization_unconfirmed"),
        "Reuters Celltrion U.S. factory acquisition and expansion anchors",
        "price_data_unavailable_after_deep_search",
        "$330M acquisition / up to 700B won expansion",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        {
            "factory_acquisition_value_usd_mn": 330.0,
            "target_seller": "Eli Lilly / ImClone Systems LLC",
            "additional_capacity_investment_krw_bn": 700.0,
            "additional_capacity_investment_usd_mn": 478.17,
            "tariff_hedge_rationale": True,
            "product_transfer_confirmed": False,
            "us_factory_utilization_confirmed": False,
        },
        "unknown",
        "success_candidate_but_price_data_unavailable",
        "unknown",
        "BIOSIMILAR_US_TARIFF_HEDGE_STAGE2",
        "stage2_watch_success",
        "acquisition_capacity_not_tariff_saving_margin_green",
        "price_data_unavailable_after_deep_search",
        "U.S. tariff hedge is Stage 2; product transfer, utilization and margin are still missing.",
    ),
    Round289CaseCandidate(
        "r7_loop14_sk_bioscience_idt_biologika_ma",
        "302440",
        "SK Bioscience",
        E2RArchetype.VACCINE_CDMO_MA_EVENT_PREMIUM,
        (E2RArchetype.VACCINE_CDMO_M_AND_A_STAGE2, E2RArchetype.VACCINE_CMO_RESTRUCTURING),
        "success_candidate",
        "event_premium_success_candidate",
        date(2024, 6, 27),
        date(2024, 6, 27),
        None,
        date(2024, 6, 27),
        date(2024, 6, 27),
        "Stage 2 only; M&A control is not backlog, utilization or margin.",
        "4B-watch: +11.7% event premium before utilization proof",
        False,
        False,
        ("stake_acquisition", "deal_value", "novavax_partnership_validation"),
        ("M&A_without_utilization", "plant_utilization_unconfirmed"),
        "Reuters SK Bioscience-IDT Biologika M&A anchor",
        "+11.7%",
        "339B won / $243.75M deal",
        11.7,
        None,
        None,
        None,
        None,
        None,
        None,
        {
            "acquired_stake_pct": 60,
            "deal_value_krw_bn": 339.0,
            "deal_value_usd_mn": 243.75,
            "seller_retained_stake_pct": 40,
            "ipo_2021_raise_usd_bn": 1.33,
            "novavax_partnership_validation": True,
            "cdmo_backlog_confirmed": False,
            "plant_utilization_confirmed": False,
        },
        "price_moved_without_evidence",
        "event_premium_success_candidate",
        "event_premium",
        "VACCINE_CDMO_MA_STAGE2",
        "false_yellow",
        "ma_control_not_cdmo_utilization_green",
        "partial_reported_anchor",
        "IDT acquisition drove event premium; integration, backlog and margin must be proven.",
    ),
    Round289CaseCandidate(
        "r7_loop14_alteogen_keytruda_qlex_sc_formulation",
        "196170",
        "Alteogen",
        E2RArchetype.BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE,
        (E2RArchetype.PLATFORM_TECH_ENZYME_ROYALTY_OPTIONALITY, E2RArchetype.PATENT_CHALLENGE_OVERLAY),
        "success_candidate",
        "structural_success_candidate_price_unavailable",
        date(2024, 11, 19),
        date(2025, 3, 27),
        date(2025, 9, 19),
        date(2025, 9, 19),
        date(2025, 9, 19),
        "Stage 3 candidate, not automatic Green; adoption, royalty and patent freedom-to-operate required.",
        "4B/4C-watch: FDA approval can rerate before royalty and patent clarity",
        False,
        False,
        ("keytruda_sales_base", "adoption_target", "fda_approval", "enzyme_supplier_role"),
        ("patent_dispute_unresolved", "royalty_conversion_unconfirmed", "adoption_not_realized"),
        "Reuters Keytruda SC trial/launch/approval anchors + WSJ patent-dispute anchor",
        "price_data_unavailable_after_deep_search",
        "Keytruda Qlex approval / 30-40% adoption target",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        {
            "keytruda_2024_sales_usd_bn": 30.0,
            "target_peak_adoption_pct_range": "30-40",
            "administration_time_sc_minutes": "1-2",
            "administration_time_iv_minutes": 30,
            "us_availability_expected": "late_2025_09",
            "alteogen_enzyme_role": "develops_and_manufactures_enzyme_used_with_Keytruda_SC",
            "patent_dispute_watch": True,
            "royalty_conversion_confirmed": False,
        },
        "unknown",
        "structural_success_candidate_but_price_data_unavailable",
        "unknown",
        "BLOCKBUSTER_SC_FORMULATION_STAGE3_CANDIDATE",
        "stage2_watch_success",
        "FDA_approval_not_royalty_adoption_patent_green",
        "price_data_unavailable_after_deep_search",
        "Strongest structural candidate in this pack; Green waits for adoption, royalty and IP gates.",
    ),
    Round289CaseCandidate(
        "r7_loop14_yuhan_lazertinib_jnj_rybrevant_approval",
        "000100",
        "Yuhan",
        E2RArchetype.ONCOLOGY_LICENSE_ROYALTY_STAGE2,
        (E2RArchetype.KOREAN_ORIGIN_DRUG_GLOBAL_APPROVAL, E2RArchetype.MANUFACTURING_INSPECTION_CRL_OVERLAY),
        "success_candidate",
        "success_candidate_price_unavailable",
        date(2024, 8, 20),
        date(2024, 8, 20),
        None,
        date(2024, 8, 20),
        date(2024, 12, 16),
        "Stage 2 only; approval needs launch uptake, royalty economics and manufacturing gate.",
        "4B/4C-watch: launch premium with later manufacturing CRL watch",
        False,
        False,
        ("fda_approval", "peak_sales_expectation", "pfs_benefit", "partner_launch"),
        ("approval_without_reimbursement", "manufacturing_inspection_CRL_watch", "royalty_not_realized"),
        "Reuters FDA approval and later CRL anchors",
        "price_data_unavailable_after_deep_search",
        "FDA approval / Rybrevant peak sales above $5B",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        {
            "indication": "first-line EGFR-mutated non-small cell lung cancer",
            "combination": "Rybrevant + lazertinib",
            "rybrevant_peak_sales_expectation_usd_bn": 5.0,
            "pfs_benefit_vs_tagrisso": True,
            "later_crl_related_to": "pre-approval inspection at manufacturing facility",
            "later_crl_not_related_to": ["formulation", "efficacy", "safety_data"],
            "iv_rybrevant_unaffected": True,
        },
        "unknown",
        "success_candidate_but_price_data_unavailable",
        "unknown",
        "ONCOLOGY_LICENSE_ROYALTY_STAGE2",
        "stage2_watch_success",
        "approval_not_royalty_launch_margin_green",
        "price_data_unavailable_after_deep_search",
        "FDA approval is Stage 2; royalty economics and manufacturing regulatory gate remain.",
    ),
    Round289CaseCandidate(
        "r7_loop14_hugel_letybo_us_aesthetic_launch",
        "145020",
        "Hugel",
        E2RArchetype.AESTHETIC_MEDICAL_DEVICE_US_LAUNCH_STAGE2,
        (E2RArchetype.BOTULINUM_TOXIN_US_LAUNCH, E2RArchetype.DEVICE_SAFETY_COUNTERFEIT_OVERLAY),
        "success_candidate",
        "success_candidate_regulatory_watch",
        date(2025, 3, 1),
        date(2025, 3, 1),
        None,
        date(2025, 3, 1),
        date(2025, 11, 1),
        "Stage 2 only; FDA approval and U.S. rollout need physician adoption and distributor margin.",
        "4B/4C-watch: U.S. aesthetic premium with category safety/counterfeit risk",
        False,
        False,
        ("fda_approval", "us_launch", "pricing_advantage_context", "category_demand"),
        ("aesthetic_launch_without_doctor_adoption", "category_safety_watch", "distributor_margin_unconfirmed"),
        "Allure Letybo U.S. launch context + AP FDA counterfeit Botox warning",
        "price_data_unavailable_after_deep_search",
        "Letybo U.S. launch / FDA category safety warning",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        {
            "product": "Letybo / Botulax",
            "us_indication": "glabellar_lines",
            "category": "botulinum_toxin_A_neuromodulator",
            "pricing_advantage_context": True,
            "category_safety_watch": True,
            "physician_adoption_confirmed": False,
            "distributor_margin_confirmed": False,
        },
        "unknown",
        "success_candidate_but_price_data_unavailable",
        "unknown",
        "AESTHETIC_MEDICAL_US_LAUNCH_STAGE2",
        "stage2_watch_success",
        "FDA_approval_not_adoption_margin_green",
        "price_data_unavailable_after_deep_search",
        "FDA approval and U.S. launch need physician adoption, distributor margin and safety compliance.",
    ),
    Round289CaseCandidate(
        "r7_loop14_adel_sanofi_alzheimers_tech_export_reference",
        "unlisted",
        "ADEL / Sanofi",
        E2RArchetype.KOREAN_BIOTECH_TECH_EXPORT_STAGE2,
        (E2RArchetype.BIOTECH_LICENSE_MILESTONE_PLATFORM, E2RArchetype.BIOTECH_PRE_REVENUE_REGULATORY),
        "success_candidate",
        "success_candidate_reference_only",
        date(2025, 12, 15),
        date(2025, 12, 15),
        None,
        date(2025, 12, 15),
        date(2025, 12, 15),
        "Stage 2 reference only; unlisted early-stage deal is not listed-stock Green.",
        "4B/4C-watch: tech-export premium before Phase 2/3 and milestone probability",
        False,
        False,
        ("deal_value", "upfront_payment", "global_partner", "early_stage_trial"),
        ("tech_export_upfront_only", "early_stage_deal_without_phase2_3", "listed_readthrough_unconfirmed"),
        "Reuters ADEL-Sanofi deal anchor",
        "unlisted_reference_no_ohlc",
        "$1.04B max deal / $80M upfront",
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        {
            "deal_value_max_usd_bn": 1.04,
            "upfront_payment_usd_mn": 80.0,
            "candidate": "ADEL-Y01",
            "disease_area": "Alzheimer's disease",
            "mechanism_context": "tau acetylation / harmful tau-related protein forms",
            "clinical_stage": "early-stage human trials in U.S.",
            "listed_stock_readthrough_confirmed": False,
        },
        "unknown",
        "success_candidate_reference_only",
        "unknown",
        "KOREAN_BIOTECH_TECH_EXPORT_STAGE2",
        "stage2_watch_success",
        "upfront_milestone_deal_not_phase3_royalty_green",
        "unlisted_reference_no_ohlc",
        "Upfront/milestone deal is Stage 2; Phase 2/3 data and royalty probability are required.",
    ),
    Round289CaseCandidate(
        "r7_loop14_global_clinical_fda_failure_hard_reference",
        "global_reference",
        "HilleVax / Corcept / PepGen reference",
        E2RArchetype.GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE,
        (E2RArchetype.VACCINE_DEMAND_COLLAPSE_HARD_REFERENCE, E2RArchetype.COMMERCIALIZATION_FAILURE_OVERLAY),
        "4c_thesis_break",
        "sector_hard_4C_reference",
        date(2024, 7, 8),
        None,
        None,
        None,
        date(2024, 7, 8),
        "Not a positive candidate; reference for clinical/FDA downside.",
        "Hard 4C reference: clinical/FDA failures reset biotech valuation immediately",
        False,
        True,
        ("clinical_failure_drawdown", "FDA_rejection_drawdown", "clinical_hold_drawdown"),
        ("pivotal_trial_primary_endpoint_failure", "FDA_CRL_or_rejection", "clinical_hold"),
        "Reuters/Barron's clinical trial failure and FDA rejection/hold anchors",
        "HilleVax -87.6%, Corcept -50.8%, PepGen -25%+",
        "sector hard 4C reference",
        None,
        -87.6,
        None,
        None,
        None,
        None,
        1.75,
        {
            "hillevax_trial_efficacy_pct": 5,
            "hillevax_event_mae_pct": -87.6,
            "hillevax_event_low_usd": 1.75,
            "corcept_event_mae_pct": -50.8,
            "corcept_price_before_usd": 70.20,
            "corcept_price_after_usd": 34.51,
            "corcept_market_value_loss_usd_bn": 3.7,
            "pepgen_after_hours_mae_pct": -25,
            "direct_krx_hard_4c_confirmed": False,
            "use_as_sector_hard_reference": True,
        },
        "false_positive_score",
        "thesis_break_reference",
        "thesis_break",
        "GLOBAL_CLINICAL_FAILURE_HARD_4C_REFERENCE",
        "should_have_been_red",
        "clinical_or_FDA_failure_resets_pipeline_valuation",
        "partial_reported_anchor",
        "Clinical/FDA failure can reset biotech valuation immediately; use as sector hard 4C reference.",
    ),
)


def round289_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND289_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR" if candidate.symbol not in {"unlisted", "global_reference"} else "GLOBAL_REFERENCE",
            sector_raw="Bio / Healthcare / Medical Device",
            large_sector=ROUND289_LARGE_SECTOR,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=candidate.notes,
            stage1_evidence=tuple(field for field in candidate.evidence_fields if "headline" in field or "approval" in field or "acquisition" in field),
            stage2_evidence=candidate.evidence_fields,
            stage3_evidence=tuple(field for field in candidate.evidence_fields if field in ROUND289_GREEN_REQUIRED_FIELDS),
            stage4b_evidence=tuple(field for field in candidate.red_flag_fields if "headline" in field or "premium" in field or "unconfirmed" in field),
            stage4c_evidence=tuple(field for field in candidate.red_flag_fields if "CRL" in field or "clinical" in field or "failure" in field or "safety" in field),
            must_have_fields=ROUND289_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"4c_thesis_break", "event_premium"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.round_alignment_label,
            score_weight_hint={row.axis: float(row.points) for row in ROUND289_SCORE_ADJUSTMENTS if row.direction == "raise"},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "do_not_use_round289_cases_as_candidate_generation_input",
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
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
                    or candidate.stage1_price_anchor is not None
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


def round289_case_rows() -> tuple[dict[str, str], ...]:
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
            "sector_hard_4c_reference_confirmed": str(candidate.sector_hard_4c_reference_confirmed).lower(),
            "price_data_source": candidate.price_data_source,
            "reported_event_return_anchor": candidate.reported_event_return_anchor,
            "reported_event_price_anchor": candidate.reported_event_price_anchor,
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
        for candidate in ROUND289_CASE_CANDIDATES
    )


def round289_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND289_SCORE_ADJUSTMENTS)


def round289_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND289_SHADOW_WEIGHT_ROWS)


def round289_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND289_DEEP_SUB_ARCHETYPES)


def round289_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round289_price_validation": "true"} for field in ROUND289_PRICE_VALIDATION_FIELDS)


def round289_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round289_label": label, "canonical_archetype": canonical} for label, canonical in ROUND289_REQUIRED_TARGET_ALIASES.items())


def round289_summary() -> dict[str, int | bool | str]:
    cases = ROUND289_CASE_CANDIDATES
    return {
        "source_round": ROUND289_SOURCE_ROUND_PATH,
        "round_id": ROUND289_ANALYST_ROUND_ID,
        "large_sector": ROUND289_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "sector_hard_4c_reference_count": sum(1 for case in cases if case.sector_hard_4c_reference_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "unknown_alignment_count": sum(1 for case in cases if case.score_price_alignment == "unknown"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "target_archetype_count": len(ROUND289_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND289_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND289_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "direct_KRX_hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
        "sector_hard_4c_reference_confirmed": any(case.sector_hard_4c_reference_confirmed for case in cases),
    }


def round289_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND289_SOURCE_ROUND_PATH,
        "round_id": ROUND289_ANALYST_ROUND_ID,
        "large_sector": ROUND289_LARGE_SECTOR,
        "summary": round289_summary(),
        "target_aliases": dict(ROUND289_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND289_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND289_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND289_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND289_HARD_4C_GATES),
        "score_adjustments": list(round289_score_adjustment_rows()),
        "shadow_weights": list(round289_shadow_weight_rows()),
        "deep_sub_archetypes": list(round289_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND289_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round289_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_fda_cdmo_tech_export_or_medical_device_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round289_summary_markdown() -> str:
    summary = round289_summary()
    lines = [
        "# Round 289 R7 Loop 14 Bio Healthcare Medical Device Price Validation",
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
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- sector_hard_4c_reference: {summary['sector_hard_4c_reference_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND289_CASE_CANDIDATES:
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
            "- CMO/CDMO facility acquisition is Stage 2 until utilization, inspection, tech transfer and margin appear.",
            "- FDA approval is Stage 2 until launch, reimbursement, uptake and royalty economics appear.",
            "- Tech-export upfront value is Stage 2 until Phase 2/3 data, milestones and partner execution improve probability.",
            "- Medical-aesthetic launch is Stage 2 until physician adoption, distributor margin and safety compliance appear.",
            "- Global clinical/FDA failures are sector hard 4C references, not positive candidates.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round289_green_gate_review_markdown() -> str:
    lines = [
        "# Round 289 R7 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R7 Stage 3-Green is not `FDA approval`, `CMO facility`, `tech export`, `Keytruda`, `U.S. factory`, or `medical-aesthetic launch`. It requires launch conversion, utilization, royalty probability, partner execution, IP freedom, reimbursement, physician adoption, and price path after evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND289_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND289_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND289_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Samsung Bio U.S. facility` is Stage 2; Green needs utilization and margin.",
            "- `Alteogen Keytruda Qlex approval` is a Stage 3 candidate; Green waits for adoption, royalty and patent clarity.",
            "- `ADEL $1.04B deal` is Stage 2 reference; Green cannot be inferred from upfront alone.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round289_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 289 R7 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND289_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND289_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | direct hard 4C | sector hard reference | interpretation |", "|---|---|---|---|---|---|"])
    for case in ROUND289_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {str(case.sector_hard_4c_reference_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round289_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 289 R7 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, utilization, inspection quality, reimbursement, royalty conversion, physician adoption, or Phase 2/3 data where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND289_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND289_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_event_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round289_r7_loop14_reports(
    output_directory: str | Path = ROUND289_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND289_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND289_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round289_case_records(), cases_path),
        "audit": _write_json(round289_audit_payload(), audit_path),
        "summary": output / "round289_r7_loop14_price_validation_summary.md",
        "case_matrix": output / "round289_r7_loop14_case_matrix.csv",
        "target_aliases": output / "round289_r7_loop14_target_aliases.csv",
        "score_adjustments": output / "round289_r7_loop14_score_adjustments.csv",
        "shadow_weights": output / "round289_r7_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round289_r7_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round289_r7_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round289_r7_loop14_green_gate_review.md",
        "price_validation_plan": output / "round289_r7_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round289_r7_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round289_summary_markdown(), encoding="utf-8")
    _write_csv(round289_case_rows(), paths["case_matrix"])
    _write_csv(round289_target_alias_rows(), paths["target_aliases"])
    _write_csv(round289_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round289_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round289_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round289_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round289_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round289_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round289_stage4b_4c_review_markdown(), encoding="utf-8")
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
