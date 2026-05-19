"""Round-206 R2 Loop-8 AI semiconductor price validation pack.

Round 206 is calibration/evaluation material only. It captures reported price
anchors for HBM leaders, HBM equipment, HBM catch-up, design-win, policy
foundry, export-control shock, and OpenAI/Stargate AI memory events from
``docs/round/round_206.md``.

Simple example: a design win is useful Stage 2 evidence. It is not Stage
3-Green until tape-out, shipment, revenue conversion, gross margin, and
EPS/FCF revision are visible as-of the replay date.
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


ROUND206_SOURCE_ROUND_PATH = "docs/round/round_206.md"
ROUND206_LARGE_SECTOR = Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS
ROUND206_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round206_r2_loop8_ai_semiconductor_price_validation"
ROUND206_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop8_round206.jsonl"
ROUND206_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round206_r2_loop8_ai_semiconductor_price_validation_audit.json"

ROUND206_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "MEMORY_HBM_CAPACITY": E2RArchetype.MEMORY_HBM_CAPACITY.value,
    "MEMORY_HBM_LTA_PREPAYMENT": E2RArchetype.MEMORY_HBM_LTA_PREPAYMENT.value,
    "HBM_CATCHUP_EXECUTION": E2RArchetype.HBM_CATCHUP_EXECUTION.value,
    "COMMODITY_MEMORY_GENERAL_SEMI": E2RArchetype.COMMODITY_MEMORY_GENERAL_SEMI.value,
    "SEMI_EQUIPMENT_AI_CAPEX": E2RArchetype.SEMI_EQUIPMENT_AI_CAPEX.value,
    "HBM_BONDER_EQUIPMENT_KOREA": E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA.value,
    "ADVANCED_PACKAGING_EQUIPMENT_KOREA": E2RArchetype.ADVANCED_PACKAGING_EQUIPMENT_KOREA.value,
    "SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER": E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER.value,
    "AI_CHIP_FABRIC_INFRA": E2RArchetype.AI_CHIP_FABRIC_INFRA.value,
    "AI_DATA_CENTER_INFRASTRUCTURE": E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE.value,
    "REDTEAM_ACCOUNTING_TRUST_OVERLAY": E2RArchetype.REDTEAM_ACCOUNTING_TRUST_OVERLAY.value,
    "AI_CAPEX_CROWDING_OVERLAY": E2RArchetype.AI_CAPEX_CROWDING_OVERLAY.value,
    "DISCLOSURE_CONFIDENCE_CAP": E2RArchetype.DISCLOSURE_CONFIDENCE_CAP.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "GEOPOLITICAL_EXPORT_CONTROL_OVERLAY": E2RArchetype.IP_LEAK_SUPPLY_CHAIN_REDTEAM.value,
}

ROUND206_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "company_level_customer_evidence",
    "product_specific_exposure",
    "order_shipment_contract_or_revenue_path_confirmed",
    "gross_margin_or_opm_improvement",
    "eps_fcf_revision_confirmed",
    "capacity_bottleneck_or_supply_allocation",
    "price_path_after_evidence",
    "export_control_china_fab_accounting_trust_passed",
)

ROUND206_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ai_keyword_only",
    "server_theme_only",
    "unconfirmed_customer_media_report",
    "design_win_without_revenue",
    "policy_foundry_without_order",
    "openai_or_nvidia_headline_without_company_revenue",
)

ROUND206_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "stage3_after_3x_or_more_return",
    "market_cap_milestone_headline",
    "unconfirmed_customer_diversification_report_rally",
    "openai_nvidia_stargate_event_index_rally",
    "ai_capex_consensus_crowding",
    "new_order_price_moves_ahead_of_valuation",
)

ROUND206_HARD_4C_GATES: tuple[str, ...] = (
    "hbm_qualification_failure",
    "order_pushout",
    "customer_capex_cut",
    "memory_price_decline",
    "hbm_supply_normalization",
    "china_fab_export_control_disruption",
    "equipment_authorization_loss",
    "accounting_or_disclosure_trust_break",
    "production_strike_or_labor_disruption",
    "customer_concentration_failure",
)

ROUND206_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "peak_price",
    "reported_mfe_minimum_pct",
    "reported_market_cap_mfe_minimum_pct",
    "reported_compounded_return_minimum_pct",
    "mfe_1d",
    "mfe_1d_secondary",
    "mae_1d",
    "mae_1d_secondary",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round206ScoreAdjustment:
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
class Round206CaseCandidate:
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
    reported_mfe_minimum_pct: float | None
    reported_market_cap_mfe_minimum_pct: float | None
    reported_compounded_return_minimum_pct: float | None
    mfe_1d: float | None
    mfe_1d_secondary: float | None
    mae_1d: float | None
    mae_1d_secondary: float | None
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    peak_price_anchor: float | None
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND206_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND206_SCORE_ADJUSTMENTS: tuple[Round206ScoreAdjustment, ...] = (
    Round206ScoreAdjustment("eps_revision", 5, "raise", "HBM/메모리 rerating은 EPS 상향이 동반될 때 가격경로와 맞았다."),
    Round206ScoreAdjustment("capacity_bottleneck", 5, "raise", "HBM 공급 배분과 CAPA 병목은 R2 구조적 visibility의 핵심이다."),
    Round206ScoreAdjustment("customer_visibility", 5, "raise", "고객 주문과 수요 visibility가 없는 AI 이름표는 부족하다."),
    Round206ScoreAdjustment("confirmed_customer_order", 5, "raise", "확인된 고객 주문과 미확정 media report를 분리한다."),
    Round206ScoreAdjustment("hbm_product_specificity", 4, "raise", "HBM/TSV-TC bonder처럼 제품 노출이 특정될수록 신뢰도가 높다."),
    Round206ScoreAdjustment("order_to_revenue_conversion", 4, "raise", "수주와 design win은 매출 전환 경로가 있을 때 Stage 3 후보가 된다."),
    Round206ScoreAdjustment("gross_margin_visibility", 4, "raise", "R2 Green에는 gross margin 또는 OPM 개선이 필요하다."),
    Round206ScoreAdjustment("price_path_alignment", 5, "raise", "증거 이후 가격경로가 따라온 케이스를 보상한다."),
    Round206ScoreAdjustment("ai_keyword_only", -5, "lower", "AI 이름만으로는 EPS/FCF 체급 변화를 증명하지 못한다."),
    Round206ScoreAdjustment("server_theme_only", -4, "lower", "서버 테마만 있고 고객·제품·마진이 없으면 Green 금지다."),
    Round206ScoreAdjustment("design_win_without_revenue", -4, "lower", "design win은 Stage 2 근거지만 양산·매출 전 Green은 아니다."),
    Round206ScoreAdjustment("policy_foundry_without_order", -4, "lower", "정책 foundry 협의는 회사 단위 order/utilization 전까지 이벤트다."),
    Round206ScoreAdjustment("unconfirmed_media_report", -5, "lower", "미확정 고객 보도 급등은 4B-watch로 분리한다."),
    Round206ScoreAdjustment("openai_or_nvidia_event_without_company_revenue", -3, "lower", "OpenAI/Nvidia headline은 회사 매출 경로 전까지 Green 충분조건이 아니다."),
    Round206ScoreAdjustment("customer_name_without_margin", -3, "lower", "고객 이름만 있고 margin이 없으면 고신뢰 Green을 막는다."),
    Round206ScoreAdjustment("price_rally_before_confirmation", -5, "lower", "확인 전 가격 급등은 price-before-evidence로 본다."),
)


ROUND206_CASE_CANDIDATES: tuple[Round206CaseCandidate, ...] = (
    Round206CaseCandidate(
        case_id="r2_loop8_sk_hynix_hbm_aligned_4b",
        symbol="000660",
        company_name="SK하이닉스",
        primary_archetype=E2RArchetype.MEMORY_HBM_CAPACITY,
        secondary_archetypes=(
            E2RArchetype.MEMORY_HBM_LTA_PREPAYMENT,
            E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH,
            E2RArchetype.CROWDED_RERATING_4B_WATCH,
        ),
        case_type="structural_success",
        stage1_date=None,
        stage2_date=date(2024, 6, 25),
        stage3_date=date(2024, 6, 25),
        stage4b_date=date(2026, 5, 14),
        stage4c_date=None,
        stage3_decision="hbm_dominance_eps_revision_and_old_memory_frame_break_aligned_with_large_mfe",
        stage4b_status="elevated",
        hard_4c_confirmed=False,
        evidence_fields=("hbm_dominance", "memory_price_upcycle", "nomura_op_revision_2024_30tn_2025_53tn", "capacity_sold_out", "old_memory_cycle_frame_break", "reported_stage3_price_222000"),
        red_flag_fields=("market_cap_near_one_trillion", "intel_emib_partnership_report_watch", "crowding_watch", "ai_capex_dependency"),
        price_data_source="MarketWatch/Reuters/Tom's Hardware reported anchors",
        reported_price_anchor="222,000 KRW stage3 anchor; 1,946,000 KRW reported intraday high",
        reported_return_anchor="+776.6% from stage3 anchor to reported peak; market cap minimum +842%; 2025 +274% and 2026 >+200%",
        reported_mfe_minimum_pct=776.6,
        reported_market_cap_mfe_minimum_pct=842.0,
        reported_compounded_return_minimum_pct=1022.0,
        mfe_1d=None,
        mfe_1d_secondary=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=222000.0,
        stage3_price_anchor=222000.0,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=1946000.0,
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="green_success",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="HBM dominance plus EPS revision aligns with a large reported price path; by 2026-05 this is 4B-watch/elevated, not fresh Green.",
    ),
    Round206CaseCandidate(
        case_id="r2_loop8_hanmi_semiconductor_hbm_bonder_4b",
        symbol="042700",
        company_name="한미반도체",
        primary_archetype=E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA,
        secondary_archetypes=(E2RArchetype.SEMI_EQUIPMENT_AI_CAPEX, E2RArchetype.DISCLOSURE_CONFIDENCE_CAP, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="structural_success",
        stage1_date=None,
        stage2_date=date(2024, 3, 26),
        stage3_date=date(2024, 3, 26),
        stage4b_date=date(2024, 3, 28),
        stage4c_date=None,
        stage3_decision="confirmed_sk_hynix_hbm_bonder_order_is_stage3_candidate_but_unconfirmed_micron_report_is_4b_watch",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("tsv_tc_bonder", "confirmed_sk_hynix_customer", "recent_contracts_about_200bn_krw", "hbm_packaging_bottleneck", "stage2_event_plus_16pct"),
        red_flag_fields=("unconfirmed_micron_media_report", "price_ahead_of_confirmed_order", "customer_diversification_rumor", "valuation_crowding_watch"),
        price_data_source="WSJ reported event return and intraday price anchor",
        reported_price_anchor="139,100 KRW intraday after unconfirmed Micron report; implied pre-4B reference about 114,016 KRW",
        reported_return_anchor="+16% on confirmed SK Hynix order day; +22% on unconfirmed Micron report day",
        reported_mfe_minimum_pct=22.0,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=16.0,
        mfe_1d_secondary=22.0,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=139100.0,
        stage4c_price_anchor=None,
        peak_price_anchor=139100.0,
        score_price_alignment="aligned",
        rerating_result="true_rerating",
        stage_failure_type="green_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Confirmed SK Hynix HBM bonder orders support a Stage 3 candidate; unconfirmed Micron customer news is a 4B-watch confidence cap.",
    ),
    Round206CaseCandidate(
        case_id="r2_loop8_samsung_memory_recovery_hbm_watch",
        symbol="005930",
        company_name="삼성전자",
        primary_archetype=E2RArchetype.HBM_CATCHUP_EXECUTION,
        secondary_archetypes=(E2RArchetype.COMMODITY_MEMORY_GENERAL_SEMI, E2RArchetype.AI_CAPEX_CROWDING_OVERLAY),
        case_type="success_candidate",
        stage1_date=date(2025, 10, 2),
        stage2_date=date(2025, 10, 14),
        stage3_date=None,
        stage4b_date=date(2025, 10, 2),
        stage4c_date=None,
        stage3_decision="commodity_memory_recovery_is_stage2_watch_until_hbm_execution_sales_and_margin_are_confirmed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("q3_2025_op_estimate_12_1tn", "commodity_dram_nand_price_up", "data_center_server_demand", "openai_event_close_89000"),
        red_flag_fields=("hbm_lag_vs_sk_hynix", "nvidia_qualification_gap", "hbm_sales_growth_needed", "volume_shipment_needed"),
        price_data_source="Reuters/WSJ reported event return and close anchors",
        reported_price_anchor="OpenAI event close 89,000 KRW",
        reported_return_anchor="+3.5% OpenAI event close; Q3 profit event +2.9% intraday then -0.5% close",
        reported_mfe_minimum_pct=3.5,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=3.5,
        mfe_1d_secondary=2.9,
        mae_1d=-0.5,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=89000.0,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        score_price_alignment="unknown",
        rerating_result="cyclical_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="stage2_watch_not_stage3",
        notes="Commodity memory recovery can be Stage 2, but HBM customer qualification, shipment, margin, and EPS/FCF revision are needed before Green.",
    ),
    Round206CaseCandidate(
        case_id="r2_loop8_gaonchips_pfn_design_win",
        symbol="399720",
        company_name="가온칩스",
        primary_archetype=E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER,
        secondary_archetypes=(E2RArchetype.AI_CHIP_FABRIC_INFRA, E2RArchetype.DISCLOSURE_CONFIDENCE_CAP),
        case_type="success_candidate",
        stage1_date=None,
        stage2_date=date(2024, 7, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="design_win_is_stage2_until_tapeout_mass_production_revenue_and_margin_are_confirmed",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("preferred_networks_ai_chip_design_win", "samsung_2nm_gaa", "advanced_packaging", "generative_ai_hpc_chip"),
        red_flag_fields=("design_win_without_revenue", "tapeout_needed", "mass_production_needed", "gross_margin_needed"),
        price_data_source="Reuters evidence source only",
        reported_price_anchor="no reported price anchor",
        reported_return_anchor="price data unavailable after deep search",
        reported_mfe_minimum_pct=None,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=None,
        mfe_1d_secondary=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="A company-level AI chip design win is useful Stage 2 evidence, but tape-out, volume production, revenue conversion, and margin are required for Stage 3.",
    ),
    Round206CaseCandidate(
        case_id="r2_loop8_db_hitek_policy_foundry",
        symbol="000990",
        company_name="DB하이텍",
        primary_archetype=E2RArchetype.AI_CHIP_FABRIC_INFRA,
        secondary_archetypes=(E2RArchetype.AI_DATA_CENTER_INFRASTRUCTURE, E2RArchetype.DISCLOSURE_CONFIDENCE_CAP, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="event_premium",
        stage1_date=date(2025, 12, 10),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="policy_foundry_consultation_is_attention_only_until_funded_capex_customer_order_utilization_and_eps_revision",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("public_private_40nm_foundry_review", "government_consultation_target", "legacy_chip_policy_support"),
        red_flag_fields=("policy_foundry_without_order", "company_level_contract_missing", "utilization_unknown", "gross_margin_unknown"),
        price_data_source="Reuters evidence source only",
        reported_price_anchor="no reported price anchor",
        reported_return_anchor="price data unavailable after deep search",
        reported_mfe_minimum_pct=None,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=None,
        mfe_1d_secondary=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        score_price_alignment="unknown",
        rerating_result="policy_event_rerating",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Government foundry consultation is Stage 1 attention or weak Stage 2 only; company order, utilization, margin, and EPS/FCF revision are required before Green.",
    ),
    Round206CaseCandidate(
        case_id="r2_loop8_hana_micron_hanmi_export_control_watch",
        symbol="067310/042700",
        company_name="하나마이크론/한미반도체",
        primary_archetype=E2RArchetype.IP_LEAK_SUPPLY_CHAIN_REDTEAM,
        secondary_archetypes=(E2RArchetype.REDTEAM_ACCOUNTING_TRUST_OVERLAY, E2RArchetype.AI_CAPEX_CROWDING_OVERLAY),
        case_type="4b_watch",
        stage1_date=date(2025, 9, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 1),
        stage3_decision="export_control_shock_is_4c_watch_until_actual_production_revenue_or_customer_disruption_is_confirmed",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("us_revokes_china_chip_equipment_authorizations", "samsung_mae_1d_minus_2_3", "sk_hynix_mae_1d_minus_4_4", "hana_micron_mae_1d_minus_1_7", "hanmi_mae_1d_minus_4_4"),
        red_flag_fields=("china_fab_export_control_disruption_watch", "equipment_authorization_loss_watch", "production_revenue_disruption_needs_confirmation"),
        price_data_source="Reuters reported event returns",
        reported_price_anchor="Samsung -2.3%; SK Hynix -4.4%; Hana Micron -1.7%; Hanmi Semiconductor -4.4%",
        reported_return_anchor="export-control shock one-day reported returns",
        reported_mfe_minimum_pct=None,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=None,
        mfe_1d_secondary=None,
        mae_1d=-1.7,
        mae_1d_secondary=-4.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        score_price_alignment="unknown",
        rerating_result="no_rerating",
        stage_failure_type="unknown",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="Export-control shock is a 4C-watch. Hard 4C requires confirmed production disruption, revenue loss, order cancellation, or customer impact.",
    ),
    Round206CaseCandidate(
        case_id="r2_loop8_openai_stargate_memory_4b",
        symbol="000660/005930",
        company_name="SK하이닉스/삼성전자",
        primary_archetype=E2RArchetype.AI_CAPEX_CROWDING_OVERLAY,
        secondary_archetypes=(E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.HBM_CATCHUP_EXECUTION, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="4b_watch",
        stage1_date=date(2025, 10, 1),
        stage2_date=date(2025, 10, 2),
        stage3_date=None,
        stage4b_date=date(2025, 10, 2),
        stage4c_date=None,
        stage3_decision="openai_stargate_validates_ai_memory_demand_but_is_also_4b_watch_after_large_hbm_rerating",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("openai_stargate_loi", "hbm_demand_up_to_900k_dram_wafers_month_discussion", "sk_hynix_close_395500", "samsung_close_89000", "kospi_record_high"),
        red_flag_fields=("openai_or_nvidia_headline_without_company_revenue", "ai_capex_consensus_crowding", "price_rally_before_confirmation"),
        price_data_source="Reuters/FT/WSJ reported return and close price anchors",
        reported_price_anchor="SK Hynix close 395,500 KRW; Samsung close 89,000 KRW",
        reported_return_anchor="SK Hynix +12% intraday / about +10% close; Samsung +3.5% close to +4.7% reported",
        reported_mfe_minimum_pct=12.0,
        reported_market_cap_mfe_minimum_pct=None,
        reported_compounded_return_minimum_pct=None,
        mfe_1d=12.0,
        mfe_1d_secondary=3.5,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=395500.0,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        score_price_alignment="aligned",
        rerating_result="event_premium",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_return_not_full_ohlc",
        notes="OpenAI/Stargate validates AI memory demand for SK Hynix, but after a large HBM rerating it is also 4B-watch; Samsung still needs HBM execution proof.",
    ),
)


def round206_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND206_CASE_CANDIDATES:
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
                "Round206 R2 Loop-8 AI semiconductor price-path validation "
                "case. Calibration-only; not production scoring input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "event" in field or "reported" in field or "loi" in field or "policy" in field or "watch" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "hbm" in field
                or "eps" in field
                or "op_revision" in field
                or "capacity" in field
                or "confirmed" in field
                or "customer" in field
                or "memory_price" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "crowding" in field
                or "market_cap" in field
                or "openai" in field
                or "price_rally" in field
                or "unconfirmed" in field
                or "milestone" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "export_control" in field
                or "qualification" in field
                or "capex_cut" in field
                or "disruption" in field
                or "trust" in field
                or "authorization" in field
            ),
            must_have_fields=ROUND206_GREEN_REQUIRED_FIELDS,
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
                "eps_revision_delta": 5.0,
                "capacity_bottleneck_delta": 5.0,
                "customer_visibility_delta": 5.0,
                "confirmed_customer_order_delta": 5.0,
                "hbm_product_specificity_delta": 4.0,
                "order_to_revenue_conversion_delta": 4.0,
                "gross_margin_visibility_delta": 4.0,
                "price_path_alignment_delta": 5.0,
                "ai_keyword_only_delta": -5.0,
                "server_theme_only_delta": -4.0,
                "design_win_without_revenue_delta": -4.0,
                "policy_foundry_without_order_delta": -4.0,
                "unconfirmed_media_report_delta": -5.0,
                "openai_or_nvidia_event_without_company_revenue_delta": -3.0,
                "customer_name_without_margin_delta": -3.0,
                "price_rally_before_confirmation_delta": -5.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_ai_keyword_design_win_policy_foundry_or_unconfirmed_customer_report_as_green",
                *ROUND206_GREEN_REQUIRED_FIELDS,
                *ROUND206_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_price=candidate.peak_price_anchor,
                peak_return_from_stage3=candidate.reported_mfe_minimum_pct,
                mfe_30d=candidate.mfe_1d,
                mfe_1y=candidate.reported_mfe_minimum_pct,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=False,
                stage_dates_confidence=0.85 if candidate.stage3_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round206_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND206_CASE_CANDIDATES:
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
                "reported_mfe_minimum_pct": _float_text(candidate.reported_mfe_minimum_pct),
                "reported_market_cap_mfe_minimum_pct": _float_text(candidate.reported_market_cap_mfe_minimum_pct),
                "reported_compounded_return_minimum_pct": _float_text(candidate.reported_compounded_return_minimum_pct),
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mfe_1d_secondary": _float_text(candidate.mfe_1d_secondary),
                "mae_1d": _float_text(candidate.mae_1d),
                "mae_1d_secondary": _float_text(candidate.mae_1d_secondary),
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


def round206_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND206_SCORE_ADJUSTMENTS)


def round206_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round206_price_validation": "true"} for field in ROUND206_PRICE_VALIDATION_FIELDS)


def round206_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple(
        {"round206_label": label, "canonical_archetype": canonical}
        for label, canonical in ROUND206_REQUIRED_TARGET_ALIASES.items()
    )


def round206_summary() -> dict[str, int | bool | str]:
    records = round206_case_records()
    return {
        "case_candidate_count": len(records),
        "required_target_count": len(ROUND206_REQUIRED_TARGET_ALIASES),
        "score_adjustment_count": len(ROUND206_SCORE_ADJUSTMENTS),
        "price_validation_field_count": len(ROUND206_PRICE_VALIDATION_FIELDS),
        "structural_success_count": sum(1 for case in records if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in records if case.case_type == "success_candidate"),
        "event_premium_or_watch_count": sum(1 for case in records if case.case_type in {"event_premium", "4b_watch"}),
        "hard_4c_case_count": sum(1 for case in ROUND206_CASE_CANDIDATES if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in ROUND206_CASE_CANDIDATES if case.stage3_date),
        "stage4b_watch_or_elevated_count": sum(
            1 for case in ROUND206_CASE_CANDIDATES if case.stage4b_status in {"watch", "elevated"}
        ),
        "reported_price_anchor_count": sum(
            1 for case in ROUND206_CASE_CANDIDATES if case.price_validation_status != "price_data_unavailable_after_deep_search"
        ),
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
    }


def write_round206_r2_loop8_reports(
    *,
    output_directory: str | Path = ROUND206_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND206_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND206_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cases = write_case_library(round206_case_records(), cases_path)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": cases,
        "audit_json": audit,
        "summary": output / "round206_r2_loop8_price_validation_summary.md",
        "case_matrix": output / "round206_r2_loop8_case_matrix.csv",
        "target_aliases": output / "round206_r2_loop8_target_aliases.csv",
        "score_adjustments": output / "round206_r2_loop8_score_adjustments.csv",
        "price_validation_fields": output / "round206_r2_loop8_price_validation_fields.csv",
        "green_gate_review": output / "round206_r2_loop8_green_gate_review.md",
        "price_validation_plan": output / "round206_r2_loop8_price_validation_plan.md",
        "stage4b_4c_review": output / "round206_r2_loop8_stage4b_4c_review.md",
    }
    audit.write_text(json.dumps(round206_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round206_case_rows(), paths["case_matrix"])
    _write_rows(round206_target_alias_rows(), paths["target_aliases"])
    _write_rows(round206_score_adjustment_rows(), paths["score_adjustments"])
    _write_rows(round206_price_validation_field_rows(), paths["price_validation_fields"])
    paths["summary"].write_text(render_round206_summary_markdown(), encoding="utf-8")
    paths["green_gate_review"].write_text(render_round206_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round206_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round206_stage4b_4c_review_markdown(), encoding="utf-8")
    return paths


def round206_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND206_SOURCE_ROUND_PATH,
        "large_sector": ROUND206_LARGE_SECTOR.value,
        "summary": round206_summary(),
        "target_aliases": list(round206_target_alias_rows()),
        "green_required_fields": list(ROUND206_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND206_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND206_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND206_HARD_4C_GATES),
        "score_adjustments": list(round206_score_adjustment_rows()),
        "case_ids": [case.case_id for case in ROUND206_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round206_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_ai_keyword_design_win_policy_foundry_or_unconfirmed_customer_report_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
            "keep_full_ohlc_complete_false_until_official_backfill_is_done",
        ],
    }


def render_round206_summary_markdown() -> str:
    summary = round206_summary()
    lines = [
        "# Round-206 R2 Loop-8 Price-Path Validation Summary",
        "",
        f"- source_round: `{ROUND206_SOURCE_ROUND_PATH}`",
        f"- large_sector: `{ROUND206_LARGE_SECTOR.value}`",
        "- scope: HBM leader, HBM equipment, HBM catch-up, design house, policy foundry, export-control shock, and OpenAI/Stargate memory event",
        f"- case_candidate_count: {summary['case_candidate_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- score_adjustment_count: {summary['score_adjustment_count']}",
        f"- price_validation_field_count: {summary['price_validation_field_count']}",
        f"- structural_success_count: {summary['structural_success_count']}",
        f"- success_candidate_count: {summary['success_candidate_count']}",
        f"- event_premium_or_watch_count: {summary['event_premium_or_watch_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- stage3_case_count: {summary['stage3_case_count']}",
        f"- stage4b_watch_or_elevated_count: {summary['stage4b_watch_or_elevated_count']}",
        f"- reported_price_anchor_count: {summary['reported_price_anchor_count']}",
        "- production_scoring_changed: false",
        "- candidate_generation_input: false",
        "- shadow_weight_only: true",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Interpretation",
        "",
        "- SK하이닉스는 HBM dominance와 EPS revision이 실제 대형 MFE와 맞았던 aligned benchmark다.",
        "- 한미반도체는 confirmed SK Hynix order와 unconfirmed Micron report를 분리해야 한다.",
        "- 삼성전자는 commodity memory 회복으로 Stage 2 watch가 가능하지만, HBM execution 전 Green은 보류한다.",
        "- 가온칩스 design win과 DB하이텍 policy foundry는 매출·마진 전까지 Stage 3-Green 근거가 아니다.",
        "- export-control shock은 hard 4C가 아니라 4C-watch다. 실제 생산·매출 차질이 확인되어야 hard 4C다.",
        "- OpenAI/Stargate event는 수요 검증이면서, 이미 오른 HBM winner에게는 4B-watch다.",
        "",
        "쉬운 예: `as_of_date=2024-07-09`에 가온칩스가 AI chip design win에 언급되어도, 그날 tape-out·양산·매출·마진이 없으면 Stage 3-Green이 아니라 Stage 2 watch다.",
    ]
    return "\n".join(lines) + "\n"


def render_round206_green_gate_review_markdown() -> str:
    lines = [
        "# Round-206 R2 Loop-8 Green Gate Review",
        "",
        "## Green Required Evidence",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND206_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Green Forbidden Patterns", ""])
    lines.extend(f"- `{field}`" for field in ROUND206_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "| --- | --- | ---: | --- |"])
    for adjustment in ROUND206_SCORE_ADJUSTMENTS:
        lines.append(f"| `{adjustment.axis}` | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## What Not To Change",
            "",
            "- Do not apply these weights to production scoring yet.",
            "- Do not use Round206 cases as candidate-generation input.",
            "- Do not lower Stage 3-Green thresholds to force promotion.",
            "- Do not invent full OHLC, stage prices, or MFE/MAE when only reported anchors exist.",
            "- Do not treat AI keyword, server theme, design win, policy foundry, unconfirmed customer report, or OpenAI/Nvidia headline as Green evidence alone.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round206_price_validation_plan_markdown() -> str:
    lines = [
        "# Round-206 R2 Loop-8 Price Validation Plan",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND206_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | price data source | reported anchor | status |", "| --- | --- | --- | --- |"])
    for case in ROUND206_CASE_CANDIDATES:
        lines.append(
            f"| `{case.case_id}` | {case.price_data_source} | {case.reported_return_anchor} | `{case.price_validation_status}` |"
        )
    lines.extend(
        [
            "",
            "## Backfill Rule",
            "",
            "- Use reported Reuters/WSJ/FT/MarketWatch/Tom's Hardware anchors only for fields they explicitly support.",
            "- Keep full OHLC unavailable until official or adjusted daily price backfill is done.",
            "- Separate Stage 2 design/order evidence, Stage 3 HBM/EPS evidence, 4B crowding, and 4C-watch export-control events.",
            "- Do not create a Stage 3 anchor when the case intentionally has no Stage 3 date.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round206_stage4b_4c_review_markdown() -> str:
    lines = [
        "# Round-206 R2 Loop-8 Stage 4B / 4C Review",
        "",
        "## 4B Watch Triggers",
        "",
    ]
    lines.extend(f"- `{field}`" for field in ROUND206_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- `{field}`" for field in ROUND206_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## R2 Loop-8 Interpretation",
            "",
            "- HBM winner가 맞아도 Stage 3 이후 3배 이상 오르면 신규 Green보다 4B-watch를 붙인다.",
            "- 미확정 고객 보도 급등은 disclosure confidence cap과 4B-watch다.",
            "- export-control shock은 4C-watch이며, 실제 생산·매출 차질 확인 전까지 hard 4C로 확정하지 않는다.",
            "- OpenAI/Stargate는 수요 검증이지만, 회사별 매출·마진 경로가 없으면 Green 충분조건이 아니다.",
            "",
            "## Case Review",
            "",
            "| case | 4B status | hard 4C confirmed | interpretation |",
            "| --- | --- | --- | --- |",
        ]
    )
    for case in ROUND206_CASE_CANDIDATES:
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
    "ROUND206_CASE_CANDIDATES",
    "ROUND206_DEFAULT_AUDIT_PATH",
    "ROUND206_DEFAULT_CASES_PATH",
    "ROUND206_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND206_GREEN_FORBIDDEN_PATTERNS",
    "ROUND206_GREEN_REQUIRED_FIELDS",
    "ROUND206_HARD_4C_GATES",
    "ROUND206_PRICE_VALIDATION_FIELDS",
    "ROUND206_REQUIRED_TARGET_ALIASES",
    "ROUND206_SCORE_ADJUSTMENTS",
    "ROUND206_SOURCE_ROUND_PATH",
    "ROUND206_STAGE4B_WATCH_TRIGGERS",
    "Round206CaseCandidate",
    "Round206ScoreAdjustment",
    "render_round206_green_gate_review_markdown",
    "render_round206_price_validation_plan_markdown",
    "render_round206_stage4b_4c_review_markdown",
    "render_round206_summary_markdown",
    "round206_audit_payload",
    "round206_case_records",
    "round206_case_rows",
    "round206_price_validation_field_rows",
    "round206_score_adjustment_rows",
    "round206_summary",
    "round206_target_alias_rows",
    "write_round206_r2_loop8_reports",
]
