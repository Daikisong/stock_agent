"""Round-49 R9 mobility, transport, and leisure calibration pack.

Round 49 separates auto value-up and high-value component rerating from
airline, shipping, tourism, rental, micromobility, eVTOL, and space-theme
cycles. R9 can be Green-eligible only in narrow paths where OPM, FCF, capital
return, backlog, or recurring connectivity revenue are visible. Most transport
and leisure cases remain Watch/RedTeam until cycle, policy-event, fuel/FX,
residual-value, certification, debt, and cash-burn risks are resolved.

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


ROUND49_SOURCE_ROUND_PATH = "docs/round/round_49.md"
ROUND49_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round49_r9_mobility_transport_leisure"
ROUND49_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r9_round49.jsonl"
ROUND49_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round49_r9_v1.csv"


@dataclass(frozen=True)
class Round49ScoreWeightDraft:
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
class Round49ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round49ScoreWeightDraft
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
        return Round10LargeSector.MOBILITY_TRANSPORT_LEISURE

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round49CaseCandidate:
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


ROUND49_SCORE_TARGETS: tuple[Round49ScoreTarget, ...] = (
    Round49ScoreTarget(
        "AUTO_MOBILITY_COMPLETED_VEHICLE",
        E2RArchetype.AUTO_MOBILITY_COMPLETED_VEHICLE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round49ScoreWeightDraft(20, 18, 10, 15, 17, 10, 5),
        ("hybrid_demand", "ev_slowdown_response", "shareholder_return", "export_mix"),
        ("op_fcf_stability", "sales_target", "buyback_or_dividend", "roe_pbr_rerating"),
        ("fcf_supports_return", "high_margin_mix", "old_auto_discount_removed"),
        ("valueup_narrative_crowded", "peak_margin_ignored"),
        ("tariff_hit", "recall_cost", "demand_slowdown", "peak_margin_reversal"),
        ("op_fcf_stability", "hybrid_or_mix_improvement", "shareholder_return", "roe_pbr_rerating", "tariff_risk_low"),
        ("tariff", "recall", "peak_margin", "policy_risk", "demand_slowdown"),
        "Completed vehicles can be Green only when FCF, mix, and return execution are source-backed.",
    ),
    Round49ScoreTarget(
        "AUTO_MOBILITY_COMPONENTS",
        E2RArchetype.AUTO_MOBILITY_COMPONENTS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round49ScoreWeightDraft(20, 17, 10, 14, 14, 3, 5),
        ("auto_parts_order", "electronics_component", "lighting_or_adas_demand"),
        ("customer_diversification", "cost_pass_through", "op_eps_revision", "raw_material_stable"),
        ("repeat_program_visibility", "high_value_mix", "quality_cost_low"),
        ("component_group_crowded",),
        ("customer_program_cut", "quality_recall", "raw_material_squeeze", "oem_pressure"),
        ("customer_diversification", "cost_pass_through", "op_eps_revision", "quality_cost_low"),
        ("customer_concentration", "raw_material", "quality_cost", "oem_pressure"),
        "Auto components need customer mix and cost pass-through, not OEM volume alone.",
    ),
    Round49ScoreTarget(
        "TIRE_AUTO_COMPONENT_SPREAD",
        E2RArchetype.TIRE_AUTO_COMPONENT_SPREAD,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round49ScoreWeightDraft(18, 13, 12, 11, 10, 2, 5),
        ("tire_demand_recovery", "raw_material_spread", "replacement_market"),
        ("oe_re_mix", "op_eps_revision", "north_america_demand_stable"),
        ("spread_fcf_persistent", "china_competition_controlled"),
        ("spread_peak_ignored",),
        ("north_america_demand_slowdown", "raw_material_spike", "tariff_hit", "vehicle_sales_slowdown"),
        ("oe_re_mix", "raw_material_spread", "op_eps_revision", "fcf_margin"),
        ("north_america_demand", "raw_material", "china_competition", "tariff"),
        "Tire Green is restricted; demand recovery must become margin and FCF.",
    ),
    Round49ScoreTarget(
        "AIRLINE_TRAVEL_CYCLE",
        E2RArchetype.AIRLINE_TRAVEL_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round49ScoreWeightDraft(18, 14, 5, 12, 10, 2, 5),
        ("passenger_recovery", "cargo_rate", "airline_merger", "reopening_news"),
        ("revenue_op_improvement", "integration_synergy", "passenger_cargo_mix"),
        ("fcf_cost_stability", "fuel_fx_risk_low"),
        ("integration_or_reopening_crowded",),
        ("fuel_shock", "fx_loss", "integration_cost", "cargo_passenger_slowdown"),
        ("load_factor", "yield_or_margin", "fuel_fx_risk_low", "integration_cost_controlled"),
        ("fuel", "fx", "integration_cost", "cargo_cycle", "regulatory_condition"),
        "Airline recovery is Watch-first; traffic without margin is not Green evidence.",
    ),
    Round49ScoreTarget(
        "TRAVEL_LEISURE_REOPENING",
        E2RArchetype.TRAVEL_LEISURE_REOPENING,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round49ScoreWeightDraft(17, 13, 5, 12, 10, 1, 5),
        ("tourist_recovery", "hotel_occupancy", "leisure_reopening"),
        ("revpar_improvement", "op_leverage", "visitor_spend"),
        ("repeat_travel_spend", "occupancy_and_margin_visible"),
        ("reopening_policy_crowded",),
        ("visitor_mix_weak", "occupancy_slowdown", "cost_inflation"),
        ("visitor_spend", "hotel_occupancy", "revpar", "opm_improvement"),
        ("tourist_mix", "policy_event_only", "cost_inflation", "occupancy_slowdown"),
        "Travel needs spend and operating leverage, not arrival headlines alone.",
    ),
    Round49ScoreTarget(
        "CASINO_DUTYFREE_TOURISM",
        E2RArchetype.CASINO_DUTYFREE_TOURISM,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round49ScoreWeightDraft(18, 13, 5, 12, 10, 2, 5),
        ("visa_policy", "china_group_tourism", "casino_dutyfree_recovery"),
        ("tourist_spend", "drop_amount", "duty_free_sales", "hotel_occupancy", "op_leverage"),
        ("visitor_mix_diversified", "china_dependence_lower", "cashflow_margin_visible"),
        ("tourism_policy_rally_crowded",),
        ("drop_slowdown", "duty_free_asp_weak", "china_mix_weak", "capex_burden"),
        ("tourist_arrivals", "casino_drop_amount", "duty_free_sales", "opm_improvement"),
        ("china_dependence", "drop_amount", "capex", "policy_event_only"),
        "Tourism policy is Stage 1 until actual spend, drop, ASP, and OPM are visible.",
    ),
    Round49ScoreTarget(
        "SHIPPING_FREIGHT_CYCLE",
        E2RArchetype.SHIPPING_FREIGHT_CYCLE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round49ScoreWeightDraft(20, 8, 18, 8, 8, 0, 5),
        ("freight_rate_spike", "red_sea_disruption", "capacity_adjustment"),
        ("freight_rate_index", "ebitda_improvement", "cash_or_dividend"),
        ("multi_year_supply_discipline", "contract_rate_visibility"),
        ("freight_peak", "shipping_stock_crowded"),
        ("freight_rate_collapse", "overcapacity", "new_ship_delivery", "route_normalization", "earnings_collapse"),
        ("contract_vs_spot_rate", "fleet_capacity_discipline", "ebitda_cashflow", "overcapacity_low"),
        ("overcapacity", "freight_peak", "demand_slowdown", "route_normalization"),
        "Shipping is cycle-heavy; structural Green is highly restricted.",
    ),
    Round49ScoreTarget(
        "LOGISTICS_PARCEL_FREIGHT",
        E2RArchetype.LOGISTICS_PARCEL_FREIGHT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round49ScoreWeightDraft(18, 15, 6, 12, 10, 2, 5),
        ("parcel_volume", "freight_volume", "network_efficiency"),
        ("unit_price_stable", "labor_cost_control", "opm_improvement"),
        ("network_density_advantage", "recurring_shipper_contract"),
        ("logistics_efficiency_crowded",),
        ("unit_price_pressure", "labor_cost_spike", "volume_slowdown"),
        ("volume_growth", "unit_price_stable", "labor_cost_control", "opm_improvement"),
        ("unit_price_pressure", "labor_cost", "volume_slowdown"),
        "Logistics needs unit price and labor-cost control, not volume alone.",
    ),
    Round49ScoreTarget(
        "RENTAL_USED_CAR_MOBILITY",
        E2RArchetype.RENTAL_USED_CAR_MOBILITY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round49ScoreWeightDraft(17, 14, 6, 12, 10, 1, 5),
        ("rental_demand", "used_car_price", "fleet_strategy"),
        ("fleet_margin", "residual_value_stable", "repair_cost_control", "utilization_rate"),
        ("asset_turnover_and_fcf", "residual_value_resilient"),
        ("fleet_strategy_crowded",),
        ("residual_value_drop", "repair_cost_spike", "interest_cost", "fleet_writedown"),
        ("residual_value", "repair_cost_per_vehicle", "utilization_rate", "fcf_margin"),
        ("residual_value", "repair_cost", "interest_rate", "fleet_writedown"),
        "Rental and used-car stories need unit economics and residual value.",
    ),
    Round49ScoreTarget(
        "MOBILITY_RENTAL_MICROMOBILITY",
        E2RArchetype.MOBILITY_RENTAL_MICROMOBILITY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round49ScoreWeightDraft(17, 14, 6, 12, 10, 1, 5),
        ("ipo_filing", "city_expansion", "ridership_growth"),
        ("revenue_growth", "fcf_positive", "unit_economics", "utilization_rate"),
        ("recurring_usage", "debt_stability", "regulatory_risk_controlled"),
        ("ipo_valuation_crowded",),
        ("debt_maturity", "regulatory_restriction", "seasonality_loss", "repair_cost_spike"),
        ("micromobility_revenue", "micromobility_fcf", "utilization_rate", "debt_maturity_manageable"),
        ("unit_economics", "debt", "regulation", "seasonality"),
        "Micromobility needs FCF and debt stability; rides or city count alone is not enough.",
    ),
    Round49ScoreTarget(
        "AUTO_COMPONENTS_EV_ADAS",
        E2RArchetype.AUTO_COMPONENTS_EV_ADAS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round49ScoreWeightDraft(18, 16, 9, 13, 11, 0, 5),
        ("adas_adoption", "sensor_or_camera_order", "ev_component_demand"),
        ("actual_adoption", "customer_diversification", "development_cost_control"),
        ("content_per_vehicle_growth", "multi_customer_program"),
        ("adas_theme_crowded",),
        ("customer_concentration", "development_cost", "ev_slowdown", "program_delay"),
        ("actual_adoption", "customer_diversification", "op_eps_revision"),
        ("actual_adoption_missing", "customer_concentration", "development_cost"),
        "ADAS parts need adoption and customer diversification, not autonomy theme labels.",
    ),
    Round49ScoreTarget(
        "URBAN_AIR_DRONE",
        E2RArchetype.URBAN_AIR_DRONE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round49ScoreWeightDraft(10, 10, 6, 12, 7, 0, 5),
        ("part135", "strategic_investment", "evtol_policy", "drone_theme"),
        ("type_certification", "production_certification", "commercial_operation", "customer_contract"),
        ("commercial_revenue", "unit_economics", "cash_runway_secure"),
        ("pre_revenue_valuation_crowded",),
        ("certification_delay", "cash_burn", "discounted_offering", "production_delay"),
        ("type_certification_flag", "commercial_revenue", "cash_runway_months", "dilution_risk_low"),
        ("certification", "cash_burn", "dilution", "pre_revenue", "discounted_offering"),
        "eVTOL/drone is RedTeam-first until certification, revenue, and cash runway are proven.",
    ),
    Round49ScoreTarget(
        "SPACE_SUPPLYCHAIN",
        E2RArchetype.SPACE_SUPPLYCHAIN,
        Round10ThemePosture.REDTEAM_FIRST,
        Round49ScoreWeightDraft(14, 13, 8, 12, 9, 0, 5),
        ("space_theme", "satellite_supply_contract", "launch_program"),
        ("actual_contract", "delivery_revenue", "backlog_visibility"),
        ("repeat_space_supply_revenue", "customer_contract_quality"),
        ("spacex_supplychain_theme_crowded",),
        ("no_actual_contract", "launch_delay", "capex_debt_stress"),
        ("actual_delivery_contract", "revenue_conversion", "backlog_visibility"),
        ("no_contract", "launch_delay", "capex_debt", "theme_only"),
        "Space supply-chain labels need actual contracts and delivery revenue.",
    ),
    Round49ScoreTarget(
        "SATELLITE_CONNECTIVITY_INFRA",
        E2RArchetype.SATELLITE_CONNECTIVITY_INFRA,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round49ScoreWeightDraft(18, 20, 10, 13, 11, 2, 5),
        ("airline_connectivity_contract", "secure_communications", "satellite_backlog"),
        ("connectivity_revenue_growth", "airline_contract_count", "ebitda_improvement", "backlog"),
        ("recurring_connectivity_revenue", "gross_backlog", "debt_capex_manageable"),
        ("connectivity_narrative_crowded",),
        ("launch_delay", "contract_cancellation", "capex_debt_stress", "competitor_constellation"),
        ("satellite_backlog", "connectivity_revenue_growth", "airline_contract_count", "capex_debt_ratio_ok"),
        ("capex_debt", "launch_delay", "competitor_constellation", "contract_cancellation"),
        "Satellite connectivity can be Green-eligible only with real backlog and recurring revenue.",
    ),
)


ROUND49_CASE_CANDIDATES: tuple[Round49CaseCandidate, ...] = (
    Round49CaseCandidate(
        "hyundai_hybrid_valueup_case",
        "AUTO_MOBILITY_COMPLETED_VEHICLE",
        "005380",
        "Hyundai Motor hybrid value-up",
        "KR",
        "success_candidate",
        date(2024, 8, 28),
        date(2024, 8, 28),
        None,
        None,
        None,
        ("hybrid_demand", "sales_target", "shareholder_return", "op_fcf_stability"),
        ("tariff", "peak_margin", "recall"),
        "auto_valueup_aligned_candidate",
        "needs_price_backfill",
        ("Reuters Hyundai 2030 sales, hybrid expansion, buyback, and dividend policy",),
        "Completed vehicle value-up needs hybrid/mix, FCF, and return execution.",
    ),
    Round49CaseCandidate(
        "toyota_hybrid_supply_bottleneck_case",
        "AUTO_MOBILITY_COMPLETED_VEHICLE",
        "7203.T",
        "Toyota hybrid demand bottleneck reference",
        "JP",
        "success_candidate",
        date(2025, 1, 3),
        date(2025, 3, 31),
        None,
        None,
        None,
        ("hybrid_demand", "supply_bottleneck", "parts_constraint", "sales_growth"),
        ("component_shortage", "cost_pressure"),
        "hybrid_structural_demand_reference",
        "needs_price_backfill",
        ("Reuters Toyota US sales and hybrid bottleneck coverage",),
        "Hybrid demand can support auto and component visibility, but Stage 3 still needs FCF and margin proof.",
    ),
    Round49CaseCandidate(
        "hyundai_mobis_lighting_restructuring_case",
        "AUTO_MOBILITY_COMPONENTS",
        "012330",
        "Hyundai Mobis lighting restructuring",
        "KR",
        "success_candidate",
        date(2026, 1, 27),
        date(2026, 1, 27),
        None,
        None,
        None,
        ("lighting_business", "portfolio_restructuring", "high_value_component", "customer_diversification"),
        ("customer_concentration", "quality_cost"),
        "auto_component_restructuring_candidate",
        "needs_price_backfill",
        ("Reuters OPmobility Hyundai Mobis lighting business talks",),
        "Auto components should be scored through mix, customer breadth, and margin, not vehicle volume alone.",
    ),
    Round49CaseCandidate(
        "korean_air_asiana_integration_case",
        "AIRLINE_TRAVEL_CYCLE",
        "003490",
        "Korean Air Asiana integration",
        "KR",
        "cyclical_success",
        date(2024, 12, 12),
        date(2025, 2, 7),
        None,
        date(2025, 2, 7),
        None,
        ("airline_merger", "integration_synergy", "record_revenue", "passenger_cargo_mix"),
        ("fuel", "fx", "integration_cost", "cargo_cycle"),
        "airline_integration_success_candidate_but_cycle_watch",
        "needs_price_backfill",
        ("Reuters Korean Air completes Asiana takeover", "Reuters Korean Air record annual revenue"),
        "Airline integration can be a strong Watch case, but fuel, FX, and integration cost keep Green restricted.",
    ),
    Round49CaseCandidate(
        "china_group_visa_tourism_case",
        "CASINO_DUTYFREE_TOURISM",
        "KR_TOURISM_POLICY",
        "Korea China group visa tourism policy basket",
        "KR",
        "event_premium",
        date(2025, 8, 6),
        None,
        None,
        date(2025, 8, 6),
        None,
        ("visa_policy", "china_group_tourism", "tourism_policy_event"),
        ("policy_event_only", "drop_amount_unverified", "duty_free_asp_weak"),
        "tourism_policy_event_aligned_stage1",
        "needs_price_backfill",
        ("Reuters Korea visa-free entry for Chinese tourist groups",),
        "Tourism policy can move prices immediately, but Stage 3 needs spend, drop amount, ASP, and OPM.",
    ),
    Round49CaseCandidate(
        "ses_airline_connectivity_case",
        "SATELLITE_CONNECTIVITY_INFRA",
        "SESG.PA",
        "SES airline connectivity backlog",
        "EU",
        "success_candidate",
        date(2026, 5, 12),
        date(2026, 5, 12),
        None,
        None,
        None,
        ("airline_connectivity_contract", "connectivity_revenue_growth", "satellite_backlog", "airline_contract_count"),
        ("capex_debt", "launch_delay", "competitor_constellation"),
        "satellite_connectivity_aligned_candidate",
        "needs_price_backfill",
        ("Reuters SES revenue jumps on airline connectivity contracts",),
        "Satellite connectivity differs from SpaceX theme when real airline contracts, backlog, and revenue exist.",
    ),
    Round49CaseCandidate(
        "lime_ipo_micromobility_case",
        "MOBILITY_RENTAL_MICROMOBILITY",
        "LIME_PRIVATE",
        "Lime micromobility IPO filing",
        "US",
        "success_candidate",
        date(2026, 5, 1),
        date(2026, 5, 1),
        None,
        date(2026, 5, 1),
        None,
        ("micromobility_revenue", "micromobility_fcf", "city_count", "utilization_rate"),
        ("debt_maturity", "seasonality", "regulation", "net_loss"),
        "micromobility_mixed_watch_candidate",
        "needs_price_backfill",
        ("MarketWatch Lime IPO filing and debt concerns",),
        "Micromobility can improve with FCF, but debt maturity and losses keep it Watch.",
    ),
    Round49CaseCandidate(
        "maersk_overcapacity_rate_collapse_case",
        "SHIPPING_FREIGHT_CYCLE",
        "MAERSK-B.CO",
        "Maersk overcapacity freight-rate collapse",
        "DK",
        "4c_thesis_break",
        date(2024, 3, 14),
        None,
        None,
        date(2025, 10, 3),
        date(2026, 2, 5),
        ("freight_rate_index", "container_rate", "red_sea_disruption_flag"),
        ("overcapacity", "freight_rate_collapse", "route_normalization", "earnings_collapse"),
        "shipping_cycle_hard_counterexample",
        "needs_price_backfill",
        ("Reuters Maersk unsustainable container rates", "Reuters Maersk 2026 earnings hit warning"),
        "Shipping freight spikes are cyclical unless contract rate and supply discipline persist.",
    ),
    Round49CaseCandidate(
        "hertz_ev_rental_failure_case",
        "RENTAL_USED_CAR_MOBILITY",
        "HTZ",
        "Hertz EV rental residual-value failure",
        "US",
        "4c_thesis_break",
        date(2024, 1, 11),
        None,
        None,
        None,
        date(2024, 1, 11),
        ("ev_fleet_ratio", "fleet_strategy"),
        ("repair_cost", "residual_value_drop", "fleet_writedown", "low_customer_demand"),
        "rental_ev_strategy_4c",
        "needs_price_backfill",
        ("Axios Hertz sells 20,000 EVs and records loss",),
        "Rental EV strategy needs residual value and repair cost validation, not EV label.",
    ),
    Round49CaseCandidate(
        "michelin_tire_demand_cut_case",
        "TIRE_AUTO_COMPONENT_SPREAD",
        "ML.PA",
        "Michelin tire demand outlook cut",
        "EU",
        "4c_thesis_break",
        date(2025, 10, 13),
        None,
        None,
        None,
        date(2025, 10, 13),
        ("tire_demand_recovery", "raw_material_spread"),
        ("north_america_demand_slowdown", "replacement_market_weakness", "tariff", "fx"),
        "tire_demand_slowdown_4c_watch",
        "needs_price_backfill",
        ("Reuters Michelin cuts annual outlook on North America tire demand",),
        "Tire margin visibility breaks when replacement demand and volume weaken.",
    ),
    Round49CaseCandidate(
        "joby_blade_acquisition_case",
        "URBAN_AIR_DRONE",
        "JOBY",
        "Joby Blade passenger business acquisition",
        "US",
        "success_candidate",
        date(2025, 8, 4),
        date(2025, 8, 4),
        None,
        date(2025, 8, 4),
        None,
        ("launch_infrastructure", "operating_experience", "customer_access"),
        ("pre_revenue", "cash_burn", "certification", "dilution"),
        "launch_infra_candidate_but_pre_revenue_watch",
        "needs_price_backfill",
        ("Reuters Joby to acquire Blade Air passenger business",),
        "Blade acquisition helps launch infrastructure, but eVTOL remains RedTeam-first before certification and revenue.",
    ),
    Round49CaseCandidate(
        "joby_discounted_offering_case",
        "URBAN_AIR_DRONE",
        "JOBY",
        "Joby discounted offering",
        "US",
        "4c_thesis_break",
        date(2025, 10, 8),
        None,
        None,
        None,
        date(2025, 10, 8),
        ("evtol_policy", "pre_revenue_valuation"),
        ("discounted_offering", "cash_burn", "dilution", "pre_revenue"),
        "evtOL_execution_candidate_but_dilution_4c_watch",
        "needs_price_backfill",
        ("Reuters Joby shares tumble after discounted offering",),
        "Discounted offering after a large run-up is a hard cash-runway and dilution warning.",
    ),
    Round49CaseCandidate(
        "archer_part135_no_type_cert_case",
        "URBAN_AIR_DRONE",
        "ACHR",
        "Archer Part 135 without type certification",
        "US",
        "event_premium",
        date(2024, 6, 5),
        None,
        None,
        date(2024, 6, 5),
        None,
        ("part135_flag", "evtol_policy"),
        ("type_certification_missing", "cash_runway", "production_certification_missing"),
        "part135_event_not_commercialization",
        "needs_price_backfill",
        ("Reuters Archer receives FAA nod to start commercial services",),
        "Part 135 is a milestone, not proof that the aircraft is certified or commercially scaled.",
    ),
)


ROUND49_PRICE_FIELDS: tuple[str, ...] = (
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
    "vehicle_sales_growth",
    "hybrid_sales_growth",
    "ev_sales_growth",
    "operating_margin",
    "fcf_margin",
    "buyback_amount",
    "dividend_policy_change",
    "tariff_event_flag",
    "recall_flag",
    "auto_parts_customer_concentration",
    "raw_material_cost_change",
    "quality_cost_flag",
    "passenger_revenue_growth",
    "cargo_revenue_growth",
    "load_factor",
    "jet_fuel_price",
    "fx_rate_exposure",
    "integration_cost",
    "synergy_amount",
    "tourist_arrivals",
    "china_tourist_arrivals",
    "casino_drop_amount",
    "duty_free_sales",
    "hotel_occupancy",
    "revpar",
    "average_spend_per_visitor",
    "freight_rate_index",
    "container_rate",
    "fleet_capacity_growth",
    "red_sea_disruption_flag",
    "overcapacity_flag",
    "ebitda_change",
    "rental_fleet_size",
    "used_car_residual_value",
    "repair_cost_per_vehicle",
    "ev_fleet_ratio",
    "utilization_rate",
    "micromobility_revenue",
    "micromobility_fcf",
    "debt_maturity_amount",
    "city_count",
    "seasonality_risk",
    "evt_burn_rate",
    "type_certification_flag",
    "part135_flag",
    "discounted_offering_flag",
    "cash_runway_months",
    "satellite_backlog",
    "connectivity_revenue_growth",
    "airline_contract_count",
    "capex_debt_ratio",
    "launch_delay_flag",
    "score_price_alignment",
    "price_validation_status",
)


def target_for(target_id: str) -> Round49ScoreTarget | None:
    for target in ROUND49_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round49_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND49_CASE_CANDIDATES:
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
                f"Round49 R9 case for {candidate.target_id}; "
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
                "demand_recovery_or_policy_headline_is_not_green_evidence_alone",
                "opm_fcf_unit_economics_required_for_green",
                "cycle_event_and_cash_burn_risks_can_block_green",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.7 if candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.3,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round49_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND49_SCORE_TARGETS:
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


def round49_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND49_CASE_CANDIDATES:
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


def round49_stage_date_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND49_SCORE_TARGETS:
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


def round49_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round49_backfill": "true"} for field in ROUND49_PRICE_FIELDS)


def round49_summary() -> dict[str, int | bool]:
    records = round49_case_records()
    return {
        "target_count": len(ROUND49_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch"),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND49_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND49_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND49_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round49_r9_reports(
    *,
    output_directory: str | Path = ROUND49_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND49_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND49_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round49_r9_mobility_transport_leisure_summary.md",
        "case_matrix": output / "round49_r9_case_matrix.csv",
        "stage_date_plan": output / "round49_r9_stage_date_plan.csv",
        "green_guardrails": output / "round49_r9_green_guardrails.md",
        "cycle_event_caps": output / "round49_r9_cycle_event_caps.md",
        "price_validation_plan": output / "round49_r9_price_validation_plan.md",
        "price_fields": output / "round49_r9_price_fields.csv",
    }
    _write_case_jsonl(round49_case_records(), cases)
    _write_rows(round49_score_profile_rows(), score_profiles)
    _write_rows(round49_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round49_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round49_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round49_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round49_green_guardrail_markdown(), encoding="utf-8")
    paths["cycle_event_caps"].write_text(render_round49_cycle_event_cap_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round49_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round49_summary_markdown() -> str:
    summary = round49_summary()
    lines = [
        "# Round-49 R9 Mobility / Transport / Leisure Summary",
        "",
        f"- source_round: `{ROUND49_SOURCE_ROUND_PATH}`",
        "- large_sector: `MOBILITY_TRANSPORT_LEISURE`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- cyclical_success_count: {summary['cyclical_success_count']}",
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
        "- R9 is not a demand-recovery round; it is an OPM, FCF, unit-economics, and cycle-risk round.",
        "- Example: Hyundai Motor can be Green-eligible only when hybrid mix, FCF, and shareholder return are durable.",
        "- Example: China tourism visa news is Stage 1 until actual spend, drop amount, ASP, and OPM are visible.",
        "- Example: Maersk and Hertz show that freight spikes or EV fleet narratives can become 4C when cycle or unit economics break.",
    ]
    return "\n".join(lines) + "\n"


def render_round49_green_guardrail_markdown() -> str:
    lines = [
        "# Round-49 R9 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND49_SCORE_TARGETS:
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
            "- Do not apply these R9 v1.0 weights to production scoring yet.",
            "- Do not treat demand recovery, tourist arrivals, freight spikes, EV fleet expansion, Part 135, SpaceX theme, or policy headlines as Green evidence by itself.",
            "- Do not invent OPM, FCF, unit economics, tourist spend, freight rates, fuel/FX exposure, residual value, certification, backlog, or price-path fields.",
            "- Do not lower Stage 3-Green for mobility recall. Green requires source-backed OPM/FCF, unit economics, valuation room, and low cycle or cash-burn risk.",
            "- Treat overcapacity, fuel/FX shock, EV residual-value failure, discounted offering, certification delay, and policy-event-only rallies as RedTeam evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round49_cycle_event_cap_markdown() -> str:
    lines = [
        "# Round-49 R9 Cycle / Event Caps",
        "",
        "- `SHIPPING_FREIGHT_CYCLE`: freight-rate spikes are cyclical unless contract rates and fleet supply discipline persist.",
        "- `AIRLINE_TRAVEL_CYCLE`: passenger recovery needs yield, load factor, fuel/FX, and integration-cost proof.",
        "- `CASINO_DUTYFREE_TOURISM`: visa policy is Stage 1 until actual spend, drop amount, ASP, and OPM appear.",
        "- `RENTAL_USED_CAR_MOBILITY`: EV fleet plans need residual value, repair cost, utilization, and FCF.",
        "- `URBAN_AIR_DRONE`: Part 135 or partnerships are not enough without type certification, commercial revenue, cash runway, and low dilution risk.",
        "- `SPACE_SUPPLYCHAIN`: SpaceX or space-theme labels need actual contracts and delivery revenue.",
        "",
        "Simple example: a casino stock can jump on visa-free tourism news, but if `casino_drop_amount` and `duty_free_sales` are still missing, the case stays Stage 1/Watch rather than Stage 3-Green.",
    ]
    return "\n".join(lines) + "\n"


def render_round49_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-49 R9 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Calculate peak price, drawdown after peak, and below-stage3 flag.",
        "6. Compare price paths with OPM, FCF, buyback/dividend, fuel/FX, tourist spend, freight rates, residual value, certification, backlog, capex/debt, and cash burn.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | stage candidate | check |",
        "| --- | --- | --- |",
    ]
    priority = {
        "hyundai_hybrid_valueup_case",
        "maersk_overcapacity_rate_collapse_case",
        "hertz_ev_rental_failure_case",
        "joby_discounted_offering_case",
        "ses_airline_connectivity_case",
    }
    for row in round49_case_candidate_rows():
        if row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or row["case_id"] in priority:
            stage_date = row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or "needs_source_date"
            lines.append(f"| `{row['case_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `aligned`: mix, FCF, capital return, backlog, or recurring revenue moves with price rerating.",
            "- `cyclical_success`: airline, shipping, tire, or travel cycle improves but does not prove structural Green.",
            "- `policy_event_premium`: visa, tourism, merger, or policy headline moves price before operating evidence.",
            "- `unit_economics_failure`: fleet, rental, micromobility, or eVTOL revenue grows while residual value, debt, repair cost, or cash burn breaks.",
            "- `thesis_break`: freight collapse, EV rental write-down, certification delay, discounted offering, fuel/FX shock, or major recall damages the thesis.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round49CaseCandidate) -> str:
    if "aligned" in candidate.alignment_hint and candidate.case_type in {"structural_success", "success_candidate"}:
        return "aligned"
    if candidate.case_type in {"cyclical_success", "event_premium", "4b_watch"}:
        return "price_moved_without_evidence"
    if candidate.case_type in {"failed_rerating", "4c_thesis_break"}:
        return "false_positive_score"
    return "unknown"


def _rerating_result(candidate: Round49CaseCandidate) -> str:
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
    "ROUND49_CASE_CANDIDATES",
    "ROUND49_DEFAULT_CASES_PATH",
    "ROUND49_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND49_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND49_PRICE_FIELDS",
    "ROUND49_SCORE_TARGETS",
    "ROUND49_SOURCE_ROUND_PATH",
    "Round49CaseCandidate",
    "Round49ScoreTarget",
    "Round49ScoreWeightDraft",
    "render_round49_cycle_event_cap_markdown",
    "render_round49_green_guardrail_markdown",
    "render_round49_price_validation_plan_markdown",
    "render_round49_summary_markdown",
    "round49_case_candidate_rows",
    "round49_case_records",
    "round49_price_field_rows",
    "round49_score_profile_rows",
    "round49_stage_date_rows",
    "round49_summary",
    "target_for",
    "write_round49_r9_reports",
]
