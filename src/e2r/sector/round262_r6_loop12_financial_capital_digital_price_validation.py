"""Round-262 R6 Loop-12 financial/capital/digital price-validation pack.

This module converts ``docs/round/round_262.md`` into calibration-only case
records and reports. It intentionally leaves production scoring, candidate
generation, and StageClassifier thresholds unchanged.

Easy example: a securities basket can rise 13.5% on a KOSPI 7000 day, but that
is a market-volume cycle until brokerage fee, IB revenue, ROE, and PF risk are
confirmed.
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


ROUND262_SOURCE_ROUND_PATH = "docs/round/round_262.md"
ROUND262_ROUND_ID = "round_190"
ROUND262_LARGE_SECTOR = Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL.value
ROUND262_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round262_r6_loop12_financial_capital_digital_price_validation"
ROUND262_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_loop12_round262.jsonl"
ROUND262_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round262_r6_loop12_financial_capital_digital_price_validation_audit.json"

ROUND262_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BANK_VALUEUP_ROE_PBR_RERATING": E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING.value,
    "BROKERAGE_MARKET_VOLUME_CYCLE": E2RArchetype.BROKERAGE_MARKET_VOLUME_CYCLE.value,
    "INSURANCE_NAV_CAPITAL_RELEASE": E2RArchetype.INSURANCE_NAV_CAPITAL_RELEASE.value,
    "BANK_DIGITAL_ASSET_EQUITY_OPTION": E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_OPTION.value,
    "DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH": E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH.value,
    "FINTECH_SUPERAPP_BIOMETRIC_PAYMENT": E2RArchetype.FINTECH_SUPERAPP_BIOMETRIC_PAYMENT.value,
    "INTERNET_BANK_GOVERNANCE_4C": E2RArchetype.INTERNET_BANK_GOVERNANCE_4C.value,
    "STABLECOIN_POLICY_OVERHEAT_FX_GATE": E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE.value,
}

ROUND262_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "roe_improvement_or_sustainability",
    "cet1_kics_or_capital_buffer_sufficient",
    "credit_cost_or_pf_risk_stable",
    "actual_buyback_cancellation_or_recurring_dividend",
    "brokerage_ib_or_trading_income_sustainability",
    "regulated_digital_revenue_or_equity_method_income",
    "platform_exchange_trust_intact",
    "data_privacy_and_biometric_risk_passed",
    "fx_outflow_and_stablecoin_macro_risk_passed",
    "price_path_after_evidence",
)

ROUND262_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "low_pbr_only",
    "policy_valueup_only",
    "market_volume_spike_only",
    "stablecoin_theme_only",
    "digital_asset_equity_option_only",
    "major_shareholder_legal_risk_present",
    "exchange_trust_incident_present",
    "privacy_or_data_gate_unresolved",
)

ROUND262_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "pbr_rerating_before_roe_cet1",
    "securities_basket_plus_10pct_on_volume_cycle",
    "bank_rerates_on_digital_asset_stake_before_equity_method_income",
    "stablecoin_related_stocks_double_or_triple_without_revenue_model",
    "large_platform_merger_priced_before_regulatory_approval",
    "toss_ipo_or_facepay_narrative_before_take_rate_credit_cost",
    "financial_valueup_prices_before_actual_cancellation_or_dividend",
)

ROUND262_HARD_4C_GATES: tuple[str, ...] = (
    "pf_credit_cost_spike",
    "cet1_or_kics_deterioration",
    "buyback_cancellation_failure",
    "dividend_retreat",
    "bank_ownership_suitability_failure",
    "financial_crime_conviction_affecting_bank_control",
    "exchange_abnormal_withdrawal_or_hack",
    "stablecoin_driven_fx_outflow",
    "non_bank_issuer_failure",
    "biometric_data_breach",
    "major_credit_loss_from_fintech_lending",
)

ROUND262_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "relative_performance_vs_kospi",
    "capital_return_or_ratio_anchor",
    "digital_revenue_or_equity_anchor",
    "trust_privacy_or_fx_gate",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round262ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round262ShadowWeightRow:
    archetype: E2RArchetype
    roe_sustainability: int
    capital_buffer: int
    real_buyback_cancel: int
    recurring_dividend: int
    credit_cost: int
    brokerage_fee_sustainability: int
    regulated_digital_revenue: int
    equity_method_visibility: int
    platform_trust: int
    fx_stability: int
    data_privacy: int
    event_penalty: int
    stage4b_watch_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "roe_sustainability": _signed(self.roe_sustainability),
            "capital_buffer": _signed(self.capital_buffer),
            "real_buyback_cancel": _signed(self.real_buyback_cancel),
            "recurring_dividend": _signed(self.recurring_dividend),
            "credit_cost": _signed(self.credit_cost),
            "brokerage_fee_sustainability": _signed(self.brokerage_fee_sustainability),
            "regulated_digital_revenue": _signed(self.regulated_digital_revenue),
            "equity_method_visibility": _signed(self.equity_method_visibility),
            "platform_trust": _signed(self.platform_trust),
            "fx_stability": _signed(self.fx_stability),
            "data_privacy": _signed(self.data_privacy),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round262DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round262CaseCandidate:
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


ROUND262_SCORE_ADJUSTMENTS: tuple[Round262ScoreAdjustment, ...] = (
    Round262ScoreAdjustment("ROE_sustainability", 5, "raise", "R6 Green은 저PBR보다 지속 ROE가 먼저다."),
    Round262ScoreAdjustment("CET1_or_capital_buffer", 5, "raise", "은행과 보험은 자본비율이 주주환원을 받쳐야 한다."),
    Round262ScoreAdjustment("real_buyback_cancellation", 5, "raise", "자사주는 취득보다 실제 소각이 중요하다."),
    Round262ScoreAdjustment("recurring_dividend_policy", 4, "raise", "반복 배당정책이 있어야 value-up이 일회성이 아니다."),
    Round262ScoreAdjustment("credit_cost_control", 5, "raise", "PF와 credit cost가 흔들리면 저PBR 리레이팅은 막힌다."),
    Round262ScoreAdjustment("brokerage_fee_sustainability", 4, "raise", "증권주는 거래대금 spike보다 수수료와 IB 수익 지속성이 필요하다."),
    Round262ScoreAdjustment("regulated_digital_revenue", 5, "raise", "디지털자산과 스테이블코인은 규제된 수익모델이 보여야 한다."),
    Round262ScoreAdjustment("equity_method_visibility", 4, "raise", "Dunamu 지분투자는 지분법 이익으로 닫혀야 은행 EPS가 된다."),
    Round262ScoreAdjustment("platform_trust", 5, "raise", "거래소·결제 플랫폼은 trust가 깨지면 scale이 의미 없다."),
    Round262ScoreAdjustment("FX_stability", 5, "raise", "stablecoin은 FX outflow gate를 통과해야 한다."),
    Round262ScoreAdjustment("data_privacy_control", 5, "raise", "생체결제와 fintech는 privacy/data gate가 hard risk다."),
    Round262ScoreAdjustment("low_PBR_only", -5, "lower", "저PBR만으로는 Stage 3 근거가 아니다."),
    Round262ScoreAdjustment("policy_valueup_only", -5, "lower", "정책 value-up만 있고 실제 소각·배당이 없으면 Stage 2다."),
    Round262ScoreAdjustment("market_volume_spike_only", -4, "lower", "거래대금 spike는 cycle이지 구조적 Green이 아니다."),
    Round262ScoreAdjustment("digital_asset_equity_option_only", -4, "lower", "디지털자산 지분투자만으로 은행 EPS가 생기지 않는다."),
    Round262ScoreAdjustment("stablecoin_policy_theme_only", -5, "lower", "스테이블코인 정책 테마는 수익모델 전까지 가격 테마다."),
    Round262ScoreAdjustment("nonbank_stablecoin_FX_risk", -5, "lower", "비은행 발행과 FX outflow는 4C-watch다."),
    Round262ScoreAdjustment("exchange_trust_break", -5, "lower", "거래소 이상출금과 hack은 digital finance hard gate다."),
    Round262ScoreAdjustment("biometric_data_risk", -4, "lower", "생체정보 사고는 fintech thesis break가 될 수 있다."),
    Round262ScoreAdjustment("major_shareholder_legal_risk", -5, "lower", "인터넷은행은 대주주 적격성 리스크가 성장성보다 먼저다."),
    Round262ScoreAdjustment("event_rally_before_regulated_revenue", -5, "lower", "규제된 수익 전 이벤트 rally는 4B-watch다."),
)


ROUND262_SHADOW_WEIGHT_ROWS: tuple[Round262ShadowWeightRow, ...] = (
    Round262ShadowWeightRow(E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING, 5, 5, 5, 4, 5, 0, 0, 0, 3, 3, 1, -5, 4, 5, "Financial holding value-up is Stage 2 until ROE/CET1/credit cost and recurring capital return confirm."),
    Round262ShadowWeightRow(E2RArchetype.BROKERAGE_MARKET_VOLUME_CYCLE, 4, 3, 0, 2, 3, 5, 0, 0, 3, 3, 1, -4, 5, 4, "Securities +13.5% is cyclical success and 4B-watch before revenue/ROE confirmation."),
    Round262ShadowWeightRow(E2RArchetype.INSURANCE_NAV_CAPITAL_RELEASE, 3, 5, 2, 4, 3, 0, 0, 0, 3, 2, 1, -3, 4, 4, "Samsung Life stake sale is capital release Stage 2; K-ICS/CSM/use of proceeds needed."),
    Round262ShadowWeightRow(E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_OPTION, 2, 4, 0, 1, 2, 1, 5, 5, 5, 4, 3, -4, 5, 5, "Hana/Dunamu is Stage 2 until regulated revenue/equity-method earnings and trust confirm."),
    Round262ShadowWeightRow(E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH, 2, 3, 0, 1, 2, 1, 5, 4, 5, 4, 4, -5, 5, 5, "Naver/Dunamu has exchange abnormal-withdrawal 4C-watch."),
    Round262ShadowWeightRow(E2RArchetype.FINTECH_SUPERAPP_BIOMETRIC_PAYMENT, 3, 3, 0, 0, 4, 3, 5, 0, 5, 4, 5, -4, 5, 5, "Toss FacePay is unlisted Stage 2 with biometric privacy/data gate."),
    Round262ShadowWeightRow(E2RArchetype.INTERNET_BANK_GOVERNANCE_4C, 0, 4, 0, 0, 4, 2, 2, 0, 5, 2, 3, 0, 4, 5, "KakaoBank Green blocked by major-shareholder legal/ownership risk."),
    Round262ShadowWeightRow(E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE, 0, 2, 0, 0, 0, 0, 5, 0, 3, 5, 4, -5, 5, 5, "Stablecoin basket moved before issuer license/reserve income/fee revenue and creates FX 4C-watch."),
)


ROUND262_DEEP_SUB_ARCHETYPES: tuple[Round262DeepSubArchetype, ...] = (
    Round262DeepSubArchetype("금융지주 value-up", E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING, ("KB", "Shinhan", "Hana", "Woori", "treasury-share cancellation", "ROE", "CET1", "credit cost")),
    Round262DeepSubArchetype("증권 거래대금 cycle", E2RArchetype.BROKERAGE_MARKET_VOLUME_CYCLE, ("securities basket", "KOSPI 7000", "brokerage revenue", "IB", "trading income")),
    Round262DeepSubArchetype("보험 NAV capital release", E2RArchetype.INSURANCE_NAV_CAPITAL_RELEASE, ("Samsung Life", "Samsung Electronics stake sale", "K-ICS", "CSM", "use of proceeds")),
    Round262DeepSubArchetype("은행 디지털자산 지분 option", E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_OPTION, ("Hana Bank", "Dunamu", "Upbit", "equity-method income", "remittance")),
    Round262DeepSubArchetype("플랫폼 금융 merger trust", E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH, ("NAVER Financial", "Dunamu", "Naver Pay", "Upbit", "abnormal withdrawal")),
    Round262DeepSubArchetype("핀테크 super-app biometric", E2RArchetype.FINTECH_SUPERAPP_BIOMETRIC_PAYMENT, ("Toss", "FacePay", "Toss Bank", "Toss Securities", "biometric payment", "privacy")),
    Round262DeepSubArchetype("인터넷은행 governance 4C", E2RArchetype.INTERNET_BANK_GOVERNANCE_4C, ("Kakao", "KakaoBank", "founder legal risk", "bank ownership suitability")),
    Round262DeepSubArchetype("Stablecoin / FX gate", E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE, ("Kakao Pay", "LG CNS", "Aton", "ME2ON", "kimchi bond", "FX outflow")),
)


ROUND262_CASE_CANDIDATES: tuple[Round262CaseCandidate, ...] = (
    Round262CaseCandidate(
        case_id="r6_loop12_financial_holdings_valueup_stage2",
        symbol="105560/055550/086790/316140",
        company_name="Korean financial holding value-up basket",
        primary_archetype=E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING,
        secondary_archetypes=(E2RArchetype.BANK_HOLDING_VALUEUP_CAPITAL_RETURN, E2RArchetype.TREASURY_CANCEL_MANDATE_POLICY),
        case_type="success_candidate",
        round_case_type="success_candidate / Stage 2, not Green",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2026, 2, 25),
        stage3_date=None,
        stage4b_date=date(2026, 5, 6),
        stage4c_date=None,
        stage3_decision="valueup_policy_and_sector_rally_are_not_green_before_roe_cet1_credit_cost_and_actual_return",
        stage4b_status="4B-watch if PBR rerates before ROE and capital return",
        hard_4c_confirmed=False,
        evidence_fields=("commercial_act_treasury_share_cancellation_rule", "financial_groups_plus_4_2pct", "kospi_plus_6_45pct", "foreign_net_purchase_3_1tn_krw"),
        red_flag_fields=("low_pbr_only", "policy_valueup_only", "roe_cet1_credit_cost_unconfirmed", "relative_underperformance_vs_kospi"),
        price_data_source="Reuters Commercial Act / KOSPI 7000 event-return anchors",
        reported_price_anchor="Financial groups +4.2% while KOSPI +6.45%; foreign investors bought 3.1T KRW",
        reported_return_anchor="Relative performance vs KOSPI -2.25pp on KOSPI 7000 context",
        mfe_1d=4.2,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"financial_groups_event_mfe_pct": 4.2, "kospi_same_context_pct": 6.45, "relative_performance_vs_kospi_pp": -2.25, "foreign_net_purchase_krw_trn": 3.1, "foreign_net_purchase_usd_bn": 2.13, "existing_treasury_share_grace_period_months": 6},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="policy_event_rerating",
        round_rerating_label="financial_holding_valueup_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="policy_and_market_rally_not_green",
        price_validation_status="reported_sector_anchor_not_full_ohlc",
        notes="Value-up policy and sector rally are Stage 2; ROE/CET1/credit cost and actual recurring shareholder return are required before Green.",
    ),
    Round262CaseCandidate(
        case_id="r6_loop12_securities_market_volume_cycle",
        symbol="securities_basket",
        company_name="Korean securities firms basket",
        primary_archetype=E2RArchetype.BROKERAGE_MARKET_VOLUME_CYCLE,
        secondary_archetypes=(E2RArchetype.SECURITIES_MARKET_VOLUME_CYCLE, E2RArchetype.SECURITIES_IB_PF_RISK_OVERLAY),
        case_type="cyclical_success",
        round_case_type="cyclical_success + 4B-watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 5, 6),
        stage3_date=None,
        stage4b_date=date(2026, 5, 6),
        stage4c_date=None,
        stage3_decision="market_volume_cycle_not_structural_green_before_brokerage_ib_revenue_and_roe",
        stage4b_status="4B-watch securities +13.5% before revenue proof",
        hard_4c_confirmed=False,
        evidence_fields=("kospi_plus_6_45pct", "kospi_intraday_high_plus_7_06pct", "securities_firms_plus_13_5pct", "foreign_net_purchase_3_1tn_krw"),
        red_flag_fields=("market_volume_spike_only", "brokerage_ib_revenue_unconfirmed", "pf_ib_loss_risk", "tax_policy_risk"),
        price_data_source="Reuters KOSPI 7000 sector-return anchor",
        reported_price_anchor="Securities firms +13.5%, financial groups +4.2%, KOSPI +6.45%",
        reported_return_anchor="Securities relative outperformance vs KOSPI +7.05pp",
        mfe_1d=13.5,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kospi_event_return_pct": 6.45, "kospi_intraday_high_return_pct": 7.06, "securities_firms_event_mfe_pct": 13.5, "financial_groups_event_mfe_pct": 4.2, "securities_relative_outperformance_vs_kospi_pp": 7.05, "foreign_net_purchase_krw_trn": 3.1, "foreign_net_purchase_usd_bn": 2.13},
        score_price_alignment="unknown",
        round_alignment_label="cyclical_success",
        rerating_result="cyclical_rerating",
        round_rerating_label="brokerage_market_volume_cycle_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_cycle_not_green",
        price_validation_status="reported_sector_anchor_not_full_ohlc",
        notes="Securities +13.5% is cyclical success and 4B-watch until brokerage/IB revenue and ROE confirm.",
    ),
    Round262CaseCandidate(
        case_id="r6_loop12_samsung_life_nav_capital_release",
        symbol="032830",
        company_name="Samsung Life",
        primary_archetype=E2RArchetype.INSURANCE_NAV_CAPITAL_RELEASE,
        secondary_archetypes=(E2RArchetype.INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE, E2RArchetype.INSURANCE_KICS_CSM_GATE),
        case_type="success_candidate",
        round_case_type="success_candidate + regulatory_watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 3, 19),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="capital_release_not_green_until_use_of_proceeds_kics_csm_dividend_buyback_confirm",
        stage4b_status="NAV rally watch",
        hard_4c_confirmed=False,
        evidence_fields=("samsung_electronics_stake_sale_1_3tn_krw", "resolve_financial_company_governance_regulation_risk", "fx_rate_1499_3_krw_usd"),
        red_flag_fields=("use_of_proceeds_unconfirmed", "kics_csm_unconfirmed", "affiliate_price_drawdown_risk", "regulatory_sale_pressure"),
        price_data_source="Reuters regulatory share-sale anchor",
        reported_price_anchor="Samsung Electronics stake sale 1.3T KRW / $867.07M",
        reported_return_anchor="Capital release Stage 2; full Samsung Life OHLC unavailable",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_electronics_stake_sale_krw_trn": 1.3, "samsung_electronics_stake_sale_usd_mn": 867.07, "fx_rate_krw_per_usd": 1499.3},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_regulatory_watch",
        rerating_result="unknown",
        round_rerating_label="insurance_NAV_capital_release_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="capital_release_not_green_until_use_of_proceeds",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Capital release is Stage 2; K-ICS, CSM, dividend/buyback and use of proceeds are required before Green.",
    ),
    Round262CaseCandidate(
        case_id="r6_loop12_hana_bank_dunamu_equity_option",
        symbol="086790",
        company_name="Hana Financial / Hana Bank / Dunamu",
        primary_archetype=E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_OPTION,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION, E2RArchetype.EXCHANGE_SECURITY_OPERATIONAL_RISK),
        case_type="success_candidate",
        round_case_type="success_candidate / regulated digital-asset equity option",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 5, 14),
        stage3_date=None,
        stage4b_date=date(2026, 5, 14),
        stage4c_date=None,
        stage3_decision="digital_asset_equity_option_not_green_before_equity_method_regulated_revenue_capital_and_trust",
        stage4b_status="4B-watch if bank rerates before equity-method income",
        hard_4c_confirmed=False,
        evidence_fields=("hana_bank_acquires_6_55pct_dunamu_stake", "transaction_value_about_1tn_krw", "upbit_more_than_80pct_trading_volume_share", "blockchain_remittance_technical_verification_completed"),
        red_flag_fields=("equity_method_income_missing", "regulatory_approval_pending", "exchange_trust_risk", "crypto_volume_risk", "capital_impact_unconfirmed"),
        price_data_source="Reuters / WSJ transaction anchors",
        reported_price_anchor="Hana Bank acquires 6.55% Dunamu stake for about 1T KRW / $700M",
        reported_return_anchor="Implied Dunamu equity value about 15.27T KRW; full Hana price path unavailable",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"transaction_value_krw_trn": 1.0, "wsj_transaction_value_krw_trn": 1.003, "stake_acquired_pct": 6.55, "shares_acquired_mn": 2.284, "implied_dunamu_equity_value_krw_trn": 15.27, "upbit_trading_volume_share_pct_min": 80.0, "kakao_investment_remaining_stake_pct": 4.03, "expected_closing": "2026-06-15"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="bank_digital_asset_equity_option_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_equity_option_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Dunamu stake is Stage 2; regulated revenue, equity-method earnings, capital impact and exchange trust are required before Green.",
    ),
    Round262CaseCandidate(
        case_id="r6_loop12_naver_dunamu_platform_merger_trust_watch",
        symbol="035420",
        company_name="NAVER / NAVER Financial / Dunamu",
        primary_archetype=E2RArchetype.DIGITAL_ASSET_PLATFORM_MERGER_TRUST_WATCH,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_EXCHANGE_CONSOLIDATION, E2RArchetype.EXCHANGE_SECURITY_OPERATIONAL_RISK),
        case_type="success_candidate",
        round_case_type="success_candidate + event_premium + 4C-watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 11, 27),
        stage3_date=None,
        stage4b_date=date(2025, 11, 27),
        stage4c_date=date(2025, 11, 27),
        stage3_decision="platform_merger_stage2_but_exchange_abnormal_withdrawal_blocks_green_until_trust_recovers",
        stage4b_status="4B-watch deal rally plus exchange-trust 4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("naver_financial_acquires_dunamu", "deal_value_15_13tn_krw", "exchange_ratio_2_54", "upbit_market_share_70pct", "naver_initial_plus_7pct", "naver_later_minus_4_2pct", "abnormal_withdrawal_54bn_krw"),
        red_flag_fields=("exchange_abnormal_withdrawal_or_hack", "regulatory_approval_pending", "platform_trust_break_watch", "event_rally_before_regulated_revenue"),
        price_data_source="Reuters transaction / event-return / trust-risk anchor",
        reported_price_anchor="Deal value 15.13T KRW / $10.27B; NAVER initially +7% then -4.2%",
        reported_return_anchor="Event swing -11.2pp after 54B KRW abnormal withdrawal; Upbit to cover using own assets",
        mfe_1d=7.0,
        mae_1d=-4.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"deal_value_krw_trn": 15.13, "deal_value_usd_bn": 10.27, "exchange_ratio_naver_financial_per_dunamu": 2.54, "upbit_market_share_pct": 70.0, "event_initial_mfe_pct": 7.0, "event_later_mae_pct": -4.2, "event_swing_pp": -11.2, "abnormal_withdrawal_krw_bn": 54.0},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_trust_watch",
        rerating_result="event_premium",
        round_rerating_label="digital_asset_platform_merger_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="platform_stage2_with_exchange_trust_4C_watch",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Digital-asset platform Stage 2, but abnormal withdrawal creates exchange-trust 4C-watch.",
    ),
    Round262CaseCandidate(
        case_id="r6_loop12_toss_facepay_fintech_superapp_privacy_watch",
        symbol="unlisted_Toss/payment_fintech_readthrough",
        company_name="Toss / Viva Republica / FacePay",
        primary_archetype=E2RArchetype.FINTECH_SUPERAPP_BIOMETRIC_PAYMENT,
        secondary_archetypes=(E2RArchetype.PAYMENT_BIOMETRIC_INFRASTRUCTURE, E2RArchetype.PAYMENT_PRIVACY_REGULATORY_4C),
        case_type="success_candidate",
        round_case_type="success_candidate + privacy_watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 9, 9),
        stage3_date=None,
        stage4b_date=date(2026, 5, 1),
        stage4c_date=None,
        stage3_decision="unlisted_fintech_stage2_until_take_rate_credit_loss_nim_privacy_and_ipo_pricing_confirm",
        stage4b_status="4B-watch IPO/FacePay narrative before take-rate and credit-cost proof",
        hard_4c_confirmed=False,
        evidence_fields=("toss_more_than_30mn_users", "facepay_4_8mn_users", "facepay_330000_merchants", "facepay_target_10mn_users", "facepay_target_1mn_merchants", "us_ipo_q2_2026_target", "won_stablecoin_ambition"),
        red_flag_fields=("unlisted_company", "biometric_data_risk", "privacy_regulation_watch", "take_rate_unconfirmed", "credit_cost_unconfirmed", "ipo_pricing_unconfirmed"),
        price_data_source="Reuters global expansion / FT FacePay anchors",
        reported_price_anchor="Toss unlisted; FacePay 4.8M users and 330k merchants; IPO target >$10B",
        reported_return_anchor="User target requires +108.3%; merchant target requires +203.0%; no listed OHLC",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"toss_users_mn_min": 30.0, "facepay_users_mn": 4.8, "facepay_merchant_locations": 330000, "facepay_user_target_year_end_mn": 10.0, "facepay_merchant_target_year_end": 1000000, "user_target_growth_needed_pct": 108.3, "merchant_target_growth_needed_pct": 203.0, "ipo_valuation_target_usd_bn_min": 10.0, "ipo_valuation_possible_usd_bn": 15.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_unlisted",
        rerating_result="unknown",
        round_rerating_label="fintech_superapp_biometric_payment_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="unlisted_stage2_privacy_gate",
        price_validation_status="unlisted_no_ohlc",
        notes="Biometric payment is Stage 2; take-rate, credit cost, privacy/data compliance and IPO pricing are required.",
    ),
    Round262CaseCandidate(
        case_id="r6_loop12_kakao_kakaobank_governance_gate",
        symbol="035720/323410",
        company_name="Kakao / KakaoBank",
        primary_archetype=E2RArchetype.INTERNET_BANK_GOVERNANCE_4C,
        secondary_archetypes=(E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK, E2RArchetype.GOVERNANCE_EXECUTION_FAILURE_OVERLAY),
        case_type="4b_watch",
        round_case_type="4C-watch / governance gate",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 7, 22),
        stage3_decision="internet_bank_growth_is_blocked_by_major_shareholder_suitability_risk",
        stage4b_status="4C-watch governance gate",
        hard_4c_confirmed=False,
        evidence_fields=("kakao_founder_arrested", "kakao_minus_3_4pct", "kakao_group_value_86tn_krw", "kim_controlled_stake_24pct", "bank_ownership_suitability_risk"),
        red_flag_fields=("major_shareholder_legal_risk", "bank_ownership_suitability_failure_watch", "financial_crime_conviction_affecting_bank_control", "governance_legal_break"),
        price_data_source="Reuters Kakao founder arrest / bank ownership-risk anchors",
        reported_price_anchor="Kakao -3.4%; Kakao group value around 86T KRW; founder controls 24%",
        reported_return_anchor="Conviction risk could affect KakaoBank control due bank ownership restrictions",
        mfe_1d=None,
        mae_1d=-3.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kakao_event_mae_pct": -3.4, "kakao_group_value_krw_trn": 86.0, "kakao_group_value_usd_bn": 62.0, "kim_controlled_stake_pct": 24.0},
        score_price_alignment="unknown",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="internet_bank_governance_gate",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="governance_4C_watch",
        price_validation_status="kakaobank_ohlc_unavailable_after_deep_search",
        notes="KakaoBank Green is blocked by major-shareholder legal and bank-ownership suitability risk.",
    ),
    Round262CaseCandidate(
        case_id="r6_loop12_stablecoin_policy_overheat_fx_gate",
        symbol="377300/LG_CNS/Aton/ME2ON/KRW/banks",
        company_name="Stablecoin policy basket / FX gate",
        primary_archetype=E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE,
        secondary_archetypes=(E2RArchetype.KRW_STABLECOIN_POLICY_OVERHEAT, E2RArchetype.FX_LIQUIDITY_STABLECOIN_OUTFLOW),
        case_type="overheat",
        round_case_type="overheat + 4C-watch",
        stage1_date=date(2025, 6, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 6, 1),
        stage4c_date=date(2025, 6, 30),
        stage3_decision="stablecoin_policy_overheat_is_not_green_before_issuer_license_reserve_income_fee_revenue_and_fx_stability",
        stage4b_status="4B-watch plus macro FX 4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("kakao_pay_more_than_2x", "lg_cns_plus_70pct", "aton_plus_80pct", "me2on_3x", "margin_loans_20_5tn_krw", "stablecoin_trading_q1_57tn_krw", "capital_outflow_context_above_19bn_usd", "kimchi_bond_ban_lifted"),
        red_flag_fields=("stablecoin_policy_theme_only", "issuer_license_missing", "reserve_income_missing", "fee_revenue_missing", "stablecoin_driven_fx_outflow", "nonbank_stablecoin_fx_risk"),
        price_data_source="FT stablecoin / kimchi-bond / FX-risk anchors",
        reported_price_anchor="Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x before issuer economics",
        reported_return_anchor="Q1 stablecoin trading 57T KRW / $42B and capital outflow context >$19B",
        mfe_1d=200.0,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kakao_pay_mfe_pct_min": 100.0, "lg_cns_mfe_pct": 70.0, "aton_mfe_pct": 80.0, "me2on_mfe_pct": 200.0, "margin_loan_context_krw_trn": 20.5, "stablecoin_trading_q1_krw_trn": 57.0, "stablecoin_trading_q1_usd_bn": 42.0, "capital_outflow_context_usd_bn_min": 19.0, "proposed_minimum_equity_for_issuer_krw_mn": 500.0, "kimchi_bond_ban_duration_years": 14, "krw_strength_after_policy_per_usd": 1347, "krw_stabilization_level_per_usd": 1353},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence + FX_4C_watch",
        rerating_result="theme_overheat",
        round_rerating_label="stablecoin_policy_overheat",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4B_before_regulated_revenue",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Stablecoin policy rally happened before regulated revenue, while FX outflow risk remains 4C-watch.",
    ),
)


def round262_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND262_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND262_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round262 R6 Loop-12 financial/capital/digital price validation case. "
                "Calibration-only; not candidate-generation input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if any(token in field for token in ("roe", "cet1", "kics", "revenue", "fee", "capital", "trust", "income", "buyback", "dividend"))
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if any(token in field for token in ("rally", "plus", "mfe", "event", "theme", "stake", "stablecoin", "volume"))
            ),
            stage4c_evidence=tuple(
                field
                for field in (*candidate.red_flag_fields, *candidate.evidence_fields)
                if any(token in field for token in ("trust", "privacy", "fx", "ownership", "legal", "credit", "hack", "withdrawal", "deterioration", "failure"))
            ),
            must_have_fields=ROUND262_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4b_watch", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND262_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_roe_cet1_kics_credit_cost_digital_revenue_fx_or_stage_prices",
                "do_not_treat_low_pbr_valueup_volume_digital_asset_stablecoin_or_ipo_headline_as_green_alone",
                *ROUND262_GREEN_REQUIRED_FIELDS,
                *ROUND262_GREEN_FORBIDDEN_PATTERNS,
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


def round262_case_rows() -> tuple[dict[str, str], ...]:
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
        for candidate in ROUND262_CASE_CANDIDATES
    )


def round262_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND262_SCORE_ADJUSTMENTS)


def round262_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND262_SHADOW_WEIGHT_ROWS)


def round262_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND262_DEEP_SUB_ARCHETYPES)


def round262_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round262_price_validation": "true"} for field in ROUND262_PRICE_VALIDATION_FIELDS)


def round262_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round262_label": label, "canonical_archetype": canonical} for label, canonical in ROUND262_REQUIRED_TARGET_ALIASES.items())


def round262_summary() -> dict[str, int | bool | str]:
    cases = ROUND262_CASE_CANDIDATES
    return {
        "source_round": ROUND262_SOURCE_ROUND_PATH,
        "round_id": ROUND262_ROUND_ID,
        "large_sector": ROUND262_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for case in cases if case.case_type == "cyclical_success"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "watch_case_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "watch_4c_count": sum(1 for case in cases if case.stage4c_date is not None or "4C-watch" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "reported_price_anchor_count": sum(1 for case in cases if case.price_validation_status != "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND262_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND262_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND262_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round262_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND262_SOURCE_ROUND_PATH,
        "round_id": ROUND262_ROUND_ID,
        "large_sector": ROUND262_LARGE_SECTOR,
        "summary": round262_summary(),
        "target_aliases": dict(ROUND262_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND262_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND262_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND262_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND262_HARD_4C_GATES),
        "score_adjustments": list(round262_score_adjustment_rows()),
        "shadow_weights": list(round262_shadow_weight_rows()),
        "deep_sub_archetypes": list(round262_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND262_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round262_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_low_pbr_valueup_brokerage_volume_digital_asset_stablecoin_or_ipo_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round262_summary_markdown() -> str:
    summary = round262_summary()
    lines = [
        "# Round 262 R6 Loop 12 Financial Capital Digital Price Validation",
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
        f"- overheat: {summary['overheat_count']}",
        f"- watch_cases: {summary['watch_case_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND262_CASE_CANDIDATES:
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
            "- Financial value-up is Stage 2 until ROE, capital buffers, credit cost, and actual return execution confirm.",
            "- Securities are cyclical success when market volume jumps before brokerage and IB earnings proof.",
            "- Bank or platform digital-asset exposure must pass regulated revenue, equity-method income and trust gates.",
            "- Toss FacePay is unlisted Stage 2 with biometric privacy/data gates.",
            "- KakaoBank governance and stablecoin FX outflow are 4C-watch, not Green evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round262_green_gate_review_markdown() -> str:
    lines = [
        "# Round 262 R6 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R6 Stage 3-Green is not `low PBR`, `value-up`, `securities`, `digital asset`, `stablecoin`, or `IPO`. It requires ROE, capital buffers, credit cost, actual capital return, regulated digital revenue, platform trust, privacy control, FX stability, and price path after evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND262_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND262_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND262_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `low PBR bank` is Stage 1/2 attention; Green needs ROE, CET1 and real cancellation/dividend execution.",
            "- `Dunamu stake` is an option; Green needs equity-method income and exchange trust.",
            "- `stablecoin stocks doubled` is 4B-watch until issuer economics and FX stability are visible.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round262_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 262 R6 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND262_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND262_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | interpretation |", "|---|---|---|---|"])
    for case in ROUND262_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round262_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 262 R6 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, ROE, CET1, K-ICS, credit cost, digital revenue, FX stability, or trust resolution where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND262_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND262_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round262_r6_loop12_reports(
    output_directory: str | Path = ROUND262_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND262_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND262_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round262_case_records(), cases_path),
        "audit": _write_json(round262_audit_payload(), audit_path),
        "summary": output / "round262_r6_loop12_price_validation_summary.md",
        "case_matrix": output / "round262_r6_loop12_case_matrix.csv",
        "target_aliases": output / "round262_r6_loop12_target_aliases.csv",
        "score_adjustments": output / "round262_r6_loop12_score_adjustments.csv",
        "shadow_weights": output / "round262_r6_loop12_shadow_weights.csv",
        "deep_sub_archetypes": output / "round262_r6_loop12_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round262_r6_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round262_r6_loop12_green_gate_review.md",
        "price_validation_plan": output / "round262_r6_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round262_r6_loop12_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round262_summary_markdown(), encoding="utf-8")
    _write_csv(round262_case_rows(), paths["case_matrix"])
    _write_csv(round262_target_alias_rows(), paths["target_aliases"])
    _write_csv(round262_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round262_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round262_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round262_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round262_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round262_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round262_stage4b_4c_review_markdown(), encoding="utf-8")
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
