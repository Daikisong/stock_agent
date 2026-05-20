"""Round-234 R4 Loop-10 materials/spread/strategic resources pack.

The pack converts ``docs/round/round_234.md`` into structured,
calibration-only case records. It does not change production scoring.

Easy example: a lithium price rebound can move a basket for one day, but R4
Stage 3-Green needs product spread, offtake, cost curve, FCF, and capex or
dilution risk to clear.
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


ROUND234_SOURCE_ROUND_PATH = "docs/round/round_234.md"
ROUND234_LARGE_SECTOR = Round10LargeSector.MATERIALS_SPREAD_STRATEGIC
ROUND234_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round234_r4_loop10_materials_spread_strategic_price_validation"
ROUND234_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r4_loop10_round234.jsonl"
ROUND234_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round234_r4_loop10_materials_spread_strategic_price_validation_audit.json"

ROUND234_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "STRATEGIC_MINERALS_SUPPLY_CHAIN": E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS.value,
    "CRITICAL_MINERALS_US_REFINERY": E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS.value,
    "GOVERNANCE_DILUTION_EVENT": E2RArchetype.GOVERNANCE_DILUTION_EVENT.value,
    "PETROCHEMICAL_RESTRUCTURING_KOREA": E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA.value,
    "REFINING_SPREAD_CYCLE": E2RArchetype.REFINING_OIL_SPREAD.value,
    "LITHIUM_RESOURCE_SECURITY": E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA.value,
    "LITHIUM_CYCLE_OVERLAY": E2RArchetype.LITHIUM_CYCLE_OVERLAY.value,
    "STEEL_POLICY_CAPEX_TARIFF_HEDGE": E2RArchetype.SPECIALTY_STEEL_US_LOCALIZATION_OPTION.value,
    "BUILDING_MATERIALS_DEMAND_CYCLE": E2RArchetype.BUILDING_MATERIALS_CYCLE.value,
    "BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK": E2RArchetype.CONTRACT_QUALITY_BREAK.value,
    "POLYSILICON_NON_CHINA_SUPPLY_OPTION": E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION.value,
    "COPPER_PROCESSING_PLUS_DEFENSE": E2RArchetype.COPPER_PROCESSING_PLUS_DEFENSE.value,
    "M_AND_A_OPTIONALITY_EVENT": E2RArchetype.EVENT_PREMIUM.value,
    "PRICE_ONLY_RALLY": E2RArchetype.PRICE_ONLY_RALLY.value,
    "EVENT_PREMIUM": E2RArchetype.EVENT_PREMIUM.value,
}

ROUND234_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
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

ROUND234_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "commodity_price_spike_only",
    "strategic_material_headline_only",
    "tender_offer_premium",
    "governance_battle_only",
    "policy_support_without_fcf",
    "unconfirmed_media_report",
    "mna_rumor_without_transaction",
    "restructuring_plan_without_margin",
    "lithium_or_polysilicon_price_event_only",
    "customer_name_contract_headline_without_calloff",
)

ROUND234_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "commodity_price_group_rally",
    "restructuring_expectation_multiple_expansion",
    "tender_offer_buyback_governance_battle_rally",
    "lithium_or_polysilicon_supply_discipline_event",
    "geopolitical_refining_margin_spike",
    "unconfirmed_customer_or_mna_report_rally",
    "strategic_minerals_headline_prices_before_offtake_fcf",
    "price_runs_before_spread_and_fcf",
)

ROUND234_HARD_4C_GATES: tuple[str, ...] = (
    "contract_value_collapse",
    "contract_cancellation",
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
    "policy_capex_funding_failure",
)

ROUND234_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "share_issue_vs_project_value_pct",
    "contract_value_drawdown_pct",
    "rumor_duration_days",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round234ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round234ShadowWeightRow:
    archetype: E2RArchetype
    product_spread: int
    fcf_after_wc: int
    supply_discipline: int
    capacity_shutdown: int
    offtake: int
    contract_quality: int
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
            "product_spread": _signed(self.product_spread),
            "fcf_after_wc": _signed(self.fcf_after_wc),
            "supply_discipline": _signed(self.supply_discipline),
            "capacity_shutdown": _signed(self.capacity_shutdown),
            "offtake": _signed(self.offtake),
            "contract_quality": _signed(self.contract_quality),
            "cost_curve": _signed(self.cost_curve),
            "tariff_resilience": _signed(self.tariff_resilience),
            "resource_security": _signed(self.resource_security),
            "event_penalty": _signed(self.event_penalty),
            "governance_redteam": _signed(self.governance_redteam),
            "4b_watch_sensitivity": _signed(self.stage4b_watch_sensitivity),
            "hard4c_sensitivity": _signed(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round234DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round234CaseCandidate:
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
    extra_price_metrics: Mapping[str, float | str | bool | list[str]]
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


ROUND234_SCORE_ADJUSTMENTS: tuple[Round234ScoreAdjustment, ...] = (
    Round234ScoreAdjustment("actual_product_spread", 5, "raise", "R4는 원자재 가격보다 제품 spread 확인이 먼저다."),
    Round234ScoreAdjustment("fcf_after_working_capital", 5, "raise", "재고와 운전자본 이후 FCF가 남아야 구조적이다."),
    Round234ScoreAdjustment("supply_discipline_confirmed", 5, "raise", "설비중단/공급규율이 확인되어야 spread 회복이 지속된다."),
    Round234ScoreAdjustment("capacity_shutdown_confirmed", 4, "raise", "Daesan NCC shutdown처럼 확정된 설비 조정은 Stage 2 relief다."),
    Round234ScoreAdjustment("price_floor_or_offtake", 5, "raise", "전략자원은 offtake/price floor가 있어야 commodity cycle과 분리된다."),
    Round234ScoreAdjustment("cost_curve_advantage", 4, "raise", "cost curve 우위가 있어야 가격 하락에도 FCF가 버틴다."),
    Round234ScoreAdjustment("strategic_customer_or_government_offtake", 4, "raise", "정부/전략 고객의 실제 offtake가 있으면 visibility가 강해진다."),
    Round234ScoreAdjustment("inventory_normalization", 4, "raise", "재고 축소는 spread 회복의 품질을 높인다."),
    Round234ScoreAdjustment("tariff_resilience", 4, "raise", "관세 환경에서 수출마진이 방어되는지 확인한다."),
    Round234ScoreAdjustment("resource_security_with_downstream_margin", 4, "raise", "resource security는 downstream margin과 연결될 때 강하다."),
    Round234ScoreAdjustment("contract_quality", 5, "raise", "소재 계약은 금액보다 call-off, volume, margin 변환이 중요하다."),
    Round234ScoreAdjustment("commodity_price_up_only", -5, "lower", "원자재 가격 상승만으로는 EPS/FCF 체급 변화를 증명하지 못한다."),
    Round234ScoreAdjustment("strategic_material_headline_only", -4, "lower", "전략광물 headline만으로 Green 금지다."),
    Round234ScoreAdjustment("governance_premium_only", -5, "lower", "경영권/공개매수 premium은 구조적 Stage 3와 분리한다."),
    Round234ScoreAdjustment("share_issue_dilution", -5, "lower", "대규모 신주발행과 dilution은 RedTeam 입력이다."),
    Round234ScoreAdjustment("restructuring_plan_without_margin", -4, "lower", "구조조정 계획은 margin/FCF 회복 전 Stage 2 watch다."),
    Round234ScoreAdjustment("policy_capex_without_funding", -5, "lower", "funding/margin 불명확한 정책 CAPEX는 false-positive 위험이다."),
    Round234ScoreAdjustment("mna_rumor_without_transaction", -5, "lower", "확정되지 않은 M&A rumor는 event premium이다."),
    Round234ScoreAdjustment("unconfirmed_media_report", -5, "lower", "미확정 고객 보도는 Green 근거가 아니다."),
    Round234ScoreAdjustment("lithium_price_event", -5, "lower", "리튬 가격 이벤트는 company-level margin/FCF 전 event premium이다."),
    Round234ScoreAdjustment("contract_headline_without_calloff", -5, "lower", "고객명과 계약금액 headline만으로 Green 금지다."),
    Round234ScoreAdjustment("capex_heavy_project_pre_revenue", -4, "lower", "상업가동 전 대형 CAPEX는 FCF/dilution risk가 크다."),
)


ROUND234_SHADOW_WEIGHT_ROWS: tuple[Round234ShadowWeightRow, ...] = (
    Round234ShadowWeightRow(E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS, 3, 4, 3, 0, 5, 4, 4, 2, 5, -3, 5, 5, 4, "Korea Zinc strategic minerals are Stage 2; governance/dilution blocks Green."),
    Round234ShadowWeightRow(E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA, 5, 5, 5, 5, 1, 2, 4, 0, 0, -3, 2, 3, 5, "Daesan shutdown is restructuring relief, not Green before spread/FCF."),
    Round234ShadowWeightRow(E2RArchetype.REFINING_OIL_SPREAD, 5, 4, 2, 0, 1, 2, 3, 0, 0, -3, 1, 4, 3, "Refining rebound is cyclical; battery drag and margin durability matter."),
    Round234ShadowWeightRow(E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA, 2, 4, 2, 0, 5, 3, 4, 0, 5, -5, 1, 4, 4, "POSCO lithium JV is resource-security Stage 2 with lithium-cycle risk."),
    Round234ShadowWeightRow(E2RArchetype.SPECIALTY_STEEL_US_LOCALIZATION_OPTION, 4, 5, 3, 0, 2, 2, 3, 5, 0, -5, 2, 4, 5, "Hyundai Steel policy capex can fail without funding and margin clarity."),
    Round234ShadowWeightRow(E2RArchetype.CONTRACT_QUALITY_BREAK, 2, 5, 1, 0, 5, 5, 3, 0, 0, 0, 1, 3, 5, "L&F Tesla contract collapse is hard 4C."),
    Round234ShadowWeightRow(E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION, 3, 4, 3, 0, 5, 3, 3, 2, 3, -5, 1, 5, 3, "OCI U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium."),
    Round234ShadowWeightRow(E2RArchetype.COPPER_PROCESSING_PLUS_DEFENSE, 4, 4, 2, 0, 3, 3, 3, 1, 0, -5, 2, 5, 3, "Poongsan M&A rumor faded; Green requires confirmed transaction or margin/FCF."),
    Round234ShadowWeightRow(E2RArchetype.EVENT_PREMIUM, 0, 0, 0, 0, 0, 0, 0, 0, 0, -5, 3, 5, 3, "M&A rumor without signed transaction should not become Green."),
)


ROUND234_DEEP_SUB_ARCHETYPES: tuple[Round234DeepSubArchetype, ...] = (
    Round234DeepSubArchetype("Strategic minerals", E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS, ("Korea Zinc", "antimony", "gallium", "germanium", "U.S. critical-minerals refinery", "data-center waste rare earths")),
    Round234DeepSubArchetype("Petrochemical restructuring", E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA, ("Lotte Chemical", "HD Hyundai Chemical", "Daesan NCC shutdown", "China Middle East oversupply")),
    Round234DeepSubArchetype("Refining spread", E2RArchetype.REFINING_OIL_SPREAD, ("SK Innovation", "S-Oil", "crack spread", "Middle East disruption", "battery-unit drag")),
    Round234DeepSubArchetype("Lithium resource security", E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA, ("POSCO Holdings", "MinRes", "Wodgina", "Mt Marion", "spodumene offtake")),
    Round234DeepSubArchetype("Steel policy capex", E2RArchetype.SPECIALTY_STEEL_US_LOCALIZATION_OPTION, ("Hyundai Steel", "Louisiana plant", "tariff hedge", "rebar demand weakness", "Chinese imports")),
    Round234DeepSubArchetype("Battery contract break", E2RArchetype.CONTRACT_QUALITY_BREAK, ("L&F", "Tesla 4680", "contract value collapse", "customer-name false Green prevention")),
    Round234DeepSubArchetype("Non-China polysilicon", E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION, ("OCI Holdings", "Texas expansion", "non-China polysilicon", "SpaceX unconfirmed report")),
    Round234DeepSubArchetype("Copper defense optionality", E2RArchetype.COPPER_PROCESSING_PLUS_DEFENSE, ("Poongsan", "copper processing", "ammunition optionality", "Hanwha acquisition rumor fade")),
)


ROUND234_CASE_CANDIDATES: tuple[Round234CaseCandidate, ...] = (
    Round234CaseCandidate(
        case_id="r4_loop10_korea_zinc_strategic_minerals_governance",
        symbol="010130",
        company_name="Korea Zinc",
        primary_archetype=E2RArchetype.RARE_METALS_STRATEGIC_MATERIALS,
        secondary_archetypes=(E2RArchetype.STRATEGIC_MATERIALS_WITH_GOVERNANCE_OVERLAY, E2RArchetype.GOVERNANCE_DILUTION_EVENT),
        case_type="success_candidate",
        stage1_date=date(2024, 9, 1),
        stage2_date=date(2026, 3, 12),
        stage3_date=None,
        stage4b_date=date(2026, 3, 12),
        stage4c_date=date(2025, 12, 16),
        stage3_decision="strategic_minerals_project_is_stage2_until_fid_offtake_margin_fcf_dilution_and_governance_clear",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("tennessee_critical_minerals_refinery_7_4bn_usd", "planned_output_540k_tons", "eleven_critical_minerals", "antimony_gallium_germanium", "rare_earth_data_center_waste_talks", "2025_op_1_2tn_krw"),
        red_flag_fields=("share_issue_1_9bn_usd", "share_issue_vs_project_value_25_7pct", "governance_battle", "injunction_event_minus_13pct", "offtake_fcf_unconfirmed"),
        price_data_source="Reuters critical-minerals / governance event anchors",
        reported_price_anchor="injunction -13%; court rejection relief +5%; YoungPoong -10.5%",
        reported_return_anchor="$7.4B project, 540k tons output, 11 critical minerals, 2025 OP 1.2T KRW",
        mfe_1d=5.0,
        mae_1d=-13.0,
        mae_1d_secondary=-10.5,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"us_smelter_project_value_usd_bn": 7.4, "planned_output_tons": 540000.0, "critical_minerals_count": 11.0, "target_margin_low_pct": 17.0, "target_margin_high_pct": 19.0, "planned_construction_start": "early_2027", "planned_operation_year": 2030.0, "operating_profit_2025_krw_trn": 1.2, "share_issue_usd_bn": 1.9, "share_issue_vs_project_value_pct": 25.7, "new_investor_stake_pct": 10.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_governance_watch",
        rerating_result="unknown",
        round_rerating_label="strategic_minerals_project_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_evidence_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Strategic minerals are Stage 2; dilution, governance, offtake and FCF must clear before Stage 3.",
    ),
    Round234CaseCandidate(
        case_id="r4_loop10_lotte_hd_petrochemical_restructuring",
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
        stage3_decision="restructuring_approval_is_relief_until_spread_opm_fcf_debt_and_funding_cost_confirm",
        stage4b_status="watch_if_chemical_basket_rerates_on_restructuring_only",
        hard_4c_confirmed=False,
        evidence_fields=("daesan_ncc_1_1mn_tpy_shutdown", "shutdown_duration_three_years", "support_package_over_2tn_krw", "capital_increase_1_2tn_krw", "national_ncc_capacity_cut_3_7mn_tpy"),
        red_flag_fields=("china_middle_east_oversupply", "spread_recovery_unconfirmed", "opm_fcf_unconfirmed", "debt_funding_cost_watch", "capacity_cut_insufficient_risk"),
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
        extra_price_metrics={"daesan_ncc_capacity_mn_tpy": 1.1, "shutdown_duration_years": 3.0, "government_support_package_krw_trn": 2.0, "capital_increase_krw_trn": 1.2, "utility_cost_savings_krw_bn": 115.0, "rnd_funding_krw_bn": 26.0, "equity_split_after_restructuring": "50:50", "target_capacity_cut_national_mn_tpy": 3.7, "industry_capacity_cut_goal_pct": 25.0},
        score_price_alignment="false_positive_score",
        round_alignment_label="failed_rerating_then_restructuring_watch",
        rerating_result="no_rerating",
        round_rerating_label="petrochemical_restructuring_relief",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_relief_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Capacity shutdown/support is Stage 2 relief; spread, OPM and FCF recovery required for Green.",
    ),
    Round234CaseCandidate(
        case_id="r4_loop10_sk_innovation_soil_refining_cycle",
        symbol="096770/010950",
        company_name="SK Innovation / S-Oil",
        primary_archetype=E2RArchetype.REFINING_OIL_SPREAD,
        secondary_archetypes=(E2RArchetype.REFINING_SPREAD_TURNAROUND_KOREA, E2RArchetype.REFINING_PETCHEM_MIX_DRAG),
        case_type="cyclical_success",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2026, 5, 13),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="refining_margin_rebound_is_cyclical_stage2_until_multi_quarter_margin_floor_fcf_deleveraging_and_battery_drag_control",
        stage4b_status="watch_if_geopolitical_margin_spike_prices_before_margin_floor",
        hard_4c_confirmed=False,
        evidence_fields=("q3_2025_op_573bn_krw", "q1_2026_op_2_2tn_krw", "q1_beat_vs_estimate_57_1pct", "refining_margin_recovery"),
        red_flag_fields=("q4_forecast_miss_16pct", "sk_on_loss_worsening_252_8pct", "battery_unit_drag", "refining_margin_cycle"),
        price_data_source="Reuters refining-cycle financial and price anchors",
        reported_price_anchor="Q3 +0.2% vs KOSPI +0.3%; Q4 +0.4% vs KOSPI +1.3%",
        reported_return_anchor="Q1 2026 OP 2.2T KRW vs 1.4T estimate; but battery drag persists",
        mfe_1d=0.4,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"q3_2025_op_krw_bn": 573.0, "q3_2024_op_krw_bn": -423.0, "q3_profit_swing_krw_bn": 996.0, "q3_estimate_krw_bn": 304.0, "q3_beat_vs_estimate_pct": 88.5, "q3_revenue_growth_pct": 16.3, "q3_event_return_pct": 0.2, "kospi_q3_context_pct": 0.3, "q4_2025_op_krw_bn": 295.0, "q4_forecast_krw_bn": 351.0, "q4_miss_vs_forecast_pct": -16.0, "q4_relative_underperformance_pp": -0.9, "sk_on_q4_loss_krw_bn": 441.0, "sk_on_loss_worsening_pct": 252.8, "q1_2026_op_krw_trn": 2.2, "q1_profit_swing_krw_trn": 2.23, "q1_beat_vs_estimate_pct": 57.1},
        score_price_alignment="aligned",
        round_alignment_label="cyclical_success",
        rerating_result="cyclical_rerating",
        round_rerating_label="refining_cycle_rebound_with_battery_drag",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="cyclical_stage2_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Refining rebound is cyclical; Stage 3 requires multi-quarter margin floor, FCF, deleveraging and battery-loss control.",
    ),
    Round234CaseCandidate(
        case_id="r4_loop10_posco_minres_lithium_jv",
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
        stage3_decision="resource_security_is_stage2_until_lithium_hydroxide_margin_offtake_economics_and_downstream_fcf_confirm",
        stage4b_status="watch_if_lithium_price_rebound_prices_before_margin",
        hard_4c_confirmed=False,
        evidence_fields=("minres_lithium_jv_765mn_usd", "wodgina_mt_marion_indirect_15pct", "spodumene_concentrate_access"),
        red_flag_fields=("lithium_price_cycle", "downstream_margin_unconfirmed", "posco_stock_ohlc_unavailable", "commodity_rebound_from_low_base"),
        price_data_source="Reuters lithium transaction / commodity anchors",
        reported_price_anchor="POSCO stock OHLC unavailable; MinRes +10.8%",
        reported_return_anchor="$765M transaction, indirect 15% Wodgina/Mt Marion, spodumene still -85%+ vs peak",
        mfe_1d=10.8,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"transaction_value_usd_mn": 765.0, "posco_indirect_stake_pct": 15.0, "minres_event_mfe_pct": 10.8, "spodumene_peak_2022_usd_per_t": 6000.0, "spodumene_low_2025_june_usd_per_t": 610.0, "spodumene_drawdown_peak_to_low_pct": -89.8, "spodumene_rebound_610_to_880_pct": 44.3, "spodumene_880_vs_peak_pct": -85.3},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_cyclical_watch",
        rerating_result="unknown",
        round_rerating_label="resource_security_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="resource_security_stage2_not_green",
        price_validation_status="posco_stock_ohlc_unavailable_after_deep_search",
        notes="Lithium mine stake is Stage 2; Stage 3 requires offtake economics, downstream margin and FCF.",
    ),
    Round234CaseCandidate(
        case_id="r4_loop10_hyundai_steel_policy_capex_rebar_4c",
        symbol="004020",
        company_name="Hyundai Steel",
        primary_archetype=E2RArchetype.SPECIALTY_STEEL_US_LOCALIZATION_OPTION,
        secondary_archetypes=(E2RArchetype.BUILDING_MATERIALS_CYCLE, E2RArchetype.STEEL_EXPORT_TARIFF_4C),
        case_type="failed_rerating",
        stage1_date=date(2024, 6, 21),
        stage2_date=date(2025, 3, 25),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 4, 22),
        stage3_decision="policy_capex_tariff_hedge_failed_without_funding_margin_and_rebar_demand_confirmation",
        stage4b_status="4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("us_louisiana_steel_plant_5_8bn_usd", "annual_capacity_2_7mn_tonnes", "tariff_hedge_narrative", "announcement_initial_plus_5pct"),
        red_flag_fields=("announcement_reversal_minus_4_4pct", "post_announcement_drawdown_21_2pct", "funding_plan_unclear", "net_profit_forecast_cut_73pct", "rebar_price_decline_10pct", "weak_domestic_construction_demand"),
        price_data_source="Reuters / MarketWatch capex and weak-demand anchors",
        reported_price_anchor="initial +5% then -4.4%; after announcement -21.2%",
        reported_return_anchor="$5.8B-$6.0B Louisiana plant, 2.7M tpy capacity, NP forecast -73%",
        mfe_1d=5.0,
        mae_1d=-4.4,
        mae_1d_secondary=-21.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=29000.0,
        peak_price_anchor=None,
        extra_price_metrics={"us_plant_investment_usd_bn_low": 5.8, "us_plant_investment_usd_bn_high": 6.0, "us_plant_capacity_mn_tpy": 2.7, "post_announcement_drawdown_pct": -21.2, "posco_holdings_same_period_pct": -18.3, "benchmark_same_period_pct": -5.5, "relative_underperformance_vs_benchmark_pp": -15.7, "funding_plan": "50pct_borrowing_rest_unclear_possible_posco_equity", "net_profit_forecast_2024_krw_bn": 215.0, "net_profit_forecast_cut_pct": -73.0, "implied_prior_net_profit_forecast_krw_bn": 796.3, "rebar_price_expected_decline_pct": -10.0, "weak_demand_event_price_krw": 29000.0, "weak_demand_event_mae_pct": -1.2},
        score_price_alignment="false_positive_score",
        round_alignment_label="false_positive_score_prevention",
        rerating_result="no_rerating",
        round_rerating_label="policy_capex_without_funding_failed",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4C_watch",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Tariff-hedge capex and weak rebar demand block Green; funding/margin clarity required.",
    ),
    Round234CaseCandidate(
        case_id="r4_loop10_lnf_tesla_cathode_contract_hard_4c",
        symbol="066970",
        company_name="L&F",
        primary_archetype=E2RArchetype.CONTRACT_QUALITY_BREAK,
        secondary_archetypes=(E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C, E2RArchetype.CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK),
        case_type="4c_thesis_break",
        stage1_date=date(2023, 1, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 29),
        stage3_decision="tesla_customer_name_and_contract_value_headline_failed_after_actual_contract_value_collapse",
        stage4b_status="hard_4C",
        hard_4c_confirmed=True,
        evidence_fields=("tesla_4680_high_nickel_cathode_supply_deal", "initial_contract_value_2_9bn_usd", "contract_period_2024_2025"),
        red_flag_fields=("contract_value_collapse_to_7386_usd", "contract_value_drawdown_99_999745pct", "4680_yield_issue", "ev_demand_slowdown", "cybertruck_demand_disappointment"),
        price_data_source="Reuters contract-value collapse anchor",
        reported_price_anchor="stock OHLC unavailable; contract value $2.9B -> $7,386",
        reported_return_anchor="Tesla cathode deal value collapsed by about -99.999745%",
        mfe_1d=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"initial_contract_value_usd_bn": 2.9, "revised_contract_value_usd": 7386.0, "contract_value_drawdown_pct": -99.999745, "contract_period": "2024-2025", "product": "high-nickel cathode materials for Tesla 4680 cells", "reason_context": ["4680_yield_issue", "EV_demand_slowdown", "Cybertruck_demand_disappointment"]},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="battery_material_contract_quality_failure",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C",
        price_validation_status="reported_contract_anchor_not_full_ohlc",
        notes="Customer name and contract headline cannot be Green without actual call-off, volume and margin conversion.",
    ),
    Round234CaseCandidate(
        case_id="r4_loop10_oci_non_china_polysilicon_spacex_watch",
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
        stage3_decision="non_china_polysilicon_capacity_is_stage2_but_spacex_report_is_unconfirmed_event_premium",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("texas_plant_capacity_expansion_1_2bn_usd", "target_capacity_10gw_by_2027", "non_china_solar_supply_chain", "us_solar_cell_capacity"),
        red_flag_fields=("spacex_supply_talk_unconfirmed_media_report", "capex_heavy_project_pre_revenue", "confirmed_customer_contract_unavailable", "margin_fcf_unconfirmed"),
        price_data_source="FT / Reuters capacity and media-report anchors",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="$1.2B Texas expansion to 10GW by 2027; SpaceX report unconfirmed",
        mfe_1d=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"us_investment_usd_bn": 1.2, "target_capacity_gw": 10.0, "target_year": 2027.0, "spacex_contract_status": "unconfirmed_media_report", "spacex_planned_satellite_constellation": 1000000.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_event_premium",
        rerating_result="unknown",
        round_rerating_label="non_China_polysilicon_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_evidence_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium until contract terms, margin and FCF confirm.",
    ),
    Round234CaseCandidate(
        case_id="r4_loop10_poongsan_hanwha_mna_rumor_fade",
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
        stage3_decision="mna_optionality_is_stage1_attention_until_transaction_financing_eps_accretion_and_integration_confirm",
        stage4b_status="watch",
        hard_4c_confirmed=False,
        evidence_fields=("hanwha_acquisition_report_1_5tn_krw", "ammunition_business", "copper_defense_optionality", "rumor_duration_six_days"),
        red_flag_fields=("mna_rumor_without_transaction", "unconfirmed_media_report", "transaction_dropped", "no_sale_plan"),
        price_data_source="Reuters M&A report / termination anchors",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="reported 1.5T KRW / $1.1B M&A rumor dropped after 6 calendar days",
        mfe_1d=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        peak_price_anchor=None,
        extra_price_metrics={"reported_deal_value_krw_trn": 1.5, "reported_deal_value_usd_bn": 1.1, "rumor_date": "2026-04-03", "termination_date": "2026-04-09", "rumor_duration_days": 6.0, "transaction_status": "not_decided_to_dropped_no_sale_plan"},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium",
        rerating_result="event_premium",
        round_rerating_label="copper_defense_M&A_optionality_fade",
        stage_failure_type="false_yellow",
        round_stage_failure_label="stage1_attention_only",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="M&A rumor faded in six days; Stage 3 requires confirmed transaction or copper/ammunition margin and FCF.",
    ),
)


def round234_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND234_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND234_LARGE_SECTOR.value,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round234 R4 Loop-10 materials/spread/strategic-resources price validation case. "
                "Calibration-only; not candidate-generation input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(token in field for token in ("spread", "offtake", "fcf", "capacity", "contract", "margin", "output"))),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field for token in ("event", "rumor", "governance", "unconfirmed", "rally", "headline"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field for token in ("collapse", "drawdown", "dilution", "demand", "failure", "weak", "oversupply", "dropped", "unclear", "unconfirmed"))),
            must_have_fields=ROUND234_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND234_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_spreads_offtakes_or_fcf",
                "do_not_treat_commodity_tariff_governance_policy_unconfirmed_media_or_mna_rumor_as_green",
                *ROUND234_GREEN_REQUIRED_FIELDS,
                *ROUND234_GREEN_FORBIDDEN_PATTERNS,
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
                    candidate.stage2_price_anchor is not None
                    or candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                    or candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                    or candidate.mae_1d_secondary is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round234_case_rows() -> tuple[dict[str, str], ...]:
    rows: list[dict[str, str]] = []
    for candidate in ROUND234_CASE_CANDIDATES:
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


def round234_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND234_SCORE_ADJUSTMENTS)


def round234_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND234_SHADOW_WEIGHT_ROWS)


def round234_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND234_DEEP_SUB_ARCHETYPES)


def round234_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round234_price_validation": "true"} for field in ROUND234_PRICE_VALIDATION_FIELDS)


def round234_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round234_label": label, "canonical_archetype": canonical} for label, canonical in ROUND234_REQUIRED_TARGET_ALIASES.items())


def round234_summary() -> dict[str, int | bool | str]:
    cases = ROUND234_CASE_CANDIDATES
    return {
        "source_round": ROUND234_SOURCE_ROUND_PATH,
        "large_sector": ROUND234_LARGE_SECTOR.value,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "cyclical_success_count": sum(1 for case in cases if case.case_type == "cyclical_success"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "watch" in case.stage4b_status),
        "stage4c_watch_count": sum(1 for case in cases if case.stage4c_date is not None and not case.hard_4c_confirmed),
        "reported_price_anchor_count": sum(1 for case in cases if case.price_validation_status != "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND234_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND234_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND234_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
    }


def round234_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND234_SOURCE_ROUND_PATH,
        "large_sector": ROUND234_LARGE_SECTOR.value,
        "summary": round234_summary(),
        "target_aliases": dict(ROUND234_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND234_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND234_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND234_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND234_HARD_4C_GATES),
        "score_adjustments": list(round234_score_adjustment_rows()),
        "shadow_weights": list(round234_shadow_weight_rows()),
        "deep_sub_archetypes": list(round234_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND234_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round234_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_commodity_tariff_governance_policy_unconfirmed_media_or_mna_rumor_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round234_summary_markdown() -> str:
    summary = round234_summary()
    lines = [
        "# Round 234 R4 Loop 10 Materials Spread Strategic Resources Price Validation",
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
        f"- hard_4c: {summary['hard_4c_case_count']}",
        f"- Stage 3 dated cases: {summary['stage3_case_count']}",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "",
        "## Case Matrix",
        "",
        "| case | company | type | Stage 2 | Stage 3 | 4B | 4C | alignment | note |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for case in ROUND234_CASE_CANDIDATES:
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
            "- Korea Zinc is strategic-minerals Stage 2, but governance/dilution/offtake/FCF block Green.",
            "- Lotte Chemical restructuring is relief, not Green before spread, OPM and FCF recovery.",
            "- SK Innovation / S-Oil refining rebound is cyclical Stage 2 because battery drag and margin durability remain.",
            "- POSCO lithium JV is resource-security Stage 2, but lithium cycle and downstream margin still matter.",
            "- Hyundai Steel is false-positive prevention for policy CAPEX without funding and margin clarity.",
            "- L&F is the hard 4C anchor: customer name and contract headline failed after value collapse.",
            "- OCI and Poongsan separate real capacity/options from unconfirmed media or M&A event premium.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round234_green_gate_review_markdown() -> str:
    lines = [
        "# Round 234 R4 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R4 Stage 3-Green is not `strategic mineral`, `restructuring`, `lithium`, `tariff hedge`, or `M&A optionality`. It requires spread, offtake, cost curve, FCF, and risk clearance.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND234_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND234_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND234_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `lithium price rebound` is event premium until downstream margin and FCF confirm.",
            "- `M&A rumor` is Stage 1 attention or 4B-watch until a signed transaction exists.",
            "- `Tesla customer name` is not Green if actual contract value collapses.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round234_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 234 R4 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND234_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND234_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | interpretation |", "|---|---|---|---|"])
    for case in ROUND234_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round234_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 234 R4 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, spreads, offtake, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND234_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND234_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round234_r4_loop10_reports(
    output_directory: str | Path = ROUND234_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND234_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND234_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round234_case_records(), cases_path),
        "audit": _write_json(round234_audit_payload(), audit_path),
        "summary": output / "round234_r4_loop10_price_validation_summary.md",
        "case_matrix": output / "round234_r4_loop10_case_matrix.csv",
        "target_aliases": output / "round234_r4_loop10_target_aliases.csv",
        "score_adjustments": output / "round234_r4_loop10_score_adjustments.csv",
        "shadow_weights": output / "round234_r4_loop10_shadow_weights.csv",
        "deep_sub_archetypes": output / "round234_r4_loop10_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round234_r4_loop10_price_validation_fields.csv",
        "green_gate_review": output / "round234_r4_loop10_green_gate_review.md",
        "price_validation_plan": output / "round234_r4_loop10_price_validation_plan.md",
        "stage4b_4c_review": output / "round234_r4_loop10_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round234_summary_markdown(), encoding="utf-8")
    _write_csv(round234_case_rows(), paths["case_matrix"])
    _write_csv(round234_target_alias_rows(), paths["target_aliases"])
    _write_csv(round234_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round234_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round234_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round234_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round234_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round234_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round234_stage4b_4c_review_markdown(), encoding="utf-8")
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
