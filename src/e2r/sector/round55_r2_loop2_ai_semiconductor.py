"""Round-55 R2 Loop-2 AI, semiconductor, and electronics pack.

Round 55 separates AI beneficiaries into different economic structures:
HBM, commodity memory, equipment, materials, packaging, optical/PCB,
server ODM, neocloud, cooling, AI chips, data-center infrastructure, and
accounting trust gates.

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


ROUND55_SOURCE_ROUND_PATH = "docs/round/round_55.md"
ROUND55_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round55_r2_loop2_ai_semiconductor"
ROUND55_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop2_round55.jsonl"
ROUND55_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round55_r2_loop2_v2.csv"


@dataclass(frozen=True)
class Round55ScoreWeightDraft:
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
class Round55ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round55ScoreWeightDraft
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
        return Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round55CaseCandidate:
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


ROUND55_SCORE_TARGETS: tuple[Round55ScoreTarget, ...] = (
    Round55ScoreTarget(
        "MEMORY_HBM_CAPACITY",
        E2RArchetype.MEMORY_HBM_CAPACITY,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round55ScoreWeightDraft(24, 21, 19, 14, 11, 0, 5),
        ("hbm_demand", "nvidia_supply_chain", "ai_server_memory_shortage"),
        ("hbm_sales_mix", "op_eps_revision", "customer_supply_allocation", "price_band_or_prepayment"),
        ("long_term_contract", "prepayment_or_price_band", "hbm_capa_constraint", "multi_year_eps_revision", "pbr_to_per_frame_shift"),
        ("market_cap_rerating_saturated", "crowded_hbm_consensus", "customer_price_resistance"),
        ("ai_capex_slowdown", "hbm_price_decline", "capacity_oversupply", "customer_order_cut"),
        ("hbm_demand", "capacity_constraint", "multi_year_eps_revision", "supply_discipline", "customer_visibility"),
        ("crowding", "capex_reversal", "customer_price_resistance", "memory_price_decline"),
        ("crowding", "capex_reversal", "customer_price_resistance"),
        "HBM remains the strongest R2 Green-capable axis, but Loop 2 lowers mispricing/valuation after broad recognition.",
    ),
    Round55ScoreTarget(
        "COMMODITY_MEMORY_GENERAL_SEMI",
        E2RArchetype.COMMODITY_MEMORY_GENERAL_SEMI,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(22, 16, 17, 13, 10, 0, 5),
        ("dram_price_rebound", "nand_price_rebound", "hbm_conversion_supply_squeeze"),
        ("op_eps_revision", "inventory_normalization", "supply_discipline"),
        ("commodity_memory_price_support", "multi_quarter_revision", "cycle_to_structural_frame_shift"),
        ("memory_rebound_crowded", "spot_price_fully_priced"),
        ("supply_rebound", "hbm_lag", "price_decline", "customer_capex_cut"),
        ("op_eps_revision", "supply_discipline", "inventory_normalization"),
        ("spot_rebound", "supply_rebound", "hbm_lag"),
        ("spot_rebound", "supply_rebound", "hbm_lag"),
        "General DRAM/NAND can be a strong cycle recovery but has lower visibility than HBM.",
    ),
    Round55ScoreTarget(
        "SEMI_EQUIPMENT_CAPEX",
        E2RArchetype.SEMI_EQUIPMENT_CAPEX,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(22, 20, 18, 14, 12, 0, 5),
        ("customer_ai_hbm_fab_capex", "equipment_order_keyword", "euv_or_packaging_tool_keyword"),
        ("equipment_order", "guidance_raise", "backlog_growth", "customer_capex_budget"),
        ("order_to_revenue_conversion", "op_eps_revision", "customer_diversification", "margin_visible"),
        ("equipment_group_overheating", "customer_capex_peak"),
        ("order_pushout", "export_control", "customer_capex_cut", "inventory_build"),
        ("customer_capex", "orders", "revenue_conversion", "op_eps_revision"),
        ("order_pushout", "export_control", "customer_capex_cut"),
        ("customer_capex_peak", "order_delay", "export_control"),
        "Equipment is Watch-to-Green because customer CAPEX can turn quickly.",
    ),
    Round55ScoreTarget(
        "SEMI_MATERIALS_PROCESS",
        E2RArchetype.SEMI_MATERIALS_PROCESS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(20, 18, 14, 13, 11, 0, 5),
        ("process_material_keyword", "customer_qualification", "fab_ramp"),
        ("qualification_passed", "volume_ramp", "margin_visibility"),
        ("repeat_volume", "customer_diversification", "op_eps_revision"),
        ("material_theme_crowded", "qualification_fully_priced"),
        ("qualification_delay", "customer_capex_cut", "price_pressure"),
        ("qualification", "volume_ramp", "margin_visibility"),
        ("qualification_delay", "single_customer", "price_pressure"),
        ("customer_concentration", "inventory", "price_pressure"),
        "Materials need qualification, repeat volume, and customer diversification.",
    ),
    Round55ScoreTarget(
        "ADVANCED_PACKAGING_PCB",
        E2RArchetype.ADVANCED_PACKAGING_PCB,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(21, 21, 19, 13, 12, 0, 5),
        ("ai_server_pcb", "optical_transceiver_pcb", "high_layer_pcb", "glass_substrate_keyword"),
        ("order_visibility", "lead_time_extended", "capacity_constraint", "op_eps_revision"),
        ("ai_server_demand_converts_to_revenue", "pricing_power", "customer_diversification"),
        ("pcb_substrate_theme_crowded", "capa_expansion_news"),
        ("capa_normalization", "inventory_build", "customer_order_delay", "yield_issue"),
        ("order_visibility", "capacity_constraint", "op_eps_revision", "pricing_power"),
        ("capa_normalization", "theme_without_order", "inventory_build"),
        ("customer_concentration", "capa_normalization", "inventory"),
        "Loop 2 separates AI optical PCB from ordinary PCB and keeps theme-only substrate stories Watch.",
    ),
    Round55ScoreTarget(
        "ADVANCED_PACKAGING_COWOS_EMIB",
        E2RArchetype.ADVANCED_PACKAGING_COWOS_EMIB,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round55ScoreWeightDraft(22, 21, 20, 14, 12, 0, 5),
        ("cowos_bottleneck", "cowos_l", "emib_keyword", "2_5d_packaging"),
        ("packaging_tool_or_substrate_order", "lead_time_extended", "capacity_shortage"),
        ("packaging_revenue_growth", "op_eps_revision", "bottleneck_frame_confirmed"),
        ("bottleneck_consensus_crowded", "capa_expansion"),
        ("bottleneck_easing", "yield_issue", "customer_capex_delay"),
        ("packaging_bottleneck", "revenue_growth", "op_eps_revision", "customer_visibility"),
        ("capa_expansion", "yield_issue", "bottleneck_easing"),
        ("capex_cycle", "yield", "bottleneck_normalization"),
        "CoWoS/EMIB can be Green when packaging bottleneck becomes revenue and EPS.",
    ),
    Round55ScoreTarget(
        "DISPLAY_OLED_SUPPLYCHAIN",
        E2RArchetype.DISPLAY_OLED_SUPPLYCHAIN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(19, 18, 12, 13, 11, 0, 5),
        ("oled_capex", "lcd_to_oled_shift", "display_customer_capex"),
        ("panel_capex_order", "material_volume_ramp", "margin_visible"),
        ("multi_customer_oled_ramp", "op_eps_revision", "cycle_risk_controlled"),
        ("display_capex_crowded", "panel_capex_peak"),
        ("panel_capex_delay", "price_pressure", "customer_cut"),
        ("panel_capex_order", "volume_ramp", "margin_visible"),
        ("capex_cycle", "single_customer", "panel_delay"),
        ("capex_cycle", "price_competition", "customer_concentration"),
        "OLED remains Watch because capex and price cycles can reverse.",
    ),
    Round55ScoreTarget(
        "ELECTRONIC_COMPONENTS_MLCC_SENSOR",
        E2RArchetype.ELECTRONIC_COMPONENTS_MLCC_SENSOR,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(19, 17, 13, 12, 11, 1, 5),
        ("mlcc_sensor_or_camera_keyword", "smartphone_parts_recovery", "content_growth"),
        ("customer_diversification", "content_per_device_growth", "margin_improvement"),
        ("recurring_component_growth", "op_eps_revision", "inventory_normalization"),
        ("component_cycle_crowded", "smartphone_recovery_fully_priced"),
        ("inventory_build", "customer_cut", "asp_pressure", "china_supply_chain_pressure"),
        ("content_growth", "customer_diversification", "margin_improvement"),
        ("inventory_build", "customer_cut", "asp_pressure"),
        ("inventory", "customer_concentration", "china_supply_chain"),
        "Electronic components need inventory discipline and customer diversification.",
    ),
    Round55ScoreTarget(
        "AI_CHIP_FABRIC_INFRA",
        E2RArchetype.AI_CHIP_FABRIC_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(18, 15, 12, 14, 11, 0, 5),
        ("ai_chip_tapeout", "foundry_or_system_semi_keyword", "domestic_ai_chip"),
        ("customer_design_win", "mass_production_plan", "yield_or_foundry_progress"),
        ("revenue_conversion", "gross_margin_visible", "repeat_customer"),
        ("ai_chip_theme_crowded", "ipo_or_mou_premium"),
        ("tapeout_delay", "yield_failure", "no_revenue", "customer_loss"),
        ("design_win", "mass_production", "revenue_conversion"),
        ("mou_only", "no_revenue", "yield_issue"),
        ("customer_validation", "yield", "no_revenue"),
        "AI chip fabric remains Watch until yield, mass production, and revenue are source-backed.",
    ),
    Round55ScoreTarget(
        "AI_ACCELERATOR_CHIP_PUREPLAY",
        E2RArchetype.AI_ACCELERATOR_CHIP_PUREPLAY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(18, 15, 13, 15, 10, 0, 5),
        ("ai_accelerator_ipo", "wafer_scale_engine", "nvidia_competition_keyword"),
        ("named_customer", "commercial_revenue", "gross_margin_visible"),
        ("repeat_customer", "software_ecosystem", "eps_or_fcf_path"),
        ("pureplay_valuation_overheat", "nvidia_competition_ignored"),
        ("customer_loss", "no_revenue", "valuation_compression", "funding_need"),
        ("named_customer", "commercial_revenue", "gross_margin_visible"),
        ("valuation_overheat", "no_revenue", "funding_need"),
        ("nvidia_competition", "valuation_overheat", "rd_burn"),
        "AI accelerator pure-play is high-risk Watch until customers, revenue, margin, and ecosystem are proven.",
    ),
    Round55ScoreTarget(
        "AI_SERVER_ODM_EMS_SUPPLY_CHAIN",
        E2RArchetype.AI_SERVER_ODM_EMS_SUPPLY_CHAIN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(22, 18, 15, 14, 10, 0, 5),
        ("ai_server_rack_demand", "odm_ems_keyword", "server_shipment_growth"),
        ("ai_server_revenue_mix", "shipment_growth", "op_eps_revision"),
        ("ai_server_mix_changes_eps_fcf", "margin_stability", "customer_diversification"),
        ("ai_server_valuation_overheat", "inventory_growth"),
        ("accounting_issue", "auditor_resignation", "low_margin", "inventory_build", "customer_concentration"),
        ("ai_server_revenue_mix", "op_eps_revision", "margin_stability"),
        ("accounting_issue", "low_margin", "inventory_build", "customer_concentration"),
        ("low_margin", "inventory", "accounting", "customer_concentration"),
        "ODM/EMS can grow revenue but is not HBM; margin, inventory, customer concentration, and trust gate matter.",
    ),
    Round55ScoreTarget(
        "NEOCLOUD_GPU_RENTAL",
        E2RArchetype.NEOCLOUD_GPU_RENTAL,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(18, 21, 18, 14, 9, 0, 5),
        ("large_gpu_cloud_contract", "gpu_rental_keyword", "take_or_pay_contract"),
        ("backlog_or_take_or_pay", "revenue_growth", "ebitda_improvement"),
        ("fcf_conversion", "debt_stabilization", "customer_diversification"),
        ("ai_cloud_valuation_overheat", "gpu_debt_multiple"),
        ("refinancing_pressure", "gpu_obsolescence", "customer_concentration", "fcf_negative", "ipo_downsize"),
        ("take_or_pay_backlog", "fcf_conversion", "debt_stabilization", "customer_diversification"),
        ("high_debt", "fcf_negative", "gpu_obsolescence", "customer_concentration"),
        ("high_debt", "gpu_depreciation", "fcf_negative", "customer_concentration"),
        "Neocloud has contract visibility but stays high-risk Watch until debt and FCF pass.",
    ),
    Round55ScoreTarget(
        "OPTICAL_NETWORKING_AI_DATACENTER",
        E2RArchetype.OPTICAL_NETWORKING_AI_DATACENTER,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round55ScoreWeightDraft(21, 22, 20, 13, 12, 0, 5),
        ("optical_networking_bottleneck", "fiber_or_transceiver_demand", "laser_supply_constraint"),
        ("hyperscaler_contract", "lead_time_extended", "order_visibility"),
        ("long_term_contract", "op_eps_revision", "bottleneck_frame_confirmed"),
        ("optical_group_crowded", "valuation_band_expansion"),
        ("lead_time_normalization", "new_capacity", "customer_capex_delay", "order_cancellation"),
        ("hyperscaler_contract", "lead_time_extended", "op_eps_revision", "capacity_constraint"),
        ("lead_time_normalization", "new_capacity", "customer_capex_delay"),
        ("customer_concentration", "lead_time_normalization", "valuation_crowding"),
        "Optical networking can be Green when hyperscaler demand, lead time, and EPS evidence line up.",
    ),
    Round55ScoreTarget(
        "INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA",
        E2RArchetype.INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(19, 23, 13, 13, 12, 3, 5),
        ("fab_gas_plant", "ultrahigh_purity_nitrogen", "onsite_utility_contract"),
        ("long_term_gas_supply", "fab_ramp", "capacity_commitment"),
        ("utility_like_revenue_visibility", "margin_visible", "customer_contract_duration"),
        ("utility_contract_fully_priced",),
        ("fab_delay", "customer_capex_cut", "contract_margin_low", "energy_cost_spike"),
        ("long_term_supply", "contract_duration", "fab_ramp", "margin_visible"),
        ("fab_delay", "capex_cut", "low_margin_contract"),
        ("fab_delay", "customer_concentration", "energy_cost"),
        "Semiconductor gases are utility-like; duration, fab ramp, and margin matter more than theme heat.",
    ),
    Round55ScoreTarget(
        "AI_DATA_CENTER_COOLING",
        E2RArchetype.AI_DATA_CENTER_COOLING,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round55ScoreWeightDraft(21, 22, 22, 13, 12, 0, 5),
        ("liquid_cooling", "immersion_cooling", "thermal_management", "hvac_datacenter"),
        ("strategic_cooling_contract", "data_center_customer", "capacity_constraint", "cooling_revenue"),
        ("order_to_revenue_conversion", "op_eps_revision", "thermal_bottleneck_confirmed", "service_revenue"),
        ("cooling_theme_crowded", "mna_multiple_expansion"),
        ("customer_capex_delay", "technology_substitution", "margin_miss", "mna_overpay", "debt_financing"),
        ("data_center_customer", "thermal_bottleneck", "orders", "op_eps_revision"),
        ("mna_overpay", "debt_financing", "customer_capex_delay", "eps_accretion_delay"),
        ("mna_overpay", "debt", "ai_capex_delay"),
        "AI cooling remains Green-capable, but M&A valuation and debt are Loop-2 RedTeam fields.",
    ),
    Round55ScoreTarget(
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        E2RArchetype.DATA_CENTER_REIT_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(18, 23, 18, 13, 13, 5, 5),
        ("data_center_reit_ipo", "hyperscaler_lease", "power_capacity_site"),
        ("lease_backlog", "occupancy_growth", "funding_cost_visible"),
        ("cash_yield_growth", "lease_duration", "capital_cost_controlled"),
        ("data_center_reit_crowded", "cap_rate_compression"),
        ("funding_cost_spike", "power_constraint", "lease_delay", "tenant_concentration"),
        ("lease_backlog", "funding_cost_visible", "cash_yield_growth"),
        ("funding_cost", "power_constraint", "tenant_concentration"),
        ("capex", "funding_cost", "tenant_concentration"),
        "Data-center REITs need AFFO/cash-yield evidence and funding-cost control.",
    ),
    Round55ScoreTarget(
        "AI_GRID_FLEXIBILITY_SOFTWARE",
        E2RArchetype.AI_GRID_FLEXIBILITY_SOFTWARE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round55ScoreWeightDraft(17, 17, 15, 13, 10, 0, 6),
        ("grid_flexibility_software", "virtual_power_plant", "ai_power_management"),
        ("utility_customer", "recurring_contract", "deployment_schedule"),
        ("recurring_revenue", "gross_margin_visible", "grid_customer_expansion"),
        ("grid_ai_software_crowded",),
        ("pilot_only", "regulatory_delay", "no_recurring_revenue"),
        ("utility_customer", "recurring_revenue", "deployment_schedule"),
        ("pilot_only", "regulatory_delay", "no_recurring_revenue"),
        ("poc", "commercialization_delay"),
        "Grid flexibility software stays Watch until utility deployment becomes recurring revenue.",
    ),
    Round55ScoreTarget(
        "REDTEAM_ACCOUNTING_TRUST_OVERLAY",
        E2RArchetype.REDTEAM_ACCOUNTING_TRUST_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round55ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("auditor_resignation", "filing_delay", "internal_control_issue", "related_party_transaction"),
        ("trust_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("auditor_resignation", "filing_delay", "internal_control_weakness", "doj_sec_investigation", "related_party_transaction"),
        (),
        ("auditor_resignation", "filing_delay", "internal_control_weakness", "doj_sec_investigation", "related_party_transaction"),
        ("auditor_resignation", "filing_delay", "internal_control_weakness"),
        "Accounting trust overlay is a hard RedTeam gate for R2; it is not a positive score bucket.",
        gate_only=True,
    ),
)


ROUND55_CASE_CANDIDATES: tuple[Round55CaseCandidate, ...] = (
    Round55CaseCandidate(
        "sk_hynix_hbm_rerating_success_case",
        "MEMORY_HBM_CAPACITY",
        "000660",
        "SK하이닉스 HBM 리레이팅",
        "KR",
        "structural_success",
        None,
        date(2026, 5, 14),
        date(2026, 5, 14),
        date(2026, 5, 14),
        None,
        ("hbm_demand", "ai_memory_rerating", "market_cap_rerating", "multi_year_eps_revision_candidate"),
        ("crowding", "capex_reversal", "customer_price_resistance"),
        "structural_ai_bottleneck_aligned_plus_4b_watch",
        "needs_price_backfill",
        ("round_55.md Reuters SK Hynix AI memory rerating",),
        "HBM is the strongest R2 structural success reference, but the same price path requires 4B-watch after broad recognition.",
        (E2RArchetype.STRUCTURAL_SUCCESS_ALIGNED, E2RArchetype.CROWDED_RERATING_4B_WATCH),
    ),
    Round55CaseCandidate(
        "applied_materials_ai_packaging_growth_case",
        "SEMI_EQUIPMENT_CAPEX",
        "AMAT",
        "Applied Materials AI packaging growth",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 14),
        None,
        None,
        None,
        ("guidance_raise", "semiconductor_equipment_growth", "packaging_revenue_growth", "after_hours_price_up_3pct"),
        ("customer_capex_peak", "order_pushout", "export_control"),
        "early_aligned_candidate",
        "needs_price_backfill",
        ("round_55.md Reuters Applied Materials guidance",),
        "AI CAPEX is showing up in equipment and packaging guidance, but equipment remains CAPEX-cycle Watch-to-Green.",
        (E2RArchetype.ADVANCED_PACKAGING_COWOS_EMIB,),
    ),
    Round55CaseCandidate(
        "nvidia_cowos_l_transition_case",
        "ADVANCED_PACKAGING_COWOS_EMIB",
        "NVDA",
        "NVIDIA CoWoS-L transition",
        "US",
        "success_candidate",
        None,
        date(2025, 1, 16),
        None,
        None,
        None,
        ("cowos_l", "advanced_packaging_bottleneck", "capacity_still_bottleneck", "blackwell_packaging"),
        ("capa_expansion", "bottleneck_normalization", "yield_issue"),
        "packaging_bottleneck_reference",
        "needs_price_backfill",
        ("round_55.md Reuters Nvidia CoWoS-L reference",),
        "CoWoS demand did not vanish; technology mix shifted. CAPA expansion still creates 4B risk.",
    ),
    Round55CaseCandidate(
        "broadcom_optical_pcb_leadtime_case",
        "OPTICAL_NETWORKING_AI_DATACENTER",
        "AVGO",
        "Broadcom optical PCB lead-time bottleneck",
        "US",
        "success_candidate",
        None,
        date(2026, 3, 24),
        None,
        None,
        None,
        ("optical_transceiver_pcb_leadtime", "lead_time_6_weeks_to_6_months", "laser_supply_constraint", "ai_datacenter_network"),
        ("new_capacity", "lead_time_normalization", "customer_concentration"),
        "optical_pcb_bottleneck_reference",
        "needs_price_backfill",
        ("round_55.md Reuters Broadcom optical/PCB bottleneck",),
        "AI bottleneck extends into optical networking and PCB, but Green still needs customer/order/OP evidence.",
        (E2RArchetype.ADVANCED_PACKAGING_PCB,),
    ),
    Round55CaseCandidate(
        "foxconn_ai_server_rack_growth_case",
        "AI_SERVER_ODM_EMS_SUPPLY_CHAIN",
        "2317.TW",
        "Foxconn AI server rack growth",
        "TW",
        "success_candidate",
        None,
        date(2026, 5, 14),
        None,
        None,
        None,
        ("ai_server_rack_shipments_double", "q1_profit_up", "ai_server_capex_up", "server_revenue_growth"),
        ("consignment_model", "low_margin", "inventory", "index_underperformance"),
        "ai_revenue_but_margin_watch",
        "needs_price_backfill",
        ("round_55.md Reuters Foxconn AI server rack growth",),
        "AI server revenue success is not HBM-style Green unless margin, inventory, and customer concentration pass.",
    ),
    Round55CaseCandidate(
        "ecolab_coolit_liquid_cooling_case",
        "AI_DATA_CENTER_COOLING",
        "ECL",
        "Ecolab-CoolIT liquid cooling",
        "US",
        "success_candidate",
        None,
        date(2026, 3, 20),
        None,
        None,
        None,
        ("liquid_cooling", "nvidia_amd_exposure", "cooling_revenue_550m", "eps_accretion_2028"),
        ("mna_overpay", "debt_financing", "eps_accretion_delay", "premarket_price_down"),
        "strategic_cooling_success_candidate_but_mna_debt_watch",
        "needs_price_backfill",
        ("round_55.md Reuters Ecolab CoolIT acquisition",),
        "AI cooling is Green-capable, but acquisition price, debt, and EPS accretion timing must be validated.",
    ),
    Round55CaseCandidate(
        "coreweave_openai_contract_ipo_case",
        "NEOCLOUD_GPU_RENTAL",
        "CRWV",
        "CoreWeave OpenAI contract IPO",
        "US",
        "4b_watch",
        None,
        date(2025, 3, 20),
        None,
        None,
        None,
        ("openai_contract_11_9b", "gpu_cloud_revenue_growth", "ipo_valuation_target"),
        ("microsoft_concentration", "net_loss", "high_debt", "gpu_depreciation"),
        "ai_contract_visibility_but_leverage_risk",
        "needs_price_backfill",
        ("round_55.md Reuters CoreWeave IPO/contract reference",),
        "Large contracts improve visibility, but high debt, customer concentration, and FCF risk block Green.",
        (E2RArchetype.LEVERAGE_FCF_BREAKDOWN,),
    ),
    Round55CaseCandidate(
        "coreweave_downsized_ipo_debt_case",
        "NEOCLOUD_GPU_RENTAL",
        "CRWV",
        "CoreWeave downsized IPO debt watch",
        "US",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("gpu_cloud_contracts", "revenue_growth"),
        ("ipo_downsize", "debt_8b", "fcf_negative", "microsoft_revenue_62pct", "customer_concentration"),
        "neocloud_4c_watch_debt_customer_concentration",
        "needs_source_date_and_price_backfill",
        ("round_55.md Investopedia CoreWeave IPO pricing/debt reference",),
        "Downsized IPO plus debt/customer concentration shows why neocloud is high-risk Watch rather than Green.",
        (E2RArchetype.LEVERAGE_FCF_BREAKDOWN,),
    ),
    Round55CaseCandidate(
        "supermicro_ey_resignation_case",
        "REDTEAM_ACCOUNTING_TRUST_OVERLAY",
        "SMCI",
        "Supermicro EY resignation",
        "US",
        "4c_thesis_break",
        date(2023, 1, 1),
        None,
        None,
        None,
        date(2024, 10, 30),
        ("ai_server_revenue_rerating", "market_cap_44b_to_67b"),
        ("auditor_resignation", "filing_delay", "internal_control_issue", "hindenburg_accounting_claim", "doj_probe"),
        "early_rerating_success_then_hard_4c",
        "needs_price_backfill",
        ("round_55.md Reuters Supermicro EY resignation",),
        "AI server growth cannot overcome auditor resignation or filing/trust breakdown; R2 accounting trust is a hard gate.",
        (E2RArchetype.AI_SERVER_ODM_EMS_SUPPLY_CHAIN, E2RArchetype.THESIS_BREAK_4C),
    ),
    Round55CaseCandidate(
        "samsung_ai_boom_labor_execution_case",
        "COMMODITY_MEMORY_GENERAL_SEMI",
        "005930",
        "삼성전자 AI boom labor/execution RedTeam",
        "KR",
        "failed_rerating",
        None,
        date(2026, 5, 15),
        None,
        None,
        None,
        ("ai_memory_recovery", "one_stop_semiconductor_strategy"),
        ("labor_strike", "execution_risk", "foundry_yield_risk", "talent_retention_risk"),
        "execution_labor_redteam",
        "needs_price_backfill",
        ("round_55.md Reuters Samsung AI boom labor divisions",),
        "Large semiconductor incumbents still need execution, foundry yield, HBM competitiveness, and labor stability checks.",
        (E2RArchetype.LEGAL_REGULATORY_REDTEAM,),
    ),
    Round55CaseCandidate(
        "commodity_memory_price_rebound_case",
        "COMMODITY_MEMORY_GENERAL_SEMI",
        "MEMORY_REBOUND",
        "Commodity DRAM/NAND rebound reference",
        "GLOBAL",
        "cyclical_success",
        None,
        None,
        None,
        None,
        None,
        ("memory_spot_price_rebound", "dram_nand_contract_price_rebound", "op_eps_recovery"),
        ("supply_rebound", "spot_reversal", "hbm_lag"),
        "cyclical_success_not_hbm_green",
        "needs_price_backfill",
        ("round_55.md commodity memory distinction",),
        "Commodity memory can produce strong EPS recovery, but it is not the same visibility profile as HBM.",
    ),
    Round55CaseCandidate(
        "cxl_glass_substrate_theme_case",
        "AI_CHIP_FABRIC_INFRA",
        "CXL_GLASS_THEME",
        "CXL/glass substrate theme-only reference",
        "GLOBAL",
        "overheat",
        None,
        None,
        None,
        None,
        None,
        ("cxl_keyword", "glass_substrate_keyword", "neuromorphic_theme"),
        ("theme_without_revenue", "no_customer_validation", "no_mass_production", "valuation_overheat"),
        "theme_without_revenue",
        "missing_price_data",
        ("round_55.md CXL/glass substrate theme guardrail",),
        "CXL, glass substrate, and neuromorphic tags remain Watch/Red until adoption, yield, and revenue are real.",
        (E2RArchetype.THEME_VALUATION_OVERHEAT,),
    ),
)


ROUND55_PRICE_FIELDS: tuple[str, ...] = (
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
    "hbm_revenue_share",
    "hbm_capacity_growth",
    "hbm_contract_duration",
    "hbm_price_band_flag",
    "prepayment_flag",
    "customer_name",
    "nvidia_supply_chain_flag",
    "memory_spot_price_change",
    "memory_contract_price_change",
    "dram_nand_mix",
    "commodity_memory_supply_rebound_flag",
    "equipment_order_growth",
    "equipment_backlog",
    "customer_capex_growth",
    "order_pushout_flag",
    "export_control_flag",
    "packaging_revenue_growth",
    "cowos_capacity_growth",
    "cowos_l_flag",
    "yield_issue_flag",
    "bottleneck_normalization_flag",
    "pcb_lead_time_weeks",
    "optical_transceiver_order",
    "laser_supply_constraint_flag",
    "hyperscaler_contract_flag",
    "ai_server_revenue",
    "ai_server_rack_shipments",
    "ai_server_margin",
    "consignment_model_flag",
    "inventory_growth",
    "customer_concentration",
    "gpu_cloud_revenue",
    "gpu_cloud_contract_value",
    "take_or_pay_flag",
    "debt_to_ebitda",
    "net_debt",
    "fcf_margin",
    "gpu_depreciation",
    "refinancing_risk_flag",
    "cooling_revenue",
    "liquid_cooling_order",
    "mna_price",
    "mna_debt_financing_flag",
    "eps_accretion_year",
    "auditor_resignation_flag",
    "filing_delay_flag",
    "internal_control_issue_flag",
    "regulatory_probe_flag",
    "related_party_risk_flag",
    "labor_strike_flag",
    "execution_risk_flag",
    "foundry_yield_risk_flag",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def target_for(target_id: str) -> Round55ScoreTarget | None:
    for target in ROUND55_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round55_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND55_CASE_CANDIDATES:
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
                f"Round55 R2 Loop-2 case for {candidate.target_id}; "
                "AI-semiconductor substructures and RedTeam evidence remain calibration-only."
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
                "hbm_is_not_same_as_all_ai_semiconductor",
                "do_not_invent_contract_prices_margins_or_stage_prices",
                "accounting_trust_is_hard_gate",
                "debt_fcf_customer_concentration_blocks_neocloud_green",
                "theme_without_revenue_blocks_green",
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


def round55_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND55_SCORE_TARGETS:
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


def round55_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND55_CASE_CANDIDATES:
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


def round55_stage_date_rows() -> tuple[dict[str, str], ...]:
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
        for target in ROUND55_SCORE_TARGETS
    )


def round55_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round55_backfill": "true"} for field in ROUND55_PRICE_FIELDS)


def round55_summary() -> dict[str, int | bool]:
    records = round55_case_records()
    return {
        "target_count": len(ROUND55_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND55_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND55_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND55_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND55_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round55_r2_loop2_reports(
    *,
    output_directory: str | Path = ROUND55_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND55_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND55_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round55_r2_loop2_ai_semiconductor_summary.md",
        "case_matrix": output / "round55_r2_loop2_case_matrix.csv",
        "stage_date_plan": output / "round55_r2_loop2_stage_date_plan.csv",
        "green_guardrails": output / "round55_r2_loop2_green_guardrails.md",
        "risk_overlays": output / "round55_r2_loop2_risk_overlays.md",
        "price_validation_plan": output / "round55_r2_loop2_price_validation_plan.md",
        "price_fields": output / "round55_r2_loop2_price_fields.csv",
    }
    _write_case_jsonl(round55_case_records(), cases)
    _write_rows(round55_score_profile_rows(), score_profiles)
    _write_rows(round55_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round55_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round55_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round55_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round55_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round55_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round55_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round55_summary_markdown() -> str:
    summary = round55_summary()
    lines = [
        "# Round-55 R2 Loop-2 AI / Semiconductor / Electronics Summary",
        "",
        f"- source_round: `{ROUND55_SOURCE_ROUND_PATH}`",
        "- large_sector: `AI_SEMICONDUCTOR_ELECTRONICS`",
        "- loop: `R2 Loop 2 / v2.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- cyclical_success_count: {summary['cyclical_success_count']}",
        f"- overheat_count: {summary['overheat_count']}",
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
        "- R2 Loop 2 says AI beneficiaries are not one structure.",
        "- Example: HBM can be structural Green because EPS/FCF, bottleneck, and price path can align.",
        "- Example: neocloud may have a huge contract, but high debt, FCF losses, GPU depreciation, and customer concentration block Green.",
        "- Example: Supermicro-style auditor resignation is a hard accounting trust gate for all R2 candidates.",
        "- Example: CXL or glass substrate keywords stay Watch/Red until customer validation, yield, production, and revenue exist.",
    ]
    return "\n".join(lines) + "\n"


def render_round55_green_guardrail_markdown() -> str:
    lines = [
        "# Round-55 R2 Loop-2 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-2 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND55_SCORE_TARGETS:
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
            "- Do not apply R2 Loop-2 v2.0 weights to production scoring yet.",
            "- Do not score every AI tag equally.",
            "- Do not treat CXL, glass substrate, AI chip, or neuromorphic keywords as Green evidence without revenue.",
            "- Do not invent contract duration, prepayment, price bands, margins, customer names, stage prices, or FCF.",
            "- Treat high debt, FCF losses, accounting trust breaks, customer concentration, and bottleneck normalization as hard RedTeam fields.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round55_risk_overlay_markdown() -> str:
    lines = [
        "# Round-55 R2 Loop-2 Risk Overlays",
        "",
        "- `structural_ai_bottleneck_aligned`: AI bottleneck converts into revenue, EPS/FCF, and price rerating.",
        "- `ai_revenue_but_margin_watch`: revenue rises, but margin, inventory, or customer concentration limit Green.",
        "- `ai_contract_visibility_but_leverage_risk`: contract visibility exists, but debt/FCF/GPU depreciation block Green.",
        "- `bottleneck_normalization_4b`: CoWoS, optical, PCB, or cooling bottleneck is real but capacity expansion can normalize it.",
        "- `accounting_trust_break_4c`: auditor resignation, filing delay, internal control, or regulatory probe breaks the thesis.",
        "- `theme_without_revenue`: CXL, glass substrate, AI chip, or neuromorphic tag has no customer validation or revenue.",
        "",
        "Simple example: `OpenAI contract` can be Stage 2 visibility for a GPU cloud. It is not Green if debt, FCF losses, GPU depreciation, and customer concentration are still unresolved.",
    ]
    return "\n".join(lines) + "\n"


def render_round55_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-55 R2 Loop-2 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare EPS revision, revenue guidance, backlog, margin, customer concentration, accounting flags, and price path.",
        "6. Mark accounting trust break, high debt, FCF loss, GPU depreciation, and bottleneck normalization explicitly.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round55_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `structural_ai_bottleneck_aligned`: HBM/packaging/optical/cooling bottleneck and EPS/price path align.",
            "- `ai_revenue_but_margin_watch`: AI server revenue grows but margin and working-capital quality are unproven.",
            "- `ai_contract_visibility_but_leverage_risk`: contract visibility exists but leverage and FCF block Green.",
            "- `theme_without_revenue`: technical theme has no customer validation, yield, production, or revenue.",
            "- `hard_4c_accounting_break`: trust evidence breaks the Stage 3 thesis.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round55CaseCandidate) -> str:
    if "theme_without_revenue" in candidate.alignment_hint:
        return "price_moved_without_evidence"
    if candidate.case_type in {"structural_success", "success_candidate", "cyclical_success"}:
        return "aligned"
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if "debt" in candidate.alignment_hint or "execution" in candidate.alignment_hint:
        return "evidence_good_but_price_failed"
    return "false_positive_score"


def _rerating_result(candidate: Round55CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "overheat":
        return "theme_overheat"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "4b_watch":
        return "theme_overheat"
    return "unknown" if candidate.case_type == "success_candidate" else "no_rerating"


def _score_weight_hint(target: Round55ScoreTarget) -> dict[str, float]:
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
    "ROUND55_CASE_CANDIDATES",
    "ROUND55_DEFAULT_CASES_PATH",
    "ROUND55_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND55_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND55_PRICE_FIELDS",
    "ROUND55_SCORE_TARGETS",
    "Round55CaseCandidate",
    "Round55ScoreTarget",
    "Round55ScoreWeightDraft",
    "render_round55_green_guardrail_markdown",
    "render_round55_price_validation_plan_markdown",
    "render_round55_risk_overlay_markdown",
    "render_round55_summary_markdown",
    "round55_case_candidate_rows",
    "round55_case_records",
    "round55_price_field_rows",
    "round55_score_profile_rows",
    "round55_stage_date_rows",
    "round55_summary",
    "target_for",
    "write_round55_r2_loop2_reports",
]
