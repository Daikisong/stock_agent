"""Round-261 R5 Loop-12 consumer/retail/brand price-validation pack.

This module converts ``docs/round/round_261.md`` into calibration-only case
records and reports. It intentionally leaves production scoring, candidate
generation, and StageClassifier thresholds unchanged.

Easy example: a K-beauty brand can get a large global M&A validation, but that
does not make a listed ODM or distributor Stage 3-Green until actual orders,
sell-through, margin, and cash conversion are visible.
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


ROUND261_SOURCE_ROUND_PATH = "docs/round/round_261.md"
ROUND261_ROUND_ID = "round_189"
ROUND261_LARGE_SECTOR = Round10LargeSector.CONSUMER_RETAIL_BRAND.value
ROUND261_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round261_r5_loop12_consumer_retail_brand_price_validation"
ROUND261_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r5_loop12_round261.jsonl"
ROUND261_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round261_r5_loop12_consumer_retail_brand_price_validation_audit.json"

ROUND261_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "K_FOOD_EXPORT_ASP_CAPACITY": E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY.value,
    "H_AND_B_RETAIL_GLOBAL_PLATFORM": E2RArchetype.H_AND_B_RETAIL_GLOBAL_PLATFORM.value,
    "K_BEAUTY_BRAND_M_AND_A_VALIDATION": E2RArchetype.K_BEAUTY_BRAND_M_AND_A_VALIDATION.value,
    "K_BEAUTY_INDIE_PHYSICAL_STORE_TEST": E2RArchetype.K_BEAUTY_INDIE_PHYSICAL_STORE_TEST.value,
    "ECOMMERCE_JV_SCALE_DATA_GATE": E2RArchetype.ECOMMERCE_JV_SCALE_DATA_GATE.value,
    "OFFLINE_GROCERY_DISTRESS_4C": E2RArchetype.OFFLINE_GROCERY_DISTRESS_4C.value,
    "GLOBAL_CONFECTIONERY_LOCALIZATION": E2RArchetype.GLOBAL_CONFECTIONERY_LOCALIZATION.value,
    "FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM": E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM.value,
}

ROUND261_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "repeat_purchase_or_repeat_demand_confirmed",
    "overseas_sell_through_confirmed",
    "physical_store_sell_through_confirmed_where_relevant",
    "asp_or_mix_improvement_confirmed",
    "opm_fcf_improvement_confirmed",
    "inventory_and_receivables_stable",
    "channel_retention_or_reorder_confirmed",
    "customer_data_and_platform_trust_risk_passed",
    "price_path_after_evidence",
)

ROUND261_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "k_food_or_k_beauty_label_only",
    "us_store_plan_only",
    "mna_validation_only",
    "retail_talks_only",
    "celebrity_food_event_only",
    "jv_headline_only",
    "offline_asset_value_only",
    "overseas_capex_only",
)

ROUND261_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "debut_or_listing_return_above_2x",
    "single_sku_or_single_brand_concentration_70_90pct_plus",
    "us_store_or_major_retailer_expectation_rally",
    "mna_validation_basket_rally",
    "jv_or_platform_data_scale_headline_rally",
    "celebrity_event_plus_20_30pct",
    "offline_restructuring_relief_price_only",
)

ROUND261_HARD_4C_GATES: tuple[str, ...] = (
    "channel_stuffing",
    "inventory_build",
    "receivables_deterioration",
    "physical_store_sell_through_failure",
    "customer_data_misuse",
    "platform_trust_break",
    "offline_grocery_court_led_restructuring",
    "liquidation_value_above_going_concern_value",
    "input_cost_shock_without_pass_through",
    "single_sku_demand_fade",
    "celebrity_event_fade",
)

ROUND261_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "business_anchor",
    "platform_or_channel_anchor",
    "data_or_trust_gate",
    "retail_distress_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round261ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round261ShadowWeightRow:
    archetype: E2RArchetype
    repeat_purchase: int
    overseas_sell_through: int
    physical_store_sell_through: int
    asp_uplift: int
    channel_retention: int
    inventory_quality: int
    working_capital_quality: int
    opm_fcf: int
    data_compliance: int
    platform_trust: int
    event_penalty: int
    stage4b_watch_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "repeat_purchase": _signed(self.repeat_purchase),
            "overseas_sell_through": _signed(self.overseas_sell_through),
            "physical_store_sell_through": _signed(self.physical_store_sell_through),
            "asp_uplift": _signed(self.asp_uplift),
            "channel_retention": _signed(self.channel_retention),
            "inventory_quality": _signed(self.inventory_quality),
            "working_capital_quality": _signed(self.working_capital_quality),
            "opm_fcf": _signed(self.opm_fcf),
            "data_compliance": _signed(self.data_compliance),
            "platform_trust": _signed(self.platform_trust),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round261DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round261CaseCandidate:
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
    direct_krx_hard_4c_confirmed: bool
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


ROUND261_SCORE_ADJUSTMENTS: tuple[Round261ScoreAdjustment, ...] = (
    Round261ScoreAdjustment("repeat_purchase", 5, "raise", "R5 Green은 유행보다 반복구매가 먼저다."),
    Round261ScoreAdjustment("overseas_sell_through", 5, "raise", "수출 선적이 해외 소비자 sell-through로 닫혀야 한다."),
    Round261ScoreAdjustment("physical_store_sell_through", 5, "raise", "K-beauty는 오프라인 입점보다 매장 회전이 중요하다."),
    Round261ScoreAdjustment("ASP_uplift", 4, "raise", "ASP와 mix 개선은 음식료·브랜드 체급 변화를 확인한다."),
    Round261ScoreAdjustment("channel_retention", 5, "raise", "리오더와 채널 유지율은 일회성 viral을 걸러낸다."),
    Round261ScoreAdjustment("inventory_quality", 4, "raise", "재고가 쌓이면 매출 성장은 sell-in일 수 있다."),
    Round261ScoreAdjustment("working_capital_quality", 4, "raise", "매출채권과 운전자본이 악화되면 FCF로 닫히지 않는다."),
    Round261ScoreAdjustment("OPM_FCF_conversion", 5, "raise", "브랜드력은 OPM과 FCF로 확인되어야 한다."),
    Round261ScoreAdjustment("data_compliance", 5, "raise", "이커머스 JV는 고객데이터 규제 통과가 핵심 gate다."),
    Round261ScoreAdjustment("platform_trust", 5, "raise", "플랫폼 trust가 깨지면 scale이 오히려 4C가 된다."),
    Round261ScoreAdjustment("brand_heat_only", -5, "lower", "브랜드가 핫하다는 문장만으로 Green을 만들 수 없다."),
    Round261ScoreAdjustment("viral_event_only", -5, "lower", "유명인 이벤트와 meme 수요는 매출 증거가 아니다."),
    Round261ScoreAdjustment("M&A_validation_without_revenue", -4, "lower", "M&A validation은 상장사 매출 bridge 없이는 Stage 2 참고다."),
    Round261ScoreAdjustment("U.S._store_plan_without_sell_through", -4, "lower", "U.S. store plan은 매장 sell-through 전까지 Green이 아니다."),
    Round261ScoreAdjustment("retail_talks_without_orders", -5, "lower", "Ulta/Sephora/Target talks는 발주와 sell-through가 필요하다."),
    Round261ScoreAdjustment("JV_without_GMV_margin", -5, "lower", "JV headline은 GMV, take-rate, margin 전까지 Stage 2다."),
    Round261ScoreAdjustment("offline_asset_value_without_cashflow", -5, "lower", "오프라인 자산가치만으로는 회전율·현금흐름 붕괴를 못 막는다."),
    Round261ScoreAdjustment("overseas_capex_without_parent_FCF", -4, "lower", "해외 CAPEX는 연결 매출·마진·FCF bridge가 필요하다."),
    Round261ScoreAdjustment("single_SKU_concentration", -4, "lower", "단일 SKU 의존도는 4B-watch와 4C gate를 키운다."),
    Round261ScoreAdjustment("customer_data_risk", -5, "lower", "고객 데이터 리스크는 플랫폼 scale을 상쇄할 수 있다."),
)


ROUND261_SHADOW_WEIGHT_ROWS: tuple[Round261ShadowWeightRow, ...] = (
    Round261ShadowWeightRow(E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY, 5, 5, 3, 5, 4, 4, 4, 5, 1, 2, -2, 4, 4, "Samyang supports Green candidate only when export, ASP, OP revision and capacity align; single-SKU watch remains."),
    Round261ShadowWeightRow(E2RArchetype.H_AND_B_RETAIL_GLOBAL_PLATFORM, 5, 5, 5, 3, 5, 4, 4, 5, 4, 5, -4, 5, 4, "Olive Young is Stage 2; parent earnings bridge and physical-store economics required."),
    Round261ShadowWeightRow(E2RArchetype.K_BEAUTY_BRAND_M_AND_A_VALIDATION, 4, 5, 4, 3, 4, 3, 3, 4, 1, 2, -5, 5, 3, "Dr.G/L'Oreal validates brand value but not listed-company revenue."),
    Round261ShadowWeightRow(E2RArchetype.K_BEAUTY_INDIE_PHYSICAL_STORE_TEST, 5, 5, 5, 3, 5, 5, 5, 5, 1, 2, -4, 5, 4, "d'Alba/Silicon2/Cosmax/Kolmar need physical-store sell-through and inventory control."),
    Round261ShadowWeightRow(E2RArchetype.ECOMMERCE_JV_SCALE_DATA_GATE, 4, 3, 0, 2, 5, 4, 4, 5, 5, 5, -5, 5, 5, "E-Mart/Alibaba JV is Stage 2 but data compliance and GMV/margin gate are essential."),
    Round261ShadowWeightRow(E2RArchetype.OFFLINE_GROCERY_DISTRESS_4C, 0, 0, 0, 0, 0, 5, 5, 5, 2, 3, 0, 3, 5, "Homeplus is sector hard reference for offline grocery distress."),
    Round261ShadowWeightRow(E2RArchetype.GLOBAL_CONFECTIONERY_LOCALIZATION, 5, 5, 4, 3, 4, 4, 4, 5, 1, 2, -3, 4, 4, "Lotte India localization is Stage 2 until parent revenue/margin/FCF confirm."),
    Round261ShadowWeightRow(E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM, 2, 1, 2, 2, 2, 3, 3, 4, 1, 2, -5, 5, 3, "Kyochon/Cherrybro/Neuromeka Jensen event is price_moved_without_evidence."),
)


ROUND261_DEEP_SUB_ARCHETYPES: tuple[Round261DeepSubArchetype, ...] = (
    Round261DeepSubArchetype("K-food export ASP capacity", E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY, ("Samyang", "Buldak", "ASP", "U.S./Europe shipment", "capacity expansion", "single-SKU watch")),
    Round261DeepSubArchetype("H&B retail global platform", E2RArchetype.H_AND_B_RETAIL_GLOBAL_PLATFORM, ("CJ Olive Young", "U.S. store", "global platform", "California customers", "CJ Corp indirect")),
    Round261DeepSubArchetype("K-beauty brand M&A validation", E2RArchetype.K_BEAUTY_BRAND_M_AND_A_VALIDATION, ("Dr.G", "Gowoonsesang", "L'Oreal", "dermocosmetics", "ODM read-through")),
    Round261DeepSubArchetype("K-beauty indie physical-store test", E2RArchetype.K_BEAUTY_INDIE_PHYSICAL_STORE_TEST, ("d'Alba", "Tirtir", "Torriden", "Beauty of Joseon", "Ulta", "Sephora", "Target", "Costco", "Silicon2", "Cosmax", "Kolmar")),
    Round261DeepSubArchetype("E-commerce JV data gate", E2RArchetype.ECOMMERCE_JV_SCALE_DATA_GATE, ("E-Mart", "Shinsegae", "Alibaba", "Gmarket", "AliExpress Korea", "KFTC", "data-sharing restriction")),
    Round261DeepSubArchetype("Offline grocery distress", E2RArchetype.OFFLINE_GROCERY_DISTRESS_4C, ("Homeplus", "MBK", "court-led restructuring", "liquidation value", "creditors")),
    Round261DeepSubArchetype("Global confectionery localization", E2RArchetype.GLOBAL_CONFECTIONERY_LOCALIZATION, ("Lotte Wellfood", "Lotte India", "Pepero", "ChocoPie", "India snacks", "capex")),
    Round261DeepSubArchetype("Food service celebrity event", E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM, ("Kyochon", "Cherrybro", "Neuromeka", "Jensen Huang", "Kkanbu Chicken", "meme demand")),
)


ROUND261_CASE_CANDIDATES: tuple[Round261CaseCandidate, ...] = (
    Round261CaseCandidate(
        case_id="r5_loop12_samyang_buldak_export_asp_capacity",
        symbol="003230",
        company_name="Samyang Foods",
        primary_archetype=E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY,
        secondary_archetypes=(E2RArchetype.K_FOOD_EXPORT_RECURRING, E2RArchetype.K_FOOD_SINGLE_SKU_EXPORT_RISK),
        case_type="structural_success",
        round_case_type="structural_success_candidate + single-SKU/input 4B-watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 6, 14),
        stage3_date=date(2024, 6, 14),
        stage4b_date=date(2024, 6, 14),
        stage4c_date=None,
        stage3_decision="export_asp_op_revision_capacity_align_but_single_sku_watch_remains",
        stage4b_status="4B-watch single-SKU premium",
        hard_4c_confirmed=False,
        direct_krx_hard_4c_confirmed=False,
        evidence_fields=("buldak_global_viral_demand", "us_europe_shipments_increase", "asp_continues_to_rise", "capacity_expansion_supports_revenue", "q2_op_estimate_81_2bn_krw", "op_growth_estimate_84pct_yoy"),
        red_flag_fields=("single_sku_concentration", "input_cost_packaging_watch", "channel_inventory_risk"),
        price_data_source="MarketWatch / WSJ Market Talk reported price and earnings anchor",
        reported_price_anchor="Stage price 647,000 KRW; target 830,000 KRW; Q2 OP estimate 81.2B KRW",
        reported_return_anchor="Shares +5.7% on 2024-06-14; implied prior close 611,921 KRW; target upside +28.3%",
        mfe_1d=5.7,
        mae_1d=None,
        stage2_price_anchor=647000.0,
        stage3_price_anchor=647000.0,
        stage4b_price_anchor=647000.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"implied_prior_close_krw": 611921, "target_price_krw": 830000, "target_upside_from_stage3_price_pct": 28.3, "q2_op_estimate_krw_bn": 81.2, "op_growth_estimate_pct": 84.0},
        score_price_alignment="aligned",
        round_alignment_label="aligned_partial",
        rerating_result="true_rerating",
        round_rerating_label="K_food_export_ASP_capacity_rerating_candidate",
        stage_failure_type="green_success",
        round_stage_failure_label="Green_candidate_but_single_SKU_4B_watch",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Export, ASP, OP revision and capacity expansion support a Stage 3 candidate; single-SKU concentration remains 4B-watch.",
    ),
    Round261CaseCandidate(
        case_id="r5_loop12_cj_olive_young_hb_global_platform",
        symbol="CJ_Corp_indirect",
        company_name="CJ Olive Young / CJ Corp exposure",
        primary_archetype=E2RArchetype.H_AND_B_RETAIL_GLOBAL_PLATFORM,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_RETAIL_PLATFORM, E2RArchetype.STRONG_PRIVATE_PLATFORM_BUT_HOLDCO_LINK_CAP),
        case_type="success_candidate",
        round_case_type="success_candidate + insufficient_price_data",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 6, 5),
        stage3_date=None,
        stage4b_date=date(2025, 6, 5),
        stage4c_date=None,
        stage3_decision="unlisted_subsidiary_needs_parent_earnings_bridge_and_physical_store_economics",
        stage4b_status="4B-watch IPO/U.S. store speculation",
        hard_4c_confirmed=False,
        direct_krx_hard_4c_confirmed=False,
        evidence_fields=("olive_young_first_us_store_plan_los_angeles", "california_largest_global_online_customer_region", "south_korea_cosmetics_output_13bn_usd", "export_share_about_four_fifths"),
        red_flag_fields=("unlisted_subsidiary", "parent_earnings_bridge_absent", "physical_store_sell_through_unconfirmed", "tariff_inventory_china_demand_watch"),
        price_data_source="Reuters K-beauty / Olive Young business anchor",
        reported_price_anchor="Olive Young is unlisted; CJ Corp direct event price unavailable",
        reported_return_anchor="LA store plan and global platform evidence without parent price path",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"south_korea_cosmetics_output_usd_bn": 13.0, "export_share_context": "about four-fifths", "listed_exposure": "CJ Corp indirect"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_insufficient_price_data",
        rerating_result="unknown",
        round_rerating_label="H_and_B_retail_global_platform_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="unlisted_subsidiary_not_parent_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Strong H&B retail platform evidence, but Olive Young is unlisted; parent earnings bridge and listed price path are required.",
    ),
    Round261CaseCandidate(
        case_id="r5_loop12_dr_g_loreal_kbeauty_brand_mna_validation",
        symbol="K_beauty_ODM_brand_basket",
        company_name="Dr.G / Gowoonsesang / L'Oreal acquisition read-through",
        primary_archetype=E2RArchetype.K_BEAUTY_BRAND_M_AND_A_VALIDATION,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_BRAND_MNA_VALIDATION_STAGE2_REFERENCE, E2RArchetype.K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE),
        case_type="success_candidate",
        round_case_type="success_candidate + M&A validation, not Green",
        stage1_date=date(2024, 12, 20),
        stage2_date=date(2024, 12, 23),
        stage3_date=None,
        stage4b_date=date(2024, 12, 23),
        stage4c_date=None,
        stage3_decision="brand_mna_validation_is_stage2_until_listed_revenue_order_margin_bridge",
        stage4b_status="4B-watch M&A validation basket",
        hard_4c_confirmed=False,
        direct_krx_hard_4c_confirmed=False,
        evidence_fields=("loreal_acquires_gowoonsesang_dr_g", "drg_no1_korean_dermocosmetics_facial_care_line", "pan_asian_global_growth_potential", "mibelle_2023_revenue_661mn_chf"),
        red_flag_fields=("unlisted_target", "deal_value_not_disclosed", "listed_revenue_bridge_absent", "brand_mna_validation_without_revenue"),
        price_data_source="Reuters L'Oreal / Dr.G acquisition anchor",
        reported_price_anchor="Deal value not disclosed; target unlisted; no listed direct price path",
        reported_return_anchor="Mibelle 2023 revenue 661M CHF / about $739M; brand validation only",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"mibelle_2023_revenue_chf_mn": 661.0, "mibelle_2023_revenue_usd_mn": 739.0, "buyer": "L'Oreal", "seller": "Migros / Mibelle Group", "deal_value": "not disclosed"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_M&A_validation",
        rerating_result="event_premium",
        round_rerating_label="K_beauty_brand_value_validation_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="brand_M&A_not_listed_revenue",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Brand M&A validates K-beauty value, but it is not listed-company revenue; ODM/distributor order bridge is required.",
    ),
    Round261CaseCandidate(
        case_id="r5_loop12_dalba_silicon2_cosmax_kolmar_physical_store_test",
        symbol="483650/257720/192820/161890",
        company_name="d'Alba / Silicon2 / Cosmax / Kolmar basket",
        primary_archetype=E2RArchetype.K_BEAUTY_INDIE_PHYSICAL_STORE_TEST,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_INDIE_BRAND_US_CHANNEL, E2RArchetype.K_BEAUTY_ODM_DISTRIBUTOR_LEVERAGE),
        case_type="success_candidate",
        round_case_type="success_candidate + overheat_watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 6, 5),
        stage3_date=None,
        stage4b_date=date(2025, 6, 5),
        stage4c_date=None,
        stage3_decision="ecommerce_success_needs_physical_store_sell_through_repeat_order_inventory_opm",
        stage4b_status="4B-watch post-debut >2x and retail-talks rally",
        hard_4c_confirmed=False,
        direct_krx_hard_4c_confirmed=False,
        evidence_fields=("top5_kbeauty_us_ecommerce_growth_71pct", "overall_us_market_growth_21pct", "retail_talks_ulta_sephora_target_costco", "dalba_reported_return_since_debut_above_100pct", "cosmax_kolmar_odm_leverage", "silicon2_distribution_leverage"),
        red_flag_fields=("physical_store_sell_through_unconfirmed", "retail_talks_without_orders", "inventory_quality_unconfirmed", "debut_rally_above_2x"),
        price_data_source="Reuters K-beauty retail / e-commerce / d'Alba price anchor",
        reported_price_anchor="d'Alba shares more than doubled since debut; full OHLC unavailable",
        reported_return_anchor="Top-five K-beauty U.S. e-commerce +71% vs overall market +21%; d'Alba >+100% since debut",
        mfe_1d=100.0,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"top5_kbeauty_us_ecommerce_growth_pct": 71.0, "overall_us_market_growth_pct": 21.0, "relative_growth_multiple": 3.38, "dalba_reported_return_since_debut_pct_min": 100.0, "retail_talks": ["Ulta", "Sephora", "Target", "Costco"]},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_plus_4B_watch",
        rerating_result="unknown",
        round_rerating_label="K_beauty_indie_physical_store_test",
        stage_failure_type="false_yellow",
        round_stage_failure_label="e-commerce_success_not_physical_store_green",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="E-commerce growth is strong, but physical-store sell-through, repeat orders, inventory and OPM are required before Green.",
    ),
    Round261CaseCandidate(
        case_id="r5_loop12_emart_shinsegae_alibaba_jv_data_gate",
        symbol="139480/004170",
        company_name="E-Mart / Shinsegae / Alibaba JV",
        primary_archetype=E2RArchetype.ECOMMERCE_JV_SCALE_DATA_GATE,
        secondary_archetypes=(E2RArchetype.ECOMMERCE_JV_SCALE_AND_DATA_GATE, E2RArchetype.RETAIL_PLATFORM_DATA_REGULATION_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate + data_gate_watch",
        stage1_date=date(2024, 12, 26),
        stage2_date=date(2024, 12, 26),
        stage3_date=None,
        stage4b_date=date(2024, 12, 26),
        stage4c_date=None,
        stage3_decision="jv_scale_is_stage2_until_gmv_take_rate_margin_retention_data_compliance",
        stage4b_status="4B-watch JV headline before GMV/margin",
        hard_4c_confirmed=False,
        direct_krx_hard_4c_confirmed=False,
        evidence_fields=("emart_alibaba_50_50_jv", "gmarket_aliexpress_korea_combination", "emart_plus_5_5pct", "kftc_conditional_approval", "expected_cross_border_market_share_41pct", "gmarket_50mn_customer_database", "three_year_data_sharing_restriction"),
        red_flag_fields=("jv_without_gmv_margin", "customer_data_risk", "platform_trust_risk", "product_safety_watch", "price_war_margin_dilution"),
        price_data_source="WSJ / Reuters JV and regulatory anchors",
        reported_price_anchor="E-Mart +5.5% on JV headline; KFTC later imposed data-sharing restrictions",
        reported_return_anchor="50:50 JV; expected cross-border share 41%; Gmarket 50M customers; 3-year data-sharing restriction",
        mfe_1d=5.5,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"emart_event_mfe_pct": 5.5, "expected_cross_border_market_share_pct": 41.0, "gmarket_customer_database_mn": 50.0, "data_sharing_restriction_years": 3, "korean_spending_chinese_online_imports_2024_krw_trn": 4.7, "growth_2024_pct": 32.0, "alibaba_share_by_value_pct": 62.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_data_gate_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="e_commerce_JV_scale_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="JV_headline_not_GMV_margin_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="JV scale is Stage 2; GMV, take-rate, margin, retention and data compliance are required before Green.",
    ),
    Round261CaseCandidate(
        case_id="r5_loop12_homeplus_mbk_offline_grocery_distress_reference",
        symbol="unlisted_Homeplus/Lotte_Shopping_E-Mart_sector_readthrough",
        company_name="Homeplus / MBK Partners",
        primary_archetype=E2RArchetype.OFFLINE_GROCERY_DISTRESS_4C,
        secondary_archetypes=(E2RArchetype.RETAIL_DOMESTIC_CONSUMER, E2RArchetype.RETAIL_ECOMMERCE_LOGISTICS),
        case_type="4c_thesis_break",
        round_case_type="4C-thesis-break reference",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 3, 1),
        stage3_decision="offline_grocery_distress_is_sector_hard_reference_not_green",
        stage4b_status="hard 4C reference / unlisted sector read-through",
        hard_4c_confirmed=True,
        direct_krx_hard_4c_confirmed=False,
        evidence_fields=("homeplus_court_led_restructuring", "liquidation_value_3_7tn_krw", "total_assets_6_8tn_krw", "mbk_share_writeoff_2_5tn_krw", "sale_plan_to_repay_creditors_preserve_jobs_protect_partners"),
        red_flag_fields=("offline_grocery_court_led_restructuring", "liquidation_value_above_going_concern_value", "creditor_repayment_sale", "offline_asset_value_without_cashflow"),
        price_data_source="Reuters Homeplus restructuring / sale-plan anchors",
        reported_price_anchor="Homeplus unlisted; sector reference with liquidation value and restructuring anchors",
        reported_return_anchor="Liquidation value 3.7T KRW, assets 6.8T KRW, MBK write-off 2.5T KRW",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"liquidation_value_krw_trn": 3.7, "total_assets_krw_trn": 6.8, "liquidation_value_to_assets_pct": 54.4, "mbk_share_writeoff_krw_trn": 2.5, "mbk_share_writeoff_usd_bn": 1.83},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="offline_grocery_distress_hard_reference",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="unlisted_but_sector_4C_reference",
        price_validation_status="unlisted_sector_reference",
        notes="Unlisted but important R5 hard reference: offline grocery asset value is not Green without cash flow and debt stability.",
    ),
    Round261CaseCandidate(
        case_id="r5_loop12_lotte_wellfood_india_pepero_localization",
        symbol="280360",
        company_name="Lotte Wellfood / Lotte India",
        primary_archetype=E2RArchetype.GLOBAL_CONFECTIONERY_LOCALIZATION,
        secondary_archetypes=(E2RArchetype.K_FOOD_GLOBAL_LOCALIZATION, E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND_SECOND_WAVE),
        case_type="success_candidate",
        round_case_type="success_candidate + insufficient_price_data",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 7, 24),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="india_localization_stage2_until_parent_revenue_margin_fcf_fx_capex_confirm",
        stage4b_status="localization watch",
        hard_4c_confirmed=False,
        direct_krx_hard_4c_confirmed=False,
        evidence_fields=("lotte_india_2027_turnover_target_3000_crore_inr", "2025_turnover_expected_above_2000_crore_inr", "fy25_26_capex_475_crore_inr", "pepero_investment_225_crore_inr", "confectionery_ebitda_13pct", "india_snacks_market_growth_13_14pct"),
        red_flag_fields=("overseas_capex_without_parent_fcf", "fx_capex_risk", "input_cost_cocoa_sugar_watch", "working_capital_unconfirmed"),
        price_data_source="Times of India / Lotte India business anchor",
        reported_price_anchor="Lotte Wellfood full adjusted OHLC unavailable; India business anchor only",
        reported_return_anchor="2027 target 3,000 crore rupees vs 2025 >2,000 crore; FY25-26 capex 475 crore",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"lotte_india_2025_turnover_expected_crore_inr_min": 2000.0, "lotte_india_2027_turnover_target_crore_inr": 3000.0, "target_growth_from_2025_pct_min": 50.0, "fy25_26_capex_crore_inr": 475.0, "pepero_investment_crore_inr": 225.0, "pepero_share_of_capex_pct": 47.4, "confectionery_division_ebitda_pct": 13.0, "india_snacks_market_size_lakh_crore_inr": 1.7, "india_snacks_market_growth_pct": "13-14"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_insufficient_price_data",
        rerating_result="unknown",
        round_rerating_label="global_confectionery_localization_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="overseas_capex_not_parent_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="India localization is Stage 2; parent-company revenue recognition, margin, FCF and FX/capex risk must confirm.",
    ),
    Round261CaseCandidate(
        case_id="r5_loop12_kyochon_cherrybro_neuromeka_jensen_event",
        symbol="339770/066360/348340",
        company_name="Kyochon F&B / Cherrybro / Neuromeka",
        primary_archetype=E2RArchetype.FOOD_SERVICE_CELEBRITY_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.FOOD_SERVICE_EVENT_PREMIUM, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE),
        case_type="overheat",
        round_case_type="overheat / price_moved_without_evidence",
        stage1_date=date(2025, 10, 31),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 10, 31),
        stage4c_date=None,
        stage3_decision="celebrity_food_event_has_no_same_store_sales_or_franchise_margin_evidence",
        stage4b_status="4B-watch celebrity +20-30% event premium",
        hard_4c_confirmed=False,
        direct_krx_hard_4c_confirmed=False,
        evidence_fields=("jensen_huang_fried_chicken_event", "kyochon_up_to_20pct", "cherrybro_up_to_30pct", "neuromeka_surged", "event_at_unlisted_kkanbu_chicken"),
        red_flag_fields=("celebrity_food_event_only", "fundamental_revenue_evidence_absent", "same_store_sales_absent", "franchise_margin_absent", "event_fade_risk"),
        price_data_source="Tom's Hardware / MarketWatch event-return anchors",
        reported_price_anchor="Kyochon up to +20%, Cherrybro up to +30%; restaurant visited was non-listed Kkanbu Chicken",
        reported_return_anchor="Only Neuromeka reportedly retained gains by close; no same-store sales or franchise margin evidence",
        mfe_1d=30.0,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kyochon_event_mfe_pct": 20.0, "cherrybro_event_mfe_pct": 30.0, "neuromeka_event": "surged; only one of three retained gains by close", "event_driver": "Jensen Huang dinner at non-listed Kkanbu Chicken"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence",
        rerating_result="event_premium",
        round_rerating_label="celebrity_food_event_premium",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="should_have_been_stage1_or_4B_watch",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="Viral celebrity food-service event is 4B/event premium until same-store sales, franchise margin and repeat demand confirm.",
    ),
)


def round261_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND261_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND261_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round261 R5 Loop-12 consumer/retail/brand price-validation case. "
                "Calibration-only; not candidate-generation input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if any(token in field for token in ("export", "asp", "op_", "capacity", "sell_through", "fcf", "margin", "gmv", "retention"))
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if any(token in field for token in ("single", "debut", "event", "headline", "mna", "jv", "premium", "watch", "rally"))
            ),
            stage4c_evidence=tuple(
                field
                for field in (*candidate.red_flag_fields, *candidate.evidence_fields)
                if any(token in field for token in ("inventory", "receivable", "trust", "data", "liquidation", "court", "input", "fade", "risk", "distress"))
            ),
            must_have_fields=ROUND261_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4b_watch", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND261_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_sell_through_inventory_receivables_or_fcf",
                "do_not_treat_k_food_k_beauty_mna_store_plan_jv_or_celebrity_event_as_green_alone",
                *ROUND261_GREEN_REQUIRED_FIELDS,
                *ROUND261_GREEN_FORBIDDEN_PATTERNS,
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
                    candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round261_case_rows() -> tuple[dict[str, str], ...]:
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
            "direct_krx_hard_4c_confirmed": str(candidate.direct_krx_hard_4c_confirmed).lower(),
            "price_data_source": candidate.price_data_source,
            "reported_price_anchor": candidate.reported_price_anchor,
            "reported_return_anchor": candidate.reported_return_anchor,
            "mfe_1d": _float_text(candidate.mfe_1d),
            "mae_1d": _float_text(candidate.mae_1d),
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
        for candidate in ROUND261_CASE_CANDIDATES
    )


def round261_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND261_SCORE_ADJUSTMENTS)


def round261_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND261_SHADOW_WEIGHT_ROWS)


def round261_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND261_DEEP_SUB_ARCHETYPES)


def round261_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round261_price_validation": "true"} for field in ROUND261_PRICE_VALIDATION_FIELDS)


def round261_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round261_label": label, "canonical_archetype": canonical} for label, canonical in ROUND261_REQUIRED_TARGET_ALIASES.items())


def round261_summary() -> dict[str, int | bool | str]:
    cases = ROUND261_CASE_CANDIDATES
    return {
        "source_round": ROUND261_SOURCE_ROUND_PATH,
        "round_id": ROUND261_ROUND_ID,
        "large_sector": ROUND261_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "thesis_break_reference_count": sum(1 for case in cases if case.case_type == "4c_thesis_break"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "direct_krx_hard_4c_confirmed": any(case.direct_krx_hard_4c_confirmed for case in cases),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "watch_4c_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "reported_price_anchor_count": sum(1 for case in cases if case.price_validation_status != "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND261_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND261_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND261_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round261_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND261_SOURCE_ROUND_PATH,
        "round_id": ROUND261_ROUND_ID,
        "large_sector": ROUND261_LARGE_SECTOR,
        "summary": round261_summary(),
        "target_aliases": dict(ROUND261_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND261_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND261_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND261_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND261_HARD_4C_GATES),
        "score_adjustments": list(round261_score_adjustment_rows()),
        "shadow_weights": list(round261_shadow_weight_rows()),
        "deep_sub_archetypes": list(round261_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND261_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round261_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_k_food_k_beauty_store_plan_mna_jv_or_celebrity_events_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round261_summary_markdown() -> str:
    summary = round261_summary()
    lines = [
        "# Round 261 R5 Loop 12 Consumer Retail Brand Price Validation",
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
        f"- thesis_break_reference: {summary['thesis_break_reference_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- direct_krx_hard_4c_confirmed: {str(summary['direct_krx_hard_4c_confirmed']).lower()}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND261_CASE_CANDIDATES:
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
            "- Samyang is the R5 K-food export benchmark because export, ASP, OP revision and capacity appeared together.",
            "- CJ Olive Young and Dr.G are strong Stage 2 references, but unlisted or indirect exposure blocks automatic Green.",
            "- d'Alba/K-beauty indie and E-Mart/Alibaba JV need physical sell-through or GMV/margin/data-compliance proof.",
            "- Homeplus is an unlisted offline grocery 4C reference, not a Green case.",
            "- Kyochon/Cherrybro/Neuromeka is price_moved_without_evidence from a celebrity food-service event.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round261_green_gate_review_markdown() -> str:
    lines = [
        "# Round 261 R5 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R5 Stage 3-Green is not `K-food`, `K-beauty`, `brand`, `U.S. store`, `M&A`, `JV`, or `celebrity event`. It requires repeat demand, sell-through, ASP/mix, OPM/FCF, inventory/receivable quality, and platform trust.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND261_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND261_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND261_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `LA store plan` is Stage 2 attention; Green needs store sell-through and parent earnings bridge.",
            "- `brand M&A validation` proves category value, but not listed-company EPS by itself.",
            "- `celebrity fried-chicken event` can move price, but same-store sales and franchise margin are still missing.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round261_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 261 R5 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND261_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND261_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | direct KRX hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND261_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {str(case.direct_krx_hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round261_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 261 R5 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, sell-through, inventory, receivables, GMV, margin, or FCF where raw adjusted data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND261_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND261_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round261_r5_loop12_reports(
    output_directory: str | Path = ROUND261_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND261_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND261_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round261_case_records(), cases_path),
        "audit": _write_json(round261_audit_payload(), audit_path),
        "summary": output / "round261_r5_loop12_price_validation_summary.md",
        "case_matrix": output / "round261_r5_loop12_case_matrix.csv",
        "target_aliases": output / "round261_r5_loop12_target_aliases.csv",
        "score_adjustments": output / "round261_r5_loop12_score_adjustments.csv",
        "shadow_weights": output / "round261_r5_loop12_shadow_weights.csv",
        "deep_sub_archetypes": output / "round261_r5_loop12_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round261_r5_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round261_r5_loop12_green_gate_review.md",
        "price_validation_plan": output / "round261_r5_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round261_r5_loop12_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round261_summary_markdown(), encoding="utf-8")
    _write_csv(round261_case_rows(), paths["case_matrix"])
    _write_csv(round261_target_alias_rows(), paths["target_aliases"])
    _write_csv(round261_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round261_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round261_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round261_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round261_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round261_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round261_stage4b_4c_review_markdown(), encoding="utf-8")
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
