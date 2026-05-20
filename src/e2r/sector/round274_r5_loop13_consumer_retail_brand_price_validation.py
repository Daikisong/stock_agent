"""Round-274 R5 Loop-13 consumer/retail/brand price-validation pack.

This module converts ``docs/round/round_274.md`` into structured,
calibration-only records and reports. It intentionally does not change
production scoring, candidate generation, or StageClassifier thresholds.

Easy example: a beauty brand entering Ulta or a celebrity eating chicken can
move prices, but R5 Green needs repeat purchase, sell-through, SSS, gross
margin, inventory discipline, data trust, and cash conversion.
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


ROUND274_SOURCE_ROUND_PATH = "docs/round/round_274.md"
ROUND274_ANALYST_ROUND_ID = "round_202"
ROUND274_LARGE_SECTOR = Round10LargeSector.CONSUMER_RETAIL_BRAND.value
ROUND274_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round274_r5_loop13_consumer_retail_brand_price_validation"
ROUND274_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r5_loop13_round274.jsonl"
ROUND274_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round274_r5_loop13_consumer_retail_brand_price_validation_audit.json"

ROUND274_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "K_BEAUTY_DEVICE_GLOBAL_BRAND_4B": E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND_4B.value,
    "INDIE_K_BEAUTY_US_RETAIL_CHANNEL": E2RArchetype.INDIE_K_BEAUTY_US_RETAIL_CHANNEL.value,
    "H_AND_B_PLATFORM_GLOBALIZATION": E2RArchetype.H_AND_B_PLATFORM_GLOBALIZATION.value,
    "K_FOOD_EXPORT_ASP_CAPACITY": E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY.value,
    "CHINA_TOURISM_DUTYFREE_RETAIL_EVENT": E2RArchetype.CHINA_TOURISM_DUTYFREE_RETAIL_EVENT.value,
    "CROSS_BORDER_ECOMMERCE_DATA_GATE": E2RArchetype.CROSS_BORDER_ECOMMERCE_DATA_GATE.value,
    "GROCERY_RETAIL_CREDIT_4C_REFERENCE": E2RArchetype.GROCERY_RETAIL_CREDIT_4C_REFERENCE.value,
    "CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM": E2RArchetype.CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM.value,
}

ROUND274_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "repeat_purchase_confirmed",
    "physical_store_sellthrough_confirmed",
    "same_store_sales_confirmed",
    "gross_margin_after_tariff_confirmed",
    "inventory_discipline_confirmed",
    "channel_reorder_rate_confirmed",
    "parent_value_bridge_confirmed",
    "data_governance_passed",
    "franchise_margin_confirmed",
    "cash_conversion_confirmed",
    "price_path_after_evidence",
)

ROUND274_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "viral_social_media_only",
    "celebrity_event_only",
    "tourist_arrival_headline_only",
    "IPO_or_debut_pop_only",
    "channel_talks_without_sellthrough",
    "unlisted_subsidiary_readthrough_only",
    "gross_margin_before_tariff_pass",
    "data_sharing_regulatory_risk",
    "offline_retail_credit_stress",
)

ROUND274_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "beauty_stock_2x_to_4x_before_repeat_purchase_margin_proof",
    "IPO_or_debut_pop_above_100pct",
    "tourism_dutyfree_basket_plus_5_to_10pct_on_policy_headline",
    "celebrity_food_service_event_plus_20_to_30pct",
    "us_retail_channel_talks_before_sellthrough",
    "parent_company_rally_on_unlisted_platform_value",
    "cross_border_jv_premium_before_data_compliance",
)

ROUND274_HARD_4C_GATES: tuple[str, ...] = (
    "food_safety_recall",
    "input_cost_shock_without_pass_through",
    "retail_credit_restructuring",
    "data_governance_violation",
    "tourism_policy_reversal",
    "china_korea_diplomatic_shock",
    "inventory_build_or_channel_stuffing",
    "franchise_margin_collapse",
    "celebrity_event_fade",
)

ROUND274_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "business_anchor",
    "sellthrough_or_reorder_anchor",
    "gross_margin_or_tariff_anchor",
    "data_or_credit_gate",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round274ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round274ShadowWeightRow:
    archetype: E2RArchetype
    repeat_purchase: int
    physical_store_sellthrough: int
    same_store_sales: int
    gross_margin_after_tariff: int
    inventory_discipline: int
    channel_reorder_rate: int
    parent_value_bridge: int
    data_governance: int
    franchise_margin: int
    cash_conversion: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "repeat_purchase": _signed(self.repeat_purchase),
            "physical_store_sellthrough": _signed(self.physical_store_sellthrough),
            "same_store_sales": _signed(self.same_store_sales),
            "gross_margin_after_tariff": _signed(self.gross_margin_after_tariff),
            "inventory_discipline": _signed(self.inventory_discipline),
            "channel_reorder_rate": _signed(self.channel_reorder_rate),
            "parent_value_bridge": _signed(self.parent_value_bridge),
            "data_governance": _signed(self.data_governance),
            "franchise_margin": _signed(self.franchise_margin),
            "cash_conversion": _signed(self.cash_conversion),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round274DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round274CaseCandidate:
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
    direct_listed_hard_4c_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    event_mfe_pct: float | None
    event_mae_pct: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    peak_return_from_stage3_pct: float | None
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


ROUND274_SCORE_ADJUSTMENTS: tuple[Round274ScoreAdjustment, ...] = (
    Round274ScoreAdjustment("repeat_purchase", 5, "raise", "R5 Green은 유행보다 반복구매가 먼저다."),
    Round274ScoreAdjustment("physical_store_sellthrough", 5, "raise", "입점이나 채널 협의보다 실제 sell-through와 리오더를 본다."),
    Round274ScoreAdjustment("same_store_sales", 5, "raise", "관광객·유명인 이벤트는 SSS로 닫혀야 한다."),
    Round274ScoreAdjustment("gross_margin_after_tariff", 5, "raise", "관세와 가격전가 이후의 gross margin이 중요하다."),
    Round274ScoreAdjustment("inventory_discipline", 5, "raise", "재고가 쌓이면 sell-in일 수 있다."),
    Round274ScoreAdjustment("channel_reorder_rate", 5, "raise", "채널 리오더는 일회성 viral을 걸러낸다."),
    Round274ScoreAdjustment("parent_value_bridge", 4, "raise", "비상장 자회사는 상장 모회사 이익 연결고리가 필요하다."),
    Round274ScoreAdjustment("data_governance", 5, "raise", "플랫폼은 데이터 규제와 신뢰가 Green gate다."),
    Round274ScoreAdjustment("franchise_margin", 4, "raise", "외식은 유명인 방문보다 가맹점 마진을 본다."),
    Round274ScoreAdjustment("cash_conversion", 5, "raise", "매출 성장이 FCF로 닫혀야 한다."),
    Round274ScoreAdjustment("viral_social_media_only", -5, "lower", "TikTok/유명인 노출만으로 Green 금지다."),
    Round274ScoreAdjustment("celebrity_event_only", -5, "lower", "유명인이 먹었다는 장면은 매출 증거가 아니다."),
    Round274ScoreAdjustment("tourist_arrival_headline_only", -5, "lower", "관광객 headline은 spend와 margin 전에는 event premium이다."),
    Round274ScoreAdjustment("IPO_or_debut_pop_only", -5, "lower", "상장 직후 2배는 sell-through 전이면 4B-watch다."),
    Round274ScoreAdjustment("channel_talks_without_sellthrough", -5, "lower", "Costco/Ulta/Target 협의는 실제 매장 회전 전에는 Stage 2다."),
    Round274ScoreAdjustment("unlisted_subsidiary_readthrough_only", -4, "lower", "Olive Young처럼 비상장 자회사 가치는 parent bridge가 필요하다."),
    Round274ScoreAdjustment("data_sharing_regulatory_risk", -5, "lower", "데이터 공유 제한은 플랫폼 Green을 막는 핵심 리스크다."),
    Round274ScoreAdjustment("offline_retail_credit_stress", -5, "lower", "오프라인 점포망이 커도 credit stress면 thesis break다."),
)


ROUND274_SHADOW_WEIGHT_ROWS: tuple[Round274ShadowWeightRow, ...] = (
    Round274ShadowWeightRow(E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND_4B, 5, 4, 3, 5, 5, 5, 2, 2, 0, 5, -4, 5, 3, "APR device economics are strong, but >4x rally requires repeat purchase and margin proof."),
    Round274ShadowWeightRow(E2RArchetype.INDIE_K_BEAUTY_US_RETAIL_CHANNEL, 5, 5, 3, 5, 5, 5, 2, 2, 0, 5, -5, 5, 3, "d'Alba/K-beauty channel talks need physical-store sell-through and reorder proof."),
    Round274ShadowWeightRow(E2RArchetype.H_AND_B_PLATFORM_GLOBALIZATION, 5, 5, 5, 5, 5, 5, 5, 4, 0, 5, -4, 5, 3, "Olive Young platform value needs parent bridge and U.S. unit economics."),
    Round274ShadowWeightRow(E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY, 5, 5, 4, 5, 5, 5, 1, 1, 2, 5, -2, 4, 4, "Samyang export/ASP/capacity aligned; recall and input-cost risks remain."),
    Round274ShadowWeightRow(E2RArchetype.CHINA_TOURISM_DUTYFREE_RETAIL_EVENT, 4, 5, 5, 4, 5, 4, 2, 2, 0, 5, -5, 5, 4, "Tourist-flow event requires spend, SSS, hotel occupancy and margin."),
    Round274ShadowWeightRow(E2RArchetype.CROSS_BORDER_ECOMMERCE_DATA_GATE, 5, 4, 4, 4, 5, 5, 3, 5, 0, 5, -4, 4, 5, "Shinsegae-Ali JV needs data compliance and GMV/take-rate proof."),
    Round274ShadowWeightRow(E2RArchetype.GROCERY_RETAIL_CREDIT_4C_REFERENCE, 3, 3, 5, 4, 5, 3, 0, 3, 0, 5, 0, 3, 5, "Homeplus shows offline retail credit stress is hard reference."),
    Round274ShadowWeightRow(E2RArchetype.CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM, 1, 0, 5, 3, 3, 1, 0, 1, 5, 3, -5, 5, 3, "Kyochon/Cherrybro Jensen event is price_moved_without_evidence."),
)


ROUND274_DEEP_SUB_ARCHETYPES: tuple[Round274DeepSubArchetype, ...] = (
    Round274DeepSubArchetype("K-beauty device", E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND_4B, ("APR", "Medicube", "beauty device", "celebrity TikTok", "tariff risk")),
    Round274DeepSubArchetype("indie K-beauty U.S. retail", E2RArchetype.INDIE_K_BEAUTY_US_RETAIL_CHANNEL, ("d'Alba", "Tirtir", "Sephora", "Ulta", "Costco", "Target", "sell-through")),
    Round274DeepSubArchetype("H&B platform", E2RArchetype.H_AND_B_PLATFORM_GLOBALIZATION, ("CJ Olive Young", "U.S. store", "online GMV", "parent value bridge")),
    Round274DeepSubArchetype("K-food ASP capacity", E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY, ("Samyang", "Buldak", "ASP", "capacity", "recall", "packaging cost")),
    Round274DeepSubArchetype("China tourism retail", E2RArchetype.CHINA_TOURISM_DUTYFREE_RETAIL_EVENT, ("Hotel Shilla", "Hyundai Department Store", "Shinsegae", "Chinese visa-free", "duty-free spend")),
    Round274DeepSubArchetype("cross-border e-commerce data", E2RArchetype.CROSS_BORDER_ECOMMERCE_DATA_GATE, ("Shinsegae", "Gmarket", "AliExpress", "50M customers", "data sharing ban")),
    Round274DeepSubArchetype("grocery retail credit", E2RArchetype.GROCERY_RETAIL_CREDIT_4C_REFERENCE, ("Homeplus", "MBK", "liquidation value", "court-led restructuring")),
    Round274DeepSubArchetype("celebrity food-service event", E2RArchetype.CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM, ("Kyochon", "Cherrybro", "Neuromeka", "Jensen Huang", "Kkanbu Chicken")),
)


ROUND274_CASE_CANDIDATES: tuple[Round274CaseCandidate, ...] = (
    Round274CaseCandidate(
        case_id="r5_loop13_apr_medicube_kbeauty_device_4b",
        symbol="278470",
        company_name="APR / Medicube",
        primary_archetype=E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND_4B,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_DEVICE_GLOBAL_BRAND, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="success_candidate",
        round_case_type="structural_success_candidate_plus_4B_watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 10, 20),
        stage3_date=None,
        stage4b_date=date(2025, 10, 20),
        stage4c_date=None,
        stage3_decision="device_revenue_conversion_is_strong_but_green_requires_repeat_purchase_replacement_cycle_margin_channel_durability_and_tariff_pass_through",
        stage4b_status="4B-watch/fourfold-rerating-before-repeat-purchase-proof",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("stock_more_than_fourfold_since_january_2025", "market_value_about_6bn_usd", "device_price_180_usd", "device_about_one_third_us_sales", "overseas_revenue_nearly_80pct_q2", "us_revenue_nearly_30pct", "revenue_7x_since_2018"),
        red_flag_fields=("fourfold_rerating_before_repeat_purchase_proof", "single_device_concentration", "tariff_pass_through_untested", "channel_durability_unconfirmed"),
        price_data_source="FT APR / Medicube reported return and business anchors",
        reported_price_anchor="Market value about $6B; $180 facial skincare device",
        reported_return_anchor="Stock price more than four-fold since January 2025",
        event_mfe_pct=300.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"reported_stock_return_since_jan_2025_pct": 300.0, "market_value_usd_bn": 6.0, "device_price_usd": 180.0, "device_share_of_us_sales": "about_one_third", "q2_overseas_revenue_share_pct": 80.0, "us_revenue_share_pct": 30.0, "revenue_growth_since_2018_multiple": 7.0, "us_tariff_on_korean_cosmetics_pct": 15.0, "price_increase_plan": "not_planning_to_raise_prices_at_source_date"},
        score_price_alignment="aligned",
        round_alignment_label="aligned_partial_but_4B_watch",
        rerating_result="true_rerating",
        round_rerating_label="K_beauty_device_structural_candidate",
        stage_failure_type="yellow_success",
        round_stage_failure_label="fourfold_rerating_requires_repeat_purchase_margin_check",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Device brand economics look strong, but a fourfold rerating needs repeat purchase, channel durability and margin proof.",
    ),
    Round274CaseCandidate(
        case_id="r5_loop13_dalba_indie_kbeauty_us_channel",
        symbol="483650/257720/090430/192820",
        company_name="d'Alba Global / Silicon2 / Amorepacific / Cosmax-Kolmar read-through",
        primary_archetype=E2RArchetype.INDIE_K_BEAUTY_US_RETAIL_CHANNEL,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_INDIE_BRAND_US_CHANNEL, E2RArchetype.K_BEAUTY_INDIE_PHYSICAL_STORE_TEST),
        case_type="success_candidate",
        round_case_type="success_candidate_plus_overheat",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 6, 5),
        stage3_date=None,
        stage4b_date=date(2025, 6, 5),
        stage4c_date=None,
        stage3_decision="us_retail_shelf_access_is_stage2_until_physical_store_sellthrough_reorder_gross_margin_after_tariffs_and_inventory_discipline_confirm",
        stage4b_status="4B-watch/debut-pop-before-sellthrough",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("dalba_shares_more_than_doubled_since_debut", "costco_ulta_target_talks", "tirtir_aims_to_double_us_sales", "beauty_of_joseon_torriden_sephora_launch", "korea_cosmetics_output_13bn_usd", "top5_korean_us_ecommerce_growth_71pct"),
        red_flag_fields=("actual_physical_store_sellthrough_unconfirmed", "channel_talks_without_sellthrough", "debut_pop_above_100pct", "tariff_margin_untested"),
        price_data_source="Reuters K-beauty U.S. expansion / d'Alba anchor",
        reported_price_anchor="d'Alba shares more than doubled since debut; full OHLC unavailable",
        reported_return_anchor="Top-five Korean U.S. e-commerce beauty brands +71% over two years vs U.S. market +21%",
        event_mfe_pct=100.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"d_alba_post_debut_return_min_pct": 100.0, "korea_cosmetics_output_2024_usd_bn": 13.0, "export_share_of_output_pct": 80.0, "implied_export_output_usd_bn": 10.4, "top5_korean_us_ecommerce_growth_2y_pct": 71.0, "overall_us_market_growth_2y_pct": 21.0, "korean_vs_overall_growth_spread_pp": 50.0, "top5_french_us_ecommerce_growth_2y_pct": 15.0, "korean_vs_french_growth_spread_pp": 56.0, "tariff_baseline_pct": 10.0, "planned_tariff_pct": 25.0, "actual_physical_store_sellthrough_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_but_overheat",
        rerating_result="unknown",
        round_rerating_label="indie_K_beauty_US_channel_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="IPO_debut_rally_and_channel_talks_not_sellthrough_green",
        price_validation_status="reported_anchor_not_full_ohlc",
        notes="U.S. channel talks and ecommerce growth are Stage 2; sell-through, reorder and gross margin after tariffs are required.",
    ),
    Round274CaseCandidate(
        case_id="r5_loop13_cj_olive_young_global_hb_platform",
        symbol="CJ_Corp_readthrough/unlisted_OliveYoung",
        company_name="CJ Olive Young / CJ Corp read-through",
        primary_archetype=E2RArchetype.H_AND_B_PLATFORM_GLOBALIZATION,
        secondary_archetypes=(E2RArchetype.H_AND_B_RETAIL_GLOBAL_PLATFORM, E2RArchetype.STRONG_PRIVATE_PLATFORM_BUT_HOLDCO_LINK_CAP),
        case_type="success_candidate",
        round_case_type="success_candidate_unlisted_platform_gap",
        stage1_date=date(2025, 6, 5),
        stage2_date=date(2025, 10, 15),
        stage3_date=None,
        stage4b_date=date(2025, 10, 15),
        stage4c_date=None,
        stage3_decision="unlisted_olive_young_platform_is_not_cj_corp_green_without_parent_value_bridge_us_unit_economics_gmv_take_rate_and_margin",
        stage4b_status="4B-watch/parent-readthrough-before-unit-economics",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("olive_young_us_store_plan", "us_kbeauty_market_2bn_usd", "us_kbeauty_market_growth_37pct", "olive_young_more_than_1300_korea_stores", "sephora_ulta_competition"),
        red_flag_fields=("unlisted_subsidiary_readthrough_only", "parent_value_bridge_unconfirmed", "store_unit_economics_unconfirmed", "online_gmv_take_rate_unconfirmed"),
        price_data_source="Reuters K-beauty / Business Insider U.S. K-beauty and Olive Young anchors",
        reported_price_anchor="Olive Young unlisted; CJ Corp read-through requires bridge",
        reported_return_anchor="U.S. K-beauty market $2B and +37%; no direct listed price path",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"direct_listed_ticker": "N/A", "parent_readthrough": "CJ Corp", "olive_young_korea_store_count": 1300, "us_kbeauty_market_size_2025_usd_bn": 2.0, "us_kbeauty_market_growth_pct": 37.0, "us_store_launch_timing": "2026 expected in BI; Reuters reported LA plan as early as 2025", "parent_value_bridge_confirmed": False, "store_unit_economics_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_insufficient_price_data",
        rerating_result="unknown",
        round_rerating_label="H_and_B_platform_globalization_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="unlisted_subsidiary_not_parent_green",
        price_validation_status="unlisted_subsidiary_price_data_unavailable_after_deep_search",
        notes="Olive Young platform value is Stage 2; CJ Corp Green requires store economics, GMV/take-rate and value bridge.",
    ),
    Round274CaseCandidate(
        case_id="r5_loop13_samyang_buldak_export_asp_capacity",
        symbol="003230",
        company_name="Samyang Foods",
        primary_archetype=E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY,
        secondary_archetypes=(E2RArchetype.K_FOOD_EXPORT_RECURRING, E2RArchetype.K_FOOD_SINGLE_SKU_EXPORT_RISK, E2RArchetype.K_FOOD_INPUT_PACKAGING_4C),
        case_type="structural_success",
        round_case_type="structural_success_candidate_plus_safety_input_cost_watch",
        stage1_date=date(2024, 6, 14),
        stage2_date=date(2024, 6, 14),
        stage3_date=date(2024, 6, 14),
        stage4b_date=date(2024, 6, 14),
        stage4c_date=date(2024, 6, 12),
        stage3_decision="export_asp_capacity_and_op_revision_align_but_single_brand_recall_and_input_cost_risks_remain",
        stage4b_status="4B-watch/single-brand-plus-safety-input-cost",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("buldak_exports", "asp_rise", "us_europe_shipment_growth", "production_capacity_expansion", "q2_op_estimate_81_2bn_krw", "op_growth_estimate_84pct_yoy", "target_price_830000_krw"),
        red_flag_fields=("denmark_recall_three_spicy_products", "high_capsaicin_acute_poisoning_concern", "packaging_material_shortage_risk", "single_brand_concentration"),
        price_data_source="MarketWatch earnings anchor + AP recall + Reuters packaging-cost risk",
        reported_price_anchor="Stage3 anchor 647,000 KRW; target 830,000 KRW; Q2 OP estimate 81.2B KRW",
        reported_return_anchor="Shares closed +5.7%; target upside from anchor +28.3%",
        event_mfe_pct=5.7,
        event_mae_pct=None,
        stage2_price_anchor=647000.0,
        stage3_price_anchor=647000.0,
        stage4b_price_anchor=647000.0,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"entry_date": "2024-06-14", "stage3_price_krw": 647000.0, "event_mfe_1d_pct": 5.7, "implied_prior_close_krw": 611921.0, "target_price_krw": 830000.0, "target_upside_from_stage3_pct": 28.3, "q2_op_estimate_krw_bn": 81.2, "op_growth_estimate_pct": 84.0, "denmark_recalled_products": 3, "recall_reason": "high capsaicin / acute poisoning concern", "input_cost_watch": "PET / packaging material shortage risk under Middle East energy shock"},
        score_price_alignment="aligned",
        round_alignment_label="aligned_partial",
        rerating_result="true_rerating",
        round_rerating_label="K_food_export_ASP_capacity_stage3_candidate",
        stage_failure_type="green_success",
        round_stage_failure_label="single_brand_safety_input_cost_4C_watch",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Export/ASP/capacity evidence aligned, but single-brand concentration, recall and input-cost risk remain.",
    ),
    Round274CaseCandidate(
        case_id="r5_loop13_china_tourism_dutyfree_retail_event",
        symbol="069960/008770/004170/123690/034230",
        company_name="Hyundai Department Store / Hotel Shilla / Shinsegae / Hankook Cosmetics / Paradise",
        primary_archetype=E2RArchetype.CHINA_TOURISM_DUTYFREE_RETAIL_EVENT,
        secondary_archetypes=(E2RArchetype.TOURISM_RETAIL_DUTYFREE_EVENT, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE),
        case_type="event_premium",
        round_case_type="event_premium_plus_4B_watch",
        stage1_date=date(2025, 3, 20),
        stage2_date=date(2025, 8, 6),
        stage3_date=None,
        stage4b_date=date(2025, 11, 21),
        stage4c_date=None,
        stage3_decision="tourist_policy_and_redirect_are_stage2_event_premium_until_dutyfree_spend_hotel_occupancy_department_store_sss_cosmetics_sellthrough_and_margin_confirm",
        stage4b_status="4B-watch/tourism-policy-and-cruise-rerouting",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("chinese_group_visa_free_entry", "hyundai_department_store_plus_7_1pct", "hotel_shilla_plus_4_8pct", "hankook_cosmetics_plus_9_9pct", "china_japan_cruise_rerouting", "shinsegae_plus_6pct"),
        red_flag_fields=("tourist_arrival_headline_only", "dutyfree_spend_unconfirmed", "department_store_sss_unconfirmed", "hotel_occupancy_unconfirmed", "tourism_reversal_risk"),
        price_data_source="Reuters China visa-free / cruise rerouting event anchors",
        reported_price_anchor="Visa-free event and later cruise-rerouting basket anchors",
        reported_return_anchor="Hyundai Dept +7.1%, Hotel Shilla +4.8%, Hankook +9.9%; later Shinsegae +6%",
        event_mfe_pct=9.9,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"visa_free_start": "2025-09-29", "programme_end": "2026-06", "group_condition": "3_or_more_mainland_Chinese_tourists", "visa_free_stay_days": 15, "hyundai_department_store_mfe_pct": 7.1, "hotel_shilla_mfe_pct": 4.8, "paradise_mfe_pct": 2.9, "hankook_cosmetics_mfe_pct": 9.9, "lotte_tour_redirect_mfe_pct": 20.0, "yellow_balloon_redirect_mfe_pct": 24.0, "shinsegae_redirect_mfe_pct": 6.0, "adora_usual_jeju_stay_hours": 9, "adora_new_jeju_stay_hours": "31-57", "jeju_stay_extension_low_pct": 244.4, "jeju_stay_extension_high_pct": 533.3},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="China_tourism_retail_dutyfree_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="tourist_flow_headline_not_spend_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Tourist-flow policy is Stage 2; duty-free spend, hotel occupancy, SSS and margin are required before Green.",
    ),
    Round274CaseCandidate(
        case_id="r5_loop13_shinsegae_aliexpress_gmarket_data_gate",
        symbol="004170/139480_readthrough",
        company_name="Shinsegae / AliExpress Korea / Gmarket JV",
        primary_archetype=E2RArchetype.CROSS_BORDER_ECOMMERCE_DATA_GATE,
        secondary_archetypes=(E2RArchetype.ECOMMERCE_JV_SCALE_DATA_GATE, E2RArchetype.RETAIL_PLATFORM_DATA_REGULATION_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate_plus_data_4C_watch",
        stage1_date=date(2025, 9, 18),
        stage2_date=date(2025, 9, 18),
        stage3_date=None,
        stage4b_date=date(2025, 9, 18),
        stage4c_date=date(2025, 9, 18),
        stage3_decision="jv_approval_is_stage2_until_take_rate_gmv_logistics_margin_data_compliance_and_customer_retention_confirm",
        stage4b_status="4B-watch/JV-premium-before-data-compliance",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("ali_express_shinsegae_jv_conditional_approval", "combined_market_share_41pct", "gmarket_customer_database_50mn", "china_direct_import_spending_4_7tn_krw", "alibaba_share_62pct"),
        red_flag_fields=("data_sharing_ban_three_years", "independent_operation_required", "take_rate_unconfirmed", "gmv_profitability_unconfirmed", "data_governance_gate"),
        price_data_source="Reuters KFTC conditional approval anchor",
        reported_price_anchor="Combined overseas online-shopping share 41%; Gmarket 50M customer database",
        reported_return_anchor="Price path unavailable; data sharing banned for 3 years",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"combined_market_share_overseas_online_shopping_pct": 41.0, "gmarket_customer_database_mn": 50.0, "korean_china_import_online_spending_2024_krw_trn": 4.7, "spending_growth_2024_pct": 32.0, "alibaba_share_by_value_pct": 62.0, "data_sharing_ban_years": 3, "independent_operation_required": True, "take_rate_confirmed": False, "gmv_profitability_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_data_4C_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="cross_border_ecommerce_platform_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="JV_approval_not_GMV_margin_data_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="JV approval is Stage 2; data governance, take-rate, GMV profitability and logistics margin are required.",
    ),
    Round274CaseCandidate(
        case_id="r5_loop13_homeplus_retail_credit_hard_reference",
        symbol="unlisted_Homeplus/grocery_retail_reference",
        company_name="Homeplus / MBK Partners",
        primary_archetype=E2RArchetype.GROCERY_RETAIL_CREDIT_4C_REFERENCE,
        secondary_archetypes=(E2RArchetype.OFFLINE_GROCERY_DISTRESS_4C, E2RArchetype.RETAIL_DOMESTIC_CONSUMER),
        case_type="4c_thesis_break",
        round_case_type="retail_credit_hard_reference",
        stage1_date=date(2025, 3, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 6, 13),
        stage3_decision="offline_store_network_is_not_green_when_liquidation_value_exceeds_going_concern_value_and_equity_writeoff_appears",
        stage4b_status="none",
        hard_4c_confirmed=True,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("homeplus_court_led_restructuring", "liquidation_value_3_7tn_krw", "total_assets_6_8tn_krw", "mbk_share_writeoff_2_5tn_krw", "court_sale_plan_approved"),
        red_flag_fields=("retail_credit_restructuring", "liquidation_value_above_going_concern_value", "equity_writeoff", "forced_sale_to_repay_creditors"),
        price_data_source="Reuters Homeplus restructuring / court-sale anchors",
        reported_price_anchor="Unlisted; liquidation value 3.7T KRW and total assets 6.8T KRW",
        reported_return_anchor="MBK to write off 2.5T KRW shares; no listed price path",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"direct_listed_ticker": "N/A", "company_status": "court-led restructuring", "liquidation_value_krw_trn": 3.7, "total_assets_krw_trn": 6.8, "mbk_share_writeoff_krw_trn": 2.5, "mbk_share_writeoff_usd_bn": 1.83, "prior_deal_context_usd_bn": 6.1, "sale_manager": "Samil PwC", "sale_timeline_months": "2-3", "hard_4c_reference": True},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="grocery_retail_credit_failure_reference",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="unlisted_retail_credit_hard_reference",
        price_validation_status="unlisted_retail_credit_reference",
        notes="Offline retail scale cannot override credit stress; this is an R5 hard reference, not a direct listed row.",
    ),
    Round274CaseCandidate(
        case_id="r5_loop13_kyochon_cherrybro_neuromeka_jensen_event",
        symbol="339770/066360/348340",
        company_name="Kyochon F&B / Cherrybro / Neuromeka",
        primary_archetype=E2RArchetype.CELEBRITY_FOOD_SERVICE_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE),
        case_type="overheat",
        round_case_type="overheat_price_moved_without_evidence",
        stage1_date=date(2025, 10, 31),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 10, 31),
        stage4c_date=None,
        stage3_decision="celebrity_food_event_has_no_same_store_sales_franchise_margin_or_repeat_demand_evidence",
        stage4b_status="4B-watch/celebrity-event-plus-20-to-30pct",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("jensen_huang_fried_chicken_event", "kyochon_up_to_20pct", "cherrybro_daily_limit_plus_30pct", "neuromeka_surged", "actual_restaurant_kkanbu_chicken_unlisted"),
        red_flag_fields=("celebrity_event_only", "same_store_sales_absent", "franchise_margin_absent", "repeat_demand_absent", "actual_restaurant_not_listed"),
        price_data_source="Tom's Hardware / MarketWatch event-return anchors",
        reported_price_anchor="Kyochon up to +20%, Cherrybro +30%; actual restaurant Kkanbu Chicken not listed",
        reported_return_anchor="Only Neuromeka reportedly retained gains by close; no SSS or franchise margin evidence",
        event_mfe_pct=30.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"kyochon_event_mfe_pct": 20.0, "cherrybro_event_mfe_pct": 30.0, "neuromeka_event": "surged; only one of the three retained gains by close according to MarketWatch", "actual_restaurant": "Kkanbu Chicken", "actual_restaurant_listed": False, "same_store_sales_confirmed": False, "franchise_margin_confirmed": False, "repeat_demand_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence",
        rerating_result="event_premium",
        round_rerating_label="celebrity_food_service_event_premium",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="should_be_4B_not_stage3",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Celebrity viral event is 4B/event premium, not Stage 3 without SSS, franchise margin and repeat demand.",
    ),
)


def round274_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("export", "asp", "capacity", "op_estimate", "gross_margin", "sellthrough", "repeat", "cash_conversion", "margin")
    for candidate in ROUND274_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND274_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round274 R5 Loop-13 consumer/retail/brand price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "4b" in field.lower()
                or "fourfold" in field.lower()
                or "debut" in field.lower()
                or "event" in field.lower()
                or "rally" in field.lower()
                or "headline" in field.lower()
                or "celebrity" in field.lower()
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "recall" in field.lower()
                or "credit" in field.lower()
                or "data" in field.lower()
                or "tariff" in field.lower()
                or "input" in field.lower()
                or "stuffing" in field.lower()
                or "fade" in field.lower()
                or "liquidation" in field.lower()
            ),
            must_have_fields=ROUND274_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4b_watch", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND274_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_kbeauty_kfood_tourism_celeb_channel_or_jv_headlines_as_green_alone",
                *ROUND274_GREEN_REQUIRED_FIELDS,
                *ROUND274_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_return_from_stage3=candidate.peak_return_from_stage3_pct,
                mfe_30d=candidate.event_mfe_pct,
                mae_30d=candidate.event_mae_pct,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=candidate.stage2_price_anchor is not None
                or candidate.stage3_price_anchor is not None
                or candidate.stage4b_price_anchor is not None
                or candidate.stage4c_price_anchor is not None
                or candidate.event_mfe_pct is not None
                or candidate.event_mae_pct is not None,
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round274_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND274_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "source_sector": "R5",
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
                "direct_listed_hard_4c_confirmed": str(candidate.direct_listed_hard_4c_confirmed).lower(),
                "price_data_source": candidate.price_data_source,
                "reported_price_anchor": candidate.reported_price_anchor,
                "reported_return_anchor": candidate.reported_return_anchor,
                "event_mfe_pct": _float_text(candidate.event_mfe_pct),
                "event_mae_pct": _float_text(candidate.event_mae_pct),
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
                "stage3_price_anchor": _float_text(candidate.stage3_price_anchor),
                "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
                "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
                "peak_return_from_stage3_pct": _float_text(candidate.peak_return_from_stage3_pct),
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
        )
    return tuple(rows)


def round274_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND274_SCORE_ADJUSTMENTS)


def round274_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND274_SHADOW_WEIGHT_ROWS)


def round274_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND274_DEEP_SUB_ARCHETYPES)


def round274_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round274_price_validation": "true"} for field in ROUND274_PRICE_VALIDATION_FIELDS)


def round274_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round274_label": label, "canonical_archetype": canonical} for label, canonical in ROUND274_REQUIRED_TARGET_ALIASES.items())


def round274_summary() -> dict[str, int | bool | str]:
    cases = ROUND274_CASE_CANDIDATES
    return {
        "source_round": ROUND274_SOURCE_ROUND_PATH,
        "round_id": ROUND274_ANALYST_ROUND_ID,
        "large_sector": ROUND274_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_candidate_count": sum(1 for case in cases if "structural_success_candidate" in case.round_case_type),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.rerating_result == "event_premium"),
        "overheat_count": sum(1 for case in cases if "overheat" in case.round_case_type or case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "direct_listed_hard_4c_case_count": sum(1 for case in cases if case.direct_listed_hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None),
        "price_data_unavailable_count": sum(1 for case in cases if "unavailable" in case.price_validation_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND274_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND274_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND274_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
        "hard_4c_confirmed_scope": "true_for_retail_credit_reference",
        "direct_listed_hard_4c_confirmed": False,
    }


def round274_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND274_SOURCE_ROUND_PATH,
        "round_id": ROUND274_ANALYST_ROUND_ID,
        "large_sector": ROUND274_LARGE_SECTOR,
        "summary": round274_summary(),
        "target_aliases": dict(ROUND274_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND274_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND274_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND274_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND274_HARD_4C_GATES),
        "deep_sub_archetypes": round274_deep_sub_archetype_rows(),
        "shadow_weights": round274_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round274_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_kbeauty_kfood_tourism_celeb_channel_or_jv_headlines_as_green_alone",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round274_summary_markdown() -> str:
    summary = round274_summary()
    lines = [
        "# Round 274 R5 Loop 13 Consumer Retail Brand Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- structural_success_candidate: {summary['structural_success_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- direct_listed_hard_4c_case_count: {summary['direct_listed_hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch/reference cases: {summary['stage4c_watch_count']}",
        f"- price_data_unavailable: {summary['price_data_unavailable_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- full_adjusted_ohlc_complete: {str(summary['full_adjusted_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND274_CASE_CANDIDATES:
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
            "- R5 Stage 3 is not the word K-beauty, K-food, tourism, channel listing, IPO pop, or celebrity event.",
            "- APR/Medicube is a strong structural candidate, but a fourfold move before repeat-purchase proof is 4B-watch.",
            "- d'Alba and indie K-beauty are Stage 2 until physical-store sell-through, reorder, margin and inventory discipline appear.",
            "- Olive Young is a strong platform, but CJ Corp needs a parent value bridge and U.S. unit economics.",
            "- Samyang has export/ASP/capacity/OP-revision alignment, with recall and input-cost 4C-watch overlays.",
            "- Tourism retail and Jensen chicken events are price moves before spend, SSS, franchise margin or repeat-demand proof.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round274_green_gate_review_markdown() -> str:
    lines = ["# Round 274 R5 Loop 13 Green Gate Review", "", "Do not apply these weights to production scoring yet.", "", "## Required Fields", ""]
    lines.extend(f"- {field}" for field in ROUND274_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND274_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `d'Alba 상장 후 2배`는 관심 신호다. 하지만 Ulta/Costco 매장 sell-through와 리오더 전에는 Green이 아니다.",
            "- `중국 관광객 비자면제`는 Stage 2 이벤트다. 면세 spend, 호텔 점유율, 백화점 SSS가 필요하다.",
            "- `Jensen Huang이 치킨을 먹었다`는 매출이 아니다. SSS와 가맹점 마진이 없으면 4B/event premium이다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round274_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 274 R5 Loop 13 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND274_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND274_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B는 반복구매·sell-through·마진 증거보다 가격이 먼저 간 상태다.",
            "- 4C는 recall, input-cost shock, data-governance violation, retail credit restructuring처럼 thesis를 끊는 위험이다.",
            "- 이번 라운드의 hard 4C는 Homeplus retail-credit reference에 한정되고, 직접 상장주 hard 4C는 확정하지 않는다.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND274_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.stage4c_date or case.hard_4c_confirmed:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round274_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 274 R5 Loop 13 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND274_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round274_r5_loop13_reports(
    output_directory: str | Path = ROUND274_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND274_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND274_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round274_case_records(), cases_path),
        "audit": _write_json(round274_audit_payload(), audit_path),
        "summary": output / "round274_r5_loop13_price_validation_summary.md",
        "case_matrix": output / "round274_r5_loop13_case_matrix.csv",
        "target_aliases": output / "round274_r5_loop13_target_aliases.csv",
        "score_adjustments": output / "round274_r5_loop13_score_adjustments.csv",
        "shadow_weights": output / "round274_r5_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round274_r5_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round274_r5_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round274_r5_loop13_green_gate_review.md",
        "price_validation_plan": output / "round274_r5_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round274_r5_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round274_summary_markdown(), encoding="utf-8")
    _write_csv(round274_case_rows(), paths["case_matrix"])
    _write_csv(round274_target_alias_rows(), paths["target_aliases"])
    _write_csv(round274_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round274_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round274_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round274_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round274_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round274_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round274_stage4b_4c_review_markdown(), encoding="utf-8")
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
    return f"{value:+d}" if isinstance(value, int) else str(value)
