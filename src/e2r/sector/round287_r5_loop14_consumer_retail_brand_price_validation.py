"""Round-287 R5 Loop-14 consumer/retail/brand price-validation pack.

This module converts ``docs/round/round_287.md`` into calibration-only case
records and reports. It intentionally does not change production scoring,
StageClassifier thresholds, or candidate generation.

Easy example: Samyang's Buldak export case gets credit for ASP, U.S./Europe
shipments and capacity conversion, but a Denmark recall still stays as a
local-regulation 4C-watch gate. Popularity alone is not Stage 3-Green.
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


ROUND287_SOURCE_ROUND_PATH = "docs/round/round_287.md"
ROUND287_ANALYST_ROUND_ID = "round_215"
ROUND287_LARGE_SECTOR = "CONSUMER_RETAIL_BRAND"
ROUND287_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round287_r5_loop14_consumer_retail_brand_price_validation"
ROUND287_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r5_loop14_round287.jsonl"
ROUND287_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round287_r5_loop14_consumer_retail_brand_price_validation_audit.json"

ROUND287_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE": E2RArchetype.K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE.value,
    "K_FOOD_EXPORT_REGULATORY_4C_WATCH": E2RArchetype.K_FOOD_EXPORT_REGULATORY_4C_WATCH.value,
    "K_BEAUTY_DEVICE_BRAND_4B": E2RArchetype.K_BEAUTY_DEVICE_BRAND_4B.value,
    "K_BEAUTY_US_EXPANSION_STAGE2": E2RArchetype.K_BEAUTY_US_EXPANSION_STAGE2.value,
    "CHINA_TOURISM_RETAIL_EVENT_PREMIUM": E2RArchetype.CHINA_TOURISM_RETAIL_EVENT_PREMIUM.value,
    "ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE": E2RArchetype.ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE.value,
    "ECOMMERCE_TRUST_BREAK_HARD_REFERENCE": E2RArchetype.ECOMMERCE_TRUST_BREAK_HARD_REFERENCE.value,
    "RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2": E2RArchetype.RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2.value,
    "DOMESTIC_CONSUMPTION_SHOCK_4C_WATCH": E2RArchetype.DOMESTIC_CONSUMPTION_SHOCK_4C_WATCH.value,
}

ROUND287_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "export_sellthrough_confirmed",
    "brand_ASP_power_confirmed",
    "capacity_to_revenue_conversion_confirmed",
    "offline_channel_sellthrough_confirmed",
    "tariff_absorption_confirmed",
    "tourist_spend_per_head_confirmed",
    "ecommerce_take_rate_confirmed",
    "data_trust_internal_control_confirmed",
    "fulfillment_unit_economics_confirmed",
    "domestic_consumption_sensitivity_measured",
    "price_path_after_evidence",
)

ROUND287_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "viral_brand_headline_only",
    "visitor_count_only",
    "online_ecommerce_growth_without_offline_sellthrough",
    "JV_scale_without_take_rate",
    "revenue_uplift_without_unit_economics",
    "IPO_or_stock_pop_without_repeat_purchase",
    "consumer_export_story_without_local_regulatory_fit",
    "domestic_retail_ignored",
    "data_breach_or_customer_trust_failure",
)

ROUND287_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "brand_rerating_50_to_100pct_before_channel_margin",
    "IPO_pop_2x_before_repeat_purchase",
    "viral_tiktok_or_celebrity_before_repeat_purchase",
    "tourism_visa_headline_basket_rally",
    "cross_border_JV_scale_before_take_rate",
    "logistics_revenue_uplift_before_unit_economics",
    "competitor_readthrough_after_trust_event",
)

ROUND287_HARD_4C_GATES: tuple[str, ...] = (
    "data_breach_customer_trust_break",
    "regulatory_recall_local_health_issue",
    "tariff_shock_not_absorbed",
    "channel_inventory_or_sellthrough_failure",
    "tourist_arrivals_without_spending_conversion",
    "JV_data_regulation_constraint",
    "fulfillment_cost_inflation_unit_economics_break",
    "domestic_consumption_shock_discretionary_decline",
)

ROUND287_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "reported_event_price_anchor",
    "target_price_anchor",
    "op_estimate_anchor",
    "sales_export_anchor",
    "user_spend_anchor",
    "policy_period_anchor",
    "data_trust_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round287ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round287ShadowWeightRow:
    archetype: E2RArchetype
    export_sellthrough: int
    brand_asp_power: int
    capacity_to_revenue: int
    offline_sellthrough: int
    tariff_absorption: int
    tourist_spend_per_head: int
    ecommerce_take_rate: int
    data_trust: int
    fulfillment_unit_economics: int
    domestic_consumption_sensitivity: int
    headline_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "export_sellthrough": _signed(self.export_sellthrough),
            "brand_ASP_power": _signed(self.brand_asp_power),
            "capacity_to_revenue": _signed(self.capacity_to_revenue),
            "offline_sellthrough": _signed(self.offline_sellthrough),
            "tariff_absorption": _signed(self.tariff_absorption),
            "tourist_spend_per_head": _signed(self.tourist_spend_per_head),
            "ecommerce_take_rate": _signed(self.ecommerce_take_rate),
            "data_trust": _signed(self.data_trust),
            "fulfillment_unit_economics": _signed(self.fulfillment_unit_economics),
            "domestic_consumption_sensitivity": _signed(self.domestic_consumption_sensitivity),
            "headline_penalty": _signed(self.headline_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round287DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round287CaseCandidate:
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
    service_trust_hard_reference_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    event_mfe_pct: float | None
    event_mae_pct: float | None
    stage1_price_anchor: float | None
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


ROUND287_SCORE_ADJUSTMENTS: tuple[Round287ScoreAdjustment, ...] = (
    Round287ScoreAdjustment("export_sellthrough", 5, "raise", "K-food/K-beauty 수출은 sell-in보다 sell-through가 먼저다."),
    Round287ScoreAdjustment("brand_ASP_power", 5, "raise", "브랜드가 실제 판가와 마진으로 닫혀야 한다."),
    Round287ScoreAdjustment("capacity_to_revenue_conversion", 4, "raise", "CAPA 증설은 매출과 OP로 전환될 때만 강하다."),
    Round287ScoreAdjustment("offline_channel_sellthrough", 5, "raise", "미국 리테일 입점은 매장 회전과 리오더가 필요하다."),
    Round287ScoreAdjustment("tariff_absorption", 5, "raise", "관세 이후에도 gross margin이 유지되어야 한다."),
    Round287ScoreAdjustment("tourist_spend_per_head", 5, "raise", "관광객 수보다 객단가와 구매전환율이 중요하다."),
    Round287ScoreAdjustment("ecommerce_take_rate", 5, "raise", "플랫폼 규모는 take-rate과 margin으로 닫혀야 한다."),
    Round287ScoreAdjustment("data_trust_internal_control", 5, "raise", "이커머스는 데이터 신뢰와 내부통제가 Green gate다."),
    Round287ScoreAdjustment("fulfillment_unit_economics", 5, "raise", "물류 매출 증가는 건당 마진과 FCF 전환이 필요하다."),
    Round287ScoreAdjustment("domestic_consumption_sensitivity", 4, "raise", "내수 유통은 소비둔화 민감도를 RedTeam에 넣는다."),
    Round287ScoreAdjustment("viral_brand_headline_only", -5, "lower", "바이럴 브랜드 headline만으로 Stage 3-Green을 만들지 않는다."),
    Round287ScoreAdjustment("visitor_count_only", -5, "lower", "방문객 수만 있고 지출/마진이 없으면 event premium이다."),
    Round287ScoreAdjustment("online_ecommerce_growth_without_offline_sellthrough", -5, "lower", "온라인 성장만으로 오프라인 sell-through를 대체하지 않는다."),
    Round287ScoreAdjustment("JV_scale_without_take_rate", -5, "lower", "JV 규모와 고객 DB는 take-rate 전에는 Stage 2다."),
    Round287ScoreAdjustment("revenue_uplift_without_unit_economics", -5, "lower", "물류 매출 uplift는 unit economics 전에는 Green 금지다."),
    Round287ScoreAdjustment("IPO_or_stock_pop_without_repeat_purchase", -5, "lower", "IPO/주가 급등은 반복구매 전에는 4B-watch다."),
    Round287ScoreAdjustment("consumer_export_story_without_local_regulatory_fit", -4, "lower", "수출 브랜드는 현지 규제 적합성 게이트가 필요하다."),
    Round287ScoreAdjustment("domestic_retail_ignored", -4, "lower", "내수 소비 충격을 무시하면 유통 Green이 왜곡된다."),
    Round287ScoreAdjustment("data_breach_or_customer_trust_failure", -5, "lower", "데이터 유출과 고객 신뢰 훼손은 hard 4C 참고점이다."),
)


ROUND287_SHADOW_WEIGHT_ROWS: tuple[Round287ShadowWeightRow, ...] = (
    Round287ShadowWeightRow(E2RArchetype.K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE, 5, 5, 4, 1, 2, 0, 0, 1, 0, 1, -3, 4, 4, "Samyang/Nongshim need export sell-through, ASP, capacity conversion and regulatory fit."),
    Round287ShadowWeightRow(E2RArchetype.K_FOOD_EXPORT_REGULATORY_4C_WATCH, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, -4, 3, 5, "Food recall, spiciness and local health rules are RedTeam overlays."),
    Round287ShadowWeightRow(E2RArchetype.K_BEAUTY_DEVICE_BRAND_4B, 3, 5, 2, 4, 5, 0, 0, 2, 0, 0, -5, 5, 4, "APR-style device rerating needs repeat purchase, return-rate, tariff and margin proof."),
    Round287ShadowWeightRow(E2RArchetype.K_BEAUTY_US_EXPANSION_STAGE2, 4, 4, 2, 5, 5, 0, 0, 2, 0, 0, -5, 5, 4, "K-beauty U.S. growth is Stage 2 until physical sell-through and tariff absorption confirm."),
    Round287ShadowWeightRow(E2RArchetype.CHINA_TOURISM_RETAIL_EVENT_PREMIUM, 0, 0, 0, 0, 0, 5, 0, 1, 0, 4, -5, 5, 4, "Tourism policy needs spend-per-head, conversion and margin, not visitor count only."),
    Round287ShadowWeightRow(E2RArchetype.ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE, 0, 0, 0, 0, 0, 0, 5, 5, 3, 0, -5, 4, 5, "Gmarket/AliExpress JV needs take-rate, compliance, retention and fulfillment margin."),
    Round287ShadowWeightRow(E2RArchetype.ECOMMERCE_TRUST_BREAK_HARD_REFERENCE, 0, 0, 0, 0, 0, 0, 0, 5, 2, 0, -5, 4, 5, "Coupang breach is a hard trust reference; competitor read-through cannot create Green."),
    Round287ShadowWeightRow(E2RArchetype.RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2, 0, 0, 2, 0, 0, 0, 2, 2, 5, 1, -5, 4, 4, "CJ Logistics revenue uplift requires parcel economics and cash conversion."),
    Round287ShadowWeightRow(E2RArchetype.DOMESTIC_CONSUMPTION_SHOCK_4C_WATCH, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5, -4, 3, 5, "Domestic consumption shock is a RedTeam overlay for discretionary retail."),
)


ROUND287_DEEP_SUB_ARCHETYPES: tuple[Round287DeepSubArchetype, ...] = (
    Round287DeepSubArchetype("K-food export brand", E2RArchetype.K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE, ("Samyang", "Buldak", "Nongshim", "Shin Ramyun", "ASP", "U.S./Europe shipments", "capacity expansion")),
    Round287DeepSubArchetype("K-food regulatory watch", E2RArchetype.K_FOOD_EXPORT_REGULATORY_4C_WATCH, ("Denmark recall", "capsaicin", "spiciness", "local health regulation", "youth challenge risk")),
    Round287DeepSubArchetype("K-beauty device brand", E2RArchetype.K_BEAUTY_DEVICE_BRAND_4B, ("APR", "Medicube", "beauty device", "repeat purchase", "return rate", "tariff")),
    Round287DeepSubArchetype("K-beauty U.S. expansion", E2RArchetype.K_BEAUTY_US_EXPANSION_STAGE2, ("d'Alba", "Beauty of Joseon", "Tirtir", "Torriden", "COSRX", "Silicon2", "physical retail")),
    Round287DeepSubArchetype("China tourism retail", E2RArchetype.CHINA_TOURISM_RETAIL_EVENT_PREMIUM, ("Hyundai Department Store", "Hotel Shilla", "Hankook Cosmetics", "Paradise", "spend per head")),
    Round287DeepSubArchetype("cross-border e-commerce JV", E2RArchetype.ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE, ("Shinsegae", "E-Mart", "Gmarket", "Alibaba", "AliExpress", "take-rate", "data restriction")),
    Round287DeepSubArchetype("e-commerce trust break", E2RArchetype.ECOMMERCE_TRUST_BREAK_HARD_REFERENCE, ("Coupang", "data breach", "customer trust", "Naver", "Kurly", "CJ Logistics")),
    Round287DeepSubArchetype("retail fulfilment unit economics", E2RArchetype.RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2, ("CJ Logistics", "SSG.com", "fulfillment", "unit economics", "parcel margin")),
    Round287DeepSubArchetype("domestic consumption shock", E2RArchetype.DOMESTIC_CONSUMPTION_SHOCK_4C_WATCH, ("retail sales", "cars", "home appliances", "entertainment spending", "GDP", "won weakness")),
)


ROUND287_CASE_CANDIDATES: tuple[Round287CaseCandidate, ...] = (
    Round287CaseCandidate(
        case_id="r5_loop14_samyang_buldak_export_stage3_candidate",
        symbol="003230",
        company_name="Samyang Foods / Buldak export",
        primary_archetype=E2RArchetype.K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE,
        secondary_archetypes=(E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY, E2RArchetype.K_FOOD_EXPORT_RECURRING, E2RArchetype.K_FOOD_EXPORT_REGULATORY_4C_WATCH),
        case_type="structural_success",
        round_case_type="structural_success_candidate + regulatory 4C-watch",
        stage1_date=date(2024, 6, 14),
        stage2_date=date(2024, 6, 14),
        stage3_date=date(2024, 6, 14),
        stage4b_date=date(2024, 6, 14),
        stage4c_date=date(2024, 6, 12),
        stage3_decision="export_ASP_capacity_and_OP_revision_are_aligned_but_local_regulatory_fit_remains_gate",
        stage4b_status="4B-watch/brand-rerating; 4C-watch/local-regulatory-recall",
        hard_4c_confirmed=False,
        service_trust_hard_reference_confirmed=False,
        evidence_fields=("Buldak_ASP_increase", "US_Europe_shipments_growth", "capacity_expansion", "q2_OP_estimate_81_2bn_krw", "target_price_raise_26pct"),
        red_flag_fields=("regulatory_recall_local_health_issue", "denmark_recall_three_spicy_products", "capsaicin_spiciness_acute_poisoning_concern", "consumer_export_story_without_local_regulatory_fit"),
        price_data_source="MarketWatch/Dow Jones event anchor + AP Denmark recall anchor",
        reported_price_anchor="Shares closed +5.7% at 647,000 KRW; target price 830,000 KRW",
        reported_return_anchor="OP estimate +84% YoY, target price +26%, target upside 28.3%",
        event_mfe_pct=5.7,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=647000.0,
        stage4b_price_anchor=647000.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"q2_op_estimate_krw_bn": 81.2, "q2_op_estimate_yoy_growth_pct": 84, "target_price_krw": 830000, "target_price_raise_pct": 26, "target_upside_from_stage3_price_pct": 28.3, "denmark_recall_products_count": 3, "quality_defect_confirmed": False},
        score_price_alignment="aligned",
        round_alignment_label="aligned_partial",
        rerating_result="true_rerating",
        round_rerating_label="K_food_export_brand_stage3_candidate",
        stage_failure_type="green_success",
        round_stage_failure_label="export_brand_success_but_local_regulatory_fit_gate",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Samyang is the closest R5 Stage 3 candidate, but Denmark recall keeps regulatory fit as an explicit Green gate.",
    ),
    Round287CaseCandidate(
        case_id="r5_loop14_nongshim_shin_ramyun_global_expansion",
        symbol="004370",
        company_name="Nongshim / Shin Ramyun global expansion",
        primary_archetype=E2RArchetype.K_FOOD_EXPORT_BRAND_STAGE3_CANDIDATE,
        secondary_archetypes=(E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND, E2RArchetype.K_FOOD_EXPORT_RECURRING),
        case_type="success_candidate",
        round_case_type="success_candidate + insufficient_price_data",
        stage1_date=date(2024, 5, 27),
        stage2_date=date(2024, 5, 27),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="global_brand_sales_are_stage2_until_stock_price_sellthrough_margin_and_regional_offset_confirm",
        stage4b_status="watch/global-brand-stage2-not-green",
        hard_4c_confirmed=False,
        service_trust_hard_reference_confirmed=False,
        evidence_fields=("global_instant_noodle_market_50bn_usd", "Korean_exports_1bn_usd", "Shin_Ramyun_sales_1_2tn_krw", "overseas_sales_share_60pct", "US_sales_target_1_5bn_usd_2030"),
        red_flag_fields=("direct_stock_event_price_unavailable", "factory_utilization_unconfirmed", "gross_margin_unconfirmed", "China_slowdown_offset_unconfirmed"),
        price_data_source="FT brand/export anchor",
        reported_price_anchor="Direct listed event price unavailable",
        reported_return_anchor="Shin Ramyun sales 1.2T KRW; overseas share nearly 60%; U.S. sales target 1.5B USD by 2030",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"global_instant_noodle_market_usd_bn": 50, "korean_exports_prior_year_usd_bn": 1, "shin_ramyun_2023_sales_krw_trn": 1.2, "shin_ramyun_2023_sales_usd_mn": 883, "overseas_sales_share_pct": 60, "us_sales_target_2030_usd_bn": 1.5},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_price_data_unavailable",
        rerating_result="unknown",
        round_rerating_label="K_food_global_brand_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="global_brand_sales_not_event_price_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Nongshim has global brand evidence, but no event-day price anchor or margin/FCF bridge in this round.",
    ),
    Round287CaseCandidate(
        case_id="r5_loop14_apr_medicube_beauty_device_brand_4b",
        symbol="278470",
        company_name="APR / Medicube beauty device",
        primary_archetype=E2RArchetype.K_BEAUTY_DEVICE_BRAND_4B,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND_4B, E2RArchetype.BEAUTY_DEVICE_CONSUMER_CLINIC_CROSSOVER),
        case_type="success_candidate",
        round_case_type="structural_success_candidate + 4B-overheat",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 7, 1),
        stage3_date=None,
        stage4b_date=date(2025, 10, 1),
        stage4c_date=date(2025, 10, 1),
        stage3_decision="beauty_device_growth_is_stage2_until_repeat_purchase_return_rate_tariff_and_offline_sellthrough_confirm",
        stage4b_status="4B-watch/IPO-and-stock-pop-before-repeat-purchase; 4C-watch/tariff-return-rate",
        hard_4c_confirmed=False,
        service_trust_hard_reference_confirmed=False,
        evidence_fields=("market_cap_4_2bn_usd_July", "market_cap_6bn_usd_October", "stock_more_than_4x_since_January", "overseas_revenue_Q2_2025_80pct", "device_share_US_sales_one_third"),
        red_flag_fields=("IPO_or_stock_pop_without_repeat_purchase", "viral_tiktok_or_celebrity_before_repeat_purchase", "return_rate_unconfirmed", "tariff_absorption_unconfirmed"),
        price_data_source="FT reported valuation and stock-pop anchors",
        reported_price_anchor="Market cap about 4.2B USD in July and 6B USD in October",
        reported_return_anchor="Stock +75% since IPO in July context and more than 4x since January context",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"market_cap_july_usd_bn": 4.2, "market_cap_october_usd_bn": 6.0, "stock_gain_since_january_multiple": 4.0, "device_price_usd": 180, "overseas_revenue_share_q2_2025_pct": 80, "device_share_us_sales_pct": 33, "repeat_purchase_confirmed": False},
        score_price_alignment="aligned",
        round_alignment_label="aligned_partial_but_4B_watch",
        rerating_result="true_rerating",
        round_rerating_label="K_beauty_device_brand_4B",
        stage_failure_type="yellow_success",
        round_stage_failure_label="device_brand_success_but_repeat_purchase_and_tariff_gate",
        price_validation_status="reported_valuation_anchor_not_full_ohlc",
        notes="APR is useful as a K-beauty device success candidate and 4B-watch; repeat purchase and return-rate decide Green durability.",
    ),
    Round287CaseCandidate(
        case_id="r5_loop14_kbeauty_us_expansion_basket",
        symbol="483650/257720/090430/192820/161890",
        company_name="K-beauty U.S. expansion basket",
        primary_archetype=E2RArchetype.K_BEAUTY_US_EXPANSION_STAGE2,
        secondary_archetypes=(E2RArchetype.INDIE_K_BEAUTY_US_RETAIL_CHANNEL, E2RArchetype.K_BEAUTY_INDIE_PHYSICAL_STORE_TEST, E2RArchetype.K_BEAUTY_TARIFF_IMPORT_REVIEW),
        case_type="success_candidate",
        round_case_type="success_candidate + tariff/physical sell-through 4C-watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 6, 5),
        stage3_date=None,
        stage4b_date=date(2025, 6, 5),
        stage4c_date=date(2025, 6, 5),
        stage3_decision="US_K_beauty_growth_is_stage2_until_physical_store_sellthrough_tariff_absorption_and_working_capital_confirm",
        stage4b_status="4B-watch/K-beauty-online-growth-before-offline-sellthrough; 4C-watch/tariff",
        hard_4c_confirmed=False,
        service_trust_hard_reference_confirmed=False,
        evidence_fields=("Korea_US_cosmetics_export_rank_1_2024", "global_beauty_export_rank_3", "output_13bn_usd", "export_share_80pct", "top5_Korean_US_ecommerce_growth_71pct"),
        red_flag_fields=("online_ecommerce_growth_without_offline_sellthrough", "tariff_shock_not_absorbed", "physical_sellthrough_unconfirmed", "channel_inventory_or_sellthrough_failure"),
        price_data_source="Reuters/AP K-beauty export and tariff anchors",
        reported_price_anchor="d'Alba more than doubled since debut; full OHLC unavailable",
        reported_return_anchor="Top-five Korean U.S. e-commerce growth 71% over two years; U.S. market 21%; French top-five 15%",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"korea_us_cosmetics_export_rank_2024": 1, "global_beauty_export_rank": 3, "output_usd_bn": 13, "export_share_pct": 80, "top5_korean_us_ecommerce_growth_2y_pct": 71, "us_market_growth_pct": 21, "french_top5_growth_pct": 15, "ap_imports_usd_bn": 1.7, "imports_growth_pct": 54, "tariff_current_pct": 10, "tariff_risk_pct": 25, "physical_sellthrough_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_but_offline_sellthrough_unproven",
        rerating_result="unknown",
        round_rerating_label="K_beauty_US_expansion_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="online_growth_not_physical_sellthrough_green",
        price_validation_status="reported_growth_anchor_not_full_ohlc",
        notes="K-beauty U.S. expansion is a Stage 2 path; physical-store sell-through and tariff absorption decide upgrade.",
    ),
    Round287CaseCandidate(
        case_id="r5_loop14_china_tourism_retail_event_premium",
        symbol="069960/008770/123690/034230/004170",
        company_name="China tourism retail/dutyfree/beauty event basket",
        primary_archetype=E2RArchetype.CHINA_TOURISM_RETAIL_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.CHINA_TOURISM_DUTYFREE_RETAIL_EVENT, E2RArchetype.TOURISM_RETAIL_DUTYFREE_EVENT, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE),
        case_type="event_premium",
        round_case_type="tourism_event_premium + 4B-watch",
        stage1_date=date(2025, 3, 20),
        stage2_date=date(2025, 8, 6),
        stage3_date=None,
        stage4b_date=date(2025, 8, 6),
        stage4c_date=None,
        stage3_decision="visa_free_tourism_is_event_premium_until_spend_per_head_conversion_and_margin_confirm",
        stage4b_status="4B-watch/tourism-visa-headline-before-spend",
        hard_4c_confirmed=False,
        service_trust_hard_reference_confirmed=False,
        evidence_fields=("visa_free_policy_period_2025_09_29_to_2026_06", "visitor_count_2024_16_4m", "visitor_yoy_growth_48pct", "Chinese_visitor_share_28pct", "visitor_target_2025_18_5m"),
        red_flag_fields=("visitor_count_only", "tourist_arrivals_without_spending_conversion", "spend_per_head_unconfirmed", "margin_unconfirmed"),
        price_data_source="reported tourism policy basket event-return anchors",
        reported_price_anchor="Hyundai Department +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%",
        reported_return_anchor="Visitor-count and visa headline moved basket, but spend/conversion/margin were not confirmed",
        event_mfe_pct=9.9,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"visa_free_start": "2025-09-29", "visa_free_end": "2026-06", "visitors_2024_mn": 16.4, "visitor_yoy_growth_pct": 48, "chinese_visitor_share_pct": 28, "visitor_target_2025_mn": 18.5, "hyundai_department_event_mfe_pct": 7.1, "hotel_shilla_event_mfe_pct": 4.8, "paradise_event_mfe_pct": 2.9, "hankook_cosmetics_event_mfe_pct": 9.9, "spend_conversion_margin_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_visitor_count_not_spend",
        rerating_result="event_premium",
        round_rerating_label="China_tourism_retail_event_premium",
        stage_failure_type="false_yellow",
        round_stage_failure_label="visitor_count_not_spend_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Tourism policy can move a basket, but R5 Green needs spend per head, conversion and margin.",
    ),
    Round287CaseCandidate(
        case_id="r5_loop14_shinsegae_emart_alibaba_gmarket_jv_data_gate",
        symbol="004170/139480",
        company_name="Shinsegae / E-Mart / Alibaba-Gmarket JV",
        primary_archetype=E2RArchetype.ECOMMERCE_CROSS_BORDER_JV_STAGE2_DATA_GATE,
        secondary_archetypes=(E2RArchetype.CROSS_BORDER_ECOMMERCE_DATA_GATE, E2RArchetype.ECOMMERCE_JV_SCALE_DATA_GATE, E2RArchetype.RETAIL_PLATFORM_DATA_REGULATION_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate + data gate",
        stage1_date=date(2024, 12, 26),
        stage2_date=date(2025, 9, 18),
        stage3_date=None,
        stage4b_date=date(2024, 12, 26),
        stage4c_date=date(2025, 9, 18),
        stage3_decision="JV_scale_is_stage2_until_take_rate_GMV_fulfillment_margin_and_data_compliance_confirm",
        stage4b_status="4B-watch/JV-scale-before-take-rate; 4C-watch/data-sharing-restriction",
        hard_4c_confirmed=False,
        service_trust_hard_reference_confirmed=False,
        evidence_fields=("JV_value_4bn_usd", "E_Mart_Gmarket_100pct_contribution", "customer_database_50m", "expected_cross_border_share_41pct", "KFTC_conditional_approval"),
        red_flag_fields=("JV_scale_without_take_rate", "data_sharing_restriction_three_years", "take_rate_unconfirmed", "fulfillment_margin_unconfirmed"),
        price_data_source="reported JV, KFTC and cross-border market anchors",
        reported_price_anchor="JV valued about 4B USD; full listed price anchor unavailable",
        reported_return_anchor="Expected cross-border market share 41%; data sharing restricted for three years",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"JV_value_usd_bn": 4.0, "customer_database_mn": 50, "data_sharing_restriction_years": 3, "expected_cross_border_market_share_pct": 41, "korea_china_online_import_spending_2024_krw_trn": 4.7, "spending_growth_pct": 32, "alibaba_share_pct": 62, "take_rate_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_data_gate",
        rerating_result="policy_event_rerating",
        round_rerating_label="ecommerce_cross_border_JV_stage2_data_gate",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="JV_scale_not_take_rate_green",
        price_validation_status="reported_JV_anchor_not_full_ohlc",
        notes="Gmarket/AliExpress JV is Stage 2 until take-rate, GMV, data compliance and fulfilment economics prove FCF.",
    ),
    Round287CaseCandidate(
        case_id="r5_loop14_coupang_data_breach_retail_trust_hard_reference",
        symbol="CPNG/035420/139480/000120_readthrough",
        company_name="Coupang data breach / retail trust hard reference",
        primary_archetype=E2RArchetype.ECOMMERCE_TRUST_BREAK_HARD_REFERENCE,
        secondary_archetypes=(E2RArchetype.ECOMMERCE_TRUST_BREACH_HARD_4C, E2RArchetype.ECOMMERCE_SERVICE_TRUST_HARD_REFERENCE),
        case_type="4c_thesis_break",
        round_case_type="hard 4C service trust reference",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 2, 25),
        stage3_decision="customer_trust_break_is_hard_reference_and_competitor_readthrough_cannot_create_green",
        stage4b_status="hard-4C/data-breach-customer-trust-break; competitor-readthrough-not-Green",
        hard_4c_confirmed=True,
        service_trust_hard_reference_confirmed=True,
        evidence_fields=("affected_users_34m", "names_phone_shipping_address_exposed", "management_failure_not_sophisticated_attack", "CPNG_shares_down_34pct", "spending_and_estimate_cuts"),
        red_flag_fields=("data_breach_customer_trust_break", "data_breach_or_customer_trust_failure", "management_control_failure", "competitor_readthrough_after_trust_event"),
        price_data_source="reported breach, spending and competitor read-through anchors",
        reported_price_anchor="CPNG shares -34%; daily spending -6.3%; revenue estimate cut -2.2%; core earnings cut -6.7%",
        reported_return_anchor="Naver users +23% and CJ Logistics volume +120% are read-through, not automatic Green",
        event_mfe_pct=None,
        event_mae_pct=-34.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"affected_users_mn": 34, "payment_or_login_exposed": False, "CPNG_share_decline_pct": -34, "mobile_user_activity_decline_pct": -3.5, "daily_spending_decline_pct": -6.3, "spending_krw_bn": 139.2, "revenue_estimate_cut_pct": -2.2, "core_earnings_cut_pct": -6.7, "naver_user_gain_pct": 23, "cj_logistics_volume_gain_pct": 120, "competitor_stage3_allowed": False},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="ecommerce_trust_break_hard_reference",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="data_trust_break_blocks_green_and_readthrough",
        price_validation_status="reported_breach_anchor_not_full_ohlc",
        notes="Coupang breach is the hard trust reference: competitor traffic gain must still prove GMV and margin before any positive stage.",
    ),
    Round287CaseCandidate(
        case_id="r5_loop14_cj_logistics_shinsegae_fulfillment_unit_economics",
        symbol="000120",
        company_name="CJ Logistics / Shinsegae fulfilment",
        primary_archetype=E2RArchetype.RETAIL_FULFILLMENT_UNIT_ECONOMICS_STAGE2,
        secondary_archetypes=(E2RArchetype.RETAIL_ECOMMERCE_LOGISTICS, E2RArchetype.ECOMMERCE_LOGISTICS_REPEAT_CONTRACT, E2RArchetype.LIFE_SERVICE_LOGISTICS_CONTRACT_STAGE2),
        case_type="failed_rerating",
        round_case_type="stage2_candidate_but_price_failed",
        stage1_date=date(2024, 6, 17),
        stage2_date=date(2024, 6, 17),
        stage3_date=None,
        stage4b_date=date(2024, 6, 17),
        stage4c_date=None,
        stage3_decision="fulfillment_revenue_uplift_is_stage2_until_unit_economics_margin_and_cash_conversion_confirm",
        stage4b_status="watch/revenue-uplift-before-unit-economics",
        hard_4c_confirmed=False,
        service_trust_hard_reference_confirmed=False,
        evidence_fields=("annual_revenue_uplift_300bn_krw", "three_year_partnership", "Shinsegae_SSG_dot_com_contract", "target_price_116000_krw"),
        red_flag_fields=("revenue_uplift_without_unit_economics", "local_growth_slower", "overseas_recovery_delay", "unit_economics_unconfirmed"),
        price_data_source="reported target-price and event-price anchors",
        reported_price_anchor="Event price 99,100 KRW; target 116,000 KRW; target cut -17%",
        reported_return_anchor="Annual revenue uplift 300B KRW, but event return -0.2%",
        event_mfe_pct=None,
        event_mae_pct=-0.2,
        stage1_price_anchor=99100.0,
        stage2_price_anchor=99100.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"annual_revenue_uplift_krw_bn": 300, "partnership_years": 3, "target_price_krw": 116000, "target_cut_pct": -17, "event_price_krw": 99100, "event_return_pct": -0.2, "target_upside_pct": 17.1, "unit_economics_confirmed": False},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        round_rerating_label="retail_fulfillment_unit_economics_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="revenue_uplift_not_unit_economics_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="CJ Logistics has revenue uplift evidence, but weak event return and missing unit economics keep it below Green.",
    ),
    Round287CaseCandidate(
        case_id="r5_loop14_domestic_retail_sales_shock_4c_watch",
        symbol="023530/139480/004170/069960/066570_discretionary_basket",
        company_name="Domestic retail sales shock discretionary basket",
        primary_archetype=E2RArchetype.DOMESTIC_CONSUMPTION_SHOCK_4C_WATCH,
        secondary_archetypes=(E2RArchetype.RETAIL_DOMESTIC_CONSUMER, E2RArchetype.DISCOUNT_PROMOTION_MARGIN_OVERLAY, E2RArchetype.POLITICAL_SHOCK_KOREA_DISCOUNT_HARD_GATE),
        case_type="failed_rerating",
        round_case_type="domestic consumption 4C-watch",
        stage1_date=date(2024, 12, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 2, 3),
        stage3_decision="domestic_discretionary_retail_should_not_ignore_consumption_shock",
        stage4b_status="4C-watch/domestic-consumption-shock-discretionary-decline",
        hard_4c_confirmed=False,
        service_trust_hard_reference_confirmed=False,
        evidence_fields=("December_retail_sales_down_0_6pct_mom", "four_months_no_retail_growth", "cars_home_appliances_down_4_1pct", "entertainment_spending_down_0_6pct", "Q4_GDP_0_1pct"),
        red_flag_fields=("domestic_retail_ignored", "domestic_consumption_shock_discretionary_decline", "won_15_year_low_context", "discretionary_margin_pressure"),
        price_data_source="reported macro and retail-sales anchors",
        reported_price_anchor="No individual OHLC anchor; retail-sales shock reference",
        reported_return_anchor="Dec retail sales -0.6% MoM; cars/home appliances -4.1%; entertainment -0.6%; Q4 GDP 0.1%",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"dec_retail_sales_mom_pct": -0.6, "months_without_retail_growth": 4, "cars_home_appliances_pct": -4.1, "entertainment_spending_pct": -0.6, "q4_gdp_pct": 0.1, "won_15_year_low_context": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="domestic_consumption_shock_watch",
        rerating_result="thesis_break",
        round_rerating_label="domestic_consumption_shock_4C_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="domestic_retail_shock_must_block_discretionary_green",
        price_validation_status="macro_anchor_not_stock_ohlc",
        notes="Domestic consumption shock is a RedTeam overlay; export/tourism headlines must not hide weak discretionary demand.",
    ),
)


def round287_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND287_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND287_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round287 R5 Loop-14 consumer/retail/brand price-validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=candidate.evidence_fields if candidate.stage3_date else (),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("rerating", "pop", "headline", "visitor", "jv", "valuation", "readthrough", "price"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("recall", "tariff", "breach", "trust", "shock", "restriction", "decline", "4c", "domestic", "regulatory"))),
            must_have_fields=ROUND287_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type not in {"structural_success", "success_candidate"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND287_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "round287_service_trust_hard_reference_true",
                "do_not_use_round287_cases_as_candidate_generation_input",
                "do_not_treat_K_food_K_beauty_tourism_or_JV_headlines_as_green",
                "do_not_invent_price_or_stage_dates",
                *ROUND287_GREEN_REQUIRED_FIELDS,
                *ROUND287_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.event_mfe_pct,
                mae_30d=candidate.event_mae_pct,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.event_mfe_pct is not None
                    or candidate.event_mae_pct is not None
                    or candidate.stage1_price_anchor is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.84 if "unavailable" not in candidate.price_validation_status else 0.72,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round287_case_rows() -> tuple[dict[str, str], ...]:
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
            "service_trust_hard_reference_confirmed": str(candidate.service_trust_hard_reference_confirmed).lower(),
            "price_data_source": candidate.price_data_source,
            "reported_price_anchor": candidate.reported_price_anchor,
            "reported_return_anchor": candidate.reported_return_anchor,
            "event_mfe_pct": _float_text(candidate.event_mfe_pct),
            "event_mae_pct": _float_text(candidate.event_mae_pct),
            "stage1_price_anchor": _float_text(candidate.stage1_price_anchor),
            "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
            "stage3_price_anchor": _float_text(candidate.stage3_price_anchor),
            "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
            "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
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
        for candidate in ROUND287_CASE_CANDIDATES
    )


def round287_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND287_SCORE_ADJUSTMENTS)


def round287_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND287_SHADOW_WEIGHT_ROWS)


def round287_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND287_DEEP_SUB_ARCHETYPES)


def round287_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round287_price_validation": "true"} for field in ROUND287_PRICE_VALIDATION_FIELDS)


def round287_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round287_label": label, "canonical_archetype": canonical} for label, canonical in ROUND287_REQUIRED_TARGET_ALIASES.items())


def round287_summary() -> dict[str, int | bool | str]:
    cases = ROUND287_CASE_CANDIDATES
    return {
        "source_round": ROUND287_SOURCE_ROUND_PATH,
        "round_id": ROUND287_ANALYST_ROUND_ID,
        "large_sector": ROUND287_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "service_trust_hard_reference_count": sum(1 for case in cases if case.service_trust_hard_reference_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "unknown_alignment_count": sum(1 for case in cases if case.score_price_alignment == "unknown"),
        "aligned_count": sum(1 for case in cases if case.score_price_alignment == "aligned"),
        "target_archetype_count": len(ROUND287_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND287_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND287_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
        "service_trust_hard_reference_confirmed": any(case.service_trust_hard_reference_confirmed for case in cases),
    }


def round287_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND287_SOURCE_ROUND_PATH,
        "round_id": ROUND287_ANALYST_ROUND_ID,
        "large_sector": ROUND287_LARGE_SECTOR,
        "summary": round287_summary(),
        "target_aliases": dict(ROUND287_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND287_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND287_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND287_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND287_HARD_4C_GATES),
        "score_adjustments": list(round287_score_adjustment_rows()),
        "shadow_weights": list(round287_shadow_weight_rows()),
        "deep_sub_archetypes": list(round287_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND287_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round287_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_K_food_K_beauty_tourism_or_JV_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round287_summary_markdown() -> str:
    summary = round287_summary()
    lines = [
        "# Round 287 R5 Loop 14 Consumer Retail Brand Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- Stage 3 dated candidates: {summary['stage3_case_count']}",
        f"- stage4b_watch: {summary['stage4b_watch_count']}",
        f"- stage4c_watch: {summary['stage4c_watch_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- service_trust_hard_reference: {summary['service_trust_hard_reference_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND287_CASE_CANDIDATES:
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
            "- Samyang/Buldak is the closest R5 Stage 3 candidate, but local regulatory fit remains a Green gate.",
            "- Nongshim and K-beauty U.S. expansion are Stage 2 paths until price, sell-through, margin and tariff evidence close.",
            "- Tourism and JV scale are event premium or Stage 2 until spend-per-head, take-rate and compliance are proven.",
            "- Coupang data breach is a hard trust reference; competitor read-through cannot become Green by itself.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round287_green_gate_review_markdown() -> str:
    lines = [
        "# Round 287 R5 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R5 Stage 3-Green is not `K-food`, `K-beauty`, `tourism`, `JV`, or `brand` as a label. It requires sell-through, ASP, capacity-to-revenue conversion, tariff/regulatory fit, take-rate, data trust, fulfilment unit economics and price-path evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND287_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND287_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND287_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Buldak export` can be Stage 3-like only when ASP, shipments, capacity and OP revision all close; a local recall stays as a 4C-watch.",
            "- `K-beauty U.S. growth` is Stage 2 until physical-store sell-through and tariff absorption are visible.",
            "- `tourist visa-free policy` can move stocks, but without spend per head and margin it remains event premium.",
            "- `Gmarket/AliExpress JV` is Stage 2 until take-rate, compliance and fulfillment margin are proven.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round287_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 287 R5 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND287_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND287_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | service trust reference | interpretation |", "|---|---|---|---|---|---|"])
    for case in ROUND287_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {str(case.service_trust_hard_reference_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round287_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 287 R5 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, full MFE/MAE, sell-through, tariff absorption, take-rate, unit economics, data trust, spend conversion, or stage dates where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND287_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND287_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round287_r5_loop14_reports(
    output_directory: str | Path = ROUND287_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND287_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND287_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round287_case_records(), cases_path),
        "audit": _write_json(round287_audit_payload(), audit_path),
        "summary": output / "round287_r5_loop14_price_validation_summary.md",
        "case_matrix": output / "round287_r5_loop14_case_matrix.csv",
        "target_aliases": output / "round287_r5_loop14_target_aliases.csv",
        "score_adjustments": output / "round287_r5_loop14_score_adjustments.csv",
        "shadow_weights": output / "round287_r5_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round287_r5_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round287_r5_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round287_r5_loop14_green_gate_review.md",
        "price_validation_plan": output / "round287_r5_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round287_r5_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round287_summary_markdown(), encoding="utf-8")
    _write_csv(round287_case_rows(), paths["case_matrix"])
    _write_csv(round287_target_alias_rows(), paths["target_aliases"])
    _write_csv(round287_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round287_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round287_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round287_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round287_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round287_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round287_stage4b_4c_review_markdown(), encoding="utf-8")
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


__all__ = [
    "ROUND287_CASE_CANDIDATES",
    "ROUND287_GREEN_FORBIDDEN_PATTERNS",
    "ROUND287_GREEN_REQUIRED_FIELDS",
    "ROUND287_HARD_4C_GATES",
    "ROUND287_LARGE_SECTOR",
    "ROUND287_PRICE_VALIDATION_FIELDS",
    "ROUND287_REQUIRED_TARGET_ALIASES",
    "ROUND287_SHADOW_WEIGHT_ROWS",
    "ROUND287_STAGE4B_WATCH_TRIGGERS",
    "render_round287_green_gate_review_markdown",
    "render_round287_stage4b_4c_review_markdown",
    "round287_audit_payload",
    "round287_case_records",
    "round287_case_rows",
    "round287_deep_sub_archetype_rows",
    "round287_shadow_weight_rows",
    "round287_summary",
    "write_round287_r5_loop14_reports",
]
