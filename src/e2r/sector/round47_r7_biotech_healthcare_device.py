"""Round-47 R7 biotech, healthcare, and medical-device calibration pack.

Round 47 separates scoreable healthcare business models from clinical,
approval, AI, and one-off demand headlines. CDMO and medical-device exports can
be Green-eligible when contracts, utilization, procedures, consumables, and FCF
are visible. Pre-revenue biotech, AI drug-discovery platforms, infectious
diagnostics, and telehealth stories remain Watch/Red until commercialization,
reimbursement, unit economics, and cash runway are proven.

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


ROUND47_SOURCE_ROUND_PATH = "docs/round/round_47.md"
ROUND47_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round47_r7_biotech_healthcare_device"
ROUND47_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r7_round47.jsonl"
ROUND47_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round47_r7_v1.csv"


@dataclass(frozen=True)
class Round47ScoreWeightDraft:
    eps_fcf: int
    structural_visibility: int
    bottleneck_pricing: int
    market_mispricing: int
    valuation: int
    capital_allocation: int
    information_confidence: int

    def as_dict(self) -> dict[str, int]:
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
class Round47ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round47ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    normalization_point: str

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.BIOTECH_HEALTHCARE_DEVICE

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round47CaseCandidate:
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


ROUND47_SCORE_TARGETS: tuple[Round47ScoreTarget, ...] = (
    Round47ScoreTarget(
        "CDMO_HEALTHCARE_CONTRACT",
        E2RArchetype.CDMO_HEALTHCARE_CONTRACT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round47ScoreWeightDraft(20, 24, 12, 12, 12, 0, 5),
        ("cdmo_contract", "capacity_expansion", "new_manufacturing_site"),
        ("long_term_contract", "capacity_utilization", "customer_diversification", "op_eps_revision"),
        ("multi_year_production_visibility", "fcf_conversion", "utilization_leverage"),
        ("capacity_premium_overheated", "capex_story_priced_before_utilization"),
        ("utilization_down", "contract_delay", "capex_burden", "tariff_or_quality_issue"),
        ("long_term_contract", "capacity_utilization", "customer_diversification", "fcf_conversion"),
        ("underutilization", "customer_concentration", "capex_burden", "quality_issue", "tariff"),
        "CDMO is production-contract scoring, not clinical-news scoring.",
    ),
    Round47ScoreTarget(
        "CRO_CLINICAL_SERVICE",
        E2RArchetype.CRO_CLINICAL_SERVICE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round47ScoreWeightDraft(18, 20, 8, 12, 12, 0, 5),
        ("clinical_service_backlog", "pharma_rd_budget", "trial_volume_growth"),
        ("service_revenue_growth", "customer_diversification", "repeat_service_revenue"),
        ("multi_year_backlog", "funding_cycle_stable", "high_fcf_conversion"),
        ("cro_recovery_expectation_overheated",),
        ("biotech_funding_crunch", "customer_rd_budget_cut", "forecast_cut", "order_cancellation"),
        ("service_backlog", "customer_diversification", "repeat_service_revenue", "opm_improvement"),
        ("biotech_funding_cycle_down", "customer_budget_cut", "trial_delay", "low_margin_backlog"),
        "CRO is more scoreable than pre-revenue biotech, but funding-cycle exposure caps Green.",
    ),
    Round47ScoreTarget(
        "BIOSIMILAR_COMMERCIALIZATION",
        E2RArchetype.BIOSIMILAR_COMMERCIALIZATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round47ScoreWeightDraft(18, 20, 6, 13, 11, 0, 6),
        ("fda_ema_approval", "patent_expiry", "biosimilar_launch"),
        ("pbm_listing", "insurance_coverage", "prescription_conversion", "launch_revenue"),
        ("prescription_growth", "margin_defense", "multi_country_launch"),
        ("approval_news_overheated", "biosimilar_launch_crowded"),
        ("price_competition", "prescription_conversion_delay", "margin_collapse"),
        ("pbm_listing", "insurance_coverage", "prescription_conversion", "revenue_conversion"),
        ("price_competition", "coverage_gap", "slow_switching", "margin_pressure"),
        "Biosimilar approval is Stage 1; prescription, coverage, and margin decide Stage 2/3.",
    ),
    Round47ScoreTarget(
        "BIOSIMILAR_ORIGINATOR_DEFENSE",
        E2RArchetype.BIOSIMILAR_ORIGINATOR_DEFENSE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round47ScoreWeightDraft(19, 18, 8, 13, 11, 2, 6),
        ("patent_cliff", "originator_defense", "pipeline_replacement"),
        ("pipeline_revenue_offset", "price_defense", "capital_allocation"),
        ("defended_revenue_base", "new_product_offset", "margin_protection"),
        ("defense_narrative_overpriced",),
        ("patent_cliff", "pipeline_failure", "pricing_pressure", "share_loss"),
        ("pipeline_revenue_offset", "price_defense", "margin_protection"),
        ("patent_cliff", "pipeline_failure", "share_loss", "pricing_pressure"),
        "Originator defense needs actual revenue offset, not litigation or patent language alone.",
    ),
    Round47ScoreTarget(
        "OBESITY_GLP1_COMMERCIALIZATION",
        E2RArchetype.OBESITY_GLP1_COMMERCIALIZATION,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round47ScoreWeightDraft(22, 20, 12, 13, 12, 0, 6),
        ("glp1_approval", "oral_glp1_trial", "prescription_growth"),
        ("weekly_scripts", "insurance_coverage", "supply_capacity", "sales_ramp"),
        ("durable_prescription_growth", "price_defense", "op_eps_revision", "coverage_expansion"),
        ("obesity_market_narrative_crowded", "scripts_lag_valuation"),
        ("compounded_alternative", "price_cut", "coverage_denial", "prescription_slowdown"),
        ("prescription_volume", "insurance_coverage", "supply_capacity", "price_defense", "op_eps_revision"),
        ("competition", "compounded_alternative", "coverage_gap", "price_regulation", "slow_uptake"),
        "GLP-1 can be Green, but only with prescriptions, coverage, price defense, and OP/EPS support.",
    ),
    Round47ScoreTarget(
        "GENE_THERAPY_RARE_DISEASE",
        E2RArchetype.GENE_THERAPY_RARE_DISEASE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round47ScoreWeightDraft(8, 12, 8, 10, 6, 0, 5),
        ("gene_therapy_approval", "rare_disease_unmet_need", "patient_recruitment"),
        ("treated_patients", "reimbursement", "commercial_sales", "cash_runway"),
        ("repeat_commercial_uptake", "dilution_risk_controlled", "pipeline_revenue"),
        ("approval_news_overheated", "rare_disease_story_crowded"),
        ("slow_uptake", "cash_crunch", "going_concern", "discounted_take_private", "dilution"),
        ("patient_uptake", "reimbursement", "cash_runway", "commercial_revenue"),
        ("cash_burn", "reimbursement_failure", "slow_uptake", "dilution", "going_concern"),
        "Approval without commercial uptake and cash runway is not Green.",
    ),
    Round47ScoreTarget(
        "AI_DRUG_DISCOVERY_PLATFORM",
        E2RArchetype.AI_DRUG_DISCOVERY_PLATFORM,
        Round10ThemePosture.REDTEAM_FIRST,
        Round47ScoreWeightDraft(6, 10, 7, 12, 6, 0, 5),
        ("ai_drug_discovery_platform", "candidate_molecule", "platform_partnership"),
        ("big_pharma_milestone", "clinical_entry", "cash_runway"),
        ("validated_pipeline", "partner_funded_progress", "commercial_or_royalty_path"),
        ("ai_drug_platform_overheated", "poc_story_crowded"),
        ("clinical_failure", "cash_burn", "platform_hype_unwind", "no_approved_drug"),
        ("big_pharma_partnership", "clinical_progress", "cash_runway", "milestone_revenue"),
        ("no_approved_drug", "cash_burn", "clinical_failure", "platform_hype"),
        "AI drug-discovery labels are not score evidence without milestones, clinical progress, and cash runway.",
    ),
    Round47ScoreTarget(
        "DIGITAL_HEALTHCARE_AI",
        E2RArchetype.DIGITAL_HEALTHCARE_AI,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round47ScoreWeightDraft(18, 17, 8, 13, 12, 0, 7),
        ("clinical_ai_paper", "external_validation", "hospital_pilot", "regulatory_clearance"),
        ("hospital_adoption", "reimbursement", "paid_workflow", "recurring_revenue"),
        ("workflow_embedded", "recurring_revenue", "op_improvement", "liability_risk_low"),
        ("medical_ai_narrative_overheated", "paper_only_valuation_premium"),
        ("subgroup_performance_issue", "reimbursement_denial", "liability_event", "hospital_adoption_failure"),
        ("external_validation", "hospital_adoption", "reimbursement_or_paid_usage", "recurring_revenue"),
        ("subgroup_bias", "no_reimbursement", "liability", "poc_only", "date_unverified"),
        "Medical AI papers lift Stage 1/2, but Green requires paid adoption and reimbursement.",
    ),
    Round47ScoreTarget(
        "DIGITAL_HEALTHCARE_REMOTE_MEDICINE",
        E2RArchetype.DIGITAL_HEALTHCARE_REMOTE_MEDICINE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round47ScoreWeightDraft(18, 18, 8, 13, 12, 1, 6),
        ("remote_medicine_policy", "wearable_or_emr_integration", "digital_health_platform"),
        ("hospital_or_insurer_contract", "b2b_b2b2c_contract", "recurring_subscription", "unit_economics"),
        ("embedded_workflow", "reimbursement_visible", "repeat_usage", "opm_improvement"),
        ("telehealth_theme_crowded",),
        ("regulatory_reversal", "reimbursement_failure", "privacy_incident", "unit_economics_failure"),
        ("hospital_or_insurer_contract", "recurring_revenue", "unit_economics", "regulatory_clearance"),
        ("regulation", "privacy", "reimbursement", "cac", "churn"),
        "Remote medicine needs contracts, reimbursement, and unit economics, not usage story alone.",
    ),
    Round47ScoreTarget(
        "TELEHEALTH_BEHAVIORAL_HEALTH",
        E2RArchetype.TELEHEALTH_BEHAVIORAL_HEALTH,
        Round10ThemePosture.REDTEAM_FIRST,
        Round47ScoreWeightDraft(17, 16, 6, 12, 10, 0, 6),
        ("online_behavioral_health_demand", "subscriber_growth", "dtc_health_platform"),
        ("employer_or_insurer_contract", "cac_stable", "repeat_usage"),
        ("low_churn_contract_revenue", "fcf_margin", "privacy_clean"),
        ("dtc_telehealth_growth_crowded",),
        ("cac_spike", "privacy_incident", "impairment", "forecast_withdrawal", "churn"),
        ("employer_or_insurer_contract", "cac_stable", "churn_stable", "fcf_margin"),
        ("cac", "privacy", "impairment", "forecast_withdrawal", "churn"),
        "DTC telehealth is RedTeam-first unless contract revenue and unit economics are clear.",
    ),
    Round47ScoreTarget(
        "PHARMA_CHANNEL_AND_PRIVACY_RISK",
        E2RArchetype.PHARMA_CHANNEL_AND_PRIVACY_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        Round47ScoreWeightDraft(16, 15, 6, 12, 10, 0, 6),
        ("online_pharmacy", "compounded_drug_channel", "health_data_platform"),
        ("legal_prescription_channel", "gross_margin", "subscriber_revenue"),
        ("regulated_repeat_channel", "privacy_clean", "fcf_visible"),
        ("online_drug_channel_crowded",),
        ("fda_ftc_scrutiny", "compounded_quality_issue", "privacy_breach", "margin_collapse"),
        ("legal_prescription_channel", "gross_margin", "privacy_clean", "fcf_visible"),
        ("regulatory_scrutiny", "privacy", "quality_issue", "margin_pressure"),
        "Drug-channel platforms need legal channel, margin, privacy, and FCF proof before scoring strength.",
    ),
    Round47ScoreTarget(
        "MEDICAL_DEVICE_HEALTHCARE_EXPORT",
        E2RArchetype.MEDICAL_DEVICE_HEALTHCARE_EXPORT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round47ScoreWeightDraft(20, 22, 13, 14, 12, 0, 5),
        ("medical_device_export", "new_approval", "procedure_growth"),
        ("export_country_expansion", "recurring_procedure", "consumable_revenue", "opm_roe_improvement"),
        ("repeat_procedure_demand", "asp_stable", "fcf_improvement", "channel_quality"),
        ("device_premium_crowded", "target_multiple_saturated"),
        ("approval_delay", "safety_issue", "price_control", "channel_failure", "single_device_no_consumable"),
        ("export_growth", "consumable_repeat_revenue", "regulatory_approval", "opm_roe_improvement"),
        ("approval_delay", "safety", "competition", "channel_quality", "single_device_no_consumable"),
        "Medical-device Green needs repeat procedures, consumables, approvals, and export/channel proof.",
    ),
    Round47ScoreTarget(
        "MEDICAL_DEVICE_DENTAL_IMPLANT",
        E2RArchetype.MEDICAL_DEVICE_DENTAL_IMPLANT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round47ScoreWeightDraft(20, 22, 13, 14, 12, 0, 5),
        ("dental_implant_growth", "procedure_growth", "approval_or_channel"),
        ("export_country_expansion", "recurring_procedure_consumable", "opm_roe_improvement"),
        ("approval_stable", "repeat_consumable_revenue", "pricing_pressure_low", "channel_quality"),
        ("implant_premium_crowded", "vbp_risk_ignored"),
        ("vbp_price_control", "asp_drop", "approval_delay", "safety_issue", "competition"),
        ("recurring_procedure_consumable", "approval_stable", "opm_roe_improvement", "channel_quality"),
        ("vbp_price_control", "approval", "safety", "competition", "asp_drop"),
        "Dental implant Green is possible, but VBP and ASP compression are hard risk gates.",
    ),
    Round47ScoreTarget(
        "BOTULINUM_AESTHETIC_REGULATED",
        E2RArchetype.BOTULINUM_AESTHETIC_REGULATED,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round47ScoreWeightDraft(19, 20, 12, 13, 11, 0, 5),
        ("botulinum_toxin_demand", "aesthetic_procedure_growth", "licensed_channel"),
        ("repeat_procedure", "regulatory_approval", "safe_distribution_channel", "op_eps_revision"),
        ("licensed_repeat_procedure", "safety_clean", "export_channel", "fcf_conversion"),
        ("aesthetic_toxin_premium_crowded",),
        ("counterfeit_product", "unapproved_product", "injury_report", "channel_failure", "safety_issue"),
        ("regulatory_approval", "repeat_procedure", "safe_distribution_channel", "op_eps_revision"),
        ("counterfeit", "unapproved_product", "safety", "channel_failure"),
        "Aesthetic toxins are Watch-to-Green only through licensed, safe, repeat-procedure channels.",
    ),
    Round47ScoreTarget(
        "DIAGNOSTICS_INFECTIOUS_DISEASE",
        E2RArchetype.DIAGNOSTICS_INFECTIOUS_DISEASE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round47ScoreWeightDraft(20, 5, 5, 5, 5, 0, 5),
        ("infectious_disease_diagnostic_demand", "pandemic_or_mpox_event", "test_kit_sales_spike"),
        ("recurring_non_event_demand", "installed_base_consumables", "post_event_revenue"),
        ("recurring_platform_revenue", "margin_normalization", "non_event_demand"),
        ("diagnostic_event_extrapolated",),
        ("one_off_demand", "guidance_down", "inventory_build", "demand_cliff"),
        ("recurring_non_event_demand", "post_event_revenue", "margin_normalization"),
        ("one_off_demand", "inventory_build", "guidance_down", "demand_cliff"),
        "Infectious diagnostics are RedTeam-first because event demand can disappear quickly.",
    ),
    Round47ScoreTarget(
        "ANIMAL_HEALTH_BIOSECURITY",
        E2RArchetype.ANIMAL_HEALTH_BIOSECURITY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round47ScoreWeightDraft(16, 14, 8, 10, 8, 0, 5),
        ("animal_vaccine", "biosecurity_policy", "disease_outbreak"),
        ("government_or_farm_contract", "recurring_prevention_revenue", "margin_visibility"),
        ("recurring_biosecurity_demand", "policy_budget", "fcf_visibility"),
        ("outbreak_theme_crowded",),
        ("disease_event_normalization", "policy_budget_cut", "inventory_build", "approval_issue"),
        ("recurring_prevention_revenue", "government_or_farm_contract", "margin_visibility"),
        ("event_normalization", "policy_uncertainty", "approval_issue", "inventory"),
        "Animal health is Watch unless recurring prevention demand survives after the disease event.",
    ),
)


ROUND47_CASE_CANDIDATES: tuple[Round47CaseCandidate, ...] = (
    Round47CaseCandidate(
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
        "strategic_success_candidate_delayed_price_alignment",
        "needs_price_backfill",
        ("Reuters Samsung Biologics GSK US facility",),
        "US manufacturing capacity is strategic, but utilization, customer contracts, CAPEX, and FCF must be verified.",
    ),
    Round47CaseCandidate(
        "samsung_biologics_cdmo_contract_reference",
        "CDMO_HEALTHCARE_CONTRACT",
        "207940",
        "Samsung Biologics large pharma CDMO contract reference",
        "KR",
        "structural_success",
        None,
        None,
        None,
        None,
        None,
        ("major_pharma_contracts", "customer_diversification", "capacity_utilization_to_verify", "op_margin_to_verify"),
        ("customer_concentration", "contract_delay", "quality_issue"),
        "cdmo_structural_reference",
        "needs_source_date_and_price_backfill",
        ("Round47 Samsung Biologics contract reference",),
        "CDMO references are Green-eligible only after contract, utilization, margin, and FCF conversion are matched to stage dates.",
    ),
    Round47CaseCandidate(
        "straumann_dental_implant_growth_case",
        "MEDICAL_DEVICE_DENTAL_IMPLANT",
        "STMN.SW",
        "Straumann dental implant growth case",
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
        ("Reuters Straumann 2026 growth",),
        "Dental implant growth is aligned when procedure and sales growth persist, but VBP price control is a hard gate.",
    ),
    Round47CaseCandidate(
        "botox_counterfeit_fda_warning_case",
        "BOTULINUM_AESTHETIC_REGULATED",
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
        "safety_regulatory_4c_watch",
        "missing_direct_symbol_mapping",
        ("AP FDA unapproved Botox warning",),
        "Aesthetic demand cannot offset counterfeit, unapproved-product, and safety-channel risks.",
    ),
    Round47CaseCandidate(
        "lunit_mammography_ai_subgroup_case",
        "DIGITAL_HEALTHCARE_AI",
        "328130",
        "Lunit mammography AI external validation and subgroup risk",
        "KR",
        "success_candidate",
        None,
        date(2025, 3, 17),
        None,
        None,
        None,
        ("external_validation", "ai_model_auc", "clinical_ai_paper"),
        ("subgroup_performance_risk", "no_reimbursement_verified", "hospital_adoption_unverified"),
        "clinical_validation_candidate_commercialization_unproven",
        "needs_price_backfill",
        ("arXiv Lunit DBT subgroup performance",),
        "AUC and external validation support Stage 1/2, but reimbursement, hospital workflow, and recurring revenue are separate gates.",
    ),
    Round47CaseCandidate(
        "lilly_oral_glp1_foundayo_case",
        "OBESITY_GLP1_COMMERCIALIZATION",
        "LLY",
        "Lilly oral GLP-1 Foundayo uptake watch",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 8),
        None,
        None,
        None,
        ("oral_glp1", "weekly_scripts", "maintenance_therapy", "supply_capacity_to_verify"),
        ("slow_uptake", "coverage_unverified", "consensus_gap", "competition"),
        "high_growth_watch_to_green",
        "needs_price_backfill",
        ("Reuters Lilly obesity pill prescription uptake",),
        "GLP-1 market size is not enough; weekly scripts, coverage, supply, and sales versus consensus must be checked.",
    ),
    Round47CaseCandidate(
        "novo_wegovy_outlook_cut_case",
        "OBESITY_GLP1_COMMERCIALIZATION",
        "NVO",
        "Novo Nordisk Wegovy outlook cut and price pressure",
        "DK",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 5, 7),
        ("glp1_market_growth",),
        ("wegovy_sales_slowdown", "zepbound_competition", "compounded_alternative", "price_pressure", "outlook_cut"),
        "glp1_competition_price_4c_watch",
        "needs_price_backfill",
        ("Reuters Novo Nordisk 2025 outlook cut", "Reuters Novo Nordisk 2026 plunge"),
        "Large GLP-1 markets still break when competition, compounded alternatives, price cuts, and slower scripts hit estimates.",
    ),
    Round47CaseCandidate(
        "hims_glp1_strategy_shift_case",
        "PHARMA_CHANNEL_AND_PRIVACY_RISK",
        "HIMS",
        "Hims & Hers GLP-1 strategy shift and channel economics risk",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 11),
        ("online_pharmacy", "glp1_strategy_shift"),
        ("revenue_miss", "unexpected_loss", "subscriber_revenue_down", "compounded_drug_regulation", "margin_pressure"),
        "channel_regulatory_unit_economics_4c",
        "needs_price_backfill",
        ("Reuters Hims Hers revenue miss",),
        "Online drug-channel stories need legal channel, margin, CAC, subscriber economics, and regulatory proof.",
    ),
    Round47CaseCandidate(
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
        "gene_therapy_commercialization_failure",
        "needs_price_backfill",
        ("Reuters bluebird bio take-private cash crunch",),
        "Approved gene therapies still fail E2R if uptake, reimbursement, and cash runway do not support FCF.",
    ),
    Round47CaseCandidate(
        "bluebird_revised_offer_event_premium_case",
        "GENE_THERAPY_RARE_DISEASE",
        "BLUE",
        "bluebird bio revised take-private offer event premium",
        "US",
        "event_premium",
        None,
        date(2025, 5, 14),
        None,
        None,
        None,
        ("revised_take_private_offer", "event_price_bounce"),
        ("event_premium", "cash_crunch_not_solved_by_operations", "commercialization_failure_remaining"),
        "event_premium_not_structural_success",
        "needs_price_backfill",
        ("Reuters bluebird revised offer",),
        "A higher M&A offer can move price, but it is not evidence of structural commercialization success.",
    ),
    Round47CaseCandidate(
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
        "cro_funding_cycle_4c",
        "needs_price_backfill",
        ("Reuters Charles River forecast cut",),
        "CRO is service revenue, but funding-cycle cuts can break backlog and forecast visibility.",
    ),
    Round47CaseCandidate(
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
        ("impairment_charge", "forecast_withdrawal", "advertising_cost_increase", "revenue_slowdown", "record_low_stock"),
        "telehealth_dtc_failure_4c",
        "needs_price_backfill",
        ("Reuters Teladoc record low",),
        "Telehealth demand is not enough when CAC, impairment, churn, privacy, and FCF are weak.",
    ),
    Round47CaseCandidate(
        "recursion_exscientia_ai_drug_platform_case",
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
        "ai_platform_watch_commercialization_unproven",
        "needs_price_backfill",
        ("Reuters Recursion Exscientia merger",),
        "AI drug-discovery platform consolidation is Watch until milestones, clinical proof, and commercial economics appear.",
    ),
)


ROUND47_PRICE_FIELDS: tuple[str, ...] = (
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
    "below_stage3_price_flag",
    "contract_value",
    "contract_duration",
    "capacity_liters",
    "capacity_utilization",
    "backlog_growth",
    "customer_concentration",
    "op_margin_change",
    "fcf_margin",
    "prescription_volume",
    "weekly_scripts",
    "insurance_coverage",
    "pbm_listing_flag",
    "biosimilar_discount_pct",
    "drug_price_change",
    "compounded_alternative_flag",
    "clinical_trial_phase",
    "approval_status",
    "patient_uptake",
    "reimbursement_status",
    "cash_runway_months",
    "going_concern_flag",
    "dilution_or_take_private_flag",
    "hospital_adoption_count",
    "reimbursement_code_flag",
    "recurring_revenue_ratio",
    "ai_model_auc",
    "subgroup_performance_risk",
    "liability_risk_flag",
    "device_export_country_count",
    "procedure_volume",
    "consumable_revenue_ratio",
    "vbp_price_control_flag",
    "counterfeit_safety_flag",
    "cac",
    "churn",
    "privacy_incident_flag",
    "impairment_charge",
    "forecast_withdrawal_flag",
    "score_price_alignment",
    "price_validation_status",
)


def target_for(target_id: str) -> Round47ScoreTarget | None:
    for target in ROUND47_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round47_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND47_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
        weights = target.score_weight.as_dict()
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
                f"Round47 R7 case for {candidate.target_id}; "
                "case evidence is calibration-only and missing prices remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage2_signals or field in target.green_conditions),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage3_conditions),
            stage4b_evidence=stage4b_evidence,
            stage4c_evidence=stage4c_evidence,
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "overheat", "4b_watch", "4c_thesis_break"} else None,
            score_price_alignment=_score_price_alignment(candidate),
            rerating_result=_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint={
                "eps_fcf": float(weights["eps_fcf"]),
                "visibility": float(weights["structural_visibility"]),
                "bottleneck": float(weights["bottleneck_pricing"]),
                "mispricing": float(weights["market_mispricing"]),
                "valuation": float(weights["valuation"]),
                "capital_allocation": float(weights["capital_allocation"]),
            },
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_cross_evidence_for_green",
                "theme_label_is_not_score_evidence",
                "approval_or_clinical_news_is_not_revenue",
                "paper_auc_or_ai_label_is_not_green_evidence_alone",
                "commercialization_reimbursement_fcf_required_for_green",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.7 if candidate.stage2_date or candidate.stage4c_date else 0.3,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round47_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND47_SCORE_TARGETS:
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
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round47_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND47_CASE_CANDIDATES:
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


def round47_stage_date_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND47_SCORE_TARGETS:
        rows.append(
            {
                "target_id": target.target_id,
                "stage1": "|".join(target.stage1_signals),
                "stage2": "|".join(target.stage2_signals),
                "stage3": "|".join(target.stage3_conditions),
                "stage4b": "|".join(target.stage4b_conditions),
                "stage4c": "|".join(target.stage4c_conditions),
                "production_scoring_changed": "false",
            }
        )
    return tuple(rows)


def round47_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round47_backfill": "true"} for field in ROUND47_PRICE_FIELDS)


def round47_summary() -> dict[str, int | bool]:
    records = round47_case_records()
    return {
        "target_count": len(ROUND47_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch"),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND47_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND47_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND47_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round47_r7_reports(
    *,
    output_directory: str | Path = ROUND47_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND47_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND47_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round47_r7_biotech_healthcare_device_summary.md",
        "case_matrix": output / "round47_r7_case_matrix.csv",
        "stage_date_plan": output / "round47_r7_stage_date_plan.csv",
        "green_guardrails": output / "round47_r7_green_guardrails.md",
        "price_validation_plan": output / "round47_r7_price_validation_plan.md",
        "price_fields": output / "round47_r7_price_fields.csv",
    }
    _write_case_jsonl(round47_case_records(), cases)
    _write_rows(round47_score_profile_rows(), score_profiles)
    _write_rows(round47_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round47_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round47_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round47_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round47_green_guardrail_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round47_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round47_summary_markdown() -> str:
    summary = round47_summary()
    lines = [
        "# Round-47 R7 Biotech / Healthcare / Medical Device Summary",
        "",
        f"- source_round: `{ROUND47_SOURCE_ROUND_PATH}`",
        "- large_sector: `BIOTECH_HEALTHCARE_DEVICE`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R7 splits scoreable CDMO/device models from clinical, approval, AI, telehealth, and diagnostic headlines.",
        "- Example: Samsung Biologics capacity helps only after utilization, contracts, margin, and FCF are visible.",
        "- Example: Lunit model performance supports Stage 1/2, but reimbursement and hospital adoption decide higher stages.",
        "- Example: bluebird shows approval without commercialization can become a 4C thesis break.",
    ]
    return "\n".join(lines) + "\n"


def render_round47_green_guardrail_markdown() -> str:
    lines = [
        "# Round-47 R7 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND47_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these R7 v1.0 weights to production scoring yet.",
            "- Do not treat approval, clinical success, AI model AUC, a paper, a pilot, user growth, or disease outbreak demand as Green evidence by itself.",
            "- Do not invent prescription volume, reimbursement, hospital adoption, capacity utilization, patient uptake, cash runway, procedure volume, consumable revenue, CAC, churn, or price-path fields.",
            "- Do not lower Stage 3-Green for biotech recall. Green requires commercialization, reimbursement, recurring revenue, FCF conversion, or contracted utilization evidence.",
            "- Treat slow uptake, cash crunch, dilution, take-private, forecast cut, privacy breach, impairment, counterfeit product, safety issue, price control, and one-off diagnostic normalization as RedTeam evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round47_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-47 R7 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Calculate peak price, drawdown after peak, and below-stage3 flag.",
        "6. Compare price paths with utilization, prescriptions, reimbursement, patient uptake, hospital adoption, procedure volume, consumables, cash runway, CAC, churn, and safety/regulatory events.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | stage candidate | check |",
        "| --- | --- | --- |",
    ]
    priority = {
        "samsung_biologics_cdmo_contract_reference",
        "recursion_exscientia_ai_drug_platform_case",
    }
    for row in round47_case_candidate_rows():
        if row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or row["case_id"] in priority:
            stage_date = row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or "needs_source_date"
            lines.append(f"| `{row['case_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `aligned`: commercialization, utilization, prescriptions, procedures, reimbursement, or FCF moves with price rerating.",
            "- `delayed_or_uncertain`: strategic evidence exists, but price or EPS/FCF conversion is not yet confirmed.",
            "- `approval_without_commercialization`: approval exists but patient uptake, reimbursement, or sales are missing.",
            "- `clinical_or_ai_hype`: paper, AI model, or PoC drives attention without paid deployment.",
            "- `event_premium`: M&A or revised offer moves price without operational rerating.",
            "- `thesis_break`: cash crunch, forecast cut, safety event, impairment, or one-off demand normalization breaks the thesis.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round47CaseCandidate) -> str:
    if "aligned" in candidate.alignment_hint and candidate.case_type in {"structural_success", "success_candidate"}:
        return "aligned"
    if candidate.case_type in {"event_premium", "overheat", "4b_watch"}:
        return "price_moved_without_evidence"
    if candidate.case_type in {"failed_rerating", "4c_thesis_break"}:
        return "false_positive_score"
    return "unknown"


def _rerating_result(candidate: Round47CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "event_premium":
        return "event_premium"
    if candidate.case_type == "overheat":
        return "theme_overheat"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "failed_rerating":
        return "no_rerating"
    return "unknown"


def _write_case_jsonl(records: Iterable[E2RCaseRecord], path: Path) -> Path:
    lines = []
    for record in records:
        record.validate()
        lines.append(json.dumps(record.as_dict(), ensure_ascii=False, sort_keys=True))
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return path


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    row_tuple = tuple(rows)
    if not row_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(row_tuple[0].keys()), lineterminator="\n")
        writer.writeheader()
        for row in row_tuple:
            writer.writerow(row)
    return path


__all__ = [
    "ROUND47_CASE_CANDIDATES",
    "ROUND47_DEFAULT_CASES_PATH",
    "ROUND47_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND47_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND47_PRICE_FIELDS",
    "ROUND47_SCORE_TARGETS",
    "ROUND47_SOURCE_ROUND_PATH",
    "Round47CaseCandidate",
    "Round47ScoreTarget",
    "Round47ScoreWeightDraft",
    "render_round47_green_guardrail_markdown",
    "render_round47_price_validation_plan_markdown",
    "render_round47_summary_markdown",
    "round47_case_candidate_rows",
    "round47_case_records",
    "round47_price_field_rows",
    "round47_score_profile_rows",
    "round47_stage_date_rows",
    "round47_summary",
    "target_for",
    "write_round47_r7_reports",
]
