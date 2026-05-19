"""Round-218 R1 Loop-9 industrial orders and infrastructure price validation.

Round 218 is calibration/evaluation material only. It turns the analyst's
industrial-infra price anchors into structured case records, shadow weights,
and Green/4B/4C guardrails.

Easy example: HD Hyundai Marine Solution may be a useful ship-MRO platform, but
an IPO first-day +96.5% move is not Stage 3 evidence. It is a 4B/event-premium
warning until recurring MRO revenue, margin, FCF, and price path are visible.
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


ROUND218_SOURCE_ROUND_PATH = "docs/round/round_218.md"
ROUND218_LARGE_SECTOR = "INDUSTRIAL_ORDERS_INFRA"
ROUND218_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round218_r1_loop9_industrial_infra_price_validation"
ROUND218_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r1_loop9_round218.jsonl"
ROUND218_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round218_r1_loop9_industrial_infra_price_validation_audit.json"

ROUND218_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "GRID_POWER_EQUIPMENT_AI_DATACENTER": E2RArchetype.GRID_POWER_EQUIPMENT_AI_DATACENTER.value,
    "TRANSFORMER_CAPACITY_BOTTLENECK": E2RArchetype.TRANSFORMER_CAPACITY_BOTTLENECK.value,
    "POWER_EQUIPMENT_EXPORT_US_GRID": E2RArchetype.POWER_EQUIPMENT_EXPORT_US_GRID.value,
    "OVERSEAS_EPC_CONTRACT_BACKLOG": E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG.value,
    "EPC_LOW_MARGIN_ORDER_OVERLAY": E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY.value,
    "NUCLEAR_POLICY_TO_EQUIPMENT_BACKLOG": E2RArchetype.NUCLEAR_POLICY_TO_EQUIPMENT_BACKLOG.value,
    "SHIPBUILDING_US_POLICY_MASGA": E2RArchetype.SHIPBUILDING_US_POLICY_MASGA.value,
    "SHIP_MRO_RECURRING_PLATFORM": E2RArchetype.SHIP_MRO_RECURRING_PLATFORM.value,
    "GEOPOLITICAL_SHIPBUILDING_SANCTION": E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION.value,
    "IPO_EVENT_PREMIUM": E2RArchetype.IPO_EVENT_PREMIUM.value,
    "CONTRACT_HEADLINE_NOT_STAGE3": E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "THESIS_BREAK_4C_WATCH": E2RArchetype.THESIS_BREAK_4C_WATCH.value,
}

ROUND218_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "company_order_or_contract_confirmed",
    "contract_amount_customer_delivery_visible",
    "actual_delivery_or_revenue_recognition_confirmed",
    "margin_and_cost_control_confirmed",
    "backlog_to_revenue_conversion_confirmed",
    "eps_revision_or_fcf_path_confirmed",
    "price_path_after_evidence_confirmed",
    "geopolitical_financing_dilution_risk_passed",
    "no_hard_redteam",
)

ROUND218_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "policy_news_only",
    "mou_or_merger_policy_only",
    "contract_headline_without_margin",
    "epc_order_without_cost_control",
    "transformer_sector_data_without_company_order",
    "nuclear_preferred_bidder_without_equipment_backlog",
    "shipbuilding_policy_theme_without_funded_order",
    "sanctions_or_geopolitical_trust_break",
    "ipo_event_premium_only",
    "record_high_event_rally",
    "high_score_without_price_validation",
)

ROUND218_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "ipo_first_day_50_to_100pct_rally",
    "policy_or_merger_event_record_high",
    "preferred_bidder_rally_before_final_contract",
    "contract_announcement_event_rally",
    "ai_grid_theme_multiple_ahead_of_company_orders",
    "good_news_price_response_fade",
    "valuation_ahead_of_delivery_margin_and_fcf",
)

ROUND218_HARD_4C_GATES: tuple[str, ...] = (
    "contract_cancellation",
    "final_contract_failure",
    "epc_cost_overrun",
    "margin_collapse",
    "working_capital_deterioration",
    "customer_payment_delay",
    "legal_delay_or_court_block",
    "sanction_trade_restriction",
    "policy_budget_failure",
    "integration_cost_overrun",
    "supply_chain_blocked",
)

ROUND218_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_price",
    "target_price",
    "target_upside_pct",
    "reported_mfe_pct",
    "mfe_1d",
    "mae_1d",
    "event_mae_pct",
    "relative_outperformance_pp",
    "contract_value_usd_bn",
    "policy_contract_value",
    "ipo_first_day_return_pct",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round218ScoreAdjustment:
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
class Round218ShadowWeightRow:
    archetype: E2RArchetype
    contract_amount: int
    order_to_revenue: int
    delivery_schedule: int
    backlog_margin: int
    customer_quality: int
    capacity_bottleneck: int
    us_grid_exposure: int
    price_path_alignment: int
    event_penalty: int
    geopolitical_redteam: int
    stage4b_watch_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "contract_amount": _signed_int_text(self.contract_amount),
            "order_to_revenue": _signed_int_text(self.order_to_revenue),
            "delivery_schedule": _signed_int_text(self.delivery_schedule),
            "backlog_margin": _signed_int_text(self.backlog_margin),
            "customer_quality": _signed_int_text(self.customer_quality),
            "capacity_bottleneck": _signed_int_text(self.capacity_bottleneck),
            "us_grid_exposure": _signed_int_text(self.us_grid_exposure),
            "price_path_alignment": _signed_int_text(self.price_path_alignment),
            "event_penalty": _signed_int_text(self.event_penalty),
            "geopolitical_redteam": _signed_int_text(self.geopolitical_redteam),
            "4b_watch_sensitivity": _signed_int_text(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed_int_text(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round218CaseCandidate:
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
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    peak_price_anchor: float | None
    reported_mfe_pct: float | None
    mfe_1d: float | None
    mae_1d: float | None
    extra_price_metrics: Mapping[str, float | str | bool]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND218_LARGE_SECTOR

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND218_SCORE_ADJUSTMENTS: tuple[Round218ScoreAdjustment, ...] = (
    Round218ScoreAdjustment("confirmed_contract_amount", 5, "raise", "계약금액이 고객·납기와 같이 확인되면 Stage 2 품질이 올라간다."),
    Round218ScoreAdjustment("order_to_revenue_conversion", 5, "raise", "수주가 납품·매출·OP/EPS로 내려오는 경로를 보상한다."),
    Round218ScoreAdjustment("delivery_schedule", 4, "raise", "납기와 공정이 있어야 backlog가 실제 실적으로 변한다."),
    Round218ScoreAdjustment("backlog_margin_visibility", 5, "raise", "수주잔고가 마진과 FCF로 이어질 때만 Green에 가까워진다."),
    Round218ScoreAdjustment("customer_quality", 4, "raise", "전력망·정부·Aramco처럼 고객 질이 높으면 visibility가 좋아진다."),
    Round218ScoreAdjustment("capacity_bottleneck", 4, "raise", "변압기 lead time, CAPA 병목, 선박 슬롯 부족은 구조적 신호다."),
    Round218ScoreAdjustment("us_grid_exposure", 4, "raise", "미국 grid/data-center exposure는 R1 구조 신호지만 회사별 주문 확인이 필요하다."),
    Round218ScoreAdjustment("price_path_alignment", 5, "raise", "증거 이후 가격경로가 따라오면 score-price alignment를 인정한다."),
    Round218ScoreAdjustment("contract_headline_without_margin", -5, "lower", "계약 headline만 있고 마진·현금회수가 없으면 Green 금지다."),
    Round218ScoreAdjustment("policy_or_mou_without_order", -5, "lower", "정책·MOU·합병 이벤트는 funded order 전 event premium이다."),
    Round218ScoreAdjustment("ipo_first_day_rally", -5, "lower", "IPO 첫날 급등은 구조적 Stage 3가 아니라 4B-watch다."),
    Round218ScoreAdjustment("record_high_on_policy_event", -4, "lower", "정책/합병 신고가는 가격이 증거보다 앞섰을 수 있다."),
    Round218ScoreAdjustment("geopolitical_sanction_unpriced", -4, "lower", "제재·지정학 리스크는 4C-watch로 별도 분리한다."),
    Round218ScoreAdjustment("epc_backlog_without_cashflow", -4, "lower", "EPC 대형수주는 원가율·cash collection 전 Green이 아니다."),
)


ROUND218_SHADOW_WEIGHT_ROWS: tuple[Round218ShadowWeightRow, ...] = (
    Round218ShadowWeightRow(E2RArchetype.POWER_EQUIPMENT_EXPORT_US_GRID, 3, 4, 3, 5, 4, 4, 5, 3, -2, 1, 4, 3, "LS Electric has strong U.S. grid evidence but event price failed."),
    Round218ShadowWeightRow(E2RArchetype.TRANSFORMER_CAPACITY_BOTTLENECK, 3, 3, 4, 5, 4, 5, 5, 2, -2, 1, 5, 3, "K-transformer basket has strong bottleneck evidence but needs company-level orders and margins."),
    Round218ShadowWeightRow(E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG, 5, 4, 4, 5, 5, 0, 0, 4, -3, 2, 4, 4, "Samsung E&A confirms Stage 2 contract; Stage 3 requires margins and cash collection."),
    Round218ShadowWeightRow(E2RArchetype.NUCLEAR_POLICY_TO_EQUIPMENT_BACKLOG, 4, 4, 5, 5, 5, 2, 0, 4, -4, 2, 5, 4, "Doosan preferred bidder/final contract is Stage 2; equipment backlog needed."),
    Round218ShadowWeightRow(E2RArchetype.SHIPBUILDING_US_POLICY_MASGA, 4, 3, 4, 5, 4, 2, 0, 3, -5, 3, 5, 4, "HD Hyundai/Mipo merger is Stage 2 and 4B-watch until funded orders and margins confirm."),
    Round218ShadowWeightRow(E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION, 0, 0, 0, 0, 0, 0, 0, 2, 0, 5, 3, 5, "Hanwha Ocean China sanctions require 4C-watch."),
    Round218ShadowWeightRow(E2RArchetype.SHIP_MRO_RECURRING_PLATFORM, 3, 3, 3, 4, 3, 0, 0, 1, -5, 1, 5, 3, "HD Hyundai Marine IPO rally is 4B/event premium before recurring MRO proof."),
    Round218ShadowWeightRow(E2RArchetype.IPO_EVENT_PREMIUM, 0, 0, 0, 0, 0, 0, 0, 0, -5, 0, 5, 2, "First-day IPO rally blocks Stage 3 until operating evidence appears."),
)


ROUND218_CASE_CANDIDATES: tuple[Round218CaseCandidate, ...] = (
    Round218CaseCandidate(
        case_id="r1_loop9_ls_electric_us_grid_watch",
        symbol="010120",
        company_name="LS ELECTRIC",
        primary_archetype=E2RArchetype.POWER_EQUIPMENT_EXPORT_US_GRID,
        secondary_archetypes=(E2RArchetype.GRID_POWER_EQUIPMENT_AI_DATACENTER, E2RArchetype.EVIDENCE_GOOD_BUT_PRICE_FAILED),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2024, 7, 1),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="us_grid_growth_evidence_good_but_price_failed_until_orders_margin_fcf_confirm",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("us_business_growth_opportunity", "target_price_raise_150k_to_280k", "us_revenue_share_expected_20pct", "stage2_price_208500"),
        red_flag_fields=("event_price_down_5_4pct", "company_level_order_margin_fcf_unconfirmed", "price_path_not_yet_confirmed"),
        price_data_source="MarketWatch reported price and target anchors",
        reported_price_anchor="208,500 KRW event price; target 280,000 KRW",
        reported_return_anchor="event price -5.4%; target upside +34.3%; target raise +86.7%",
        stage2_price_anchor=208500.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        reported_mfe_pct=None,
        mfe_1d=None,
        mae_1d=-5.4,
        extra_price_metrics={
            "target_price": 280000.0,
            "target_upside_pct": 34.3,
            "target_raise_pct": 86.7,
            "us_revenue_share_2024_expected_pct": 20.0,
            "us_revenue_share_2022_max_pct": 5.0,
            "minimum_relative_mix_increase_pct": 300.0,
        },
        score_price_alignment="evidence_good_but_price_failed",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="미국 grid/data-center 성장 근거는 좋지만 보도 시점 가격이 빠졌다. Green은 회사별 주문·마진·FCF와 이후 가격경로 확인 뒤다.",
    ),
    Round218CaseCandidate(
        case_id="r1_loop9_k_transformer_bottleneck_basket",
        symbol="267260/298040",
        company_name="HD현대일렉트릭/효성중공업",
        primary_archetype=E2RArchetype.TRANSFORMER_CAPACITY_BOTTLENECK,
        secondary_archetypes=(E2RArchetype.GRID_POWER_EQUIPMENT_AI_DATACENTER, E2RArchetype.GRID_TRANSFORMER_SHORTAGE_KOREA),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2026, 5, 11),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="sector_bottleneck_stage2_until_company_orders_margin_fcf_and_ohlc_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("gsu_transformer_demand_growth_274pct", "substation_transformer_demand_growth_116pct", "transformer_price_increase_80pct_5y", "large_transformer_lead_time_4y", "hyosung_opm_6pct_2024"),
        red_flag_fields=("sector_data_without_company_order", "company_ohlc_unavailable", "margin_fcf_conversion_unconfirmed", "transformer_cycle_peakout_watch"),
        price_data_source="Reuters sector evidence and public company profile anchors",
        reported_price_anchor="No company OHLC anchor in round note",
        reported_return_anchor="GSU demand +274%; substation demand +116%; transformer prices +80%; lead time up to 4 years",
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        reported_mfe_pct=None,
        mfe_1d=None,
        mae_1d=None,
        extra_price_metrics={
            "gsu_transformer_demand_growth_pct": 274.0,
            "substation_transformer_demand_growth_pct": 116.0,
            "transformer_price_increase_5y_pct": 80.0,
            "large_transformer_lead_time_years": 4.0,
            "hyosung_revenue_2024_krw_trn": 4.3,
            "hyosung_op_income_2024_krw_bn": 257.8,
            "hyosung_op_margin_pct": 6.0,
        },
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="미국 transformer shortage는 강한 Stage 2 sector evidence다. 다만 회사별 order/margin/FCF와 가격경로 전 Stage 3는 보류한다.",
    ),
    Round218CaseCandidate(
        case_id="r1_loop9_samsung_ea_fadhili_epc",
        symbol="028050",
        company_name="삼성E&A",
        primary_archetype=E2RArchetype.OVERSEAS_EPC_CONTRACT_BACKLOG,
        secondary_archetypes=(E2RArchetype.EPC_LOW_MARGIN_ORDER_OVERLAY, E2RArchetype.CONTRACT_HEADLINE_NOT_STAGE3),
        case_type="success_candidate",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 3),
        stage3_date=None,
        stage4b_date=date(2024, 4, 3),
        stage4c_date=None,
        stage3_decision="large_epc_contract_stage2_until_margin_progress_revenue_and_cash_collection_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("fadhili_gas_expansion", "saudi_aramco_customer", "samsung_ea_6bn_usd_contract", "aramco_total_project_7_7bn_usd", "event_peak_price_26750", "relative_outperformance_9_9pp"),
        red_flag_fields=("epc_margin_unconfirmed", "cash_collection_unconfirmed", "cost_overrun_watch", "contract_headline_without_margin"),
        price_data_source="WSJ/Reuters reported contract and price anchors",
        reported_price_anchor="26,750 KRW event peak",
        reported_return_anchor="+8.5% event move; KOSPI relative outperformance +9.9pp; KB target 35,000 KRW",
        stage2_price_anchor=26750.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=26750.0,
        stage4c_price_anchor=None,
        peak_price_anchor=26750.0,
        reported_mfe_pct=8.5,
        mfe_1d=8.5,
        mae_1d=None,
        extra_price_metrics={
            "implied_pre_event_reference_price": 24654.0,
            "kospi_same_context_return_pct": -1.4,
            "relative_outperformance_pp": 9.9,
            "contract_value_usd_bn": 6.0,
            "aramco_total_project_usd_bn": 7.7,
            "samsung_share_of_project_pct": 77.9,
            "kb_target_price": 35000.0,
            "target_upside_from_event_peak_pct": 30.8,
        },
        score_price_alignment="aligned",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="Fadhili $6B 계약은 좋은 Stage 2 사례다. Stage 3는 EPC margin, progress revenue, cash collection 확인 뒤다.",
    ),
    Round218CaseCandidate(
        case_id="r1_loop9_doosan_czech_nuclear_policy_to_contract",
        symbol="034020",
        company_name="두산에너빌리티",
        primary_archetype=E2RArchetype.NUCLEAR_POLICY_TO_EQUIPMENT_BACKLOG,
        secondary_archetypes=(E2RArchetype.NUCLEAR_POLICY_TO_CONTRACT, E2RArchetype.NUCLEAR_SMR_GRID_POLICY),
        case_type="success_candidate",
        stage1_date=date(2024, 7, 17),
        stage2_date=date(2025, 6, 4),
        stage3_date=None,
        stage4b_date=date(2024, 7, 17),
        stage4c_date=date(2025, 5, 6),
        stage3_decision="policy_to_contract_partly_verified_but_equipment_backlog_margin_eps_revision_needed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("czech_nuclear_preferred_bidder", "court_clearance_then_contract_signed", "407b_koruna_contract", "18_7bn_usd_contract", "reported_3m_mfe_48pct"),
        red_flag_fields=("preferred_bidder_rally_before_final_contract", "legal_delay_or_court_block", "equipment_backlog_unconfirmed", "margin_eps_revision_unconfirmed"),
        price_data_source="Reuters/AP reported policy, contract, and return anchors",
        reported_price_anchor="No full OHLC; reported 3M +48% before final contract",
        reported_return_anchor="reported 3M +48%; signed 407B koruna / $18.7B contract",
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        reported_mfe_pct=48.0,
        mfe_1d=None,
        mae_1d=None,
        extra_price_metrics={
            "signed_contract_value_koruna_bn": 407.0,
            "signed_contract_value_usd_bn": 18.7,
            "reactor_count": 2.0,
            "contract_value_per_reactor_koruna_bn": 203.5,
            "signed_contract_per_reactor_vs_estimate_pct": 1.75,
        },
        score_price_alignment="unknown",
        rerating_result="policy_event_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_return_anchor_not_full_ohlc",
        notes="체코 원전은 preferred bidder에서 final contract로 일부 검증됐다. 두산 장비 수주잔고·마진·EPS revision 전 Green은 아니다.",
    ),
    Round218CaseCandidate(
        case_id="r1_loop9_hd_hyundai_heavy_mipo_masga_event",
        symbol="329180/010620",
        company_name="HD현대중공업/HD현대미포",
        primary_archetype=E2RArchetype.SHIPBUILDING_US_POLICY_MASGA,
        secondary_archetypes=(E2RArchetype.SHIPBUILDING_OFFSHORE_BACKLOG, E2RArchetype.EVENT_PREMIUM),
        case_type="4b_watch",
        stage1_date=date(2025, 8, 1),
        stage2_date=date(2025, 8, 27),
        stage3_date=None,
        stage4b_date=date(2025, 8, 27),
        stage4c_date=None,
        stage3_decision="masga_merger_policy_event_is_stage2_4b_watch_until_funded_orders_margin_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("masga_us_shipbuilding_policy", "merger_event", "hd_hyundai_heavy_11_3pct", "hd_hyundai_mipo_14_6pct", "record_high_status"),
        red_flag_fields=("policy_or_merger_event_record_high", "funded_us_order_unconfirmed", "margin_unconfirmed", "record_high_event_rally"),
        price_data_source="Reuters reported event return anchors",
        reported_price_anchor="event return anchors only",
        reported_return_anchor="HD Hyundai Heavy +11.3%; HD Hyundai Mipo +14.6%; record highs",
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        reported_mfe_pct=14.6,
        mfe_1d=14.6,
        mae_1d=None,
        extra_price_metrics={
            "hd_hyundai_heavy_mfe_1d_pct": 11.3,
            "hd_hyundai_mipo_mfe_1d_pct": 14.6,
            "record_high_status": True,
            "share_exchange_ratio_mipo_per_heavy": 1.04059146,
        },
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="MASGA·합병 이벤트는 Stage 2 + 4B-watch다. funded U.S. order와 margin 전 Stage 3는 금지다.",
    ),
    Round218CaseCandidate(
        case_id="r1_loop9_hanwha_ocean_china_sanction_watch",
        symbol="042660",
        company_name="한화오션",
        primary_archetype=E2RArchetype.GEOPOLITICAL_SHIPBUILDING_SANCTION,
        secondary_archetypes=(E2RArchetype.SHIP_MRO_RECURRING_PLATFORM, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="failed_rerating",
        stage1_date=date(2024, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 10, 14),
        stage3_decision="us_shipbuilding_policy_exposure_gets_4c_watch_when_geopolitical_sanctions_arrive",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("philly_shipyard_acquisition_100m_usd", "us_shipbuilding_investment_5bn_usd", "sanctioned_entities_5", "hanwha_ocean_close_minus_5_8pct"),
        red_flag_fields=("geopolitical_sanction", "sanction_trade_restriction_watch", "revenue_disruption_unconfirmed", "hard_4c_not_confirmed"),
        price_data_source="Reuters/AP reported sanction and price anchors",
        reported_price_anchor="Hanwha Ocean close -5.8%; intraday over -8%; HD Hyundai Heavy -4.1%",
        reported_return_anchor="China sanctions five U.S.-linked subsidiaries; Philly Shipyard $100M; U.S. investment $5B",
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        reported_mfe_pct=None,
        mfe_1d=None,
        mae_1d=-5.8,
        extra_price_metrics={
            "hanwha_ocean_close_mae_pct": -5.8,
            "hanwha_ocean_intraday_mae_pct": -8.0,
            "hd_hyundai_heavy_mae_pct": -4.1,
            "philly_shipyard_acquisition_usd_mn": 100.0,
            "announced_us_investment_usd_bn": 5.0,
            "investment_vs_acquisition_multiple": 50.0,
            "sanctioned_entities": 5.0,
        },
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="한화오션은 hard 4C가 아니라 4C-watch다. 실제 매출·수주·공급 차질이 확인되면 hard 4C로 승격한다.",
    ),
    Round218CaseCandidate(
        case_id="r1_loop9_hd_hyundai_marine_solution_ipo_premium",
        symbol="443060",
        company_name="HD현대마린솔루션",
        primary_archetype=E2RArchetype.SHIP_MRO_RECURRING_PLATFORM,
        secondary_archetypes=(E2RArchetype.IPO_EVENT_PREMIUM, E2RArchetype.EVENT_PREMIUM, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="overheat",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 5, 8),
        stage3_date=None,
        stage4b_date=date(2024, 5, 8),
        stage4c_date=None,
        stage3_decision="ship_mro_structure_possible_but_ipo_first_day_rally_is_event_premium_not_stage3",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("ship_mro_after_sales_platform", "ipo_price_83400", "first_day_close_163900", "first_day_return_96_5pct", "revenue_growth_2023_7_2pct", "earnings_growth_2023_44pct"),
        red_flag_fields=("ipo_first_day_rally", "price_moved_before_recurring_mro_fcf", "post_ipo_multiple_compression_watch", "lockup_or_sell_down_watch"),
        price_data_source="WSJ/Reuters Breakingviews IPO anchors",
        reported_price_anchor="IPO price 83,400 KRW to first-day close 163,900 KRW",
        reported_return_anchor="+96.5% first-day close; market cap +98.5%",
        stage2_price_anchor=83400.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=163900.0,
        stage4c_price_anchor=None,
        peak_price_anchor=163900.0,
        reported_mfe_pct=96.5,
        mfe_1d=96.5,
        mae_1d=None,
        extra_price_metrics={
            "ipo_price": 83400.0,
            "first_day_close": 163900.0,
            "ipo_first_day_return_pct": 96.5,
            "ipo_market_cap_usd_bn": 2.70,
            "first_day_market_cap_usd_bn": 5.36,
            "market_cap_mfe_1d_pct": 98.5,
            "ipo_proceeds_krw_bn": 742.26,
            "shares_outstanding_mn": 44.5,
            "revenue_2023_krw_trn": 1.43,
            "revenue_growth_2023_pct": 7.2,
            "earnings_2023_krw_bn": 151.1,
            "earnings_growth_2023_pct": 44.0,
        },
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="reported_price_anchor_not_stage3",
        notes="좋은 MRO 구조일 수 있지만 IPO 첫날 +96.5%는 Stage 3가 아니라 4B/event premium이다.",
    ),
)


def round218_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND218_CASE_CANDIDATES:
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
                "Round218 R1 Loop-9 industrial orders/infrastructure price validation case. "
                "Calibration-only; not candidate-generation input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "policy" in field or "ipo" in field or "growth" in field or "preferred" in field or "platform" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "revenue" in field or "earnings" in field or "opm" in field or "contract" in field or "price_208500" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "rally" in field
                or "record" in field
                or "premium" in field
                or "first_day" in field
                or "preferred_bidder" in field
                or "price_moved" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "sanction" in field
                or "legal" in field
                or "cost_overrun" in field
                or "margin_collapse" in field
                or "hard_4c" in field
            ),
            must_have_fields=ROUND218_GREEN_REQUIRED_FIELDS,
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
                "confirmed_contract_amount_delta": 5.0,
                "order_to_revenue_conversion_delta": 5.0,
                "delivery_schedule_delta": 4.0,
                "backlog_margin_visibility_delta": 5.0,
                "capacity_bottleneck_delta": 4.0,
                "us_grid_exposure_delta": 4.0,
                "price_path_alignment_delta": 5.0,
                "contract_headline_without_margin_delta": -5.0,
                "policy_or_mou_without_order_delta": -5.0,
                "ipo_first_day_rally_delta": -5.0,
                "geopolitical_sanction_unpriced_delta": -4.0,
                "epc_backlog_without_cashflow_delta": -4.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_margins_or_fcf",
                "do_not_treat_policy_mou_ipo_record_high_or_contract_headline_as_green",
                *ROUND218_GREEN_REQUIRED_FIELDS,
                *ROUND218_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_price=candidate.peak_price_anchor,
                peak_return_from_stage3=candidate.reported_mfe_pct,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.stage2_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.reported_mfe_pct is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage4b_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round218_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND218_CASE_CANDIDATES:
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
                "stage2_price": _float_text(candidate.stage2_price_anchor),
                "stage3_price": _float_text(candidate.stage3_price_anchor),
                "stage4b_price": _float_text(candidate.stage4b_price_anchor),
                "stage4c_price": _float_text(candidate.stage4c_price_anchor),
                "peak_price": _float_text(candidate.peak_price_anchor),
                "reported_mfe_pct": _float_text(candidate.reported_mfe_pct),
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mae_1d": _float_text(candidate.mae_1d),
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


def round218_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND218_SCORE_ADJUSTMENTS)


def round218_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND218_SHADOW_WEIGHT_ROWS)


def round218_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round218_price_validation": "true"} for field in ROUND218_PRICE_VALIDATION_FIELDS)


def round218_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round218_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND218_REQUIRED_TARGET_ALIASES.items()
    )


def round218_summary() -> dict[str, int | bool | str]:
    cases = ROUND218_CASE_CANDIDATES
    return {
        "source_round": ROUND218_SOURCE_ROUND_PATH,
        "large_sector": ROUND218_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "overheat_count": sum(1 for case in cases if case.case_type == "overheat"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "watch_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status in {"watch", "elevated"}),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "aligned_stage2_count": sum(1 for case in cases if case.score_price_alignment == "aligned" and case.stage3_date is None),
        "target_archetype_count": len(ROUND218_REQUIRED_TARGET_ALIASES),
        "shadow_weight_row_count": len(ROUND218_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
    }


def round218_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND218_SOURCE_ROUND_PATH,
        "large_sector": ROUND218_LARGE_SECTOR,
        "summary": round218_summary(),
        "target_aliases": dict(ROUND218_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND218_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND218_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND218_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND218_HARD_4C_GATES),
        "score_adjustments": list(round218_score_adjustment_rows()),
        "shadow_weights": list(round218_shadow_weight_rows()),
        "case_ids": [case.case_id for case in ROUND218_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round218_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_policy_mou_merger_ipo_or_contract_headline_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round218_summary_markdown() -> str:
    summary = round218_summary()
    lines = [
        "# Round 218 R1 Loop 9 Industrial Infra Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- 4B watch cases: {summary['stage4b_watch_count']}",
        f"- 4C watch cases: {summary['stage4c_watch_count']}",
        f"- overheat: {summary['overheat_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- evidence_good_but_price_failed: {summary['evidence_good_but_price_failed_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C-watch | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND218_CASE_CANDIDATES:
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
            "- LS Electric은 미국 grid evidence가 좋지만 보도 시점 가격이 빠져 `evidence_good_but_price_failed`다.",
            "- Transformer basket은 sector bottleneck은 강하지만 회사별 주문·마진·FCF 전 Stage 2다.",
            "- 삼성E&A와 두산에너빌리티는 큰 계약/정책-to-contract가 있으나 margin과 장비 backlog 전 Green은 보류한다.",
            "- HD현대중공업/미포와 HD현대마린솔루션은 event premium과 4B-watch를 분리한다.",
            "- 한화오션은 sanction event를 hard 4C가 아닌 4C-watch로 기록한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round218_green_gate_review_markdown() -> str:
    lines = [
        "# Round 218 R1 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND218_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND218_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND218_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `계약금액 + 납기 + 마진 + EPS revision`이 같이 있어야 Stage 3 후보가 된다.",
            "- `정책/MOU/합병 뉴스 + 신고가`는 funded order 전 4B-watch다.",
            "- `IPO 첫날 +96.5%`는 운영 증거가 아니라 event premium이다.",
            "- `중국 제재`는 실제 매출 차질 확인 전 4C-watch로 기록한다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round218_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 218 R1 4B / 4C Review",
        "",
        "## 4B Watch Triggers",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND218_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND218_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Case Review",
            "",
            "| case | 4B status | hard 4C | interpretation |",
            "|---|---|---|---|",
        ]
    )
    for case in ROUND218_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round218_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 218 R1 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND218_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND218_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round218_r1_loop9_reports(
    output_directory: str | Path = ROUND218_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND218_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND218_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)

    paths = {
        "cases": write_case_library(round218_case_records(), cases_path),
        "audit": _write_json(round218_audit_payload(), audit_path),
        "summary": output / "round218_r1_loop9_price_validation_summary.md",
        "case_matrix": output / "round218_r1_loop9_case_matrix.csv",
        "target_aliases": output / "round218_r1_loop9_target_aliases.csv",
        "score_adjustments": output / "round218_r1_loop9_score_adjustments.csv",
        "shadow_weights": output / "round218_r1_loop9_shadow_weights.csv",
        "price_validation_fields": output / "round218_r1_loop9_price_validation_fields.csv",
        "green_gate_review": output / "round218_r1_loop9_green_gate_review.md",
        "price_validation_plan": output / "round218_r1_loop9_price_validation_plan.md",
        "stage4b_4c_review": output / "round218_r1_loop9_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round218_summary_markdown(), encoding="utf-8")
    _write_csv(round218_case_rows(), paths["case_matrix"])
    _write_csv(round218_target_alias_rows(), paths["target_aliases"])
    _write_csv(round218_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round218_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round218_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round218_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round218_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round218_stage4b_4c_review_markdown(), encoding="utf-8")
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


def _signed_int_text(value: int) -> str:
    return f"+{value}" if value > 0 else str(value)
