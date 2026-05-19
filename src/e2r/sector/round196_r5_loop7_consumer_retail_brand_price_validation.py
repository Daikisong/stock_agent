"""Round-196 R5 Loop-7 consumer/retail/brand price-path validation pack.

Round 196 is a calibration-only layer for K-food, K-beauty, ODM, beauty-device,
retail-platform, apparel, IPO, and M&A-event cases. It records why repeat
demand, channel sell-through, OPM, inventory, receivables, and price-path
alignment are required before a consumer brand can be treated as a high-quality
E2R candidate.

Simple example: `Costco/Ulta/Target talks` can be Stage 2 attention. It is not
Stage 3-Green until actual sell-through, repeat order, OPM, inventory, and
receivables quality are visible as-of the case date.

This module is report/evaluation material only. Production candidate
generation, feature engineering, scoring, staging, and RedTeam code must not
import it.
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


ROUND196_SOURCE_ROUND_PATH = "docs/round/round_196.md"
ROUND196_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round196_r5_loop7_consumer_retail_brand_price_validation"
ROUND196_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r5_loop7_round196.jsonl"
ROUND196_DEFAULT_AUDIT_PATH = (
    "data/sector_taxonomy/round196_r5_loop7_consumer_retail_brand_price_validation_audit.json"
)

ROUND196_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "EXPORT_RECURRING_CONSUMER": E2RArchetype.EXPORT_RECURRING_CONSUMER.value,
    "K_FOOD_GLOBAL_STAPLE_BRAND": E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND.value,
    "K_FOOD_SINGLE_SKU_RISK": E2RArchetype.K_FOOD_SINGLE_SKU_RISK.value,
    "K_BEAUTY_EXPORT_DISTRIBUTION": E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION.value,
    "K_BEAUTY_BRAND_US_CHANNEL": E2RArchetype.K_BEAUTY_BRAND_US_CHANNEL.value,
    "K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA": E2RArchetype.K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA.value,
    "K_BEAUTY_RETAIL_PLATFORM": E2RArchetype.K_BEAUTY_RETAIL_PLATFORM.value,
    "BEAUTY_DEVICE_EXPORT": E2RArchetype.BEAUTY_DEVICE_EXPORT.value,
    "RETAIL_ECOMMERCE_LOGISTICS": E2RArchetype.RETAIL_ECOMMERCE_LOGISTICS.value,
    "APPAREL_FAST_FASHION_BRAND_OEM": E2RArchetype.APPAREL_FAST_FASHION_BRAND_OEM.value,
    "EVENT_PREMIUM_GOVERNANCE_OVERLAY": E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY.value,
    "CHANNEL_STUFFING_INVENTORY_OVERLAY": E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY.value,
    "TARIFF_IMPORT_MARGIN_OVERLAY": E2RArchetype.TARIFF_IMPORT_MARGIN_OVERLAY.value,
    "CHINA_CONSUMER_EXPOSURE_4C": E2RArchetype.CHINA_CONSUMER_EXPOSURE_4C.value,
    "DISCLOSURE_CONFIDENCE_CAP": E2RArchetype.DISCLOSURE_CONFIDENCE_CAP.value,
    "STRONG_PRIVATE_PLATFORM_BUT_HOLDCO_LINK_CAP": E2RArchetype.STRONG_PRIVATE_PLATFORM_BUT_HOLDCO_LINK_CAP.value,
    "BEAUTY_FAST_PRODUCT_CYCLE_RISK": E2RArchetype.BEAUTY_FAST_PRODUCT_CYCLE_RISK.value,
    "APPAREL_LICENSE_BRAND_CHINA_RISK": E2RArchetype.APPAREL_LICENSE_BRAND_CHINA_RISK.value,
}

ROUND196_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "repeat_purchase_evidence",
    "overseas_sales_mix_growth",
    "channel_sell_through_confirmed",
    "opm_improvement",
    "inventory_and_receivables_stable",
    "asp_or_product_mix_improvement",
    "single_product_dependence_not_excessive",
    "tariff_regulation_recall_passed",
    "price_path_after_evidence",
)

ROUND196_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "tiktok_viral_only",
    "retail_talks_only",
    "ipo_first_month_rally",
    "influencer_endorsement_only",
    "mna_event_only",
    "private_affiliate_value_only",
    "china_decline_without_offset",
)

ROUND196_STAGE4B_STATUSES: tuple[str, ...] = ("none", "watch", "elevated", "graduated")

ROUND196_HARD_4C_GATES: tuple[str, ...] = (
    "recall_or_food_safety_issue",
    "channel_stuffing",
    "inventory_build",
    "receivables_spike",
    "single_product_fad_collapse",
    "us_tariff_margin_squeeze",
    "retail_channel_sellthrough_failure",
    "china_sales_collapse_not_offset_by_us_or_europe",
    "brand_acquisition_impairment",
    "mna_event_failure",
    "privacy_data_consumer_regulation_issue",
)

ROUND196_PRICE_BACKFILL_FIELDS: tuple[str, ...] = (
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
    "peak_date",
    "peak_price",
    "MFE_5D",
    "MFE_20D",
    "MFE_30D",
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_5D",
    "MAE_20D",
    "MAE_30D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "MAE_2Y",
    "drawdown_after_peak",
    "relative_strength_vs_kospi",
    "relative_strength_vs_consumer_basket",
    "relative_strength_vs_kbeauty_basket",
    "relative_strength_vs_kfood_basket",
    "repeat_purchase_evidence",
    "overseas_sales_mix",
    "us_sales_mix",
    "channel_sell_through",
    "repeat_order",
    "opm_improvement",
    "eps_revision",
    "fcf_conversion",
    "inventory_days",
    "receivables_days",
    "asp_or_product_mix",
    "single_sku_dependence",
    "retail_talks_without_sell_through_flag",
    "ipo_first_month_rally_flag",
    "mna_event_premium_flag",
    "holdco_or_private_link_cap_flag",
    "tariff_margin_uncertainty_flag",
    "food_safety_or_recall_flag",
    "stage4b_status",
    "hard_4c_confirmed",
)


@dataclass(frozen=True)
class Round196ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {
            "axis": self.axis,
            "points": str(self.points),
            "direction": self.direction,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class Round196CaseCandidate:
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
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.CONSUMER_RETAIL_BRAND

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND196_SCORE_ADJUSTMENTS: tuple[Round196ScoreAdjustment, ...] = (
    Round196ScoreAdjustment("repeat_demand", 4, "raise", "유행이 아니라 반복구매가 확인될 때 R5 visibility가 올라간다."),
    Round196ScoreAdjustment("channel_sell_through", 4, "raise", "입점이 아니라 매장 회전과 반복 발주가 확인되어야 한다."),
    Round196ScoreAdjustment("overseas_sales_mix", 3, "raise", "미국/유럽/글로벌 매출 비중 증가는 내수 프레임 제거 근거다."),
    Round196ScoreAdjustment("us_retail_channel_confirmed", 3, "raise", "Costco/Ulta/Target/Sephora/Walmart 등 실제 채널 확인은 Stage 2 이상 근거다."),
    Round196ScoreAdjustment("opm_improvement", 4, "raise", "수출 성장이나 브랜드 열기가 OPM으로 내려와야 EPS/FCF 체급 변화다."),
    Round196ScoreAdjustment("inventory_quality", 3, "raise", "재고가 안정적이면 channel stuffing 위험이 낮아진다."),
    Round196ScoreAdjustment("receivables_quality", 3, "raise", "매출채권이 안정적이면 매출 성장의 현금화 품질이 올라간다."),
    Round196ScoreAdjustment("brand_portfolio_breadth", 2, "raise", "단일 제품보다 포트폴리오가 넓으면 fad 위험이 낮다."),
    Round196ScoreAdjustment("odm_customer_diversification", 3, "raise", "ODM은 고객 다변화와 주문 visibility가 핵심이다."),
    Round196ScoreAdjustment("localized_manufacturing", 2, "raise", "현지 생산은 관세/물류 리스크를 줄이는 보조 근거다."),
    Round196ScoreAdjustment("viral_product_only", -5, "lower", "틱톡/viral만으로는 반복수요와 FCF를 확인할 수 없다."),
    Round196ScoreAdjustment("brand_heat_only", -4, "lower", "브랜드 열기만 있고 실적 품질이 없으면 Green 근거가 아니다."),
    Round196ScoreAdjustment("ipo_first_month_rally", -4, "lower", "상장 직후 주가 급등은 가격경로 경고이지 구조 증거가 아니다."),
    Round196ScoreAdjustment("retail_talks_without_sell_through", -3, "lower", "입점 논의는 Stage 2 attention이고 sell-through 전에는 제한한다."),
    Round196ScoreAdjustment("influencer_endorsement_only", -3, "lower", "인플루언서 endorsement만으로 반복구매를 만들지 않는다."),
    Round196ScoreAdjustment("single_sku_dependence", -4, "lower", "단일 SKU 의존도는 fad normalization과 4C 위험을 키운다."),
    Round196ScoreAdjustment("china_exposure_without_offset", -3, "lower", "중국 둔화를 미국/유럽 성장으로 상쇄하지 못하면 제한한다."),
    Round196ScoreAdjustment("holdco_or_private_link_cap", -3, "lower", "비상장 자회사 가치와 상장 모회사 수익률은 분리해야 한다."),
    Round196ScoreAdjustment("mna_event_premium", -4, "lower", "M&A/ROFR/법적 분쟁은 본업 브랜드 리레이팅 증거가 아니다."),
    Round196ScoreAdjustment("tariff_margin_uncertainty", -2, "lower", "관세 부담을 판가에 전가하지 못하면 OPM 품질이 낮아진다."),
    Round196ScoreAdjustment("inventory_or_receivables_build", -4, "lower", "재고/채권 증가는 channel stuffing과 현금화 리스크다."),
)


ROUND196_CASE_CANDIDATES: tuple[Round196CaseCandidate, ...] = (
    Round196CaseCandidate(
        case_id="nongshim_shin_ramyun_global_staple_stage2_watch",
        symbol="004370",
        company_name="농심",
        primary_archetype=E2RArchetype.K_FOOD_GLOBAL_STAPLE_BRAND,
        secondary_archetypes=(E2RArchetype.EXPORT_RECURRING_CONSUMER, E2RArchetype.K_FOOD_SINGLE_SKU_RISK),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2024, 5, 27),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_opm_eps_revision_us_factory_utilization_and_channel_sellthrough",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=(
            "shin_ramyun_2023_sales_record_1_2t_krw",
            "overseas_sales_mix_near_60pct",
            "north_america_sales_growth_2023",
            "2030_us_revenue_target",
            "global_staple_brand_repeat_consumption",
        ),
        red_flag_fields=("opm_eps_revision_unverified", "food_safety_recall_watch", "cost_inflation", "channel_sellthrough_unverified"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="K-food staple export is a real Stage 2 structure, but Stage 3 waits for OPM, EPS revision, factory utilization, and sell-through.",
    ),
    Round196CaseCandidate(
        case_id="apr_medicube_beauty_device_structural_success_4b_watch",
        symbol="278470",
        company_name="APR",
        primary_archetype=E2RArchetype.BEAUTY_DEVICE_EXPORT,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_BRAND_US_CHANNEL, E2RArchetype.BEAUTY_DEVICE_REGULATORY_SAFETY),
        case_type="structural_success",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 10, 20),
        stage4c_date=None,
        stage3_decision="possible_after_q2_2025_overseas_us_sales_device_revenue_opm_confirmation_but_exact_stage3_date_needs_backfill",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=(
            "medicube_skincare_device_success",
            "overseas_sales_mix_near_80pct",
            "us_sales_mix_near_30pct",
            "beauty_device_category_revenue_confirmed",
            "share_price_more_than_4x_since_jan_2025_anchor",
        ),
        red_flag_fields=("valuation_4b_watch", "viral_influencer_dependence", "device_competition", "tariff_margin_squeeze", "regulation_culture_risk"),
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="APR has stronger evidence than a theme case, but the 4x price anchor means Stage 4B-watch must be attached before any Green discussion.",
    ),
    Round196CaseCandidate(
        case_id="dalba_global_us_retail_talks_ipo_overheat_watch",
        symbol="483650",
        company_name="d'Alba Global",
        primary_archetype=E2RArchetype.K_BEAUTY_BRAND_US_CHANNEL,
        secondary_archetypes=(
            E2RArchetype.BEAUTY_FAST_PRODUCT_CYCLE_RISK,
            E2RArchetype.PRICE_ONLY_RALLY,
            E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY,
        ),
        case_type="overheat",
        stage1_date=None,
        stage2_date=date(2025, 6, 5),
        stage3_date=None,
        stage4b_date=date(2025, 6, 5),
        stage4c_date=None,
        stage3_decision="forbidden_retail_talks_and_ipo_double_before_sellthrough_repeat_order_opm_inventory_quality",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("costco_ulta_target_retail_talks", "us_kbeauty_ecommerce_growth_context", "ipo_post_listing_price_more_than_2x"),
        red_flag_fields=("retail_talks_without_sellthrough", "ipo_first_month_rally", "sellthrough_missing", "inventory_receivables_unknown"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="theme_overheat",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Retail talks are Stage 2 attention. IPO after a 2x move is 4B-watch, not Stage 3 evidence.",
    ),
    Round196CaseCandidate(
        case_id="cosmax_kolmar_fast_beauty_odm_supply_chain_stage2_watch",
        symbol="192820/161890",
        company_name="코스맥스/한국콜마",
        primary_archetype=E2RArchetype.K_BEAUTY_OEM_ODM_SUPPLYCHAIN_KOREA,
        secondary_archetypes=(E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION, E2RArchetype.K_BEAUTY_BRAND_US_CHANNEL),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2025, 6, 5),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_customer_diversification_orders_opm_inventory_receivables_us_europe_volume",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("fast_beauty_foxconn_supply_chain", "indie_kbeauty_contract_manufacturing", "us_europe_brand_portfolio", "odm_operating_leverage"),
        red_flag_fields=("single_hot_brand_dependence", "receivables_growth_watch", "inventory_build_watch", "tariff_pass_through_failure"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="ODM leverage can be Stage 2, but Green needs order visibility, OPM, customer diversification, and working-capital quality.",
    ),
    Round196CaseCandidate(
        case_id="amorepacific_legacy_kbeauty_china_to_us_transition_watch",
        symbol="090430",
        company_name="아모레퍼시픽",
        primary_archetype=E2RArchetype.K_BEAUTY_BRAND_US_CHANNEL,
        secondary_archetypes=(E2RArchetype.CHINA_CONSUMER_EXPOSURE_4C, E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION),
        case_type="failed_rerating",
        stage1_date=None,
        stage2_date=date(2025, 6, 5),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="forbidden_until_china_decline_offset_us_europe_sellthrough_cosrx_laneige_sulwhasoo_opm_recovery",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("kbeauty_us_push", "cosrx_laneige_sulwhasoo_global_expansion", "legacy_brand_turnaround_watch"),
        red_flag_fields=("china_exports_decline", "cosrx_growth_plateau", "low_priced_alternative_competition", "opm_recovery_missing", "inventory_risk"),
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        stage_failure_type="false_green",
        price_validation_status="needs_ohlc_backfill",
        notes="K-beauty macro tailwind is not company-level Green when China exposure and brand plateau risk remain unresolved.",
    ),
    Round196CaseCandidate(
        case_id="cj_olive_young_private_platform_holdco_cap_stage2_watch",
        symbol="001040",
        company_name="CJ/올리브영",
        primary_archetype=E2RArchetype.K_BEAUTY_RETAIL_PLATFORM,
        secondary_archetypes=(E2RArchetype.STRONG_PRIVATE_PLATFORM_BUT_HOLDCO_LINK_CAP, E2RArchetype.K_BEAUTY_EXPORT_DISTRIBUTION),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2025, 6, 5),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_listed_parent_value_capture_sellthrough_opm_and_holdco_discount_needed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("olive_young_la_first_us_store_plan", "global_online_customer_base", "kbeauty_curation_platform", "california_customer_concentration"),
        red_flag_fields=("listed_exposure_unclear", "holdco_discount", "ipo_event_premium", "sellthrough_unverified"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Olive Young may be a strong platform, but listed CJ exposure and holdco discount cap the Stage before value capture is proven.",
    ),
    Round196CaseCandidate(
        case_id="fnf_taylormade_mna_event_premium_not_brand_rerating",
        symbol="383220",
        company_name="F&F",
        primary_archetype=E2RArchetype.APPAREL_FAST_FASHION_BRAND_OEM,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY, E2RArchetype.APPAREL_LICENSE_BRAND_CHINA_RISK),
        case_type="event_premium",
        stage1_date=date(2025, 7, 21),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 7, 21),
        stage4c_date=None,
        stage3_decision="forbidden_mna_rofr_legal_event_without_core_brand_revenue_opm_fcf_or_accretion",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("taylormade_acquisition_rofr_event", "goldman_advisor", "legal_dispute_watch", "possible_3_5b_usd_enterprise_value"),
        red_flag_fields=("mna_event_premium", "legal_dispute", "core_brand_revenue_unconfirmed", "china_global_channel_weak", "acquisition_accretion_missing"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="TaylorMade optionality is an event premium. It is not brand rerating before core revenue, OPM, FCF, and acquisition accretion are confirmed.",
    ),
)


def round196_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND196_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector.value,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round196 R5 Loop-7 consumer/retail/brand price-path validation case. "
                "This is calibration-only and must not be used for candidate generation."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "event" in field or "ipo" in field or "story" in field or "talks" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "overseas_sales_mix" in field or "us_sales_mix" in field or "device_category" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "4b" in field or "price" in field or "ipo" in field or "valuation" in field or "premium" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "recall" in field
                or "inventory" in field
                or "receivables" in field
                or "china" in field
                or "tariff" in field
                or "sellthrough" in field
                or "legal" in field
            ),
            must_have_fields=ROUND196_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={
                "repeat_demand_delta": 4.0,
                "channel_sell_through_delta": 4.0,
                "overseas_sales_mix_delta": 3.0,
                "us_retail_channel_confirmed_delta": 3.0,
                "opm_improvement_delta": 4.0,
                "inventory_quality_delta": 3.0,
                "receivables_quality_delta": 3.0,
                "viral_product_only_delta": -5.0,
                "ipo_first_month_rally_delta": -4.0,
                "mna_event_premium_delta": -4.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "needs_ohlc_backfill_true",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_retail_talks_ipo_or_mna_as_green_evidence",
                *ROUND196_GREEN_REQUIRED_FIELDS,
                *ROUND196_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8 if candidate.stage2_date or candidate.stage4b_date else 0.35,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round196_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND196_CASE_CANDIDATES:
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
                "score_price_alignment": candidate.score_price_alignment,
                "rerating_result": candidate.rerating_result,
                "stage_failure_type": candidate.stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round196_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND196_SCORE_ADJUSTMENTS)


def round196_price_backfill_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round196_backfill": "true"} for field in ROUND196_PRICE_BACKFILL_FIELDS)


def round196_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round196_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND196_REQUIRED_TARGET_ALIASES.items()
    )


def round196_summary() -> dict[str, int | bool]:
    cases = round196_case_records()
    return {
        "case_candidate_count": len(cases),
        "required_target_count": len(ROUND196_REQUIRED_TARGET_ALIASES),
        "score_adjustment_count": len(ROUND196_SCORE_ADJUSTMENTS),
        "price_backfill_field_count": len(ROUND196_PRICE_BACKFILL_FIELDS),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "hard_4c_case_count": sum(1 for case in ROUND196_CASE_CANDIDATES if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in ROUND196_CASE_CANDIDATES if case.stage3_date),
        "stage3_possible_candidate_count": sum(1 for case in ROUND196_CASE_CANDIDATES if "possible" in case.stage3_decision),
        "stage4b_watch_or_elevated_count": sum(
            1 for case in ROUND196_CASE_CANDIDATES if case.stage4b_status in {"watch", "elevated"}
        ),
        "needs_ohlc_backfill_count": sum(1 for case in ROUND196_CASE_CANDIDATES if case.price_validation_status == "needs_ohlc_backfill"),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "needs_ohlc_backfill": True,
    }


def write_round196_r5_loop7_reports(
    *,
    output_directory: str | Path = ROUND196_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND196_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND196_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = write_case_library(round196_case_records(), cases_path)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "audit_json": audit,
        "summary": output / "round196_r5_loop7_price_validation_summary.md",
        "case_matrix": output / "round196_r5_loop7_case_matrix.csv",
        "target_aliases": output / "round196_r5_loop7_target_aliases.csv",
        "score_adjustments": output / "round196_r5_loop7_score_adjustments.csv",
        "price_backfill_fields": output / "round196_r5_loop7_price_backfill_fields.csv",
        "green_gate_review": output / "round196_r5_loop7_green_gate_review.md",
        "price_backfill_plan": output / "round196_r5_loop7_price_backfill_plan.md",
        "stage4b_4c_review": output / "round196_r5_loop7_stage4b_4c_review.md",
    }
    audit.write_text(json.dumps(round196_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round196_case_rows(), paths["case_matrix"])
    _write_rows(round196_target_alias_rows(), paths["target_aliases"])
    _write_rows(round196_score_adjustment_rows(), paths["score_adjustments"])
    _write_rows(round196_price_backfill_field_rows(), paths["price_backfill_fields"])
    paths["summary"].write_text(render_round196_summary_markdown(), encoding="utf-8")
    paths["green_gate_review"].write_text(render_round196_green_gate_review_markdown(), encoding="utf-8")
    paths["price_backfill_plan"].write_text(render_round196_price_backfill_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round196_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def round196_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND196_SOURCE_ROUND_PATH,
        "large_sector": Round10LargeSector.CONSUMER_RETAIL_BRAND.value,
        "summary": round196_summary(),
        "target_aliases": list(round196_target_alias_rows()),
        "green_required_fields": list(ROUND196_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND196_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_statuses": list(ROUND196_STAGE4B_STATUSES),
        "hard_4c_gates": list(ROUND196_HARD_4C_GATES),
        "score_adjustments": list(round196_score_adjustment_rows()),
        "case_ids": [case.case_id for case in ROUND196_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round196_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_viral_ipo_retail_talks_or_mna_as_green_evidence",
            "do_not_invent_prices_stage_dates_sellthrough_opm_inventory_receivables_or_fcf",
        ],
    }


def render_round196_summary_markdown() -> str:
    summary = round196_summary()
    lines = [
        "# Round-196 R5 Loop-7 Price-Path Validation Summary",
        "",
        f"- source_round: `{ROUND196_SOURCE_ROUND_PATH}`",
        "- large_sector: `CONSUMER_RETAIL_BRAND`",
        "- scope: K-food, K-beauty, ODM, beauty-device, retail platform, apparel, IPO, and M&A event validation",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- score_adjustment_count: {summary['score_adjustment_count']}",
        f"- price_backfill_field_count: {summary['price_backfill_field_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- overheat_count: {summary['overheat_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- stage3_case_count: {summary['stage3_case_count']}",
        f"- stage3_possible_candidate_count: {summary['stage3_possible_candidate_count']}",
        f"- stage4b_watch_or_elevated_count: {summary['stage4b_watch_or_elevated_count']}",
        f"- needs_ohlc_backfill_count: {summary['needs_ohlc_backfill_count']}",
        "- production_scoring_changed: false",
        "- candidate_generation_input: false",
        "- shadow_weight_only: true",
        "- needs_ohlc_backfill: true",
        "",
        "## Interpretation",
        "",
        "- R5는 진짜 구조적 수출 소비재와 viral/event premium을 분리하는 라운드다.",
        "- 농심은 K-food staple Stage 2 후보지만 OPM/EPS와 channel sell-through 전에는 Stage 3가 아니다.",
        "- APR은 overseas/US sales와 device revenue가 강하지만 2025년 4배 상승 anchor 때문에 4B-watch가 필요하다.",
        "- d'Alba는 retail talks와 IPO 2x rally를 Green 근거로 쓰면 안 된다.",
        "- 코스맥스/한국콜마 ODM은 고객 다변화, 주문 visibility, OPM, 재고/채권 확인 전 Green 금지다.",
        "- 아모레퍼시픽은 K-beauty macro와 China/COSRX company-level risk를 분리해야 한다.",
        "- CJ/올리브영은 좋은 private platform과 listed-parent value capture를 분리해야 한다.",
        "- F&F TaylorMade는 M&A event premium이지 본업 브랜드 rerating 증거가 아니다.",
        "",
        "쉬운 예: `as_of_date=2025-06-05`에 d'Alba가 미국 매장 입점 논의를 했더라도, 실제 매장 회전율과 반복 발주가 없으면 Stage 3-Green이 아니다.",
    ]
    return "\n".join(lines) + "\n"


def render_round196_green_gate_review_markdown() -> str:
    lines = [
        "# Round-196 R5 Loop-7 Green Gate Review",
        "",
        "## Green Required Evidence",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND196_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Green Forbidden Patterns", ""])
    lines.extend(f"- `{field}`" for field in ROUND196_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "| --- | --- | ---: | --- |"])
    for adjustment in ROUND196_SCORE_ADJUSTMENTS:
        lines.append(f"| `{adjustment.axis}` | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these weights to production scoring yet.",
            "- Do not use Round196 cases as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds to force promotion.",
            "- Do not invent sell-through, reorder, OPM, inventory, receivables, stage prices, or MFE/MAE.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round196_price_backfill_plan_markdown() -> str:
    lines = [
        "# Round-196 R5 Loop-7 Price Backfill Plan",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND196_PRICE_BACKFILL_FIELDS)
    lines.extend(["", "## Priority Cases", "", "| case | stage marker | current status | 4B status | hard 4C |", "| --- | --- | --- | --- | --- |"])
    for case in ROUND196_CASE_CANDIDATES:
        stage_marker = case.stage3_date or case.stage2_date or case.stage4b_date or case.stage1_date
        lines.append(
            f"| `{case.case_id}` | {_date_text(stage_marker) or 'undated'} | "
            f"{case.price_validation_status} | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} |"
        )
    lines.extend(
        [
            "",
            "## Backfill Rule",
            "",
            "- Use official OHLC data for exact MFE/MAE.",
            "- Keep unknown values null or `needs_ohlc_backfill`.",
            "- Split retail-talks, IPO, M&A, and holdco premium price paths from structural consumer evidence.",
            "- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round196_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round-196 R5 Loop-7 Stage 4B / 4C Review",
        "",
        "## 4B Status Definitions",
        "",
        "- `watch`: price or valuation runs ahead of verified sell-through, OPM, FCF, or channel quality.",
        "- `elevated`: competition, inventory, receivables, tariffs, or channel weakness becomes material.",
        "- `graduated`: beat/channel news no longer surprises and growth normalizes.",
        "",
        "## Hard 4C Gates",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND196_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C confirmed | interpretation |", "| --- | --- | --- | --- |"])
    for case in ROUND196_CASE_CANDIDATES:
        lines.append(
            f"| `{case.case_id}` | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    rows_tuple = tuple(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows_tuple[0].keys()), lineterminator="\n")
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow(dict(row))
    return path


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


__all__ = [
    "ROUND196_CASE_CANDIDATES",
    "ROUND196_DEFAULT_AUDIT_PATH",
    "ROUND196_DEFAULT_CASES_PATH",
    "ROUND196_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND196_GREEN_FORBIDDEN_PATTERNS",
    "ROUND196_GREEN_REQUIRED_FIELDS",
    "ROUND196_HARD_4C_GATES",
    "ROUND196_PRICE_BACKFILL_FIELDS",
    "ROUND196_REQUIRED_TARGET_ALIASES",
    "ROUND196_SCORE_ADJUSTMENTS",
    "ROUND196_SOURCE_ROUND_PATH",
    "ROUND196_STAGE4B_STATUSES",
    "Round196CaseCandidate",
    "Round196ScoreAdjustment",
    "render_round196_green_gate_review_markdown",
    "render_round196_price_backfill_plan_markdown",
    "render_round196_stage4b_4c_review_markdown",
    "render_round196_summary_markdown",
    "round196_audit_payload",
    "round196_case_records",
    "round196_case_rows",
    "round196_price_backfill_field_rows",
    "round196_score_adjustment_rows",
    "round196_summary",
    "round196_target_alias_rows",
    "write_round196_r5_loop7_reports",
]
