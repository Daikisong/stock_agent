"""Round-138 R6 Loop-8 financial, capital-allocation, and digital-finance pack.

Round 138 separates cheapness from discount removal. Low PBR, value-up policy,
buyback plans, IPO hopes, stablecoin legislation, and exchange stakes are
routing evidence. Stage 3 needs ROE/PBR band change, repeated return execution,
credit-cost stability, capital ratios, regulated digital-finance economics, and
observed price-path alignment.

Simple example: `저PBR 은행주` is Stage 1. `ROE 개선 + CET1 안정 + 실제 소각
+ credit cost 안정 + PBR band 변화` can support Stage 2/3 review.

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


ROUND138_SOURCE_ROUND_PATH = "docs/round/round_138.md"
ROUND138_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round138_r6_loop8_financial_capital_digital"
ROUND138_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_loop8_round138.jsonl"
ROUND138_DEFAULT_SCORE_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round138_r6_loop8_v8.csv"


@dataclass(frozen=True)
class Round138ScoreWeightDraft:
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
class Round138ScoreTarget:
    target_id: str
    canonical_archetype: E2RArchetype
    posture: Round10ThemePosture
    score_weight: Round138ScoreWeightDraft
    stage1_signals: tuple[str, ...]
    stage2_signals: tuple[str, ...]
    stage3_conditions: tuple[str, ...]
    stage4b_conditions: tuple[str, ...]
    stage4c_conditions: tuple[str, ...]
    green_conditions: tuple[str, ...]
    red_flags: tuple[str, ...]
    loop8_penalty_axes: tuple[str, ...]
    normalization_point: str
    gate_only: bool = False

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.FINANCIAL_CAPITAL_DIGITAL

    @property
    def production_scoring_changed(self) -> bool:
        return False


@dataclass(frozen=True)
class Round138CaseCandidate:
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


@dataclass(frozen=True)
class Round138BaseScoreWeight:
    component: str
    weight: int
    interpretation: str


@dataclass(frozen=True)
class Round138StageCap:
    cap_id: str
    max_stage: str
    condition: str
    example: str


@dataclass(frozen=True)
class Round138ScoreStagePriceAlignment:
    case_id: str
    score_stage: str
    price_path_signal: str
    verdict: str
    normalization_adjustment: str


def _w(
    eps_fcf: int | str,
    visibility: int | str,
    bottleneck: int | str,
    mispricing: int | str,
    valuation: int | str,
    capital: int | str,
    confidence: int | str,
) -> Round138ScoreWeightDraft:
    return Round138ScoreWeightDraft(eps_fcf, visibility, bottleneck, mispricing, valuation, capital, confidence)


def _target(
    target_id: str,
    archetype: E2RArchetype,
    posture: Round10ThemePosture,
    weight: Round138ScoreWeightDraft,
    *,
    stage1: tuple[str, ...],
    stage2: tuple[str, ...],
    stage3: tuple[str, ...],
    stage4b: tuple[str, ...],
    stage4c: tuple[str, ...],
    green: tuple[str, ...],
    red: tuple[str, ...],
    penalties: tuple[str, ...],
    note: str,
    gate_only: bool = False,
) -> Round138ScoreTarget:
    return Round138ScoreTarget(
        target_id,
        archetype,
        posture,
        weight,
        stage1,
        stage2,
        stage3,
        stage4b,
        stage4c,
        green,
        red,
        penalties,
        note,
        gate_only,
    )


GATE_WEIGHT = _w("gate", "gate", "gate", "gate", "gate", "gate", "gate")


ROUND138_BASE_SCORE_WEIGHTS: tuple[Round138BaseScoreWeight, ...] = (
    Round138BaseScoreWeight(
        "roe_eps_fcf_durability",
        22,
        "Stage 3 needs ROE/EPS/FCF durability, not a low-PBR label.",
    ),
    Round138BaseScoreWeight(
        "capital_return_execution",
        18,
        "Actual cancellation, dividend expansion, and repeated return policy matter more than buyback plans.",
    ),
    Round138BaseScoreWeight(
        "capital_ratio_credit_cost_stability",
        18,
        "CET1, K-ICS, PF exposure, reserve build, and credit cost are hard gates for financial value-up.",
    ),
    Round138BaseScoreWeight(
        "regulated_revenue_model_visibility",
        14,
        "Stablecoin reserve/redemption, exchange fee/custody/tokenization, and fintech take rate need visible economics.",
    ),
    Round138BaseScoreWeight(
        "market_mispricing_rerating_gap",
        8,
        "The old low-PBR or non-bank discount frame must still be wrong after execution evidence appears.",
    ),
    Round138BaseScoreWeight(
        "valuation_room_4b_runway",
        8,
        "Korea value-up, Circle-style stablecoin IPO rallies, and exchange-stake narratives can become crowded 4B.",
    ),
    Round138BaseScoreWeight(
        "information_security_governance_confidence",
        12,
        "Governance execution, disclosure detail, exchange security, reserve design, and regulation are stronger Loop-8 hard gates.",
    ),
)


ROUND138_STAGE_CAPS: tuple[Round138StageCap, ...] = (
    Round138StageCap(
        "stage1_policy_or_label_only_cap",
        "Stage 1",
        "low PBR, value-up index inclusion, buyback expectation, stablecoin bill, IPO expectation, or exchange-stake rumor only",
        "Value-up policy headline or KRW stablecoin theme without company-level execution.",
    ),
    Round138StageCap(
        "stage2_execution_or_regulated_metric_cap",
        "Stage 2",
        "actual cancellation, dividend increase, stable CET1/K-ICS, stake acquisition, stablecoin circulation/reserve income, or IPO valuation filing",
        "SK Square cancellation plan, Hana-Dunamu stake, Circle USDC circulation/reserve income, or Commercial Act treasury mandate.",
    ),
    Round138StageCap(
        "stage3_durable_rerating_required",
        "Stage 3 candidate",
        "ROE/PBR band change, repeated returns, credit-cost stability, FCF/capital ratio durability, regulated revenue model, and price-path alignment",
        "Circle can be Stage 2~3 candidate only with reserve/redemption/revenue proof and 4B/regulatory-economics watch.",
    ),
    Round138StageCap(
        "stage4b_crowded_valueup_or_digital_finance",
        "4B-watch",
        "Korea value-up, stablecoin infrastructure, digital-asset exchange exposure, or capital-return expectation is broadly accepted and priced first",
        "Circle trades more than 3x IPO price or value-up PBR bands already rerate before execution.",
    ),
    Round138StageCap(
        "stage4c_hard_redteam",
        "4C",
        "PF credit-cost spike, activist rejection, buyback cancel with business failure, IPO valuation cut, exchange hack, de-peg/reserve failure, or tax shock",
        "Samsung C&T activist rejection, Clear Street IPO cut, Bybit hack, TerraUSD/Luna collapse, or BoE reserve-rule margin squeeze.",
    ),
)


ROUND138_SCORE_STAGE_PRICE_ALIGNMENT: tuple[Round138ScoreStagePriceAlignment, ...] = (
    Round138ScoreStagePriceAlignment(
        "korea_commercial_act_treasury_cancel_case",
        "Stage 1~2 macro tailwind",
        "Korea value-up policy tailwind; individual stock Green not proven",
        "policy direction is useful but not company-level Stage 3",
        "add macro policy credit; require individual cancellation, ROE/PBR, credit/capital stability for Stage 3",
    ),
    Round138ScoreStagePriceAlignment(
        "sk_square_buyback_cancel_case",
        "Stage 2",
        "NAV discount, actual cancellation, additional buyback/cancel plan, independent director",
        "execution evidence is strong; OHLCV backfill still required",
        "raise NAV discount plus actual cancellation plus governance execution credit",
    ),
    Round138ScoreStagePriceAlignment(
        "samsung_electronics_treasury_cancel_case",
        "Stage 2 failed rerating",
        "treasury cancellation announced; event-day price reportedly -5.2%",
        "buyback/cancellation-only false positive was correctly exposed",
        "strengthen business EPS/FCF, ROE/PBR, and execution-quality gate after cancellation",
    ),
    Round138ScoreStagePriceAlignment(
        "hana_bank_dunamu_stake_case",
        "Stage 2",
        "Hana Bank 6.55% Dunamu stake and Upbit market-share visibility",
        "digital-asset stake visibility improved, but Stage 3 income is unproven",
        "raise bank digital-asset stake visibility; cap Stage 3 until equity-method income, collaboration revenue, regulation, and security pass",
    ),
    Round138ScoreStagePriceAlignment(
        "circle_usdc_stablecoin_earnings_case",
        "Stage 2~3 candidate + 4B-watch",
        "reserve income/circulation grew; shares up after earnings and more than 3x IPO price",
        "regulated stablecoin structure was captured and 4B risk is high",
        "raise regulated stablecoin infra credit; strengthen valuation, rate, issuer-margin, redemption, and regulation gates",
    ),
    Round138ScoreStagePriceAlignment(
        "samsung_ct_activist_rejection_case",
        "4C-watch",
        "activist proposal rejection followed by roughly -10% price path in cited source",
        "governance execution gate matched the failure",
        "strengthen activist rejection, minority protection, no-cancellation, and controlling-shareholder penalties",
    ),
    Round138ScoreStagePriceAlignment(
        "korea_pf_credit_cost_overlay_case",
        "sector hard cap",
        "PF delinquency rose to 2.70%; bank/insurance support facilities were needed",
        "PF and credit cost are hard gates for value-up",
        "raise credit-cost/PF penalty and require CET1/K-ICS/reserve stability before Green",
    ),
    Round138ScoreStagePriceAlignment(
        "clear_street_ipo_valuation_cut_case",
        "4C-watch",
        "IPO size cut by 65%; valuation target reduced from about $11.8B to $7.2B",
        "fintech IPO optionality cap matched the business path",
        "strengthen IPO valuation, market-window, crypto-exposure, take-rate, and FCF gates",
    ),
    Round138ScoreStagePriceAlignment(
        "bybit_exchange_hack_case",
        "hard 4C",
        "$1.5B exchange hack attributed by FBI to North Korea",
        "exchange security gate must dominate exchange market-share stories",
        "add operational security hard gate for digital-asset exchange and bank stake exposure",
    ),
    Round138ScoreStagePriceAlignment(
        "terrausd_do_kwon_case",
        "hard 4C",
        "$40B algorithmic stablecoin collapse and fraud case",
        "algorithmic stablecoin separation is mandatory",
        "keep algorithmic stablecoin as hard RedTeam and separate it from regulated fiat-backed stablecoin",
    ),
    Round138ScoreStagePriceAlignment(
        "boe_stablecoin_rules_reconsider_case",
        "4C-watch",
        "user cap and unremunerated reserve requirement discussion can compress issuer economics",
        "stablecoin regulation can change the margin model",
        "strengthen user-cap, reserve requirement, issuer margin, and bank-deposit disintermediation gates",
    ),
    Round138ScoreStagePriceAlignment(
        "ai_citizen_dividend_policy_shock_case",
        "4C-watch",
        "KOSPI reportedly fell intraday -5.1% and closed -2.3% after AI windfall/citizen-dividend policy comments",
        "policy shock can break crowded 4B price paths before direct EPS damage appears",
        "strengthen crowded-trade, policy-comment, market-wide selloff, and valuation-room penalties",
    ),
)


ROUND138_SCORE_TARGETS: tuple[Round138ScoreTarget, ...] = (
    _target(
        "FINANCIAL_SPREAD_BALANCE_SHEET",
        E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(15, 20, 5, 15, 25, 10, 5),
        stage1=("korea_discount_policy", "commercial_act_revision", "bank_low_pbr", "financial_valueup_news"),
        stage2=("roe_improvement", "cet1_stable", "credit_cost_down", "dividend_or_buyback_execution"),
        stage3=("pbr_roe_frame_change", "recurring_return_policy", "roe_stable", "credit_risk_stable"),
        stage4b=("financial_valueup_crowded", "pbr_band_above_history", "roe_before_price_gap_closed"),
        stage4c=("credit_cost_spike", "pf_loss", "cet1_deterioration", "return_policy_retreat", "tax_policy_shock"),
        green=("roe", "cet1_ratio", "credit_cost", "pf_exposure_controlled", "shareholder_return_execution"),
        red=("credit_cost", "pf_exposure", "cet1_deterioration", "return_policy_retreat", "tax_policy_shock"),
        penalties=("credit_cost", "pf_exposure", "cet1", "tax_policy"),
        note="Low PBR is Stage 1; Green needs ROE/PBR, CET1, credit cost, and executed return together.",
    ),
    _target(
        "BANK_HOLDING_VALUEUP_CAPITAL_RETURN",
        E2RArchetype.BANK_HOLDING_VALUEUP_CAPITAL_RETURN,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(15, 21, 5, 16, 25, 11, 5),
        stage1=("bank_low_pbr", "financial_holding_valueup_news", "dividend_or_buyback_plan", "commercial_act_revision"),
        stage2=("cet1_stable", "shareholder_return_execution", "credit_cost_stable", "pbr_roe_band_watch"),
        stage3=("roe_stable_or_improving", "pbr_roe_frame_change", "repeat_return_policy", "pf_exposure_controlled"),
        stage4b=("bank_valueup_crowded", "pbr_band_above_history", "return_policy_fully_priced"),
        stage4c=("credit_cost_spike", "pf_loss", "cet1_deterioration", "nim_pressure", "return_policy_retreat"),
        green=("roe", "cet1_ratio", "credit_cost", "pf_exposure_controlled", "shareholder_return_execution", "pbr_roe_band_change"),
        red=("credit_cost", "pf_exposure", "cet1_deterioration", "nim_pressure", "return_policy_failure", "low_pbr_only"),
        penalties=("credit_cost", "cet1", "nim", "pf_exposure", "return_execution"),
        note="Bank holding value-up is Green-capable only when ROE/PBR, CET1, credit cost, and executed return all improve.",
    ),
    _target(
        "BANK_CREDIT_COST_PF_OVERLAY",
        E2RArchetype.BANK_CREDIT_COST_PF_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("pf_exposure", "real_estate_pf_headline", "bridge_loan", "credit_cost_watch"),
        stage2=("pf_delinquency_rise", "reserve_build", "syndicated_loan_support", "capital_buffer_check"),
        stage3=("not_applicable_gate_only",),
        stage4b=("valueup_rally_ignores_pf_credit_cost",),
        stage4c=("pf_delinquency_spike", "credit_cost_spike", "reserve_build_large", "cet1_pressure", "dividend_buyback_cut_risk"),
        green=(),
        red=("pf_exposure", "pf_delinquency_spike", "credit_cost_spike", "reserve_build", "cet1_pressure", "dividend_buyback_cut_risk"),
        penalties=("pf_exposure", "credit_cost", "reserve_build", "cet1", "return_cut"),
        note="PF credit cost is a hard gate: low PBR and value-up cannot become Green while credit cost is rising.",
        gate_only=True,
    ),
    _target(
        "INSURANCE_UNDERWRITING_CYCLE",
        E2RArchetype.INSURANCE_UNDERWRITING_CYCLE,
        Round10ThemePosture.GREEN_POSSIBLE,
        _w(15, 21, 4, 15, 25, 10, 5),
        stage1=("loss_ratio_improvement", "csm_growth", "insurance_valueup_news"),
        stage2=("roe_improvement", "k_ics_stable", "dividend_or_buyback_execution", "csm_quality"),
        stage3=("pbr_roe_rerating", "repeat_underwriting_quality", "capital_ratio_stable", "return_policy_repeatable"),
        stage4b=("insurance_valueup_crowded", "pbr_normalized", "dividend_yield_chasing"),
        stage4c=("loss_ratio_worse", "k_ics_deterioration", "alternative_investment_loss", "csm_quality_damage"),
        green=("roe", "k_ics_ratio", "csm_growth", "loss_ratio", "shareholder_return_execution"),
        red=("loss_ratio", "k_ics_deterioration", "investment_loss", "csm_quality_damage"),
        penalties=("loss_ratio", "k_ics", "investment_loss", "csm_quality"),
        note="Insurance Green needs CSM quality, K-ICS, loss ratio, and repeatable return policy, not yield alone.",
    ),
    _target(
        "INSURANCE_CAPITAL_RELEASE_VALUEUP",
        E2RArchetype.INSURANCE_CAPITAL_RELEASE_VALUEUP,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 19, 4, 14, 20, 12, 7),
        stage1=("insurance_valueup_news", "capital_release_expectation", "dividend_or_buyback_plan", "csm_growth"),
        stage2=("k_ics_stable", "csm_quality", "capital_release_execution", "dividend_or_buyback_execution"),
        stage3=("repeat_return_policy", "loss_ratio_stable", "capital_ratio_stable", "pbr_roe_rerating"),
        stage4b=("insurance_capital_release_crowded", "dividend_yield_chasing", "pbr_normalized"),
        stage4c=("k_ics_deterioration", "csm_quality_damage", "loss_ratio_worse", "return_policy_retreat"),
        green=("k_ics_ratio", "csm_quality", "capital_release_execution", "shareholder_return_execution", "loss_ratio_stable"),
        red=("k_ics_deterioration", "csm_quality_damage", "loss_ratio_worse", "return_policy_retreat"),
        penalties=("k_ics", "csm_quality", "loss_ratio", "return_policy"),
        note="Insurance capital release can become value-up only when CSM/K-ICS remain stable and actual returns execute.",
    ),
    _target(
        "SECURITIES_BROKERAGE_CYCLE",
        E2RArchetype.SECURITIES_BROKERAGE_CYCLE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(17, 12, 5, 13, 15, 6, 5),
        stage1=("trading_value_growth", "market_rally", "ipo_ib_recovery_expectation"),
        stage2=("brokerage_revenue_growth", "ib_fee_growth", "op_eps_revision"),
        stage3=("pf_risk_low", "roe_structure_improved", "ib_pipeline_durable"),
        stage4b=("brokerage_cycle_peak", "securities_group_overheated", "trading_value_peak"),
        stage4c=("transaction_tax_change", "capital_gains_tax_change", "trading_value_drop", "pf_loss", "proprietary_trading_loss"),
        green=("trading_value", "ib_fee_revenue", "pf_risk_low", "roe_improvement"),
        red=("tax_policy_shock", "trading_value_drop", "pf_loss", "proprietary_loss"),
        penalties=("trading_value", "tax_policy", "pf_loss", "proprietary_loss"),
        note="Brokerage remains cycle/watch unless trading value, IB, PF risk, and ROE structure all support durability.",
    ),
    _target(
        "VALUE_UP_SHAREHOLDER_RETURN",
        E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(12, 20, 4, 20, 25, 12, 5),
        stage1=("commercial_act_revision", "dividend_tax_reform", "valueup_index", "buyback_policy_news"),
        stage2=("treasury_share_cancellation", "dividend_growth", "roe_improvement", "shareholder_return_execution"),
        stage3=("pbr_nav_discount_narrows", "repeat_return_policy", "capital_allocation_execution", "pbr_roe_band_shift"),
        stage4b=("valueup_crowded_trade", "pbr_band_rerated_before_execution", "policy_premium_fully_priced"),
        stage4c=("no_cancellation", "activist_rejection", "capital_allocation_retreat", "controlling_shareholder_risk"),
        green=("buyback_cancelled", "dividend_growth", "roe_improvement", "minority_shareholder_protection"),
        red=("no_cancellation", "execution_failure", "low_roe", "controlling_shareholder_risk", "buyback_only"),
        penalties=("execution_failure", "buyback_only", "low_roe", "policy_only"),
        note="Value-up is Green only when policy becomes executed cancellation, dividends, ROE, and governance improvement.",
    ),
    _target(
        "TREASURY_SHARE_CANCEL_EXECUTION",
        E2RArchetype.TREASURY_SHARE_CANCEL_EXECUTION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(12, 21, 4, 18, 23, 13, 5),
        stage1=("treasury_share_buyback_plan", "treasury_share_cancellation_plan", "commercial_act_alignment"),
        stage2=("treasury_share_cancellation_completed", "treasury_share_cancel_amount", "cancel_ratio_verified"),
        stage3=("roe_pbr_band_change", "business_eps_fcf_path", "repeat_return_policy", "shareholder_return_execution"),
        stage4b=("cancellation_announcement_overpriced", "one_off_cancellation_crowded", "policy_premium_fully_priced"),
        stage4c=("cancellation_not_completed", "business_execution_failure", "one_off_return_then_stop", "roe_not_improving"),
        green=("treasury_share_cancellation_completed", "roe_improvement", "business_eps_fcf_path", "repeat_return_policy"),
        red=("buyback_only", "cancellation_not_completed", "business_execution_failure", "roe_not_improving"),
        penalties=("buyback_only", "business_eps_missing", "one_off_cancellation", "roe_not_improving"),
        note="Treasury-share cancellation is stronger than buyback news, but Green still needs business EPS/FCF and ROE/PBR confirmation.",
    ),
    _target(
        "TREASURY_CANCEL_MANDATE_POLICY",
        E2RArchetype.TREASURY_CANCEL_MANDATE_POLICY,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(10, 18, 3, 18, 22, 10, 5),
        stage1=("commercial_act_revision", "treasury_cancel_mandate", "minority_shareholder_protection", "korea_discount_policy"),
        stage2=("individual_treasury_cancel_execution", "existing_treasury_grace_period_resolution", "dividend_or_buyback_execution"),
        stage3=("roe_pbr_band_change", "repeat_return_policy", "business_eps_fcf_path", "minority_protection_execution"),
        stage4b=("policy_premium_fully_priced", "valueup_policy_crowded", "execution_lag_ignored"),
        stage4c=("policy_only_no_execution", "buyback_without_cancellation", "roe_not_improving", "governance_execution_failure"),
        green=("individual_treasury_cancel_execution", "roe_improvement", "pbr_roe_band_change", "repeat_return_policy"),
        red=("policy_only_no_execution", "buyback_without_cancellation", "existing_treasury_grace_period_unresolved", "roe_not_improving"),
        penalties=("policy_only", "execution_missing", "buyback_only", "low_roe"),
        note="Treasury-cancel mandate is macro tailwind; individual Green waits for actual cancellation and ROE/PBR change.",
    ),
    _target(
        "BUYBACK_CANCEL_BUT_BUSINESS_RISK",
        E2RArchetype.BUYBACK_CANCEL_BUT_BUSINESS_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("treasury_share_cancellation_completed", "buyback_cancelled_flag", "shareholder_return_headline"),
        stage2=("business_risk_detected_after_cancel", "price_down_on_event", "eps_fcf_path_unverified"),
        stage3=("not_applicable_gate_only",),
        stage4b=("cancellation_announcement_overpriced",),
        stage4c=("business_execution_failure", "roe_not_improving", "price_down_on_event", "eps_fcf_path_break", "competitive_position_weak"),
        green=(),
        red=("business_execution_failure", "roe_not_improving", "price_down_on_event", "eps_fcf_path_break", "buyback_only"),
        penalties=("business_eps_missing", "roe_not_improving", "price_path_failed", "one_off_cancellation"),
        note="Completed cancellation is Stage 2 evidence, but business EPS/FCF failure can still block or break the thesis.",
        gate_only=True,
    ),
    _target(
        "HOLDING_RESTRUCTURING_GOVERNANCE",
        E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(12, 19, 4, 22, 24, 12, 5),
        stage1=("nav_discount", "subsidiary_value_gap", "activist_or_buyback_news"),
        stage2=("buyback_cancel", "independent_director", "dividend_policy", "governance_improvement"),
        stage3=("nav_discount_narrows", "repeat_capital_return", "minority_protection", "subsidiary_value_supported"),
        stage4b=("holding_valueup_crowded", "nav_discount_compression_priced"),
        stage4c=("activist_rejection", "governance_battle", "share_issuance_defense", "minority_shareholder_value_damage"),
        green=("nav_discount", "actual_cancellation", "independent_director", "governance_improvement", "capital_structure_stable"),
        red=("governance_battle", "event_premium", "share_issuance_defense", "minority_conflict"),
        penalties=("event_premium", "governance_battle", "share_issuance", "debt_ratio_jump"),
        note="Holding rerating needs NAV discount plus actual governance and capital-allocation execution.",
    ),
    _target(
        "EVENT_PREMIUM_GOVERNANCE_BATTLE",
        E2RArchetype.EVENT_PREMIUM_GOVERNANCE_BATTLE,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(8, 6, 3, 12, 8, 0, 5),
        stage1=("tender_offer", "hostile_takeover", "management_control_battle", "governance_event"),
        stage2=("event_premium_detected", "deal_terms_known"),
        stage3=("not_structural_green_by_default",),
        stage4b=("control_premium_fully_priced", "event_spread_crowded"),
        stage4c=("share_issuance_after_tender", "unfair_trading_probe", "capital_structure_risk", "minority_shareholder_damage"),
        green=(),
        red=("tender_offer", "governance_event", "event_premium", "share_issuance_after_tender", "capital_structure_risk"),
        penalties=("event_premium", "governance_battle", "capital_structure", "hostile_takeover"),
        note="Tender offers and governance battles are event premium first, not value-up execution.",
    ),
    _target(
        "PAYMENT_FINTECH_INFRA",
        E2RArchetype.PAYMENT_FINTECH_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(18, 20, 8, 14, 14, 2, 5),
        stage1=("active_users_growth", "global_expansion", "payment_remittance_finance_service"),
        stage2=("payment_volume", "take_rate", "financial_service_attach", "profit_or_fcf"),
        stage3=("repeat_financial_infra_revenue", "regulatory_stability", "security_clean", "credit_loss_control"),
        stage4b=("ipo_valuation_overheated", "user_count_story_crowded"),
        stage4c=("security_incident", "credit_loss_rate_up", "take_rate_pressure", "regulatory_sanction"),
        green=("payment_volume", "take_rate", "attach_rate", "profit_fcf", "regulation_security_clean"),
        red=("take_rate_pressure", "security_incident", "credit_loss", "regulatory_sanction", "user_count_only"),
        penalties=("take_rate", "fcf", "security", "credit_loss", "ipo_valuation"),
        note="Payment fintech needs transaction economics and FCF; user count is routing context, not Green evidence.",
    ),
    _target(
        "FINTECH_SUPERAPP_IPO_OPTION",
        E2RArchetype.FINTECH_SUPERAPP_IPO_OPTION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(17, 17, 7, 15, 10, 1, 5),
        stage1=("super_app_users", "ipo_plan", "global_expansion", "financial_service_attach_story"),
        stage2=("payment_volume", "take_rate", "attach_rate", "profit_or_fcf", "credit_loss_control"),
        stage3=("repeat_financial_service_revenue", "security_clean", "regulatory_stability", "fcf_margin_visible"),
        stage4b=("ipo_valuation_overheated", "user_count_story_crowded", "private_market_mark_up"),
        stage4c=("credit_loss_rate_up", "take_rate_pressure", "security_incident", "regulatory_sanction"),
        green=("take_rate", "attach_rate", "profit_fcf", "credit_loss_control", "security_clean"),
        red=("user_count_only", "ipo_valuation_risk", "credit_loss", "security_incident", "regulatory_sanction"),
        penalties=("user_count_only", "ipo_valuation", "credit_loss", "security", "regulation"),
        note="Superapp and IPO optionality are Stage 1/2 until take rate, FCF, credit loss, security, and regulation are visible.",
    ),
    _target(
        "KRW_STABLECOIN_INFRA_OPTION",
        E2RArchetype.KRW_STABLECOIN_INFRA_OPTION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(15, 16, 8, 15, 9, 1, 6),
        stage1=("won_stablecoin_plan", "krw_stablecoin_law", "fintech_or_bank_issuer_intent", "cross_border_payment_story"),
        stage2=("regulatory_approval", "reserve_structure_disclosed", "redemption_rail_defined", "pilot_issued_amount"),
        stage3=("regulated_volume", "fee_or_reserve_revenue", "redemption_at_par", "bank_deposit_impact_understood"),
        stage4b=("krw_stablecoin_theme_crowded", "law_expectation_fully_priced"),
        stage4c=("regulatory_rejection", "reserve_opacity", "convertibility_failure", "bank_deposit_disintermediation_shock"),
        green=("regulatory_approval", "reserve_transparency", "redemption_capacity", "issued_amount", "fee_model"),
        red=("regulatory_approval_missing", "reserve_unverified", "stablecoin_volume_unverified", "bank_deposit_disintermediation", "convertibility_risk"),
        penalties=("regulation", "reserve", "redemption", "bank_deposit_impact", "fee_model"),
        note="KRW stablecoin is an option value until regulation, reserve, redemption, volume, and fee economics are visible.",
    ),
    _target(
        "DIGITAL_ASSET_TOKENIZATION",
        E2RArchetype.DIGITAL_ASSET_TOKENIZATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(16, 18, 8, 16, 12, 3, 5),
        stage1=("stablecoin_sto_bill", "tokenization_business_entry", "partnership_news"),
        stage2=("regulatory_approval", "issued_amount", "transaction_volume", "fee_model", "reserve_disclosure"),
        stage3=("payment_custody_settlement_infra", "repeat_revenue", "reserve_transparency", "convertibility_clear"),
        stage4b=("stablecoin_law_expectation_crowded", "sto_theme_rally"),
        stage4c=("depeg", "convertibility_failure", "reserve_problem", "regulatory_rejection", "fraud"),
        green=("regulatory_approval", "reserve_transparency", "redemption_capacity", "transaction_volume", "fee_model"),
        red=("depeg", "reserve_opacity", "convertibility_risk", "fraud", "regulatory_rejection"),
        penalties=("reserve", "convertibility", "regulated_revenue", "fee_model"),
        note="Digital-asset Green is blocked until regulated volume, fee model, reserve, and convertibility are proven.",
    ),
    _target(
        "REGULATED_STABLECOIN_INFRA",
        E2RArchetype.REGULATED_STABLECOIN_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(17, 19, 9, 16, 10, 3, 6),
        stage1=("stablecoin_law", "fiat_backed_issuer", "stablecoin_ipo", "payment_partnership"),
        stage2=("regulatory_approval", "reserve_asset_disclosure", "issued_amount", "transaction_volume", "redemption_system"),
        stage3=("payment_settlement_infra", "repeat_fee_or_reserve_revenue", "reserve_transparency", "redemption_at_par"),
        stage4b=("stablecoin_infra_valuation_overheated", "ipo_rally_crowded"),
        stage4c=("depeg", "reserve_failure", "issuer_margin_compression", "regulatory_economics_break"),
        green=("fiat_backed", "reserve_transparency", "redemption_capacity", "issued_amount", "transaction_volume", "fee_model"),
        red=("reserve_opacity", "convertibility_risk", "depeg", "algorithmic_design", "regulatory_economics_break"),
        penalties=("reserve", "redemption", "issuer_margin", "regulation"),
        note="Regulated stablecoin can become infrastructure, but only after reserve, redemption, volume, and fees are proven.",
    ),
    _target(
        "STABLECOIN_AI_AGENT_PAYMENT_OPTION",
        E2RArchetype.STABLECOIN_AI_AGENT_PAYMENT_OPTION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(14, 16, 8, 14, 8, 1, 7),
        stage1=("ai_agent_payment_narrative", "nanopayment", "wallet_developer_tools", "stablecoin_ai_option"),
        stage2=("developer_adoption", "pilot_transaction_volume", "wallet_integration", "non_reserve_fee_revenue_initial"),
        stage3=("repeat_fee_revenue", "compliance_pass", "settlement_reliability", "developer_ecosystem_retention"),
        stage4b=("ai_payment_option_valuation_overheated", "stablecoin_ai_story_crowded"),
        stage4c=("fee_revenue_absent", "regulatory_block", "settlement_failure", "developer_adoption_fades"),
        green=("repeat_fee_revenue", "compliance_pass", "settlement_reliability", "developer_adoption"),
        red=("fee_revenue_absent", "regulatory_block", "settlement_failure", "developer_adoption_fades"),
        penalties=("fee_revenue", "regulation", "settlement", "developer_adoption"),
        note="AI-agent payment is an option until fee revenue, compliance, and settlement reliability are visible.",
    ),
    _target(
        "STABLECOIN_REGULATORY_ECONOMICS",
        E2RArchetype.STABLECOIN_REGULATORY_ECONOMICS,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("stablecoin_user_cap", "unremunerated_reserve_requirement", "issuer_margin_watch", "reserve_rule_change"),
        stage2=("regulatory_economics_risk_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("stablecoin_adoption_story_ignores_margin_rule",),
        stage4c=("user_cap_constraint", "unremunerated_reserve_requirement", "issuer_margin_compression", "reserve_yield_hit", "bank_deposit_disintermediation"),
        green=(),
        red=("user_cap", "unremunerated_reserve_requirement", "issuer_margin_compression", "reserve_yield_hit", "bank_deposit_disintermediation"),
        penalties=("user_cap", "reserve_requirement", "issuer_margin", "bank_deposit"),
        note="Regulated stablecoin can still fail economics if user caps or unremunerated reserves compress issuer margins.",
        gate_only=True,
    ),
    _target(
        "STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION",
        E2RArchetype.STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("stablecoin_user_cap", "bank_deposit_disintermediation", "unremunerated_reserve_requirement", "reserve_rule_change"),
        stage2=("risk_event_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("bank_deposit_outflow", "issuer_margin_compression", "user_cap_constraint", "reserve_yield_hit", "liquidity_stress"),
        green=(),
        red=("bank_deposit_disintermediation", "user_cap", "unremunerated_reserve_requirement", "issuer_margin_compression", "reserve_yield_hit"),
        penalties=("bank_deposit", "user_cap", "reserve_requirement", "issuer_margin"),
        note="Stablecoin bank-deposit disintermediation is a RedTeam gate for banks and stablecoin issuers.",
        gate_only=True,
    ),
    _target(
        "ALGORITHMIC_STABLECOIN_FAILURE",
        E2RArchetype.ALGORITHMIC_STABLECOIN_FAILURE,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("algorithmic_stablecoin", "depeg_warning", "reserve_design_unclear"),
        stage2=("risk_event_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("depeg", "reserve_failure", "convertibility_failure", "liquidity_run", "fraud", "algorithmic_stablecoin_failure"),
        green=(),
        red=("algorithmic_stablecoin", "depeg", "reserve_failure", "fraud", "run_risk"),
        penalties=("depeg", "reserve_failure", "algorithmic", "fraud"),
        note="Algorithmic stablecoin failure is a hard RedTeam gate.",
        gate_only=True,
    ),
    _target(
        "CREDIT_DATA_INFRA",
        E2RArchetype.CREDIT_DATA_INFRA,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(17, 19, 7, 13, 12, 1, 5),
        stage1=("credit_data_contract", "financial_data_infra", "customer_growth"),
        stage2=("recurring_financial_institution_contract", "data_revenue_growth", "opm_improvement"),
        stage3=("repeat_data_revenue", "regulatory_clean", "customer_diversification"),
        stage4b=("credit_data_story_crowded",),
        stage4c=("privacy_breach", "regulatory_sanction", "customer_concentration", "contract_loss"),
        green=("recurring_contracts", "data_revenue", "regulatory_clean", "customer_diversification"),
        red=("privacy_breach", "regulation", "customer_concentration"),
        penalties=("privacy", "regulation", "customer_concentration"),
        note="Credit-data infra needs recurring contracts and clean privacy/regulatory record.",
    ),
    _target(
        "VC_EXIT_MARKET_CYCLE",
        E2RArchetype.VC_EXIT_MARKET_CYCLE,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(15, 10, 4, 12, 9, 2, 5),
        stage1=("ipo_market_reopen", "venture_exit_expectation", "valuation_rebound"),
        stage2=("exit_volume", "realized_gain", "fundraising_recovery"),
        stage3=("repeat_exit_market", "portfolio_quality", "cash_return"),
        stage4b=("vc_exit_cycle_crowded",),
        stage4c=("ipo_market_slowdown", "valuation_loss", "funding_market_freeze"),
        green=("exit_volume", "realized_gain", "cash_return"),
        red=("ipo_slowdown", "valuation_loss", "funding_freeze"),
        penalties=("ipo_cycle", "valuation_loss", "funding_freeze"),
        note="VC/exit market is cycle-heavy and stays RedTeam-first until realized exits and cash returns are visible.",
    ),
    _target(
        "FINTECH_IPO_VALUATION_RISK",
        E2RArchetype.FINTECH_IPO_VALUATION_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        _w(12, 10, 4, 10, 6, 0, 5),
        stage1=("fintech_ipo_plan", "user_count_story", "private_market_valuation", "crypto_capital_market_exposure"),
        stage2=("ipo_size_cut", "ipo_valuation_cut", "investor_caution", "weak_market_window"),
        stage3=("not_green_without_post_listing_economics",),
        stage4b=("ipo_valuation_overheated", "private_market_markdown", "growth_story_crowded"),
        stage4c=("ipo_size_cut", "ipo_valuation_cut", "valuation_target_cut", "crypto_exposure_hit", "market_window_closed", "post_listing_price_break"),
        green=(),
        red=("ipo_size_cut", "ipo_valuation_cut", "crypto_exposure", "investor_caution", "user_count_only"),
        penalties=("ipo_valuation", "market_window", "crypto_exposure", "investor_caution"),
        note="Fintech IPO optionality is Watch/Red until post-listing economics, take rate, FCF, credit loss, and security are proven.",
    ),
    _target(
        "DIGITAL_ASSET_EXCHANGE_CONSOLIDATION",
        E2RArchetype.DIGITAL_ASSET_EXCHANGE_CONSOLIDATION,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(17, 17, 8, 14, 10, 2, 5),
        stage1=("crypto_exchange_acquisition", "fintech_exchange_integration", "market_share_news"),
        stage2=("exchange_market_share", "exchange_fee_revenue", "user_cross_sell", "regulatory_approval"),
        stage3=("repeat_exchange_fee_revenue", "financial_platform_integration", "security_clean", "regulatory_stability"),
        stage4b=("exchange_consolidation_premium_crowded", "crypto_market_rally_priced"),
        stage4c=("abnormal_crypto_withdrawal", "exchange_security_incident", "regulatory_investigation", "deal_dilution", "crypto_volume_drop"),
        green=("exchange_market_share", "fee_revenue", "security_clean", "regulatory_approval", "platform_cross_sell"),
        red=("abnormal_withdrawal", "security_incident", "regulatory_investigation", "deal_dilution", "crypto_cycle"),
        penalties=("security", "regulation", "crypto_cycle", "deal_dilution"),
        note="Exchange consolidation can route research, but abnormal withdrawals or security incidents put RedTeam first.",
    ),
    _target(
        "BANK_DIGITAL_ASSET_EQUITY_STAKE",
        E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_STAKE,
        Round10ThemePosture.WATCH_YELLOW_FIRST,
        _w(15, 15, 8, 14, 10, 2, 5),
        stage1=("bank_exchange_equity_stake", "digital_asset_partnership", "crypto_exchange_market_share"),
        stage2=("equity_stake_purchase_completed", "equity_method_accounting", "joint_service_plan", "regulatory_approval"),
        stage3=("equity_method_income", "strategic_collaboration_revenue", "custody_or_settlement_revenue", "security_clean"),
        stage4b=("exchange_stake_premium_crowded", "crypto_cycle_valuation_priced"),
        stage4c=("abnormal_crypto_withdrawal", "exchange_security_incident", "crypto_trading_value_drop", "regulatory_investigation", "stake_impairment"),
        green=("equity_method_income", "strategic_collaboration_revenue", "regulatory_approval", "security_clean"),
        red=("equity_method_income_unverified", "security_incident", "regulatory_investigation", "crypto_cycle", "stake_impairment"),
        penalties=("equity_income_unverified", "security", "regulation", "crypto_cycle", "stake_valuation"),
        note="Bank exchange stakes are Stage 1/2 until equity-method income, collaboration revenue, regulation, and security are proven.",
    ),
    _target(
        "EXCHANGE_SECURITY_OPERATIONAL_RISK",
        E2RArchetype.EXCHANGE_SECURITY_OPERATIONAL_RISK,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("crypto_exchange_market_share", "exchange_fee_revenue", "exchange_security_watch", "wallet_infrastructure"),
        stage2=("security_incident_detected", "abnormal_withdrawal", "wallet_compromise"),
        stage3=("not_applicable_gate_only",),
        stage4b=("exchange_market_share_story_ignores_security",),
        stage4c=("exchange_security_incident", "wallet_compromise", "customer_compensation_cost", "regulatory_investigation", "trust_damage"),
        green=(),
        red=("exchange_security_incident", "wallet_compromise", "customer_compensation_cost", "regulatory_investigation", "trust_damage"),
        penalties=("security", "wallet", "customer_compensation", "regulation", "trust_damage"),
        note="Exchange market share is not enough; security incidents are hard RedTeam gates for exchange and bank-stake exposure.",
        gate_only=True,
    ),
    _target(
        "TAX_POLICY_MARKET_SHOCK_OVERLAY",
        E2RArchetype.TAX_POLICY_MARKET_SHOCK_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("transaction_tax_hike", "capital_gains_tax_threshold_change", "corporate_tax_hike", "dividend_tax_uncertainty"),
        stage2=("risk_event_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("trading_value_drop", "tax_policy_shock", "dividend_tax_uncertainty", "market_sentiment_collapse", "ai_windfall_tax_comment"),
        green=(),
        red=("transaction_tax_change", "capital_gains_tax_change", "corporate_tax_change", "dividend_tax_change", "trading_value_drop"),
        penalties=("tax_policy", "trading_value", "macro_sentiment"),
        note="Tax policy shock is a RedTeam overlay for brokerage, value-up, and crowded market rallies.",
        gate_only=True,
    ),
    _target(
        "AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK",
        E2RArchetype.AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("ai_windfall_policy_comment", "citizen_dividend_comment", "crowded_ai_valueup_rally", "market_wide_selloff"),
        stage2=("risk_event_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("ai_windfall_policy_shock", "citizen_dividend_policy_shock", "market_sentiment_collapse", "trading_value_drop"),
        green=(),
        red=("ai_windfall_tax_comment", "citizen_dividend_comment", "crowded_trade_unwind", "market_wide_selloff"),
        penalties=("policy_comment", "crowded_trade", "market_sentiment"),
        note="AI windfall/citizen-dividend policy shock is a RedTeam overlay for crowded AI, value-up, and brokerage rallies.",
        gate_only=True,
    ),
    _target(
        "GOVERNANCE_EXECUTION_FAILURE_OVERLAY",
        E2RArchetype.GOVERNANCE_EXECUTION_FAILURE_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("activist_proposal_rejection", "buyback_without_cancellation", "controlling_shareholder_defense"),
        stage2=("risk_event_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("activist_rejection", "minority_shareholder_protection_failure", "share_issuance_defense", "governance_discount_persists"),
        green=(),
        red=("activist_rejection", "no_cancellation", "minority_shareholder_protection_failure", "controlling_shareholder_risk"),
        penalties=("governance_execution", "minority_protection", "capital_structure"),
        note="Governance execution failure is a RedTeam overlay, not a positive score bucket.",
        gate_only=True,
    ),
    _target(
        "STABLECOIN_CONVERTIBILITY_OVERLAY",
        E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY,
        Round10ThemePosture.REDTEAM_FIRST,
        GATE_WEIGHT,
        stage1=("stablecoin_convertibility_warning", "reserve_mismatch", "redemption_not_at_par", "regulatory_economics_change"),
        stage2=("risk_event_detected",),
        stage3=("not_applicable_gate_only",),
        stage4b=("not_applicable_gate_only",),
        stage4c=("depeg", "convertibility_failure", "reserve_failure", "liquidity_run", "issuer_margin_compression"),
        green=(),
        red=("reserve_mismatch", "redemption_not_at_par", "convertibility_risk", "run_risk", "issuer_margin_compression"),
        penalties=("reserve", "convertibility", "depeg", "issuer_margin"),
        note="Stablecoin convertibility is a RedTeam overlay; issuance news is not regulated fee revenue.",
        gate_only=True,
    ),
    _target(
        "DISCLOSURE_CONFIDENCE_CAP",
        E2RArchetype.DISCLOSURE_CONFIDENCE_CAP,
        Round10ThemePosture.REDTEAM_FIRST,
        _w("cap", "cap", "cap", "cap", "cap", "cap", "+"),
        stage1=("list_level_disclosure", "headline_without_detail", "return_policy_without_amount", "stablecoin_without_reserve_detail"),
        stage2=("detail_gap_detected",),
        stage3=("not_applicable_cap_only",),
        stage4b=("headline_priced_without_detail",),
        stage4c=("disclosure_detail_missing", "parser_confidence_low", "amount_or_duration_missing", "reserve_or_redemption_detail_missing"),
        green=(),
        red=("disclosure_detail_missing", "parser_confidence_low", "amount_or_duration_missing", "reserve_or_redemption_detail_missing"),
        penalties=("disclosure_detail", "parser_confidence", "amount_detail", "reserve_detail"),
        note="Financial, capital-return, and stablecoin Stage 3 is capped when detail fields are missing.",
        gate_only=True,
    ),
)


ROUND138_CASE_CANDIDATES: tuple[Round138CaseCandidate, ...] = (
    Round138CaseCandidate(
        "korea_commercial_act_treasury_cancel_case",
        "TREASURY_CANCEL_MANDATE_POLICY",
        "KOSPI_VALUEUP_POLICY_REF",
        "Korea Commercial Act treasury cancellation reform",
        "KR",
        "success_candidate",
        date(2026, 2, 25),
        None,
        None,
        None,
        None,
        ("commercial_act_revision", "treasury_cancel_mandate_flag", "treasury_share_cancel_deadline", "existing_treasury_grace_period_flag", "minority_shareholder_protection", "korea_discount_policy", "kospi_policy_rally"),
        ("policy_expectation_only", "individual_execution_not_verified", "crowded_trade", "buyback_without_cancellation"),
        "treasury_cancel_policy_tailwind",
        "missing_direct_symbol_mapping",
        ("round_138.md Reuters commercial act treasury cancellation",),
        "Commercial Act reform is a strong Stage 1 value-up background, but individual Green still needs cancellation, ROE, and FCF.",
        (E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN,),
    ),
    Round138CaseCandidate(
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
        ("nav_discount", "sk_hynix_stake_value", "buyback_cancel", "additional_buyback", "independent_director", "activist_engagement"),
        ("subsidiary_price_dependency", "holding_discount_persistence", "cancellation_scale_insufficient"),
        "holding_nav_discount_reduction_candidate",
        "needs_price_backfill",
        ("round_138.md Reuters SK Square buybacks",),
        "NAV discount plus cancellation and independent-director evidence makes this an execution candidate, not policy-only value-up.",
    ),
    Round138CaseCandidate(
        "samsung_electronics_treasury_cancel_case",
        "TREASURY_SHARE_CANCEL_EXECUTION",
        "005930",
        "Samsung Electronics treasury-share cancellation mixed case",
        "KR",
        "failed_rerating",
        None,
        date(2026, 3, 31),
        None,
        None,
        None,
        ("treasury_share_cancel_amount", "treasury_share_cancellation_completed", "shareholder_return_policy", "commercial_act_alignment"),
        ("price_down_on_event", "business_thesis_weakness", "hbm_ai_execution_risk", "labor_risk"),
        "buyback_cancel_execution_but_business_risk_remains",
        "needs_price_backfill",
        ("round_138.md Reuters Samsung treasury cancellation",),
        "Cancellation improves capital allocation quality, but negative price reaction and business risks keep this from Green.",
        (E2RArchetype.MEMORY_HBM_CAPACITY,),
    ),
    Round138CaseCandidate(
        "korea_bank_financial_holding_valueup_candidate",
        "BANK_HOLDING_VALUEUP_CAPITAL_RETURN",
        "KOREA_BANK_VALUEUP_REF",
        "은행·금융지주 value-up 후보군",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("roe_required", "cet1_ratio_required", "credit_cost_required", "pf_exposure_required", "shareholder_return_execution_required", "pbr_roe_band_required"),
        ("pf_exposure_unverified", "credit_cost_unverified", "cet1_unverified", "tax_policy_shock", "low_pbr_only"),
        "financial_holding_valueup_candidate",
        "needs_named_case_and_price_backfill",
        ("round_138.md section 4-4 bank and financial holding candidate",),
        "Round 138 keeps banks and financial holdings Green-capable only after ROE, CET1, credit cost, PF exposure, and return execution are verified.",
        (E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,),
    ),
    Round138CaseCandidate(
        "korea_insurance_underwriting_valueup_candidate",
        "INSURANCE_UNDERWRITING_CYCLE",
        "KOREA_INSURANCE_VALUEUP_REF",
        "손해보험·생명보험 underwriting value-up 후보군",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("csm_growth_required", "csm_quality_required", "k_ics_ratio_required", "loss_ratio_required", "shareholder_return_execution_required"),
        ("loss_ratio_unverified", "k_ics_unverified", "alternative_investment_loss", "csm_quality_unverified"),
        "insurance_valueup_underwriting_candidate",
        "needs_named_case_and_price_backfill",
        ("round_138.md section 4-5 insurance underwriting candidate",),
        "Round 138 keeps insurance Green-capable, but separates CSM quality, K-ICS, loss ratio, and investment-loss risks from bank value-up.",
    ),
    Round138CaseCandidate(
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
        ("nav_discount", "activist_campaign", "low_pbr", "asset_value"),
        ("activist_rejection", "capital_allocation_retreat", "minority_shareholder_protection_failure", "controlling_shareholder_risk"),
        "governance_execution_failure_4c_watch",
        "needs_source_date_and_price_backfill",
        ("round_138.md Financial Times Samsung C&T activist rejection",),
        "Year-level timing and near-10% price reaction are given, so no exact stage date is invented.",
        (E2RArchetype.HOLDING_RESTRUCTURING_GOVERNANCE,),
    ),
    Round138CaseCandidate(
        "korea_zinc_tender_offer_event_case",
        "EVENT_PREMIUM_GOVERNANCE_BATTLE",
        "010130",
        "Korea Zinc tender offer event premium",
        "KR",
        "event_premium",
        None,
        date(2024, 9, 13),
        None,
        None,
        None,
        ("tender_offer_flag", "governance_event_flag", "day_price_reaction_plus_19_8pct", "control_battle"),
        ("event_premium", "hostile_takeover", "control_battle", "fcf_not_verified"),
        "event_premium_governance_battle_watch",
        "needs_price_backfill",
        ("round_138.md Reuters Korea Zinc tender offer",),
        "Tender-offer price reaction is event premium first; it must not be misclassified as structural value-up.",
        (E2RArchetype.NONFERROUS_STRATEGIC_METALS,),
    ),
    Round138CaseCandidate(
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
        ("share_issuance_flag", "share_issuance_amount_1_8b", "governance_event_flag", "capital_structure_risk_flag"),
        ("share_issuance_after_tender_flag", "unfair_trading_probe", "minority_shareholder_harm", "capital_structure_deterioration"),
        "capital_structure_governance_4c_watch",
        "needs_price_backfill",
        ("round_138.md Reuters Korea Zinc share issuance probe",),
        "Share issuance after a tender battle is a governance and capital-structure RedTeam event.",
        (E2RArchetype.EVENT_PREMIUM_GOVERNANCE_BATTLE,),
    ),
    Round138CaseCandidate(
        "korea_capital_gains_tax_scrap_case",
        "TAX_POLICY_MARKET_SHOCK_OVERLAY",
        "KOSPI_TAX_SHOCK_REF",
        "Korea stock-market tax policy shock",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 9, 11),
        ("market_rally", "valueup_crowded_trade", "brokerage_cycle", "capital_gains_tax_threshold_change"),
        ("transaction_tax_change", "capital_gains_tax_change", "corporate_tax_change", "dividend_tax_uncertainty", "market_sentiment_collapse"),
        "tax_policy_market_shock_4c_watch",
        "missing_direct_symbol_mapping",
        ("round_138.md Reuters Korea tax policy shock",),
        "Tax-policy relief can help sentiment, but transaction-tax, dividend-tax, and future threshold uncertainty remain R6 RedTeam overlays.",
        (E2RArchetype.SECURITIES_BROKERAGE_CYCLE, E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN),
    ),
    Round138CaseCandidate(
        "ai_citizen_dividend_policy_shock_case",
        "AI_WINDFALL_CITIZEN_DIVIDEND_POLICY_SHOCK",
        "KOSPI_AI_WINDFALL_TAX_REF",
        "AI windfall / citizen dividend policy-comment shock",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 12),
        ("ai_market_rally", "crowded_trade", "policy_comment", "kospi_intraday_down_5pct"),
        ("tax_policy_shock", "market_sentiment_collapse", "ai_windfall_tax_comment", "trading_value_drop_risk"),
        "ai_windfall_tax_policy_shock",
        "missing_direct_symbol_mapping",
        ("round_138.md Barron's AI windfall tax policy shock",),
        "AI windfall or citizen-dividend policy comments can damage crowded value-up and brokerage price paths even before tax law changes.",
        (E2RArchetype.TAX_POLICY_MARKET_SHOCK_OVERLAY, E2RArchetype.SECURITIES_BROKERAGE_CYCLE, E2RArchetype.VALUE_UP_SHAREHOLDER_RETURN),
    ),
    Round138CaseCandidate(
        "mynt_gcash_ipo_case",
        "FINTECH_SUPERAPP_IPO_OPTION",
        "MYNT_GCASH_REF",
        "Mynt / GCash e-wallet financial platform",
        "PH",
        "success_candidate",
        None,
        date(2026, 5, 14),
        None,
        None,
        None,
        ("active_users_94m", "bill_payment", "remittance", "savings_lending_insurance_attach", "ipo_valuation_8b"),
        ("user_count_only", "take_rate_unverified", "credit_loss_unverified", "ipo_valuation_risk", "regulation"),
        "ewallet_financial_platform_reference",
        "missing_public_price_data",
        ("round_138.md Reuters Mynt GCash IPO",),
        "Large user base is useful, but take rate, attach, credit loss, security, and FCF remain required.",
        (E2RArchetype.PAYMENT_FINTECH_INFRA,),
    ),
    Round138CaseCandidate(
        "clear_street_ipo_valuation_cut_case",
        "FINTECH_IPO_VALUATION_RISK",
        "CLEAR_STREET_REF",
        "Clear Street fintech IPO valuation compression",
        "US",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 2, 12),
        ("fintech_ipo_plan", "ipo_size_cut_flag", "ipo_valuation_cut_flag", "crypto_exposure_flag", "investor_caution"),
        ("ipo_size_cut", "ipo_valuation_cut", "crypto_exposure", "weak_market_window", "investor_caution"),
        "fintech_ipo_valuation_compression_watch",
        "missing_public_price_data",
        ("round_138.md Reuters Clear Street IPO valuation cut",),
        "A fintech IPO plan is not Green; size cuts, valuation cuts, crypto exposure, and investor caution are RedTeam-first.",
    ),
    Round138CaseCandidate(
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
        ("active_users_30m_plus", "global_expansion", "super_app", "won_stablecoin_plan", "ipo_plan_10_15b"),
        ("regulatory_approval_missing", "stablecoin_volume_unverified", "reserve_unverified", "valuation_risk", "fee_model_unverified"),
        "fintech_success_candidate_stablecoin_stage1_watch",
        "missing_public_price_data",
        ("round_138.md Reuters Toss global push won stablecoin",),
        "Toss fintech is a success candidate, while won stablecoin remains Watch before regulation, volume, reserve, and fees.",
        (
            E2RArchetype.FINTECH_SUPERAPP_IPO_OPTION,
            E2RArchetype.KRW_STABLECOIN_INFRA_OPTION,
            E2RArchetype.DIGITAL_ASSET_TOKENIZATION,
            E2RArchetype.REGULATED_STABLECOIN_INFRA,
        ),
    ),
    Round138CaseCandidate(
        "circle_usdc_stablecoin_earnings_case",
        "REGULATED_STABLECOIN_INFRA",
        "CRCL",
        "Circle regulated stablecoin IPO valuation",
        "US",
        "4b_watch",
        None,
        date(2026, 5, 11),
        None,
        date(2026, 5, 11),
        None,
        ("fiat_backed_stablecoin", "fully_reserved_usd_backed", "genius_act_framework", "reserve_income_694m", "stablecoin_circulation_77b", "circulation_growth_28pct", "ipo_price_three_times_plus"),
        ("valuation_overheat", "issuer_margin_sensitivity", "tether_competition", "regulatory_change", "rate_sensitivity"),
        "regulated_stablecoin_success_but_4b_watch",
        "needs_price_backfill",
        ("round_138.md Reuters Circle IPO valuation",),
        "Circle is a regulated stablecoin infrastructure reference, but post-IPO valuation requires 4B-watch.",
        (E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY,),
    ),
    Round138CaseCandidate(
        "boe_stablecoin_rules_reconsider_case",
        "STABLECOIN_BANK_DEPOSIT_DISINTERMEDIATION",
        "STABLECOIN_RULES_REF",
        "Bank of England stablecoin rules reconsideration",
        "GLOBAL",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2026, 5, 14),
        ("stablecoin_cross_border_payment", "regulatory_standard", "boe_rule_reconsideration", "bank_deposit_disintermediation_flag", "user_cap_flag", "unremunerated_reserve_requirement_flag"),
        ("user_cap_flag", "unremunerated_reserve_requirement_flag", "redemption_rail_unclear", "issuer_margin_compression", "bank_deposit_disintermediation"),
        "stablecoin_regulation_fluid_watch",
        "missing_direct_symbol_mapping",
        ("round_138.md Reuters Bank of England stablecoin regulation",),
        "Regulated stablecoin exposure still needs reserve, redemption, issuer economics, and regulatory proof.",
        (E2RArchetype.REGULATED_STABLECOIN_INFRA, E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY),
    ),
    Round138CaseCandidate(
        "terrausd_do_kwon_case",
        "ALGORITHMIC_STABLECOIN_FAILURE",
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
        ("depeg_event_flag", "reserve_failure", "fraud", "algorithmic_stablecoin_failure", "investor_loss_40b"),
        "algorithmic_stablecoin_thesis_break",
        "needs_source_date_and_price_backfill",
        ("round_138.md Reuters TerraUSD Do Kwon",),
        "The document gives a 2022~2025 range, so no exact stage date is invented.",
        (E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY, E2RArchetype.DIGITAL_ASSET_TOKENIZATION),
    ),
    Round138CaseCandidate(
        "hana_bank_dunamu_stake_case",
        "BANK_DIGITAL_ASSET_EQUITY_STAKE",
        "086790_DUNAMU_REF",
        "Hana Bank Dunamu / Upbit equity-stake watch",
        "KR",
        "success_candidate",
        None,
        date(2026, 5, 14),
        None,
        None,
        None,
        ("bank_exchange_equity_stake", "equity_stake_purchase_amount_700m", "upbit_market_share", "digital_asset_partnership"),
        ("equity_method_income_unverified", "crypto_trading_value_drop", "exchange_security_incident", "regulatory_investigation", "stake_impairment"),
        "bank_digital_asset_stake_watch",
        "needs_price_backfill",
        ("round_138.md Reuters Hana Bank Dunamu stake",),
        "A bank exchange stake is strategic Stage 1/2 evidence; Green waits for equity-method income, collaboration revenue, regulation, and security stability.",
        (E2RArchetype.DIGITAL_ASSET_EXCHANGE_CONSOLIDATION, E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY),
    ),
    Round138CaseCandidate(
        "dunamu_naver_financial_merger_option_case",
        "DIGITAL_ASSET_EXCHANGE_CONSOLIDATION",
        "DUNAMU_NAVER_FINANCIAL_REF",
        "Dunamu / Naver Financial merger option",
        "KR",
        "success_candidate",
        None,
        None,
        None,
        None,
        None,
        ("fintech_exchange_merger_flag", "share_swap_ratio_2_54", "naver_financial_distribution", "crypto_exchange_market_share", "payment_distribution_cross_sell"),
        ("regulatory_approval_missing", "shareholder_approval_missing", "exchange_security_incident_risk", "crypto_trading_value_drop", "deal_dilution"),
        "digital_asset_exchange_consolidation_option",
        "needs_exact_stage_date_backfill",
        ("round_138.md WSJ Dunamu Naver Financial merger option",),
        "A Dunamu-Naver Financial share-swap option is Stage 1/2 until approvals, fee revenue, platform cross-sell, and security stability are verified.",
        (E2RArchetype.PAYMENT_FINTECH_INFRA, E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_STAKE),
    ),
    Round138CaseCandidate(
        "digital_asset_exchange_security_cycle_case",
        "DIGITAL_ASSET_EXCHANGE_CONSOLIDATION",
        "CRYPTO_EXCHANGE_SECURITY_REF",
        "Digital asset exchange security and cycle break reference",
        "GLOBAL",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        None,
        ("crypto_exchange_market_share", "crypto_trading_volume", "exchange_fee_revenue"),
        ("abnormal_crypto_withdrawal", "exchange_security_incident", "customer_compensation_cost", "regulatory_investigation", "crypto_trading_value_drop"),
        "digital_asset_exchange_security_cycle_4c_watch",
        "needs_named_case_and_price_backfill",
        ("round_138.md digital asset exchange security cycle checklist",),
        "Exchange exposure must keep security, regulatory, and crypto-cycle failure paths separate from strategic stake narratives.",
        (E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_STAKE, E2RArchetype.STABLECOIN_CONVERTIBILITY_OVERLAY),
    ),
    Round138CaseCandidate(
        "korea_pf_credit_cost_overlay_case",
        "BANK_CREDIT_COST_PF_OVERLAY",
        "KOREA_PF_CREDIT_REF",
        "Korea real-estate PF credit-cost overlay",
        "KR",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2024, 5, 13),
        ("pf_exposure", "pf_delinquency_rate_2_70pct", "syndicated_loan_support", "reserve_build", "capital_buffer_check"),
        ("pf_delinquency_spike", "credit_cost_spike", "reserve_build", "cet1_pressure", "dividend_buyback_cut_risk"),
        "pf_credit_cost_valueup_hard_cap",
        "missing_direct_symbol_mapping",
        ("round_138.md Reuters Korean PF restructuring scrutiny",),
        "PF delinquency and reserve burden are sector-level hard gates for bank, insurance, and securities value-up.",
        (
            E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET,
            E2RArchetype.BANK_HOLDING_VALUEUP_CAPITAL_RETURN,
            E2RArchetype.INSURANCE_CAPITAL_RELEASE_VALUEUP,
        ),
    ),
    Round138CaseCandidate(
        "bybit_exchange_hack_case",
        "EXCHANGE_SECURITY_OPERATIONAL_RISK",
        "BYBIT_HACK_REF",
        "Bybit exchange security hard 4C",
        "GLOBAL",
        "4c_thesis_break",
        None,
        None,
        None,
        None,
        date(2025, 2, 27),
        ("crypto_exchange_market_share", "crypto_trading_volume", "exchange_fee_revenue", "large_user_base"),
        ("exchange_security_incident", "wallet_compromise", "hack_amount_1_5b", "north_korea_attribution", "customer_compensation_cost", "trust_damage"),
        "exchange_security_operational_hard_4c",
        "missing_public_price_data",
        ("round_138.md Reuters FBI Bybit hack attribution",),
        "Exchange market share and fee revenue must be capped when wallet compromise, compensation cost, regulation, or trust damage appears.",
        (
            E2RArchetype.DIGITAL_ASSET_EXCHANGE_CONSOLIDATION,
            E2RArchetype.BANK_DIGITAL_ASSET_EQUITY_STAKE,
        ),
    ),
)


ROUND138_PRICE_FIELDS: tuple[str, ...] = (
    "case_id", "symbol", "company_name", "primary_archetype", "secondary_archetypes",
    "stage1_date", "stage2_date", "stage3_date", "stage4b_date", "stage4c_date",
    "stage1_price", "stage2_price", "stage3_price", "stage4b_price", "stage4c_price", "peak_price", "peak_date",
    "MFE_30D", "MFE_90D", "MFE_180D", "MFE_1Y", "MFE_2Y",
    "MAE_30D", "MAE_90D", "MAE_180D", "MAE_1Y",
    "drawdown_after_peak", "below_stage2_price_flag", "below_stage3_price_flag",
    "roe", "roa", "pbr", "pbr_band_before", "pbr_band_after",
    "cet1_ratio", "k_ics_ratio", "csm_growth", "csm_quality_signal", "loss_ratio", "credit_cost", "pf_exposure", "pf_delinquency_rate", "reserve_build", "npl_ratio",
    "dividend_payout_ratio", "dividend_growth", "dividend_per_share", "buyback_amount", "buyback_cancelled_flag",
    "treasury_share_cancel_amount", "treasury_share_cancel_deadline", "treasury_share_cancel_execution_date", "treasury_share_cancel_required_flag",
    "treasury_cancel_mandate_flag", "existing_treasury_grace_period_flag",
    "shareholder_return_policy", "shareholder_return_execution_flag", "buyback_only_flag",
    "nav_value", "nav_discount", "holding_company_discount", "subsidiary_stake_value", "asset_sale_flag", "independent_director_flag",
    "activist_campaign_flag", "activist_proposal_rejection_flag", "minority_shareholder_protection_flag",
    "tender_offer_flag", "tender_offer_price", "governance_event_flag", "share_issuance_flag", "share_issuance_amount",
    "share_issuance_after_tender_flag", "debt_to_equity_change", "capital_structure_risk_flag", "unfair_trading_probe_flag",
    "trading_value", "brokerage_revenue", "ib_fee_revenue", "ipo_pipeline_count", "vc_exit_volume", "proprietary_trading_gain_loss",
    "transaction_tax_change_flag", "capital_gains_tax_change_flag", "capital_gains_tax_threshold_change_flag",
    "securities_transaction_tax_hike_flag", "corporate_tax_change_flag", "corporate_tax_hike_flag",
    "dividend_tax_change_flag", "dividend_tax_uncertainty_flag", "ai_windfall_tax_comment_flag", "citizen_dividend_comment_flag", "market_wide_selloff_flag",
    "payment_volume", "take_rate", "active_users", "merchant_count", "financial_service_attach_rate", "credit_loss_rate",
    "security_incident_flag", "fcf_margin", "ipo_valuation", "ipo_timeline_status", "ipo_size_cut_flag", "ipo_valuation_cut_flag", "crypto_exposure_flag",
    "stablecoin_issued_amount", "stablecoin_circulation", "stablecoin_transaction_volume", "reserve_asset_type", "reserve_income",
    "reserve_yield", "reserve_yield_sensitivity", "redemption_reserve_ratio", "redemption_at_par_flag",
    "convertibility_risk_flag", "regulatory_approval_flag", "user_cap_flag",
    "unremunerated_reserve_requirement_flag", "depeg_event_flag", "algorithmic_stablecoin_flag", "krw_stablecoin_flag", "bank_deposit_disintermediation_flag",
    "crypto_exchange_market_share", "crypto_trading_volume", "exchange_fee_revenue", "exchange_operator_stake_pct",
    "equity_stake_purchase_amount", "equity_method_income", "bank_exchange_partnership_flag", "strategic_collaboration_revenue",
    "fintech_exchange_merger_flag", "share_swap_ratio", "regulatory_approval_status", "shareholder_approval_status",
    "abnormal_withdrawal_flag",
    "exchange_security_incident_flag", "wallet_compromise_flag", "hack_amount", "customer_compensation_cost", "trust_damage_flag",
    "regulatory_investigation_flag", "deal_dilution_flag",
    "opendart_rcept_no", "opendart_detail_fetched_flag", "disclosure_confidence_score", "detail_parser_confidence",
    "disclosure_signal_class", "routine_disclosure_flag", "risk_disclosure_flag", "high_signal_disclosure_flag",
    "score_price_alignment", "price_validation_status", "review_notes",
)


def round138_target_for(target_id: str) -> Round138ScoreTarget | None:
    for target in ROUND138_SCORE_TARGETS:
        if target.target_id == target_id:
            return target
    return None


def round138_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND138_CASE_CANDIDATES:
        target = round138_target_for(candidate.target_id)
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
                f"Round138 R6 Loop-8 case for {candidate.target_id}; "
                "low-PBR, value-up, fintech, stablecoin, and exchange narratives are separated from execution evidence."
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
                "exchange_market_share_is_not_security_cleanliness",
                "algorithmic_stablecoin_is_hard_4c",
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


def round138_score_profile_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for target in ROUND138_SCORE_TARGETS:
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
                "loop8_penalty_axes": "|".join(target.loop8_penalty_axes),
                "gate_only": str(target.gate_only).lower(),
                "production_scoring_changed": str(target.production_scoring_changed).lower(),
                "normalization_point": target.normalization_point,
            }
        )
    return tuple(rows)


def round138_case_candidate_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND138_CASE_CANDIDATES:
        target = round138_target_for(candidate.target_id)
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


def round138_stage_date_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "target_id": target.target_id,
            "stage1": "|".join(target.stage1_signals),
            "stage2": "|".join(target.stage2_signals),
            "stage3": "|".join(target.stage3_conditions),
            "stage4b": "|".join(target.stage4b_conditions),
            "stage4c": "|".join(target.stage4c_conditions),
            "red_flags": "|".join(target.red_flags),
            "loop8_penalty_axes": "|".join(target.loop8_penalty_axes),
            "gate_only": str(target.gate_only).lower(),
            "production_scoring_changed": "false",
        }
        for target in ROUND138_SCORE_TARGETS
    )


def round138_price_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round138_backfill": "true"} for field in ROUND138_PRICE_FIELDS)


def round138_base_score_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "component": row.component,
            "weight": str(row.weight),
            "interpretation": row.interpretation,
            "production_scoring_changed": "false",
        }
        for row in ROUND138_BASE_SCORE_WEIGHTS
    )


def round138_stage_cap_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "cap_id": row.cap_id,
            "max_stage": row.max_stage,
            "condition": row.condition,
            "example": row.example,
            "production_scoring_changed": "false",
        }
        for row in ROUND138_STAGE_CAPS
    )


def round138_score_stage_price_alignment_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "case_id": row.case_id,
            "score_stage": row.score_stage,
            "price_path_signal": row.price_path_signal,
            "verdict": row.verdict,
            "normalization_adjustment": row.normalization_adjustment,
            "production_scoring_changed": "false",
        }
        for row in ROUND138_SCORE_STAGE_PRICE_ALIGNMENT
    )


def round138_summary() -> dict[str, int | bool]:
    records = round138_case_records()
    return {
        "target_count": len(ROUND138_SCORE_TARGETS),
        "case_candidate_count": len(records),
        "base_score_component_count": len(ROUND138_BASE_SCORE_WEIGHTS),
        "stage_cap_count": len(ROUND138_STAGE_CAPS),
        "score_stage_price_alignment_count": len(ROUND138_SCORE_STAGE_PRICE_ALIGNMENT),
        "structural_success_count": sum(1 for record in records if record.case_type == "structural_success"),
        "success_candidate_count": sum(1 for record in records if record.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for record in records if record.case_type == "failed_rerating"),
        "cyclical_success_count": sum(1 for record in records if record.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for record in records if record.case_type == "event_premium"),
        "overheat_count": sum(1 for record in records if record.case_type == "overheat"),
        "stage4b_case_count": sum(1 for record in records if record.case_type == "4b_watch" or record.stage4b_date),
        "stage4c_case_count": sum(1 for record in records if record.case_type == "4c_thesis_break"),
        "green_possible_count": sum(1 for target in ROUND138_SCORE_TARGETS if target.posture == Round10ThemePosture.GREEN_POSSIBLE),
        "watch_yellow_first_count": sum(1 for target in ROUND138_SCORE_TARGETS if target.posture == Round10ThemePosture.WATCH_YELLOW_FIRST),
        "redteam_first_count": sum(1 for target in ROUND138_SCORE_TARGETS if target.posture == Round10ThemePosture.REDTEAM_FIRST),
        "gate_only_target_count": sum(1 for target in ROUND138_SCORE_TARGETS if target.gate_only),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def write_round138_r6_loop8_reports(
    *,
    output_directory: str | Path = ROUND138_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND138_DEFAULT_CASES_PATH,
    score_profile_path: str | Path = ROUND138_DEFAULT_SCORE_PROFILE_PATH,
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
        "summary": output / "round138_r6_loop8_financial_capital_digital_summary.md",
        "case_matrix": output / "round138_r6_loop8_case_matrix.csv",
        "stage_date_plan": output / "round138_r6_loop8_stage_date_plan.csv",
        "green_guardrails": output / "round138_r6_loop8_green_guardrails.md",
        "risk_overlays": output / "round138_r6_loop8_risk_overlays.md",
        "price_validation_plan": output / "round138_r6_loop8_price_validation_plan.md",
        "price_fields": output / "round138_r6_loop8_price_fields.csv",
        "base_score_weights": output / "round138_r6_loop8_base_score_weights.csv",
        "stage_caps": output / "round138_r6_loop8_stage_caps.csv",
        "score_stage_price_alignment": output / "round138_r6_loop8_score_stage_price_alignment.csv",
        "score_stage_price_alignment_md": output / "round138_r6_loop8_score_stage_price_alignment.md",
    }
    _write_case_jsonl(round138_case_records(), cases)
    _write_rows(round138_score_profile_rows(), score_profiles)
    _write_rows(round138_case_candidate_rows(), paths["case_matrix"])
    _write_rows(round138_stage_date_rows(), paths["stage_date_plan"])
    _write_rows(round138_price_field_rows(), paths["price_fields"])
    _write_rows(round138_base_score_weight_rows(), paths["base_score_weights"])
    _write_rows(round138_stage_cap_rows(), paths["stage_caps"])
    _write_rows(round138_score_stage_price_alignment_rows(), paths["score_stage_price_alignment"])
    paths["summary"].write_text(render_round138_summary_markdown(), encoding="utf-8")
    paths["green_guardrails"].write_text(render_round138_green_guardrail_markdown(), encoding="utf-8")
    paths["risk_overlays"].write_text(render_round138_risk_overlay_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round138_price_validation_plan_markdown(), encoding="utf-8")
    paths["score_stage_price_alignment_md"].write_text(
        render_round138_score_stage_price_alignment_markdown(),
        encoding="utf-8",
    )
    return paths


def render_round138_summary_markdown() -> str:
    summary = round138_summary()
    lines = [
        "# Round-138 R6 Loop-8 Financial / Capital / Digital Summary",
        "",
        f"- source_round: `{ROUND138_SOURCE_ROUND_PATH}`",
        "- large_sector: `FINANCIAL_CAPITAL_DIGITAL`",
        "- loop: `R6 Loop 8 / v8.0`",
        f"- target_count: {summary['target_count']}",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- base_score_component_count: {summary['base_score_component_count']}",
        f"- stage_cap_count: {summary['stage_cap_count']}",
        f"- score_stage_price_alignment_count: {summary['score_stage_price_alignment_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
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
        "- R6 Loop 8 says low PBR, value-up policy, and digital-asset labels are not enough; execution decides.",
        "- Example: buyback is useful, but completed cancellation plus ROE/FCF path is stronger evidence.",
        "- Example: treasury-cancel mandate is macro tailwind; individual names still need actual cancellation and ROE/PBR change.",
        "- Example: bank holding value-up needs ROE, CET1, credit cost, PF exposure, and executed return, not low PBR alone.",
        "- Example: Korea Zinc tender events are event premium first, not structural value-up.",
        "- Example: fintech user count and IPO optionality are Stage 1 unless take rate, FCF, security, and credit loss are visible.",
        "- Example: KRW stablecoin intent is an option; regulation, reserve, redemption, volume, and fee economics decide later.",
        "- Example: a bank's exchange stake is Stage 1/2 until equity-method income, collaboration revenue, regulation, and security are visible.",
        "- Example: regulated stablecoin and algorithmic stablecoin must be separated before any score discussion.",
    ]
    return "\n".join(lines) + "\n"


def render_round138_green_guardrail_markdown() -> str:
    lines = [
        "# Round-138 R6 Loop-8 Green Guardrails",
        "",
        "| target | posture | Green unlock evidence | Loop-8 penalties |",
        "| --- | --- | --- | --- |",
    ]
    for target in ROUND138_SCORE_TARGETS:
        lines.append(
            "| "
            f"`{target.target_id}` | {target.posture.value} | "
            f"{', '.join(target.green_conditions) or 'not_applicable'} | {', '.join(target.loop8_penalty_axes)} |"
        )
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply R6 Loop-8 v8.0 weights to production scoring yet.",
            "- Do not treat low PBR, value-up index inclusion, buyback announcement, user count, IPO optionality, exchange stake, exchange market share, or stablecoin law news as Green evidence by themselves.",
            "- Do not equate buyback with cancellation.",
            "- Do not invent ROE, CET1, K-ICS, CSM, cancellation amount, cancellation completion, take rate, FCF, reserve ratio, stablecoin volume, equity-method income, collaboration revenue, exchange security status, or stage prices.",
            "- Treat governance execution failure, tax policy shock, stablecoin convertibility failure, algorithmic stablecoin failure, and exchange security incidents as RedTeam overlays.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round138_risk_overlay_markdown() -> str:
    lines = [
        "# Round-138 R6 Loop-8 Risk Overlays",
        "",
        "- `VALUEUP_EXECUTION_ALIGNED`: actual cancellation, dividend, ROE, and price rerating move together.",
        "- `TREASURY_CANCEL_POLICY_ONLY`: mandate or policy news is not individual execution.",
        "- `BUYBACK_ONLY_REBOUND`: buyback or policy news creates a short rebound without completed cancellation or ROE/FCF improvement.",
        "- `BUYBACK_CANCEL_BUT_BUSINESS_RISK`: cancellation exists, but business EPS/FCF path or competitive position fails.",
        "- `HOLDING_NAV_DISCOUNT_REDUCTION`: NAV discount narrows with actual cancellation, governance, or asset-value action.",
        "- `EVENT_PREMIUM_NOT_VALUEUP`: tender offer, control battle, or defense financing is not structural value-up.",
        "- `TAX_POLICY_SHOCK`: transaction, capital-gains, corporate, dividend, or AI windfall tax comment damages the price path.",
        "- `AI_CITIZEN_DIVIDEND_POLICY_SHOCK`: AI or citizen-dividend policy comments can unwind crowded AI/value-up rallies.",
        "- `FINTECH_USER_GROWTH_NO_FCF`: users grow but take rate, FCF, security, and credit loss are unverified.",
        "- `FINTECH_IPO_VALUATION_COMPRESSION`: IPO size cuts, valuation cuts, crypto exposure, or investor caution block Green.",
        "- `KRW_STABLECOIN_OPTION_NOT_REVENUE`: KRW stablecoin intent is not regulated revenue before approval, reserve, redemption, and fees.",
        "- `REGULATED_STABLECOIN_INFRA`: approval, reserve, redemption, volume, and fees are visible.",
        "- `STABLECOIN_REGULATION_FLUID_WATCH`: user caps, unremunerated reserves, or bank-deposit impact can change issuer economics.",
        "- `ALGORITHMIC_STABLECOIN_4C`: de-peg, reserve failure, algorithmic design, or fraud is a hard thesis break.",
        "- `BANK_DIGITAL_ASSET_STAKE_WATCH`: bank exchange stakes need equity-method income, collaboration revenue, regulation, and security proof.",
        "- `DIGITAL_ASSET_EXCHANGE_SECURITY_4C`: exchange consolidation is blocked by abnormal withdrawal, security incident, or regulatory probe.",
        "",
        "Simple example: `저PBR` is Stage 1. `ROE 개선 + CET1 안정 + 자사주 실제 소각 + PBR band 변화` can support Stage 2/3 review.",
    ]
    return "\n".join(lines) + "\n"


def render_round138_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-138 R6 Loop-8 Price Validation Plan",
        "",
        "## Method",
        "",
        "1. Assign stage dates from source evidence only.",
        "2. Store stage-date close prices from official price data.",
        "3. Calculate MFE_30D / 90D / 180D / 1Y / 2Y.",
        "4. Calculate MAE_30D / 90D / 180D / 1Y.",
        "5. Compare ROE, PBR, CET1, K-ICS, CSM, credit cost, dividends, cancellation, NAV, take rate, FCF, reserve, redemption, equity-method income, collaboration revenue, and exchange security with price path.",
        "6. Mark governance failure, event premium, tax shock, stablecoin convertibility, algorithmic stablecoin failure, and exchange security incidents explicitly.",
        "",
        "## Priority Case Checks",
        "",
        "| case_id | target | stage marker | check |",
        "| --- | --- | --- | --- |",
    ]
    for row in round138_case_candidate_rows():
        stage_date = row["stage4c_date"] or row["stage4b_date"] or row["stage3_date"] or row["stage2_date"] or row["stage1_date"] or "undated"
        lines.append(f"| `{row['case_id']}` | `{row['target_id']}` | {stage_date} | {row['price_validation_status']} |")
    lines.extend(
        [
            "",
            "## Alignment Labels",
            "",
            "- `VALUEUP_EXECUTION_ALIGNED`: actual cancellation, dividend, ROE, and price path align.",
            "- `TREASURY_CANCEL_POLICY_TAILWIND`: policy is a tailwind; individual execution is still missing.",
            "- `BUYBACK_CANCEL_BUT_BUSINESS_RISK`: cancellation happened, but price/EPS path did not confirm the thesis.",
            "- `HOLDING_NAV_DISCOUNT_REDUCTION`: NAV discount reduction follows capital allocation or governance execution.",
            "- `EVENT_PREMIUM_NOT_VALUEUP`: control premium or tender event is not structural rerating.",
            "- `TAX_POLICY_SHOCK`: tax policy damages value-up or brokerage momentum.",
            "- `AI_CITIZEN_DIVIDEND_POLICY_SHOCK`: policy comments damage crowded AI/value-up price paths.",
            "- `FINTECH_USER_GROWTH_NO_FCF`: user growth exists, economics are still missing.",
            "- `FINTECH_IPO_VALUATION_COMPRESSION`: IPO valuation or size is cut before public proof of economics.",
            "- `KRW_STABLECOIN_OPTION_NOT_REVENUE`: KRW stablecoin option exists, but approval/volume/fees are missing.",
            "- `REGULATED_STABLECOIN_INFRA`: regulated reserve/redemption/volume/fees are proven.",
            "- `STABLECOIN_REGULATION_FLUID_WATCH`: bank-deposit impact, user caps, or reserve rules can compress economics.",
            "- `ALGORITHMIC_STABLECOIN_4C`: algorithmic de-peg or reserve failure is hard 4C.",
            "- `BANK_DIGITAL_ASSET_STAKE_WATCH`: bank exchange stake is strategic, but income/revenue/security is still missing.",
            "- `DIGITAL_ASSET_EXCHANGE_SECURITY_4C`: exchange deal has security/regulatory break risk.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round138_score_stage_price_alignment_markdown() -> str:
    lines = [
        "# Round-138 R6 Loop-8 Score / Stage / Price Alignment",
        "",
        "Round 138 checks whether financial, capital-allocation, and digital-finance score interpretation matches the observed price and operating path.",
        "This is calibration material only; it does not change production scoring.",
        "",
        "| case | score-stage view | price-path signal | verdict | normalization adjustment |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in ROUND138_SCORE_STAGE_PRICE_ALIGNMENT:
        lines.append(
            "| "
            f"`{row.case_id}` | {row.score_stage} | {row.price_path_signal} | "
            f"{row.verdict} | {row.normalization_adjustment} |"
        )
    lines.extend(
        [
            "",
            "## Loop-8 Takeaway",
            "",
            "- Raise actual cancellation, repeated return execution, NAV discount plus governance action, PF/credit-cost gates, regulated stablecoin circulation/reserve income, and bank digital-asset stake visibility.",
            "- Keep low-PBR-only, buyback-only, value-up-index-only, IPO-hype-only, stablecoin-law-only, exchange-market-share-only, and algorithmic-stablecoin stories capped.",
            "- Stage 3 needs ROE/PBR band change, repeated return policy, credit-cost stability, FCF/capital-ratio durability, regulated revenue economics, and price-path alignment.",
            "- Stage 4C is explicit for PF credit cost, activist rejection, business failure after cancellation, IPO valuation cut, exchange hack, de-peg/reserve failure, regulatory-economics break, and tax shock.",
        ]
    )
    return "\n".join(lines) + "\n"


def _score_price_alignment(candidate: Round138CaseCandidate) -> str:
    if candidate.case_type == "failed_rerating":
        return "evidence_good_but_price_failed"
    if candidate.case_type in {"4b_watch", "overheat"}:
        return "price_moved_without_evidence"
    if candidate.case_type == "event_premium":
        return "price_moved_without_evidence"
    if candidate.case_type == "4c_thesis_break":
        return "false_positive_score"
    if candidate.case_type in {"structural_success", "success_candidate", "cyclical_success"}:
        return "aligned"
    return "unknown"


def _rerating_result(candidate: Round138CaseCandidate) -> str:
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
    if candidate.case_type == "failed_rerating":
        return "no_rerating"
    return "unknown" if candidate.case_type == "success_candidate" else "no_rerating"


def _score_weight_hint(target: Round138ScoreTarget) -> dict[str, float]:
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
        writer = csv.DictWriter(handle, fieldnames=tuple(rows_tuple[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows_tuple)
    return path


__all__ = [
    "ROUND138_CASE_CANDIDATES",
    "ROUND138_DEFAULT_CASES_PATH",
    "ROUND138_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND138_DEFAULT_SCORE_PROFILE_PATH",
    "ROUND138_PRICE_FIELDS",
    "ROUND138_BASE_SCORE_WEIGHTS",
    "ROUND138_SCORE_TARGETS",
    "ROUND138_SCORE_STAGE_PRICE_ALIGNMENT",
    "ROUND138_STAGE_CAPS",
    "Round138BaseScoreWeight",
    "Round138CaseCandidate",
    "Round138ScoreStagePriceAlignment",
    "Round138ScoreTarget",
    "Round138ScoreWeightDraft",
    "Round138StageCap",
    "render_round138_green_guardrail_markdown",
    "render_round138_price_validation_plan_markdown",
    "render_round138_risk_overlay_markdown",
    "render_round138_score_stage_price_alignment_markdown",
    "render_round138_summary_markdown",
    "round138_base_score_weight_rows",
    "round138_case_candidate_rows",
    "round138_case_records",
    "round138_price_field_rows",
    "round138_score_stage_price_alignment_rows",
    "round138_score_profile_rows",
    "round138_stage_cap_rows",
    "round138_stage_date_rows",
    "round138_summary",
    "round138_target_for",
    "write_round138_r6_loop8_reports",
]
