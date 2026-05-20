"""Round-269 R13 Loop-12 cross-archetype RedTeam validation pack.

Round 269 converts ``docs/round/round_269.md`` into structured,
calibration-only case records. It does not change production scoring, staging,
or candidate generation.

Easy example: SK Hynix can be a valid old Stage 3 success and still be a
current 4B-watch case after a huge price and market-cap rerating. A Samsung
E&A mega-contract is different: it stays Stage 2 until progress revenue, EPC
margin, working capital, and cash collection close.
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


ROUND269_SOURCE_ROUND_PATH = "docs/round/round_269.md"
ROUND269_ANALYST_ROUND_ID = "round_197"
ROUND269_LARGE_SECTOR = "CROSS_ARCHETYPE_REDTEAM_PRICE_VALIDATION"
ROUND269_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round269_r13_loop12_cross_archetype_redteam_price_validation"
ROUND269_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r13_loop12_round269.jsonl"
ROUND269_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round269_r13_loop12_cross_archetype_redteam_price_validation_audit.json"
ROUND269_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round269_r13_loop12_v1.csv"
ROUND269_DEFAULT_STAGE3_BIAS = "redteam_first_after_price_validation"

ROUND269_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "TRUE_STRUCTURAL_RERATING": E2RArchetype.TRUE_STRUCTURAL_RERATING.value,
    "STRUCTURAL_SUCCESS_NOW_4B": E2RArchetype.STRUCTURAL_SUCCESS_NOW_4B.value,
    "CONTRACT_HEADLINE_STAGE2_NOT_GREEN": E2RArchetype.CONTRACT_HEADLINE_STAGE2_NOT_GREEN.value,
    "POLICY_CAPEX_FALSE_POSITIVE": E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE.value,
    "DIGITAL_POLICY_PRICE_ONLY": E2RArchetype.DIGITAL_POLICY_PRICE_ONLY.value,
    "PLATFORM_TRUST_4C_WATCH": E2RArchetype.PLATFORM_TRUST_4C_WATCH.value,
    "CONTRACT_QUALITY_HARD_4C": E2RArchetype.CONTRACT_QUALITY_HARD_4C.value,
    "OPERATIONAL_TRUST_HARD_4C": E2RArchetype.OPERATIONAL_TRUST_HARD_4C.value,
    "MACRO_GEOPOLITICAL_HARD_4C": E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C.value,
}

ROUND269_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "revenue_eps_fcf_conversion_confirmed",
    "price_path_after_evidence",
    "actual_calloff_or_delivery_confirmed",
    "contract_margin_and_cash_collection_confirmed",
    "platform_trust_and_security_cleared",
    "policy_to_revenue_bridge_confirmed",
    "capex_roi_funding_and_utilization_confirmed",
    "no_4b_overheat_signal",
    "no_hard_4c",
)

ROUND269_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "contract_headline_only",
    "policy_capex_without_roi",
    "stablecoin_policy_theme_only",
    "mna_without_trust_or_closing",
    "ipo_or_event_pop_only",
    "single_product_or_single_theme_concentration",
    "unconfirmed_revenue_bridge",
    "data_breach_or_safety_failure",
    "macro_shock_unhedged",
)

ROUND269_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "stage3_after_3x_to_5x_or_more_move",
    "market_cap_milestone_headline",
    "contract_announcement_day_plus_5_to_10pct_move",
    "policy_stablecoin_or_ai_fiscal_story_two_to_three_x_move",
    "mna_announcement_before_regulatory_or_trust_gate",
    "ipo_celebrity_or_policy_event_pop",
    "index_or_sector_fomo_without_revenue_model",
)

ROUND269_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation_or_value_collapse",
    "actual_calloff_failure",
    "data_breach_or_security_failure",
    "fatal_safety_accident",
    "exchange_abnormal_withdrawal_or_hack",
    "macro_energy_chokepoint_shock",
    "fx_disorderly_depreciation",
    "labor_strike_threatens_national_exports",
    "legal_block_on_final_contract",
    "capex_funding_failure",
)

ROUND269_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "peak_return_from_stage3",
    "market_cap_anchor",
    "contract_value_anchor",
    "trust_break_cost_anchor",
    "macro_cost_anchor",
    "policy_or_theme_revenue_bridge",
    "hard_4c_before_price_damage",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round269ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round269ShadowWeightRow:
    archetype: E2RArchetype
    evidence_price_alignment: int
    revenue_eps_fcf: int
    actual_calloff_delivery: int
    cash_collection: int
    operating_leverage: int
    platform_trust: int
    safety_security_trust: int
    macro_energy_fx_overlay: int
    hard_4c_prevention: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "stage3_evidence_price_alignment": _signed(self.evidence_price_alignment),
            "revenue_eps_fcf": _signed(self.revenue_eps_fcf),
            "actual_calloff_delivery": _signed(self.actual_calloff_delivery),
            "cash_collection": _signed(self.cash_collection),
            "operating_leverage": _signed(self.operating_leverage),
            "platform_trust": _signed(self.platform_trust),
            "safety_security_trust": _signed(self.safety_security_trust),
            "macro_energy_fx_overlay": _signed(self.macro_energy_fx_overlay),
            "hard_4c_prevention": _signed(self.hard_4c_prevention),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round269DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round269CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    source_sector: str
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
    peak_return_from_stage3_pct: float | None
    extra_price_metrics: Mapping[str, float | str | bool]
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


ROUND269_SCORE_ADJUSTMENTS: tuple[Round269ScoreAdjustment, ...] = (
    Round269ScoreAdjustment("stage3_evidence_to_price_alignment", 5, "raise", "Stage 3는 증거 뒤 가격경로가 따라와야 검증된다."),
    Round269ScoreAdjustment("revenue_EPS_FCF_conversion", 5, "raise", "좋은 이야기가 아니라 매출/EPS/FCF로 닫혀야 한다."),
    Round269ScoreAdjustment("actual_calloff_or_delivery", 5, "raise", "계약은 실제 call-off, 납품, 인도까지 봐야 한다."),
    Round269ScoreAdjustment("cash_collection_quality", 5, "raise", "EPC/계약은 현금회수 전 Green이 아니다."),
    Round269ScoreAdjustment("operating_leverage", 4, "raise", "실적 레버리지가 확인된 구조만 high-conviction으로 간다."),
    Round269ScoreAdjustment("platform_trust", 5, "raise", "플랫폼은 M&A보다 신뢰/보안/출금 통제가 먼저다."),
    Round269ScoreAdjustment("safety_security_trust", 5, "raise", "안전·보안 사고는 즉시 thesis gate다."),
    Round269ScoreAdjustment("macro_energy_FX_overlay", 5, "raise", "에너지·FX shock은 전 섹터 위에 덮이는 hard overlay다."),
    Round269ScoreAdjustment("hard_4C_prevention", 5, "raise", "계약취소·보안·안전·매크로 4C를 조기에 잡아야 한다."),
    Round269ScoreAdjustment("contract_headline_only", -5, "lower", "수주 headline은 margin/cash 전 Stage 2다."),
    Round269ScoreAdjustment("policy_CAPEX_without_ROI", -5, "lower", "CAPEX headline은 funding/ROI/utilization 전 false positive가 될 수 있다."),
    Round269ScoreAdjustment("stablecoin_policy_theme_only", -5, "lower", "license/reserve income/fee revenue 전 stablecoin 테마는 Green 금지다."),
    Round269ScoreAdjustment("M&A_without_trust_or_closing", -4, "lower", "M&A는 closing과 trust 회복 전 Stage 2/4C-watch다."),
    Round269ScoreAdjustment("IPO_or_event_pop_only", -5, "lower", "IPO·celebrity·event pop은 가격검증 전 구조적 증거가 아니다."),
    Round269ScoreAdjustment("single_product_or_single_theme_concentration", -4, "lower", "단일 제품/테마 concentration은 4B-watch를 빠르게 켠다."),
    Round269ScoreAdjustment("unconfirmed_revenue_bridge", -5, "lower", "정책·테마가 매출로 닫히지 않으면 Stage 3 금지다."),
    Round269ScoreAdjustment("data_breach_or_safety_failure", -5, "lower", "보안/안전 failure는 hard 4C로 격상한다."),
    Round269ScoreAdjustment("macro_shock_unhedged", -5, "lower", "hedge 없는 macro shock은 개별 thesis보다 먼저 본다."),
)


ROUND269_SHADOW_WEIGHT_ROWS: tuple[Round269ShadowWeightRow, ...] = (
    Round269ShadowWeightRow(E2RArchetype.TRUE_STRUCTURAL_RERATING, 5, 5, 4, 4, 5, 2, 2, 2, 3, -1, 4, 3, "SK Hynix and Samyang show evidence-to-price alignment."),
    Round269ShadowWeightRow(E2RArchetype.STRUCTURAL_SUCCESS_NOW_4B, 5, 5, 4, 4, 5, 2, 2, 2, 4, -2, 5, 4, "Large MFE or market-cap milestone requires 4B-watch."),
    Round269ShadowWeightRow(E2RArchetype.CONTRACT_HEADLINE_STAGE2_NOT_GREEN, 3, 3, 5, 5, 3, 1, 2, 1, 4, -5, 5, 5, "Samsung E&A and LGES show contract headline must clear call-off/margin/cash."),
    Round269ShadowWeightRow(E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE, 2, 2, 1, 2, 2, 1, 2, 2, 4, -5, 5, 5, "Hyundai Steel shows CAPEX headline without ROI can fail."),
    Round269ShadowWeightRow(E2RArchetype.DIGITAL_POLICY_PRICE_ONLY, 1, 1, 0, 0, 1, 5, 3, 5, 5, -5, 5, 5, "Stablecoin basket moved before regulated revenue and FX gate."),
    Round269ShadowWeightRow(E2RArchetype.PLATFORM_TRUST_4C_WATCH, 3, 3, 1, 2, 4, 5, 5, 4, 5, -5, 5, 5, "NAVER/Dunamu shows M&A needs closing and trust recovery."),
    Round269ShadowWeightRow(E2RArchetype.CONTRACT_QUALITY_HARD_4C, 0, 0, 5, 5, 0, 1, 2, 2, 5, 0, 3, 5, "LGES contract cancellations are hard 4C."),
    Round269ShadowWeightRow(E2RArchetype.OPERATIONAL_TRUST_HARD_4C, 0, 0, 0, 0, 0, 5, 5, 3, 5, 0, 4, 5, "Jeju and SKT show safety/security hard gates."),
    Round269ShadowWeightRow(E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C, 0, 0, 0, 0, 0, 2, 3, 5, 5, 0, 5, 5, "Middle East/Iran shock confirms macro hard 4C overlay."),
)


ROUND269_DEEP_SUB_ARCHETYPES: tuple[Round269DeepSubArchetype, ...] = (
    Round269DeepSubArchetype("성공 benchmark / HBM", E2RArchetype.STRUCTURAL_SUCCESS_NOW_4B, ("SK Hynix HBM", "AI memory", "OP revision", "Stage 3 success", "market cap $942B", "4B-watch")),
    Round269DeepSubArchetype("성공 benchmark / K-food", E2RArchetype.TRUE_STRUCTURAL_RERATING, ("Samyang Foods Buldak", "export", "ASP", "capacity", "OP revision", "single-SKU 4B-watch")),
    Round269DeepSubArchetype("계약 headline Stage 2", E2RArchetype.CONTRACT_HEADLINE_STAGE2_NOT_GREEN, ("Samsung E&A", "Fadhili", "Saudi Aramco", "EPC margin", "working capital", "cash collection")),
    Round269DeepSubArchetype("정책 CAPEX false positive", E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE, ("Hyundai Steel", "Louisiana steel plant", "tariff hedge", "funding unclear", "ROI unclear")),
    Round269DeepSubArchetype("디지털 policy price-only", E2RArchetype.DIGITAL_POLICY_PRICE_ONLY, ("KRW stablecoin", "Kakao Pay", "LG CNS", "Aton", "ME2ON", "issuer license")),
    Round269DeepSubArchetype("플랫폼 M&A trust gate", E2RArchetype.PLATFORM_TRUST_4C_WATCH, ("NAVER Financial", "Dunamu", "Upbit", "abnormal withdrawal", "exchange trust")),
    Round269DeepSubArchetype("계약품질 hard 4C", E2RArchetype.CONTRACT_QUALITY_HARD_4C, ("LGES", "Ford cancellation", "Freudenberg cancellation", "lost expected revenue", "actual call-off")),
    Round269DeepSubArchetype("운영신뢰 hard 4C", E2RArchetype.OPERATIONAL_TRUST_HARD_4C, ("Jeju Air crash", "SK Telecom data breach", "USIM replacement", "fine", "revenue forecast cut")),
    Round269DeepSubArchetype("거시 지정학 hard 4C", E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C, ("Middle East / Iran", "KOSPI -12.06%", "KRW 1505.8", "Hyundai -15.8%", "Samsung -11.7%")),
)


ROUND269_CASE_CANDIDATES: tuple[Round269CaseCandidate, ...] = (
    Round269CaseCandidate(
        case_id="r13_loop12_sk_hynix_true_stage3_now_4b",
        symbol="000660",
        company_name="SK Hynix",
        source_sector="R2",
        primary_archetype=E2RArchetype.STRUCTURAL_SUCCESS_NOW_4B,
        secondary_archetypes=(E2RArchetype.TRUE_STRUCTURAL_RERATING, E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="structural_success",
        round_case_type="structural_success_plus_4b_watch",
        stage1_date=date(2024, 5, 1),
        stage2_date=date(2024, 6, 25),
        stage3_date=date(2024, 6, 25),
        stage4b_date=date(2026, 5, 14),
        stage4c_date=None,
        stage3_decision="hbm_dominance_dram_price_recovery_and_op_revision_validated_stage3_but_2026_market_cap_milestone_requires_4b_watch",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("hbm_sold_out_ai_memory_bottleneck", "dram_price_recovery", "op_estimate_2024_30tn_krw", "op_estimate_2025_53tn_krw", "target_price_290000", "stage3_price_222000", "q2_2024_op_5_47tn_krw", "q2_2024_revenue_16_4tn_krw", "hbm_shipments_more_than_double_next_year"),
        red_flag_fields=("reported_2025_return_274pct", "reported_2026_return_above_200pct", "market_cap_milestone_942bn_usd", "crowding_watch"),
        price_data_source="MarketWatch / Reuters reported anchors",
        reported_price_anchor="Stage 3 anchor 222,000 KRW; 2026 market cap about $942B",
        reported_return_anchor="Target 290,000 KRW (+30.6%); 2025 +274%; 2026 >+200%; from under $100B to about $942B",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=222000.0,
        stage3_price_anchor=222000.0,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=842.0,
        extra_price_metrics={"target_price_krw": 290000.0, "target_upside_pct": 30.6, "op_estimate_2024_krw_tn": 30.0, "op_estimate_2025_krw_tn": 53.0, "q2_2024_op_krw_tn": 5.47, "q2_2024_revenue_krw_tn": 16.4, "q2_2024_revenue_growth_pct": 125.0, "reported_return_2025_pct": 274.0, "reported_return_2026_min_pct": 200.0, "market_cap_2026_usd_bn": 942.0, "market_cap_mfe_from_under_100b_pct": 842.0},
        score_price_alignment="aligned",
        round_alignment_label="aligned_but_now_4B",
        rerating_result="true_rerating",
        round_rerating_label="true_structural_rerating",
        stage_failure_type="green_success",
        round_stage_failure_label="green_success_then_4b_watch",
        price_validation_status="reported_anchor_not_full_ohlc",
        notes="Stage 3 worked; current state is 4B-watch due massive return and market-cap milestone.",
    ),
    Round269CaseCandidate(
        case_id="r13_loop12_samyang_kfood_export_stage3_candidate",
        symbol="003230",
        company_name="Samyang Foods",
        source_sector="R5/R12",
        primary_archetype=E2RArchetype.TRUE_STRUCTURAL_RERATING,
        secondary_archetypes=(E2RArchetype.K_FOOD_EXPORT_ASP_CAPACITY, E2RArchetype.K_FOOD_SINGLE_HERO_PRODUCT, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="success_candidate",
        round_case_type="structural_success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 6, 14),
        stage3_date=date(2024, 6, 14),
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="export_asp_capacity_and_op_revision_align_but_single_sku_concentration_remains_4b_watch",
        stage4b_status="4B-single-SKU-watch",
        hard_4c_confirmed=False,
        evidence_fields=("buldak_global_export_demand", "asp_increase", "us_europe_shipment_increase", "capacity_expansion", "q2_op_estimate_81_2bn_krw", "op_growth_estimate_84pct", "stage3_price_647000", "target_price_830000"),
        red_flag_fields=("single_sku_concentration_watch", "channel_inventory_watch", "margin_peak_watch"),
        price_data_source="MarketWatch / WSJ Market Talk reported anchor",
        reported_price_anchor="Stage 3 anchor 647,000 KRW, shares closed +5.7%",
        reported_return_anchor="Target 830,000 KRW (+28.3%); Q2 OP estimate 81.2B KRW, +84% YoY",
        mfe_1d=5.7,
        mae_1d=None,
        stage2_price_anchor=647000.0,
        stage3_price_anchor=647000.0,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"implied_prior_close_krw": 611921.0, "target_price_krw": 830000.0, "target_upside_pct": 28.3, "q2_op_estimate_krw_bn": 81.2, "op_growth_estimate_pct": 84.0},
        score_price_alignment="aligned",
        round_alignment_label="aligned_partial",
        rerating_result="true_rerating",
        round_rerating_label="K_food_export_ASP_capacity_rerating_candidate",
        stage_failure_type="yellow_success",
        round_stage_failure_label="single_SKU_4B_watch",
        price_validation_status="reported_anchor_not_full_ohlc",
        notes="Export, ASP, capacity and OP revision aligned; single-SKU concentration remains 4B-watch.",
    ),
    Round269CaseCandidate(
        case_id="r13_loop12_samsung_ea_fadhili_contract_stage2",
        symbol="028050",
        company_name="Samsung E&A",
        source_sector="R1/R10",
        primary_archetype=E2RArchetype.CONTRACT_HEADLINE_STAGE2_NOT_GREEN,
        secondary_archetypes=(E2RArchetype.STAGE2_STRONG_NOT_GREEN, E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3, E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL),
        case_type="success_candidate",
        round_case_type="success_candidate_plus_event_premium",
        stage1_date=date(2024, 4, 3),
        stage2_date=date(2024, 4, 3),
        stage3_date=None,
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        stage3_decision="signed_mega_order_is_stage2_not_green_until_progress_revenue_epc_margin_working_capital_and_cash_collection_close",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("fadhili_contract_estimated_6bn_usd", "aramco_total_project_7_7bn_usd", "gas_processing_capacity_plus_60pct", "event_price_26750_krw", "event_mfe_8_5pct", "target_price_35000_krw"),
        red_flag_fields=("contract_headline_only", "progress_revenue_unconfirmed", "epc_margin_unconfirmed", "working_capital_unconfirmed", "cash_collection_unconfirmed"),
        price_data_source="WSJ reported contract and event-return anchor",
        reported_price_anchor="Event price 26,750 KRW; implied prior 24,654 KRW",
        reported_return_anchor="Shares +8.5%; KOSPI -1.4%; relative outperformance +9.9pp",
        mfe_1d=8.5,
        mae_1d=None,
        stage2_price_anchor=26750.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=26750.0,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"implied_prior_price_krw": 24654.0, "kospi_same_context_pct": -1.4, "relative_outperformance_pp": 9.9, "contract_value_usd_bn": 6.0, "total_project_value_usd_bn": 7.7, "contract_share_of_total_pct": 77.9, "target_price_krw": 35000.0, "target_upside_from_event_price_pct": 30.8},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="EPC_order_stage2_not_green",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="contract_headline_without_margin_cash",
        price_validation_status="reported_anchor_not_full_ohlc",
        notes="Signed mega-order is Stage 2; margin and cash collection are required before Green.",
    ),
    Round269CaseCandidate(
        case_id="r13_loop12_hyundai_steel_us_capex_false_positive",
        symbol="004020",
        company_name="Hyundai Steel",
        source_sector="R4/R10",
        primary_archetype=E2RArchetype.POLICY_CAPEX_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.REGIONAL_POLICY_CAPEX_EVENT_PREMIUM, E2RArchetype.FALSE_POSITIVE_SCORE),
        case_type="failed_rerating",
        round_case_type="policy_capex_false_positive",
        stage1_date=date(2025, 3, 24),
        stage2_date=date(2025, 3, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 22),
        stage3_decision="us_policy_capex_tariff_hedge_story_failed_without_funding_roi_and_utilization_clarity",
        stage4b_status="not_applicable",
        hard_4c_confirmed=False,
        evidence_fields=("louisiana_steel_plant_5_8bn_usd", "hyundai_group_us_package_21bn_usd", "tariff_hedge_story", "low_carbon_steel_localization"),
        red_flag_fields=("policy_capex_without_roi", "funding_unclear", "roi_unclear", "political_signaling_risk", "relative_underperformance_after_capex"),
        price_data_source="Reuters U.S. steel plant / investor backlash anchor",
        reported_price_anchor="Stock lost 21.2% since announcement; KOSPI -5.5%",
        reported_return_anchor="Relative underperformance vs KOSPI -15.7pp; funding details unclear",
        mfe_1d=None,
        mae_1d=-21.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"plant_investment_usd_bn": 5.8, "group_us_investment_package_usd_bn": 21.0, "post_announcement_drawdown_pct": -21.2, "posco_same_period_pct": -18.3, "kospi_same_period_pct": -5.5, "relative_underperformance_vs_kospi_pp": -15.7, "borrowing_share_pct": 50.0, "remaining_funding_unclear": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="false_positive_score",
        rerating_result="no_rerating",
        round_rerating_label="policy_CAPEX_failed_rerating",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="CAPEX_without_ROI_and_funding",
        price_validation_status="reported_anchor_not_full_ohlc",
        notes="Policy CAPEX without funding/ROI failed price validation.",
    ),
    Round269CaseCandidate(
        case_id="r13_loop12_stablecoin_policy_overheat",
        symbol="KakaoPay/LG_CNS/Aton/ME2ON/KRW",
        company_name="Stablecoin policy basket",
        source_sector="R6/R11",
        primary_archetype=E2RArchetype.DIGITAL_POLICY_PRICE_ONLY,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_POLICY_OVERHEAT, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE, E2RArchetype.EVENT_PREMIUM),
        case_type="overheat",
        round_case_type="overheat_plus_4c_watch",
        stage1_date=date(2025, 6, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 6, 1),
        stage4c_date=date(2025, 7, 1),
        stage3_decision="stablecoin_policy_basket_is_price_moved_without_evidence_until_license_reserve_income_fee_revenue_and_fx_gate_clear",
        stage4b_status="4B-elevated",
        hard_4c_confirmed=False,
        evidence_fields=("won_stablecoin_policy_expectation", "digital_asset_reform", "retail_leverage_expansion", "kakao_pay_above_2x", "lg_cns_plus_70pct", "aton_plus_80pct", "me2on_3x", "margin_loans_20_5tn_krw"),
        red_flag_fields=("stablecoin_policy_theme_only", "issuer_license_unconfirmed", "reserve_income_unconfirmed", "fee_revenue_unconfirmed", "bok_fx_capital_flow_warning"),
        price_data_source="FT / Reuters stablecoin policy and FX-risk anchors",
        reported_price_anchor="Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x",
        reported_return_anchor="No issuer license, reserve income, or fee revenue confirmed; margin loans 20.5T KRW",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"kakao_pay_mfe_pct_min": 100.0, "lg_cns_mfe_pct": 70.0, "aton_mfe_pct": 80.0, "me2on_mfe_pct": 200.0, "margin_loans_krw_tn": 20.5, "proposed_issuer_equity_krw_mn": 500.0, "capital_outflow_context_usd_bn": 19.0, "issuer_license_confirmed": False, "reserve_income_confirmed": False, "fee_revenue_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence",
        rerating_result="theme_overheat",
        round_rerating_label="stablecoin_policy_overheat",
        stage_failure_type="false_yellow",
        round_stage_failure_label="4B_before_regulated_revenue",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Stablecoin policy moved prices before regulated revenue and before FX gate cleared.",
    ),
    Round269CaseCandidate(
        case_id="r13_loop12_naver_dunamu_platform_trust_watch",
        symbol="035420",
        company_name="NAVER / NAVER Financial / Dunamu",
        source_sector="R8/R6",
        primary_archetype=E2RArchetype.PLATFORM_TRUST_4C_WATCH,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE, E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_plus_event_premium_plus_4c_watch",
        stage1_date=date(2025, 11, 27),
        stage2_date=date(2025, 11, 27),
        stage3_date=None,
        stage4b_date=date(2025, 11, 27),
        stage4c_date=date(2025, 11, 27),
        stage3_decision="platform_mna_stage2_but_green_blocked_until_closing_regulatory_approval_trust_recovery_and_revenue_bridge",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("naver_financial_dunamu_all_stock_deal", "deal_value_15_13tn_krw", "deal_value_10_27bn_usd", "exchange_ratio_2_54", "upbit_market_share_70pct", "naver_initial_plus_7pct"),
        red_flag_fields=("mna_without_trust_or_closing", "abnormal_withdrawal_54bn_krw", "exchange_trust_gate_open", "regulatory_approval_unconfirmed", "revenue_bridge_unconfirmed"),
        price_data_source="Reuters deal / event-return / trust-risk anchor",
        reported_price_anchor="NAVER initially +7%+ but later -4.2%",
        reported_return_anchor="Event swing -11.2pp after 54B KRW abnormal withdrawal from Upbit",
        mfe_1d=7.0,
        mae_1d=-4.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"deal_value_krw_tn": 15.13, "deal_value_usd_bn": 10.27, "exchange_ratio": 2.54, "upbit_market_share_pct": 70.0, "event_initial_mfe_pct": 7.0, "event_later_mae_pct": -4.2, "event_swing_pp": -11.2, "abnormal_withdrawal_krw_bn": 54.0, "loss_covered_by_upbit_assets": True},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_trust_watch",
        rerating_result="event_premium",
        round_rerating_label="digital_asset_platform_merger_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="platform_stage2_with_exchange_trust_4C_watch",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="M&A is Stage 2; abnormal withdrawal creates platform trust 4C-watch.",
    ),
    Round269CaseCandidate(
        case_id="r13_loop12_lges_contract_quality_hard_4c",
        symbol="373220",
        company_name="LG Energy Solution",
        source_sector="R3",
        primary_archetype=E2RArchetype.CONTRACT_QUALITY_HARD_4C,
        secondary_archetypes=(E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK, E2RArchetype.CONTRACT_QUALITY_BREAK, E2RArchetype.FALSE_POSITIVE_SCORE),
        case_type="4c_thesis_break",
        round_case_type="contract_quality_hard_4c",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 26),
        stage3_decision="battery_contract_headline_failed_actual_calloff_and_expected_revenue_visibility",
        stage4b_status="not_applicable",
        hard_4c_confirmed=True,
        evidence_fields=("ford_cancelled_contract_9_6tn_krw", "freudenberg_cancelled_order_3_9tn_krw", "total_lost_expected_revenue_13_5tn_krw", "lges_2024_revenue_25_62tn_krw"),
        red_flag_fields=("contract_cancellation_or_value_collapse", "actual_calloff_failure", "lost_revenue_vs_revenue_52_7pct", "ev_customer_demand_risk"),
        price_data_source="Reuters contract-cancellation anchor",
        reported_price_anchor="Ford 9.6T KRW and Freudenberg 3.9T KRW cancellations",
        reported_return_anchor="Total lost expected revenue 13.5T KRW, 52.7% of 2024 revenue",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"ford_cancelled_contract_krw_tn": 9.6, "freudenberg_cancelled_contract_krw_tn": 3.9, "total_lost_expected_revenue_krw_tn": 13.5, "lges_2024_revenue_krw_tn": 25.62, "lost_revenue_vs_2024_revenue_pct": 52.7},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="battery_contract_quality_failure",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C",
        price_validation_status="reported_contract_anchor_not_full_ohlc",
        notes="Contract headline failed actual call-off; hard 4C.",
    ),
    Round269CaseCandidate(
        case_id="r13_loop12_hard_4c_reference_pack_jeju_skt_macro",
        symbol="089590/017670/KOSPI/KRW",
        company_name="Jeju Air / SK Telecom / Middle East-Iran shock",
        source_sector="R8/R11",
        primary_archetype=E2RArchetype.OPERATIONAL_TRUST_HARD_4C,
        secondary_archetypes=(E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C, E2RArchetype.OPERATIONAL_TRUST_AND_MACRO_HARD_4C, E2RArchetype.AIRLINE_SAFETY_OPERATIONAL_TRUST_4C),
        case_type="4c_thesis_break",
        round_case_type="safety_security_macro_hard_4c_reference_pack",
        stage1_date=date(2024, 12, 30),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 30),
        stage3_decision="safety_security_and_macro_shocks_are_hard_4c_reference_gates_not_general_redteam_only",
        stage4b_status="not_applicable",
        hard_4c_confirmed=True,
        evidence_fields=("jeju_air_fatal_crash_179_deaths", "skt_cyberattack_data_breach", "middle_east_iran_kospi_minus_12_06pct", "krw_1505_8_per_usd"),
        red_flag_fields=("fatal_safety_accident", "data_breach_or_security_failure", "exchange_or_system_trust_break", "macro_energy_chokepoint_shock", "fx_disorderly_depreciation"),
        price_data_source="Reuters hard-4C reported anchors",
        reported_price_anchor="Jeju Air 6,920 KRW event low; KOSPI 5,093.54 macro close",
        reported_return_anchor="Jeju -15.7%; SKT -8.5% intraday / -6.7% close; KOSPI -12.06%",
        mfe_1d=None,
        mae_1d=-15.7,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=5093.54,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"jeju_event_low_price_krw": 6920.0, "jeju_intraday_mae_pct": -15.7, "jeju_market_cap_wipeout_krw_bn": 95.7, "skt_intraday_mae_pct": -8.5, "skt_close_mae_pct": -6.7, "skt_relative_underperformance_pp": -6.8, "skt_affected_users_mn": 23.0, "skt_leaked_data_pieces_mn": 26.96, "skt_data_protection_investment_krw_bn": 700.0, "skt_revenue_forecast_cut_krw_bn": 800.0, "skt_fine_krw_bn": 134.0, "kospi_mae_pct": -12.06, "kospi_close": 5093.54, "market_cap_wipeout_2d_usd_bn": 553.82, "krw_low_per_usd": 1505.8, "hyundai_motor_mae_pct": -15.8, "samsung_electronics_mae_pct": -11.7, "sk_hynix_mae_pct": -9.6},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="hard_4C_reference_pack",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="safety_security_macro_hard_gate",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Safety, cybersecurity and macro energy shock confirm hard 4C gates.",
    ),
)


def round269_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("revenue", "eps", "fcf", "op_", "revision", "hbm", "export", "asp", "capacity", "price_path")
    for candidate in ROUND269_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND269_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round269 R13 Loop-12 cross-archetype RedTeam price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "price" in field or "return" in field or "market_cap" in field or "event" in field or "mfe" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "cancellation" in field
                or "collapse" in field
                or "failure" in field
                or "breach" in field
                or "accident" in field
                or "trust" in field
                or "macro" in field
                or "fx" in field
                or "shock" in field
            ),
            must_have_fields=ROUND269_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND269_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                f"r13_default_stage3_bias_{ROUND269_DEFAULT_STAGE3_BIAS}",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_contract_policy_stablecoin_platform_or_hard_4c_event_as_green_alone",
                *ROUND269_GREEN_REQUIRED_FIELDS,
                *ROUND269_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_price=candidate.peak_price_anchor,
                peak_return_from_stage3=candidate.peak_return_from_stage3_pct,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=candidate.stage2_price_anchor is not None
                or candidate.stage3_price_anchor is not None
                or candidate.stage4b_price_anchor is not None
                or candidate.stage4c_price_anchor is not None
                or candidate.mfe_1d is not None
                or candidate.mae_1d is not None,
                stage_dates_confidence=0.85 if candidate.stage3_date or candidate.stage4c_date else 0.75,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round269_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND269_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "source_sector": candidate.source_sector,
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
                "price_data_source": candidate.price_data_source,
                "reported_price_anchor": candidate.reported_price_anchor,
                "reported_return_anchor": candidate.reported_return_anchor,
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mae_1d": _float_text(candidate.mae_1d),
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


def round269_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND269_SCORE_ADJUSTMENTS)


def round269_shadow_weight_rows() -> tuple[dict[str, str]]:
    return tuple(row.as_row() for row in ROUND269_SHADOW_WEIGHT_ROWS)


def round269_deep_sub_archetype_rows() -> tuple[dict[str, str]]:
    return tuple(row.as_row() for row in ROUND269_DEEP_SUB_ARCHETYPES)


def round269_price_validation_field_rows() -> tuple[dict[str, str]]:
    return tuple({"field": field, "required_for_round269_price_validation": "true"} for field in ROUND269_PRICE_VALIDATION_FIELDS)


def round269_target_alias_rows() -> tuple[dict[str, str]]:
    return tuple({"round269_label": label, "canonical_archetype": canonical} for label, canonical in ROUND269_REQUIRED_TARGET_ALIASES.items())


def round269_summary() -> dict[str, int | bool | str]:
    cases = ROUND269_CASE_CANDIDATES
    return {
        "source_round": ROUND269_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND269_ANALYST_ROUND_ID,
        "large_sector": ROUND269_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.stage4b_status or case.stage4b_date is not None),
        "stage4c_case_count": sum(1 for case in cases if case.stage4c_date is not None),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "aligned_count": sum(1 for case in cases if case.score_price_alignment == "aligned"),
        "target_archetype_count": len(ROUND269_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND269_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND269_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "r13_default_stage3_bias": ROUND269_DEFAULT_STAGE3_BIAS,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round269_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND269_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND269_ANALYST_ROUND_ID,
        "large_sector": ROUND269_LARGE_SECTOR,
        "summary": round269_summary(),
        "target_aliases": dict(ROUND269_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND269_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND269_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND269_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND269_HARD_4C_GATES),
        "deep_sub_archetypes": round269_deep_sub_archetype_rows(),
        "shadow_weights": round269_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round269_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_contract_policy_stablecoin_platform_or_hard_4c_event_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "do_not_weaken_stage3_green_to_improve_recall",
        ],
    }


def render_round269_summary_markdown() -> str:
    summary = round269_summary()
    lines = [
        "# Round 269 R13 Loop 12 Cross-Archetype RedTeam Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- analyst_round_id: {summary['analyst_round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- structural_success: {summary['structural_success_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C dated cases: {summary['stage4c_case_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- aligned_count: {summary['aligned_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | source | type | stage3 | 4B | 4C | round alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND269_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.source_sector,
                    case.case_type,
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
            "- SK Hynix is the clearest Stage 3 success benchmark, but current state is 4B-watch.",
            "- Samyang Foods is aligned K-food export/ASP/capacity evidence, with single-SKU 4B-watch risk.",
            "- Samsung E&A is signed-contract Stage 2, not Green, until margin and cash collection close.",
            "- Hyundai Steel is policy CAPEX false positive because price failed before funding/ROI clarity.",
            "- Stablecoin basket is price_moved_without_evidence before licensed revenue and FX gate clearance.",
            "- NAVER/Dunamu is platform M&A Stage 2 plus trust 4C-watch.",
            "- LGES, Jeju Air, SK Telecom, and Middle East/Iran are hard 4C reference anchors.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round269_green_gate_review_markdown() -> str:
    lines = [
        "# Round 269 R13 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND269_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND269_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `HBM + OP revision + price path` can validate Stage 3, but a later 3x-5x+ move can still become 4B-watch.",
            "- `signed EPC contract + +8.5% event return` is Stage 2/4B-watch until margin and cash collection appear.",
            "- `stablecoin policy + 2x basket rally` is price_moved_without_evidence until regulated revenue appears.",
            "- `contract cancellation`, `data breach`, `fatal crash`, or `macro energy shock` are hard 4C gates.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round269_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 269 R13 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND269_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND269_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B is about price prepayment, graduation, crowding, and event premium.",
            "- 4C is about thesis break: contract cancellation, safety, security, exchange trust, or macro shock.",
            "- Price-only rallies stay watch items until revenue, EPS, FCF, licensed economics, or trust recovery are visible.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND269_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round269_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 269 R13 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- r13_default_stage3_bias: redteam_first_after_price_validation",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND269_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round269_r13_loop12_reports(
    output_directory: str | Path = ROUND269_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND269_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND269_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round269_case_records(), cases_path),
        "audit": _write_json(round269_audit_payload(), audit_path),
        "summary": output / "round269_r13_loop12_price_validation_summary.md",
        "case_matrix": output / "round269_r13_loop12_case_matrix.csv",
        "target_aliases": output / "round269_r13_loop12_target_aliases.csv",
        "score_adjustments": output / "round269_r13_loop12_score_adjustments.csv",
        "shadow_weights": output / "round269_r13_loop12_shadow_weights.csv",
        "deep_sub_archetypes": output / "round269_r13_loop12_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round269_r13_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round269_r13_loop12_green_gate_review.md",
        "price_validation_plan": output / "round269_r13_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round269_r13_loop12_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round269_summary_markdown(), encoding="utf-8")
    _write_csv(round269_case_rows(), paths["case_matrix"])
    _write_csv(round269_target_alias_rows(), paths["target_aliases"])
    _write_csv(round269_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round269_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round269_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round269_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round269_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round269_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round269_stage4b_4c_review_markdown(), encoding="utf-8")
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
    return f"{value:+d}"
