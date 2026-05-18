"""Round-181 R10 Loop-11 Korea construction, real-estate, and materials pack.

Round 181 keeps the R10 construction/real-estate/building-materials work
Korea-focused. It treats overseas EPC awards, PF relief, REIT yield, AI
data-center real-asset narratives, cement price hikes, and building-material
mix shifts as calibration evidence only. Production feature engineering,
scoring, staging, and RedTeam code must not import it.
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


ROUND181_SOURCE_ROUND_PATH = "docs/round/round_181.md"
ROUND181_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round181_r10_loop11_construction_real_estate_materials"
ROUND181_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r10_loop11_round181.jsonl"
ROUND181_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round181_r10_loop11_v11.csv"
ROUND181_SOURCE_CANONICAL_TARGET_IDS: tuple[str, ...] = (
    "OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA",
    "EPC_LOW_MARGIN_ORDER_OVERLAY",
    "AI_DATA_CENTER_REAL_ASSET_KOREA",
    "CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA",
    "PF_RESTRUCTURING_RELIEF_KOREA",
    "APARTMENT_QUALITY_SAFETY_OVERLAY",
    "LARGE_BUILDER_BALANCE_SHEET_DEFENSE",
    "K_REIT_DIVIDEND_COVERAGE",
    "LOGISTICS_REIT_OCCUPANCY_KOREA",
    "BUILDING_MATERIALS_PRICE_COST_KOREA",
    "CEMENT_REGULATORY_COLLUSION_OVERLAY",
    "HOME_INTERIOR_HOUSING_CYCLE",
    "DISCLOSURE_CONFIDENCE_CAP",
)
ROUND181_SOURCE_CANONICAL_TARGET_COUNT = len(ROUND181_SOURCE_CANONICAL_TARGET_IDS)


@dataclass(frozen=True)
class Round181ScoreWeightDraft:
    eps_fcf_noi_affo_conversion: int | str
    contract_asset_tenant_pf_visibility: int | str
    cash_conversion_cost_ratio_dividend_coverage: int | str
    pf_safety_quality_regulatory_risk: int | str
    early_price_path_validation: int | str
    market_mispricing_rerating_gap: int | str
    valuation_room_4b_runway: int | str

    def as_dict(self) -> dict[str, int | str]:
        return {
            "eps_fcf_noi_affo_conversion": self.eps_fcf_noi_affo_conversion,
            "contract_asset_tenant_pf_visibility": self.contract_asset_tenant_pf_visibility,
            "cash_conversion_cost_ratio_dividend_coverage": self.cash_conversion_cost_ratio_dividend_coverage,
            "pf_safety_quality_regulatory_risk": self.pf_safety_quality_regulatory_risk,
            "early_price_path_validation": self.early_price_path_validation,
            "market_mispricing_rerating_gap": self.market_mispricing_rerating_gap,
            "valuation_room_4b_runway": self.valuation_room_4b_runway,
        }


@dataclass(frozen=True)
class Round181ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round181ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop11_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.CONSTRUCTION_REAL_ESTATE_MATERIALS

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round181CaseCandidate:
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
class Round181BaseScoreWeight:
    component: str
    points: int
    loop11_direction: str
    reason: str


@dataclass(frozen=True)
class Round181StageCap:
    stage_band: str
    max_score: str
    required_evidence: tuple[str, ...]
    example_cases: tuple[str, ...]
    green_policy: str


@dataclass(frozen=True)
class Round181ScoreStagePriceAlignment:
    case_id: str
    detected_stage: str
    price_path_status: str
    verdict: str
    normalization_adjustment: str


def _weights(
    eps_fcf_noi_affo: int | str,
    visibility: int | str,
    cash_cost_dividend: int | str,
    risk: int | str,
    price: int | str,
    mispricing: int | str,
    valuation: int | str,
) -> Round181ScoreWeightDraft:
    return Round181ScoreWeightDraft(eps_fcf_noi_affo, visibility, cash_cost_dividend, risk, price, mispricing, valuation)


def _target(
    target_id: str,
    archetype: E2RArchetype,
    posture: Round10ThemePosture,
    weight: Round181ScoreWeightDraft,
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
) -> Round181ScoreTarget:
    return Round181ScoreTarget(target_id, archetype, posture, weight, stage1, stage2, stage3, stage4b, stage4c, green, red, penalties, note, gate_only)


def _d(value: str) -> date:
    return date.fromisoformat(value)


GATE_WEIGHT = _weights("gate", "gate", "gate", "gate", "gate", "gate", "gate")
CAP_WEIGHT = _weights("cap", "cap", "cap", "+", "cap", "cap", "cap")

ROUND181_BASE_SCORE_WEIGHTS: tuple[Round181BaseScoreWeight, ...] = (
    Round181BaseScoreWeight("eps_fcf_noi_affo_conversion", 24, "raise_cashflow_bodyweight", "Construction, REIT, and real-asset stories only matter when OP/EPS, FCF, NOI, or AFFO converts."),
    Round181BaseScoreWeight("contract_asset_tenant_pf_visibility", 20, "raise_visibility", "Contract amount, counterparty, period, tenant lease, occupancy, and project-level PF repair define Stage 2 visibility."),
    Round181BaseScoreWeight("cash_conversion_cost_ratio_dividend_coverage", 18, "raise_cash_quality", "Cost ratio, cash conversion, AFFO/share, dividend coverage, and refinancing rate separate Stage 2 from Stage 3."),
    Round181BaseScoreWeight("pf_safety_quality_regulatory_risk", 16, "hard_redteam_gate", "PF workout, safety accident, quality cost, business suspension, collusion, and dilution can break R10 immediately."),
    Round181BaseScoreWeight("early_price_path_validation", 8, "loop11_axis", "Stage 2 이후 60D MFE validates early Stage 3; Stage 2 이후 120D MFE helps detect 4B cooling."),
    Round181BaseScoreWeight("market_mispricing_rerating_gap", 8, "old_frame_check", "PF, low-margin EPC, yield, or housing-cycle discounts matter only after cash-flow evidence exists."),
    Round181BaseScoreWeight("valuation_room_4b_runway", 6, "cool_theme_rerating", "PF relief, AI data-center, REIT yield, and cement headlines can rerate faster than cash flow."),
)

ROUND181_STAGE_CAPS: tuple[Round181StageCap, ...] = (
    Round181StageCap(
        "Stage 1",
        "45",
        ("pf_support_package", "rate_cut_expectation", "overseas_epc_order", "ai_data_center_narrative", "reconstruction_policy", "cement_price_hike", "high_dividend_reit_headline"),
        ("samsung_ct_ai_data_center_option_no_contract_cap_case", "k_reit_dividend_coverage_ltv_refinancing_case"),
        "Headlines route research only; they do not prove contract economics, PF repair, NOI/AFFO, cost ratio, or safety quality.",
    ),
    Round181StageCap(
        "Stage 2",
        "70",
        ("contract_amount", "counterparty", "completion_date", "pf_refinancing", "project_normalization", "tenant_or_occupancy", "noi_affo", "price_pass_through"),
        ("samsung_ea_fadhili_epc_stage2_strong_case", "gs_construction_fadhili_epc_pf_quality_cap_case", "large_builder_pf_relief_balance_sheet_defense_case"),
        "Stage 2 can be strong, but Green waits for OP/EPS, cost ratio, cash conversion, PF exposure, or NOI/AFFO confirmation.",
    ),
    Round181StageCap(
        "Stage 3",
        "requires_5_of_8",
        ("contract_amount_counterparty_period_confirmed", "op_eps_revision_or_quarterly_op_beat", "cost_ratio_stable_or_improving", "cash_conversion_improves", "pf_exposure_decreases_or_refinancing_succeeds", "stage2_60d_mfe_20pct", "no_safety_quality_hard_issue", "valuation_not_overheated"),
        ("samsung_ea_fadhili_epc_stage2_strong_case", "logistics_reit_occupancy_green_possible_case"),
        "Stage 3 requires five of eight R10 conditions; contract, PF, AI data-center, REIT, or cement headlines alone cannot create Green.",
    ),
    Round181StageCap(
        "Stage 4B",
        "requires_3_of_5",
        ("stage2_120d_mfe_60pct", "pf_ratecut_ai_dc_reconstruction_basket_rally", "narrative_priced_before_contract", "op_eps_revision_cannot_follow_price", "high_dividend_low_pbr_ai_dc_keywords_crowded"),
        ("ai_data_center_no_contract_4b_watch_case", "k_reit_dividend_coverage_ltv_refinancing_case"),
        "Cool R10 candidates when price moves before contract economics, NOI/AFFO, cost ratio, or PF repair.",
    ),
    Round181StageCap(
        "Stage 4C",
        "hard_gate",
        ("pf_workout_or_debt_rescheduling", "major_safety_collapse_or_fatal_accident", "government_investigation_business_suspension_quality_cost", "contract_cancellation_delay_or_cost_ratio_deterioration", "reit_dividend_cut_ltv_spike_refinancing_failure", "no_data_center_tenant_or_contract", "cement_or_material_collusion_fines", "rights_offering_cb_bw_dilution"),
        ("taeyoung_construction_pf_workout_hard_4c_case", "hdc_hyundai_development_gwangju_collapse_hard_4c_case"),
        "One hard PF, safety, quality, tenant, dividend, regulatory, or dilution break can block unsafe Green.",
    ),
)

ROUND181_SCORE_TARGETS: tuple[Round181ScoreTarget, ...] = (
    _target(
        "OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA",
        E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(24, 22, 18, 12, 8, 8, 8),
        stage1=("middle_east_epc_recovery", "gas_infra_order", "overseas_order_headline"),
        stage2=("contract_amount", "counterparty", "completion_date", "price_reaction"),
        stage3=("cost_ratio_stable", "op_eps_revision", "cash_conversion_improves", "fcf_improves", "project_execution_clean"),
        stage4b=("large_contract_priced_before_margin", "epc_basket_crowded"),
        stage4c=("cost_ratio_deterioration", "construction_delay", "contract_cancellation", "low_margin_order"),
        green=("contract_amount", "counterparty", "completion_date", "cost_ratio_stable", "op_eps_revision", "cash_conversion_improves"),
        red=("cost_ratio_deterioration", "construction_delay", "contract_cancellation", "low_margin_order"),
        penalties=("cost_ratio", "cash_conversion", "low_margin_order", "delay"),
        note="Samsung E&A-style EPC can be Green-capable only after margin, OP/EPS, and cash conversion confirm.",
    ),
    _target(
        "EPC_LOW_MARGIN_ORDER_OVERLAY",
        E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("large_epc_contract", "long_term_project"),
        stage2=("contract_amount", "project_period", "revenue_recognition_schedule"),
        stage3=("not_green_if_cost_ratio_or_cash_conversion_missing",),
        stage4b=("contract_headline_priced_before_margin",),
        stage4c=("cost_overrun", "construction_delay", "low_margin_order", "cash_conversion_failure"),
        green=(),
        red=("cost_overrun", "construction_delay", "low_margin_order", "cash_conversion_failure"),
        penalties=("cost", "delay", "margin", "cash"),
        note="EPC size is Stage 2 evidence, not Stage 3 proof, until margin and cash are verified.",
        gate_only=True,
    ),
    _target(
        "AI_DATA_CENTER_REAL_ASSET_KOREA",
        E2RArchetype.AI_DATA_CENTER_REAL_ASSET_KOREA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(12, 18, 12, 16, 8, 14, 8),
        stage1=("openai_korea_data_center_plan", "aws_korea_data_center_investment", "samsung_affiliate_rally"),
        stage2=("actual_contract_option", "tenant_or_epc_candidate", "power_water_permitting_plan"),
        stage3=("binding_epc_contract", "tenant_lease", "noi_affo_or_op_eps_visible", "power_water_secured"),
        stage4b=("ai_data_center_name_only_rally", "construction_material_basket_rally"),
        stage4c=("actual_contract_missing", "tenant_missing", "power_water_permitting_failure", "noi_affo_missing"),
        green=("binding_epc_contract", "tenant_lease", "power_water_secured", "noi_affo_or_op_eps_visible"),
        red=("actual_contract_missing", "tenant_missing", "power_water_permitting_failure", "noi_affo_missing"),
        penalties=("no_contract", "no_tenant", "power_water", "noi_affo"),
        note="AI data-center demand is real asset option only until contract, tenant, power/water, and cash-flow ownership are source-backed.",
    ),
    _target(
        "CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA",
        E2RArchetype.CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("pf_stress", "rate_cut_expectation", "support_package"),
        stage2=("debt_rescheduling", "project_normalization", "guarantee_support"),
        stage3=("not_green_if_workout_or_bridge_loan_rollover_active",),
        stage4b=("pf_relief_rally_before_repair",),
        stage4c=("pf_workout", "debt_rescheduling", "bridge_loan_rollover_failure", "liquidity_crisis"),
        green=(),
        red=("pf_workout", "debt_rescheduling", "bridge_loan_rollover_failure", "liquidity_crisis"),
        penalties=("pf", "workout", "liquidity", "bridge_loan"),
        note="Korea construction credit is RedTeam-first; PF workout is a hard break, not recovery evidence.",
        gate_only=True,
    ),
    _target(
        "PF_RESTRUCTURING_RELIEF_KOREA",
        E2RArchetype.PF_RESTRUCTURING_RELIEF_KOREA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(12, 16, 16, 18, 8, 14, 6),
        stage1=("government_support_package", "guarantee_expansion", "market_stabilization_fund"),
        stage2=("pf_refinancing", "profitable_project_normalized", "bad_project_separated"),
        stage3=("pf_exposure_decreases", "cash_conversion_improves", "cost_ratio_stable", "op_eps_revision"),
        stage4b=("support_news_priced_as_recovery",),
        stage4c=("workout", "refinancing_failure", "delinquency_increase", "impairment"),
        green=("pf_exposure_decreases", "pf_refinancing", "cash_conversion_improves", "cost_ratio_stable"),
        red=("workout", "refinancing_failure", "delinquency_increase", "impairment"),
        penalties=("policy_only", "pf_exposure", "cash_conversion", "impairment"),
        note="PF support is Watch until project-level refinancing and cash conversion are proven.",
    ),
    _target(
        "APARTMENT_QUALITY_SAFETY_OVERLAY",
        E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("housing_brand", "presale_recovery"),
        stage2=("quality_recovery_plan", "compensation_plan"),
        stage3=("not_green_if_fatal_accident_or_quality_cost_active",),
        stage4b=("brand_recovery_priced_before_trust_repair",),
        stage4c=("fatal_collapse", "government_investigation", "business_suspension", "quality_cost", "brand_damage"),
        green=(),
        red=("fatal_collapse", "government_investigation", "business_suspension", "quality_cost", "brand_damage"),
        penalties=("safety", "quality", "investigation", "brand"),
        note="Residential builders cannot ignore safety and quality hard breaks.",
        gate_only=True,
    ),
    _target(
        "LARGE_BUILDER_BALANCE_SHEET_DEFENSE",
        E2RArchetype.LARGE_BUILDER_BALANCE_SHEET_DEFENSE,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(22, 18, 20, 16, 8, 10, 6),
        stage1=("large_builder_defense", "overseas_infra_mix", "pf_relief"),
        stage2=("balance_sheet_strength", "project_diversification", "guarantee_support", "cashflow_defense"),
        stage3=("pf_exposure_decreases", "cash_conversion_improves", "cost_ratio_stable", "op_eps_revision", "unsold_units_decline"),
        stage4b=("large_builder_relief_rally_crowded",),
        stage4c=("pf_delinquency", "cashflow_deterioration", "provision_increase", "cost_ratio_spike"),
        green=("pf_exposure_decreases", "cash_conversion_improves", "cost_ratio_stable", "op_eps_revision", "unsold_units_decline"),
        red=("pf_delinquency", "cashflow_deterioration", "provision_increase", "cost_ratio_spike"),
        penalties=("pf", "cash", "cost_ratio", "unsold_units"),
        note="Large builders can be Stage 2/3 candidates only when PF exposure and cash conversion improve.",
    ),
    _target(
        "K_REIT_DIVIDEND_COVERAGE",
        E2RArchetype.K_REIT_DIVIDEND_COVERAGE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(22, 20, 22, 14, 8, 8, 6),
        stage1=("rate_cut_expectation", "high_dividend_yield", "nav_discount"),
        stage2=("occupancy_stable", "noi_affo_visible", "ltv_managed", "refinancing_rate_stable"),
        stage3=("affo_per_share_improves", "dividend_coverage_stable", "ltv_stable", "occupancy_resilient"),
        stage4b=("yield_rally_before_affo", "rate_cut_priced"),
        stage4c=("dividend_cut", "ltv_spike", "refinancing_failure", "vacancy_increase"),
        green=("affo_per_share_improves", "dividend_coverage_stable", "ltv_stable", "occupancy_resilient"),
        red=("dividend_cut", "ltv_spike", "refinancing_failure", "vacancy_increase"),
        penalties=("dividend", "ltv", "refinancing", "occupancy"),
        note="K-REIT yield needs AFFO/share, dividend coverage, LTV, and refinancing support before Green.",
    ),
    _target(
        "LOGISTICS_REIT_OCCUPANCY_KOREA",
        E2RArchetype.LOGISTICS_REIT_OCCUPANCY_KOREA,
        Round10ThemePosture.GREEN_POSSIBLE,
        _weights(22, 22, 20, 12, 8, 8, 8),
        stage1=("logistics_asset_recovery", "rate_cut_expectation", "warehouse_demand"),
        stage2=("occupancy", "lease_rate", "tenant_quality", "noi_affo_visible"),
        stage3=("occupancy_resilient", "rental_growth", "affo_per_share_improves", "ltv_stable"),
        stage4b=("logistics_reit_rally_before_affo",),
        stage4c=("vacancy_increase", "tenant_default", "ltv_spike", "dividend_cut"),
        green=("occupancy_resilient", "rental_growth", "affo_per_share_improves", "ltv_stable"),
        red=("vacancy_increase", "tenant_default", "ltv_spike", "dividend_cut"),
        penalties=("vacancy", "tenant", "ltv", "dividend"),
        note="Logistics REIT can be Green-capable only with occupancy, rent, AFFO/share, and leverage evidence.",
    ),
    _target(
        "BUILDING_MATERIALS_PRICE_COST_KOREA",
        E2RArchetype.BUILDING_MATERIALS_PRICE_COST_KOREA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(20, 14, 20, 16, 8, 14, 8),
        stage1=("cement_price_hike", "housing_transaction_recovery", "product_mix_shift", "overseas_investment"),
        stage2=("price_pass_through", "energy_cost_stable", "volume_defended", "product_mix_improves"),
        stage3=("opm_fcf_improves", "volume_defended", "raw_material_cost_stable", "specialty_mix_margin"),
        stage4b=("price_hike_or_housing_cycle_rally",),
        stage4c=("volume_decline", "raw_material_cost_spike", "price_pass_through_failure", "integration_failure"),
        green=("opm_fcf_improves", "volume_defended", "raw_material_cost_stable", "specialty_mix_margin"),
        red=("volume_decline", "raw_material_cost_spike", "price_pass_through_failure", "integration_failure"),
        penalties=("volume", "raw_material", "housing_cycle", "integration"),
        note="Building-material stories need price-cost-volume and mix evidence, not housing-cycle headlines alone.",
    ),
    _target(
        "CEMENT_REGULATORY_COLLUSION_OVERLAY",
        E2RArchetype.CEMENT_REGULATORY_COLLUSION_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("cement_price_hike", "construction_starts_recovery"),
        stage2=("price_pass_through", "energy_cost_down"),
        stage3=("not_green_if_regulatory_collusion_or_volume_missing",),
        stage4b=("cement_price_hike_basket_rally",),
        stage4c=("collusion_fine", "regulatory_risk", "construction_starts_decline", "ready_mix_demand_decline"),
        green=(),
        red=("collusion_fine", "regulatory_risk", "construction_starts_decline", "ready_mix_demand_decline"),
        penalties=("collusion", "regulation", "volume", "starts"),
        note="Cement price pass-through is capped by volume and regulatory history.",
        gate_only=True,
    ),
    _target(
        "HOME_INTERIOR_HOUSING_CYCLE",
        E2RArchetype.HOME_INTERIOR_HOUSING_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _weights(18, 14, 18, 14, 8, 16, 12),
        stage1=("housing_transaction_recovery", "interior_demand", "remodeling_cycle"),
        stage2=("volume_recovery", "opm_improvement", "product_mix", "inventory_normalization"),
        stage3=("opm_fcf_improves", "housing_volume_defended", "working_capital_clean", "valuation_old_frame"),
        stage4b=("housing_cycle_rally_priced_before_margin",),
        stage4c=("transaction_decline", "inventory_buildup", "margin_compression", "raw_material_cost_spike"),
        green=("opm_fcf_improves", "housing_volume_defended", "working_capital_clean", "valuation_old_frame"),
        red=("transaction_decline", "inventory_buildup", "margin_compression", "raw_material_cost_spike"),
        penalties=("transaction", "inventory", "margin", "raw_material"),
        note="Interior and housing-cycle names stay Watch until OPM/FCF and working capital confirm.",
    ),
    _target(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        CAP_WEIGHT,
        stage1=("contract_pf_noi_affo_headline", "ai_data_center_headline", "cement_price_headline"),
        stage2=("contract_amount_required", "pf_detail_required", "noi_affo_required", "cost_ratio_required", "dividend_coverage_required"),
        stage3=("multi_source_confirmation", "detail_fields_verified", "cashflow_verified"),
        stage4b=("headline_rerating",),
        stage4c=("contract_amount_missing", "pf_detail_missing", "noi_affo_missing", "cost_ratio_missing", "dividend_coverage_missing"),
        green=("contract_amount", "pf_detail", "noi_affo", "cost_ratio", "dividend_coverage"),
        red=("contract_amount_missing", "pf_detail_missing", "noi_affo_missing", "cost_ratio_missing", "dividend_coverage_missing"),
        penalties=("disclosure", "detail", "cashflow", "parser_confidence"),
        note="OpenDART list or headline-only evidence caps R10 until contract, PF, NOI/AFFO, cost ratio, and dividend fields are parsed.",
    ),
)

ROUND181_SCORE_STAGE_PRICE_ALIGNMENT: tuple[Round181ScoreStagePriceAlignment, ...] = (
    Round181ScoreStagePriceAlignment("samsung_ea_fadhili_epc_stage2_strong_case", "Stage 2 strong", "Fadhili $6B Samsung E&A contract aligned with intraday +8.5% price reaction", "epc_stage2_strong_not_green_until_margin_cash", "score contract/counterparty/date as Stage 2; require cost ratio, OP/EPS, and cash conversion for Stage 3"),
    Round181ScoreStagePriceAlignment("gs_construction_fadhili_epc_pf_quality_cap_case", "Stage 2 plus PF/quality cap", "Fadhili award gives visibility, but housing PF and quality risks need caps", "epc_visibility_needs_builder_redteam", "attach PF, quality, and cost-ratio overlays before any Green evaluation"),
    Round181ScoreStagePriceAlignment("samsung_ct_ai_data_center_option_no_contract_cap_case", "Stage 1/2 option plus 4B-watch", "OpenAI/AWS Korea data-center news can move Samsung affiliates before contracts", "ai_dc_option_not_green_without_contract_tenant_noi", "cap at Watch until EPC/tenant/power/water/NOI ownership is verified"),
    Round181ScoreStagePriceAlignment("taeyoung_construction_pf_workout_hard_4c_case", "hard 4C", "Debt rescheduling and PF workout are thesis-break reference points", "pf_workout_hard_gate", "block Green immediately and treat support packages as relief events only"),
    Round181ScoreStagePriceAlignment("hdc_hyundai_development_gwangju_collapse_hard_4c_case", "hard 4C", "Fatal collapse, investigation, resignation, and faulty methods override housing recovery", "safety_quality_hard_gate", "safety and quality failures outrank backlog, brand, and housing-cycle evidence"),
)

ROUND181_CASE_CANDIDATES: tuple[Round181CaseCandidate, ...] = (
    Round181CaseCandidate(
        "samsung_ea_fadhili_epc_stage2_strong_case",
        "OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA",
        "028050",
        "Samsung E&A Fadhili EPC Stage 2 strong candidate",
        "KR",
        "success_candidate",
        None,
        _d("2024-04-02"),
        None,
        None,
        None,
        ("fadhili_gas_expansion", "saudi_aramco_customer", "7_7bn_usd_project", "samsung_ea_6bn_usd_contract", "completion_2027_11", "intraday_price_plus_8_5pct", "kospi_minus_1_4pct"),
        ("cost_ratio_unconfirmed", "cash_conversion_unconfirmed", "low_margin_order_risk"),
        "stage2_price_aligned_epc_not_green_until_margin_cash",
        "needs_cost_ratio_cash_conversion_op_eps_price_backfill",
        ("round_181.md Reuters Fadhili gas expansion", "round_181.md WSJ Samsung E&A contract reaction"),
        "Samsung E&A is the clean R10 Stage 2 example; Stage 3 waits for EPC margin, OP/EPS revision, and cash conversion.",
        (E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY,),
    ),
    Round181CaseCandidate(
        "gs_construction_fadhili_epc_pf_quality_cap_case",
        "OVERSEAS_EPC_CONTRACT_BACKLOG_KOREA",
        "006360",
        "GS Engineering & Construction Fadhili EPC with PF and quality cap",
        "KR",
        "success_candidate",
        None,
        _d("2024-04-02"),
        None,
        None,
        None,
        ("fadhili_project_awardee", "saudi_aramco_customer", "overseas_epc_recovery"),
        ("individual_contract_amount_missing", "epc_margin_unconfirmed", "housing_pf_exposure", "quality_cost_risk"),
        "stage2_epc_visibility_with_pf_quality_cap",
        "needs_contract_amount_margin_pf_quality_price_backfill",
        ("round_181.md Reuters Fadhili gas expansion",),
        "GS Construction gets Stage 2 visibility from Fadhili, but the builder-specific PF and quality gates remain active.",
        (E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY, E2RArchetype.PF_RESTRUCTURING_RELIEF_KOREA, E2RArchetype.APARTMENT_QUALITY_SAFETY_OVERLAY),
    ),
    Round181CaseCandidate(
        "samsung_ct_ai_data_center_option_no_contract_cap_case",
        "AI_DATA_CENTER_REAL_ASSET_KOREA",
        "028260",
        "Samsung C&T AI data-center real-asset option without contract cap",
        "KR",
        "event_premium",
        _d("2025-10-02"),
        _d("2025-10-29"),
        None,
        _d("2025-10-02"),
        None,
        ("openai_korea_data_center_plan", "samsung_affiliate_price_reaction", "aws_5bn_korea_data_center_investment", "20mw_two_data_centers"),
        ("actual_epc_contract_missing", "tenant_lease_missing", "power_water_permitting_unknown", "noi_affo_missing"),
        "ai_data_center_option_price_reaction_not_green_without_contract",
        "needs_epc_tenant_power_noi_affo_price_backfill",
        ("round_181.md Reuters OpenAI Samsung SK partnership", "round_181.md Reuters AWS Korea investment"),
        "Samsung C&T can be an AI real-asset option, but actual EPC contract, tenant, power/water, and NOI/AFFO are required before Stage 3.",
        (E2RArchetype.THEME_VALUATION_OVERHEAT,),
    ),
    Round181CaseCandidate(
        "large_builder_pf_relief_balance_sheet_defense_case",
        "LARGE_BUILDER_BALANCE_SHEET_DEFENSE",
        "000720/047040/375500",
        "Hyundai E&C Daewoo E&C DL E&C large-builder PF relief basket",
        "KR",
        "success_candidate",
        _d("2024-03-27"),
        _d("2024-03-27"),
        None,
        None,
        None,
        ("40_6tn_krw_support_package", "guarantee_expansion", "market_stabilization_fund", "large_builder_diversification"),
        ("pf_exposure_unconfirmed", "cash_conversion_unconfirmed", "unsold_units_risk", "cost_ratio_risk"),
        "large_builder_stage2_relief_not_green_until_pf_cash_repair",
        "needs_pf_exposure_cash_conversion_cost_ratio_price_backfill",
        ("round_181.md Reuters Korea support package",),
        "Large builders may defend better than small builders, but PF exposure, cash conversion, unsold units, and cost ratio decide Stage 3.",
        (E2RArchetype.PF_RESTRUCTURING_RELIEF_KOREA,),
    ),
    Round181CaseCandidate(
        "k_reit_dividend_coverage_ltv_refinancing_case",
        "K_REIT_DIVIDEND_COVERAGE",
        "395400/365550/330590",
        "SK REIT ESR Kendall Square REIT Lotte REIT dividend coverage gate",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("high_dividend_reit", "rate_cut_expectation", "occupancy_needed", "noi_affo_needed"),
        ("dividend_coverage_missing", "ltv_risk", "refinancing_rate_risk", "occupancy_missing"),
        "reit_yield_stage2_watch_not_green_until_affo_ltv",
        "needs_occupancy_noi_affo_dividend_ltv_price_backfill",
        ("round_181.md K-REIT dividend coverage section",),
        "K-REITs need occupancy, NOI/AFFO/share, dividend coverage, LTV, and refinancing rate before Green.",
        (E2RArchetype.LOGISTICS_REIT_OCCUPANCY_KOREA,),
    ),
    Round181CaseCandidate(
        "logistics_reit_occupancy_green_possible_case",
        "LOGISTICS_REIT_OCCUPANCY_KOREA",
        "365550",
        "ESR Kendall Square REIT logistics occupancy green-possible gate",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("logistics_asset_recovery", "occupancy_needed", "lease_rate_needed", "tenant_quality_needed", "noi_affo_needed"),
        ("vacancy_risk", "tenant_default_risk", "ltv_risk", "dividend_coverage_missing"),
        "logistics_reit_can_improve_if_occupancy_affo_ltv_confirm",
        "needs_occupancy_rent_affo_ltv_price_backfill",
        ("round_181.md logistics REIT section",),
        "Logistics REIT is Green-capable only after occupancy, rent, AFFO/share, LTV, and dividend coverage are verified.",
    ),
    Round181CaseCandidate(
        "kcc_kccglass_lxhausys_material_mix_cycle_case",
        "BUILDING_MATERIALS_PRICE_COST_KOREA",
        "002380/344820/108670",
        "KCC KCC Glass LX Hausys building-material mix and housing-cycle cap",
        "KR",
        "success_candidate",
        None,
        _d("2025-04-28"),
        None,
        None,
        None,
        ("momentive_integration", "silicone_specialty_mix", "kcc_glass_indonesia_investment_option", "building_material_product_mix"),
        ("housing_cycle_risk", "raw_material_cost_risk", "integration_risk", "volume_missing"),
        "building_material_mix_stage2_not_green_until_volume_opm_fcf",
        "needs_volume_raw_material_opm_fcf_price_backfill",
        ("round_181.md Momentive case", "round_181.md Reuters Indonesia investment case"),
        "KCC-type building-material names need product mix, volume, OPM/FCF, raw-material cost, and integration evidence.",
        (E2RArchetype.HOME_INTERIOR_HOUSING_CYCLE,),
    ),
    Round181CaseCandidate(
        "taeyoung_construction_pf_workout_hard_4c_case",
        "CONSTRUCTION_REAL_ESTATE_CREDIT_KOREA",
        "009410",
        "Taeyoung Construction PF workout hard 4C reference",
        "KR",
        "4c_thesis_break",
        None,
        _d("2024-03-27"),
        None,
        None,
        _d("2024-03-27"),
        ("pf_support_context", "debt_rescheduling_reference"),
        ("pf_workout_flag", "debt_rescheduling", "liquidity_crisis", "shareholder_dilution_or_creditor_control"),
        "pf_workout_is_hard_4c_not_recovery",
        "needs_pf_workout_event_price_backfill",
        ("round_181.md Reuters Korea support package and Taeyoung debt rescheduling context",),
        "Taeyoung is the R10 PF hard break reference; support packages are relief context, not Stage 3 evidence.",
    ),
    Round181CaseCandidate(
        "hdc_hyundai_development_gwangju_collapse_hard_4c_case",
        "APARTMENT_QUALITY_SAFETY_OVERLAY",
        "294870",
        "HDC Hyundai Development Gwangju collapse hard quality 4C",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        _d("2022-01-11"),
        ("housing_brand_recovery_prior",),
        ("fatal_collapse_6_deaths", "government_investigation", "chairman_resignation", "faulty_method_and_materials", "brand_damage"),
        "safety_quality_hard_4c",
        "needs_collapse_event_price_quality_cost_backfill",
        ("round_181.md Gwangju Hwajeong I-Park collapse reference",),
        "A fatal apartment collapse immediately blocks Green regardless of housing-cycle or brand recovery evidence.",
    ),
    Round181CaseCandidate(
        "hanil_cement_price_pass_collusion_regulatory_cap_case",
        "BUILDING_MATERIALS_PRICE_COST_KOREA",
        "300720/004980",
        "Hanil Cement and Sungshin Cement price pass-through with collusion cap",
        "KR",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("cement_price_hike", "energy_cost_down_option", "price_pass_through_signal"),
        ("collusion_penalty_history", "volume_missing", "construction_start_cycle", "regulatory_risk"),
        "cement_price_hike_not_green_without_volume_regulatory_clearance",
        "needs_volume_energy_cost_regulatory_price_backfill",
        ("round_181.md Hanil Cement collusion history",),
        "Cement price hikes can be Stage 2 evidence, but volume and regulatory history cap Stage 3.",
        (E2RArchetype.CEMENT_REGULATORY_COLLUSION_OVERLAY,),
    ),
    Round181CaseCandidate(
        "ai_data_center_no_contract_4b_watch_case",
        "AI_DATA_CENTER_REAL_ASSET_KOREA",
        "KR_R10_AI_DC_BASKET",
        "Korea AI data-center real-asset basket without contract",
        "KR",
        "4b_watch",
        _d("2025-10-02"),
        _d("2025-10-29"),
        None,
        _d("2025-10-02"),
        None,
        ("openai_aws_korea_data_center_macro", "construction_materials_basket_rally_option"),
        ("actual_contract_missing", "tenant_missing", "power_water_permitting_unknown", "noi_affo_missing"),
        "ai_data_center_name_only_is_4b_watch_not_green",
        "needs_contract_tenant_power_water_noi_affo_backfill",
        ("round_181.md OpenAI and AWS AI data-center macro",),
        "AI data-center macro demand can create a basket rally, but no contract/no tenant/no NOI-AFFO remains 4B-watch.",
        (E2RArchetype.THEME_VALUATION_OVERHEAT,),
    ),
    Round181CaseCandidate(
        "epc_low_margin_order_overlay_case",
        "EPC_LOW_MARGIN_ORDER_OVERLAY",
        "KR_R10_EPC_BASKET",
        "Korea EPC low-margin order overlay",
        "KR",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("large_epc_contract_amount", "long_term_project"),
        ("cost_ratio_unconfirmed", "construction_delay_risk", "low_margin_order_risk", "cash_conversion_missing"),
        "large_order_not_green_if_margin_cash_missing",
        "needs_epc_margin_cash_conversion_backfill",
        ("round_181.md EPC low-margin order overlay",),
        "Large EPC order size must be paired with margin, execution, and cash conversion before Stage 3.",
    ),
    Round181CaseCandidate(
        "r10_disclosure_confidence_cap_case",
        "DISCLOSURE_CONFIDENCE_CAP",
        "KR_R10_DISCLOSURE_BASKET",
        "Korea R10 disclosure confidence cap basket",
        "KR",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("contract_pf_noi_affo_headline",),
        ("contract_amount_missing", "pf_detail_missing", "noi_affo_missing", "cost_ratio_missing", "dividend_coverage_missing"),
        "disclosure_detail_missing_cap",
        "needs_contract_pf_noi_affo_cost_dividend_backfill",
        ("round_181.md R10 disclosure confidence cap",),
        "R10 headline evidence is capped when contract amount, PF detail, NOI/AFFO, cost ratio, or dividend coverage is missing.",
    ),
)

ROUND181_PRICE_FIELDS: tuple[str, ...] = (
    "ticker",
    "company_name",
    "stage1_date",
    "stage2_date",
    "stage3_date",
    "stage4b_date",
    "stage4c_date",
    "stage1_trigger",
    "stage2_trigger",
    "stage3_trigger",
    "stage4b_trigger",
    "stage4c_trigger",
    "price_at_stage1",
    "price_at_stage2",
    "price_at_stage3",
    "price_at_stage4b",
    "price_at_stage4c",
    "return_1d_after_event",
    "return_5d_after_event",
    "return_20d_after_stage2",
    "return_60d_after_stage2",
    "return_120d_after_stage2",
    "return_252d_after_stage2",
    "mfe_60d_after_stage2",
    "mae_60d_after_stage2",
    "mfe_120d_after_stage2",
    "mae_120d_after_stage2",
    "mfe_252d_after_stage2",
    "mae_252d_after_stage2",
    "relative_strength_vs_kospi",
    "relative_strength_vs_construction_basket",
    "relative_strength_vs_reit_basket",
    "relative_strength_vs_building_materials_basket",
    "contract_amount",
    "contract_counterparty",
    "contract_period",
    "project_completion_date",
    "contract_amount_to_prior_sales",
    "backlog",
    "cost_ratio",
    "op_revision_before_stage3",
    "op_revision_after_stage3",
    "eps_revision_before_stage3",
    "eps_revision_after_stage3",
    "cash_conversion_signal",
    "pf_exposure",
    "pf_refinancing_success_flag",
    "bridge_loan_exposure",
    "unsold_units_signal",
    "workout_flag",
    "debt_rescheduling_flag",
    "tenant_lease_flag",
    "occupancy",
    "noi",
    "affo",
    "affo_per_share",
    "dividend_coverage",
    "ltv",
    "refinancing_rate",
    "safety_accident_flag",
    "fatal_accident_flag",
    "government_investigation_flag",
    "quality_cost_flag",
    "business_suspension_flag",
    "building_material_volume",
    "price_pass_through_signal",
    "energy_cost_signal",
    "regulatory_collusion_flag",
    "disclosure_confidence",
    "valuation_at_stage3",
    "valuation_at_stage4b",
)


def round181_target_for(target_id: str) -> Round181ScoreTarget | None:
    for target in ROUND181_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round181_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND181_CASE_CANDIDATES:
        target = round181_target_for(candidate.target_id)
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
                f"Round181 R10 Loop-11 case for {candidate.target_id}; "
                "Korea construction, real-estate, REIT, AI data-center, and building-material headlines are separated from contract, PF, NOI/AFFO, cost ratio, safety, regulatory, and price-path evidence."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage2_signals or field in target.green_conditions),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage3_conditions or field in target.green_conditions),
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
                "construction_pf_reit_ai_dc_headline_is_not_stage3",
                "require_contract_cost_cash_pf_or_noi_affo_evidence_for_green",
                "stage3_early_catch_requires_5_of_8_loop11_conditions",
                "do_not_invent_contract_amount_pf_noi_affo_cost_ratio_stage_prices_or_mfe_mae",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.75 if candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.2,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round181_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND181_SCORE_TARGETS:
        weights = target.score_weight.as_dict()
        rows.append(
            {
                "target_id": target.target_id,
                "large_sector": target.large_sector.value,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "eps_fcf_noi_affo_conversion": str(weights["eps_fcf_noi_affo_conversion"]),
                "contract_asset_tenant_pf_visibility": str(weights["contract_asset_tenant_pf_visibility"]),
                "cash_conversion_cost_ratio_dividend_coverage": str(weights["cash_conversion_cost_ratio_dividend_coverage"]),
                "pf_safety_quality_regulatory_risk": str(weights["pf_safety_quality_regulatory_risk"]),
                "early_price_path_validation": str(weights["early_price_path_validation"]),
                "market_mispricing_rerating_gap": str(weights["market_mispricing_rerating_gap"]),
                "valuation_room_4b_runway": str(weights["valuation_room_4b_runway"]),
                "stage1_signals": "|".join(target.stage1_signals),
                "stage2_signals": "|".join(target.stage2_signals),
                "stage3_conditions": "|".join(target.stage3_conditions),
                "stage4b_conditions": "|".join(target.stage4b_conditions),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "loop11_penalty_axes": "|".join(target.loop11_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round181_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND181_CASE_CANDIDATES:
        target = round181_target_for(candidate.target_id)
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


def round181_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "red_flags": "|".join(target.red_flags),
            "loop11_penalty_axes": "|".join(target.loop11_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND181_SCORE_TARGETS
    )


def round181_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round181_backfill": "true"} for field in ROUND181_PRICE_FIELDS)


def round181_base_score_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "component": item.component,
            "points": str(item.points),
            "loop11_direction": item.loop11_direction,
            "reason": item.reason,
            "production_scoring_changed": "false",
        }
        for item in ROUND181_BASE_SCORE_WEIGHTS
    )


def round181_stage_cap_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "stage_band": item.stage_band,
            "max_score": item.max_score,
            "required_evidence": "|".join(item.required_evidence),
            "example_cases": "|".join(item.example_cases),
            "green_policy": item.green_policy,
            "production_scoring_changed": "false",
        }
        for item in ROUND181_STAGE_CAPS
    )


def round181_score_stage_price_alignment_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "case_id": item.case_id,
            "detected_stage": item.detected_stage,
            "price_path_status": item.price_path_status,
            "verdict": item.verdict,
            "normalization_adjustment": item.normalization_adjustment,
            "production_scoring_changed": "false",
        }
        for item in ROUND181_SCORE_STAGE_PRICE_ALIGNMENT
    )


def round181_summary() -> dict[str, int | bool]:
    records = round181_case_records()
    return {
        "target_count": len(ROUND181_SCORE_TARGETS),
        "source_canonical_target_count": ROUND181_SOURCE_CANONICAL_TARGET_COUNT,
        "case_candidate_count": len(records),
        "base_score_component_count": len(ROUND181_BASE_SCORE_WEIGHTS),
        "stage_cap_count": len(ROUND181_STAGE_CAPS),
        "score_stage_price_alignment_count": len(ROUND181_SCORE_STAGE_PRICE_ALIGNMENT),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND181_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND181_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND181_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND181_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round181_r10_loop11_reports(
    *,
    output_directory: str | Path = ROUND181_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND181_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND181_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round181_r10_loop11_construction_real_estate_materials_summary.md",
        "case_matrix": output / "round181_r10_loop11_case_matrix.csv",
        "stage_date_plan": output / "round181_r10_loop11_stage_date_plan.csv",
        "green_guardrails": output / "round181_r10_loop11_green_guardrails.md",
        "risk_overlays": output / "round181_r10_loop11_risk_overlays.md",
        "price_validation_plan": output / "round181_r10_loop11_price_validation_plan.md",
        "price_fields": output / "round181_r10_loop11_price_fields.csv",
        "base_score_weights": output / "round181_r10_loop11_base_score_weights.csv",
        "stage_caps": output / "round181_r10_loop11_stage_caps.csv",
        "score_stage_price_alignment": output / "round181_r10_loop11_score_stage_price_alignment.csv",
        "score_stage_price_alignment_md": output / "round181_r10_loop11_score_stage_price_alignment.md",
    }
    _write_case_jsonl(round181_case_records(), cases)
    _write_rows(round181_score_profile_rows(), score_profiles)
    _write_rows(round181_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round181_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round181_price_field_rows(), paths["price_fields"])
    _write_rows(round181_base_score_weight_rows(), paths["base_score_weights"])
    _write_rows(round181_stage_cap_rows(), paths["stage_caps"])
    _write_rows(round181_score_stage_price_alignment_rows(), paths["score_stage_price_alignment"])
    paths["summary"].write_text(render_round181_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round181_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round181_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round181_price_validation_plan_markdown(), encoding="utf-8")
    paths["score_stage_price_alignment_md"].write_text(render_round181_score_stage_price_alignment_markdown(), encoding="utf-8")
    return paths


def render_round181_summary_markdown() -> str:
    summary = round181_summary()
    lines = [
        "# Round-181 R10 Loop-11 Korea Construction / Real Estate / Materials Summary",
        "",
        f"- source_round: `{ROUND181_SOURCE_ROUND_PATH}`",
        "- large_sector: `CONSTRUCTION_REAL_ESTATE_MATERIALS`",
        "- loop: `R10 Loop 11 / v11.0`",
        f"- target_count: {summary['target_count']}",
        f"- source_canonical_target_count: {summary['source_canonical_target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- base_score_component_count: {summary['base_score_component_count']}",
        f"- stage_cap_count: {summary['stage_cap_count']}",
        f"- score_stage_price_alignment_count: {summary['score_stage_price_alignment_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
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
        "- R10 Loop 11 separates EPC, PF support, REIT yield, AI data-center, cement, and building-material headlines from cash-flow evidence.",
        "- Example: Samsung E&A Fadhili is Stage 2 strong, but Green waits for cost ratio, OP/EPS, and cash conversion.",
        "- Example: Samsung C&T AI data-center optionality stays Watch until contract, tenant, power/water, and NOI/AFFO are source-backed.",
        "- Example: Taeyoung PF workout and HDC Gwangju collapse are hard 4C reference cases.",
    ]
    return "\n".join(lines) + "\n"


def render_round181_green_guardrail_markdown() -> str:
    lines = [
        "# Round-181 R10 Loop-11 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-11 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND181_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.loop11_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R10 Loop-11 v11.0 weights to production scoring yet.",
            "- Do not treat EPC order, PF support, rate-cut expectation, AI data-center headline, REIT yield, or cement price hike as Green evidence by itself.",
            "- Do not invent contract amount, PF exposure, NOI/AFFO, cost ratio, dividend coverage, stage prices, or MFE/MAE.",
            "- Green requires contract/PF/NOI/AFFO or cost evidence, clean safety and quality status, and price-path support.",
            "- PF workout, fatal accident, quality cost, dividend cut, no tenant, collusion, and disclosure confidence failures remain RedTeam gates.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round181_risk_overlay_markdown() -> str:
    lines = [
        "# Round-181 R10 Loop-11 Risk Overlays",
        "",
        "| target | stage4c conditions | red flags |",
        "| --- | --- | --- |",
    ]
    for target in ROUND181_SCORE_TARGETS:
        if target.red_flags or target.gate_only:
            lines.append(f"| `{target.target_id}` | {', '.join(target.stage4c_conditions)} | {', '.join(target.red_flags)} |")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- R10 is especially sensitive to PF, safety, quality, dividend coverage, tenant, and regulatory breaks.",
            "- Example: PF support without project refinancing is relief, not Stage 3 evidence.",
            "- Example: REIT yield without AFFO/share and dividend coverage can become 4B-watch.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round181_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-181 R10 Loop-11 Price Validation Plan",
        "",
        "R10 needs event-date price-path validation because contracts, PF events, tenant evidence, safety events, and cement pricing can move prices before fundamentals confirm.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND181_PRICE_FIELDS)
    lines.extend(
        [
            "",
            "## Case Backfill Priorities",
            "",
            "- `samsung_ea_fadhili_epc_stage2_strong_case`: cost ratio, cash conversion, OP/EPS revision, and Fadhili event price path.",
            "- `gs_construction_fadhili_epc_pf_quality_cap_case`: individual contract amount, EPC margin, PF exposure, and quality cost.",
            "- `samsung_ct_ai_data_center_option_no_contract_cap_case`: EPC contract, tenant lease, power/water/permitting, NOI/AFFO, and price-path reaction.",
            "- `k_reit_dividend_coverage_ltv_refinancing_case`: occupancy, NOI, AFFO/share, dividend coverage, LTV, and refinancing rate.",
            "- `taeyoung_construction_pf_workout_hard_4c_case`: workout/debt-rescheduling event date and price reaction.",
            "- `hdc_hyundai_development_gwangju_collapse_hard_4c_case`: safety accident date, quality cost, investigation, and brand impact.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round181_score_stage_price_alignment_markdown() -> str:
    lines = [
        "# Round-181 R10 Loop-11 Score / Stage / Price Alignment",
        "",
        "| case | detected stage | price path status | verdict | adjustment |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in ROUND181_SCORE_STAGE_PRICE_ALIGNMENT:
        lines.append(f"| `{row.case_id}` | {row.detected_stage} | {row.price_path_status} | {row.verdict} | {row.normalization_adjustment} |")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Samsung E&A and GS Construction show why EPC Stage 2 evidence needs margin and cash validation.",
            "- Samsung C&T and AI data-center baskets show why narrative can be 4B-watch before contracts.",
            "- Taeyoung and HDC show why PF, safety, and quality can override headline recovery immediately.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_weight_hint(target: Round181ScoreTarget) -> Mapping[str, float]:
    values: dict[str, float] = {}
    for key, value in target.score_weight.as_dict().items():
        if isinstance(value, int):
            values[key] = float(value)
    return values


def _score_price_alignment(candidate: Round181CaseCandidate) -> str:
    if candidate.case_type == "event_premium":
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    if candidate.case_type == "failed_rerating":
        return "evidence_good_but_price_failed"
    if candidate.case_type == "4b_watch":
        return "price_moved_without_evidence"
    return "unknown"


def _rerating_result(candidate: Round181CaseCandidate) -> str:
    if candidate.case_type == "event_premium":
        return "event_premium"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "failed_rerating":
        return "no_rerating"
    if candidate.case_type == "4b_watch":
        return "theme_overheat"
    return "unknown"


def _write_case_jsonl(records: Iterable[E2RCaseRecord], path: Path) -> None:
    lines = []
    for record in records:
        record.validate()
        lines.append(json.dumps(record.as_dict(), ensure_ascii=False, sort_keys=True))
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> None:
    rows = tuple(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


__all__ = [
    "ROUND181_BASE_SCORE_WEIGHTS",
    "ROUND181_CASE_CANDIDATES",
    "ROUND181_DEFAULT_CASES_PATH",
    "ROUND181_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND181_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND181_PRICE_FIELDS",
    "ROUND181_SCORE_STAGE_PRICE_ALIGNMENT",
    "ROUND181_SCORE_TARGETS",
    "ROUND181_SOURCE_CANONICAL_TARGET_COUNT",
    "ROUND181_SOURCE_CANONICAL_TARGET_IDS",
    "ROUND181_STAGE_CAPS",
    "render_round181_green_guardrail_markdown",
    "render_round181_price_validation_plan_markdown",
    "render_round181_risk_overlay_markdown",
    "render_round181_score_stage_price_alignment_markdown",
    "render_round181_summary_markdown",
    "round181_base_score_weight_rows",
    "round181_case_candidate_rows",
    "round181_case_records",
    "round181_price_field_rows",
    "round181_score_profile_rows",
    "round181_score_stage_price_alignment_rows",
    "round181_stage_cap_rows",
    "round181_stage_date_rows",
    "round181_summary",
    "round181_target_for",
    "write_round181_r10_loop11_reports",
]
