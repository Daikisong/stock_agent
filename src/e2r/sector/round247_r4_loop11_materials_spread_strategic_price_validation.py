"""Round-247 R4 Loop-11 materials/spread/strategic-resources pack.

This module converts ``docs/round/round_247.md`` into structured,
calibration-only case-library records and reports. It does not change
production scoring or candidate generation.

Easy example: a non-China polysilicon media report can move attention, but
R4 Stage 3-Green still needs confirmed offtake, product spread, margin, FCF,
and governance or tariff risks to clear.
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


ROUND247_SOURCE_ROUND_PATH = "docs/round/round_247.md"
ROUND247_ROUND_ID = "round_175"
ROUND247_LARGE_SECTOR = Round10LargeSector.MATERIALS_SPREAD_STRATEGIC.value
ROUND247_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round247_r4_loop11_materials_spread_strategic_price_validation"
ROUND247_DEFAULT_CASES_PATH = "data/e2r_case_library/cases_r4_loop11_round247.jsonl"
ROUND247_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round247_r4_loop11_materials_spread_strategic_price_validation_audit.json"

ROUND247_REQUIRED_TARGET_ALIASES: Mapping[str, str] = {
    "CRITICAL_MINERALS_SUPPLY_CHAIN": E2RArchetype.CRITICAL_MINERALS_SUPPLY_CHAIN.value,
    "STRATEGIC_METALS_DILUTION_GOVERNANCE": E2RArchetype.STRATEGIC_METALS_DILUTION_GOVERNANCE.value,
    "PETROCHEMICAL_CAPACITY_RESTRUCTURING": E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING.value,
    "STANDALONE_NCC_CREDIT_BREAK": E2RArchetype.STANDALONE_NCC_CREDIT_BREAK.value,
    "STEEL_ANTIDUMPING_POLICY_RELIEF": E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF.value,
    "STEEL_TARIFF_EXPORT_RISK": E2RArchetype.STEEL_TARIFF_EXPORT_RISK.value,
    "CATHODE_SUPPLY_CHAIN_DERISKING": E2RArchetype.CATHODE_SUPPLY_CHAIN_DERISKING.value,
    "LITHIUM_RESOURCE_SECURITY": E2RArchetype.LITHIUM_RESOURCE_SECURITY.value,
    "NON_CHINA_POLYSILICON_OPTIONALITY": E2RArchetype.NON_CHINA_POLYSILICON_OPTIONALITY.value,
    "BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK": E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK.value,
    "COMMODITY_PRICE_EVENT_PREMIUM": E2RArchetype.COMMODITY_PRICE_EVENT_PREMIUM.value,
}

ROUND247_GREEN_REQUIRED_FIELDS: tuple[str, ...] = (
    "product_spread_confirmed",
    "cost_curve_advantage",
    "supply_discipline_or_capacity_shutdown_confirmed",
    "offtake_price_floor_or_take_or_pay",
    "fcf_after_working_capital",
    "contract_quality_confirmed",
    "china_tariff_sanction_governance_risk_passed",
    "capex_burden_and_dilution_risk_passed",
    "price_path_after_evidence",
)

ROUND247_GREEN_FORBIDDEN_PATTERNS: tuple[str, ...] = (
    "commodity_price_spike_only",
    "strategic_material_headline_only",
    "policy_relief_only",
    "unconfirmed_media_report",
    "restructuring_plan_only",
    "customer_name_only_material_contract",
    "resource_deal_without_offtake",
    "governance_dilution_unresolved",
)

ROUND247_STAGE4B_WATCH_TRIGGERS: tuple[str, ...] = (
    "commodity_price_rebound_group_rally",
    "strategic_mineral_headline_price_first",
    "anti_dumping_or_tariff_relief_rally",
    "petrochemical_restructuring_expectation_rally",
    "unconfirmed_customer_media_report_rally",
    "lithium_resource_security_price_first",
    "governance_fight_or_share_issue_price_driver",
)

ROUND247_HARD_4C_GATES: tuple[str, ...] = (
    "contract_value_collapse",
    "contract_cancellation",
    "spread_reversal",
    "china_oversupply",
    "standalone_cracker_credit_break",
    "inventory_build",
    "ncc_shutdown_from_distress",
    "share_issuance_or_governance_abuse",
    "tariff_shock_causing_export_margin_damage",
    "unconfirmed_deal_failure",
    "resource_project_write_down",
    "offtake_failure",
    "fcf_deterioration",
)

ROUND247_PRICE_VALIDATION_FIELDS: tuple[str, ...] = (
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
    "mae_1d_secondary",
    "project_or_contract_value_anchor",
    "spread_or_capacity_anchor",
    "governance_or_tariff_anchor",
    "price_validation_status",
)


@dataclass(frozen=True)
class Round247ScoreAdjustment:
    axis: str
    points: int
    direction: str
    reason: str

    def as_row(self) -> dict[str, str]:
        return {"axis": self.axis, "points": str(self.points), "direction": self.direction, "reason": self.reason}


@dataclass(frozen=True)
class Round247ShadowWeightRow:
    archetype: E2RArchetype
    product_spread: int
    cost_curve: int
    offtake_quality: int
    contract_quality: int
    fcf_after_wc: int
    supply_discipline: int
    capacity_shutdown: int
    china_exposure_reduction: int
    governance_cleanliness: int
    event_penalty: int
    stage4b_watch_sensitivity: int
    hard4c_sensitivity: int
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "archetype": self.archetype.value,
            "product_spread": _signed(self.product_spread),
            "cost_curve": _signed(self.cost_curve),
            "offtake_quality": _signed(self.offtake_quality),
            "contract_quality": _signed(self.contract_quality),
            "fcf_after_wc": _signed(self.fcf_after_wc),
            "supply_discipline": _signed(self.supply_discipline),
            "capacity_shutdown": _signed(self.capacity_shutdown),
            "china_exposure_reduction": _signed(self.china_exposure_reduction),
            "governance_cleanliness": _signed(self.governance_cleanliness),
            "event_penalty": _signed(self.event_penalty),
            "4b_watch_sensitivity": _signed(self.stage4b_watch_sensitivity),
            "hard_4c_sensitivity": _signed(self.hard4c_sensitivity),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class Round247DeepSubArchetype:
    category: str
    primary_archetype: E2RArchetype
    terms: tuple[str, ...]

    def as_row(self) -> dict[str, str]:
        return {"category": self.category, "primary_archetype": self.primary_archetype.value, "terms": "|".join(self.terms)}


@dataclass(frozen=True)
class Round247CaseCandidate:
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
    mae_1d_secondary: float | None
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


ROUND247_SCORE_ADJUSTMENTS: tuple[Round247ScoreAdjustment, ...] = (
    Round247ScoreAdjustment("product_spread", 5, "raise", "R4는 원자재 가격보다 제품 spread 확인이 먼저다."),
    Round247ScoreAdjustment("cost_curve_advantage", 5, "raise", "가격 하락에도 FCF가 버티려면 cost curve 우위가 필요하다."),
    Round247ScoreAdjustment("offtake_quality", 5, "raise", "전략자원은 offtake, price floor, take-or-pay가 있어야 cycle과 분리된다."),
    Round247ScoreAdjustment("contract_quality", 5, "raise", "소재 계약은 고객명보다 call-off, volume, margin 변환이 중요하다."),
    Round247ScoreAdjustment("FCF_after_working_capital", 5, "raise", "재고와 운전자본 이후 현금흐름이 남아야 구조적이다."),
    Round247ScoreAdjustment("supply_discipline_confirmed", 5, "raise", "설비중단과 공급규율은 spread 지속성을 높인다."),
    Round247ScoreAdjustment("capacity_shutdown_confirmed", 4, "raise", "Daesan NCC shutdown처럼 확정된 설비 조정은 Stage 2 relief다."),
    Round247ScoreAdjustment("China_exposure_reduction", 4, "raise", "중국 공급망 의존 완화는 Stage 2 품질을 높인다."),
    Round247ScoreAdjustment("resource_security_with_downstream_margin", 4, "raise", "resource security는 downstream margin과 연결될 때 강하다."),
    Round247ScoreAdjustment("governance_cleanliness", 4, "raise", "전략광물 프로젝트도 dilution/governance가 깨끗해야 Green 후보가 된다."),
    Round247ScoreAdjustment("commodity_price_up_only", -5, "lower", "가격 상승만으로 EPS/FCF 체급 변화를 증명하지 못한다."),
    Round247ScoreAdjustment("strategic_material_headline_only", -5, "lower", "전략광물 headline만으로 Green 금지다."),
    Round247ScoreAdjustment("policy_relief_only", -5, "lower", "정책 relief는 spread/FCF 확인 전 event premium이다."),
    Round247ScoreAdjustment("unconfirmed_media_report", -5, "lower", "미확정 고객 보도는 Stage 3 근거가 아니다."),
    Round247ScoreAdjustment("restructuring_plan_without_margin", -4, "lower", "구조조정 계획은 margin 회복 전 Stage 2 watch다."),
    Round247ScoreAdjustment("capacity_cut_without_spread_recovery", -4, "lower", "capacity cut만으로 petrochemical Green을 만들 수 없다."),
    Round247ScoreAdjustment("contract_headline_without_calloff", -5, "lower", "실제 call-off 없는 계약 headline은 L&F hard 4C의 반례다."),
    Round247ScoreAdjustment("customer_name_without_volume", -5, "lower", "고객명은 volume/margin 전환 전까지 visibility가 아니다."),
    Round247ScoreAdjustment("governance_dilution_risk", -5, "lower", "share issuance와 control fight는 RedTeam 입력이다."),
    Round247ScoreAdjustment("China_customer_or_supply_chain_concentration", -4, "lower", "중국 고객/공급망 집중은 tariff/sanction risk를 키운다."),
)


ROUND247_SHADOW_WEIGHT_ROWS: tuple[Round247ShadowWeightRow, ...] = (
    Round247ShadowWeightRow(E2RArchetype.CRITICAL_MINERALS_SUPPLY_CHAIN, 3, 5, 5, 4, 5, 3, 0, 4, 4, -3, 5, 4, "Korea Zinc strategic minerals are Stage 2 but governance/dilution blocks Green."),
    Round247ShadowWeightRow(E2RArchetype.STRATEGIC_METALS_DILUTION_GOVERNANCE, 2, 4, 4, 3, 5, 2, 0, 3, 5, -5, 5, 5, "Share issuance/control fight requires governance RedTeam."),
    Round247ShadowWeightRow(E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING, 5, 4, 1, 2, 5, 5, 5, 0, 3, -3, 3, 5, "Restructuring relief requires spread/OPM/FCF before Green."),
    Round247ShadowWeightRow(E2RArchetype.STANDALONE_NCC_CREDIT_BREAK, 5, 3, 0, 0, 5, 5, 5, 0, 3, 0, 3, 5, "YNCC weak financials and shutdown risk are 4C-watch."),
    Round247ShadowWeightRow(E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF, 5, 3, 1, 2, 4, 3, 0, 0, 3, -3, 4, 4, "Anti-dumping tariff is Stage 2 relief, not Green before spread/FCF."),
    Round247ShadowWeightRow(E2RArchetype.STEEL_TARIFF_EXPORT_RISK, 4, 3, 1, 2, 4, 2, 0, 0, 3, -4, 4, 5, "U.S./Vietnam tariff risk offsets domestic relief."),
    Round247ShadowWeightRow(E2RArchetype.CATHODE_SUPPLY_CHAIN_DERISKING, 3, 3, 5, 4, 5, 2, 0, 5, 3, -2, 3, 4, "LG Chem/Toyota reduces China exposure but needs offtake and margin."),
    Round247ShadowWeightRow(E2RArchetype.LITHIUM_RESOURCE_SECURITY, 2, 4, 5, 3, 5, 2, 0, 2, 3, -5, 4, 4, "POSCO lithium JV is resource-security Stage 2 but lithium cycle risk remains."),
    Round247ShadowWeightRow(E2RArchetype.NON_CHINA_POLYSILICON_OPTIONALITY, 4, 3, 5, 3, 5, 3, 0, 5, 3, -5, 5, 4, "OCI U.S. expansion is Stage 2; SpaceX report is unconfirmed."),
    Round247ShadowWeightRow(E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK, 1, 2, 5, 5, 5, 0, 0, 1, 3, 0, 3, 5, "L&F Tesla contract collapse is hard 4C."),
)


ROUND247_DEEP_SUB_ARCHETYPES: tuple[Round247DeepSubArchetype, ...] = (
    Round247DeepSubArchetype("Strategic minerals", E2RArchetype.CRITICAL_MINERALS_SUPPLY_CHAIN, ("Korea Zinc", "antimony", "gallium", "germanium", "Tennessee smelter", "data-center waste rare earths")),
    Round247DeepSubArchetype("Strategic metals governance", E2RArchetype.STRATEGIC_METALS_DILUTION_GOVERNANCE, ("MBK", "YoungPoong", "share issuance", "injunction", "control battle")),
    Round247DeepSubArchetype("Petrochemical restructuring", E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING, ("Lotte Chemical", "HD Hyundai Chemical", "Daesan NCC shutdown", "China/Middle East oversupply")),
    Round247DeepSubArchetype("Standalone NCC credit break", E2RArchetype.STANDALONE_NCC_CREDIT_BREAK, ("YNCC", "Yeochun NCC", "standalone cracker", "debt-to-equity 249%", "No.3 cracker shutdown")),
    Round247DeepSubArchetype("Steel policy two-sided risk", E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF, ("Hyundai Steel", "POSCO Holdings", "Chinese steel plate anti-dumping", "U.S. tariff threat")),
    Round247DeepSubArchetype("Cathode derisking", E2RArchetype.CATHODE_SUPPLY_CHAIN_DERISKING, ("LG Chem", "Toyota Tsusho", "Huayou Cobalt", "China exposure reduction")),
    Round247DeepSubArchetype("Lithium resource security", E2RArchetype.LITHIUM_RESOURCE_SECURITY, ("POSCO Holdings", "MinRes", "Wodgina", "Mt Marion", "spodumene")),
    Round247DeepSubArchetype("Non-China polysilicon", E2RArchetype.NON_CHINA_POLYSILICON_OPTIONALITY, ("OCI Holdings", "OCI TerraSus", "Texas expansion", "SpaceX unconfirmed report")),
    Round247DeepSubArchetype("Battery material contract break", E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK, ("L&F", "Tesla 4680", "contract value collapse", "actual call-off failure")),
)


ROUND247_CASE_CANDIDATES: tuple[Round247CaseCandidate, ...] = (
    Round247CaseCandidate(
        case_id="r4_loop11_korea_zinc_critical_minerals_governance",
        symbol="010130",
        company_name="Korea Zinc",
        primary_archetype=E2RArchetype.CRITICAL_MINERALS_SUPPLY_CHAIN,
        secondary_archetypes=(E2RArchetype.STRATEGIC_METALS_DILUTION_GOVERNANCE, E2RArchetype.GOVERNANCE_DILUTION_EVENT, E2RArchetype.STRATEGIC_MATERIALS_WITH_GOVERNANCE_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate_governance_watch",
        stage1_date=date(2024, 9, 1),
        stage2_date=date(2026, 3, 12),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 12, 16),
        stage3_decision="critical_minerals_project_is_stage2_until_fid_offtake_margin_fcf_dilution_and_governance_clear",
        stage4b_status="4B-watch-if-strategic-minerals-price-first",
        hard_4c_confirmed=False,
        evidence_fields=("tennessee_critical_minerals_refinery_7_4bn_usd", "planned_output_540k_tons", "eleven_critical_minerals", "antimony_gallium_germanium", "rare_earth_data_center_waste_talks", "2025_op_1_2tn_krw"),
        red_flag_fields=("share_issue_1_94bn_usd", "share_issue_vs_project_value_26_2pct", "new_investor_stake_10pct", "governance_battle", "injunction_event_minus_13pct", "offtake_fcf_unconfirmed"),
        price_data_source="Reuters critical-minerals / governance / share-issuance anchors",
        reported_price_anchor="injunction -13%; court rejection relief +5%; YoungPoong -10.5%",
        reported_return_anchor="$7.4B project, 540k tons output, 11 critical minerals, 2025 OP 1.2T KRW",
        mfe_1d=5.0,
        mae_1d=-13.0,
        mae_1d_secondary=-10.5,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"stage2_window": "2025-12_to_2026-03", "us_smelter_project_value_usd_bn": 7.4, "planned_output_tons": 540000.0, "critical_minerals_count": 11.0, "target_margin_low_pct": 17.0, "target_margin_high_pct": 19.0, "planned_construction_start": "early_2027", "planned_operation_year": 2030, "operating_profit_2025_krw_trn": 1.2, "share_issue_revised_krw_trn": 2.833, "share_issue_revised_usd_bn": 1.94, "share_issue_vs_project_value_pct": 26.2, "new_investor_stake_pct": 10.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_governance_watch",
        rerating_result="unknown",
        round_rerating_label="strategic_minerals_project_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_evidence_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Strategic minerals are Stage 2; FID/offtake/margin/FCF and governance/dilution must clear before Green.",
    ),
    Round247CaseCandidate(
        case_id="r4_loop11_lotte_hd_petrochemical_restructuring",
        symbol="011170/HD_Hyundai_Chemical",
        company_name="Lotte Chemical / HD Hyundai Chemical",
        primary_archetype=E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING,
        secondary_archetypes=(E2RArchetype.PETROCHEMICAL_RESTRUCTURING_KOREA, E2RArchetype.CHEMICAL_SPREAD_KOREA, E2RArchetype.COMMODITY_PRICE_4C_OVERLAY),
        case_type="failed_rerating",
        round_case_type="failed_rerating_restructuring_relief",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2026, 2, 24),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="restructuring_approval_is_relief_until_spread_opm_fcf_debt_and_funding_cost_confirm",
        stage4b_status="4B-watch-if-restructuring-basket-rally",
        hard_4c_confirmed=False,
        evidence_fields=("daesan_ncc_1_1mn_tpy_shutdown", "shutdown_duration_three_years", "support_package_over_2tn_krw", "capital_increase_1_2tn_krw", "national_ncc_capacity_cut_3_7mn_tpy"),
        red_flag_fields=("china_middle_east_oversupply", "spread_recovery_unconfirmed", "opm_fcf_unconfirmed", "debt_funding_cost_watch", "capacity_cut_without_spread_recovery"),
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
        extra_price_metrics={"plan_submitted_date": "2025-11-26", "daesan_ncc_capacity_mn_tpy": 1.1, "shutdown_duration_years": 3.0, "capital_increase_krw_trn": 1.2, "each_parent_injection_krw_bn": 600.0, "government_support_package_krw_trn": 2.0, "utility_cost_savings_krw_bn": 115.0, "rnd_funding_krw_bn": 26.0, "equity_split_after_restructuring": "50:50", "target_capacity_cut_national_mn_tpy": 3.7, "industry_capacity_cut_goal_pct": 25.0},
        score_price_alignment="false_positive_score",
        round_alignment_label="failed_rerating_then_restructuring_watch",
        rerating_result="no_rerating",
        round_rerating_label="petrochemical_restructuring_relief",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_relief_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Capacity shutdown/support is Stage 2 relief; spread, OPM and FCF recovery required for Green.",
    ),
    Round247CaseCandidate(
        case_id="r4_loop11_yncc_standalone_ncc_credit_watch",
        symbol="DL_Chemical/Hanwha_Solutions_exposure",
        company_name="Yeochun NCC / DL Chemical / Hanwha Solutions exposure",
        primary_archetype=E2RArchetype.STANDALONE_NCC_CREDIT_BREAK,
        secondary_archetypes=(E2RArchetype.PETROCHEMICAL_CAPACITY_RESTRUCTURING, E2RArchetype.CHEMICAL_SPREAD_KOREA, E2RArchetype.COMMODITY_PRICE_4C_OVERLAY),
        case_type="failed_rerating",
        round_case_type="4C-watch",
        stage1_date=date(2025, 8, 1),
        stage2_date=None,
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 8, 27),
        stage3_decision="weak_financials_and_forced_restructuring_are_not_positive_evidence",
        stage4b_status="not_applicable_4C-watch",
        hard_4c_confirmed=False,
        evidence_fields=("yncc_debt_to_equity_249pct", "third_largest_ethylene_producer", "possible_shutdown_one_or_two_crackers", "no3_cracker_shut_august_2025"),
        red_flag_fields=("standalone_cracker_credit_break", "weak_financials", "lack_of_integration", "forced_shutdown_risk", "shaheen_new_supply_overhang"),
        price_data_source="Reuters petrochemical overhaul / YNCC credit-risk anchor",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="debt/equity 249%, one or two cracker shutdown risk, No.3 cracker already shut",
        mfe_1d=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"yncc_debt_to_equity_1h2025_pct": 249.0, "yncc_position": "third_largest_south_korean_ethylene_producer", "possible_shutdown": "one_or_two_of_three_crackers", "no3_cracker_status": "shut_in_August_2025", "national_capacity_cut_target_mn_tpy": "2.7-3.7", "national_capacity_cut_equivalent_pct": 25.0, "naphtha_feedstock_share_for_ethylene_pct": 82.0, "shaheen_new_supply_mn_tpy": 1.8},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break_watch",
        rerating_result="thesis_break",
        round_rerating_label="standalone_NCC_credit_risk",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="4C_watch",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Weak financials and standalone NCC exposure require 4C-watch, not restructuring Green.",
    ),
    Round247CaseCandidate(
        case_id="r4_loop11_hyundai_posco_steel_tariff_two_sided",
        symbol="004020/005490",
        company_name="Hyundai Steel / POSCO Holdings",
        primary_archetype=E2RArchetype.STEEL_ANTIDUMPING_POLICY_RELIEF,
        secondary_archetypes=(E2RArchetype.STEEL_TARIFF_EXPORT_RISK, E2RArchetype.COMMODITY_PRICE_EVENT_PREMIUM, E2RArchetype.EVENT_PREMIUM),
        case_type="event_premium",
        round_case_type="event_premium_4C-watch",
        stage1_date=date(2024, 1, 1),
        stage2_date=date(2025, 2, 20),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=date(2025, 6, 2),
        stage3_decision="domestic_anti_dumping_relief_is_stage2_until_plate_spread_export_margin_utilization_and_fcf_confirm",
        stage4b_status="4B-watch-if-policy-relief-rally",
        hard_4c_confirmed=False,
        evidence_fields=("korea_antidumping_tariff_27_91_to_38_02pct", "chinese_steel_imports_10_4bn_usd", "hyundai_steel_relief_plus_5_8pct", "posco_holdings_relief_plus_3_9pct"),
        red_flag_fields=("us_tariff_threat_25_to_50pct", "hyundai_tariff_threat_minus_5_1pct", "posco_tariff_threat_minus_3_2pct", "export_margin_risk", "policy_relief_only"),
        price_data_source="Reuters / WSJ tariff-policy and event-return anchors",
        reported_price_anchor="anti-dumping relief: Hyundai +5.8%, POSCO +3.9%; U.S. tariff threat: Hyundai -5.1%, POSCO -3.2%",
        reported_return_anchor="Korea anti-dumping 27.91%-38.02%; Chinese steel import share 49%",
        mfe_1d=5.8,
        mae_1d=-5.1,
        mae_1d_secondary=-3.2,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"korea_antidumping_tariff_pct": "27.91-38.02", "chinese_steel_imports_2024_usd_bn": 10.4, "chinese_share_of_korea_steel_imports_pct": 49.0, "hyundai_steel_relief_mfe_pct": 5.8, "posco_holdings_relief_mfe_pct": 3.9, "kospi_same_context_pct": -0.7, "hyundai_relative_outperformance_pp": 6.5, "posco_relative_outperformance_pp": 4.6, "us_tariff_threat_pct": "25_to_50", "hyundai_tariff_threat_mae_pct": -5.1, "posco_tariff_threat_mae_pct": -3.2, "kospi_tariff_threat_context_pct": -0.2},
        score_price_alignment="price_moved_without_evidence",
        round_alignment_label="event_premium_tariff_4c_watch",
        rerating_result="event_premium",
        round_rerating_label="steel_policy_relief_with_export_risk",
        stage_failure_type="false_yellow",
        round_stage_failure_label="policy_stage2_not_green",
        price_validation_status="reported_event_anchor_not_full_ohlc",
        notes="Anti-dumping relief helps domestic spread but export tariff risk blocks Green until spread/margin/FCF confirm.",
    ),
    Round247CaseCandidate(
        case_id="r4_loop11_lg_chem_toyota_cathode_derisking",
        symbol="051910",
        company_name="LG Chem",
        primary_archetype=E2RArchetype.CATHODE_SUPPLY_CHAIN_DERISKING,
        secondary_archetypes=(E2RArchetype.CATHODE_LONG_CONTRACT_VISIBILITY, E2RArchetype.BATTERY_MATERIALS_CAPEX_OVERHEAT),
        case_type="success_candidate",
        round_case_type="success_candidate",
        stage1_date=date(2025, 1, 1),
        stage2_date=date(2025, 9, 9),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="ownership_derisking_is_stage2_until_cathode_volume_customer_offtake_opm_and_fcf_confirm",
        stage4b_status="4B-watch-if-China-exposure-derisking-rally",
        hard_4c_confirmed=False,
        evidence_fields=("toyota_tsusho_25pct_stake", "huayou_cobalt_stake_reduced_49_to_24pct", "china_exposure_reduction", "south_korea_cathode_plant"),
        red_flag_fields=("cathode_volume_unconfirmed", "customer_offtake_unconfirmed", "opm_fcf_unconfirmed", "battery_material_demand_slowdown_risk"),
        price_data_source="Reuters ownership-structure anchor",
        reported_price_anchor="stock OHLC unavailable",
        reported_return_anchor="Toyota Tsusho 25%; Huayou Cobalt stake 49% -> 24%",
        mfe_1d=None,
        mae_1d=None,
        mae_1d_secondary=None,
        stage2_price_anchor=None,
        stage3_price_anchor=None,
        stage4b_price_anchor=None,
        stage4c_price_anchor=None,
        extra_price_metrics={"toyota_tsusho_stake_pct": 25.0, "huayou_stake_before_pct": 49.0, "huayou_stake_after_pct": 24.0, "huayou_stake_reduction_pp": -25.0, "huayou_stake_reduction_relative_pct": -51.0},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate",
        rerating_result="unknown",
        round_rerating_label="cathode_supply_chain_derisking_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_evidence_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="Ownership derisking is Stage 2; cathode volume, customer offtake, OPM and FCF required before Green.",
    ),
    Round247CaseCandidate(
        case_id="r4_loop11_posco_minres_lithium_resource_security",
        symbol="005490",
        company_name="POSCO Holdings / MinRes lithium JV",
        primary_archetype=E2RArchetype.LITHIUM_RESOURCE_SECURITY,
        secondary_archetypes=(E2RArchetype.LITHIUM_RESOURCE_SECURITY_KOREA, E2RArchetype.LITHIUM_CYCLE_OVERLAY),
        case_type="success_candidate",
        round_case_type="success_candidate_cyclical_watch",
        stage1_date=date(2023, 1, 1),
        stage2_date=date(2025, 11, 11),
        stage3_date=None,
        stage4b_date=None,
        stage4c_date=None,
        stage3_decision="resource_security_is_stage2_until_lithium_hydroxide_margin_offtake_economics_and_downstream_fcf_confirm",
        stage4b_status="4B-watch-if-lithium-rebound-rally",
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
        extra_price_metrics={"transaction_value_usd_mn": 765.0, "posco_indirect_stake_pct": 15.0, "assets": ["Wodgina", "Mt Marion"], "minres_event_mfe_pct": 10.8, "spodumene_peak_2022_usd_per_t": 6000.0, "spodumene_low_2025_usd_per_t": 610.0, "spodumene_drawdown_peak_to_low_pct": -89.8, "spodumene_rebound_610_to_880_pct": 44.3, "spodumene_880_vs_peak_pct": -85.3},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_cyclical_watch",
        rerating_result="unknown",
        round_rerating_label="lithium_resource_security_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_watch_success_not_green",
        price_validation_status="posco_stock_ohlc_unavailable_after_deep_search",
        notes="Resource security is Stage 2; downstream margin, offtake economics and FCF required before Green.",
    ),
    Round247CaseCandidate(
        case_id="r4_loop11_oci_non_china_polysilicon_spacex_watch",
        symbol="010060",
        company_name="OCI Holdings / OCI TerraSus",
        primary_archetype=E2RArchetype.NON_CHINA_POLYSILICON_OPTIONALITY,
        secondary_archetypes=(E2RArchetype.POLYSILICON_NON_CHINA_SUPPLY_OPTION, E2RArchetype.POLYSILICON_REPORT_NOT_CONTRACT, E2RArchetype.COMMODITY_PRICE_EVENT_PREMIUM, E2RArchetype.EVENT_PREMIUM),
        case_type="success_candidate",
        round_case_type="success_candidate_event_premium",
        stage1_date=date(2025, 6, 7),
        stage2_date=date(2025, 6, 7),
        stage3_date=None,
        stage4b_date=date(2026, 4, 14),
        stage4c_date=None,
        stage3_decision="non_china_polysilicon_capacity_is_stage2_but_spacex_report_is_unconfirmed_event_premium",
        stage4b_status="4B-watch-unconfirmed-media-report",
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
        extra_price_metrics={"us_investment_usd_bn": 1.2, "target_capacity_gw": 10.0, "target_year": 2027, "capacity_equivalent": "roughly_10_nuclear_power_plants", "spacex_contract_status": "unconfirmed_media_report", "spacex_response": "no_response_reported", "oci_response": "could_not_confirm_report", "spacex_solar_satellite_constellation": 1000000},
        score_price_alignment="unknown",
        round_alignment_label="success_candidate_event_premium",
        rerating_result="unknown",
        round_rerating_label="non_China_polysilicon_watch",
        stage_failure_type="stage2_watch_success",
        round_stage_failure_label="stage2_evidence_not_green",
        price_validation_status="price_data_unavailable_after_deep_search",
        notes="U.S. expansion is Stage 2; unconfirmed SpaceX report is event premium until contract/offtake/margin/FCF confirm.",
    ),
    Round247CaseCandidate(
        case_id="r4_loop11_lnf_tesla_cathode_contract_hard_4c",
        symbol="066970",
        company_name="L&F",
        primary_archetype=E2RArchetype.BATTERY_MATERIAL_CONTRACT_QUALITY_BREAK,
        secondary_archetypes=(E2RArchetype.CONTRACT_QUALITY_BREAK, E2RArchetype.BATTERY_CONTRACT_CANCELLATION_4C, E2RArchetype.CONTRACT_CANCELLATION_CUSTOMER_STRATEGY_RISK),
        case_type="4c_thesis_break",
        round_case_type="4C-thesis-break",
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
        extra_price_metrics={"initial_contract_value_usd_bn": 2.9, "revised_contract_value_usd": 7386.0, "contract_value_drawdown_pct": -99.999745, "contract_period": "2024-2025", "product": "high-nickel cathode materials for Tesla 4680 cells", "reason_context": ["4680_yield_issue", "EV_demand_slowdown", "Cybertruck_demand_disappointment"]},
        score_price_alignment="evidence_good_but_price_failed",
        round_alignment_label="thesis_break",
        rerating_result="thesis_break",
        round_rerating_label="battery_material_contract_quality_failure",
        stage_failure_type="should_have_been_red",
        round_stage_failure_label="hard_4C",
        price_validation_status="reported_contract_anchor_not_full_ohlc",
        notes="Customer name and contract headline cannot be Green without actual call-off and volume/margin conversion.",
    ),
)


def round247_case_records() -> tuple[E2RCaseRecord, ...]:
    records: list[E2RCaseRecord] = []
    for candidate in ROUND247_CASE_CANDIDATES:
        record = E2RCaseRecord(
            case_id=candidate.case_id,
            symbol=candidate.symbol,
            company_name=candidate.company_name,
            market="KR",
            sector_raw=candidate.primary_archetype.value,
            primary_archetype=candidate.primary_archetype,
            secondary_archetypes=candidate.secondary_archetypes,
            expected_group=candidate.expected_group,
            large_sector=ROUND247_LARGE_SECTOR,
            case_type=candidate.case_type,
            stage1_date=candidate.stage1_date,
            stage2_date=candidate.stage2_date,
            stage3_date=candidate.stage3_date,
            stage4b_date=candidate.stage4b_date,
            stage4c_date=candidate.stage4c_date,
            evidence_summary=(
                "Round247 R4 Loop-11 materials/spread/strategic-resources price validation case. "
                "Calibration-only; not candidate-generation input."
            ),
            stage1_evidence=candidate.evidence_fields,
            stage2_evidence=candidate.evidence_fields if candidate.stage2_date else (),
            stage3_evidence=tuple(field for field in candidate.evidence_fields if any(token in field for token in ("spread", "offtake", "fcf", "capacity", "contract", "margin", "output", "stake"))),
            stage4b_evidence=tuple(field for field in (*candidate.evidence_fields, *candidate.red_flag_fields) if any(token in field for token in ("event", "unconfirmed", "headline", "governance", "rally", "resource"))),
            stage4c_evidence=tuple(field for field in (*candidate.red_flag_fields, *candidate.evidence_fields) if any(token in field for token in ("collapse", "shutdown", "dilution", "failure", "weak", "oversupply", "tariff", "unconfirmed", "credit", "share_issue"))),
            must_have_fields=ROUND247_GREEN_REQUIRED_FIELDS,
            red_flag_fields=candidate.red_flag_fields,
            key_evidence_fields=candidate.evidence_fields,
            false_positive_reason="; ".join(candidate.red_flag_fields) if candidate.case_type in {"failed_rerating", "event_premium", "4c_thesis_break", "overheat"} else None,
            score_price_alignment=candidate.score_price_alignment,
            rerating_result=candidate.rerating_result,
            stage_failure_type=candidate.stage_failure_type,
            price_pattern=candidate.stage3_decision,
            score_weight_hint={f"{item.axis}_delta": float(item.points) for item in ROUND247_SCORE_ADJUSTMENTS},
            green_guardrails=(
                "production_scoring_changed_false",
                "candidate_generation_input_false",
                "shadow_weight_only_true",
                "full_ohlc_complete_false",
                "price_validation_partial_with_reported_price_anchors",
                "do_not_invent_ohlc_stage_prices_spreads_offtakes_or_fcf",
                "do_not_treat_commodity_strategic_mineral_policy_restructuring_or_unconfirmed_media_as_green",
                *ROUND247_GREEN_REQUIRED_FIELDS,
                *ROUND247_GREEN_FORBIDDEN_PATTERNS,
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
                price_data_available=(
                    candidate.mfe_1d is not None
                    or candidate.mae_1d is not None
                    or candidate.mae_1d_secondary is not None
                    or candidate.stage2_price_anchor is not None
                    or candidate.stage3_price_anchor is not None
                    or candidate.stage4b_price_anchor is not None
                    or candidate.stage4c_price_anchor is not None
                ),
                stage_dates_confidence=0.85 if candidate.stage2_date or candidate.stage4c_date else 0.65,
            ),
        )
        record.validate()
        records.append(record)
    return tuple(records)


def round247_case_rows() -> tuple[dict[str, str], ...]:
    return tuple(
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
            "mae_1d_secondary": _float_text(candidate.mae_1d_secondary),
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
        for candidate in ROUND247_CASE_CANDIDATES
    )


def round247_score_adjustment_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND247_SCORE_ADJUSTMENTS)


def round247_shadow_weight_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND247_SHADOW_WEIGHT_ROWS)


def round247_deep_sub_archetype_rows() -> tuple[dict[str, str], ...]:
    return tuple(item.as_row() for item in ROUND247_DEEP_SUB_ARCHETYPES)


def round247_price_validation_field_rows() -> tuple[dict[str, str], ...]:
    return tuple({"field": field, "required_for_round247_price_validation": "true"} for field in ROUND247_PRICE_VALIDATION_FIELDS)


def round247_target_alias_rows() -> tuple[dict[str, str], ...]:
    return tuple({"round247_label": label, "canonical_archetype": canonical} for label, canonical in ROUND247_REQUIRED_TARGET_ALIASES.items())


def round247_summary() -> dict[str, int | bool | str]:
    cases = ROUND247_CASE_CANDIDATES
    return {
        "source_round": ROUND247_SOURCE_ROUND_PATH,
        "round_id": ROUND247_ROUND_ID,
        "large_sector": ROUND247_LARGE_SECTOR,
        "case_candidate_count": len(cases),
        "success_candidate_count": sum(1 for case in cases if case.case_type == "success_candidate"),
        "event_premium_count": sum(1 for case in cases if case.case_type == "event_premium"),
        "failed_rerating_count": sum(1 for case in cases if case.case_type == "failed_rerating"),
        "hard_4c_case_count": sum(1 for case in cases if case.hard_4c_confirmed),
        "stage3_case_count": sum(1 for case in cases if case.stage3_date is not None),
        "stage4b_watch_count": sum(1 for case in cases if "4B-watch" in case.stage4b_status),
        "watch_4c_count": sum(1 for case in cases if case.stage4c_date is not None),
        "evidence_good_but_price_failed_count": sum(1 for case in cases if case.score_price_alignment == "evidence_good_but_price_failed"),
        "price_moved_without_evidence_count": sum(1 for case in cases if case.score_price_alignment == "price_moved_without_evidence"),
        "reported_price_anchor_count": sum(1 for case in cases if case.price_validation_status != "price_data_unavailable_after_deep_search"),
        "target_archetype_count": len(ROUND247_REQUIRED_TARGET_ALIASES),
        "deep_sub_archetype_count": len(ROUND247_DEEP_SUB_ARCHETYPES),
        "shadow_weight_row_count": len(ROUND247_SHADOW_WEIGHT_ROWS),
        "price_validation_completed": "partial_with_reported_price_anchors",
        "full_ohlc_complete": False,
        "production_scoring_changed": False,
        "candidate_generation_input": False,
        "shadow_weight_only": True,
        "hard_4c_confirmed": any(case.hard_4c_confirmed for case in cases),
    }


def round247_audit_payload() -> dict[str, object]:
    return {
        "source_round": ROUND247_SOURCE_ROUND_PATH,
        "round_id": ROUND247_ROUND_ID,
        "large_sector": ROUND247_LARGE_SECTOR,
        "summary": round247_summary(),
        "target_aliases": dict(ROUND247_REQUIRED_TARGET_ALIASES),
        "green_required_fields": list(ROUND247_GREEN_REQUIRED_FIELDS),
        "green_forbidden_patterns": list(ROUND247_GREEN_FORBIDDEN_PATTERNS),
        "stage4b_watch_triggers": list(ROUND247_STAGE4B_WATCH_TRIGGERS),
        "hard_4c_gates": list(ROUND247_HARD_4C_GATES),
        "score_adjustments": list(round247_score_adjustment_rows()),
        "shadow_weights": list(round247_shadow_weight_rows()),
        "deep_sub_archetypes": list(round247_deep_sub_archetype_rows()),
        "case_ids": [case.case_id for case in ROUND247_CASE_CANDIDATES],
        "what_not_to_change": [
            "do_not_apply_to_production_scoring_yet",
            "do_not_use_round247_cases_as_candidate_generation_input",
            "do_not_lower_stage3_green_thresholds",
            "do_not_treat_commodity_strategic_mineral_policy_restructuring_or_unconfirmed_media_as_green",
            "do_not_invent_full_ohlc_or_stage_prices_when_only_reported_anchors_exist",
        ],
    }


def render_round247_summary_markdown() -> str:
    summary = round247_summary()
    lines = [
        "# Round 247 R4 Loop 11 Materials Spread Strategic Resources Price Validation",
        "",
        "This pack is calibration-only. Production scoring and candidate generation are unchanged.",
        "",
        "## Summary",
        "",
        f"- source_round: {summary['source_round']}",
        f"- round_id: {summary['round_id']}",
        f"- large_sector: {summary['large_sector']}",
        f"- cases: {summary['case_candidate_count']}",
        f"- success_candidate: {summary['success_candidate_count']}",
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
    for case in ROUND247_CASE_CANDIDATES:
        lines.append(
            "| "
            + " | ".join(
                (
                    case.case_id,
                    case.company_name,
                    case.round_case_type,
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
            "- Korea Zinc is strategic-minerals Stage 2 plus governance/dilution watch, not Green before FID, offtake, margin and FCF.",
            "- Petrochemical restructuring is relief unless product spread, OPM and FCF recover.",
            "- YNCC is standalone NCC credit 4C-watch, not a restructuring winner.",
            "- Steel policy is two-sided: domestic anti-dumping relief and export tariff risk must both be considered.",
            "- LG Chem/Toyota and POSCO/MinRes are Stage 2 supply-chain/resource-security cases, not Green before margin and offtake.",
            "- OCI is Stage 2 optionality, while the SpaceX item is unconfirmed media/event premium.",
            "- L&F remains the hard 4C anchor for customer-name/material-contract false positives.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round247_green_gate_review_markdown() -> str:
    lines = [
        "# Round 247 R4 Green Gate Review",
        "",
        "Do not apply these weights to production scoring yet.",
        "",
        "R4 Stage 3-Green is not `commodity price up`, `strategic minerals`, `tariff relief`, `restructuring`, or `unconfirmed customer media`. It requires spread, offtake, cost curve, contract quality, FCF and risk clearance.",
        "",
        "## Required Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND247_GREEN_REQUIRED_FIELDS)
    lines.extend(["", "## Forbidden Patterns", ""])
    lines.extend(f"- {field}" for field in ROUND247_GREEN_FORBIDDEN_PATTERNS)
    lines.extend(["", "## Shadow Score Adjustments", "", "| axis | direction | points | reason |", "|---|---|---:|---|"])
    for adjustment in ROUND247_SCORE_ADJUSTMENTS:
        lines.append(f"| {adjustment.axis} | {adjustment.direction} | {adjustment.points} | {adjustment.reason} |")
    lines.extend(
        [
            "",
            "## Easy Examples",
            "- `anti-dumping tariff relief` is Stage 2 attention until steel spread and export margin confirm.",
            "- `SpaceX supply talk` is event premium while the customer and contract are unconfirmed.",
            "- `Tesla customer name` is not Green if the actual contract value collapses.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_round247_stage4b_4c_review_markdown() -> str:
    lines = ["# Round 247 R4 4B / 4C Review", "", "## 4B Watch Triggers", ""]
    lines.extend(f"- {field}" for field in ROUND247_STAGE4B_WATCH_TRIGGERS)
    lines.extend(["", "## Hard 4C Gates", ""])
    lines.extend(f"- {field}" for field in ROUND247_HARD_4C_GATES)
    lines.extend(["", "## Case Review", "", "| case | 4B status | hard 4C | interpretation |", "|---|---|---|---|"])
    for case in ROUND247_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.stage4b_status} | {str(case.hard_4c_confirmed).lower()} | {case.notes} |")
    return "\n".join(lines) + "\n"


def render_round247_price_validation_plan_markdown() -> str:
    lines = [
        "# Round 247 R4 Price Validation Plan",
        "",
        "- price_validation_completed: partial_with_reported_price_anchors",
        "- full_ohlc_complete: false",
        "- Do not invent OHLC, stage prices, spreads, offtake, MFE, or MAE where raw adjusted daily prices are unavailable.",
        "",
        "## Backfill Fields",
        "",
    ]
    lines.extend(f"- {field}" for field in ROUND247_PRICE_VALIDATION_FIELDS)
    lines.extend(["", "## Case Anchors", "", "| case | data source | reported anchor | status |", "|---|---|---|---|"])
    for case in ROUND247_CASE_CANDIDATES:
        lines.append(f"| {case.case_id} | {case.price_data_source} | {case.reported_return_anchor} | {case.price_validation_status} |")
    return "\n".join(lines) + "\n"


def write_round247_r4_loop11_reports(
    output_directory: str | Path = ROUND247_DEFAULT_OUTPUT_DIRECTORY,
    cases_path: str | Path = ROUND247_DEFAULT_CASES_PATH,
    audit_path: str | Path = ROUND247_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths = {
        "cases": write_case_library(round247_case_records(), cases_path),
        "audit": _write_json(round247_audit_payload(), audit_path),
        "summary": output / "round247_r4_loop11_price_validation_summary.md",
        "case_matrix": output / "round247_r4_loop11_case_matrix.csv",
        "target_aliases": output / "round247_r4_loop11_target_aliases.csv",
        "score_adjustments": output / "round247_r4_loop11_score_adjustments.csv",
        "shadow_weights": output / "round247_r4_loop11_shadow_weights.csv",
        "deep_sub_archetypes": output / "round247_r4_loop11_deep_sub_archetypes.csv",
        "price_validation_fields": output / "round247_r4_loop11_price_validation_fields.csv",
        "green_gate_review": output / "round247_r4_loop11_green_gate_review.md",
        "price_validation_plan": output / "round247_r4_loop11_price_validation_plan.md",
        "stage4b_4c_review": output / "round247_r4_loop11_stage4b_4c_review.md",
    }
    paths["summary"].write_text(render_round247_summary_markdown(), encoding="utf-8")
    _write_csv(round247_case_rows(), paths["case_matrix"])
    _write_csv(round247_target_alias_rows(), paths["target_aliases"])
    _write_csv(round247_score_adjustment_rows(), paths["score_adjustments"])
    _write_csv(round247_shadow_weight_rows(), paths["shadow_weights"])
    _write_csv(round247_deep_sub_archetype_rows(), paths["deep_sub_archetypes"])
    _write_csv(round247_price_validation_field_rows(), paths["price_validation_fields"])
    paths["green_gate_review"].write_text(render_round247_green_gate_review_markdown(), encoding="utf-8")
    paths["price_validation_plan"].write_text(render_round247_price_validation_plan_markdown(), encoding="utf-8")
    paths["stage4b_4c_review"].write_text(render_round247_stage4b_4c_review_markdown(), encoding="utf-8")
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
