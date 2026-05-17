"""Round-108 R3 Loop-6 battery, EV, and green-energy pack.

Round 108 tightens the R3 split again after R2 Loop 6. It separates Tesla
Megapack supply-chain confirmation, EV CAPA contract cancellation, EV battery
JV restructuring, ESS LFP grid storage, AI data-center storage, EV-to-ESS
redeployment, recycling/second-life storage, graphite supply security,
sodium-ion substitution, solid-state licensing, disclosure-confidence caps,
BESS/EV safety gates, SOH transparency, and speculative battery technology.
It keeps the core rule explicit: EV growth narrative is not durable EPS/FCF
evidence unless contracts, customers, margins, utilization, and FCF are visible
as-of the case date.

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


ROUND108_SOURCE_ROUND_PATH = "docs/round/round_108.md"
ROUND108_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round108_r3_loop6_battery_ev_green"
ROUND108_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop6_round108.jsonl"
ROUND108_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round108_r3_loop6_v6.csv"


@dataclass(frozen=True)
class Round108ScoreWeightDraft:
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
class Round108ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round108ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop6_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.BATTERY_EV_GREEN

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round108CaseCandidate:
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


def _w(
    eps_fcf: int | str,
    visibility: int | str,
    bottleneck: int | str,
    mispricing: int | str,
    valuation: int | str,
    capital: int | str = 0,
    confidence: int | str = 5,
) -> Round108ScoreWeightDraft:
    return Round108ScoreWeightDraft(eps_fcf, visibility, bottleneck, mispricing, valuation, capital, confidence)


def _target(
    target_id: str,
    archetype: E2RArchetype,
    posture: Round10ThemePosture,
    weight: Round108ScoreWeightDraft,
    *,
    stage1: tuple[str, ...],
    stage2: tuple[str, ...],
    stage3: tuple[str, ...],
    stage4b: tuple[str, ...],
    stage4c: tuple[str, ...],
    green: tuple[str, ...],
    red: tuple[str, ...],
    penalties: tuple[str, ...],
    note: str,
    gate_only: bool = False,
) -> Round108ScoreTarget:
    return Round108ScoreTarget(
        target_id,
        archetype,
        posture,
        weight,
        stage1,
        stage2,
        stage3,
        stage4b,
        stage4c,
        green,
        red,
        penalties,
        note,
        gate_only,
    )


ROUND108_SCORE_TARGETS: tuple[Round108ScoreTarget, ...] = (
    _target(
        "BATTERY_MATERIALS_CAPEX_OVERHEAT",
        E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(14, 9, 11, 8, 6),
        stage1=("ev_growth_narrative", "long_term_supply_contract", "capa_expansion_news"),
        stage2=("real_contract", "price_margin_improvement", "op_eps_revision", "line_utilization"),
        stage3=("long_term_contract", "price_pass_through", "fcf_after_capex", "demand_visibility"),
        stage4b=("per_pbr_overheat", "capa_race", "target_price_crowding"),
        stage4c=("ev_demand_slowdown", "raw_material_price_drop", "capa_overbuild", "customer_contract_cancelled", "plant_idle"),
        green=("contract_quality", "price_pass_through", "fcf_after_capex", "demand_visibility"),
        red=("ev_demand_slowdown", "capa_overbuild", "lithium_price_crash", "customer_contract_cancelled", "plant_idle"),
        penalties=("ev_demand_slowdown", "capa_overbuild", "contract_cancellation", "mineral_price"),
        note="Loop 6 lowers battery-material scores because EV CAPA, idle plants, and contract cancellations can quickly become 4C.",
    ),
    _target(
        "BATTERY_EQUIPMENT_PARTS",
        E2RArchetype.BATTERY_EQUIPMENT_PARTS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 15, 10, 11, 9),
        stage1=("battery_equipment_order", "cell_customer_capex", "delivery_schedule_keyword"),
        stage2=("customer_order", "delivery_schedule", "margin_visibility", "revenue_conversion"),
        stage3=("order_to_revenue_conversion", "customer_diversification", "op_eps_revision"),
        stage4b=("equipment_capex_cycle_crowded", "cell_capex_peak"),
        stage4c=("customer_capex_cut", "delivery_delay", "margin_miss", "single_customer", "ev_line_idle"),
        green=("customer_order", "delivery_schedule", "margin_visibility", "op_eps_revision"),
        red=("customer_capex_cut", "delivery_delay", "single_customer", "ev_line_idle"),
        penalties=("customer_capex_cut", "delivery_delay", "ev_line_idle"),
        note="Battery equipment is Watch-to-Green only when CAPEX becomes delivery, revenue, and margin.",
    ),
    _target(
        "BATTERY_RECYCLING_ESS_SHIFT",
        E2RArchetype.BATTERY_RECYCLING_ESS_SHIFT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(20, 18, 14, 11, 10),
        stage1=("battery_recycling", "second_life_battery", "black_mass", "recycling_policy"),
        stage2=("recycling_volume", "metal_recovery_revenue", "customer_contract", "ess_use_case"),
        stage3=("recurring_recycling_fcf", "second_life_revenue", "soh_validation", "customer_diversification"),
        stage4b=("recycling_premium_overheat", "critical_minerals_narrative_crowded"),
        stage4c=("recycling_volume_shortfall", "soh_validation_failure", "metal_price_drop", "second_life_margin_miss"),
        green=("recycling_volume", "metal_recovery_revenue", "customer_contract", "soh_validation", "recurring_fcf"),
        red=("contract_value_missing", "recycling_volume_shortfall", "metal_price_drop", "soh_unreliable"),
        penalties=("recycling_volume", "soh_validation", "metal_price", "contract_value_missing"),
        note="Recycling/second-life stays Watch-to-Green but now requires SOH and grading-cost validation.",
    ),
    _target(
        "SECOND_LIFE_BATTERY_GRID_STORAGE",
        E2RArchetype.SECOND_LIFE_BATTERY_GRID_STORAGE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 16, 12, 11, 9),
        stage1=("second_life_ev_battery", "used_ev_battery_pack", "grid_services", "data_center_backup"),
        stage2=("soh_validation", "residual_capacity_verified", "grid_storage_customer", "warranty_framework"),
        stage3=("second_life_revenue", "safety_validation", "repeat_grid_storage_contract", "fcf_conversion"),
        stage4b=("second_life_narrative_crowded", "recycling_storage_premium"),
        stage4c=("soh_unreliable", "residual_capacity_uncertainty", "fire_safety_failure", "warranty_enforcement_risk"),
        green=("soh_validation", "grid_storage_customer", "safety_validation", "repeat_revenue", "fcf_conversion"),
        red=("soh_unreliable", "residual_capacity_uncertainty", "fire_safety_failure", "warranty_risk"),
        penalties=("soh", "safety", "warranty", "residual_capacity"),
        note="Second-life battery storage is not simple recycling: SOH, residual capacity, safety, warranty, and customer contracts decide visibility.",
    ),
    _target(
        "ESS_LFP_GRID_STORAGE",
        E2RArchetype.ESS_LFP_GRID_STORAGE,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(22, 21, 15, 12, 11),
        stage1=("ess_shift", "lfp_ess_production", "north_america_ess_demand", "grid_storage"),
        stage2=("ess_customer_contract", "ess_contract_value", "ess_contract_duration", "ess_contract_volume_gwh", "production_factory"),
        stage3=("ess_revenue_growth", "ess_opm", "fcf_conversion", "customer_diversification"),
        stage4b=("ess_narrative_crowded", "lfp_ess_related_rally"),
        stage4c=("ess_margin_miss", "lfp_competition", "customer_demand_slowdown", "subsidy_or_tariff_damage"),
        green=("ess_contract_value", "ess_contract_duration", "customer", "gwh_volume", "ess_margin", "fcf_conversion"),
        red=("contract_value_missing", "ess_margin_unverified", "customer_concentration", "subsidy_dependency"),
        penalties=("ess_margin", "lfp_competition", "customer_concentration", "subsidy"),
        note="ESS LFP grid storage is split out because value, duration, customer, and GWh can make a cleaner Stage 2/3 path.",
    ),
    _target(
        "ESS_TESLA_MEGAPACK_SUPPLY_CHAIN",
        E2RArchetype.ESS_TESLA_MEGAPACK_SUPPLY_CHAIN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(23, 24, 16, 13, 11, 0, 6),
        stage1=("lfp_supply_contract", "customer_use_case_unknown", "megapack_keyword"),
        stage2=("tesla_megapack_use_case_confirmed", "lansing_production", "contract_duration", "contract_value"),
        stage3=("lansing_ramp_up", "megapack_revenue_recognition", "ess_opm", "fcf_conversion"),
        stage4b=("tesla_megapack_narrative_crowded", "lfp_contract_premium", "lansing_capacity_fully_priced"),
        stage4c=("lansing_ramp_delay", "tesla_order_cut", "lfp_asp_decline", "feoc_tariff_change"),
        green=("tesla_customer_confirmed", "megapack_use_case", "contract_value", "contract_duration", "lansing_ramp_up", "ess_opm", "fcf_conversion"),
        red=("lansing_ramp_delay", "tesla_concentration", "ess_opm_unverified", "lfp_competition", "feoc_or_tariff_risk"),
        penalties=("lansing_ramp", "tesla_concentration", "ess_margin", "lfp_price", "feoc_tariff"),
        note="Tesla Megapack confirmation can upgrade an undisclosed LFP contract to Stage 2, but Green still needs ramp-up, ESS OPM, utilization, and FCF.",
    ),
    _target(
        "ESS_AI_DATA_CENTER_STORAGE",
        E2RArchetype.ESS_AI_DATA_CENTER_STORAGE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(22, 20, 16, 13, 11),
        stage1=("ai_datacenter_power_demand", "storage_demand", "utility_scale_battery", "backup_storage"),
        stage2=("data_center_storage_customer", "utility_customer_contract", "deployment_gwh", "margin_signal"),
        stage3=("repeat_storage_revenue", "ess_opm", "fcf_conversion", "customer_diversification"),
        stage4b=("ai_power_storage_narrative_crowded", "storage_capacity_rally"),
        stage4c=("datacenter_project_delay", "safety_regulation", "customer_contract_delay", "lfp_competition"),
        green=("data_center_customer", "deployment_gwh", "storage_margin", "fcf_conversion", "repeat_revenue"),
        red=("customer_contract_missing", "datacenter_capex_delay", "safety_regulation", "lfp_competition"),
        penalties=("customer_contract_missing", "datacenter_capex_delay", "safety_regulation"),
        note="AI data-center storage has strong demand but stays Watch until customer contracts, GWh, margin, and FCF are visible.",
    ),
    _target(
        "EV_TO_ESS_CAPACITY_REDEPLOYMENT",
        E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 17, 13, 12, 9),
        stage1=("ev_line_idle", "ev_line_to_ess_conversion", "ess_redeployment_plan"),
        stage2=("ess_line_conversion_complete", "storage_customer_contract", "converted_line_capacity_gwh", "converted_line_utilization"),
        stage3=("ess_revenue_offsets_ev_idle_cost", "ess_opm", "fcf_conversion", "customer_diversification"),
        stage4b=("ev_failure_reframed_as_ess_overhyped", "redeployment_narrative_crowded"),
        stage4c=("conversion_cost_increase", "ess_contract_absent", "low_utilization", "ev_write_down_continues"),
        green=("storage_customer_contract", "converted_line_utilization", "ess_opm", "fcf_conversion"),
        red=("ev_line_idle", "conversion_cost_increase", "ess_contract_absent", "low_utilization", "ev_write_down"),
        penalties=("ev_idle_overhang", "conversion_cost", "contract_absent", "margin_unverified"),
        note="EV-to-ESS redeployment is useful only if the idle EV fixed-cost problem is offset by real ESS contracts and margins.",
    ),
    _target(
        "EV_BATTERY_JV_RESTRUCTURING",
        E2RArchetype.EV_BATTERY_JV_RESTRUCTURING,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(15, 13, 10, 11, 8),
        stage1=("jv_dissolution", "plant_ownership_change", "ev_demand_slowdown", "ev_subsidy_expiry"),
        stage2=("fixed_cost_reduction", "debt_reduction", "ess_pivot_plan", "new_customer_contract"),
        stage3=("post_restructuring_opm_improvement", "ess_or_ev_mix_improves_fcf", "capacity_utilization_recovers"),
        stage4b=("ess_pivot_narrative_crowded", "ev_restructuring_read_as_clean_positive"),
        stage4c=("ev_demand_slowdown", "plant_idle_continues", "operating_loss_expands", "ess_pivot_failure"),
        green=("fixed_cost_reduction", "ess_customer_contract", "opm_improvement", "fcf_conversion"),
        red=("jv_dissolution", "operating_loss", "ev_subsidy_expiry", "ess_pivot_unproven", "plant_idle"),
        penalties=("jv_dissolution", "operating_loss", "fixed_cost", "ess_pivot_unproven"),
        note="SK On-Ford-style JV restructuring is a Watch path: fixed-cost relief and ESS pivot can help, but EV-demand 4C remains attached.",
    ),
    _target(
        "EV_CAPA_CONTRACT_CANCELLATION",
        E2RArchetype.EV_CAPA_CONTRACT_CANCELLATION,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("ev_battery_contract", "automaker_ev_plan", "expected_revenue"),
        stage2=("cancellation_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("contract_cancellation", "automaker_ev_cutback", "expected_revenue_loss", "capacity_underutilization", "write_down"),
        green=(),
        red=("contract_cancellation", "automaker_ev_cutback", "expected_revenue_loss", "capacity_underutilization", "write_down"),
        penalties=("contract_cancellation", "expected_revenue_loss", "ev_demand_slowdown", "underutilization", "write_down"),
        note="EV CAPA contract cancellation is a 4C/RedTeam gate; it must not be averaged into positive battery growth evidence.",
        gate_only=True,
    ),
    _target(
        "BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE",
        E2RArchetype.BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("large_battery_contract", "lfp_supply_contract", "customer_confidential"),
        stage2=("disclosure_gap_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("customer_undisclosed", "use_case_undisclosed", "contract_value_missing", "margin_unverified"),
        green=(),
        red=("customer_undisclosed", "use_case_undisclosed", "contract_value_missing", "margin_unverified"),
        penalties=("customer_disclosure", "use_case_disclosure", "contract_value", "margin"),
        note="Large battery contracts get a Stage 3 cap when customer, use-case, value, or margin is not disclosed.",
        gate_only=True,
    ),
    _target(
        "EV_INFRASTRUCTURE",
        E2RArchetype.EV_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(16, 13, 7, 10, 8),
        stage1=("charging_station", "fast_charging", "ev_infrastructure_policy"),
        stage2=("utilization", "recurring_revenue", "subsidy_visibility"),
        stage3=("profitable_utilization", "repeat_revenue", "subsidy_independent_margin"),
        stage4b=("ev_charging_theme_crowded",),
        stage4c=("low_utilization", "subsidy_cut", "fire_regulation", "maintenance_cost"),
        green=("utilization", "recurring_revenue", "profitability"),
        red=("low_utilization", "subsidy_dependency", "fire_regulation"),
        penalties=("utilization", "fire_regulation", "subsidy_dependency"),
        note="EV infrastructure needs utilization and unit economics, not charger-count headlines.",
    ),
    _target(
        "HYDROGEN_FUEL_CELL_INFRA",
        E2RArchetype.HYDROGEN_FUEL_CELL_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 18, 12, 12, 10),
        stage1=("hydrogen_factory_groundbreaking", "hydrogen_policy", "electrolyzer_or_fuel_cell_capex"),
        stage2=("customer_or_demand_source", "production_capacity", "delivery_contract", "plant_completion_date"),
        stage3=("utilization", "op_eps_conversion", "subsidy_independent_economics"),
        stage4b=("hydrogen_theme_overheat",),
        stage4c=("subsidy_cut", "customer_absent", "low_utilization", "project_delay"),
        green=("customer_demand", "production_capacity", "utilization", "op_eps_conversion"),
        red=("subsidy_dependency", "customer_absent", "low_utilization"),
        penalties=("customer_absent", "utilization", "subsidy_dependency", "infrastructure_gap"),
        note="Hydrogen CAPEX can reach Stage 2, but Green needs customers, utilization, and OP conversion.",
    ),
    _target(
        "SOLAR_TARIFF_SUPPLYCHAIN",
        E2RArchetype.SOLAR_TARIFF_SUPPLYCHAIN,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(14, 11, 11, 9, 7),
        stage1=("solar_factory", "us_factory", "subsidy_policy"),
        stage2=("utilization", "customer_contract", "supply_chain_stable", "op_turnaround"),
        stage3=("subsidy_independent_fcf", "supply_chain_clean", "margin_visible"),
        stage4b=("solar_us_manufacturing_narrative_crowded", "subsidy_premium"),
        stage4c=("tariff_risk", "customs_detention", "uflpa_detention", "feoc_risk", "worker_furlough", "component_delay"),
        green=("utilization", "customer_contract", "supply_chain_stable", "fcf_margin"),
        red=("tariff_risk", "customs_detention", "uflpa_detention", "subsidy_dependency", "feoc_risk"),
        penalties=("customs", "tariff", "uflpa", "feoc", "supply_chain_disruption"),
        note="Solar stays RedTeam-first because subsidy and US manufacturing can break on customs or supply-chain detention.",
    ),
    _target(
        "RENEWABLE_ENERGY_PROJECT_ECONOMICS",
        E2RArchetype.RENEWABLE_ENERGY_PROJECT_ECONOMICS,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(14, 11, 9, 9, 7),
        stage1=("wind_project", "renewable_policy", "ppa_or_project_news"),
        stage2=("permitted_project", "funding_visible", "cost_schedule_visible", "construction_start"),
        stage3=("project_economics", "op_eps_conversion", "cost_controlled", "repeat_project_backlog"),
        stage4b=("renewable_policy_crowded", "project_premium"),
        stage4c=("impairment", "project_delay", "financing_cost_increase", "foundation_cost", "cost_overrun"),
        green=("permitting", "funding", "cost_schedule", "margin_visibility"),
        red=("permitting_delay", "financing_cost", "cost_overrun", "impairment"),
        penalties=("rates", "cost_overrun", "permitting", "impairment"),
        note="Wind/PPA policy stories remain Watch until project economics survive rates, permits, and foundation costs.",
    ),
    _target(
        "WASTE_RECYCLING_ENVIRONMENT",
        E2RArchetype.WASTE_RECYCLING_ENVIRONMENT,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(18, 22, 15, 13, 12, 3),
        stage1=("waste_treatment_platform", "permit_value", "plastic_recycling", "waste_to_energy"),
        stage2=("treatment_volume", "long_term_contract", "utilization", "fcf_visible"),
        stage3=("permit_asset", "recurring_fcf", "valuation_frame_change", "mna_value_support"),
        stage4b=("waste_mna_premium_crowded", "permit_value_fully_priced"),
        stage4c=("utilization_drop", "capex_burden", "metal_price_drop", "regulatory_cost"),
        green=("permit_asset", "treatment_volume", "utilization", "recurring_fcf"),
        red=("utilization_drop", "capex_burden", "commodity_recycling_price_drop"),
        penalties=("utilization", "capex", "metal_price", "regulatory_cost"),
        note="Waste treatment remains the clearest R3 Green-capable axis when permits, volume, and recurring FCF are proven.",
    ),
    _target(
        "CARBON_CREDIT_CBAM_COMPLIANCE",
        E2RArchetype.CARBON_CREDIT_CBAM_COMPLIANCE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(14, 17, 10, 12, 8, 2, 6),
        stage1=("eu_ets_or_cbam_policy", "carbon_accounting", "compliance_monitoring"),
        stage2=("carbon_accounting_revenue", "verification_revenue", "low_carbon_product_premium"),
        stage3=("recurring_compliance_revenue", "cost_pass_through", "industrial_customer_base"),
        stage4b=("carbon_price_theme_crowded",),
        stage4c=("carbon_price_drop", "free_allowance_expansion", "greenwashing_risk", "policy_delay"),
        green=("recurring_revenue", "verification_customer", "cost_pass_through"),
        red=("carbon_price_volatility", "greenwashing", "policy_reversal"),
        penalties=("policy_reform", "carbon_price", "greenwashing"),
        note="Carbon price is not enough; compliance revenue and cost pass-through are the stronger route.",
    ),
    _target(
        "DATA_CENTER_WATER_REUSE_INFRA",
        E2RArchetype.DATA_CENTER_WATER_REUSE_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(16, 18, 14, 12, 10, 2),
        stage1=("ai_datacenter_water_use", "water_reuse", "closed_loop_cooling", "water_treatment"),
        stage2=("data_center_customer", "reuse_project", "contracted_revenue"),
        stage3=("repeat_water_reuse_revenue", "margin_visible", "local_permit_support"),
        stage4b=("water_reuse_theme_crowded",),
        stage4c=("customer_absent", "local_opposition", "unit_economics_weak", "permitting_delay"),
        green=("data_center_customer", "contracted_revenue", "unit_economics"),
        red=("customer_absent", "local_opposition", "weak_economics"),
        penalties=("customer_absent", "local_opposition", "economics"),
        note="Data-center water reuse needs named customers and economics before Green.",
    ),
    _target(
        "EV_FIRE_BESS_SAFETY_OVERLAY",
        E2RArchetype.EV_FIRE_BESS_SAFETY_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("ev_fire", "bess_fire", "battery_recall", "insurance_cost", "battery_certification"),
        stage2=("risk_event_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("battery_fire", "bess_fire", "certification_requirement", "battery_supplier_disclosure", "recall", "insurance_cost", "parking_charging_regulation", "facility_permitting_delay"),
        green=(),
        red=("battery_fire", "bess_fire", "certification_requirement", "recall", "insurance_cost", "fire_regulation"),
        penalties=("fire", "certification", "recall", "insurance", "permitting"),
        note="EV/BESS fire, certification, insurance, and facility-permitting overlay is a RedTeam gate, not positive score.",
        gate_only=True,
    ),
    _target(
        "BESS_SAFETY_PERMITTING",
        E2RArchetype.BESS_SAFETY_PERMITTING,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("bess_fire", "facility_permitting", "resident_evacuation", "insurance_cost"),
        stage2=("safety_permitting_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("bess_fire", "evacuation", "fire_safety_capex", "facility_permitting_delay", "insurance_cost", "local_opposition"),
        green=(),
        red=("bess_fire", "evacuation", "facility_permitting_delay", "insurance_cost", "local_opposition"),
        penalties=("bess_fire", "permitting", "insurance", "local_opposition"),
        note="Moss Landing-style BESS fire shows storage demand can still fail on safety, permitting, insurance, and local acceptance.",
        gate_only=True,
    ),
    _target(
        "BATTERY_SOH_SECOND_LIFE_TRANSPARENCY",
        E2RArchetype.BATTERY_SOH_SECOND_LIFE_TRANSPARENCY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("soh_unreliable", "battery_passport", "second_life_validation", "residual_capacity_uncertainty"),
        stage2=("transparency_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("soh_unreliable", "residual_capacity_uncertainty", "second_life_grading_cost", "warranty_enforcement_risk"),
        green=(),
        red=("soh_unreliable", "second_life_grading_cost", "battery_passport_compliance", "warranty_risk"),
        penalties=("soh", "second_life_validation", "battery_passport", "grading_cost"),
        note="SOH opacity is a battery recycling and second-life RedTeam gate, not a Green input.",
        gate_only=True,
    ),
    _target(
        "BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY",
        E2RArchetype.BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(17, 15, 16, 12, 9),
        stage1=("graphite_anode_dependency", "china_graphite_dependency", "supplychain_security", "import_restriction"),
        stage2=("policy_financing", "graphite_offtake", "customer_contract", "production_cost_path"),
        stage3=("battery_grade_graphite_revenue", "margin_visible", "fcf_conversion", "customer_diversification"),
        stage4b=("graphite_security_narrative_crowded", "policy_financing_premium"),
        stage4c=("us_graphite_cost_uncompetitive", "policy_financing_absent", "offtake_missing", "china_price_pressure", "capex_burden"),
        green=("graphite_offtake", "customer_contract", "cost_path", "margin_visible", "fcf_conversion"),
        red=("us_graphite_cost_uncompetitive", "policy_financing_absent", "offtake_missing", "china_price_pressure"),
        penalties=("us_cost", "policy_financing", "offtake", "china_price_pressure"),
        note="Graphite security is a supply-chain Watch axis, not automatic Green: cost, financing, and offtake must be proven.",
    ),
    _target(
        "LITHIUM_ESS_DEMAND_CYCLE",
        E2RArchetype.LITHIUM_ESS_DEMAND_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w("cycle", "cycle", "cycle", "cycle", "cycle", "cycle", 5),
        stage1=("lithium_price_rebound", "mine_shutdown", "ess_lithium_demand"),
        stage2=("ess_demand_outlook_improves", "cost_curve_support", "inventory_absorption"),
        stage3=("low_cost_structure", "long_term_offtake", "fcf_defense", "capex_discipline"),
        stage4b=("lithium_rebound_crowded", "mine_restart_ignored", "sodium_ion_ignored"),
        stage4c=("lithium_price_crash", "mine_restart_supply_rebound", "ev_demand_slowdown", "capex_cut"),
        green=("low_cost_structure", "long_term_offtake", "fcf_defense", "capex_discipline"),
        red=("lithium_price_crash", "mine_restart", "supply_rebound", "sodium_ion_competition"),
        penalties=("price_crash", "mine_restart", "sodium_ion", "ev_demand_slowdown"),
        note="Lithium ESS demand is a cycle overlay by default; ESS demand can help Stage 1/2 but does not make Green alone.",
    ),
    _target(
        "SODIUM_ION_SUBSTITUTION_OVERLAY",
        E2RArchetype.SODIUM_ION_SUBSTITUTION_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("sodium_ion_battery", "low_cost_ess", "low_cost_ev", "lithium_price_ceiling"),
        stage2=("substitution_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("sodium_ion_substitution", "lithium_price_ceiling", "lfp_price_pressure", "low_cost_ess_substitution"),
        green=(),
        red=("sodium_ion_substitution", "lithium_price_ceiling", "lfp_price_pressure"),
        penalties=("substitution", "price_ceiling", "low_cost_ess"),
        note="Sodium-ion is a RedTeam overlay because it can cap lithium/LFP economics in low-cost ESS or low-cost EV use cases.",
        gate_only=True,
    ),
    _target(
        "SOLID_STATE_COMMERCIALIZATION_LICENSE",
        E2RArchetype.SOLID_STATE_COMMERCIALIZATION_LICENSE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(12, 13, 10, 12, 8),
        stage1=("solid_state_sample", "technology_claim", "prototype_or_mou"),
        stage2=("license", "royalty_framework", "production_rights_gwh", "oem_partnership"),
        stage3=("mass_production", "vehicle_series_adoption", "royalty_revenue", "yield_cost_visible"),
        stage4b=("solid_state_license_narrative_crowded", "commercialization_priced_before_revenue"),
        stage4c=("technology_condition_unmet", "yield_failure", "cost_overrun", "mass_production_delay", "vehicle_series_absent"),
        green=("mass_production", "vehicle_series_adoption", "royalty_revenue", "yield_cost_visible"),
        red=("technology_condition_unmet", "yield_failure", "mass_production_delay", "vehicle_series_absent"),
        penalties=("commercialization", "yield", "cost", "vehicle_adoption"),
        note="Solid-state licensing can be Stage 2, but Green waits for production, vehicle adoption, royalty revenue, cost, and yield.",
    ),
    _target(
        "SPECULATIVE_BATTERY_TECH",
        E2RArchetype.SPECULATIVE_BATTERY_TECH,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(6, 5, 6, 8, 5, 0, 4),
        stage1=("solid_state_battery", "new_battery_material", "prototype_or_mou", "technology_theme"),
        stage2=("commercial_customer", "pilot_revenue", "mass_production_schedule"),
        stage3=("scaled_revenue", "customer_diversification", "verified_margin", "fcf_conversion"),
        stage4b=("solid_state_theme_overheat", "pre_revenue_rally"),
        stage4c=("commercialization_delay", "customer_absent", "mass_production_failure", "dilution_or_cash_burn"),
        green=("scaled_revenue", "commercial_customer", "verified_margin", "fcf_conversion"),
        red=("pre_commercialization", "customer_absent", "mass_production_failure", "cash_burn"),
        penalties=("commercialization", "customer_absent", "mass_production", "cash_burn"),
        note="Speculative solid-state or new battery technology cannot be Green before commercialization, customer evidence, and FCF.",
    ),
)


ROUND108_CASE_CANDIDATES: tuple[Round108CaseCandidate, ...] = (
    Round108CaseCandidate(
        "lg_energy_lfp_4_3b_contract_initial_case",
        "BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE",
        "373220",
        "LG Energy Solution initial LFP $4.3B contract disclosure cap",
        "KR",
        "success_candidate",
        None,
        date(2025, 7, 30),
        None,
        None,
        None,
        ("ess_contract_value_4_3b", "ess_contract_duration_2027_08_2030_07", "lfp_battery_contract", "extension_option_7y"),
        ("customer_undisclosed", "use_case_undisclosed", "ess_margin_unverified", "lfp_competition", "ira_tariff_feoc_risk"),
        "ess_disclosure_capped",
        "needs_price_backfill",
        ("round_108.md Reuters LGES $4.3B LFP contract",),
        "Initial 2025 disclosure value and duration support Stage 2, but customer and use-case were undisclosed then, so Stage 3-Green must be capped.",
        (E2RArchetype.ESS_LFP_GRID_STORAGE,),
    ),
    Round108CaseCandidate(
        "tesla_lges_megapack3_lansing_case",
        "ESS_TESLA_MEGAPACK_SUPPLY_CHAIN",
        "373220",
        "Tesla-LGES Megapack 3 Lansing LFP supply",
        "KR",
        "success_candidate",
        None,
        date(2026, 3, 17),
        None,
        None,
        None,
        (
            "ess_contract_value_4_3b",
            "ess_contract_duration_2027_08_2030_07",
            "tesla_megapack_flag",
            "megapack_version_3",
            "lansing_production_flag",
            "production_start_year_2027",
            "lfp_prismatic_cell",
        ),
        (
            "ess_margin_unverified",
            "lansing_ramp_up_needed",
            "tesla_concentration",
            "lfp_competition",
            "feoc_or_tariff_risk",
        ),
        "ess_tesla_megapack_stage2_watch",
        "needs_price_backfill",
        ("round_108.md Reuters Tesla-LGES Megapack 3 Lansing confirmation",),
        "The same $4.3B LFP contract becomes a stronger Stage 2 candidate once Tesla Megapack 3 and Lansing production are confirmed, but ramp-up, utilization, ESS OPM, and FCF remain required.",
        (E2RArchetype.ESS_LFP_GRID_STORAGE,),
    ),
    Round108CaseCandidate(
        "sk_on_flatiron_ess_7_2gwh_case",
        "ESS_LFP_GRID_STORAGE",
        "SKON_FLATIRON_REF",
        "SK On-Flatiron ESS 7.2GWh supply",
        "KR",
        "success_candidate",
        None,
        date(2025, 9, 3),
        None,
        None,
        None,
        ("ess_contract_volume_7_2gwh", "ess_contract_duration_2026_2030", "lfp_ess_mass_production", "ev_line_to_ess_conversion"),
        ("contract_value_missing", "ess_margin_unverified", "customer_demand_unverified", "ev_line_conversion_cost"),
        "ess_contract_stage2_value_missing",
        "needs_price_backfill",
        ("round_108.md Reuters SK On Flatiron ESS deal",),
        "GWh and duration support Stage 2, but missing contract value caps EPS/FCF and Green credit.",
        (E2RArchetype.BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE,),
    ),
    Round108CaseCandidate(
        "gm_lg_ultium_ohio_idle_case",
        "EV_TO_ESS_CAPACITY_REDEPLOYMENT",
        "GM_LG_ULTIUM_REF",
        "GM-LG Ultium Ohio plant idle",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 12),
        ("ev_battery_capa", "tennessee_ess_shift_candidate"),
        ("ev_demand_slowdown", "plant_idle", "layoff_furlough", "capacity_underutilization", "restart_uncertain"),
        "ev_capa_false_green_plus_ess_shift_watch",
        "needs_price_backfill",
        ("round_108.md Reuters GM-LG Ohio battery plant",),
        "EV CAPA can become hard 4C while a separate ESS conversion remains only a Watch candidate.",
        (E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT, E2RArchetype.ESS_LFP_GRID_STORAGE),
    ),
    Round108CaseCandidate(
        "sk_on_ford_jv_dissolution_case",
        "EV_BATTERY_JV_RESTRUCTURING",
        "SKON_FORD_JV_REF",
        "SK On-Ford battery JV dissolution and ESS pivot watch",
        "US",
        "success_candidate",
        None,
        date(2025, 12, 11),
        None,
        None,
        None,
        ("jv_dissolution_flag", "plant_ownership_change", "ess_pivot_flag", "fixed_cost_reduction_candidate"),
        ("ev_demand_slowdown", "ev_subsidy_expiry", "operating_loss_amount", "ess_pivot_revenue_unconfirmed"),
        "ev_jv_restructuring_with_ess_pivot",
        "needs_price_backfill",
        ("round_108.md Reuters SK On Ford JV dissolution",),
        "JV dissolution can reduce fixed-cost drag and create an ESS pivot option, but EV-demand weakness and operating losses keep it Watch.",
        (E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT, E2RArchetype.EV_CAPA_CONTRACT_CANCELLATION),
    ),
    Round108CaseCandidate(
        "ford_energy_storage_pivot_case",
        "ESS_AI_DATA_CENTER_STORAGE",
        "F",
        "Ford Energy ESS and AI data-center storage pivot",
        "US",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("ford_energy_launch", "ai_data_center_storage", "utility_storage_customer_target", "annual_deployment_target_20gwh", "catl_lfp_license"),
        ("ev_write_down_19_5b", "customer_contract_missing", "execution_timeline_2027", "margin_unverified", "feoc_or_national_security_risk"),
        "ev_to_ess_redeployment_watch",
        "needs_exact_stage_date_backfill",
        ("round_108.md Financial Times Ford Energy storage pivot",),
        "Ford Energy is a useful AI data-center storage pivot reference, but exact source date, customer contracts, margins, and FCF remain unverified.",
        (E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT,),
    ),
    Round108CaseCandidate(
        "ford_lges_ev_contract_cancel_case",
        "EV_CAPA_CONTRACT_CANCELLATION",
        "FORD_LGES_CANCEL_REF",
        "Ford-LGES EV battery contract cancellation",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 12, 17),
        ("ev_battery_contract_6_5b", "ford_ev_program", "expected_revenue"),
        ("contract_cancelled", "ev_model_discontinued", "expected_revenue_loss", "write_down_19_5b", "policy_shift", "ev_demand_slowdown"),
        "ev_battery_contract_cancellation_hard_4c",
        "needs_price_backfill",
        ("round_108.md Reuters Ford LGES contract cancellation",),
        "Long-term EV battery supply contracts are not automatically Green if customer EV strategy changes.",
    ),
    Round108CaseCandidate(
        "lges_freudenberg_contract_cancel_case",
        "EV_CAPA_CONTRACT_CANCELLATION",
        "373220",
        "LGES-Freudenberg EV battery contract cancellation",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 12, 26),
        ("battery_order_3_9tn_krw", "ev_battery_contract", "expected_revenue"),
        ("contract_cancelled", "customer_strategy_risk", "expected_revenue_loss", "capacity_underutilization", "ev_demand_slowdown"),
        "ev_battery_contract_cancellation_hard_4c",
        "needs_price_backfill",
        ("round_108.md LGES-Freudenberg contract cancellation",),
        "A multi-trillion-won EV battery order can still be 4C if the customer cancels and expected revenue disappears.",
    ),
    Round108CaseCandidate(
        "redwood_recycling_energy_storage_case",
        "BATTERY_RECYCLING_ESS_SHIFT",
        "REDWOOD_REF",
        "Redwood recycling and energy storage",
        "US",
        "success_candidate",
        None,
        date(2025, 10, 23),
        None,
        date(2025, 10, 23),
        None,
        ("battery_recycling", "metal_recovery_lithium_cobalt_nickel_copper", "grid_services", "datacenter_ess", "strategic_customers"),
        ("private_company_reference", "recycling_margin_unverified", "soh_validation_needed", "public_price_unavailable"),
        "recycling_plus_storage_structural_reference",
        "missing_public_price_data",
        ("round_108.md Reuters Redwood recycling funding",),
        "Recycling gets stronger when recovered metals, ESS/grid services, data-center demand, and customers connect.",
        (E2RArchetype.ESS_LFP_GRID_STORAGE, E2RArchetype.ESS_AI_DATA_CENTER_STORAGE),
    ),
    Round108CaseCandidate(
        "second_life_battery_grid_storage_reference_case",
        "SECOND_LIFE_BATTERY_GRID_STORAGE",
        "SECOND_LIFE_STORAGE_REF",
        "Second-life battery grid storage SOH validation reference",
        "GLOBAL",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("second_life_battery_flag", "second_life_grid_storage_flag", "grid_services", "soh_validation_needed"),
        ("soh_unreliable", "residual_capacity_uncertainty_flag", "battery_grading_cost", "warranty_enforcement_risk_flag"),
        "recycling_second_life_risk",
        "needs_exact_stage_date_backfill",
        ("round_108.md second-life battery grid storage SOH guardrail",),
        "Second-life storage can become useful grid evidence only when SOH, safety, warranty, and customer contracts are independently validated.",
        (E2RArchetype.BATTERY_RECYCLING_ESS_SHIFT, E2RArchetype.BATTERY_SOH_SECOND_LIFE_TRANSPARENCY),
    ),
    Round108CaseCandidate(
        "graphite_supply_security_case",
        "BATTERY_GRAPHITE_SUPPLYCHAIN_SECURITY",
        "GRAPHITE_SECURITY_REF",
        "Battery graphite supply security with cost risk",
        "GLOBAL",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("graphite_supplychain_security_flag", "china_graphite_dependency_pct", "policy_financing_candidate"),
        ("us_graphite_cost_premium", "policy_financing_absent", "graphite_offtake_missing", "china_price_pressure"),
        "graphite_security_but_cost_risk",
        "needs_exact_stage_date_backfill",
        ("round_108.md arXiv graphite battery supply security",),
        "China dependency makes graphite strategically important, but US cost, policy financing, and offtake must be validated before Green.",
    ),
    Round108CaseCandidate(
        "eqt_kj_environment_waste_platform_case",
        "WASTE_RECYCLING_ENVIRONMENT",
        "KJ_ENV_REF",
        "EQT-KJ Environment 폐기물 플랫폼",
        "KR",
        "structural_success",
        None,
        date(2024, 8, 16),
        None,
        None,
        None,
        ("waste_treatment_platform", "permit_asset", "plastic_recycling", "waste_to_energy", "mna_value_1tn_krw", "metro_area_coverage"),
        ("utilization_drop", "capex_burden", "regulatory_cost"),
        "waste_platform_structural_reference",
        "missing_public_price_data",
        ("round_108.md Reuters EQT KJ Environment platform",),
        "Waste treatment is R3's clearest Green-capable infrastructure reference when permits, volume, and recurring FCF are visible.",
    ),
    Round108CaseCandidate(
        "hyundai_hydrogen_fuel_cell_plant_case",
        "HYDROGEN_FUEL_CELL_INFRA",
        "005380",
        "현대차 수소연료전지 울산 공장",
        "KR",
        "success_candidate",
        None,
        date(2025, 10, 30),
        None,
        date(2025, 10, 30),
        None,
        ("hydrogen_capex_930bn_krw", "plant_completion_2027", "fuel_cell_capacity", "electrolyzer_plan", "commercial_vehicle_ship_construction_equipment"),
        ("customer_absent", "subsidy_dependency", "low_utilization", "hydrogen_infra_gap"),
        "hydrogen_capex_stage1_to_stage2_candidate",
        "needs_price_backfill",
        ("round_108.md Reuters Hyundai hydrogen fuel-cell plant",),
        "Actual CAPEX is stronger than policy talk, but customers, utilization, and OP conversion are still required.",
    ),
    Round108CaseCandidate(
        "qcells_customs_detention_furlough_case",
        "SOLAR_TARIFF_SUPPLYCHAIN",
        "QCELLS_REF",
        "Qcells customs detention and furlough",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 11, 8),
        ("solar_us_factory", "subsidy_policy"),
        ("customs_detention", "uflpa_flag", "component_delay", "furlough_layoff", "production_disruption"),
        "solar_policy_supplychain_4c",
        "missing_public_price_data",
        ("round_108.md Reuters Qcells customs detention",),
        "Solar subsidy and US manufacturing narrative can break when customs and component supply stop production.",
    ),
    Round108CaseCandidate(
        "orsted_sunrise_wind_impairment_case",
        "RENEWABLE_ENERGY_PROJECT_ECONOMICS",
        "ORSTED.CO",
        "Ørsted Sunrise Wind impairment",
        "EU",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 1, 20),
        ("offshore_wind_project", "renewable_policy", "ppa"),
        ("impairment_1_7b", "project_delay", "cost_overrun", "financing_cost_increase", "foundation_cost"),
        "wind_project_impairment_4c",
        "needs_price_backfill",
        ("round_108.md Reuters Orsted Sunrise Wind impairment",),
        "Renewable policy and PPAs cannot overcome project economics when rates, foundations, and delay create impairment.",
    ),
    Round108CaseCandidate(
        "lithium_price_86pct_crash_case",
        "LITHIUM_ESS_DEMAND_CYCLE",
        "LITHIUM_CYCLE_REF",
        "리튬 가격 86% 급락",
        "GLOBAL",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 1, 13),
        ("lithium_price_cycle", "mine_shutdown"),
        ("lithium_price_crash", "raw_material_price_drop", "mine_restart_supply_rebound", "ev_demand_slowdown"),
        "lithium_cycle_hard_counterexample",
        "missing_price_data",
        ("round_108.md Reuters lithium prices after crash",),
        "Lithium rebound is not structural Green without cost curve, offtake, FCF, and CAPEX discipline.",
    ),
    Round108CaseCandidate(
        "lithium_ess_demand_recovery_case",
        "LITHIUM_ESS_DEMAND_CYCLE",
        "LITHIUM_ESS_REF",
        "리튬 ESS demand recovery",
        "GLOBAL",
        "cyclical_success",
        None,
        date(2026, 1, 4),
        None,
        None,
        None,
        ("ess_lithium_demand_growth", "datacenter_storage_demand", "china_power_market_reform"),
        ("mine_restart_supply_rebound", "sodium_ion_competition", "ev_subsidy_expiry"),
        "lithium_ess_demand_recovery_but_cycle_watch",
        "missing_price_data",
        ("round_108.md Reuters energy storage lithium demand",),
        "ESS can improve lithium demand, but lithium miners remain cycle/Watch until FCF and supply response are controlled.",
    ),
    Round108CaseCandidate(
        "sodium_ion_substitution_watch_case",
        "SODIUM_ION_SUBSTITUTION_OVERLAY",
        "SODIUM_ION_REF",
        "Sodium-ion substitution pressure on lithium/LFP economics",
        "GLOBAL",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("sodium_ion_substitution_flag", "sodium_ion_ess_flag", "low_cost_ess_substitution"),
        ("sodium_ion_price_pressure_flag", "lithium_price_ceiling", "lfp_price_pressure"),
        "sodium_ion_substitution_watch",
        "needs_exact_stage_date_backfill",
        ("round_108.md Reuters lithium ESS demand sodium-ion risk",),
        "Sodium-ion is a price-ceiling and substitution overlay for lithium/LFP cases, not a positive Green target.",
    ),
    Round108CaseCandidate(
        "korea_ev_battery_certification_fire_case",
        "EV_FIRE_BESS_SAFETY_OVERLAY",
        "EV_FIRE_RISK_REF",
        "Korea EV battery certification and fire risk",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 8, 25),
        ("ev_growth_narrative",),
        ("battery_fire", "battery_certification", "battery_supplier_disclosure", "parking_charging_regulation", "insurance_cost"),
        "ev_fire_regulatory_overlay",
        "missing_price_data",
        ("round_108.md Reuters Korea EV battery certification",),
        "EV fire and battery disclosure should become a separate RedTeam overlay for battery, charging, and ESS candidates.",
    ),
    Round108CaseCandidate(
        "moss_landing_bess_fire_case",
        "BESS_SAFETY_PERMITTING",
        "MOSS_LANDING_BESS_REF",
        "Moss Landing BESS fire safety and permitting overlay",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 1, 17),
        ("grid_scale_bess", "energy_storage_boom"),
        ("bess_fire", "resident_evacuation", "highway_closure", "facility_permitting_delay", "insurance_cost"),
        "ev_bess_safety_regulatory_overlay",
        "needs_exact_stage_date_backfill",
        ("round_108.md Guardian Moss Landing battery storage fire",),
        "Large BESS demand can be offset by fire, permitting, insurance, and local-safety risk; exact stage date needs backfill.",
    ),
    Round108CaseCandidate(
        "battery_soh_transparency_case",
        "BATTERY_SOH_SECOND_LIFE_TRANSPARENCY",
        "BATTERY_SOH_REF",
        "Battery SOH transparency and second-life risk",
        "GLOBAL",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("soh_unreliable", "residual_capacity_uncertainty", "second_life_battery", "battery_passport"),
        ("soh_validation_failure", "second_life_grading_cost", "warranty_enforcement_risk", "battery_passport_compliance"),
        "battery_health_transparency_redteam",
        "needs_exact_stage_date_backfill",
        ("round_108.md arXiv battery health validation",),
        "Second-life and recycling economics can be overstated when SOH and residual capacity are not independently validated.",
    ),
    Round108CaseCandidate(
        "quantumscape_vw_solid_state_license_case",
        "SOLID_STATE_COMMERCIALIZATION_LICENSE",
        "QS",
        "QuantumScape-Volkswagen solid-state license",
        "US",
        "success_candidate",
        None,
        date(2024, 7, 11),
        None,
        None,
        None,
        ("solid_state_license_flag", "solid_state_license_capacity_gwh", "royalty_structure_flag", "oem_partnership"),
        ("commercialization_condition_flag", "mass_production_unverified", "solid_state_yield_signal_missing", "vehicle_series_adoption_absent"),
        "solid_state_license_stage2_but_commercialization_watch",
        "needs_price_backfill",
        ("round_108.md Reuters Volkswagen QuantumScape solid-state license",),
        "A solid-state license can be Stage 2, but Green waits for production, vehicle adoption, royalty revenue, cost, and yield.",
        (E2RArchetype.SPECULATIVE_BATTERY_TECH,),
    ),
    Round108CaseCandidate(
        "speculative_solid_state_theme_case",
        "SPECULATIVE_BATTERY_TECH",
        "SOLID_STATE_THEME_REF",
        "Speculative solid-state battery technology theme",
        "GLOBAL",
        "overheat",
        None,
        None,
        None,
        None,
        None,
        ("solid_state_battery", "new_material_theme", "prototype_or_mou"),
        ("commercial_customer_absent", "mass_production_unverified", "pre_revenue_rally", "cash_burn_or_dilution"),
        "speculative_tech_price_moved_without_evidence",
        "needs_exact_stage_date_backfill",
        ("round_108.md speculative battery technology guardrail",),
        "Solid-state and new battery materials stay Watch/Red until commercialization, customers, production, margin, and FCF are proven.",
    ),
)


ROUND108_PRICE_FIELDS: tuple[str, ...] = (
    "case_id", "symbol", "company_name", "primary_archetype", "secondary_archetypes",
    "stage1_date", "stage2_date", "stage3_date", "stage4b_date", "stage4c_date",
    "stage1_price", "stage2_price", "stage3_price", "stage4b_price", "stage4c_price", "peak_price", "peak_date",
    "MFE_30D", "MFE_90D", "MFE_180D", "MFE_1Y", "MFE_2Y",
    "MAE_30D", "MAE_90D", "MAE_180D", "MAE_1Y",
    "drawdown_after_peak", "below_stage2_price_flag", "below_stage3_price_flag",
    "ev_demand_indicator", "ev_sales_growth", "ev_subsidy_change_flag", "ev_tax_credit_expiry_flag",
    "automaker_ev_cutback_flag", "ev_model_discontinued_flag", "plant_idle_flag", "layoff_furlough_flag",
    "contract_cancelled_flag", "capacity_utilization", "capex_amount", "capex_to_revenue", "capex_cut_flag",
    "ev_battery_jv_restructuring_flag", "jv_dissolution_flag", "plant_ownership_change",
    "fixed_cost_reduction_flag", "operating_loss_amount", "debt_reduction_flag",
    "ess_pivot_flag", "ess_pivot_revenue_confirmed_flag",
    "ess_contract_value", "ess_contract_duration_months", "ess_contract_customer",
    "ess_customer_disclosed_flag", "ess_use_case_disclosed_flag", "ess_contract_volume_gwh",
    "ess_capacity_gwh", "ess_capacity_utilization", "ess_margin", "ess_revenue_growth", "lfp_ess_flag",
    "grid_storage_flag", "data_center_storage_flag", "contract_extension_option_years", "disclosure_confidence_score",
    "tesla_megapack_flag", "megapack_version", "lansing_production_flag", "production_start_year",
    "opendart_rcept_no", "opendart_detail_fetched_flag", "detail_parser_confidence",
    "disclosure_signal_class", "routine_disclosure_flag", "risk_disclosure_flag", "high_signal_disclosure_flag",
    "ev_to_ess_conversion_flag", "ev_line_conversion_cost", "converted_line_capacity_gwh", "converted_line_utilization",
    "storage_customer_contract_flag", "ai_data_center_storage_customer_flag", "gross_margin_target", "catl_license_flag",
    "feoc_or_national_security_risk_flag", "battery_material_contract_value",
    "battery_material_contract_duration", "price_pass_through_flag", "raw_material_price_change",
    "contract_cancellation_reason", "expected_revenue_loss",
    "lithium_price_change", "nickel_price_change", "cobalt_price_change", "graphite_price_change", "black_mass_price",
    "metal_recovery_revenue", "recycling_volume", "recovered_material_volume", "recovery_rate", "pCAM_output",
    "graphite_supplychain_security_flag", "china_graphite_dependency_pct", "us_graphite_cost_premium",
    "policy_financing_flag", "graphite_offtake_flag", "graphite_customer_contract_flag",
    "recycling_customer_contract", "second_life_battery_flag", "second_life_grid_storage_flag", "soh_validation_flag",
    "battery_passport_compliance_flag", "battery_grading_cost", "residual_capacity_uncertainty_flag",
    "warranty_enforcement_risk_flag", "waste_treatment_volume",
    "solid_state_license_flag", "solid_state_license_capacity_gwh", "royalty_structure_flag",
    "mass_production_flag", "vehicle_series_adoption_flag", "solid_state_yield_signal",
    "solid_state_cost_signal", "commercialization_condition_flag",
    "sodium_ion_substitution_flag", "sodium_ion_customer_contract_flag", "sodium_ion_ess_flag",
    "sodium_ion_price_pressure_flag",
    "waste_treatment_capacity", "permit_asset_flag", "recurring_fcf_flag", "waste_to_energy_flag",
    "plastic_recycling_revenue", "catchment_area_population_share", "hydrogen_capex_amount",
    "hydrogen_plant_completion_date", "fuel_cell_capacity", "electrolyzer_capacity",
    "hydrogen_customer_contract", "hydrogen_subsidy_dependency", "hydrogen_capacity_utilization",
    "solar_tariff_event", "customs_detention_flag", "uflpa_flag", "feoc_flag", "component_delay_flag",
    "solar_capacity_utilization", "furlough_layoff_flag", "wind_project_delay_flag",
    "wind_project_impairment", "financing_cost_change", "foundation_cost_increase", "permitting_delay_flag",
    "grid_connection_delay_flag", "carbon_credit_price", "cbam_exposure", "carbon_accounting_revenue",
    "pass_through_ability", "ev_fire_event_flag", "bess_fire_event_flag", "battery_certification_flag",
    "battery_supplier_disclosure_flag", "recall_flag", "insurance_cost_change",
    "underground_parking_regulation_flag", "overcharge_prevention_charger_flag",
    "facility_permitting_delay_flag", "fire_safety_capex_flag", "evacuation_flag",
    "local_opposition_flag",
    "score_price_alignment", "price_validation_status", "review_notes",
)


def round108_target_for(target_id: str) -> Round108ScoreTarget | None:
    for target in ROUND108_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round108_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND108_CASE_CANDIDATES:
        target = round108_target_for(candidate.target_id)
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
                f"Round108 R3 Loop-6 case for {candidate.target_id}; "
                "EV growth, ESS contracts, recycling economics, and green-policy risks remain separated."
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
                "ev_growth_is_not_fcf_evidence",
                "do_not_invent_contract_value_margin_utilization_customer_or_stage_prices",
                "ess_lfp_storage_needs_value_duration_customer_gwh_margin",
                "battery_recycling_needs_soh_validation_and_recovered_material_revenue",
                "solar_wind_policy_requires_project_economics",
                "ev_fire_certification_is_redteam_gate",
                "lithium_is_cycle_overlay_not_structural_green_by_default",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.75 if candidate.stage1_date or candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.2,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round108_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND108_SCORE_TARGETS:
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
                "loop6_penalty_axes": "|".join(target.loop6_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round108_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND108_CASE_CANDIDATES:
        target = round108_target_for(candidate.target_id)
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


def round108_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "loop6_penalty_axes": "|".join(target.loop6_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND108_SCORE_TARGETS
    )


def round108_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round108_backfill": "true"} for field in ROUND108_PRICE_FIELDS)


def round108_summary() -> dict[str, int | bool]:
    records = round108_case_records()
    return {
        "target_count": len(ROUND108_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND108_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND108_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND108_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND108_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round108_r3_loop6_reports(
    *,
    output_directory: str | Path = ROUND108_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND108_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND108_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round108_r3_loop6_battery_ev_green_summary.md",
        "case_matrix": output / "round108_r3_loop6_case_matrix.csv",
        "stage_date_plan": output / "round108_r3_loop6_stage_date_plan.csv",
        "green_guardrails": output / "round108_r3_loop6_green_guardrails.md",
        "risk_overlays": output / "round108_r3_loop6_risk_overlays.md",
        "price_validation_plan": output / "round108_r3_loop6_price_validation_plan.md",
        "price_fields": output / "round108_r3_loop6_price_fields.csv",
    }
    _write_case_jsonl(round108_case_records(), cases)
    _write_rows(round108_score_profile_rows(), score_profiles)
    _write_rows(round108_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round108_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round108_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round108_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round108_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round108_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round108_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round108_summary_markdown() -> str:
    summary = round108_summary()
    lines = [
        "# Round-108 R3 Loop-6 Battery / EV / Green-Energy Summary",
        "",
        f"- source_round: `{ROUND108_SOURCE_ROUND_PATH}`",
        "- large_sector: `BATTERY_EV_GREEN`",
        "- loop: `R3 Loop 6 / v6.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- cyclical_success_count: {summary['cyclical_success_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
        f"- overheat_count: {summary['overheat_count']}",
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
        "- R3 Loop 6 says EV growth and durable FCF are different things.",
        "- Example: an ESS LFP contract with value, duration, customer, and GWh can be Stage 2 evidence.",
        "- Example: a $4.3B LFP contract with undisclosed customer/use-case is Stage 2 evidence with a disclosure cap.",
        "- Example: the same LFP contract becomes stronger once Tesla Megapack 3 and Lansing production are verified, but Green still needs ramp-up, utilization, ESS OPM, and FCF.",
        "- Example: SK On-Ford-style JV restructuring is Watch, because ESS pivot may help but EV demand, losses, and fixed costs are still attached.",
        "- Example: EV CAPA becomes 4C when plants idle or contracts are cancelled.",
        "- Example: BESS fire is a safety/permitting RedTeam gate, not positive storage evidence.",
        "- Example: graphite supply security is not automatic Green; cost, policy financing, and offtake must be proven.",
        "- Example: solid-state licensing is Stage 2 at most until production, vehicle adoption, royalty revenue, cost, and yield are visible.",
        "- Example: waste treatment can be Green-capable when permits, processing volume, and recurring FCF are proven.",
        "- Example: battery recycling needs SOH validation before second-life economics can be trusted.",
    ]
    return "\n".join(lines) + "\n"


def render_round108_green_guardrail_markdown() -> str:
    lines = [
        "# Round-108 R3 Loop-6 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-6 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND108_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions) or 'not_applicable'} | {', '.join(target.loop6_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R3 Loop-6 v6.0 weights to production scoring yet.",
            "- Do not treat EV growth, ESS, recycling, hydrogen, solar, wind, or lithium labels as Green evidence by themselves.",
            "- Do not invent contract value, customer, duration, GWh, margin, utilization, recovery volume, SOH, graphite cost, offtake, royalty, stage prices, or FCF.",
            "- Treat customer/use-case nondisclosure, JV dissolution, plant idle, contract cancellation, customs detention, wind impairment, lithium supply rebound, sodium-ion substitution, EV/BESS fire, speculative battery tech, and SOH opacity as RedTeam fields.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round108_risk_overlay_markdown() -> str:
    lines = [
        "# Round-108 R3 Loop-6 Risk Overlays",
        "",
        "- `EV_CAPA_FALSE_GREEN`: CAPA expansion exists, but demand slowdown, plant idle, layoff, or contract cancellation breaks the thesis.",
        "- `EV_CONTRACT_CANCELLATION_4C`: expected revenue from EV battery contracts disappears through cancellation, customer strategy change, or write-down.",
        "- `ESS_CONTRACT_ALIGNED`: ESS value, duration, customer, GWh, production route, and later margin/FCF are visible.",
        "- `ESS_TESLA_MEGAPACK_ALIGNED`: Tesla/Megapack use-case is verified, but Lansing ramp-up, utilization, ESS OPM, and FCF are still required before Green.",
        "- `ESS_DISCLOSURE_CAPPED`: contract value exists, but customer, use-case, or margin is undisclosed, so Stage 3-Green is capped.",
        "- `ESS_SHIFT_BUT_EV_OVERHANG`: ESS transition exists, but EV slowdown or idle plant still weighs on the path.",
        "- `EV_TO_ESS_REDEPLOYMENT_WATCH`: EV lines are repurposed for ESS, but customer contracts, margins, utilization, and conversion cost must be proven.",
        "- `EV_JV_RESTRUCTURING_WATCH`: JV dissolution can reduce fixed costs, but EV-demand 4C and unproven ESS pivot stay visible.",
        "- `RECYCLING_SECOND_LIFE_RISK`: recycling or second-life story ignores SOH, residual capacity, and grading cost.",
        "- `GRAPHITE_SECURITY_BUT_COST_RISK`: graphite dependency is real, but high production cost, missing policy financing, and absent offtake cap the score.",
        "- `SOLID_STATE_LICENSE_NOT_COMMERCIALIZATION`: licensing supports Stage 2, but production, vehicle adoption, royalty revenue, cost, and yield decide Stage 3.",
        "- `SOLAR_POLICY_SUPPLYCHAIN_4C`: US manufacturing/subsidy narrative breaks on customs, UFLPA, tariff, FEOC, or component detention.",
        "- `WIND_PROJECT_IMPAIRMENT_4C`: PPA/policy narrative breaks on foundation cost, financing cost, delay, or impairment.",
        "- `LITHIUM_CYCLICAL_SUCCESS_OR_FAILURE`: lithium price and ESS demand are cycle signals unless FCF/offtake are durable.",
        "- `SODIUM_ION_SUBSTITUTION_WATCH`: sodium-ion can cap lithium/LFP economics in low-cost ESS or EV use cases.",
        "- `EV_BESS_SAFETY_REGULATORY_OVERLAY`: EV/BESS fire, certification, supplier disclosure, recall, parking/charging regulation, facility permitting, or insurance cost blocks unsafe Green.",
        "- `BESS_SAFETY_PERMITTING_4C_WATCH`: BESS fire, evacuation, permitting, insurance, and local opposition can break storage project economics.",
        "- `SPECULATIVE_BATTERY_TECH_RED`: solid-state or new-material technology is not Green until commercialization, customers, scaled revenue, and FCF are visible.",
        "",
        "Simple example: `ESS 전환` is useful evidence. It is not Green if there is no contract value, margin, utilization, or FCF.",
    ]
    return "\n".join(lines) + "\n"


def render_round108_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-108 R3 Loop-6 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare EV demand, ESS contracts, factory utilization, CAPEX, mineral prices, subsidy/tariff, fire/certification, and SOH events with price path.",
        "6. Mark plant idle, contract cancellation, customs detention, wind impairment, lithium crash, EV fire regulation, and SOH opacity explicitly.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round108_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `ess_contract_aligned`: contract value, duration, customer, GWh, ESS use case, and later price/EPS path align.",
            "- `ess_tesla_megapack_stage2_watch`: Tesla/Megapack confirmation improves visibility, but ramp-up, utilization, ESS OPM, and FCF are still open.",
            "- `ess_disclosure_capped`: a large contract exists, but undisclosed customer/use-case/margin blocks Green.",
            "- `ev_battery_contract_cancellation_hard_4c`: EV contract value becomes a thesis-break signal when cancellation removes expected revenue.",
            "- `ev_capa_false_green_plus_ess_shift_watch`: EV CAPA is broken, while ESS conversion remains only Watch.",
            "- `ev_to_ess_redeployment_watch`: EV assets move toward ESS, but conversion cost, customer, utilization, and margin are not proven.",
            "- `ev_jv_restructuring_with_ess_pivot`: JV restructuring is not clean positive evidence until cost relief and ESS revenue/margin are visible.",
            "- `recycling_plus_storage_structural_reference`: recycling, recovered metals, ESS/grid services, and customers connect.",
            "- `graphite_security_but_cost_risk`: graphite supply security needs policy financing, offtake, cost path, and customers.",
            "- `solid_state_license_stage2_but_commercialization_watch`: license is not commercialization before production, vehicle adoption, royalty revenue, cost, and yield.",
            "- `solar_policy_supplychain_4c`: policy/subsidy story failed because customs, UFLPA, tariff, or component supply broke production.",
            "- `wind_project_impairment_4c`: policy/PPA story failed because project economics broke.",
            "- `battery_health_transparency_redteam`: SOH and residual-capacity opacity blocks unsafe second-life/recycling Green.",
            "- `speculative_tech_price_moved_without_evidence`: technology theme moved before commercialization, customer evidence, production, and FCF.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round108CaseCandidate) -> str:
    if "value_missing" in candidate.alignment_hint or "overhang" in candidate.alignment_hint or "capped" in candidate.alignment_hint:
        return "evidence_good_but_price_failed"
    if candidate.case_type in {"structural_success", "success_candidate", "cyclical_success"}:
        return "aligned"
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    if candidate.case_type == "failed_rerating":
        return "evidence_good_but_price_failed"
    return "false_positive_score"


def _rerating_result(candidate: Round108CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "theme_overheat"
    return "unknown" if candidate.case_type == "success_candidate" else "no_rerating"


def _score_weight_hint(target: Round108ScoreTarget) -> dict[str, float]:
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
        writer = csv.DictWriter(handle, fieldnames=tuple(rows_tuple[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows_tuple)
    return path
