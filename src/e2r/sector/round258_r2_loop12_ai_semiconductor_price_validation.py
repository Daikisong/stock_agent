"""Round-258 R2 Loop-12 AI/semiconductor/electronics price validation pack.

This module converts ``docs/round/round_258.md`` into calibration-only
case-library records and reports. It intentionally leaves production scoring,
candidate generation, and StageClassifier thresholds unchanged.

Easy example: SK Hynix can be a true HBM structural success, but after a
massive multi-year return it also becomes 4B-watch. Samsung's HBM4/foundry
catch-up is Stage 2 until volume shipment, margin, EPS/FCF revision, labor risk,
and China export-control risk clear.
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


ROUND258_SOURCE_ROUND_PATH = "docs/round/round_258.md"
ROUND258_ROUND_ID = "round_186"
ROUND258_LARGE_SECTOR = Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS.value
ROUND258_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round258_r2_loop12_ai_semiconductor_price_validation"
ROUND258_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop12_round258.jsonl"
ROUND258_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round258_r2_loop12_ai_semiconductor_price_validation_audit.json"

ROUND258_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "MEMORY_HBM4_CAPACITY_LEADER": E2RArchetype.MEMORY_HBM4_CAPACITY_LEADER.value,
    "HBM_CATCHUP_FOUNDRY_TURNAROUND": E2RArchetype.HBM_CATCHUP_FOUNDRY_TURNAROUND.value,
    "HBM_BONDER_EQUIPMENT_ORDER": E2RArchetype.HBM_BONDER_EQUIPMENT_ORDER.value,
    "SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER": E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER.value,
    "AI_DEVICE_COMPONENT_OPTIONALITY": E2RArchetype.AI_DEVICE_COMPONENT_OPTIONALITY.value,
    "DISPLAY_LCD_EXIT_OLED_TURNAROUND": E2RArchetype.DISPLAY_LCD_EXIT_OLED_TURNAROUND.value,
    "CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF": E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF.value,
    "GEOPOLITICAL_EXPORT_CONTROL_OVERLAY": E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY.value,
}

ROUND258_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "confirmed_customer_order",
    "product_specific_exposure",
    "delivery_mass_production_shipment_readiness",
    "revenue_recognition_path",
    "gross_margin_or_opm_improvement",
    "eps_fcf_revision",
    "capacity_bottleneck_or_allocation_power",
    "customer_concentration_china_labor_export_control_risk_passed",
    "price_path_after_evidence",
)

ROUND258_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ai_keyword_only",
    "unconfirmed_customer_rumor",
    "design_win_only",
    "apple_replacement_cycle_only",
    "capex_plant_sale_partnership_only",
    "china_customer_relief_only",
    "labor_strike_risk_unresolved",
    "export_control_risk_unresolved",
)

ROUND258_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "stage3_after_3x_to_5x_plus",
    "market_cap_milestone_headline",
    "hbm_customer_rumor_plus_20pct",
    "kospi_7000_or_ai_fomo_day_largecap_plus_10pct",
    "apple_ai_lidar_optionality_component_rally",
    "china_cxmt_relief_equipment_rally",
    "good_news_price_response_deteriorates",
)

ROUND258_HARD_4C_GATES: tuple[str, ...] = (
    "hbm_qualification_failure",
    "volume_shipment_failure",
    "customer_order_cancellation",
    "order_push_out",
    "china_fab_license_denial",
    "china_technology_upgrade_block",
    "labor_strike_production_halt",
    "ip_leakage_china_competitive_catchup",
    "gross_margin_collapse",
    "customer_concentration_loss",
    "cash_burn_or_capex_overrun",
)

ROUND258_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
    "price_data_source",
    "full_ohlc_available",
    "reported_price_anchor",
    "reported_return_anchor",
    "stage2_price_anchor",
    "stage3_price",
    "stage4b_price",
    "stage4c_price",
    "mfe_1d",
    "mae_1d",
    "mfe_30d",
    "mae_30d",
    "contract_capex_policy_value_anchor",
    "market_share_anchor",
    "labor_export_control_anchor",
    "customer_rumor_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round258ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round258ShadowWeightRow:
    archetype: E2RArchetype
    confirmed_customer_order: int
    hbm_transition: int
    capacity_bottleneck: int
    advanced_packaging: int
    euv_order: int
    production_readiness: int
    design_lockin: int
    order_to_revenue: int
    gross_margin: int
    price_path_alignment: int
    event_penalty: int
    china_labor_export_redteam: int
    stage4b_watch_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "confirmed_customer_order": _signed(self.confirmed_customer_order),
            "hbm_transition": _signed(self.hbm_transition),
            "capacity_bottleneck": _signed(self.capacity_bottleneck),
            "advanced_packaging": _signed(self.advanced_packaging),
            "euv_order": _signed(self.euv_order),
            "production_readiness": _signed(self.production_readiness),
            "design_lockin": _signed(self.design_lockin),
            "order_to_revenue": _signed(self.order_to_revenue),
            "gross_margin": _signed(self.gross_margin),
            "price_path_alignment": _signed(self.price_path_alignment),
            "event_penalty": _signed(self.event_penalty),
            "china_labor_export_redteam": _signed(self.china_labor_export_redteam),
            "4b_watch_sensitivity": _signed(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round258DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round258CaseCandidate:
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
    mfe_1d: float | None
    mae_1d: float | None
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


ROUND258_SCORE_ADJUSTMENTS: tuple[Round258ScoreAdjustment, ...] = (
    Round258ScoreAdjustment("confirmed_customer_order", 5, "raise", "R2는 고객 주문이 확인될 때만 강하게 본다."),
    Round258ScoreAdjustment("HBM_generation_transition", 5, "raise", "HBM 세대 전환은 EPS/FCF 체급 변화의 핵심 증거다."),
    Round258ScoreAdjustment("capacity_bottleneck", 5, "raise", "CAPA 병목과 allocation은 단순 AI keyword보다 강하다."),
    Round258ScoreAdjustment("advanced_packaging_capacity", 5, "raise", "advanced packaging CAPA가 HBM 출하로 이어질 때 visibility가 오른다."),
    Round258ScoreAdjustment("EUV_order", 5, "raise", "EUV 발주는 HBM/advanced DRAM 생산능력 검증 신호다."),
    Round258ScoreAdjustment("delivery_or_mass_production_readiness", 5, "raise", "출하·양산 readiness가 design win을 매출로 바꾼다."),
    Round258ScoreAdjustment("customer_specific_design_lockin", 4, "raise", "고객별 HBM4·ASIC lock-in은 반복 수요 가능성을 높인다."),
    Round258ScoreAdjustment("order_to_revenue_conversion", 5, "raise", "주문과 design win은 매출·마진으로 전환되어야 한다."),
    Round258ScoreAdjustment("gross_margin_visibility", 5, "raise", "메모리·장비·부품 모두 마진 가시성이 필요하다."),
    Round258ScoreAdjustment("price_path_alignment", 5, "raise", "증거 이후 가격경로가 따라오는지 검증한다."),
    Round258ScoreAdjustment("AI_keyword_only", -5, "lower", "AI 이름만 있으면 Stage 1 연구 라우팅 수준이다."),
    Round258ScoreAdjustment("unconfirmed_customer_rumor", -5, "lower", "미확정 고객 보도로 급등하면 4B-watch다."),
    Round258ScoreAdjustment("design_win_without_revenue", -5, "lower", "design win은 양산·매출·마진 전 Stage 2다."),
    Round258ScoreAdjustment("Apple_AI_replacement_cycle_only", -4, "lower", "Apple AI 교체수요 기대만으로 부품주 Green은 금지다."),
    Round258ScoreAdjustment("lidar_optionality_without_volume", -4, "lower", "lidar optionality는 실제 volume ramp 전 event premium이다."),
    Round258ScoreAdjustment("LCD_exit_without_OLED_profit", -4, "lower", "LCD exit는 OLED 이익과 FCF 전 Stage 2다."),
    Round258ScoreAdjustment("China_customer_concentration", -5, "lower", "중국 고객 집중은 export-control RedTeam을 키운다."),
    Round258ScoreAdjustment("export_control_exposure", -5, "lower", "중국 fab 장비허가 리스크는 4C-watch다."),
    Round258ScoreAdjustment("labor_disruption_risk", -5, "lower", "파업·생산중단은 HBM/foundry 실행 신뢰도를 낮춘다."),
    Round258ScoreAdjustment("event_rally_before_revenue", -5, "lower", "매출 전 event rally는 4B-watch다."),
)


ROUND258_SHADOW_WEIGHT_ROWS: tuple[Round258ShadowWeightRow, ...] = (
    Round258ShadowWeightRow(E2RArchetype.MEMORY_HBM4_CAPACITY_LEADER, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, -1, 4, 5, 4, "SK Hynix is aligned Stage 3 but current state is 4B-watch."),
    Round258ShadowWeightRow(E2RArchetype.HBM_CATCHUP_FOUNDRY_TURNAROUND, 5, 5, 4, 4, 3, 5, 4, 5, 5, 4, -3, 5, 5, 4, "Samsung is Stage 2 until volume/margin and labor/export-control risk clear."),
    Round258ShadowWeightRow(E2RArchetype.HBM_BONDER_EQUIPMENT_ORDER, 5, 5, 5, 4, 1, 4, 3, 5, 5, 5, -4, 4, 5, 4, "Hanmi confirmed order is good, but unconfirmed customer rumor gets 4B penalty."),
    Round258ShadowWeightRow(E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER, 3, 2, 2, 3, 0, 3, 5, 5, 4, 3, -5, 2, 4, 4, "Gaonchips design win needs tape-out, mass production and revenue."),
    Round258ShadowWeightRow(E2RArchetype.AI_DEVICE_COMPONENT_OPTIONALITY, 3, 2, 2, 2, 0, 3, 3, 5, 4, 4, -5, 2, 5, 3, "LG Innotek Apple AI/lidar optionality needs actual volume and margin."),
    Round258ShadowWeightRow(E2RArchetype.DISPLAY_LCD_EXIT_OLED_TURNAROUND, 2, 0, 1, 0, 0, 3, 1, 4, 5, 3, -4, 2, 4, 4, "LG Display LCD exit/loss narrowing is Stage 2 until OLED profit/FCF confirm."),
    Round258ShadowWeightRow(E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF, 3, 2, 3, 2, 0, 3, 2, 4, 4, 3, -5, 5, 5, 4, "Jusung/Mirae relief is not Green due China concentration/export-control risk."),
    Round258ShadowWeightRow(E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 5, 4, 5, "China fab VEU revocation and MATCH Act are 4C-watch overlays."),
)


ROUND258_DEEP_SUB_ARCHETYPES: tuple[Round258DeepSubArchetype, ...] = (
    Round258DeepSubArchetype("HBM leader", E2RArchetype.MEMORY_HBM4_CAPACITY_LEADER, ("SK Hynix", "HBM sold-out", "HBM4 certification", "ASML EUV", "advanced packaging", "4B-watch")),
    Round258DeepSubArchetype("Samsung catch-up", E2RArchetype.HBM_CATCHUP_FOUNDRY_TURNAROUND, ("Samsung Electronics", "HBM4 Nvidia", "AMD MoU", "foundry turnaround", "union strike", "China fab export-control")),
    Round258DeepSubArchetype("HBM bonder equipment", E2RArchetype.HBM_BONDER_EQUIPMENT_ORDER, ("Hanmi Semiconductor", "TSV-TC bonder", "SK Hynix confirmed order", "Micron unconfirmed report")),
    Round258DeepSubArchetype("Design house", E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER, ("Gaonchips", "Preferred Networks", "Samsung 2nm GAA", "advanced packaging", "order size undisclosed")),
    Round258DeepSubArchetype("AI-device components", E2RArchetype.AI_DEVICE_COMPONENT_OPTIONALITY, ("LG Innotek", "Apple Intelligence", "camera module", "Aeva lidar", "single customer risk")),
    Round258DeepSubArchetype("Display turnaround", E2RArchetype.DISPLAY_LCD_EXIT_OLED_TURNAROUND, ("LG Display", "LCD exit", "Guangzhou sale", "OLED focus", "loss narrowing")),
    Round258DeepSubArchetype("China/CXMT relief", E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF, ("Jusung Engineering", "Mirae Corp", "CXMT exclusion", "China customer concentration")),
    Round258DeepSubArchetype("Export-control RedTeam", E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, ("Samsung", "SK Hynix", "Hana Micron", "Hanmi", "VEU revocation", "MATCH Act")),
)


ROUND258_CASE_CANDIDATES: tuple[Round258CaseCandidate, ...] = (
    Round258CaseCandidate(
        case_id="r2_loop12_sk_hynix_hbm4_structural_success_4b",
        symbol="000660",
        company_name="SK Hynix",
        primary_archetype=E2RArchetype.MEMORY_HBM4_CAPACITY_LEADER,
        secondary_archetypes=(E2RArchetype.MEMORY_HBM_CAPACITY_LEADER, E2RArchetype.HBM_EUV_ADVANCED_PACKAGING_CAPEX, E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH),
        case_type="structural_success",
        round_case_type="structural_success + 4B-watch",
        stage1_date=date(2024, 5, 2),
        stage2_date=date(2025, 9, 12),
        stage3_date=date(2025, 10, 29),
        stage4b_date=date(2026, 5, 14),
        stage4c_date=None,
        stage3_decision="hbm4_certification_record_op_sold_out_output_euv_and_advanced_packaging_validate_stage3_but_current_state_is_4b_watch",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("hbm_sold_out_2024", "hbm_almost_booked_2025", "hbm4_internal_certification", "q3_2025_op_11_4tn_krw", "asml_euv_order_11_95tn_krw", "advanced_packaging_plant_19tn_krw"),
        red_flag_fields=("reported_return_2025_274pct", "reported_return_2026_ytd_above_200pct", "market_cap_milestone_942bn_usd", "ai_memory_consensus_crowded"),
        price_data_source="WSJ / Reuters reported price and event anchors",
        reported_price_anchor="HBM4 +7.3%; Q3 OP event +6.0%; ASML EUV +5.7%; market cap about $942B",
        reported_return_anchor="HBM sold out; Q3 OP 11.4T KRW +62%; 2025 +274%; 2026 >+200%",
        mfe_1d=7.3,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hbm_sold_out_2024": True, "hbm_almost_booked_2025": True, "ai_chip_revenue_share_2023_pct": 5.0, "ai_chip_revenue_share_2028_expected_pct": 61.0, "hbm4_certification_event_mfe_pct": 7.3, "kospi_same_context_pct": 1.2, "relative_outperformance_pp": 6.1, "q3_2025_op_krw_trn": 11.4, "q3_2025_op_growth_pct": 62.0, "q3_2025_event_mfe_pct": 6.0, "q3_kospi_same_context_pct": 1.5, "q3_relative_outperformance_pp": 4.5, "asml_euv_order_krw_trn": 11.95, "asml_euv_order_usd_bn": 7.97, "asml_event_mfe_pct": 5.7, "advanced_packaging_investment_krw_trn": 19.0, "advanced_packaging_investment_usd_bn": 12.9, "reported_return_2025_pct": 274.0, "reported_return_2026_ytd_min_pct": 200.0, "market_cap_usd_bn": 942.0, "market_cap_mfe_from_under_100b_pct": 842.0},
        score_price_alignment="aligned",
        round_alignment_label="aligned_but_now_4B",
        rerating_result="true_rerating",
        round_rerating_label="true_HBM_structural_rerating",
        stage_failure_type="green_success",
        round_stage_failure_label="current_state_4B_watch",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="HBM sold-out, HBM4, OP, EUV, packaging이 연결된 Stage 3 benchmark지만 현재는 massive MFE로 4B-watch다.",
    ),
    Round258CaseCandidate(
        case_id="r2_loop12_samsung_hbm4_foundry_labor_export_watch",
        symbol="005930",
        company_name="Samsung Electronics",
        primary_archetype=E2RArchetype.HBM_CATCHUP_FOUNDRY_TURNAROUND,
        secondary_archetypes=(E2RArchetype.HBM_CATCHUP_EXECUTION, E2RArchetype.FOUNDRY_TURNAROUND_CONTRACT, E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, E2RArchetype.LABOR_SUPPLY_CHAIN_4C_WATCH),
        case_type="success_candidate",
        round_case_type="success_candidate + 4C-watch",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 1, 25),
        stage3_date=None,
        stage4b_date=date(2026, 5, 6),
        stage4c_date=date(2025, 9, 1),
        stage3_decision="hbm4_and_foundry_catchup_are_stage2_until_volume_shipment_margin_eps_fcf_labor_and_export_control_risks_clear",
        stage4b_status="4B-watch/4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("hbm4_nvidia_production_start", "hbm4_qualification_for_nvidia_amd", "nvidia_ai_chip_tieup_4nm", "amd_hbm4_ddr5_mou", "market_cap_1tn_usd_event"),
        red_flag_fields=("china_fab_export_control_event", "samsung_china_dram_more_than_one_third", "labor_strike_risk_45000_workers", "volume_margin_eps_unconfirmed"),
        price_data_source="Reuters HBM4 / Nvidia / AMD / KOSPI / labor / export-control anchors",
        reported_price_anchor="HBM4 +2.2%; Nvidia tie-up +5.0% to 196,800 KRW; KOSPI 7000 day +14.4%; export-control -2.3%",
        reported_return_anchor="HBM4 for Nvidia/AMD; AMD MoU; China fab exposure; labor strike risk",
        mfe_1d=5.0,
        mae_1d=-2.3,
        stage2_price_anchor=196800.0,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"hbm4_nvidia_event_mfe_pct": 2.2, "sk_hynix_same_context_pct": -2.9, "nvidia_ai_chip_tieup_event_mfe_pct": 5.0, "nvidia_tieup_price_anchor_krw": 196800.0, "kospi_same_context_nvidia_pct": 2.7, "relative_outperformance_nvidia_event_pp": 2.3, "kospi_7000_day_samsung_mfe_pct": 14.4, "kospi_7000_day_kospi_pct": 6.45, "relative_outperformance_kospi7000_pp": 7.95, "market_cap_milestone_usd_trn": 1.0, "samsung_hbm_share_pct": 22.0, "sk_hynix_hbm_share_pct": 57.0, "china_export_control_mae_pct": -2.3, "kospi_export_control_context_pct": -0.7, "relative_underperformance_export_control_pp": -1.6, "samsung_china_dram_exposure": "more_than_one_third", "strike_risk_workers": 45000, "strike_start_target": "2026-05-21", "hard_4c_status": "not_confirmed_as_of_2026-05-18"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4C_watch",
        rerating_result="unknown",
        round_rerating_label="HBM4_foundry_catchup_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_not_green_until_volume_margin_labor_export_risk_clear",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="HBM4/foundry catch-up Stage 2지만 shipment/margin과 노동·중국 fab 리스크가 Green을 막는다.",
    ),
    Round258CaseCandidate(
        case_id="r2_loop12_hanmi_hbm_bonder_order_rumor_4b",
        symbol="042700",
        company_name="Hanmi Semiconductor",
        primary_archetype=E2RArchetype.HBM_BONDER_EQUIPMENT_ORDER,
        secondary_archetypes=(E2RArchetype.HBM_BONDER_EQUIPMENT, E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA, E2RArchetype.PRICE_ONLY_RALLY, E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate + 4B-watch",
        stage1_date=date(2024, 3, 1),
        stage2_date=date(2024, 3, 1),
        stage3_date=None,
        stage4b_date=date(2024, 3, 28),
        stage4c_date=date(2025, 9, 1),
        stage3_decision="confirmed_sk_hynix_order_supports_stage2_but_unconfirmed_customer_rumor_is_4b_and_revenue_margin_eps_conversion_required",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("tsv_tc_bonder", "confirmed_sk_hynix_contract_21_48bn_krw", "recent_contract_wins_200bn_krw", "hbm_packaging_equipment"),
        red_flag_fields=("micron_deal_unconfirmed_media_report", "micron_rumor_event_mfe_22pct", "customer_concentration", "china_export_control_event_mae_minus_4_4pct"),
        price_data_source="WSJ / Reuters event and contract anchors",
        reported_price_anchor="Micron unconfirmed report +22% to 139,100 KRW",
        reported_return_anchor="SK Hynix contract 21.48B KRW; recent contract wins about 200B KRW",
        mfe_1d=22.0,
        mae_1d=-4.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=139100.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"sk_hynix_contract_krw_bn": 21.48, "recent_contract_wins_krw_bn": 200.0, "event_mfe_20240326_pct": 16.0, "sk_hynix_event_mfe_20240326_pct": 4.3, "kospi_same_context_pct": 0.7, "relative_outperformance_20240326_pp": 15.3, "micron_rumor_event_mfe_pct": 22.0, "rumor_event_price_krw": 139100.0, "implied_pre_rumor_reference_price_krw": 114016.0, "kospi_rumor_context_pct": -0.3, "relative_outperformance_rumor_pp": 22.3, "micron_deal_status": "unconfirmed_media_report", "china_export_control_event_mae_pct": -4.4},
        score_price_alignment="aligned",
        round_alignment_label="success_candidate_4B_watch",
        rerating_result="unknown",
        round_rerating_label="HBM_bonder_equipment_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="confirmed_order_good_but_unconfirmed_customer_rumor_4B",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="확정 SK하이닉스 주문은 Stage 2지만 Micron 미확정 보도 +22%는 4B-watch다.",
    ),
    Round258CaseCandidate(
        case_id="r2_loop12_gaonchips_pfn_ai_design_house",
        symbol="399720",
        company_name="Gaonchips",
        primary_archetype=E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER,
        secondary_archetypes=(E2RArchetype.STAGE2_EVIDENCE_NOT_GREEN,),
        case_type="success_candidate",
        round_case_type="success_candidate / insufficient_price_data",
        stage1_date=date(2024, 7, 9),
        stage2_date=date(2024, 7, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="design_win_is_stage2_but_tapeout_mass_production_revenue_and_gross_margin_required_before_green",
        stage4b_status="4B-watch-if-design-house-theme-rallies",
        hard_4c_confirmed=False,
        evidence_fields=("preferred_networks_ai_chip_order", "samsung_2nm_gaa", "advanced_packaging", "gaonchips_designed_chips", "generative_ai_llm_hpc_end_use"),
        red_flag_fields=("order_size_not_disclosed", "design_win_without_revenue", "mass_production_unconfirmed", "tapeout_delay_risk"),
        price_data_source="Reuters design-win evidence",
        reported_price_anchor="Gaonchips adjusted OHLC or event return unavailable in this pass",
        reported_return_anchor="Preferred Networks AI chip uses Samsung 2nm GAA and advanced packaging; Gaonchips designed the chips",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"order_size": "not_disclosed", "customer": "Preferred Networks", "foundry": "Samsung Electronics", "process": "2nm GAA", "packaging": "advanced packaging", "designer": "Gaonchips", "end_use": "generative AI / LLM high-performance computing hardware"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_insufficient_price_data",
        rerating_result="unknown",
        round_rerating_label="AI_design_house_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="design_win_not_revenue",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Design win은 Stage 2다. tape-out·양산·매출·마진 전 Green이 아니다.",
    ),
    Round258CaseCandidate(
        case_id="r2_loop12_lg_innotek_apple_ai_aeva_lidar",
        symbol="011070",
        company_name="LG Innotek",
        primary_archetype=E2RArchetype.AI_DEVICE_COMPONENT_OPTIONALITY,
        secondary_archetypes=(E2RArchetype.CAMERA_LIDAR_ADAS_ELECTRONICS, E2RArchetype.EVENT_PREMIUM, E2RArchetype.PRICE_MOVED_WITHOUT_EVIDENCE),
        case_type="success_candidate",
        round_case_type="success_candidate + event_premium",
        stage1_date=date(2024, 6, 12),
        stage2_date=date(2024, 6, 12),
        stage3_date=None,
        stage4b_date=date(2024, 6, 12),
        stage4c_date=None,
        stage3_decision="apple_ai_replacement_cycle_and_lidar_partnership_are_stage2_optionality_until_actual_volume_asp_module_margin_lidar_ramp_and_fcf_confirm",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("apple_ai_replacement_cycle", "op_growth_projection_2024_33pct", "aeva_strategic_collaboration_50mn_usd", "lg_innotek_equity_investment_32mn_usd"),
        red_flag_fields=("apple_replacement_cycle_only", "lidar_optionality_without_volume", "single_customer_concentration", "module_margin_unknown"),
        price_data_source="WSJ Apple-AI event anchor / Reuters Aeva deal anchor",
        reported_price_anchor="Apple AI event up to +19%; KOSPI +0.4%",
        reported_return_anchor="Aeva $50M strategic collaboration including $32M LG Innotek equity investment",
        mfe_1d=19.0,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"apple_ai_event_mfe_pct": 19.0, "kospi_same_context_pct": 0.4, "relative_outperformance_pp": 18.6, "op_growth_projection_2024_pct": 33.0, "aeva_total_deal_usd_mn": 50.0, "lg_innotek_equity_investment_usd_mn": 32.0, "aeva_stake": "single_digit_percentage", "remaining_capacity_amount_usd_mn": 18.0, "target_applications": "vehicles|industrial equipment|robotics|consumer electronics|AR headsets"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="success_candidate_event_premium",
        rerating_result="event_premium",
        round_rerating_label="AI_device_component_optionality_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_optionality_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Apple AI와 lidar optionality는 Stage 2다. 실제 물량·ASP·module margin·FCF가 필요하다.",
    ),
    Round258CaseCandidate(
        case_id="r2_loop12_lg_display_lcd_exit_oled_turnaround",
        symbol="034220",
        company_name="LG Display",
        primary_archetype=E2RArchetype.DISPLAY_LCD_EXIT_OLED_TURNAROUND,
        secondary_archetypes=(E2RArchetype.DISPLAY_OLED_SUPPLYCHAIN, E2RArchetype.STAGE2_EVIDENCE_NOT_GREEN),
        case_type="success_candidate",
        round_case_type="success_candidate + evidence_incomplete",
        stage1_date=date(2024, 4, 1),
        stage2_date=date(2024, 7, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="lcd_exit_and_loss_narrowing_are_stage2_but_sustained_oled_profit_fcf_customer_mix_and_debt_reduction_required_before_green",
        stage4b_status="4B-watch-if-lcd-exit-oled-turnaround-rallies",
        hard_4c_confirmed=False,
        evidence_fields=("q2_operating_loss_94bn_krw", "loss_better_than_expected", "revenue_growth_42pct", "guangzhou_lcd_sale_1_54bn_usd", "oled_focus"),
        red_flag_fields=("lcd_exit_without_oled_profit", "cash_burn_risk", "apple_concentration", "panel_price_decline"),
        price_data_source="Reuters earnings / LCD plant sale anchors",
        reported_price_anchor="Full adjusted OHLC unavailable in this pass",
        reported_return_anchor="Q2 loss 94B KRW vs expected 308B; Guangzhou LCD sale $1.54B",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"q2_operating_loss_krw_bn": 94.0, "expected_q2_loss_krw_bn": 308.0, "loss_surprise_vs_expected_pct": 69.5, "prior_year_q2_loss_krw_bn": 881.0, "loss_reduction_vs_prior_year_pct": 89.3, "q2_revenue_krw_trn": 6.7, "revenue_growth_pct": 42.0, "q2_op_margin_pct": -1.4, "guangzhou_lcd_sale_yuan_bn": 10.8, "guangzhou_lcd_sale_usd_bn": 1.54, "stake_sold": "80% large LCD panel plant|100% LCD module plant"},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_but_evidence_incomplete",
        rerating_result="unknown",
        round_rerating_label="LCD_exit_OLED_turnaround_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="restructuring_stage2_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="적자 축소와 LCD exit는 Stage 2다. 지속 OLED 이익·FCF·부채 감소 전 Green은 보류다.",
    ),
    Round258CaseCandidate(
        case_id="r2_loop12_jusung_mirae_cxmt_relief_watch",
        symbol="036930/025560",
        company_name="Jusung Engineering / Mirae Corp",
        primary_archetype=E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF,
        secondary_archetypes=(E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="event_premium",
        round_case_type="event_premium + 4C-watch",
        stage1_date=date(2024, 11, 1),
        stage2_date=date(2024, 12, 3),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 3),
        stage3_decision="cxmt_exclusion_relief_is_stage2_event_not_green_without_non_china_diversification_order_durability_margin_and_export_control_durability",
        stage4b_status="4B-watch-if-CXMT-relief-rally",
        hard_4c_confirmed=False,
        evidence_fields=("cxmt_excluded_from_entity_list", "jusung_relief_mfe_7_7pct", "mirae_cxmt_revenue_share_15pct", "mirae_cxmt_supply_deals_9bn_krw", "china_equipment_imports_24_12bn_usd"),
        red_flag_fields=("china_customer_concentration", "export_control_uncertainty", "relief_event_not_green", "match_act_restriction_risk"),
        price_data_source="Reuters CXMT exclusion / equipment supplier anchor",
        reported_price_anchor="Jusung nearly -7% then +7.7%; Mirae +1.4% relief",
        reported_return_anchor="Mirae 1H revenue about 15% from CXMT; about 9B KRW CXMT supply deals",
        mfe_1d=7.7,
        mae_1d=-7.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"jusung_previous_session_mae_pct": -7.0, "jusung_relief_mfe_pct": 7.7, "mirae_relief_mfe_pct": 1.4, "mirae_previous_session_mfe_pct": 7.0, "mirae_cxmt_revenue_share_1h2024_pct": 15.0, "mirae_cxmt_supply_deals_krw_bn": 9.0, "mirae_cxmt_supply_deals_usd_mn": 6.41, "china_equipment_imports_9m2024_usd_bn": 24.12, "china_equipment_import_growth_pct": 33.0, "expected_china_chip_capex_drop_usd_bn": 10.0, "expected_china_chip_capex_drop_pct": 30.0},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4C_watch",
        rerating_result="event_premium",
        round_rerating_label="China_equipment_relief_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="relief_stage2_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="CXMT relief는 Green이 아니라 export-control relief다. 중국 고객 집중과 재규제 리스크가 남는다.",
    ),
    Round258CaseCandidate(
        case_id="r2_loop12_export_control_overlay_samsung_skh_hana_hanmi",
        symbol="005930/000660/067310/042700",
        company_name="Samsung / SK Hynix / Hana Micron / Hanmi export-control basket",
        primary_archetype=E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY,
        secondary_archetypes=(E2RArchetype.THESIS_BREAK_4C_WATCH, E2RArchetype.SEMICONDUCTOR_IP_LEAK_REDTEAM),
        case_type="failed_rerating",
        round_case_type="4C-watch",
        stage1_date=date(2025, 8, 29),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 1),
        stage3_decision="export_control_shock_is_redteam_overlay_not_positive_evidence_and_hard_4c_requires_confirmed_license_denial_or_revenue_technology_impairment",
        stage4b_status="not_applicable_4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("us_revokes_veu_authorizations", "samsung_mae_2_3pct", "sk_hynix_mae_4_4pct", "hana_micron_mae_1_7pct", "hanmi_mae_4_4pct", "match_act_targets_cxmt_ymtc_smic"),
        red_flag_fields=("china_fab_export_control_disruption", "equipment_authorization_loss", "license_denial_watch", "technology_upgrade_block_watch", "hard_4c_not_confirmed_yet"),
        price_data_source="Reuters export-control / MATCH Act anchors",
        reported_price_anchor="Samsung -2.3%, SK Hynix -4.4%, Hana Micron -1.7%, Hanmi -4.4%",
        reported_return_anchor="VEU revocation; Samsung China DRAM > one-third; SK Hynix China DRAM/NAND 30-40%",
        mfe_1d=None,
        mae_1d=-4.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_event_mae_pct": -2.3, "sk_hynix_event_mae_pct": -4.4, "hana_micron_event_mae_pct": -1.7, "hanmi_event_mae_pct": -4.4, "kospi_same_context_pct": -0.7, "samsung_relative_underperformance_pp": -1.6, "sk_hynix_relative_underperformance_pp": -3.7, "hanmi_relative_underperformance_pp": -3.7, "samsung_china_dram_exposure": "more_than_one_third", "sk_hynix_china_dram_nand_exposure_pct": "30-40", "veu_revocation_effective_delay_days": 120, "license_policy": "existing operations likely allowed; expansion/upgrade not intended", "match_act_targets": "CXMT|YMTC|SMIC|DUV immersion machines|foreign equipment servicing alignment", "hard_4c_status": "not_confirmed"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="export_control_overlay_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4C_watch_not_hard_4C",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="수출통제는 긍정 후보가 아니라 4C-watch overlay다. license denial이나 매출/기술 훼손 확인 전 hard 4C는 아니다.",
    ),
)


def round258_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("hbm", "euv", "packaging", "eps", "fcf", "capacity", "order", "revenue", "margin", "shipment", "mass_production")
    for candidate in ROUND258_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND258_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round258 R2 Loop-12 AI/semiconductor/electronics price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "4b" in field.lower()
                or "mfe" in field.lower()
                or "milestone" in field.lower()
                or "rumor" in field.lower()
                or "rally" in field.lower()
                or "optionality" in field.lower()
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "export" in field.lower()
                or "labor" in field.lower()
                or "strike" in field.lower()
                or "china" in field.lower()
                or "license" in field.lower()
                or "authorization" in field.lower()
                or "customer_concentration" in field.lower()
                or "risk" in field.lower()
            ),
            must_have_fields=ROUND258_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND258_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_margins_or_fcf",
                "do_not_treat_ai_keyword_design_win_rumor_optionality_or_relief_as_green",
                *ROUND258_GREEN_REQUIRED_FIELDS,
                *ROUND258_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                mfe_30d=candidate.mfe_1d,
                mae_30d=candidate.mae_1d,
                price_validation_status=candidate.price_validation_status,
            ),
            data_quality=CaseDataQuality(
                official_data_available=True,
                report_data_available=True,
                price_data_available=candidate.stage2_price_anchor is not None
                or candidate.stage3_price_anchor is not None
                or candidate.stage4b_price_anchor is not None
                or candidate.stage4c_price_anchor is not None
                or candidate.mfe_1d is not None
                or candidate.mae_1d is not None,
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage3_date or candidate.stage4c_date else 0.7,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round258_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND258_CASE_CANDIDATES:
        rows.append(
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
                "mfe_1d": _float_text(candidate.mfe_1d),
                "mae_1d": _float_text(candidate.mae_1d),
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
                "stage3_price_anchor": _float_text(candidate.stage3_price_anchor),
                "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
                "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
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
        )
    return tuple(rows)


def round258_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND258_SCORE_ADJUSTMENTS)


def round258_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND258_SHADOW_WEIGHT_ROWS)


def round258_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND258_DEEP_SUB_ARCHETYPES)


def round258_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round258_price_validation": "true"} for field in ROUND258_PRICE_VALIDATION_FIELDS)


def round258_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round258_label": label, "canonical_archetype": canonical} for label, canonical in ROUND258_REQUIRED_TARGET_ALIASES.items())


def round258_summary() -> dict[str, int | bool | str]:
    cases = ROUND258_CASE_CANDIDATES
    return {
        "source_round": ROUND258_SOURCE_ROUND_PATH,
        "round_id": ROUND258_ROUND_ID,
        "large_sector": ROUND258_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B" in case.stage4b_status),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "price_data_unavailable_count": sum(1 for case in cases if case.price_validation_status == "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND258_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND258_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND258_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": False,
    }


def round258_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND258_SOURCE_ROUND_PATH,
        "round_id": ROUND258_ROUND_ID,
        "large_sector": ROUND258_LARGE_SECTOR,
        "summary": round258_summary(),
        "target_aliases": dict(ROUND258_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND258_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND258_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND258_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND258_HARD_4C_GATES),
        "deep_sub_archetypes": round258_deep_sub_archetype_rows(),
        "shadow_weights": round258_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round258_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_ai_keyword_design_win_rumor_optionality_or_relief_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "do_not_call_4c_hard_without_license_denial_revenue_or_technology_impairment",
        ],
    }


def render_round258_summary_markdown() -> str:
    summary = round258_summary()
    lines = [
        "# Round 258 R2 Loop 12 AI Semiconductor Electronics Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- structural_success: {summary['structural_success_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- 4B-watch cases: {summary['stage4b_watch_count']}",
        f"- price_moved_without_evidence: {summary['price_moved_without_evidence_count']}",
        f"- evidence_good_but_price_failed: {summary['evidence_good_but_price_failed_count']}",
        f"- price_data_unavailable: {summary['price_data_unavailable_count']}",
        f"- target_archetype_count: {summary['target_archetype_count']}",
        f"- shadow_weight_row_count: {summary['shadow_weight_row_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND258_CASE_CANDIDATES:
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
            "- R2 Stage 3 is not `AI semiconductor beneficiary`. It needs confirmed customer order, generation transition, capacity bottleneck, shipment/revenue, margin, EPS/FCF revision, and post-evidence price path.",
            "- SK Hynix remains the structural success benchmark, but current state is 4B-watch after massive reported return and market-cap milestone.",
            "- Samsung, Hanmi, Gaonchips, LG Innotek, and LG Display show why catch-up, rumor, design win, optionality, and restructuring must stay Stage 2 until revenue/margin/FCF gates close.",
            "- Export-control and labor disruption are 4C-watch overlays; this round does not force hard 4C without license denial, production halt, revenue impairment, or technology impairment.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round258_green_gate_review_markdown() -> str:
    lines = [
        "# Round 258 R2 Loop 12 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND258_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND258_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `SK Hynix HBM sold-out + record OP + EUV order` can support Stage 3; after a very large return it still needs 4B-watch.",
            "- `Hanmi confirmed SK Hynix order` can support Stage 2; `Micron unconfirmed report +22%` is 4B-watch.",
            "- `Gaonchips design win`, `LG Innotek Apple AI`, and `LG Display LCD sale` are not Green until revenue, margin, and FCF are visible.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round258_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 258 R2 Loop 12 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND258_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND258_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B means AI/HBM/component price has run ahead of customer order, shipment, margin, revision, or risk clearance.",
            "- 4C-watch means labor, China fab, license, customer, or export-control risk is serious but not yet a confirmed hard thesis break.",
            "- Hard 4C needs confirmed license denial, production halt, order push-out, revenue impairment, margin collapse, or technology impairment.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND258_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.stage4c_date:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round258_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 258 R2 Loop 12 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND258_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round258_r2_loop12_reports(
    output_directory: str | Path = ROUND258_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND258_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND258_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round258_case_records(), cases_path),
        "audit": _write_json(round258_audit_payload(), audit_path),
        "summary": output / "round258_r2_loop12_price_validation_summary.md",
        "case_matrix": output / "round258_r2_loop12_case_matrix.csv",
        "target_aliases": output / "round258_r2_loop12_target_aliases.csv",
        "score_adjustments": output / "round258_r2_loop12_score_adjustments.csv",
        "shadow_weights": output / "round258_r2_loop12_shadow_weights.csv",
        "deep_sub_archetypes": output / "round258_r2_loop12_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round258_r2_loop12_price_validation_fields.csv",
        "green_gate_review": output / "round258_r2_loop12_green_gate_review.md",
        "price_validation_plan": output / "round258_r2_loop12_price_validation_plan.md",
        "stage4b_4c_review": output / "round258_r2_loop12_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round258_summary_markdown(), encoding="utf-8")
    _write_csv(round258_case_rows(), paths["case_matrix"])
    _write_csv(round258_target_alias_rows(), paths["target_aliases"])
    _write_csv(round258_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round258_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round258_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round258_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round258_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round258_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round258_stage4b_4c_review_markdown(), encoding="utf-8")
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
    return f"{value:+d}" if isinstance(value, int) else str(value)
