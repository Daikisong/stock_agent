"""Round-219 R2 Loop-9 AI semiconductor price validation pack.

Round 219 is calibration/evaluation material only. It converts the analyst's
AI semiconductor price anchors into structured case records, shadow weights,
and Green/4B/4C guardrails.

Easy example: SK Hynix HBM4 evidence can be a true rerating case, but after a
large multi-bagger price path it is also 4B-watch. Samsung's OpenAI/Stargate
headline is useful Stage 2 evidence, but HBM volume shipment, customer margin,
and labor/production risks decide whether it can move beyond watch status.
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


ROUND219_SOURCE_ROUND_PATH = "docs/round/round_219.md"
ROUND219_LARGE_SECTOR = Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS
ROUND219_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round219_r2_loop9_ai_semiconductor_price_validation"
ROUND219_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop9_round219.jsonl"
ROUND219_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round219_r2_loop9_ai_semiconductor_price_validation_audit.json"

ROUND219_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "MEMORY_HBM_CAPACITY": E2RArchetype.MEMORY_HBM_CAPACITY.value,
    "MEMORY_HBM4_FIRST_MOVER": E2RArchetype.MEMORY_HBM4_FIRST_MOVER.value,
    "MEMORY_SUPERCYCLE_AI_CAPEX": E2RArchetype.MEMORY_SUPERCYCLE_AI_CAPEX.value,
    "HBM_CATCHUP_EXECUTION": E2RArchetype.HBM_CATCHUP_EXECUTION.value,
    "HBM_BONDER_EQUIPMENT_KOREA": E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA.value,
    "SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER": E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER.value,
    "AI_CHIP_FABRIC_INFRA": E2RArchetype.AI_CHIP_FABRIC_INFRA.value,
    "POLICY_FOUNDRY_EVENT": E2RArchetype.POLICY_FOUNDRY_EVENT.value,
    "OPENAI_STARGATE_AI_CAPEX_EVENT": E2RArchetype.OPENAI_STARGATE_AI_CAPEX_EVENT.value,
    "GEOPOLITICAL_EXPORT_CONTROL_OVERLAY": E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY.value,
    "LABOR_SUPPLY_CHAIN_4C_WATCH": E2RArchetype.LABOR_SUPPLY_CHAIN_4C_WATCH.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
}

ROUND219_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "company_level_customer_evidence",
    "product_specific_exposure",
    "order_shipment_contract_or_revenue_path_confirmed",
    "gross_margin_or_opm_improvement",
    "eps_fcf_revision_confirmed",
    "capacity_bottleneck_or_supply_allocation",
    "price_path_after_evidence",
    "export_control_china_fab_labor_accounting_trust_passed",
    "no_hard_redteam",
)

ROUND219_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ai_keyword_only",
    "server_theme_only",
    "unconfirmed_customer_media_report",
    "design_win_without_revenue",
    "policy_foundry_without_order",
    "openai_or_nvidia_headline_without_company_revenue",
    "customer_name_without_margin",
    "price_rally_before_confirmation",
    "labor_disruption_unpriced",
    "export_control_unpriced",
)

ROUND219_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "stage3_after_3x_or_more_return",
    "market_cap_milestone_headline",
    "openai_stargate_event_index_rally",
    "unconfirmed_customer_report_20pct_rally",
    "ai_capex_consensus_crowding",
    "record_high_good_news",
    "winner_already_rerated",
)

ROUND219_HARD_4C_GATES: tuple[str, ...] = (
    "hbm_qualification_failure",
    "order_pushout",
    "customer_capex_cut",
    "memory_price_decline",
    "hbm_supply_normalization",
    "china_fab_export_control_disruption",
    "equipment_authorization_loss",
    "labor_strike_or_production_halt",
    "accounting_or_disclosure_trust_break",
    "customer_concentration_failure",
)

ROUND219_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_price",
    "reported_mfe_pct",
    "reported_market_cap_mfe_minimum_pct",
    "reported_compounded_return_minimum_pct",
    "hbm4_event_mfe_intraday_pct",
    "relative_outperformance_pp",
    "mfe_1d",
    "mfe_1d_secondary",
    "mae_1d",
    "mae_1d_secondary",
    "contract_value_krw_bn",
    "project_size_krw_trn",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round219ScoreAdjustment:
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
class Round219ShadowWeightRow:
    archetype: E2RArchetype
    eps_revision: int
    capacity_bottleneck: int
    customer_visibility: int
    product_specificity: int
    price_path_alignment: int
    memory_price_upcycle: int
    order_to_revenue: int
    hbm_first_mover_or_execution: int
    event_penalty: int
    redteam_sensitivity: int
    stage4b_watch_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "eps_revision": _signed_int_text(self.eps_revision),
            "capacity_bottleneck": _signed_int_text(self.capacity_bottleneck),
            "customer_visibility": _signed_int_text(self.customer_visibility),
            "product_specificity": _signed_int_text(self.product_specificity),
            "price_path_alignment": _signed_int_text(self.price_path_alignment),
            "memory_price_upcycle": _signed_int_text(self.memory_price_upcycle),
            "order_to_revenue": _signed_int_text(self.order_to_revenue),
            "hbm_first_mover_or_execution": _signed_int_text(self.hbm_first_mover_or_execution),
            "event_penalty": _signed_int_text(self.event_penalty),
            "redteam_sensitivity": _signed_int_text(self.redteam_sensitivity),
            "4b_watch_sensitivity": _signed_int_text(self.stage4b_watch_sensitivity),
            "hard4c_sensitivity": _signed_int_text(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round219CaseCandidate:
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
    reported_market_cap_mfe_minimum_pct: float | None
    reported_compounded_return_minimum_pct: float | None
    mfe_1d: float | None
    mfe_1d_secondary: float | None
    mae_1d: float | None
    mae_1d_secondary: float | None
    extra_price_metrics: Mapping[str, float | str | bool]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND219_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND219_SCORE_ADJUSTMENTS: tuple[Round219ScoreAdjustment, ...] = (
    Round219ScoreAdjustment("eps_revision", 5, "raise", "HBM 리더는 OP/EPS revision이 가격경로와 같이 움직일 때만 강하게 본다."),
    Round219ScoreAdjustment("capacity_bottleneck", 5, "raise", "HBM 세대 전환과 CAPA 배분은 구조적 visibility의 핵심이다."),
    Round219ScoreAdjustment("hbm4_first_mover", 5, "raise", "HBM4 first mover와 고객 인증은 단순 메모리 사이클보다 높은 신뢰도를 준다."),
    Round219ScoreAdjustment("customer_visibility", 5, "raise", "Nvidia/OpenAI급 고객 수요가 회사 매출 경로로 연결될 때 보상한다."),
    Round219ScoreAdjustment("memory_price_upcycle", 4, "raise", "메모리 가격 상승은 EPS/FCF revision과 같이 있을 때 보상한다."),
    Round219ScoreAdjustment("confirmed_customer_order", 5, "raise", "확인된 고객 주문은 미확정 media rumor와 분리한다."),
    Round219ScoreAdjustment("order_to_revenue_conversion", 4, "raise", "design win이나 장비 수주가 매출·마진으로 내려오는 경로를 보상한다."),
    Round219ScoreAdjustment("price_path_alignment", 5, "raise", "증거 이후 가격경로가 따라오면 score-price alignment를 인정한다."),
    Round219ScoreAdjustment("unconfirmed_media_report", -5, "lower", "미확정 고객 보도만으로 오른 구간은 4B-watch다."),
    Round219ScoreAdjustment("design_win_without_revenue", -5, "lower", "design win은 Stage 2 근거지만 양산·매출·마진 전 Green은 아니다."),
    Round219ScoreAdjustment("policy_foundry_without_order", -5, "lower", "정책 foundry 협의는 회사 단위 order/utilization 전 event premium이다."),
    Round219ScoreAdjustment("openai_or_nvidia_headline_without_company_revenue", -4, "lower", "OpenAI/Nvidia headline만으로 후발주 Green을 만들면 안 된다."),
    Round219ScoreAdjustment("customer_name_without_margin", -3, "lower", "고객 이름만 있고 margin이 없으면 Green 신뢰도를 막는다."),
    Round219ScoreAdjustment("price_rally_before_confirmation", -5, "lower", "확인 전 가격 급등은 price-before-evidence로 본다."),
    Round219ScoreAdjustment("labor_or_export_control_unpriced", -5, "lower", "노동/수출통제 리스크가 실적 차질로 이어질 수 있으면 4C-watch다."),
)


ROUND219_SHADOW_WEIGHT_ROWS: tuple[Round219ShadowWeightRow, ...] = (
    Round219ShadowWeightRow(E2RArchetype.MEMORY_HBM4_FIRST_MOVER, 5, 5, 5, 4, 5, 4, 4, 5, -1, 3, 5, 4, "SK Hynix confirms large MFE and 4B-watch after HBM4 and market-cap milestone."),
    Round219ShadowWeightRow(E2RArchetype.HBM_CATCHUP_EXECUTION, 4, 3, 4, 3, 4, 3, 4, 3, -2, 5, 4, 4, "Samsung is Stage 2 until volume HBM sales and margins; labor risk creates 4C-watch."),
    Round219ShadowWeightRow(E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA, 3, 0, 5, 5, 5, 4, 4, 4, -3, 2, 5, 3, "Hanmi confirmed order is good; unconfirmed customer rumor is 4B/event risk."),
    Round219ShadowWeightRow(E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER, 2, 1, 4, 5, 2, 0, 5, 2, -4, 2, 4, 4, "Gaonchips design win is Stage 2 until tape-out, revenue, and margin are visible."),
    Round219ShadowWeightRow(E2RArchetype.POLICY_FOUNDRY_EVENT, 1, 1, 2, 3, 1, 0, 3, 1, -5, 3, 4, 4, "DB HiTek foundry policy consultation is not company revenue evidence."),
    Round219ShadowWeightRow(E2RArchetype.OPENAI_STARGATE_AI_CAPEX_EVENT, 3, 2, 5, 3, 3, 2, 2, 4, -4, 2, 5, 3, "OpenAI demand validates leaders but causes 4B/event premium for laggards."),
    Round219ShadowWeightRow(E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, 0, 0, 0, 0, 2, 0, 0, 0, 0, 5, 3, 5, "China fab authorization loss is 4C-watch until production/revenue disruption is confirmed."),
    Round219ShadowWeightRow(E2RArchetype.LABOR_SUPPLY_CHAIN_4C_WATCH, 0, 0, 0, 0, 1, 0, 0, 0, -1, 5, 3, 5, "Samsung labor disruption is a RedTeam overlay, not positive E2R evidence."),
)


ROUND219_CASE_CANDIDATES: tuple[Round219CaseCandidate, ...] = (
    Round219CaseCandidate(
        case_id="r2_loop9_sk_hynix_hbm4_stage3_4b",
        symbol="000660",
        company_name="SK하이닉스",
        primary_archetype=E2RArchetype.MEMORY_HBM4_FIRST_MOVER,
        secondary_archetypes=(
            E2RArchetype.MEMORY_HBM_CAPACITY,
            E2RArchetype.MEMORY_SUPERCYCLE_AI_CAPEX,
            E2RArchetype.CROWDED_RERATING_4B_WATCH,
        ),
        case_type="structural_success",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 6, 25),
        stage3_date=date(2024, 6, 25),
        stage4b_date=date(2026, 5, 4),
        stage4c_date=None,
        stage3_decision="hbm_dominance_hbm4_first_mover_eps_revision_and_memory_price_upcycle_aligned_with_large_mfe",
        stage4b_status="elevated",
        hard_4c_confirmed=False,
        evidence_fields=(
            "hbm_dominance",
            "nomura_2024_op_30tn_2025_op_53tn_revision",
            "stage3_price_222000",
            "hbm4_internal_certification",
            "hbm4_event_intraday_plus_7_3pct",
            "record_close_1447000",
            "market_cap_near_942bn_usd",
        ),
        red_flag_fields=("market_cap_milestone", "ai_capex_consensus_crowding", "customer_price_resistance_watch", "hbm_supply_normalization_watch"),
        price_data_source="MarketWatch/Reuters reported price and return anchors",
        reported_price_anchor="222,000 KRW Stage 3 anchor; 1,447,000 KRW 2026-05-04 record close",
        reported_return_anchor="+551.8% from Stage 3 anchor to record close; 2025 +274%; 2026 >+200%; market cap <$100B to about $942B",
        stage2_price_anchor=222000.0,
        stage3_price_anchor=222000.0,
        stage4b_price_anchor=1447000.0,
        stage4c_price_anchor=None,
        peak_price_anchor=1447000.0,
        reported_mfe_pct=551.8,
        reported_market_cap_mfe_minimum_pct=842.0,
        reported_compounded_return_minimum_pct=1022.0,
        mfe_1d=7.3,
        mfe_1d_secondary=12.52,
        mae_1d=None,
        mae_1d_secondary=None,
        extra_price_metrics={
            "hbm4_event_mfe_intraday_pct": 7.3,
            "hbm4_relative_outperformance_pp": 6.1,
            "record_close_2026_05_04": 1447000.0,
            "reported_return_2025_pct": 274.0,
            "reported_return_2026_ytd_pct_minimum": 200.0,
            "market_cap_usd_bn": 942.0,
        },
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="green_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="HBM dominance, HBM4 first mover and EPS revision produced large MFE; now it is 4B-watch/elevated, not a fresh Green.",
    ),
    Round219CaseCandidate(
        case_id="r2_loop9_samsung_hbm_catchup_labor_watch",
        symbol="005930",
        company_name="삼성전자",
        primary_archetype=E2RArchetype.HBM_CATCHUP_EXECUTION,
        secondary_archetypes=(E2RArchetype.LABOR_SUPPLY_CHAIN_4C_WATCH, E2RArchetype.MEMORY_HBM_CAPACITY),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 10, 2),
        stage3_date=None,
        stage4b_date=date(2026, 5, 6),
        stage4c_date=date(2026, 5, 15),
        stage3_decision="hbm_catchup_is_stage2_until_volume_hbm_sales_customer_margin_and_labor_production_risk_clear",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=(
            "openai_stargate_partnership",
            "openai_event_return_plus_4_7pct",
            "q3_2025_op_12_2tn",
            "q3_2025_op_growth_32_5pct",
            "q3_2025_revenue_86tn",
            "semiconductor_division_op_7tn",
            "hbm3e_mass_production_hbm4_sample_shipment",
        ),
        red_flag_fields=("hbm_volume_margin_unconfirmed", "labor_strike_risk", "foundry_logic_losses", "production_disruption_watch", "jpmorgan_op_loss_estimate_21_31tn"),
        price_data_source="Reuters/AP reported event anchors",
        reported_price_anchor="OpenAI event +4.7%; 2026-05-06 AI rally +14.4%; strike event -9.3%",
        reported_return_anchor="OpenAI +4.7%; Q3 OP 12.2T KRW; AI rally +14.4% vs KOSPI +6.45%; strike event -9.3%",
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        reported_mfe_pct=14.4,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=4.7,
        mfe_1d_secondary=14.4,
        mae_1d=-9.3,
        mae_1d_secondary=None,
        extra_price_metrics={
            "q3_2025_op_krw_trn": 12.2,
            "q3_2025_op_growth_pct": 32.5,
            "q3_2025_revenue_krw_trn": 86.0,
            "semiconductor_division_op_krw_trn": 7.0,
            "ai_rally_relative_outperformance_pp": 7.95,
            "sales_opportunity_loss_krw_trn": 4.5,
            "jpmorgan_op_loss_estimate_krw_trn": "21-31",
        },
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Samsung has AI memory recovery and OpenAI demand validation, but HBM volume/margin proof is still needed and labor risk is 4C-watch.",
    ),
    Round219CaseCandidate(
        case_id="r2_loop9_hanmi_hbm_bonder_confirmed_vs_rumor",
        symbol="042700",
        company_name="한미반도체",
        primary_archetype=E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA,
        secondary_archetypes=(E2RArchetype.MEMORY_HBM4_FIRST_MOVER, E2RArchetype.CROWDED_RERATING_4B_WATCH, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="success_candidate",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 3, 26),
        stage3_date=None,
        stage4b_date=date(2024, 3, 28),
        stage4c_date=None,
        stage3_decision="confirmed_sk_hynix_hbm_bonder_order_is_good_but_micron_unconfirmed_report_is_4b_watch",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("sk_hynix_hbm_bonder_contract_21_48bn", "recent_deals_total_200bn", "tsv_tc_bonder", "hbm_packaging_bottleneck"),
        red_flag_fields=("unconfirmed_micron_media_report", "customer_diversification_rumor", "price_rally_before_confirmation", "margin_eps_revision_needed"),
        price_data_source="WSJ reported price and contract anchors",
        reported_price_anchor="139,100 KRW intraday after unconfirmed Micron report; implied pre-event about 114,016 KRW",
        reported_return_anchor="+22% on unconfirmed Micron report; KOSPI -0.3%; relative +22.3pp",
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=139100.0,
        stage4c_price_anchor=None,
        peak_price_anchor=139100.0,
        reported_mfe_pct=22.0,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=22.0,
        mfe_1d_secondary=None,
        mae_1d=None,
        mae_1d_secondary=None,
        extra_price_metrics={
            "confirmed_sk_hynix_contract_krw_bn": 21.48,
            "recent_deals_total_krw_bn": 200.0,
            "implied_pre_4b_reference_price": 114016.0,
            "kospi_same_context_pct": -0.3,
            "relative_outperformance_pp": 22.3,
        },
        score_price_alignment="aligned",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Confirmed SK Hynix HBM equipment order is Stage 2/3 candidate evidence, but the Micron rumor rally is 4B-watch.",
    ),
    Round219CaseCandidate(
        case_id="r2_loop9_gaonchips_pfn_design_win",
        symbol="399720",
        company_name="가온칩스",
        primary_archetype=E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER,
        secondary_archetypes=(E2RArchetype.AI_CHIP_FABRIC_INFRA, E2RArchetype.DISCLOSURE_CONFIDENCE_CAP),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 7, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="design_win_is_stage2_until_tapeout_mass_production_revenue_and_margin_are_confirmed",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("preferred_networks_ai_chip_design_win", "samsung_2nm_gaa", "advanced_packaging", "generative_ai_llm_hpc_hardware"),
        red_flag_fields=("design_win_without_revenue", "order_size_not_disclosed", "tapeout_needed", "mass_production_needed", "gross_margin_needed"),
        price_data_source="Reuters evidence source only",
        reported_price_anchor="no reported price anchor",
        reported_return_anchor="price data unavailable after deep search",
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        reported_mfe_pct=None,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=None,
        mfe_1d_secondary=None,
        mae_1d=None,
        mae_1d_secondary=None,
        extra_price_metrics={"order_size": "not_disclosed", "technology": "Samsung 2nm GAA + advanced packaging", "customer": "Preferred Networks"},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Design win is Stage 2; tape-out, mass production, revenue and margin are required for Stage 3.",
    ),
    Round219CaseCandidate(
        case_id="r2_loop9_db_hitek_policy_foundry",
        symbol="000990",
        company_name="DB하이텍",
        primary_archetype=E2RArchetype.POLICY_FOUNDRY_EVENT,
        secondary_archetypes=(E2RArchetype.AI_CHIP_FABRIC_INFRA, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="event_premium",
        stage1_date=date(2025, 12, 10),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="public_private_foundry_policy_is_attention_only_until_company_order_utilization_margin_and_eps_revision",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("public_private_foundry_4_5tn_krw", "40nm_12inch_foundry_review", "defense_semiconductor_localization", "government_consultation_target"),
        red_flag_fields=("policy_foundry_without_order", "company_order_missing", "utilization_unknown", "gross_margin_unknown", "eps_revision_missing"),
        price_data_source="Reuters policy evidence source",
        reported_price_anchor="no reported price anchor",
        reported_return_anchor="price data unavailable after deep search",
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        reported_mfe_pct=None,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=None,
        mfe_1d_secondary=None,
        mae_1d=None,
        mae_1d_secondary=None,
        extra_price_metrics={
            "foundry_project_size_krw_trn": 4.5,
            "foundry_project_size_usd_bn": 3.06,
            "process_node_nm": 40.0,
            "wafer_size_inch": 12.0,
            "defense_semiconductor_import_dependency_pct": 99.0,
            "company_status": "consultation_target_not_confirmed_order",
        },
        score_price_alignment="unknown",
        rerating_result="policy_event_rerating",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Government foundry consultation is Stage 1/2 attention, not company-level Green evidence.",
    ),
    Round219CaseCandidate(
        case_id="r2_loop9_openai_stargate_memory_4b",
        symbol="000660/005930",
        company_name="SK하이닉스/삼성전자",
        primary_archetype=E2RArchetype.OPENAI_STARGATE_AI_CAPEX_EVENT,
        secondary_archetypes=(E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.MEMORY_SUPERCYCLE_AI_CAPEX, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="4b_watch",
        stage1_date=date(2025, 10, 1),
        stage2_date=date(2025, 10, 2),
        stage3_date=None,
        stage4b_date=date(2025, 10, 2),
        stage4c_date=None,
        stage3_decision="openai_stargate_validates_ai_memory_demand_but_is_4b_watch_after_large_hbm_rerating",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("openai_stargate_partnership", "sk_hynix_event_plus_12pct", "samsung_event_plus_4_7pct", "combined_market_cap_added_37bn_usd", "expected_dram_wafers_900k_per_month"),
        red_flag_fields=("openai_or_nvidia_headline_without_company_revenue", "ai_capex_consensus_crowding", "post_rerating_winner_4b_watch", "laggard_green_forbidden"),
        price_data_source="Reuters/Tom's Hardware reported anchors",
        reported_price_anchor="SK Hynix +12%; Samsung +4.7%; combined market cap +$37B",
        reported_return_anchor="OpenAI/Stargate event: SK Hynix +12%, Samsung +4.7%, KOSPI >+3%, DRAM wafer demand up to 900k/month",
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        reported_mfe_pct=12.0,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=12.0,
        mfe_1d_secondary=4.7,
        mae_1d=None,
        mae_1d_secondary=None,
        extra_price_metrics={
            "combined_market_cap_added_usd_bn": 37.0,
            "kospi_event_return_pct_minimum": 3.0,
            "openai_expected_dram_wafers_monthly": 900000.0,
            "share_of_global_dram_output_pct": 40.0,
            "implied_global_dram_output_wafers_monthly": 2250000.0,
            "stargate_project_scale_usd_bn": 500.0,
        },
        score_price_alignment="aligned",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Demand validation for leaders, but 4B-watch after large rerating; laggard Green is forbidden without company revenue and margin.",
    ),
    Round219CaseCandidate(
        case_id="r2_loop9_export_control_china_fab_watch",
        symbol="005930/000660/067310/042700",
        company_name="Samsung/SK Hynix/Hana Micron/Hanmi",
        primary_archetype=E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY,
        secondary_archetypes=(E2RArchetype.LABOR_SUPPLY_CHAIN_4C_WATCH, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="failed_rerating",
        stage1_date=date(2025, 9, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 1),
        stage3_decision="china_fab_export_control_shock_is_4c_watch_until_production_revenue_or_customer_disruption_is_confirmed",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("us_china_equipment_authorization_revocation", "samsung_mae_1d_minus_2_3", "sk_hynix_mae_1d_minus_4_4", "hana_micron_mae_1d_minus_1_7", "hanmi_mae_1d_minus_4_4"),
        red_flag_fields=("china_fab_export_control_disruption_watch", "equipment_authorization_loss_watch", "production_revenue_disruption_needs_confirmation", "hard_4c_not_confirmed"),
        price_data_source="Reuters reported event returns",
        reported_price_anchor="Samsung -2.3%; SK Hynix -4.4%; Hana Micron -1.7%; Hanmi -4.4%",
        reported_return_anchor="export-control shock one-day reported returns; KOSPI -0.7%",
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        reported_mfe_pct=None,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=None,
        mfe_1d_secondary=None,
        mae_1d=-4.4,
        mae_1d_secondary=-1.7,
        extra_price_metrics={
            "samsung_mae_1d_pct": -2.3,
            "sk_hynix_mae_1d_pct": -4.4,
            "hana_micron_mae_1d_pct": -1.7,
            "hanmi_mae_1d_pct": -4.4,
            "kospi_same_context_pct": -0.7,
            "authorization_effective_delay_days": 120.0,
            "samsung_china_dram_exposure": "more_than_one_third",
            "sk_hynix_china_dram_nand_exposure_pct": "30-40",
        },
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Export-control shock is 4C-watch; hard 4C requires confirmed production or revenue disruption.",
    ),
)


def round219_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND219_CASE_CANDIDATES:
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
                "Round219 R2 Loop-9 AI semiconductor/electronics price validation case. "
                "Calibration-only; not candidate-generation input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "openai" in field or "policy" in field or "design" in field or "authorization" in field or "hbm" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "eps" in field
                or "op_" in field
                or "hbm4" in field
                or "customer" in field
                or "contract" in field
                or "capacity" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "market_cap" in field
                or "crowding" in field
                or "openai" in field
                or "unconfirmed" in field
                or "record" in field
                or "rally" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "labor" in field
                or "strike" in field
                or "export_control" in field
                or "authorization" in field
                or "production" in field
                or "disruption" in field
                or "trust" in field
            ),
            must_have_fields=ROUND219_GREEN_REQUIRED_FIELDS,
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
                "eps_revision_delta": 5.0,
                "capacity_bottleneck_delta": 5.0,
                "hbm4_first_mover_delta": 5.0,
                "customer_visibility_delta": 5.0,
                "memory_price_upcycle_delta": 4.0,
                "confirmed_customer_order_delta": 5.0,
                "order_to_revenue_conversion_delta": 4.0,
                "price_path_alignment_delta": 5.0,
                "unconfirmed_media_report_delta": -5.0,
                "design_win_without_revenue_delta": -5.0,
                "policy_foundry_without_order_delta": -5.0,
                "openai_or_nvidia_headline_without_company_revenue_delta": -4.0,
                "labor_or_export_control_unpriced_delta": -5.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_margins_fcf_or_customer_orders",
                "do_not_treat_ai_keyword_design_win_policy_foundry_openai_headline_or_unconfirmed_customer_report_as_green",
                *ROUND219_GREEN_REQUIRED_FIELDS,
                *ROUND219_GREEN_FORBIDDEN_PATTERNS,
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
                mfe_1y=candidate.reported_mfe_pct,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=(
                    candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.reported_mfe_pct is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                ),
                stage_dates_confidence=0.9 if candidate.stage3_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round219_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND219_CASE_CANDIDATES:
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
                "reported_market_cap_mfe_minimum_pct": _float_text(candidate.reported_market_cap_mfe_minimum_pct),
                "reported_compounded_return_minimum_pct": _float_text(candidate.reported_compounded_return_minimum_pct),
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mfe_1d_secondary": _float_text(candidate.mfe_1d_secondary),
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


def round219_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND219_SCORE_ADJUSTMENTS)


def round219_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND219_SHADOW_WEIGHT_ROWS)


def round219_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round219_price_validation": "true"} for field in ROUND219_PRICE_VALIDATION_FIELDS)


def round219_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round219_label": label, "canonical_archetype": canonical} for label, canonical in ROUND219_REQUIRED_TARGET_ALIASES.items())


def round219_summary() -> dict[str, int | bool | str]:
    cases = ROUND219_CASE_CANDIDATES
    return {
        "source_round": ROUND219_SOURCE_ROUND_PATH,
        "large_sector": ROUND219_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "watch_count": sum(1 for case in cases if case.case_type == "4b_watch"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status in {"watch", "elevated"}),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "reported_price_anchor_count": sum(1 for case in cases if case.price_validation_status != "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND219_REQUIRED_TARGET_ALIASES),
        "shadow_weight_row_count": len(ROUND219_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
    }


def round219_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND219_SOURCE_ROUND_PATH,
        "large_sector": ROUND219_LARGE_SECTOR.value,
        "summary": round219_summary(),
        "target_aliases": dict(ROUND219_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND219_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND219_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND219_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND219_HARD_4C_GATES),
        "score_adjustments": list(round219_score_adjustment_rows()),
        "shadow_weights": list(round219_shadow_weight_rows()),
        "case_ids": [case.case_id for case in ROUND219_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round219_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_design_win_policy_foundry_openai_headline_or_unconfirmed_customer_report_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
            "keep_export_control_and_labor_risk_as_watch_until_real_production_or_revenue_disruption_is_confirmed",
        ],
    }


def render_round219_summary_markdown() -> str:
    summary = round219_summary()
    lines = [
        "# Round 219 R2 Loop 9 AI Semiconductor Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- structural_success: {summary['structural_success_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- 4B watch cases: {summary['stage4b_watch_count']}",
        f"- 4C watch cases: {summary['stage4c_watch_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- reported_price_anchor_count: {summary['reported_price_anchor_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C-watch | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND219_CASE_CANDIDATES:
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
            "- SK하이닉스는 HBM4/EPS revision 이후 큰 가격경로가 확인되지만 현재는 4B-watch/elevated다.",
            "- 삼성전자는 OpenAI event와 Q3 OP 회복으로 Stage 2 후보지만 HBM volume/margin 전 Green은 보류한다.",
            "- 한미반도체는 확인된 SK하이닉스 장비 수주는 좋지만 Micron 미확정 보도 +22%는 4B-watch다.",
            "- 가온칩스 design win과 DB하이텍 foundry 정책 이벤트는 매출·마진 전 Stage 1~2로 제한한다.",
            "- OpenAI/Stargate는 수요 검증이지만 후발주 Green 충분조건이 아니다.",
            "- export-control과 labor risk는 hard 4C가 아니라 4C-watch로 두고 실제 생산/매출 차질 확인을 기다린다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round219_green_gate_review_markdown() -> str:
    lines = [
        "# Round 219 R2 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND219_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND219_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND219_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `HBM4 + EPS revision + 고객 수요 + 가격경로`가 같이 있으면 강한 케이스다.",
            "- `OpenAI headline + 후발주 급등`은 매출·마진 전 Green이 아니라 4B/event watch다.",
            "- `design win`은 좋은 Stage 2 신호지만 tape-out, 양산, 매출, 마진 전 Green은 아니다.",
            "- `수출통제/파업`은 실제 생산·매출 차질 전까지 hard 4C가 아니라 4C-watch다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round219_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round 219 R2 4B / 4C Review",
        "",
        "## 4B Watch Triggers",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND219_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND219_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | interpretation |", "|---|---|---|---|"])
    for case in ROUND219_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round219_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 219 R2 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND219_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND219_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round219_r2_loop9_reports(
    output_directory: str | Path = ROUND219_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND219_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND219_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)

    paths = {
        "cases": write_case_library(round219_case_records(), cases_path),
        "audit": _write_json(round219_audit_payload(), audit_path),
        "summary": output / "round219_r2_loop9_price_validation_summary.md",
        "case_matrix": output / "round219_r2_loop9_case_matrix.csv",
        "target_aliases": output / "round219_r2_loop9_target_aliases.csv",
        "score_adjustments": output / "round219_r2_loop9_score_adjustments.csv",
        "shadow_weights": output / "round219_r2_loop9_shadow_weights.csv",
        "price_validation_fields": output / "round219_r2_loop9_price_validation_fields.csv",
        "green_gate_review": output / "round219_r2_loop9_green_gate_review.md",
        "price_validation_plan": output / "round219_r2_loop9_price_validation_plan.md",
        "stage4b_4c_review": output / "round219_r2_loop9_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round219_summary_markdown(), encoding="utf-8")
    _write_csv(round219_case_rows(), paths["case_matrix"])
    _write_csv(round219_target_alias_rows(), paths["target_aliases"])
    _write_csv(round219_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round219_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round219_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round219_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round219_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round219_stage4b_4c_review_markdown(), encoding="utf-8")
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
