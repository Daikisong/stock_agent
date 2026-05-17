"""Round-81 R2 Loop-4 AI, semiconductor, and electronics pack.

Round 81 returns to R2 after the R1 Loop-4 pass. It separates HBM leaders,
HBM catch-up execution, AI storage NAND, AI equipment CAPEX, advanced
packaging, optical networking, server ODM, neocloud, cooling, AI accelerator
pure-plays, and accounting trust overlays.

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


ROUND81_SOURCE_ROUND_PATH = "docs/round/round_81.md"
ROUND81_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round81_r2_loop4_ai_semiconductor"
ROUND81_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop4_round81.jsonl"
ROUND81_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round81_r2_loop4_v4.csv"


@dataclass(frozen=True)
class Round81ScoreWeightDraft:
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
class Round81ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round81ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop4_penalty_axes: tuple[str, ...]
    normalization_point: str
    hard_gate: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round81CaseCandidate:
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


def _weights(
    eps_fcf: int | str,
    visibility: int | str,
    bottleneck: int | str,
    mispricing: int | str,
    valuation: int | str,
    capital: int | str = 0,
    confidence: int | str = 5,
) -> Round81ScoreWeightDraft:
    return Round81ScoreWeightDraft(eps_fcf, visibility, bottleneck, mispricing, valuation, capital, confidence)


ROUND81_SCORE_TARGETS: tuple[Round81ScoreTarget, ...] = (
    Round81ScoreTarget(
        "MEMORY_HBM_CAPACITY",
        E2RArchetype.MEMORY_HBM_CAPACITY,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(24, 22, 20, 13, 9),
        ("hbm3e_hbm4_demand", "nvidia_supply_chain", "ai_memory_shortage"),
        ("hbm_revenue_share", "hbm_capacity_growth", "customer_allocation", "price_band_or_prepayment"),
        ("multi_year_eps_revision", "hbm_capacity_constraint", "lta_or_prepayment", "old_memory_frame_shift"),
        ("hbm_consensus_crowded", "market_cap_rerating_saturated", "customer_price_resistance"),
        ("ai_capex_slowdown", "capacity_oversupply", "hbm_price_decline", "customer_order_cut"),
        ("hbm_customer_visibility", "capacity_constraint", "multi_year_eps_revision", "price_band_or_prepayment"),
        ("customer_price_resistance", "capex_reversal", "capa_normalization", "memory_price_decline"),
        ("4b_crowding", "capacity_normalization", "customer_price_resistance"),
        "Loop 4 keeps HBM Green-capable, but valuation credit is reduced because successful HBM cases can already be 4B-watch.",
    ),
    Round81ScoreTarget(
        "HBM_CATCHUP_EXECUTION",
        E2RArchetype.HBM_CATCHUP_EXECUTION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(22, 18, 18, 14, 10),
        ("hbm4_sample", "hbm4_shipping", "hbm4e_sample_plan", "amd_or_nvidia_memory_mou"),
        ("customer_qualification", "volume_shipment", "hbm4_yield_signal", "customer_specific_base_die"),
        ("yield_stable", "hbm_revenue_share_growth", "fy1_fy2_eps_revision", "customer_adoption_visible"),
        ("catchup_expectation_crowded", "qualification_priced_before_volume"),
        ("qualification_delay", "yield_shortfall", "labor_strike", "production_disruption", "foundry_execution_issue"),
        ("customer_qualification", "volume_shipment", "yield_stable", "eps_revision"),
        ("qualification_delay", "yield_shortfall", "labor_strike", "production_disruption", "talent_retention_risk"),
        ("qualification", "yield", "labor", "foundry_execution"),
        "Samsung/Micron-style HBM catch-up is Watch-to-Green: shipment is not enough without qualification, yield, volume, and execution control.",
    ),
    Round81ScoreTarget(
        "AI_STORAGE_NAND_SHORTAGE",
        E2RArchetype.AI_STORAGE_NAND_SHORTAGE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(23, 17, 18, 12, 8),
        ("ai_storage_demand", "enterprise_ssd_shortage", "nand_underinvestment", "ssd_asp_increase"),
        ("nand_profit_growth", "enterprise_ssd_revenue", "profit_guidance_raise", "op_eps_revision"),
        ("multi_year_nand_shortage", "ai_storage_eps_revision", "supply_discipline"),
        ("ai_storage_narrative_crowded", "stock_up_10x_20x", "nand_shortage_fully_priced"),
        ("supply_rebound", "consumer_demand_destruction", "ssd_price_reversal", "memory_price_reversal"),
        ("enterprise_ssd_revenue", "nand_profit_growth", "op_eps_revision", "supply_discipline"),
        ("cycle_reversal", "supply_rebound", "consumer_demand_destruction", "ssd_price_reversal"),
        ("nand_cycle_reversal", "supply_rebound", "4b_crowding"),
        "AI storage NAND is split from general memory because shortage can be real, but cycle reversal and 4B crowding remain large.",
    ),
    Round81ScoreTarget(
        "COMMODITY_MEMORY_GENERAL_SEMI",
        E2RArchetype.COMMODITY_MEMORY_GENERAL_SEMI,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(22, 16, 16, 11, 8),
        ("dram_nand_price_rebound", "hbm_conversion_supply_squeeze", "memory_contract_price_up"),
        ("contract_price_up", "inventory_normalization", "op_eps_revision", "supply_discipline"),
        ("multi_quarter_revision", "supply_discipline", "old_memory_cycle_frame_shift"),
        ("memory_cycle_crowded", "stock_multiple_expansion", "spot_price_fully_priced"),
        ("supply_rebound", "contract_price_decline", "customer_capex_cut", "inventory_build"),
        ("op_eps_revision", "supply_discipline", "ai_storage_demand"),
        ("cycle_reversal", "supply_rebound", "spot_price_reversal"),
        ("nand_dram_cycle_reversal", "supply_rebound"),
        "General DRAM/NAND stays Watch-to-Green; AI storage NAND now has its own target, so cycle penalty remains higher here.",
    ),
    Round81ScoreTarget(
        "SEMI_EQUIPMENT_AI_CAPEX",
        E2RArchetype.SEMI_EQUIPMENT_AI_CAPEX,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(22, 20, 18, 14, 11),
        ("wfe_capex", "hbm_fab_capex", "advanced_node_capex", "packaging_tool_keyword"),
        ("equipment_order_growth", "guidance_raise", "backlog_growth", "customer_capex_budget"),
        ("order_to_revenue_conversion", "op_eps_revision", "customer_diversification", "margin_visible"),
        ("equipment_capex_crowded", "customer_capex_peak", "order_growth_slowdown"),
        ("order_pushout", "export_control", "customer_capex_cut", "inventory_build"),
        ("orders", "revenue_conversion", "op_eps_revision", "customer_capex"),
        ("order_pushout", "export_control", "customer_capex_cut"),
        ("customer_capex_peak", "order_delay", "export_control"),
        "AI equipment CAPEX is Watch-to-Green because orders can convert into EPS, but customer CAPEX peak and order push-out can break the path quickly.",
    ),
    Round81ScoreTarget(
        "SEMI_MATERIALS_PROCESS",
        E2RArchetype.SEMI_MATERIALS_PROCESS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(20, 18, 14, 13, 11),
        ("process_material_keyword", "customer_qualification", "fab_ramp"),
        ("qualification_passed", "volume_ramp", "margin_visibility"),
        ("repeat_volume", "customer_diversification", "op_eps_revision"),
        ("qualification_crowded", "material_theme_fully_priced"),
        ("qualification_delay", "customer_capex_cut", "price_pressure"),
        ("qualification", "volume_ramp", "margin_visibility"),
        ("qualification_delay", "single_customer", "price_pressure"),
        ("qualification_delay", "customer_concentration", "price_pressure"),
        "Materials need qualification, repeat volume, and customer diversification before Green.",
    ),
    Round81ScoreTarget(
        "ADVANCED_PACKAGING_COWOS_EMIB",
        E2RArchetype.ADVANCED_PACKAGING_COWOS_EMIB,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(22, 21, 20, 14, 10),
        ("cowos_s_l", "emib", "interposer", "hbm_gpu_package_bottleneck"),
        ("packaging_order", "lead_time_extended", "capacity_shortage", "yield_progress"),
        ("packaging_revenue_growth", "op_eps_revision", "bottleneck_frame_confirmed"),
        ("cowos_capacity_fourfold", "packaging_consensus_crowded", "capacity_expansion"),
        ("bottleneck_easing", "yield_issue", "customer_capex_delay"),
        ("packaging_bottleneck", "revenue_growth", "op_eps_revision", "customer_visibility"),
        ("bottleneck_normalization", "yield_issue", "customer_capex_delay"),
        ("capacity_normalization", "yield", "capex_cycle"),
        "CoWoS/EMIB stays Green-capable when packaging bottleneck converts into revenue and EPS.",
    ),
    Round81ScoreTarget(
        "ADVANCED_PACKAGING_PCB",
        E2RArchetype.ADVANCED_PACKAGING_PCB,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(21, 21, 19, 13, 10),
        ("ai_server_pcb", "high_layer_pcb", "optical_transceiver_pcb", "glass_substrate_keyword"),
        ("pcb_lead_time_extended", "order_visibility", "capacity_constraint", "op_eps_revision"),
        ("pcb_revenue_conversion", "pricing_power", "customer_diversification"),
        ("pcb_theme_crowded", "new_capacity", "lead_time_normalization"),
        ("inventory_build", "customer_order_delay", "yield_issue", "theme_without_order"),
        ("order_visibility", "capacity_constraint", "op_eps_revision", "pricing_power"),
        ("theme_without_revenue", "lead_time_normalization", "inventory_build"),
        ("lead_time_normalization", "customer_concentration", "inventory"),
        "AI server PCB can be strong, but glass/CXL substrate keywords are not revenue evidence by themselves.",
    ),
    Round81ScoreTarget(
        "OPTICAL_NETWORKING_AI_DATACENTER",
        E2RArchetype.OPTICAL_NETWORKING_AI_DATACENTER,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(22, 22, 21, 13, 11),
        ("800g_1_6t_transceiver", "laser_supply_constraint", "silicon_photonics", "ai_datacenter_network"),
        ("hyperscaler_contract", "lead_time_6_weeks_to_6_months", "order_visibility"),
        ("long_term_contract", "op_eps_revision", "optical_bottleneck_confirmed"),
        ("optical_pcb_crowded", "new_capacity", "lead_time_normalization"),
        ("lead_time_normalization", "customer_capex_delay", "order_cancellation"),
        ("hyperscaler_contract", "lead_time_extended", "op_eps_revision", "capacity_constraint"),
        ("lead_time_normalization", "new_capacity", "customer_capex_delay"),
        ("lead_time_normalization", "customer_concentration", "valuation_crowding"),
        "Broadcom-style optical/PCB lead-time expansion strengthens this axis, but normalization is a 4B/4C field.",
    ),
    Round81ScoreTarget(
        "AI_SERVER_ODM_EMS_SUPPLY_CHAIN",
        E2RArchetype.AI_SERVER_ODM_EMS_SUPPLY_CHAIN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(22, 17, 14, 13, 8),
        ("ai_server_rack_demand", "odm_ems_keyword", "server_shipment_growth"),
        ("ai_server_revenue_mix", "rack_shipments", "capex_growth", "op_eps_revision"),
        ("ai_server_mix_changes_eps_fcf", "margin_stability", "customer_diversification", "working_capital_control"),
        ("ai_server_revenue_crowded", "inventory_growth", "low_margin_ignored"),
        ("accounting_issue", "auditor_resignation", "low_margin", "inventory_build", "customer_concentration"),
        ("ai_server_revenue_mix", "op_eps_revision", "margin_stability", "inventory_quality"),
        ("low_margin", "consignment_model", "inventory_growth", "accounting_issue", "customer_concentration"),
        ("low_margin", "consignment", "inventory", "accounting", "customer_concentration"),
        "Foxconn-style rack growth is real revenue evidence, but low margin and consignment economics limit Green.",
    ),
    Round81ScoreTarget(
        "NEOCLOUD_GPU_RENTAL",
        E2RArchetype.NEOCLOUD_GPU_RENTAL,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(18, 22, 18, 14, 7),
        ("large_gpu_cloud_contract", "take_or_pay_contract", "gpu_rental_revenue"),
        ("contract_backlog", "revenue_growth", "ebitda_improvement", "customer_contract"),
        ("fcf_conversion", "debt_to_ebitda_stable", "customer_diversification", "gpu_depreciation_control"),
        ("ai_cloud_valuation_overheat", "gpu_debt_multiple", "ipo_premium"),
        ("refinancing_pressure", "gpu_obsolescence", "customer_concentration", "fcf_negative", "delivery_issue"),
        ("take_or_pay_backlog", "fcf_conversion", "debt_stabilization", "customer_diversification"),
        ("high_debt", "fcf_negative", "gpu_depreciation", "customer_concentration", "delivery_issue"),
        ("high_debt", "gpu_depreciation", "fcf_negative", "refinancing", "customer_concentration"),
        "CoreWeave-like neocloud has contract visibility, but debt, FCF, depreciation, and concentration block Green.",
    ),
    Round81ScoreTarget(
        "AI_DATA_CENTER_COOLING",
        E2RArchetype.AI_DATA_CENTER_COOLING,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(21, 22, 22, 13, 10),
        ("liquid_cooling", "direct_to_chip", "immersion_cooling", "thermal_management"),
        ("strategic_cooling_customer", "cooling_revenue", "capacity_constraint", "mna_visibility"),
        ("order_to_revenue_conversion", "op_eps_revision", "service_revenue", "thermal_bottleneck_confirmed"),
        ("cooling_mna_valuation_crowded", "mna_multiple_expansion"),
        ("ai_capex_delay", "mna_overpay", "debt_financing", "eps_accretion_delay", "integration_risk"),
        ("data_center_customer", "thermal_bottleneck", "orders", "op_eps_revision"),
        ("mna_overpay", "debt_financing", "customer_capex_delay", "eps_accretion_delay"),
        ("mna_overpay", "debt", "ai_capex_delay"),
        "AI cooling is Green-capable, but CoolIT-style M&A price and EPS accretion timing need validation.",
    ),
    Round81ScoreTarget(
        "INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA",
        E2RArchetype.INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(19, 23, 13, 13, 12, 3),
        ("fab_gas_plant", "ultrahigh_purity_gas", "onsite_utility_contract"),
        ("long_term_gas_supply", "fab_ramp", "capacity_commitment"),
        ("utility_like_revenue_visibility", "margin_visible", "customer_contract_duration"),
        ("utility_contract_fully_priced",),
        ("fab_delay", "customer_capex_cut", "contract_margin_low", "energy_cost_spike"),
        ("long_term_supply", "contract_duration", "fab_ramp", "margin_visible"),
        ("fab_delay", "capex_cut", "low_margin_contract"),
        ("fab_delay", "customer_concentration", "energy_cost"),
        "Semiconductor gases are utility-like and need duration, fab ramp, and margin evidence.",
    ),
    Round81ScoreTarget(
        "AI_CHIP_FABRIC_INFRA",
        E2RArchetype.AI_CHIP_FABRIC_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(18, 15, 12, 14, 10),
        ("custom_asic", "tapeout", "foundry_yield", "domestic_ai_chip"),
        ("customer_validation", "mass_production_plan", "foundry_progress"),
        ("revenue_conversion", "gross_margin_visible", "repeat_customer"),
        ("ai_chip_theme_crowded", "mou_or_ipo_premium"),
        ("tapeout_delay", "yield_failure", "no_revenue", "customer_loss"),
        ("customer_validation", "mass_production", "revenue_conversion"),
        ("mou_only", "no_revenue", "yield_issue", "theme_only"),
        ("customer_validation_missing", "yield", "no_revenue"),
        "CXL, glass substrate, neuromorphic, and AI chip tags remain Watch/Red until adoption and revenue are real.",
    ),
    Round81ScoreTarget(
        "AI_ACCELERATOR_CHIP_PUREPLAY",
        E2RArchetype.AI_ACCELERATOR_CHIP_PUREPLAY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(17, 15, 13, 15, 7),
        ("ai_accelerator_ipo", "nvidia_competition_keyword", "wafer_scale_engine"),
        ("named_customer", "commercial_revenue", "gross_margin_visible"),
        ("repeat_customer", "software_ecosystem", "eps_or_fcf_path"),
        ("pureplay_valuation_overheat", "nvidia_competition_ignored"),
        ("customer_loss", "no_revenue", "valuation_compression", "funding_need"),
        ("named_customer", "commercial_revenue", "gross_margin_visible"),
        ("valuation_overheat", "no_revenue", "funding_need"),
        ("nvidia_competition", "valuation_overheat", "rd_burn"),
        "AI accelerator pure-play needs named customers, revenue, margin, and ecosystem before conviction.",
    ),
    Round81ScoreTarget(
        "DISPLAY_OLED_SUPPLYCHAIN",
        E2RArchetype.DISPLAY_OLED_SUPPLYCHAIN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(19, 18, 12, 13, 11),
        ("oled_capex", "display_customer_capex", "lcd_to_oled_shift"),
        ("panel_capex_order", "material_volume_ramp", "margin_visible"),
        ("multi_customer_oled_ramp", "op_eps_revision", "cycle_risk_controlled"),
        ("display_capex_crowded", "panel_capex_peak"),
        ("panel_capex_delay", "price_pressure", "customer_cut"),
        ("panel_capex_order", "volume_ramp", "margin_visible"),
        ("capex_cycle", "single_customer", "panel_delay"),
        ("capex_cycle", "price_competition", "customer_concentration"),
        "OLED stays cyclical Watch unless volume ramp, margin, and multiple customers are verified.",
    ),
    Round81ScoreTarget(
        "ELECTRONIC_COMPONENTS_MLCC_SENSOR",
        E2RArchetype.ELECTRONIC_COMPONENTS_MLCC_SENSOR,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(19, 17, 13, 12, 11, 1),
        ("mlcc_sensor_camera_keyword", "smartphone_parts_recovery", "content_growth"),
        ("customer_diversification", "content_per_device_growth", "margin_improvement"),
        ("recurring_component_growth", "op_eps_revision", "inventory_normalization"),
        ("component_cycle_crowded", "smartphone_recovery_fully_priced"),
        ("inventory_build", "customer_cut", "asp_pressure", "china_supply_chain_pressure"),
        ("content_growth", "customer_diversification", "margin_improvement"),
        ("inventory_build", "customer_cut", "asp_pressure"),
        ("inventory", "customer_concentration", "china_supply_chain"),
        "Components need inventory discipline and content/customer diversification, not only AI-adjacent keywords.",
    ),
    Round81ScoreTarget(
        "REDTEAM_ACCOUNTING_TRUST_OVERLAY",
        E2RArchetype.REDTEAM_ACCOUNTING_TRUST_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _weights("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("auditor_resignation", "filing_delay", "internal_control_issue", "related_party_transaction"),
        ("trust_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("auditor_resignation", "filing_delay", "internal_control_weakness", "doj_sec_investigation", "related_party_transaction"),
        (),
        ("auditor_resignation", "filing_delay", "internal_control_weakness", "doj_sec_investigation", "related_party_transaction"),
        ("auditor_resignation", "filing_delay", "internal_control_weakness"),
        "Supermicro-style accounting trust break is a hard 4C gate, not a score bucket.",
        hard_gate=True,
    ),
    Round81ScoreTarget(
        "AI_CAPEX_CROWDING_OVERLAY",
        E2RArchetype.AI_CAPEX_CROWDING_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _weights("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("ai_capex_consensus_crowded", "price_only_ai_rally", "universal_bullish_reports"),
        ("4b_watch_triggered",),
        ("not_applicable_overlay",),
        ("price_multiple_expansion", "revision_slowdown", "capacity_normalization", "hyperscaler_capex_peak"),
        ("customer_capex_cut", "order_pushout", "lead_time_normalization", "guidance_down"),
        (),
        ("revision_slowdown", "capacity_normalization", "customer_capex_cut", "order_pushout"),
        ("crowding", "capex_peak", "capacity_normalization", "revision_slowdown"),
        "AI CAPEX crowding is a 4B/4C overlay: it must warn, but not fabricate a positive Green score.",
    ),
)


ROUND81_CASE_CANDIDATES: tuple[Round81CaseCandidate, ...] = (
    Round81CaseCandidate(
        "sk_hynix_hbm_trillion_case",
        "MEMORY_HBM_CAPACITY",
        "000660",
        "SK하이닉스 HBM structural success plus 4B-watch",
        "KR",
        "structural_success",
        None,
        date(2026, 5, 14),
        date(2026, 5, 14),
        date(2026, 5, 14),
        None,
        ("hbm_demand", "market_cap_near_1t", "multi_year_eps_revision_candidate", "ai_memory_rerating"),
        ("4b_crowding", "capacity_normalization", "customer_price_resistance", "ai_capex_slowdown"),
        "hbm_structural_success_but_4b",
        "needs_price_backfill",
        ("round_81.md Reuters SK Hynix AI boom market value",),
        "HBM structure is valid, but the price path and broad recognition require 4B-watch at the same time.",
        (E2RArchetype.STRUCTURAL_SUCCESS_ALIGNED, E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH),
    ),
    Round81CaseCandidate(
        "samsung_hbm4_shipping_case",
        "HBM_CATCHUP_EXECUTION",
        "005930",
        "삼성전자 HBM4 catch-up shipping",
        "KR",
        "success_candidate",
        None,
        date(2026, 2, 12),
        None,
        None,
        None,
        ("hbm4_shipping_flag", "customer_sample_shipping", "hbm4e_sample_plan", "share_price_up_6_4pct"),
        ("qualification_status_unknown", "yield_signal_needed", "volume_shipment_needed"),
        "hbm_catchup_execution_candidate",
        "needs_price_backfill",
        ("round_81.md Reuters Samsung HBM4 shipment",),
        "Catch-up shipping can be Stage 2, but Green needs customer qualification, yield, and volume shipment evidence.",
    ),
    Round81CaseCandidate(
        "samsung_amd_hbm4_mou_case",
        "HBM_CATCHUP_EXECUTION",
        "005930",
        "삼성전자-AMD HBM4 / foundry MOU",
        "KR",
        "success_candidate",
        None,
        date(2026, 3, 18),
        None,
        None,
        None,
        ("amd_supply_chain_flag", "hbm4_mou", "foundry_partnership_candidate", "customer_specific_base_die_flag"),
        ("mou_only", "qualification_status_unknown", "yield_signal_needed", "volume_shipment_needed"),
        "hbm_catchup_execution_candidate",
        "needs_price_backfill",
        ("round_81.md Reuters Samsung AMD AI memory MOU",),
        "AMD HBM4 and foundry MOU can support catch-up visibility, but MOU is not volume shipment or margin evidence.",
        (E2RArchetype.MEMORY_HBM_CAPACITY,),
    ),
    Round81CaseCandidate(
        "samsung_labor_strike_execution_case",
        "HBM_CATCHUP_EXECUTION",
        "005930",
        "삼성전자 labor/execution RedTeam",
        "KR",
        "failed_rerating",
        None,
        date(2026, 5, 15),
        None,
        None,
        None,
        ("ai_memory_recovery", "one_stop_semiconductor_strategy"),
        ("labor_strike", "production_disruption", "execution_risk", "foundry_yield_risk", "talent_retention_risk"),
        "execution_labor_redteam",
        "needs_price_backfill",
        ("round_81.md Reuters Samsung labor strike plan",),
        "Even a memory catch-up story can be blocked by labor, execution, foundry yield, or talent retention risk.",
        (E2RArchetype.OPERATIONAL_TRUST_BREAK,),
    ),
    Round81CaseCandidate(
        "kioxia_ai_nand_profit_case",
        "AI_STORAGE_NAND_SHORTAGE",
        "285A.T",
        "Kioxia AI NAND profit explosion",
        "JP",
        "4b_watch",
        None,
        date(2026, 5, 15),
        None,
        date(2026, 5, 15),
        None,
        ("nand_profit_growth", "ai_storage_demand", "stock_multiple_expansion", "commodity_memory_to_ai_storage"),
        ("cycle_reversal", "supply_rebound", "stock_up_20x", "memory_price_reversal"),
        "commodity_memory_ai_storage_success_plus_4b",
        "needs_price_backfill",
        ("round_81.md Reuters Kioxia AI profit", "round_81.md FT Kioxia profit surge"),
        "AI storage can make NAND look structural for a time, but a 20x stock path needs 4B/cycle reversal review.",
        (E2RArchetype.CYCLICAL_SUCCESS, E2RArchetype.CROWDED_RERATING_4B_WATCH),
    ),
    Round81CaseCandidate(
        "applied_materials_ai_packaging_growth_case",
        "SEMI_EQUIPMENT_AI_CAPEX",
        "AMAT",
        "Applied Materials AI packaging growth",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 14),
        None,
        None,
        None,
        ("guidance_raise", "semiconductor_equipment_growth", "packaging_revenue_growth_over_50pct", "after_hours_price_up_3pct"),
        ("customer_capex_peak", "order_pushout", "export_control"),
        "semi_capex_aligned",
        "needs_price_backfill",
        ("round_81.md Reuters Applied Materials guidance",),
        "AI CAPEX is visible in equipment and packaging guidance, but CAPEX-cycle risk still keeps it Watch-to-Green.",
        (E2RArchetype.ADVANCED_PACKAGING_COWOS_EMIB,),
    ),
    Round81CaseCandidate(
        "nvidia_cowos_l_transition_case",
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
        ("cowos_l_flag", "advanced_packaging_bottleneck", "cowos_capacity_fourfold", "capacity_still_bottleneck"),
        ("bottleneck_normalization", "yield_issue", "capacity_expansion"),
        "packaging_bottleneck_aligned",
        "needs_price_backfill",
        ("round_81.md Reuters Nvidia CoWoS-L reference",),
        "CoWoS capacity expanded sharply but remains a bottleneck; both facts must be tracked together.",
    ),
    Round81CaseCandidate(
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
        ("optical_transceiver_order", "pcb_lead_time_6_weeks_to_6_months", "laser_supply_constraint", "tsmc_capacity_bottleneck"),
        ("lead_time_normalization", "new_capacity", "hyperscaler_capex_delay", "customer_concentration"),
        "optical_pcb_bottleneck_aligned",
        "needs_price_backfill",
        ("round_81.md Reuters Broadcom supply constraints",),
        "Optical networking/PCB bottleneck becomes stronger in Loop 4 because lead time expanded from weeks to months.",
        (E2RArchetype.ADVANCED_PACKAGING_PCB,),
    ),
    Round81CaseCandidate(
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
        ("ai_server_rack_shipments_double", "q1_profit_up_19pct", "ai_server_capex_up_30pct"),
        ("consignment_model", "low_margin", "inventory_growth", "customer_concentration"),
        "ai_revenue_but_margin_watch",
        "needs_price_backfill",
        ("round_81.md Reuters Foxconn Q1 profit",),
        "AI server revenue and rack shipments can pass Stage 2, but margin and working-capital quality decide conviction.",
    ),
    Round81CaseCandidate(
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
        ("liquid_cooling_order", "nvidia_amd_exposure", "cooling_revenue_550m", "eps_accretion_2028"),
        ("mna_overpay", "mna_debt_financing", "eps_accretion_delay", "integration_risk"),
        "cooling_success_candidate_plus_mna_watch",
        "needs_price_backfill",
        ("round_81.md Reuters Ecolab CoolIT acquisition",),
        "Cooling can be a structural data-center bottleneck, but acquisition multiple and accretion timing remain RedTeam fields.",
    ),
    Round81CaseCandidate(
        "coreweave_openai_contract_case",
        "NEOCLOUD_GPU_RENTAL",
        "CRWV",
        "CoreWeave OpenAI contract with leverage risk",
        "US",
        "success_candidate",
        None,
        date(2025, 3, 10),
        None,
        None,
        None,
        ("openai_contract_11_9b", "take_or_pay_candidate", "gpu_cloud_revenue_growth"),
        ("microsoft_revenue_62pct", "debt_8b", "fcf_negative", "gpu_depreciation", "delivery_issue"),
        "contract_visibility_but_leverage_risk",
        "needs_price_backfill",
        ("round_81.md FT OpenAI CoreWeave contract",),
        "A huge AI cloud contract can be Stage 2 visibility, but FCF, debt, and customer concentration block Green.",
        (E2RArchetype.LEVERAGE_FCF_BREAKDOWN,),
    ),
    Round81CaseCandidate(
        "coreweave_expanded_openai_contract_case",
        "NEOCLOUD_GPU_RENTAL",
        "CRWV",
        "CoreWeave expanded OpenAI contract concentration watch",
        "US",
        "success_candidate",
        None,
        date(2025, 9, 25),
        None,
        None,
        None,
        ("openai_contract_expansion", "gpu_cloud_contract_value", "revenue_visibility", "take_or_pay_candidate"),
        ("customer_concentration", "debt_to_ebitda_risk", "gpu_depreciation", "refinancing_risk_flag"),
        "contract_visibility_but_customer_concentration_watch",
        "needs_price_backfill",
        ("round_81.md Reuters CoreWeave OpenAI expanded pact",),
        "Expanded OpenAI contract raises visibility, but customer concentration and GPU/debt economics still block Green.",
        (E2RArchetype.LEVERAGE_FCF_BREAKDOWN,),
    ),
    Round81CaseCandidate(
        "coreweave_downsized_ipo_debt_case",
        "NEOCLOUD_GPU_RENTAL",
        "CRWV",
        "CoreWeave downsized IPO debt watch",
        "US",
        "failed_rerating",
        None,
        date(2025, 3, 28),
        None,
        None,
        None,
        ("gpu_cloud_contracts", "revenue_growth"),
        ("ipo_downsize", "debt_8b", "net_loss_863m", "fcf_negative", "customer_concentration"),
        "neocloud_debt_fcf_customer_concentration",
        "needs_price_backfill",
        ("round_81.md Investopedia CoreWeave IPO pricing",),
        "Downsized IPO plus high debt shows why neocloud is high-risk Watch rather than HBM-like Green.",
        (E2RArchetype.LEVERAGE_FCF_BREAKDOWN,),
    ),
    Round81CaseCandidate(
        "cerebras_ai_accelerator_ipo_case",
        "AI_ACCELERATOR_CHIP_PUREPLAY",
        "CEREBRAS",
        "Cerebras AI accelerator IPO event premium",
        "US",
        "event_premium",
        date(2026, 5, 14),
        date(2026, 5, 14),
        None,
        None,
        None,
        ("ai_accelerator_ipo", "openai_customer_flag", "aws_customer_flag", "ipo_first_day_return", "inference_capacity_demand"),
        ("customer_concentration", "nvidia_competition_flag", "software_ecosystem_gap", "gross_margin_unverified", "ipo_valuation_overheat"),
        "ai_accelerator_ipo_event_premium",
        "needs_price_backfill",
        ("round_81.md WSJ Cerebras IPO",),
        "AI accelerator pure-play demand can be Stage 2 watch evidence, but IPO surge and ecosystem/customer risk keep it event premium.",
        (E2RArchetype.THEME_VALUATION_OVERHEAT,),
    ),
    Round81CaseCandidate(
        "supermicro_ey_resignation_case",
        "REDTEAM_ACCOUNTING_TRUST_OVERLAY",
        "SMCI",
        "Supermicro EY resignation accounting break",
        "US",
        "4c_thesis_break",
        date(2023, 1, 1),
        None,
        None,
        None,
        date(2024, 10, 30),
        ("ai_server_revenue_rerating", "ai_server_growth"),
        ("auditor_resignation", "filing_delay", "internal_control_issue", "hindenburg_accounting_claim", "doj_sec_investigation"),
        "accounting_trust_break_4c",
        "needs_price_backfill",
        ("round_81.md Reuters Supermicro EY resignation",),
        "AI server growth cannot overcome auditor resignation, filing delay, or internal-control trust break.",
        (E2RArchetype.AI_SERVER_ODM_EMS_SUPPLY_CHAIN, E2RArchetype.THESIS_BREAK_4C),
    ),
    Round81CaseCandidate(
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
        ("theme_only_flag", "actual_revenue_missing", "customer_validation_missing", "mass_production_missing"),
        "theme_without_revenue",
        "missing_price_data",
        ("round_81.md CXL/glass substrate guardrail",),
        "CXL, glass substrate, and neuromorphic tags remain Watch/Red until adoption, validation, production, and revenue exist.",
        (E2RArchetype.THEME_VALUATION_OVERHEAT,),
    ),
    Round81CaseCandidate(
        "furiosa_ai_related_stock_case",
        "AI_ACCELERATOR_CHIP_PUREPLAY",
        "FURIOSA_RELATED",
        "퓨리오사AI related stock watch",
        "KR",
        "overheat",
        None,
        None,
        None,
        None,
        None,
        ("ai_chip_keyword", "domestic_ai_chip_theme"),
        ("theme_only_flag", "customer_validation_missing", "tapeout_missing", "actual_revenue_missing"),
        "theme_without_revenue",
        "missing_price_data",
        ("round_81.md FuriosaAI related stock watch",),
        "Related-stock exposure is not evidence. Customer validation, tape-out, mass production, and revenue must come first.",
        (E2RArchetype.THEME_VALUATION_OVERHEAT,),
    ),
    Round81CaseCandidate(
        "ai_capex_crowding_overlay_case",
        "AI_CAPEX_CROWDING_OVERLAY",
        "AI_CAPEX_OVERLAY",
        "AI CAPEX crowding overlay",
        "GLOBAL",
        "4b_watch",
        None,
        None,
        None,
        None,
        None,
        ("ai_capex_consensus_crowded", "universal_bullish_reports", "price_multiple_expansion"),
        ("revision_slowdown", "capacity_normalization", "customer_capex_cut", "order_pushout"),
        "ai_capex_crowding_4b_overlay",
        "missing_price_data",
        ("round_81.md AI CAPEX crowding overlay",),
        "Crowded AI CAPEX evidence is a 4B warning overlay and must not create positive Green score by itself.",
        (E2RArchetype.CROWDED_RERATING_4B_WATCH,),
    ),
)


ROUND81_PRICE_FIELDS: tuple[str, ...] = (
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
    "hbm4_shipping_flag",
    "hbm4_yield_signal",
    "qualification_status",
    "volume_shipment_flag",
    "customer_specific_base_die_flag",
    "memory_spot_price_change",
    "memory_contract_price_change",
    "dram_nand_mix",
    "nand_profit_growth",
    "enterprise_ssd_revenue",
    "ssd_price_change",
    "commodity_memory_supply_rebound_flag",
    "consumer_demand_destruction_flag",
    "equipment_order_growth",
    "equipment_backlog",
    "customer_capex_growth",
    "customer_forecast_duration_quarters",
    "order_pushout_flag",
    "export_control_flag",
    "packaging_revenue_growth",
    "cowos_capacity_growth",
    "cowos_l_flag",
    "cowos_s_flag",
    "emib_revenue_flag",
    "interposer_supply_constraint_flag",
    "yield_issue_flag",
    "bottleneck_normalization_flag",
    "pcb_lead_time_weeks",
    "optical_transceiver_order",
    "laser_supply_constraint_flag",
    "hyperscaler_contract_flag",
    "silicon_photonics_revenue",
    "optical_networking_inventory_flag",
    "ai_server_revenue",
    "ai_server_rack_shipments",
    "ai_server_margin",
    "consignment_model_flag",
    "inventory_growth",
    "customer_concentration",
    "working_capital_pressure",
    "gpu_cloud_revenue",
    "gpu_cloud_contract_value",
    "take_or_pay_flag",
    "debt_to_ebitda",
    "net_debt",
    "fcf_margin",
    "gpu_depreciation",
    "refinancing_risk_flag",
    "delivery_issue_flag",
    "ipo_downsize_flag",
    "cooling_revenue",
    "liquid_cooling_order",
    "mna_price",
    "mna_multiple",
    "mna_debt_financing_flag",
    "eps_accretion_year",
    "integration_risk_flag",
    "ai_accelerator_revenue",
    "ai_accelerator_customer_count",
    "openai_customer_flag",
    "aws_customer_flag",
    "gross_margin",
    "software_ecosystem_score",
    "repeat_order_flag",
    "nvidia_competition_flag",
    "ipo_first_day_return",
    "auditor_resignation_flag",
    "filing_delay_flag",
    "internal_control_issue_flag",
    "regulatory_probe_flag",
    "related_party_risk_flag",
    "labor_strike_flag",
    "production_disruption_flag",
    "execution_risk_flag",
    "foundry_yield_risk_flag",
    "talent_retention_risk_flag",
    "theme_only_flag",
    "actual_revenue_flag",
    "customer_validation_flag",
    "tapeout_flag",
    "mass_production_flag",
    "direct_equity_exposure_flag",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def round81_target_for(target_id: str) -> Round81ScoreTarget | None:
    for target in ROUND81_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round81_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND81_CASE_CANDIDATES:
        target = round81_target_for(candidate.target_id)
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
                f"Round81 R2 Loop-4 case for {candidate.target_id}; "
                "AI beneficiary tags are split by economic structure and remain calibration-only."
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
                "ai_beneficiary_is_not_one_archetype",
                "do_not_invent_contract_prices_margins_customers_stage_prices_or_yield",
                "accounting_trust_is_hard_gate",
                "neocloud_debt_fcf_customer_concentration_blocks_green",
                "theme_without_revenue_blocks_green",
                "price_only_ai_capex_crowding_is_4b_overlay_not_green",
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


def round81_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND81_SCORE_TARGETS:
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
                "hard_gate": str(target.hard_gate).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round81_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND81_CASE_CANDIDATES:
        target = round81_target_for(candidate.target_id)
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


def round81_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "loop4_penalty_axes": "|".join(target.loop4_penalty_axes),
            "hard_gate": str(target.hard_gate).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND81_SCORE_TARGETS
    )


def round81_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round81_backfill": "true"} for field in ROUND81_PRICE_FIELDS)


def round81_summary() -> dict[str, int | bool]:
    records = round81_case_records()
    return {
        "target_count": len(ROUND81_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND81_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND81_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND81_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "hard_gate_target_count": sum(1 for target in ROUND81_SCORE_TARGETS if target.hard_gate),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round81_r2_loop4_reports(
    *,
    output_directory: str | Path = ROUND81_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND81_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND81_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round81_r2_loop4_ai_semiconductor_summary.md",
        "case_matrix": output / "round81_r2_loop4_case_matrix.csv",
        "stage_date_plan": output / "round81_r2_loop4_stage_date_plan.csv",
        "green_guardrails": output / "round81_r2_loop4_green_guardrails.md",
        "loop4_risk_overlays": output / "round81_r2_loop4_risk_overlays.md",
        "price_validation_plan": output / "round81_r2_loop4_price_validation_plan.md",
        "price_fields": output / "round81_r2_loop4_price_fields.csv",
    }
    _write_case_jsonl(round81_case_records(), cases)
    _write_rows(round81_score_profile_rows(), score_profiles)
    _write_rows(round81_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round81_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round81_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round81_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round81_green_guardrail_markdown(), encoding="utf-8")
    paths["loop4_risk_overlays"].write_text(render_round81_loop4_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round81_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round81_summary_markdown() -> str:
    summary = round81_summary()
    lines = [
        "# Round-81 R2 Loop-4 AI / Semiconductor / Electronics Summary",
        "",
        f"- source_round: `{ROUND81_SOURCE_ROUND_PATH}`",
        "- large_sector: `AI_SEMICONDUCTOR_ELECTRONICS`",
        "- loop: `R2 Loop 4 / v4.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- overheat_count: {summary['overheat_count']}",
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
        "- R2 Loop 4 says `AI 수혜` is not a score bucket.",
        "- Example: HBM can be structural, but SK하이닉스-like success can also be 4B-watch after rerating.",
        "- Example: Samsung/Micron-style HBM catch-up is separate from HBM leadership because qualification, yield, and volume are still execution gates.",
        "- Example: Kioxia-style AI storage NAND can show profit explosion, but 10x-20x price paths and NAND supply rebound require 4B/cycle review.",
        "- Example: Foxconn-style AI server rack growth is revenue evidence, but low margin and consignment economics still matter.",
        "- Example: CoreWeave-style contract visibility is not Green until debt, FCF, depreciation, and customer concentration pass.",
        "- Example: Supermicro-style auditor resignation is a hard accounting trust break even if AI server revenue was strong.",
    ]
    return "\n".join(lines) + "\n"


def render_round81_green_guardrail_markdown() -> str:
    lines = [
        "# Round-81 R2 Loop-4 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-4 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND81_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions) or 'not_applicable'} | {', '.join(target.loop4_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R2 Loop-4 v4.0 weights to production scoring yet.",
            "- Do not treat all AI beneficiaries as one archetype.",
            "- Do not make CXL, glass substrate, neuromorphic, or AI chip related-stock keywords Green evidence without revenue.",
            "- Do not invent contract value, customer name, duration, prepayment, HBM yield, margin, stage price, or FCF.",
            "- Treat accounting trust break as hard 4C; treat AI CAPEX crowding as a 4B overlay, not a positive score.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round81_loop4_risk_overlay_markdown() -> str:
    lines = [
        "# Round-81 R2 Loop-4 Risk Overlays",
        "",
        "- `HBM_STRUCTURAL_SUCCESS_BUT_4B`: HBM is structurally right, but broad recognition and price path require 4B-watch.",
        "- `HBM_CATCHUP_EXECUTION_CANDIDATE`: catch-up shipment is Stage 2 only until qualification, yield, and volume are proven.",
        "- `AI_STORAGE_NAND_SUCCESS_BUT_4B`: NAND/enterprise SSD can benefit from AI storage, but 4B crowding and supply rebound remain central.",
        "- `OPTICAL_PCB_BOTTLENECK_ALIGNED`: optical/PCB lead time and orders matter, but lead-time normalization is a 4B/4C field.",
        "- `AI_REVENUE_BUT_MARGIN_WATCH`: AI server revenue grows, but margin, consignment, inventory, and customer concentration limit Green.",
        "- `CONTRACT_VISIBILITY_BUT_LEVERAGE_RISK`: neocloud contracts improve visibility, but debt, FCF, GPU depreciation, and concentration can block Green.",
        "- `AI_ACCELERATOR_IPO_EVENT_PREMIUM`: AI accelerator IPO demand is not Green until repeat orders, gross margin, ecosystem, and FCF are visible.",
        "- `ACCOUNTING_TRUST_BREAK_4C`: auditor resignation, filing delay, internal control, or regulatory probe breaks the thesis.",
        "- `THEME_WITHOUT_REVENUE`: CXL, glass substrate, AI chip, or neuromorphic theme has no customer validation or revenue.",
        "",
        "Simple example: `OpenAI contract` can support Stage 2 visibility for a GPU cloud. It is not Green if debt and FCF are still unresolved.",
    ]
    return "\n".join(lines) + "\n"


def render_round81_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-81 R2 Loop-4 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare EPS revision, guidance, backlog, margin, customer concentration, accounting flags, and price path.",
        "6. Mark HBM 4B, commodity-memory cycle reversal, neocloud leverage, accounting trust break, and theme-only AI explicitly.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round81_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `hbm_structural_success_but_4b`: HBM evidence and price path align, but rerating may already be crowded.",
            "- `ai_revenue_but_margin_watch`: AI server revenue grows but margin and working capital remain unproven.",
            "- `contract_visibility_but_leverage_risk`: contract visibility exists but leverage and FCF block Green.",
            "- `theme_without_revenue`: technical theme has no customer validation, yield, production, or revenue.",
            "- `accounting_trust_break_4c`: trust evidence breaks the Stage 3 thesis.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round81CaseCandidate) -> str:
    if "theme_without_revenue" in candidate.alignment_hint:
        return "price_moved_without_evidence"
    if candidate.case_type == "event_premium":
        return "price_moved_without_evidence"
    if candidate.case_type in {"structural_success", "success_candidate"}:
        if "leverage" in candidate.alignment_hint or "margin_watch" in candidate.alignment_hint:
            return "evidence_good_but_price_failed"
        return "aligned"
    if candidate.case_type == "4b_watch":
        return "price_moved_without_evidence"
    if "debt" in candidate.alignment_hint or "execution" in candidate.alignment_hint or "labor" in candidate.alignment_hint:
        return "evidence_good_but_price_failed"
    return "false_positive_score"


def _rerating_result(candidate: Round81CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type in {"overheat", "4b_watch"}:
        return "theme_overheat"
    if candidate.case_type == "event_premium":
        return "event_premium"
    return "unknown" if candidate.case_type == "success_candidate" else "no_rerating"


def _score_weight_hint(target: Round81ScoreTarget) -> dict[str, float]:
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
