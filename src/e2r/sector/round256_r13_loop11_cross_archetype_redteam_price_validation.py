"""Round-256 R13 Loop-11 cross-archetype RedTeam validation pack.

Round 256 converts ``docs/round/round_256.md`` into structured,
calibration-only case records. It does not change production scoring.

Easy example: SK Hynix shows that a valid Stage 3 can later require 4B-watch
after a 5x-plus price path. A Samsung E&A contract headline is different: it is
strong Stage 2 until progress revenue, EPC margin, and cash collection close.
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


ROUND256_SOURCE_ROUND_PATH = "docs/round/round_256.md"
ROUND256_ANALYST_ROUND_ID = "round_184"
ROUND256_LARGE_SECTOR = "CROSS_ARCHETYPE_REDTEAM_PRICE_VALIDATION"
ROUND256_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round256_r13_loop11_cross_archetype_redteam_price_validation"
ROUND256_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r13_loop11_round256.jsonl"
ROUND256_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round256_r13_loop11_cross_archetype_redteam_price_validation_audit.json"
ROUND256_DEFAULT_STAGE3_BIAS = "redteam_first_after_price_validation"

ROUND256_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "STRUCTURAL_SUCCESS_ALIGNED": E2RArchetype.STRUCTURAL_SUCCESS_ALIGNED.value,
    "STRUCTURAL_SUCCESS_BUT_4B_WATCH": E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH.value,
    "CONTRACT_HEADLINE_STAGE2_NOT_GREEN": E2RArchetype.STAGE2_STRONG_NOT_GREEN.value,
    "AI_CAPITAL_ALLOCATION_EVENT_PREMIUM": E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM.value,
    "POLICY_DIGITAL_ASSET_PRICE_ONLY": E2RArchetype.DIGITAL_ASSET_POLICY_OVERHEAT.value,
    "EVIDENCE_GOOD_BUT_PRICE_FAILED": E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED.value,
    "CONTRACT_QUALITY_HARD_4C": E2RArchetype.CONTRACT_QUALITY_HARD_4C.value,
    "OPERATIONAL_TRUST_HARD_4C": E2RArchetype.OPERATIONAL_TRUST_HARD_4C.value,
    "MACRO_GEOPOLITICAL_HARD_4C": E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C.value,
}

ROUND256_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "revenue_eps_fcf_conversion_confirmed",
    "price_path_after_evidence",
    "stage3_to_large_mfe_confirmation",
    "mae_not_excessive",
    "actual_calloff_margin_cash_collection_for_contracts",
    "paid_usage_arpu_trust_for_platforms",
    "capacity_utilization_supply_continuity_for_manufacturing",
    "no_hard_4c",
    "no_macro_hard_overlay",
)

ROUND256_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_news_only",
    "ai_capital_allocation_without_revenue",
    "stablecoin_policy_theme_only",
    "contract_headline_without_margin",
    "customer_name_without_calloff",
    "mna_or_facility_without_utilization",
    "ipo_debut_or_listing_story",
    "good_news_but_price_failed_for_green",
    "data_breach_or_security_failure",
    "factory_fire_or_supply_disruption",
    "macro_energy_fx_shock_ignored",
)

ROUND256_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "stage3_after_3x_to_5x_price_move",
    "market_cap_milestone_headline",
    "large_contract_day_plus_5_to_10pct_move",
    "ai_mna_cb_event_plus_20pct_move",
    "stablecoin_policy_theme_two_to_three_x_move",
    "ipo_debut_after_short_term_double",
    "good_news_with_weak_price_response",
    "valuation_moves_ahead_of_evidence",
    "single_brand_or_customer_concentration_above_80pct",
)

ROUND256_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "contract_value_collapse",
    "actual_calloff_failure",
    "operational_trust_break",
    "data_breach_or_security_failure",
    "security_or_privacy_breach_with_revenue_cut",
    "factory_fire_or_supply_disruption",
    "fatal_safety_accident",
    "regulatory_reversal",
    "geopolitical_energy_chokepoint_shock",
    "krw_disorderly_depreciation",
    "macro_circuit_breaker_or_index_crash",
)

ROUND256_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "fresh_rerating_response",
    "hard_4c_before_price_damage",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round256ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round256ShadowWeightRow:
    archetype: E2RArchetype
    price_path_alignment: int
    stage3_mfe_confirmation: int
    revenue_eps_conversion: int
    actual_contract_quality: int
    operational_trust: int
    macro_risk_overlay: int
    event_penalty: int
    capex_funding_redteam: int
    governance_security_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "price_path_alignment": _signed(self.price_path_alignment),
            "stage3_mfe_confirmation": _signed(self.stage3_mfe_confirmation),
            "revenue_eps_conversion": _signed(self.revenue_eps_conversion),
            "actual_contract_quality": _signed(self.actual_contract_quality),
            "operational_trust": _signed(self.operational_trust),
            "macro_risk_overlay": _signed(self.macro_risk_overlay),
            "event_penalty": _signed(self.event_penalty),
            "capex_funding_redteam": _signed(self.capex_funding_redteam),
            "governance_security_redteam": _signed(self.governance_security_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round256DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round256CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    source_sector: str
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


ROUND256_SCORE_ADJUSTMENTS: tuple[Round256ScoreAdjustment, ...] = (
    Round256ScoreAdjustment("stage3_to_large_MFE_confirmation", 5, "raise", "SK하이닉스처럼 Stage 3 이후 대형 MFE가 확인되면 성공 기준점이 된다."),
    Round256ScoreAdjustment("revenue_or_EPS_conversion", 5, "raise", "Stage 3 이후 가격경로는 revenue/EPS/FCF 전환과 함께 확인해야 한다."),
    Round256ScoreAdjustment("commercial_revenue_conversion", 5, "raise", "AI·stablecoin·시설·정책 이벤트는 상업 매출 전환 전 Green이 아니다."),
    Round256ScoreAdjustment("actual_calloff_or_take_or_pay", 5, "raise", "실제 인출·take-or-pay는 계약 품질을 높인다."),
    Round256ScoreAdjustment("cash_collection_quality", 5, "raise", "EPC·계약·시설 투자는 현금회수까지 봐야 한다."),
    Round256ScoreAdjustment("price_path_alignment", 5, "raise", "증거 뒤 가격이 따라와야 성공 검증이고, 가격이 먼저 달리면 4B다."),
    Round256ScoreAdjustment("fresh_rerating_response", 4, "raise", "좋은 뉴스에도 가격이 실패하면 fresh rerating으로 보지 않는다."),
    Round256ScoreAdjustment("operational_trust", 5, "raise", "운영 신뢰는 항공·서비스·플랫폼의 hard gate다."),
    Round256ScoreAdjustment("security_privacy_trust", 5, "raise", "보안·개인정보 훼손은 매출전망과 보상비용으로 이어진다."),
    Round256ScoreAdjustment("macro_risk_overlay", 5, "raise", "Hormuz/Iran 같은 거시 shock은 모든 섹터 위에 덮이는 hard gate다."),
    Round256ScoreAdjustment("contract_headline_without_margin", -5, "lower", "EPC 수주 headline은 progress revenue, margin, cash collection 전 Stage 2다."),
    Round256ScoreAdjustment("AI_capital_allocation_without_revenue", -5, "lower", "AI 투자·CB 이벤트는 recurring AI revenue 전 Stage 2/4B다."),
    Round256ScoreAdjustment("stablecoin_policy_theme_only", -5, "lower", "발행권·reserve income·fee revenue 전 stablecoin 테마는 event premium이다."),
    Round256ScoreAdjustment("IPO_debut_or_listing_story", -5, "lower", "IPO·상장 스토리는 가격 실패 가능성을 별도 검증해야 한다."),
    Round256ScoreAdjustment("M&A_or_facility_without_utilization", -5, "lower", "시설·M&A는 utilization과 margin 없이 Green이 아니다."),
    Round256ScoreAdjustment("customer_name_without_calloff", -5, "lower", "고객명만 있고 실제 call-off가 없으면 계약품질 hard 4C에 취약하다."),
    Round256ScoreAdjustment("good_news_but_price_failed", -4, "lower", "좋은 evidence라도 가격이 실패하면 fresh rerating 축은 낮춘다."),
    Round256ScoreAdjustment("data_breach_or_security_failure", -5, "lower", "보안사고는 비용·벌금·매출전망 훼손으로 이어지는 hard gate다."),
    Round256ScoreAdjustment("factory_fire_or_supply_disruption", -5, "lower", "공장화재·생산중단은 수요보다 먼저 보는 hard gate다."),
    Round256ScoreAdjustment("macro_energy_FX_shock", -5, "lower", "에너지·FX shock은 섹터 중립이 아니라 한국 시장 hard overlay다."),
)


ROUND256_SHADOW_WEIGHT_ROWS: tuple[Round256ShadowWeightRow, ...] = (
    Round256ShadowWeightRow(E2RArchetype.STRUCTURAL_SUCCESS_ALIGNED, 5, 5, 5, 4, 3, 2, 0, 0, 0, 4, 2, "SK Hynix and APR prove Stage 3 can produce large MFE when revenue/EPS conversion exists."),
    Round256ShadowWeightRow(E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH, 5, 5, 5, 4, 3, 2, -1, 1, 1, 5, 3, "Large MFE, market-cap milestone, or concentration requires 4B-watch."),
    Round256ShadowWeightRow(E2RArchetype.STAGE2_STRONG_NOT_GREEN, 3, 1, 3, 4, 2, 1, -3, 2, 1, 5, 3, "Samsung E&A contract headline is strong Stage 2 until margin and cash collection close."),
    Round256ShadowWeightRow(E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM, 3, 2, 3, 2, 3, 2, -5, 3, 2, 5, 3, "Samsung SDS KKR event is Stage 2 and 4B before AI revenue/FCF."),
    Round256ShadowWeightRow(E2RArchetype.DIGITAL_ASSET_POLICY_OVERHEAT, 0, 0, 0, 0, 1, 3, -5, 1, 3, 5, 4, "Stablecoin rallies are price_moved_without_evidence until licensing/revenue clarity."),
    Round256ShadowWeightRow(E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED, 3, -2, 4, 2, 2, 1, -4, 2, 1, 3, 2, "LG CNS and SamsungBio show good evidence is not fresh rerating when price response fails."),
    Round256ShadowWeightRow(E2RArchetype.CONTRACT_QUALITY_HARD_4C, 0, 0, 0, 5, 2, 1, 0, 1, 1, 3, 5, "LGES and L&F contract cancellations/value collapse are hard 4C."),
    Round256ShadowWeightRow(E2RArchetype.OPERATIONAL_TRUST_HARD_4C, 0, 0, 0, 0, 5, 2, 0, 0, 5, 3, 5, "SK Telecom breach and Kumho factory fire are operational trust hard 4C."),
    Round256ShadowWeightRow(E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C, 0, 0, 0, 0, 3, 5, 0, 2, 2, 4, 5, "Hormuz/Iran shock is cross-sector macro hard 4C."),
)


ROUND256_DEEP_SUB_ARCHETYPES: tuple[Round256DeepSubArchetype, ...] = (
    Round256DeepSubArchetype("성공 benchmark / HBM", E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH, ("SK Hynix HBM", "ASML EUV order", "AI memory", "EPS revision", "stage3 to +551.8% MFE", "market-cap milestone")),
    Round256DeepSubArchetype("성공 검증 / K-beauty device", E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH, ("APR", "Medicube", "K-beauty device", "overseas revenue growth", "single-brand concentration")),
    Round256DeepSubArchetype("계약 headline Stage 2", E2RArchetype.STAGE2_STRONG_NOT_GREEN, ("Samsung E&A", "Fadhili", "Saudi Aramco", "EPC margin", "progress revenue", "cash collection")),
    Round256DeepSubArchetype("AI capital allocation 4B", E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM, ("Samsung SDS", "KKR convertible bond", "AI infrastructure", "M&A", "capital allocation", "recurring AI revenue required")),
    Round256DeepSubArchetype("디지털자산 policy overheat", E2RArchetype.DIGITAL_ASSET_POLICY_OVERHEAT, ("KRW stablecoin", "Kakao Pay", "LG CNS", "Aton", "ME2ON", "issuer license", "reserve income")),
    Round256DeepSubArchetype("좋은 증거 but price failed", E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED, ("LG CNS IPO", "Samsung Biologics GSK facility", "cloud AI IPO", "U.S. CDMO facility", "fresh rerating failed")),
    Round256DeepSubArchetype("계약품질 hard 4C", E2RArchetype.CONTRACT_QUALITY_HARD_4C, ("LGES", "Ford cancellation", "Freudenberg cancellation", "L&F Tesla cathode", "contract value collapse", "actual call-off")),
    Round256DeepSubArchetype("운영신뢰 hard 4C", E2RArchetype.OPERATIONAL_TRUST_HARD_4C, ("SK Telecom data breach", "Kumho Tire factory fire", "security fine", "revenue forecast cut", "production suspension")),
    Round256DeepSubArchetype("거시 지정학 hard 4C", E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C, ("Hormuz", "Iran shock", "KOSPI -12.06%", "KRW 1505.8", "macro hard 4C")),
)


ROUND256_CASE_CANDIDATES: tuple[Round256CaseCandidate, ...] = (
    Round256CaseCandidate(
        case_id="r13_loop11_sk_hynix_hbm_structural_success_4b_watch",
        symbol="000660",
        company_name="SK하이닉스",
        source_sector="R2",
        primary_archetype=E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH,
        secondary_archetypes=(E2RArchetype.STRUCTURAL_SUCCESS_ALIGNED, E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="structural_success",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 6, 25),
        stage3_date=date(2024, 6, 25),
        stage4b_date=date(2026, 5, 4),
        stage4c_date=None,
        stage3_decision="hbm_dominance_eps_revision_and_memory_price_upcycle_validated_stage3_success_but_plus_551_8pct_mfe_requires_4b_watch",
        stage4b_status="4B-watch/elevated",
        hard_4c_confirmed=False,
        evidence_fields=("hbm_demand", "dram_price_upcycle", "op_forecast_2024_30tn_krw", "op_forecast_2025_53tn_krw", "target_price_290000", "asml_euv_order_11_95tn_krw", "stage3_price_222000", "record_high_1447000"),
        red_flag_fields=("market_cap_milestone_headline", "reported_2025_return_274pct", "reported_2026_return_above_200pct", "crowding_watch"),
        price_data_source="MarketWatch / Reuters reported price and return anchors",
        reported_price_anchor="222,000 KRW Stage 3 anchor to 1,447,000 KRW reported record high",
        reported_return_anchor="MFE +551.8%; ASML EUV event +5.7%; 2025 +274%; 2026 >+200%; market cap about $942B",
        mfe_1d=5.7,
        mae_1d=None,
        stage2_price_anchor=222000.0,
        stage3_price_anchor=222000.0,
        stage4b_price_anchor=1447000.0,
        stage4c_price_anchor=None,
        peak_price_anchor=1447000.0,
        peak_return_from_stage3_pct=551.8,
        extra_price_metrics={"op_forecast_2024_krw_tn": 30.0, "op_forecast_2025_krw_tn": 53.0, "target_price_krw": 290000.0, "asml_euv_order_krw_tn": 11.95, "asml_euv_order_usd_bn": 7.97, "asml_event_return_pct": 5.7, "reported_return_2025_pct": 274.0, "reported_return_2026_pct_min": 200.0, "minimum_compounded_return_from_2025_start_pct": 1022.0, "market_cap_2026_usd_bn": 942.0, "minimum_market_cap_mfe_pct": 842.0},
        score_price_alignment="aligned",
        round_alignment_label="aligned",
        rerating_result="true_rerating",
        round_rerating_label="true_structural_rerating",
        stage_failure_type="green_success",
        round_stage_failure_label="green_success_then_4b_watch",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Loop 11 전체의 Stage 3 성공 benchmark다. 다만 5배 이상 MFE 이후에는 신규 Green이 아니라 4B-watch다.",
    ),
    Round256CaseCandidate(
        case_id="r13_loop11_apr_medicube_structural_concentration_4b",
        symbol="278470",
        company_name="APR / Medicube",
        source_sector="R5",
        primary_archetype=E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH,
        secondary_archetypes=(E2RArchetype.STRUCTURAL_SUCCESS_ALIGNED, E2RArchetype.BEAUTY_DEVICE_EXPORT, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="structural_success",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 1, 1),
        stage3_date=date(2025, 10, 1),
        stage4b_date=date(2025, 10, 1),
        stage4c_date=None,
        stage3_decision="overseas_sell_through_and_revenue_growth_support_stage3_candidate_but_medicube_91_7pct_concentration_requires_4b_watch",
        stage4b_status="4B-concentration-watch",
        hard_4c_confirmed=False,
        evidence_fields=("q4_revenue_440m_usd_plus_124pct", "q4_overseas_revenue_362m_usd_plus_203pct", "overseas_share_87pct", "fy_revenue_1_2bn_usd", "medicube_revenue_1_1bn_usd", "tiktok_shop_revenue_102_9m_usd", "amazon_prime_day_sales_22m_usd", "ulta_1400_stores"),
        red_flag_fields=("single_brand_device_concentration", "medicube_revenue_share_91_7pct", "valuation_premium_after_rapid_growth", "fast_product_cycle_watch"),
        price_data_source="Vogue Business reported revenue/channel anchors",
        reported_price_anchor="No adjusted OHLC in this pass; revenue and channel anchors only",
        reported_return_anchor="Q4 revenue +124%; overseas +203%; Medicube revenue share 91.7%",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"q4_2025_revenue_usd_mn": 440.0, "q4_2025_revenue_growth_pct": 124.0, "q4_2025_overseas_revenue_usd_mn": 362.0, "q4_2025_overseas_growth_pct": 203.0, "overseas_revenue_share_pct": 87.0, "fy_2025_revenue_usd_bn": 1.2, "medicube_fy_2025_revenue_usd_bn": 1.1, "medicube_revenue_share_pct": 91.7, "tiktok_shop_revenue_usd_mn": 102.9, "amazon_prime_day_sales_usd_mn": 22.0, "ulta_store_count_min": 1400.0},
        score_price_alignment="aligned",
        round_alignment_label="aligned_partial",
        rerating_result="true_rerating",
        round_rerating_label="K_beauty_structural_rerating",
        stage_failure_type="green_success",
        round_stage_failure_label="green_success_candidate_plus_concentration_4b_watch",
        price_validation_status="revenue_channel_anchor_not_full_ohlc",
        notes="실제 sell-through와 해외매출이 찍힌 구조 후보지만 Medicube 매출집중도 91.7% 때문에 4B-watch를 동시에 올린다.",
    ),
    Round256CaseCandidate(
        case_id="r13_loop11_samsung_ea_fadhili_contract_stage2_4b",
        symbol="028050",
        company_name="Samsung E&A Fadhili",
        source_sector="R1/R10",
        primary_archetype=E2RArchetype.STAGE2_STRONG_NOT_GREEN,
        secondary_archetypes=(E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3, E2RArchetype.CONTRACT_BACKLOG_INDUSTRIAL, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="success_candidate",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 3),
        stage3_date=None,
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        stage3_decision="signed_6bn_usd_epc_contract_is_strong_stage2_but_progress_revenue_margin_and_cash_collection_required_before_green",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("saudi_aramco_fadhili_contract_6bn_usd", "total_fadhili_package_7_7bn_usd", "event_price_26750_krw", "event_mfe_8_5pct", "target_price_35000_krw"),
        red_flag_fields=("contract_headline_without_margin", "progress_revenue_unconfirmed", "epc_margin_unconfirmed", "cash_collection_unconfirmed", "price_moves_before_cash_conversion"),
        price_data_source="WSJ reported contract and event-return anchor",
        reported_price_anchor="26,750 KRW event price; implied prior 24,654 KRW",
        reported_return_anchor="Shares +8.5%; KOSPI -1.4%; relative outperformance +9.9pp",
        mfe_1d=8.5,
        mae_1d=None,
        stage2_price_anchor=26750.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=26750.0,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"implied_prior_price_krw": 24654.0, "kospi_same_context_return_pct": -1.4, "relative_outperformance_pp": 9.9, "contract_value_usd_bn": 6.0, "total_fadhili_package_usd_bn": 7.7, "contract_share_of_total_pct": 77.9, "target_price_krw": 35000.0, "target_upside_from_event_price_pct": 30.8},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_success_candidate",
        rerating_result="event_premium",
        round_rerating_label="EPC_order_stage2_not_green",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="should_not_be_green_until_margin_cash_collection",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="약 $6B 수주는 강한 Stage 2지만, 공정률·마진·현금회수 전에는 Stage 3-Green이 아니다.",
    ),
    Round256CaseCandidate(
        case_id="r13_loop11_samsung_sds_stablecoin_ai_digital_event_premium",
        symbol="018260/377300/LG_CNS/Aton/ME2ON",
        company_name="Samsung SDS + KRW stablecoin basket",
        source_sector="R6/R8",
        primary_archetype=E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_POLICY_OVERHEAT, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE, E2RArchetype.EVENT_PREMIUM),
        case_type="overheat",
        stage1_date=date(2025, 6, 1),
        stage2_date=date(2026, 4, 15),
        stage3_date=None,
        stage4b_date=date(2026, 4, 15),
        stage4c_date=None,
        stage3_decision="ai_capital_allocation_and_stablecoin_policy_are_stage2_or_stage1_but_revenue_before_green_and_price_rallies_are_4b",
        stage4b_status="4B-elevated",
        hard_4c_confirmed=False,
        evidence_fields=("samsung_sds_kkr_cb_820m_usd", "existing_cash_6_4tn_krw", "ai_infrastructure_mna_narrative", "stablecoin_policy_pledge", "stablecoin_basket_two_to_three_x_moves", "margin_loan_20_5tn_krw"),
        red_flag_fields=("ai_capital_allocation_without_revenue", "stablecoin_policy_theme_only", "issuer_license_unconfirmed", "reserve_income_unconfirmed", "fee_revenue_unconfirmed", "price_moved_before_revenue"),
        price_data_source="Reuters / FT reported event-return anchors",
        reported_price_anchor="Samsung SDS +20.8%; Kakao Pay >2x; LG CNS +70%; Aton +80%; ME2ON 3x",
        reported_return_anchor="No issuer license, reserve income, fee revenue, or recurring AI revenue confirmed",
        mfe_1d=20.8,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"samsung_sds_event_mfe_pct": 20.8, "samsung_sds_morning_return_pct": 19.4, "kospi_same_context_return_pct": 3.0, "samsung_sds_relative_outperformance_pp": 17.8, "kkr_cb_investment_usd_mn": 820.0, "samsung_sds_existing_cash_krw_trn": 6.4, "combined_cash_plus_cb_krw_trn": 7.607, "kakao_pay_mfe_pct_min": 100.0, "lg_cns_mfe_pct": 70.0, "aton_mfe_pct": 80.0, "me2on_mfe_pct": 200.0, "margin_loan_context_krw_trn": 20.5, "issuer_license_confirmed": False, "reserve_income_confirmed": False, "fee_revenue_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence_event_premium",
        rerating_result="event_premium",
        round_rerating_label="AI_digital_policy_4B",
        stage_failure_type="false_yellow",
        round_stage_failure_label="should_have_been_stage1_or_4B_watch",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="AI 자본조달과 stablecoin 정책은 Stage 2/1 신호가 될 수 있지만, 매출 전 +20~200%는 Green이 아니라 4B다.",
    ),
    Round256CaseCandidate(
        case_id="r13_loop11_lg_cns_samsung_biologics_good_evidence_price_failed",
        symbol="LG_CNS/207940",
        company_name="LG CNS + Samsung Biologics",
        source_sector="R7/R8",
        primary_archetype=E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED,
        secondary_archetypes=(E2RArchetype.CDMO_HEALTHCARE_CONTRACT, E2RArchetype.FALSE_POSITIVE_SCORE),
        case_type="failed_rerating",
        stage1_date=date(2025, 2, 5),
        stage2_date=date(2025, 12, 21),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="cloud_ai_ipo_and_us_cdmo_facility_are_good_stage2_evidence_but_price_failed_so_green_threshold_should_not_be_lowered",
        stage4b_status="not_applicable",
        hard_4c_confirmed=False,
        evidence_fields=("lg_cns_cloud_ai_more_than_half_sales", "lg_cns_1q_3q_2024_revenue_4tn_krw", "lg_cns_1q_3q_2024_op_313bn_krw", "samsung_biologics_gsk_rockville_facility_280m_usd", "samsung_biologics_capacity_60000l"),
        red_flag_fields=("good_news_but_price_failed", "fresh_rerating_response_missing", "ipo_debut_below_offer", "facility_utilization_unconfirmed", "margin_fcf_conversion_unconfirmed"),
        price_data_source="Reuters reported IPO/facility event anchors",
        reported_price_anchor="LG CNS IPO 61,900 KRW vs debut 59,700 KRW; SamsungBio event -0.4%",
        reported_return_anchor="LG CNS -3.55%; SamsungBio -0.4% while KOSPI +2.0%",
        mfe_1d=None,
        mae_1d=-3.55,
        stage2_price_anchor=61900.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"lg_cns_ipo_price_krw": 61900.0, "lg_cns_debut_trade_krw": 59700.0, "lg_cns_debut_mae_pct": -3.55, "lg_cns_revenue_1q_3q_2024_krw_tn": 4.0, "lg_cns_op_1q_3q_2024_krw_bn": 313.0, "lg_cns_op_margin_pct": 7.8, "samsung_biologics_gsk_facility_value_usd_mn": 280.0, "samsung_biologics_facility_capacity_l": 60000.0, "samsung_biologics_event_mae_pct": -0.4, "kospi_same_context_return_pct": 2.0, "samsung_biologics_relative_underperformance_pp": -2.4},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        round_rerating_label="good_evidence_but_no_fresh_rerating",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="wait_for_revenue_margin_fcf",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="좋은 사업 evidence가 있어도 가격 반응이 실패하면 fresh rerating 축을 낮추고 Green threshold를 낮추지 않는다.",
    ),
    Round256CaseCandidate(
        case_id="r13_loop11_lges_lnf_contract_quality_hard_4c",
        symbol="373220/066970",
        company_name="LGES / L&F contract-quality hard 4C",
        source_sector="R3/R4",
        primary_archetype=E2RArchetype.CONTRACT_QUALITY_HARD_4C,
        secondary_archetypes=(E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK, E2RArchetype.CONTRACT_QUALITY_BREAK, E2RArchetype.FALSE_POSITIVE_SCORE),
        case_type="4c_thesis_break",
        stage1_date=date(2023, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 29),
        stage3_decision="battery_customer_and_contract_headlines_are_not_green_without_actual_calloff_volume_take_or_pay_margin_and_cash_collection",
        stage4b_status="not_applicable",
        hard_4c_confirmed=True,
        evidence_fields=("lges_ford_cancelled_contract_9_6tn_krw", "lges_freudenberg_cancelled_contract_3_9tn_krw", "lges_total_lost_expected_revenue_13_5tn_krw", "lnf_tesla_contract_2_9bn_usd_to_7386_usd"),
        red_flag_fields=("contract_cancellation", "contract_value_collapse", "actual_calloff_failure", "customer_name_without_calloff", "ev_demand_slowdown", "take_or_pay_unconfirmed"),
        price_data_source="Reuters contract-cancellation / contract-value-collapse anchors",
        reported_price_anchor="Stock OHLC unavailable beyond contract cancellation/value-collapse anchors",
        reported_return_anchor="LGES lost 13.5T KRW expected revenue; L&F Tesla deal collapsed from $2.9B to $7,386",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"lges_ford_cancelled_contract_krw_tn": 9.6, "lges_freudenberg_cancelled_contract_krw_tn": 3.9, "lges_total_lost_expected_revenue_krw_tn": 13.5, "lges_2024_revenue_krw_tn": 25.62, "lges_lost_revenue_vs_2024_revenue_pct": 52.7, "lnf_initial_contract_value_usd_bn": 2.9, "lnf_revised_contract_value_usd": 7386.0, "lnf_contract_value_collapse_pct": 99.999745},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="battery_contract_quality_failure",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C",
        price_validation_status="reported_contract_anchor_not_full_ohlc",
        notes="고객명·계약금액 headline은 actual call-off, volume, take-or-pay, margin, cash collection 없이는 Green이 아니다.",
    ),
    Round256CaseCandidate(
        case_id="r13_loop11_skt_kumho_operational_trust_hard_4c",
        symbol="017670/073240",
        company_name="SK Telecom / Kumho Tire operational trust hard 4C",
        source_sector="R8/R9",
        primary_archetype=E2RArchetype.OPERATIONAL_TRUST_HARD_4C,
        secondary_archetypes=(E2RArchetype.SECURITY_OPERATIONAL_TRUST_HARD_4C, E2RArchetype.OPERATIONAL_TRUST_BREAK, E2RArchetype.FALSE_POSITIVE_SCORE),
        case_type="4c_thesis_break",
        stage1_date=date(2025, 4, 28),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 28),
        stage3_decision="data_breach_and_factory_fire_are_operational_trust_breaks_that_block_platform_or_mobility_recovery_green",
        stage4b_status="not_applicable",
        hard_4c_confirmed=True,
        evidence_fields=("skt_data_breach", "skt_26_96m_user_data_pieces_leaked", "skt_revenue_forecast_cut_800bn_krw", "skt_security_investment_700bn_krw", "skt_fine_134bn_krw", "kumho_factory_fire_capacity_12m_tires"),
        red_flag_fields=("data_breach_or_security_failure", "security_privacy_trust_break", "revenue_forecast_cut", "regulatory_fine", "factory_fire_or_supply_disruption", "production_suspension"),
        price_data_source="Reuters breach / fine / factory-fire anchors",
        reported_price_anchor="SKT close -6.7%; Kumho -8.0%",
        reported_return_anchor="SKT revenue forecast cut 800B KRW, security investment 700B KRW, fine 134B KRW; Kumho plant nearly 20% global capacity",
        mfe_1d=None,
        mae_1d=-8.5,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"skt_initial_intraday_mae_pct": -8.5, "skt_initial_close_mae_pct": -6.7, "kospi_same_context_return_pct": 0.1, "skt_relative_underperformance_pp": -6.8, "skt_users_initially_affected_mn": 23.0, "skt_data_leak_pieces_mn": 26.96, "skt_july4_mae_pct": -5.6, "skt_security_investment_krw_bn": 700.0, "skt_annualized_security_investment_krw_bn": 140.0, "skt_revenue_forecast_cut_krw_bn": 800.0, "skt_fine_krw_bn": 134.0, "kumho_event_mae_pct": -8.0, "kumho_gwangju_capacity_mn_tires_per_year": 12.0, "kumho_share_of_global_capacity_pct": 20.0},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="operational_trust_break",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="보안·공장·안전·품질 사고는 일반 RedTeam이 아니라 매출성장 점수보다 먼저 보는 hard gate다.",
    ),
    Round256CaseCandidate(
        case_id="r13_loop11_hormuz_iran_macro_hard_4c",
        symbol="KOSPI/KRW/005380/005930/000660",
        company_name="Hormuz / Iran macro energy shock",
        source_sector="R11",
        primary_archetype=E2RArchetype.MACRO_GEOPOLITICAL_HARD_4C,
        secondary_archetypes=(E2RArchetype.MACRO_HARD_4C, E2RArchetype.GEOPOLITICAL_ENERGY_IMPORT_SHOCK, E2RArchetype.POLICY_MARKET_SHOCK_OVERLAY),
        case_type="4c_thesis_break",
        stage1_date=date(2026, 3, 4),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 3, 4),
        stage3_decision="hormuz_iran_energy_fx_shock_is_cross_sector_macro_hard_4c_overlay_not_company_green_evidence",
        stage4b_status="not_applicable",
        hard_4c_confirmed=True,
        evidence_fields=("hormuz_iran_conflict_escalation", "kospi_minus_12_06pct", "krw_1505_8_per_usd", "market_cap_wipeout_553_82bn_usd", "hyundai_minus_15_8pct", "samsung_electronics_minus_11_7pct", "sk_hynix_minus_9_6pct"),
        red_flag_fields=("geopolitical_energy_chokepoint_shock", "macro_energy_fx_shock", "krw_disorderly_depreciation", "macro_circuit_breaker_or_index_crash", "market_wide_riskoff", "oil_import_dependency"),
        price_data_source="Reuters / Barron's macro-market anchors",
        reported_price_anchor="KOSPI 5,093.54; KRW 1,505.8/USD",
        reported_return_anchor="KOSPI -12.06%; Hyundai -15.8%; Samsung Electronics -11.7%; SK Hynix -9.6%; two-day market-cap wipeout $553.82B",
        mfe_1d=None,
        mae_1d=-12.06,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=5093.54,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"kospi_event_mae_pct": -12.06, "kospi_close": 5093.54, "market_cap_wipeout_2d_usd_bn": 553.82, "krw_intraday_low_per_usd": 1505.8, "hyundai_motor_mae_pct": -15.8, "samsung_electronics_mae_pct": -11.7, "sk_hynix_mae_pct": -9.6, "middle_east_oil_import_dependency_pct": 70.0},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="macro_energy_security_hard_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="macro_hard_4C_overlay",
        price_validation_status="reported_macro_market_anchor_not_full_ohlc",
        notes="Hormuz/energy/FX shock은 sector-neutral 악재가 아니라 한국 시장 전체에 덮는 macro hard gate다.",
    ),
)


def round256_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("revenue", "eps", "fcf", "revision", "hbm", "overseas", "margin", "price_path")
    for candidate in ROUND256_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND256_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round256 R13 Loop-11 cross-archetype RedTeam price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "mfe" in field or "price" in field or "market_cap" in field or "valuation" in field or "event" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "break" in field
                or "collapse" in field
                or "accident" in field
                or "breach" in field
                or "failure" in field
                or "cut" in field
                or "cancellation" in field
                or "redteam" in field
                or "chokepoint" in field
                or "oil" in field
                or "macro" in field
            ),
            must_have_fields=ROUND256_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND256_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "r13_default_stage3_bias_redteam_first_after_price_validation",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_policy_stablecoin_cb_macro_or_capex_event_as_green_alone",
                *ROUND256_GREEN_REQUIRED_FIELDS,
                *ROUND256_GREEN_FORBIDDEN_PATTERNS,
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


def round256_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND256_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "source_sector": candidate.source_sector,
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


def round256_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND256_SCORE_ADJUSTMENTS)


def round256_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND256_SHADOW_WEIGHT_ROWS)


def round256_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND256_DEEP_SUB_ARCHETYPES)


def round256_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round256_price_validation": "true"} for field in ROUND256_PRICE_VALIDATION_FIELDS)


def round256_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round256_label": label, "canonical_archetype": canonical} for label, canonical in ROUND256_REQUIRED_TARGET_ALIASES.items())


def round256_summary() -> dict[str, int | bool | str]:
    cases = ROUND256_CASE_CANDIDATES
    return {
        "source_round": ROUND256_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND256_ANALYST_ROUND_ID,
        "large_sector": ROUND256_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND256_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND256_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND256_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "r13_default_stage3_bias": ROUND256_DEFAULT_STAGE3_BIAS,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round256_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND256_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND256_ANALYST_ROUND_ID,
        "large_sector": ROUND256_LARGE_SECTOR,
        "summary": round256_summary(),
        "target_aliases": dict(ROUND256_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND256_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND256_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND256_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND256_HARD_4C_GATES),
        "deep_sub_archetypes": round256_deep_sub_archetype_rows(),
        "shadow_weights": round256_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round256_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_contract_ai_stablecoin_macro_or_operational_event_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "do_not_weaken_stage3_green_to_improve_recall",
        ],
    }


def render_round256_summary_markdown() -> str:
    summary = round256_summary()
    lines = [
        "# Round 256 R13 Loop 11 Cross-Archetype RedTeam Price Validation",
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
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- deep_sub_archetype_count: {summary['deep_sub_archetype_count']}",
        f"- shadow_weight_row_count: {summary['shadow_weight_row_count']}",
        f"- r13_default_stage3_bias: {summary['r13_default_stage3_bias']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | source | type | stage3 | 4B | 4C | round alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND256_CASE_CANDIDATES:
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
            "- SK Hynix and APR/Medicube are aligned structural-success benchmarks, but both need 4B-watch after major rerating.",
            "- Samsung E&A is signed-contract Stage 2, not Green, until progress revenue, margin, and cash collection close.",
            "- Samsung SDS and the stablecoin basket are event premium / price_moved_without_evidence before recurring AI or regulated revenue.",
            "- LG CNS and Samsung Biologics show that good evidence with weak price response should not lower Green gates.",
            "- LGES/L&F and SKT/Kumho are hard 4C anchors for contract quality and operational trust.",
            "- Hormuz/Iran is a macro hard 4C overlay across energy, FX, autos, chips, airlines, and the broad market.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round256_green_gate_review_markdown() -> str:
    lines = [
        "# Round 256 R13 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND256_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND256_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `Stage 3 evidence + large MFE` validates a structural case, but may also trigger 4B-watch.",
            "- `signed EPC contract + event-day +8.5%` is Stage 2/4B-watch until margin and cash collection appear.",
            "- `CB/M&A/AI headline + one-day +20%` is Stage 2/4B-watch until recurring revenue appears.",
            "- `contract cancellation`, `data breach`, `factory fire`, or `geopolitical energy shock` are hard RedTeam gates.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round256_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 256 R13 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND256_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND256_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B is about graduation, crowding, price prepayment, and event premium.",
            "- 4C is about thesis break: contract quality, operational trust, security, factory disruption, or macro shock.",
            "- Price-only rallies stay watch items until company-level revenue, EPS, FCF, or licensed economics are visible.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND256_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round256_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 256 R13 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- r13_default_stage3_bias: redteam_first_after_price_validation",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND256_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round256_r13_loop11_reports(
    output_directory: str | Path = ROUND256_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND256_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND256_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round256_case_records(), cases_path),
        "audit": _write_json(round256_audit_payload(), audit_path),
        "summary": output / "round256_r13_loop11_price_validation_summary.md",
        "case_matrix": output / "round256_r13_loop11_case_matrix.csv",
        "target_aliases": output / "round256_r13_loop11_target_aliases.csv",
        "score_adjustments": output / "round256_r13_loop11_score_adjustments.csv",
        "shadow_weights": output / "round256_r13_loop11_shadow_weights.csv",
        "deep_sub_archetypes": output / "round256_r13_loop11_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round256_r13_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round256_r13_loop11_green_gate_review.md",
        "price_validation_plan": output / "round256_r13_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round256_r13_loop11_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round256_summary_markdown(), encoding="utf-8")
    _write_csv(round256_case_rows(), paths["case_matrix"])
    _write_csv(round256_target_alias_rows(), paths["target_aliases"])
    _write_csv(round256_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round256_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round256_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round256_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round256_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round256_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round256_stage4b_4c_review_markdown(), encoding="utf-8")
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
