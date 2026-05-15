"""Round-46 R6 financial, capital-allocation, and digital-finance pack.

Round 46 expands the Round-40 protocol for banks, insurers, securities,
value-up, holding-company governance, payment fintech, and digital-asset
finance themes. It stores target sub-archetypes, shadow score-weight drafts,
stage-date guidance, case candidates, and price-validation fields.

This module is calibration/report material only. Production feature
engineering, scoring, staging, and RedTeam code must not import it.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.archetypes import E2RArchetype
from e2r.sector.case_library import CaseDataQuality, E2RCaseRecord, PriceValidation
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector, Round10ThemePosture


ROUND46_SOURCE_ROUND_PATH = "docs/round/round_46.md"
ROUND46_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round46_r6_financial_capital_digital"
ROUND46_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_round46.jsonl"
ROUND46_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round46_r6_v1.csv"


@dataclass(frozen=True)
class Round46ScoreWeightDraft:
    eps_fcf: int
    structural_visibility: int
    bottleneck_pricing: int
    market_mispricing: int
    valuation: int
    capital_allocation: int
    information_confidence: int

    def as_dict(self) -> dict[str, int]:
        return {
            "eps_fcf": self.eps_fcf,
            "structural_visibility": self.structural_visibility,
            "bottleneck_pricing": self.bottleneck_pricing,
            "market_mispricing": self.market_mispricing,
            "valuation": self.valuation,
            "capital_allocation": self.capital_allocation,
            "information_confidence": self.information_confidence,
        }


@dataclass(frozen=True)
class Round46ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round46ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    normalization_point: str

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round46CaseCandidate:
    case_id: str
    target_id: str
    symbol: str
    company_name: str
    market: str
    case_type: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    alignment_hint: str
    price_validation_status: str
    source_refs: tuple[str, ...]
    notes: str
    secondary_archetypes: tuple[E2RArchetype, ...] = ()

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND46_SCORE_TARGETS: tuple[Round46ScoreTarget, ...] = (
    Round46ScoreTarget(
        "FINANCIAL_SPREAD_BALANCE_SHEET",
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round46ScoreWeightDraft(15, 20, 5, 15, 25, 10, 5),
        ("korea_discount_policy", "dividend_tax_reform", "bank_pbr_rerating_news"),
        ("roe_improvement", "cet1_stable", "credit_cost_down", "buyback_or_dividend"),
        ("pbr_roe_frame_change", "recurring_return_policy", "roe_stable", "credit_risk_low"),
        ("financial_valueup_crowded", "pbr_band_above_history"),
        ("credit_cost_spike", "pf_loss", "cet1_deterioration", "shareholder_return_retreat"),
        ("roe", "cet1_ratio", "credit_cost", "pf_exposure_controlled", "shareholder_return_execution"),
        ("credit_cost", "pf_exposure", "cet1_deterioration", "return_policy_retreat"),
        "Financial Green needs ROE/PBR, capital ratio, credit cost, and executed shareholder return together.",
    ),
    Round46ScoreTarget(
        "INSURANCE_UNDERWRITING_CYCLE",
        E2RArchetype.INSURANCE_UNDERWRITING_CYCLE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round46ScoreWeightDraft(15, 21, 4, 15, 25, 10, 5),
        ("loss_ratio_improvement", "csm_growth", "valueup_insurance_news"),
        ("roe_improvement", "k_ics_stable", "dividend_or_buyback_execution"),
        ("pbr_roe_rerating", "repeat_underwriting_quality", "capital_ratio_stable"),
        ("insurance_valueup_crowded", "pbr_normalized"),
        ("loss_ratio_worse", "k_ics_deterioration", "alternative_investment_loss", "cyber_operational_risk"),
        ("roe", "k_ics_ratio", "csm_growth", "loss_ratio", "shareholder_return_execution"),
        ("loss_ratio", "k_ics_deterioration", "operational_risk", "investment_loss"),
        "Insurance Green needs underwriting quality, capital, and repeatable return policy, not dividend yield alone.",
    ),
    Round46ScoreTarget(
        "SECURITIES_BROKERAGE_CYCLE",
        E2RArchetype.SECURITIES_BROKERAGE_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round46ScoreWeightDraft(18, 14, 5, 15, 18, 8, 5),
        ("trading_value_growth", "market_rally", "ipo_ib_recovery_expectation"),
        ("brokerage_revenue_growth", "ib_fee_growth", "op_eps_revision"),
        ("pf_risk_low", "roe_structure_improved", "ib_pipeline_durable"),
        ("brokerage_cycle_peak", "securities_group_overheated"),
        ("tax_policy_shock", "trading_value_drop", "pf_loss", "proprietary_trading_loss"),
        ("trading_value", "ib_fee_revenue", "pf_risk_low", "roe_improvement"),
        ("tax_policy_shock", "trading_value_drop", "pf_loss", "proprietary_loss"),
        "Brokerage is cycle/watch unless trading value, IB, PF risk, and ROE structure all support durability.",
    ),
    Round46ScoreTarget(
        "VALUE_UP_SHAREHOLDER_RETURN",
        E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round46ScoreWeightDraft(12, 18, 4, 20, 25, 10, 5),
        ("commercial_act_revision", "dividend_tax_reform", "valueup_index", "buyback_policy_news"),
        ("treasury_share_cancellation", "dividend_growth", "roe_improvement"),
        ("pbr_nav_discount_narrows", "repeat_return_policy", "capital_allocation_execution"),
        ("valueup_crowded_trade", "pbr_band_rerated_before_execution"),
        ("no_cancellation", "activist_rejection", "capital_allocation_retreat", "controlling_shareholder_risk"),
        ("buyback_cancelled", "dividend_growth", "roe_improvement", "minority_shareholder_protection"),
        ("no_cancellation", "execution_failure", "low_roe", "controlling_shareholder_risk"),
        "Value-up is Green only when policy becomes executed buyback cancellation, dividends, ROE, and governance improvement.",
    ),
    Round46ScoreTarget(
        "HOLDING_RESTRUCTURING_GOVERNANCE",
        E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round46ScoreWeightDraft(12, 17, 4, 22, 24, 10, 5),
        ("nav_discount", "subsidiary_value_gap", "activist_or_buyback_news"),
        ("buyback_cancel", "independent_director", "dividend_policy", "governance_improvement"),
        ("nav_discount_narrows", "repeat_capital_return", "minority_protection", "subsidiary_value_supported"),
        ("holding_valueup_crowded", "event_premium_fully_priced"),
        ("activist_rejection", "governance_battle", "debt_ratio_jump", "subsidiary_value_impairment"),
        ("nav_discount", "actual_cancellation", "governance_improvement", "capital_structure_stable"),
        ("governance_battle", "event_premium", "debt_ratio_jump", "minority_conflict"),
        "Holding-company rerating needs NAV discount plus actual governance and capital-allocation execution.",
    ),
    Round46ScoreTarget(
        "PAYMENT_FINTECH_INFRA",
        E2RArchetype.PAYMENT_FINTECH_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round46ScoreWeightDraft(18, 20, 8, 14, 14, 2, 5),
        ("active_users_growth", "global_expansion", "payment_remittance_finance_service"),
        ("payment_volume", "take_rate", "financial_service_attach", "profit_or_fcf"),
        ("repeat_financial_infra_revenue", "regulatory_stability", "security_clean", "credit_loss_control"),
        ("ipo_valuation_overheated", "user_count_story_crowded"),
        ("security_incident", "credit_loss_rate_up", "take_rate_pressure", "regulatory_sanction"),
        ("payment_volume", "take_rate", "attach_rate", "profit_fcf", "regulation_security_clean"),
        ("take_rate_pressure", "security_incident", "credit_loss", "regulatory_sanction"),
        "Payment fintech can improve only when users convert into repeat fee and financial-service revenue.",
    ),
    Round46ScoreTarget(
        "DIGITAL_ASSET_TOKENIZATION",
        E2RArchetype.DIGITAL_ASSET_TOKENIZATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round46ScoreWeightDraft(16, 18, 8, 16, 12, 3, 5),
        ("stablecoin_sto_bill", "tokenization_business_entry", "partnership_news"),
        ("regulatory_approval", "issued_amount", "transaction_volume", "fee_model"),
        ("payment_custody_settlement_infra", "repeat_revenue", "reserve_transparency", "convertibility_clear"),
        ("stablecoin_law_expectation_crowded", "sto_theme_rally"),
        ("depeg", "convertibility_failure", "reserve_problem", "regulatory_rejection", "fraud"),
        ("regulatory_approval", "reserve_transparency", "redemption_capacity", "transaction_volume", "fee_model"),
        ("depeg", "reserve_opacity", "convertibility_risk", "fraud", "regulatory_rejection"),
        "Digital asset Green is blocked until regulated volume, fee model, reserve, and convertibility are proven.",
    ),
    Round46ScoreTarget(
        "CREDIT_DATA_INFRA",
        E2RArchetype.CREDIT_DATA_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round46ScoreWeightDraft(17, 19, 7, 13, 12, 1, 5),
        ("credit_data_contract", "financial_data_infra", "customer_growth"),
        ("recurring_financial_institution_contract", "data_revenue_growth", "opm_improvement"),
        ("repeat_data_revenue", "regulatory_clean", "customer_diversification"),
        ("credit_data_story_crowded",),
        ("privacy_breach", "regulatory_sanction", "customer_concentration", "contract_loss"),
        ("recurring_contracts", "data_revenue", "regulatory_clean", "customer_diversification"),
        ("privacy_breach", "regulation", "customer_concentration"),
        "Credit-data infra needs recurring contracts and clean privacy/regulatory record.",
    ),
    Round46ScoreTarget(
        "VC_EXIT_MARKET_CYCLE",
        E2RArchetype.VC_EXIT_MARKET_CYCLE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round46ScoreWeightDraft(16, 11, 4, 12, 10, 2, 5),
        ("ipo_market_reopen", "venture_exit_expectation", "valuation_rebound"),
        ("exit_volume", "realized_gain", "fundraising_recovery"),
        ("repeat_exit_market", "portfolio_quality", "cash_return"),
        ("vc_exit_cycle_crowded",),
        ("ipo_market_slowdown", "valuation_loss", "funding_market_freeze"),
        ("exit_volume", "realized_gain", "cash_return"),
        ("ipo_slowdown", "valuation_loss", "funding_freeze"),
        "VC/exit market is cycle-heavy and should stay RedTeam-first until realized exits and cash returns are visible.",
    ),
    Round46ScoreTarget(
        "DIGITAL_ASSET_THEME_OVERHEAT",
        E2RArchetype.DIGITAL_ASSET_THEME_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round46ScoreWeightDraft(5, 5, 5, 6, 5, 0, 3),
        ("nft_coin_theme", "blockchain_keyword", "algorithmic_stablecoin_story"),
        ("regulated_revenue", "license_or_partner", "cash_flow"),
        ("legal_recurring_revenue", "reserve_and_redemption_proven", "low_regulatory_risk"),
        ("digital_asset_theme_overheated",),
        ("depeg", "run", "reserve_failure", "fraud", "market_manipulation", "no_revenue"),
        ("regulated_revenue", "reserve_transparency", "cash_flow"),
        ("depeg", "reserve_failure", "fraud", "theme_only", "no_revenue"),
        "Digital-asset themes are Green-blocked without regulated revenue, reserve proof, and cash flow.",
    ),
)


ROUND46_CASE_CANDIDATES: tuple[Round46CaseCandidate, ...] = (
    Round46CaseCandidate(
        "korea_commercial_act_treasury_share_cancel_case",
        "VALUE_UP_SHAREHOLDER_RETURN",
        "KOSPI_VALUEUP_POLICY_REF",
        "Korea Commercial Act treasury-share cancellation reform",
        "KR",
        "success_candidate",
        None,
        date(2026, 2, 25),
        None,
        None,
        None,
        ("commercial_act_revision", "treasury_share_cancel_deadline", "korea_discount_policy", "kospi_rerating"),
        ("policy_expectation_only", "individual_execution_not_verified", "crowded_trade"),
        "macro_policy_aligned_candidate",
        "missing_direct_symbol_mapping",
        ("Reuters Korea Commercial Act revision",),
        "Policy can support R6 rerating background, but individual companies still need executed cancellation, dividends, ROE, and capital quality.",
    ),
    Round46CaseCandidate(
        "korea_dividend_tax_reform_case",
        "VALUE_UP_SHAREHOLDER_RETURN",
        "KOSPI_DIVIDEND_TAX_REF",
        "Korea dividend tax and shareholder-protection reform",
        "KR",
        "success_candidate",
        None,
        date(2025, 6, 11),
        None,
        None,
        None,
        ("dividend_tax_reform", "shareholder_protection", "kospi_price_reaction"),
        ("policy_expectation_only", "individual_execution_not_verified"),
        "stage1_policy_price_aligned",
        "missing_direct_symbol_mapping",
        ("Reuters Korea dividend tax reform",),
        "Dividend tax reform is a market-level Stage 1/2 catalyst; company-level rerating still requires return execution.",
    ),
    Round46CaseCandidate(
        "sk_square_buyback_cancel_case",
        "HOLDING_RESTRUCTURING_GOVERNANCE",
        "402340",
        "SK Square buyback cancellation and governance improvement",
        "KR",
        "success_candidate",
        None,
        date(2024, 11, 21),
        None,
        None,
        None,
        ("nav_discount", "buyback_cancel", "additional_buyback", "independent_director", "subsidiary_value_gap"),
        ("subsidiary_price_dependency", "holding_discount_persistence", "cancellation_scale_insufficient"),
        "holding_valueup_success_candidate",
        "needs_price_backfill",
        ("Reuters SK Square buyback plan",),
        "NAV discount plus actual cancellation and governance improvement is a higher-quality holding-company value-up case.",
    ),
    Round46CaseCandidate(
        "samsung_electronics_buyback_mixed_case",
        "VALUE_UP_SHAREHOLDER_RETURN",
        "005930",
        "Samsung Electronics buyback mixed case",
        "KR",
        "event_premium",
        None,
        date(2024, 11, 15),
        None,
        None,
        None,
        ("buyback_amount", "partial_cancellation", "day_price_reaction"),
        ("buyback_only", "business_thesis_weakness", "hbm_competition_risk", "share_price_down_ytd"),
        "buyback_price_aligned_but_business_risk_remaining",
        "needs_price_backfill",
        ("Reuters Samsung Electronics buyback",),
        "Buyback can support price, but business competitiveness and EPS path remain separate gates.",
        (E2RArchetype.MEMORY_HBM_CAPACITY,),
    ),
    Round46CaseCandidate(
        "korean_financial_holdings_valueup_case",
        "FINANCIAL_SPREAD_BALANCE_SHEET",
        "KR_BANK_HOLDINGS_REF",
        "Korean bank and financial holding value-up rerating",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("roe_to_verify", "cet1_to_verify", "credit_cost_to_verify", "dividend_buyback_execution_to_verify", "pbr_band_to_verify"),
        ("pf_exposure", "credit_cost_spike", "cet1_deterioration", "return_policy_retreat"),
        "sector_success_candidate",
        "needs_source_date_and_price_backfill",
        ("Round46 bank/financial holding framework",),
        "Banks and financial holdings are Green-eligible only after ROE, CET1, credit cost, and shareholder return execution are verified.",
    ),
    Round46CaseCandidate(
        "mynt_gcash_payment_platform_case",
        "PAYMENT_FINTECH_INFRA",
        "MYNT_GCASH_REF",
        "Mynt / GCash payment platform reference",
        "PH",
        "success_candidate",
        None,
        date(2026, 5, 14),
        None,
        None,
        None,
        ("active_users", "bill_payment", "remittance", "savings_lending_insurance_access", "ipo_valuation"),
        ("private_company", "take_rate_unverified", "credit_loss_unverified", "regulation"),
        "payment_platform_success_reference",
        "missing_public_price_data",
        ("Reuters Mynt GCash IPO valuation",),
        "User count is routing context; payment volume, take rate, financial attach, credit loss, and FCF must be checked.",
    ),
    Round46CaseCandidate(
        "toss_won_stablecoin_case",
        "PAYMENT_FINTECH_INFRA",
        "TOSS_REF",
        "Toss global expansion and won stablecoin watch",
        "KR",
        "success_candidate",
        None,
        date(2025, 9, 9),
        None,
        None,
        None,
        ("active_users", "global_expansion", "super_app", "won_stablecoin_plan", "ipo_plan"),
        ("regulatory_approval_missing", "stablecoin_volume_unverified", "valuation_risk"),
        "fintech_success_candidate_plus_stablecoin_watch",
        "missing_public_price_data",
        ("Reuters Toss global push won stablecoin",),
        "Toss payment fintech may be a success candidate, but won stablecoin remains Watch before regulation, volume, and fee model.",
        (E2RArchetype.DIGITAL_ASSET_TOKENIZATION,),
    ),
    Round46CaseCandidate(
        "samsung_ct_activist_rejection_case",
        "HOLDING_RESTRUCTURING_GOVERNANCE",
        "028260",
        "Samsung C&T activist proposal rejection",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("nav_discount", "activist_campaign"),
        ("activist_rejection", "capital_allocation_retreat", "minority_shareholder_protection_failure", "controlling_shareholder_risk"),
        "governance_execution_failure_4c_watch",
        "needs_source_date_and_price_backfill",
        ("Financial Times Samsung C&T activist proposal rejection",),
        "Round document gives a year but no exact date; no stage date is invented.",
    ),
    Round46CaseCandidate(
        "korea_zinc_buyback_event_case",
        "HOLDING_RESTRUCTURING_GOVERNANCE",
        "010130",
        "Korea Zinc buyback and control premium event",
        "KR",
        "event_premium",
        None,
        date(2024, 10, 21),
        None,
        None,
        None,
        ("tender_offer", "buyback_offer", "governance_event", "event_day_price_reaction"),
        ("governance_battle", "debt_ratio_jump", "event_premium", "minority_conflict"),
        "event_premium_plus_governance_watch",
        "needs_price_backfill",
        ("Reuters Korea Zinc buyback offer",),
        "Buybacks and tenders must be separated into shareholder-return execution versus control-premium event risk.",
    ),
    Round46CaseCandidate(
        "korea_tax_policy_shock_case",
        "SECURITIES_BROKERAGE_CYCLE",
        "KOSPI_TAX_SHOCK_REF",
        "Korea stock-market tax policy shock",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 8, 1),
        ("market_rally", "brokerage_cycle"),
        ("tax_policy_shock", "trading_value_drop_risk", "sentiment_collapse", "transaction_tax_risk"),
        "policy_tax_shock_4c_watch",
        "missing_direct_symbol_mapping",
        ("MarketWatch Korea tax proposals",),
        "Tax policy shock can break brokerage and value-up momentum through trading-value and sentiment pressure.",
    ),
    Round46CaseCandidate(
        "terrausd_do_kwon_collapse_case",
        "DIGITAL_ASSET_THEME_OVERHEAT",
        "TERRA_LUNA_REF",
        "TerraUSD / Luna algorithmic stablecoin collapse",
        "GLOBAL",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("algorithmic_stablecoin",),
        ("depeg", "run", "reserve_failure", "fraud", "market_manipulation", "investor_loss"),
        "algorithmic_stablecoin_thesis_break",
        "needs_source_date_and_price_backfill",
        ("Reuters TerraUSD Do Kwon sentencing",),
        "The document gives a broad 2022~2025 window, so no exact stage date is invented.",
        (E2RArchetype.DIGITAL_ASSET_TOKENIZATION,),
    ),
    Round46CaseCandidate(
        "boe_stablecoin_convertibility_warning_case",
        "DIGITAL_ASSET_TOKENIZATION",
        "STABLECOIN_CONVERTIBILITY_REF",
        "Bank of England stablecoin convertibility warning",
        "GLOBAL",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 8),
        ("stablecoin_cross_border_payment",),
        ("convertibility_risk", "reserve_transparency_risk", "liquidity_run", "international_regulatory_conflict"),
        "stablecoin_regulatory_4c_watch",
        "missing_direct_symbol_mapping",
        ("Reuters Bank of England Bailey stablecoin regulation",),
        "Even fiat-backed stablecoin exposure needs reserve, redemption, liquidity, and regulatory proof.",
    ),
)


ROUND46_PRICE_FIELDS: tuple[str, ...] = (
    "case_id",
    "symbol",
    "company_name",
    "primary_archetype",
    "secondary_archetypes",
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
    "peak_price",
    "MFE_30D",
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_30D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "drawdown_after_peak",
    "below_stage3_price_flag",
    "roe",
    "roa",
    "pbr",
    "cet1_ratio",
    "k_ics_ratio",
    "csm_growth",
    "loss_ratio",
    "credit_cost",
    "pf_exposure",
    "dividend_payout_ratio",
    "dividend_growth",
    "buyback_amount",
    "buyback_cancelled_flag",
    "treasury_share_cancel_deadline",
    "shareholder_return_policy",
    "trading_value",
    "brokerage_revenue",
    "ib_fee_revenue",
    "ipo_pipeline_count",
    "vc_exit_volume",
    "proprietary_trading_gain_loss",
    "payment_volume",
    "take_rate",
    "active_users",
    "merchant_count",
    "financial_service_attach_rate",
    "credit_loss_rate",
    "security_incident_flag",
    "stablecoin_issued_amount",
    "stablecoin_transaction_volume",
    "redemption_reserve_ratio",
    "convertibility_risk_flag",
    "regulatory_approval_flag",
    "depeg_event_flag",
    "governance_event_flag",
    "activist_campaign_flag",
    "tender_offer_flag",
    "minority_shareholder_protection_flag",
    "score_price_alignment",
    "price_validation_status",
)


def target_for(target_id: str) -> Round46ScoreTarget | None:
    for target in ROUND46_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round46_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND46_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
        weights = target.score_weight.as_dict()
        stage4b_evidence = candidate.evidence_fields if candidate.case_type == "4b_watch" or candidate.stage4b_date else ()
        stage4c_evidence = candidate.red_flag_fields if candidate.case_type == "4c_thesis_break" or candidate.stage4c_date else ()
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market=candidate.market,
            sector_raw=candidate.target_id,
            primary_archetype=target.canonical_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=target.large_sector.value,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                f"Round46 R6 case for {candidate.target_id}; "
                "case evidence is calibration-only and missing prices remain unfilled."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage2_signals or field in target.green_conditions),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage3_conditions),
            stage4b_evidence=stage4b_evidence,
            stage4c_evidence=stage4c_evidence,
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "overheat", "4b_watch", "4c_thesis_break"} else None,
            score_price_alignment=_score_price_alignment(candidate),
            rerating_result=_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint={
                "eps_fcf": float(weights["eps_fcf"]),
                "visibility": float(weights["structural_visibility"]),
                "bottleneck": float(weights["bottleneck_pricing"]),
                "mispricing": float(weights["market_mispricing"]),
                "valuation": float(weights["valuation"]),
                "capital_allocation": float(weights["capital_allocation"]),
            },
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_cross_evidence_for_green",
                "theme_label_is_not_score_evidence",
                "low_pbr_or_policy_name_is_not_structural_evidence_alone",
                "roe_capital_return_or_regulated_revenue_required_for_green",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.7 if candidate.stage2_date or candidate.stage4c_date else 0.3,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round46_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND46_SCORE_TARGETS:
        weights = target.score_weight.as_dict()
        rows.append(
            {
                "target_id": target.target_id,
                "large_sector": target.large_sector.value,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "eps_fcf": str(weights["eps_fcf"]),
                "structural_visibility": str(weights["structural_visibility"]),
                "bottleneck_pricing": str(weights["bottleneck_pricing"]),
                "market_mispricing": str(weights["market_mispricing"]),
                "valuation": str(weights["valuation"]),
                "capital_allocation": str(weights["capital_allocation"]),
                "information_confidence": str(weights["information_confidence"]),
                "stage1_signals": "|".join(target.stage1_signals),
                "stage2_signals": "|".join(target.stage2_signals),
                "stage3_conditions": "|".join(target.stage3_conditions),
                "stage4b_conditions": "|".join(target.stage4b_conditions),
                "stage4c_conditions": "|".join(target.stage4c_conditions),
                "green_conditions": "|".join(target.green_conditions),
                "red_flags": "|".join(target.red_flags),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round46_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND46_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        assert target is not None
        rows.append(
            {
                "case_id": candidate.case_id,
                "target_id": candidate.target_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "market": candidate.market,
                "case_type": candidate.case_type,
                "canonical_archetype": target.canonical_archetype.value,
                "posture": target.posture.value,
                "stage1_date": candidate.stage1_date.isoformat() if candidate.stage1_date else "",
                "stage2_date": candidate.stage2_date.isoformat() if candidate.stage2_date else "",
                "stage3_date": candidate.stage3_date.isoformat() if candidate.stage3_date else "",
                "stage4b_date": candidate.stage4b_date.isoformat() if candidate.stage4b_date else "",
                "stage4c_date": candidate.stage4c_date.isoformat() if candidate.stage4c_date else "",
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "alignment_hint": candidate.alignment_hint,
                "price_validation_status": candidate.price_validation_status,
                "production_input": "false",
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round46_stage_date_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND46_SCORE_TARGETS:
        rows.append(
            {
                "target_id": target.target_id,
                "stage1": "|".join(target.stage1_signals),
                "stage2": "|".join(target.stage2_signals),
                "stage3": "|".join(target.stage3_conditions),
                "stage4b": "|".join(target.stage4b_conditions),
                "stage4c": "|".join(target.stage4c_conditions),
                "production_scoring_changed": "false",
            }
        )
    return tuple(rows)


def round46_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round46_backfill": "true"} for field in ROUND46_PRICE_FIELDS)


def round46_summary() -> dict[str, int | bool]:
    records = round46_case_records()
    return {
        "target_count": len(ROUND46_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch"),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND46_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND46_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND46_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round46_r6_reports(
    *,
    output_directory: str | Path = ROUND46_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND46_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND46_DEFAULT_SCORE_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = Path(cases_path)
    score_profiles = Path(score_profile_path)
    cases.parent.mkdir(parents=True, exist_ok=True)
    score_profiles.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "score_profiles": score_profiles,
        "summary": output / "round46_r6_financial_capital_digital_summary.md",
        "case_matrix": output / "round46_r6_case_matrix.csv",
        "stage_date_plan": output / "round46_r6_stage_date_plan.csv",
        "green_guardrails": output / "round46_r6_green_guardrails.md",
        "price_validation_plan": output / "round46_r6_price_validation_plan.md",
        "price_fields": output / "round46_r6_price_fields.csv",
    }
    _write_case_jsonl(round46_case_records(), cases)
    _write_rows(round46_score_profile_rows(), score_profiles)
    _write_rows(round46_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round46_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round46_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round46_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round46_green_guardrail_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round46_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round46_summary_markdown() -> str:
    summary = round46_summary()
    lines = [
        "# Round-46 R6 Financial / Capital Allocation / Digital Finance Summary",
        "",
        f"- source_round: `{ROUND46_SOURCE_ROUND_PATH}`",
        "- large_sector: `FINANCIAL_CAPITAL_DIGITAL`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R6 should separate true discount removal from low-PBR, index-inclusion, buyback-only, and tokenization headlines.",
        "- Example: SK Square is higher quality because NAV discount, cancellation, and governance improvement appear together.",
        "- Example: Samsung Electronics buyback created price support, but business/EPS path remains a separate gate.",
        "- Example: stablecoin/STO remains Watch until regulation, reserves, convertibility, volume, and fee model are proven.",
    ]
    return "\n".join(lines) + "\n"


def render_round46_green_guardrail_markdown() -> str:
    lines = [
        "# Round-46 R6 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Red flags |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND46_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.red_flags)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these R6 v1.0 weights to production scoring yet.",
            "- Do not treat low PBR, high dividend yield, value-up index inclusion, buyback headline, user count, stablecoin/STO headline, or IPO valuation as score evidence by themselves.",
            "- Do not invent ROE, CET1, K-ICS, credit cost, PF exposure, buyback cancellation, payment volume, take rate, reserve ratio, transaction volume, or price-path fields.",
            "- Do not lower Stage 3-Green for value-up or fintech stories. Green requires executed capital return, quality balance sheet, recurring revenue, or regulated financial infrastructure evidence.",
            "- Treat activist rejection, buyback without cancellation, governance battle, debt jump, tax shock, de-peg, convertibility risk, fraud, and reserve failure as RedTeam evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round46_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-46 R6 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Calculate peak price, drawdown after peak, and below-stage3 flag.",
        "6. Compare price paths with ROE, PBR, CET1, K-ICS, CSM, loss ratio, credit cost, dividends, buybacks, trading value, take rate, and stablecoin volume/reserves.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | stage candidate | check |",
        "| --- | --- | --- |",
    ]
    priority = {
        "korean_financial_holdings_valueup_case",
        "samsung_ct_activist_rejection_case",
        "terrausd_do_kwon_collapse_case",
    }
    for row in round46_case_candidate_rows():
        if row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or row["case_id"] in priority:
            stage_date = row["stage2_date"] or row["stage4b_date"] or row["stage4c_date"] or "needs_source_date"
            lines.append(f"| `{row['case_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `aligned`: ROE/PBR/shareholder return or transaction economics move with price rerating.",
            "- `policy_rerating`: policy changes rerate the sector, but company execution still needs verification.",
            "- `buyback_only_rebound`: buyback lifts price without business or ROE change.",
            "- `event_premium`: tender, control battle, IPO, or policy event moves price before core economics are proven.",
            "- `false_positive_score`: low PBR or value-up label exists but cancellation, dividend, or ROE improvement is missing.",
            "- `thesis_break`: governance failure, de-peg, stablecoin run, tax shock, or credit-cost spike breaks the thesis.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round46CaseCandidate) -> str:
    if "aligned" in candidate.alignment_hint and candidate.case_type in {"structural_success", "success_candidate"}:
        return "aligned"
    if candidate.case_type in {"event_premium", "overheat", "4b_watch"}:
        return "price_moved_without_evidence"
    if candidate.case_type in {"failed_rerating", "4c_thesis_break"}:
        return "false_positive_score"
    return "unknown"


def _rerating_result(candidate: Round46CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "event_premium":
        return "event_premium"
    if candidate.case_type == "overheat":
        return "theme_overheat"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    if candidate.case_type == "failed_rerating":
        return "no_rerating"
    if "policy" in candidate.alignment_hint:
        return "policy_event_rerating"
    return "unknown"


def _write_case_jsonl(records: Iterable[E2RCaseRecord], path: Path) -> Path:
    lines = []
    for record in records:
        record.validate()
        lines.append(json.dumps(record.as_dict(), ensure_ascii=False, sort_keys=True))
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return path


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    row_tuple = tuple(rows)
    if not row_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(row_tuple[0].keys()), lineterminator="\n")
        writer.writeheader()
        for row in row_tuple:
            writer.writerow(row)
    return path


__all__ = [
    "ROUND46_CASE_CANDIDATES",
    "ROUND46_DEFAULT_CASES_PATH",
    "ROUND46_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND46_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND46_PRICE_FIELDS",
    "ROUND46_SCORE_TARGETS",
    "ROUND46_SOURCE_ROUND_PATH",
    "Round46CaseCandidate",
    "Round46ScoreTarget",
    "Round46ScoreWeightDraft",
    "render_round46_green_guardrail_markdown",
    "render_round46_price_validation_plan_markdown",
    "render_round46_summary_markdown",
    "round46_case_candidate_rows",
    "round46_case_records",
    "round46_price_field_rows",
    "round46_score_profile_rows",
    "round46_stage_date_rows",
    "round46_summary",
    "target_for",
    "write_round46_r6_reports",
]
