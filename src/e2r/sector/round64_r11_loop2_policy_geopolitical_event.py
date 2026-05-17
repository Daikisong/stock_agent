"""Round-64 R11 Loop-2 policy/geopolitical/disaster/event pack.

Round 64 tightens the R11 event-risk pack from Round 51. The rule stays simple:
large headlines are only routing evidence. They must turn into contracts,
budgets, government orders, financing, construction starts, recurring revenue,
or EPS/FCF conversion before they can support higher-stage conviction.

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


ROUND64_SOURCE_ROUND_PATH = "docs/round/round_64.md"
ROUND64_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round64_r11_loop2_policy_geopolitical_event"
ROUND64_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r11_loop2_round64.jsonl"
ROUND64_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round64_r11_loop2_v2.csv"


@dataclass(frozen=True)
class Round64ScoreWeightDraft:
    eps_fcf: int | str
    structural_visibility: int | str
    bottleneck_pricing: int | str
    market_mispricing: int | str
    valuation: int | str
    capital_allocation: int | str
    information_confidence: int | str

    def as_csv_dict(self) -> dict[str, str]:
        return {
            "eps_fcf": str(self.eps_fcf),
            "structural_visibility": str(self.structural_visibility),
            "bottleneck_pricing": str(self.bottleneck_pricing),
            "market_mispricing": str(self.market_mispricing),
            "valuation": str(self.valuation),
            "capital_allocation": str(self.capital_allocation),
            "information_confidence": str(self.information_confidence),
        }

    def as_numeric_dict(self) -> dict[str, float]:
        return {
            key: float(value) if str(value).isdigit() else 0.0
            for key, value in self.as_csv_dict().items()
        }


@dataclass(frozen=True)
class Round64ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round64ScoreWeightDraft
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
        return Round10LargeSector.POLICY_GEOPOLITICAL_EVENT

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round64CaseCandidate:
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


ROUND64_SCORE_TARGETS: tuple[Round64ScoreTarget, ...] = (
    Round64ScoreTarget(
        "NORTH_KOREA_POLICY_EVENT",
        E2RArchetype.NORTH_KOREA_POLICY_EVENT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round64ScoreWeightDraft(5, 4, 5, 8, 5, 0, 3),
        ("summit_or_dialogue", "tourism_reopening_headline", "sanctions_discussion", "inter_korea_infra_theme"),
        ("government_approval", "business_restart", "sanctions_relief", "cash_flow_project"),
        ("very_rare_cash_flow_project", "multi_year_contract", "low_sanctions_risk"),
        ("summit_expectation_rally", "policy_theme_basket_crowding", "tourism_reopen_price_spike"),
        ("military_tension", "facility_dismantle", "road_rail_destroyed", "sanctions_intact", "hostile_state_rhetoric"),
        ("sanctions_relief", "funded_project", "cash_flow_project", "revenue_visibility"),
        ("sanctions", "military_tension", "facility_dismantle", "road_rail_destroyed", "policy_reversal"),
        "North Korea policy themes remain hard Red-biased until sanctions relief and cash-flow evidence exist.",
    ),
    Round64ScoreTarget(
        "GEOPOLITICAL_RECONSTRUCTION",
        E2RArchetype.GEOPOLITICAL_RECONSTRUCTION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round64ScoreWeightDraft(12, 11, 8, 10, 8, 0, 4),
        ("reconstruction_conference", "mou_or_policy_declaration", "post_war_infra_theme"),
        ("actual_project", "project_financing", "participating_company", "company_contract", "construction_started"),
        ("multi_year_revenue", "supplier_margin", "funded_backlog", "delivery_schedule"),
        ("reconstruction_basket_rally_before_contract", "headline_project_priced", "financing_expectation_crowding"),
        ("war_escalation", "financing_failure", "insurance_delay", "project_start_delay"),
        ("actual_project", "project_financing", "company_contract", "margin_visibility"),
        ("mou_only", "financing_missing", "geopolitical_setback", "project_delay"),
        "Reconstruction is a Watch path only after funded projects and company-level exposure appear.",
    ),
    Round64ScoreTarget(
        "DISASTER_REBUILD_EVENT",
        E2RArchetype.DISASTER_REBUILD_EVENT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round64ScoreWeightDraft(10, 6, 7, 8, 6, 0, 4),
        ("earthquake_rebuild", "wildfire_rebuild", "flood_or_typhoon_rebuild", "rebuild_material_theme"),
        ("rebuild_order", "insurance_or_budget_approved", "sell_through", "margin_visibility"),
        ("repeat_rebuild_demand", "fcf_after_event", "multi_period_orders"),
        ("disaster_theme_rally", "material_basket_crowding", "insurance_expectation_rally"),
        ("one_off_rebuild_fade", "insurance_delay", "budget_delay", "inventory_build"),
        ("rebuild_order", "budget_approved", "margin_visibility", "repeat_demand"),
        ("one_off_demand", "budget_delay", "insurance_delay", "inventory"),
        "Disaster rebuilding needs orders, budget, insurance, and margin checks before scoring credit.",
    ),
    Round64ScoreTarget(
        "CLIMATE_DISASTER_EVENT",
        E2RArchetype.CLIMATE_DISASTER_EVENT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round64ScoreWeightDraft(12, 13, 11, 10, 8, 0, 5),
        ("heatwave", "cooling_demand", "grid_stress", "air_quality_event", "wildfire_or_flood_event"),
        ("grid_investment", "cooling_order", "demand_response_program", "vpp_program", "repeat_weather_demand"),
        ("structural_grid_capex", "recurring_cooling_demand", "energy_system_investment", "op_eps_conversion"),
        ("seasonal_weather_theme_rally", "cooling_theme_crowded", "grid_theme_price_spike"),
        ("weather_normalization", "inventory_build", "demand_fade", "margin_reversal", "policy_budget_delay"),
        ("repeat_demand", "grid_capex", "sales_or_order", "margin_visibility", "vpp_or_ess_revenue"),
        ("seasonality", "weather_fade", "inventory", "no_sales_conversion"),
        "Climate events become stronger only when they cross into grid, cooling, VPP, ESS, or rebuild capex.",
    ),
    Round64ScoreTarget(
        "EVENT_DISEASE_PEST_DEMAND",
        E2RArchetype.EVENT_DISEASE_PEST_DEMAND,
        Round10ThemePosture.REDTEAM_FIRST,
        Round64ScoreWeightDraft(13, 9, 8, 8, 6, 0, 5),
        ("outbreak_alert", "who_emergency", "pest_demand_spike", "stockpile_headline"),
        ("government_order", "stockpile_contract", "guide_up", "dose_or_amount_disclosed"),
        ("recurring_procurement", "non_event_demand", "ebitda_margin_visible"),
        ("outbreak_news_rally", "vaccine_or_pest_basket_crowding", "demand_extrapolated"),
        ("outbreak_normalization", "government_purchase_end", "inventory_build", "demand_cliff"),
        ("government_order", "stockpile_contract", "guide_up", "recurring_procurement"),
        ("one_off_outbreak", "demand_normalization", "purchase_end", "inventory"),
        "Disease/pest events are RedTeam-first unless orders, stockpile contracts, and guidance are source-backed.",
    ),
    Round64ScoreTarget(
        "DIAGNOSTICS_INFECTIOUS_EVENT",
        E2RArchetype.DIAGNOSTICS_INFECTIOUS_EVENT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round64ScoreWeightDraft(20, 5, 5, 5, 5, 0, 5),
        ("diagnostic_test_demand", "pandemic_or_outbreak_testing", "test_kit_order"),
        ("diagnostic_revenue_after_event", "recurring_non_event_demand", "margin_normalization"),
        ("durable_testing_market", "non_event_revenue_base", "fcf_conversion"),
        ("test_kit_rally_after_case_counts", "diagnostic_margin_extrapolated"),
        ("testing_demand_wane", "diagnostic_sales_decline", "guide_down", "inventory_writeoff"),
        ("non_event_revenue", "recurring_testing_demand", "margin_normalization", "fcf_conversion"),
        ("covid_like_one_off", "sales_decline", "guide_down", "inventory"),
        "Diagnostic EPS spikes must be tested against post-event revenue normalization.",
    ),
    Round64ScoreTarget(
        "SPECULATIVE_SCIENCE_THEME",
        E2RArchetype.SPECULATIVE_SCIENCE_THEME,
        Round10ThemePosture.REDTEAM_FIRST,
        Round64ScoreWeightDraft(5, 4, 5, 5, 5, 0, 3),
        ("preprint", "lab_claim", "sns_video", "paper_keyword"),
        ("independent_replication", "peer_review_validation", "customer_testing", "commercial_product", "contract_or_revenue"),
        ("commercial_revenue", "repeat_customer", "eps_fcf_conversion"),
        ("preprint_sns_rally", "retail_theme_crowding", "paper_to_price_gap"),
        ("replication_failure", "impurity_explanation", "peer_review_failure", "trading_warning"),
        ("replication_success", "commercial_product", "customer_contract", "revenue"),
        ("replication_failure", "no_commercial_product", "preprint_only", "sns_only"),
        "Science-themes need independent validation, customers, products, and revenue before they become scoring evidence.",
    ),
    Round64ScoreTarget(
        "ADVANCED_MATERIAL_SPECULATIVE_THEME",
        E2RArchetype.ADVANCED_MATERIAL_SPECULATIVE_THEME,
        Round10ThemePosture.REDTEAM_FIRST,
        Round64ScoreWeightDraft(7, 6, 6, 8, 6, 0, 3),
        ("mxene_or_graphene_claim", "quantum_material_news", "advanced_material_theme"),
        ("technical_validation", "pilot_customer", "supply_contract", "revenue_conversion"),
        ("repeat_order", "commercial_scale", "margin_visibility"),
        ("advanced_material_theme_crowding", "paper_to_price_gap"),
        ("validation_failure", "no_customer", "no_revenue", "dilution_or_funding_need"),
        ("technical_validation", "pilot_customer", "revenue_conversion", "margin_visibility"),
        ("paper_only", "no_customer", "no_revenue", "funding_need"),
        "Advanced materials are Watch/Red until commercial validation exists.",
    ),
    Round64ScoreTarget(
        "POLICY_LOCAL_THEME",
        E2RArchetype.POLICY_LOCAL_THEME,
        Round10ThemePosture.REDTEAM_FIRST,
        Round64ScoreWeightDraft(5, 5, 5, 8, 5, 0, 3),
        ("local_policy_headline", "administrative_capital_theme", "regional_development_policy"),
        ("budget_approved", "contract_awarded", "construction_started", "revenue_visibility"),
        ("repeat_project_revenue", "margin_visibility", "fcf_conversion"),
        ("local_policy_theme_rally", "election_policy_crowding"),
        ("policy_reversal", "budget_cut", "project_delay", "no_company_exposure"),
        ("budget_approved", "contract_awarded", "revenue_visibility", "margin_visibility"),
        ("budget_missing", "policy_reversal", "project_delay", "no_exposure"),
        "Local policy labels are routing data only until budget, contract, construction, or revenue exists.",
    ),
    Round64ScoreTarget(
        "ONE_OFF_EVENT_DEMAND",
        E2RArchetype.ONE_OFF_EVENT_DEMAND,
        Round10ThemePosture.REDTEAM_FIRST,
        Round64ScoreWeightDraft(8, 5, 5, 6, 5, 0, 4),
        ("temporary_shortage", "event_demand_spike", "emergency_purchase"),
        ("short_term_order", "reported_revenue_spike", "margin_visible"),
        ("recurrence_proven", "post_event_revenue_base", "fcf_conversion"),
        ("event_demand_extrapolated", "peak_margin_crowding"),
        ("demand_normalization", "one_off_purchase_end", "asp_or_margin_drop"),
        ("recurrence_proven", "post_event_revenue_base", "fcf_conversion"),
        ("one_off_risk", "normalization", "purchase_end", "margin_reversal"),
        "One-off event demand should normally remain Yellow/Red unless recurrence is proven.",
    ),
    Round64ScoreTarget(
        "EVENT_TO_CONTRACT_ESCALATION",
        E2RArchetype.EVENT_PREMIUM,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round64ScoreWeightDraft(14, 13, 8, 10, 8, 0, 5),
        ("event_headline", "disease_or_policy_or_rebuild_trigger", "theme_price_move"),
        ("actual_contract", "government_order", "project_financing", "budget_allocated", "construction_started"),
        ("recurring_revenue", "margin_visibility", "eps_fcf_conversion", "repeat_procurement"),
        ("event_to_contract_rally", "single_contract_extrapolated"),
        ("contract_ends", "no_follow_on_order", "budget_delay", "demand_normalization"),
        ("actual_contract", "budget_or_financing", "revenue_recognized", "margin_visibility"),
        ("headline_only", "contract_missing", "budget_missing", "revenue_missing"),
        "Auxiliary diagnostic target for events that actually become contracts, budgets, orders, or financing.",
    ),
    Round64ScoreTarget(
        "THEME_VALUATION_OVERHEAT",
        E2RArchetype.THEME_VALUATION_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round64ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("price_only_rally", "theme_keyword_spike", "retail_crowding"),
        ("real_estimate_or_contract_needed",),
        ("normally_blocked_without_eps_fcf",),
        ("valuation_saturation", "price_blowoff", "crowded_reports"),
        ("estimate_cut", "accounting_or_trust_issue", "dilution", "theme_unwind"),
        ("cross_evidence", "eps_fcf_path", "redteam_low"),
        ("price_only", "crowding", "no_cash_flow", "dilution"),
        "This is a RedTeam overlay. It gates unsafe Green rather than adding positive score.",
        gate_only=True,
    ),
)


ROUND64_CASE_CANDIDATES: tuple[Round64CaseCandidate, ...] = (
    Round64CaseCandidate(
        "bavarian_nordic_us_stockpile_contract_case",
        "EVENT_TO_CONTRACT_ESCALATION",
        "BAVA.CO",
        "Bavarian Nordic U.S. stockpile contract",
        "EU",
        "success_candidate",
        date(2026, 5, 11),
        date(2026, 5, 11),
        None,
        None,
        None,
        ("government_order", "stockpile_contract", "contract_value", "guide_up", "ebitda_margin_guidance_raise"),
        ("one_off_outbreak", "government_purchase_end", "demand_normalization"),
        "event_to_contract_stockpile_candidate",
        "needs_price_backfill",
        ("Reuters Bavarian Nordic stockpile contract",),
        "A stockpile option and guidance raise can support Stage 2; recurrence and non-event revenue still decide higher stages.",
        (E2RArchetype.EVENT_DISEASE_PEST_DEMAND,),
    ),
    Round64CaseCandidate(
        "bavarian_nordic_2024_mpox_order_case",
        "EVENT_DISEASE_PEST_DEMAND",
        "BAVA.CO",
        "Bavarian Nordic 2024 mpox vaccine order",
        "EU",
        "event_premium",
        date(2024, 8, 15),
        None,
        None,
        date(2024, 8, 16),
        None,
        ("who_emergency", "vaccine_order_doses", "outbreak_alert", "vaccine_theme_rally"),
        ("one_off_outbreak", "purchase_unverified", "demand_normalization"),
        "event_premium_with_contract_validation_needed",
        "needs_price_backfill",
        ("Investopedia Bavarian Nordic mpox order",),
        "A vaccine order can validate part of the event, but the case remains event premium until recurring demand is clear.",
    ),
    Round64CaseCandidate(
        "ukraine_telecom_ebrd_ifc_case",
        "GEOPOLITICAL_RECONSTRUCTION",
        "UKRAINE_TELECOM_RECOVERY",
        "Ukraine telecom EBRD IFC financing",
        "GLOBAL",
        "success_candidate",
        date(2024, 10, 10),
        date(2024, 10, 10),
        None,
        None,
        None,
        ("project_financing", "financing_amount", "telecom_infrastructure", "participating_company"),
        ("war_escalation", "financing_delay", "insurance_delay"),
        "funded_geopolitical_infra_candidate",
        "needs_price_backfill",
        ("Reuters Ukraine telecom EBRD IFC financing",),
        "Financing is better than a reconstruction slogan; company-level revenue and margin evidence still need validation.",
    ),
    Round64CaseCandidate(
        "heatwave_ac_grid_stress_case",
        "CLIMATE_DISASTER_EVENT",
        "HEATWAVE_GRID_BASKET",
        "Heatwave air-conditioning grid stress",
        "GLOBAL",
        "success_candidate",
        date(2025, 7, 18),
        date(2025, 7, 18),
        None,
        None,
        None,
        ("heatwave_event", "cooling_demand", "grid_stress", "peak_load_increase_estimate"),
        ("seasonality", "weather_normalization", "no_sales_conversion"),
        "climate_event_to_grid_infra_watch",
        "needs_price_backfill",
        ("German heatwave AC demand study",),
        "Heatwaves can route research to grid, cooling, ESS, HVAC, and transformers, but the weather event alone is not Green.",
    ),
    Round64CaseCandidate(
        "nyc_ac_battery_vpp_case",
        "CLIMATE_DISASTER_EVENT",
        "NYC_VPP_BATTERY_PROGRAM",
        "NYC AC battery VPP demand-response program",
        "US",
        "success_candidate",
        date(2026, 5, 1),
        date(2026, 5, 1),
        None,
        None,
        None,
        ("vpp_program", "battery_program_capacity", "demand_response_program", "grid_stress"),
        ("policy_budget_delay", "seasonal_demand_normalization", "no_follow_on_contract"),
        "event_to_infra_crossover_candidate",
        "needs_price_backfill",
        ("AP air-conditioning battery VPP program",),
        "A VPP/battery program is stronger than a heatwave headline because it points to energy-system investment.",
    ),
    Round64CaseCandidate(
        "north_korea_kumgang_dismantle_case",
        "NORTH_KOREA_POLICY_EVENT",
        "INTER_KOREA_POLICY_BASKET",
        "North Korea Kumgang facility dismantle",
        "KR",
        "4c_thesis_break",
        date(2025, 2, 13),
        None,
        None,
        None,
        date(2025, 2, 13),
        ("facility_dismantle", "hostile_state_rhetoric", "road_rail_destroyed"),
        ("facility_dismantle", "military_tension", "sanctions_intact", "policy_reversal"),
        "north_korea_hard_red",
        "needs_price_backfill",
        ("Reuters Kumgang facility dismantle",),
        "Facility dismantling and military deterioration are hard RedTeam evidence for inter-Korea policy themes.",
    ),
    Round64CaseCandidate(
        "lk99_superconductor_no_replication_case",
        "SPECULATIVE_SCIENCE_THEME",
        "LK99_THEME_BASKET",
        "LK-99 no replication case",
        "GLOBAL",
        "4c_thesis_break",
        date(2023, 8, 8),
        None,
        None,
        None,
        date(2023, 8, 8),
        ("replication_failure", "peer_review_failure", "no_commercial_product"),
        ("replication_failure", "no_commercial_product", "technical_validation_failure"),
        "speculative_science_failure",
        "needs_price_backfill",
        ("arXiv LK-99 absence of superconductivity",),
        "Replication failure is the clean 4C example for speculative-science themes.",
        (E2RArchetype.THEME_VALUATION_OVERHEAT,),
    ),
    Round64CaseCandidate(
        "lk99_cu2s_impurity_case",
        "SPECULATIVE_SCIENCE_THEME",
        "LK99_THEME_BASKET",
        "LK-99 Cu2S impurity explanation",
        "GLOBAL",
        "4c_thesis_break",
        date(2023, 11, 1),
        None,
        None,
        None,
        date(2023, 11, 1),
        ("impurity_explanation", "replication_failure", "peer_review_failure"),
        ("impurity_explanation", "no_commercial_product", "no_customer_contract"),
        "speculative_science_failure",
        "needs_price_backfill",
        ("arXiv LK-99 Cu2S impurity explanation",),
        "An impurity explanation is thesis-break evidence when a material theme lacks customers, products, and revenue.",
        (E2RArchetype.THEME_VALUATION_OVERHEAT,),
    ),
    Round64CaseCandidate(
        "abbott_diagnostics_demand_wane_case",
        "DIAGNOSTICS_INFECTIOUS_EVENT",
        "ABT",
        "Abbott diagnostics demand wanes",
        "US",
        "4c_thesis_break",
        date(2025, 10, 15),
        None,
        None,
        None,
        date(2025, 10, 15),
        ("diagnostic_sales_decline", "testing_demand_wane", "post_event_revenue_drop"),
        ("testing_demand_wane", "diagnostic_sales_decline", "guide_down"),
        "one_off_diagnostic_demand_normalized",
        "needs_price_backfill",
        ("Reuters Abbott diagnostics demand",),
        "Diagnostics revenue decline after event demand proves why COVID-style EPS spikes should not be structural Green.",
    ),
    Round64CaseCandidate(
        "climate_event_seasonal_watch_case",
        "CLIMATE_DISASTER_EVENT",
        "CLIMATE_EVENT_BASKET",
        "Climate seasonal event watch",
        "GLOBAL",
        "event_premium",
        date(2025, 7, 18),
        None,
        None,
        date(2025, 7, 18),
        None,
        ("heatwave_event", "air_quality_event", "seasonal_theme_rally"),
        ("seasonality", "weather_normalization", "no_sales_conversion"),
        "seasonal_climate_event_watch",
        "needs_price_backfill",
        ("Round64 analyst matrix",),
        "Heat, dust, flood, or wildfire events stay seasonal unless they produce contracts, orders, or infrastructure capex.",
    ),
    Round64CaseCandidate(
        "policy_local_theme_case",
        "POLICY_LOCAL_THEME",
        "LOCAL_POLICY_BASKET",
        "Local policy theme basket",
        "KR",
        "event_premium",
        None,
        None,
        None,
        None,
        None,
        ("local_policy_headline", "regional_development_theme"),
        ("budget_missing", "no_company_exposure", "policy_reversal"),
        "policy_relief_only",
        "needs_price_backfill",
        ("Round64 analyst matrix",),
        "A local-policy label is search routing only until budget, contract, construction, or revenue is visible.",
    ),
    Round64CaseCandidate(
        "disaster_rebuild_material_case",
        "DISASTER_REBUILD_EVENT",
        "DISASTER_REBUILD_MATERIAL",
        "Disaster rebuild material basket",
        "GLOBAL",
        "event_premium",
        None,
        None,
        None,
        None,
        None,
        ("disaster_event", "rebuild_material_theme", "rebuild_project_count"),
        ("one_off_rebuild_fade", "budget_delay", "insurance_delay"),
        "event_premium_rebuild_without_contract",
        "needs_price_backfill",
        ("Round64 analyst matrix",),
        "Rebuild headlines need actual orders, budget, insurance payout, and margin before becoming scoring evidence.",
    ),
)


ROUND64_PRICE_FIELDS: tuple[str, ...] = (
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
    "MFE_5D",
    "MFE_20D",
    "MFE_60D",
    "MFE_90D",
    "MFE_180D",
    "MAE_5D",
    "MAE_20D",
    "MAE_60D",
    "MAE_90D",
    "MAE_180D",
    "drawdown_after_peak",
    "below_stage1_price_flag",
    "below_stage2_price_flag",
    "below_stage3_price_flag",
    "event_type",
    "policy_event_flag",
    "geopolitical_event_flag",
    "disaster_event_flag",
    "climate_event_flag",
    "disease_event_flag",
    "science_preprint_flag",
    "social_media_theme_flag",
    "actual_contract_flag",
    "contract_value",
    "contract_duration_months",
    "government_order_flag",
    "stockpile_contract_flag",
    "vaccine_order_doses",
    "project_financing_flag",
    "financing_amount",
    "budget_allocated_flag",
    "construction_started_flag",
    "revenue_recognized_flag",
    "outbreak_status",
    "who_emergency_flag",
    "government_purchase_amount",
    "diagnostic_sales_change",
    "demand_normalization_flag",
    "inventory_build_flag",
    "replication_success_flag",
    "replication_failure_flag",
    "peer_review_status",
    "commercial_product_flag",
    "customer_contract_flag",
    "impurity_explanation_flag",
    "sanctions_status",
    "military_tension_flag",
    "tourism_reopen_flag",
    "facility_dismantle_flag",
    "road_rail_destroyed_flag",
    "hostile_state_rhetoric_flag",
    "rebuild_project_count",
    "rebuild_budget_amount",
    "insurance_payout_status",
    "one_off_demand_flag",
    "heatwave_event_flag",
    "peak_load_increase_estimate",
    "grid_stress_flag",
    "vpp_program_flag",
    "battery_program_capacity",
    "cooling_order_flag",
    "energy_system_investment_flag",
    "policy_budget_flag",
    "local_policy_flag",
    "regional_development_contract_flag",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def target_for(target_id: str) -> Round64ScoreTarget | None:
    for target in ROUND64_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round64_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND64_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
        weights = target.score_weight.as_numeric_dict()
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
                f"Round64 R11 Loop-2 case for {candidate.target_id}; "
                "event evidence is calibration-only and missing prices remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage2_signals or field in target.green_conditions),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage3_conditions),
            stage4b_evidence=stage4b_evidence,
            stage4c_evidence=stage4c_evidence,
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "overheat", "4b_watch", "4c_thesis_break", "one_off"} else None,
            score_price_alignment=_score_price_alignment(candidate),
            rerating_result=_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint={
                "eps_fcf": weights["eps_fcf"],
                "visibility": weights["structural_visibility"],
                "bottleneck": weights["bottleneck_pricing"],
                "mispricing": weights["market_mispricing"],
                "valuation": weights["valuation"],
                "capital_allocation": weights["capital_allocation"],
            },
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_cross_evidence_for_green",
                "event_news_is_not_green_evidence_alone",
                "contract_budget_order_financing_revenue_or_eps_required",
                "do_not_invent_contracts_budgets_orders_financing_stage_prices_or_guidance",
                "date_verified_evidence_required",
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


def round64_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND64_SCORE_TARGETS:
        weights = target.score_weight.as_csv_dict()
        rows.append(
            {
                "target_id": target.target_id,
                "large_sector": target.large_sector.value,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "eps_fcf": weights["eps_fcf"],
                "structural_visibility": weights["structural_visibility"],
                "bottleneck_pricing": weights["bottleneck_pricing"],
                "market_mispricing": weights["market_mispricing"],
                "valuation": weights["valuation"],
                "capital_allocation": weights["capital_allocation"],
                "information_confidence": weights["information_confidence"],
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


def round64_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND64_CASE_CANDIDATES:
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


def round64_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "production_scoring_changed": "false",
        }
        for target in ROUND64_SCORE_TARGETS
    )


def round64_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round64_backfill": "true"} for field in ROUND64_PRICE_FIELDS)


def round64_summary() -> dict[str, int | bool]:
    records = round64_case_records()
    return {
        "target_count": len(ROUND64_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "one_off_count": sum(1 for record in records if record.case_type == "one_off"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND64_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND64_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND64_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND64_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round64_r11_loop2_reports(
    *,
    output_directory: str | Path = ROUND64_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND64_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND64_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round64_r11_loop2_policy_geopolitical_event_summary.md",
        "case_matrix": output / "round64_r11_loop2_case_matrix.csv",
        "stage_date_plan": output / "round64_r11_loop2_stage_date_plan.csv",
        "green_guardrails": output / "round64_r11_loop2_green_guardrails.md",
        "event_false_positive_caps": output / "round64_r11_loop2_event_false_positive_caps.md",
        "price_validation_plan": output / "round64_r11_loop2_price_validation_plan.md",
        "price_fields": output / "round64_r11_loop2_price_fields.csv",
    }
    _write_case_jsonl(round64_case_records(), cases)
    _write_rows(round64_score_profile_rows(), score_profiles)
    _write_rows(round64_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round64_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round64_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round64_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round64_green_guardrail_markdown(), encoding="utf-8")
    paths["event_false_positive_caps"].write_text(render_round64_event_false_positive_caps_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round64_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round64_summary_markdown() -> str:
    summary = round64_summary()
    lines = [
        "# Round-64 R11 Loop-2 Policy / Geopolitical / Disaster / Event Summary",
        "",
        f"- source_round: `{ROUND64_SOURCE_ROUND_PATH}`",
        "- large_sector: `POLICY_GEOPOLITICAL_EVENT`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        f"- gate_only_target_count: {summary['gate_only_target_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R11 Loop-2 is mostly a false-positive defense pack.",
        "- Example: a big outbreak headline can create Stage 1 routing. Without `government_order`, `stockpile_contract`, or `guide_up`, it stays event premium.",
        "- Example: Ukraine reconstruction becomes stronger only when financing, participating companies, construction start, and revenue/margin evidence are visible.",
        "- Example: LK-99 style preprints are not revenue evidence; replication failure or impurity explanation is a hard 4C-style counterexample.",
    ]
    return "\n".join(lines) + "\n"


def render_round64_green_guardrail_markdown() -> str:
    lines = [
        "# Round-64 R11 Loop-2 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND64_SCORE_TARGETS:
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
            "- Do not apply these R11 Loop-2 v2 weights to production scoring yet.",
            "- Do not treat policy headlines, war/reconstruction slogans, disasters, outbreaks, local policy, or preprints as Green evidence by itself.",
            "- Do not invent contracts, government orders, budgets, dose amounts, project financing, construction starts, revenue, guidance, or price-path fields.",
            "- Do not lower Stage 3-Green for event recall. Green requires source-backed contract, budget, revenue, recurring demand, or EPS/FCF conversion.",
            "- Treat replication failure, facility dismantling, military escalation, demand normalization, purchase end, budget delay, and no-customer science themes as RedTeam evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round64_event_false_positive_caps_markdown() -> str:
    lines = [
        "# Round-64 R11 Loop-2 Event False-Positive Caps",
        "",
        "- `EVENT_PREMIUM`: news moved price, but actual revenue, contract, or budget is missing.",
        "- `EVENT_TO_CONTRACT`: event moved into government contract, stockpile, financing, construction, or recognized revenue.",
        "- `EVENT_TO_INFRA_CROSSOVER`: disaster/climate event crossed into grid, cooling, VPP, ESS, or rebuild capex.",
        "- `PRICE_MOVED_WITHOUT_EVIDENCE`: policy, SNS, or paper moved price without cash-flow evidence.",
        "- `SPECULATIVE_SCIENCE_FAILURE`: replication failure or no product/customer breaks the thesis.",
        "- `ONE_OFF_REVENUE`: revenue happened, but demand normalized after the event.",
        "- `POLICY_RELIEF_ONLY`: policy existed, but budget, contract, construction, or revenue did not.",
        "- `NORTH_KOREA_HARD_RED`: sanctions, military tension, facility dismantling, road/rail destruction, or hostile rhetoric block unsafe escalation.",
        "",
        "Simple example: a heatwave can route research to grid or HVAC names. If `cooling_order_flag`, `vpp_program_flag`, and `revenue_recognized_flag` are empty, the case stays Watch/Event, not Stage 3-Green.",
    ]
    return "\n".join(lines) + "\n"


def render_round64_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-64 R11 Loop-2 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store Stage 1 and Stage 2 event-date close prices from official price data.",
        "3. Calculate MFE_5D / 20D / 60D / 90D / 180D and matching MAE windows.",
        "4. Calculate peak_price and drawdown_after_peak.",
        "5. Compare price moves with actual contracts, budgets, government orders, financing, construction starts, revenue, and EPS evidence.",
        "6. If evidence is missing, classify as `price_moved_without_evidence`, `event_premium`, or `policy_relief_only`.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | stage candidate | check |",
        "| --- | --- | --- |",
    ]
    for row in round64_case_candidate_rows():
        if row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"]:
            stage_date = row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or row["stage1_date"]
            lines.append(f"| `{row['case_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `event_to_contract_stockpile_candidate`: event demand is backed by a government stockpile contract, but still needs recurrence and margin checks.",
            "- `funded_geopolitical_infra_candidate`: financing exists; company-level contract and margin proof still decide scoring.",
            "- `event_to_infra_crossover_candidate`: climate/disaster demand crossed into grid, VPP, ESS, cooling, or rebuild infrastructure.",
            "- `price_moved_without_evidence`: science, policy, or disaster theme moved price before technical/customer/revenue evidence.",
            "- `speculative_science_failure`: replication failure or impurity explanation breaks the thesis.",
            "- `one_off_diagnostic_demand_normalized`: diagnostics revenue fell after temporary event demand normalized.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round64CaseCandidate) -> str:
    if candidate.case_type == "success_candidate" and (
        "contract" in candidate.alignment_hint
        or "funded" in candidate.alignment_hint
        or "infra" in candidate.alignment_hint
    ):
        return "aligned"
    if candidate.case_type in {"event_premium", "one_off", "4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type in {"failed_rerating", "4c_thesis_break"}:
        return "false_positive_score"
    return "unknown"


def _rerating_result(candidate: Round64CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "success_candidate":
        if "geopolitical" in candidate.alignment_hint or "infra" in candidate.alignment_hint:
            return "policy_event_rerating"
        if "contract" in candidate.alignment_hint or "stockpile" in candidate.alignment_hint:
            return "event_premium"
        return "unknown"
    if candidate.case_type in {"event_premium", "one_off"}:
        return "event_premium"
    if candidate.case_type in {"4b_watch", "overheat"}:
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
    "ROUND64_CASE_CANDIDATES",
    "ROUND64_DEFAULT_CASES_PATH",
    "ROUND64_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND64_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND64_PRICE_FIELDS",
    "ROUND64_SCORE_TARGETS",
    "ROUND64_SOURCE_ROUND_PATH",
    "Round64CaseCandidate",
    "Round64ScoreTarget",
    "Round64ScoreWeightDraft",
    "render_round64_event_false_positive_caps_markdown",
    "render_round64_green_guardrail_markdown",
    "render_round64_price_validation_plan_markdown",
    "render_round64_summary_markdown",
    "round64_case_candidate_rows",
    "round64_case_records",
    "round64_price_field_rows",
    "round64_score_profile_rows",
    "round64_stage_date_rows",
    "round64_summary",
    "target_for",
    "write_round64_r11_loop2_reports",
]
