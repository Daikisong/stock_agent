"""Round-275 R6 Loop-13 financial/capital/digital price-validation pack.

This module converts ``docs/round/round_275.md`` into structured,
calibration-only records and reports. It intentionally leaves production
scoring, candidate generation, and StageClassifier thresholds unchanged.

Easy example: a bank basket can rerate on a value-up headline, but R6 Green
still needs CET1, ROE, NIM, credit-cost, RWA and real capital-return execution.
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


ROUND275_SOURCE_ROUND_PATH = "docs/round/round_275.md"
ROUND275_ANALYST_ROUND_ID = "round_203"
ROUND275_LARGE_SECTOR = Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL.value
ROUND275_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round275_r6_loop13_financial_capital_digital_price_validation"
ROUND275_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_loop13_round275.jsonl"
ROUND275_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round275_r6_loop13_financial_capital_digital_price_validation_audit.json"

ROUND275_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BANK_VALUE_UP_RERATING_STAGE2": E2RArchetype.BANK_VALUE_UP_RERATING_STAGE2.value,
    "HOLDCO_DISCOUNT_BUYBACK_CANCELLATION": E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_CANCELLATION.value,
    "INSURANCE_HOLDING_STAKE_REGULATORY_GATE": E2RArchetype.INSURANCE_HOLDING_STAKE_REGULATORY_GATE.value,
    "DIGITAL_ASSET_BANK_STAKE_STAGE2": E2RArchetype.DIGITAL_ASSET_BANK_STAKE_STAGE2.value,
    "FINTECH_CRYPTO_M_AND_A_TRUST_GATE": E2RArchetype.FINTECH_CRYPTO_M_AND_A_TRUST_GATE.value,
    "INTERNET_BANK_IPO_OVERHANG": E2RArchetype.INTERNET_BANK_IPO_OVERHANG.value,
    "STABLECOIN_POLICY_OVERHEAT_FX_GATE": E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE.value,
    "CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE": E2RArchetype.CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE.value,
    "SECURITIES_TRADING_VOLUME_EVENT_PREMIUM": E2RArchetype.SECURITIES_TRADING_VOLUME_EVENT_PREMIUM.value,
}

ROUND275_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "actual_buyback_cancellation_confirmed",
    "sustainable_dividend_payout_confirmed",
    "cet1_rbc_capital_buffer_stable",
    "credit_cost_control_confirmed",
    "nim_fee_income_stability_confirmed",
    "roe_improvement_confirmed",
    "regulatory_approval_clearance_confirmed",
    "digital_asset_trust_confirmed",
    "exchange_internal_control_confirmed",
    "fee_revenue_bridge_confirmed",
    "price_path_after_evidence",
)

ROUND275_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_valueup_headline_only",
    "sector_rally_without_bank_metrics",
    "IPO_valuation_without_credit_quality",
    "digital_asset_equity_stake_only",
    "stablecoin_theme_only",
    "exchange_trust_incident",
    "regulatory_capital_uncertainty",
    "data_or_internal_control_failure",
    "trading_volume_event_only",
)

ROUND275_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "securities_financials_plus_10pct_on_trading_volume_expectation",
    "stablecoin_basket_2x_to_3x_before_regulated_revenue",
    "dunamu_upbit_stake_rerating_before_bank_earnings_bridge",
    "ipo_valuation_5tn_without_credit_data",
    "holdco_discount_closes_before_repeated_buyback_execution",
    "insurance_stock_rerates_on_electronics_stake_before_insurance_earnings_bridge",
)

ROUND275_HARD_4C_GATES: tuple[str, ...] = (
    "bank_credit_cost_spike",
    "cet1_or_rbc_deterioration",
    "regulatory_rejection_of_mna_or_stake_investment",
    "crypto_exchange_abnormal_withdrawal_or_operational_error",
    "stablecoin_driven_fx_outflow",
    "data_breach_or_internal_control_failure",
    "ipo_cancellation_due_valuation_or_concentration_risk",
    "dividend_or_buyback_cancellation_reversal",
)

ROUND275_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "bank_quality_anchor",
    "capital_return_anchor",
    "digital_asset_trust_gate",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round275ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round275ShadowWeightRow:
    archetype: E2RArchetype
    capital_return_execution: int
    cet1_rbc_buffer: int
    roe_nim_credit_quality: int
    regulatory_clearance: int
    digital_asset_trust: int
    fee_revenue_bridge: int
    internal_control: int
    event_penalty: int
    stage4b_watch_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "capital_return_execution": _signed(self.capital_return_execution),
            "cet1_rbc_buffer": _signed(self.cet1_rbc_buffer),
            "roe_nim_credit_quality": _signed(self.roe_nim_credit_quality),
            "regulatory_clearance": _signed(self.regulatory_clearance),
            "digital_asset_trust": _signed(self.digital_asset_trust),
            "fee_revenue_bridge": _signed(self.fee_revenue_bridge),
            "internal_control": _signed(self.internal_control),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round275DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round275CaseCandidate:
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
    direct_listed_hard_4c_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    event_mfe_pct: float | None
    event_mae_pct: float | None
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


ROUND275_SCORE_ADJUSTMENTS: tuple[Round275ScoreAdjustment, ...] = (
    Round275ScoreAdjustment("actual_buyback_cancellation", 5, "raise", "Value-up은 취득보다 실제 소각과 반복성이 중요하다."),
    Round275ScoreAdjustment("sustainable_dividend_payout", 4, "raise", "배당은 CET1/RBC와 credit cost가 받쳐야 한다."),
    Round275ScoreAdjustment("CET1_RBC_capital_buffer", 5, "raise", "은행·보험 Green은 자본비율이 먼저다."),
    Round275ScoreAdjustment("NIM_fee_income_stability", 5, "raise", "금융 EPS는 NIM·수수료·credit cost로 닫혀야 한다."),
    Round275ScoreAdjustment("ROE_RWA_control", 5, "raise", "저PBR이 아니라 ROE와 RWA control이 rerating 근거다."),
    Round275ScoreAdjustment("regulatory_approval_clearance", 5, "raise", "지분투자와 M&A는 규제 승인 전에는 Stage 2다."),
    Round275ScoreAdjustment("digital_asset_trust", 5, "raise", "Upbit/Dunamu optionality는 exchange trust가 있어야 한다."),
    Round275ScoreAdjustment("exchange_internal_control", 5, "raise", "이상출금·오배분은 hard 4C reference다."),
    Round275ScoreAdjustment("policy_valueup_headline_only", -5, "lower", "정책 headline만으로 은행 Green 금지다."),
    Round275ScoreAdjustment("sector_rally_without_bank_metrics", -5, "lower", "섹터 랠리는 ROE/CET1/NIM 확인 전엔 4B-watch다."),
    Round275ScoreAdjustment("IPO_valuation_without_credit_quality", -5, "lower", "인터넷은행 IPO는 credit/NIM/예금집중 확인 전엔 event premium이다."),
    Round275ScoreAdjustment("digital_asset_equity_stake_only", -5, "lower", "Dunamu 지분만으로 은행 EPS를 만들지 않는다."),
    Round275ScoreAdjustment("stablecoin_theme_only", -5, "lower", "스테이블코인 정책 테마는 발행·준비금·수수료 전에는 과열이다."),
    Round275ScoreAdjustment("exchange_trust_incident", -5, "lower", "거래소 신뢰 사고는 Green을 막는 RedTeam gate다."),
    Round275ScoreAdjustment("trading_volume_event_only", -4, "lower", "증권주는 거래대금 이벤트만으로 구조적 Green 금지다."),
)


ROUND275_SHADOW_WEIGHT_ROWS: tuple[Round275ShadowWeightRow, ...] = (
    Round275ShadowWeightRow(E2RArchetype.BANK_VALUE_UP_RERATING_STAGE2, 5, 5, 5, 3, 0, 3, 2, -5, 4, 5, "Bank value-up is Stage 2 until CET1, ROE, NIM, credit cost and RWA confirm."),
    Round275ShadowWeightRow(E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_CANCELLATION, 5, 2, 2, 3, 0, 2, 2, -3, 4, 4, "Holdco discount needs repeated cancellation and NAV bridge, not one buyback only."),
    Round275ShadowWeightRow(E2RArchetype.INSURANCE_HOLDING_STAKE_REGULATORY_GATE, 3, 5, 4, 5, 0, 2, 2, -3, 4, 5, "Insurance stake sale is Stage 2 until use of proceeds and capital buffer confirm."),
    Round275ShadowWeightRow(E2RArchetype.DIGITAL_ASSET_BANK_STAKE_STAGE2, 1, 4, 2, 5, 5, 4, 5, -5, 5, 5, "Dunamu stake is Stage 2 until regulated revenue, capital impact and trust confirm."),
    Round275ShadowWeightRow(E2RArchetype.FINTECH_CRYPTO_M_AND_A_TRUST_GATE, 0, 2, 2, 5, 5, 5, 5, -5, 5, 5, "Fintech-crypto M&A must clear closing, approval, trust and take-rate bridge."),
    Round275ShadowWeightRow(E2RArchetype.INTERNET_BANK_IPO_OVERHANG, 0, 5, 5, 3, 2, 4, 3, -5, 5, 5, "Internet-bank IPO is not Green before credit quality, NIM and deposit concentration."),
    Round275ShadowWeightRow(E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE, 0, 1, 0, 5, 4, 5, 4, -5, 5, 5, "Stablecoin basket is 4B/FX watch before licensed revenue and FX stability."),
    Round275ShadowWeightRow(E2RArchetype.CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE, 0, 0, 0, 5, 5, 0, 5, 0, 3, 5, "Exchange operational error is hard reference, not production Green evidence."),
    Round275ShadowWeightRow(E2RArchetype.SECURITIES_TRADING_VOLUME_EVENT_PREMIUM, 0, 2, 3, 2, 0, 5, 2, -4, 5, 4, "Trading-volume event premium needs recurring brokerage and IB revenue."),
)


ROUND275_DEEP_SUB_ARCHETYPES: tuple[Round275DeepSubArchetype, ...] = (
    Round275DeepSubArchetype("금융지주 value-up", E2RArchetype.BANK_VALUE_UP_RERATING_STAGE2, ("KB", "Shinhan", "Hana", "Woori", "CET1", "NIM", "credit cost", "RWA")),
    Round275DeepSubArchetype("지주사 discount", E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_CANCELLATION, ("SK Square", "SK Hynix stake", "buyback cancellation", "NAV discount", "Palliser")),
    Round275DeepSubArchetype("보험 보유지분 규제", E2RArchetype.INSURANCE_HOLDING_STAKE_REGULATORY_GATE, ("Samsung Life", "Samsung Electronics stake", "book-value discount", "RBC", "K-ICS")),
    Round275DeepSubArchetype("은행 디지털자산 지분", E2RArchetype.DIGITAL_ASSET_BANK_STAKE_STAGE2, ("Hana Bank", "Dunamu", "Upbit", "equity-method income", "capital impact")),
    Round275DeepSubArchetype("핀테크 crypto M&A", E2RArchetype.FINTECH_CRYPTO_M_AND_A_TRUST_GATE, ("NAVER Financial", "Dunamu", "Upbit", "abnormal withdrawal", "deal close")),
    Round275DeepSubArchetype("인터넷은행 IPO overhang", E2RArchetype.INTERNET_BANK_IPO_OVERHANG, ("K Bank", "IPO", "customers", "deposit concentration", "credit quality")),
    Round275DeepSubArchetype("Stablecoin / FX gate", E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE, ("Kakao Pay", "LG CNS", "Aton", "ME2ON", "issuer equity", "FX outflow")),
    Round275DeepSubArchetype("Crypto exchange hard reference", E2RArchetype.CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE, ("Bithumb", "erroneous distribution", "abnormal withdrawal", "regulator inspection")),
    Round275DeepSubArchetype("증권 거래대금 event premium", E2RArchetype.SECURITIES_TRADING_VOLUME_EVENT_PREMIUM, ("securities firms", "KOSPI 7000", "foreign net purchase", "brokerage fee")),
)


ROUND275_CASE_CANDIDATES: tuple[Round275CaseCandidate, ...] = (
    Round275CaseCandidate(
        case_id="r6_loop13_financial_holdings_valueup_sector_4b",
        symbol="105560/055550/086790/316140",
        company_name="KB / Shinhan / Hana / Woori financial holding basket",
        primary_archetype=E2RArchetype.BANK_VALUE_UP_RERATING_STAGE2,
        secondary_archetypes=(E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING, E2RArchetype.SECURITIES_TRADING_VOLUME_EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate + 4B-watch",
        stage1_date=date(2024, 2, 1),
        stage2_date=date(2024, 5, 2),
        stage3_date=None,
        stage4b_date=date(2026, 5, 6),
        stage4c_date=None,
        stage3_decision="valueup_policy_and_sector_rally_are_stage2_until_cet1_roe_nim_credit_cost_rwa_and_actual_return_confirm",
        stage4b_status="4B-watch/sector-rally-before-bank-quality-green",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("commercial_act_treasury_cancellation_rule_newly_acquired_shares_cancel_within_one_year", "kospi_7000_event_return_6_45pct", "securities_firms_event_return_13_5pct", "financial_groups_event_return_4_2pct", "foreign_net_purchase_3_1tn_krw"),
        red_flag_fields=("policy_valueup_headline_only", "sector_rally_without_bank_metrics", "actual_bank_cet1_credit_cost_nim_verified_false", "bank_quality_green_missing"),
        price_data_source="Reuters / analyst round value-up and KOSPI 7000 reported anchors",
        reported_price_anchor="Financial groups +4.2%, securities firms +13.5%, KOSPI +6.45%",
        reported_return_anchor="Foreign net purchase 3.1T KRW; bank-quality metrics not verified",
        event_mfe_pct=4.2,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"value_up_guideline_event_kospi_pct": -0.2, "commercial_act_treasury_cancellation_rule": "newly_acquired_treasury_shares_cancel_within_one_year", "kospi_7000_event_date": "2026-05-06", "kospi_event_mfe_pct": 6.45, "securities_firms_event_mfe_pct": 13.5, "financial_groups_event_mfe_pct": 4.2, "foreign_net_purchase_krw_trn": 3.1, "actual_bank_cet1_credit_cost_nim_verified": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4B_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="bank_value_up_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="policy_and_sector_rally_not_bank_quality_green",
        price_validation_status="reported_sector_anchor_not_full_ohlc",
        notes="Value-up and sector flow can be Layer 1/Stage 2, but not Green without bank-quality metrics.",
    ),
    Round275CaseCandidate(
        case_id="r6_loop13_sk_square_holdco_discount_buyback",
        symbol="402340",
        company_name="SK Square",
        primary_archetype=E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_CANCELLATION,
        secondary_archetypes=(E2RArchetype.HOLDING_NAV_DISCOUNT_VALUEUP, E2RArchetype.TREASURY_SHARE_CANCEL_EXECUTION),
        case_type="success_candidate",
        round_case_type="structural_success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 11, 21),
        stage3_date=None,
        stage4b_date=date(2024, 11, 21),
        stage4c_date=None,
        stage3_decision="buyback_cancellation_and_NAV_discount_are_stage2_until_repeated_execution_underlying_NAV_and_non_hynix_asset_clarity_confirm",
        stage4b_status="4B-watch/discount-closes-before-repeated-buyback",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("existing_buyback_cancel_100bn_krw", "new_buyback_100bn_krw", "total_buyback_cancel_200bn_krw", "sk_hynix_stake_20pct", "stake_value_18bn_usd", "palliser_activist_1pct"),
        red_flag_fields=("buyback_plan_not_recurring_yet", "NAV_discount_bridge_unconfirmed", "single_asset_hynix_dependency", "non_hynix_asset_clarity_missing"),
        price_data_source="Analyst round SK Square holdco-discount reported anchors",
        reported_price_anchor="SK Hynix stake value about $18B; SK Square market value less than half of that anchor",
        reported_return_anchor="Buyback/cancellation 200B KRW; full adjusted OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"existing_buyback_cancel_krw_bn": 100.0, "new_buyback_krw_bn": 100.0, "total_buyback_cancel_krw_bn": 200.0, "sk_hynix_stake_pct": 20.0, "stake_value_usd_bn": 18.0, "implied_mcap_upper_bound_usd_bn": 9.0, "discount_min_pct": 50.0, "palliser_stake_pct": 1.0, "independent_director": True},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="policy_event_rerating",
        round_rerating_label="holdco_discount_buyback_cancellation_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="buyback_plan_not_NAV_discount_green_until_executed_and_repeated",
        price_validation_status="reported_NAV_anchor_not_full_ohlc",
        notes="Buyback cancellation is stronger than headline value-up, but Green needs repeated execution and NAV durability.",
    ),
    Round275CaseCandidate(
        case_id="r6_loop13_samsung_life_samsung_electronics_stake_regulatory_gate",
        symbol="032830",
        company_name="Samsung Life Insurance",
        primary_archetype=E2RArchetype.INSURANCE_HOLDING_STAKE_REGULATORY_GATE,
        secondary_archetypes=(E2RArchetype.INSURANCE_NAV_CAPITAL_RELEASE, E2RArchetype.INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE),
        case_type="success_candidate",
        round_case_type="success_candidate + 4C-watch",
        stage1_date=date(2026, 3, 1),
        stage2_date=date(2026, 3, 19),
        stage3_date=None,
        stage4b_date=date(2026, 3, 19),
        stage4c_date=date(2026, 3, 19),
        stage3_decision="stake_sale_relief_is_stage2_until_use_of_proceeds_rbc_kics_csm_and_insurance_earnings_bridge_confirm",
        stage4b_status="4C-watch/regulatory-stake-sale-overhang",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("samsung_electronics_stake_sale_1_3tn_krw", "samsung_life_electronics_stake_about_10pct", "book_value_about_0_5x", "financial_company_governance_regulation_driver"),
        red_flag_fields=("regulatory_capital_uncertainty", "use_of_proceeds_false", "insurance_capital_return_bridge_false", "affiliate_stake_price_risk"),
        price_data_source="Analyst round Samsung Life regulatory stake-sale anchors",
        reported_price_anchor="Samsung Electronics stake sale 1.3T KRW / 867.07M USD",
        reported_return_anchor="Book value about 0.5x; insurance earnings bridge not confirmed",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stake_sale_krw_trn": 1.3, "stake_sale_usd_mn": 867.07, "samsung_life_samsung_electronics_stake_pct_context": 10.0, "book_value_multiple_about": 0.5, "regulatory_driver": "financial_company_governance_risk", "use_of_proceeds_confirmed": False, "insurance_capital_return_bridge_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4C_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="insurance_holdco_value_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stake_value_not_insurance_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Affiliate stake value can be Stage 2, but regulation and use-of-proceeds uncertainty stay visible.",
    ),
    Round275CaseCandidate(
        case_id="r6_loop13_hana_bank_dunamu_digital_asset_stake",
        symbol="086790",
        company_name="Hana Financial Group / Hana Bank / Dunamu",
        primary_archetype=E2RArchetype.DIGITAL_ASSET_BANK_STAKE_STAGE2,
        secondary_archetypes=(E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_OPTION, E2RArchetype.EXCHANGE_SECURITY_OPERATIONAL_RISK),
        case_type="success_candidate",
        round_case_type="success_candidate + 4B-watch",
        stage1_date=date(2026, 5, 14),
        stage2_date=date(2026, 5, 14),
        stage3_date=None,
        stage4b_date=date(2026, 5, 14),
        stage4c_date=None,
        stage3_decision="dunamu_stake_is_stage2_until_equity_method_income_regulatory_capital_exchange_trust_and_stablecoin_framework_confirm",
        stage4b_status="4B-watch/stake-rerating-before-bank-earnings-bridge",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("hana_bank_dunamu_stake_6_55pct", "purchase_1_003tn_krw", "implied_dunamu_equity_15_31tn_krw", "upbit_trading_share_80pct", "remittance_verification_completed"),
        red_flag_fields=("digital_asset_equity_stake_only", "regulatory_bridge_false", "equity_method_income_missing", "exchange_trust_risk", "capital_impact_unconfirmed"),
        price_data_source="Analyst round Hana/Dunamu transaction anchors",
        reported_price_anchor="Hana Bank buys 6.55% Dunamu stake for about 1.003T KRW",
        reported_return_anchor="Implied Dunamu equity 15.31T KRW; regulatory bridge not confirmed",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stake_acquired_pct": 6.55, "purchase_krw_trn": 1.003, "purchase_usd_mn": 672.5, "implied_dunamu_equity_value_krw_trn": 15.31, "seller": "Kakao affiliate", "shareholder_rank_after_purchase": 4, "upbit_trading_share_pct": 80.0, "remittance_verification_completed": True, "regulatory_bridge_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4B_watch",
        rerating_result="unknown",
        round_rerating_label="bank_digital_asset_stake_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="equity_stake_not_bank_EPS_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Dunamu stake can be an option, but bank EPS/FCF needs regulated revenue, capital and trust gates.",
    ),
    Round275CaseCandidate(
        case_id="r6_loop13_naver_dunamu_fintech_ma_trust_gate",
        symbol="035420",
        company_name="Naver Financial / Dunamu / Upbit",
        primary_archetype=E2RArchetype.FINTECH_CRYPTO_M_AND_A_TRUST_GATE,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE, E2RArchetype.EXCHANGE_SECURITY_OPERATIONAL_RISK),
        case_type="success_candidate",
        round_case_type="success_candidate + event_premium + 4C-watch",
        stage1_date=date(2025, 11, 27),
        stage2_date=date(2025, 11, 27),
        stage3_date=None,
        stage4b_date=date(2025, 11, 27),
        stage4c_date=date(2025, 11, 27),
        stage3_decision="fintech_crypto_mna_is_stage2_until_deal_closes_regulatory_approval_trust_recovery_and_take_rate_earnings_bridge_confirm",
        stage4b_status="4B-watch/event-premium-plus-exchange-trust-4C-watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("deal_value_15_13tn_krw", "exchange_ratio_2_54", "upbit_market_share_70pct", "naver_initial_mfe_7pct", "naver_later_mae_minus_4_2pct", "abnormal_withdrawal_54bn_krw"),
        red_flag_fields=("exchange_trust_incident", "abnormal_withdrawal_54bn_krw", "regulatory_approval_pending", "event_rally_before_regulated_revenue", "closing_not_confirmed"),
        price_data_source="Reuters transaction and event-return anchors",
        reported_price_anchor="Deal value 15.13T KRW / $10.27B; NAVER initially +7% then -4.2%",
        reported_return_anchor="Event swing -11.2pp after abnormal withdrawal; Upbit to cover using own assets",
        event_mfe_pct=7.0,
        event_mae_pct=-4.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"deal_value_krw_trn": 15.13, "deal_value_usd_bn": 10.27, "exchange_ratio": 2.54, "upbit_market_share_pct": 70.0, "initial_mfe_pct": 7.0, "later_mae_pct": -4.2, "event_swing_pp": -11.2, "abnormal_withdrawal_krw_bn": 54.0, "upbit_cover_with_own_assets": True, "closing_regulatory_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_trust_watch",
        rerating_result="event_premium",
        round_rerating_label="fintech_crypto_mna_stage2_trust_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="trust_watch_blocks_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="M&A premium is not Green while abnormal withdrawal and closing/regulatory gates remain unresolved.",
    ),
    Round275CaseCandidate(
        case_id="r6_loop13_kbank_internet_bank_ipo_overhang",
        symbol="unlisted_KBank_IPO_candidate",
        company_name="K Bank",
        primary_archetype=E2RArchetype.INTERNET_BANK_IPO_OVERHANG,
        secondary_archetypes=(E2RArchetype.INTERNET_BANK_IPO_PROFITABILITY, E2RArchetype.INTERNET_BANK_GOVERNANCE_4C),
        case_type="event_premium",
        round_case_type="event_premium_insufficient_evidence",
        stage1_date=date(2024, 9, 10),
        stage2_date=date(2024, 9, 10),
        stage3_date=None,
        stage4b_date=date(2024, 9, 10),
        stage4c_date=None,
        stage3_decision="internet_bank_IPO_is_event_premium_until_credit_quality_nim_deposit_concentration_capital_and_listed_price_path_confirm",
        stage4b_status="4B-watch/ipo-valuation-without-credit-data",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("raise_max_984bn_krw", "max_valuation_5tn_krw", "customers_10mn", "h1_2024_operating_profit_86_7bn_krw", "new_and_existing_shares_each_41mn"),
        red_flag_fields=("IPO_valuation_without_credit_quality", "deposit_concentration_unconfirmed", "credit_NIM_deposit_false", "listed_price_path_missing", "existing_share_overhang"),
        price_data_source="Analyst round K Bank IPO anchors",
        reported_price_anchor="Price range 9,500-12,000 KRW; max valuation 5T KRW",
        reported_return_anchor="Raise max 984B KRW; no listed price path before listing",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"raise_max_krw_bn": 984.0, "raise_max_usd_mn": 731.64, "shares_total_mn": 82.0, "new_shares_mn": 41.0, "existing_shares_mn": 41.0, "price_range_low_krw": 9500.0, "price_range_high_krw": 12000.0, "max_valuation_krw_trn": 5.0, "raise_to_valuation_pct": 19.68, "h1_2024_operating_profit_krw_bn": 86.7, "operating_profit_yoy_multiple_min": 3.0, "customers_mn": 10.0, "listing_date": "2024-10-30", "credit_nim_deposit_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="event_premium_insufficient_evidence",
        rerating_result="event_premium",
        round_rerating_label="internet_bank_IPO_overhang",
        stage_failure_type="false_yellow",
        round_stage_failure_label="IPO_valuation_not_credit_quality_green",
        price_validation_status="unlisted_pre_IPO_no_ohlc",
        notes="Customer count and IPO valuation are not enough; credit quality, NIM and deposit concentration decide bank quality.",
    ),
    Round275CaseCandidate(
        case_id="r6_loop13_stablecoin_policy_overheat_fx_gate",
        symbol="KakaoPay/LG_CNS/Aton/ME2ON",
        company_name="Stablecoin policy basket",
        primary_archetype=E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE,
        secondary_archetypes=(E2RArchetype.KRW_STABLECOIN_POLICY_OVERHEAT, E2RArchetype.STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION),
        case_type="overheat",
        round_case_type="overheat + 4C-watch",
        stage1_date=date(2025, 6, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 6, 1),
        stage4c_date=date(2025, 6, 1),
        stage3_decision="stablecoin_policy_theme_is_not_green_before_issuer_license_reserve_income_fee_revenue_and_fx_gate_clear",
        stage4b_status="4B-watch/2x-to-3x-before-regulated-revenue-plus-FX-watch",
        hard_4c_confirmed=False,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("kakao_pay_plus_100pct", "lg_cns_plus_70pct", "aton_plus_80pct", "me2on_plus_200pct", "margin_loans_20_5tn_krw", "proposed_issuer_equity_500mn_krw"),
        red_flag_fields=("stablecoin_theme_only", "issuer_license_missing", "reserve_income_missing", "fee_revenue_missing", "stablecoin_driven_fx_outflow", "bok_fx_concern"),
        price_data_source="Analyst round stablecoin basket reported anchors",
        reported_price_anchor="Kakao Pay +100%, LG CNS +70%, Aton +80%, ME2ON +200%",
        reported_return_anchor="Won weakness quarter 4%; issuer/license/reserve/fee not confirmed",
        event_mfe_pct=200.0,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kakao_pay_mfe_pct": 100.0, "lg_cns_mfe_pct": 70.0, "aton_mfe_pct": 80.0, "me2on_mfe_pct": 200.0, "margin_loans_krw_trn": 20.5, "proposed_issuer_equity_krw_mn": 500.0, "won_weakness_quarter_pct": 4.0, "issuer_license_reserve_fee_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="price_moved_without_evidence_FX_watch",
        rerating_result="theme_overheat",
        round_rerating_label="stablecoin_policy_overheat",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="policy_theme_not_regulated_revenue",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Stablecoin basket is 4B/FX watch until issuer economics and FX stability are visible.",
    ),
    Round275CaseCandidate(
        case_id="r6_loop13_bithumb_operational_error_hard_reference",
        symbol="unlisted_Bithumb/crypto_exchange_reference",
        company_name="Bithumb",
        primary_archetype=E2RArchetype.CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE,
        secondary_archetypes=(E2RArchetype.EXCHANGE_SECURITY_OPERATIONAL_RISK, E2RArchetype.FINTECH_CRYPTO_M_AND_A_TRUST_GATE),
        case_type="4c_thesis_break",
        round_case_type="hard_4C_reference",
        stage1_date=date(2026, 2, 6),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2026, 2, 7),
        stage3_decision="crypto_exchange_operational_error_is_hard_reference_not_green_source_even_if_most_assets_recovered",
        stage4b_status="hard-4C-reference/not-direct-listed",
        hard_4c_confirmed=True,
        direct_listed_hard_4c_confirmed=False,
        evidence_fields=("erroneous_distribution_44bn_usd", "erroneous_btc_total_620000", "affected_customers_695", "recovered_share_99_7pct", "restriction_35min", "regulator_inspection_true"),
        red_flag_fields=("crypto_exchange_abnormal_withdrawal_or_operational_error", "data_or_internal_control_failure", "exchange_trust_incident", "customer_asset_restriction", "regulator_inspection"),
        price_data_source="Analyst round Bithumb operational-error reported anchors",
        reported_price_anchor="Erroneous distribution $44B / 620,000 BTC; 99.7% recovered",
        reported_return_anchor="Bithumb BTC -17% on exchange; regulator inspection",
        event_mfe_pct=None,
        event_mae_pct=-17.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"erroneous_distribution_usd_bn": 44.0, "erroneous_btc_total": 620000.0, "affected_customers": 695, "btc_per_user_min": 2000.0, "recovered_share_pct": 99.7, "restriction_minutes": 35, "bithumb_btc_mae_pct": -17.0, "btc_low_krw_mn": 81.1, "btc_recovered_price_krw_mn": 104.5, "external_hack": False, "regulator_inspection": True},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_reference",
        rerating_result="thesis_break",
        round_rerating_label="crypto_exchange_operational_hard_reference",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C_reference_not_direct_listed",
        price_validation_status="unlisted_hard_reference_reported_anchor",
        notes="Operational control failure is a hard reference. It must feed RedTeam, not create digital-finance Green.",
    ),
)


def round275_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND275_CASE_CANDIDATES:
        stage3_terms = ("roe", "cet1", "nim", "credit", "fee", "capital", "trust", "buyback", "dividend", "rwa")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND275_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round275 R6 Loop-13 financial/capital/digital price validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(token in field.lower() for token in stage3_terms)),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if any(token in field.lower() for token in ("rally", "plus", "mfe", "event", "theme", "stake", "ipo", "stablecoin", "volume", "4b"))
            ),
            stage4c_evidence=tuple(
                field
                for field in (*candidate.red_flag_fields, *candidate.evidence_fields)
                if any(token in field.lower() for token in ("trust", "fx", "credit", "regulatory", "operational", "control", "withdrawal", "deterioration", "failure", "ipo_cancellation"))
            ),
            must_have_fields=ROUND275_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND275_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "do_not_use_round275_cases_as_candidate_generation_input",
                "do_not_treat_valueup_stake_ipo_stablecoin_or_volume_headline_as_green_alone",
                *ROUND275_GREEN_REQUIRED_FIELDS,
                *ROUND275_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.event_mfe_pct,
                mae_30d=candidate.event_mae_pct,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.event_mfe_pct is not None
                    or candidate.event_mae_pct is not None
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


def round275_case_rows() -> tuple[dict[str, str], ...]:
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
            "direct_listed_hard_4c_confirmed": str(candidate.direct_listed_hard_4c_confirmed).lower(),
            "price_data_source": candidate.price_data_source,
            "reported_price_anchor": candidate.reported_price_anchor,
            "reported_return_anchor": candidate.reported_return_anchor,
            "event_mfe_pct": _float_text(candidate.event_mfe_pct),
            "event_mae_pct": _float_text(candidate.event_mae_pct),
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
        for candidate in ROUND275_CASE_CANDIDATES
    )


def round275_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND275_SCORE_ADJUSTMENTS)


def round275_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND275_SHADOW_WEIGHT_ROWS)


def round275_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND275_DEEP_SUB_ARCHETYPES)


def round275_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round275_price_validation": "true"} for field in ROUND275_PRICE_VALIDATION_FIELDS)


def round275_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round275_label": label, "canonical_archetype": canonical} for label, canonical in ROUND275_REQUIRED_TARGET_ALIASES.items())


def round275_summary() -> dict[str, int | bool | str]:
    cases = ROUND275_CASE_CANDIDATES
    return {
        "source_round": ROUND275_SOURCE_ROUND_PATH,
        "round_id": ROUND275_ANALYST_ROUND_ID,
        "large_sector": ROUND275_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "direct_listed_hard_4c_case_count": sum(1 for case in cases if case.direct_listed_hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND275_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND275_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND275_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
        "direct_listed_hard_4c_confirmed": any(case.direct_listed_hard_4c_confirmed for case in cases),
    }


def round275_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND275_SOURCE_ROUND_PATH,
        "round_id": ROUND275_ANALYST_ROUND_ID,
        "large_sector": ROUND275_LARGE_SECTOR,
        "summary": round275_summary(),
        "target_aliases": dict(ROUND275_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND275_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND275_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND275_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND275_HARD_4C_GATES),
        "score_adjustments": list(round275_score_adjustment_rows()),
        "shadow_weights": list(round275_shadow_weight_rows()),
        "deep_sub_archetypes": list(round275_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND275_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round275_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_valueup_holdco_stake_ipo_stablecoin_volume_or_exchange_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round275_summary_markdown() -> str:
    summary = round275_summary()
    lines = [
        "# Round 275 R6 Loop 13 Financial Capital Digital Price Validation",
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
        f"- event_premium: {summary['event_premium_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- direct_listed_hard_4c: {str(summary['direct_listed_hard_4c_confirmed']).lower()}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND275_CASE_CANDIDATES:
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
            "- Financial value-up is Stage 2 until CET1, ROE, NIM, credit cost, RWA and real capital return confirm.",
            "- Holdco and insurance stake rerating need repeated execution, use of proceeds and capital buffer evidence.",
            "- Digital-asset stakes and M&A must pass regulatory, earnings, exchange-trust and internal-control gates.",
            "- Stablecoin and securities-volume baskets are 4B/event premium until regulated revenue or recurring fee evidence appears.",
            "- Bithumb is a hard 4C reference, but not a direct listed-company hard 4C case.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round275_green_gate_review_markdown() -> str:
    lines = [
        "# Round 275 R6 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R6 Stage 3-Green is not `value-up`, `buyback`, `financial holding`, `Dunamu stake`, `internet-bank IPO`, `stablecoin policy`, or `trading volume`. It requires actual payout execution, capital buffer, bank-quality earnings, regulatory clearance, trust, internal controls, and price path after evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND275_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND275_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND275_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `KB value-up headline` is Stage 2 attention; Green needs CET1, ROE, NIM and credit cost.",
            "- `Hana buys Dunamu stake` is an option; Green needs equity-method income, capital impact and exchange trust.",
            "- `stablecoin basket doubles` is 4B-watch until issuer economics and FX stability are visible.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round275_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 275 R6 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND275_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND275_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | direct listed hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND275_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {str(case.direct_listed_hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def render_round275_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 275 R6 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, CET1, RBC, ROE, NIM, credit cost, RWA, exchange trust, fee revenue or regulatory clearance where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND275_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND275_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round275_r6_loop13_reports(
    output_directory: str | Path = ROUND275_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND275_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND275_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round275_case_records(), cases_path),
        "audit": _write_json(round275_audit_payload(), audit_path),
        "summary": output / "round275_r6_loop13_price_validation_summary.md",
        "case_matrix": output / "round275_r6_loop13_case_matrix.csv",
        "target_aliases": output / "round275_r6_loop13_target_aliases.csv",
        "score_adjustments": output / "round275_r6_loop13_score_adjustments.csv",
        "shadow_weights": output / "round275_r6_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round275_r6_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round275_r6_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round275_r6_loop13_green_gate_review.md",
        "price_validation_plan": output / "round275_r6_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round275_r6_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round275_summary_markdown(), encoding="utf-8")
    _write_csv(round275_case_rows(), paths["case_matrix"])
    _write_csv(round275_target_alias_rows(), paths["target_aliases"])
    _write_csv(round275_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round275_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round275_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round275_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round275_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round275_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round275_stage4b_4c_review_markdown(), encoding="utf-8")
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
