"""Round-314 R6 Loop-16 financial capital allocation and digital-finance validation.

This module converts ``docs/round/round_314.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: a 10T won buyback with cancellation can be Stage2 evidence. It
is still not Stage3-Green until the buyback is executed and ROE/EPS or FCF
actually improve as of the replay date.
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


ROUND314_SOURCE_ROUND_PATH = "docs/round/round_314.md"
ROUND314_ANALYST_ROUND_ID = "round_242"
ROUND314_LARGE_SECTOR = "FINANCIALS_CAPITAL_ALLOCATION_DIGITAL_FINANCE"
ROUND314_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND314_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round314_r6_loop16_financial_capital_digital_trigger_validation"
ROUND314_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r6_loop16_round242.jsonl"
ROUND314_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r6_loop16_round242.jsonl"
ROUND314_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round314_r6_loop16_financial_capital_digital_trigger_validation_audit.json"
ROUND314_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round242_r6_loop16_v1.csv"

ROUND314_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE": E2RArchetype.BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE.value,
    "HOLDCO_DISCOUNT_BUYBACK_STAGE2": E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_STAGE2.value,
    "BROKERAGE_TRADING_VOLUME_STAGE2_BETA": E2RArchetype.BROKERAGE_TRADING_VOLUME_STAGE2_BETA.value,
    "BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE": E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE.value,
    "FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4B": E2RArchetype.FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4B.value,
    "STABLECOIN_POLICY_EVENT_PREMIUM_4B": E2RArchetype.STABLECOIN_POLICY_EVENT_PREMIUM_4B.value,
    "ELS_MISSELLING_CONSUMER_PROTECTION_4C": E2RArchetype.ELS_MISSELLING_CONSUMER_PROTECTION_4C.value,
    "FX_OVERSEAS_STOCK_FLOW_4C_WATCH": E2RArchetype.FX_OVERSEAS_STOCK_FLOW_4C_WATCH.value,
    "PRIVATE_FINTECH_STABLECOIN_IPO_OPTIONALITY_STAGE2": E2RArchetype.PRIVATE_FINTECH_STABLECOIN_IPO_OPTIONALITY_STAGE2.value,
}

ROUND314_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "large_buyback_and_actual_cancellation_disclosed",
    "event_return_at_least_5pct_or_market_relative_return_at_least_5pp",
    "capital_allocation_can_link_to_EPS_ROE_or_discount_narrowing",
    "digital_asset_deal_has_value_stake_approval_path_or_revenue_model",
    "brokerage_beta_links_to_turnover_foreign_inflow_or_fee_income",
    "no_consumer_protection_custody_security_or_FX_hard_gate_for_positive_candidate",
)

ROUND314_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_ROE_fee_income_or_revenue_model_can_change_materially",
    "one_of_approval_security_capital_ratio_consumer_protection_or_FX_gate_remains_open",
    "reported_price_anchor_supports_trigger_but_full_adjusted_OHLC_is_missing",
    "case_is_not_pure_policy_stablecoin_market_beta_or_private_optionality",
)

ROUND314_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "buyback_is_executed_and_cancelled",
    "ROE_EPS_improves_after_capital_return",
    "digital_asset_MA_receives_regulatory_approval",
    "custody_security_AML_controls_are_proven",
    "stablecoin_issuer_license_reserve_rule_and_revenue_model_are_confirmed",
    "ELS_consumer_protection_liabilities_are_provisioned_and_cleared",
    "FX_overseas_stock_risk_is_managed",
    "full_adjusted_OHLC_MFE_MAE_window_supports_stage_candidate",
)

ROUND314_GREEN_BLOCKERS: tuple[str, ...] = (
    "buyback_without_business_recovery",
    "shareholder_return_without_cancellation",
    "stablecoin_policy_without_license",
    "crypto_MA_without_security_controls",
    "bank_digital_asset_without_capital_clarity",
    "market_beta_without_earnings",
    "overseas_stock_flow_without_FX_risk",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND314_SCORE_UP_AXES: tuple[str, ...] = (
    "actual_buyback_cancellation",
    "ROE_EPS_recovery_after_buyback",
    "holdco_discount_narrowing",
    "brokerage_turnover_fee_conversion",
    "digital_asset_regulatory_approval",
    "custody_security_AML",
    "bank_capital_ratio_after_digital_asset",
    "consumer_protection_compliance",
    "FX_risk_disclosure",
)

ROUND314_SCORE_DOWN_AXES: tuple[str, ...] = (
    "buyback_without_business_recovery",
    "shareholder_return_without_cancellation",
    "stablecoin_policy_without_license",
    "crypto_MA_without_security_controls",
    "bank_digital_asset_without_capital_clarity",
    "market_beta_without_earnings",
    "overseas_stock_flow_without_FX_risk",
)

ROUND314_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "buyback_rally_without_business_recovery",
    "stablecoin_theme_rallies_before_issuer_license_or_reserve_rules",
    "crypto_exchange_MA_rallies_before_security_or_custody_controls",
    "brokerage_stocks_rally_on_market_beta_before_fee_earnings",
    "bank_buys_crypto_stake_before_capital_or_risk_weight_treatment",
    "retail_overseas_stock_flow_grows_while_won_or_FX_risk_worsens",
)

ROUND314_4C_WATCH_GATES: tuple[str, ...] = (
    "mis_selling_consumer_protection_fine",
    "crypto_exchange_abnormal_withdrawal_or_custody_failure",
    "financial_platform_data_breach",
    "stablecoin_issuer_failure_or_reserve_mismatch",
    "FX_risk_mis_disclosure_to_retail_investors",
    "capital_ratio_breach_after_acquisition_or_digital_asset_exposure",
)

ROUND314_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_buyback_deal_policy_flow_or_penalty_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_buyback_stablecoin_crypto_MA_market_beta_or_private_fintech_headline_as_Green_without_ROE_EPS_security_approval_revenue_or_FCF",
)


@dataclass(frozen=True)
class Round314ShadowWeightRow:
    archetype: E2RArchetype
    buyback_cancellation: int
    roe_eps_recovery: int
    holdco_discount_narrowing: int
    brokerage_fee_conversion: int
    digital_asset_approval: int
    custody_security_aml: int
    bank_capital_ratio: int
    consumer_protection: int
    fx_risk_disclosure: int
    policy_without_license_penalty: int
    market_beta_without_earnings_penalty: int
    security_or_custody_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "buyback_cancellation": _signed(self.buyback_cancellation),
            "ROE_EPS_recovery": _signed(self.roe_eps_recovery),
            "holdco_discount_narrowing": _signed(self.holdco_discount_narrowing),
            "brokerage_fee_conversion": _signed(self.brokerage_fee_conversion),
            "digital_asset_approval": _signed(self.digital_asset_approval),
            "custody_security_AML": _signed(self.custody_security_aml),
            "bank_capital_ratio": _signed(self.bank_capital_ratio),
            "consumer_protection": _signed(self.consumer_protection),
            "FX_risk_disclosure": _signed(self.fx_risk_disclosure),
            "policy_without_license_penalty": _signed(self.policy_without_license_penalty),
            "market_beta_without_earnings_penalty": _signed(self.market_beta_without_earnings_penalty),
            "security_or_custody_penalty": _signed(self.security_or_custody_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round314TriggerRecord:
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
class Round314CaseCandidate:
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
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
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
            "do_not_use_round314_cases_as_candidate_generation_input",
            "do_not_treat_buyback_stablecoin_crypto_MA_market_beta_or_private_fintech_headline_as_Green_without_ROE_EPS_security_approval_revenue_or_FCF",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND314_LARGE_SECTOR,
            large_sector=ROUND314_LARGE_SECTOR,
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
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4B" in field or "4b" in field or "overheat" in field or "rally" in field),
            stage4c_evidence=tuple(
                field
                for field in (*self.red_flag_fields, *self.evidence_fields)
                if "4C" in field
                or "4c" in field
                or "mis_selling" in field
                or "consumer_protection" in field
                or "abnormal_withdrawal" in field
                or "FX" in field
                or "capital_ratio_breach" in field
            ),
            must_have_fields=ROUND314_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.case_type in {"event_premium", "4b_watch", "4c_thesis_break", "failed_rerating", "overheat"} else None,
            score_price_alignment=self.score_price_alignment,
            rerating_result=self.rerating_result,
            stage_failure_type=self.stage_failure_type,
            price_pattern="reported_event_anchor_only",
            score_weight_hint={},
            green_guardrails=tuple(guardrails),
            notes=self.notes,
            price_validation=PriceValidation(
                stage1_price=self.stage1_price_anchor,
                stage2_price=self.stage2_price_anchor,
                stage3_price=self.stage2_price_anchor if self.stage3_date else None,
                stage4b_price=self.stage4b_price_anchor,
                stage4c_price=self.stage4c_price_anchor,
                mfe_30d=self.event_mfe_pct,
                mae_30d=self.event_mae_pct,
                price_validation_status="price_data_unavailable_after_deep_search",
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8 if not self.hard_4c_confirmed else 0.88,
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
            "event_mfe_pct": _value_text(self.event_mfe_pct),
            "event_mae_pct": _value_text(self.event_mae_pct),
            "stage1_price_anchor": _value_text(self.stage1_price_anchor),
            "stage2_price_anchor": _value_text(self.stage2_price_anchor),
            "stage4b_price_anchor": _value_text(self.stage4b_price_anchor),
            "stage4c_price_anchor": _value_text(self.stage4c_price_anchor),
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND314_CASE_CANDIDATES: tuple[Round314CaseCandidate, ...] = (
    Round314CaseCandidate(
        "r6_loop16_samsung_buyback_capital_allocation",
        "005930",
        "Samsung Electronics",
        E2RArchetype.BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE,
        (E2RArchetype.BUYBACK_CAPITAL_ALLOCATION_STAGE2_ACTIONABLE, E2RArchetype.TREASURY_SHARE_CANCEL_EXECUTION, E2RArchetype.BUYBACK_CANCEL_BUT_BUSINESS_RISK),
        "success_candidate",
        "Stage2_Actionable_buyback_with_4B_business_gate",
        "r6l16_samsung_buyback_T1",
        "Stage2-Actionable_buyback_cancellation",
        "Stage2-Actionable + 4B-watch",
        date(2024, 11, 1),
        date(2024, 11, 15),
        None,
        date(2024, 11, 15),
        None,
        False,
        ("buyback_krw_10tn", "first_buyback_since_2017", "initial_cancelled_repurchase_krw_3tn", "shares_plus_7_2pct", "ytd_decline_minus_32pct"),
        ("ROE_EPS_recovery_missing", "business_recovery_gate_open", "full_adjusted_OHLC_MFE_MAE_missing", "buyback_rally_without_business_recovery_4B"),
        7.2,
        None,
        None,
        None,
        None,
        None,
        {"buyback_krw_tn": 10, "buyback_usd_bn": 7.17, "initial_cancelled_repurchase_krw_tn": 3, "event_return_pct": 7.2, "ytd_decline_pct": -32},
        "aligned",
        "excellent_stage2_buyback_candidate_not_Green",
        "policy_event_rerating",
        "stage2_watch_success",
        "Large buyback and cancellation are Stage2 evidence, but ROE/EPS recovery and execution remain Green gates.",
    ),
    Round314CaseCandidate(
        "r6_loop16_sk_square_buyback_holdco_discount",
        "402340",
        "SK Square",
        E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_STAGE2,
        (E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_CANCELLATION, E2RArchetype.HOLDING_NAV_DISCOUNT_VALUEUP),
        "success_candidate",
        "Stage2_holdco_discount_buyback",
        "r6l16_sk_square_buyback_T1",
        "Stage2_holdco_discount_buyback",
        "Stage2",
        date(2024, 11, 21),
        date(2024, 11, 21),
        None,
        date(2024, 11, 21),
        None,
        False,
        ("previous_buyback_cancelled_krw_100bn", "new_repurchase_cancel_krw_100bn", "sk_hynix_stake_20pct", "market_value_less_than_half_of_stake_value", "activist_engagement"),
        ("non_hynix_asset_clarity_missing", "discount_compression_missing", "repeat_execution_missing", "single_asset_NAV_rally_4B"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"previous_cancelled_buyback_krw_bn": 100, "new_repurchase_cancel_krw_bn": 100, "sk_hynix_stake_pct": 20, "market_value_vs_stake_value": "<50pct", "activist_stake_context_pct": 1},
        "evidence_good_but_price_failed",
        "Stage2_holdco_discount_but_discount_close_pending",
        "unknown",
        "stage2_watch_success",
        "Holdco discount and repeated cancellation are Stage2 evidence, but discount compression and non-Hynix asset clarity remain gates.",
    ),
    Round314CaseCandidate(
        "r6_loop16_kospi_brokerage_financial_beta",
        "securities_sector/financial_groups_sector",
        "Korea securities and financial groups basket",
        E2RArchetype.BROKERAGE_TRADING_VOLUME_STAGE2_BETA,
        (E2RArchetype.BROKERAGE_MARKET_VOLUME_STAGE2_ACTIONABLE, E2RArchetype.SECURITIES_BROKERAGE_MARKET_BETA),
        "cyclical_success",
        "Stage2_market_beta_with_4B_fee_gate",
        "r6l16_kospi_brokerage_T1",
        "Stage2_brokerage_trading_volume_beta",
        "Stage2 beta + 4B-watch",
        date(2025, 1, 1),
        date(2026, 5, 14),
        None,
        date(2026, 5, 14),
        None,
        False,
        ("kospi_plus_6_45pct", "kospi_close_7384_56", "foreign_net_buy_krw_3_1tn", "securities_plus_13_5pct", "financial_groups_plus_4_2pct"),
        ("brokerage_fee_income_missing", "IB_WM_income_bridge_missing", "market_beta_without_earnings_4B", "tax_or_leverage_policy_watch"),
        13.5,
        None,
        None,
        None,
        None,
        None,
        {"kospi_event_return_pct": 6.45, "kospi_close": 7384.56, "foreign_net_buy_krw_tn": 3.1, "foreign_net_buy_usd_bn": 2.13, "securities_return_pct": 13.5, "financial_groups_return_pct": 4.2},
        "aligned",
        "Stage2_beta_not_structural_Green",
        "cyclical_rerating",
        "stage2_watch_success",
        "Market beta can route brokerage to Stage2, but fee income and ROE conversion are required before Yellow or Green.",
    ),
    Round314CaseCandidate(
        "r6_loop16_naver_financial_dunamu_ma",
        "035420/Dunamu_private",
        "Naver Financial / Dunamu",
        E2RArchetype.FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4B,
        (E2RArchetype.FINTECH_CRYPTO_M_AND_A_TRUST_GATE, E2RArchetype.DIGITAL_ASSET_MA_TRUST_4C_WATCH),
        "success_candidate",
        "Stage2_crypto_MA_with_security_4B",
        "r6l16_naver_dunamu_T1",
        "Stage2_crypto_exchange_MA_security_gate",
        "Stage2 + 4B-watch",
        date(2025, 11, 27),
        date(2025, 11, 27),
        None,
        date(2025, 11, 27),
        None,
        False,
        ("deal_value_krw_15_13tn", "deal_value_usd_10_27bn", "share_swap_structure", "naver_initial_plus_7pct", "upbit_market_share_70pct"),
        ("regulatory_approval_missing", "custody_security_AML_missing", "abnormal_withdrawal_krw_54bn", "post_event_minus_4_2pct", "crypto_MA_without_security_controls_4B"),
        7.0,
        -4.2,
        None,
        None,
        None,
        None,
        {"deal_value_krw_tn": 15.13, "deal_value_usd_bn": 10.27, "naver_initial_return_pct": 7, "naver_later_return_pct": -4.2, "abnormal_withdrawal_krw_bn": 54, "upbit_market_share_pct": 70},
        "evidence_good_but_price_failed",
        "Stage2_crypto_MA_but_security_gate_open",
        "unknown",
        "stage2_watch_success",
        "Crypto exchange M&A has deal size and market share, but approval, custody and abnormal-withdrawal controls block Green.",
    ),
    Round314CaseCandidate(
        "r6_loop16_hana_bank_dunamu_stake",
        "086790/Dunamu_private",
        "Hana Financial / Dunamu stake",
        E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE,
        (E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2, E2RArchetype.DIGITAL_ASSET_BANK_STAKE_STAGE2),
        "success_candidate",
        "Stage2_bank_digital_asset_stake_with_capital_gate",
        "r6l16_hana_dunamu_T1",
        "Stage2_bank_digital_asset_stake",
        "Stage2 + 4B-watch",
        date(2026, 5, 14),
        date(2026, 5, 15),
        None,
        date(2026, 5, 15),
        None,
        False,
        ("dunamu_stake_6_55pct", "stake_value_krw_1tn", "shares_2_284mn", "upbit_share_over_80pct", "kakao_investment_post_sale_4_03pct"),
        ("capital_ratio_treatment_missing", "equity_method_income_missing", "regulatory_approval_missing", "bank_digital_asset_without_capital_clarity_4B"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"stake_pct": 6.55, "stake_value_krw_tn": 1.0, "stake_value_usd_bn": 0.7, "shares_mn": 2.284, "upbit_share_pct": ">80", "kakao_investment_post_sale_pct": 4.03},
        "evidence_good_but_price_failed",
        "Stage2_stake_value_but_capital_gate_open",
        "unknown",
        "stage2_watch_success",
        "A bank digital-asset stake can be Stage2, but capital ratio, approval and earnings pickup must be visible before Green.",
    ),
    Round314CaseCandidate(
        "r6_loop16_won_stablecoin_policy_mania",
        "377300/LG_CNS/158430/201490",
        "Kakao Pay / LG CNS / Aton / ME2ON stablecoin basket",
        E2RArchetype.STABLECOIN_POLICY_EVENT_PREMIUM_4B,
        (E2RArchetype.STABLECOIN_POLICY_4B_OVERHEAT, E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE),
        "overheat",
        "policy_event_premium_4B",
        "r6l16_stablecoin_policy_T1",
        "stablecoin_policy_event_premium_4B",
        "4B-watch",
        date(2025, 6, 1),
        None,
        None,
        date(2025, 6, 1),
        None,
        False,
        ("kakao_pay_over_100pct", "lg_cns_plus_70pct", "aton_plus_80pct", "me2on_tripled", "stablecoin_minimum_equity_krw_500mn"),
        ("issuer_license_missing", "reserve_rule_missing", "revenue_model_missing", "stablecoin_policy_without_license_4B", "FX_capital_flow_risk"),
        200.0,
        None,
        None,
        None,
        None,
        None,
        {"kakao_pay_return_context_pct": ">100", "lg_cns_return_pct": 70, "aton_return_pct": 80, "me2on_return_context": "tripled", "minimum_equity_krw_mn": 500, "q1_2025_stablecoin_capital_outflow_usd_bn": 19},
        "false_positive_score",
        "policy_theme_4B_not_Green",
        "theme_overheat",
        "false_green",
        "Stablecoin policy can create event premium, but issuer license, reserve quality and revenue model are required before constructive staging.",
    ),
    Round314CaseCandidate(
        "r6_loop16_hongkong_els_misselling_banks",
        "105560/055550/086790/316140/bank_basket",
        "Korea bank basket / Hong Kong ELS mis-selling",
        E2RArchetype.ELS_MISSELLING_CONSUMER_PROTECTION_4C,
        (E2RArchetype.BANK_CREDIT_COST_PF_OVERLAY, E2RArchetype.FINANCIAL_GROUP_VALUEUP_STAGE2),
        "4c_thesis_break",
        "hard_4C_consumer_protection",
        "r6l16_els_misselling_T0",
        "hard_4C_consumer_protection",
        "4C",
        date(2024, 3, 11),
        None,
        None,
        None,
        date(2024, 3, 11),
        True,
        ("fss_investigation_2024_03_11", "retail_losses_krw_5_8tn", "compensation_range_20_60pct", "expected_fine_per_bank_krw_1tn", "fsc_final_approval_required"),
        ("mis_selling_consumer_protection_fine_4C", "capital_ratio_pressure", "trust_damage", "valueup_rally_blocked_until_liability_cleared"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"investigation_date": "2024-03-11", "losses_krw_tn": 5.8, "compensation_low_pct": 20, "compensation_high_pct": 60, "expected_fine_per_bank_krw_tn": 1.0, "penalty_date": "2026-02-12"},
        "aligned",
        "consumer_protection_hard_4C",
        "thesis_break",
        "should_have_been_red",
        "ELS mis-selling is a hard consumer-protection 4C gate for bank rerating until liability and capital impact are cleared.",
    ),
    Round314CaseCandidate(
        "r6_loop16_overseas_stock_fx_flow",
        "securities_basket/banks",
        "Korea overseas-stock flow brokers and banks",
        E2RArchetype.FX_OVERSEAS_STOCK_FLOW_4C_WATCH,
        (E2RArchetype.BROKERAGE_TRADING_VOLUME_STAGE2_BETA, E2RArchetype.STABLECOIN_POLICY_OVERHEAT_FX_GATE),
        "4b_watch",
        "Stage2_flow_with_FX_4C_watch",
        "r6l16_overseas_stock_fx_T1",
        "Stage2_overseas_stock_flow_FX_watch",
        "Stage2 + 4C-watch",
        date(2026, 1, 29),
        date(2026, 2, 4),
        None,
        date(2026, 2, 4),
        None,
        False,
        ("overseas_stock_holdings_usd_171bn", "jan_net_buys_usd_5bn", "dec_net_buys_usd_1_9bn", "won_near_17y_low", "fss_fx_review"),
        ("FX_risk_disclosure_missing", "consumer_protection_risk", "fee_conversion_missing", "overseas_stock_flow_without_FX_risk_4C_watch"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"holdings_usd_bn": 171, "jan_net_buys_usd_bn": 5.0, "dec_net_buys_usd_bn": 1.9, "won_context": "near_17y_low", "fss_fx_review": True},
        "aligned",
        "Stage2_flow_but_FX_4C_watch",
        "event_premium",
        "stage2_watch_success",
        "Retail overseas-stock flow can help brokerage fees, but FX disclosure and consumer protection must be explicit.",
    ),
    Round314CaseCandidate(
        "r6_loop16_toss_global_stablecoin_ipo",
        "private",
        "Toss / Viva Republica",
        E2RArchetype.PRIVATE_FINTECH_STABLECOIN_IPO_OPTIONALITY_STAGE2,
        (E2RArchetype.FINTECH_SUPERAPP_IPO_OPTION_KOREA, E2RArchetype.KRW_STABLECOIN_POLICY_OPTION),
        "success_candidate",
        "private_fintech_optionality_stage2_reference",
        "r6l16_toss_ipo_stablecoin_T1",
        "private_fintech_stablecoin_IPO_optionality",
        "Stage2 private reference",
        date(2025, 9, 9),
        date(2025, 9, 9),
        None,
        date(2025, 9, 9),
        None,
        False,
        ("users_30mn", "australia_launch_end_2025", "won_stablecoin_plan", "us_ipo_q2_2026", "valuation_above_10_to_15bn_usd"),
        ("private_company_no_listed_price", "license_missing", "revenue_model_missing", "credit_quality_missing", "private_valuation_4B"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"users_mn": 30, "australia_launch": "end_2025", "won_stablecoin_plan": True, "us_ipo_target": "2026_Q2", "valuation_usd_bn_range": ">10_to_>15"},
        "unknown",
        "private_optionality_reference_not_live_Green",
        "unknown",
        "stage2_watch_success",
        "Toss is a private Stage2 optionality reference; listing, license and profit evidence are required before any Green-style conclusion.",
    ),
)


ROUND314_TRIGGER_RECORDS: tuple[Round314TriggerRecord, ...] = (
    Round314TriggerRecord("r6l16_samsung_buyback_T1", "r6_loop16_samsung_buyback_capital_allocation", "Stage2-Actionable_buyback_cancellation", "2024-11-15", "Samsung announces 10T won buyback with 3T won initial cancellation; shares +7.2% after a YTD drawdown.", 7.2, "excellent_stage2_buyback_candidate_not_Green", "Stage2-Actionable", {"buyback_krw_tn": 10, "initial_cancelled_repurchase_krw_tn": 3}),
    Round314TriggerRecord("r6l16_sk_square_buyback_T1", "r6_loop16_sk_square_buyback_holdco_discount", "Stage2_holdco_discount_buyback", "2024-11-21", "SK Square cancels previous 100B won buyback and announces another 100B won repurchase/cancellation plan against a large Hynix stake discount.", "price_anchor_missing", "Stage2_holdco_discount_but_discount_close_pending", "Stage2", {"new_repurchase_cancel_krw_bn": 100}),
    Round314TriggerRecord("r6l16_kospi_brokerage_T1", "r6_loop16_kospi_brokerage_financial_beta", "Stage2_brokerage_beta", "2026-05-14", "KOSPI +6.45% to 7,384.56, foreign net buy 3.1T won, securities basket +13.5%.", 13.5, "Stage2_beta_not_structural_Green", "Stage2+4B", {"foreign_net_buy_krw_tn": 3.1}),
    Round314TriggerRecord("r6l16_naver_dunamu_T1", "r6_loop16_naver_financial_dunamu_ma", "Stage2_crypto_exchange_MA_security_gate", "2025-11-27", "Naver Financial/Dunamu deal value 15.13T won; Naver initially +7%, later -4.2%; abnormal withdrawal 54B won remains a trust gate.", 7.0, "Stage2_crypto_MA_but_security_gate_open", "Stage2+4B", {"deal_value_krw_tn": 15.13, "abnormal_withdrawal_krw_bn": 54}),
    Round314TriggerRecord("r6l16_hana_dunamu_T1", "r6_loop16_hana_bank_dunamu_stake", "Stage2_bank_digital_asset_stake", "2026-05-15", "Hana has 6.55% Dunamu stake with 1T won value context and Upbit share above 80%; capital treatment is the gate.", "price_anchor_missing", "Stage2_stake_value_but_capital_gate_open", "Stage2+4B", {"stake_pct": 6.55, "stake_value_krw_tn": 1.0}),
    Round314TriggerRecord("r6l16_stablecoin_policy_T1", "r6_loop16_won_stablecoin_policy_mania", "stablecoin_policy_event_premium_4B", "2025-06-01", "Stablecoin related names double/triple before issuer license, reserve rule and revenue model are confirmed.", "basket_70_to_200pct_context", "policy_theme_4B_not_Green", "4B-watch", {"minimum_equity_krw_mn": 500}),
    Round314TriggerRecord("r6l16_els_misselling_T0", "r6_loop16_hongkong_els_misselling_banks", "hard_4C_consumer_protection", "2024-03-11", "Hong Kong ELS mis-selling investigation starts; losses 5.8T won and compensation/fine risk create hard consumer-protection gate.", None, "consumer_protection_hard_4C", "4C", {"losses_krw_tn": 5.8}),
    Round314TriggerRecord("r6l16_overseas_stock_fx_T1", "r6_loop16_overseas_stock_fx_flow", "Stage2_overseas_stock_flow_FX_watch", "2026-02-04", "Overseas stock holdings 171B USD and January net buys 5B USD while won is near 17-year lows; FSS FX review is a 4C-watch gate.", None, "Stage2_flow_but_FX_4C_watch", "Stage2+4C-watch", {"holdings_usd_bn": 171, "jan_net_buys_usd_bn": 5.0}),
    Round314TriggerRecord("r6l16_toss_ipo_stablecoin_T1", "r6_loop16_toss_global_stablecoin_ipo", "private_fintech_stablecoin_IPO_optionality", "2025-09-09", "Toss has 30M users, overseas launch and IPO/stablecoin optionality, but it is a private reference until listing and license evidence exist.", None, "private_optionality_reference_not_live_Green", "Stage2_private_reference", {"users_mn": 30}),
)


ROUND314_SHADOW_WEIGHT_ROWS: tuple[Round314ShadowWeightRow, ...] = (
    Round314ShadowWeightRow(E2RArchetype.BUYBACK_CANCELLATION_VALUEUP_STAGE2_ACTIONABLE, 5, 4, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, "buyback+cancellation+event return", "business recovery pending", "executed cancellation+ROE/EPS recovery", "Samsung template."),
    Round314ShadowWeightRow(E2RArchetype.HOLDCO_DISCOUNT_BUYBACK_STAGE2, 4, 1, 5, 0, 0, 0, 0, 0, 0, -1, 0, 0, "discount+repeat cancellation", "discount compression pending", "repeat execution+NAV intact", "SK Square template."),
    Round314ShadowWeightRow(E2RArchetype.BROKERAGE_TRADING_VOLUME_STAGE2_BETA, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, -5, 0, "trading value+foreign flow", "fee income pending", "fee income+ROE proof", "Brokerage beta template."),
    Round314ShadowWeightRow(E2RArchetype.FINTECH_CRYPTO_EXCHANGE_MA_STAGE2_WITH_SECURITY_4B, 0, 0, 0, 0, 4, 5, 0, 0, 0, -2, 0, -5, "deal value+approval path", "security and custody pending", "closed deal+security+revenue", "Naver/Dunamu template."),
    Round314ShadowWeightRow(E2RArchetype.BANK_DIGITAL_ASSET_STAKE_STAGE2_WITH_CAPITAL_GATE, 0, 0, 0, 0, 4, 4, 5, 0, 0, -2, 0, -4, "stake value+exchange share", "capital treatment pending", "capital+revenue+trust", "Hana/Dunamu template."),
    Round314ShadowWeightRow(E2RArchetype.STABLECOIN_POLICY_EVENT_PREMIUM_4B, 0, 0, 0, 0, 2, 1, 0, 0, 2, -5, 0, -2, "policy event only", "license/reserve missing", "licensed issuer economics", "Stablecoin theme template."),
    Round314ShadowWeightRow(E2RArchetype.ELS_MISSELLING_CONSUMER_PROTECTION_4C, 0, 0, 0, 0, 0, 0, -5, -5, 0, 0, 0, 0, "not positive", "liability clearing required", "N/A", "Bank ELS 4C template."),
    Round314ShadowWeightRow(E2RArchetype.FX_OVERSEAS_STOCK_FLOW_4C_WATCH, 0, 0, 0, 3, 0, 0, 0, 1, 5, 0, -2, 0, "overseas flow+fee bridge", "FX disclosure pending", "fee conversion+FX risk control", "Overseas-stock flow template."),
    Round314ShadowWeightRow(E2RArchetype.PRIVATE_FINTECH_STABLECOIN_IPO_OPTIONALITY_STAGE2, 0, 1, 0, 0, 3, 2, 0, 0, 1, -4, 0, -3, "private users+IPO option", "license/listing pending", "listed price+licensed revenue", "Toss private reference."),
)


def round314_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND314_CASE_CANDIDATES]


def round314_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND314_CASE_CANDIDATES]


def round314_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND314_TRIGGER_RECORDS]


def round314_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND314_SHADOW_WEIGHT_ROWS]


def round314_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND314_REQUIRED_TARGET_ALIASES.items()]


def round314_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND314_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND314_SCORE_DOWN_AXES]
    )


def round314_summary() -> dict[str, object]:
    return {
        "source_round": ROUND314_SOURCE_ROUND_PATH,
        "round_id": ROUND314_ANALYST_ROUND_ID,
        "large_sector": ROUND314_LARGE_SECTOR,
        "method": ROUND314_METHOD,
        "case_candidate_count": len(ROUND314_CASE_CANDIDATES),
        "trigger_count": len(ROUND314_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND314_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 3,
        "stage2_event_candidate_count": 5,
        "private_stage2_reference_count": 1,
        "stage3_yellow_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 6,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 1,
        "evidence_good_but_price_failed_or_muted_count": 3,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R7 Loop 16",
    }


def round314_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND314_SOURCE_ROUND_PATH,
        "round_id": ROUND314_ANALYST_ROUND_ID,
        "large_sector": ROUND314_LARGE_SECTOR,
        "method": ROUND314_METHOD,
        "summary": round314_summary(),
        "required_target_aliases": dict(ROUND314_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND314_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND314_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND314_STAGE3_GREEN_RULES,
        "green_blockers": ROUND314_GREEN_BLOCKERS,
        "score_up_axes": ROUND314_SCORE_UP_AXES,
        "score_down_axes": ROUND314_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND314_STAGE4B_WATCH_TRIGGERS,
        "stage4c_watch_gates": ROUND314_4C_WATCH_GATES,
        "row_separation_rules": ROUND314_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round314_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_buyback_stablecoin_crypto_MA_market_beta_or_private_fintech_headline_as_green_without_ROE_EPS_security_approval_revenue_or_FCF",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round314_summary_markdown() -> str:
    summary = round314_summary()
    lines = [
        "# R6 Loop 16 Financial Capital Allocation / Digital Finance Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: a stablecoin policy rally is a 4B-watch event until issuer license, reserve rules and revenue economics are visible.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Buyback, holdco discount, brokerage beta and digital-asset optionality can create Stage2 candidates.",
            "- Stage2 examples: Samsung buyback/cancellation, SK Square holdco discount, brokerage trading-volume beta, Naver/Dunamu crypto M&A and Hana/Dunamu stake.",
            "- Stage3-Green confirmed: `0`.",
            "- Hard 4C reference: Hong Kong ELS mis-selling / consumer-protection liability.",
            "- Stablecoin policy and crypto M&A remain 4B-watch until license, reserve, approval, custody and revenue gates close.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round314_trigger_grid_markdown() -> str:
    lines = [
        "# Round 314 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round314_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round314_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 314 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND314_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND314_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND314_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND314_GREEN_BLOCKERS),
            "",
            "## 4C Watch Gates",
            *_bullet_lines(ROUND314_4C_WATCH_GATES),
        ]
    ) + "\n"


def render_round314_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 314 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND314_STAGE4B_WATCH_TRIGGERS),
        "",
        "## 4C Watch Gates",
        *_bullet_lines(ROUND314_4C_WATCH_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND314_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round314_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 314 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND314_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round314_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 314 Row Separation Plan",
        "",
        "Case evidence, trigger anchors and full OHLC windows must be separate rows.",
        "",
        "Easy example: a crypto exchange M&A trigger can be Stage2. It is not Green until approval, custody/security and revenue gates are visible.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND314_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round314_r6_loop16_reports(
    output_directory: str | Path = ROUND314_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND314_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND314_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND314_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND314_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round314_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND314_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round314_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round314_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round314_r6_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round314_r6_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round314_r6_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round314_r6_loop16_trigger_grid.md",
        "summary": output_dir / "round314_r6_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round314_r6_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round314_r6_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round314_r6_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round314_r6_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round314_r6_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round314_r6_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round314_case_rows())
    _write_csv(paths["target_aliases"], round314_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round314_trigger_rows())
    _write_csv(paths["score_adjustments"], round314_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round314_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round314_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round314_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round314_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round314_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round314_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round314_row_separation_plan_markdown(), encoding="utf-8")
    return paths


def _write_csv(path: Path, rows: Iterable[Mapping[str, str]]) -> None:
    rows = list(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _write_jsonl(path: Path, rows: Iterable[Mapping[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _signed(value: int) -> str:
    return f"{value:+d}" if value else "+0"


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    return str(value)


def _bullet_lines(items: Iterable[str]) -> list[str]:
    return [f"- {item}" for item in items]


__all__ = [
    "ROUND314_4C_WATCH_GATES",
    "ROUND314_CASE_CANDIDATES",
    "ROUND314_GREEN_BLOCKERS",
    "ROUND314_LARGE_SECTOR",
    "ROUND314_REQUIRED_TARGET_ALIASES",
    "ROUND314_ROW_SEPARATION_RULES",
    "ROUND314_SCORE_DOWN_AXES",
    "ROUND314_SCORE_UP_AXES",
    "ROUND314_SHADOW_WEIGHT_ROWS",
    "ROUND314_STAGE2_ACTIONABLE_RULES",
    "ROUND314_STAGE3_GREEN_RULES",
    "ROUND314_STAGE3_YELLOW_RULES",
    "ROUND314_STAGE4B_WATCH_TRIGGERS",
    "ROUND314_TRIGGER_RECORDS",
    "render_round314_stage4b_4c_review_markdown",
    "render_round314_stage_rules_markdown",
    "render_round314_trigger_grid_markdown",
    "round314_audit_payload",
    "round314_case_records",
    "round314_case_rows",
    "round314_shadow_weight_rows",
    "round314_summary",
    "round314_trigger_rows",
    "write_round314_r6_loop16_reports",
]
