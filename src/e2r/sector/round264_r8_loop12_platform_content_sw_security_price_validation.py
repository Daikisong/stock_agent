"""Round-264 R8 Loop-12 platform/content/SW/security price validation pack.

This module converts ``docs/round/round_264.md`` into calibration-only case
records, shadow weights, and guardrail reports. Production scoring and
candidate generation are unchanged.

Easy example: a game IPO can show strong revenue and margin, but it is not
Stage 3-Green until retention, repeat-title evidence, and FCF are visible.
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


ROUND264_SOURCE_ROUND_PATH = "docs/round/round_264.md"
ROUND264_ANALYST_ROUND_ID = "round_192"
ROUND264_LARGE_SECTOR = Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY.value
ROUND264_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round264_r8_loop12_platform_content_sw_security_price_validation"
ROUND264_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r8_loop12_round264.jsonl"
ROUND264_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round264_r8_loop12_platform_content_sw_security_price_validation_audit.json"

ROUND264_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "GAME_IP_IPO_SINGLE_TITLE_RISK": E2RArchetype.GAME_IP_IPO_SINGLE_TITLE_RISK.value,
    "KIDS_CONTENT_IP_IPO_EVENT_PREMIUM": E2RArchetype.KIDS_CONTENT_IP_IPO_EVENT_PREMIUM.value,
    "KPOP_IP_CHINA_OPTIONALITY": E2RArchetype.KPOP_IP_CHINA_OPTIONALITY.value,
    "DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE": E2RArchetype.DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE.value,
    "ECOMMERCE_PLATFORM_DATA_BREACH_4C": E2RArchetype.ECOMMERCE_PLATFORM_DATA_BREACH_4C.value,
    "GAME_STUDIO_M_AND_A_GOVERNANCE_4C": E2RArchetype.GAME_STUDIO_M_AND_A_GOVERNANCE_4C.value,
    "TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C": E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C.value,
}

ROUND264_DEEP_SUB_ARCHETYPES: tuple[str, ...] = (
    "Shift Up game IPO / Nikke live-service / Stellar Blade single-title risk",
    "Pinkfong kids content IPO / Baby Shark legacy IP / repeat-hit durability",
    "SM Entertainment Tencent Music stake / China reopening optionality",
    "NAVER Financial Dunamu Upbit M&A / exchange trust gate",
    "Coupang e-commerce data breach / non-KRX platform trust reference",
    "Krafton Unknown Worlds Subnautica 2 earnout / studio governance 4C-watch",
    "SK Telecom USIM data breach / direct KRX cybersecurity hard 4C",
)

ROUND264_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "paid_user_or_active_user_retention",
    "arpu_take_rate_or_paid_usage",
    "repeat_content_hit_or_live_service_durability",
    "ip_licensing_merchandise_or_platform_fee_revenue",
    "operating_leverage_or_fcf",
    "mna_closing_integration_and_revenue_bridge",
    "platform_or_exchange_trust_intact",
    "cybersecurity_data_governance_risk_passed",
    "price_path_after_evidence",
)

ROUND264_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ipo_pop_only",
    "single_title_hit_only",
    "single_ip_legacy_only",
    "mna_announcement_only",
    "china_reopening_expectation_only",
    "digital_asset_platform_without_trust_recovery",
    "data_breach_unresolved",
    "cybersecurity_remediation_cost_unquantified",
)

ROUND264_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "ipo_first_day_50pct_plus_spike",
    "single_title_or_single_ip_valuation_before_repeat_revenue",
    "mna_announcement_5_to_10pct_spike_before_closing",
    "china_reopening_headline_prices_before_ticket_revenue",
    "platform_deal_prices_before_regulatory_closing",
    "digital_asset_platform_deal_swings_around_trust_incident",
    "content_ip_views_valued_before_paid_monetization",
)

ROUND264_HARD_4C_GATES: tuple[str, ...] = (
    "major_data_breach",
    "cybersecurity_breach_with_revenue_guidance_cut",
    "platform_trust_failure",
    "exchange_abnormal_withdrawal_or_hack",
    "mna_governance_dispute_delays_release",
    "regulatory_approval_failure",
    "content_ip_single_hit_fade",
    "live_service_retention_collapse",
    "large_compensation_fine_or_remediation_cost",
)

ROUND264_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_event_return",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "relative_underperformance_pp",
    "transaction_or_ipo_anchor",
    "revenue_margin_or_user_anchor",
    "trust_security_or_governance_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round264ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round264ShadowWeightRow:
    archetype: E2RArchetype
    paid_retention: int
    arpu_take_rate: int
    repeat_hit: int
    ip_licensing: int
    live_service_retention: int
    platform_trust: int
    cybersecurity_control: int
    data_governance: int
    regulatory_closing: int
    operating_leverage_fcf: int
    event_penalty: int
    trust_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "paid_retention": _signed(self.paid_retention),
            "arpu_take_rate": _signed(self.arpu_take_rate),
            "repeat_hit": _signed(self.repeat_hit),
            "ip_licensing": _signed(self.ip_licensing),
            "live_service_retention": _signed(self.live_service_retention),
            "platform_trust": _signed(self.platform_trust),
            "cybersecurity_control": _signed(self.cybersecurity_control),
            "data_governance": _signed(self.data_governance),
            "regulatory_closing": _signed(self.regulatory_closing),
            "operating_leverage_fcf": _signed(self.operating_leverage_fcf),
            "event_penalty": _signed(self.event_penalty),
            "trust_redteam": _signed(self.trust_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round264CaseCandidate:
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
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    mfe_1d: float | None
    mae_1d: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str | bool | None]
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


ROUND264_SCORE_ADJUSTMENTS: tuple[Round264ScoreAdjustment, ...] = (
    Round264ScoreAdjustment("paid_user_retention", 5, "raise", "게임·콘텐츠·플랫폼은 활성/유료 이용 유지가 반복매출의 첫 관문이다."),
    Round264ScoreAdjustment("arpu_or_take_rate", 5, "raise", "MAU나 조회수보다 ARPU, take-rate, paid usage가 Stage 3 visibility다."),
    Round264ScoreAdjustment("repeat_hit_generation", 5, "raise", "단일 히트보다 반복 흥행과 후속 IP 전환이 중요하다."),
    Round264ScoreAdjustment("ip_licensing_revenue", 5, "raise", "조회수와 팬덤은 licensing, merchandise, platform fee로 닫혀야 한다."),
    Round264ScoreAdjustment("live_service_retention", 5, "raise", "Nikke 같은 live-service 매출은 retention이 확인돼야 지속성이 있다."),
    Round264ScoreAdjustment("platform_trust", 5, "raise", "디지털 플랫폼은 규모보다 거래소·개인정보·운영 신뢰가 먼저다."),
    Round264ScoreAdjustment("cybersecurity_control", 5, "raise", "보안 사고는 매출전망·보상·투자비로 연결될 수 있는 hard gate다."),
    Round264ScoreAdjustment("data_governance", 5, "raise", "플랫폼 데이터 거버넌스는 RedTeam 입력으로 강하게 본다."),
    Round264ScoreAdjustment("regulatory_closing", 4, "raise", "M&A와 중국 optionality는 승인·공연·매출 전환이 확인돼야 한다."),
    Round264ScoreAdjustment("operating_leverage_fcf", 5, "raise", "IP와 플랫폼 매출이 OPM/FCF로 닫히는지 확인한다."),
    Round264ScoreAdjustment("ipo_pop_only", -5, "lower", "IPO 첫날 급등은 event premium이지 Stage 3 증거가 아니다."),
    Round264ScoreAdjustment("single_title_or_single_ip_concentration", -5, "lower", "단일 게임·단일 IP 의존은 4B/4C 감시를 높인다."),
    Round264ScoreAdjustment("mna_deal_without_closing", -4, "lower", "M&A 발표만 있고 closing·integration·revenue bridge가 없으면 제한한다."),
    Round264ScoreAdjustment("china_reopening_optional_only", -4, "lower", "중국 재개 기대는 실제 공연·티켓 매출 전에는 Green이 아니다."),
    Round264ScoreAdjustment("digital_asset_platform_without_trust", -5, "lower", "거래소 trust issue가 있으면 deal value보다 먼저 감점한다."),
    Round264ScoreAdjustment("exchange_abnormal_withdrawal", -5, "lower", "비정상 출금은 플랫폼 M&A의 4C-watch 트리거다."),
    Round264ScoreAdjustment("data_breach", -5, "lower", "대규모 데이터 유출은 플랫폼 논리 훼손이다."),
    Round264ScoreAdjustment("cybersecurity_revenue_cut", -5, "lower", "보안 사고가 매출전망 하향으로 이어지면 hard 4C다."),
    Round264ScoreAdjustment("unlisted_or_non_krx_reference_gap", -3, "lower", "비KRX 참고사례는 직접 후보가 아니라 guardrail로만 쓴다."),
    Round264ScoreAdjustment("event_rally_before_paid_usage", -5, "lower", "유료 사용·ARPU 확인 전 이벤트 랠리는 4B-watch다."),
)

ROUND264_SHADOW_WEIGHT_ROWS: tuple[Round264ShadowWeightRow, ...] = (
    Round264ShadowWeightRow(E2RArchetype.GAME_IP_IPO_SINGLE_TITLE_RISK, 5, 4, 5, 3, 5, 2, 1, 2, 1, 5, -5, 3, 5, 4, "Shift Up is Stage 2/watch until retention, repeat hit, pipeline, OPM and FCF confirm."),
    Round264ShadowWeightRow(E2RArchetype.KIDS_CONTENT_IP_IPO_EVENT_PREMIUM, 4, 3, 5, 5, 3, 2, 1, 2, 1, 4, -5, 2, 5, 3, "Pinkfong IPO pop needs repeat-hit and licensing/merchandise margin before Green."),
    Round264ShadowWeightRow(E2RArchetype.KPOP_IP_CHINA_OPTIONALITY, 3, 4, 4, 4, 2, 3, 1, 2, 4, 4, -4, 3, 4, 3, "SM/Tencent is China optionality; actual concerts and revenue are required."),
    Round264ShadowWeightRow(E2RArchetype.DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE, 2, 4, 1, 1, 0, 5, 5, 5, 5, 3, -5, 5, 5, 5, "NAVER/Dunamu deal is blocked by exchange trust until closing and remediation."),
    Round264ShadowWeightRow(E2RArchetype.ECOMMERCE_PLATFORM_DATA_BREACH_4C, 0, 0, 0, 0, 0, 5, 5, 5, 2, 0, -5, 5, 4, 5, "Coupang is non-KRX platform trust reference; data breach blocks unsafe Green."),
    Round264ShadowWeightRow(E2RArchetype.GAME_STUDIO_M_AND_A_GOVERNANCE_4C, 2, 1, 3, 3, 2, 3, 1, 2, 2, 2, -4, 5, 4, 5, "Krafton/Unknown Worlds needs release revenue and governance clarity."),
    Round264ShadowWeightRow(E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C, 0, 0, 0, 0, 0, 5, 5, 5, 1, 0, -5, 5, 4, 5, "SK Telecom is direct KRX hard 4C from breach, revenue-cut, security spend and compensation."),
)

ROUND264_CASE_CANDIDATES: tuple[Round264CaseCandidate, ...] = (
    Round264CaseCandidate(
        case_id="r8_loop12_shift_up_game_ip_ipo_single_title_watch",
        symbol="462870",
        company_name="Shift Up",
        primary_archetype=E2RArchetype.GAME_IP_IPO_SINGLE_TITLE_RISK,
        secondary_archetypes=(E2RArchetype.GAME_CONTENT_IP, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_4b_watch",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=date(2024, 6, 27),
        stage4c_date=None,
        stage3_decision="ipo_and_hit_title_not_green_until_retention_repeat_title_pipeline_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ipo_raise_435bn_krw", "implied_market_cap_3_5tn_krw", "nikke_sales_255bn_krw", "revenue_2023_169bn_krw", "op_2023_111bn_krw"),
        red_flag_fields=("single_title_concentration", "tencent_platform_risk", "sony_exclusivity_watch", "next_title_delay_risk", "full_ohlc_unavailable"),
        price_data_source="Reuters IPO / sales / earnings anchors",
        reported_price_anchor="IPO raise 435B won, implied market cap 3.5T won; full adjusted OHLC unavailable",
        reported_return_anchor="Valuation/revenue 20.7x and valuation/OP 31.5x before repeat-title proof",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_raise_krw_bn": 435.0, "ipo_raise_usd_mn": 313.0, "implied_market_cap_krw_trn": 3.5, "implied_market_cap_usd_bn": 2.52, "nikke_sales_launch_to_1q2024_krw_bn": 255.0, "revenue_2023_krw_bn": 169.0, "op_2023_krw_bn": 111.0, "op_margin_2023_pct": 65.7, "ipo_valuation_to_revenue_2023": 20.7, "ipo_valuation_to_op_2023": 31.5, "tencent_post_ipo_stake_pct": 35.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="game_IP_IPO_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="IPO_and_hit_title_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Strong game-IP economics, but IPO and hit title are not Green until retention, repeat hit, pipeline and FCF confirm.",
    ),
    Round264CaseCandidate(
        case_id="r8_loop12_pinkfong_kids_content_ip_ipo_event",
        symbol="Pinkfong_newly_listed",
        company_name="Pinkfong Company",
        primary_archetype=E2RArchetype.KIDS_CONTENT_IP_IPO_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.EDUCATION_SPECIALTY_SERVICES, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="kids_content_ipo_event_premium",
        stage1_date=date(2025, 11, 18),
        stage2_date=date(2025, 11, 18),
        stage3_date=None,
        stage4b_date=date(2025, 11, 18),
        stage4c_date=None,
        stage3_decision="ipo_pop_and_legacy_ip_not_green_until_repeat_hit_and_licensing_margin_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ipo_raise_76bn_krw", "baby_shark_16bn_views", "prior_year_sales_97_4bn_krw", "prior_year_op_18_8bn_krw"),
        red_flag_fields=("ipo_pop_only", "single_ip_legacy_only", "repeat_hit_unverified", "licensing_margin_unverified"),
        price_data_source="FT IPO price and financial anchors",
        reported_price_anchor="Intraday +62%, close +9% at 41,550 won; full OHLC unavailable",
        reported_return_anchor="Content IPO event premium before repeat-hit and licensing/merchandise proof",
        mfe_1d=62.0,
        mae_1d=None,
        stage2_price_anchor=38119.0,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_raise_krw_bn": 76.0, "intraday_mfe_pct": 62.0, "close_price_krw": 41550.0, "close_return_pct": 9.0, "implied_ipo_price_krw": 38119.0, "implied_intraday_high_krw": 61552.0, "baby_shark_views_bn": 16.0, "prior_year_sales_krw_bn": 97.4, "prior_year_op_krw_bn": 18.8, "op_margin_pct": 19.3},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium",
        rerating_result="event_premium",
        round_rerating_label="kids_content_IP_IPO_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="IPO_pop_not_repeat_hit_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="IPO pop is 4B/event premium; repeat hit, licensing, merchandise margin and retention are required before Green.",
    ),
    Round264CaseCandidate(
        case_id="r8_loop12_sm_tencent_kpop_china_optionality",
        symbol="041510",
        company_name="SM Entertainment / Tencent Music",
        primary_archetype=E2RArchetype.KPOP_IP_CHINA_OPTIONALITY,
        secondary_archetypes=(E2RArchetype.KPOP_PLATFORM_CONTENT_IP, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_china_optionality_stage2",
        stage1_date=date(2025, 5, 27),
        stage2_date=date(2025, 5, 30),
        stage3_date=None,
        stage4b_date=date(2025, 5, 30),
        stage4c_date=None,
        stage3_decision="shareholder_transaction_not_green_until_china_concert_ticket_revenue_and_regulatory_durability_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("tencent_music_9_7pct_stake", "hybe_sells_2_2m_sm_shares", "transaction_value_243bn_krw", "china_performance_ban_thaw_optionality"),
        red_flag_fields=("china_reopening_expectation_only", "ticket_revenue_unverified", "regulatory_durability_unverified", "kakao_control_governance_watch"),
        price_data_source="Reuters SM / Tencent transaction anchor",
        reported_price_anchor="Tencent Music buys 9.7% stake for 243B won; full adjusted OHLC unavailable",
        reported_return_anchor="Implied SM equity value about 2.51T won before actual China ticket revenue",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stake_sold_pct": 9.7, "shares_sold_mn": 2.2, "transaction_value_krw_bn": 243.0, "transaction_value_usd_mn": 177.0, "implied_sm_equity_value_krw_trn": 2.51, "kakao_kakaoent_control_stake_pct": 42.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="Kpop_China_optional_reopen_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="shareholder_transaction_not_ticket_revenue_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Shareholder transaction and China thaw optionality are Stage 2; ticket revenue and regulatory durability are required before Green.",
    ),
    Round264CaseCandidate(
        case_id="r8_loop12_naver_dunamu_platform_merger_trust_gate",
        symbol="035420",
        company_name="NAVER / NAVER Financial / Dunamu",
        primary_archetype=E2RArchetype.DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="platform_mna_stage2_exchange_trust_4c_watch",
        stage1_date=date(2025, 11, 27),
        stage2_date=date(2025, 11, 27),
        stage3_date=None,
        stage4b_date=date(2025, 11, 27),
        stage4c_date=date(2025, 11, 27),
        stage3_decision="deal_value_not_green_until_approval_closing_regulated_revenue_and_exchange_trust_recovery_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("deal_value_15_13tn_krw", "exchange_ratio_2_54", "upbit_market_share_70pct", "naver_initial_mfe_7pct"),
        red_flag_fields=("abnormal_withdrawal_54bn_krw", "exchange_trust_unresolved", "regulatory_closing_unverified", "event_swing_minus_11_2pp"),
        price_data_source="Reuters deal / event return / trust-risk anchors",
        reported_price_anchor="NAVER initially >+7%, later -4.2%; abnormal withdrawal 54B won",
        reported_return_anchor="Deal premium reversed around exchange trust incident; event swing -11.2pp",
        mfe_1d=7.0,
        mae_1d=-4.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"deal_value_krw_trn": 15.13, "deal_value_usd_bn": 10.27, "exchange_ratio_naver_financial_per_dunamu": 2.54, "upbit_market_share_pct": 70.0, "event_initial_mfe_pct": 7.0, "event_later_mae_pct": -4.2, "event_swing_pp": -11.2, "abnormal_withdrawal_krw_bn": 54.0},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_trust_watch",
        rerating_result="event_premium",
        round_rerating_label="digital_asset_platform_merger_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="platform_stage2_with_exchange_trust_4C_watch",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Digital-asset platform M&A is Stage 2, but abnormal withdrawal creates exchange-trust 4C-watch.",
    ),
    Round264CaseCandidate(
        case_id="r8_loop12_coupang_platform_data_breach_reference",
        symbol="CPNG_non_KRX",
        company_name="Coupang",
        primary_archetype=E2RArchetype.ECOMMERCE_PLATFORM_DATA_BREACH_4C,
        secondary_archetypes=(E2RArchetype.PLATFORM_PRIVACY_SECURITY_OVERLAY, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        round_case_type="non_krx_platform_trust_4c_reference",
        stage1_date=date(2025, 6, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 1),
        stage3_decision="non_krx_reference_not_green_until_trust_restoration_retention_regulatory_cost_and_compensation_confirm",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("33_7m_accounts_affected", "former_employee_context", "retained_data_about_3000_customers", "relief_event_plus_9_2pct"),
        red_flag_fields=("major_data_breach", "delayed_detection", "ceo_resignation_context", "police_raid_context", "non_krx_reference_gap"),
        price_data_source="IBD / Barron's breach and event-return anchors",
        reported_price_anchor="Stock down >4% at $26.86, later +9.2% relief event; non-KRX reference",
        reported_return_anchor="33.7M accounts affected; retained data later reported around 3,000 customers",
        mfe_1d=9.2,
        mae_1d=-4.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=26.86,
        extra_price_metrics={"breach_affected_accounts_mn": 33.7, "event_mae_pct": -4.0, "event_price_anchor_usd": 26.86, "retained_data_customers_after_investigation": 3000.0, "retained_data_share_pct": 0.0091, "relief_event_mfe_pct": 9.2},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch_then_relief",
        rerating_result="thesis_break",
        round_rerating_label="platform_data_trust_4C_reference",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="non_KRX_but_R8_platform_trust_reference",
        price_validation_status="reported_event_anchor_not_full_ohlc_non_KRX",
        notes="Non-KRX but important platform trust reference; growth cannot override data-governance breach.",
    ),
    Round264CaseCandidate(
        case_id="r8_loop12_krafton_unknown_worlds_subnautica_governance_watch",
        symbol="259960",
        company_name="Krafton / Unknown Worlds / Subnautica 2",
        primary_archetype=E2RArchetype.GAME_STUDIO_M_AND_A_GOVERNANCE_4C,
        secondary_archetypes=(E2RArchetype.GAME_IP_M_AND_A_CONTENT_EXPANSION, E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK),
        case_type="4c_thesis_break",
        round_case_type="game_mna_governance_4c_watch",
        stage1_date=date(2021, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 3, 16),
        stage3_decision="acquired_ip_not_green_until_release_sales_retention_review_score_and_legal_governance_overhang_clear",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("unknown_worlds_acquisition_500m_usd", "earnout_dispute_250m_usd", "subnautica_2_development_context", "delaware_reinstatement_order"),
        red_flag_fields=("mna_governance_dispute", "earnout_litigation", "release_execution_risk", "studio_autonomy_break"),
        price_data_source="Reuters legal ruling / acquisition / earnout anchors",
        reported_price_anchor="Krafton KRX OHLC unavailable after deep search around ruling",
        reported_return_anchor="$500M acquisition and $250M earnout dispute anchor governance 4C-watch",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"unknown_worlds_acquisition_upfront_usd_mn": 500.0, "earnout_at_issue_usd_mn": 250.0, "court_event": "Krafton ordered to reinstate Unknown Worlds CEO Ted Gill", "subnautica_2_status": "in development / early access preparation context"},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="game_studio_M&A_governance_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="IP_acquisition_not_release_revenue_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Acquired IP is not Green until release, sales, retention and legal/governance overhang clear.",
    ),
    Round264CaseCandidate(
        case_id="r8_loop12_skt_cybersecurity_operational_trust_hard_4c",
        symbol="017670",
        company_name="SK Telecom",
        primary_archetype=E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C,
        secondary_archetypes=(E2RArchetype.SECURITY_OPERATIONAL_TRUST_HARD_4C, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        round_case_type="direct_krx_cybersecurity_operational_trust_hard_4c",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 28),
        stage3_decision="cyberattack_data_leak_revenue_cut_security_investment_and_compensation_create_hard_4c",
        stage4b_status="none",
        hard_4c_confirmed=True,
        evidence_fields=("23m_users_usim_replacement", "26_96m_data_pieces_leaked", "security_investment_700bn_krw", "revenue_forecast_cut_800bn_krw", "possible_compensation_2_3tn_krw"),
        red_flag_fields=("cyberattack", "customer_data_leak", "revenue_guidance_cut", "large_security_investment", "compensation_liability"),
        price_data_source="Reuters breach / July investigation / compensation anchors",
        reported_price_anchor="Initial intraday -8.5%, close -6.7% vs KOSPI +0.1%; July close -5.6%",
        reported_return_anchor="Revenue guide cut 800B won, customer benefit package 500B won, possible all-victim compensation nearly 2.3T won",
        mfe_1d=None,
        mae_1d=-8.5,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"initial_intraday_mae_pct": -8.5, "initial_close_mae_pct": -6.7, "kospi_same_context_pct": 0.1, "relative_underperformance_initial_close_pp": -6.8, "affected_users_initial_mn": 23.0, "protection_service_signups_mn": 5.54, "protection_signup_share_pct": 24.1, "july_event_mae_pct": -5.6, "leaked_data_pieces_mn": 26.96, "data_protection_investment_krw_bn": 700.0, "annualized_security_investment_krw_bn": 140.0, "revenue_forecast_cut_2025_krw_bn": 800.0, "customer_benefit_package_krw_bn": 500.0, "individual_compensation_order_krw": 100000.0, "applicant_count": 58.0, "possible_all_victim_compensation_cost_krw_trn": 2.3},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="cybersecurity_operational_trust_break",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Direct KRX hard 4C: breach caused price drop, revenue-cut, security investment, compensation and possible broader liabilities.",
    ),
)


def round264_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND264_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="US" if candidate.symbol.endswith("non_KRX") else "KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND264_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round264 R8 Loop-12 platform/content/SW/security price validation case. Calibration-only; not production scoring input.",
            stage1_evidence=tuple(field for field in candidate.evidence_fields if "ipo" in field or "deal" in field or "stake" in field or "users" in field),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if "revenue" in field or "op_" in field or "retention" in field or "fcf" in field),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "ipo" in field or "event" in field or "single" in field or "mna" in field or "china" in field),
            stage4c_evidence=tuple(field for field in candidate.red_flag_fields if "breach" in field or "leak" in field or "withdrawal" in field or "governance" in field or "cyber" in field or "compensation" in field),
            must_have_fields=ROUND264_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=("; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4c_thesis_break"} else None),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND264_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_stage_dates_retention_arpu_take_rate_opm_fcf_or_security_costs",
                "do_not_treat_ipo_hit_title_single_ip_mna_or_china_optional_headline_as_green",
                "do_not_ignore_platform_exchange_cybersecurity_or_data_trust_hard_gates",
                f"round_case_type={candidate.round_case_type}",
                f"round_alignment_label={candidate.round_alignment_label}",
                f"round_rerating_label={candidate.round_rerating_label}",
                f"round_stage_failure_label={candidate.round_stage_failure_label}",
                *ROUND264_GREEN_REQUIRED_FIELDS,
                *ROUND264_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=candidate.stage2_price_anchor is not None or candidate.mfe_1d is not None or candidate.mae_1d is not None,
                stage_dates_confidence=0.86 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round264_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND264_CASE_CANDIDATES:
        rows.append(
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
                "price_data_source": candidate.price_data_source,
                "reported_price_anchor": candidate.reported_price_anchor,
                "reported_return_anchor": candidate.reported_return_anchor,
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mae_1d": _float_text(candidate.mae_1d),
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
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
        )
    return tuple(rows)


def round264_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND264_SCORE_ADJUSTMENTS)


def round264_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND264_SHADOW_WEIGHT_ROWS)


def round264_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round264_price_validation": "true"} for field in ROUND264_PRICE_VALIDATION_FIELDS)


def round264_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round264_label": label, "canonical_archetype": canonical} for label, canonical in ROUND264_REQUIRED_TARGET_ALIASES.items())


def round264_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple({"deep_sub_archetype": item, "large_sector": ROUND264_LARGE_SECTOR} for item in ROUND264_DEEP_SUB_ARCHETYPES)


def round264_summary() -> dict[str, int | bool | str]:
    cases = ROUND264_CASE_CANDIDATES
    return {
        "source_round": ROUND264_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND264_ANALYST_ROUND_ID,
        "large_sector": ROUND264_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "thesis_break_or_watch_count": sum(1 for case in cases if case.rerating_result == "thesis_break" or "4c" in case.round_case_type.lower()),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND264_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND264_DEEP_SUB_ARCHETYPES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round264_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND264_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND264_ANALYST_ROUND_ID,
        "large_sector": ROUND264_LARGE_SECTOR,
        "summary": round264_summary(),
        "target_aliases": dict(ROUND264_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetypes": list(ROUND264_DEEP_SUB_ARCHETYPES),
        "green_required_fields": list(ROUND264_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND264_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND264_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND264_HARD_4C_GATES),
        "case_ids": [case.case_id for case in ROUND264_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_use_round264_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_ipo_hit_title_single_ip_mna_china_optionality_or_platform_deal_headline_as_green",
            "do_not_ignore_platform_exchange_data_cybersecurity_or_governance_hard_gates",
            "do_not_invent_ohlc_retention_arpu_take_rate_opm_fcf_security_or_compensation_costs",
        ],
    }


def render_round264_summary_markdown() -> str:
    summary = round264_summary()
    lines = [
        "# Round 264 R8 Loop 12 Platform Content SW Security Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- analyst_round_id: {summary['analyst_round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round type | stage2 | stage3 | 4B | 4C | hard 4C | round alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND264_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.case_type,
                    case.round_case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    str(case.hard_4c_confirmed).lower(),
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
            "- Shift Up is game-IP Stage 2/watch, not Green, until retention, repeat-title pipeline and FCF confirm.",
            "- Pinkfong is kids-content IPO event premium; Baby Shark views alone are not recurring cash flow.",
            "- SM/Tencent is China optionality Stage 2; ticket revenue and regulatory durability are required.",
            "- NAVER/Dunamu is platform M&A Stage 2 plus exchange-trust 4C-watch.",
            "- Coupang is a non-KRX platform trust reference, not a KR production candidate.",
            "- Krafton/Unknown Worlds is game M&A governance 4C-watch until release revenue and legal risk clear.",
            "- SK Telecom is direct KRX hard 4C because cybersecurity break hit price, revenue outlook, security spend and compensation.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round264_green_gate_review_markdown() -> str:
    lines = [
        "# Round 264 R8 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND264_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND264_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND264_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `IPO +62%` is not Green if repeat-hit and licensing margin are unverified.",
            "- `M&A deal value` is not Green if exchange trust or regulatory closing is unresolved.",
            "- `subscriber base` is not enough when cybersecurity caused revenue-guide cuts and compensation risk.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round264_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 264 R8 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND264_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND264_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | 4C date | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND264_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.stage4b_status} | {_date_text(case.stage4c_date)} | "
            f"{str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round264_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 264 R8 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: true",
        "- Do not invent OHLC, peak, MFE, MAE, stage prices, retention, ARPU, take-rate, OPM, FCF, security costs, or compensation liabilities.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND264_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND264_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def render_round264_deep_sub_archetypes_markdown() -> str:
    lines = [
        "# Round 264 R8 Deep Sub-Archetypes",
        "",
        "These labels describe research coverage. They are not production scoring inputs.",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND264_DEEP_SUB_ARCHETYPES)
    return "\n".join(lines) + "\n"


def write_round264_r8_loop12_reports(
    output_directory: str | Path = ROUND264_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND264_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND264_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round264_case_records(), cases_path),
        "audit": _write_json(round264_audit_payload(), audit_path),
        "summary": output / "round264_r8_loop12_price_validation_summary.md",
        "case_matrix": output / "round264_r8_loop12_case_matrix.csv",
        "target_aliases": output / "round264_r8_loop12_target_aliases.csv",
        "deep_sub_archetypes": output / "round264_r8_loop12_deep_sub_archetypes.csv",
        "score_adjustments": output / "round264_r8_loop12_score_adjustments.csv",
        "shadow_weights": output / "round264_r8_loop12_shadow_weights.csv",
        "price_validation_fields": output / "round264_r8_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round264_r8_loop12_green_gate_review.md",
        "price_validation_plan": output / "round264_r8_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round264_r8_loop12_stage4b_4c_review.md",
        "deep_sub_archetype_review": output / "round264_r8_loop12_deep_sub_archetypes.md",
    }
    paths["summary"].write_text(render_round264_summary_markdown(), encoding="utf-8")
    _write_csv(round264_case_rows(), paths["case_matrix"])
    _write_csv(round264_target_alias_rows(), paths["target_aliases"])
    _write_csv(round264_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round264_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round264_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round264_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round264_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round264_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round264_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["deep_sub_archetype_review"].write_text(render_round264_deep_sub_archetypes_markdown(), encoding="utf-8")
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
