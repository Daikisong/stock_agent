"""Round-67 R1 Loop-3 industrial orders and infrastructure pack.

Round 67 returns to R1 after the R13 Loop-2 RedTeam pass. It narrows the
industrial/order/infrastructure sector around contract quality, margin
conversion, EPS/FCF revision, project-delay risk, capital-allocation shock,
and price-path validation.

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


ROUND67_SOURCE_ROUND_PATH = "docs/round/round_67.md"
ROUND67_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round67_r1_loop3_industrial_infra"
ROUND67_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop3_round67.jsonl"
ROUND67_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round67_r1_loop3_v3.csv"


@dataclass(frozen=True)
class Round67ScoreWeightDraft:
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
class Round67ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round67ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop3_penalty_axes: tuple[str, ...]
    normalization_point: str
    hard_gate: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.INDUSTRIAL_ORDERS_INFRA

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round67CaseCandidate:
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


ROUND67_SCORE_TARGETS: tuple[Round67ScoreTarget, ...] = (
    Round67ScoreTarget(
        "GRID_TRANSFORMER_SHORTAGE",
        E2RArchetype.GRID_TRANSFORMER_SHORTAGE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round67ScoreWeightDraft(24, 25, 24, 12, 12, 1, 5),
        ("data_center_power_demand", "ev_grid_demand", "grid_modernization", "lead_time_extended", "transformer_price_increase"),
        ("supply_contract", "contract_value_to_sales", "delivery_schedule", "backlog_growth", "op_eps_revision"),
        ("fy1_fy2_fy3_revision", "long_lead_time", "price_increase", "margin_improvement", "old_industrial_frame_rerating"),
        ("sector_wide_ai_grid_consensus", "valuation_band_expansion", "capacity_addition_news", "new_order_growth_slowdown"),
        ("data_center_project_delay", "capa_normalization", "low_margin_contract", "margin_miss"),
        ("contract_value", "contract_duration", "delivery_schedule", "backlog_growth", "margin_improvement", "op_eps_revision"),
        ("capa_normalization", "data_center_project_delay", "low_margin_contract", "raw_material_tariff_cost"),
        ("capa_normalization", "data_center_delay", "low_margin_long_term_contract", "project_delay"),
        "Loop 3 strengthens transformer shortage, but Green still requires contract amount, duration, delivery, margin, and EPS conversion.",
    ),
    Round67ScoreTarget(
        "AI_DATA_CENTER_POWER_EQUIPMENT",
        E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round67ScoreWeightDraft(22, 23, 19, 13, 12, 0, 5),
        ("ups_pdu_switchgear_keyword", "modular_power", "electrification_equipment", "hyperscaler_power_demand"),
        ("data_center_orders", "bookings_growth", "backlog_growth", "revenue_guidance_up"),
        ("orders_to_revenue_conversion", "op_margin_improvement", "fcf_conversion", "valuation_frame_change"),
        ("data_center_power_consensus_crowded", "ytd_return_extreme", "valuation_crowding"),
        ("project_delay", "bookings_slowdown", "data_center_capex_delay", "low_margin_project"),
        ("orders", "backlog", "revenue_guidance", "op_eps_revision", "margin_visible"),
        ("project_delay", "valuation_crowding", "orders_slowdown", "wind_or_mix_risk"),
        ("project_delay", "valuation_crowding", "orders_slowdown"),
        "GE Vernova-style orders/backlog can support Stage 2/3, but rapid rerating creates 4B-watch.",
    ),
    Round67ScoreTarget(
        "CONTRACT_BACKLOG_INDUSTRIAL",
        E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round67ScoreWeightDraft(20, 24, 18, 13, 12, 1, 5),
        ("supply_contract_news", "trading_value_breakout", "backlog_keyword"),
        ("contract_amount_to_sales", "contract_duration", "counterparty", "delivery_schedule", "op_eps_revision"),
        ("multi_year_backlog", "margin_visible", "capacity_constraint", "fy1_fy2_revision"),
        ("crowded_order_story", "target_price_cluster", "new_order_growth_slowdown"),
        ("contract_cancelled", "delivery_delay", "margin_miss", "customer_credit_issue"),
        ("contract_value", "contract_duration", "counterparty", "delivery_schedule", "margin_visible", "op_eps_revision"),
        ("contract_quality_unclear", "delivery_delay", "margin_uncertainty", "mou_or_loi_only"),
        ("contract_quality_unclear", "delivery_delay", "margin_uncertainty"),
        "Generic order/backlog names need contract quality and margin/EPS conversion, not just order size.",
    ),
    Round67ScoreTarget(
        "DEFENSE_GOVERNMENT_BACKLOG",
        E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round67ScoreWeightDraft(21, 24, 17, 14, 14, 3, 5),
        ("nato_rearmament", "defense_export_news", "government_customer"),
        ("official_contract", "contract_value", "multi_year_delivery", "order_backlog_growth", "op_eps_revision"),
        ("government_backlog_to_sales", "delivery_visibility", "opm_improvement", "export_mix_growth"),
        ("defense_rerating_crowded", "target_price_cluster", "local_production_capex_ignored"),
        ("delivery_delay", "cost_overrun", "export_permit_issue", "dilution_shock", "contract_cancelled"),
        ("government_customer", "multi_year_contract", "delivery_schedule", "backlog_growth", "opm_improvement"),
        ("delivery_delay", "cost_overrun", "export_license_risk", "dilution", "local_production_capex"),
        ("capital_allocation_shock", "dilution", "delivery_delay", "export_permit_issue"),
        "Defense remains Green-capable, but delivery schedule, margin, and dilution/CAPEX overlay are mandatory.",
    ),
    Round67ScoreTarget(
        "DEFENSE_TECH_AUTONOMOUS_SYSTEMS",
        E2RArchetype.DEFENSE_TECH_AUTONOMOUS_SYSTEMS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round67ScoreWeightDraft(19, 21, 15, 15, 13, 2, 5),
        ("autonomous_weapon_keyword", "loitering_munition", "prototype_program"),
        ("framework_agreement", "evaluation_schedule", "procurement_quantity_hint"),
        ("program_of_record", "mass_procurement", "production_capacity", "eps_conversion"),
        ("prototype_theme_crowded", "defense_ai_valuation_jump"),
        ("procurement_delay", "program_cancelled", "valuation_overheat", "export_control"),
        ("funded_procurement", "production_capacity", "customer_budget", "eps_conversion"),
        ("prototype_only", "procurement_delay", "valuation_overheat"),
        ("prototype", "production_delay", "valuation_overheat"),
        "Prototype and framework agreements stay Watch until funded procurement and production revenue appear.",
    ),
    Round67ScoreTarget(
        "DEFENSE_DRONE_COUNTER_UAS",
        E2RArchetype.DEFENSE_DRONE_COUNTER_UAS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round67ScoreWeightDraft(19, 21, 14, 14, 13, 3, 5),
        ("drone_or_counter_uas_keyword", "loitering_munition", "directed_energy_keyword"),
        ("military_order", "delivery_schedule", "production_capacity"),
        ("repeat_procurement", "export_customer", "margin_visible"),
        ("drone_theme_crowding", "mna_dilution"),
        ("export_control", "procurement_delay", "production_failure", "dilution"),
        ("actual_order", "delivery_schedule", "production_capacity", "repeat_procurement"),
        ("prototype_only", "export_control", "mna_dilution"),
        ("prototype", "export_control", "mna_dilution"),
        "Drone/counter-UAS stories need production capacity and repeat procurement.",
    ),
    Round67ScoreTarget(
        "DEFENSE_AI_SOFTWARE_INTELLIGENCE",
        E2RArchetype.DEFENSE_AI_SOFTWARE_INTELLIGENCE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round67ScoreWeightDraft(18, 20, 10, 15, 13, 0, 5),
        ("military_ai_software", "command_control_software", "prototype_contract"),
        ("government_customer", "deployment_schedule", "paid_pilot"),
        ("program_of_record", "recurring_license", "gross_margin_visible"),
        ("defense_ai_software_crowded", "multiple_expansion_without_arr"),
        ("prototype_not_renewed", "budget_cycle_cut", "political_ethics_risk"),
        ("government_customer", "deployment_schedule", "recurring_license", "gross_margin_visible"),
        ("prototype_stage", "budget_cycle", "recurring_sw_revenue_absent"),
        ("prototype", "no_repeat_software_revenue", "budget_cycle"),
        "Defense AI software stays Watch until repeat software economics are visible.",
    ),
    Round67ScoreTarget(
        "SHIPBUILDING_OFFSHORE_BACKLOG",
        E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round67ScoreWeightDraft(21, 22, 18, 13, 13, 1, 5),
        ("newbuilding_price_up", "ship_order_recovery", "lng_or_offshore_order", "ship_engine_or_fitting_valve"),
        ("large_order", "low_margin_backlog_rolloff", "high_margin_delivery_start", "op_eps_revision"),
        ("backlog_quality_improves", "fy2_fy3_margin_recognition", "cost_pressure_controlled"),
        ("shipbuilder_group_rally", "newbuilding_price_narrative_crowded", "mro_option_crowded"),
        ("steel_plate_cost_spike", "labor_cost_spike", "order_slowdown", "contract_cancelled", "delivery_delay"),
        ("newbuilding_price_up", "low_margin_backlog_rolloff", "high_margin_delivery_start", "op_eps_revision"),
        ("low_margin_backlog", "steel_plate_cost", "labor_cost", "delivery_delay"),
        ("low_margin_backlog", "steel_plate_cost", "labor_cost", "delivery_delay"),
        "Shipbuilding needs order quality, newbuilding prices, margin recognition, and cost controls.",
    ),
    Round67ScoreTarget(
        "SHIPBUILDING_NAVAL_MRO",
        E2RArchetype.SHIPBUILDING_NAVAL_MRO,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round67ScoreWeightDraft(17, 17, 11, 13, 10, 1, 5),
        ("naval_mro_keyword", "msra", "us_shipyard_acquisition", "us_navy_repair_contract"),
        ("actual_mro_contract", "work_period", "revenue_recognition"),
        ("repeat_high_margin_mro", "newbuild_or_naval_order", "margin_visible"),
        ("naval_mro_option_crowded", "mro_story_priced_as_newbuild"),
        ("low_margin_mro", "newbuild_license_uncertain", "us_legal_restriction", "shipyard_modernization_capex"),
        ("repeat_mro", "margin_visible", "newbuild_order_or_license", "revenue_conversion"),
        ("low_margin_mro", "legal_restriction", "license_uncertain", "capex_burden"),
        ("mro_option_only", "low_margin_mro", "legal_restriction"),
        "MRO is Stage 2 reference; Stage 3 needs repeat high-margin MRO or newbuild conversion.",
    ),
    Round67ScoreTarget(
        "RAIL_INFRASTRUCTURE",
        E2RArchetype.RAIL_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round67ScoreWeightDraft(20, 22, 12, 14, 11, 1, 5),
        ("rail_order_news", "foreign_rail_investment", "urban_or_high_speed_rail_policy"),
        ("official_contract", "contract_amount_to_sales", "delivery_schedule"),
        ("delivery_visibility", "margin_visible", "op_eps_revision", "financing_risk_low"),
        ("rail_order_expectation_fully_priced",),
        ("project_delay", "financing_failure", "margin_miss", "warranty_cost", "fx_cost"),
        ("official_contract", "contract_amount_to_sales", "delivery_schedule", "margin_visible", "financing_secured"),
        ("project_delay", "margin_uncertainty", "financing", "warranty_cost"),
        ("project_delay", "financing", "warranty_cost", "margin_uncertainty"),
        "Rail contracts can reach Stage 2, but Green needs margin, delivery, warranty, and financing evidence.",
    ),
    Round67ScoreTarget(
        "NUCLEAR_EXISTING_PPA",
        E2RArchetype.NUCLEAR_EXISTING_PPA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round67ScoreWeightDraft(18, 22, 12, 14, 12, 2, 5),
        ("big_tech_clean_power_demand", "existing_nuclear_ppa", "plant_relicense_support"),
        ("signed_ppa", "contract_duration_years", "plant_capacity_mw", "relicensing_support"),
        ("long_term_fcf_visibility", "ppa_economics_visible", "valuation_frame_change"),
        ("nuclear_ppa_theme_crowded", "related_stock_theme_spillover"),
        ("relicense_failure", "plant_outage", "policy_change", "ppa_economics_break"),
        ("signed_ppa", "duration", "plant_capacity", "fcf_visibility"),
        ("relicense_risk", "plant_specific_risk", "ppa_economics_unverified"),
        ("relicense", "plant_outage", "ppa_economics"),
        "Existing nuclear PPA is stronger than SMR policy because it has clearer cashflow visibility.",
    ),
    Round67ScoreTarget(
        "NUCLEAR_SMR_GRID_POLICY",
        E2RArchetype.NUCLEAR_SMR_GRID_POLICY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round67ScoreWeightDraft(14, 13, 10, 13, 8, 1, 5),
        ("smr_policy", "ai_power_demand", "nuclear_equipment_theme"),
        ("ppa", "customer_subscription", "cost_confirmed", "permit", "financing"),
        ("actual_construction", "supplier_revenue_visibility", "cost_and_customer_risk_resolved"),
        ("smr_theme_crowded", "nuclear_policy_premium"),
        ("cost_overrun", "customer_subscription_failure", "financing_failure", "project_cancelled", "permit_delay"),
        ("ppa", "customer_subscription", "cost_confirmed", "permit", "financing", "revenue_visibility"),
        ("cost_overrun", "customer_subscription_failure", "financing_failure", "policy_headline_only"),
        ("cost_overrun", "customer_subscription_failure", "financing_failure", "project_cancelled"),
        "SMR policy is Watch/Red until PPA, customer, cost, permit, financing, and revenue visibility are confirmed.",
    ),
    Round67ScoreTarget(
        "GEOPOLITICAL_RECONSTRUCTION",
        E2RArchetype.GEOPOLITICAL_RECONSTRUCTION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round67ScoreWeightDraft(10, 8, 8, 10, 7, 0, 4),
        ("ukraine_reconstruction", "neom_city_theme", "overseas_infra_policy", "mou_or_bid_news"),
        ("binding_contract", "revenue_schedule", "financing_visible", "construction_started"),
        ("actual_delivery_and_margin", "eps_conversion", "cash_collection"),
        ("policy_event_crowded", "event_premium_fades"),
        ("no_contract", "project_delay", "financing_failure", "policy_reversal"),
        ("binding_contract", "revenue_schedule", "financing_visible", "margin_visible"),
        ("actual_contract_missing", "policy_event_only", "mou_only", "budget_missing"),
        ("policy_to_contract_failed", "financing_failure", "mou_only"),
        "Reconstruction and Neom-style themes remain Event/Watch before binding contracts and revenue schedules.",
    ),
    Round67ScoreTarget(
        "SMART_FACTORY_AUTOMATION",
        E2RArchetype.SMART_FACTORY_AUTOMATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round67ScoreWeightDraft(18, 16, 8, 12, 10, 0, 5),
        ("smart_factory_keyword", "automation_order", "factory_ai_keyword"),
        ("actual_order", "installed_base", "recurring_maintenance_or_software"),
        ("revenue_conversion", "opm_improvement", "customer_diversification"),
        ("automation_theme_crowded",),
        ("mou_or_poc_only", "customer_capex_delay", "no_revenue_conversion"),
        ("actual_order", "installed_base", "recurring_revenue", "opm_improvement"),
        ("mou_only", "poc_only", "revenue_conversion_failure"),
        ("mou_only", "poc_only", "customer_capex_delay"),
        "Smart factory stories need order-to-revenue conversion; PoC and MOU stay Watch.",
    ),
    Round67ScoreTarget(
        "PROJECT_DELAY_CAPEX_OVERLAY",
        E2RArchetype.PROJECT_DELAY_CAPEX_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round67ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("data_center_local_opposition", "water_permitting_delay", "grid_interconnection_delay", "rail_or_nuclear_delay"),
        ("project_delay_confirmed", "permit_delay", "community_opposition", "power_price_backlash"),
        ("not_applicable_until_project_schedule_restored",),
        ("delay_ignored_by_order_story",),
        ("project_cancelled_or_delayed", "financing_failure", "order_slowdown"),
        (),
        ("local_opposition", "water_permitting_delay", "grid_interconnection_delay", "project_cancellation"),
        ("project_delay", "permitting_delay", "capex_burden"),
        "Hard/soft RedTeam overlay for data-center, rail, nuclear, and infrastructure project execution delays.",
        hard_gate=True,
    ),
    Round67ScoreTarget(
        "CAPITAL_ALLOCATION_DILUTION_OVERLAY",
        E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round67ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("share_issuance_plan", "large_capex", "overseas_factory_capex", "mna_funding"),
        ("dilution", "use_of_proceeds_unclear", "regulator_revision_request", "shareholder_value_shock"),
        ("not_applicable_until_funding_quality_restored",),
        ("dilution_ignored_by_backlog_story",),
        ("large_equity_issuance", "dilution", "fcf_burden", "regulator_revision_request"),
        (),
        ("large_equity_issuance", "dilution", "use_of_proceeds_unclear", "capex_burden"),
        ("capital_allocation_shock", "dilution", "capex_burden"),
        "Capital allocation overlay for order/backlog companies whose expansion funding damages the price path.",
        hard_gate=True,
    ),
)


ROUND67_CASE_CANDIDATES: tuple[Round67CaseCandidate, ...] = (
    Round67CaseCandidate(
        "us_transformer_shortage_import_slots_case",
        "GRID_TRANSFORMER_SHORTAGE",
        "POWER_TRANSFORMER_IMPORT",
        "US transformer shortage import/factory-slot reference",
        "GLOBAL",
        "success_candidate",
        date(2026, 5, 11),
        date(2026, 5, 11),
        None,
        None,
        None,
        ("gsu_transformer_demand_274pct", "substation_transformer_demand_116pct", "lead_time_four_years", "price_up_80pct", "factory_slot_prebuy", "korea_turkey_imports"),
        ("capa_normalization", "data_center_project_delay", "raw_material_tariff_cost", "low_margin_contract"),
        "grid_bottleneck_structural_reference",
        "needs_price_backfill",
        ("round_67.md Reuters US transformer shortage",),
        "Transformer shortage is strong structural reference, but company-specific contracts, margin, and price path still need backfill.",
        (E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,),
    ),
    Round67CaseCandidate(
        "ge_vernova_data_center_orders_case",
        "AI_DATA_CENTER_POWER_EQUIPMENT",
        "GEV",
        "GE Vernova data-center power orders",
        "US",
        "4b_watch",
        date(2026, 4, 22),
        date(2026, 4, 22),
        None,
        date(2026, 4, 22),
        None,
        ("orders_up_71pct", "orders_18_3b_usd", "backlog_163b_usd", "data_center_orders_2_4b_usd", "revenue_guidance_up", "event_day_price_up_15pct"),
        ("ytd_return_70pct", "valuation_crowding", "project_delay", "wind_mix_risk"),
        "data_center_power_equipment_aligned_plus_4b_watch",
        "needs_price_backfill",
        ("round_67.md WSJ GE Vernova orders/backlog",),
        "Orders, backlog, guidance, and price reaction align, but rapid YTD rerating requires 4B-watch.",
        (E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE, E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH),
    ),
    Round67CaseCandidate(
        "data_center_local_opposition_grid_case",
        "PROJECT_DELAY_CAPEX_OVERLAY",
        "DATA_CENTER_DELAY",
        "AI data-center local opposition / grid delay reference",
        "GLOBAL",
        "4c_thesis_break",
        date(2026, 5, 13),
        None,
        None,
        None,
        date(2026, 5, 13),
        ("ai_data_center_demand", "local_opposition", "water_usage", "grid_power_demand"),
        ("local_opposition", "water_permitting_delay", "grid_interconnection_delay", "power_price_backlash", "project_cancellation"),
        "data_center_project_delay_soft_4c_overlay",
        "needs_price_backfill",
        ("round_67.md The Verge AI data-center opposition", "round_67.md Guardian Utah data-center backlash"),
        "Power-equipment demand can be structural, but data-center permitting and local opposition can break new-order visibility.",
        (E2RArchetype.GRID_TRANSFORMER_SHORTAGE, E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT),
    ),
    Round67CaseCandidate(
        "hanwha_aerospace_romania_k9_case",
        "DEFENSE_GOVERNMENT_BACKLOG",
        "012450",
        "한화에어로스페이스 루마니아 K9 계약",
        "KR",
        "structural_success",
        None,
        date(2024, 7, 9),
        None,
        None,
        None,
        ("romania_k9_contract", "k10_ammunition_vehicle", "contract_1bn_usd", "delivery_to_2029", "backlog_growth", "event_day_record_high"),
        ("delivery_delay", "cost_overrun", "export_license_risk", "dilution"),
        "defense_backlog_aligned_candidate",
        "needs_price_backfill",
        ("round_67.md Reuters Romania K9 contract",),
        "Government customer, contract size, delivery term, and backlog growth make this a defense backlog reference case.",
        (E2RArchetype.STRUCTURAL_SUCCESS_ALIGNED,),
    ),
    Round67CaseCandidate(
        "hanwha_aerospace_europe_sales_visibility_case",
        "DEFENSE_GOVERNMENT_BACKLOG",
        "012450",
        "한화에어로스페이스 유럽 지상무기 매출 visibility",
        "KR",
        "success_candidate",
        None,
        date(2024, 10, 7),
        None,
        None,
        None,
        ("europe_land_arms_sales_double_by_2027", "poland_contracts", "romania_contract", "local_production_preference", "land_arms_backlog_10x"),
        ("local_factory_capex", "delivery_delay", "political_risk", "dilution"),
        "multi_year_defense_visibility_candidate",
        "needs_price_backfill",
        ("round_67.md Reuters Hanwha Europe land arms sales",),
        "Regional platform demand is stronger than a one-off order, but CAPEX/dilution and delivery risk remain guardrails.",
        (E2RArchetype.STRUCTURAL_SUCCESS_ALIGNED,),
    ),
    Round67CaseCandidate(
        "hanwha_aerospace_dilution_case",
        "CAPITAL_ALLOCATION_DILUTION_OVERLAY",
        "012450",
        "한화에어로스페이스 대규모 자본조달 리스크",
        "KR",
        "failed_rerating",
        date(2025, 3, 27),
        date(2025, 3, 27),
        None,
        date(2025, 3, 27),
        None,
        ("share_issuance_plan", "overseas_expansion_capex", "capital_raise_3_6t_krw"),
        ("large_equity_issuance", "dilution", "use_of_proceeds_unclear", "regulator_revision_request", "event_day_price_down_13pct"),
        "capital_allocation_shock",
        "needs_price_backfill",
        ("round_67.md Reuters Hanwha Aerospace share issuance revision",),
        "Good defense backlog can be damaged by dilution and unclear overseas CAPEX funding.",
        (E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, E2RArchetype.LEVERAGE_FCF_BREAKDOWN),
    ),
    Round67CaseCandidate(
        "korean_shipbuilder_contract_rally_case",
        "SHIPBUILDING_OFFSHORE_BACKLOG",
        "KR_SHIPBUILDERS",
        "한국 조선주 수주·선가 랠리",
        "KR",
        "cyclical_success",
        None,
        None,
        None,
        None,
        None,
        ("contract_wins", "newbuilding_price_index_up", "korea_order_share_recovery", "shipbuilder_group_price_reaction"),
        ("low_margin_backlog", "steel_plate_cost", "labor_cost", "delivery_delay", "order_slowdown"),
        "shipbuilding_price_aligned_candidate_needs_margin_backfill",
        "needs_source_date_backfill",
        ("round_67.md WSJ Korean shipbuilder contract rally",),
        "Shipbuilding price reaction is useful, but Green requires backlog quality, low-margin rolloff, and delivery margin evidence.",
        (E2RArchetype.CYCLICAL_SUCCESS,),
    ),
    Round67CaseCandidate(
        "hanwha_ocean_us_navy_mro_case",
        "SHIPBUILDING_NAVAL_MRO",
        "042660",
        "한화오션 미 해군 MRO 옵션",
        "KR",
        "success_candidate",
        date(2025, 5, 5),
        date(2025, 5, 5),
        None,
        None,
        None,
        ("philadelphia_shipyard_acquisition", "us_navy_mro_contracts", "overseas_naval_sales_target_4t_krw", "mro_reference"),
        ("low_margin_mro", "newbuild_license_uncertain", "us_legal_restriction", "shipyard_modernization_capex"),
        "naval_mro_option_candidate_low_margin_watch",
        "needs_price_backfill",
        ("round_67.md Reuters Hanwha Ocean US Navy MRO",),
        "MRO contracts are useful Stage 2 references, but not high-margin newbuild backlog until repeat economics are shown.",
        (E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG,),
    ),
    Round67CaseCandidate(
        "hyundai_rotem_morocco_rail_case",
        "RAIL_INFRASTRUCTURE",
        "064350",
        "현대로템 모로코 철도 수주",
        "KR",
        "success_candidate",
        None,
        date(2025, 2, 26),
        None,
        None,
        None,
        ("morocco_oncf_contract", "rail_contract_2_2t_krw", "largest_rail_order", "double_deck_train_order"),
        ("margin_uncertainty", "delivery_schedule_needed", "warranty_cost", "financing_risk", "fx_cost"),
        "rail_infrastructure_stage2_candidate",
        "needs_price_backfill",
        ("round_67.md Reuters Hyundai Rotem Morocco rail order",),
        "A large signed rail order is Stage-2 style evidence; Green needs margin, delivery, financing, and OP/EPS evidence.",
        (E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,),
    ),
    Round67CaseCandidate(
        "meta_constellation_existing_nuclear_ppa_case",
        "NUCLEAR_EXISTING_PPA",
        "CEG",
        "Meta-Constellation existing nuclear PPA",
        "US",
        "success_candidate",
        None,
        date(2025, 6, 3),
        None,
        None,
        None,
        ("twenty_year_nuclear_ppa", "clinton_plant_1121mw", "ai_data_center_power_demand", "relicensing_support"),
        ("ppa_price_unverified", "plant_specific_risk", "korea_equipment_mapping_needed"),
        "existing_nuclear_ppa_aligned_reference",
        "needs_price_backfill",
        ("round_67.md Reuters Meta Constellation nuclear PPA",),
        "Existing nuclear PPA has stronger cashflow visibility than SMR policy, but Korean equipment mapping needs direct contracts.",
        (E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT,),
    ),
    Round67CaseCandidate(
        "nuscale_uamps_smrcancel_case",
        "NUCLEAR_SMR_GRID_POLICY",
        "SMR",
        "NuScale UAMPS CFPP cancellation",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2023, 11, 1),
        ("smr_project", "customer_subscription_attempt", "policy_theme"),
        ("cost_overrun", "customer_subscription_failure", "financing_failure", "project_cancelled"),
        "smr_cost_overrun_hard_4c",
        "needs_price_backfill",
        ("round_67.md NuScale UAMPS CFPP cancellation",),
        "SMR policy is not existing nuclear PPA; cost, customer, financing, and cancellation risk can be hard 4C.",
        (E2RArchetype.THESIS_BREAK_4C,),
    ),
    Round67CaseCandidate(
        "ukraine_reconstruction_policy_case",
        "GEOPOLITICAL_RECONSTRUCTION",
        "UKRAINE_REBUILD",
        "Ukraine reconstruction policy reference",
        "GLOBAL",
        "event_premium",
        None,
        None,
        None,
        None,
        None,
        ("reconstruction_policy", "mou_or_bid_news", "infrastructure_theme"),
        ("actual_contract_missing", "financing_unsecured", "budget_missing", "revenue_recognition_absent"),
        "policy_to_contract_failed_before_binding_contract",
        "needs_price_backfill",
        ("round_67.md reconstruction policy rule",),
        "Reconstruction themes stay Event/Watch until binding contract, financing, construction, and revenue evidence appear.",
        (E2RArchetype.EVENT_PREMIUM,),
    ),
    Round67CaseCandidate(
        "neom_city_policy_case",
        "GEOPOLITICAL_RECONSTRUCTION",
        "NEOM_POLICY",
        "Neom city policy/infrastructure reference",
        "GLOBAL",
        "event_premium",
        None,
        None,
        None,
        None,
        None,
        ("neom_city_theme", "overseas_infra_policy", "mou_or_bid_news"),
        ("actual_contract_missing", "financing_unsecured", "contractor_unclear", "revenue_recognition_absent"),
        "policy_infra_event_premium",
        "needs_price_backfill",
        ("round_67.md Neom policy/infrastructure rule",),
        "Neom-style policy infrastructure is not Green without contract, financing, construction start, and revenue recognition.",
        (E2RArchetype.EVENT_PREMIUM,),
    ),
)


ROUND67_PRICE_FIELDS: tuple[str, ...] = (
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
    "contract_value_to_sales",
    "contract_duration_months",
    "contract_start_date",
    "contract_end_date",
    "counterparty",
    "delivery_schedule",
    "backlog_growth",
    "backlog_to_revenue",
    "new_order_growth",
    "book_to_bill",
    "gross_margin_change",
    "op_margin_change",
    "eps_revision_1q",
    "eps_revision_1y",
    "op_revision_1q",
    "op_revision_1y",
    "fcf_margin_change",
    "transformer_type",
    "transformer_lead_time_months",
    "transformer_price_change",
    "factory_slot_prebuy_flag",
    "grid_modernization_flag",
    "data_center_customer_flag",
    "data_center_orders",
    "data_center_backlog",
    "data_center_power_equipment_revenue",
    "project_delay_flag",
    "local_opposition_flag",
    "water_permitting_delay_flag",
    "grid_interconnection_delay_flag",
    "defense_customer_country",
    "government_customer_flag",
    "local_production_flag",
    "export_license_risk_flag",
    "delivery_batch_count",
    "defense_backlog",
    "capex_amount",
    "dilution_flag",
    "share_issuance_amount",
    "use_of_proceeds_clarity",
    "regulator_revision_request_flag",
    "ship_newbuilding_price_index",
    "low_margin_backlog_flag",
    "steel_plate_cost_change",
    "labor_cost_change",
    "naval_mro_contract_flag",
    "msra_flag",
    "naval_newbuild_license_flag",
    "mro_margin_signal",
    "rail_contract_value",
    "rail_delivery_schedule",
    "rail_warranty_risk",
    "rail_financing_secured_flag",
    "nuclear_ppa_flag",
    "ppa_duration_years",
    "plant_capacity_mw",
    "relicensing_support_flag",
    "smr_flag",
    "smr_cost_overrun_flag",
    "customer_subscription_flag",
    "project_cancelled_flag",
    "reconstruction_contract_flag",
    "financing_secured_flag",
    "budget_allocated_flag",
    "construction_started_flag",
    "revenue_recognized_flag",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def round67_target_for(target_id: str) -> Round67ScoreTarget | None:
    for target in ROUND67_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round67_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND67_CASE_CANDIDATES:
        target = round67_target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
        weights = target.score_weight.as_dict()
        stage4b_evidence = candidate.evidence_fields if candidate.case_type == "4b_watch" or candidate.stage4b_date else ()
        stage4c_evidence = candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" or candidate.stage4c_date or target.hard_gate else ()
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
                f"Round67 R1 Loop-3 case for {candidate.target_id}; "
                "contract-quality, project-delay, dilution, margin, and price-path evidence remain calibration-only."
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
            score_price_alignment=_round67_score_price_alignment(candidate),
            rerating_result=_round67_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint={
                "eps_fcf": _numeric_weight(weights["eps_fcf"]),
                "visibility": _numeric_weight(weights["structural_visibility"]),
                "bottleneck": _numeric_weight(weights["bottleneck_pricing"]),
                "mispricing": _numeric_weight(weights["market_mispricing"]),
                "valuation": _numeric_weight(weights["valuation"]),
                "capital_allocation": _numeric_weight(weights["capital_allocation"]),
            },
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_contract_quality_delivery_margin_eps_revision_fcf_for_green",
                "do_not_invent_contract_dates_prices_margins_or_counterparties",
                "project_delay_capital_allocation_shock_low_margin_mro_smr_false_green_are_loop3_penalties",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.75
                if candidate.stage1_date or candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date
                else 0.2,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round67_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND67_SCORE_TARGETS:
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
                "hard_gate": str(target.hard_gate).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round67_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND67_CASE_CANDIDATES:
        target = round67_target_for(candidate.target_id)
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


def round67_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "loop3_penalty_axes": "|".join(target.loop3_penalty_axes),
            "hard_gate": str(target.hard_gate).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND67_SCORE_TARGETS
    )


def round67_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round67_backfill": "true"} for field in ROUND67_PRICE_FIELDS)


def round67_summary() -> dict[str, int | bool]:
    records = round67_case_records()
    return {
        "target_count": len(ROUND67_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND67_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND67_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND67_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "hard_gate_target_count": sum(1 for target in ROUND67_SCORE_TARGETS if target.hard_gate),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round67_r1_loop3_reports(
    *,
    output_directory: str | Path = ROUND67_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND67_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND67_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round67_r1_loop3_industrial_infra_summary.md",
        "case_matrix": output / "round67_r1_loop3_case_matrix.csv",
        "stage_date_plan": output / "round67_r1_loop3_stage_date_plan.csv",
        "green_guardrails": output / "round67_r1_loop3_green_guardrails.md",
        "loop3_risk_overlays": output / "round67_r1_loop3_risk_overlays.md",
        "price_validation_plan": output / "round67_r1_loop3_price_validation_plan.md",
        "price_fields": output / "round67_r1_loop3_price_fields.csv",
    }
    _write_case_jsonl(round67_case_records(), cases)
    _write_rows(round67_score_profile_rows(), score_profiles)
    _write_rows(round67_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round67_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round67_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round67_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round67_green_guardrail_markdown(), encoding="utf-8")
    paths["loop3_risk_overlays"].write_text(render_round67_loop3_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round67_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round67_summary_markdown() -> str:
    summary = round67_summary()
    lines = [
        "# Round-67 R1 Loop-3 Industrial Orders / Infrastructure Summary",
        "",
        f"- source_round: `{ROUND67_SOURCE_ROUND_PATH}`",
        "- large_sector: `INDUSTRIAL_ORDERS_INFRA`",
        "- loop: `R1 Loop 3 / v3.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- cyclical_success_count: {summary['cyclical_success_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        f"- hard_gate_target_count: {summary['hard_gate_target_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R1 Loop 3 narrows order/backlog candidates after the R13 RedTeam pass.",
        "- Order size is not enough. Green needs contract amount, duration, counterparty, delivery schedule, margin, OP/EPS revision, FCF conversion, and price-path alignment.",
        "- Example: transformer shortage is strong, but low-margin long-term contracts or data-center project delay can still block Green.",
        "- Example: defense backlog can be strong, but share issuance and unclear overseas CAPEX are capital-allocation shocks.",
        "- Example: existing nuclear PPA and SMR policy are separated because cashflow visibility is different.",
    ]
    return "\n".join(lines) + "\n"


def render_round67_green_guardrail_markdown() -> str:
    lines = [
        "# Round-67 R1 Loop-3 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-3 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND67_SCORE_TARGETS:
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
            "- Do not apply R1 Loop-3 v3.0 weights to production scoring yet.",
            "- Do not lower Stage 3-Green thresholds because R1 is Green-capable.",
            "- Do not treat MOU, policy expectation, prototype, or project headline as Green evidence.",
            "- Do not invent contract values, contract dates, counterparties, delivery schedules, margins, or stage prices.",
            "- Treat project delay, capital-allocation shock, low-margin backlog, MRO option-only, and SMR policy false Green as strong penalties.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round67_loop3_risk_overlay_markdown() -> str:
    lines = [
        "# Round-67 R1 Loop-3 Risk Overlays",
        "",
        "- `CONTRACT_QUALITY_ALIGNED`: contract amount, duration, counterparty, delivery schedule, margin, OP/EPS, FCF, and price path align.",
        "- `BACKLOG_WITHOUT_MARGIN`: backlog exists but margin and EPS conversion are unclear.",
        "- `GRID_BOTTLENECK_STRUCTURAL`: lead time, price, import/factory slot, CAPA bottleneck, and revision evidence align.",
        "- `DATA_CENTER_POWER_4B`: orders/backlog are strong but valuation is already crowded.",
        "- `PROJECT_DELAY_RISK`: data-center, rail, nuclear, reconstruction, or infrastructure demand exists but projects are delayed.",
        "- `CAPITAL_ALLOCATION_SHOCK`: order/backlog remains attractive but dilution or funding damages the price path.",
        "- `NAVAL_MRO_OPTION_ONLY`: MRO credential or initial contract exists, but high-margin repeat MRO or newbuild conversion is unproven.",
        "- `EXISTING_NUCLEAR_PPA_ALIGNED`: existing nuclear PPA supports cashflow visibility better than SMR policy talk.",
        "- `SMR_POLICY_FALSE_GREEN`: SMR policy/thematic demand lacks cost, customer, permit, financing, or revenue confirmation.",
        "- `POLICY_TO_CONTRACT_FAILED`: reconstruction, Neom, or policy infra news does not become funded order or revenue.",
        "",
        "Simple example: `as_of_date=2025-02-26` and a rail contract is announced. That can be Stage 2 evidence. It is not Stage 3-Green until margin, financing, warranty, delivery schedule, and OP/EPS path are visible as of that date.",
    ]
    return "\n".join(lines) + "\n"


def render_round67_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-67 R1 Loop-3 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare contract quality, backlog, margin, OP/EPS revision, FCF conversion, and price path.",
        "6. Mark project delay, capital-allocation shock, low-margin backlog, MRO option-only, SMR policy false Green, and policy-to-contract failure explicitly.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round67_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `CONTRACT_QUALITY_ALIGNED`: contract value/duration/counterparty/delivery/margin/EPS and price path align.",
            "- `BACKLOG_WITHOUT_MARGIN`: backlog/order exists but margin or EPS conversion is not proven.",
            "- `PROJECT_DELAY_RISK`: demand exists but project execution threatens order growth.",
            "- `CAPITAL_ALLOCATION_SHOCK`: backlog remains attractive but dilution or funding damages price path.",
            "- `SMR_POLICY_FALSE_GREEN`: policy and theme exist but cost/customer/permit/financing are missing.",
            "- `POLICY_TO_CONTRACT_FAILED`: policy/MOU does not become funded order or revenue.",
        ]
    )
    return "\n".join(lines) + "\n"


def _round67_score_price_alignment(candidate: Round67CaseCandidate) -> str:
    if candidate.case_type in {"structural_success", "success_candidate", "cyclical_success"}:
        return "aligned"
    if candidate.case_type in {"event_premium", "overheat", "4b_watch"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "failed_rerating" and "capital_allocation" in candidate.alignment_hint:
        return "evidence_good_but_price_failed"
    return "false_positive_score"


def _round67_rerating_result(candidate: Round67CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "event_premium":
        return "event_premium"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "4b_watch":
        return "theme_overheat"
    return "unknown" if candidate.case_type == "success_candidate" else "no_rerating"


def _numeric_weight(value: int | str) -> float:
    if isinstance(value, int):
        return float(value)
    if value == "gate":
        return 0.0
    return float(value)


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
    "ROUND67_CASE_CANDIDATES",
    "ROUND67_DEFAULT_CASES_PATH",
    "ROUND67_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND67_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND67_PRICE_FIELDS",
    "ROUND67_SCORE_TARGETS",
    "Round67CaseCandidate",
    "Round67ScoreTarget",
    "Round67ScoreWeightDraft",
    "render_round67_green_guardrail_markdown",
    "render_round67_loop3_risk_overlay_markdown",
    "render_round67_price_validation_plan_markdown",
    "render_round67_summary_markdown",
    "round67_case_candidate_rows",
    "round67_case_records",
    "round67_price_field_rows",
    "round67_score_profile_rows",
    "round67_stage_date_rows",
    "round67_summary",
    "round67_target_for",
    "write_round67_r1_loop3_reports",
]
