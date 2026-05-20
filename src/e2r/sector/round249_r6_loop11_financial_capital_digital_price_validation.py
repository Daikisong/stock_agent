"""Round-249 R6 Loop-11 financial/capital/digital price-validation pack.

This module converts ``docs/round/round_249.md`` into structured,
calibration-only case-library records and reports. It does not change
production scoring or candidate generation.

Easy example: a bank can rally on "low PBR" and value-up policy. That is
Stage 2 at best until ROE, CET1, credit cost, and actual repeated cancellation
or dividend execution confirm.
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


ROUND249_SOURCE_ROUND_PATH = "docs/round/round_249.md"
ROUND249_ROUND_ID = "round_177"
ROUND249_LARGE_SECTOR = Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL.value
ROUND249_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round249_r6_loop11_financial_capital_digital_price_validation"
ROUND249_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_loop11_round249.jsonl"
ROUND249_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round249_r6_loop11_financial_capital_digital_price_validation_audit.json"

ROUND249_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BANK_VALUEUP_ROE_PBR_RERATING": E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING.value,
    "SECURITIES_MARKET_VOLUME_CYCLE": E2RArchetype.SECURITIES_MARKET_VOLUME_CYCLE.value,
    "HOLDING_NAV_DISCOUNT_VALUEUP": E2RArchetype.HOLDING_NAV_DISCOUNT_VALUEUP.value,
    "INSURANCE_NAV_CAPITAL_RELEASE": E2RArchetype.INSURANCE_NAV_CAPITAL_RELEASE.value,
    "DIGITAL_ASSET_BANK_EQUITY_OPTION": E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION.value,
    "DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH": E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH.value,
    "INTERNET_BANK_IPO_PROFITABILITY": E2RArchetype.INTERNET_BANK_IPO_PROFITABILITY.value,
    "INTERNET_BANK_GOVERNANCE_4C": E2RArchetype.INTERNET_BANK_GOVERNANCE_4C.value,
    "KRW_STABLECOIN_POLICY_OVERHEAT": E2RArchetype.KRW_STABLECOIN_POLICY_OVERHEAT.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
}

ROUND249_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "roe_improving_or_sustained",
    "cet1_or_kics_capital_buffer",
    "credit_cost_or_pf_risk_passed",
    "actual_buyback_cancellation",
    "repeat_dividend_or_cancellation_policy",
    "pbr_roe_gap_and_rerating_runway",
    "capital_release_use_confirmed",
    "regulated_revenue_or_equity_method_income",
    "platform_or_exchange_trust_passed",
    "price_path_after_evidence",
)

ROUND249_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "low_pbr_only",
    "policy_valueup_only",
    "treasury_buyback_without_cancellation",
    "stablecoin_policy_theme_only",
    "digital_asset_equity_option_without_revenue",
    "fintech_user_growth_without_profit",
    "event_rally_before_regulated_revenue",
    "major_shareholder_legal_risk",
    "exchange_trust_break",
)

ROUND249_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "pbr_rerating_before_roe_and_return_execution",
    "securities_sector_plus_10pct_before_revenue_confirmation",
    "nav_trade_crowded_after_underlying_asset_rally",
    "insurance_nav_rally_before_capital_policy",
    "digital_asset_equity_option_priced_before_revenue",
    "mna_or_all_stock_deal_priced_before_approval",
    "stablecoin_related_stock_doubles_or_triples_before_license",
)

ROUND249_HARD_4C_GATES: tuple[str, ...] = (
    "pf_credit_cost_spike",
    "cet1_or_kics_weakening",
    "buyback_cancellation_cancelled",
    "dividend_policy_retreat",
    "capital_ratio_damaged_by_acquisition",
    "major_shareholder_suitability_break",
    "financial_crime_or_governance_legal_break",
    "exchange_abnormal_withdrawal",
    "stablecoin_issuer_regulation_reversal",
    "digital_asset_volume_collapse",
    "stake_investment_impairment",
)

ROUND249_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "transaction_value_anchor",
    "policy_or_regulatory_anchor",
    "capital_or_trust_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round249ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round249ShadowWeightRow:
    archetype: E2RArchetype
    roe: int
    capital_buffer: int
    buyback_cancel: int
    shareholder_return: int
    pbr_roe_gap: int
    credit_cost: int
    regulated_revenue: int
    nav_monetization: int
    platform_trust: int
    event_penalty: int
    governance_trust_redteam: int
    stage4b_watch_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "roe": _signed(self.roe),
            "capital_buffer": _signed(self.capital_buffer),
            "buyback_cancel": _signed(self.buyback_cancel),
            "shareholder_return": _signed(self.shareholder_return),
            "pbr_roe_gap": _signed(self.pbr_roe_gap),
            "credit_cost": _signed(self.credit_cost),
            "regulated_revenue": _signed(self.regulated_revenue),
            "nav_monetization": _signed(self.nav_monetization),
            "platform_trust": _signed(self.platform_trust),
            "event_penalty": _signed(self.event_penalty),
            "governance_trust_redteam": _signed(self.governance_trust_redteam),
            "4b_watch_sensitivity": _signed(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round249DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round249CaseCandidate:
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


ROUND249_SCORE_ADJUSTMENTS: tuple[Round249ScoreAdjustment, ...] = (
    Round249ScoreAdjustment("roe_sustainability", 5, "raise", "R6 Green은 저PBR보다 ROE 지속성이 먼저다."),
    Round249ScoreAdjustment("cet1_or_capital_buffer", 5, "raise", "은행/보험은 자본비율이 주주환원 지속성을 결정한다."),
    Round249ScoreAdjustment("real_buyback_cancellation", 5, "raise", "자사주 매입보다 실제 소각이 중요하다."),
    Round249ScoreAdjustment("dividend_payout_visibility", 4, "raise", "반복 배당 정책은 PBR 프레임 전환의 증거다."),
    Round249ScoreAdjustment("credit_cost_control", 5, "raise", "PF와 credit cost를 통과해야 value-up이 Green으로 올라간다."),
    Round249ScoreAdjustment("pbr_roe_gap", 4, "raise", "PBR-ROE gap은 rerating runway를 판단하는 축이다."),
    Round249ScoreAdjustment("capital_release_quality", 4, "raise", "보험/지주 NAV는 현금화와 활용처가 확인될 때 강해진다."),
    Round249ScoreAdjustment("regulated_revenue_visibility", 4, "raise", "디지털자산은 규제수익/지분법 이익이 보여야 한다."),
    Round249ScoreAdjustment("nav_discount_with_monetization", 4, "raise", "NAV discount는 소각/매각/환원으로 연결될 때 Stage 2 품질이 올라간다."),
    Round249ScoreAdjustment("digital_asset_equity_value_with_regulation", 3, "raise", "거래소 지분가치는 규제와 신뢰를 통과해야 은행 가치가 된다."),
    Round249ScoreAdjustment("platform_trust", 5, "raise", "플랫폼 금융은 신뢰가 깨지면 사용자와 거래가 빠질 수 있다."),
    Round249ScoreAdjustment("low_pbr_only", -5, "lower", "저PBR만으로는 구조적 rerating 증거가 아니다."),
    Round249ScoreAdjustment("policy_valueup_only", -4, "lower", "정책 기대는 회사별 ROE/환원으로 닫혀야 한다."),
    Round249ScoreAdjustment("treasury_buyback_without_cancellation", -4, "lower", "매입만 있고 소각이 없으면 환원 실행력이 약하다."),
    Round249ScoreAdjustment("stablecoin_policy_theme_only", -5, "lower", "스테이블코인 정책 테마만으로는 수익모델이 없다."),
    Round249ScoreAdjustment("digital_asset_equity_option_without_revenue", -3, "lower", "거래소 지분투자는 지분법/규제수익 전 Stage 2 watch다."),
    Round249ScoreAdjustment("fintech_user_growth_without_profit", -3, "lower", "인터넷은행/핀테크 user count는 ROE와 credit quality 전 Green이 아니다."),
    Round249ScoreAdjustment("exchange_trust_break", -5, "lower", "abnormal withdrawal 같은 거래소 신뢰 훼손은 4C-watch다."),
    Round249ScoreAdjustment("major_shareholder_legal_risk", -5, "lower", "인터넷은행 대주주 적격성 리스크는 Green을 막는다."),
    Round249ScoreAdjustment("capital_ratio_weakening", -4, "lower", "인수나 주주환원 뒤 자본비율이 훼손되면 thesis break다."),
    Round249ScoreAdjustment("event_rally_before_regulated_revenue", -5, "lower", "규제수익 전 이벤트 급등은 4B-watch다."),
)


ROUND249_SHADOW_WEIGHT_ROWS: tuple[Round249ShadowWeightRow, ...] = (
    Round249ShadowWeightRow(E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING, 5, 5, 5, 5, 5, 5, 0, 0, 2, -3, 3, 4, 4, "Bank value-up needs ROE/CET1/credit cost and repeated shareholder return."),
    Round249ShadowWeightRow(E2RArchetype.SECURITIES_MARKET_VOLUME_CYCLE, 4, 3, 0, 2, 3, 3, 0, 0, 2, -3, 2, 5, 4, "Securities +13.5% is cyclical; revenue/ROE must confirm before Green."),
    Round249ShadowWeightRow(E2RArchetype.HOLDING_NAV_DISCOUNT_VALUEUP, 2, 2, 5, 5, 5, 1, 0, 5, 2, -2, 2, 4, 3, "SK Square needs actual cancellation and discount narrowing."),
    Round249ShadowWeightRow(E2RArchetype.INSURANCE_NAV_CAPITAL_RELEASE, 3, 5, 1, 4, 5, 3, 0, 5, 2, -2, 3, 4, 4, "Samsung Life needs use of proceeds and K-ICS/CSM confirmation."),
    Round249ShadowWeightRow(E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION, 2, 4, 0, 1, 2, 2, 5, 2, 4, -3, 4, 5, 4, "Hana/Dunamu is Stage 2 until regulated revenue and capital impact confirm."),
    Round249ShadowWeightRow(E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH, 2, 3, 0, 1, 2, 2, 5, 1, 5, -4, 5, 5, 5, "Naver/Dunamu has exchange-trust 4C-watch from abnormal withdrawal."),
    Round249ShadowWeightRow(E2RArchetype.INTERNET_BANK_IPO_PROFITABILITY, 5, 4, 0, 1, 4, 5, 2, 0, 3, -4, 3, 5, 4, "K Bank needs listed path, ROE/NIM/credit quality."),
    Round249ShadowWeightRow(E2RArchetype.INTERNET_BANK_GOVERNANCE_4C, 0, 0, 0, 0, 0, 0, 0, 0, 5, -3, 5, 3, 5, "KakaoBank Green blocked by major shareholder legal/ownership risk."),
    Round249ShadowWeightRow(E2RArchetype.KRW_STABLECOIN_POLICY_OVERHEAT, 0, 1, 0, 0, 1, 0, 1, 0, 3, -5, 4, 5, 4, "Stablecoin rally is price_moved_without_evidence until licensing/revenue clarity."),
)


ROUND249_DEEP_SUB_ARCHETYPES: tuple[Round249DeepSubArchetype, ...] = (
    Round249DeepSubArchetype("Bank value-up", E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING, ("KB", "Shinhan", "Hana", "Woori", "ROE", "CET1", "credit cost")),
    Round249DeepSubArchetype("Securities cycle", E2RArchetype.SECURITIES_MARKET_VOLUME_CYCLE, ("securities basket", "KOSPI 7000", "trading volume", "brokerage", "IB")),
    Round249DeepSubArchetype("Holding NAV", E2RArchetype.HOLDING_NAV_DISCOUNT_VALUEUP, ("SK Square", "SK Hynix stake", "buyback cancellation", "NAV discount")),
    Round249DeepSubArchetype("Insurance NAV", E2RArchetype.INSURANCE_NAV_CAPITAL_RELEASE, ("Samsung Life", "Samsung Electronics stake", "K-ICS", "CSM")),
    Round249DeepSubArchetype("Bank digital asset", E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION, ("Hana Bank", "Dunamu", "Upbit", "equity method income")),
    Round249DeepSubArchetype("Platform merger trust", E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH, ("NAVER Financial", "Dunamu", "abnormal withdrawal", "exchange trust")),
    Round249DeepSubArchetype("Internet bank", E2RArchetype.INTERNET_BANK_IPO_PROFITABILITY, ("K Bank", "KakaoBank", "IPO", "credit quality", "NIM")),
    Round249DeepSubArchetype("Internet bank governance", E2RArchetype.INTERNET_BANK_GOVERNANCE_4C, ("Kakao founder", "bank ownership cap", "major shareholder suitability")),
    Round249DeepSubArchetype("KRW stablecoin theme", E2RArchetype.KRW_STABLECOIN_POLICY_OVERHEAT, ("Kakao Pay", "LG CNS", "Aton", "ME2ON", "issuer license", "reserve income")),
)


ROUND249_CASE_CANDIDATES: tuple[Round249CaseCandidate, ...] = (
    Round249CaseCandidate(
        case_id="r6_loop11_big4_financial_valueup_stage2",
        symbol="105560/055550/086790/316140",
        company_name="KB/Shinhan/Hana/Woori financial groups",
        primary_archetype=E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING,
        secondary_archetypes=(E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN, E2RArchetype.BANK_HOLDING_VALUEUP_CAPITAL_RETURN_KOREA),
        case_type="success_candidate",
        round_case_type="market_structure_stage2_not_green",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2026, 2, 25),
        stage3_date=None,
        stage4b_date=date(2026, 5, 6),
        stage4c_date=None,
        stage3_decision="bank_valueup_is_stage2_until_roe_cet1_credit_cost_and_repeated_shareholder_return_confirm",
        stage4b_status="4B-watch-PBR-rerating-before-bank-specific-execution",
        hard_4c_confirmed=False,
        evidence_fields=("commercial_act_treasury_cancellation", "financial_groups_plus_4_2pct", "foreign_net_purchase_3_1tn_krw", "kospi_plus_6_45pct"),
        red_flag_fields=("low_pbr_only", "policy_valueup_only", "credit_cost_unconfirmed", "cet1_unconfirmed", "return_execution_unconfirmed"),
        price_data_source="Reuters Commercial Act / KOSPI 7000 sector-return anchors",
        reported_price_anchor="Financial groups +4.2%; KOSPI +6.45%; foreign net purchase 3.1T won",
        reported_return_anchor="Newly acquired treasury shares must be cancelled within 1 year; existing shares 6-month grace period",
        mfe_1d=4.2,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"commercial_act_revision_date": "2026-02-25", "existing_treasury_share_grace_period_months": 6, "financial_groups_event_mfe_1d_pct": 4.2, "kospi_same_context_pct": 6.45, "relative_underperformance_vs_kospi_pp": -2.25, "foreign_net_purchase_krw_trn": 3.1, "foreign_net_purchase_usd_bn": 2.13},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="policy_event_rerating",
        round_rerating_label="bank_valueup_ROE_PBR_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="market_structure_stage2_not_green",
        price_validation_status="reported_sector_anchor_not_full_ohlc",
        notes="Bank value-up is Stage 2; ROE/CET1/credit cost and repeated shareholder return required before Green.",
    ),
    Round249CaseCandidate(
        case_id="r6_loop11_securities_capital_market_boom",
        symbol="securities_basket",
        company_name="Korean securities firms basket",
        primary_archetype=E2RArchetype.SECURITIES_MARKET_VOLUME_CYCLE,
        secondary_archetypes=(E2RArchetype.SECURITIES_BROKERAGE_CYCLE, E2RArchetype.SECURITIES_IB_PF_RISK_OVERLAY),
        case_type="cyclical_success",
        round_case_type="cyclical_success_4B-watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 5, 6),
        stage3_date=None,
        stage4b_date=date(2026, 5, 6),
        stage4c_date=None,
        stage3_decision="securities_rally_is_cycle_stage2_until_brokerage_ib_revenue_roe_and_risk_controls_confirm",
        stage4b_status="4B-watch-sector-plus-13_5pct-before-revenue-proof",
        hard_4c_confirmed=False,
        evidence_fields=("kospi_plus_6_45pct", "securities_plus_13_5pct", "foreign_net_purchase_3_1tn_krw", "trading_volume_cycle"),
        red_flag_fields=("market_beta_only", "brokerage_revenue_unconfirmed", "ib_revenue_unconfirmed", "pf_risk_unconfirmed"),
        price_data_source="Reuters sector-return anchor",
        reported_price_anchor="Securities firms +13.5%; KOSPI close +6.45%; intraday high +7.06%",
        reported_return_anchor="Securities relative outperformance vs KOSPI +7.05pp",
        mfe_1d=13.5,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kospi_event_return_pct": 6.45, "kospi_intraday_high_return_pct": 7.06, "securities_firms_mfe_1d_pct": 13.5, "relative_outperformance_vs_kospi_pp": 7.05, "foreign_net_purchase_krw_trn": 3.1, "foreign_net_purchase_usd_bn": 2.13},
        score_price_alignment="aligned",
        round_alignment_label="cyclical_success",
        rerating_result="cyclical_rerating",
        round_rerating_label="securities_market_volume_boom_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_cyclical_not_green",
        price_validation_status="reported_sector_return_not_full_ohlc",
        notes="Securities rally is Stage 2/cyclical and 4B-watch; brokerage/IB revenue and ROE required before Green.",
    ),
    Round249CaseCandidate(
        case_id="r6_loop11_sk_square_nav_discount_valueup",
        symbol="402340",
        company_name="SK Square",
        primary_archetype=E2RArchetype.HOLDING_NAV_DISCOUNT_VALUEUP,
        secondary_archetypes=(E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE, E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN),
        case_type="success_candidate",
        round_case_type="NAV_discount_valueup_stage2",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 11, 21),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="NAV_discount_stage2_until_repeat_cancellation_and_actual_discount_narrowing_confirm",
        stage4b_status="4B-watch-if-SK-Hynix-NAV-trade-becomes-crowded",
        hard_4c_confirmed=False,
        evidence_fields=("cancelled_buyback_100bn_krw", "additional_buyback_cancel_plan_100bn_krw", "sk_hynix_stake_20pct", "nav_discount_above_50pct"),
        red_flag_fields=("nav_discount_without_monetization", "underlying_asset_dependency", "repeat_cancellation_unconfirmed"),
        price_data_source="Reuters buyback / NAV-discount anchor",
        reported_price_anchor="100B won cancellation plus 100B won additional buyback/cancel plan",
        reported_return_anchor="SK Square market value less than half of $18B SK Hynix stake value",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"cancelled_buyback_krw_bn": 100.0, "additional_buyback_cancel_plan_krw_bn": 100.0, "total_buyback_cancel_program_krw_bn": 200.0, "sk_hynix_stake_pct": 20.0, "sk_hynix_stake_value_2024_usd_bn": 18.0, "minimum_nav_discount_2024_pct": 50.0, "palliser_stake_pct": 1.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="policy_event_rerating",
        round_rerating_label="NAV_discount_valueup_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Actual cancellation supports Stage 2; repeated cancellation and discount narrowing required for Stage 3.",
    ),
    Round249CaseCandidate(
        case_id="r6_loop11_samsung_life_nav_capital_release",
        symbol="032830",
        company_name="Samsung Life",
        primary_archetype=E2RArchetype.INSURANCE_NAV_CAPITAL_RELEASE,
        secondary_archetypes=(E2RArchetype.INSURANCE_CAPITAL_RELEASE_VALUEUP_KOREA, E2RArchetype.INSURANCE_KICS_CSM_GATE),
        case_type="success_candidate",
        round_case_type="success_candidate_regulatory_watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 3, 19),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="insurance_nav_capital_release_is_stage2_until_use_of_proceeds_kics_csm_and_return_policy_confirm",
        stage4b_status="4B-watch-if-Samsung-Electronics-NAV-rally-over-reflected",
        hard_4c_confirmed=False,
        evidence_fields=("samsung_electronics_stake_sale_1_3tn_krw", "regulatory_risk_resolution", "capital_release_candidate"),
        red_flag_fields=("use_of_proceeds_unconfirmed", "kics_unconfirmed", "csm_unconfirmed", "affiliate_price_dependency"),
        price_data_source="Reuters regulatory share-sale anchor",
        reported_price_anchor="Samsung Electronics stake sale 1.3T won / $867.07M",
        reported_return_anchor="Purpose: resolve local financial-company governance regulation risk",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_electronics_stake_sale_krw_trn": 1.3, "samsung_electronics_stake_sale_usd_mn": 867.07, "fx_rate_krw_per_usd": 1499.3},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_regulatory_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="insurance_NAV_valueup_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Capital release is Stage 2; use of proceeds, K-ICS/CSM and shareholder return required before Green.",
    ),
    Round249CaseCandidate(
        case_id="r6_loop11_hana_dunamu_equity_option",
        symbol="086790",
        company_name="Hana Financial / Hana Bank / Dunamu",
        primary_archetype=E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION,
        secondary_archetypes=(E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_STAKE, E2RArchetype.KRW_STABLECOIN_POLICY_OPTION),
        case_type="success_candidate",
        round_case_type="regulated_digital_asset_equity_option_stage2",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 5, 14),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="digital_asset_equity_option_is_stage2_until_equity_method_income_regulated_revenue_and_capital_impact_confirm",
        stage4b_status="4B-watch-if-digital-asset-option-priced-before-revenue",
        hard_4c_confirmed=False,
        evidence_fields=("dunamu_6_55pct_stake_acquired", "transaction_value_1tn_krw", "implied_dunamu_equity_15_27tn_krw", "upbit_share_above_80pct"),
        red_flag_fields=("regulated_revenue_unconfirmed", "equity_method_income_unconfirmed", "capital_ratio_impact_unconfirmed", "exchange_trust_risk"),
        price_data_source="Reuters / WSJ transaction anchor",
        reported_price_anchor="Hana Bank acquires 6.55% Dunamu stake for 1T won / about $700M",
        reported_return_anchor="Implied Dunamu equity value about 15.27T won; Upbit share >80%",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"transaction_value_krw_trn": 1.0, "transaction_value_usd_mn": 700.0, "stake_acquired_pct": 6.55, "implied_dunamu_equity_value_krw_trn": 15.27, "upbit_trading_volume_share_pct": 80.0, "kakao_investment_remaining_stake_pct": 4.03, "completion_timing": "2026-06-15_expected_by_WSJ"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="regulated_digital_asset_equity_option",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Dunamu stake is Stage 2; regulated revenue, equity-method earnings, capital impact and exchange trust required for Stage 3.",
    ),
    Round249CaseCandidate(
        case_id="r6_loop11_naver_dunamu_platform_merger_trust_watch",
        symbol="035420",
        company_name="NAVER / NAVER Financial / Dunamu",
        primary_archetype=E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_EXCHANGE_CONSOLIDATION, E2RArchetype.EXCHANGE_SECURITY_OPERATIONAL_RISK),
        case_type="event_premium",
        round_case_type="success_candidate_event_premium_4C-watch",
        stage1_date=date(2025, 11, 27),
        stage2_date=date(2025, 11, 27),
        stage3_date=None,
        stage4b_date=date(2025, 11, 27),
        stage4c_date=date(2025, 11, 27),
        stage3_decision="deal_is_stage2_but_abnormal_withdrawal_blocks_green_until_approval_closing_revenue_and_trust_clear",
        stage4b_status="4B-watch-initial-plus-7pct-before-approval-and-trust-clearance",
        hard_4c_confirmed=False,
        evidence_fields=("all_stock_deal_15_13tn_krw", "exchange_ratio_2_54", "upbit_market_share_70pct", "initial_naver_plus_7pct"),
        red_flag_fields=("abnormal_withdrawal_54bn_krw", "exchange_trust_watch", "regulatory_approval_pending", "security_resolution_unconfirmed"),
        price_data_source="Reuters transaction / event-return anchor",
        reported_price_anchor="NAVER initially +7% then -4.2% after 54B won Upbit abnormal withdrawal",
        reported_return_anchor="15.13T won all-stock deal; 2.54 NAVER Financial shares per Dunamu share",
        mfe_1d=7.0,
        mae_1d=-4.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"deal_value_krw_trn": 15.13, "deal_value_usd_bn": 10.27, "exchange_ratio_naver_financial_per_dunamu": 2.54, "upbit_market_share_pct": 70.0, "event_mfe_initial_pct": 7.0, "event_mae_same_day_pct": -4.2, "event_swing_pp": -11.2, "abnormal_withdrawal_krw_bn": 54.0},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_trust_watch",
        rerating_result="event_premium",
        round_rerating_label="digital_asset_platform_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="stage2_watch_success_with_4C_watch",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="Strong Stage 2 digital-asset merger, but abnormal withdrawal creates exchange-trust 4C-watch.",
    ),
    Round249CaseCandidate(
        case_id="r6_loop11_internet_bank_kbank_kakaobank_watch",
        symbol="unlisted_KBank/323410/035720",
        company_name="K Bank / KakaoBank / Kakao",
        primary_archetype=E2RArchetype.INTERNET_BANK_IPO_PROFITABILITY,
        secondary_archetypes=(E2RArchetype.INTERNET_BANK_GOVERNANCE_4C, E2RArchetype.INTERNET_BANK_PROFITABILITY),
        case_type="success_candidate",
        round_case_type="success_candidate_governance_4C_watch",
        stage1_date=date(2024, 9, 10),
        stage2_date=date(2024, 9, 10),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 7, 23),
        stage3_decision="kbank_is_unlisted_stage2_and_kakaobank_green_blocked_by_major_shareholder_legal_risk",
        stage4b_status="4B-watch-if-IPO-valuation-priced-before-credit-quality",
        hard_4c_confirmed=False,
        evidence_fields=("kbank_ipo_raise_max_984bn_krw", "kbank_h1_op_86_7bn_krw", "customers_above_10mn", "kakao_founder_arrest_governance_risk"),
        red_flag_fields=("unlisted_ipo_candidate", "credit_quality_unconfirmed", "major_shareholder_legal_risk", "bank_ownership_cap_risk"),
        price_data_source="Reuters IPO / legal-governance anchors",
        reported_price_anchor="Kakao -3.4% on founder arrest; YTD -24% context",
        reported_return_anchor="K Bank IPO up to 984B won; valuation up to about 5T won; H1 OP 86.7B won",
        mfe_1d=None,
        mae_1d=-3.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kbank_ipo_raise_max_krw_bn": 984.0, "kbank_price_range_low_krw": 9500.0, "kbank_price_range_high_krw": 12000.0, "kbank_shares_to_sell_mn": 82.0, "kbank_max_offer_value_check_krw_bn": 984.0, "kbank_reported_valuation_up_to_krw_trn": 5.0, "kbank_h1_2024_operating_profit_krw_bn": 86.7, "kbank_customer_count_mn": 10.0, "kakao_event_mae_1d_pct": -3.4, "kakao_ytd_drawdown_context_pct": -24.0, "kim_controlled_stake_pct": 24.0, "bank_ownership_cap_risk_pct": 10.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_for_KBank_thesis_break_watch_for_KakaoBank",
        rerating_result="unknown",
        round_rerating_label="internet_bank_profitability_watch_with_governance_gate",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_unlisted_not_green_governance_4C_watch",
        price_validation_status="kbank_unlisted_kakaobank_ohlc_unavailable",
        notes="K Bank is unlisted Stage 2; KakaoBank Green is blocked by major shareholder legal/ownership risk.",
    ),
    Round249CaseCandidate(
        case_id="r6_loop11_stablecoin_policy_theme_overheat",
        symbol="377300/LG_CNS/158430/ME2ON",
        company_name="Kakao Pay / stablecoin policy basket",
        primary_archetype=E2RArchetype.KRW_STABLECOIN_POLICY_OVERHEAT,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_THEME_OVERHEAT, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="overheat",
        round_case_type="overheat_price_moved_without_evidence",
        stage1_date=date(2025, 6, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 6, 1),
        stage4c_date=None,
        stage3_decision="stablecoin_policy_theme_is_not_green_before_issuer_license_reserve_income_fee_revenue_and_regulatory_capital",
        stage4b_status="4B-watch-related-stocks-doubled-or-tripled-before-revenue-proof",
        hard_4c_confirmed=False,
        evidence_fields=("kakao_pay_more_than_2x", "lg_cns_plus_70pct", "aton_plus_80pct", "me2on_3x", "margin_loan_20_5tn_krw"),
        red_flag_fields=("stablecoin_policy_theme_only", "issuer_license_unconfirmed", "reserve_income_unconfirmed", "fee_revenue_unconfirmed", "fx_risk_concern"),
        price_data_source="FT reported return and policy-risk anchors",
        reported_price_anchor="Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x",
        reported_return_anchor="Margin loan 20.5T won; proposed minimum equity for issuers 500M won",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kakao_pay_mfe_month_pct": 100.0, "lg_cns_mfe_month_pct": 70.0, "aton_mfe_month_pct": 80.0, "me2on_mfe_month_pct": 200.0, "margin_loan_context_krw_trn": 20.5, "proposed_minimum_equity_for_issuers_krw_mn": 500.0, "regulated_revenue_confirmed": False, "issuer_license_confirmed": False, "reserve_income_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence",
        rerating_result="theme_overheat",
        round_rerating_label="stablecoin_policy_theme_overheat",
        stage_failure_type="false_yellow",
        round_stage_failure_label="should_have_been_stage1_or_4B_watch",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Stablecoin theme rallied before licensed issuer, reserve income, fee revenue or regulatory capital clarity.",
    ),
)


def round249_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(_case_record(candidate) for candidate in ROUND249_CASE_CANDIDATES)


def _case_record(candidate: Round249CaseCandidate) -> E2RCaseRecord:
    return E2RCaseRecord(
        case_id=candidate.case_id,
        symbol=candidate.symbol,
        company_name=candidate.company_name,
        market="KR",
        sector_raw=ROUND249_LARGE_SECTOR,
        primary_archetype=candidate.primary_archetype,
        expected_group=candidate.expected_group,
        large_sector=ROUND249_LARGE_SECTOR,
        secondary_archetypes=candidate.secondary_archetypes,
        case_type=candidate.case_type,
        stage1_date=candidate.stage1_date,
        stage2_date=candidate.stage2_date,
        stage3_date=candidate.stage3_date,
        stage4b_date=candidate.stage4b_date,
        stage4c_date=candidate.stage4c_date,
        evidence_summary=(
            f"Round249 R6 Loop-11 price-validation case. {candidate.notes} "
            "Calibration-only; production scoring and candidate generation are unchanged."
        ),
        stage1_evidence=tuple(field for field in candidate.evidence_fields if any(token in field for token in ("policy", "valueup", "kospi", "ipo", "stablecoin", "deal"))),
        stage2_evidence=candidate.evidence_fields,
        stage3_evidence=(),
        stage4b_evidence=tuple(field for field in candidate.evidence_fields if candidate.stage4b_date is not None),
        stage4c_evidence=tuple(candidate.red_flag_fields if candidate.stage4c_date is not None else ()),
        must_have_fields=ROUND249_GREEN_REQUIRED_FIELDS,
        red_flag_fields=candidate.red_flag_fields,
        key_evidence_fields=candidate.evidence_fields,
        false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"overheat", "event_premium", "failed_rerating", "4c_thesis_break"} else None,
        score_price_alignment=candidate.score_price_alignment,
        rerating_result=candidate.rerating_result,
        stage_failure_type=candidate.stage_failure_type,
        price_pattern=candidate.round_case_type,
        score_weight_hint={item.axis: float(item.points) for item in ROUND249_SCORE_ADJUSTMENTS},
        green_guardrails=(
            "production_scoring_changed_false",
            "candidate_generation_input_false",
            "shadow_weight_only_true",
            "full_ohlc_complete_false",
            "do_not_treat_low_pbr_valueup_stablecoin_digital_asset_or_ipo_headline_as_green",
            *ROUND249_GREEN_REQUIRED_FIELDS,
            *ROUND249_GREEN_FORBIDDEN_PATTERNS,
        ),
        notes=candidate.notes,
        price_validation=PriceValidation(
            stage2_price=candidate.stage2_price_anchor,
            stage3_price=candidate.stage3_price_anchor,
            stage4b_price=candidate.stage4b_price_anchor,
            stage4c_price=candidate.stage4c_price_anchor,
            mfe_30d=None,
            mae_30d=None,
            price_validation_status=candidate.price_validation_status,
        ),
        data_quality=CaseDataQuality(
            official_data_available=True,
            report_data_available=True,
            price_data_available=False,
            stage_dates_confidence=0.75,
        ),
    )


def round249_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "case_id": case.case_id,
            "symbol": case.symbol,
            "company_name": case.company_name,
            "case_type": case.case_type,
            "primary_archetype": case.primary_archetype.value,
            "secondary_archetypes": "|".join(item.value for item in case.secondary_archetypes),
            "stage1_date": _date_text(case.stage1_date),
            "stage2_date": _date_text(case.stage2_date),
            "stage3_date": _date_text(case.stage3_date),
            "stage4b_date": _date_text(case.stage4b_date),
            "stage4c_date": _date_text(case.stage4c_date),
            "stage3_decision": case.stage3_decision,
            "stage4b_status": case.stage4b_status,
            "hard_4c_confirmed": str(case.hard_4c_confirmed).lower(),
            "evidence_fields": "|".join(case.evidence_fields),
            "red_flag_fields": "|".join(case.red_flag_fields),
            "price_data_source": case.price_data_source,
            "reported_price_anchor": case.reported_price_anchor,
            "reported_return_anchor": case.reported_return_anchor,
            "mfe_1d": _float_text(case.mfe_1d),
            "mae_1d": _float_text(case.mae_1d),
            "score_price_alignment": case.score_price_alignment,
            "round_alignment_label": case.round_alignment_label,
            "rerating_result": case.rerating_result,
            "round_rerating_label": case.round_rerating_label,
            "stage_failure_type": case.stage_failure_type,
            "round_stage_failure_label": case.round_stage_failure_label,
            "price_validation_status": case.price_validation_status,
            "extra_price_metrics": json.dumps(case.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "notes": case.notes,
        }
        for case in ROUND249_CASE_CANDIDATES
    )


def round249_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"target_alias": alias, "canonical_archetype": archetype} for alias, archetype in ROUND249_REQUIRED_TARGET_ALIASES.items())


def round249_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND249_SCORE_ADJUSTMENTS)


def round249_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND249_SHADOW_WEIGHT_ROWS)


def round249_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND249_DEEP_SUB_ARCHETYPES)


def round249_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_now": "false", "reason": "round249 full OHLC not available; keep missing values explicit"} for field in ROUND249_PRICE_VALIDATION_FIELDS)


def round249_summary() -> dict[str, object]:
    cases = ROUND249_CASE_CANDIDATES
    return {
        "source_round": ROUND249_SOURCE_ROUND_PATH,
        "round_id": ROUND249_ROUND_ID,
        "large_sector": ROUND249_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for case in cases if case.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B-watch" in case.stage4b_status),
        "watch_4c_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.round_case_type),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "reported_price_anchor_count": sum(1 for case in cases if case.price_validation_status != "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND249_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND249_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND249_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round249_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND249_SOURCE_ROUND_PATH,
        "round_id": ROUND249_ROUND_ID,
        "large_sector": ROUND249_LARGE_SECTOR,
        "summary": round249_summary(),
        "target_aliases": dict(ROUND249_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND249_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND249_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND249_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND249_HARD_4C_GATES),
        "score_adjustments": list(round249_score_adjustment_rows()),
        "shadow_weights": list(round249_shadow_weight_rows()),
        "deep_sub_archetypes": list(round249_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND249_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round249_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_low_pbr_valueup_stablecoin_digital_asset_or_ipo_headline_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round249_summary_markdown() -> str:
    summary = round249_summary()
    lines = [
        "# Round 249 R6 Loop 11 Financial Capital Digital Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- cyclical_success: {summary['cyclical_success_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- hard_4c_confirmed: {str(summary['hard_4c_confirmed']).lower()}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND249_CASE_CANDIDATES:
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
            "- Big-4 financial groups value-up is Stage 2, not Green, until ROE/CET1/credit cost and repeated return execution confirm.",
            "- Securities +13.5% is cyclical Stage 2 and 4B-watch before brokerage/IB revenue proof.",
            "- SK Square and Samsung Life are NAV/capital-release Stage 2 cases, not Green without monetization/use-of-proceeds proof.",
            "- Hana/Dunamu and NAVER/Dunamu are digital-asset Stage 2 cases with regulated-revenue and trust gates.",
            "- K Bank is unlisted profitability Stage 2, while KakaoBank has major-shareholder governance 4C-watch.",
            "- Stablecoin basket is price_moved_without_evidence until issuer license, reserve income, fee revenue and regulatory capital are confirmed.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round249_green_gate_review_markdown() -> str:
    lines = [
        "# Round 249 R6 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R6 Stage 3-Green is not `low PBR`, `value-up`, `digital asset`, or `stablecoin`. It requires ROE, capital buffer, actual cancellation/dividend execution, regulated revenue, and platform trust.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND249_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND249_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND249_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `low PBR` is only a cheap label until ROE and credit cost are proven.",
            "- `buyback` is weaker than actual cancellation.",
            "- `stablecoin policy` is a theme until issuer license, reserve income, and fee revenue exist.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round249_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 249 R6 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND249_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND249_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | interpretation |", "|---|---|---|---|"])
    for case in ROUND249_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round249_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 249 R6 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, CET1, K-ICS, credit cost, equity-method income, stablecoin revenue, MFE, or MAE where raw adjusted daily prices or filings are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND249_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND249_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round249_r6_loop11_reports(
    output_directory: str | Path = ROUND249_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND249_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND249_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round249_case_records(), cases_path),
        "audit": _write_json(round249_audit_payload(), audit_path),
        "summary": output / "round249_r6_loop11_price_validation_summary.md",
        "case_matrix": output / "round249_r6_loop11_case_matrix.csv",
        "target_aliases": output / "round249_r6_loop11_target_aliases.csv",
        "score_adjustments": output / "round249_r6_loop11_score_adjustments.csv",
        "shadow_weights": output / "round249_r6_loop11_shadow_weights.csv",
        "deep_sub_archetypes": output / "round249_r6_loop11_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round249_r6_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round249_r6_loop11_green_gate_review.md",
        "price_validation_plan": output / "round249_r6_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round249_r6_loop11_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round249_summary_markdown(), encoding="utf-8")
    _write_csv(round249_case_rows(), paths["case_matrix"])
    _write_csv(round249_target_alias_rows(), paths["target_aliases"])
    _write_csv(round249_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round249_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round249_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round249_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round249_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round249_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round249_stage4b_4c_review_markdown(), encoding="utf-8")
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
