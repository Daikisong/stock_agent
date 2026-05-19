"""Round-198 R7 Loop-7 biotech/healthcare/device price-path validation pack.

Round 198 is a calibration-only layer for Korean oncology royalty,
botulinum/aesthetic launch, biosimilar tariff-hedge manufacturing, CDMO/CMO
M&A, large CDMO 4B benchmarking, and medical-AI external validation cases. It
records why approval news, clinical headlines, partner peak-sales targets,
papers, and M&A announcements must be separated from prescription volume,
reimbursement, commercial revenue, royalty recognition, utilization, margin,
cash runway, and dilution risk.

Simple example: FDA approval can be strong Stage 2 evidence. It is not
Stage 3-Green until prescriptions, payer access, revenue, royalty, EPS/FCF, and
cash-runway quality are visible as-of the case date.

This module is report/evaluation material only. Production candidate
generation, feature engineering, scoring, staging, and RedTeam code must not
import it.
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


ROUND198_SOURCE_ROUND_PATH = "docs/round/round_198.md"
ROUND198_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round198_r7_loop7_biotech_healthcare_device_price_validation"
ROUND198_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_loop7_round198.jsonl"
ROUND198_DEFAULT_AUDIT_PATH = (
    "data/sector_taxonomy/round198_r7_loop7_biotech_healthcare_device_price_validation_audit.json"
)

ROUND198_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BIOTECH_ROYALTY_COMMERCIALIZATION": E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION.value,
    "KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION": E2RArchetype.KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION.value,
    "BIOSIMILAR_COMMERCIALIZATION": E2RArchetype.BIOSIMILAR_COMMERCIALIZATION.value,
    "BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING": E2RArchetype.BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING.value,
    "CDMO_HEALTHCARE_CONTRACT": E2RArchetype.CDMO_HEALTHCARE_CONTRACT.value,
    "CDMO_US_TARIFF_HEDGE_CAPACITY": E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY.value,
    "MEDICAL_DEVICE_HEALTHCARE_EXPORT": E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT.value,
    "BOTULINUM_US_MARKET_ENTRY": E2RArchetype.BOTULINUM_US_MARKET_ENTRY.value,
    "DIGITAL_HEALTHCARE_AI": E2RArchetype.DIGITAL_HEALTHCARE_AI.value,
    "MEDICAL_AI_EXTERNAL_VALIDATION": E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION.value,
    "MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK": E2RArchetype.MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK.value,
    "APPROVAL_ONLY_NOT_COMMERCIALIZATION": E2RArchetype.APPROVAL_ONLY_NOT_COMMERCIALIZATION.value,
    "REIMBURSEMENT_ACCESS_OVERLAY": E2RArchetype.REIMBURSEMENT_ACCESS_OVERLAY.value,
    "COMMERCIALIZATION_FAILURE_OVERLAY": E2RArchetype.COMMERCIALIZATION_FAILURE_OVERLAY.value,
    "MANUFACTURING_INSPECTION_CRL_OVERLAY": E2RArchetype.MANUFACTURING_INSPECTION_CRL_OVERLAY.value,
    "DEVICE_SAFETY_COUNTERFEIT_OVERLAY": E2RArchetype.DEVICE_SAFETY_COUNTERFEIT_OVERLAY.value,
    "BIOTECH_PRE_REVENUE_REGULATORY": E2RArchetype.BIOTECH_PRE_REVENUE_REGULATORY.value,
    "CAPITAL_ALLOCATION_DILUTION_OVERLAY": E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY.value,
}

ROUND198_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "approval_or_regulatory_clearance",
    "commercial_launch",
    "prescription_volume_or_hospital_adoption",
    "reimbursement_or_payer_access",
    "revenue_recognition",
    "royalty_or_gross_margin_confirmed",
    "cash_runway_and_dilution_risk_passed",
    "partner_execution_risk_passed",
    "price_path_after_commercial_evidence",
)

ROUND198_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "approval_news_only",
    "clinical_headline_only",
    "paper_validation_without_revenue",
    "partner_peak_sales_without_royalty_visibility",
    "mna_announcement_only",
    "fda_clearance_without_sales",
    "cash_runway_short",
    "large_dilution_or_cb_risk",
)

ROUND198_STAGE4B_STATUSES: tuple[str, ...] = ("none", "watch", "elevated", "graduated")

ROUND198_HARD_4C_GATES: tuple[str, ...] = (
    "fda_crl_or_approval_rejection",
    "efficacy_or_safety_crl",
    "clinical_failure",
    "commercialization_failure",
    "prescription_volume_miss",
    "reimbursement_failure",
    "royalty_not_recognized",
    "large_dilution",
    "cash_runway_collapse",
    "manufacturing_inspection_failure",
    "product_safety_issue",
    "subgroup_clinical_performance_failure",
    "partner_launch_failure",
)

ROUND198_PRICE_BACKFILL_FIELDS: tuple[str, ...] = (
    "stage1_date",
    "stage2_date",
    "stage3_date",
    "stage4b_date",
    "stage4c_date",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_date",
    "peak_price",
    "MFE_5D",
    "MFE_20D",
    "MFE_30D",
    "MFE_60D",
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_5D",
    "MAE_20D",
    "MAE_30D",
    "MAE_60D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "MAE_2Y",
    "drawdown_after_peak",
    "relative_strength_vs_kospi",
    "relative_strength_vs_biotech_basket",
    "relative_strength_vs_cdmo_basket",
    "relative_strength_vs_medical_device_basket",
    "approval_date",
    "commercial_launch_date",
    "prescription_volume",
    "reimbursement_status",
    "commercial_revenue",
    "royalty_recognition",
    "gross_margin",
    "contract_backlog",
    "capacity_utilization",
    "cash_runway_months",
    "dilution_or_cb_flag",
    "manufacturing_inspection_issue_flag",
    "efficacy_safety_crl_flag",
    "external_validation_flag",
    "subgroup_performance_risk_flag",
    "mna_without_utilization_flag",
    "stage4b_status",
    "hard_4c_confirmed",
)


@dataclass(frozen=True)
class Round198ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {
            "axis": self.axis,
            "points": str(self.points),
            "direction": self.direction,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class Round198CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
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
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND198_SCORE_ADJUSTMENTS: tuple[Round198ScoreAdjustment, ...] = (
    Round198ScoreAdjustment("commercial_revenue", 5, "raise", "R7 Stage 3는 승인 뉴스가 아니라 실제 상업화 매출에서 시작한다."),
    Round198ScoreAdjustment("prescription_volume", 5, "raise", "신약/보툴리눔은 처방량과 시술 채널 침투가 핵심이다."),
    Round198ScoreAdjustment("royalty_recognition", 5, "raise", "파트너 peak sales보다 실제 로열티 인식이 중요하다."),
    Round198ScoreAdjustment("reimbursement_access", 4, "raise", "보험/급여 접근이 없으면 처방과 매출 ramp가 제한된다."),
    Round198ScoreAdjustment("contract_backlog", 4, "raise", "CDMO/CMO는 수주잔고가 있어야 가동률과 FCF로 이어진다."),
    Round198ScoreAdjustment("capacity_utilization", 4, "raise", "공장 인수나 CAPA는 실제 가동률 확인 전까지 Stage 2다."),
    Round198ScoreAdjustment("gross_margin_visibility", 4, "raise", "매출이 gross margin과 FCF로 내려와야 체급 변화다."),
    Round198ScoreAdjustment("cash_runway", 4, "raise", "현금 runway와 dilution risk 통과는 바이오 Green의 기본 안전장치다."),
    Round198ScoreAdjustment("us_commercial_launch_with_sales", 3, "raise", "미국 출시 자체보다 매출이 붙은 launch가 강하다."),
    Round198ScoreAdjustment("external_validation_with_adoption", 3, "raise", "의료AI 외부검증은 병원 도입/수가와 연결될 때 강하다."),
    Round198ScoreAdjustment("approval_news_only", -5, "lower", "승인 뉴스만으로는 Stage 3-Green을 만들지 않는다."),
    Round198ScoreAdjustment("clinical_headline_only", -5, "lower", "임상 헤드라인은 상업화 전까지 Stage 1~2다."),
    Round198ScoreAdjustment("paper_validation_without_revenue", -4, "lower", "논문 성능만 있고 매출/수가가 없으면 제한한다."),
    Round198ScoreAdjustment("mna_without_utilization", -3, "lower", "M&A 공장 인수는 가동률/계약 전까지 event watch다."),
    Round198ScoreAdjustment("fda_approval_without_reimbursement", -4, "lower", "FDA 승인 후에도 payer access가 없으면 매출 ramp가 제한된다."),
    Round198ScoreAdjustment("partner_peak_sales_without_royalty_visibility", -3, "lower", "파트너 peak sales 목표만으로 로열티를 발명하지 않는다."),
    Round198ScoreAdjustment("pre_revenue_biotech_story", -5, "lower", "매출 전 바이오 narrative는 Green 금지에 가깝다."),
    Round198ScoreAdjustment("cash_burn_or_dilution_risk", -5, "lower", "cash burn과 유증/CB 위험은 hard RedTeam이다."),
    Round198ScoreAdjustment("manufacturing_inspection_issue", -3, "lower", "제조시설 CRL은 상업화 지연 watch지만 효능/안전성 CRL과 분리한다."),
    Round198ScoreAdjustment("subgroup_performance_risk", -3, "lower", "의료AI subgroup 성능 리스크는 Green 확신을 낮춘다."),
)


ROUND198_CASE_CANDIDATES: tuple[Round198CaseCandidate, ...] = (
    Round198CaseCandidate(
        case_id="yuhan_lazertinib_fda_approval_royalty_commercialization_watch",
        symbol="000100",
        company_name="유한양행",
        primary_archetype=E2RArchetype.BIOTECH_ROYALTY_COMMERCIALIZATION,
        secondary_archetypes=(
            E2RArchetype.KOREA_ONCOLOGY_DRUG_COMMERCIALIZATION,
            E2RArchetype.APPROVAL_ONLY_NOT_COMMERCIALIZATION,
            E2RArchetype.MANUFACTURING_INSPECTION_CRL_OVERLAY,
        ),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2024, 8, 20),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_prescription_volume_jj_sales_yuhan_royalty_recognition_eps_revision_and_sc_convenience_risk_passed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=(
            "fda_approval_rybrevant_lazertinib_first_line_egfr_nsclc",
            "mariposa_late_stage_data",
            "jj_peak_sales_expectation_above_5b_usd",
            "global_partner_commercialization",
        ),
        red_flag_fields=(
            "prescription_volume_unverified",
            "royalty_recognition_unverified",
            "eps_revision_unverified",
            "2024_12_16_sc_formulation_manufacturing_inspection_crl_watch_not_hard_4c",
        ),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="FDA approval is strong Stage 2, but Stage 3 waits for prescriptions, J&J sales, Yuhan royalty, and EPS revision.",
    ),
    Round198CaseCandidate(
        case_id="hugel_letybo_us_launch_botulinum_commercialization_watch",
        symbol="145020",
        company_name="휴젤",
        primary_archetype=E2RArchetype.BOTULINUM_US_MARKET_ENTRY,
        secondary_archetypes=(E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT, E2RArchetype.DEVICE_SAFETY_COUNTERFEIT_OVERLAY),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2025, 3, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_us_sales_channel_penetration_asp_margin_repeat_order_and_safety_risk_passed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("letybo_fda_approval", "us_dermatology_office_launch", "botox_competitor_narrative", "repeat_treatment_demand_option"),
        red_flag_fields=("us_sales_absent", "approval_only_risk", "price_competition", "safety_or_counterfeit_risk", "channel_rollout_unverified"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="US launch is strong Stage 2, but Green waits for US sales, channel penetration, ASP, margin, and repeat orders.",
    ),
    Round198CaseCandidate(
        case_id="celltrion_us_facility_biosimilar_tariff_hedge_stage2_watch",
        symbol="068270",
        company_name="셀트리온",
        primary_archetype=E2RArchetype.BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING,
        secondary_archetypes=(E2RArchetype.BIOSIMILAR_COMMERCIALIZATION, E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY),
        case_type="success_candidate",
        stage1_date=date(2025, 7, 29),
        stage2_date=date(2025, 9, 23),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_product_transfer_fda_quality_readiness_utilization_tariff_savings_gross_margin_and_fcf",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=(
            "us_pharma_factory_preferred_bidder_tariff_hedge",
            "imclone_systems_330m_usd_acquisition",
            "us_manufacturing_facility_secured",
            "future_launch_tariff_protection",
        ),
        red_flag_fields=("utilization_unverified", "capex_burden", "integration_delay", "tariff_policy_reversal", "biosimilar_price_competition"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="US facility acquisition is Stage 2 tariff-hedge evidence, not Stage 3 before transfer, utilization, margin, and FCF.",
    ),
    Round198CaseCandidate(
        case_id="sk_bioscience_idt_biologika_cmo_transition_event_watch",
        symbol="302440",
        company_name="SK바이오사이언스",
        primary_archetype=E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        secondary_archetypes=(E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY, E2RArchetype.APPROVAL_ONLY_NOT_COMMERCIALIZATION),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=date(2024, 6, 27),
        stage4c_date=None,
        stage3_decision="deferred_until_idt_contract_backlog_utilization_customer_margin_integration_cost_and_fcf",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("idt_biologika_60pct_acquisition", "global_vaccine_cmo_footprint", "post_covid_cmo_transition", "event_day_price_up_11_7pct_anchor"),
        red_flag_fields=("mna_without_utilization", "integration_cost_unverified", "cash_burn_watch", "new_order_failure_watch", "event_premium_watch"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="IDT acquisition can be Stage 2 CMO transition evidence, while the event-day rally is not Green before utilization and backlog.",
    ),
    Round198CaseCandidate(
        case_id="samsung_biologics_us_gsk_facility_cdmo_4b_benchmark",
        symbol="207940",
        company_name="삼성바이오로직스",
        primary_archetype=E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY,
        secondary_archetypes=(E2RArchetype.CDMO_HEALTHCARE_CONTRACT, E2RArchetype.CDMO_ADC_CELL_GENE_CAPABILITY),
        case_type="4b_watch",
        stage1_date=None,
        stage2_date=date(2025, 12, 22),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="existing_cdmo_success_anchor_not_new_stage3_in_round198_monitor_valuation_saturation_utilization_capex_return",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("gsk_rockville_facility_280m_usd_acquisition", "60000_liter_drug_substance_capacity", "us_long_term_demand_capacity_expansion", "tariff_hedge_option"),
        red_flag_fields=("large_cdmo_premium_known", "valuation_saturation_watch", "capex_return_unverified", "utilization_risk", "contract_slowdown_watch"),
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="green_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Samsung Biologics is a CDMO structural benchmark, but this round treats the US facility as 4B/saturation monitoring rather than a new Green.",
    ),
    Round198CaseCandidate(
        case_id="lunit_external_validation_medical_ai_commercialization_gap_watch",
        symbol="328130",
        company_name="루닛",
        primary_archetype=E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION,
        secondary_archetypes=(E2RArchetype.DIGITAL_HEALTHCARE_AI, E2RArchetype.MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK, E2RArchetype.REIMBURSEMENT_ACCESS_OVERLAY),
        case_type="failed_rerating",
        stage1_date=None,
        stage2_date=date(2025, 3, 17),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="forbidden_external_validation_without_reimbursement_hospital_adoption_recurring_revenue_arr_margin_and_cash_runway",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("external_validation_embed_dataset", "lunit_insight_dbt_auc_0_91", "medical_ai_diagnostic_performance"),
        red_flag_fields=("paper_validation_without_revenue", "subgroup_performance_risk", "reimbursement_unverified", "hospital_adoption_unverified", "cash_burn_watch"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="false_green",
        price_validation_status="needs_ohlc_backfill",
        notes="External validation can be Stage 2, but medical AI Green needs reimbursement, hospital adoption, recurring revenue, margin, and cash runway.",
    ),
    Round198CaseCandidate(
        case_id="r7_hard_4c_reliable_source_gap_watch",
        symbol="R7_HARD_4C_WATCH",
        company_name="R7 hard 4C source gap",
        primary_archetype=E2RArchetype.COMMERCIALIZATION_FAILURE_OVERLAY,
        secondary_archetypes=(E2RArchetype.MANUFACTURING_INSPECTION_CRL_OVERLAY, E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY),
        case_type="failed_rerating",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="hard_4c_not_confirmed_without_reliable_primary_or_major_source_for_crl_clinical_failure_cash_runway_dilution_or_commercialization_failure",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("r7_hard_4c_taxonomy_required", "source_gap_recorded", "do_not_force_4c_without_reliable_source"),
        red_flag_fields=("reliable_source_gap", "hard_4c_confirmation_deferred", "do_not_invent_failed_trial_or_dilution"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="unknown",
        price_validation_status="needs_ohlc_backfill",
        notes="Round198 intentionally does not force a named hard 4C case without reliable source/date evidence.",
    ),
)


def round198_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND198_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector.value,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round198 R7 Loop-7 biotech/healthcare/device price-path validation case. "
                "This is calibration-only and must not be used for candidate generation."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "approval" in field or "story" in field or "option" in field or "validation" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "royalty" in field or "commercialization" in field or "facility" in field or "capacity" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "price" in field or "premium" in field or "valuation" in field or "event" in field or "peak" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "crl" in field
                or "failure" in field
                or "safety" in field
                or "cash_burn" in field
                or "dilution" in field
                or "subgroup" in field
                or "reimbursement" in field
            ),
            must_have_fields=ROUND198_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4b_watch", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={
                "commercial_revenue_delta": 5.0,
                "prescription_volume_delta": 5.0,
                "royalty_recognition_delta": 5.0,
                "reimbursement_access_delta": 4.0,
                "contract_backlog_delta": 4.0,
                "capacity_utilization_delta": 4.0,
                "cash_runway_delta": 4.0,
                "approval_news_only_delta": -5.0,
                "paper_validation_without_revenue_delta": -4.0,
                "cash_burn_or_dilution_risk_delta": -5.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "needs_ohlc_backfill_true",
                "hard_4c_confirmed_false_in_this_pass",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_approval_clinical_paper_or_mna_headline_as_green_evidence",
                *ROUND198_GREEN_REQUIRED_FIELDS,
                *ROUND198_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8 if candidate.stage2_date or candidate.stage4b_date else 0.35,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round198_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND198_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "primary_archetype": candidate.primary_archetype.value,
                "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
                "case_type": candidate.case_type,
                "stage1_date": _date_text(candidate.stage1_date),
                "stage2_date": _date_text(candidate.stage2_date),
                "stage3_date": _date_text(candidate.stage3_date),
                "stage4b_date": _date_text(candidate.stage4b_date),
                "stage4c_date": _date_text(candidate.stage4c_date),
                "stage3_decision": candidate.stage3_decision,
                "stage4b_status": candidate.stage4b_status,
                "hard_4c_confirmed": str(candidate.hard_4c_confirmed).lower(),
                "score_price_alignment": candidate.score_price_alignment,
                "rerating_result": candidate.rerating_result,
                "stage_failure_type": candidate.stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round198_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND198_SCORE_ADJUSTMENTS)


def round198_price_backfill_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round198_backfill": "true"} for field in ROUND198_PRICE_BACKFILL_FIELDS)


def round198_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round198_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND198_REQUIRED_TARGET_ALIASES.items()
    )


def round198_summary() -> dict[str, int | bool]:
    cases = round198_case_records()
    return {
        "case_candidate_count": len(cases),
        "required_target_count": len(ROUND198_REQUIRED_TARGET_ALIASES),
        "score_adjustment_count": len(ROUND198_SCORE_ADJUSTMENTS),
        "price_backfill_field_count": len(ROUND198_PRICE_BACKFILL_FIELDS),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "stage4b_watch_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "hard_4c_case_count": sum(1 for case in ROUND198_CASE_CANDIDATES if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in ROUND198_CASE_CANDIDATES if case.stage3_date),
        "stage4b_watch_or_elevated_count": sum(
            1 for case in ROUND198_CASE_CANDIDATES if case.stage4b_status in {"watch", "elevated"}
        ),
        "source_gap_case_count": sum(1 for case in ROUND198_CASE_CANDIDATES if "source_gap" in case.case_id),
        "needs_ohlc_backfill_count": sum(1 for case in ROUND198_CASE_CANDIDATES if case.price_validation_status == "needs_ohlc_backfill"),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "needs_ohlc_backfill": True,
    }


def write_round198_r7_loop7_reports(
    *,
    output_directory: str | Path = ROUND198_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND198_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND198_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = write_case_library(round198_case_records(), cases_path)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "audit_json": audit,
        "summary": output / "round198_r7_loop7_price_validation_summary.md",
        "case_matrix": output / "round198_r7_loop7_case_matrix.csv",
        "target_aliases": output / "round198_r7_loop7_target_aliases.csv",
        "score_adjustments": output / "round198_r7_loop7_score_adjustments.csv",
        "price_backfill_fields": output / "round198_r7_loop7_price_backfill_fields.csv",
        "green_gate_review": output / "round198_r7_loop7_green_gate_review.md",
        "price_backfill_plan": output / "round198_r7_loop7_price_backfill_plan.md",
        "stage4b_4c_review": output / "round198_r7_loop7_stage4b_4c_review.md",
    }
    audit.write_text(json.dumps(round198_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round198_case_rows(), paths["case_matrix"])
    _write_rows(round198_target_alias_rows(), paths["target_aliases"])
    _write_rows(round198_score_adjustment_rows(), paths["score_adjustments"])
    _write_rows(round198_price_backfill_field_rows(), paths["price_backfill_fields"])
    paths["summary"].write_text(render_round198_summary_markdown(), encoding="utf-8")
    paths["green_gate_review"].write_text(render_round198_green_gate_review_markdown(), encoding="utf-8")
    paths["price_backfill_plan"].write_text(render_round198_price_backfill_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round198_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def round198_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND198_SOURCE_ROUND_PATH,
        "large_sector": Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE.value,
        "summary": round198_summary(),
        "target_aliases": list(round198_target_alias_rows()),
        "green_required_fields": list(ROUND198_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND198_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_statuses": list(ROUND198_STAGE4B_STATUSES),
        "hard_4c_gates": list(ROUND198_HARD_4C_GATES),
        "score_adjustments": list(round198_score_adjustment_rows()),
        "case_ids": [case.case_id for case in ROUND198_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round198_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_approval_clinical_paper_partner_peak_sales_or_mna_as_green_evidence",
            "do_not_invent_prices_stage_dates_prescriptions_reimbursement_revenue_royalty_utilization_margin_cash_runway_or_dilution",
            "do_not_confirm_hard_4c_without_reliable_primary_or_major_source",
        ],
    }


def render_round198_summary_markdown() -> str:
    summary = round198_summary()
    lines = [
        "# Round-198 R7 Loop-7 Price-Path Validation Summary",
        "",
        f"- source_round: `{ROUND198_SOURCE_ROUND_PATH}`",
        "- large_sector: `BIOTECH_HEALTHCARE_DEVICE`",
        "- scope: oncology royalty, botulinum launch, biosimilar/CDMO manufacturing, medical AI, and hard 4C source-gap validation",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- score_adjustment_count: {summary['score_adjustment_count']}",
        f"- price_backfill_field_count: {summary['price_backfill_field_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
        f"- stage4b_watch_count: {summary['stage4b_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- stage3_case_count: {summary['stage3_case_count']}",
        f"- stage4b_watch_or_elevated_count: {summary['stage4b_watch_or_elevated_count']}",
        f"- source_gap_case_count: {summary['source_gap_case_count']}",
        f"- needs_ohlc_backfill_count: {summary['needs_ohlc_backfill_count']}",
        "- production_scoring_changed: false",
        "- candidate_generation_input: false",
        "- shadow_weight_only: true",
        "- needs_ohlc_backfill: true",
        "- hard_4c_confirmed: false in this pass",
        "",
        "## Interpretation",
        "",
        "- R7은 승인, 임상, 논문, M&A보다 상업화 숫자를 늦게 확인해야 하는 섹터다.",
        "- 유한양행은 FDA 승인으로 Stage 2 후보지만 처방량, 로열티, EPS revision 전 Stage 3는 보류한다.",
        "- 휴젤은 미국 launch가 Stage 2지만 미국 매출, ASP, 채널 침투 전 Green 금지다.",
        "- 셀트리온 미국 공장 인수는 tariff hedge Stage 2지만 제품 이전, 가동률, margin, FCF 전에는 Green이 아니다.",
        "- SK바이오사이언스 IDT 인수는 CMO 전환 후보지만 발표 당일 급등은 event premium watch다.",
        "- 삼성바이오로직스는 CDMO structural benchmark지만 이번 시설 인수는 신규 Green보다 4B/saturation 감시에 가깝다.",
        "- 루닛은 외부검증이 있어도 reimbursement, hospital adoption, recurring revenue 전에는 Stage 3가 아니다.",
        "- 이번 pass에서는 신뢰할 수 있는 원문이 부족한 hard 4C를 억지로 확정하지 않는다.",
        "",
        "쉬운 예: `as_of_date=2024-08-20`에 FDA 승인이 나도 실제 처방량과 로열티가 없으면 Stage 3-Green이 아니라 강한 Stage 2다.",
    ]
    return "\n".join(lines) + "\n"


def render_round198_green_gate_review_markdown() -> str:
    lines = [
        "# Round-198 R7 Loop-7 Green Gate Review",
        "",
        "## Green Required Evidence",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND198_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Green Forbidden Patterns", ""])
    lines.extend(f"- `{field}`" for field in ROUND198_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "| --- | --- | ---: | --- |"])
    for adjustment in ROUND198_SCORE_ADJUSTMENTS:
        lines.append(f"| `{adjustment.axis}` | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these weights to production scoring yet.",
            "- Do not use Round198 cases as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds to force promotion.",
            "- Do not invent prescriptions, reimbursement, revenue, royalty, utilization, margin, cash runway, dilution, stage prices, or MFE/MAE.",
            "- Do not treat manufacturing-inspection CRL as the same as efficacy/safety CRL.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round198_price_backfill_plan_markdown() -> str:
    lines = [
        "# Round-198 R7 Loop-7 Price Backfill Plan",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND198_PRICE_BACKFILL_FIELDS)
    lines.extend(["", "## Priority Cases", "", "| case | stage marker | current status | 4B status | hard 4C |", "| --- | --- | --- | --- | --- |"])
    for case in ROUND198_CASE_CANDIDATES:
        stage_marker = case.stage3_date or case.stage2_date or case.stage4b_date or case.stage4c_date or case.stage1_date
        lines.append(
            f"| `{case.case_id}` | {_date_text(stage_marker) or 'undated'} | "
            f"{case.price_validation_status} | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} |"
        )
    lines.extend(
        [
            "",
            "## Backfill Rule",
            "",
            "- Use official OHLC data for exact MFE/MAE.",
            "- Keep unknown values null or `needs_ohlc_backfill`.",
            "- Split FDA approval, CRL, paper, M&A, launch, and commercial revenue dates.",
            "- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round198_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round-198 R7 Loop-7 Stage 4B / 4C Review",
        "",
        "## 4B Status Definitions",
        "",
        "- `watch`: approval, paper, M&A, partner peak-sales, or CDMO capacity premium runs ahead of commercialization.",
        "- `elevated`: launch slows, reimbursement is limited, capex exceeds contracts, competition rises, or cash burn continues.",
        "- `graduated`: revenue/royalty ramp misses consensus and positive news no longer moves the price path.",
        "",
        "## Hard 4C Gates",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND198_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## CRL Interpretation",
            "",
            "- efficacy/safety CRL can be hard 4C.",
            "- manufacturing-inspection CRL is commercialization delay watch when no additional trial is required.",
            "",
            "## Case Review",
            "",
            "| case | 4B status | hard 4C confirmed | interpretation |",
            "| --- | --- | --- | --- |",
        ]
    )
    for case in ROUND198_CASE_CANDIDATES:
        lines.append(
            f"| `{case.case_id}` | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    rows_tuple = tuple(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows_tuple[0].keys()), lineterminator="\n")
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow(dict(row))
    return path


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


__all__ = [
    "ROUND198_CASE_CANDIDATES",
    "ROUND198_DEFAULT_AUDIT_PATH",
    "ROUND198_DEFAULT_CASES_PATH",
    "ROUND198_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND198_GREEN_FORBIDDEN_PATTERNS",
    "ROUND198_GREEN_REQUIRED_FIELDS",
    "ROUND198_HARD_4C_GATES",
    "ROUND198_PRICE_BACKFILL_FIELDS",
    "ROUND198_REQUIRED_TARGET_ALIASES",
    "ROUND198_SCORE_ADJUSTMENTS",
    "ROUND198_SOURCE_ROUND_PATH",
    "ROUND198_STAGE4B_STATUSES",
    "Round198CaseCandidate",
    "Round198ScoreAdjustment",
    "render_round198_green_gate_review_markdown",
    "render_round198_price_backfill_plan_markdown",
    "render_round198_stage4b_4c_review_markdown",
    "render_round198_summary_markdown",
    "round198_audit_payload",
    "round198_case_records",
    "round198_case_rows",
    "round198_price_backfill_field_rows",
    "round198_score_adjustment_rows",
    "round198_summary",
    "round198_target_alias_rows",
    "write_round198_r7_loop7_reports",
]
