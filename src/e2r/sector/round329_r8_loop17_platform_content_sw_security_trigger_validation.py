"""Round-329 R8 Loop-17 platform, content, software and security validation.

This module converts ``docs/round/round_329.md`` into calibration-only case
records, trigger rows, shadow weights and reports. It does not change
production scoring, staging, or candidate generation.

Easy example: Kakao can be Stage2 on an OpenAI partnership headline. It still
cannot become Green until MAU turns into ARPU, paid usage, ad/commerce lift and
controlled compute cost as of the replay date.
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


ROUND329_SOURCE_ROUND_PATH = "docs/round/round_329.md"
ROUND329_ANALYST_ROUND_ID = "round_257"
ROUND329_LOOP_NAME = "R8 Loop 17"
ROUND329_LARGE_SECTOR = "PLATFORM_CONTENT_SW_SECURITY"
ROUND329_METHOD = "trigger_level_backtest_v1_after_redteam"
ROUND329_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round329_r8_loop17_platform_content_sw_security_trigger_validation"
ROUND329_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r8_loop17_round257.jsonl"
ROUND329_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r8_loop17_round257.jsonl"
ROUND329_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round329_r8_loop17_platform_content_sw_security_trigger_validation_audit.json"
ROUND329_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round257_r8_loop17_v1.csv"

ROUND329_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED": E2RArchetype.AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED.value,
    "SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B": E2RArchetype.SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B.value,
    "WEBTOON_CONTENT_PLATFORM_STAGE2_HOLDCO_DISCOUNT": E2RArchetype.WEBTOON_CONTENT_PLATFORM_STAGE2_HOLDCO_DISCOUNT.value,
    "GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B": E2RArchetype.GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B.value,
    "IT_SERVICES_AI_CLOUD_IPO_PRICE_FAILED": E2RArchetype.IT_SERVICES_AI_CLOUD_IPO_PRICE_FAILED.value,
    "CYBER_BREACH_HARD_4C_SECURITY_CAPEX": E2RArchetype.CYBER_BREACH_HARD_4C_SECURITY_CAPEX.value,
    "KPOP_LABEL_GOVERNANCE_4B": E2RArchetype.KPOP_LABEL_GOVERNANCE_4B.value,
    "PLATFORM_GOVERNANCE_REGULATORY_4B": E2RArchetype.PLATFORM_GOVERNANCE_REGULATORY_4B.value,
}

ROUND329_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "event_return_at_least_5pct_or_reported_relative_price_validation",
    "AI_product_or_sovereign_AI_infra_trigger_is_specific",
    "content_or_game_IP_has_revenue_MAU_sales_or_profit_anchor",
    "IT_services_AI_cloud_IPO_has_sales_mix_OP_or_order_visibility_anchor",
    "governance_or_cybersecurity_overlay_is_separated_from_positive_stage_candidate",
    "trigger_row_stores_reported_event_anchor_without_inventing_full_MFE_MAE",
)

ROUND329_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "Stage2_conditions_pass",
    "monetization_or_utilization_path_exists_but_one_gate_remains_open",
    "MAU_ARPU_paid_conversion_cloud_utilization_or_live_service_retention_is_partially_visible",
    "reported_price_anchor_supports_evidence_but_full_adjusted_OHLC_is_missing",
    "legal_governance_or_cybersecurity_red_team_risk_is_not_hard_4C",
)

ROUND329_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "AI_chat_partnership_converts_to_paid_usage_ARPU_and_margin",
    "sovereign_AI_cloud_capex_converts_to_enterprise_or_government_contracts_and_utilization",
    "webtoon_MAU_converts_to_paid_ARPU_IP_revenue_and_parent_value_capture",
    "game_IP_converts_to_repeat_sales_live_service_retention_and_pipeline",
    "AI_cloud_IT_services_show_external_order_backlog_margin_and_post_IPO_price_strength",
    "governance_legal_and_cybersecurity_overhangs_are_closed",
    "full_adjusted_OHLC_MFE_MAE_window_supports_stage_candidate",
)

ROUND329_GREEN_BLOCKERS: tuple[str, ...] = (
    "AI_partnership_without_monetization",
    "AI_capex_without_utilization_or_contracts",
    "MAU_without_ARPU_paid_conversion_or_profit",
    "game_title_without_retention_or_pipeline",
    "IPO_without_aftermarket_strength",
    "content_IP_without_margin_or_parent_value_capture",
    "founder_label_or_platform_governance_risk_unresolved",
    "cyber_breach_or_security_capex_treated_as_growth",
    "full_adjusted_ohlc_missing_for_Green_confirmation",
)

ROUND329_SCORE_UP_AXES: tuple[str, ...] = (
    "AI_product_integration",
    "sovereign_AI_infra",
    "cloud_AI_capex_to_contract",
    "content_IP_partnership",
    "MAU_paid_conversion",
    "gaming_IP_sales_retention",
    "cyber_trust_security",
    "governance_legal_risk",
)

ROUND329_SCORE_DOWN_AXES: tuple[str, ...] = (
    "AI_partnership_without_monetization_penalty",
    "AI_capex_without_utilization_penalty",
    "IPO_without_aftermarket_strength_penalty",
    "content_IP_without_margin_penalty",
    "legal_control_dispute_penalty",
    "security_breach_revenue_cut_penalty",
    "founder_regulatory_risk_penalty",
)

ROUND329_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "AI_partnership_initial_pop_fades_without_monetization",
    "GPU_or_AI_cloud_capex_rerates_before_enterprise_contracts",
    "webtoon_IP_or_IPO_rally_remains_trapped_by_parent_holdco_discount",
    "game_IP_success_faces_title_concentration_or_legal_control_dispute",
    "AI_cloud_IT_services_IPO_trades_below_issue_price",
    "Kpop_label_artist_or_founder_governance_dispute",
    "platform_founder_or_regulatory_overhang_delays_AI_product_execution",
)

ROUND329_HARD_4C_GATES: tuple[str, ...] = (
    "large_scale_customer_data_breach_with_revenue_forecast_cut",
    "security_capex_and_compensation_liability_change_FCF_path",
    "regulator_finding_or_fine_confirms_operational_trust_break",
    "artist_contract_termination_causes_revenue_collapse",
    "founder_or_platform_control_risk_creates_permanent_business_impairment",
)

ROUND329_ROW_SEPARATION_RULES: tuple[str, ...] = (
    "case_library_row_describes_stage_candidate_and_evidence_quality",
    "trigger_calibration_row_stores_reported_event_anchor_AI_IPO_IP_governance_or_cybersecurity_metrics",
    "ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown",
    "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
    "do_not_treat_AI_chat_sovereign_AI_webtoon_game_IPO_governance_or_cybersecurity_headline_as_Green_without_monetization_utilization_retention_margin_or_risk_closure",
)


@dataclass(frozen=True)
class Round329TriggerRecord:
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
class Round329ShadowWeightRow:
    archetype: E2RArchetype
    ai_product_integration: int
    sovereign_ai_infra: int
    cloud_ai_capex_to_contract: int
    content_ip_partnership: int
    mau_paid_conversion: int
    gaming_ip_sales_retention: int
    cyber_trust_security: int
    governance_legal_risk: int
    ai_partnership_without_monetization_penalty: int
    ai_capex_without_utilization_penalty: int
    ipo_without_aftermarket_strength_penalty: int
    content_ip_without_margin_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "AI_product_integration": _signed(self.ai_product_integration),
            "sovereign_AI_infra": _signed(self.sovereign_ai_infra),
            "cloud_AI_capex_to_contract": _signed(self.cloud_ai_capex_to_contract),
            "content_IP_partnership": _signed(self.content_ip_partnership),
            "MAU_paid_conversion": _signed(self.mau_paid_conversion),
            "gaming_IP_sales_retention": _signed(self.gaming_ip_sales_retention),
            "cyber_trust_security": _signed(self.cyber_trust_security),
            "governance_legal_risk": _signed(self.governance_legal_risk),
            "AI_partnership_without_monetization_penalty": _signed(self.ai_partnership_without_monetization_penalty),
            "AI_capex_without_utilization_penalty": _signed(self.ai_capex_without_utilization_penalty),
            "IPO_without_aftermarket_strength_penalty": _signed(self.ipo_without_aftermarket_strength_penalty),
            "content_IP_without_margin_penalty": _signed(self.content_ip_without_margin_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round329CaseCandidate:
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
            "do_not_use_round329_cases_as_candidate_generation_input",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_AI_chat_sovereign_AI_webtoon_game_IPO_governance_or_cybersecurity_headline_as_Green_without_monetization_utilization_retention_margin_or_risk_closure",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")

        stage4b_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4B" in field
            or "4b" in field
            or "legal" in field
            or "governance" in field
            or "holdco" in field
            or "IPO" in field
            or "capex" in field
        )
        stage4c_evidence = tuple(
            field
            for field in (*self.red_flag_fields, *self.evidence_fields)
            if "4C" in field
            or "4c" in field
            or "breach" in field
            or "forecast_cut" in field
            or "compensation" in field
            or "regulator" in field
            or "data_leak" in field
        )
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR" if "/" not in self.symbol or "WBTN" in self.symbol else "KR/US",
            sector_raw=ROUND329_LARGE_SECTOR,
            large_sector=ROUND329_LARGE_SECTOR,
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
            must_have_fields=ROUND329_STAGE3_GREEN_RULES,
            red_flag_fields=self.red_flag_fields,
            key_evidence_fields=self.evidence_fields,
            false_positive_reason="; ".join(self.red_flag_fields) if self.case_type in {"event_premium", "4b_watch", "4c_thesis_break", "failed_rerating"} else None,
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
            "extra_price_metrics": json.dumps(self.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": self.score_price_alignment,
            "round_alignment_label": self.round_alignment_label,
            "rerating_result": self.rerating_result,
            "stage_failure_type": self.stage_failure_type,
            "notes": self.notes,
        }


ROUND329_CASE_CANDIDATES: tuple[Round329CaseCandidate, ...] = (
    Round329CaseCandidate(
        "r8_loop17_kakao_openai_ai_partnership",
        "035720",
        "Kakao",
        E2RArchetype.AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED,
        (E2RArchetype.AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE, E2RArchetype.AI_SOFTWARE_PARTNERSHIP_EVENT),
        "success_candidate",
        "Stage2_AI_chat_partnership_price_failed",
        "r8l17_kakao_openai_T1",
        "Stage2_price_failed",
        "Stage2 price-failed",
        date(2025, 2, 4),
        date(2025, 2, 4),
        None,
        date(2025, 2, 4),
        None,
        False,
        ("OpenAI_Kakao_joint_develop", "KakaoTalk_AI_integration", "Korean_AI_localization", "initial_plus_9pct", "later_minus_2pct"),
        ("product_monetization_uncertain_4B", "AI_inference_cost_4B", "founder_legal_overhang_4B", "regulatory_scrutiny_4B", "execution_risk_4B"),
        {"trigger_date": "2025-02-04", "initial_event_return_pct": 9, "later_event_return_pct": -2, "context": "Stargate_adjacent_AI_partnership"},
        "evidence_good_but_price_failed",
        "AI_partnership_stage2_price_failed",
        "event_premium",
        "stage2_watch_success",
        "AI partnership evidence is real, but the initial rally faded; paid AI usage, ARPU and margin are Green gates.",
    ),
    Round329CaseCandidate(
        "r8_loop17_naver_sovereign_ai_blackwell",
        "035420",
        "Naver",
        E2RArchetype.SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B,
        (E2RArchetype.AI_INFRA_PORTAL_STAGE2_ACTIONABLE, E2RArchetype.SOVEREIGN_KOREAN_AI_MODEL),
        "success_candidate",
        "Stage2_sovereign_AI_cloud_capex_4B",
        "r8l17_naver_blackwell_T1",
        "Stage2_sovereign_AI_infra",
        "Stage2",
        date(2025, 10, 31),
        date(2025, 10, 31),
        None,
        date(2025, 10, 31),
        None,
        False,
        ("South_Korea_over_260000_Blackwell_chips", "Naver_60000_chips", "AI_cloud_investment_usd_690M_2026", "sovereign_AI_data_sovereignty", "Middle_East_SEA_Japan_expansion"),
        ("capex_ROI_4B", "global_cloud_scale_risk_4B", "enterprise_contract_visibility_4B", "GPU_depreciation_4B", "AI_margin_uncertainty_4B"),
        {"trigger_date": "2025-10-31", "blackwell_chips_south_korea": 260000, "naver_chips": 60000, "ai_cloud_investment_usd_mn": 690, "ytd_return_context_pct": 20},
        "aligned",
        "sovereign_AI_infra_stage2_capex_4B",
        "event_premium",
        "stage2_watch_success",
        "Sovereign AI infrastructure can be Stage2, but enterprise contracts, utilization and capex ROI are still required before Yellow or Green.",
    ),
    Round329CaseCandidate(
        "r8_loop17_webtoon_naver_content_platform",
        "WBTN/035420",
        "Webtoon Entertainment / Naver",
        E2RArchetype.WEBTOON_CONTENT_PLATFORM_STAGE2_HOLDCO_DISCOUNT,
        (E2RArchetype.WEBTOON_IP_MONETIZATION_STAGE2_ACTIONABLE, E2RArchetype.WEBTOON_IPO_CONTENT_PLATFORM_STAGE2),
        "success_candidate",
        "Stage2_webtoon_content_platform_holdco_discount",
        "r8l17_webtoon_disney_T2",
        "Stage2_content_IP_platform",
        "Stage2-Actionable candidate + 4B-watch",
        date(2024, 6, 27),
        date(2024, 6, 27),
        None,
        date(2024, 6, 19),
        None,
        False,
        ("IPO_intraday_plus_14_3pct", "IPO_raise_usd_315M", "valuation_usd_2_71B", "Naver_private_placement_usd_50M", "Disney_plus_62pct", "Q2_revenue_usd_348_3M", "revenue_yoy_plus_8_5pct"),
        ("parent_holdco_discount_4B", "Naver_market_talk_minus_0_9pct", "Nomura_target_cut_22pct", "holdco_discount_50pct", "post_IPO_drawdown_4B", "creator_payout_4B"),
        {"ipo_event_return_intraday_pct": 14.3, "ipo_raise_usd_mn": 315, "valuation_usd_bn": 2.71, "naver_private_placement_usd_mn": 50, "disney_event_return_pct": 62, "q2_revenue_usd_mn": 348.3, "q2_revenue_yoy_pct": 8.5, "holdco_discount_pct": 50},
        "aligned",
        "Webtoon_stage2_but_Naver_holdco_discount_4B",
        "unknown",
        "stage2_watch_success",
        "Webtoon has Stage2 content-platform evidence, but parent value capture and holding-company discount remain 4B gates.",
    ),
    Round329CaseCandidate(
        "r8_loop17_shift_up_gaming_ip_ipo",
        "462870",
        "Shift Up",
        E2RArchetype.GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B,
        (E2RArchetype.GAME_IP_IPO_STAGE2_WITH_CONCENTRATION_4B, E2RArchetype.GAME_IP_MONETIZATION_IPO_STAGE2),
        "success_candidate",
        "Stage2_game_IP_success_with_concentration_4B",
        "r8l17_shiftup_ipo_T1",
        "Stage2_game_IP",
        "Stage2 + 4B-watch",
        date(2024, 6, 27),
        date(2024, 6, 27),
        None,
        date(2024, 6, 27),
        None,
        False,
        ("IPO_raise_krw_435B", "IPO_raise_usd_313M", "valuation_krw_3_5T", "valuation_usd_2_52B", "Nikke_revenue_krw_255B", "Stellar_Blade_launch"),
        ("title_concentration_4B", "Tencent_ownership_4B", "PC_port_sales_execution_4B", "sequel_pipeline_4B", "live_service_retention_4B"),
        {"trigger_date": "2024-06-27", "ipo_raise_krw_bn": 435, "ipo_raise_usd_mn": 313, "valuation_krw_trn": 3.5, "valuation_usd_bn": 2.52, "nikke_revenue_krw_bn": 255},
        "unknown",
        "game_IP_stage2_not_Green_without_retention_pipeline",
        "event_premium",
        "stage2_watch_success",
        "Hit-title and IPO evidence support Stage2, but retention, sequel pipeline and concentration risk are still gates.",
    ),
    Round329CaseCandidate(
        "r8_loop17_krafton_subnautica_legal_4b",
        "259960",
        "Krafton / Unknown Worlds",
        E2RArchetype.GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B,
        (E2RArchetype.GAME_IP_LAUNCH_DELAY_LEGAL_RISK, E2RArchetype.GAME_STUDIO_M_AND_A_GOVERNANCE_4C),
        "4b_watch",
        "game_studio_control_legal_4B",
        "r8l17_krafton_subnautica_T1",
        "4B_legal_control_dispute",
        "4B-watch",
        date(2026, 3, 16),
        None,
        None,
        date(2026, 3, 16),
        None,
        False,
        ("Delaware_court_against_Krafton", "improper_removal_CEO", "operational_control_returned_to_Ted_Gill", "earnout_usd_250M", "timeline_extended"),
        ("release_timing_4B", "studio_governance_4B", "earnout_liability_4B", "reputation_damage_4B", "appeal_risk_4B"),
        {"trigger_date": "2026-03-16", "earnout_usd_mn": 250, "control_returned_to": "Ted_Gill"},
        "aligned",
        "game_legal_control_4B_not_positive_stage",
        "no_rerating",
        "should_have_been_red",
        "A studio control dispute is a 4B risk overlay; it is not positive E2R evidence even if the IP remains valuable.",
    ),
    Round329CaseCandidate(
        "r8_loop17_lg_cns_ai_cloud_ipo_price_failed",
        "064400",
        "LG CNS",
        E2RArchetype.IT_SERVICES_AI_CLOUD_IPO_PRICE_FAILED,
        (E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE, E2RArchetype.CLOUD_AI_IT_SERVICES_EVIDENCE_GOOD_PRICE_FAILED),
        "failed_rerating",
        "AI_cloud_IT_services_IPO_price_failed",
        "r8l17_lg_cns_ipo_T1",
        "Stage2_price_failed",
        "Stage2 price-failed",
        date(2025, 2, 5),
        date(2025, 2, 5),
        None,
        date(2025, 2, 5),
        None,
        False,
        ("IPO_raise_krw_1_2T", "IPO_raise_usd_827_1M", "issue_price_61900", "open_60500", "last_59700", "cloud_AI_sales_share_54pct", "revenue_krw_4_0T", "OP_krw_313B"),
        ("weak_IPO_debut_4B", "valuation_overhang_4B", "AI_MA_execution_4B", "captive_sales_mix_4B", "external_order_backlog_unknown_4B"),
        {"trigger_date": "2025-02-05", "ipo_raise_krw_trn": 1.2, "ipo_raise_usd_mn": 827.1, "issue_price_krw": 61900, "open_price_krw": 60500, "last_price_krw": 59700, "cloud_ai_sales_share_pct": 54, "revenue_krw_trn": 4.0, "op_krw_bn": 313},
        "evidence_good_but_price_failed",
        "AI_cloud_IPO_evidence_good_but_price_failed",
        "unknown",
        "stage2_watch_success",
        "AI/cloud mix and OP are real, but the IPO traded below issue price; external backlog and margin durability are required.",
    ),
    Round329CaseCandidate(
        "r8_loop17_sk_telecom_cyber_breach",
        "017670",
        "SK Telecom",
        E2RArchetype.CYBER_BREACH_HARD_4C_SECURITY_CAPEX,
        (E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C, E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C),
        "4c_thesis_break",
        "hard_4C_cyber_breach_security_capex",
        "r8l17_skt_breach_T0",
        "hard_4C_cybersecurity",
        "4C",
        date(2025, 4, 28),
        None,
        None,
        None,
        date(2025, 4, 28),
        True,
        ("intraday_minus_8_5pct", "close_minus_6_7pct", "KOSPI_plus_0_1pct", "affected_subscribers_23M", "leaked_data_26_96M", "security_capex_krw_700B", "August_fee_discount_50pct", "revenue_forecast_cut_krw_800B", "compensation_potential_krw_2_3T"),
        ("churn_stabilization_required_4C", "ARPU_recovery_required_4C", "security_audit_completion_required_4C", "compensation_finality_required_4C", "regulator_closure_required_4C"),
        {"trigger_date": "2025-04-28", "intraday_event_return_pct": -8.5, "close_event_return_pct": -6.7, "kospi_same_context_pct": 0.1, "market_relative_pp": -6.8, "affected_subscribers_mn": 23, "leaked_data_pieces_mn": 26.96, "security_capex_krw_bn": 700, "august_fee_discount_pct": 50, "revenue_forecast_cut_krw_bn": 800, "possible_compensation_krw_trn": 2.3},
        "aligned",
        "hard_4C_success_cybersecurity",
        "thesis_break",
        "should_have_been_red",
        "The breach has customer trust, security capex, revenue forecast and compensation impacts; this is hard 4C, not a growth capex case.",
    ),
    Round329CaseCandidate(
        "r8_loop17_hybe_ador_bang_governance_4b",
        "352820",
        "HYBE",
        E2RArchetype.KPOP_LABEL_GOVERNANCE_4B,
        (E2RArchetype.CONTENT_LABEL_GOVERNANCE_4C_WATCH, E2RArchetype.KPOP_IP_GOVERNANCE_4C_WATCH),
        "4b_watch",
        "Kpop_label_governance_4B",
        "r8l17_hybe_ador_T0",
        "4B_label_founder_governance",
        "4B-watch",
        date(2024, 4, 24),
        None,
        None,
        date(2024, 4, 24),
        None,
        False,
        ("ADOR_audit", "NewJeans_control_dispute", "HYBE_nearly_minus_8pct", "Bang_warrant_2026_04_21", "Bang_event_minus_2_4pct"),
        ("ADOR_NewJeans_label_control_4B", "artist_contract_uncertainty_4B", "founder_capital_market_law_investigation_4B", "IPO_related_legal_risk_4B", "brand_reputation_4B"),
        {"ador_dispute_date": "2024-04-24", "ador_dispute_event_return_pct": "nearly_-8", "bang_warrant_date": "2026-04-21", "bang_warrant_event_return_pct": -2.4},
        "aligned",
        "Kpop_label_governance_4B_not_hard_4C_without_revenue_collapse",
        "no_rerating",
        "should_have_been_red",
        "Artist IP is not enough for Green while label control and founder legal overhang remain open.",
    ),
    Round329CaseCandidate(
        "r8_loop17_kakao_founder_legal_governance",
        "035720",
        "Kakao",
        E2RArchetype.PLATFORM_GOVERNANCE_REGULATORY_4B,
        (E2RArchetype.PLATFORM_FOUNDER_REGULATORY_4C_RELIEF, E2RArchetype.KAKAO_PLATFORM_GOVERNANCE_4C_WATCH),
        "4b_watch",
        "platform_founder_regulatory_4B",
        "r8l17_kakao_founder_T0",
        "4B_founder_regulatory",
        "4B-watch",
        date(2024, 7, 23),
        None,
        None,
        date(2024, 7, 23),
        None,
        False,
        ("Kim_Beom_su_arrested", "SM_Entertainment_stock_manipulation_allegation", "Kakao_minus_3_4pct", "YTD_minus_24pct", "KakaoBank_control_risk", "relief_2025_10_21_acquittal_no_price_anchor"),
        ("SM_Entertainment_stock_manipulation_allegation_4B", "AI_investment_delay_4B", "overseas_expansion_delay_4B", "KakaoBank_control_risk_4B", "regulatory_scrutiny_4B"),
        {"arrest_date": "2024-07-23", "arrest_event_return_pct": -3.4, "ytd_return_context_pct": -24, "relief_date": "2025-10-21", "direct_relief_price_anchor": None},
        "aligned",
        "platform_founder_regulatory_4B_with_relief_but_no_business_conversion",
        "credit_relief_rally",
        "should_have_been_red",
        "Founder legal relief can remove an overhang, but it is not earnings conversion and does not create Green without platform monetization recovery.",
    ),
)

ROUND329_TRIGGER_RECORDS: tuple[Round329TriggerRecord, ...] = (
    Round329TriggerRecord("r8l17_kakao_openai_T1", "r8_loop17_kakao_openai_ai_partnership", "Stage2_AI_chat_partnership_price_failed", "2025-02-04", "Kakao and OpenAI partnership for Korean AI localization and KakaoTalk integration; initial +9% later faded to -2%.", "initial_+9_later_-2", "AI_partnership_price_failed", "Stage2_price_failed", {"initial_event_return_pct": 9, "later_event_return_pct": -2}),
    Round329TriggerRecord("r8l17_naver_blackwell_T1", "r8_loop17_naver_sovereign_ai_blackwell", "Stage2_sovereign_AI_infra", "2025-10-31", "South Korea Blackwell allocation and Naver 60,000-chip context; Naver AI/cloud investment planned.", "reported_price_anchor_only", "sovereign_AI_infra_stage2", "Stage2", {"naver_chips": 60000, "ai_cloud_investment_usd_mn": 690}),
    Round329TriggerRecord("r8l17_webtoon_ipo_T0", "r8_loop17_webtoon_naver_content_platform", "Stage2_content_platform_IPO", "2024-06-27", "Webtoon IPO raised $315M and traded up 14.3% intraday.", 14.3, "content_platform_IPO_stage2", "Stage2", {"ipo_raise_usd_mn": 315, "valuation_usd_bn": 2.71}),
    Round329TriggerRecord("r8l17_webtoon_disney_T2", "r8_loop17_webtoon_naver_content_platform", "Stage2_Actionable_candidate", "2025-08-13", "Webtoon +62% on Disney/IP and earnings context.", 62, "content_IP_partnership_stage2_actionable_candidate", "Stage2-Actionable_candidate", {"disney_event_return_pct": 62}),
    Round329TriggerRecord("r8l17_naver_webtoon_holdco_T1", "r8_loop17_webtoon_naver_content_platform", "4B_holdco_discount", "2024-06-19", "Naver read-through was muted around Webtoon value-unlock expectations.", -0.9, "Naver_holdco_discount_4B", "4B-watch", {"naver_market_talk_return_pct": -0.9, "holdco_discount_pct": 50}),
    Round329TriggerRecord("r8l17_shiftup_ipo_T1", "r8_loop17_shift_up_gaming_ip_ipo", "Stage2_game_IP_IPO", "2024-06-27", "Shift Up IPO raise and hit-title revenue support Stage2 but not Green.", "reported_price_anchor_only", "game_IP_stage2_with_4B_concentration", "Stage2+4B", {"ipo_raise_krw_bn": 435, "nikke_revenue_krw_bn": 255}),
    Round329TriggerRecord("r8l17_krafton_subnautica_T1", "r8_loop17_krafton_subnautica_legal_4b", "4B_game_studio_legal_control", "2026-03-16", "Court ruling and studio control dispute create legal/control 4B overlay.", "price_data_unavailable_after_deep_search", "game_legal_control_4B", "4B-watch", {"earnout_usd_mn": 250}),
    Round329TriggerRecord("r8l17_lg_cns_ipo_T1", "r8_loop17_lg_cns_ai_cloud_ipo_price_failed", "Stage2_AI_cloud_IPO_price_failed", "2025-02-05", "LG CNS issue price 61,900 won, opened 60,500 won, later 59,700 won despite AI/cloud mix.", "issue_61900_last_59700", "AI_cloud_IPO_price_failed", "Stage2_price_failed", {"issue_price_krw": 61900, "last_price_krw": 59700}),
    Round329TriggerRecord("r8l17_skt_breach_T0", "r8_loop17_sk_telecom_cyber_breach", "hard_4C_cybersecurity", "2025-04-28", "SK Telecom breach: close -6.7% vs KOSPI +0.1%, 23M affected subscribers and revenue forecast cut risk.", -6.7, "hard_4C_success_cybersecurity", "4C", {"market_relative_pp": -6.8, "affected_subscribers_mn": 23, "revenue_forecast_cut_krw_bn": 800}),
    Round329TriggerRecord("r8l17_hybe_ador_T0", "r8_loop17_hybe_ador_bang_governance_4b", "4B_label_governance", "2024-04-24", "HYBE audits ADOR amid NewJeans control dispute; shares nearly -8%.", "nearly_-8", "label_governance_4B", "4B-watch", {"ador_event_return_pct": "nearly_-8"}),
    Round329TriggerRecord("r8l17_hybe_bang_T2", "r8_loop17_hybe_ador_bang_governance_4b", "4B_founder_legal", "2026-04-21", "Bang Si-hyuk warrant/investigation context; HYBE -2.4%.", -2.4, "founder_legal_4B", "4B-watch", {"bang_event_return_pct": -2.4}),
    Round329TriggerRecord("r8l17_kakao_founder_T0", "r8_loop17_kakao_founder_legal_governance", "4B_founder_regulatory", "2024-07-23", "Kakao founder arrest over SM Entertainment stock manipulation allegation; Kakao -3.4%.", -3.4, "platform_founder_regulatory_4B", "4B-watch", {"arrest_event_return_pct": -3.4}),
)

ROUND329_SHADOW_WEIGHT_ROWS: tuple[Round329ShadowWeightRow, ...] = (
    Round329ShadowWeightRow(E2RArchetype.AI_CHAT_PLATFORM_PARTNERSHIP_STAGE2_PRICE_FAILED, 5, 1, 2, 0, 4, 0, 2, 4, -5, -2, -1, -1, "AI partnership + product integration", "paid usage/ARPU still missing", "paid AI usage+ARPU+margin", "Kakao/OpenAI."),
    Round329ShadowWeightRow(E2RArchetype.SOVEREIGN_AI_CLOUD_INFRA_STAGE2_CAPEX_4B, 2, 5, 5, 0, 2, 0, 2, 1, -1, -5, -1, -1, "sovereign AI infra capex", "contract/utilization missing", "enterprise contract+utilization+ROI", "Naver Blackwell."),
    Round329ShadowWeightRow(E2RArchetype.WEBTOON_CONTENT_PLATFORM_STAGE2_HOLDCO_DISCOUNT, 0, 0, 1, 5, 5, 0, 1, 1, -1, -1, -2, -4, "IPO/IP partnership+MAU", "holdco discount and margin gates", "paid conversion+IP revenue+parent value capture", "Webtoon/Naver."),
    Round329ShadowWeightRow(E2RArchetype.GAMING_IP_SUCCESS_STAGE2_WITH_LEGAL_4B, 0, 0, 0, 1, 1, 5, 1, 5, -1, -1, -2, -1, "hit game IP sales", "title concentration/legal risk", "retention+pipeline+legal closure", "Shift Up/Krafton."),
    Round329ShadowWeightRow(E2RArchetype.IT_SERVICES_AI_CLOUD_IPO_PRICE_FAILED, 2, 2, 5, 0, 0, 0, 2, 1, -2, -4, -5, -1, "AI/cloud sales mix", "IPO below issue", "external backlog+margin+price strength", "LG CNS."),
    Round329ShadowWeightRow(E2RArchetype.CYBER_BREACH_HARD_4C_SECURITY_CAPEX, 0, 0, 0, 0, 5, 0, 5, 3, -1, -1, -1, -1, "trust/security metrics", "hard 4C if forecast/cost hit", "N/A", "SK Telecom."),
    Round329ShadowWeightRow(E2RArchetype.KPOP_LABEL_GOVERNANCE_4B, 0, 0, 0, 5, 2, 0, 1, 5, -1, -1, -1, -3, "content IP but governance risk", "label control/legal gate", "artist continuity+governance closure", "HYBE."),
    Round329ShadowWeightRow(E2RArchetype.PLATFORM_GOVERNANCE_REGULATORY_4B, 3, 1, 2, 2, 3, 0, 2, 5, -3, -1, -1, -2, "platform governance relief", "business conversion missing", "legal closure+monetization recovery", "Kakao founder/legal."),
)


def round329_case_records() -> tuple[E2RCaseRecord, ...]:
    records = tuple(candidate.to_case_record() for candidate in ROUND329_CASE_CANDIDATES)
    for record in records:
        record.validate()
    return records


def round329_case_rows() -> list[dict[str, str]]:
    return [candidate.as_row() for candidate in ROUND329_CASE_CANDIDATES]


def round329_trigger_rows() -> list[dict[str, str]]:
    return [trigger.as_row() for trigger in ROUND329_TRIGGER_RECORDS]


def round329_shadow_weight_rows() -> list[dict[str, str]]:
    return [row.as_row() for row in ROUND329_SHADOW_WEIGHT_ROWS]


def round329_summary() -> dict[str, object]:
    return {
        "source_round": ROUND329_SOURCE_ROUND_PATH,
        "round_id": ROUND329_ANALYST_ROUND_ID,
        "loop_name": ROUND329_LOOP_NAME,
        "large_sector": ROUND329_LARGE_SECTOR,
        "method": ROUND329_METHOD,
        "case_candidate_count": len(ROUND329_CASE_CANDIDATES),
        "trigger_count": len(ROUND329_TRIGGER_RECORDS),
        "target_archetype_count": len(ROUND329_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_candidate_count": sum(1 for case in ROUND329_CASE_CANDIDATES if "Actionable" in case.stage_candidate),
        "stage2_candidate_count": sum(1 for case in ROUND329_CASE_CANDIDATES if "Stage2" in case.stage_candidate),
        "stage3_yellow_candidate_count": sum(1 for case in ROUND329_CASE_CANDIDATES if "Yellow" in case.stage_candidate),
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": sum(1 for case in ROUND329_CASE_CANDIDATES if case.stage4b_date is not None),
        "hard_4c_case_count": sum(1 for case in ROUND329_CASE_CANDIDATES if case.hard_4c_confirmed),
        "evidence_good_but_price_failed_or_muted_count": sum(1 for case in ROUND329_CASE_CANDIDATES if case.score_price_alignment == "evidence_good_but_price_failed"),
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "next_round": "R9 Loop 17",
    }


def round329_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND329_SOURCE_ROUND_PATH,
        "round_id": ROUND329_ANALYST_ROUND_ID,
        "large_sector": ROUND329_LARGE_SECTOR,
        "method": ROUND329_METHOD,
        "summary": round329_summary(),
        "target_archetypes": dict(ROUND329_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND329_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND329_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND329_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND329_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND329_SCORE_UP_AXES),
        "score_down_axes": list(ROUND329_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND329_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND329_HARD_4C_GATES),
        "row_separation_rules": list(ROUND329_ROW_SEPARATION_RULES),
        "shadow_weights": round329_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_change_production_scoring",
            "do_not_use_round329_cases_as_candidate_generation_input",
            "do_not_force_Stage3_Green",
            "do_not_create_MFE_MAE_without_full_adjusted_OHLC",
            "do_not_treat_AI_chat_sovereign_AI_webtoon_game_IPO_governance_or_cybersecurity_headline_as_Green_without_monetization_utilization_retention_margin_or_risk_closure",
        ],
    }


def render_round329_summary_markdown() -> str:
    summary = round329_summary()
    lines = [
        "# Round 329 R8 Loop 17 Platform Content Software Security Trigger Validation",
        "",
        f"- source_round: `{ROUND329_SOURCE_ROUND_PATH}`",
        f"- analyst_round_id: `{ROUND329_ANALYST_ROUND_ID}`",
        f"- large_sector: `{ROUND329_LARGE_SECTOR}`",
        f"- method: `{ROUND329_METHOD}`",
        f"- case candidates: `{summary['case_candidate_count']}`",
        f"- triggers: `{summary['trigger_count']}`",
        f"- Stage2 candidates: `{summary['stage2_candidate_count']}`",
        f"- Stage3-Green confirmed: `{summary['stage3_green_confirmed_count']}`",
        "- production_scoring_changed: `false`",
        "- candidate_generation_input: `false`",
        "- shadow_weight_only: `true`",
        "",
        "## 핵심 결론",
        "",
        "- Kakao / OpenAI는 Stage2 price-failed다. 파트너십은 증거지만 유료 사용과 ARPU가 없으면 Green이 아니다.",
        "- Naver sovereign AI 인프라는 Stage2다. GPU/CapEx가 계약과 utilization으로 이어져야 한다.",
        "- Webtoon은 Stage2-Actionable 후보지만 Naver parent holdco discount가 4B gate다.",
        "- Shift Up은 게임 IP Stage2이고, Krafton/Subnautica는 법적 통제 분쟁 4B다.",
        "- LG CNS는 AI/cloud 매출 mix가 있어도 IPO가 issue price 아래로 거래되어 price-failed다.",
        "- SK Telecom breach는 hard 4C다. 보안 capex를 성장 capex로 보지 않는다.",
        "- HYBE와 Kakao founder/legal 리스크는 Green 차단용 4B governance overlay다.",
    ]
    return "\n".join(lines) + "\n"


def render_round329_trigger_grid_markdown() -> str:
    lines = [
        "# Round 329 R8 Loop 17 Trigger Grid",
        "",
        "| trigger_id | case_id | trigger_type | date | event_return | promote_to |",
        "| --- | --- | --- | --- | ---: | --- |",
    ]
    for row in round329_trigger_rows():
        lines.append(
            f"| {row['trigger_id']} | {row['case_id']} | {row['trigger_type']} | {row['trigger_date']} | {row['event_return_pct']} | {row['promote_to']} |"
        )
    return "\n".join(lines) + "\n"


def render_round329_stage_rules_markdown() -> str:
    sections = [
        ("Stage2-Actionable Rules", ROUND329_STAGE2_ACTIONABLE_RULES),
        ("Stage3-Yellow Rules", ROUND329_STAGE3_YELLOW_RULES),
        ("Stage3-Green Rules", ROUND329_STAGE3_GREEN_RULES),
        ("Green Blockers", ROUND329_GREEN_BLOCKERS),
        ("Score Up Axes", ROUND329_SCORE_UP_AXES),
        ("Score Down Axes", ROUND329_SCORE_DOWN_AXES),
        ("Row Separation Rules", ROUND329_ROW_SEPARATION_RULES),
    ]
    lines = ["# Round 329 R8 Loop 17 Stage Rules", "", "Do not apply these weights to production scoring yet.", ""]
    for title, values in sections:
        lines.extend([f"## {title}", ""])
        lines.extend(f"- `{value}`" for value in values)
        lines.append("")
    return "\n".join(lines)


def render_round329_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 329 R8 Loop 17 Stage 4B / 4C Review", "", "## 4B Watch", ""]
    lines.extend(f"- `{item}`" for item in ROUND329_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- `{item}`" for item in ROUND329_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND329_CASE_CANDIDATES:
        lines.append(f"- `{case.case_id}`: {case.stage_candidate}; {case.round_alignment_label}")
    return "\n".join(lines) + "\n"


def render_round329_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 329 R8 Loop 17 Price Validation Plan",
        "",
        "Full adjusted OHLC is not complete. Reported event anchors are retained, but MFE/MAE, peak and drawdown are not invented.",
        "",
        "| case_id | status | event anchor | next backfill |",
        "| --- | --- | --- | --- |",
    ]
    for case in ROUND329_CASE_CANDIDATES:
        lines.append(
            f"| {case.case_id} | price_data_unavailable_after_deep_search | {json.dumps(case.extra_price_metrics, ensure_ascii=False, sort_keys=True)} | adjusted OHLC backfill required |"
        )
    return "\n".join(lines) + "\n"


def write_round329_r8_loop17_reports(
    *,
    output_directory: str | Path = ROUND329_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND329_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND329_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND329_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND329_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)
    cases_path = Path(cases_path)
    triggers_path = Path(triggers_path)
    audit_path = Path(audit_path)
    weight_profile_path = Path(weight_profile_path)

    cases = write_case_library(round329_case_records(), cases_path)
    triggers = _write_jsonl(triggers_path, (trigger.as_dict() for trigger in ROUND329_TRIGGER_RECORDS))
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(json.dumps(round329_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    weights = _write_csv(weight_profile_path, round329_shadow_weight_rows())

    paths = {
        "cases": cases,
        "triggers": triggers,
        "audit": audit_path,
        "weight_profile": weights,
        "case_rows_csv": output_directory / "case_rows.csv",
        "trigger_rows_csv": output_directory / "trigger_rows.csv",
        "summary": output_directory / "round329_summary.md",
        "trigger_grid_md": output_directory / "trigger_grid.md",
        "stage_rules": output_directory / "stage_rules.md",
        "stage4b_4c_review": output_directory / "stage4b_4c_review.md",
        "price_validation_plan": output_directory / "price_validation_plan.md",
    }
    _write_csv(paths["case_rows_csv"], round329_case_rows())
    _write_csv(paths["trigger_rows_csv"], round329_trigger_rows())
    paths["summary"].write_text(render_round329_summary_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round329_trigger_grid_markdown(), encoding="utf-8")
    paths["stage_rules"].write_text(render_round329_stage_rules_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round329_stage4b_4c_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round329_price_validation_plan_markdown(), encoding="utf-8")
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


__all__ = [
    "ROUND329_CASE_CANDIDATES",
    "ROUND329_GREEN_BLOCKERS",
    "ROUND329_HARD_4C_GATES",
    "ROUND329_LARGE_SECTOR",
    "ROUND329_REQUIRED_TARGET_ALIASES",
    "ROUND329_ROW_SEPARATION_RULES",
    "ROUND329_SCORE_DOWN_AXES",
    "ROUND329_SCORE_UP_AXES",
    "ROUND329_SHADOW_WEIGHT_ROWS",
    "ROUND329_STAGE2_ACTIONABLE_RULES",
    "ROUND329_STAGE3_GREEN_RULES",
    "ROUND329_STAGE3_YELLOW_RULES",
    "ROUND329_STAGE4B_WATCH_TRIGGERS",
    "ROUND329_TRIGGER_RECORDS",
    "render_round329_stage4b_4c_review_markdown",
    "render_round329_stage_rules_markdown",
    "render_round329_trigger_grid_markdown",
    "round329_audit_payload",
    "round329_case_records",
    "round329_case_rows",
    "round329_shadow_weight_rows",
    "round329_summary",
    "round329_trigger_rows",
    "write_round329_r8_loop17_reports",
]
