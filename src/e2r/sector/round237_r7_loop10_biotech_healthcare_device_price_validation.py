"""Round-237 R7 Loop-10 biotech/healthcare/device price validation pack.

Round 237 is calibration/evaluation material only. It converts
``docs/round/round_237.md`` into structured case records, shadow weights, and
guardrail reports.

Easy example: a medical AI paper with AUC 0.91 is useful Stage 2 evidence. It
is not Stage 3-Green until reimbursement, hospital adoption, recurring revenue,
margin, cash runway, and post-evidence price behavior are visible as of the
case date.
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


ROUND237_SOURCE_ROUND_PATH = "docs/round/round_237.md"
ROUND237_ANALYST_ROUND_ID = "round_165"
ROUND237_LARGE_SECTOR = Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE
ROUND237_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round237_r7_loop10_biotech_healthcare_device_price_validation"
ROUND237_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_loop10_round237.jsonl"
ROUND237_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round237_r7_loop10_biotech_healthcare_device_price_validation_audit.json"

ROUND237_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "MEDICAL_AESTHETIC_DEVICE_GLOBALIZATION": E2RArchetype.AESTHETIC_DEVICE_EXPORT_KOREA.value,
    "AESTHETIC_DEVICE_TAKE_PRIVATE": E2RArchetype.EVENT_PREMIUM.value,
    "BOTULINUM_US_MARKET_ENTRY": E2RArchetype.BOTULINUM_US_MARKET_ENTRY.value,
    "BIOPHARMA_CMO_M_AND_A": E2RArchetype.CDMO_HEALTHCARE_CONTRACT.value,
    "BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING": E2RArchetype.BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING.value,
    "CDMO_US_TARIFF_HEDGE_CAPACITY": E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY.value,
    "AUTOIMMUNE_PARTNER_TRIAL_FAILURE": E2RArchetype.THESIS_BREAK_4C_WATCH.value,
    "MEDICAL_AI_EXTERNAL_VALIDATION": E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION.value,
    "MEDICAL_AI_COMMERCIALIZATION_GATE": E2RArchetype.DIGITAL_HEALTHCARE_AI.value,
    "APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN": E2RArchetype.APPROVAL_ONLY_NOT_COMMERCIALIZATION.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
    "EVIDENCE_GOOD_BUT_PRICE_FAILED": E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED.value,
}

ROUND237_DEEP_SUB_ARCHETYPES: tuple[str, ...] = (
    "Jeisys Medical",
    "Classys peer read-through",
    "energy-based devices",
    "anti-aging aesthetic healthcare",
    "take-private premium vs listed rerating",
    "Hugel Letybo",
    "FDA-approved neuromodulator",
    "U.S. launch channel penetration",
    "price discount vs Botox",
    "SK Bioscience IDT Biologika",
    "Celltrion ImClone Systems",
    "Samsung Biologics GSK Rockville facility",
    "U.S. manufacturing tariff hedge",
    "facility acquisition vs utilization",
    "HanAll Biopharma Immunovant batoclimab",
    "partner trial failure",
    "Lunit INSIGHT DBT",
    "external validation AUC",
    "subgroup weakness",
    "reimbursement and hospital adoption gate",
)

ROUND237_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "approval_clearance_or_launch_confirmed",
    "commercial_launch_after_approval",
    "commercial_revenue_or_royalty_recognition",
    "prescription_procedure_volume_or_hospital_adoption",
    "reimbursement_payer_access_or_asp_confirmed",
    "capacity_utilization_or_channel_penetration",
    "gross_margin_or_fcf_visibility",
    "repeat_treatment_consumables_or_contract_backlog",
    "cash_runway_and_dilution_risk_passed",
    "partner_execution_risk_passed",
    "price_path_after_evidence",
)

ROUND237_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "approval_news_only",
    "clinical_headline_only",
    "external_validation_without_revenue",
    "mna_without_utilization",
    "take_private_premium_only",
    "fda_approval_without_commercial_sales",
    "partner_pipeline_without_indication_success",
    "pre_revenue_medical_ai_story",
    "cash_burn_or_dilution_risk",
    "subgroup_performance_risk",
    "facility_acquisition_without_product_transfer",
    "us_launch_without_channel_sales",
)

ROUND237_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "fda_approval_price_spike_before_sales",
    "us_launch_before_us_sales",
    "mna_announcement_day_spike",
    "take_private_premium_peer_readthrough",
    "medical_ai_validation_price_spike_before_reimbursement",
    "cdmo_capacity_premium_before_utilization",
    "valuation_moves_before_commercial_revenue",
)

ROUND237_HARD_4C_GATES: tuple[str, ...] = (
    "fda_crl_or_approval_rejection",
    "efficacy_or_safety_trial_failure",
    "partner_trial_failure",
    "commercialization_failure",
    "prescription_or_procedure_volume_underperformance",
    "reimbursement_failure",
    "royalty_non_recognition",
    "large_dilution",
    "cash_runway_break",
    "manufacturing_inspection_failure",
    "product_safety_issue",
    "subgroup_clinical_performance_failure",
    "partner_launch_failure",
    "patent_ip_legal_loss",
)

ROUND237_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "relative_underperformance_pp",
    "transaction_value_or_facility_capacity",
    "launch_price_or_discount",
    "trial_size_or_exam_count",
    "approval_launch_validation_date",
    "commercialization_gate_status",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round237ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round237ShadowWeightRow:
    archetype: E2RArchetype
    commercial_revenue: int
    procedure_or_prescription_volume: int
    channel_penetration: int
    reimbursement: int
    capacity_utilization: int
    gross_margin: int
    cash_runway: int
    event_penalty: int
    clinical_partner_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "commercial_revenue": _signed(self.commercial_revenue),
            "procedure_or_prescription_volume": _signed(self.procedure_or_prescription_volume),
            "channel_penetration": _signed(self.channel_penetration),
            "reimbursement": _signed(self.reimbursement),
            "capacity_utilization": _signed(self.capacity_utilization),
            "gross_margin": _signed(self.gross_margin),
            "cash_runway": _signed(self.cash_runway),
            "event_penalty": _signed(self.event_penalty),
            "clinical_partner_redteam": _signed(self.clinical_partner_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round237CaseCandidate:
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
    extra_price_metrics: Mapping[str, float | str | bool | None]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND237_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND237_SCORE_ADJUSTMENTS: tuple[Round237ScoreAdjustment, ...] = (
    Round237ScoreAdjustment("commercial_revenue", 5, "raise", "승인·출시 이후 실제 매출이 보여야 R7 Stage 3 후보가 된다."),
    Round237ScoreAdjustment("prescription_or_procedure_volume", 5, "raise", "처방량·시술량은 제품이 실제 사용으로 바뀌는 증거다."),
    Round237ScoreAdjustment("channel_penetration", 5, "raise", "미국 launch나 미용기기는 병의원 채널 침투가 핵심이다."),
    Round237ScoreAdjustment("reimbursement_access", 5, "raise", "보험·수가 접근이 없으면 의료 제품 매출 지속성이 약하다."),
    Round237ScoreAdjustment("capacity_utilization", 5, "raise", "CDMO/CMO는 공장 보유보다 가동률과 제품 이전이 핵심이다."),
    Round237ScoreAdjustment("contract_backlog", 4, "raise", "CMO/CDMO는 고객 계약과 backlog가 Stage 3 visibility를 만든다."),
    Round237ScoreAdjustment("gross_margin_visibility", 4, "raise", "매출이 있어도 gross margin이 확인돼야 EPS/FCF 체급 변화로 이어진다."),
    Round237ScoreAdjustment("cash_runway", 4, "raise", "상업화 전 현금 runway가 부족하면 희석 리스크가 먼저다."),
    Round237ScoreAdjustment("repeat_treatment_or_consumables", 4, "raise", "미용기기와 보툴리눔은 반복 시술·소모품 구조가 visibility를 만든다."),
    Round237ScoreAdjustment("hospital_adoption", 4, "raise", "의료AI는 논문보다 병원 도입과 반복 사용이 중요하다."),
    Round237ScoreAdjustment("approval_news_only", -5, "lower", "승인 뉴스만으로는 Stage 3-Green을 만들 수 없다."),
    Round237ScoreAdjustment("clinical_headline_only", -5, "lower", "임상 헤드라인은 처방·매출·로열티 전까지 Stage 2 watch다."),
    Round237ScoreAdjustment("external_validation_without_revenue", -4, "lower", "논문 성능은 좋지만 수가·도입·반복매출 없이는 Green 금지다."),
    Round237ScoreAdjustment("mna_without_utilization", -5, "lower", "M&A 발표만 있고 가동률·마진이 없으면 event premium이다."),
    Round237ScoreAdjustment("take_private_premium_only", -4, "lower", "take-private valuation은 peer Green 조건이 아니라 Stage 2 이벤트다."),
    Round237ScoreAdjustment("fda_approval_without_commercial_sales", -4, "lower", "FDA approval 이후 상업 매출이 없으면 Stage 3 보류다."),
    Round237ScoreAdjustment("partner_pipeline_without_indication_success", -4, "lower", "파트너 pipeline 기대는 indication별 성공 전까지 제한한다."),
    Round237ScoreAdjustment("pre_revenue_medical_ai_story", -5, "lower", "pre-revenue 의료AI는 수가와 병원 도입 전 Green 금지다."),
    Round237ScoreAdjustment("cash_burn_or_dilution_risk", -5, "lower", "대규모 희석이나 cash runway 붕괴는 Green hard blocker다."),
    Round237ScoreAdjustment("subgroup_performance_risk", -3, "lower", "의료AI subgroup 성능 약점은 실제 도입 리스크다."),
)


ROUND237_SHADOW_WEIGHT_ROWS: tuple[Round237ShadowWeightRow, ...] = (
    Round237ShadowWeightRow(E2RArchetype.AESTHETIC_DEVICE_EXPORT_KOREA, 5, 5, 5, 1, 3, 5, 4, -3, 2, 4, 3, "Jeisys take-private validates demand, but listed Green requires recurring sales/consumables/margin/FCF."),
    Round237ShadowWeightRow(E2RArchetype.BOTULINUM_US_MARKET_ENTRY, 5, 5, 5, 3, 0, 5, 4, -3, 3, 4, 4, "Hugel Letybo U.S. launch needs sales/channel/ASP/repeat treatment before Green."),
    Round237ShadowWeightRow(E2RArchetype.CDMO_HEALTHCARE_CONTRACT, 4, 0, 0, 0, 5, 5, 4, -5, 2, 5, 4, "SK Bioscience IDT M&A is Stage 2 until utilization/backlog/margin/FCF confirm."),
    Round237ShadowWeightRow(E2RArchetype.BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING, 4, 0, 0, 1, 5, 5, 4, -3, 2, 4, 4, "Celltrion U.S. facility is tariff hedge Stage 2, not Green before transfer/utilization/FCF."),
    Round237ShadowWeightRow(E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY, 4, 0, 0, 0, 5, 5, 4, -4, 2, 4, 4, "Samsung Biologics U.S. facility had weak price reaction; watch valuation saturation."),
    Round237ShadowWeightRow(E2RArchetype.THESIS_BREAK_4C_WATCH, 0, 0, 0, 0, 0, 0, 5, 0, 5, 3, 5, "HanAll/Immunovant trial failure is 4C-watch for partner-pipeline value."),
    Round237ShadowWeightRow(E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION, 2, 0, 0, 5, 0, 3, 5, -4, 3, 5, 5, "Lunit external validation is not Green without reimbursement/adoption/revenue."),
    Round237ShadowWeightRow(E2RArchetype.APPROVAL_ONLY_NOT_COMMERCIALIZATION, 0, 0, 0, 0, 0, 0, 4, -5, 3, 5, 4, "Approval or validation headlines should remain Stage 2 until commercial conversion."),
)


ROUND237_CASE_CANDIDATES: tuple[Round237CaseCandidate, ...] = (
    Round237CaseCandidate(
        case_id="r7_loop10_jeisys_aesthetic_device_take_private",
        symbol="287410",
        company_name="Jeisys Medical",
        primary_archetype=E2RArchetype.AESTHETIC_DEVICE_EXPORT_KOREA,
        secondary_archetypes=(E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_event_premium",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 9, 11),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="take_private_event_is_stage2_until_recurring_device_sales_consumables_margin_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("archimed_take_private", "deal_value_742m_usd", "reported_close_price_12860_krw", "fy2023_revenue_107m_usd", "fy2023_adjusted_pretax_31m_usd", "revenue_cagr_44pct", "pretax_earnings_cagr_45pct"),
        red_flag_fields=("take_private_premium_only", "listed_peer_green_unverified", "consumable_attach_rate_unverified", "margin_fcf_unverified"),
        price_data_source="WSJ reported acquisition, price, and financial anchors",
        reported_price_anchor="12,860 KRW close around the report",
        reported_return_anchor="Deal value about $742M; FY2023 revenue $107M; adjusted pretax earnings $31M",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=12860.0,
        stage3_price_anchor=None,
        extra_price_metrics={"deal_value_usd_mn": 742.0, "fy2023_revenue_usd_mn": 107.0, "fy2023_adjusted_pretax_earnings_usd_mn": 31.0, "adjusted_pretax_margin_pct": 29.0, "revenue_cagr_3y_pct": 44.0, "adjusted_pretax_earnings_cagr_3y_pct": 45.0},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Take-private validates aesthetic-device demand but is Stage 2; recurring sales, consumables, margin and FCF are required for Green.",
    ),
    Round237CaseCandidate(
        case_id="r7_loop10_hugel_letybo_us_launch",
        symbol="145020",
        company_name="휴젤",
        primary_archetype=E2RArchetype.BOTULINUM_US_MARKET_ENTRY,
        secondary_archetypes=(E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT, E2RArchetype.BOTULINUM_AESTHETIC_REGULATED),
        case_type="success_candidate",
        round_case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 3, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="us_launch_is_stage2_until_us_sales_channel_penetration_asp_repeat_treatment_and_opm_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("letybo_fda_approval", "letybo_us_launch", "glabellar_lines_indication", "letybo_unit_price_9_12_usd", "botox_unit_price_12_18_usd", "potential_discount_25_33pct"),
        red_flag_fields=("us_sales_unverified", "channel_penetration_unverified", "asp_opm_unverified", "price_war_watch", "safety_or_channel_rollout_risk"),
        price_data_source="Allure/New York Post product launch and price anchors",
        reported_price_anchor="Hugel Korea OHLC unavailable after deep search",
        reported_return_anchor="Letybo estimated $9-12/unit vs Botox $12-18/unit; potential 25-33.3% discount",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"letybo_unit_price_low_usd": 9.0, "letybo_unit_price_high_usd": 12.0, "botox_unit_price_low_usd": 12.0, "botox_unit_price_high_usd": 18.0, "low_end_discount_pct": -25.0, "high_end_discount_pct": -33.3, "fda_approval_status": "approved_neuromodulator_for_glabellar_lines"},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="U.S. launch is Stage 2; U.S. sales, channel penetration, ASP, repeat treatment and OPM are required before Green.",
    ),
    Round237CaseCandidate(
        case_id="r7_loop10_sk_bioscience_idt_cmo_mna",
        symbol="302440",
        company_name="SK바이오사이언스",
        primary_archetype=E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        secondary_archetypes=(E2RArchetype.VACCINE_CMO_RESTRUCTURING, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="success_candidate_event_premium",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=date(2024, 6, 27),
        stage4c_date=None,
        stage3_decision="idt_acquisition_is_stage2_event_premium_until_utilization_backlog_margin_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("idt_biologika_60pct_acquisition", "deal_value_339bn_krw", "deal_value_243_75m_usd", "first_major_mna_since_2021_ipo", "event_morning_return_11_7pct"),
        red_flag_fields=("mna_without_utilization", "integration_cost_unverified", "backlog_unverified", "cash_burn_or_goodwill_impairment_watch"),
        price_data_source="Reuters acquisition and event-return anchors",
        reported_price_anchor="SK Bioscience Korea full OHLC unavailable after deep search",
        reported_return_anchor="Shares +11.7% in morning trade after IDT Biologika acquisition announcement",
        mfe_1d=11.7,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"deal_value_krw_bn": 339.0, "deal_value_usd_mn": 243.75, "stake_acquired_pct": 60.0, "implied_idt_equity_value_krw_bn": 565.0, "remaining_klocke_stake_pct": 40.0, "sk_bioscience_2021_ipo_proceeds_usd_bn": 1.33, "deal_value_vs_ipo_proceeds_pct": 18.3, "event_mfe_morning_pct": 11.7},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="IDT acquisition is Stage 2/event premium; utilization, backlog, margin and FCF are required before Green.",
    ),
    Round237CaseCandidate(
        case_id="r7_loop10_celltrion_us_manufacturing_tariff_hedge",
        symbol="068270",
        company_name="셀트리온",
        primary_archetype=E2RArchetype.BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING,
        secondary_archetypes=(E2RArchetype.BIOSIMILAR_COMMERCIALIZATION, E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY),
        case_type="success_candidate",
        round_case_type="success_candidate",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 9, 23),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="us_factory_tariff_hedge_is_stage2_until_product_transfer_quality_readiness_utilization_margin_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("imclone_acquisition_330m_usd", "us_manufacturing_base_secured", "tariff_hedge_supply_chain_resilience", "us_factory_expansion_up_to_700bn_krw"),
        red_flag_fields=("product_transfer_unverified", "fda_quality_readiness_unverified", "utilization_unverified", "gross_margin_fcf_unverified", "biosimilar_pricing_pressure"),
        price_data_source="Reuters transaction and investment anchors",
        reported_price_anchor="Celltrion Korea OHLC unavailable after deep search",
        reported_return_anchor="ImClone acquisition $330M; expansion up to 700B KRW / $478.17M",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"imclone_acquisition_usd_mn": 330.0, "expansion_investment_krw_bn": 700.0, "expansion_investment_usd_mn": 478.17, "imclone_acquisition_krw_bn_at_1463_9": 483.1, "combined_acquisition_plus_expansion_krw_trn": 1.183},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="U.S. facility is Stage 2 tariff hedge evidence; product transfer, quality readiness, utilization, margin and FCF decide promotion.",
    ),
    Round237CaseCandidate(
        case_id="r7_loop10_samsung_biologics_gsk_facility_price_failed",
        symbol="207940",
        company_name="삼성바이오로직스",
        primary_archetype=E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY,
        secondary_archetypes=(E2RArchetype.CDMO_HEALTHCARE_CONTRACT, E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED),
        case_type="success_candidate",
        round_case_type="evidence_good_but_price_failed",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 12, 22),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="good_us_cdmo_facility_news_failed_price_confirmation_and_needs_utilization_contract_transfer_margin_and_fcf",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("gsk_rockville_facility_acquisition", "deal_value_280m_usd", "drug_substance_capacity_60000l", "first_us_drug_production_facility", "expected_close_end_q1_2026"),
        red_flag_fields=("weak_price_reaction", "valuation_saturation_watch", "contract_transfer_unverified", "utilization_unverified", "tariff_benefit_reversal_watch"),
        price_data_source="Reuters reported event return and facility capacity anchor",
        reported_price_anchor="Samsung Biologics -0.4% while KOSPI +2.0%",
        reported_return_anchor="relative underperformance -2.4pp on GSK facility acquisition event",
        mfe_1d=None,
        mae_1d=-0.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"stage2_event_mae_1d_pct": -0.4, "kospi_same_day_return_pct": 2.0, "relative_underperformance_pp": -2.4, "deal_value_usd_mn": 280.0, "facility_capacity_liters": 60000.0, "expected_close": "around_end_q1_2026"},
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Good U.S. CDMO capacity event but immediate price reaction failed; utilization/contract transfer is needed for a fresh Stage 3 path.",
    ),
    Round237CaseCandidate(
        case_id="r7_loop10_hanall_immunovant_batoclimab_ted_failure",
        symbol="009420",
        company_name="한올바이오파마 / Immunovant",
        primary_archetype=E2RArchetype.THESIS_BREAK_4C_WATCH,
        secondary_archetypes=(E2RArchetype.BIOTECH_PRE_REVENUE_REGULATORY,),
        case_type="failed_rerating",
        round_case_type="4C-watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 4, 2),
        stage3_decision="partner_pipeline_expectation_is_not_green_and_ted_trial_failure_creates_4c_watch",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("fcrn_autoimmune_pipeline", "immunovant_roivant_partner_value", "batoclimab_ted_trials"),
        red_flag_fields=("partner_trial_failure", "two_late_stage_ted_trials_failed", "primary_endpoint_not_met", "immunovant_event_mae_4_8pct", "hanall_stock_ohlc_unavailable", "hard_4c_not_confirmed_for_entire_pipeline"),
        price_data_source="Reuters partner trial-failure anchor",
        reported_price_anchor="Immunovant event price $23.89; HanAll stock OHLC unavailable",
        reported_return_anchor="Immunovant -4.8% after batoclimab failed two late-stage thyroid eye disease trials",
        mfe_1d=None,
        mae_1d=-4.8,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"partner": "Immunovant/Roivant", "trial": "two_late_stage_thyroid_eye_disease_trials", "primary_endpoint": "at_least_2mm_reduction_in_eye_bulging_after_24_weeks", "result": "failed_to_meet_primary_goal", "immunovant_event_mae_pct": -4.8, "immunovant_event_price_usd": 23.89, "hard_4c_confirmed": False},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="hanall_stock_price_data_unavailable_after_deep_search",
        notes="Partner trial failure is 4C-watch; hard 4C requires broader pipeline or cashflow impairment confirmation.",
    ),
    Round237CaseCandidate(
        case_id="r7_loop10_lunit_medical_ai_external_validation",
        symbol="328130",
        company_name="루닛",
        primary_archetype=E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION,
        secondary_archetypes=(E2RArchetype.DIGITAL_HEALTHCARE_AI, E2RArchetype.MEDICAL_AI_SUBGROUP_GENERALIZATION_RISK, E2RArchetype.APPROVAL_ONLY_NOT_COMMERCIALIZATION),
        case_type="failed_rerating",
        round_case_type="insufficient_evidence",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2025, 3, 17),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="external_validation_is_stage2_not_green_without_reimbursement_hospital_adoption_recurring_revenue_margin_and_cash_runway",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("lunit_insight_dbt_external_validation", "screening_mammography_exams_163449", "screen_detected_cancers_1368", "overall_auc_0_91", "commercial_model_validation"),
        red_flag_fields=("reimbursement_unverified", "hospital_adoption_unverified", "recurring_revenue_unverified", "cash_runway_unverified", "subgroup_performance_risk", "non_invasive_cancer_auc_0_85", "calcification_auc_0_80"),
        price_data_source="arXiv external validation evidence",
        reported_price_anchor="Lunit Korea OHLC unavailable after deep search",
        reported_return_anchor="AUC 0.91 overall; precision 0.08; weaker subgroup AUCs require commercialization gate",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"exam_count": 163449.0, "positive_cases": 1368.0, "negative_exams": 162081.0, "overall_auc": 0.91, "precision": 0.08, "recall": 0.73, "non_invasive_cancer_auc": 0.85, "calcification_auc": 0.80, "dense_breast_auc": 0.90},
        score_price_alignment="unknown",
        rerating_result="no_rerating",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="External validation is Stage 2 evidence; reimbursement, hospital adoption, recurring revenue, gross margin and cash runway are required before Green.",
    ),
)


def round237_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND237_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round237 R7 Loop-10 biotech/healthcare/device price-path "
                "validation case. Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "approval" in field or "launch" in field or "validation" in field or "pipeline" in field or "demand" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "revenue" in field
                or "earnings" in field
                or "sales" in field
                or "commercial" in field
                or "margin" in field
                or "capacity" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "event" in field or "mna" in field or "premium" in field or "price" in field or "valuation" in field or "weak_price" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "failure" in field
                or "failed" in field
                or "safety" in field
                or "cash" in field
                or "dilution" in field
                or "subgroup" in field
                or "partner" in field
                or "reimbursement" in field
                or "inspection" in field
            ),
            must_have_fields=ROUND237_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND237_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "hard_4c_confirmed_false",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_approval_clinical_paper_mna_takeprivate_or_medical_ai_validation_as_green_alone",
                f"round_case_type={candidate.round_case_type}",
                *ROUND237_GREEN_REQUIRED_FIELDS,
                *ROUND237_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=candidate.stage2_price_anchor is not None or candidate.mfe_1d is not None or candidate.mae_1d is not None,
                stage_dates_confidence=0.82 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round237_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND237_CASE_CANDIDATES:
        rows.append(
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
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
                "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
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


def round237_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND237_SCORE_ADJUSTMENTS)


def round237_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND237_SHADOW_WEIGHT_ROWS)


def round237_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round237_price_validation": "true"} for field in ROUND237_PRICE_VALIDATION_FIELDS)


def round237_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round237_label": label, "canonical_archetype": canonical} for label, canonical in ROUND237_REQUIRED_TARGET_ALIASES.items())


def round237_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple({"deep_sub_archetype": item, "large_sector": ROUND237_LARGE_SECTOR.value} for item in ROUND237_DEEP_SUB_ARCHETYPES)


def round237_summary() -> dict[str, int | bool | str]:
    cases = ROUND237_CASE_CANDIDATES
    return {
        "source_round": ROUND237_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND237_ANALYST_ROUND_ID,
        "large_sector": ROUND237_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "target_archetype_count": len(ROUND237_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND237_DEEP_SUB_ARCHETYPES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": False,
    }


def round237_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND237_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND237_ANALYST_ROUND_ID,
        "large_sector": ROUND237_LARGE_SECTOR.value,
        "summary": round237_summary(),
        "target_aliases": dict(ROUND237_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetypes": list(ROUND237_DEEP_SUB_ARCHETYPES),
        "green_required_fields": list(ROUND237_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND237_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND237_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND237_HARD_4C_GATES),
        "case_ids": [case.case_id for case in ROUND237_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_use_round237_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_approval_clinical_paper_mna_takeprivate_or_medical_ai_validation_as_green",
            "do_not_confirm_hard_4c_without_company_level_impairment",
            "do_not_invent_ohlc_stage_prices_or_business_metrics",
        ],
    }


def render_round237_summary_markdown() -> str:
    summary = round237_summary()
    lines = [
        "# Round 237 R7 Loop 10 Biotech Healthcare Device Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- analyst_round_id: {summary['analyst_round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- evidence_good_but_price_failed: {summary['evidence_good_but_price_failed_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round type | stage2 | stage3 | 4B | 4C-watch | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND237_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.case_type,
                    case.round_case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    case.score_price_alignment,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Jeisys validates aesthetic device demand through take-private valuation, but that is Stage 2/event premium for listed peers.",
            "- Hugel Letybo U.S. launch is Stage 2 until U.S. sales, channel penetration, ASP, repeat treatment, and OPM confirm.",
            "- SK Bioscience and Celltrion facility/M&A events need utilization, backlog, product transfer, margin, and FCF before Green.",
            "- Samsung Biologics has good U.S. CDMO evidence but immediate price confirmation failed, so it remains evidence_good_but_price_failed.",
            "- HanAll/Immunovant is 4C-watch because partner trial failure matters, but hard 4C is not forced without broader impairment.",
            "- Lunit external validation is Stage 2 evidence; reimbursement, hospital adoption, recurring revenue, and cash runway decide promotion.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round237_green_gate_review_markdown() -> str:
    lines = [
        "# Round 237 R7 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND237_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND237_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND237_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `FDA approval` means Stage 2 attention. It is not Green until sales, reimbursement, margin, and cash runway follow.",
            "- `M&A announcement + same-day price spike` is 4B/event premium until utilization, backlog, margin, and FCF exist.",
            "- `AUC 0.91 medical AI validation` is useful evidence, but reimbursement and hospital adoption are the Green gate.",
            "- `Partner trial failure` is RedTeam evidence even when the Korean stock OHLC is missing.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round237_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 237 R7 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND237_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND237_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | 4C-watch date | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND237_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.stage4b_status} | {_date_text(case.stage4c_date)} | "
            f"{str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round237_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 237 R7 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: false",
        "- Do not invent OHLC, peak, MFE, MAE, stage prices, prescription volume, utilization, margin, FCF, or royalty values.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND237_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND237_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def render_round237_deep_sub_archetypes_markdown() -> str:
    lines = [
        "# Round 237 R7 Deep Sub-Archetypes",
        "",
        "These labels describe research coverage. They are not production scoring inputs.",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND237_DEEP_SUB_ARCHETYPES)
    return "\n".join(lines) + "\n"


def write_round237_r7_loop10_reports(
    output_directory: str | Path = ROUND237_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND237_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND237_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round237_case_records(), cases_path),
        "audit": _write_json(round237_audit_payload(), audit_path),
        "summary": output / "round237_r7_loop10_price_validation_summary.md",
        "case_matrix": output / "round237_r7_loop10_case_matrix.csv",
        "target_aliases": output / "round237_r7_loop10_target_aliases.csv",
        "deep_sub_archetypes": output / "round237_r7_loop10_deep_sub_archetypes.csv",
        "score_adjustments": output / "round237_r7_loop10_score_adjustments.csv",
        "shadow_weights": output / "round237_r7_loop10_shadow_weights.csv",
        "price_validation_fields": output / "round237_r7_loop10_price_validation_fields.csv",
        "green_gate_review": output / "round237_r7_loop10_green_gate_review.md",
        "price_validation_plan": output / "round237_r7_loop10_price_validation_plan.md",
        "stage4b_4c_review": output / "round237_r7_loop10_stage4b_4c_review.md",
        "deep_sub_archetype_review": output / "round237_r7_loop10_deep_sub_archetypes.md",
    }
    paths["summary"].write_text(render_round237_summary_markdown(), encoding="utf-8")
    _write_csv(round237_case_rows(), paths["case_matrix"])
    _write_csv(round237_target_alias_rows(), paths["target_aliases"])
    _write_csv(round237_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round237_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round237_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round237_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round237_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round237_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round237_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["deep_sub_archetype_review"].write_text(render_round237_deep_sub_archetypes_markdown(), encoding="utf-8")
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
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _float_text(value: float | None) -> str:
    return "" if value is None else f"{value:g}"


def _signed(value: int) -> str:
    return f"{value:+d}"
