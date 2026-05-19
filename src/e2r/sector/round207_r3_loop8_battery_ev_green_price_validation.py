"""Round-207 R3 Loop-8 battery/EV/green price validation pack.

Round 207 is calibration/evaluation material only. It captures reported price
anchors and contract-quality breaks from ``docs/round/round_207.md``.

Simple example: an ESS LFP contract can be useful Stage 2 evidence. It is not
Stage 3-Green until delivery, GWh/call-off, utilization, OPM, FCF after capex,
and subsidy-excluded earnings quality are visible as-of the replay date.
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


ROUND207_SOURCE_ROUND_PATH = "docs/round/round_207.md"
ROUND207_LARGE_SECTOR = Round10LargeSector.BATTERY_EV_GREEN
ROUND207_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round207_r3_loop8_battery_ev_green_price_validation"
ROUND207_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r3_loop8_round207.jsonl"
ROUND207_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round207_r3_loop8_battery_ev_green_price_validation_audit.json"

ROUND207_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "BATTERY_MATERIALS_CAPEX_OVERHEAT": E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT.value,
    "CATHODE_LONG_CONTRACT_VISIBILITY": E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY.value,
    "BATTERY_CONTRACT_CANCELLATION_4C": E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C.value,
    "BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE": E2RArchetype.BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE.value,
    "ESS_LFP_GRID_STORAGE": E2RArchetype.ESS_LFP_GRID_STORAGE.value,
    "EV_TO_ESS_CAPACITY_REDEPLOYMENT": E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT.value,
    "EV_BATTERY_JV_RESTRUCTURING": E2RArchetype.EV_BATTERY_JV_RESTRUCTURING.value,
    "SEPARATOR_EV_DEMAND_CYCLE": E2RArchetype.SEPARATOR_EV_DEMAND_CYCLE.value,
    "LITHIUM_CYCLE_OVERLAY": E2RArchetype.LITHIUM_CYCLE_OVERLAY.value,
    "EVENT_LITHIUM_PRICE_RALLY": E2RArchetype.EVENT_LITHIUM_PRICE_RALLY.value,
    "CHANNEL_STUFFING_INVENTORY_OVERLAY": E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "THESIS_BREAK_4C": E2RArchetype.THESIS_BREAK_4C.value,
    "LEVERAGE_FCF_BREAKDOWN": E2RArchetype.LEVERAGE_FCF_BREAKDOWN.value,
    "PRECURSOR_SUPPLY_CHAIN": E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT.value,
}

ROUND207_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "binding_contract",
    "actual_calloff",
    "gwh_or_tonnage_volume",
    "utilization_improvement",
    "opm_or_gross_margin_improvement",
    "fcf_after_capex",
    "subsidy_excluded_profit_quality",
    "customer_ev_strategy_risk_passed",
    "price_path_after_evidence",
)

ROUND207_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "customer_name_only",
    "contract_value_headline_only",
    "ess_or_lfp_theme_only",
    "capa_conversion_only",
    "ampc_excluded_profit_missing_or_negative",
    "ev_demand_slowdown_ignored",
    "ipo_or_vertical_integration_story_only",
    "lithium_price_event_only",
)

ROUND207_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "battery_supply_chain_lithium_event_group_rally",
    "ess_lfp_contract_announcement_rally_without_delivery_margin",
    "battery_materials_valuation_expansion_without_calloff",
    "ipo_or_vertical_integration_price_ahead_of_evidence",
    "ampc_included_earnings_surprise_only",
)

ROUND207_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "contract_value_collapse",
    "customer_ev_model_cancellation",
    "customer_strategy_pullback",
    "take_or_pay_absence_confirmed",
    "gwh_calloff_failure",
    "utilization_delay",
    "negative_fcf",
    "debt_burden_or_emergency_management",
    "subsidy_quality_profit_collapse",
    "share_issuance_or_dilution_under_weak_demand",
)

ROUND207_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_price",
    "mfe_1d",
    "mae_1d",
    "mae_1d_secondary",
    "contract_value_drawdown_pct",
    "lost_revenue_vs_prior_revenue_pct",
    "net_debt_increase_pct",
    "loss_worsening_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round207ScoreAdjustment:
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
class Round207CaseCandidate:
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
    mae_1d_secondary: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    peak_price_anchor: float | None
    extra_price_metrics: Mapping[str, float | str]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND207_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND207_SCORE_ADJUSTMENTS: tuple[Round207ScoreAdjustment, ...] = (
    Round207ScoreAdjustment("binding_contract_quality", 5, "raise", "계약이 있어도 binding/call-off 구조가 보일 때만 R3 visibility가 오른다."),
    Round207ScoreAdjustment("actual_calloff", 5, "raise", "L&F 사례처럼 고객명과 계약금액 headline은 call-off가 없으면 무너질 수 있다."),
    Round207ScoreAdjustment("gwh_or_tonnage_volume", 5, "raise", "배터리 계약은 GWh/tonnage와 배송 시점이 확인되어야 매출 경로가 보인다."),
    Round207ScoreAdjustment("utilization_rate", 5, "raise", "EV 라인 전환이나 ESS 증설은 가동률 개선 전까지 Stage 3가 아니다."),
    Round207ScoreAdjustment("opm_visibility", 5, "raise", "OPM 또는 gross margin 개선이 없으면 EPS/FCF 체급 변화가 약하다."),
    Round207ScoreAdjustment("fcf_after_capex", 5, "raise", "CAPEX 이후 FCF가 확인되어야 배터리 Green 후보가 된다."),
    Round207ScoreAdjustment("ess_revenue_conversion", 4, "raise", "ESS 계약은 delivery/revenue conversion이 보일 때 Stage 2를 넘어선다."),
    Round207ScoreAdjustment("customer_quality", 4, "raise", "고객의 EV 전략 지속성과 주문 품질을 따로 확인한다."),
    Round207ScoreAdjustment("subsidy_quality_adjustment", 4, "raise", "AMPC/보조금을 제외한 이익 품질을 분리한다."),
    Round207ScoreAdjustment("ev_theme_only", -5, "lower", "EV 테마만으로는 OPM/FCF 개선을 증명하지 못한다."),
    Round207ScoreAdjustment("ess_theme_only", -4, "lower", "ESS/LFP 전환 기대만 있고 배송·마진이 없으면 Green 금지다."),
    Round207ScoreAdjustment("customer_name_only", -5, "lower", "Tesla/Ford 같은 고객명만으로는 actual call-off를 대체할 수 없다."),
    Round207ScoreAdjustment("contract_value_headline_without_calloff", -5, "lower", "계약금액 headline은 call-off와 매출 인식 전까지 confidence cap이다."),
    Round207ScoreAdjustment("capa_announcement", -4, "lower", "CAPA 발표는 가동률과 FCF 전까지 부담일 수 있다."),
    Round207ScoreAdjustment("subsidy_dependent_profit", -5, "lower", "AMPC 포함 이익만 좋고 제외 이익이 약하면 Green을 막는다."),
    Round207ScoreAdjustment("negative_fcf_or_debt_burden", -5, "lower", "SK온 사례처럼 손실과 부채는 구조적 rerating을 차단한다."),
    Round207ScoreAdjustment("ipo_or_vertical_integration_story", -4, "lower", "전구체/수직계열화/IPO narrative는 외부 고객·가동률·OPM 전까지 부족하다."),
    Round207ScoreAdjustment("lithium_price_event", -4, "lower", "리튬 가격 이벤트는 event premium 또는 cycle로 분리한다."),
)


ROUND207_CASE_CANDIDATES: tuple[Round207CaseCandidate, ...] = (
    Round207CaseCandidate(
        case_id="r3_loop8_lges_ess_pivot_contract_break",
        symbol="373220",
        company_name="LG에너지솔루션",
        primary_archetype=E2RArchetype.ESS_LFP_GRID_STORAGE,
        secondary_archetypes=(
            E2RArchetype.EV_TO_ESS_CAPACITY_REDEPLOYMENT,
            E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C,
            E2RArchetype.BATTERY_TAX_CREDIT_QUALITY_OVERLAY,
        ),
        case_type="success_candidate",
        stage1_date=date(2025, 7, 25),
        stage2_date=date(2025, 7, 30),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 18),
        stage3_decision="ess_lfp_contract_is_stage2_until_delivery_utilization_opm_fcf_and_ampc_excluded_profit_are_visible",
        stage4b_status="none",
        hard_4c_confirmed=True,
        evidence_fields=("q2_op_492bn_krw", "ampc_excluded_op_1_4bn_krw", "tesla_lfp_ess_contract_4_3bn_usd", "delivery_2027_08_to_2030_07", "us_factory_supply"),
        red_flag_fields=("ev_demand_slowdown", "ampc_dependent_profit", "ford_contract_cancellation", "freudenberg_contract_termination", "lost_expected_revenue_13_5tn_krw"),
        price_data_source="Reuters reported event returns and contract anchors",
        reported_price_anchor="no stage2 price anchor; Ford cancellation intraday drop reported",
        reported_return_anchor="-1.6% after Q2 demand warning; -7.6% intraday after Ford cancellation",
        mfe_1d=None,
        mae_1d=-1.6,
        mae_1d_secondary=-7.6,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"lost_expected_revenue_krw_trn": 13.5, "lost_revenue_vs_2024_revenue_pct": 52.7},
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="thesis_break",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="ESS LFP contract is Stage 2; Ford/Freudenberg cancellations and AMPC-dependent profit create 4C-watch/hard 4C evidence.",
    ),
    Round207CaseCandidate(
        case_id="r3_loop8_lnf_tesla_contract_collapse",
        symbol="066970",
        company_name="L&F",
        primary_archetype=E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C,
        secondary_archetypes=(E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY, E2RArchetype.THESIS_BREAK_4C),
        case_type="4c_thesis_break",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2023, 1, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 29),
        stage3_decision="tesla_customer_name_and_contract_value_headline_are_not_green_without_4680_ramp_actual_calloff_and_margin",
        stage4b_status="watch",
        hard_4c_confirmed=True,
        evidence_fields=("tesla_high_nickel_cathode_supply_deal", "tesla_4680_exposure"),
        red_flag_fields=("contract_value_collapse", "customer_ramp_failure", "cybertruck_demand_weakness", "ev_demand_slowdown"),
        price_data_source="Reuters contract value anchor",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="$2.9B expected contract value cut to $7,386",
        mfe_1d=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"contract_value_initial_usd": 2_900_000_000.0, "contract_value_revised_usd": 7_386.0, "contract_value_drawdown_pct": -99.999745},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="false_green",
        price_validation_status="contract_value_anchor_stock_ohlc_unavailable",
        notes="Tesla contract value collapse is a hard 4C benchmark. Customer name and contract value headline are not enough for Green.",
    ),
    Round207CaseCandidate(
        case_id="r3_loop8_samsung_sdi_ess_lfp_stage2",
        symbol="006400",
        company_name="삼성SDI",
        primary_archetype=E2RArchetype.ESS_LFP_GRID_STORAGE,
        secondary_archetypes=(E2RArchetype.BATTERY_CONTRACT_DISCLOSURE_CONFIDENCE, E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY),
        case_type="success_candidate",
        stage1_date=date(2025, 3, 5),
        stage2_date=date(2025, 12, 10),
        stage3_date=None,
        stage4b_date=date(2025, 12, 10),
        stage4c_date=date(2025, 4, 9),
        stage3_decision="confirmed_ess_contract_is_stage2_but_delivery_after_2027_opm_fcf_and_dilution_risk_keep_green_blocked",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("us_lfp_ess_supply_contract_over_2tn_krw", "delivery_from_2027_for_three_years", "ess_event_plus_6_1pct"),
        red_flag_fields=("ev_demand_sluggish_until_h1_2026", "q4_operating_loss", "equity_offering_price_cut", "capex_funding_pressure"),
        price_data_source="Reuters event returns and offering-price anchor",
        reported_price_anchor="offering price cut from 169,200 KRW to 146,200 KRW",
        reported_return_anchor="+6.1% ESS contract intraday; offering price -13.6%; YTD -29.5%",
        mfe_1d=6.1,
        mae_1d=-1.0,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=146200.0,
        peak_price_anchor=None,
        extra_price_metrics={"offering_price_reduction_pct": -13.6, "reported_ytd_drawdown_pct": -29.5},
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="ESS contract is Stage 2; EV demand weakness and capital raise pressure block Stage 3-Green until operating proof appears.",
    ),
    Round207CaseCandidate(
        case_id="r3_loop8_sk_innovation_skon_failed_rerating",
        symbol="096770",
        company_name="SK이노베이션/SK온",
        primary_archetype=E2RArchetype.EV_BATTERY_JV_RESTRUCTURING,
        secondary_archetypes=(E2RArchetype.LEVERAGE_FCF_BREAKDOWN, E2RArchetype.THESIS_BREAK_4C),
        case_type="failed_rerating",
        stage1_date=date(2021, 1, 1),
        stage2_date=date(2024, 8, 27),
        stage3_date=None,
        stage4b_date=date(2024, 8, 27),
        stage4c_date=date(2024, 7, 7),
        stage3_decision="restructuring_relief_is_not_green_when_battery_unit_has_losses_debt_and_parent_support_dependency",
        stage4b_status="watch",
        hard_4c_confirmed=True,
        evidence_fields=("sk_innovation_sk_es_merger_approval", "merger_event_plus_5pct"),
        red_flag_fields=("sk_on_10_consecutive_quarterly_losses", "net_debt_2_9tn_to_15_6tn", "emergency_management", "parent_support_dependency"),
        price_data_source="FT debt/loss anchor and Reuters merger return anchor",
        reported_price_anchor="no stage price anchor",
        reported_return_anchor="+5% merger approval intraday; net debt +437.9%",
        mfe_1d=5.0,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"net_debt_increase_pct": 437.9, "loss_record": "10 consecutive quarters"},
        score_price_alignment="false_positive_score",
        rerating_result="credit_relief_rally",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="SK On loss/debt burden makes SK Innovation a restructuring relief case, not an EV battery Green case.",
    ),
    Round207CaseCandidate(
        case_id="r3_loop8_skiet_separator_demand_break",
        symbol="361610",
        company_name="SK아이이테크놀로지",
        primary_archetype=E2RArchetype.SEPARATOR_EV_DEMAND_CYCLE,
        secondary_archetypes=(E2RArchetype.EV_BATTERY_JV_RESTRUCTURING, E2RArchetype.THESIS_BREAK_4C),
        case_type="failed_rerating",
        stage1_date=date(2021, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 5, 15),
        stage3_decision="separator_essentiality_is_not_green_without_utilization_customer_shipments_opm_and_fcf",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("separator_business", "panasonic_customer_reference", "market_cap_4_09tn_krw"),
        red_flag_fields=("sale_consideration", "ev_demand_weakening", "sk_on_financial_difficulty", "sk_on_loss_worsening"),
        price_data_source="Reuters business event anchor",
        reported_price_anchor="4.09tn KRW market cap as of 2024-05-14",
        reported_return_anchor="SK On Q1 loss widened from 18.6bn KRW to 332.0bn KRW",
        mfe_1d=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"market_cap_anchor_krw_trn": 4.09, "sk_on_loss_worsening_pct": 1684.9},
        score_price_alignment="false_positive_score",
        rerating_result="thesis_break",
        stage_failure_type="should_have_been_red",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Separator demand broke with EV weakness and SK On financial stress; essential material status alone is not E2R visibility.",
    ),
    Round207CaseCandidate(
        case_id="r3_loop8_posco_future_m_lithium_event",
        symbol="003670",
        company_name="포스코퓨처엠",
        primary_archetype=E2RArchetype.LITHIUM_CYCLE_OVERLAY,
        secondary_archetypes=(E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY, E2RArchetype.EVENT_LITHIUM_PRICE_RALLY),
        case_type="event_premium",
        stage1_date=date(2025, 8, 11),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2025, 8, 11),
        stage4c_date=date(2025, 12, 16),
        stage3_decision="lithium_price_event_is_event_premium_until_company_order_quality_opm_and_fcf_are_confirmed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("catl_yichun_lithium_mine_suspension", "lithium_event_plus_8_3pct"),
        red_flag_fields=("lithium_price_event_only", "catl_license_renewal_possible", "ford_ev_strategy_pullback", "customer_ev_strategy_risk"),
        price_data_source="WSJ/Reuters event return anchors",
        reported_price_anchor="no stage price anchor",
        reported_return_anchor="+8.3% CATL lithium event; -8.2% Ford EV retreat shock",
        mfe_1d=8.3,
        mae_1d=-8.2,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Lithium price shock can move the stock, but commodity/event sensitivity is not structural Stage 3 evidence.",
    ),
    Round207CaseCandidate(
        case_id="r3_loop8_ecopro_materials_precursor_overheat",
        symbol="450080",
        company_name="에코프로머티리얼즈",
        primary_archetype=E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT,
        secondary_archetypes=(E2RArchetype.PRICE_ONLY_RALLY, E2RArchetype.CHANNEL_STUFFING_INVENTORY_OVERLAY),
        case_type="overheat",
        stage1_date=date(2023, 11, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 6, 14),
        stage3_decision="precursor_vertical_integration_and_ipo_premium_are_not_green_without_external_customers_utilization_opm_and_fcf",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("precursor_story", "vertical_integration_narrative", "ipo_premium"),
        red_flag_fields=("price_moved_without_evidence", "ev_demand_slowdown", "customer_project_reduction", "utilization_unknown"),
        price_data_source="MarketWatch reported price anchor",
        reported_price_anchor="119,200 KRW after -11% one-day fall; implied prior about 133,933 KRW",
        reported_return_anchor="-11% to 119,200 KRW; about -5% Ford supply-chain event",
        mfe_1d=None,
        mae_1d=-11.0,
        mae_1d_secondary=-5.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=119200.0,
        peak_price_anchor=None,
        extra_price_metrics={"implied_pre_event_reference_price": 133933.0},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="theme_overheat",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="IPO/precursor/vertical integration story is insufficient without external customers, utilization, OPM, and FCF.",
    ),
)


def round207_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND207_CASE_CANDIDATES:
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
                "Round207 R3 Loop-8 battery/EV/green price-path validation "
                "case. Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(field for field in candidate.evidence_fields if "event" in field or "story" in field or "demand" in field),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "contract" in field or "delivery" in field or "ess" in field or "op" in field or "gwh" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "event" in field or "lithium" in field or "ipo" in field or "premium" in field or "rally" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "cancellation" in field
                or "collapse" in field
                or "debt" in field
                or "loss" in field
                or "demand" in field
                or "strategy" in field
                or "dilution" in field
            ),
            must_have_fields=ROUND207_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason=(
                "; ".join(candidate.red_flag_fields)
                if candidate.case_type in {"event_premium", "overheat", "4b_watch", "4c_thesis_break", "failed_rerating"}
                else None
            ),
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={
                "binding_contract_quality_delta": 5.0,
                "actual_calloff_delta": 5.0,
                "gwh_or_tonnage_volume_delta": 5.0,
                "utilization_rate_delta": 5.0,
                "opm_visibility_delta": 5.0,
                "fcf_after_capex_delta": 5.0,
                "ess_revenue_conversion_delta": 4.0,
                "customer_quality_delta": 4.0,
                "subsidy_quality_adjustment_delta": 4.0,
                "ev_theme_only_delta": -5.0,
                "ess_theme_only_delta": -4.0,
                "customer_name_only_delta": -5.0,
                "contract_value_headline_without_calloff_delta": -5.0,
                "capa_announcement_delta": -4.0,
                "subsidy_dependent_profit_delta": -5.0,
                "negative_fcf_or_debt_burden_delta": -5.0,
                "ipo_or_vertical_integration_story_delta": -4.0,
                "lithium_price_event_delta": -4.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_ess_lfp_ev_theme_customer_name_contract_headline_or_lithium_event_as_green_alone",
                *ROUND207_GREEN_REQUIRED_FIELDS,
                *ROUND207_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_price=candidate.peak_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.8 if candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round207_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND207_CASE_CANDIDATES:
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
                "mae_1d_secondary": _float_text(candidate.mae_1d_secondary),
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


def round207_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND207_SCORE_ADJUSTMENTS)


def round207_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round207_price_validation": "true"} for field in ROUND207_PRICE_VALIDATION_FIELDS)


def round207_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round207_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND207_REQUIRED_TARGET_ALIASES.items()
    )


def round207_summary() -> dict[str, int | bool | str]:
    records = round207_case_records()
    return {
        "case_candidate_count": len(records),
        "required_target_count": len(ROUND207_REQUIRED_TARGET_ALIASES),
        "score_adjustment_count": len(ROUND207_SCORE_ADJUSTMENTS),
        "price_validation_field_count": len(ROUND207_PRICE_VALIDATION_FIELDS),
        "success_candidate_count": sum(1 for case in records if case.case_type == "success_candidate"),
        "failed_rerating_count": sum(1 for case in records if case.case_type == "failed_rerating"),
        "event_premium_or_overheat_count": sum(1 for case in records if case.case_type in {"event_premium", "overheat"}),
        "hard_4c_case_count": sum(1 for case in ROUND207_CASE_CANDIDATES if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in ROUND207_CASE_CANDIDATES if case.stage3_date),
        "stage4c_watch_or_hard_count": sum(1 for case in ROUND207_CASE_CANDIDATES if case.stage4c_date),
        "reported_price_anchor_count": sum(
            1 for case in ROUND207_CASE_CANDIDATES if case.price_validation_status != "price_data_unavailable_after_deep_search"
        ),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
    }


def write_round207_r3_loop8_reports(
    *,
    output_directory: str | Path = ROUND207_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND207_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND207_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = write_case_library(round207_case_records(), cases_path)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "audit_json": audit,
        "summary": output / "round207_r3_loop8_price_validation_summary.md",
        "case_matrix": output / "round207_r3_loop8_case_matrix.csv",
        "target_aliases": output / "round207_r3_loop8_target_aliases.csv",
        "score_adjustments": output / "round207_r3_loop8_score_adjustments.csv",
        "price_validation_fields": output / "round207_r3_loop8_price_validation_fields.csv",
        "green_gate_review": output / "round207_r3_loop8_green_gate_review.md",
        "price_validation_plan": output / "round207_r3_loop8_price_validation_plan.md",
        "stage4b_4c_review": output / "round207_r3_loop8_stage4b_4c_review.md",
    }
    audit.write_text(json.dumps(round207_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round207_case_rows(), paths["case_matrix"])
    _write_rows(round207_target_alias_rows(), paths["target_aliases"])
    _write_rows(round207_score_adjustment_rows(), paths["score_adjustments"])
    _write_rows(round207_price_validation_field_rows(), paths["price_validation_fields"])
    paths["summary"].write_text(render_round207_summary_markdown(), encoding="utf-8")
    paths["green_gate_review"].write_text(render_round207_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round207_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round207_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def round207_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND207_SOURCE_ROUND_PATH,
        "large_sector": ROUND207_LARGE_SECTOR.value,
        "summary": round207_summary(),
        "target_aliases": list(round207_target_alias_rows()),
        "green_required_fields": list(ROUND207_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND207_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND207_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND207_HARD_4C_GATES),
        "score_adjustments": list(round207_score_adjustment_rows()),
        "case_ids": [case.case_id for case in ROUND207_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round207_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_ess_lfp_ev_theme_customer_name_contract_headline_lithium_event_or_ipo_story_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
            "keep_full_ohlc_complete_false_until_official_backfill_is_done",
        ],
    }


def render_round207_summary_markdown() -> str:
    summary = round207_summary()
    lines = [
        "# Round-207 R3 Loop-8 Price-Path Validation Summary",
        "",
        f"- source_round: `{ROUND207_SOURCE_ROUND_PATH}`",
        f"- large_sector: `{ROUND207_LARGE_SECTOR.value}`",
        "- scope: ESS LFP contracts, EV demand slowdown, contract cancellation, cathode value collapse, SK On restructuring, lithium event premium, and precursor overheat",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- score_adjustment_count: {summary['score_adjustment_count']}",
        f"- price_validation_field_count: {summary['price_validation_field_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- failed_rerating_count: {summary['failed_rerating_count']}",
        f"- event_premium_or_overheat_count: {summary['event_premium_or_overheat_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- stage3_case_count: {summary['stage3_case_count']}",
        f"- stage4c_watch_or_hard_count: {summary['stage4c_watch_or_hard_count']}",
        f"- reported_price_anchor_count: {summary['reported_price_anchor_count']}",
        "- production_scoring_changed: false",
        "- candidate_generation_input: false",
        "- shadow_weight_only: true",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Interpretation",
        "",
        "- LG에너지솔루션과 삼성SDI의 ESS/LFP 계약은 Stage 2 후보지만, 배송·가동률·OPM·FCF 확인 전 Green은 보류한다.",
        "- L&F는 Tesla 계약가치 붕괴로 `contract_value_collapse` hard 4C 기준점이다.",
        "- SK이노베이션/SK온과 SKIET는 EV 배터리 성장 thesis가 손실·부채·수요 둔화로 깨질 때의 failed rerating 사례다.",
        "- 포스코퓨처엠 리튬 이벤트와 에코프로머티리얼즈 전구체 narrative는 event premium/overheat로 분리한다.",
        "",
        "쉬운 예: `as_of_date=2025-07-30`에 LGES가 43억 달러 ESS 계약을 발표했더라도, 2027년 이후 배송·마진·FCF가 아직 없으면 Stage 3-Green이 아니라 Stage 2 watch다.",
    ]
    return "\n".join(lines) + "\n"


def render_round207_green_gate_review_markdown() -> str:
    lines = ["# Round-207 R3 Loop-8 Green Gate Review", "", "## Green Required Evidence", ""]
    lines.extend(f"- `{field}`" for field in ROUND207_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Green Forbidden Patterns", ""])
    lines.extend(f"- `{field}`" for field in ROUND207_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "| --- | --- | ---: | --- |"])
    for adjustment in ROUND207_SCORE_ADJUSTMENTS:
        lines.append(f"| `{adjustment.axis}` | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these weights to production scoring yet.",
            "- Do not use Round207 cases as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds to force promotion.",
            "- Do not invent full OHLC, stage prices, or MFE/MAE when only reported anchors exist.",
            "- Do not treat EV/ESS theme, customer name, contract headline, CAPA conversion, lithium event, or IPO story as Green evidence alone.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round207_price_validation_plan_markdown() -> str:
    lines = ["# Round-207 R3 Loop-8 Price Validation Plan", "", "## Required Fields", ""]
    lines.extend(f"- `{field}`" for field in ROUND207_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | price data source | reported anchor | status |", "| --- | --- | --- | --- |"])
    for case in ROUND207_CASE_CANDIDATES:
        lines.append(
            f"| `{case.case_id}` | {case.price_data_source} | {case.reported_return_anchor} | `{case.price_validation_status}` |"
        )
    lines.extend(
        [
            "",
            "## Backfill Rule",
            "",
            "- Use reported Reuters/WSJ/FT/MarketWatch anchors only for fields they explicitly support.",
            "- Keep full OHLC unavailable until official or adjusted daily price backfill is done.",
            "- Separate Stage 2 ESS/contract evidence, Green-required operating proof, 4B event premium, and 4C contract-quality breaks.",
            "- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round207_stage4b_4c_review_markdown() -> str:
    lines = ["# Round-207 R3 Loop-8 Stage 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- `{field}`" for field in ROUND207_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- `{field}`" for field in ROUND207_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## R3 Loop-8 Interpretation",
            "",
            "- ESS/LFP contract rally는 delivery·utilization·OPM·FCF 전까지 4B-watch도 함께 본다.",
            "- 계약 취소와 계약가치 붕괴는 R3에서 가장 강한 4C gate다.",
            "- 리튬 가격 이벤트와 IPO/전구체 narrative는 Green이 아니라 event premium 또는 overheat로 분리한다.",
            "- AMPC 포함 이익은 보조금 제외 이익 품질을 확인하기 전까지 confidence cap을 둔다.",
            "",
            "## Case Review",
            "",
            "| case | 4B status | hard 4C confirmed | interpretation |",
            "| --- | --- | --- | --- |",
        ]
    )
    for case in ROUND207_CASE_CANDIDATES:
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


def _float_text(value: float | None) -> str:
    return "" if value is None else str(value)


__all__ = [
    "ROUND207_CASE_CANDIDATES",
    "ROUND207_DEFAULT_AUDIT_PATH",
    "ROUND207_DEFAULT_CASES_PATH",
    "ROUND207_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND207_GREEN_FORBIDDEN_PATTERNS",
    "ROUND207_GREEN_REQUIRED_FIELDS",
    "ROUND207_HARD_4C_GATES",
    "ROUND207_PRICE_VALIDATION_FIELDS",
    "ROUND207_REQUIRED_TARGET_ALIASES",
    "ROUND207_SCORE_ADJUSTMENTS",
    "ROUND207_SOURCE_ROUND_PATH",
    "ROUND207_STAGE4B_WATCH_TRIGGERS",
    "Round207CaseCandidate",
    "Round207ScoreAdjustment",
    "render_round207_green_gate_review_markdown",
    "render_round207_price_validation_plan_markdown",
    "render_round207_stage4b_4c_review_markdown",
    "render_round207_summary_markdown",
    "round207_audit_payload",
    "round207_case_records",
    "round207_case_rows",
    "round207_price_validation_field_rows",
    "round207_score_adjustment_rows",
    "round207_summary",
    "round207_target_alias_rows",
    "write_round207_r3_loop8_reports",
]
