"""Round-121 R2 Loop-7 AI, semiconductor, and electronics pack.

Round 121 returns to R2 after the R1 Loop-7 pass. It separates HBM leaders,
HBM LTA/prepayment, HBM catch-up execution, memory supply reallocation,
AI storage NAND, AI equipment CAPEX, custom AI ASICs, advanced packaging,
AI networking, photonics, server ODM, neocloud, cooling, AI accelerator
pure-plays, circular financing, and accounting trust overlays.

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


ROUND121_SOURCE_ROUND_PATH = "docs/round/round_121.md"
ROUND121_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round121_r2_loop7_ai_semiconductor"
ROUND121_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop7_round121.jsonl"
ROUND121_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round121_r2_loop7_v7.csv"


@dataclass(frozen=True)
class Round121ScoreWeightDraft:
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
class Round121ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round121ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop7_penalty_axes: tuple[str, ...]
    normalization_point: str
    hard_gate: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round121CaseCandidate:
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


@dataclass(frozen=True)
class Round121BaseScoreWeight:
    component: str
    points: int
    loop7_direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {
            "component": self.component,
            "points": str(self.points),
            "loop7_direction": self.loop7_direction,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class Round121StageCap:
    stage_band: str
    max_score: str
    required_evidence: tuple[str, ...]
    example_cases: tuple[str, ...]
    green_policy: str

    def as_row(self) -> dict[str, str]:
        return {
            "stage_band": self.stage_band,
            "max_score": self.max_score,
            "required_evidence": "|".join(self.required_evidence),
            "example_cases": "|".join(self.example_cases),
            "green_policy": self.green_policy,
        }


@dataclass(frozen=True)
class Round121ScoreStagePriceAlignment:
    case_id: str
    detected_stage: str
    price_path_status: str
    verdict: str
    normalization_adjustment: str

    def as_row(self) -> dict[str, str]:
        return {
            "case_id": self.case_id,
            "detected_stage": self.detected_stage,
            "price_path_status": self.price_path_status,
            "verdict": self.verdict,
            "normalization_adjustment": self.normalization_adjustment,
        }


def _weights(
    eps_fcf: int | str,
    visibility: int | str,
    bottleneck: int | str,
    mispricing: int | str,
    valuation: int | str,
    capital: int | str = 0,
    confidence: int | str = 5,
) -> Round121ScoreWeightDraft:
    return Round121ScoreWeightDraft(eps_fcf, visibility, bottleneck, mispricing, valuation, capital, confidence)


ROUND121_BASE_SCORE_WEIGHTS: tuple[Round121BaseScoreWeight, ...] = (
    Round121BaseScoreWeight("eps_fcf_revision", 25, "up", "SK Hynix, Applied Materials, and Broadcom show price paths follow OP/EPS/FCF evidence."),
    Round121BaseScoreWeight("customer_shipment_revenue_visibility", 22, "up", "Customer names, shipments, AI orders, and guidance create Stage 2 signal."),
    Round121BaseScoreWeight("bottleneck_pricing_power", 19, "hold_up", "HBM, NAND, TSMC capacity, optical PCB, and photonics bottlenecks still matter."),
    Round121BaseScoreWeight("market_mispricing_gap", 12, "hold", "The old memory/cyclical or generic server frame must still be wrong."),
    Round121BaseScoreWeight("valuation_room_4b_runway", 8, "cap_after_rerating", "SK Hynix, Kioxia, and IPO cases show good structures can already be 4B."),
    Round121BaseScoreWeight("capital_discipline_fcf_stability", 6, "up", "CoreWeave, Cerebras, and Ecolab-CoolIT make FCF, debt, and M&A price central."),
    Round121BaseScoreWeight("information_confidence_disclosure_detail", 8, "up", "Supermicro and list-only AI disclosures require accounting, customer, amount, period, and parser confidence checks."),
)


ROUND121_STAGE_CAPS: tuple[Round121StageCap, ...] = (
    Round121StageCap(
        "Stage 1",
        "45",
        ("ai_hbm_custom_asic_cxl_glass_theme", "narrative_without_customer_contract_shipment_revenue"),
        ("cxl_glass_substrate_theme_case", "furiosa_ai_related_stock_case"),
        "Green blocked until customer, shipment, revenue, or guidance evidence exists.",
    ),
    Round121StageCap(
        "Stage 2",
        "70",
        ("customer_name", "shipment", "contract", "revenue_guidance", "ai_order_or_deal_amount"),
        ("samsung_hbm4_shipping_case", "tower_photonics_ai_datacenter_deal_case", "cisco_ai_networking_orders_case"),
        "Green blocked until OP/EPS/FCF, margin, and price-path alignment confirm.",
    ),
    Round121StageCap(
        "Stage 3",
        "100",
        ("op_eps_fcf_revision", "margin_or_capital_return", "price_path_alignment", "cross_evidence"),
        ("sk_hynix_record_profit_buyback_case", "applied_materials_ai_packaging_growth_case", "broadcom_custom_ai_asic_100b_case"),
        "Green possible only before 4B saturation and without RedTeam hard gates.",
    ),
    Round121StageCap(
        "Stage 4B",
        "monitoring",
        ("large_rerating", "valuation_saturation", "crowded_ai_consensus", "price_outruns_new_evidence"),
        ("sk_hynix_hbm_trillion_case", "kioxia_ai_nand_profit_case", "cerebras_ai_accelerator_ipo_case"),
        "A correct AI structure can become a monitoring case when price has already rerated heavily.",
    ),
    Round121StageCap(
        "Stage 4C",
        "hard_gate",
        ("auditor_resignation", "filing_delay", "circular_financing", "fcf_negative_high_debt", "labor_or_production_disruption"),
        ("supermicro_ey_resignation_case", "coreweave_nvidia_circular_financing_case", "samsung_labor_strike_execution_case"),
        "Hard RedTeam overrides AI growth narratives.",
    ),
)


ROUND121_SCORE_STAGE_PRICE_ALIGNMENT: tuple[Round121ScoreStagePriceAlignment, ...] = (
    Round121ScoreStagePriceAlignment(
        "sk_hynix_hbm_trillion_case",
        "Stage 3 -> 4B-watch",
        "Q4 reaction and multi-year rerating are cited in round note; full OHLCV backfill still required",
        "score_to_stage_to_price_aligned_but_4b",
        "raise HBM EPS/FCF and bottleneck credit, but cut valuation room after large rerating",
    ),
    Round121ScoreStagePriceAlignment(
        "samsung_hbm4_shipping_case",
        "Stage 2",
        "HBM4 shipment price reaction aligned with Stage 2, not Stage 3",
        "stage2_detection_aligned",
        "raise catch-up visibility but require qualification, yield, volume shipment, and EPS conversion",
    ),
    Round121ScoreStagePriceAlignment(
        "applied_materials_ai_packaging_growth_case",
        "Stage 2 -> Stage 3 candidate",
        "Guidance beats and price reactions support equipment Stage 2/3 calibration",
        "stage_detection_price_aligned",
        "raise equipment EPS/visibility while preserving order-pushout and export-control overlays",
    ),
    Round121ScoreStagePriceAlignment(
        "broadcom_custom_ai_asic_100b_case",
        "Stage 2 -> Stage 3 candidate",
        "AI revenue guide and supply bottleneck evidence aligned with price reaction",
        "custom_asic_independent_archetype_confirmed",
        "promote custom ASIC as its own axis; keep margin, customer, startup-credit, and capacity risks",
    ),
    Round121ScoreStagePriceAlignment(
        "cisco_ai_networking_orders_case",
        "Stage 2 -> Stage 3 candidate",
        "AI infrastructure and switching orders aligned with price reaction",
        "networking_stage_detection_aligned",
        "raise AI networking visibility, but require margin, FCF, and repeat order conversion",
    ),
    Round121ScoreStagePriceAlignment(
        "tower_photonics_ai_datacenter_deal_case",
        "Stage 2",
        "Photonic AI data-center deal amount supported Stage 2 price reaction",
        "photonics_stage2_aligned",
        "raise photonics deal visibility, but require delivery, revenue recognition, and margin before Green",
    ),
    Round121ScoreStagePriceAlignment(
        "foxconn_ai_server_rack_growth_case",
        "Stage 2",
        "AI server revenue/profit evidence works, but ODM margin power remains capped",
        "revenue_aligned_margin_capped",
        "keep server ODM revenue credit while lowering bottleneck/pricing score",
    ),
    Round121ScoreStagePriceAlignment(
        "kioxia_ai_nand_profit_case",
        "Stage 3 -> 4B-watch",
        "Profit guidance validates AI storage NAND, but 20x stock move is 4B-heavy",
        "structure_aligned_valuation_crowded",
        "raise NAND EPS evidence and sharply reduce valuation/mispricing after large price path",
    ),
    Round121ScoreStagePriceAlignment(
        "supermicro_ey_resignation_case",
        "Stage 4C",
        "Auditor resignation matched severe negative price reaction in round note",
        "redteam_hard_gate_aligned",
        "strengthen accounting trust hard gate across AI server and adjacent names",
    ),
    Round121ScoreStagePriceAlignment(
        "coreweave_nvidia_circular_financing_case",
        "Stage 2 visibility + 4B/4C-watch",
        "Contract visibility is not clean demand when supplier/customer/investor loops exist",
        "green_block_correct",
        "lower capital/FCF score and require clean FCF, leverage, utilization, and customer diversification",
    ),
    Round121ScoreStagePriceAlignment(
        "cerebras_ai_accelerator_ipo_case",
        "IPO event premium / 4B-watch",
        "First-day surge and next-day decline fit event-premium rather than structural Green",
        "valuation_watch_aligned",
        "cap pure-play accelerator valuation until repeat orders, margin, ecosystem, and FCF appear",
    ),
    Round121ScoreStagePriceAlignment(
        "ecolab_coolit_liquid_cooling_case",
        "Stage 2 M&A + valuation watch",
        "AI cooling deal still had negative price reaction due to M&A multiple/accretion delay",
        "mna_redteam_aligned",
        "penalize M&A overpay, debt financing, and delayed EPS accretion",
    ),
)


ROUND121_SCORE_TARGETS: tuple[Round121ScoreTarget, ...] = (
    Round121ScoreTarget(
        "MEMORY_HBM_CAPACITY",
        E2RArchetype.MEMORY_HBM_CAPACITY,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(25, 22, 20, 12, 6, 6, 8),
        ("hbm3e_hbm4_demand", "nvidia_supply_chain", "ai_memory_shortage"),
        ("hbm_revenue_share", "hbm_capacity_growth", "customer_allocation", "price_band_or_prepayment"),
        ("multi_year_eps_revision", "hbm_capacity_constraint", "lta_or_prepayment", "old_memory_frame_shift"),
        ("hbm_consensus_crowded", "market_cap_rerating_saturated", "customer_price_resistance"),
        ("ai_capex_slowdown", "capacity_oversupply", "hbm_price_decline", "customer_order_cut"),
        ("hbm_customer_visibility", "capacity_constraint", "multi_year_eps_revision", "price_band_or_prepayment"),
        ("customer_price_resistance", "capex_reversal", "capa_normalization", "memory_price_decline"),
        ("4b_crowding", "capacity_normalization", "customer_price_resistance"),
        "Loop 7 keeps HBM Green-capable, but valuation credit is reduced because successful HBM cases can already be 4B-watch.",
    ),
    Round121ScoreTarget(
        "MEMORY_HBM_LTA_PREPAYMENT",
        E2RArchetype.MEMORY_HBM_LTA_PREPAYMENT,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(25, 24, 20, 12, 8, 6, 8),
        ("hbm_supply_security", "lta_negotiation", "capacity_reservation_keyword", "customer_prepayment"),
        ("hbm_lta_flag", "hbm_price_band_flag", "prepayment_flag", "capacity_reservation_flag", "customer_name"),
        ("lta_revenue_conversion", "multi_year_eps_revision", "fcf_visibility", "capacity_locked_by_customer"),
        ("lta_prepayment_narrative_crowded", "hbm_market_share_fully_priced", "contract_visibility_over_extrapolated"),
        ("weak_binding_contract", "customer_order_cut", "price_band_down", "prepayment_absent", "capacity_reservation_cancelled"),
        ("hbm_lta_flag", "hbm_price_band_flag", "prepayment_flag", "capacity_reservation_flag", "multi_year_eps_revision"),
        ("weak_binding_contract", "prepayment_absent", "customer_order_cut", "price_band_down"),
        ("contract_binding_quality", "prepayment_quality", "capacity_reservation", "customer_concentration"),
        "Loop 7 splits HBM LTA/prepayment from general HBM because price bands, prepayment, and reserved capacity are stronger visibility than headlines.",
    ),
    Round121ScoreTarget(
        "HBM_CATCHUP_EXECUTION",
        E2RArchetype.HBM_CATCHUP_EXECUTION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(20, 20, 17, 12, 8, 3, 8),
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
    Round121ScoreTarget(
        "HBM_CATCHUP_EXECUTION_RISK",
        E2RArchetype.HBM_CATCHUP_EXECUTION_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        _weights("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("labor_strike", "bonus_gap", "production_disruption", "foundry_logic_execution_issue"),
        ("execution_risk_detected", "qualification_delay", "yield_shortfall"),
        ("not_applicable_overlay",),
        ("catchup_expectation_priced_before_volume", "execution_risk_ignored"),
        ("labor_strike", "production_disruption", "qualification_delay", "yield_shortfall", "talent_retention_risk"),
        (),
        ("labor_strike", "production_disruption", "qualification_delay", "yield_shortfall", "foundry_execution_issue"),
        ("labor", "yield", "production", "qualification"),
        "HBM catch-up can be Stage 2, but labor, yield, volume, and foundry execution risk must cap or block Stage 3.",
    ),
    Round121ScoreTarget(
        "MEMORY_SUPPLY_REALLOCATION",
        E2RArchetype.MEMORY_SUPPLY_REALLOCATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(21, 19, 17, 12, 8, 3, 8),
        ("consumer_memory_exit", "ai_customer_allocation", "memory_shortage", "capacity_reallocation"),
        ("consumer_memory_exit_flag", "strategic_customer_allocation_flag", "capacity_reallocation_flag", "dram_nand_mix"),
        ("ai_customer_mix_improves_opm", "supply_reallocation_to_hbm_or_enterprise", "multi_quarter_op_eps_revision"),
        ("supply_reallocation_story_crowded", "consumer_exit_read_as_clean_shortage"),
        ("consumer_demand_destruction", "ai_capex_slowdown", "hbm_supply_normalization", "memory_price_reversal"),
        ("strategic_customer_allocation_flag", "capacity_reallocation_flag", "op_eps_revision", "mix_improvement"),
        ("consumer_demand_destruction", "ai_capex_slowdown", "memory_price_reversal"),
        ("consumer_demand_destruction", "ai_capex_slowdown", "supply_normalization"),
        "Loop 7 separates supply reallocation from simple memory price rebound: consumer exit must become AI/HBM/enterprise mix and EPS evidence.",
    ),
    Round121ScoreTarget(
        "AI_STORAGE_NAND_SHORTAGE",
        E2RArchetype.AI_STORAGE_NAND_SHORTAGE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(25, 18, 19, 12, 4, 4, 8),
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
    Round121ScoreTarget(
        "COMMODITY_MEMORY_GENERAL_SEMI",
        E2RArchetype.COMMODITY_MEMORY_GENERAL_SEMI,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(21, 16, 16, 11, 7, 3, 8),
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
    Round121ScoreTarget(
        "SEMI_EQUIPMENT_AI_CAPEX",
        E2RArchetype.SEMI_EQUIPMENT_AI_CAPEX,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(24, 22, 19, 12, 8, 6, 8),
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
    Round121ScoreTarget(
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
    Round121ScoreTarget(
        "CUSTOM_AI_ASIC_HYPERSCALER",
        E2RArchetype.CUSTOM_AI_ASIC_HYPERSCALER,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(24, 22, 19, 12, 8, 4, 8),
        ("custom_ai_asic", "hyperscaler_custom_chip", "google_tpu", "meta_mtia", "openai_custom_accelerator"),
        ("custom_ai_asic_revenue", "hyperscaler_customer_name", "tsmc_capacity_secured_flag", "ai_chip_revenue"),
        ("repeat_custom_asic_revenue", "margin_visible", "customer_diversification", "fcf_conversion"),
        ("custom_asic_narrative_crowded", "single_customer_growth_extrapolated", "tsmc_capacity_fully_priced"),
        ("customer_project_delay", "custom_chip_margin_pressure", "startup_customer_credit_risk", "tsmc_capacity_miss"),
        ("named_hyperscaler_customer", "custom_ai_asic_revenue", "capacity_secured", "margin_visible"),
        ("customer_concentration", "custom_chip_margin_pressure", "startup_customer_risk_flag", "tsmc_capacity_miss"),
        ("customer_concentration", "margin", "startup_credit", "capacity"),
        "Loop 7 splits hyperscaler custom ASICs from generic AI chips because named customer, capacity, margin, and repeat revenue matter.",
    ),
    Round121ScoreTarget(
        "CUSTOM_AI_ASIC_MARGIN_CONCENTRATION",
        E2RArchetype.CUSTOM_AI_ASIC_MARGIN_CONCENTRATION,
        Round10ThemePosture.REDTEAM_FIRST,
        _weights("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("single_hyperscaler_dependency", "custom_chip_low_margin", "startup_customer_exposure", "asic_project_delay"),
        ("concentration_risk_detected", "custom_chip_margin_unverified", "customer_credit_risk_detected"),
        ("not_applicable_gate_only",),
        ("custom_ai_asic_visibility_overstated", "customer_concentration_ignored"),
        ("customer_project_delay", "customer_loss", "margin_miss", "startup_customer_default", "tsmc_capacity_loss"),
        (),
        ("customer_concentration", "custom_chip_margin_pressure", "startup_customer_risk_flag", "customer_project_delay"),
        ("customer_concentration", "margin", "startup_credit", "project_delay"),
        "Custom ASIC revenue is not HBM-like visibility if customer concentration, lower margin, or startup credit risk dominates.",
        hard_gate=True,
    ),
    Round121ScoreTarget(
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
    Round121ScoreTarget(
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
    Round121ScoreTarget(
        "OPTICAL_NETWORKING_AI_DATACENTER",
        E2RArchetype.OPTICAL_NETWORKING_AI_DATACENTER,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(22, 22, 20, 12, 8, 3, 8),
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
    Round121ScoreTarget(
        "AI_NETWORKING_SWITCHING_INFRA",
        E2RArchetype.AI_NETWORKING_SWITCHING_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(23, 22, 18, 12, 8, 6, 8),
        ("ai_datacenter_networking", "ethernet_ai_fabric", "hyperscaler_switching", "ai_infrastructure_orders"),
        ("ai_networking_orders", "hyperscaler_order_value", "data_center_switching_order_growth", "guidance_raise"),
        ("orders_to_recurring_revenue", "opm_conversion", "fcf_conversion", "customer_lock_in"),
        ("ai_networking_narrative_crowded", "switching_order_fully_priced", "legacy_drag_ignored"),
        ("hyperscaler_order_delay", "legacy_networking_drag", "restructuring_cost", "margin_miss"),
        ("ai_networking_orders", "guidance_raise", "opm_conversion", "fcf_conversion"),
        ("hyperscaler_concentration", "legacy_mix", "restructuring_cost", "order_delay"),
        ("hyperscaler_concentration", "legacy_mix", "restructuring", "order_delay"),
        "Cisco-style AI networking orders can support Stage 2, but orders must convert into margin, FCF, and repeat revenue before Green.",
    ),
    Round121ScoreTarget(
        "PHOTONICS_AI_DATACENTER_CHIPS",
        E2RArchetype.PHOTONICS_AI_DATACENTER_CHIPS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(20, 22, 19, 12, 8, 3, 8),
        ("silicon_photonics", "light_based_data_transfer", "ai_datacenter_interconnect", "photonics_chip_contract"),
        ("photonics_chip_contract_value", "photonics_delivery_year", "customer_name", "product_use_case"),
        ("revenue_recognition", "opm_conversion", "fcf_conversion", "customer_diversification"),
        ("photonics_theme_crowded", "contract_priced_before_delivery"),
        ("delivery_delay", "customer_cancellation", "yield_issue", "margin_miss"),
        ("contract_value", "delivery_schedule", "revenue_recognition", "margin_visible"),
        ("customer_concentration", "delivery_delay", "margin_unverified", "yield_issue"),
        ("customer_concentration", "delivery_delay", "yield", "margin_unverified"),
        "Tower-style photonics chip deals are Stage 2 when amount and delivery are known; Stage 3 needs revenue, margin, FCF, and customer diversity.",
    ),
    Round121ScoreTarget(
        "AI_SERVER_ODM_EMS_SUPPLY_CHAIN",
        E2RArchetype.AI_SERVER_ODM_EMS_SUPPLY_CHAIN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(22, 18, 12, 12, 7, 5, 8),
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
    Round121ScoreTarget(
        "NEOCLOUD_GPU_RENTAL",
        E2RArchetype.NEOCLOUD_GPU_RENTAL,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(16, 22, 15, 12, 4, 2, 8),
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
    Round121ScoreTarget(
        "AI_DATA_CENTER_COOLING",
        E2RArchetype.AI_DATA_CENTER_COOLING,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(20, 20, 18, 12, 6, 3, 8),
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
    Round121ScoreTarget(
        "AI_CHIP_FABRIC_INFRA",
        E2RArchetype.AI_CHIP_FABRIC_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(17, 14, 12, 14, 9),
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
    Round121ScoreTarget(
        "AI_ACCELERATOR_CHIP_PUREPLAY",
        E2RArchetype.AI_ACCELERATOR_CHIP_PUREPLAY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(14, 14, 10, 12, 3, 1, 8),
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
    Round121ScoreTarget(
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
    Round121ScoreTarget(
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
    Round121ScoreTarget(
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
    Round121ScoreTarget(
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
    Round121ScoreTarget(
        "CIRCULAR_AI_FINANCING_OVERLAY",
        E2RArchetype.CIRCULAR_AI_FINANCING_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _weights("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("supplier_equity_stake", "customer_equity_stake", "capacity_guarantee", "related_financing_loop"),
        ("circular_financing_detected", "capacity_purchase_guarantee", "equity_linked_customer_contract"),
        ("not_applicable_overlay",),
        ("valuation_ignores_circularity", "contract_visibility_overstated", "funding_loop_crowded"),
        ("capacity_guarantee_break", "refinancing_pressure", "customer_contract_loss", "supplier_support_withdrawal"),
        (),
        ("circular_financing", "capacity_guarantee_dependence", "customer_supplier_investor_overlap", "refinancing_pressure"),
        ("circular_financing", "capacity_guarantee", "refinancing", "customer_supplier_overlap"),
        "Neocloud circular financing is a RedTeam overlay: customer, supplier, and investor relationships must not be treated as clean demand evidence.",
        hard_gate=True,
    ),
    Round121ScoreTarget(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        _weights("cap", "cap", "cap", "cap", "cap", "cap", "+"),
        ("contract_headline", "facility_investment_headline", "rights_or_cb_headline", "correction_or_cancellation_headline"),
        ("detail_fetch_required", "contract_amount_missing", "customer_name_missing", "margin_missing"),
        ("not_applicable_cap_only",),
        ("list_only_disclosure_over_scored", "headline_contract_priced"),
        ("contract_cancelled", "contract_corrected", "dilution_detail_bad", "audit_or_trading_halt"),
        (),
        ("detail_missing", "amount_missing", "counterparty_missing", "duration_missing", "margin_missing"),
        ("detail_missing", "amount_missing", "counterparty_missing", "duration_missing", "margin_missing"),
        "OpenDART list-only or headline evidence caps Stage 3 until amount, counterparty, period, margin, and parser confidence are checked.",
    ),
)


ROUND121_CASE_CANDIDATES: tuple[Round121CaseCandidate, ...] = (
    Round121CaseCandidate(
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
        ("round_121.md Reuters SK Hynix AI boom market value",),
        "HBM structure is valid, but the price path and broad recognition require 4B-watch at the same time.",
        (E2RArchetype.STRUCTURAL_SUCCESS_ALIGNED, E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH),
    ),
    Round121CaseCandidate(
        "sk_hynix_record_profit_buyback_case",
        "MEMORY_HBM_LTA_PREPAYMENT",
        "000660",
        "SK하이닉스 record profit, HBM visibility, and capital return",
        "KR",
        "4b_watch",
        None,
        date(2026, 1, 28),
        None,
        date(2026, 1, 28),
        None,
        (
            "record_quarterly_profit",
            "hbm_demand",
            "explosive_memory_chip_demand",
            "buyback_cancel_amount",
            "capital_return_flag",
        ),
        (
            "4b_crowding",
            "hbm_market_share_fully_priced",
            "capacity_normalization",
            "customer_price_resistance",
        ),
        "hbm_eps_explosion_plus_capital_return_4b_watch",
        "needs_price_backfill",
        ("round_121.md Reuters SK Hynix record profit and buyback",),
        "Record HBM-led profit and capital return strengthen visibility, but the rerated price path still needs 4B-watch validation.",
        (E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH),
    ),
    Round121CaseCandidate(
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
        ("round_121.md Reuters Samsung HBM4 shipment",),
        "Catch-up shipping can be Stage 2, but Green needs customer qualification, yield, and volume shipment evidence.",
    ),
    Round121CaseCandidate(
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
        ("round_121.md Reuters Samsung AMD AI memory MOU",),
        "AMD HBM4 and foundry MOU can support catch-up visibility, but MOU is not volume shipment or margin evidence.",
        (E2RArchetype.MEMORY_HBM_CAPACITY,),
    ),
    Round121CaseCandidate(
        "samsung_labor_strike_execution_case",
        "HBM_CATCHUP_EXECUTION_RISK",
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
        ("round_121.md Reuters Samsung labor strike plan",),
        "Even a memory catch-up story can be blocked by labor, execution, foundry yield, or talent retention risk.",
        (E2RArchetype.OPERATIONAL_TRUST_BREAK,),
    ),
    Round121CaseCandidate(
        "micron_consumer_memory_exit_case",
        "MEMORY_SUPPLY_REALLOCATION",
        "MU",
        "Micron consumer memory exit and AI supply reallocation",
        "US",
        "success_candidate",
        None,
        date(2025, 12, 3),
        None,
        None,
        None,
        (
            "consumer_memory_exit_flag",
            "strategic_customer_allocation_flag",
            "capacity_reallocation_flag",
            "memory_shortage",
        ),
        (
            "consumer_demand_destruction_flag",
            "ai_capex_slowdown",
            "memory_price_reversal",
            "hbm_supply_normalization",
        ),
        "memory_supply_reallocation_aligned",
        "needs_price_backfill",
        ("round_121.md Reuters Micron consumer memory exit",),
        "Consumer memory exit can indicate AI/HBM allocation pressure, but it must convert into mix, OPM, and EPS evidence.",
        (E2RArchetype.COMMODITY_MEMORY_GENERAL_SEMI,),
    ),
    Round121CaseCandidate(
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
        ("round_121.md Reuters Kioxia AI profit", "round_121.md FT Kioxia profit surge"),
        "AI storage can make NAND look structural for a time, but a 20x stock path needs 4B/cycle reversal review.",
        (E2RArchetype.CYCLICAL_SUCCESS, E2RArchetype.CROWDED_RERATING_4B_WATCH),
    ),
    Round121CaseCandidate(
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
        ("round_121.md Reuters Applied Materials guidance",),
        "AI CAPEX is visible in equipment and packaging guidance, but CAPEX-cycle risk still keeps it Watch-to-Green.",
        (E2RArchetype.ADVANCED_PACKAGING_COWOS_EMIB,),
    ),
    Round121CaseCandidate(
        "broadcom_custom_ai_asic_100b_case",
        "CUSTOM_AI_ASIC_HYPERSCALER",
        "AVGO",
        "Broadcom custom AI ASIC hyperscaler demand",
        "US",
        "success_candidate",
        None,
        date(2026, 3, 4),
        None,
        None,
        None,
        (
            "custom_ai_asic_revenue",
            "hyperscaler_customer_name",
            "ai_chip_revenue",
            "tsmc_capacity_secured_flag",
            "ai_chip_sales_100b_by_2027",
        ),
        (
            "customer_concentration",
            "custom_chip_margin_pressure",
            "startup_customer_risk_flag",
            "tsmc_capacity_miss",
        ),
        "custom_ai_asic_aligned",
        "needs_price_backfill",
        ("round_121.md Reuters Broadcom custom AI chip demand",),
        "Hyperscaler custom ASIC revenue can be Stage 2 or better only when capacity, named customer, margin, and repeat revenue are visible.",
        (E2RArchetype.AI_CHIP_FABRIC_INFRA, E2RArchetype.OPTICAL_NETWORKING_AI_DATACENTER),
    ),
    Round121CaseCandidate(
        "broadcom_custom_ai_margin_concentration_case",
        "CUSTOM_AI_ASIC_MARGIN_CONCENTRATION",
        "AVGO_CUSTOM_MARGIN",
        "Custom AI ASIC customer concentration and margin watch",
        "GLOBAL",
        "failed_rerating",
        None,
        date(2026, 3, 4),
        None,
        None,
        None,
        ("custom_ai_asic_revenue", "single_hyperscaler_dependency", "tsmc_capacity_secured_flag"),
        ("customer_concentration", "custom_chip_margin_pressure", "startup_customer_risk_flag", "customer_project_delay"),
        "custom_ai_asic_margin_concentration_watch",
        "missing_price_data",
        ("round_121.md custom ASIC margin concentration guardrail",),
        "Custom ASIC visibility must be capped when revenue depends on a narrow customer base, lower custom-chip margin, or startup customer credit.",
        (E2RArchetype.REDTEAM_ACCOUNTING_TRUST_OVERLAY,),
    ),
    Round121CaseCandidate(
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
        ("round_121.md Reuters Nvidia CoWoS-L reference",),
        "CoWoS capacity expanded sharply but remains a bottleneck; both facts must be tracked together.",
    ),
    Round121CaseCandidate(
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
        ("round_121.md Reuters Broadcom supply constraints",),
        "Optical networking/PCB bottleneck becomes stronger in Loop 7 because lead time expanded from weeks to months.",
        (E2RArchetype.ADVANCED_PACKAGING_PCB,),
    ),
    Round121CaseCandidate(
        "cisco_ai_networking_orders_case",
        "AI_NETWORKING_SWITCHING_INFRA",
        "CSCO",
        "Cisco AI networking orders and switching guidance",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 13),
        None,
        None,
        None,
        ("ai_networking_orders", "hyperscaler_order_value", "data_center_switching_order_growth", "ai_infrastructure_order_guidance"),
        ("hyperscaler_concentration", "legacy_networking_revenue_change", "networking_restructuring_cost", "margin_miss"),
        "ai_networking_order_aligned",
        "needs_price_backfill",
        ("round_121.md Reuters Cisco AI orders",),
        "AI networking orders and guidance can support Stage 2, but legacy mix, restructuring cost, and order-to-margin conversion remain checks.",
        (E2RArchetype.AI_CAPEX_CROWDING_OVERLAY,),
    ),
    Round121CaseCandidate(
        "tower_photonics_ai_datacenter_deal_case",
        "PHOTONICS_AI_DATACENTER_CHIPS",
        "TSEM",
        "Tower Semiconductor AI data-center photonics deal",
        "US",
        "success_candidate",
        None,
        date(2026, 5, 13),
        None,
        None,
        None,
        ("photonics_chip_contract_value", "photonics_delivery_year", "silicon_photonics_revenue", "ai_datacenter_interconnect"),
        ("customer_concentration", "delivery_delay", "contract_margin_unverified", "yield_issue"),
        "photonics_contract_stage2",
        "needs_price_backfill",
        ("round_121.md Reuters Tower Semiconductor AI chip deals",),
        "A photonics chip contract can be Stage 2 when amount and delivery are known; Green needs revenue recognition, margin, and customer diversity.",
        (E2RArchetype.OPTICAL_NETWORKING_AI_DATACENTER,),
    ),
    Round121CaseCandidate(
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
        ("round_121.md Reuters Foxconn Q1 profit",),
        "AI server revenue and rack shipments can pass Stage 2, but margin and working-capital quality decide conviction.",
    ),
    Round121CaseCandidate(
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
        ("round_121.md Reuters Ecolab CoolIT acquisition",),
        "Cooling can be a structural data-center bottleneck, but acquisition multiple and accretion timing remain RedTeam fields.",
    ),
    Round121CaseCandidate(
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
        ("round_121.md FT OpenAI CoreWeave contract",),
        "A huge AI cloud contract can be Stage 2 visibility, but FCF, debt, and customer concentration block Green.",
        (E2RArchetype.LEVERAGE_FCF_BREAKDOWN,),
    ),
    Round121CaseCandidate(
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
        ("round_121.md Reuters CoreWeave OpenAI expanded pact",),
        "Expanded OpenAI contract raises visibility, but customer concentration and GPU/debt economics still block Green.",
        (E2RArchetype.LEVERAGE_FCF_BREAKDOWN,),
    ),
    Round121CaseCandidate(
        "coreweave_nvidia_circular_financing_case",
        "CIRCULAR_AI_FINANCING_OVERLAY",
        "CRWV",
        "CoreWeave/Nvidia/OpenAI circular financing watch",
        "US",
        "4b_watch",
        None,
        date(2026, 5, 13),
        None,
        date(2026, 5, 13),
        None,
        ("nvidia_capacity_guarantee_flag", "openai_equity_stake_flag", "gpu_cloud_contract_value", "capacity_guarantee_dependence"),
        ("circular_financing_flag", "customer_concentration", "refinancing_risk_flag", "fcf_negative", "supplier_support_dependency"),
        "circular_ai_financing_watch",
        "needs_price_backfill",
        ("round_121.md Reuters CoreWeave circular financing watch",),
        "Circular AI financing can inflate demand visibility; it must be RedTeam evidence until clean FCF and customer diversity are proven.",
        (E2RArchetype.NEOCLOUD_GPU_RENTAL, E2RArchetype.LEVERAGE_FCF_BREAKDOWN),
    ),
    Round121CaseCandidate(
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
        ("round_121.md WSJ Cerebras IPO",),
        "AI accelerator pure-play demand can be Stage 2 watch evidence, but IPO surge and ecosystem/customer risk keep it event premium.",
        (E2RArchetype.THEME_VALUATION_OVERHEAT,),
    ),
    Round121CaseCandidate(
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
        ("round_121.md Reuters Supermicro EY resignation",),
        "AI server growth cannot overcome auditor resignation, filing delay, or internal-control trust break.",
        (E2RArchetype.AI_SERVER_ODM_EMS_SUPPLY_CHAIN, E2RArchetype.THESIS_BREAK_4C),
    ),
    Round121CaseCandidate(
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
        ("round_121.md CXL/glass substrate guardrail",),
        "CXL, glass substrate, and neuromorphic tags remain Watch/Red until adoption, validation, production, and revenue exist.",
        (E2RArchetype.THEME_VALUATION_OVERHEAT,),
    ),
    Round121CaseCandidate(
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
        ("round_121.md FuriosaAI related stock watch",),
        "Related-stock exposure is not evidence. Customer validation, tape-out, mass production, and revenue must come first.",
        (E2RArchetype.THEME_VALUATION_OVERHEAT,),
    ),
    Round121CaseCandidate(
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
        ("round_121.md AI CAPEX crowding overlay",),
        "Crowded AI CAPEX evidence is a 4B warning overlay and must not create positive Green score by itself.",
        (E2RArchetype.CROWDED_RERATING_4B_WATCH,),
    ),
)


ROUND121_PRICE_FIELDS: tuple[str, ...] = (
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
    "hbm_revenue",
    "hbm_capacity_growth",
    "hbm_contract_duration",
    "hbm_lta_flag",
    "hbm_price_band_flag",
    "prepayment_flag",
    "hbm_prepayment_amount",
    "capacity_reservation_flag",
    "rpo_visibility",
    "hbm_market_share",
    "buyback_cancel_amount",
    "capital_return_flag",
    "customer_name",
    "nvidia_supply_chain_flag",
    "amd_supply_chain_flag",
    "hbm4_shipping_flag",
    "hbm4_yield_signal",
    "qualification_status",
    "volume_shipment_flag",
    "customer_specific_base_die_flag",
    "memory_spot_price_change",
    "memory_contract_price_change",
    "dram_nand_mix",
    "consumer_memory_exit_flag",
    "strategic_customer_allocation_flag",
    "capacity_reallocation_flag",
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
    "china_restriction_flag",
    "custom_ai_asic_revenue",
    "custom_ai_asic_customer_count",
    "hyperscaler_customer_name",
    "ai_chip_revenue",
    "custom_chip_margin",
    "startup_customer_risk_flag",
    "startup_customer_exposure_flag",
    "customer_project_delay_flag",
    "tsmc_capacity_secured_flag",
    "tsmc_capacity_miss_flag",
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
    "photonics_chip_contract_value",
    "photonics_delivery_year",
    "optical_networking_inventory_flag",
    "ai_networking_orders",
    "hyperscaler_order_value",
    "data_center_switching_order_growth",
    "ai_infrastructure_order_guidance",
    "networking_restructuring_cost",
    "legacy_networking_revenue_change",
    "ai_server_revenue",
    "ai_server_rack_shipments",
    "ai_server_margin",
    "gpu_server_revenue",
    "asic_server_revenue",
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
    "circular_financing_flag",
    "nvidia_capacity_guarantee_flag",
    "openai_equity_stake_flag",
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
    "government_customer_flag",
    "uae_revenue_concentration",
    "gross_margin",
    "software_ecosystem_score",
    "repeat_order_flag",
    "nvidia_competition_flag",
    "ipo_first_day_return",
    "ipo_valuation",
    "cash_burn_flag",
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


def round121_target_for(target_id: str) -> Round121ScoreTarget | None:
    for target in ROUND121_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round121_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND121_CASE_CANDIDATES:
        target = round121_target_for(candidate.target_id)
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
                f"Round121 R2 Loop-7 case for {candidate.target_id}; "
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


def round121_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND121_SCORE_TARGETS:
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
                "loop7_penalty_axes": "|".join(target.loop7_penalty_axes),
                "hard_gate": str(target.hard_gate).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round121_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND121_CASE_CANDIDATES:
        target = round121_target_for(candidate.target_id)
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


def round121_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "loop7_penalty_axes": "|".join(target.loop7_penalty_axes),
            "hard_gate": str(target.hard_gate).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND121_SCORE_TARGETS
    )


def round121_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round121_backfill": "true"} for field in ROUND121_PRICE_FIELDS)


def round121_base_score_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(weight.as_row() for weight in ROUND121_BASE_SCORE_WEIGHTS)


def round121_stage_cap_rows() -> tuple[dict[str, str], ...]:
    return tuple(cap.as_row() for cap in ROUND121_STAGE_CAPS)


def round121_score_stage_price_alignment_rows() -> tuple[dict[str, str], ...]:
    return tuple(alignment.as_row() for alignment in ROUND121_SCORE_STAGE_PRICE_ALIGNMENT)


def round121_summary() -> dict[str, int | bool]:
    records = round121_case_records()
    return {
        "target_count": len(ROUND121_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "base_score_component_count": len(ROUND121_BASE_SCORE_WEIGHTS),
        "stage_cap_count": len(ROUND121_STAGE_CAPS),
        "score_stage_price_alignment_count": len(ROUND121_SCORE_STAGE_PRICE_ALIGNMENT),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND121_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND121_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND121_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "hard_gate_target_count": sum(1 for target in ROUND121_SCORE_TARGETS if target.hard_gate),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round121_r2_loop7_reports(
    *,
    output_directory: str | Path = ROUND121_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND121_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND121_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round121_r2_loop7_ai_semiconductor_summary.md",
        "case_matrix": output / "round121_r2_loop7_case_matrix.csv",
        "stage_date_plan": output / "round121_r2_loop7_stage_date_plan.csv",
        "green_guardrails": output / "round121_r2_loop7_green_guardrails.md",
        "loop7_risk_overlays": output / "round121_r2_loop7_risk_overlays.md",
        "price_validation_plan": output / "round121_r2_loop7_price_validation_plan.md",
        "price_fields": output / "round121_r2_loop7_price_fields.csv",
        "base_score_weights": output / "round121_r2_loop7_base_score_weights.csv",
        "stage_caps": output / "round121_r2_loop7_stage_caps.csv",
        "score_stage_price_alignment": output / "round121_r2_loop7_score_stage_price_alignment.csv",
        "score_stage_price_alignment_md": output / "round121_r2_loop7_score_stage_price_alignment.md",
    }
    _write_case_jsonl(round121_case_records(), cases)
    _write_rows(round121_score_profile_rows(), score_profiles)
    _write_rows(round121_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round121_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round121_price_field_rows(), paths["price_fields"])
    _write_rows(round121_base_score_weight_rows(), paths["base_score_weights"])
    _write_rows(round121_stage_cap_rows(), paths["stage_caps"])
    _write_rows(round121_score_stage_price_alignment_rows(), paths["score_stage_price_alignment"])
    paths["summary"].write_text(render_round121_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round121_green_guardrail_markdown(), encoding="utf-8")
    paths["loop7_risk_overlays"].write_text(render_round121_loop7_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round121_price_validation_plan_markdown(), encoding="utf-8")
    paths["score_stage_price_alignment_md"].write_text(render_round121_score_stage_price_alignment_markdown(), encoding="utf-8")
    return paths


def render_round121_summary_markdown() -> str:
    summary = round121_summary()
    lines = [
        "# Round-121 R2 Loop-7 AI / Semiconductor / Electronics Summary",
        "",
        f"- source_round: `{ROUND121_SOURCE_ROUND_PATH}`",
        "- large_sector: `AI_SEMICONDUCTOR_ELECTRONICS`",
        "- loop: `R2 Loop 7 / v7.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- base_score_component_count: {summary['base_score_component_count']}",
        f"- stage_cap_count: {summary['stage_cap_count']}",
        f"- score_stage_price_alignment_count: {summary['score_stage_price_alignment_count']}",
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
        "- R2 Loop 7 says `AI 수혜` is not a score bucket.",
        "- Example: HBM can be structural, but SK하이닉스-like success can also be 4B-watch after rerating.",
        "- Example: HBM LTA/prepayment is stronger than a headline because price band, prepayment, and reserved capacity prove demand quality.",
        "- Example: Samsung/Micron-style HBM catch-up is separate from HBM leadership because qualification, yield, and volume are still execution gates.",
        "- Example: Micron-style consumer memory exit is not automatically structural; it must become AI/HBM allocation, mix, OPM, and EPS evidence.",
        "- Example: Kioxia-style AI storage NAND can show profit explosion, but 10x-20x price paths and NAND supply rebound require 4B/cycle review.",
        "- Example: Broadcom-style custom ASIC demand is not generic AI-chip evidence because customer concentration, TSMC capacity, and custom-chip margin must be checked.",
        "- Example: Cisco/Tower-style AI networking or photonics contracts can support Stage 2, but margin, delivery, and FCF conversion still decide conviction.",
        "- Example: Foxconn-style AI server rack growth is revenue evidence, but low margin and consignment economics still matter.",
        "- Example: CoreWeave-style contract visibility is not Green until debt, FCF, depreciation, and customer concentration pass.",
        "- Example: circular AI financing can make demand look cleaner than it is, so supplier/customer/investor overlap is RedTeam evidence.",
        "- Example: Supermicro-style auditor resignation is a hard accounting trust break even if AI server revenue was strong.",
    ]
    return "\n".join(lines) + "\n"


def render_round121_green_guardrail_markdown() -> str:
    lines = [
        "# Round-121 R2 Loop-7 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-7 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND121_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions) or 'not_applicable'} | {', '.join(target.loop7_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R2 Loop-7 v7.0 weights to production scoring yet.",
            "- Do not treat all AI beneficiaries as one archetype.",
            "- Do not treat HBM LTA, custom ASIC, AI server ODM, neocloud, and theme-only AI chips as the same evidence type.",
            "- Do not make CXL, glass substrate, neuromorphic, or AI chip related-stock keywords Green evidence without revenue.",
            "- Do not invent contract value, customer name, duration, prepayment, HBM yield, custom ASIC margin, stage price, or FCF.",
            "- Treat accounting trust break as hard 4C; treat AI CAPEX crowding as a 4B overlay, not a positive score.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round121_loop7_risk_overlay_markdown() -> str:
    lines = [
        "# Round-121 R2 Loop-7 Risk Overlays",
        "",
        "- `HBM_STRUCTURAL_SUCCESS_BUT_4B`: HBM is structurally right, but broad recognition and price path require 4B-watch.",
        "- `HBM_LTA_PREPAYMENT_CONFIRMED`: LTA, price band, prepayment, and capacity reservation are stronger visibility than a supply-shortage headline.",
        "- `HBM_CATCHUP_EXECUTION_CANDIDATE`: catch-up shipment is Stage 2 only until qualification, yield, and volume are proven.",
        "- `MEMORY_SUPPLY_REALLOCATION_ALIGNED`: consumer exit or channel shrinkage matters only if capacity shifts toward AI/HBM/enterprise mix and EPS.",
        "- `AI_STORAGE_NAND_SUCCESS_BUT_4B`: NAND/enterprise SSD can benefit from AI storage, but 4B crowding and supply rebound remain central.",
        "- `CUSTOM_AI_ASIC_ALIGNED`: named hyperscaler demand, secured capacity, margin visibility, and repeat revenue can support Stage 2 or better.",
        "- `CUSTOM_AI_ASIC_MARGIN_CONCENTRATION_WATCH`: custom ASIC visibility is capped if one customer, low custom margin, startup credit, or project delay dominates.",
        "- `OPTICAL_PCB_BOTTLENECK_ALIGNED`: optical/PCB lead time and orders matter, but lead-time normalization is a 4B/4C field.",
        "- `AI_NETWORKING_ORDER_ALIGNED`: AI switching/networking orders support Stage 2 only when guidance, margin, and FCF conversion follow.",
        "- `PHOTONICS_CONTRACT_STAGE2`: photonic chip contract amount, delivery year, customer, and use case support Stage 2 before Stage 3 proof.",
        "- `AI_REVENUE_BUT_MARGIN_WATCH`: AI server revenue grows, but margin, consignment, inventory, and customer concentration limit Green.",
        "- `CONTRACT_VISIBILITY_BUT_LEVERAGE_RISK`: neocloud contracts improve visibility, but debt, FCF, GPU depreciation, and concentration can block Green.",
        "- `CIRCULAR_AI_FINANCING_WATCH`: supplier, customer, and investor relationships can overstate clean demand visibility.",
        "- `AI_ACCELERATOR_IPO_EVENT_PREMIUM`: AI accelerator IPO demand is not Green until repeat orders, gross margin, ecosystem, and FCF are visible.",
        "- `ACCOUNTING_TRUST_BREAK_4C`: auditor resignation, filing delay, internal control, or regulatory probe breaks the thesis.",
        "- `DISCLOSURE_CONFIDENCE_CAPPED`: contract or facility headlines are capped until amount, counterparty, period, margin, and parser confidence are checked.",
        "- `THEME_WITHOUT_REVENUE`: CXL, glass substrate, AI chip, or neuromorphic theme has no customer validation or revenue.",
        "",
        "Simple example: `OpenAI contract` can support Stage 2 visibility for a GPU cloud. It is not Green if debt and FCF are still unresolved.",
    ]
    return "\n".join(lines) + "\n"


def render_round121_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-121 R2 Loop-7 Price Validation Plan",
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
    for row in round121_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `hbm_structural_success_but_4b`: HBM evidence and price path align, but rerating may already be crowded.",
            "- `hbm_lta_prepayment_confirmed`: long-term agreements, price bands, prepayment, and capacity reservation increase visibility but still need price-path validation.",
            "- `memory_supply_reallocation_aligned`: capacity shift from consumer memory toward AI/HBM/enterprise demand must show mix and EPS improvement.",
            "- `custom_ai_asic_aligned`: hyperscaler custom ASIC demand must show named customer, capacity, margin, and repeat revenue.",
            "- `custom_ai_asic_margin_concentration_watch`: customer concentration or margin pressure is a RedTeam gate, not a positive score.",
            "- `ai_revenue_but_margin_watch`: AI server revenue grows but margin and working capital remain unproven.",
            "- `AI_NETWORKING_ORDER_ALIGNED`: AI networking/switching orders align only after revenue, margin, and repeat customer proof.",
            "- `PHOTONICS_CONTRACT_STAGE2`: AI photonics deal is Stage 2 before revenue recognition and customer diversification.",
            "- `contract_visibility_but_leverage_risk`: contract visibility exists but leverage and FCF block Green.",
            "- `CIRCULAR_AI_FINANCING_WATCH`: circular supplier/customer/investor structures are RedTeam overlays, not clean demand proof.",
            "- `theme_without_revenue`: technical theme has no customer validation, yield, production, or revenue.",
            "- `accounting_trust_break_4c`: trust evidence breaks the Stage 3 thesis.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round121_score_stage_price_alignment_markdown() -> str:
    lines = [
        "# Round-121 R2 Loop-7 Score -> Stage -> Price Alignment",
        "",
        "Round 121 uses the R2 v7 score table to test whether AI/semiconductor evidence produced the right stage and whether that stage matched the observed price path in the source note.",
        "",
        "## R2 v7 Base Score Weights",
        "",
        "| component | points | direction | reason |",
        "| --- | ---: | --- | --- |",
    ]
    for row in round121_base_score_weight_rows():
        lines.append(f"| `{row['component']}` | {row['points']} | {row['loop7_direction']} | {row['reason']} |")
    lines.extend(
        [
            "",
            "## Stage Caps",
            "",
            "| stage | cap | required evidence | examples | Green policy |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in round121_stage_cap_rows():
        lines.append(
            "| "
            f"{row['stage_band']} | {row['max_score']} | {row['required_evidence']} | "
            f"{row['example_cases']} | {row['green_policy']} |"
        )
    lines.extend(
        [
            "",
            "## Alignment Cases",
            "",
            "| case_id | detected_stage | price_path_status | verdict | normalization_adjustment |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in round121_score_stage_price_alignment_rows():
        lines.append(
            "| "
            f"`{row['case_id']}` | {row['detected_stage']} | {row['price_path_status']} | "
            f"{row['verdict']} | {row['normalization_adjustment']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- HBM and AI storage can be structurally right while already requiring 4B-watch after a large rerating.",
            "- HBM catch-up, photonics, networking, and equipment can reach Stage 2 when customer, shipment, order, or guidance evidence exists.",
            "- AI server ODM, neocloud, and AI accelerator IPO cases need capital, margin, accounting, and customer-concentration checks before any Green discussion.",
            "- Simple example: `Samsung HBM4 shipped` can be Stage 2; it is not Stage 3-Green until qualification, yield, volume shipment, and EPS conversion are verified.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round121CaseCandidate) -> str:
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


def _rerating_result(candidate: Round121CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type in {"overheat", "4b_watch"}:
        return "theme_overheat"
    if candidate.case_type == "event_premium":
        return "event_premium"
    return "unknown" if candidate.case_type == "success_candidate" else "no_rerating"


def _score_weight_hint(target: Round121ScoreTarget) -> dict[str, float]:
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
