"""Round-327 R6 Loop-17 financials, capital allocation and digital-finance validation.

This module converts ``docs/round/round_327.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a securities basket can be Stage2-Actionable when KOSPI and
brokerage turnover beta are explicit. A bank does not become Green just
because the financial-groups index rose; bank-specific ROE, capital return,
credit cost and fee-income evidence still have to close.
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


ROUND327_SOURCE_ROUND_PATH = "docs/round/round_327.md"
ROUND327_ANALYST_ROUND_ID = "round_255"
ROUND327_LOOP_NAME = "R6 Loop 17"
ROUND327_LARGE_SECTOR = "FINANCIALS_CAPITAL_ALLOCATION_DIGITAL_FINANCE"
ROUND327_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND327_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round327_r6_loop17_financials_capital_digital_trigger_validation"
ROUND327_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_loop17_round255.jsonl"
ROUND327_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r6_loop17_round255.jsonl"
ROUND327_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round327_r6_loop17_financials_capital_digital_trigger_validation_audit.json"
ROUND327_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round255_r6_loop17_v1.csv"

ROUND327_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE": E2RArchetype.KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE.value,
    "VALUE_UP_CAPITAL_RETURN_HOLDCO_STAGE2_ACTIONABLE": E2RArchetype.VALUE_UP_CAPITAL_RETURN_HOLDCO_STAGE2_ACTIONABLE.value,
    "BANK_CRYPTO_EXCHANGE_STRATEGIC_STAKE_STAGE2": E2RArchetype.BANK_CRYPTO_EXCHANGE_STRATEGIC_STAKE_STAGE2.value,
    "FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_CYBER_4B": E2RArchetype.FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_CYBER_4B.value,
    "WON_STABLECOIN_RETAIL_FRENZY_STAGE2_OVERHEAT": E2RArchetype.WON_STABLECOIN_RETAIL_FRENZY_STAGE2_OVERHEAT.value,
    "BANK_STABLECOIN_POLICY_STAGE2_WITH_FX_4B": E2RArchetype.BANK_STABLECOIN_POLICY_STAGE2_WITH_FX_4B.value,
    "ELS_MISSELLING_SANCTION_4B": E2RArchetype.ELS_MISSELLING_SANCTION_4B.value,
    "SHORT_SELLING_NORMALIZATION_INFRA_STAGE2_4B": E2RArchetype.SHORT_SELLING_NORMALIZATION_INFRA_STAGE2_4B.value,
}

ROUND327_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_or_sector_index_return_at_least_5pct",
    "buyback_plus_cancellation_is_explicit",
    "holding_discount_closure_is_measurable",
    "digital_asset_stake_or_MA_value_is_explicit",
    "turnover_fee_income_or_brokerage_activity_bridge_is_plausible",
    "regulatory_approval_or_license_path_is_visible",
    "cyber_consumer_protection_ELS_or_retail_backlash_4B_is_identified_and_manageable",
)

ROUND327_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "brokerage_earnings_from_turnover_IB_or_WM_confirm",
    "recurring_buyback_cancel_policy_appears",
    "digital_asset_stake_contributes_to_fee_income_or_remittance_revenue",
    "stablecoin_law_passes_and_issuer_reserve_rules_are_clear",
    "cyber_or_custody_event_is_contained",
    "ELS_or_sales_practice_fines_are_provisioned_and_capital_impact_limited",
    "discount_or_PBR_rerating_continues_with_balance_sheet_discipline",
)

ROUND327_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "capital_return_policy_is_recurring_and_cash_flow_funded",
    "digital_finance_revenue_is_visible_not_only_equity_stake_or_theme",
    "stablecoin_framework_has_passed_with_investable_reserve_and_issuer_rules",
    "cyber_custody_AML_risk_is_controlled",
    "ELS_consumer_protection_costs_are_provisioned_and_non_recurring",
    "securities_turnover_boom_converts_into_recurring_brokerage_IB_earnings",
    "full_window_MFE_MAE_is_available_and_supportive",
)

ROUND327_GREEN_BLOCKERS: tuple[str, ...] = (
    "financial_group_index_without_company_trigger",
    "buyback_without_cancellation",
    "one_off_buyback_without_recurring_policy",
    "crypto_stake_without_earnings",
    "stablecoin_theme_without_regulation",
    "cyber_incident_ignored",
    "ELS_sanction_ignored",
    "short_selling_retail_backlash_ignored",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND327_SCORE_UP_AXES: tuple[str, ...] = (
    "securities_turnover_beta",
    "market_infrastructure_liquidity",
    "capital_return_cancellation",
    "holding_discount_closure",
    "digital_asset_strategic_stake",
    "stablecoin_policy_optionality",
    "MAU_fee_income_conversion",
    "consumer_protection_risk",
    "cyber_custody_risk",
)

ROUND327_SCORE_DOWN_AXES: tuple[str, ...] = (
    "financials_index_without_company_trigger",
    "buyback_without_cancellation",
    "one_off_buyback_without_recurring_policy",
    "crypto_stake_without_earnings",
    "stablecoin_theme_without_regulation",
    "cyber_incident_ignored",
    "ELS_sanction_ignored",
    "short_selling_retail_backlash_ignored",
)

ROUND327_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "securities_beta_after_market_overheat",
    "buyback_not_recurring",
    "crypto_stake_without_earnings_contribution",
    "stablecoin_theme_without_law_reserve_or_issuer_rules",
    "cyber_or_abnormal_withdrawal_at_crypto_exchange",
    "ELS_or_mis_selling_sanctions",
    "short_selling_retail_backlash",
    "FX_liquidity_pressure_from_dollar_stablecoin_trading",
)

ROUND327_HARD_4C_GATES: tuple[str, ...] = (
    "bank_capital_impairment_from_regulatory_penalties",
    "crypto_custody_failure_causing_unrecoverable_customer_loss",
    "stablecoin_issuer_collapse_or_reserve_mismatch",
    "repeated_mis_selling_sanctions_damaging_funding_or_trust",
    "broker_liquidity_or_credit_event_from_retail_leverage_or_market_crash",
)

ROUND327_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_reported_event_return_deal_policy_penalty_or_market_infra_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
    "do_not_treat_financial_beta_buyback_crypto_stake_stablecoin_or_short_selling_headline_as_Green_without_earnings_revenue_regulatory_or_risk_closure",
)


@dataclass(frozen=True)
class Round327TriggerRecord:
    trigger_id: str
    case_id: str
    trigger_type: str
    trigger_date: str
    evidence_available: str
    event_return_pct: float | str | None
    trigger_outcome_label: str
    promote_to: str
    extra_metrics: Mapping[str, object]

    def as_dict(self) -> dict[str, object]:
        return {
            "trigger_id": self.trigger_id,
            "case_id": self.case_id,
            "trigger_type": self.trigger_type,
            "trigger_date": self.trigger_date,
            "evidence_available": self.evidence_available,
            "event_return_pct": self.event_return_pct,
            "trigger_outcome_label": self.trigger_outcome_label,
            "promote_to": self.promote_to,
            "extra_metrics": dict(self.extra_metrics),
        }

    def as_row(self) -> dict[str, str]:
        row = {key: _value_text(value) for key, value in self.as_dict().items() if key != "extra_metrics"}
        row["extra_metrics"] = json.dumps(self.extra_metrics, ensure_ascii=False, sort_keys=True)
        return row


@dataclass(frozen=True)
class Round327ShadowWeightRow:
    archetype: E2RArchetype
    securities_turnover_beta: int
    market_infrastructure_liquidity: int
    capital_return_cancellation: int
    holding_discount_closure: int
    digital_asset_strategic_stake: int
    stablecoin_policy_optionality: int
    mau_fee_income_conversion: int
    consumer_protection_risk: int
    cyber_custody_risk: int
    financials_index_without_company_trigger_penalty: int
    buyback_without_cancellation_penalty: int
    crypto_stake_without_earnings_penalty: int
    stablecoin_theme_without_regulation_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "securities_turnover_beta": _signed(self.securities_turnover_beta),
            "market_infrastructure_liquidity": _signed(self.market_infrastructure_liquidity),
            "capital_return_cancellation": _signed(self.capital_return_cancellation),
            "holding_discount_closure": _signed(self.holding_discount_closure),
            "digital_asset_strategic_stake": _signed(self.digital_asset_strategic_stake),
            "stablecoin_policy_optionality": _signed(self.stablecoin_policy_optionality),
            "MAU_fee_income_conversion": _signed(self.mau_fee_income_conversion),
            "consumer_protection_risk": _signed(self.consumer_protection_risk),
            "cyber_custody_risk": _signed(self.cyber_custody_risk),
            "financials_index_without_company_trigger_penalty": _signed(self.financials_index_without_company_trigger_penalty),
            "buyback_without_cancellation_penalty": _signed(self.buyback_without_cancellation_penalty),
            "crypto_stake_without_earnings_penalty": _signed(self.crypto_stake_without_earnings_penalty),
            "stablecoin_theme_without_regulation_penalty": _signed(self.stablecoin_theme_without_regulation_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round327CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    round_case_type: str
    best_trigger: str
    best_trigger_type: str
    stage_candidate: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    hard_4c_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    extra_price_metrics: Mapping[str, object]
    score_price_alignment: str
    round_alignment_label: str
    rerating_result: str
    stage_failure_type: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type

    def to_case_record(self) -> E2RCaseRecord:
        guardrails = [
            "production_scoring_changed_false",
            "candidate_generation_input_false",
            "shadow_weight_only_true",
            "full_adjusted_ohlc_complete_false",
            "do_not_use_round327_cases_as_candidate_generation_input",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_financial_beta_buyback_crypto_stake_stablecoin_or_short_selling_headline_as_Green_without_earnings_revenue_regulatory_or_risk_closure",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")

        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "cyber" in field
            or "ELS" in field
            or "stablecoin" in field
            or "retail_backlash" in field
            or "FX" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field or "4c" in field or "hard" in field or "capital_impairment" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND327_LARGE_SECTOR,
            large_sector=ROUND327_LARGE_SECTOR,
            primary_archetype=self.primary_archetype,
            secondary_archetypes=self.secondary_archetypes,
            expected_group=self.expected_group,
            case_type=self.case_type,
            stage1_date=self.stage1_date,
            stage2_date=self.stage2_date,
            stage3_date=self.stage3_date,
            stage4b_date=self.stage4b_date,
            stage4c_date=self.stage4c_date,
            evidence_summary=self.notes,
            stage1_evidence=self.evidence_fields,
            stage2_evidence=self.evidence_fields if self.stage2_date else (),
            stage3_evidence=self.evidence_fields if self.stage3_date else (),
            stage4b_evidence=stage4b_evidence,
            stage4c_evidence=stage4c_evidence,
            must_have_fields=ROUND327_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.case_type in {"event_premium", "4b_watch", "overheat", "failed_rerating"} else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern="reported_event_anchor_only",
            score_weight_hint={},
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(price_validation_status="price_data_unavailable_after_deep_search"),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8,
            ),
        )

    def as_row(self) -> dict[str, str]:
        return {
            "case_id": self.case_id,
            "symbol": self.symbol,
            "company_name": self.company_name,
            "primary_archetype": self.primary_archetype.value,
            "secondary_archetypes": "|".join(archetype.value for archetype in self.secondary_archetypes),
            "case_type": self.case_type,
            "round_case_type": self.round_case_type,
            "best_trigger": self.best_trigger,
            "best_trigger_type": self.best_trigger_type,
            "stage_candidate": self.stage_candidate,
            "stage1_date": _date_text(self.stage1_date),
            "stage2_date": _date_text(self.stage2_date),
            "stage3_date": _date_text(self.stage3_date),
            "stage4b_date": _date_text(self.stage4b_date),
            "stage4c_date": _date_text(self.stage4c_date),
            "hard_4c_confirmed": str(self.hard_4c_confirmed).lower(),
            "evidence_fields": "|".join(self.evidence_fields),
            "red_flag_fields": "|".join(self.red_flag_fields),
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND327_CASE_CANDIDATES: tuple[Round327CaseCandidate, ...] = (
    Round327CaseCandidate(
        "r6_loop17_kospi_boom_securities_financials",
        "039490/005940/016360/071050/105560/055550/086790/316140",
        "Korea securities and financial groups basket",
        E2RArchetype.KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE,
        (E2RArchetype.BROKERAGE_TRADING_VOLUME_STAGE2_BETA, E2RArchetype.BANK_VALUE_UP_RERATING_STAGE2),
        "success_candidate",
        "Stage2_Actionable_brokerage_beta_with_market_4B",
        "T2/T3",
        "Stage2-Actionable_brokerage_beta",
        "Stage2-Actionable",
        date(2026, 5, 6),
        date(2026, 5, 6),
        None,
        date(2026, 5, 6),
        None,
        False,
        ("KOSPI_plus_6_45pct", "securities_firms_index_plus_13_5pct", "financial_groups_index_plus_4_2pct", "stock_market_turnover_beta", "brokerage_fee_beta", "IB_and_WM_activity"),
        ("AI_concentration_4B", "market_correction_4B", "retail_leverage_4B", "tax_hike_4B", "short_selling_volatility_4B", "banks_not_green_from_index_beta"),
        {"trigger_date": "2026-05-06", "kospi_event_return_pct": 6.45, "securities_firms_index_event_return_pct": 13.5, "financial_groups_index_event_return_pct": 4.2},
        "aligned",
        "excellent_stage2_actionable_for_securities_not_bank_green",
        "event_premium",
        "stage2_watch_success",
        "Securities beta is clear from the KOSPI boom, but banks need company-specific capital return and earnings validation.",
    ),
    Round327CaseCandidate(
        "r6_loop17_sk_square_buyback_holding_discount",
        "402340",
        "SK Square",
        E2RArchetype.VALUE_UP_CAPITAL_RETURN_HOLDCO_STAGE2_ACTIONABLE,
        (E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_STAGE2, E2RArchetype.HOLDCO_DISCOUNT_ACTIVIST_STAGE2),
        "success_candidate",
        "Stage2_Actionable_capital_return_holding_discount",
        "T1/T3",
        "Stage2-Actionable_capital_return",
        "Stage2-Actionable",
        date(2024, 11, 21),
        date(2024, 11, 21),
        None,
        date(2024, 11, 21),
        None,
        False,
        ("prior_buyback_cancel_100B_won", "new_buyback_cancel_100B_won", "SK_Hynix_stake_value_18B_usd_context", "market_value_less_than_half_of_stake_value", "Palliser_activist_1pct_stake"),
        ("one_off_buyback_risk_4B", "portfolio_monetization_uncertain", "SK_Hynix_price_dependence", "holding_company_discount_persistence"),
        {"trigger_date": "2024-11-21", "prior_buyback_cancel_krw_bn": 100, "new_buyback_cancel_krw_bn": 100, "sk_hynix_stake_value_context_usd_bn": 18, "market_value_vs_stake_value_context": "less_than_half"},
        "aligned",
        "capital_return_stage2_actionable_no_ohlc",
        "event_premium",
        "stage2_watch_success",
        "Buyback plus cancellation and measurable holding discount make SK Square Stage2-Actionable, but recurring policy is the Yellow gate.",
    ),
    Round327CaseCandidate(
        "r6_loop17_hana_bank_dunamu_stake",
        "086790/Dunamu_private/035720_seller_readthrough",
        "Hana Bank / Dunamu / Kakao Investment",
        E2RArchetype.BANK_CRYPTO_EXCHANGE_STRATEGIC_STAKE_STAGE2,
        (E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE, E2RArchetype.DIGITAL_ASSET_BANK_ENTRY_STAGE2),
        "success_candidate",
        "Stage2_bank_crypto_exchange_strategic_stake",
        "T0/T3",
        "Stage2_bank_crypto_exchange_stake",
        "Stage2",
        date(2026, 5, 14),
        date(2026, 5, 14),
        None,
        date(2026, 5, 14),
        None,
        False,
        ("Hana_Bank_Dunamu_stake_6_55pct", "deal_value_1T_won", "Upbit_more_than_80pct_Korea_virtual_asset_volume", "digital_asset_strategy", "blockchain_remittance", "fee_income_optionality"),
        ("crypto_regulation_4B", "Upbit_operational_risk_4B", "valuation_risk", "capital_allocation_risk", "earnings_contribution_missing"),
        {"trigger_date": "2026-05-14", "deal_value_krw_trn": 1.0, "deal_value_usd_mn": 700, "hana_bank_dunamu_stake_pct": 6.55, "upbit_korea_virtual_asset_volume_share_pct": ">80", "kakao_investment_post_sale_stake_pct": 4.03},
        "aligned",
        "Stage2_digital_asset_stake_no_direct_price",
        "event_premium",
        "stage2_watch_success",
        "Strategic crypto exposure is real; fee-income, remittance revenue, regulation and bank capital treatment are the next gates.",
    ),
    Round327CaseCandidate(
        "r6_loop17_naver_financial_dunamu_merger",
        "035420/Dunamu_private/Naver_Financial_private",
        "Naver Financial / Dunamu / Upbit",
        E2RArchetype.FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_CYBER_4B,
        (E2RArchetype.FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4B, E2RArchetype.CRYPTO_EXCHANGE_OPERATIONAL_HARD_REFERENCE),
        "event_premium",
        "Stage2_fintech_crypto_MA_with_cyber_4B",
        "T0/T3",
        "Stage2_fintech_crypto_MA",
        "Stage2 + 4B-watch",
        date(2025, 11, 27),
        date(2025, 11, 27),
        None,
        date(2025, 11, 27),
        None,
        False,
        ("all_stock_deal_15_13T_won", "deal_value_10_27B_usd", "exchange_ratio_2_54_Naver_Financial_per_1_Dunamu", "Naver_initial_plus_7pct", "Upbit_abnormal_withdrawal_54B_won"),
        ("regulatory_approval_4B", "shareholder_approval_4B", "crypto_custody_cybersecurity_4B", "abnormal_withdrawal_4B", "valuation_and_Nasdaq_speculation"),
        {"trigger_date": "2025-11-27", "deal_value_krw_trn": 15.13, "deal_value_usd_bn": 10.27, "exchange_ratio": "2.54_Naver_Financial_shares_per_1_Dunamu_share", "naver_initial_event_return_pct": ">7", "naver_later_event_return_pct": -4.2, "upbit_abnormal_withdrawal_krw_bn": 54},
        "evidence_good_but_price_failed",
        "Stage2_fintech_MA_with_operational_4B",
        "event_premium",
        "stage2_watch_success",
        "The M&A value is large, but Upbit abnormal withdrawal and approval gates make this Stage2 plus operational 4B, not Green.",
    ),
    Round327CaseCandidate(
        "r6_loop17_kakao_pay_won_stablecoin_frenzy",
        "377300/012510/158430/201490",
        "Kakao Pay / LG CNS / Aton / ME2ON",
        E2RArchetype.WON_STABLECOIN_RETAIL_FRENZY_STAGE2_OVERHEAT,
        (E2RArchetype.KRW_STABLECOIN_POLICY_OVERHEAT, E2RArchetype.STABLECOIN_POLICY_EVENT_PREMIUM_4B),
        "overheat",
        "Stage2_speculative_won_stablecoin_theme_with_overheat_4B",
        "T1/T3",
        "Stage2_speculative_stablecoin_theme",
        "speculative Stage2",
        date(2025, 6, 1),
        date(2025, 6, 1),
        None,
        date(2025, 6, 1),
        None,
        False,
        ("Kakao_Pay_more_than_2x", "LG_CNS_almost_plus_70pct", "Aton_plus_80pct", "ME2ON_tripled", "margin_loans_20_5T_won"),
        ("regulatory_framework_missing_4B", "issuer_capital_threshold_risk", "BOK_non_bank_issuer_concern", "retail_leverage_4B", "theme_overheat_4B"),
        {"trigger_period": "2025-06", "kakao_pay_event_return_context": ">2x", "lg_cns_event_return_context_pct": "almost_70", "aton_event_return_context_pct": 80, "me2on_event_return_context": "tripled", "margin_loans_context_krw_trn": 20.5},
        "false_positive_score",
        "Stage2_speculative_overheat_not_Green",
        "theme_overheat",
        "should_have_been_red",
        "Stablecoin theme moved stocks strongly, but law, reserve rules, issuer capital and revenue model are missing.",
    ),
    Round327CaseCandidate(
        "r6_loop17_bok_stablecoin_kimchi_bond_fx_policy",
        "bank_payment_stablecoin_basket/377300/035420/086790",
        "BOK / bank-payment stablecoin basket",
        E2RArchetype.BANK_STABLECOIN_POLICY_STAGE2_WITH_FX_4B,
        (E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE, E2RArchetype.FX_LIQUIDITY_STABLECOIN_OUTFLOW),
        "event_premium",
        "Stage2_policy_infrastructure_with_FX_4B",
        "T0/T3",
        "Stage2_policy_infrastructure",
        "policy Stage2",
        date(2026, 4, 14),
        date(2026, 4, 14),
        None,
        date(2026, 4, 14),
        None,
        False,
        ("BOK_won_stablecoin_policy_positive", "stablecoin_trading_Q1_2025_57T_won", "stablecoin_trading_Q1_2025_42B_usd", "kimchi_bond_ban_lifted_after_14_years"),
        ("FX_liquidity_pressure_4B", "won_weakness_4B", "issuer_quality", "reserve_rules_missing", "capital_flow_volatility"),
        {"stablecoin_policy_date": "2026-04-14", "stablecoin_trading_q1_2025_krw_trn": 57, "stablecoin_trading_q1_2025_usd_bn": 42, "kimchi_bond_ban_lifted": True, "kimchi_bond_ban_duration_years": 14},
        "aligned",
        "policy_stage2_with_fx_liquidity_4B",
        "policy_event_rerating",
        "stage2_watch_success",
        "Stablecoin policy infrastructure is real, but FX liquidity and issuer/reserve rules remain 4B.",
    ),
    Round327CaseCandidate(
        "r6_loop17_hong_kong_els_bank_sanctions",
        "105560/055550/086790/316140",
        "KB / Shinhan / Hana / Woori financial groups",
        E2RArchetype.ELS_MISSELLING_SANCTION_4B,
        (E2RArchetype.ELS_MISSELLING_CONSUMER_PROTECTION_4C,),
        "4b_watch",
        "4B_bank_consumer_protection_sanction",
        "T1/T3",
        "4B_consumer_protection_sanction",
        "4B-watch",
        date(2026, 2, 12),
        None,
        None,
        date(2026, 2, 12),
        None,
        False,
        ("Hong_Kong_ELS_misselling_sanction", "FSS_planned_fines_around_1T_won", "FSC_finalization_pending", "consumer_protection_cost"),
        ("consumer_protection_4B", "sales_practice_misconduct", "compensation_cost", "capital_buffer", "trust_damage"),
        {"trigger_date": "2026-02-12", "fine_context_krw_trn": 1.0, "regulator": "Financial_Supervisory_Service", "finalization_body": "Financial_Services_Commission", "product": "Hong_Kong_equity_linked_derivatives", "hard_4C_status": "not_confirmed"},
        "aligned",
        "bank_ELS_sanction_4B_not_hard_4C",
        "no_rerating",
        "should_have_been_red",
        "ELS consumer-protection costs must be deducted before bank value-up scoring; hard stock-specific 4C is not confirmed.",
    ),
    Round327CaseCandidate(
        "r6_loop17_short_selling_normalization",
        "brokerage_basket/039490/016360/005940/071050",
        "Korea brokerage basket",
        E2RArchetype.SHORT_SELLING_NORMALIZATION_INFRA_STAGE2_4B,
        (E2RArchetype.SHORT_SELLING_MARKET_INTEGRITY_STAGE2_4B, E2RArchetype.SHORT_SELLING_MARKET_ACCESS_REFORM),
        "event_premium",
        "Stage2_market_infrastructure_with_retail_4B",
        "T1/T3",
        "Stage2_market_infrastructure",
        "Stage2 infrastructure",
        date(2025, 2, 11),
        date(2025, 2, 11),
        None,
        date(2025, 2, 11),
        None,
        False,
        ("short_selling_ban_lift_target_2025_03", "illegal_trade_detection_system", "HSBC_case_16B_won", "court_outcome_cleared", "market_infrastructure_liquidity"),
        ("retail_backlash_4B", "market_volatility_4B", "foreign_short_selling_sensitivity", "implementation_risk"),
        {"trigger_date": "2025-02-11", "ban_lift_target_month": "2025-03", "illegal_trade_detection_system": True, "hsbc_case_value_krw_bn": 16, "court_outcome": "cleared"},
        "aligned",
        "market_infrastructure_stage2_with_volatility_4B",
        "policy_event_rerating",
        "stage2_watch_success",
        "Short-selling normalization can improve liquidity, but retail backlash and volatility remain 4B until stable implementation and earnings bridge are visible.",
    ),
)

ROUND327_TRIGGER_RECORDS: tuple[Round327TriggerRecord, ...] = (
    Round327TriggerRecord("r6l17_kospi_securities_T2", "r6_loop17_kospi_boom_securities_financials", "Stage2-Actionable_brokerage_beta", "2026-05-06", "reported_event_anchor", "securities_index_+13.5_financial_groups_+4.2_kospi_+6.45", "excellent_stage2_actionable_for_brokerage_beta", "Stage2-Actionable", {"kospi_event_return_pct": 6.45, "securities_firms_index_event_return_pct": 13.5, "financial_groups_index_event_return_pct": 4.2}),
    Round327TriggerRecord("r6l17_sk_square_buyback_T1", "r6_loop17_sk_square_buyback_holding_discount", "Stage2-Actionable_capital_return", "2024-11-21", "reported_event_anchor", "price_data_unavailable_after_deep_search", "buyback_cancellation_holding_discount_stage2", "Stage2-Actionable", {"prior_buyback_cancel_krw_bn": 100, "new_buyback_cancel_krw_bn": 100}),
    Round327TriggerRecord("r6l17_hana_dunamu_T0", "r6_loop17_hana_bank_dunamu_stake", "Stage2_bank_crypto_exchange_stake", "2026-05-14", "reported_event_anchor", "price_data_unavailable_after_deep_search", "digital_asset_stake_stage2_no_price", "Stage2", {"deal_value_krw_trn": 1.0, "stake_pct": 6.55}),
    Round327TriggerRecord("r6l17_naver_dunamu_T0", "r6_loop17_naver_financial_dunamu_merger", "Stage2_fintech_crypto_MA", "2025-11-27", "reported_event_anchor", "Naver_initial_+7_then_-4.2", "Stage2_MA_with_cyber_4B", "Stage2+4B", {"deal_value_krw_trn": 15.13, "upbit_abnormal_withdrawal_krw_bn": 54}),
    Round327TriggerRecord("r6l17_upbit_withdrawal_T2", "r6_loop17_naver_financial_dunamu_merger", "4B_crypto_custody_operational", "2025-11-27", "reported_event_anchor", -4.2, "abnormal_withdrawal_4B", "4B-watch", {"upbit_abnormal_withdrawal_krw_bn": 54}),
    Round327TriggerRecord("r6l17_kakao_pay_stablecoin_T1", "r6_loop17_kakao_pay_won_stablecoin_frenzy", "Stage2_speculative_stablecoin_theme", "2025-06", "reported_event_anchor", "KakaoPay_>2x_LGCNS_+70_Aton_+80_ME2ON_tripled", "speculative_stage2_overheat", "Stage2_overheat", {"margin_loans_context_krw_trn": 20.5}),
    Round327TriggerRecord("r6l17_bok_stablecoin_policy_T0", "r6_loop17_bok_stablecoin_kimchi_bond_fx_policy", "Stage2_policy_infrastructure", "2026-04-14", "reported_event_anchor", "price_data_unavailable_after_deep_search", "stablecoin_policy_stage2_fx_4B", "Stage2", {"stablecoin_trading_q1_2025_krw_trn": 57}),
    Round327TriggerRecord("r6l17_kimchi_bond_T2", "r6_loop17_bok_stablecoin_kimchi_bond_fx_policy", "Stage2_FX_liquidity_policy", "2025-06-30", "reported_event_anchor", "price_data_unavailable_after_deep_search", "kimchi_bond_fx_liquidity_stage2", "Stage2", {"kimchi_bond_ban_lifted": True, "kimchi_bond_ban_duration_years": 14}),
    Round327TriggerRecord("r6l17_els_sanction_T1", "r6_loop17_hong_kong_els_bank_sanctions", "4B_consumer_protection_sanction", "2026-02-12", "reported_event_anchor", "price_data_unavailable_after_deep_search", "bank_ELS_sanction_4B", "4B-watch", {"fine_context_krw_trn": 1.0}),
    Round327TriggerRecord("r6l17_short_selling_normalization_T1", "r6_loop17_short_selling_normalization", "Stage2_market_infrastructure", "2025-02-11", "reported_event_anchor", "price_data_unavailable_after_deep_search", "short_selling_normalization_stage2_with_retail_4B", "Stage2", {"hsbc_case_value_krw_bn": 16}),
)

ROUND327_SHADOW_WEIGHT_ROWS: tuple[Round327ShadowWeightRow, ...] = (
    Round327ShadowWeightRow(E2RArchetype.KOSPI_BOOM_SECURITIES_STAGE2_ACTIONABLE, 5, 4, 0, 0, 0, 0, 3, 1, 1, -4, -1, -1, -1, "securities index +13.5", "brokerage earnings confirmation", "recurring brokerage/IB earnings", "KOSPI securities"),
    Round327ShadowWeightRow(E2RArchetype.VALUE_UP_CAPITAL_RETURN_HOLDCO_STAGE2_ACTIONABLE, 1, 1, 5, 5, 0, 0, 0, 0, 0, -2, -4, -1, -1, "buyback+cancel+holding discount", "recurring policy missing", "recurring buyback+discount compression", "SK Square"),
    Round327ShadowWeightRow(E2RArchetype.BANK_CRYPTO_EXCHANGE_STRATEGIC_STAKE_STAGE2, 0, 1, 0, 1, 5, 3, 5, 2, 4, -1, -1, -5, -3, "Hana 6.55% Dunamu stake", "earnings contribution missing", "fee income/remittance revenue", "Hana Bank"),
    Round327ShadowWeightRow(E2RArchetype.FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_CYBER_4B, 0, 2, 0, 0, 5, 4, 5, 3, 5, -1, -1, -4, -3, "Naver-Dunamu large M&A", "abnormal withdrawal 4B", "approval+cyber containment+revenue", "Naver"),
    Round327ShadowWeightRow(E2RArchetype.WON_STABLECOIN_RETAIL_FRENZY_STAGE2_OVERHEAT, 1, 2, 0, 0, 2, 5, 3, 2, 3, -1, -1, -3, -5, "stablecoin stock frenzy", "regulation missing", "law+reserve rules+issuer license", "Kakao Pay"),
    Round327ShadowWeightRow(E2RArchetype.BANK_STABLECOIN_POLICY_STAGE2_WITH_FX_4B, 0, 4, 0, 0, 2, 5, 2, 2, 2, -1, -1, -2, -5, "BOK stablecoin stance and kimchi bonds", "FX liquidity 4B", "licensed issuers+bank revenue model", "BOK policy basket"),
    Round327ShadowWeightRow(E2RArchetype.ELS_MISSELLING_SANCTION_4B, 0, 0, 0, 0, 0, 0, 0, 5, 1, -1, -1, -1, -1, "ELS sanctions hurt bank trust/capital", "final provision missing", "fine/provision closure", "big banks"),
    Round327ShadowWeightRow(E2RArchetype.SHORT_SELLING_NORMALIZATION_INFRA_STAGE2_4B, 4, 5, 0, 0, 0, 0, 2, 1, 0, -1, -1, -1, -1, "short-selling normalization supports liquidity", "retail backlash 4B", "turnover+broker earnings+stable implementation", "brokerage basket"),
)


def round327_case_records() -> tuple[E2RCaseRecord, ...]:
    records = tuple(candidate.to_case_record() for candidate in ROUND327_CASE_CANDIDATES)
    for record in records:
        record.validate()
    return records


def round327_case_rows() -> list[dict[str, str]]:
    return [candidate.as_row() for candidate in ROUND327_CASE_CANDIDATES]


def round327_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND327_TRIGGER_RECORDS]


def round327_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND327_SHADOW_WEIGHT_ROWS]


def round327_summary() -> dict[str, object]:
    return {
        "source_round": ROUND327_SOURCE_ROUND_PATH,
        "round_id": ROUND327_ANALYST_ROUND_ID,
        "loop_name": ROUND327_LOOP_NAME,
        "large_sector": ROUND327_LARGE_SECTOR,
        "method": ROUND327_METHOD,
        "case_candidate_count": len(ROUND327_CASE_CANDIDATES),
        "trigger_count": len(ROUND327_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND327_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": sum(1 for case in ROUND327_CASE_CANDIDATES if "Stage2-Actionable" in case.stage_candidate),
        "stage2_candidate_count": sum(1 for case in ROUND327_CASE_CANDIDATES if "Stage2" in case.stage_candidate),
        "stage3_yellow_candidate_count": sum(1 for case in ROUND327_CASE_CANDIDATES if "Yellow" in case.stage_candidate),
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": sum(1 for case in ROUND327_CASE_CANDIDATES if case.stage4b_date is not None),
        "hard_4c_case_count": sum(1 for case in ROUND327_CASE_CANDIDATES if case.hard_4c_confirmed),
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
    }


def round327_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND327_SOURCE_ROUND_PATH,
        "round_id": ROUND327_ANALYST_ROUND_ID,
        "large_sector": ROUND327_LARGE_SECTOR,
        "method": ROUND327_METHOD,
        "summary": round327_summary(),
        "target_archetypes": dict(ROUND327_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND327_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND327_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND327_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND327_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND327_SCORE_UP_AXES),
        "score_down_axes": list(ROUND327_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND327_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND327_HARD_4C_GATES),
        "row_separation_rules": list(ROUND327_ROW_SEPARATION_RULES),
        "shadow_weights": round327_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_change_production_scoring",
            "do_not_use_round327_cases_as_candidate_generation_input",
            "do_not_force_Stage3_Green",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_financial_beta_buyback_crypto_stake_stablecoin_or_short_selling_headline_as_Green_without_earnings_revenue_regulatory_or_risk_closure",
        ],
    }


def render_round327_summary_markdown() -> str:
    summary = round327_summary()
    lines = [
        "# Round 327 R6 Loop 17 Financials Capital Allocation Digital Finance Trigger Validation",
        "",
        f"- source_round: `{ROUND327_SOURCE_ROUND_PATH}`",
        f"- analyst_round_id: `{ROUND327_ANALYST_ROUND_ID}`",
        f"- large_sector: `{ROUND327_LARGE_SECTOR}`",
        f"- method: `{ROUND327_METHOD}`",
        f"- case candidates: `{summary['case_candidate_count']}`",
        f"- triggers: `{summary['trigger_count']}`",
        f"- Stage2-Actionable candidates: `{summary['stage2_actionable_candidate_count']}`",
        f"- Stage3-Yellow candidates: `{summary['stage3_yellow_candidate_count']}`",
        "- Stage3-Green confirmed: `0`",
        "- production_scoring_changed: `false`",
        "- candidate_generation_input: `false`",
        "- shadow_weight_only: `true`",
        "",
        "## 핵심 결론",
        "",
        "- KOSPI boom / securities firms는 가장 좋은 Stage2-Actionable이다. 증권주는 거래대금 beta가 직접 연결되지만, 은행은 금융지수 상승만으로 Green이 아니다.",
        "- SK Square는 buyback + cancellation + holding discount가 닫힌 capital-return Stage2-Actionable이다.",
        "- Hana Bank / Dunamu는 digital-asset strategic stake Stage2지만 은행 EPS contribution, regulation, capital treatment가 남아 있다.",
        "- Naver Financial / Dunamu는 Stage2 M&A와 cyber/custody 4B가 동시에 존재한다.",
        "- Kakao Pay / won-stablecoin은 speculative Stage2 overheat이며, 법/준비금/issuer rule 전에는 Green 금지다.",
        "- BOK stablecoin / kimchi bond policy는 Stage2 infrastructure지만 FX liquidity와 issuer-quality 4B가 크다.",
        "- Hong Kong ELS sanctions는 bank 4B로, bank value-up score에서 선차감해야 한다.",
        "- Short-selling normalization은 market-infra Stage2지만 retail backlash와 volatility 4B가 붙는다.",
    ]
    return "\n".join(lines) + "\n"


def render_round327_trigger_grid_markdown() -> str:
    lines = [
        "# Round 327 R6 Loop 17 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | date | event_return | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round327_trigger_rows():
        lines.append(
            f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |"
        )
    return "\n".join(lines) + "\n"


def render_round327_stage_rules_markdown() -> str:
    sections = [
        ("Stage2-Actionable Rules", ROUND327_STAGE2_ACTIONABLE_RULES),
        ("Stage3-Yellow Rules", ROUND327_STAGE3_YELLOW_RULES),
        ("Stage3-Green Rules", ROUND327_STAGE3_GREEN_RULES),
        ("Green Blockers", ROUND327_GREEN_BLOCKERS),
        ("Score Up Axes", ROUND327_SCORE_UP_AXES),
        ("Score Down Axes", ROUND327_SCORE_DOWN_AXES),
        ("Row Separation Rules", ROUND327_ROW_SEPARATION_RULES),
    ]
    lines = ["# Round 327 R6 Loop 17 Stage Rules", "", "Do not apply these weights to production scoring yet.", ""]
    for title, values in sections:
        lines.extend([f"## {title}", ""])
        lines.extend(f"- `{value}`" for value in values)
        lines.append("")
    return "\n".join(lines)


def render_round327_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 327 R6 Loop 17 Stage 4B / 4C Review", "", "## 4B Watch", ""]
    lines.extend(f"- `{item}`" for item in ROUND327_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- `{item}`" for item in ROUND327_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND327_CASE_CANDIDATES:
        lines.append(f"- `{case.case_id}`: {case.stage_candidate}; {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round327_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 327 R6 Loop 17 Price Validation Plan",
        "",
        "Full adjusted OHLC is not complete. Do not create MFE/MAE or peak/drawdown values from reported event anchors.",
        "",
        "| case_id | status | event anchor | next backfill |",
        "| --- | --- | --- | --- |",
    ]
    for case in ROUND327_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | price_data_unavailable_after_deep_search | {json.dumps(case.extra_price_metrics, ensure_ascii=False, sort_keys=True)} | adjusted OHLC backfill required |"
        )
    return "\n".join(lines) + "\n"


def write_round327_r6_loop17_reports(
    *,
    output_directory: str | Path = ROUND327_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND327_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND327_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND327_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND327_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    cases_path = Path(cases_path)
    triggers_path = Path(triggers_path)
    audit_path = Path(audit_path)
    weight_profile_path = Path(weight_profile_path)

    cases = write_case_library(round327_case_records(), cases_path)
    triggers = _write_jsonl(triggers_path, (trigger.as_dict() for trigger in ROUND327_TRIGGER_RECORDS))
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(json.dumps(round327_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    weights = _write_csv(weight_profile_path, round327_shadow_weight_rows())

    paths = {
        "cases": cases,
        "triggers": triggers,
        "audit": audit_path,
        "weight_profile": weights,
        "case_rows_csv": output_directory / "case_rows.csv",
        "trigger_rows_csv": output_directory / "trigger_rows.csv",
        "summary": output_directory / "round327_summary.md",
        "trigger_grid_md": output_directory / "trigger_grid.md",
        "stage_rules": output_directory / "stage_rules.md",
        "stage4b_4c_review": output_directory / "stage4b_4c_review.md",
        "price_validation_plan": output_directory / "price_validation_plan.md",
    }
    _write_csv(paths["case_rows_csv"], round327_case_rows())
    _write_csv(paths["trigger_rows_csv"], round327_trigger_rows())
    paths["summary"].write_text(render_round327_summary_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round327_trigger_grid_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round327_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round327_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round327_price_validation_plan_markdown(), encoding="utf-8")
    return paths


def _write_jsonl(path: str | Path, rows: Iterable[Mapping[str, object]]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    return path


def _write_csv(path: str | Path, rows: Iterable[Mapping[str, object]]) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path


def _signed(value: int) -> str:
    return f"{value:+d}"


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)
