"""Round-232 R2 Loop-10 AI semiconductor price validation pack.

This pack converts ``docs/round/round_232.md`` into structured,
calibration-only case records. It does not change production scoring.

Easy example: SK Hynix has HBM4, EUV, advanced packaging CAPEX, and price-path
validation, so it is a structural-success anchor that now needs 4B-watch. A
design win or AI headline without shipment, revenue, margin, and EPS/FCF is
only Stage 2/event premium.
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


ROUND232_SOURCE_ROUND_PATH = "docs/round/round_232.md"
ROUND232_LARGE_SECTOR = "AI_SEMICONDUCTOR_ELECTRONICS"
ROUND232_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round232_r2_loop10_ai_semiconductor_price_validation"
ROUND232_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r2_loop10_round232.jsonl"
ROUND232_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round232_r2_loop10_ai_semiconductor_price_validation_audit.json"

ROUND232_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "MEMORY_HBM_CAPACITY": E2RArchetype.MEMORY_HBM_CAPACITY.value,
    "MEMORY_HBM4_FIRST_MOVER": E2RArchetype.MEMORY_HBM4_FIRST_MOVER.value,
    "HBM_CAPEX_CAPACITY_BUILDOUT": E2RArchetype.MEMORY_SUPERCYCLE_AI_CAPEX.value,
    "HBM_EUV_AND_ADVANCED_PACKAGING_CAPEX": E2RArchetype.ADVANCED_PACKAGING_EQUIPMENT_KOREA.value,
    "HBM_CATCHUP_EXECUTION": E2RArchetype.HBM_CATCHUP_EXECUTION.value,
    "FOUNDRY_TURNAROUND_CONTRACT": E2RArchetype.SYSTEM_SEMI_FOUNDARY_OPTION_KOREA.value,
    "HBM_BONDER_EQUIPMENT_KOREA": E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA.value,
    "SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER": E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER.value,
    "POLICY_FOUNDRY_EVENT": E2RArchetype.POLICY_FOUNDRY_EVENT.value,
    "AI_CHIP_INFRASTRUCTURE_EVENT": E2RArchetype.OPENAI_STARGATE_AI_CAPEX_EVENT.value,
    "GEOPOLITICAL_EXPORT_CONTROL_OVERLAY": E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY.value,
    "SEMICONDUCTOR_IP_LEAK_REDTEAM": E2RArchetype.IP_LEAK_SUPPLY_CHAIN_REDTEAM.value,
    "CORPORATE_ACTION_SPINOFF_EVENT": E2RArchetype.EVENT_PREMIUM.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
}

ROUND232_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "company_level_customer_evidence",
    "product_specific_exposure",
    "order_shipment_contract_or_revenue_path",
    "gross_margin_or_opm_improvement",
    "eps_or_fcf_revision",
    "capacity_bottleneck_or_supply_allocation",
    "price_path_after_evidence",
    "export_control_labor_ip_accounting_risk_passed",
)

ROUND232_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "ai_keyword_only",
    "server_theme_only",
    "unconfirmed_customer_media_report",
    "design_win_without_revenue",
    "policy_foundry_without_order",
    "openai_or_nvidia_headline_without_company_revenue",
    "spin_off_or_corporate_action_only",
    "customer_name_without_margin",
)

ROUND232_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "stage3_after_3x_plus_price_move",
    "market_cap_milestone_headline",
    "openai_stargate_or_nvidia_event_basket_rally",
    "unconfirmed_customer_diversification_report_plus_20pct",
    "ai_capex_consensus_crowding",
    "record_high_before_volume_or_margin",
    "spin_off_or_corporate_action_prices_before_revenue",
)

ROUND232_HARD_4C_GATES: tuple[str, ...] = (
    "hbm_qualification_failure",
    "order_pushout",
    "customer_capex_cut",
    "memory_price_decline",
    "hbm_supply_normalization",
    "china_fab_export_control_disruption",
    "equipment_authorization_loss",
    "labor_strike_or_production_halt",
    "ip_leakage_or_china_competitive_catchup",
    "accounting_or_disclosure_trust_break",
    "customer_concentration_failure",
)

ROUND232_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "capex_or_contract_value_anchor",
    "market_cap_anchor",
    "allocation_or_capacity_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round232ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round232ShadowWeightRow:
    archetype: E2RArchetype
    eps_revision: int
    hbm4_first_mover: int
    capacity_bottleneck: int
    confirmed_order: int
    product_specificity: int
    order_to_revenue: int
    margin_visibility: int
    advanced_packaging_capacity: int
    price_path_alignment: int
    event_penalty: int
    labor_export_ip_redteam: int
    watch_4b_sensitivity: int
    hard_4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "eps_revision": _signed(self.eps_revision),
            "hbm4_first_mover": _signed(self.hbm4_first_mover),
            "capacity_bottleneck": _signed(self.capacity_bottleneck),
            "confirmed_order": _signed(self.confirmed_order),
            "product_specificity": _signed(self.product_specificity),
            "order_to_revenue": _signed(self.order_to_revenue),
            "margin_visibility": _signed(self.margin_visibility),
            "advanced_packaging_capacity": _signed(self.advanced_packaging_capacity),
            "price_path_alignment": _signed(self.price_path_alignment),
            "event_penalty": _signed(self.event_penalty),
            "labor_export_ip_redteam": _signed(self.labor_export_ip_redteam),
            "4b_watch_sensitivity": _signed(self.watch_4b_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard_4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round232DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round232CaseCandidate:
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
    stage2_price_anchor: float | None
    stage3_price_anchor: float | None
    stage4b_price_anchor: float | None
    stage4c_price_anchor: float | None
    peak_price_anchor: float | None
    peak_return_from_stage3_pct: float | None
    extra_price_metrics: Mapping[str, float | str | bool]
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


ROUND232_SCORE_ADJUSTMENTS: tuple[Round232ScoreAdjustment, ...] = (
    Round232ScoreAdjustment("eps_revision", 5, "raise", "R2 Green은 EPS/FCF revision이 있어야 한다."),
    Round232ScoreAdjustment("hbm4_first_mover", 5, "raise", "HBM4 first mover는 구조적 visibility를 높인다."),
    Round232ScoreAdjustment("capacity_bottleneck", 5, "raise", "HBM, EUV, advanced packaging CAPA 병목은 핵심 축이다."),
    Round232ScoreAdjustment("confirmed_customer_order", 5, "raise", "미확정 보도보다 확인된 고객 주문을 우선한다."),
    Round232ScoreAdjustment("product_specificity", 4, "raise", "HBM bonder, 2nm GAA처럼 제품 단위 노출이 필요하다."),
    Round232ScoreAdjustment("order_to_revenue_conversion", 4, "raise", "order/design win은 매출 전환 전 Stage 2다."),
    Round232ScoreAdjustment("gross_margin_visibility", 4, "raise", "volume shipment만으로 부족하고 margin이 필요하다."),
    Round232ScoreAdjustment("advanced_packaging_capacity", 4, "raise", "AI memory 병목은 advanced packaging CAPA와 연결된다."),
    Round232ScoreAdjustment("price_path_alignment", 5, "raise", "증거 이후 가격경로가 따라오는지 확인한다."),
    Round232ScoreAdjustment("ai_keyword_only", -5, "lower", "AI 이름만으로 Green 금지다."),
    Round232ScoreAdjustment("server_theme_only", -4, "lower", "서버 테마만으로는 회사 EPS/FCF가 아니다."),
    Round232ScoreAdjustment("design_win_without_revenue", -4, "lower", "design win은 tape-out, 양산, revenue 전 Stage 2다."),
    Round232ScoreAdjustment("policy_foundry_without_order", -5, "lower", "정책 foundry는 회사 주문 전 event/policy watch다."),
    Round232ScoreAdjustment("unconfirmed_media_report", -5, "lower", "미확정 고객 보도 급등은 4B-watch다."),
    Round232ScoreAdjustment("openai_or_nvidia_event_without_company_revenue", -4, "lower", "OpenAI/Nvidia headline은 후발주 revenue bridge 전 Green 금지다."),
    Round232ScoreAdjustment("customer_name_without_margin", -3, "lower", "고객명보다 margin/OPM/EPS가 필요하다."),
    Round232ScoreAdjustment("corporate_action_without_order", -4, "lower", "spin-off만으로 Stage 3가 아니다."),
    Round232ScoreAdjustment("price_rally_before_confirmation", -5, "lower", "확인 전 급등은 4B-watch로 둔다."),
    Round232ScoreAdjustment("labor_disruption_risk", -4, "lower", "파업·생산중단 리스크는 R2 4C-watch다."),
    Round232ScoreAdjustment("china_fab_export_control_risk", -4, "lower", "중국 fab 장비규제는 4C-watch다."),
    Round232ScoreAdjustment("ip_leak_to_china_risk", -4, "lower", "IP 유출은 경쟁력 훼손 RedTeam이다."),
)


ROUND232_SHADOW_WEIGHT_ROWS: tuple[Round232ShadowWeightRow, ...] = (
    Round232ShadowWeightRow(E2RArchetype.MEMORY_HBM4_FIRST_MOVER, 5, 5, 5, 4, 5, 4, 4, 5, 5, -1, 3, 5, 4, "SK Hynix confirms structural success but now requires 4B-watch."),
    Round232ShadowWeightRow(E2RArchetype.HBM_CATCHUP_EXECUTION, 4, 3, 4, 3, 4, 3, 4, 3, 3, -2, 5, 4, 4, "Samsung is Stage 2 until HBM/foundry volume sales and margins confirm."),
    Round232ShadowWeightRow(E2RArchetype.SYSTEM_SEMI_FOUNDARY_OPTION_KOREA, 4, 1, 2, 5, 3, 4, 5, 2, 3, -3, 4, 4, 4, "Samsung foundry deal helps but yield, margin and labor risks remain."),
    Round232ShadowWeightRow(E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA, 3, 0, 5, 5, 5, 4, 4, 3, 4, -3, 2, 5, 3, "Hanmi confirmed order is good; unconfirmed customer rumor is 4B risk."),
    Round232ShadowWeightRow(E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER, 2, 0, 2, 2, 4, 3, 3, 1, 2, -4, 1, 3, 3, "Gaonchips design win needs tape-out, production and revenue."),
    Round232ShadowWeightRow(E2RArchetype.POLICY_FOUNDRY_EVENT, 1, 0, 2, 1, 2, 1, 2, 1, 1, -5, 2, 4, 3, "Policy foundry consultation is not company Green."),
    Round232ShadowWeightRow(E2RArchetype.OPENAI_STARGATE_AI_CAPEX_EVENT, 3, 2, 5, 3, 3, 2, 2, 2, 4, -4, 2, 5, 3, "OpenAI/Nvidia events validate leaders but create event premium for followers."),
    Round232ShadowWeightRow(E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 5, 3, 5, "China fab authorization loss is 4C-watch until production/revenue impact confirmed."),
    Round232ShadowWeightRow(E2RArchetype.EVENT_PREMIUM, 1, 0, 2, 1, 2, 2, 3, 1, 2, -5, 2, 5, 3, "Spin-off optionality requires listed vehicle, order book and revenue conversion."),
)


ROUND232_DEEP_SUB_ARCHETYPES: tuple[Round232DeepSubArchetype, ...] = (
    Round232DeepSubArchetype("HBM leader", E2RArchetype.MEMORY_HBM4_FIRST_MOVER, ("SK Hynix", "HBM4 certification", "Nvidia customer visibility", "EUV order", "advanced packaging plant", "4B crowding")),
    Round232DeepSubArchetype("Samsung catch-up", E2RArchetype.HBM_CATCHUP_EXECUTION, ("Samsung Electronics", "HBM3E", "HBM4", "Nvidia", "AMD", "Tesla foundry contract", "labor strike")),
    Round232DeepSubArchetype("HBM equipment", E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA, ("Hanmi Semiconductor", "TSV-TC bonder", "SK Hynix order", "unconfirmed Micron report")),
    Round232DeepSubArchetype("System semiconductor", E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER, ("Gaonchips", "Preferred Networks", "Samsung 2nm GAA", "design win", "mass production required")),
    Round232DeepSubArchetype("Policy foundry", E2RArchetype.POLICY_FOUNDRY_EVENT, ("DB HiTek", "40nm foundry", "defense semiconductor", "policy support", "company order required")),
    Round232DeepSubArchetype("AI infrastructure event", E2RArchetype.OPENAI_STARGATE_AI_CAPEX_EVENT, ("OpenAI Stargate", "Nvidia Blackwell", "Korea data centers", "leader demand validation", "follower event premium")),
    Round232DeepSubArchetype("Export control RedTeam", E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY, ("U.S. China equipment authorization", "China fab exposure", "Samsung", "SK Hynix", "4C-watch")),
    Round232DeepSubArchetype("Corporate action equipment optionality", E2RArchetype.EVENT_PREMIUM, ("Hanwha Precision Machinery", "spin-off", "HBM equipment optionality", "order revenue required")),
)


ROUND232_CASE_CANDIDATES: tuple[Round232CaseCandidate, ...] = (
    Round232CaseCandidate(
        case_id="r2_loop10_sk_hynix_hbm4_euv_packaging_4b",
        symbol="000660",
        company_name="SK하이닉스",
        primary_archetype=E2RArchetype.MEMORY_HBM4_FIRST_MOVER,
        secondary_archetypes=(E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.MEMORY_SUPERCYCLE_AI_CAPEX, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="structural_success",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 6, 25),
        stage3_date=date(2024, 6, 25),
        stage4b_date=date(2026, 5, 14),
        stage4c_date=None,
        stage3_decision="hbm_dominance_hbm4_euv_advanced_packaging_and_eps_revision_validate_stage3_but_current_state_is_4b_watch",
        stage4b_status="4B-watch/elevated",
        hard_4c_confirmed=False,
        evidence_fields=("hbm_dominance", "dram_price_upcycle", "eps_revision", "hbm4_internal_certification", "asml_euv_order_11_95tn_krw", "advanced_packaging_plant_19tn_krw"),
        red_flag_fields=("market_cap_milestone_headline", "reported_2025_return_274pct", "reported_2026_return_above_200pct", "crowding_watch"),
        price_data_source="MarketWatch / Reuters reported price and return anchors",
        reported_price_anchor="222,000 KRW Stage 3 anchor; market cap about $942B by 2026-05-14",
        reported_return_anchor="HBM4 +7.3%; EUV order +5.7%; 2025 +274%; 2026 >+200%",
        mfe_1d=7.3,
        mae_1d=None,
        stage2_price_anchor=222000.0,
        stage3_price_anchor=222000.0,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"hbm4_event_return_pct": 7.3, "hbm4_event_kospi_pct": 1.2, "hbm4_relative_outperformance_pp": 6.1, "asml_euv_order_krw_trn": 11.95, "asml_euv_order_usd_bn": 7.97, "asml_euv_event_return_pct": 5.7, "estimated_euv_tools": 30.0, "advanced_packaging_investment_krw_trn": 19.0, "advanced_packaging_investment_usd_bn": 12.85, "reported_return_2025_pct": 274.0, "reported_return_2026_ytd_pct_min": 200.0, "minimum_compounded_return_from_2025_start_pct": 1022.0, "market_cap_2026_usd_bn": 942.0, "minimum_market_cap_mfe_pct": 842.0},
        score_price_alignment="aligned",
        round_alignment_label="aligned",
        rerating_result="true_rerating",
        round_rerating_label="true_rerating_plus_4B_watch",
        stage_failure_type="green_success",
        round_stage_failure_label="green_success_then_4B_watch",
        price_validation_status="reported_price_anchor_not_full_ohlc",
        notes="HBM4, EUV and advanced packaging capacity confirm structural success; current state is 4B-watch after massive MFE.",
    ),
    Round232CaseCandidate(
        case_id="r2_loop10_samsung_hbm_foundry_labor_export_watch",
        symbol="005930",
        company_name="삼성전자",
        primary_archetype=E2RArchetype.HBM_CATCHUP_EXECUTION,
        secondary_archetypes=(E2RArchetype.SYSTEM_SEMI_FOUNDARY_OPTION_KOREA, E2RArchetype.LABOR_SUPPLY_CHAIN_4C_WATCH, E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY),
        case_type="success_candidate",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 7, 28),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 1),
        stage3_decision="hbm_foundry_catchup_is_stage2_until_volume_margin_eps_and_labor_export_risks_clear",
        stage4b_status="4B-watch-if_catchup_narrative_prices_before_volume",
        hard_4c_confirmed=False,
        evidence_fields=("foundry_contract_16_5bn_usd", "contract_through_2033", "tesla_client_reported", "nvidia_hbm3e_hbm4_collaboration", "amd_ai_memory_mou"),
        red_flag_fields=("china_fab_export_control_event", "labor_strike_risk", "foundry_loss_h1_above_5tn_krw", "hbm_volume_margin_unconfirmed"),
        price_data_source="Reuters contract/event/strike anchors",
        reported_price_anchor="Foundry event +3.5%; Nvidia HBM event +4.32%; strike event -9.3%",
        reported_return_anchor="Export-control -2.3%; court relief +3.88%; possible strike workers 45,000-50,000+",
        mfe_1d=4.32,
        mae_1d=-9.3,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"foundry_contract_usd_bn": 16.5, "foundry_contract_event_return_pct": 3.5, "foundry_contract_duration": "through_end_2033", "tesla_client_reported": True, "estimated_foundry_loss_h1_krw_trn": 5.0, "nvidia_hbm_event_return_pct": 4.32, "export_control_event_mae_pct": -2.3, "samsung_china_dram_exposure": "more_than_one_third", "strike_event_mae_pct": -9.3, "court_ruling_relief_return_pct": 3.88, "kospi_same_context_may18_pct": 0.31, "relative_outperformance_may18_pp": 3.57, "possible_strike_workers": "45000-50000+", "possible_direct_loss_per_day_krw_trn": 1.0, "prolonged_disruption_damage_krw_trn": 100.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_4C_watch",
        rerating_result="unknown",
        round_rerating_label="HBM_catchup_foundry_turnaround_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_until_volume_margin_confirm",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Samsung has Stage 2 HBM/foundry evidence, but volume/margin/EPS and labor/export-control risks must clear before Green.",
    ),
    Round232CaseCandidate(
        case_id="r2_loop10_hanmi_hbm_bonder_confirmed_vs_rumor",
        symbol="042700",
        company_name="한미반도체",
        primary_archetype=E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA,
        secondary_archetypes=(E2RArchetype.SEMI_EQUIPMENT_AI_CAPEX, E2RArchetype.CROWDED_RERATING_4B_WATCH),
        case_type="success_candidate",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2024, 3, 1),
        stage3_date=None,
        stage4b_date=date(2024, 3, 28),
        stage4c_date=None,
        stage3_decision="confirmed_hynix_order_supports_stage2_but_unconfirmed_micron_report_is_4b_watch",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("confirmed_sk_hynix_contract_21_48bn_krw", "recent_deals_total_200bn_krw", "tsv_tc_bonder", "hbm_packaging_equipment"),
        red_flag_fields=("micron_deal_unconfirmed_media_report", "stage4b_event_mfe_22pct", "customer_concentration", "hbm_capex_pause_risk"),
        price_data_source="WSJ reported price and contract anchors",
        reported_price_anchor="139,100 KRW stage4b peak on unconfirmed Micron media report",
        reported_return_anchor="+22% event MFE; KOSPI -0.3%; relative +22.3pp",
        mfe_1d=22.0,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=139100.0,
        stage4c_price_anchor=None,
        peak_price_anchor=139100.0,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"confirmed_sk_hynix_contract_krw_bn": 21.48, "recent_deals_total_krw_bn": 200.0, "stage4b_event_mfe_pct": 22.0, "implied_pre_4b_reference_price": 114016.0, "kospi_same_context_pct": -0.3, "relative_outperformance_pp": 22.3, "micron_deal_status": "unconfirmed_media_report"},
        score_price_alignment="aligned",
        round_alignment_label="aligned_candidate_4B_watch",
        rerating_result="unknown",
        round_rerating_label="HBM_equipment_rerating_candidate",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="confirmed_order_good_but_unconfirmed_customer_rumor_4B",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Confirmed SK Hynix order is Stage 2/3 candidate; unconfirmed Micron report is 4B-watch.",
    ),
    Round232CaseCandidate(
        case_id="r2_loop10_gaonchips_pfn_design_win",
        symbol="399720",
        company_name="가온칩스",
        primary_archetype=E2RArchetype.SYSTEM_SEMI_DESIGN_HOUSE_AI_ORDER,
        secondary_archetypes=(E2RArchetype.SYSTEM_SEMI_FOUNDARY_OPTION_KOREA,),
        case_type="success_candidate",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2024, 7, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="design_win_is_stage2_until_tapeout_mass_production_revenue_and_margin_confirm",
        stage4b_status="4B-watch-if_ai_design_house_theme_prices_before_revenue",
        hard_4c_confirmed=False,
        evidence_fields=("preferred_networks_ai_chip_order", "samsung_2nm_gaa", "advanced_packaging", "gaonchips_designed_chips", "generative_ai_llm_hpc_hardware"),
        red_flag_fields=("order_size_not_disclosed", "revenue_recognition_unconfirmed", "gross_margin_unconfirmed", "tapeout_yield_risk"),
        price_data_source="Reuters evidence source",
        reported_price_anchor="Reuters did not provide Gaonchips stock reaction anchor",
        reported_return_anchor="Order size undisclosed; stage2 evidence only",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"order_size": "not_disclosed", "technology": "Samsung 2nm GAA + advanced packaging", "customer": "Preferred Networks", "end_use": "generative AI / LLM HPC hardware"},
        score_price_alignment="unknown",
        round_alignment_label="unknown_insufficient_evidence",
        rerating_result="unknown",
        round_rerating_label="design_win_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_evidence_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Design win is Stage 2; tape-out, mass production, revenue and margin required for Stage 3.",
    ),
    Round232CaseCandidate(
        case_id="r2_loop10_db_hitek_policy_foundry",
        symbol="000990",
        company_name="DB하이텍 / policy foundry exposure",
        primary_archetype=E2RArchetype.POLICY_FOUNDRY_EVENT,
        secondary_archetypes=(E2RArchetype.SYSTEM_SEMI_FOUNDARY_OPTION_KOREA, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        stage1_date=date(2025, 12, 10),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="policy_foundry_consultation_is_stage1_to_2_until_funded_capex_company_order_utilization_and_margin_confirm",
        stage4b_status="4B-watch-if_policy_foundry_theme_prices_before_order",
        hard_4c_confirmed=False,
        evidence_fields=("public_private_foundry_4_5tn_krw", "12inch_40nm_facility", "automotive_data_center_legacy_chip", "defense_semiconductor_localization"),
        red_flag_fields=("company_order_unconfirmed", "utilization_unconfirmed", "customer_commitment_missing", "budget_or_private_burden_risk"),
        price_data_source="Reuters policy evidence source",
        reported_price_anchor="Reuters did not provide DB HiTek stock reaction anchor",
        reported_return_anchor="4.5T KRW public-private foundry; defense import dependence 99%",
        mfe_1d=None,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"foundry_project_size_krw_trn": 4.5, "foundry_project_size_usd_bn": 3.06, "process_node_nm": 40.0, "wafer_size_inch": 12.0, "defense_semiconductor_import_dependency_pct": 99.0, "company_status": "policy_beneficiary_candidate_not_confirmed_order"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_policy_watch",
        rerating_result="policy_event_rerating",
        round_rerating_label="policy_foundry_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="stage1_attention_only",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Government foundry consultation is Stage 1/2, not company Green.",
    ),
    Round232CaseCandidate(
        case_id="r2_loop10_openai_nvidia_korea_ai_infra_event",
        symbol="000660/005930/035420/035720/AI_infra_basket",
        company_name="OpenAI/Nvidia Korea AI infrastructure event",
        primary_archetype=E2RArchetype.OPENAI_STARGATE_AI_CAPEX_EVENT,
        secondary_archetypes=(E2RArchetype.MEMORY_HBM_CAPACITY, E2RArchetype.AI_CHIP_LISTED_EARNINGS_LINK_GATE, E2RArchetype.EVENT_PREMIUM),
        case_type="4b_watch",
        stage1_date=date(2025, 10, 2),
        stage2_date=date(2025, 10, 31),
        stage3_date=None,
        stage4b_date=date(2025, 10, 2),
        stage4c_date=None,
        stage3_decision="openai_nvidia_event_validates_leaders_but_followers_need_company_revenue_bridge_before_green",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("openai_stargate_partnership", "sk_hynix_event_mfe_12pct", "samsung_event_mfe_4_7pct", "nvidia_blackwell_korea_260k_chips", "korea_data_center_initial_20mw"),
        red_flag_fields=("follower_company_revenue_bridge_missing", "ai_infra_basket_event_premium", "openai_or_nvidia_headline_without_company_revenue"),
        price_data_source="Reuters reported event return and AI-chip allocation anchors",
        reported_price_anchor="Combined Samsung/SK Hynix market cap added $37B",
        reported_return_anchor="OpenAI event: SK Hynix +12%, Samsung +4.7%, KOSPI >+3%",
        mfe_1d=12.0,
        mae_1d=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"sk_hynix_openai_event_mfe_pct": 12.0, "samsung_openai_event_mfe_pct": 4.7, "combined_market_cap_added_usd_bn": 37.0, "kospi_event_return_pct_min": 3.0, "openai_korea_data_center_initial_capacity_mw": 20.0, "nvidia_blackwell_korea_total_chips_min": 260000.0, "government_allocation_chips": 50000.0, "samsung_allocation_chips": 50000.0, "sk_group_allocation_chips": 50000.0, "hyundai_allocation_chips": 50000.0, "naver_allocation_chips": 60000.0},
        score_price_alignment="aligned",
        round_alignment_label="aligned_for_SK_Hynix_event_premium_for_followers",
        rerating_result="event_premium",
        round_rerating_label="AI_memory_and_AI_infra_demand_validation_4B_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="4B_watch",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Demand validation for leaders, but followers need company revenue bridge before Green.",
    ),
    Round232CaseCandidate(
        case_id="r2_loop10_export_control_china_fab_watch",
        symbol="005930/000660/067310/042700",
        company_name="Samsung/SK Hynix/Hana Micron/Hanmi",
        primary_archetype=E2RArchetype.GEOPOLITICAL_EXPORT_CONTROL_OVERLAY,
        secondary_archetypes=(E2RArchetype.HBM_SUPPLY_CHAIN_LABOR_DISRUPTION_OVERLAY, E2RArchetype.IP_LEAK_SUPPLY_CHAIN_REDTEAM),
        case_type="4c_thesis_break",
        stage1_date=date(2025, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 9, 1),
        stage3_decision="export_control_shock_is_r2_4c_watch_until_production_or_revenue_disruption_confirms_hard_4c",
        stage4b_status="4C-watch-not-hard-4C",
        hard_4c_confirmed=False,
        evidence_fields=("us_revokes_china_equipment_authorization", "samsung_china_dram_exposure_above_one_third", "sk_hynix_china_dram_nand_exposure_30_40pct"),
        red_flag_fields=("export_control_event_mae", "china_fab_exposure", "authorization_loss", "production_disruption_unconfirmed"),
        price_data_source="Reuters reported event return anchor",
        reported_price_anchor="Samsung -2.3%, SK Hynix -4.4%, Hana Micron -1.7%, Hanmi -4.4%",
        reported_return_anchor="KOSPI -0.7%; authorization effective delay 120 days",
        mfe_1d=None,
        mae_1d=-4.4,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"samsung_mae_1d_pct": -2.3, "sk_hynix_mae_1d_pct": -4.4, "hana_micron_mae_1d_pct": -1.7, "hanmi_mae_1d_pct": -4.4, "kospi_same_context_pct": -0.7, "samsung_relative_underperformance_pp": -1.6, "sk_hynix_relative_underperformance_pp": -3.7, "hanmi_relative_underperformance_pp": -3.7, "samsung_china_dram_exposure": "more_than_one_third", "sk_hynix_china_dram_nand_exposure_pct": "30-40", "authorization_effective_delay_days": 120.0},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="export_control_4C_watch",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4C_watch_not_hard_4C",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Export-control shock is 4C-watch; hard 4C requires production/revenue disruption.",
    ),
    Round232CaseCandidate(
        case_id="r2_loop10_hanwha_precision_hbm_equipment_spinoff",
        symbol="012450_parent_exposure",
        company_name="Hanwha Precision Machinery / Hanwha Aerospace spin-off exposure",
        primary_archetype=E2RArchetype.EVENT_PREMIUM,
        secondary_archetypes=(E2RArchetype.HBM_BONDER_EQUIPMENT_KOREA, E2RArchetype.CAPITAL_ALLOCATION_DILUTION_OVERLAY),
        case_type="event_premium",
        stage1_date=date(2024, 4, 2),
        stage2_date=date(2024, 4, 5),
        stage3_date=None,
        stage4b_date=date(2024, 4, 2),
        stage4c_date=None,
        stage3_decision="hbm_equipment_optionality_via_spinoff_is_corporate_action_watch_until_order_revenue_margin_confirm",
        stage4b_status="4B-watch",
        hard_4c_confirmed=False,
        evidence_fields=("hanwha_precision_machinery_spinoff", "hbm_equipment_development_angle", "industrial_solutions_value_2tn_krw", "defense_business_value_10tn_krw"),
        red_flag_fields=("corporate_action_without_order", "formal_announcement_event_mae_minus_8pct", "order_book_missing", "listed_vehicle_missing"),
        price_data_source="Reuters corporate-action / event-return anchor",
        reported_price_anchor="Parent rose >15% on media report, then fell -8% after formal announcement",
        reported_return_anchor="Industrial solutions value 2T KRW; defense business value 10T KRW",
        mfe_1d=15.0,
        mae_1d=-8.0,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        peak_return_from_stage3_pct=None,
        extra_price_metrics={"media_report_event_mfe_pct_min": 15.0, "formal_announcement_event_mae_pct": -8.0, "industrial_solutions_estimated_value_krw_trn": 2.0, "industrial_solutions_estimated_value_usd_bn": 1.48, "defense_business_estimated_value_krw_trn": 10.0, "revenue_contribution_from_spun_units_pct": 16.0, "parent_market_cap_context_krw_trn": 11.0, "industrial_plus_defense_estimate_krw_trn": 12.0, "estimated_sum_vs_parent_market_cap_pct": 9.1},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium",
        rerating_result="event_premium",
        round_rerating_label="HBM_equipment_corporate_action_watch",
        stage_failure_type="false_yellow",
        round_stage_failure_label="stage2_evidence_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="HBM equipment optionality via spin-off is Stage 2/corporate-action event; order/revenue/margin required before Green.",
    ),
)


def round232_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    stage3_terms = ("hbm", "euv", "advanced_packaging", "eps", "revenue", "margin", "fcf", "price")
    for candidate in ROUND232_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND232_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round232 R2 Loop-10 AI semiconductor price validation case. "
                "Calibration-only; not production scoring input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(term in field.lower() for term in stage3_terms)),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if "4b" in field.lower() or "event" in field.lower() or "market_cap" in field.lower() or "report" in field.lower() or "premium" in field.lower()),
            stage4c_evidence=tuple(field for field in candidate.red_flag_fields if "export" in field.lower() or "strike" in field.lower() or "labor" in field.lower() or "ip" in field.lower() or "authorization" in field.lower() or "disruption" in field.lower() or "risk" in field.lower()),
            must_have_fields=ROUND232_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"event_premium", "overheat", "failed_rerating", "4b_watch", "4c_thesis_break"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND232_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_price_or_stage_dates",
                "do_not_treat_ai_keyword_design_win_policy_event_or_spinoff_as_green_alone",
                *ROUND232_GREEN_REQUIRED_FIELDS,
                *ROUND232_GREEN_FORBIDDEN_PATTERNS,
            ),
            notes=candidate.notes,
            price_validation=PriceValidation(
                stage2_price=candidate.stage2_price_anchor,
                stage3_price=candidate.stage3_price_anchor,
                stage4b_price=candidate.stage4b_price_anchor,
                stage4c_price=candidate.stage4c_price_anchor,
                peak_price=candidate.peak_price_anchor,
                peak_return_from_stage3=candidate.peak_return_from_stage3_pct,
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
                stage_dates_confidence=0.85 if candidate.stage3_date else 0.75,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round232_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND232_CASE_CANDIDATES:
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
                "stage2_price_anchor": _float_text(candidate.stage2_price_anchor),
                "stage3_price_anchor": _float_text(candidate.stage3_price_anchor),
                "stage4b_price_anchor": _float_text(candidate.stage4b_price_anchor),
                "stage4c_price_anchor": _float_text(candidate.stage4c_price_anchor),
                "peak_return_from_stage3_pct": _float_text(candidate.peak_return_from_stage3_pct),
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


def round232_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND232_SCORE_ADJUSTMENTS)


def round232_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND232_SHADOW_WEIGHT_ROWS)


def round232_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND232_DEEP_SUB_ARCHETYPES)


def round232_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round232_price_validation": "true"} for field in ROUND232_PRICE_VALIDATION_FIELDS)


def round232_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round232_label": label, "canonical_archetype": canonical} for label, canonical in ROUND232_REQUIRED_TARGET_ALIASES.items())


def round232_summary() -> dict[str, int | bool | str]:
    cases = ROUND232_CASE_CANDIDATES
    return {
        "source_round": ROUND232_SOURCE_ROUND_PATH,
        "large_sector": ROUND232_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "structural_success_count": sum(1 for case in cases if case.case_type == "structural_success"),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium" or case.rerating_result == "event_premium"),
        "watch_4b_count": sum(1 for case in cases if case.case_type == "4b_watch" or "4B" in case.stage4b_status),
        "watch_4c_count": sum(1 for case in cases if case.stage4c_date is not None),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "target_archetype_count": len(ROUND232_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND232_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND232_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
    }


def round232_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND232_SOURCE_ROUND_PATH,
        "large_sector": ROUND232_LARGE_SECTOR,
        "summary": round232_summary(),
        "target_aliases": dict(ROUND232_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND232_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND232_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND232_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND232_HARD_4C_GATES),
        "deep_sub_archetypes": round232_deep_sub_archetype_rows(),
        "shadow_weights": round232_shadow_weight_rows(),
        "what_not_to_change": [
            "do_not_use_round232_cases_as_candidate_generation_input",
            "do_not_apply_shadow_weights_to_production_scoring_yet",
            "do_not_treat_ai_keyword_design_win_policy_event_or_spinoff_as_green",
            "do_not_invent_ohlc_or_stage_dates",
        ],
    }


def render_round232_summary_markdown() -> str:
    summary = round232_summary()
    lines = [
        "# Round 232 R2 Loop 10 AI Semiconductor Price Validation",
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
        f"- event_premium_count: {summary['event_premium_count']}",
        f"- 4B-watch cases: {summary['watch_4b_count']}",
        f"- 4C-watch cases: {summary['watch_4c_count']}",
        f"- hard_4c_case_count: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        f"- full_ohlc_complete: {str(summary['full_ohlc_complete']).lower()}",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | stage3 | 4B | 4C | round alignment | note |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND232_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.case_type,
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
            "- SK Hynix remains the clean R2 structural-success benchmark, but current state is 4B-watch after very large rerating.",
            "- Samsung Electronics is Stage 2 watch until HBM/foundry volume, margin, EPS, labor and export-control risks clear.",
            "- Hanmi Semiconductor separates confirmed SK Hynix orders from an unconfirmed Micron-rumor rally.",
            "- Gaonchips is a design-win Stage 2 case; tape-out, mass production, revenue and margin are required before Green.",
            "- DB HiTek/public-private foundry is policy evidence, not company-level Green.",
            "- OpenAI/Nvidia Korea events validate memory demand for leaders but are event premium for follower baskets.",
            "- Export-control shock and labor/IP risks are R2 4C-watch until production or revenue disruption confirms hard 4C.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round232_green_gate_review_markdown() -> str:
    lines = [
        "# Round 232 R2 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R2 Stage 3-Green is not `AI semiconductor beneficiary`. It requires customer order, product specificity, shipment/revenue, margin, EPS/FCF, and price-path confirmation.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND232_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND232_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(
        [
            "",
            "## Easy Example",
            "- `HBM4 certification + EUV order + advanced packaging plant + EPS revision` can validate Stage 3, then still trigger 4B-watch after a large rerating.",
            "- `Preferred Networks design win` is Stage 2 until tape-out, production, revenue and margin are visible.",
            "- `OpenAI/Nvidia headline` validates leader demand but does not make every AI-infra follower Green.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round232_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 232 R2 4B/4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND232_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND232_HARD_4C_GATES)
    lines.extend(
        [
            "",
            "## Plain-Language Gate Notes",
            "",
            "- 4B catches leader rerating, market-cap headlines, unconfirmed customer-rumor rallies, and AI-infra basket event premium.",
            "- 4C catches export-control, labor disruption, IP leakage, customer capex cuts, and memory price reversals.",
            "- Export-control and strike events are watch states here; hard 4C requires production, shipment, revenue, or margin disruption.",
            "",
            "## Case Notes",
            "",
        ]
    )
    for case in ROUND232_CASE_CANDIDATES:
        if "4B" in case.stage4b_status or case.stage4c_date or case.red_flag_fields:
            lines.append(f"- {case.case_id}: {', '.join(case.red_flag_fields)}")
    return "\n".join(lines) + "\n"


def render_round232_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 232 R2 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND232_PRICE_VALIDATION_FIELDS)
    return "\n".join(lines) + "\n"


def write_round232_r2_loop10_reports(
    output_directory: str | Path = ROUND232_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND232_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND232_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round232_case_records(), cases_path),
        "audit": _write_json(round232_audit_payload(), audit_path),
        "summary": output / "round232_r2_loop10_price_validation_summary.md",
        "case_matrix": output / "round232_r2_loop10_case_matrix.csv",
        "target_aliases": output / "round232_r2_loop10_target_aliases.csv",
        "score_adjustments": output / "round232_r2_loop10_score_adjustments.csv",
        "shadow_weights": output / "round232_r2_loop10_shadow_weights.csv",
        "deep_sub_archetypes": output / "round232_r2_loop10_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round232_r2_loop10_price_validation_fields.csv",
        "green_gate_review": output / "round232_r2_loop10_green_gate_review.md",
        "price_validation_plan": output / "round232_r2_loop10_price_validation_plan.md",
        "stage4b_4c_review": output / "round232_r2_loop10_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round232_summary_markdown(), encoding="utf-8")
    _write_csv(round232_case_rows(), paths["case_matrix"])
    _write_csv(round232_target_alias_rows(), paths["target_aliases"])
    _write_csv(round232_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round232_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round232_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round232_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round232_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round232_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round232_stage4b_4c_review_markdown(), encoding="utf-8")
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
    return f"{value:+d}"
