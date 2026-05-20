"""Round-290 R8 Loop-14 platform/content/software/security validation pack.

This module converts ``docs/round/round_290.md`` into calibration-only case
records and reports. It does not change production scoring, candidate
generation, or StageClassifier thresholds.

Easy example: a Webtoon IPO pop is useful Stage 2 evidence. It is not
Stage 3-Green until paid conversion, IP revenue stability, OP/FCF, and parent
value capture are visible.
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


ROUND290_SOURCE_ROUND_PATH = "docs/round/round_290.md"
ROUND290_ANALYST_ROUND_ID = "round_218"
ROUND290_LARGE_SECTOR = Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY.value
ROUND290_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round290_r8_loop14_platform_content_sw_security_price_validation"
ROUND290_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r8_loop14_round290.jsonl"
ROUND290_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round290_r8_loop14_platform_content_sw_security_price_validation_audit.json"

ROUND290_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE": E2RArchetype.WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE.value,
    "KAKAO_PLATFORM_GOVERNANCE_4C_WATCH": E2RArchetype.KAKAO_PLATFORM_GOVERNANCE_4C_WATCH.value,
    "KPOP_IP_CONTRACT_GOVERNANCE_4C": E2RArchetype.KPOP_IP_CONTRACT_GOVERNANCE_4C.value,
    "GAME_IP_IPO_STAGE2_QUALITY_GATE": E2RArchetype.GAME_IP_IPO_STAGE2_QUALITY_GATE.value,
    "LEGACY_GAME_TURNAROUND_BUYBACK_4B": E2RArchetype.LEGACY_GAME_TURNAROUND_BUYBACK_4B.value,
    "AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE": E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE.value,
    "ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2": E2RArchetype.ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2.value,
    "CYBERSECURITY_TRUST_HARD_4C_REFERENCE": E2RArchetype.CYBERSECURITY_TRUST_HARD_4C_REFERENCE.value,
}

ROUND290_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "paid_conversion_arpu_confirmed",
    "retention_and_repeat_usage_confirmed",
    "ip_revenue_stability_confirmed",
    "artist_contract_continuity_confirmed",
    "game_live_service_retention_confirmed",
    "new_title_pipeline_execution_confirmed",
    "cloud_ai_recurring_revenue_confirmed",
    "arr_retention_enterprise_sw_confirmed",
    "data_trust_internal_control_confirmed",
    "regulatory_governance_clearance_confirmed",
    "price_path_after_evidence",
)

ROUND290_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "MAU_headline_only",
    "IPO_pop_only",
    "AI_cloud_keyword_only",
    "creator_IP_optional_value_only",
    "artist_fandom_without_contract_stability",
    "buyback_without_new_title_retention",
    "PE_control_premium_without_ARR",
    "cybersecurity_theme_readthrough_without_contract",
    "governance_legal_risk_unresolved",
)

ROUND290_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "IPO_debut_plus_10_to_20pct",
    "AI_cloud_keyword_aggressive_IPO_pricing",
    "game_IP_valuation_single_hit_concentration",
    "buyback_earnings_beat_before_new_title_validation",
    "K_content_artist_fandom_before_contract_stability",
    "PE_control_premium_before_ARR",
    "platform_MAU_before_paid_conversion",
)

ROUND290_HARD_4C_GATES: tuple[str, ...] = (
    "major_data_breach_or_customer_trust_break",
    "founder_legal_risk_blocks_platform_or_financial_control",
    "artist_IP_contract_termination_or_label_governance_breakdown",
    "IPO_weak_debut_after_aggressive_pricing",
    "platform_IP_revenue_guidance_miss",
    "game_launch_failure_or_retention_collapse",
    "enterprise_software_regulatory_approval_failure",
    "cloud_AI_revenue_mix_not_translating_into_margin",
)

ROUND290_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_event_return_anchor",
    "reported_event_price_anchor",
    "ipo_price_anchor",
    "deal_value_anchor",
    "revenue_op_anchor",
    "mau_anchor",
    "data_breach_cost_anchor",
    "stage1_price",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round290ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round290ShadowWeightRow:
    archetype: E2RArchetype
    paid_conversion_arpu: int
    retention_repeat_usage: int
    ip_revenue_stability: int
    artist_contract_continuity: int
    game_live_service_retention: int
    new_title_pipeline_execution: int
    cloud_ai_recurring_revenue: int
    arr_retention_enterprise_sw: int
    data_trust_internal_control: int
    regulatory_governance_clearance: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "paid_conversion_arpu": _signed(self.paid_conversion_arpu),
            "retention_repeat_usage": _signed(self.retention_repeat_usage),
            "ip_revenue_stability": _signed(self.ip_revenue_stability),
            "artist_contract_continuity": _signed(self.artist_contract_continuity),
            "game_live_service_retention": _signed(self.game_live_service_retention),
            "new_title_pipeline_execution": _signed(self.new_title_pipeline_execution),
            "cloud_ai_recurring_revenue": _signed(self.cloud_ai_recurring_revenue),
            "arr_retention_enterprise_sw": _signed(self.arr_retention_enterprise_sw),
            "data_trust_internal_control": _signed(self.data_trust_internal_control),
            "regulatory_governance_clearance": _signed(self.regulatory_governance_clearance),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round290DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round290CaseCandidate:
    case_id: str
    symbol: str
    company_name: str
    primary_archetype: E2RArchetype
    secondary_archetypes: tuple[E2RArchetype, ...]
    case_type: str
    round_case_type: str
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
    price_data_source: str
    reported_event_return_anchor: str
    reported_event_price_anchor: str
    event_mfe_pct: float | None
    event_mae_pct: float | None
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, object]
    score_price_alignment: str
    round_alignment_label: str
    rerating_result: str
    round_rerating_label: str
    stage_failure_type: str
    round_stage_failure_label: str
    price_validation_status: str
    notes: str

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND290_SCORE_ADJUSTMENTS: tuple[Round290ScoreAdjustment, ...] = (
    Round290ScoreAdjustment("paid_conversion_ARPU", 5, "raise", "플랫폼 MAU는 결제전환과 ARPU로 닫혀야 한다."),
    Round290ScoreAdjustment("retention_and_repeat_usage", 5, "raise", "콘텐츠와 게임은 반복 사용/retention이 핵심이다."),
    Round290ScoreAdjustment("IP_revenue_stability", 5, "raise", "IP optionality는 안정 매출로 확인되어야 한다."),
    Round290ScoreAdjustment("artist_contract_continuity", 5, "raise", "K-pop IP는 artist contract와 label governance가 뿌리다."),
    Round290ScoreAdjustment("game_live_service_retention", 5, "raise", "게임 hit title은 live-service retention으로 검증한다."),
    Round290ScoreAdjustment("new_title_pipeline_execution", 5, "raise", "레거시 게임 턴어라운드는 신작 실행력이 필요하다."),
    Round290ScoreAdjustment("cloud_AI_recurring_revenue", 5, "raise", "AI/cloud 매출비중보다 반복매출과 margin이 중요하다."),
    Round290ScoreAdjustment("ARR_retention_enterprise_SW", 5, "raise", "enterprise SW는 ARR, churn, retention이 Green의 핵심이다."),
    Round290ScoreAdjustment("data_trust_internal_control", 5, "raise", "보안 신뢰는 매출전망, 과징금, 보상비용으로 연결된다."),
    Round290ScoreAdjustment("regulatory_governance_clearance", 5, "raise", "창업자/규제 overhang이 있으면 플랫폼 premium을 유예한다."),
    Round290ScoreAdjustment("MAU_headline_only", -5, "lower", "MAU headline만으로 Stage 3-Green을 만들지 않는다."),
    Round290ScoreAdjustment("IPO_pop_only", -5, "lower", "IPO pop은 unit economics 전에는 event premium이다."),
    Round290ScoreAdjustment("AI_cloud_keyword_only", -5, "lower", "AI/cloud 키워드는 recurring revenue 전에는 부족하다."),
    Round290ScoreAdjustment("creator_IP_optional_value_only", -5, "lower", "creator/IP optional value만으로 OP/FCF를 만들지 않는다."),
    Round290ScoreAdjustment("artist_fandom_without_contract_stability", -5, "lower", "fandom은 contract stability 없이는 Green이 아니다."),
    Round290ScoreAdjustment("buyback_without_new_title_retention", -5, "lower", "buyback은 신작 retention 없이는 event premium이다."),
    Round290ScoreAdjustment("PE_control_premium_without_ARR", -5, "lower", "PE control premium은 ARR/margin 전에는 Stage 2다."),
    Round290ScoreAdjustment("cybersecurity_theme_readthrough_without_contract", -5, "lower", "보안사고 수혜 테마는 실제 계약/ARR 전에는 Green이 아니다."),
    Round290ScoreAdjustment("governance_legal_risk_unresolved", -5, "lower", "거버넌스·법률 리스크 미해소는 Green을 막는다."),
)


ROUND290_SHADOW_WEIGHT_ROWS: tuple[Round290ShadowWeightRow, ...] = (
    Round290ShadowWeightRow(E2RArchetype.WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE, 5, 5, 5, 1, 0, 0, 2, 0, 3, 3, -5, 5, 4, "Webtoon IPO pop/MAU failed to prove durable parent value capture and revenue-guide stability."),
    Round290ShadowWeightRow(E2RArchetype.KAKAO_PLATFORM_GOVERNANCE_4C_WATCH, 3, 4, 3, 2, 0, 0, 3, 2, 4, 5, 0, 4, 5, "Kakao shows platform moat must pass founder/legal/regulatory gate."),
    Round290ShadowWeightRow(E2RArchetype.KPOP_IP_CONTRACT_GOVERNANCE_4C, 2, 5, 5, 5, 0, 0, 0, 0, 2, 5, 0, 5, 4, "HYBE/NewJeans shows artist contract continuity is core IP gate."),
    Round290ShadowWeightRow(E2RArchetype.GAME_IP_IPO_STAGE2_QUALITY_GATE, 2, 5, 4, 0, 5, 5, 0, 0, 1, 3, -5, 5, 3, "Shift Up hit IP/IPO needs live-service retention and next-title pipeline."),
    Round290ShadowWeightRow(E2RArchetype.LEGACY_GAME_TURNAROUND_BUYBACK_4B, 1, 5, 3, 0, 5, 5, 0, 0, 1, 3, -5, 5, 3, "NCSoft buyback/earnings beat needs new-title retention and monetization proof."),
    Round290ShadowWeightRow(E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE, 2, 4, 0, 0, 0, 0, 5, 5, 2, 3, -5, 5, 4, "LG CNS shows AI/cloud mix and oversubscription can still fail aftermarket demand."),
    Round290ShadowWeightRow(E2RArchetype.ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2, 3, 5, 0, 0, 0, 0, 4, 5, 3, 5, -5, 4, 3, "Douzone/EQT needs ARR, churn, cloud margin and regulatory approval."),
    Round290ShadowWeightRow(E2RArchetype.CYBERSECURITY_TRUST_HARD_4C_REFERENCE, 0, 3, 0, 0, 0, 0, 2, 3, 5, 5, 0, 5, 5, "SK Telecom confirms data-trust/internal-control failure is hard 4C."),
)


ROUND290_DEEP_SUB_ARCHETYPES: tuple[Round290DeepSubArchetype, ...] = (
    Round290DeepSubArchetype("웹툰 플랫폼 IPO after-market", E2RArchetype.WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE, ("NAVER", "Webtoon Entertainment", "WBTN", "170M MAU", "Disney deal", "parent holdco discount")),
    Round290DeepSubArchetype("카카오 플랫폼 거버넌스", E2RArchetype.KAKAO_PLATFORM_GOVERNANCE_4C_WATCH, ("Kakao", "SM Entertainment", "founder arrest", "KakaoBank control", "stock manipulation allegation")),
    Round290DeepSubArchetype("K-pop IP 계약 거버넌스", E2RArchetype.KPOP_IP_CONTRACT_GOVERNANCE_4C, ("HYBE", "ADOR", "NewJeans", "artist contract", "label governance")),
    Round290DeepSubArchetype("게임 IP IPO 품질", E2RArchetype.GAME_IP_IPO_STAGE2_QUALITY_GATE, ("Shift Up", "Nikke", "Stellar Blade", "Tencent", "single-IP concentration")),
    Round290DeepSubArchetype("레거시 게임 턴어라운드", E2RArchetype.LEGACY_GAME_TURNAROUND_BUYBACK_4B, ("NCSoft", "buyback", "earnings beat", "new title pipeline", "legacy decline")),
    Round290DeepSubArchetype("AI/cloud IT서비스 IPO false positive", E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE, ("LG CNS", "cloud AI sales", "IPO price break", "oversubscription", "margin durability")),
    Round290DeepSubArchetype("enterprise SW PE control", E2RArchetype.ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2, ("Douzone Bizon", "EQT", "ERP", "ARR", "KFTC clearance")),
    Round290DeepSubArchetype("사이버보안 신뢰 hard 4C", E2RArchetype.CYBERSECURITY_TRUST_HARD_4C_REFERENCE, ("SK Telecom", "USIM", "26.96M data pieces", "revenue forecast cut", "fine")),
)


ROUND290_CASE_CANDIDATES: tuple[Round290CaseCandidate, ...] = (
    Round290CaseCandidate(
        case_id="r8_loop14_naver_webtoon_ipo_aftermarket_gate",
        symbol="035420/WBTN",
        company_name="NAVER / Webtoon Entertainment",
        primary_archetype=E2RArchetype.WEBTOON_PLATFORM_IPO_AFTERMARKET_GATE,
        secondary_archetypes=(E2RArchetype.GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN, E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION),
        case_type="event_premium",
        round_case_type="event_premium + aftermarket gate",
        stage1_date=date(2024, 5, 31),
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=date(2024, 6, 27),
        stage4c_date=date(2026, 5, 11),
        stage3_decision="webtoon_ipo_and_mau_are_stage2_until_paid_conversion_ip_revenue_stability_and_parent_value_capture_confirm",
        stage4b_status="4B-watch/IPO-pop-then-aftermarket-validation",
        hard_4c_confirmed=False,
        evidence_fields=("webtoon_ipo_price_21_usd", "ipo_raise_315mn_usd", "monthly_active_users_170mn", "q1_2024_revenue_326_7mn_usd", "q1_2024_net_income_6_2mn_usd", "disney_earnings_rebound"),
        red_flag_fields=("MAU_headline_only", "IPO_pop_only", "parent_holding_company_discount", "post_ipo_drawdown", "platform_IP_revenue_guidance_miss"),
        price_data_source="Reuters / MarketWatch / Barron's / WSJ event anchors",
        reported_event_return_anchor="WBTN +14.3% debut, later -55%, +62% rebound, then -15% after-hours on weak guide",
        reported_event_price_anchor="IPO $21; debut high $24; later after-hours $11.24; NAVER event price 165,300 KRW",
        event_mfe_pct=14.3,
        event_mae_pct=-15.0,
        stage1_price_anchor=None,
        stage2_price_anchor=21.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=24.0,
        stage4c_price_anchor=11.24,
        extra_price_metrics={"webtoon_ipo_price_usd": 21.0, "webtoon_open_price_usd": 21.30, "webtoon_debut_high_usd": 24.0, "webtoon_debut_mfe_pct": 14.3, "ipo_raise_usd_mn": 315.0, "ipo_valuation_usd_bn": 2.71, "q1_2024_revenue_usd_mn": 326.7, "q1_2024_net_income_usd_mn": 6.2, "monthly_active_users_mn": 170.0, "naver_event_price_krw": 165300, "naver_event_mae_pct": -0.9, "naver_target_price_krw": 210000, "naver_target_cut_pct": -22.0, "holding_company_discount_applied_pct": 50.0, "post_ipo_decline_before_disney_pct": -55.0, "disney_earnings_rebound_mfe_pct": 62.0, "disney_rebound_price_usd": 15.16, "q2_2025_revenue_usd_mn": 348.3, "q2_2025_revenue_growth_pct": 8.5, "q1_2026_revenue_usd_mn": 320.9, "q1_2026_revenue_decline_pct": -1.5, "q2_2026_guidance_usd_mn": "332-342", "q2_2026_consensus_usd_mn": 348.0, "q1_2026_after_hours_mae_pct": -15.0, "q1_2026_after_hours_price_usd": 11.24},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_then_aftermarket_gate",
        rerating_result="event_premium",
        round_rerating_label="WEBTOON_PLATFORM_IPO_STAGE2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="IPO_pop_MAU_not_parent_value_capture_green",
        price_validation_status="reported_event_anchors_not_full_ohlc",
        notes="IPO pop and 170M MAU are Stage 2; Green needs paid conversion, IP revenue stability, and parent value capture.",
    ),
    Round290CaseCandidate(
        case_id="r8_loop14_kakao_platform_governance_sm_case",
        symbol="035720/041510_readthrough",
        company_name="Kakao / SM Entertainment read-through",
        primary_archetype=E2RArchetype.KAKAO_PLATFORM_GOVERNANCE_4C_WATCH,
        secondary_archetypes=(E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_4C_WATCH, E2RArchetype.KPOP_PLATFORM_CONTENT_IP_GOVERNANCE),
        case_type="4b_watch",
        round_case_type="thesis_break_watch_then_relief",
        stage1_date=date(2023, 2, 1),
        stage2_date=date(2025, 10, 21),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 7, 23),
        stage3_decision="platform_user_base_is_not_green_without_founder_legal_regulatory_and_control_risk_clearance",
        stage4b_status="4C-watch/founder-legal-governance-risk-then-relief",
        hard_4c_confirmed=False,
        evidence_fields=("kakao_sm_acquisition_context", "founder_arrest_stock_manipulation_allegation", "kakao_event_mae_minus_3_4pct", "later_acquittal_relief"),
        red_flag_fields=("governance_legal_risk_unresolved", "founder_legal_risk_blocks_platform_or_financial_control", "KakaoBank_control_risk", "SM_content_governance_risk"),
        price_data_source="Reuters Kakao founder arrest and prosecution anchors",
        reported_event_return_anchor="Kakao -3.4% on founder arrest; YTD -24% context",
        reported_event_price_anchor="Direct SM event price unavailable; Kakao event return anchor used",
        event_mfe_pct=None,
        event_mae_pct=-3.4,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"kakao_event_mae_pct": -3.4, "kakao_ytd_decline_context_pct": -24.0, "founder_affiliated_stake_pct": 24.0, "group_assets_krw_trn": 86.0, "prosecutor_sought_sentence_years": 15, "prosecutor_sought_fine_krw_mn": 500.0, "risk_channels": ["AI investment", "international expansion", "KakaoBank control", "SM content governance"], "sm_stock_manipulation_allegation": True, "direct_sm_event_price": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="thesis_break_watch_then_relief",
        rerating_result="unknown",
        round_rerating_label="PLATFORM_GOVERNANCE_4C_WATCH",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="user_base_not_green_without_founder_legal_regulatory_clearance",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Platform moat is not Green while founder/legal and financial-control read-through risk remains.",
    ),
    Round290CaseCandidate(
        case_id="r8_loop14_hybe_ador_newjeans_ip_governance",
        symbol="352820",
        company_name="HYBE / ADOR / NewJeans",
        primary_archetype=E2RArchetype.KPOP_IP_CONTRACT_GOVERNANCE_4C,
        secondary_archetypes=(E2RArchetype.KPOP_IP_GOVERNANCE_4C_WATCH, E2RArchetype.KPOP_PLATFORM_CONTENT_IP_GOVERNANCE),
        case_type="4b_watch",
        round_case_type="4C-watch / artist-IP contract governance",
        stage1_date=date(2024, 4, 22),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 4, 24),
        stage3_decision="fandom_and_artist_ip_are_not_green_without_contract_stability_label_governance_and_revenue_continuity",
        stage4b_status="4C-watch/artist-IP-contract-and-label-governance",
        hard_4c_confirmed=False,
        evidence_fields=("hybe_audits_ador", "newjeans_ip_governance_concern", "hybe_event_mae_nearly_minus_8pct", "contract_dispute_persistence"),
        red_flag_fields=("artist_fandom_without_contract_stability", "artist_IP_contract_termination_or_label_governance_breakdown", "multi_label_governance_risk", "content_IP_dependency"),
        price_data_source="Reuters HYBE/ADOR audit and share reaction anchor",
        reported_event_return_anchor="HYBE shares nearly -8% on ADOR/NewJeans dispute",
        reported_event_price_anchor="Direct adjusted OHLC unavailable; event return anchor used",
        event_mfe_pct=None,
        event_mae_pct=-8.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_mae_pct": -8.0, "dispute_parties": ["HYBE", "ADOR", "Min Hee-jin", "NewJeans"], "risk_type": ["artist_contract_continuity", "multi_label_governance", "content_IP_dependency"], "newjeans_contract_dispute_persistence": True, "direct_adjusted_ohlc": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="KPOP_IP_CONTRACT_GOVERNANCE_GATE",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="fandom_and_artist_IP_not_green_without_contract_stability",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="K-pop fandom is not enough; artist contract continuity and label governance are the evidence gate.",
    ),
    Round290CaseCandidate(
        case_id="r8_loop14_shift_up_game_ip_ipo_quality_gate",
        symbol="462870",
        company_name="Shift Up",
        primary_archetype=E2RArchetype.GAME_IP_IPO_STAGE2_QUALITY_GATE,
        secondary_archetypes=(E2RArchetype.GAME_IP_MONETIZATION_IPO_STAGE2, E2RArchetype.GAME_IP_IPO_SINGLE_TITLE_RISK),
        case_type="success_candidate",
        round_case_type="success_candidate + IPO quality gate",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=date(2024, 6, 27),
        stage4c_date=None,
        stage3_decision="hit_ip_and_ipo_are_stage2_until_live_service_retention_recurring_monetization_next_title_pipeline_and_aftermarket_demand_confirm",
        stage4b_status="4B-watch/IPO-valuation-before-retention-proof",
        hard_4c_confirmed=False,
        evidence_fields=("shiftup_ipo_raise_435bn_krw", "valuation_3_5trn_krw", "nikke_sales_255bn_krw", "revenue_2023_169bn_krw", "op_2023_111bn_krw", "stellar_blade_rankings"),
        red_flag_fields=("IPO_pop_only", "game_IP_valuation_single_hit_concentration", "live_service_retention_unconfirmed", "next_title_pipeline_unconfirmed"),
        price_data_source="Reuters Shift Up IPO and game-IP anchor",
        reported_event_return_anchor="IPO raise/value and game sales anchors; full post-IPO OHLC unavailable",
        reported_event_price_anchor="435B KRW IPO raise; 3.5T KRW valuation",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_raise_krw_bn": 435.0, "ipo_raise_usd_mn": 313.0, "valuation_krw_trn": 3.5, "valuation_usd_bn": 2.52, "tencent_stake_before_pct": 40.0, "tencent_stake_after_expected_pct": 35.0, "nikke_sales_krw_bn_to_q1_2024": 255.0, "revenue_2023_krw_bn": 169.0, "op_2023_krw_bn": 111.0, "op_margin_2023_pct": 65.7, "stellar_blade_download_ranking": {"Japan_PS": 1, "North_America_PS": 2}, "stage3_conditions": ["live_service_retention", "global_sellthrough", "recurring_monetization", "next_title_pipeline", "post_ipo_demand"]},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_IPO_quality_gate",
        rerating_result="unknown",
        round_rerating_label="GAME_IP_IPO_STAGE2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="hit_IP_and_IPO_not_recurring_revenue_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Strong hit-IP economics are Stage 2; Green needs live-service retention and next-title execution.",
    ),
    Round290CaseCandidate(
        case_id="r8_loop14_ncsoft_earnings_buyback_turnaround",
        symbol="036570",
        company_name="NCSoft",
        primary_archetype=E2RArchetype.LEGACY_GAME_TURNAROUND_BUYBACK_4B,
        secondary_archetypes=(E2RArchetype.GAME_CONTENT_IP_REPEAT_MONETIZATION, E2RArchetype.BUYBACK_EXECUTION_PRICE_FAILED),
        case_type="event_premium",
        round_case_type="event_premium + 4B-watch",
        stage1_date=date(2024, 5, 1),
        stage2_date=date(2024, 5, 1),
        stage3_date=None,
        stage4b_date=date(2024, 5, 1),
        stage4c_date=None,
        stage3_decision="earnings_beat_and_buyback_are_stage2_until_new_title_retention_global_monetization_and_legacy_decline_stabilize",
        stage4b_status="4B-watch/buyback-earnings-beat-before-new-title-validation",
        hard_4c_confirmed=False,
        evidence_fields=("q1_net_profit_57_12bn_krw", "shares_up_to_plus_14pct", "buyback_533417_shares", "new_title_pipeline"),
        red_flag_fields=("buyback_without_new_title_retention", "legacy_game_decline_not_stabilized", "global_monetization_unconfirmed"),
        price_data_source="WSJ NCSoft Q1 earnings beat / buyback event anchor",
        reported_event_return_anchor="Shares up to +14% on earnings beat and buyback",
        reported_event_price_anchor="Q1 net profit 57.12B KRW; buyback 533,417 shares",
        event_mfe_pct=14.0,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"event_mfe_pct": 14.0, "q1_net_profit_krw_bn": 57.12, "net_profit_yoy_change_pct": -50.0, "analyst_forecast_low_krw_bn": 24.99, "analyst_forecast_high_krw_bn": 26.0, "buyback_shares": 533417, "treasury_share_ratio_context_pct": 10.0, "new_title_pipeline": ["Battle Crush", "Project BSS", "LLL", "Throne and Liberty global expansion"], "new_title_retention_confirmed": False, "global_monetization_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4B_watch",
        rerating_result="event_premium",
        round_rerating_label="LEGACY_GAME_TURNAROUND_STAGE2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="buyback_earnings_beat_not_new_title_retention_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Buyback and a one-quarter beat are not enough without new-title retention and monetization.",
    ),
    Round290CaseCandidate(
        case_id="r8_loop14_lg_cns_ai_cloud_ipo_false_positive",
        symbol="064400",
        company_name="LG CNS",
        primary_archetype=E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_FALSE_POSITIVE,
        secondary_archetypes=(E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE, E2RArchetype.ENTERPRISE_AI_CLOUD_INFRA_KOREA),
        case_type="failed_rerating",
        round_case_type="evidence_good_but_price_failed",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 2, 5),
        stage3_date=None,
        stage4b_date=date(2025, 2, 5),
        stage4c_date=None,
        stage3_decision="cloud_ai_sales_mix_is_stage2_until_recurring_revenue_arr_retention_margin_and_aftermarket_demand_confirm",
        stage4b_status="4B-watch/AI-cloud-IPO-demand-before-aftermarket-proof",
        hard_4c_confirmed=False,
        evidence_fields=("cloud_ai_sales_share_54pct", "ipo_raise_1_2trn_krw", "retail_oversubscription_123x", "revenue_9m2024_4trn_krw", "op_9m2024_313bn_krw"),
        red_flag_fields=("AI_cloud_keyword_only", "IPO_weak_debut_after_aggressive_pricing", "aftermarket_demand_failed", "arr_retention_unconfirmed"),
        price_data_source="Reuters LG CNS IPO/debut anchor",
        reported_event_return_anchor="IPO price 61,900 KRW; morning trading 59,700 KRW, -3.23% vs IPO",
        reported_event_price_anchor="IPO 61,900 KRW, open 60,500 KRW, morning 59,700 KRW",
        event_mfe_pct=None,
        event_mae_pct=-3.23,
        stage1_price_anchor=None,
        stage2_price_anchor=61900.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=59700.0,
        extra_price_metrics={"ipo_price_krw": 61900, "open_price_krw": 60500, "morning_trading_price_krw": 59700, "debut_mae_vs_ipo_pct": -3.23, "ipo_raise_krw_trn": 1.2, "ipo_raise_usd_mn": 827.1, "retail_oversubscription_multiple": 123.0, "institutional_bids_krw_trn": 76.0, "cloud_ai_sales_share_9m2024_pct": 54.0, "revenue_9m2024_krw_trn": 4.0, "op_9m2024_krw_bn": 313.0, "op_margin_9m2024_pct": 7.8, "aftermarket_demand_confirmed": False},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="unknown",
        round_rerating_label="AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE",
        stage_failure_type="false_yellow",
        round_stage_failure_label="AI_cloud_sales_mix_not_aftermarket_green",
        price_validation_status="reported_ipo_anchor_not_full_ohlc",
        notes="Cloud/AI sales mix and oversubscription failed the aftermarket price test.",
    ),
    Round290CaseCandidate(
        case_id="r8_loop14_douzone_bizon_eqt_enterprise_sw_stage2",
        symbol="012510",
        company_name="Douzone Bizon",
        primary_archetype=E2RArchetype.ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2,
        secondary_archetypes=(E2RArchetype.B2B_SAAS_ERP_WORKFLOW, E2RArchetype.PRIVATE_EQUITY_SOFTWARE_RERATING),
        case_type="success_candidate",
        round_case_type="success_candidate + regulatory/control watch",
        stage1_date=date(2025, 11, 7),
        stage2_date=date(2025, 11, 7),
        stage3_date=None,
        stage4b_date=date(2025, 11, 7),
        stage4c_date=None,
        stage3_decision="pe_control_premium_is_stage2_until_arr_retention_cloud_margin_cross_sell_and_regulatory_approval_confirm",
        stage4b_status="4B-watch/PE-control-premium-before-ARR-proof",
        hard_4c_confirmed=False,
        evidence_fields=("eqt_investment_930mn_usd", "stake_acquired_37_6pct", "ERP_accounting_tax_compliance_cloud_software", "KFTC_and_ministry_approval_required"),
        red_flag_fields=("PE_control_premium_without_ARR", "regulatory_approval_unconfirmed", "arr_retention_unconfirmed", "cloud_margin_unconfirmed"),
        price_data_source="Reuters EQT-Douzone Bizon stake anchor",
        reported_event_return_anchor="Direct event return unavailable; $930M for 37.6% stake used as control-premium anchor",
        reported_event_price_anchor="$930M investment for 37.6% stake",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"eqt_investment_usd_mn": 930.0, "stake_acquired_pct": 37.6, "chairman_stake_sold_pct": 23.2, "shinhan_affiliate_stake_sold_pct": 14.4, "business_model": ["ERP", "accounting", "tax", "compliance", "cloud-based SME software"], "regulatory_approvals_required": ["KFTC merger clearance", "Ministry of Trade licensing authorization"], "arr_retention_confirmed": False, "cloud_margin_confirmed": False, "direct_event_return": "price_data_unavailable_after_deep_search"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_price_data_unavailable",
        rerating_result="unknown",
        round_rerating_label="ENTERPRISE_SOFTWARE_PE_CONTROL_STAGE2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="PE_control_premium_not_ARR_margin_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="PE control premium is Stage 2; Green needs ARR retention, cloud margin, and regulatory approval.",
    ),
    Round290CaseCandidate(
        case_id="r8_loop14_sk_telecom_cybersecurity_trust_hard_4c",
        symbol="017670",
        company_name="SK Telecom",
        primary_archetype=E2RArchetype.CYBERSECURITY_TRUST_HARD_4C_REFERENCE,
        secondary_archetypes=(E2RArchetype.CYBERSECURITY_TRUST_HARD_4C, E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C, E2RArchetype.SECURITY_OPERATIONAL_TRUST_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="hard 4C reference / cybersecurity trust break",
        stage1_date=date(2025, 4, 18),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 28),
        stage3_decision="major_customer_data_breach_is_hard_4c_when_revenue_cut_compensation_security_capex_and_fine_follow",
        stage4b_status="hard-4C/data-trust-internal-control-break",
        hard_4c_confirmed=True,
        evidence_fields=("skt_data_breach", "initial_intraday_minus_8_5pct", "free_usim_replacement_23mn_users", "26_96mn_data_pieces_leaked", "700bn_krw_security_investment", "800bn_krw_revenue_forecast_cut", "134bn_krw_fine"),
        red_flag_fields=("major_data_breach_or_customer_trust_break", "data_trust_internal_control_break", "revenue_forecast_cut", "customer_compensation_liability", "regulatory_fine"),
        price_data_source="Reuters SK Telecom data-breach event, investigation and fine anchors",
        reported_event_return_anchor="Shares -8.5% intraday and -6.7% close; later -5.6% on leak validation",
        reported_event_price_anchor="26.96M data pieces leaked; 700B KRW security investment; 800B KRW revenue forecast cut; 134B KRW fine",
        event_mfe_pct=None,
        event_mae_pct=-8.5,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"initial_intraday_mae_pct": -8.5, "initial_close_mae_pct": -6.7, "kospi_same_context_pct": 0.1, "relative_underperformance_initial_pp": -6.8, "free_usim_replacement_users_mn": 23.0, "retail_stores_involved": 2600, "usim_protection_service_signups_mn": 5.54, "leaked_data_pieces_mn": 26.96, "july_event_close_mae_pct": -5.6, "data_protection_investment_krw_bn": 700.0, "revenue_forecast_cut_krw_bn": 800.0, "customer_benefit_package_cost_krw_bn": 500.0, "pipc_fine_krw_bn": 134.0},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="CYBERSECURITY_TRUST_HARD_4C_REFERENCE",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="data_trust_internal_control_break",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Data-trust failure became stock drop, revenue cut, compensation package, security capex, and fine: hard 4C.",
    ),
)


def round290_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND290_CASE_CANDIDATES:
        stage3_terms = ("paid", "arpu", "retention", "recurring", "margin", "arr", "contract", "governance", "clearance", "fcf")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND290_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round290 R8 Loop-14 platform/content/software/security price validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(token in field.lower() for token in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("ipo", "buyback", "premium", "mau", "ai", "cloud", "pe", "valuation"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("breach", "legal", "governance", "contract", "trust", "fine", "forecast", "regulatory", "weak", "guidance"))),
            must_have_fields=ROUND290_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4b_watch", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND290_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "direct_KRX_hard_4c_confirmed_true_for_SK_Telecom_security_reference",
                "do_not_use_round290_cases_as_candidate_generation_input",
                "do_not_treat_MAU_IPO_AI_cloud_IP_or_buyback_as_green_alone",
                *ROUND290_GREEN_REQUIRED_FIELDS,
                *ROUND290_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.event_mfe_pct,
                mae_30d=candidate.event_mae_pct,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.event_mfe_pct is not None
                    or candidate.event_mae_pct is not None
                    or candidate.stage1_price_anchor is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round290_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {
            "case_id": candidate.case_id,
            "symbol": candidate.symbol,
            "company_name": candidate.company_name,
            "primary_archetype": candidate.primary_archetype.value,
            "secondary_archetypes": "|".join(item.value for item in candidate.secondary_archetypes),
            "case_type": candidate.case_type,
            "round_case_type": candidate.round_case_type,
            "stage1_date": _date_text(candidate.stage1_date),
            "stage2_date": _date_text(candidate.stage2_date),
            "stage3_date": _date_text(candidate.stage3_date),
            "stage4b_date": _date_text(candidate.stage4b_date),
            "stage4c_date": _date_text(candidate.stage4c_date),
            "stage3_decision": candidate.stage3_decision,
            "stage4b_status": candidate.stage4b_status,
            "hard_4c_confirmed": str(candidate.hard_4c_confirmed).lower(),
            "price_data_source": candidate.price_data_source,
            "reported_event_return_anchor": candidate.reported_event_return_anchor,
            "reported_event_price_anchor": candidate.reported_event_price_anchor,
            "event_mfe_pct": _float_text(candidate.event_mfe_pct),
            "event_mae_pct": _float_text(candidate.event_mae_pct),
            "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
            "score_price_alignment": candidate.score_price_alignment,
            "round_alignment_label": candidate.round_alignment_label,
            "rerating_result": candidate.rerating_result,
            "round_rerating_label": candidate.round_rerating_label,
            "stage_failure_type": candidate.stage_failure_type,
            "round_stage_failure_label": candidate.round_stage_failure_label,
            "price_validation_status": candidate.price_validation_status,
            "evidence_fields": "|".join(candidate.evidence_fields),
            "red_flag_fields": "|".join(candidate.red_flag_fields),
            "notes": candidate.notes,
        }
        for candidate in ROUND290_CASE_CANDIDATES
    )


def round290_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND290_SCORE_ADJUSTMENTS)


def round290_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND290_SHADOW_WEIGHT_ROWS)


def round290_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND290_DEEP_SUB_ARCHETYPES)


def round290_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round290_price_validation": "true"} for field in ROUND290_PRICE_VALIDATION_FIELDS)


def round290_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round290_label": label, "canonical_archetype": canonical} for label, canonical in ROUND290_REQUIRED_TARGET_ALIASES.items())


def round290_summary() -> dict[str, int | bool | str]:
    cases = ROUND290_CASE_CANDIDATES
    return {
        "source_round": ROUND290_SOURCE_ROUND_PATH,
        "round_id": ROUND290_ANALYST_ROUND_ID,
        "large_sector": ROUND290_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "watch_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "false_positive_score_count": sum(1 for case in cases if case.score_price_alignment == "false_positive_score"),
        "unknown_alignment_count": sum(1 for case in cases if case.score_price_alignment == "unknown"),
        "target_archetype_count": len(ROUND290_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND290_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND290_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "direct_KRX_hard_4c_confirmed": True,
    }


def round290_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND290_SOURCE_ROUND_PATH,
        "round_id": ROUND290_ANALYST_ROUND_ID,
        "large_sector": ROUND290_LARGE_SECTOR,
        "summary": round290_summary(),
        "target_aliases": dict(ROUND290_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND290_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND290_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND290_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND290_HARD_4C_GATES),
        "score_adjustments": list(round290_score_adjustment_rows()),
        "shadow_weights": list(round290_shadow_weight_rows()),
        "deep_sub_archetypes": list(round290_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND290_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round290_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_MAU_IPO_AI_cloud_IP_or_buyback_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round290_summary_markdown() -> str:
    summary = round290_summary()
    lines = [
        "# Round 290 R8 Loop 14 Platform Content Software Security Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- watch rows: {summary['watch_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND290_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.round_case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    case.round_alignment_label,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- Webtoon/NAVER is Stage 2 platform IPO evidence; MAU and IPO pop need paid conversion, IP revenue stability, and parent value capture.",
            "- Kakao and HYBE show governance, legal, and artist-contract gates can block platform/content premium.",
            "- Shift Up and NCSoft are game/IP Stage 2 or 4B-watch until retention, monetization, and new-title execution are visible.",
            "- LG CNS shows AI/cloud mix can still fail the aftermarket demand test.",
            "- Douzone is enterprise SW Stage 2 until ARR, churn, cloud margin, and regulatory approval are visible.",
            "- SK Telecom is the hard 4C reference for cybersecurity trust break.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round290_green_gate_review_markdown() -> str:
    lines = [
        "# Round 290 R8 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R8 Stage 3-Green is not `MAU`, `IPO`, `K-pop fandom`, `game IP`, `AI/cloud`, `PE control premium`, or `buyback`. It requires paid conversion, retention, IP revenue stability, contract/governance clearance, ARR, margin, trust, OP/FCF, and price path after evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND290_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND290_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND290_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Webtoon 170M MAU` is Stage 2; Green needs paid conversion and parent value capture.",
            "- `LG CNS cloud/AI 54% sales` is useful, but IPO price failure means recurring margin is not proven.",
            "- `SK Telecom data breach` is hard 4C because revenue guidance, fine, compensation, and trust costs followed.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round290_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 290 R8 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND290_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND290_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND290_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round290_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 290 R8 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, paid conversion, ARR, retention, creator economics, recurring revenue, governance clearance, security remediation, margin, or FCF where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND290_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND290_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_event_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round290_r8_loop14_reports(
    output_directory: str | Path = ROUND290_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND290_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND290_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round290_case_records(), cases_path),
        "audit": _write_json(round290_audit_payload(), audit_path),
        "summary": output / "round290_r8_loop14_price_validation_summary.md",
        "case_matrix": output / "round290_r8_loop14_case_matrix.csv",
        "target_aliases": output / "round290_r8_loop14_target_aliases.csv",
        "score_adjustments": output / "round290_r8_loop14_score_adjustments.csv",
        "shadow_weights": output / "round290_r8_loop14_shadow_weights.csv",
        "deep_sub_archetypes": output / "round290_r8_loop14_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round290_r8_loop14_price_validation_fields.csv",
        "green_gate_review": output / "round290_r8_loop14_green_gate_review.md",
        "price_validation_plan": output / "round290_r8_loop14_price_validation_plan.md",
        "stage4b_4c_review": output / "round290_r8_loop14_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round290_summary_markdown(), encoding="utf-8")
    _write_csv(round290_case_rows(), paths["case_matrix"])
    _write_csv(round290_target_alias_rows(), paths["target_aliases"])
    _write_csv(round290_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round290_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round290_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round290_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round290_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round290_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round290_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def _write_json(payload: object, path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def _write_csv(rows: Iterable[dict[str, str]], path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    rows = tuple(rows)
    if not rows:
        target.write_text("", encoding="utf-8")
        return target
    with target.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _float_text(value: float | None) -> str:
    return "" if value is None else f"{value:g}"


def _signed(value: int) -> str:
    return f"+{value}" if value > 0 else str(value)
