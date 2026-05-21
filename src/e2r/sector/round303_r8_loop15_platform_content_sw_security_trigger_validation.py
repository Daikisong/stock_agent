"""Round-303 R8 Loop-15 platform/content/SW/security trigger validation pack.

This module converts ``docs/round/round_303.md`` into calibration-only case
records, trigger rows, and reports. It does not change production scoring,
staging, or candidate generation.

Easy example: an OpenAI partnership can be Stage 2 evidence, but it is not
Stage 3-Green until paid usage, retention, ad uplift, and margin are visible.
Likewise, a data breach is not a "security investment" growth story; it is a
trust-break gate that can become hard 4C.
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


ROUND303_SOURCE_ROUND_PATH = "docs/round/round_303.md"
ROUND303_ANALYST_ROUND_ID = "round_231"
ROUND303_LARGE_SECTOR = "PLATFORM_CONTENT_SW_SECURITY"
ROUND303_METHOD = "trigger_level_backtest_v1"
ROUND303_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round303_r8_loop15_platform_content_sw_security_trigger_validation"
ROUND303_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r8_loop15_round231.jsonl"
ROUND303_DEFAULT_TRIGGERS_PATH = "data/e2r_trigger_calibration/triggers_r8_loop15_round231.jsonl"
ROUND303_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round303_r8_loop15_platform_content_sw_security_trigger_validation_audit.json"
ROUND303_DEFAULT_WEIGHT_PROFILE_PATH = "data/sector_taxonomy/score_weight_profiles_round231_r8_loop15_v1.csv"

ROUND303_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE": E2RArchetype.AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE.value,
    "AI_INFRA_PORTAL_STAGE2_ACTIONABLE": E2RArchetype.AI_INFRA_PORTAL_STAGE2_ACTIONABLE.value,
    "WEBTOON_IPO_CONTENT_PLATFORM_STAGE2": E2RArchetype.WEBTOON_IPO_CONTENT_PLATFORM_STAGE2.value,
    "CLOUD_AI_IT_SERVICES_EVIDENCE_GOOD_PRICE_FAILED": E2RArchetype.CLOUD_AI_IT_SERVICES_EVIDENCE_GOOD_PRICE_FAILED.value,
    "AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B": E2RArchetype.AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B.value,
    "GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE": E2RArchetype.GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE.value,
    "KPOP_ARTIST_GOVERNANCE_4C_WATCH": E2RArchetype.KPOP_ARTIST_GOVERNANCE_4C_WATCH.value,
    "CYBERSECURITY_DATA_BREACH_HARD_4C": E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C.value,
    "CONTENT_MA_IP_EXPANSION_STAGE2": E2RArchetype.CONTENT_MA_IP_EXPANSION_STAGE2.value,
}

ROUND303_STAGE2_ACTIONABLE_RULES: tuple[str, ...] = (
    "ai_partnership_connects_to_product_integration_or_infra_purchase",
    "cloud_ai_revenue_share_or_enterprise_order_path_is_numeric",
    "ipo_or_ma_has_mau_revenue_profit_ip_library_or_user_base",
    "event_day_market_relative_price_reaction_exceeds_5pp",
    "game_or_content_ip_has_sales_downloads_mau_retention_or_licensing",
    "enterprise_sw_has_backlog_recurring_revenue_margin_or_customer_wins",
    "security_or_data_risk_is_absent_or_controllable",
)

ROUND303_STAGE3_YELLOW_RULES: tuple[str, ...] = (
    "ai_product_or_content_trigger_changes_eps_op_fcf_path_but_one_gate_remains",
    "enterprise_order_backlog_or_cloud_margin_visible_but_durability_pending",
    "content_ip_monetization_visible_but_retention_or_parent_bridge_pending",
    "game_sellthrough_visible_but_live_service_retention_pending",
    "artist_governance_or_data_security_gate_not_hard_failed",
)

ROUND303_STAGE3_GREEN_RULES: tuple[str, ...] = (
    "paid_ai_usage_api_revenue_or_ad_uplift_is_visible",
    "cloud_ai_margin_and_enterprise_backlog_are_visible",
    "content_ip_recurring_revenue_or_licensing_is_visible",
    "game_retention_and_live_service_revenue_are_visible_after_launch",
    "mna_integration_revenue_synergy_is_visible",
    "artist_contract_governance_and_data_security_hard_gates_are_clear",
    "full_window_mfe_mae_is_available_and_supportive",
)

ROUND303_GREEN_BLOCKERS: tuple[str, ...] = (
    "ai_partnership_headline_only",
    "dominant_mau_without_paid_ai_usage",
    "ipo_pop_without_parent_monetization",
    "cloud_ai_sales_mix_without_order_backlog_or_margin",
    "cb_capital_injection_without_ai_order_backlog",
    "ip_acquisition_without_revenue_synergy",
    "game_ip_hype_without_retention",
    "artist_name_without_contract_control",
    "security_capex_after_breach_as_positive",
)

ROUND303_SCORE_UP_AXES: tuple[str, ...] = (
    "paid_AI_usage_conversion",
    "AI_cloud_margin_visibility",
    "enterprise_order_backlog",
    "content_IP_monetization",
    "game_sellthrough_and_retention",
    "global_IP_licensing",
    "platform_user_data_security",
    "artist_contract_governance",
    "M&A_integration_revenue",
    "AI_infra_capex_ROI",
)

ROUND303_SCORE_DOWN_AXES: tuple[str, ...] = (
    "AI_partnership_headline_only",
    "IPO_pop_without_parent_monetization",
    "cloud_AI_sales_mix_without_price_confirmation",
    "CB_capital_injection_without_order_backlog",
    "IP_acquisition_without_revenue_synergy",
    "game_IP_hype_without_retention",
    "artist_name_without_contract_control",
    "security_capex_after_breach_as_positive",
)

ROUND303_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "ai_partnership_headline_rerates_before_paid_usage",
    "ipo_pop_does_not_bridge_to_parent_eps_fcf",
    "cb_or_strategic_capital_price_pop_before_order_backlog",
    "game_or_ip_ma_is_priced_as_immediate_earnings",
    "artist_or_ip_sentiment_moves_price_without_contract_control",
    "security_remediation_capex_is_misread_as_growth_capex",
)

ROUND303_HARD_4C_GATES: tuple[str, ...] = (
    "data_breach_or_customer_data_leak",
    "regulatory_negligence_finding",
    "breach_related_revenue_forecast_cut",
    "customer_compensation_or_large_remediation_cost",
    "artist_contract_collapse_or_injunction_blocks_activity",
    "ai_data_privacy_violation",
    "cloud_or_security_failure_causes_enterprise_churn",
)


@dataclass(frozen=True)
class Round303ShadowWeightRow:
    archetype: E2RArchetype
    paid_ai_usage_conversion: int
    ai_cloud_margin_visibility: int
    enterprise_order_backlog: int
    content_ip_monetization: int
    game_sellthrough_retention: int
    global_ip_licensing: int
    platform_user_data_security: int
    artist_contract_governance: int
    ma_integration_revenue: int
    ai_infra_capex_roi: int
    ai_partnership_headline_only_penalty: int
    ipo_pop_without_parent_monetization_penalty: int
    cloud_ai_mix_without_price_confirmation_penalty: int
    cb_capital_without_backlog_penalty: int
    stage2_actionable_promote: str
    stage3_yellow_gate: str
    stage3_green_gate: str
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "paid_ai_usage_conversion": _signed(self.paid_ai_usage_conversion),
            "ai_cloud_margin_visibility": _signed(self.ai_cloud_margin_visibility),
            "enterprise_order_backlog": _signed(self.enterprise_order_backlog),
            "content_ip_monetization": _signed(self.content_ip_monetization),
            "game_sellthrough_retention": _signed(self.game_sellthrough_retention),
            "global_ip_licensing": _signed(self.global_ip_licensing),
            "platform_user_data_security": _signed(self.platform_user_data_security),
            "artist_contract_governance": _signed(self.artist_contract_governance),
            "ma_integration_revenue": _signed(self.ma_integration_revenue),
            "ai_infra_capex_roi": _signed(self.ai_infra_capex_roi),
            "ai_partnership_headline_only_penalty": _signed(self.ai_partnership_headline_only_penalty),
            "ipo_pop_without_parent_monetization_penalty": _signed(self.ipo_pop_without_parent_monetization_penalty),
            "cloud_ai_mix_without_price_confirmation_penalty": _signed(self.cloud_ai_mix_without_price_confirmation_penalty),
            "cb_capital_without_backlog_penalty": _signed(self.cb_capital_without_backlog_penalty),
            "stage2_actionable_promote": self.stage2_actionable_promote,
            "stage3_yellow_gate": self.stage3_yellow_gate,
            "stage3_green_gate": self.stage3_green_gate,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round303TriggerRecord:
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
class Round303CaseCandidate:
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
            "do_not_use_round303_cases_as_candidate_generation_input",
            "do_not_treat_ai_partnership_ipo_cb_ip_or_security_capex_headline_as_green",
        ]
        if not self.hard_4c_confirmed:
            guardrails.append("hard_4c_confirmed_false")
        return E2RCaseRecord(
            case_id=self.case_id,
            symbol=self.symbol,
            company_name=self.company_name,
            market="KR",
            sector_raw=ROUND303_LARGE_SECTOR,
            large_sector=ROUND303_LARGE_SECTOR,
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
            must_have_fields=ROUND303_STAGE2_ACTIONABLE_RULES + ROUND303_STAGE3_YELLOW_RULES + ROUND303_STAGE3_GREEN_RULES,
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
                mfe_30d=self.event_mfe_pct if self.event_mfe_pct and self.event_mfe_pct > 0 else None,
                mae_30d=self.event_mae_pct if self.event_mae_pct and self.event_mae_pct < 0 else None,
                price_validation_status="reported_event_anchor_not_full_ohlc",
            ),
            data_quality=CaseDataQuality(False, True, False, 0.68),
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


ROUND303_SHADOW_WEIGHT_ROWS: tuple[Round303ShadowWeightRow, ...] = (
    Round303ShadowWeightRow(E2RArchetype.AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE, 5, 4, 2, 1, 0, 0, 4, 2, 1, 3, -5, -2, -2, -2, "AI partnership+dominant messenger base", "paid usage/ad uplift missing", "paid usage+retention+margin", "Kakao/OpenAI is Stage2, not Green."),
    Round303ShadowWeightRow(E2RArchetype.AI_INFRA_PORTAL_STAGE2_ACTIONABLE, 5, 5, 4, 3, 0, 0, 4, 1, 2, 5, -4, -3, -2, -2, "AI infra purchase+portal base", "capex ROI missing", "AI revenue+margin+retention", "Naver Blackwell trigger is Stage2."),
    Round303ShadowWeightRow(E2RArchetype.WEBTOON_IPO_CONTENT_PLATFORM_STAGE2, 1, 1, 1, 5, 0, 5, 2, 2, 2, 0, -2, -4, -1, -1, "MAU+IPO+profitability", "post-listing durability missing", "parent monetization+IP revenue", "Webtoon IPO pop is not parent Green."),
    Round303ShadowWeightRow(E2RArchetype.CLOUD_AI_IT_SERVICES_EVIDENCE_GOOD_PRICE_FAILED, 2, 5, 5, 0, 0, 0, 4, 1, 3, 4, -3, -2, -4, -2, "cloud/AI sales mix", "weak price/backlog missing", "backlog+margin expansion", "LG CNS remains evidence-good price-failed."),
    Round303ShadowWeightRow(E2RArchetype.AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B, 3, 5, 5, 0, 0, 0, 4, 1, 4, 4, -3, -2, -2, -4, "strategic capital+AI/M&A", "CB/backlog missing", "order backlog+margin+M&A execution", "Samsung SDS Stage2+4B."),
    Round303ShadowWeightRow(E2RArchetype.GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE, 0, 0, 0, 4, 5, 4, 2, 2, 4, 0, -2, -2, -1, -1, "game IP sales/ranking", "retention/new title missing", "recurring revenue+retention", "Krafton/Shift Up game IP Stage2."),
    Round303ShadowWeightRow(E2RArchetype.KPOP_ARTIST_GOVERNANCE_4C_WATCH, 0, 0, 0, 5, 0, 5, 1, 5, 1, 0, -2, -2, -1, -1, "artist IP governance dispute", "contract resolution pending", "artist schedule+revenue stability", "HYBE/NewJeans is 4C-watch."),
    Round303ShadowWeightRow(E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C, 0, 2, 2, 0, 0, 0, 5, 2, 0, 1, -1, -1, -1, -1, "data breach/customer trust", "trust recovery pending", "security proven+churn controlled", "SKT breach is hard 4C."),
    Round303ShadowWeightRow(E2RArchetype.CONTENT_MA_IP_EXPANSION_STAGE2, 0, 0, 1, 5, 3, 5, 2, 2, 5, 0, -2, -2, -1, -2, "IP acquisition/library", "synergy revenue missing", "new IP revenue+licensing", "Krafton ADK Stage2."),
)

ROUND303_TRIGGER_RECORDS: tuple[Round303TriggerRecord, ...] = (
    Round303TriggerRecord("r8l15_kakao_openai_T1", "r8_loop15_kakao_openai_ai_messaging", "Stage2-Actionable", date(2025, 2, 4), "OpenAI-Kakao AI product partnership, KakaoTalk 97% domestic messaging share, initial +9% then -2% close", "initial +9 / close -2", "evidence_good_but_price_failed", "Stage2-Actionable_only", {"kakaotalk_domestic_share_pct": 97, "initial_event_mfe_pct": 9, "close_event_return_pct": -2}),
    Round303TriggerRecord("r8l15_naver_webtoon_T2", "r8_loop15_naver_webtoon_nvidia_ai_infra", "Stage2-Actionable", date(2024, 6, 27), "Webtoon IPO priced at $21, raised $315M, 170M MAU, debut +14.3%", 14.3, "Stage2_promote_candidate", "Stage2-Actionable", {"webtoon_maus_mn": 170, "webtoon_ipo_raise_usd_mn": 315, "webtoon_debut_mfe_pct": 14.3}),
    Round303TriggerRecord("r8l15_naver_blackwell_T3", "r8_loop15_naver_webtoon_nvidia_ai_infra", "Stage2_AI_infra", date(2025, 10, 31), "Naver to buy 60,000 Nvidia Blackwell chips; Korea total 260,000 chips", "price_data_unavailable_after_deep_search", "Stage2_AI_infra", "Stage2", {"naver_blackwell_chip_purchase_units": 60000, "korea_total_blackwell_chips_units": 260000}),
    Round303TriggerRecord("r8l15_lgcns_ipo_T1", "r8_loop15_lg_cns_cloud_ai_ipo", "evidence_good_but_price_failed", date(2025, 2, 5), "Cloud/AI 54% of sales, IPO raised 1.2T won, but debut traded below 61,900 won issue price at 59,700 won", -3.55, "evidence_good_but_price_failed", "Stage2_only", {"cloud_ai_sales_share_pct": 54, "debut_return_vs_issue_pct": -3.55}),
    Round303TriggerRecord("r8l15_samsungsds_kkr_T1", "r8_loop15_samsung_sds_kkr_cb_ai", "Stage2-Actionable+4B-watch", date(2026, 4, 15), "KKR buys $820M Samsung SDS CB; shares +20.8%; AI/M&A/capital allocation advisory", 20.8, "Stage2_promote_candidate_with_4B_overlay", "Stage2-Actionable", {"convertible_bond_value_usd_mn": 820, "market_relative_return_pp": 17.8}),
    Round303TriggerRecord("r8l15_krafton_adk_T1", "r8_loop15_krafton_adk_india_ip_expansion", "Stage2-Actionable", date(2025, 6, 24), "Krafton to buy ADK for 75B yen / $516M; 300+ animation productions including Doraemon/Yu-Gi-Oh!/Crayon Shin-chan", "price_data_unavailable_after_deep_search", "Stage2_IP_expansion", "Stage2-Actionable", {"adk_acquisition_value_usd_mn": 516.21, "adk_animation_productions_count": 300}),
    Round303TriggerRecord("r8l15_shiftup_ipo_T1", "r8_loop15_shiftup_ipo_stellarblade_nikke", "Stage2-Actionable", date(2024, 6, 27), "Shift Up IPO expected top range, 435B won raise, 3.5T won valuation, Nikke 255B won sales, Stellar Blade PS rankings", "price_data_unavailable_after_deep_search", "Stage2_game_IP", "Stage2-Actionable", {"ipo_raise_krw_bn": 435, "nikke_sales_krw_bn": 255}),
    Round303TriggerRecord("r8l15_hybe_newjeans_T0", "r8_loop15_hybe_newjeans_sm_tencent_kpop_governance", "4C-watch", date(2024, 4, 24), "HYBE audits ADOR over independence/control allegations; shares fell nearly 8%", -8.0, "artist_governance_4C_watch", "4C-watch", {"hybe_audit_event_mae_pct": -8}),
    Round303TriggerRecord("r8l15_skt_breach_T0", "r8_loop15_skt_data_breach_security_4c", "hard_4C", date(2025, 4, 28), "SK Telecom malware data leak; free USIM replacement for 23M users; shares closed -6.7% vs KOSPI +0.1%", -6.7, "hard_4c_success", "4C", {"subscribers_affected_context_mn": 23, "market_relative_return_pp": -6.8}),
    Round303TriggerRecord("r8l15_skt_breach_T1", "r8_loop15_skt_data_breach_security_4c", "hard_4C_validation", date(2025, 7, 4), "Regulator found SKT negligent; 26.96M data pieces leaked; shares -5.6%; 700B won security investment; 800B won revenue forecast cut", -5.6, "hard_4c_validated", "4C", {"data_pieces_leaked_mn": 26.96, "security_investment_5y_krw_bn": 700, "revenue_forecast_cut_2025_krw_bn": 800}),
)

ROUND303_CASE_CANDIDATES: tuple[Round303CaseCandidate, ...] = (
    Round303CaseCandidate("r8_loop15_kakao_openai_ai_messaging", "035720", "Kakao", E2RArchetype.AI_MESSAGING_PARTNERSHIP_STAGE2_WITH_MONETIZATION_GATE, (E2RArchetype.AI_SOFTWARE_PARTNERSHIP_EVENT, E2RArchetype.PLATFORM_PRIVACY_SECURITY_OVERLAY), "success_candidate", "Stage2_Actionable_but_evidence_good_price_failed", "T1/T2", "Stage2-Actionable_with_monetization_gate", "Stage2-Actionable", date(2025, 2, 4), date(2025, 2, 4), None, date(2025, 2, 4), None, False, ("OpenAI_partnership", "KakaoTalk_97pct_domestic_share", "AI_product_integration"), ("paid_AI_usage_missing", "retention_missing", "ad_uplift_missing", "API_cloud_margin_missing", "data_privacy_clearance_missing", "initial_pop_faded_to_negative_close"), 9.0, -2.0, {"kakaotalk_domestic_share_pct": 97, "initial_event_mfe_pct": 9, "close_event_return_pct": -2}, "evidence_good_but_price_failed", "AI_partnership_monetization_gate", "unknown", "stage2_watch_success", "OpenAI headline and KakaoTalk base are Stage2-Actionable, but paid usage and ad uplift are not confirmed."),
    Round303CaseCandidate("r8_loop15_naver_webtoon_nvidia_ai_infra", "035420/WBTN", "Naver / Webtoon Entertainment", E2RArchetype.AI_INFRA_PORTAL_STAGE2_ACTIONABLE, (E2RArchetype.WEBTOON_IPO_CONTENT_PLATFORM_STAGE2, E2RArchetype.GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN), "success_candidate", "Stage2_promote_candidate", "T2/T3", "Stage2-Actionable_content_AI_infra", "Stage2-Actionable", date(2024, 6, 27), date(2024, 6, 27), None, None, None, False, ("Webtoon_170M_MAU", "Webtoon_Q1_revenue_326_7M_USD", "IPO_315M_USD", "IPO_debut_plus_14_3pct", "Naver_60000_Blackwell_chips"), ("parent_level_monetization_missing", "AI_search_ad_uplift_missing", "cloud_margin_missing", "capex_ROI_missing"), 14.3, None, {"webtoon_maus_mn": 170, "webtoon_q1_revenue_usd_mn": 326.7, "webtoon_q1_net_income_usd_mn": 6.2, "webtoon_ipo_raise_usd_mn": 315, "webtoon_ipo_valuation_usd_bn": 2.67, "webtoon_debut_mfe_pct": 14.3, "naver_blackwell_chip_purchase_units": 60000}, "missed_due_to_score", "Stage2_promote_candidate", "event_premium", "stage2_watch_success", "Webtoon IPO and Naver AI infra are Stage2-Actionable; Green needs parent-level AI/content monetization."),
    Round303CaseCandidate("r8_loop15_lg_cns_cloud_ai_ipo", "LG_CNS", "LG CNS", E2RArchetype.CLOUD_AI_IT_SERVICES_EVIDENCE_GOOD_PRICE_FAILED, (E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE, E2RArchetype.CLOUD_AI_SOFTWARE_INFRA), "failed_rerating", "evidence_good_but_price_failed", "T1/T2", "Stage2_only", "Stage2", date(2025, 2, 5), date(2025, 2, 5), None, date(2025, 2, 5), None, False, ("cloud_AI_sales_share_54pct", "IPO_raise_1_2T_KRW", "OP_313B_KRW"), ("weak_IPO_debut", "enterprise_AI_order_backlog_missing", "cloud_margin_missing", "M&A_execution_missing"), None, -3.55, {"ipo_issue_price_krw": 61900, "debut_last_reported_price_krw": 59700, "debut_return_vs_issue_pct": -3.55, "cloud_ai_sales_share_3q2024_pct": 54, "revenue_3q2024_krw_trn": 4.0, "op_3q2024_krw_bn": 313}, "evidence_good_but_price_failed", "cloud_AI_mix_weak_price", "no_rerating", "false_yellow", "Cloud/AI sales mix was real, but weak debut blocks any Green interpretation."),
    Round303CaseCandidate("r8_loop15_samsung_sds_kkr_cb_ai", "018260", "Samsung SDS", E2RArchetype.AI_SOFTWARE_CB_STRATEGIC_CAPITAL_STAGE2_WITH_4B, (E2RArchetype.CLOUD_AI_SOFTWARE_INFRA, E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY), "success_candidate", "Stage2_Actionable_with_4B_overlay", "T1/T2", "Stage2-Actionable+4B-watch", "Stage2-Actionable + 4B-watch", date(2026, 4, 15), date(2026, 4, 15), None, date(2026, 4, 15), None, False, ("KKR_820M_USD_convertible_bond", "event_return_plus_20_8pct", "AI_infrastructure_strategy", "M&A_advisory", "cash_6_4T_KRW"), ("CB_dilution_absorption_missing", "AI_order_backlog_missing", "M&A_closure_missing", "margin_expansion_missing"), 20.8, None, {"convertible_bond_value_usd_mn": 820, "event_mfe_pct": 20.8, "market_relative_return_pp": 17.8, "cash_and_equivalents_krw_trn": 6.4}, "missed_due_to_score", "Stage2_promote_candidate_with_4B_overlay", "event_premium", "stage2_watch_success", "KKR strategic capital is actionable, but CB/dilution and backlog gates remain."),
    Round303CaseCandidate("r8_loop15_krafton_adk_india_ip_expansion", "259960", "Krafton", E2RArchetype.CONTENT_MA_IP_EXPANSION_STAGE2, (E2RArchetype.GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE, E2RArchetype.EMERGING_MARKET_GAME_PLATFORM_OPTION), "success_candidate", "Stage2_promote_candidate", "T1/T3", "Stage2-Actionable_IP_geography", "Stage2-Actionable", date(2025, 6, 24), date(2025, 6, 24), None, None, None, False, ("ADK_516M_USD_acquisition", "ADK_300_plus_animation_library", "India_fund_666M_USD", "BGMI_240M_downloads"), ("ADK_integration_missing", "new_IP_revenue_missing", "India_fund_return_missing", "BGMI_data_security_regulatory_history"), None, None, {"adk_acquisition_value_jpy_bn": 75, "adk_acquisition_value_usd_mn": 516.21, "adk_animation_productions_count": 300, "india_fund_target_usd_mn": 666, "bgmi_downloads_mn": 240}, "aligned", "Stage2_IP_expansion", "unknown", "stage2_watch_success", "ADK and India fund expand IP/geography; integration and regulatory stability remain gates."),
    Round303CaseCandidate("r8_loop15_shiftup_ipo_stellarblade_nikke", "462870", "Shift Up", E2RArchetype.GAME_IP_GLOBALIZATION_STAGE2_ACTIONABLE, (E2RArchetype.GAME_IP_IPO_STAGE2_QUALITY_GATE, E2RArchetype.GAME_IP_IPO_SINGLE_TITLE_RISK), "success_candidate", "Stage2_promote_candidate", "T1/T2", "Stage2-Actionable_game_IP", "Stage2-Actionable", date(2024, 6, 27), date(2024, 6, 27), None, date(2024, 6, 27), None, False, ("IPO_raise_435B_KRW", "Nikke_sales_255B_KRW", "Stellar_Blade_Japan_rank_1", "Stellar_Blade_North_America_rank_2", "OP_2023_111B_KRW"), ("post_IPO_durability_missing", "IP_concentration_missing", "live_service_retention_missing", "Tencent_ownership_overlay"), None, None, {"ipo_raise_krw_bn": 435, "expected_market_cap_krw_trn": 3.5, "tencent_pre_ipo_stake_pct": 40, "nikke_sales_krw_bn": 255, "op_2023_krw_bn": 111, "stellar_blade_japan_ps_download_rank": 1, "stellar_blade_north_america_ps_download_rank": 2}, "missed_due_to_score", "Stage2_game_IP_not_Green", "event_premium", "stage2_watch_success", "Nikke sales, Stellar Blade ranking and IPO valuation support Stage2; Green needs post-IPO durability."),
    Round303CaseCandidate("r8_loop15_hybe_newjeans_sm_tencent_kpop_governance", "352820/041510/035720", "HYBE / NewJeans / SM / Tencent / Kakao", E2RArchetype.KPOP_ARTIST_GOVERNANCE_4C_WATCH, (E2RArchetype.KPOP_IP_CONTRACT_GOVERNANCE_4C, E2RArchetype.KPOP_IP_CHINA_OPTIONALITY), "4b_watch", "artist_governance_4C_watch_plus_Stage2_China_optionality", "T0/T1/T2", "4C-watch / Stage2 China optionality", "4C-watch", date(2024, 4, 24), None, None, date(2024, 4, 24), date(2025, 3, 21), False, ("HYBE_ADOR_audit", "NewJeans_activity_injunction", "Tencent_SM_9_7pct_stake", "China_Kpop_thaw_optionality"), ("artist_contract_control_missing", "court_injunction_blocks_activities", "label_governance_break", "China_ticket_revenue_missing"), None, -8.0, {"hybe_audit_event_mae_pct": -8, "court_injunction_date": "2025-03-21", "sm_tencent_transaction_date": "2025-05-27", "sm_stake_sold_pct": 9.7, "sm_stake_sale_value_krw_bn": 243, "kakao_sm_control_stake_pct": 42}, "unknown", "artist_governance_4C_watch", "thesis_break", "should_have_been_red", "Artist IP governance is 4C-watch; China optionality stays Stage2 until concerts and ticket revenue confirm."),
    Round303CaseCandidate("r8_loop15_skt_data_breach_security_4c", "017670", "SK Telecom", E2RArchetype.CYBERSECURITY_DATA_BREACH_HARD_4C, (E2RArchetype.CYBERSECURITY_TRUST_HARD_4C_REFERENCE, E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C), "4c_thesis_break", "hard_4c_reference", "T0/T1/T2", "hard_4C", "4C", date(2025, 4, 28), None, None, date(2025, 4, 28), date(2025, 7, 4), True, ("data_breach", "26_96M_data_pieces_leaked", "regulatory_negligence", "700B_KRW_security_investment", "800B_KRW_revenue_forecast_cut"), ("customer_data_leak", "trust_loss", "customer_compensation", "revenue_forecast_cut", "regulatory_negligence_finding"), None, -6.7, {"t0_intraday_mae_pct": -8.5, "t0_close_return_pct": -6.7, "data_pieces_leaked_mn": 26.96, "security_investment_5y_krw_bn": 700, "revenue_forecast_cut_2025_krw_bn": 800, "customer_benefit_package_cost_krw_bn": 500, "usim_replacements_by_late_june_mn": 9.39}, "false_positive_score", "hard_4c_success", "thesis_break", "should_have_been_red", "Data breach is R8 hard 4C; security investment after breach is trust-repair cost, not growth capex."),
)


def round303_case_records() -> tuple[E2RCaseRecord, ...]:
    return tuple(case.to_case_record() for case in ROUND303_CASE_CANDIDATES)


def round303_summary() -> dict[str, object]:
    return {
        "source_round": ROUND303_SOURCE_ROUND_PATH,
        "round_id": ROUND303_ANALYST_ROUND_ID,
        "large_sector": ROUND303_LARGE_SECTOR,
        "method": ROUND303_METHOD,
        "case_candidate_count": len(ROUND303_CASE_CANDIDATES),
        "trigger_count": len(ROUND303_TRIGGER_RECORDS),
        "stage2_actionable_candidate_count": 5,
        "stage2_only_candidate_count": 1,
        "stage3_yellow_candidate_count": 0,
        "stage3_green_candidate_count": 0,
        "stage3_green_confirmed_count": 0,
        "stage4b_watch_count": 4,
        "stage4c_watch_count": 2,
        "hard_4c_case_count": 1,
        "price_validation_completed": "partial_with_reported_event_price_anchors",
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "full_adjusted_ohlc_complete": False,
        "shadow_weight_only": True,
    }


def round303_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(case.as_row() for case in ROUND303_CASE_CANDIDATES)


def round303_trigger_rows() -> tuple[dict[str, str], ...]:
    return tuple(trigger.as_row() for trigger in ROUND303_TRIGGER_RECORDS)


def round303_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"requested_alias": key, "canonical_archetype": value} for key, value in ROUND303_REQUIRED_TARGET_ALIASES.items())


def round303_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND303_SHADOW_WEIGHT_ROWS)


def round303_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    up_points = {
        "paid_AI_usage_conversion": "+5",
        "AI_cloud_margin_visibility": "+5",
        "enterprise_order_backlog": "+5",
        "content_IP_monetization": "+5",
        "game_sellthrough_and_retention": "+5",
        "global_IP_licensing": "+4",
        "platform_user_data_security": "+5",
        "artist_contract_governance": "+5",
        "M&A_integration_revenue": "+4",
        "AI_infra_capex_ROI": "+5",
    }
    down_points = {
        "AI_partnership_headline_only": "-5",
        "IPO_pop_without_parent_monetization": "-4",
        "cloud_AI_sales_mix_without_price_confirmation": "-4",
        "CB_capital_injection_without_order_backlog": "-4",
        "IP_acquisition_without_revenue_synergy": "-4",
        "game_IP_hype_without_retention": "-5",
        "artist_name_without_contract_control": "-5",
        "security_capex_after_breach_as_positive": "-5",
    }
    rows = []
    for axis in ROUND303_SCORE_UP_AXES:
        rows.append({"axis": axis, "points": up_points[axis], "direction": "raise", "reason": "R8 platform/content/SW/security trigger quality axis"})
    for axis in ROUND303_SCORE_DOWN_AXES:
        rows.append({"axis": axis, "points": down_points[axis], "direction": "lower", "reason": "R8 headline, IPO, CB, IP or breach false-positive blocker"})
    return tuple(rows)


def round303_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND303_SOURCE_ROUND_PATH,
        "round_id": ROUND303_ANALYST_ROUND_ID,
        "large_sector": ROUND303_LARGE_SECTOR,
        "method": ROUND303_METHOD,
        "summary": round303_summary(),
        "target_archetypes": dict(ROUND303_REQUIRED_TARGET_ALIASES),
        "stage2_actionable_rules": list(ROUND303_STAGE2_ACTIONABLE_RULES),
        "stage3_yellow_rules": list(ROUND303_STAGE3_YELLOW_RULES),
        "stage3_green_rules": list(ROUND303_STAGE3_GREEN_RULES),
        "green_blockers": list(ROUND303_GREEN_BLOCKERS),
        "score_up_axes": list(ROUND303_SCORE_UP_AXES),
        "score_down_axes": list(ROUND303_SCORE_DOWN_AXES),
        "stage4b_watch_triggers": list(ROUND303_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND303_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_apply_round303_shadow_weights_to_production_scoring_yet",
            "do_not_use_round303_cases_as_candidate_generation_input",
            "do_not_treat_ai_partnership_ipo_cb_ip_or_security_capex_headline_as_green",
            "do_not_downgrade_stage_candidate_only_because_full_ohlc_is_missing",
        ],
    }


def render_round303_summary_markdown() -> str:
    summary = round303_summary()
    lines = [
        "# Round 303 R8 Loop 15 Platform/Content/SW/Security Trigger Validation",
        "",
        "이번 라운드는 AI 제휴, 콘텐츠 IPO, 게임/IP M&A, K-pop 거버넌스, 데이터 유출을 같은 플랫폼 테마로 묶지 않고 trigger별로 분리한다.",
        "",
        "쉬운 예: `OpenAI 제휴`는 문을 두드린 신호다. Green은 실제 유료 사용, 광고 매출, 마진이 확인될 때다. 반대로 `데이터 유출`은 성장 투자가 아니라 신뢰 훼손 4C 게이트다.",
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
        "stage2_only_candidate_count",
        "stage3_yellow_candidate_count",
        "stage3_green_confirmed_count",
        "stage4b_watch_count",
        "stage4c_watch_count",
        "hard_4c_case_count",
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
            "- Kakao/OpenAI는 Stage2-Actionable이지만 paid usage, retention, ad uplift, API/cloud margin 전에는 Green이 아니다.",
            "- Naver/Webtoon/Nvidia AI infra는 Stage2-Actionable이다. Webtoon IPO pop과 Blackwell chip purchase는 강하지만 parent-level monetization이 필요하다.",
            "- LG CNS는 cloud/AI sales mix가 있어도 weak IPO debut 때문에 evidence_good_but_price_failed다.",
            "- Samsung SDS/KKR CB는 Stage2-Actionable + 4B-watch다. +20.8% trigger는 강하지만 CB dilution과 order backlog gate가 남아 있다.",
            "- Krafton/ADK/India fund와 Shift Up은 game/content IP Stage2-Actionable이다. Integration, retention, new-IP revenue가 Green gate다.",
            "- HYBE/NewJeans는 artist governance 4C-watch다. SM/Tencent China optionality는 별도 Stage2 후보일 뿐이다.",
            "- SK Telecom data breach는 hard 4C다. 보안투자는 성장 capex가 아니라 trust-repair cost로 기록한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round303_trigger_grid_markdown() -> str:
    lines = [
        "# Round 303 Trigger Grid",
        "",
        "| trigger_id | case_id | date | type | outcome | promote_to | evidence |",
        "|---|---|---|---|---|---|---|",
    ]
    for trigger in ROUND303_TRIGGER_RECORDS:
        lines.append(
            f"| {trigger.trigger_id} | {trigger.case_id} | {trigger.trigger_date.isoformat()} | {trigger.trigger_type} | {trigger.trigger_outcome_label} | {trigger.promote_to} | {trigger.evidence_available} |"
        )
    return "\n".join(lines) + "\n"


def render_round303_stage_rules_markdown() -> str:
    lines = ["# Round 303 Stage Rules", "", "Do not apply these weights to production scoring yet.", "", "## Stage2-Actionable", ""]
    lines.extend(f"- {rule}" for rule in ROUND303_STAGE2_ACTIONABLE_RULES)
    lines.extend(["", "## Stage3-Yellow", ""])
    lines.extend(f"- {rule}" for rule in ROUND303_STAGE3_YELLOW_RULES)
    lines.extend(["", "## Stage3-Green", ""])
    lines.extend(f"- {rule}" for rule in ROUND303_STAGE3_GREEN_RULES)
    lines.extend(["", "## Green Blockers", ""])
    lines.extend(f"- {rule}" for rule in ROUND303_GREEN_BLOCKERS)
    return "\n".join(lines) + "\n"


def render_round303_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 303 4B/4C Review",
        "",
        "이번 라운드에서 Stage3-Green 확정은 없다. AI/IPO/CB/IP headline의 4B-watch와 데이터 유출 hard 4C를 분리한다.",
        "",
        "## 4B Watch",
        "",
    ]
    lines.extend(f"- {item}" for item in ROUND303_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {item}" for item in ROUND303_HARD_4C_GATES)
    lines.extend(["", "## Confirmed Hard 4C", "", "- SK Telecom data breach"])
    return "\n".join(lines) + "\n"


def render_round303_price_validation_plan_markdown() -> str:
    return "\n".join(
        [
            "# Round 303 Price Validation Plan",
            "",
            "- reported_event_anchor_not_full_ohlc 상태를 유지한다.",
            "- full adjusted OHLC가 없다는 이유로 Stage2-Actionable 또는 4C 후보를 강등하지 않는다.",
            "- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.",
            "- 다음 단계에서는 trigger date 기준 30/90/180일 MFE/MAE, below-entry, paid AI usage, cloud margin, IP retention, artist contract stability, breach churn/cost를 채운다.",
            "",
        ]
    )


def write_round303_r8_loop15_reports(
    *,
    output_directory: str | Path = ROUND303_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND303_DEFAULT_CASES_PATH,
    triggers_path: str | Path = ROUND303_DEFAULT_TRIGGERS_PATH,
    audit_path: str | Path = ROUND303_DEFAULT_AUDIT_PATH,
    weight_profile_path: str | Path = ROUND303_DEFAULT_WEIGHT_PROFILE_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round303_case_records(), cases_path),
        "triggers": write_round303_triggers(triggers_path),
        "audit": _write_json(round303_audit_payload(), audit_path),
        "weight_profile": _write_csv(round303_shadow_weight_rows(), weight_profile_path),
        "summary": output / "round303_r8_loop15_trigger_validation_summary.md",
        "case_matrix": output / "round303_r8_loop15_case_matrix.csv",
        "trigger_grid": output / "round303_r8_loop15_trigger_grid.csv",
        "target_aliases": output / "round303_r8_loop15_target_aliases.csv",
        "score_adjustments": output / "round303_r8_loop15_score_adjustments.csv",
        "shadow_weights": output / "round303_r8_loop15_shadow_weights.csv",
        "stage_rules": output / "round303_r8_loop15_stage_rules.md",
        "trigger_grid_md": output / "round303_r8_loop15_trigger_grid.md",
        "price_validation_plan": output / "round303_r8_loop15_price_validation_plan.md",
        "stage4b_4c_review": output / "round303_r8_loop15_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round303_summary_markdown(), encoding="utf-8")
    _write_csv(round303_case_rows(), paths["case_matrix"])
    _write_csv(round303_trigger_rows(), paths["trigger_grid"])
    _write_csv(round303_target_alias_rows(), paths["target_aliases"])
    _write_csv(round303_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round303_shadow_weight_rows(), paths["shadow_weights"])
    paths["stage_rules"].write_text(render_round303_stage_rules_markdown(), encoding="utf-8")
    paths["trigger_grid_md"].write_text(render_round303_trigger_grid_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round303_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round303_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def write_round303_triggers(path: str | Path = ROUND303_DEFAULT_TRIGGERS_PATH) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(trigger.as_dict(), ensure_ascii=False, sort_keys=True) for trigger in ROUND303_TRIGGER_RECORDS]
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
    if value > 0:
        return f"+{value}"
    return str(value)
