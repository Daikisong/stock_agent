"""Round-221 R4 Loop-9 materials/spread/strategic-resources price validation.

Round 221 is calibration/evaluation material only. It turns the analyst's
materials, spread, and strategic-resource price anchors into structured case
records, shadow weights, and Green/4B/4C guardrails.

Easy example: a U.S. critical-minerals smelter can be useful Stage 2 evidence.
It is not Stage 3-Green until offtake, spread, cost curve, FCF, capex burden,
dilution risk, and price-path confirmation are visible as-of the replay date.
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


ROUND221_SOURCE_ROUND_PATH = "docs/round/round_221.md"
ROUND221_LARGE_SECTOR = Round10LargeSector.MATERIALS_SPREAD_STRATEGIC
ROUND221_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round221_r4_loop9_materials_spread_strategic_price_validation"
ROUND221_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r4_loop9_round221.jsonl"
ROUND221_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round221_r4_loop9_materials_spread_strategic_price_validation_audit.json"

ROUND221_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "STEEL_TARIFF_SPREAD_OVERLAY": E2RArchetype.STEEL_TARIFF_EVENT_KOREA.value,
    "STEEL_EXPORT_COMPETITIVENESS_4C_WATCH": E2RArchetype.STEEL_EXPORT_TARIFF_4C.value,
    "NONFERROUS_STRATEGIC_METALS": E2RArchetype.NONFERROUS_STRATEGIC_METALS.value,
    "CRITICAL_MINERALS_US_SUPPLY_CHAIN": E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS.value,
    "GOVERNANCE_DILUTION_EVENT": E2RArchetype.GOVERNANCE_DILUTION_EVENT.value,
    "PETROCHEMICAL_RESTRUCTURING_KOREA": E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA.value,
    "CHEMICAL_SPREAD_4C": E2RArchetype.COMMODITY_PRICE_4C_OVERLAY.value,
    "REFINING_SPREAD_CYCLE": E2RArchetype.REFINING_OIL_SPREAD.value,
    "LITHIUM_RESOURCE_SECURITY": E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA.value,
    "LITHIUM_CYCLE_OVERLAY": E2RArchetype.LITHIUM_CYCLE_OVERLAY.value,
    "POLYSILICON_NON_CHINA_SUPPLY_OPTION": E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION.value,
    "COPPER_PROCESSING_PLUS_DEFENSE": E2RArchetype.COPPER_PROCESSING_PLUS_DEFENSE.value,
    "M_AND_A_OPTIONALITY_EVENT": E2RArchetype.EVENT_PREMIUM.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
}

ROUND221_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "actual_product_spread",
    "cost_curve_advantage",
    "supply_discipline_or_capacity_shutdown",
    "inventory_build_absent",
    "fcf_after_working_capital",
    "price_floor_or_offtake",
    "medium_term_eps_revision",
    "capex_and_dilution_risk_passed",
    "policy_tariff_sanction_stress_passed",
    "price_path_after_evidence",
)

ROUND221_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "commodity_price_spike_only",
    "tariff_headline_only",
    "tender_offer_premium",
    "governance_battle_only",
    "policy_support_without_fcf",
    "unconfirmed_media_report",
    "mna_rumor_without_transaction",
    "restructuring_plan_without_margin",
    "lithium_or_polysilicon_price_event_only",
    "geopolitical_refining_margin_shock_only",
)

ROUND221_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "commodity_price_group_rally",
    "restructuring_expectation_multiple_expansion",
    "tender_offer_buyback_governance_battle_rally",
    "lithium_or_polysilicon_supply_discipline_event",
    "geopolitical_refining_margin_spike",
    "unconfirmed_customer_or_mna_report_rally",
    "price_runs_before_spread_and_fcf",
)

ROUND221_HARD_4C_GATES: tuple[str, ...] = (
    "spread_reversal",
    "china_oversupply",
    "middle_east_capacity_overhang",
    "inventory_build",
    "ncc_shutdown_or_operating_loss",
    "deal_or_tender_event_failure",
    "regulator_revision_order",
    "large_share_issue_or_dilution",
    "commodity_price_recollapse",
    "project_capex_overrun",
    "offtake_absence",
    "fcf_deterioration",
    "tariff_shock_causing_export_margin_damage",
)

ROUND221_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "relative_underperformance_pp",
    "commodity_drawdown_pct",
    "commodity_rebound_pct",
    "share_issuance_vs_project_value_pct",
    "rumor_duration_days",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round221ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round221ShadowWeightRow:
    archetype: E2RArchetype
    product_spread: int
    fcf_after_wc: int
    supply_discipline: int
    capacity_shutdown: int
    offtake: int
    cost_curve: int
    tariff_resilience: int
    resource_security: int
    event_penalty: int
    governance_redteam: int
    stage4b_watch_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "product_spread": _signed_int_text(self.product_spread),
            "fcf_after_wc": _signed_int_text(self.fcf_after_wc),
            "supply_discipline": _signed_int_text(self.supply_discipline),
            "capacity_shutdown": _signed_int_text(self.capacity_shutdown),
            "offtake": _signed_int_text(self.offtake),
            "cost_curve": _signed_int_text(self.cost_curve),
            "tariff_resilience": _signed_int_text(self.tariff_resilience),
            "resource_security": _signed_int_text(self.resource_security),
            "event_penalty": _signed_int_text(self.event_penalty),
            "governance_redteam": _signed_int_text(self.governance_redteam),
            "4b_watch_sensitivity": _signed_int_text(self.stage4b_watch_sensitivity),
            "hard4c_sensitivity": _signed_int_text(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round221CaseCandidate:
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
    extra_price_metrics: Mapping[str, float | str | bool]
    score_price_alignment: str
    rerating_result: str
    stage_failure_type: str
    price_validation_status: str
    notes: str

    @property
    def large_sector(self) -> str:
        return ROUND221_LARGE_SECTOR.value

    @property
    def expected_group(self) -> str:
        return self.case_type


ROUND221_SCORE_ADJUSTMENTS: tuple[Round221ScoreAdjustment, ...] = (
    Round221ScoreAdjustment("actual_product_spread", 5, "raise", "R4 Stage 3는 원자재 가격보다 제품 스프레드 확인이 먼저다."),
    Round221ScoreAdjustment("fcf_after_working_capital", 5, "raise", "재고와 운전자본 이후 FCF가 보여야 구조적 rerating 후보가 된다."),
    Round221ScoreAdjustment("supply_discipline_confirmed", 5, "raise", "공급규율 또는 설비중단이 실제 확인되어야 spread 회복이 지속된다."),
    Round221ScoreAdjustment("capacity_shutdown_confirmed", 4, "raise", "Daesan NCC 가동중단처럼 확정된 shutdown은 Stage 2 relief다."),
    Round221ScoreAdjustment("price_floor_or_offtake", 5, "raise", "전략자원은 price floor/offtake가 있어야 commodity cycle과 분리된다."),
    Round221ScoreAdjustment("cost_curve_advantage", 4, "raise", "cost curve 우위가 있어야 가격 하락에도 FCF 방어가 가능하다."),
    Round221ScoreAdjustment("tariff_resilience", 4, "raise", "관세 환경에서도 수출 마진이 방어되는지 확인한다."),
    Round221ScoreAdjustment("resource_security_with_downstream_margin", 4, "raise", "resource security는 downstream margin과 연결될 때만 강해진다."),
    Round221ScoreAdjustment("commodity_price_up_only", -5, "lower", "원자재 가격 상승만으로는 EPS/FCF 체급 변화를 증명하지 못한다."),
    Round221ScoreAdjustment("tariff_event_only", -4, "lower", "관세 headline은 수출업체에는 4C-watch가 될 수 있다."),
    Round221ScoreAdjustment("restructuring_plan_without_margin", -4, "lower", "구조조정 계획은 OPM/FCF 회복 전까지 Stage 2 watch다."),
    Round221ScoreAdjustment("policy_support_without_fcf", -4, "lower", "정책 지원만 있고 FCF가 없으면 Green 금지다."),
    Round221ScoreAdjustment("tender_offer_or_governance_premium", -5, "lower", "공개매수/경영권 프리미엄은 구조적 Stage 3와 분리한다."),
    Round221ScoreAdjustment("unconfirmed_media_report", -5, "lower", "미확정 고객·M&A 보도는 event premium이다."),
    Round221ScoreAdjustment("mna_rumor_without_transaction", -5, "lower", "거래가 확정되지 않은 M&A rumor는 Green 근거가 아니다."),
    Round221ScoreAdjustment("lithium_price_event", -5, "lower", "리튬 가격 반등은 cycle/event로 먼저 본다."),
    Round221ScoreAdjustment("refining_margin_geopolitical_shock", -3, "lower", "지정학적 정제마진 spike는 multi-quarter floor 전까지 cycle이다."),
    Round221ScoreAdjustment("capex_heavy_project_pre_revenue", -4, "lower", "상업가동 전 대형 CAPEX 프로젝트는 dilution/FCF 리스크가 크다."),
)


ROUND221_SHADOW_WEIGHT_ROWS: tuple[Round221ShadowWeightRow, ...] = (
    Round221ShadowWeightRow(E2RArchetype.STEEL_TARIFF_EVENT_KOREA, 5, 4, 3, 0, 1, 3, 5, 0, -4, 1, 4, 4, "POSCO/Hyundai Steel tariff shock shows export competitiveness 4C-watch."),
    Round221ShadowWeightRow(E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS, 3, 4, 3, 0, 5, 4, 2, 5, -3, 5, 5, 4, "Korea Zinc strategic minerals are Stage 2 but governance/dilution blocks Green."),
    Round221ShadowWeightRow(E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA, 5, 5, 5, 5, 1, 4, 0, 0, -3, 2, 3, 5, "Lotte Daesan shutdown is restructuring relief, not Green before spread/FCF."),
    Round221ShadowWeightRow(E2RArchetype.REFINING_OIL_SPREAD, 5, 4, 2, 0, 1, 3, 0, 0, -3, 1, 4, 3, "SK/S-Oil refining rebound is cyclical; battery drag and margin durability matter."),
    Round221ShadowWeightRow(E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA, 2, 4, 2, 0, 5, 4, 0, 5, -5, 1, 4, 4, "POSCO lithium JV is resource-security Stage 2 but lithium cycle risk remains."),
    Round221ShadowWeightRow(E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION, 3, 4, 3, 0, 5, 3, 2, 3, -5, 1, 5, 3, "OCI U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium."),
    Round221ShadowWeightRow(E2RArchetype.COPPER_PROCESSING_PLUS_DEFENSE, 4, 4, 2, 0, 3, 3, 1, 0, -5, 2, 5, 3, "Poongsan M&A rumor faded; Green requires confirmed transaction or margin/FCF."),
    Round221ShadowWeightRow(E2RArchetype.EVENT_PREMIUM, 0, 0, 0, 0, 0, 0, 0, 0, -5, 3, 5, 3, "M&A rumor without signed transaction should not become Green."),
)


ROUND221_CASE_CANDIDATES: tuple[Round221CaseCandidate, ...] = (
    Round221CaseCandidate(
        case_id="r4_loop9_posco_hyundai_steel_tariff_watch",
        symbol="005490/004020",
        company_name="POSCO Holdings / Hyundai Steel",
        primary_archetype=E2RArchetype.STEEL_TARIFF_EVENT_KOREA,
        secondary_archetypes=(E2RArchetype.STEEL_EXPORT_TARIFF_4C, E2RArchetype.STEEL_METAL_SPREAD),
        case_type="failed_rerating",
        stage1_date=date(2025, 2, 10),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 2, 10),
        stage3_decision="tariff_shock_is_redteam_input_for_korean_exporters_not_positive_stage",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("us_steel_aluminum_tariff_threat_25pct", "posco_price_230500", "posco_mae_3_6pct", "hyundai_steel_mae_2_9pct", "tariff_50pct_threat"),
        red_flag_fields=("tariff_export_competitiveness_risk", "policy_shock_unpriced", "steel_price_event_without_margin", "hard_4c_not_confirmed"),
        price_data_source="Reuters/WSJ reported event-return anchors",
        reported_price_anchor="POSCO 230,500 KRW on 2025-02-10 tariff shock",
        reported_return_anchor="POSCO -3.6%; Hyundai Steel -2.9%; later 50% tariff threat: Hyundai Steel -5.1%, POSCO -3.2%",
        mfe_1d=None,
        mae_1d=-3.6,
        mae_1d_secondary=-5.1,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=230500.0,
        peak_price_anchor=None,
        extra_price_metrics={
            "posco_implied_pre_event_reference_price": 239108.0,
            "hyundai_steel_mae_2025_02_10_pct": -2.9,
            "kospi_2025_02_10_pct": -0.5,
            "posco_relative_underperformance_pp": -3.1,
            "hyundai_steel_relative_underperformance_pp": -2.4,
            "hyundai_steel_mae_2025_06_02_pct": -5.1,
            "posco_mae_2025_06_02_pct": -3.2,
        },
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="should_have_been_red",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="U.S. tariff shock is 4C-watch for Korean steel exporters; Green requires actual spread and export margin resilience.",
    ),
    Round221CaseCandidate(
        case_id="r4_loop9_korea_zinc_strategic_governance",
        symbol="010130/000670",
        company_name="Korea Zinc / YoungPoong",
        primary_archetype=E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS,
        secondary_archetypes=(E2RArchetype.NONFERROUS_STRATEGIC_METALS, E2RArchetype.GOVERNANCE_DILUTION_EVENT, E2RArchetype.EVENT_PREMIUM_GOVERNANCE_OVERLAY),
        case_type="success_candidate",
        stage1_date=date(2024, 9, 1),
        stage2_date=date(2025, 12, 15),
        stage3_date=None,
        stage4b_date=date(2025, 12, 15),
        stage4c_date=date(2025, 12, 16),
        stage3_decision="critical_minerals_project_is_stage2_until_offtake_capex_fcf_dilution_and_governance_clear",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("us_critical_minerals_smelter_7_4bn_usd", "antimony_germanium_gallium_zinc_lead_copper_precious_metals", "commercial_operations_2027_2029", "us_smelter_event_plus_27pct"),
        red_flag_fields=("share_issuance_dilution", "governance_battle", "injunction_event_minus_13pct", "offtake_unconfirmed", "capex_heavy_project_pre_revenue"),
        price_data_source="FT/Reuters reported event anchors",
        reported_price_anchor="Korea Zinc +27%, -13%, +5%; YoungPoong -10.5%; share issue about $1.94B",
        reported_return_anchor="U.S. smelter +27%; injunction -13%; court rejection +5%; YoungPoong -10.5%",
        mfe_1d=27.0,
        mae_1d=-13.0,
        mae_1d_secondary=-10.5,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={
            "us_smelter_project_usd_bn": 7.4,
            "share_issuance_usd_bn": 1.94,
            "share_issuance_vs_project_value_pct": 26.2,
            "new_investor_stake_pct": 10.0,
            "mbk_youngpoong_stake_pct": "44-46",
            "commercial_operations": "2027-2029 gradual",
        },
        score_price_alignment="price_moved_without_evidence",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Strategic minerals are Stage 2; governance, dilution, offtake, and FCF must clear before Stage 3.",
    ),
    Round221CaseCandidate(
        case_id="r4_loop9_lotte_hd_petrochemical_restructuring",
        symbol="011170/HD_Hyundai_Chemical",
        company_name="Lotte Chemical / HD Hyundai Chemical",
        primary_archetype=E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA,
        secondary_archetypes=(E2RArchetype.CHEMICAL_SPREAD_KOREA, E2RArchetype.COMMODITY_PRICE_4C_OVERLAY),
        case_type="failed_rerating",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2026, 2, 24),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="restructuring_approval_is_stage2_relief_until_spread_opm_fcf_and_debt_stabilization",
        stage4b_status="none",
        hard_4c_confirmed=False,
        evidence_fields=("daesan_ncc_1_1mn_tpy_shutdown", "shutdown_duration_three_years", "support_package_over_2tn_krw", "capital_increase_1_2tn_krw", "50_50_equity_split"),
        red_flag_fields=("china_middle_east_oversupply", "spread_recovery_unconfirmed", "opm_fcf_unconfirmed", "debt_funding_cost_watch"),
        price_data_source="Reuters restructuring evidence",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="Daesan NCC 1.1M tpy shut for 3 years; support >2T KRW; capital increase 1.2T KRW",
        mfe_1d=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"daesan_ncc_capacity_mn_tpy": 1.1, "shutdown_duration_years": 3.0, "support_package_krw_trn": 2.0, "capital_increase_krw_trn": 1.2, "utility_cost_savings_krw_bn": 115.0, "rnd_funding_krw_bn": 26.0},
        score_price_alignment="false_positive_score",
        rerating_result="no_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Capacity shutdown and support are Stage 2 relief; spread, OPM and FCF recovery are required for Green.",
    ),
    Round221CaseCandidate(
        case_id="r4_loop9_sk_innovation_soil_refining_cycle",
        symbol="096770/010950",
        company_name="SK Innovation / S-Oil",
        primary_archetype=E2RArchetype.REFINING_OIL_SPREAD,
        secondary_archetypes=(E2RArchetype.REFINING_SPREAD_TURNAROUND_KOREA, E2RArchetype.COMMODITY_SPREAD_CYCLE_NOT_STRUCTURAL),
        case_type="cyclical_success",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 1, 28),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="refining_margin_rebound_is_cyclical_stage2_until_multi_quarter_margin_floor_fcf_deleveraging_and_capital_return",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("sk_q4_op_295bn_krw", "s_oil_q4_op_growth_91pct", "sk_q1_2026_op_2_2tn_krw", "beat_vs_lseg_estimate_57_1pct"),
        red_flag_fields=("analyst_forecast_miss_16pct", "sk_on_battery_loss_drag", "refining_margin_cycle", "geopolitical_supply_shock_risk"),
        price_data_source="Reuters reported financial/event anchors",
        reported_price_anchor="SK Innovation +0.4% vs KOSPI +1.3% on Q4 event",
        reported_return_anchor="Q4 OP 295B KRW, forecast miss -16%; Q1 2026 OP 2.2T KRW, +57.1% beat",
        mfe_1d=0.4,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"sk_q4_op_krw_bn": 295.0, "sk_q4_op_growth_pct": 67.6, "miss_vs_forecast_pct": -16.0, "relative_underperformance_pp": -0.9, "sk_on_loss_worsening_pct": 252.8, "sk_q1_2026_op_krw_trn": 2.2, "beat_vs_lseg_estimate_pct": 57.1, "s_oil_q4_op_growth_pct": 91.0},
        score_price_alignment="aligned",
        rerating_result="cyclical_rerating",
        stage_failure_type="stage2_watch_success",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Refining rebound is cyclical Stage 2; Green needs multi-quarter margin floor, FCF, deleveraging and battery loss control.",
    ),
    Round221CaseCandidate(
        case_id="r4_loop9_posco_minres_lithium_jv",
        symbol="005490",
        company_name="POSCO Holdings / MinRes lithium JV",
        primary_archetype=E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA,
        secondary_archetypes=(E2RArchetype.LITHIUM_CYCLE_OVERLAY, E2RArchetype.RARE_METALS_PRICE_FLOOR_OFFTAKE),
        case_type="success_candidate",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2025, 11, 11),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="lithium_resource_security_is_stage2_until_offtake_economics_downstream_margin_and_fcf",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("minres_lithium_jv_765mn_usd", "wodgina_mt_marion_indirect_15pct", "spodumene_concentrate_access"),
        red_flag_fields=("lithium_price_event", "downstream_margin_unconfirmed", "commodity_cycle_risk", "posco_stock_ohlc_unavailable"),
        price_data_source="Reuters commodity/transaction anchors",
        reported_price_anchor="POSCO stock OHLC unavailable; MinRes +10.8%",
        reported_return_anchor="MinRes +10.8%; spodumene >$6,000/t to ~$610/t then ~$880/t",
        mfe_1d=10.8,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"transaction_value_usd_mn": 765.0, "posco_indirect_stake_pct": 15.0, "spodumene_drawdown_peak_to_low_pct": -89.8, "spodumene_rebound_610_to_880_pct": 44.3, "spodumene_880_vs_peak_pct": -85.3},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="posco_stock_ohlc_unavailable_after_deep_search",
        notes="Lithium mine stake is Stage 2; Stage 3 requires offtake economics, downstream margin and FCF.",
    ),
    Round221CaseCandidate(
        case_id="r4_loop9_oci_non_china_polysilicon",
        symbol="010060",
        company_name="OCI Holdings",
        primary_archetype=E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION,
        secondary_archetypes=(E2RArchetype.POLYSILICON_REPORT_NOT_CONTRACT, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        stage1_date=date(2025, 6, 7),
        stage2_date=date(2025, 6, 7),
        stage3_date=None,
        stage4b_date=date(2026, 4, 14),
        stage4c_date=None,
        stage3_decision="non_china_polysilicon_capacity_is_stage2_until_confirmed_contract_volume_price_duration_margin_and_fcf",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("texas_solar_capacity_expansion_1_2bn_usd", "target_capacity_10gw_2027", "non_china_solar_supply_chain_option", "ai_data_center_power_demand"),
        red_flag_fields=("spacex_contract_unconfirmed_media_report", "capex_heavy_project_pre_revenue", "subsidy_uncertainty", "polysilicon_price_decline_risk"),
        price_data_source="FT/Reuters evidence anchors",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="$1.2B Texas expansion, 10GW by 2027; SpaceX report unconfirmed",
        mfe_1d=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"us_investment_usd_bn": 1.2, "target_capacity_gw": 10.0, "target_year": 2027.0, "spacex_contract_status": "unconfirmed media report", "spacex_solar_satellite_constellation": 1000000.0},
        score_price_alignment="unknown",
        rerating_result="unknown",
        stage_failure_type="stage2_watch_success",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium until contract terms, margin and FCF confirm.",
    ),
    Round221CaseCandidate(
        case_id="r4_loop9_poongsan_hanwha_mna_rumor_fade",
        symbol="103140",
        company_name="Poongsan",
        primary_archetype=E2RArchetype.COPPER_PROCESSING_PLUS_DEFENSE,
        secondary_archetypes=(E2RArchetype.EVENT_PREMIUM, E2RArchetype.DEFENSE_AMMO_EVENT_PREMIUM),
        case_type="event_premium",
        stage1_date=date(2026, 4, 3),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=date(2026, 4, 3),
        stage4c_date=date(2026, 4, 9),
        stage3_decision="mna_rumor_is_stage1_attention_until_transaction_order_margin_and_fcf_are_confirmed",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("hanwha_acquisition_report_1_5tn_krw", "ammunition_business", "copper_defense_optionality", "rumor_duration_six_days"),
        red_flag_fields=("mna_rumor_without_transaction", "unconfirmed_media_report", "transaction_dropped", "no_sale_plan"),
        price_data_source="Reuters M&A report/termination anchors",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="reported 1.5T KRW M&A rumor dropped after 6 calendar days",
        mfe_1d=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"reported_deal_value_krw_trn": 1.5, "reported_deal_value_usd_bn": 1.1, "rumor_duration_days": 6.0, "transaction_status": "not_decided_to_dropped_no_sale_plan"},
        score_price_alignment="price_moved_without_evidence",
        rerating_result="event_premium",
        stage_failure_type="false_yellow",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="M&A rumor faded in six days; Stage 3 requires confirmed transaction or copper/ammunition margin and FCF.",
    ),
)


def round221_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND221_CASE_CANDIDATES:
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
                "Round221 R4 Loop-9 materials/spread/strategic-resources price validation case. "
                "Calibration-only; not candidate-generation input."
            ),
            stage1_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "tariff" in field or "report" in field or "event" in field or "resource" in field or "rumor" in field
            ),
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(
                field
                for field in candidate.evidence_fields
                if "spread" in field or "offtake" in field or "fcf" in field or "capacity" in field or "contract" in field or "margin" in field
            ),
            stage4b_evidence=tuple(
                field
                for field in (*candidate.evidence_fields, *candidate.red_flag_fields)
                if "event" in field or "rumor" in field or "governance" in field or "unconfirmed" in field or "rally" in field
            ),
            stage4c_evidence=tuple(
                field
                for field in (*candidate.red_flag_fields, *candidate.evidence_fields)
                if "tariff" in field
                or "oversupply" in field
                or "dilution" in field
                or "dropped" in field
                or "decline" in field
                or "watch" in field
            ),
            must_have_fields=ROUND221_GREEN_REQUIRED_FIELDS,
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
                "actual_product_spread_delta": 5.0,
                "fcf_after_working_capital_delta": 5.0,
                "supply_discipline_confirmed_delta": 5.0,
                "capacity_shutdown_confirmed_delta": 4.0,
                "price_floor_or_offtake_delta": 5.0,
                "cost_curve_advantage_delta": 4.0,
                "tariff_resilience_delta": 4.0,
                "resource_security_with_downstream_margin_delta": 4.0,
                "commodity_price_up_only_delta": -5.0,
                "tariff_event_only_delta": -4.0,
                "restructuring_plan_without_margin_delta": -4.0,
                "policy_support_without_fcf_delta": -4.0,
                "tender_offer_or_governance_premium_delta": -5.0,
                "unconfirmed_media_report_delta": -5.0,
                "mna_rumor_without_transaction_delta": -5.0,
                "lithium_price_event_delta": -5.0,
                "refining_margin_geopolitical_shock_delta": -3.0,
                "capex_heavy_project_pre_revenue_delta": -4.0,
            },
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_spreads_offtakes_or_fcf",
                "do_not_treat_commodity_price_tariff_governance_policy_unconfirmed_media_or_mna_rumor_as_green",
                *ROUND221_GREEN_REQUIRED_FIELDS,
                *ROUND221_GREEN_FORBIDDEN_PATTERNS,
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
                price_data_available=(
                    candidate.stage4c_price_anchor is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round221_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND221_CASE_CANDIDATES:
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


def round221_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(adjustment.as_row() for adjustment in ROUND221_SCORE_ADJUSTMENTS)


def round221_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(row.as_row() for row in ROUND221_SHADOW_WEIGHT_ROWS)


def round221_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round221_price_validation": "true"} for field in ROUND221_PRICE_VALIDATION_FIELDS)


def round221_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round221_label": label, "canonical_archetype": canonical} for label, canonical in ROUND221_REQUIRED_TARGET_ALIASES.items())


def round221_summary() -> dict[str, int | bool | str]:
    cases = ROUND221_CASE_CANDIDATES
    return {
        "source_round": ROUND221_SOURCE_ROUND_PATH,
        "large_sector": ROUND221_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for case in cases if case.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if case.stage4b_status == "watch"),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "reported_price_anchor_count": sum(1 for case in cases if case.price_validation_status != "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND221_REQUIRED_TARGET_ALIASES),
        "shadow_weight_row_count": len(ROUND221_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
    }


def round221_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND221_SOURCE_ROUND_PATH,
        "large_sector": ROUND221_LARGE_SECTOR.value,
        "summary": round221_summary(),
        "target_aliases": dict(ROUND221_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND221_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND221_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND221_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND221_HARD_4C_GATES),
        "score_adjustments": list(round221_score_adjustment_rows()),
        "shadow_weights": list(round221_shadow_weight_rows()),
        "case_ids": [case.case_id for case in ROUND221_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round221_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_commodity_tariff_governance_policy_unconfirmed_media_or_mna_rumor_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round221_summary_markdown() -> str:
    summary = round221_summary()
    lines = [
        "# Round 221 R4 Loop 9 Materials Spread Strategic Resources Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
        f"- cyclical_success: {summary['cyclical_success_count']}",
        f"- event_premium: {summary['event_premium_count']}",
        f"- failed_rerating: {summary['failed_rerating_count']}",
        f"- 4B watch cases: {summary['stage4b_watch_count']}",
        f"- 4C watch cases: {summary['stage4c_watch_count']}",
        f"- hard_4c: {summary['hard_4c_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C-watch | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND221_CASE_CANDIDATES:
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
            "- 철강 관세는 한국 수출업체에는 4C-watch가 될 수 있다.",
            "- 고려아연은 전략광물 Stage 2 후보지만 governance/dilution/offtake/FCF 전 Green은 아니다.",
            "- 롯데케미칼 구조조정은 relief이지 spread/OPM/FCF 확인 전 Green이 아니다.",
            "- SK Innovation/S-Oil 정유 반등은 cyclical Stage 2다.",
            "- POSCO lithium JV와 OCI non-China polysilicon은 Stage 2 후보지만 commodity/capex/media-report risk가 남아 있다.",
            "- 풍산 M&A rumor는 6일 만에 fade된 event premium이다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round221_green_gate_review_markdown() -> str:
    lines = ["# Round 221 R4 Green Gate Review", "", "Do not apply these weights to production scoring yet.", "", "## Required Fields", ""]
    lines.extend(f"- {field}" for field in ROUND221_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND221_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND221_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `리튬 가격 반등`만 있으면 event premium이다. downstream margin과 FCF가 있어야 Stage 3 후보가 된다.",
            "- `M&A 보도`는 거래 확정 전까지 Stage 1 attention 또는 4B-watch다.",
            "- `구조조정 승인`은 Stage 2 relief다. spread, OPM, FCF 회복 전 Green은 아니다.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round221_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 221 R4 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND221_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND221_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | interpretation |", "|---|---|---|---|"])
    for case in ROUND221_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round221_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 221 R4 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, spreads, offtake, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND221_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND221_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round221_r4_loop9_reports(
    output_directory: str | Path = ROUND221_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND221_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND221_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round221_case_records(), cases_path),
        "audit": _write_json(round221_audit_payload(), audit_path),
        "summary": output / "round221_r4_loop9_price_validation_summary.md",
        "case_matrix": output / "round221_r4_loop9_case_matrix.csv",
        "target_aliases": output / "round221_r4_loop9_target_aliases.csv",
        "score_adjustments": output / "round221_r4_loop9_score_adjustments.csv",
        "shadow_weights": output / "round221_r4_loop9_shadow_weights.csv",
        "price_validation_fields": output / "round221_r4_loop9_price_validation_fields.csv",
        "green_gate_review": output / "round221_r4_loop9_green_gate_review.md",
        "price_validation_plan": output / "round221_r4_loop9_price_validation_plan.md",
        "stage4b_4c_review": output / "round221_r4_loop9_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round221_summary_markdown(), encoding="utf-8")
    _write_csv(round221_case_rows(), paths["case_matrix"])
    _write_csv(round221_target_alias_rows(), paths["target_aliases"])
    _write_csv(round221_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round221_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round221_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round221_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round221_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round221_stage4b_4c_review_markdown(), encoding="utf-8")
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
