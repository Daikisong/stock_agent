"""Round-321 R13 Loop-16 cross-archetype RedTeam validation pack.

This module converts ``docs/round/round_321.md`` into calibration-only case
records, trigger rows, shadow weights, and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: Samsung E&A's large Fadhili EPC contract and +8.5% event return
can justify Stage2-Actionable review. It is still not Stage3-Green until EPC
margin, working capital, claims, cost escalation and cash conversion are visible.
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


ROUND321_SOURCE_ROUND_PATH = "docs/round/round_321.md"
ROUND321_ANALYST_ROUND_ID = "round_249"
ROUND321_LARGE_SECTOR = "CROSS_ARCHETYPE_REDTEAM_4B_4C_ACCOUNTING_TRUST_PRICE_VALIDATION"
ROUND321_METHOD = "trigger_level_redteam_v1"
ROUND321_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round321_r13_loop16_cross_archetype_redteam_price_validation"
ROUND321_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r13_loop16_round249.jsonl"
ROUND321_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r13_loop16_round249.jsonl"
ROUND321_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round321_r13_loop16_cross_archetype_redteam_price_validation_audit.json"
ROUND321_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round249_r13_loop16_v1.csv"

ROUND321_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "CROSS_STAGE2_ACTIONABLE_CONFIRMED": E2RArchetype.CROSS_STAGE2_ACTIONABLE_CONFIRMED.value,
    "GOOD_EVIDENCE_PRICE_FAILED": E2RArchetype.GOOD_EVIDENCE_PRICE_FAILED.value,
    "CONTRACT_VALUE_WITH_MARGIN_GATE": E2RArchetype.CONTRACT_VALUE_WITH_MARGIN_GATE.value,
    "GROWTH_WITH_DILUTION_4B": E2RArchetype.GROWTH_WITH_DILUTION_4B.value,
    "EXPORT_ORDER_TO_COMBAT_VALIDATION_YELLOW": E2RArchetype.EXPORT_ORDER_TO_COMBAT_VALIDATION_YELLOW.value,
    "POLICY_OR_PREFERRED_BIDDER_WITH_LEGAL_4B": E2RArchetype.POLICY_OR_PREFERRED_BIDDER_WITH_LEGAL_4B.value,
    "SECURITY_TRUST_BREAK_HARD_4C": E2RArchetype.SECURITY_TRUST_BREAK_HARD_4C.value,
    "TARIFF_RELIEF_THAT_STILL_SELLOFF": E2RArchetype.TARIFF_RELIEF_THAT_STILL_SELLOFF.value,
    "FOREIGN_STRATEGIC_CAPITAL_WITH_CB_4B": E2RArchetype.FOREIGN_STRATEGIC_CAPITAL_WITH_CB_4B.value,
}

ROUND321_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_at_least_5pct",
    "market_relative_return_at_least_5pp",
    "contract_deal_or_funding_value_is_clear",
    "trigger_source_is_hard_source_such_as_disclosure_reuters_court_or_government",
    "trigger_can_connect_to_revenue_backlog_or_capital_allocation",
    "4B_overlay_is_identified_and_limited",
    "price_beats_issue_price_or_prior_expectation",
)

ROUND321_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "delivery_or_execution_schedule_is_realizing",
    "margin_or_cash_conversion_visibility_improves",
    "repeat_order_adoption_or_user_conversion_evidence_exists",
    "legal_final_contract_or_dilution_absorption_gate_is_partly_closed",
    "4B_overlay_is_reduced_to_manageable_level",
)

ROUND321_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "margin_revenue_or_cash_conversion_confirmed_after_Stage2_Actionable",
    "4B_overlay_cleared_or_contained",
    "legal_approval_contract_or_policy_finality_closed",
    "price_holds_after_event_without_below_entry_break",
    "full_OHLC_MFE_MAE_window_supports_candidate",
)

ROUND321_GREEN_BLOCKERS: tuple[str, ...] = (
    "theme_label_without_price_validation",
    "ipo_demand_without_post_listing_strength",
    "preferred_bidder_without_contract",
    "growth_with_dilution_ignored",
    "contract_without_margin",
    "user_shift_without_revenue",
    "policy_or_trade_relief_headline",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND321_SCORE_UP_AXES: tuple[str, ...] = (
    "reported_event_return",
    "market_relative_return",
    "contract_value_visibility",
    "strategic_capital_quality",
    "delivery_margin_conversion",
    "security_trust_break",
    "legal_finality",
    "tariff_margin_reality",
)

ROUND321_SCORE_DOWN_AXES: tuple[str, ...] = (
    "theme_label_without_price_validation",
    "ipo_demand_without_post_listing_strength",
    "preferred_bidder_without_contract",
    "growth_with_dilution_ignored",
    "contract_without_margin",
    "user_shift_without_revenue",
    "policy_or_trade_relief_headline",
)

ROUND321_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "good_order_followed_by_large_dilution_or_CB",
    "preferred_bidder_followed_by_legal_appeal_or_court_block",
    "AI_cloud_headline_followed_by_below_issue_price",
    "tariff_relief_headline_followed_by_stock_selloff",
    "user_shift_without_revenue_or_margin_conversion",
    "policy_reform_without_company_specific_action",
    "contract_value_without_margin_or_cash_conversion",
)

ROUND321_HARD_4C_GATES: tuple[str, ...] = (
    "customer_trust_breach_with_user_or_spending_deterioration",
    "fatal_accident_or_safety_collapse",
    "political_crisis_or_market_wide_confidence_break",
    "PF_default_or_liquidity_freeze",
    "final_contract_legally_blocked_for_long_period",
    "regulatory_sanction_that_changes_business_model",
)

ROUND321_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_return_contract_value_legal_or_selloff_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_news_size_as_entry_quality_without_price_conversion_dilution_legal_margin_trust_or_tariff_gates",
)


@dataclass(frozen=True)
class Round321TriggerRecord:
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
class Round321CaseCandidate:
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
            "do_not_use_round321_cases_as_candidate_generation_input",
            "do_not_treat_news_size_as_entry_quality_without_price_conversion_dilution_legal_margin_trust_or_tariff_gates",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "dilution" in field
            or "CB" in field
            or "margin" in field
            or "legal" in field
            or "tariff" in field
            or "price_failed" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "breach" in field
            or "trust" in field
            or "tariff_margin_damage" in field
            or "court_blocks" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND321_LARGE_SECTOR,
            large_sector=ROUND321_LARGE_SECTOR,
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
            must_have_fields=ROUND321_STAGE3_GREEN_RULES,
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
                mfe_30d=self.event_mfe_pct,
                mae_30d=self.event_mae_pct,
                price_validation_status="price_data_unavailable_after_deep_search",
            ),
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
            "event_mfe_pct": _value_text(self.event_mfe_pct),
            "event_mae_pct": _value_text(self.event_mae_pct),
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND321_CASE_CANDIDATES: tuple[Round321CaseCandidate, ...] = (
    Round321CaseCandidate(
        "r13_loop16_samsung_sds_kkr_cross_redteam",
        "018260",
        "Samsung SDS",
        E2RArchetype.FOREIGN_STRATEGIC_CAPITAL_WITH_CB_4B,
        (E2RArchetype.CROSS_STAGE2_ACTIONABLE_CONFIRMED, E2RArchetype.STRATEGIC_CAPITAL_WITH_DILUTION_4B),
        "success_candidate",
        "Stage2_Actionable_foreign_strategic_capital_with_CB_4B",
        "T1/T2",
        "Stage2-Actionable_foreign_strategic_capital",
        "Stage2-Actionable + 4B-watch",
        date(2025, 1, 1),
        date(2026, 4, 15),
        None,
        date(2026, 4, 15),
        None,
        False,
        ("KKR_820M_usd_CB", "intraday_plus_20_8pct", "morning_plus_19_4pct", "KOSPI_plus_3_0pct", "market_relative_morning_plus_16_4pp", "cash_balance_6_4T_won", "M&A_capital_allocation_AI_expansion_advisory"),
        ("CB_dilution_4B", "AI_execution_missing", "M&A_ROIC_missing", "physical_AI_stablecoin_overextension", "full_OHLC_MFE_MAE_missing"),
        20.8,
        None,
        {"trigger_date": "2026-04-15", "event_return_intraday_pct": 20.8, "event_return_morning_pct": 19.4, "kospi_same_context_pct": 3.0, "market_relative_morning_pp": 16.4, "cb_value_usd_mn": 820, "cash_balance_krw_trn": 6.4},
        "aligned",
        "excellent_stage2_actionable_with_4B",
        "event_premium",
        "stage2_watch_success",
        "Strong foreign strategic capital trigger, but CB dilution and AI/M&A execution remain 4B gates.",
    ),
    Round321CaseCandidate(
        "r13_loop16_samsung_ea_fadhili_cross_redteam",
        "028050",
        "Samsung E&A",
        E2RArchetype.CONTRACT_VALUE_WITH_MARGIN_GATE,
        (E2RArchetype.CROSS_STAGE2_ACTIONABLE_CONFIRMED, E2RArchetype.OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE),
        "success_candidate",
        "Stage2_Actionable_contract_value_with_margin_gate",
        "T1/T2",
        "Stage2-Actionable_contract_value",
        "Stage2-Actionable + margin 4B-watch",
        date(2024, 4, 2),
        date(2024, 4, 3),
        None,
        date(2024, 4, 3),
        None,
        False,
        ("Fadhili_EPC_contract_context_6B_usd", "event_return_plus_8_5pct", "event_price_26750_won", "KOSPI_minus_1_4pct", "market_relative_plus_9_9pp", "capacity_expansion_to_4B_scf_day", "completion_Nov_2027"),
        ("EPC_margin_missing", "working_capital_missing", "claims_missing", "cost_escalation_missing", "execution_delay_4B", "full_OHLC_MFE_MAE_missing"),
        8.5,
        None,
        {"trigger_date": "2024-04-03", "contract_value_context_usd_bn": 6.0, "event_return_pct": 8.5, "event_price_krw": 26750, "kospi_same_context_pct": -1.4, "market_relative_return_pp": 9.9},
        "aligned",
        "excellent_stage2_actionable_contract_with_margin_gate",
        "event_premium",
        "stage2_watch_success",
        "Contract value and price reaction are aligned. Yellow/Green waits for EPC margin and cash conversion.",
    ),
    Round321CaseCandidate(
        "r13_loop16_hanwha_export_dilution_cross_redteam",
        "012450",
        "Hanwha Aerospace",
        E2RArchetype.GROWTH_WITH_DILUTION_4B,
        (E2RArchetype.DEFENSE_BACKLOG_DILUTION_4B, E2RArchetype.CROSS_STAGE2_ACTIONABLE_CONFIRMED),
        "success_candidate",
        "Stage2_Actionable_export_with_dilution_4B",
        "T1/T3",
        "Stage2-Actionable_export_with_dilution_4B",
        "Stage2-Actionable + dilution 4B-watch",
        date(2022, 2, 24),
        date(2024, 7, 9),
        None,
        date(2025, 3, 21),
        None,
        False,
        ("Romania_K9_K10_order_1B_usd", "export_event_return_above_5pct", "record_high", "backlog_5_1T_to_30T_won", "global_howitzer_export_share_above_50pct", "capital_raise_plan_3_6T_won", "dilution_event_minus_13pct"),
        ("dilution_4B", "delivery_margin_missing", "capacity_missing", "dilution_absorption_missing", "full_OHLC_MFE_MAE_missing"),
        5.0,
        -13.0,
        {"export_trigger_date": "2024-07-09", "contract_value_usd_bn": 1.0, "export_event_return_pct": ">5", "backlog_end_2021_krw_trn": 5.1, "backlog_mar_2024_krw_trn": 30, "dilution_trigger_date": "2025-03-21", "capital_raise_plan_krw_trn": 3.6, "dilution_event_return_pct": -13},
        "aligned",
        "Stage2_success_with_4B_dilution",
        "event_premium",
        "stage2_watch_success",
        "Defense export success remains real, but capital raise dilution is a live 4B overlay.",
    ),
    Round321CaseCandidate(
        "r13_loop16_lig_nex1_export_yellow_cross_redteam",
        "079550",
        "LIG Nex1",
        E2RArchetype.EXPORT_ORDER_TO_COMBAT_VALIDATION_YELLOW,
        (E2RArchetype.MISSILE_DEFENSE_COMBAT_VALIDATION_STAGE3_YELLOW, E2RArchetype.CROSS_STAGE2_ACTIONABLE_CONFIRMED),
        "success_candidate",
        "Stage3_Yellow_candidate_export_validation",
        "T0/T2",
        "Stage3-Yellow_candidate_export_validation",
        "Stage3-Yellow candidate",
        date(2024, 9, 20),
        date(2024, 9, 20),
        date(2026, 3, 11),
        date(2026, 3, 11),
        None,
        False,
        ("Iraq_M-SAM_II_order_3_71T_won", "contract_value_2_8B_usd", "event_return_plus_3_6pct", "KOSPI_plus_0_9pct", "market_relative_plus_2_7pp", "Iraq_fourth_operator", "combat_validation_plus_47pct_context"),
        ("production_capacity_missing", "delivery_schedule_missing", "war_event_premium_4B", "export_finance_missing", "margin_missing", "full_OHLC_MFE_MAE_missing"),
        47.0,
        None,
        {"trigger_date": "2024-09-20", "contract_value_krw_trn": 3.71, "contract_value_usd_bn": 2.8, "event_return_pct": 3.6, "kospi_same_context_pct": 0.9, "market_relative_return_pp": 2.7, "operator_count_after_iraq": 4},
        "aligned",
        "Stage3_Yellow_candidate_not_Green",
        "event_premium",
        "yellow_success",
        "Export order plus operator expansion and combat validation support Yellow candidate review; Green waits for delivery, production capacity and margin.",
    ),
    Round321CaseCandidate(
        "r13_loop16_lg_cns_ipo_false_positive_cross_redteam",
        "064400",
        "LG CNS",
        E2RArchetype.GOOD_EVIDENCE_PRICE_FAILED,
        (E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED, E2RArchetype.AI_CLOUD_IPO_FALSE_POSITIVE),
        "failed_rerating",
        "evidence_good_but_price_failed",
        "T1",
        "evidence_good_but_price_failed",
        "not actionable",
        date(2025, 2, 5),
        None,
        None,
        date(2025, 2, 5),
        None,
        False,
        ("IPO_raise_1_2T_won", "IPO_raise_827_1M_usd", "AI_cloud_services_over_half_sales", "issue_price_61900_won", "debut_open_60500_won", "debut_later_59700_won", "below_issue_price"),
        ("IPO_overhang_4B", "valuation_missing", "external_AI_cloud_revenue_missing", "margin_uncertainty", "post_listing_strength_missing", "price_failed"),
        None,
        -3.55,
        {"trigger_date": "2025-02-05", "ipo_raise_krw_trn": 1.2, "ipo_raise_usd_mn": 827.1, "issue_price_krw": 61900, "debut_open_krw": 60500, "debut_later_price_krw": 59700, "price_vs_issue": "below_issue_price"},
        "evidence_good_but_price_failed",
        "false_positive_if_promoted_to_stage3",
        "no_rerating",
        "false_yellow",
        "AI/cloud evidence was real, but below-issue-price trading blocks Actionable or Green promotion.",
    ),
    Round321CaseCandidate(
        "r13_loop16_coupang_security_delivery_cross_redteam",
        "CPNG/035420/000120/139480",
        "Coupang / Naver / CJ Logistics / E-Mart",
        E2RArchetype.SECURITY_TRUST_BREAK_HARD_4C,
        (E2RArchetype.EVERYDAY_DELIVERY_SHARE_SHIFT_STAGE2_WITH_SECURITY_4C, E2RArchetype.ECOMMERCE_SECURITY_TRUST_4C_AND_RIVAL_STAGE2),
        "4c_thesis_break",
        "hard_4C_with_rival_Stage2",
        "T0/T2",
        "hard_4C_with_rival_Stage2",
        "4C + rival Stage2 watch",
        date(2025, 11, 1),
        date(2026, 2, 25),
        None,
        None,
        date(2025, 11, 1),
        True,
        ("affected_users_34M", "Coupang_minus_34pct", "mobile_MAU_minus_3_5pct", "daily_spending_minus_6_3pct", "daily_spending_139_2B_won", "Naver_users_plus_23pct", "CJ_volume_plus_120pct"),
        ("customer_trust_breach_hard_4C", "rival_revenue_conversion_missing", "rival_margin_missing", "hypermarket_rule_4B", "fine_finalization_missing"),
        None,
        -34.0,
        {"affected_users_mn": 34, "coupang_return_since_breach_pct": -34, "mobile_mau_change_pct": -3.5, "daily_spending_change_pct": -6.3, "daily_spending_krw_bn": 139.2, "naver_user_change_pct": 23, "cj_logistics_volume_yoy_pct": 120},
        "aligned",
        "hard_4C_success_with_rival_stage2",
        "thesis_break",
        "should_have_been_red",
        "Customer trust break is hard 4C because stock, MAU and spending all deteriorated; rival Stage2 still needs revenue and margin.",
    ),
    Round321CaseCandidate(
        "r13_loop16_hyundai_kia_tariff_redteam",
        "005380/000270",
        "Hyundai Motor / Kia",
        E2RArchetype.TARIFF_RELIEF_THAT_STILL_SELLOFF,
        (E2RArchetype.AUTO_TARIFF_4C_AND_LOCALIZATION_HEDGE, E2RArchetype.US_KOREA_TARIFF_POLICY_4C_WATCH),
        "4c_thesis_break",
        "4C_tariff_relief_that_still_sold_off",
        "T1/T3",
        "4C_tariff_relief_that_still_sold_off",
        "4C-watch + localization hedge watch",
        date(2025, 4, 1),
        None,
        None,
        date(2025, 7, 31),
        date(2025, 7, 31),
        False,
        ("US_imported_auto_tariff_25pct_background", "US_Korea_trade_deal_auto_tariff_15pct", "Hyundai_minus_4_5pct", "Kia_minus_6_6pct", "Hyundai_Group_US_investment_21B_usd", "steel_plant_5_8B_usd", "Georgia_expansion"),
        ("tariff_margin_damage", "KORUS_advantage_loss", "US_plant_utilization_missing", "tariff_savings_uncertain", "policy_or_trade_relief_headline_4C_watch"),
        None,
        -6.6,
        {"trigger_date": "2025-07-31", "tariff_rate_after_deal_pct": 15, "prior_tariff_context_pct": 25, "hyundai_event_return_pct": -4.5, "kia_event_return_pct": -6.6},
        "aligned",
        "tariff_4C_not_relief",
        "thesis_break",
        "should_have_been_red",
        "A tariff relief headline still sold off because the market saw margin damage and lost tariff advantage.",
    ),
    Round321CaseCandidate(
        "r13_loop16_czech_nuclear_legal_gate_cross_redteam",
        "034020/052690/051600/015760",
        "KHNP / Doosan Enerbility / KEPCO E&C / KEPCO Plant S&E",
        E2RArchetype.POLICY_OR_PREFERRED_BIDDER_WITH_LEGAL_4B,
        (E2RArchetype.NUCLEAR_EXPORT_POLICY_STAGE2_WITH_LEGAL_4B, E2RArchetype.NUCLEAR_EXPORT_PREFERRED_BIDDER_STAGE2),
        "event_premium",
        "Stage2_preferred_bidder_with_legal_4B",
        "T0/T2",
        "Stage2_preferred_bidder_with_legal_4B",
        "Stage2 + legal 4B-watch",
        date(2024, 7, 17),
        date(2024, 7, 17),
        None,
        date(2025, 5, 6),
        None,
        False,
        ("KHNP_preferred_bidder_Dukovany", "two_reactors", "project_value_context_18B_usd", "nuclear_basket_rally", "Czech_court_blocks_final_signing_after_EDF_complaint"),
        ("final_contract_missing", "legal_resolution_missing", "workshare_missing", "financing_missing", "margin_missing", "court_blocks_signing_4B"),
        None,
        None,
        {"preferred_bidder_date": "2024-07", "project_value_context_usd_bn": 18, "legal_4b_date": "2025-05-06", "legal_4b_event": "Czech_court_blocks_contract_signing_after_EDF_complaint", "stage3_gate_missing": ["final_contract", "legal_resolution", "workshare", "financing", "margin"]},
        "aligned",
        "preferred_bidder_not_green_legal_4B",
        "policy_event_rerating",
        "stage2_watch_success",
        "Preferred bidder remains Stage2 until final contract, legal clearance, workshare, financing and margin are closed.",
    ),
)

ROUND321_TRIGGER_RECORDS: tuple[Round321TriggerRecord, ...] = (
    Round321TriggerRecord("r13l16_samsung_sds_kkr_T1", "r13_loop16_samsung_sds_kkr_cross_redteam", "Stage2-Actionable", "2026-04-15", "KKR buys $820M Samsung SDS CB; shares +20.8% intraday and +19.4% morning vs KOSPI +3.0%.", 20.8, "excellent_entry_with_CB_4B", "Stage2-Actionable", {"market_relative_pp": 16.4, "cb_value_usd_mn": 820}),
    Round321TriggerRecord("r13l16_samsung_ea_fadhili_T1", "r13_loop16_samsung_ea_fadhili_cross_redteam", "Stage2-Actionable", "2024-04-03", "Samsung E&A wins roughly $6B Fadhili EPC share; shares +8.5% to 26,750 won while KOSPI -1.4%.", 8.5, "excellent_entry_contract_value_margin_gate", "Stage2-Actionable", {"market_relative_pp": 9.9, "event_price_krw": 26750}),
    Round321TriggerRecord("r13l16_hanwha_romania_T1", "r13_loop16_hanwha_export_dilution_cross_redteam", "Stage2-Actionable", "2024-07-09", "Hanwha Aerospace Romania K9/K10 $1B order sends shares +5%+ to record high.", ">5", "good_entry_defense_export", "Stage2-Actionable", {"contract_value_usd_bn": 1.0}),
    Round321TriggerRecord("r13l16_hanwha_dilution_T3", "r13_loop16_hanwha_export_dilution_cross_redteam", "4B_dilution", "2025-03-21", "Large capital raise plan follows defense rerating and shares fall 13%.", -13, "4B_success_dilution", "4B-watch", {"capital_raise_plan_krw_trn": 3.6}),
    Round321TriggerRecord("r13l16_lig_iraq_T0", "r13_loop16_lig_nex1_export_yellow_cross_redteam", "Stage3-Yellow_candidate", "2024-09-20", "LIG Nex1 Iraq M-SAM order 3.71T won / $2.8B; +3.6% vs KOSPI +0.9%; Iraq becomes fourth operator.", 3.6, "good_stage2_to_yellow_candidate", "Stage3-Yellow_candidate", {"market_relative_pp": 2.7, "operator_count_after_iraq": 4}),
    Round321TriggerRecord("r13l16_lg_cns_ipo_T1", "r13_loop16_lg_cns_ipo_false_positive_cross_redteam", "false_positive_price_failed", "2025-02-05", "LG CNS AI/cloud evidence and 1.2T won IPO, but debut trades below 61,900 won issue price at 59,700 won.", "below_issue_price", "evidence_good_but_price_failed", "no_actionable", {"issue_price_krw": 61900, "debut_later_price_krw": 59700}),
    Round321TriggerRecord("r13l16_coupang_breach_T1", "r13_loop16_coupang_security_delivery_cross_redteam", "hard_4C", "2025-11_to_2026-02", "Coupang breach affects 34M users; stock -34%, MAU -3.5%, spending -6.3%; rivals gain users/volume.", -34, "hard_4C_success_customer_trust_break", "4C", {"affected_users_mn": 34, "naver_user_change_pct": 23, "cj_logistics_volume_yoy_pct": 120}),
    Round321TriggerRecord("r13l16_hyundai_kia_tariff_T1", "r13_loop16_hyundai_kia_tariff_redteam", "4C_tariff_margin", "2025-07-31", "U.S.-Korea trade deal lowers tariff to 15%, but Hyundai -4.5% and Kia -6.6%.", "Hyundai_-4.5_Kia_-6.6", "tariff_relief_headline_failed", "4C-watch", {"tariff_rate_after_deal_pct": 15, "hyundai_event_return_pct": -4.5, "kia_event_return_pct": -6.6}),
    Round321TriggerRecord("r13l16_czech_nuclear_legal_T2", "r13_loop16_czech_nuclear_legal_gate_cross_redteam", "4B_legal_gate", "2025-05-06", "Czech court blocks final nuclear signing after EDF complaint; preferred bidder is not Green before legal clearance.", "price_data_unavailable_after_deep_search", "preferred_bidder_legal_4B", "4B-watch", {"project_value_context_usd_bn": 18}),
)

ROUND321_SHADOW_WEIGHT_ROWS: tuple[dict[str, str], ...] = (
    {"archetype": E2RArchetype.CROSS_STAGE2_ACTIONABLE_CONFIRMED.value, "reported_event_return": "+5", "market_relative_return": "+5", "contract_value_visibility": "+4", "strategic_capital_quality": "+4", "delivery_margin_conversion": "+3", "security_trust_break": "+0", "legal_finality": "+1", "tariff_margin_reality": "+1", "theme_label_without_price_validation_penalty": "-2", "ipo_demand_without_post_listing_strength_penalty": "-2", "preferred_bidder_without_contract_penalty": "-2", "growth_with_dilution_ignored_penalty": "-2", "stage2_actionable_promote": "event return and relative return closed", "stage3_yellow_gate": "conversion gate remains", "stage3_green_gate": "margin/revenue/cash conversion", "notes": "Samsung SDS/Samsung E&A."},
    {"archetype": E2RArchetype.GOOD_EVIDENCE_PRICE_FAILED.value, "reported_event_return": "+0", "market_relative_return": "-5", "contract_value_visibility": "+2", "strategic_capital_quality": "+1", "delivery_margin_conversion": "+0", "security_trust_break": "+0", "legal_finality": "+0", "tariff_margin_reality": "+0", "theme_label_without_price_validation_penalty": "-5", "ipo_demand_without_post_listing_strength_penalty": "-5", "preferred_bidder_without_contract_penalty": "-2", "growth_with_dilution_ignored_penalty": "-1", "stage2_actionable_promote": "good evidence but price failed", "stage3_yellow_gate": "no Actionable", "stage3_green_gate": "post-listing strength required", "notes": "LG CNS."},
    {"archetype": E2RArchetype.CONTRACT_VALUE_WITH_MARGIN_GATE.value, "reported_event_return": "+5", "market_relative_return": "+5", "contract_value_visibility": "+5", "strategic_capital_quality": "+0", "delivery_margin_conversion": "+5", "security_trust_break": "+0", "legal_finality": "+1", "tariff_margin_reality": "+0", "theme_label_without_price_validation_penalty": "-2", "ipo_demand_without_post_listing_strength_penalty": "-1", "preferred_bidder_without_contract_penalty": "-1", "growth_with_dilution_ignored_penalty": "-1", "stage2_actionable_promote": "contract value strong", "stage3_yellow_gate": "margin/cash missing", "stage3_green_gate": "margin+cash conversion", "notes": "Samsung E&A."},
    {"archetype": E2RArchetype.GROWTH_WITH_DILUTION_4B.value, "reported_event_return": "+4", "market_relative_return": "+2", "contract_value_visibility": "+5", "strategic_capital_quality": "+0", "delivery_margin_conversion": "+4", "security_trust_break": "+0", "legal_finality": "+1", "tariff_margin_reality": "+0", "theme_label_without_price_validation_penalty": "-1", "ipo_demand_without_post_listing_strength_penalty": "-1", "preferred_bidder_without_contract_penalty": "-1", "growth_with_dilution_ignored_penalty": "-5", "stage2_actionable_promote": "growth order strong", "stage3_yellow_gate": "dilution overlay", "stage3_green_gate": "delivery+margin+dilution absorption", "notes": "Hanwha."},
    {"archetype": E2RArchetype.EXPORT_ORDER_TO_COMBAT_VALIDATION_YELLOW.value, "reported_event_return": "+4", "market_relative_return": "+3", "contract_value_visibility": "+5", "strategic_capital_quality": "+0", "delivery_margin_conversion": "+5", "security_trust_break": "+0", "legal_finality": "+1", "tariff_margin_reality": "+0", "theme_label_without_price_validation_penalty": "-1", "ipo_demand_without_post_listing_strength_penalty": "-1", "preferred_bidder_without_contract_penalty": "-1", "growth_with_dilution_ignored_penalty": "-1", "stage2_actionable_promote": "export order plus validation", "stage3_yellow_gate": "production/margin missing", "stage3_green_gate": "repeat orders+delivery+margin", "notes": "LIG Nex1."},
    {"archetype": E2RArchetype.POLICY_OR_PREFERRED_BIDDER_WITH_LEGAL_4B.value, "reported_event_return": "+2", "market_relative_return": "+1", "contract_value_visibility": "+3", "strategic_capital_quality": "+0", "delivery_margin_conversion": "+2", "security_trust_break": "+0", "legal_finality": "+5", "tariff_margin_reality": "+0", "theme_label_without_price_validation_penalty": "-2", "ipo_demand_without_post_listing_strength_penalty": "-1", "preferred_bidder_without_contract_penalty": "-5", "growth_with_dilution_ignored_penalty": "-1", "stage2_actionable_promote": "preferred bidder/policy stage2", "stage3_yellow_gate": "legal finality missing", "stage3_green_gate": "final contract+legal resolution", "notes": "Czech nuclear."},
    {"archetype": E2RArchetype.SECURITY_TRUST_BREAK_HARD_4C.value, "reported_event_return": "+0", "market_relative_return": "+0", "contract_value_visibility": "+0", "strategic_capital_quality": "+0", "delivery_margin_conversion": "+0", "security_trust_break": "+5", "legal_finality": "+0", "tariff_margin_reality": "+0", "theme_label_without_price_validation_penalty": "-1", "ipo_demand_without_post_listing_strength_penalty": "-1", "preferred_bidder_without_contract_penalty": "-1", "growth_with_dilution_ignored_penalty": "-1", "stage2_actionable_promote": "data breach with user/spending decline", "stage3_yellow_gate": "hard 4C", "stage3_green_gate": "N/A", "notes": "Coupang."},
    {"archetype": E2RArchetype.TARIFF_RELIEF_THAT_STILL_SELLOFF.value, "reported_event_return": "+0", "market_relative_return": "-5", "contract_value_visibility": "+0", "strategic_capital_quality": "+0", "delivery_margin_conversion": "+3", "security_trust_break": "+0", "legal_finality": "+1", "tariff_margin_reality": "+5", "theme_label_without_price_validation_penalty": "-1", "ipo_demand_without_post_listing_strength_penalty": "-1", "preferred_bidder_without_contract_penalty": "-1", "growth_with_dilution_ignored_penalty": "-1", "stage2_actionable_promote": "relief headline sold off", "stage3_yellow_gate": "margin reality first", "stage3_green_gate": "tariff savings+localization margin", "notes": "Hyundai/Kia."},
)


def round321_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND321_CASE_CANDIDATES]


def round321_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND321_CASE_CANDIDATES]


def round321_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND321_TRIGGER_RECORDS]


def round321_shadow_weight_rows() -> list[dict[str, str]]:
    return [dict(row) for row in ROUND321_SHADOW_WEIGHT_ROWS]


def round321_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND321_REQUIRED_TARGET_ALIASES.items()]


def round321_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND321_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND321_SCORE_DOWN_AXES]
    )


def round321_summary() -> dict[str, object]:
    return {
        "source_round": ROUND321_SOURCE_ROUND_PATH,
        "round_id": ROUND321_ANALYST_ROUND_ID,
        "large_sector": ROUND321_LARGE_SECTOR,
        "method": ROUND321_METHOD,
        "case_candidate_count": len(ROUND321_CASE_CANDIDATES),
        "trigger_count": len(ROUND321_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND321_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 3,
        "stage2_candidate_count": 5,
        "stage3_yellow_candidate_count": 5,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 6,
        "stage4c_watch_count": 4,
        "hard_4c_case_count": 1,
        "evidence_good_but_price_failed_or_unavailable_count": 5,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R1 Loop 17",
    }


def round321_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND321_SOURCE_ROUND_PATH,
        "round_id": ROUND321_ANALYST_ROUND_ID,
        "large_sector": ROUND321_LARGE_SECTOR,
        "method": ROUND321_METHOD,
        "summary": round321_summary(),
        "required_target_aliases": dict(ROUND321_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND321_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND321_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND321_STAGE3_GREEN_RULES,
        "green_blockers": ROUND321_GREEN_BLOCKERS,
        "score_up_axes": ROUND321_SCORE_UP_AXES,
        "score_down_axes": ROUND321_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND321_STAGE4B_WATCH_TRIGGERS,
        "hard_4c_gates": ROUND321_HARD_4C_GATES,
        "row_separation_rules": ROUND321_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round321_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_news_size_as_entry_quality_without_price_conversion_dilution_legal_margin_trust_or_tariff_gates",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round321_summary_markdown() -> str:
    summary = round321_summary()
    lines = [
        "# R13 Loop 16 Cross-Archetype RedTeam / 4B / 4C / Price Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: LG CNS had credible AI/cloud evidence, but below-issue-price trading means the system must not promote it to Actionable or Green.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Samsung SDS / KKR and Samsung E&A / Fadhili are clean Stage2-Actionable anchors, but both retain conversion gates.",
            "- Hanwha Aerospace confirms growth success can still carry dilution 4B.",
            "- LIG Nex1 is a Stage3-Yellow candidate pattern, not Green before production, delivery and margin.",
            "- LG CNS is evidence-good but price-failed.",
            "- Coupang breach is hard 4C because stock, MAU and spending all deteriorated.",
            "- Hyundai/Kia tariff shows relief headlines can still be margin-damage 4C-watch.",
            "- Czech nuclear proves preferred bidder is not final contract.",
            "- Stage3-Green confirmed: `0`.",
            "- Hard 4C confirmed: `1`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round321_trigger_grid_markdown() -> str:
    lines = [
        "# Round 321 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round321_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round321_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 321 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND321_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND321_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND321_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND321_GREEN_BLOCKERS),
            "",
            "## Hard 4C Gates",
            *_bullet_lines(ROUND321_HARD_4C_GATES),
        ]
    ) + "\n"


def render_round321_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 321 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND321_STAGE4B_WATCH_TRIGGERS),
        "",
        "## Hard 4C Gates",
        *_bullet_lines(ROUND321_HARD_4C_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND321_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round321_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 321 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event returns and event prices are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND321_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round321_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 321 Row Separation Plan",
        "",
        "Cross-archetype RedTeam rows must separate case evidence, trigger anchors and full adjusted OHLC backfill.",
        "",
        "Easy example: a preferred-bidder headline can be Stage2, but the OHLC backtest row and final-contract/legal-clearance row must stay separate.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND321_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round321_r13_loop16_reports(
    output_directory: str | Path = ROUND321_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND321_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND321_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND321_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND321_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round321_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND321_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round321_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round321_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round321_r13_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round321_r13_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round321_r13_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round321_r13_loop16_trigger_grid.md",
        "summary": output_dir / "round321_r13_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round321_r13_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round321_r13_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round321_r13_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round321_r13_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round321_r13_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round321_r13_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round321_case_rows())
    _write_csv(paths["target_aliases"], round321_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round321_trigger_rows())
    _write_csv(paths["score_adjustments"], round321_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round321_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round321_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round321_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round321_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round321_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round321_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round321_row_separation_plan_markdown(), encoding="utf-8")
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


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _value_text(value: object) -> str:
    if value is None:
        return ""
    return str(value)


def _bullet_lines(items: Iterable[str]) -> list[str]:
    return [f"- {item}" for item in items]


__all__ = [
    "ROUND321_CASE_CANDIDATES",
    "ROUND321_GREEN_BLOCKERS",
    "ROUND321_HARD_4C_GATES",
    "ROUND321_LARGE_SECTOR",
    "ROUND321_REQUIRED_TARGET_ALIASES",
    "ROUND321_ROW_SEPARATION_RULES",
    "ROUND321_SCORE_DOWN_AXES",
    "ROUND321_SCORE_UP_AXES",
    "ROUND321_SHADOW_WEIGHT_ROWS",
    "ROUND321_STAGE2_ACTIONABLE_RULES",
    "ROUND321_STAGE3_GREEN_RULES",
    "ROUND321_STAGE3_YELLOW_RULES",
    "ROUND321_STAGE4B_WATCH_TRIGGERS",
    "ROUND321_TRIGGER_RECORDS",
    "render_round321_stage4b_4c_review_markdown",
    "render_round321_stage_rules_markdown",
    "render_round321_trigger_grid_markdown",
    "round321_audit_payload",
    "round321_case_records",
    "round321_case_rows",
    "round321_shadow_weight_rows",
    "round321_summary",
    "round321_trigger_rows",
    "write_round321_r13_loop16_reports",
]
