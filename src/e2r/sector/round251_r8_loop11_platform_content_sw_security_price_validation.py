"""Round-251 R8 Loop-11 platform/content/SW/security price validation pack.

This pack converts ``docs/round/round_251.md`` into calibration-only case
records, shadow weights, and guardrail reports. Production scoring is not
changed.

Easy example: an AI partnership can move a stock price, but it is not
Stage 3-Green until paid usage, ARPU, OPM/FCF, and operational-trust evidence
are visible.
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


ROUND251_SOURCE_ROUND_PATH = "docs/round/round_251.md"
ROUND251_ANALYST_ROUND_ID = "round_179"
ROUND251_LARGE_SECTOR = Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY.value
ROUND251_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round251_r8_loop11_platform_content_sw_security_price_validation"
ROUND251_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r8_loop11_round251.jsonl"
ROUND251_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round251_r8_loop11_platform_content_sw_security_price_validation_audit.json"

ROUND251_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "B2B_SAAS_ERP_WORKFLOW": E2RArchetype.B2B_SAAS_ERP_WORKFLOW.value,
    "AI_CLOUD_CAPITAL_ALLOCATION": E2RArchetype.AI_CLOUD_CAPITAL_ALLOCATION.value,
    "CLOUD_AI_SOFTWARE_INFRA": E2RArchetype.CLOUD_AI_SOFTWARE_INFRA.value,
    "WEBTOON_PLATFORM_IP_MONETIZATION": E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION.value,
    "AI_SOFTWARE_PARTNERSHIP_EVENT": E2RArchetype.AI_SOFTWARE_PARTNERSHIP_EVENT.value,
    "GAME_IP_PLATFORM_EXPANSION": E2RArchetype.GAME_IP_PLATFORM_EXPANSION.value,
    "GAME_IP_M_AND_A_CONTENT_EXPANSION": E2RArchetype.GAME_IP_M_AND_A_CONTENT_EXPANSION.value,
    "SECURITY_OPERATIONAL_TRUST_HARD_4C": E2RArchetype.SECURITY_OPERATIONAL_TRUST_HARD_4C.value,
    "KPOP_PLATFORM_CONTENT_IP_GOVERNANCE": E2RArchetype.KPOP_PLATFORM_CONTENT_IP_GOVERNANCE.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
    "EVIDENCE_GOOD_BUT_PRICE_FAILED": E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED.value,
}

ROUND251_DEEP_SUB_ARCHETYPES: tuple[str, ...] = (
    "Douzone Bizon cloud ERP / tax / compliance SaaS",
    "EQT operating improvement and regulatory approval",
    "Samsung SDS KKR convertible bond AI capital allocation",
    "LG CNS cloud-AI IPO price failure",
    "NAVER Webtoon IPO and Disney IP monetization",
    "Kakao OpenAI partnership paid-usage gate",
    "Krafton PUBG / BGMI India expansion",
    "Krafton ADK animation IP M&A",
    "SK Telecom data breach operational trust hard 4C",
    "HYBE founder legal governance watch",
)

ROUND251_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "recurring_revenue_or_bookings",
    "arpu_paid_usage_or_arr_proxy",
    "opm_or_gross_margin_improvement",
    "fcf_conversion",
    "customer_retention_or_churn_stability",
    "ip_monetization_beyond_single_launch",
    "ai_feature_to_paid_revenue_or_cost_savings",
    "privacy_security_governance_risk_passed",
    "price_path_after_evidence",
)

ROUND251_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ai_partnership_headline_only",
    "ai_infra_capital_plan_only",
    "mau_without_arpu",
    "ipo_or_debut_premium_only",
    "mna_without_integration",
    "download_count_without_bookings",
    "single_ip_dependence_without_retention",
    "founder_legal_risk",
    "security_privacy_incident",
    "data_breach_revenue_cut",
)

ROUND251_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "ai_partnership_spike_before_paid_usage",
    "ai_infra_kkr_mna_price_spike_before_revenue",
    "ipo_debut_premium_before_repeat_monetization",
    "webtoon_ip_valuation_before_paid_usage",
    "game_downloads_before_bookings",
    "kpop_comeback_expectation_over_governance_risk",
    "single_ip_developer_mna_or_ai_first_premium",
    "good_news_price_response_fades_or_fails",
)

ROUND251_HARD_4C_GATES: tuple[str, ...] = (
    "privacy_breach",
    "security_outage",
    "data_leak_with_compensation_or_revenue_cut",
    "data_breach_revenue_cut",
    "founder_or_major_shareholder_legal_break",
    "regulatory_sanction",
    "ai_product_monetization_failure",
    "arr_churn_spike",
    "paid_user_decline",
    "game_launch_failure",
    "ip_litigation",
    "mna_integration_failure",
    "single_ip_collapse",
    "advertising_or_commerce_take_rate_damage",
    "fcf_deterioration_from_ai_capex",
)

ROUND251_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "transaction_or_capital_anchor",
    "revenue_or_margin_anchor",
    "user_or_booking_anchor",
    "security_or_legal_risk_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round251ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round251ShadowWeightRow:
    archetype: E2RArchetype
    recurring_revenue: int
    arr_proxy: int
    paid_usage: int
    bookings: int
    enterprise_contract: int
    opm_fcf: int
    ip_monetization: int
    operational_trust: int
    security_privacy_trust: int
    data_governance: int
    event_penalty: int
    legal_privacy_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "recurring_revenue": _signed(self.recurring_revenue),
            "arr_proxy": _signed(self.arr_proxy),
            "paid_usage": _signed(self.paid_usage),
            "bookings": _signed(self.bookings),
            "enterprise_contract": _signed(self.enterprise_contract),
            "opm_fcf": _signed(self.opm_fcf),
            "ip_monetization": _signed(self.ip_monetization),
            "operational_trust": _signed(self.operational_trust),
            "security_privacy_trust": _signed(self.security_privacy_trust),
            "data_governance": _signed(self.data_governance),
            "event_penalty": _signed(self.event_penalty),
            "legal_privacy_redteam": _signed(self.legal_privacy_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round251CaseCandidate:
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
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND251_SCORE_ADJUSTMENTS: tuple[Round251ScoreAdjustment, ...] = (
    Round251ScoreAdjustment("recurring_revenue", 5, "raise", "SaaS·SW·플랫폼은 일회성 이벤트보다 반복매출이 Stage 3 visibility다."),
    Round251ScoreAdjustment("arr_proxy", 5, "raise", "ARR proxy는 B2B SaaS와 cloud/AI 매출 지속성을 보는 핵심 축이다."),
    Round251ScoreAdjustment("paid_usage_conversion", 5, "raise", "MAU나 partnership보다 paid usage와 ARPU가 중요하다."),
    Round251ScoreAdjustment("bookings_repeatability", 4, "raise", "게임·콘텐츠는 다운로드보다 반복 bookings가 중요하다."),
    Round251ScoreAdjustment("enterprise_contract_quality", 4, "raise", "B2B 계약은 고객 lock-in, 기간, 갱신성이 확인돼야 한다."),
    Round251ScoreAdjustment("opm_improvement", 5, "raise", "플랫폼 매출 성장이 OPM 개선으로 이어져야 체급 변화다."),
    Round251ScoreAdjustment("fcf_conversion", 5, "raise", "AI capex와 콘텐츠 투자가 FCF를 훼손하면 Green을 제한한다."),
    Round251ScoreAdjustment("customer_retention_or_churn", 4, "raise", "retention/churn은 반복매출 품질을 확인하는 지표다."),
    Round251ScoreAdjustment("ip_monetization_beyond_launch", 4, "raise", "웹툰·게임·K-pop은 launch/comeback 이후 반복 monetization이 필요하다."),
    Round251ScoreAdjustment("operational_trust", 5, "raise", "플랫폼은 운영 신뢰가 깨지면 반복매출 질도 깨진다."),
    Round251ScoreAdjustment("security_privacy_trust", 5, "raise", "보안·개인정보 신뢰는 R8의 hard gate다."),
    Round251ScoreAdjustment("data_governance", 5, "raise", "AI·플랫폼은 데이터 governance가 없으면 RedTeam 리스크가 커진다."),
    Round251ScoreAdjustment("ai_feature_only", -5, "lower", "AI 기능명만으로 paid revenue를 인정하지 않는다."),
    Round251ScoreAdjustment("partnership_headline_only", -5, "lower", "AI partnership headline은 monetization 전 event premium이다."),
    Round251ScoreAdjustment("mau_without_arpu", -4, "lower", "MAU만 있고 ARPU/paid usage가 없으면 Green 금지다."),
    Round251ScoreAdjustment("ipo_debut_premium", -5, "lower", "IPO/debut premium은 반복 monetization 전 4B-watch다."),
    Round251ScoreAdjustment("mna_without_integration", -4, "lower", "M&A 발표만 있고 통합·매출 전환이 없으면 제한한다."),
    Round251ScoreAdjustment("ai_capex_without_revenue", -5, "lower", "AI capex는 유료 매출이나 비용절감으로 닫혀야 한다."),
    Round251ScoreAdjustment("game_downloads_without_bookings", -4, "lower", "다운로드 수만으로 bookings와 retention을 대체하지 않는다."),
    Round251ScoreAdjustment("single_ip_dependence", -4, "lower", "단일 IP 의존은 4B/4C 감시를 높인다."),
    Round251ScoreAdjustment("founder_legal_risk", -5, "lower", "창업자 법적 리스크는 IP monetization보다 먼저 봐야 한다."),
    Round251ScoreAdjustment("privacy_security_trust_break", -5, "lower", "보안·개인정보 사고는 플랫폼 논리 훼손이다."),
    Round251ScoreAdjustment("data_breach_revenue_cut", -5, "lower", "매출전망 하향·보상비·벌금이 동반된 유출은 hard 4C다."),
)

ROUND251_SHADOW_WEIGHT_ROWS: tuple[Round251ShadowWeightRow, ...] = (
    Round251ShadowWeightRow(E2RArchetype.B2B_SAAS_ERP_WORKFLOW, 5, 5, 3, 3, 5, 5, 0, 3, 2, 3, -2, 1, 3, 3, "Douzone/EQT is Stage 2 until ARR/churn/OPM/FCF confirm."),
    Round251ShadowWeightRow(E2RArchetype.AI_CLOUD_CAPITAL_ALLOCATION, 3, 3, 3, 2, 4, 5, 0, 3, 2, 3, -5, 2, 5, 3, "Samsung SDS KKR event is 4B-watch before AI revenue conversion."),
    Round251ShadowWeightRow(E2RArchetype.CLOUD_AI_SOFTWARE_INFRA, 4, 4, 3, 2, 4, 5, 0, 3, 2, 3, -4, 2, 4, 3, "LG CNS IPO weak price action blocks Green despite cloud/AI mix."),
    Round251ShadowWeightRow(E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION, 3, 3, 5, 4, 2, 5, 5, 3, 2, 2, -3, 2, 5, 4, "Webtoon needs paid usage, ARPU, IP monetization and FCF beyond MAU/IPO."),
    Round251ShadowWeightRow(E2RArchetype.AI_SOFTWARE_PARTNERSHIP_EVENT, 2, 2, 5, 2, 2, 4, 0, 3, 2, 2, -5, 2, 5, 3, "Kakao/OpenAI partnership is price_moved_without_evidence until monetization."),
    Round251ShadowWeightRow(E2RArchetype.GAME_IP_PLATFORM_EXPANSION, 3, 0, 3, 5, 0, 5, 5, 3, 3, 3, -4, 4, 4, 4, "Krafton needs bookings/IP conversion and India regulation clearance beyond downloads/M&A."),
    Round251ShadowWeightRow(E2RArchetype.SECURITY_OPERATIONAL_TRUST_HARD_4C, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0, 5, 4, 5, "SK Telecom breach is hard 4C with revenue, fine and compensation impact."),
    Round251ShadowWeightRow(E2RArchetype.KPOP_PLATFORM_CONTENT_IP_GOVERNANCE, 2, 1, 3, 4, 0, 4, 5, 5, 2, 2, -3, 5, 4, 5, "HYBE legal risk is 4C-watch; hard 4C only after legal outcome materially impairs business."),
)

ROUND251_CASE_CANDIDATES: tuple[Round251CaseCandidate, ...] = (
    Round251CaseCandidate(
        case_id="r8_loop11_douzone_bizon_eqt_saas",
        symbol="012510",
        company_name="Douzone Bizon",
        primary_archetype=E2RArchetype.B2B_SAAS_ERP_WORKFLOW,
        secondary_archetypes=(E2RArchetype.PRIVATE_EQUITY_SOFTWARE_RERATING, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_b2b_saas_stage2",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 11, 7),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stage2_watch_success_not_green_until_arr_churn_opm_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("eqt_37_6pct_stake_acquisition", "cloud_erp_accounting_tax_compliance_business", "sme_workflow_lock_in_candidate"),
        red_flag_fields=("arr_unverified", "churn_unverified", "opm_fcf_unverified", "regulatory_approval_required"),
        price_data_source="Reuters transaction evidence",
        reported_price_anchor="Douzone raw adjusted OHLC unavailable after deep search",
        reported_return_anchor="EQT $930M for 37.6%, implied equity value about $2.473B",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"eqt_investment_usd_mn": 930.0, "stake_acquired_pct": 37.6, "implied_equity_value_usd_bn": 2.473, "stake_from_chairman_pct": 23.2, "stake_from_shinhan_affiliates_pct": 14.4, "bpea_fund_ix_post_deal_exposure": "5_to_10pct"},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="EQT investment validates business quality, but Green requires ARR proxy, churn, OPM and FCF conversion.",
    ),
    Round251CaseCandidate(
        case_id="r8_loop11_samsung_sds_kkr_ai_4b",
        symbol="018260",
        company_name="Samsung SDS",
        primary_archetype=E2RArchetype.AI_CLOUD_CAPITAL_ALLOCATION,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="success_candidate",
        round_case_type="success_candidate_4b_watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 4, 15),
        stage3_date=None,
        stage4b_date=date(2026, 4, 15),
        stage4c_date=None,
        stage3_decision="should_not_be_green_until_recurring_ai_revenue_margin_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("kkr_820m_usd_convertible_bond", "ai_infra_mna_global_expansion_plan", "existing_cash_6_4tn_krw", "kkr_six_year_advisory_role"),
        red_flag_fields=("ai_revenue_unconfirmed", "cb_dilution_watch", "mna_execution_unconfirmed", "stablecoin_regulatory_risk"),
        price_data_source="Reuters reported event return anchor",
        reported_price_anchor="Samsung SDS intraday +20.8%, morning +19.4%, KOSPI +3.0%",
        reported_return_anchor="Relative intraday outperformance +17.8pp before recurring AI revenue confirmation",
        mfe_1d=20.8,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stage2_event_mfe_1d_pct": 20.8, "morning_trade_return_pct": 19.4, "kospi_same_context_pct": 3.0, "relative_intraday_outperformance_pp": 17.8, "cb_investment_usd_mn": 820.0, "cb_investment_krw_trn": 1.207, "existing_cash_krw_trn": 6.4, "combined_cash_plus_cb_krw_trn": 7.607, "kkr_advisory_period_years": 6.0},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="KKR/AI capital allocation is Stage 2 plus 4B-watch; recurring AI revenue and FCF are required for Green.",
    ),
    Round251CaseCandidate(
        case_id="r8_loop11_lg_cns_ai_cloud_ipo_price_failed",
        symbol="LG_CNS",
        company_name="LG CNS",
        primary_archetype=E2RArchetype.CLOUD_AI_SOFTWARE_INFRA,
        secondary_archetypes=(E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED, E2RArchetype.IPO_EVENT_PREMIUM),
        case_type="failed_rerating",
        round_case_type="evidence_good_but_price_failed",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 2, 5),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stage2_not_green_until_recurring_cloud_revenue_retention_margin_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ipo_price_61900_krw", "cloud_ai_services_54pct_sales_mix", "revenue_1q_3q_2024_4tn_krw", "op_313bn_krw"),
        red_flag_fields=("ipo_price_action_failed", "retention_unverified", "recurring_revenue_unverified", "fcf_unverified"),
        price_data_source="Reuters IPO price anchor",
        reported_price_anchor="IPO 61,900 won, opening 60,500, debut trade 59,700",
        reported_return_anchor="Debut MAE -3.55% despite cloud/AI services at 54% of sales",
        mfe_1d=None,
        mae_1d=-3.55,
        stage2_price_anchor=61900.0,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_price_krw": 61900.0, "opening_price_krw": 60500.0, "opening_return_vs_ipo_pct": -2.26, "debut_trade_price_krw": 59700.0, "debut_mae_pct": -3.55, "ipo_proceeds_krw_trn": 1.2, "morning_market_value_krw_trn": 5.79, "cloud_ai_sales_mix_pct": 54.0, "revenue_1q_3q_2024_krw_trn": 4.0, "op_1q_3q_2024_krw_bn": 313.0, "op_margin_1q_3q_2024_pct": 7.8},
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Cloud/AI mix is useful Stage 2 evidence, but IPO price action failed and Green needs recurring revenue, retention, margin and FCF.",
    ),
    Round251CaseCandidate(
        case_id="r8_loop11_naver_webtoon_ip_platform",
        symbol="035420/WBTN",
        company_name="NAVER / Webtoon",
        primary_archetype=E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION,
        secondary_archetypes=(E2RArchetype.PLATFORM_SOFTWARE_INTERNET, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_event_premium_watch",
        stage1_date=date(2024, 6, 1),
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=date(2025, 8, 13),
        stage4c_date=None,
        stage3_decision="stage2_watch_success_not_green_until_paid_usage_arpu_ip_licensing_operating_leverage_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("webtoon_ipo_price_21_usd", "debut_intraday_high_24_usd", "ipo_raise_315m_usd", "disney_collaboration_surprise_profit", "mau_155m_context"),
        red_flag_fields=("mau_without_arpu", "paid_usage_unverified", "post_ipo_drawdown_55pct", "fcf_unverified"),
        price_data_source="Reuters / Barron's price and earnings anchors",
        reported_price_anchor="Webtoon IPO $21 to $24; Disney event price $15.16 early trading",
        reported_return_anchor="IPO debut +14.3%, Disney/earnings event +62%, but pre-event post-IPO drawdown -55%",
        mfe_1d=14.3,
        mae_1d=None,
        stage2_price_anchor=21.0,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"webtoon_ipo_price_usd": 21.0, "webtoon_debut_intraday_high_usd": 24.0, "debut_mfe_from_ipo_pct": 14.3, "ipo_raise_usd_mn": 315.0, "naver_private_placement_usd_mn": 50.0, "disney_event_price_usd": 15.16, "disney_event_mfe_pct": 62.0, "pre_disney_post_ipo_drawdown_context_pct": -55.0, "disney_event_revenue_usd_mn": 348.3, "disney_event_revenue_growth_pct": 8.5, "adjusted_q2_profit_per_share_usd": 0.07, "expected_adjusted_loss_per_share_usd": -0.14, "mau_context_mn": 155.0},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="IP platform is Stage 2; paid usage, ARPU, IP licensing, operating leverage and FCF are required before Green.",
    ),
    Round251CaseCandidate(
        case_id="r8_loop11_kakao_openai_partnership_price_only",
        symbol="035720",
        company_name="Kakao",
        primary_archetype=E2RArchetype.AI_SOFTWARE_PARTNERSHIP_EVENT,
        secondary_archetypes=(E2RArchetype.PRICE_ONLY_RALLY, E2RArchetype.EVENT_PREMIUM),
        case_type="overheat",
        round_case_type="price_moved_without_evidence",
        stage1_date=date(2025, 2, 4),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 2, 4),
        stage4c_date=None,
        stage3_decision="should_have_been_stage1_or_4b_watch_until_paid_ai_usage_arpu_and_monetization_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("openai_kakao_partnership", "kakaotalk_ai_feature_expectation", "domestic_messaging_share_97pct"),
        red_flag_fields=("partnership_headline_only", "ai_revenue_unconfirmed", "paid_usage_unconfirmed", "founder_governance_legal_risk_watch"),
        price_data_source="Reuters event return anchor",
        reported_price_anchor="Kakao +9% before announcement and -2% on announcement day",
        reported_return_anchor="Two-session cumulative +6.8%, with -11pp fade from peak",
        mfe_1d=9.0,
        mae_1d=-2.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_mfe_before_announcement_pct": 9.0, "event_mae_following_day_pct": -2.0, "two_session_cumulative_return_pct": 6.8, "event_fade_from_peak_pp": -11.0, "kakaotalk_domestic_market_share_pct": 97.0, "ai_revenue_confirmed": False, "paid_usage_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="OpenAI partnership moved price before monetization; paid usage, ARPU and margin are required for Green.",
    ),
    Round251CaseCandidate(
        case_id="r8_loop11_krafton_game_ip_india_adk_watch",
        symbol="259960",
        company_name="Krafton",
        primary_archetype=E2RArchetype.GAME_IP_PLATFORM_EXPANSION,
        secondary_archetypes=(E2RArchetype.GAME_IP_M_AND_A_CONTENT_EXPANSION, E2RArchetype.GAME_CONTENT_IP),
        case_type="success_candidate",
        round_case_type="success_candidate_execution_watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 6, 24),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stage2_watch_success_not_green_until_bookings_retention_new_ip_conversion_india_regulation_and_fcf_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("adk_acquisition_75bn_yen", "adk_300_plus_animation_participation", "india_fund_target_666m_usd", "bgmi_240m_downloads"),
        red_flag_fields=("bookings_unverified", "retention_unverified", "bgmi_data_security_regulatory_risk", "subnautica_2_legal_dispute_watch", "ai_first_restructuring_risk"),
        price_data_source="Reuters India fund and ADK acquisition anchors",
        reported_price_anchor="Krafton adjusted OHLC unavailable after deep search",
        reported_return_anchor="ADK $516M and India fund $666M provide business anchors, not stage3 price path",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"adk_acquisition_value_yen_bn": 75.0, "adk_acquisition_value_usd_mn": 516.21, "adk_animation_participation_count": 300.0, "india_fund_target_usd_mn": 666.0, "india_fund_initial_pool_usd_mn": 333.0, "krafton_prior_india_investment_usd_mn": 200.0, "bgmi_downloads_mn": 240.0, "bgmi_risk": "temporary ban in India over data-security concerns"},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Game/IP expansion is Stage 2; bookings, retention, IP conversion, India regulation and FCF decide promotion.",
    ),
    Round251CaseCandidate(
        case_id="r8_loop11_skt_cybersecurity_operational_trust_hard_4c",
        symbol="017670",
        company_name="SK Telecom",
        primary_archetype=E2RArchetype.SECURITY_OPERATIONAL_TRUST_HARD_4C,
        secondary_archetypes=(E2RArchetype.SECURITY_OPERATIONAL_TRUST_OVERLAY, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        round_case_type="hard_4c_cybersecurity_operational_trust_break",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 28),
        stage3_decision="data_breach_revenue_cut_compensation_fine_and_security_investment_create_hard_4c",
        stage4b_status="none",
        hard_4c_confirmed=True,
        evidence_fields=("customer_data_leak_due_to_cyberattack", "23m_users_usim_replacement", "26_96m_data_pieces_leaked", "revenue_forecast_cut_800bn_krw", "pipc_fine_134bn_krw"),
        red_flag_fields=("privacy_breach", "data_leak_with_compensation_or_revenue_cut", "regulatory_sanction", "revenue_forecast_cut", "customer_benefit_package_cost", "security_investment_required"),
        price_data_source="Reuters breach / price / fine / revenue-cut anchors",
        reported_price_anchor="2025-04-28 intraday -8.5%, close -6.7%; KOSPI +0.1%",
        reported_return_anchor="Revenue cut 800B won, customer benefit package 500B won, PIPC fine 134B won",
        mfe_1d=None,
        mae_1d=-8.5,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_intraday_mae_pct": -8.5, "event_close_mae_pct": -6.7, "kospi_same_context_pct": 0.1, "relative_underperformance_close_pp": -6.8, "affected_users_initial_mn": 23.0, "usim_replacement_stores": 2600.0, "protection_service_signups_mn": 5.54, "signup_share_pct": 24.1, "leaked_user_data_pieces_mn": 26.96, "july4_close_mae_pct": -5.6, "security_investment_krw_bn": 700.0, "annualized_security_investment_krw_bn": 140.0, "revenue_forecast_cut_2025_krw_bn": 800.0, "customer_benefit_package_cost_krw_bn": 500.0, "pipc_fine_krw_bn": 134.0, "pipc_fine_usd_mn": 96.53},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Cybersecurity breach directly hit price, revenue guide, compensation and fine; this is hard 4C.",
    ),
    Round251CaseCandidate(
        case_id="r8_loop11_hybe_founder_legal_governance_watch",
        symbol="352820",
        company_name="HYBE",
        primary_archetype=E2RArchetype.KPOP_PLATFORM_CONTENT_IP_GOVERNANCE,
        secondary_archetypes=(E2RArchetype.KPOP_PLATFORM_CONTENT_IP, E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK),
        case_type="failed_rerating",
        round_case_type="governance_legal_4c_watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 4, 21),
        stage3_decision="governance_legal_overhang_blocks_green_until_legal_risk_clears_and_ip_monetization_confirms",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("bts_global_ip", "weverse_platform_expectation", "police_raid_over_ipo_share_probe", "founder_detention_warrant_request"),
        red_flag_fields=("founder_legal_risk", "ipo_related_investigation", "warrant_request", "governance_overhang", "hard_4c_not_confirmed_warrant_declined"),
        price_data_source="Reuters / AP legal event anchors",
        reported_price_anchor="HYBE -2.4% vs KOSPI +2.7% on warrant-request report",
        reported_return_anchor="Relative underperformance -5.1pp; warrant later declined so hard 4C remains unconfirmed",
        mfe_1d=None,
        mae_1d=-2.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_mae_1d_pct": -2.4, "kospi_same_context_pct": 2.7, "relative_underperformance_pp": -5.1, "alleged_profit_krw_bn": 190.0, "alleged_profit_usd_mn": 129.1, "travel_ban_since": "2025-08", "hard_4c_confirmed": False, "legal_relief_date": "2026-04-24"},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="K-pop IP monetization cannot outrank governance/legal overhang; warrant declined, so hard 4C is not confirmed.",
    ),
)


def round251_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND251_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND251_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round251 R8 Loop-11 platform/content/SW/security price validation case. Calibration-only; not production scoring input.",
            stage1_evidence=tuple(field for field in candidate.evidence_fields if "partnership" in field or "platform" in field or "ipo" in field or "ai" in field or "game" in field),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if "revenue" in field or "paid" in field or "bookings" in field or "fcf" in field or "opm" in field),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "event" in field or "premium" in field or "ipo" in field or "price" in field or "partnership" in field or "mna" in field),
            stage4c_evidence=tuple(field for field in candidate.red_flag_fields if "breach" in field or "leak" in field or "legal" in field or "sanction" in field or "revenue_forecast_cut" in field or "warrant" in field or "governance" in field),
            must_have_fields=ROUND251_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=("; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4c_thesis_break"} else None),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND251_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_stage_dates_arr_paid_usage_bookings_opm_fcf_or_security_costs",
                "do_not_treat_ai_platform_webtoon_game_or_kpop_headline_as_green",
                f"round_case_type={candidate.round_case_type}",
                *ROUND251_GREEN_REQUIRED_FIELDS,
                *ROUND251_GREEN_FORBIDDEN_PATTERNS,
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
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round251_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND251_CASE_CANDIDATES:
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


def round251_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND251_SCORE_ADJUSTMENTS)


def round251_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND251_SHADOW_WEIGHT_ROWS)


def round251_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round251_price_validation": "true"} for field in ROUND251_PRICE_VALIDATION_FIELDS)


def round251_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round251_label": label, "canonical_archetype": canonical} for label, canonical in ROUND251_REQUIRED_TARGET_ALIASES.items())


def round251_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple({"deep_sub_archetype": item, "large_sector": ROUND251_LARGE_SECTOR} for item in ROUND251_DEEP_SUB_ARCHETYPES)


def round251_summary() -> dict[str, int | bool | str]:
    cases = ROUND251_CASE_CANDIDATES
    return {
        "source_round": ROUND251_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND251_ANALYST_ROUND_ID,
        "large_sector": ROUND251_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND251_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND251_DEEP_SUB_ARCHETYPES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": True,
    }


def round251_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND251_SOURCE_ROUND_PATH,
        "analyst_round_id": ROUND251_ANALYST_ROUND_ID,
        "large_sector": ROUND251_LARGE_SECTOR,
        "summary": round251_summary(),
        "target_aliases": dict(ROUND251_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetypes": list(ROUND251_DEEP_SUB_ARCHETYPES),
        "green_required_fields": list(ROUND251_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND251_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND251_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND251_HARD_4C_GATES),
        "case_ids": [case.case_id for case in ROUND251_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_use_round251_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_ai_platform_webtoon_game_kpop_or_ipo_headline_as_green",
            "do_not_ignore_security_privacy_or_governance_hard_gates",
            "do_not_invent_ohlc_arr_paid_usage_bookings_opm_fcf_or_security_costs",
        ],
    }


def render_round251_summary_markdown() -> str:
    summary = round251_summary()
    lines = [
        "# Round 251 R8 Loop 11 Platform Content SW Security Price Validation",
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
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- 4C-watch cases: {summary['stage4c_watch_count']}",
        f"- evidence_good_but_price_failed: {summary['evidence_good_but_price_failed_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | round type | stage2 | stage3 | 4B | 4C | hard 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND251_CASE_CANDIDATES:
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
            "- Douzone is B2B SaaS Stage 2; ARR, churn, OPM and FCF decide promotion.",
            "- Samsung SDS is AI capital-allocation Stage 2 plus 4B-watch because price moved before recurring AI revenue.",
            "- LG CNS has cloud/AI evidence but IPO price action failed.",
            "- Webtoon is IP-platform Stage 2; paid usage, ARPU, IP licensing and FCF are required before Green.",
            "- Kakao/OpenAI is price_moved_without_evidence until paid AI usage and monetization appear.",
            "- Krafton is game/IP expansion Stage 2; bookings, retention, regulation and FCF decide promotion.",
            "- SK Telecom is hard 4C because the breach hit price, revenue outlook, compensation, security spend and fine.",
            "- HYBE is governance 4C-watch; warrant relief means hard 4C is not confirmed.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round251_green_gate_review_markdown() -> str:
    lines = [
        "# Round 251 R8 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND251_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND251_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND251_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `AI partnership` is not Green until paid usage, ARPU, margin and FCF appear.",
            "- `Webtoon MAU` is not enough without paid content, IP licensing and operating leverage.",
            "- `BGMI downloads` are useful context, but bookings and retention decide game/IP quality.",
            "- `Data breach with revenue cut and fine` is hard 4C because operational trust is broken.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round251_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 251 R8 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND251_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND251_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | 4C date | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND251_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.stage4b_status} | {_date_text(case.stage4c_date)} | "
            f"{str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round251_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 251 R8 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- hard_4c_confirmed: true",
        "- Do not invent OHLC, peak, MFE, MAE, stage prices, ARR, paid usage, bookings, OPM, FCF, security costs, or fines.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND251_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND251_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def render_round251_deep_sub_archetypes_markdown() -> str:
    lines = [
        "# Round 251 R8 Deep Sub-Archetypes",
        "",
        "These labels describe research coverage. They are not production scoring inputs.",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND251_DEEP_SUB_ARCHETYPES)
    return "\n".join(lines) + "\n"


def write_round251_r8_loop11_reports(
    output_directory: str | Path = ROUND251_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND251_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND251_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round251_case_records(), cases_path),
        "audit": _write_json(round251_audit_payload(), audit_path),
        "summary": output / "round251_r8_loop11_price_validation_summary.md",
        "case_matrix": output / "round251_r8_loop11_case_matrix.csv",
        "target_aliases": output / "round251_r8_loop11_target_aliases.csv",
        "deep_sub_archetypes": output / "round251_r8_loop11_deep_sub_archetypes.csv",
        "score_adjustments": output / "round251_r8_loop11_score_adjustments.csv",
        "shadow_weights": output / "round251_r8_loop11_shadow_weights.csv",
        "price_validation_fields": output / "round251_r8_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round251_r8_loop11_green_gate_review.md",
        "price_validation_plan": output / "round251_r8_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round251_r8_loop11_stage4b_4c_review.md",
        "deep_sub_archetype_review": output / "round251_r8_loop11_deep_sub_archetypes.md",
    }
    paths["summary"].write_text(render_round251_summary_markdown(), encoding="utf-8")
    _write_csv(round251_case_rows(), paths["case_matrix"])
    _write_csv(round251_target_alias_rows(), paths["target_aliases"])
    _write_csv(round251_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round251_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round251_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round251_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round251_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round251_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round251_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["deep_sub_archetype_review"].write_text(render_round251_deep_sub_archetypes_markdown(), encoding="utf-8")
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
