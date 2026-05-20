"""Round-263 R7 Loop-12 biotech/healthcare/device price-validation pack.

This module converts ``docs/round/round_263.md`` into calibration-only case
records and reports. It does not change production scoring, candidate
generation, or StageClassifier thresholds.

Easy example: FDA approval for a toxin launch is a strong Stage 2 signal. It is
not Stage 3-Green until provider adoption, repeat procedures, ASP/margin, and
safety trust are confirmed.
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


ROUND263_SOURCE_ROUND_PATH = "docs/round/round_263.md"
ROUND263_ROUND_ID = "round_191"
ROUND263_LARGE_SECTOR = Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE.value
ROUND263_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round263_r7_loop12_biotech_healthcare_device_price_validation"
ROUND263_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_loop12_round263.jsonl"
ROUND263_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round263_r7_loop12_biotech_healthcare_device_price_validation_audit.json"

ROUND263_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "AESTHETIC_EBD_GLOBAL_BUYOUT": E2RArchetype.AESTHETIC_EBD_GLOBAL_BUYOUT.value,
    "BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER": E2RArchetype.BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER.value,
    "AESTHETIC_DEVICE_EXPORT_PLATFORM": E2RArchetype.AESTHETIC_DEVICE_EXPORT_PLATFORM.value,
    "BOTULINUM_TOXIN_US_LAUNCH": E2RArchetype.BOTULINUM_TOXIN_US_LAUNCH.value,
    "UNAPPROVED_TOXIN_SAFETY_TRUST_4C": E2RArchetype.UNAPPROVED_TOXIN_SAFETY_TRUST_4C.value,
    "MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE": E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE.value,
    "MEDICAL_SERVICE_DISRUPTION_POLICY_4C": E2RArchetype.MEDICAL_SERVICE_DISRUPTION_POLICY_4C.value,
    "DENTAL_IMPLANT_GLOBAL_M_AND_A": E2RArchetype.DENTAL_IMPLANT_GLOBAL_M_AND_A.value,
}

ROUND263_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "procedure_or_prescription_volume_confirmed",
    "installed_base_or_utilization_confirmed",
    "consumable_or_repeat_treatment_revenue_confirmed",
    "provider_or_hospital_adoption_confirmed",
    "reimbursement_or_selfpay_asp_confirmed",
    "gross_margin_or_fcf_confirmed",
    "safety_counterfeit_and_unauthorized_distribution_risk_passed",
    "policy_or_service_disruption_risk_passed",
    "price_path_after_evidence",
)

ROUND263_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "fda_approval_only",
    "mna_rumor_only",
    "external_validation_only",
    "unlisted_or_delisted_asset_only",
    "device_viral_story_only",
    "unauthorized_toxin_distribution_risk_present",
    "medical_service_capacity_disruption_present",
    "subgroup_performance_weakness_unresolved",
)

ROUND263_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "pe_buyout_or_delisting_premium",
    "fda_approval_spike_before_procedure_volume",
    "medical_device_export_story_before_utilization",
    "beauty_device_three_to_four_x_rally_on_viral_demand",
    "mna_rumor_target_rally_before_close",
    "ai_validation_paper_before_reimbursement",
    "medical_policy_news_healthcare_basket_rally",
)

ROUND263_HARD_4C_GATES: tuple[str, ...] = (
    "fda_rejection_or_crl",
    "post_approval_safety_signal",
    "counterfeit_or_unauthorized_distribution_regulatory_action",
    "provider_adoption_failure",
    "reimbursement_failure",
    "clinical_subgroup_failure_blocks_adoption",
    "mna_cancellation",
    "medical_service_disruption_procedure_volume_collapse",
    "cash_burn_or_dilution_from_commercialization_failure",
)

ROUND263_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "transaction_or_market_value_anchor",
    "procedure_volume_or_exam_count",
    "installed_base_or_export_channel_anchor",
    "regulatory_safety_or_policy_gate",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round263ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round263ShadowWeightRow:
    archetype: E2RArchetype
    procedure_volume: int
    installed_base: int
    consumable_attach_rate: int
    repeat_treatment_frequency: int
    provider_adoption: int
    reimbursement_selfpay: int
    gross_margin_visibility: int
    regulatory_safety_trust: int
    commercial_revenue_conversion: int
    cash_conversion: int
    event_penalty: int
    safety_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "procedure_volume": _signed(self.procedure_volume),
            "installed_base": _signed(self.installed_base),
            "consumable_attach_rate": _signed(self.consumable_attach_rate),
            "repeat_treatment_frequency": _signed(self.repeat_treatment_frequency),
            "provider_adoption": _signed(self.provider_adoption),
            "reimbursement_selfpay": _signed(self.reimbursement_selfpay),
            "gross_margin_visibility": _signed(self.gross_margin_visibility),
            "regulatory_safety_trust": _signed(self.regulatory_safety_trust),
            "commercial_revenue_conversion": _signed(self.commercial_revenue_conversion),
            "cash_conversion": _signed(self.cash_conversion),
            "event_penalty": _signed(self.event_penalty),
            "safety_redteam": _signed(self.safety_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round263DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round263CaseCandidate:
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
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    mfe_1d: float | None
    mae_1d: float | None
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


ROUND263_SCORE_ADJUSTMENTS: tuple[Round263ScoreAdjustment, ...] = (
    Round263ScoreAdjustment("procedure_volume", 5, "raise", "R7 Green은 실제 시술량이나 처방량이 확인되어야 한다."),
    Round263ScoreAdjustment("device_installed_base", 5, "raise", "미용의료기기는 설치대수와 utilization이 반복매출의 출발점이다."),
    Round263ScoreAdjustment("consumable_attach_rate", 5, "raise", "소모품 attach-rate가 있어야 단발 장비판매가 아니다."),
    Round263ScoreAdjustment("repeat_treatment_frequency", 5, "raise", "반복 시술 빈도가 procedure TAM을 현금흐름으로 바꾼다."),
    Round263ScoreAdjustment("provider_adoption", 5, "raise", "톡신과 의료AI는 provider/hospital adoption 전까지 Stage 2다."),
    Round263ScoreAdjustment("reimbursement_or_selfpay_conversion", 4, "raise", "보험·수가 또는 self-pay ASP가 매출 지속성을 만든다."),
    Round263ScoreAdjustment("gross_margin_visibility", 5, "raise", "의료기기와 톡신은 gross margin과 FCF 확인이 중요하다."),
    Round263ScoreAdjustment("regulatory_safety_trust", 5, "raise", "안전·위조·비공식 유통 리스크가 Green을 막는다."),
    Round263ScoreAdjustment("commercial_revenue_conversion", 5, "raise", "승인·논문·M&A가 실제 매출로 전환되어야 한다."),
    Round263ScoreAdjustment("cash_conversion", 4, "raise", "성장률보다 FCF 전환이 Stage 3 품질을 결정한다."),
    Round263ScoreAdjustment("approval_headline_only", -5, "lower", "FDA 승인만으로 Stage 3-Green을 만들지 않는다."),
    Round263ScoreAdjustment("M&A_rumor_only", -5, "lower", "M&A rumor는 확인 전 event premium이다."),
    Round263ScoreAdjustment("external_validation_without_revenue", -5, "lower", "AUC와 외부검증은 상환·병원도입·매출 전 Green 근거가 아니다."),
    Round263ScoreAdjustment("device_viral_demand_only", -4, "lower", "viral device 수요만으로 반복매출을 발명하지 않는다."),
    Round263ScoreAdjustment("unlisted_subsidiary_or_delisted_tracking_gap", -4, "lower", "비상장·상폐 자산은 상장주 Stage 3 추적을 제한한다."),
    Round263ScoreAdjustment("unauthorized_distribution_risk", -5, "lower", "비공식 톡신 유통은 safety/trust 4C-watch다."),
    Round263ScoreAdjustment("safety_or_counterfeit_toxin_risk", -5, "lower", "위조·미승인 톡신 리스크는 제품 신뢰를 훼손한다."),
    Round263ScoreAdjustment("medical_service_disruption", -4, "lower", "의사파업·정책 disruption은 procedure volume을 교란한다."),
    Round263ScoreAdjustment("subgroup_performance_weakness", -4, "lower", "의료AI subgroup weakness는 deployment risk다."),
)


ROUND263_SHADOW_WEIGHT_ROWS: tuple[Round263ShadowWeightRow, ...] = (
    Round263ShadowWeightRow(E2RArchetype.AESTHETIC_EBD_GLOBAL_BUYOUT, 3, 5, 4, 4, 3, 2, 5, 4, 5, 4, -4, 4, 5, 4, "PE buyout validates business quality, but delisting closes public Stage 3 tracking."),
    Round263ShadowWeightRow(E2RArchetype.BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER, 4, 3, 3, 4, 3, 3, 4, 4, 5, 4, -4, 4, 5, 4, "APR-style growth needs repeat demand and channel durability, not viral device demand alone."),
    Round263ShadowWeightRow(E2RArchetype.AESTHETIC_DEVICE_EXPORT_PLATFORM, 4, 5, 5, 4, 4, 3, 5, 5, 5, 4, -3, 5, 4, 5, "Classys-like platform needs installed base, consumables, OPM and FCF."),
    Round263ShadowWeightRow(E2RArchetype.BOTULINUM_TOXIN_US_LAUNCH, 5, 1, 2, 5, 5, 4, 5, 5, 5, 4, -5, 5, 5, 5, "FDA approval is Stage 2 until provider adoption and repeat injection volume confirm."),
    Round263ShadowWeightRow(E2RArchetype.UNAPPROVED_TOXIN_SAFETY_TRUST_4C, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, -5, 5, 5, 5, "Unauthorized toxin distribution is a safety/trust gate, not a Green source."),
    Round263ShadowWeightRow(E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE, 0, 0, 0, 0, 5, 5, 2, 4, 5, 3, -5, 5, 5, 5, "AUC and external validation need reimbursement, adoption and revenue bridge."),
    Round263ShadowWeightRow(E2RArchetype.MEDICAL_SERVICE_DISRUPTION_POLICY_4C, 5, 0, 0, 0, 0, 3, 0, 5, 0, 0, -4, 5, 5, 5, "Policy relief is not Green while procedure volume and hospital utilization are disrupted."),
    Round263ShadowWeightRow(E2RArchetype.DENTAL_IMPLANT_GLOBAL_M_AND_A, 3, 2, 2, 3, 2, 2, 4, 3, 4, 3, -5, 4, 5, 4, "M&A target rally is event premium until close, integration and listed bridge are visible."),
)


ROUND263_DEEP_SUB_ARCHETYPES: tuple[Round263DeepSubArchetype, ...] = (
    Round263DeepSubArchetype("미용의료기기 EBD buyout", E2RArchetype.AESTHETIC_EBD_GLOBAL_BUYOUT, ("Jeisys Medical", "ArchiMed", "EBD", "HIFU", "RF", "laser", "body contouring", "delisting")),
    Round263DeepSubArchetype("Beauty device crossover", E2RArchetype.BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER, ("APR", "Medicube", "at-home beauty device", "TikTok", "overseas revenue")),
    Round263DeepSubArchetype("Aesthetic export platform", E2RArchetype.AESTHETIC_DEVICE_EXPORT_PLATFORM, ("Classys", "Bain Capital", "60 countries", "installed base", "consumables")),
    Round263DeepSubArchetype("톡신 U.S. launch", E2RArchetype.BOTULINUM_TOXIN_US_LAUNCH, ("Hugel", "Letybo", "FDA approval", "provider adoption", "Botox price")),
    Round263DeepSubArchetype("톡신 safety trust", E2RArchetype.UNAPPROVED_TOXIN_SAFETY_TRUST_4C, ("Medytox", "Innotox", "DIY injection", "UK unlicensed", "FDA warning")),
    Round263DeepSubArchetype("의료AI validation not revenue", E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE, ("Lunit", "INSIGHT DBT", "AUC", "subgroup weakness", "reimbursement")),
    Round263DeepSubArchetype("의료서비스 policy disruption", E2RArchetype.MEDICAL_SERVICE_DISRUPTION_POLICY_4C, ("doctors strike", "medical quota", "emergency care", "surgery delay", "hospital utilization")),
    Round263DeepSubArchetype("치과 implant M&A", E2RArchetype.DENTAL_IMPLANT_GLOBAL_M_AND_A, ("Osstem Implant", "ZimVie", "delisted buyer", "takeover rumor", "integration")),
)


ROUND263_CASE_CANDIDATES: tuple[Round263CaseCandidate, ...] = (
    Round263CaseCandidate(
        case_id="r7_loop12_jeisys_medical_ebd_global_buyout",
        symbol="287410",
        company_name="Jeisys Medical",
        primary_archetype=E2RArchetype.AESTHETIC_EBD_GLOBAL_BUYOUT,
        secondary_archetypes=(E2RArchetype.AESTHETIC_DEVICE_EXPORT_KOREA, E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT),
        case_type="success_candidate",
        round_case_type="structural_success_candidate / PE buyout",
        stage1_date=date(2024, 6, 1),
        stage2_date=date(2024, 9, 11),
        stage3_date=None,
        stage4b_date=date(2024, 9, 11),
        stage4c_date=None,
        stage3_decision="business_quality_validated_but_public_equity_tracking_closed_after_delisting",
        stage4b_status="4B-watch buyout and delisting premium closes public path",
        hard_4c_confirmed=False,
        evidence_fields=("archimed_742mn_usd_acquisition", "jeisys_close_12860_krw", "revenue_cagr_44pct", "adjusted_pretax_earnings_cagr_45pct", "global_ebd_market_expected_16bn_usd"),
        red_flag_fields=("delisting_tracking_gap", "buyout_premium_not_public_stage3", "integration_leverage_risk"),
        price_data_source="WSJ ArchiMed / Jeisys acquisition anchor",
        reported_price_anchor="Jeisys shares closed at 12,860 KRW before delisting process; ArchiMed acquisition about $742M",
        reported_return_anchor="Business quality validated, but public post-event OHLC is unsuitable after delisting",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=12860.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"deal_value_usd_mn": 742.0, "fy2023_revenue_usd_mn": 107.0, "fy2023_adjusted_pretax_earnings_usd_mn": 31.0, "revenue_cagr_pct": 44.0, "adjusted_pretax_earnings_cagr_pct": 45.0, "deal_value_to_revenue_x": 6.93, "deal_value_to_adjusted_pretax_earnings_x": 23.9, "global_ebd_market_prior_usd_bn": 4.5, "global_ebd_market_2032_expected_usd_bn_min": 16.0, "market_growth_multiple_min": 3.56},
        score_price_alignment="aligned",
        round_alignment_label="business_validated_delisting_tracking_gap",
        rerating_result="true_rerating",
        round_rerating_label="aesthetic_EBD_business_quality_validated",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="public_equity_tracking_closed_after_delisting",
        price_validation_status="reported_transaction_anchor_delisting_no_full_ohlc",
        notes="EBD business quality is validated, but delisting prevents listed-equity Stage 3 path tracking.",
    ),
    Round263CaseCandidate(
        case_id="r7_loop12_apr_medicube_device_crossover",
        symbol="278470",
        company_name="APR / Medicube device",
        primary_archetype=E2RArchetype.BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION, E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT),
        case_type="success_candidate",
        round_case_type="structural_success_candidate + 4B-watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 10, 20),
        stage3_date=None,
        stage4b_date=date(2025, 10, 20),
        stage4c_date=None,
        stage3_decision="beauty_device_growth_is_strong_but_green_needs_repeat_revenue_channel_durability_and_regulatory_boundary",
        stage4b_status="4B-watch more-than-four-fold stock rise and device concentration",
        hard_4c_confirmed=False,
        evidence_fields=("stock_more_than_fourfold_since_january_2025", "market_value_about_6bn_usd", "device_180_usd", "device_one_third_us_sales", "overseas_revenue_nearly_80pct_q2_2025", "revenue_7x_since_2018"),
        red_flag_fields=("single_device_concentration", "viral_social_commerce_demand", "clinic_crossover_unconfirmed", "regulatory_boundary_watch"),
        price_data_source="FT APR / beauty-device anchor",
        reported_price_anchor="APR stock more than four-fold since January 2025; market value about $6B",
        reported_return_anchor="MFE from January 2025 greater than +300%; no full adjusted OHLC in this pass",
        mfe_1d=300.0,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"reported_stock_return_since_january_2025_min_pct": 300.0, "market_value_usd_bn": 6.0, "device_price_usd": 180.0, "device_share_of_us_sales_pct_approx": 33.3, "q2_2025_overseas_revenue_share_pct_nearly": 80.0, "revenue_growth_since_2018_x": 7.0},
        score_price_alignment="aligned",
        round_alignment_label="aligned_partial_4B_concentration_watch",
        rerating_result="true_rerating",
        round_rerating_label="beauty_device_structural_rerating_candidate",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="current_state_4B_concentration_watch",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="APR device demand has revenue evidence, but concentration/channel/regulatory durability must be proven before Green.",
    ),
    Round263CaseCandidate(
        case_id="r7_loop12_classys_aesthetic_device_export_platform",
        symbol="214150",
        company_name="Classys",
        primary_archetype=E2RArchetype.AESTHETIC_DEVICE_EXPORT_PLATFORM,
        secondary_archetypes=(E2RArchetype.AESTHETIC_DEVICE_EXPORT_KOREA, E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT),
        case_type="success_candidate",
        round_case_type="success_candidate / insufficient_price_data",
        stage1_date=date(2022, 1, 1),
        stage2_date=date(2025, 1, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="export_platform_stage2_but_green_needs_installed_base_consumables_opm_and_fcf",
        stage4b_status="4B-watch if K-aesthetic premium or acquirer rumor moves before utilization data",
        hard_4c_confirmed=False,
        evidence_fields=("exports_to_60_plus_countries", "non_invasive_aesthetic_treatment_technology", "bain_60_84pct_stake", "bain_transaction_670bn_krw"),
        red_flag_fields=("installed_base_unconfirmed", "consumable_attach_rate_unconfirmed", "overseas_opm_unconfirmed", "reliable_event_price_anchor_unavailable"),
        price_data_source="public company profile / secondary summary",
        reported_price_anchor="Classys exports to 60+ countries; Bain acquired 60.84% stake for 670B KRW",
        reported_return_anchor="Business/export anchor confirmed, but reliable event return or full OHLC unavailable",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"bain_stake_pct": 60.84, "bain_transaction_value_krw_bn": 670.0, "export_countries_min": 60.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_insufficient_price_data",
        rerating_result="unknown",
        round_rerating_label="aesthetic_device_export_platform_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="business_quality_without_price_validation",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Aesthetic export platform is Stage 2; installed base, consumables, OPM, FCF and price path are missing.",
    ),
    Round263CaseCandidate(
        case_id="r7_loop12_hugel_letybo_us_toxin_launch",
        symbol="145020",
        company_name="Hugel / Letybo",
        primary_archetype=E2RArchetype.BOTULINUM_TOXIN_US_LAUNCH,
        secondary_archetypes=(E2RArchetype.BOTULINUM_US_MARKET_ENTRY, E2RArchetype.BOTULINUM_AESTHETIC_REGULATED),
        case_type="success_candidate",
        round_case_type="success_candidate / U.S. toxin launch",
        stage1_date=date(2024, 2, 1),
        stage2_date=date(2025, 3, 31),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="fda_approval_and_price_advantage_are_not_green_until_provider_adoption_repeat_volume_asp_and_margin",
        stage4b_status="4B-watch if FDA approval or cheaper-than-Botox narrative rerates before procedure volume",
        hard_4c_confirmed=False,
        evidence_fields=("letybo_fda_approval_glabellar_lines", "us_dermatology_office_launch", "letybo_9_12_usd_per_unit", "botox_12_18_usd_per_unit", "relative_discount_25_33pct"),
        red_flag_fields=("provider_adoption_unconfirmed", "repeat_injection_volume_unconfirmed", "asp_margin_unconfirmed", "counterfeit_unapproved_toxin_confusion"),
        price_data_source="Allure / NY Post U.S. launch and price anchors",
        reported_price_anchor="Letybo estimated $9~12/unit vs Botox $12~18/unit; appearing in U.S. dermatologist offices by March 2025",
        reported_return_anchor="Launch Stage 2; Hugel stock OHLC unavailable in this pass",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"letybo_unit_price_low_usd": 9.0, "letybo_unit_price_high_usd": 12.0, "botox_unit_price_low_usd": 12.0, "botox_unit_price_high_usd": 18.0, "letybo_25_unit_cost_low_usd": 225.0, "letybo_25_unit_cost_high_usd": 300.0, "botox_25_unit_cost_low_usd": 300.0, "botox_25_unit_cost_high_usd": 450.0, "relative_unit_price_discount_low_case_pct": 33.3, "relative_unit_price_discount_high_case_pct": 25.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="U.S._botulinum_toxin_launch_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="approval_not_green_until_provider_adoption_margin",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="FDA approval and price advantage are Stage 2; provider adoption and repeat injection economics are required.",
    ),
    Round263CaseCandidate(
        case_id="r7_loop12_medytox_innotox_unauthorized_distribution",
        symbol="086900",
        company_name="Medytox / Innotox",
        primary_archetype=E2RArchetype.UNAPPROVED_TOXIN_SAFETY_TRUST_4C,
        secondary_archetypes=(E2RArchetype.DEVICE_SAFETY_CHANNEL_OVERLAY, E2RArchetype.BOTULINUM_AESTHETIC_REGULATED),
        case_type="4b_watch",
        round_case_type="4C-watch / safety trust",
        stage1_date=date(2025, 7, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 7, 1),
        stage3_decision="unauthorized_distribution_and_patient_safety_risk_block_green",
        stage4b_status="4C-watch unauthorized distribution and safety trust gate",
        hard_4c_confirmed=False,
        evidence_fields=("innotox_online_diy_injection_trend", "uk_unlicensed_status", "medytox_luvantas_investigating_unauthorized_importation", "fda_warning_context_unapproved_botulinum_toxins"),
        red_flag_fields=("unauthorized_distribution_risk", "patient_safety_risk", "brand_trust_risk", "fda_warning_context"),
        price_data_source="Guardian / People safety-regulatory anchors",
        reported_price_anchor="Unauthorized Innotox online/DIY injection trend; UK unlicensed status; FDA unapproved toxin warning context",
        reported_return_anchor="Safety-trust 4C-watch; no reliable Medytox event OHLC in this pass",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"uk_license_status": "not licensed for use in the UK", "hard_4c_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="toxin_safety_distribution_trust_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4C_watch_not_hard_4C",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Unauthorized toxin distribution is a safety/trust watch and blocks Green until resolved.",
    ),
    Round263CaseCandidate(
        case_id="r7_loop12_lunit_insight_dbt_validation_not_revenue",
        symbol="328130",
        company_name="Lunit / INSIGHT DBT",
        primary_archetype=E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION_NOT_REVENUE,
        secondary_archetypes=(E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION, E2RArchetype.MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK),
        case_type="failed_rerating",
        round_case_type="insufficient_evidence / validation not revenue",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 3, 17),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 3, 17),
        stage3_decision="external_validation_not_green_before_reimbursement_hospital_adoption_and_recurring_revenue",
        stage4b_status="4C-watch subgroup weakness and no revenue bridge",
        hard_4c_confirmed=False,
        evidence_fields=("screening_exam_count_163449", "screen_detected_cancers_1368", "overall_auc_0_91", "precision_0_08", "recall_0_73"),
        red_flag_fields=("non_invasive_cancer_auc_0_85", "calcification_auc_0_80", "dense_breast_auc_0_90", "reimbursement_absent", "hospital_adoption_absent", "recurring_revenue_absent"),
        price_data_source="arXiv external-validation evidence",
        reported_price_anchor="External validation of 163,449 exams; AUC 0.91 but no revenue bridge",
        reported_return_anchor="Medical AI validation, not Green; price path unavailable",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"exam_count": 163449.0, "positive_cases": 1368.0, "negative_exams": 162081.0, "overall_auc": 0.91, "precision": 0.08, "recall": 0.73, "non_invasive_cancer_auc": 0.85, "calcification_auc": 0.80, "dense_breast_auc": 0.90},
        score_price_alignment="unknown",
        round_alignment_label="insufficient_evidence",
        rerating_result="unknown",
        round_rerating_label="medical_AI_validation_watch",
        stage_failure_type="unknown",
        round_stage_failure_label="validation_not_reimbursement_or_revenue",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Aggregate AUC is useful validation, but Green needs reimbursement, adoption and recurring revenue.",
    ),
    Round263CaseCandidate(
        case_id="r7_loop12_medical_quota_doctors_strike_disruption",
        symbol="hospital/medtech/elective_procedure_basket",
        company_name="Medical-school quota / doctors' strike",
        primary_archetype=E2RArchetype.MEDICAL_SERVICE_DISRUPTION_POLICY_4C,
        secondary_archetypes=(E2RArchetype.REIMBURSEMENT_ACCESS_OVERLAY, E2RArchetype.COMMERCIALIZATION_FAILURE_OVERLAY),
        case_type="4b_watch",
        round_case_type="medical-service 4C-watch",
        stage1_date=date(2024, 2, 20),
        stage2_date=date(2026, 2, 10),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 3, 7),
        stage3_decision="policy_resolution_or_quota_change_is_not_green_without_procedure_volume_hospital_utilization_and_reimbursement",
        stage4b_status="4C-watch medical-service disruption and policy risk",
        hard_4c_confirmed=False,
        evidence_fields=("trainee_doctors_walkout", "13_month_dispute", "90pct_trainee_doctors_resigned", "emergency_care_and_surgery_delays", "quota_3058_to_3548_2027_and_3871_2030"),
        red_flag_fields=("medical_service_disruption", "procedure_volume_unconfirmed", "hospital_utilization_unconfirmed", "policy_uncertainty"),
        price_data_source="Reuters / AP medical-crisis policy anchors",
        reported_price_anchor="90% trainee doctors resigned during dispute; quota plan 3,058 to 3,548 in 2027 and 3,871 by 2030",
        reported_return_anchor="Policy disruption/relief; listed healthcare stock OHLC unavailable",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"dispute_duration_months": 13.0, "trainee_doctor_resignation_share_pct": 90.0, "original_medical_quota": 3058.0, "quota_2027": 3548.0, "quota_2030": 3871.0, "quota_2027_increase_pct": 16.0, "quota_2030_increase_pct": 26.6},
        score_price_alignment="unknown",
        round_alignment_label="thesis_break_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="healthcare_service_policy_disruption_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="policy_event_not_procedure_volume_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Medical quota policy is not Green until procedure volume, utilization and reimbursement are visible.",
    ),
    Round263CaseCandidate(
        case_id="r7_loop12_osstem_zimvie_dental_mna_event",
        symbol="delisted_Osstem/ZIMV",
        company_name="Osstem Implant / ZimVie",
        primary_archetype=E2RArchetype.DENTAL_IMPLANT_GLOBAL_M_AND_A,
        secondary_archetypes=(E2RArchetype.MEDICAL_DEVICE_DENTAL_IMPLANT, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium / global dental M&A validation",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 7, 18),
        stage3_date=None,
        stage4b_date=date(2024, 7, 18),
        stage4c_date=None,
        stage3_decision="mna_rumor_and_target_rally_are_not_korean_listed_green_before_close_integration_margin_and_debt",
        stage4b_status="4B-watch target rally before confirmed transaction close",
        hard_4c_confirmed=False,
        evidence_fields=("osstem_delisted_2023", "zimvie_plus_12_5pct", "zimvie_event_price_21_31_usd", "zimvie_market_cap_517mn_usd_prior_close", "reported_final_bid_not_confirmed_close"),
        red_flag_fields=("delisted_buyer_tracking_gap", "mna_rumor_only", "transaction_close_unconfirmed", "integration_debt_margin_unconfirmed"),
        price_data_source="Investors.com / Bloomberg-reported takeover rumor anchor",
        reported_price_anchor="ZimVie +12.5% to $21.31 on takeover rumor; Osstem delisted in 2023",
        reported_return_anchor="M&A event premium, not Korean listed Green",
        mfe_1d=12.5,
        mae_1d=None,
        stage2_price_anchor=21.31,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"zimvie_event_price_usd": 21.31, "zimvie_event_mfe_pct": 12.5, "zimvie_market_cap_prior_usd_mn": 517.0, "korean_listed_price_available": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium",
        rerating_result="event_premium",
        round_rerating_label="dental_implant_global_M&A_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="delisted_buyer_and_unconfirmed_M&A_not_green",
        price_validation_status="reported_target_event_anchor_delisted_buyer_no_ohlc",
        notes="Target-stock event return validates M&A interest, but delisted buyer and unconfirmed close block Green.",
    ),
)


def round263_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND263_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND263_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round263 R7 Loop-12 biotech/healthcare/device price validation case. "
                "Calibration-only; not candidate-generation input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if any(token in field for token in ("procedure", "provider", "revenue", "installed", "consumable", "margin", "fcf", "adoption"))
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if any(token in field for token in ("premium", "rally", "mfe", "event", "fourfold", "mna", "buyout", "viral", "delisting"))
            ),
            stage4c_evidence=tuple(
                field
                for field in (*candidate.red_flag_fields, *candidate.evidence_fields)
                if any(token in field for token in ("safety", "unauthorized", "subgroup", "disruption", "reimbursement", "adoption", "policy", "counterfeit", "delisted"))
            ),
            must_have_fields=ROUND263_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4b_watch", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND263_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "hard_4c_confirmed_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_procedure_volume_installed_base_consumables_provider_adoption_reimbursement_or_stage_prices",
                "do_not_treat_fda_approval_mna_auc_k_aesthetic_ai_diagnosis_or_medical_policy_as_green_alone",
                *ROUND263_GREEN_REQUIRED_FIELDS,
                *ROUND263_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
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


def round263_case_rows() -> tuple[dict[str, str], ...]:
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
            "price_data_source": candidate.price_data_source,
            "reported_price_anchor": candidate.reported_price_anchor,
            "reported_return_anchor": candidate.reported_return_anchor,
            "mfe_1d": _float_text(candidate.mfe_1d),
            "mae_1d": _float_text(candidate.mae_1d),
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
        for candidate in ROUND263_CASE_CANDIDATES
    )


def round263_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND263_SCORE_ADJUSTMENTS)


def round263_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND263_SHADOW_WEIGHT_ROWS)


def round263_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND263_DEEP_SUB_ARCHETYPES)


def round263_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round263_price_validation": "true"} for field in ROUND263_PRICE_VALIDATION_FIELDS)


def round263_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round263_label": label, "canonical_archetype": canonical} for label, canonical in ROUND263_REQUIRED_TARGET_ALIASES.items())


def round263_summary() -> dict[str, int | bool | str]:
    cases = ROUND263_CASE_CANDIDATES
    return {
        "source_round": ROUND263_SOURCE_ROUND_PATH,
        "round_id": ROUND263_ROUND_ID,
        "large_sector": ROUND263_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "watch_case_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C-watch" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "reported_price_anchor_count": sum(1 for case in cases if case.price_validation_status != "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND263_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND263_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND263_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round263_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND263_SOURCE_ROUND_PATH,
        "round_id": ROUND263_ROUND_ID,
        "large_sector": ROUND263_LARGE_SECTOR,
        "summary": round263_summary(),
        "target_aliases": dict(ROUND263_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND263_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND263_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND263_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND263_HARD_4C_GATES),
        "score_adjustments": list(round263_score_adjustment_rows()),
        "shadow_weights": list(round263_shadow_weight_rows()),
        "deep_sub_archetypes": list(round263_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND263_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round263_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_fda_approval_mna_auc_k_aesthetic_ai_diagnosis_or_medical_policy_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round263_summary_markdown() -> str:
    summary = round263_summary()
    lines = [
        "# Round 263 R7 Loop 12 Biotech Healthcare Device Price Validation",
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
        f"- watch_cases: {summary['watch_case_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND263_CASE_CANDIDATES:
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
            "- Aesthetic device buyouts validate business quality, but delisting can close public Stage 3 tracking.",
            "- Beauty-device growth needs repeat demand and channel durability, not viral demand alone.",
            "- FDA approval and AI AUC are Stage 2 until adoption, reimbursement and revenue conversion confirm.",
            "- Unauthorized toxin distribution and medical-service disruption are 4C-watch, not Green evidence.",
            "- Dental M&A rumor is event premium until close, integration and public listed bridge are visible.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round263_green_gate_review_markdown() -> str:
    lines = [
        "# Round 263 R7 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R7 Stage 3-Green is not `FDA approval`, `M&A`, `AUC`, `K-aesthetic`, `AI diagnosis`, or `medical policy`. It requires procedure/prescription volume, installed base/utilization, consumables or repeat treatment, provider/hospital adoption, reimbursement or self-pay ASP, gross margin/FCF, safety trust, and price path after evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND263_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND263_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND263_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `FDA approval` is Stage 2; Green needs repeat procedures and ASP/margin.",
            "- `AUC 0.91` is useful validation; Green needs reimbursement and hospital adoption.",
            "- `ZimVie +12.5% on rumor` is M&A event premium, not Korean listed Stage 3.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round263_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 263 R7 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND263_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND263_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | interpretation |", "|---|---|---|---|"])
    for case in ROUND263_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round263_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 263 R7 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, procedure volume, installed base, consumable attach-rate, provider adoption, reimbursement, FCF, or safety resolution where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND263_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND263_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round263_r7_loop12_reports(
    output_directory: str | Path = ROUND263_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND263_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND263_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round263_case_records(), cases_path),
        "audit": _write_json(round263_audit_payload(), audit_path),
        "summary": output / "round263_r7_loop12_price_validation_summary.md",
        "case_matrix": output / "round263_r7_loop12_case_matrix.csv",
        "target_aliases": output / "round263_r7_loop12_target_aliases.csv",
        "score_adjustments": output / "round263_r7_loop12_score_adjustments.csv",
        "shadow_weights": output / "round263_r7_loop12_shadow_weights.csv",
        "deep_sub_archetypes": output / "round263_r7_loop12_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round263_r7_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round263_r7_loop12_green_gate_review.md",
        "price_validation_plan": output / "round263_r7_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round263_r7_loop12_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round263_summary_markdown(), encoding="utf-8")
    _write_csv(round263_case_rows(), paths["case_matrix"])
    _write_csv(round263_target_alias_rows(), paths["target_aliases"])
    _write_csv(round263_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round263_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round263_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round263_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round263_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round263_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round263_stage4b_4c_review_markdown(), encoding="utf-8")
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
