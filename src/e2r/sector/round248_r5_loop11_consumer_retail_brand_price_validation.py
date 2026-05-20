"""Round-248 R5 Loop-11 consumer/retail/brand price-validation pack.

This module converts ``docs/round/round_248.md`` into structured,
calibration-only case-library records and reports. It does not change
production scoring or candidate generation.

Easy example: a tourism visa policy can move duty-free stocks for a day. It is
not Stage 3-Green until tourist spend, store sell-through, OPM, and FCF are
visible.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import CaseDataQuality, E2RCaseRecord, PriceValidation, write_case_library
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector


ROUND248_SOURCE_ROUND_PATH = "docs/round/round_248.md"
ROUND248_ROUND_ID = "round_176"
ROUND248_LARGE_SECTOR = Round10LargeSector.CONSUMER_RETAIL_BRAND.value
ROUND248_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round248_r5_loop11_consumer_retail_brand_price_validation"
ROUND248_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r5_loop11_round248.jsonl"
ROUND248_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round248_r5_loop11_consumer_retail_brand_price_validation_audit.json"

ROUND248_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "K_FOOD_EXPORT_RECURRING": E2RArchetype.K_FOOD_EXPORT_RECURRING.value,
    "K_FOOD_GLOBAL_STAPLE_BRAND": E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND.value,
    "K_FOOD_INPUT_PACKAGING_4C": E2RArchetype.K_FOOD_INPUT_PACKAGING_4C.value,
    "K_BEAUTY_DEVICE_GLOBAL_BRAND": E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND.value,
    "K_BEAUTY_INDIE_BRAND_US_CHANNEL": E2RArchetype.K_BEAUTY_INDIE_BRAND_US_CHANNEL.value,
    "K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE": E2RArchetype.K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE.value,
    "LEGACY_BEAUTY_CHINA_EXPOSURE_4C": E2RArchetype.LEGACY_BEAUTY_CHINA_EXPOSURE_4C.value,
    "ECOMMERCE_JV_SCALE_AND_DATA_GATE": E2RArchetype.ECOMMERCE_JV_SCALE_AND_DATA_GATE.value,
    "ECOMMERCE_TRUST_BREACH_HARD_4C": E2RArchetype.ECOMMERCE_TRUST_BREACH_HARD_4C.value,
    "TOURISM_RETAIL_DUTYFREE_EVENT": E2RArchetype.TOURISM_RETAIL_DUTYFREE_EVENT.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
}

ROUND248_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "repeat_demand_confirmed",
    "overseas_sales_mix_increasing",
    "channel_sellthrough_confirmed",
    "physical_store_sellthrough_confirmed",
    "asp_or_product_mix_improvement",
    "opm_or_fcf_improvement",
    "inventory_and_receivables_stable",
    "tariff_packaging_input_shock_passed",
    "customer_data_or_platform_trust_passed",
    "price_path_after_evidence",
)

ROUND248_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "viral_tiktok_only",
    "retail_talks_only",
    "ipo_or_debut_rally_only",
    "tourism_policy_only",
    "ecommerce_jv_headline_only",
    "china_decline_without_offset",
    "single_product_story_only",
    "data_breach_or_trust_break",
)

ROUND248_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "stage3_after_2x_to_4x_rerating",
    "ipo_or_debut_doubles_within_one_month",
    "single_sku_or_single_device_concentration",
    "us_listing_expectation_prices_before_sellthrough",
    "tourism_policy_basket_rally",
    "jv_or_data_scale_headline_rally",
    "good_news_while_input_tariff_risk_rises",
)

ROUND248_HARD_4C_GATES: tuple[str, ...] = (
    "food_safety_recall",
    "packaging_input_shortage_causing_production_disruption",
    "tariff_margin_squeeze",
    "channel_stuffing",
    "inventory_build",
    "receivables_spike",
    "single_product_fad_collapse",
    "retail_channel_sellthrough_failure",
    "china_sales_collapse_not_offset",
    "customer_data_breach",
    "platform_trust_break",
    "gmv_user_spending_deterioration",
    "tourism_spend_failure",
)

ROUND248_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "revenue_or_sales_anchor",
    "channel_or_user_anchor",
    "trust_or_policy_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round248ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round248ShadowWeightRow:
    archetype: E2RArchetype
    repeat_demand: int
    export_growth: int
    overseas_mix: int
    asp: int
    channel_sellthrough: int
    physical_store_sellthrough: int
    opm_fcf: int
    inventory_quality: int
    platform_trust: int
    data_compliance: int
    event_penalty: int
    stage4b_watch_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "repeat_demand": _signed(self.repeat_demand),
            "export_growth": _signed(self.export_growth),
            "overseas_mix": _signed(self.overseas_mix),
            "asp": _signed(self.asp),
            "channel_sellthrough": _signed(self.channel_sellthrough),
            "physical_store_sellthrough": _signed(self.physical_store_sellthrough),
            "opm_fcf": _signed(self.opm_fcf),
            "inventory_quality": _signed(self.inventory_quality),
            "platform_trust": _signed(self.platform_trust),
            "data_compliance": _signed(self.data_compliance),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round248DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round248CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    round_case_type: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    stage3_decision: str
    stage4b_status: str
    hard_4c_confirmed: bool
    hard_4c_krx_direct: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    mfe_1d: float | None
    mae_1d: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, object]
    score_price_alignment: str
    round_alignment_label: str
    rerating_result: str
    round_rerating_label: str
    stage_failure_type: str
    round_stage_failure_label: str
    price_validation_status: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND248_SCORE_ADJUSTMENTS: tuple[Round248ScoreAdjustment, ...] = (
    Round248ScoreAdjustment("repeat_demand", 5, "raise", "R5는 viral보다 반복구매가 중요하다."),
    Round248ScoreAdjustment("export_growth", 5, "raise", "K-food/K-beauty export가 OP/EPS로 내려오면 Stage 2 품질이 올라간다."),
    Round248ScoreAdjustment("overseas_sales_mix", 5, "raise", "해외 매출 비중 증가는 내수 프레임 해소의 핵심이다."),
    Round248ScoreAdjustment("ASP_uplift", 4, "raise", "ASP와 product mix 개선은 매출 성장의 질을 높인다."),
    Round248ScoreAdjustment("channel_sellthrough", 5, "raise", "입점이 아니라 실제 sell-through가 Green gate다."),
    Round248ScoreAdjustment("physical_store_sellthrough", 5, "raise", "오프라인 진열 후 재구매가 확인되어야 e-commerce viral과 분리된다."),
    Round248ScoreAdjustment("OPM_improvement", 5, "raise", "수출과 채널 확장은 OPM/FCF로 닫혀야 한다."),
    Round248ScoreAdjustment("inventory_quality", 4, "raise", "재고 안정은 shipment와 sell-through를 구분한다."),
    Round248ScoreAdjustment("receivables_quality", 4, "raise", "매출채권 품질은 유통/ODM의 현금전환 검증축이다."),
    Round248ScoreAdjustment("platform_trust", 5, "raise", "이커머스는 신뢰가 깨지면 사용자와 소비액이 실제로 빠진다."),
    Round248ScoreAdjustment("customer_data_compliance", 5, "raise", "JV/data scale은 data compliance를 통과해야 한다."),
    Round248ScoreAdjustment("viral_product_only", -5, "lower", "TikTok viral만으로는 반복구매를 증명하지 못한다."),
    Round248ScoreAdjustment("brand_heat_only", -5, "lower", "브랜드 열기만으로 OPM/FCF 체급 변화를 만들 수 없다."),
    Round248ScoreAdjustment("retail_talks_without_sell_through", -5, "lower", "입점 논의는 sell-through 전 Stage 2 watch다."),
    Round248ScoreAdjustment("IPO_or_debut_rally", -5, "lower", "상장/데뷔 후 급등은 4B-watch 입력이다."),
    Round248ScoreAdjustment("China_exposure_without_offset", -5, "lower", "중국 premium/travel retail 약세가 상쇄되지 않으면 Green 금지다."),
    Round248ScoreAdjustment("tourism_policy_only", -5, "lower", "관광정책은 spend/OPM 전 event premium이다."),
    Round248ScoreAdjustment("ecommerce_JV_without_GMV_margin", -4, "lower", "JV scale은 GMV/take-rate/margin 전 Green이 아니다."),
    Round248ScoreAdjustment("customer_data_risk", -5, "lower", "data breach와 privacy gate는 hard 4C/RedTeam 입력이다."),
    Round248ScoreAdjustment("packaging_input_shortage", -4, "lower", "포장재/input shortage는 K-food/K-beauty 생산과 margin을 깬다."),
    Round248ScoreAdjustment("tariff_margin_uncertainty", -4, "lower", "tariff 비용 전가가 안 되면 수출 growth의 질이 낮아진다."),
)


ROUND248_SHADOW_WEIGHT_ROWS: tuple[Round248ShadowWeightRow, ...] = (
    Round248ShadowWeightRow(E2RArchetype.K_FOOD_EXPORT_RECURRING, 5, 5, 5, 4, 5, 3, 5, 4, 2, 1, -2, 4, 3, "Samyang export/ASP/OP revision supports Stage 3 candidate but packaging/input watch remains."),
    Round248ShadowWeightRow(E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND, 5, 5, 5, 3, 5, 4, 4, 4, 2, 1, -1, 3, 3, "Nongshim global staple is Stage 2 until OPM/EPS/sell-through confirm."),
    Round248ShadowWeightRow(E2RArchetype.K_FOOD_INPUT_PACKAGING_4C, 0, 0, 0, 0, 0, 0, 4, 5, 2, 1, -3, 3, 5, "Packaging/naphtha shortage can become R5 input-cost 4C."),
    Round248ShadowWeightRow(E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND, 5, 5, 5, 3, 5, 5, 5, 3, 2, 1, -2, 5, 3, "APR is structural success but valuation/concentration require 4B-watch."),
    Round248ShadowWeightRow(E2RArchetype.K_BEAUTY_INDIE_BRAND_US_CHANNEL, 3, 5, 5, 2, 5, 5, 4, 4, 2, 1, -5, 5, 4, "D'Alba/indie K-beauty requires physical sell-through before Green."),
    Round248ShadowWeightRow(E2RArchetype.K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE, 3, 5, 5, 2, 5, 5, 4, 5, 2, 1, -3, 4, 4, "Cosmax/Kolmar/Silicon2 benefit only if brand sell-through and working capital hold."),
    Round248ShadowWeightRow(E2RArchetype.LEGACY_BEAUTY_CHINA_EXPOSURE_4C, 2, 3, 3, 2, 3, 3, 4, 5, 2, 1, -2, 4, 5, "Amore/LG H&H legacy China exposure blocks macro K-beauty Green until offset is proven."),
    Round248ShadowWeightRow(E2RArchetype.ECOMMERCE_JV_SCALE_AND_DATA_GATE, 4, 3, 2, 2, 5, 4, 5, 4, 5, 5, -4, 5, 5, "E-Mart/Alibaba JV needs GMV/take-rate/margin and data compliance."),
    Round248ShadowWeightRow(E2RArchetype.ECOMMERCE_TRUST_BREACH_HARD_4C, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 3, 5, "Coupang breach is R5 platform-trust hard 4C reference."),
    Round248ShadowWeightRow(E2RArchetype.TOURISM_RETAIL_DUTYFREE_EVENT, 2, 3, 3, 2, 5, 5, 4, 3, 3, 1, -5, 5, 4, "Tourism retail needs spend/sell-through/OPM, not just visitor policy."),
)


ROUND248_DEEP_SUB_ARCHETYPES: tuple[Round248DeepSubArchetype, ...] = (
    Round248DeepSubArchetype("K-food export", E2RArchetype.K_FOOD_EXPORT_RECURRING, ("Samyang Foods", "Buldak", "U.S./Europe shipment", "ASP", "capacity expansion")),
    Round248DeepSubArchetype("Global staple ramen", E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND, ("Nongshim", "Shin Ramyun", "North America sales", "global staple brand")),
    Round248DeepSubArchetype("K-food input shock", E2RArchetype.K_FOOD_INPUT_PACKAGING_4C, ("packaging shortage", "naphtha", "Hormuz energy crisis", "Yonwoo")),
    Round248DeepSubArchetype("K-beauty device", E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND, ("APR", "Medicube", "TikTok Shop", "Amazon", "Ulta")),
    Round248DeepSubArchetype("Indie K-beauty channel", E2RArchetype.K_BEAUTY_INDIE_BRAND_US_CHANNEL, ("d'Alba", "Tirtir", "Torriden", "Beauty of Joseon", "Ulta Sephora Target Costco")),
    Round248DeepSubArchetype("ODM/distribution leverage", E2RArchetype.K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE, ("Silicon2", "Cosmax", "Kolmar", "multi-brand repeat orders")),
    Round248DeepSubArchetype("Legacy China beauty", E2RArchetype.LEGACY_BEAUTY_CHINA_EXPOSURE_4C, ("AmorePacific", "LG H&H", "C-Beauty", "travel retail weakness")),
    Round248DeepSubArchetype("E-commerce data gate", E2RArchetype.ECOMMERCE_JV_SCALE_AND_DATA_GATE, ("E-Mart", "Shinsegae", "Alibaba", "Gmarket", "AliExpress Korea")),
    Round248DeepSubArchetype("Platform trust break", E2RArchetype.ECOMMERCE_TRUST_BREACH_HARD_4C, ("Coupang breach", "Naver", "CJ Logistics", "GMV user spending deterioration")),
    Round248DeepSubArchetype("Tourism retail event", E2RArchetype.TOURISM_RETAIL_DUTYFREE_EVENT, ("Hotel Shilla", "Hyundai Department Store", "Paradise", "Hankook Cosmetics", "visa-free Chinese tourists")),
)


ROUND248_CASE_CANDIDATES: tuple[Round248CaseCandidate, ...] = (
    Round248CaseCandidate(
        case_id="r5_loop11_samyang_buldak_export_packaging_watch",
        symbol="003230",
        company_name="Samyang Foods",
        primary_archetype=E2RArchetype.K_FOOD_EXPORT_RECURRING,
        secondary_archetypes=(E2RArchetype.EXPORT_RECURRING_CONSUMER, E2RArchetype.K_FOOD_INPUT_PACKAGING_4C, E2RArchetype.K_FOOD_SINGLE_SKU_RISK),
        case_type="structural_success",
        round_case_type="structural_success_candidate_4C-watch",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 6, 14),
        stage3_date=date(2024, 6, 14),
        stage4b_date=None,
        stage4c_date=date(2026, 3, 26),
        stage3_decision="export_asp_op_revision_supports_stage3_candidate_but_packaging_input_watch_remains",
        stage4b_status="4B-watch-if-Buldak-single-SKU-premium-prices-first",
        hard_4c_confirmed=False,
        hard_4c_krx_direct=False,
        evidence_fields=("buldak_export_growth", "us_europe_shipment_growth", "asp_uplift", "capacity_expansion", "q2_op_estimate_84pct_yoy"),
        red_flag_fields=("single_sku_premium_watch", "packaging_shortage_context", "naphtha_energy_crisis", "input_availability_risk"),
        price_data_source="MarketWatch / Reuters reported anchors",
        reported_price_anchor="647,000 KRW close, +5.7% event return",
        reported_return_anchor="target price 830,000 KRW, Q2 OP estimate 81.2B KRW and +84% YoY",
        mfe_1d=5.7,
        mae_1d=None,
        stage2_price_anchor=647000.0,
        stage3_price_anchor=647000.0,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"implied_prior_close_krw": 611921.0, "target_price_krw": 830000.0, "target_upside_pct": 28.3, "op_estimate_q2_krw_bn": 81.2, "op_growth_estimate_pct": 84.0, "packaging_shock_context": "Samyang/Nongshim/Yonwoo packaging shortage under naphtha/energy crisis"},
        score_price_alignment="aligned",
        round_alignment_label="aligned_partial",
        rerating_result="true_rerating",
        round_rerating_label="K_food_export_rerating_candidate",
        stage_failure_type="green_success",
        round_stage_failure_label="green_success_candidate_with_input_packaging_watch",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Export/ASP/OP revision supports Stage 3 candidate; packaging/input risk requires 4C-watch.",
    ),
    Round248CaseCandidate(
        case_id="r5_loop11_nongshim_shin_global_staple",
        symbol="004370",
        company_name="Nongshim",
        primary_archetype=E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND,
        secondary_archetypes=(E2RArchetype.EXPORT_RECURRING_CONSUMER, E2RArchetype.K_FOOD_INPUT_PACKAGING_4C),
        case_type="success_candidate",
        round_case_type="success_candidate",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 5, 27),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="global_staple_structure_is_stage2_until_opm_eps_channel_sellthrough_inventory_confirm",
        stage4b_status="4B-watch-if-global-staple-narrative-rally",
        hard_4c_confirmed=False,
        hard_4c_krx_direct=False,
        evidence_fields=("shin_ramyun_2023_sales_1_2tn_krw", "overseas_sales_nearly_60pct", "north_america_sales_538mn_usd", "us_sales_target_1_5bn_by_2030"),
        red_flag_fields=("opm_eps_confirmation_needed", "channel_sellthrough_needed", "inventory_backfill_needed", "packaging_input_shock_watch"),
        price_data_source="FT business evidence",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="Shin Ramyun 2023 sales 1.2T KRW / $883M, overseas nearly 60%, North America +10%",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"shin_2023_sales_krw_trn": 1.2, "shin_2023_sales_usd_mn": 883.0, "overseas_sales_share_pct": 60.0, "north_america_sales_2023_usd_mn": 538.0, "north_america_growth_pct": 10.0, "us_sales_target_2030_usd_bn": 1.5, "target_growth_from_2023_na_sales_pct": 178.8},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="global_staple_brand_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Global staple and overseas expansion are Stage 2; OPM/EPS and channel sell-through required for Green.",
    ),
    Round248CaseCandidate(
        case_id="r5_loop11_apr_medicube_structural_4b",
        symbol="278470",
        company_name="APR / Medicube",
        primary_archetype=E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND,
        secondary_archetypes=(E2RArchetype.BEAUTY_DEVICE_AFFILIATE_COMMERCE, E2RArchetype.K_BEAUTY_BRAND_US_CHANNEL, E2RArchetype.BEAUTY_DEVICE_REGULATORY_SAFETY),
        case_type="structural_success",
        round_case_type="structural_success_4B-watch",
        stage1_date=date(2024, 2, 1),
        stage2_date=date(2025, 7, 8),
        stage3_date=None,
        stage4b_date=date(2025, 7, 8),
        stage4c_date=None,
        stage3_decision="revenue_conversion_supports_structural_success_but_stage3_date_is_quarter_window_not_exact",
        stage4b_status="4B-watch-valuation-and-Medicube-concentration",
        hard_4c_confirmed=False,
        hard_4c_krx_direct=False,
        evidence_fields=("stage2_price_158300_krw", "ipo_to_stage2_up_over_75pct", "q4_2025_revenue_growth_124pct", "overseas_revenue_growth_203pct", "tiktok_amazon_ulta_channel_conversion"),
        red_flag_fields=("medicube_revenue_share_91_7pct", "single_brand_device_concentration", "post_ipo_valuation_watch", "sellthrough_retention_backfill_needed"),
        price_data_source="Business Insider / Vogue Business anchors",
        reported_price_anchor="158,300 KRW stage2 price, IPO-to-stage2 >75%",
        reported_return_anchor="Q4 2025 revenue $440M +124%, overseas $362M +203%, Medicube FY revenue $1.1B",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=158300.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=158300.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"stage3_window": "2025_Q4_candidate", "ipo_to_stage2_mfe_min_pct": 75.0, "implied_ipo_reference_price_max_krw": 90457.0, "market_cap_july_2025_usd_bn": 4.2, "q4_2025_revenue_usd_mn": 440.0, "q4_2025_revenue_growth_pct": 124.0, "q4_2025_overseas_revenue_usd_mn": 362.0, "q4_2025_overseas_growth_pct": 203.0, "q4_overseas_revenue_share_pct": 87.0, "fy_2025_revenue_usd_bn": 1.2, "medicube_fy_2025_revenue_usd_bn": 1.1, "medicube_revenue_share_pct": 91.7, "tiktok_shop_revenue_usd_mn": 102.9, "amazon_prime_day_sales_usd_mn": 22.0, "ulta_store_expansion_count": 1400},
        score_price_alignment="aligned",
        round_alignment_label="aligned",
        rerating_result="true_rerating",
        round_rerating_label="K_beauty_device_true_rerating_plus_4B_watch",
        stage_failure_type="green_success",
        round_stage_failure_label="green_success_candidate",
        price_validation_status="reported_price_and_revenue_anchor_not_full_ohlc",
        notes="Revenue conversion supports structural success, but Medicube concentration and valuation require 4B-watch.",
    ),
    Round248CaseCandidate(
        case_id="r5_loop11_indie_kbeauty_odm_distribution_watch",
        symbol="483650/257720/192820/161890",
        company_name="d'Alba / Silicon2 / Cosmax / Kolmar basket",
        primary_archetype=E2RArchetype.K_BEAUTY_INDIE_BRAND_US_CHANNEL,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE, E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION_KOREA, E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY),
        case_type="overheat",
        round_case_type="success_candidate_overheat",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 6, 5),
        stage3_date=None,
        stage4b_date=date(2025, 6, 5),
        stage4c_date=None,
        stage3_decision="retail_talks_and_ecommerce_growth_are_stage2_until_physical_sellthrough_repeat_order_opm_working_capital_confirm",
        stage4b_status="4B-watch-debut-rally-before-sellthrough",
        hard_4c_confirmed=False,
        hard_4c_krx_direct=False,
        evidence_fields=("top5_kbeauty_us_ecommerce_growth_71pct", "us_market_growth_21pct", "retail_talks_ulta_sephora_target_costco", "cosmax_kolmar_odm_model", "silicon2_distribution_leverage"),
        red_flag_fields=("dalba_reported_more_than_double_since_debut", "physical_store_sellthrough_missing", "inventory_receivables_unknown", "tariff_margin_uncertainty"),
        price_data_source="Reuters business and reported return anchors",
        reported_price_anchor="d'Alba reported more than doubled since debut",
        reported_return_anchor="top-five K-beauty U.S. e-commerce brands +71% over two years vs U.S. market +21%",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"dalba_reported_mfe_since_debut_pct": 100.0, "top5_korean_cosmetics_us_ecommerce_growth_pct": 71.0, "overall_us_market_growth_pct": 21.0, "relative_growth_vs_us_market_multiple": 3.38, "retail_talks": ["Ulta", "Sephora", "Target", "Costco"], "odm_model": ["Cosmax", "Kolmar"]},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence_for_dalba_success_candidate_for_odm_distribution",
        rerating_result="theme_overheat",
        round_rerating_label="K_beauty_indie_retail_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="stage2_evidence_not_green",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Retail talks and ecommerce growth are Stage 2; physical sell-through, repeat orders, OPM and working-capital quality required before Green.",
    ),
    Round248CaseCandidate(
        case_id="r5_loop11_amore_lghh_legacy_china_exposure",
        symbol="090430/051900",
        company_name="AmorePacific / LG Household & Health Care",
        primary_archetype=E2RArchetype.LEGACY_BEAUTY_CHINA_EXPOSURE_4C,
        secondary_archetypes=(E2RArchetype.CHINA_CONSUMER_EXPOSURE_4C, E2RArchetype.K_BEAUTY_TARIFF_IMPORT_REVIEW),
        case_type="failed_rerating",
        round_case_type="failed_rerating_4C-watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="kbeauty_macro_tailwind_is_not_company_green_without_us_europe_offset_and_opm_recovery",
        stage4b_status="not_applicable_4C-watch",
        hard_4c_confirmed=False,
        hard_4c_krx_direct=False,
        evidence_fields=("china_beauty_market_75bn_usd", "new_kbeauty_outperformance_context", "apr_valuation_context_6bn_usd"),
        red_flag_fields=("china_demand_weakness", "cbeauty_local_competition", "dutyfree_travel_retail_weakness", "premium_beauty_slowdown"),
        price_data_source="FT / Vogue / Reuters legacy-China beauty context",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="legacy China/travel retail risk while new K-beauty winners outperform",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stage4c_window": "2024_to_2026_watch", "china_beauty_market_size_usd_bn": 75.0, "legacy_risk_factors": ["China demand weakness", "C-Beauty local competition", "duty-free/travel retail weakness", "premium beauty slowdown"], "new_kbeauty_outperformance_context": "APR became most valuable Korean beauty group in FT framing", "apr_valuation_context_usd_bn": 6.0},
        score_price_alignment="unknown",
        round_alignment_label="thesis_break_watch_insufficient_price_data",
        rerating_result="thesis_break",
        round_rerating_label="legacy_K_beauty_China_exposure_break",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="should_have_been_yellow_or_red",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="K-beauty macro is not enough; China and travel-retail weakness block Green until U.S./Europe offset is proven.",
    ),
    Round248CaseCandidate(
        case_id="r5_loop11_emart_shinsegae_alibaba_jv_data_gate",
        symbol="139480/004170",
        company_name="E-Mart / Shinsegae / Alibaba JV",
        primary_archetype=E2RArchetype.ECOMMERCE_JV_SCALE_AND_DATA_GATE,
        secondary_archetypes=(E2RArchetype.ECOMMERCE_RESTRUCTURING_JV_KOREA, E2RArchetype.RETAIL_PLATFORM_DATA_REGULATION_OVERLAY, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_data_privacy_watch",
        stage1_date=date(2024, 12, 26),
        stage2_date=date(2025, 9, 18),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="jv_and_data_scale_are_stage2_until_gmv_take_rate_margin_retention_and_data_compliance_confirm",
        stage4b_status="4B-watch-if-JV-headline-rally",
        hard_4c_confirmed=False,
        hard_4c_krx_direct=False,
        evidence_fields=("emart_event_plus_5_5pct", "50_50_joint_venture", "expected_cross_border_market_share_41pct", "gmarket_50mn_customer_database", "alibaba_share_by_value_62pct"),
        red_flag_fields=("kftc_conditional_approval", "data_sharing_restriction_three_years", "gmv_take_rate_margin_unconfirmed", "cross_border_margin_pressure"),
        price_data_source="WSJ / Reuters JV and regulatory anchors",
        reported_price_anchor="E-Mart +5.5% JV event return",
        reported_return_anchor="JV share 41%, Gmarket 50M customer data, China online imports 4.7T KRW +32%",
        mfe_1d=5.5,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"jv_announcement_date": "2024-12-26", "kftc_approval_date": "2025-09-18", "jv_structure": "50:50 joint venture", "assets": ["AliExpress Korea", "Gmarket"], "kftc_approval": "conditional", "expected_cross_border_market_share_pct": 41.0, "gmarket_customer_database_mn": 50.0, "data_sharing_restriction_years": 3.0, "korean_spending_chinese_online_imports_2024_krw_trn": 4.7, "growth_pct": 32.0, "alibaba_share_by_value_pct": 62.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_regulatory_data_watch",
        rerating_result="unknown",
        round_rerating_label="e_commerce_JV_scale_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="JV scale is Stage 2; GMV, take-rate, margin, retention and data compliance required before Green.",
    ),
    Round248CaseCandidate(
        case_id="r5_loop11_coupang_breach_ecommerce_trust_reference",
        symbol="CPNG/035420/139480/000120",
        company_name="Coupang breach / Naver-E-Mart-CJ Logistics competitor basket",
        primary_archetype=E2RArchetype.ECOMMERCE_TRUST_BREACH_HARD_4C,
        secondary_archetypes=(E2RArchetype.ECOMMERCE_TRUST_SECURITY, E2RArchetype.OPERATIONAL_TRUST_HARD_4C, E2RArchetype.RETAIL_ECOMMERCE_LOGISTICS),
        case_type="4c_thesis_break",
        round_case_type="hard_4C_reference_competitor_success_candidate",
        stage1_date=date(2025, 11, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 2, 25),
        stage3_decision="competitor_opportunity_is_not_green_until_user_retention_gmv_margin_logistics_utilization_confirm",
        stage4b_status="not_applicable_hard_4C_reference",
        hard_4c_confirmed=True,
        hard_4c_krx_direct=False,
        evidence_fields=("coupang_users_affected_34mn", "coupang_mobile_activity_minus_3_5pct", "average_daily_spending_minus_6_3pct", "coupang_stock_drawdown_minus_34pct", "naver_mobile_users_plus_23pct", "cj_logistics_volume_plus_120pct"),
        red_flag_fields=("customer_data_breach", "platform_trust_break", "gmv_user_spending_deterioration", "revenue_estimate_trim", "core_earnings_estimate_trim"),
        price_data_source="Reuters e-commerce breach / competitor anchor",
        reported_price_anchor="Coupang -34% since breach; Naver users +23%; CJ overnight/one-day volume +120%",
        reported_return_anchor="34M users affected, activity -3.5%, spending -6.3%",
        mfe_1d=None,
        mae_1d=-34.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stage4c_window": "2025-11_to_2026-02", "coupang_users_affected_mn": 34.0, "mobile_activity_change_pct": -3.5, "average_daily_spending_change_pct": -6.3, "average_daily_spending_january_krw_bn": 139.2, "coupang_stock_drawdown_since_breach_pct": -34.0, "naver_mobile_users_change_pct": 23.0, "cj_logistics_overnight_one_day_volume_growth_pct": 120.0, "q4_revenue_estimate_trim_pct": -2.2, "q4_core_earnings_estimate_trim_pct": -6.7, "hard_4c_krx_direct": False, "hard_4c_reference": True},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_for_Coupang_success_candidate_for_competitors",
        rerating_result="thesis_break",
        round_rerating_label="e_commerce_trust_break_and_share_shift_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C_reference_non_krx",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Coupang is non-KRX but is the clean R5 platform-trust hard 4C reference; competitors need GMV/margin confirmation before Green.",
    ),
    Round248CaseCandidate(
        case_id="r5_loop11_tourism_retail_china_visa_event",
        symbol="008770/069960/034230/123690",
        company_name="Hotel Shilla / Hyundai Department Store / Paradise / Hankook Cosmetics",
        primary_archetype=E2RArchetype.TOURISM_RETAIL_DUTYFREE_EVENT,
        secondary_archetypes=(E2RArchetype.CASINO_DUTYFREE_TOURISM, E2RArchetype.TOURISM_POLICY_EVENT, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_success_candidate",
        stage1_date=date(2025, 8, 6),
        stage2_date=date(2025, 8, 6),
        stage3_date=None,
        stage4b_date=date(2025, 8, 6),
        stage4c_date=None,
        stage3_decision="tourism_policy_event_is_stage2_until_tourist_spend_dutyfree_sales_casino_drop_hold_opm_confirm",
        stage4b_status="4B-watch-tourism-policy-basket-rally",
        hard_4c_confirmed=False,
        hard_4c_krx_direct=False,
        evidence_fields=("china_group_tourist_visa_free_policy", "hyundai_department_plus_7_1pct", "hotel_shilla_plus_4_8pct", "paradise_plus_2_9pct", "hankook_cosmetics_plus_9_9pct"),
        red_flag_fields=("tourism_policy_only", "tourist_spend_unconfirmed", "dutyfree_margin_unknown", "anti_chinese_social_trust_risk", "tourism_policy_fade"),
        price_data_source="Reuters event return and tourism policy anchors",
        reported_price_anchor="Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%",
        reported_return_anchor="Chinese groups of 3+ can stay 15 days visa-free from 2025-09-29 through 2026-06",
        mfe_1d=9.9,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hyundai_department_event_mfe_1d_pct": 7.1, "hotel_shilla_event_mfe_1d_pct": 4.8, "paradise_event_mfe_1d_pct": 2.9, "hankook_cosmetics_event_mfe_1d_pct": 9.9, "visa_free_period": "2025-09-29_to_2026-06", "visa_free_stay_days": 15, "group_condition": "3+ Chinese tourists"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="tourism_retail_recovery_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Visa-free tourist policy is Stage 2/event; tourist spend, sell-through, duty-free sales and OPM required before Green.",
    ),
)


def round248_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND248_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND248_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round248 R5 Loop-11 consumer/retail/brand price validation case. "
                "Calibration-only; not candidate-generation input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(token in field for token in ("export", "asp", "op", "revenue", "overseas", "sellthrough", "channel"))),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field for token in ("premium", "rally", "debut", "ipo", "concentration", "event"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field for token in ("breach", "trust", "shortage", "china", "inventory", "receivables", "tariff", "weakness", "collapse", "spending"))),
            must_have_fields=ROUND248_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND248_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_sellthrough_gmv_margin_inventory_or_fcf",
                "do_not_treat_brand_heat_tourism_policy_jv_or_viral_media_as_green",
                *ROUND248_GREEN_REQUIRED_FIELDS,
                *ROUND248_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.stage2_price_anchor is not None
                    or candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round248_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "case_id": candidate.case_id,
            "symbol": candidate.symbol,
            "company_name": candidate.company_name,
            "primary_archetype": candidate.primary_archetype.value,
            "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
            "case_type": candidate.case_type,
            "round_case_type": candidate.round_case_type,
            "stage1_date": _date_text(candidate.stage1_date),
            "stage2_date": _date_text(candidate.stage2_date),
            "stage3_date": _date_text(candidate.stage3_date),
            "stage4b_date": _date_text(candidate.stage4b_date),
            "stage4c_date": _date_text(candidate.stage4c_date),
            "stage3_decision": candidate.stage3_decision,
            "stage4b_status": candidate.stage4b_status,
            "hard_4c_confirmed": str(candidate.hard_4c_confirmed).lower(),
            "hard_4c_krx_direct": str(candidate.hard_4c_krx_direct).lower(),
            "price_data_source": candidate.price_data_source,
            "reported_price_anchor": candidate.reported_price_anchor,
            "reported_return_anchor": candidate.reported_return_anchor,
            "mfe_1d": _float_text(candidate.mfe_1d),
            "mae_1d": _float_text(candidate.mae_1d),
            "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
            "stage3_price_anchor": _float_text(candidate.stage3_price_anchor),
            "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": candidate.score_price_alignment,
            "round_alignment_label": candidate.round_alignment_label,
            "rerating_result": candidate.rerating_result,
            "round_rerating_label": candidate.round_rerating_label,
            "stage_failure_type": candidate.stage_failure_type,
            "round_stage_failure_label": candidate.round_stage_failure_label,
            "price_validation_status": candidate.price_validation_status,
            "evidence_fields": "|".join(candidate.evidence_fields),
            "red_flag_fields": "|".join(candidate.red_flag_fields),
            "notes": candidate.notes,
        }
        for candidate in ROUND248_CASE_CANDIDATES
    )


def round248_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND248_SCORE_ADJUSTMENTS)


def round248_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND248_SHADOW_WEIGHT_ROWS)


def round248_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND248_DEEP_SUB_ARCHETYPES)


def round248_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round248_price_validation": "true"} for field in ROUND248_PRICE_VALIDATION_FIELDS)


def round248_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round248_label": label, "canonical_archetype": canonical} for label, canonical in ROUND248_REQUIRED_TARGET_ALIASES.items())


def round248_summary() -> dict[str, int | bool | str]:
    cases = ROUND248_CASE_CANDIDATES
    return {
        "source_round": ROUND248_SOURCE_ROUND_PATH,
        "round_id": ROUND248_ROUND_ID,
        "large_sector": ROUND248_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "hard_4c_krx_confirmed": any(case.hard_4c_krx_direct for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B-watch" in case.stage4b_status),
        "watch_4c_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.round_case_type),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "reported_price_anchor_count": sum(1 for case in cases if case.price_validation_status != "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND248_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND248_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND248_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round248_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND248_SOURCE_ROUND_PATH,
        "round_id": ROUND248_ROUND_ID,
        "large_sector": ROUND248_LARGE_SECTOR,
        "summary": round248_summary(),
        "target_aliases": dict(ROUND248_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND248_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND248_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND248_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND248_HARD_4C_GATES),
        "score_adjustments": list(round248_score_adjustment_rows()),
        "shadow_weights": list(round248_shadow_weight_rows()),
        "deep_sub_archetypes": list(round248_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND248_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round248_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_brand_heat_tourism_policy_jv_or_viral_media_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round248_summary_markdown() -> str:
    summary = round248_summary()
    lines = [
        "# Round 248 R5 Loop 11 Consumer Retail Brand Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- structural_success: {summary['structural_success_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- hard_4c_reference: {summary['hard_4c_case_count']}",
        f"- hard_4c_krx_confirmed: {str(summary['hard_4c_krx_confirmed']).lower()}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND248_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.round_case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    case.round_alignment_label,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Samyang is an export/ASP/OP revision Stage 3 candidate, but packaging/input shock stays on 4C-watch.",
            "- Nongshim is global-staple Stage 2 until OPM/EPS and channel sell-through confirm.",
            "- APR/Medicube is structural success, but Medicube concentration and valuation need 4B-watch.",
            "- d'Alba and the indie K-beauty/ODM basket are Stage 2/overheat until physical sell-through and working capital confirm.",
            "- Legacy Amore/LG H&H must clear China and travel-retail weakness before any Green interpretation.",
            "- E-Mart/Shinsegae-Alibaba JV is Stage 2 scale optionality with data-compliance gates.",
            "- Coupang breach is a non-KRX hard 4C reference for platform trust; competitor opportunities still need GMV/margin proof.",
            "- Tourism retail is an event premium until tourist spend, duty-free sales, casino drop/hold and OPM confirm.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round248_green_gate_review_markdown() -> str:
    lines = [
        "# Round 248 R5 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R5 Stage 3-Green is not `K-food`, `K-beauty`, `tourism policy`, or `e-commerce JV`. It requires repeat demand, overseas sell-through, ASP/OPM, inventory/receivables quality, and platform trust.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND248_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND248_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND248_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `retail talks` are Stage 2 until physical-store sell-through and reorder appear.",
            "- `tourism visa-free policy` is event premium until tourist spend and OPM appear.",
            "- `data breach` is platform-trust 4C; competitor opportunity still needs GMV and margin.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round248_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 248 R5 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND248_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND248_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | KRX direct hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND248_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {str(case.hard_4c_krx_direct).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round248_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 248 R5 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, sell-through, GMV, margin, inventory, receivables, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND248_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND248_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round248_r5_loop11_reports(
    output_directory: str | Path = ROUND248_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND248_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND248_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round248_case_records(), cases_path),
        "audit": _write_json(round248_audit_payload(), audit_path),
        "summary": output / "round248_r5_loop11_price_validation_summary.md",
        "case_matrix": output / "round248_r5_loop11_case_matrix.csv",
        "target_aliases": output / "round248_r5_loop11_target_aliases.csv",
        "score_adjustments": output / "round248_r5_loop11_score_adjustments.csv",
        "shadow_weights": output / "round248_r5_loop11_shadow_weights.csv",
        "deep_sub_archetypes": output / "round248_r5_loop11_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round248_r5_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round248_r5_loop11_green_gate_review.md",
        "price_validation_plan": output / "round248_r5_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round248_r5_loop11_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round248_summary_markdown(), encoding="utf-8")
    _write_csv(round248_case_rows(), paths["case_matrix"])
    _write_csv(round248_target_alias_rows(), paths["target_aliases"])
    _write_csv(round248_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round248_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round248_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round248_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round248_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round248_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round248_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def _write_json(payload: object, path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def _write_csv(rows: Iterable[dict[str, str]], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    rows = tuple(rows)
    if not rows:
        target.write_text("", encoding="utf-8")
        return target
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _float_text(value: float | None) -> str:
    return "" if value is None else f"{value:g}"


def _signed(value: int) -> str:
    return f"+{value}" if value > 0 else str(value)
