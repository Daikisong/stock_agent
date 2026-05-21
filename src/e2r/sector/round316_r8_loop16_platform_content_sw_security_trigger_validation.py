"""Round-316 R8 Loop-16 platform, content, software and security validation.

This module converts ``docs/round/round_316.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: an AI data-center announcement can move Kakao or LG CNS on the
event date. It is still Stage2 until cloud/SI backlog, recurring revenue,
utilization and margin are visible as of the replay date.
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


ROUND316_SOURCE_ROUND_PATH = "docs/round/round_316.md"
ROUND316_ANALYST_ROUND_ID = "round_244"
ROUND316_LARGE_SECTOR = "PLATFORM_CONTENT_SW_SECURITY"
ROUND316_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND316_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round316_r8_loop16_platform_content_sw_security_trigger_validation"
ROUND316_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r8_loop16_round244.jsonl"
ROUND316_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r8_loop16_round244.jsonl"
ROUND316_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round316_r8_loop16_platform_content_sw_security_trigger_validation_audit.json"
ROUND316_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round244_r8_loop16_v1.csv"

ROUND316_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE": E2RArchetype.AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE.value,
    "AI_CLOUD_IPO_PRICE_MUTED": E2RArchetype.AI_CLOUD_IPO_PRICE_MUTED.value,
    "WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE": E2RArchetype.WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE.value,
    "GAME_IP_GLOBAL_EXPANSION_STAGE2": E2RArchetype.GAME_IP_GLOBAL_EXPANSION_STAGE2.value,
    "GAME_IP_IPO_STAGE2_WITH_CONCENTRATION_4B": E2RArchetype.GAME_IP_IPO_STAGE2_WITH_CONCENTRATION_4B.value,
    "CONTENT_LABEL_GOVERNANCE_4C_WATCH": E2RArchetype.CONTENT_LABEL_GOVERNANCE_4C_WATCH.value,
    "PLATFORM_FOUNDER_REGULATORY_4C_RELIEF": E2RArchetype.PLATFORM_FOUNDER_REGULATORY_4C_RELIEF.value,
    "CYBERSECURITY_DATA_BREACH_HARD_4C": E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C.value,
}

ROUND316_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_at_least_5pct_or_market_relative_return_at_least_5pp",
    "AI_cloud_or_data_center_trigger_links_to_cloud_SI_backlog_or_recurring_revenue",
    "content_platform_has_two_of_MAU_revenue_profit_or_IP_licensing",
    "game_company_has_two_of_hit_sales_retention_live_service_or_pipeline",
    "platform_expansion_has_ARPU_GMV_ROI_or_regulatory_stability",
    "governance_founder_legal_or_cybersecurity_4B_4C_overlay_is_not_dominant_for_positive_candidate",
)

ROUND316_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_Actionable_conditions_pass",
    "EPS_OP_FCF_path_can_change_materially",
    "one_of_monetization_margin_retention_legal_or_security_gate_remains_open",
    "reported_price_anchor_supports_trigger_but_full_adjusted_OHLC_is_missing",
    "case_is_not_pure_AI_infra_IPO_MAU_game_hit_artist_IP_or_founder_relief_headline",
)

ROUND316_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "AI_infrastructure_converts_to_recurring_cloud_SI_revenue",
    "MAU_converts_to_ARPU_paid_conversion_ad_revenue_and_profit",
    "IP_licensing_converts_to_durable_revenue_and_margin",
    "game_hit_converts_to_repeat_sales_live_service_retention_and_sequel_pipeline",
    "governance_founder_and_label_legal_overhangs_are_resolved",
    "cybersecurity_remediation_is_complete_and_revenue_guidance_recovers",
    "full_adjusted_OHLC_MFE_MAE_window_supports_stage_candidate",
)

ROUND316_GREEN_BLOCKERS: tuple[str, ...] = (
    "AI_infra_headline_without_revenue",
    "IPO_valuation_without_post_listing_strength",
    "MAU_without_ARPU_profit",
    "game_hit_without_pipeline",
    "geographic_fund_without_ROI",
    "artist_IP_without_governance",
    "platform_founder_risk_ignored",
    "security_incident_treated_as_one_off",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND316_SCORE_UP_AXES: tuple[str, ...] = (
    "AI_compute_to_cloud_revenue",
    "SI_contract_backlog",
    "IP_platform_MAU_monetization",
    "content_IP_license_revenue",
    "game_IP_repeat_sales",
    "India_platform_monetization",
    "label_governance_stability",
    "founder_regulatory_clearance",
    "cybersecurity_trust_cost",
)

ROUND316_SCORE_DOWN_AXES: tuple[str, ...] = (
    "AI_infra_headline_without_revenue",
    "IPO_valuation_without_post_listing_strength",
    "MAU_without_ARPU_profit",
    "game_hit_without_pipeline",
    "geographic_fund_without_ROI",
    "artist_IP_without_governance",
    "platform_founder_risk_ignored",
    "security_incident_treated_as_one_off",
)

ROUND316_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "AI_infra_headline_rallies_before_cloud_SI_revenue",
    "IPO_prices_high_but_trades_below_issue_price",
    "content_platform_rallies_on_IP_deal_after_large_drawdown",
    "game_IPO_rallies_on_one_or_two_hit_titles_before_repeatability",
    "Kpop_content_IP_faces_label_or_founder_governance_dispute",
    "platform_founder_faces_regulatory_or_legal_investigation",
    "security_breach_creates_compensation_and_revenue_guidance_tail_risk",
)

ROUND316_4C_WATCH_GATES: tuple[str, ...] = (
    "large_scale_customer_data_breach",
    "regulatory_fine_or_compensation_changes_revenue_guidance",
    "platform_founder_arrest_or_capital_market_law_investigation",
    "content_label_control_dispute_disrupts_artist_IP",
    "cyber_incident_with_user_churn_and_remediation_cost",
    "IPO_below_issue_price_with_no_follow_through_demand",
    "game_pipeline_cancellation_after_one_title_concentration",
)

ROUND316_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_event_anchor_AI_infra_IPO_MAU_IP_deal_game_governance_or_cybersecurity_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing",
    "do_not_treat_AI_infra_IPO_MAU_game_hit_artist_IP_founder_relief_or_security_headline_as_Green_without_recurring_revenue_ARPU_profit_repeat_sales_governance_clearance_or_trust_recovery",
)


@dataclass(frozen=True)
class Round316ShadowWeightRow:
    archetype: E2RArchetype
    ai_compute_to_cloud_revenue: int
    si_contract_backlog: int
    ip_platform_mau_monetization: int
    content_ip_license_revenue: int
    game_ip_repeat_sales: int
    india_platform_monetization: int
    label_governance_stability: int
    founder_regulatory_clearance: int
    cybersecurity_trust_cost: int
    ai_infra_headline_without_revenue_penalty: int
    ipo_valuation_without_post_listing_strength_penalty: int
    mau_without_arpu_profit_penalty: int
    game_hit_without_pipeline_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "AI_compute_to_cloud_revenue": _signed(self.ai_compute_to_cloud_revenue),
            "SI_contract_backlog": _signed(self.si_contract_backlog),
            "IP_platform_MAU_monetization": _signed(self.ip_platform_mau_monetization),
            "content_IP_license_revenue": _signed(self.content_ip_license_revenue),
            "game_IP_repeat_sales": _signed(self.game_ip_repeat_sales),
            "India_platform_monetization": _signed(self.india_platform_monetization),
            "label_governance_stability": _signed(self.label_governance_stability),
            "founder_regulatory_clearance": _signed(self.founder_regulatory_clearance),
            "cybersecurity_trust_cost": _signed(self.cybersecurity_trust_cost),
            "AI_infra_headline_without_revenue_penalty": _signed(self.ai_infra_headline_without_revenue_penalty),
            "IPO_valuation_without_post_listing_strength_penalty": _signed(self.ipo_valuation_without_post_listing_strength_penalty),
            "MAU_without_ARPU_profit_penalty": _signed(self.mau_without_arpu_profit_penalty),
            "game_hit_without_pipeline_penalty": _signed(self.game_hit_without_pipeline_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round316TriggerRecord:
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
class Round316CaseCandidate:
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
            "do_not_use_round316_cases_as_candidate_generation_input",
            "do_not_treat_AI_infra_IPO_MAU_game_hit_artist_IP_founder_relief_or_security_headline_as_Green_without_recurring_revenue_ARPU_profit_repeat_sales_governance_clearance_or_trust_recovery",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND316_LARGE_SECTOR,
            large_sector=ROUND316_LARGE_SECTOR,
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
            stage4b_evidence=tuple(field for field in self.red_flag_fields if "4B" in field or "4b" in field or "drawdown" in field or "concentration" in field or "governance" in field),
            stage4c_evidence=tuple(
                field
                for field in (*self.red_flag_fields, *self.evidence_fields)
                if "4C" in field
                or "4c" in field
                or "breach" in field
                or "fine" in field
                or "compensation" in field
                or "founder" in field
                or "governance" in field
                or "legal" in field
            ),
            must_have_fields=ROUND316_STAGE3_GREEN_RULES,
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
                stage_dates_confidence=0.82,
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


ROUND316_CASE_CANDIDATES: tuple[Round316CaseCandidate, ...] = (
    Round316CaseCandidate(
        "r8_loop16_kakao_lgcns_sk_aws_ai_datacenter",
        "035720/064400/SK_group_readthrough",
        "Kakao / LG CNS / SK-AWS AI data center read-through",
        E2RArchetype.AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE,
        (E2RArchetype.AI_INFRA_PORTAL_STAGE2_ACTIONABLE, E2RArchetype.CLOUD_AI_SOFTWARE_INFRA),
        "success_candidate",
        "Stage2_Actionable_AI_infrastructure",
        "r8l16_kakao_lgcns_ai_dc_T1",
        "Stage2-Actionable_AI_infra",
        "Stage2-Actionable",
        date(2025, 6, 20),
        date(2025, 6, 20),
        None,
        date(2025, 6, 20),
        None,
        False,
        ("SK_AWS_Ulsan_AI_data_center_krw_7tn", "AWS_contribution_usd_4bn", "100MW_full_operation_2029", "Kakao_plus_11pct", "LG_CNS_plus_9pct"),
        ("cloud_contract_backlog_missing", "LG_CNS_SI_margin_missing", "Kakao_AI_service_monetization_missing", "data_center_utilization_missing", "AI_infra_headline_without_revenue_4B"),
        11.0,
        None,
        None,
        None,
        None,
        None,
        {"trigger_date": "2025-06-20", "investment_krw_trn": 7.0, "investment_usd_bn": 5.11, "aws_contribution_usd_bn": 4.0, "initial_capacity_mw": 100, "full_operation_year": 2029, "future_capacity_target_gw": 1.0, "kakao_event_return_pct": 11, "lg_cns_event_return_pct": 9, "sk_hynix_event_return_pct": 3},
        "aligned",
        "excellent_stage2_actionable_AI_infrastructure",
        "policy_event_rerating",
        "stage2_watch_success",
        "AI infrastructure trigger was price-aligned, but cloud/SI backlog and recurring revenue are Green gates.",
    ),
    Round316CaseCandidate(
        "r8_loop16_lg_cns_ipo_ai_cloud_price_muted",
        "064400",
        "LG CNS",
        E2RArchetype.AI_CLOUD_IPO_PRICE_MUTED,
        (E2RArchetype.CLOUD_AI_IT_SERVICES_EVIDENCE_GOOD_PRICE_FAILED, E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE),
        "failed_rerating",
        "evidence_good_but_price_failed",
        "r8l16_lgcns_ipo_T1",
        "Stage2_AI_cloud_but_price_failed",
        "Stage2 but not Actionable",
        date(2025, 2, 5),
        date(2025, 2, 5),
        None,
        date(2025, 2, 5),
        None,
        False,
        ("IPO_raise_krw_1_2tn", "IPO_raise_usd_827_1mn", "AI_cloud_services_over_half_sales", "issue_price_61900", "debut_later_price_59700"),
        ("IPO_debut_below_issue_price", "external_AI_cloud_contract_growth_missing", "cloud_margin_missing", "post_IPO_multiple_absorption_missing", "evidence_good_but_price_failed_4B"),
        None,
        -3.55,
        None,
        61900,
        59700,
        None,
        {"trigger_date": "2025-02-05", "ipo_raise_krw_trn": 1.2, "ipo_raise_usd_mn": 827.1, "issue_price_krw": 61900, "debut_open_krw": 60500, "debut_later_price_krw": 59700, "ai_cloud_sales_share_context": ">50%_of_first_three_quarters_2024_sales"},
        "evidence_good_but_price_failed",
        "evidence_good_but_price_failed",
        "no_rerating",
        "stage2_watch_success",
        "AI/cloud exposure was real, but the IPO traded below issue price; no Actionable promotion.",
    ),
    Round316CaseCandidate(
        "r8_loop16_webtoon_naver_ip_monetization",
        "WBTN/035420_readthrough",
        "Webtoon Entertainment / Naver",
        E2RArchetype.WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE,
        (E2RArchetype.WEBTOON_IPO_CONTENT_PLATFORM_STAGE2, E2RArchetype.WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE),
        "success_candidate",
        "Stage2_Actionable_content_platform_with_4B_volatility",
        "r8l16_webtoon_disney_T2",
        "Stage2-Actionable_IP_platform",
        "Stage2-Actionable to Yellow candidate",
        date(2024, 5, 31),
        date(2024, 6, 27),
        date(2025, 8, 13),
        date(2025, 8, 13),
        None,
        False,
        ("170M_MAU", "150_plus_countries", "IPO_price_usd_21", "debut_close_usd_23", "Disney_deal_surprise_profit_plus_62pct"),
        ("pre_Disney_post_IPO_decline_minus_55pct", "paid_conversion_missing", "ad_ARPU_missing", "creator_payout_ratio_missing", "Naver_parent_value_capture_missing"),
        62.0,
        None,
        21.0,
        23.0,
        15.16,
        None,
        {"ipo_filing_date": "2024-05-31", "ipo_pricing_date": "2024-06-27", "ipo_price_usd": 21, "ipo_valuation_usd_bn": 2.7, "ipo_raise_usd_mn": 315, "debut_close_usd": 23.0, "debut_return_pct": 9.5, "monthly_active_users_mn": 170, "countries": ">150", "q1_2024_revenue_usd_mn": 326.7, "q1_2024_net_income_usd_mn": 6.2, "disney_earnings_event_return_pct": 62, "disney_event_price_usd": 15.16, "pre_disney_post_ipo_decline_pct": -55},
        "aligned",
        "Stage2_Actionable_content_platform_with_4B_volatility",
        "unknown",
        "yellow_success",
        "IPO and Disney/earnings triggers were strong, but prior drawdown and sustained profitability remain gates.",
    ),
    Round316CaseCandidate(
        "r8_loop16_krafton_naver_mirae_india_fund",
        "259960/035420/006800",
        "Krafton / Naver / Mirae Asset",
        E2RArchetype.GAME_IP_GLOBAL_EXPANSION_STAGE2,
        (E2RArchetype.GAME_IP_PLATFORM_EXPANSION, E2RArchetype.EMERGING_MARKET_GAME_PLATFORM_OPTION),
        "success_candidate",
        "Stage2_platform_game_geographic_expansion",
        "r8l16_krafton_india_T1",
        "Stage2_geographic_expansion",
        "Stage2",
        date(2025, 12, 19),
        date(2025, 12, 19),
        None,
        date(2025, 12, 19),
        None,
        False,
        ("India_tech_fund_usd_666mn", "initial_capital_usd_333mn", "Krafton_India_investment_over_usd_200mn", "BGMI_downloads_over_240mn"),
        ("direct_price_anchor_missing", "India_game_revenue_missing", "BGMI_ARPU_missing", "startup_fund_IRR_missing", "regulatory_stability_missing"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"trigger_date": "2025-12-19", "fund_total_usd_mn": 666, "initial_capital_usd_mn": 333, "fund_launch": "2026-01", "krafton_existing_india_investment_usd_mn": ">200", "bgmi_downloads_mn": ">240"},
        "unknown",
        "Stage2_geographic_expansion_not_Green",
        "unknown",
        "stage2_watch_success",
        "India platform expansion is strategic, but monetization and fund ROI are not verified.",
    ),
    Round316CaseCandidate(
        "r8_loop16_shiftup_game_ip_ipo",
        "ShiftUp_KOSPI",
        "Shift Up",
        E2RArchetype.GAME_IP_IPO_STAGE2_WITH_CONCENTRATION_4B,
        (E2RArchetype.GAME_IP_MONETIZATION_IPO_STAGE2, E2RArchetype.GAME_IP_IPO_SINGLE_TITLE_RISK),
        "success_candidate",
        "Stage2_game_IP_with_4B_concentration",
        "r8l16_shiftup_ipo_T0",
        "Stage2_game_IP",
        "Stage2 + 4B-watch",
        date(2024, 6, 27),
        date(2024, 6, 27),
        None,
        date(2024, 6, 27),
        None,
        False,
        ("IPO_raise_krw_435bn", "expected_market_cap_krw_3_5tn", "Nikke_sales_krw_255bn", "Stellar_Blade_Japan_rank_1", "OP_2023_krw_111bn"),
        ("direct_post_listing_price_anchor_missing", "Stellar_Blade_repeat_sales_missing", "Nikke_live_service_retention_missing", "project_pipeline_missing", "title_concentration_4B"),
        None,
        None,
        None,
        None,
        None,
        None,
        {"trigger_date": "2024-06-27", "ipo_raise_krw_bn": 435, "ipo_raise_usd_mn": 313, "expected_market_cap_krw_trn": 3.5, "expected_market_cap_usd_bn": 2.52, "nikke_sales_launch_to_q1_2024_krw_bn": 255, "stellar_blade_japan_ps_download_rank": 1, "stellar_blade_north_america_ps_download_rank": 2, "op_2023_krw_bn": 111, "revenue_2023_krw_bn": 169, "op_2022_krw_bn": 18},
        "unknown",
        "Stage2_game_IP_not_Green",
        "unknown",
        "stage2_watch_success",
        "Game IP evidence is strong, but post-listing price path, repeat sales and title concentration are gates.",
    ),
    Round316CaseCandidate(
        "r8_loop16_hybe_content_label_governance",
        "352820",
        "HYBE",
        E2RArchetype.CONTENT_LABEL_GOVERNANCE_4C_WATCH,
        (E2RArchetype.KPOP_IP_GOVERNANCE_4C_WATCH, E2RArchetype.ENTERTAINMENT_GOVERNANCE_LEGAL_OVERLAY),
        "4b_watch",
        "4C_watch_content_governance",
        "r8l16_hybe_ador_T0",
        "4C-watch_content_governance",
        "4C-watch",
        date(2024, 4, 24),
        None,
        None,
        date(2024, 4, 24),
        date(2024, 4, 24),
        False,
        ("ADOR_NewJeans_label_control_dispute", "HYBE_shares_nearly_minus_8pct", "Bang_detention_warrant_request", "HYBE_minus_2_4pct_despite_market_uptick"),
        ("artist_activity_normalization_missing", "legal_resolution_missing", "label_governance_stability_missing", "founder_risk_resolution_missing", "content_IP_governance_4C_watch"),
        None,
        -8.0,
        None,
        None,
        None,
        None,
        {"ador_dispute_date": "2024-04-24", "ador_dispute_event_return_pct": "nearly_-8", "bang_warrant_date": "2026-04-21", "bang_warrant_event_return_pct": -2.4},
        "aligned",
        "content_IP_governance_4C_watch",
        "thesis_break",
        "should_have_been_red",
        "Artist IP value is offset by label governance and founder legal overhang.",
    ),
    Round316CaseCandidate(
        "r8_loop16_kakao_founder_regulatory_relief",
        "035720",
        "Kakao",
        E2RArchetype.PLATFORM_FOUNDER_REGULATORY_4C_RELIEF,
        (E2RArchetype.KAKAO_PLATFORM_GOVERNANCE_4C_WATCH, E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_4C_WATCH),
        "4b_watch",
        "4C_watch_with_relief",
        "r8l16_kakao_founder_T0",
        "4C-watch_founder_regulatory",
        "4C-watch to relief",
        date(2024, 7, 22),
        None,
        None,
        date(2024, 7, 22),
        date(2024, 7, 22),
        False,
        ("Kim_Beom_su_arrest", "SM_Entertainment_stock_manipulation_suspicion", "Kakao_minus_3_4pct", "court_acquittal_relief_2025_10_21"),
        ("AI_investment_delay_risk", "global_expansion_delay_risk", "KakaoBank_control_rule_risk", "direct_relief_price_anchor_missing", "platform_founder_regulatory_4C_watch"),
        None,
        -3.4,
        None,
        None,
        None,
        None,
        {"arrest_date": "2024-07-22/2024-07-23", "arrest_event_return_pct": -3.4, "charge_context": "SM_Entertainment_stock_manipulation_suspicion", "relief_date": "2025-10-21", "relief_event": "court_clears_Kim_Beom_su_of_stock_manipulation_charges"},
        "aligned",
        "platform_founder_regulatory_4C_with_relief",
        "credit_relief_rally",
        "should_have_been_red",
        "Founder regulatory overhang hit shares; acquittal is relief but business normalization remains necessary.",
    ),
    Round316CaseCandidate(
        "r8_loop16_sk_telecom_cyber_breach",
        "017670",
        "SK Telecom",
        E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C,
        (E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C, E2RArchetype.SECURITY_OPERATIONAL_TRUST_HARD_4C),
        "4c_thesis_break",
        "hard_4C_cybersecurity",
        "r8l16_skt_breach_T0",
        "hard_4C_cybersecurity",
        "4C",
        date(2025, 4, 28),
        None,
        None,
        None,
        date(2025, 4, 28),
        True,
        ("malware_customer_data_breach", "23M_users_free_USIM_replacement", "26_96M_data_pieces_leaked", "134B_won_fine", "800B_won_revenue_forecast_cut"),
        ("security_investment_5y_krw_700bn", "possible_compensation_krw_2_3tn", "customer_churn_stabilization_missing", "revenue_guidance_recovery_missing", "cybersecurity_hard_4C"),
        None,
        -8.5,
        None,
        None,
        None,
        None,
        {"breach_price_event_date": "2025-04-28", "intraday_event_return_pct": -8.5, "close_event_return_pct": -6.7, "kospi_same_context_pct": 0.1, "affected_subscribers_mn": 23, "user_data_pieces_leaked_mn": 26.96, "july_probe_event_return_pct": -5.6, "security_investment_5y_krw_bn": 700, "revenue_forecast_cut_krw_bn": 800, "fine_krw_bn": 134, "possible_all_victim_compensation_krw_trn": 2.3},
        "aligned",
        "hard_4C_success_cybersecurity",
        "thesis_break",
        "should_have_been_red",
        "Cyber breach triggered price collapse, fine, remediation cost, revenue guidance cut and compensation tail risk.",
    ),
)


ROUND316_TRIGGER_RECORDS: tuple[Round316TriggerRecord, ...] = (
    Round316TriggerRecord("r8l16_kakao_lgcns_ai_dc_T1", "r8_loop16_kakao_lgcns_sk_aws_ai_datacenter", "Stage2-Actionable_AI_infra", "2025-06-20", "SK Group and AWS announce 7T won / $5.11B Ulsan AI data center; Kakao +11%, LG CNS +9%, SK Hynix +3%, KOSPI above 3,000.", "Kakao +11 / LG CNS +9", "excellent_stage2_actionable_AI_infrastructure", "Stage2-Actionable", {"investment_krw_trn": 7.0, "aws_contribution_usd_bn": 4.0}),
    Round316TriggerRecord("r8l16_lgcns_ipo_T1", "r8_loop16_lg_cns_ipo_ai_cloud_price_muted", "evidence_good_but_price_failed", "2025-02-05", "LG CNS IPO raised 1.2T won / $827M; cloud and AI services over half of sales, but shares traded at 59,700 won below 61,900 won issue price.", "below_issue_price", "evidence_good_but_price_failed", "Stage2_only", {"issue_price_krw": 61900, "debut_later_price_krw": 59700}),
    Round316TriggerRecord("r8l16_webtoon_ipo_T1", "r8_loop16_webtoon_naver_ip_monetization", "Stage2-Actionable_IP_platform", "2024-06-27/2024-06-28", "Webtoon IPO priced at $21, valuation $2.7B, raised $315M, debut close $23.00; 170M MAU and 150+ countries.", 9.5, "Stage2_Actionable_content_platform", "Stage2-Actionable", {"monthly_active_users_mn": 170}),
    Round316TriggerRecord("r8l16_webtoon_disney_T2", "r8_loop16_webtoon_naver_ip_monetization", "Stage2_validation_Yellow_candidate", "2025-08-13", "Webtoon shares +62% to $15.16 after Disney IP deal and surprise profit, after prior 55% post-IPO decline.", 62, "IP_monetization_validation_with_4B_volatility", "Stage2-Actionable_to_Yellow_candidate", {"pre_disney_post_ipo_decline_pct": -55}),
    Round316TriggerRecord("r8l16_krafton_india_T1", "r8_loop16_krafton_naver_mirae_india_fund", "Stage2_geographic_expansion", "2025-12-19", "Krafton, Naver and Mirae Asset launch $666M India tech fund; initial $333M; Krafton invested over $200M in India and BGMI has over 240M downloads.", "price_data_unavailable_after_deep_search", "Stage2_geographic_expansion_not_Green", "Stage2", {"fund_total_usd_mn": 666, "bgmi_downloads_mn": ">240"}),
    Round316TriggerRecord("r8l16_shiftup_ipo_T0", "r8_loop16_shiftup_game_ip_ipo", "Stage2_game_IP", "2024-06-27", "Shift Up IPO expected to raise 435B won / $313M; Nikke 255B won sales; Stellar Blade top PS download rankings; 2023 OP 111B won.", "price_data_unavailable_after_deep_search", "Stage2_game_IP_with_concentration_4B", "Stage2+4B", {"op_2023_krw_bn": 111}),
    Round316TriggerRecord("r8l16_hybe_ador_T0", "r8_loop16_hybe_content_label_governance", "4C-watch_content_governance", "2024-04-24", "HYBE audits ADOR amid Min Hee-jin/NewJeans label dispute; shares fall nearly 8%.", "nearly_-8", "content_label_governance_4C_watch", "4C-watch", {"ador_dispute_event_return_pct": "nearly_-8"}),
    Round316TriggerRecord("r8l16_hybe_bang_T2", "r8_loop16_hybe_content_label_governance", "4C-watch_founder_legal", "2026-04-21", "Police seek detention warrant for Bang Si-hyuk over alleged capital-market law violation; HYBE shares -2.4% despite market uptick.", -2.4, "founder_governance_4C_watch", "4C-watch", {"bang_warrant_event_return_pct": -2.4}),
    Round316TriggerRecord("r8l16_kakao_founder_T0", "r8_loop16_kakao_founder_regulatory_relief", "4C-watch_founder_regulatory", "2024-07-22/2024-07-23", "Kakao founder Kim Beom-su arrested over suspected SM Entertainment stock manipulation; Kakao shares -3.4%.", -3.4, "platform_founder_regulatory_4C_watch", "4C-watch", {"arrest_event_return_pct": -3.4}),
    Round316TriggerRecord("r8l16_skt_breach_T0", "r8_loop16_sk_telecom_cyber_breach", "hard_4C_cybersecurity", "2025-04-28", "SK Telecom discloses customer data leak from malware; shares as much as -8.5%, close -6.7%, KOSPI +0.1%; free USIM replacement for 23M users.", -6.7, "hard_4C_success_cybersecurity", "4C", {"affected_subscribers_mn": 23}),
    Round316TriggerRecord("r8l16_skt_breach_penalty_T2", "r8_loop16_sk_telecom_cyber_breach", "4C_validation_penalty", "2025-07-04/2025-08-28/2025-12-21", "Probe confirms 26.96M data pieces leaked, shares -5.6%, 700B won security investment, 800B won revenue forecast cut, 134B won fine, possible compensation near 2.3T won.", -5.6, "cybersecurity_4C_validation", "4C", {"fine_krw_bn": 134, "possible_all_victim_compensation_krw_trn": 2.3}),
)


ROUND316_SHADOW_WEIGHT_ROWS: tuple[Round316ShadowWeightRow, ...] = (
    Round316ShadowWeightRow(E2RArchetype.AI_DATA_CENTER_CLOUD_SI_STAGE2_ACTIONABLE, 5, 5, 1, 0, 0, 0, 1, 1, 2, -5, -2, -1, -1, "AI data center+price reaction", "cloud/SI revenue missing", "recurring revenue+margin", "Kakao/LG CNS."),
    Round316ShadowWeightRow(E2RArchetype.AI_CLOUD_IPO_PRICE_MUTED, 4, 4, 0, 0, 0, 0, 0, 0, 1, -4, -5, -1, -1, "AI/cloud sales but IPO price failed", "post-listing strength missing", "contract growth+margin", "LG CNS IPO."),
    Round316ShadowWeightRow(E2RArchetype.WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE, 1, 0, 5, 5, 0, 1, 1, 1, 0, -1, -3, -5, -1, "MAU+IPO+Disney/IP deal", "profit durability missing", "paid conversion+IP revenue+profit", "Webtoon/Naver."),
    Round316ShadowWeightRow(E2RArchetype.GAME_IP_GLOBAL_EXPANSION_STAGE2, 0, 0, 1, 1, 5, 5, 0, 0, 1, -1, -2, -1, -4, "India expansion+BGMI scale", "ARPU/fund ROI missing", "India monetization+fund exits", "Krafton/Naver/Mirae."),
    Round316ShadowWeightRow(E2RArchetype.GAME_IP_IPO_STAGE2_WITH_CONCENTRATION_4B, 0, 0, 0, 1, 5, 0, 0, 0, 0, -1, -4, -1, -5, "game IP sales/profit", "repeat sales/pipeline missing", "retention+new title pipeline", "Shift Up."),
    Round316ShadowWeightRow(E2RArchetype.CONTENT_LABEL_GOVERNANCE_4C_WATCH, 0, 0, 2, 5, 0, 0, 5, 4, 1, -1, -1, -1, -1, "artist IP disrupted by governance", "legal resolution missing", "N/A", "HYBE."),
    Round316ShadowWeightRow(E2RArchetype.PLATFORM_FOUNDER_REGULATORY_4C_RELIEF, 2, 0, 2, 0, 0, 0, 3, 5, 1, -1, -1, -1, -1, "founder regulatory overhang", "platform monetization/relief price missing", "regulatory clearance+business normalization", "Kakao."),
    Round316ShadowWeightRow(E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C, 0, 0, 0, 0, 0, 0, 1, 1, 5, -1, -1, -1, -1, "data breach/fine/compensation", "remediation and trust recovery missing", "N/A", "SK Telecom."),
)


def round316_case_records() -> list[E2RCaseRecord]:
    return [case.to_case_record() for case in ROUND316_CASE_CANDIDATES]


def round316_case_rows() -> list[dict[str, str]]:
    return [case.as_row() for case in ROUND316_CASE_CANDIDATES]


def round316_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND316_TRIGGER_RECORDS]


def round316_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND316_SHADOW_WEIGHT_ROWS]


def round316_target_alias_rows() -> list[dict[str, str]]:
    return [{"target_alias": alias, "canonical_archetype": canonical} for alias, canonical in ROUND316_REQUIRED_TARGET_ALIASES.items()]


def round316_score_adjustment_rows() -> list[dict[str, str]]:
    return (
        [{"direction": "up", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND316_SCORE_UP_AXES]
        + [{"direction": "down", "axis": axis, "production_scoring_changed": "false"} for axis in ROUND316_SCORE_DOWN_AXES]
    )


def round316_summary() -> dict[str, object]:
    return {
        "source_round": ROUND316_SOURCE_ROUND_PATH,
        "round_id": ROUND316_ANALYST_ROUND_ID,
        "large_sector": ROUND316_LARGE_SECTOR,
        "method": ROUND316_METHOD,
        "case_candidate_count": len(ROUND316_CASE_CANDIDATES),
        "trigger_count": len(ROUND316_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND316_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": 2,
        "stage2_candidate_count": 5,
        "stage3_yellow_candidate_count": 1,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 5,
        "stage4c_watch_count": 3,
        "hard_4c_case_count": 1,
        "evidence_good_but_price_failed_or_muted_count": 2,
        "row_separation_required": True,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "full_adjusted_ohlc_complete": False,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R9 Loop 16",
    }


def round316_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND316_SOURCE_ROUND_PATH,
        "round_id": ROUND316_ANALYST_ROUND_ID,
        "large_sector": ROUND316_LARGE_SECTOR,
        "method": ROUND316_METHOD,
        "summary": round316_summary(),
        "required_target_aliases": dict(ROUND316_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": ROUND316_STAGE2_ACTIONABLE_RULES,
        "stage3_yellow_rules": ROUND316_STAGE3_YELLOW_RULES,
        "stage3_green_rules": ROUND316_STAGE3_GREEN_RULES,
        "green_blockers": ROUND316_GREEN_BLOCKERS,
        "score_up_axes": ROUND316_SCORE_UP_AXES,
        "score_down_axes": ROUND316_SCORE_DOWN_AXES,
        "stage4b_watch_triggers": ROUND316_STAGE4B_WATCH_TRIGGERS,
        "stage4c_watch_gates": ROUND316_4C_WATCH_GATES,
        "row_separation_rules": ROUND316_ROW_SEPARATION_RULES,
        "what_not_to_change": (
            "do_not_change_production_scoring",
            "do_not_use_round316_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_AI_infra_IPO_MAU_game_hit_artist_IP_founder_relief_or_security_headline_as_Green_without_recurring_revenue_ARPU_profit_repeat_sales_governance_clearance_or_trust_recovery",
            "do_not_invent_full_mfe_mae_without_adjusted_ohlc",
        ),
    }


def render_round316_summary_markdown() -> str:
    summary = round316_summary()
    lines = [
        "# R8 Loop 16 Platform / Content / Software / Security Trigger Validation",
        "",
        "This is calibration-only material. Production scoring and candidate generation are unchanged.",
        "",
        "Easy example: MAU is useful Stage2 evidence. It becomes Green only after ARPU, paid conversion, IP licensing revenue and profit are visible.",
        "",
        "## Summary",
    ]
    for key, value in summary.items():
        lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## Core Finding",
            "- Kakao / LG CNS / SK-AWS AI data center is the cleanest Stage2-Actionable AI infrastructure trigger.",
            "- LG CNS IPO is evidence-good but price failed because it traded below issue price.",
            "- Webtoon / Naver is Stage2-Actionable and Yellow-candidate, but prior drawdown and profit durability remain gates.",
            "- Krafton / Naver / Mirae and Shift Up are Stage2 until ARPU, ROI, repeat sales and pipeline evidence close.",
            "- HYBE, Kakao founder risk and SK Telecom breach are governance/security 4C-watch or hard 4C cases.",
            "- Stage3-Green confirmed: `0`.",
            "- Hard 4C confirmed: `1`.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round316_trigger_grid_markdown() -> str:
    lines = [
        "# Round 316 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | trigger_date | event_return_pct | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round316_trigger_rows():
        lines.append(f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |")
    return "\n".join(lines) + "\n"


def render_round316_stage_rules_markdown() -> str:
    return "\n".join(
        [
            "# Round 316 Stage Rules",
            "",
            "Do not apply these weights to production scoring yet.",
            "",
            "## Stage2-Actionable Rules",
            *_bullet_lines(ROUND316_STAGE2_ACTIONABLE_RULES),
            "",
            "## Stage3-Yellow Rules",
            *_bullet_lines(ROUND316_STAGE3_YELLOW_RULES),
            "",
            "## Stage3-Green Rules",
            *_bullet_lines(ROUND316_STAGE3_GREEN_RULES),
            "",
            "## Green Blockers",
            *_bullet_lines(ROUND316_GREEN_BLOCKERS),
            "",
            "## 4C Watch Gates",
            *_bullet_lines(ROUND316_4C_WATCH_GATES),
        ]
    ) + "\n"


def render_round316_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 316 Stage 4B / 4C Review",
        "",
        "## 4B Watch",
        *_bullet_lines(ROUND316_STAGE4B_WATCH_TRIGGERS),
        "",
        "## 4C Watch Gates",
        *_bullet_lines(ROUND316_4C_WATCH_GATES),
        "",
        "## Case Review",
    ]
    for case in ROUND316_CASE_CANDIDATES:
        if case.stage4b_date or case.stage4c_date:
            lines.append(f"- {case.case_id}: {case.stage_candidate} / {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round316_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 316 Price Validation Plan",
        "",
        "Full adjusted OHLC was not available. Reported event anchors are retained without inventing full-window MFE/MAE.",
        "",
    ]
    for case in ROUND316_CASE_CANDIDATES:
        lines.append(f"- {case.case_id}: {case.best_trigger} / {case.round_alignment_label} / full_window=`price_data_unavailable_after_deep_search`")
    return "\n".join(lines) + "\n"


def render_round316_row_separation_plan_markdown() -> str:
    lines = [
        "# Round 316 Row Separation Plan",
        "",
        "Case evidence, trigger anchors and full OHLC windows must be separate rows.",
        "",
        "Easy example: a Webtoon MAU or Disney headline is Stage2 evidence. It is not Green until ARPU, paid conversion, IP revenue and profit are visible.",
        "",
    ]
    lines.extend(_bullet_lines(ROUND316_ROW_SEPARATION_RULES))
    return "\n".join(lines) + "\n"


def write_round316_r8_loop16_reports(
    output_directory: str | Path = ROUND316_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND316_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND316_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND316_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND316_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    cases_file = Path(cases_path)
    triggers_file = Path(triggers_path)
    audit_file = Path(audit_path)
    weight_profile_file = Path(weight_profile_path)
    for path in (cases_file, triggers_file, audit_file, weight_profile_file):
        path.parent.mkdir(parents=True, exist_ok=True)

    write_case_library(round316_case_records(), cases_file)
    _write_jsonl(triggers_file, [trigger.as_dict() for trigger in ROUND316_TRIGGER_RECORDS])
    audit_file.write_text(json.dumps(round316_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(weight_profile_file, round316_shadow_weight_rows())

    paths = {
        "cases": cases_file,
        "triggers": triggers_file,
        "audit": audit_file,
        "weight_profiles": weight_profile_file,
        "case_matrix": output_dir / "round316_r8_loop16_case_matrix.csv",
        "target_aliases": output_dir / "round316_r8_loop16_target_aliases.csv",
        "trigger_grid_csv": output_dir / "round316_r8_loop16_trigger_grid.csv",
        "trigger_grid_md": output_dir / "round316_r8_loop16_trigger_grid.md",
        "summary": output_dir / "round316_r8_loop16_trigger_validation_summary.md",
        "stage_rules": output_dir / "round316_r8_loop16_stage_rules.md",
        "stage4b_4c_review": output_dir / "round316_r8_loop16_stage4b_4c_review.md",
        "score_adjustments": output_dir / "round316_r8_loop16_score_adjustments.csv",
        "shadow_weights": output_dir / "round316_r8_loop16_shadow_weights.csv",
        "price_validation_plan": output_dir / "round316_r8_loop16_price_validation_plan.md",
        "row_separation_plan": output_dir / "round316_r8_loop16_row_separation_plan.md",
    }

    _write_csv(paths["case_matrix"], round316_case_rows())
    _write_csv(paths["target_aliases"], round316_target_alias_rows())
    _write_csv(paths["trigger_grid_csv"], round316_trigger_rows())
    _write_csv(paths["score_adjustments"], round316_score_adjustment_rows())
    _write_csv(paths["shadow_weights"], round316_shadow_weight_rows())
    paths["trigger_grid_md"].write_text(render_round316_trigger_grid_markdown(), encoding="utf-8")
    paths["summary"].write_text(render_round316_summary_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round316_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round316_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round316_price_validation_plan_markdown(), encoding="utf-8")
    paths["row_separation_plan"].write_text(render_round316_row_separation_plan_markdown(), encoding="utf-8")
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
    "ROUND316_4C_WATCH_GATES",
    "ROUND316_CASE_CANDIDATES",
    "ROUND316_GREEN_BLOCKERS",
    "ROUND316_LARGE_SECTOR",
    "ROUND316_REQUIRED_TARGET_ALIASES",
    "ROUND316_ROW_SEPARATION_RULES",
    "ROUND316_SCORE_DOWN_AXES",
    "ROUND316_SCORE_UP_AXES",
    "ROUND316_SHADOW_WEIGHT_ROWS",
    "ROUND316_STAGE2_ACTIONABLE_RULES",
    "ROUND316_STAGE3_GREEN_RULES",
    "ROUND316_STAGE3_YELLOW_RULES",
    "ROUND316_STAGE4B_WATCH_TRIGGERS",
    "ROUND316_TRIGGER_RECORDS",
    "render_round316_stage4b_4c_review_markdown",
    "render_round316_stage_rules_markdown",
    "render_round316_trigger_grid_markdown",
    "round316_audit_payload",
    "round316_case_records",
    "round316_case_rows",
    "round316_shadow_weight_rows",
    "round316_summary",
    "round316_trigger_rows",
    "write_round316_r8_loop16_reports",
]
