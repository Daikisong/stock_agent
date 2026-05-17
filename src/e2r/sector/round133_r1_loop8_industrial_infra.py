"""Round-133 R1 Loop-8 industrial orders and infrastructure pack.

Round 133 returns to R1 after the R13 Loop-7 RedTeam pass. It tightens the
industrial/order/infrastructure sector around backlog-to-FCF conversion,
contract detail, margin evidence, capital-allocation shock, approval gates,
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


ROUND133_SOURCE_ROUND_PATH = "docs/round/round_133.md"
ROUND133_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round133_r1_loop8_industrial_infra"
ROUND133_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop8_round133.jsonl"
ROUND133_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round133_r1_loop8_v8.csv"


@dataclass(frozen=True)
class Round133ScoreWeightDraft:
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
class Round133ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round133ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop8_penalty_axes: tuple[str, ...]
    normalization_point: str
    hard_gate: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.INDUSTRIAL_ORDERS_INFRA

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round133CaseCandidate:
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
class Round133BaseScoreWeight:
    component: str
    points: int
    loop8_direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {
            "component": self.component,
            "points": str(self.points),
            "loop8_direction": self.loop8_direction,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class Round133StageCap:
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
class Round133ScoreStagePriceAlignment:
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


ROUND133_BASE_SCORE_WEIGHTS: tuple[Round133BaseScoreWeight, ...] = (
    Round133BaseScoreWeight("eps_fcf_revision", 25, "up", "Stage 3 promotion depends on order/backlog becoming OP/EPS/FCF."),
    Round133BaseScoreWeight("contract_backlog_visibility", 22, "hold_but_detail_required", "Contract amount, period, counterparty, delivery, backlog, PPA, and slot reservation define Stage 2."),
    Round133BaseScoreWeight("bottleneck_pricing_power", 18, "hold_with_price_path_check", "Transformer lead time, turbine slot, grid bottleneck, and defense capacity matter only if they support margin."),
    Round133BaseScoreWeight("market_mispricing_gap", 10, "cap_after_consensus", "Old industrial frame must still be wrong, but crowded AI power or defense consensus lowers room."),
    Round133BaseScoreWeight("valuation_room_4b_runway", 7, "cap_after_rerating", "GE Vernova-style rerating needs explicit 4B watch after the market recognizes the power-equipment theme."),
    Round133BaseScoreWeight("capital_discipline_fcf_conversion", 10, "up", "FCF-funded buyback/dividend adds quality; dilution, FSS correction, and unclear CAPEX become hard RedTeam."),
    Round133BaseScoreWeight("information_confidence_disclosure_detail", 8, "up", "OpenDART list-only, MoU-only, PPA without approval, or missing detail caps Stage 3."),
)


ROUND133_STAGE_CAPS: tuple[Round133StageCap, ...] = (
    Round133StageCap(
        "Stage 1",
        "45",
        ("industry_news", "policy_news", "mou_or_moa", "macro_shortage_without_company_contract", "demand_narrative_without_cashflow"),
        ("us_transformer_shortage_import_slots_case", "hd_hyundai_huntington_us_navy_aux_case", "oklo_smr_no_revenue_watch_case", "ukraine_reconstruction_policy_case"),
        "Green blocked until company-level contract/backlog detail appears.",
    ),
    Round133StageCap(
        "Stage 2",
        "70",
        ("contract_amount", "customer", "period_or_delivery_schedule", "backlog_or_guidance", "ppa_or_slot_reservation_with_gate_status"),
        ("ls_electric_525kv_us_datacenter_transformer_case", "hyundai_rotem_morocco_rail_case", "constellation_tmi_microsoft_restart_case"),
        "Green blocked until OP/EPS/FCF, margin, and price path confirm.",
    ),
    Round133StageCap(
        "Stage 3",
        "100",
        ("op_eps_fcf_revision", "margin_or_fcf_conversion", "price_path_alignment", "cross_evidence"),
        ("ge_vernova_data_center_orders_case", "siemens_energy_fcf_buyback_case"),
        "Green possible only if not already saturated 4B and no hard RedTeam.",
    ),
    Round133StageCap(
        "Stage 4B",
        "monitoring",
        ("large_rerating", "crowded_consensus", "valuation_room_reduced", "revision_slowdown_watch"),
        ("ge_vernova_data_center_orders_case", "siemens_energy_fcf_buyback_case"),
        "A good structure can be downgraded to watch when the new frame is widely priced.",
    ),
    Round133StageCap(
        "Stage 4C",
        "hard_gate",
        ("dilution", "fss_correction_request", "contract_cancel_or_delay", "low_margin", "permitting_or_policy_break", "profit_miss", "accounting_or_disclosure_shock"),
        ("hanwha_aerospace_dilution_trim_case", "siemens_orders_profit_miss_case", "oklo_smr_no_revenue_watch_case", "perth_data_center_withdrawal_case"),
        "Hard RedTeam overrides high order/backlog score.",
    ),
)


ROUND133_SCORE_STAGE_PRICE_ALIGNMENT: tuple[Round133ScoreStagePriceAlignment, ...] = (
    Round133ScoreStagePriceAlignment(
        "ge_vernova_data_center_orders_case",
        "Stage 2 -> Stage 3 / 4B-watch",
        "event-day price reaction confirmed in round note; longer MFE/MAE still needs official OHLCV backfill",
        "score_to_stage_to_price_aligned",
        "keep EPS/FCF, visibility, and bottleneck weights high; reduce valuation room through 4B watch",
    ),
    Round133ScoreStagePriceAlignment(
        "siemens_energy_fcf_buyback_case",
        "Stage 3 candidate / 4B-watch",
        "FCF and buyback evidence strong; price path requires OHLCV backfill",
        "partially_confirmed",
        "raise capital/FCF conversion weight but require price validation before Green",
    ),
    Round133ScoreStagePriceAlignment(
        "ls_electric_525kv_us_datacenter_transformer_case",
        "Stage 2",
        "contract detail strong; price path requires backfill",
        "stage2_not_green_yet",
        "raise EHV visibility; keep EPS/FCF cap until margin and revisions appear",
    ),
    Round133ScoreStagePriceAlignment(
        "hyundai_rotem_morocco_rail_case",
        "Stage 2",
        "large contract visible; price path and margin require backfill",
        "stage2_not_green_yet",
        "rail remains capped before margin, warranty, financing, FX, and OP/EPS evidence",
    ),
    Round133ScoreStagePriceAlignment(
        "constellation_tmi_microsoft_restart_case",
        "Stage 2",
        "Q1 beat and Microsoft PPA context exist, but the round note recorded a negative price reaction and open FERC/grid-rights gates",
        "stage2_with_approval_gate",
        "existing nuclear PPA/restart stays capped until FERC/PJM grid rights, restart CAPEX, and guidance conversion are verified",
    ),
    Round133ScoreStagePriceAlignment(
        "hanwha_aerospace_dilution_trim_case",
        "Stage 2 structure + 4C-watch",
        "capital raise shock matched negative price-path warning in round note",
        "redteam_alignment_confirmed",
        "strengthen capital discipline penalty and stage_after_redteam downgrade",
    ),
    Round133ScoreStagePriceAlignment(
        "hd_hyundai_huntington_us_navy_aux_case",
        "Stage 1~2 option",
        "MoU/MoA only; any price move is event premium until contract economics appear",
        "green_block_correct",
        "strengthen MoU/MoA score cap and require vessel count, contract value, schedule, margin, and yard CAPEX",
    ),
    Round133ScoreStagePriceAlignment(
        "siemens_orders_profit_miss_case",
        "Stage 2 capped / 4C-watch",
        "orders and backlog looked strong, but sales and industrial profit miss matched the negative price reaction",
        "orders_only_false_positive_contained",
        "orders-only evidence is capped when profit/margin conversion is missing or negative",
    ),
    Round133ScoreStagePriceAlignment(
        "oklo_smr_no_revenue_watch_case",
        "Stage 1~2 watch",
        "regulatory progress did not offset no revenue, wider loss, and delayed commercialization in the round note",
        "pre_revenue_smr_green_block_correct",
        "SMR policy/news is capped before revenue, signed customer economics, financing, and commercial operation visibility",
    ),
)


ROUND133_SCORE_TARGETS: tuple[Round133ScoreTarget, ...] = (
    Round133ScoreTarget(
        "GRID_TRANSFORMER_SHORTAGE",
        E2RArchetype.GRID_TRANSFORMER_SHORTAGE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round133ScoreWeightDraft(24, 25, 24, 12, 10, 1, 5),
        ("data_center_power_demand", "ev_grid_demand", "grid_modernization", "lead_time_extended", "transformer_price_increase"),
        ("supply_contract", "contract_value_to_sales", "delivery_schedule", "backlog_growth", "op_eps_revision"),
        ("fy1_fy2_fy3_revision", "long_lead_time", "price_increase", "margin_improvement", "old_industrial_frame_rerating"),
        ("sector_wide_ai_grid_consensus", "valuation_band_expansion", "capacity_addition_news", "new_order_growth_slowdown"),
        ("data_center_project_delay", "capa_normalization", "low_margin_contract", "margin_miss"),
        ("contract_value", "contract_duration", "delivery_schedule", "backlog_growth", "margin_improvement", "op_eps_revision"),
        ("capa_normalization", "data_center_project_delay", "low_margin_contract", "raw_material_tariff_cost"),
        ("capa_normalization", "data_center_delay", "low_margin_long_term_contract", "project_delay"),
        "Loop 8 strengthens transformer shortage, but Green still requires contract amount, duration, delivery, margin, and EPS conversion.",
    ),
    Round133ScoreTarget(
        "GRID_EHV_TRANSFORMER_EXPORT",
        E2RArchetype.GRID_EHV_TRANSFORMER_EXPORT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft(24, 25, 24, 13, 10, 1, 6),
        ("ehv_transformer_shortage", "525kv_transformer", "765kv_transformer", "us_grid_import_demand"),
        ("ehv_export_contract", "contract_value", "delivery_schedule", "data_center_use_case", "counterparty_visible"),
        ("backlog_growth", "margin_visible", "op_eps_revision", "fcf_conversion", "old_industrial_frame_rerating"),
        ("k_transformer_export_narrative_crowded", "ehv_contract_priced_as_green"),
        ("delivery_delay", "raw_material_cost_spike", "customer_project_delay", "capa_normalization", "margin_unknown"),
        ("contract_value", "delivery_schedule", "counterparty", "data_center_or_utility_customer", "margin_visible", "op_eps_revision"),
        ("contract_margin_missing", "delivery_delay", "copper_or_goes_cost", "customer_project_delay"),
        ("contract_margin", "delivery_delay", "raw_material_cost", "customer_project_delay", "project_delay"),
        "525kV/765kV EHV export contracts are stronger than generic transformer headlines, but margin and delivery detail remain mandatory.",
    ),
    Round133ScoreTarget(
        "GRID_SUPPLY_SLOT_PREBUY",
        E2RArchetype.GRID_SUPPLY_SLOT_PREBUY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft(22, 24, 22, 12, 10, 1, 5),
        ("lead_time_extended", "factory_slot_prebuy", "production_slot_shortage", "transformer_price_increase"),
        ("slot_based_long_term_agreement", "prepayment", "customer_project_schedule", "capacity_allocation"),
        ("slot_to_revenue_conversion", "multi_year_visibility", "margin_improvement", "op_eps_revision"),
        ("slot_prebuy_story_crowded", "slot_premium_priced"),
        ("slot_cancelled", "customer_project_delay", "capa_normalization", "slot_premium_fades"),
        ("slot_agreement", "prepayment", "customer_project_schedule", "revenue_conversion", "margin_visible"),
        ("slot_cancelled", "customer_project_delay", "capa_normalization", "prepayment_missing"),
        ("slot_cancelled", "project_delay", "capa_normalization", "slot_premium_fades"),
        "Production-slot prebuy is a stronger visibility signal than generic demand, but it must convert into revenue, margin, and EPS.",
    ),
    Round133ScoreTarget(
        "GRID_MEDIUM_VOLTAGE_EXPANSION",
        E2RArchetype.GRID_MEDIUM_VOLTAGE_EXPANSION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft(22, 23, 20, 12, 10, 1, 5),
        ("medium_voltage_demand", "switchgear_keyword", "substation_automation", "utility_demand", "electrification_demand"),
        ("medium_voltage_order", "capacity_expansion", "utility_customer", "grid_operator_customer", "op_eps_revision"),
        ("product_mix_improvement", "order_to_revenue_conversion", "opm_improvement", "fy1_fy2_revision"),
        ("medium_voltage_ai_grid_consensus_crowded", "capacity_expansion_priced"),
        ("capa_normalization", "lead_time_normalization", "price_normalization", "mix_margin_miss"),
        ("medium_voltage_order", "switchgear_order", "utility_customer", "op_eps_revision", "margin_visible"),
        ("capa_normalization", "product_mix_unclear", "price_normalization"),
        ("capa_normalization", "product_mix_unclear", "price_normalization"),
        "Medium-voltage equipment expands the grid bottleneck lens beyond large transformers, but CAPA normalization must be tracked.",
    ),
    Round133ScoreTarget(
        "AI_DATA_CENTER_POWER_EQUIPMENT",
        E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round133ScoreWeightDraft(22, 23, 19, 13, 10, 0, 5),
        ("ups_pdu_switchgear_keyword", "modular_power", "electrification_equipment", "hyperscaler_power_demand"),
        ("data_center_orders", "bookings_growth", "backlog_growth", "revenue_guidance_up"),
        ("orders_to_revenue_conversion", "op_margin_improvement", "fcf_conversion", "valuation_frame_change"),
        ("data_center_power_consensus_crowded", "ytd_return_extreme", "valuation_crowding"),
        ("project_delay", "bookings_slowdown", "data_center_capex_delay", "low_margin_project"),
        ("orders", "backlog", "revenue_guidance", "op_eps_revision", "margin_visible"),
        ("project_delay", "valuation_crowding", "orders_slowdown", "wind_or_mix_risk", "grid_integration_complexity"),
        ("project_delay", "valuation_crowding", "orders_slowdown", "grid_interconnection_delay"),
        "GE Vernova-style orders/backlog can support Stage 2/3, but rapid rerating creates 4B-watch.",
    ),
    Round133ScoreTarget(
        "GAS_TURBINE_POWER_BACKLOG",
        E2RArchetype.GAS_TURBINE_POWER_BACKLOG,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft(21, 22, 18, 12, 10, 0, 5),
        ("ai_power_demand", "gas_turbine_slot_shortage", "power_backlog", "turbine_reservation"),
        ("gas_turbine_backlog", "turbine_slot_reservation", "power_revenue_guidance_up", "storage_equipment_order"),
        ("turbine_backlog_to_revenue", "electrification_profit_growth", "margin_visible", "fcf_conversion"),
        ("gas_turbine_ai_power_story_crowded", "turbine_slot_priced"),
        ("tariff_cost", "wind_segment_loss", "turbine_delivery_delay", "project_cancellation"),
        ("turbine_backlog", "slot_reservation", "guidance_up", "margin_visible"),
        ("tariff_cost", "wind_segment_loss", "delivery_delay", "project_cancellation"),
        ("tariff_cost", "wind_segment_loss", "delivery_delay", "project_cancelled"),
        "AI power gas-turbine backlog is separated from generic data-center equipment because tariff cost, wind drag, and delivery slots need their own gate.",
    ),
    Round133ScoreTarget(
        "POWER_EQUIPMENT_BACKLOG_TO_FCF",
        E2RArchetype.POWER_EQUIPMENT_BACKLOG_TO_FCF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft(22, 22, 18, 12, 9, 4, 5),
        ("power_equipment_backlog", "ai_power_demand", "fcf_growth", "buyback_or_dividend"),
        ("orders_to_fcf", "cash_flow_jump", "buyback_acceleration", "margin_guidance_up"),
        ("repeat_order_to_fcf_conversion", "capital_return_durable", "op_eps_revision", "valuation_frame_change"),
        ("capital_return_story_crowded", "order_peak_priced", "buyback_fully_capitalized"),
        ("order_peak", "legacy_segment_loss", "fcf_slowdown", "buyback_cut"),
        ("fcf_growth", "buyback_or_dividend", "margin_visible", "order_backlog_quality"),
        ("order_peak", "legacy_loss", "fcf_slowdown", "capital_return_one_off"),
        ("order_peak", "fcf_slowdown", "buyback_cut", "legacy_loss"),
        "Backlog that converts to FCF and capital return can raise quality, but it also turns on 4B-watch if valuation has already rerated.",
    ),
    Round133ScoreTarget(
        "DATA_CENTER_GRID_FLEXIBILITY_OVERLAY",
        E2RArchetype.DATA_CENTER_GRID_FLEXIBILITY_OVERLAY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("ai_load_flexibility", "demand_response", "grid_deferral_model", "data_center_power_software"),
        ("model_validated", "utility_program", "customer_contract", "revenue_mapping"),
        ("not_company_green_until_contract_revenue_and_margin_exist",),
        ("grid_flexibility_model_priced_as_equipment_revenue",),
        ("model_only", "no_contract", "no_revenue_mapping", "project_delay"),
        (),
        ("model_only", "no_contract", "no_revenue_mapping"),
        ("model_to_revenue_misclassified", "project_delay", "no_customer_contract"),
        "AI load-flexibility research supports structural demand context, not individual Stage 3 evidence without contract and revenue mapping.",
    ),
    Round133ScoreTarget(
        "CONTRACT_BACKLOG_INDUSTRIAL",
        E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round133ScoreWeightDraft(20, 24, 18, 13, 12, 1, 5),
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
    Round133ScoreTarget(
        "DEFENSE_GOVERNMENT_BACKLOG",
        E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round133ScoreWeightDraft(21, 24, 17, 14, 14, 3, 5),
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
    Round133ScoreTarget(
        "DEFENSE_LOCAL_PRODUCTION_PLATFORM",
        E2RArchetype.DEFENSE_LOCAL_PRODUCTION_PLATFORM,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft(21, 23, 16, 14, 13, 2, 5),
        ("local_production_preference", "customer_country_manufacturing", "local_content_requirement"),
        ("local_factory_plan", "delivery_batch", "multi_year_customer_country_demand", "backlog_growth"),
        ("regional_platform_visibility", "repeat_orders", "opm_improvement", "capex_and_margin_risk_controlled"),
        ("local_production_platform_story_crowded", "capex_ignored_by_rally"),
        ("local_factory_capex_burden", "margin_dilution", "political_risk", "delivery_delay", "dilution_shock"),
        ("local_production_contract", "repeat_customer_demand", "delivery_batch", "opm_improvement"),
        ("local_factory_capex", "margin_dilution", "political_risk", "dilution"),
        ("local_factory_capex", "margin_dilution", "political_risk", "dilution"),
        "Customer-country production can improve defense visibility, but CAPEX, local cost, and dilution must be checked.",
    ),
    Round133ScoreTarget(
        "DEFENSE_CAPITAL_ALLOCATION_SHOCK",
        E2RArchetype.DEFENSE_CAPITAL_ALLOCATION_SHOCK,
        Round10ThemePosture.REDTEAM_FIRST,
        Round133ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("share_issuance_plan", "overseas_factory_capex", "unclear_capex_plan"),
        ("large_equity_issuance", "use_of_proceeds_unclear", "regulator_revision_request", "shareholder_value_shock"),
        ("not_applicable_until_funding_quality_restored",),
        ("dilution_ignored_by_defense_backlog_story",),
        ("large_equity_issuance", "dilution", "regulator_revision_request", "fcf_burden"),
        (),
        ("large_equity_issuance", "dilution", "use_of_proceeds_unclear", "overseas_factory_capex"),
        ("capital_allocation_shock", "dilution", "use_of_proceeds_unclear", "regulator_revision_request"),
        "Defense backlog does not override a large unclear capital raise or dilution shock.",
        hard_gate=True,
    ),
    Round133ScoreTarget(
        "DEFENSE_US_SHIPBUILDING_PLATFORM",
        E2RArchetype.DEFENSE_US_SHIPBUILDING_PLATFORM,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft(16, 16, 12, 13, 9, 1, 5),
        ("us_shipbuilding_rebuild", "naval_mro_option", "moa_or_partnership", "summit_headline"),
        ("actual_vessel_contract", "mro_order", "yard_investment", "schedule_visible"),
        ("repeat_mro_or_newbuild_revenue", "margin_visible", "yard_execution", "op_eps_revision"),
        ("us_shipbuilding_option_crowded", "moa_priced_as_contract"),
        ("moa_only", "yard_capex_uncertain", "us_workforce_bottleneck", "legal_or_political_condition_failed"),
        ("actual_contract", "revenue_schedule", "margin_visible", "yard_capacity_funded"),
        ("moa_only", "yard_capex_uncertain", "workforce_bottleneck", "legal_restriction"),
        ("moa_only", "yard_capex", "workforce_bottleneck", "legal_restriction"),
        "US shipbuilding cooperation is an option value path; Stage 3 waits for actual contract, CAPEX, schedule, and margin evidence.",
    ),
    Round133ScoreTarget(
        "SHIPBUILDING_OFFSHORE_BACKLOG",
        E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round133ScoreWeightDraft(21, 22, 18, 13, 13, 1, 5),
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
    Round133ScoreTarget(
        "SHIPBUILDING_NAVAL_MRO",
        E2RArchetype.SHIPBUILDING_NAVAL_MRO,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft(16, 17, 11, 13, 10, 1, 5),
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
    Round133ScoreTarget(
        "SHIPBUILDING_PROCUREMENT_LEADTIME",
        E2RArchetype.SHIPBUILDING_PROCUREMENT_LEADTIME,
        Round10ThemePosture.REDTEAM_FIRST,
        Round133ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("procurement_lead_time_miss", "pipe_spool_delay", "supplier_delay", "engineered_to_order_delay"),
        ("procurement_delay_confirmed", "downstream_block_delay", "delivery_delay", "margin_penalty"),
        ("not_applicable_until_procurement_and_delivery_schedule_restored",),
        ("backlog_quality_ignores_procurement_delay",),
        ("supplier_delay", "pipe_spool_delay", "delivery_delay", "margin_penalty", "warranty_cost"),
        (),
        ("supplier_delay", "pipe_spool_delay", "delivery_delay", "margin_penalty"),
        ("procurement_delay", "delivery_delay", "margin_penalty"),
        "Shipbuilding and plant backlog can break if critical procured items delay downstream work and margin recognition.",
        hard_gate=True,
    ),
    Round133ScoreTarget(
        "RAIL_INFRASTRUCTURE",
        E2RArchetype.RAIL_INFRASTRUCTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft(20, 22, 12, 14, 11, 1, 5),
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
    Round133ScoreTarget(
        "NUCLEAR_EXISTING_PPA_RESTART",
        E2RArchetype.NUCLEAR_EXISTING_PPA_RESTART,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft(19, 23, 13, 14, 12, 2, 5),
        ("big_tech_clean_power_demand", "existing_nuclear_ppa", "nuclear_restart", "plant_relicense_support"),
        ("signed_ppa", "contract_duration_years", "plant_capacity_mw", "relicensing_support", "restart_capex_visible"),
        ("long_term_fcf_visibility", "ppa_economics_visible", "grid_injection_rights", "valuation_frame_change"),
        ("nuclear_ppa_theme_crowded", "related_stock_theme_spillover"),
        ("relicense_failure", "plant_outage", "policy_change", "ppa_economics_break", "restart_capex_overrun"),
        ("signed_ppa", "duration", "plant_capacity", "fcf_visibility", "grid_injection_rights"),
        ("relicense_risk", "plant_specific_risk", "ppa_economics_unverified", "restart_capex"),
        ("relicense", "plant_outage", "ppa_economics", "restart_capex"),
        "Existing nuclear PPA/restart is stronger than SMR policy because it has clearer cashflow visibility.",
    ),
    Round133ScoreTarget(
        "NUCLEAR_GRID_INJECTION_RIGHTS",
        E2RArchetype.NUCLEAR_GRID_INJECTION_RIGHTS,
        Round10ThemePosture.REDTEAM_FIRST,
        Round133ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("grid_injection_rights", "ferc_pjm_gate", "nuclear_restart_interconnection", "capacity_transfer"),
        ("ferc_approval", "pjm_interconnection", "grid_capacity_transfer", "ppa_grid_rights_confirmed"),
        ("not_applicable_until_grid_rights_and_restart_capex_are_confirmed",),
        ("ppa_or_restart_theme_ignores_grid_rights",),
        ("grid_rights_failure", "ferc_delay", "pjm_interconnection_delay", "restart_capex_overrun"),
        ("ferc_approval", "pjm_interconnection", "grid_rights_confirmed", "restart_capex_visible"),
        ("grid_rights_failure", "ferc_delay", "pjm_delay", "restart_capex"),
        ("grid_rights_failure", "ferc_delay", "pjm_delay", "restart_capex"),
        "Existing nuclear restart needs grid injection rights and interconnection approval before it can support high-conviction cashflow visibility.",
        hard_gate=True,
    ),
    Round133ScoreTarget(
        "NUCLEAR_SMR_GRID_POLICY",
        E2RArchetype.NUCLEAR_SMR_GRID_POLICY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round133ScoreWeightDraft(13, 12, 10, 13, 7, 1, 5),
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
    Round133ScoreTarget(
        "GEOPOLITICAL_RECONSTRUCTION",
        E2RArchetype.GEOPOLITICAL_RECONSTRUCTION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round133ScoreWeightDraft(10, 8, 8, 10, 7, 0, 4),
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
    Round133ScoreTarget(
        "DATA_CENTER_POWER_WATER_PERMITTING",
        E2RArchetype.DATA_CENTER_POWER_WATER_PERMITTING,
        Round10ThemePosture.REDTEAM_FIRST,
        Round133ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("data_center_local_opposition", "water_capacity_shortage", "water_permitting_delay", "grid_interconnection_delay", "moratorium", "noise_pollution"),
        ("project_delay_confirmed", "permit_delay", "community_opposition", "water_rights", "power_price_backlash", "project_withdrawal"),
        ("not_applicable_until_power_water_project_schedule_and_interconnection_restored",),
        ("delay_ignored_by_ai_power_order_story",),
        ("project_cancelled_or_delayed", "moratorium", "water_permitting_delay", "grid_interconnection_delay", "order_slowdown"),
        (),
        ("local_opposition", "water_permitting_delay", "water_capacity", "grid_interconnection_delay", "moratorium", "project_withdrawal"),
        ("project_delay", "water_permitting", "grid_interconnection_delay", "moratorium", "local_opposition"),
        "Hard RedTeam gate for data-center local opposition, water capacity/permitting, power interconnection, noise, and moratorium risk.",
        hard_gate=True,
    ),
    Round133ScoreTarget(
        "CAPITAL_ALLOCATION_DILUTION_OVERLAY",
        E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round133ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
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
    Round133ScoreTarget(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        Round133ScoreWeightDraft("cap", "cap", "cap", "cap", "cap", "cap", "+"),
        ("opendart_list_only", "contract_headline", "high_signal_disclosure"),
        ("opendart_detail_fetched", "contract_amount", "counterparty", "contract_duration"),
        ("contract_amount_to_sales", "delivery_schedule", "margin_visible", "multi_source_confirmation"),
        ("undisclosed_contract_theme_crowded",),
        ("detail_missing", "contract_amount_missing", "counterparty_missing", "duration_missing", "margin_unknown"),
        ("contract_value", "contract_duration", "counterparty", "delivery_schedule", "margin_visible"),
        ("detail_missing", "contract_amount_missing", "counterparty_missing", "duration_missing", "margin_unknown"),
        ("disclosure_confidence_capped", "detail_missing", "margin_unknown"),
        "R1 applies the R13 disclosure confidence cap: list-only or headline-only contract evidence cannot support Stage 3-Green.",
    ),
)


ROUND133_CASE_CANDIDATES: tuple[Round133CaseCandidate, ...] = (
    Round133CaseCandidate(
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
        ("round_133.md Reuters US transformer shortage",),
        "Transformer shortage is strong structural reference, but company-specific contracts, margin, and price path still need backfill.",
        (E2RArchetype.GRID_SUPPLY_SLOT_PREBUY, E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL),
    ),
    Round133CaseCandidate(
        "ls_electric_525kv_us_datacenter_transformer_case",
        "GRID_EHV_TRANSFORMER_EXPORT",
        "010120",
        "LS ELECTRIC 525kV 미국 데이터센터 변압기 후보",
        "KR",
        "success_candidate",
        None,
        date(2025, 11, 1),
        None,
        None,
        None,
        (
            "525kv_ehv_transformer",
            "us_datacenter_transformer",
            "korea_export",
            "data_center_customer",
            "delivery_schedule_needed",
        ),
        ("contract_amount_missing", "counterparty_missing", "margin_unknown", "disclosure_confidence_capped"),
        "korea_ehv_transformer_direct_mapping_needs_detail_confidence",
        "needs_price_backfill",
        ("round_133.md LS Electric 525kV US datacenter transformer case placeholder",),
        "Korean EHV transformer mapping can become high-quality R1 evidence only after amount, counterparty, delivery, and margin detail are verified.",
        (E2RArchetype.GRID_SUPPLY_SLOT_PREBUY, E2RArchetype.DISCLOSURE_CONFIDENCE_CAP),
    ),
    Round133CaseCandidate(
        "abb_medium_voltage_expansion_case",
        "GRID_MEDIUM_VOLTAGE_EXPANSION",
        "ABB",
        "ABB medium-voltage equipment expansion",
        "GLOBAL",
        "success_candidate",
        date(2026, 5, 11),
        date(2026, 5, 11),
        None,
        None,
        None,
        ("medium_voltage_capacity_expansion", "switchgear_demand", "utility_demand", "data_center_electrification", "capacity_up_50_to_300pct"),
        ("capa_normalization", "price_normalization", "product_mix_unclear"),
        "medium_voltage_expansion_aligned_needs_margin_backfill",
        "needs_price_backfill",
        ("round_133.md Reuters ABB medium-voltage equipment investment",),
        "Medium-voltage bottleneck broadens the grid equipment lens, but added CAPA can later normalize lead times and pricing.",
        (E2RArchetype.GRID_TRANSFORMER_SHORTAGE,),
    ),
    Round133CaseCandidate(
        "siemens_energy_fcf_buyback_case",
        "POWER_EQUIPMENT_BACKLOG_TO_FCF",
        "ENR",
        "Siemens Energy FCF and buyback acceleration",
        "GLOBAL",
        "4b_watch",
        date(2026, 5, 12),
        date(2026, 5, 12),
        None,
        date(2026, 5, 12),
        None,
        ("power_equipment_backlog", "cash_flow_jump", "buyback_acceleration", "margin_guidance_up"),
        ("order_peak", "buyback_fully_priced", "legacy_segment_loss", "fcf_slowdown"),
        "power_equipment_backlog_to_fcf_plus_4b_watch",
        "needs_price_backfill",
        ("round_133.md Reuters Siemens Energy cash flow and buyback",),
        "Backlog-to-FCF and buyback are quality upgrades, but the same evidence can mean 4B-watch when capital return is already priced.",
        (E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH,),
    ),
    Round133CaseCandidate(
        "siemens_energy_record_backlog_case",
        "POWER_EQUIPMENT_BACKLOG_TO_FCF",
        "ENR",
        "Siemens Energy record backlog and AI data-center order reference",
        "GLOBAL",
        "success_candidate",
        date(2026, 2, 1),
        date(2026, 2, 1),
        None,
        None,
        None,
        ("record_backlog", "ai_data_center_order", "power_equipment_order", "fcf_visibility_needed"),
        ("order_peak", "legacy_loss", "margin_unknown"),
        "power_equipment_record_backlog_needs_fcf_and_margin_backfill",
        "needs_price_backfill",
        ("round_133.md Siemens Energy record backlog context",),
        "Record backlog is useful Stage 2 evidence only after margin, FCF conversion, and order-quality checks.",
        (E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT,),
    ),
    Round133CaseCandidate(
        "siemens_orders_profit_miss_case",
        "POWER_EQUIPMENT_BACKLOG_TO_FCF",
        "ENR",
        "Siemens Energy strong orders with profit miss",
        "GLOBAL",
        "failed_rerating",
        date(2026, 5, 13),
        date(2026, 5, 13),
        None,
        None,
        None,
        ("orders_up_11pct", "record_backlog_124b_eur", "profit_miss", "sales_miss", "industrial_profit_down_8pct"),
        ("orders_only_without_profit", "sales_miss", "industrial_profit_miss", "margin_pressure", "fx_hit"),
        "orders_only_false_positive_before_eps_fcf_conversion",
        "needs_price_backfill",
        ("round_133.md Reuters Siemens orders strong but profit miss",),
        "Loop 8 separates strong orders from E2R quality: if sales/profit miss and margin conversion fail, backlog cannot create Green.",
        (E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,),
    ),
    Round133CaseCandidate(
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
        ("round_133.md WSJ GE Vernova orders/backlog",),
        "Orders, backlog, guidance, and price reaction align, but rapid YTD rerating requires 4B-watch.",
        (E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE, E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH),
    ),
    Round133CaseCandidate(
        "ge_vernova_power_backlog_turbine_case",
        "GAS_TURBINE_POWER_BACKLOG",
        "GEV",
        "GE Vernova power backlog / gas turbine slot case",
        "US",
        "4b_watch",
        date(2026, 1, 1),
        date(2026, 4, 22),
        None,
        date(2026, 4, 22),
        None,
        ("gas_turbine_backlog", "power_backlog_163b_usd", "revenue_guidance_up", "electrification_profit_growth"),
        ("tariff_cost", "wind_segment_loss", "valuation_crowding", "project_delay"),
        "gas_turbine_power_backlog_aligned_but_4b_watch",
        "needs_price_backfill",
        ("round_133.md Reuters GE Vernova power backlog / turbine context",),
        "Power and gas-turbine backlog can validate AI electricity demand, but wind drag, tariff cost, and rapid rerating require 4B-watch.",
        (E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT, E2RArchetype.SECTOR_SUCCESS_BUT_4B_WATCH),
    ),
    Round133CaseCandidate(
        "us_power_demand_record_eia_case",
        "AI_DATA_CENTER_POWER_EQUIPMENT",
        "US_POWER_DEMAND",
        "US power demand record EIA macro tailwind",
        "US",
        "success_candidate",
        date(2026, 5, 12),
        None,
        None,
        None,
        None,
        ("ai_crypto_datacenter_power_demand", "commercial_electricity_sales_record", "electrification_demand"),
        ("macro_tailwind_not_company_contract", "company_mapping_missing", "contract_detail_missing"),
        "grid_macro_tailwind_not_company_green",
        "needs_price_backfill",
        ("round_133.md Reuters EIA US power demand record path",),
        "Macro power demand raises the R1 radar floor, but individual Stage 3 needs company contract, margin, and EPS evidence.",
        (E2RArchetype.GRID_TRANSFORMER_SHORTAGE, E2RArchetype.DISCLOSURE_CONFIDENCE_CAP),
    ),
    Round133CaseCandidate(
        "data_center_grid_flexibility_case",
        "DATA_CENTER_GRID_FLEXIBILITY_OVERLAY",
        "AI_GRID_FLEX",
        "AI data-center grid flexibility reference",
        "GLOBAL",
        "event_premium",
        date(2026, 4, 1),
        None,
        None,
        None,
        None,
        ("ai_load_flexibility", "grid_deferral_model", "demand_response", "interconnection_delay_relief"),
        ("model_only", "no_company_contract", "no_revenue_mapping", "misclassified_as_equipment_order"),
        "grid_flexibility_reference_not_company_green",
        "needs_price_backfill",
        ("round_133.md arXiv AI data-center flexibility",),
        "Load-flexibility research helps explain grid bottlenecks, but it cannot create company Stage 3 evidence without contracts and revenue.",
        (E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT,),
    ),
    Round133CaseCandidate(
        "perth_data_center_withdrawal_case",
        "DATA_CENTER_POWER_WATER_PERMITTING",
        "PERTH_DATA_CENTER",
        "Perth data-center withdrawal reference",
        "GLOBAL",
        "4c_thesis_break",
        date(2026, 5, 15),
        None,
        None,
        None,
        date(2026, 5, 15),
        ("ai_data_center_demand", "local_opposition", "cultural_environmental_sensitivity", "diesel_generator_noise", "project_withdrawal"),
        ("local_opposition", "diesel_generator_noise", "project_withdrawal", "permitting_delay", "grid_interconnection_delay"),
        "data_center_project_delay_overlay",
        "needs_price_backfill",
        ("round_133.md Guardian Perth data-center withdrawal",),
        "Power-equipment demand can be structural, but local opposition and project withdrawal can break new-order timing.",
        (E2RArchetype.GRID_TRANSFORMER_SHORTAGE, E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT),
    ),
    Round133CaseCandidate(
        "indianapolis_data_center_moratorium_case",
        "DATA_CENTER_POWER_WATER_PERMITTING",
        "INDIANAPOLIS_DC_MORATORIUM",
        "Indianapolis data-center moratorium reference",
        "GLOBAL",
        "4c_thesis_break",
        date(2026, 5, 15),
        None,
        None,
        None,
        date(2026, 5, 15),
        ("ai_data_center_demand", "moratorium", "utility_strain", "power_price_backlash"),
        ("moratorium", "local_opposition", "grid_interconnection_delay", "power_price_backlash", "order_slowdown"),
        "data_center_moratorium_soft_4c_overlay",
        "needs_price_backfill",
        ("round_133.md data-center moratorium reference",),
        "A local moratorium can delay project timing even when AI data-center power demand is structurally real.",
        (E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT, E2RArchetype.GRID_TRANSFORMER_SHORTAGE),
    ),
    Round133CaseCandidate(
        "seattle_data_center_moratorium_case",
        "DATA_CENTER_POWER_WATER_PERMITTING",
        "SEATTLE_DC_MORATORIUM",
        "Seattle data-center moratorium watch",
        "GLOBAL",
        "4c_thesis_break",
        date(2026, 5, 15),
        None,
        None,
        None,
        date(2026, 5, 15),
        ("ai_data_center_demand", "urban_moratorium_review", "environmental_impact", "grid_capacity_strain"),
        ("moratorium", "local_opposition", "grid_interconnection_delay", "power_price_backlash", "order_slowdown"),
        "urban_data_center_moratorium_4c_overlay",
        "needs_price_backfill",
        ("round_133.md Seattle data-center moratorium watch",),
        "Urban data-center moratorium risk is a delivery/order timing overlay, not a positive equipment-revenue input.",
        (E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT, E2RArchetype.GRID_TRANSFORMER_SHORTAGE),
    ),
    Round133CaseCandidate(
        "water_capacity_data_center_case",
        "DATA_CENTER_POWER_WATER_PERMITTING",
        "DATA_CENTER_WATER_CAPACITY",
        "Data-center public water capacity bottleneck reference",
        "GLOBAL",
        "4c_thesis_break",
        date(2026, 3, 1),
        None,
        None,
        None,
        date(2026, 3, 1),
        ("water_capacity_requirement", "dry_cooling_cost_increase", "summer_peak_grid_stress"),
        ("water_capacity_shortage", "water_permitting_delay", "community_water_conflict", "project_delay"),
        "data_center_water_capacity_4c_overlay",
        "needs_price_backfill",
        ("round_133.md arXiv data-center public water systems",),
        "AI data-center demand can be real while water capacity blocks project timing and related equipment orders.",
        (E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT,),
    ),
    Round133CaseCandidate(
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
        ("round_133.md Reuters Romania K9 contract",),
        "Government customer, contract size, delivery term, and backlog growth make this a defense backlog reference case.",
        (E2RArchetype.STRUCTURAL_SUCCESS_ALIGNED,),
    ),
    Round133CaseCandidate(
        "hanwha_aerospace_europe_sales_visibility_case",
        "DEFENSE_LOCAL_PRODUCTION_PLATFORM",
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
        ("round_133.md Reuters Hanwha Europe land arms sales",),
        "Regional platform demand is stronger than a one-off order, but CAPEX/dilution and delivery risk remain guardrails.",
        (E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, E2RArchetype.STRUCTURAL_SUCCESS_ALIGNED),
    ),
    Round133CaseCandidate(
        "hanwha_aerospace_dilution_trim_case",
        "DEFENSE_CAPITAL_ALLOCATION_SHOCK",
        "012450",
        "한화에어로스페이스 증자 축소와 자본배분 shock",
        "KR",
        "failed_rerating",
        date(2025, 4, 7),
        date(2025, 4, 7),
        None,
        date(2025, 4, 7),
        None,
        ("share_issuance_plan_trimmed", "overseas_expansion_capex", "capital_raise_1_6b_usd"),
        ("large_equity_issuance", "dilution", "use_of_proceeds_unclear", "regulator_revision_request"),
        "capital_allocation_shock",
        "needs_price_backfill",
        ("round_133.md Reuters Hanwha Aerospace trims capital increase plan",),
        "Good defense backlog can still be capped by dilution, overseas factory CAPEX, and regulator-driven capital allocation uncertainty.",
        (E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY),
    ),
    Round133CaseCandidate(
        "hd_hyundai_huntington_us_navy_aux_case",
        "DEFENSE_US_SHIPBUILDING_PLATFORM",
        "329180",
        "HD Hyundai Heavy / Huntington Ingalls U.S. navy auxiliary ship option",
        "KR",
        "success_candidate",
        date(2025, 10, 26),
        None,
        None,
        None,
        None,
        ("us_shipbuilding_moa", "naval_auxiliary_ship_option", "summit_headline", "yard_cooperation"),
        ("moa_only", "actual_contract_missing", "yard_capex_uncertain", "us_workforce_bottleneck", "margin_unknown"),
        "us_naval_shipbuilding_option_watch_not_green",
        "needs_price_backfill",
        ("round_133.md Reuters HD Hyundai Heavy / Huntington Ingalls MoA",),
        "U.S. naval shipbuilding cooperation is strategically useful, but MoA-only evidence must not be treated as signed recurring revenue.",
        (E2RArchetype.SHIPBUILDING_NAVAL_MRO, E2RArchetype.DISCLOSURE_CONFIDENCE_CAP),
    ),
    Round133CaseCandidate(
        "hanwha_ocean_us_shipbuilding_sanction_case",
        "SHIPBUILDING_NAVAL_MRO",
        "042660",
        "한화오션 미국 조선/MRO 제재 리스크",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("philly_shipyard_acquisition", "us_navy_mro_reference", "us_shipbuilding_rebuild_option", "jones_act_option"),
        ("geopolitical_sanction", "low_margin_mro", "newbuild_license_uncertain", "us_legal_restriction", "shipyard_modernization_capex"),
        "naval_mro_option_with_geopolitical_risk",
        "needs_source_date_backfill",
        ("round_133.md AP Hanwha Ocean China sanctions",),
        "US naval MRO is a strategic option, but sanctions, low-margin early work, legal limits, and CAPEX can block Green.",
        (E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG,),
    ),
    Round133CaseCandidate(
        "shipbuilding_procurement_leadtime_case",
        "SHIPBUILDING_PROCUREMENT_LEADTIME",
        "SHIPYARD_PROCUREMENT",
        "Shipbuilding procurement lead-time delay reference",
        "GLOBAL",
        "4c_thesis_break",
        date(2026, 1, 1),
        None,
        None,
        None,
        date(2026, 1, 1),
        ("procurement_lead_time_prediction", "pipe_spool_delay", "supplier_delay", "downstream_block_delay"),
        ("procurement_delay", "delivery_delay", "margin_penalty", "warranty_cost"),
        "procurement_delay_margin_risk_overlay",
        "needs_price_backfill",
        ("round_133.md arXiv shipyard procurement lead-time prediction",),
        "Engineered-to-order backlog can look strong while procurement delays break delivery timing and margin recognition.",
        (E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG,),
    ),
    Round133CaseCandidate(
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
        ("round_133.md Reuters Hyundai Rotem Morocco rail order",),
        "A large signed rail order is Stage-2 style evidence; Green needs margin, delivery, financing, and OP/EPS evidence.",
        (E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL,),
    ),
    Round133CaseCandidate(
        "meta_constellation_existing_nuclear_ppa_case",
        "NUCLEAR_EXISTING_PPA_RESTART",
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
        ("round_133.md Reuters Meta Constellation nuclear PPA",),
        "Existing nuclear PPA has stronger cashflow visibility than SMR policy, but Korean equipment mapping needs direct contracts.",
        (E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT,),
    ),
    Round133CaseCandidate(
        "constellation_tmi_microsoft_restart_case",
        "NUCLEAR_EXISTING_PPA_RESTART",
        "CEG",
        "Constellation Three Mile Island / Microsoft restart",
        "US",
        "success_candidate",
        date(2026, 5, 11),
        date(2026, 5, 11),
        None,
        None,
        None,
        ("nuclear_restart", "microsoft_power_demand", "ferc_decision_expected", "grid_injection_rights", "restart_capex"),
        ("restart_capex_overrun", "regulatory_delay", "grid_rights_failure", "ppa_economics_unverified"),
        "nuclear_restart_ppa_candidate_needs_regulatory_and_capex_backfill",
        "needs_price_backfill",
        ("round_133.md Reuters Three Mile Island restart decision",),
        "Existing nuclear restart can be stronger than SMR policy, but needs regulatory, grid rights, restart CAPEX, and PPA economics verification.",
        (E2RArchetype.NUCLEAR_GRID_INJECTION_RIGHTS, E2RArchetype.AI_DATA_CENTER_POWER_EQUIPMENT),
    ),
    Round133CaseCandidate(
        "nuclear_grid_injection_rights_gate_case",
        "NUCLEAR_GRID_INJECTION_RIGHTS",
        "NUCLEAR_GRID_RIGHTS",
        "Existing nuclear restart grid injection rights gate",
        "US",
        "4c_thesis_break",
        date(2026, 5, 11),
        None,
        None,
        None,
        None,
        ("grid_injection_rights", "ferc_decision_expected", "pjm_interconnection", "restart_capex"),
        ("grid_rights_failure", "ferc_delay", "pjm_interconnection_delay", "restart_capex_overrun"),
        "nuclear_grid_injection_gate_before_green",
        "needs_price_backfill",
        ("round_133.md Reuters Three Mile Island restart grid rights gate",),
        "Existing nuclear PPA/restart evidence needs grid injection and interconnection rights before high-conviction cashflow can be assumed.",
        (E2RArchetype.NUCLEAR_EXISTING_PPA_RESTART,),
    ),
    Round133CaseCandidate(
        "nuscale_uamps_smr_cancel_case",
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
        ("round_133.md NuScale UAMPS CFPP cancellation",),
        "SMR policy is not existing nuclear PPA; cost, customer, financing, and cancellation risk can be hard 4C.",
        (E2RArchetype.THESIS_BREAK_4C,),
    ),
    Round133CaseCandidate(
        "oklo_smr_no_revenue_watch_case",
        "NUCLEAR_SMR_GRID_POLICY",
        "OKLO",
        "Oklo SMR regulatory progress without revenue",
        "US",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("smr_regulatory_milestone", "commercial_operation_target_2028", "no_revenue", "net_loss_widened"),
        ("pre_revenue_smr", "loss_widening", "financing_risk", "commercialization_delay", "customer_contract_missing"),
        "pre_revenue_smr_watch_not_green",
        "needs_source_date_backfill",
        ("round_133.md Oklo pre-revenue SMR watch case",),
        "SMR policy momentum can enter watch, but no revenue, wider loss, and delayed commercialization cap it before Stage 3.",
        (E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,),
    ),
    Round133CaseCandidate(
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
        ("round_133.md reconstruction policy rule",),
        "Reconstruction themes stay Event/Watch until binding contract, financing, construction, and revenue evidence appear.",
        (E2RArchetype.EVENT_PREMIUM,),
    ),
    Round133CaseCandidate(
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
        ("round_133.md Neom policy/infrastructure rule",),
        "Neom-style policy infrastructure is not Green without contract, financing, construction start, and revenue recognition.",
        (E2RArchetype.EVENT_PREMIUM,),
    ),
)


ROUND133_PRICE_FIELDS: tuple[str, ...] = (
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
    "transformer_voltage_kv",
    "transformer_lead_time_months",
    "transformer_price_change",
    "factory_slot_prebuy_flag",
    "grid_modernization_flag",
    "data_center_customer_flag",
    "foreign_import_flag",
    "korea_export_flag",
    "goes_cost_change",
    "copper_cost_change",
    "medium_voltage_order",
    "medium_voltage_capacity_expansion",
    "switchgear_order",
    "substation_equipment_order",
    "utility_customer_flag",
    "grid_operator_customer_flag",
    "data_center_orders",
    "data_center_backlog",
    "data_center_power_equipment_revenue",
    "gas_turbine_backlog_gw",
    "gas_turbine_slot_reservation_gw",
    "power_equipment_backlog",
    "storage_equipment_order",
    "electrification_profit_growth",
    "wind_segment_loss",
    "tariff_cost_amount",
    "project_delay_flag",
    "local_opposition_flag",
    "moratorium_flag",
    "water_permitting_delay_flag",
    "grid_interconnection_delay_flag",
    "diesel_generator_noise_flag",
    "project_withdrawal_flag",
    "defense_customer_country",
    "government_customer_flag",
    "local_production_flag",
    "local_content_requirement",
    "export_license_risk_flag",
    "delivery_batch_count",
    "defense_backlog",
    "nato_customer_flag",
    "technology_transfer_flag",
    "capex_amount",
    "dilution_flag",
    "share_issuance_amount",
    "use_of_proceeds_clarity",
    "regulator_revision_request_flag",
    "local_factory_capex_flag",
    "margin_dilution_flag",
    "unmanned_system_contract_flag",
    "prototype_flag",
    "pentagon_contract_flag",
    "production_contract_flag",
    "autonomous_naval_system_flag",
    "ship_newbuilding_price_index",
    "low_margin_backlog_flag",
    "steel_plate_cost_change",
    "labor_cost_change",
    "naval_mro_contract_flag",
    "msra_flag",
    "naval_newbuild_license_flag",
    "mro_margin_signal",
    "geopolitical_sanction_flag",
    "rail_contract_value",
    "rail_delivery_schedule",
    "rail_warranty_risk",
    "rail_financing_secured_flag",
    "rail_fx_risk",
    "nuclear_ppa_flag",
    "ppa_duration_years",
    "plant_capacity_mw",
    "relicensing_support_flag",
    "nuclear_restart_flag",
    "grid_injection_rights_flag",
    "restart_capex_amount",
    "smr_flag",
    "smr_cost_overrun_flag",
    "customer_subscription_flag",
    "project_cancelled_flag",
    "doe_subsidy_flag",
    "reconstruction_contract_flag",
    "financing_secured_flag",
    "budget_allocated_flag",
    "construction_started_flag",
    "revenue_recognized_flag",
    "opendart_rcept_no",
    "opendart_detail_fetched_flag",
    "disclosure_confidence_score",
    "detail_parser_confidence",
    "disclosure_signal_class",
    "routine_disclosure_flag",
    "risk_disclosure_flag",
    "high_signal_disclosure_flag",
    "buyback_amount",
    "ehv_transformer_flag",
    "ehv_transformer_voltage_kv",
    "production_slot_reserved_flag",
    "prepayment_flag",
    "medium_voltage_order_flag",
    "switchgear_order_flag",
    "power_equipment_fcf_growth",
    "order_backlog_value",
    "gas_turbine_backlog",
    "transformer_price_increase_pct",
    "data_center_grid_flexibility_flag",
    "ai_power_consumption_twh",
    "grid_investment_savings_pct",
    "water_capacity_needed_mgd",
    "dry_cooling_required_flag",
    "existing_nuclear_ppa_flag",
    "relicense_flag",
    "ferc_pjm_gate_flag",
    "rail_financing_flag",
    "rail_local_content_requirement",
    "rail_warranty_risk_flag",
    "us_shipbuilding_moa_flag",
    "naval_auxiliary_ship_option_flag",
    "yard_capex_uncertain_flag",
    "us_workforce_bottleneck_flag",
    "shipbuilding_procurement_delay_flag",
    "pipe_spool_delay_flag",
    "procurement_lead_time_days",
    "supplier_delay_flag",
    "margin_penalty_flag",
    "orders_only_without_profit_flag",
    "sales_miss_flag",
    "industrial_profit_miss_flag",
    "pre_revenue_smr_flag",
    "loss_widening_flag",
    "commercial_operation_target_year",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def round133_target_for(target_id: str) -> Round133ScoreTarget | None:
    for target in ROUND133_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round133_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND133_CASE_CANDIDATES:
        target = round133_target_for(candidate.target_id)
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
                f"Round133 R1 Loop-8 case for {candidate.target_id}; "
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
            score_price_alignment=_round133_score_price_alignment(candidate),
            rerating_result=_round133_rerating_result(candidate),
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
                "project_delay_capital_allocation_shock_low_margin_mro_smr_false_green_are_loop8_penalties",
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


def round133_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND133_SCORE_TARGETS:
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
                "loop8_penalty_axes": "|".join(target.loop8_penalty_axes),
                "hard_gate": str(target.hard_gate).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round133_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND133_CASE_CANDIDATES:
        target = round133_target_for(candidate.target_id)
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


def round133_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "loop8_penalty_axes": "|".join(target.loop8_penalty_axes),
            "hard_gate": str(target.hard_gate).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND133_SCORE_TARGETS
    )


def round133_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round133_backfill": "true"} for field in ROUND133_PRICE_FIELDS)


def round133_base_score_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(weight.as_row() for weight in ROUND133_BASE_SCORE_WEIGHTS)


def round133_stage_cap_rows() -> tuple[dict[str, str], ...]:
    return tuple(cap.as_row() for cap in ROUND133_STAGE_CAPS)


def round133_score_stage_price_alignment_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND133_SCORE_STAGE_PRICE_ALIGNMENT)


def round133_summary() -> dict[str, int | bool]:
    records = round133_case_records()
    return {
        "target_count": len(ROUND133_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "base_score_component_count": len(ROUND133_BASE_SCORE_WEIGHTS),
        "stage_cap_count": len(ROUND133_STAGE_CAPS),
        "score_stage_price_alignment_count": len(ROUND133_SCORE_STAGE_PRICE_ALIGNMENT),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND133_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND133_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND133_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "hard_gate_target_count": sum(1 for target in ROUND133_SCORE_TARGETS if target.hard_gate),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round133_r1_loop8_reports(
    *,
    output_directory: str | Path = ROUND133_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND133_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND133_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round133_r1_loop8_industrial_infra_summary.md",
        "case_matrix": output / "round133_r1_loop8_case_matrix.csv",
        "stage_date_plan": output / "round133_r1_loop8_stage_date_plan.csv",
        "green_guardrails": output / "round133_r1_loop8_green_guardrails.md",
        "loop8_risk_overlays": output / "round133_r1_loop8_risk_overlays.md",
        "price_validation_plan": output / "round133_r1_loop8_price_validation_plan.md",
        "price_fields": output / "round133_r1_loop8_price_fields.csv",
        "base_score_weights": output / "round133_r1_loop8_base_score_weights.csv",
        "stage_caps": output / "round133_r1_loop8_stage_caps.csv",
        "score_stage_price_alignment": output / "round133_r1_loop8_score_stage_price_alignment.csv",
        "score_stage_price_alignment_md": output / "round133_r1_loop8_score_stage_price_alignment.md",
    }
    _write_case_jsonl(round133_case_records(), cases)
    _write_rows(round133_score_profile_rows(), score_profiles)
    _write_rows(round133_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round133_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round133_price_field_rows(), paths["price_fields"])
    _write_rows(round133_base_score_weight_rows(), paths["base_score_weights"])
    _write_rows(round133_stage_cap_rows(), paths["stage_caps"])
    _write_rows(round133_score_stage_price_alignment_rows(), paths["score_stage_price_alignment"])
    paths["summary"].write_text(render_round133_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round133_green_guardrail_markdown(), encoding="utf-8")
    paths["loop8_risk_overlays"].write_text(render_round133_loop8_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round133_price_validation_plan_markdown(), encoding="utf-8")
    paths["score_stage_price_alignment_md"].write_text(render_round133_score_stage_price_alignment_markdown(), encoding="utf-8")
    return paths


def render_round133_summary_markdown() -> str:
    summary = round133_summary()
    lines = [
        "# Round-133 R1 Loop-8 Industrial Orders / Infrastructure Summary",
        "",
        f"- source_round: `{ROUND133_SOURCE_ROUND_PATH}`",
        "- large_sector: `INDUSTRIAL_ORDERS_INFRA`",
        "- loop: `R1 Loop 8 / v8.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- base_score_component_count: {summary['base_score_component_count']}",
        f"- stage_cap_count: {summary['stage_cap_count']}",
        f"- score_stage_price_alignment_count: {summary['score_stage_price_alignment_count']}",
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
        "- R1 Loop 8 narrows order/backlog candidates after the R13 Loop-7 RedTeam pass.",
        "- Order size is not enough. Green needs contract amount, duration, counterparty, delivery schedule, margin, OP/EPS revision, FCF conversion, and price-path alignment.",
        "- Loop 8 makes score-to-stage-to-price validation explicit: Stage 2 contracts are not Stage 3 until OP/EPS/FCF, margin, and price path line up.",
        "- Loop 8 base score weights are EPS/FCF 25, visibility 22, bottleneck/pricing 18, mispricing 10, valuation room 7, capital discipline 10, information confidence 8.",
        "- Loop 8 keeps EHV transformer export, backlog-to-FCF conversion, grid-flexibility context, nuclear restart approval gates, and data-center power/water gates.",
        "- Example: transformer shortage is strong, but low-margin long-term contracts or data-center project delay can still block Green.",
        "- Example: GE Vernova is score-to-stage-to-price aligned, but its large rerating requires 4B-watch.",
        "- Example: LS Electric 525kV and Hyundai Rotem Morocco rail are Stage 2 until price, margin, OP/EPS, and FCF are backfilled.",
        "- Example: defense backlog can be strong, but share issuance and unclear overseas CAPEX are capital-allocation shocks.",
        "- Example: OpenDART list-only contract evidence is capped until amount, counterparty, duration, and margin detail are checked.",
        "- Example: existing nuclear PPA and SMR policy are separated because cashflow visibility is different.",
    ]
    return "\n".join(lines) + "\n"


def render_round133_green_guardrail_markdown() -> str:
    lines = [
        "# Round-133 R1 Loop-8 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-8 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND133_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.loop8_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R1 Loop-8 v8.0 weights to production scoring yet.",
            "- Do not lower Stage 3-Green thresholds because R1 is Green-capable.",
            "- Do not treat MOU, policy expectation, prototype, or project headline as Green evidence.",
            "- Do not invent contract values, contract dates, counterparties, delivery schedules, margins, or stage prices.",
            "- Treat project delay, capital-allocation shock, low-margin backlog, MRO option-only, and SMR policy false Green as strong penalties.",
            "- Apply disclosure confidence caps when contract amount, counterparty, period, or margin detail is missing.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round133_loop8_risk_overlay_markdown() -> str:
    lines = [
        "# Round-133 R1 Loop-8 Risk Overlays",
        "",
        "- `CONTRACT_QUALITY_ALIGNED`: contract amount, duration, counterparty, delivery schedule, margin, OP/EPS, FCF, and price path align.",
        "- `BACKLOG_WITHOUT_MARGIN`: backlog exists but margin and EPS conversion are unclear.",
        "- `GRID_BOTTLENECK_STRUCTURAL`: lead time, price, import/factory slot, CAPA bottleneck, and revision evidence align.",
        "- `EHV_EXPORT_CONTRACT_ALIGNED`: 525kV/765kV export contract, value, customer use-case, delivery, margin, and OP/EPS evidence align.",
        "- `GRID_SLOT_VISIBILITY`: production-slot prebuy, long-term agreement, or prepayment confirms multi-year delivery visibility.",
        "- `POWER_EQUIPMENT_BACKLOG_TO_FCF`: orders/backlog convert to FCF and buyback/dividend without hiding order-peak risk.",
        "- `DATA_CENTER_POWER_4B`: orders/backlog are strong but valuation is already crowded.",
        "- `DATA_CENTER_PERMITTING_4C`: local opposition, water, grid interconnection, or moratorium breaks project timing.",
        "- `DATA_CENTER_GRID_FLEXIBILITY_REFERENCE`: load-flexibility research is demand context, not company Green evidence.",
        "- `POWER_EQUIPMENT_BACKLOG_ALIGNED`: data-center or turbine equipment backlog connects to guidance, EPS, and FCF.",
        "- `PROJECT_DELAY_RISK`: data-center, rail, nuclear, reconstruction, or infrastructure demand exists but projects are delayed.",
        "- `CAPITAL_ALLOCATION_SHOCK`: order/backlog remains attractive but dilution or funding damages the price path.",
        "- `US_NAVAL_SHIPBUILDING_OPTION`: MoA/MRO/yard partnership is an option until actual contract, CAPEX, schedule, and margin appear.",
        "- `SHIPBUILDING_PROCUREMENT_DELAY_RISK`: pipe spool, supplier, or engineered-to-order procurement delay can break delivery and margin.",
        "- `NAVAL_MRO_OPTION_ONLY`: MRO credential or initial contract exists, but high-margin repeat MRO or newbuild conversion is unproven.",
        "- `EXISTING_NUCLEAR_PPA_ALIGNED`: existing nuclear PPA supports cashflow visibility better than SMR policy talk.",
        "- `NUCLEAR_GRID_INJECTION_GATE`: nuclear restart/PPA needs grid injection rights, interconnection, and restart CAPEX verification.",
        "- `SMR_POLICY_FALSE_GREEN`: SMR policy/thematic demand lacks cost, customer, permit, financing, or revenue confirmation.",
        "- `POLICY_TO_CONTRACT_FAILED`: reconstruction, Neom, or policy infra news does not become funded order or revenue.",
        "- `DISCLOSURE_CONFIDENCE_CAPPED`: contract headline exists, but amount, counterparty, period, or margin detail is missing.",
        "",
        "Simple example: `as_of_date=2025-02-26` and a rail contract is announced. That can be Stage 2 evidence. It is not Stage 3-Green until margin, financing, warranty, delivery schedule, and OP/EPS path are visible as of that date.",
    ]
    return "\n".join(lines) + "\n"


def render_round133_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-133 R1 Loop-8 Price Validation Plan",
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
    for row in round133_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `CONTRACT_QUALITY_ALIGNED`: contract value/duration/counterparty/delivery/margin/EPS and price path align.",
            "- `BACKLOG_WITHOUT_MARGIN`: backlog/order exists but margin or EPS conversion is not proven.",
            "- `EHV_EXPORT_CONTRACT_ALIGNED`: ultra-high-voltage export contract is verified by contract amount, customer, delivery, margin, and OP/EPS path.",
            "- `POWER_EQUIPMENT_BACKLOG_TO_FCF`: backlog converts to FCF and shareholder return, while 4B-watch checks order-peak risk.",
            "- `PROJECT_DELAY_RISK`: demand exists but project execution threatens order growth.",
            "- `DATA_CENTER_PERMITTING_4C`: local opposition, power, water, or moratorium delays block positive equipment evidence.",
            "- `US_NAVAL_SHIPBUILDING_OPTION`: MoA or MRO option remains Watch until signed contract and margin evidence.",
            "- `SHIPBUILDING_PROCUREMENT_DELAY_RISK`: procurement delay threatens delivery, warranty, and margin conversion.",
            "- `CAPITAL_ALLOCATION_SHOCK`: backlog remains attractive but dilution or funding damages price path.",
            "- `NUCLEAR_GRID_INJECTION_GATE`: existing nuclear restart needs interconnection rights, FERC/PJM, and restart CAPEX verification.",
            "- `SMR_POLICY_FALSE_GREEN`: policy and theme exist but cost/customer/permit/financing are missing.",
            "- `POLICY_TO_CONTRACT_FAILED`: policy/MOU does not become funded order or revenue.",
            "- `DISCLOSURE_CONFIDENCE_CAPPED`: OpenDART list or headline evidence is capped until detail fields are parsed.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round133_score_stage_price_alignment_markdown() -> str:
    lines = [
        "# Round-133 R1 Loop-8 Score -> Stage -> Price Alignment",
        "",
        "## Base Score Weights",
        "",
        "| component | points | direction | reason |",
        "| --- | ---: | --- | --- |",
    ]
    for row in ROUND133_BASE_SCORE_WEIGHTS:
        lines.append(f"| `{row.component}` | {row.points} | {row.loop8_direction} | {row.reason} |")
    lines.extend(
        [
            "",
            "## Stage Caps",
            "",
            "| stage band | max score | evidence | examples | Green policy |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for cap in ROUND133_STAGE_CAPS:
        lines.append(
            f"| `{cap.stage_band}` | {cap.max_score} | {', '.join(cap.required_evidence)} | "
            f"{', '.join(cap.example_cases)} | {cap.green_policy} |"
        )
    lines.extend(
        [
            "",
            "## Alignment Cases",
            "",
            "| case | detected stage | price-path status | verdict | adjustment |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    for row in ROUND133_SCORE_STAGE_PRICE_ALIGNMENT:
        lines.append(
            f"| `{row.case_id}` | {row.detected_stage} | {row.price_path_status} | "
            f"{row.verdict} | {row.normalization_adjustment} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- GE Vernova is the cleanest Loop-8 example where score, stage, and short-term price reaction align, but it also turns on 4B-watch.",
            "- LS Electric and Hyundai Rotem are Stage 2 examples: the contract evidence is strong, but Green waits for margin, OP/EPS/FCF, and official price-path backfill.",
            "- Hanwha Aerospace shows why capital discipline is now a larger R1 weight: good defense backlog can be downgraded by dilution shock.",
            "- HD Hyundai-Huntington remains event/watch while it is MoU/MoA-only.",
        ]
    )
    return "\n".join(lines) + "\n"


def _round133_score_price_alignment(candidate: Round133CaseCandidate) -> str:
    if candidate.case_type in {"structural_success", "success_candidate", "cyclical_success"}:
        return "aligned"
    if candidate.case_type in {"event_premium", "overheat", "4b_watch"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "failed_rerating" and "capital_allocation" in candidate.alignment_hint:
        return "evidence_good_but_price_failed"
    return "false_positive_score"


def _round133_rerating_result(candidate: Round133CaseCandidate) -> str:
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
    if value in {"gate", "cap", "+"}:
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
        writer = csv.DictWriter(handle, fieldnames=tuple(rows_tuple[0].keys()), lineterminator="\n")
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow(dict(row))
    return path


__all__ = [
    "ROUND133_CASE_CANDIDATES",
    "ROUND133_BASE_SCORE_WEIGHTS",
    "ROUND133_DEFAULT_CASES_PATH",
    "ROUND133_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND133_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND133_PRICE_FIELDS",
    "ROUND133_SCORE_TARGETS",
    "ROUND133_SCORE_STAGE_PRICE_ALIGNMENT",
    "ROUND133_STAGE_CAPS",
    "Round133CaseCandidate",
    "Round133BaseScoreWeight",
    "Round133ScoreStagePriceAlignment",
    "Round133ScoreTarget",
    "Round133ScoreWeightDraft",
    "Round133StageCap",
    "render_round133_green_guardrail_markdown",
    "render_round133_loop8_risk_overlay_markdown",
    "render_round133_price_validation_plan_markdown",
    "render_round133_score_stage_price_alignment_markdown",
    "render_round133_summary_markdown",
    "round133_base_score_weight_rows",
    "round133_case_candidate_rows",
    "round133_case_records",
    "round133_price_field_rows",
    "round133_score_profile_rows",
    "round133_score_stage_price_alignment_rows",
    "round133_stage_cap_rows",
    "round133_stage_date_rows",
    "round133_summary",
    "round133_target_for",
    "write_round133_r1_loop8_reports",
]
