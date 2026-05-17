"""Round-65 R12 Loop-2 agriculture, life services, and miscellaneous pack.

Round 65 tightens the R12 unit-economics pack from Round 52. Agriculture,
education, rental, kiosk, and regulated-consumer stories can look defensive or
essential, but they do not support Stage 3-Green until repeat contracts,
repeat revenue, unit economics, pass-through, churn, CAC, regulatory scope, and
FCF conversion are source-backed.

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


ROUND65_SOURCE_ROUND_PATH = "docs/round/round_65.md"
ROUND65_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round65_r12_loop2_agri_life_misc"
ROUND65_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r12_loop2_round65.jsonl"
ROUND65_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round65_r12_loop2_v2.csv"


@dataclass(frozen=True)
class Round65ScoreWeightDraft:
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
class Round65ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round65ScoreWeightDraft
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
        return Round10LargeSector.EDUCATION_LIFE_AGRI_MISC

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round65CaseCandidate:
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


ROUND65_SCORE_TARGETS: tuple[Round65ScoreTarget, ...] = (
    Round65ScoreTarget(
        "SMART_FARM_AGRI_TECH",
        E2RArchetype.SMART_FARM_AGRI_TECH,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round65ScoreWeightDraft(17, 13, 12, 9, 8, 0, 5),
        ("smart_farm_policy", "autonomous_agri_equipment", "vertical_farming", "agri_ai"),
        ("actual_order", "operation_contract", "maintenance_saas_revenue", "capacity_utilization"),
        ("unit_economics_positive", "fcf_conversion", "repeat_contracts", "energy_cost_control"),
        ("smart_farm_theme_crowded", "vertical_farming_story_priced_before_unit_economics"),
        ("chapter11", "shutdown", "energy_cost_failure", "premium_pricing_failure", "capex_burden"),
        ("actual_order", "operation_contract", "unit_economics_positive", "fcf_conversion"),
        ("energy_cost", "capex_burden", "unit_economics_failure", "subsidy_dependency"),
        "Smart-farm labels need orders, utilization, energy-cost proof, and FCF before Green.",
    ),
    Round65ScoreTarget(
        "AGRI_MACHINERY_PRECISION_CYCLE",
        E2RArchetype.AGRI_MACHINERY_PRECISION_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round65ScoreWeightDraft(17, 13, 10, 10, 9, 1, 5),
        ("autonomous_tractor", "precision_agriculture", "agri_drone", "ces_technology_demo"),
        ("equipment_sales_growth", "farmer_roi", "software_attach_rate", "service_revenue"),
        ("recurring_software_or_service", "farm_income_support", "low_financing_stress"),
        ("autonomous_agri_theme_crowded", "technology_priced_before_adoption"),
        ("farm_income_weakness", "high_borrowing_cost", "equipment_sales_decline", "right_to_repair_lawsuit"),
        ("equipment_sales_growth", "farmer_roi", "software_attach_rate", "service_revenue"),
        ("farm_income", "financing_cost", "replacement_cycle", "right_to_repair", "dealer_inventory"),
        "Autonomous farm equipment still needs farm-income, financing, adoption, and software attachment checks.",
    ),
    Round65ScoreTarget(
        "AGRI_LIVESTOCK_FOOD_COMMODITY",
        E2RArchetype.AGRI_LIVESTOCK_FOOD_COMMODITY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round65ScoreWeightDraft(18, 9, 14, 8, 7, 0, 5),
        ("avian_flu", "asf", "egg_price_spike", "feed_cost_change", "soybean_or_tuna_price"),
        ("price_pass_through", "op_profit_increase", "cost_stabilization"),
        ("structural_green_restricted", "multi_period_margin_stability"),
        ("food_price_cycle_crowded", "disease_price_spike_extrapolated"),
        ("price_normalization", "feed_cost_spike", "government_inquiry", "price_fixing_investigation", "disease_normalization"),
        ("price_pass_through", "cost_stabilization", "multi_period_margin_stability"),
        ("disease_event", "feed_cost", "weather", "price_normalization", "government_inquiry"),
        "Livestock and food commodities are usually cyclical success or RedTeam cases, not structural Green.",
    ),
    Round65ScoreTarget(
        "ANIMAL_HEALTH_BIOSECURITY",
        E2RArchetype.ANIMAL_HEALTH_BIOSECURITY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round65ScoreWeightDraft(17, 15, 8, 10, 8, 0, 5),
        ("outbreak", "vaccine_conditional_approval", "government_stockpile"),
        ("government_purchase_contract", "government_stockpile", "repeat_vaccination", "guidance_up", "distribution_channel"),
        ("recurring_animal_health_revenue", "customer_diversification", "fcf_conversion"),
        ("animal_vaccine_event_crowded", "stockpile_story_priced"),
        ("government_purchase_end", "disease_normalization", "vaccine_unused", "trade_restriction"),
        ("government_purchase_contract", "repeat_vaccination", "recurring_revenue", "fcf_conversion"),
        ("emergency_license", "one_off_stockpile", "government_policy_uncertain", "outbreak_normalization"),
        "Animal-health can improve after approval and stockpile demand, but one-off outbreak risk remains.",
    ),
    Round65ScoreTarget(
        "EDUCATION_SPECIALTY_SERVICES",
        E2RArchetype.EDUCATION_SPECIALTY_SERVICES,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round65ScoreWeightDraft(17, 16, 5, 12, 11, 2, 5),
        ("ai_training", "adult_education", "job_training", "b2b_education_contract"),
        ("repeat_enrollment", "enterprise_contract", "completion_rate", "paid_conversion", "opm_improvement"),
        ("b2b_b2g_recurring_revenue", "student_roi", "low_cac", "fcf_conversion", "ai_disruption_defense"),
        ("ai_education_narrative_crowded", "valuation_before_profitability"),
        ("ai_substitutes_core_service", "bookings_miss", "subscriber_decline", "cac_spike", "bankruptcy"),
        ("enterprise_contract", "completion_rate", "student_roi", "opm_improvement", "fcf_conversion"),
        ("ai_disruption", "cac", "completion_rate", "student_roi", "debt", "bookings_miss"),
        "Education needs monetization, outcomes, retention, and margin; user growth alone is weak.",
    ),
    Round65ScoreTarget(
        "HOME_CHILD_EDUCATION",
        E2RArchetype.HOME_CHILD_EDUCATION,
        Round10ThemePosture.REDTEAM_FIRST,
        Round65ScoreWeightDraft(15, 11, 5, 10, 8, 0, 5),
        ("kids_product", "learning_material", "premium_childcare", "overseas_expansion"),
        ("repeat_subscription", "export_channel", "premium_mix", "inventory_control"),
        ("low_birthrate_offset", "recurring_revenue", "fcf_conversion"),
        ("premium_kids_theme_crowded",),
        ("low_birthrate", "tam_decline", "inventory_build", "regulatory_risk"),
        ("repeat_subscription", "export_channel", "low_birthrate_offset", "fcf_conversion"),
        ("birthrate_decline", "tam_shrink", "inventory", "policy_risk"),
        "Kids/home education faces low-birthrate TAM risk unless export or subscription economics offset it.",
    ),
    Round65ScoreTarget(
        "HOME_LIVING_APPLIANCE_RENTAL",
        E2RArchetype.HOME_LIVING_APPLIANCE_RENTAL,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round65ScoreWeightDraft(18, 16, 6, 12, 11, 2, 5),
        ("rental_accounts_growth", "new_product", "overseas_expansion"),
        ("rental_churn_stable", "filter_service_revenue", "care_service_revenue", "opm_fcf_improvement"),
        ("recurring_service_revenue_dominates", "hardware_cycle_less_important", "fcf_conversion"),
        ("rental_account_growth_crowded", "consumer_service_multiple_rerated"),
        ("replacement_demand_collapse", "dividend_suspension", "rental_churn_spike", "housing_weakness"),
        ("rental_churn_stable", "recurring_service_revenue", "opm_fcf_improvement", "overseas_margin"),
        ("replacement_cycle", "housing_turnover", "churn", "hardware_only", "dividend_suspension"),
        "Rental/care revenue can improve quality, but hardware replacement cycles and churn must be checked.",
    ),
    Round65ScoreTarget(
        "SERVICE_KIOSK_SELF_CHECKOUT",
        E2RArchetype.SERVICE_KIOSK_SELF_CHECKOUT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round65ScoreWeightDraft(16, 14, 7, 11, 9, 0, 5),
        ("labor_cost_increase", "unmanned_store", "self_checkout_rollout", "kiosk_installation"),
        ("installed_base", "maintenance_revenue", "payment_fee_revenue", "loss_prevention_effect"),
        ("recurring_service_revenue", "hardware_mix_declines", "customer_friction_low"),
        ("automation_theme_crowded", "installed_base_priced_before_service_revenue"),
        ("retailer_retreat", "theft_shrink", "customer_friction", "employee_workload", "one_off_hardware_sales"),
        ("maintenance_revenue", "payment_fee_revenue", "loss_prevention_effect", "recurring_service_revenue"),
        ("theft", "customer_friction", "retailer_retreat", "employee_workload", "one_off_hardware"),
        "Kiosk adoption needs service/fee economics; installation count alone is not productivity proof.",
    ),
    Round65ScoreTarget(
        "CONSUMER_REGULATED_PRODUCT",
        E2RArchetype.CONSUMER_REGULATED_PRODUCT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round65ScoreWeightDraft(18, 15, 8, 12, 10, 0, 5),
        ("fda_approval", "dea_rescheduling", "regulated_product_license"),
        ("sales_authorization", "channel_access", "tax_effect", "repeat_consumption"),
        ("regulatory_stability", "repeat_revenue", "fcf_conversion"),
        ("regulatory_approval_rally_crowded", "policy_reversal_ignored"),
        ("approval_revoked", "sales_ban", "legal_conflict", "youth_usage_controversy", "public_health_backlash"),
        ("sales_authorization", "channel_access", "repeat_consumption", "regulatory_stability"),
        ("public_health", "social_backlash", "legal_conflict", "license_scope", "youth_usage"),
        "Regulated consumer products can rerate on approval, but scope and public-health risks stay high.",
    ),
    Round65ScoreTarget(
        "FOOD_INPUT_REGULATED_CYCLE",
        E2RArchetype.FOOD_INPUT_REGULATED_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round65ScoreWeightDraft(17, 11, 12, 8, 8, 0, 5),
        ("grain_input_price", "alcohol_or_food_input_regulation", "feed_or_soybean_cost"),
        ("price_pass_through", "regulated_margin", "cost_stabilization"),
        ("multi_period_spread", "stable_regulation", "fcf_conversion"),
        ("food_input_spread_crowded", "regulated_price_theme"),
        ("cost_spike", "price_control", "regulatory_margin_cap", "demand_fade"),
        ("price_pass_through", "regulated_margin", "cost_stabilization", "fcf_conversion"),
        ("cost", "price_control", "regulation", "commodity_cycle"),
        "Food inputs need price pass-through and regulation checks before any structural claim.",
    ),
    Round65ScoreTarget(
        "POLICY_LOCAL_SERVICE_THEME",
        E2RArchetype.POLICY_LOCAL_SERVICE_THEME,
        Round10ThemePosture.REDTEAM_FIRST,
        Round65ScoreWeightDraft(5, 5, 5, 8, 5, 0, 3),
        ("jobs_policy", "local_service_policy", "regional_service_theme"),
        ("budget_approved", "contract_awarded", "revenue_visibility"),
        ("repeat_service_revenue", "fcf_conversion", "policy_execution"),
        ("local_service_policy_theme_crowded", "election_policy_rally"),
        ("budget_cut", "policy_reversal", "no_company_exposure", "project_delay"),
        ("budget_approved", "contract_awarded", "revenue_visibility", "fcf_conversion"),
        ("policy_dependency", "budget_missing", "no_contract", "no_revenue"),
        "Local-service policy is routing data until budget, contracts, and revenue are visible.",
    ),
    Round65ScoreTarget(
        "AGRI_DISEASE_EVENT_OVERLAY",
        E2RArchetype.AGRI_DISEASE_EVENT_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round65ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("avian_flu", "asf", "livestock_disease", "egg_or_meat_price_spike"),
        ("government_stockpile_or_order_needed",),
        ("normally_blocked_without_repeat_demand",),
        ("disease_theme_crowded", "price_spike_extrapolated"),
        ("disease_normalization", "price_normalization", "government_inquiry"),
        ("repeat_procurement", "multi_period_margin", "low_normalization_risk"),
        ("one_off_disease", "price_normalization", "government_inquiry"),
        "Disease and commodity price spikes are RedTeam overlays, not positive score.",
        gate_only=True,
    ),
    Round65ScoreTarget(
        "AI_EDUCATION_DISRUPTION_OVERLAY",
        E2RArchetype.AI_EDUCATION_DISRUPTION_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round65ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("ai_tutor", "ai_search_answer", "ai_education_tool"),
        ("ai_defense_contract_or_productivity_needed",),
        ("normally_blocked_if_core_service_substituted",),
        ("ai_education_theme_crowded", "user_growth_before_monetization"),
        ("traffic_decline", "subscriber_decline", "bookings_miss", "layoff", "bankruptcy"),
        ("b2b_contract", "completion_rate", "student_roi", "fcf_conversion"),
        ("ai_substitution", "cac_spike", "bookings_miss", "debt"),
        "AI can be a product feature or a thesis break; traffic and subscriber evidence decide.",
        gate_only=True,
    ),
    Round65ScoreTarget(
        "REGULATED_CONSUMER_APPROVAL_OVERLAY",
        E2RArchetype.REGULATED_CONSUMER_APPROVAL_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round65ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("fda_approval", "dea_rescheduling", "license_or_ban"),
        ("sales_authorization_and_scope_needed",),
        ("normally_blocked_without_scope_channel_and_recurring_revenue",),
        ("approval_theme_crowded", "policy_relief_rally"),
        ("approval_revoked", "limited_scope", "youth_usage", "state_federal_conflict", "public_health_backlash"),
        ("authorization_scope", "sales_channel", "repeat_consumption", "regulatory_stability"),
        ("license_scope", "legal_conflict", "youth_usage", "public_health"),
        "Approval headlines gate risk; they do not add positive score without scope, channel, and repeat revenue.",
        gate_only=True,
    ),
)


ROUND65_CASE_CANDIDATES: tuple[Round65CaseCandidate, ...] = (
    Round65CaseCandidate(
        "john_deere_autonomous_agri_ces_case",
        "AGRI_MACHINERY_PRECISION_CYCLE",
        "DE",
        "John Deere autonomous agriculture CES case",
        "US",
        "success_candidate",
        date(2025, 1, 6),
        None,
        None,
        None,
        None,
        ("autonomous_tractor", "precision_agriculture", "labor_shortage_solution", "software_attach_potential"),
        ("farm_income", "financing_cost", "adoption_rate_unverified", "right_to_repair"),
        "precision_agri_stage1_success_candidate",
        "needs_price_backfill",
        ("The Verge John Deere CES autonomous equipment",),
        "Autonomous agriculture technology is useful Stage 1 evidence, but sales, farmer ROI, and software attachment must verify it.",
        (E2RArchetype.SMART_FARM_AGRI_TECH,),
    ),
    Round65CaseCandidate(
        "deere_farm_equipment_demand_slowdown_case",
        "AGRI_MACHINERY_PRECISION_CYCLE",
        "DE",
        "Deere farm equipment demand slowdown",
        "US",
        "4c_thesis_break",
        date(2025, 2, 13),
        None,
        None,
        None,
        date(2025, 2, 13),
        ("equipment_sales_decline", "farm_income_weakness", "high_borrowing_cost", "revenue_decline"),
        ("farm_income_weakness", "high_borrowing_cost", "equipment_sales_decline", "tariff_uncertainty"),
        "agri_machinery_cycle_4c_watch",
        "needs_price_backfill",
        ("Reuters Deere muted farm equipment demand",),
        "Precision agriculture can be promising while the machinery company is still capped by farm-income and financing cycles.",
    ),
    Round65CaseCandidate(
        "deere_right_to_repair_settlement_case",
        "AGRI_MACHINERY_PRECISION_CYCLE",
        "DE",
        "Deere right-to-repair settlement",
        "US",
        "failed_rerating",
        date(2026, 4, 1),
        None,
        None,
        None,
        None,
        ("right_to_repair_flag", "repair_settlement_amount", "software_lock_in"),
        ("right_to_repair_lawsuit", "repair_monopoly_allegation", "customer_backlash"),
        "agri_machinery_software_lockin_regulatory_watch",
        "needs_price_backfill",
        ("AP Deere right-to-repair settlement",),
        "Software-enabled equipment lock-in can become a RedTeam risk if regulation or lawsuits weaken the model.",
    ),
    Round65CaseCandidate(
        "zoetis_bird_flu_vaccine_conditional_case",
        "ANIMAL_HEALTH_BIOSECURITY",
        "ZTS",
        "Zoetis bird flu vaccine conditional clearance",
        "US",
        "success_candidate",
        date(2025, 2, 14),
        date(2025, 2, 14),
        None,
        None,
        None,
        ("vaccine_conditional_approval", "government_stockpile", "biosecurity_demand"),
        ("emergency_license", "government_policy_uncertain", "one_off_stockpile", "trade_restriction"),
        "animal_health_event_to_contract_candidate",
        "needs_price_backfill",
        ("Reuters Zoetis bird flu vaccine conditional clearance",),
        "Conditional approval and stockpile rebuilding can move disease news toward Stage 2, but recurring use must be checked.",
    ),
    Round65CaseCandidate(
        "calmaine_egg_price_profit_case",
        "AGRI_LIVESTOCK_FOOD_COMMODITY",
        "CALM",
        "Cal-Maine egg price profit cycle",
        "US",
        "cyclical_success",
        date(2025, 4, 9),
        date(2025, 4, 9),
        None,
        date(2025, 4, 9),
        None,
        ("egg_price_spike", "avian_flu_supply_shock", "op_profit_increase"),
        ("price_normalization", "disease_normalization", "price_fixing_investigation"),
        "livestock_price_cyclical_success_regulatory_watch",
        "needs_price_backfill",
        ("Financial Times Cal-Maine egg profit cycle",),
        "Egg-price profit spikes can be real cyclical success, but price normalization and investigations cap Green.",
        (E2RArchetype.AGRI_DISEASE_EVENT_OVERLAY,),
    ),
    Round65CaseCandidate(
        "bowery_vertical_farming_shutdown_case",
        "SMART_FARM_AGRI_TECH",
        "BOWERY_PRIVATE",
        "Bowery vertical farming shutdown",
        "US",
        "4c_thesis_break",
        date(2024, 11, 5),
        None,
        None,
        None,
        date(2024, 11, 5),
        ("vertical_farming", "shutdown", "premium_pricing_failure", "unit_economics_failure"),
        ("unit_economics_failure", "energy_cost", "premium_pricing_failure", "capex_burden"),
        "vertical_farming_unit_economics_4c",
        "needs_price_backfill",
        ("Axios Bowery shutdown",),
        "Vertical farming can fail when consumers do not pay enough premium to cover energy and capex.",
    ),
    Round65CaseCandidate(
        "appharvest_chapter11_case",
        "SMART_FARM_AGRI_TECH",
        "APPH",
        "AppHarvest Chapter 11",
        "US",
        "4c_thesis_break",
        date(2023, 7, 24),
        None,
        None,
        None,
        date(2023, 7, 24),
        ("vertical_farming", "chapter11", "greenhouse_sale"),
        ("chapter11", "capex_burden", "unit_economics_failure", "labor_or_safety_issue"),
        "smart_farm_spac_hard_4c",
        "needs_price_backfill",
        ("AppHarvest reference",),
        "Hydroponics and greenhouse capex without unit economics can become hard 4C.",
    ),
    Round65CaseCandidate(
        "duolingo_ai_strategy_bookings_miss_case",
        "EDUCATION_SPECIALTY_SERVICES",
        "DUOL",
        "Duolingo AI strategy and softer bookings",
        "US",
        "4c_thesis_break",
        date(2026, 2, 26),
        None,
        None,
        None,
        date(2026, 2, 26),
        ("ai_speaking_feature", "user_growth_priority", "bookings_outlook_miss"),
        ("bookings_miss", "monetization_pressure", "ai_cost"),
        "education_app_success_candidate_but_monetization_watch",
        "needs_price_backfill",
        ("Reuters Duolingo bookings outlook",),
        "Education apps need bookings and monetization; AI features and user growth alone can still break the thesis.",
        (E2RArchetype.AI_EDUCATION_DISRUPTION_OVERLAY,),
    ),
    Round65CaseCandidate(
        "chegg_ai_disruption_case",
        "EDUCATION_SPECIALTY_SERVICES",
        "CHGG",
        "Chegg AI disruption",
        "US",
        "4c_thesis_break",
        date(2023, 5, 2),
        None,
        None,
        None,
        date(2023, 5, 2),
        ("ai_substitutes_core_service", "traffic_decline", "subscriber_decline"),
        ("ai_disruption", "traffic_decline", "subscriber_decline", "layoff", "strategic_review"),
        "ai_education_disruption_hard_4c",
        "needs_price_backfill",
        ("Investopedia Chegg ChatGPT impact",),
        "Education recurring revenue can break when AI substitutes the core service or search traffic channel.",
        (E2RArchetype.AI_EDUCATION_DISRUPTION_OVERLAY,),
    ),
    Round65CaseCandidate(
        "2u_chapter11_case",
        "EDUCATION_SPECIALTY_SERVICES",
        "TWOU",
        "2U Chapter 11",
        "US",
        "4c_thesis_break",
        date(2024, 7, 25),
        None,
        None,
        None,
        date(2024, 7, 25),
        ("online_education_platform", "chapter11", "debt_restructuring"),
        ("chapter11", "student_roi", "debt", "partner_concentration", "regulatory_oversight"),
        "online_education_opm_hard_4c",
        "needs_price_backfill",
        ("Wall Street Journal 2U Chapter 11",),
        "Online education platforms need CAC, completion, student ROI, partner concentration, and debt checks.",
    ),
    Round65CaseCandidate(
        "coway_rental_recurring_case",
        "HOME_LIVING_APPLIANCE_RENTAL",
        "021240",
        "Coway rental recurring service model",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("rental_accounts", "filter_service_revenue", "care_service_revenue", "overseas_accounts"),
        ("rental_churn", "competition", "overseas_margin", "quality_recall"),
        "recurring_home_service_candidate",
        "needs_price_backfill",
        ("Coway company reference",),
        "Rental accounts and care services are stronger than one-time appliance sales, but churn and overseas margin remain required fields.",
    ),
    Round65CaseCandidate(
        "whirlpool_dividend_suspension_case",
        "HOME_LIVING_APPLIANCE_RENTAL",
        "WHR",
        "Whirlpool dividend suspension and hardware cycle",
        "US",
        "4c_thesis_break",
        date(2026, 5, 7),
        None,
        None,
        None,
        date(2026, 5, 7),
        ("home_appliance_hardware", "dividend_suspension", "replacement_demand_collapse", "guidance_cut"),
        ("replacement_demand_collapse", "dividend_suspension", "housing_turnover_weakness", "debt_reduction_pressure"),
        "home_appliance_hardware_cycle_4c",
        "needs_price_backfill",
        ("Reuters Whirlpool dividend suspension",),
        "Appliance hardware without recurring rental/care revenue remains exposed to housing and replacement cycles.",
    ),
    Round65CaseCandidate(
        "target_self_checkout_limit_case",
        "SERVICE_KIOSK_SELF_CHECKOUT",
        "TARGET_SELF_CHECKOUT",
        "Target self-checkout item limit",
        "US",
        "failed_rerating",
        date(2024, 3, 16),
        None,
        None,
        None,
        None,
        ("self_checkout_rollout", "self_checkout_limit", "retailer_retreat", "customer_friction"),
        ("theft_shrink", "customer_friction", "retailer_retreat", "employee_workload"),
        "kiosk_self_checkout_operational_counterexample",
        "needs_price_backfill",
        ("New York Post Target self-checkout limit", "arXiv pseudo-automation research"),
        "Self-checkout installation count is weak if theft, customer friction, and operational workload rise.",
    ),
    Round65CaseCandidate(
        "juul_fda_approval_case",
        "CONSUMER_REGULATED_PRODUCT",
        "JUUL_PRIVATE",
        "Juul FDA tobacco and menthol e-cigarette approval",
        "US",
        "success_candidate",
        date(2025, 7, 17),
        date(2025, 7, 17),
        None,
        None,
        None,
        ("fda_approval", "sales_authorization", "repeat_consumption", "license_scope"),
        ("youth_usage_controversy", "policy_reversal", "license_scope", "public_health_warning"),
        "regulated_consumer_approval_stage2_candidate",
        "needs_price_backfill",
        ("Reuters Juul FDA approval",),
        "Regulatory approval can change Stage materially, but scope, channels, social backlash, and reversal risk remain core checks.",
        (E2RArchetype.REGULATED_CONSUMER_APPROVAL_OVERLAY,),
    ),
    Round65CaseCandidate(
        "cannabis_schedule3_limited_case",
        "CONSUMER_REGULATED_PRODUCT",
        "CANNABIS_POLICY_BASKET",
        "Cannabis Schedule III limited rescheduling",
        "US",
        "event_premium",
        date(2026, 5, 12),
        None,
        None,
        date(2026, 5, 12),
        None,
        ("dea_rescheduling", "tax_effect_possible", "regulated_product_policy"),
        ("legal_conflict", "license_scope", "no_full_legalization", "dea_registration_required"),
        "regulated_consumer_policy_stage1_watch",
        "needs_price_backfill",
        ("Reuters cannabis rescheduling final order",),
        "Rescheduling can help some operators, but it is not full legalization and remains a policy/event watch.",
        (E2RArchetype.REGULATED_CONSUMER_APPROVAL_OVERLAY,),
    ),
)


ROUND65_PRICE_FIELDS: tuple[str, ...] = (
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
    "farm_income_indicator",
    "equipment_sales_growth",
    "precision_agriculture_revenue",
    "autonomous_equipment_order",
    "software_attach_rate",
    "farmer_financing_cost",
    "tariff_exposure_flag",
    "right_to_repair_flag",
    "repair_settlement_amount",
    "vertical_farming_revenue",
    "vertical_farming_energy_cost",
    "capacity_utilization",
    "unit_economics_margin",
    "premium_pricing_success_flag",
    "yield_loss_flag",
    "chapter11_flag",
    "chapter7_flag",
    "shutdown_flag",
    "livestock_price_change",
    "egg_price_change",
    "pork_price_change",
    "chicken_price_change",
    "feed_cost_change",
    "soybean_price_change",
    "disease_event_flag",
    "avian_flu_flag",
    "asf_flag",
    "government_stockpile_flag",
    "vaccine_approval_flag",
    "vaccine_order_value",
    "price_fixing_investigation_flag",
    "education_revenue_growth",
    "bookings_growth",
    "subscription_count",
    "paid_conversion_rate",
    "enterprise_contract_count",
    "completion_rate",
    "student_roi_metric",
    "cac",
    "churn_rate",
    "ai_disruption_flag",
    "traffic_decline_flag",
    "layoff_flag",
    "bankruptcy_flag",
    "rental_accounts",
    "rental_churn",
    "recurring_service_revenue_ratio",
    "filter_service_revenue",
    "hardware_sales_ratio",
    "dividend_suspension_flag",
    "replacement_demand_indicator",
    "housing_turnover_indicator",
    "quality_recall_flag",
    "kiosk_installed_base",
    "maintenance_revenue",
    "payment_fee_revenue",
    "retailer_retreat_flag",
    "self_checkout_limit_flag",
    "theft_shrink_indicator",
    "customer_friction_flag",
    "employee_workload_flag",
    "regulatory_approval_flag",
    "fda_approval_flag",
    "dea_rescheduling_flag",
    "license_scope",
    "youth_usage_risk_flag",
    "public_health_warning_flag",
    "legal_conflict_flag",
    "compliance_cost",
    "sales_channel_authorized_flag",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def target_for(target_id: str) -> Round65ScoreTarget | None:
    for target in ROUND65_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round65_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND65_CASE_CANDIDATES:
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
                f"Round65 R12 Loop-2 case for {candidate.target_id}; "
                "unit-economics evidence is calibration-only and missing prices remain unfilled."
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
                "life_essential_policy_or_disease_label_is_not_green_evidence_alone",
                "repeat_contract_repeat_revenue_unit_economics_or_regulatory_scope_required",
                "fcf_conversion_required_for_green",
                "do_not_invent_unit_economics_orders_cac_churn_regulatory_scope_or_stage_prices",
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


def round65_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND65_SCORE_TARGETS:
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


def round65_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND65_CASE_CANDIDATES:
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


def round65_stage_date_rows() -> tuple[dict[str, str], ...]:
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
        for target in ROUND65_SCORE_TARGETS
    )


def round65_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round65_backfill": "true"} for field in ROUND65_PRICE_FIELDS)


def round65_summary() -> dict[str, int | bool]:
    records = round65_case_records()
    return {
        "target_count": len(ROUND65_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND65_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND65_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND65_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND65_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round65_r12_loop2_reports(
    *,
    output_directory: str | Path = ROUND65_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND65_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND65_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round65_r12_loop2_agri_life_misc_summary.md",
        "case_matrix": output / "round65_r12_loop2_case_matrix.csv",
        "stage_date_plan": output / "round65_r12_loop2_stage_date_plan.csv",
        "green_guardrails": output / "round65_r12_loop2_green_guardrails.md",
        "unit_economics_caps": output / "round65_r12_loop2_unit_economics_caps.md",
        "price_validation_plan": output / "round65_r12_loop2_price_validation_plan.md",
        "price_fields": output / "round65_r12_loop2_price_fields.csv",
    }
    _write_case_jsonl(round65_case_records(), cases)
    _write_rows(round65_score_profile_rows(), score_profiles)
    _write_rows(round65_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round65_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round65_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round65_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round65_green_guardrail_markdown(), encoding="utf-8")
    paths["unit_economics_caps"].write_text(render_round65_unit_economics_cap_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round65_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round65_summary_markdown() -> str:
    summary = round65_summary()
    lines = [
        "# Round-65 R12 Loop-2 Agriculture / Life Services / Misc Summary",
        "",
        f"- source_round: `{ROUND65_SOURCE_ROUND_PATH}`",
        "- large_sector: `EDUCATION_LIFE_AGRI_MISC`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- cyclical_success_count: {summary['cyclical_success_count']}",
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
        "- R12 Loop-2 separates recurring FCF from disease, weather, policy, AI, hardware, and regulation headlines.",
        "- Example: smart farming news is Stage 1 until actual orders, unit economics, energy cost, and FCF are visible.",
        "- Example: education apps need bookings, paid conversion, CAC, and monetization, not user growth alone.",
        "- Example: rental appliances can improve quality only if recurring care revenue and churn data beat the hardware cycle.",
    ]
    return "\n".join(lines) + "\n"


def render_round65_green_guardrail_markdown() -> str:
    lines = [
        "# Round-65 R12 Loop-2 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND65_SCORE_TARGETS:
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
            "- Do not apply these R12 Loop-2 v2 weights to production scoring yet.",
            "- Do not treat essential demand, policy support, weather, disease, grain prices, education users, rental accounts, or FDA/DEA headlines as Green evidence by itself.",
            "- Do not invent unit economics, government orders, completion rates, CAC, churn, regulatory scope, software attach rate, or price-path fields.",
            "- Do not lower Stage 3-Green for R12 recall. Green requires repeat contracts, repeat revenue, unit economics, regulatory stability, and FCF conversion.",
            "- Treat Chapter 11, AI substitution, bookings misses, dividend suspension, retailer retreat, theft/shrink, public-health reversal, commodity normalization, and right-to-repair risk as RedTeam evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round65_unit_economics_cap_markdown() -> str:
    lines = [
        "# Round-65 R12 Loop-2 Unit-Economics / Cycle Caps",
        "",
        "- `SMART_FARM_AGRI_TECH`: technology and policy are Stage 1; orders, energy cost, utilization, and FCF decide escalation.",
        "- `AGRI_MACHINERY_PRECISION_CYCLE`: autonomous equipment still depends on farm income, financing cost, right-to-repair risk, and replacement cycles.",
        "- `AGRI_LIVESTOCK_FOOD_COMMODITY`: price spikes can be cyclical success, but disease and price normalization cap Green.",
        "- `ANIMAL_HEALTH_BIOSECURITY`: conditional approval and stockpile can create Stage 2, but repeated use decides durability.",
        "- `EDUCATION_SPECIALTY_SERVICES`: AI education can work only when contracts, completion, retention, CAC, and margin are visible.",
        "- `HOME_LIVING_APPLIANCE_RENTAL`: recurring rental/care revenue must dominate hardware replacement-cycle risk.",
        "- `SERVICE_KIOSK_SELF_CHECKOUT`: installed base must convert into maintenance, payment fee, or loss-prevention economics.",
        "- `CONSUMER_REGULATED_PRODUCT`: approval scope, channel access, public-health risk, and legal conflict must be checked.",
        "",
        "Simple example: a vertical-farming company may sound structural because food is essential. If energy cost and unit economics are negative, it is a 4C-style counterexample rather than Stage 3-Green.",
    ]
    return "\n".join(lines) + "\n"


def render_round65_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-65 R12 Loop-2 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare price paths with farm income, equipment sales, commodity prices, disease events, recurring revenue, CAC, churn, regulatory scope, and FCF.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | stage candidate | check |",
        "| --- | --- | --- |",
    ]
    for row in round65_case_candidate_rows():
        if row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"]:
            stage_date = row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or row["stage1_date"]
            lines.append(f"| `{row['case_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `smart_farm_unit_economics_aligned`: orders, utilization, energy cost, and FCF move together.",
            "- `vertical_farming_4c`: shutdown, Chapter 11, premium-pricing failure, or CAPEX burden breaks the case.",
            "- `agri_machinery_tech_but_cycle_watch`: technology exists, but farm income, financing, and equipment demand cap the case.",
            "- `animal_health_event_to_contract`: disease event turns into vaccine approval, stockpile, and repeated use.",
            "- `livestock_cyclical_success`: price spike generated profit, but structural durability is weak.",
            "- `education_ai_disruption_4c`: AI replaces the core service or weakens traffic, subscribers, bookings, and revenue.",
            "- `rental_recurring_success`: rental accounts, churn, care-service revenue, and FCF are confirmed.",
            "- `regulated_consumer_approval_stage2`: FDA/DEA approval can create Stage 2, but scope and public-health gates remain.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round65CaseCandidate) -> str:
    if candidate.case_type == "success_candidate" and (
        "recurring" in candidate.alignment_hint
        or "contract" in candidate.alignment_hint
        or "approval" in candidate.alignment_hint
        or "candidate" in candidate.alignment_hint
    ):
        return "aligned"
    if candidate.case_type == "cyclical_success":
        return "aligned"
    if candidate.case_type in {"event_premium", "one_off", "4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type in {"failed_rerating", "4c_thesis_break"}:
        return "false_positive_score"
    return "unknown"


def _rerating_result(candidate: Round65CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "success_candidate":
        if "approval" in candidate.alignment_hint or "event_to_contract" in candidate.alignment_hint:
            return "event_premium"
        return "unknown"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
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
    "ROUND65_CASE_CANDIDATES",
    "ROUND65_DEFAULT_CASES_PATH",
    "ROUND65_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND65_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND65_PRICE_FIELDS",
    "ROUND65_SCORE_TARGETS",
    "ROUND65_SOURCE_ROUND_PATH",
    "Round65CaseCandidate",
    "Round65ScoreTarget",
    "Round65ScoreWeightDraft",
    "render_round65_green_guardrail_markdown",
    "render_round65_price_validation_plan_markdown",
    "render_round65_summary_markdown",
    "render_round65_unit_economics_cap_markdown",
    "round65_case_candidate_rows",
    "round65_case_records",
    "round65_price_field_rows",
    "round65_score_profile_rows",
    "round65_stage_date_rows",
    "round65_summary",
    "target_for",
    "write_round65_r12_loop2_reports",
]
