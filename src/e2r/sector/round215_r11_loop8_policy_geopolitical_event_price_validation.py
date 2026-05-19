"""Round-215 R11 Loop-8 policy/geopolitical/event price validation pack.

Round 215 is calibration/evaluation material only. It structures
``docs/round/round_215.md`` into case records, reported anchors, and shadow
scoring notes.

Easy example: an offshore resource headline can move Korea Gas +30% intraday.
It is still Stage 1/event premium until drilling results, commerciality,
development plan, production timeline, and revenue conversion are visible.
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


ROUND215_SOURCE_ROUND_PATH = "docs/round/round_215.md"
ROUND215_LARGE_SECTOR = Round10LargeSector.POLICY_GEOPOLITICAL_EVENT
ROUND215_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round215_r11_loop8_policy_geopolitical_event_price_validation"
ROUND215_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r11_loop8_round215.jsonl"
ROUND215_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round215_r11_loop8_policy_geopolitical_event_price_validation_audit.json"
ROUND215_DEFAULT_STAGE3_BIAS = "very_conservative"

ROUND215_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "DOMESTIC_RESOURCE_DISCOVERY_EVENT": E2RArchetype.DOMESTIC_RESOURCE_DISCOVERY_EVENT.value,
    "ENERGY_SECURITY_POLICY_EVENT": E2RArchetype.ENERGY_SECURITY_POLICY_EVENT.value,
    "NUCLEAR_POLICY_TO_CONTRACT": E2RArchetype.NUCLEAR_POLICY_TO_CONTRACT.value,
    "SMR_AI_POWER_POLICY_EVENT": E2RArchetype.SMR_AI_POWER_POLICY_EVENT.value,
    "GEOPOLITICAL_SHIPBUILDING_POLICY": E2RArchetype.GEOPOLITICAL_SHIPBUILDING_POLICY.value,
    "US_SHIPBUILDING_REBUILD_POLICY": E2RArchetype.US_SHIPBUILDING_REBUILD_POLICY.value,
    "EVENT_DISEASE_PEST_DEMAND": E2RArchetype.EVENT_DISEASE_PEST_DEMAND.value,
    "SPECULATIVE_SCIENCE_THEME": E2RArchetype.SPECULATIVE_SCIENCE_THEME.value,
    "MARKET_STRUCTURE_SHORT_SELLING_POLICY": E2RArchetype.MARKET_STRUCTURE_SHORT_SELLING_POLICY.value,
    "POLICY_MARKET_SHOCK_EVENT": E2RArchetype.POLICY_MARKET_SHOCK_EVENT.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
    "THESIS_BREAK_4C": E2RArchetype.THESIS_BREAK_4C.value,
}

ROUND215_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "event_escalated_to_company_contract",
    "funded_budget_or_contract_amount",
    "financing_secured",
    "procurement_award_or_actual_order",
    "revenue_conversion_visible",
    "margin_or_eps_fcf_revision_visible",
    "repeat_demand_not_event_fade",
    "price_path_after_evidence",
)

ROUND215_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_news_only",
    "mou_only",
    "geopolitical_headline_only",
    "resource_estimate_without_drilling",
    "disease_import_ban_only",
    "preprint_or_science_claim_only",
    "government_announcement_basket_rally_only",
    "market_structure_reform_without_earnings",
    "price_rally_before_contract",
    "event_fade_risk",
)

ROUND215_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "same_day_limit_up_or_intraday_spike",
    "policy_mou_resource_theme_basket_rally",
    "science_preprint_theme_rally",
    "disease_disaster_event_5d_20d_spike",
    "mou_priced_as_contract",
    "theme_reports_before_contract",
)

ROUND215_HARD_4C_GATES: tuple[str, ...] = (
    "drilling_failure",
    "commerciality_absent",
    "mou_failure",
    "budget_not_funded",
    "policy_reversal",
    "import_restriction_eased",
    "independent_replication_failure",
    "regulatory_reversal",
    "political_shock",
    "market_structure_reform_failure",
    "contract_cancellation",
    "financing_failure",
)

ROUND215_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "event_peak_price",
    "event_mfe_1d_pct",
    "reported_mfe_3m_pct",
    "macro_market_mae_pct",
    "contract_or_budget_amount",
    "event_duration_days",
    "validation_or_replication_status",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round215ScoreAdjustment:
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
class Round215CaseCandidate:
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
    price_data_source: str
    reported_price_anchor: str
    reported_return_anchor: str
    mfe_1d: float | None
    mae_1d: float | None
    mfe_90d: float | None
    stage1_price_anchor: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4c_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str | bool]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND215_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND215_SCORE_ADJUSTMENTS: tuple[Round215ScoreAdjustment, ...] = (
    Round215ScoreAdjustment("funded_budget", 5, "raise", "정책 이벤트는 예산이 배정돼야 Stage 2 이상으로 간다."),
    Round215ScoreAdjustment("actual_contract", 5, "raise", "MOU보다 실제 계약과 발주가 중요하다."),
    Round215ScoreAdjustment("revenue_conversion", 5, "raise", "정책 뉴스가 매출과 EPS/FCF로 내려와야 한다."),
    Round215ScoreAdjustment("financing_secured", 5, "raise", "자원·원전·조선·인프라 이벤트는 financing 확인이 필요하다."),
    Round215ScoreAdjustment("procurement_award", 4, "raise", "정부·국방·원전 정책은 조달계약이 Stage 2 증거다."),
    Round215ScoreAdjustment("commerciality_confirmed", 5, "raise", "자원 발견은 상업성이 확인되기 전 Green 금지다."),
    Round215ScoreAdjustment("independent_replication_or_validation", 5, "raise", "과학 테마는 독립 검증 전 Stage 1이다."),
    Round215ScoreAdjustment("event_to_contract_escalation", 5, "raise", "정책이 계약으로 승격되는 순간만 긍정적으로 본다."),
    Round215ScoreAdjustment("policy_durability", 4, "raise", "정책 지속성과 법적 안정성이 있어야 한다."),
    Round215ScoreAdjustment("policy_news_only", -5, "lower", "정책 뉴스만으로는 Stage 3-Green 금지다."),
    Round215ScoreAdjustment("mou_only", -5, "lower", "MOU는 계약이 아니다."),
    Round215ScoreAdjustment("geopolitical_headline_only", -5, "lower", "지정학 headline만으로 EPS/FCF가 생기지 않는다."),
    Round215ScoreAdjustment("resource_estimate_without_drilling", -5, "lower", "시추 전 자원 추정은 event premium이다."),
    Round215ScoreAdjustment("preprint_or_science_claim_only", -5, "lower", "preprint만으로는 Green 금지다."),
    Round215ScoreAdjustment("disease_import_ban_only", -4, "lower", "질병·수입금지 이벤트는 빠르게 fade될 수 있다."),
    Round215ScoreAdjustment("market_structure_reform_without_earnings", -3, "lower", "시장구조 개선은 개별 기업 이익 전까지 overlay다."),
    Round215ScoreAdjustment("price_rally_before_contract", -5, "lower", "계약 전 가격 급등은 4B-watch다."),
    Round215ScoreAdjustment("event_fade_risk", -5, "lower", "이벤트가 완화되면 Stage 4C/fade로 본다."),
)


ROUND215_CASE_CANDIDATES: tuple[Round215CaseCandidate, ...] = (
    Round215CaseCandidate(
        case_id="r11_loop8_kogas_east_sea_resource_event",
        symbol="036460",
        company_name="한국가스공사",
        primary_archetype=E2RArchetype.DOMESTIC_RESOURCE_DISCOVERY_EVENT,
        secondary_archetypes=(E2RArchetype.ENERGY_SECURITY_POLICY_EVENT, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="event_premium",
        stage1_date=date(2024, 6, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2024, 6, 3),
        stage4c_date=None,
        stage3_decision="resource_estimate_and_drilling_approval_are_stage1_until_drilling_commerciality_and_revenue_conversion",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("east_sea_oil_gas_drilling_approval", "resource_estimate_up_to_14bn_barrels", "event_peak_price_38700_krw"),
        red_flag_fields=("resource_estimate_without_drilling", "commerciality_unknown", "drilling_cost_burden", "price_rally_before_commerciality"),
        price_data_source="WSJ reported intraday price anchor",
        reported_price_anchor="38,700 KRW intraday event peak",
        reported_return_anchor="Korea Gas intraday +30.0%",
        mfe_1d=30.0,
        mae_1d=None,
        mfe_90d=None,
        stage1_price_anchor=38700.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={
            "event_peak_price_krw": 38700.0,
            "event_mfe_1d_pct": 30.0,
            "implied_pre_event_reference_price_krw": 29769.0,
            "drilling_cost_per_attempt_krw_bn": 100.0,
            "potential_resource_barrels_bn": 14.0,
        },
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Resource estimate and drilling approval are Stage 1/event premium until commerciality and revenue conversion.",
    ),
    Round215CaseCandidate(
        case_id="r11_loop8_doosan_nuclear_policy_to_contract",
        symbol="034020",
        company_name="두산에너빌리티",
        primary_archetype=E2RArchetype.NUCLEAR_POLICY_TO_CONTRACT,
        secondary_archetypes=(E2RArchetype.SMR_AI_POWER_POLICY_EVENT, E2RArchetype.NUCLEAR_EXPORT_LEGAL_GATE),
        case_type="success_candidate",
        stage1_date=date(2024, 7, 17),
        stage2_date=date(2025, 6, 4),
        stage3_date=None,
        stage4b_date=date(2024, 7, 17),
        stage4c_date=date(2025, 5, 6),
        stage3_decision="preferred_bidder_and_final_contract_are_stage2_until_doosan_equipment_backlog_margin_eps_revision_and_cashflow_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("czech_nuclear_preferred_bidder", "czech_contract_signed_407bn_koruna", "smr_x_energy_aws_fermi_cooperation", "reported_mfe_3m_48pct"),
        red_flag_fields=("court_or_legal_delay", "smr_mou_without_order", "equipment_backlog_unverified", "price_rally_before_backlog"),
        price_data_source="Reuters/AP reported return and contract anchors",
        reported_price_anchor="Absolute Doosan price unavailable; reported +48% over 3 months",
        reported_return_anchor="Doosan Enerbility +48% over 3 months; Czech contract 407B koruna / $18.7B",
        mfe_1d=None,
        mae_1d=None,
        mfe_90d=48.0,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={
            "reported_mfe_90d_pct": 48.0,
            "signed_contract_value_koruna_bn": 407.0,
            "signed_contract_value_usd_bn": 18.7,
            "reactor_count": 2.0,
            "contract_value_per_reactor_koruna_bn": 203.5,
            "initial_unit_cost_estimate_koruna_bn": 200.0,
        },
        score_price_alignment="aligned",
        rerating_result="policy_event_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="Policy-to-contract reached Stage 2; Doosan equipment backlog, margin, and EPS revision are required for Stage 3.",
    ),
    Round215CaseCandidate(
        case_id="r11_loop8_hd_hyundai_masga_shipbuilding_event",
        symbol="329180/010620",
        company_name="HD현대중공업/HD현대미포",
        primary_archetype=E2RArchetype.US_SHIPBUILDING_REBUILD_POLICY,
        secondary_archetypes=(E2RArchetype.GEOPOLITICAL_SHIPBUILDING_POLICY, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        stage1_date=date(2025, 4, 1),
        stage2_date=date(2025, 8, 27),
        stage3_date=None,
        stage4b_date=date(2025, 8, 27),
        stage4c_date=None,
        stage3_decision="masga_merger_and_mou_are_stage2_until_funded_order_contract_amount_margin_and_revenue_conversion_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("masga_shipbuilding_policy", "hd_hyundai_heavy_mipo_merger", "record_high_event_return", "us_korea_shipbuilding_cooperation"),
        red_flag_fields=("mou_only", "funded_order_unverified", "integration_cost_watch", "price_rally_before_contract"),
        price_data_source="Reuters reported event return anchor",
        reported_price_anchor="Both HD Hyundai Heavy and HD Hyundai Mipo closed at record highs",
        reported_return_anchor="HD Hyundai Heavy +11.3%; HD Hyundai Mipo +14.6%",
        mfe_1d=14.6,
        mae_1d=None,
        mfe_90d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={
            "hd_hyundai_heavy_event_mfe_1d_pct": 11.3,
            "hd_hyundai_mipo_event_mfe_1d_pct": 14.6,
            "record_high_status": True,
            "share_exchange_ratio_mipo_per_heavy": 1.04059146,
        },
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="MASGA, merger, and MOU are Stage 2 and 4B-watch until funded orders and margins appear.",
    ),
    Round215CaseCandidate(
        case_id="r11_loop8_poultry_bird_flu_import_ban_event",
        symbol="Harim/Maniker_basket",
        company_name="Poultry basket",
        primary_archetype=E2RArchetype.EVENT_DISEASE_PEST_DEMAND,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM, E2RArchetype.THESIS_BREAK_4C),
        case_type="event_premium",
        stage1_date=date(2025, 5, 19),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 5, 19),
        stage4c_date=date(2025, 6, 23),
        stage3_decision="bird_flu_import_ban_is_stage1_until_domestic_volume_price_feed_cost_inventory_and_opm_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("brazil_bird_flu_import_restriction", "domestic_poultry_substitution_theme"),
        red_flag_fields=("disease_import_ban_only", "import_restriction_eased", "one_off_demand_fade", "stock_anchor_unavailable"),
        price_data_source="Reuters disease/import-restriction evidence",
        reported_price_anchor="Korean poultry stock reaction anchor unavailable",
        reported_return_anchor="Korea eased restrictions after 35 calendar days",
        mfe_1d=None,
        mae_1d=None,
        mfe_90d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={
            "brazil_2024_poultry_exports_mn_tons": 5.0,
            "eu_share_of_brazil_exports_pct": 4.4,
            "event_duration_days": 35.0,
        },
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Disease import ban is one-off Stage 1; restriction easing is event fade.",
    ),
    Round215CaseCandidate(
        case_id="r11_loop8_lk99_speculative_science_break",
        symbol="superconductor_basket",
        company_name="LK-99 초전도체 basket",
        primary_archetype=E2RArchetype.SPECULATIVE_SCIENCE_THEME,
        secondary_archetypes=(E2RArchetype.PRICE_ONLY_RALLY, E2RArchetype.THESIS_BREAK_4C),
        case_type="overheat",
        stage1_date=date(2023, 7, 22),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2023, 8, 1),
        stage4c_date=date(2023, 8, 7),
        stage3_decision="preprint_is_stage1_and_independent_replication_failure_is_4c_thesis_break",
        stage4b_status="watch",
        hard_4c_confirmed=True,
        evidence_fields=("lk99_arxiv_preprint", "room_temperature_superconductor_claim"),
        red_flag_fields=("preprint_or_science_claim_only", "independent_replication_failure", "commercial_path_absent", "speculative_science_theme_rally"),
        price_data_source="arXiv / LK-99 scientific evidence",
        reported_price_anchor="Korean superconductor basket OHLC anchor unavailable",
        reported_return_anchor="Claim to negative replication: 16 calendar days",
        mfe_1d=None,
        mae_1d=None,
        mfe_90d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={
            "claim_to_negative_replication_days": 16.0,
            "claim_date": "2023-07-22",
            "negative_replication_date": "2023-08-07",
        },
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Preprint is Stage 1; independent replication failure is 4C/thesis break.",
    ),
    Round215CaseCandidate(
        case_id="r11_loop8_martial_law_macro_market_shock",
        symbol="KOSPI_macro",
        company_name="Korea market macro shock",
        primary_archetype=E2RArchetype.POLICY_MARKET_SHOCK_EVENT,
        secondary_archetypes=(E2RArchetype.POLICY_MARKET_SHOCK_OVERLAY, E2RArchetype.THESIS_BREAK_4C),
        case_type="failed_rerating",
        stage1_date=date(2024, 12, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 4),
        stage3_decision="martial_law_shock_is_macro_redteam_overlay_not_company_stage3_signal",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("emergency_martial_law_declaration", "market_stabilization_fund_10tn_krw", "unlimited_liquidity_support"),
        red_flag_fields=("political_shock", "fx_volatility", "foreign_outflow_risk", "policy_stability_risk"),
        price_data_source="Reuters macro-market event anchors",
        reported_price_anchor="KOSPI broad-market event anchor",
        reported_return_anchor="KOSPI nearly -2%; YTD drawdown context more than -7%",
        mfe_1d=None,
        mae_1d=-2.0,
        mfe_90d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={
            "kospi_event_mae_pct": -2.0,
            "kospi_ytd_drawdown_context_pct": -7.0,
            "market_stabilization_fund_krw_trn": 10.0,
            "liquidity_support": "unlimited",
        },
        score_price_alignment="false_positive_score",
        rerating_result="no_rerating",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_macro_anchor_not_full_ohlc",
        notes="Macro overlay; do not convert it into company-specific Stage 3/4C without direct exposure.",
    ),
    Round215CaseCandidate(
        case_id="r11_loop8_short_selling_msci_market_structure",
        symbol="market_structure_basket",
        company_name="Short-selling / MSCI accessibility",
        primary_archetype=E2RArchetype.MARKET_STRUCTURE_SHORT_SELLING_POLICY,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM,),
        case_type="success_candidate",
        stage1_date=date(2025, 3, 1),
        stage2_date=date(2025, 6, 20),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="market_structure_improvement_is_stage2_overlay_until_foreign_inflow_trading_value_brokerage_earnings_and_market_multiple_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("short_selling_ban_lifted", "msci_short_selling_accessibility_improved", "market_accessibility_watch"),
        red_flag_fields=("market_structure_reform_without_earnings", "msci_watchlist_probability_below_50pct", "fx_access_issue_remaining"),
        price_data_source="Reuters market-structure evidence",
        reported_price_anchor="Securities basket stock reaction anchor unavailable",
        reported_return_anchor="Short-selling accessibility improved after five-year ban lifted",
        mfe_1d=None,
        mae_1d=None,
        mfe_90d=None,
        stage1_price_anchor=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={
            "short_selling_ban_period_years": 5.0,
            "watchlist_probability_context_pct": 50.0,
        },
        score_price_alignment="unknown",
        rerating_result="policy_event_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Market accessibility is Stage 2 overlay; company EPS or brokerage revenue is needed for Stage 3.",
    ),
)


def round215_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND215_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=candidate.large_sector,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round215 R11 Loop-8 policy/geopolitical/event price-path "
                "validation case. Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "policy" in field
                or "event" in field
                or "claim" in field
                or "approval" in field
                or "declaration" in field
                or "restriction" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "contract" in field
                or "funded" in field
                or "revenue" in field
                or "backlog" in field
                or "accessibility" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "rally" in field or "price" in field or "theme" in field or "mou" in field or "event" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "failure" in field
                or "delay" in field
                or "fade" in field
                or "shock" in field
                or "reversal" in field
                or "commerciality" in field
                or "restriction_eased" in field
                or "replication" in field
            ),
            must_have_fields=ROUND215_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4c_thesis_break"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={
                "funded_budget_delta": 5.0,
                "actual_contract_delta": 5.0,
                "revenue_conversion_delta": 5.0,
                "financing_secured_delta": 5.0,
                "procurement_award_delta": 4.0,
                "commerciality_confirmed_delta": 5.0,
                "independent_replication_or_validation_delta": 5.0,
                "event_to_contract_escalation_delta": 5.0,
                "policy_durability_delta": 4.0,
                "policy_news_only_delta": -5.0,
                "mou_only_delta": -5.0,
                "geopolitical_headline_only_delta": -5.0,
                "resource_estimate_without_drilling_delta": -5.0,
                "preprint_or_science_claim_only_delta": -5.0,
                "disease_import_ban_only_delta": -4.0,
                "market_structure_reform_without_earnings_delta": -3.0,
                "price_rally_before_contract_delta": -5.0,
                "event_fade_risk_delta": -5.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "r11_default_stage3_bias_very_conservative",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_policy_mou_resource_disaster_science_or_market_structure_event_as_green_alone",
                *ROUND215_GREEN_REQUIRED_FIELDS,
                *ROUND215_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage1_price=candidate.stage1_price_anchor,
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage1_price_anchor if candidate.stage4b_date else None,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mfe_90d=candidate.mfe_90d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=candidate.stage1_price_anchor is not None
                or candidate.stage2_price_anchor is not None
                or candidate.mfe_1d is not None
                or candidate.mae_1d is not None
                or candidate.mfe_90d is not None,
                stage_dates_confidence=0.8 if candidate.stage1_date or candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round215_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND215_CASE_CANDIDATES:
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
                "price_data_source": candidate.price_data_source,
                "reported_price_anchor": candidate.reported_price_anchor,
                "reported_return_anchor": candidate.reported_return_anchor,
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mae_1d": _float_text(candidate.mae_1d),
                "mfe_90d": _float_text(candidate.mfe_90d),
                "stage1_price_anchor": _float_text(candidate.stage1_price_anchor),
                "extra_price_metrics": json.dumps(candidate.extra_price_metrics, ensure_ascii=False, sort_keys=True),
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


def round215_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND215_SCORE_ADJUSTMENTS)


def round215_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round215_price_validation": "true"} for field in ROUND215_PRICE_VALIDATION_FIELDS)


def round215_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round215_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND215_REQUIRED_TARGET_ALIASES.items()
    )


def round215_summary() -> dict[str, int | bool | str]:
    cases = ROUND215_CASE_CANDIDATES
    return {
        "source_round": ROUND215_SOURCE_ROUND_PATH,
        "large_sector": ROUND215_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "price_moved_without_evidence_count": sum(
            1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"
        ),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "target_archetype_count": len(ROUND215_REQUIRED_TARGET_ALIASES),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "r11_default_stage3_bias": ROUND215_DEFAULT_STAGE3_BIAS,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
    }


def round215_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND215_SOURCE_ROUND_PATH,
        "large_sector": ROUND215_LARGE_SECTOR.value,
        "summary": round215_summary(),
        "target_aliases": dict(ROUND215_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND215_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND215_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND215_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND215_HARD_4C_GATES),
        "what_not_to_change": [
            "do_not_use_round215_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_policy_mou_resource_disaster_science_or_market_structure_event_as_green",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round215_summary_markdown() -> str:
    summary = round215_summary()
    lines = [
        "# Round 215 R11 Loop 8 Policy Geopolitical Event Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- r11_default_stage3_bias: {summary['r11_default_stage3_bias']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | stage2 | stage3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND215_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.case_type,
                    _date_text(case.stage2_date),
                    _date_text(case.stage3_date),
                    _date_text(case.stage4b_date),
                    _date_text(case.stage4c_date),
                    case.score_price_alignment,
                    case.notes,
                )
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- R11 default is event premium, not Stage 3-Green.",
            "- Korea Gas East Sea resource event is Stage 1/4B-watch until drilling and commerciality confirm.",
            "- Doosan nuclear policy-to-contract can reach Stage 2, but equipment backlog and margin are still required.",
            "- MASGA/shipbuilding policy, poultry disease events, and market-structure reform need company earnings conversion.",
            "- LK-99 shows preprint-only science themes need independent replication before any promotion.",
            "- Martial-law shock is macro RedTeam overlay, not a company-specific Stage 3 signal.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round215_green_gate_review_markdown() -> str:
    lines = [
        "# Round 215 R11 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND215_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND215_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `Resource discovery approval` means Stage 1 routing.",
            "- `funded contract + financing + revenue conversion + EPS/FCF revision` is the bundle that can support Stage 3.",
            "- `preprint only` remains Stage 1; independent replication failure is 4C/thesis break.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round215_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 215 R11 4B/4C Review",
        "",
        "## 4B Watch Triggers",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND215_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND215_HARD_4C_GATES)
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND215_CASE_CANDIDATES:
        if case.stage4b_status == "watch" or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round215_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 215 R11 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- r11_default_stage3_bias: very_conservative",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND215_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round215_r11_loop8_reports(
    output_directory: str | Path = ROUND215_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND215_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND215_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)

    paths = {
        "cases": write_case_library(round215_case_records(), cases_path),
        "audit": _write_json(round215_audit_payload(), audit_path),
        "summary": output / "round215_r11_loop8_price_validation_summary.md",
        "case_matrix": output / "round215_r11_loop8_case_matrix.csv",
        "target_aliases": output / "round215_r11_loop8_target_aliases.csv",
        "score_adjustments": output / "round215_r11_loop8_score_adjustments.csv",
        "price_validation_fields": output / "round215_r11_loop8_price_validation_fields.csv",
        "green_gate_review": output / "round215_r11_loop8_green_gate_review.md",
        "price_validation_plan": output / "round215_r11_loop8_price_validation_plan.md",
        "stage4b_4c_review": output / "round215_r11_loop8_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round215_summary_markdown(), encoding="utf-8")
    _write_csv(round215_case_rows(), paths["case_matrix"])
    _write_csv(round215_target_alias_rows(), paths["target_aliases"])
    _write_csv(round215_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round215_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round215_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round215_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round215_stage4b_4c_review_markdown(), encoding="utf-8")
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
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return target


def _date_text(value: date | None) -> str:
    return value.isoformat() if value else ""


def _float_text(value: float | None) -> str:
    return "" if value is None else f"{value:g}"
