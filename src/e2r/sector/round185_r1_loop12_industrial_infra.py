"""Round-185 R1 Loop-12 Korea industrial orders and infrastructure pack.

Round 185 returns to R1 with Korea-centered mid/small industrial candidates:
power equipment and cables, defense electronics, space launch programs,
construction equipment, nuclear decommissioning, and shipbuilding equipment.

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


ROUND185_SOURCE_ROUND_PATH = "docs/round/round_185.md"
ROUND185_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round185_r1_loop12_industrial_infra"
ROUND185_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop12_round185.jsonl"
ROUND185_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round185_r1_loop12_v12.csv"
ROUND185_SOURCE_CANONICAL_TARGET_IDS: tuple[str, ...] = (
    "GRID_TRANSFORMER_MIDCAP_KOREA",
    "POWER_CABLE_GRID_BACKLOG_KOREA",
    "DEFENSE_ELECTRONICS_KF21_RADAR",
    "SPACE_LAUNCH_PROGRAM_OF_RECORD",
    "DEFENSE_CAPITAL_RAISE_DILUTION",
    "CONSTRUCTION_EQUIPMENT_CYCLE_KOREA",
    "CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY",
    "NUCLEAR_DECOMMISSIONING_KOREA",
    "NUCLEAR_POLICY_STAGE1_2_NOT_GREEN",
    "SHIPBUILDING_EQUIPMENT_BACKLOG_KOREA",
    "SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK",
    "DISCLOSURE_CONFIDENCE_CAP",
)
ROUND185_SOURCE_CANONICAL_TARGET_COUNT = len(ROUND185_SOURCE_CANONICAL_TARGET_IDS)


@dataclass(frozen=True)
class Round185ScoreWeightDraft:
    eps_fcf_opm: int | str
    contract_customer_visibility: int | str
    bottleneck_pricing: int | str
    early_price_validation: int | str
    capital_governance: int | str
    disclosure_redteam: int | str
    valuation_4b_room: int | str

    def as_dict(self) -> dict[str, int | str]:
        return {
            "eps_fcf_opm": self.eps_fcf_opm,
            "contract_customer_visibility": self.contract_customer_visibility,
            "bottleneck_pricing": self.bottleneck_pricing,
            "early_price_validation": self.early_price_validation,
            "capital_governance": self.capital_governance,
            "disclosure_redteam": self.disclosure_redteam,
            "valuation_4b_room": self.valuation_4b_room,
        }


@dataclass(frozen=True)
class Round185ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round185ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop12_penalty_axes: tuple[str, ...]
    normalization_point: str
    hard_gate: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.INDUSTRIAL_ORDERS_INFRA

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round185CaseCandidate:
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
class Round185BaseScoreWeight:
    component: str
    points: int
    loop12_direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {
            "component": self.component,
            "points": str(self.points),
            "loop12_direction": self.loop12_direction,
            "reason": self.reason,
            "production_scoring_changed": "false",
        }


@dataclass(frozen=True)
class Round185StageCap:
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
            "production_scoring_changed": "false",
        }


@dataclass(frozen=True)
class Round185ScoreStagePriceAlignment:
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
            "production_scoring_changed": "false",
        }


ROUND185_BASE_SCORE_WEIGHTS: tuple[Round185BaseScoreWeight, ...] = (
    Round185BaseScoreWeight("eps_fcf_opm_conversion", 24, "keep_high", "R1 Loop 12 still starts with OP/EPS/FCF and OPM conversion, not order headlines."),
    Round185BaseScoreWeight("contract_backlog_customer_visibility", 20, "detail_required", "Customer, amount, period, delivery schedule, government program, and recurring service define Stage 2 quality."),
    Round185BaseScoreWeight("bottleneck_pricing_power", 16, "sector_specific", "Transformer lead time, cable backlog, radar localization, and shipbuilding equipment shortage are useful only when they convert to margin."),
    Round185BaseScoreWeight("early_price_path_validation", 12, "required_backfill", "Stage 2 이후 MFE, relative strength, event return, and volume decide whether the market is validating or overheating."),
    Round185BaseScoreWeight("capital_discipline_governance", 10, "raised_for_loop12", "Hanwha Aerospace dilution and Doosan Bobcat governance show why capital discipline must be visible in R1."),
    Round185BaseScoreWeight("disclosure_confidence_hard_redteam", 10, "hard_review", "OpenDART detail, customer/amount/period/margin, regulator correction, MOU/LOI, and hard RedTeam cap Green."),
    Round185BaseScoreWeight("valuation_room_4b_runway", 8, "cool_crowded_names", "Good structures with price-only rotation or peer top-quartile valuation should move to 4B-watch."),
)


ROUND185_STAGE_CAPS: tuple[Round185StageCap, ...] = (
    Round185StageCap(
        "Stage 1",
        "45",
        ("ai_grid_demand", "kf21_radar_story", "space_launch_story", "nuclear_policy", "shipbuilding_equipment_story", "construction_cycle_recovery"),
        ("nuclear_policy_stage1_2_not_green_case", "nuclear_decommissioning_policy_stage1_2_case"),
        "Green blocked until company-level contract, delivery, margin, or OP/EPS/FCF evidence appears.",
    ),
    Round185StageCap(
        "Stage 2",
        "70",
        ("contract_amount", "customer_name", "delivery_schedule", "program_budget", "radar_batch_production", "actual_khnp_contract", "shipyard_backlog_link"),
        ("hanwha_system_kf21_aesa_radar_stage2_case", "hanwha_aerospace_kslv_program_stage2_case"),
        "Stage 2 can be strong, but Green waits for revenue, OPM/FCF, and clean capital/governance.",
    ),
    Round185StageCap(
        "Stage 3",
        "requires_5_of_8",
        ("customer_amount_period_confirmed", "backlog_growth_long_delivery", "op_eps_revision_or_beat", "opm_or_fcf_improvement", "60d_mfe_20pct", "relative_strength_vs_market", "no_dilution_governance_hard_issue", "valuation_not_overheated"),
        ("iljin_midcap_transformer_stage3_candidate_case", "shipbuilding_equipment_backlog_stage3_candidate_case"),
        "Stage 3 early catch is possible only when contract detail, earnings conversion, price path, and RedTeam are aligned.",
    ),
    Round185StageCap(
        "Stage 4B",
        "requires_4_of_6",
        ("stage2_120d_mfe_80pct", "basket_rally_without_contract_detail", "price_faster_than_revision", "crowded_reports_news_community", "peer_top_quartile_valuation", "entry_return_depends_on_narrative_not_fcf"),
        ("power_equipment_midcap_basket_4b_watch_case", "nuclear_decommissioning_policy_stage1_2_case"),
        "R1 Loop 12 cools late rotations before they are mislabeled as fresh Stage 3.",
    ),
    Round185StageCap(
        "Stage 4C",
        "hard_gate",
        ("large_capital_raise_cb_bw_dilution", "fss_revision_request", "controversial_merger_or_minority_damage", "contract_cancel_or_correction", "legal_sanction_export_restriction", "dealer_inventory_or_equipment_demand_drop", "satellite_investment_loss_or_strategy_retreat", "mou_loi_media_only_without_contract"),
        ("hanwha_aerospace_capital_raise_dilution_case", "doosan_bobcat_governance_cap_case"),
        "A single hard capital, governance, demand-cycle, legal, or disclosure-confidence issue can block Green.",
    ),
)


def _w(
    eps: int | str,
    visibility: int | str,
    bottleneck: int | str,
    price: int | str,
    capital: int | str,
    disclosure: int | str,
    valuation: int | str,
) -> Round185ScoreWeightDraft:
    return Round185ScoreWeightDraft(eps, visibility, bottleneck, price, capital, disclosure, valuation)


CAP_WEIGHT = _w("cap", "cap", "cap", "cap", "cap", "cap", "+")
GATE_WEIGHT = _w("gate", "gate", "gate", "gate", "gate", "gate", "gate")


ROUND185_SCORE_TARGETS: tuple[Round185ScoreTarget, ...] = (
    Round185ScoreTarget(
        "GRID_TRANSFORMER_MIDCAP_KOREA",
        E2RArchetype.GRID_TRANSFORMER_MIDCAP_KOREA,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(24, 20, 16, 12, 10, 10, 8),
        ("ai_data_center_grid_demand", "us_transformer_shortage", "long_lead_time", "transformer_price_increase"),
        ("customer_name", "contract_amount", "delivery_period", "backlog_growth", "op_eps_revision"),
        ("op_eps_fcf_revision", "opm_improvement", "lead_time_power", "60d_mfe_20pct", "relative_strength"),
        ("midcap_power_basket_rotation", "price_2x_3x_before_revision", "peer_top_quartile_valuation"),
        ("customer_project_delay", "capa_normalization", "raw_material_cost_spike", "margin_miss"),
        ("customer_name", "contract_amount", "delivery_period", "backlog_quality", "op_eps_revision", "opm_improvement"),
        ("customer_missing", "counterparty_missing", "price_only_rally", "margin_unknown", "capa_normalization"),
        ("customer_missing", "price_only_rally", "margin_unknown"),
        "Iljin/JeRyoung-style midcap transformer candidates can be early Stage 3 only with contract detail and OP/EPS conversion.",
    ),
    Round185ScoreTarget(
        "POWER_CABLE_GRID_BACKLOG_KOREA",
        E2RArchetype.POWER_CABLE_GRID_BACKLOG_KOREA,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(23, 21, 15, 12, 10, 10, 8),
        ("power_cable_shortage", "ehv_cable", "subsea_cable", "us_grid_expansion", "data_center_power_grid"),
        ("cable_contract", "customer_name", "contract_amount", "delivery_period", "copper_passthrough", "margin_path"),
        ("op_eps_revision", "margin_visible", "copper_passthrough_working", "delivery_visibility", "60d_mfe_20pct"),
        ("cable_basket_rotation", "contract_detail_missing_rally", "price_faster_than_revision"),
        ("copper_cost_mismatch", "low_margin_order", "customer_missing", "delivery_delay"),
        ("contract_amount", "counterparty", "contract_period", "margin_visible", "op_eps_revision"),
        ("customer_missing", "margin_unknown", "copper_passthrough_missing", "price_only_rotation"),
        ("customer_missing", "low_margin_order", "copper_cost_risk"),
        "Power cable names need contract quality, copper pass-through, margin, and delivery schedule before Green.",
    ),
    Round185ScoreTarget(
        "DEFENSE_ELECTRONICS_KF21_RADAR",
        E2RArchetype.DEFENSE_ELECTRONICS_KF21_RADAR,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(20, 20, 15, 10, 10, 10, 8),
        ("kf21_localization", "aesa_radar", "apy016k", "defense_electronics"),
        ("kf21_batch_production", "radar_delivery_visibility", "avionics_supply", "government_program"),
        ("radar_revenue_recognition", "defense_electronics_opm", "block2_or_export_demand", "repeat_delivery"),
        ("kf21_keyword_rally_before_revenue", "defense_electronics_story_crowded"),
        ("revenue_missing", "opm_missing", "export_contract_missing", "program_delay"),
        ("radar_delivery", "revenue_recognition", "opm_visible", "repeat_delivery"),
        ("actual_revenue_missing", "opm_missing", "export_contract_missing"),
        ("revenue_missing", "opm_missing", "program_delay"),
        "KF-21 AESA radar is Stage 2-quality evidence, but radar revenue and OPM gate Stage 3.",
    ),
    Round185ScoreTarget(
        "SPACE_LAUNCH_PROGRAM_OF_RECORD",
        E2RArchetype.SPACE_LAUNCH_PROGRAM_OF_RECORD,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 21, 12, 12, 10, 10, 8),
        ("kslv_iii", "next_generation_launcher", "government_program_of_record", "sole_bidder"),
        ("program_budget", "government_allocation", "long_cycle_rd", "price_path_12pct"),
        ("contract_signed", "milestone_delivery", "space_revenue_recognition", "opm_fcf_improvement", "dilution_absorbed"),
        ("space_launch_name_rally", "program_priced_before_contract"),
        ("capital_raise", "fss_revision_request", "rd_cost_overrun", "dilution"),
        ("contract_signed", "program_budget", "milestone_delivery", "opm_fcf_visible", "capital_clean"),
        ("capital_raise", "dilution", "fss_revision_request", "contract_missing"),
        ("capital_raise", "dilution", "rd_cost_overrun"),
        "Space launch program visibility is strong Stage 2, not Green until contract economics and capital discipline are clean.",
    ),
    Round185ScoreTarget(
        "DEFENSE_CAPITAL_RAISE_DILUTION",
        E2RArchetype.DEFENSE_CAPITAL_RAISE_DILUTION,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("large_rights_offering", "capital_raise_plan", "regulator_review"),
        ("dilution_terms_identified", "use_of_proceeds_needed"),
        ("not_green_until_dilution_and_use_of_proceeds_absorbed",),
        ("defense_backlog_rally_meets_capital_shock",),
        ("large_capital_raise", "fss_revision_request", "share_price_drop", "dilution_uncertainty"),
        (),
        ("large_capital_raise", "fss_revision_request", "dilution", "use_of_proceeds_unclear"),
        ("large_capital_raise", "fss_revision_request", "dilution"),
        "Defense order quality is capped when dilution or regulator correction breaks capital discipline.",
        hard_gate=True,
    ),
    Round185ScoreTarget(
        "CONSTRUCTION_EQUIPMENT_CYCLE_KOREA",
        E2RArchetype.CONSTRUCTION_EQUIPMENT_CYCLE_KOREA,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(18, 12, 10, 8, 10, 10, 8),
        ("infrastructure_demand", "compact_equipment", "north_america_construction", "emerging_market_demand"),
        ("exports_up", "dealer_inventory_normalization", "asp_or_opm_improvement"),
        ("op_eps_revision", "dealer_inventory_stable", "parts_service_growth", "fcf_improvement"),
        ("machinery_cycle_rally", "construction_equipment_valuation_crowded"),
        ("high_borrowing_cost", "dealer_inventory_rise", "china_real_estate_weakness", "tariff_cost", "global_equipment_warning"),
        ("dealer_inventory_stable", "op_eps_revision", "fcf_improvement"),
        ("dealer_inventory_risk", "high_borrowing_cost", "global_machinery_warning", "china_real_estate"),
        ("dealer_inventory", "high_borrowing_cost", "demand_drop"),
        "Construction equipment is an R1 cycle watch; Green is restricted until dealer inventory and FCF are stable.",
    ),
    Round185ScoreTarget(
        "CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY",
        E2RArchetype.CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("value_up_story", "holding_restructuring", "minority_shareholder_concern"),
        ("controversial_restructuring", "share_exchange_ratio", "governance_discount_identified"),
        ("not_green_until_governance_resolved_and_minorities_protected",),
        ("value_up_rally_ignores_governance",),
        ("minority_shareholder_damage", "controversial_merger", "governance_discount_expands"),
        ("governance_resolved", "minority_shareholder_protected", "cashflow_not_transferred_away"),
        ("minority_shareholder_risk", "controversial_restructuring", "governance_discount"),
        ("minority_shareholder_risk", "controversial_restructuring", "governance_discount"),
        "Doosan Bobcat-style cash flow can be capped by governance and minority shareholder value risk.",
        hard_gate=True,
    ),
    Round185ScoreTarget(
        "NUCLEAR_DECOMMISSIONING_KOREA",
        E2RArchetype.NUCLEAR_DECOMMISSIONING_KOREA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(16, 18, 8, 10, 10, 10, 8),
        ("kori_1_decommissioning_approval", "nuclear_decommissioning", "waste_handling", "maintenance_service"),
        ("khnp_service_contract", "contract_amount", "contract_period", "company_scope_confirmed"),
        ("repeat_decommissioning_revenue", "opm_fcf_improvement", "additional_pipeline", "price_path_aligned"),
        ("policy_news_rally_without_contract", "nuclear_decommissioning_theme_crowded"),
        ("company_contract_missing", "opm_fcf_missing", "project_delay", "policy_only"),
        ("actual_khnp_contract", "company_scope", "opm_fcf_visible", "repeat_pipeline"),
        ("company_contract_missing", "policy_only", "opm_missing"),
        ("contract_missing", "policy_only", "opm_missing"),
        "Kori-1 approval is Stage 1/2 policy visibility; individual suppliers need KHNP contract economics before Green.",
    ),
    Round185ScoreTarget(
        "NUCLEAR_POLICY_STAGE1_2_NOT_GREEN",
        E2RArchetype.NUCLEAR_POLICY_STAGE1_2_NOT_GREEN,
        Round10ThemePosture.REDTEAM_FIRST,
        CAP_WEIGHT,
        ("national_energy_plan", "large_reactor_policy", "smr_policy", "nuclear_generation_mix"),
        ("policy_to_project_visibility", "macro_project_budget"),
        ("not_green_until_company_contract_revenue_margin",),
        ("nuclear_policy_rally_before_scope",),
        ("policy_reversal", "company_scope_missing", "contract_missing", "margin_unknown"),
        ("company_contract", "revenue_recognition", "opm_visible", "fcf_visible"),
        ("policy_only", "contract_missing", "scope_unknown"),
        ("policy_only", "contract_missing", "scope_unknown"),
        "Nuclear policy is not individual-company Stage 3 evidence.",
    ),
    Round185ScoreTarget(
        "SHIPBUILDING_EQUIPMENT_BACKLOG_KOREA",
        E2RArchetype.SHIPBUILDING_EQUIPMENT_BACKLOG_KOREA,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(22, 20, 16, 12, 10, 10, 8),
        ("shipyard_backlog", "lng_ship_equipment", "ship_engine", "fitting_valve", "offshore_module"),
        ("yard_customer_backlog", "delivery_schedule", "engine_or_module_visibility", "order_to_revenue_path"),
        ("equipment_delivery_to_revenue", "opm_improvement", "low_margin_orders_cleared", "60d_mfe_20pct"),
        ("shipbuilding_body_rally_then_equipment_rotation", "price_only_rotation"),
        ("delivery_schedule_missing", "opm_missing", "yard_order_delay", "low_margin_equipment"),
        ("customer_yard_backlog", "delivery_schedule", "opm_visible", "op_eps_revision", "fcf_visible"),
        ("delivery_missing", "opm_missing", "price_only_rotation", "low_margin_order"),
        ("delivery_missing", "opm_missing", "yard_delay"),
        "Shipbuilding equipment can be Stage 3 when yard backlog converts to delivery, margin, and FCF.",
    ),
    Round185ScoreTarget(
        "SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK",
        E2RArchetype.SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("satellite_theme", "oneweb", "leo_communications", "starlink_competition"),
        ("equity_investment", "space_option", "strategy_pivot"),
        ("not_green_until_civil_or_defense_satellite_revenue_and_capital_allocation_proven",),
        ("satellite_theme_rally_ignores_write_down",),
        ("eutelsat_stake_sale", "investment_loss", "civilian_leo_strategy_retreat", "capital_allocation_damage"),
        ("capital_allocation_clean", "satellite_revenue_visible", "defense_satellite_contract"),
        ("investment_loss", "strategy_retreat", "theme_without_revenue"),
        ("investment_loss", "strategy_retreat", "theme_without_revenue"),
        "Satellite theme options are capped when capital allocation losses or strategy retreat appear.",
        hard_gate=True,
    ),
    Round185ScoreTarget(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        CAP_WEIGHT,
        ("opendart_list_only", "media_report", "mou", "loi", "non_binding", "policy_event"),
        ("detail_fetch_required", "customer_amount_period_margin_required"),
        ("not_green_until_binding_detail_and_eps_fcf_path",),
        ("headline_priced_before_detail",),
        ("contract_amount_missing", "customer_missing", "period_missing", "margin_unknown", "final_contract_missing"),
        ("binding_contract", "contract_amount", "customer_name", "contract_period", "margin_visible"),
        ("opendart_list_only", "media_only", "mou_loi", "non_binding", "detail_missing"),
        ("opendart_list_only", "media_only", "mou_loi", "non_binding", "detail_missing"),
        "R1 Loop 12 uses OpenDART detail and binding contract data as a Green confidence gate.",
    ),
)


ROUND185_CASE_CANDIDATES: tuple[Round185CaseCandidate, ...] = (
    Round185CaseCandidate(
        "iljin_midcap_transformer_stage3_candidate_case",
        "GRID_TRANSFORMER_MIDCAP_KOREA",
        "103590",
        "일진전기",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("us_grid_transformer_demand", "long_lead_time", "contract_detail_needed", "op_eps_revision_needed", "60d_mfe_backfill_needed"),
        ("customer_missing", "contract_period_missing", "opm_unconfirmed", "price_only_rally"),
        "stage2_to_stage3_candidate_needs_contract_opm_price_backfill",
        "needs_contract_op_revision_price_backfill",
        ("round_185.md Reuters US transformer shortage",),
        "Iljin Electric remains a Stage 2~3 candidate only when contract detail, OPM, OP/EPS, and price path align.",
        (E2RArchetype.STRUCTURAL_STAGE3_EARLY_CAPTURE, E2RArchetype.DISCLOSURE_CONFIDENCE_CAP),
    ),
    Round185CaseCandidate(
        "daehan_gaon_power_cable_stage3_candidate_case",
        "POWER_CABLE_GRID_BACKLOG_KOREA",
        "001440/000500",
        "대한전선·가온전선 power cable basket",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("ehv_cable", "subsea_cable", "us_grid_expansion", "data_center_power_grid", "copper_passthrough_needed"),
        ("customer_missing", "margin_unknown", "copper_passthrough_missing", "price_only_rotation"),
        "power_cable_stage3_candidate_but_margin_and_customer_gate",
        "needs_contract_margin_copper_price_backfill",
        ("round_185.md power cable grid backlog section",),
        "Power cable names are Stage 2~3 candidates only if customer, amount, delivery, copper pass-through, and margin are visible.",
        (E2RArchetype.DISCLOSURE_CONFIDENCE_CAP, E2RArchetype.STRUCTURAL_STAGE3_EARLY_CAPTURE),
    ),
    Round185CaseCandidate(
        "power_equipment_midcap_basket_4b_watch_case",
        "GRID_TRANSFORMER_MIDCAP_KOREA",
        "103590/001440/000500",
        "전력설비 중소형 basket price-only rotation",
        "KR",
        "4b_watch",
        None,
        None,
        None,
        None,
        None,
        ("power_equipment_keyword_rotation", "stage2_120d_mfe_backfill_needed", "relative_strength_backfill_needed"),
        ("contract_detail_missing", "op_eps_revision_missing", "price_only_rally", "peer_top_quartile_valuation"),
        "stage4b_watch_if_keyword_rotation_runs_ahead_of_revision",
        "needs_mfe_mae_revision_valuation_backfill",
        ("round_185.md Stage 4B early conversion condition",),
        "Midcap power equipment can be a valid early catch, but keyword-only rotation after large-cap winners is 4B-watch.",
        (E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH,),
    ),
    Round185CaseCandidate(
        "hanwha_system_kf21_aesa_radar_stage2_case",
        "DEFENSE_ELECTRONICS_KF21_RADAR",
        "272210",
        "한화시스템 KF-21 AESA radar",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("kf21_aesa_radar", "apy016k", "batch_production_option", "defense_electronics_visibility"),
        ("radar_revenue_missing", "opm_missing", "export_contract_missing"),
        "stage2_program_visibility_not_green_before_revenue_opm",
        "needs_radar_delivery_revenue_opm_price_backfill",
        ("round_185.md KF-21 AESA radar section",),
        "Hanwha Systems has Stage 2 radar visibility, but Stage 3 waits for delivery, revenue, OPM, and follow-on/export demand.",
        (E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG,),
    ),
    Round185CaseCandidate(
        "hanwha_aerospace_kslv_program_stage2_case",
        "SPACE_LAUNCH_PROGRAM_OF_RECORD",
        "012450",
        "한화에어로스페이스 KSLV-III program",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("kslv_iii_sole_bidder", "program_budget_2tn_krw", "government_program_of_record", "intraday_plus_12pct"),
        ("contract_missing", "opm_fcf_missing", "capital_raise_watch"),
        "stage2_strong_program_requires_contract_economics_and_clean_capital",
        "needs_contract_milestone_opm_fcf_price_backfill",
        ("round_185.md WSJ Hanwha Aerospace KSLV-III",),
        "KSLV-III is Stage 2 strong, not Green before contract economics and clean capital discipline.",
        (E2RArchetype.DEFENSE_GOVERNMENT_BACKLOG, E2RArchetype.DEFENSE_CAPITAL_RAISE_DILUTION),
    ),
    Round185CaseCandidate(
        "hanwha_aerospace_capital_raise_dilution_case",
        "DEFENSE_CAPITAL_RAISE_DILUTION",
        "012450",
        "한화에어로스페이스 capital raise dilution watch",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("large_capital_raise", "fss_revision_request", "share_price_minus_13pct", "rights_offering_plan"),
        ("dilution", "fss_revision_request", "use_of_proceeds_unclear", "disclosure_confidence_hit"),
        "good_defense_backlog_cooled_by_capital_discipline_hard_gate",
        "needs_dilution_terms_price_mae_backfill",
        ("round_185.md Reuters Hanwha Aerospace capital raise",),
        "Hanwha Aerospace is the core Stage 2 strong plus capital RedTeam case: dilution can block Stage 3 even when backlog is strong.",
        (E2RArchetype.SPACE_LAUNCH_PROGRAM_OF_RECORD,),
    ),
    Round185CaseCandidate(
        "doosan_bobcat_governance_cap_case",
        "CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY",
        "241560",
        "두산밥캣 governance value-up contradiction",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("value_up_story", "cash_flow_business", "controversial_restructuring", "share_exchange_criticism"),
        ("minority_shareholder_risk", "governance_discount", "controlling_family_benefit_risk"),
        "cash_flow_candidate_capped_by_governance_overlay",
        "needs_governance_event_price_backfill",
        ("round_185.md FT Doosan Bobcat restructuring",),
        "Doosan Bobcat can have good cash flow, but governance and minority shareholder risk cap rerating.",
        (E2RArchetype.CONSTRUCTION_EQUIPMENT_CYCLE_KOREA,),
    ),
    Round185CaseCandidate(
        "construction_equipment_global_cycle_4c_watch_case",
        "CONSTRUCTION_EQUIPMENT_CYCLE_KOREA",
        "241560/042670/267270",
        "두산밥캣·HD현대인프라코어·HD현대건설기계 cycle watch",
        "KR",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("infrastructure_demand", "export_exposure", "machinery_cycle"),
        ("dealer_inventory_risk", "high_borrowing_cost", "china_real_estate_weakness", "global_equipment_warning"),
        "watch_red_until_inventory_and_fcf_are_stable",
        "needs_inventory_opm_fcf_price_backfill",
        ("round_185.md Reuters Caterpillar warning", "round_185.md Reuters CNH warning"),
        "Construction equipment stays Watch/Red when global demand cycle, dealer inventory, and borrowing-cost warnings dominate.",
    ),
    Round185CaseCandidate(
        "nuclear_decommissioning_policy_stage1_2_case",
        "NUCLEAR_DECOMMISSIONING_KOREA",
        "083650/457550/046120",
        "비에이치아이·우진엔텍·오르비텍 nuclear decommissioning option",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("kori_1_decommissioning_approval", "twelve_year_project", "project_cost_1_1tn_krw", "waste_handling"),
        ("company_contract_missing", "opm_fcf_missing", "policy_only_rally"),
        "stage1_2_policy_option_not_green_before_khnp_contract",
        "needs_khnp_contract_scope_opm_price_backfill",
        ("round_185.md Reuters Kori-1 decommissioning approval",),
        "Kori-1 decommissioning is a useful Stage 1/2 option, but individual stocks need actual KHNP contract scope and economics.",
        (E2RArchetype.NUCLEAR_POLICY_STAGE1_2_NOT_GREEN, E2RArchetype.DISCLOSURE_CONFIDENCE_CAP),
    ),
    Round185CaseCandidate(
        "nuclear_policy_stage1_2_not_green_case",
        "NUCLEAR_POLICY_STAGE1_2_NOT_GREEN",
        "KR_NUCLEAR_POLICY",
        "Korea nuclear policy macro not company Green",
        "KR",
        "event_premium",
        None,
        None,
        None,
        None,
        None,
        ("two_large_reactors_policy", "smr_policy", "nuclear_generation_mix_target"),
        ("company_scope_missing", "contract_missing", "margin_unknown", "policy_only"),
        "macro_policy_can_route_research_but_not_company_stage3",
        "needs_company_contract_revenue_backfill",
        ("round_185.md Reuters Korea nuclear energy plan",),
        "National nuclear policy is macro evidence; it cannot create company-level Stage 3 without signed scope and margin.",
        (E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,),
    ),
    Round185CaseCandidate(
        "shipbuilding_equipment_backlog_stage3_candidate_case",
        "SHIPBUILDING_EQUIPMENT_BACKLOG_KOREA",
        "082740/014620/023160/013030",
        "한화엔진·성광벤드·태광·하이록코리아 shipbuilding equipment basket",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("shipyard_backlog", "ship_engine_visibility", "lng_ship_equipment", "fitting_valve", "delivery_schedule_needed"),
        ("delivery_missing", "opm_missing", "price_only_rotation", "yard_order_delay"),
        "stage2_to_stage3_candidate_needs_delivery_opm_fcf",
        "needs_delivery_opm_revision_price_backfill",
        ("round_185.md Reuters Hanwha Dyna-Mac / HSD Engine context",),
        "Shipbuilding equipment can become Stage 3 when yard backlog converts to equipment delivery, OPM, and FCF.",
        (E2RArchetype.STRUCTURAL_STAGE3_EARLY_CAPTURE,),
    ),
    Round185CaseCandidate(
        "hanwha_system_eutelsat_loss_4c_watch_case",
        "SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK",
        "272210",
        "한화시스템 Eutelsat OneWeb investment loss",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("eutelsat_stake_sale", "oneweb_investment_loss", "civilian_leo_strategy_retreat", "defense_satellite_pivot"),
        ("investment_loss", "capital_allocation_damage", "strategy_retreat", "theme_without_revenue"),
        "satellite_theme_capped_by_capital_allocation_loss",
        "needs_investment_loss_price_backfill",
        ("round_185.md Reuters Hanwha Eutelsat stake sale",),
        "Hanwha Systems can be Stage 2 in defense electronics while satellite capital allocation remains a 4C-watch overlay.",
        (E2RArchetype.DEFENSE_ELECTRONICS_KF21_RADAR,),
    ),
    Round185CaseCandidate(
        "r1_loop12_disclosure_confidence_reference_case",
        "DISCLOSURE_CONFIDENCE_CAP",
        "R1_DISCLOSURE_CAP",
        "R1 Loop 12 OpenDART detail confidence reference",
        "KR",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("watch_disclosure_detail_required", "contract_amount_to_sales_required", "counterparty_required", "contract_period_required"),
        ("opendart_list_only", "media_only", "mou_loi", "non_binding", "detail_missing"),
        "list_only_or_media_only_cannot_create_green",
        "needs_opendart_detail_parser_backfill",
        ("round_185.md OpenDART detail-fetch requirement",),
        "R1 Loop 12 explicitly requires detail fetch for watch disclosures and forbids invented missing fields.",
    ),
)


ROUND185_SCORE_STAGE_PRICE_ALIGNMENT: tuple[Round185ScoreStagePriceAlignment, ...] = (
    Round185ScoreStagePriceAlignment("iljin_midcap_transformer_stage3_candidate_case", "Stage 2~3 candidate", "KRX and KOSPI/KOSDAQ relative strength backfill required", "stage3_candidate_if_contract_opm_price_align", "credit grid bottleneck; cap if customer/period/OPM missing"),
    Round185ScoreStagePriceAlignment("hanwha_system_kf21_aesa_radar_stage2_case", "Stage 2", "Program visibility exists; revenue and OPM price validation missing", "stage2_not_green_yet", "credit radar localization but require delivery revenue and OPM"),
    Round185ScoreStagePriceAlignment("hanwha_aerospace_capital_raise_dilution_case", "Stage 2 strong -> 4C-watch", "KSLV/K-defense price path can be interrupted by FSS correction and dilution", "capital_redteam_blocks_green", "apply capital discipline hard gate"),
    Round185ScoreStagePriceAlignment("doosan_bobcat_governance_cap_case", "Stage 2 candidate -> governance cap", "Value-up cash flow story can be discounted by minority-shareholder risk", "governance_cap_blocks_green", "apply governance overlay until resolved"),
    Round185ScoreStagePriceAlignment("nuclear_decommissioning_policy_stage1_2_case", "Stage 1~2", "Policy/project size can move theme stocks before company contract economics", "policy_to_contract_not_green", "credit policy visibility but require KHNP contract and OPM"),
    Round185ScoreStagePriceAlignment("shipbuilding_equipment_backlog_stage3_candidate_case", "Stage 2~3 candidate", "Yard backlog must convert to delivery, OPM, FCF, and own price path", "stage3_candidate_if_delivery_margin_convert", "do not borrow shipbuilder price path without equipment evidence"),
)


ROUND185_PRICE_FIELDS: tuple[str, ...] = (
    "ticker",
    "company_name",
    "canonical_archetype",
    "case_type",
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
    "relative_strength_vs_kosdaq",
    "relative_strength_vs_industrial_basket",
    "relative_strength_vs_power_equipment_basket",
    "relative_strength_vs_defense_basket",
    "relative_strength_vs_shipbuilding_equipment_basket",
    "contract_amount",
    "contract_counterparty",
    "contract_period",
    "contract_amount_to_prior_sales",
    "product_or_service",
    "backlog",
    "delivery_schedule",
    "government_program_flag",
    "program_budget",
    "recurring_service_flag",
    "op_revision_before_stage3",
    "op_revision_after_stage3",
    "eps_revision_before_stage3",
    "eps_revision_after_stage3",
    "opm",
    "fcf_signal",
    "cash_conversion_signal",
    "capital_raise_flag",
    "cb_bw_flag",
    "dilution_type",
    "fss_revision_request_flag",
    "governance_risk_flag",
    "minority_shareholder_risk_flag",
    "media_report_only_flag",
    "mou_loi_flag",
    "non_binding_flag",
    "disclosure_confidence",
    "valuation_at_stage3",
    "valuation_at_stage4b",
)


def round185_target_for(target_id: str) -> Round185ScoreTarget | None:
    for target in ROUND185_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round185_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND185_CASE_CANDIDATES:
        target = round185_target_for(candidate.target_id)
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
                f"Round185 R1 Loop-12 Korea industrial case for {candidate.target_id}; "
                "calibration-only and focused on contract detail, OP/EPS/FCF conversion, price path, capital discipline, governance, and disclosure confidence."
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
            score_price_alignment=_round185_score_price_alignment(candidate),
            rerating_result=_round185_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint={
                "eps_fcf": _numeric_weight(weights["eps_fcf_opm"]),
                "visibility": _numeric_weight(weights["contract_customer_visibility"]),
                "bottleneck": _numeric_weight(weights["bottleneck_pricing"]),
                "early_price_validation": _numeric_weight(weights["early_price_validation"]),
                "capital_governance": _numeric_weight(weights["capital_governance"]),
                "disclosure_redteam": _numeric_weight(weights["disclosure_redteam"]),
                "valuation_4b_room": _numeric_weight(weights["valuation_4b_room"]),
            },
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "stage3_early_catch_requires_5_of_8_loop12_conditions",
                "require_contract_detail_op_eps_fcf_price_path_for_green",
                "capital_raise_governance_and_disclosure_confidence_can_block_green",
                "policy_mou_loi_media_only_cannot_create_stage3",
                "do_not_invent_contract_prices_margins_mfe_mae_or_counterparties",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.75
                if candidate.stage1_date or candidate.stage2_date or candidate.stage3_date or candidate.stage4b_date or candidate.stage4c_date
                else 0.2,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round185_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND185_SCORE_TARGETS:
        weights = target.score_weight.as_dict()
        rows.append(
            {
                "target_id": target.target_id,
                "large_sector": target.large_sector.value,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "eps_fcf_opm": str(weights["eps_fcf_opm"]),
                "contract_customer_visibility": str(weights["contract_customer_visibility"]),
                "bottleneck_pricing": str(weights["bottleneck_pricing"]),
                "early_price_validation": str(weights["early_price_validation"]),
                "capital_governance": str(weights["capital_governance"]),
                "disclosure_redteam": str(weights["disclosure_redteam"]),
                "valuation_4b_room": str(weights["valuation_4b_room"]),
                "stage1_signals": "|".join(target.stage1_signals),
                "stage2_signals": "|".join(target.stage2_signals),
                "stage3_conditions": "|".join(target.stage3_conditions),
                "stage4b_conditions": "|".join(target.stage4b_conditions),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "loop12_penalty_axes": "|".join(target.loop12_penalty_axes),
                "hard_gate": str(target.hard_gate).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round185_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND185_CASE_CANDIDATES:
        target = round185_target_for(candidate.target_id)
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


def round185_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "red_flags": "|".join(target.red_flags),
            "hard_gate": str(target.hard_gate).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND185_SCORE_TARGETS
    )


def round185_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round185_backfill": "true"} for field in ROUND185_PRICE_FIELDS)


def round185_base_score_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND185_BASE_SCORE_WEIGHTS)


def round185_stage_cap_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND185_STAGE_CAPS)


def round185_score_stage_price_alignment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND185_SCORE_STAGE_PRICE_ALIGNMENT)


def round185_summary() -> dict[str, int | bool]:
    records = round185_case_records()
    return {
        "target_count": len(ROUND185_SCORE_TARGETS),
        "source_canonical_target_count": ROUND185_SOURCE_CANONICAL_TARGET_COUNT,
        "case_candidate_count": len(records),
        "base_score_axis_count": len(ROUND185_BASE_SCORE_WEIGHTS),
        "stage_cap_count": len(ROUND185_STAGE_CAPS),
        "score_stage_price_alignment_count": len(ROUND185_SCORE_STAGE_PRICE_ALIGNMENT),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "hard_gate_target_count": sum(1 for target in ROUND185_SCORE_TARGETS if target.hard_gate),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round185_r1_loop12_reports(
    *,
    output_directory: str | Path = ROUND185_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND185_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND185_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round185_r1_loop12_industrial_infra_summary.md",
        "case_matrix": output / "round185_r1_loop12_case_matrix.csv",
        "stage_date_plan": output / "round185_r1_loop12_stage_date_plan.csv",
        "green_guardrails": output / "round185_r1_loop12_green_guardrails.md",
        "risk_overlays": output / "round185_r1_loop12_risk_overlays.md",
        "price_validation_plan": output / "round185_r1_loop12_price_validation_plan.md",
        "price_fields": output / "round185_r1_loop12_price_fields.csv",
        "base_score_weights": output / "round185_r1_loop12_base_score_weights.csv",
        "stage_caps": output / "round185_r1_loop12_stage_caps.csv",
        "score_stage_price_alignment": output / "round185_r1_loop12_score_stage_price_alignment.csv",
        "score_stage_price_alignment_md": output / "round185_r1_loop12_score_stage_price_alignment.md",
    }
    _write_case_jsonl(round185_case_records(), cases)
    _write_rows(round185_score_profile_rows(), score_profiles)
    _write_rows(round185_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round185_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round185_price_field_rows(), paths["price_fields"])
    _write_rows(round185_base_score_weight_rows(), paths["base_score_weights"])
    _write_rows(round185_stage_cap_rows(), paths["stage_caps"])
    _write_rows(round185_score_stage_price_alignment_rows(), paths["score_stage_price_alignment"])
    paths["summary"].write_text(render_round185_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round185_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round185_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round185_price_validation_plan_markdown(), encoding="utf-8")
    paths["score_stage_price_alignment_md"].write_text(render_round185_score_stage_price_alignment_markdown(), encoding="utf-8")
    return paths


def render_round185_summary_markdown() -> str:
    summary = round185_summary()
    lines = [
        "# Round-185 R1 Loop-12 Industrial Orders / Infrastructure Summary",
        "",
        f"- source_round: `{ROUND185_SOURCE_ROUND_PATH}`",
        f"- large_sector: `{Round10LargeSector.INDUSTRIAL_ORDERS_INFRA.value}`",
        "- loop: `R1 Loop 12 / v12.0`",
        f"- target_count: {summary['target_count']}",
        f"- source_canonical_target_count: {summary['source_canonical_target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- base_score_axis_count: {summary['base_score_axis_count']}",
        f"- stage_cap_count: {summary['stage_cap_count']}",
        f"- score_stage_price_alignment_count: {summary['score_stage_price_alignment_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- hard_gate_target_count: {summary['hard_gate_target_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R1 Loop 12 is Korea-first and reduces repeated focus on prior flagship cases.",
        "- Example: Iljin Electric or shipbuilding equipment can become Stage 3 only when contract detail, OPM/FCF, and price-path validation align.",
        "- Example: Hanwha Aerospace KSLV/K-defense can be Stage 2 strong, but dilution and FSS correction can block Green.",
        "- Example: Doosan Bobcat cash flow can still be governance-capped if minority shareholder value risk is unresolved.",
    ]
    return "\n".join(lines) + "\n"


def render_round185_green_guardrail_markdown() -> str:
    lines = [
        "# Round-185 R1 Loop-12 Green Guardrails",
        "",
        "Stage 3-Green is not granted for sector names, policy headlines, MOU/LOI, or price-only rotations.",
        "",
        "## Stage 3 Early Catch",
        "",
        "R1 Loop 12 requires at least 5 of 8 checks:",
    ]
    stage3 = next(item for item in ROUND185_STAGE_CAPS if item.stage_band == "Stage 3")
    lines.extend(f"- `{field}`" for field in stage3.required_evidence)
    lines.extend(
        [
            "",
            "## What This Means",
            "",
            "- Power equipment: customer, amount, period, backlog quality, OPM, OP/EPS, and price-path matter.",
            "- Defense electronics: KF-21 radar visibility is Stage 2 until delivery revenue and margin appear.",
            "- Nuclear decommissioning: Kori-1 policy visibility routes research, but individual supplier contracts gate Stage 3.",
            "- Shipbuilding equipment: yard backlog must convert to equipment delivery and OPM, not merely follow shipbuilder price moves.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round185_risk_overlay_markdown() -> str:
    lines = [
        "# Round-185 R1 Loop-12 Risk Overlays",
        "",
        "| target | hard gate | red flags |",
        "| --- | --- | --- |",
    ]
    for target in ROUND185_SCORE_TARGETS:
        lines.append(f"| `{target.target_id}` | {str(target.hard_gate).lower()} | {', '.join(target.red_flags)} |")
    lines.extend(
        [
            "",
            "## Hard 4C Examples",
            "",
            "- `DEFENSE_CAPITAL_RAISE_DILUTION`: large rights offering, FSS revision request, dilution, and disclosure confidence hit.",
            "- `CONSTRUCTION_EQUIPMENT_GOVERNANCE_OVERLAY`: controversial restructuring and minority shareholder value risk.",
            "- `SPACE_SATELLITE_CAPITAL_ALLOCATION_RISK`: satellite investment loss and strategy retreat.",
            "- `DISCLOSURE_CONFIDENCE_CAP`: list-only, media-only, MOU/LOI, non-binding, or missing detail cannot create Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round185_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-185 R1 Loop-12 Price Validation Plan",
        "",
        "R1 Loop 12 must backfill order/contract fields, price-path fields, and capital/governance fields together.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND185_PRICE_FIELDS)
    lines.extend(
        [
            "",
            "## Backfill Priorities",
            "",
            "- `iljin_midcap_transformer_stage3_candidate_case`: customer, amount, period, OPM, OP/EPS, MFE/MAE, and relative strength.",
            "- `hanwha_aerospace_capital_raise_dilution_case`: dilution terms, FSS correction timing, price MAE, and use-of-proceeds confidence.",
            "- `doosan_bobcat_governance_cap_case`: governance event date, minority-shareholder impact, valuation discount, and price path.",
            "- `shipbuilding_equipment_backlog_stage3_candidate_case`: yard backlog link, delivery schedule, OPM, FCF, and own price path.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round185_score_stage_price_alignment_markdown() -> str:
    lines = [
        "# Round-185 R1 Loop-12 Score / Stage / Price Alignment",
        "",
        "| case | detected stage | price path status | verdict | adjustment |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in ROUND185_SCORE_STAGE_PRICE_ALIGNMENT:
        lines.append(f"| `{row.case_id}` | {row.detected_stage} | {row.price_path_status} | {row.verdict} | {row.normalization_adjustment} |")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Iljin and shipbuilding equipment are valid Stage 2~3 candidates only when contract economics and own price-path validate.",
            "- Hanwha Systems KF-21 radar is Stage 2 until revenue and OPM appear.",
            "- Hanwha Aerospace and Doosan Bobcat show why capital/governance can stop an otherwise strong R1 narrative.",
        ]
    )
    return "\n".join(lines) + "\n"


def _round185_score_price_alignment(candidate: Round185CaseCandidate) -> str:
    if candidate.case_type in {"success_candidate", "structural_success"}:
        return "unknown"
    if candidate.case_type in {"event_premium", "4b_watch", "cyclical_success"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    if candidate.case_type == "failed_rerating":
        return "evidence_good_but_price_failed"
    return "unknown"


def _round185_rerating_result(candidate: Round185CaseCandidate) -> str:
    if candidate.case_type in {"success_candidate", "structural_success"}:
        return "unknown"
    if candidate.case_type == "event_premium":
        return "event_premium"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "4b_watch":
        return "theme_overheat"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "failed_rerating":
        return "no_rerating"
    return "unknown"


def _numeric_weight(value: int | str) -> float:
    return float(value) if isinstance(value, int) else 0.0


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
    "ROUND185_BASE_SCORE_WEIGHTS",
    "ROUND185_CASE_CANDIDATES",
    "ROUND185_DEFAULT_CASES_PATH",
    "ROUND185_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND185_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND185_PRICE_FIELDS",
    "ROUND185_SCORE_STAGE_PRICE_ALIGNMENT",
    "ROUND185_SCORE_TARGETS",
    "ROUND185_SOURCE_CANONICAL_TARGET_COUNT",
    "ROUND185_SOURCE_CANONICAL_TARGET_IDS",
    "ROUND185_STAGE_CAPS",
    "render_round185_green_guardrail_markdown",
    "render_round185_price_validation_plan_markdown",
    "render_round185_risk_overlay_markdown",
    "render_round185_score_stage_price_alignment_markdown",
    "render_round185_summary_markdown",
    "round185_base_score_weight_rows",
    "round185_case_candidate_rows",
    "round185_case_records",
    "round185_price_field_rows",
    "round185_score_profile_rows",
    "round185_score_stage_price_alignment_rows",
    "round185_stage_cap_rows",
    "round185_stage_date_rows",
    "round185_summary",
    "round185_target_for",
    "write_round185_r1_loop12_reports",
]
