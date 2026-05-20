"""Round-245 R2 Loop-11 AI/semiconductor price-validation pack.

This module converts ``docs/round/round_245.md`` into calibration-only
case-library records and reports. It intentionally leaves production scoring,
candidate generation, and StageClassifier thresholds unchanged.

Easy example: SK Hynix can remain a structural HBM success benchmark, but after
large multi-year returns it also becomes 4B-watch. Hanmi's confirmed SK Hynix
order is Stage 2 evidence, while an unconfirmed Micron rumor is 4B-watch rather
than Stage 3-Green evidence.
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


ROUND245_SOURCE_ROUND_PATH = "docs/round/round_245.md"
ROUND245_ROUND_ID = "round_173"
ROUND245_LARGE_SECTOR = Round10LargeSector.AI_SEMICONDUCTOR_ELECTRONICS.value
ROUND245_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round245_r2_loop11_ai_semiconductor_price_validation"
ROUND245_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop11_round245.jsonl"
ROUND245_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round245_r2_loop11_ai_semiconductor_price_validation_audit.json"

ROUND245_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "MEMORY_HBM_CAPACITY_LEADER": E2RArchetype.MEMORY_HBM_CAPACITY_LEADER.value,
    "HBM_EUV_ADVANCED_PACKAGING_CAPEX": E2RArchetype.HBM_EUV_ADVANCED_PACKAGING_CAPEX.value,
    "HBM_CATCHUP_EXECUTION": E2RArchetype.HBM_CATCHUP_EXECUTION.value,
    "FOUNDRY_TURNAROUND_CONTRACT": E2RArchetype.FOUNDRY_TURNAROUND_CONTRACT.value,
    "HBM_BONDER_EQUIPMENT": E2RArchetype.HBM_BONDER_EQUIPMENT.value,
    "CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF": E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF.value,
    "SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER": E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER.value,
    "POLICY_FOUNDRY_EVENT": E2RArchetype.POLICY_FOUNDRY_EVENT.value,
    "SEMICONDUCTOR_EQUIPMENT_SPINOFF_OPTIONALITY": E2RArchetype.SEMICONDUCTOR_EQUIPMENT_SPINOFF_OPTIONALITY.value,
    "GEOPOLITICAL_EXPORT_CONTROL_OVERLAY": E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY.value,
    "SEMICONDUCTOR_IP_LEAK_REDTEAM": E2RArchetype.SEMICONDUCTOR_IP_LEAK_REDTEAM.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
}

ROUND245_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "company_level_customer_evidence",
    "product_specific_exposure",
    "order_shipment_contract_revenue_path",
    "gross_margin_or_opm_improvement",
    "eps_fcf_revision",
    "capacity_bottleneck_or_supply_allocation",
    "customer_diversification",
    "export_control_china_fab_labor_ip_accounting_passed",
    "price_path_after_evidence",
)

ROUND245_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ai_keyword_only",
    "hbm_rumor_only",
    "unconfirmed_customer_report",
    "design_win_without_revenue",
    "policy_foundry_without_order",
    "spin_off_or_corporate_action_only",
    "china_customer_concentration_only",
    "labor_export_control_or_ip_risk_ignored",
    "price_rally_before_confirmation",
)

ROUND245_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "stage3_after_3x_plus",
    "market_cap_milestone_headline",
    "unconfirmed_customer_diversification_report_plus_20pct",
    "spin_off_corporate_action_priced_before_revenue",
    "ai_capex_consensus_crowded",
    "good_news_price_response_deteriorates",
    "negative_event_sensitivity_rises",
)

ROUND245_HARD_4C_GATES: tuple[str, ...] = (
    "hbm_qualification_failure",
    "order_push_out",
    "customer_capex_cut",
    "memory_price_decline",
    "hbm_supply_normalization",
    "china_fab_export_control_disruption",
    "equipment_authorization_loss",
    "labor_strike_production_halt",
    "ip_leakage_china_competitive_catchup",
    "accounting_or_disclosure_trust_break",
    "customer_concentration_failure",
)

ROUND245_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "export_control_anchor",
    "ip_leak_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round245ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round245ShadowWeightRow:
    archetype: E2RArchetype
    confirmed_order: int
    hbm_transition: int
    capacity_bottleneck: int
    euv_packaging: int
    product_specificity: int
    order_to_revenue: int
    margin_visibility: int
    customer_diversification: int
    price_path_alignment: int
    event_penalty: int
    china_export_ip_redteam: int
    stage4b_watch_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "confirmed_order": _signed(self.confirmed_order),
            "hbm_transition": _signed(self.hbm_transition),
            "capacity_bottleneck": _signed(self.capacity_bottleneck),
            "euv_packaging": _signed(self.euv_packaging),
            "product_specificity": _signed(self.product_specificity),
            "order_to_revenue": _signed(self.order_to_revenue),
            "margin_visibility": _signed(self.margin_visibility),
            "customer_diversification": _signed(self.customer_diversification),
            "price_path_alignment": _signed(self.price_path_alignment),
            "event_penalty": _signed(self.event_penalty),
            "china_export_ip_redteam": _signed(self.china_export_ip_redteam),
            "4b_watch_sensitivity": _signed(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round245DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {
            "category": self.category,
            "primary_archetype": self.primary_archetype.value,
            "terms": "|".join(self.terms),
        }


@dataclass(frozen=True)
class Round245CaseCandidate:
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
    extra_price_metrics: Mapping[str, float | int | str | bool | list[str]]
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


ROUND245_SCORE_ADJUSTMENTS: tuple[Round245ScoreAdjustment, ...] = (
    Round245ScoreAdjustment("confirmed_customer_order", 5, "raise", "R2는 고객 주문이 확인될 때만 강하게 본다."),
    Round245ScoreAdjustment("HBM_generation_transition", 5, "raise", "HBM 세대 전환은 EPS/FCF 체급 변화의 핵심 증거다."),
    Round245ScoreAdjustment("capacity_bottleneck", 5, "raise", "CAPA 병목과 allocation은 단순 AI keyword보다 강하다."),
    Round245ScoreAdjustment("EUV_or_advanced_packaging_capacity", 5, "raise", "EUV/advanced packaging 투자가 HBM 매출로 이어질 때 visibility가 올라간다."),
    Round245ScoreAdjustment("product_specificity", 4, "raise", "HBM4, 2nm GAA, TSV-TC bonder처럼 제품이 구체적이어야 한다."),
    Round245ScoreAdjustment("order_to_revenue_conversion", 5, "raise", "주문이 매출·마진으로 전환되어야 Stage 3 후보가 된다."),
    Round245ScoreAdjustment("gross_margin_visibility", 5, "raise", "장비/파운드리/메모리 모두 마진 가시성이 필요하다."),
    Round245ScoreAdjustment("customer_diversification", 4, "raise", "단일 고객·중국 고객 집중은 Green 전에 확인해야 한다."),
    Round245ScoreAdjustment("price_path_alignment", 5, "raise", "증거 이후 가격경로가 따라오는지 검증한다."),
    Round245ScoreAdjustment("AI_keyword_only", -5, "lower", "AI 이름만 있으면 Stage 1 연구 라우팅 수준이다."),
    Round245ScoreAdjustment("MOU_or_policy_only", -5, "lower", "MoU와 정책 검토는 주문·매출 전 Green이 아니다."),
    Round245ScoreAdjustment("unconfirmed_media_report", -5, "lower", "미확정 고객 보도로 급등하면 4B-watch다."),
    Round245ScoreAdjustment("design_win_without_revenue", -4, "lower", "design win은 양산·매출·마진 전 Stage 2다."),
    Round245ScoreAdjustment("policy_foundry_without_order", -5, "lower", "정책 foundry는 회사 단위 order 전 event premium이다."),
    Round245ScoreAdjustment("corporate_action_without_order", -4, "lower", "spin-off optionality는 order/revenue 전 Green이 아니다."),
    Round245ScoreAdjustment("China_customer_dependency", -5, "lower", "중국 고객 집중은 export-control RedTeam을 키운다."),
    Round245ScoreAdjustment("export_control_exposure", -5, "lower", "중국 fab 장비허가 리스크는 4C-watch다."),
    Round245ScoreAdjustment("IP_leak_risk", -5, "lower", "기술유출은 moat와 trust를 훼손할 수 있다."),
    Round245ScoreAdjustment("labor_disruption_risk", -5, "lower", "파업·생산중단은 HBM/foundry 실행 신뢰도를 낮춘다."),
    Round245ScoreAdjustment("price_rally_before_confirmation", -5, "lower", "확인 전 가격만 먼저 움직이면 4B-watch다."),
)

ROUND245_SHADOW_WEIGHT_ROWS: tuple[Round245ShadowWeightRow, ...] = (
    Round245ShadowWeightRow(E2RArchetype.MEMORY_HBM_CAPACITY_LEADER, 5, 5, 5, 5, 5, 5, 5, 4, 5, -1, 4, 5, 4, "SK Hynix is aligned Stage 3 but now requires 4B-watch."),
    Round245ShadowWeightRow(E2RArchetype.HBM_CATCHUP_EXECUTION, 4, 4, 4, 3, 4, 4, 5, 3, 3, -2, 5, 4, 4, "Samsung is Stage 2 until HBM/foundry volume, margin and labor/export risks clear."),
    Round245ShadowWeightRow(E2RArchetype.FOUNDRY_TURNAROUND_CONTRACT, 5, 2, 3, 3, 4, 4, 5, 3, 3, -3, 4, 4, 4, "$16.5B contract helps Samsung but yield/margin/revenue bridge must confirm."),
    Round245ShadowWeightRow(E2RArchetype.HBM_BONDER_EQUIPMENT, 5, 5, 5, 3, 5, 5, 5, 4, 4, -3, 3, 5, 3, "Hanmi confirmed order is good; unconfirmed Micron rumor is 4B risk."),
    Round245ShadowWeightRow(E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF, 3, 2, 3, 2, 4, 4, 4, 2, 2, -4, 5, 5, 4, "Jusung/Mirae CXMT relief is event, not Green; customer concentration matters."),
    Round245ShadowWeightRow(E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER, 2, 1, 2, 2, 5, 4, 4, 3, 2, -4, 2, 3, 3, "Gaonchips design win needs tape-out, production and revenue."),
    Round245ShadowWeightRow(E2RArchetype.POLICY_FOUNDRY_EVENT, 1, 0, 2, 1, 2, 1, 2, 1, 1, -5, 2, 4, 3, "Policy foundry consultation is not company Green."),
    Round245ShadowWeightRow(E2RArchetype.SEMICONDUCTOR_EQUIPMENT_SPINOFF_OPTIONALITY, 2, 2, 2, 2, 3, 2, 3, 2, 2, -5, 2, 5, 3, "Spin-off optionality requires order book and revenue conversion."),
    Round245ShadowWeightRow(E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 5, 3, 5, "China fab authorization loss and IP leak are 4C-watch until production/revenue impact confirms."),
)

ROUND245_DEEP_SUB_ARCHETYPES: tuple[Round245DeepSubArchetype, ...] = (
    Round245DeepSubArchetype("HBM leader", E2RArchetype.MEMORY_HBM_CAPACITY_LEADER, ("SK Hynix", "HBM", "advanced DRAM", "ASML EUV", "advanced packaging", "4B crowding")),
    Round245DeepSubArchetype("Samsung catch-up", E2RArchetype.HBM_CATCHUP_EXECUTION, ("Samsung Electronics", "HBM4", "AMD MoU", "foundry contract", "strike", "China fab")),
    Round245DeepSubArchetype("Foundry turnaround", E2RArchetype.FOUNDRY_TURNAROUND_CONTRACT, ("$16.5B contract", "through 2033", "yield margin utilization required")),
    Round245DeepSubArchetype("HBM bonder equipment", E2RArchetype.HBM_BONDER_EQUIPMENT, ("Hanmi Semiconductor", "TSV-TC bonder", "SK Hynix contract", "Micron unconfirmed report")),
    Round245DeepSubArchetype("China/CXMT equipment suppliers", E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF, ("Jusung Engineering", "Mirae Corp", "CXMT exclusion relief", "export-control uncertainty")),
    Round245DeepSubArchetype("Design house", E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER, ("Gaonchips", "Preferred Networks", "Samsung 2nm GAA", "advanced packaging")),
    Round245DeepSubArchetype("Policy foundry", E2RArchetype.POLICY_FOUNDRY_EVENT, ("DB HiTek", "40nm", "12-inch", "defense semiconductor localization", "consultation target")),
    Round245DeepSubArchetype("Equipment spin-off", E2RArchetype.SEMICONDUCTOR_EQUIPMENT_SPINOFF_OPTIONALITY, ("Hanwha Precision Machinery", "Hanwha Aerospace", "HBM equipment optionality", "spin-off")),
    Round245DeepSubArchetype("RedTeam", E2RArchetype.SEMICONDUCTOR_IP_LEAK_REDTEAM, ("export-control", "China fab authorization", "Samsung DRAM IP leak", "CXMT", "labor disruption")),
)


ROUND245_CASE_CANDIDATES: tuple[Round245CaseCandidate, ...] = (
    Round245CaseCandidate(
        case_id="r2_loop11_sk_hynix_euv_packaging_4b",
        symbol="000660",
        company_name="SK Hynix",
        primary_archetype=E2RArchetype.MEMORY_HBM_CAPACITY_LEADER,
        secondary_archetypes=(E2RArchetype.HBM_EUV_ADVANCED_PACKAGING_CAPEX, E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.STRUCTURAL_SUCCESS_BUT_4B_WATCH),
        case_type="structural_success",
        round_case_type="structural_success + 4B-watch",
        stage1_date=None,
        stage2_date=date(2024, 6, 25),
        stage3_date=date(2024, 6, 25),
        stage4b_date=date(2026, 5, 14),
        stage4c_date=None,
        stage3_decision="hbm_leadership_euv_and_advanced_packaging_validate_structural_success_but_large_mfe_requires_4b_watch",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("hbm_dominance", "dram_price_upcycle", "eps_revision", "stage3_candidate_anchor_222000", "asml_euv_order_11_95tn_krw", "advanced_packaging_plant_19tn_krw", "reported_return_2025_274pct", "market_cap_near_942bn_usd"),
        red_flag_fields=("stage3_after_3x_plus", "market_cap_milestone_headline", "ai_memory_consensus_crowded"),
        price_data_source="MarketWatch / Reuters reported price and return anchors",
        reported_price_anchor="stage3 candidate anchor 222,000 KRW; market cap from below $100B to about $942B",
        reported_return_anchor="ASML EUV order +5.7%; 2025 +274%; 2026 YTD > +200%",
        mfe_1d=5.7,
        mae_1d=None,
        stage2_price_anchor=222000.0,
        stage3_price_anchor=222000.0,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"asml_euv_order_krw_trn": 11.95, "asml_euv_order_usd_bn": 7.97, "asml_euv_event_mfe_pct": 5.7, "estimated_euv_tools": 30, "advanced_packaging_investment_krw_trn": 19.0, "advanced_packaging_investment_usd_bn": 12.85, "reported_return_2025_pct": 274.0, "reported_return_2026_ytd_min_pct": 200.0, "minimum_compounded_return_from_2025_start_pct": 1022.0, "market_cap_mfe_minimum_pct": 842.0},
        score_price_alignment="aligned",
        round_alignment_label="aligned_now_4B_watch",
        rerating_result="true_rerating",
        round_rerating_label="true_rerating_now_4B_watch",
        stage_failure_type="green_success",
        round_stage_failure_label="green_success_now_4B_watch",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="HBM/EUV/advanced packaging confirms structural success; current state is 4B-watch after massive reported MFE.",
    ),
    Round245CaseCandidate(
        case_id="r2_loop11_samsung_hbm_foundry_strike_export_ip_watch",
        symbol="005930",
        company_name="Samsung Electronics",
        primary_archetype=E2RArchetype.HBM_CATCHUP_EXECUTION,
        secondary_archetypes=(E2RArchetype.FOUNDRY_TURNAROUND_CONTRACT, E2RArchetype.SEMICONDUCTOR_IP_LEAK_REDTEAM, E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate + 4C-watch",
        stage1_date=None,
        stage2_date=date(2025, 7, 28),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 1),
        stage3_decision="stage2_hbm_foundry_catchup_until_volume_shipment_margin_eps_revision_and_risks_clear",
        stage4b_status="4B-watch-if-catchup-rerates-before-volume",
        hard_4c_confirmed=False,
        evidence_fields=("foundry_contract_16_5bn_usd", "foundry_contract_event_return_3_5pct", "contract_through_end_2033", "amd_mou_hbm4_ddr5_foundry", "samsung_hbm_share_22pct", "sk_hynix_hbm_share_57pct"),
        red_flag_fields=("strike_event_mae_minus_9_3pct", "china_fab_export_control", "samsung_china_dram_more_than_one_third", "ip_leak_watch", "volume_margin_eps_unconfirmed"),
        price_data_source="Reuters reported contract / event-return / strike-risk anchors",
        reported_price_anchor="foundry contract +3.5%; strike risk -9.3%; court relief +3.88%; export control -2.3%",
        reported_return_anchor="$16.5B foundry contract through end-2033; AMD HBM4/DDR5 MoU",
        mfe_1d=3.5,
        mae_1d=-9.3,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"foundry_contract_usd_bn": 16.5, "foundry_contract_event_return_pct": 3.5, "foundry_contract_end_year": 2033, "samsung_hbm_market_share_pct": 22.0, "sk_hynix_hbm_market_share_pct": 57.0, "export_control_event_mae_pct": -2.3, "strike_event_mae_pct": -9.3, "court_ruling_relief_return_pct": 3.88, "kospi_same_context_may18_pct": 0.31, "relative_outperformance_may18_pp": 3.57, "possible_strike_workers": 45000, "possible_direct_loss_per_day_krw_trn": 1.0},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="success_candidate_4c_watch",
        rerating_result="unknown",
        round_rerating_label="HBM_catchup_foundry_turnaround_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_until_volume_margin_confirm",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Samsung has Stage 2 foundry/HBM evidence, but volume/margin/EPS plus labor/export/IP risks must clear before Green.",
    ),
    Round245CaseCandidate(
        case_id="r2_loop11_hanmi_hbm_bonder_confirmed_order_rumor_4b",
        symbol="042700",
        company_name="Hanmi Semiconductor",
        primary_archetype=E2RArchetype.HBM_BONDER_EQUIPMENT,
        secondary_archetypes=(E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA, E2RArchetype.PRICE_ONLY_RALLY, E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate + 4B-watch",
        stage1_date=None,
        stage2_date=date(2024, 3, 1),
        stage3_date=None,
        stage4b_date=date(2024, 3, 28),
        stage4c_date=None,
        stage3_decision="confirmed_sk_hynix_order_supports_stage2_but_order_to_revenue_margin_and_eps_revision_required_before_green",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("tsv_tc_bonder", "confirmed_sk_hynix_contract_21_48bn_krw", "recent_deals_total_200bn_krw", "hbm_packaging_equipment"),
        red_flag_fields=("micron_unconfirmed_media_report", "stage4b_event_mfe_22pct", "customer_concentration", "export_control_event_mae_minus_4_4pct"),
        price_data_source="WSJ reported price and contract anchors",
        reported_price_anchor="Micron unconfirmed report +22% intraday to 139,100 KRW",
        reported_return_anchor="SK Hynix contract 21.48B KRW; recent deals about 200B KRW",
        mfe_1d=22.0,
        mae_1d=-4.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=139100.0,
        stage4c_price_anchor=None,
        extra_price_metrics={"confirmed_sk_hynix_contract_krw_bn": 21.48, "recent_deals_total_krw_bn": 200.0, "stage4b_peak_price_krw": 139100.0, "stage4b_event_mfe_pct": 22.0, "implied_pre_4b_reference_price_krw": 114016.0, "kospi_same_context_pct": -0.3, "relative_outperformance_pp": 22.3, "export_control_event_mae_pct": -4.4, "micron_deal_status": "unconfirmed_media_report"},
        score_price_alignment="aligned",
        round_alignment_label="aligned_candidate_4B_watch",
        rerating_result="unknown",
        round_rerating_label="HBM_equipment_rerating_candidate",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="confirmed_order_good_but_unconfirmed_customer_rumor_4B",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Confirmed SK Hynix order is good Stage 2 evidence; unconfirmed Micron media report is 4B-watch.",
    ),
    Round245CaseCandidate(
        case_id="r2_loop11_jusung_mirae_cxmt_supplier_relief",
        symbol="036930/025560",
        company_name="Jusung Engineering / Mirae Corp",
        primary_archetype=E2RArchetype.CHINA_CXMT_EQUIPMENT_SUPPLIER_RELIEF,
        secondary_archetypes=(E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, E2RArchetype.PRICE_ONLY_RALLY),
        case_type="event_premium",
        round_case_type="event_premium + 4C-watch",
        stage1_date=None,
        stage2_date=date(2024, 12, 3),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2024, 12, 3),
        stage3_decision="cxmt_exclusion_relief_is_stage2_event_not_green_without_non_china_diversification_revenue_margin_and_authorization_durability",
        stage4b_status="4B-watch-if-relief-rally",
        hard_4c_confirmed=False,
        evidence_fields=("cxmt_excluded_from_entity_list", "jusung_relief_mfe_7_7pct", "mirae_cxmt_revenue_share_15pct", "mirae_cxmt_supply_deals_9bn_krw", "china_equipment_imports_24_12bn_usd"),
        red_flag_fields=("china_customer_concentration", "export_control_uncertainty", "relief_event_not_order", "next_export_control_wave"),
        price_data_source="Reuters China export-control / CXMT relief anchor",
        reported_price_anchor="Jusung nearly -7% then +7.7%; Mirae +1.4% relief",
        reported_return_anchor="Mirae 1H2024 CXMT revenue share about 15%; supply deals about 9B KRW",
        mfe_1d=7.7,
        mae_1d=-7.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"jusung_previous_session_mae_pct": -7.0, "jusung_relief_mfe_pct": 7.7, "mirae_relief_mfe_pct": 1.4, "mirae_previous_session_gain_pct": 7.0, "mirae_cxmt_revenue_share_1h2024_pct": 15.0, "mirae_cxmt_supply_deals_krw_bn": 9.0, "mirae_cxmt_supply_deals_usd_mn": 6.41, "china_equipment_imports_9m2024_usd_bn": 24.12, "china_equipment_import_growth_pct": 33.0},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_4C_watch",
        rerating_result="event_premium",
        round_rerating_label="China_equipment_relief_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_relief_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="CXMT exclusion relief is Stage 2 event, not Green; export-control durability and customer diversification are required.",
    ),
    Round245CaseCandidate(
        case_id="r2_loop11_gaonchips_pfn_design_win",
        symbol="399720",
        company_name="Gaonchips",
        primary_archetype=E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER,
        secondary_archetypes=(E2RArchetype.STAGE2_EVIDENCE_NOT_GREEN,),
        case_type="success_candidate",
        round_case_type="success_candidate / insufficient_price_data",
        stage1_date=None,
        stage2_date=date(2024, 7, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="design_win_is_stage2_but_tapeout_mass_production_revenue_and_margin_required_before_green",
        stage4b_status="4B-watch-if-design-house-rallies",
        hard_4c_confirmed=False,
        evidence_fields=("preferred_networks_ai_chip_order", "samsung_2nm_gaa", "advanced_packaging", "gaonchips_designed_chips", "generative_ai_llm_hpc_end_use"),
        red_flag_fields=("order_size_not_disclosed", "mass_production_unconfirmed", "revenue_margin_unconfirmed", "tapeout_delay_risk"),
        price_data_source="Reuters evidence source",
        reported_price_anchor="Gaonchips price reaction not available in Reuters anchor",
        reported_return_anchor="Preferred Networks AI chip uses Samsung 2nm GAA and advanced packaging; order size undisclosed",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"order_size": "not_disclosed", "technology": "Samsung 2nm GAA + advanced packaging", "customer": "Preferred Networks", "end_use": "generative AI / LLM high-performance computing hardware"},
        score_price_alignment="unknown",
        round_alignment_label="unknown_insufficient_evidence",
        rerating_result="unknown",
        round_rerating_label="design_win_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_evidence_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Design win is Stage 2; tape-out, mass production, revenue and margin are required for Stage 3.",
    ),
    Round245CaseCandidate(
        case_id="r2_loop11_db_hitek_policy_foundry",
        symbol="000990",
        company_name="DB HiTek / policy foundry exposure",
        primary_archetype=E2RArchetype.POLICY_FOUNDRY_EVENT,
        secondary_archetypes=(E2RArchetype.PRICE_ONLY_RALLY,),
        case_type="event_premium",
        round_case_type="event_premium / policy_watch",
        stage1_date=date(2025, 12, 10),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="public_private_foundry_policy_is_stage1_2_attention_not_company_green_before_funded_capex_customer_order_utilization_and_margin",
        stage4b_status="4B-watch-if-policy-basket-rallies",
        hard_4c_confirmed=False,
        evidence_fields=("public_private_foundry_4_5tn_krw", "12_inch_40nm_facility", "automotive_data_center_legacy_chip", "defense_semiconductor_localization", "defense_import_dependency_99pct"),
        red_flag_fields=("policy_foundry_without_order", "consultation_target_not_confirmed_order", "customer_absent", "utilization_failure_risk"),
        price_data_source="Reuters policy evidence source",
        reported_price_anchor="DB HiTek price reaction not available in Reuters anchor",
        reported_return_anchor="4.5T KRW / $3.06B public-private foundry under review",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"foundry_project_size_krw_trn": 4.5, "foundry_project_size_usd_bn": 3.06, "process_node_nm": 40, "wafer_size_inch": 12, "defense_semiconductor_import_dependency_pct": 99.0, "company_status": "policy_beneficiary_candidate_not_confirmed_order"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_policy_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="policy_foundry_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="stage1_attention_only",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Government foundry consultation is Stage 1/2, not company Green.",
    ),
    Round245CaseCandidate(
        case_id="r2_loop11_hanwha_precision_hbm_equipment_spinoff",
        symbol="012450_parent_exposure",
        company_name="Hanwha Precision Machinery / Hanwha Aerospace spin-off exposure",
        primary_archetype=E2RArchetype.SEMICONDUCTOR_EQUIPMENT_SPINOFF_OPTIONALITY,
        secondary_archetypes=(E2RArchetype.PRICE_ONLY_RALLY, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium / corporate_action_watch",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 5),
        stage3_date=None,
        stage4b_date=date(2024, 4, 5),
        stage4c_date=None,
        stage3_decision="spin_off_hbm_equipment_optionality_is_not_green_before_order_book_revenue_margin_and_listed_vehicle_economics",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("hanwha_precision_machinery_spinoff", "hbm_equipment_optionality", "industrial_solutions_value_2tn_krw", "defence_business_value_10tn_krw", "spun_units_revenue_contribution_16pct"),
        red_flag_fields=("media_report_event_mfe_above_15pct", "formal_announcement_event_mae_minus_8pct", "corporate_action_without_order", "listed_vehicle_economics_unconfirmed"),
        price_data_source="Reuters corporate-action / event-return anchor",
        reported_price_anchor="media report +15%+; formal announcement -8%",
        reported_return_anchor="industrial solutions value about 2T KRW; defence business value about 10T KRW",
        mfe_1d=15.0,
        mae_1d=-8.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"media_report_event_mfe_pct": 15.0, "formal_announcement_event_mae_pct": -8.0, "industrial_solutions_estimated_value_krw_trn": 2.0, "industrial_solutions_estimated_value_usd_bn": 1.48, "defence_business_estimated_value_krw_trn": 10.0, "revenue_contribution_from_spun_units_pct": 16.0, "parent_market_cap_context_krw_trn": 11.0, "industrial_plus_defence_estimate_krw_trn": 12.0, "estimated_sum_vs_parent_market_cap_pct": 9.1},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium",
        rerating_result="event_premium",
        round_rerating_label="HBM_equipment_corporate_action_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="corporate_action_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="HBM equipment optionality via spin-off is Stage 2/corporate-action event; order/revenue/margin are required before Green.",
    ),
    Round245CaseCandidate(
        case_id="r2_loop11_export_control_ip_leak_redteam",
        symbol="005930/000660/067310/042700",
        company_name="Samsung/SK Hynix/Hana Micron/Hanmi export-control and IP-leak basket",
        primary_archetype=E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY,
        secondary_archetypes=(E2RArchetype.SEMICONDUCTOR_IP_LEAK_REDTEAM, E2RArchetype.THESIS_BREAK_4C_WATCH),
        case_type="failed_rerating",
        round_case_type="4C-watch",
        stage1_date=None,
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 1),
        stage3_decision="negative_redteam_event_not_a_candidate_source_and_hard_4c_requires_confirmed_production_revenue_or_competitive_impairment",
        stage4b_status="not_applicable_4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("us_revokes_china_equipment_authorizations", "samsung_mae_2_3pct", "sk_hynix_mae_4_4pct", "hana_micron_mae_1_7pct", "hanmi_mae_4_4pct", "samsung_dram_ip_leak_charges", "ip_leak_development_cost_1_6tn_krw"),
        red_flag_fields=("china_fab_export_control_disruption", "equipment_authorization_loss", "ip_leakage_china_competitive_catchup", "customer_concentration_failure", "hard_4c_not_confirmed_yet"),
        price_data_source="Reuters export-control and IP-leak anchors",
        reported_price_anchor="Samsung -2.3%, SK Hynix -4.4%, Hana Micron -1.7%, Hanmi -4.4% on authorization revocation",
        reported_return_anchor="Samsung DRAM process leak charges; 1.6T KRW development cost; losses potentially tens of trillions KRW",
        mfe_1d=None,
        mae_1d=-4.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"samsung_mae_1d_pct": -2.3, "sk_hynix_mae_1d_pct": -4.4, "hana_micron_mae_1d_pct": -1.7, "hanmi_mae_1d_pct": -4.4, "kospi_same_context_pct": -0.7, "samsung_relative_underperformance_pp": -1.6, "sk_hynix_relative_underperformance_pp": -3.7, "hanmi_relative_underperformance_pp": -3.7, "samsung_china_dram_exposure": "more_than_one_third", "sk_hynix_china_dram_nand_exposure_pct": "30-40", "authorization_effective_delay_days": 120, "ip_leak_development_cost_krw_trn": 1.6, "estimated_losses": "at_least_tens_of_trillions_of_won"},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="export_control_and_IP_leak_4C_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4C_watch_not_hard_4C",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Export-control and IP leakage are R2 4C-watch; hard 4C requires production/revenue/competitive impairment confirmation.",
    ),
)


def round245_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("hbm", "euv", "packaging", "eps", "fcf", "capacity", "order", "revenue", "margin")
    for candidate in ROUND245_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND245_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round245 R2 Loop-11 AI/semiconductor price validation case. "
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
                or "media_report" in field.lower()
                or "corporate_action" in field.lower()
                or "rally" in field.lower()
            ),
            stage4c_evidence=tuple(
                field
                for field in candidate.red_flag_fields
                if "export" in field.lower()
                or "ip" in field.lower()
                or "labor" in field.lower()
                or "strike" in field.lower()
                or "china" in field.lower()
                or "authorization" in field.lower()
                or "customer_concentration" in field.lower()
                or "risk" in field.lower()
            ),
            must_have_fields=ROUND245_GREEN_REQUIRED_FIELDS,
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
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND245_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_margins_or_fcf",
                "do_not_treat_ai_keyword_mou_policy_design_win_rumor_or_spinoff_as_green",
                *ROUND245_GREEN_REQUIRED_FIELDS,
                *ROUND245_GREEN_FORBIDDEN_PATTERNS,
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


def round245_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND245_CASE_CANDIDATES:
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


def round245_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND245_SCORE_ADJUSTMENTS)


def round245_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND245_SHADOW_WEIGHT_ROWS)


def round245_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND245_DEEP_SUB_ARCHETYPES)


def round245_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round245_price_validation": "true"} for field in ROUND245_PRICE_VALIDATION_FIELDS)


def round245_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round245_label": label, "canonical_archetype": canonical} for label, canonical in ROUND245_REQUIRED_TARGET_ALIASES.items())


def round245_summary() -> dict[str, int | bool | str]:
    cases = ROUND245_CASE_CANDIDATES
    return {
        "source_round": ROUND245_SOURCE_ROUND_PATH,
        "round_id": ROUND245_ROUND_ID,
        "large_sector": ROUND245_LARGE_SECTOR,
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
        "target_archetype_count": len(ROUND245_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND245_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND245_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": False,
    }


def round245_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND245_SOURCE_ROUND_PATH,
        "round_id": ROUND245_ROUND_ID,
        "large_sector": ROUND245_LARGE_SECTOR,
        "summary": round245_summary(),
        "target_aliases": dict(ROUND245_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND245_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND245_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND245_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND245_HARD_4C_GATES),
        "deep_sub_archetypes": round245_deep_sub_archetype_rows(),
        "shadow_weights": round245_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round245_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_ai_keyword_mou_policy_design_win_rumor_or_spinoff_as_green",
            "do_not_invent_ohlc_or_stage_dates",
            "do_not_call_4c_hard_without_production_revenue_or_competitive_impairment",
        ],
    }


def render_round245_summary_markdown() -> str:
    summary = round245_summary()
    lines = [
        "# Round 245 R2 Loop 11 AI Semiconductor Price Validation",
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
        f"- target_archetype_count: {summary['target_archetype_count']}",
        f"- shadow_weight_row_count: {summary['shadow_weight_row_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND245_CASE_CANDIDATES:
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
            "- R2 Stage 3 is not `AI semiconductor beneficiary`. It requires customer order, HBM generation transition, CAPA bottleneck, margin, EPS/FCF revision, and post-evidence price path.",
            "- SK Hynix remains a structural success benchmark, but after very large reported returns it is now 4B-watch.",
            "- Samsung, Hanmi, Gaonchips, and DB HiTek show why confirmed order, design win, MoU, policy, and rumor must be separated.",
            "- Export-control, labor disruption, and IP leakage are strong 4C-watch overlays, but this round does not force hard 4C without production/revenue/competitive impairment proof.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round245_green_gate_review_markdown() -> str:
    lines = [
        "# Round 245 R2 Loop 11 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND245_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND245_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `confirmed SK Hynix order` can support Stage 2 for Hanmi; `unconfirmed Micron rumor +22%` is 4B-watch.",
            "- `Samsung $16.5B foundry contract` is useful Stage 2 evidence; Green waits for volume shipment, yield, margin, and EPS/FCF revision.",
            "- `policy foundry`, `design win`, and `spin-off optionality` are not Green without company-level order, revenue, and margin.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round245_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 245 R2 Loop 11 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND245_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND245_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B means price or event premium has run ahead of confirmed order, revenue, margin, and revision evidence.",
            "- 4C-watch means the thesis has a serious risk overlay, but hard 4C needs confirmed production, revenue, customer, competitive, accounting, or trust damage.",
            "- Price-only or rumor-only moves stay out of Stage 3-Green.",
        ]
    )
    lines.extend(["", "## Case Notes", ""])
    for case in ROUND245_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.stage4c_date:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round245_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 245 R2 Loop 11 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND245_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round245_r2_loop11_reports(
    output_directory: str | Path = ROUND245_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND245_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND245_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round245_case_records(), cases_path),
        "audit": _write_json(round245_audit_payload(), audit_path),
        "summary": output / "round245_r2_loop11_price_validation_summary.md",
        "case_matrix": output / "round245_r2_loop11_case_matrix.csv",
        "target_aliases": output / "round245_r2_loop11_target_aliases.csv",
        "score_adjustments": output / "round245_r2_loop11_score_adjustments.csv",
        "shadow_weights": output / "round245_r2_loop11_shadow_weights.csv",
        "deep_sub_archetypes": output / "round245_r2_loop11_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round245_r2_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round245_r2_loop11_green_gate_review.md",
        "price_validation_plan": output / "round245_r2_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round245_r2_loop11_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round245_summary_markdown(), encoding="utf-8")
    _write_csv(round245_case_rows(), paths["case_matrix"])
    _write_csv(round245_target_alias_rows(), paths["target_aliases"])
    _write_csv(round245_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round245_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round245_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round245_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round245_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round245_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round245_stage4b_4c_review_markdown(), encoding="utf-8")
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
