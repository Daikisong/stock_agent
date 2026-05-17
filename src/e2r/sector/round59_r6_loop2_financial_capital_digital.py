"""Round-59 R6 Loop-2 financial, capital-allocation, and digital-finance pack.

Round 59 tightens the Round-46 financial sector pack. It separates low-PBR,
value-up, buyback, fintech, and stablecoin narratives from evidence that can
actually support E2R rerating: ROE, CET1, K-ICS, credit cost, executed
cancellations, dividends, take rate, FCF, reserve quality, and redemption.

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


ROUND59_SOURCE_ROUND_PATH = "docs/round/round_59.md"
ROUND59_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round59_r6_loop2_financial_capital_digital"
ROUND59_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_loop2_round59.jsonl"
ROUND59_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round59_r6_loop2_v2.csv"


@dataclass(frozen=True)
class Round59ScoreWeightDraft:
    eps_fcf: int | str
    structural_visibility: int | str
    bottleneck_pricing: int | str
    market_mispricing: int | str
    valuation: int | str
    capital_allocation: int | str
    information_confidence: int | str

    def as_dict(self) -> dict[str, int | str]:
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
class Round59ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round59ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop2_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round59CaseCandidate:
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


GATE_WEIGHT = Round59ScoreWeightDraft("gate", "gate", "gate", "gate", "gate", "gate", "gate")


ROUND59_SCORE_TARGETS: tuple[Round59ScoreTarget, ...] = (
    Round59ScoreTarget(
        "FINANCIAL_SPREAD_BALANCE_SHEET",
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round59ScoreWeightDraft(15, 20, 5, 15, 25, 10, 5),
        ("korea_discount_policy", "dividend_tax_reform", "bank_pbr_rerating_news", "valueup_index_news"),
        ("roe_improvement", "cet1_stable", "credit_cost_down", "buyback_or_dividend_execution"),
        ("pbr_roe_frame_change", "recurring_return_policy", "roe_stable", "credit_risk_low"),
        ("financial_valueup_crowded", "pbr_band_above_history", "return_policy_fully_priced"),
        ("credit_cost_spike", "pf_loss", "cet1_deterioration", "shareholder_return_retreat", "tax_policy_shock"),
        ("roe", "cet1_ratio", "credit_cost", "pf_exposure_controlled", "shareholder_return_execution"),
        ("credit_cost", "pf_exposure", "cet1_deterioration", "return_policy_retreat", "tax_policy_shock"),
        ("credit_cost", "pf_exposure", "cet1", "tax_policy"),
        "Low PBR is Stage 1; Green needs ROE/PBR, CET1, credit cost, and executed return together.",
    ),
    Round59ScoreTarget(
        "INSURANCE_UNDERWRITING_CYCLE",
        E2RArchetype.INSURANCE_UNDERWRITING_CYCLE,
        Round10ThemePosture.GREEN_POSSIBLE,
        Round59ScoreWeightDraft(15, 21, 4, 15, 25, 10, 5),
        ("loss_ratio_improvement", "csm_growth", "valueup_insurance_news"),
        ("roe_improvement", "k_ics_stable", "dividend_or_buyback_execution", "csm_growth"),
        ("pbr_roe_rerating", "repeat_underwriting_quality", "capital_ratio_stable", "return_policy_repeatable"),
        ("insurance_valueup_crowded", "pbr_normalized", "dividend_yield_chasing"),
        ("loss_ratio_worse", "k_ics_deterioration", "alternative_investment_loss", "cyber_operational_risk"),
        ("roe", "k_ics_ratio", "csm_growth", "loss_ratio", "shareholder_return_execution"),
        ("loss_ratio", "k_ics_deterioration", "operational_risk", "investment_loss"),
        ("loss_ratio", "k_ics", "investment_loss", "operational_risk"),
        "Insurance Green needs underwriting quality, capital, and repeatable return policy, not yield alone.",
    ),
    Round59ScoreTarget(
        "SECURITIES_BROKERAGE_CYCLE",
        E2RArchetype.SECURITIES_BROKERAGE_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round59ScoreWeightDraft(18, 13, 5, 14, 17, 7, 5),
        ("trading_value_growth", "market_rally", "ipo_ib_recovery_expectation"),
        ("brokerage_revenue_growth", "ib_fee_growth", "op_eps_revision"),
        ("pf_risk_low", "roe_structure_improved", "ib_pipeline_durable"),
        ("brokerage_cycle_peak", "securities_group_overheated", "trading_value_peak"),
        ("tax_policy_shock", "trading_value_drop", "pf_loss", "proprietary_trading_loss"),
        ("trading_value", "ib_fee_revenue", "pf_risk_low", "roe_improvement"),
        ("tax_policy_shock", "trading_value_drop", "pf_loss", "proprietary_loss"),
        ("trading_value", "tax_policy", "pf_loss", "proprietary_loss"),
        "Brokerage is cycle/watch unless trading value, IB, PF risk, and ROE structure all support durability.",
    ),
    Round59ScoreTarget(
        "VALUE_UP_SHAREHOLDER_RETURN",
        E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round59ScoreWeightDraft(12, 19, 4, 20, 25, 11, 5),
        ("commercial_act_revision", "dividend_tax_reform", "valueup_index", "buyback_policy_news"),
        ("treasury_share_cancellation", "dividend_growth", "roe_improvement", "shareholder_return_execution"),
        ("pbr_nav_discount_narrows", "repeat_return_policy", "capital_allocation_execution", "pbr_roe_band_shift"),
        ("valueup_crowded_trade", "pbr_band_rerated_before_execution"),
        ("no_cancellation", "activist_rejection", "capital_allocation_retreat", "controlling_shareholder_risk"),
        ("buyback_cancelled", "dividend_growth", "roe_improvement", "minority_shareholder_protection"),
        ("no_cancellation", "execution_failure", "low_roe", "controlling_shareholder_risk", "buyback_only"),
        ("execution_failure", "buyback_only", "low_roe", "policy_only"),
        "Value-up is Green only when policy becomes executed cancellation, dividends, ROE, and governance improvement.",
    ),
    Round59ScoreTarget(
        "HOLDING_RESTRUCTURING_GOVERNANCE",
        E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round59ScoreWeightDraft(12, 18, 4, 22, 24, 11, 5),
        ("nav_discount", "subsidiary_value_gap", "activist_or_buyback_news"),
        ("buyback_cancel", "independent_director", "dividend_policy", "governance_improvement"),
        ("nav_discount_narrows", "repeat_capital_return", "minority_protection", "subsidiary_value_supported"),
        ("holding_valueup_crowded", "event_premium_fully_priced"),
        ("activist_rejection", "governance_battle", "debt_ratio_jump", "subsidiary_value_impairment", "share_issuance_defense"),
        ("nav_discount", "actual_cancellation", "governance_improvement", "capital_structure_stable"),
        ("governance_battle", "event_premium", "debt_ratio_jump", "minority_conflict", "share_issuance_defense"),
        ("event_premium", "governance_battle", "share_issuance", "debt_ratio_jump"),
        "Holding rerating needs NAV discount plus actual governance and capital-allocation execution.",
    ),
    Round59ScoreTarget(
        "PAYMENT_FINTECH_INFRA",
        E2RArchetype.PAYMENT_FINTECH_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round59ScoreWeightDraft(18, 20, 8, 14, 14, 2, 5),
        ("active_users_growth", "global_expansion", "payment_remittance_finance_service"),
        ("payment_volume", "take_rate", "financial_service_attach", "profit_or_fcf"),
        ("repeat_financial_infra_revenue", "regulatory_stability", "security_clean", "credit_loss_control"),
        ("ipo_valuation_overheated", "user_count_story_crowded"),
        ("security_incident", "credit_loss_rate_up", "take_rate_pressure", "regulatory_sanction"),
        ("payment_volume", "take_rate", "attach_rate", "profit_fcf", "regulation_security_clean"),
        ("take_rate_pressure", "security_incident", "credit_loss", "regulatory_sanction", "user_count_only"),
        ("take_rate", "fcf", "security", "credit_loss", "ipo_valuation"),
        "Payment fintech needs transaction economics and FCF; user count is routing context, not Green evidence.",
    ),
    Round59ScoreTarget(
        "DIGITAL_ASSET_TOKENIZATION",
        E2RArchetype.DIGITAL_ASSET_TOKENIZATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round59ScoreWeightDraft(16, 18, 8, 16, 12, 3, 5),
        ("stablecoin_sto_bill", "tokenization_business_entry", "partnership_news"),
        ("regulatory_approval", "issued_amount", "transaction_volume", "fee_model", "reserve_disclosure"),
        ("payment_custody_settlement_infra", "repeat_revenue", "reserve_transparency", "convertibility_clear"),
        ("stablecoin_law_expectation_crowded", "sto_theme_rally"),
        ("depeg", "convertibility_failure", "reserve_problem", "regulatory_rejection", "fraud"),
        ("regulatory_approval", "reserve_transparency", "redemption_capacity", "transaction_volume", "fee_model"),
        ("depeg", "reserve_opacity", "convertibility_risk", "fraud", "regulatory_rejection"),
        ("reserve", "convertibility", "regulated_revenue", "fee_model"),
        "Digital-asset Green is blocked until regulated volume, fee model, reserve, and convertibility are proven.",
    ),
    Round59ScoreTarget(
        "CREDIT_DATA_INFRA",
        E2RArchetype.CREDIT_DATA_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        Round59ScoreWeightDraft(17, 19, 7, 13, 12, 1, 5),
        ("credit_data_contract", "financial_data_infra", "customer_growth"),
        ("recurring_financial_institution_contract", "data_revenue_growth", "opm_improvement"),
        ("repeat_data_revenue", "regulatory_clean", "customer_diversification"),
        ("credit_data_story_crowded",),
        ("privacy_breach", "regulatory_sanction", "customer_concentration", "contract_loss"),
        ("recurring_contracts", "data_revenue", "regulatory_clean", "customer_diversification"),
        ("privacy_breach", "regulation", "customer_concentration"),
        ("privacy", "regulation", "customer_concentration"),
        "Credit-data infra needs recurring contracts and clean privacy/regulatory record.",
    ),
    Round59ScoreTarget(
        "VC_EXIT_MARKET_CYCLE",
        E2RArchetype.VC_EXIT_MARKET_CYCLE,
        Round10ThemePosture.REDTEAM_FIRST,
        Round59ScoreWeightDraft(15, 10, 4, 12, 9, 2, 5),
        ("ipo_market_reopen", "venture_exit_expectation", "valuation_rebound"),
        ("exit_volume", "realized_gain", "fundraising_recovery"),
        ("repeat_exit_market", "portfolio_quality", "cash_return"),
        ("vc_exit_cycle_crowded",),
        ("ipo_market_slowdown", "valuation_loss", "funding_market_freeze"),
        ("exit_volume", "realized_gain", "cash_return"),
        ("ipo_slowdown", "valuation_loss", "funding_freeze"),
        ("ipo_cycle", "valuation_loss", "funding_freeze"),
        "VC/exit market is cycle-heavy and stays RedTeam-first until realized exits and cash returns are visible.",
    ),
    Round59ScoreTarget(
        "DIGITAL_ASSET_THEME_OVERHEAT",
        E2RArchetype.DIGITAL_ASSET_THEME_OVERHEAT,
        Round10ThemePosture.REDTEAM_FIRST,
        Round59ScoreWeightDraft(5, 5, 5, 6, 5, 0, 3),
        ("nft_coin_theme", "blockchain_keyword", "algorithmic_stablecoin_story"),
        ("regulated_revenue", "license_or_partner", "cash_flow"),
        ("legal_recurring_revenue", "reserve_and_redemption_proven", "low_regulatory_risk"),
        ("digital_asset_theme_overheated",),
        ("depeg", "run", "reserve_failure", "fraud", "market_manipulation", "no_revenue"),
        ("regulated_revenue", "reserve_transparency", "cash_flow"),
        ("depeg", "reserve_failure", "fraud", "theme_only", "no_revenue"),
        ("theme_only", "no_revenue", "depeg", "fraud"),
        "Digital-asset themes are Green-blocked without regulated revenue, reserve proof, and cash flow.",
    ),
    Round59ScoreTarget(
        "GOVERNANCE_EXECUTION_FAILURE_OVERLAY",
        E2RArchetype.GOVERNANCE_EXECUTION_FAILURE_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("activist_proposal_rejection", "buyback_without_cancellation", "controlling_shareholder_defense"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("activist_rejection", "minority_shareholder_protection_failure", "share_issuance_defense", "governance_discount_persists"),
        (),
        ("activist_rejection", "no_cancellation", "minority_shareholder_protection_failure", "controlling_shareholder_risk"),
        ("governance_execution", "minority_protection", "capital_structure"),
        "Governance execution failure is a RedTeam overlay, not a positive score bucket.",
        gate_only=True,
    ),
    Round59ScoreTarget(
        "TAX_POLICY_MARKET_SHOCK_OVERLAY",
        E2RArchetype.TAX_POLICY_MARKET_SHOCK_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("transaction_tax_hike", "capital_gains_tax_threshold_change", "corporate_tax_hike"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("trading_value_drop", "tax_policy_shock", "dividend_tax_uncertainty", "market_sentiment_collapse"),
        (),
        ("transaction_tax_change", "capital_gains_tax_change", "corporate_tax_change", "trading_value_drop"),
        ("tax_policy", "trading_value", "macro_sentiment"),
        "Tax policy shock is a RedTeam overlay for brokerage, value-up, and crowded market rallies.",
        gate_only=True,
    ),
    Round59ScoreTarget(
        "STABLECOIN_CONVERTIBILITY_OVERLAY",
        E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        ("stablecoin_convertibility_warning", "reserve_mismatch", "redemption_not_at_par"),
        ("risk_event_detected",),
        ("not_applicable_gate_only",),
        ("not_applicable_gate_only",),
        ("depeg", "convertibility_failure", "reserve_failure", "liquidity_run", "algorithmic_stablecoin_failure"),
        (),
        ("reserve_mismatch", "redemption_not_at_par", "convertibility_risk", "run_risk"),
        ("reserve", "convertibility", "depeg", "algorithmic"),
        "Stablecoin convertibility is a RedTeam overlay; issuance news is not regulated fee revenue.",
        gate_only=True,
    ),
)


ROUND59_CASE_CANDIDATES: tuple[Round59CaseCandidate, ...] = (
    Round59CaseCandidate(
        "korea_commercial_act_treasury_cancel_case",
        "VALUE_UP_SHAREHOLDER_RETURN",
        "KOSPI_VALUEUP_POLICY_REF",
        "Korea Commercial Act treasury cancellation reform",
        "KR",
        "success_candidate",
        None,
        date(2026, 2, 25),
        None,
        None,
        None,
        ("commercial_act_revision", "treasury_share_cancel_deadline", "minority_shareholder_protection", "korea_discount_policy"),
        ("policy_expectation_only", "individual_execution_not_verified", "crowded_trade"),
        "macro_valueup_policy_aligned",
        "missing_direct_symbol_mapping",
        ("round_59.md Reuters commercial act treasury cancellation",),
        "Macro value-up policy can help Stage 1/2 routing, but company-level Green still needs actual cancellation, ROE, and FCF.",
    ),
    Round59CaseCandidate(
        "sk_square_buyback_cancel_case",
        "HOLDING_RESTRUCTURING_GOVERNANCE",
        "402340",
        "SK Square buyback cancellation and governance execution",
        "KR",
        "success_candidate",
        None,
        date(2024, 11, 21),
        None,
        None,
        None,
        ("nav_discount", "buyback_cancel", "additional_buyback", "independent_director", "activist_engagement"),
        ("subsidiary_price_dependency", "holding_discount_persistence", "cancellation_scale_insufficient"),
        "holding_nav_discount_reduction",
        "needs_price_backfill",
        ("round_59.md Reuters SK Square buybacks",),
        "NAV discount plus executed cancellation and independent director evidence makes this a higher-quality value-up candidate.",
    ),
    Round59CaseCandidate(
        "samsung_electronics_buyback_case",
        "VALUE_UP_SHAREHOLDER_RETURN",
        "005930",
        "Samsung Electronics buyback rebound",
        "KR",
        "event_premium",
        None,
        date(2024, 11, 15),
        None,
        None,
        None,
        ("buyback_amount", "day_price_reaction", "partial_cancellation"),
        ("buyback_only", "business_thesis_weakness", "hbm_competition_risk", "roe_fcf_path_unverified"),
        "buyback_only_rebound",
        "needs_price_backfill",
        ("round_59.md Investopedia Samsung buyback",),
        "Buyback can create a rebound, but business competitiveness and EPS/FCF path remain separate gates.",
        (E2RArchetype.MEMORY_HBM_CAPACITY,),
    ),
    Round59CaseCandidate(
        "samsung_electronics_treasury_cancel_case",
        "VALUE_UP_SHAREHOLDER_RETURN",
        "005930",
        "Samsung Electronics treasury-share cancellation mixed case",
        "KR",
        "event_premium",
        None,
        date(2026, 3, 31),
        None,
        None,
        None,
        ("treasury_share_cancel_amount", "shareholder_return_policy"),
        ("business_thesis_weakness", "price_down_on_event", "hbm_competition_risk"),
        "buyback_aligned_but_business_risk_remains",
        "needs_price_backfill",
        ("round_59.md Reuters Samsung treasury cancellation",),
        "Cancellation improves capital allocation quality, but the source reports negative price reaction and business risk remains.",
        (E2RArchetype.MEMORY_HBM_CAPACITY,),
    ),
    Round59CaseCandidate(
        "samsung_ct_activist_rejection_case",
        "GOVERNANCE_EXECUTION_FAILURE_OVERLAY",
        "028260",
        "Samsung C&T activist proposal rejection",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("nav_discount", "activist_campaign", "low_pbr"),
        ("activist_rejection", "capital_allocation_retreat", "minority_shareholder_protection_failure", "controlling_shareholder_risk"),
        "governance_execution_failure_4c_watch",
        "needs_source_date_and_price_backfill",
        ("round_59.md Financial Times Samsung C&T activist rejection",),
        "The round gives year-level timing and price reaction only, so no exact stage date is invented.",
        (E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,),
    ),
    Round59CaseCandidate(
        "korea_zinc_tender_offer_event_case",
        "HOLDING_RESTRUCTURING_GOVERNANCE",
        "010130",
        "Korea Zinc tender offer event premium",
        "KR",
        "event_premium",
        None,
        date(2024, 9, 13),
        None,
        None,
        None,
        ("tender_offer_flag", "governance_event_flag", "day_price_reaction"),
        ("event_premium", "hostile_takeover", "control_battle", "fcf_not_verified"),
        "event_premium_not_valueup",
        "needs_price_backfill",
        ("round_59.md Reuters Korea Zinc tender offer",),
        "Tender offer price reaction is event premium first; it must not be misclassified as structural value-up.",
    ),
    Round59CaseCandidate(
        "korea_zinc_buyback_court_case",
        "HOLDING_RESTRUCTURING_GOVERNANCE",
        "010130",
        "Korea Zinc buyback court decision event",
        "KR",
        "event_premium",
        None,
        date(2024, 10, 21),
        None,
        None,
        None,
        ("buyback_offer", "court_decision", "governance_event_flag", "day_price_reaction"),
        ("governance_battle", "debt_ratio_jump", "event_premium", "minority_conflict"),
        "event_premium_not_valueup",
        "needs_price_backfill",
        ("round_59.md Reuters Korea Zinc court buyback",),
        "Court-cleared buyback can move price, but debt and control-battle risk keep it outside structural Green.",
    ),
    Round59CaseCandidate(
        "korea_zinc_share_issue_probe_case",
        "GOVERNANCE_EXECUTION_FAILURE_OVERLAY",
        "010130",
        "Korea Zinc share issuance probe",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 10, 31),
        ("share_issuance_flag", "governance_event_flag", "capital_structure_risk_flag"),
        ("share_issuance_defense", "market_watchdog_probe", "minority_shareholder_harm", "capital_structure_deterioration"),
        "capital_structure_governance_4c_watch",
        "needs_price_backfill",
        ("round_59.md Reuters Korea Zinc share issuance probe",),
        "Share issuance after tender battle is a governance/capital-structure RedTeam event.",
        (E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,),
    ),
    Round59CaseCandidate(
        "korea_tax_policy_shock_case",
        "TAX_POLICY_MARKET_SHOCK_OVERLAY",
        "KOSPI_TAX_SHOCK_REF",
        "Korea stock-market tax policy shock",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 8, 6),
        ("market_rally", "valueup_crowded_trade", "brokerage_cycle"),
        ("transaction_tax_change", "capital_gains_tax_change", "corporate_tax_change", "market_sentiment_collapse"),
        "tax_policy_shock",
        "missing_direct_symbol_mapping",
        ("round_59.md Reuters/MarketWatch Korea tax policy shock",),
        "Tax policy can break brokerage, value-up, and crowded market rallies through sentiment and trading-value pressure.",
        (E2RArchetype.SECURITIES_BROKERAGE_CYCLE,),
    ),
    Round59CaseCandidate(
        "ai_windfall_tax_comment_case",
        "TAX_POLICY_MARKET_SHOCK_OVERLAY",
        "KOSPI_AI_WINDFALL_TAX_REF",
        "AI windfall tax policy-comment shock",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 12),
        ("ai_market_rally", "crowded_trade", "policy_comment"),
        ("tax_policy_shock", "market_sentiment_collapse", "windfall_tax_comment", "trading_value_drop_risk"),
        "tax_policy_shock",
        "missing_direct_symbol_mapping",
        ("round_59.md MarketWatch AI windfall tax shock",),
        "Policy comments can create 4B/4C-watch in crowded AI and value-up markets.",
        (E2RArchetype.SECURITIES_BROKERAGE_CYCLE,),
    ),
    Round59CaseCandidate(
        "stripe_payment_infra_profit_case",
        "PAYMENT_FINTECH_INFRA",
        "STRIPE",
        "Stripe profitable payment infrastructure reference",
        "US",
        "success_candidate",
        None,
        date(2025, 2, 27),
        None,
        None,
        None,
        ("payment_volume", "merchant_count", "profit_or_fcf", "financial_process_automation"),
        ("private_company", "valuation_risk", "take_rate_pressure", "competition"),
        "payment_infra_profit_reference",
        "missing_public_price_data",
        ("round_59.md Reuters Stripe tender offer",),
        "Payment infrastructure gets stronger when profit/FCF and merchant lock-in are visible, not just users.",
    ),
    Round59CaseCandidate(
        "mynt_gcash_ipo_case",
        "PAYMENT_FINTECH_INFRA",
        "MYNT_GCASH_REF",
        "Mynt / GCash e-wallet financial platform",
        "PH",
        "success_candidate",
        None,
        date(2026, 5, 14),
        None,
        None,
        None,
        ("active_users", "bill_payment", "remittance", "financial_service_attach_rate", "ipo_valuation"),
        ("user_count_only", "take_rate_unverified", "credit_loss_unverified", "regulation"),
        "ewallet_financial_platform_reference",
        "missing_public_price_data",
        ("round_59.md Reuters Mynt GCash IPO",),
        "Large user base is useful, but take rate, attach, credit loss, security, and FCF remain required.",
    ),
    Round59CaseCandidate(
        "toss_global_stablecoin_case",
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
        ("regulatory_approval_missing", "stablecoin_volume_unverified", "valuation_risk", "fee_model_unverified"),
        "fintech_success_stablecoin_stage1_watch",
        "missing_public_price_data",
        ("round_59.md Reuters Toss global push won stablecoin",),
        "Toss fintech is a success candidate, while won stablecoin remains Watch before regulation, volume, reserve, and fees.",
        (E2RArchetype.DIGITAL_ASSET_TOKENIZATION,),
    ),
    Round59CaseCandidate(
        "boe_stablecoin_convertibility_case",
        "STABLECOIN_CONVERTIBILITY_OVERLAY",
        "STABLECOIN_CONVERTIBILITY_REF",
        "Bank of England stablecoin convertibility warning",
        "GLOBAL",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 8),
        ("stablecoin_cross_border_payment", "regulatory_standard"),
        ("convertibility_risk", "reserve_transparency_risk", "liquidity_run", "international_regulatory_conflict"),
        "stablecoin_convertibility_4c_watch",
        "missing_direct_symbol_mapping",
        ("round_59.md Reuters Bank of England stablecoin regulation",),
        "Fiat-backed stablecoin exposure still needs reserve, redemption, liquidity, and regulatory proof.",
        (E2RArchetype.DIGITAL_ASSET_TOKENIZATION,),
    ),
    Round59CaseCandidate(
        "terrausd_do_kwon_case",
        "STABLECOIN_CONVERTIBILITY_OVERLAY",
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
        ("depeg", "run", "reserve_failure", "fraud", "algorithmic_stablecoin_failure", "investor_loss"),
        "algorithmic_stablecoin_4c",
        "needs_source_date_and_price_backfill",
        ("round_59.md Reuters TerraUSD Do Kwon",),
        "The document gives a 2022~2025 range, so no exact stage date is invented.",
        (E2RArchetype.DIGITAL_ASSET_THEME_OVERHEAT,),
    ),
)


ROUND59_PRICE_FIELDS: tuple[str, ...] = (
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
    "peak_date",
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
    "below_stage2_price_flag",
    "below_stage3_price_flag",
    "roe",
    "roa",
    "pbr",
    "pbr_band_before",
    "pbr_band_after",
    "cet1_ratio",
    "k_ics_ratio",
    "csm_growth",
    "loss_ratio",
    "credit_cost",
    "pf_exposure",
    "npl_ratio",
    "dividend_payout_ratio",
    "dividend_growth",
    "dividend_per_share",
    "buyback_amount",
    "buyback_cancelled_flag",
    "treasury_share_cancel_amount",
    "treasury_share_cancel_deadline",
    "shareholder_return_policy",
    "shareholder_return_execution_flag",
    "nav_value",
    "nav_discount",
    "holding_company_discount",
    "subsidiary_stake_value",
    "asset_sale_flag",
    "independent_director_flag",
    "activist_campaign_flag",
    "minority_shareholder_protection_flag",
    "tender_offer_flag",
    "tender_offer_price",
    "governance_event_flag",
    "share_issuance_flag",
    "share_issuance_amount",
    "debt_to_equity_change",
    "capital_structure_risk_flag",
    "trading_value",
    "brokerage_revenue",
    "ib_fee_revenue",
    "ipo_pipeline_count",
    "vc_exit_volume",
    "proprietary_trading_gain_loss",
    "transaction_tax_change_flag",
    "capital_gains_tax_change_flag",
    "corporate_tax_change_flag",
    "payment_volume",
    "take_rate",
    "active_users",
    "merchant_count",
    "financial_service_attach_rate",
    "credit_loss_rate",
    "security_incident_flag",
    "stablecoin_issued_amount",
    "stablecoin_transaction_volume",
    "reserve_asset_type",
    "redemption_reserve_ratio",
    "convertibility_risk_flag",
    "regulatory_approval_flag",
    "depeg_event_flag",
    "algorithmic_stablecoin_flag",
    "score_price_alignment",
    "price_validation_status",
    "review_notes",
)


def target_for(target_id: str) -> Round59ScoreTarget | None:
    for target in ROUND59_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round59_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND59_CASE_CANDIDATES:
        target = target_for(candidate.target_id)
        if target is None:
            raise ValueError(f"unknown target_id: {candidate.target_id}")
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
                f"Round59 R6 Loop-2 case for {candidate.target_id}; "
                "policy, value-up, fintech, and stablecoin narratives are separated from executed evidence."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage2_signals or field in target.green_conditions),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if field in target.stage3_conditions),
            stage4b_evidence=stage4b_evidence,
            stage4c_evidence=stage4c_evidence,
            must_have_fields=target.green_conditions,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"failed_rerating", "event_premium", "overheat", "4b_watch", "4c_thesis_break", "one_off"}
                else None
            ),
            score_price_alignment=_score_price_alignment(candidate),
            rerating_result=_rerating_result(candidate),
            price_pattern=candidate.alignment_hint,
            score_weight_hint=_score_weight_hint(target),
            green_guardrails=(
                "do_not_use_case_as_candidate_input",
                "do_not_change_production_scoring",
                "require_price_path_validation",
                "require_cross_evidence_for_green",
                "low_pbr_or_policy_name_is_not_structural_evidence_alone",
                "buyback_is_not_cancellation",
                "valueup_index_is_stage1_not_execution",
                "fintech_user_count_is_not_take_rate_or_fcf",
                "stablecoin_news_is_not_regulated_revenue",
                "do_not_invent_roe_cet1_csm_buyback_cancel_take_rate_stablecoin_volume_or_stage_prices",
                *target.red_flags,
            ),
            notes=f"{candidate.notes} Sources: {', '.join(candidate.source_refs)}.",
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=bool(candidate.evidence_fields),
                report_data_available=False,
                price_data_available=False,
                stage_dates_confidence=0.75 if candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.2,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round59_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND59_SCORE_TARGETS:
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
                "loop2_penalty_axes": "|".join(target.loop2_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round59_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND59_CASE_CANDIDATES:
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


def round59_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "red_flags": "|".join(target.red_flags),
            "loop2_penalty_axes": "|".join(target.loop2_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND59_SCORE_TARGETS
    )


def round59_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round59_backfill": "true"} for field in ROUND59_PRICE_FIELDS)


def round59_summary() -> dict[str, int | bool]:
    records = round59_case_records()
    return {
        "target_count": len(ROUND59_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND59_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND59_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND59_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND59_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round59_r6_loop2_reports(
    *,
    output_directory: str | Path = ROUND59_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND59_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND59_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round59_r6_loop2_financial_capital_digital_summary.md",
        "case_matrix": output / "round59_r6_loop2_case_matrix.csv",
        "stage_date_plan": output / "round59_r6_loop2_stage_date_plan.csv",
        "green_guardrails": output / "round59_r6_loop2_green_guardrails.md",
        "risk_overlays": output / "round59_r6_loop2_risk_overlays.md",
        "price_validation_plan": output / "round59_r6_loop2_price_validation_plan.md",
        "price_fields": output / "round59_r6_loop2_price_fields.csv",
    }
    _write_case_jsonl(round59_case_records(), cases)
    _write_rows(round59_score_profile_rows(), score_profiles)
    _write_rows(round59_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round59_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round59_price_field_rows(), paths["price_fields"])
    paths["summary"].write_text(render_round59_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round59_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round59_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round59_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def render_round59_summary_markdown() -> str:
    summary = round59_summary()
    lines = [
        "# Round-59 R6 Loop-2 Financial / Capital / Digital Summary",
        "",
        f"- source_round: `{ROUND59_SOURCE_ROUND_PATH}`",
        "- large_sector: `FINANCIAL_CAPITAL_DIGITAL`",
        "- loop: `R6 Loop 2 / v2.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- stage4b_case_count: {summary['stage4b_case_count']}",
        f"- stage4c_case_count: {summary['stage4c_case_count']}",
        f"- green_possible_count: {summary['green_possible_count']}",
        f"- watch_yellow_first_count: {summary['watch_yellow_first_count']}",
        f"- redteam_first_count: {summary['redteam_first_count']}",
        f"- gate_only_target_count: {summary['gate_only_target_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- R6 Loop 2 says low PBR and value-up policy are not enough; execution decides.",
        "- Example: buyback is useful, but cancellation plus ROE/FCF path is stronger evidence.",
        "- Example: Korea Zinc tender events are event premium first, not structural value-up.",
        "- Example: fintech user count is Stage 1 unless take rate, FCF, security, and credit loss are visible.",
        "- Example: stablecoin news is blocked from Green until reserve, redemption, regulation, volume, and fee model are proven.",
    ]
    return "\n".join(lines) + "\n"


def render_round59_green_guardrail_markdown() -> str:
    lines = [
        "# Round-59 R6 Loop-2 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-2 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND59_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions)} | {', '.join(target.loop2_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R6 Loop-2 v2.0 weights to production scoring yet.",
            "- Do not treat low PBR, value-up index inclusion, buyback announcement, user count, or stablecoin law news as Green evidence by themselves.",
            "- Do not equate buyback with cancellation.",
            "- Do not invent ROE, CET1, K-ICS, CSM, cancellation amount, take rate, FCF, reserve ratio, stablecoin volume, or stage prices.",
            "- Treat governance execution failure, tax policy shock, and stablecoin convertibility failure as RedTeam overlays.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round59_risk_overlay_markdown() -> str:
    lines = [
        "# Round-59 R6 Loop-2 Risk Overlays",
        "",
        "- `VALUEUP_EXECUTION_ALIGNED`: actual cancellation, dividend, ROE, and price rerating move together.",
        "- `BUYBACK_ONLY_REBOUND`: buyback creates a rebound, but business and ROE/FCF evidence is missing.",
        "- `HOLDING_NAV_DISCOUNT_REDUCTION`: NAV discount narrows with actual cancellation, governance, or asset-value action.",
        "- `EVENT_PREMIUM_NOT_VALUEUP`: tender offer, control battle, or defense buyback is not structural value-up.",
        "- `TAX_POLICY_SHOCK`: transaction, capital-gains, corporate, or dividend tax change damages the price path.",
        "- `FINTECH_USER_GROWTH_NO_FCF`: users grow but take rate, FCF, security, and credit loss are unverified.",
        "- `REGULATED_STABLECOIN_INFRA`: approval, reserve, redemption, volume, and fees are visible.",
        "- `ALGORITHMIC_STABLECOIN_4C`: de-peg, reserve failure, algorithmic design, or fraud is a hard thesis break.",
        "",
        "Simple example: `밸류업 지수 편입` is Stage 1. `자사주 실제 소각 + ROE 개선 + PBR band 변화` can support Stage 2/3 review.",
    ]
    return "\n".join(lines) + "\n"


def render_round59_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-59 R6 Loop-2 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare ROE, PBR, CET1, K-ICS, CSM, credit cost, dividends, cancellation, NAV, take rate, FCF, reserve, and redemption with price path.",
        "6. Mark governance failure, event premium, tax shock, stablecoin convertibility, and algorithmic stablecoin failure explicitly.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round59_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `VALUEUP_EXECUTION_ALIGNED`: actual cancellation, dividend, ROE, and price path align.",
            "- `BUYBACK_ONLY_REBOUND`: buyback-driven rebound without business or ROE/FCF confirmation.",
            "- `HOLDING_NAV_DISCOUNT_REDUCTION`: NAV discount reduction follows capital allocation or governance execution.",
            "- `EVENT_PREMIUM_NOT_VALUEUP`: control premium or tender event is not structural rerating.",
            "- `TAX_POLICY_SHOCK`: tax policy damages value-up or brokerage momentum.",
            "- `FINTECH_USER_GROWTH_NO_FCF`: user growth exists, economics are still missing.",
            "- `REGULATED_STABLECOIN_INFRA`: regulated reserve/redemption/volume/fees are proven.",
            "- `ALGORITHMIC_STABLECOIN_4C`: algorithmic de-peg or reserve failure is hard 4C.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round59CaseCandidate) -> str:
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "event_premium":
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    if candidate.case_type in {"structural_success", "success_candidate", "cyclical_success"}:
        return "aligned"
    return "unknown"


def _rerating_result(candidate: Round59CaseCandidate) -> str:
    if candidate.case_type == "structural_success":
        return "true_rerating"
    if candidate.case_type == "cyclical_success":
        return "cyclical_rerating"
    if candidate.case_type == "event_premium":
        return "event_premium"
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "theme_overheat"
    if candidate.case_type == "4c_thesis_break":
        return "thesis_break"
    return "unknown" if candidate.case_type == "success_candidate" else "no_rerating"


def _score_weight_hint(target: Round59ScoreTarget) -> dict[str, float]:
    weights = target.score_weight.as_dict()
    return {
        "eps_fcf": _numeric_weight(weights["eps_fcf"]),
        "visibility": _numeric_weight(weights["structural_visibility"]),
        "bottleneck": _numeric_weight(weights["bottleneck_pricing"]),
        "mispricing": _numeric_weight(weights["market_mispricing"]),
        "valuation": _numeric_weight(weights["valuation"]),
        "capital_allocation": _numeric_weight(weights["capital_allocation"]),
    }


def _numeric_weight(value: int | str) -> float:
    if isinstance(value, int):
        return float(value)
    return 0.0


def _write_case_jsonl(records: Iterable[E2RCaseRecord], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(record.as_dict(), ensure_ascii=False, sort_keys=True) for record in records]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return path


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    rows_tuple = tuple(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows_tuple[0].keys()))
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow(dict(row))
    return path


__all__ = [
    "ROUND59_CASE_CANDIDATES",
    "ROUND59_DEFAULT_CASES_PATH",
    "ROUND59_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND59_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND59_PRICE_FIELDS",
    "ROUND59_SCORE_TARGETS",
    "Round59CaseCandidate",
    "Round59ScoreTarget",
    "Round59ScoreWeightDraft",
    "render_round59_green_guardrail_markdown",
    "render_round59_price_validation_plan_markdown",
    "render_round59_risk_overlay_markdown",
    "render_round59_summary_markdown",
    "round59_case_candidate_rows",
    "round59_case_records",
    "round59_price_field_rows",
    "round59_score_profile_rows",
    "round59_stage_date_rows",
    "round59_summary",
    "target_for",
    "write_round59_r6_loop2_reports",
]
