"""Round-277 R8 Loop-13 platform/content/software/security validation pack.

This module converts ``docs/round/round_277.md`` into calibration-only case
records and reports. It does not change production scoring, candidate
generation, or StageClassifier thresholds.

Easy example: 170M MAU is not Stage 3-Green by itself. It becomes stronger only
when paid conversion, ARPU/take-rate, OP/FCF, and parent value bridge are visible.
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


ROUND277_SOURCE_ROUND_PATH = "docs/round/round_277.md"
ROUND277_ANALYST_ROUND_ID = "round_205"
ROUND277_LARGE_SECTOR = Round10LargeSector.PLATFORM_CONTENT_SW_SECURITY.value
ROUND277_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round277_r8_loop13_platform_content_sw_security_price_validation"
ROUND277_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r8_loop13_round277.jsonl"
ROUND277_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round277_r8_loop13_platform_content_sw_security_price_validation_audit.json"

ROUND277_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "DATA_SOVEREIGNTY_PLATFORM_4C_WATCH": E2RArchetype.DATA_SOVEREIGNTY_PLATFORM_4C_WATCH.value,
    "GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN": E2RArchetype.GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN.value,
    "PLATFORM_GOVERNANCE_LEGAL_4C_WATCH": E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_4C_WATCH.value,
    "KPOP_IP_GOVERNANCE_4C_WATCH": E2RArchetype.KPOP_IP_GOVERNANCE_4C_WATCH.value,
    "GAME_IP_MONETIZATION_IPO_STAGE2": E2RArchetype.GAME_IP_MONETIZATION_IPO_STAGE2.value,
    "AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE": E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE.value,
    "EMERGING_MARKET_GAME_PLATFORM_OPTION": E2RArchetype.EMERGING_MARKET_GAME_PLATFORM_OPTION.value,
    "CYBERSECURITY_TRUST_HARD_4C": E2RArchetype.CYBERSECURITY_TRUST_HARD_4C.value,
}

ROUND277_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "paid_conversion_confirmed",
    "arpu_take_rate_growth_confirmed",
    "platform_unit_economics_confirmed",
    "creator_or_developer_economics_confirmed",
    "parent_value_bridge_confirmed",
    "multi_title_or_ip_retention_confirmed",
    "recurring_cloud_ai_revenue_confirmed",
    "cloud_ai_margin_durability_confirmed",
    "data_governance_clearance_confirmed",
    "cybersecurity_internal_control_confirmed",
    "regulatory_founder_legal_overhang_cleared",
    "op_fcf_conversion_confirmed",
    "price_path_after_evidence",
)

ROUND277_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "MAU_only",
    "IPO_pop_only",
    "downloads_without_ARPU",
    "AI_cloud_keyword_without_margin",
    "content_IP_headline_only",
    "unlisted_subsidiary_or_US_listed_parent_bridge_missing",
    "founder_legal_overhang_unresolved",
    "label_or_artist_governance_dispute_unresolved",
    "data_breach_or_internal_control_failure",
)

ROUND277_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "IPO_debut_plus_10_to_15pct_before_unit_economics",
    "game_IPO_top_range_before_multi_title_durability",
    "MAU_100mn_headline_parent_rally_without_value_bridge",
    "AI_cloud_sales_mix_headline_before_recurring_margin",
    "India_or_emerging_market_downloads_before_ARPU",
    "Kpop_IP_rebound_without_governance_clearance",
    "data_breach_relief_rebound_before_full_cost",
)

ROUND277_HARD_4C_GATES: tuple[str, ...] = (
    "large_data_breach",
    "USIM_identity_authentication_leakage",
    "regulatory_fine",
    "revenue_forecast_cut_from_trust_event",
    "platform_forced_selldown_or_data_sovereignty_dispute",
    "founder_arrest_or_capital_market_law_risk",
    "artist_IP_contract_rupture",
    "cloud_AI_recurring_revenue_miss",
    "IPO_valuation_break",
    "game_regulatory_ban_or_data_security_ban",
)

ROUND277_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_adjusted_ohlc_complete",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "event_mfe_pct",
    "event_mae_pct",
    "platform_monetization_anchor",
    "governance_or_legal_anchor",
    "cybersecurity_trust_cost_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round277ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round277ShadowWeightRow:
    archetype: E2RArchetype
    paid_conversion: int
    arpu_take_rate: int
    recurring_cloud_ai_revenue: int
    creator_economics: int
    content_ip_retention: int
    platform_data_governance: int
    cybersecurity_internal_control: int
    regulatory_clearance: int
    parent_value_bridge: int
    customer_trust_repair_cost: int
    event_penalty: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "paid_conversion": _signed(self.paid_conversion),
            "arpu_take_rate": _signed(self.arpu_take_rate),
            "recurring_cloud_ai_revenue": _signed(self.recurring_cloud_ai_revenue),
            "creator_economics": _signed(self.creator_economics),
            "content_ip_retention": _signed(self.content_ip_retention),
            "platform_data_governance": _signed(self.platform_data_governance),
            "cybersecurity_internal_control": _signed(self.cybersecurity_internal_control),
            "regulatory_clearance": _signed(self.regulatory_clearance),
            "parent_value_bridge": _signed(self.parent_value_bridge),
            "customer_trust_repair_cost": _signed(self.customer_trust_repair_cost),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round277DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round277CaseCandidate:
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
    reported_price_anchor: str
    reported_return_anchor: str
    event_mfe_pct: float | None
    event_mae_pct: float | None
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


ROUND277_SCORE_ADJUSTMENTS: tuple[Round277ScoreAdjustment, ...] = (
    Round277ScoreAdjustment("paid_conversion", 5, "raise", "MAU는 유료 전환과 ARPU/take-rate로 닫혀야 한다."),
    Round277ScoreAdjustment("ARPU_take_rate", 5, "raise", "플랫폼 Green은 사용자 수보다 monetization이 중요하다."),
    Round277ScoreAdjustment("recurring_cloud_AI_revenue", 5, "raise", "AI/cloud 매출은 반복성과 margin이 확인되어야 한다."),
    Round277ScoreAdjustment("creator_economics", 4, "raise", "콘텐츠 플랫폼은 creator economics가 지속 가능해야 한다."),
    Round277ScoreAdjustment("content_IP_retention", 5, "raise", "게임/K-pop IP는 retention과 repeat monetization이 필요하다."),
    Round277ScoreAdjustment("platform_data_governance", 5, "raise", "해외 플랫폼은 data governance와 control risk가 먼저다."),
    Round277ScoreAdjustment("cybersecurity_internal_control", 5, "raise", "보안 신뢰는 플랫폼/통신 cash flow의 hard gate다."),
    Round277ScoreAdjustment("regulatory_clearance", 5, "raise", "규제·창업자·법률 overhang 해소가 필요하다."),
    Round277ScoreAdjustment("parent_value_bridge", 4, "raise", "상장 자회사/해외 IPO는 모회사 가치 연결고리가 필요하다."),
    Round277ScoreAdjustment("customer_trust_repair_cost", 5, "raise", "데이터 침해는 매출, 보상, 과징금, 보안투자 비용으로 내려온다."),
    Round277ScoreAdjustment("MAU_only", -5, "lower", "MAU-only는 Stage 3-Green 증거가 아니다."),
    Round277ScoreAdjustment("IPO_pop_only", -5, "lower", "IPO pop은 unit economics 전에는 event premium이다."),
    Round277ScoreAdjustment("downloads_without_ARPU", -5, "lower", "다운로드만으로 ARPU/FCF를 만들지 않는다."),
    Round277ScoreAdjustment("AI_cloud_keyword_without_margin", -5, "lower", "AI/cloud 키워드는 recurring margin 전에는 부족하다."),
    Round277ScoreAdjustment("founder_legal_overhang", -5, "lower", "창업자/자본시장법 리스크는 platform premium을 막는다."),
    Round277ScoreAdjustment("label_or_artist_governance_dispute", -5, "lower", "K-pop IP는 label governance가 깨지면 4C-watch다."),
    Round277ScoreAdjustment("data_breach_or_internal_control_failure", -5, "lower", "대형 data breach는 hard 4C가 될 수 있다."),
)


ROUND277_SHADOW_WEIGHT_ROWS: tuple[Round277ShadowWeightRow, ...] = (
    Round277ShadowWeightRow(E2RArchetype.DATA_SOVEREIGNTY_PLATFORM_4C_WATCH, 3, 3, 2, 2, 3, 5, 5, 5, 4, 5, 0, 4, 5, "NAVER/Line Yahoo shows data sovereignty can override platform scale."),
    Round277ShadowWeightRow(E2RArchetype.GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN, 5, 5, 1, 5, 5, 4, 3, 3, 5, 3, -5, 5, 4, "Webtoon IPO/MAU needs monetization and parent NAVER value bridge."),
    Round277ShadowWeightRow(E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_4C_WATCH, 3, 4, 2, 3, 5, 4, 4, 5, 4, 4, 0, 4, 5, "Kakao/SM shows founder legal risk blocks platform content premium."),
    Round277ShadowWeightRow(E2RArchetype.KPOP_IP_GOVERNANCE_4C_WATCH, 4, 5, 1, 3, 5, 4, 3, 5, 3, 4, 0, 4, 5, "HYBE/ADOR shows artist IP is not enough without label governance."),
    Round277ShadowWeightRow(E2RArchetype.GAME_IP_MONETIZATION_IPO_STAGE2, 5, 5, 1, 2, 5, 2, 2, 3, 2, 2, -5, 5, 4, "Shift Up needs multi-title durability beyond IPO and single-IP economics."),
    Round277ShadowWeightRow(E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE, 3, 4, 5, 0, 1, 3, 4, 3, 3, 2, -5, 5, 3, "LG CNS needs recurring AI/cloud revenue and margin durability, not IPO demand."),
    Round277ShadowWeightRow(E2RArchetype.EMERGING_MARKET_GAME_PLATFORM_OPTION, 5, 5, 1, 1, 4, 4, 3, 5, 2, 3, -4, 5, 4, "Krafton India needs ARPU, paid conversion, regulatory clearance and second-hit proof."),
    Round277ShadowWeightRow(E2RArchetype.CYBERSECURITY_TRUST_HARD_4C, 0, 0, 0, 0, 0, 5, 5, 5, 0, 5, 0, 4, 5, "SKT breach confirms data/security trust hard gate."),
)


ROUND277_DEEP_SUB_ARCHETYPES: tuple[Round277DeepSubArchetype, ...] = (
    Round277DeepSubArchetype("플랫폼 데이터 주권", E2RArchetype.DATA_SOVEREIGNTY_PLATFORM_4C_WATCH, ("NAVER", "LY Corp", "Line Yahoo", "Japan administrative guidance", "SoftBank control", "data sovereignty")),
    Round277DeepSubArchetype("글로벌 웹툰 플랫폼", E2RArchetype.GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN, ("Webtoon Entertainment", "Nasdaq IPO", "170M MAU", "Line Manga", "Wattpad", "parent value bridge")),
    Round277DeepSubArchetype("플랫폼 거버넌스 법률", E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_4C_WATCH, ("Kakao", "SM Entertainment", "founder arrest", "KakaoBank control", "IPO pipeline")),
    Round277DeepSubArchetype("K-pop IP 거버넌스", E2RArchetype.KPOP_IP_GOVERNANCE_4C_WATCH, ("HYBE", "ADOR", "NewJeans", "Bang Si-hyuk", "artist IP concentration")),
    Round277DeepSubArchetype("게임 IP IPO", E2RArchetype.GAME_IP_MONETIZATION_IPO_STAGE2, ("Shift Up", "Nikke", "Stellar Blade", "Tencent stake", "single-IP concentration")),
    Round277DeepSubArchetype("AI/cloud IT서비스 IPO", E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE, ("LG CNS", "cloud and AI sales", "IPO price failure", "recurring revenue", "margin durability")),
    Round277DeepSubArchetype("인도 게임 플랫폼 옵션", E2RArchetype.EMERGING_MARKET_GAME_PLATFORM_OPTION, ("Krafton", "BGMI", "India fund", "240M downloads", "ARPU", "regulatory volatility")),
    Round277DeepSubArchetype("사이버보안 신뢰 hard 4C", E2RArchetype.CYBERSECURITY_TRUST_HARD_4C, ("SK Telecom", "USIM replacement", "26.96M data pieces", "revenue forecast cut", "fine", "compensation")),
)


ROUND277_CASE_CANDIDATES: tuple[Round277CaseCandidate, ...] = (
    Round277CaseCandidate(
        case_id="r8_loop13_naver_line_yahoo_data_sovereignty_watch",
        symbol="035420",
        company_name="NAVER / Line Yahoo / LY Corp",
        primary_archetype=E2RArchetype.DATA_SOVEREIGNTY_PLATFORM_4C_WATCH,
        secondary_archetypes=(E2RArchetype.PLATFORM_TRUST_4C_WATCH, E2RArchetype.PLATFORM_PRIVACY_SECURITY_OVERLAY),
        case_type="4b_watch",
        round_case_type="4C-watch / data-sovereignty platform control",
        stage1_date=date(2023, 11, 1),
        stage2_date=date(2024, 8, 2),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 4, 27),
        stage3_decision="platform_scale_is_not_green_until_data_governance_regulatory_clearance_and_capital_structure_clarity",
        stage4b_status="4C-watch/data-sovereignty-control-risk",
        hard_4c_confirmed=False,
        evidence_fields=("line_yahoo_data_leak", "japan_administrative_guidance", "softbank_control_discussion", "ly_buyback_150bn_jpy", "voting_rights_decline_64_42_to_62_50pct"),
        red_flag_fields=("platform_forced_selldown_or_data_sovereignty_dispute", "data_governance_clearance_unconfirmed", "capital_control_risk", "outsourcing_to_naver_unwind_watch"),
        price_data_source="Reuters data leak / SoftBank talks / LY buyback anchors",
        reported_price_anchor="LY Corp 150B yen buyback; A Holdings voting rights 64.42% to as low as 62.50%",
        reported_return_anchor="Data-sovereignty relief, not Green; NAVER OHLC unavailable",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"data_leak_records_context": "more_than_300000_Line_users_and_others_in_Reuters_source", "ly_corp_market_value_may2024_jpy_trn": 2.77, "ly_corp_market_value_may2024_usd_bn": 17.77, "a_holdings_pre_buyback_voting_rights_pct": 64.42, "a_holdings_post_buyback_low_voting_rights_pct": 62.50, "voting_rights_decline_pp": -1.92, "buyback_value_jpy_bn": 150.0, "buyback_value_usd_bn": 1.01, "buyback_price_jpy": 388.0, "buyback_premium_pct": 11.0},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="data_sovereignty_platform_4C_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="overseas_platform_control_not_green_without_data_governance",
        price_validation_status="naver_ohlc_unavailable_after_deep_search",
        notes="MAU scale and buyback relief are not Green until data governance and capital-control clarity are visible.",
    ),
    Round277CaseCandidate(
        case_id="r8_loop13_naver_webtoon_entertainment_ipo",
        symbol="035420/WBTN",
        company_name="NAVER / Webtoon Entertainment",
        primary_archetype=E2RArchetype.GLOBAL_CONTENT_PLATFORM_IPO_NOT_PARENT_GREEN,
        secondary_archetypes=(E2RArchetype.WEBTOON_PLATFORM_IP_MONETIZATION, E2RArchetype.PLATFORM_SOFTWARE_INTERNET),
        case_type="success_candidate",
        round_case_type="success_candidate + event_premium / parent value bridge gap",
        stage1_date=date(2024, 6, 26),
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=date(2024, 6, 27),
        stage4c_date=None,
        stage3_decision="webtoon_ipo_is_stage2_until_paid_conversion_creator_economics_op_fcf_and_parent_value_bridge",
        stage4b_status="4B-watch/ipo-pop-before-monetization",
        hard_4c_confirmed=False,
        evidence_fields=("webtoon_ipo_price_21_usd", "ipo_raise_315mn_usd", "valuation_2_67bn_usd", "monthly_active_users_170mn", "webtoon_2023_revenue_1_28bn_usd"),
        red_flag_fields=("MAU_only", "IPO_pop_only", "creator_platform_loss_ignored", "unlisted_subsidiary_or_US_listed_parent_bridge_missing", "webtoon_2023_net_loss_145mn_usd"),
        price_data_source="Reuters / FT Webtoon IPO anchors",
        reported_price_anchor="Webtoon sold 15M shares at $21, raised $315M, valuation about $2.67B",
        reported_return_anchor="Debut high $24, +14.3%; NAVER parent value bridge unconfirmed",
        event_mfe_pct=14.3,
        event_mae_pct=None,
        stage2_price_anchor=21.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=24.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_price_usd": 21.0, "shares_sold_mn": 15.0, "ipo_raise_usd_mn": 315.0, "valuation_usd_bn": 2.67, "debut_high_usd": 24.0, "debut_mfe_pct": 14.3, "opened_at_usd": 21.30, "naver_private_placement_usd_mn": 50.0, "blackrock_indicated_interest_usd_mn": 50.0, "monthly_active_users_mn": 170.0, "countries": 150, "webtoon_2023_revenue_usd_bn": 1.28, "webtoon_2023_net_loss_usd_mn": 145.0, "naver_parent_value_bridge_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_event_premium",
        rerating_result="event_premium",
        round_rerating_label="global_content_platform_IPO_stage2",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="IPO_MAU_not_parent_EPS_green",
        price_validation_status="reported_ipo_anchor_not_full_ohlc",
        notes="Webtoon IPO is Stage 2; MAU and IPO pop are not parent NAVER Green without monetization and value bridge.",
    ),
    Round277CaseCandidate(
        case_id="r8_loop13_kakao_sm_founder_legal_governance",
        symbol="035720",
        company_name="Kakao / SM Entertainment legal overhang",
        primary_archetype=E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_4C_WATCH,
        secondary_archetypes=(E2RArchetype.PLATFORM_GOVERNANCE_LEGAL_RISK, E2RArchetype.KPOP_PLATFORM_CONTENT_IP_GOVERNANCE),
        case_type="4b_watch",
        round_case_type="4C-watch / platform governance legal overhang",
        stage1_date=date(2023, 3, 1),
        stage2_date=date(2025, 10, 21),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 7, 23),
        stage3_decision="sm_ownership_is_not_green_until_founder_legal_overhang_governance_and_ip_monetization_clear",
        stage4b_status="4C-watch/founder-legal-overhang-then-relief",
        hard_4c_confirmed=False,
        evidence_fields=("kakao_sm_control_battle", "founder_arrest_stock_manipulation_suspicion", "kakao_event_mae_minus_3_4pct", "later_acquittal_relief"),
        red_flag_fields=("founder_legal_overhang_unresolved", "platform_content_MA_governance_gate", "KakaoBank_control_risk", "IPO_pipeline_risk"),
        price_data_source="Reuters Kakao arrest/acquittal anchors",
        reported_price_anchor="Founder arrest during SM acquisition probe; later acquittal relief",
        reported_return_anchor="Kakao shares -3.4% on founder arrest",
        event_mfe_pct=None,
        event_mae_pct=-3.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"arrest_event_date": "2024-07-23", "kakao_event_mae_pct": -3.4, "kim_beom_su_kakao_stake_pct": 24.0, "kakao_group_value_context_krw_trn": 86.0, "kakao_group_value_context_usd_bn": 62.0, "prosecutor_sought_sentence_years": 15, "prosecutor_sought_fine_krw_mn": 500.0, "acquittal_date": "2025-10-21", "sm_content_monetization_confirmed": False},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch_then_relief",
        rerating_result="unknown",
        round_rerating_label="platform_content_MA_governance_gate",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="founder_legal_overhang_not_content_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="SM acquisition context is not Green while founder/legal governance risk blocks platform premium.",
    ),
    Round277CaseCandidate(
        case_id="r8_loop13_hybe_ador_bang_legal_ip_governance",
        symbol="352820",
        company_name="HYBE / ADOR / Bang Si-hyuk legal risk",
        primary_archetype=E2RArchetype.KPOP_IP_GOVERNANCE_4C_WATCH,
        secondary_archetypes=(E2RArchetype.KPOP_PLATFORM_CONTENT_IP_GOVERNANCE, E2RArchetype.ENTERTAINMENT_GOVERNANCE_LEGAL_OVERLAY),
        case_type="4b_watch",
        round_case_type="4C-watch / content IP governance legal risk",
        stage1_date=date(2024, 4, 22),
        stage2_date=date(2026, 4, 24),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 4, 24),
        stage3_decision="artist_ip_strength_is_not_green_until_label_governance_founder_legal_risk_and_op_fcf_clear",
        stage4b_status="4C-watch/artist-IP-governance-and-founder-legal-risk",
        hard_4c_confirmed=False,
        evidence_fields=("hybe_audits_ador", "newjeans_label_dispute", "hybe_shares_nearly_minus_8pct", "bang_sihyuk_share_probe", "detention_warrant_request_minus_2_4pct"),
        red_flag_fields=("label_or_artist_governance_dispute_unresolved", "founder_legal_overhang_unresolved", "artist_IP_contract_rupture_watch", "shareholder_trust_overhang"),
        price_data_source="Reuters / AP HYBE governance and legal-risk anchors",
        reported_price_anchor="ADOR dispute and Bang Si-hyuk IPO-related investigation anchors",
        reported_return_anchor="HYBE nearly -8% on ADOR dispute; -2.4% on warrant request",
        event_mfe_pct=None,
        event_mae_pct=-8.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ador_dispute_event_mae_pct": -8.0, "bang_detention_request_event_mae_pct": -2.4, "alleged_profit_arrangement_krw_bn": 190.0, "alleged_profit_arrangement_usd_mn": 129.1, "police_raid_date": "2025-07-24", "prosecutors_rejected_warrant_request_date": "2026-04-24", "artist_ip_strength_confirmed": True, "governance_legal_clearance_confirmed": False},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break_watch",
        rerating_result="unknown",
        round_rerating_label="Kpop_IP_governance_4C_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="artist_IP_not_green_without_label_governance_clearance",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Artist IP strength does not override label governance and founder legal risk.",
    ),
    Round277CaseCandidate(
        case_id="r8_loop13_shiftup_game_ip_ipo_overheat",
        symbol="462870",
        company_name="Shift Up",
        primary_archetype=E2RArchetype.GAME_IP_MONETIZATION_IPO_STAGE2,
        secondary_archetypes=(E2RArchetype.GAME_IP_IPO_SINGLE_TITLE_RISK, E2RArchetype.GAME_CONTENT_IP),
        case_type="success_candidate",
        round_case_type="success_candidate + overheat / game-IP IPO Stage 2",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 6, 27),
        stage3_date=None,
        stage4b_date=date(2024, 7, 1),
        stage4c_date=None,
        stage3_decision="game_ip_ipo_is_stage2_until_multi_title_durability_live_ops_retention_arpu_and_fcf_confirm",
        stage4b_status="4B-watch/ipo-top-range-single-IP-premium",
        hard_4c_confirmed=False,
        evidence_fields=("shiftup_ipo_raise_435bn_krw", "valuation_3_5trn_krw", "nikke_revenue_255bn_krw", "revenue_2023_169bn_krw", "op_2023_111bn_krw"),
        red_flag_fields=("IPO_pop_only", "game_single_IP_concentration", "post_ipo_multititle_durability_unconfirmed", "China_launch_review_retention_watch"),
        price_data_source="Reuters Shift Up IPO anchor",
        reported_price_anchor="Top-range IPO, 435B KRW raise, 3.5T KRW valuation",
        reported_return_anchor="Full OHLC unavailable; single-IP durability unconfirmed",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"ipo_raise_krw_bn": 435.0, "ipo_raise_usd_mn": 313.0, "valuation_krw_trn": 3.5, "valuation_usd_bn": 2.52, "tencent_stake_pre_ipo_pct": 40.0, "tencent_stake_post_ipo_pct": 35.0, "nikke_revenue_late2022_to_q1_2024_krw_bn": 255.0, "revenue_2023_krw_bn": 169.0, "op_2023_krw_bn": 111.0, "op_margin_2023_pct": 65.7, "post_ipo_multititle_durability_confirmed": False},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_but_ipo_overheat",
        rerating_result="event_premium",
        round_rerating_label="game_IP_monetization_stage2",
        stage_failure_type="false_yellow",
        round_stage_failure_label="IPO_top_range_not_multititle_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Strong game-IP economics are Stage 2; Green needs multi-title durability and live-ops retention.",
    ),
    Round277CaseCandidate(
        case_id="r8_loop13_lg_cns_ai_cloud_ipo_quality_gate",
        symbol="064400",
        company_name="LG CNS",
        primary_archetype=E2RArchetype.AI_CLOUD_IT_SERVICE_IPO_QUALITY_GATE,
        secondary_archetypes=(E2RArchetype.CLOUD_AI_SOFTWARE_INFRA, E2RArchetype.ENTERPRISE_AI_CLOUD_INFRA_KOREA),
        case_type="success_candidate",
        round_case_type="evidence_good_but_price_failed / AI-cloud IPO quality gate",
        stage1_date=date(2025, 1, 6),
        stage2_date=date(2025, 2, 5),
        stage3_date=None,
        stage4b_date=date(2025, 2, 5),
        stage4c_date=date(2025, 2, 5),
        stage3_decision="ai_cloud_mix_is_stage2_until_recurring_revenue_margin_durability_mna_roi_and_fcf_confirm",
        stage4b_status="4B-watch/IPO-demand-before-margin-durability",
        hard_4c_confirmed=False,
        evidence_fields=("cloud_ai_sales_share_54pct", "revenue_9m2024_4trn_krw", "op_9m2024_313bn_krw", "ipo_raise_1_2trn_krw", "retail_oversubscription_123x"),
        red_flag_fields=("AI_cloud_keyword_without_margin", "IPO_valuation_break", "recurring_revenue_unconfirmed", "margin_durability_unconfirmed", "mna_roi_unconfirmed"),
        price_data_source="Reuters LG CNS IPO and debut anchors",
        reported_price_anchor="IPO price 61,900 KRW; debut morning 59,700 KRW",
        reported_return_anchor="Debut price below IPO price, -3.23%",
        event_mfe_pct=None,
        event_mae_pct=-3.23,
        stage2_price_anchor=61900.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=59700.0,
        extra_price_metrics={"ipo_price_krw": 61900.0, "open_price_krw": 60500.0, "morning_trading_price_krw": 59700.0, "debut_mae_vs_ipo_pct": -3.23, "ipo_raise_krw_trn": 1.2, "ipo_raise_usd_mn": 827.1, "market_valuation_morning_krw_trn": 5.79, "retail_oversubscription_multiple": 123.0, "institutional_bids_krw_trn": 76.0, "cloud_ai_sales_share_9m2024_pct": 54.0, "revenue_9m2024_krw_trn": 4.0, "op_9m2024_krw_bn": 313.0, "op_margin_9m2024_pct": 7.8, "new_issuance_use_for_ma_krw_bn": 390.0},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="evidence_good_but_price_failed",
        rerating_result="unknown",
        round_rerating_label="AI_cloud_IT_service_IPO_quality_gate",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="AI_cloud_mix_not_IPO_green",
        price_validation_status="reported_ipo_anchor_not_full_ohlc",
        notes="AI/cloud mix is good evidence, but IPO price failure shows recurring revenue and margin durability are required.",
    ),
    Round277CaseCandidate(
        case_id="r8_loop13_krafton_india_game_platform_option",
        symbol="259960",
        company_name="Krafton / BGMI / India platform option",
        primary_archetype=E2RArchetype.EMERGING_MARKET_GAME_PLATFORM_OPTION,
        secondary_archetypes=(E2RArchetype.GAME_IP_PLATFORM_EXPANSION, E2RArchetype.GAME_CONTENT_IP),
        case_type="success_candidate",
        round_case_type="success_candidate + 4C-watch / India platform option",
        stage1_date=date(2025, 8, 1),
        stage2_date=date(2025, 12, 19),
        stage3_date=None,
        stage4b_date=date(2025, 12, 19),
        stage4c_date=date(2025, 12, 19),
        stage3_decision="india_downloads_and_fund_are_stage2_until_paid_conversion_arpu_regulatory_clearance_second_hit_and_fcf_confirm",
        stage4b_status="4C-watch/regulatory-data-security-and-second-hit-risk",
        hard_4c_confirmed=False,
        evidence_fields=("india_tech_fund_666mn_usd", "bgmi_downloads_240mn", "india_top_five_market", "india_10pct_1h_sales", "india_gamers_444mn"),
        red_flag_fields=("downloads_without_ARPU", "game_regulatory_ban_or_data_security_ban", "second_hit_unconfirmed", "regulatory_data_security_watch"),
        price_data_source="Reuters / FT Krafton India platform anchors",
        reported_price_anchor="$666M India tech fund; BGMI 240M+ downloads",
        reported_return_anchor="ARPU, paid conversion, regulatory clearance and second-hit proof required",
        event_mfe_pct=None,
        event_mae_pct=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"india_tech_fund_total_usd_mn": 666.0, "initial_pool_usd_mn": 333.0, "fund_launch": "2026-01", "krafton_prior_india_investment_usd_mn": 200.0, "bgmi_downloads_mn": 240.0, "annual_india_investment_plan_usd_mn": 50.0, "india_share_of_1h_record_sales_pct": 10.0, "krafton_1h_sales_krw_trn": 1.5, "implied_india_sales_1h_krw_bn": 150.0, "india_gamers_mn": 444.0, "india_gamer_growth_pct": 12.0, "spending_gamer_share_pct": 33.0, "regulatory_data_security_watch": True, "second_hit_confirmed": False},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_regulatory_watch",
        rerating_result="unknown",
        round_rerating_label="emerging_market_game_platform_option",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="downloads_and_market_option_not_ARPU_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="India option is Stage 2; downloads are not ARPU, regulatory clearance, or FCF.",
    ),
    Round277CaseCandidate(
        case_id="r8_loop13_skt_data_breach_cybersecurity_hard_4c",
        symbol="017670",
        company_name="SK Telecom",
        primary_archetype=E2RArchetype.CYBERSECURITY_TRUST_HARD_4C,
        secondary_archetypes=(E2RArchetype.TELECOM_CYBERSECURITY_OPERATIONAL_TRUST_HARD_4C, E2RArchetype.SECURITY_OPERATIONAL_TRUST_HARD_4C),
        case_type="4c_thesis_break",
        round_case_type="4C-thesis-break / cybersecurity trust hard 4C",
        stage1_date=date(2025, 4, 18),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 28),
        stage3_decision="large_customer_data_breach_is_hard_4c_when_revenue_cut_fine_security_investment_and_compensation_follow",
        stage4b_status="hard-4C/cybersecurity-trust-break",
        hard_4c_confirmed=True,
        evidence_fields=("skt_data_breach", "initial_intraday_minus_8_5pct", "26_96mn_data_pieces_leaked", "700bn_krw_security_investment", "800bn_krw_revenue_forecast_cut", "134bn_krw_fine"),
        red_flag_fields=("large_data_breach", "USIM_identity_authentication_leakage", "regulatory_fine", "revenue_forecast_cut_from_trust_event", "customer_compensation_liability"),
        price_data_source="Reuters SK Telecom breach / investigation / fine / compensation anchors",
        reported_price_anchor="26.96M data pieces leaked; 700B KRW security investment; 800B KRW revenue forecast cut",
        reported_return_anchor="Shares -8.5% intraday and -6.7% close after breach; later -5.6% on leak validation",
        event_mfe_pct=None,
        event_mae_pct=-8.5,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"initial_intraday_mae_pct": -8.5, "initial_close_mae_pct": -6.7, "kospi_same_context_pct": 0.1, "relative_underperformance_initial_pp": -6.8, "usim_replacement_users_mn": 23.0, "retail_stores_involved": 2600, "usim_protection_service_signups_mn": 5.54, "leaked_data_pieces_mn": 26.96, "july_event_close_mae_pct": -5.6, "data_protection_investment_krw_bn": 700.0, "august_bill_discount_pct": 50.0, "customers_for_discount_mn": 24.0, "revenue_forecast_cut_krw_bn": 800.0, "customer_benefit_package_cost_krw_bn": 500.0, "pipc_fine_krw_bn": 134.0, "possible_total_compensation_krw_trn": 2.3},
        score_price_alignment="false_positive_score",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="cybersecurity_trust_hard_4C",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="data_breach_cost_revenue_trust_break",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Data breach became revenue cut, security capex, regulatory fine and possible compensation: hard 4C.",
    ),
)


def round277_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND277_CASE_CANDIDATES:
        stage3_terms = ("paid", "arpu", "take_rate", "creator", "recurring", "margin", "fcf", "retention", "governance", "clearance")
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND277_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary="Round277 R8 Loop-13 platform/content/software/security price validation case. Calibration-only; not candidate-generation input.",
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(token in field.lower() for token in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field.lower() for token in ("ipo", "mau", "downloads", "ai", "cloud", "rally", "overheat", "premium", "relief"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field.lower() for token in ("breach", "legal", "governance", "founder", "data", "fine", "forecast", "regulatory", "security", "trust"))),
            must_have_fields=ROUND277_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4b_watch", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND277_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_adjusted_ohlc_complete_false",
                "hard_4c_confirmed_true_for_cybersecurity_trust",
                "do_not_use_round277_cases_as_candidate_generation_input",
                "do_not_treat_mau_ipo_ip_ai_cloud_downloads_or_policy_relief_as_green_alone",
                *ROUND277_GREEN_REQUIRED_FIELDS,
                *ROUND277_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
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
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round277_case_rows() -> tuple[dict[str, str], ...]:
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
            "reported_price_anchor": candidate.reported_price_anchor,
            "reported_return_anchor": candidate.reported_return_anchor,
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
        for candidate in ROUND277_CASE_CANDIDATES
    )


def round277_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND277_SCORE_ADJUSTMENTS)


def round277_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND277_SHADOW_WEIGHT_ROWS)


def round277_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND277_DEEP_SUB_ARCHETYPES)


def round277_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round277_price_validation": "true"} for field in ROUND277_PRICE_VALIDATION_FIELDS)


def round277_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round277_label": label, "canonical_archetype": canonical} for label, canonical in ROUND277_REQUIRED_TARGET_ALIASES.items())


def round277_summary() -> dict[str, int | bool | str]:
    cases = ROUND277_CASE_CANDIDATES
    return {
        "source_round": ROUND277_SOURCE_ROUND_PATH,
        "round_id": ROUND277_ANALYST_ROUND_ID,
        "large_sector": ROUND277_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "watch_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_date is not None or "4B" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None or "4C" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "target_archetype_count": len(ROUND277_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND277_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND277_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_adjusted_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round277_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND277_SOURCE_ROUND_PATH,
        "round_id": ROUND277_ANALYST_ROUND_ID,
        "large_sector": ROUND277_LARGE_SECTOR,
        "summary": round277_summary(),
        "target_aliases": dict(ROUND277_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND277_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND277_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND277_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND277_HARD_4C_GATES),
        "score_adjustments": list(round277_score_adjustment_rows()),
        "shadow_weights": list(round277_shadow_weight_rows()),
        "deep_sub_archetypes": list(round277_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND277_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round277_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_mau_ipo_ip_ai_cloud_downloads_or_policy_relief_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round277_summary_markdown() -> str:
    summary = round277_summary()
    lines = [
        "# Round 277 R8 Loop 13 Platform Content Software Security Price Validation",
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
        f"- 4C-watch / watch rows: {summary['watch_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND277_CASE_CANDIDATES:
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
            "- NAVER/Line Yahoo is data-sovereignty 4C-watch; overseas platform Green needs governance and regulatory clarity.",
            "- Webtoon IPO is Stage 2; MAU and IPO pop need paid conversion, creator economics, OP/FCF and parent value bridge.",
            "- Kakao and HYBE show founder/legal and label governance can block platform/content premium.",
            "- Shift Up and Krafton are Stage 2 options until ARPU, retention, multi-title durability and regulatory clearance appear.",
            "- LG CNS shows AI/cloud revenue mix is not enough when IPO price and margin durability fail.",
            "- SK Telecom is the hard 4C reference for cybersecurity trust break.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round277_green_gate_review_markdown() -> str:
    lines = [
        "# Round 277 R8 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R8 Stage 3-Green is not `MAU`, `IPO`, `K-pop IP`, `game IP`, `AI/cloud`, or `downloads`. It requires paid conversion, ARPU/take-rate, recurring revenue, data governance, cybersecurity trust, regulatory clearance, OP/FCF and price path after evidence.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND277_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND277_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND277_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `Webtoon 170M MAU` is Stage 2; Green needs paid conversion and parent NAVER value bridge.",
            "- `LG CNS cloud/AI 54% sales` is useful evidence; Green still needs recurring margin and FCF.",
            "- `SK Telecom data breach` is hard 4C because revenue guidance, fine, compensation and trust costs followed.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round277_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 277 R8 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND277_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND277_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | company | 4B status | hard 4C | interpretation |", "|---|---|---|---|---|"])
    for case in ROUND277_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.company_name} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round277_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 277 R8 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_adjusted_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, paid conversion, ARPU, take-rate, creator economics, recurring revenue, governance clearance, cybersecurity remediation, margin or FCF where raw data are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND277_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND277_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round277_r8_loop13_reports(
    output_directory: str | Path = ROUND277_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND277_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND277_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round277_case_records(), cases_path),
        "audit": _write_json(round277_audit_payload(), audit_path),
        "summary": output / "round277_r8_loop13_price_validation_summary.md",
        "case_matrix": output / "round277_r8_loop13_case_matrix.csv",
        "target_aliases": output / "round277_r8_loop13_target_aliases.csv",
        "score_adjustments": output / "round277_r8_loop13_score_adjustments.csv",
        "shadow_weights": output / "round277_r8_loop13_shadow_weights.csv",
        "deep_sub_archetypes": output / "round277_r8_loop13_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round277_r8_loop13_price_validation_fields.csv",
        "green_gate_review": output / "round277_r8_loop13_green_gate_review.md",
        "price_validation_plan": output / "round277_r8_loop13_price_validation_plan.md",
        "stage4b_4c_review": output / "round277_r8_loop13_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round277_summary_markdown(), encoding="utf-8")
    _write_csv(round277_case_rows(), paths["case_matrix"])
    _write_csv(round277_target_alias_rows(), paths["target_aliases"])
    _write_csv(round277_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round277_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round277_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round277_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round277_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round277_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round277_stage4b_4c_review_markdown(), encoding="utf-8")
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
