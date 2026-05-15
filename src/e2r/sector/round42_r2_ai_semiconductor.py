"""Round-42 R2 AI/semiconductor/electronics calibration pack.

Round 42 expands the Round-40 protocol for R2 AI, semiconductor, and
electronics themes. It stores target sub-archetypes, shadow score-weight
drafts, stage-date guidance, case candidates, and price-validation fields.

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


ROUND42_SOURCE_ROUND_PATH = "docs/round/round_42.md"
ROUND42_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round42_r2_ai_semiconductor"
ROUND42_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_round42.jsonl"
ROUND42_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round42_r2_v1.csv"


@dataclass(frozen=True)
class Round42ScoreWeightDraft:
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
class Round42ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round42ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round42CaseCandidate:
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


ROUND42_SCORE_TARGETS: tuple[Round42ScoreTarget, ...] = (
    Round42ScoreTarget(
        "MEMORY_HBM_CAPACITY",
        E2RArchetype.MEMORY_HBM_CAPACITY,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round42ScoreWeightDraft(24, 21, 19, 15, 12, 0, 5),
        ("hbm_demand", "memory_price_increase", "ai_server_memory_shortage"),
        ("hbm_sales_mix", "op_eps_revision", "supply_discipline", "customer_supply_allocation"),
        ("long_term_contract", "prepayment_or_price_band", "hbm_capa_constraint", "multi_year_eps_revision", "pbr_to_per_frame_shift"),
        ("market_cap_rerating_saturated", "crowded_hbm_consensus", "capex_overbuild_news"),
        ("ai_capex_slowdown", "hbm_price_decline", "capacity_oversupply", "customer_order_cut"),
        ("hbm_demand", "capacity_constraint", "multi_year_eps_revision", "supply_discipline", "customer_visibility"),
        ("crowding", "capex_reversal", "customer_price_resistance", "memory_price_decline"),
        "HBM can be Green only when AI memory demand becomes source-backed EPS/FCF and capacity-bottleneck evidence.",
    ),
    Round42ScoreTarget(
        "COMMODITY_MEMORY_GENERAL_SEMI",
        E2RArchetype.MEMORY_HBM_CAPACITY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(22, 16, 17, 13, 10, 0, 5),
        ("dram_or_nand_price_increase", "earnings_turnaround", "hbm_conversion_supply_squeeze"),
        ("op_eps_revision", "inventory_normalization", "supply_discipline"),
        ("commodity_memory_price_support", "multi_quarter_revision", "cycle_to_structural_frame_shift"),
        ("memory_rally_crowded", "price_rebound_fully_priced"),
        ("supply_rebound", "hbm_competitive_lag", "price_decline", "customer_capex_cut"),
        ("op_eps_revision", "supply_discipline", "inventory_normalization"),
        ("pure_cyclical_bounce", "hbm_lag", "supply_rebound"),
        "General DRAM/NAND recovery stays Watch-to-Green because commodity memory can reverse quickly.",
    ),
    Round42ScoreTarget(
        "SEMI_EQUIPMENT_CAPEX",
        E2RArchetype.SEMI_EQUIPMENT_CAPEX,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(22, 20, 18, 14, 12, 0, 5),
        ("customer_ai_hbm_fab_capex", "equipment_order_keyword", "euv_or_back_end_tool_keyword"),
        ("equipment_order", "guidance_raise", "backlog_growth", "customer_capex_budget"),
        ("order_to_revenue_conversion", "op_eps_revision", "customer_diversification", "margin_visible"),
        ("equipment_group_overheating", "customer_capex_peak"),
        ("order_pushout", "export_control", "customer_capex_cut", "inventory_build"),
        ("customer_capex", "orders", "revenue_conversion", "op_eps_revision"),
        ("order_pushout", "export_control", "customer_concentration"),
        "Equipment needs customer CAPEX plus order-to-revenue conversion; capex peak is a first-class 4B/4C risk.",
    ),
    Round42ScoreTarget(
        "SEMI_MATERIALS_PROCESS",
        E2RArchetype.SEMI_EQUIPMENT_CAPEX,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(20, 18, 14, 13, 11, 0, 5),
        ("process_material_keyword", "customer_qualification", "fab_ramp"),
        ("qualification_passed", "volume_ramp", "margin_visibility"),
        ("repeat_volume", "customer_diversification", "op_eps_revision"),
        ("material_theme_crowded", "qualification_fully_priced"),
        ("qualification_delay", "customer_capex_cut", "price_pressure"),
        ("qualification", "volume_ramp", "margin_visibility"),
        ("qualification_delay", "single_customer", "price_pressure"),
        "Materials need qualification and volume ramp evidence, not only semiconductor theme tags.",
    ),
    Round42ScoreTarget(
        "ADVANCED_PACKAGING_PCB",
        E2RArchetype.SEMI_EQUIPMENT_CAPEX,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(21, 20, 18, 13, 12, 0, 5),
        ("ai_server_pcb", "optical_transceiver_pcb", "glass_substrate_keyword", "cxl_substrate_keyword"),
        ("order_visibility", "lead_time_extended", "capacity_constraint", "op_eps_revision"),
        ("ai_server_demand_converts_to_revenue", "pricing_power", "customer_diversification"),
        ("substrate_theme_crowded", "capa_expansion_news"),
        ("capa_normalization", "customer_order_delay", "yield_issue"),
        ("order_visibility", "capacity_constraint", "op_eps_revision", "pricing_power"),
        ("capa_normalization", "theme_without_order", "customer_delay"),
        "PCB/substrate can improve quickly, but Green requires order visibility and margin conversion.",
    ),
    Round42ScoreTarget(
        "ADVANCED_PACKAGING_COWOS_EMIB",
        E2RArchetype.SEMI_EQUIPMENT_CAPEX,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round42ScoreWeightDraft(22, 21, 20, 14, 12, 0, 5),
        ("cowos_bottleneck", "emib_keyword", "2_5d_packaging", "interposer_substrate"),
        ("packaging_tool_or_substrate_order", "lead_time_extended", "capacity_shortage"),
        ("packaging_revenue_growth", "op_eps_revision", "bottleneck_frame_confirmed"),
        ("bottleneck_consensus_crowded", "capa_expansion"),
        ("bottleneck_easing", "yield_issue", "customer_capex_delay"),
        ("packaging_bottleneck", "revenue_growth", "op_eps_revision", "customer_visibility"),
        ("capa_expansion", "yield_issue", "bottleneck_easing"),
        "Advanced packaging can be Green when bottleneck economics show up in revenue and EPS, not just CoWoS keywords.",
    ),
    Round42ScoreTarget(
        "DISPLAY_OLED_SUPPLYCHAIN",
        E2RArchetype.SEMI_EQUIPMENT_CAPEX,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(19, 18, 12, 13, 11, 0, 5),
        ("oled_capex", "lcd_to_oled_shift", "apple_oled_keyword"),
        ("panel_capex_order", "material_volume_ramp", "margin_visible"),
        ("multi_customer_oled_ramp", "op_eps_revision", "cycle_risk_controlled"),
        ("display_capex_crowded", "panel_capex_peak"),
        ("panel_capex_delay", "price_pressure", "customer_cut"),
        ("panel_capex_order", "volume_ramp", "margin_visible"),
        ("capex_cycle", "single_customer", "panel_delay"),
        "OLED/display supply chain is cyclical and should remain Watch until durable order and margin evidence exist.",
    ),
    Round42ScoreTarget(
        "ELECTRONIC_COMPONENTS_MLCC_SENSOR",
        E2RArchetype.SEMI_EQUIPMENT_CAPEX,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(19, 17, 13, 12, 11, 1, 5),
        ("mlcc_sensor_or_camera_keyword", "smartphone_parts_recovery", "content_growth"),
        ("customer_diversification", "content_per_device_growth", "margin_improvement"),
        ("recurring_component_growth", "op_eps_revision", "inventory_normalization"),
        ("component_cycle_crowded", "smartphone_recovery_fully_priced"),
        ("inventory_build", "customer_cut", "asp_pressure"),
        ("content_growth", "customer_diversification", "margin_improvement"),
        ("smartphone_cycle_only", "inventory_build", "asp_pressure"),
        "Components need content growth and inventory discipline because end-device cycles can reverse.",
    ),
    Round42ScoreTarget(
        "AI_CHIP_FABRIC_INFRA",
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(18, 15, 12, 14, 11, 0, 5),
        ("ai_chip_tapeout", "foundry_or_system_semi_keyword", "domestic_ai_chip"),
        ("customer_design_win", "mass_production_plan", "yield_or_foundry_progress"),
        ("revenue_conversion", "gross_margin_visible", "repeat_customer"),
        ("ai_chip_theme_crowded", "ipo_or_mou_premium"),
        ("tapeout_delay", "yield_failure", "no_revenue", "customer_loss"),
        ("design_win", "mass_production", "revenue_conversion"),
        ("mou_only", "no_revenue", "yield_issue"),
        "AI chip/fabric remains Watch until design wins convert into yield, production, and revenue.",
    ),
    Round42ScoreTarget(
        "AI_ACCELERATOR_CHIP_PUREPLAY",
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(18, 15, 13, 15, 10, 0, 5),
        ("ai_accelerator_ipo", "wafer_scale_engine", "nvidia_competition_keyword"),
        ("named_customer", "commercial_revenue", "gross_margin_visible"),
        ("repeat_customer", "software_ecosystem", "eps_or_fcf_path"),
        ("pureplay_valuation_overheat", "nvidia_competition_ignored"),
        ("customer_loss", "no_revenue", "valuation_compression", "funding_need"),
        ("named_customer", "commercial_revenue", "gross_margin_visible"),
        ("valuation_overheat", "no_revenue", "funding_need"),
        "AI accelerator pure-play can be researched, but valuation and Nvidia competition keep it Watch-first.",
    ),
    Round42ScoreTarget(
        "AI_SERVER_ODM_EMS_SUPPLY_CHAIN",
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(22, 19, 16, 14, 11, 0, 5),
        ("ai_server_rack_demand", "odm_ems_keyword", "server_shipment_growth"),
        ("ai_server_revenue_mix", "shipment_growth", "op_eps_revision"),
        ("ai_server_mix_changes_eps_fcf", "margin_stability", "customer_diversification"),
        ("ai_server_valuation_overheat", "inventory_growth"),
        ("accounting_issue", "auditor_resignation", "low_margin", "inventory_build", "customer_concentration"),
        ("ai_server_revenue_mix", "op_eps_revision", "margin_stability"),
        ("accounting_issue", "low_margin", "inventory_build", "customer_concentration"),
        "ODM/EMS revenue can surge, but low margin, inventory, customer concentration, and trust risk cap Green.",
    ),
    Round42ScoreTarget(
        "NEOCLOUD_GPU_RENTAL",
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(18, 21, 18, 14, 10, 0, 5),
        ("large_gpu_cloud_contract", "gpu_rental_keyword", "take_or_pay_contract"),
        ("backlog_or_take_or_pay", "revenue_growth", "ebitda_improvement"),
        ("fcf_conversion", "debt_stabilization", "customer_diversification"),
        ("ai_cloud_valuation_overheat", "gpu_debt_multiple"),
        ("refinancing_pressure", "gpu_obsolescence", "customer_concentration", "fcf_negative"),
        ("take_or_pay_backlog", "fcf_conversion", "debt_stabilization"),
        ("high_debt", "fcf_negative", "gpu_obsolescence", "customer_concentration"),
        "Neocloud is high-risk Watch: backlog matters, but debt, GPU depreciation, and FCF decide quality.",
    ),
    Round42ScoreTarget(
        "OPTICAL_NETWORKING_AI_DATACENTER",
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round42ScoreWeightDraft(21, 22, 20, 13, 12, 0, 5),
        ("optical_networking_bottleneck", "fiber_or_transceiver_demand", "ai_datacenter_network"),
        ("hyperscaler_contract", "lead_time_extended", "order_visibility"),
        ("long_term_contract", "op_eps_revision", "bottleneck_frame_confirmed"),
        ("optical_group_crowded", "valuation_band_expansion"),
        ("capa_normalization", "customer_capex_delay", "order_cancellation"),
        ("hyperscaler_contract", "lead_time_extended", "op_eps_revision", "capacity_constraint"),
        ("capa_normalization", "customer_capex_delay", "order_cancellation"),
        "Optical networking can be Green when hyperscaler demand, lead time, and EPS evidence line up.",
    ),
    Round42ScoreTarget(
        "INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA",
        E2RArchetype.SEMI_EQUIPMENT_CAPEX,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(19, 23, 13, 13, 12, 3, 5),
        ("fab_gas_plant", "ultrahigh_purity_nitrogen", "onsite_utility_contract"),
        ("long_term_gas_supply", "fab_ramp", "capacity_commitment"),
        ("utility_like_revenue_visibility", "margin_visible", "customer_contract_duration"),
        ("utility_contract_fully_priced",),
        ("fab_delay", "customer_capex_cut", "contract_margin_low"),
        ("long_term_supply", "contract_duration", "fab_ramp", "margin_visible"),
        ("fab_delay", "capex_cut", "low_margin_contract"),
        "Semiconductor gases are utility-like; duration and fab ramp matter more than theme heat.",
    ),
    Round42ScoreTarget(
        "AI_DATA_CENTER_COOLING",
        E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round42ScoreWeightDraft(21, 22, 22, 13, 12, 0, 5),
        ("liquid_cooling", "immersion_cooling", "thermal_management", "hvac_datacenter"),
        ("strategic_cooling_contract", "data_center_customer", "capacity_constraint"),
        ("order_to_revenue_conversion", "op_eps_revision", "thermal_bottleneck_confirmed"),
        ("cooling_theme_crowded", "capacity_expansion"),
        ("customer_capex_delay", "technology_substitution", "margin_miss"),
        ("data_center_customer", "thermal_bottleneck", "orders", "op_eps_revision"),
        ("customer_capex_delay", "technology_substitution", "margin_miss"),
        "AI cooling is Green-capable only when thermal bottleneck turns into orders, revenue, and margin.",
    ),
    Round42ScoreTarget(
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(18, 23, 18, 13, 13, 5, 5),
        ("data_center_reit_ipo", "hyperscaler_lease", "power_capacity_site"),
        ("lease_backlog", "occupancy_growth", "funding_cost_visible"),
        ("cash_yield_growth", "lease_duration", "capital_cost_controlled"),
        ("data_center_reit_crowded", "cap_rate_compression"),
        ("funding_cost_spike", "power_constraint", "lease_delay"),
        ("lease_backlog", "funding_cost_visible", "cash_yield_growth"),
        ("funding_cost", "power_constraint", "flat_ipo"),
        "Data-center REITs need lease cash-flow and funding-cost evidence; AI real-estate label alone is not enough.",
    ),
    Round42ScoreTarget(
        "AI_GRID_FLEXIBILITY_SOFTWARE",
        E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round42ScoreWeightDraft(17, 17, 15, 13, 10, 0, 6),
        ("grid_flexibility_software", "virtual_power_plant", "ai_power_management"),
        ("utility_customer", "recurring_contract", "deployment_schedule"),
        ("recurring_revenue", "gross_margin_visible", "grid_customer_expansion"),
        ("grid_ai_software_crowded",),
        ("pilot_only", "regulatory_delay", "no_recurring_revenue"),
        ("utility_customer", "recurring_revenue", "deployment_schedule"),
        ("pilot_only", "regulatory_delay", "no_recurring_revenue"),
        "Grid flexibility software stays Watch until utility deployment becomes recurring revenue.",
    ),
    Round42ScoreTarget(
        "REDTEAM_ACCOUNTING_TRUST_OVERLAY",
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round42ScoreWeightDraft(0, 0, 0, 0, 0, 0, 0),
        ("auditor_resignation", "filing_delay", "internal_control_issue", "related_party_transaction"),
        ("trust_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("auditor_resignation", "filing_delay", "internal_control_weakness", "related_party_transaction"),
        (),
        ("auditor_resignation", "filing_delay", "internal_control_weakness", "related_party_transaction"),
        "Accounting/trust overlay is a hard RedTeam gate, not a positive scoring bucket.",
        gate_only=True,
    ),
)


ROUND42_CASE_CANDIDATES: tuple[Round42CaseCandidate, ...] = (
    Round42CaseCandidate(
        "sk_hynix_hbm_rerating_success_case",
        "MEMORY_HBM_CAPACITY",
        "000660",
        "SK하이닉스 HBM 리레이팅",
        "KR",
        "structural_success",
        None,
        date(2026, 5, 14),
        None,
        date(2026, 5, 14),
        None,
        ("hbm_demand", "market_cap_rerating", "multi_year_eps_revision_candidate", "capacity_constraint"),
        ("crowding", "capex_reversal", "customer_price_resistance"),
        "aligned_success_plus_4b_watch",
        "needs_price_backfill",
        ("Reuters SK Hynix AI memory rerating",),
        "HBM changed the market frame from commodity memory to AI infrastructure bottleneck; 4B-watch is required after large rerating.",
    ),
    Round42CaseCandidate(
        "sk_hynix_asml_euv_capex_case",
        "SEMI_EQUIPMENT_CAPEX",
        "000660",
        "SK하이닉스 ASML EUV CAPEX",
        "KR",
        "success_candidate",
        None,
        date(2026, 3, 24),
        None,
        None,
        None,
        ("customer_ai_hbm_fab_capex", "euv_order", "next_generation_process", "hbm_competitiveness"),
        ("customer_capex_peak", "order_pushout", "export_control"),
        "equipment_capex_success_signal",
        "needs_price_backfill",
        ("WSJ SK Hynix EUV order",),
        "Large EUV order is CAPEX evidence for the equipment chain, but supplier revenue conversion must be backfilled.",
    ),
    Round42CaseCandidate(
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
        ("guidance_raise", "semiconductor_equipment_growth", "packaging_revenue_growth", "after_hours_price_reaction"),
        ("customer_capex_peak", "order_pushout"),
        "early_aligned_candidate",
        "needs_price_backfill",
        ("Reuters Applied Materials guidance",),
        "Guidance and packaging growth are aligned, but 180D/1Y MFE and margin durability remain open.",
        (E2RArchetype.SEMI_EQUIPMENT_CAPEX,),
    ),
    Round42CaseCandidate(
        "nvidia_cowos_l_packaging_bottleneck_case",
        "ADVANCED_PACKAGING_COWOS_EMIB",
        "NVDA",
        "NVIDIA CoWoS-L packaging bottleneck",
        "US",
        "success_candidate",
        None,
        date(2025, 1, 16),
        None,
        None,
        None,
        ("cowos_l", "advanced_packaging_bottleneck", "ai_accelerator_demand", "supplier_capacity_constraint"),
        ("capacity_normalization", "customer_capex_delay"),
        "structural_bottleneck_reference",
        "needs_price_backfill",
        ("Reuters Nvidia advanced packaging bottleneck reference",),
        "Reference case for CoWoS/EMIB economics; Korean supplier mapping must be source-backed.",
        (E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,),
    ),
    Round42CaseCandidate(
        "broadcom_optical_pcb_leadtime_case",
        "OPTICAL_NETWORKING_AI_DATACENTER",
        "AVGO",
        "Broadcom optical/PCB lead-time reference",
        "US",
        "success_candidate",
        None,
        date(2026, 3, 24),
        None,
        None,
        None,
        ("optical_networking_bottleneck", "lead_time_extended", "ai_datacenter_network", "pcb_substrate_demand"),
        ("capa_normalization", "customer_capex_delay"),
        "supply_chain_bottleneck_reference",
        "needs_price_backfill",
        ("Round42 Broadcom optical/PCB reference",),
        "Optical and PCB lead-time evidence should route supplier research, not become automatic Green.",
        (E2RArchetype.SEMI_EQUIPMENT_CAPEX,),
    ),
    Round42CaseCandidate(
        "meta_corning_fiber_contract_case",
        "OPTICAL_NETWORKING_AI_DATACENTER",
        "GLW",
        "Meta-Corning fiber contract",
        "US",
        "success_candidate",
        None,
        date(2026, 1, 27),
        None,
        date(2026, 1, 27),
        None,
        ("hyperscaler_contract", "fiber_demand", "order_visibility", "event_day_price_reaction"),
        ("optical_group_crowded", "capa_normalization"),
        "aligned_candidate_plus_4b_watch",
        "needs_price_backfill",
        ("Reuters Meta Corning fiber contract",),
        "Hyperscaler contract and price reaction are aligned; rerating size and backlog conversion need validation.",
    ),
    Round42CaseCandidate(
        "tower_semiconductor_ai_light_chip_deal_case",
        "AI_CHIP_FABRIC_INFRA",
        "TSEM",
        "Tower Semiconductor AI light-chip deal",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 13),
        None,
        None,
        None,
        ("ai_chip_customer_deal", "event_day_price_reaction", "foundry_revenue_path"),
        ("no_revenue", "yield_issue", "single_customer"),
        "event_aligned_candidate",
        "needs_price_backfill",
        ("Reuters Tower Semiconductor AI chip deal",),
        "Event reaction is useful, but Stage 3 needs production, yield, and revenue conversion.",
    ),
    Round42CaseCandidate(
        "air_liquide_micron_gas_plant_case",
        "INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA",
        "AI.PA",
        "Air Liquide-Micron gas plant",
        "EU",
        "success_candidate",
        None,
        date(2024, 6, 5),
        None,
        None,
        None,
        ("long_term_gas_supply", "fab_gas_plant", "onsite_utility", "customer_fab_ramp"),
        ("fab_delay", "low_margin_contract"),
        "utility_like_success_candidate",
        "needs_price_backfill",
        ("Round42 Air Liquide Micron gas plant reference",),
        "Semiconductor gas supply is a duration/utility-style case, not a high-beta theme case.",
    ),
    Round42CaseCandidate(
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
        ("liquid_cooling", "strategic_cooling_contract", "thermal_bottleneck", "data_center_customer"),
        ("technology_substitution", "customer_capex_delay"),
        "strategic_cooling_candidate",
        "needs_price_backfill",
        ("Round42 Ecolab CoolIT cooling reference",),
        "AI cooling can be Green-capable if thermal bottleneck turns into repeat revenue and margin.",
    ),
    Round42CaseCandidate(
        "coreweave_neocloud_high_debt_case",
        "NEOCLOUD_GPU_RENTAL",
        "CRWV",
        "CoreWeave neocloud high-debt watch",
        "US",
        "4b_watch",
        None,
        None,
        None,
        None,
        None,
        ("large_gpu_cloud_contract", "take_or_pay_backlog", "revenue_growth"),
        ("high_debt", "fcf_negative", "gpu_obsolescence", "customer_concentration"),
        "high_risk_watch",
        "needs_source_date_and_price_backfill",
        ("Round42 CoreWeave IPO/neocloud reference",),
        "Neocloud can show backlog, but debt, GPU depreciation, FCF, and customer concentration keep it high-risk Watch.",
    ),
    Round42CaseCandidate(
        "blackstone_data_center_reit_case",
        "DATA_CENTER_REIT_INFRASTRUCTURE",
        "BX_DC_REF",
        "Blackstone data-center REIT infrastructure",
        "US",
        "failed_rerating",
        None,
        date(2026, 5, 14),
        None,
        None,
        None,
        ("data_center_reit_ipo", "ai_real_estate_demand", "lease_backlog_candidate"),
        ("flat_ipo", "funding_cost", "power_constraint"),
        "no_rerating_yet",
        "needs_price_backfill",
        ("Round42 Blackstone data-center REIT reference",),
        "Data-center property demand is not enough if cash yield, lease duration, and funding-cost evidence are weak.",
    ),
    Round42CaseCandidate(
        "supermicro_ey_resignation_4c_case",
        "REDTEAM_ACCOUNTING_TRUST_OVERLAY",
        "SMCI",
        "Supermicro EY resignation",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 10, 30),
        ("ai_server_revenue_mix",),
        ("auditor_resignation", "filing_delay", "internal_control_issue", "trust_issue"),
        "hard_4c_accounting_break",
        "needs_price_backfill",
        ("Reuters Supermicro EY resignation",),
        "AI server growth cannot overcome auditor resignation or filing/trust breakdown; this is a hard RedTeam case.",
        (E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE,),
    ),
    Round42CaseCandidate(
        "ai_server_odm_low_margin_inventory_counterexample",
        "AI_SERVER_ODM_EMS_SUPPLY_CHAIN",
        "AI_SERVER_ODM_REF",
        "AI 서버 ODM 저마진·재고 반례",
        "GLOBAL",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("ai_server_revenue_growth",),
        ("low_margin", "inventory_build", "customer_concentration", "accounting_issue"),
        "false_positive_score_risk",
        "missing_price_data",
        ("Round42 ODM risk note",),
        "Server revenue growth without margin, inventory, trust, and customer-quality evidence should not become Green.",
    ),
    Round42CaseCandidate(
        "samsung_commodity_memory_recovery_case",
        "COMMODITY_MEMORY_GENERAL_SEMI",
        "005930",
        "삼성전자 범용 메모리 회복",
        "KR",
        "cyclical_success",
        None,
        None,
        None,
        None,
        None,
        ("dram_nand_price_recovery", "op_recovery_candidate", "memory_cycle_rebound"),
        ("hbm_competitive_lag", "supply_rebound", "commodity_price_decline"),
        "cyclical_to_structural_candidate",
        "needs_source_date_and_price_backfill",
        ("Round42 Samsung memory recovery note",),
        "Commodity memory recovery can work, but HBM lag and supply rebound risk keep it below HBM-quality Green until proven.",
    ),
    Round42CaseCandidate(
        "cerebras_ai_chip_pureplay_valuation_case",
        "AI_ACCELERATOR_CHIP_PUREPLAY",
        "CEREBRAS_REF",
        "Cerebras AI chip pure-play valuation",
        "US",
        "overheat",
        None,
        None,
        None,
        None,
        None,
        ("ai_accelerator_ipo", "wafer_scale_engine", "nvidia_competition_keyword"),
        ("valuation_overheat", "no_revenue", "funding_need", "nvidia_competition"),
        "valuation_watch",
        "missing_public_price_data",
        ("Round42 Cerebras AI accelerator reference",),
        "AI accelerator pure-play stays Watch/Red unless customers, commercial revenue, and margin are verified.",
    ),
    Round42CaseCandidate(
        "commodity_memory_supply_rebound_false_positive",
        "COMMODITY_MEMORY_GENERAL_SEMI",
        "MEMORY_CYCLE_REF",
        "범용 메모리 공급 반등 반례",
        "GLOBAL",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("memory_price_rebound",),
        ("supply_rebound", "price_decline", "customer_capex_cut", "pure_cyclical_bounce"),
        "false_positive_score_risk",
        "missing_price_data",
        ("Round42 commodity memory false-positive note",),
        "Price-only memory rebounds should be capped when supply and customer CAPEX can reverse the cycle.",
    ),
    Round42CaseCandidate(
        "advanced_packaging_capacity_normalization_4b_watch",
        "ADVANCED_PACKAGING_COWOS_EMIB",
        "PACKAGING_4B_REF",
        "첨단패키징 CAPA 정상화 4B-watch",
        "GLOBAL",
        "4b_watch",
        None,
        None,
        None,
        None,
        None,
        ("packaging_bottleneck", "valuation_band_expansion", "bottleneck_consensus_crowded"),
        ("capa_expansion", "bottleneck_easing", "yield_issue", "customer_capex_delay"),
        "4b_watch",
        "missing_price_data",
        ("Round42 advanced packaging 4B note",),
        "Packaging bottleneck can be Green early, but capacity expansion and bottleneck easing create 4B-watch.",
    ),
    Round42CaseCandidate(
        "neocloud_debt_fcf_breakdown_4c_watch",
        "NEOCLOUD_GPU_RENTAL",
        "NEOCLOUD_4C_REF",
        "Neocloud 부채·FCF 훼손 4C-watch",
        "GLOBAL",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("gpu_rental_revenue_growth",),
        ("refinancing_pressure", "gpu_obsolescence", "fcf_negative", "customer_concentration"),
        "4c_watch",
        "missing_price_data",
        ("Round42 neocloud 4C note",),
        "GPU rental growth can break when debt, FCF, GPU obsolescence, or customer concentration overwhelms contracts.",
    ),
)


ROUND42_PRICE_FIELDS: tuple[str, ...] = (
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
    "revenue_revision_1q",
    "revenue_revision_1y",
    "op_revision_1q",
    "op_revision_1y",
    "eps_revision_1q",
    "eps_revision_1y",
    "gross_margin_change",
    "op_margin_change",
    "inventory_growth",
    "capex_growth",
    "backlog_growth",
    "customer_concentration",
    "debt_to_ebitda",
    "fcf_margin",
    "accounting_red_flag",
    "auditor_resignation",
    "filing_delay",
    "internal_control_issue",
    "score_price_alignment",
    "price_validation_status",
)


def target_for(target_id: str) -> Round42ScoreTarget | None:
    for target in ROUND42_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round42_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND42_CASE_CANDIDATES:
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
                f"Round42 R2 case for {candidate.target_id}; "
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
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "overheat", "4b_watch", "4c_thesis_break"} else None,
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
                "hbm_is_not_same_as_all_ai_semiconductor",
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


def round42_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND42_SCORE_TARGETS:
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
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round42_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND42_CASE_CANDIDATES:
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


def round42_stage_date_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND42_SCORE_TARGETS:
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


def round42_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round42_backfill": "true"} for field in ROUND42_PRICE_FIELDS)


def round42_summary() -> dict[str, int | bool]:
    records = round42_case_records()
    return {
        "target_count": len(ROUND42_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch"),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND42_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND42_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND42_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round42_r2_reports(
    *,
    output_directory: str | Path = ROUND42_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND42_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND42_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round42_r2_ai_semiconductor_summary.md",
        "case_matrix": output / "round42_r2_case_matrix.csv",
        "stage_date_plan": output / "round42_r2_stage_date_plan.csv",
        "green_guardrails": output / "round42_r2_green_guardrails.md",
        "price_validation_plan": output / "round42_r2_price_validation_plan.md",
        "price_fields": output / "round42_r2_price_fields.csv",
    }
    _write_case_jsonl(round42_case_records(), cases)
    _write_rows(round42_score_profile_rows(), score_profiles)
    _write_rows(round42_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round42_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round42_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round42_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round42_green_guardrail_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round42_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round42_summary_markdown() -> str:
    summary = round42_summary()
    lines = [
        "# Round-42 R2 AI / Semiconductor / Electronics Summary",
        "",
        f"- source_round: `{ROUND42_SOURCE_ROUND_PATH}`",
        "- large_sector: `AI_SEMICONDUCTOR_ELECTRONICS`",
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
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R2 must not score every AI tag equally. HBM bottleneck, optical networking, and data-center cooling are very different from AI-chip themes or low-margin server ODM stories.",
        "- Example: `HBM demand + capacity constraint + multi-year EPS revision` may become Green-capable evidence. `AI chip keyword + no revenue` remains Watch/Red.",
        "- Example: AI server revenue can look strong, but auditor resignation, filing delay, internal-control weakness, inventory build, or customer concentration should override the positive story.",
    ]
    return "\n".join(lines) + "\n"


def render_round42_green_guardrail_markdown() -> str:
    lines = [
        "# Round-42 R2 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND42_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions) or 'not applicable'} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these R2 v1.0 weights to production scoring yet.",
            "- Do not treat AI, HBM, CXL, glass substrate, or neocloud labels as score evidence by themselves.",
            "- Do not invent revenue, EPS, FCF, capacity, order, customer, margin, accounting, or price-path fields.",
            "- Do not loosen Stage 3-Green to catch AI themes. Green still requires cross-evidence and low RedTeam risk.",
            "- Treat auditor resignation, filing delay, internal-control weakness, and related-party trust issues as hard RedTeam evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round42_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-42 R2 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Calculate peak price, drawdown after peak, and below-stage3 flag.",
        "6. Compare price paths with revenue/OP/EPS revision, margin, inventory, CAPEX, customer concentration, debt, and accounting red flags.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | stage candidate | check |",
        "| --- | --- | --- |",
    ]
    priority = {
        "sk_hynix_hbm_rerating_success_case",
        "supermicro_ey_resignation_4c_case",
        "coreweave_neocloud_high_debt_case",
        "samsung_commodity_memory_recovery_case",
        "advanced_packaging_capacity_normalization_4b_watch",
        "neocloud_debt_fcf_breakdown_4c_watch",
    }
    for row in round42_case_candidate_rows():
        if row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or row["case_id"] in priority:
            stage_date = row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or "needs_source_date"
            lines.append(f"| `{row['case_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `aligned`: Stage 2/3 evidence and price rerating persist together.",
            "- `cyclical_success`: price worked, but structural EPS persistence is not yet proven.",
            "- `overheat`: valuation/theme pressure is high enough that Green should be restricted.",
            "- `false_positive_score`: theme or revenue looked strong, but margin/EPS/trust/price validation failed.",
            "- `thesis_break`: accounting, filing, internal-control, order, debt, or FCF failure damages the thesis.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round42CaseCandidate) -> str:
    if "aligned" in candidate.alignment_hint:
        return "aligned"
    if candidate.case_type in {"overheat", "4b_watch"}:
        return "price_moved_without_evidence"
    if candidate.case_type in {"failed_rerating", "4c_thesis_break"}:
        return "false_positive_score"
    return "unknown"


def _rerating_result(candidate: Round42CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
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
    "ROUND42_CASE_CANDIDATES",
    "ROUND42_DEFAULT_CASES_PATH",
    "ROUND42_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND42_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND42_PRICE_FIELDS",
    "ROUND42_SCORE_TARGETS",
    "ROUND42_SOURCE_ROUND_PATH",
    "Round42CaseCandidate",
    "Round42ScoreTarget",
    "Round42ScoreWeightDraft",
    "render_round42_green_guardrail_markdown",
    "render_round42_price_validation_plan_markdown",
    "render_round42_summary_markdown",
    "round42_case_candidate_rows",
    "round42_case_records",
    "round42_price_field_rows",
    "round42_score_profile_rows",
    "round42_stage_date_rows",
    "round42_summary",
    "target_for",
    "write_round42_r2_reports",
]
