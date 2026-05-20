"""Round-288 R6 Loop-14 finance/capital/digital price-validation pack.

This module converts ``docs/round/round_288.md`` into structured,
calibration-only records and reports. It intentionally leaves production
scoring, candidate generation, and StageClassifier thresholds unchanged.

Easy example: a Value-Up law can move bank stocks, but R6 Green still needs
CET1, actual payout/cancellation, credit-cost control, and ROE/PBR evidence.
Likewise, a crypto M&A headline is Stage 2 until custody, AML/KYC, regulatory
approval, and revenue contribution are verified.
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


ROUND288_SOURCE_ROUND_PATH = "docs/round/round_288.md"
ROUND288_ANALYST_ROUND_ID = "round_216"
ROUND288_LARGE_SECTOR = "FINANCE_CAPITAL_ALLOCATION_DIGITAL_FINANCE"
ROUND288_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round288_r6_loop14_financial_capital_digital_price_validation"
ROUND288_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_loop14_round288.jsonl"
ROUND288_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round288_r6_loop14_financial_capital_digital_price_validation_audit.json"

ROUND288_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "VALUE_UP_FINANCIAL_HOLDING_STAGE2": E2RArchetype.VALUE_UP_FINANCIAL_HOLDING_STAGE2.value,
    "HOLDCO_DISCOUNT_BUYBACK_STAGE2": E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_STAGE2.value,
    "SHAREHOLDER_RETURN_FAILURE_FALSE_POSITIVE": E2RArchetype.SHAREHOLDER_RETURN_FAILURE_FALSE_POSITIVE.value,
    "DIGITAL_BANK_IPO_QUALITY_GATE": E2RArchetype.DIGITAL_BANK_IPO_QUALITY_GATE.value,
    "DIGITAL_BANK_CONTROL_RISK_4C_WATCH": E2RArchetype.DIGITAL_BANK_CONTROL_RISK_4C_WATCH.value,
    "DIGITAL_ASSET_MA_TRUST_4C_WATCH": E2RArchetype.DIGITAL_ASSET_MA_TRUST_4C_WATCH.value,
    "BANK_DIGITAL_ASSET_STAKE_STAGE2": E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2.value,
    "PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM": E2RArchetype.PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM.value,
}

ROUND288_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "cet1_capital_buffer_confirmed",
    "actual_payout_execution_confirmed",
    "treasury_share_cancellation_confirmed",
    "credit_cost_control_confirmed",
    "holdco_discount_compression_confirmed",
    "ipo_aftermarket_demand_confirmed",
    "digital_asset_custody_control_confirmed",
    "aml_kyc_regulatory_clearance_confirmed",
    "cb_dilution_adjusted_roic_confirmed",
    "minority_shareholder_alignment_confirmed",
    "price_path_after_evidence",
)

ROUND288_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "Value_Up_headline_only",
    "shareholder_return_proposal_only",
    "announced_buyback_without_cancellation",
    "IPO_size_or_customer_count_only",
    "crypto_exchange_market_share_only",
    "M&A_synergy_without_custody_control",
    "CB_or_PE_investment_headline_only",
    "stablecoin_keyword_without_revenue",
    "founder_legal_risk_unresolved",
)

ROUND288_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "Value_Up_law_or_policy_pre_pricing",
    "buyback_announcement_before_cancellation",
    "activist_proposal_rally_before_vote",
    "digital_asset_MA_plus_5_to_10pct",
    "PE_CB_investment_plus_15_to_20pct",
    "stablecoin_or_crypto_keyword_before_revenue",
    "IPO_valuation_on_MAU_or_customers_only",
)

ROUND288_HARD_4C_GATES: tuple[str, ...] = (
    "bank_ownership_loss_due_founder_financial_crime_conviction",
    "abnormal_withdrawal_or_custody_failure",
    "aml_kyc_or_regulatory_rejection",
    "shareholder_return_proposal_failure_after_valueup_rally",
    "cb_dilution_without_clear_roic",
    "credit_cost_spike_or_pf_deterioration",
    "cet1_buffer_below_payout_requirement",
    "weak_ipo_debut_after_aggressive_pricing",
)

ROUND288_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "reported_event_price_anchor",
    "deal_value_anchor",
    "buyback_amount_anchor",
    "ipo_range_anchor",
    "cb_value_anchor",
    "stake_percent_anchor",
    "regulatory_restriction_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round288ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round288ShadowWeightRow:
    archetype: E2RArchetype
    cet1_capital_buffer: int
    actual_payout_execution: int
    treasury_share_cancellation: int
    credit_cost_control: int
    holdco_discount_compression: int
    ipo_aftermarket_demand: int
    digital_asset_custody_control: int
    aml_kyc_regulatory_clearance: int
    cb_dilution_adjusted_roic: int
    minority_shareholder_alignment: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "cet1_capital_buffer": _signed(self.cet1_capital_buffer),
            "actual_payout_execution": _signed(self.actual_payout_execution),
            "treasury_share_cancellation": _signed(self.treasury_share_cancellation),
            "credit_cost_control": _signed(self.credit_cost_control),
            "holdco_discount_compression": _signed(self.holdco_discount_compression),
            "ipo_aftermarket_demand": _signed(self.ipo_aftermarket_demand),
            "digital_asset_custody_control": _signed(self.digital_asset_custody_control),
            "aml_kyc_regulatory_clearance": _signed(self.aml_kyc_regulatory_clearance),
            "cb_dilution_adjusted_roic": _signed(self.cb_dilution_adjusted_roic),
            "minority_shareholder_alignment": _signed(self.minority_shareholder_alignment),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round288DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round288CaseCandidate:
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
    event_mfe_pct: float | None
    event_mae_pct: float | None
    stage1_price_anchor: float | None
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


ROUND288_SCORE_ADJUSTMENTS: tuple[Round288ScoreAdjustment, ...] = (
    Round288ScoreAdjustment("CET1_capital_buffer", 5, "raise", "금융지주 Green은 자본비율이 배당·소각을 버틸 때만 가능하다."),
    Round288ScoreAdjustment("actual_payout_execution", 5, "raise", "배당·자사주는 발표가 아니라 실제 집행이 증거다."),
    Round288ScoreAdjustment("treasury_share_cancellation", 5, "raise", "자사주 매입은 소각되어야 minority alignment로 연결된다."),
    Round288ScoreAdjustment("credit_cost_control", 5, "raise", "은행/금융지주 EPS는 대손비용이 흔들리면 바로 약해진다."),
    Round288ScoreAdjustment("holdco_discount_compression", 4, "raise", "지주 할인은 실제 discount compression이 확인되어야 한다."),
    Round288ScoreAdjustment("IPO_aftermarket_demand", 5, "raise", "IPO 규모와 고객수보다 상장 후 수요와 가격 검증이 중요하다."),
    Round288ScoreAdjustment("digital_asset_custody_control", 5, "raise", "디지털자산은 거래량보다 custody/internal control이 먼저다."),
    Round288ScoreAdjustment("AML_KYC_regulatory_clearance", 5, "raise", "가상자산/핀테크 수익화는 AML/KYC와 규제 승인 전엔 Stage 2다."),
    Round288ScoreAdjustment("CB_dilution_adjusted_ROIC", 5, "raise", "CB/PE 투자는 희석 조정 ROIC와 자금사용 성과로 닫혀야 한다."),
    Round288ScoreAdjustment("minority_shareholder_alignment", 5, "raise", "Value-Up은 소액주주 정렬이 실제로 개선될 때만 점수를 준다."),
    Round288ScoreAdjustment("Value_Up_headline_only", -5, "lower", "정책 headline은 Stage 2 신호이지 은행 Green 증거가 아니다."),
    Round288ScoreAdjustment("shareholder_return_proposal_only", -5, "lower", "주주제안은 통과·집행 전에는 자본환원이 아니다."),
    Round288ScoreAdjustment("announced_buyback_without_cancellation", -5, "lower", "소각 없는 매입 발표는 반복 환원으로 보지 않는다."),
    Round288ScoreAdjustment("IPO_size_or_customer_count_only", -5, "lower", "인터넷은행 고객수/IPO 규모만으로 bank-quality Green 금지다."),
    Round288ScoreAdjustment("crypto_exchange_market_share_only", -5, "lower", "거래소 점유율은 custody와 regulatory gate 전에는 수익가시성이 아니다."),
    Round288ScoreAdjustment("M&A_synergy_without_custody_control", -5, "lower", "디지털자산 M&A 시너지는 custody/internal control 전에는 event premium이다."),
    Round288ScoreAdjustment("CB_or_PE_investment_headline_only", -5, "lower", "PE/CB headline만 있고 ROIC·희석 조건이 없으면 4B-watch다."),
    Round288ScoreAdjustment("stablecoin_keyword_without_revenue", -5, "lower", "stablecoin 단어는 실제 수익모델 전에는 Green 증거가 아니다."),
    Round288ScoreAdjustment("founder_legal_risk_unresolved", -5, "lower", "은행 ownership에 영향을 주는 창업자 법적 리스크는 RedTeam gate다."),
)


ROUND288_SHADOW_WEIGHT_ROWS: tuple[Round288ShadowWeightRow, ...] = (
    Round288ShadowWeightRow(E2RArchetype.VALUE_UP_FINANCIAL_HOLDING_STAGE2, 5, 5, 5, 5, 2, 1, 0, 2, 1, 5, -5, 4, 4, "Financial holding Green needs CET1, actual payout/cancellation and credit-cost stability."),
    Round288ShadowWeightRow(E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_STAGE2, 1, 5, 5, 1, 5, 0, 0, 1, 2, 5, -4, 4, 3, "Holdco discount buyback is Stage 2 until discount compression and governance execution."),
    Round288ShadowWeightRow(E2RArchetype.SHAREHOLDER_RETURN_FAILURE_FALSE_POSITIVE, 1, 5, 5, 1, 3, 0, 0, 1, 1, 5, 0, 5, 4, "Samsung C&T shows proposal failure can create false positives."),
    Round288ShadowWeightRow(E2RArchetype.DIGITAL_BANK_IPO_QUALITY_GATE, 4, 1, 1, 5, 0, 5, 2, 5, 0, 3, -5, 5, 4, "K Bank IPO needs credit quality, funding cost, NIM and aftermarket demand."),
    Round288ShadowWeightRow(E2RArchetype.DIGITAL_BANK_CONTROL_RISK_4C_WATCH, 4, 2, 1, 4, 0, 2, 2, 5, 0, 5, 0, 4, 5, "KakaoBank control risk shows founder/legal gate for digital banks."),
    Round288ShadowWeightRow(E2RArchetype.DIGITAL_ASSET_MA_TRUST_4C_WATCH, 2, 1, 1, 2, 0, 2, 5, 5, 1, 4, -5, 5, 5, "Naver/Dunamu shows M&A premium can reverse on custody/internal-control risk."),
    Round288ShadowWeightRow(E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2, 4, 2, 1, 4, 0, 1, 5, 5, 2, 4, -5, 4, 5, "Hana/Dunamu stake needs custody, AML/KYC, capital treatment and revenue bridge."),
    Round288ShadowWeightRow(E2RArchetype.PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM, 1, 2, 1, 1, 1, 2, 4, 4, 5, 4, -5, 5, 4, "Samsung SDS/KKR CB needs dilution-adjusted ROIC and actual stablecoin/AI revenue."),
)


ROUND288_DEEP_SUB_ARCHETYPES: tuple[Round288DeepSubArchetype, ...] = (
    Round288DeepSubArchetype("Value-Up / financial holding", E2RArchetype.VALUE_UP_FINANCIAL_HOLDING_STAGE2, ("KB", "Shinhan", "Hana", "Woori", "Commercial Act", "treasury-share cancellation", "CET1", "credit cost")),
    Round288DeepSubArchetype("Holdco discount", E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_STAGE2, ("SK Square", "SK Hynix stake", "buyback", "cancellation", "activist", "discount compression")),
    Round288DeepSubArchetype("Shareholder return failure", E2RArchetype.SHAREHOLDER_RETURN_FAILURE_FALSE_POSITIVE, ("Samsung C&T", "activist proposal", "NPS vote", "minority shareholders", "proposal failure")),
    Round288DeepSubArchetype("Internet bank IPO", E2RArchetype.DIGITAL_BANK_IPO_QUALITY_GATE, ("K Bank", "IPO", "10M customers", "credit quality", "aftermarket demand", "NIM")),
    Round288DeepSubArchetype("Digital-bank governance", E2RArchetype.DIGITAL_BANK_CONTROL_RISK_4C_WATCH, ("KakaoBank", "Kakao founder", "bank ownership 10%", "financial crime", "acquittal relief")),
    Round288DeepSubArchetype("Digital asset M&A", E2RArchetype.DIGITAL_ASSET_MA_TRUST_4C_WATCH, ("Naver Financial", "Dunamu", "Upbit", "abnormal withdrawal", "custody", "AML/KYC")),
    Round288DeepSubArchetype("Bank digital-asset stake", E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2, ("Hana Bank", "Dunamu", "6.55%", "Upbit", "capital treatment", "custody")),
    Round288DeepSubArchetype("PE/CB/stablecoin", E2RArchetype.PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM, ("Samsung SDS", "KKR", "convertible bond", "AI infrastructure", "stablecoins", "dilution-adjusted ROIC")),
)


ROUND288_CASE_CANDIDATES: tuple[Round288CaseCandidate, ...] = (
    Round288CaseCandidate(
        case_id="r6_loop14_financial_holding_value_up_policy_stage2",
        symbol="105560/055550/086790/316140",
        company_name="KB / Shinhan / Hana / Woori financial holding basket",
        primary_archetype=E2RArchetype.VALUE_UP_FINANCIAL_HOLDING_STAGE2,
        secondary_archetypes=(E2RArchetype.BANK_VALUE_UP_RERATING_STAGE2, E2RArchetype.BANK_VALUEUP_ROE_PBR_RERATING),
        case_type="success_candidate",
        round_case_type="success_candidate_policy_stage2",
        stage1_date=date(2024, 2, 1),
        stage2_date=date(2026, 2, 25),
        stage3_date=None,
        stage4b_date=date(2026, 2, 25),
        stage4c_date=None,
        stage3_decision="policy_law_is_stage2_until_CET1_actual_payout_cancellation_credit_cost_and_ROE_PBR_close",
        stage4b_status="4B-watch/value-up-policy-before-bank-quality",
        hard_4c_confirmed=False,
        evidence_fields=("Commercial_Act_revision_passed", "new_treasury_share_cancellation_within_one_year", "existing_treasury_share_six_month_grace", "minority_shareholder_protection", "KOSPI_crossed_6000_context"),
        red_flag_fields=("Value_Up_headline_only", "credit_cost_control_unconfirmed", "CET1_buffer_unconfirmed", "actual_payout_execution_unconfirmed"),
        price_data_source="Reuters/FT Commercial Act and Value-Up reform anchors",
        reported_price_anchor="Financial holding direct event prices unavailable",
        reported_return_anchor="Treasury-share cancellation law anchor; KOSPI crossed 6000 in reform rally context",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"treasury_share_new_cancellation_deadline_years": 1, "existing_treasury_share_grace_period_months": 6, "kospi_reform_context": "KOSPI_crossed_6000", "stage3_conditions": ["CET1 buffer", "actual buyback cancellation", "payout ratio", "credit cost", "ROE/PBR rerating"]},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_policy_stage2",
        rerating_result="policy_event_rerating",
        round_rerating_label="financial_holding_value_up_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="policy_law_not_bank_ROE_payout_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Value-Up law is Stage 2; financial holding Green requires CET1, payout/cancellation execution and credit-cost stability.",
    ),
    Round288CaseCandidate(
        case_id="r6_loop14_sk_square_holdco_discount_buyback",
        symbol="402340",
        company_name="SK Square",
        primary_archetype=E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_STAGE2,
        secondary_archetypes=(E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_CANCELLATION, E2RArchetype.HOLDING_NAV_DISCOUNT_VALUEUP),
        case_type="success_candidate",
        round_case_type="success_candidate_but_price_data_unavailable",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 11, 21),
        stage3_date=None,
        stage4b_date=date(2024, 11, 21),
        stage4c_date=None,
        stage3_decision="buyback_cancellation_is_stage2_until_repeated_execution_discount_compression_and_governance_close",
        stage4b_status="4B-watch/holdco-discount-rerating-before-repeat-execution",
        hard_4c_confirmed=False,
        evidence_fields=("SK_Hynix_stake_value_visible", "buyback_cancellation_100bn_krw", "new_repurchase_and_cancel_100bn_krw", "independent_director_nomination", "activist_pressure"),
        red_flag_fields=("announced_buyback_without_cancellation", "holdco_discount_compression_unconfirmed", "single_asset_NAV_dependency"),
        price_data_source="Reuters SK Square buyback / activist / holdco discount anchor",
        reported_price_anchor="Direct event return unavailable",
        reported_return_anchor="200B KRW cancellation-related plan; 20% SK Hynix stake value context",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"first_cancellation_krw_bn": 100, "new_repurchase_and_cancellation_krw_bn": 100, "total_announced_cancellation_related_krw_bn": 200, "sk_hynix_stake_pct": 20, "sk_hynix_stake_value_usd_bn_context": 18, "market_value_less_than_half_stake_value": True, "activist_stake_context_pct": 1},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_price_data_unavailable",
        rerating_result="policy_event_rerating",
        round_rerating_label="holdco_discount_buyback_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="announced_buyback_not_discount_compression_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="SK Square is Stage 2: cancellation is useful, but holdco-discount compression and governance execution are the proof.",
    ),
    Round288CaseCandidate(
        case_id="r6_loop14_samsung_ct_activist_valueup_failure",
        symbol="028260",
        company_name="Samsung C&T",
        primary_archetype=E2RArchetype.SHAREHOLDER_RETURN_FAILURE_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.GOVERNANCE_EXECUTION_FAILURE_OVERLAY, E2RArchetype.VALUE_UP_CROWDED_4B_WATCH),
        case_type="failed_rerating",
        round_case_type="false_positive_score",
        stage1_date=date(2024, 3, 1),
        stage2_date=date(2024, 3, 1),
        stage3_date=None,
        stage4b_date=date(2024, 3, 15),
        stage4c_date=date(2024, 3, 15),
        stage3_decision="activist_pressure_is_not_green_without_board_adoption_payout_execution_and_cancellation",
        stage4b_status="4B-watch/value-up-expectation; 4C-watch/shareholder-return-proposal-failure",
        hard_4c_confirmed=False,
        evidence_fields=("activist_dividend_buyback_proposal", "Norway_oil_fund_and_Canadian_pension_support", "NPS_sided_with_management"),
        red_flag_fields=("shareholder_return_proposal_only", "proposal_passed_false", "minority_shareholder_alignment_failed", "shares_almost_minus_10pct"),
        price_data_source="FT activist proposal / share-price failure anchor",
        reported_price_anchor="Samsung C&T shares closed almost -10%",
        reported_return_anchor="Activist proposal failed; NPS sided with management",
        event_mfe_pct=None,
        event_mae_pct=-10.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_mae_pct": -10.0, "activist_backers": ["Norway oil fund", "Canadian pension investors"], "nps_vote": "sided_with_management", "proposal_passed": False, "proposal_type": ["dividend increase", "share buyback increase"]},
        score_price_alignment="false_positive_score",
        round_alignment_label="false_positive_score",
        rerating_result="thesis_break",
        round_rerating_label="shareholder_return_proposal_failed",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="activist_proposal_not_capital_return_execution",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Samsung C&T is the clean false-positive guardrail: proposal failure is not shareholder-return execution.",
    ),
    Round288CaseCandidate(
        case_id="r6_loop14_kbank_digital_bank_ipo_quality_gate",
        symbol="unlisted_KBank_readthrough",
        company_name="K Bank",
        primary_archetype=E2RArchetype.DIGITAL_BANK_IPO_QUALITY_GATE,
        secondary_archetypes=(E2RArchetype.INTERNET_BANK_IPO_OVERHANG, E2RArchetype.INTERNET_BANK_IPO_PROFITABILITY),
        case_type="success_candidate",
        round_case_type="success_candidate_IPO_quality_gate",
        stage1_date=date(2024, 9, 10),
        stage2_date=date(2024, 9, 10),
        stage3_date=None,
        stage4b_date=date(2024, 9, 10),
        stage4c_date=None,
        stage3_decision="IPO_size_and_customer_count_are_stage2_until_aftermarket_demand_NIM_credit_quality_and_CAC_close",
        stage4b_status="4B-watch/IPO-valuation-on-customers-before-credit-quality",
        hard_4c_confirmed=False,
        evidence_fields=("IPO_raise_up_to_984bn_krw", "price_range_9500_to_12000_krw", "valuation_up_to_5tn_krw", "H1_OP_86_7bn_krw", "10M_plus_customers"),
        red_flag_fields=("IPO_size_or_customer_count_only", "aftermarket_demand_unconfirmed", "credit_quality_unconfirmed", "deposit_funding_cost_unconfirmed"),
        price_data_source="Reuters K Bank IPO plan anchor",
        reported_price_anchor="Unlisted IPO plan; no aftermarket OHLC",
        reported_return_anchor="Raise up to 984B KRW; valuation up to 5T KRW; H1 OP 86.7B KRW; 10M+ customers",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_raise_max_krw_bn": 984, "ipo_raise_max_usd_mn": 731.64, "shares_to_sell_mn": 82, "new_shares_mn": 41, "existing_shares_mn": 41, "price_range_low_krw": 9500, "price_range_high_krw": 12000, "valuation_max_krw_trn": 5, "h1_2024_operating_profit_krw_bn": 86.7, "customer_count_context_mn": 10},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_IPO_quality_gate",
        rerating_result="event_premium",
        round_rerating_label="digital_bank_IPO_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="customer_count_and_IPO_size_not_aftermarket_NIM_green",
        price_validation_status="unlisted_ipo_plan_no_aftermarket_ohlc",
        notes="K Bank is Stage 2 until listed aftermarket demand, NIM, funding cost, credit quality and CAC are visible.",
    ),
    Round288CaseCandidate(
        case_id="r6_loop14_kakaobank_control_risk_kakao_founder",
        symbol="323410/035720",
        company_name="KakaoBank / Kakao",
        primary_archetype=E2RArchetype.DIGITAL_BANK_CONTROL_RISK_4C_WATCH,
        secondary_archetypes=(E2RArchetype.INTERNET_BANK_GOVERNANCE_4C, E2RArchetype.INTERNET_BANK_PROFITABILITY),
        case_type="failed_rerating",
        round_case_type="4C-watch_then_relief",
        stage1_date=date(2024, 7, 22),
        stage2_date=date(2025, 10, 21),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 7, 23),
        stage3_decision="digital_bank_growth_is_blocked_until_founder_legal_ownership_regulatory_clearance",
        stage4b_status="4C-watch/founder-control-risk; relief-after-acquittal",
        hard_4c_confirmed=False,
        evidence_fields=("founder_arrested_for_suspected_stock_manipulation", "bank_ownership_rule_risk", "later_acquittal_relief"),
        red_flag_fields=("founder_legal_risk_unresolved", "bank_ownership_loss_due_founder_financial_crime_conviction", "major_shareholder_suitability_risk"),
        price_data_source="Reuters Kakao founder arrest / KakaoBank control-risk anchors",
        reported_price_anchor="Kakao shares -3.4%; Kakao YTD -24% context",
        reported_return_anchor="Bank ownership above 10% could be restricted if financial-crime conviction occurred; later acquittal was relief",
        event_mfe_pct=None,
        event_mae_pct=-3.4,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kakao_event_mae_pct": -3.4, "kakao_ytd_decline_context_pct": -24, "founder_affiliated_stake_pct": 24, "bank_ownership_limit_if_financial_crime_conviction_pct": 10, "group_assets_krw_trn_context": 86, "prosecutor_sought_sentence_years": 15, "prosecutor_sought_fine_krw_mn": 500, "acquittal_relief": True},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch_then_relief",
        rerating_result="thesis_break",
        round_rerating_label="digital_bank_control_risk_gate",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="fintech_bank_growth_not_green_without_ownership_regulatory_clearance",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="KakaoBank growth cannot be scored as Green while founder/legal ownership eligibility is unresolved.",
    ),
    Round288CaseCandidate(
        case_id="r6_loop14_naver_financial_dunamu_upbit_trust_gate",
        symbol="035420",
        company_name="Naver Financial / Dunamu / Upbit",
        primary_archetype=E2RArchetype.DIGITAL_ASSET_MA_TRUST_4C_WATCH,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE, E2RArchetype.FINTECH_CRYPTO_M_AND_A_TRUST_GATE),
        case_type="event_premium",
        round_case_type="event_premium_trust_watch",
        stage1_date=date(2025, 11, 27),
        stage2_date=date(2025, 11, 27),
        stage3_date=None,
        stage4b_date=date(2025, 11, 27),
        stage4c_date=date(2025, 11, 27),
        stage3_decision="digital_asset_MA_is_stage2_until_custody_internal_control_AML_KYC_and_revenue_bridge_close",
        stage4b_status="4B-watch/digital-asset-MA-plus-7pct; 4C-watch/abnormal-withdrawal-custody",
        hard_4c_confirmed=False,
        evidence_fields=("all_stock_deal_15_13tn_krw", "exchange_ratio_2_54", "Upbit_market_share_context", "Naver_initial_plus_7pct"),
        red_flag_fields=("M&A_synergy_without_custody_control", "abnormal_withdrawal_or_custody_failure", "Naver_later_minus_4_2pct", "AML_KYC_regulatory_clearance_unconfirmed"),
        price_data_source="Reuters Naver Financial-Dunamu deal and Upbit abnormal withdrawal anchor",
        reported_price_anchor="Naver initially +7% then later -4.2%",
        reported_return_anchor="15.13T KRW deal; 54B KRW abnormal withdrawal turned the same-day trust gate negative",
        event_mfe_pct=7.0,
        event_mae_pct=-4.2,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"deal_value_krw_trn": 15.13, "deal_value_usd_bn": 10.27, "exchange_ratio_naver_financial_per_dunamu": 2.54, "upbit_market_share_context_pct": 70, "event_initial_mfe_pct": 7.0, "event_later_mae_pct": -4.2, "event_swing_pp": -11.2, "abnormal_withdrawal_krw_bn": 54, "loss_coverage": "Upbit_to_cover_using_own_assets"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_trust_watch",
        rerating_result="event_premium",
        round_rerating_label="digital_asset_MA_stage2_4C_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="deal_synergy_not_green_without_custody_internal_control",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Naver/Dunamu is the digital-asset trust lesson: synergy premium reversed when custody/internal-control risk appeared.",
    ),
    Round288CaseCandidate(
        case_id="r6_loop14_hana_bank_dunamu_digital_asset_stake",
        symbol="086790",
        company_name="Hana Financial / Hana Bank / Dunamu",
        primary_archetype=E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_BANK_STAKE_STAGE2, E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_STAKE),
        case_type="success_candidate",
        round_case_type="success_candidate_but_price_data_unavailable",
        stage1_date=date(2026, 5, 14),
        stage2_date=date(2026, 5, 14),
        stage3_date=None,
        stage4b_date=date(2026, 5, 14),
        stage4c_date=None,
        stage3_decision="bank_crypto_stake_is_stage2_until_custody_AML_KYC_capital_treatment_and_revenue_contribution_close",
        stage4b_status="4B-watch/bank-digital-asset-premium-before-revenue-bridge",
        hard_4c_confirmed=False,
        evidence_fields=("Hana_Bank_acquires_6_55pct_Dunamu_stake", "stake_purchase_1tn_krw", "implied_Dunamu_value_15_27tn_krw", "Upbit_volume_share_context"),
        red_flag_fields=("crypto_exchange_market_share_only", "capital_treatment_unconfirmed", "custody_controls_unconfirmed", "AML_KYC_regulatory_clearance_unconfirmed"),
        price_data_source="Reuters Hana Bank-Dunamu stake acquisition anchor",
        reported_price_anchor="Direct event return unavailable",
        reported_return_anchor="1T KRW stake; 6.55%; implied Dunamu value 15.27T KRW; Upbit volume share context >80%",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stake_purchase_krw_trn": 1.0, "stake_purchase_usd_mn_context": 700, "dunamu_stake_acquired_pct": 6.55, "implied_dunamu_equity_value_krw_trn": 15.27, "kakao_investment_remaining_stake_pct": 4.03, "upbit_trading_volume_share_context_pct": 80},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_price_data_unavailable",
        rerating_result="unknown",
        round_rerating_label="bank_digital_asset_stake_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="strategic_crypto_stake_not_bank_EPS_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Hana/Dunamu is Stage 2; custody, AML/KYC, capital treatment and revenue bridge decide any promotion.",
    ),
    Round288CaseCandidate(
        case_id="r6_loop14_samsung_sds_kkr_cb_stablecoin_event",
        symbol="018260",
        company_name="Samsung SDS / KKR",
        primary_archetype=E2RArchetype.PRIVATE_CAPITAL_CB_STABLECOIN_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.AI_CAPITAL_ALLOCATION_EVENT_PREMIUM, E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE),
        case_type="event_premium",
        round_case_type="event_premium_4B_watch",
        stage1_date=date(2026, 4, 15),
        stage2_date=date(2026, 4, 15),
        stage3_date=None,
        stage4b_date=date(2026, 4, 15),
        stage4c_date=date(2026, 4, 15),
        stage3_decision="PE_CB_stablecoin_headline_is_event_premium_until_dilution_adjusted_ROIC_and_revenue_close",
        stage4b_status="4B-watch/PE-CB-plus-20pct; 4C-watch/dilution-stablecoin-revenue",
        hard_4c_confirmed=False,
        evidence_fields=("KKR_CB_820mn_usd", "AI_infrastructure_use_of_funds", "physical_AI_and_stablecoin_optionality", "advisor_period_six_years", "shares_plus_20_8pct_intraday"),
        red_flag_fields=("CB_or_PE_investment_headline_only", "stablecoin_keyword_without_revenue", "cb_dilution_without_clear_roic", "dilution_terms_fully_modelled_false"),
        price_data_source="Reuters KKR convertible-bond and Samsung SDS share reaction anchor",
        reported_price_anchor="Samsung SDS shares +20.8% intraday; KOSPI +3.0%",
        reported_return_anchor="$820M CB and AI/stablecoin/M&A use-of-funds headline moved shares before ROIC proof",
        event_mfe_pct=20.8,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kkr_cb_investment_usd_mn": 820, "kkr_cb_investment_krw_trn_context": 1.207, "cash_and_equivalents_krw_trn": 6.4, "cash_and_equivalents_usd_bn": 4.35, "advisor_period_years": 6, "event_intraday_mfe_pct": 20.8, "event_morning_mfe_pct": 19.4, "kospi_same_context_pct": 3.0, "relative_outperformance_intraday_pp": 17.8, "use_of_funds": ["global growth", "AI infrastructure", "physical AI", "stablecoins", "M&A"], "dilution_terms_fully_modelled": False, "stablecoin_revenue_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="private_capital_CB_digital_finance_option_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="PE_CB_stablecoin_headline_not_ROIC_revenue_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Samsung SDS/KKR is a 4B-watch event premium until dilution-adjusted ROIC and actual AI/stablecoin revenue are proven.",
    ),
)


def round288_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND288_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND288_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round288 R6 Loop-14 finance/capital/digital price-validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=candidate.evidence_fields if candidate.stage3_date else (),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("policy", "rally", "premium", "ipo", "buyback", "m&a", "cb", "plus", "valuation", "stage2"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("4c", "failure", "custody", "withdrawal", "legal", "ownership", "credit", "cet1", "aml", "kyc", "dilution", "proposal"))),
            must_have_fields=ROUND288_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type not in {"structural_success", "success_candidate"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND288_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "hard_4c_not_confirmed_true",
                "do_not_use_round288_cases_as_candidate_generation_input",
                "do_not_treat_valueup_ipo_crypto_stablecoin_or_pe_headlines_as_green",
                "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
                *ROUND288_GREEN_REQUIRED_FIELDS,
                *ROUND288_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
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
                    or candidate.stage1_price_anchor is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.84 if "unavailable" not in candidate.price_validation_status else 0.72,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round288_case_rows() -> tuple[dict[str, str], ...]:
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
            "event_mfe_pct": _float_text(candidate.event_mfe_pct),
            "event_mae_pct": _float_text(candidate.event_mae_pct),
            "stage1_price_anchor": _float_text(candidate.stage1_price_anchor),
            "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
            "stage3_price_anchor": _float_text(candidate.stage3_price_anchor),
            "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
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
        for candidate in ROUND288_CASE_CANDIDATES
    )


def round288_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND288_SCORE_ADJUSTMENTS)


def round288_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND288_SHADOW_WEIGHT_ROWS)


def round288_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND288_DEEP_SUB_ARCHETYPES)


def round288_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round288_price_validation": "true"} for field in ROUND288_PRICE_VALIDATION_FIELDS)


def round288_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round288_label": label, "canonical_archetype": canonical} for label, canonical in ROUND288_REQUIRED_TARGET_ALIASES.items())


def round288_summary() -> dict[str, int | bool | str]:
    cases = ROUND288_CASE_CANDIDATES
    return {
        "source_round": ROUND288_SOURCE_ROUND_PATH,
        "round_id": ROUND288_ANALYST_ROUND_ID,
        "large_sector": ROUND288_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "unknown_alignment_count": sum(1 for case in cases if case.score_price_alignment == "unknown"),
        "target_archetype_count": len(ROUND288_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND288_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND288_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
        "hard_4c_not_confirmed": not any(case.hard_4c_confirmed for case in cases),
    }


def round288_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND288_SOURCE_ROUND_PATH,
        "round_id": ROUND288_ANALYST_ROUND_ID,
        "large_sector": ROUND288_LARGE_SECTOR,
        "summary": round288_summary(),
        "target_aliases": dict(ROUND288_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND288_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND288_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND288_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND288_HARD_4C_GATES),
        "score_adjustments": list(round288_score_adjustment_rows()),
        "shadow_weights": list(round288_shadow_weight_rows()),
        "deep_sub_archetypes": list(round288_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND288_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round288_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_valueup_ipo_crypto_stablecoin_or_pe_headlines_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round288_summary_markdown() -> str:
    summary = round288_summary()
    lines = [
        "# Round 288 R6 Loop 14 Finance Capital Digital Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- Stage 3 dated candidates: {summary['stage3_case_count']}",
        f"- stage4b_watch: {summary['stage4b_watch_count']}",
        f"- stage4c_watch: {summary['stage4c_watch_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND288_CASE_CANDIDATES:
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
            "- Financial holding Value-Up and SK Square are Stage 2 paths until actual payout/cancellation, credit cost and discount compression close.",
            "- Samsung C&T is the shareholder-return false-positive guardrail: proposal is not execution.",
            "- K Bank and KakaoBank show that digital-bank growth needs aftermarket, credit and ownership-risk gates.",
            "- Naver/Dunamu, Hana/Dunamu and Samsung SDS/KKR show that digital-asset or stablecoin optionality is Stage 2/4B-watch before custody, AML/KYC, capital treatment and ROIC proof.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round288_green_gate_review_markdown() -> str:
    lines = [
        "# Round 288 R6 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R6 Stage 3-Green is not `Value-Up`, `buyback`, `IPO`, `crypto`, `stablecoin`, or `PE investment` as a headline. It requires CET1, actual payout/cancellation, credit-cost control, discount compression, aftermarket demand, custody/internal control, AML/KYC, capital treatment, dilution-adjusted ROIC, and price-path evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND288_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND288_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND288_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Value-Up law` is like a door opening. The company still has to walk through it with CET1, payout execution and credit-cost control.",
            "- `K Bank customers` are useful, but Green needs listed aftermarket demand, NIM, funding cost and credit quality.",
            "- `Naver/Dunamu M&A` can move price, but an Upbit abnormal withdrawal makes custody/internal-control a blocking gate.",
            "- `Samsung SDS/KKR CB` is a credible catalyst, but dilution-adjusted ROIC and real AI/stablecoin revenue decide durability.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round288_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 288 R6 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND288_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C / Strong Watch Gates", ""])
    lines.extend(f"- {field}" for field in ROUND288_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C confirmed | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND288_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    lines.extend(["", "이번 라운드에서 직접 hard 4C는 확정하지 않고 strong watch로 유지한다."])
    return "\n".join(lines) + "\n"


def render_round288_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 288 R6 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, full MFE/MAE, capital-return execution, credit quality, custody controls, AML/KYC clearance, ROIC, revenue contribution, or stage prices where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND288_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND288_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round288_r6_loop14_reports(
    output_directory: str | Path = ROUND288_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND288_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND288_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round288_case_records(), cases_path),
        "audit": _write_json(round288_audit_payload(), audit_path),
        "summary": output / "round288_r6_loop14_price_validation_summary.md",
        "case_matrix": output / "round288_r6_loop14_case_matrix.csv",
        "target_aliases": output / "round288_r6_loop14_target_aliases.csv",
        "score_adjustments": output / "round288_r6_loop14_score_adjustments.csv",
        "shadow_weights": output / "round288_r6_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round288_r6_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round288_r6_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round288_r6_loop14_green_gate_review.md",
        "price_validation_plan": output / "round288_r6_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round288_r6_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round288_summary_markdown(), encoding="utf-8")
    _write_csv(round288_case_rows(), paths["case_matrix"])
    _write_csv(round288_target_alias_rows(), paths["target_aliases"])
    _write_csv(round288_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round288_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round288_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round288_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round288_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round288_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round288_stage4b_4c_review_markdown(), encoding="utf-8")
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


__all__ = [
    "ROUND288_CASE_CANDIDATES",
    "ROUND288_GREEN_FORBIDDEN_PATTERNS",
    "ROUND288_GREEN_REQUIRED_FIELDS",
    "ROUND288_HARD_4C_GATES",
    "ROUND288_LARGE_SECTOR",
    "ROUND288_PRICE_VALIDATION_FIELDS",
    "ROUND288_REQUIRED_TARGET_ALIASES",
    "ROUND288_SCORE_ADJUSTMENTS",
    "ROUND288_SHADOW_WEIGHT_ROWS",
    "ROUND288_STAGE4B_WATCH_TRIGGERS",
    "render_round288_green_gate_review_markdown",
    "render_round288_stage4b_4c_review_markdown",
    "round288_audit_payload",
    "round288_case_records",
    "round288_case_rows",
    "round288_deep_sub_archetype_rows",
    "round288_shadow_weight_rows",
    "round288_summary",
    "write_round288_r6_loop14_reports",
]
