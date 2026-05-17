"""Round-89 R10 Loop-4 construction, real-estate, and building-materials pack.

Round 89 tightens the Round-50 R10 pack. It separates PF relief rallies,
REIT cash-flow quality, AI data-center real assets, cold-chain logistics,
building-material price/cost cycles, and reconstruction policy events.
Backlog, dividend yield, AI data-center labels, and reconstruction headlines
are not Stage 3 evidence unless PF risk, cash conversion, occupancy, NOI/AFFO,
tenant lease, power/water access, volume, OPM, and FCF are source-backed.

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


ROUND89_SOURCE_ROUND_PATH = "docs/round/round_89.md"
ROUND89_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round89_r10_loop4_construction_real_estate_materials"
ROUND89_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop4_round89.jsonl"
ROUND89_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round89_r10_loop4_v4.csv"


@dataclass(frozen=True)
class Round89ScoreWeightDraft:
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
class Round89ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round89ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop4_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round89CaseCandidate:
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


GATE_WEIGHT = Round89ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate")


ROUND89_SCORE_TARGETS: tuple[Round89ScoreTarget, ...] = (
    Round89ScoreTarget(
        "CONSTRUCTION_REAL_ESTATE_CREDIT",
        E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round89ScoreWeightDraft(12, 8, 5, 11, 7, 0, 5),
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
    Round89ScoreTarget(
        "PF_RESTRUCTURING_RELIEF",
        E2RArchetype.PF_RESTRUCTURING_RELIEF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round89ScoreWeightDraft(10, 8, 4, 10, 7, 0, 5),
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
    Round89ScoreTarget(
        "RESIDENTIAL_HOUSING_CYCLE",
        E2RArchetype.RESIDENTIAL_HOUSING_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round89ScoreWeightDraft(15, 12, 5, 12, 9, 1, 5),
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
    Round89ScoreTarget(
        "REIT_DEVELOPMENT_TRUST",
        E2RArchetype.REIT_DEVELOPMENT_TRUST,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round89ScoreWeightDraft(15, 16, 5, 13, 11, 5, 5),
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
    Round89ScoreTarget(
        "COMMERCIAL_REAL_ESTATE_CREDIT",
        E2RArchetype.COMMERCIAL_REAL_ESTATE_CREDIT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round89ScoreWeightDraft(10, 7, 4, 11, 6, 0, 5),
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
    Round89ScoreTarget(
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        E2RArchetype.DATA_CENTER_REIT_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round89ScoreWeightDraft(18, 22, 18, 13, 11, 5, 5),
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
    Round89ScoreTarget(
        "DATA_CENTER_REIT_IPO_NO_ASSET",
        E2RArchetype.DATA_CENTER_REIT_IPO_NO_ASSET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round89ScoreWeightDraft(11, 12, 13, 12, 7, 1, 5),
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
    Round89ScoreTarget(
        "AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT",
        E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round89ScoreWeightDraft(13, 15, 16, 13, 7, 2, 5),
        ("ai_data_center_campus", "dedicated_power_plan", "energy_infra_development"),
        ("binding_tenant_lease", "power_secured", "permitting", "funding_secured"),
        ("revenue_start", "noi_affo", "tenant_contract_quality", "financing_stability"),
        ("pre_revenue_ai_real_asset_valuation_crowded", "long_term_plan_priced_today"),
        ("no_revenue", "no_tenant", "single_site_concentration", "permitting_failure", "funding_gap", "power_or_water_delay"),
        ("binding_tenant_lease", "power_secured", "water_permitting_secured", "revenue_start", "noi_affo"),
        ("pre_revenue", "single_site", "permitting", "funding", "power_water", "tenant_missing"),
        ("pre_revenue", "tenant", "power_water", "permitting", "funding"),
        "AI data-center real-asset development stays high-risk Watch until lease, power/water, revenue, NOI/AFFO, and financing are proven.",
    ),
    Round89ScoreTarget(
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
    Round89ScoreTarget(
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
    Round89ScoreTarget(
        "COLD_CHAIN_REIT_LOGISTICS",
        E2RArchetype.COLD_CHAIN_REIT_LOGISTICS,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round89ScoreWeightDraft(17, 19, 12, 12, 10, 5, 5),
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
    Round89ScoreTarget(
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
    Round89ScoreTarget(
        "BUILDING_MATERIALS_PRICE_COST",
        E2RArchetype.BUILDING_MATERIALS_PRICE_COST,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round89ScoreWeightDraft(18, 15, 12, 11, 10, 3, 5),
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
    Round89ScoreTarget(
        "BUILDING_MATERIALS_VOLUME_FAILURE",
        E2RArchetype.BUILDING_MATERIALS_VOLUME_FAILURE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round89ScoreWeightDraft(13, 9, 8, 8, 6, 1, 5),
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
    Round89ScoreTarget(
        "INFRA_RECONSTRUCTION_POLICY",
        E2RArchetype.INFRA_RECONSTRUCTION_POLICY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round89ScoreWeightDraft(10, 8, 8, 10, 7, 0, 4),
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
    Round89ScoreTarget(
        "POLICY_LOCAL_REAL_ESTATE_THEME",
        E2RArchetype.POLICY_LOCAL_REAL_ESTATE_THEME,
        Round10ThemePosture.REDTEAM_FIRST,
        Round89ScoreWeightDraft(5, 5, 4, 8, 5, 0, 3),
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
    Round89ScoreTarget(
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
    Round89ScoreTarget(
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
    Round89ScoreTarget(
        "AI_INFRA_REAL_ASSET_THEME_OVERLAY",
        E2RArchetype.AI_INFRA_REAL_ASSET_THEME_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("ai_data_center_theme", "space_or_power_narrative", "pre_revenue_real_asset"),
        ("asset_acquired", "binding_tenant_lease", "revenue_start"),
        ("noi_affo_visible", "power_water_secured", "financing_stable"),
        ("ai_real_asset_theme_valuation_crowded",),
        ("no_revenue", "no_assets", "no_binding_tenant", "single_site_concentration", "funding_gap"),
        ("asset_acquired_flag", "binding_lease_flag", "revenue_recognized_flag"),
        ("no_revenue", "no_asset", "no_tenant", "single_site", "funding_gap"),
        ("asset", "tenant", "revenue", "funding"),
        "AI infrastructure real-asset themes are gate-only until asset, tenant, revenue, and financing are source-backed.",
        gate_only=True,
    ),
)



ROUND89_CASE_CANDIDATES: tuple[Round89CaseCandidate, ...] = (
    Round89CaseCandidate(
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
    Round89CaseCandidate(
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
    Round89CaseCandidate(
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
    Round89CaseCandidate(
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
    Round89CaseCandidate(
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
    Round89CaseCandidate(
        "equinix_malaysia_ai_liquid_cooling_case",
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        "EQIX",
        "Equinix Malaysia AI liquid-cooling expansion",
        "US",
        "success_candidate",
        date(2026, 5, 12),
        date(2026, 5, 12),
        None,
        date(2026, 5, 12),
        None,
        ("advanced_liquid_cooling_flag", "data_center_asset_pipeline", "power_secured_flag", "water_permitting_flag"),
        ("power_grid_constraint", "water_resource_constraint", "ai_chip_access_geopolitics", "capex_burden"),
        "data_center_demand_real_but_power_water_gate",
        "needs_price_backfill",
        ("round_89.md Reuters Equinix Malaysia data centre",),
        "AI/HPC demand is real, but power, water, grid access, and AFFO per share remain Stage gates.",
    ),
    Round89CaseCandidate(
        "blackstone_data_center_reit_flat_debut_case",
        "DATA_CENTER_REIT_IPO_NO_ASSET",
        "BLACKSTONE_DC_REIT",
        "Blackstone Digital Infrastructure Trust flat debut",
        "US",
        "failed_rerating",
        date(2026, 5, 14),
        None,
        None,
        date(2026, 5, 14),
        None,
        ("ai_data_center_reit_ipo", "hyperscale_tenant_target", "asset_pipeline"),
        ("no_acquired_assets", "no_affo", "tenant_lease_missing"),
        "data_center_reit_theme_without_assets_yet",
        "needs_price_backfill",
        ("Reuters Blackstone data center vehicle makes muted debut",),
        "Sponsor and AI infrastructure demand are not enough before assets, tenants, NOI/AFFO, and power/water are verified.",
    ),
    Round89CaseCandidate(
        "fermi_ai_data_center_no_revenue_case",
        "AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT",
        "FRMI",
        "Fermi AI data-center no-revenue project",
        "US",
        "4b_watch",
        date(2025, 9, 30),
        None,
        None,
        date(2025, 9, 30),
        None,
        ("ai_data_center_campus", "power_pipeline", "asset_pipeline_value"),
        ("no_revenue", "funding_gap", "tenant_missing", "single_site_concentration"),
        "ai_real_asset_no_revenue_high_risk_watch",
        "needs_price_backfill",
        ("Reuters Fermi REIT raises $682 million in U.S. IPO",),
        "Pre-revenue AI real-asset mega-project valuation is 4B-watch, not Green.",
        (E2RArchetype.AI_INFRA_REAL_ASSET_THEME_OVERLAY,),
    ),
    Round89CaseCandidate(
        "fermi_no_tenant_net_loss_case",
        "AI_INFRA_REAL_ASSET_THEME_OVERLAY",
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
        ("no_binding_tenant_lease", "net_loss_flag", "funding_agreement_terminated", "single_site_concentration_flag"),
        "ai_real_asset_no_revenue_high_risk",
        "needs_price_backfill",
        ("round_89.md FT Fermi shares plunge on net loss",),
        "AI real-asset stories break when tenant lease, revenue, and funding remain unproven after valuation has moved.",
        (E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT,),
    ),
    Round89CaseCandidate(
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
    Round89CaseCandidate(
        "utah_stratos_datacenter_backlash_case",
        "DATA_CENTER_POWER_WATER_PERMITTING",
        "UTAH_STRATOS_DC",
        "Utah Stratos AI data-center backlash",
        "US",
        "4b_watch",
        date(2026, 5, 13),
        None,
        None,
        date(2026, 5, 13),
        None,
        ("power_demand_gw", "water_permitting_flag", "referendum_or_moratorium_flag"),
        ("water_rights_delay", "grid_interconnection_delay", "referendum_or_moratorium"),
        "data_center_power_water_4b_watch",
        "needs_price_backfill",
        ("Guardian Utah approves datacenter amid backlash",),
        "A 9GW data-center plan can be a 4B-watch when power and water backlash are not resolved.",
    ),
    Round89CaseCandidate(
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
    Round89CaseCandidate(
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
    Round89CaseCandidate(
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
    Round89CaseCandidate(
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
    Round89CaseCandidate(
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
        ("round_89.md Reuters Cemex core earnings increase but volumes weak",),
        "Price/cost improvement can support Watch, but flat cement volume and ready-mix/aggregate weakness keep Green capped.",
        (E2RArchetype.BUILDING_MATERIALS_VOLUME_FAILURE,),
    ),
    Round89CaseCandidate(
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
        ("Round89 analyst matrix",),
        "Reconstruction policy needs funded contracts and supplier margin evidence before Green.",
    ),
    Round89CaseCandidate(
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
        ("Round89 analyst matrix",),
        "Neom-related theme labels remain Event/Watch until actual contract economics are visible.",
    ),
    Round89CaseCandidate(
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
        ("Round89 analyst matrix",),
        "Local real-estate policy themes remain Stage 1 until budget, contract, and revenue recognition are visible.",
    ),
)



ROUND89_PRICE_FIELDS: tuple[str, ...] = (
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
    "no_revenue_flag",
    "single_site_concentration_flag",
    "power_delivery_date",
    "local_opposition_flag",
    "referendum_or_moratorium_flag",
    "project_withdrawal_flag",
    "noise_pollution_flag",
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
    "policy_support_amount",
    "government_support_flag",
    "reconstruction_contract_flag",
    "budget_allocated_flag",
    "project_delay_flag",
    "financing_failure_flag",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)



def target_for(target_id: str) -> Round89ScoreTarget | None:
    for target in ROUND89_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round89_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND89_CASE_CANDIDATES:
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
                f"Round89 R10 case for {candidate.target_id}; "
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


def round89_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND89_SCORE_TARGETS:
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
                "loop4_penalty_axes": "|".join(target.loop4_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round89_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND89_CASE_CANDIDATES:
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


def round89_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "red_flags": "|".join(target.red_flags),
            "loop4_penalty_axes": "|".join(target.loop4_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND89_SCORE_TARGETS
    )


def round89_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round89_backfill": "true"} for field in ROUND89_PRICE_FIELDS)


def round89_summary() -> dict[str, int | bool]:
    records = round89_case_records()
    return {
        "target_count": len(ROUND89_SCORE_TARGETS),
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
        "green_possible_count": sum(1 for target in ROUND89_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND89_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND89_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND89_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round89_r10_reports(
    *,
    output_directory: str | Path = ROUND89_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND89_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND89_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round89_r10_loop4_construction_real_estate_materials_summary.md",
        "case_matrix": output / "round89_r10_loop4_case_matrix.csv",
        "stage_date_plan": output / "round89_r10_loop4_stage_date_plan.csv",
        "green_guardrails": output / "round89_r10_loop4_green_guardrails.md",
        "risk_overlays": output / "round89_r10_loop4_risk_overlays.md",
        "price_validation_plan": output / "round89_r10_loop4_price_validation_plan.md",
        "price_fields": output / "round89_r10_loop4_price_fields.csv",
    }
    _write_case_jsonl(round89_case_records(), cases)
    _write_rows(round89_score_profile_rows(), score_profiles)
    _write_rows(round89_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round89_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round89_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round89_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round89_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round89_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round89_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round89_summary_markdown() -> str:
    summary = round89_summary()
    lines = [
        "# Round 89 R10 Loop-4 Construction / Real Estate / Building Materials Summary",
        "",
        "Round 89 is calibration material only. It does not change production scoring.",
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
        ]
    )
    return "\n".join(lines) + "\n"


def render_round89_green_guardrail_markdown() -> str:
    lines = [
        "# Round 89 R10 Loop-4 Green Guardrails",
        "",
        "- Do not apply R10 Loop-4 v4.0 weights to production scoring yet.",
        "- Do not use case records as candidate-generation input.",
        "- Do not treat construction backlog, dividend yield, rate-cut expectation, AI data-center label, reconstruction headline, Neom, or local real-estate policy as Green evidence alone.",
        "- Construction Green requires PF exposure reduction, refinancing success, cash conversion, and cost-ratio stability.",
        "- REIT Green requires occupancy, NOI/AFFO, dividend coverage, LTV/funding-cost control, and AFFO integrity.",
        "- Data-center real-asset Green requires acquired assets, binding tenant lease, power/water/grid access, NOI/AFFO, and financing stability.",
        "- Data-center REIT IPOs without acquired assets, binding tenant leases, and NOI/AFFO remain Watch, even with a strong sponsor.",
        "- Data-center CAPEX must become per-share AFFO and dividend coverage; asset growth alone is not Green evidence.",
        "- Cold-chain warehouse scale is not Green if net loss, debt, energy cost, or occupancy risk is unresolved.",
        "- Building-material Green requires price pass-through, cost control, volume stability, OPM, and FCF.",
        "- Do not invent PF exposure, NOI/AFFO, dividend coverage, tenant lease, power/water, occupancy, volume, OPM, FCF, or stage prices.",
        "",
        "간단한 예시: 정부 PF 지원책은 유동성 충격을 줄일 수 있지만, `refinancing_success_flag`와 `cash_conversion_cycle`이 확인되기 전에는 Stage 1 relief입니다.",
    ]
    return "\n".join(lines) + "\n"


def render_round89_risk_overlay_markdown() -> str:
    lines = [
        "# Round 89 R10 Loop-4 Risk Overlays",
        "",
        "- `PF_CREDIT_REDTEAM_OVERLAY`: PF delinquency, bridge-loan rollover failure, workout, and impairment can block Green.",
        "- `REIT_AFFO_INTEGRITY_OVERLAY`: AFFO growth and dividend coverage must pass maintenance-capex and capex-burden checks.",
        "- `DATA_CENTER_POWER_WATER_PERMITTING`: power, water, grid interconnection, local opposition, referendum, and withdrawal are hard real-asset gates.",
        "- `DATA_CENTER_CAPEX_AFFO_DILUTION`: CAPEX growth above AFFO/share growth can turn AI data-center demand into 4B/4C-watch.",
        "- `COLD_CHAIN_DEBT_OCCUPANCY_RISK`: net loss, energy cost, debt, occupancy decline, and customer inventory normalization can block Green.",
        "- `DATA_CENTER_REIT_IPO_NO_ASSET`: sponsor premium is only Watch until assets, tenants, NOI/AFFO, and power/water are verified.",
        "- `AI_INFRA_REAL_ASSET_THEME_OVERLAY`: no asset, no binding tenant, no revenue, and single-site concentration keep AI real-asset themes Watch/Red.",
        "- `BUILDING_MATERIALS_VOLUME_FAILURE`: price hikes and cost cuts are capped when volume and EBITDA are weak.",
        "",
        "These overlays are diagnostic calibration labels. They are not production score inputs.",
    ]
    return "\n".join(lines) + "\n"


def render_round89_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-89 R10 Price Validation Plan",
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
        "blackstone_mortgage_trust_dividend_cut_case",
        "blackstone_data_center_reit_flat_debut_case",
        "fermi_ai_data_center_no_revenue_case",
        "fermi_no_tenant_net_loss_case",
        "equinix_malaysia_ai_liquid_cooling_case",
        "lineage_cold_storage_debt_occupancy_case",
        "heidelberg_materials_price_cost_case",
        "cemex_price_cost_restructuring_case",
    }
    for row in round89_case_candidate_rows():
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
            "- `theme_without_asset`: data-center, reconstruction, Neom, or disaster-rebuild theme lacks assets, tenants, contracts, or financing.",
            "- `thesis_break`: PF delinquency, debt workout, dividend cut, vacancy, impairment, net loss, or refinancing failure breaks the case.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round89CaseCandidate) -> str:
    if "aligned" in candidate.alignment_hint and candidate.case_type in {"structural_success", "success_candidate"}:
        return "aligned"
    if candidate.case_type in {"event_premium", "one_off", "4b_watch"}:
        return "price_moved_without_evidence"
    if candidate.case_type in {"failed_rerating", "4c_thesis_break"}:
        return "false_positive_score"
    return "unknown"


def _rerating_result(candidate: Round89CaseCandidate) -> str:
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


def _score_weight_hint(target: Round89ScoreTarget) -> dict[str, float]:
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
    "ROUND89_CASE_CANDIDATES",
    "ROUND89_DEFAULT_CASES_PATH",
    "ROUND89_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND89_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND89_PRICE_FIELDS",
    "ROUND89_SCORE_TARGETS",
    "ROUND89_SOURCE_ROUND_PATH",
    "Round89CaseCandidate",
    "Round89ScoreTarget",
    "Round89ScoreWeightDraft",
    "render_round89_green_guardrail_markdown",
    "render_round89_price_validation_plan_markdown",
    "render_round89_risk_overlay_markdown",
    "render_round89_summary_markdown",
    "round89_case_candidate_rows",
    "round89_case_records",
    "round89_price_field_rows",
    "round89_score_profile_rows",
    "round89_stage_date_rows",
    "round89_summary",
    "target_for",
    "write_round89_r10_reports",
]
