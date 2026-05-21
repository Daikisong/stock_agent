"""Round-301 R6 Loop-15 financial/capital/digital trigger validation pack.

This module converts ``docs/round/round_301.md`` into calibration-only case
records, trigger rows, and reports. It does not change production scoring,
staging, or candidate generation.

Easy example: a bank can announce a digital-asset deal, but it is not Stage 3
evidence until regulatory approval, security, capital-ratio impact, and actual
revenue are visible.
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


ROUND301_SOURCE_ROUND_PATH = "docs/round/round_301.md"
ROUND301_ANALYST_ROUND_ID = "round_229"
ROUND301_LARGE_SECTOR = "FINANCIALS_CAPITAL_ALLOCATION_DIGITAL_FINANCE"
ROUND301_METHOD = "trigger_level_backtest_v1"
ROUND301_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round301_r6_loop15_financial_capital_digital_trigger_validation"
ROUND301_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_loop15_round229.jsonl"
ROUND301_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r6_loop15_round229.jsonl"
ROUND301_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round301_r6_loop15_financial_capital_digital_trigger_validation_audit.json"
ROUND301_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round229_r6_loop15_v1.csv"

ROUND301_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE": E2RArchetype.BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE.value,
    "FINANCIAL_GROUP_VALUEUP_STAGE2": E2RArchetype.FINANCIAL_GROUP_VALUEUP_STAGE2.value,
    "BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE": E2RArchetype.BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE.value,
    "HOLDCO_DISCOUNT_ACTIVIST_STAGE2": E2RArchetype.HOLDCO_DISCOUNT_ACTIVIST_STAGE2.value,
    "DIGITAL_ASSET_BANK_ENTRY_STAGE2": E2RArchetype.DIGITAL_ASSET_BANK_ENTRY_STAGE2.value,
    "CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4C": E2RArchetype.CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4C.value,
    "STABLECOIN_POLICY_4B_OVERHEAT": E2RArchetype.STABLECOIN_POLICY_4B_OVERHEAT.value,
    "FINTECH_DATA_GOVERNANCE_4C": E2RArchetype.FINTECH_DATA_GOVERNANCE_4C.value,
    "KAKAO_BANK_CONTROL_REGULATORY_4C": E2RArchetype.KAKAO_BANK_CONTROL_REGULATORY_4C.value,
}

ROUND301_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "actual_buyback_cancellation_is_disclosed",
    "cet1_or_capital_buffer_supports_return_capacity",
    "brokerage_beta_bridges_to_trading_value_margin_finance_or_ib_fee",
    "fintech_ma_has_regulatory_approval_path_and_revenue_synergy",
    "nav_discount_is_measurable_with_activist_buyback_or_asset_monetization_trigger",
    "event_or_market_relative_price_reaction_is_strong",
)

ROUND301_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "financial_trigger_likely_connects_to_earnings_but_one_gate_remains",
    "brokerage_trading_value_or_fee_income_confirmed_but_cycle_risk_remains",
    "nav_discount_narrowing_or_repeat_cancellation_visible_but_underlying_asset_risk_remains",
    "crypto_ma_security_remediation_and_regulatory_path_visible_but_revenue_durability_pending",
)

ROUND301_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "buyback_cancellation_executes_and_eps_accretion_is_visible",
    "financial_group_cet1_roe_payout_credit_cost_and_nim_are_stable",
    "brokerage_trading_value_converts_to_net_profit",
    "fintech_ma_approval_security_revenue_and_aml_kyc_controls_are_closed",
    "stablecoin_license_reserve_quality_fee_revenue_and_redemption_are_verified",
    "full_window_mfe_mae_is_available_and_supportive",
)

ROUND301_GREEN_BLOCKERS: tuple[str, ...] = (
    "policy_valueup_headline_only",
    "buyback_announcement_without_cancellation",
    "brokerage_beta_without_trading_value",
    "crypto_exchange_market_share_only",
    "fintech_ma_without_regulatory_approval",
    "stablecoin_policy_hype_only",
    "founder_legal_risk_ignored",
    "data_rights_privacy_or_security_unresolved",
)

ROUND301_SCORE_UP_AXES: tuple[str, ...] = (
    "actual_buyback_cancellation",
    "cet1_capital_return_capacity",
    "roe_and_credit_cost_visibility",
    "brokerage_trading_value_conversion",
    "nav_discount_narrowing",
    "regulatory_approval_for_fintech_ma",
    "custody_security_trust",
    "stablecoin_license_and_reserve_quality",
    "customer_data_rights_and_privacy",
    "financial_license_governance_risk_cleared",
)

ROUND301_SCORE_DOWN_AXES: tuple[str, ...] = (
    "policy_valueup_headline_only",
    "buyback_announcement_without_cancellation",
    "crypto_exchange_market_share_only",
    "stablecoin_policy_hype_only",
    "fintech_ma_without_regulatory_approval",
    "brokerage_beta_without_trading_value",
    "founder_legal_risk_ignored",
)

ROUND301_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "stablecoin_or_crypto_policy_theme_doubles_or_triples_before_revenue",
    "ma_headline_price_pop_before_security_or_regulatory_clearance",
    "securities_basket_rerates_on_market_beta_before_earnings_conversion",
    "buyback_rebound_without_business_recovery",
    "valueup_policy_expectation_without_firm_level_execution",
)

ROUND301_HARD_4C_GATES: tuple[str, ...] = (
    "crypto_exchange_abnormal_withdrawal_or_custody_failure",
    "fintech_customer_data_violation",
    "founder_or_major_shareholder_legal_risk_threatens_bank_license_or_ownership",
    "stablecoin_reserve_failure_or_regulatory_ban",
    "broker_pf_loss_or_margin_loan_unwind",
    "bank_credit_cost_spike_or_cet1_deterioration_blocks_return",
    "buyback_cancellation_not_executed_after_announcement",
)


@dataclass(frozen=True)
class Round301ShadowWeightRow:
    archetype: E2RArchetype
    actual_buyback_cancellation: int
    cet1_capital_return_capacity: int
    roe_credit_cost_visibility: int
    brokerage_trading_value_conversion: int
    nav_discount_narrowing: int
    fintech_ma_regulatory_approval: int
    custody_security_trust: int
    stablecoin_license_reserve_quality: int
    customer_data_rights_privacy: int
    financial_license_governance_risk: int
    policy_headline_only_penalty: int
    buyback_no_cancel_penalty: int
    crypto_market_share_only_penalty: int
    stablecoin_hype_only_penalty: int
    fintech_ma_no_approval_penalty: int
    brokerage_beta_only_penalty: int
    founder_legal_risk_ignored_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "actual_buyback_cancellation": _signed(self.actual_buyback_cancellation),
            "cet1_capital_return_capacity": _signed(self.cet1_capital_return_capacity),
            "roe_credit_cost_visibility": _signed(self.roe_credit_cost_visibility),
            "brokerage_trading_value_conversion": _signed(self.brokerage_trading_value_conversion),
            "nav_discount_narrowing": _signed(self.nav_discount_narrowing),
            "fintech_ma_regulatory_approval": _signed(self.fintech_ma_regulatory_approval),
            "custody_security_trust": _signed(self.custody_security_trust),
            "stablecoin_license_reserve_quality": _signed(self.stablecoin_license_reserve_quality),
            "customer_data_rights_privacy": _signed(self.customer_data_rights_privacy),
            "financial_license_governance_risk": _signed(self.financial_license_governance_risk),
            "policy_headline_only_penalty": _signed(self.policy_headline_only_penalty),
            "buyback_no_cancel_penalty": _signed(self.buyback_no_cancel_penalty),
            "crypto_market_share_only_penalty": _signed(self.crypto_market_share_only_penalty),
            "stablecoin_hype_only_penalty": _signed(self.stablecoin_hype_only_penalty),
            "fintech_ma_no_approval_penalty": _signed(self.fintech_ma_no_approval_penalty),
            "brokerage_beta_only_penalty": _signed(self.brokerage_beta_only_penalty),
            "founder_legal_risk_ignored_penalty": _signed(self.founder_legal_risk_ignored_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round301TriggerRecord:
    trigger_id: str
    case_id: str
    trigger_type: str
    trigger_date: date
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
            "trigger_date": self.trigger_date.isoformat(),
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
class Round301CaseCandidate:
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
    event_mfe_pct: float | None
    event_mae_pct: float | None
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
            "stage_candidate_not_downgraded_for_missing_full_ohlc",
            "do_not_use_round301_cases_as_candidate_generation_input",
            "do_not_treat_policy_buyback_ma_or_market_share_headline_as_green",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND301_LARGE_SECTOR,
            large_sector=ROUND301_LARGE_SECTOR,
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
            stage1_evidence=self.evidence_fields if self.stage1_date else (),
            stage2_evidence=self.evidence_fields if self.stage2_date else (),
            stage3_evidence=self.evidence_fields if self.stage3_date else (),
            stage4b_evidence=self.red_flag_fields if self.stage4b_date else (),
            stage4c_evidence=self.red_flag_fields if self.stage4c_date else (),
            must_have_fields=ROUND301_STAGE2_ACTIONABLE_RULES + ROUND301_STAGE3_YELLOW_RULES + ROUND301_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.red_flag_fields else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern=self.round_alignment_label,
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(
                stage2_price=None,
                mfe_30d=self.event_mfe_pct if self.event_mfe_pct and self.event_mfe_pct > 0 else None,
                mae_30d=self.event_mae_pct if self.event_mae_pct and self.event_mae_pct < 0 else None,
                price_validation_status="reported_event_anchor_not_full_ohlc",
            ),
            data_quality=CaseDataQuality(False, True, False, 0.7),
        )

    def as_row(self) -> dict[str, str]:
        return {
            "case_id": self.case_id,
            "symbol": self.symbol,
            "company_name": self.company_name,
            "primary_archetype": self.primary_archetype.value,
            "secondary_archetypes": ";".join(item.value for item in self.secondary_archetypes),
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
            "evidence_fields": ";".join(self.evidence_fields),
            "red_flag_fields": ";".join(self.red_flag_fields),
            "event_mfe_pct": _value_text(self.event_mfe_pct),
            "event_mae_pct": _value_text(self.event_mae_pct),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "price_validation_status": "reported_event_anchor_not_full_ohlc",
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "notes": self.notes,
        }


ROUND301_SHADOW_WEIGHT_ROWS: tuple[Round301ShadowWeightRow, ...] = (
    Round301ShadowWeightRow(E2RArchetype.BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE, 0, 0, 2, 5, 0, 0, 0, 0, 0, 0, -2, -1, -1, -1, -1, -5, -1, "securities +13.5% plus trading-value bridge", "actual brokerage earnings pending", "trading value converts to net profit", "Brokerage beta can be Stage2-Actionable, not Green."),
    Round301ShadowWeightRow(E2RArchetype.FINANCIAL_GROUP_VALUEUP_STAGE2, 3, 5, 5, 0, 1, 0, 0, 0, 0, 2, -5, -3, -1, -1, -1, -1, -2, "Value-Up plus bank metrics", "CET1/ROE/payout execution pending", "CET1+ROE+payout+credit cost stable", "Policy beta alone remains Stage2."),
    Round301ShadowWeightRow(E2RArchetype.BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE, 5, 1, 2, 0, 0, 0, 0, 0, 0, 0, -2, -5, -1, -1, -1, -1, -1, "buyback plus cancellation", "business recovery pending", "EPS accretion plus OP/FCF recovery", "Cancellation is stronger than announcement."),
    Round301ShadowWeightRow(E2RArchetype.HOLDCO_DISCOUNT_ACTIVIST_STAGE2, 5, 0, 1, 0, 5, 0, 0, 0, 0, 2, -2, -3, -1, -1, -1, -1, -1, "activist+cancel+NAV discount", "discount narrowing pending", "repeat execution plus NAV narrowing", "SK Square-style holdco discount actionability."),
    Round301ShadowWeightRow(E2RArchetype.DIGITAL_ASSET_BANK_ENTRY_STAGE2, 0, 3, 1, 0, 0, 5, 4, 1, 1, 2, -1, -1, -5, -2, -4, -1, -1, "bank+exchange stake", "approval/revenue/capital pending", "regulated income plus capital impact", "Hana/Dunamu is Stage2 until monetization clears."),
    Round301ShadowWeightRow(E2RArchetype.CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4C, 0, 0, 1, 0, 0, 5, 5, 1, 3, 2, -1, -1, -5, -2, -4, -1, -1, "deal+market share+approval path", "security remediation pending", "deal closes with trust and revenue", "Naver/Dunamu needs custody/security overlay."),
    Round301ShadowWeightRow(E2RArchetype.STABLECOIN_POLICY_4B_OVERHEAT, 0, 0, 0, 0, 0, 2, 2, 5, 2, 1, -5, -1, -2, -5, -3, -1, -1, "policy option only", "license/reserve/revenue missing", "licensed volume+reserve+fee revenue", "Stablecoin frenzy is 4B before economics."),
    Round301ShadowWeightRow(E2RArchetype.FINTECH_DATA_GOVERNANCE_4C, 0, 0, 0, 0, 0, 2, 5, 0, 5, 4, -2, -1, -2, -1, -4, -1, -3, "data rights cleared", "privacy/security gate pending", "data monetization with controls", "Customer data is not monetizable until rights are clear."),
    Round301ShadowWeightRow(E2RArchetype.KAKAO_BANK_CONTROL_REGULATORY_4C, 0, 0, 0, 0, 0, 0, 2, 0, 2, 5, -1, -1, -1, -1, -2, -1, -5, "legal/control risk watch", "ownership clearance pending", "not applicable before legal clearance", "Founder legal risk is a financial-license overlay."),
)


ROUND301_TRIGGER_RECORDS: tuple[Round301TriggerRecord, ...] = (
    Round301TriggerRecord("r6l15_brokerage_T1", "r6_loop15_brokerage_kospi_liquidity_boom", "Stage2-Actionable", date(2026, 5, 6), "KOSPI first crosses 7,000; foreign net buying 3.1T won; securities +13.5%; financial groups +4.2%", 13.5, "Stage2_Actionable_liquidity_brokerage", "Stage2-Actionable", {"kospi_close_return_pct": 6.45, "kospi_intraday_high_return_pct": 7.06, "kospi_close": 7384.56, "foreign_net_buying_krw_trn": 3.1, "financial_groups_index_return_pct": 4.2}),
    Round301TriggerRecord("r6l15_valueup_T1", "r6_loop15_financial_group_valueup_basket", "Stage2_policy", date(2024, 2, 28), "Corporate Value-Up and shareholder-return penalties under discussion", "price_data_unavailable_after_deep_search", "Stage2_policy_not_Green", "Stage2", {"possible_delisting_for_non_compliance": True, "bank_specific_price_anchor": "price_data_unavailable_after_deep_search"}),
    Round301TriggerRecord("r6l15_samsung_T1", "r6_loop15_samsung_buyback_capital_allocation", "Stage2-Actionable", date(2024, 11, 15), "10T won buyback, 3T won immediate repurchase and cancellation; shares +7.2%", 7.2, "Stage2_Actionable_buyback_not_business_Green", "Stage2-Actionable", {"buyback_total_krw_trn": 10, "immediate_buyback_cancel_krw_trn": 3, "ytd_pre_event_return_pct": -32}),
    Round301TriggerRecord("r6l15_sksquare_T1", "r6_loop15_sk_square_activist_buyback", "Stage2-Actionable", date(2024, 11, 21), "100B won cancellation, new 100B won buyback, Palliser activism and SK Hynix stake discount", "price_data_unavailable_after_deep_search", "Stage2_Actionable_holdco_discount", "Stage2-Actionable", {"existing_buyback_cancel_krw_bn": 100, "new_buyback_krw_bn": 100, "activist_stake_pct": 1, "sk_hynix_stake_pct": 20}),
    Round301TriggerRecord("r6l15_hana_T1", "r6_loop15_hana_dunamu_digital_asset_entry", "Stage2_digital_asset_entry", date(2026, 5, 15), "Hana Bank acquires 6.55% Dunamu stake for 1T won; Upbit handles over 80% Korea virtual-asset volume", "price_data_unavailable_after_deep_search", "Stage2_digital_asset_bank_entry", "Stage2", {"stake_acquired_pct": 6.55, "transaction_value_krw_trn": 1.0, "upbit_korea_virtual_asset_volume_share_pct": 80}),
    Round301TriggerRecord("r6l15_naver_T1", "r6_loop15_naver_financial_dunamu_ma_security", "Stage2_MA_with_security_4C_watch", date(2025, 11, 27), "15.13T won all-stock deal; Naver initially +7%, then -4.2% after 54B won abnormal Upbit withdrawal", "7.0 then -4.2", "Stage2_Actionable_MA_with_security_4C_overlay", "Stage2-Actionable+4C-watch", {"deal_value_krw_trn": 15.13, "deal_value_usd_bn": 10.27, "abnormal_withdrawal_krw_bn": 54, "upbit_market_share_pct_context": 70}),
    Round301TriggerRecord("r6l15_stablecoin_T2", "r6_loop15_stablecoin_policy_fintech_frenzy", "4B_policy_overheat", date(2025, 6, 1), "Stablecoin policy frenzy; Kakao Pay 2x+, LG CNS +70%, Aton +80%, ME2ON 3x, margin loans 20.5T won", 100, "4B_policy_overheat_not_stage3", "4B-watch", {"kakao_pay_monthly_return_pct": 100, "lg_cns_return_pct": 70, "aton_return_pct": 80, "me2on_return_pct": 200, "margin_loans_krw_trn": 20.5}),
    Round301TriggerRecord("r6l15_kakao_T2", "r6_loop15_kakao_founder_kakaobank_control_risk", "4C_governance_regulatory_watch", date(2024, 7, 23), "Kakao founder arrested/indicted context; possible KakaoBank ownership risk; Kakao -4.6% after arrest source", -4.6, "4C_watch_not_hard_until_conviction_or_ownership_action", "4C-watch", {"founder_stake_control_context_pct": 24, "financial_crime_bank_stake_threshold_pct": 10, "q2_op_yoy_pct": 18.5, "hard_4c_confirmed": False}),
)


ROUND301_CASE_CANDIDATES: tuple[Round301CaseCandidate, ...] = (
    Round301CaseCandidate("r6_loop15_brokerage_kospi_liquidity_boom", "016360/039490/005940/006800/brokerage_basket", "Samsung Securities / Kiwoom / NH Investment / Mirae / brokerage basket", E2RArchetype.BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE, (E2RArchetype.SECURITIES_BROKERAGE_MARKET_BETA, E2RArchetype.SECURITIES_TRADING_VOLUME_EVENT_PREMIUM), "success_candidate", "Stage2_promote_candidate", "T1/T2", "Stage2-Actionable_to_Stage3-Yellow_candidate", "Stage2-Actionable", date(2025, 1, 1), date(2026, 5, 6), None, date(2026, 5, 6), None, False, ("kospi_7000_cross", "foreign_net_buying_3_1T_won", "securities_firms_plus_13_5pct", "financial_groups_plus_4_2pct"), ("daily_trading_value_missing", "brokerage_commission_revenue_missing", "margin_finance_balance_missing", "IB_fee_income_missing", "PF_risk_absorption_missing"), 13.5, None, {"kospi_close_return_pct": 6.45, "kospi_intraday_high_return_pct": 7.06, "kospi_close": 7384.56, "foreign_net_buying_krw_trn": 3.1, "foreign_net_buying_usd_bn": 2.13, "securities_firms_index_return_pct": 13.5, "financial_groups_index_return_pct": 4.2, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "missed_due_to_score", "Stage2_Actionable_liquidity_brokerage", "cyclical_rerating", "stage2_watch_success", "Market liquidity and securities index +13.5% are Stage2-Actionable, but Green needs earnings conversion."),
    Round301CaseCandidate("r6_loop15_financial_group_valueup_basket", "105560/055550/086790/316140", "KB Financial / Shinhan / Hana / Woori", E2RArchetype.FINANCIAL_GROUP_VALUEUP_STAGE2, (E2RArchetype.VALUE_UP_FINANCIAL_HOLDING_STAGE2, E2RArchetype.FINANCIAL_SPREAD_BALANCE_SHEET), "success_candidate", "success_candidate_stage2", "T1/T2", "Stage2_policy_success_candidate", "Stage2", date(2024, 2, 1), date(2024, 2, 28), None, date(2026, 5, 6), None, False, ("corporate_valueup_policy", "shareholder_return_penalty_discussion", "governance_reform", "dividend_tax_incentive_discussion"), ("CET1_ratio_missing", "payout_ratio_missing", "buyback_cancellation_missing", "ROE_missing", "NIM_missing", "credit_cost_missing"), None, None, {"possible_delisting_for_non_compliance": True, "bank_specific_price_anchor": "price_data_unavailable_after_deep_search", "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "aligned", "Stage2_policy_not_Green", "policy_event_rerating", "stage2_watch_success", "Value-Up is Stage2 policy beta; bank-level Yellow requires CET1, ROE, payout and credit-cost proof."),
    Round301CaseCandidate("r6_loop15_samsung_buyback_capital_allocation", "005930", "Samsung Electronics", E2RArchetype.BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE, (E2RArchetype.TREASURY_SHARE_CANCEL_EXECUTION, E2RArchetype.BUYBACK_CANCEL_BUT_BUSINESS_RISK), "success_candidate", "Stage2_promote_candidate", "T1/T2", "Stage2-Actionable", "Stage2-Actionable", date(2024, 11, 1), date(2024, 11, 15), None, date(2024, 11, 15), None, False, ("buyback_total_10T_KRW", "immediate_3T_KRW_cancellation", "first_buyback_since_2017", "event_return_plus_7_2pct"), ("HBM_competitiveness_recovery_missing", "Nvidia_qualification_missing", "foundry_loss_reduction_missing", "sustained_OP_recovery_missing", "remaining_7T_execution_missing"), 7.2, None, {"buyback_total_krw_trn": 10, "buyback_total_usd_bn": 7.17, "immediate_buyback_cancel_krw_trn": 3, "first_buyback_since": 2017, "event_return_pct": 7.2, "ytd_pre_event_return_pct": -32, "full_ohlc_status": "price_data_unavailable_after_deep_search"}, "missed_due_to_score", "Stage2_Actionable_buyback_not_business_Green", "policy_event_rerating", "stage2_watch_success", "Buyback plus cancellation is actionable capital allocation, but Green requires business recovery and execution."),
    Round301CaseCandidate("r6_loop15_sk_square_activist_buyback", "402340", "SK Square", E2RArchetype.HOLDCO_DISCOUNT_ACTIVIST_STAGE2, (E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_STAGE2, E2RArchetype.HOLDING_NAV_DISCOUNT_VALUEUP), "success_candidate", "Stage2_promote_candidate", "T1/T2", "Stage2-Actionable", "Stage2-Actionable", date(2024, 1, 1), date(2024, 11, 21), None, date(2024, 11, 21), None, False, ("existing_100B_KRW_cancellation", "new_100B_KRW_buyback", "Palliser_activism", "SK_Hynix_stake_discount"), ("NAV_discount_narrowing_missing", "repeat_buyback_missing", "asset_monetization_missing", "governance_execution_missing", "SK_Hynix_stake_risk_control_missing"), None, None, {"existing_buyback_cancel_krw_bn": 100, "new_buyback_krw_bn": 100, "sk_hynix_stake_pct": 20, "sk_hynix_stake_value_usd_bn": 18, "activist": "Palliser Capital", "activist_stake_pct": 1, "direct_event_return": "price_data_unavailable_after_deep_search"}, "missed_due_to_score", "Stage2_Actionable_holdco_discount", "policy_event_rerating", "stage2_watch_success", "Activist plus cancellation plus NAV discount is Stage2-Actionable; Green needs discount narrowing and repeated execution."),
    Round301CaseCandidate("r6_loop15_hana_dunamu_digital_asset_entry", "086790/private_Dunamu", "Hana Financial / Hana Bank / Dunamu", E2RArchetype.DIGITAL_ASSET_BANK_ENTRY_STAGE2, (E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2, E2RArchetype.DIGITAL_ASSET_BANK_STAKE_STAGE2), "success_candidate", "success_candidate_stage2", "T1/T2", "Stage2_digital_asset_entry", "Stage2", date(2025, 1, 1), date(2026, 5, 15), None, date(2026, 5, 15), None, False, ("stake_acquired_6_55pct", "transaction_value_1T_KRW", "Upbit_volume_share_over_80pct", "blockchain_remittance_technical_verification"), ("regulatory_approval_missing", "crypto_trading_volume_durability_missing", "remittance_revenue_model_missing", "capital_ratio_impact_missing", "Dunamu_valuation_mark_missing"), None, None, {"stake_acquired_pct": 6.55, "transaction_value_krw_trn": 1.0, "transaction_value_usd_mn": 700, "upbit_korea_virtual_asset_volume_share_pct": 80, "kakao_investment_remaining_stake_pct": 4.03, "blockchain_remittance_technical_verification": True, "direct_hana_price_anchor": "price_data_unavailable_after_deep_search"}, "aligned", "Stage2_digital_asset_bank_entry", "unknown", "stage2_watch_success", "Bank digital-asset entry is Stage2; Green requires approval, monetization and capital-ratio clarity."),
    Round301CaseCandidate("r6_loop15_naver_financial_dunamu_ma_security", "035420/private_Dunamu", "Naver Financial / Dunamu / Upbit", E2RArchetype.CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4C, (E2RArchetype.DIGITAL_ASSET_MA_TRUST_4C_WATCH, E2RArchetype.FINTECH_DATA_GOVERNANCE_4C), "success_candidate", "Stage2_with_4C_overlay", "T1/T2", "Stage2_MA_with_security_4C_watch", "Stage2-Actionable_with_security_4C", date(2025, 1, 1), date(2025, 11, 27), None, date(2025, 11, 27), date(2025, 11, 27), False, ("deal_value_15_13T_KRW", "Naver_initial_plus_7pct", "Upbit_market_share_70pct", "share_exchange_ratio_2_54"), ("abnormal_withdrawal_54B_KRW", "regulatory_approval_missing", "shareholder_approval_missing", "security_remediation_missing", "crypto_revenue_durability_missing"), 7.0, -4.2, {"deal_value_krw_trn": 15.13, "deal_value_usd_bn": 10.27, "share_exchange_ratio": "2.54_Naver_Financial_shares_per_Dunamu_share", "naver_initial_event_mfe_pct": 7.0, "naver_later_event_return_pct": -4.2, "upbit_market_share_pct_context": 70, "abnormal_withdrawal_krw_bn": 54, "upbit_cover_loss_with_own_assets": True}, "evidence_good_but_price_failed", "Stage2_Actionable_MA_with_security_4C_overlay", "event_premium", "stage2_watch_success", "Crypto exchange M&A must include custody/security overlay; market share alone is not Green."),
    Round301CaseCandidate("r6_loop15_stablecoin_policy_fintech_frenzy", "377300/064400/158430/201490", "Kakao Pay / LG CNS / Aton / ME2ON", E2RArchetype.STABLECOIN_POLICY_4B_OVERHEAT, (E2RArchetype.KRW_STABLECOIN_POLICY_OVERHEAT, E2RArchetype.KRW_STABLECOIN_POLICY_THEME), "overheat", "event_premium_4B_watch", "T2", "4B_policy_overheat", "4B-watch", date(2025, 6, 1), None, None, date(2025, 6, 1), None, False, ("stablecoin_policy_pledge", "Kakao_Pay_more_than_doubled", "LG_CNS_plus_70pct", "Aton_plus_80pct", "ME2ON_tripled"), ("stablecoin_license_missing", "issuance_volume_missing", "fee_revenue_missing", "reserve_management_missing", "AML_KYC_controls_missing", "margin_loans_20_5T_KRW"), 200, None, {"kakao_pay_monthly_return_pct": 100, "lg_cns_return_pct": 70, "aton_return_pct": 80, "me2on_return_pct": 200, "margin_loans_krw_trn": 20.5, "stablecoin_bill_min_equity_krw_mn": 500, "bok_concern_nonbank_issuers": True, "regulatory_framework_unclear": True}, "false_positive_score", "4B_policy_overheat_not_stage3", "theme_overheat", "false_green", "Stablecoin policy rally is 4B overheat until license, reserve quality and revenue are confirmed."),
    Round301CaseCandidate("r6_loop15_kakao_founder_kakaobank_control_risk", "035720/323410/377300", "Kakao / KakaoBank / Kakao Pay", E2RArchetype.KAKAO_BANK_CONTROL_REGULATORY_4C, (E2RArchetype.INTERNET_BANK_GOVERNANCE_4C, E2RArchetype.FINTECH_DATA_GOVERNANCE_4C), "4b_watch", "4C_governance_regulatory_watch", "T1/T2/T3", "4C_governance_regulatory_watch", "4C-watch", date(2023, 1, 1), None, None, date(2024, 7, 23), date(2024, 7, 23), False, ("founder_arrest_indictment_context", "KakaoBank_control_risk_if_convicted", "financial_crime_bank_stake_threshold_10pct", "Kakao_event_mae_minus_4_6pct"), ("legal_resolution_missing", "bank_ownership_clearance_missing", "financial_license_stability_missing", "governance_reform_missing", "affiliate_fundraising_recovery_missing"), None, -4.6, {"founder_stake_control_context_pct": 24, "kakaobank_control_risk_if_convicted": True, "financial_crime_bank_stake_threshold_pct": 10, "kakao_event_mae_pct": -4.6, "q2_op_krw_bn": 134, "q2_op_yoy_pct": 18.5, "founder_indicted": True, "hard_4c_confirmed": False}, "false_positive_score", "4C_watch_not_hard_until_conviction_or_ownership_action", "thesis_break", "should_have_been_red", "Founder/legal risk is a financial-license and bank-control 4C overlay for fintech and online-bank names."),
)


def round301_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(case.to_case_record() for case in ROUND301_CASE_CANDIDATES)


def round301_summary() -> dict[str, object]:
    return {
        "source_round": ROUND301_SOURCE_ROUND_PATH,
        "round_id": ROUND301_ANALYST_ROUND_ID,
        "large_sector": ROUND301_LARGE_SECTOR,
        "method": ROUND301_METHOD,
        "case_candidate_count": len(ROUND301_CASE_CANDIDATES),
        "trigger_count": len(ROUND301_TRIGGER_RECORDS),
        "stage2_actionable_candidate_count": 4,
        "stage3_yellow_candidate_count": 3,
        "stage3_green_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 5,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 0,
        "missed_structural_count": 2,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "full_adjusted_ohlc_complete": False,
        "shadow_weight_only": True,
    }


def round301_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(case.as_row() for case in ROUND301_CASE_CANDIDATES)


def round301_trigger_rows() -> tuple[dict[str, str], ...]:
    return tuple(trigger.as_row() for trigger in ROUND301_TRIGGER_RECORDS)


def round301_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"requested_alias": key, "canonical_archetype": value} for key, value in ROUND301_REQUIRED_TARGET_ALIASES.items())


def round301_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND301_SHADOW_WEIGHT_ROWS)


def round301_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    rows = []
    for axis in ROUND301_SCORE_UP_AXES:
        rows.append({"axis": axis, "points": "+5", "direction": "raise", "reason": "R6 financial trigger quality axis"})
    for axis in ROUND301_SCORE_DOWN_AXES:
        rows.append({"axis": axis, "points": "-5", "direction": "lower", "reason": "R6 headline, policy, market-share or legal-risk blocker"})
    return tuple(rows)


def round301_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND301_SOURCE_ROUND_PATH,
        "round_id": ROUND301_ANALYST_ROUND_ID,
        "large_sector": ROUND301_LARGE_SECTOR,
        "method": ROUND301_METHOD,
        "summary": round301_summary(),
        "target_archetypes": dict(ROUND301_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND301_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND301_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND301_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND301_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND301_SCORE_UP_AXES),
        "score_down_axes": list(ROUND301_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND301_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND301_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_apply_round301_shadow_weights_to_production_scoring_yet",
            "do_not_use_round301_cases_as_candidate_generation_input",
            "do_not_treat_policy_buyback_ma_market_share_or_stablecoin_headline_as_green",
            "do_not_ignore_cet1_roe_credit_cost_security_regulatory_data_rights_or_execution_gates",
        ],
    }


def render_round301_summary_markdown() -> str:
    summary = round301_summary()
    lines = [
        "# Round 301 R6 Loop 15 Financial/Capital/Digital Trigger Validation",
        "",
        "이번 라운드는 금융 headline이 아니라 CET1, ROE, 실제 소각, 거래대금의 이익 전환, 규제 승인, 보안과 데이터 권리를 분리한다.",
        "",
        "쉬운 예: 자사주 매입 발표는 Stage2 신호일 수 있지만, 실제 소각과 영업 회복이 없으면 Stage3-Green 근거가 아니다.",
        "",
        "## Summary",
        "",
    ]
    for key in (
        "round_id",
        "large_sector",
        "case_candidate_count",
        "trigger_count",
        "stage2_actionable_candidate_count",
        "stage3_yellow_candidate_count",
        "stage3_green_confirmed_count",
        "stage4b_watch_count",
        "stage4c_watch_count",
        "hard_4c_case_count",
        "missed_structural_count",
        "production_scoring_changed",
        "candidate_generation_input",
        "full_adjusted_ohlc_complete",
        "shadow_weight_only",
    ):
        lines.append(f"- {key}: {summary[key]}")
    lines.extend(
        [
            "",
            "## Core Findings",
            "",
            "- Brokerage basket은 securities +13.5%로 Stage2-Actionable이지만 거래대금과 순이익 전환 전에는 Green이 아니다.",
            "- Financial Value-Up은 Stage2 policy beta이며 CET1, ROE, payout, credit cost가 bank-level gate다.",
            "- Samsung buyback은 10T won buyback과 3T won cancellation으로 Stage2-Actionable이지만 business recovery gate가 남는다.",
            "- SK Square는 activist, cancellation, NAV discount가 있어 Stage2-Actionable이나 discount narrowing이 필요하다.",
            "- Hana/Dunamu는 bank digital-asset entry Stage2이며 approval, monetization, capital-ratio impact가 Green gate다.",
            "- Naver/Dunamu는 M&A Stage2와 security 4C-watch가 동시에 붙는다.",
            "- Stablecoin policy frenzy는 license, reserve, fee revenue 전까지 4B overheat다.",
            "- Kakao founder/KakaoBank risk는 financial-license/control 4C-watch다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round301_trigger_grid_markdown() -> str:
    lines = [
        "# Round 301 Trigger Grid",
        "",
        "| trigger_id | case_id | date | type | outcome | promote_to | evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for trigger in ROUND301_TRIGGER_RECORDS:
        lines.append(
            f"| {trigger.trigger_id} | {trigger.case_id} | {trigger.trigger_date.isoformat()} | {trigger.trigger_type} | {trigger.trigger_outcome_label} | {trigger.promote_to} | {trigger.evidence_available} |"
        )
    return "\n".join(lines) + "\n"


def render_round301_stage_rules_markdown() -> str:
    lines = ["# Round 301 Stage Rules", "", "Do not apply these weights to production scoring yet.", "", "## Stage2-Actionable", ""]
    lines.extend(f"- {rule}" for rule in ROUND301_STAGE2_ACTIONABLE_RULES)
    lines.extend(["", "## Stage3-Yellow", ""])
    lines.extend(f"- {rule}" for rule in ROUND301_STAGE3_YELLOW_RULES)
    lines.extend(["", "## Stage3-Green", ""])
    lines.extend(f"- {rule}" for rule in ROUND301_STAGE3_GREEN_RULES)
    lines.extend(["", "## Green Blockers", ""])
    lines.extend(f"- {rule}" for rule in ROUND301_GREEN_BLOCKERS)
    return "\n".join(lines) + "\n"


def render_round301_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 301 4B/4C Review",
        "",
        "이번 라운드에서 확정 Green과 hard 4C는 없다. 대신 policy, buyback, M&A, stablecoin headline의 4B/4C-watch를 분리한다.",
        "",
        "## 4B Watch",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND301_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## 4C Gates", ""])
    lines.extend(f"- {item}" for item in ROUND301_HARD_4C_GATES)
    return "\n".join(lines) + "\n"


def render_round301_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round 301 Price Validation Plan",
            "",
            "- reported_event_anchor_not_full_ohlc 상태를 유지한다.",
            "- full adjusted OHLC가 없다는 이유로 Stage2/Yellow 후보를 강등하지 않는다.",
            "- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.",
            "- 다음 단계에서는 trigger date 기준 30/90/180일 MFE/MAE, below-entry, CET1/ROE, 거래대금, security remediation, regulatory approval gate를 채운다.",
            "",
        ]
    )


def write_round301_r6_loop15_reports(
    *,
    output_directory: str | Path = ROUND301_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND301_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND301_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND301_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND301_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round301_case_records(), cases_path),
        "triggers": write_round301_triggers(triggers_path),
        "audit": _write_json(round301_audit_payload(), audit_path),
        "weight_profile": _write_csv(round301_shadow_weight_rows(), weight_profile_path),
        "summary": output / "round301_r6_loop15_trigger_validation_summary.md",
        "case_matrix": output / "round301_r6_loop15_case_matrix.csv",
        "trigger_grid": output / "round301_r6_loop15_trigger_grid.csv",
        "target_aliases": output / "round301_r6_loop15_target_aliases.csv",
        "score_adjustments": output / "round301_r6_loop15_score_adjustments.csv",
        "shadow_weights": output / "round301_r6_loop15_shadow_weights.csv",
        "stage_rules": output / "round301_r6_loop15_stage_rules.md",
        "trigger_grid_md": output / "round301_r6_loop15_trigger_grid.md",
        "price_validation_plan": output / "round301_r6_loop15_price_validation_plan.md",
        "stage4b_4c_review": output / "round301_r6_loop15_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round301_summary_markdown(), encoding="utf-8")
    _write_csv(round301_case_rows(), paths["case_matrix"])
    _write_csv(round301_trigger_rows(), paths["trigger_grid"])
    _write_csv(round301_target_alias_rows(), paths["target_aliases"])
    _write_csv(round301_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round301_shadow_weight_rows(), paths["shadow_weights"])
    paths["stage_rules"].write_text(render_round301_stage_rules_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round301_trigger_grid_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round301_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round301_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def write_round301_triggers(path: str | Path = ROUND301_DEFAULT_TRIGGERS_PATH) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(trigger.as_dict(), ensure_ascii=False, sort_keys=True) for trigger in ROUND301_TRIGGER_RECORDS]
    target.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")
    return target


def _write_json(payload: Mapping[str, object], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def _write_csv(rows: Iterable[Mapping[str, object]], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    rows_tuple = tuple(rows)
    with target.open("w", encoding="utf-8", newline="") as handle:
        if not rows_tuple:
            handle.write("")
            return target
        writer = csv.DictWriter(handle, fieldnames=list(rows_tuple[0].keys()))
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow({key: _value_text(value) for key, value in row.items()})
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def _signed(value: int) -> str:
    return f"{value:+d}"


__all__ = [
    "ROUND301_CASE_CANDIDATES",
    "ROUND301_GREEN_BLOCKERS",
    "ROUND301_HARD_4C_GATES",
    "ROUND301_LARGE_SECTOR",
    "ROUND301_REQUIRED_TARGET_ALIASES",
    "ROUND301_SCORE_DOWN_AXES",
    "ROUND301_SCORE_UP_AXES",
    "ROUND301_SHADOW_WEIGHT_ROWS",
    "ROUND301_STAGE2_ACTIONABLE_RULES",
    "ROUND301_STAGE3_GREEN_RULES",
    "ROUND301_STAGE3_YELLOW_RULES",
    "ROUND301_STAGE4B_WATCH_TRIGGERS",
    "ROUND301_TRIGGER_RECORDS",
    "render_round301_stage_rules_markdown",
    "render_round301_stage4b_4c_review_markdown",
    "render_round301_trigger_grid_markdown",
    "round301_audit_payload",
    "round301_case_records",
    "round301_case_rows",
    "round301_shadow_weight_rows",
    "round301_summary",
    "round301_trigger_rows",
    "write_round301_r6_loop15_reports",
]
