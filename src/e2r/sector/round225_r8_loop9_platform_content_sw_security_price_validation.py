"""Round-225 R8 Loop-9 platform/content/SW/security price validation pack.

Round 225 is calibration/evaluation material only. It turns
``docs/round/round_225.md`` into case-library records and guardrail reports.

Easy example: an AI partnership headline can make a stock visible at Stage 1 or
Stage 2. It is not Stage 3-Green until paid usage, recurring revenue, margin,
FCF, and operational-trust evidence are visible as of the case date.
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


ROUND225_SOURCE_ROUND_PATH = "docs/round/round_225.md"
ROUND225_LARGE_SECTOR = Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY
ROUND225_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round225_r8_loop9_platform_content_sw_security_price_validation"
ROUND225_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r8_loop9_round225.jsonl"
ROUND225_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round225_r8_loop9_platform_content_sw_security_price_validation_audit.json"

ROUND225_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "B2B_SAAS_ERP_WORKFLOW": E2RArchetype.B2B_SAAS_ERP_WORKFLOW.value,
    "AI_CLOUD_CAPITAL_ALLOCATION": E2RArchetype.AI_CLOUD_CAPITAL_ALLOCATION.value,
    "CLOUD_AI_SOFTWARE_INFRA": E2RArchetype.CLOUD_AI_SOFTWARE_INFRA.value,
    "WEBTOON_PLATFORM_IP_MONETIZATION": E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION.value,
    "AI_SOFTWARE_PARTNERSHIP_EVENT": E2RArchetype.AI_SOFTWARE_APPLICATION.value,
    "GAME_IP_REPEAT_MONETIZATION": E2RArchetype.GAME_CONTENT_IP_REPEAT_MONETIZATION.value,
    "GAME_IP_IPO_PREMIUM": E2RArchetype.SINGLE_IP_RELEASE_EVENT_PREMIUM.value,
    "SECURITY_OPERATIONAL_TRUST_OVERLAY": E2RArchetype.SECURITY_OPERATIONAL_TRUST_OVERLAY.value,
    "KPOP_PLATFORM_CONTENT_IP": E2RArchetype.KPOP_PLATFORM_CONTENT_IP.value,
    "PLATFORM_GOVERNANCE_LEGAL_RISK": E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK.value,
    "PLATFORM_PRIVACY_SECURITY_OVERLAY": E2RArchetype.PLATFORM_PRIVACY_SECURITY_OVERLAY.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
    "EVIDENCE_GOOD_BUT_PRICE_FAILED": E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED.value,
}

ROUND225_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "recurring_revenue_or_bookings",
    "paid_usage_or_arpu_or_arr_proxy",
    "opm_or_gross_margin_improvement",
    "fcf_conversion",
    "customer_retention_or_churn",
    "ip_monetization_beyond_launch",
    "ai_feature_to_paid_revenue_or_cost_savings",
    "privacy_security_governance_risk_passed",
    "price_path_after_evidence",
)

ROUND225_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ai_partnership_headline_only",
    "ai_infra_investment_plan_only",
    "mau_without_arpu",
    "ipo_or_debut_premium_only",
    "mna_without_integration",
    "game_first_week_sales_only",
    "single_ip_dependence_without_retention",
    "founder_legal_risk",
    "security_privacy_incident",
    "data_breach_revenue_cut",
)

ROUND225_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "ai_partnership_spike_before_paid_usage",
    "cloud_ai_or_kkr_mna_price_spike_before_revenue",
    "ipo_debut_premium_before_repeat_monetization",
    "webtoon_ip_valuation_before_subscription_or_ads",
    "game_launch_sales_before_retention",
    "kpop_comeback_expectation_over_governance_risk",
    "single_ip_developer_ipo_premium",
)

ROUND225_HARD_4C_GATES: tuple[str, ...] = (
    "privacy_breach_or_security_outage",
    "large_customer_data_leak",
    "data_breach_revenue_cut",
    "founder_legal_break",
    "regulatory_sanction",
    "ai_monetization_failure",
    "arr_churn_or_paid_user_decline",
    "game_launch_failure_or_retention_collapse",
    "ip_litigation_or_artist_contract_break",
    "mna_integration_failure",
    "single_ip_collapse",
    "ad_or_commerce_take_rate_damage",
    "fcf_deterioration",
)

ROUND225_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "mfe_event",
    "mae_event",
    "relative_underperformance_pp",
    "transaction_or_capital_anchor",
    "revenue_or_margin_anchor",
    "trust_or_legal_risk_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round225ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round225ShadowWeightRow:
    archetype: E2RArchetype
    recurring_revenue: int
    paid_usage: int
    bookings_repeatability: int
    opm_fcf: int
    ip_repeatability: int
    ai_revenue_conversion: int
    operational_trust: int
    event_penalty: int
    governance_security_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "recurring_revenue": _signed(self.recurring_revenue),
            "paid_usage": _signed(self.paid_usage),
            "bookings_repeatability": _signed(self.bookings_repeatability),
            "opm_fcf": _signed(self.opm_fcf),
            "ip_repeatability": _signed(self.ip_repeatability),
            "ai_revenue_conversion": _signed(self.ai_revenue_conversion),
            "operational_trust": _signed(self.operational_trust),
            "event_penalty": _signed(self.event_penalty),
            "governance_security_redteam": _signed(self.governance_security_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round225CaseCandidate:
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
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str | bool]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND225_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND225_SCORE_ADJUSTMENTS: tuple[Round225ScoreAdjustment, ...] = (
    Round225ScoreAdjustment("recurring_revenue", 5, "raise", "SaaS/SW는 일회성 구축보다 반복 매출이 Stage 3 visibility를 만든다."),
    Round225ScoreAdjustment("arr_proxy", 5, "raise", "ARR proxy나 구독·유지보수 반복 매출이 있어야 AI/SW 매출 지속성을 본다."),
    Round225ScoreAdjustment("paid_usage_conversion", 5, "raise", "무료 사용량이나 MAU보다 유료 전환이 중요하다."),
    Round225ScoreAdjustment("bookings_repeatability", 4, "raise", "엔터프라이즈 수주가 반복되면 Stage 2에서 Stage 3 후보로 올라간다."),
    Round225ScoreAdjustment("enterprise_contract_quality", 4, "raise", "B2B 계약은 고객·기간·갱신성이 확인돼야 점수를 준다."),
    Round225ScoreAdjustment("opm_improvement", 5, "raise", "플랫폼/SW는 매출 증가가 OPM 개선으로 이어져야 체급 변화다."),
    Round225ScoreAdjustment("fcf_conversion", 5, "raise", "콘텐츠·게임·클라우드도 FCF가 따라오지 않으면 Green을 제한한다."),
    Round225ScoreAdjustment("customer_retention_or_churn", 4, "raise", "재계약률/이탈률은 반복 매출의 품질 증거다."),
    Round225ScoreAdjustment("ip_monetization_beyond_launch", 4, "raise", "게임·웹툰·K-pop은 출시/컴백 이후 반복 monetization이 필요하다."),
    Round225ScoreAdjustment("operational_trust", 5, "raise", "보안·개인정보·지배구조 신뢰가 통과돼야 플랫폼 Green을 허용한다."),
    Round225ScoreAdjustment("ai_feature_only", -5, "lower", "AI 기능 탑재만으로는 유료 매출 증거가 아니다."),
    Round225ScoreAdjustment("ai_partnership_headline_only", -5, "lower", "AI 파트너십 헤드라인은 paid usage 전까지 event premium이다."),
    Round225ScoreAdjustment("mau_without_arpu", -4, "lower", "MAU만 있고 ARPU/paid usage가 없으면 Stage 3를 막는다."),
    Round225ScoreAdjustment("ipo_debut_premium", -5, "lower", "IPO/debut premium은 반복 monetization 전까지 4B-watch다."),
    Round225ScoreAdjustment("mna_without_integration", -4, "lower", "M&A 발표만 있고 통합·가동률·매출 전환이 없으면 제한한다."),
    Round225ScoreAdjustment("ai_capex_without_revenue", -5, "lower", "AI capex는 매출/비용절감으로 연결돼야 한다."),
    Round225ScoreAdjustment("game_launch_first_week_only", -4, "lower", "첫 주 판매량만으로는 retention과 DLC/후속 매출을 알 수 없다."),
    Round225ScoreAdjustment("single_ip_dependence", -4, "lower", "단일 IP 의존은 Stage 3 확신을 낮춘다."),
    Round225ScoreAdjustment("founder_legal_risk", -5, "lower", "창업자·핵심 경영진 법적 리스크는 RedTeam 입력이다."),
    Round225ScoreAdjustment("privacy_security_trust_break", -5, "lower", "데이터 유출·보안 사고는 플랫폼 논리 훼손 감시다."),
    Round225ScoreAdjustment("data_breach_revenue_cut", -5, "lower", "보상·매출 감소가 동반된 유출은 hard 4C 후보가 된다."),
)


ROUND225_SHADOW_WEIGHT_ROWS: tuple[Round225ShadowWeightRow, ...] = (
    Round225ShadowWeightRow(E2RArchetype.B2B_SAAS_ERP_WORKFLOW, 5, 5, 5, 5, 0, 3, 4, -2, 4, 4, 4, "Douzone needs ARR/churn, operating margin, FCF, and regulatory close after EQT."),
    Round225ShadowWeightRow(E2RArchetype.CLOUD_AI_SOFTWARE_INFRA, 4, 4, 4, 5, 0, 5, 4, -4, 4, 5, 4, "Samsung SDS/LG CNS need cloud-AI revenue conversion, integration, OPM, and FCF."),
    Round225ShadowWeightRow(E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION, 4, 5, 4, 4, 5, 2, 4, -5, 4, 5, 4, "Webtoon IPO/IP events are watch until ads/subscriptions/IP monetization and losses improve."),
    Round225ShadowWeightRow(E2RArchetype.AI_SOFTWARE_APPLICATION, 3, 5, 3, 4, 0, 5, 4, -5, 5, 5, 5, "AI partnerships are not Green without paid usage, cost savings, and governance pass."),
    Round225ShadowWeightRow(E2RArchetype.GAME_CONTENT_IP_REPEAT_MONETIZATION, 4, 4, 4, 5, 5, 0, 4, -4, 4, 5, 4, "Shift Up needs retention, DLC/PC tail, platform expansion, and single-IP risk control."),
    Round225ShadowWeightRow(E2RArchetype.SECURITY_OPERATIONAL_TRUST_OVERLAY, 0, 0, 0, 0, 0, 0, 5, -5, 5, 5, 5, "SKT-like data leaks should feed 4C watch, not positive rerating."),
    Round225ShadowWeightRow(E2RArchetype.KPOP_PLATFORM_CONTENT_IP, 4, 4, 3, 4, 5, 0, 4, -3, 5, 5, 5, "K-pop needs IP monetization and governance/legal risk pass before Green."),
    Round225ShadowWeightRow(E2RArchetype.EVENT_PREMIUM, 0, 0, 0, 0, 0, 0, 0, -5, 5, 5, 4, "Event premium is a watch label until repeat revenue and FCF evidence arrive."),
)


ROUND225_CASE_CANDIDATES: tuple[Round225CaseCandidate, ...] = (
    Round225CaseCandidate(
        case_id="r8_loop9_douzone_eqt_b2b_saas_stage2_watch",
        symbol="012510",
        company_name="더존비즈온",
        primary_archetype=E2RArchetype.B2B_SAAS_ERP_WORKFLOW,
        secondary_archetypes=(E2RArchetype.PLATFORM_SOFTWARE_INTERNET, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2025, 11, 7),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="eqt_investment_is_stage2_until_arr_churn_opm_fcf_and_regulatory_close_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("eqt_investment_930m_usd", "stake_37_6pct", "implied_equity_value_2_473bn_usd", "bpea_fund_ix_exposure_5_10pct"),
        red_flag_fields=("arr_unverified", "churn_unverified", "opm_fcf_unverified", "regulatory_close_unverified", "event_premium_watch"),
        price_data_source="reported private-equity transaction anchors",
        reported_price_anchor="Public OHLC not completed for the event window",
        reported_return_anchor="EQT investment $930M for 37.6% stake implies about $2.473B equity value",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"eqt_investment_usd_mn": 930.0, "stake_pct": 37.6, "implied_equity_value_usd_bn": 2.473, "bpea_fund_ix_exposure_low_pct": 5.0, "bpea_fund_ix_exposure_high_pct": 10.0},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_transaction_anchor_not_full_ohlc",
        notes="Private-equity validation is useful, but ARR, churn, OPM, FCF, and closing conditions decide promotion.",
    ),
    Round225CaseCandidate(
        case_id="r8_loop9_samsung_sds_ai_cloud_kkr_event_premium",
        symbol="018260",
        company_name="삼성SDS",
        primary_archetype=E2RArchetype.CLOUD_AI_SOFTWARE_INFRA,
        secondary_archetypes=(E2RArchetype.AI_CLOUD_CAPITAL_ALLOCATION, E2RArchetype.EVENT_PREMIUM, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="event_premium",
        stage1_date=None,
        stage2_date=date(2026, 4, 15),
        stage3_date=None,
        stage4b_date=date(2026, 4, 15),
        stage4c_date=None,
        stage3_decision="ai_cloud_kkr_capital_event_is_4b_watch_until_ai_revenue_cost_savings_opm_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("event_mfe_20_8pct", "morning_gain_19_4pct", "kospi_gain_3_0pct", "relative_outperformance_17_8pp", "convertible_bond_820m_usd", "existing_cash_6_4tn_krw"),
        red_flag_fields=("price_moved_before_ai_revenue", "ai_capex_without_revenue", "mna_integration_unverified", "fcf_conversion_unverified"),
        price_data_source="reported event return and capital anchors",
        reported_price_anchor="event MFE +20.8%; morning +19.4%; KOSPI +3.0%",
        reported_return_anchor="relative outperformance +17.8pp; $820M CB at FX 1,472 implies about 1.207T KRW",
        mfe_1d=20.8,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_mfe_pct": 20.8, "morning_gain_pct": 19.4, "kospi_return_pct": 3.0, "relative_outperformance_pp": 17.8, "convertible_bond_usd_mn": 820.0, "fx_krw_per_usd": 1472.0, "convertible_bond_krw_tn": 1.207, "existing_cash_krw_tn": 6.4, "combined_liquidity_krw_tn": 7.607},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Large price reaction is 4B/event premium until AI/cloud revenue conversion, M&A execution, OPM, and FCF are visible.",
    ),
    Round225CaseCandidate(
        case_id="r8_loop9_lg_cns_ipo_cloud_ai_price_failed",
        symbol="LG_CNS",
        company_name="LG CNS",
        primary_archetype=E2RArchetype.CLOUD_AI_SOFTWARE_INFRA,
        secondary_archetypes=(E2RArchetype.AI_CLOUD_CAPITAL_ALLOCATION, E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED, E2RArchetype.EVENT_PREMIUM),
        case_type="failed_rerating",
        stage1_date=None,
        stage2_date=date(2025, 2, 5),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="cloud_ai_mix_and_mna_budget_are_not_green_when_ipo_price_path_fails_and_fcf_conversion_is_unverified",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ipo_price_61900_krw", "debut_close_59700_krw", "ipo_proceeds_1_2tn_krw", "mna_budget_390bn_krw", "cloud_ai_sales_mix_54pct", "opm_7_8pct"),
        red_flag_fields=("ipo_price_failed", "mna_integration_unverified", "fcf_conversion_unverified", "public_market_demand_unconfirmed"),
        price_data_source="reported IPO and operating anchors",
        reported_price_anchor="IPO 61,900 KRW; debut close 59,700 KRW",
        reported_return_anchor="debut MAE -3.55%; opening return -2.26%; cloud/AI mix 54%; OPM 7.8%",
        mfe_1d=None,
        mae_1d=-3.55,
        stage1_price_anchor=None,
        stage2_price_anchor=61900.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_price_krw": 61900.0, "debut_close_krw": 59700.0, "debut_mae_pct": -3.55, "opening_price_krw": 60500.0, "opening_return_pct": -2.26, "ipo_proceeds_krw_tn": 1.2, "mna_budget_krw_bn": 390.0, "new_issuance_total_krw_bn": 594.0, "mna_share_of_new_issuance_pct": 65.7, "cloud_ai_sales_mix_pct": 54.0, "revenue_1q_3q_2024_krw_tn": 4.0, "operating_profit_krw_bn": 313.0, "opm_pct": 7.8},
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        stage_failure_type="false_yellow",
        price_validation_status="reported_ipo_anchor_not_full_ohlc",
        notes="Cloud/AI operating anchors are useful, but the IPO price path failed and integration/FCF evidence is still required.",
    ),
    Round225CaseCandidate(
        case_id="r8_loop9_naver_webtoon_ipo_disney_ip_watch",
        symbol="035420/WBTN",
        company_name="NAVER/Webtoon",
        primary_archetype=E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION,
        secondary_archetypes=(E2RArchetype.PLATFORM_SOFTWARE_INTERNET, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        stage1_date=date(2024, 6, 1),
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=date(2025, 8, 13),
        stage4c_date=None,
        stage3_decision="ipo_and_disney_ip_events_are_stage2_4b_watch_until_ads_subscription_ip_revenue_and_loss_improvement_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ipo_price_21_usd", "first_day_close_23_usd", "next_day_high_25_66_usd", "prior_revenue_1_28bn_usd", "net_loss_145m_usd", "disney_event_mfe_62pct"),
        red_flag_fields=("net_loss_margin_11_3pct", "ipo_premium_before_profit", "ip_event_before_monetization", "post_ipo_drawdown_watch"),
        price_data_source="reported IPO and Disney IP event anchors",
        reported_price_anchor="IPO $21; first-day close $23; next-day high $25.66; Disney event price $15.16",
        reported_return_anchor="first-day +9.5%; next-day MFE +22.2%; Disney event MFE +62%; pre-Disney post-IPO drawdown -55%",
        mfe_1d=22.2,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=21.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=15.16,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_price_usd": 21.0, "debut_high_usd": 24.0, "debut_mfe_pct": 14.3, "first_day_close_usd": 23.0, "first_day_return_pct": 9.5, "next_day_high_usd": 25.66, "next_day_mfe_pct": 22.2, "prior_revenue_usd_bn": 1.28, "net_loss_usd_mn": 145.0, "net_loss_margin_pct": 11.3, "disney_event_price_usd": 15.16, "disney_event_mfe_pct": 62.0, "pre_disney_post_ipo_drawdown_pct": -55.0},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_ipo_and_event_anchors_not_full_ohlc",
        notes="Webtoon/IP can be a Stage 2 watch, but losses, ads/subscription/IP monetization, and post-IPO price path still gate Green.",
    ),
    Round225CaseCandidate(
        case_id="r8_loop9_kakao_openai_partnership_price_only_rally",
        symbol="035720",
        company_name="카카오",
        primary_archetype=E2RArchetype.AI_SOFTWARE_APPLICATION,
        secondary_archetypes=(E2RArchetype.PLATFORM_SOFTWARE_INTERNET, E2RArchetype.PRICE_ONLY_RALLY, E2RArchetype.EVENT_PREMIUM),
        case_type="overheat",
        stage1_date=date(2025, 2, 4),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 2, 4),
        stage4c_date=None,
        stage3_decision="openai_partnership_is_price_only_event_until_paid_usage_arpu_cost_savings_opm_and_governance_pass",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("openai_partnership_headline", "two_session_gain_6_8pct", "kakaotalk_market_share_97pct"),
        red_flag_fields=("partnership_headline_only", "paid_usage_unverified", "arpu_unverified", "governance_risk_watch", "price_only_rally"),
        price_data_source="reported event return anchors",
        reported_price_anchor="+9% before event, then -2% following; two-session +6.8%",
        reported_return_anchor="intra-event swing about -11pp after the headline rally",
        mfe_1d=9.0,
        mae_1d=-2.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"pre_event_gain_pct": 9.0, "following_return_pct": -2.0, "two_session_return_pct": 6.8, "swing_pp": -11.0, "kakaotalk_share_pct": 97.0},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="AI partnership creates a research watch, not Green. Paid usage, ARPU, cost savings, margin, and governance pass are required.",
    ),
    Round225CaseCandidate(
        case_id="r8_loop9_shiftup_single_ip_repeat_monetization_watch",
        symbol="462870",
        company_name="시프트업",
        primary_archetype=E2RArchetype.GAME_CONTENT_IP_REPEAT_MONETIZATION,
        secondary_archetypes=(E2RArchetype.SINGLE_IP_RELEASE_EVENT_PREMIUM, E2RArchetype.GAME_CONTENT_IP),
        case_type="success_candidate",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 7, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stellar_blade_pc_sales_and_high_opm_are_stage2_until_retention_dlc_platform_tail_and_single_ip_risk_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ipo_raise_435bn_krw", "ipo_valuation_3_5tn_krw", "2023_opm_65_7pct", "nikke_revenue_255bn_krw", "stellar_blade_pc_3d_sales_above_1m", "stellar_blade_total_sales_above_3m"),
        red_flag_fields=("single_ip_dependence", "retention_unverified", "dlc_tail_unverified", "platform_expansion_unverified", "ipo_premium_watch"),
        price_data_source="reported IPO and sales anchors",
        reported_price_anchor="IPO valuation 3.5T KRW; full OHLC not completed",
        reported_return_anchor="Stellar Blade PC 3-day sales above 1M; total sales above 3M",
        mfe_1d=None,
        mae_1d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_raise_krw_bn": 435.0, "ipo_valuation_krw_tn": 3.5, "tencent_post_ipo_stake_pct": 35.0, "tencent_pre_ipo_stake_pct": 40.0, "tencent_stake_change_pp": -5.0, "revenue_2023_krw_bn": 169.0, "operating_profit_2023_krw_bn": 111.0, "opm_2023_pct": 65.7, "nikke_revenue_krw_bn": 255.0, "stellar_blade_pc_3d_sales_mn": 1.0, "stellar_blade_total_sales_mn": 3.0},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_ipo_and_sales_anchor_not_full_ohlc",
        notes="High OPM and sales are useful, but retention, tail monetization, platform expansion, and single-IP risk decide promotion.",
    ),
    Round225CaseCandidate(
        case_id="r8_loop9_skt_data_breach_operational_trust_4c_watch",
        symbol="017670",
        company_name="SK텔레콤",
        primary_archetype=E2RArchetype.SECURITY_OPERATIONAL_TRUST_OVERLAY,
        secondary_archetypes=(E2RArchetype.PLATFORM_PRIVACY_SECURITY_OVERLAY, E2RArchetype.PLATFORM_SOFTWARE_INTERNET),
        case_type="4c_thesis_break",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 28),
        stage3_decision="data_breach_and_customer_compensation_are_4c_watch_inputs_not_positive_rerating_evidence",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("event_mae_8_5pct", "close_return_minus_6_7pct", "relative_underperformance_minus_6_8pp", "affected_users_23m", "stores_2600_plus", "protection_signups_5_54m", "security_investment_700bn_krw", "revenue_forecast_cut_800bn_krw", "customer_package_500bn_krw"),
        red_flag_fields=("privacy_breach_or_security_outage", "data_breach_revenue_cut", "customer_compensation", "operational_trust_break", "regulatory_watch"),
        price_data_source="reported breach, protection, and compensation anchors",
        reported_price_anchor="event intraday MAE -8.5%; close -6.7%; KOSPI +0.1%",
        reported_return_anchor="relative underperformance -6.8pp; July event -5.6%; leaked data 26.96M",
        mfe_1d=None,
        mae_1d=-8.5,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_intraday_mae_pct": -8.5, "event_close_return_pct": -6.7, "kospi_same_day_return_pct": 0.1, "relative_underperformance_pp": -6.8, "affected_users_mn": 23.0, "stores_count": 2600.0, "protection_signups_mn": 5.54, "signup_share_pct": 24.1, "july_event_return_pct": -5.6, "leaked_data_mn": 26.96, "security_investment_krw_bn": 700.0, "security_investment_annual_krw_bn": 140.0, "revenue_forecast_cut_krw_bn": 800.0, "customer_package_krw_bn": 500.0, "possible_compensation_krw_tn": 2.3},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Security and privacy breach evidence belongs to RedTeam/4C-watch; it must not be treated as positive rerating evidence.",
    ),
    Round225CaseCandidate(
        case_id="r8_loop9_hybe_founder_legal_governance_4c_watch",
        symbol="352820",
        company_name="HYBE",
        primary_archetype=E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK,
        secondary_archetypes=(E2RArchetype.KPOP_PLATFORM_CONTENT_IP, E2RArchetype.SECURITY_OPERATIONAL_TRUST_OVERLAY),
        case_type="failed_rerating",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 4, 21),
        stage3_decision="founder_legal_risk_blocks_content_ip_green_until_governance_risk_is_resolved_and_fcf_evidence_confirms",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("event_mae_2_4pct", "relative_underperformance_minus_5_1pp", "alleged_profit_190bn_krw", "travel_ban_since_aug_2025", "legal_relief_2026_04_24"),
        red_flag_fields=("founder_legal_risk", "governance_trust_break_watch", "kpop_ip_event_premium_watch", "hard_4c_not_confirmed"),
        price_data_source="reported legal-risk event anchors",
        reported_price_anchor="event MAE -2.4%; KOSPI +2.7%",
        reported_return_anchor="relative underperformance -5.1pp; alleged profit 190B KRW; legal relief on 2026-04-24",
        mfe_1d=None,
        mae_1d=-2.4,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_mae_pct": -2.4, "kospi_same_day_return_pct": 2.7, "relative_underperformance_pp": -5.1, "alleged_profit_krw_bn": 190.0, "alleged_profit_usd_mn": 129.1, "travel_ban_since": "2025-08", "legal_relief_date": "2026-04-24", "hard_4c_confirmed": False},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="K-pop/IP evidence cannot overcome founder/legal governance risk until the trust issue is resolved and FCF evidence supports rerating.",
    ),
)


def round225_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND225_CASE_CANDIDATES:
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
                "Round225 R8 Loop-9 platform/content/SW/security price-path "
                "validation case. Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "headline" in field or "ipo" in field or "event" in field or "sales" in field or "investment" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "revenue" in field
                or "opm" in field
                or "sales" in field
                or "bookings" in field
                or "recurring" in field
                or "retention" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "event" in field or "premium" in field or "price" in field or "ipo" in field or "spike" in field or "mfe" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "privacy" in field
                or "security" in field
                or "breach" in field
                or "legal" in field
                or "governance" in field
                or "revenue_cut" in field
                or "trust" in field
            ),
            must_have_fields=ROUND225_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND225_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_ai_partnership_ipo_mna_game_launch_or_kpop_headline_as_green_alone",
                *ROUND225_GREEN_REQUIRED_FIELDS,
                *ROUND225_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
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
                    or candidate.stage4b_price_anchor is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                ),
                stage_dates_confidence=0.8 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round225_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND225_CASE_CANDIDATES:
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
                "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
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


def round225_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND225_SCORE_ADJUSTMENTS)


def round225_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND225_SHADOW_WEIGHT_ROWS)


def round225_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round225_price_validation": "true"} for field in ROUND225_PRICE_VALIDATION_FIELDS)


def round225_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round225_label": label, "canonical_archetype": canonical} for label, canonical in ROUND225_REQUIRED_TARGET_ALIASES.items())


def round225_summary() -> dict[str, int | bool | str]:
    cases = ROUND225_CASE_CANDIDATES
    return {
        "source_round": ROUND225_SOURCE_ROUND_PATH,
        "large_sector": ROUND225_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "target_archetype_count": len(ROUND225_REQUIRED_TARGET_ALIASES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": False,
    }


def round225_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND225_SOURCE_ROUND_PATH,
        "large_sector": ROUND225_LARGE_SECTOR.value,
        "summary": round225_summary(),
        "target_aliases": dict(ROUND225_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND225_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND225_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND225_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND225_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_use_round225_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_ai_partnership_ipo_mna_game_launch_webtoon_or_kpop_headline_as_green",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round225_summary_markdown() -> str:
    summary = round225_summary()
    lines = [
        "# Round 225 R8 Loop 9 Platform Content SW Security Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | stage2 | stage3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND225_CASE_CANDIDATES:
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
                    case.score_price_alignment,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Douzone and Shift Up are Stage 2 watch examples, not automatic Green.",
            "- Samsung SDS, NAVER/Webtoon, Kakao, and LG CNS show why event premium and price confirmation must be separated.",
            "- SKT and HYBE are trust/governance watch examples; these feed RedTeam/4C checks rather than positive scoring.",
            "- R8 Green needs recurring revenue, paid usage, margin, FCF, retention, operational trust, and price behavior after evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round225_green_gate_review_markdown() -> str:
    lines = [
        "# Round 225 R8 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND225_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND225_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `AI partnership + same-day price spike` is Stage 1/2 attention or 4B-watch.",
            "- `AI partnership + paid users + ARR proxy + OPM/FCF improvement + no governance/security issue` is the bundle that can support Stage 3 review.",
            "- `data leak + customer compensation + revenue cut` is RedTeam/4C-watch, not positive platform rerating evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round225_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 225 R8 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND225_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND225_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND225_CASE_CANDIDATES:
        if case.stage4b_status == "watch" or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round225_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 225 R8 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND225_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round225_r8_loop9_reports(
    output_directory: str | Path = ROUND225_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND225_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND225_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)

    paths = {
        "cases": write_case_library(round225_case_records(), cases_path),
        "audit": _write_json(round225_audit_payload(), audit_path),
        "summary": output / "round225_r8_loop9_price_validation_summary.md",
        "case_matrix": output / "round225_r8_loop9_case_matrix.csv",
        "target_aliases": output / "round225_r8_loop9_target_aliases.csv",
        "score_adjustments": output / "round225_r8_loop9_score_adjustments.csv",
        "shadow_weights": output / "round225_r8_loop9_shadow_weights.csv",
        "price_validation_fields": output / "round225_r8_loop9_price_validation_fields.csv",
        "green_gate_review": output / "round225_r8_loop9_green_gate_review.md",
        "price_validation_plan": output / "round225_r8_loop9_price_validation_plan.md",
        "stage4b_4c_review": output / "round225_r8_loop9_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round225_summary_markdown(), encoding="utf-8")
    _write_csv(round225_case_rows(), paths["case_matrix"])
    _write_csv(round225_target_alias_rows(), paths["target_aliases"])
    _write_csv(round225_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round225_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round225_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round225_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round225_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round225_stage4b_4c_review_markdown(), encoding="utf-8")
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
