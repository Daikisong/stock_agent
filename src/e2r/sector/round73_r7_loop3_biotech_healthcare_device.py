"""Round-73 R7 Loop-3 biotech, healthcare, and medical-device pack.

Round 73 tightens the Round-47 healthcare pack. It separates approvals,
clinical wins, AI papers, user growth, and large TAM stories from actual
commercialization evidence: prescriptions, reimbursement, revenue conversion,
capacity utilization, recurring procedures, consumables, OPM, FCF, and cash
runway.

This module is calibration/report material only. Production feature
engineering, scoring, staging, and RedTeam code must not import it.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import CaseDataQuality, E2RCaseRecord, PriceValidation
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture


ROUND73_SOURCE_ROUND_PATH = "docs/round/round_73.md"
ROUND73_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round73_r7_loop3_biotech_healthcare_device"
ROUND73_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_loop3_round73.jsonl"
ROUND73_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round73_r7_loop3_v3.csv"


@dataclass(frozen=True)
class Round73ScoreWeightDraft:
    eps_fcf: int | str
    structural_visibility: int | str
    bottleneck_pricing: int | str
    market_mispricing: int | str
    valuation: int | str
    capital_allocation: int | str
    information_confidence: int | str

    def as_dict(self) -> dict[str, int | str]:
        return {
            "eps_fcf": self.eps_fcf,
            "structural_visibility": self.structural_visibility,
            "bottleneck_pricing": self.bottleneck_pricing,
            "market_mispricing": self.market_mispricing,
            "valuation": self.valuation,
            "capital_allocation": self.capital_allocation,
            "information_confidence": self.information_confidence,
        }


@dataclass(frozen=True)
class Round73ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round73ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop3_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round73CaseCandidate:
    case_id: str
    target_id: str
    symbol: str
    company_name: str
    market: str
    case_type: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    alignment_hint: str
    price_validation_status: str
    source_refs: tuple[str, ...]
    notes: str
    secondary_archetypes: tuple[E2RArchetype, ...] = ()

    @property
    def expected_group(self) -> str:
        return self.case_type


GATE_WEIGHT = Round73ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate")


ROUND73_SCORE_TARGETS: tuple[Round73ScoreTarget, ...] = (
    Round73ScoreTarget(
        "CDMO_HEALTHCARE_CONTRACT",
        E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round73ScoreWeightDraft(20, 24, 12, 12, 12, 0, 5),
        ("cdmo_contract", "capacity_expansion", "new_manufacturing_site", "us_eu_local_production"),
        ("long_term_contract", "capacity_utilization", "customer_diversification", "op_eps_revision"),
        ("multi_year_production_visibility", "fcf_conversion", "utilization_leverage", "high_value_modality_mix"),
        ("capacity_premium_overheated", "capex_story_priced_before_utilization"),
        ("utilization_down", "contract_delay", "capex_burden", "tariff_or_quality_issue", "us_operating_cost"),
        ("long_term_contract", "capacity_utilization", "customer_diversification", "fcf_conversion"),
        ("underutilization", "customer_concentration", "capex_burden", "quality_issue", "tariff", "us_operating_cost"),
        ("utilization", "customer_contract", "capex", "quality"),
        "CDMO is Green-capable, but capacity alone is not Stage 3 without utilization, contracts, margin, and FCF.",
    ),
    Round73ScoreTarget(
        "CRO_CLINICAL_SERVICE",
        E2RArchetype.CRO_CLINICAL_SERVICE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round73ScoreWeightDraft(16, 17, 7, 11, 9, 0, 5),
        ("clinical_service_backlog", "pharma_rd_budget", "trial_volume_growth"),
        ("service_revenue_growth", "customer_diversification", "repeat_service_revenue", "funding_cycle_stable"),
        ("multi_year_backlog", "funding_cycle_stable", "high_fcf_conversion"),
        ("cro_recovery_expectation_overheated",),
        ("biotech_funding_crunch", "customer_rd_budget_cut", "forecast_cut", "order_cancellation", "revenue_decline"),
        ("service_backlog", "customer_diversification", "repeat_service_revenue", "opm_improvement"),
        ("biotech_funding_cycle_down", "customer_budget_cut", "trial_delay", "low_margin_backlog", "forecast_cut"),
        ("funding_cycle", "customer_budget", "forecast_cut"),
        "CRO is service revenue, but funding-cycle cuts can break backlog and forecast visibility.",
    ),
    Round73ScoreTarget(
        "BIOSIMILAR_COMMERCIALIZATION",
        E2RArchetype.BIOSIMILAR_COMMERCIALIZATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round73ScoreWeightDraft(18, 18, 6, 12, 9, 0, 6),
        ("fda_ema_approval", "patent_expiry", "biosimilar_launch", "discount_access_program"),
        ("pbm_listing", "insurance_coverage", "prescription_conversion", "launch_revenue"),
        ("prescription_growth", "margin_defense", "multi_country_launch", "payer_access"),
        ("approval_news_overheated", "biosimilar_launch_crowded"),
        ("price_competition", "prescription_conversion_delay", "margin_collapse", "pbm_incentive_gap"),
        ("pbm_listing", "insurance_coverage", "prescription_conversion", "revenue_conversion"),
        ("price_competition", "coverage_gap", "slow_switching", "margin_pressure", "pbm_incentive_gap"),
        ("pbm", "coverage", "prescription_switch", "margin"),
        "Biosimilar approval and discount are Stage 1; PBM, coverage, prescriptions, and margin decide higher stages.",
    ),
    Round73ScoreTarget(
        "BIOSIMILAR_ORIGINATOR_DEFENSE",
        E2RArchetype.BIOSIMILAR_ORIGINATOR_DEFENSE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round73ScoreWeightDraft(19, 18, 8, 13, 11, 2, 6),
        ("patent_cliff", "originator_defense", "pipeline_replacement"),
        ("pipeline_revenue_offset", "price_defense", "capital_allocation"),
        ("defended_revenue_base", "new_product_offset", "margin_protection"),
        ("defense_narrative_overpriced",),
        ("patent_cliff", "pipeline_failure", "pricing_pressure", "share_loss"),
        ("pipeline_revenue_offset", "price_defense", "margin_protection"),
        ("patent_cliff", "pipeline_failure", "share_loss", "pricing_pressure"),
        ("patent_cliff", "pipeline_offset", "pricing_pressure"),
        "Originator defense needs actual revenue offset, not litigation or patent language alone.",
    ),
    Round73ScoreTarget(
        "OBESITY_GLP1_COMMERCIALIZATION",
        E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round73ScoreWeightDraft(22, 20, 12, 13, 10, 0, 6),
        ("glp1_approval", "oral_glp1_trial", "prescription_growth", "maintenance_therapy_data"),
        ("weekly_scripts", "insurance_coverage", "supply_capacity", "sales_ramp", "price_defense"),
        ("durable_prescription_growth", "price_defense", "op_eps_revision", "coverage_expansion", "maintenance_use_case"),
        ("obesity_market_narrative_crowded", "scripts_lag_valuation", "market_size_priced_before_uptake"),
        ("compounded_alternative", "price_cut", "coverage_denial", "prescription_slowdown", "telehealth_channel_risk"),
        ("prescription_volume", "insurance_coverage", "supply_capacity", "price_defense", "op_eps_revision"),
        ("competition", "compounded_alternative", "coverage_gap", "price_regulation", "slow_uptake", "telehealth_channel_risk"),
        ("scripts", "coverage", "price", "competition", "compounded_drugs"),
        "GLP-1 can be Green, but TAM is not enough; scripts, coverage, price, supply, and OP/EPS must follow.",
    ),
    Round73ScoreTarget(
        "GLP1_TELEHEALTH_CHANNEL",
        E2RArchetype.GLP1_TELEHEALTH_CHANNEL,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round73ScoreWeightDraft(18, 15, 5, 13, 8, 0, 6),
        ("telehealth_glp1_offering", "compounded_product", "branded_partnership_news"),
        ("subscriber_growth", "branded_drug_attach", "legal_settlement", "channel_revenue"),
        ("cac_stable", "gross_margin_stable", "compliance_clean", "fcf_conversion"),
        ("dtc_glp1_channel_valuation_overheated", "channel_event_premium_crowded"),
        ("fda_crackdown", "compounding_ban", "legal_cost", "revenue_recognition_shock", "cac_spike"),
        ("branded_drug_attach", "cac_stable", "gross_margin_stable", "compliance_clean", "fcf_conversion"),
        ("compounding_crackdown", "revenue_recognition", "legal_cost", "cac", "margin_compression"),
        ("cac", "compounding", "revenue_recognition", "legal_cost"),
        "GLP-1 telehealth channels are separated from drug commercialization because channel economics and compliance can break the thesis.",
    ),
    Round73ScoreTarget(
        "GENE_THERAPY_RARE_DISEASE",
        E2RArchetype.GENE_THERAPY_RARE_DISEASE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round73ScoreWeightDraft(7, 10, 8, 9, 5, 0, 5),
        ("gene_therapy_approval", "rare_disease_unmet_need", "patient_recruitment"),
        ("treated_patients", "reimbursement", "commercial_sales", "cash_runway"),
        ("repeat_commercial_uptake", "dilution_risk_controlled", "pipeline_revenue"),
        ("approval_news_overheated", "rare_disease_story_crowded"),
        ("slow_uptake", "cash_crunch", "going_concern", "discounted_take_private", "dilution"),
        ("patient_uptake", "reimbursement", "cash_runway", "commercial_revenue"),
        ("cash_burn", "reimbursement_failure", "slow_uptake", "dilution", "going_concern"),
        ("cash_runway", "reimbursement", "patient_uptake", "dilution"),
        "Approval without commercial uptake and cash runway is not Green.",
    ),
    Round73ScoreTarget(
        "AI_DRUG_DISCOVERY_PLATFORM",
        E2RArchetype.AI_DRUG_DISCOVERY_PLATFORM,
        Round10ThemePosture.REDTEAM_FIRST,
        Round73ScoreWeightDraft(6, 10, 7, 12, 6, 0, 5),
        ("ai_drug_discovery_platform", "candidate_molecule", "platform_partnership"),
        ("big_pharma_milestone", "clinical_entry", "cash_runway"),
        ("validated_pipeline", "partner_funded_progress", "commercial_or_royalty_path"),
        ("ai_drug_platform_overheated", "poc_story_crowded"),
        ("clinical_failure", "cash_burn", "platform_hype_unwind", "no_approved_drug"),
        ("big_pharma_partnership", "clinical_progress", "cash_runway", "milestone_revenue"),
        ("no_approved_drug", "cash_burn", "clinical_failure", "platform_hype"),
        ("milestone", "clinical_progress", "cash_runway", "approved_drug"),
        "AI drug-discovery labels are not score evidence without milestones, clinical progress, and cash runway.",
    ),
    Round73ScoreTarget(
        "DIGITAL_HEALTHCARE_AI",
        E2RArchetype.DIGITAL_HEALTHCARE_AI,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round73ScoreWeightDraft(18, 17, 8, 13, 12, 0, 7),
        ("clinical_ai_paper", "external_validation", "hospital_pilot", "regulatory_clearance"),
        ("hospital_adoption", "reimbursement", "paid_workflow", "recurring_revenue"),
        ("workflow_embedded", "recurring_revenue", "op_improvement", "liability_risk_low"),
        ("medical_ai_narrative_overheated", "paper_only_valuation_premium"),
        ("subgroup_performance_issue", "reimbursement_denial", "liability_event", "hospital_adoption_failure"),
        ("external_validation", "hospital_adoption", "reimbursement_or_paid_usage", "recurring_revenue"),
        ("subgroup_bias", "no_reimbursement", "liability", "poc_only", "date_unverified"),
        ("hospital_adoption", "reimbursement", "subgroup", "liability"),
        "Medical AI papers lift Stage 1/2, but Green requires paid adoption and reimbursement.",
    ),
    Round73ScoreTarget(
        "DIGITAL_HEALTHCARE_REMOTE_MEDICINE",
        E2RArchetype.DIGITAL_HEALTHCARE_REMOTE_MEDICINE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round73ScoreWeightDraft(16, 16, 7, 12, 9, 1, 6),
        ("remote_medicine_policy", "wearable_or_emr_integration", "digital_health_platform"),
        ("hospital_or_insurer_contract", "b2b_b2b2c_contract", "recurring_subscription", "unit_economics"),
        ("embedded_workflow", "reimbursement_visible", "repeat_usage", "opm_improvement"),
        ("telehealth_theme_crowded",),
        ("regulatory_reversal", "reimbursement_failure", "privacy_incident", "unit_economics_failure"),
        ("hospital_or_insurer_contract", "recurring_revenue", "unit_economics", "regulatory_clearance"),
        ("regulation", "privacy", "reimbursement", "cac", "churn"),
        ("regulation", "reimbursement", "unit_economics", "privacy"),
        "Remote medicine needs contracts, reimbursement, and unit economics, not usage story alone.",
    ),
    Round73ScoreTarget(
        "TELEHEALTH_BEHAVIORAL_HEALTH",
        E2RArchetype.TELEHEALTH_BEHAVIORAL_HEALTH,
        Round10ThemePosture.REDTEAM_FIRST,
        Round73ScoreWeightDraft(15, 13, 5, 10, 8, 0, 6),
        ("online_behavioral_health_demand", "subscriber_growth", "dtc_health_platform"),
        ("employer_or_insurer_contract", "cac_stable", "repeat_usage"),
        ("low_churn_contract_revenue", "fcf_margin", "privacy_clean"),
        ("dtc_telehealth_growth_crowded",),
        ("cac_spike", "privacy_incident", "impairment", "forecast_withdrawal", "churn"),
        ("employer_or_insurer_contract", "cac_stable", "churn_stable", "fcf_margin"),
        ("cac", "privacy", "impairment", "forecast_withdrawal", "churn"),
        ("cac", "privacy", "impairment", "churn"),
        "DTC telehealth is RedTeam-first unless contract revenue and unit economics are clear.",
    ),
    Round73ScoreTarget(
        "PHARMA_CHANNEL_AND_PRIVACY_RISK",
        E2RArchetype.PHARMA_CHANNEL_AND_PRIVACY_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("online_pharmacy", "compounded_drug_channel", "health_data_platform"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("fda_ftc_scrutiny", "compounded_quality_issue", "privacy_breach", "margin_collapse", "doj_referral_risk"),
        (),
        ("fda_ftc_scrutiny", "compounded_quality_issue", "privacy_breach", "margin_pressure", "illegal_copycat_drug"),
        ("fda", "ftc", "privacy", "compounded_quality"),
        "Compounded drug, FDA/FTC, advertising, and privacy risks are RedTeam gates, not positive score buckets.",
        gate_only=True,
    ),
    Round73ScoreTarget(
        "MEDICAL_DEVICE_HEALTHCARE_EXPORT",
        E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round73ScoreWeightDraft(20, 22, 13, 14, 12, 0, 5),
        ("medical_device_export", "new_approval", "procedure_growth"),
        ("export_country_expansion", "recurring_procedure", "consumable_revenue", "opm_roe_improvement"),
        ("repeat_procedure_demand", "asp_stable", "fcf_improvement", "channel_quality"),
        ("device_premium_crowded", "target_multiple_saturated"),
        ("approval_delay", "safety_issue", "price_control", "channel_failure", "single_device_no_consumable"),
        ("export_growth", "consumable_repeat_revenue", "regulatory_approval", "opm_roe_improvement"),
        ("approval_delay", "safety", "competition", "channel_quality", "single_device_no_consumable"),
        ("approval", "safety", "channel_quality", "procedure_repeat"),
        "Medical-device Green needs repeat procedures, consumables, approvals, and export/channel proof.",
    ),
    Round73ScoreTarget(
        "MEDICAL_DEVICE_DENTAL_IMPLANT",
        E2RArchetype.MEDICAL_DEVICE_DENTAL_IMPLANT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round73ScoreWeightDraft(20, 22, 13, 14, 12, 0, 5),
        ("dental_implant_growth", "procedure_growth", "approval_or_channel"),
        ("export_country_expansion", "recurring_procedure_consumable", "opm_roe_improvement"),
        ("approval_stable", "repeat_consumable_revenue", "pricing_pressure_low", "channel_quality"),
        ("implant_premium_crowded", "vbp_risk_ignored"),
        ("vbp_price_control", "asp_drop", "approval_delay", "safety_issue", "competition"),
        ("recurring_procedure_consumable", "approval_stable", "opm_roe_improvement", "channel_quality"),
        ("vbp_price_control", "approval", "safety", "competition", "asp_drop"),
        ("vbp", "asp", "approval", "procedure_repeat"),
        "Dental implant Green is possible, but VBP and ASP compression are hard risk gates.",
    ),
    Round73ScoreTarget(
        "SURGICAL_ROBOT_INSTALLED_BASE",
        E2RArchetype.SURGICAL_ROBOT_INSTALLED_BASE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round73ScoreWeightDraft(21, 23, 13, 14, 12, 1, 5),
        ("new_robot_launch", "installed_base_growth", "procedure_growth"),
        ("procedure_growth", "system_placement", "instruments_accessories_revenue"),
        ("recurring_consumable_revenue", "installed_base_expansion", "opm_fcf_improvement"),
        ("surgical_robot_platform_premium_overheated", "installed_base_fully_priced"),
        ("hospital_capex_slowdown", "procedure_mix_worse", "glp1_bariatric_slowdown", "competition"),
        ("installed_base", "procedure_growth", "instruments_accessories_revenue", "opm_fcf_improvement"),
        ("hospital_capex", "procedure_mix", "glp1_bariatric_slowdown", "competition"),
        ("installed_base", "procedure_growth", "consumables", "hospital_capex"),
        "Surgical robots are separated from generic medical devices because installed base plus instruments/accessories can create recurring revenue.",
    ),
    Round73ScoreTarget(
        "BOTULINUM_AESTHETIC_REGULATED",
        E2RArchetype.BOTULINUM_AESTHETIC_REGULATED,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round73ScoreWeightDraft(19, 20, 12, 13, 11, 0, 5),
        ("botulinum_toxin_demand", "aesthetic_procedure_growth", "licensed_channel"),
        ("repeat_procedure", "regulatory_approval", "safe_distribution_channel", "op_eps_revision"),
        ("licensed_repeat_procedure", "safety_clean", "export_channel", "fcf_conversion"),
        ("aesthetic_toxin_premium_crowded",),
        ("counterfeit_product", "unapproved_product", "injury_report", "channel_failure", "safety_issue"),
        ("regulatory_approval", "repeat_procedure", "safe_distribution_channel", "op_eps_revision"),
        ("counterfeit", "unapproved_product", "safety", "channel_failure"),
        ("counterfeit", "approval", "licensed_channel", "safety"),
        "Aesthetic toxins are Watch-to-Green only through licensed, safe, repeat-procedure channels.",
    ),
    Round73ScoreTarget(
        "DIAGNOSTICS_INFECTIOUS_DISEASE",
        E2RArchetype.DIAGNOSTICS_INFECTIOUS_DISEASE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round73ScoreWeightDraft(20, 5, 5, 5, 5, 0, 5),
        ("infectious_disease_diagnostic_demand", "pandemic_or_mpox_event", "test_kit_sales_spike"),
        ("recurring_non_event_demand", "installed_base_consumables", "post_event_revenue"),
        ("recurring_platform_revenue", "margin_normalization", "non_event_demand"),
        ("diagnostic_event_extrapolated",),
        ("one_off_demand", "guidance_down", "inventory_build", "demand_cliff"),
        ("recurring_non_event_demand", "post_event_revenue", "margin_normalization"),
        ("one_off_demand", "inventory_build", "guidance_down", "demand_cliff"),
        ("one_off_demand", "inventory", "guidance_down"),
        "Infectious diagnostics are RedTeam-first because event demand can disappear quickly.",
    ),
    Round73ScoreTarget(
        "COMMERCIALIZATION_FAILURE_OVERLAY",
        E2RArchetype.COMMERCIALIZATION_FAILURE_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("approval_without_uptake", "launch_without_revenue", "commercialization_gap"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("slow_uptake", "reimbursement_failure", "commercial_revenue_missing", "cash_crunch", "going_concern"),
        (),
        ("slow_uptake", "reimbursement_failure", "commercial_revenue_missing", "cash_runway_short", "going_concern"),
        ("uptake", "reimbursement", "commercial_revenue", "cash_runway"),
        "Approval after commercialization failure is a RedTeam gate, not positive evidence.",
        gate_only=True,
    ),
    Round73ScoreTarget(
        "REIMBURSEMENT_ACCESS_OVERLAY",
        E2RArchetype.REIMBURSEMENT_ACCESS_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("coverage_gap", "pbm_access_issue", "reimbursement_denial", "pricing_pressure"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("insurance_denial", "pbm_exclusion", "reimbursement_failure", "gross_to_net_pressure", "prescription_conversion_delay"),
        (),
        ("insurance_denial", "pbm_exclusion", "reimbursement_failure", "gross_to_net_pressure", "prescription_conversion_delay"),
        ("coverage", "pbm", "reimbursement", "gross_to_net", "prescription_conversion"),
        "Insurance, PBM, reimbursement, and access failures can block GLP-1, biosimilar, gene therapy, and medical AI theses.",
        gate_only=True,
    ),
    Round73ScoreTarget(
        "DEVICE_SAFETY_COUNTERFEIT_OVERLAY",
        E2RArchetype.DEVICE_SAFETY_COUNTERFEIT_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("counterfeit_product", "unapproved_device", "recall_or_warning", "product_safety_issue"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("counterfeit_product", "unapproved_injectable", "fda_warning", "injury_report", "licensed_channel_failure", "recall"),
        (),
        ("counterfeit_product", "unapproved_injectable", "fda_warning", "injury_report", "licensed_channel_failure", "recall"),
        ("safety", "license", "channel", "recall", "counterfeit"),
        "Safety, counterfeit, unapproved product, and recall issues are device/aesthetic RedTeam gates.",
        gate_only=True,
    ),
)


ROUND73_CASE_CANDIDATES: tuple[Round73CaseCandidate, ...] = (
    Round73CaseCandidate(
        "samsung_biologics_gsk_us_facility_case",
        "CDMO_HEALTHCARE_CONTRACT",
        "207940",
        "Samsung Biologics GSK US facility acquisition",
        "KR",
        "success_candidate",
        None,
        date(2025, 12, 22),
        None,
        None,
        None,
        ("us_manufacturing_site", "capacity_liters", "capacity_expansion", "tariff_mitigation"),
        ("utilization_unverified", "capex_burden", "customer_contract_unverified", "us_operating_cost"),
        "strategic_cdmo_success_candidate_price_alignment_delayed",
        "needs_price_backfill",
        ("round_73.md Reuters Samsung Biologics GSK US facility",),
        "US capacity is strategic, but utilization, customer contracts, CAPEX, and FCF must be verified.",
    ),
    Round73CaseCandidate(
        "samsung_biologics_cdmo_capacity_reference",
        "CDMO_HEALTHCARE_CONTRACT",
        "207940",
        "Samsung Biologics CDMO capacity reference",
        "KR",
        "structural_success",
        None,
        None,
        None,
        None,
        None,
        ("major_pharma_contracts", "customer_diversification", "capacity_liters", "high_value_modality_mix"),
        ("customer_concentration", "contract_delay", "quality_issue", "underutilization"),
        "cdmo_structural_reference",
        "needs_source_date_and_price_backfill",
        ("round_73.md Samsung Biologics CDMO structure reference",),
        "CDMO references are Green-eligible only after contract, utilization, margin, and FCF conversion are matched to stage dates.",
    ),
    Round73CaseCandidate(
        "intuitive_surgical_q1_2026_procedure_growth_case",
        "SURGICAL_ROBOT_INSTALLED_BASE",
        "ISRG",
        "Intuitive Surgical Q1 2026 procedure growth and recurring consumables",
        "US",
        "structural_success",
        None,
        date(2026, 4, 1),
        None,
        None,
        None,
        ("installed_base", "procedure_growth", "system_placement", "instruments_accessories_revenue", "guidance_raise"),
        ("hospital_capex_cycle", "procedure_mix_risk", "glp1_bariatric_slowdown", "medtech_valuation_compression"),
        "surgical_robot_recurring_consumable_success",
        "needs_exact_stage_date_and_price_backfill",
        ("round_73.md Investors Intuitive Surgical Q1 2026",),
        "Installed base, procedure growth, and instruments/accessories revenue make surgical robots a separate recurring-revenue archetype.",
    ),
    Round73CaseCandidate(
        "straumann_dental_implant_vbp_case",
        "MEDICAL_DEVICE_DENTAL_IMPLANT",
        "STMN.SW",
        "Straumann dental implant growth with VBP risk",
        "CH",
        "success_candidate",
        None,
        date(2026, 2, 18),
        None,
        None,
        None,
        ("sales_growth", "procedure_growth", "regional_growth", "guidance_growth"),
        ("vbp_price_control", "asp_pressure", "china_procurement_uncertainty"),
        "medical_device_aligned_candidate",
        "needs_price_backfill",
        ("round_73.md Reuters Straumann dental implant growth",),
        "Dental implant growth is aligned when procedure and sales growth persist, but VBP price control is a hard gate.",
    ),
    Round73CaseCandidate(
        "lilly_foundayo_fda_approval_case",
        "OBESITY_GLP1_COMMERCIALIZATION",
        "LLY",
        "Lilly oral GLP-1 Foundayo FDA approval",
        "US",
        "success_candidate",
        None,
        date(2026, 4, 1),
        None,
        None,
        None,
        ("fda_approval", "oral_glp1", "trial_weight_loss", "launch_price"),
        ("coverage_unverified", "weekly_scripts_unverified", "competition", "price_pressure"),
        "approval_stage2_not_green",
        "needs_price_backfill",
        ("round_73.md Reuters Lilly oral GLP-1 approval",),
        "Approval and TAM support Stage 1/2; scripts, coverage, supply, price, and OP/EPS decide higher stages.",
    ),
    Round73CaseCandidate(
        "lilly_foundayo_prescription_uptake_case",
        "OBESITY_GLP1_COMMERCIALIZATION",
        "LLY",
        "Lilly Foundayo prescription uptake watch",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 8),
        None,
        None,
        None,
        ("weekly_scripts", "sales_consensus_gap", "oral_glp1"),
        ("slow_uptake", "coverage_unverified", "consensus_gap", "competition"),
        "approval_without_uptake_watch",
        "needs_price_backfill",
        ("round_73.md Reuters Foundayo scripts uptake",),
        "Early scripts were modest; this is exactly why approval and market size cannot create Green alone.",
    ),
    Round73CaseCandidate(
        "lilly_foundayo_switch_maintenance_case",
        "OBESITY_GLP1_COMMERCIALIZATION",
        "LLY",
        "Lilly Foundayo switch-maintenance therapy data",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 12),
        None,
        None,
        None,
        ("maintenance_therapy_data", "weight_maintenance", "oral_glp1", "long_term_use_case"),
        ("coverage_unverified", "price_pressure", "competition", "scripts_needed"),
        "glp1_maintenance_structural_candidate",
        "needs_price_backfill",
        ("round_73.md Reuters Foundayo switch maintenance",),
        "Maintenance evidence can support a more durable GLP-1 path, but insurance, price, and scripts still gate Green.",
    ),
    Round73CaseCandidate(
        "boehringer_goodrx_humira_biosimilar_case",
        "BIOSIMILAR_COMMERCIALIZATION",
        "BIOSIMILAR_ACCESS_REF",
        "Boehringer / GoodRx Humira biosimilar access but uptake watch",
        "US",
        "success_candidate",
        None,
        date(2024, 7, 18),
        None,
        None,
        None,
        ("biosimilar_discount_pct", "access_program", "prescription_volume"),
        ("slow_switching", "pbm_incentive_gap", "margin_pressure", "humira_prescription_dominance"),
        "biosimilar_access_candidate_but_slow_uptake",
        "missing_direct_symbol_mapping",
        ("round_73.md Reuters Humira biosimilar GoodRx access",),
        "A 92% discount improves access, but slow prescription switching and margin defense remain core gates.",
    ),
    Round73CaseCandidate(
        "novo_glp1_price_pressure_case",
        "OBESITY_GLP1_COMMERCIALIZATION",
        "NVO",
        "Novo Nordisk GLP-1 price pressure and competition",
        "DK",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 2, 4),
        ("glp1_market_growth", "wegovy_sales_base"),
        ("price_pressure", "competition", "compounded_alternative", "outlook_cut", "sales_profit_decline"),
        "glp1_4b_to_4c",
        "needs_price_backfill",
        ("round_73.md Reuters Novo 2026 outlook warning",),
        "GLP-1 TAM can still break when price, competition, coverage, and scripts hit estimates.",
    ),
    Round73CaseCandidate(
        "hims_branded_glp1_pivot_loss_case",
        "GLP1_TELEHEALTH_CHANNEL",
        "HIMS",
        "Hims branded GLP-1 pivot and unexpected loss",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 12),
        ("telehealth_glp1_channel", "branded_drug_pivot"),
        ("revenue_miss", "unexpected_loss", "restructuring_cost", "revenue_recognition_timing", "margin_pressure"),
        "telehealth_channel_volatility",
        "needs_price_backfill",
        ("round_73.md Reuters Hims GLP-1 revenue miss",),
        "Telehealth GLP-1 channel stories require legal channel, CAC, margin, revenue recognition, and FCF checks.",
        (E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION, E2RArchetype.PHARMA_CHANNEL_AND_PRIVACY_RISK),
    ),
    Round73CaseCandidate(
        "hims_novo_partnership_case",
        "GLP1_TELEHEALTH_CHANNEL",
        "HIMS",
        "Hims Novo partnership GLP-1 event premium",
        "US",
        "event_premium",
        None,
        date(2026, 3, 9),
        None,
        None,
        None,
        ("novo_partnership", "branded_glp1_channel", "event_price_reaction"),
        ("event_premium", "margin_unverified", "regulatory_dependency", "telehealth_channel_volatility"),
        "telehealth_channel_event_premium",
        "needs_price_backfill",
        ("round_73.md Reuters Hims Novo partnership",),
        "Partnership news can move price, but it is not stable commercialization evidence without channel economics.",
        (E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION, E2RArchetype.PHARMA_CHANNEL_AND_PRIVACY_RISK),
    ),
    Round73CaseCandidate(
        "hims_compounded_glp1_crackdown_case",
        "PHARMA_CHANNEL_AND_PRIVACY_RISK",
        "HIMS",
        "Hims compounded GLP-1 regulatory crackdown",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 2, 7),
        ("compounded_glp1_channel", "online_pharmacy"),
        ("fda_ftc_scrutiny", "illegal_copycat_drug", "compounded_quality_issue", "doj_referral_risk", "channel_shutdown"),
        "compounded_glp1_regulatory_4c_watch",
        "needs_price_backfill",
        ("round_73.md Reuters Hims compounded GLP-1 crackdown",),
        "Large obesity demand does not offset an unproven or illegal drug-channel risk.",
        (E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION,),
    ),
    Round73CaseCandidate(
        "bluebird_gene_therapy_cash_crunch_case",
        "GENE_THERAPY_RARE_DISEASE",
        "BLUE",
        "bluebird bio gene therapy cash crunch",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 2, 21),
        ("approved_gene_therapies",),
        ("cash_crunch", "slow_uptake", "discounted_take_private", "going_concern", "commercialization_failure"),
        "gene_therapy_cash_crunch",
        "needs_price_backfill",
        ("round_73.md Reuters bluebird bio take-private cash crunch",),
        "Approved gene therapies still fail E2R if uptake, reimbursement, and cash runway do not support FCF.",
    ),
    Round73CaseCandidate(
        "charles_river_cro_funding_crunch_case",
        "CRO_CLINICAL_SERVICE",
        "CRL",
        "Charles River CRO funding crunch",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 8, 7),
        ("cro_service_revenue",),
        ("biotech_funding_crunch", "forecast_cut", "revenue_decline", "customer_budget_cut"),
        "cro_funding_cycle_4c_watch",
        "needs_price_backfill",
        ("round_73.md Reuters Charles River forecast cut",),
        "CRO is service revenue, but funding-cycle cuts can break backlog and forecast visibility.",
    ),
    Round73CaseCandidate(
        "teladoc_betterhelp_impairment_case",
        "TELEHEALTH_BEHAVIORAL_HEALTH",
        "TDOC",
        "Teladoc BetterHelp impairment and DTC unit economics failure",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 8, 1),
        ("telehealth_usage", "behavioral_health_platform"),
        ("impairment_charge", "forecast_withdrawal", "advertising_cost_increase", "cac_spike", "revenue_slowdown"),
        "telehealth_dtc_failure_4c",
        "needs_price_backfill",
        ("round_73.md Reuters Teladoc record low",),
        "Telehealth demand is not enough when CAC, impairment, churn, privacy, and FCF are weak.",
    ),
    Round73CaseCandidate(
        "recursion_exscientia_ai_drug_case",
        "AI_DRUG_DISCOVERY_PLATFORM",
        "RXRX",
        "Recursion Exscientia AI drug discovery platform merger",
        "US",
        "success_candidate",
        None,
        date(2024, 8, 8),
        None,
        None,
        None,
        ("ai_drug_discovery_platform", "pipeline_combination", "cash_runway", "candidate_molecules"),
        ("no_approved_drug", "clinical_validation_unproven", "cash_burn", "platform_hype"),
        "ai_drug_platform_watch",
        "needs_price_backfill",
        ("round_73.md Reuters Recursion Exscientia merger",),
        "AI drug-discovery consolidation is Watch until milestones, clinical proof, and commercial economics appear.",
    ),
    Round73CaseCandidate(
        "lunit_dbt_subgroup_validation_case",
        "DIGITAL_HEALTHCARE_AI",
        "328130",
        "Lunit DBT external validation and subgroup risk",
        "KR",
        "success_candidate",
        None,
        date(2025, 3, 17),
        None,
        None,
        None,
        ("external_validation", "ai_model_auc", "clinical_ai_paper", "subgroup_performance_risk"),
        ("subgroup_performance_risk", "no_reimbursement_verified", "hospital_adoption_unverified", "liability_risk"),
        "ai_clinical_validation_not_commercial",
        "needs_price_backfill",
        ("round_73.md arXiv Lunit DBT subgroup performance",),
        "AUC and external validation support Stage 1/2, but reimbursement, hospital workflow, and recurring revenue are separate gates.",
    ),
    Round73CaseCandidate(
        "amgen_samsung_bioepis_biosimilar_litigation_case",
        "BIOSIMILAR_COMMERCIALIZATION",
        "BIOSIMILAR_LITIGATION_REF",
        "Amgen / Samsung Bioepis biosimilar patent litigation risk",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 8, 13),
        ("biosimilar_application", "patent_litigation", "launch_timing_risk"),
        ("patent_litigation", "launch_delay", "pbm_exclusion", "price_competition", "margin_compression"),
        "biosimilar_patent_litigation_4c_watch",
        "missing_direct_symbol_mapping",
        ("round_73.md Reuters Amgen Samsung Bioepis patent litigation",),
        "Biosimilar approval or filing is not enough when patent litigation can delay launch and damage economics.",
        (E2RArchetype.REIMBURSEMENT_ACCESS_OVERLAY,),
    ),
    Round73CaseCandidate(
        "botox_counterfeit_fda_warning_case",
        "DEVICE_SAFETY_COUNTERFEIT_OVERLAY",
        "BOTOX_SAFETY_REF",
        "FDA counterfeit Botox safety warning",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 11, 5),
        ("aesthetic_procedure_demand",),
        ("counterfeit_product", "unapproved_product", "injury_report", "licensed_channel_failure"),
        "device_safety_regulatory_4c",
        "missing_direct_symbol_mapping",
        ("round_73.md AP FDA unapproved Botox warning",),
        "Aesthetic demand cannot offset counterfeit, unapproved-product, and safety-channel risks.",
        (E2RArchetype.BOTULINUM_AESTHETIC_REGULATED,),
    ),
)


ROUND73_PRICE_FIELDS: tuple[str, ...] = (
    "case_id",
    "symbol",
    "company_name",
    "primary_archetype",
    "secondary_archetypes",
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
    "peak_price",
    "peak_date",
    "MFE_30D",
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_30D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "drawdown_after_peak",
    "below_stage2_price_flag",
    "below_stage3_price_flag",
    "contract_value",
    "contract_duration",
    "capacity_liters",
    "capacity_utilization",
    "us_operating_cost",
    "capex_amount",
    "backlog_growth",
    "customer_concentration",
    "op_margin_change",
    "fcf_margin",
    "prescription_volume",
    "weekly_scripts",
    "insurance_coverage",
    "pbm_listing_flag",
    "biosimilar_discount_pct",
    "prescription_conversion_rate",
    "drug_price_change",
    "monthly_price",
    "gross_to_net_discount",
    "script_growth_rate",
    "coverage_gap_flag",
    "pbm_exclusion_flag",
    "patent_litigation_flag",
    "launch_delay_flag",
    "compounded_alternative_flag",
    "branded_drug_attach_rate",
    "legal_settlement_flag",
    "revenue_recognition_issue_flag",
    "clinical_trial_phase",
    "approval_status",
    "patient_uptake",
    "reimbursement_status",
    "cash_runway_months",
    "going_concern_flag",
    "dilution_or_take_private_flag",
    "hospital_adoption_count",
    "reimbursement_code_flag",
    "paid_workflow_flag",
    "recurring_revenue_ratio",
    "ai_model_auc",
    "subgroup_performance_risk",
    "liability_risk_flag",
    "device_export_country_count",
    "installed_base",
    "system_placement_count",
    "procedure_volume",
    "procedure_growth_rate",
    "instruments_accessories_revenue",
    "consumable_revenue_ratio",
    "hospital_capex_cycle_flag",
    "procedure_mix_risk_flag",
    "glp1_bariatric_slowdown_flag",
    "vbp_price_control_flag",
    "asp_drop_flag",
    "counterfeit_safety_flag",
    "unapproved_product_flag",
    "fda_ftc_scrutiny_flag",
    "compounded_quality_issue_flag",
    "doj_referral_risk_flag",
    "cac",
    "churn",
    "privacy_incident_flag",
    "impairment_charge",
    "forecast_withdrawal_flag",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def target_for(target_id: str) -> Round73ScoreTarget | None:
    for target in ROUND73_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round73_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND73_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
        stage4b_evidence = candidate.evidence_fields if candidate.case_type == "4b_watch" or candidate.stage4b_date else ()
        stage4c_evidence = candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" or candidate.stage4c_date else ()
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market=candidate.market,
            sector_raw=candidate.target_id,
            primary_archetype=target.canonical_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=target.large_sector.value,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                f"Round73 R7 Loop-3 case for {candidate.target_id}; "
                "approval, AI, capacity, telehealth, and device narratives are separated from commercialization evidence."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage2_signals or field in target.green_conditions),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage3_conditions),
            stage4b_evidence=stage4b_evidence,
            stage4c_evidence=stage4c_evidence,
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"failed_rerating", "event_premium", "overheat", "4b_watch", "4c_thesis_break", "one_off"}
                else None
            ),
            score_price_alignment=_score_price_alignment(candidate),
            rerating_result=_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint=_score_weight_hint(target),
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_cross_evidence_for_green",
                "approval_or_clinical_news_is_not_revenue",
                "paper_auc_or_ai_label_is_not_green_evidence_alone",
                "commercialization_reimbursement_fcf_required_for_green",
                "capacity_without_utilization_is_not_stage3",
                "glp1_tam_is_not_green_without_scripts_coverage_price_and_eps",
                "do_not_invent_prescriptions_reimbursement_capacity_uptake_cash_runway_hospital_adoption_or_stage_prices",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.75 if candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.2,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round73_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND73_SCORE_TARGETS:
        weights = target.score_weight.as_dict()
        rows.append(
            {
                "target_id": target.target_id,
                "large_sector": target.large_sector.value,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "eps_fcf": str(weights["eps_fcf"]),
                "structural_visibility": str(weights["structural_visibility"]),
                "bottleneck_pricing": str(weights["bottleneck_pricing"]),
                "market_mispricing": str(weights["market_mispricing"]),
                "valuation": str(weights["valuation"]),
                "capital_allocation": str(weights["capital_allocation"]),
                "information_confidence": str(weights["information_confidence"]),
                "stage1_signals": "|".join(target.stage1_signals),
                "stage2_signals": "|".join(target.stage2_signals),
                "stage3_conditions": "|".join(target.stage3_conditions),
                "stage4b_conditions": "|".join(target.stage4b_conditions),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "loop3_penalty_axes": "|".join(target.loop3_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round73_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND73_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        assert target is not None
        rows.append(
            {
                "case_id": candidate.case_id,
                "target_id": candidate.target_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "market": candidate.market,
                "case_type": candidate.case_type,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "stage1_date": candidate.stage1_date.isoformat() if candidate.stage1_date else "",
                "stage2_date": candidate.stage2_date.isoformat() if candidate.stage2_date else "",
                "stage3_date": candidate.stage3_date.isoformat() if candidate.stage3_date else "",
                "stage4b_date": candidate.stage4b_date.isoformat() if candidate.stage4b_date else "",
                "stage4c_date": candidate.stage4c_date.isoformat() if candidate.stage4c_date else "",
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "alignment_hint": candidate.alignment_hint,
                "price_validation_status": candidate.price_validation_status,
                "production_input": "false",
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round73_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "red_flags": "|".join(target.red_flags),
            "loop3_penalty_axes": "|".join(target.loop3_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND73_SCORE_TARGETS
    )


def round73_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round73_backfill": "true"} for field in ROUND73_PRICE_FIELDS)


def round73_summary() -> dict[str, int | bool]:
    records = round73_case_records()
    return {
        "target_count": len(ROUND73_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND73_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND73_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND73_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND73_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round73_r7_loop3_reports(
    *,
    output_directory: str | Path = ROUND73_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND73_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND73_DEFAULT_SCORE_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = Path(cases_path)
    score_profiles = Path(score_profile_path)
    cases.parent.mkdir(parents=True, exist_ok=True)
    score_profiles.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "score_profiles": score_profiles,
        "summary": output / "round73_r7_loop3_biotech_healthcare_device_summary.md",
        "case_matrix": output / "round73_r7_loop3_case_matrix.csv",
        "stage_date_plan": output / "round73_r7_loop3_stage_date_plan.csv",
        "green_guardrails": output / "round73_r7_loop3_green_guardrails.md",
        "risk_overlays": output / "round73_r7_loop3_risk_overlays.md",
        "price_validation_plan": output / "round73_r7_loop3_price_validation_plan.md",
        "price_fields": output / "round73_r7_loop3_price_fields.csv",
    }
    _write_case_jsonl(round73_case_records(), cases)
    _write_rows(round73_score_profile_rows(), score_profiles)
    _write_rows(round73_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round73_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round73_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round73_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round73_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round73_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round73_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round73_summary_markdown() -> str:
    summary = round73_summary()
    lines = [
        "# Round-73 R7 Loop-3 Biotech / Healthcare / Medical Device Summary",
        "",
        f"- source_round: `{ROUND73_SOURCE_ROUND_PATH}`",
        "- large_sector: `BIOTECH_HEALTHCARE_DEVICE`",
        "- loop: `R7 Loop 3 / v3.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        f"- gate_only_target_count: {summary['gate_only_target_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R7 Loop 3 says approval, clinical success, AI papers, and TAM are not commercialization by themselves.",
        "- Example: CDMO capacity is useful, but utilization, customer contracts, OPM, and FCF decide Stage 3 review.",
        "- Example: GLP-1 approval is Stage 1/2; weekly scripts, insurance, price defense, and OP/EPS must follow.",
        "- Example: medical AI AUC supports research quality, but hospital adoption, reimbursement, and recurring revenue decide higher stages.",
        "- Example: gene therapy approval can still become 4C if uptake, reimbursement, and cash runway fail.",
    ]
    return "\n".join(lines) + "\n"


def render_round73_green_guardrail_markdown() -> str:
    lines = [
        "# Round-73 R7 Loop-3 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-3 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND73_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.loop3_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R7 Loop-3 v3.0 weights to production scoring yet.",
            "- Do not treat FDA/EMA approval, clinical success, AI model AUC, external-validation paper, pilot, user growth, or disease-event demand as Green evidence by itself.",
            "- Do not invent prescription volume, PBM/insurance coverage, reimbursement, capacity utilization, patient uptake, hospital adoption, procedure volume, consumable revenue, cash runway, CAC, churn, or stage prices.",
            "- Green requires commercialization, reimbursement, recurring revenue, FCF conversion, contracted utilization, or repeated procedure/consumable evidence.",
            "- Treat slow uptake, cash crunch, dilution, take-private, forecast cut, FDA/FTC scrutiny, privacy breach, impairment, counterfeit product, safety issue, price control, and one-off diagnostic normalization as RedTeam evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round73_risk_overlay_markdown() -> str:
    lines = [
        "# Round-73 R7 Loop-3 Risk Overlays",
        "",
        "- `COMMERCIALIZATION_ALIGNED`: approval/contract is followed by prescriptions, revenue, OPM, FCF, or price-path confirmation.",
        "- `APPROVAL_WITHOUT_UPTAKE`: approval exists, but prescription, reimbursement, patient uptake, or sales are weak.",
        "- `CAPACITY_WITHOUT_UTILIZATION`: CDMO/device capacity exists, but utilization and customer contracts are unverified.",
        "- `GLP1_APPROVAL_BUT_SCRIPT_GATE`: GLP-1 approval exists, but weekly scripts, coverage, and price defense are not yet proven.",
        "- `GLP1_4B_TO_4C`: obesity-market narrative breaks through price, competition, coverage, or compounded-drug pressure.",
        "- `TELEHEALTH_CHANNEL_VOLATILITY`: telehealth partnership, compounded drug, branded pivot, CAC, or revenue recognition drives unstable price action.",
        "- `AI_CLINICAL_VALIDATION_NOT_COMMERCIAL`: AI paper or AUC is strong, but deployment, reimbursement, and recurring revenue are missing.",
        "- `GENE_THERAPY_CASH_CRUNCH`: approved therapy fails because uptake, reimbursement, and cash runway break.",
        "- `DEVICE_SAFETY_REGULATORY_4C`: device, Botox, implant, counterfeit, VBP, or safety risk blocks unsafe Green.",
        "- `SURGICAL_ROBOT_RECURRING_CONSUMABLE_SUCCESS`: installed base, procedure growth, and instruments/accessories revenue move together.",
        "",
        "Simple example: `FDA 허가` is useful Stage 1/2 evidence. It is not Green if scripts, coverage, revenue, and FCF are still missing.",
    ]
    return "\n".join(lines) + "\n"


def render_round73_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-73 R7 Loop-3 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare capacity, utilization, prescriptions, PBM/insurance, reimbursement, patient uptake, hospital adoption, procedure volume, consumables, cash runway, CAC, churn, safety, and regulatory events with price path.",
        "6. Mark capacity-without-utilization, approval-without-uptake, GLP-1 4B-to-4C, telehealth volatility, AI validation-not-commercial, gene-therapy cash crunch, and device safety 4C explicitly.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round73_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `COMMERCIALIZATION_ALIGNED`: commercialization, utilization, prescriptions, procedures, reimbursement, or FCF moves with price rerating.",
            "- `APPROVAL_WITHOUT_UPTAKE`: approval exists but patient uptake, reimbursement, prescriptions, or sales are missing.",
            "- `CAPACITY_WITHOUT_UTILIZATION`: capacity/site expansion exists, but contract and utilization are still missing.",
            "- `GLP1_APPROVAL_BUT_SCRIPT_GATE`: approval is useful, but weekly scripts, insurance, price defense, and OP/EPS still gate Green.",
            "- `GLP1_4B_TO_4C`: price/competition/coverage/compounded-drug pressure breaks a GLP-1 narrative.",
            "- `TELEHEALTH_CHANNEL_VOLATILITY`: partnership or channel change creates price action without durable economics.",
            "- `AI_CLINICAL_VALIDATION_NOT_COMMERCIAL`: paper/AUC validates model quality but not paid deployment.",
            "- `GENE_THERAPY_CASH_CRUNCH`: approval fails to convert into cash-flow-safe commercialization.",
            "- `DEVICE_SAFETY_REGULATORY_4C`: counterfeit, VBP, safety, or unapproved-channel risk blocks Green.",
            "- `SURGICAL_ROBOT_RECURRING_CONSUMABLE_SUCCESS`: installed base, procedure growth, and consumable revenue validate recurring medtech economics.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round73CaseCandidate) -> str:
    if candidate.case_type == "event_premium":
        return "price_moved_without_evidence"
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    if candidate.case_type == "structural_success":
        return "aligned"
    if candidate.case_type == "success_candidate" and "aligned" in candidate.alignment_hint:
        return "aligned"
    if candidate.case_type == "success_candidate" and "structural_candidate" in candidate.alignment_hint:
        return "aligned"
    return "unknown"


def _rerating_result(candidate: Round73CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "event_premium":
        return "event_premium"
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "theme_overheat"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "failed_rerating":
        return "no_rerating"
    return "unknown"


def _score_weight_hint(target: Round73ScoreTarget) -> dict[str, float]:
    weights = target.score_weight.as_dict()
    return {
        "eps_fcf": _numeric_weight(weights["eps_fcf"]),
        "visibility": _numeric_weight(weights["structural_visibility"]),
        "bottleneck": _numeric_weight(weights["bottleneck_pricing"]),
        "mispricing": _numeric_weight(weights["market_mispricing"]),
        "valuation": _numeric_weight(weights["valuation"]),
        "capital_allocation": _numeric_weight(weights["capital_allocation"]),
    }


def _numeric_weight(value: int | str) -> float:
    if isinstance(value, int):
        return float(value)
    return 0.0


def _write_case_jsonl(records: Iterable[E2RCaseRecord], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(record.as_dict(), ensure_ascii=False, sort_keys=True) for record in records]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return path


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    rows_tuple = tuple(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows_tuple[0].keys()))
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow(dict(row))
    return path


__all__ = [
    "ROUND73_CASE_CANDIDATES",
    "ROUND73_DEFAULT_CASES_PATH",
    "ROUND73_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND73_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND73_PRICE_FIELDS",
    "ROUND73_SCORE_TARGETS",
    "Round73CaseCandidate",
    "Round73ScoreTarget",
    "Round73ScoreWeightDraft",
    "render_round73_green_guardrail_markdown",
    "render_round73_price_validation_plan_markdown",
    "render_round73_risk_overlay_markdown",
    "render_round73_summary_markdown",
    "round73_case_candidate_rows",
    "round73_case_records",
    "round73_price_field_rows",
    "round73_score_profile_rows",
    "round73_stage_date_rows",
    "round73_summary",
    "target_for",
    "write_round73_r7_loop3_reports",
]
