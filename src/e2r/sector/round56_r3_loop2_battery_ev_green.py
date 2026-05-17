"""Round-56 R3 Loop-2 battery, EV, and green-energy pack.

Round 56 separates EV-growth narratives from durable FCF structures:
ESS contracts, recycling economics, hydrogen utilization, solar tariff risk,
wind project economics, waste-treatment permits, carbon compliance revenue,
and EV fire/regulatory overlays.

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


ROUND56_SOURCE_ROUND_PATH = "docs/round/round_56.md"
ROUND56_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round56_r3_loop2_battery_ev_green"
ROUND56_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop2_round56.jsonl"
ROUND56_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round56_r3_loop2_v2.csv"


@dataclass(frozen=True)
class Round56ScoreWeightDraft:
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
class Round56ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round56ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop2_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.BATTERY_EV_GREEN

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round56CaseCandidate:
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


ROUND56_SCORE_TARGETS: tuple[Round56ScoreTarget, ...] = (
    Round56ScoreTarget(
        "BATTERY_MATERIALS_CAPEX_OVERHEAT",
        E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round56ScoreWeightDraft(18, 13, 12, 9, 8, 0, 5),
        ("ev_growth_narrative", "long_term_supply_contract", "capa_expansion_news", "mineral_price_rebound"),
        ("real_contract", "price_margin_improvement", "op_eps_revision", "line_utilization"),
        ("long_term_contract", "price_pass_through", "fcf_after_capex", "demand_visibility"),
        ("per_pbr_overheat", "capa_race", "target_price_crowding"),
        ("ev_demand_slowdown", "raw_material_price_drop", "capa_overbuild", "customer_contract_cancelled", "plant_idle"),
        ("contract_quality", "price_pass_through", "fcf_after_capex", "demand_visibility"),
        ("ev_demand_slowdown", "capa_overbuild", "lithium_price_crash", "customer_contract_cancelled", "plant_idle"),
        ("ev_demand_slowdown", "capa_overbuild", "contract_cancellation", "mineral_price"),
        "Loop 2 lowers battery-material scores because EV demand, CAPA, contract cancellation, and mineral prices can reverse the thesis.",
    ),
    Round56ScoreTarget(
        "BATTERY_EQUIPMENT_PARTS",
        E2RArchetype.BATTERY_EQUIPMENT_PARTS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round56ScoreWeightDraft(19, 16, 11, 11, 9, 0, 5),
        ("battery_equipment_order", "cell_customer_capex", "delivery_schedule_keyword"),
        ("customer_order", "delivery_schedule", "margin_visibility", "revenue_conversion"),
        ("order_to_revenue_conversion", "customer_diversification", "op_eps_revision"),
        ("equipment_capex_cycle_crowded", "cell_capex_peak"),
        ("customer_capex_cut", "delivery_delay", "margin_miss", "single_customer"),
        ("customer_order", "delivery_schedule", "margin_visibility", "op_eps_revision"),
        ("customer_capex_cut", "delivery_delay", "single_customer"),
        ("customer_capex_cut", "delivery_delay"),
        "Battery equipment is Watch-to-Green only when customer CAPEX becomes delivery, revenue, and margin.",
    ),
    Round56ScoreTarget(
        "BATTERY_RECYCLING_ESS_SHIFT",
        E2RArchetype.BATTERY_RECYCLING_ESS_SHIFT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round56ScoreWeightDraft(21, 18, 14, 11, 10, 0, 5),
        ("ess_shift", "battery_recycling", "lfp_ess_production", "black_mass", "second_life_battery"),
        ("ess_customer_contract", "ess_contract_value", "ess_contract_duration", "recycling_volume", "metal_recovery_revenue"),
        ("recurring_ess_or_recycling_fcf", "ess_margin", "capacity_utilization", "ev_slowdown_offset"),
        ("ess_narrative_crowded", "recycling_premium_overheat"),
        ("recycling_volume_shortfall", "metal_price_drop", "ess_margin_miss", "customer_demand_slowdown"),
        ("ess_contract", "capacity_utilization", "recycling_volume", "metal_recovery_revenue", "fcf_margin"),
        ("contract_value_missing", "recycling_volume_shortfall", "metal_price_drop", "ess_margin_miss"),
        ("ess_margin", "recycling_volume", "contract_value_missing"),
        "ESS/recycling earns higher Loop-2 credit only when contracts, duration, volume, and margin are visible.",
    ),
    Round56ScoreTarget(
        "EV_INFRASTRUCTURE",
        E2RArchetype.EV_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round56ScoreWeightDraft(16, 13, 7, 10, 8, 0, 5),
        ("charging_station", "charger_installation", "ev_infrastructure_policy", "fast_charging"),
        ("utilization", "recurring_revenue", "subsidy_visibility"),
        ("profitable_utilization", "repeat_revenue", "subsidy_independent_margin"),
        ("ev_charging_theme_crowded",),
        ("low_utilization", "subsidy_cut", "fire_regulation", "maintenance_cost"),
        ("utilization", "recurring_revenue", "profitability"),
        ("low_utilization", "subsidy_dependency", "fire_regulation"),
        ("utilization", "fire_regulation", "subsidy_dependency"),
        "EV infrastructure needs usage and unit economics, not charger count or subsidy headlines.",
    ),
    Round56ScoreTarget(
        "HYDROGEN_FUEL_CELL_INFRA",
        E2RArchetype.HYDROGEN_FUEL_CELL_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round56ScoreWeightDraft(18, 18, 12, 12, 10, 0, 5),
        ("hydrogen_fuel_cell_factory", "hydrogen_policy", "electrolyzer_or_commercial_vehicle", "hydrogen_capex"),
        ("customer_or_demand_source", "production_capacity", "delivery_contract", "plant_completion_date"),
        ("utilization", "op_eps_conversion", "subsidy_independent_economics"),
        ("hydrogen_theme_overheat",),
        ("subsidy_cut", "customer_absent", "low_utilization", "project_delay"),
        ("customer_demand", "production_capacity", "utilization", "op_eps_conversion"),
        ("subsidy_dependency", "customer_absent", "low_utilization"),
        ("customer_absent", "utilization", "subsidy_dependency"),
        "Hydrogen CAPEX is stronger than policy talk, but Green needs customers, utilization, and OP conversion.",
    ),
    Round56ScoreTarget(
        "SOLAR_TARIFF_SUPPLYCHAIN",
        E2RArchetype.SOLAR_TARIFF_SUPPLYCHAIN,
        Round10ThemePosture.REDTEAM_FIRST,
        Round56ScoreWeightDraft(17, 14, 11, 10, 8, 0, 5),
        ("solar_factory", "subsidy_policy", "module_or_cell_demand", "us_factory"),
        ("utilization", "customer_contract", "supply_chain_stable", "op_turnaround"),
        ("subsidy_independent_fcf", "supply_chain_clean", "margin_visible"),
        ("solar_manufacturing_narrative_crowded", "subsidy_premium"),
        ("tariff_risk", "customs_detention", "uflpa_detention", "feoc_risk", "worker_furlough", "production_disruption"),
        ("utilization", "customer_contract", "supply_chain_stable", "fcf_margin"),
        ("tariff_risk", "customs_detention", "uflpa_detention", "subsidy_dependency", "feoc_risk"),
        ("customs", "tariff", "uflpa", "supply_chain_disruption"),
        "Solar is RedTeam-first because subsidies and tariff/customs breaks can arrive together.",
    ),
    Round56ScoreTarget(
        "RENEWABLE_ENERGY_POLICY",
        E2RArchetype.RENEWABLE_ENERGY_POLICY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round56ScoreWeightDraft(17, 14, 9, 10, 8, 0, 5),
        ("wind_or_renewable_project", "carbon_policy", "ppa_or_project_news"),
        ("permitted_project", "funding_visible", "cost_schedule_visible", "construction_start"),
        ("project_economics", "op_eps_conversion", "cost_controlled", "repeat_project_backlog"),
        ("renewable_policy_crowded", "project_premium"),
        ("permitting_delay", "financing_cost", "cost_overrun", "project_delay", "impairment", "foundation_cost"),
        ("permitting", "funding", "cost_schedule", "margin_visibility"),
        ("permitting_delay", "financing_cost", "cost_overrun", "impairment"),
        ("rates", "cost_overrun", "permitting", "impairment"),
        "Wind and renewables stay Watch until project economics survive rates, permits, and cost pressure.",
    ),
    Round56ScoreTarget(
        "ENERGY_DISTRIBUTION_FUEL",
        E2RArchetype.ENERGY_DISTRIBUTION_FUEL,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round56ScoreWeightDraft(18, 15, 16, 10, 10, 2, 5),
        ("lng_or_lpg_distribution", "fuel_spread", "energy_price_move"),
        ("spread_improvement", "inventory_status", "demand_visibility"),
        ("repeat_spread_margin", "fcf_defense", "capital_allocation_disciplined"),
        ("fuel_spread_crowded",),
        ("energy_price_reversal", "inventory_loss", "tariff_or_policy_shock"),
        ("spread_improvement", "inventory_status", "fcf_margin"),
        ("price_reversal", "inventory_loss", "policy_shock"),
        ("energy_price", "inventory", "policy"),
        "Energy distribution is spread/cycle driven and should carry cycle caps.",
    ),
    Round56ScoreTarget(
        "WASTE_RECYCLING_ENVIRONMENT",
        E2RArchetype.WASTE_RECYCLING_ENVIRONMENT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round56ScoreWeightDraft(18, 22, 15, 13, 12, 3, 5),
        ("waste_treatment_platform", "recycling_demand", "permit_value", "waste_to_energy"),
        ("treatment_volume", "long_term_contract", "utilization", "fcf_visible"),
        ("permit_asset", "recurring_fcf", "valuation_frame_change", "mna_value_support"),
        ("waste_mna_premium_crowded", "permit_value_fully_priced"),
        ("utilization_drop", "capex_burden", "metal_price_drop", "regulatory_cost"),
        ("permit_asset", "treatment_volume", "utilization", "recurring_fcf"),
        ("utilization_drop", "capex_burden", "commodity_recycling_price_drop"),
        ("utilization", "capex", "metal_price"),
        "Waste treatment remains the clearest R3 Green-capable axis when permits, volume, and recurring FCF are proven.",
    ),
    Round56ScoreTarget(
        "CARBON_CREDIT_CBAM_COMPLIANCE",
        E2RArchetype.CARBON_CREDIT_CBAM_COMPLIANCE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round56ScoreWeightDraft(14, 17, 10, 12, 8, 2, 6),
        ("eu_ets_or_cbam_policy", "carbon_accounting", "compliance_monitoring"),
        ("carbon_accounting_revenue", "verification_revenue", "low_carbon_product_premium"),
        ("recurring_compliance_revenue", "cost_pass_through", "industrial_customer_base"),
        ("carbon_price_theme_crowded",),
        ("carbon_price_drop", "free_allowance_expansion", "greenwashing_risk", "policy_delay"),
        ("recurring_revenue", "verification_customer", "cost_pass_through"),
        ("carbon_price_volatility", "greenwashing", "policy_reversal"),
        ("policy_reform", "carbon_price", "greenwashing"),
        "Carbon credits alone are Watch; compliance software/service revenue is the stronger route.",
    ),
    Round56ScoreTarget(
        "DATA_CENTER_WATER_REUSE_INFRA",
        E2RArchetype.DATA_CENTER_WATER_REUSE_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round56ScoreWeightDraft(16, 18, 14, 12, 10, 2, 5),
        ("ai_datacenter_water_use", "water_reuse", "closed_loop_cooling", "water_treatment"),
        ("data_center_customer", "reuse_project", "contracted_revenue"),
        ("repeat_water_reuse_revenue", "margin_visible", "local_permit_support"),
        ("water_reuse_theme_crowded",),
        ("customer_absent", "local_opposition", "unit_economics_weak", "permitting_delay"),
        ("data_center_customer", "contracted_revenue", "unit_economics"),
        ("customer_absent", "local_opposition", "weak_economics"),
        ("customer_absent", "local_opposition", "economics"),
        "Data-center water reuse is Watch-to-Green only with named customers and economics.",
    ),
    Round56ScoreTarget(
        "EV_FIRE_RISK_OVERLAY",
        E2RArchetype.EV_FIRE_RISK_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round56ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("ev_fire", "battery_recall", "insurance_cost", "regulatory_investigation", "battery_certification"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("battery_fire", "certification_requirement", "battery_supplier_disclosure", "recall", "insurance_cost", "parking_charging_regulation"),
        (),
        ("battery_fire", "certification_requirement", "recall", "insurance_cost", "fire_regulation"),
        ("fire", "certification", "recall", "insurance"),
        "EV fire/certification/recall/regulation overlay is a hard RedTeam gate, not a positive score bucket.",
        gate_only=True,
    ),
)


ROUND56_CASE_CANDIDATES: tuple[Round56CaseCandidate, ...] = (
    Round56CaseCandidate(
        "lg_energy_solution_ess_shift_case",
        "BATTERY_RECYCLING_ESS_SHIFT",
        "373220",
        "LG에너지솔루션 ESS 전환",
        "KR",
        "success_candidate",
        None,
        date(2025, 7, 25),
        None,
        None,
        None,
        ("ess_shift", "lfp_ess_capacity_expansion", "ess_capacity_17_to_30gwh", "q2_op_profit", "ira_credit_dependency"),
        ("ev_demand_slowdown", "tariff_policy_risk", "event_day_price_decline", "ira_credit_excluded_profit_low"),
        "ess_shift_but_price_failed",
        "needs_price_backfill",
        ("round_56.md Reuters LG Energy Solution ESS shift",),
        "ESS shift is positive, but event-day price weakness shows EV slowdown and credit dependency still matter.",
    ),
    Round56CaseCandidate(
        "lg_energy_tesla_lfp_ess_contract_case",
        "BATTERY_RECYCLING_ESS_SHIFT",
        "373220_TESLA_ESS",
        "LGES-Tesla LFP ESS supply contract",
        "KR",
        "success_candidate",
        None,
        date(2025, 7, 30),
        None,
        None,
        None,
        ("ess_contract_value_4_3b", "ess_contract_duration_36m", "tesla_customer", "lfp_ess_us_production", "extension_option_7y"),
        ("ess_margin_unverified", "ev_slowdown_overhang"),
        "ess_contract_aligned",
        "needs_price_backfill",
        ("round_56.md WSJ LG Energy Tesla ESS deal",),
        "Contract value, duration, customer, and ESS use case make this a strong Stage 2 candidate, but margin and MFE still need backfill.",
    ),
    Round56CaseCandidate(
        "sk_on_flatiron_ess_7_2gwh_case",
        "BATTERY_RECYCLING_ESS_SHIFT",
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
        ("contract_value_missing", "ess_margin_unverified", "customer_demand_unverified"),
        "ess_contract_stage2_value_missing",
        "needs_price_backfill",
        ("round_56.md Reuters SK On Flatiron ESS deal",),
        "Volume and duration support Stage 2, but missing contract value caps EPS/FCF credit.",
    ),
    Round56CaseCandidate(
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
        ("private_company_reference", "recycling_margin_unverified", "public_price_unavailable"),
        "battery_recycling_energy_storage_reference",
        "missing_public_price_data",
        ("round_56.md Reuters Redwood recycling funding",),
        "Recycling becomes stronger when recovered metals, ESS use case, customers, and data-center power demand connect.",
    ),
    Round56CaseCandidate(
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
        ("customer_absent", "subsidy_dependency", "low_utilization"),
        "hydrogen_capex_stage1_to_stage2_candidate",
        "needs_price_backfill",
        ("round_56.md Reuters Hyundai hydrogen fuel-cell plant",),
        "Actual CAPEX is stronger than policy talk, but customers, utilization, and OP conversion are still required.",
    ),
    Round56CaseCandidate(
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
        ("waste_treatment_platform", "permit_asset", "recycling_operation", "waste_to_energy", "mna_value_1tn_krw", "metro_area_coverage"),
        ("utilization_drop", "capex_burden"),
        "recycling_infra_success",
        "missing_public_price_data",
        ("round_56.md Reuters EQT KJ Environment platform",),
        "Waste treatment is the clearest R3 Green-capable reference when permits, facilities, processing volume, and recurring FCF are visible.",
    ),
    Round56CaseCandidate(
        "gm_lg_ultium_ohio_idle_case",
        "BATTERY_MATERIALS_CAPEX_OVERHEAT",
        "GM_LG_ULTIUM_REF",
        "GM-LG Ultium Ohio plant idle",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 12),
        ("ev_battery_capa", "ess_shift_candidate"),
        ("ev_demand_slowdown", "plant_idle", "layoff_furlough", "capacity_underutilization", "restart_uncertain"),
        "ev_capa_false_green",
        "needs_price_backfill",
        ("round_56.md Reuters GM-LG Ohio battery plant",),
        "EV battery CAPA can become hard 4C when plant restart, utilization, and jobs are uncertain.",
    ),
    Round56CaseCandidate(
        "ford_lges_ev_contract_cancel_case",
        "BATTERY_MATERIALS_CAPEX_OVERHEAT",
        "FORD_LGES_CANCEL_REF",
        "Ford-LGES EV battery contract cancellation",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 12, 17),
        ("ev_battery_contract", "ford_ev_program"),
        ("contract_cancelled", "ev_model_cutback", "write_down_19_5b", "policy_shift", "ev_demand_slowdown"),
        "ev_battery_contract_cancellation_4c",
        "needs_price_backfill",
        ("round_56.md Reuters Ford LGES contract cancellation",),
        "EV battery long-term contracts must be checked against customer strategy and policy risk; cancellation is 4C.",
    ),
    Round56CaseCandidate(
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
        ("round_56.md Reuters Qcells customs detention",),
        "Solar subsidy and US manufacturing narrative can break when customs and component supply stop production.",
    ),
    Round56CaseCandidate(
        "orsted_sunrise_wind_impairment_case",
        "RENEWABLE_ENERGY_POLICY",
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
        ("round_56.md Reuters Orsted Sunrise Wind impairment",),
        "Renewable policy and PPAs cannot overcome project economics when rates, foundations, and delay create impairment.",
    ),
    Round56CaseCandidate(
        "lithium_price_86pct_crash_case",
        "BATTERY_MATERIALS_CAPEX_OVERHEAT",
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
        ("lithium_price_crash", "raw_material_price_drop", "mine_restart_cap", "supply_rebound"),
        "lithium_cycle_hard_counterexample",
        "missing_price_data",
        ("round_56.md Reuters lithium prices after crash",),
        "Lithium rebound is not structural Green without cost curve, offtake, FCF, and CAPEX discipline.",
    ),
    Round56CaseCandidate(
        "albemarle_cost_cut_low_lithium_case",
        "BATTERY_MATERIALS_CAPEX_OVERHEAT",
        "ALB",
        "Albemarle low lithium cost-cut survival",
        "US",
        "cyclical_success",
        None,
        date(2025, 2, 12),
        None,
        None,
        None,
        ("cost_cut", "quarterly_profit", "capex_cut", "after_hours_price_up_2_5pct"),
        ("lithium_price_drop_53pct", "revenue_drop_1_1b", "capex_cut"),
        "lithium_cyclical_success_or_failure",
        "needs_price_backfill",
        ("round_56.md Reuters Albemarle cost cuts",),
        "Cost cuts can stabilize price reaction, but this is cycle survival rather than structural Green.",
    ),
    Round56CaseCandidate(
        "korea_ev_battery_certification_fire_case",
        "EV_FIRE_RISK_OVERLAY",
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
        ("round_56.md Reuters Korea EV battery certification",),
        "EV fire and certification should become a separate RedTeam overlay for battery, charging, and ESS candidates.",
    ),
)


ROUND56_PRICE_FIELDS: tuple[str, ...] = (
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
    "ev_demand_indicator",
    "ev_sales_growth",
    "ev_subsidy_change_flag",
    "ev_tax_credit_expiry_flag",
    "automaker_ev_cutback_flag",
    "plant_idle_flag",
    "layoff_furlough_flag",
    "contract_cancelled_flag",
    "capacity_utilization",
    "capex_amount",
    "capex_to_revenue",
    "capex_cut_flag",
    "ess_contract_value",
    "ess_contract_duration_months",
    "ess_contract_customer",
    "ess_contract_volume_gwh",
    "ess_capacity_gwh",
    "ess_capacity_utilization",
    "ess_margin",
    "ess_revenue_growth",
    "lfp_ess_flag",
    "battery_material_contract_value",
    "battery_material_contract_duration",
    "price_pass_through_flag",
    "raw_material_price_change",
    "lithium_price_change",
    "nickel_price_change",
    "cobalt_price_change",
    "black_mass_price",
    "metal_recovery_revenue",
    "recycling_volume",
    "recovered_material_volume",
    "pCAM_output",
    "recycling_customer_contract",
    "waste_treatment_volume",
    "waste_treatment_capacity",
    "permit_asset_flag",
    "recurring_fcf_flag",
    "hydrogen_capex_amount",
    "hydrogen_plant_completion_date",
    "fuel_cell_capacity",
    "electrolyzer_capacity",
    "hydrogen_customer_contract",
    "hydrogen_subsidy_dependency",
    "solar_tariff_event",
    "customs_detention_flag",
    "uflpa_flag",
    "feoc_flag",
    "component_delay_flag",
    "solar_capacity_utilization",
    "furlough_layoff_flag",
    "wind_project_delay_flag",
    "wind_project_impairment",
    "financing_cost_change",
    "foundation_cost_increase",
    "permitting_delay_flag",
    "carbon_credit_price",
    "cbam_exposure",
    "carbon_accounting_revenue",
    "pass_through_ability",
    "ev_fire_event_flag",
    "battery_certification_flag",
    "battery_supplier_disclosure_flag",
    "recall_flag",
    "insurance_cost_change",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def target_for(target_id: str) -> Round56ScoreTarget | None:
    for target in ROUND56_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round56_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND56_CASE_CANDIDATES:
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
                f"Round56 R3 Loop-2 case for {candidate.target_id}; "
                "EV growth narrative and durable FCF structure remain separated."
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
                "do_not_invent_contract_value_margin_utilization_or_stage_prices",
                "ess_shift_needs_contract_value_duration_margin_or_utilization",
                "battery_material_capa_requires_ev_demand_and_fcf_validation",
                "solar_wind_policy_requires_project_economics",
                "ev_fire_certification_is_redteam_gate",
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


def round56_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND56_SCORE_TARGETS:
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
                "loop2_penalty_axes": "|".join(target.loop2_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round56_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND56_CASE_CANDIDATES:
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


def round56_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "loop2_penalty_axes": "|".join(target.loop2_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND56_SCORE_TARGETS
    )


def round56_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round56_backfill": "true"} for field in ROUND56_PRICE_FIELDS)


def round56_summary() -> dict[str, int | bool]:
    records = round56_case_records()
    return {
        "target_count": len(ROUND56_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND56_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND56_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND56_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND56_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round56_r3_loop2_reports(
    *,
    output_directory: str | Path = ROUND56_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND56_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND56_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round56_r3_loop2_battery_ev_green_summary.md",
        "case_matrix": output / "round56_r3_loop2_case_matrix.csv",
        "stage_date_plan": output / "round56_r3_loop2_stage_date_plan.csv",
        "green_guardrails": output / "round56_r3_loop2_green_guardrails.md",
        "risk_overlays": output / "round56_r3_loop2_risk_overlays.md",
        "price_validation_plan": output / "round56_r3_loop2_price_validation_plan.md",
        "price_fields": output / "round56_r3_loop2_price_fields.csv",
    }
    _write_case_jsonl(round56_case_records(), cases)
    _write_rows(round56_score_profile_rows(), score_profiles)
    _write_rows(round56_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round56_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round56_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round56_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round56_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round56_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round56_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round56_summary_markdown() -> str:
    summary = round56_summary()
    lines = [
        "# Round-56 R3 Loop-2 Battery / EV / Green-Energy Summary",
        "",
        f"- source_round: `{ROUND56_SOURCE_ROUND_PATH}`",
        "- large_sector: `BATTERY_EV_GREEN`",
        "- loop: `R3 Loop 2 / v2.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- cyclical_success_count: {summary['cyclical_success_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
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
        "- R3 Loop 2 says EV growth and durable FCF are different things.",
        "- Example: an ESS contract with value, duration, customer, and utilization can be Stage 2 evidence.",
        "- Example: EV CAPA can become 4C when plants idle or contracts are cancelled.",
        "- Example: waste treatment can be Green-capable when permits, processing volume, and recurring FCF are proven.",
        "- Example: solar and wind policy headlines stay Watch/Red when customs, tariff, financing, or impairment risk is unresolved.",
    ]
    return "\n".join(lines) + "\n"


def render_round56_green_guardrail_markdown() -> str:
    lines = [
        "# Round-56 R3 Loop-2 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-2 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND56_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.loop2_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R3 Loop-2 v2.0 weights to production scoring yet.",
            "- Do not treat EV growth, ESS transition, recycling, hydrogen, solar, or wind labels as Green evidence by themselves.",
            "- Do not invent contract values, margins, utilization, recovery volume, stage prices, or FCF.",
            "- Treat plant idle, contract cancellation, customs detention, wind impairment, lithium crash, and EV fire/certification as RedTeam fields.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round56_risk_overlay_markdown() -> str:
    lines = [
        "# Round-56 R3 Loop-2 Risk Overlays",
        "",
        "- `EV_CAPA_FALSE_GREEN`: CAPA expansion exists, but demand slowdown, plant idle, or contract cancellation breaks the thesis.",
        "- `ESS_CONTRACT_ALIGNED`: ESS value, duration, customer, and production route are visible.",
        "- `ESS_SHIFT_BUT_PRICE_FAILED`: ESS shift exists, but EV slowdown, subsidy, or margin concern dominates price.",
        "- `RECYCLING_INFRA_SUCCESS`: permits, processing volume, recovered materials, customers, and recurring FCF align.",
        "- `SOLAR_POLICY_SUPPLYCHAIN_4C`: US manufacturing/subsidy narrative breaks on customs, UFLPA, tariff, or component detention.",
        "- `WIND_PROJECT_IMPAIRMENT_4C`: PPA/policy narrative breaks on foundation cost, financing cost, delay, or impairment.",
        "- `LITHIUM_CYCLICAL_SUCCESS_OR_FAILURE`: lithium price and cost-cut moves are cycle signals unless FCF/offtake are durable.",
        "- `EV_FIRE_REGULATORY_OVERLAY`: fire, certification, supplier disclosure, recall, or insurance cost blocks unsafe Green.",
        "",
        "Simple example: `ESS 전환` is useful evidence. It is not Green if the record only says a line may be converted and does not show contract value, margin, utilization, or FCF.",
    ]
    return "\n".join(lines) + "\n"


def render_round56_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-56 R3 Loop-2 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare EV demand, ESS contract, utilization, CAPEX, mineral prices, subsidies, customs/tariffs, and price path.",
        "6. Mark plant idle, contract cancellation, customs detention, wind impairment, lithium crash, and EV fire regulation explicitly.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round56_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `ess_contract_aligned`: contract value, duration, customer, ESS use case, and later price/EPS path align.",
            "- `ess_shift_but_price_failed`: ESS transition exists but EV slowdown or subsidy risk suppresses price.",
            "- `ev_capa_false_green`: CAPA expansion was scored positively before utilization or customer demand failed.",
            "- `solar_policy_supplychain_4c`: policy/subsidy story failed because customs, UFLPA, tariff, or component supply broke production.",
            "- `wind_project_impairment_4c`: policy/PPA story failed because project economics broke.",
            "- `ev_fire_regulatory_overlay`: fire/certification/retrieval risk blocks unsafe Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round56CaseCandidate) -> str:
    if "price_failed" in candidate.alignment_hint or "overhang" in candidate.alignment_hint:
        return "evidence_good_but_price_failed"
    if candidate.case_type in {"structural_success", "success_candidate", "cyclical_success"}:
        return "aligned"
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    return "false_positive_score"


def _rerating_result(candidate: Round56CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "4b_watch":
        return "theme_overheat"
    if candidate.case_type == "overheat":
        return "theme_overheat"
    return "unknown" if candidate.case_type == "success_candidate" else "no_rerating"


def _score_weight_hint(target: Round56ScoreTarget) -> dict[str, float]:
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
    "ROUND56_CASE_CANDIDATES",
    "ROUND56_DEFAULT_CASES_PATH",
    "ROUND56_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND56_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND56_PRICE_FIELDS",
    "ROUND56_SCORE_TARGETS",
    "Round56CaseCandidate",
    "Round56ScoreTarget",
    "Round56ScoreWeightDraft",
    "render_round56_green_guardrail_markdown",
    "render_round56_price_validation_plan_markdown",
    "render_round56_risk_overlay_markdown",
    "render_round56_summary_markdown",
    "round56_case_candidate_rows",
    "round56_case_records",
    "round56_price_field_rows",
    "round56_score_profile_rows",
    "round56_stage_date_rows",
    "round56_summary",
    "target_for",
    "write_round56_r3_loop2_reports",
]
