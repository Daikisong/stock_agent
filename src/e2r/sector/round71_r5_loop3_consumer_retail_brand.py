"""Round-71 R5 Loop-3 consumer, retail, and brand calibration pack.

Round 71 tightens R5 by separating recurring export consumption from viral
events, channel-entry headlines, channel stuffing, trust/regulation breaks, and
hardware cycles. It is calibration/report material only: production feature
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


ROUND71_SOURCE_ROUND_PATH = "docs/round/round_71.md"
ROUND71_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round71_r5_loop3_consumer_retail_brand"
ROUND71_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r5_loop3_round71.jsonl"
ROUND71_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round71_r5_loop3_v3.csv"


@dataclass(frozen=True)
class Round71ScoreWeightDraft:
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
class Round71ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round71ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop3_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.CONSUMER_RETAIL_BRAND

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round71CaseCandidate:
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


def _w(
    eps_fcf: int | str,
    visibility: int | str,
    bottleneck: int | str,
    mispricing: int | str,
    valuation: int | str,
    capital: int | str = 0,
    confidence: int | str = 5,
) -> Round71ScoreWeightDraft:
    return Round71ScoreWeightDraft(eps_fcf, visibility, bottleneck, mispricing, valuation, capital, confidence)


def _target(
    target_id: str,
    archetype: E2RArchetype,
    posture: Round10ThemePosture,
    weight: Round71ScoreWeightDraft,
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
) -> Round71ScoreTarget:
    return Round71ScoreTarget(
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


ROUND71_SCORE_TARGETS: tuple[Round71ScoreTarget, ...] = (
    _target(
        "EXPORT_RECURRING_CONSUMER",
        E2RArchetype.EXPORT_RECURRING_CONSUMER,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(22, 23, 12, 16, 13),
        stage1=("k_food_export_growth", "ramen_viral", "capa_expansion", "overseas_channel_news"),
        stage2=("asp_change", "us_europe_shipments", "op_revision_1q", "eps_revision_1q"),
        stage3=("repeat_orders", "channel_sell_through", "opm_improvement", "fy1_fy2_eps_revision", "inventory_stable"),
        stage4b=("k_food_rerating_crowded", "target_price_revision_crowded", "capacity_expansion_priced"),
        stage4c=("recall_flag", "country_sales_ban", "foreign_inventory_growth", "channel_stuffing", "single_product_demand_fatigue"),
        green=("export_growth", "recurring_demand", "channel_sell_through", "reorder_signal", "opm_improvement", "eps_revision"),
        red=("single_product_dependency", "recall_flag", "foreign_inventory_growth", "channel_stuffing"),
        penalties=("single_product", "recall", "foreign_inventory", "channel_stuffing"),
        note="K-food Green stays possible, but export, ASP, OPM, reorder, inventory, and safety checks must align.",
    ),
    _target(
        "K_FOOD_SINGLE_HERO_PRODUCT",
        E2RArchetype.K_FOOD_SINGLE_HERO_PRODUCT,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(23, 21, 12, 16, 12),
        stage1=("hero_product_viral", "spicy_challenge", "export_growth", "single_sku_awareness"),
        stage2=("asp_change", "sku_expansion", "capa_expansion", "op_eps_revision"),
        stage3=("multi_sku_portfolio", "multi_country_sell_through", "repeat_purchase", "opm_improvement"),
        stage4b=("hero_product_narrative_overheated", "single_product_story_crowded"),
        stage4c=("country_recall", "food_safety_issue", "single_product_demand_fatigue", "foreign_inventory_growth"),
        green=("sku_expansion", "multi_country_sell_through", "repeat_purchase", "opm_improvement"),
        red=("single_product_revenue_ratio_high", "recall_flag", "viral_challenge_safety", "foreign_inventory_growth"),
        penalties=("hero_product_dependency", "recall", "viral_safety", "foreign_inventory"),
        note="Hero products can create Stage 2, but Stage 3 needs repeat portfolio evidence and safety guardrails.",
    ),
    _target(
        "K_BEAUTY_EXPORT_DISTRIBUTION",
        E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(22, 23, 12, 16, 13),
        stage1=("us_japan_europe_export_growth", "k_beauty_viral", "brand_awareness", "ecommerce_sales_growth"),
        stage2=("sephora_ulta_target_costco_channel", "offline_channel_entry", "online_sales_growth", "op_eps_revision"),
        stage3=("sell_through", "reorder_signal", "opm_fcf_improvement", "china_dependency_down", "inventory_receivables_stable"),
        stage4b=("k_beauty_group_overheated", "channel_entry_priced", "indie_brand_valuation_surge"),
        stage4c=("tariff_flag", "import_review", "offline_sell_through_failure", "inventory_growth", "receivables_growth", "china_channel_slowdown"),
        green=("export_growth", "offline_channel_sell_through", "reorder_signal", "opm_roe_improvement", "inventory_receivables_stable"),
        red=("tariff", "china_dependency", "sell_through_failure", "inventory_growth", "receivables_growth"),
        penalties=("tariff", "sell_through", "inventory", "receivables", "china_slowdown"),
        note="K-beauty Green needs offline sell-through and repeat orders, not TikTok or channel entry alone.",
    ),
    _target(
        "BEAUTY_DEVICE_EXPORT",
        E2RArchetype.BEAUTY_DEVICE_EXPORT,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(23, 22, 14, 16, 11),
        stage1=("beauty_device_viral", "tiktok_sales", "influencer_endorsement", "device_awareness"),
        stage2=("device_unit_sales", "amazon_tiktok_shop_sales", "offline_channel_entry", "overseas_sales_ratio"),
        stage3=("device_asp_stable", "repeat_skincare_consumables", "device_margin", "opm_improvement"),
        stage4b=("beauty_device_narrative_overheated", "share_price_multiple_expansion", "celebrity_endorsement_crowded"),
        stage4c=("device_competition", "safety_regulatory_issue", "tariff", "hero_product_fatigue"),
        green=("device_unit_sales", "device_asp", "device_margin", "repeat_consumables", "opm_improvement"),
        red=("device_competition", "safety_regulatory_issue", "tariff", "hero_product_dependency"),
        penalties=("4b_crowding", "device_competition", "regulation", "tariff"),
        note="Beauty devices can be strong, but device ASP, unit sales, safety, and 4B risk must be checked.",
    ),
    _target(
        "BEAUTY_OEM_ODM_SUPPLYCHAIN",
        E2RArchetype.BEAUTY_OEM_ODM_SUPPLYCHAIN,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(22, 22, 12, 15, 12),
        stage1=("global_k_beauty_order_growth", "brand_customer_growth", "production_utilization"),
        stage2=("customer_diversification", "repeat_orders", "capacity_utilization", "opm_improvement"),
        stage3=("overseas_customer_diversification", "repeat_orders", "eps_fcf_bodyweight_change", "receivables_stable"),
        stage4b=("beauty_supply_chain_premium_crowded",),
        stage4c=("customer_sell_through_slowdown", "inventory_growth", "receivables_growth", "customer_concentration"),
        green=("customer_diversification", "repeat_orders", "capacity_utilization", "opm_improvement", "receivables_stable"),
        red=("inventory_growth", "receivables_growth", "customer_concentration", "sell_through_failure"),
        penalties=("customer_diversification", "inventory", "receivables", "brand_sell_through"),
        note="Beauty OEM/ODM can be Green-capable, but customer inventory and receivables are hard checks.",
    ),
    _target(
        "RETAIL_CONVENIENCE_OFFLINE",
        E2RArchetype.RETAIL_CONVENIENCE_OFFLINE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 16, 5, 13, 14, 3),
        stage1=("same_store_sales_growth", "pb_mix", "store_count", "overseas_store"),
        stage2=("store_profitability", "pb_mix_ratio", "opm_improvement", "fcf_stability"),
        stage3=("same_store_sales", "store_profitability", "pb_mix", "fcf_stability"),
        stage4b=("store_count_story_crowded", "defensive_retail_premium_full"),
        stage4c=("same_store_sales_slowdown", "rent_wage_pressure", "store_density_competition"),
        green=("same_store_sales", "pb_mix", "opm_improvement", "fcf_stability"),
        red=("store_count_only", "rent_pressure", "wage_pressure", "store_density"),
        penalties=("sssg", "pb_mix", "store_profitability", "rent_wage"),
        note="Convenience retail is Watch-to-Green only when store productivity drives OPM and FCF.",
    ),
    _target(
        "RETAIL_ECOMMERCE_LOGISTICS",
        E2RArchetype.RETAIL_ECOMMERCE_LOGISTICS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(16, 14, 5, 11, 10, 2),
        stage1=("gmv_growth", "logistics_network_expansion", "customer_count_growth"),
        stage2=("logistics_cost_ratio_down", "opm_improvement", "fcf_improvement", "gross_margin_quality"),
        stage3=("repeat_customers", "cost_leverage", "low_regulatory_risk", "low_data_security_risk"),
        stage4b=("scale_narrative_crowded", "fcf_ignored", "trust_risk_ignored"),
        stage4c=("data_breach", "supplier_regulation", "payment_delay", "logistics_cost_increase", "fcf_deterioration"),
        green=("repeat_customer_base", "logistics_efficiency", "fcf_improvement", "trust_and_regulation_clean"),
        red=("data_breach", "supplier_pressure", "payment_delay", "trust_damage", "regulatory_investigation"),
        penalties=("data_security", "supplier_regulation", "logistics_cost", "fcf", "margin_quality"),
        note="E-commerce scale is not Green evidence unless unit economics, FCF, security, and supplier regulation are clean.",
    ),
    _target(
        "ECOMMERCE_FRESH_LOGISTICS",
        E2RArchetype.ECOMMERCE_FRESH_LOGISTICS,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(16, 13, 6, 11, 9, 1),
        stage1=("fresh_food_delivery_growth", "cold_chain_expansion", "repeat_order_growth", "ipo_expectation"),
        stage2=("unit_economics_improvement", "waste_rate_control", "delivery_cost_control", "op_turnaround"),
        stage3=("repeat_order", "cold_chain_efficiency", "op_fcf_turnaround", "low_waste_rate"),
        stage4b=("fresh_logistics_growth_story_crowded", "listing_expectation_premium"),
        stage4c=("delivery_cost_increase", "waste_rate_spike", "delayed_profitability", "cash_burn"),
        green=("unit_economics", "repeat_orders", "waste_rate_control", "fcf_path"),
        red=("cash_burn", "waste_rate", "delivery_cost", "profitability_delay"),
        penalties=("waste_rate", "delivery_cost", "cash_burn"),
        note="Fresh e-commerce must prove unit economics and waste control; GMV or listing hopes are Stage 1 only.",
    ),
    _target(
        "APPAREL_FAST_FASHION_BRAND_OEM",
        E2RArchetype.APPAREL_FAST_FASHION_BRAND_OEM,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(16, 14, 8, 12, 9),
        stage1=("brand_momentum", "fast_fashion_growth", "oem_order_growth", "overseas_channel"),
        stage2=("inventory_turnover", "discount_rate_control", "order_visibility", "opm_improvement"),
        stage3=("repeat_orders", "inventory_turnover", "brand_pricing_power", "fcf_improvement"),
        stage4b=("fashion_brand_hype_crowded", "fast_fashion_growth_priced"),
        stage4c=("ip_litigation", "product_safety_regulation", "supplier_exclusivity_dispute", "inventory_markdown", "customs_scrutiny"),
        green=("order_visibility", "inventory_turnover", "discount_rate_control", "opm_improvement"),
        red=("ip_litigation", "product_safety", "supplier_exclusivity", "inventory_markdown", "customs_scrutiny"),
        penalties=("inventory", "discount", "ip_litigation", "product_safety", "tariff"),
        note="Apparel and fast fashion are Watch/Red because IP, safety, tariff, and inventory can break the thesis.",
    ),
    _target(
        "HOME_LIVING_APPLIANCE_RENTAL",
        E2RArchetype.HOME_LIVING_APPLIANCE_RENTAL,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 16, 6, 12, 11, 2),
        stage1=("rental_accounts_growth", "overseas_accounts_growth", "new_product_launch"),
        stage2=("rental_churn_stable", "filter_service_revenue", "recurring_service_revenue_ratio", "opm_fcf_improvement"),
        stage3=("recurring_revenue_over_hardware_cycle", "low_churn", "service_margin", "fcf_improvement"),
        stage4b=("rental_account_growth_crowded",),
        stage4c=("replacement_demand_slowdown", "hardware_sales_ratio_high", "housing_cycle_down", "dividend_suspension"),
        green=("rental_accounts", "churn_stable", "recurring_service_revenue", "fcf_improvement"),
        red=("hardware_cycle", "housing_cycle", "consumer_sentiment", "dividend_suspension", "churn_rise"),
        penalties=("churn", "overseas_margin", "hardware_cycle", "quality_recall"),
        note="Home appliance Green needs rental/service recurring economics, not hardware replacement sales.",
    ),
    _target(
        "HOME_CHILD_EDUCATION",
        E2RArchetype.HOME_CHILD_EDUCATION,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(15, 11, 5, 10, 8),
        stage1=("kids_product_growth", "education_or_childcare_theme", "household_product_news"),
        stage2=("recurring_demand", "channel_expansion", "opm_improvement"),
        stage3=("subscription_or_repeat_purchase", "policy_risk_low", "fcf_path"),
        stage4b=("kids_theme_crowded",),
        stage4c=("low_birth_rate_tam_decline", "policy_regulation", "one_off_product_cycle", "inventory_growth"),
        green=("recurring_demand", "channel_expansion", "opm_improvement"),
        red=("low_birth_rate", "tam_decline", "policy_regulation", "inventory_growth"),
        penalties=("birth_rate", "tam", "policy", "inventory"),
        note="Kids/home education is RedTeam-first because demographics and TAM can cap the rerating.",
    ),
    _target(
        "CONSUMER_REGULATED_PRODUCT",
        E2RArchetype.CONSUMER_REGULATED_PRODUCT,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 14, 8, 12, 10),
        stage1=("regulated_consumer_product_approval", "new_market_access", "policy_change"),
        stage2=("legal_revenue", "distribution_approval", "margin_visibility"),
        stage3=("regulated_market_open", "repeat_revenue", "low_social_backlash"),
        stage4b=("regulated_product_theme_crowded",),
        stage4c=("license_reversal", "social_backlash", "product_safety_issue", "regulatory_ban"),
        green=("legal_revenue", "approval", "repeat_revenue", "margin_visibility"),
        red=("regulatory_ban", "social_backlash", "product_safety_issue"),
        penalties=("approval", "public_health", "regulatory_ban"),
        note="Regulated consumer products stay Watch until approval becomes legal recurring revenue.",
    ),
    _target(
        "FOOD_SAFETY_RECALL_OVERLAY",
        E2RArchetype.FOOD_SAFETY_RECALL_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("recall", "country_specific_sales_ban", "food_safety_issue", "capsaicin_or_additive_risk"),
        stage2=("risk_event_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("recall_flag", "country_sales_ban", "food_safety_flag", "single_product_concentration", "viral_challenge_safety_issue"),
        green=(),
        red=("recall_flag", "food_safety_flag", "country_sales_ban", "single_product_dependency"),
        penalties=("food_safety", "recall", "country_ban"),
        note="Food safety is a RedTeam overlay, not a positive score bucket.",
        gate_only=True,
    ),
    _target(
        "DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY",
        E2RArchetype.DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("data_breach", "supplier_pressure", "payment_delay", "retailer_law_violation"),
        stage2=("risk_event_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("data_breach_flag", "affected_customer_count", "customer_trust_damage", "regulatory_investigation", "payment_delay", "supplier_regulation"),
        green=(),
        red=("data_breach", "supplier_pressure", "payment_delay", "regulatory_investigation", "gross_margin_quality_risk"),
        penalties=("data_security", "supplier_regulation", "payment_delay", "margin_quality"),
        note="Data breach and supplier regulation are RedTeam overlays for e-commerce and marketplace models.",
        gate_only=True,
    ),
    _target(
        "CHANNEL_STUFFING_INVENTORY_OVERLAY",
        E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("shipment_growth", "channel_entry", "inventory_growth", "sell_through_unverified"),
        stage2=("shipment_sell_through_gap_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("channel_stuffing", "inventory_growth", "receivables_growth", "sell_through_failure", "reorder_absent"),
        green=(),
        red=("channel_stuffing", "inventory_growth", "receivables_growth", "sell_through_failure", "reorder_absent"),
        penalties=("shipment_vs_sell_through", "inventory", "receivables", "reorder"),
        note="Shipment and channel entry must be separated from sell-through and reorder.",
        gate_only=True,
    ),
    _target(
        "TARIFF_IMPORT_REGULATION_OVERLAY",
        E2RArchetype.TARIFF_IMPORT_REGULATION_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("tariff", "de_minimis_change", "import_review", "customs_scrutiny"),
        stage2=("tariff_import_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("tariff_flag", "import_delay", "fda_import_review", "gross_margin_buffer_weak", "price_increase_failed"),
        green=(),
        red=("tariff", "de_minimis_change", "import_review", "customs_scrutiny", "margin_buffer_weak"),
        penalties=("tariff", "import_review", "de_minimis", "gross_margin_buffer"),
        note="Tariff/import regulation is a RedTeam gate for K-beauty, fast fashion, and imported consumer products.",
        gate_only=True,
    ),
)


ROUND71_CASE_CANDIDATES: tuple[Round71CaseCandidate, ...] = (
    Round71CaseCandidate(
        "samyang_buldak_export_rerating_case",
        "EXPORT_RECURRING_CONSUMER",
        "003230",
        "삼양식품 Buldak 수출 리레이팅",
        "KR",
        "success_candidate",
        None,
        date(2024, 6, 14),
        None,
        date(2024, 6, 14),
        None,
        ("export_sales_growth", "us_europe_shipments", "asp_change", "capa_expansion", "op_revision_84pct", "target_price_revision_26pct", "share_price_plus_5_7pct"),
        ("single_product_dependency", "foreign_inventory_check_needed", "recall_overlay_required", "viral_challenge_safety_risk"),
        "export_recurring_aligned_candidate",
        "needs_price_backfill",
        ("round_71.md MarketWatch Samyang Buldak target revision",),
        "Export, ASP, CAPA, OP revision, and event-day price align, but single-product and recall overlays remain required.",
        (E2RArchetype.K_FOOD_SINGLE_HERO_PRODUCT, E2RArchetype.FOOD_SAFETY_RECALL_OVERLAY),
    ),
    Round71CaseCandidate(
        "samyang_buldak_denmark_recall_case",
        "FOOD_SAFETY_RECALL_OVERLAY",
        "003230_RECALL",
        "삼양식품 Buldak 덴마크 리콜",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 6, 12),
        ("buldak_brand", "single_product_concentration"),
        ("recall_flag", "country_sales_ban", "capsaicin_or_additive_risk", "viral_challenge_safety_issue"),
        "food_safety_regulatory_4c_watch",
        "needs_price_backfill",
        ("round_71.md AP Samyang Denmark recall",),
        "A successful K-food candidate still needs country-level recall and safety overlays.",
        (E2RArchetype.EXPORT_RECURRING_CONSUMER, E2RArchetype.K_FOOD_SINGLE_HERO_PRODUCT),
    ),
    Round71CaseCandidate(
        "kbeauty_us_export_overtake_france_case",
        "K_BEAUTY_EXPORT_DISTRIBUTION",
        "KBEAUTY_US_REF",
        "K뷰티 미국 수출 프랑스 추월",
        "KR",
        "success_candidate",
        None,
        date(2025, 6, 5),
        None,
        date(2025, 6, 5),
        None,
        ("us_export_overtake_france", "us_ecommerce_growth_71pct", "offline_channel_entry", "sephora_ulta_target_costco_channel", "brand_diversification"),
        ("tariff_flag", "china_sales_change", "sell_through_unverified", "brand_saturation"),
        "kbeauty_structural_success_candidate",
        "missing_direct_symbol_mapping",
        ("round_71.md Reuters K-beauty US export",),
        "K-beauty export growth and channel entry route research, but sell-through and reorder are required before Green.",
        (E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY, E2RArchetype.TARIFF_IMPORT_REGULATION_OVERLAY),
    ),
    Round71CaseCandidate(
        "kbeauty_us_tariff_risk_case",
        "TARIFF_IMPORT_REGULATION_OVERLAY",
        "KBEAUTY_TARIFF_REF",
        "K뷰티 미국 관세·수입규제 리스크",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("k_beauty_export_growth", "us_import_1_7b", "us_channel_entry"),
        ("tariff_flag", "tariff_rate_25pct_possible", "import_delay", "fda_import_review", "gross_margin_buffer_weak"),
        "kbeauty_tariff_4c_watch",
        "needs_exact_stage_date_backfill",
        ("round_71.md AP K-beauty US tariff risk",),
        "Tariff/import regulation can damage channel margin; month-level source marker needs exact date backfill.",
        (E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,),
    ),
    Round71CaseCandidate(
        "apr_medicube_beauty_device_case",
        "BEAUTY_DEVICE_EXPORT",
        "278470",
        "APR / Medicube beauty device",
        "KR",
        "4b_watch",
        None,
        date(2025, 10, 20),
        None,
        date(2025, 10, 20),
        None,
        ("share_price_4x", "market_value_6b", "overseas_sales_ratio_80pct", "us_sales_exceeds_korea", "beauty_device_revenue_share"),
        ("valuation_overheat", "tariff_flag", "device_competition", "hero_product_dependency", "regulatory_risk"),
        "beauty_device_aligned_but_4b",
        "needs_price_backfill",
        ("round_71.md FT APR beauty device",),
        "Beauty device export can be structurally strong, but 4x price move and valuation expansion require 4B-watch.",
        (E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,),
    ),
    Round71CaseCandidate(
        "medicube_ulta_tiktok_omnichannel_case",
        "BEAUTY_DEVICE_EXPORT",
        "MEDICUBE_REF",
        "Medicube Ulta / TikTok omnichannel",
        "KR",
        "success_candidate",
        None,
        date(2026, 2, 13),
        None,
        None,
        None,
        ("ulta_1400_store_entry", "tiktok_shop_sales_102_9m", "prime_day_sales_22m", "creator_network_34000", "omnichannel_sell_through"),
        ("publisher_profile_bias", "price_backfill_needed", "sell_through_quality_check_needed", "channel_stuffing_check_needed"),
        "omnichannel_sell_through_candidate",
        "missing_direct_symbol_mapping",
        ("round_71.md Vogue Medicube omnichannel",),
        "Omnichannel evidence is useful, but price, OP margin, sell-through, and reorder quality need backfill.",
        (E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION, E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY),
    ),
    Round71CaseCandidate(
        "coupang_data_breach_case",
        "DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY",
        "CPNG_BREACH",
        "Coupang data breach",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("ecommerce_scale", "customer_accounts"),
        ("data_breach_flag", "affected_customer_count_33_7m", "customer_trust_damage", "regulatory_investigation", "security_remediation_cost"),
        "ecommerce_data_security_hard_4c",
        "needs_exact_stage_date_backfill",
        ("round_71.md Barron's Coupang data breach",),
        "Data breach is a hard trust break; month-level date needs exact event-day backfill.",
        (E2RArchetype.RETAIL_ECOMMERCE_LOGISTICS,),
    ),
    Round71CaseCandidate(
        "coupang_supplier_payment_regulation_case",
        "DATA_SECURITY_SUPPLIER_REGULATION_OVERLAY",
        "CPNG",
        "Coupang 공급업체 압박·대금지연",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 2, 26),
        ("ecommerce_scale", "supplier_network", "margin_improvement_story"),
        ("supplier_regulation", "payment_delay", "retailer_law_violation", "supplier_pressure", "gross_margin_quality_risk"),
        "supplier_regulation_4c_watch",
        "needs_price_backfill",
        ("round_71.md Reuters Coupang supplier regulation",),
        "E-commerce margin must be separated from supplier pressure, payment delay, and regulation.",
        (E2RArchetype.RETAIL_ECOMMERCE_LOGISTICS,),
    ),
    Round71CaseCandidate(
        "coway_rental_recurring_case",
        "HOME_LIVING_APPLIANCE_RENTAL",
        "021240",
        "Coway 렌탈·관리 반복매출",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("rental_accounts", "recurring_service_revenue_ratio", "filter_service_revenue", "overseas_accounts_growth"),
        ("rental_churn_unverified", "overseas_margin_unverified", "quality_recall_risk", "governance_capital_allocation_risk"),
        "rental_recurring_success",
        "needs_source_date_and_price_backfill",
        ("round_71.md Coway rental model reference",),
        "Rental accounts and service revenue can separate Coway from hardware cycles, but churn and margin need backfill.",
    ),
    Round71CaseCandidate(
        "whirlpool_dividend_suspension_case",
        "HOME_LIVING_APPLIANCE_RENTAL",
        "WHR",
        "Whirlpool hardware cycle 4C",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("home_appliance_hardware",),
        ("replacement_demand_collapse", "housing_turnover_weakness", "dividend_suspension", "guidance_cut", "fcf_cut"),
        "home_appliance_hardware_cycle_4c",
        "needs_exact_stage_date_backfill",
        ("round_71.md Barron's Whirlpool dividend suspension",),
        "Hardware replacement-cycle weakness is a 4C reference for appliance stories without rental/service recurrence.",
    ),
    Round71CaseCandidate(
        "shein_temu_ip_litigation_case",
        "APPAREL_FAST_FASHION_BRAND_OEM",
        "SHEIN_TEMU_REF",
        "Shein-Temu IP·공급망 규제",
        "GLOBAL",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 11),
        ("fast_fashion_growth", "global_marketplace"),
        ("ip_litigation_flag", "supplier_exclusivity_dispute", "competition_law_claim", "product_safety_flag", "customs_scrutiny"),
        "fast_fashion_legal_regulatory_4c_watch",
        "missing_public_price_data",
        ("round_71.md Reuters Shein Temu litigation",),
        "Fast-fashion growth must remain Watch when IP, supplier exclusivity, product safety, and customs risks are active.",
        (E2RArchetype.TARIFF_IMPORT_REGULATION_OVERLAY,),
    ),
    Round71CaseCandidate(
        "shein_temu_eu_product_safety_case",
        "APPAREL_FAST_FASHION_BRAND_OEM",
        "SHEIN_TEMU_EU_REF",
        "Shein·Temu EU 제품안전·수입규제",
        "GLOBAL",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("fast_fashion_growth", "low_price_platform"),
        ("unsafe_item_removal_100000_plus", "product_safety_flag", "platform_responsibility", "customs_scrutiny", "import_regulation"),
        "fast_fashion_product_safety_regulatory_4c_watch",
        "needs_exact_stage_date_backfill",
        ("round_71.md FT France EU Shein Temu crackdown",),
        "Fast-fashion platforms need product-safety, customs, and platform-liability gates before any Green discussion.",
        (E2RArchetype.TARIFF_IMPORT_REGULATION_OVERLAY,),
    ),
)


ROUND71_PRICE_FIELDS: tuple[str, ...] = (
    "case_id", "symbol", "company_name", "primary_archetype", "secondary_archetypes",
    "stage1_date", "stage2_date", "stage3_date", "stage4b_date", "stage4c_date",
    "stage1_price", "stage2_price", "stage3_price", "stage4b_price", "stage4c_price", "peak_price", "peak_date",
    "MFE_30D", "MFE_90D", "MFE_180D", "MFE_1Y", "MFE_2Y",
    "MAE_30D", "MAE_90D", "MAE_180D", "MAE_1Y",
    "drawdown_after_peak", "below_stage2_price_flag", "below_stage3_price_flag",
    "export_sales_growth", "overseas_sales_ratio", "us_sales_ratio", "europe_sales_ratio", "japan_sales_ratio", "china_sales_change",
    "asp_change", "volume_growth", "shipment_growth", "sell_through_signal", "reorder_signal", "channel_entry_flag",
    "offline_channel_count", "amazon_sales_growth", "tiktok_shop_sales", "prime_day_sales",
    "op_margin_change", "eps_revision_1q", "eps_revision_1y", "fcf_margin",
    "inventory_growth", "receivables_growth", "channel_stuffing_risk_flag",
    "single_product_revenue_ratio", "hero_product_flag", "sku_expansion_flag", "recall_flag", "food_safety_flag",
    "country_sales_ban_flag", "capsaicin_or_additive_risk_flag", "viral_challenge_safety_flag",
    "tariff_flag", "tariff_rate", "de_minimis_change_flag", "fda_import_review_flag", "import_delay_flag", "gross_margin_buffer",
    "beauty_device_revenue", "beauty_device_units_sold", "beauty_device_margin", "beauty_device_asp",
    "clinical_or_safety_claim_flag", "medical_device_regulatory_risk_flag", "device_competition_flag", "repeat_consumables_revenue",
    "oem_customer_count", "odm_customer_diversification", "customer_concentration", "production_utilization", "brand_customer_sell_through",
    "same_store_sales_growth", "pb_mix_ratio", "store_count", "store_profitability", "rent_wage_pressure",
    "gmv_growth", "logistics_cost_ratio", "supplier_regulation_flag", "payment_delay_flag", "data_breach_flag",
    "affected_customer_count", "customer_trust_damage_flag", "security_remediation_cost", "gross_margin_quality_risk_flag",
    "rental_accounts", "rental_churn", "recurring_service_revenue_ratio", "filter_service_revenue", "hardware_sales_ratio",
    "dividend_suspension_flag", "replacement_demand_indicator", "housing_turnover_indicator",
    "inventory_markdown_rate", "discount_rate", "ip_litigation_flag", "product_safety_flag", "customs_scrutiny_flag",
    "supplier_exclusivity_dispute_flag", "unsafe_item_removal_count",
    "score_price_alignment", "price_validation_status", "review_notes",
)


def round71_target_for(target_id: str) -> Round71ScoreTarget | None:
    for target in ROUND71_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round71_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND71_CASE_CANDIDATES:
        target = round71_target_for(candidate.target_id)
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
                f"Round71 R5 Loop-3 case for {candidate.target_id}; "
                "recurring export/channel evidence, viral events, channel stuffing, and trust risks remain separated."
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
                "consumer_sales_growth_is_not_structural_evidence_alone",
                "sell_through_reorder_opm_and_fcf_required_for_green",
                "viral_or_channel_entry_is_stage1_not_green",
                "shipment_is_not_sell_through",
                "food_safety_data_security_tariff_and_supplier_regulation_are_redteam_overlays",
                "do_not_invent_export_sell_through_reorder_inventory_receivables_churn_or_stage_prices",
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


def round71_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND71_SCORE_TARGETS:
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
                "loop3_penalty_axes": "|".join(target.loop3_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round71_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND71_CASE_CANDIDATES:
        target = round71_target_for(candidate.target_id)
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


def round71_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "loop3_penalty_axes": "|".join(target.loop3_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND71_SCORE_TARGETS
    )


def round71_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round71_backfill": "true"} for field in ROUND71_PRICE_FIELDS)


def round71_summary() -> dict[str, int | bool]:
    records = round71_case_records()
    return {
        "target_count": len(ROUND71_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND71_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND71_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND71_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND71_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round71_r5_loop3_reports(
    *,
    output_directory: str | Path = ROUND71_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND71_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND71_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round71_r5_loop3_consumer_retail_brand_summary.md",
        "case_matrix": output / "round71_r5_loop3_case_matrix.csv",
        "stage_date_plan": output / "round71_r5_loop3_stage_date_plan.csv",
        "green_guardrails": output / "round71_r5_loop3_green_guardrails.md",
        "risk_overlays": output / "round71_r5_loop3_risk_overlays.md",
        "price_validation_plan": output / "round71_r5_loop3_price_validation_plan.md",
        "price_fields": output / "round71_r5_loop3_price_fields.csv",
    }
    _write_case_jsonl(round71_case_records(), cases)
    _write_rows(round71_score_profile_rows(), score_profiles)
    _write_rows(round71_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round71_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round71_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round71_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round71_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round71_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round71_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round71_summary_markdown() -> str:
    summary = round71_summary()
    lines = [
        "# Round-71 R5 Loop-3 Consumer / Retail / Brand Summary",
        "",
        f"- source_round: `{ROUND71_SOURCE_ROUND_PATH}`",
        "- large_sector: `CONSUMER_RETAIL_BRAND`",
        "- loop: `R5 Loop 3 / v3.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
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
        "- R5 Loop 3 says sales buzz and recurring FCF are different things.",
        "- Example: K-food can be Green-capable only when export, ASP, OPM, reorder, inventory, and safety checks align.",
        "- Example: Ulta or Sephora entry is Stage 2 evidence; sell-through and reorder decide whether it can move higher.",
        "- Example: e-commerce scale is not enough when data breach, supplier regulation, or payment delay appears.",
        "- Example: appliance hardware cycles are separate from rental/service recurring revenue.",
    ]
    return "\n".join(lines) + "\n"


def render_round71_green_guardrail_markdown() -> str:
    lines = [
        "# Round-71 R5 Loop-3 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-3 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND71_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions) or 'not_applicable'} | {', '.join(target.loop3_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R5 Loop-3 v3.0 weights to production scoring yet.",
            "- Do not treat viral demand, channel entry, GMV, user count, store count, or appliance hardware sales as Green evidence by themselves.",
            "- Do not invent export growth, sell-through, reorder, inventory, receivables, churn, tariff rate, FCF, or stage prices.",
            "- Treat food recall, country sales ban, data breach, supplier regulation, payment delay, channel stuffing, IP litigation, product safety, and tariff/import damage as RedTeam fields.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round71_risk_overlay_markdown() -> str:
    lines = [
        "# Round-71 R5 Loop-3 Risk Overlays",
        "",
        "- `EXPORT_RECURRING_ALIGNED`: export, ASP, OPM, EPS revision, and price path align.",
        "- `HERO_PRODUCT_4B`: a single hero product drives EPS, but recall, fatigue, and concentration risk remain high.",
        "- `VIRAL_WITHOUT_SELL_THROUGH`: TikTok or influencer demand exists, but reorder and OPM are unverified.",
        "- `CHANNEL_ENTRY_BUT_UNKNOWN_REORDER`: Sephora/Ulta/Target entry exists, but sell-through and reorder are missing.",
        "- `BEAUTY_DEVICE_ALIGNED_BUT_4B`: beauty device/export story works but price and valuation already require 4B-watch.",
        "- `ECOMMERCE_SCALE_WITH_TRUST_RISK`: scale exists, but data breach, supplier pressure, or payment delay threatens trust.",
        "- `MARGIN_QUALITY_RISK`: margin improvement came from supplier pressure or payment delay, not logistics efficiency.",
        "- `RENTAL_RECURRING_SUCCESS`: rental accounts, churn, service revenue, and FCF support recurrence.",
        "- `HARDWARE_CYCLE_FAILURE`: appliance demand, housing cycle, dividend, or guidance breaks the thesis.",
        "- `FAST_FASHION_LEGAL_4C`: IP, product safety, supplier, customs, or import regulation blocks unsafe Green.",
        "",
        "Simple example: `Ulta 입점` is useful Stage 2 evidence. It is not Green if sell-through, reorder, OPM, inventory, and receivables are unknown.",
    ]
    return "\n".join(lines) + "\n"


def render_round71_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-71 R5 Loop-3 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare export, sell-through, reorder, OPM, EPS revision, inventory, receivables, churn, regulation, and price path.",
        "6. Mark food recall, tariff, data breach, supplier regulation, channel stuffing, hardware cycle, and IP/product safety explicitly.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round71_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `EXPORT_RECURRING_ALIGNED`: export, ASP, OPM, EPS revision, and price path align.",
            "- `FOOD_SAFETY_REGULATORY_4C_WATCH`: recall or country sales ban requires Stage 3 review.",
            "- `KBEAUTY_STRUCTURAL_SUCCESS_CANDIDATE`: channel and export evidence route research; sell-through must be verified.",
            "- `BEAUTY_DEVICE_ALIGNED_BUT_4B`: successful device/export story, but valuation and price run require 4B-watch.",
            "- `ECOMMERCE_DATA_SECURITY_HARD_4C`: trust/regulation breaks the scale narrative.",
            "- `SUPPLIER_REGULATION_4C_WATCH`: margin quality breaks when supplier pressure or payment delay is visible.",
            "- `HARDWARE_CYCLE_FAILURE`: appliance hardware cycle lacks recurring service economics.",
            "- `FAST_FASHION_LEGAL_REGULATORY_4C_WATCH`: IP, supplier, product safety, or customs risk blocks Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round71CaseCandidate) -> str:
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    if candidate.case_type in {"structural_success", "success_candidate", "cyclical_success"}:
        return "aligned"
    return "unknown"


def _rerating_result(candidate: Round71CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "4b_watch":
        return "theme_overheat"
    if candidate.case_type == "overheat":
        return "theme_overheat"
    if candidate.case_type == "event_premium":
        return "event_premium"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    return "unknown" if candidate.case_type == "success_candidate" else "no_rerating"


def _score_weight_hint(target: Round71ScoreTarget) -> dict[str, float]:
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
    "ROUND71_CASE_CANDIDATES",
    "ROUND71_DEFAULT_CASES_PATH",
    "ROUND71_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND71_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND71_PRICE_FIELDS",
    "ROUND71_SCORE_TARGETS",
    "Round71CaseCandidate",
    "Round71ScoreTarget",
    "Round71ScoreWeightDraft",
    "render_round71_green_guardrail_markdown",
    "render_round71_price_validation_plan_markdown",
    "render_round71_risk_overlay_markdown",
    "render_round71_summary_markdown",
    "round71_case_candidate_rows",
    "round71_case_records",
    "round71_price_field_rows",
    "round71_score_profile_rows",
    "round71_stage_date_rows",
    "round71_summary",
    "round71_target_for",
    "write_round71_r5_loop3_reports",
]
