"""Round-250 R7 Loop-11 biotech/healthcare/device price validation pack.

This pack converts ``docs/round/round_250.md`` into calibration-only case
records and guardrail reports. Production scoring is not changed.

Easy example: FDA approval is a strong Stage 2 signal. It is not Stage 3-Green
until prescriptions, reimbursement, royalty or commercial revenue, margin, FCF,
and post-evidence price behavior are visible.
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


ROUND250_SOURCE_ROUND_PATH = "docs/round/round_250.md"
ROUND250_ANALYST_ROUND_ID = "round_178"
ROUND250_LARGE_SECTOR = Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE.value
ROUND250_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round250_r7_loop11_biotech_healthcare_device_price_validation"
ROUND250_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_loop11_round250.jsonl"
ROUND250_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round250_r7_loop11_biotech_healthcare_device_price_validation_audit.json"

ROUND250_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BIO_PLATFORM_ROYALTY_CONVERSION": E2RArchetype.BIO_PLATFORM_ROYALTY_CONVERSION.value,
    "KOREAN_NEW_DRUG_GLOBAL_APPROVAL": E2RArchetype.KOREAN_NEW_DRUG_GLOBAL_APPROVAL.value,
    "CDMO_US_TARIFF_HEDGE_CAPACITY": E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY.value,
    "CMO_M_AND_A_TRANSITION": E2RArchetype.CMO_M_AND_A_TRANSITION.value,
    "BIOPHARMA_POLICY_TARIFF_RELIEF": E2RArchetype.BIOPHARMA_POLICY_TARIFF_RELIEF.value,
    "AUTOIMMUNE_PARTNER_TRIAL_FAILURE": E2RArchetype.AUTOIMMUNE_PARTNER_TRIAL_FAILURE.value,
    "MEDICAL_AI_EXTERNAL_VALIDATION": E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION.value,
    "APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN": E2RArchetype.APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
    "EVIDENCE_GOOD_BUT_PRICE_FAILED": E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED.value,
}

ROUND250_DEEP_SUB_ARCHETYPES: tuple[str, ...] = (
    "Alteogen hyaluronidase enzyme platform",
    "Merck Keytruda SC 30-40pct adoption target",
    "Halozyme patent challenge watch",
    "Yuhan lazertinib global approval",
    "J&J Rybrevant plus Lazcluze launch revenue gate",
    "Samsung Biologics GSK Rockville facility",
    "Celltrion ImClone U.S. manufacturing tariff hedge",
    "SK Bioscience IDT Biologika CMO transition",
    "HanAll Immunovant batoclimab partner trial failure",
    "Lunit INSIGHT DBT external validation",
    "medical AI reimbursement and hospital adoption gate",
    "biopharma tariff-policy relief basket",
)

ROUND250_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "approval_clearance_or_launch_confirmed",
    "commercial_launch_after_approval",
    "commercial_revenue_or_royalty_recognition",
    "prescription_volume_or_procedure_volume",
    "reimbursement_payer_or_asp_confirmed",
    "hospital_adoption_or_channel_penetration",
    "royalty_milestone_or_supply_revenue_confirmed",
    "gross_margin_or_royalty_margin_confirmed",
    "capacity_utilization_or_contract_backlog",
    "cash_runway_and_dilution_risk_passed",
    "partner_execution_risk_passed",
    "price_path_after_evidence",
)

ROUND250_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "fda_approval_only",
    "clinical_headline_only",
    "external_validation_without_revenue",
    "policy_support_without_order",
    "mna_without_utilization",
    "facility_acquisition_without_backlog",
    "partner_pipeline_without_indication_success",
    "royalty_unconfirmed_platform_story",
    "medical_ai_auc_without_reimbursement",
    "patent_litigation_risk_unresolved",
    "cash_burn_or_dilution_risk",
)

ROUND250_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "fda_approval_price_spike_before_sales",
    "big_pharma_partner_name_valuation_spike",
    "royalty_before_recognition_platform_rerating",
    "mna_announcement_before_utilization",
    "policy_support_day_sector_rally",
    "medical_ai_external_validation_price_spike",
    "cdmo_capacity_premium_before_utilization",
    "launch_started_but_prescription_slow",
    "patent_or_litigation_risk_after_rerating",
)

ROUND250_HARD_4C_GATES: tuple[str, ...] = (
    "fda_crl_or_approval_rejection",
    "efficacy_or_safety_trial_failure",
    "partner_trial_failure",
    "commercial_launch_failure",
    "royalty_non_recognition",
    "prescription_volume_failure",
    "reimbursement_failure",
    "manufacturing_inspection_failure",
    "product_safety_issue",
    "subgroup_clinical_performance_failure",
    "capacity_utilization_failure",
    "large_dilution_or_cash_runway_break",
)

ROUND250_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_event_return",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "relative_underperformance_pp",
    "sales_base_or_peak_sales_expectation",
    "adoption_or_exam_count",
    "transaction_value_or_capacity",
    "trial_or_crl_status",
    "commercialization_gate_status",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round250ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round250ShadowWeightRow:
    archetype: E2RArchetype
    commercial_revenue: int
    royalty_visibility: int
    prescription_volume: int
    reimbursement: int
    hospital_adoption: int
    utilization: int
    gross_margin: int
    cash_runway: int
    partner_execution: int
    event_penalty: int
    clinical_regulatory_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "commercial_revenue": _signed(self.commercial_revenue),
            "royalty_visibility": _signed(self.royalty_visibility),
            "prescription_volume": _signed(self.prescription_volume),
            "reimbursement": _signed(self.reimbursement),
            "hospital_adoption": _signed(self.hospital_adoption),
            "utilization": _signed(self.utilization),
            "gross_margin": _signed(self.gross_margin),
            "cash_runway": _signed(self.cash_runway),
            "partner_execution": _signed(self.partner_execution),
            "event_penalty": _signed(self.event_penalty),
            "clinical_regulatory_redteam": _signed(self.clinical_regulatory_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round250CaseCandidate:
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
    def expected_group(self) -> str:
        return self.case_type


ROUND250_SCORE_ADJUSTMENTS: tuple[Round250ScoreAdjustment, ...] = (
    Round250ScoreAdjustment("commercial_revenue", 5, "raise", "승인 뒤 실제 매출이 들어와야 R7 Stage 3 후보가 된다."),
    Round250ScoreAdjustment("royalty_revenue_visibility", 5, "raise", "플랫폼 바이오는 royalty/supply revenue가 확인되어야 현금흐름 전환이다."),
    Round250ScoreAdjustment("prescription_volume", 5, "raise", "신약은 처방량이 approval headline을 상업 성과로 바꾸는 증거다."),
    Round250ScoreAdjustment("reimbursement_access", 5, "raise", "보험·수가 접근 없이는 병원 도입과 반복 매출 지속성이 약하다."),
    Round250ScoreAdjustment("hospital_adoption", 4, "raise", "의료AI와 의료기기는 병원 도입 전까지 validation-only다."),
    Round250ScoreAdjustment("capacity_utilization", 5, "raise", "CDMO 공장·M&A는 가동률과 backlog가 있어야 이익으로 바뀐다."),
    Round250ScoreAdjustment("contract_backlog", 4, "raise", "CMO/CDMO는 계약 잔고가 시설 증설을 Stage 3 근거로 만든다."),
    Round250ScoreAdjustment("gross_margin_visibility", 4, "raise", "의료 제품은 매출만큼 gross margin과 FCF 확인이 중요하다."),
    Round250ScoreAdjustment("cash_runway", 4, "raise", "바이오 섹터는 cash runway와 dilution risk 통과가 필수다."),
    Round250ScoreAdjustment("partner_execution_quality", 5, "raise", "대형 파트너도 임상·제조·출시 실행이 깨지면 RedTeam 근거다."),
    Round250ScoreAdjustment("approval_news_only", -5, "lower", "FDA 승인만으로 Stage 3-Green을 만들지 않는다."),
    Round250ScoreAdjustment("clinical_headline_only", -5, "lower", "임상 headline은 revenue conversion 전 Stage 2에 그친다."),
    Round250ScoreAdjustment("external_validation_without_revenue", -5, "lower", "AUC나 외부검증은 수가·도입·반복매출 전 Green 근거가 아니다."),
    Round250ScoreAdjustment("mna_without_utilization", -5, "lower", "M&A 발표는 가동률·margin·FCF 전 event premium이다."),
    Round250ScoreAdjustment("policy_support_without_order", -4, "lower", "정책지원은 회사별 주문·마진·FCF로 닫히기 전 Green이 아니다."),
    Round250ScoreAdjustment("facility_acquisition_without_backlog", -4, "lower", "미국 공장 인수는 product transfer/backlog 전 Stage 2다."),
    Round250ScoreAdjustment("partner_program_without_indication_success", -5, "lower", "파트너 pipeline 기대는 indication별 성공 전 Green 금지다."),
    Round250ScoreAdjustment("patent_litigation_risk", -4, "lower", "특허분쟁은 royalty durability를 깎는 RedTeam 축이다."),
    Round250ScoreAdjustment("cash_burn_or_dilution_risk", -5, "lower", "상업화 전 현금소진/희석 위험은 Green을 막는다."),
    Round250ScoreAdjustment("subgroup_performance_risk", -3, "lower", "의료AI subgroup 약점은 실제 도입 리스크다."),
)

ROUND250_SHADOW_WEIGHT_ROWS: tuple[Round250ShadowWeightRow, ...] = (
    Round250ShadowWeightRow(E2RArchetype.BIO_PLATFORM_ROYALTY_CONVERSION, 5, 5, 3, 3, 3, 0, 5, 4, 5, -3, 5, 5, 4, "Alteogen/Keytruda SC needs royalty, supply revenue and patent durability."),
    Round250ShadowWeightRow(E2RArchetype.KOREAN_NEW_DRUG_GLOBAL_APPROVAL, 5, 5, 5, 5, 4, 0, 5, 4, 5, -4, 4, 5, 4, "Yuhan/lazertinib approval is Stage 2 until prescription and royalty revenue confirm."),
    Round250ShadowWeightRow(E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY, 4, 0, 0, 0, 0, 5, 5, 4, 3, -4, 2, 4, 4, "SamsungBio/Celltrion facilities need utilization, backlog, margin and FCF."),
    Round250ShadowWeightRow(E2RArchetype.CMO_M_AND_A_TRANSITION, 4, 0, 0, 0, 0, 5, 5, 4, 4, -5, 2, 5, 4, "SK Bioscience IDT acquisition is Stage 2 until integration and utilization confirm."),
    Round250ShadowWeightRow(E2RArchetype.BIOPHARMA_POLICY_TARIFF_RELIEF, 2, 0, 0, 0, 0, 2, 3, 3, 2, -5, 3, 5, 3, "Policy support is relief, not Green."),
    Round250ShadowWeightRow(E2RArchetype.AUTOIMMUNE_PARTNER_TRIAL_FAILURE, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 5, 3, 5, "HanAll/Immunovant trial failure is partner-program 4C-watch."),
    Round250ShadowWeightRow(E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION, 2, 0, 0, 5, 5, 0, 3, 5, 3, -4, 4, 5, 5, "Lunit external validation is not Green without reimbursement, adoption and revenue."),
    Round250ShadowWeightRow(E2RArchetype.APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN, 0, 0, 0, 0, 0, 0, 0, 4, 3, -5, 4, 5, 4, "Approval or validation headlines stay Stage 2 until commercial conversion."),
)

ROUND250_CASE_CANDIDATES: tuple[Round250CaseCandidate, ...] = (
    Round250CaseCandidate(
        case_id="r7_loop11_alteogen_keytruda_sc_platform_royalty",
        symbol="196170",
        company_name="Alteogen",
        primary_archetype=E2RArchetype.BIO_PLATFORM_ROYALTY_CONVERSION,
        secondary_archetypes=(E2RArchetype.PATENT_CHALLENGE_OVERLAY, E2RArchetype.APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN),
        case_type="success_candidate",
        round_case_type="success_candidate_4b_watch",
        stage1_date=date(2024, 11, 19),
        stage2_date=date(2025, 3, 27),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stage2_strong_but_not_green_until_royalty_supply_revenue_and_patent_durability_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("keytruda_sc_noninferior_trial", "alteogen_enzyme_used", "administration_time_2_to_3_minutes", "keytruda_2024_sales_nearly_30bn_usd", "expected_sc_adoption_30_to_40pct", "fda_decision_target_2025_09_23", "planned_us_launch_2025_10_01"),
        red_flag_fields=("royalty_revenue_unconfirmed", "supply_revenue_unconfirmed", "patent_challenge_possible", "stock_ohlc_unavailable"),
        price_data_source="Reuters / WSJ clinical-launch-patent anchors",
        reported_price_anchor="Alteogen stock OHLC unavailable after deep search",
        reported_return_anchor="Keytruda $30B product base and 30-40% SC adoption target, but no stage3 stock path",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"keytruda_2024_sales_usd_bn": 30.0, "expected_sc_adoption_low_pct": 30.0, "expected_sc_adoption_high_pct": 40.0, "administration_time_minutes": "2_to_3_vs_about_30_iv", "fda_decision_target": "2025-09-23", "planned_us_launch": "2025-10-01", "patent_risk": "Halozyme challenge possible"},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Platform royalty story is Stage 2; Green requires royalty/supply revenue, launch adoption and patent durability.",
    ),
    Round250CaseCandidate(
        case_id="r7_loop11_yuhan_lazertinib_global_approval",
        symbol="000100/039200",
        company_name="Yuhan / Oscotec / Lazertinib",
        primary_archetype=E2RArchetype.KOREAN_NEW_DRUG_GLOBAL_APPROVAL,
        secondary_archetypes=(E2RArchetype.APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN, E2RArchetype.MANUFACTURING_INSPECTION_CRL_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate_launch_revenue_gate",
        stage1_date=date(2024, 8, 1),
        stage2_date=date(2024, 8, 20),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 16),
        stage3_decision="approval_not_green_until_royalty_milestone_prescription_and_revenue_recognition_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("rybrevant_lazcluze_fda_approval", "egfr_mutated_nsclc_first_line", "longer_progression_free_survival", "jj_peak_sales_expectation_over_5bn_usd"),
        red_flag_fields=("royalty_revenue_unconfirmed", "prescription_uptake_unconfirmed", "sc_rybrevant_crl_manufacturing_inspection", "crl_not_efficacy_or_safety"),
        price_data_source="Reuters approval and CRL anchors",
        reported_price_anchor="Yuhan and Oscotec stock OHLC unavailable after deep search",
        reported_return_anchor="FDA approval validates molecule, while SC Rybrevant CRL creates manufacturing-inspection watch",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"jj_peak_sales_expectation_usd_bn": 5.0, "sc_rybrevant_crl_reason": "manufacturing_inspection_observations", "crl_not_related_to_formulation_efficacy_safety": True},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Global approval is Stage 2; royalty, milestone, prescription uptake and revenue recognition decide promotion.",
    ),
    Round250CaseCandidate(
        case_id="r7_loop11_samsung_biologics_gsk_facility_price_failed",
        symbol="207940",
        company_name="Samsung Biologics",
        primary_archetype=E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY,
        secondary_archetypes=(E2RArchetype.CDMO_HEALTHCARE_CONTRACT, E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED),
        case_type="success_candidate",
        round_case_type="evidence_good_but_price_failed",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 12, 22),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stage2_good_evidence_but_price_failed_until_utilization_contract_transfer_margin_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("pharma_policy_support_event", "samsung_bio_policy_event_return_6_23pct", "gsk_rockville_facility_acquisition", "deal_value_280m_usd", "drug_substance_capacity_60000l", "first_us_drug_production_facility"),
        red_flag_fields=("weak_price_reaction", "relative_underperformance_minus_2_4pp", "contract_transfer_unverified", "utilization_unverified", "margin_fcf_unverified"),
        price_data_source="Reuters policy, facility-acquisition and event-return anchors",
        reported_price_anchor="GSK facility event: Samsung Biologics -0.4% vs KOSPI +2.0%",
        reported_return_anchor="Policy support day +6.23%; GSK facility event relative underperformance -2.4pp",
        mfe_1d=6.23,
        mae_1d=-0.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"pharmaceutical_sector_event_mfe_pct": 3.97, "samsung_biologics_policy_event_mfe_pct": 6.23, "gsk_facility_deal_value_usd_mn": 280.0, "facility_capacity_liters": 60000.0, "gsk_facility_event_mae_pct": -0.4, "kospi_same_day_return_pct": 2.0, "relative_underperformance_pp": -2.4},
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Good U.S. CDMO evidence failed immediate price confirmation; utilization and FCF are still required.",
    ),
    Round250CaseCandidate(
        case_id="r7_loop11_celltrion_us_tariff_hedge_factory",
        symbol="068270",
        company_name="Celltrion",
        primary_archetype=E2RArchetype.CDMO_US_TARIFF_HEDGE_CAPACITY,
        secondary_archetypes=(E2RArchetype.BIOSIMILAR_TARIFF_HEDGE_MANUFACTURING,),
        case_type="success_candidate",
        round_case_type="success_candidate_us_tariff_hedge_manufacturing",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 9, 23),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stage2_watch_success_not_green_until_product_transfer_quality_readiness_utilization_margin_and_fcf",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("preferred_bidder_us_manufacturing_facility", "planned_investment_700bn_krw", "imclone_systems_acquisition_330m_usd", "us_manufacturing_base_secured", "expansion_up_to_700bn_krw"),
        red_flag_fields=("product_transfer_unverified", "fda_quality_readiness_unverified", "utilization_unverified", "gross_margin_fcf_unverified"),
        price_data_source="Reuters acquisition and expansion anchors",
        reported_price_anchor="Celltrion stock OHLC unavailable after deep search",
        reported_return_anchor="ImClone $330M acquisition plus expansion up to 700B won, but no stage3 price path",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"preferred_bidder_investment_plan_krw_bn": 700.0, "possible_additional_investment_krw_bn_low": 300.0, "possible_additional_investment_krw_bn_high": 700.0, "imclone_acquisition_value_usd_mn": 330.0, "expansion_investment_krw_bn": 700.0, "expansion_investment_usd_mn": 478.17, "usd_330m_krw_equivalent_at_1463_9_bn": 483.1, "combined_acquisition_plus_expansion_krw_trn": 1.183},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="U.S. tariff-hedge manufacturing is Stage 2; product transfer, utilization, margin and FCF decide Stage 3.",
    ),
    Round250CaseCandidate(
        case_id="r7_loop11_sk_bioscience_idt_cmo_mna",
        symbol="302440",
        company_name="SK Bioscience",
        primary_archetype=E2RArchetype.CMO_M_AND_A_TRANSITION,
        secondary_archetypes=(E2RArchetype.CDMO_HEALTHCARE_CONTRACT, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_event_premium",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=date(2024, 6, 27),
        stage4c_date=None,
        stage3_decision="mna_stage2_not_green_until_backlog_utilization_margin_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("idt_biologika_60pct_acquisition", "deal_value_339bn_krw", "deal_value_243_75m_usd", "first_major_mna_since_2021_ipo", "event_morning_return_11_7pct"),
        red_flag_fields=("mna_without_utilization", "backlog_unverified", "integration_cost_unverified", "cash_burn_or_goodwill_impairment_watch"),
        price_data_source="Reuters acquisition and event-return anchor",
        reported_price_anchor="SK Bioscience +11.7% morning trade after IDT Biologika acquisition",
        reported_return_anchor="Announcement rally before utilization/backlog confirmation",
        mfe_1d=11.7,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"deal_value_krw_bn": 339.0, "deal_value_usd_mn": 243.75, "stake_acquired_pct": 60.0, "implied_idt_equity_value_krw_bn": 565.0, "remaining_klocke_stake_pct": 40.0, "sk_bioscience_2021_ipo_proceeds_usd_bn": 1.33, "deal_value_vs_ipo_proceeds_pct": 18.3, "event_mfe_morning_pct": 11.7},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="M&A is Stage 2/event premium; backlog, utilization, margin and FCF are required before Green.",
    ),
    Round250CaseCandidate(
        case_id="r7_loop11_hanall_immunovant_batoclimab_ted_failure",
        symbol="009420",
        company_name="HanAll Biopharma / Immunovant",
        primary_archetype=E2RArchetype.AUTOIMMUNE_PARTNER_TRIAL_FAILURE,
        secondary_archetypes=(E2RArchetype.THESIS_BREAK_4C_WATCH, E2RArchetype.BIOTECH_PRE_REVENUE_REGULATORY),
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
        red_flag_fields=("partner_trial_failure", "two_late_stage_ted_trials_failed", "primary_endpoint_not_met", "immunovant_event_mae_4_8pct", "hard_4c_not_confirmed_for_entire_pipeline"),
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
        notes="Partner trial failure is 4C-watch; hard 4C is not forced without broader pipeline or cashflow impairment.",
    ),
    Round250CaseCandidate(
        case_id="r7_loop11_lunit_medical_ai_external_validation",
        symbol="328130",
        company_name="Lunit",
        primary_archetype=E2RArchetype.MEDICAL_AI_EXTERNAL_VALIDATION,
        secondary_archetypes=(E2RArchetype.APPROVAL_OR_VALIDATION_ONLY_NOT_GREEN,),
        case_type="failed_rerating",
        round_case_type="insufficient_evidence",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2025, 3, 17),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="validation_not_revenue_until_reimbursement_hospital_adoption_recurring_revenue_margin_and_cash_runway_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("lunit_insight_dbt_external_validation", "screening_mammography_exams_163449", "screen_detected_cancers_1368", "overall_auc_0_91", "subgroup_performance_reported"),
        red_flag_fields=("reimbursement_unverified", "hospital_adoption_unverified", "recurring_revenue_unverified", "cash_runway_unverified", "subgroup_performance_risk", "non_invasive_cancer_auc_0_85", "calcification_auc_0_80"),
        price_data_source="arXiv external validation evidence",
        reported_price_anchor="Lunit stock OHLC unavailable after deep search",
        reported_return_anchor="AUC 0.91 with subgroup weakness, but no reimbursement/adoption revenue anchor",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"exam_count": 163449.0, "positive_cases": 1368.0, "negative_exams": 162081.0, "overall_auc": 0.91, "precision": 0.08, "recall": 0.73, "non_invasive_cancer_auc": 0.85, "calcification_auc": 0.80, "dense_breast_auc": 0.90},
        score_price_alignment="unknown",
        rerating_result="no_rerating",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="External validation is Stage 2 evidence; reimbursement, hospital adoption, recurring revenue and cash runway block Green.",
    ),
    Round250CaseCandidate(
        case_id="r7_loop11_biopharma_tariff_policy_relief_basket",
        symbol="207940/068270/biopharma_basket",
        company_name="Biopharma tariff-policy basket",
        primary_archetype=E2RArchetype.BIOPHARMA_POLICY_TARIFF_RELIEF,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM,),
        case_type="event_premium",
        round_case_type="event_premium_policy_relief",
        stage1_date=date(2025, 5, 20),
        stage2_date=date(2025, 5, 21),
        stage3_date=None,
        stage4b_date=date(2025, 5, 21),
        stage4c_date=None,
        stage3_decision="policy_relief_not_green_until_company_level_order_tariff_pass_through_margin_localization_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("us_tariff_pressure_on_pharmaceuticals", "korea_biopharma_support_policy", "pharmaceutical_sector_event_return_3_97pct", "samsung_bio_event_return_6_23pct", "celltrion_event_return_0_35pct"),
        red_flag_fields=("policy_support_without_order", "company_level_margin_unconfirmed", "us_plant_cost_burden_watch", "tariff_details_worsen_watch"),
        price_data_source="Reuters policy and sector-return anchor",
        reported_price_anchor="Pharmaceutical sector +3.97%, SamsungBio +6.23%, Celltrion +0.35%",
        reported_return_anchor="Policy-support sector rally before company-level earnings bridge",
        mfe_1d=3.97,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        extra_price_metrics={"pharmaceutical_sector_event_mfe_pct": 3.97, "samsung_biologics_event_mfe_pct": 6.23, "celltrion_event_mfe_pct": 0.35, "kospi_same_context_pct": 0.99, "foreign_net_buy_krw_bn": 113.7, "foreign_net_buy_usd_mn": 82.05, "won_strengthening_pct": 0.56},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="policy_event_rerating",
        stage_failure_type="false_yellow",
        price_validation_status="reported_sector_anchor_not_full_ohlc",
        notes="Policy relief is event premium; company-level revenue, margin and FCF are required before Green.",
    ),
)


def round250_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND250_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND250_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round250 R7 Loop-11 biotech/healthcare/device price validation case. Calibration-only; not production scoring input.",
            stage1_evidence=tuple(field for field in candidate.evidence_fields if "trial" in field or "approval" in field or "policy" in field or "validation" in field or "pipeline" in field),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if "revenue" in field or "royalty" in field or "capacity" in field or "launch" in field or "sales" in field),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "event" in field or "policy" in field or "mna" in field or "price" in field or "valuation" in field or "premium" in field),
            stage4c_evidence=tuple(field for field in candidate.red_flag_fields if "failure" in field or "failed" in field or "crl" in field or "inspection" in field or "patent" in field or "subgroup" in field or "cash" in field or "dilution" in field or "partner" in field),
            must_have_fields=ROUND250_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=("; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4c_thesis_break"} else None),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND250_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "hard_4c_confirmed_false",
                "do_not_invent_price_stage_dates_royalty_prescription_reimbursement_utilization_margin_or_fcf",
                "do_not_treat_approval_clinical_validation_policy_mna_or_facility_headline_as_green",
                f"round_case_type={candidate.round_case_type}",
                *ROUND250_GREEN_REQUIRED_FIELDS,
                *ROUND250_GREEN_FORBIDDEN_PATTERNS,
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
                stage_dates_confidence=0.84 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round250_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND250_CASE_CANDIDATES:
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


def round250_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND250_SCORE_ADJUSTMENTS)


def round250_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND250_SHADOW_WEIGHT_ROWS)


def round250_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round250_price_validation": "true"} for field in ROUND250_PRICE_VALIDATION_FIELDS)


def round250_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round250_label": label, "canonical_archetype": canonical} for label, canonical in ROUND250_REQUIRED_TARGET_ALIASES.items())


def round250_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple({"deep_sub_archetype": item, "large_sector": ROUND250_LARGE_SECTOR} for item in ROUND250_DEEP_SUB_ARCHETYPES)


def round250_summary() -> dict[str, int | bool | str]:
    cases = ROUND250_CASE_CANDIDATES
    return {
        "source_round": ROUND250_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND250_ANALYST_ROUND_ID,
        "large_sector": ROUND250_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "target_archetype_count": len(ROUND250_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND250_DEEP_SUB_ARCHETYPES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": False,
    }


def round250_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND250_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND250_ANALYST_ROUND_ID,
        "large_sector": ROUND250_LARGE_SECTOR,
        "summary": round250_summary(),
        "target_aliases": dict(ROUND250_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetypes": list(ROUND250_DEEP_SUB_ARCHETYPES),
        "green_required_fields": list(ROUND250_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND250_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND250_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND250_HARD_4C_GATES),
        "case_ids": [case.case_id for case in ROUND250_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_use_round250_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_fda_approval_clinical_ai_policy_mna_or_facility_headline_as_green",
            "do_not_confirm_hard_4c_without_company_level_impairment",
            "do_not_invent_ohlc_stage_prices_or_business_metrics",
        ],
    }


def render_round250_summary_markdown() -> str:
    summary = round250_summary()
    lines = [
        "# Round 250 R7 Loop 11 Biotech Healthcare Device Price Validation",
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
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
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
    for case in ROUND250_CASE_CANDIDATES:
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
            "- Alteogen is a strong platform royalty Stage 2, but Green waits for launch adoption, royalty/supply revenue and patent durability.",
            "- Yuhan/lazertinib is global approval Stage 2, not Stage 3 until royalty, milestone and prescription uptake are visible.",
            "- Samsung Biologics has good U.S. CDMO evidence but immediate price confirmation failed.",
            "- Celltrion and SK Bioscience need product transfer, utilization, backlog, margin and FCF before Green.",
            "- HanAll/Immunovant partner trial failure is RedTeam 4C-watch, not a forced hard 4C for the whole company.",
            "- Lunit external validation is useful but reimbursement, hospital adoption and recurring revenue decide promotion.",
            "- Biopharma tariff policy is event relief, not company-level Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round250_green_gate_review_markdown() -> str:
    lines = [
        "# Round 250 R7 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND250_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND250_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND250_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `FDA approval` is Stage 2 attention. It is not Green until prescriptions, reimbursement, revenue, margin and cash runway follow.",
            "- `AUC 0.91 medical AI validation` is useful evidence, but it is not commercial revenue.",
            "- `M&A announcement +11.7%` is 4B/event premium until utilization, backlog, margin and FCF exist.",
            "- `Partner trial failure` belongs in RedTeam even when Korean-stock OHLC is missing.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round250_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 250 R7 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND250_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND250_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | 4C-watch date | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND250_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.stage4b_status} | {_date_text(case.stage4c_date)} | "
            f"{str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round250_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 250 R7 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: false",
        "- Do not invent OHLC, peak, MFE, MAE, stage prices, prescription volume, utilization, margin, FCF, or royalty values.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND250_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND250_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def render_round250_deep_sub_archetypes_markdown() -> str:
    lines = [
        "# Round 250 R7 Deep Sub-Archetypes",
        "",
        "These labels describe research coverage. They are not production scoring inputs.",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND250_DEEP_SUB_ARCHETYPES)
    return "\n".join(lines) + "\n"


def write_round250_r7_loop11_reports(
    output_directory: str | Path = ROUND250_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND250_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND250_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round250_case_records(), cases_path),
        "audit": _write_json(round250_audit_payload(), audit_path),
        "summary": output / "round250_r7_loop11_price_validation_summary.md",
        "case_matrix": output / "round250_r7_loop11_case_matrix.csv",
        "target_aliases": output / "round250_r7_loop11_target_aliases.csv",
        "deep_sub_archetypes": output / "round250_r7_loop11_deep_sub_archetypes.csv",
        "score_adjustments": output / "round250_r7_loop11_score_adjustments.csv",
        "shadow_weights": output / "round250_r7_loop11_shadow_weights.csv",
        "price_validation_fields": output / "round250_r7_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round250_r7_loop11_green_gate_review.md",
        "price_validation_plan": output / "round250_r7_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round250_r7_loop11_stage4b_4c_review.md",
        "deep_sub_archetype_review": output / "round250_r7_loop11_deep_sub_archetypes.md",
    }
    paths["summary"].write_text(render_round250_summary_markdown(), encoding="utf-8")
    _write_csv(round250_case_rows(), paths["case_matrix"])
    _write_csv(round250_target_alias_rows(), paths["target_aliases"])
    _write_csv(round250_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round250_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round250_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round250_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round250_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round250_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round250_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["deep_sub_archetype_review"].write_text(render_round250_deep_sub_archetypes_markdown(), encoding="utf-8")
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
    return f"{value:+d}"
