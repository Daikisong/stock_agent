"""Round-162 R4 Loop-10 materials, spread, and strategic-resources pack.

Round 162 turns R4 into a score-stage-price alignment layer for chemicals,
refining, metals, rare earths, copper, lithium, gold miners, fertilizer input
cost squeezes, Korea Zinc-style event premiums, packaging, and speculative
material themes. It separates
commodity price moves from structural EPS/FCF rerating: price floor, offtake,
government investment, realized price, AISC, production volume, cash cost, FCF,
capital return, dilution, governance events, and processing/fertilizer input
costs decide the stage.

Simple example: copper record highs are useful Stage 1/2 macro evidence. They
are not company-level Stage 3-Green unless production volume, cash cost, FCF,
capital return, and processing input costs are visible as-of the case date.

This module is calibration/report material only: production feature
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


ROUND162_SOURCE_ROUND_PATH = "docs/round/round_162.md"
ROUND162_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round162_r4_loop10_materials_spread_strategic"
ROUND162_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r4_loop10_round162.jsonl"
ROUND162_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round162_r4_loop10_v10.csv"
ROUND162_SOURCE_CANONICAL_TARGET_COUNT = 22


@dataclass(frozen=True)
class Round162ScoreWeightDraft:
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
class Round162ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round162ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop10_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.MATERIALS_SPREAD_STRATEGIC

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round162CaseCandidate:
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
class Round162BaseScoreWeight:
    component: str
    weight: int
    interpretation: str


@dataclass(frozen=True)
class Round162StageCap:
    cap_id: str
    max_stage: str
    condition: str
    example: str


@dataclass(frozen=True)
class Round162ScoreStagePriceAlignment:
    case_id: str
    score_stage: str
    price_path_signal: str
    verdict: str
    normalization_adjustment: str


def _w(
    eps_fcf: int | str,
    visibility: int | str,
    bottleneck: int | str,
    mispricing: int | str,
    valuation: int | str,
    capital: int | str = 0,
    confidence: int | str = 5,
) -> Round162ScoreWeightDraft:
    return Round162ScoreWeightDraft(eps_fcf, visibility, bottleneck, mispricing, valuation, capital, confidence)


def _target(
    target_id: str,
    archetype: E2RArchetype,
    posture: Round10ThemePosture,
    weight: Round162ScoreWeightDraft,
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
) -> Round162ScoreTarget:
    return Round162ScoreTarget(
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


ROUND162_BASE_SCORE_WEIGHTS: tuple[Round162BaseScoreWeight, ...] = (
    Round162BaseScoreWeight(
        "eps_fcf_transition",
        22,
        "Commodity price alone is capped; OP/EPS/FCF and cost control decide Stage 3.",
    ),
    Round162BaseScoreWeight(
        "contract_offtake_price_floor_visibility",
        20,
        "Price floor, offtake, government investment, customer contract, production plan, and buyback support Stage 2.",
    ),
    Round162BaseScoreWeight(
        "bottleneck_pricing_power",
        18,
        "Copper AI-grid demand, rare earth scarcity, realized gold price, and spread improvement are useful only with bottleneck durability.",
    ),
    Round162BaseScoreWeight(
        "capital_discipline_dilution_risk",
        12,
        "Capital raise, share issuance, all-stock dilution, CAPEX burden, dividend cut, and buyback quality are stronger Loop-10 score axes.",
    ),
    Round162BaseScoreWeight(
        "information_confidence_disclosure_detail",
        10,
        "Stage 3 needs contract terms, counterparty, price floor, duration, realized price, AISC, production, and FCF details.",
    ),
    Round162BaseScoreWeight(
        "market_mispricing_rerating_gap",
        10,
        "Separate structural mispricing from tender-offer or governance event premium.",
    ),
    Round162BaseScoreWeight(
        "valuation_room_4b_runway",
        8,
        "Large scarcity rallies, YTD multi-baggers, and record commodity consensus reduce runway.",
    ),
)


ROUND162_STAGE_CAPS: tuple[Round162StageCap, ...] = (
    Round162StageCap(
        "stage1_price_or_event_only_cap",
        "Stage 1",
        "commodity price increase, export-control headline, safe-haven demand, China stimulus, supply shortage headline, or science theme only",
        "Rare-earth export-control news, copper record high, or graphene/MXene/superconductor social-media theme.",
    ),
    Round162StageCap(
        "stage2_structural_visibility_cap",
        "Stage 2",
        "price floor, offtake, government investment, customer contract, M&A, production plan, buyback, realized price, or AISC confirmed",
        "MP Materials DoD/Apple contracts, Barrick realized price plus AISC plus buyback, or Equinox-Orla jurisdiction M&A.",
    ),
    Round162StageCap(
        "stage3_operating_confirmation_required",
        "Stage 3 candidate",
        "OP/EPS/FCF revision, cost control, stable production, capital return, price-path alignment, and no hard 4C flag",
        "Gold miner Stage 3 needs realized price, AISC, production delivery, FCF, and capital return, not just gold price.",
    ),
    Round162StageCap(
        "stage4b_scarcity_consensus_priced",
        "4B-watch",
        "scarcity or strategic-material narrative is widely accepted and valuation moves ahead of production/FCF",
        "MP Materials YTD +275% before dilution risk is resolved.",
    ),
    Round162StageCap(
        "stage4c_hard_redteam",
        "4C",
        "price collapse, supply restart, oversupply, dilution, governance shock, event premium unwind, input-cost spike, or replication failure",
        "Korea Zinc share issuance/probe, LG/Lotte petrochemical oversupply, lithium -86%, HPAL sulfur squeeze, Mosaic fertilizer input-cost squeeze, or speculative science failure.",
    ),
)


ROUND162_SCORE_STAGE_PRICE_ALIGNMENT: tuple[Round162ScoreStagePriceAlignment, ...] = (
    Round162ScoreStagePriceAlignment(
        "mp_materials_dod_price_floor_case",
        "Stage 2 + 4B-watch",
        "rare-earth structure reflected; YTD +275% before offering",
        "structural capture is right, but valuation already moved",
        "raise offtake/price-floor/government-investment credit; strengthen valuation and capital dilution penalty",
    ),
    Round162ScoreStagePriceAlignment(
        "mp_materials_capital_raise_dilution_case",
        "4C-watch",
        "after-hours -5.8% after $500M common stock offering",
        "capital penalty matched price path",
        "strengthen capital_raise, dilution, and CAPEX-funding penalty",
    ),
    Round162ScoreStagePriceAlignment(
        "copper_ai_grid_record_high_case",
        "Stage 1~2",
        "copper record high; approximately +40% YoY futures move",
        "commodity price path matched, but not company-level Green",
        "raise copper bottleneck score; require production, cash cost, FCF, and capital return for Green",
    ),
    Round162ScoreStagePriceAlignment(
        "barrick_record_gold_buyback_case",
        "Stage 2~3 candidate",
        "net earnings tripled, realized gold price $4,823/oz, AISC $1,708/oz, $3B buyback",
        "earnings path matched; OHLCV backfill still required",
        "raise gold miner EPS/FCF and capital-return credit while keeping cycle cap",
    ),
    Round162ScoreStagePriceAlignment(
        "equinox_orla_gold_jurisdiction_case",
        "Stage 2",
        "Canada-focused M&A; price backfill required",
        "jurisdiction rerating thesis is stage-detectable",
        "keep jurisdiction rerating archetype; penalize all-stock dilution and integration risk",
    ),
    Round162ScoreStagePriceAlignment(
        "korea_zinc_tender_offer_event_case",
        "Event Premium",
        "Korea Zinc +19.8% on tender offer; Young Poong limit-up",
        "event premium separation worked",
        "strengthen event_premium cap before any strategic-metal score is considered",
    ),
    Round162ScoreStagePriceAlignment(
        "korea_zinc_share_issue_probe_case",
        "4C-watch",
        "filing/probe/revision-order path erased prior event premium; -8% filing reaction noted",
        "governance/capital RedTeam matched",
        "strengthen capital structure, regulator probe, and share issuance gate",
    ),
    Round162ScoreStagePriceAlignment(
        "lg_chem_lotte_chemical_oversupply_case",
        "Stage 4C",
        "OP plunge and losses from China/Middle East oversupply",
        "chemical Green false-positive avoided",
        "lower CHEMICAL_SPREAD and require restructuring/supply closure/FCF recovery",
    ),
    Round162ScoreStagePriceAlignment(
        "lithium_price_86pct_crash_case",
        "Stage 4C / cycle",
        "lithium price down about 86% from 2022 peak",
        "cycle RedTeam is very strong",
        "keep lithium Stage 3 capped until low-cost position, offtake, FCF defense, and supply-response control are proven",
    ),
    Round162ScoreStagePriceAlignment(
        "indonesia_nickel_hpal_sulfur_squeeze_case",
        "4C-watch",
        "nickel price rose, but HPAL sulfur input cost and capacity cuts pressured processing economics",
        "price-only rally can be wrong",
        "add processing input cost, sulfuric acid cost, and refinery-margin fields",
    ),
    Round162ScoreStagePriceAlignment(
        "mosaic_phosphate_sulfuric_acid_squeeze_case",
        "4C-watch",
        "phosphate pricing was favorable, but sulfuric acid, sulfur, ammonia, and urea input costs drove losses and guidance withdrawal",
        "spread headline was weaker than input-cost evidence",
        "add fertilizer sulfuric-acid input overlay and require margin/FCF confirmation before any fertilizer spread rerating",
    ),
)


ROUND162_SCORE_TARGETS: tuple[Round162ScoreTarget, ...] = (
    _target(
        "REFINING_OIL_SPREAD",
        E2RArchetype.REFINING_OIL_SPREAD,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 12, 16, 10, 8, 5, 10),
        stage1=("refining_margin_rebound", "oil_geopolitical_event", "inventory_gain", "logistics_normalization"),
        stage2=("refining_op_improvement", "inventory_gain_loss_excluded", "core_refining_margin", "op_revision_1q"),
        stage3=("repeat_fcf", "core_margin_durable", "high_margin_mix", "inventory_noise_excluded"),
        stage4b=("refining_margin_peak", "inventory_gain_crowded", "geopolitical_premium_fully_priced"),
        stage4c=("refining_margin_drop", "inventory_loss", "logistics_recovery_delay", "demand_slowdown"),
        green=("repeat_fcf", "core_margin_durable", "inventory_noise_excluded"),
        red=("inventory_loss", "refining_margin_drop", "temporary_crack_spread", "geopolitical_event_reversal"),
        penalties=("refining_margin", "inventory_gain_loss", "logistics", "geopolitics"),
        note="Refining remains Watch because crack spread and inventory gains are not durable FCF by themselves.",
    ),
    _target(
        "LUBRICANTS_HIGH_MARGIN_MIX",
        E2RArchetype.LUBRICANTS_HIGH_MARGIN_MIX,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(19, 16, 12, 12, 10, 6, 10),
        stage1=("lubricants_high_margin_mix", "base_oil_margin", "repeat_industrial_demand"),
        stage2=("mix_ratio_improves", "repeat_demand", "opm_expansion", "fcf_margin"),
        stage3=("high_margin_mix_durable", "repeat_customer_demand", "capital_return", "fcf_conversion"),
        stage4b=("lubricants_premium_crowded", "margin_peak_ignored"),
        stage4c=("oil_price_shock", "mix_deterioration", "industrial_demand_slowdown", "margin_reversal"),
        green=("high_margin_mix_durable", "repeat_demand", "fcf_conversion", "capital_return"),
        red=("mix_deterioration", "oil_price_shock", "demand_slowdown"),
        penalties=("oil_price", "mix", "demand", "margin"),
        note="Lubricants can move toward Green only when high-margin mix is repeatable and cash-generative.",
    ),
    _target(
        "CHEMICAL_SPREAD",
        E2RArchetype.CHEMICAL_SPREAD,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(14, 5, 12, 7, 5, 4, 10),
        stage1=("chemical_spread_rebound", "china_stimulus", "product_price_rebound", "restocking"),
        stage2=("actual_op_improvement", "spread_change_90d", "inventory_normalization", "capacity_shutdown"),
        stage3=("supply_glut_easing", "restructuring", "durable_spread", "fcf_margin"),
        stage4b=("spread_recovery_crowded", "china_stimulus_overpriced"),
        stage4c=("china_middle_east_capacity_glut", "spread_reversal", "inventory_increase", "op_fcf_drop"),
        green=("supply_glut_easing", "capacity_restructuring", "durable_fcf"),
        red=("china_middle_east_capacity_glut", "supply_glut", "spread_reversal", "inventory_increase"),
        penalties=("oversupply", "supply_glut", "china_middle_east_capacity", "inventory"),
        note="Chemicals are RedTeam-first because spread rebound can reverse before FCF becomes structural.",
    ),
    _target(
        "STEEL_METAL_SPREAD",
        E2RArchetype.STEEL_METAL_SPREAD,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(17, 10, 15, 10, 7, 5, 10),
        stage1=("steel_spread", "iron_ore_price", "china_construction_demand", "plate_price"),
        stage2=("steel_spread_improvement", "cost_control", "op_revision_1q", "inventory_normalization"),
        stage3=("supply_discipline", "demand_recovery", "fcf_margin", "dividend_supported_by_fcf"),
        stage4b=("steel_recovery_crowded", "dividend_expectation_full"),
        stage4c=("iron_ore_price_decline", "china_demand_weakness", "dividend_cut", "profit_downcycle"),
        green=("supply_discipline", "demand_recovery", "fcf_margin"),
        red=("chinese_exports", "china_demand_weakness", "dividend_cut", "price_pressure"),
        penalties=("china_demand", "iron_ore", "steel_spread", "dividend"),
        note="Steel is Watch; China demand, raw material cost, and dividends decide whether the story survives.",
    ),
    _target(
        "IRON_ORE_CHINA_DEMAND_CYCLE",
        E2RArchetype.IRON_ORE_CHINA_DEMAND_CYCLE,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(16, 8, 14, 8, 6, 5, 10),
        stage1=("iron_ore_price", "china_property_demand", "steel_production", "dividend_expectation"),
        stage2=("iron_ore_margin", "china_demand_visible", "capital_return_supported", "cost_curve_advantage"),
        stage3=("low_cost_position", "china_demand_recovery", "fcf_defense", "dividend_supported_by_fcf"),
        stage4b=("iron_ore_rebound_crowded", "dividend_expectation_full"),
        stage4c=("iron_ore_price_decline", "china_demand_weakness", "dividend_cut", "profit_downcycle"),
        green=("low_cost_position", "fcf_defense", "dividend_supported_by_fcf", "demand_recovery"),
        red=("iron_ore_price_decline", "china_demand_weakness", "dividend_cut", "profit_downcycle"),
        penalties=("china_demand", "iron_ore_price", "dividend_cut", "profit_downcycle"),
        note="Iron ore is RedTeam-first because China demand weakness can quickly cut profit and capital return.",
    ),
    _target(
        "NONFERROUS_STRATEGIC_METALS",
        E2RArchetype.NONFERROUS_STRATEGIC_METALS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 14, 15, 12, 8, 6, 10),
        stage1=("copper_zinc_aluminum_price", "smelting_margin", "mine_disruption", "strategic_metal_keyword"),
        stage2=("realized_metal_price", "smelting_margin", "op_revision_1q", "fcf_margin"),
        stage3=("cost_curve_advantage", "supply_constraint", "fcf_conversion", "capital_return"),
        stage4b=("nonferrous_price_rally_crowded", "event_premium_confused_with_fcf"),
        stage4c=("metal_price_drop", "china_demand_slowdown", "smelting_margin_drop", "governance_event_only"),
        green=("cost_curve_advantage", "supply_constraint", "fcf_conversion", "capital_return"),
        red=("metal_price_drop", "smelting_margin_drop", "event_premium", "governance_dispute"),
        penalties=("metal_price", "smelting_margin", "event_premium", "china_demand"),
        note="Nonferrous needs smelting-margin and FCF evidence; event price moves must be separated.",
    ),
    _target(
        "COPPER_AI_GRID_STRUCTURAL_DEMAND",
        E2RArchetype.COPPER_AI_GRID_STRUCTURAL_DEMAND,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(20, 16, 20, 12, 8, 6, 10),
        stage1=("ai_datacenter_grid_demand", "grid_modernization", "ev_renewable_copper_demand", "copper_price_breakout"),
        stage2=("deficit_forecast", "mine_disruption", "company_eps_revision", "realized_copper_price"),
        stage3=("low_cost_production", "production_volume_stable", "fcf_conversion", "capital_return"),
        stage4b=("ai_copper_narrative_crowded", "stockpile_distortion_ignored", "physical_etf_flow_overpriced"),
        stage4c=("copper_price_drop", "mine_supply_normalization", "demand_destruction", "tariff_inventory_unwind"),
        green=("low_cost_production", "production_volume_stable", "fcf_conversion", "capital_return"),
        red=("inventory_distortion", "tariff_stockpile", "mine_restart", "demand_destruction"),
        penalties=("tariff_inventory", "mine_restart", "demand_destruction", "stockpile"),
        note="Copper has AI-grid demand, but company-level Green still needs cost curve, volume, FCF, and returns.",
    ),
    _target(
        "COPPER_PROCESSING_INPUT_COST_OVERLAY",
        E2RArchetype.COPPER_PROCESSING_INPUT_COST_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("sulfuric_acid_cost", "processing_input_cost", "mine_disruption", "tariff_inventory_distortion"),
        stage2=("input_cost_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("sulfuric_acid_spike", "processing_cost_squeeze", "mine_supply_disruption", "tariff_inventory_unwind"),
        green=(),
        red=("sulfuric_acid_spike", "processing_cost_squeeze", "mine_supply_disruption", "tariff_inventory_unwind"),
        penalties=("sulfuric_acid", "processing_input_cost", "mine_disruption", "tariff_inventory"),
        note="Copper processing input cost is a RedTeam overlay; it can eat the benefit of AI-grid copper demand.",
        gate_only=True,
    ),
    _target(
        "NICKEL_SULFUR_HPAL_INPUT_COST",
        E2RArchetype.NICKEL_SULFUR_HPAL_INPUT_COST,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("battery_grade_nickel_demand", "indonesia_hpal_capacity", "nickel_price_rebound"),
        stage2=("nickel_price_rebound_detected", "hpal_margin_risk_detected"),
        stage3=("not_applicable_gate_only",),
        stage4b=("battery_nickel_rally_before_processing_margin",),
        stage4c=("sulfur_shortage", "sulfuric_acid_spike", "hpal_capacity_cut", "processing_margin_squeeze", "import_dependency"),
        green=(),
        red=("sulfur_shortage", "sulfuric_acid_spike", "hpal_capacity_cut", "processing_margin_squeeze", "import_dependency"),
        penalties=("sulfur", "sulfuric_acid", "hpal_margin", "input_cost"),
        note="Nickel price rebound is not enough when sulfur/HPAL input costs squeeze battery-grade nickel economics.",
        gate_only=True,
    ),
    _target(
        "FERTILIZER_INPUT_COST_SULFURIC_ACID",
        E2RArchetype.FERTILIZER_INPUT_COST_SULFURIC_ACID,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("phosphate_price_strength", "fertilizer_supply_tightness", "sulfuric_acid_cost", "sulfur_cost"),
        stage2=("input_cost_risk_detected", "production_guidance_at_risk"),
        stage3=("not_applicable_gate_only",),
        stage4b=("fertilizer_price_rally_before_input_cost_audit",),
        stage4c=(
            "sulfuric_acid_spike",
            "sulfur_cost_spike",
            "ammonia_cost_spike",
            "urea_cost_spike",
            "production_curtailment",
            "guidance_withdrawal",
            "loss_reported",
        ),
        green=(),
        red=(
            "sulfuric_acid_spike",
            "sulfur_cost_spike",
            "ammonia_cost_spike",
            "urea_cost_spike",
            "production_curtailment",
            "guidance_withdrawal",
            "loss_reported",
        ),
        penalties=("sulfuric_acid", "sulfur", "ammonia", "urea", "production_curtailment", "guidance_withdrawal"),
        note="Fertilizer price strength can fail when sulfuric acid, sulfur, ammonia, or urea costs overwhelm phosphate pricing.",
        gate_only=True,
    ),
    _target(
        "RARE_METALS_PRICE_FLOOR_OFFTAKE",
        E2RArchetype.RARE_METALS_PRICE_FLOOR_OFFTAKE,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(20, 24, 20, 12, 8, 8, 10),
        stage1=("rare_earth_export_control", "strategic_supply_chain", "defense_supply_chain", "rare_earth_price_spike"),
        stage2=("government_investment", "price_floor", "offtake_contract", "long_term_purchase", "production_capacity"),
        stage3=("production_ramp_up", "customer_diversification", "revenue_recognized", "fcf_conversion"),
        stage4b=("rare_earth_related_rally_crowded", "no_production_capacity_rally", "price_floor_overgeneralized"),
        stage4c=("production_ramp_failure", "price_floor_policy_change", "customer_offtake_delay", "policy_support_delay"),
        green=("government_support", "price_floor", "offtake_contract", "production_capacity", "fcf_conversion"),
        red=("no_production_capacity", "no_offtake", "no_price_floor", "project_delay", "policy_dependency"),
        penalties=("policy", "production_ramp", "project_execution", "price_floor"),
        note="Rare metals get stronger only when policy support is tied to price floor, offtake, production, and FCF.",
    ),
    _target(
        "RARE_EARTH_MAGNET_SUPPLY_CHAIN",
        E2RArchetype.RARE_EARTH_MAGNET_SUPPLY_CHAIN,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(20, 22, 19, 12, 8, 8, 10),
        stage1=("rare_earth_magnet_supply_chain", "ndfeb_magnet", "domestic_magnet_production", "china_export_control"),
        stage2=("apple_prepayment", "dod_customer", "magnet_production_schedule", "recycled_feedstock", "offtake_contract"),
        stage3=("magnet_ramp_up", "customer_qualification", "revenue_recognized", "fcf_conversion"),
        stage4b=("magnet_supply_chain_premium_crowded", "policy_premium_overgeneralized"),
        stage4c=("magnet_ramp_delay", "customer_qualification_failure", "feedstock_shortage", "policy_support_change"),
        green=("magnet_production", "customer_qualification", "offtake_contract", "recycled_feedstock", "fcf_conversion"),
        red=("magnet_ramp_delay", "customer_qualification_failure", "feedstock_shortage", "policy_support_change"),
        penalties=("magnet_ramp", "customer_qualification", "feedstock", "policy_support"),
        note="Rare-earth magnet supply-chain evidence is stronger than raw price spikes only when customers, production ramp, feedstock, and FCF are visible.",
    ),
    _target(
        "RARE_METALS_EXPORT_CONTROL_EVENT",
        E2RArchetype.RARE_METALS_EXPORT_CONTROL_EVENT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(10, 8, 16, 10, 6, 4, 10),
        stage1=("rare_earth_export_control", "export_license_delay", "yttrium_export_delay", "dysprosium_shortage", "terbium_shortage"),
        stage2=("company_supply_contract", "production_capacity", "customer_offtake", "strategic_supply_chain"),
        stage3=("price_floor", "offtake_contract", "production_ramp_up", "fcf_conversion"),
        stage4b=("rare_earth_export_control_rally_crowded", "price_spike_overgeneralized", "no_production_capacity_rally"),
        stage4c=("export_control_relief", "truce_extension", "price_normalization", "production_capacity_absent"),
        green=("price_floor", "offtake_contract", "production_capacity", "fcf_conversion"),
        red=("no_production_capacity", "no_offtake", "export_control_relief", "price_normalization"),
        penalties=("export_control_relief", "price_spike", "no_production_capacity", "policy_truce"),
        note="Export-control news is Stage 1 macro evidence; without company production and offtake it is not Green.",
    ),
    _target(
        "RARE_EARTH_CAPITAL_RAISE_DILUTION",
        E2RArchetype.RARE_EARTH_CAPITAL_RAISE_DILUTION,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("rare_earth_contract_after_rally", "strategic_resource_capex", "government_support"),
        stage2=("capital_raise_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("rare_earth_rally_after_price_floor", "valuation_moved_before_production"),
        stage4c=("common_stock_offering", "share_dilution", "capex_funding_gap", "policy_dependency"),
        green=(),
        red=("common_stock_offering", "share_dilution", "capex_funding_gap", "valuation_already_moved"),
        penalties=("capital_raise", "dilution", "capex", "valuation_runup"),
        note="MP-style strategic rare-earth success still needs capital discipline; offering and dilution cap unsafe Green.",
        gate_only=True,
    ),
    _target(
        "LITHIUM_ESS_DEMAND_CYCLE",
        E2RArchetype.LITHIUM_ESS_DEMAND_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(14, 8, 12, 7, 5, 5, 10),
        stage1=("lithium_price_rebound", "mine_shutdown", "ev_or_ess_demand", "capex_cut"),
        stage2=("low_cost_mine", "offtake_contract", "fcf_defense", "capex_discipline"),
        stage3=("durable_fcf", "restart_supply_risk_controlled", "low_cost_position", "price_defense"),
        stage4b=("lithium_rebound_crowded", "mine_restart_ignored", "sodium_ion_ignored"),
        stage4c=("lithium_price_crash", "mine_restart_supply_rebound", "ev_demand_slowdown", "sodium_ion_substitution"),
        green=("low_cost_mine", "offtake_contract", "fcf_defense", "capex_discipline"),
        red=("price_crash", "mine_restart", "supply_rebound", "sodium_ion_competition", "ev_demand_slowdown"),
        penalties=("lithium_price", "mine_restart", "ev_demand", "sodium_ion"),
        note="Lithium ESS demand can help Stage 1/2 but remains Cycle/Watch without FCF and supply response control.",
    ),
    _target(
        "PRECIOUS_METALS_SAFE_HAVEN_MINERS",
        E2RArchetype.PRECIOUS_METALS_SAFE_HAVEN_MINERS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(22, 13, 16, 10, 8, 10, 10),
        stage1=("gold_silver_price", "safe_haven_demand", "real_rate_drop", "mine_output"),
        stage2=("realized_gold_price", "aisc_control", "fcf_improvement", "buyback_or_dividend"),
        stage3=("cost_control", "capital_return", "production_stable", "jurisdiction_risk_controlled"),
        stage4b=("record_gold_price_crowded", "miner_group_overheat", "safe_haven_narrative_crowded"),
        stage4c=("gold_price_correction", "aisc_rise", "production_drop", "jurisdiction_risk"),
        green=("realized_price", "aisc_control", "capital_return", "fcf_conversion", "production_stable"),
        red=("gold_price_correction", "aisc_rise", "mine_risk", "production_drop"),
        penalties=("gold_price", "aisc", "production", "jurisdiction"),
        note="Gold miners can work as cycles, but safe-haven price alone is not structural visibility.",
    ),
    _target(
        "GOLD_MINER_JURISDICTION_RERATING",
        E2RArchetype.GOLD_MINER_JURISDICTION_RERATING,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(20, 16, 14, 12, 8, 8, 10),
        stage1=("jurisdiction_safety_premium", "gold_mna", "canada_us_assets", "safe_haven_gold"),
        stage2=("safe_jurisdiction_assets", "mna_synergy", "production_profile", "aisc_control"),
        stage3=("fcf_conversion", "reserve_replacement", "capital_return", "jurisdiction_discount_narrows"),
        stage4b=("jurisdiction_safety_premium_crowded", "gold_mna_premium_full"),
        stage4c=("mna_dilution", "integration_failure", "production_miss", "gold_price_reversal"),
        green=("safe_jurisdiction_assets", "fcf_conversion", "capital_return", "reserve_replacement"),
        red=("mna_dilution", "integration_failure", "production_miss", "gold_price_reversal"),
        penalties=("mna_dilution", "integration", "gold_price", "production"),
        note="Gold-miner jurisdiction rerating needs safer assets, production/AISC proof, FCF, and capital return, not gold price alone.",
    ),
    _target(
        "GENERAL_TRADING_RESOURCE_INFRA",
        E2RArchetype.GENERAL_TRADING_RESOURCE_INFRA,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(17, 20, 12, 12, 16, 10, 10),
        stage1=("resource_rights", "energy_contract", "buyback_dividend", "conglomerate_discount_rerating"),
        stage2=("long_term_offtake", "project_stake", "fcf", "capital_return", "valuation_discount"),
        stage3=("resource_infra_fcf_frame", "capital_allocation_execution", "valuation_discount_narrows"),
        stage4b=("sogo_shosha_story_crowded", "resource_infra_rerating_full"),
        stage4c=("commodity_price_drop", "project_delay", "capital_allocation_retreat", "fx_hit"),
        green=("long_term_offtake", "project_stake", "fcf", "capital_return"),
        red=("commodity_cycle", "project_delay", "capital_allocation_retreat"),
        penalties=("commodity", "fx", "conglomerate_discount", "project_delay"),
        note="Trading/resource houses rerate on resource-infra FCF and capital allocation, not sales scale alone.",
    ),
    _target(
        "LNG_ENERGY_TRADING_DISTRIBUTION",
        E2RArchetype.LNG_ENERGY_TRADING_DISTRIBUTION,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(18, 18, 16, 10, 8, 6, 10),
        stage1=("lng_long_term_contract", "energy_security", "lpg_distribution", "project_news"),
        stage2=("long_term_contract", "fid_status", "project_equity_investment", "margin_visible"),
        stage3=("repeat_fcf", "project_stake", "energy_security_value", "margin_visible"),
        stage4b=("lng_contract_story_crowded", "energy_security_premium_full"),
        stage4c=("fid_delay", "financing_delay", "lng_price_reversal", "project_delay"),
        green=("long_term_contract", "fid_status", "project_stake", "margin_visible", "repeat_fcf"),
        red=("fid_delay", "financing_delay", "price_reversal", "project_delay"),
        penalties=("fid", "lng_price", "project_financing", "margin"),
        note="LNG can be Watch-to-Green when long contracts, FID, project stake, and FCF are explicit.",
    ),
    _target(
        "PAPER_PACKAGING_CYCLE",
        E2RArchetype.PAPER_PACKAGING_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(16, 12, 12, 10, 7, 5, 10),
        stage1=("paper_price", "corrugated_spread", "packaging_mna", "plastic_replacement"),
        stage2=("volume_recovery", "price_cost_spread", "mna_synergy", "cash_return"),
        stage3=("durable_spread", "scale_economics", "cash_return", "fcf_stable"),
        stage4b=("packaging_mna_premium_crowded", "consolidation_narrative_overpriced"),
        stage4c=("low_volume", "price_pressure", "competition_remedy", "plant_divestment", "mature_industry_limit"),
        green=("volume_recovery", "price_cost_spread", "cash_return", "fcf_stable"),
        red=("low_volume", "price_pressure", "competition_remedy", "mature_industry", "plant_divestment"),
        penalties=("cost", "competition", "mature_industry", "regulatory_remedy"),
        note="Packaging is mature and cyclical; M&A premium is not durable spread evidence by itself.",
    ),
    _target(
        "PACKAGING_CONSOLIDATION_REMEDY",
        E2RArchetype.PACKAGING_CONSOLIDATION_REMEDY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(14, 12, 10, 9, 6, 6, 10),
        stage1=("packaging_mna", "consolidation", "scale_economics_claim"),
        stage2=("competition_remedy", "plant_divestment", "mna_synergy", "cash_return"),
        stage3=("synergy_realization", "fcf_stable", "regulatory_remedy_completed", "cash_return"),
        stage4b=("mna_premium_crowded", "consolidation_synergy_overpriced"),
        stage4c=("plant_divestment", "regulatory_remedy_delay", "synergy_shortfall", "mature_industry_limit"),
        green=("synergy_realization", "fcf_stable", "cash_return", "regulatory_remedy_completed"),
        red=("plant_divestment", "regulatory_remedy_delay", "synergy_shortfall", "mature_industry_limit"),
        penalties=("regulatory_remedy", "plant_divestment", "synergy", "mature_industry"),
        note="Packaging M&A can support Stage 2, but competition remedies and divestments cap Green until FCF and synergy are proven.",
    ),
    _target(
        "ADVANCED_MATERIAL_SPECULATIVE_THEME",
        E2RArchetype.ADVANCED_MATERIAL_SPECULATIVE_THEME,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(5, 4, 5, 5, 4, 0, 10),
        stage1=("graphene_mxene_ferrite_superconductor_theme", "paper_or_preprint", "sns_theme"),
        stage2=("commercial_contract", "qualified_customer", "revenue_conversion"),
        stage3=("commercial_revenue", "repeat_customer", "fcf_path"),
        stage4b=("speculative_material_theme_overheat", "paper_only_price_run"),
        stage4c=("no_commercialization", "paper_only", "no_revenue", "dilution"),
        green=("commercial_contract", "revenue_conversion", "fcf_path"),
        red=("paper_only", "no_revenue", "theme_only", "no_commercialization", "dilution"),
        penalties=("commercialization", "customer_validation", "revenue", "dilution"),
        note="Advanced materials are RedTeam-first before commercial revenue and customer validation.",
    ),
    _target(
        "SPECULATIVE_SCIENCE_THEME",
        E2RArchetype.SPECULATIVE_SCIENCE_THEME,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(4, 3, 4, 4, 3, 0, 10),
        stage1=("paper_or_preprint", "sns_science_theme", "lab_result"),
        stage2=("independent_replication", "commercial_customer", "revenue_path"),
        stage3=("commercial_revenue", "repeat_customer", "fcf_path"),
        stage4b=("science_theme_overheat", "retail_crowding"),
        stage4c=("replication_failure", "commercial_product_absent", "no_customer", "dilution"),
        green=("commercial_revenue", "customer_validation", "fcf_path"),
        red=("replication_failure", "paper_only", "no_commercial_product", "no_revenue"),
        penalties=("replication", "commercial_product", "customer", "revenue"),
        note="Science themes are Red by default when only papers, preprints, or social-media narratives exist.",
    ),
    _target(
        "EVENT_PREMIUM_GOVERNANCE_OVERLAY",
        E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("tender_offer", "hostile_takeover", "governance_battle", "event_day_price_reaction"),
        stage2=("event_premium_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("event_premium_misclassified_as_structural", "capital_structure_risk", "governance_dispute"),
        green=(),
        red=("tender_offer", "governance_event", "event_premium", "capital_structure_risk"),
        penalties=("event_premium", "governance", "capital_structure", "hostile_takeover"),
        note="Tender offers and governance battles are RedTeam overlays, not EPS/FCF rerating evidence.",
        gate_only=True,
    ),
    _target(
        "COMMODITY_PRICE_4C_OVERLAY",
        E2RArchetype.COMMODITY_PRICE_4C_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("commodity_price_breakout_or_crash", "spread_reversal", "supply_restart", "dividend_change"),
        stage2=("commodity_4c_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("price_crash", "supply_restart", "dividend_cut", "capex_cut", "demand_destruction"),
        green=(),
        red=("price_crash", "supply_restart", "dividend_cut", "capex_cut", "demand_destruction"),
        penalties=("commodity_price", "supply_restart", "dividend", "capex"),
        note="Commodity price reversal, supply restart, and dividend cuts are 4C overlays, not positive score.",
        gate_only=True,
    ),
    _target(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("cap", "cap", "cap", "cap", "cap", "cap", "+"),
        stage1=("large_resource_contract", "offtake_contract", "price_floor_claim", "customer_confidential"),
        stage2=("disclosure_gap_detected",),
        stage3=("not_applicable_cap_only",),
        stage4b=("not_applicable_cap_only",),
        stage4c=("contract_value_missing", "price_terms_missing", "counterparty_undisclosed", "duration_missing"),
        green=(),
        red=("contract_value_missing", "price_terms_missing", "counterparty_undisclosed", "duration_missing"),
        penalties=("contract_value", "price_terms", "counterparty", "duration"),
        note="Resource contracts receive a Stage 3 cap when value, price terms, counterparty, or duration are not disclosed.",
        gate_only=True,
    ),
)


ROUND162_CASE_CANDIDATES: tuple[Round162CaseCandidate, ...] = (
    Round162CaseCandidate(
        "mp_materials_dod_price_floor_case",
        "RARE_METALS_PRICE_FLOOR_OFFTAKE",
        "MP",
        "MP Materials DoD price floor / offtake",
        "US",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("government_investment_400m", "price_floor", "offtake_contract_10y", "production_capacity", "supply_chain_security"),
        ("production_ramp_failure", "policy_dependency", "capex_execution_risk", "price_floor_policy_change"),
        "price_floor_offtake_green_candidate",
        "needs_exact_stage_date_backfill",
        ("round_162.md AP MP Materials Pentagon agreement",),
        "DoD investment, price floor, and offtake are strong Stage 2 ingredients, but the exact July 2025 stage date and price must be backfilled from source data.",
        (E2RArchetype.RARE_METALS_EXPORT_CONTROL_EVENT,),
    ),
    Round162CaseCandidate(
        "mp_materials_apple_magnet_contract_case",
        "RARE_EARTH_MAGNET_SUPPLY_CHAIN",
        "MP",
        "MP Materials Apple magnet supply chain",
        "US",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("apple_500m_contract", "apple_prepayment", "magnet_production_flag", "magnet_production_start_year_2027", "recycled_feedstock", "fort_worth_facility"),
        ("magnet_ramp_delay", "customer_qualification_failure", "feedstock_shortage", "policy_support_change"),
        "rare_earth_magnet_supply_chain_aligned",
        "needs_exact_stage_date_backfill",
        ("round_162.md AP MP Materials Apple magnet agreement",),
        "Apple magnet supply evidence is separate from raw rare-earth price evidence; Green still needs ramp-up, customer qualification, revenue, and FCF.",
        (E2RArchetype.RARE_METALS_PRICE_FLOOR_OFFTAKE,),
    ),
    Round162CaseCandidate(
        "mp_materials_capital_raise_dilution_case",
        "RARE_EARTH_CAPITAL_RAISE_DILUTION",
        "MP",
        "MP Materials $500M common stock offering after strategic contracts",
        "US",
        "4b_watch",
        None,
        None,
        None,
        date(2025, 7, 16),
        None,
        ("common_stock_offering_500m", "rare_earth_price_floor", "apple_contract", "dod_support", "ytd_price_runup_275pct"),
        ("share_dilution", "capex_funding_gap", "valuation_already_moved", "after_hours_drop_5_8pct"),
        "structural_resource_success_with_dilution_watch",
        "needs_price_backfill",
        ("round_162.md Reuters MP Materials $500M offering",),
        "Price floor and offtake can be strong Stage 2 evidence, but post-contract capital raise and dilution can turn the case into 4B/dilution watch.",
        (E2RArchetype.RARE_METALS_PRICE_FLOOR_OFFTAKE,),
    ),
    Round162CaseCandidate(
        "china_heavy_rare_earth_export_control_case",
        "RARE_METALS_EXPORT_CONTROL_EVENT",
        "RARE_EARTH_CONTROL_REF",
        "중국 heavy rare earth 수출통제",
        "GLOBAL",
        "event_premium",
        None,
        date(2026, 5, 13),
        None,
        None,
        None,
        ("rare_earth_export_control", "heavy_rare_earth_shortage", "geopolitical_bottleneck", "strategic_supply_chain"),
        ("price_only_rally", "no_production_capacity", "no_offtake", "policy_truce_or_relief"),
        "geopolitical_bottleneck_reference",
        "missing_direct_symbol_mapping",
        ("round_162.md Reuters rare-earth export controls",),
        "Export controls are macro bottleneck evidence, not company-level Green without production, offtake, and FCF.",
        (E2RArchetype.RARE_METALS_PRICE_FLOOR_OFFTAKE,),
    ),
    Round162CaseCandidate(
        "china_yttrium_dysprosium_terbium_delay_case",
        "RARE_METALS_EXPORT_CONTROL_EVENT",
        "RARE_EARTH_LICENSE_DELAY_REF",
        "중국 yttrium/dysprosium/terbium export approval delay",
        "GLOBAL",
        "event_premium",
        None,
        date(2026, 5, 15),
        None,
        None,
        None,
        ("yttrium_export_delay", "dysprosium_shortage", "terbium_shortage", "rare_earth_license_delay", "price_spike_multiple"),
        ("export_control_relief", "truce_extension", "price_normalization", "no_production_capacity"),
        "export_control_event_only",
        "missing_direct_symbol_mapping",
        ("round_162.md Reuters rare-earth approval delay",),
        "License delays are useful routing evidence, but they remain event evidence unless a company has production, customer contracts, and price-floor/offtake economics.",
        (E2RArchetype.RARE_METALS_PRICE_FLOOR_OFFTAKE,),
    ),
    Round162CaseCandidate(
        "copper_ai_grid_record_high_case",
        "COPPER_AI_GRID_STRUCTURAL_DEMAND",
        "COPPER_GRID_REF",
        "구리 AI 데이터센터·전력망 record high",
        "GLOBAL",
        "success_candidate",
        None,
        date(2026, 5, 11),
        None,
        date(2026, 5, 11),
        None,
        ("copper_price_record_high", "ai_datacenter_grid_demand", "deficit_forecast", "mine_disruption", "grid_modernization", "processing_input_cost_risk"),
        ("tariff_inventory_distortion", "stockpile_distortion", "mine_supply_recovery", "demand_destruction", "sulfuric_acid_cost_risk"),
        "copper_ai_grid_watch",
        "missing_direct_symbol_mapping",
        ("round_162.md WSJ copper record high",),
        "Copper has AI/grid demand evidence, but tariff inventory, mine recovery, and processing input cost must be audited before company-level Green.",
        (E2RArchetype.COPPER_PROCESSING_INPUT_COST_OVERLAY,),
    ),
    Round162CaseCandidate(
        "indonesia_nickel_hpal_sulfur_squeeze_case",
        "NICKEL_SULFUR_HPAL_INPUT_COST",
        "NICKEL_HPAL_REF",
        "Indonesia nickel HPAL sulfur input cost squeeze",
        "GLOBAL",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 14),
        ("battery_grade_nickel_demand", "indonesia_hpal_capacity", "nickel_price_rebound", "sulfur_import_dependency"),
        ("sulfur_shortage", "sulfuric_acid_spike", "hpal_capacity_cut", "processing_margin_squeeze", "input_cost_spike"),
        "nickel_price_up_but_hpal_margin_squeezed",
        "missing_direct_symbol_mapping",
        ("round_162.md Reuters sulfur squeeze Indonesian nickel sector",),
        "Nickel price can rise while HPAL processing economics deteriorate; sulfur and sulfuric acid costs must be audited before any Green interpretation.",
        (E2RArchetype.COMMODITY_PRICE_4C_OVERLAY,),
    ),
    Round162CaseCandidate(
        "mosaic_phosphate_sulfuric_acid_squeeze_case",
        "FERTILIZER_INPUT_COST_SULFURIC_ACID",
        "MOS",
        "Mosaic phosphate sulfuric-acid input-cost squeeze",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("phosphate_price_strength", "fertilizer_supply_tightness", "farmer_margin_pressure"),
        (
            "sulfuric_acid_spike",
            "sulfur_cost_spike",
            "ammonia_cost_spike",
            "urea_cost_spike",
            "production_curtailment",
            "guidance_withdrawal",
            "loss_reported",
            "capex_cut",
        ),
        "phosphate_price_good_but_input_cost_squeezed",
        "needs_exact_stage_date_backfill",
        ("round_162.md WSJ Mosaic sulfuric-acid input-cost squeeze",),
        "Fertilizer price strength can be overwhelmed by sulfuric acid, sulfur, ammonia, and urea costs; this is a 4C-watch overlay until exact stage date and price path are backfilled.",
        (E2RArchetype.COMMODITY_PRICE_4C_OVERLAY, E2RArchetype.AGRI_COMMODITY_INPUTS),
    ),
    Round162CaseCandidate(
        "barrick_record_gold_buyback_case",
        "PRECIOUS_METALS_SAFE_HAVEN_MINERS",
        "GOLD",
        "Barrick record gold and buyback",
        "US",
        "cyclical_success",
        None,
        date(2026, 5, 11),
        None,
        date(2026, 5, 11),
        None,
        ("record_gold_price", "realized_gold_price_4823", "aisc_1708", "net_income_growth", "buyback_3b"),
        ("gold_price_correction", "aisc_rise", "production_drop", "jurisdiction_risk"),
        "precious_metals_cyclical_success_candidate",
        "needs_price_backfill",
        ("round_162.md Reuters Barrick Q1 profit and buyback",),
        "Gold price, AISC control, and buyback are useful, but this stays cycle/Watch until durability is proven.",
        (E2RArchetype.GOLD_MINER_JURISDICTION_RERATING,),
    ),
    Round162CaseCandidate(
        "equinox_orla_gold_jurisdiction_case",
        "GOLD_MINER_JURISDICTION_RERATING",
        "EQX_ORLA_REF",
        "Equinox-Orla Canada-focused gold miner M&A",
        "GLOBAL",
        "success_candidate",
        None,
        date(2026, 5, 13),
        None,
        None,
        None,
        ("gold_mna_flag", "safe_jurisdiction_assets", "canada_us_assets", "jurisdiction_discount_narrows", "production_profile"),
        ("mna_dilution", "integration_risk", "gold_price_reversal", "production_miss"),
        "gold_miner_jurisdiction_rerating",
        "missing_direct_symbol_mapping",
        ("round_162.md Reuters Equinox Orla gold producer merger",),
        "Gold miner rerating can come from safer jurisdiction and M&A scale, but dilution, integration, production, and AISC still need validation.",
    ),
    Round162CaseCandidate(
        "posco_international_alaska_lng_20y_case",
        "GENERAL_TRADING_RESOURCE_INFRA",
        "047050",
        "POSCO International Alaska LNG 20년 계약",
        "KR",
        "success_candidate",
        None,
        date(2025, 12, 4),
        None,
        None,
        None,
        ("twenty_year_lng_supply", "lng_volume_1mtpa", "project_equity_investment", "pipeline_steel_supply", "energy_security"),
        ("fid_pending", "financing_risk", "lng_price_risk", "project_delay"),
        "general_trading_resource_infra_stage2_candidate",
        "needs_price_backfill",
        ("round_162.md Reuters POSCO Alaska LNG deal",),
        "Long LNG contract, project stake, and pipeline steel supply make stronger evidence than spot trading exposure.",
        (E2RArchetype.LNG_ENERGY_TRADING_DISTRIBUTION,),
    ),
    Round162CaseCandidate(
        "sk_innovation_refining_recovery_case",
        "REFINING_OIL_SPREAD",
        "096770",
        "SK Innovation 정유 흑자전환",
        "KR",
        "cyclical_success",
        None,
        date(2026, 5, 13),
        None,
        date(2026, 5, 13),
        None,
        ("refining_op_turnaround", "earnings_beat", "refining_recovery", "logistics_normalization_delay"),
        ("recovery_delay_warning", "refining_margin_reversal", "inventory_loss", "middle_east_event_fades"),
        "refining_cyclical_recovery_candidate",
        "needs_price_backfill",
        ("round_162.md Reuters SK Innovation Q1 profit",),
        "Strong OP recovery remains Watch because refining margin, inventory, and event duration still need validation.",
    ),
    Round162CaseCandidate(
        "lg_chem_lotte_chemical_oversupply_case",
        "CHEMICAL_SPREAD",
        "KR_CHEMICALS_REF",
        "LG Chem / Lotte Chemical 공급과잉",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 2, 7),
        ("chemical_spread_story",),
        ("china_middle_east_capacity_glut", "operating_loss", "op_profit_collapse", "spread_reversal", "supply_glut"),
        "chemical_spread_green_hard_counterexample",
        "needs_price_backfill",
        ("round_162.md Reuters Korean petrochemical oversupply",),
        "Chemical spread recovery is not structural Green when China/Middle East capacity crushes OP and FCF.",
    ),
    Round162CaseCandidate(
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
        ("lithium_price_crash", "mine_restart", "supply_rebound", "ev_demand_slowdown", "capex_cut"),
        "lithium_cycle_hard_counterexample",
        "missing_price_data",
        ("round_162.md Reuters lithium prices after crash",),
        "Lithium rebound is not structural Green when mine restarts and EV slowdown can cap prices.",
        (E2RArchetype.COMMODITY_PRICE_4C_OVERLAY,),
    ),
    Round162CaseCandidate(
        "bhp_iron_ore_profit_dividend_cut_case",
        "IRON_ORE_CHINA_DEMAND_CYCLE",
        "BHP",
        "BHP 철광석 이익·배당 축소",
        "AU",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 2, 18),
        ("iron_ore_cycle", "capital_return", "dividend_supported_by_fcf"),
        ("iron_ore_price_decline", "china_demand_weakness", "profit_downcycle", "dividend_cut"),
        "iron_ore_commodity_downcycle_4c",
        "needs_price_backfill",
        ("round_162.md FT BHP dividend cut",),
        "Large miners can lose capital-return support when commodity price and China demand weaken.",
        (E2RArchetype.COMMODITY_PRICE_4C_OVERLAY,),
    ),
    Round162CaseCandidate(
        "korea_zinc_tender_offer_event_case",
        "EVENT_PREMIUM_GOVERNANCE_OVERLAY",
        "010130",
        "Korea Zinc 공개매수 이벤트",
        "KR",
        "event_premium",
        None,
        date(2024, 9, 13),
        None,
        None,
        None,
        ("tender_offer", "governance_event", "event_day_price_reaction", "strategic_metal_exposure"),
        ("event_premium", "governance_dispute", "hostile_takeover", "fcf_not_verified"),
        "event_premium_misclassified",
        "needs_price_backfill",
        ("round_162.md Reuters Korea Zinc tender offer",),
        "Tender-offer price reaction must be separated from durable smelting-margin and FCF rerating.",
        (E2RArchetype.NONFERROUS_STRATEGIC_METALS,),
    ),
    Round162CaseCandidate(
        "korea_zinc_share_issue_probe_case",
        "EVENT_PREMIUM_GOVERNANCE_OVERLAY",
        "010130",
        "Korea Zinc 신주발행·감독당국 조사",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 10, 31),
        ("share_issuance_after_tender", "regulator_probe", "governance_event", "strategic_metal_exposure"),
        ("capital_structure_risk", "regulator_revision_order", "minority_shareholder_value_damage", "event_premium_misclassified_as_structural"),
        "governance_event_capital_structure_4c_watch",
        "needs_price_backfill",
        ("round_162.md Reuters Korea Zinc share issuance probe",),
        "Strategic-metal exposure cannot offset governance and capital-structure risk after a tender-offer event.",
        (E2RArchetype.NONFERROUS_STRATEGIC_METALS,),
    ),
    Round162CaseCandidate(
        "international_paper_ds_smith_divestment_case",
        "PAPER_PACKAGING_CYCLE",
        "IP_DS_SMITH_REF",
        "International Paper / DS Smith plant divestment",
        "EU",
        "event_premium",
        None,
        date(2025, 4, 14),
        None,
        None,
        None,
        ("packaging_mna", "consolidation", "competition_remedy", "plant_divestment"),
        ("mature_industry", "regulatory_divestiture", "price_pressure", "volume_decline"),
        "packaging_mature_consolidation_watch",
        "missing_public_price_data",
        ("round_162.md Reuters International Paper DS Smith divestment",),
        "Packaging consolidation is a Watch case; competition remedies and mature-industry limits cap Green quality.",
    ),
    Round162CaseCandidate(
        "international_paper_ds_smith_remedy_case",
        "PACKAGING_CONSOLIDATION_REMEDY",
        "IP_DS_SMITH_REMEDY_REF",
        "International Paper / DS Smith consolidation remedy",
        "EU",
        "event_premium",
        None,
        date(2025, 4, 14),
        None,
        None,
        None,
        ("packaging_mna", "competition_remedy", "plant_divestment", "mna_synergy_claim"),
        ("regulatory_divestiture", "synergy_shortfall", "mature_industry_limit", "price_pressure"),
        "packaging_consolidation_remedy_watch",
        "missing_public_price_data",
        ("round_162.md packaging consolidation remedy calibration",),
        "Packaging M&A can support Stage 2, but competition remedies, divestitures, and mature-industry limits cap Green until realized FCF is visible.",
        (E2RArchetype.PAPER_PACKAGING_CYCLE,),
    ),
    Round162CaseCandidate(
        "graphene_mxene_superconductor_theme_case",
        "ADVANCED_MATERIAL_SPECULATIVE_THEME",
        "ADV_MATERIAL_THEME_REF",
        "그래핀·맥신·초전도체 소재 테마",
        "GLOBAL",
        "overheat",
        None,
        None,
        None,
        None,
        None,
        ("paper_or_preprint", "sns_science_theme", "material_theme_keyword"),
        ("paper_only", "no_commercialization", "no_customer", "no_revenue", "theme_only"),
        "speculative_material_theme",
        "missing_price_data",
        ("round_162.md advanced material speculative theme note",),
        "Scientific-material themes are Red/Watch before customer validation, revenue recognition, and FCF path exist.",
        (E2RArchetype.SPECULATIVE_SCIENCE_THEME,),
    ),
)


ROUND162_PRICE_FIELDS: tuple[str, ...] = (
    "case_id", "symbol", "company_name", "primary_archetype", "secondary_archetypes",
    "stage1_date", "stage2_date", "stage3_date", "stage4b_date", "stage4c_date",
    "stage1_price", "stage2_price", "stage3_price", "stage4b_price", "stage4c_price", "peak_price", "peak_date",
    "MFE_30D", "MFE_90D", "MFE_180D", "MFE_1Y", "MFE_2Y",
    "MAE_30D", "MAE_90D", "MAE_180D", "MAE_1Y",
    "drawdown_after_peak", "below_stage2_price_flag", "below_stage3_price_flag",
    "commodity_type", "commodity_price_at_stage", "commodity_price_peak",
    "commodity_price_change_30D", "commodity_price_change_90D", "commodity_price_change_1Y",
    "product_spread_metric", "spread_change_30D", "spread_change_90D",
    "inventory_gain_loss", "refining_margin", "lubricants_mix_ratio", "chemical_spread", "steel_spread", "smelting_margin",
    "copper_price", "copper_production_volume", "copper_cash_cost", "copper_inventory_distortion_flag",
    "tariff_stockpile_flag", "mine_disruption_flag", "deficit_forecast_flag",
    "demand_destruction_flag", "sulfuric_acid_cost_change", "processing_input_cost_risk_flag",
    "sulfur_shortage_flag", "sulfur_import_dependency_pct", "hpal_capacity_cut_flag", "processing_margin_squeeze_flag",
    "fertilizer_price", "phosphate_price", "sulfuric_acid_cost", "sulfur_cost", "ammonia_cost", "urea_cost",
    "fertilizer_input_cost_squeeze_flag", "production_curtailment_flag", "guidance_withdrawal_flag",
    "revenue_revision_1q", "op_revision_1q", "eps_revision_1q", "eps_revision_1y", "fcf_margin",
    "dividend_change", "buyback_amount",
    "offtake_contract_flag", "offtake_contract_value", "offtake_duration_years",
    "price_floor_flag", "price_floor_level", "government_support_flag", "government_investment_amount",
    "capital_raise_flag", "common_stock_offering_amount", "share_dilution_flag", "ytd_price_runup_pct",
    "strategic_supply_chain_flag", "defense_customer_flag", "apple_or_bigtech_customer_flag",
    "prepayment_amount",
    "rare_earth_export_control_flag", "rare_earth_license_delay_flag", "yttrium_export_delay_flag",
    "dysprosium_shortage_flag", "terbium_shortage_flag", "export_control_truce_flag", "price_spike_multiple",
    "magnet_production_flag", "magnet_production_location", "magnet_customer",
    "magnet_production_start_year", "recycled_feedstock_flag", "customer_qualification_flag",
    "production_capacity", "capacity_ramp_up_date", "project_execution_risk_flag",
    "customer_contract_flag", "customer_concentration",
    "lithium_price_change", "mine_shutdown_flag", "mine_restart_flag", "ess_demand_support_flag",
    "sodium_ion_substitution_flag", "capex_cut_flag",
    "gold_realized_price", "aisc", "gold_production_volume", "jurisdiction_risk_flag", "safe_haven_demand_flag",
    "jurisdiction_quality_score", "gold_mna_flag", "mna_dilution_flag", "integration_risk_flag",
    "lng_contract_volume_mtpa", "lng_contract_duration_years", "fid_status",
    "project_equity_investment_flag", "pipeline_steel_supply_flag", "commodity_trading_margin",
    "tender_offer_flag", "governance_event_flag", "event_premium_flag", "hostile_takeover_flag",
    "share_issuance_after_tender_flag", "regulator_probe_flag", "regulator_revision_order_flag", "capital_structure_risk_flag",
    "oversupply_flag", "supply_glut_flag", "china_middle_east_capacity_flag", "dividend_cut_flag",
    "packaging_mna_flag", "competition_remedy_flag", "plant_divestment_flag", "mature_industry_flag",
    "speculative_material_theme_flag", "commercial_product_flag", "customer_validation_flag", "revenue_recognized_flag",
    "opendart_rcept_no", "opendart_detail_fetched_flag", "disclosure_confidence_score",
    "detail_parser_confidence", "disclosure_signal_class", "routine_disclosure_flag",
    "risk_disclosure_flag", "high_signal_disclosure_flag",
    "score_price_alignment", "price_validation_status", "review_notes",
)


def round162_target_for(target_id: str) -> Round162ScoreTarget | None:
    for target in ROUND162_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round162_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND162_CASE_CANDIDATES:
        target = round162_target_for(candidate.target_id)
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
                f"Round162 R4 Loop-10 case for {candidate.target_id}; "
                "commodity cycle, spread recovery, event premium, and strategic supply-chain rerating remain separated."
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
                "commodity_price_is_not_structural_evidence",
                "price_increase_is_not_company_level_green",
                "spread_recovery_needs_inventory_and_oversupply_check",
                "require_price_floor_offtake_production_fcf_for_rare_metals_green",
                "capital_raise_and_dilution_can_cap_strategic_resource_cases",
                "processing_input_cost_can_offset_metal_price_rally",
                "fertilizer_input_cost_can_offset_phosphate_price_rally",
                "event_premium_is_not_fcf_rerating",
                "do_not_invent_spread_offtake_price_floor_aisc_cash_cost_input_cost_fcf_or_stage_prices",
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


def round162_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND162_SCORE_TARGETS:
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
                "loop10_penalty_axes": "|".join(target.loop10_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round162_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND162_CASE_CANDIDATES:
        target = round162_target_for(candidate.target_id)
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


def round162_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "loop10_penalty_axes": "|".join(target.loop10_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND162_SCORE_TARGETS
    )


def round162_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round162_backfill": "true"} for field in ROUND162_PRICE_FIELDS)


def round162_base_score_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "component": row.component,
            "weight": str(row.weight),
            "interpretation": row.interpretation,
            "production_scoring_changed": "false",
        }
        for row in ROUND162_BASE_SCORE_WEIGHTS
    )


def round162_stage_cap_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "cap_id": row.cap_id,
            "max_stage": row.max_stage,
            "condition": row.condition,
            "example": row.example,
            "production_scoring_changed": "false",
        }
        for row in ROUND162_STAGE_CAPS
    )


def round162_score_stage_price_alignment_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "case_id": row.case_id,
            "score_stage": row.score_stage,
            "price_path_signal": row.price_path_signal,
            "verdict": row.verdict,
            "normalization_adjustment": row.normalization_adjustment,
            "production_scoring_changed": "false",
        }
        for row in ROUND162_SCORE_STAGE_PRICE_ALIGNMENT
    )


def round162_summary() -> dict[str, int | bool]:
    records = round162_case_records()
    return {
        "target_count": len(ROUND162_SCORE_TARGETS),
        "source_canonical_target_count": ROUND162_SOURCE_CANONICAL_TARGET_COUNT,
        "helper_overlay_target_count": len(ROUND162_SCORE_TARGETS) - ROUND162_SOURCE_CANONICAL_TARGET_COUNT,
        "case_candidate_count": len(records),
        "base_score_component_count": len(ROUND162_BASE_SCORE_WEIGHTS),
        "stage_cap_count": len(ROUND162_STAGE_CAPS),
        "score_stage_price_alignment_count": len(ROUND162_SCORE_STAGE_PRICE_ALIGNMENT),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND162_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND162_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND162_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND162_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round162_r4_loop10_reports(
    *,
    output_directory: str | Path = ROUND162_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND162_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND162_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round162_r4_loop10_materials_spread_strategic_summary.md",
        "case_matrix": output / "round162_r4_loop10_case_matrix.csv",
        "stage_date_plan": output / "round162_r4_loop10_stage_date_plan.csv",
        "green_guardrails": output / "round162_r4_loop10_green_guardrails.md",
        "risk_overlays": output / "round162_r4_loop10_risk_overlays.md",
        "price_validation_plan": output / "round162_r4_loop10_price_validation_plan.md",
        "price_fields": output / "round162_r4_loop10_price_fields.csv",
        "base_score_weights": output / "round162_r4_loop10_base_score_weights.csv",
        "stage_caps": output / "round162_r4_loop10_stage_caps.csv",
        "score_stage_price_alignment": output / "round162_r4_loop10_score_stage_price_alignment.csv",
        "score_stage_price_alignment_md": output / "round162_r4_loop10_score_stage_price_alignment.md",
    }
    _write_case_jsonl(round162_case_records(), cases)
    _write_rows(round162_score_profile_rows(), score_profiles)
    _write_rows(round162_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round162_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round162_price_field_rows(), paths["price_fields"])
    _write_rows(round162_base_score_weight_rows(), paths["base_score_weights"])
    _write_rows(round162_stage_cap_rows(), paths["stage_caps"])
    _write_rows(round162_score_stage_price_alignment_rows(), paths["score_stage_price_alignment"])
    paths["summary"].write_text(render_round162_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round162_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round162_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round162_price_validation_plan_markdown(), encoding="utf-8")
    paths["score_stage_price_alignment_md"].write_text(
        render_round162_score_stage_price_alignment_markdown(),
        encoding="utf-8",
    )
    return paths


def render_round162_summary_markdown() -> str:
    summary = round162_summary()
    lines = [
        "# Round-162 R4 Loop-10 Materials / Spread / Strategic Resources Summary",
        "",
        f"- source_round: `{ROUND162_SOURCE_ROUND_PATH}`",
        "- large_sector: `MATERIALS_SPREAD_STRATEGIC`",
        "- loop: `R4 Loop 10 / v10.0`",
        f"- target_count: {summary['target_count']}",
        f"- source_canonical_target_count: {summary['source_canonical_target_count']}",
        f"- helper_overlay_target_count: {summary['helper_overlay_target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- base_score_component_count: {summary['base_score_component_count']}",
        f"- stage_cap_count: {summary['stage_cap_count']}",
        f"- score_stage_price_alignment_count: {summary['score_stage_price_alignment_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- cyclical_success_count: {summary['cyclical_success_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
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
        "- R4 Loop 10 says price increase and structural rerating are different things.",
        "- Example: MP Materials DoD/Apple price floor and offtake evidence is strong Stage 2, but YTD +275% and a follow-on offering also create 4B/dilution watch.",
        "- Example: copper AI-grid demand can explain a record commodity price, but company-level Green still needs production, cash cost, FCF, and capital return.",
        "- Example: Barrick has realized gold price, AISC, earnings, and buyback evidence, but gold miner cases still need OHLCV and cycle validation.",
        "- Example: Korea Zinc tender-offer upside is event premium, not strategic-metal structural success.",
        "- Example: Mosaic phosphate can have a good price backdrop, but sulfuric acid, sulfur, ammonia, and urea costs can still force guidance withdrawal and 4C-watch.",
        "- Example: LG/Lotte petrochemical oversupply, lithium -86%, HPAL sulfur squeeze, and fertilizer input-cost squeeze are hard RedTeam references.",
    ]
    return "\n".join(lines) + "\n"


def render_round162_green_guardrail_markdown() -> str:
    lines = [
        "# Round-162 R4 Loop-10 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-10 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND162_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions) or 'not_applicable'} | {', '.join(target.loop10_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R4 Loop-10 v10.0 weights to production scoring yet.",
            "- Do not treat commodity price, spread recovery, tender offers, policy headlines, or science themes as Green evidence by themselves.",
            "- Do not invent spread, offtake, price floor, production capacity, AISC, cash cost, FCF, capital return, project FID, sulfur input cost, or stage prices.",
            "- Treat oversupply, mine restart, dividend cut, inventory distortion, event premium, capital raise, dilution, sulfur/HPAL input-cost squeeze, fertilizer sulfuric-acid squeeze, and no commercialization as RedTeam fields.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round162_risk_overlay_markdown() -> str:
    lines = [
        "# Round-162 R4 Loop-10 Risk Overlays",
        "",
        "- `STRUCTURAL_RESOURCE_SUCCESS`: price floor, offtake, government support, production, FCF, and capital allocation change the market frame.",
        "- `PRICE_FLOOR_OFFTAKE_GREEN_CANDIDATE`: rare metals/strategic resources have actual downside support and long purchase commitments.",
        "- `RARE_EARTH_DILUTION_WATCH`: strategic contracts are real, but follow-on offerings and CAPEX funding can cut the price path.",
        "- `RARE_EARTH_MAGNET_SUPPLY_CHAIN_ALIGNED`: magnet production, Apple/DoD or defense customers, recycled feedstock, and customer qualification are verified.",
        "- `EXPORT_CONTROL_EVENT_ONLY`: rare-earth export controls create bottleneck routing evidence, but not company-level Green without production, offtake, and FCF.",
        "- `COMMODITY_CYCLICAL_SUCCESS`: commodity price or spread worked, but durability is not proven.",
        "- `COPPER_AI_GRID_WATCH`: AI-grid demand is real, but copper remains exposed to inventory distortion and supply response.",
        "- `COPPER_INPUT_COST_RISK`: sulfuric acid, processing inputs, mine disruptions, or tariff inventory can squeeze margins despite high copper prices.",
        "- `NICKEL_HPAL_INPUT_COST_4C`: nickel price rises, but sulfur shortage and HPAL input costs can still crush processing margins.",
        "- `FERTILIZER_INPUT_COST_SQUEEZE`: phosphate or fertilizer pricing can look strong while sulfuric acid, sulfur, ammonia, and urea costs destroy margin and guidance.",
        "- `GOLD_MINER_JURISDICTION_RERATING`: safer jurisdictions and M&A scale can help, but dilution, integration, production, AISC, and gold reversal remain risks.",
        "- `SPREAD_RECOVERY_FALSE_GREEN`: refining, chemical, steel, or packaging spread recovery is scored before inventory and oversupply are checked.",
        "- `PACKAGING_CONSOLIDATION_REMEDY`: packaging M&A requires competition remedies, divestments, synergy, and FCF checks.",
        "- `EVENT_PREMIUM_MISCLASSIFIED`: tender offer, M&A, or governance event is being confused with EPS/FCF rerating.",
        "- `GOVERNANCE_CAPITAL_STRUCTURE_4C`: tender-offer follow-on issuance, regulator probe, or capital-structure damage can break the event thesis.",
        "- `COMMODITY_PRICE_4C`: commodity price collapse, mine restart, dividend cut, or oversupply breaks the thesis.",
        "- `SPECULATIVE_MATERIAL_THEME`: graphene, MXene, superconductor, ferrite, or science themes lack commercial revenue.",
        "",
        "Simple example: `희토류 가격 급등` is routing evidence. It is not Green if the company has no production, offtake, price floor, or FCF path.",
    ]
    return "\n".join(lines) + "\n"


def render_round162_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-162 R4 Loop-10 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare commodity price, product spread, inventory gain/loss, offtake, price floor, FCF, dividend/buyback, and price path.",
        "6. Mark event premium, oversupply, supply restart, stockpile distortion, dividend cut, fertilizer input-cost squeeze, M&A remedies, and no commercialization explicitly.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round162_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `price_floor_offtake_green_candidate`: price floor, offtake, government support, production, and FCF align.",
            "- `rare_earth_magnet_supply_chain_aligned`: magnet production, Apple/DoD customers, feedstock, and qualification align.",
            "- `geopolitical_bottleneck_reference`: export-control evidence is useful for routing, but not direct company-level Green.",
            "- `export_control_event_only`: rare-earth approval delay remains macro event evidence without production/offtake.",
            "- `commodity_cyclical_success`: price/spread worked, but structural durability remains unproven.",
            "- `copper_ai_grid_watch`: AI-grid demand helps, but copper price distortions and supply response remain.",
            "- `phosphate_price_good_but_input_cost_squeezed`: fertilizer pricing can fail when sulfuric acid, sulfur, ammonia, or urea costs overwhelm margin.",
            "- `gold_miner_jurisdiction_rerating`: safer mining jurisdictions and M&A scale are a Watch-to-Green path only with FCF and capital return.",
            "- `chemical_spread_green_hard_counterexample`: spread recovery failed due to oversupply and OP/FCF deterioration.",
            "- `event_premium_misclassified`: event-day price reaction should not be scored as FCF rerating.",
            "- `governance_event_capital_structure_4c_watch`: post-event capital structure or regulator risk can turn a premium into a thesis-break watch.",
            "- `speculative_material_theme`: science/materials theme needs commercial product, customer validation, and revenue.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round162_score_stage_price_alignment_markdown() -> str:
    lines = [
        "# Round-162 R4 Loop-10 Score / Stage / Price Alignment",
        "",
        "Round 162 checks whether R4 score interpretation matches the observed price, operating, and capital path.",
        "This is calibration material only; it does not change production scoring.",
        "",
        "| case | score-stage view | price-path signal | verdict | normalization adjustment |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in ROUND162_SCORE_STAGE_PRICE_ALIGNMENT:
        lines.append(
            "| "
            f"`{row.case_id}` | {row.score_stage} | {row.price_path_signal} | "
            f"{row.verdict} | {row.normalization_adjustment} |"
        )
    lines.extend(
        [
            "",
            "## Loop-10 Takeaway",
            "",
            "- Price increase and structural rerating are intentionally separated.",
            "- Raise price floor, offtake, government investment, realized price, AISC, buyback, jurisdiction rerating, and copper AI-grid bottleneck evidence.",
            "- Keep Stage 3 capped until company-level realized price, cash cost, production volume, FCF, capital return, and price-path alignment are visible.",
            "- Strengthen 4C gates for dilution, event-premium unwind, governance shock, oversupply, lithium crash, HPAL input-cost squeeze, and speculative science failure.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round162CaseCandidate) -> str:
    if "event_premium" in candidate.alignment_hint or candidate.case_type == "event_premium":
        return "price_moved_without_evidence"
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    if candidate.case_type in {"structural_success", "success_candidate", "cyclical_success"}:
        return "aligned"
    return "unknown"


def _rerating_result(candidate: Round162CaseCandidate) -> str:
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
    return "unknown" if candidate.case_type == "success_candidate" else "no_rerating"


def _score_weight_hint(target: Round162ScoreTarget) -> dict[str, float]:
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


__all__ = [
    "ROUND162_CASE_CANDIDATES",
    "ROUND162_DEFAULT_CASES_PATH",
    "ROUND162_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND162_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND162_PRICE_FIELDS",
    "ROUND162_BASE_SCORE_WEIGHTS",
    "ROUND162_SCORE_TARGETS",
    "ROUND162_SCORE_STAGE_PRICE_ALIGNMENT",
    "ROUND162_STAGE_CAPS",
    "Round162BaseScoreWeight",
    "Round162CaseCandidate",
    "Round162ScoreStagePriceAlignment",
    "Round162ScoreTarget",
    "Round162ScoreWeightDraft",
    "Round162StageCap",
    "render_round162_green_guardrail_markdown",
    "render_round162_price_validation_plan_markdown",
    "render_round162_risk_overlay_markdown",
    "render_round162_score_stage_price_alignment_markdown",
    "render_round162_summary_markdown",
    "round162_base_score_weight_rows",
    "round162_case_candidate_rows",
    "round162_case_records",
    "round162_price_field_rows",
    "round162_score_stage_price_alignment_rows",
    "round162_score_profile_rows",
    "round162_stage_cap_rows",
    "round162_stage_date_rows",
    "round162_summary",
    "round162_target_for",
    "write_round162_r4_loop10_reports",
]
