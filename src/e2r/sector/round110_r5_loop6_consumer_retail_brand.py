"""Round-110 R5 Loop-6 consumer, retail, and brand calibration pack.

Round 110 tightens R5 by separating export recurrence, hero-product
concentration, K-beauty retail platform evidence, beauty-device affiliate
commerce, e-commerce trust breaks, fast-fashion regulation, rental recurrence,
and hardware cycles. It is calibration/report material only: production feature
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


ROUND110_SOURCE_ROUND_PATH = "docs/round/round_110.md"
ROUND110_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round110_r5_loop6_consumer_retail_brand"
ROUND110_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r5_loop6_round110.jsonl"
ROUND110_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round110_r5_loop6_v6.csv"


@dataclass(frozen=True)
class Round110ScoreWeightDraft:
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
class Round110ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round110ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop6_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.CONSUMER_RETAIL_BRAND

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round110CaseCandidate:
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
) -> Round110ScoreWeightDraft:
    return Round110ScoreWeightDraft(eps_fcf, visibility, bottleneck, mispricing, valuation, capital, confidence)


def _target(
    target_id: str,
    archetype: E2RArchetype,
    posture: Round10ThemePosture,
    weight: Round110ScoreWeightDraft,
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
) -> Round110ScoreTarget:
    return Round110ScoreTarget(
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


ROUND110_SCORE_TARGETS: tuple[Round110ScoreTarget, ...] = (
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
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(23, 21, 12, 16, 10),
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
        "K_FOOD_GLOBAL_PORTFOLIO_EXPANSION",
        E2RArchetype.K_FOOD_GLOBAL_PORTFOLIO_EXPANSION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(21, 22, 11, 15, 13),
        stage1=("k_food_export_growth", "sku_expansion", "multi_country_channel", "capa_expansion"),
        stage2=("multi_sku_sales", "multi_country_shipments", "op_eps_revision", "channel_diversification"),
        stage3=("portfolio_repeat_purchase", "multi_country_sell_through", "opm_improvement", "inventory_stable"),
        stage4b=("global_k_food_portfolio_story_crowded", "capa_expansion_priced"),
        stage4c=("sku_expansion_failure", "foreign_inventory_growth", "capa_overbuild", "food_safety_issue"),
        green=("multi_sku_sales", "multi_country_sell_through", "repeat_purchase", "opm_improvement", "inventory_stable"),
        red=("single_product_dependency", "foreign_inventory_growth", "capa_overbuild", "food_safety_issue"),
        penalties=("sku_expansion", "foreign_inventory", "capa", "food_safety"),
        note="Global K-food portfolio evidence is stronger than one viral product, but sell-through and inventory still decide quality.",
    ),
    _target(
        "K_FOOD_VIRAL_BRAND_CULTURE",
        E2RArchetype.K_FOOD_VIRAL_BRAND_CULTURE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(19, 16, 8, 14, 9),
        stage1=("viral_campaign", "spicy_challenge", "creator_content", "social_media_awareness"),
        stage2=("viral_to_sales_conversion", "repeat_purchase_signal", "opm_check", "channel_expansion"),
        stage3=("sell_through", "reorder_signal", "opm_improvement", "multi_channel_repeat_purchase"),
        stage4b=("viral_narrative_overpriced", "single_campaign_story_crowded"),
        stage4c=("viral_fade", "single_campaign_failure", "discount_promotion_margin_break", "food_safety_issue"),
        green=("sell_through", "reorder_signal", "opm_improvement", "repeat_purchase"),
        red=("viral_fade", "single_campaign_dependency", "discount_promotion", "food_safety_issue"),
        penalties=("viral_fade", "single_campaign", "reorder_unverified", "discount"),
        note="Viral culture is Stage 1 routing evidence until sell-through, reorder, and OPM prove recurrence.",
    ),
    _target(
        "K_BEAUTY_EXPORT_DISTRIBUTION",
        E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(22, 23, 12, 16, 12),
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
        "K_BEAUTY_OFFLINE_SELL_THROUGH",
        E2RArchetype.K_BEAUTY_OFFLINE_SELL_THROUGH,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(22, 21, 11, 16, 12),
        stage1=("offline_channel_negotiation", "amazon_tiktok_sales", "online_viral", "us_retailer_entry"),
        stage2=("sephora_ulta_target_costco_entry", "store_count", "initial_shipment", "offline_channel_entry"),
        stage3=("offline_sell_through", "reorder_signal", "store_expansion", "inventory_receivables_stable"),
        stage4b=("channel_entry_priced_before_reorder", "k_beauty_offline_story_crowded"),
        stage4c=("reorder_absent", "inventory_growth", "receivables_growth", "discount_clearance"),
        green=("offline_sell_through", "reorder_signal", "store_expansion", "inventory_receivables_stable"),
        red=("reorder_absent", "inventory_growth", "receivables_growth", "discount_clearance"),
        penalties=("sell_through", "reorder", "inventory", "receivables", "discount"),
        note="Offline channel entry is Stage 2; sell-through and reorder are the Stage 3 proof.",
    ),
    _target(
        "K_BEAUTY_RETAIL_PLATFORM",
        E2RArchetype.K_BEAUTY_RETAIL_PLATFORM,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(21, 21, 10, 15, 12),
        stage1=("olive_young_us_entry", "sephora_ulta_kbeauty_sourcing", "curated_channel_expansion", "indie_brand_discovery"),
        stage2=("store_count", "brand_onboarding", "initial_sales", "online_to_offline_conversion"),
        stage3=("store_level_sell_through", "reorder_signal", "inventory_stable", "opm_fcf_improvement"),
        stage4b=("platform_premium_crowded", "store_expansion_priced_before_unit_economics", "online_viral_auto_translated_to_reorder"),
        stage4c=("store_economics_weak", "inventory_growth", "brand_churn", "channel_conflict", "receivables_growth"),
        green=("store_level_sell_through", "reorder_signal", "inventory_stable", "opm_fcf_improvement"),
        red=("store_economics_weak", "inventory_growth", "brand_churn", "channel_conflict", "receivables_growth"),
        penalties=("store_economics", "inventory", "brand_churn", "channel_conflict", "sell_through"),
        note="K-beauty retail platform evidence is Stage 1-2 until store-level sell-through, reorder, inventory, and FCF are visible.",
    ),
    _target(
        "K_BEAUTY_TARIFF_IMPORT_REVIEW",
        E2RArchetype.K_BEAUTY_TARIFF_IMPORT_REVIEW,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("tariff", "import_review", "fda_import_review", "retailer_stockpiling"),
        stage2=("tariff_import_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("k_beauty_tariff_risk_ignored",),
        stage4c=("tariff_flag", "import_delay", "price_increase_failed", "gross_margin_buffer_weak", "consumer_purchase_pause"),
        green=(),
        red=("tariff", "import_review", "fda_import_review", "gross_margin_buffer_weak", "price_increase_failed"),
        penalties=("tariff", "import_review", "price_increase", "gross_margin_buffer"),
        note="K-beauty export growth must pass tariff, import-review, price-increase, and gross-margin-buffer checks.",
        gate_only=True,
    ),
    _target(
        "BEAUTY_DEVICE_EXPORT",
        E2RArchetype.BEAUTY_DEVICE_EXPORT,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(23, 22, 14, 16, 9),
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
        "BEAUTY_DEVICE_AFFILIATE_COMMERCE",
        E2RArchetype.BEAUTY_DEVICE_AFFILIATE_COMMERCE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(21, 19, 12, 15, 10),
        stage1=("tiktok_affiliate", "creator_network", "prime_day_sales", "viral_review"),
        stage2=("actual_commerce_sales", "creator_conversion", "store_rollout", "affiliate_revenue"),
        stage3=("affiliate_cac_stable", "discount_rate_stable", "reorder_signal", "opm_improvement"),
        stage4b=("tiktok_amazon_sales_number_overpriced", "affiliate_story_crowded"),
        stage4c=("creator_roi_down", "discount_rate_increase", "viral_fade", "channel_inventory_build"),
        green=("affiliate_cac_stable", "discount_rate_stable", "reorder_signal", "opm_improvement"),
        red=("affiliate_cac_spike", "discount_rate_increase", "creator_dependency", "viral_fade", "channel_inventory_build"),
        penalties=("cac", "discount", "creator_dependency", "viral_fade", "inventory"),
        note="Affiliate commerce can route candidates, but CAC, discounts, creator reliance, and reorder decide margin quality.",
    ),
    _target(
        "BEAUTY_DEVICE_REGULATORY_SAFETY",
        E2RArchetype.BEAUTY_DEVICE_REGULATORY_SAFETY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("device_safety_claim", "medical_grade_claim", "electrical_device_claim", "country_regulation"),
        stage2=("regulatory_safety_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("safety_or_clinical_claim_underpriced",),
        stage4c=("medical_device_regulatory_risk", "safety_claim_challenge", "country_sales_restriction", "product_liability"),
        green=(),
        red=("medical_device_regulatory_risk", "safety_claim_challenge", "country_sales_restriction", "product_liability"),
        penalties=("device_safety", "medical_claim", "country_regulation"),
        note="Beauty devices need safety and regulatory gates when electrical, medical-grade, or clinical claims appear.",
        gate_only=True,
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
        "BEAUTY_FAST_PRODUCT_CYCLE_RISK",
        E2RArchetype.BEAUTY_FAST_PRODUCT_CYCLE_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("fast_product_cycle", "indie_brand_churn", "sku_overexpansion", "viral_brand_launch"),
        stage2=("fast_cycle_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("fast_beauty_cycle_overpriced",),
        stage4c=("sku_overexpansion", "brand_churn", "inventory_growth", "receivables_growth", "sell_through_failure"),
        green=(),
        red=("sku_overexpansion", "brand_churn", "inventory_growth", "receivables_growth", "sell_through_failure"),
        penalties=("sku_overexpansion", "brand_churn", "inventory", "receivables"),
        note="Fast beauty product velocity is a risk overlay when SKU churn, inventory, or receivables outrun sell-through.",
        gate_only=True,
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
        _w(15, 12, 5, 10, 8, 2),
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
        _w(16, 14, 8, 12, 8),
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
        "ULTRA_LOW_COST_CROSSBORDER_PLATFORM",
        E2RArchetype.ULTRA_LOW_COST_CROSSBORDER_PLATFORM,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(14, 12, 8, 11, 6),
        stage1=("crossborder_low_cost_platform_growth", "shein_temu_growth", "de_minimis", "low_price_traffic"),
        stage2=("unit_economics_improvement", "customs_compliance", "product_safety_process", "supplier_quality"),
        stage3=("repeat_customer_economics", "low_regulatory_risk", "opm_fcf_improvement"),
        stage4b=("ultra_low_cost_growth_story_crowded", "de_minimis_risk_ignored"),
        stage4c=("unsafe_item_removal", "dsa_investigation", "ip_litigation", "de_minimis_removal", "customs_scrutiny"),
        green=("unit_economics", "customs_compliance", "product_safety_process", "opm_fcf_improvement"),
        red=("unsafe_item_removal", "dsa_investigation", "ip_litigation", "de_minimis_removal", "customs_scrutiny"),
        penalties=("unsafe_items", "dsa", "de_minimis", "ip_litigation", "tariff"),
        note="Ultra-low-cost cross-border platforms are RedTeam-first because product safety, IP, customs, and platform regulation dominate.",
    ),
    _target(
        "FAST_FASHION_IP_SUPPLIER_LITIGATION",
        E2RArchetype.FAST_FASHION_IP_SUPPLIER_LITIGATION,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("ip_litigation", "supplier_exclusivity_dispute", "competition_law_claim", "copyright_claim"),
        stage2=("legal_supplychain_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("legal_risk_ignored_by_growth_narrative",),
        stage4c=("copyright_litigation", "supplier_exclusivity_dispute", "competition_law_claim", "injunction_risk"),
        green=(),
        red=("copyright_litigation", "supplier_exclusivity_dispute", "competition_law_claim", "injunction_risk"),
        penalties=("ip_litigation", "supplier_exclusivity", "competition_law"),
        note="Fast-fashion IP and supplier litigation are RedTeam overlays, not positive growth evidence.",
        gate_only=True,
    ),
    _target(
        "FAST_FASHION_PRODUCT_SAFETY_DSA",
        E2RArchetype.FAST_FASHION_PRODUCT_SAFETY_DSA,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("unsafe_item_removal", "product_safety_regulation", "dsa_investigation", "platform_responsibility"),
        stage2=("product_safety_dsa_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("product_safety_risk_ignored_by_low_price_growth",),
        stage4c=("unsafe_item_removal", "dsa_investigation", "product_safety_enforcement", "customs_scrutiny"),
        green=(),
        red=("unsafe_item_removal", "dsa_investigation", "product_safety_enforcement", "customs_scrutiny"),
        penalties=("unsafe_items", "dsa", "product_safety", "customs"),
        note="Fast-fashion product safety and DSA enforcement can cap or break low-cost platform narratives.",
        gate_only=True,
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
        "HOME_APPLIANCE_HARDWARE_CYCLE",
        E2RArchetype.HOME_APPLIANCE_HARDWARE_CYCLE,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(14, 9, 5, 8, 5),
        stage1=("home_appliance_replacement_demand", "housing_turnover", "hardware_sales_cycle"),
        stage2=("guidance_stable", "fcf_defense", "dividend_supported"),
        stage3=("not_applicable_without_recurring_service",),
        stage4b=("hardware_replacement_story_crowded",),
        stage4c=("replacement_demand_collapse", "housing_turnover_weakness", "dividend_suspension", "guidance_cut", "fcf_cut"),
        green=("recurring_service_revenue", "low_churn", "fcf_improvement"),
        red=("replacement_demand_collapse", "housing_turnover_weakness", "dividend_suspension", "guidance_cut", "fcf_cut"),
        penalties=("replacement_demand", "housing", "dividend", "guidance", "fcf"),
        note="Hardware appliance cycles are RedTeam-first unless rental/service recurrence dominates hardware replacement demand.",
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
        "ECOMMERCE_TRUST_SECURITY",
        E2RArchetype.ECOMMERCE_TRUST_SECURITY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("data_breach", "privacy_incident", "customer_trust_damage", "government_investigation"),
        stage2=("trust_security_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("scale_narrative_ignores_trust_risk",),
        stage4c=("data_breach_flag", "affected_customer_count", "customer_trust_damage", "regulatory_investigation", "security_remediation_cost"),
        green=(),
        red=("data_breach", "privacy_incident", "customer_trust_damage", "regulatory_investigation"),
        penalties=("data_security", "privacy", "trust_damage", "security_cost"),
        note="E-commerce trust and security are hard gates; customer count and logistics scale do not offset a trust break.",
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
        "ECOMMERCE_SUPPLIER_MARGIN_QUALITY",
        E2RArchetype.ECOMMERCE_SUPPLIER_MARGIN_QUALITY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("supplier_pressure", "payment_delay", "retailer_law_violation", "gross_margin_quality_risk"),
        stage2=("supplier_margin_quality_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("margin_quality_risk_ignored",),
        stage4c=("supplier_pressure_flag", "payment_delay_flag", "retailer_law_violation_flag", "gross_margin_quality_risk"),
        green=(),
        red=("supplier_pressure", "payment_delay", "retailer_law_violation", "gross_margin_quality_risk"),
        penalties=("supplier_pressure", "payment_delay", "margin_quality", "regulation"),
        note="E-commerce OPM quality must distinguish logistics efficiency from supplier pressure or delayed payments.",
        gate_only=True,
    ),
    _target(
        "DISCOUNT_PROMOTION_MARGIN_OVERLAY",
        E2RArchetype.DISCOUNT_PROMOTION_MARGIN_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("gate", "gate", "gate", "gate", "gate", "gate", "gate"),
        stage1=("discount_promotion", "affiliate_commission", "creator_cac", "viral_sales_dependency"),
        stage2=("discount_margin_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("discount_rate_increase", "affiliate_cac_spike", "creator_commission_rise", "gross_margin_break", "viral_fade"),
        green=(),
        red=("discount_rate_increase", "affiliate_cac_spike", "creator_commission_rise", "gross_margin_break", "viral_fade"),
        penalties=("discount", "affiliate_cac", "creator_commission", "gross_margin", "viral_fade"),
        note="Discount and affiliate promotion are RedTeam gates when sales growth comes from margin-damaging promotion.",
        gate_only=True,
    ),
    _target(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("cap", "cap", "cap", "cap", "cap", "cap", "+"),
        stage1=("headline_without_detail", "channel_entry_without_sell_through", "export_growth_without_inventory_detail"),
        stage2=("detail_gap_detected",),
        stage3=("not_applicable_cap_only",),
        stage4b=("headline_priced_without_detail",),
        stage4c=("disclosure_detail_missing", "parser_confidence_low", "sell_through_unverified", "margin_detail_missing"),
        green=(),
        red=("disclosure_detail_missing", "parser_confidence_low", "sell_through_unverified", "margin_detail_missing"),
        penalties=("disclosure_detail", "parser_confidence", "sell_through", "margin_detail"),
        note="Stage 3 is capped when export, channel, inventory, reorder, or margin detail is missing.",
        gate_only=True,
    ),
)


ROUND110_CASE_CANDIDATES: tuple[Round110CaseCandidate, ...] = (
    Round110CaseCandidate(
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
        ("round_110.md MarketWatch Samyang Buldak target revision",),
        "Export, ASP, CAPA, OP revision, and event-day price align, but single-product and recall overlays remain required.",
        (E2RArchetype.K_FOOD_SINGLE_HERO_PRODUCT, E2RArchetype.FOOD_SAFETY_RECALL_OVERLAY),
    ),
    Round110CaseCandidate(
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
        ("round_110.md AP Samyang Denmark recall",),
        "A successful K-food candidate still needs country-level recall and safety overlays.",
        (E2RArchetype.EXPORT_RECURRING_CONSUMER, E2RArchetype.K_FOOD_SINGLE_HERO_PRODUCT),
    ),
    Round110CaseCandidate(
        "samyang_buldak_denmark_partial_reversal_case",
        "FOOD_SAFETY_RECALL_OVERLAY",
        "003230_RECALL_REVERSAL",
        "삼양식품 Buldak 덴마크 리콜 일부 해소",
        "KR",
        "event_premium",
        None,
        date(2024, 8, 8),
        None,
        None,
        None,
        ("country_sales_ban_reversal", "buldak_brand", "regulatory_review"),
        ("country_specific_regulation_still_active", "single_product_concentration", "viral_challenge_safety_issue"),
        "food_safety_partial_reversal_watch",
        "needs_price_backfill",
        ("round_110.md AP Samyang Denmark partial reversal",),
        "Partial recall reversal can reduce one risk but does not remove country-level food-safety monitoring.",
        (E2RArchetype.EXPORT_RECURRING_CONSUMER, E2RArchetype.K_FOOD_SINGLE_HERO_PRODUCT),
    ),
    Round110CaseCandidate(
        "kfood_hero_to_portfolio_case",
        "K_FOOD_GLOBAL_PORTFOLIO_EXPANSION",
        "KFOOD_PORTFOLIO_REF",
        "K푸드 hero product에서 portfolio 확장",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("hero_product_flag", "sku_expansion_flag", "country_diversification_score", "channel_diversification_score", "repeat_purchase_signal"),
        ("hero_product_fatigue", "foreign_inventory_growth", "sku_expansion_failure", "country_sales_ban_risk"),
        "k_food_hero_to_portfolio_watch",
        "needs_source_date_and_price_backfill",
        ("round_110.md K-food hero to portfolio expansion framework",),
        "Hero products can create Stage 2, but Stage 3 needs SKU, country, channel, sell-through, and reorder proof.",
        (
            E2RArchetype.K_FOOD_SINGLE_HERO_PRODUCT,
            E2RArchetype.K_FOOD_VIRAL_BRAND_CULTURE,
            E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY,
        ),
    ),
    Round110CaseCandidate(
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
        ("round_110.md Reuters K-beauty US export",),
        "K-beauty export growth and channel entry route research, but sell-through and reorder are required before Green.",
        (E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY, E2RArchetype.K_BEAUTY_TARIFF_IMPORT_REVIEW),
    ),
    Round110CaseCandidate(
        "olive_young_us_retail_platform_case",
        "K_BEAUTY_RETAIL_PLATFORM",
        "OLIVEYOUNG_REF",
        "Olive Young 미국 리테일 플랫폼",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("olive_young_us_entry", "sephora_ulta_target_costco_channel", "indie_brand_discovery", "online_to_offline_conversion"),
        ("store_economics_unverified", "inventory_growth", "brand_churn", "channel_conflict", "sell_through_unverified"),
        "kbeauty_retail_platform_stage2_candidate",
        "needs_exact_stage_date_backfill",
        ("round_110.md Reuters Olive Young US retail platform",),
        "Retail platform evidence is useful, but store-level sell-through, reorder, inventory, and FCF must be backfilled before any Green discussion.",
        (
            E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,
            E2RArchetype.K_BEAUTY_OFFLINE_SELL_THROUGH,
            E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY,
        ),
    ),
    Round110CaseCandidate(
        "kbeauty_us_tariff_risk_case",
        "K_BEAUTY_TARIFF_IMPORT_REVIEW",
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
        ("round_110.md AP K-beauty US tariff risk",),
        "Tariff/import regulation can damage channel margin; month-level source marker needs exact date backfill.",
        (E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,),
    ),
    Round110CaseCandidate(
        "kbeauty_offline_sellthrough_case",
        "K_BEAUTY_OFFLINE_SELL_THROUGH",
        "KBEAUTY_OFFLINE_REF",
        "K뷰티 오프라인 sell-through 검증",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("offline_channel_entry", "sephora_ulta_target_costco_channel", "store_count", "initial_shipment"),
        ("reorder_absent", "inventory_growth", "receivables_growth", "discount_clearance", "sell_through_unverified"),
        "channel_entry_but_unknown_reorder",
        "needs_retailer_entry_date_and_price_backfill",
        ("round_110.md K-beauty offline sell-through framework",),
        "Offline retailer entry is Stage 2 evidence, while sell-through, reorder, inventory, receivables, and OPM decide higher stages.",
        (
            E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,
            E2RArchetype.K_BEAUTY_RETAIL_PLATFORM,
            E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY,
        ),
    ),
    Round110CaseCandidate(
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
        ("round_110.md FT APR beauty device",),
        "Beauty device export can be structurally strong, but 4x price move and valuation expansion require 4B-watch.",
        (E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,),
    ),
    Round110CaseCandidate(
        "medicube_ulta_tiktok_omnichannel_case",
        "BEAUTY_DEVICE_AFFILIATE_COMMERCE",
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
        ("round_110.md Vogue Medicube omnichannel",),
        "Omnichannel evidence is useful, but price, OP margin, sell-through, and reorder quality need backfill.",
        (
            E2RArchetype.BEAUTY_DEVICE_EXPORT,
            E2RArchetype.K_BEAUTY_OFFLINE_SELL_THROUGH,
            E2RArchetype.DISCOUNT_PROMOTION_MARGIN_OVERLAY,
            E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY,
        ),
    ),
    Round110CaseCandidate(
        "kbeauty_oem_odm_fast_beauty_case",
        "BEAUTY_OEM_ODM_SUPPLYCHAIN",
        "KBEAUTY_OEM_ODM_REF",
        "K뷰티 OEM/ODM fast-beauty 공급망",
        "KR",
        "success_candidate",
        None,
        date(2025, 6, 5),
        None,
        None,
        None,
        ("cosmax_kolmar_contract_manufacturer", "fast_beauty_model", "brand_customer_growth", "customer_diversification"),
        ("brand_sell_through_unverified", "inventory_growth", "receivables_growth", "customer_concentration"),
        "beauty_oem_odm_supplychain_candidate",
        "missing_direct_symbol_mapping",
        ("round_110.md Reuters K-beauty fast beauty OEM/ODM",),
        "OEM/ODM can diversify brand risk, but customer sell-through, inventory, receivables, and reorder must be checked.",
        (
            E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION,
            E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY,
            E2RArchetype.K_BEAUTY_TARIFF_IMPORT_REVIEW,
            E2RArchetype.BEAUTY_FAST_PRODUCT_CYCLE_RISK,
        ),
    ),
    Round110CaseCandidate(
        "coupang_data_breach_case",
        "ECOMMERCE_TRUST_SECURITY",
        "CPNG_BREACH",
        "Coupang data breach",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 11, 29),
        ("ecommerce_scale", "customer_accounts"),
        ("data_breach_flag", "affected_customer_count_33_7m", "customer_trust_damage", "regulatory_investigation", "security_remediation_cost"),
        "ecommerce_data_security_hard_4c",
        "needs_exact_stage_date_backfill",
        ("round_110.md Barron's Coupang data breach",),
        "Data breach is a hard trust break; month-level date needs exact event-day backfill.",
        (E2RArchetype.RETAIL_ECOMMERCE_LOGISTICS,),
    ),
    Round110CaseCandidate(
        "coupang_supplier_payment_regulation_case",
        "ECOMMERCE_SUPPLIER_MARGIN_QUALITY",
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
        ("round_110.md Reuters Coupang supplier regulation",),
        "E-commerce margin must be separated from supplier pressure, payment delay, and regulation.",
        (E2RArchetype.RETAIL_ECOMMERCE_LOGISTICS,),
    ),
    Round110CaseCandidate(
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
        ("round_110.md Coway rental model reference",),
        "Rental accounts and service revenue can separate Coway from hardware cycles, but churn and margin need backfill.",
    ),
    Round110CaseCandidate(
        "whirlpool_dividend_suspension_case",
        "HOME_APPLIANCE_HARDWARE_CYCLE",
        "WHR",
        "Whirlpool hardware cycle 4C",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 7),
        ("home_appliance_hardware",),
        ("replacement_demand_collapse", "housing_turnover_weakness", "dividend_suspension", "guidance_cut", "fcf_cut"),
        "home_appliance_hardware_cycle_4c",
        "needs_exact_stage_date_backfill",
        ("round_110.md Barron's Whirlpool dividend suspension",),
        "Hardware replacement-cycle weakness is a 4C reference for appliance stories without rental/service recurrence.",
    ),
    Round110CaseCandidate(
        "shein_temu_ip_litigation_case",
        "FAST_FASHION_IP_SUPPLIER_LITIGATION",
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
        ("round_110.md Reuters Shein Temu litigation",),
        "Fast-fashion growth must remain Watch when IP, supplier exclusivity, product safety, and customs risks are active.",
        (
            E2RArchetype.APPAREL_FAST_FASHION_BRAND_OEM,
            E2RArchetype.ULTRA_LOW_COST_CROSSBORDER_PLATFORM,
            E2RArchetype.FAST_FASHION_PRODUCT_SAFETY_DSA,
        ),
    ),
    Round110CaseCandidate(
        "shein_temu_eu_product_safety_case",
        "FAST_FASHION_PRODUCT_SAFETY_DSA",
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
        ("round_110.md FT France EU Shein Temu crackdown",),
        "Fast-fashion platforms need product-safety, customs, and platform-liability gates before any Green discussion.",
        (
            E2RArchetype.APPAREL_FAST_FASHION_BRAND_OEM,
            E2RArchetype.ULTRA_LOW_COST_CROSSBORDER_PLATFORM,
            E2RArchetype.FAST_FASHION_IP_SUPPLIER_LITIGATION,
        ),
    ),
)


ROUND110_PRICE_FIELDS: tuple[str, ...] = (
    "case_id", "symbol", "company_name", "primary_archetype", "secondary_archetypes",
    "stage1_date", "stage2_date", "stage3_date", "stage4b_date", "stage4c_date",
    "stage1_price", "stage2_price", "stage3_price", "stage4b_price", "stage4c_price", "peak_price", "peak_date",
    "MFE_30D", "MFE_90D", "MFE_180D", "MFE_1Y", "MFE_2Y",
    "MAE_30D", "MAE_90D", "MAE_180D", "MAE_1Y",
    "drawdown_after_peak", "below_stage2_price_flag", "below_stage3_price_flag",
    "export_sales_growth", "overseas_sales_ratio", "us_sales_ratio", "europe_sales_ratio", "japan_sales_ratio", "china_sales_change",
    "asp_change", "volume_growth", "shipment_growth", "sell_through_signal", "reorder_signal", "channel_entry_flag",
    "offline_channel_count", "store_count", "store_level_sales", "store_level_margin", "amazon_sales_growth", "tiktok_shop_sales", "prime_day_sales",
    "op_margin_change", "eps_revision_1q", "eps_revision_1y", "fcf_margin",
    "inventory_growth", "receivables_growth", "channel_stuffing_risk_flag",
    "single_product_revenue_ratio", "hero_product_flag", "sku_expansion_flag", "portfolio_expansion_flag",
    "country_diversification_score", "channel_diversification_score", "recall_flag", "food_safety_flag",
    "country_sales_ban_flag", "country_sales_ban_reversal_flag", "capsaicin_or_additive_risk_flag", "viral_challenge_safety_flag",
    "tariff_flag", "tariff_rate", "de_minimis_change_flag", "fda_import_review_flag", "import_delay_flag", "gross_margin_buffer", "price_increase_flag",
    "retailer_stockpiling_flag", "consumer_purchase_pause_flag",
    "beauty_device_revenue", "beauty_device_units_sold", "beauty_device_margin", "beauty_device_asp",
    "clinical_or_safety_claim_flag", "medical_device_regulatory_risk_flag", "device_competition_flag", "repeat_consumables_revenue",
    "device_replacement_cycle",
    "affiliate_creator_count", "creator_commission_rate", "affiliate_cac", "roas", "viral_sales_dependency_flag",
    "tiktok_shop_revenue", "amazon_prime_day_revenue", "offline_reorder_signal",
    "oem_customer_count", "odm_customer_diversification", "customer_concentration", "production_utilization", "brand_customer_sell_through",
    "fast_product_cycle_flag", "brand_churn_rate", "sku_overexpansion_flag",
    "same_store_sales_growth", "pb_mix_ratio", "store_profitability", "rent_wage_pressure",
    "gmv_growth", "logistics_cost_ratio", "supplier_regulation_flag", "payment_delay_flag", "supplier_pressure_flag",
    "retailer_law_violation_flag", "data_breach_flag",
    "affected_customer_count", "customer_trust_damage_flag", "security_remediation_cost", "post_incident_disclosure_risk_flag", "gross_margin_quality_risk_flag",
    "rental_accounts", "rental_churn", "recurring_service_revenue_ratio", "filter_service_revenue", "hardware_sales_ratio",
    "dividend_suspension_flag", "replacement_demand_indicator", "housing_turnover_indicator",
    "hardware_guidance_cut_flag", "fcf_guidance_cut_flag",
    "inventory_markdown_rate", "discount_rate", "ip_litigation_flag", "product_safety_flag", "customs_scrutiny_flag",
    "copyright_litigation_flag", "supplier_exclusivity_dispute_flag", "unsafe_item_removal_count", "platform_regulatory_investigation_flag",
    "dsa_investigation_flag", "de_minimis_exposure_flag",
    "opendart_rcept_no", "opendart_detail_fetched_flag", "disclosure_confidence_score", "detail_parser_confidence",
    "disclosure_signal_class", "routine_disclosure_flag", "risk_disclosure_flag", "high_signal_disclosure_flag",
    "score_price_alignment", "price_validation_status", "review_notes",
)


def round110_target_for(target_id: str) -> Round110ScoreTarget | None:
    for target in ROUND110_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round110_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND110_CASE_CANDIDATES:
        target = round110_target_for(candidate.target_id)
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
                f"Round110 R5 Loop-6 case for {candidate.target_id}; "
                "recurring export/channel evidence, offline sell-through, affiliate margin quality, channel stuffing, and trust risks remain separated."
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
                "discount_promotion_sales_are_not_green_without_margin_quality",
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


def round110_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND110_SCORE_TARGETS:
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
                "loop6_penalty_axes": "|".join(target.loop6_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round110_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND110_CASE_CANDIDATES:
        target = round110_target_for(candidate.target_id)
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


def round110_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "loop6_penalty_axes": "|".join(target.loop6_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND110_SCORE_TARGETS
    )


def round110_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round110_backfill": "true"} for field in ROUND110_PRICE_FIELDS)


def round110_summary() -> dict[str, int | bool]:
    records = round110_case_records()
    return {
        "target_count": len(ROUND110_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND110_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND110_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND110_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND110_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round110_r5_loop6_reports(
    *,
    output_directory: str | Path = ROUND110_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND110_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND110_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round110_r5_loop6_consumer_retail_brand_summary.md",
        "case_matrix": output / "round110_r5_loop6_case_matrix.csv",
        "stage_date_plan": output / "round110_r5_loop6_stage_date_plan.csv",
        "green_guardrails": output / "round110_r5_loop6_green_guardrails.md",
        "risk_overlays": output / "round110_r5_loop6_risk_overlays.md",
        "price_validation_plan": output / "round110_r5_loop6_price_validation_plan.md",
        "price_fields": output / "round110_r5_loop6_price_fields.csv",
    }
    _write_case_jsonl(round110_case_records(), cases)
    _write_rows(round110_score_profile_rows(), score_profiles)
    _write_rows(round110_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round110_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round110_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round110_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round110_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round110_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round110_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round110_summary_markdown() -> str:
    summary = round110_summary()
    lines = [
        "# Round-110 R5 Loop-6 Consumer / Retail / Brand Summary",
        "",
        f"- source_round: `{ROUND110_SOURCE_ROUND_PATH}`",
        "- large_sector: `CONSUMER_RETAIL_BRAND`",
        "- loop: `R5 Loop 6 / v6.0`",
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
        "- R5 Loop 6 says sales buzz and recurring FCF are different things.",
        "- Example: K-food can be Green-capable only when export, ASP, OPM, reorder, inventory, and safety checks align.",
        "- Example: Ulta or Sephora entry is Stage 2 evidence; sell-through and reorder decide whether it can move higher.",
        "- Example: Olive Young or other curated platforms need store-level sell-through and brand churn checks, not just US entry headlines.",
        "- Example: beauty-device affiliate commerce needs CAC and discount checks, not just TikTok or Amazon sales numbers.",
        "- Example: e-commerce scale is not enough when data breach, supplier regulation, or payment delay appears.",
        "- Example: appliance hardware cycles are separate from rental/service recurring revenue.",
    ]
    return "\n".join(lines) + "\n"


def render_round110_green_guardrail_markdown() -> str:
    lines = [
        "# Round-110 R5 Loop-6 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-6 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND110_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions) or 'not_applicable'} | {', '.join(target.loop6_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R5 Loop-6 v6.0 weights to production scoring yet.",
            "- Do not treat viral demand, channel entry, GMV, user count, store count, or appliance hardware sales as Green evidence by themselves.",
            "- Do not invent export growth, sell-through, reorder, inventory, receivables, churn, tariff rate, FCF, or stage prices.",
            "- Treat food recall, country sales ban, data breach, supplier regulation, payment delay, channel stuffing, IP litigation, product safety, and tariff/import damage as RedTeam fields.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round110_risk_overlay_markdown() -> str:
    lines = [
        "# Round-110 R5 Loop-6 Risk Overlays",
        "",
        "- `EXPORT_RECURRING_ALIGNED`: export, ASP, OPM, EPS revision, and price path align.",
        "- `HERO_PRODUCT_4B`: a single hero product drives EPS, but recall, fatigue, and concentration risk remain high.",
        "- `VIRAL_WITHOUT_SELL_THROUGH`: TikTok or influencer demand exists, but reorder and OPM are unverified.",
        "- `CHANNEL_ENTRY_BUT_UNKNOWN_REORDER`: Sephora/Ulta/Target entry exists, but sell-through and reorder are missing.",
        "- `RETAIL_PLATFORM_STAGE2_NOT_STAGE3`: curated retail platform expansion exists, but store economics and FCF are missing.",
        "- `K_FOOD_PORTFOLIO_EXPANSION`: multi-SKU and multi-country demand is stronger than one hero product, but inventory still matters.",
        "- `BEAUTY_DEVICE_ALIGNED_BUT_4B`: beauty device/export story works but price and valuation already require 4B-watch.",
        "- `AFFILIATE_COMMERCE_MARGIN_WATCH`: TikTok/Amazon sales need CAC, discount, creator-commission, and reorder checks.",
        "- `ECOMMERCE_SCALE_WITH_TRUST_RISK`: scale exists, but data breach, supplier pressure, or payment delay threatens trust.",
        "- `MARGIN_QUALITY_RISK`: margin improvement came from supplier pressure or payment delay, not logistics efficiency.",
        "- `RENTAL_RECURRING_SUCCESS`: rental accounts, churn, service revenue, and FCF support recurrence.",
        "- `HARDWARE_CYCLE_FAILURE`: appliance demand, housing cycle, dividend, or guidance breaks the thesis.",
        "- `FAST_FASHION_LEGAL_4C`: IP, product safety, supplier, customs, or import regulation blocks unsafe Green.",
        "- `FAST_FASHION_PRODUCT_SAFETY_DSA`: unsafe item removal, DSA, customs, or platform responsibility blocks low-price platform Green.",
        "- `DISCLOSURE_CONFIDENCE_CAP`: export, channel, inventory, reorder, or margin headlines are capped until detail fields are verified.",
        "",
        "Simple example: `Ulta 입점` is useful Stage 2 evidence. It is not Green if sell-through, reorder, OPM, inventory, and receivables are unknown.",
    ]
    return "\n".join(lines) + "\n"


def render_round110_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-110 R5 Loop-6 Price Validation Plan",
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
    for row in round110_case_candidate_rows():
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
            "- `RETAIL_PLATFORM_STAGE2_NOT_STAGE3`: retail platform expansion is useful, but store-level sell-through, reorder, and inventory must be verified.",
            "- `BEAUTY_DEVICE_ALIGNED_BUT_4B`: successful device/export story, but valuation and price run require 4B-watch.",
            "- `AFFILIATE_COMMERCE_MARGIN_WATCH`: affiliate sales need CAC and discount checks before margin-quality credit.",
            "- `ECOMMERCE_DATA_SECURITY_HARD_4C`: trust/regulation breaks the scale narrative.",
            "- `POST_BREACH_TRUST_WATCH`: remediation claims need regulator confirmation before trust risk is cleared.",
            "- `SUPPLIER_REGULATION_4C_WATCH`: margin quality breaks when supplier pressure or payment delay is visible.",
            "- `HARDWARE_CYCLE_FAILURE`: appliance hardware cycle lacks recurring service economics.",
            "- `FAST_FASHION_LEGAL_REGULATORY_4C_WATCH`: IP, supplier, product safety, or customs risk blocks Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round110CaseCandidate) -> str:
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    if candidate.case_type in {"structural_success", "success_candidate", "cyclical_success"}:
        return "aligned"
    return "unknown"


def _rerating_result(candidate: Round110CaseCandidate) -> str:
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


def _score_weight_hint(target: Round110ScoreTarget) -> dict[str, float]:
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
    "ROUND110_CASE_CANDIDATES",
    "ROUND110_DEFAULT_CASES_PATH",
    "ROUND110_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND110_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND110_PRICE_FIELDS",
    "ROUND110_SCORE_TARGETS",
    "Round110CaseCandidate",
    "Round110ScoreTarget",
    "Round110ScoreWeightDraft",
    "render_round110_green_guardrail_markdown",
    "render_round110_price_validation_plan_markdown",
    "render_round110_risk_overlay_markdown",
    "render_round110_summary_markdown",
    "round110_case_candidate_rows",
    "round110_case_records",
    "round110_price_field_rows",
    "round110_score_profile_rows",
    "round110_stage_date_rows",
    "round110_summary",
    "round110_target_for",
    "write_round110_r5_loop6_reports",
]
