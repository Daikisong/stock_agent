"""Round-104 R12 Loop-5 agriculture, life services, and miscellaneous pack.

Round 104 tightens the R12 unit-economics pack from Round 65. Agriculture,
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


ROUND104_SOURCE_ROUND_PATH = "docs/round/round_104.md"
ROUND104_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round104_r12_loop5_agri_life_misc"
ROUND104_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r12_loop5_round104.jsonl"
ROUND104_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round104_r12_loop5_v5.csv"


@dataclass(frozen=True)
class Round104ScoreWeightDraft:
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
class Round104ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round104ScoreWeightDraft
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
class Round104CaseCandidate:
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


ROUND104_SCORE_TARGETS: tuple[Round104ScoreTarget, ...] = (
    Round104ScoreTarget(
        "SMART_FARM_AGRI_TECH",
        E2RArchetype.SMART_FARM_AGRI_TECH,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(17, 13, 12, 9, 8, 0, 5),
        ("smart_farm_policy", "autonomous_agri_equipment", "vertical_farming", "agri_ai"),
        ("actual_order", "operation_contract", "maintenance_saas_revenue", "capacity_utilization"),
        ("unit_economics_positive", "fcf_conversion", "repeat_contracts", "energy_cost_control"),
        ("smart_farm_theme_crowded", "vertical_farming_story_priced_before_unit_economics"),
        ("chapter11", "shutdown", "energy_cost_failure", "premium_pricing_failure", "capex_burden"),
        ("actual_order", "operation_contract", "unit_economics_positive", "fcf_conversion"),
        ("energy_cost", "capex_burden", "unit_economics_failure", "subsidy_dependency"),
        "Smart-farm labels need orders, utilization, energy-cost proof, and FCF before Green.",
    ),
    Round104ScoreTarget(
        "VERTICAL_FARMING_UNIT_ECONOMICS",
        E2RArchetype.VERTICAL_FARMING_UNIT_ECONOMICS,
        Round10ThemePosture.REDTEAM_FIRST,
        Round104ScoreWeightDraft(8, 6, 5, 7, 5, 0, 4),
        ("vertical_farming", "indoor_farm", "hydroponics", "leafy_greens", "ai_farming_narrative"),
        ("capacity_utilization", "customer_contract", "yield_stability", "premium_pricing_success", "energy_cost_control"),
        ("unit_economics_positive", "repeat_customer_demand", "fcf_conversion", "low_energy_cost_burden"),
        ("vertical_farming_unicorn_narrative", "premium_pricing_assumed", "capex_risk_ignored"),
        ("shutdown", "chapter11", "energy_cost_failure", "premium_pricing_failure", "yield_loss", "capex_burden"),
        ("unit_economics_positive", "customer_contract", "energy_cost_control", "fcf_conversion"),
        ("energy_cost_failure", "capex_burden", "premium_pricing_failure", "shutdown", "chapter11"),
        "Vertical farming is separated from smart-farm automation because unit economics can break the whole thesis.",
    ),
    Round104ScoreTarget(
        "AGRI_MACHINERY_PRECISION_CYCLE",
        E2RArchetype.AGRI_MACHINERY_PRECISION_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(16, 13, 10, 10, 9, 1, 5),
        ("autonomous_tractor", "precision_agriculture", "agri_drone", "ces_technology_demo"),
        ("equipment_sales_growth", "farmer_roi", "software_attach_rate", "service_revenue"),
        ("recurring_software_or_service", "farm_income_support", "low_financing_stress"),
        ("autonomous_agri_theme_crowded", "technology_priced_before_adoption"),
        ("farm_income_weakness", "high_borrowing_cost", "equipment_sales_decline", "right_to_repair_lawsuit"),
        ("equipment_sales_growth", "farmer_roi", "software_attach_rate", "service_revenue"),
        ("farm_income", "financing_cost", "replacement_cycle", "right_to_repair", "dealer_inventory"),
        "Autonomous farm equipment still needs farm-income, financing, adoption, and software attachment checks.",
    ),
    Round104ScoreTarget(
        "AGRI_MACHINERY_DEMAND_CYCLE",
        E2RArchetype.AGRI_MACHINERY_DEMAND_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(14, 11, 8, 9, 7, 1, 5),
        ("equipment_replacement_cycle", "farm_productivity", "precision_agriculture_narrative"),
        ("equipment_sales_growth", "dealer_inventory_normalization", "farm_income_improvement"),
        ("recurring_software_or_service", "equipment_cycle_buffered", "fcf_conversion"),
        ("autonomous_precision_agri_expectation_crowded",),
        ("crop_price_decline", "financing_cost_increase", "rental_instead_of_purchase", "dealer_inventory_increase"),
        ("equipment_sales_growth", "dealer_inventory_normalization", "service_revenue", "fcf_conversion"),
        ("farm_income_weakness", "crop_price", "dealer_inventory", "farmer_financing_cost"),
        "Farm-equipment demand is scored separately from precision-agriculture technology because crop prices and dealer inventory can break the case.",
    ),
    Round104ScoreTarget(
        "AGRI_MACHINERY_SOFTWARE_LOCKIN",
        E2RArchetype.AGRI_MACHINERY_SOFTWARE_LOCKIN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(16, 14, 9, 11, 9, 1, 5),
        ("software_enabled_equipment", "precision_agriculture_platform", "dealer_network_lockin", "repair_software"),
        ("software_attach_rate", "service_revenue", "farmer_roi", "authorized_service_revenue"),
        ("recurring_software_or_service", "low_regulatory_risk", "customer_retention", "fcf_conversion"),
        ("software_lockin_multiple_expansion", "right_to_repair_risk_ignored"),
        ("right_to_repair_lawsuit", "repair_monopoly_allegation", "settlement_cost", "ftc_lawsuit", "customer_backlash"),
        ("software_attach_rate", "service_revenue", "customer_retention", "fcf_conversion"),
        ("right_to_repair", "repair_monopoly", "ftc_lawsuit", "customer_backlash"),
        "Farm-equipment software lock-in earns credit only after right-to-repair and dealer-monopoly risks are checked.",
    ),
    Round104ScoreTarget(
        "RIGHT_TO_REPAIR_REGULATORY_OVERLAY",
        E2RArchetype.RIGHT_TO_REPAIR_REGULATORY_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round104ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("right_to_repair_lawsuit", "repair_monopoly_allegation", "ftc_scrutiny"),
        ("settlement_terms", "digital_tool_access", "customer_repair_rights"),
        ("low_regulatory_risk",),
        ("software_lockin_priced_without_regulatory_risk",),
        ("settlement_cost", "ftc_lawsuit", "repair_monopoly_allegation", "customer_backlash"),
        ("regulatory_risk_resolved", "customer_retention", "service_revenue"),
        ("right_to_repair", "repair_monopoly", "settlement_cost", "ftc_lawsuit", "customer_backlash"),
        "Right-to-repair is a RedTeam overlay for software lock-in; it gates confidence rather than adding positive score.",
        gate_only=True,
    ),
    Round104ScoreTarget(
        "AGRI_INPUT_SEED_CROP_PROTECTION",
        E2RArchetype.AGRI_INPUT_SEED_CROP_PROTECTION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(18, 16, 11, 12, 10, 1, 5),
        ("seed_licensing", "crop_protection_patent", "food_security", "new_product"),
        ("licensing_revenue", "price_pass_through", "farmer_roi", "ebitda_improvement"),
        ("repeat_seed_revenue", "crop_protection_margin", "litigation_control", "fcf_conversion"),
        ("food_security_seed_ip_theme_crowded",),
        ("crop_protection_litigation", "patent_expiry", "regulatory_restriction", "farmer_margin_pressure"),
        ("licensing_revenue", "farmer_roi", "ebitda_improvement", "fcf_conversion"),
        ("litigation", "patent_expiry", "regulation", "farmer_margin"),
        "Seed and crop-protection stories need licensing/IP economics, farmer ROI, and litigation/regulatory controls.",
    ),
    Round104ScoreTarget(
        "FERTILIZER_INPUT_COST_CYCLE",
        E2RArchetype.FERTILIZER_INPUT_COST_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(18, 11, 14, 9, 8, 0, 5),
        ("potash_price", "phosphate_price", "nitrogen_price", "supply_disruption", "crop_nutrient_depletion"),
        ("fertilizer_volume", "fertilizer_price", "margin_improvement", "application_rate"),
        ("low_cost_supply", "structural_demand", "fcf_conversion"),
        ("fertilizer_price_spike_theme_crowded",),
        ("crop_price_decline", "farmer_margin_pressure", "demand_deferral", "input_cost_spike", "guidance_cut"),
        ("volume_growth", "price_margin", "farmer_roi", "fcf_conversion"),
        ("crop_price", "farmer_margin", "input_cost", "demand_deferral", "geopolitical_supply"),
        "Fertilizer can be a strong cycle, but crop prices, farmer margin, input cost, and geopolitics cap Green.",
    ),
    Round104ScoreTarget(
        "AGRI_LIVESTOCK_FOOD_COMMODITY",
        E2RArchetype.AGRI_LIVESTOCK_FOOD_COMMODITY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round104ScoreWeightDraft(18, 8, 14, 8, 7, 0, 5),
        ("avian_flu", "asf", "egg_price_spike", "feed_cost_change", "soybean_or_tuna_price"),
        ("price_pass_through", "op_profit_increase", "cost_stabilization"),
        ("structural_green_restricted", "multi_period_margin_stability"),
        ("food_price_cycle_crowded", "disease_price_spike_extrapolated"),
        ("price_normalization", "feed_cost_spike", "government_inquiry", "price_fixing_investigation", "disease_normalization"),
        ("price_pass_through", "cost_stabilization", "multi_period_margin_stability"),
        ("disease_event", "feed_cost", "weather", "price_normalization", "government_inquiry"),
        "Livestock and food commodities are usually cyclical success or RedTeam cases, not structural Green.",
    ),
    Round104ScoreTarget(
        "ANIMAL_HEALTH_BIOSECURITY",
        E2RArchetype.ANIMAL_HEALTH_BIOSECURITY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(18, 16, 8, 11, 9, 0, 5),
        ("outbreak", "vaccine_conditional_approval", "government_stockpile"),
        ("government_purchase_contract", "government_stockpile", "repeat_vaccination", "guidance_up", "distribution_channel"),
        ("recurring_animal_health_revenue", "customer_diversification", "fcf_conversion"),
        ("animal_vaccine_event_crowded", "stockpile_story_priced"),
        ("government_purchase_end", "disease_normalization", "vaccine_unused", "trade_restriction"),
        ("government_purchase_contract", "repeat_vaccination", "recurring_revenue", "fcf_conversion"),
        ("emergency_license", "one_off_stockpile", "government_policy_uncertain", "outbreak_normalization"),
        "Animal-health can improve after approval and stockpile demand, but one-off outbreak risk remains.",
    ),
    Round104ScoreTarget(
        "AGRI_DISEASE_AI_MONITORING",
        E2RArchetype.AGRI_DISEASE_AI_MONITORING,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(14, 12, 8, 10, 8, 0, 5),
        ("disease_ai_monitoring", "farm_sensor", "biosecurity_app", "livestock_surveillance"),
        ("farm_adoption_contract", "data_quality", "privacy_compliance", "repeat_subscription"),
        ("recurring_monitoring_revenue", "low_privacy_risk", "fcf_conversion"),
        ("agri_ai_monitoring_theme_crowded",),
        ("data_quality_failure", "farm_privacy_backlash", "no_adoption_contract", "subsidy_dependency"),
        ("farm_contract", "repeat_subscription", "data_quality", "fcf_conversion"),
        ("data_quality", "privacy", "adoption_missing", "subsidy_dependency"),
        "Disease AI monitoring needs farm contracts, data quality, privacy compliance, and repeat subscriptions.",
    ),
    Round104ScoreTarget(
        "EDUCATION_SPECIALTY_SERVICES",
        E2RArchetype.EDUCATION_SPECIALTY_SERVICES,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(17, 16, 5, 12, 10, 2, 5),
        ("ai_training", "adult_education", "job_training", "b2b_education_contract"),
        ("repeat_enrollment", "enterprise_contract", "completion_rate", "paid_conversion", "opm_improvement"),
        ("b2b_b2g_recurring_revenue", "student_roi", "low_cac", "fcf_conversion", "ai_disruption_defense"),
        ("ai_education_narrative_crowded", "valuation_before_profitability"),
        ("ai_substitutes_core_service", "bookings_miss", "subscriber_decline", "cac_spike", "bankruptcy"),
        ("enterprise_contract", "completion_rate", "student_roi", "opm_improvement", "fcf_conversion"),
        ("ai_disruption", "cac", "completion_rate", "student_roi", "debt", "bookings_miss"),
        "Education needs monetization, outcomes, retention, and margin; user growth alone is weak.",
    ),
    Round104ScoreTarget(
        "EDTECH_AI_MONETIZATION_TRADEOFF",
        E2RArchetype.EDTECH_AI_MONETIZATION_TRADEOFF,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(16, 15, 5, 12, 9, 1, 5),
        ("ai_speaking", "ai_tutor", "ai_learning_feature"),
        ("engagement_growth", "bookings_growth", "paid_conversion", "ai_cost_control"),
        ("bookings_and_margin_together", "fcf_conversion", "paid_conversion_stable"),
        ("ai_education_app_narrative_crowded",),
        ("ai_feature_cost_increase", "bookings_miss", "monetization_retreat", "paid_conversion_slowdown"),
        ("bookings_growth", "paid_conversion", "margin_stability", "fcf_conversion"),
        ("ai_cost", "bookings_miss", "monetization_retreat", "paid_conversion_slowdown"),
        "AI learning features are not enough; bookings, paid conversion, AI cost, margin, and FCF decide escalation.",
    ),
    Round104ScoreTarget(
        "EDTECH_AI_DISRUPTION",
        E2RArchetype.EDTECH_AI_DISRUPTION,
        Round10ThemePosture.REDTEAM_FIRST,
        Round104ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("ai_tutor", "ai_answer_engine", "homework_help_ai", "traffic_risk"),
        ("ai_defense_contract_or_productivity_needed",),
        ("normally_blocked_if_core_service_substituted",),
        ("ai_education_theme_crowded", "user_growth_before_monetization"),
        ("ai_substitutes_core_service", "traffic_decline", "subscriber_decline", "bookings_miss", "layoff", "strategic_review"),
        ("b2b_contract", "completion_rate", "student_roi", "fcf_conversion"),
        ("ai_substitution", "traffic_decline", "subscriber_decline", "bookings_miss", "cac_spike"),
        "AI education is a feature only if it supports outcomes; if it substitutes the core service, it is a RedTeam gate.",
        gate_only=True,
    ),
    Round104ScoreTarget(
        "ONLINE_EDUCATION_OPM_DISTRESS",
        E2RArchetype.ONLINE_EDUCATION_OPM_DISTRESS,
        Round10ThemePosture.REDTEAM_FIRST,
        Round104ScoreWeightDraft(10, 8, 4, 8, 5, 0, 5),
        ("online_degree_platform", "bootcamp_growth", "opm_revenue_share", "edtech_platform"),
        ("student_roi", "completion_rate", "partner_retention", "fcf_conversion", "debt_reduction"),
        ("repeat_contracts", "low_debt_stress", "regulatory_compliance", "fcf_conversion"),
        ("online_education_platform_premium", "growth_priced_before_roi"),
        ("chapter11", "high_leverage", "student_roi_failure", "regulatory_scrutiny", "partner_concentration_failure"),
        ("student_roi", "completion_rate", "partner_retention", "fcf_conversion"),
        ("debt", "student_roi", "regulatory_oversight", "partner_concentration", "chapter11"),
        "Online OPM platforms need student ROI, completion, partner retention, and debt checks before any rerating claim.",
    ),
    Round104ScoreTarget(
        "HOME_CHILD_EDUCATION",
        E2RArchetype.HOME_CHILD_EDUCATION,
        Round10ThemePosture.REDTEAM_FIRST,
        Round104ScoreWeightDraft(15, 11, 5, 10, 8, 0, 5),
        ("kids_product", "learning_material", "premium_childcare", "overseas_expansion"),
        ("repeat_subscription", "export_channel", "premium_mix", "inventory_control"),
        ("low_birthrate_offset", "recurring_revenue", "fcf_conversion"),
        ("premium_kids_theme_crowded",),
        ("low_birthrate", "tam_decline", "inventory_build", "regulatory_risk"),
        ("repeat_subscription", "export_channel", "low_birthrate_offset", "fcf_conversion"),
        ("birthrate_decline", "tam_shrink", "inventory", "policy_risk"),
        "Kids/home education faces low-birthrate TAM risk unless export or subscription economics offset it.",
    ),
    Round104ScoreTarget(
        "HOME_LIVING_APPLIANCE_RENTAL",
        E2RArchetype.HOME_LIVING_APPLIANCE_RENTAL,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(18, 16, 6, 12, 11, 2, 5),
        ("rental_accounts_growth", "new_product", "overseas_expansion"),
        ("rental_churn_stable", "filter_service_revenue", "care_service_revenue", "opm_fcf_improvement"),
        ("recurring_service_revenue_dominates", "hardware_cycle_less_important", "fcf_conversion"),
        ("rental_account_growth_crowded", "consumer_service_multiple_rerated"),
        ("replacement_demand_collapse", "dividend_suspension", "rental_churn_spike", "housing_weakness"),
        ("rental_churn_stable", "recurring_service_revenue", "opm_fcf_improvement", "overseas_margin"),
        ("replacement_cycle", "housing_turnover", "churn", "hardware_only", "dividend_suspension"),
        "Rental/care revenue can improve quality, but hardware replacement cycles and churn must be checked.",
    ),
    Round104ScoreTarget(
        "HOME_APPLIANCE_HARDWARE_CYCLE",
        E2RArchetype.HOME_APPLIANCE_HARDWARE_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(14, 10, 5, 8, 6, 0, 5),
        ("replacement_demand", "housing_cycle", "appliance_export"),
        ("sales_growth", "margin_stability", "fcf_guidance"),
        ("repeat_service_revenue", "housing_cycle_buffered", "fcf_conversion"),
        ("hardware_replacement_theme_crowded",),
        ("replacement_demand_collapse", "housing_turnover_weakness", "dividend_suspension", "guidance_cut", "debt_reduction_pressure"),
        ("repeat_service_revenue", "margin_stability", "fcf_conversion"),
        ("replacement_cycle", "housing_turnover", "dividend_suspension", "guidance_cut", "debt"),
        "Home-appliance hardware remains a replacement and housing-cycle story unless repeat service revenue changes the economics.",
    ),
    Round104ScoreTarget(
        "SERVICE_KIOSK_SELF_CHECKOUT",
        E2RArchetype.SERVICE_KIOSK_SELF_CHECKOUT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(15, 13, 7, 10, 8, 0, 5),
        ("labor_cost_increase", "unmanned_store", "self_checkout_rollout", "kiosk_installation"),
        ("installed_base", "maintenance_revenue", "payment_fee_revenue", "loss_prevention_effect"),
        ("recurring_service_revenue", "hardware_mix_declines", "customer_friction_low"),
        ("automation_theme_crowded", "installed_base_priced_before_service_revenue"),
        ("retailer_retreat", "theft_shrink", "customer_friction", "employee_workload", "one_off_hardware_sales"),
        ("maintenance_revenue", "payment_fee_revenue", "loss_prevention_effect", "recurring_service_revenue"),
        ("theft", "customer_friction", "retailer_retreat", "employee_workload", "one_off_hardware"),
        "Kiosk adoption needs service/fee economics; installation count alone is not productivity proof.",
    ),
    Round104ScoreTarget(
        "SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY",
        E2RArchetype.SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round104ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("local_self_checkout_regulation", "item_limit", "staffed_lane_requirement"),
        ("retailer_compliance_cost", "store_policy_change"),
        ("regulatory_risk_resolved",),
        ("self_checkout_adoption_priced_without_regulation",),
        ("item_limit", "staff_required_per_kiosk", "local_ordinance", "retailer_retreat"),
        ("regulation_resolved", "maintenance_revenue", "retailer_retention"),
        ("item_limit", "staff_required", "local_ordinance", "retailer_retreat"),
        "Local self-checkout rules are a RedTeam gate for kiosk economics, especially item limits and staffing requirements.",
        gate_only=True,
    ),
    Round104ScoreTarget(
        "CONSUMER_REGULATED_PRODUCT",
        E2RArchetype.CONSUMER_REGULATED_PRODUCT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(18, 15, 8, 12, 10, 0, 5),
        ("fda_approval", "dea_rescheduling", "regulated_product_license"),
        ("sales_authorization", "channel_access", "tax_effect", "repeat_consumption"),
        ("regulatory_stability", "repeat_revenue", "fcf_conversion"),
        ("regulatory_approval_rally_crowded", "policy_reversal_ignored"),
        ("approval_revoked", "sales_ban", "legal_conflict", "youth_usage_controversy", "public_health_backlash"),
        ("sales_authorization", "channel_access", "repeat_consumption", "regulatory_stability"),
        ("public_health", "social_backlash", "legal_conflict", "license_scope", "youth_usage"),
        "Regulated consumer products can rerate on approval, but scope and public-health risks stay high.",
    ),
    Round104ScoreTarget(
        "NICOTINE_ALTERNATIVE_REGULATED",
        E2RArchetype.NICOTINE_ALTERNATIVE_REGULATED,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(16, 13, 8, 10, 8, 0, 5),
        ("e_cigarette", "nicotine_pouch", "fda_enforcement_easing", "reduced_risk_product"),
        ("sales_authorization", "license_scope", "authorized_channel", "repeat_consumption"),
        ("regulatory_stability", "repeat_revenue", "public_health_risk_contained", "fcf_conversion"),
        ("nicotine_policy_relief_rally", "approval_scope_ignored"),
        ("youth_usage_risk", "flavored_product_restriction", "public_health_warning", "unauthorized_product_status", "enforcement_reversal"),
        ("sales_authorization", "license_scope", "authorized_channel", "repeat_consumption"),
        ("youth_usage", "public_health", "flavor_restriction", "unauthorized_status"),
        "Nicotine alternatives have repeat-consumption potential, but youth/public-health and authorization scope gates remain hard.",
    ),
    Round104ScoreTarget(
        "NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY",
        E2RArchetype.NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round104ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        ("nicotine_pouch_growth", "youth_usage_warning", "flavor_marketing"),
        ("age_verification", "nicotine_limit", "advertising_compliance"),
        ("public_health_risk_contained",),
        ("nicotine_repeat_consumption_priced_without_youth_risk",),
        ("youth_addiction_warning", "high_nicotine_content", "flavor_restriction", "advertising_ban", "influencer_marketing_risk"),
        ("age_verification", "authorization_scope", "public_health_risk_contained"),
        ("youth_addiction", "high_nicotine", "flavor", "advertising", "public_health"),
        "Nicotine pouch growth is capped until youth-addiction, flavor, advertising, and nicotine-content risks are controlled.",
        gate_only=True,
    ),
    Round104ScoreTarget(
        "CANNABIS_REGULATED_PRODUCT",
        E2RArchetype.CANNABIS_REGULATED_PRODUCT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(16, 14, 8, 11, 8, 0, 5),
        ("cannabis_rescheduling", "medical_cannabis_policy", "dea_registration", "state_license"),
        ("license_scope", "tax_effect", "sales_channel", "compliance_cost_visible"),
        ("regulatory_stability", "repeat_revenue", "tax_benefit_realized", "fcf_conversion"),
        ("cannabis_policy_relief_rally", "full_legalization_assumed"),
        ("state_federal_conflict", "dea_registration_failure", "legal_challenge", "public_health_backlash", "license_scope_limited"),
        ("license_scope", "sales_channel", "tax_effect", "regulatory_stability"),
        ("no_full_legalization", "dea_registration_required", "state_federal_conflict", "legal_challenge"),
        "Cannabis rescheduling is not full legalization; stage credit requires license scope, channel, tax effect, and FCF.",
    ),
    Round104ScoreTarget(
        "FOOD_INPUT_REGULATED_CYCLE",
        E2RArchetype.FOOD_INPUT_REGULATED_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round104ScoreWeightDraft(17, 11, 12, 8, 8, 0, 5),
        ("grain_input_price", "alcohol_or_food_input_regulation", "feed_or_soybean_cost"),
        ("price_pass_through", "regulated_margin", "cost_stabilization"),
        ("multi_period_spread", "stable_regulation", "fcf_conversion"),
        ("food_input_spread_crowded", "regulated_price_theme"),
        ("cost_spike", "price_control", "regulatory_margin_cap", "demand_fade"),
        ("price_pass_through", "regulated_margin", "cost_stabilization", "fcf_conversion"),
        ("cost", "price_control", "regulation", "commodity_cycle"),
        "Food inputs need price pass-through and regulation checks before any structural claim.",
    ),
    Round104ScoreTarget(
        "AGRI_DISEASE_EVENT_OVERLAY",
        E2RArchetype.AGRI_DISEASE_EVENT_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round104ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
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
    Round104ScoreTarget(
        "REGULATED_CONSUMER_APPROVAL_OVERLAY",
        E2RArchetype.REGULATED_CONSUMER_APPROVAL_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        Round104ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
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
    Round104ScoreTarget(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        Round104ScoreWeightDraft("cap", "cap", "cap", "cap", "cap", "cap", "+"),
        ("order_headline", "rental_account_headline", "regulatory_approval_headline", "unit_economics_claim"),
        ("detail_fetch_required", "source_detail_confidence_checked"),
        ("stage3_cap_until_unit_economics_or_scope_detail_verified",),
        ("headline_priced_before_detail",),
        ("contract_value_missing", "churn_missing", "cac_missing", "regulatory_scope_missing", "unit_economics_missing", "parser_confidence_low"),
        (),
        ("contract_value_missing", "churn_missing", "cac_missing", "regulatory_scope_missing", "unit_economics_missing", "parser_confidence_low"),
        "R12 caps Stage 3 until contract value, churn, CAC, recurring revenue, unit economics, regulatory scope, and parser confidence are verified.",
    ),
)


ROUND104_CASE_CANDIDATES: tuple[Round104CaseCandidate, ...] = (
    Round104CaseCandidate(
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
    Round104CaseCandidate(
        "deere_farm_equipment_demand_slowdown_case",
        "AGRI_MACHINERY_DEMAND_CYCLE",
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
        "agri_machinery_demand_cycle_4c_watch",
        "needs_price_backfill",
        ("Reuters Deere muted farm equipment demand",),
        "Precision agriculture can be promising while the machinery company is still capped by farm-income and financing cycles.",
    ),
    Round104CaseCandidate(
        "deere_right_to_repair_settlement_case",
        "RIGHT_TO_REPAIR_REGULATORY_OVERLAY",
        "DE",
        "Deere right-to-repair settlement",
        "US",
        "failed_rerating",
        date(2026, 4, 1),
        None,
        None,
        None,
        None,
        ("right_to_repair_flag", "repair_settlement_amount", "software_lock_in", "ftc_lawsuit_flag"),
        ("right_to_repair_lawsuit", "repair_monopoly_allegation", "settlement_cost", "ftc_lawsuit", "customer_backlash"),
        "agri_machinery_software_lockin_regulatory_watch",
        "needs_price_backfill",
        ("AP Deere right-to-repair settlement",),
        "Software-enabled equipment lock-in can become a RedTeam risk if regulation or lawsuits weaken the model.",
        (E2RArchetype.AGRI_MACHINERY_SOFTWARE_LOCKIN,),
    ),
    Round104CaseCandidate(
        "cnh_agri_machinery_demand_cycle_case",
        "AGRI_MACHINERY_DEMAND_CYCLE",
        "CNH",
        "CNH farm equipment demand cycle",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("farm_income_weakness", "crop_price_decline", "dealer_inventory_increase", "equipment_sales_decline"),
        ("farm_income_weakness", "crop_price_decline", "dealer_inventory_increase", "farmer_financing_cost"),
        "agri_machinery_demand_4c_watch",
        "needs_price_backfill",
        ("Reuters CNH profit forecast demand cycle",),
        "CNH-style demand misses show that farm-income, crop-price, financing, and dealer-inventory evidence can override precision-agriculture narratives.",
        (E2RArchetype.AGRI_MACHINERY_PRECISION_CYCLE,),
    ),
    Round104CaseCandidate(
        "bayer_crop_science_seed_license_case",
        "AGRI_INPUT_SEED_CROP_PROTECTION",
        "BAYN",
        "Bayer Crop Science seed licensing case",
        "DE",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("seed_licensing", "licensing_revenue", "crop_science_ebitda_improvement", "farmer_roi"),
        ("roundup_litigation", "crop_protection_litigation", "farmer_margin_pressure", "debt_burden"),
        "agri_input_licensed_ip_success_candidate",
        "needs_price_backfill",
        ("Reuters Bayer Crop Science EBITDA and seed licensing dispute",),
        "Seed/IP licensing can support Stage 2 research, while crop-protection litigation and farmer margin remain RedTeam fields.",
    ),
    Round104CaseCandidate(
        "nutrien_potash_demand_cycle_case",
        "FERTILIZER_INPUT_COST_CYCLE",
        "NTR",
        "Nutrien potash demand cycle",
        "CA",
        "cyclical_success",
        None,
        None,
        None,
        None,
        None,
        ("potash_sales_forecast_raise", "fertilizer_volume", "potash_demand", "application_rate"),
        ("crop_price_decline", "farmer_margin_pressure", "input_cost_spike", "demand_deferral"),
        "fertilizer_cycle_with_input_risk",
        "needs_price_backfill",
        ("Reuters Nutrien potash sales forecast raise",),
        "Potash demand can produce a strong cycle, but crop prices, farmer margin, and input-cost risk keep it Watch/Yellow-first.",
    ),
    Round104CaseCandidate(
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
    Round104CaseCandidate(
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
    Round104CaseCandidate(
        "bowery_vertical_farming_shutdown_case",
        "VERTICAL_FARMING_UNIT_ECONOMICS",
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
    Round104CaseCandidate(
        "appharvest_chapter11_case",
        "VERTICAL_FARMING_UNIT_ECONOMICS",
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
    Round104CaseCandidate(
        "duolingo_ai_strategy_bookings_miss_case",
        "EDTECH_AI_MONETIZATION_TRADEOFF",
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
        (E2RArchetype.EDUCATION_SPECIALTY_SERVICES, E2RArchetype.EDTECH_AI_DISRUPTION),
    ),
    Round104CaseCandidate(
        "chegg_ai_disruption_case",
        "EDTECH_AI_DISRUPTION",
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
        (E2RArchetype.EDUCATION_SPECIALTY_SERVICES,),
    ),
    Round104CaseCandidate(
        "2u_chapter11_case",
        "ONLINE_EDUCATION_OPM_DISTRESS",
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
    Round104CaseCandidate(
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
    Round104CaseCandidate(
        "whirlpool_dividend_suspension_case",
        "HOME_APPLIANCE_HARDWARE_CYCLE",
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
        (E2RArchetype.HOME_LIVING_APPLIANCE_RENTAL,),
    ),
    Round104CaseCandidate(
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
        (E2RArchetype.SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY,),
    ),
    Round104CaseCandidate(
        "santa_ana_self_checkout_regulation_case",
        "SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY",
        "LOCAL_SELF_CHECKOUT_POLICY",
        "Santa Ana self-checkout local regulation case",
        "US",
        "failed_rerating",
        None,
        None,
        None,
        None,
        None,
        ("local_self_checkout_regulation", "item_limit", "staffed_lane_requirement", "staff_required_per_kiosk"),
        ("item_limit", "staff_required_per_kiosk", "local_ordinance", "retailer_retreat"),
        "self_checkout_local_regulation_watch",
        "needs_price_backfill",
        ("Local self-checkout ordinance reference",),
        "Local self-checkout restrictions can cap kiosk productivity narratives unless retailer compliance economics are verified.",
        (E2RArchetype.SERVICE_KIOSK_SELF_CHECKOUT,),
    ),
    Round104CaseCandidate(
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
    Round104CaseCandidate(
        "fda_vape_enforcement_easing_case",
        "NICOTINE_ALTERNATIVE_REGULATED",
        "NICOTINE_POLICY_BASKET",
        "FDA unauthorized vape enforcement easing",
        "US",
        "event_premium",
        date(2026, 5, 8),
        None,
        None,
        date(2026, 5, 8),
        None,
        ("fda_enforcement_easing", "unauthorized_product_status", "nicotine_pouch_or_vape_policy"),
        ("unauthorized_product_status", "enforcement_reversal", "youth_usage_risk", "public_health_warning"),
        "nicotine_alternative_regulatory_watch",
        "needs_price_backfill",
        ("Reuters FDA unauthorized vape enforcement easing",),
        "Enforcement easing can route research, but it is not the same as durable authorization, channel access, and repeat FCF.",
        (E2RArchetype.REGULATED_CONSUMER_APPROVAL_OVERLAY,),
    ),
    Round104CaseCandidate(
        "who_nicotine_pouch_youth_warning_case",
        "NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY",
        "NICOTINE_PUBLIC_HEALTH",
        "WHO nicotine pouch youth warning",
        "GLOBAL",
        "failed_rerating",
        date(2026, 5, 15),
        None,
        None,
        None,
        None,
        ("public_health_warning", "youth_usage_risk", "nicotine_pouch_regulation"),
        ("youth_usage_risk", "public_health_warning", "flavored_product_restriction", "regulatory_backlash"),
        "nicotine_public_health_redteam",
        "needs_price_backfill",
        ("Reuters WHO nicotine pouch youth warning",),
        "Nicotine repeat consumption is not enough; youth usage and public-health warnings can cap or break the thesis.",
        (E2RArchetype.NICOTINE_ALTERNATIVE_REGULATED, E2RArchetype.REGULATED_CONSUMER_APPROVAL_OVERLAY),
    ),
    Round104CaseCandidate(
        "cannabis_schedule3_limited_case",
        "CANNABIS_REGULATED_PRODUCT",
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


ROUND104_PRICE_FIELDS: tuple[str, ...] = (
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
    "farm_income_improvement_flag",
    "equipment_sales_growth",
    "dealer_inventory",
    "dealer_inventory_increase_flag",
    "dealer_inventory_normalization_flag",
    "equipment_rental_instead_of_purchase_flag",
    "crop_price",
    "precision_agriculture_revenue",
    "autonomous_equipment_order",
    "software_attach_rate",
    "farmer_financing_cost",
    "tariff_exposure_flag",
    "right_to_repair_flag",
    "repair_settlement_amount",
    "repair_monopoly_allegation_flag",
    "customer_backlash_flag",
    "digital_tool_access_flag",
    "ftc_lawsuit_flag",
    "seed_licensing_revenue",
    "crop_science_ebitda_growth",
    "roundup_litigation_flag",
    "patent_expiry_flag",
    "crop_protection_litigation_flag",
    "farmer_margin_pressure_flag",
    "fertilizer_volume",
    "fertilizer_price",
    "application_rate",
    "potash_sales_forecast",
    "input_cost_spike_flag",
    "demand_deferral_flag",
    "vertical_farming_revenue",
    "vertical_farming_energy_cost",
    "capacity_utilization",
    "unit_economics_margin",
    "premium_pricing_success_flag",
    "yield_loss_flag",
    "chapter11_flag",
    "chapter7_flag",
    "shutdown_flag",
    "debt_burden_flag",
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
    "conditional_license_flag",
    "vaccine_order_value",
    "agri_ai_monitoring_contract",
    "farm_sensor_adoption",
    "farm_privacy_risk_flag",
    "data_quality_score",
    "repeat_subscription_flag",
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
    "ai_feature_cost",
    "ai_cost_control_flag",
    "monetization_retreat_flag",
    "paid_conversion_slowdown_flag",
    "ai_disruption_flag",
    "traffic_decline_flag",
    "subscriber_decline_flag",
    "layoff_flag",
    "bankruptcy_flag",
    "opm_model_flag",
    "partner_concentration_flag",
    "student_debt_risk_flag",
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
    "local_self_checkout_regulation_flag",
    "staffed_lane_requirement_flag",
    "staff_required_per_kiosk_flag",
    "local_ordinance_flag",
    "regulatory_approval_flag",
    "fda_approval_flag",
    "fda_enforcement_easing_flag",
    "dea_rescheduling_flag",
    "license_scope",
    "medical_cannabis_only_flag",
    "recreational_cannabis_benefit_flag",
    "dea_registration_required_flag",
    "state_federal_conflict_flag",
    "youth_usage_risk_flag",
    "public_health_warning_flag",
    "legal_conflict_flag",
    "compliance_cost",
    "sales_channel_authorized_flag",
    "age_verification_flag",
    "nicotine_limit",
    "advertising_compliance_flag",
    "high_nicotine_content_flag",
    "flavor_restriction_flag",
    "advertising_ban_flag",
    "influencer_marketing_risk_flag",
    "contract_value_missing_flag",
    "churn_missing_flag",
    "cac_missing_flag",
    "regulatory_scope_missing_flag",
    "unit_economics_missing_flag",
    "parser_confidence",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def target_for(target_id: str) -> Round104ScoreTarget | None:
    for target in ROUND104_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round104_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND104_CASE_CANDIDATES:
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
                f"Round104 R12 Loop-5 case for {candidate.target_id}; "
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


def round104_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND104_SCORE_TARGETS:
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


def round104_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND104_CASE_CANDIDATES:
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


def round104_stage_date_rows() -> tuple[dict[str, str], ...]:
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
        for target in ROUND104_SCORE_TARGETS
    )


def round104_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round104_backfill": "true"} for field in ROUND104_PRICE_FIELDS)


def round104_summary() -> dict[str, int | bool]:
    records = round104_case_records()
    return {
        "target_count": len(ROUND104_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND104_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND104_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND104_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND104_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round104_r12_loop5_reports(
    *,
    output_directory: str | Path = ROUND104_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND104_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND104_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round104_r12_loop5_agri_life_misc_summary.md",
        "case_matrix": output / "round104_r12_loop5_case_matrix.csv",
        "stage_date_plan": output / "round104_r12_loop5_stage_date_plan.csv",
        "green_guardrails": output / "round104_r12_loop5_green_guardrails.md",
        "unit_economics_caps": output / "round104_r12_loop5_unit_economics_caps.md",
        "price_validation_plan": output / "round104_r12_loop5_price_validation_plan.md",
        "price_fields": output / "round104_r12_loop5_price_fields.csv",
    }
    _write_case_jsonl(round104_case_records(), cases)
    _write_rows(round104_score_profile_rows(), score_profiles)
    _write_rows(round104_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round104_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round104_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round104_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round104_green_guardrail_markdown(), encoding="utf-8")
    paths["unit_economics_caps"].write_text(render_round104_unit_economics_cap_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round104_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round104_summary_markdown() -> str:
    summary = round104_summary()
    lines = [
        "# Round-104 R12 Loop-5 Agriculture / Life Services / Misc Summary",
        "",
        f"- source_round: `{ROUND104_SOURCE_ROUND_PATH}`",
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
        "- R12 Loop-5 separates recurring FCF from disease, weather, policy, AI, hardware, and regulation headlines.",
        "- Example: smart farming news is Stage 1 until actual orders, unit economics, energy cost, and FCF are visible.",
        "- Example: education apps need bookings, paid conversion, CAC, and monetization, not user growth alone.",
        "- Example: rental appliances can improve quality only if recurring care revenue and churn data beat the hardware cycle.",
    ]
    return "\n".join(lines) + "\n"


def render_round104_green_guardrail_markdown() -> str:
    lines = [
        "# Round-104 R12 Loop-5 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND104_SCORE_TARGETS:
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
            "- Do not apply these R12 Loop-5 v5 weights to production scoring yet.",
            "- Do not treat essential demand, policy support, weather, disease, grain prices, education users, rental accounts, or FDA/DEA headlines as Green evidence by itself.",
            "- Do not invent unit economics, government orders, completion rates, CAC, churn, regulatory scope, software attach rate, or price-path fields.",
            "- Do not lower Stage 3-Green for R12 recall. Green requires repeat contracts, repeat revenue, unit economics, regulatory stability, and FCF conversion.",
            "- Treat Chapter 11, AI substitution, bookings misses, dividend suspension, retailer retreat, theft/shrink, public-health reversal, commodity normalization, and right-to-repair risk as RedTeam evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round104_unit_economics_cap_markdown() -> str:
    lines = [
        "# Round-104 R12 Loop-5 Unit-Economics / Cycle Caps",
        "",
        "- `SMART_FARM_AGRI_TECH`: technology and policy are Stage 1; orders, energy cost, utilization, and FCF decide escalation.",
        "- `VERTICAL_FARMING_UNIT_ECONOMICS`: indoor-farm stories need energy cost, yield, premium pricing, and FCF; shutdown or Chapter 11 is hard RedTeam.",
        "- `AGRI_MACHINERY_PRECISION_CYCLE`: autonomous equipment still depends on farm income, financing cost, right-to-repair risk, and replacement cycles.",
        "- `AGRI_MACHINERY_DEMAND_CYCLE`: equipment demand must pass farm-income, crop-price, financing-cost, and dealer-inventory checks before technology credit matters.",
        "- `AGRI_MACHINERY_SOFTWARE_LOCKIN`: software attach is useful only while right-to-repair, dealer monopoly, and FTC risk are controlled.",
        "- `RIGHT_TO_REPAIR_REGULATORY_OVERLAY`: repair monopoly, settlement, and FTC risk gate software lock-in confidence.",
        "- `AGRI_INPUT_SEED_CROP_PROTECTION`: seed/IP licensing can be durable, but crop-protection litigation, patent expiry, regulation, and farmer margin cap Green.",
        "- `FERTILIZER_INPUT_COST_CYCLE`: potash, phosphate, and nitrogen cycles need crop price, farmer margin, input cost, volume, and FCF checks.",
        "- `AGRI_LIVESTOCK_FOOD_COMMODITY`: price spikes can be cyclical success, but disease and price normalization cap Green.",
        "- `ANIMAL_HEALTH_BIOSECURITY`: conditional approval and stockpile can create Stage 2, but repeated use decides durability.",
        "- `AGRI_DISEASE_AI_MONITORING`: AI monitoring needs farm adoption contracts, data quality, privacy compliance, and repeat subscriptions.",
        "- `EDUCATION_SPECIALTY_SERVICES`: AI education can work only when contracts, completion, retention, CAC, and margin are visible.",
        "- `EDTECH_AI_MONETIZATION_TRADEOFF`: AI features must lift bookings and paid conversion without damaging margin and FCF.",
        "- `EDTECH_AI_DISRUPTION`: Chegg-style AI substitution is a gate, not a positive education score.",
        "- `ONLINE_EDUCATION_OPM_DISTRESS`: OPM models need debt, student ROI, completion, partner concentration, and regulation checks.",
        "- `HOME_LIVING_APPLIANCE_RENTAL`: recurring rental/care revenue must dominate hardware replacement-cycle risk.",
        "- `HOME_APPLIANCE_HARDWARE_CYCLE`: hardware appliance stories are capped by replacement demand, housing turnover, dividend risk, guidance, and debt.",
        "- `SERVICE_KIOSK_SELF_CHECKOUT`: installed base must convert into maintenance, payment fee, or loss-prevention economics.",
        "- `SELF_CHECKOUT_LOCAL_REGULATION_OVERLAY`: item limits, staffed-lane rules, and local ordinances gate kiosk adoption narratives.",
        "- `CONSUMER_REGULATED_PRODUCT`: approval scope, channel access, public-health risk, and legal conflict must be checked.",
        "- `NICOTINE_ALTERNATIVE_REGULATED`: repeat consumption does not bypass youth usage, flavor, and public-health gates.",
        "- `NICOTINE_POUCH_YOUTH_SAFETY_OVERLAY`: nicotine-pouch growth is capped by youth addiction, nicotine content, flavor, advertising, and influencer risk.",
        "- `CANNABIS_REGULATED_PRODUCT`: rescheduling is not full legalization; license scope, tax effect, and state/federal conflict decide credit.",
        "- `DISCLOSURE_CONFIDENCE_CAP`: headlines cannot create Stage 3 until contract value, churn, CAC, unit economics, regulatory scope, and parser confidence are verified.",
        "",
        "Simple example: a vertical-farming company may sound structural because food is essential. If energy cost and unit economics are negative, it is a 4C-style counterexample rather than Stage 3-Green.",
    ]
    return "\n".join(lines) + "\n"


def render_round104_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-104 R12 Loop-5 Price Validation Plan",
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
    for row in round104_case_candidate_rows():
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
            "- `agri_machinery_demand_4c`: farm income, crop price, financing cost, and dealer inventory break the equipment-cycle case.",
            "- `agri_machinery_software_lockin_regulatory_watch`: software attach exists, but right-to-repair and dealer-monopoly risk must be priced.",
            "- `agri_input_licensed_ip_success`: seed/IP licensing and crop-science EBITDA can help only if litigation and farmer margin risk are controlled.",
            "- `fertilizer_cycle_with_input_risk`: potash or fertilizer demand is cycle credit, not Green, until farmer margin and FCF prove durability.",
            "- `animal_health_event_to_contract`: disease event turns into vaccine approval, stockpile, and repeated use.",
            "- `livestock_cyclical_success`: price spike generated profit, but structural durability is weak.",
            "- `edtech_ai_monetization_failed`: AI education features hurt the thesis if bookings, paid conversion, monetization, or margin breaks.",
            "- `education_ai_disruption_4c`: AI replaces the core service or weakens traffic, subscribers, bookings, and revenue.",
            "- `online_education_opm_hard_4c`: debt, student ROI, partner concentration, or bankruptcy breaks online OPM.",
            "- `rental_recurring_success`: rental accounts, churn, care-service revenue, and FCF are confirmed.",
            "- `kiosk_operational_failure`: self-checkout or kiosk rollout retreats because theft, customer friction, or workload rises.",
            "- `self_checkout_local_regulation_watch`: item limits, staff requirements, or local ordinances cap the kiosk productivity story.",
            "- `regulated_consumer_approval_stage2`: FDA/DEA approval can create Stage 2, but scope and public-health gates remain.",
            "- `nicotine_alternative_regulatory_watch`: enforcement easing or nicotine-pouch growth still needs authorization scope and youth-risk checks.",
            "- `nicotine_pouch_youth_safety_gate`: youth addiction, high nicotine content, flavor, advertising, or influencer risk blocks positive nicotine-pouch scoring.",
            "- `disclosure_confidence_capped`: R12 headlines stay capped until unit economics, regulatory scope, and parser confidence are verified.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round104CaseCandidate) -> str:
    if candidate.case_type == "success_candidate" and (
        "recurring" in candidate.alignment_hint
        or "contract" in candidate.alignment_hint
        or "approval" in candidate.alignment_hint
        or "candidate" in candidate.alignment_hint
        or "success" in candidate.alignment_hint
        or "licensed" in candidate.alignment_hint
    ):
        return "aligned"
    if candidate.case_type == "cyclical_success":
        return "aligned"
    if candidate.case_type in {"event_premium", "one_off", "4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type in {"failed_rerating", "4c_thesis_break"}:
        return "false_positive_score"
    return "unknown"


def _rerating_result(candidate: Round104CaseCandidate) -> str:
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
    "ROUND104_CASE_CANDIDATES",
    "ROUND104_DEFAULT_CASES_PATH",
    "ROUND104_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND104_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND104_PRICE_FIELDS",
    "ROUND104_SCORE_TARGETS",
    "ROUND104_SOURCE_ROUND_PATH",
    "Round104CaseCandidate",
    "Round104ScoreTarget",
    "Round104ScoreWeightDraft",
    "render_round104_green_guardrail_markdown",
    "render_round104_price_validation_plan_markdown",
    "render_round104_summary_markdown",
    "render_round104_unit_economics_cap_markdown",
    "round104_case_candidate_rows",
    "round104_case_records",
    "round104_price_field_rows",
    "round104_score_profile_rows",
    "round104_stage_date_rows",
    "round104_summary",
    "target_for",
    "write_round104_r12_loop5_reports",
]
