"""Round-197 R6 Loop-7 financial/capital/digital price-path validation pack.

Round 197 is a calibration-only layer for Korea financial value-up, holding
company capital allocation, bank/insurance capital quality, fintech trust,
digital-asset equity options, and stablecoin policy themes. It records why
low-PBR, policy value-up, treasury buyback headlines, stablecoin excitement,
and fintech user growth must be separated from durable ROE, CET1/K-ICS,
actual cancellation, credit-cost control, and regulated revenue.

Simple example: `low PBR + value-up policy` can be Stage 1 attention. It is
not Stage 3-Green until ROE, capital buffer, executed cancellation, credit
cost, and company-level capital allocation are visible as-of the case date.

This module is report/evaluation material only. Production candidate
generation, feature engineering, scoring, staging, and RedTeam code must not
import it.
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


ROUND197_SOURCE_ROUND_PATH = "docs/round/round_197.md"
ROUND197_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round197_r6_loop7_financial_capital_digital_price_validation"
ROUND197_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_loop7_round197.jsonl"
ROUND197_DEFAULT_AUDIT_PATH = (
    "data/sector_taxonomy/round197_r6_loop7_financial_capital_digital_price_validation_audit.json"
)

ROUND197_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "FINANCIAL_SPREAD_BALANCE_SHEET": E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET.value,
    "BANK_HOLDING_VALUEUP_CAPITAL_RETURN": E2RArchetype.BANK_HOLDING_VALUEUP_CAPITAL_RETURN.value,
    "BANK_ROE_PBR_RERATING_KOREA": E2RArchetype.BANK_ROE_PBR_RERATING_KOREA.value,
    "INSURANCE_CAPITAL_RELEASE_VALUEUP": E2RArchetype.INSURANCE_CAPITAL_RELEASE_VALUEUP.value,
    "INSURANCE_KICS_CSM_GATE": E2RArchetype.INSURANCE_KICS_CSM_GATE.value,
    "INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE": E2RArchetype.INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE.value,
    "VALUE_UP_SHAREHOLDER_RETURN": E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN.value,
    "HOLDING_RESTRUCTURING_GOVERNANCE": E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE.value,
    "TREASURY_SHARE_CANCEL_EXECUTION": E2RArchetype.TREASURY_SHARE_CANCEL_EXECUTION.value,
    "PAYMENT_FINTECH_INFRA": E2RArchetype.PAYMENT_FINTECH_INFRA.value,
    "PAYMENT_PRIVACY_REGULATORY_4C": E2RArchetype.PAYMENT_PRIVACY_REGULATORY_4C.value,
    "DIGITAL_ASSET_TOKENIZATION": E2RArchetype.DIGITAL_ASSET_TOKENIZATION.value,
    "DIGITAL_ASSET_BANK_EQUITY_OPTION": E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION.value,
    "KRW_STABLECOIN_POLICY_THEME": E2RArchetype.KRW_STABLECOIN_POLICY_THEME.value,
    "DIGITAL_ASSET_THEME_OVERHEAT": E2RArchetype.DIGITAL_ASSET_THEME_OVERHEAT.value,
    "STABLECOIN_CONVERTIBILITY_OVERLAY": E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY.value,
    "REGULATED_STABLECOIN_INFRA": E2RArchetype.REGULATED_STABLECOIN_INFRA.value,
    "INTERNET_BANK_PROFITABILITY": E2RArchetype.INTERNET_BANK_PROFITABILITY.value,
    "PLATFORM_GOVERNANCE_LEGAL_RISK": E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK.value,
    "BANK_CREDIT_COST_PF_OVERLAY": E2RArchetype.BANK_CREDIT_COST_PF_OVERLAY.value,
    "VALUE_UP_CROWDED_4B_WATCH": E2RArchetype.VALUE_UP_CROWDED_4B_WATCH.value,
}

ROUND197_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "roe_structurally_improving_or_sustained",
    "cet1_or_kics_capital_buffer",
    "actual_buyback_cancellation",
    "dividend_or_cancel_policy_durable",
    "credit_cost_pf_risk_passed",
    "pbr_rerating_runway",
    "company_level_capital_allocation_evidence",
    "digital_asset_revenue_model_or_equity_method_income",
    "regulatory_privacy_governance_trust_passed",
)

ROUND197_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "low_pbr_only",
    "policy_valueup_only",
    "treasury_buyback_without_cancellation",
    "stablecoin_policy_theme_only",
    "digital_asset_equity_option_without_revenue",
    "fintech_user_growth_without_profit",
    "non_bank_acquisition_with_capital_ratio_weakening",
    "major_shareholder_legal_risk",
    "privacy_or_data_trust_break",
)

ROUND197_STAGE4B_STATUSES: tuple[str, ...] = ("none", "watch", "elevated", "graduated")

ROUND197_HARD_4C_GATES: tuple[str, ...] = (
    "pf_credit_cost_spike",
    "cet1_or_kics_weakening",
    "buyback_cancellation_cancelled",
    "dividend_payout_retreat",
    "large_acquisition_capital_ratio_damage",
    "major_shareholder_legal_risk",
    "financial_crime_or_governance_legal_break",
    "privacy_data_transfer_fine",
    "stablecoin_forex_risk_regulation_tightening",
    "digital_asset_volume_collapse",
    "equity_stake_impairment",
)

ROUND197_PRICE_BACKFILL_FIELDS: tuple[str, ...] = (
    "stage1_date",
    "stage2_date",
    "stage3_date",
    "stage4b_date",
    "stage4c_date",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_date",
    "peak_price",
    "MFE_5D",
    "MFE_20D",
    "MFE_30D",
    "MFE_60D",
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_5D",
    "MAE_20D",
    "MAE_30D",
    "MAE_60D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "MAE_2Y",
    "drawdown_after_peak",
    "relative_strength_vs_kospi",
    "relative_strength_vs_financial_basket",
    "relative_strength_vs_bank_basket",
    "relative_strength_vs_insurance_basket",
    "roe",
    "cet1_ratio",
    "kics_ratio",
    "csm_growth",
    "credit_cost",
    "pf_exposure",
    "buyback_announced",
    "buyback_cancelled",
    "dividend_payout_ratio",
    "pbr",
    "pbr_roe_gap",
    "nav_discount",
    "equity_method_income",
    "regulated_revenue",
    "stablecoin_policy_theme_flag",
    "digital_asset_revenue_unverified_flag",
    "privacy_data_trust_break_flag",
    "major_shareholder_legal_risk_flag",
    "stage4b_status",
    "hard_4c_confirmed",
)


@dataclass(frozen=True)
class Round197ScoreAdjustment:
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
class Round197CaseCandidate:
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
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND197_SCORE_ADJUSTMENTS: tuple[Round197ScoreAdjustment, ...] = (
    Round197ScoreAdjustment("roe_sustainability", 4, "raise", "저PBR보다 ROE가 유지되거나 개선되는지가 PBR frame change의 시작이다."),
    Round197ScoreAdjustment("cet1_buffer", 4, "raise", "CET1/K-ICS buffer가 있어야 환원과 인수가 지속된다."),
    Round197ScoreAdjustment("real_buyback_cancellation", 5, "raise", "자사주 매입보다 실제 소각이 자본배분 실행 증거다."),
    Round197ScoreAdjustment("dividend_payout_visibility", 3, "raise", "배당/소각 정책이 반복 가능해야 한다."),
    Round197ScoreAdjustment("credit_cost_control", 4, "raise", "PF와 credit cost가 안정돼야 금융주 rerating이 지속된다."),
    Round197ScoreAdjustment("pbr_roe_gap", 3, "raise", "ROE 대비 PBR discount가 줄어들 여지가 있어야 한다."),
    Round197ScoreAdjustment("capital_release_quality", 3, "raise", "보험/지주 NAV는 매각대금 활용과 자본 release가 확인될 때 강해진다."),
    Round197ScoreAdjustment("regulated_revenue_visibility", 3, "raise", "디지털자산/결제는 실제 수수료, 지분법, reserve income이 필요하다."),
    Round197ScoreAdjustment("nav_discount_with_monetization", 3, "raise", "NAV discount는 소각/배당/자산화로 이어질 때만 강하다."),
    Round197ScoreAdjustment("non_bank_expansion_with_capital_buffer", 2, "raise", "비은행 확장은 CET1 buffer를 훼손하지 않을 때만 가점한다."),
    Round197ScoreAdjustment("low_pbr_only", -5, "lower", "저PBR만으로는 Stage 1 attention이다."),
    Round197ScoreAdjustment("policy_valueup_only", -4, "lower", "정책 기대만 있고 회사 실행이 없으면 Green 근거가 아니다."),
    Round197ScoreAdjustment("treasury_buyback_without_cancellation", -4, "lower", "자사주 매입만 있고 소각이 없으면 환원 실행력이 낮다."),
    Round197ScoreAdjustment("stablecoin_policy_theme_only", -5, "lower", "원화 스테이블코인 정책 테마만으로는 수익모델이 없다."),
    Round197ScoreAdjustment("digital_asset_equity_option_without_revenue", -3, "lower", "지분투자는 수익화와 자본비율 영향 확인 전 Stage 2 watch다."),
    Round197ScoreAdjustment("fintech_user_growth_without_profit", -3, "lower", "사용자 수만 있고 take rate/OP가 없으면 제한한다."),
    Round197ScoreAdjustment("privacy_or_data_trust_break", -5, "lower", "개인정보/데이터 신뢰 훼손은 fintech hard RedTeam이다."),
    Round197ScoreAdjustment("major_shareholder_legal_risk", -5, "lower", "대주주 적격성 리스크는 은행/핀테크 Green을 막는다."),
    Round197ScoreAdjustment("capital_ratio_weakening", -4, "lower", "인수나 환원으로 자본비율이 약해지면 Stage 3를 제한한다."),
    Round197ScoreAdjustment("pf_credit_cost_unknown", -3, "lower", "PF/credit cost가 불명확하면 저PBR rerating을 보류한다."),
    Round197ScoreAdjustment("mna_expansion_without_cet1_buffer", -3, "lower", "비은행 인수는 CET1 buffer 확인 전 가점하지 않는다."),
)


ROUND197_CASE_CANDIDATES: tuple[Round197CaseCandidate, ...] = (
    Round197CaseCandidate(
        case_id="sk_square_valueup_buyback_nav_discount_stage2_4b_watch",
        symbol="402340",
        company_name="SK스퀘어",
        primary_archetype=E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
        secondary_archetypes=(
            E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,
            E2RArchetype.TREASURY_SHARE_CANCEL_EXECUTION,
            E2RArchetype.VALUE_UP_CROWDED_4B_WATCH,
        ),
        case_type="structural_success",
        stage1_date=None,
        stage2_date=date(2024, 11, 21),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="conditional_until_nav_discount_narrows_with_repeat_cancellation_and_value_capture_not_only_skhynix_price",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=(
            "100b_krw_treasury_share_cancellation",
            "additional_100b_krw_buyback_cancellation_plan",
            "activist_pressure_valueup_context",
            "skhynix_stake_nav_discount",
            "independent_director_nomination",
        ),
        red_flag_fields=("skhynix_price_dependency", "discount_rewidening_watch", "cancellation_continuity_unverified", "ai_semiconductor_rally_4b_watch"),
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Actual cancellation plus NAV discount is strong R6 evidence, but SK Hynix-driven price acceleration requires 4B-watch.",
    ),
    Round197CaseCandidate(
        case_id="hana_financial_dunamu_equity_option_stage2_watch",
        symbol="086790",
        company_name="하나금융지주/하나은행",
        primary_archetype=E2RArchetype.DIGITAL_ASSET_BANK_EQUITY_OPTION,
        secondary_archetypes=(
            E2RArchetype.REGULATED_STABLECOIN_INFRA,
            E2RArchetype.BANK_HOLDING_VALUEUP_CAPITAL_RETURN,
            E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY,
        ),
        case_type="success_candidate",
        stage1_date=date(2025, 6, 18),
        stage2_date=date(2026, 5, 14),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_equity_method_income_regulatory_approval_capital_ratio_and_digital_asset_revenue_model",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("dunamu_6_55pct_stake_1t_krw_acquisition", "upbit_high_market_share", "digital_asset_equity_option", "won_stablecoin_policy_context"),
        red_flag_fields=("regulatory_revenue_unverified", "capital_ratio_impact_unverified", "digital_asset_volume_risk", "stablecoin_forex_concern"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Dunamu equity option is strong Stage 2, but Stage 3 waits for regulated revenue, equity-method income, and capital impact.",
    ),
    Round197CaseCandidate(
        case_id="samsung_life_nav_valueup_forced_stake_sale_regulatory_watch",
        symbol="032830",
        company_name="삼성생명",
        primary_archetype=E2RArchetype.INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE,
        secondary_archetypes=(E2RArchetype.INSURANCE_CAPITAL_RELEASE_VALUEUP, E2RArchetype.INSURANCE_KICS_CSM_GATE),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2026, 3, 19),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_sale_proceeds_use_dividend_cancel_kics_csm_and_insurance_core_profit_confirmed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("samsung_electronics_stake_nav_discount", "book_value_discount", "1_3t_krw_samsung_electronics_stake_sale", "regulatory_risk_response"),
        red_flag_fields=("forced_sale_or_regulatory_overhang", "capital_release_use_unverified", "kics_csm_unverified", "samsung_electronics_price_dependency"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Insurance NAV value-up is useful, but a regulatory stake sale is not Green before capital release and shareholder return use are confirmed.",
    ),
    Round197CaseCandidate(
        case_id="kakaobank_internet_bank_governance_ownership_4c_watch",
        symbol="323410",
        company_name="카카오뱅크",
        primary_archetype=E2RArchetype.INTERNET_BANK_PROFITABILITY,
        secondary_archetypes=(E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK, E2RArchetype.PAYMENT_FINTECH_INFRA),
        case_type="failed_rerating",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 7, 22),
        stage3_decision="forbidden_until_profitability_non_interest_income_asset_quality_and_major_shareholder_legal_risk_resolved",
        stage4b_status="watch",
        hard_4c_confirmed=True,
        evidence_fields=("internet_bank_growth_story", "mobile_bank_profitability_option"),
        red_flag_fields=("major_shareholder_legal_risk", "bank_ownership_regulatory_risk", "governance_legal_overhang", "ipo_overvaluation_watch"),
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="no_rerating",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Internet-bank user growth cannot override major-shareholder legal and ownership regulatory risk.",
    ),
    Round197CaseCandidate(
        case_id="kakaopay_aton_krw_stablecoin_policy_theme_overheat",
        symbol="377300/158430",
        company_name="카카오페이/아톤 등 스테이블코인 테마",
        primary_archetype=E2RArchetype.KRW_STABLECOIN_POLICY_THEME,
        secondary_archetypes=(E2RArchetype.DIGITAL_ASSET_THEME_OVERHEAT, E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY),
        case_type="overheat",
        stage1_date=date(2025, 6, 18),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 6, 18),
        stage4c_date=None,
        stage3_decision="forbidden_policy_theme_without_license_issuance_fee_reserve_income_or_bank_partner_revenue",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("won_stablecoin_policy_expectation", "related_stock_price_rally", "digital_asset_reform_bet"),
        red_flag_fields=("stablecoin_policy_theme_only", "revenue_model_missing", "forex_capital_flow_concern", "non_bank_issuance_systemic_risk"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="theme_overheat",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Stablecoin policy excitement is Stage 1/4B-watch before licensing, fee, reserve income, and regulated revenue are visible.",
    ),
    Round197CaseCandidate(
        case_id="kakaopay_privacy_data_transfer_fine_payment_4c_break",
        symbol="377300",
        company_name="카카오페이",
        primary_archetype=E2RArchetype.PAYMENT_PRIVACY_REGULATORY_4C,
        secondary_archetypes=(E2RArchetype.PAYMENT_FINTECH_INFRA, E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK),
        case_type="4c_thesis_break",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="forbidden_privacy_data_trust_break_before_take_rate_op_profit_and_regulatory_trust_recovered",
        stage4b_status="watch",
        hard_4c_confirmed=True,
        evidence_fields=("payment_fintech_infra_growth_story", "payment_volume_option"),
        red_flag_fields=("2025_04_privacy_data_transfer_fine_month_only", "privacy_data_trust_break", "regulatory_trust_damage", "take_rate_profit_unverified"),
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="Payment volume is not enough when privacy/data trust is broken; exact April 2025 sanction date needs source/date backfill.",
    ),
    Round197CaseCandidate(
        case_id="woori_financial_valueup_nonbank_expansion_capital_buffer_watch",
        symbol="316140",
        company_name="우리금융지주",
        primary_archetype=E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        secondary_archetypes=(E2RArchetype.BANK_HOLDING_VALUEUP_CAPITAL_RETURN, E2RArchetype.BANK_CREDIT_COST_PF_OVERLAY),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_cet1_credit_cost_dividend_cancel_nonbank_integration_and_capital_buffer_confirmed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("2025_net_income_growth_summary", "non_bank_insurance_expansion", "valueup_bank_low_pbr_context"),
        red_flag_fields=("capital_buffer_watch", "cet1_unverified", "pf_credit_cost_unknown", "acquisition_integration_cost", "shareholder_return_durability_unverified"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Non-bank expansion can be good, but it is not Green before CET1, credit cost, integration cost, and shareholder return are clear.",
    ),
)


def round197_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND197_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector.value,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round197 R6 Loop-7 financial/capital/digital price-path validation case. "
                "This is calibration-only and must not be used for candidate generation."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "policy" in field or "story" in field or "rally" in field or "option" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "cancellation" in field or "nav_discount" in field or "equity_option" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "4b" in field or "rally" in field or "premium" in field or "theme" in field or "price" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "legal" in field
                or "privacy" in field
                or "regulatory" in field
                or "credit" in field
                or "cet1" in field
                or "capital" in field
                or "trust" in field
            ),
            must_have_fields=ROUND197_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4b_watch", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={
                "roe_sustainability_delta": 4.0,
                "cet1_buffer_delta": 4.0,
                "real_buyback_cancellation_delta": 5.0,
                "credit_cost_control_delta": 4.0,
                "capital_release_quality_delta": 3.0,
                "regulated_revenue_visibility_delta": 3.0,
                "low_pbr_only_delta": -5.0,
                "stablecoin_policy_theme_only_delta": -5.0,
                "privacy_or_data_trust_break_delta": -5.0,
                "major_shareholder_legal_risk_delta": -5.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "needs_ohlc_backfill_true",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_low_pbr_valueup_policy_or_stablecoin_theme_as_green_evidence",
                *ROUND197_GREEN_REQUIRED_FIELDS,
                *ROUND197_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8 if candidate.stage2_date or candidate.stage4c_date else 0.35,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round197_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND197_CASE_CANDIDATES:
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


def round197_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND197_SCORE_ADJUSTMENTS)


def round197_price_backfill_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round197_backfill": "true"} for field in ROUND197_PRICE_BACKFILL_FIELDS)


def round197_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round197_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND197_REQUIRED_TARGET_ALIASES.items()
    )


def round197_summary() -> dict[str, int | bool]:
    cases = round197_case_records()
    return {
        "case_candidate_count": len(cases),
        "required_target_count": len(ROUND197_REQUIRED_TARGET_ALIASES),
        "score_adjustment_count": len(ROUND197_SCORE_ADJUSTMENTS),
        "price_backfill_field_count": len(ROUND197_PRICE_BACKFILL_FIELDS),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "thesis_break_count": sum(1 for case in cases if case.case_type == "4c_thesis_break"),
        "hard_4c_case_count": sum(1 for case in ROUND197_CASE_CANDIDATES if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in ROUND197_CASE_CANDIDATES if case.stage3_date),
        "stage3_conditional_candidate_count": sum(1 for case in ROUND197_CASE_CANDIDATES if "conditional" in case.stage3_decision),
        "stage4b_watch_or_elevated_count": sum(
            1 for case in ROUND197_CASE_CANDIDATES if case.stage4b_status in {"watch", "elevated"}
        ),
        "needs_ohlc_backfill_count": sum(1 for case in ROUND197_CASE_CANDIDATES if case.price_validation_status == "needs_ohlc_backfill"),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "needs_ohlc_backfill": True,
    }


def write_round197_r6_loop7_reports(
    *,
    output_directory: str | Path = ROUND197_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND197_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND197_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = write_case_library(round197_case_records(), cases_path)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "audit_json": audit,
        "summary": output / "round197_r6_loop7_price_validation_summary.md",
        "case_matrix": output / "round197_r6_loop7_case_matrix.csv",
        "target_aliases": output / "round197_r6_loop7_target_aliases.csv",
        "score_adjustments": output / "round197_r6_loop7_score_adjustments.csv",
        "price_backfill_fields": output / "round197_r6_loop7_price_backfill_fields.csv",
        "green_gate_review": output / "round197_r6_loop7_green_gate_review.md",
        "price_backfill_plan": output / "round197_r6_loop7_price_backfill_plan.md",
        "stage4b_4c_review": output / "round197_r6_loop7_stage4b_4c_review.md",
    }
    audit.write_text(json.dumps(round197_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round197_case_rows(), paths["case_matrix"])
    _write_rows(round197_target_alias_rows(), paths["target_aliases"])
    _write_rows(round197_score_adjustment_rows(), paths["score_adjustments"])
    _write_rows(round197_price_backfill_field_rows(), paths["price_backfill_fields"])
    paths["summary"].write_text(render_round197_summary_markdown(), encoding="utf-8")
    paths["green_gate_review"].write_text(render_round197_green_gate_review_markdown(), encoding="utf-8")
    paths["price_backfill_plan"].write_text(render_round197_price_backfill_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round197_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def round197_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND197_SOURCE_ROUND_PATH,
        "large_sector": Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL.value,
        "summary": round197_summary(),
        "target_aliases": list(round197_target_alias_rows()),
        "green_required_fields": list(ROUND197_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND197_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_statuses": list(ROUND197_STAGE4B_STATUSES),
        "hard_4c_gates": list(ROUND197_HARD_4C_GATES),
        "score_adjustments": list(round197_score_adjustment_rows()),
        "case_ids": [case.case_id for case in ROUND197_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round197_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_low_pbr_policy_valueup_or_stablecoin_theme_as_green_evidence",
            "do_not_invent_prices_stage_dates_roe_cet1_kics_credit_cost_buyback_cancellation_or_regulated_revenue",
        ],
    }


def render_round197_summary_markdown() -> str:
    summary = round197_summary()
    lines = [
        "# Round-197 R6 Loop-7 Price-Path Validation Summary",
        "",
        f"- source_round: `{ROUND197_SOURCE_ROUND_PATH}`",
        "- large_sector: `FINANCIAL_CAPITAL_DIGITAL`",
        "- scope: Korean bank, insurance, holding value-up, payment fintech, digital asset, and stablecoin policy validation",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- score_adjustment_count: {summary['score_adjustment_count']}",
        f"- price_backfill_field_count: {summary['price_backfill_field_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- overheat_count: {summary['overheat_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
        f"- thesis_break_count: {summary['thesis_break_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- stage3_case_count: {summary['stage3_case_count']}",
        f"- stage3_conditional_candidate_count: {summary['stage3_conditional_candidate_count']}",
        f"- stage4b_watch_or_elevated_count: {summary['stage4b_watch_or_elevated_count']}",
        f"- needs_ohlc_backfill_count: {summary['needs_ohlc_backfill_count']}",
        "- production_scoring_changed: false",
        "- candidate_generation_input: false",
        "- shadow_weight_only: true",
        "- needs_ohlc_backfill: true",
        "",
        "## Interpretation",
        "",
        "- R6는 저PBR과 정책 밸류업을 실제 ROE/CET1/소각/credit-cost evidence와 분리한다.",
        "- SK스퀘어는 소각과 NAV discount가 강하지만 SK하이닉스 랠리 뒤에는 4B-watch가 필요하다.",
        "- 하나금융의 두나무 지분은 Stage 2 후보지만 규제수익, 지분법, 자본비율 영향 전에는 Green이 아니다.",
        "- 삼성생명은 NAV discount가 있어도 규제성 지분매각과 capital release를 같이 봐야 한다.",
        "- 카카오뱅크/카카오페이는 사용자 수보다 대주주 적격성, 개인정보, 규제 신뢰가 먼저다.",
        "- 스테이블코인 테마는 수익모델 전에는 price_moved_without_evidence로 분리한다.",
        "- 우리금융은 비은행 확장과 CET1/credit cost/주주환원을 함께 검증해야 한다.",
        "",
        "쉬운 예: `as_of_date=2025-06-18`에 스테이블코인 정책 기대가 커져 관련주가 올라도, 실제 발행권·수수료·reserve income이 없으면 Stage 3-Green이 아니다.",
    ]
    return "\n".join(lines) + "\n"


def render_round197_green_gate_review_markdown() -> str:
    lines = [
        "# Round-197 R6 Loop-7 Green Gate Review",
        "",
        "## Green Required Evidence",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND197_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Green Forbidden Patterns", ""])
    lines.extend(f"- `{field}`" for field in ROUND197_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "| --- | --- | ---: | --- |"])
    for adjustment in ROUND197_SCORE_ADJUSTMENTS:
        lines.append(f"| `{adjustment.axis}` | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these weights to production scoring yet.",
            "- Do not use Round197 cases as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds to force promotion.",
            "- Do not invent ROE, CET1, K-ICS, credit cost, cancellation, regulated revenue, stage prices, or MFE/MAE.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round197_price_backfill_plan_markdown() -> str:
    lines = [
        "# Round-197 R6 Loop-7 Price Backfill Plan",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND197_PRICE_BACKFILL_FIELDS)
    lines.extend(["", "## Priority Cases", "", "| case | stage marker | current status | 4B status | hard 4C |", "| --- | --- | --- | --- | --- |"])
    for case in ROUND197_CASE_CANDIDATES:
        stage_marker = case.stage3_date or case.stage2_date or case.stage4c_date or case.stage4b_date or case.stage1_date
        lines.append(
            f"| `{case.case_id}` | {_date_text(stage_marker) or 'undated'} | "
            f"{case.price_validation_status} | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} |"
        )
    lines.extend(
        [
            "",
            "## Backfill Rule",
            "",
            "- Use official OHLC data for exact MFE/MAE.",
            "- Keep unknown values null or `needs_ohlc_backfill`.",
            "- Split policy value-up, stablecoin, Dunamu, and NAV event price paths from durable ROE/capital-return evidence.",
            "- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round197_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round-197 R6 Loop-7 Stage 4B / 4C Review",
        "",
        "## 4B Status Definitions",
        "",
        "- `watch`: PBR rerating, NAV discount, stablecoin, or digital-asset price moves ahead of durable evidence.",
        "- `elevated`: CET1/K-ICS, PF credit, M&A capital burden, privacy, or regulatory risk becomes material.",
        "- `graduated`: ROE acceleration or capital-return surprise fades and further rerating room narrows.",
        "",
        "## Hard 4C Gates",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND197_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C confirmed | interpretation |", "| --- | --- | --- | --- |"])
    for case in ROUND197_CASE_CANDIDATES:
        lines.append(
            f"| `{case.case_id}` | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    rows_tuple = tuple(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows_tuple[0].keys()), lineterminator="\n")
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow(dict(row))
    return path


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


__all__ = [
    "ROUND197_CASE_CANDIDATES",
    "ROUND197_DEFAULT_AUDIT_PATH",
    "ROUND197_DEFAULT_CASES_PATH",
    "ROUND197_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND197_GREEN_FORBIDDEN_PATTERNS",
    "ROUND197_GREEN_REQUIRED_FIELDS",
    "ROUND197_HARD_4C_GATES",
    "ROUND197_PRICE_BACKFILL_FIELDS",
    "ROUND197_REQUIRED_TARGET_ALIASES",
    "ROUND197_SCORE_ADJUSTMENTS",
    "ROUND197_SOURCE_ROUND_PATH",
    "ROUND197_STAGE4B_STATUSES",
    "Round197CaseCandidate",
    "Round197ScoreAdjustment",
    "render_round197_green_gate_review_markdown",
    "render_round197_price_backfill_plan_markdown",
    "render_round197_stage4b_4c_review_markdown",
    "render_round197_summary_markdown",
    "round197_audit_payload",
    "round197_case_records",
    "round197_case_rows",
    "round197_price_backfill_field_rows",
    "round197_score_adjustment_rows",
    "round197_summary",
    "round197_target_alias_rows",
    "write_round197_r6_loop7_reports",
]
