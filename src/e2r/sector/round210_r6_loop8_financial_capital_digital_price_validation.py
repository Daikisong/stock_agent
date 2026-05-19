"""Round-210 R6 Loop-8 financial/capital/digital price validation pack.

Round 210 is calibration/evaluation material only. It captures reported price
anchors, valuation anchors, event returns, ownership stakes, and transaction
values from ``docs/round/round_210.md``.

Simple example: `low PBR + value-up policy` can be Stage 1 attention. It is not
Stage 3-Green until ROE, capital buffer, executed cancellation, credit cost,
privacy/governance trust, and company-level capital allocation are visible
as-of the case date.
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


ROUND210_SOURCE_ROUND_PATH = "docs/round/round_210.md"
ROUND210_LARGE_SECTOR = Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL
ROUND210_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round210_r6_loop8_financial_capital_digital_price_validation"
ROUND210_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_loop8_round210.jsonl"
ROUND210_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round210_r6_loop8_financial_capital_digital_price_validation_audit.json"

ROUND210_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "VALUE_UP_SHAREHOLDER_RETURN": E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN.value,
    "HOLDING_RESTRUCTURING_GOVERNANCE": E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE.value,
    "TREASURY_SHARE_CANCEL_EXECUTION": E2RArchetype.TREASURY_SHARE_CANCEL_EXECUTION.value,
    "FINANCIAL_SPREAD_BALANCE_SHEET": E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET.value,
    "BANK_HOLDING_VALUEUP_CAPITAL_RETURN": E2RArchetype.BANK_HOLDING_VALUEUP_CAPITAL_RETURN.value,
    "BANK_ROE_PBR_RERATING_KOREA": E2RArchetype.BANK_ROE_PBR_RERATING_KOREA.value,
    "INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE": E2RArchetype.INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE.value,
    "INSURANCE_CAPITAL_RELEASE_VALUEUP": E2RArchetype.INSURANCE_CAPITAL_RELEASE_VALUEUP.value,
    "DIGITAL_ASSET_BANK_EQUITY_OPTION": E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION.value,
    "REGULATED_STABLECOIN_INFRA": E2RArchetype.REGULATED_STABLECOIN_INFRA.value,
    "KRW_STABLECOIN_POLICY_THEME": E2RArchetype.KRW_STABLECOIN_POLICY_THEME.value,
    "PAYMENT_FINTECH_INFRA": E2RArchetype.PAYMENT_FINTECH_INFRA.value,
    "PAYMENT_PRIVACY_REGULATORY_4C": E2RArchetype.PAYMENT_PRIVACY_REGULATORY_4C.value,
    "PLATFORM_GOVERNANCE_LEGAL_RISK": E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK.value,
    "DIGITAL_ASSET_TOKENIZATION": E2RArchetype.DIGITAL_ASSET_TOKENIZATION.value,
    "DIGITAL_ASSET_THEME_OVERHEAT": E2RArchetype.DIGITAL_ASSET_THEME_OVERHEAT.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
}

ROUND210_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "roe_improvement_or_sustainability",
    "cet1_or_kics_capital_buffer",
    "actual_buyback_cancellation",
    "durable_shareholder_return_policy",
    "credit_cost_pf_risk_passed",
    "pbr_roe_gap_rerating_runway",
    "regulated_revenue_or_equity_method_income",
    "privacy_data_governance_trust_passed",
    "price_path_after_evidence",
)

ROUND210_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "low_pbr_only",
    "policy_valueup_only",
    "treasury_buyback_without_cancellation",
    "stablecoin_policy_theme_only",
    "digital_asset_equity_option_without_revenue",
    "fintech_user_growth_without_profit",
    "privacy_or_data_trust_break",
    "major_shareholder_legal_risk",
    "capital_ratio_weakening",
    "mna_expansion_without_capital_buffer",
    "event_rally_before_regulated_revenue",
)

ROUND210_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "financials_trade_near_or_above_book_after_pbr_rerating",
    "buyback_cancellation_surprise_fades",
    "nav_rally_transferred_to_holding_or_insurance_without_monetization",
    "stablecoin_theme_two_to_three_x_without_revenue",
    "digital_asset_stake_investment_at_volume_peak",
    "mna_or_stock_swap_priced_before_regulatory_approval",
)

ROUND210_HARD_4C_GATES: tuple[str, ...] = (
    "pf_credit_cost_spike",
    "cet1_or_kics_weakening",
    "buyback_cancellation_cancelled",
    "dividend_payout_retreat",
    "large_acquisition_capital_ratio_damage",
    "major_shareholder_suitability_risk",
    "financial_crime_or_governance_legal_break",
    "privacy_data_transfer_fine",
    "stablecoin_forex_risk_regulation_tightening",
    "digital_asset_volume_collapse",
    "exchange_security_incident_or_abnormal_withdrawal",
    "equity_stake_impairment",
)

ROUND210_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "event_swing_pp",
    "discount_to_nav_or_book",
    "transaction_value",
    "implied_equity_value",
    "reported_theme_basket_return",
    "fine_amount",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round210ScoreAdjustment:
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
class Round210CaseCandidate:
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
    extra_price_metrics: Mapping[str, float | str]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND210_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND210_SCORE_ADJUSTMENTS: tuple[Round210ScoreAdjustment, ...] = (
    Round210ScoreAdjustment("roe_sustainability", 5, "raise", "저PBR보다 ROE가 유지되거나 개선되는지가 PBR frame change의 시작이다."),
    Round210ScoreAdjustment("cet1_or_capital_buffer", 5, "raise", "은행 CET1과 보험 K-ICS buffer가 있어야 환원과 인수가 지속된다."),
    Round210ScoreAdjustment("real_buyback_cancellation", 5, "raise", "자사주 매입보다 실제 소각이 자본배분 실행 증거다."),
    Round210ScoreAdjustment("dividend_payout_visibility", 4, "raise", "배당과 소각이 반복 가능한 policy로 고정될 때 신뢰도가 올라간다."),
    Round210ScoreAdjustment("credit_cost_control", 5, "raise", "PF와 credit cost가 안정돼야 금융주 rerating이 지속된다."),
    Round210ScoreAdjustment("pbr_roe_gap", 4, "raise", "ROE 대비 PBR discount가 줄어들 여지가 있어야 한다."),
    Round210ScoreAdjustment("capital_release_quality", 4, "raise", "보험/지주 NAV는 매각대금 활용과 자본 release가 확인될 때 강해진다."),
    Round210ScoreAdjustment("regulated_revenue_visibility", 4, "raise", "디지털자산/결제는 실제 수수료, 지분법, reserve income이 필요하다."),
    Round210ScoreAdjustment("nav_discount_with_monetization", 4, "raise", "NAV discount는 소각/배당/자산화로 이어질 때만 강하다."),
    Round210ScoreAdjustment("digital_asset_equity_value_with_regulation", 3, "raise", "디지털자산 지분 옵션은 규제 승인과 수익화 구조가 붙어야 한다."),
    Round210ScoreAdjustment("low_pbr_only", -5, "lower", "저PBR만으로는 Stage 3-Green을 만들 수 없다."),
    Round210ScoreAdjustment("policy_valueup_only", -4, "lower", "밸류업 정책 기대만 있고 실행이 없으면 Stage 1 attention이다."),
    Round210ScoreAdjustment("treasury_buyback_without_cancellation", -4, "lower", "자사주 매입만 있고 소각이 없으면 자본배분 품질을 제한한다."),
    Round210ScoreAdjustment("stablecoin_policy_theme_only", -5, "lower", "스테이블코인 정책 테마만으로는 규제수익을 증명하지 못한다."),
    Round210ScoreAdjustment("digital_asset_equity_option_without_revenue", -3, "lower", "지분 옵션만 있고 지분법/수수료/거래량 지속성이 없으면 Green 금지다."),
    Round210ScoreAdjustment("fintech_user_growth_without_profit", -3, "lower", "사용자 수 성장만 있고 take-rate/이익이 없으면 제한한다."),
    Round210ScoreAdjustment("privacy_or_data_trust_break", -5, "lower", "개인정보·데이터 신뢰 훼손은 결제/핀테크 hard gate다."),
    Round210ScoreAdjustment("major_shareholder_legal_risk", -5, "lower", "인터넷은행은 대주주 적격성 리스크가 성장성보다 먼저다."),
    Round210ScoreAdjustment("capital_ratio_weakening", -4, "lower", "대형 인수나 비은행 확장이 자본비율을 훼손하면 제한한다."),
    Round210ScoreAdjustment("mna_expansion_without_capital_buffer", -3, "lower", "M&A 확장은 자본 buffer와 수익성을 확인하기 전 Stage 2 watch다."),
    Round210ScoreAdjustment("event_rally_before_regulated_revenue", -5, "lower", "규제수익 전 가격 급등은 4B/event premium이다."),
)


ROUND210_CASE_CANDIDATES: tuple[Round210CaseCandidate, ...] = (
    Round210CaseCandidate(
        case_id="r6_loop8_sk_square_valueup_nav_discount",
        symbol="402340",
        company_name="SK스퀘어",
        primary_archetype=E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
        secondary_archetypes=(E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE, E2RArchetype.TREASURY_SHARE_CANCEL_EXECUTION, E2RArchetype.VALUE_UP_CROWDED_4B_WATCH),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 11, 21),
        stage3_date=None,
        stage4b_date=date(2026, 5, 14),
        stage4c_date=None,
        stage3_decision="stage3_requires_repeated_cancellation_nav_monetization_and_discount_narrowing_price_path_not_low_pbr_alone",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("buyback_cancelled_100bn_krw", "additional_buyback_cancel_plan_100bn_krw", "sk_hynix_stake_20pct", "holding_discount_to_skhynix_exposure"),
        red_flag_fields=("low_pbr_or_nav_discount_only", "skhynix_price_dependency", "discount_narrowing_price_path_unverified", "repeated_cancellation_unverified"),
        price_data_source="Reuters/Barron's valuation anchors",
        reported_price_anchor="stock OHLC unavailable; SK Square traded at 47% discount to SK Hynix exposure in 2026 hedge-fund view",
        reported_return_anchor="100bn KRW cancellation plus additional 100bn KRW buyback/cancellation plan; SK Hynix stake 20%",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"buyback_cancelled_krw_bn": 100.0, "additional_buyback_cancel_plan_krw_bn": 100.0, "total_announced_buyback_cancel_krw_bn": 200.0, "sk_hynix_stake_pct": 20.0, "discount_to_sk_hynix_exposure_pct": 47.0, "implied_value_capture_ratio_pct": 53.0},
        score_price_alignment="unknown",
        rerating_result="policy_event_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Actual cancellation supports Stage 2; Stage 3 requires repeated cancellation and NAV discount narrowing in the price path.",
    ),
    Round210CaseCandidate(
        case_id="r6_loop8_hana_dunamu_equity_option",
        symbol="086790",
        company_name="하나금융지주/하나은행",
        primary_archetype=E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION,
        secondary_archetypes=(E2RArchetype.REGULATED_STABLECOIN_INFRA, E2RArchetype.BANK_HOLDING_VALUEUP_CAPITAL_RETURN),
        case_type="success_candidate",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 5, 14),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stage3_requires_regulatory_approval_equity_method_income_capital_ratio_impact_and_volume_durability",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("dunamu_stake_acquired_6_55pct", "transaction_value_1_003tn_krw", "upbit_market_share_over_80pct", "blockchain_remittance_poc"),
        red_flag_fields=("equity_method_income_unverified", "regulatory_approval_unverified", "capital_ratio_impact_unverified", "stablecoin_forex_concern"),
        price_data_source="Reuters/WSJ transaction anchors",
        reported_price_anchor="Hana Financial stock OHLC unavailable",
        reported_return_anchor="Dunamu 6.55% stake acquired for 1.003tn KRW; implied Dunamu value about 15.31tn KRW",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"transaction_value_krw_trn": 1.003, "stake_acquired_pct": 6.55, "implied_dunamu_value_krw_trn": 15.31, "upbit_market_share_pct": 80.0},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Dunamu stake is a regulated digital-asset Stage 2 option; Stage 3 needs earnings contribution, capital impact, and regulatory clarity.",
    ),
    Round210CaseCandidate(
        case_id="r6_loop8_samsung_life_nav_valueup",
        symbol="032830",
        company_name="삼성생명",
        primary_archetype=E2RArchetype.INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE,
        secondary_archetypes=(E2RArchetype.INSURANCE_CAPITAL_RELEASE_VALUEUP, E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET),
        case_type="success_candidate",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 3, 19),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="stage3_requires_use_of_proceeds_shareholder_return_kics_csm_and_insurance_profit_quality_not_hidden_nav_only",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("samsung_electronics_stake_sale_1_3tn_krw", "samsung_electronics_stake_owned_about_10pct", "trades_about_50pct_of_book_value", "regulatory_risk_response"),
        red_flag_fields=("forced_sale_or_regulatory_overhang", "use_of_proceeds_unverified", "kics_csm_unverified", "samsung_electronics_nav_dependency"),
        price_data_source="Reuters/Barron's valuation anchors",
        reported_price_anchor="stock OHLC unavailable; trading about 50% of book value",
        reported_return_anchor="Samsung Electronics stake sale 1.3tn KRW; about 10% Samsung Electronics stake owned",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_electronics_stake_sale_krw_trn": 1.3, "samsung_electronics_stake_owned_pct": 10.0, "trading_level_vs_book_pct": 50.0, "implied_book_discount_pct": 50.0},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Hidden NAV and book discount support Stage 2; use of proceeds, K-ICS/CSM, and shareholder return are required for Stage 3.",
    ),
    Round210CaseCandidate(
        case_id="r6_loop8_naver_dunamu_digital_asset_event",
        symbol="035420",
        company_name="네이버/네이버파이낸셜",
        primary_archetype=E2RArchetype.DIGITAL_ASSET_TOKENIZATION,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_THEME_OVERHEAT, E2RArchetype.PAYMENT_FINTECH_INFRA),
        case_type="event_premium",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 11, 27),
        stage3_date=None,
        stage4b_date=date(2025, 11, 27),
        stage4c_date=date(2025, 11, 27),
        stage3_decision="stage3_deferred_until_merger_closing_regulatory_approval_fintech_monetization_volume_durability_and_exchange_security_pass",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("naver_financial_dunamu_stock_swap", "deal_value_15_13tn_krw", "upbit_market_leadership", "initial_event_return_above_7pct"),
        red_flag_fields=("abnormal_withdrawal_54bn_krw", "event_rally_before_regulated_revenue", "regulatory_approval_unverified", "exchange_security_trust_watch"),
        price_data_source="Reuters reported event returns and deal anchor",
        reported_price_anchor="absolute price unavailable",
        reported_return_anchor="Naver initially +7% then -4.2% after Upbit abnormal withdrawal; event swing -11.2pp",
        mfe_1d=7.0,
        mae_1d=-4.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"deal_value_krw_trn": 15.13, "event_mfe_initial_pct": 7.0, "event_mae_same_day_pct": -4.2, "abnormal_withdrawal_krw_bn": 54.0, "event_swing_pp": -11.2},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="The Dunamu transaction is strong Stage 2/event material, but abnormal withdrawal creates exchange-trust 4C-watch before Green.",
    ),
    Round210CaseCandidate(
        case_id="r6_loop8_kakaobank_kakao_governance_watch",
        symbol="323410/035720",
        company_name="카카오뱅크/카카오",
        primary_archetype=E2RArchetype.INTERNET_BANK_PROFITABILITY,
        secondary_archetypes=(E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK,),
        case_type="failed_rerating",
        stage1_date=date(2021, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 7, 23),
        stage3_decision="internet_bank_growth_cannot_be_green_before_roe_nim_fee_income_credit_quality_and_major_shareholder_suitability_risk_clear",
        stage4b_status="watch",
        hard_4c_confirmed=True,
        evidence_fields=("internet_bank_growth", "mobile_banking_scale", "founder_legal_overhang_relief_in_2025"),
        red_flag_fields=("major_shareholder_legal_risk", "bank_ownership_cap_risk", "financial_crime_governance_overhang", "kakaobank_direct_price_unavailable"),
        price_data_source="Reuters reported event returns and legal anchors",
        reported_price_anchor="KakaoBank direct price unavailable; Kakao proxy event return used",
        reported_return_anchor="Kakao -3.4% around founder arrest event; YTD -24% by 2024-07-23",
        mfe_1d=None,
        mae_1d=-3.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kakao_event_mae_1d": -3.4, "kakao_ytd_drawdown_pct": -24.0},
        score_price_alignment="false_positive_score",
        rerating_result="no_rerating",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="For KakaoBank, major-shareholder legal risk and bank ownership caps come before internet-bank growth scoring.",
    ),
    Round210CaseCandidate(
        case_id="r6_loop8_stablecoin_theme_overheat",
        symbol="377300/368970/158430/201490",
        company_name="Kakao Pay/LG CNS/Aton/ME2ON",
        primary_archetype=E2RArchetype.KRW_STABLECOIN_POLICY_THEME,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_THEME_OVERHEAT, E2RArchetype.PRICE_ONLY_RALLY, E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY),
        case_type="overheat",
        stage1_date=date(2025, 6, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 6, 1),
        stage4c_date=None,
        stage3_decision="stablecoin_theme_is_stage1_or_4b_until_licensed_issuer_bank_partnership_reserve_income_fee_revenue_and_capital_rules_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("won_stablecoin_policy_pledge", "crypto_reform_expectation", "kakao_pay_monthly_double", "me2on_tripled"),
        red_flag_fields=("stablecoin_policy_theme_only", "regulated_revenue_unverified", "non_bank_systemic_risk", "fx_outflow_risk", "price_only_rally"),
        price_data_source="FT reported return anchors",
        reported_price_anchor="absolute prices unavailable",
        reported_return_anchor="Kakao Pay >2x; LG CNS +70%; Aton +80%; ME2ON +200% in stablecoin-theme month",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kakao_pay_mfe_month_pct": 100.0, "lg_cns_mfe_month_pct": 70.0, "aton_mfe_month_pct": 80.0, "me2on_mfe_month_pct": 200.0},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="theme_overheat",
        stage_failure_type="false_yellow",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Stablecoin policy theme moved before licensing, reserve income, fee revenue, or capital rules; this is 4B/event premium.",
    ),
    Round210CaseCandidate(
        case_id="r6_loop8_kakao_pay_privacy_4c_watch",
        symbol="377300",
        company_name="카카오페이",
        primary_archetype=E2RArchetype.PAYMENT_PRIVACY_REGULATORY_4C,
        secondary_archetypes=(E2RArchetype.PAYMENT_FINTECH_INFRA,),
        case_type="4c_thesis_break",
        stage1_date=date(2021, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 1),
        stage3_decision="payment_volume_or_user_growth_cannot_be_green_when_privacy_data_trust_break_is_present",
        stage4b_status="watch",
        hard_4c_confirmed=True,
        evidence_fields=("payment_fintech_growth", "privacy_data_transfer_fine_summary"),
        red_flag_fields=("privacy_data_trust_break", "user_data_transfer_without_consent", "payment_privacy_regulatory_break", "source_confidence_medium_low"),
        price_data_source="Wikipedia/Korea Times summary only, lower confidence",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="15bn KRW fine; about 40mn affected user records",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"fine_amount_krw_bn": 15.0, "affected_user_count_mn": 40.0, "source_confidence": "medium_low"},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Payment fintech Green should be blocked by privacy/data-transfer trust break even when payment-volume narratives look attractive.",
    ),
)


def round210_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND210_CASE_CANDIDATES:
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
                "Round210 R6 Loop-8 financial/capital/digital price-path "
                "validation case. Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(field for field in candidate.evidence_fields if "policy" in field or "growth" in field or "discount" in field or "option" in field),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "buyback" in field
                or "cancel" in field
                or "roe" in field
                or "capital" in field
                or "stake" in field
                or "revenue" in field
                or "book" in field
                or "discount" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "theme" in field or "rally" in field or "event" in field or "price" in field or "nav" in field or "discount" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "privacy" in field
                or "legal" in field
                or "trust" in field
                or "capital" in field
                or "credit" in field
                or "security" in field
                or "withdrawal" in field
                or "regulatory" in field
                or "fx" in field
            ),
            must_have_fields=ROUND210_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={
                "roe_sustainability_delta": 5.0,
                "cet1_or_capital_buffer_delta": 5.0,
                "real_buyback_cancellation_delta": 5.0,
                "dividend_payout_visibility_delta": 4.0,
                "credit_cost_control_delta": 5.0,
                "pbr_roe_gap_delta": 4.0,
                "capital_release_quality_delta": 4.0,
                "regulated_revenue_visibility_delta": 4.0,
                "nav_discount_with_monetization_delta": 4.0,
                "digital_asset_equity_value_with_regulation_delta": 3.0,
                "low_pbr_only_delta": -5.0,
                "policy_valueup_only_delta": -4.0,
                "treasury_buyback_without_cancellation_delta": -4.0,
                "stablecoin_policy_theme_only_delta": -5.0,
                "digital_asset_equity_option_without_revenue_delta": -3.0,
                "fintech_user_growth_without_profit_delta": -3.0,
                "privacy_or_data_trust_break_delta": -5.0,
                "major_shareholder_legal_risk_delta": -5.0,
                "capital_ratio_weakening_delta": -4.0,
                "mna_expansion_without_capital_buffer_delta": -3.0,
                "event_rally_before_regulated_revenue_delta": -5.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_low_pbr_policy_stablecoin_theme_digital_asset_option_or_mna_event_as_green_alone",
                *ROUND210_GREEN_REQUIRED_FIELDS,
                *ROUND210_GREEN_FORBIDDEN_PATTERNS,
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
                price_data_available=False,
                stage_dates_confidence=0.8 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round210_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND210_CASE_CANDIDATES:
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


def round210_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND210_SCORE_ADJUSTMENTS)


def round210_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round210_price_validation": "true"} for field in ROUND210_PRICE_VALIDATION_FIELDS)


def round210_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round210_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND210_REQUIRED_TARGET_ALIASES.items()
    )


def round210_summary() -> dict[str, int | bool | str]:
    cases = ROUND210_CASE_CANDIDATES
    return {
        "source_round": ROUND210_SOURCE_ROUND_PATH,
        "large_sector": ROUND210_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "thesis_break_count": sum(1 for case in cases if case.case_type == "4c_thesis_break"),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "target_archetype_count": len(ROUND210_REQUIRED_TARGET_ALIASES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
    }


def round210_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND210_SOURCE_ROUND_PATH,
        "large_sector": ROUND210_LARGE_SECTOR.value,
        "summary": round210_summary(),
        "target_aliases": dict(ROUND210_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND210_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND210_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND210_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND210_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_use_round210_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_low_pbr_policy_stablecoin_theme_or_digital_asset_option_as_green",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round210_summary_markdown() -> str:
    summary = round210_summary()
    lines = [
        "# Round 210 R6 Loop 8 Financial Capital Digital Price Validation",
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
        f"- overheat: {summary['overheat_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- 4c_thesis_break: {summary['thesis_break_count']}",
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
    for case in ROUND210_CASE_CANDIDATES:
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
            "- SK Square, Hana, and Samsung Life are Stage 2 candidates until capital execution and price-path proof improve.",
            "- Naver/Dunamu is digital-asset Stage 2/event material with exchange-trust 4C-watch.",
            "- Stablecoin basket rallies are price-moved-without-evidence until licensing, reserve income, fee revenue, and capital rules exist.",
            "- KakaoBank/Kakao and Kakao Pay privacy cases show governance and data trust can block Green before growth scoring matters.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round210_green_gate_review_markdown() -> str:
    lines = [
        "# Round 210 R6 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND210_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND210_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `low PBR + value-up policy` means Stage 1 attention.",
            "- `actual cancellation + ROE + capital buffer + credit-cost control` is the bundle that can support Stage 3.",
            "- `stablecoin policy theme + 2x price move` is 4B/event premium until regulated revenue exists.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round210_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 210 R6 4B/4C Review",
        "",
        "## 4B Watch Triggers",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND210_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND210_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND210_CASE_CANDIDATES:
        if case.stage4b_status == "watch" or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round210_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 210 R6 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND210_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round210_r6_loop8_reports(
    output_directory: str | Path = ROUND210_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND210_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND210_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)

    paths = {
        "cases": write_case_library(round210_case_records(), cases_path),
        "audit": _write_json(round210_audit_payload(), audit_path),
        "summary": output / "round210_r6_loop8_price_validation_summary.md",
        "case_matrix": output / "round210_r6_loop8_case_matrix.csv",
        "target_aliases": output / "round210_r6_loop8_target_aliases.csv",
        "score_adjustments": output / "round210_r6_loop8_score_adjustments.csv",
        "price_validation_fields": output / "round210_r6_loop8_price_validation_fields.csv",
        "green_gate_review": output / "round210_r6_loop8_green_gate_review.md",
        "price_validation_plan": output / "round210_r6_loop8_price_validation_plan.md",
        "stage4b_4c_review": output / "round210_r6_loop8_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round210_summary_markdown(), encoding="utf-8")
    _write_csv(round210_case_rows(), paths["case_matrix"])
    _write_csv(round210_target_alias_rows(), paths["target_aliases"])
    _write_csv(round210_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round210_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round210_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round210_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round210_stage4b_4c_review_markdown(), encoding="utf-8")
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
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _float_text(value: float | None) -> str:
    return "" if value is None else f"{value:g}"
