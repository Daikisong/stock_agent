"""Round-50 R10 construction, real-estate, and building-materials pack.

Round 50 makes R10 a RedTeam-first calibration pack. The core rule is simple:
construction backlog, asset value, dividend yield, or reconstruction policy is
not enough for Stage 3-Green. PF risk, cash flow, cost ratio, occupancy,
NOI/AFFO, dividend coverage, funding cost, and real contracts or tenants must
be checked first.

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


ROUND50_SOURCE_ROUND_PATH = "docs/round/round_50.md"
ROUND50_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round50_r10_construction_real_estate_materials"
ROUND50_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_round50.jsonl"
ROUND50_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round50_r10_v1.csv"


@dataclass(frozen=True)
class Round50ScoreWeightDraft:
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
class Round50ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round50ScoreWeightDraft
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
        return Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round50CaseCandidate:
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


ROUND50_SCORE_TARGETS: tuple[Round50ScoreTarget, ...] = (
    Round50ScoreTarget(
        "CONSTRUCTION_REAL_ESTATE_CREDIT",
        E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round50ScoreWeightDraft(14, 10, 5, 12, 9, 0, 5),
        ("pf_support", "rate_cut_expectation", "property_recovery_news"),
        ("refinancing_success", "unsold_inventory_decline", "cash_flow_improvement", "cost_ratio_stable"),
        ("pf_risk_reduced", "eps_fcf_recovery", "valuation_frame_change"),
        ("pf_relief_rally_crowded", "support_news_priced_before_restructuring"),
        ("pf_delinquency_increase", "bridge_loan_rollover_failure", "debt_workout", "impairment"),
        ("refinancing_success", "cash_flow_improvement", "unsold_inventory_decline", "cost_ratio_stable"),
        ("pf_exposure", "unsold_inventory", "refinancing", "construction_cost_ratio", "debt_workout"),
        "Government support is Stage 1 relief until PF, cash flow, and cost risks improve.",
    ),
    Round50ScoreTarget(
        "REIT_DEVELOPMENT_TRUST",
        E2RArchetype.REIT_DEVELOPMENT_TRUST,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round50ScoreWeightDraft(15, 16, 5, 13, 11, 5, 5),
        ("rate_cut_expectation", "dividend_yield", "nav_discount"),
        ("occupancy", "noi_affo", "dividend_coverage", "ltv_stable"),
        ("affo_growth", "dividend_sustainability", "nav_discount_narrowing"),
        ("high_yield_reit_rally_crowded", "rate_cut_priced"),
        ("vacancy_increase", "ltv_deterioration", "refinancing_failure", "dividend_cut"),
        ("occupancy", "noi_affo", "dividend_coverage", "ltv_stable", "funding_cost_controlled"),
        ("vacancy", "ltv", "refinancing", "dividend_cut", "funding_cost"),
        "REIT/development-trust cases need asset cash flow and dividend coverage, not yield alone.",
    ),
    Round50ScoreTarget(
        "BUILDING_MATERIALS_CYCLE",
        E2RArchetype.BUILDING_MATERIALS_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round50ScoreWeightDraft(17, 13, 12, 10, 9, 3, 5),
        ("price_hike", "cost_stabilization", "housing_starts_recovery"),
        ("volume_recovery", "opm_improvement", "cost_pass_through", "energy_cost_control"),
        ("fcf_stability", "volume_and_price_aligned", "infrastructure_demand_visible"),
        ("building_material_price_hike_crowded", "infrastructure_spend_priced"),
        ("volume_decline", "energy_cost_spike", "raw_material_cost_spike", "construction_slowdown"),
        ("volume_recovery", "price_hike", "cost_pass_through", "opm_improvement", "fcf_stability"),
        ("volume_decline", "energy_cost", "raw_material_cost", "construction_slowdown"),
        "Building materials can work on price/cost alignment, but starts and volume must confirm.",
    ),
    Round50ScoreTarget(
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        E2RArchetype.DATA_CENTER_REIT_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round50ScoreWeightDraft(18, 23, 18, 13, 13, 5, 5),
        ("ai_data_center_reit_ipo", "hyperscale_demand", "asset_pipeline"),
        ("asset_acquisition", "tenant_lease", "power_cooling_secured", "noi_affo"),
        ("affo_growth", "dividend_coverage", "tenant_contract_quality", "funding_cost_controlled"),
        ("ai_infrastructure_reit_valuation_crowded", "capex_pipeline_priced_before_cashflow"),
        ("no_acquired_assets", "no_tenant", "no_affo", "power_or_water_permitting_failure", "funding_cost_up"),
        ("asset_acquisition", "hyperscale_tenant", "noi_affo", "dividend_coverage", "power_secured"),
        ("no_assets", "tenant_concentration", "capex", "funding_cost", "power_water_permitting"),
        "Data-center REIT Green requires assets, tenants, power/cooling, and AFFO.",
    ),
    Round50ScoreTarget(
        "COLD_CHAIN_REIT_LOGISTICS",
        E2RArchetype.COLD_CHAIN_REIT_LOGISTICS,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round50ScoreWeightDraft(17, 21, 12, 12, 11, 5, 5),
        ("cold_storage_ipo", "food_pharma_cold_chain_demand"),
        ("occupancy", "customer_contract", "noi_affo", "energy_cost_control"),
        ("repeat_logistics_demand", "dividend_coverage", "affo_visibility"),
        ("cold_chain_reit_premium_crowded",),
        ("net_loss", "energy_cost_pressure", "occupancy_decline", "debt_burden"),
        ("occupancy", "customer_count", "noi_affo", "energy_cost_control", "dividend_coverage"),
        ("net_loss", "energy_cost", "debt", "occupancy", "affo_uncertainty"),
        "Cold-chain scale is useful only when NOI/AFFO and energy/debt risks are controlled.",
    ),
    Round50ScoreTarget(
        "INFRA_RECONSTRUCTION_POLICY",
        E2RArchetype.INFRA_RECONSTRUCTION_POLICY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round50ScoreWeightDraft(12, 10, 8, 10, 8, 0, 4),
        ("ukraine_reconstruction", "neom_city", "overseas_infra_policy", "disaster_recovery_policy"),
        ("actual_contract", "financing_secured", "construction_started", "revenue_recognition"),
        ("multi_year_backlog", "contract_margin_visible", "delivery_schedule"),
        ("policy_theme_crowded", "reconstruction_basket_rally_before_contract"),
        ("project_cancellation", "financing_failure", "geopolitical_setback", "project_delay"),
        ("actual_contract", "financing_secured", "contract_margin_visible", "delivery_schedule"),
        ("no_actual_contract", "financing", "policy_event_only", "project_delay"),
        "Reconstruction policy is Event/Watch until funded contracts and margin evidence exist.",
    ),
    Round50ScoreTarget(
        "DISASTER_REBUILD_EVENT",
        E2RArchetype.DISASTER_REBUILD_EVENT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round50ScoreWeightDraft(10, 6, 7, 8, 6, 0, 4),
        ("earthquake_rebuild", "flood_rebuild", "short_term_material_demand"),
        ("actual_order", "sell_through", "margin_visibility"),
        ("repeat_order_visibility", "fcf_after_event"),
        ("disaster_rebuild_theme_crowded",),
        ("one_off_demand_normalization", "inventory_build", "margin_reversal"),
        ("actual_order", "margin_visibility", "repeat_demand"),
        ("one_off_demand", "inventory", "margin_reversal", "policy_event_only"),
        "Disaster rebuild is one-off demand unless repeat orders and margins are source-backed.",
    ),
    Round50ScoreTarget(
        "COMMERCIAL_REAL_ESTATE_CREDIT",
        E2RArchetype.COMMERCIAL_REAL_ESTATE_CREDIT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round50ScoreWeightDraft(12, 9, 4, 12, 8, 0, 5),
        ("office_recovery_news", "cre_credit_relief", "rate_cut_expectation"),
        ("vacancy_stabilization", "credit_loss_reserve_stable", "dividend_coverage"),
        ("loan_quality_recovery", "occupancy_recovery", "dividend_sustainability"),
        ("cre_relief_rally_before_credit_repair",),
        ("office_vacancy", "watchlisted_or_impaired_loan", "credit_loss_reserve", "dividend_cut"),
        ("vacancy_stabilization", "loan_quality_recovery", "dividend_coverage"),
        ("office_exposure", "vacancy", "impaired_asset", "credit_loss_reserve", "dividend_cut"),
        "Commercial real-estate credit is RedTeam-first because vacancy and loan losses can break yield stories.",
    ),
    Round50ScoreTarget(
        "RESIDENTIAL_HOUSING_CYCLE",
        E2RArchetype.RESIDENTIAL_HOUSING_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round50ScoreWeightDraft(15, 12, 5, 12, 9, 1, 5),
        ("housing_recovery", "rate_cut_expectation", "presale_recovery"),
        ("unsold_inventory_decline", "starts_recovery", "cost_ratio_stable"),
        ("cash_flow_recovery", "eps_fcf_recovery", "credit_risk_low"),
        ("housing_cycle_rally_crowded",),
        ("unsold_inventory_increase", "household_debt_stress", "starts_decline", "rate_shock"),
        ("unsold_inventory_decline", "cost_ratio_stable", "cash_flow_recovery", "credit_risk_low"),
        ("unsold_inventory", "household_debt", "rate", "construction_cost", "starts_decline"),
        "Housing-cycle improvement is Watch until inventory, cost, and cash conversion are visible.",
    ),
    Round50ScoreTarget(
        "AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT",
        E2RArchetype.AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round50ScoreWeightDraft(16, 18, 15, 13, 10, 3, 5),
        ("ai_data_center_campus", "power_pipeline", "energy_infra_development"),
        ("tenant_lease", "power_secured", "permitting", "funding_secured"),
        ("revenue_start", "affo_or_cashflow", "tenant_contract_quality"),
        ("pre_revenue_ai_real_asset_valuation_crowded",),
        ("no_revenue", "no_tenant", "permitting_failure", "funding_gap", "power_or_water_delay"),
        ("tenant_lease", "power_secured", "funding_secured", "revenue_start"),
        ("pre_revenue", "permitting", "funding", "power_water", "tenant_missing"),
        "AI real-asset development can become interesting, but pre-revenue mega-projects stay Green-blocked.",
    ),
)


ROUND50_CASE_CANDIDATES: tuple[Round50CaseCandidate, ...] = (
    Round50CaseCandidate(
        "korea_pf_delinquency_restructuring_case",
        "CONSTRUCTION_REAL_ESTATE_CREDIT",
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
    ),
    Round50CaseCandidate(
        "korea_builder_support_relief_case",
        "CONSTRUCTION_REAL_ESTATE_CREDIT",
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
        "policy_relief_rally_not_structural_success",
        "needs_price_backfill",
        ("Reuters Korea prepares financial support for builders",),
        "Government support is Stage 1 relief; Stage 2 needs refinancing and cash-flow proof.",
    ),
    Round50CaseCandidate(
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
        "commercial_re_credit_4c",
        "needs_price_backfill",
        ("Reuters Blackstone mortgage fund slumps as empty offices intensify pressure",),
        "Dividend cut after office credit stress is a hard CRE credit 4C example.",
    ),
    Round50CaseCandidate(
        "blackstone_data_center_reit_flat_debut_case",
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        "BLACKSTONE_DC_REIT",
        "Blackstone Digital Infrastructure Trust flat debut",
        "US",
        "failed_rerating",
        date(2026, 5, 14),
        None,
        None,
        None,
        None,
        ("ai_data_center_reit_ipo", "hyperscale_tenant_target"),
        ("no_acquired_assets", "no_affo", "funding_cost"),
        "theme_without_asset",
        "needs_price_backfill",
        ("Reuters Blackstone data center vehicle makes muted debut",),
        "A data-center REIT label needs acquired assets, tenants, and AFFO before Stage 3.",
    ),
    Round50CaseCandidate(
        "ntt_dc_reit_tepid_debut_case",
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        "NTT_DC_REIT",
        "NTT DC REIT tepid debut",
        "SG",
        "success_candidate",
        date(2025, 7, 14),
        date(2025, 7, 14),
        None,
        None,
        None,
        ("data_center_assets", "tenant_contract", "reit_ipo"),
        ("funding_cost", "affo_unverified"),
        "mild_price_alignment_no_explosive_rerating",
        "needs_price_backfill",
        ("Reuters NTT DC REIT tepid debut",),
        "Even with assets, data-center REITs need AFFO, tenant quality, and rate checks.",
    ),
    Round50CaseCandidate(
        "fermi_ai_data_center_reit_case",
        "AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT",
        "FRMI",
        "Fermi AI data-center real-asset project",
        "US",
        "4b_watch",
        date(2025, 9, 30),
        None,
        None,
        date(2025, 9, 30),
        None,
        ("ai_data_center_campus", "power_pipeline", "asset_pipeline_value"),
        ("pre_revenue", "funding_gap", "permitting", "power_water_delay"),
        "ai_infra_real_asset_high_risk_watch",
        "needs_price_backfill",
        ("Reuters Fermi REIT raises $682 million in U.S. IPO",),
        "Pre-revenue AI real-asset mega-project valuation is 4B-watch, not Green.",
    ),
    Round50CaseCandidate(
        "lineage_cold_storage_reit_ipo_case",
        "COLD_CHAIN_REIT_LOGISTICS",
        "LINE",
        "Lineage cold-storage REIT IPO",
        "US",
        "success_candidate",
        date(2024, 7, 24),
        date(2024, 7, 24),
        None,
        None,
        None,
        ("cold_storage_warehouse_count", "customer_count", "temperature_controlled_logistics"),
        ("net_loss", "energy_cost", "debt", "affo_uncertainty"),
        "cold_chain_scale_success_candidate_but_profitability_watch",
        "needs_price_backfill",
        ("Reuters Lineage raises $4.44 bln in biggest IPO of 2024",),
        "Scale and customer count help, but net loss and AFFO uncertainty keep Green restricted.",
    ),
    Round50CaseCandidate(
        "heidelberg_materials_price_cost_case",
        "BUILDING_MATERIALS_CYCLE",
        "HEI.DE",
        "Heidelberg Materials price-cost alignment",
        "EU",
        "success_candidate",
        date(2025, 11, 6),
        date(2025, 11, 6),
        None,
        date(2026, 2, 25),
        None,
        ("price_hike", "cost_saving_amount", "opm_improvement", "infrastructure_demand"),
        ("volume_decline", "energy_cost", "construction_slowdown"),
        "building_materials_price_cost_aligned_candidate",
        "needs_price_backfill",
        ("Reuters Heidelberg Materials higher Q3 profit on cost and price management",),
        "Building materials can be Watch-to-Green when price, cost, OPM, and demand align.",
    ),
    Round50CaseCandidate(
        "cemex_demand_slowdown_price_offset_case",
        "BUILDING_MATERIALS_CYCLE",
        "CEMEX",
        "Cemex demand slowdown and price-offset limit",
        "MX",
        "4c_thesis_break",
        date(2025, 2, 6),
        None,
        None,
        None,
        date(2025, 2, 6),
        ("price_hike", "cost_saving_amount"),
        ("volume_decline", "demand_slowdown", "price_increase_not_enough"),
        "building_materials_demand_slowdown_mixed_case",
        "needs_price_backfill",
        ("Reuters Cemex sales decline and savings program",),
        "Price increases cannot offset weak volumes forever; volume and FCF must be checked.",
    ),
    Round50CaseCandidate(
        "ukraine_reconstruction_event_watch_case",
        "INFRA_RECONSTRUCTION_POLICY",
        "UKRAINE_REBUILD_BASKET",
        "Ukraine reconstruction event watch",
        "GLOBAL",
        "event_premium",
        None,
        None,
        None,
        None,
        None,
        ("reconstruction_policy", "infrastructure_theme"),
        ("no_actual_contract", "financing", "geopolitical_setback"),
        "actual_contract_before_green",
        "needs_price_backfill",
        ("Round50 analyst matrix",),
        "Reconstruction policy needs funded contracts and supplier margin evidence before Green.",
    ),
    Round50CaseCandidate(
        "neom_city_event_watch_case",
        "INFRA_RECONSTRUCTION_POLICY",
        "NEOM_POLICY_BASKET",
        "Neom city event watch",
        "GLOBAL",
        "event_premium",
        None,
        None,
        None,
        None,
        None,
        ("neom_city", "policy_theme", "infrastructure_theme"),
        ("no_actual_contract", "financing", "project_delay"),
        "actual_contract_before_green",
        "needs_price_backfill",
        ("Round50 analyst matrix",),
        "Neom-related theme labels remain Event/Watch until actual contract economics are visible.",
    ),
    Round50CaseCandidate(
        "disaster_rebuild_materials_event_case",
        "DISASTER_REBUILD_EVENT",
        "DISASTER_REBUILD_BASKET",
        "Disaster rebuild materials event basket",
        "GLOBAL",
        "one_off",
        None,
        None,
        None,
        None,
        None,
        ("disaster_rebuild_event", "short_term_material_demand"),
        ("one_off_demand", "inventory_build", "margin_reversal"),
        "one_off_rebuild_event_not_structural",
        "needs_price_backfill",
        ("Round50 analyst matrix",),
        "Disaster rebuild demand can create Stage 1, but recurrence and margins are required for more.",
    ),
)


ROUND50_PRICE_FIELDS: tuple[str, ...] = (
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
    "revenue_backlog",
    "contract_value",
    "contract_duration",
    "contract_margin_signal",
    "reit_type",
    "occupancy_rate",
    "noi_growth",
    "affo_growth",
    "ffo_growth",
    "dividend_per_share",
    "dividend_cut_flag",
    "dividend_coverage_ratio",
    "ltv_ratio",
    "funding_cost",
    "refinancing_maturity",
    "office_exposure",
    "watchlisted_or_impaired_asset_ratio",
    "building_material_volume",
    "cement_price_change",
    "steel_rebar_price_change",
    "energy_cost_change",
    "raw_material_cost_change",
    "price_hike_flag",
    "cost_saving_amount",
    "data_center_asset_acquired_flag",
    "hyperscale_tenant_flag",
    "tenant_concentration",
    "power_secured_flag",
    "water_permitting_flag",
    "capex_amount",
    "asset_pipeline_value",
    "ai_infra_theme_flag",
    "cold_storage_warehouse_count",
    "cold_storage_capacity",
    "energy_cost_ratio",
    "customer_count",
    "net_loss_flag",
    "policy_support_amount",
    "government_support_flag",
    "reconstruction_contract_flag",
    "financing_secured_flag",
    "project_delay_flag",
    "score_price_alignment",
    "price_validation_status",
)


def target_for(target_id: str) -> Round50ScoreTarget | None:
    for target in ROUND50_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round50_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND50_CASE_CANDIDATES:
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
                f"Round50 R10 case for {candidate.target_id}; "
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
                "pf_support_or_rate_cut_is_not_green_evidence_alone",
                "asset_yield_or_backlog_is_not_green_evidence_alone",
                "cashflow_occupancy_affo_and_funding_cost_required_for_green",
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


def round50_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND50_SCORE_TARGETS:
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


def round50_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND50_CASE_CANDIDATES:
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


def round50_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "production_scoring_changed": "false",
        }
        for target in ROUND50_SCORE_TARGETS
    )


def round50_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round50_backfill": "true"} for field in ROUND50_PRICE_FIELDS)


def round50_summary() -> dict[str, int | bool]:
    records = round50_case_records()
    return {
        "target_count": len(ROUND50_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "one_off_count": sum(1 for record in records if record.case_type == "one_off"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch"),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND50_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND50_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND50_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round50_r10_reports(
    *,
    output_directory: str | Path = ROUND50_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND50_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND50_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round50_r10_construction_real_estate_materials_summary.md",
        "case_matrix": output / "round50_r10_case_matrix.csv",
        "stage_date_plan": output / "round50_r10_stage_date_plan.csv",
        "green_guardrails": output / "round50_r10_green_guardrails.md",
        "credit_asset_caps": output / "round50_r10_credit_asset_caps.md",
        "price_validation_plan": output / "round50_r10_price_validation_plan.md",
        "price_fields": output / "round50_r10_price_fields.csv",
    }
    _write_case_jsonl(round50_case_records(), cases)
    _write_rows(round50_score_profile_rows(), score_profiles)
    _write_rows(round50_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round50_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round50_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round50_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round50_green_guardrail_markdown(), encoding="utf-8")
    paths["credit_asset_caps"].write_text(render_round50_credit_asset_cap_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round50_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round50_summary_markdown() -> str:
    summary = round50_summary()
    lines = [
        "# Round-50 R10 Construction / Real Estate / Building Materials Summary",
        "",
        f"- source_round: `{ROUND50_SOURCE_ROUND_PATH}`",
        "- large_sector: `CONSTRUCTION_REAL_ESTATE_MATERIALS`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R10 is a credit, cash-flow, occupancy, AFFO, and funding-cost round before it is a backlog or asset round.",
        "- Example: PF support news is Stage 1 relief until refinancing, unsold inventory, cash flow, and cost ratio improve.",
        "- Example: a data-center REIT can be Green-eligible only after assets, tenants, power/cooling, NOI/AFFO, and dividend coverage are visible.",
        "- Example: reconstruction, Neom, and disaster-rebuild themes stay Event/Watch until actual contracts and margins are sourced.",
    ]
    return "\n".join(lines) + "\n"


def render_round50_green_guardrail_markdown() -> str:
    lines = [
        "# Round-50 R10 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND50_SCORE_TARGETS:
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
            "- Do not apply these R10 v1.0 weights to production scoring yet.",
            "- Do not treat backlog, asset value, dividend yield, policy support, rate cuts, reconstruction headlines, or AI data-center labels as Green evidence by itself.",
            "- Do not invent PF exposure, unsold inventory, NOI/AFFO, dividend coverage, LTV, occupancy, power, tenant, or price-path fields.",
            "- Do not lower Stage 3-Green for construction recall. Green requires source-backed credit repair, cash-flow recovery, asset cash flow, or contract economics.",
            "- Treat PF delinquency, bridge-loan rollover failure, dividend cuts, impaired CRE loans, net losses, no assets, no tenants, and funding gaps as RedTeam evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round50_credit_asset_cap_markdown() -> str:
    lines = [
        "# Round-50 R10 Credit / Asset Caps",
        "",
        "- `CONSTRUCTION_REAL_ESTATE_CREDIT`: support packages are relief, not structural success, until PF and cash conversion improve.",
        "- `COMMERCIAL_REAL_ESTATE_CREDIT`: office vacancy, impaired loans, reserves, and dividend cuts can hard-break a yield story.",
        "- `REIT_DEVELOPMENT_TRUST`: yield and NAV discount need NOI/AFFO, LTV, occupancy, and dividend coverage.",
        "- `DATA_CENTER_REIT_INFRASTRUCTURE`: AI demand needs assets, tenants, power/cooling, and AFFO before Green.",
        "- `AI_DATA_CENTER_REAL_ASSET_DEVELOPMENT`: pre-revenue mega-projects are 4B-watch if valuation prices 2030s plans today.",
        "- `INFRA_RECONSTRUCTION_POLICY`: policy headlines need funded orders and contract economics.",
        "",
        "Simple example: a construction stock can jump on a government PF support package, but if `refinancing_success_flag` and `cash_conversion_cycle` are still missing, it stays Stage 1/Watch rather than Stage 3-Green.",
    ]
    return "\n".join(lines) + "\n"


def render_round50_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-50 R10 Price Validation Plan",
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
        "fermi_ai_data_center_reit_case",
        "heidelberg_materials_price_cost_case",
    }
    for row in round50_case_candidate_rows():
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


def _score_price_alignment(candidate: Round50CaseCandidate) -> str:
    if "aligned" in candidate.alignment_hint and candidate.case_type in {"structural_success", "success_candidate"}:
        return "aligned"
    if candidate.case_type in {"event_premium", "one_off", "4b_watch"}:
        return "price_moved_without_evidence"
    if candidate.case_type in {"failed_rerating", "4c_thesis_break"}:
        return "false_positive_score"
    return "unknown"


def _rerating_result(candidate: Round50CaseCandidate) -> str:
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
    "ROUND50_CASE_CANDIDATES",
    "ROUND50_DEFAULT_CASES_PATH",
    "ROUND50_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND50_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND50_PRICE_FIELDS",
    "ROUND50_SCORE_TARGETS",
    "ROUND50_SOURCE_ROUND_PATH",
    "Round50CaseCandidate",
    "Round50ScoreTarget",
    "Round50ScoreWeightDraft",
    "render_round50_credit_asset_cap_markdown",
    "render_round50_green_guardrail_markdown",
    "render_round50_price_validation_plan_markdown",
    "render_round50_summary_markdown",
    "round50_case_candidate_rows",
    "round50_case_records",
    "round50_price_field_rows",
    "round50_score_profile_rows",
    "round50_stage_date_rows",
    "round50_summary",
    "target_for",
    "write_round50_r10_reports",
]
