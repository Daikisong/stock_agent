"""Round-235 R5 Loop-10 consumer/retail/brand price validation pack.

Round 235 is calibration/evaluation material only. It converts
``docs/round/round_235.md`` into structured R5 case records, shadow weights,
and consumer-brand Green/4B/4C guardrails.

Easy example: ``Olive Young U.S. store plan`` is useful Stage 2 attention. It
is not Stage 3-Green until listed-company earnings bridge, store economics,
OPM, inventory, receivables, and sell-through are visible as-of the case date.
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


ROUND235_SOURCE_ROUND_PATH = "docs/round/round_235.md"
ROUND235_LARGE_SECTOR = Round10LargeSector.CONSUMER_RETAIL_BRAND
ROUND235_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round235_r5_loop10_consumer_retail_brand_price_validation"
ROUND235_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r5_loop10_round235.jsonl"
ROUND235_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round235_r5_loop10_consumer_retail_brand_price_validation_audit.json"

ROUND235_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "K_FOOD_EXPORT_RECURRING": E2RArchetype.EXPORT_RECURRING_CONSUMER.value,
    "K_FOOD_GLOBAL_STAPLE_BRAND": E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND.value,
    "K_FOOD_SINGLE_SKU_REGULATORY_WATCH": E2RArchetype.K_FOOD_SINGLE_SKU_RISK.value,
    "K_BEAUTY_DEVICE_GLOBAL_BRAND": E2RArchetype.BEAUTY_DEVICE_EXPORT.value,
    "K_BEAUTY_INDIE_BRAND_US_CHANNEL": E2RArchetype.K_BEAUTY_BRAND_US_CHANNEL.value,
    "K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE": E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION_KOREA.value,
    "K_BEAUTY_RETAIL_PLATFORM": E2RArchetype.K_BEAUTY_RETAIL_PLATFORM.value,
    "LEGACY_BEAUTY_CHINA_EXPOSURE_4C": E2RArchetype.CHINA_CONSUMER_EXPOSURE_4C.value,
    "TOURISM_RETAIL_DUTYFREE_EVENT": E2RArchetype.TOURISM_POLICY_EVENT.value,
    "APPAREL_M_AND_A_OPTIONALITY": E2RArchetype.APPAREL_FAST_FASHION_BRAND_OEM.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
    "CHANNEL_SELLTHROUGH_GATE": E2RArchetype.K_BEAUTY_OFFLINE_SELL_THROUGH.value,
}

ROUND235_DEEP_SUB_ARCHETYPES: tuple[str, ...] = (
    "Samyang_Buldak_export",
    "Denmark_recall_partial_reversal",
    "Nongshim_Shin_Ramyun_global_staple",
    "US_Europe_expansion",
    "single_SKU_dependence",
    "local_regulation_food_safety_watch",
    "APR_Medicube_device_skincare",
    "dAlba_Tirtir_Torriden_Beauty_of_Joseon",
    "Silicon2_distributor_leverage",
    "Cosmax_Kolmar_ODM_leverage",
    "Olive_Young_US_store",
    "US_ecommerce_to_physical_retail_sellthrough",
    "tariff_margin_squeeze",
    "China_decline_saturation_watch",
    "AmorePacific_LGHH_legacy_beauty",
    "duty_free_weakness",
    "local_Chinese_brand_competition",
    "Hotel_Shilla_Hyundai_Department_Paradise_Hankook_Cosmetics",
    "China_visa_free_policy",
    "tourist_arrivals_vs_spend_OPM",
    "FnF_TaylorMade",
    "ROFR_consent_right_dispute",
    "MNA_optionality_vs_confirmed_EPS_accretion",
)

ROUND235_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "repeat_purchase_or_repeat_demand",
    "overseas_sales_mix_growth",
    "channel_sell_through_confirmed",
    "asp_or_product_mix_improvement",
    "opm_improvement",
    "inventory_and_receivables_stable",
    "tariff_recall_regulation_passed",
    "single_sku_or_single_device_risk_managed",
    "price_path_after_evidence",
)

ROUND235_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "viral_tiktok_only",
    "brand_heat_only",
    "retail_talks_without_sell_through",
    "ipo_or_debut_rally_only",
    "influencer_endorsement_only",
    "mna_optionality_without_eps",
    "china_decline_without_offset",
    "single_product_story_only",
    "tourism_policy_without_spend_or_opm",
    "private_affiliate_value_without_listed_earnings_bridge",
)

ROUND235_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "stage3_after_2x_to_4x_price_run",
    "ipo_or_debut_after_one_month_double",
    "single_sku_or_single_device_dependence",
    "us_retail_channel_expectation_before_sellthrough",
    "tourism_policy_day_basket_rally",
    "overseas_sales_good_but_opm_decelerating",
    "mna_optionality_prices_before_signed_transaction",
)

ROUND235_HARD_4C_GATES: tuple[str, ...] = (
    "food_safety_recall_expands",
    "regulatory_ban",
    "channel_stuffing",
    "inventory_build",
    "receivables_spike",
    "single_product_fad_collapse",
    "us_tariff_margin_squeeze",
    "retail_channel_sellthrough_failure",
    "china_sales_collapse_not_offset_by_us_or_europe",
    "mna_event_failure_or_impairment",
    "brand_acquisition_impairment",
)

ROUND235_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_price",
    "mfe_1d",
    "mae_1d",
    "target_upside_pct",
    "reported_mfe_since_debut_pct",
    "reported_mfe_since_january_pct",
    "relative_growth_vs_us_market_multiple",
    "visitor_target_growth_pct",
    "ff_investment_vs_possible_value_pct",
    "overseas_sales_mix",
    "opm_estimate",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round235ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round235ShadowWeightRow:
    archetype: E2RArchetype
    repeat_demand: int
    export_growth: int
    asp: int
    channel_sellthrough: int
    overseas_mix: int
    opm: int
    inventory_quality: int
    receivables_quality: int
    event_penalty: int
    regulatory_redteam: int
    stage4b_watch_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "repeat_demand": _signed_int_text(self.repeat_demand),
            "export_growth": _signed_int_text(self.export_growth),
            "asp": _signed_int_text(self.asp),
            "channel_sellthrough": _signed_int_text(self.channel_sellthrough),
            "overseas_mix": _signed_int_text(self.overseas_mix),
            "opm": _signed_int_text(self.opm),
            "inventory_quality": _signed_int_text(self.inventory_quality),
            "receivables_quality": _signed_int_text(self.receivables_quality),
            "event_penalty": _signed_int_text(self.event_penalty),
            "regulatory_redteam": _signed_int_text(self.regulatory_redteam),
            "4b_watch_sensitivity": _signed_int_text(self.stage4b_watch_sensitivity),
            "hard4c_sensitivity": _signed_int_text(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round235CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    stage3_decision: str
    stage4b_status: str
    hard_4c_confirmed: bool
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
    peak_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str | tuple[str, ...]]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    round_alignment_label: str
    round_rerating_label: str
    round_stage_failure_label: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND235_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND235_SCORE_ADJUSTMENTS: tuple[Round235ScoreAdjustment, ...] = (
    Round235ScoreAdjustment("repeat_demand", 5, "raise", "R5는 유행보다 반복구매와 반복수요가 확인될 때 visibility가 올라간다."),
    Round235ScoreAdjustment("export_growth", 5, "raise", "수출 성장과 해외 mix 증가는 내수 소비재 프레임 제거 근거다."),
    Round235ScoreAdjustment("asp_uplift", 4, "raise", "ASP나 product mix 개선이 OPM으로 내려오면 EPS/FCF 체급 변화 가능성이 높다."),
    Round235ScoreAdjustment("channel_sell_through", 5, "raise", "입점 논의가 아니라 실제 sell-through와 반복 발주가 필요하다."),
    Round235ScoreAdjustment("overseas_sales_mix", 5, "raise", "해외 매출 비중이 높아지면 구조적 채널 전환 근거가 된다."),
    Round235ScoreAdjustment("us_sales_mix", 4, "raise", "미국 매출 비중은 K-food/K-beauty 프레임 전환의 핵심 보조축이다."),
    Round235ScoreAdjustment("opm_improvement", 5, "raise", "브랜드 열기가 OPM으로 내려와야 실제 이익 체급 변화다."),
    Round235ScoreAdjustment("inventory_quality", 4, "raise", "재고가 안정적이면 channel stuffing 위험이 낮아진다."),
    Round235ScoreAdjustment("receivables_quality", 4, "raise", "매출채권 품질은 성장의 현금화 여부를 확인한다."),
    Round235ScoreAdjustment("physical_store_sellthrough", 5, "raise", "오프라인 매장 sell-through는 e-commerce viral보다 강한 반복수요 증거다."),
    Round235ScoreAdjustment("brand_extension_success", 3, "raise", "검증된 hero brand 확장은 Stage 2 가산 근거다."),
    Round235ScoreAdjustment("viral_product_only", -5, "lower", "TikTok/viral만으로는 반복수요와 FCF를 증명하지 못한다."),
    Round235ScoreAdjustment("brand_heat_only", -5, "lower", "브랜드 열기만 있고 실적 품질이 없으면 Green 근거가 아니다."),
    Round235ScoreAdjustment("retail_talks_without_sell_through", -5, "lower", "Ulta/Sephora/Target 논의는 Stage 2 attention이지 Green 근거가 아니다."),
    Round235ScoreAdjustment("ipo_or_debut_rally", -5, "lower", "상장 직후 주가 2배는 4B-watch이지 구조 증거가 아니다."),
    Round235ScoreAdjustment("influencer_endorsement_only", -4, "lower", "인플루언서 endorsement만으로 반복구매와 OPM을 만들지 않는다."),
    Round235ScoreAdjustment("single_sku_dependence", -4, "lower", "단일 제품 의존도는 fad normalization과 recall 리스크를 키운다."),
    Round235ScoreAdjustment("china_exposure_without_offset", -5, "lower", "중국 둔화를 미국/유럽 성장으로 상쇄하지 못하면 Green을 제한한다."),
    Round235ScoreAdjustment("mna_optionality_without_eps", -5, "lower", "TaylorMade 같은 M&A optionality는 본업 EPS/FCF 증거와 분리한다."),
    Round235ScoreAdjustment("tariff_margin_uncertainty", -3, "lower", "관세 부담을 판가에 전가하지 못하면 OPM 품질이 낮아진다."),
    Round235ScoreAdjustment("local_regulatory_recall", -4, "lower", "현지 recall은 부분 해제 전까지 4C-watch로 둔다."),
    Round235ScoreAdjustment("inventory_or_receivables_build", -5, "lower", "재고/채권 증가는 channel stuffing과 현금화 리스크다."),
)


ROUND235_SHADOW_WEIGHT_ROWS: tuple[Round235ShadowWeightRow, ...] = (
    Round235ShadowWeightRow(E2RArchetype.EXPORT_RECURRING_CONSUMER, 5, 5, 4, 4, 5, 5, 4, 4, -2, 4, 4, 3, "Samyang export/ASP/OP revision supports Stage 3 candidate but recall/regulatory watch remains."),
    Round235ShadowWeightRow(E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND, 5, 5, 3, 5, 5, 4, 4, 4, -1, 2, 3, 3, "Nongshim global staple is Stage 2 until OPM/EPS/sell-through confirm."),
    Round235ShadowWeightRow(E2RArchetype.BEAUTY_DEVICE_EXPORT, 5, 5, 3, 5, 5, 5, 3, 3, -2, 2, 5, 3, "APR is structural success but fourfold rally and concentration require 4B-watch."),
    Round235ShadowWeightRow(E2RArchetype.K_BEAUTY_BRAND_US_CHANNEL, 3, 5, 2, 5, 5, 4, 4, 4, -5, 3, 5, 4, "d'Alba/indie K-beauty retail talks require sell-through before Green."),
    Round235ShadowWeightRow(E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION_KOREA, 3, 5, 2, 5, 5, 4, 5, 5, -3, 2, 4, 4, "Cosmax/Kolmar/Silicon2 benefit only if brand sell-through and working capital hold."),
    Round235ShadowWeightRow(E2RArchetype.K_BEAUTY_RETAIL_PLATFORM, 5, 4, 2, 5, 4, 5, 4, 4, -3, 3, 4, 3, "Olive Young platform needs listed earnings bridge and U.S. store economics."),
    Round235ShadowWeightRow(E2RArchetype.CHINA_CONSUMER_EXPOSURE_4C, 2, 3, 2, 3, 3, 4, 5, 5, -2, 4, 4, 5, "Amore legacy China exposure blocks macro K-beauty Green until offset is proven."),
    Round235ShadowWeightRow(E2RArchetype.TOURISM_POLICY_EVENT, 2, 3, 2, 5, 3, 4, 4, 3, -5, 2, 5, 4, "Tourism retail event needs spend/sell-through/OPM, not just visitor policy."),
    Round235ShadowWeightRow(E2RArchetype.APPAREL_FAST_FASHION_BRAND_OEM, 1, 1, 1, 1, 1, 3, 2, 2, -5, 2, 5, 3, "F&F TaylorMade optionality is not Green until confirmed deal and EPS accretion."),
)


ROUND235_CASE_CANDIDATES: tuple[Round235CaseCandidate, ...] = (
    Round235CaseCandidate(
        case_id="r5_loop10_samyang_buldak_export_regulatory_watch",
        symbol="003230",
        company_name="삼양식품",
        primary_archetype=E2RArchetype.EXPORT_RECURRING_CONSUMER,
        secondary_archetypes=(E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND, E2RArchetype.K_FOOD_SINGLE_SKU_RISK, E2RArchetype.FOOD_SAFETY_RECALL_OVERLAY),
        case_type="structural_success",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 6, 14),
        stage3_date=date(2024, 6, 14),
        stage4b_date=None,
        stage4c_date=date(2024, 6, 12),
        stage3_decision="export_asp_op_revision_supports_stage3_candidate_but_denmark_recall_is_local_regulatory_4c_watch_after_partial_reversal",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("buldak_global_viral_export_demand", "us_europe_shipment_growth", "asp_uplift", "capacity_expansion", "q2_op_estimate_81_2bn_krw", "q2_op_estimate_yoy_plus_84pct", "target_price_upgrade_830000"),
        red_flag_fields=("single_sku_dependence", "food_safety_regulatory_watch", "denmark_recall_partial_reversal", "full_ohlc_unavailable"),
        price_data_source="MarketWatch/AP/Reuters reported anchors",
        reported_price_anchor="647,000 KRW close; target price 830,000 KRW; implied prior close 611,921 KRW",
        reported_return_anchor="+5.7% event-day return; target upside +28.3%; Denmark recall/reversal watch",
        mfe_1d=5.7,
        mae_1d=None,
        stage2_price_anchor=647000.0,
        stage3_price_anchor=647000.0,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"implied_prior_close": 611921.0, "target_price": 830000.0, "target_upside_pct": 28.3, "op_estimate_q2_krw_bn": 81.2, "op_growth_estimate_pct": 84.0},
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="green_success",
        round_alignment_label="aligned_partial",
        round_rerating_label="K_food_export_rerating_candidate",
        round_stage_failure_label="green_success_candidate_with_regulatory_watch",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Export/ASP/OP revision supports Stage 3 candidate; Denmark recall is regulatory 4C-watch, not hard 4C after partial reversal.",
    ),
    Round235CaseCandidate(
        case_id="r5_loop10_nongshim_shin_global_staple",
        symbol="004370",
        company_name="농심",
        primary_archetype=E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND,
        secondary_archetypes=(E2RArchetype.EXPORT_RECURRING_CONSUMER,),
        case_type="success_candidate",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 5, 27),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="shin_ramyun_global_staple_is_stage2_until_opm_eps_revision_and_channel_sellthrough_confirm",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("shin_ramyun_record_sales_1_2tn_krw", "shin_ramyun_sales_883mn_usd", "overseas_sales_nearly_60pct", "north_america_sales_538mn_usd", "north_america_sales_growth_10pct", "us_sales_target_1_5bn_2030"),
        red_flag_fields=("opm_eps_revision_unverified", "channel_sellthrough_unverified", "commodity_cost_watch", "stock_ohlc_unavailable"),
        price_data_source="FT business evidence",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="Shin 2023 sales $883M, overseas nearly 60%, North America $538M, U.S. target $1.5B by 2030",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"shin_2023_sales_krw_trn": 1.2, "shin_2023_sales_usd_mn": 883.0, "overseas_sales_share_pct": 60.0, "north_america_sales_2023_usd_mn": 538.0, "north_america_growth_pct": 10.0, "us_sales_target_2030_usd_bn": 1.5, "target_growth_from_2023_na_sales_pct": 178.8},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        round_alignment_label="success_candidate",
        round_rerating_label="global_staple_brand_watch",
        round_stage_failure_label="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Global staple and overseas expansion are Stage 2; OPM/EPS and channel sell-through required for Green.",
    ),
    Round235CaseCandidate(
        case_id="r5_loop10_apr_medicube_structural_4b",
        symbol="278470",
        company_name="APR / Medicube",
        primary_archetype=E2RArchetype.BEAUTY_DEVICE_EXPORT,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_BRAND_US_CHANNEL, E2RArchetype.BEAUTY_DEVICE_AFFILIATE_COMMERCE, E2RArchetype.BEAUTY_FAST_PRODUCT_CYCLE_RISK),
        case_type="structural_success",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 7, 1),
        stage3_date=date(2025, 10, 1),
        stage4b_date=date(2025, 10, 1),
        stage4c_date=None,
        stage3_decision="revenue_conversion_overseas_growth_and_us_channel_support_stage3_candidate_but_fourfold_rally_and_single_device_brand_concentration_require_4b_watch",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("medicube_device_skincare_hybrid", "q4_2025_revenue_440mn_usd", "q4_2025_revenue_growth_124pct", "q4_2025_overseas_revenue_362mn_usd", "q4_2025_overseas_growth_203pct", "fy_2025_revenue_1_2bn_usd", "ulta_1400_store_expansion", "tiktok_shop_revenue_102_9mn_usd"),
        red_flag_fields=("fourfold_rally_since_january", "single_brand_device_concentration", "beauty_device_cycle_fade", "valuation_crowding", "tariff_margin_squeeze_watch"),
        price_data_source="Vogue Business/FT revenue and market-value anchors",
        reported_price_anchor="absolute price unavailable; market value about $6B; stock more than fourfold since January",
        reported_return_anchor="Q4 revenue +124%; overseas +203%; reported MFE since January >+300%",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"q4_2025_revenue_usd_mn": 440.0, "q4_2025_revenue_growth_pct": 124.0, "q4_2025_overseas_revenue_usd_mn": 362.0, "q4_2025_overseas_growth_pct": 203.0, "q4_2025_overseas_share_calc_pct": 82.3, "fy_2025_revenue_usd_bn": 1.2, "medicube_fy_2025_revenue_usd_bn": 1.1, "medicube_revenue_share_pct": 91.7, "ulta_store_expansion_count": 1400.0, "tiktok_shop_revenue_usd_mn": 102.9, "reported_mfe_since_january_pct": 300.0, "market_value_context_usd_bn": 6.0},
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="green_success",
        round_alignment_label="aligned_plus_4B_watch",
        round_rerating_label="K_beauty_device_true_rerating_plus_4B_watch",
        round_stage_failure_label="green_success_candidate",
        price_validation_status="reported_revenue_marketcap_anchor_not_full_ohlc",
        notes="Revenue conversion supports structural success, but single-brand/device concentration and fourfold rally require 4B-watch.",
    ),
    Round235CaseCandidate(
        case_id="r5_loop10_indie_kbeauty_odm_distribution_watch",
        symbol="483650/257720/192820/161890",
        company_name="d'Alba / Silicon2 / Cosmax / Kolmar basket",
        primary_archetype=E2RArchetype.K_BEAUTY_BRAND_US_CHANNEL,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION_KOREA, E2RArchetype.K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA, E2RArchetype.K_BEAUTY_OFFLINE_SELL_THROUGH, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="overheat",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 6, 5),
        stage3_date=None,
        stage4b_date=date(2025, 6, 5),
        stage4c_date=None,
        stage3_decision="us_retail_talks_and_ecommerce_growth_are_stage2_until_physical_sellthrough_repeat_orders_opm_and_working_capital_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ulta_sephora_target_costco_retail_talks", "korea_biggest_us_cosmetics_exporter_2024", "top5_korean_cosmetics_us_ecommerce_growth_71pct", "cosmax_kolmar_odm_model", "silicon2_physical_store_sellthrough_comment"),
        red_flag_fields=("retail_talks_without_sell_through", "ipo_or_debut_rally_only", "brand_heat_only", "inventory_receivables_unverified", "tariff_squeeze_watch"),
        price_data_source="Reuters business and reported return anchors",
        reported_price_anchor="absolute price unavailable",
        reported_return_anchor="d'Alba shares more than doubled since debut; top5 Korean cosmetics U.S. e-commerce +71%",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"dalba_reported_mfe_since_debut_pct": 100.0, "top5_korean_cosmetics_us_ecommerce_growth_pct": 71.0, "overall_us_market_growth_pct": 21.0, "relative_growth_vs_us_market_multiple": 3.38, "retail_talks": "Ulta|Sephora|Target|Costco", "odm_model": "Cosmax|Kolmar"},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="theme_overheat",
        stage_failure_type="false_yellow",
        round_alignment_label="price_moved_without_evidence_for_dAlba_success_candidate_for_ODM_distribution",
        round_rerating_label="K_beauty_indie_retail_watch",
        round_stage_failure_label="stage2_evidence_not_green",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Retail talks and ecommerce growth are Stage 2; sell-through, repeat orders, OPM and working-capital quality required before Green.",
    ),
    Round235CaseCandidate(
        case_id="r5_loop10_cj_olive_young_retail_platform",
        symbol="001040/CJ_OliveYoung_exposure",
        company_name="CJ / Olive Young",
        primary_archetype=E2RArchetype.K_BEAUTY_RETAIL_PLATFORM,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_RETAIL_PLATFORM_OPTION, E2RArchetype.K_BEAUTY_OFFLINE_SELL_THROUGH, E2RArchetype.STRONG_PRIVATE_PLATFORM_BUT_HOLDCO_LINK_CAP),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 10, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="olive_young_platform_is_stage2_until_direct_listed_earnings_bridge_store_economics_and_opm_confirm",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("us_kbeauty_market_2bn_usd", "us_kbeauty_market_growth_37pct", "olive_young_1300_korea_stores", "us_first_store_2026_planned"),
        red_flag_fields=("private_affiliate_value_without_listed_earnings_bridge", "us_store_economics_unverified", "tariff_squeeze_watch", "inventory_build_watch"),
        price_data_source="Business Insider/Reuters platform evidence",
        reported_price_anchor="CJ Corp stock OHLC unavailable; CJ Olive Young not directly listed",
        reported_return_anchor="U.S. K-beauty market $2B, +37%; Olive Young 1,300+ Korea stores and U.S. 2026 plan",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"us_kbeauty_market_size_usd_bn": 2.0, "us_kbeauty_market_growth_pct": 37.0, "olive_young_korea_stores": 1300.0, "us_store_timing": "2026 planned"},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        round_alignment_label="success_candidate",
        round_rerating_label="K_beauty_retail_platform_watch",
        round_stage_failure_label="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Olive Young is Stage 2 platform exposure; direct listed earnings bridge, store economics and OPM required for Green.",
    ),
    Round235CaseCandidate(
        case_id="r5_loop10_amorepacific_legacy_china_exposure",
        symbol="090430",
        company_name="아모레퍼시픽",
        primary_archetype=E2RArchetype.CHINA_CONSUMER_EXPOSURE_4C,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_BRAND_US_CHANNEL, E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION, E2RArchetype.K_BEAUTY_TARIFF_IMPORT_REVIEW),
        case_type="failed_rerating",
        stage1_date=date(2023, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 10, 22),
        stage3_decision="kbeauty_macro_tailwind_is_not_company_green_when_china_dutyfree_weakness_and_local_brand_competition_dominate",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("kbeauty_macro_tailwind", "cosrx_laneige_sulwhasoo_us_transition_expectation", "north_america_emea_growth_attempt"),
        red_flag_fields=("china_demand_weakness", "duty_free_weakness", "local_chinese_brand_competition", "premium_beauty_pressure", "loreal_north_asia_sales_minus_6_5pct_readthrough"),
        price_data_source="Vogue AmorePacific context + Reuters global beauty China-demand evidence",
        reported_price_anchor="AmorePacific event-day OHLC unavailable",
        reported_return_anchor="L'Oreal Q3 like-for-like +3.4% vs expected +6%; North Asia -6.5%; L'Oreal share decline since June about -20%",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"loreal_q3_2024_like_for_like_growth_pct": 3.4, "loreal_expected_growth_pct": 6.0, "loreal_north_asia_sales_pct": -6.5, "loreal_share_decline_since_june_pct": -20.0, "legacy_risk_factors": "China demand weakness|duty-free weakness|local Chinese brand competition|premium beauty slowdown"},
        score_price_alignment="unknown",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        round_alignment_label="thesis_break_watch_insufficient_price_data",
        round_rerating_label="legacy_K_beauty_China_exposure_break",
        round_stage_failure_label="should_have_been_yellow_or_red",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="K-beauty macro is not enough; China/duty-free weakness and premium beauty slowdown block Green until U.S./Europe offset is proven.",
    ),
    Round235CaseCandidate(
        case_id="r5_loop10_tourism_retail_china_visa_event",
        symbol="008770/069960/034230/123690",
        company_name="호텔신라/현대백화점/파라다이스/한국화장품",
        primary_archetype=E2RArchetype.TOURISM_POLICY_EVENT,
        secondary_archetypes=(E2RArchetype.CASINO_DUTYFREE_TOURISM, E2RArchetype.CASINO_DUTYFREE_TOURISM_POLICY_KOREA, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        stage1_date=date(2025, 3, 20),
        stage2_date=date(2025, 8, 6),
        stage3_date=None,
        stage4b_date=date(2025, 8, 6),
        stage4c_date=None,
        stage3_decision="visa_free_tourist_policy_is_stage2_event_until_tourist_spend_dutyfree_sales_sellthrough_casino_drop_hold_and_opm_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("china_group_tourist_visa_free_policy", "visa_free_start_2025_09_29", "hyundai_department_plus_7_1pct", "hotel_shilla_plus_4_8pct", "paradise_plus_2_9pct", "hankook_cosmetics_plus_9_9pct", "visitors_2024_16_4mn", "visitor_target_2025_18_5mn"),
        red_flag_fields=("tourism_policy_without_spend_or_opm", "tourist_spend_unverified", "dutyfree_margin_unverified", "casino_drop_hold_unverified", "policy_day_basket_rally"),
        price_data_source="Reuters event return and tourism metric anchors",
        reported_price_anchor="absolute prices unavailable",
        reported_return_anchor="Hyundai Department +7.1%; Hotel Shilla +4.8%; Paradise +2.9%; Hankook Cosmetics +9.9%; visitor target +12.8%",
        mfe_1d=9.9,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"hyundai_department_event_mfe_1d_pct": 7.1, "hotel_shilla_event_mfe_1d_pct": 4.8, "paradise_event_mfe_1d_pct": 2.9, "hankook_cosmetics_event_mfe_1d_pct": 9.9, "visa_free_stay_days": 15.0, "visitors_2024_mn": 16.4, "visitor_growth_2024_pct": 48.0, "chinese_share_pct": 28.0, "target_visitors_2025_mn": 18.5, "target_growth_vs_2024_pct": 12.8},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        round_alignment_label="event_premium_success_candidate",
        round_rerating_label="tourism_retail_recovery_watch",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Visa-free tourist policy is Stage 2/event; tourist spend, sell-through, duty-free sales and OPM required before Green.",
    ),
    Round235CaseCandidate(
        case_id="r5_loop10_fnf_taylormade_mna_optionality",
        symbol="383220",
        company_name="F&F",
        primary_archetype=E2RArchetype.APPAREL_FAST_FASHION_BRAND_OEM,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        stage1_date=date(2025, 7, 21),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="taylormade_mna_optionality_is_stage1_or_weak_stage2_event_until_confirmed_transaction_financing_eps_accretion_and_integration_plan",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("taylormade_acquisition_optionality", "goldman_advisor", "rofr_consent_right_dispute", "possible_value_3_5bn_usd", "ff_prior_investment_358bn_krw"),
        red_flag_fields=("mna_optionality_without_eps", "confirmed_transaction_absent", "legal_dispute", "financing_and_integration_unverified", "core_apparel_evidence_missing"),
        price_data_source="Reuters deal evidence anchor",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="TaylorMade possible value $3.5B; F&F 2021 subordinated equity investment 358B KRW",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"reported_taylormade_value_usd_bn": 3.5, "ff_2021_subordinated_equity_investment_krw_bn": 358.0, "fx_rate_reported": 1387.39, "krw_equiv_value_krw_trn": 4.856, "ff_investment_vs_possible_value_pct": 7.4, "total_subordinated_equity_investment_krw_bn": 619.2, "ff_share_of_subordinated_equity_pct": 57.8},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        round_alignment_label="event_premium",
        round_rerating_label="M&A_optionality_watch",
        round_stage_failure_label="should_have_been_stage1_or_stage2_only",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="TaylorMade optionality is Stage 1/2 event; confirmed transaction, financing and EPS accretion required for Green.",
    ),
)


def round235_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND235_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round235 R5 Loop-10 consumer/retail/brand price-path validation. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "viral" in field or "policy" in field or "optionality" in field or "talk" in field or "macro" in field or "brand" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "export" in field
                or "asp" in field
                or "op_" in field
                or "overseas" in field
                or "revenue" in field
                or "capacity" in field
                or "sell" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "rally" in field
                or "ipo" in field
                or "debut" in field
                or "valuation" in field
                or "single" in field
                or "policy_day" in field
                or "optionality" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "recall" in field
                or "regulatory" in field
                or "inventory" in field
                or "receivables" in field
                or "china" in field
                or "tariff" in field
                or "impairment" in field
                or "miss" in field
                or "dutyfree" in field
            ),
            must_have_fields=ROUND235_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND235_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_or_business_metrics",
                "do_not_treat_viral_ipo_debut_rally_retail_talks_tourism_policy_influencer_mna_or_china_macro_as_green_alone",
                f"round_alignment_label={candidate.round_alignment_label}",
                f"round_rerating_label={candidate.round_rerating_label}",
                f"round_stage_failure_label={candidate.round_stage_failure_label}",
                *ROUND235_GREEN_REQUIRED_FIELDS,
                *ROUND235_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_price=candidate.peak_price_anchor,
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
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                ),
                stage_dates_confidence=0.84 if candidate.stage2_date or candidate.stage3_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round235_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND235_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "primary_archetype": candidate.primary_archetype.value,
                "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
                "case_type": candidate.case_type,
                "stage1_date": _date_text(candidate.stage1_date),
                "stage2_date": _date_text(candidate.stage2_date),
                "stage3_date": _date_text(candidate.stage3_date),
                "stage4b_date": _date_text(candidate.stage4b_date),
                "stage4c_date": _date_text(candidate.stage4c_date),
                "stage3_decision": candidate.stage3_decision,
                "stage4b_status": candidate.stage4b_status,
                "hard_4c_confirmed": str(candidate.hard_4c_confirmed).lower(),
                "price_data_source": candidate.price_data_source,
                "reported_price_anchor": candidate.reported_price_anchor,
                "reported_return_anchor": candidate.reported_return_anchor,
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mae_1d": _float_text(candidate.mae_1d),
                "stage2_price": _float_text(candidate.stage2_price_anchor),
                "stage3_price": _float_text(candidate.stage3_price_anchor),
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


def round235_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND235_SCORE_ADJUSTMENTS)


def round235_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND235_SHADOW_WEIGHT_ROWS)


def round235_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round235_price_validation": "true"} for field in ROUND235_PRICE_VALIDATION_FIELDS)


def round235_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round235_label": label, "canonical_archetype": canonical} for label, canonical in ROUND235_REQUIRED_TARGET_ALIASES.items())


def round235_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple({"deep_sub_archetype": label, "large_sector": ROUND235_LARGE_SECTOR.value} for label in ROUND235_DEEP_SUB_ARCHETYPES)


def round235_summary() -> dict[str, int | bool | str]:
    cases = ROUND235_CASE_CANDIDATES
    return {
        "source_round": ROUND235_SOURCE_ROUND_PATH,
        "large_sector": ROUND235_LARGE_SECTOR.value,
        "round_id": "round_163",
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "target_archetype_count": len(ROUND235_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND235_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND235_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
    }


def round235_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND235_SOURCE_ROUND_PATH,
        "large_sector": ROUND235_LARGE_SECTOR.value,
        "summary": round235_summary(),
        "target_aliases": dict(ROUND235_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetypes": list(ROUND235_DEEP_SUB_ARCHETYPES),
        "green_required_fields": list(ROUND235_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND235_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND235_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND235_HARD_4C_GATES),
        "score_adjustments": list(round235_score_adjustment_rows()),
        "shadow_weights": list(round235_shadow_weight_rows()),
        "case_ids": [case.case_id for case in ROUND235_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_use_round235_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_viral_ipo_debut_rally_retail_talks_tourism_policy_influencer_or_mna_optionality_as_green",
            "do_not_invent_ohlc_stage_prices_or_business_metrics",
        ],
    }


def render_round235_summary_markdown() -> str:
    summary = round235_summary()
    lines = [
        "# Round 235 R5 Loop 10 Consumer Retail Brand Price Validation",
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
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | stage2 | stage3 | 4B | 4C-watch | round alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND235_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.case_type,
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
            "- 삼양식품은 수출, ASP, OP revision이 같이 확인된 Stage 3 후보지만 local-regulatory 4C-watch가 붙는다.",
            "- APR/Medicube는 강한 structural success 후보지만 주가 4배 이상 상승과 single-device concentration 때문에 4B-watch가 필요하다.",
            "- 농심, CJ/Olive Young, Silicon2/Cosmax/Kolmar류는 Stage 2 후보지만 OPM/EPS/sell-through/working-capital 확인 전 Green이 아니다.",
            "- d'Alba, 관광/면세, F&F는 가격이나 이벤트가 먼저 움직인 event premium이다.",
            "- 아모레퍼시픽은 K-beauty macro와 회사 실적을 분리해야 하는 China exposure thesis-break watch다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round235_green_gate_review_markdown() -> str:
    lines = ["# Round 235 R5 Green Gate Review", "", "Do not apply these weights to production scoring yet.", "", "## Required Fields", ""]
    lines.extend(f"- {field}" for field in ROUND235_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND235_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND235_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `미국 입점 논의`는 Stage 2 attention이다. 실제 매장 sell-through와 반복 주문이 확인되어야 Green 후보가 된다.",
            "- `상장 직후 2배`는 구조 증거가 아니라 4B-watch다.",
            "- `관광객 무비자 정책`은 event premium이다. 객단가, 면세 매출, casino drop/hold, OPM 전에는 Green이 아니다.",
            "- `M&A optionality`는 signed transaction, financing, EPS accretion 전에는 Stage 3 근거가 아니다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round235_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 235 R5 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND235_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND235_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | interpretation |", "|---|---|---|---|"])
    for case in ROUND235_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round235_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 235 R5 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, MAE, stage prices, or business metrics where source anchors are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND235_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND235_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def render_round235_deep_sub_archetypes_markdown() -> str:
    lines = [
        "# Round 235 R5 Deep Sub-Archetypes",
        "",
        "These labels describe research coverage. They are not production scoring inputs.",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND235_DEEP_SUB_ARCHETYPES)
    return "\n".join(lines) + "\n"


def write_round235_r5_loop10_reports(
    output_directory: str | Path = ROUND235_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND235_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND235_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round235_case_records(), cases_path),
        "audit": _write_json(round235_audit_payload(), audit_path),
        "summary": output / "round235_r5_loop10_price_validation_summary.md",
        "case_matrix": output / "round235_r5_loop10_case_matrix.csv",
        "target_aliases": output / "round235_r5_loop10_target_aliases.csv",
        "deep_sub_archetypes": output / "round235_r5_loop10_deep_sub_archetypes.csv",
        "score_adjustments": output / "round235_r5_loop10_score_adjustments.csv",
        "shadow_weights": output / "round235_r5_loop10_shadow_weights.csv",
        "price_validation_fields": output / "round235_r5_loop10_price_validation_fields.csv",
        "green_gate_review": output / "round235_r5_loop10_green_gate_review.md",
        "price_validation_plan": output / "round235_r5_loop10_price_validation_plan.md",
        "stage4b_4c_review": output / "round235_r5_loop10_stage4b_4c_review.md",
        "deep_sub_archetype_review": output / "round235_r5_loop10_deep_sub_archetypes.md",
    }
    paths["summary"].write_text(render_round235_summary_markdown(), encoding="utf-8")
    _write_csv(round235_case_rows(), paths["case_matrix"])
    _write_csv(round235_target_alias_rows(), paths["target_aliases"])
    _write_csv(round235_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round235_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round235_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round235_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round235_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round235_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round235_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["deep_sub_archetype_review"].write_text(render_round235_deep_sub_archetypes_markdown(), encoding="utf-8")
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


def _signed_int_text(value: int) -> str:
    return f"+{value}" if value > 0 else str(value)
