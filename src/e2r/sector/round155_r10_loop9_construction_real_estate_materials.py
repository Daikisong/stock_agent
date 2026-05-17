"""Round-155 R10 Loop-9 construction, real-estate, and building-materials pack.

Round 155 tightens the Round-50 R10 pack. It separates PF relief rallies,
REIT cash-flow quality, AI data-center real assets, cold-chain logistics,
building-material price/cost cycles, and reconstruction policy events.
Backlog, dividend yield, AI data-center labels, and reconstruction headlines
are not Stage 3 evidence unless PF risk, cash conversion, occupancy, NOI/AFFO,
tenant lease, power/water access, volume, OPM, and FCF are source-backed.
Loop 9 adds sponsor-premium, no-revenue/no-tenant, water-rights,
ratepayer/utility-cost, and precast/building-solution gates.

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


ROUND155_SOURCE_ROUND_PATH = "docs/round/round_155.md"
ROUND155_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round155_r10_loop9_construction_real_estate_materials"
ROUND155_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop9_round155.jsonl"
ROUND155_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round155_r10_loop9_v9.csv"


@dataclass(frozen=True)
class Round155ScoreWeightDraft:
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
class Round155BaseScoreAxis:
    axis_id: str
    score_weight: int
    stage2_evidence: tuple[str, ...]
    stage3_evidence: tuple[str, ...]
    hard_redteam_flags: tuple[str, ...]
    normalization_point: str

    def as_dict(self) -> dict[str, str]:
        return {
            "axis_id": self.axis_id,
            "score_weight": str(self.score_weight),
            "stage2_evidence": "|".join(self.stage2_evidence),
            "stage3_evidence": "|".join(self.stage3_evidence),
            "hard_redteam_flags": "|".join(self.hard_redteam_flags),
            "normalization_point": self.normalization_point,
            "production_scoring_changed": "false",
        }


@dataclass(frozen=True)
class Round155StageCap:
    cap_id: str
    score_cap: str
    cap_triggers: tuple[str, ...]
    release_conditions: tuple[str, ...]
    hard_redteam_flags: tuple[str, ...]
    interpretation: str

    def as_dict(self) -> dict[str, str]:
        return {
            "cap_id": self.cap_id,
            "score_cap": self.score_cap,
            "cap_triggers": "|".join(self.cap_triggers),
            "release_conditions": "|".join(self.release_conditions),
            "hard_redteam_flags": "|".join(self.hard_redteam_flags),
            "interpretation": self.interpretation,
            "production_scoring_changed": "false",
        }


@dataclass(frozen=True)
class Round155ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round155ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop9_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round155CaseCandidate:
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


GATE_WEIGHT = Round155ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate")


ROUND155_BASE_SCORE_AXES: tuple[Round155BaseScoreAxis, ...] = (
    Round155BaseScoreAxis(
        "eps_fcf_affo_noi_conversion",
        24,
        ("noi_growth", "affo_growth", "ffo_growth", "cash_conversion_cycle", "op_margin_change"),
        ("affo_per_share_growth", "fcf_stability", "dividend_coverage_ratio", "cash_conversion_improvement"),
        ("affo_integrity_risk", "dividend_cut", "capex_growth_above_affo_growth", "net_loss"),
        "Real estate and data-center themes must convert into NOI, AFFO per share, FCF, and dividend coverage.",
    ),
    Round155BaseScoreAxis(
        "asset_tenant_contract_pf_visibility",
        20,
        ("asset_acquired_flag", "binding_lease_flag", "contract_value", "pf_refinancing_success", "occupancy_rate"),
        ("tenant_contract_quality", "pf_exposure_reduction", "refinancing_success_flag", "occupancy_resilience"),
        ("no_acquired_assets", "tenant_lease_missing", "pf_delinquency_increase", "bridge_loan_rollover_failure"),
        "Backlog, sponsor premium, or PF policy support is capped until assets, tenants, contracts, or project-level PF repair are visible.",
    ),
    Round155BaseScoreAxis(
        "power_water_permitting_local_acceptance",
        16,
        ("power_secured_flag", "water_permitting_flag", "grid_interconnection_flag", "zoning_approval_flag"),
        ("community_approval_flag", "project_schedule_intact"),
        ("project_withdrawal", "moratorium", "referendum_or_moratorium", "water_rights_delay", "ratepayer_cost_risk"),
        "AI data-center demand is not enough unless power, water, permits, grid timing, and local acceptance are secured.",
    ),
    Round155BaseScoreAxis(
        "cost_price_volume_mna_synergy",
        14,
        ("price_hike", "cost_saving_amount", "volume_recovery", "mna_multiple", "earnings_accretive_guidance_flag"),
        ("volume_and_price_aligned", "synergy_realized", "opm_improvement", "fcf_stability"),
        ("volume_decline", "energy_cost_spike", "multiple_overpay", "integration_failure"),
        "Building-material price hikes and M&A only count when volume, costs, OPM, FCF, and integration evidence line up.",
    ),
    Round155BaseScoreAxis(
        "leverage_capex_affo_integrity_disclosure",
        12,
        ("ltv_stable", "debt_to_ebitda", "capex_to_affo_ratio", "maintenance_capex", "parser_confidence"),
        ("leverage_stable", "maintenance_capex_verified", "affo_bridge_verified", "source_detail_confidence_checked"),
        ("maintenance_capex_misclassification", "funding_gap", "disclosure_confidence_low", "debt_burden"),
        "Disclosure confidence, leverage, CAPEX burden, and AFFO integrity are hard gates for REIT and infrastructure stories.",
    ),
    Round155BaseScoreAxis(
        "market_mispricing_rerating_gap",
        8,
        ("old_frame_discount", "nav_discount", "yield_chase_discount", "cyclical_discount"),
        ("rerating_gap_vs_cashflow", "new_frame_not_fully_priced"),
        ("theme_priced_before_cashflow", "support_news_priced_before_restructuring"),
        "Rerating gap matters after cash-flow evidence, not before it.",
    ),
    Round155BaseScoreAxis(
        "valuation_room_4b_margin",
        6,
        ("valuation_discount", "relative_multiple_gap", "price_path_not_extended"),
        ("valuation_room_after_stage2", "4b_margin_remaining"),
        ("price_runup_excessive", "consensus_crowded", "valuation_saturation"),
        "R10 can move from Watch to 4B quickly when valuation moves ahead of NOI/AFFO, volume, or PF repair.",
    ),
)


ROUND155_STAGE_CAPS: tuple[Round155StageCap, ...] = (
    Round155StageCap(
        "stage1_headline_cap",
        "45",
        (
            "pf_support_headline",
            "rate_cut_expectation",
            "ai_data_center_label",
            "reconstruction_policy_headline",
            "high_dividend_yield",
            "building_material_price_hike_only",
        ),
        (
            "project_level_pf_repair",
            "cash_conversion_improvement",
            "tenant_or_contract_detail",
            "noi_affo_or_fcf_conversion",
        ),
        (
            "pf_delinquency_increase",
            "no_tenant",
            "no_acquired_assets",
            "policy_event_only",
            "volume_decline",
        ),
        "Headlines can create radar candidates, but they stay capped until project cash flow or asset evidence is visible.",
    ),
    Round155StageCap(
        "stage2_cashflow_visibility_cap",
        "70",
        (
            "asset_or_tenant_claim",
            "noi_affo_claim",
            "pf_refinancing_claim",
            "occupancy_claim",
            "building_products_mna_claim",
            "rco_or_cost_saving_claim",
        ),
        (
            "affo_per_share_or_fcf_growth",
            "dividend_coverage",
            "power_water_permitting_secured",
            "volume_and_price_aligned",
            "leverage_after_mna_stable",
            "source_detail_confidence_checked",
        ),
        (
            "maintenance_capex_misclassification",
            "capex_growth_above_affo_growth",
            "office_impairment",
            "bridge_loan_rollover_failure",
            "integration_failure",
        ),
        "Stage 2 can recognize real progress, but Stage 3 needs cross-evidence and price-path validation.",
    ),
    Round155StageCap(
        "stage3_cross_evidence_gate",
        "requires_score_above_70_and_cross_evidence",
        (
            "candidate_above_70_without_cross_evidence",
            "green_requested_from_single_family_evidence",
        ),
        (
            "price_path_validated",
            "cash_flow_conversion_verified",
            "redteam_clean",
            "parser_confidence_sufficient",
            "at_least_two_independent_evidence_families",
        ),
        (
            "hard_redteam_flag",
            "unsafe_single_source_green",
            "date_or_price_path_missing",
            "future_data_leakage",
        ),
        "R10 Green is not a score-only event; it requires cash-flow evidence plus independent confirmation and no hard RedTeam flag.",
    ),
    Round155StageCap(
        "stage4b_4c_real_asset_breaks",
        "monitor_or_break",
        (
            "crowded_ai_reit",
            "crowded_building_materials",
            "sponsor_premium_pipeline",
            "price_runup_before_cashflow",
        ),
        (
            "revision_momentum_intact",
            "affo_or_fcf_keeps_up_with_capex",
            "project_schedule_intact",
            "volume_and_margin_still_confirmed",
        ),
        (
            "dividend_cut",
            "project_withdrawal",
            "water_rights_delay",
            "ratepayer_cost_risk",
            "contract_or_tenant_missing_after_promotion",
            "guidance_cut",
        ),
        "4B and 4C separate normal rerating monitoring from thesis break; price-only overheat is not full 4B without evidence.",
    ),
)


ROUND155_SCORE_TARGETS: tuple[Round155ScoreTarget, ...] = (
    Round155ScoreTarget(
        "CONSTRUCTION_REAL_ESTATE_CREDIT",
        E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round155ScoreWeightDraft(12, 8, 5, 11, 7, 0, 5),
        ("pf_support", "rate_cut_expectation", "property_recovery_news", "backlog_headline"),
        ("refinancing_success", "unsold_inventory_decline", "cash_flow_improvement", "construction_cost_ratio_stable"),
        ("pf_risk_reduced", "eps_fcf_recovery", "cash_conversion_improves", "valuation_frame_change"),
        ("pf_relief_rally_crowded", "support_news_priced_before_restructuring"),
        ("pf_delinquency_increase", "bridge_loan_rollover_failure", "debt_workout", "impairment", "cost_ratio_spike"),
        ("refinancing_success", "cash_flow_improvement", "unsold_inventory_decline", "cost_ratio_stable"),
        ("pf_exposure", "unsold_inventory", "refinancing", "construction_cost_ratio", "debt_workout"),
        ("pf", "unsold_inventory", "refinancing", "cost_ratio", "cash_conversion"),
        "Backlog is secondary; PF exposure, refinancing, cash conversion, and cost ratio decide R10 credit quality.",
    ),
    Round155ScoreTarget(
        "PF_RESTRUCTURING_RELIEF",
        E2RArchetype.PF_RESTRUCTURING_RELIEF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round155ScoreWeightDraft(10, 8, 4, 10, 7, 0, 5),
        ("government_pf_support", "guarantee_expansion", "market_stabilizing_fund"),
        ("profitable_project_refinanced", "bridge_to_main_pf_conversion", "bad_project_separated"),
        ("cash_conversion_improves", "cost_ratio_stable", "pf_exposure_declines"),
        ("relief_rally_before_restructuring", "policy_support_priced_as_recovery"),
        ("delinquency_rises_after_support", "workout", "impairment", "unprofitable_project_restructuring"),
        ("refinancing_success_flag", "pf_exposure_reduction", "cash_conversion_improvement"),
        ("policy_support_only", "unprofitable_project", "bridge_loan", "delinquency"),
        ("policy_relief", "refinancing", "cash_conversion", "project_profitability"),
        "PF policy support is Stage 1 relief until individual refinancing and cash-flow repair are proven.",
    ),
    Round155ScoreTarget(
        "PF_SYNDICATED_LOAN_SOFT_LANDING",
        E2RArchetype.PF_SYNDICATED_LOAN_SOFT_LANDING,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round155ScoreWeightDraft(11, 9, 4, 10, 7, 0, 5),
        ("syndicated_loan", "pf_support", "guarantee_expansion", "profitable_project_rescue"),
        ("syndicated_loan_amount", "refinancing_success_flag", "profitable_project_flag", "bad_project_separated"),
        ("pf_exposure_declines", "cash_conversion_improves", "cost_ratio_stable", "unprofitable_project_restructured"),
        ("soft_landing_priced_before_project_separation", "syndicated_loan_headline_priced_as_recovery"),
        ("delinquency_rises_after_support", "bridge_loan_rollover_failure", "workout", "impairment", "unprofitable_project_restructuring_delay"),
        ("refinancing_success_flag", "pf_exposure_reduction", "cash_conversion_improvement", "cost_ratio_stable"),
        ("policy_support_only", "unprofitable_project", "bridge_loan", "delinquency", "workout"),
        ("policy_relief", "refinancing", "cash_conversion", "project_profitability"),
        "Syndicated PF loans can soften credit stress, but Green requires project-level refinancing, PF exposure decline, and cash conversion.",
    ),
    Round155ScoreTarget(
        "RESIDENTIAL_HOUSING_CYCLE",
        E2RArchetype.RESIDENTIAL_HOUSING_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round155ScoreWeightDraft(15, 12, 5, 12, 9, 1, 5),
        ("housing_recovery", "rate_cut_expectation", "presale_recovery"),
        ("unsold_inventory_decline", "starts_recovery", "cost_ratio_stable"),
        ("cash_flow_recovery", "eps_fcf_recovery", "credit_risk_low"),
        ("housing_cycle_rally_crowded",),
        ("unsold_inventory_increase", "household_debt_stress", "starts_decline", "rate_shock"),
        ("unsold_inventory_decline", "cost_ratio_stable", "cash_flow_recovery", "credit_risk_low"),
        ("unsold_inventory", "household_debt", "rate", "construction_cost", "starts_decline"),
        ("unsold_inventory", "household_debt", "starts", "rate", "cost_ratio"),
        "Housing-cycle improvement is Watch until inventory, cost, and cash conversion are visible.",
    ),
    Round155ScoreTarget(
        "REIT_DEVELOPMENT_TRUST",
        E2RArchetype.REIT_DEVELOPMENT_TRUST,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round155ScoreWeightDraft(15, 16, 5, 13, 11, 5, 5),
        ("rate_cut_expectation", "dividend_yield", "nav_discount"),
        ("occupancy", "noi_affo", "dividend_coverage", "ltv_stable"),
        ("affo_growth", "dividend_sustainability", "nav_discount_narrowing"),
        ("high_yield_reit_rally_crowded", "rate_cut_priced"),
        ("vacancy_increase", "ltv_deterioration", "refinancing_failure", "dividend_cut"),
        ("occupancy", "noi_affo", "dividend_coverage", "ltv_stable", "funding_cost_controlled"),
        ("vacancy", "ltv", "refinancing", "dividend_cut", "funding_cost"),
        ("occupancy", "noi_affo", "ltv", "funding_cost", "dividend_coverage"),
        "REIT/development-trust cases need asset cash flow and dividend coverage, not yield alone.",
    ),
    Round155ScoreTarget(
        "COMMERCIAL_REAL_ESTATE_CREDIT",
        E2RArchetype.COMMERCIAL_REAL_ESTATE_CREDIT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round155ScoreWeightDraft(10, 7, 4, 11, 6, 0, 5),
        ("office_recovery_news", "cre_credit_relief", "rate_cut_expectation"),
        ("vacancy_stabilization", "credit_loss_reserve_stable", "dividend_coverage"),
        ("loan_quality_recovery", "occupancy_recovery", "dividend_sustainability"),
        ("cre_relief_rally_before_credit_repair", "yield_chase_crowded"),
        ("office_vacancy", "watchlisted_or_impaired_loan", "credit_loss_reserve", "dividend_cut"),
        ("vacancy_stabilization", "loan_quality_recovery", "dividend_coverage"),
        ("office_exposure", "vacancy", "impaired_asset", "credit_loss_reserve", "dividend_cut"),
        ("office_vacancy", "impaired_loans", "credit_reserve", "dividend_cut"),
        "Commercial real-estate credit is RedTeam-first because vacancy and loan losses can break yield stories.",
    ),
    Round155ScoreTarget(
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        E2RArchetype.DATA_CENTER_REIT_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round155ScoreWeightDraft(18, 22, 18, 13, 11, 5, 5),
        ("ai_data_center_reit_ipo", "hyperscale_demand", "asset_pipeline"),
        ("asset_acquisition", "binding_tenant_lease", "power_cooling_water_secured", "noi_affo"),
        ("affo_growth", "dividend_coverage", "tenant_contract_quality", "funding_cost_controlled"),
        ("ai_infrastructure_reit_valuation_crowded", "capex_pipeline_priced_before_cashflow"),
        ("no_acquired_assets", "no_tenant", "no_affo", "power_or_water_permitting_failure", "funding_cost_up"),
        ("asset_acquisition", "hyperscale_tenant", "noi_affo", "dividend_coverage", "power_water_secured"),
        ("no_assets", "tenant_concentration", "capex", "funding_cost", "power_water_permitting"),
        ("asset", "tenant", "noi_affo", "power_water", "funding_cost"),
        "Data-center REIT Green requires assets, tenant lease, power/water, NOI/AFFO, and dividend coverage.",
    ),
    Round155ScoreTarget(
        "DATA_CENTER_REIT_IPO_NO_ASSET",
        E2RArchetype.DATA_CENTER_REIT_IPO_NO_ASSET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round155ScoreWeightDraft(11, 12, 13, 12, 7, 1, 5),
        ("ai_data_center_ipo", "sponsor_track_record", "acquisition_pipeline"),
        ("asset_acquired_flag", "binding_tenant_lease", "power_water_secured", "noi_affo_visible"),
        ("noi_affo", "dividend_coverage", "tenant_contract_quality", "asset_cashflow_proven"),
        ("ai_infrastructure_ipo_window_crowded", "sponsor_premium_priced_without_assets"),
        ("no_acquired_assets", "tenant_lease_missing", "no_affo", "funding_cost_up", "ipo_discount_or_flat_debut"),
        ("asset_acquired_flag", "binding_lease_flag", "noi_affo", "power_water_secured"),
        ("no_asset", "no_tenant", "no_affo", "sponsor_premium", "funding_cost"),
        ("asset", "tenant", "noi_affo", "sponsor_premium"),
        "AI data-center REIT IPOs without acquired assets or binding tenant leases stay Watch; sponsor premium is not cash flow.",
    ),
    Round155ScoreTarget(
        "DATA_CENTER_SPONSOR_PREMIUM_PIPELINE",
        E2RArchetype.DATA_CENTER_SPONSOR_PREMIUM_PIPELINE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round155ScoreWeightDraft(12, 13, 13, 12, 8, 1, 5),
        ("sponsor_track_record", "acquisition_pipeline", "ai_data_center_ipo", "asset_pipeline"),
        ("asset_acquired_flag", "binding_tenant_lease", "noi_affo_visible", "power_water_secured"),
        ("asset_cashflow_proven", "tenant_contract_quality", "dividend_coverage", "affo_growth"),
        ("sponsor_premium_priced_without_assets", "pipeline_priced_as_current_cashflow"),
        ("no_acquired_assets", "tenant_lease_missing", "no_affo", "funding_cost_up", "pipeline_execution_delay"),
        ("asset_acquired_flag", "binding_lease_flag", "noi_affo", "power_water_secured"),
        ("sponsor_premium", "no_asset", "no_tenant", "no_affo", "execution_delay"),
        ("sponsor", "pipeline", "asset", "tenant", "noi_affo"),
        "Sponsor premium and acquisition pipeline are Stage 1/2 evidence only; assets, tenant leases, and NOI/AFFO must be verified.",
    ),
    Round155ScoreTarget(
        "AI_DATA_CENTER_POWER_CAMPUS",
        E2RArchetype.AI_DATA_CENTER_POWER_CAMPUS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round155ScoreWeightDraft(13, 15, 18, 13, 7, 2, 5),
        ("ai_power_campus", "planned_power_gw", "dedicated_power_plan", "nuclear_gas_solar_power_plan"),
        ("binding_tenant_lease", "planned_power_delivery_year", "power_secured", "permitting", "financing_secured"),
        ("revenue_start", "noi_affo", "tenant_contract_quality", "power_delivery_on_schedule", "financing_stability"),
        ("ai_power_campus_valuation_crowded", "long_dated_power_priced_today"),
        ("no_tenant", "power_delivery_delay", "water_permitting_delay", "funding_gap", "single_site_concentration", "non_binding_loi"),
        ("binding_tenant_lease", "power_secured", "water_permitting_secured", "revenue_start", "noi_affo"),
        ("no_tenant", "non_binding_loi", "power_delivery_delay", "water_permitting", "funding_gap"),
        ("tenant", "power_delivery", "water", "permitting", "funding"),
        "AI power campuses get bottleneck credit only after binding tenants, power delivery, water/permitting, financing, and revenue are source-backed.",
    ),
    Round155ScoreTarget(
        "AI_DATA_CENTER_NO_REVENUE_NO_TENANT",
        E2RArchetype.AI_DATA_CENTER_NO_REVENUE_NO_TENANT,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("ai_data_center_campus", "power_campus_plan", "pre_revenue_real_asset", "non_binding_loi"),
        ("binding_tenant_lease", "revenue_start", "funding_secured", "permitting_secured"),
        ("not_applicable_gate_only",),
        ("no_revenue_ai_real_asset_valuation_crowded", "tenant_gap_priced_as_secured_demand"),
        ("no_revenue", "no_tenant", "non_binding_loi", "funding_agreement_terminated", "single_site_concentration", "net_loss"),
        (),
        ("no_revenue", "no_tenant", "non_binding_loi", "funding_gap", "single_site"),
        ("revenue", "tenant", "loi", "funding", "site_concentration"),
        "No-revenue AI data-center developers with no binding tenant lease are RedTeam gates, not Green candidates.",
        gate_only=True,
    ),
    Round155ScoreTarget(
        "DATA_CENTER_POWER_WATER_PERMITTING",
        E2RArchetype.DATA_CENTER_POWER_WATER_PERMITTING,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("local_opposition", "water_rights_issue", "grid_interconnection_delay", "noise_pollution"),
        ("permit_resolution", "power_interconnection_secured", "water_permitting_secured"),
        ("community_approval", "grid_and_water_secured", "project_schedule_intact"),
        ("power_water_risk_underpriced",),
        ("project_withdrawal", "referendum_or_moratorium", "zoning_rejection", "water_permitting_delay", "grid_interconnection_failure"),
        ("power_secured_flag", "water_permitting_flag", "community_approval_flag"),
        ("local_opposition", "water_permitting", "grid_interconnection", "noise", "withdrawal"),
        ("power", "water", "community", "permitting"),
        "Power, water, and local approval are gate checks, not positive score inputs.",
        gate_only=True,
    ),
    Round155ScoreTarget(
        "DATA_CENTER_LOCAL_OPPOSITION_OVERLAY",
        E2RArchetype.DATA_CENTER_LOCAL_OPPOSITION_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("local_opposition", "zoning_pause", "referendum", "community_opposition"),
        ("local_opposition_resolved", "zoning_approval", "community_approval"),
        ("community_approval", "zoning_approval", "project_schedule_intact"),
        ("local_opposition_risk_underpriced", "zoning_delay_ignored"),
        ("moratorium", "zoning_pause", "referendum_or_moratorium", "project_delay", "project_withdrawal"),
        ("community_approval_flag", "zoning_approval_flag", "local_opposition_resolved_flag"),
        ("moratorium", "zoning_pause", "referendum", "community_opposition", "project_delay"),
        ("moratorium", "zoning", "community", "project_timing"),
        "local opposition, zoning pauses, zoning pauses, and referendum risk are hard timing gates for data-center real assets.",
        gate_only=True,
    ),
    Round155ScoreTarget(
        "DATA_CENTER_WATER_RIGHTS_REFERENDUM",
        E2RArchetype.DATA_CENTER_WATER_RIGHTS_REFERENDUM,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("water_rights_issue", "referendum", "large_power_demand", "community_opposition"),
        ("water_rights_secured", "referendum_resolved", "phased_approval_complete"),
        ("not_applicable_gate_only",),
        ("water_rights_risk_underpriced", "power_campus_priced_before_local_approval"),
        ("water_rights_delay", "referendum_or_moratorium", "phased_approval_delay", "ratepayer_cost_risk", "project_delay"),
        (),
        ("water_rights", "referendum", "ratepayer_cost", "phased_approval"),
        ("water", "referendum", "local_cost", "approval"),
        "Water-rights and referendum risk are hard gates for data-center real assets.",
        gate_only=True,
    ),
    Round155ScoreTarget(
        "DATA_CENTER_RATEPAYER_UTILITY_COST_OVERLAY",
        E2RArchetype.DATA_CENTER_RATEPAYER_UTILITY_COST_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("utility_strain", "ratepayer_cost", "power_cost_concern", "public_hearing_delay"),
        ("utility_cost_allocation_resolved", "grid_upgrade_plan_funded", "community_approval"),
        ("not_applicable_gate_only",),
        ("utility_cost_risk_underpriced",),
        ("ratepayer_cost_risk", "utility_strain", "power_cost_concern", "public_hearing_delay", "grid_upgrade_cost_dispute"),
        (),
        ("ratepayer_cost", "utility_strain", "power_cost", "public_hearing"),
        ("utility", "ratepayer", "grid", "hearing"),
        "Data-center utility strain and ratepayer-cost backlash can block project timing even when AI demand is real.",
        gate_only=True,
    ),
    Round155ScoreTarget(
        "DATA_CENTER_CAPEX_AFFO_DILUTION",
        E2RArchetype.DATA_CENTER_CAPEX_AFFO_DILUTION,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("ai_capex_plan", "data_center_expansion_capex", "affo_growth_question"),
        ("capex_to_affo_ratio", "affo_per_share_growth", "dividend_coverage_ratio"),
        ("not_applicable_gate_only",),
        ("ai_capex_growth_priced_before_affo_per_share",),
        ("capex_growth_above_affo_growth", "per_share_affo_slowdown", "funding_cost_rise", "dividend_coverage_pressure", "capacity_expansion_without_yield"),
        (),
        ("capex_to_affo", "affo_per_share_growth", "dividend_coverage", "funding_cost"),
        ("capex", "affo_share", "funding_cost", "dividend_coverage"),
        "Data-center CAPEX is a RedTeam gate when asset growth does not become per-share AFFO and dividend coverage.",
        gate_only=True,
    ),
    Round155ScoreTarget(
        "COLD_CHAIN_REIT_LOGISTICS",
        E2RArchetype.COLD_CHAIN_REIT_LOGISTICS,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round155ScoreWeightDraft(17, 19, 12, 12, 10, 5, 5),
        ("cold_storage_ipo", "food_pharma_cold_chain_demand", "warehouse_network_scale"),
        ("occupancy", "customer_contract", "noi_affo", "energy_cost_control"),
        ("repeat_logistics_demand", "dividend_coverage", "affo_visibility", "debt_stable"),
        ("cold_chain_reit_premium_crowded", "warehouse_scale_priced_without_profit"),
        ("net_loss", "energy_cost_pressure", "occupancy_decline", "debt_burden", "guidance_cut"),
        ("occupancy", "customer_count", "noi_affo", "energy_cost_control", "dividend_coverage"),
        ("net_loss", "energy_cost", "debt", "occupancy", "affo_uncertainty"),
        ("occupancy", "energy_cost", "noi_affo", "debt", "customer_inventory"),
        "Cold-chain scale is useful only when NOI/AFFO, occupancy, energy cost, debt, and dividend coverage are controlled.",
    ),
    Round155ScoreTarget(
        "COLD_CHAIN_DEBT_OCCUPANCY_RISK",
        E2RArchetype.COLD_CHAIN_DEBT_OCCUPANCY_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("cold_chain_scale", "warehouse_network_premium", "food_pharma_cold_chain_demand"),
        ("occupancy_rate", "debt_to_ebitda", "energy_cost_ratio", "affo_visibility"),
        ("not_applicable_gate_only",),
        ("cold_chain_scale_priced_before_profitability",),
        ("net_loss", "debt_burden", "occupancy_decline", "energy_cost_pressure", "customer_inventory_normalization", "post_ipo_drawdown"),
        (),
        ("net_loss", "debt", "occupancy", "energy_cost", "customer_inventory"),
        ("debt", "occupancy", "energy_cost", "net_loss"),
        "Cold-chain debt and occupancy risk is a RedTeam gate: warehouse count is not AFFO or dividend coverage.",
        gate_only=True,
    ),
    Round155ScoreTarget(
        "BUILDING_MATERIALS_PRICE_COST",
        E2RArchetype.BUILDING_MATERIALS_PRICE_COST,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round155ScoreWeightDraft(18, 15, 12, 11, 10, 3, 5),
        ("price_hike", "cost_stabilization", "housing_starts_recovery", "infrastructure_demand"),
        ("volume_recovery", "opm_improvement", "cost_pass_through", "energy_cost_control"),
        ("fcf_stability", "volume_and_price_aligned", "opm_improvement", "infrastructure_demand_visible"),
        ("building_material_price_hike_crowded", "infrastructure_spend_priced", "price_hike_fully_priced"),
        ("volume_decline", "energy_cost_spike", "raw_material_cost_spike", "construction_slowdown", "ebitda_decline"),
        ("price_hike", "cost_pass_through", "volume_recovery", "opm_improvement", "fcf_stability"),
        ("volume_decline", "energy_cost", "raw_material_cost", "construction_slowdown", "ebitda_decline"),
        ("price", "cost", "volume", "opm", "fcf"),
        "Building materials can be Watch-to-Green only when price, cost, volume, OPM, and FCF align.",
    ),
    Round155ScoreTarget(
        "BUILDING_MATERIALS_VOLUME_FAILURE",
        E2RArchetype.BUILDING_MATERIALS_VOLUME_FAILURE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round155ScoreWeightDraft(13, 9, 8, 8, 6, 1, 5),
        ("price_hike", "cost_cut_program", "infrastructure_story"),
        ("price_offset", "cost_saving_amount"),
        ("volume_recovery_required", "ebitda_recovery_required"),
        ("price_hike_story_priced_despite_volume",),
        ("volume_decline", "demand_slowdown", "ebitda_decline", "price_increase_not_enough"),
        ("volume_recovery", "ebitda_recovery", "price_cost_spread"),
        ("volume_decline", "demand_slowdown", "ebitda_decline", "price_offset_failure"),
        ("volume", "ebitda", "demand", "price_cost"),
        "Price hikes and cost cuts are capped when volume and EBITDA are weak.",
    ),
    Round155ScoreTarget(
        "LOW_CARBON_CEMENT_PREMIUM",
        E2RArchetype.LOW_CARBON_CEMENT_PREMIUM,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round155ScoreWeightDraft(16, 14, 11, 12, 9, 2, 5),
        ("net_zero_cement", "carbon_capture", "ccs_project", "green_construction_demand"),
        ("product_presold_flag", "carbon_capture_capacity_tons", "ccs_subsidy_flag", "customer_contract"),
        ("green_premium_sustainable", "repeat_contract", "fcf_stability", "production_scale"),
        ("green_cement_premium_crowded", "subsidy_risk_underpriced"),
        ("ccs_cost_overrun", "subsidy_cut", "green_premium_not_accepted", "storage_contract_failure"),
        ("product_presold_flag", "green_premium_flag", "carbon_capture_capacity_tons", "fcf_stability", "subsidy_durability_ok"),
        ("subsidy_durability_risk", "ccs_cost", "green_premium_uncertain", "scale_up_risk"),
        ("subsidy", "green_premium", "ccs_cost", "customer_contract", "fcf"),
        "Low-carbon cement is Stage 2 with pre-sales and CCS; Green needs durable premium economics and FCF beyond subsidy support.",
    ),
    Round155ScoreTarget(
        "BUILDING_PRODUCTS_MNA_SHIFT",
        E2RArchetype.BUILDING_PRODUCTS_MNA_SHIFT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round155ScoreWeightDraft(17, 16, 9, 12, 10, 3, 5),
        ("building_products_mna", "walling_roofing_insulation_shift", "portfolio_shift"),
        ("target_revenue", "target_ebitda", "mna_multiple", "earnings_accretive_guidance_flag"),
        ("synergy_realized", "margin_improvement", "fcf_growth", "leverage_stable"),
        ("mna_story_crowded", "multiple_expansion_before_synergy"),
        ("integration_failure", "multiple_overpay", "debt_burden", "synergy_miss"),
        ("earnings_accretive_guidance_flag", "synergy_realized", "margin_improvement", "leverage_after_mna_stable"),
        ("integration_risk", "multiple_overpay", "leverage_after_mna", "synergy_miss"),
        ("mna_multiple", "synergy", "margin", "leverage", "fcf"),
        "Building-products M&A can shift the frame only after accretion, synergy, margin, FCF, and leverage stability are verified.",
    ),
    Round155ScoreTarget(
        "PRECAST_WALLING_BUILDING_SOLUTIONS",
        E2RArchetype.PRECAST_WALLING_BUILDING_SOLUTIONS,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round155ScoreWeightDraft(17, 16, 9, 12, 10, 3, 5),
        ("precast_concrete_mna", "walling_systems", "water_management_systems", "building_solutions_mix"),
        ("target_revenue", "production_site_count", "earnings_accretive_guidance_flag", "systems_selling_opportunity"),
        ("synergy_realized", "building_solutions_margin", "fcf_growth", "leverage_stable"),
        ("building_solution_mna_story_crowded", "multiple_expansion_before_synergy"),
        ("deal_price_unknown", "synergy_miss", "integration_failure", "europe_construction_slowdown", "leverage_increase"),
        ("earnings_accretive_guidance_flag", "margin_improvement", "leverage_after_mna_stable", "fcf_growth"),
        ("deal_price_unknown", "integration_risk", "leverage_after_mna", "synergy_miss"),
        ("precast", "walling", "water_management", "synergy", "leverage"),
        "Precast, walling, and water-management M&A are Green-eligible only after accretion, margin, FCF, and leverage evidence.",
    ),
    Round155ScoreTarget(
        "INFRA_RECONSTRUCTION_POLICY",
        E2RArchetype.INFRA_RECONSTRUCTION_POLICY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round155ScoreWeightDraft(10, 8, 8, 10, 7, 0, 4),
        ("ukraine_reconstruction", "neom_city", "overseas_infra_policy", "disaster_recovery_policy"),
        ("actual_contract", "financing_secured", "construction_started", "revenue_recognition"),
        ("multi_year_backlog", "contract_margin_visible", "delivery_schedule"),
        ("policy_theme_crowded", "reconstruction_basket_rally_before_contract"),
        ("project_cancellation", "financing_failure", "geopolitical_setback", "project_delay"),
        ("actual_contract", "financing_secured", "contract_margin_visible", "delivery_schedule"),
        ("no_actual_contract", "financing", "policy_event_only", "project_delay"),
        ("contract", "financing", "construction_started", "revenue_recognition"),
        "Reconstruction policy is Event/Watch until funded contracts and margin evidence exist.",
    ),
    Round155ScoreTarget(
        "POLICY_LOCAL_REAL_ESTATE_THEME",
        E2RArchetype.POLICY_LOCAL_REAL_ESTATE_THEME,
        Round10ThemePosture.REDTEAM_FIRST,
        Round155ScoreWeightDraft(5, 5, 4, 8, 5, 0, 3),
        ("sejong_city", "local_development_policy", "agency_relocation_headline"),
        ("budget_allocated", "actual_contract", "land_or_permit_approval"),
        ("revenue_recognized", "project_margin_visible", "multi_year_contract"),
        ("local_policy_theme_crowded", "budget_not_yet_confirmed"),
        ("policy_reversal", "budget_absent", "contract_absent", "project_delay"),
        ("budget_allocated_flag", "actual_contract", "revenue_recognized"),
        ("policy_event_only", "budget_absent", "contract_absent", "delay"),
        ("policy", "budget", "contract", "revenue"),
        "Sejong and local-development themes are Stage 1 events until budget, contract, and revenue are verified.",
    ),
    Round155ScoreTarget(
        "PF_CREDIT_REDTEAM_OVERLAY",
        E2RArchetype.PF_CREDIT_REDTEAM_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("pf_delinquency", "bridge_loan_rollover_failure", "workout"),
        ("pf_exposure_reduced", "workout_resolved"),
        ("credit_risk_removed",),
        ("pf_relief_rally_ignores_credit",),
        ("pf_delinquency_increase", "bridge_loan_rollover_failure", "debt_workout", "impairment"),
        ("pf_exposure_declines", "refinancing_success_flag"),
        ("pf_delinquency", "bridge_loan", "workout", "impairment"),
        ("pf", "credit", "workout"),
        "PF credit risk is a RedTeam gate that can block Green even when order backlog exists.",
        gate_only=True,
    ),
    Round155ScoreTarget(
        "REIT_AFFO_INTEGRITY_OVERLAY",
        E2RArchetype.REIT_AFFO_INTEGRITY_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("affo_overstatement_allegation", "maintenance_capex_question", "dividend_coverage_question"),
        ("capex_classification_verified", "affo_bridge_verified"),
        ("affo_integrity_clean", "dividend_coverage_verified"),
        ("affo_yield_chase_ignores_capex",),
        ("maintenance_capex_misclassification", "affo_overstatement", "dividend_cut", "capex_burden"),
        ("maintenance_capex_verified", "dividend_coverage_ratio", "affo_per_share_growth"),
        ("affo_integrity", "maintenance_capex", "dividend_cut", "capex_burden"),
        ("affo", "maintenance_capex", "dividend_coverage"),
        "AFFO and dividend coverage must pass capex-integrity checks before a REIT can be Green.",
        gate_only=True,
    ),
    Round155ScoreTarget(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        Round155ScoreWeightDraft("cap", "cap", "cap", "cap", "cap", "cap", "+"),
        ("contract_headline", "tenant_headline", "pf_headline", "noi_affo_claim"),
        ("detail_fetch_required", "source_detail_confidence_checked"),
        ("stage3_cap_until_contract_tenant_noi_affo_or_pf_detail_verified",),
        ("headline_priced_before_detail_fetch",),
        ("contract_value_missing", "tenant_missing", "noi_affo_missing", "pf_detail_missing", "disclosure_confidence_low"),
        (),
        ("contract_terms_missing", "tenant_detail_missing", "noi_affo_missing", "pf_detail_missing", "parser_confidence_low"),
        ("disclosure_confidence", "contract", "tenant", "noi_affo", "pf_detail"),
        "R10 disclosures cap Stage 3 until contract, tenant, NOI/AFFO, PF detail, and parser confidence are verified.",
    ),
)



ROUND155_CASE_CANDIDATES: tuple[Round155CaseCandidate, ...] = (
    Round155CaseCandidate(
        "korea_pf_delinquency_restructuring_case",
        "PF_CREDIT_REDTEAM_OVERLAY",
        "KR_PF_DELINQUENCY",
        "Korea PF delinquency restructuring",
        "KR",
        "4c_thesis_break",
        date(2024, 5, 13),
        None,
        None,
        None,
        date(2024, 5, 13),
        ("pf_delinquency_rate", "fss_project_assessment", "restructuring"),
        ("pf_delinquency_increase", "bridge_loan_rollover_failure", "debt_workout"),
        "pf_credit_risk_hard_counterexample",
        "needs_price_backfill",
        ("Reuters Korea tightens scrutiny to speed up real estate restructuring",),
        "PF delinquency rose from 0.37% in 2021 to 2.70% in 2023; backlog alone cannot create Green.",
        (E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,),
    ),
    Round155CaseCandidate(
        "korea_builder_support_relief_case",
        "PF_RESTRUCTURING_RELIEF",
        "KR_BUILDER_SUPPORT",
        "Korea builder liquidity support",
        "KR",
        "event_premium",
        date(2024, 3, 27),
        None,
        None,
        date(2024, 3, 27),
        None,
        ("government_support", "policy_support_amount", "builder_liquidity_support"),
        ("pf_exposure", "unsold_inventory", "refinancing"),
        "pf_policy_relief_stage1",
        "needs_price_backfill",
        ("Reuters Korea prepares financial support for builders",),
        "Government support is Stage 1 relief; Stage 2 needs refinancing and cash-flow proof.",
    ),
    Round155CaseCandidate(
        "korea_pf_syndicated_loan_soft_landing_case",
        "PF_SYNDICATED_LOAN_SOFT_LANDING",
        "KR_PF_SYNDICATED_LOAN",
        "Korea PF syndicated loan soft landing",
        "KR",
        "event_premium",
        date(2024, 5, 13),
        date(2024, 5, 13),
        None,
        None,
        None,
        ("syndicated_loan_amount", "pf_soft_landing_support_flag", "profitable_project_flag"),
        ("unprofitable_project_restructuring_flag", "pf_delinquency_rate", "bridge_loan_exposure"),
        "pf_soft_landing_but_not_green",
        "needs_price_backfill",
        ("Reuters Korea FSS says banks and insurers prepare PF syndicated loan",),
        "Syndicated PF loans can support profitable projects, but unresolved bad projects, bridge loans, and cash conversion keep it Watch.",
        (E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,),
    ),
    Round155CaseCandidate(
        "blackstone_mortgage_trust_dividend_cut_case",
        "COMMERCIAL_REAL_ESTATE_CREDIT",
        "BXMT",
        "Blackstone Mortgage Trust dividend cut",
        "US",
        "4c_thesis_break",
        date(2024, 7, 24),
        None,
        None,
        None,
        date(2024, 7, 24),
        ("office_exposure", "watchlisted_or_impaired_asset_ratio", "credit_loss_reserve"),
        ("dividend_cut", "office_vacancy", "impaired_loan", "credit_loss_reserve"),
        "commercial_real_estate_credit_4c",
        "needs_price_backfill",
        ("Reuters Blackstone mortgage fund slumps as empty offices intensify pressure",),
        "Dividend cut after office credit stress is a hard CRE credit 4C example.",
    ),
    Round155CaseCandidate(
        "equinix_affo_integrity_short_case",
        "REIT_AFFO_INTEGRITY_OVERLAY",
        "EQIX",
        "Equinix AFFO integrity short case",
        "US",
        "4c_thesis_break",
        date(2024, 3, 20),
        None,
        None,
        None,
        date(2024, 3, 20),
        ("affo_overstatement_allegation", "maintenance_capex", "short_report_flag"),
        ("maintenance_capex_misclassification", "affo_integrity_risk", "power_constrained_facility"),
        "reit_affo_integrity_risk",
        "needs_price_backfill",
        ("Reuters Hindenburg shorts data center firm Equinix",),
        "Data-center REIT AFFO must be verified against maintenance capex and dividend coverage.",
        (E2RArchetype.DATA_CENTER_REIT_INFRASTRUCTURE,),
    ),
    Round155CaseCandidate(
        "equinix_ai_capex_burden_case",
        "DATA_CENTER_CAPEX_AFFO_DILUTION",
        "EQIX",
        "Equinix AI capex burden",
        "US",
        "4b_watch",
        date(2025, 6, 26),
        None,
        None,
        date(2025, 6, 26),
        None,
        ("ai_inference_demand", "capex_amount", "affo_per_share_growth"),
        ("capex_growth_above_affo_growth", "per_share_affo_slowdown", "funding_cost_rise"),
        "ai_data_center_capex_burden_4b_to_4c_watch",
        "needs_price_backfill",
        ("Reuters Equinix shares fall as revenue and capital spending forecast disappoint",),
        "AI data-center demand can still pressure per-share AFFO when capex and funding costs outrun growth.",
        (E2RArchetype.DATA_CENTER_REIT_INFRASTRUCTURE,),
    ),
    Round155CaseCandidate(
        "equinix_ai_revenue_guidance_case",
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        "EQIX",
        "Equinix AI revenue guidance and AFFO gate",
        "US",
        "success_candidate",
        date(2026, 2, 11),
        date(2026, 2, 11),
        None,
        date(2026, 2, 11),
        None,
        ("revenue_guidance_above_estimate", "hyperscale_tenant_flag", "noi_growth", "affo_growth", "power_secured_flag"),
        ("capex_burden", "maintenance_capex", "power_grid_constraint", "tenant_concentration"),
        "data_center_reit_demand_real_but_affo_capex_gate",
        "needs_price_backfill",
        ("round_155.md Reuters Equinix annual sales forecast above estimates on AI data-center demand",),
        "AI demand can support a data-center REIT, but Green still needs AFFO per share, capex integrity, power/water, and dividend coverage.",
        (E2RArchetype.REIT_AFFO_INTEGRITY_OVERLAY, E2RArchetype.DATA_CENTER_CAPEX_AFFO_DILUTION),
    ),
    Round155CaseCandidate(
        "blackstone_data_center_reit_ipo_case",
        "DATA_CENTER_REIT_IPO_NO_ASSET",
        "BLACKSTONE_DC_REIT",
        "Blackstone Digital Infrastructure Trust IPO no asset",
        "US",
        "4b_watch",
        date(2026, 5, 13),
        None,
        None,
        date(2026, 5, 13),
        None,
        ("ai_data_center_reit_ipo", "hyperscale_tenant_target", "asset_pipeline", "sponsor_premium_flag"),
        ("no_acquired_assets", "no_affo", "tenant_lease_missing", "power_water_unverified"),
        "data_center_reit_theme_without_assets_yet",
        "needs_price_backfill",
        ("round_155.md Reuters Blackstone data center REIT raises $1.75 billion in US IPO",),
        "Sponsor and AI infrastructure demand are not enough before assets, tenants, NOI/AFFO, and power/water are verified.",
        (E2RArchetype.DATA_CENTER_SPONSOR_PREMIUM_PIPELINE,),
    ),
    Round155CaseCandidate(
        "fermi_ai_data_center_no_revenue_ipo_case",
        "AI_DATA_CENTER_NO_REVENUE_NO_TENANT",
        "FRMI",
        "Fermi AI data-center no-revenue IPO",
        "US",
        "4b_watch",
        date(2025, 10, 1),
        None,
        None,
        date(2025, 10, 1),
        None,
        ("ai_power_campus_flag", "planned_power_gw", "nuclear_power_plan_flag", "asset_pipeline_value"),
        ("no_revenue", "no_tenant", "non_binding_loi", "funding_gap", "single_site_concentration"),
        "ai_real_asset_no_revenue_high_risk_watch",
        "needs_price_backfill",
        ("round_155.md Reuters Fermi data center REIT Nasdaq debut after IPO",),
        "Pre-revenue AI real-asset mega-project valuation is 4B-watch, not Green.",
        (E2RArchetype.AI_DATA_CENTER_POWER_CAMPUS,),
    ),
    Round155CaseCandidate(
        "fermi_no_tenant_net_loss_case",
        "AI_DATA_CENTER_NO_REVENUE_NO_TENANT",
        "FRMI",
        "Fermi no tenant and net loss case",
        "US",
        "4c_thesis_break",
        date(2026, 3, 30),
        None,
        None,
        None,
        date(2026, 3, 30),
        ("no_revenue_flag", "non_binding_loi_flag", "asset_pipeline_value"),
        ("no_binding_tenant_lease", "net_loss_flag", "tenant_funding_agreement_terminated_flag", "single_site_concentration_flag"),
        "ai_real_asset_no_revenue_high_risk",
        "needs_price_backfill",
        ("round_155.md FT Fermi shares plunge on net loss",),
        "AI real-asset stories break when tenant lease, revenue, and funding remain unproven after valuation has moved.",
        (E2RArchetype.AI_DATA_CENTER_POWER_CAMPUS,),
    ),
    Round155CaseCandidate(
        "perth_datacenter_withdrawal_case",
        "DATA_CENTER_POWER_WATER_PERMITTING",
        "PERTH_DC_PROJECT",
        "Perth data-center withdrawal after opposition",
        "AU",
        "4c_thesis_break",
        date(2026, 5, 15),
        None,
        None,
        None,
        date(2026, 5, 15),
        ("local_opposition_flag", "noise_pollution_flag", "project_withdrawal_flag"),
        ("project_withdrawal", "community_opposition", "zoning_rejection"),
        "data_center_power_water_4c",
        "needs_price_backfill",
        ("Guardian Perth datacentre withdrawn after community opposition",),
        "Power, water, noise, and local approval can break AI data-center real asset projects.",
    ),
    Round155CaseCandidate(
        "utah_stratos_datacenter_backlash_case",
        "DATA_CENTER_WATER_RIGHTS_REFERENDUM",
        "UTAH_STRATOS_DC",
        "Utah Stratos AI data-center backlash",
        "US",
        "4b_watch",
        date(2026, 5, 13),
        None,
        None,
        date(2026, 5, 13),
        None,
        ("planned_power_gw", "water_rights_flag", "referendum_or_moratorium_flag", "ratepayer_cost_risk_flag"),
        ("water_rights_delay", "grid_interconnection_delay", "referendum_or_moratorium", "ratepayer_cost_risk"),
        "data_center_power_water_referendum_gate",
        "needs_price_backfill",
        ("Guardian Utah approves datacenter amid backlash",),
        "A 9GW data-center plan can be a 4B-watch when power and water backlash are not resolved.",
        (E2RArchetype.DATA_CENTER_POWER_WATER_PERMITTING, E2RArchetype.DATA_CENTER_RATEPAYER_UTILITY_COST_OVERLAY),
    ),
    Round155CaseCandidate(
        "seattle_datacenter_moratorium_case",
        "DATA_CENTER_LOCAL_OPPOSITION_OVERLAY",
        "SEATTLE_DC_MORATORIUM",
        "Seattle data-center moratorium watch",
        "US",
        "4b_watch",
        date(2026, 5, 15),
        None,
        None,
        date(2026, 5, 15),
        None,
        ("local_opposition_flag", "zoning_pause_flag", "community_opposition_flag"),
        ("moratorium", "zoning_pause", "project_delay", "community_opposition"),
        "data_center_local_opposition",
        "needs_price_backfill",
        ("round_155.md Guardian Seattle large data center moratorium watch",),
        "Urban data-center local opposition risk can delay real assets even when AI demand is strong.",
        (E2RArchetype.DATA_CENTER_POWER_WATER_PERMITTING,),
    ),
    Round155CaseCandidate(
        "indianapolis_datacenter_moratorium_case",
        "DATA_CENTER_LOCAL_OPPOSITION_OVERLAY",
        "INDIANAPOLIS_DC_MORATORIUM",
        "Indianapolis data-center moratorium watch",
        "US",
        "4b_watch",
        date(2026, 5, 15),
        None,
        None,
        date(2026, 5, 15),
        None,
        ("local_opposition_flag", "zoning_pause_flag", "community_submission_count"),
        ("moratorium", "zoning_pause", "referendum_or_moratorium", "project_delay"),
        "data_center_local_opposition",
        "needs_price_backfill",
        ("round_155.md Indianapolis data center moratorium resolution",),
        "local opposition, zoning pauses are a timing and execution gate, not a positive AI-infrastructure score input.",
        (E2RArchetype.DATA_CENTER_POWER_WATER_PERMITTING, E2RArchetype.DATA_CENTER_RATEPAYER_UTILITY_COST_OVERLAY),
    ),
    Round155CaseCandidate(
        "lineage_cold_storage_ipo_case",
        "COLD_CHAIN_REIT_LOGISTICS",
        "LINE",
        "Lineage cold-storage REIT IPO",
        "US",
        "success_candidate",
        date(2024, 7, 25),
        date(2024, 7, 25),
        None,
        None,
        None,
        ("cold_storage_warehouse_count", "customer_count", "noi_growth", "adjusted_ebitda"),
        ("net_loss", "energy_cost", "debt", "affo_uncertainty"),
        "cold_chain_scale_success_candidate_but_profitability_watch",
        "needs_price_backfill",
        ("Investopedia Lineage begins trading in biggest IPO of 2024",),
        "Scale and customer count help, but net loss and AFFO uncertainty keep Green restricted.",
    ),
    Round155CaseCandidate(
        "lineage_cold_storage_debt_occupancy_case",
        "COLD_CHAIN_DEBT_OCCUPANCY_RISK",
        "LINE",
        "Lineage cold-storage debt and occupancy risk",
        "US",
        "4c_thesis_break",
        date(2025, 10, 1),
        None,
        None,
        None,
        date(2025, 10, 1),
        ("post_ipo_drawdown_flag", "customer_inventory_normalization_flag", "guidance_cut"),
        ("net_loss", "energy_cost_pressure", "occupancy_decline", "debt_burden", "guidance_cut"),
        "cold_chain_scale_to_profitability_4c_watch",
        "needs_price_backfill",
        ("Barrons cold-storage stock drawdown discussion",),
        "Cold-chain warehouse scale is not Green when demand softens, energy cost and debt remain, and guidance is cut.",
        (E2RArchetype.COLD_CHAIN_REIT_LOGISTICS,),
    ),
    Round155CaseCandidate(
        "heidelberg_materials_price_cost_case",
        "BUILDING_MATERIALS_PRICE_COST",
        "HEI.DE",
        "Heidelberg Materials price-cost alignment",
        "EU",
        "success_candidate",
        date(2025, 11, 6),
        date(2025, 11, 6),
        None,
        date(2025, 11, 6),
        None,
        ("price_hike", "cost_saving_amount", "opm_improvement", "infrastructure_demand"),
        ("volume_decline", "energy_cost", "construction_slowdown"),
        "building_materials_price_cost_aligned_candidate",
        "needs_price_backfill",
        ("Reuters Heidelberg Materials higher Q3 profit on cost and price management",),
        "Building materials can be Watch-to-Green when price, cost, OPM, volume, and FCF align.",
    ),
    Round155CaseCandidate(
        "heidelberg_evozero_low_carbon_cement_case",
        "LOW_CARBON_CEMENT_PREMIUM",
        "HEI.DE",
        "Heidelberg evoZero low-carbon cement",
        "EU",
        "success_candidate",
        date(2025, 6, 18),
        date(2025, 6, 18),
        None,
        None,
        None,
        ("low_carbon_cement_flag", "net_zero_cement_flag", "carbon_capture_capacity_tons", "product_presold_flag", "ccs_subsidy_flag"),
        ("subsidy_durability_risk_flag", "green_premium_flag_unverified", "ccs_storage_contract_risk"),
        "low_carbon_cement_stage2_candidate",
        "needs_price_backfill",
        ("Reuters Heidelberg sells out net-zero cement from Norway plant",),
        "Pre-sold net-zero cement and CCS support Stage 2, while subsidy durability and durable green premium remain Stage 3 gates.",
        (E2RArchetype.BUILDING_MATERIALS_PRICE_COST,),
    ),
    Round155CaseCandidate(
        "cemex_demand_slowdown_costcut_case",
        "BUILDING_MATERIALS_VOLUME_FAILURE",
        "CEMEX",
        "Cemex demand slowdown and cost-cut program",
        "MX",
        "4c_thesis_break",
        date(2025, 2, 6),
        None,
        None,
        None,
        date(2025, 2, 6),
        ("price_hike", "cost_saving_amount"),
        ("volume_decline", "demand_slowdown", "ebitda_decline", "price_increase_not_enough"),
        "building_materials_volume_failure",
        "needs_price_backfill",
        ("Reuters Cemex sales decline and savings program",),
        "Price increases and cost cuts cannot create Green when volume, demand, and EBITDA are weak.",
    ),
    Round155CaseCandidate(
        "cemex_price_cost_restructuring_case",
        "BUILDING_MATERIALS_PRICE_COST",
        "CEMEX",
        "Cemex price-cost restructuring mixed case",
        "MX",
        "4b_watch",
        date(2025, 10, 27),
        date(2025, 10, 27),
        None,
        date(2025, 10, 27),
        None,
        ("price_hike", "cost_saving_amount", "ebitda_change", "opm_improvement"),
        ("building_material_volume_flat", "ready_mix_volume_decline", "aggregate_volume_decline", "capex_burden"),
        "building_materials_price_cost_mixed_volume_watch",
        "needs_price_backfill",
        ("round_155.md Reuters Cemex core earnings increase but volumes weak",),
        "Price/cost improvement can support Watch, but flat cement volume and ready-mix/aggregate weakness keep Green capped.",
        (E2RArchetype.BUILDING_MATERIALS_VOLUME_FAILURE,),
    ),
    Round155CaseCandidate(
        "holcim_xella_building_products_mna_case",
        "BUILDING_PRODUCTS_MNA_SHIFT",
        "HOLN.S",
        "Holcim Xella building-products M&A shift",
        "EU",
        "success_candidate",
        date(2025, 10, 20),
        date(2025, 10, 20),
        None,
        None,
        None,
        ("building_products_mna_flag", "target_revenue", "target_ebitda", "mna_multiple", "earnings_accretive_guidance_flag"),
        ("integration_risk_flag", "leverage_after_mna", "multiple_overpay"),
        "building_products_mna_shift_stage2_candidate",
        "needs_price_backfill",
        ("Reuters Holcim to buy Xella for 1.85 billion euros",),
        "A cement-to-building-products mix shift is Stage 2 until synergy, margin, FCF, and leverage stability are proven.",
        (E2RArchetype.BUILDING_MATERIALS_PRICE_COST,),
    ),
    Round155CaseCandidate(
        "holcim_alkern_precast_case",
        "PRECAST_WALLING_BUILDING_SOLUTIONS",
        "HOLN.S",
        "Holcim Alkern precast building-solutions mix shift",
        "EU",
        "success_candidate",
        date(2026, 1, 6),
        date(2026, 1, 6),
        None,
        None,
        None,
        ("precast_concrete_flag", "water_management_systems_flag", "target_revenue", "earnings_accretive_guidance_flag"),
        ("deal_price_unknown", "integration_risk_flag", "europe_construction_slowdown", "leverage_after_mna"),
        "building_solutions_mix_shift_reference",
        "needs_price_backfill",
        ("round_155.md Reuters Holcim acquires French precast concrete maker Alkern",),
        "Precast and water-management systems improve mix only after synergy, margin, FCF, and leverage are verified.",
        (E2RArchetype.BUILDING_PRODUCTS_MNA_SHIFT, E2RArchetype.BUILDING_MATERIALS_PRICE_COST),
    ),
    Round155CaseCandidate(
        "ukraine_reconstruction_event_watch_case",
        "INFRA_RECONSTRUCTION_POLICY",
        "UKRAINE_REBUILD_BASKET",
        "Ukraine reconstruction event watch",
        "GLOBAL",
        "event_premium",
        None,
        None,
        None,
        date(2025, 1, 1),
        None,
        ("reconstruction_policy", "infrastructure_theme"),
        ("no_actual_contract", "financing", "geopolitical_setback"),
        "policy_reconstruction_event",
        "needs_price_backfill",
        ("Round155 analyst matrix",),
        "Reconstruction policy needs funded contracts and supplier margin evidence before Green.",
    ),
    Round155CaseCandidate(
        "neom_city_event_watch_case",
        "INFRA_RECONSTRUCTION_POLICY",
        "NEOM_POLICY_BASKET",
        "Neom city event watch",
        "GLOBAL",
        "event_premium",
        None,
        None,
        None,
        date(2025, 1, 1),
        None,
        ("neom_city", "policy_theme", "infrastructure_theme"),
        ("no_actual_contract", "financing", "project_delay"),
        "policy_reconstruction_event",
        "needs_price_backfill",
        ("Round155 analyst matrix",),
        "Neom-related theme labels remain Event/Watch until actual contract economics are visible.",
    ),
    Round155CaseCandidate(
        "sejong_policy_theme_case",
        "POLICY_LOCAL_REAL_ESTATE_THEME",
        "SEJONG_POLICY_BASKET",
        "Sejong local real-estate policy theme",
        "KR",
        "event_premium",
        None,
        None,
        None,
        date(2025, 1, 1),
        None,
        ("sejong_city", "local_development_policy", "agency_relocation_headline"),
        ("budget_absent", "contract_absent", "policy_reversal", "project_delay"),
        "policy_reconstruction_event",
        "needs_price_backfill",
        ("Round155 analyst matrix",),
        "Local real-estate policy themes remain Stage 1 until budget, contract, and revenue recognition are visible.",
    ),
)



ROUND155_PRICE_FIELDS: tuple[str, ...] = (
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
    "pf_exposure",
    "pf_guarantee_amount",
    "pf_delinquency_rate",
    "bridge_loan_exposure",
    "syndicated_loan_amount",
    "pf_soft_landing_support_flag",
    "refinancing_success_flag",
    "debt_workout_flag",
    "unsold_inventory_units",
    "cash_conversion_cycle",
    "construction_cost_ratio",
    "gross_margin",
    "op_margin_change",
    "profitable_project_flag",
    "unprofitable_project_restructuring_flag",
    "revenue_backlog",
    "contract_value",
    "contract_duration_months",
    "contract_margin_signal",
    "project_financing_secured_flag",
    "construction_started_flag",
    "revenue_recognized_flag",
    "reit_type",
    "occupancy_rate",
    "noi_growth",
    "affo_growth",
    "ffo_growth",
    "affo_per_share_growth",
    "dividend_per_share",
    "dividend_cut_flag",
    "dividend_coverage_ratio",
    "ltv_ratio",
    "funding_cost",
    "refinancing_maturity",
    "office_exposure",
    "watchlisted_or_impaired_asset_ratio",
    "credit_loss_reserve",
    "non_accrual_asset_ratio",
    "maintenance_capex",
    "expansion_capex",
    "capex_amount",
    "capex_to_affo_ratio",
    "affo_integrity_risk_flag",
    "short_report_flag",
    "data_center_asset_acquired_flag",
    "hyperscale_tenant_flag",
    "tenant_concentration",
    "binding_lease_flag",
    "non_binding_loi_flag",
    "funding_agreement_terminated_flag",
    "investment_grade_tenant_flag",
    "power_secured_flag",
    "water_permitting_flag",
    "cooling_secured_flag",
    "advanced_liquid_cooling_flag",
    "grid_interconnection_flag",
    "asset_pipeline_value",
    "ai_infra_theme_flag",
    "sponsor_premium_flag",
    "bonus_share_ipo_flag",
    "no_revenue_flag",
    "single_site_concentration_flag",
    "power_delivery_date",
    "local_opposition_flag",
    "referendum_or_moratorium_flag",
    "water_rights_flag",
    "ratepayer_cost_risk_flag",
    "utility_strain_flag",
    "power_cost_concern_flag",
    "public_hearing_delay_flag",
    "project_withdrawal_flag",
    "noise_pollution_flag",
    "zoning_pause_flag",
    "community_submission_count",
    "ai_power_campus_flag",
    "planned_power_gw",
    "planned_power_delivery_year",
    "nuclear_power_plan_flag",
    "gas_power_plan_flag",
    "solar_power_plan_flag",
    "tenant_signed_flag",
    "tenant_funding_agreement_terminated_flag",
    "cold_storage_warehouse_count",
    "cold_storage_capacity",
    "energy_cost_ratio",
    "customer_count",
    "net_loss_flag",
    "cold_chain_occupancy_rate",
    "post_ipo_drawdown_flag",
    "customer_inventory_normalization_flag",
    "debt_to_ebitda",
    "building_material_volume",
    "cement_price_change",
    "steel_rebar_price_change",
    "energy_cost_change",
    "raw_material_cost_change",
    "price_hike_flag",
    "cost_saving_amount",
    "ebitda_change",
    "volume_decline_flag",
    "infrastructure_demand_flag",
    "low_carbon_cement_flag",
    "net_zero_cement_flag",
    "carbon_capture_capacity_tons",
    "ccs_subsidy_flag",
    "green_premium_flag",
    "product_presold_flag",
    "ccs_storage_contract_flag",
    "subsidy_durability_risk_flag",
    "building_products_mna_flag",
    "precast_concrete_flag",
    "walling_systems_flag",
    "water_management_systems_flag",
    "production_site_count",
    "target_revenue",
    "target_ebitda",
    "mna_multiple",
    "earnings_accretive_guidance_flag",
    "systems_selling_opportunity",
    "deal_price_unknown",
    "integration_risk_flag",
    "leverage_after_mna",
    "policy_support_amount",
    "government_support_flag",
    "reconstruction_contract_flag",
    "budget_allocated_flag",
    "project_delay_flag",
    "financing_failure_flag",
    "opendart_rcept_no",
    "opendart_detail_fetched_flag",
    "disclosure_confidence_score",
    "detail_parser_confidence",
    "disclosure_signal_class",
    "routine_disclosure_flag",
    "risk_disclosure_flag",
    "high_signal_disclosure_flag",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)



def target_for(target_id: str) -> Round155ScoreTarget | None:
    for target in ROUND155_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round155_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND155_CASE_CANDIDATES:
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
                f"Round155 R10 case for {candidate.target_id}; "
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
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "overheat", "4b_watch", "4c_thesis_break", "one_off"} else None,
            score_price_alignment=_score_price_alignment(candidate),
            rerating_result=_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint=_score_weight_hint(target),
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_cross_evidence_for_green",
                "theme_label_is_not_score_evidence",
                "pf_support_or_rate_cut_is_not_green_evidence_alone",
                "backlog_dividend_ai_datacenter_or_reconstruction_headline_is_not_green_evidence_alone",
                "cashflow_occupancy_affo_tenant_power_water_volume_and_funding_cost_required_for_green",
                "do_not_invent_pf_affo_tenant_power_water_volume_cost_or_stage_price_fields",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.7 if candidate.stage1_date or candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.2,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round155_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND155_SCORE_TARGETS:
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
                "loop9_penalty_axes": "|".join(target.loop9_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round155_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND155_CASE_CANDIDATES:
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


def round155_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "red_flags": "|".join(target.red_flags),
            "loop9_penalty_axes": "|".join(target.loop9_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND155_SCORE_TARGETS
    )


def round155_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round155_backfill": "true"} for field in ROUND155_PRICE_FIELDS)


def round155_base_score_axis_rows() -> tuple[dict[str, str], ...]:
    return tuple(axis.as_dict() for axis in ROUND155_BASE_SCORE_AXES)


def round155_stage_cap_rows() -> tuple[dict[str, str], ...]:
    return tuple(cap.as_dict() for cap in ROUND155_STAGE_CAPS)


def round155_summary() -> dict[str, int | bool]:
    records = round155_case_records()
    return {
        "target_count": len(ROUND155_SCORE_TARGETS),
        "base_score_axis_count": len(ROUND155_BASE_SCORE_AXES),
        "stage_cap_count": len(ROUND155_STAGE_CAPS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "one_off_count": sum(1 for record in records if record.case_type == "one_off"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND155_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND155_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND155_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND155_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round155_r10_reports(
    *,
    output_directory: str | Path = ROUND155_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND155_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND155_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round155_r10_loop9_construction_real_estate_materials_summary.md",
        "case_matrix": output / "round155_r10_loop9_case_matrix.csv",
        "stage_date_plan": output / "round155_r10_loop9_stage_date_plan.csv",
        "green_guardrails": output / "round155_r10_loop9_green_guardrails.md",
        "risk_overlays": output / "round155_r10_loop9_risk_overlays.md",
        "price_validation_plan": output / "round155_r10_loop9_price_validation_plan.md",
        "price_fields": output / "round155_r10_loop9_price_fields.csv",
        "base_score_axes": output / "round155_r10_loop9_base_score_axes.csv",
        "stage_caps": output / "round155_r10_loop9_stage_caps.csv",
    }
    _write_case_jsonl(round155_case_records(), cases)
    _write_rows(round155_score_profile_rows(), score_profiles)
    _write_rows(round155_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round155_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round155_price_field_rows(), paths["price_fields"])
    _write_rows(round155_base_score_axis_rows(), paths["base_score_axes"])
    _write_rows(round155_stage_cap_rows(), paths["stage_caps"])
    paths["summary"].write_text(render_round155_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round155_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round155_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round155_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round155_summary_markdown() -> str:
    summary = round155_summary()
    lines = [
        "# Round 155 R10 Loop-9 Construction / Real Estate / Building Materials Summary",
        "",
        "Round 155 is calibration material only. It does not change production scoring.",
        "",
        "## Counts",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Core Rule",
            "",
            "R10 is a credit, cash-flow, occupancy, AFFO, power/water, tenant, and volume round before it is a backlog, dividend, AI data-center, or reconstruction round.",
            "Green requires source-backed PF repair, cash conversion, NOI/AFFO, dividend coverage, tenant lease, power/water access, volume, OPM, or FCF evidence.",
            "",
            "Example: a data-center REIT IPO can be useful Stage 1 evidence. It is not the same as acquired assets, binding tenant lease, NOI/AFFO, power and water access, and dividend coverage.",
            "",
            "## R10 v9 Base Score Axes",
            "",
            "These axes are calibration material only. They document how Round 155 weighs cash-flow conversion before real-estate, data-center, or building-material headlines can become higher-conviction evidence.",
        ]
    )
    for axis in ROUND155_BASE_SCORE_AXES:
        lines.append(f"- {axis.axis_id}: {axis.score_weight}")
    lines.extend(
        [
            "",
            "## R10 v9 Stage Caps",
            "",
            "These caps make the rule explicit: a headline can enter radar, but it cannot become high-conviction evidence until cash-flow, tenant, asset, power/water, volume, leverage, and price-path checks are satisfied.",
        ]
    )
    for cap in ROUND155_STAGE_CAPS:
        lines.append(f"- {cap.cap_id}: {cap.score_cap}")
    return "\n".join(lines) + "\n"


def render_round155_green_guardrail_markdown() -> str:
    lines = [
        "# Round 155 R10 Loop-9 Green Guardrails",
        "",
        "- Do not apply R10 Loop-9 v9.0 weights to production scoring yet.",
        "- Do not use case records as candidate-generation input.",
        "- Do not treat construction backlog, dividend yield, rate-cut expectation, AI data-center label, reconstruction headline, Neom, or local real-estate policy as Green evidence alone.",
        "- Construction Green requires PF exposure reduction, refinancing success, cash conversion, and cost-ratio stability.",
        "- REIT Green requires occupancy, NOI/AFFO, dividend coverage, LTV/funding-cost control, and AFFO integrity.",
        "- Data-center real-asset Green requires acquired assets, binding tenant lease, power/water/grid access, NOI/AFFO, and financing stability.",
        "- Data-center REIT IPOs without acquired assets, binding tenant leases, and NOI/AFFO remain Watch, even with a strong sponsor.",
        "- AI power-campus plans need tenant, permitting, power delivery, financing, and revenue proof before they can move beyond high-risk Watch.",
        "- Local moratorium, zoning pause, referendum, and community opposition cap data-center real-asset promotion.",
        "- Data-center CAPEX must become per-share AFFO and dividend coverage; asset growth alone is not Green evidence.",
        "- Cold-chain warehouse scale is not Green if net loss, debt, energy cost, or occupancy risk is unresolved.",
        "- Building-material Green requires price pass-through, cost control, volume stability, OPM, and FCF.",
        "- Low-carbon cement and building-products M&A need durable premium economics, synergy, margin, FCF, and leverage evidence.",
        "- Disclosure headlines cap Stage 3 until contract, tenant, NOI/AFFO, PF detail, and parser confidence are verified.",
        "- Do not invent PF exposure, NOI/AFFO, dividend coverage, tenant lease, power/water, occupancy, volume, OPM, FCF, green premium, M&A synergy, or stage prices.",
        "",
        "간단한 예시: 정부 PF 지원책은 유동성 충격을 줄일 수 있지만, `refinancing_success_flag`와 `cash_conversion_cycle`이 확인되기 전에는 Stage 1 relief입니다.",
    ]
    return "\n".join(lines) + "\n"


def render_round155_risk_overlay_markdown() -> str:
    lines = [
        "# Round 155 R10 Loop-9 Risk Overlays",
        "",
        "- `PF_CREDIT_REDTEAM_OVERLAY`: PF delinquency, bridge-loan rollover failure, workout, and impairment can block Green.",
        "- `PF_SYNDICATED_LOAN_SOFT_LANDING`: syndicated loan headlines stay Watch until bad projects are separated and cash conversion improves.",
        "- `REIT_AFFO_INTEGRITY_OVERLAY`: AFFO growth and dividend coverage must pass maintenance-capex and capex-burden checks.",
        "- `DATA_CENTER_POWER_WATER_PERMITTING`: power, water, grid interconnection, local opposition, referendum, and withdrawal are hard real-asset gates.",
        "- `DATA_CENTER_LOCAL_OPPOSITION_OVERLAY`: moratorium, zoning pause, and community opposition can delay or break data-center project timing.",
        "- `DATA_CENTER_CAPEX_AFFO_DILUTION`: CAPEX growth above AFFO/share growth can turn AI data-center demand into 4B/4C-watch.",
        "- `COLD_CHAIN_DEBT_OCCUPANCY_RISK`: net loss, energy cost, debt, occupancy decline, and customer inventory normalization can block Green.",
        "- `DATA_CENTER_REIT_IPO_NO_ASSET`: sponsor premium is only Watch until assets, tenants, NOI/AFFO, and power/water are verified.",
        "- `DATA_CENTER_SPONSOR_PREMIUM_PIPELINE`: sponsor track record and pipeline are not cash flow before assets, tenants, and NOI/AFFO.",
        "- `AI_DATA_CENTER_POWER_CAMPUS`: long-dated power-campus narratives remain high-risk Watch without tenant, permitting, financing, and revenue.",
        "- `AI_DATA_CENTER_NO_REVENUE_NO_TENANT`: no revenue, no binding tenant, non-binding LOI, and single-site concentration are gate-level risks.",
        "- `DATA_CENTER_WATER_RIGHTS_REFERENDUM`: water rights, referendum, and local-cost pushback are hard data-center gates.",
        "- `DATA_CENTER_RATEPAYER_UTILITY_COST_OVERLAY`: utility strain and ratepayer-cost backlash can break project timing.",
        "- `BUILDING_MATERIALS_VOLUME_FAILURE`: price hikes and cost cuts are capped when volume and EBITDA are weak.",
        "- `LOW_CARBON_CEMENT_PREMIUM`: pre-sales and CCS are Stage 2 until subsidy durability, green premium, and FCF are proven.",
        "- `BUILDING_PRODUCTS_MNA_SHIFT`: M&A portfolio shift needs accretion, synergy, margin, FCF, and leverage validation.",
        "- `DISCLOSURE_CONFIDENCE_CAP`: contract, tenant, NOI/AFFO, PF detail, and parser confidence gaps cap Stage 3.",
        "",
        "These overlays are diagnostic calibration labels. They are not production score inputs.",
    ]
    return "\n".join(lines) + "\n"


def render_round155_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-155 R10 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Calculate peak price, drawdown after peak, and below-stage3 flag.",
        "6. Compare price paths with PF exposure, unsold inventory, NOI/AFFO, dividend coverage, occupancy, LTV, funding cost, material volumes, price hikes, tenants, power, and contracts.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | stage candidate | check |",
        "| --- | --- | --- |",
    ]
    priority = {
        "korea_pf_delinquency_restructuring_case",
        "korea_builder_support_relief_case",
        "korea_pf_syndicated_loan_soft_landing_case",
        "blackstone_mortgage_trust_dividend_cut_case",
        "blackstone_data_center_reit_ipo_case",
        "fermi_ai_data_center_no_revenue_ipo_case",
        "fermi_no_tenant_net_loss_case",
        "seattle_datacenter_moratorium_case",
        "indianapolis_datacenter_moratorium_case",
        "equinix_ai_revenue_guidance_case",
        "lineage_cold_storage_debt_occupancy_case",
        "heidelberg_materials_price_cost_case",
        "heidelberg_evozero_low_carbon_cement_case",
        "cemex_price_cost_restructuring_case",
        "holcim_xella_building_products_mna_case",
        "holcim_alkern_precast_case",
    }
    for row in round155_case_candidate_rows():
        if row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or row["case_id"] in priority:
            stage_date = row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or row["stage1_date"] or "needs_source_date"
            lines.append(f"| `{row['case_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `policy_relief_rally`: government support or rate-cut expectations move price before credit repair.",
            "- `credit_recovery_aligned`: PF risk, cash flow, and debt structure improve with price.",
            "- `asset_cashflow_aligned`: REIT/real-asset price follows NOI/AFFO, occupancy, and dividend coverage.",
            "- `building_materials_cycle_success`: price/cost/volume alignment works, but cycle risk remains.",
            "- `low_carbon_cement_stage2`: CCS and pre-sales exist, but subsidy durability and green premium are not yet proven.",
            "- `building_products_mna_shift`: portfolio mix can improve, but synergy, margin, leverage, and FCF must be verified.",
            "- `data_center_local_opposition`: local zoning or local opposition risk can delay project timing even when AI demand is real.",
            "- `theme_without_asset`: data-center, reconstruction, Neom, or disaster-rebuild theme lacks assets, tenants, contracts, or financing.",
            "- `thesis_break`: PF delinquency, debt workout, dividend cut, vacancy, impairment, net loss, or refinancing failure breaks the case.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round155CaseCandidate) -> str:
    if "aligned" in candidate.alignment_hint and candidate.case_type in {"structural_success", "success_candidate"}:
        return "aligned"
    if candidate.case_type in {"event_premium", "one_off", "4b_watch"}:
        return "price_moved_without_evidence"
    if candidate.case_type in {"failed_rerating", "4c_thesis_break"}:
        return "false_positive_score"
    return "unknown"


def _rerating_result(candidate: Round155CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "success_candidate":
        if "building_materials" in candidate.alignment_hint:
            return "cyclical_rerating"
        return "unknown"
    if candidate.case_type == "event_premium":
        if "relief" in candidate.alignment_hint:
            return "credit_relief_rally"
        return "event_premium"
    if candidate.case_type == "one_off":
        return "event_premium"
    if candidate.case_type == "4b_watch":
        return "theme_overheat"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "failed_rerating":
        return "no_rerating"
    return "unknown"


def _score_weight_hint(target: Round155ScoreTarget) -> dict[str, float]:
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
    "ROUND155_CASE_CANDIDATES",
    "ROUND155_BASE_SCORE_AXES",
    "ROUND155_DEFAULT_CASES_PATH",
    "ROUND155_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND155_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND155_PRICE_FIELDS",
    "ROUND155_SCORE_TARGETS",
    "ROUND155_SOURCE_ROUND_PATH",
    "Round155CaseCandidate",
    "Round155BaseScoreAxis",
    "Round155ScoreTarget",
    "Round155ScoreWeightDraft",
    "render_round155_green_guardrail_markdown",
    "render_round155_price_validation_plan_markdown",
    "render_round155_risk_overlay_markdown",
    "render_round155_summary_markdown",
    "round155_case_candidate_rows",
    "round155_base_score_axis_rows",
    "round155_case_records",
    "round155_price_field_rows",
    "round155_score_profile_rows",
    "round155_stage_date_rows",
    "round155_summary",
    "target_for",
    "write_round155_r10_reports",
]
