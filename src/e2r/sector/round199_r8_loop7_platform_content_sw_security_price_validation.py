"""Round-199 R8 Loop-7 platform/content/SW/security price-path validation pack.

Round 199 is a calibration-only layer for Korean B2B SaaS, AI cloud, platform
AI, webtoon/IP, game IP, IPO/single-IP, K-pop governance, and operational trust
cases. It records why AI feature launches, partnerships, MAU, first-week game
sales, IPO moves, and M&A headlines must be separated from ARR, bookings, paid
usage, ARPU, retention/churn, OPM, FCF, repeat monetization, governance, privacy,
and security trust.

Simple example: an OpenAI partnership can be Stage 1 or Stage 2 attention. It
is not Stage 3-Green until paid AI usage, ARPU, margin, and durable platform
economics are visible as-of the case date.

This module is report/evaluation material only. Production candidate
generation, feature engineering, scoring, staging, and RedTeam code must not
import it.
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
from e2r.sector.round10_theme_tag_taxonomy import Round10LargeSector


ROUND199_SOURCE_ROUND_PATH = "docs/round/round_199.md"
ROUND199_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round199_r8_loop7_platform_content_sw_security_price_validation"
ROUND199_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r8_loop7_round199.jsonl"
ROUND199_DEFAULT_AUDIT_PATH = (
    "data/sector_taxonomy/round199_r8_loop7_platform_content_sw_security_price_validation_audit.json"
)

ROUND199_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "B2B_SAAS_ERP_WORKFLOW": E2RArchetype.B2B_SAAS_ERP_WORKFLOW.value,
    "B2B_SAAS_ERP_WORKFLOW_KOREA": E2RArchetype.B2B_SAAS_ERP_WORKFLOW_KOREA.value,
    "PRIVATE_EQUITY_SOFTWARE_RERATING": E2RArchetype.PRIVATE_EQUITY_SOFTWARE_RERATING.value,
    "CLOUD_AI_SOFTWARE_INFRA": E2RArchetype.CLOUD_AI_SOFTWARE_INFRA.value,
    "ENTERPRISE_AI_CLOUD_INFRA_KOREA": E2RArchetype.ENTERPRISE_AI_CLOUD_INFRA_KOREA.value,
    "AI_CLOUD_CAPITAL_ALLOCATION": E2RArchetype.AI_CLOUD_CAPITAL_ALLOCATION.value,
    "EDGE_AI_CLOUD_INFRASTRUCTURE": E2RArchetype.EDGE_AI_CLOUD_INFRASTRUCTURE.value,
    "AI_SOFTWARE_APPLICATION": E2RArchetype.AI_SOFTWARE_APPLICATION.value,
    "SOVEREIGN_KOREAN_AI_MODEL": E2RArchetype.SOVEREIGN_KOREAN_AI_MODEL.value,
    "PLATFORM_SOFTWARE_INTERNET": E2RArchetype.PLATFORM_SOFTWARE_INTERNET.value,
    "WEBTOON_PLATFORM_IP_MONETIZATION": E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION.value,
    "GAME_CONTENT_IP": E2RArchetype.GAME_CONTENT_IP.value,
    "GAME_CONTENT_IP_REPEAT_MONETIZATION": E2RArchetype.GAME_CONTENT_IP_REPEAT_MONETIZATION.value,
    "SINGLE_IP_RELEASE_EVENT_PREMIUM": E2RArchetype.SINGLE_IP_RELEASE_EVENT_PREMIUM.value,
    "GAME_SINGLE_IP_EVENT_PREMIUM": E2RArchetype.GAME_SINGLE_IP_EVENT_PREMIUM.value,
    "KPOP_PLATFORM_CONTENT_IP": E2RArchetype.KPOP_PLATFORM_CONTENT_IP.value,
    "PLATFORM_GOVERNANCE_LEGAL_RISK": E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK.value,
    "PLATFORM_PRIVACY_SECURITY_OVERLAY": E2RArchetype.PLATFORM_PRIVACY_SECURITY_OVERLAY.value,
    "SECURITY_OPERATIONAL_TRUST_OVERLAY": E2RArchetype.SECURITY_OPERATIONAL_TRUST_OVERLAY.value,
    "AD_CONTENT_PLATFORM_GUIDANCE_RISK": E2RArchetype.AD_CONTENT_PLATFORM_GUIDANCE_RISK.value,
    "DISCLOSURE_CONFIDENCE_CAP": E2RArchetype.DISCLOSURE_CONFIDENCE_CAP.value,
}

ROUND199_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "recurring_revenue_or_bookings_confirmed",
    "arr_arpu_paid_usage_or_billings_confirmed",
    "opm_or_gross_margin_improving",
    "fcf_conversion_visible",
    "retention_or_churn_stable",
    "ip_monetization_beyond_single_launch",
    "ai_feature_converts_to_paid_revenue_or_cost_savings",
    "privacy_security_governance_trust_passed",
    "price_path_after_repeat_economics",
)

ROUND199_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ai_feature_only",
    "partnership_headline_only",
    "model_release_or_paper_only",
    "mau_without_arpu",
    "game_launch_first_week_only",
    "ipo_first_month_rally",
    "mna_announcement_only",
    "single_ip_dependence_without_repeat_monetization",
    "ai_capex_without_revenue",
    "founder_legal_risk",
    "privacy_or_security_trust_break",
)

ROUND199_STAGE4B_STATUSES: tuple[str, ...] = ("none", "watch", "elevated", "graduated")

ROUND199_HARD_4C_GATES: tuple[str, ...] = (
    "privacy_breach",
    "security_outage",
    "founder_or_major_shareholder_legal_break",
    "regulatory_sanction",
    "ai_product_monetization_failure",
    "arr_churn_spike",
    "paid_user_decline",
    "game_launch_failure",
    "ip_litigation",
    "mna_integration_failure",
    "single_ip_collapse",
    "advertising_or_commerce_take_rate_damage",
    "fcf_deterioration_from_ai_capex",
)

ROUND199_PRICE_BACKFILL_FIELDS: tuple[str, ...] = (
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
    "peak_date",
    "peak_price",
    "MFE_5D",
    "MFE_20D",
    "MFE_30D",
    "MFE_60D",
    "MFE_90D",
    "MFE_180D",
    "MFE_1Y",
    "MFE_2Y",
    "MAE_5D",
    "MAE_20D",
    "MAE_30D",
    "MAE_60D",
    "MAE_90D",
    "MAE_180D",
    "MAE_1Y",
    "MAE_2Y",
    "drawdown_after_peak",
    "relative_strength_vs_kospi",
    "relative_strength_vs_platform_sw_basket",
    "relative_strength_vs_game_ip_basket",
    "relative_strength_vs_kpop_content_basket",
    "arr_proxy",
    "billings",
    "bookings",
    "paid_usage",
    "arpu",
    "mau",
    "retention_rate",
    "churn_rate",
    "opm",
    "gross_margin",
    "fcf_conversion",
    "enterprise_contract_value",
    "ip_repeat_monetization",
    "ai_revenue_conversion",
    "ai_capex",
    "mna_integration_status",
    "founder_legal_risk_flag",
    "privacy_security_incident_flag",
    "hard_4c_confirmed",
)


@dataclass(frozen=True)
class Round199ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {
            "axis": self.axis,
            "points": str(self.points),
            "direction": self.direction,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class Round199CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    stage1_date: date | None
    stage2_date: date | None
    stage3_date: date | None
    stage4b_date: date | None
    stage4c_date: date | None
    stage3_decision: str
    stage4b_status: str
    hard_4c_confirmed: bool
    evidence_fields: tuple[str, ...]
    red_flag_fields: tuple[str, ...]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> Round10LargeSector:
        return Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND199_SCORE_ADJUSTMENTS: tuple[Round199ScoreAdjustment, ...] = (
    Round199ScoreAdjustment("recurring_revenue", 5, "raise", "R8 Green은 반복매출과 고객 lock-in에서 시작한다."),
    Round199ScoreAdjustment("arr_proxy", 5, "raise", "ARR, billings, bookings proxy가 확인되면 SaaS/플랫폼 visibility가 올라간다."),
    Round199ScoreAdjustment("bookings_repeatability", 4, "raise", "게임/IP는 첫 주 판매보다 반복 bookings와 retention이 중요하다."),
    Round199ScoreAdjustment("paid_usage_conversion", 4, "raise", "AI 기능은 유료 사용 전환이 보여야 강한 증거다."),
    Round199ScoreAdjustment("enterprise_contract_quality", 4, "raise", "AI cloud/SW는 기업계약과 매출 전환이 확인될 때 강하다."),
    Round199ScoreAdjustment("opm_improvement", 4, "raise", "OPM 개선은 테마가 이익 체급 변화로 내려왔다는 증거다."),
    Round199ScoreAdjustment("fcf_conversion", 4, "raise", "AI capex와 콘텐츠 투자가 FCF를 훼손하지 않아야 한다."),
    Round199ScoreAdjustment("customer_retention_or_churn", 4, "raise", "retention 안정과 churn 하락은 반복매출의 질을 보여준다."),
    Round199ScoreAdjustment("ip_monetization_beyond_launch", 3, "raise", "콘텐츠/IP는 출시 이후 반복 monetization이 필요하다."),
    Round199ScoreAdjustment("cloud_ai_revenue_conversion", 4, "raise", "AI infra 투자는 실제 AI 매출로 전환될 때 점수를 준다."),
    Round199ScoreAdjustment("operational_trust", 4, "raise", "플랫폼/보안/콘텐츠는 법적·개인정보·운영 신뢰가 핵심 gate다."),
    Round199ScoreAdjustment("ai_feature_only", -5, "lower", "AI 기능 출시만으로 Stage 3-Green을 만들지 않는다."),
    Round199ScoreAdjustment("partnership_headline_only", -4, "lower", "OpenAI/KKR/파트너십 headline은 매출 전까지 Stage 1~2다."),
    Round199ScoreAdjustment("mau_without_arpu", -4, "lower", "MAU는 ARPU와 paid usage 없이 이익 체급 변화가 아니다."),
    Round199ScoreAdjustment("game_launch_first_week_only", -4, "lower", "첫 주 판매는 Stage 2 재료지만 반복 bookings 전 Green 금지다."),
    Round199ScoreAdjustment("ipo_first_month_rally", -4, "lower", "IPO 직후 가격반응은 single-IP/valuation overheat로 분리한다."),
    Round199ScoreAdjustment("single_ip_dependence", -4, "lower", "단일 IP 의존은 repeat portfolio 전까지 RedTeam이다."),
    Round199ScoreAdjustment("mna_event_without_integration", -3, "lower", "M&A 발표는 integration, 계약, margin 전까지 event premium이다."),
    Round199ScoreAdjustment("ai_capex_without_revenue", -4, "lower", "AI capex가 매출로 전환되지 않으면 FCF를 훼손할 수 있다."),
    Round199ScoreAdjustment("media_report_or_model_release_only", -3, "lower", "모델 공개나 언론 보도만으로 유료화 근거를 발명하지 않는다."),
    Round199ScoreAdjustment("founder_legal_risk", -5, "lower", "창업자/대주주 법적 리스크는 플랫폼 Green을 막을 수 있다."),
    Round199ScoreAdjustment("privacy_or_security_trust_break", -5, "lower", "개인정보·보안 신뢰 훼손은 hard RedTeam이다."),
)


ROUND199_CASE_CANDIDATES: tuple[Round199CaseCandidate, ...] = (
    Round199CaseCandidate(
        case_id="douzone_bizon_eqt_cloud_erp_stage2_watch",
        symbol="012510",
        company_name="더존비즈온",
        primary_archetype=E2RArchetype.B2B_SAAS_ERP_WORKFLOW,
        secondary_archetypes=(E2RArchetype.B2B_SAAS_ERP_WORKFLOW_KOREA, E2RArchetype.PRIVATE_EQUITY_SOFTWARE_RERATING),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2025, 11, 7),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_arr_churn_opm_fcf_customer_lockin_and_deal_approval_quality_are_visible",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("eqt_37_6pct_stake_purchase", "cloud_erp_accounting_tax_compliance", "sme_lock_in", "pe_operational_improvement"),
        red_flag_fields=("pe_event_premium", "arr_unverified", "churn_unverified", "opm_fcf_unverified", "regulatory_approval_condition"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="EQT deal and cloud ERP are Stage 2, but Green waits for ARR, churn, OPM, FCF, and customer lock-in.",
    ),
    Round199CaseCandidate(
        case_id="samsung_sds_kkr_ai_cloud_cb_4b_watch",
        symbol="018260",
        company_name="삼성SDS",
        primary_archetype=E2RArchetype.CLOUD_AI_SOFTWARE_INFRA,
        secondary_archetypes=(E2RArchetype.ENTERPRISE_AI_CLOUD_INFRA_KOREA, E2RArchetype.AI_CLOUD_CAPITAL_ALLOCATION),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2026, 4, 15),
        stage3_date=None,
        stage4b_date=date(2026, 4, 15),
        stage4c_date=None,
        stage3_decision="deferred_until_enterprise_ai_contracts_ai_revenue_margin_recurring_cloud_revenue_and_cb_dilution_risk_passed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("kkr_820m_usd_convertible_bond", "ai_infrastructure_investment", "full_stack_ai_solutions", "mna_capital_allocation_advisory"),
        red_flag_fields=("event_day_price_up_20_8pct", "cb_dilution_watch", "ai_capex_without_revenue", "mna_execution_unverified", "stablecoin_optional_theme"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="KKR and AI infra are Stage 2; event-day price spike is 4B-watch until AI contracts, revenue, and margin are visible.",
    ),
    Round199CaseCandidate(
        case_id="naver_webtoon_hyperclova_platform_ai_ip_stage2_watch",
        symbol="035420",
        company_name="NAVER",
        primary_archetype=E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        secondary_archetypes=(E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION, E2RArchetype.SOVEREIGN_KOREAN_AI_MODEL),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2024, 6, 17),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_webtoon_paid_content_arpu_ai_cloud_revenue_enterprise_contracts_search_ad_arpu_and_margin",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("webtoon_us_ipo_valuation_target", "global_mau_creator_ecosystem", "hyperclova_x_think_reasoning_model", "sovereign_korean_ai_capability"),
        red_flag_fields=("mau_without_arpu", "model_release_without_revenue", "webtoon_profitability_unverified", "ai_cloud_margin_unverified", "ad_slowdown_watch"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="Webtoon IPO and HyperCLOVA X are Stage 2 attention, not Green before paid content, AI/cloud revenue, ARPU, and margin.",
    ),
    Round199CaseCandidate(
        case_id="kakao_openai_partnership_governance_legal_event_watch",
        symbol="035720",
        company_name="카카오",
        primary_archetype=E2RArchetype.PLATFORM_SOFTWARE_INTERNET,
        secondary_archetypes=(E2RArchetype.AI_SOFTWARE_APPLICATION, E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK),
        case_type="failed_rerating",
        stage1_date=date(2025, 2, 4),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 2, 4),
        stage4c_date=None,
        stage3_decision="forbidden_openai_partnership_without_ai_revenue_arpu_opm_and_governance_trust_passed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("openai_kakao_partnership", "kakaotalk_ai_product_option", "governance_overhang_relief_after_acquittal"),
        red_flag_fields=("partnership_headline_only", "ai_monetization_unverified", "founder_legal_overhang", "event_fade_after_intraday_spike"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_green",
        price_validation_status="needs_ohlc_backfill",
        notes="OpenAI partnership is Stage 1~2 attention; Green needs AI revenue, ARPU, OPM, and governance trust.",
    ),
    Round199CaseCandidate(
        case_id="krafton_inzoi_adk_ai_first_game_ip_stage2_watch",
        symbol="259960",
        company_name="크래프톤",
        primary_archetype=E2RArchetype.GAME_CONTENT_IP_REPEAT_MONETIZATION,
        secondary_archetypes=(E2RArchetype.GAME_CONTENT_IP, E2RArchetype.SINGLE_IP_RELEASE_EVENT_PREMIUM, E2RArchetype.AI_SOFTWARE_APPLICATION),
        case_type="success_candidate",
        stage1_date=date(2025, 3, 1),
        stage2_date=date(2025, 4, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="deferred_until_repeat_bookings_retention_dlc_console_expansion_ip_monetization_and_ai_capex_revenue_conversion",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("inzoi_early_access_first_week_1m_sales", "adk_holdings_516m_usd_acquisition", "animation_ip_pipeline", "ai_first_developer_strategy"),
        red_flag_fields=("game_launch_first_week_only", "single_ip_dependence", "ai_capex_without_revenue", "mna_integration_unverified", "retention_unverified"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="needs_ohlc_backfill",
        notes="inZOI and ADK are Stage 2, while Stage 3 waits for repeat bookings, retention, DLC, and IP monetization.",
    ),
    Round199CaseCandidate(
        case_id="shiftup_stellar_blade_ipo_single_ip_overheat_watch",
        symbol="462870",
        company_name="시프트업",
        primary_archetype=E2RArchetype.SINGLE_IP_RELEASE_EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.GAME_CONTENT_IP, E2RArchetype.GAME_SINGLE_IP_EVENT_PREMIUM),
        case_type="overheat",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 7, 11),
        stage3_date=None,
        stage4b_date=date(2024, 7, 11),
        stage4c_date=None,
        stage3_decision="deferred_until_repeat_monetization_ip_portfolio_opm_fcf_and_next_pipeline_visibility",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("stellar_blade_console_hit", "ipo_korea_game_company_large_listing", "pc_version_1m_sales_3_days", "total_sales_above_3m"),
        red_flag_fields=("ipo_first_month_rally", "single_ip_dependence", "pc_port_sales_normalization", "next_title_pipeline_unverified", "valuation_overheat_watch"),
        score_price_alignment="price_moved_without_evidence",
        rerating_result="theme_overheat",
        stage_failure_type="false_green",
        price_validation_status="needs_ohlc_backfill",
        notes="Stellar Blade sales are strong Stage 2 evidence, but single-IP and IPO overheat block Green before repeat monetization.",
    ),
    Round199CaseCandidate(
        case_id="hybe_newjeans_bang_legal_governance_4c_watch",
        symbol="352820",
        company_name="HYBE",
        primary_archetype=E2RArchetype.KPOP_PLATFORM_CONTENT_IP,
        secondary_archetypes=(E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK, E2RArchetype.PLATFORM_PRIVACY_SECURITY_OVERLAY),
        case_type="failed_rerating",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 3, 21),
        stage3_decision="forbidden_until_ip_monetization_artist_pipeline_legal_risk_and_governance_trust_are_stable",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("kpop_global_ip_weverse_bts_comeback_option", "newjeans_ador_dispute_injunction", "founder_ipo_related_legal_risk_watch"),
        red_flag_fields=("artist_label_conflict", "founder_legal_risk", "governance_trust_break_watch", "ip_concentration", "legal_overhang"),
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="should_have_been_red",
        price_validation_status="needs_ohlc_backfill",
        notes="K-pop IP can be valuable, but governance/legal risk blocks Green until IP monetization and artist pipeline are stable.",
    ),
)


def round199_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND199_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector.value,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round199 R8 Loop-7 platform/content/SW/security price-path validation case. "
                "This is calibration-only and must not be used for candidate generation."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "partnership" in field
                or "ipo" in field
                or "launch" in field
                or "model" in field
                or "option" in field
                or "strategy" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "recurring" in field or "lock_in" in field or "commercial" in field or "paid" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "price" in field
                or "premium" in field
                or "valuation" in field
                or "event" in field
                or "ipo" in field
                or "overheat" in field
                or "spike" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "legal" in field
                or "governance" in field
                or "privacy" in field
                or "security" in field
                or "churn" in field
                or "retention" in field
                or "trust" in field
                or "collapse" in field
            ),
            must_have_fields=ROUND199_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4b_watch", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={
                "recurring_revenue_delta": 5.0,
                "arr_proxy_delta": 5.0,
                "bookings_repeatability_delta": 4.0,
                "paid_usage_conversion_delta": 4.0,
                "enterprise_contract_quality_delta": 4.0,
                "opm_improvement_delta": 4.0,
                "fcf_conversion_delta": 4.0,
                "ai_feature_only_delta": -5.0,
                "game_launch_first_week_only_delta": -4.0,
                "founder_legal_risk_delta": -5.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "needs_ohlc_backfill_true",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_ai_partnership_model_release_game_launch_ipo_or_mna_as_green_evidence",
                *ROUND199_GREEN_REQUIRED_FIELDS,
                *ROUND199_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(price_validation_status=candidate.price_validation_status),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8 if candidate.stage2_date or candidate.stage4b_date or candidate.stage4c_date else 0.35,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round199_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND199_CASE_CANDIDATES:
        rows.append(
            {
                "case_id": candidate.case_id,
                "symbol": candidate.symbol,
                "company_name": candidate.company_name,
                "primary_archetype": candidate.primary_archetype.value,
                "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
                "case_type": candidate.case_type,
                "stage1_date": _date_text(candidate.stage1_date),
                "stage2_date": _date_text(candidate.stage2_date),
                "stage3_date": _date_text(candidate.stage3_date),
                "stage4b_date": _date_text(candidate.stage4b_date),
                "stage4c_date": _date_text(candidate.stage4c_date),
                "stage3_decision": candidate.stage3_decision,
                "stage4b_status": candidate.stage4b_status,
                "hard_4c_confirmed": str(candidate.hard_4c_confirmed).lower(),
                "score_price_alignment": candidate.score_price_alignment,
                "rerating_result": candidate.rerating_result,
                "stage_failure_type": candidate.stage_failure_type,
                "price_validation_status": candidate.price_validation_status,
                "evidence_fields": "|".join(candidate.evidence_fields),
                "red_flag_fields": "|".join(candidate.red_flag_fields),
                "notes": candidate.notes,
            }
        )
    return tuple(rows)


def round199_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND199_SCORE_ADJUSTMENTS)


def round199_price_backfill_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round199_backfill": "true"} for field in ROUND199_PRICE_BACKFILL_FIELDS)


def round199_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round199_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND199_REQUIRED_TARGET_ALIASES.items()
    )


def round199_summary() -> dict[str, int | bool]:
    cases = round199_case_records()
    return {
        "case_candidate_count": len(cases),
        "required_target_count": len(ROUND199_REQUIRED_TARGET_ALIASES),
        "score_adjustment_count": len(ROUND199_SCORE_ADJUSTMENTS),
        "price_backfill_field_count": len(ROUND199_PRICE_BACKFILL_FIELDS),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "stage3_case_count": sum(1 for case in ROUND199_CASE_CANDIDATES if case.stage3_date),
        "hard_4c_case_count": sum(1 for case in ROUND199_CASE_CANDIDATES if case.hard_4c_confirmed),
        "stage4b_watch_or_elevated_count": sum(
            1 for case in ROUND199_CASE_CANDIDATES if case.stage4b_status in {"watch", "elevated"}
        ),
        "needs_ohlc_backfill_count": sum(1 for case in ROUND199_CASE_CANDIDATES if case.price_validation_status == "needs_ohlc_backfill"),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "needs_ohlc_backfill": True,
    }


def write_round199_r8_loop7_reports(
    *,
    output_directory: str | Path = ROUND199_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND199_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND199_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = write_case_library(round199_case_records(), cases_path)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "audit_json": audit,
        "summary": output / "round199_r8_loop7_price_validation_summary.md",
        "case_matrix": output / "round199_r8_loop7_case_matrix.csv",
        "target_aliases": output / "round199_r8_loop7_target_aliases.csv",
        "score_adjustments": output / "round199_r8_loop7_score_adjustments.csv",
        "price_backfill_fields": output / "round199_r8_loop7_price_backfill_fields.csv",
        "green_gate_review": output / "round199_r8_loop7_green_gate_review.md",
        "price_backfill_plan": output / "round199_r8_loop7_price_backfill_plan.md",
        "stage4b_4c_review": output / "round199_r8_loop7_stage4b_4c_review.md",
    }
    audit.write_text(json.dumps(round199_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round199_case_rows(), paths["case_matrix"])
    _write_rows(round199_target_alias_rows(), paths["target_aliases"])
    _write_rows(round199_score_adjustment_rows(), paths["score_adjustments"])
    _write_rows(round199_price_backfill_field_rows(), paths["price_backfill_fields"])
    paths["summary"].write_text(render_round199_summary_markdown(), encoding="utf-8")
    paths["green_gate_review"].write_text(render_round199_green_gate_review_markdown(), encoding="utf-8")
    paths["price_backfill_plan"].write_text(render_round199_price_backfill_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round199_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def round199_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND199_SOURCE_ROUND_PATH,
        "large_sector": Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY.value,
        "summary": round199_summary(),
        "target_aliases": list(round199_target_alias_rows()),
        "green_required_fields": list(ROUND199_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND199_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_statuses": list(ROUND199_STAGE4B_STATUSES),
        "hard_4c_gates": list(ROUND199_HARD_4C_GATES),
        "score_adjustments": list(round199_score_adjustment_rows()),
        "case_ids": [case.case_id for case in ROUND199_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round199_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_ai_partnership_model_release_mau_game_launch_ipo_or_mna_as_green_evidence",
            "do_not_invent_arr_bookings_paid_usage_arpu_opm_fcf_retention_churn_or_stage_prices",
            "do_not_confirm_hard_4c_without_reliable_primary_or_major_source",
        ],
    }


def render_round199_summary_markdown() -> str:
    summary = round199_summary()
    lines = [
        "# Round-199 R8 Loop-7 Price-Path Validation Summary",
        "",
        f"- source_round: `{ROUND199_SOURCE_ROUND_PATH}`",
        "- large_sector: `PLATFORM_CONTENT_SW_SECURITY`",
        "- scope: B2B SaaS, AI cloud, platform AI, webtoon/IP, game IP, IPO/single-IP, K-pop governance, and operational trust",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- score_adjustment_count: {summary['score_adjustment_count']}",
        f"- price_backfill_field_count: {summary['price_backfill_field_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
        f"- overheat_count: {summary['overheat_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- stage3_case_count: {summary['stage3_case_count']}",
        f"- stage4b_watch_or_elevated_count: {summary['stage4b_watch_or_elevated_count']}",
        f"- needs_ohlc_backfill_count: {summary['needs_ohlc_backfill_count']}",
        "- production_scoring_changed: false",
        "- candidate_generation_input: false",
        "- shadow_weight_only: true",
        "- needs_ohlc_backfill: true",
        "",
        "## Interpretation",
        "",
        "- R8은 AI 기능, 게임 출시, IPO, MAU, M&A가 가격을 먼저 밀 수 있는 섹터다.",
        "- 더존비즈온은 EQT deal과 cloud ERP가 Stage 2지만 ARR, churn, OPM, FCF 전 Green 금지다.",
        "- 삼성SDS는 KKR/AI infra 재료가 Stage 2지만 CB dilution과 AI revenue conversion을 분리해야 한다.",
        "- NAVER는 Webtoon IPO와 HyperCLOVA X가 Stage 2 attention이지만 paid content, ARPU, AI/cloud margin 전 Stage 3가 아니다.",
        "- 카카오 OpenAI partnership은 Stage 1~2 attention이며 AI monetization 전 price_moved_without_evidence다.",
        "- 크래프톤과 시프트업은 첫 판매보다 repeat bookings, retention, IP portfolio가 Stage 3 기준이다.",
        "- HYBE는 K-pop IP가 강해도 governance/legal risk가 Green을 막는다.",
        "",
        "쉬운 예: `as_of_date=2025-02-04`에 OpenAI 제휴가 나와도 AI 유료화와 ARPU가 없으면 Stage 3-Green이 아니라 Stage 1~2 watch다.",
    ]
    return "\n".join(lines) + "\n"


def render_round199_green_gate_review_markdown() -> str:
    lines = [
        "# Round-199 R8 Loop-7 Green Gate Review",
        "",
        "## Green Required Evidence",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND199_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Green Forbidden Patterns", ""])
    lines.extend(f"- `{field}`" for field in ROUND199_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "| --- | --- | ---: | --- |"])
    for adjustment in ROUND199_SCORE_ADJUSTMENTS:
        lines.append(f"| `{adjustment.axis}` | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these weights to production scoring yet.",
            "- Do not use Round199 cases as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds to force promotion.",
            "- Do not invent ARR, bookings, paid usage, ARPU, retention, churn, OPM, FCF, stage prices, or MFE/MAE.",
            "- Do not treat AI feature launch, partnership, model release, game launch, IPO, or M&A headline as Green evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round199_price_backfill_plan_markdown() -> str:
    lines = [
        "# Round-199 R8 Loop-7 Price Backfill Plan",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND199_PRICE_BACKFILL_FIELDS)
    lines.extend(["", "## Priority Cases", "", "| case | stage marker | current status | 4B status | hard 4C |", "| --- | --- | --- | --- | --- |"])
    for case in ROUND199_CASE_CANDIDATES:
        stage_marker = case.stage3_date or case.stage2_date or case.stage4b_date or case.stage4c_date or case.stage1_date
        lines.append(
            f"| `{case.case_id}` | {_date_text(stage_marker) or 'undated'} | "
            f"{case.price_validation_status} | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} |"
        )
    lines.extend(
        [
            "",
            "## Backfill Rule",
            "",
            "- Use official OHLC data for exact MFE/MAE.",
            "- Keep unknown values null or `needs_ohlc_backfill`.",
            "- Split AI partnership, model release, IPO, game launch, M&A, legal-risk, and repeat-revenue dates.",
            "- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round199_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round-199 R8 Loop-7 Stage 4B / 4C Review",
        "",
        "## 4B Status Definitions",
        "",
        "- `watch`: AI partnership, IPO, game launch, Webtoon/IP valuation, or M&A premium runs ahead of repeat economics.",
        "- `elevated`: ARR slows, retention weakens, AI capex hurts margin, M&A integration costs rise, or IP pipeline gaps appear.",
        "- `graduated`: strong releases no longer surprise, bookings normalize, or new AI/content headlines stop moving price.",
        "",
        "## Hard 4C Gates",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND199_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## R8 Interpretation",
            "",
            "- privacy/security/founder legal risk can block Green even when platform or IP is strong.",
            "- price-only AI partnership, IPO, first-week game sales, or M&A headline is 4B-watch, not full evidence-based 4B.",
            "- hard 4C requires reliable source confirmation of trust break, monetization failure, churn spike, launch failure, or legal break.",
            "",
            "## Case Review",
            "",
            "| case | 4B status | hard 4C confirmed | interpretation |",
            "| --- | --- | --- | --- |",
        ]
    )
    for case in ROUND199_CASE_CANDIDATES:
        lines.append(
            f"| `{case.case_id}` | `{case.stage4b_status}` | {str(case.hard_4c_confirmed).lower()} | {case.notes} |"
        )
    return "\n".join(lines) + "\n"


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> Path:
    rows_tuple = tuple(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows_tuple:
        path.write_text("", encoding="utf-8")
        return path
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows_tuple[0].keys()), lineterminator="\n")
        writer.writeheader()
        for row in rows_tuple:
            writer.writerow(dict(row))
    return path


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


__all__ = [
    "ROUND199_CASE_CANDIDATES",
    "ROUND199_DEFAULT_AUDIT_PATH",
    "ROUND199_DEFAULT_CASES_PATH",
    "ROUND199_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND199_GREEN_FORBIDDEN_PATTERNS",
    "ROUND199_GREEN_REQUIRED_FIELDS",
    "ROUND199_HARD_4C_GATES",
    "ROUND199_PRICE_BACKFILL_FIELDS",
    "ROUND199_REQUIRED_TARGET_ALIASES",
    "ROUND199_SCORE_ADJUSTMENTS",
    "ROUND199_SOURCE_ROUND_PATH",
    "ROUND199_STAGE4B_STATUSES",
    "Round199CaseCandidate",
    "Round199ScoreAdjustment",
    "render_round199_green_gate_review_markdown",
    "render_round199_price_backfill_plan_markdown",
    "render_round199_stage4b_4c_review_markdown",
    "render_round199_summary_markdown",
    "round199_audit_payload",
    "round199_case_records",
    "round199_case_rows",
    "round199_price_backfill_field_rows",
    "round199_score_adjustment_rows",
    "round199_summary",
    "round199_target_alias_rows",
    "write_round199_r8_loop7_reports",
]
